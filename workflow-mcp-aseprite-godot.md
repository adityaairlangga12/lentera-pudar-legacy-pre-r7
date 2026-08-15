# Workflow MCP Aseprite + MCP Godot untuk 2D Pixel Art RPG
### Dokumen referensi konsolidasi — untuk pembelajaran agent (Antigravity)

---

## 0. Konteks & Prinsip Dasar

Dokumen ini disusun setelah 4 percobaan workflow sebelumnya gagal karena pendekatan **full-AI-generate tanpa gerbang validasi** (langsung generate end-to-end besar, tanpa checkpoint di antara tahap). Prinsip inti yang menggantikannya:

1. **Observability sebelum kemampuan.** Tool untuk "melihat status/hasil saat ini" harus ada dan berfungsi SEBELUM tool untuk "membuat/mengubah sesuatu" yang lebih kompleks dibangun.
2. **Granular, bukan bulk.** Satu tool call = satu aksi kecil yang bisa gagal secara terisolasi dan mudah di-rollback. Hindari tool "do everything at once".
3. **Bertahap, tidak lompat tier.** Setiap tahap harus stabil (berhasil berulang tanpa gagal, idealnya 5-10x berturut-turut) sebelum lanjut ke tahap berikutnya.
4. **Tidak ada jaminan hasil akhir sempurna.** Yang bisa dijamin adalah: kegagalan akan selalu terlihat di titik kecil (bukan menumpuk jadi kekacauan besar di akhir), sehingga bisa didiagnosis dan diperbaiki cepat.
5. **AI (LLM) tidak "melihat" secara default.** Baik di Aseprite maupun Godot, LLM bekerja buta terhadap hasil visual kecuali secara eksplisit diberi tool untuk capture & return gambar sebagai vision input. Ini bukan fitur opsional — ini fondasi.

---

## 0A. Versi Tool yang Dipakai (per Agustus 2026)

| Tool | Versi | Catatan kompatibilitas |
|---|---|---|
| Blender | 5.2 LTS | LTS, maintained sampai Juli 2028. **Perhatian:** API Python untuk properti modifier Geometry Nodes berubah di rilis ini — uji ulang tool/addon custom yang menyentuh Geometry Nodes sebelum dipakai produksi. |
| Godot | 4.7.1 | Godot 4.6 mengembalikan dukungan IK + menjadikan Jolt Physics default; 4.7 melengkapi platform/editor. Versi ini sudah mencakup penuh fondasi IK (Bagian 2.1) tanpa workaround. |
| Aseprite | 1.3.18.2 | Rilis stabil jalur 1.3.x, API CLI & Lua scripting konsisten dengan daftar tool Tier 1-4. |
| Antigravity IDE | 2.5.5 (sudah versi terbaru untuk IDE — jangan disamakan dengan "Antigravity 2.0" agent orchestrator yang punya jalur versi terpisah, saat ini di 2.8.x) | **Perhatian:** ada laporan bug aktif per Agustus 2026 — perubahan lama bisa tersangkut status loading terus-menerus, dan model usage terus-menerus fetching tanpa selesai. Kalau loop MCP terasa hang, cek dulu apakah ini bug IDE yang sedang berjalan, jangan langsung asumsikan kesalahan arsitektur MCP. |

---

## 1. Arsitektur Gabungan

**Jalur A (2D flat sprite, default — 2 MCP):**
```
[Reference/Concept source]  (image-gen model, referensi foto/video, atau gambar manual)
            ↓
[MCP ASEPRITE]  →  Asset generation: pixelization, palette, part-slicing, anchor metadata
            ↓  (export JSON metadata: anchor point, part boundaries, palette)
[MCP GODOT]     →  Scene assembly, Skeleton2D rig, IK, physics-based secondary motion,
                    procedural locomotion, testing headless, screenshot feedback
            ↓
[Vision feedback loop]  →  LLM melihat hasil render → evaluasi → adjust parameter → re-test
```

**Jalur B (3D rig + pixelation shader, untuk 8-direction — 3 MCP):**
```
[Reference/Concept source]  (image-gen model, referensi foto/video, atau gambar manual)
            ↓
[MCP BLENDER]   →  Modeling low-poly, rigging (Armature), skinning, texturing flat/vertex-color
            ↓  (export glTF 2.0 + JSON metadata: bone hierarchy, anchor point)
[MCP GODOT]     →  Import mesh 3D, Camera3D Orthogonal + SubViewport pixelation, Skeleton3D IK,
                    physics-based secondary motion, procedural locomotion, testing headless,
                    screenshot feedback
            ↓
[Vision feedback loop]  →  LLM melihat hasil render → evaluasi → adjust parameter → re-test
```
**MCP Aseprite tetap dipakai di Jalur B**, tapi perannya bergeser: bukan lagi membuat body karakter (kini mesh 3D dari Blender), melainkan UI, icon, item, dan elemen 2D murni lain yang tidak butuh rotasi banyak arah (lihat Bagian 12).

**Pembagian tanggung jawab:**
- **MCP Aseprite** menangani segala sesuatu yang statis/artistik: tekstur, part sprite (Jalur A) atau UI/icon/item (Jalur B), palet, detail shading, monster kecil sederhana.
- **MCP Blender** (khusus Jalur B) menangani modeling low-poly, rigging, skinning, dan texturing dasar sebelum diserahkan ke Godot.
- **MCP Godot** menangani segala sesuatu yang bergerak/dinamis: rig (2D atau 3D tergantung jalur), IK, locomotion, fisika sekunder (rambut/jubah), testing runtime, dan — khusus Jalur B — render pipeline pixelation.

---

## 2. Teori Matematika & Fisika yang Relevan

Ini bagian yang membedakan hasil "smooth & hidup" dari hasil kaku/robotic. Semua ini diterapkan di layer MCP Godot — pada Skeleton2D untuk Jalur A, atau Skeleton3D untuk Jalur B (lihat Bagian 4 Tier 2B). Matematikanya identik di kedua jalur, hanya beda dimensi ruang (2D vs 3D); bukan Aseprite atau Blender yang menjalankan teori ini — kedua MCP itu hanya menghasilkan aset/rig mentah yang diserahkan ke Godot.

### 2.1 Inverse Kinematics (IK) — geometri & numerik

| Solver | Basis matematika | Kapan dipakai |
|---|---|---|
| **Two-bone IK** | Solusi analitik trigonometri (hukum cosinus) — langsung dapat jawaban eksak dalam 1 langkah | Limb sederhana (paha-betis-kaki, lengan) |
| **FABRIK** (Forward And Backward Reaching IK) | Iteratif, menggerakkan tiap sendi bergantian dari ujung ke pangkal lalu sebaliknya sampai konvergen | Chain panjang (tulang belakang, badan ular), konvergen cepat & smooth |
| **CCDIK** (Cyclic Coordinate Descent IK) | Iteratif, rotasi tiap bone satu per satu menuju target | Chain panjang dengan constraint sudut per-bone yang mudah diatur |
| **Spline IK** | Kurva Bezier/Catmull-Rom sebagai basis chain | Ekor, tentakel, elemen fleksibel panjang |

Godot 4.6 menyediakan IK sebagai modular modifier stack di atas `Skeleton2D`/`Skeleton3D` — pilih solver sesuai tabel di atas per chain, jangan pakai satu solver untuk semua kasus.

### 2.2 Gait Function — locomotion sebagai fungsi periodik

Model **inverted pendulum** (biomekanika berjalan manusia): tubuh berayun seperti pendulum terbalik di atas kaki tumpu.

```gdscript
# Per kaki, dengan phase_offset berbeda (kiri vs kanan = π radian)
foot_y_offset = amplitude * sin(phase)
foot_x_offset = stride_length * cos(phase)

# Body bob — frekuensi 2x siklus kaki karena badan naik di SETIAP kali kaki menapak
body_y_offset = bob_amplitude * abs(sin(2 * phase))
```

Parameter kunci: `amplitude` (tinggi angkat kaki), `stride_length` (panjang langkah), `frequency` (kecepatan siklus), `phase_offset` (π untuk gait 2 kaki bergantian).

### 2.3 Spring-Damper System (Hukum Hooke) — secondary motion

Untuk rambut, jubah, telinga, aksesoris — physically-based, bukan kurva preset statis:

```gdscript
force = -stiffness * (current_pos - rest_pos) - damping * velocity
velocity += force * delta
position += velocity * delta
```

Ini merespons kecepatan gerak karakter secara real-time (kalau karakter berhenti mendadak, rambut punya momentum dan menyusul — natural). Variasi "Velvet" (gerak mengayun, bukan spring murni) cocok untuk kain/jubah yang perlu terasa lebih berat/menggantung daripada memantul.

### 2.4 Verlet Integration — untuk cloth/rambut panjang yang lebih kompleks

Lebih stabil secara numerik dibanding Euler integration biasa untuk chain partikel:

```gdscript
new_pos = pos + (pos - prev_pos) * damping + acceleration * delta * delta
```

### 2.5 PD Controller (Proportional-Derivative) — transisi antar state gerak

Untuk transisi idle→walk→run agar tidak snap kaku:

```gdscript
error = target_value - current_value
output = Kp * error + Kd * (error - previous_error) / delta
```

### 2.6 Foot IK via Raycast — adaptasi ke permukaan tidak rata

Tembak raycast ke bawah dari posisi target kaki → titik hit permukaan jadi target IK aktual. Kaki otomatis menyesuaikan ke medan (lereng, tangga, batu) tanpa animasi terpisah per jenis medan.

### 2.7 Noise Functions — variasi organik non-repetitif

Perlin/Simplex noise untuk sway kecil (rambut, daun, api) yang tidak terasa berulang persis seperti sinus murni — memberi kesan "hidup" karena tidak pernah identik antar siklus.

### 2.8 Perspective & Direction Theory

- **Sudut pandang** — mayoritas top-down RPG (gaya Zelda) pakai 3/4 elevated top-down, bukan orthographic murni dari atas. Ini menentukan berapa sisi karakter yang perlu digambar unik.
- **Aturan mirroring 4-arah** — untuk animasi karakter top-down cukup 4 arah unik minimum, dan kecuali karakter punya lighting dramatis atau desain asimetris yang perlu akurat per arah, sprite menghadap samping bisa di-flip untuk kiri/kanan — jadi cukup 3 arah digambar/rig (depan, belakang, samping), arah ke-4 tinggal mirror.
- **Depth implikasi via sumbu Y** — pada sudut top-down, objek yang posisinya lebih rendah di layar diasumsikan lebih dekat ke kamera. Ini prinsip dasar di balik y-sort.
- **Y-sort (depth ordering)** — di Godot diaktifkan lewat "Y Sort Enabled" pada TileMap/Node2D, supaya karakter tampil benar di depan/belakang objek (pohon, bangunan) berdasarkan posisi Y. Tanpa ini, terjadi bug visual "menembus objek" walau animasi individual sudah sempurna.
- **Resolusi & skala native ditentukan di awal, tidak diubah di tengah jalan** — sprite top-down umumnya 8–32 pixel tinggi; pilih native resolution yang scale rapi ke resolusi layar target sejak awal proyek.

### 2.9 Anatomy Theory

- **Rasio kepala-ke-badan** menentukan gaya visual (chibi 2-3 kepala vs semi-realistis 4-6 kepala) — harus konsisten lintas SEMUA karakter dalam satu game, didefinisikan sebagai konstanta proyek bukan per-asset.
- **Hierarki sendi mengikuti anatomi asli**: hip→knee→ankle, shoulder→elbow→wrist. Chain IK di Godot harus dibangun mengikuti urutan ini persis agar `set_bone_constraint` (batas sudut) masuk akal secara biomekanik.
- **Pusat massa (center of mass)** ada di sekitar pinggul/perut bawah — ini titik acuan yang benar untuk body bob dan weight-shift, bukan titik tengah geometris sprite.
- **Personality lewat detail, bukan lewat proporsi** — meski total tinggi/proporsi sprite sama antar karakter (demi konsistensi rig), variasi personality tetap datang dari warna, mata, outline, pakaian, aksesoris.

### 2.10 Physiological / Biomechanics Theory

- **Fase gait**: *stance phase* (kaki menapak, menahan berat) vs *swing phase* (kaki mengayun bebas). Rasio durasi keduanya berubah sesuai kecepatan — jalan santai stance lebih lama, lari stance lebih pendek.
- **Bukan semua makhluk biped** — perlu gait template berbeda per tipe:
  - Quadruped: trot (pasangan kaki diagonal bergerak bersamaan) vs gallop (ritme asimetris)
  - Slime/blob: cukup squash-stretch periodik, tanpa logika kaki sama sekali
  - Makhluk terbang: tidak butuh foot-contact/raycast logic sama sekali, diganti hover/bob di udara
- **Idle bukan freeze** — napas halus (scale/offset kecil berperiode lambat di area dada) adalah baseline fisiologis minimum, tanpa ini karakter diam terlihat seperti patung/mati.

---

## 2A. Python Engineering Theory (Kekuatan MCP itu Sendiri)

Beda dari teori di atas — ini bukan soal visual, tapi soal apakah MCP kamu **robust** atau gampang collapse. Ini akar paling langsung dari 4 kegagalan sebelumnya, karena tool yang rapuh secara software akan gagal secara tidak terduga terlepas seberapa bagus teori animasinya.

- **Pydantic validation di setiap tool** — validasi parameter di pintu masuk sebelum eksekusi, supaya error ketahuan dari awal bukan menyebabkan crash setelah proses sudah jauh berjalan.
- **Async I/O untuk subprocess call** (ke Aseprite CLI, Godot headless) — MCP tidak boleh blocking, dan harus punya timeout jelas kalau proses eksternal hang.
- **Command pattern untuk undo/redo** — tiap aksi tersimpan sebagai objek command yang bisa di-reverse secara eksplisit.
- **State machine pattern eksplisit** untuk status rig/animasi (idle/walk/run/attack) — mencegah transisi ilegal, misal `attack` dipanggil sebelum rig selesai dibangun.
- **Strategy pattern untuk pemilihan IK solver** — `add_ik(chain, solver="fabrik")` mudah diganti solver tanpa rewrite besar.
- **Structured logging + exception hierarchy custom** — tiap kegagalan punya tipe error spesifik (`RigValidationError`, `AsepriteExportError`, `IKConvergenceError`, dst), bukan generic exception yang menyembunyikan akar masalah.
- **Unit test per tool secara terisolasi** — tiap tool harus lolos test sendiri sebelum dipanggil dalam alur besar oleh LLM.

---

## 3. Daftar Tool MCP Aseprite (Lengkap, dengan Tingkat Prioritas)

### Tier 1 — Fondasi (WAJIB, bangun & stabilkan duluan)
| Tool | Fungsi |
|---|---|
| `create_canvas(w, h, color_mode)` | Bikin kanvas baru |
| `get_canvas_info()` | Baca ukuran, mode warna, jumlah layer saat ini (verifikasi) |
| `add_layer(name)` / `list_layers()` | Kelola & cek layer |
| `set_pixel(x, y, color)` / `get_pixel(x, y)` | Baca-tulis pixel level dasar |
| `draw_line/rect/circle/fill(...)` | Primitif gambar |
| `save_file(path)` / `open_file(path)` | I/O dasar |
| `export_png(path, layer_filter)` | Export dengan opsi per-layer |
| `capture_canvas_as_image()` | **KRITIS** — return gambar kanvas sebagai vision input ke LLM |

### Tier 2 — Kualitas & Konsistensi
| Tool | Fungsi |
|---|---|
| `quantize_palette(n_colors, method, dither)` | Kuantisasi warna (median-cut/k-means/octree + Floyd-Steinberg) |
| `snap_to_palette(palette_id)` | Paksa konsisten satu palet proyek |
| `import_reference(path)` + `downscale_to_grid(w, h, method)` | Pipeline hybrid image-gen → pixel art |
| `outline_generate(mode, color)` | Outline otomatis |
| `undo()` / `redo()` / `get_history()` | Recovery kalau LLM salah gambar |
| `validate_canvas(rules)` | Cek aturan dasar (tidak ada pixel bocor, ukuran sesuai spec) |
| `clean_jaggies(strength)` | Fix pixel lepas sisa downscale |

### Tier 3 — Rigging & Jembatan ke Godot
| Tool | Fungsi |
|---|---|
| `set_anchor_point(name, x, y)` | Titik jangkar per part (foot_left, foot_right, pivot_center, weapon_hand) |
| `slice_into_parts(part_map)` | Potong sprite jadi part terpisah (head/torso/arm/leg) |
| `export_part_metadata(format="json")` | Export posisi/anchor/nama part → dibaca MCP Godot |
| `check_part_alignment(parts)` | Validasi origin tiap part konsisten sebelum dikirim ke Godot |
| `detect_silhouette_bounds()` | Cek bounding box tiap frame/part konsisten |
| `validate_proportions(head_to_body_ratio, tolerance)` | Cek rasio kepala-badan sesuai konstanta gaya visual proyek |
| `generate_directional_variant(base_sprite, direction, mirror=True)` | Generate arah ke-4 via mirroring dari 3 arah unik (depan/belakang/samping) |
| `set_native_resolution(w, h)` | Kunci resolusi native project di awal — dipanggil sekali, divalidasi tiap export |

### Tier 4 — Animasi Frame-based (opsional, untuk asset non-rig: item, monster kecil)
| Tool | Fungsi |
|---|---|
| `build_walk_cycle(frame_count, style)` | Preset siklus jalan dengan easing |
| `apply_easing_curve(frame_sequence, curve_type)` | linear / ease_in_out / ease_out_bounce / anticipation_hold |
| `set_frame_duration(frame_index, ms)` | Durasi custom per frame |
| `apply_squash_stretch(frame_index, axis, factor)` | Efek berat di frame contact |
| `add_follow_through(layer_name, delay_frames, damping)` | Secondary motion versi frame-based |
| `build_directional_set(base_frames, directions)` | Generate 4/8 arah otomatis (flip horizontal) |
| `attach_drop_shadow(offset, opacity, follow_anchor)` | Krusial untuk top-down — kaki "kebaca" nempel tanah |
| `render_preview_gif(cycle_id, fps)` | QC visual cepat |
| `diff_frames(frame_a, frame_b)` | Deteksi jitter/pixel anomali |
| `export_spritesheet(cycle_ids, layout, padding)` | Export sheet final |
| `export_animation_metadata(format="json")` | Metadata timing/anchor/hitbox untuk engine |

---

## 4. Daftar Tool MCP Godot (Lengkap, dengan Tingkat Prioritas)

### Tier 1 — Fondasi + Observability (paling sering diabaikan, paling sering jadi biang kegagalan)
| Tool | Fungsi |
|---|---|
| `open_project(path)` / `get_project_state()` | Load & baca status project |
| `read_node_tree(scene_path)` | Lihat struktur scene sebelum ubah apapun |
| `get_node_property(path, property)` | Baca satu nilai sebelum override |
| `set_node_property(path, property, value)` | Tulis satu nilai — granular |
| `create_node(parent_path, type, name)` | Bikin satu node |
| `delete_node(path)` | Hapus satu node |
| `run_scene_headless(scene_path, duration_frames)` | Jalankan scene tanpa GUI untuk testing cepat |
| `capture_viewport_screenshot()` | **KRITIS** — vision input hasil render ke LLM |
| `get_console_output()` / `get_last_error()` | **PALING KRITIS** — tanpa ini error GDScript silent, LLM tidak tahu ada yang crash |
| `validate_scene(scene_path)` | Cek scene bisa di-load tanpa error sebelum lanjut |

### Tier 2 — Rig & IK
| Tool | Fungsi |
|---|---|
| `import_sprite_parts(json_metadata)` | Baca output dari MCP Aseprite Tier 3 |
| `create_skeleton2d(bone_hierarchy)` | Bangun skeleton dari definisi bone |
| `attach_sprite_to_bone(sprite_part, bone_name)` | Bind part sprite ke bone |
| `add_two_bone_ik(chain_root, chain_tip, target)` | IK untuk limb |
| `add_fabrik_ik(chain, target)` | IK untuk chain panjang |
| `add_ccdik(chain, target, angle_constraints)` | IK dengan batasan sudut per-bone |
| `set_bone_constraint(bone, min_angle, max_angle)` | Batas rotasi natural |
| `preview_ik_pose(target_positions)` | Test IK statis sebelum animasi jalan |

### Tier 2B — Rig & Render Pipeline 3D (khusus Jalur B, menggantikan sebagian Tier 2 di atas)
Dipakai kalau karakter berasal dari MCP Blender (mesh 3D), bukan sprite 2D. Skeleton3D di sini menjalankan teori IK yang SAMA PERSIS dengan Bagian 2.1 — bukan sistem terpisah, hanya beda dimensi (Skeleton2D → Skeleton3D).
| Tool | Fungsi |
|---|---|
| `import_gltf_rig(gltf_path, json_metadata)` | Baca hasil `export_gltf` + `export_rig_metadata` dari MCP Blender — setara `import_sprite_parts` versi 3D |
| `verify_skeleton3d_created(node_path)` | Godot otomatis bikin Skeleton3D dari import glTF — WAJIB diverifikasi granular, jangan asumsikan otomatis selalu benar (lihat jebakan orientasi Bagian 7) |
| `setup_camera3d_orthogonal(position, zoom)` | Kamera wajib proyeksi Orthogonal, bukan Perspective — ini yang membuat hasil akhir tetap terlihat 2D top-down |
| `create_subviewport_pixelation(resolution, filter_mode="nearest")` | Setup SubViewport beresolusi rendah + nearest-neighbor — inti teknik pixelation (Bagian 7) |
| `apply_pixelation_shader(params)` | Shader tambahan (toon/cel shading) di atas SubViewport untuk shading bertingkat khas pixel art |
| `add_two_bone_ik_3d(chain_root, chain_tip, target)` | Versi 3D dari `add_two_bone_ik` — solver matematika sama (Bagian 2.1), target 3D bukan 2D |
| `validate_render_filtering(node_path)` | Cek filter "Nearest" konsisten di viewport, texture, DAN material sekaligus — jebakan umum yang sudah dicatat di Bagian 7 |

### Tier 3 — Locomotion & Fisika
| Tool | Fungsi |
|---|---|
| `write_gait_script(amplitude, frequency, stride, phase_offset)` | Generate GDScript sinusoidal gait |
| `attach_spring_bone(bone_path, stiffness, damping)` | Secondary motion spring-damper |
| `attach_velvet_modifier(bone_path, params)` | Secondary motion gaya mengayun (kain/jubah) |
| `attach_foot_raycast(foot_bone, ray_length)` | Foot IK menyesuaikan permukaan |
| `set_animation_param(node, param, value)` | Tuning parameter tanpa rewrite script |
| `run_parameter_sweep(param, range, eval_metric)` | Coba beberapa nilai otomatis, ambil paling stabil |
| `apply_pd_controller(state_transition, kp, kd)` | Transisi antar state gerak (idle/walk/run) |
| `select_gait_template(creature_type)` | Pilih model gait sesuai jenis makhluk: biped / quadruped_trot / quadruped_gallop / blob_squash / flyer_hover |
| `apply_idle_breathing(bone_path, amplitude, frequency)` | Napas halus baseline untuk idle — bukan freeze total |
| `enable_y_sort(node_path)` | Aktifkan depth-ordering berbasis posisi Y (setara "Y Sort Enabled" Godot) |

### Tier 4 — Testing, QC, Export
| Tool | Fungsi |
|---|---|
| `record_animation_to_video(duration)` | Rekam untuk review manual |
| `detect_jitter(frame_sequence)` | Analisis delta antar frame, flag anomali |
| `check_foot_sliding(cycle_id)` | Validasi kaki tidak sliding di tanah |
| `export_scene_as_reusable(path)` | Simpan hasil jadi prefab/scene reusable |

---

## 4A. Daftar Tool MCP Blender (Lengkap, dengan Tingkat Prioritas — untuk Jalur B)

Blender sekarang menjadi engine/MCP resmi ketiga, setara Aseprite dan Godot. Berlaku hanya kalau Jalur B (Bagian 7) dipilih untuk 8-direction/rig karakter.

### Tier 1 — Fondasi + Observability
| Tool | Fungsi |
|---|---|
| `open_blend_file(path)` / `save_blend_file(path)` | I/O dasar |
| `get_scene_state()` | Baca daftar objek, mode aktif, seleksi saat ini — verifikasi sebelum aksi |
| `list_objects(filter)` | Cek objek yang ada di scene |
| `render_viewport_screenshot()` | **KRITIS** — vision input ke LLM, setara `capture_canvas_as_image` di Aseprite |
| `get_console_output()` / `get_last_error()` | **KRITIS** — bpy script bisa gagal silent tanpa ini |
| `undo()` / `redo()` | Recovery |

### Tier 2 — Modeling Low-Poly
| Tool | Fungsi |
|---|---|
| `create_mesh_primitive(type, params)` | Cube/cylinder/sphere sebagai basis part tubuh |
| `apply_modifier(object, modifier_type, params)` | Mirror (simetri kiri-kanan — versi 3D dari aturan mirroring Bagian 7), Bevel, Decimate |
| `set_shading_mode(object, mode="flat")` | Flat shading, bukan smooth — penting agar tetap terlihat pas dipixelasi, bukan gradasi halus |
| `merge_by_distance(object, threshold)` | Bersihkan vertex dobel hasil modeling |
| `separate_mesh_by_material(object)` | Pisah part untuk texturing/rigging independen |
| `validate_poly_count(object, max_tris)` | Cek jumlah triangle tetap rendah — "low-poly" harus terukur, bukan asumsi. **Target acuan untuk game ini: 300-1000 triangle/karakter** (NPC/monster kecil bisa lebih rendah), karena hasil akhir didownscale ke resolusi sangat rendah sebelum dipixelasi — detail di atas angka ini tidak akan pernah terlihat pemain. Tetap jaga minimal 6-8 segmen di limb (lengan/kaki) supaya silhouette tidak pecah/segi-banyak saat diputar ke 8 arah. |

### Tier 3 — Rigging & Skinning
| Tool | Fungsi |
|---|---|
| `create_armature(bone_hierarchy)` | Bangun skeleton — WAJIB ikuti hierarki sendi anatomis (hip→knee→ankle), sama prinsip dengan IK Godot |
| `add_bone(parent, name, head_pos, tail_pos)` | Tambah bone individual, granular |
| `set_bone_roll(bone, angle)` | Orientasi sumbu bone — sering diabaikan, sumber distorsi rig paling umum saat animasi diimpor ke Godot |
| `apply_all_transforms(object)` | **KRITIS sebelum export** — apply rotation/scale/location. Transform yang belum di-apply menyebabkan data mentah hasil ekspor berbeda dari yang terlihat di viewport Blender, dan Godot membaca nilai mentah itu apa adanya |
| `validate_bone_roll_consistency(armature)` | Cek semua bone roll konsisten sebelum export — roll tidak konsisten membuat keyframe rotasi berputar di sumbu tak terduga saat diimpor ke Godot |
| `auto_weight_paint(mesh, armature)` | Skinning otomatis awal |
| `adjust_vertex_weights(bone, vertices, weight)` | Koreksi manual titik yang salah bobot dari auto-weight |
| `validate_rig_symmetry(armature)` | Cek panjang bone kiri = kanan, konsisten dengan prinsip mirroring 8-direction |

### Tier 4 — Texturing
| Tool | Fungsi |
|---|---|
| `unwrap_uv(mesh, method)` | UV unwrap dasar |
| `create_flat_material(name, color)` | Material flat/toon, bukan PBR gradient — jaga estetika pixel art |
| `apply_vertex_color(mesh, color_map)` | Alternatif texturing ringan, umum di rig low-poly gaya Rain World |
| `bake_reference_texture(image_path, mesh)` | Proyeksikan tekstur 2D custom (mis. dari MCP Aseprite) ke permukaan mesh |

### Tier 5 — Pose & Animasi Keyframe
Untuk aksi one-shot (attack/hurt/death) — pelengkap procedural IK di Godot, konsisten dengan Bagian 9.
| Tool | Fungsi |
|---|---|
| `set_pose(armature, bone_transforms)` | Set pose statis |
| `insert_keyframe(bone, frame)` | Keyframe individual |
| `apply_easing_to_action(action, curve_type)` | Easing di level Blender sebelum export (opsional) |

### Tier 6 — Export & Bridge ke Godot
Titik sambung paling kritis ke MCP Godot.
| Tool | Fungsi |
|---|---|
| `export_gltf(path, options)` | Format utama — glTF 2.0. **Perhatian orientasi:** glTF pakai +Z sebagai arah depan & +Y sebagai atas, sedangkan Godot pakai -Z sebagai depan — kontradiksi ini sering membuat karakter menghadap arah salah setelah import. Set opsi export dengan sadar, jangan asumsikan default selalu benar. |
| `export_rig_metadata(format="json")` | Nama bone, hierarki, anchor point — dibaca versi 3D dari `import_sprite_parts` di MCP Godot |
| `validate_export(path)` | Cek file hasil export tidak corrupt/kosong DAN validasi orientasi depan karakter + rest pose tidak terpuntir — sebelum diserahkan ke Godot. Beberapa masalah ini ada di sisi importer Godot sendiri (bug tercatat: rotasi limb yang normal di Blender bisa berputar 360° di Godot AnimationPlayer), jadi validasi manual tetap perlu meski setup Blender sudah benar. |

---

## 5. Urutan Bangun (Wajib Bertahap — Jangan Lompat)

**Jalur A (2D flat sprite, default):**

| Fase | Scope | Kriteria lulus sebelum lanjut |
|---|---|---|
| **1** | Tier 1 Aseprite + Tier 1 Godot saja | LLM bisa gambar 1 sprite statis sederhana, import ke Godot sebagai Sprite2D biasa (belum rig), tampil di layar, screenshot berhasil dibaca LLM. Ulangi 10x tanpa gagal. |
| **2** | Tier 2-3 Aseprite (part slicing) + Tier 2 Godot (skeleton statis, tanpa IK) | Karakter jadi beberapa part nempel ke bone, pose statis benar secara visual. |
| **3** | Tambah IK (two-bone dulu, satu kaki saja) | `preview_ik_pose` menghasilkan gerak kaki sesuai target tanpa distorsi. |
| **4** | Gait script sinusoidal sederhana (belum spring bone/raycast) | Walk cycle dasar smooth & konsisten. |
| **5** | Tambah satu per satu: foot raycast → spring bone → parameter tuning | Tiap penambahan diuji terpisah, tidak digabung sekaligus. |

**Jalur B (3D rig + pixelation shader) — tambahan Fase 0 di depan Fase 1 di atas:**

| Fase | Scope | Kriteria lulus sebelum lanjut |
|---|---|---|
| **0a** | Tier 1 Blender saja | LLM bisa buka file Blender, buat satu mesh primitif sederhana (mis. cube), screenshot viewport berhasil dibaca LLM. Ulangi 10x tanpa gagal. |
| **0b** | Tier 2 Blender (modeling low-poly dasar) | Satu part tubuh sederhana (mis. torso) dibuat, poly count tervalidasi rendah, shading flat. |
| **0c** | `export_gltf` + `validate_export` | File glTF berhasil diekspor dan tidak corrupt — diverifikasi lewat tool, bukan cuma "kelihatannya berhasil". |
| **0d** | Import hasil export ke Godot | Mesh 3D tampil benar di Godot dengan Camera3D Orthogonal + SubViewport rendah resolusi. Baru setelah ini stabil, lanjut ke Fase 1 Godot (Tier 1) seperti Jalur A, lalu Fase 2 dst diadaptasi ke Skeleton3D/IK 3D alih-alih Skeleton2D. |

**Aturan keras (berlaku untuk kedua jalur):** setiap fase harus stabil (berhasil berulang tanpa gagal) sebelum mulai fase berikutnya. Kegagalan sebelumnya (4x) kemungkinan besar terjadi karena mencoba fase lanjut tanpa fondasi Tier 1 (observability) yang solid di tiap MCP — sehingga titik gagal tidak pernah teridentifikasi dengan jelas.

---

## 7. Dukungan 8-Direction

Dua jalur, pilih salah satu sesuai skala proyek — jangan campur tanpa rencana jelas:

**Jalur A — 2D flat sprite parts (default, dari MCP Aseprite)**
Karena simetri kiri-kanan, cukup gambar/rig **5 arah unik**: N, NE, E, SE, S. Arah W, NW, SW didapat via mirror horizontal dari E, NE, SE. `build_directional_set` diperluas untuk terima `[N,NE,E,SE,S]` + flag mirror otomatis. Tiap sprite part & pose IK target butuh 5 variasi posisi.

**Jalur B — True 3D rig + kamera orthographic + pixelation shader**
Rig dibuat di software 3D (mis. Blender, low-poly), dirender lewat kamera orthographic di Godot, hasil di-pixelate via shader. 8-direction (bahkan sudut bebas) didapat gratis tanpa redraw/re-rig — tinggal putar kamera/karakter. Lebih scalable untuk karakter yang sering terlihat gerak dari banyak sudut (player, NPC utama, enemy umum), tapi butuh pipeline modeling 3D tambahan.

**Rekomendasi:** Jalur B untuk karakter frekuensi tinggi, Jalur A cukup untuk objek/karakter minor.

**Detail teknis render Jalur B (agar tetap terlihat 2D pixel top-down):**
- Kamera 3D wajib proyeksi **Orthogonal**, bukan Perspective.
- Scene 3D dirender ke **SubViewport beresolusi rendah** (mis. 320×180), lalu di-upscale via nearest-neighbor filtering — inilah yang menghasilkan tampilan pixelated dari mesh yang sebenarnya halus.
- Godot 4.6+ punya dukungan native "Scaling 3D Mode: Nearest" di Viewport, jadi tidak selalu perlu shader custom untuk efek dasar ini.
- Untuk look pixel-art yang lebih otentik (shading bertingkat, bukan gradient halus), tambahkan toon/cel shading di atas render SubViewport.
- **Jebakan umum:** SubViewport texture bisa tetap terlihat blur meski setting sudah "Nearest" — filter perlu dicek konsisten di level viewport, texture, DAN material sekaligus.

**Konsekuensi ke arsitektur MCP:** Jalur B menambah domain MCP ketiga (Blender) di luar Aseprite dan Godot. Peran MCP Aseprite bergeser — tidak lagi membuat body karakter (kini mesh 3D + texture dari Blender), tapi tetap relevan untuk UI, icon, item, dan elemen 2D murni yang tidak butuh rotasi banyak arah.

---

## 7A. MCP Blender (untuk Jalur B)

Pola umum implementasi yang sudah ada: addon di dalam Blender membuka socket TCP lokal (biasanya port 9876) + server MCP terpisah (stdio) sebagai jembatan ke LLM.

| Referensi | Karakteristik kunci | Yang layak dipelajari/diadopsi |
|---|---|---|
| `ahujasid/blender-mcp` | Paling populer; two-way socket; bisa eksekusi kode Python arbitrer langsung dari LLM | Ide "raw Python execution" — tapi jadikan escape-hatch tier terakhir, bukan jalur utama |
| `6xvl/blender-mcp` (fork) | ~270 tools direct-dispatch (bukan per-call Python compile), hang detection, forced auto-update | Hang detection + direct-dispatch (hindari overhead compile-per-call) |
| `PatrykIti/blender-ai-mcp` | **Paling selaras dengan prinsip observability kita**: goal-first routing, tools dikurasi, verifikasi deterministik, workflow dibantu vision. Eksplisit menghindari "raw bpy script generation" karena API Blender drift antar versi & operator sensitif konteks gagal kalau state salah | Pelajari struktur atomic/macro/workflow tools-nya langsung — argumen desainnya sama persis dengan alasan 4 workflow kamu sebelumnya gagal |
| `djeada/blender-mcp-server` | 22 tools/6 namespace, unit test dengan bpy di-mock (testable tanpa buka Blender GUI) | Pola testing tool tanpa dependency ke instance Blender aktif |

**Cara mencampur referensi yang benar vs salah:**
- **Salah:** Copy-paste tool list dari banyak project jadi satu MCP raksasa tanpa arsitektur konsisten → dependency conflict, gaya error handling tidak seragam, sebagian tool testable sebagian tidak, LLM kewalahan pilih dari ratusan tool tanpa routing jelas. Ini memperburuk observability, bukan memperkuat.
- **Benar:** Ambil **pola arsitektur**, bukan sekadar daftar tool, dari tiap referensi sesuai kekuatannya masing-masing (kolom terakhir tabel di atas), lalu satukan jadi satu desain konsisten — idealnya konsisten juga dengan MCP Aseprite & Godot kamu (lihat Bagian 7B).

---

## 7B. Pola Arsitektur Konsisten Lintas Ketiga MCP (Aseprite / Godot / Blender)

Supaya ketiga MCP custom tidak jadi tiga gaya berbeda, terapkan pemisahan tool yang sama di semuanya:

| Layer | Definisi | Contoh |
|---|---|---|
| **Atomic tools** | Aksi tunggal, kecil, presisi — biasanya tersembunyi dari pemanggilan langsung LLM, jadi fondasi bagi macro tools | `set_pixel()`, `create_node()`, `set_bone_constraint()` |
| **Macro tools** | Task-sized, layer utama yang dipanggil LLM — gabungan beberapa atomic tool jadi satu aksi bermakna | `build_walk_cycle()`, `attach_sprite_to_bone()`, `create_skeleton2d()` |
| **Workflow tools** | Proses multi-step dengan pelaporan eksplisit di tiap tahap — bukan endpoint "lakukan apa saja" open-ended | `run_ingest_and_rig_pipeline()` dengan report per-langkah, berhenti & lapor di step yang gagal |

Prinsip tambahan yang konsisten di ketiganya:
- **Verifikasi deterministik selalu jadi sumber kebenaran akhir** — vision/screenshot cuma alat bantu interpretasi, bukan pengganti pengecekan data aktual (posisi, ukuran, hierarki).
- **Goal-first routing** — LLM diarahkan ke tool yang relevan dengan intent saat ini, bukan disodori seluruh daftar tool sekaligus tiap giliran.
- **Raw script execution** (Lua di Aseprite, GDScript raw di Godot, bpy raw di Blender) selalu jadi tier terakhir/opsional, bukan jalur utama — dipakai hanya untuk kasus yang belum tercakup tool granular.

---

## 8. Character Archetype System (untuk semua usia, ukuran, jenis karakter)

Satu workflow bisa menangani semua jenis karakter, tapi WAJIB diparameterisasi lewat "archetype profile", bukan skeleton/rig generik tunggal. **Berlaku sama di kedua jalur** — untuk Jalur A parameter ini dipakai `create_skeleton2d` (Godot), untuk Jalur B parameter yang sama dipakai `create_armature` (Blender, Bagian 4A Tier 3), lalu diteruskan lewat `export_rig_metadata` ke Godot.

| Elemen | Perlu di-parameterisasi per archetype |
|---|---|
| Proporsi tubuh | Rasio kepala-badan berbeda per archetype (child/adult/elder/boss) |
| Panjang bone | Chain IK sama (hip-knee-ankle), tapi panjang di-scale per archetype |
| Gait template | `select_gait_template(creature_type)` — frekuensi/amplitude beda, bukan cuma di-scale ukuran |
| Validasi proporsi | `validate_proportions` menerima parameter archetype, bukan satu ratio global |

Archetype minimum yang perlu didefinisikan di awal proyek: `child`, `adult`, `elder`, `small_enemy`, `large_enemy_boss`, `quadruped`, `blob`, `flyer`.

---

## 9. Acuan Frame Animasi per Kategori Gerakan

Tidak semua gerakan cocok dibuat procedural. Locomotion periodik pakai gait function; aksi reaktif one-shot tetap pakai keyframe + easing:

| Kategori | Metode | Contoh state |
|---|---|---|
| Locomotion (periodik) | Procedural gait (sinusoidal + IK) | idle, walk, run |
| Aksi reaktif (one-shot) | Keyframe pose + easing curve — Aseprite Tier 4 untuk Jalur A, atau Blender Tier 5 (`set_pose`, `insert_keyframe`) untuk Jalur B | attack_melee, attack_ranged, hurt, death, cast_spell, block |
| Kondisi khusus | Kombinasi/blend procedural + override pose | knockback, stagger |

---

## 10. Tool & Engine Stack Ringkas

| Layer | Tool/Engine |
|---|---|
| Concept/reference | Image-gen model (opsional) atau referensi manual/video |
| Pixel art authoring | Aseprite + MCP Aseprite custom (Python) — body karakter (Jalur A) atau UI/icon/item (Jalur B) |
| Modeling & rigging 3D (khusus Jalur B) | Blender 5.2 LTS + MCP Blender custom (Python) — lihat Bagian 4A |
| Game engine & runtime rig | Godot 4.7.1 — Skeleton2D+IK (Jalur A) ATAU Skeleton3D+Camera3D Orthogonal+SubViewport pixelation (Jalur B, Bagian 4 Tier 2B) — keduanya + MCP Godot custom (Python) |
| Bahasa MCP server | Python (Pydantic untuk validasi, asyncio untuk I/O non-blocking) |
| Bahasa runtime animasi | GDScript (gait function, spring-damper, dihasilkan lewat MCP — identik di kedua jalur) |
| Agent orkestrator | Antigravity IDE 2.5.5 |

---

## 11. Batasan Jujur (Tidak Bisa Dijamin)

- Tidak ada jaminan hasil akhir "100% terasa hidup" — itu penilaian subjektif pemain yang butuh playtesting & iterasi manual, bukan murni output otomatis sistem manapun.
- LLM tidak punya insting artistik/animator asli — semua "rasa hidup" di sistem ini berasal dari rumus fisika/matematika yang di-encode eksplisit (spring-damper, gait function, IK), bukan dari kreativitas LLM itu sendiri.
- Godot IK framework (4.6+) relatif baru dan API-nya bisa berubah antar versi — cek dokumentasi Godot versi yang dipakai sebelum implementasi.
- Kombinasi hybrid image-gen → pixelization tetap butuh kurasi manual pada tahap concept/reference — tidak sepenuhnya otomatis dari nol.
- Yang bisa dijamin: dengan observability tools + urutan bertahap, kegagalan akan selalu teridentifikasi di titik kecil dan bisa diperbaiki cepat — bukan menumpuk jadi kekacauan besar tak terlacak seperti pola 4 percobaan sebelumnya.

---

## 12. Domain Tambahan: Objects, Environment, UI, Maps, FX/VFX

> **PENANDA URUTAN — WAJIB DIBACA SEBELUM BAGIAN INI:** Kelima domain di bawah **HANYA dikerjakan setelah pipeline karakter (Bagian 5, Fase 1-5, atau Fase 0a-0d+1-5 untuk Jalur B) lolos uji coba stabil.** Ini bukan checklist paralel, bukan "sambil jalan boleh dicicil". Menambah domain baru sebelum fondasi karakter terbukti stabil adalah persis pola scope-creep yang menyebabkan 4 kegagalan sebelumnya. Bagian ini didokumentasikan sekarang supaya tidak hilang dari rencana — bukan sebagai izin untuk mulai sekarang.

### 12.1 Objects/Props (item, chest, senjata, furniture, koin, obor)

Paling dekat dengan tool yang sudah ada — sebagian besar statis, cukup MCP Aseprite Tier 1-3 (canvas, quantize, part-slicing) tanpa rig/IK.

| Tool | Fungsi |
|---|---|
| `apply_simple_oscillation(param, amplitude, frequency)` | Osilasi ringan (rotasi koin, nyala obor, buka-tutup peti) — sin/cos periode pendek TANPA mesin gait/IK. Jangan pakai sistem gait manusia untuk objek non-biped kecil, itu overkill dan model yang salah. |

### 12.2 Environment (tile, tanah, pohon, air, dekorasi)

Domain baru — bukan soal rig karakter, tapi konsistensi tepi tile & aturan autotiling.

| Tool | Fungsi |
|---|---|
| `validate_tile_seamless(tile_id, adjacent_tiles)` | Cek tepi antar tile nyambung tanpa jahitan terlihat |
| `generate_autotile_bitmask(tile_set)` | Aturan transisi otomatis (rumput→jalan setapak dst.) sesuai sistem bitmask TileSet Godot |
| `create_terrain_layer(terrain_name, tiles)` | Pakai fitur Terrain di TileSet resource Godot 4, bukan penempatan tile manual satu-satu |
| `apply_environment_sway(node, noise_params)` | Air mengalir/daun bergoyang — pakai noise-based sway (Bagian 2.7), bukan gait |

### 12.3 UI (menu, HUD, tombol, panel)

Domain baru sepenuhnya — UI di Godot pakai node `Control` + container layout, bukan `Node2D`/`Skeleton2D`.

| Tool | Fungsi |
|---|---|
| `create_9slice_panel(corners, edges, center)` | Panel scalable tanpa distorsi border saat resize |
| `build_control_hierarchy(layout_type)` | VBoxContainer/HBoxContainer/GridContainer — bukan bone hierarchy |
| `render_bitmap_font_text(text, font_id)` | Reuse font bitmap tool dari Aseprite (Bagian 3) untuk UI text, bukan cuma in-world text |
| `check_icon_consistency(icon_set)` | Validasi semua icon UI konsisten resolusi & style dengan aset in-game |

### 12.4 Maps (peta dunia, layout dungeon)

Paling jauh dari workflow karakter — domain "level design"/prosedural, bukan "asset/rig". Masuk sebagai tool tambahan di **MCP Godot**, bukan MCP Aseprite, karena logikanya algoritmik bukan visual.

| Tool | Fungsi |
|---|---|
| `generate_dungeon_layout(algorithm, params)` | Procedural generation — BSP, cellular automata, atau wave function collapse |
| `compose_tilemap(room_layout, tile_palette)` | Assembly tile jadi map jadi, dari tileset environment (12.2) |
| `validate_navigation(navmesh)` | Cek semua area bisa dijangkau — tidak ada ruangan terisolasi/softlock |

### 12.5 FX/VFX (hit-flash, slash, ledakan, spell, debu, api)

**Prinsip kunci — beda dari particle system 3D/modern biasa:** particle dengan gradient alpha halus akan clash secara visual dengan sprite pixel art blocky di sekitarnya. Pixel art FX SEBAIKNYA pakai tepi keras (hard-edge)/warna terkuantisasi, bukan gradient lembut default kebanyakan tutorial particle system. Praktik industri pixel art nyata: mayoritas FX (hit, slash, ledakan kecil) dibuat sebagai **flipbook/spritesheet tangan**, bukan particle real-time — simulasi 3D real-time untuk FX kecil itu overkill dan tidak direkomendasikan.

**Prinsip pembeda:** batasnya BUKAN "sederhana vs rumit" secara umum, tapi **apakah ada fenomena fisik nyata yang perlu disimulasikan, atau murni bentuk grafis 2D yang dianimasikan.** Tebasan pedang, kilatan/flash, spark bintang — itu bentuk grafis murni (lengkungan/shape yang dianimasikan), TIDAK ada fisika nyata di baliknya untuk disimulasikan — **tetap MCP Aseprite, JANGAN pakai Blender untuk ini** meski Jalur B sudah dibangun. Bukti pasar aset game: paket FX tebasan yang beredar luas semuanya digambar tangan frame-by-frame, bukan hasil render simulasi 3D. Asap, api, cairan, kain — itu fenomena fisik sungguhan (turbulensi udara, gravitasi, momentum) yang sulit ditiru meyakinkan lewat gambar tangan — di sinilah Blender worthy.

**Kapan pakai metode yang mana:**

| Tipe FX | Metode | Alasan |
|---|---|---|
| **Tebasan pedang, hit-flash, spark, ledakan kecil geometris, spell impact sederhana** | **Flipbook/spritesheet — MCP Aseprite** (Bagian 3 Tier 4) | Bentuk grafis murni, bukan fenomena fisik. Cepat, kontrol artistik penuh, dan ini yang terbukti dipakai luas di industri — JANGAN alihkan ke Blender meski tersedia |
| **Asap, api, air, kain/tali/jubah bergerak, ledakan kompleks** | **Simulasi Blender → render ke flipbook** (MCP Blender, khusus kalau Jalur B sudah dibangun) | Fenomena fisik nyata (turbulensi, gravitasi, momentum) yang sulit ditiru meyakinkan lewat gambar tangan — sekali disimulasikan bisa dipakai ulang dengan variasi seed |
| Debu ambien, api unggun, percikan berkelanjutan, hujan | GPUParticles2D — MCP Godot, dengan tekstur hard-edge/quantized | Butuh variasi acak berkelanjutan yang mahal kalau di-flipbook manual |

**Tool tambahan (MCP Blender, khusus FX simulasi — hanya relevan kalau Jalur B):**
| Tool | Fungsi |
|---|---|
| `setup_fluid_simulation(domain, type, params)` | Mantaflow — untuk asap, api, cairan |
| `setup_cloth_physics(object, params)` | Geometry Nodes XPBD solver (Blender 5.2+, Bagian 0A) — untuk kain/jubah/tali/pita magic |
| `bake_simulation(frame_range)` | Bake simulasi ke cache sebelum render — wajib sebelum render flipbook, jangan render simulasi live |
| `render_simulation_to_flipbook(camera, resolution, output_path)` | Render Orthogonal ke resolusi rendah, hasilnya PNG sequence siap dipixelasi/dikuantisasi |

**Tool tambahan (MCP Godot):**
| Tool | Fungsi |
|---|---|
| `create_gpu_particles_2d(texture, emission_shape, params)` | Untuk FX ambien/berkelanjutan — bukan untuk hit-effect satuan |
| `quantize_particle_texture(texture, n_colors)` | Paksa tekstur particle ikut palet terbatas, konsisten dengan estetika pixel art (reuse konsep `quantize_palette` dari Aseprite) |
| `apply_hard_edge_alpha(texture, threshold)` | Ubah alpha gradient jadi tepi keras/quantized — mencegah particle terlihat "modern" menabrak sprite pixel |
| `trigger_hit_stop(duration_ms)` | Micro-pause singkat saat impact (efek "juice" klasik) — durasi acuan 0.05-0.1 detik di puncak |
| `apply_screen_shake(intensity, duration)` | Guncangan kamera saat hit/ledakan besar |
| `set_emission_cone(direction, angle)` | Arahkan partikel sesuai jenis aksi: cone depan untuk melee/proyektil, sphere untuk ledakan, cone vertikal untuk lompatan/pendaratan |

**Acuan timing (dari praktik game feel yang terbukti):** durasi total efek hit kecil 0.2-0.4 detik, flash terang di puncak pada 0.05-0.1 detik pertama lalu memudar, debris boleh sedikit lebih lama tapi jangan sampai mengganggu aksi berikutnya. Batasi 2-3 warna per efek untuk kontras tinggi dan kebacaan yang jelas.

---

## 13. Gap Analysis: Elemen Naratif *Lentera Pudar* yang Belum Tercakup

> **Konteks:** Bagian ini disusun setelah GDD *Lentera Pudar* dicocokkan terhadap workflow di atas. Sebagian besar elemen visual GDD (protagonis class-less, kombo 2-hit, 5 sektor dungeon bertema, boss per sektor) sudah tercakup penuh oleh Bagian 3-9 & 12. Tiga elemen berikut **tidak tercakup** karena sifatnya bukan animasi mandiri, melainkan visual yang terikat ke state gameplay eksternal (progres cerita, nilai meter, atau durasi trigger). Elemen non-visual (Curse Meter sebagai sistem stat, Dual Evolution Tree, AI The Hollow Reflection, dialog/quest logic) tetap sepenuhnya di luar cakupan — itu kode gameplay murni, bukan tugas MCP Aseprite/Godot/Blender.

### 13.1 The Fading Scarf — Swap State Multi-Tahap Terikat Progres Naratif

Syal Aina memendek secara **permanen dan bertahap** setiap kali Kaelen menyalakan Altar Lentera besar — bukan animasi siklus, tapi degradasi visual yang mengikuti flag cerita.

| Tool | MCP | Fungsi |
|---|---|---|
| `create_asset_variant_set(base_asset, variant_states)` | Aseprite | Kelola beberapa versi syal (panjang → sedang → pendek → koyak) sebagai satu keluarga aset dengan anchor & proporsi konsisten |
| `validate_variant_consistency(variant_set)` | Aseprite | Cek origin/anchor tiap variant sejajar, supaya swap antar tahap tidak "lompat" secara visual |
| `bind_visual_state_to_flag(node_path, state_variable, variant_map)` | Godot | Jembatan generik dari nilai state gameplay (mis. `altars_lit_count`) ke aset yang ditampilkan |
| `preview_state_transition(from_state, to_state)` | Godot | QC transisi antar tahap — bisa dikasih cross-fade pendek (0.2-0.3 detik) supaya tidak pop kasar |

**Batas tanggung jawab:** *kapan* dan *berapa altar* yang memicu perubahan tahap adalah logika save-state/progres cerita di luar MCP kita — tool di atas hanya "mendengarkan" nilai tersebut dan menukar aset yang sudah diautorkan terpisah.

### 13.2 CursedHand.gdshader — Shader dengan Uniform Live-Driven

Urat es di lengan kiri Kaelen harus merespons intensitas Curse Meter secara real-time — bukan shader dekoratif statis.

| Tool | MCP | Fungsi |
|---|---|---|
| `create_shader_material(base_shader_template, uniforms)` | Godot | Bikin material shader dengan daftar uniform parameter terdefinisi |
| `bind_uniform_to_gamestate(material_path, uniform_name, state_variable)` | Godot | Jembatan generik variabel gameplay → uniform shader (reusable untuk fitur reaktif lain di masa depan, tidak hanya Curse Meter) |
| `preview_shader_at_value(material_path, uniform_name, test_value)` | Godot | QC visual shader di titik ekstrem (0%, 50%, 100%) tanpa harus mensimulasikan gameplay penuh |

**Batas tanggung jawab:** logika naik/turunnya nilai Curse Meter (kapan pemain "digoda" kekuatan es) tetap kode gameplay murni.

### 13.3 Echoes of the Past — Reveal/Dissolve Level Environment

Menyalakan altar mengubah ruangan runtuh jadi transparan, memperlihatkan kenangan masa lalu selama 5-10 detik. Ini transisi visibilitas **seluruh ruangan**, bukan hit-effect atau particle ambien.

| Tool | MCP | Fungsi |
|---|---|---|
| `create_dual_layer_room(foreground_layer, memory_layer)` | Godot | Dua versi visual ruangan yang sama secara spasial: kondisi sekarang & kondisi masa lalu |
| `apply_dissolve_transition(node_path, duration, curve)` | Godot | Shader dissolve berbasis noise (bukan cross-fade linear polos) supaya terasa "berkabut", bukan sekadar fade |
| `trigger_timed_reveal(node_path, hold_duration, reverse_after)` | Godot | Jalankan window reveal 5-10 detik lalu kembali otomatis ke foreground |

**Konsekuensi produksi yang perlu diwaspadai:** setiap ruangan yang memakai mekanik ini butuh **dua** versi visual lengkap (foreground + memory layer) dari MCP Aseprite/Blender — beban aset ganda, bukan reuse gratis dari tileset yang sudah ada. Ini perlu masuk hitungan scope planning, terutama kalau dipakai di banyak ruangan lintas 5 sektor.

---

## 14. Catatan Urutan Build Realistis untuk *Lentera Pudar*

Urutan ini mengikuti prinsip "bertahap, tidak lompat tier" di Bagian 0 — bukan checklist paralel.

1. **Fondasi karakter Kaelen** (Bagian 5 penuh, Tier 1-4 kedua MCP) sampai stabil berulang — idle/walk/kombo 2-hit — **tanpa** syal khusus atau shader kutukan dulu.
2. **Vertical slice satu sektor** (Sektor 1 – Denial) lewat domain Environment (12.2) untuk validasi alur end-to-end sebelum digandakan ke 5 sektor.
3. **Bangun 3 tool gap di Bagian 13 satu per satu**, uji tiap tool di 1 aset/1 ruangan contoh dulu sebelum diterapkan ke skala penuh — sesuai prinsip observability-first (Bagian 0, poin 1).
4. **FX/VFX (12.5) & UI (12.3)** menyusul setelah karakter + environment + gap-tools terbukti stabil, karena keduanya bergantung pada aset yang sudah final.
5. **`generate_dungeon_layout` (12.4)** — algorithmic level layout — dikerjakan paling akhir dari sisi pipeline aset; bisa berjalan paralel dari sisi level-design tapi tidak menghalangi produksi aset visual.
6. **Di luar cakupan workflow ini sepenuhnya:** Dual Evolution Tree + 3 ending, AI The Hollow Reflection (perilaku musuh meniru pemain), sistem dialog/quest, dan save-state progres. Semua ini butuh dokumen arsitektur gameplay/state-management terpisah — bukan tugas MCP Aseprite/Godot/Blender, dan tidak akan terselesaikan dengan menambah tool MCP apa pun.

**Kesimpulan kelayakan:** GDD *Lentera Pudar* secara visual **bisa direalisasikan** dengan workflow ini setelah Bagian 13 ditambahkan — tapi volume kerja nyata (5 sektor × boss unik × dual-layer room untuk Echoes of the Past) jauh lebih besar dari sekadar "pipeline karakter sudah jadi". Realistis untuk MVP: potong scope ke 1-2 sektor dulu sebagai bukti pipeline penuh (karakter + environment + 3 gap tool + FX dasar) sebelum commit ke 5 sektor sekaligus.

---

## 15. Teori Domain Baru: Lighting, Kamera, Audio, AI Musuh

> **Kenapa bagian ini perlu ada terpisah dari daftar tool:** Bagian 2 sudah membuktikan bahwa "rasa hidup" datang dari teori matematika/fisika yang di-encode eksplisit, bukan dari insting AI menebak parameter (lihat Bagian 11, poin 2). Empat domain di bawah ini punya tool-nya sendiri yang belum didaftar sama sekali — tapi masalah lebih dalam dari itu: tanpa teori dasarnya, AI akan menebak-nebak nilai numerik tanpa paham *kenapa* nilai itu benar secara persepsi/emosi. Sebagian teori lama (spring-damper, PD controller, noise function) tetap reusable di sini — dicatat per domain di mana relevan.

### 15.1 Lighting Theory

Paling kritis dari empat domain ini karena tema lentera adalah inti gameplay *Lentera Pudar*, bukan dekorasi.

- **Photometric falloff** — intensitas cahaya berkurang terhadap jarak. Inverse-square (`intensity / distance²`) terasa lebih fisikal/realistis untuk sumber titik (obor, lentera); linear falloff terasa lebih "digambar tangan"/stylized dan lebih gampang dikontrol artistik untuk pixel art. Pilih satu secara sadar per jenis sumber cahaya, jangan campur tanpa alasan.
- **Shadow casting via occluder polygon** — di Godot 2D, bayangan dari `Light2D` butuh `LightOccluder2D` dengan polygon eksplisit per objek, bukan raycast per-pixel. Ini bukan opsional untuk suasana dungeon gelap — tanpa occluder, cahaya lentera akan tembus dinding dan merusak nuansa "misterius".
- **Color temperature sebagai pemetaan emosi** — skala Kelvin (2700K hangat/kuning ala nyala api → 6500K dingin/biru ala es) memberi AI *kerangka numerik* untuk menerjemahkan brief GDD ("kontras kehangatan cinta vs dinginnya kepasrahan abadi", syal `#F4B860` vs es `#4A6FA5`) jadi parameter cahaya yang konsisten lintas 5 sektor, bukan tebakan hex per kasus.
- **Radius sebagai mekanik, bukan cuma estetika** — GDD eksplisit menyebut radius cahaya syal menyusut 50% di Sektor 4 (Depression). Ini berarti radius `Light2D` harus jadi parameter yang di-bind ke state gameplay — pola arsitektur yang sama persis dengan `bind_visual_state_to_flag` (Bagian 13.1) dan `bind_uniform_to_gamestate` (Bagian 13.2), cuma target-nya properti cahaya.

**Tool baru (MCP Godot):**
| Tool | Fungsi |
|---|---|
| `create_light2d(node_path, falloff_type, color_temp, radius)` | Setup sumber cahaya dengan falloff & suhu warna eksplisit |
| `create_light_occluder(node_path, polygon_points)` | Definisikan bentuk bayangan per objek |
| `bind_light_property_to_state(light_path, property, state_variable)` | Jembatan generik state gameplay → properti cahaya (radius, intensity, warna) |
| `preview_lighting_at_state(scene_path, state_values)` | QC visual suasana di beberapa titik state (mis. curse meter 0%/50%/100%) sebelum playtest penuh |

### 15.2 Camera Theory

Sebagian reuse teori lama, sebagian butuh teori baru:

- **Look-ahead offset** — kamera bergeser sedikit ke arah gerak/hadap karakter (bukan strict-follow tepat di tengah), supaya pemain "melihat ke depan" lebih jauh saat bergerak. Ini beda dari spring-damper biasa; look-ahead adalah offset target berbasis velocity/facing, baru *hasil pergerakan ke target itu* yang pakai spring-damper (Bagian 2.3) atau PD controller (Bagian 2.5) yang sudah ada.
- **Camera bounds clamping** — batas pergerakan kamera per scene/ruangan supaya tidak menampakkan area di luar level. Sederhana secara matematika (clamp posisi ke rect), tapi wajib didefinisikan per ruangan, terutama untuk ruangan sempit ala Sektor 4 (Jurang Kesunyian Abadi).
- **Reuse dari Bagian 2**: spring-damper (2.3) untuk smoothing follow, PD controller (2.5) untuk transisi kamera saat masuk boss-fight (mis. zoom in/reposisi ke arena boss).

**Tool baru (MCP Godot):**
| Tool | Fungsi |
|---|---|
| `create_camera2d_with_lookahead(target, lookahead_distance, smoothing)` | Kamera follow dengan offset predictive |
| `set_camera_bounds(scene_path, rect)` | Clamp area pergerakan kamera per ruangan |
| `trigger_camera_transition(from_state, to_state, duration)` | Transisi kamera terpicu event (masuk boss arena, dsb.) — reuse PD controller |

### 15.3 Audio Theory

Kosong total di dokumen sebelumnya — dan ini kelas teori yang berbeda dari domain visual manapun:

- **Signal/mixing theory** — bus hierarchy (Master → Music/SFX/Voice), gain staging (hindari clipping dengan mengatur level per-bus sebelum master), dan **ducking** (menurunkan volume musik/SFX sementara saat dialog penting muncul — krusial untuk momen naratif seperti dialog Aina di klimaks).
- **State-based adaptive music** — musik berubah/berlapis mengikuti state gameplay (mis. layer tegang menyala saat Curse Meter tinggi, layer tenang saat dekat lentera). Pola arsitekturnya **identik** dengan `bind_visual_state_to_flag` (13.1): satu variabel gameplay men-drive lebih dari satu output — bedanya di sini outputnya volume/layer audio, bukan aset visual. Ini bukti bahwa "jembatan state → output" adalah pola generik lintas domain, bukan cuma untuk visual.

**Tool baru (MCP Godot):**
| Tool | Fungsi |
|---|---|
| `create_audio_bus_hierarchy(bus_tree)` | Setup Master/Music/SFX/Voice + routing |
| `bind_audio_layer_to_state(layer_id, state_variable, threshold_map)` | Jembatan generik state gameplay → volume/aktivasi layer musik (reuse pola 13.1) |
| `apply_ducking(trigger_bus, target_bus, duck_amount, attack_ms, release_ms)` | Auto-lower volume bus tertentu saat trigger_bus aktif (mis. dialog) |
| `crossfade_music_layer(layer_a, layer_b, duration)` | Transisi antar layer musik tanpa cut kasar |

### 15.4 AI Musuh — Kasus Khusus The Hollow Reflection

Ini beda total dari state machine idle/walk/attack yang sudah dicatat di Bagian 2A — GDD minta musuh **meniru gerakan pemain**, bukan bereaksi ke pemain.

- **Input delay & replay buffer** — rekam N frame terakhir posisi/aksi pemain ke buffer melingkar (circular buffer), lalu putar ulang buffer itu dengan delay tertentu sebagai gerakan musuh. Ini teori berbeda dari behavior tree/FSM biasa: musuh tidak "memutuskan" apa-apa, ia murni replay dengan lag — secara teknis lebih dekat ke sistem recording/playback daripada AI decision-making.
- **Delay sebagai dial kesulitan** — makin pendek delay, makin sulit (musuh nyaris real-time meniru), makin panjang delay, makin mudah diprediksi. Ini parameter tuning yang jelas dan terukur, bukan insting.
- Catatan cakupan: sistem *kapan* boss ini aktif, dialog bisikannya, dan trigger kemenangan/kekalahan tetap logika gameplay murni di luar MCP — yang masuk cakupan hanya mekanisme rekam-putar-ulang gerakannya.

**Tool baru (MCP Godot):**
| Tool | Fungsi |
|---|---|
| `create_input_replay_buffer(source_node, buffer_frames)` | Rekam N frame terakhir posisi/state node sumber (pemain) |
| `apply_delayed_playback(target_node, buffer_id, delay_frames)` | Putar ulang buffer ke node target dengan delay — inti mekanik The Hollow Reflection |
| `set_replay_delay(buffer_id, delay_frames)` | Tuning kesulitan via panjang delay |

---

## 16. Infrastruktur Produksi (Di Luar Pipeline Aset)

> **Kenapa bagian ini beda dari Bagian 12/13/15:** Bagian-bagian sebelumnya semuanya soal *menghasilkan/menampilkan* aset. Enam poin berikut adalah infrastruktur di sekeliling proses produksi itu sendiri — hal yang dibutuhkan supaya proyek bisa dikerjakan, di-track, ditest, dan akhirnya dirilis, terlepas dari seberapa bagus pipeline asetnya. Ini bukan konsumen dari MCP Aseprite/Godot/Blender, jadi tidak masuk sebagai "tool" dalam pengertian yang sama — lebih ke keputusan setup proyek yang perlu dibuat sadar sejak awal.

### 16.1 Version Control
Prinsip Bagian 0 ("granular, bisa di-rollback") secara implisit menuntut riwayat proyek lintas sesi — bukan cuma undo per-sesi di Aseprite/Godot yang hilang begitu aplikasi ditutup.
- **Git** untuk source (GDScript, scene `.tscn`, resource `.tres`, dokumen).
- **Git LFS wajib** untuk file binary besar (`.aseprite`, `.blend`, `.png`, `.wav`) — tanpa LFS, repo Git akan membengkak cepat dan riwayat jadi lambat/berat.
- Setup `.gitignore` khusus Godot (folder `.godot/`, cache import) sejak commit pertama.

### 16.2 Build & Export
GDD menargetkan PC Windows secara eksplisit (Bagian 1) — belum ada langkah konkret untuk mengubah project Godot jadi executable yang bisa dijalankan orang lain.
- Godot **export template** untuk Windows perlu di-download & dikonfigurasi terpisah dari editor.
- `export_presets.cfg` — definisikan preset export (icon, versi, include/exclude file) sekali di awal, bukan disetel manual tiap kali mau build.
- Kalau nanti berencana publish (itch.io/Steam), proses build ini juga jadi basis untuk packaging distribusi.

### 16.3 Testing Logic Gameplay
Beda dari `run_scene_headless` (Bagian 4, Tier 1) yang fungsinya QC visual/animasi — Curse Meter, branching 3 ending, dan logic non-visual lain butuh unit test yang mengecek *nilai dan alur*, bukan tampilan.
- **GUT (Godot Unit Test)** — addon testing standar untuk GDScript, memungkinkan test case seperti "curse_meter mencapai 100 → trigger game over" tanpa harus main manual tiap kali cek.

### 16.4 Dialog/Branching Narrative Tool
GDD ini naratif-berat (dialog Aina, 3 respons manusia terhadap Pudar, plot twist berlapis) — menulis semua dialog & percabangan langsung di GDScript tidak scalable begitu volume teks bertambah.
- **Dialogic** atau **Ink** (via addon Godot) — tool khusus authoring dialog/percabangan dengan editor sendiri, sudah umum dipakai di ekosistem Godot, dan bisa dipisahkan dari kode gameplay inti.

### 16.5 Save/Load System
Fading Scarf (13.1) dan Dual Evolution Tree butuh state yang **persist antar sesi main** — tanpa ini, semua progres bertahap (syal memendek, jalur evolusi dipilih) hilang tiap kali game ditutup.
- Godot `ResourceSaver`/`ResourceLoader` (native, simpan sebagai `.tres`) atau `ConfigFile` untuk format lebih sederhana.
- Alternatif: custom JSON schema kalau butuh format yang mudah dibaca manusia untuk debugging.
- Perlu didefinisikan sejak awal: variabel apa saja yang termasuk save-state (lihat diskusi dokumen sistem gameplay terpisah).

### 16.6 Font/Typography Asset
Tool render-nya sudah ada (`render_bitmap_font_text`, Bagian 3) — tapi itu cuma mesin render, sumber font-nya sendiri belum dipilih.
- Perlu font pixel yang secara visual cocok nuansa "misterius-hangat melankolis" — dipilih manual (bukan sesuatu yang bisa di-generate MCP), baik dari font gratis berlisensi jelas atau dibuat custom sebagai bitmap font di Aseprite.

---


# Design Decisions Log — Lentera Pudar

Dokumen ini mencatat seluruh keputusan arsitektur struktural, desain game, dan pilihan teknis berbiaya tinggi (*Architecture Decision Records*). Tujuannya agar keputusan di masa lalu memiliki konteks jelas dan tidak didebat ulang dari nol.

---

## Log Keputusan yang Sudah Ditetapkan

### ADR-001: Model Rendering 8-Arah Murni & Asimetri Lore
- **Tanggal**: 2026-08-13
- **Status**: Superseded by ADR-008
- **Konteks**: Karakter utama memiliki desain asimetris: tangan kiri dibalut perban dengan urat es biru (Kutukan Pudar), mata kanan mengenakan eyepatch, sedangkan tangan kanan normal.
- **Keputusan Awal**: 2D True 8-Way.
- **Evolusi**: Digantikan oleh ADR-008 (Jalur B: 3D Low-Poly Rig) yang secara otomatis menjamin akurasi geometris asimetri di seluruh 8 arah tanpa resiko mirroring glitch.

### ADR-002: Arsitektur Komunikasi Global Event Bus (GameEvents.gd)
- **Tanggal**: 2026-08-13
- **Status**: Accepted (Standard Baku)
- **Konteks**: Komunikasi antar node di Godot rawan spaghetti code jika menggunakan direct tree querying.
- **Keputusan Terpilih**: Seluruh interaksi lintas sistem wajib disalurkan melalui Autoload `GameEvents.gd`.
- **Dampak**: Node modular, decoupled, dan dapat diuji secara independen.

### ADR-003: Pipeline Visual Berbasis Otomasi & Observabilitas
- **Tanggal**: 2026-08-13
- **Status**: Superseded by ADR-008
- **Konteks**: Memaksimalkan kecepatan produksi tanpa mengorbankan kualitas pixel art 32x32 dan kepatuhan lore.
- **Keputusan Awal**: Alur 3 tahap Pixellab ➔ Aseprite ➔ Godot.
- **Evolusi**: Digantikan oleh arsitektur 3-MCP bergradasi pada ADR-008.

### ADR-004: Arsitektur Narasi Berbasis 5 Tahap Berduka (5 Stages of Grief)
- **Tanggal**: 2026-08-14
- **Status**: Accepted (Standard Baku)
- **Konteks**: Mencegah alur cerita RPG terasa monoton atau berulang dengan menyematkan struktur psikologis mendalam di setiap sektor dungeon.
- **Keputusan Terpilih**: 5 Sektor Dungeon memetakan Kübler-Ross Model (Sektor 1: Denial - Lord Alden, Sektor 2: Anger - Ignis Vulkan, Sektor 3: Bargaining - Lady Vespera, Sektor 4: Depression - The Hollow Reflection, Sektor 5: Acceptance - The Frost Sovereign & Fajar Terakhir).
- **Dampak**: Setiap bos dan lingkungan memiliki resonansi tematik yang terhubung langsung dengan perkembangan psikologis pemain dan protagonis.

### ADR-005: Mekanik Karakter Dualitas (The Fading Scarf & Temptation of Frost)
- **Tanggal**: 2026-08-14
- **Status**: Accepted (Standard Baku)
- **Konteks**: Menghubungkan narasi Kaelen & Aina langsung ke elemen visual dan gameplay.
- **Keputusan Terpilih**: 
  1. *The Fading Scarf*: Syal kuning Aina memendek secara visual seiring berjalannya progres cerita (diimplementasikan via multi-variant assets di ADR-010).
  2. *The Temptation of Frost*: Bertarung di kegelapan membuat serangan tangan kiri es semakin mematikan tetapi berisiko membeku (*Game Over*).
- **Dampak**: Pemain merasakan bobot pengorbanan Aina dan godaan kekuatan keputusasaan secara konstan.

### ADR-006: Visi Skalabilitas Franchise (Lentera Pudar Expanded Universe)
- **Tanggal**: 2026-08-14
- **Status**: Accepted (Standard Baku)
- **Konteks**: Membangun fondasi semesta yang mampu menampung sekuel (*Lentera Pudar 2: The Frozen Horizon* & *Lentera Pudar 3: The Sovereign of Dawn*).
- **Keputusan Terpilih**: Game 1 berfokus pada penyembuhan duka pribadi di dungeon bawah tanah dan berakhir dengan terbukanya gerbang ke Benua Luar (*Overworld* beku).
- **Dampak**: Arsitektur dungeon, mekanik kutukan, dan data item dirancang extensible untuk ekspansi franchise.

### ADR-007: Standardisasi Desain Visual & Anatomi Kaelen V3 (Eyepatch, Baldric, & Directional Shadows)
- **Tanggal**: 2026-08-14
- **Status**: Accepted (Standard Baku)
- **Konteks**: Memilih base art definitif yang menyeimbangkan estetika pixel art semi-detailed, resonansi emosional duka, dan kepatuhan lore asimetri.
- **Keputusan Terpilih**: 
  1. Mengesahkan Penutup Mata Kulit Hitam (*Eyepatch* `#141013`) pada mata kanan sebagai segel bekas luka beku Kutukan Pudar masa lalu.
  2. Mengesahkan Tali Selempang Kantung Kelana (*Baldric Harness*) untuk memecah bidang jubah gelap dan mempertegas identitas pengelana.
  3. Menerapkan rasio proporsi 1:3 hingga 1:3.5 chibi semi-detailed.
- **Dampak**: Identitas visual Kaelen terkunci kokoh dan bebas dari kejanggalan proporsi.

---

### ADR-008: Transisi Menyeluruh ke Jalur B (Hybrid 3-MCP: Blender 5.2 + Godot 4.7.1 + Aseprite)
- **Tanggal**: 2026-08-15
- **Status**: Accepted (Master Architecture)
- **Konteks**: Pendekatan full-AI 2D generation sebelumnya mengalami kegagalan akibat diskontinuitas asimetri (lengan kutukan tertukar saat mirror) dan kesulitan menganimasikan Syal Aina di 8 arah.
- **Keputusan Terpilih**: 
  1. **Karakter Utama, Boss, & NPC Frekuensi Tinggi**: Mengadopsi **Jalur B (3D Low-Poly 300–1000 tris di Blender 5.2 LTS + glTF 2.0 ➔ Render Camera3D Orthogonal + SubViewport Pixelation di Godot 4.7.1)**.
  2. **Domain Aseprite MCP**: Difokuskan secara penuh untuk UI (9-slice panels, HUD, icons, bitmap typography), Props/Tileset Dungeon (walls, floors, autotiling), dan FX Flipbook Hard-Edge (tebasan pedang, hit-flash, sparks).
  3. **Standardisasi 3-Layer MCP**: Seluruh MCP (Blender, Godot, Aseprite) menerapkan pemisahan *Atomic*, *Macro*, dan *Workflow Tools* dengan observability wajib sebelum mutasi.
- **Dampak**: Asimetri Kaelen 100% konsisten secara geometris, animasi hanya perlu dibuat 1x untuk mencakup seluruh 8 arah, dan performa render tetap menghasilkan estetika pixel art autentik.

### ADR-009: Standardisasi Mesin Animasi Berbasis Matematika & Fisika
- **Tanggal**: 2026-08-15
- **Status**: Accepted (Standard Baku)
- **Konteks**: Animasi murni manual sering kaku dan memakan waktu tinggi, sedangkan AI generatif murni tidak memiliki insting fisiologis.
- **Keputusan Terpilih**: 
  1. **Locomotion Periodik (Idle/Walk/Run)**: Dijalankan via *Procedural Sinusoidal Gait Function* (inverted pendulum, phase offset $\pi$, body bob frekuensi 2x) dan *Inverse Kinematics* (Two-Bone untuk kaki/tangan, FABRIK untuk chain panjang).
  2. **Secondary Motion (Syal Aina & Jubah)**: Dijalankan via *Spring-Damper System* (Hukum Hooke) dan variasi *Velvet Modifier* untuk inersia kain dinamis.
  3. **Transisi State**: Dihaluskan menggunakan *PD Controller (Proportional-Derivative)* untuk mencegah snap kaku.
  4. **Aksi Reaktif One-Shot (Punch, Cursed Strike, Hurt, Death)**: Tetap menggunakan *Keyframe Pose + Easing Curve*.
- **Dampak**: Karakter terasa berbobot, hidup, dan responsif terhadap input pemain.

### ADR-010: Arsitektur State-Driven untuk Gap Fitur Lentera Pudar
- **Tanggal**: 2026-08-15
- **Status**: Accepted (Standard Baku)
- **Konteks**: Elemen kunci lore seperti Syal yang memendek, tangan es yang berdenyut sesuai kutukan, dan penglihatan memori masa lalu membutuhkan jembatan langsung antara variabel gameplay dan representasi visual.
- **Keputusan Terpilih**: 
  1. **The Fading Scarf**: Dikelola sebagai *Asset Variant Set* (Panjang ➔ Sedang ➔ Pendek ➔ Koyak) dan ditukar via fungsi jembatan generik `bind_visual_state_to_flag(node, flag, variant_map)`.
  2. **CursedHand.gdshader**: Shader uniform live-driven via `bind_uniform_to_gamestate(material, "intensity", "curse_meter")` yang merespons real-time pada rentang 0% hingga 100%.
  3. **Echoes of the Past**: Ruangan dirancang sebagai *Dual-Layer Room* (Foreground Runtuh + Memory Layer Transparan) yang ditransisikan menggunakan *Noise-based Dissolve Shader* selama 5–10 detik.
- **Dampak**: Integrasi penuh antara narasi psikologis dan sistem engine tanpa spaghetti code.

### ADR-011: Standar Domain Baru (Lighting, Kamera, Audio, & AI Replay)
- **Tanggal**: 2026-08-15
- **Status**: Accepted (Standard Baku)
- **Konteks**: Memastikan aspek visual pencahayaan, navigasi kamera, atmosfer audio, dan bos khusus memiliki landasan teori numerik terukur.
- **Keputusan Terpilih**: 
  1. **Lighting Theory**: Menggunakan skala temperatur Kelvin (2700K Warm Light `#F4B860` vs 6500K Ice `#4A6FA5`), *photometric falloff*, `LightOccluder2D` bayangan dinding, dan radius cahaya menyusut 50% di Sektor 4 (Depression).
  2. **Camera Theory**: Kamera follow prediktif (*Look-Ahead Offset*), *Room Bounds Clamping*, dan transisi *PD Controller* saat entering arena bos.
  3. **Audio Theory**: Hirarki bus terstruktur (`Master ➔ Music / SFX / Voice`), *Gain Staging*, *Ducking* saat narasi penting Aina, dan *State-Based Adaptive Music Layers*.
  4. **AI The Hollow Reflection**: Menggunakan *Circular Input Replay Buffer* dengan frame-delay sebagai pengatur tingkat kesulitan (makin pendek delay, makin agresif tiruannya).
- **Dampak**: Presentasi game terasa kohesif, mendalam, dan berkualitas premium.

### ADR-012: Fondasi Infrastruktur Produksi & Ekosistem Game
- **Tanggal**: 2026-08-15
- **Status**: Accepted (Standard Baku)
- **Konteks**: Memastikan stabilitas repositori kode, kemudahan pengujian sistem non-visual, dan kelancaran narasi percabangan.
- **Keputusan Terpilih**: 
  1. **Version Control**: Git dengan konfigurasi **Git LFS** aktif untuk file biner besar (`.blend`, `.gltf`, `.wav`, `.png`).
  2. **Quality Control Standard**: Menerapkan **The 4-Tier Commercial Gate** untuk memastikan kelayakan rilis komersial di Steam/PC.
- **Dampak**: Proses pengembangan terukur, data save aman dari crash/power-loss, zero regression bug, dan siap rilis komersial di Steam.

---

### ADR-013: Transisi Total Menuju 3D Action RPG (Unreal Engine 5 + Blender 5.2 LTS)
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master Strategic Pivot)
- **Konteks**: Pendekatan 2D pixel top-down memerlukan penggambaran frame-by-frame manual yang sangat masif (terutama dengan asimetri kompleks Kaelen: lengan kiri kristal es, eyepatch kanan, syal mengalir), sehingga membatasi keluwesan animasi dan kecepatan produksi.
- **Keputusan Terpilih**: 
  1. **Peralihan Engine**: Berpindah dari 2D/Godot menuju **3D Action RPG (Unreal Engine 5)**.
  2. **Pipeline Visual**: Menggunakan **Blender 5.2 LTS** sebagai pusat pemodelan 3D High-Detail (gaya anime/stylized ala *Final Fantasy VII Remake / Crisis Core*), biomechanical rigging, dan animasi 3D 360°.
  3. **Pembersihan Ekosistem 2D**: Menghapus seluruh artifak, skrip generator, spritesheet 2D, shader pixelation, dan konfigurasi MCP yang tidak relevan (Aseprite, Pixellab, Godot), dan memusatkan fokus alat pada **Blender 5.2 LTS + Unreal Engine 5**.
- **Dampak**: 
  - Model 3D Kaelen dimodelkan satu kali secara high-detail dan dapat dianimasikan bebas ke seluruh sudut 360 derajat.
  - Syal Aina dan jubah dapat memanfaatkan simulasi fisika kain (*Cloth Physics & Spring Bones*) dinamis secara real-time.
  - Pencahayaan lentera 2700K dan pendaran kristal es kutukan 6500K menghasilkan kualitas visual 3D AAA di Unreal Engine 5.


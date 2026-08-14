# Laporan Audit 15 Skill Proyek (.agents/skills/)
Total Skills: 15

| No | Folder / Skill Name | Name di Frontmatter | Deskripsi Trigger | Baris | Status Format |
|---|---|---|---|---|---|
| 1 | `aseprite_lua_mastery` | `aseprite_lua_mastery` | Pustaka memori untuk Aseprite Lua API. Berisi skrip otomasi ... | 99 | OK |
| 2 | `cross_check_docs` | `cross_check_docs` | Skill audit konsistensi silang yang dipicu via /cross-check-... | 27 | OK |
| 3 | `encounter_pacing` | `encounter_pacing` | Standar kurva kesulitan (difficulty curve), ritme encounter ... | 24 | OK |
| 4 | `godot_advanced_ecosystem` | `godot_advanced_ecosystem` | Pengetahuan mendalam mengenai ekosistem plugin pihak ketiga ... | 36 | OK |
| 5 | `godot_engine_mastery` | `godot_engine_mastery` | Penguasaan tingkat tinggi terhadap arsitektur Godot 4 untuk ... | 74 | OK |
| 6 | `godot_rpg_architecture` | `godot_rpg_architecture` | Standar arsitektur tingkat lanjut untuk pembuatan game RPG d... | 74 | OK |
| 7 | `godot_systems_mastery` | `godot_systems_mastery` | Pangkalan Data untuk Sistem Inti (Core Systems) Godot 4 ting... | 45 | OK |
| 8 | `level_layout_design` | `level_layout_design` | Standar perancangan tata letak dungeon 2D top-down (low top-... | 32 | OK |
| 9 | `mcp_api_mastery` | `mcp_api_mastery` | Pemahaman mendalam mengenai arsitektur internal WebSocket Br... | 32 | OK |
| 10 | `orchestration_protocol` | `orchestration_protocol` | Protokol orkestrasi untuk Supervisor Agent dalam memecah tas... | 36 | OK |
| 11 | `pixel_art_animation_mastery` | `pixel_art_animation_mastery` | Hukum mutlak untuk proporsi 32x32px, teori warna (Hue Shifti... | 35 | OK |
| 12 | `pixellab_ecosystem` | `pixellab_ecosystem` | Keahlian penuh dalam memaksimalkan kapabilitas Pixellab Clou... | 86 | OK |
| 13 | `player_psychology_engagement` | `player_psychology_engagement` | Panduan psikologi pemain untuk Psychology Agent (Consultant)... | 29 | OK |
| 14 | `qc_check` | `qc_check` | Standar eksekusi Quality Control (QC Gate) via perintah /qc-... | 38 | OK |
| 15 | `visual_pipeline_automation` | `visual_pipeline_automation` | "Panggil skill ini setiap kali kamu diminta untuk membuat, m... | 40 | OK |

## 1. Skill: `aseprite_lua_mastery`
- **Path**: `D:/GodotProjects/Lentera-Pudar/.agents/skills\aseprite_lua_mastery\SKILL.md`
- **Frontmatter Name**: `aseprite_lua_mastery`
- **Description**: Pustaka memori untuk Aseprite Lua API. Berisi skrip otomasi mutlak untuk memanipulasi layer, menambahkan tag animasi, dan melakukan trim kanvas.

```markdown
---
name: aseprite_lua_mastery
description: Pustaka memori untuk Aseprite Lua API. Berisi skrip otomasi mutlak untuk memanipulasi layer, menambahkan tag animasi, dan melakukan trim kanvas.
---

# Aseprite Lua Automation Mastery

Skill ini memastikan AI tidak perlu menebak-nebak sintaks saat diminta untuk membersihkan atau menyiapkan aset *pixel art* secara otomatis di Aseprite. Jangan lakukan perubahan manual! Selalu gunakan `run_lua_script` dengan kerangka kerja di bawah ini.

## 1. Menambahkan Tag Animasi (Animation Tags)
Tag animasi (seperti `idle`, `walk`) sangat krusial agar Aseprite Wizard di Godot dapat membedakan animasi.
```lua
local spr = app.activeSprite
if spr then
    -- Membuat tag dari frame 1 ke 4 bernama "idle"
    local tag = spr:newTag(1, 4)
    tag.name = "idle"
    tag.color = app.pixelColor.rgba(255, 0, 0, 255) -- Merah
    tag.aniDir = AniDir.FORWARD
end
app.refresh()
```

## 2. Trimming Kanvas (Auto-Crop)
Membersihkan area transparan agar ukuran kanvas efisien sebelum dikirim ke Godot.
Gunakan perintah `app.command.Trim()` bawaan Aseprite, bukan loop manual piksel.
```lua
-- Memotong seluruh sprite berdasarkan area yang memiliki piksel (membuang ruang kosong)
app.command.Trim()
app.refresh()
...
```

---

## 2. Skill: `cross_check_docs`
- **Path**: `D:/GodotProjects/Lentera-Pudar/.agents/skills\cross_check_docs\SKILL.md`
- **Frontmatter Name**: `cross_check_docs`
- **Description**: Skill audit konsistensi silang yang dipicu via /cross-check-docs. Memeriksa konsistensi antara lore Lentera Pudar, GDD, AGENTS.md, file skill, dan kode implementasi Godot/Aseprite.

```markdown
---
name: cross_check_docs
description: Skill audit konsistensi silang yang dipicu via /cross-check-docs. Memeriksa konsistensi antara lore Lentera Pudar, GDD, AGENTS.md, file skill, dan kode implementasi Godot/Aseprite.
---

# Cross-Check Documents Protocol (/cross-check-docs)

Panduan operasional Supervisor saat perintah `/cross-check-docs` dipicu oleh pengguna.

---

## Checklist Audit 4-Titik

1. **Konsistensi Lore & Identitas (BAB I vs Implementasi)**:
   - Apakah palet warna (#F4B860, #4A6FA5, #2A211C) konsisten di `references/style-guide.md`, shader, dan lighting?
   - Apakah asimetri tangan kutukan (tangan kiri beku) tetap terjaga di semua 8 arah animasi?
2. **Sinkronisasi Aturan Tim (AGENTS.md vs Skills)**:
   - Apakah semua skill yang tercatat di tabel routing (`BAB III`) memiliki file `SKILL.md` nyata di `.agents/skills/`?
   - Apakah tidak ada kontradiksi wewenang antar peran?
3. **Audit Keputusan Desain (references/design-decisions.md)**:
   - Apakah seluruh keputusan struktural baru telah tercatat dengan format ADR?
4. **Audit Integritas File & Kode**:
   - Periksa apakah ada UID yang rusak atau referensi aset yang hilang di folder `res://Scenes/` dan `res://Scripts/`.

## Output Wajib
Laporan tabular hasil audit dengan status `PASSED` / `DISCREPANCY DETECTED` beserta langkah perbaikan konkret.

...
```

---

## 3. Skill: `encounter_pacing`
- **Path**: `D:/GodotProjects/Lentera-Pudar/.agents/skills\encounter_pacing\SKILL.md`
- **Frontmatter Name**: `encounter_pacing`
- **Description**: Standar kurva kesulitan (difficulty curve), ritme encounter musuh, loop risiko-imbalan (risk-reward), dan pacing stamina/kutukan dalam dungeon Lentera Pudar.

```markdown
---
name: encounter_pacing
description: Standar kurva kesulitan (difficulty curve), ritme encounter musuh, loop risiko-imbalan (risk-reward), dan pacing stamina/kutukan dalam dungeon Lentera Pudar.
---

# Encounter Pacing & Combat Rhythm (Game Designer)

Panduan perancangan intensitas pertempuran, pacing musuh, dan kurva emosi pemain di dalam dungeon Lentera Pudar.

---

## 1. Ritme 4-Fase Encounter
1. **Intro (Pengenalan)**: Memperkenalkan jenis ancaman baru dalam lingkungan terkontrol dengan 1 musuh tunggal dekat sumber cahaya.
2. **Escalation (Eskalasi)**: Menggabungkan musuh tersebut dengan variasi pola serangan atau rintangan lantai licin es.
3. **Twist (Tekanan Lingkungan)**: Pertarungan di area gelap dengan sumber cahaya terbatas, memaksa pemain mengandalkan radius syal lentera.
4. **Relief & Reward (Pelepasan & Hadiah)**: Ruangan aman berpenerangan hangat berisi peti harta, sumber pemulihan, atau potongan lore.

---

## 2. Manajemen Ketegangan (Tension vs Relief)
- **Tekanan Kutukan (Curse Pressure)**: Tangan beku protagonis menciptakan urgensi bertarung taktis — jangan biarkan pemain merasa terlalu aman di kegelapan tanpa batas.
- **Lantern Light as Resource/Safety**: Cahaya lentera adalah zona harapan. Pertempuran di luar radius cahaya memiliki risiko tinggi tetapi imbalan kristal energi yang lebih berharga.
- **Telegraph Serangan Jelas**: Serangan musuh wajib memiliki jeda animasi *wind-up* (100-200ms) dengan warna kilau biru dingin `#4A6FA5` agar pemain dapat bereaksi (menghindar/parry).

...
```

---

## 4. Skill: `godot_advanced_ecosystem`
- **Path**: `D:/GodotProjects/Lentera-Pudar/.agents/skills\godot_advanced_ecosystem\SKILL.md`
- **Frontmatter Name**: `godot_advanced_ecosystem`
- **Description**: Pengetahuan mendalam mengenai ekosistem plugin pihak ketiga Godot 4 dan fitur tingkat lanjut (Dialogic 2, Phantom Camera, Pathfinding AI) untuk pembuatan 2D RPG kelas atas.

```markdown
---
name: godot_advanced_ecosystem
description: Pengetahuan mendalam mengenai ekosistem plugin pihak ketiga Godot 4 dan fitur tingkat lanjut (Dialogic 2, Phantom Camera, Pathfinding AI) untuk pembuatan 2D RPG kelas atas.
---

# Godot 4 Advanced Ecosystem & Plugins

Skill ini menjamin AI tidak menulis sistem rumit dari nol secara *hardcode* yang akan merusak performa *game*. AI diwajibkan menggunakan standar industri pihak ketiga berikut ini untuk RPG Lentera Pudar.

## 1. Sistem Dialog (Dialogic 2)
Jangan pernah menggunakan *Node* `Label` biasa dan logika `if/else` di skrip pemain untuk percakapan.
- **Wajib menggunakan plugin Dialogic 2**.
- Dialogic memisahkan narasi dari kode murni. Semua percakapan dibuat di *Timeline Editor* bawaan Dialogic.
- **Integrasi Kode**: Untuk memicu dialog via skrip, gunakan API resmi:
  ```gdscript
  Dialogic.start("timeline_name")
  # Menggunakan signal untuk komunikasi dua arah dengan game logic
  Dialogic.signal_event.connect(_on_dialogic_signal)
  ```

## 2. Sistem Kamera & Screen Shake (Phantom Camera)
Jangan membuat skrip pergerakan kamera manual menggunakan `lerp` atau fungsi acak untuk *Screen Shake*.
- **Wajib menggunakan plugin Phantom Camera**.
- Gunakan mode `Simple Follow` ke karakter Protagonis.
- **Screen Shake Halus**: Untuk efek *shake* (misal saat diserang), integrasikan `FastNoiseLite` (Noise 2D) untuk mengatur `offset` kamera, BUKAN nilai `randf()` murni agar goncangan terlihat organik dan tidak patah-patah.

## 3. Navigasi AI (AStarGrid2D / NavigationAgent2D)
- Jangan gunakan raycast manual untuk pergerakan musuh *top-down*.
- Gunakan `AStarGrid2D` untuk *grid-based movement* (musuh bergerak kotak per kotak), ATAU gunakan `NavigationAgent2D` dengan `NavigationRegion2D` untuk pergerakan bebas namun menghindari tembok.

...
```

---

## 5. Skill: `godot_engine_mastery`
- **Path**: `D:/GodotProjects/Lentera-Pudar/.agents/skills\godot_engine_mastery\SKILL.md`
- **Frontmatter Name**: `godot_engine_mastery`
- **Description**: Penguasaan tingkat tinggi terhadap arsitektur Godot 4 untuk game 2D RPG, termasuk penggunaan plugin pihak ketiga dan optimalisasi render.

```markdown
---
name: godot_engine_mastery
description: Penguasaan tingkat tinggi terhadap arsitektur Godot 4 untuk game 2D RPG, termasuk penggunaan plugin pihak ketiga dan optimalisasi render.
---

# Godot 4 Engine Mastery

Skill ini memastikan implementasi teknis di dalam *engine* tidak ketinggalan zaman dan bebas dari masalah *blurring* piksel.

## 1. Integrasi Aseprite Wizard (Pihak Ketiga)
- Ekspor manual `.png` dan pemotongan `SpriteFrames` secara manual di Godot sudah usang.
- **Wajib menggunakan *plugin* Aseprite Wizard**.
- Alur: AI menginstruksikan penyimpanan *file* sumber sebagai `.aseprite` murni, lalu Godot (via plugin ini) akan secara otomatis membaca *tags* Aseprite dan membangkitkan `SpriteFrames`.

## 2. Praktik Terbaik 2D Pixel Art Rendering
- `Texture Filter` = Nearest (wajib untuk 100% ketajaman piksel).
- `Integer Scaling` = On (mencegah distorsi *shimmering* saat jendela diubah ukuran).
- `Y-Sorting` diaktifkan pada seluruh *Node* karakter agar tumpang tindih visual benar.

## 3. Sistem Pencahayaan (Lighting & Shaders)
Karena Lentera Pudar bergantung pada cahaya hangat melawan kutukan dingin, ini hukum mutlaknya:
- Pencahayaan tidak boleh dilakukan dengan menggambar piksel kuning transparan di Aseprite.
- Syal kuning Protagonis wajib menggunakan `PointLight2D` di Godot.
- Kegelapan ruangan diatur menggunakan `CanvasModulate` gelap (`#2A211C`), sehingga `PointLight2D` bisa "melubangi" kegelapan tersebut.
- Animasi tangan "Kutukan Pudar" harus menggunakan `ShaderMaterial` (*CanvasItem shader*) untuk memberikan efek berdenyut, bukan sekadar animasi warna datar.

## 5. Partikel Retro (Pixel-Perfect GPUParticles2D)
Efek sihir dan serpihan es Kutukan Pudar wajib menggunakan `GPUParticles2D`, namun tidak boleh terlihat seperti grafis modern yang kabur (*blurry*).
- Di tingkat Proyek: `Project Settings > Rendering > Textures > Canvas Textures > Default Texture Filter` HARUS di-set ke **Nearest**.
- Pada Node `GPUParticles2D`: Di bawah `CanvasItem > Texture > Filter`, pastikan tersetel ke **Nearest**.
...
```

---

## 6. Skill: `godot_rpg_architecture`
- **Path**: `D:/GodotProjects/Lentera-Pudar/.agents/skills\godot_rpg_architecture\SKILL.md`
- **Frontmatter Name**: `godot_rpg_architecture`
- **Description**: Standar arsitektur tingkat lanjut untuk pembuatan game RPG di Godot 4. Mencakup Finite State Machine (FSM) dan manajemen data berbasis Custom Resources (Inventory & Stats).

```markdown
---
name: godot_rpg_architecture
description: Standar arsitektur tingkat lanjut untuk pembuatan game RPG di Godot 4. Mencakup Finite State Machine (FSM) dan manajemen data berbasis Custom Resources (Inventory & Stats).
---

# Godot 4 RPG Architecture Mastery

Skill ini memastikan kerangka kerja (*framework*) RPG Lentera Pudar dapat diskalakan (*scalable*) dari Tahap 1 hingga tahap rilis tanpa harus menulis ulang kode dari nol.

## 1. Sistem Logika Karakter (Finite State Machine / FSM)
Jangan gunakan percabangan *boolean* yang berantakan (`if is_attacking`, `if is_walking`). Godot 4 mewajibkan penggunaan FSM.

- **Untuk Protagonis (Node-Based FSM)**:
  Karena protagonis akan memiliki banyak aksi (*Idle*, *Walk*, *Hurt*, *Dash*), gunakan pola *Node-based*.
  1. Buat *Node* induk `StateMachine`.
  2. Buat *class* dasar `State` dengan fungsi `enter()`, `exit()`, `physics_update()`.
  3. Jadikan setiap aksi (misal `IdleState.gd`) sebagai *Node* anak dari `StateMachine`.

- **Untuk Musuh Sederhana (Enum-Based FSM)**:
  ```gdscript
  enum State { IDLE, CHASE, ATTACK }
  var current_state = State.IDLE
  ```

## 2. Arsitektur Data RPG (Stats & Inventory)
**Aturan Mutlak:** Jangan pernah menyimpan data (seperti HP, Damage, nama Item) di dalam *Node*. *Node* hanya untuk visual dan perilaku. Gunakan **Custom Resources**.

- **Sistem Status (Stats System)**:
  Buat sebuah skrip yang mewarisi `Resource` (misal `class_name CharacterStats`).
  Data HP, Pertahanan, dan tingkat Kutukan Pudar disimpan sebagai *file* `.tres` dan dimasukkan ke dalam `Player.tscn`.
...
```

---

## 7. Skill: `godot_systems_mastery`
- **Path**: `D:/GodotProjects/Lentera-Pudar/.agents/skills\godot_systems_mastery\SKILL.md`
- **Frontmatter Name**: `godot_systems_mastery`
- **Description**: Pangkalan Data untuk Sistem Inti (Core Systems) Godot 4 tingkat lanjut. Mencakup keamanan Save/Load, Background Loading Screen, dan optimasi UI Pixel Art.

```markdown
---
name: godot_systems_mastery
description: Pangkalan Data untuk Sistem Inti (Core Systems) Godot 4 tingkat lanjut. Mencakup keamanan Save/Load, Background Loading Screen, dan optimasi UI Pixel Art.
---

# Godot 4 Core Systems & Commercial Architecture

Skill ini adalah pilar terakhir yang memastikan *game* tidak hanya bisa dimainkan, tetapi layak dirilis secara komersial tanpa celah keamanan (*security flaw*) atau masalah *loading*.

## 1. Keamanan Sistem Save/Load
Jangan pernah menyimpan progres pemain (Save Data) menggunakan `ResourceSaver` (file `.tres`).
- **Risiko Keamanan**: File *Resource* Godot dapat disisipi kode injeksi berbahaya. Jika pemain mengunduh file *save* dari internet, komputer mereka bisa diretas.
- **Standar Wajib (JSON/Binary)**: AI wajib menggunakan `JSON.stringify()` melalui `FileAccess` untuk membaca dan menulis data *save*. Ini 100% aman karena JSON murni berisi data, bukan skrip eksekusi. Selalu simpan di direktori `user://`.

## 2. Background Loading (Layar Pemuatan Async)
Untuk mencegah *game* macet ( *freeze*) saat memasuki *dungeon* yang luas, gunakan pemuatan asinkron (*Threaded Loading*).
- **Aturan Mutlak**: *Scene Tree* Godot tidak mendukung multithreading. Jangan pernah memanggil `add_child` atau `change_scene` dari *background thread*.
- **Pola Kode**:
  1. Mulai dengan `ResourceLoader.load_threaded_request("res://scene.tscn")`.
  2. Gunakan fungsi `_process` di layar *loading* untuk mengecek status `ResourceLoader.load_threaded_get_status`.
  3. Setelah mencapai 100%, baru jalankan `get_tree().change_scene_to_packed()`.

## 3. Optimasi UI Pixel Art (Control Nodes)
Agar UI (seperti kotak percakapan, menu, dan teks) tidak hancur atau kabur (*blurry*):
- Jangan menggunakan `Sprite2D` di dalam *Control Node*. Gunakan `TextureRect` atau `Panel`.
- Gunakan fitur **9-Patch Rect margins** pada `StyleBoxTexture` agar ujung kotak dialog melar dengan sempurna tanpa mendistorsi piksel pinggiran.
- **Pengaturan Font Wajib**: Saat mengimpor *font* piksel (seperti `.ttf`), pergi ke tab *Import* dan matikan `Antialiasing`, matikan `Hinting`, dan matikan `Subpixel Positioning`. Pakai ukuran asli (*native size*) dari font tersebut.

## 4. Performa Pertarungan (Object Pooling)
Jangan pernah memanggil `instantiate()` dan `queue_free()` secara berulang untuk proyektil ajaib atau panah di tengah pertarungan, ini akan menyebabkan *stuttering* (FPS Drop).
...
```

---

## 8. Skill: `level_layout_design`
- **Path**: `D:/GodotProjects/Lentera-Pudar/.agents/skills\level_layout_design\SKILL.md`
- **Frontmatter Name**: `level_layout_design`
- **Description**: Standar perancangan tata letak dungeon 2D top-down (low top-down 3/4), navigasi landmark, room loop, distribusi zona gelap-terang, dan gating mekanik untuk Lentera Pudar.

```markdown
---
name: level_layout_design
description: Standar perancangan tata letak dungeon 2D top-down (low top-down 3/4), navigasi landmark, room loop, distribusi zona gelap-terang, dan gating mekanik untuk Lentera Pudar.
---

# Level Layout Design (Game Designer)

Panduan perancangan level dungeon misterius-hangat untuk game 2D Pixel RPG top-down di Godot 4.

---

## 1. Prinsip Spasial & Perspektif
- **Perspektif**: Low top-down (sudut pandang 3/4 Zelda-like).
- **Grid Tile**: `32x32 px`. Koridor minimum lebar 2 tile (64px) agar pergerakan 8-arah terasa leluasa tanpa terjepit collision.
- **Room Loops**: Hindari lorong buntu linear yang membosankan (*dead-ends*). Buat pola sirkuit/looping di mana pemain bisa kembali ke area utama setelah membuka jalan pintas (*shortcut*).

---

## 2. Navigasi & Landmark
- **Visual Gating**:
  - Pintu es kristal biru (memerlukan api lentera untuk mencairkannya).
  - Jurang/keretakan lantai dungeon gelap.
  - Altar batu kuno dengan ukiran lentera sebagai titik simpan (*checkpoint* / *bonfire*).
- **Landmark Jelas**: Setiap ruangan besar wajib memiliki satu objek dominan yang mudah diingat (misal: patung kristal es raksasa di tengah, kolam air beku, atau reruntuhan tiang bercahaya).

---

## 3. Distribusi Kegelapan & Cahaya
- **Kegelapan Dasar**: Diatur oleh `CanvasModulate` `#2A211C`.
- **Cahaya Karakter**: Radius `PointLight2D` syal kuning (~150-200px) menjadi radius visibilitas pemain.
...
```

---

## 9. Skill: `mcp_api_mastery`
- **Path**: `D:/GodotProjects/Lentera-Pudar/.agents/skills\mcp_api_mastery\SKILL.md`
- **Frontmatter Name**: `mcp_api_mastery`
- **Description**: Pemahaman mendalam mengenai arsitektur internal WebSocket Bridge dari server MCP Lentera (Godot dan Aseprite). Berisi batasan batas waktu (timeout) dan mekanisme koneksi.

```markdown
---
name: mcp_api_mastery
description: Pemahaman mendalam mengenai arsitektur internal WebSocket Bridge dari server MCP Lentera (Godot dan Aseprite). Berisi batasan batas waktu (timeout) dan mekanisme koneksi.
---

# Lentera MCP API & Bridge Mastery

Skill ini memastikan AI memahami cara kerja alat internalnya sendiri, mencegah kegagalan eksekusi (*timeout*) atau salah paham mengenai status koneksi Aseprite dan Godot.

## 1. Arsitektur Jaringan (WebSocket Bridge)
Baik `lentera-aseprite-mcp` maupun `lentera-godot-mcp` menggunakan arsitektur **Node.js WebSocket Server**.
- Aseprite bertindak sebagai **WS Client** yang terhubung ke *port* **8099**.
- Godot bertindak sebagai **WS Client** yang terhubung ke *port* **8098**.

## 2. Mekanisme Tunggu Otomatis (Auto-Wait Loop)
AI **tidak perlu** khawatir jika Godot atau Aseprite belum sepenuhnya terbuka saat mengirim perintah. 
Fungsi `bridge.send()` di dalam kode MCP memiliki mekanisme *polling*:
```typescript
for (let i = 0; i < 150; i++) {
  await new Promise(r => setTimeout(r, 100)); // Menunggu hingga maksimal 15 detik
}
```
Jika setelah 15 detik koneksi gagal, sistem akan mengirim *error*. Saat itu terjadi, AI harus meminta *User* untuk membuka Aseprite/Godot dan memastikan *plugin Lentera Bridge* aktif.

## 3. Batasan Eksekusi Kritis (Timeouts)
Ini adalah parameter mutlak yang tidak boleh dilanggar oleh AI:
- **Aseprite MCP (`COMMAND_TIMEOUT_MS = 15000`)**: Jangan pernah mengirim skrip Lua yang mengandung *loop* tak berujung atau kalkulasi piksel masif yang memakan waktu lebih dari **15 detik**. Aseprite akan *timeout*.
- **Godot MCP (`COMMAND_TIMEOUT_MS = 20000`)**: Operasi `run_gdscript` harus selesai dalam waktu **20 detik**. Jika AI butuh meng- *import* aset berat, bagi menjadi beberapa perintah.

## 4. Keamanan & Isolasi
...
```

---

## 10. Skill: `orchestration_protocol`
- **Path**: `D:/GodotProjects/Lentera-Pudar/.agents/skills\orchestration_protocol\SKILL.md`
- **Frontmatter Name**: `orchestration_protocol`
- **Description**: Protokol orkestrasi untuk Supervisor Agent dalam memecah task besar, mendelegasikan ke sub-agent (Hub-and-Spoke), menetapkan kriteria selesai eksplisit, memverifikasi artifact fisik, dan mengeksekusi Pola B.

```markdown
---
name: orchestration_protocol
description: Protokol orkestrasi untuk Supervisor Agent dalam memecah task besar, mendelegasikan ke sub-agent (Hub-and-Spoke), menetapkan kriteria selesai eksplisit, memverifikasi artifact fisik, dan mengeksekusi Pola B.
---

# Orchestration Protocol (Supervisor Agent)

Pustaka protokol untuk memandu Supervisor dalam mengelola alur kerja multi-agent secara sekuensial, terukur, dan bebas dari halusinasi/teater.

---

## 1. Prinsip Hub-and-Spoke
- Seluruh komunikasi berpusat pada Supervisor.
- Sub-agent tidak berkomunikasi langsung secara bebas (mencegah race condition dan context bloat).
- Supervisor bertanggung jawab menyintesis hasil dan melaporkan ke pengguna.

---

## 2. Siklus Delegasi 5 Langkah
1. **Identifikasi & Dekomposisi**: Pecah tujuan pengguna menjadi sub-task berurutan dengan dependensi yang jelas (lihat tabel routing di `AGENTS.md`).
2. **Penugasan dengan Kriteria Selesai Eksplisit**: Delegasikan ke agent yang tepat. Sertakan batas kerja yang tidak ambigu (misal: "Hasilkan 8 file spritesheet PNG 48x48 dan konfirmasi palet heksadesimal").
3. **Verifikasi Bukti Fisik (Artifact Gate)**: Setelah sub-agent melapor, periksa keberadaan artifact fisik di filesystem (path file, diff, tool call log, atau screenshot). Dilarang percaya klaim naratif semata.
4. **Penanganan Kegagalan & Rejection Loop**: Jika artifact tidak memenuhi standar QC, kembalikan ke sub-agent dengan feedback baris/poin spesifik. Maksimal 3x percobaan sebelum mengubah strategi dan eskalasi ke user.
5. **Laporan Akhir Faktual**: Sajikan rangkuman ringkas berisi daftar tautan artifact nyata kepada pengguna.

---

## 3. Protokol Pola B (Dual-Perspective)
- **Kapan Digunakan**: Hanya untuk keputusan arsitektur struktural berbiaya tinggi (contoh: save system, combat core architecture) atau saat diminta eksplisit oleh user.
- **Format Output Wajib**:
...
```

---

## 11. Skill: `pixel_art_animation_mastery`
- **Path**: `D:/GodotProjects/Lentera-Pudar/.agents/skills\pixel_art_animation_mastery\SKILL.md`
- **Frontmatter Name**: `pixel_art_animation_mastery`
- **Description**: Hukum mutlak untuk proporsi 32x32px, teori warna (Hue Shifting), dan prinsip animasi Walk Cycle Top-Down untuk menjaga konsistensi gaya Misterius-Hangat Lentera Pudar.

```markdown
---
name: pixel_art_animation_mastery
description: Hukum mutlak untuk proporsi 32x32px, teori warna (Hue Shifting), dan prinsip animasi Walk Cycle Top-Down untuk menjaga konsistensi gaya Misterius-Hangat Lentera Pudar.
---

# 32x32 Pixel Art & Animation Mastery

Skill ini memastikan AI tidak menghasilkan *pixel art* yang kaku, proporsi yang aneh, atau warna yang kotor (*muddy*). Patuhi standar estetika ini secara absolut.

## 1. Proporsi Karakter (32x32 Top-Down)
Karena kanvas sangat kecil, realisme proporsi manusia asli tidak memungkinkan.
- **Proporsi Klasik RPG (Stylized)**: Kepala harus mengambil **1/3** dari total tinggi tubuh (sekitar 10-12 piksel dari 32 piksel). Ini memastikan rambut abu-abu berantakan Protagonis dan warna wajahnya tetap bisa dibaca oleh pemain, namun **tidak boleh** terlalu besar hingga terlihat lucu/imut (*cute chibi*). Nuansa harus tetap misterius.
- **Perspektif Low Top-Down (Stardew-like)**: Kamera menunduk sekitar 20 derajat (sesuai parameter `low top-down` Pixellab). Karakter terlihat tegak dari depan untuk memamerkan detail pakaian dan tangan bersinar, dengan sedikit bahu yang terlihat.
- Jangan memenuhi seluruh 32 piksel, sisakan 1-2 piksel kosong sebagai bantalan ( *padding*).

## 2. Animasi Walk Cycle & Jebakan Sub-Pixel (Wajah Meleleh)
*(Catatan: Pixellab secara otomatis menghitung fase pergerakan ini lewat template `walking-4-frames` atau `walking-6-frames`, namun teori ini tetap menjadi standar validasi kita)*.
Setiap siklus berjalan (*Walk Cycle*) arah (Atas, Bawah, Kiri, Kanan) wajib memiliki 4 pose utama:
1. **Contact**: Kedua kaki menyentuh tanah (jarak terjauh).
2. **Down (Squash)**: Titik terendah tubuh (bobot menekan).
3. **Passing**: Satu kaki menopang, kaki lain melewati.
4. **Up (Stretch)**: Titik tertinggi tubuh.
- **Exaggeration**: Gerakan lengan dan ayunan kepala (*head bobbing*) harus dilebih-lebihkan.
- **Jebakan Sub-Pixel (Face Melting)**: Jika piksel terlihat "berenang" atau wajah karakter tampak "meleleh" saat berjalan di *game*, itu karena posisi objek berada di koordinat pecahan (misal: X=10.4). Animasi *Pixel Art* 32x32px HARUS selalu mengunci (*snap*) posisi ke angka bulat murni (Integer). Hindari rotasi miring kecuali menggunakan *shader* khusus.

## 3. Sub-Pixel Animation (Nafas & Idle)
Bagaimana membuat Protagonis terlihat "bernapas" perlahan jika menaikkan dadanya 1 piksel terlihat seperti melompat keras?
- **Cluster Shifting**: Jangan pindahkan garis tepi (*outline*). Ubah **warna** (*anti-aliasing*) di perbatasan kluster piksel. Dengan menaikkan/menurunkan kecerahan 1 baris piksel di dalam dada, mata manusia akan tertipu dan melihat pergerakan sehalus 0.5 piksel. Ini adalah rahasia animasi *Idle* AAA di resolusi 32x32px.

## 4. Teori Warna: Misterius-Hangat (Hue Shifting)
...
```

---

## 12. Skill: `pixellab_ecosystem`
- **Path**: `D:/GodotProjects/Lentera-Pudar/.agents/skills\pixellab_ecosystem\SKILL.md`
- **Frontmatter Name**: `pixellab_ecosystem`
- **Description**: Keahlian penuh dalam memaksimalkan kapabilitas Pixellab Cloud dan Plugin untuk Tileset, Karakter 8 Arah, dan UI Assets.

```markdown
---
name: pixellab_ecosystem
description: Keahlian penuh dalam memaksimalkan kapabilitas Pixellab Cloud dan Plugin untuk Tileset, Karakter 8 Arah, dan UI Assets.
---

# Pixellab Ecosystem Maximization

Skill ini mencegah AI memperlakukan Pixellab hanya sebagai generator karakter semata.

## 1. Karakter (Mode v3 8-Arah)
- Menggunakan *Prompt-Driven Generation* dengan deskripsi teks murni (tanpa memaksakan *blueprint* kaku).
- Mampu melakukan *Rotation & Multi-Angle* secara otomatis (menghasilkan variasi 8 arah sejati).
- Mendukung fitur *One-click Animation* (walk, idle, attack, dsb) baik menggunakan preset teks maupun *skeleton-based control*.

### Kamus Parameter Tingkat Lanjut (Krusial untuk Konsistensi)
Saat menggunakan plugin Aseprite atau *prompting* tingkat lanjut, parameter ini wajib diperhatikan agar estetika Lentera Pudar tetap seragam:
- **Generation Mode**: 
  - `v3`: Wajib digunakan untuk Karakter dan Animasi. Mengotomatisasi struktur dasar, arah rotasi, dan penyiapan *template* gerak.
  - `pro`: Untuk aset non-karakter dengan kualitas tertinggi (misal UI resolusi tinggi atau lukisan potret).
  - `standard`: Untuk objek peta dasar atau *prototyping* cepat.
- **Body Type**: `humanoid` (untuk Protagonis & NPC bipedal) atau `quadruped` (untuk monster kaki empat).
- **Camera View**: 
  - `low top-down`: Kamera menunduk ~20 derajat. Karakter terlihat lebih tegak (mirip Stardew Valley). **Ini adalah gaya yang kita pakai untuk Lentera Pudar.**
  - `high top-down`: Kamera menunduk tajam ~35 derajat (mirip Zelda lawas).
  - `sidescroller`: Untuk game *platformer* murni.
- **Outline Style**:
  - `single color black outline`: Garis luar hitam tegas (Bagus untuk pemisahan *background* gelap).
  - `selective outline`: Garis luar parsial agar gambar tidak kaku.
  - `lineless`: Murni tanpa garis luar (bergantung pada kontras warna).

...
```

---

## 13. Skill: `player_psychology_engagement`
- **Path**: `D:/GodotProjects/Lentera-Pudar/.agents/skills\player_psychology_engagement\SKILL.md`
- **Frontmatter Name**: `player_psychology_engagement`
- **Description**: Panduan psikologi pemain untuk Psychology Agent (Consultant). Digunakan saat mereview motivasi dialog NPC, atmosferik dread vs hope, resonansi emosional, dan kejelasan bahasa tubuh pixel art.

```markdown
---
name: player_psychology_engagement
description: Panduan psikologi pemain untuk Psychology Agent (Consultant). Digunakan saat mereview motivasi dialog NPC, atmosferik dread vs hope, resonansi emosional, dan kejelasan bahasa tubuh pixel art.
---

# Player Psychology & Emotional Engagement (Psychology Agent)

Panduan konsultasi psikologi pemain untuk mengevaluasi resonansi emosional, kepuasan loop gameplay, dan keselarasan karakter di Lentera Pudar.

---

## 1. Sifat Peran: Konsultan Kritis (Bukan Pemilik Tahap)
- Psychology Agent **BUKAN** pemilik tahap independen di pipeline linear.
- Bekerja sebagai **Reviewer/Consultant** terhadap rancangan yang SUDAH DIBUAT oleh Game Designer atau Art Director.
- Fokus: Memberikan catatan kritis dan actionable (bukan pujian kosong) terkait motivasi, dampak emosi, dan kejelasan ekspresi.

---

## 2. Pilar Resonansi Emosional Lentera Pudar
1. **Duality of Warmth & Coldness (The Triad Resonance)**:
   - Kehangatan `#F4B860` harus terasa melegakan setelah melewati lorong es biru `#4A6FA5` yang menakutkan.
   - Jangan biarkan game terasa 100% dingin atau 100% hangat; kekuatannya ada pada kontras tajam.
2. **Kutukan Pudar (Apathy Plague)**:
   - NPC yang terkena wabah tidak sekadar pingsan, mereka kehilangan hasrat hidup dan perlahan membeku. Dialog mereka bernada pasrah, dingin, atau linglung.
   - Tindakan menyinari mereka dengan lentera harus memicu reaksi kehangatan emosional yang menyentuh hati pemain.
3. **Bahasa Tubuh & Pose Karakter (Pixel Art Review)**:
   - Dalam resolusi 32x32px, emosi disampaikan lewat siluet dan pose (misal: bahu merosot untuk keputusasaan, kepala tegak bersyal berkibar untuk tekad protagonis).
   - Pastikan pose karakter menyampaikan status emosional dengan jelas tanpa harus bergantung pada teks deskripsi panjang.

...
```

---

## 14. Skill: `qc_check`
- **Path**: `D:/GodotProjects/Lentera-Pudar/.agents/skills\qc_check\SKILL.md`
- **Frontmatter Name**: `qc_check`
- **Description**: Standar eksekusi Quality Control (QC Gate) via perintah /qc-check. Menjalankan checklist 3 lapis (Visual, Functional, Consistency) dan pencatatan pola reject ke references/qc-patterns.md.

```markdown
---
name: qc_check
description: Standar eksekusi Quality Control (QC Gate) via perintah /qc-check. Menjalankan checklist 3 lapis (Visual, Functional, Consistency) dan pencatatan pola reject ke references/qc-patterns.md.
---

# Quality Control Inspection Protocol (/qc-check)

Protokol kontrol kualitas wajib yang dijalankan oleh **QC Agent** sebelum menyerahkan hasil kerja ke Supervisor/User.

---

## 3 Lapis Checklist QC

### 1. Visual QC Gate
- [ ] Resolusi kanvas tepat `32x32 px` (atau `48x48 px` framing seragam dengan pivot tengah-bawah).
- [ ] Outline hitam solid `#000000` / `#141013` tanpa *color bleed* atau piksel liar.
- [ ] Kepatuhan palet: Kuning Syal `#F4B860`, Biru Kutukan `#4A6FA5`, Netral Gelap `#2A211C`.
- [ ] Asimetri tangan kiri beku konsisten di semua arah (terutama saat menghadap barat/timur).

### 2. Functional QC Gate
- [ ] Skrip GDScript bebas dari error parse / compile error (static typing valid).
- [ ] Animasi berputar mulus dengan framerate baku 8 FPS (125ms per frame) dan looping stabil.
- [ ] Collision shape terpasang rapi (tidak melayang atau menembus dinding).
- [ ] Shader `CursedHand.gdshader` dan `PointLight2D` menyala tanpa mengorbankan framerate (60 FPS stabil).

### 3. Consistency QC Gate
- [ ] Penamaan animasi kardinal seragam (`[aksi]_[arah]`: `idle_south`, `walk_north-east`).
- [ ] File resource Godot (`.tres`, `.tscn`) memiliki dependensi valid tanpa UID rusak.
- [ ] Struktur scene rapi sesuai hierarki standar Lentera Pudar.

...
```

---

## 15. Skill: `visual_pipeline_automation`
- **Path**: `D:/GodotProjects/Lentera-Pudar/.agents/skills\visual_pipeline_automation\SKILL.md`
- **Frontmatter Name**: `visual_pipeline_automation`
- **Description**: "Panggil skill ini setiap kali kamu diminta untuk membuat, merancang, atau men-generate karakter/objek pixel art baru untuk proyek Lentera Pudar (terutama menggunakan Pixellab dan Aseprite)."

```markdown
---
name: visual_pipeline_automation
description: "Panggil skill ini setiap kali kamu diminta untuk membuat, merancang, atau men-generate karakter/objek pixel art baru untuk proyek Lentera Pudar (terutama menggunakan Pixellab dan Aseprite)."
---

# Visual Pipeline Automation (Prompt-Driven Workflow)

Skill ini adalah implementasi praktis dari BAB VI di `AGENTS.md`. Kamu WAJIB mengikuti urutan ini demi mendapatkan hasil yang luwes dan estetis.

## Fase 1: Prompt Generation (Pixellab MCP v3)
1. Analisis elemen *lore* dari permintaan pengguna (misal: pakaian gelap, rambut abu-abu, syal kuning, tangan balutan perban biru es).
2. Buat teks *prompt* dalam bahasa Inggris yang padat dan komprehensif. Wajib sertakan instruksi kualitas seperti `hard edges, flat colors, no color bleed, pure pixel art`.
3. Panggil tool Pixellab `create_character` dengan parameter absolut berikut:
   - `mode="v3"` (Untuk 8-directional sejati).
   - `camera_view="low top-down"` (Perspektif ~20 derajat Stardew-like).
   - `body_type="humanoid"`
   - `size="32x32"` atau `48x48`
   - `details="medium detail"` dan `outline="selective outline"`.
4. Tunggu hasil *generation* dan minta konfirmasi (*review*) dari pengguna apakah hasilnya sudah memuaskan. Jika belum, lakukan re-roll dengan sedikit penyesuaian *prompt*.

## Fase 2: Pembersihan & Kurasi Warna
1. Unduh sprite karakter statis yang telah disetujui.
2. Gunakan Aseprite atau Python script untuk memverifikasi warna. 
3. *Wajib Lore Check*: Jika warna syal tidak tepat `#F4B860` atau tangan tidak tepat `#4A6FA5`, gunakan fungsi *Replace Color* untuk memaksa piksel-piksel tersebut sesuai dengan *lore*.

## Fase 3: Animasi (Pixellab MCP)
1. Setelah karakter statis disetujui dan dibersihkan, gunakan tool `animate_character` di Pixellab.
2. Pilih *template* `breathing-idle` (4 frame) untuk *idle* dan `walking-4-frames` untuk *walk*.
3. Unduh hasil 64 frame (8 arah × 4 frame × 2 animasi).

...
```

---

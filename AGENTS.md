# Lentera Pudar — Project Rules & System Prompt

> **Dokumen ini adalah sumber kebenaran (Source of Truth) utama untuk AI Asisten Teknis.** Wajib dibaca secara otomatis di setiap prompt untuk memastikan konsistensi kode, desain, dan arsitektur Lentera Pudar.

---

## BAB I: IDENTITAS & DUNIA (LORE)

- **Judul Proyek**: Lentera Pudar — 2D Pixel RPG dungeon top-down.
- **Engine**: Godot 4.7.1, Renderer Compatibility (Platform: PC Windows, Kontrol: Keyboard + Mouse).
- **Tema Visual**: Misterius-hangat. Pixel Art 32x32px (gaya semi-detailed).
- **Warna & Rendering**: 
  - Tiga warna di bawah adalah **warna dominan / penentu mood** proyek, bukan satu-satunya warna yang boleh dipakai. Warna turunan (kulit, rambut, dll) boleh ada selama tetap harmonis dalam satu palet gelap-hangat.
  - Kuning Hangat (`#F4B860`), Biru Dingin (`#4A6FA5`), Netral Gelap (`#2A211C`).
  - Pencampuran warna hanya terjadi dinamis via `PointLight2D` & `CanvasModulate` gelap di Godot. Semua impor tekstur *Lossless*.
- **Lore Inti**:
  - **Kutukan Pudar**: Wabah apatis yang membekukan warga menjadi patung kristal es biru.
  - **Protagonis**: Satu karakter tunggal tanpa kelas (*Class-less*). Pakaian gelap, rambut abu acak, bersyal kuning terang (sumber cahaya `PointLight2D`), dan tangan kiri dibalut perban yang memancarkan urat es biru (Pudar).

## BAB II: PROTOKOL PERILAKU AI (ASISTEN TEKNIS)

- **Identitas**: Bertindak murni sebagai Asisten Teknis / *Software Engineer*. **DILARANG KERAS** menggunakan *roleplay*, persona fiktif, sebutan berlebihan, atau mensimulasikan diskusi antar agen.
- **Pipeline Visual (Maximized)**: Urutan kerja aset pixel art menggunakan **Prompt-Driven Generation**: **Pixellab MCP** (membuat karakter via prompt teks detail) → **Aseprite** (pembersihan *auto-crop*, pewarnaan ulang jika perlu, & penandaan animasi oleh AI) → **Godot** (Auto-import cerdas via **Aseprite Wizard Plugin** + Implementasi efek *Lighting/Shader*).
- **Batasan Kemampuan Visual**: AI akan fokus pada pembuatan *prompt* yang kuat dan mengandalkan mesin Pixellab untuk interpretasi estetika. Koreksi warna (*color mapping*) akan dilakukan di Aseprite pasca-generate.
- **Self-Research & Adaptive Problem Solving**: Jika menemui keterbatasan pengetahuan atau kendala teknis, AI **wajib melakukan riset mandiri** terlebih dahulu — membaca dokumentasi, menelusuri kode sumber tool yang relevan, atau melakukan uji coba terkontrol — sebelum menyatakan "tidak bisa". Laporkan temuan secara faktual dan langsung. Tidak ada drama, tidak ada kata-kata berlebihan, tidak ada harapan palsu.
- **Penanganan Kegagalan MCP**: Jika *tool* UI MCP gagal, langsung gunakan jalur alternatif: eksekusi skrip Lua di Aseprite atau EditorScript/GDScript di Godot. Jika gagal lebih dari 3 kali beruntun pada pendekatan yang sama, ubah strategi dan laporkan ke pengguna sebelum mencoba lagi.
- **Aturan Prioritas**: Selalu selesaikan Tahap 1 sebelum memikirkan tahap berikutnya. Jangan menyiapkan sistem atau aset yang belum diperlukan (contoh: jangan membuat struktur data musuh jika visual Protagonis belum selesai 100%).
- **Validasi Wajib**: Sebelum menganggap sebuah kode atau aset selesai, AI WAJIB menyertakan bukti nyata — `take_screenshot` saat *play test* di Godot, atau log tanpa *error* merah di konsol.
- **Komunikasi**: Berikan solusi teknis langsung, sertakan *file path* dengan jelas, dan jelaskan konsep baru dalam satu kalimat awam jika diperlukan.
- **Sinkronisasi & Riset Komprehensif**: Setiap kali ada penambahan, penghapusan, atau perubahan konsep/fitur, AI **wajib** melakukan riset tanpa terkecuali untuk mencegah adanya bagian yang bertentangan atau kedaluwarsa. Riset dan sinkronisasi ini harus mencakup:
  - **Seluruh Direktori Proyek**: `D:\GodotProjects\Lentera-Pudar`, `D:\GodotProjects\lentera-godot-mcp`, `D:\GodotProjects\lentera-aseprite-mcp`.
  - **Seluruh Domain Ekosistem**: Pixellab, Cloud, Aseprite, dan Godot.
- **Modifikasi Aturan**: Perubahan pada file `AGENTS.md` ini WAJIB atas persetujuan pengguna.
- **Arsitektur Multi-Agent (Skills & Subagents)**:
  - **Self-Reflection**: AI sebagai *Orchestrator* wajib mengevaluasi logika skrip secara internal sebelum mengeksekusinya di Godot/Aseprite untuk menjamin akurasi 100%.
  - **Penggunaan Skills**: AI wajib menyimpan rumus kompleks, gaya kode baku, atau alur kerja khusus (seperti instruksi *prompt* karakter) ke dalam folder `.agents/skills/`. AI akan memanggil *skill* ini alih-alih memikirkannya dari nol.
  - **Penggunaan Subagents**: AI wajib mendelegasikan tugas riset eksternal yang kompleks (misal: mencari sintaks plugin *Aseprite Wizard* versi terbaru) kepada `browser_subagent` untuk menjaga akurasi konteks.
  - **Fitur Otodidak (`/learn`)**: AI wajib mematuhi pemanggilan memori via `/learn` oleh pengguna untuk mengabadikan solusi teknis yang sulit ke dalam arsitektur otak AI.


## BAB III: SPESIFIKASI GAMEPLAY & SISTEM

*(Telah Dihapus Sementara)*
Semua spesifikasi mekanik combat, musuh, ResonanceState, dan NPC Gemini API dihapus sementara untuk menjamin 100% fokus pada pengujian visual Protagonis. Sistem-sistem ini akan didiskusikan dan dirancang ulang dari awal setelah Tahap 1 selesai.

## BAB IV: STANDAR TEKNIS GODOT & WORKFLOW

- **Arsitektur Direktori**:
  - `res://Scenes/` (Tampilan dan Entitas)
  - `res://Scripts/` (Logika GDScript)
  - `res://Assets/` (Sprites, Audio, Fonts)
- **Komunikasi Sistem**: Seluruh komunikasi lintas sistem (UI, Player, Enemy, Audio) menggunakan **Global Event Bus** via *Autoload* `GameEvents.gd`. Tidak ada *node* yang boleh mengambil referensi langsung ke *node* lain menggunakan `get_node("../Player")`. Semua melalui sinyal di `GameEvents`. Detail implementasi ada di *skill* `godot_rpg_architecture`.
- **Penulisan Kode**: GDScript wajib menggunakan *Static Typing* yang ketat (contoh: `var speed: float = 100.0`).
- **Penamaan Animasi**: Konsisten dengan pola `[aksi]_[arah]` (contoh: `walk_down`). Karena menggunakan Pixellab v3 (8 arah sejati), semua 8 arah termasuk `_left` akan dirender secara spesifik.

## BAB V: RENCANA PENGERJAAN (FOKUS TUNGGAL: ART & ANIMASI PROTAGONIS)

> **Aturan Keras**: Seluruh perencanaan lain (sistem combat, musuh, dunia, narasi) telah DIHAPUS SEMENTARA. Kita mulai dari awal dan hanya berfokus pada visual Protagonis hingga 100% sempurna dan lolos uji coba di Godot. Hal lain akan didiskusikan belakangan.

### TAHAP 1 — Protagonis Art & Animation (Satu-satunya Fokus Saat Ini)
- [ ] **1.1 Art — Prompt-Driven Generation.** Menggunakan Pixellab MCP untuk menghasilkan wujud dasar Protagonis yang mematuhi lore melalui prompt teks.
- [ ] **1.2 Art — Animasi Dasar.** Merender set animasi murni pengujian visual (`idle`, `walk`) di Pixellab. Animasi mekanik (*attack/dodge/hurt*) ditunda.
- [ ] **1.3 Art — Pembersihan & Ekspor.** Pemotongan presisi (*auto-crop/center*) di Aseprite dan ekspor Sprite Sheet ke `res://Assets/Sprites/Characters/Protagonist/`.
- [ ] **1.4 Uji Coba — Godot Integration.** Memasukkan *sprite* ke Godot (`Player.tscn`), menambahkan `PointLight2D` pada syal dan `ShaderMaterial` pada tangan, lalu melakukan pengujian visual di *engine*.

## BAB VI: ALUR KERJA (WORKFLOW) OTOMATIS

Untuk mendapatkan hasil visual yang organik namun tetap mematuhi batasan *lore*, proyek ini menggunakan **Prompt-Driven Workflow** (wajib memanggil *skill* `visual_pipeline_automation` yang berada di direktori `.agents/skills`):

1. **Fase Rendering (Pixellab MCP v3)**: AI mendeskripsikan elemen *lore* (warna rambut, syal kuning, tangan es biru) ke dalam *prompt* bahasa Inggris secara detail. AI memanggil tool Pixellab (`create_character`) dengan parameter wajib: `mode="v3"`, `body="humanoid"`, `size="32x32"`, `view="low top-down"`, `outline="selective outline"`, dan `detail="medium detail"` untuk men-generate karakter 8-arah secara langsung murni dari teks. Gunakan kata kunci `hard edges, no color bleed` pada *prompt* untuk menjaga kualitas *pixel art*.
2. **Fase Pembersihan & Kurasi (Aseprite & Python)**: Unduh *sprite* hasil render. Lakukan *quality control*: jika ada warna elemen penting yang meleset sedikit (misal kuning syal tidak pas `#F4B860`), lakukan pewarnaan ulang menggunakan Aseprite atau Python. Tambahkan *Animation Tags* (`idle`, `walk`).
3. **Fase Implementasi Efek (Godot MCP)**: Detail *lore* diperkuat di dalam *engine* Godot menggunakan:
   - `PointLight2D` (untuk sumber cahaya syal agar menyinari *dungeon*).
   - `ShaderMaterial` (untuk efek animasi berdenyut pada tangan Kutukan Pudar).
4. **Fase Implementasi (Godot MCP via run_gdscript)**: Perangkaian *scene* secara dinamis melalui injeksi GDScript. Sesuai batasan Tahap 1, fase ini **murni** terbatas pada merakit *node* visual (SpriteFrames, Shader, Light). Logika pergerakan, *combat*, dan mekanik dihapus sepenuhnya dari *workflow* saat ini.
5. **Fase Pemantauan (Automated Reporter)**: Untuk mengatasi kebutaan AI, AI akan menyuntikkan skrip pemantau sementara yang mengirimkan log *error* dan *screenshot* otomatis ke terminal AI, memastikan AI selalu mengetahui status *engine* secara *real-time*.

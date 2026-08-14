# QC Patterns Log — Lentera Pudar

Dokumen ini adalah rekam jejak kegagalan kontrol kualitas (*Quality Control failures & rejection patterns*). Setiap kali ada aset, script, atau scene yang ditolak oleh QC Gate, polanya dicatat di sini untuk mencegah kesalahan yang sama terulang dan memperbaiki proses kerja (Quality Assurance).

---

## Format Pencatatan Pola Reject (Pattern Template)

```markdown
### PATTERN-XXX: [Nama Pola Kegagalan]
- **Tanggal**: YYYY-MM-DD
- **Kategori**: [Visual QC / Functional QC / Consistency QC]
- **Komponen Terdampak**: (Nama file/scene/sprite)
- **Gejala / Error**: Deskripsi error atau kecacatan visual yang muncul.
- **Akar Masalah**: Mengapa kesalahan ini bisa terjadi?
- **Tindakan Perbaikan (Fix)**: Solusi teknis yang diterapkan.
- **Langkah Preventif**: Aturan/pemeriksaan baru apa yang ditambahkan ke checklist QC agar tidak terulang?
```

---

## Log Pola yang Pernah Terjadi

### PATTERN-001: Godot 4 .tres Resource Parser Syntax & Tag Cardinal Naming
- **Tanggal**: 2026-08-13
- **Kategori**: Functional QC & Consistency QC
- **Komponen Terdampak**: `protagonist.tres`, `Player.tscn`, `Player.gd`
- **Gejala / Error**:
  1. `Parse Error: Expected ')'` dan `Expected ':'` pada file `.tres` yang di-generate via Python.
  2. `ERROR: Animation 'idle_down' doesn't exist.`
- **Akar Masalah**:
  1. Skrip Python pembangun `.tres` membuat string join dictionary array yang tidak valid sesuai format internal Text Resource Godot 4.
  2. Skrip pergerakan `Player.gd` mencari tag `idle_down` / `idle_up`, sedangkan spritesheet Aseprite menggunakan arah kardinal `idle_south` / `idle_north`.
- **Tindakan Perbaikan (Fix)**:
  1. Menulis `EditorScript` (`generate_frames.gd`) yang memanfaatkan Godot C++ API langsung (`SpriteFrames.new()`, `ResourceSaver.save()`) alih-alih merakit string text resource secara manual.
  2. Menyelaraskan seluruh mapping arah di `Player.gd` ke sistem 8-arah kardinal (`south`, `north`, `east`, `west`, `south-east`, `south-west`, `north-east`, `north-west`).
- **Langkah Preventif**:
  - Dilarang membuat file serialisasi biner/text `.tres` Godot menggunakan manipulasi teks luar jika bisa dijalankan langsung via Godot EditorScript/API.
  - Skrip pengujian otomatis (`TestRunner.gd`) wajib memverifikasi bahwa semua nama animasi di `Player.gd` terdaftar di `AnimatedSprite2D.sprite_frames.get_animation_names()`.

### PATTERN-002: AI Diffusion Mirroring Asymmetry Bias & Color Bleed Glitch
- **Tanggal**: 2026-08-14
- **Kategori**: Visual QC & Consistency QC
- **Komponen Terdampak**: `Assets/Sprites/Characters/Protagonist/`, `protagonist.tres`
- **Gejala / Error**:
  1. Pada sudut `East` / `North-East`, lengan depan Kaelen diberi warna biru es (padahal itu lengan kanan normal).
  2. Pada sudut `West` / `North-West`, lengan depan Kaelen diberi warna putih polos (padahal itu lengan kiri kutukan).
  3. Muncul artefak warna nyasar (*stray magenta pixels* `#D85888`) pada sudut `South-West`.
- **Akar Masalah**: Model AI PixelLab menggunakan asumsi simetri tubuh saat merender rotasi 8-arah (*2D mirroring bias*), sehingga fitur asimetris (lengan kiri kutukan vs lengan kanan normal) tertukar saat menghadap ke arah berlawanan.
- **Tindakan Perbaikan (Fix)**:
  1. Membangun modul `triad_palette_quantizer.py` untuk mengunci seluruh warna ke palet baku *The Triad* dan melenyapkan 100% *color noise*.
  2. Membangun engine `kaelen_pixel_surgeon.py` yang memindai koordinat spasial per frame dan mengoreksi warna lengan kutukan kiri (selalu `#4A6FA5`) dan lengan kanan (selalu normal wraps).
- **Langkah Preventif**:
  - Setiap aset karakter/musuh yang memiliki fitur asimetris wajib melalui pass `triad_palette_quantizer.py` dan bedah piksel arah sebelum digabungkan ke spritesheet Godot.


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

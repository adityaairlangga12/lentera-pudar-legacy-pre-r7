# QC Patterns Log — Lentera Pudar

Dokumen ini adalah rekam jejak kegagalan kontrol kualitas (*Quality Control failures & rejection patterns*). Setiap kali ada aset, script, atau scene yang ditolak oleh QC Gate, polanya dicatat di sini untuk mencegah kesalahan yang sama terulang dan memperbaiki proses kerja (Quality Assurance).

---

## Format Pencatatan Pola Reject (Pattern Template)

```markdown
### PATTERN-XXX: [Nama Pola Kegagalan]
- **Tanggal**: YYYY-MM-DD
- **Kategori**: [Visual QC / Functional QC / Consistency QC]
- **Komponen Terdampak**: (Nama file/scene/sprite/mesh)
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
  - Skrip pengujian otomatis wajib memverifikasi bahwa semua nama animasi di `Player.gd` terdaftar di resource animation.

### PATTERN-002: AI Diffusion Mirroring Asymmetry Bias & Color Bleed Glitch
- **Tanggal**: 2026-08-14
- **Kategori**: Visual QC & Consistency QC
- **Komponen Terdampak**: `Assets/Sprites/Characters/Protagonist/`, `protagonist.tres`
- **Gejala / Error**:
  1. Pada sudut `East` / `North-East`, lengan depan Kaelen diberi warna biru es (padahal itu lengan kanan normal).
  2. Pada sudut `West` / `North-West`, lengan depan Kaelen diberi warna putih polos (padahal itu lengan kiri kutukan).
  3. Muncul artefak warna nyasar (*stray magenta pixels* `#D85888`) pada sudut `South-West`.
- **Akar Masalah**: Model AI 2D menggunakan asumsi simetri tubuh saat merender rotasi 8-arah (*2D mirroring bias*), sehingga fitur asimetris (lengan kiri kutukan vs lengan kanan normal) tertukar saat menghadap ke arah berlawanan.
- **Tindakan Perbaikan (Fix)**: Mengadopsi **Jalur B (3D Low-Poly Armature Rig di Blender 5.2 ➔ Godot SubViewport Pixelation via ADR-008)** yang menjamin 100% konsistensi asimetri geometris di seluruh 8 arah.
- **Langkah Preventif**: Karakter dengan desain asimetris wajib dimodelkan dalam 3D low-poly rig, bukan di-generate via 2D horizontal mirroring.

### PATTERN-003: SubViewport Blurring & Texture Filtering Mismatch di Godot 4.7
- **Tanggal**: 2026-08-15
- **Kategori**: Visual QC
- **Komponen Terdampak**: `SubViewportContainer`, `SubViewport`, `PixelationShader`
- **Gejala / Error**: Render 3D karakter terlihat buram/halus (anti-aliased/bilinear) dan kehilangan ketajaman tepi piksel retro.
- **Akar Masalah**: Setting filter `Nearest` hanya disetel pada level project atau material, tetapi `SubViewportContainer` / `TextureFilter` pada viewport canvas item masih berstatus `Inherit` (Bilinear).
- **Tindakan Perbaikan (Fix)**:
  1. Memastikan `texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST` pada `SubViewportContainer`.
  2. Memastikan `stretch = false` atau integer scaling diatur pada SubViewport.
  3. Menggunakan cel-shader dengan `filter_nearest` pada sampler tekstur.
- **Langkah Preventif**: Checklist Visual QC wajib memeriksa properti filter di 3 titik serentak: Viewport, Container, dan Material.

### PATTERN-004: glTF Bone Roll & Axis Inversion Mismatch antara Blender dan Godot
- **Tanggal**: 2026-08-15
- **Kategori**: Functional QC & Consistency QC
- **Komponen Terdampak**: `Skeleton3D`, glTF Importer Godot 4.7.1
- **Gejala / Error**: Karakter menghadap ke belakang atau bone anggota badan terpuntir 180° saat animasi dijalankan di Godot.
- **Akar Masalah**: glTF 2.0 menggunakan sumbu $+Z$ sebagai forward, sedangkan sistem koordinat 3D Godot menggunakan $-Z$ sebagai forward. Selain itu, *bone roll* di Blender yang belum di-apply menyebabkan rotasi terpuntir saat diekspor.
- **Tindakan Perbaikan (Fix)**:
  1. Menjalankan `apply_all_transforms` dan `validate_bone_roll_consistency` di Blender sebelum ekspor glTF.
  2. Memverifikasi orientasi rest pose pada importer Godot.
- **Langkah Preventif**: Setiap file glTF yang baru diekspor wajib divalidasi via tool `validate_export` sebelum dirakit ke scene Godot.

---
status: ACTIVE
type: REFERENCE
authority_scope: pipeline.patterns
canonical: false
---


# QC Patterns Log — Lentera Pudar: 3D Action RPG Edition

Dokumen ini adalah rekam jejak kegagalan kontrol kualitas (*Quality Control failures & rejection patterns*). Setiap kali ada aset 3D, mesh, armature rig, shader, atau class yang ditolak oleh QC Gate, polanya dicatat di sini untuk mencegah kesalahan yang sama terulang (Quality Assurance).

---

## Format Pencatatan Pola Reject (Pattern Template)

```markdown
### PATTERN-XXX: [Nama Pola Kegagalan]
- **Tanggal**: YYYY-MM-DD
- **Kategori**: [Visual QC / Functional QC / Rigging & Physics QC / Consistency QC]
- **Komponen Terdampak**: (Nama file/mesh/armature/material)
- **Gejala / Error**: Deskripsi error atau kecacatan visual yang muncul.
- **Akar Masalah**: Mengapa kesalahan ini bisa terjadi?
- **Tindakan Perbaikan (Fix)**: Solusi teknis yang diterapkan.
- **Langkah Preventif**: Aturan/pemeriksaan baru apa yang ditambahkan ke checklist QC agar tidak terulang?
```

---

## Log Pola yang Pernah Terjadi

### PATTERN-001: AI Diffusion Mirroring Asymmetry Bias (Pivot ke 3D Native)
- **Tanggal**: 2026-08-14
- **Kategori**: Visual QC & Consistency QC
- **Komponen Terdampak**: Generasi sprite karakter asimetris
- **Gejala / Error**: Lengan kiri kutukan es dan eyepatch mata kanan tertukar saat karakter berputar arah horizontal.
- **Akar Masalah**: Algoritma AI 2D diffusion mengasumsikan simetri tubuh saat merefleksikan gambar.
- **Tindakan Perbaikan (Fix)**: Berpindah total ke **3D High-Detail Armature Rigging di Blender 5.2 LTS**, di mana posisi asimetris terkunci secara geometris pada koordinat 3D lokal $(-X = \text{Left}, +X = \text{Right})$.
- **Langkah Preventif**: Karakter asimetris wajib dimodelkan dalam bentuk 3D mesh murni.

### PATTERN-002: glTF / FBX Transform & Rest Pose Axis Alignment
- **Tanggal**: 2026-08-15
- **Kategori**: Rigging & Export QC
- **Komponen Terdampak**: Armature Hierarchy, glTF Exporter
- **Gejala / Error**: Model menghadap ke belakang atau sumbu tulang terbalik saat diimpor ke game engine.
- **Akar Masalah**: Transformasi (`Location`, `Rotation`, `Scale`) belum di-apply (`Ctrl+A ➔ Apply All Transforms`) dan orientasi sumbu forward tidak distandarisasi.
- **Tindakan Perbaikan (Fix)**: Wajib menjalankan `bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)` dan validasi bone roll sebelum ekspor glTF/FBX.
- **Langkah Preventif**: Tool ekspor 3D wajib menjalankan validasi transform otomatis sebelum menulis file biner ke disk.

### PATTERN-003: Geometric Primitives vs Organic High-Poly Sculpting Gap
- **Tanggal**: 2026-08-16
- **Kategori**: Visual Fidelity QC
- **Komponen Terdampak**: `generate_kaelen_3d_ff7_master.py`
- **Gejala / Error**: Model 3D yang disusun dari susunan silinder, kubus, dan kerucut menghasilkan siluet manekin kaku (ala PS1 1997), belum menjadi model anime organik modern ala *FF7 Remake / Genshin Impact*.
- **Akar Masalah**: Skrip geometris dasar tidak memiliki edge-loop wajah, lipatan kain jubah (*cloth folds*), dan lekukan anatomi otot manusia.
- **Tindakan Perbaikan (Fix)**: Menggunakan alur Image-to-3D AI Mesh Reconstruction atau Base Mesh Sculpting di Blender untuk menghasilkan topologi organik mulus.
- **Langkah Preventif**: Setiap pembuatan model 3D karakter utama harus menggunakan referensi base mesh organik dengan subdivision surface dan cel-shading bertekstur.

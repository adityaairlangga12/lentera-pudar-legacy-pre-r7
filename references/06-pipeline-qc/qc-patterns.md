---
status: ACTIVE
type: REFERENCE
authority_scope: pipeline.patterns
canonical: false
last_reviewed: 2026-08-18
---


# QC Patterns Log — Lentera Pudar: 3D Action RPG Edition

Dokumen ini mencatat pola kegagalan dan tindakan preventif. Sebuah entri hanya boleh diperlakukan sebagai observed project history jika memiliki evidence reference yang dapat diperiksa. Entri legacy tanpa bukti tetap non-authoritative.

---

## Format Pencatatan Pola Reject (Pattern Template)

```markdown
### PATTERN-XXX: [Nama Pola Kegagalan]
- **Tanggal**: YYYY-MM-DD
- **Kategori**: [Visual QC / Functional QC / Rigging & Physics QC / Consistency QC]
- **Komponen Terdampak**: (Nama file/mesh/armature/material)
- **Evidence Reference**: Commit, test/log, artifact, atau laporan inspeksi yang dapat diperiksa.
- **Evidence Status**: `VERIFIED` / `PARTIAL` / `UNVERIFIED_LEGACY_NOTE`.
- **Gejala / Error**: Deskripsi error atau kecacatan visual yang muncul.
- **Akar Masalah**: Mengapa kesalahan ini bisa terjadi?
- **Tindakan Perbaikan (Fix)**: Solusi teknis yang diterapkan.
- **Langkah Preventif**: Aturan/pemeriksaan baru apa yang ditambahkan ke checklist QC agar tidak terulang?
```

---

## Log Pola yang Pernah Terjadi

### PATTERN-001: AI Diffusion Mirroring Asymmetry Bias (Pivot ke 3D Native)
- **Tanggal**: 2026-08-14
- **Evidence Status**: `UNVERIFIED_LEGACY_NOTE`; tidak ada artifact audit yang tersimpan pada repository aktif.
- **Kategori**: Visual QC & Consistency QC
- **Komponen Terdampak**: Generasi sprite karakter asimetris
- **Gejala / Error**: Lengan kiri kutukan es dan eyepatch mata kanan tertukar saat karakter berputar arah horizontal.
- **Akar Masalah**: Algoritma AI 2D diffusion mengasumsikan simetri tubuh saat merefleksikan gambar.
- **Tindakan Perbaikan (Fix)**: Berpindah total ke **3D High-Detail Armature Rigging di Blender 5.2 LTS**, di mana posisi asimetris terkunci secara geometris pada koordinat 3D lokal $(-X = \text{Left}, +X = \text{Right})$.
- **Langkah Preventif**: Karakter asimetris wajib dimodelkan dalam bentuk 3D mesh murni.

### PATTERN-002: glTF / FBX Transform & Rest Pose Axis Alignment
- **Tanggal**: 2026-08-15
- **Evidence Status**: `UNVERIFIED_LEGACY_NOTE`; gunakan sebagai candidate test case, bukan bukti kejadian produksi.
- **Kategori**: Rigging & Export QC
- **Komponen Terdampak**: Armature Hierarchy, glTF Exporter
- **Gejala / Error**: Model menghadap ke belakang atau sumbu tulang terbalik saat diimpor ke game engine.
- **Akar Masalah**: Transformasi (`Location`, `Rotation`, `Scale`) belum di-apply (`Ctrl+A ➔ Apply All Transforms`) dan orientasi sumbu forward tidak distandarisasi.
- **Tindakan Perbaikan (Fix)**: Wajib menjalankan `bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)` dan validasi bone roll sebelum ekspor glTF/FBX.
- **Langkah Preventif**: Tool ekspor 3D wajib menjalankan validasi transform otomatis sebelum menulis file biner ke disk.

### PATTERN-003: Geometric Primitives vs Organic High-Poly Sculpting Gap
- **Tanggal**: 2026-08-16
- **Evidence Status**: `UNVERIFIED_LEGACY_NOTE`; komponen yang disebut tidak ada pada working tree aktif.
- **Kategori**: Visual Fidelity QC
- **Komponen Terdampak**: `generate_kaelen_3d_ff7_master.py`
- **Gejala / Error**: Model 3D yang disusun dari susunan silinder, kubus, dan kerucut menghasilkan siluet manekin kaku (ala PS1 1997), belum menjadi model anime organik modern ala *FF7 Remake / Genshin Impact*.
- **Akar Masalah**: Skrip geometris dasar tidak memiliki edge-loop wajah, lipatan kain jubah (*cloth folds*), dan lekukan anatomi otot manusia.
- **Tindakan Perbaikan (Fix)**: Menggunakan alur Image-to-3D AI Mesh Reconstruction atau Base Mesh Sculpting di Blender untuk menghasilkan topologi organik mulus.
- **Langkah Preventif**: Setiap pembuatan model 3D karakter utama harus menggunakan referensi base mesh organik dengan subdivision surface dan cel-shading bertekstur.

### PATTERN-004: Registry Pass Tidak Menjamin Seluruh Runtime Path Lulus
- **Tanggal**: 2026-08-18
- **Kategori**: Tooling Integration QC
- **Komponen Terdampak**: `lentera-blender-mcp` commit `8d2bdd5`, tool `render_viewport_screenshot`.
- **Evidence Reference**: `node --test tests/contract/*.test.js` menghasilkan 33/33 pass; `node --test tests/integration/*.test.js` menghasilkan 13/14 pass dan screenshot mengembalikan `isError: true`.
- **Evidence Status**: `VERIFIED` untuk hasil eksekusi pada host audit 2026-08-18.
- **Gejala / Error**: Public registry dan handler mapping lulus, tetapi satu execution path integrasi gagal.
- **Akar Masalah**: `UNKNOWN`; R4 tidak mengubah repository MCP terpisah dan tidak mengarang diagnosis.
- **Tindakan Perbaikan**: Turunkan status screenshot menjadi `VERIFICATION_FAILED` pada kontrak toolchain dan hindari menjadikannya bukti wajib.
- **Langkah Preventif**: Selalu jalankan contract tests dan integration tests; jangan menaikkan status behavior hanya dari `tools/list` atau handler registration.

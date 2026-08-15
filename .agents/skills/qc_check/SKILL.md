---
name: qc_check
description: "Standar eksekusi Quality Control (QC Gate) via perintah /qc-check. Menjalankan checklist 3 lapis (Visual, Functional, Consistency) dan pencatatan pola reject ke references/qc-patterns.md."
---

# QC Check Execution Protocol (/qc-check)

Protokol kontrol kualitas mandiri untuk memvalidasi scene, model 3D, shader, dan aset 2D sebelum diserahkan ke pengguna.

---

## 1. Tiga Lapis Checklist Inspeksi (The 3-Tier Gate)

### Lapis 1: Visual QC (Ketajaman & Estetika)
- [ ] **Kepatuhan Palet The Triad**: Warna sesuai kode heksadesimal (`#F4B860`, `#4A6FA5`, `#2A211C`).
- [ ] **Ketajaman Pixelation**: Filter `Nearest` aktif di Viewport, Container, dan Material (tidak ada blur/bilinear).
- [ ] **Asimetri Karakter**: Lengan kiri kutukan es dan eyepatch kanan berada pada posisi anatomis yang benar di seluruh 8 arah.
- [ ] **Hard Edges & Outlines**: Tidak ada color bleed atau piksel liar sisa rendering.

### Lapis 2: Functional QC (Stabilitas & Runtime)
- [ ] **Bebas Error Konsol**: `get_console_output()` dan `get_last_error()` bersih dari warning/error merah.
- [ ] **Animasi & IK**: Looping mulus tanpa *foot sliding*, sendi tidak berputar 360°/terkilir.
- [ ] **Shader Live Reaktif**: Parameter `intensity` pada `CursedHand.gdshader` merespons perubahan *Curse Meter* real-time.
- [ ] **Performa 60 FPS**: Tidak ada spike frame rate atau memory leak.

### Lapis 3: Consistency QC (Struktur & Penamaan)
- [ ] **Penamaan 8-Arah Kardinal**: Sesuai format baku (`idle_south`, `walk_north-west`, `attack_punch_east`).
- [ ] **Orientasi Sumbu glTF**: Karakter menghadap $-Z$ forward di Godot.
- [ ] **UID & Dependensi**: Seluruh resource `.tres` dan scene `.tscn` memiliki dependensi valid tanpa file hilang.

---

## 2. Format Laporan Wajib
Setiap eksekusi `/qc-check` wajib mengeluarkan status:
- `STATUS: PASS` ➔ Seluruh checklist terpenuhi beserta bukti artifact.
- `STATUS: REJECTED` ➔ Rincian kegagalan, dan wajib dicatat ke [references/qc-patterns.md](file:///D:/GodotProjects/Lentera-Pudar/references/qc-patterns.md).

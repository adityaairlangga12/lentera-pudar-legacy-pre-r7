# Teknik Tambahan — Lentera Pudar
### Pelengkap Teori & SOP: Teknik Praktis yang Belum Tercakup

Dokumen ini berisi teknik-teknik konkret (bukan filosofi, bukan tools) yang melengkapi SOP Workflow dan Referensi Teori — beberapa ditemukan langsung dari riset 3D Art Kena, beberapa standar industri umum yang relevan untuk skala proyek kamu.

---

## 1. Trim Sheet & Texture Atlasing

**Apa ini**: Alih-alih membuat tekstur unik untuk tiap prop kecil (puing, ornamen, detail arsitektur), buat satu tekstur besar ("trim sheet") berisi banyak strip material berbeda (batu kasar, logam berkarat, kayu lapuk), lalu UV mapping tiap prop hanya mengambil bagian strip yang relevan dari satu tekstur itu.

**Kenapa penting**: Sangat menghemat memori tekstur dan draw call untuk dungeon besar dengan ratusan prop reruntuhan — daripada 200 tekstur unik 2K, cukup 1-2 trim sheet besar dipakai berulang.

**Terhubung ke**: Style Guide bagian 5 (Poly Budget) dan Teori bagian 17.A (Performance Budgeting) — teknik ini adalah pasangan alami dari budget poligon, karena tekstur yang boros sama mahalnya dengan geometri yang boros.

---

## 2. Vertex Color Masking (Teknik di Balik "Deadzone Regrowth" Kena)

**Apa ini**: Alih-alih membuat 2 material terpisah untuk "area beku" vs "area sudah dihangatkan", satu material dibuat dengan parameter yang dikontrol oleh **vertex color** yang dicat langsung di mesh (atau render target mask sesuai temuan riset Kena) — sehingga transisi bisa terjadi mulus di satu permukaan yang sama tanpa sambungan/seam terlihat.

**Kenapa penting untuk Lentera Pudar**: Ini teknik konkret untuk mekanik pencairan es saat Altar Duka dinyalakan — dinding/lantai bisa transisi dari beku ke hangat secara real-time di satu mesh yang sama, bukan swap mesh/material kasar.

**Cara kerja teknis singkat**: Vertex color channel (R/G/B/A) dipakai sebagai "mask" di material graph — nilai vertex color dikombinasikan dengan parameter waktu/Curse Meter untuk mengontrol blend antara dua set tekstur (beku vs hangat) di area yang sama.

**Terhubung ke**: Riset 3D Art Kena bagian 7 (Deadzone Regrowth System), Style Guide bagian 1.C (desaturasi progresif).

---

## 3. Modular Level Design / Kit-Bashing

**Apa ini**: Alih-alih model setiap bagian lorong dungeon secara unik dari nol, buat set modul dasar (potongan lorong lurus, belokan, persimpangan, pintu, dsb) dengan ukuran grid konsisten (misal kelipatan 300cm), lalu susun modul-modul ini seperti Lego untuk membangun layout besar.

**Kenapa penting**: Jauh lebih cepat untuk grey-box (SOP 5) dan tetap bisa dipakai ulang di detail pass — AI agent bisa "menyusun" level dari kit yang sudah ada alih-alih generate geometri dari nol tiap kali.

**Terhubung ke**: SOP 5 (Membangun Level Baru), Teori bagian 2.A (Teaching Through Geometry).

---

## 4. Normal Map Baking (High-Poly → Low-Poly)

**Apa ini**: Detail permukaan yang di-sculpt di high-poly (ZBrush/Blender Sculpt Mode) "dipindahkan" ke normal map texture, lalu diaplikasikan ke versi low-poly yang dipakai di game — sehingga model in-game terlihat detail tanpa poly count sebenarnya setinggi itu.

**Langkah teknis singkat**:
1. Sculpt detail penuh di high-poly (jutaan poligon, tidak masalah karena tidak dipakai langsung di game).
2. Buat versi retopology low-poly (sesuai budget di Style Guide bagian 5).
3. UV unwrap versi low-poly.
4. Bake normal map dari high-poly ke low-poly (Blender punya built-in baking tool).
5. Assign normal map hasil bake ke material low-poly final.

**Terhubung ke**: SOP 1 (Membuat Prop Baru), Style Guide bagian 5 (Poly Budget), Riset 3D Art Kena bagian 8 (pipeline sculpt Kena).

---

## 5. Texel Density (Konsistensi Resolusi Tekstur)

**Apa ini**: Standar yang memastikan semua aset di game punya kepadatan piksel tekstur yang konsisten relatif terhadap ukuran fisiknya — supaya tidak ada prop yang teksturnya terlihat tajam sementara prop sebelahnya blur, atau sebaliknya boros memori tanpa manfaat visual.

**Rekomendasi baseline untuk Lentera Pudar**: 512 piksel per meter untuk aset hero (Kaelen, boss), 256 piksel per meter untuk prop environment umum — sesuaikan lebih lanjut setelah uji visual di engine.

**Kenapa penting**: Tanpa standar ini, tiap sesi kerja AI agent bisa menghasilkan UV unwrap dengan skala tekstur berbeda-beda tanpa disadari, menyebabkan inkonsistensi visual halus yang sulit dilacak sumbernya belakangan.

**Terhubung ke**: SOP 1 & 2, QA/QC bagian 2.A (DoD Model 3D) — sebaiknya ditambahkan sebagai item checklist baru.

---

## 6. Color Grading & LUT (Look-Up Table)

**Apa ini**: Beda dari lighting scene itu sendiri (yang mengatur sumber cahaya di dunia 3D), color grading adalah lapisan **post-process** di atas seluruh gambar akhir — menyesuaikan kontras, saturasi, dan pergeseran warna global sebelum sampai ke layar pemain. Biasanya diterapkan lewat LUT (Look-Up Table) — semacam "preset filter" yang dipakai konsisten di seluruh game atau berubah per sektor.

**Kenapa penting untuk Lentera Pudar**: Kurva desaturasi progresif per sektor (Style Guide bagian 1.C) sebaiknya diimplementasi lewat LUT per sektor, bukan mengubah warna tiap material satu-satu — jauh lebih konsisten dan mudah di-adjust global.

**Terhubung ke**: Style Guide bagian 1.C, UE5 Post Process Volume (native tool, sudah termasuk dalam Unreal Material Editor di Tools Stack).

---

## 7. Komposisi Environment Art (Rule of Thirds, Leading Lines)

**Apa ini**: Prinsip komposisi dari fotografi/seni lukis yang diterapkan ke penempatan objek dalam level:
- **Rule of Thirds**: elemen visual penting (landmark, altar, musuh boss) ditempatkan di sepertiga frame, bukan selalu di tengah — terasa lebih dinamis secara visual.
- **Leading Lines**: garis alami di environment (jalur reruntuhan, aliran sungai es, deretan pilar) diarahkan untuk "menuntun" mata pemain ke titik fokus (landmark, pintu keluar sektor).

**Kenapa penting**: Ini pelengkap teknis dari Teori bagian 2.C (Sightlines & Landmarking) — sightline menentukan *apa* yang terlihat, komposisi menentukan *bagaimana* itu terlihat menarik secara visual.

**Terhubung ke**: Teori bagian 2.C, SOP 5 (tahap detail level).

---

## 8. Ringkasan Tabel: Teknik → SOP/Dokumen Terkait

| Teknik | SOP Terkait | Dokumen Pendukung |
|---|---|---|
| Trim Sheet/Atlasing | SOP 1, 2 | Style Guide bagian 5 |
| Vertex Color Masking | SOP 2, 5 | Riset Kena bagian 7 |
| Modular Kit-Bashing | SOP 5 | Teori bagian 2.A |
| Normal Map Baking | SOP 1 | Style Guide bagian 5 |
| Texel Density | SOP 1, 2 | QA/QC bagian 2.A (perlu ditambah sebagai item checklist) |
| Color Grading/LUT | — (level-wide, bukan per-aset) | Style Guide bagian 1.C |
| Komposisi Environment | SOP 5 | Teori bagian 2.C |

---

*Dokumen ini melengkapi SOP Workflow dan Referensi Teori sebagai lapisan teknik praktis tambahan dalam paket dokumentasi pra-produksi Lentera Pudar.*

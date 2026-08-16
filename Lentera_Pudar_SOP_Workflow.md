# SOP / Workflow Operasional — Lentera Pudar
### Resep Langkah-per-Langkah untuk Tugas Berulang (Blender + UE5 via MCP)

Dokumen ini berisi urutan kerja **pasti**, bukan filosofi. Untuk tiap tugas berulang, AI agent mengikuti urutan ini persis — bukan menebak urutan sendiri tiap sesi. Kalau ada langkah yang di-skip dengan alasan tertentu, catat alasannya di log sesi kerja (sesuai QA/QC bagian 6.B).

---

## SOP 1: Membuat Prop Baru (dari Nol sampai Masuk UE5)

1. **Cek dulu** apakah prop serupa sudah ada di library aset (hindari duplikasi kerja) — cari di folder `/Props/` sesuai naming convention.
2. **Tentukan kategori poly budget** sesuai Style Guide bagian 5 (prop besar vs prop kecil) sebelum mulai modeling.
3. **Modeling dasar di Blender** — bentuk kasar (block-out) dulu, review siluet dari 4 sudut sebelum lanjut ke detail.
4. **Tambah detail geometri** sesuai budget poly yang sudah ditentukan di langkah 2.
5. **UV Unwrap** — pastikan tidak ada overlap tidak disengaja, seam di posisi tersembunyi/wajar.
6. **Beri nama sesuai konvensi** (`SM_[NamaProp]_[Varian]`) — cek ulang terhadap dokumen naming convention sebelum lanjut.
7. **Buat/assign material** — ikuti SOP 2 di bawah jika material baru diperlukan, atau reuse material existing jika cocok.
8. **Set collision** — custom collision untuk bentuk kompleks, simple collision (box/convex) untuk bentuk sederhana.
9. **Generate LOD** jika masuk kategori aset berulang (lihat Style Guide bagian 5) — minimal LOD1.
10. **Export ke FBX** dengan skala benar (1 unit = 1cm di UE5).
11. **Import ke UE5** lewat MCP command, taruh di folder Content Browser sesuai struktur folder yang disepakati.
12. **Verifikasi visual di UE5** — cek skala benar, tidak terbalik normal, material ter-assign benar.
13. **Jalankan DoD checklist Model 3D** (dokumen QA/QC bagian 2.A) sebelum menandai task selesai.
14. **Commit ke version control** dengan pesan commit jelas (`Add: SM_[NamaProp] - [deskripsi singkat]`).

---

## SOP 2: Setup Material Baru

1. **Tentukan kategori material** dari tabel Style Guide bagian 2 (apakah sudah ada baseline parameter, atau ini kategori benar-benar baru).
2. Jika kategori sudah ada di Style Guide → **langsung pakai range parameter yang tercantum**, jangan menebak angka baru.
3. Jika kategori benar-benar baru (belum ada di Style Guide) → **tandai sebagai gap**, jangan menebak sendiri; ajukan ke manusia untuk keputusan, baru tambahkan ke Style Guide setelah disepakati.
4. **Buat material graph di Substance Designer** (jika prosedural) atau **Substance Painter** (jika hand-paint/detail spesifik) sesuai kebutuhan.
5. **Set parameter dasar PBR** (Base Color, Roughness, Metallic, Normal) sesuai angka dari Style Guide.
6. Jika material butuh **emissive dinamis** (terhubung Curse Meter) → hubungkan ke Material Parameter Collection yang sudah ada, jangan buat parameter collection baru tanpa alasan kuat.
7. Jika material butuh **Subsurface Scattering** (es) → gunakan parameter radius & warna scatter dari Style Guide bagian 2.
8. **Uji visual minimal 2 kondisi pencahayaan berbeda** (terang & gelap) sebelum dianggap final.
9. **Beri nama sesuai konvensi** (`M_[NamaMaterial]` untuk master material, `MI_[NamaMaterial]_[Varian]` untuk instance).
10. **Jalankan DoD checklist Material** (QA/QC bagian 2.B).
11. Commit ke version control.

---

## SOP 3: Rigging Karakter/Musuh Baru

1. **Import base mesh** yang sudah lolos DoD Model 3D ke Blender.
2. **Generate rig dasar** pakai Rigify (untuk humanoid) — sesuaikan proporsi ke mesh.
3. **Skin weight painting** — mulai dari auto-weight, lalu manual cleanup di area masalah umum (ketiak, siku, area sendi kompleks).
4. **Uji deformasi** — gerakkan rig ke pose ekstrem (jongkok penuh, tangan terangkat maksimal) untuk cek area mesh yang rusak/menembus.
5. **Setup spring bone/cloth chain terpisah** jika karakter punya elemen kain/rambut panjang (lihat SOP 4 untuk cloth khusus).
6. **Export ke UE5**, setup ulang di Control Rig untuk kontrol animasi real-time & IK.
7. **Retarget animasi dasar** (locomotion) dari library existing (Mixamo/internal) sebagai starting point, jika ada.
8. **Uji IK kaki** di minimal 2 jenis medan tidak rata.
9. **Jalankan DoD checklist Rigging & Animasi** (QA/QC bagian 2.C).
10. Commit ke version control.

---

## SOP 4: Setup Cloth Simulation Baru (Syal/Jubah/Elemen Kain)

1. **Tentukan elemen ini termasuk kategori mana** di Style Guide bagian 3 (mirip syal Aina = lentur, atau mirip jubah Kaelen = berat) — atau kategori baru yang perlu parameter baru.
2. **Buat pattern kain** di Marvelous Designer jika bentuknya kompleks (bukan sekadar plane), lalu import ke Blender/UE5.
3. **Set pinning point** sesuai posisi anatomis yang masuk akal (leher untuk syal, bahu untuk jubah).
4. **Set parameter stiffness, damping, iteration count** sesuai Style Guide bagian 3 (atau ajukan sebagai gap jika kategori baru).
5. **Uji simulasi di 4 kondisi gerak**: diam, jalan (~150cm/s), lari (~400cm/s), dash — sesuai catatan wajib di Style Guide bagian 3.
6. **Cek clipping** ke tubuh di keempat kondisi — perbaiki collision shape/parameter jika ditemukan masalah.
7. **Jalankan DoD checklist Rigging & Animasi (bagian cloth)** (QA/QC bagian 2.C).
8. Commit ke version control.

---

## SOP 5: Membangun Level/Sektor Baru (dari Grey-Box sampai Detail)

**Tahap Grey-Box (WAJIB sebelum lanjut ke detail):**
1. Bangun layout kasar pakai primitive shape (BSP/simple block) sesuai konsep critical path & optional path (Teori bagian 2.B).
2. Tandai posisi calon landmark utama (Teori bagian 2.C).
3. Tandai posisi breather room di antara area combat (Teori bagian 2.D).
4. **Playtest internal grey-box minimal 3x** (sesuai Gate 2 QA/QC) — catat masalah pacing/navigasi sebelum lanjut.

**Tahap Detail (setelah grey-box lolos playtest):**
5. Ganti primitive shape dengan aset detail sesuai reference image board yang relevan.
6. Setup pencahayaan sesuai parameter Style Guide bagian 4 (Kelvin, intensitas, rasio kontras).
7. Setup World Partition streaming untuk area ini — uji tidak ada pop-in kasar.
8. Tempatkan prop/dekorasi environmental storytelling (Teori bagian 3.A) sesuai lore sektor.
9. Setup audio ambience & trigger musik adaptif untuk area ini.
10. **Jalankan DoD checklist Level/Sektor** (QA/QC bagian 2.E) secara penuh.
11. Commit ke version control.

---

## SOP 6: Menambahkan Kemampuan/Sistem Gameplay Baru (Blueprint/GAS)

1. **Cek apakah sistem serupa sudah ada** di Gameplay Ability System — hindari duplikasi logika.
2. **Tentukan parameter timing** (startup/active/recovery frame) sesuai Style Guide bagian 7, atau ajukan sebagai gap jika kemampuan benar-benar baru.
3. **Implementasi FSM/state transition** di Animation Blueprint atau Behavior Tree (untuk AI).
4. **Uji seluruh transisi state**, termasuk edge case (lihat DoD QA/QC bagian 2.F untuk contoh edge case wajib diuji).
5. **Hubungkan ke Curse Meter** jika relevan, pakai parameter dari Style Guide bagian 9.
6. **Uji tidak ada soft-lock** — coba kombinasi input yang tidak biasa/berurutan cepat.
7. **Jalankan DoD checklist Sistem Gameplay** (QA/QC bagian 2.F).
8. Commit ke version control.

---

## SOP 7: Menambahkan Audio Baru (Musik Layer/Bisikan/SFX)

1. **Rekam/kumpulkan raw audio** di DAW pilihan.
2. **Cleanup noise** di iZotope RX jika perlu (khusus voice/whisper).
3. **Import ke Wwise/MetaSounds**, set loudness sesuai target Style Guide bagian 8 (per kategori: musik/dialog/SFX/ambience).
4. **Setup ducking** jika elemen ini perlu override elemen lain (misal bisikan penting → duck musik).
5. **Setup binaural positioning** jika elemen ini butuh arah spasial (bisikan jiwa beku).
6. **Uji pakai headphone sungguhan**, bukan cuma preview software.
7. **Jalankan DoD checklist Audio** (QA/QC bagian 2.D).
8. Commit ke version control.

---

## Aturan Umum untuk Semua SOP di Atas

- **Jangan lompat tahap** — kalau SOP bilang uji dulu sebelum lanjut (misal grey-box sebelum detail), itu wajib, bukan opsional meski terasa "sudah pasti bagus".
- **Kalau menemukan situasi di luar SOP** (kasus yang tidak tercakup di sini), AI agent **berhenti dan tandai sebagai gap** — jangan improvisasi mengikuti pola tebakan sendiri, laporkan ke manusia dulu.
- Setiap SOP selesai → **selalu ditutup dengan commit ke version control** dengan pesan jelas, tidak ada pekerjaan yang menggantung tanpa tercatat.
- SOP ini adalah **living document** — kalau ditemukan cara yang lebih baik/efisien selama produksi berjalan, revisi SOP ini (dengan catatan tanggal), bukan diam-diam menyimpang tanpa update dokumentasi.

---

*Dokumen ini melengkapi GDD, Moodboard, Teori, Style Guide, dan QA/QC sebagai lapisan operasional dalam paket dokumentasi pra-produksi Lentera Pudar.*

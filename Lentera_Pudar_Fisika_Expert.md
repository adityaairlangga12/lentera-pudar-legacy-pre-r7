# Fisika Tingkat Expert — Lentera Pudar
### Versi Mendalam untuk Simulasi Real-Time (Pelengkap Referensi Teori Bagian 13)

Dokumen ini menggali lebih dalam matematika/mekanika di balik tiap sistem fisika yang dipakai proyek — level detail yang dibutuhkan kalau AI agent harus menyetel parameter solver secara presisi, bukan hanya memakai default engine.

---

## 1. Rigid Body Dynamics — Newton-Euler & Contact Resolution

### A. Persamaan Gerak Dasar
Setiap rigid body (pecahan es, reruntuhan) disimulasikan lewat dua persamaan Newton-Euler terpisah:
- **Linear**: `F = m·a` (gaya = massa × percepatan) — menentukan pergerakan pusat massa.
- **Angular**: `τ = I·α` (torsi = momen inersia × percepatan sudut) — menentukan rotasi objek. Momen inersia `I` bergantung bentuk objek (bola, kotak, silinder punya rumus tensor inersia berbeda), bukan cuma massa total.

### B. Sequential Impulse Solver (Metode Umum di Engine Real-Time)
UE5/Chaos Physics tidak menyelesaikan tabrakan lewat persamaan analitis eksak (terlalu mahal untuk ratusan objek), melainkan **iterative impulse solver**:
1. Deteksi kontak antar objek (collision detection).
2. Hitung impuls (perubahan momentum sesaat) yang diperlukan supaya objek tidak saling menembus.
3. Terapkan impuls, cek ulang apakah masih ada penetrasi.
4. Ulangi beberapa iterasi (biasanya 4-10x per frame) sampai konvergen "cukup baik" — bukan sempurna matematis, tapi cukup stabil secara visual.

**Implikasi praktis**: makin banyak objek rigid body aktif bersamaan (pecahan es besar), makin banyak iterasi solver dibutuhkan untuk stabilitas — trade-off langsung dengan performa (Teori bagian 17.A).

### C. Model Restitusi & Gesekan (Coulomb Friction Cone)
- **Restitusi** (`e`, 0-1): rasio kecepatan setelah vs sebelum tumbukan. `e=1` = pantulan sempurna elastis, `e=0` = tidak memantul sama sekali (energi diserap penuh). Untuk pecahan es (Style Guide: restitusi rendah-menengah), nilai realistis sekitar `e=0.1-0.3` — es pecah lebih "jatuh berat" daripada memantul.
- **Gesekan Coulomb**: gaya gesek maksimum = `μ × N` (koefisien gesek × gaya normal). Solver real-time memakai **friction cone approximation** — menyederhanakan gesekan jadi kerucut di ruang gaya untuk mempercepat komputasi, bukan model gesekan anisotropik penuh.

---

## 2. Soft Body & Cloth — Dari Mass-Spring ke XPBD

### A. Model Mass-Spring Klasik (Fondasi Konseptual)
Kain direpresentasikan sebagai grid partikel (mass point) terhubung oleh spring (pegas) dengan tiga jenis constraint:
- **Structural spring**: menghubungkan partikel bertetangga langsung (horizontal/vertikal) — menjaga jarak dasar kain.
- **Shear spring**: menghubungkan partikel diagonal — mencegah kain "miring" tidak wajar.
- **Bend spring**: menghubungkan partikel dua langkah terpisah — mengontrol kekakuan lipatan (bending stiffness).

Gaya pegas dihitung dari Hukum Hooke: `F = -k·(x - x₀)`, di mana `k` adalah stiffness constant dan `x₀` panjang natural spring.

**Masalah model ini**: mass-spring klasik gampang tidak stabil (jitter/meledak) kalau stiffness diset tinggi dengan timestep besar — inilah kenapa engine modern beralih ke pendekatan berikut.

### B. XPBD (Extended Position-Based Dynamics) — Standar Modern (Chaos Cloth, Blender Cloth)
Alih-alih menghitung gaya lalu mengintegrasikan ke kecepatan/posisi (seperti mass-spring), XPBD langsung memanipulasi **posisi** partikel untuk memenuhi constraint, dengan parameter **compliance** (`α`, kebalikan dari stiffness) yang membuat sistem stabil pada stiffness berapa pun tanpa meledak.

Alur per-frame:
1. Prediksi posisi baru tiap partikel dari kecepatan+gaya eksternal (gravitasi, angin) — disebut posisi "tentative".
2. Selesaikan semua constraint (jarak antar partikel, self-collision, collision dengan tubuh karakter) secara iteratif — geser posisi partikel supaya constraint terpenuhi.
3. Update kecepatan dari selisih posisi lama vs baru dibagi timestep.

**Parameter `iteration count`** di Style Guide bagian 3 secara teknis adalah jumlah pengulangan langkah 2 di atas per frame — makin tinggi, makin akurat constraint terpenuhi (kain terasa lebih "presisi"), tapi makin mahal komputasi linear.

### C. Bending Stiffness vs Stretching Stiffness (Kenapa Dipisah)
Kain nyata jauh lebih mudah ditekuk (bending) daripada diregangkan (stretching) — rasio kekakuan bisa 100-1000x berbeda. Ini kenapa parameter Style Guide membedakan implisit antara "stiffness" umum untuk syal Aina vs jubah — di implementasi nyata, sebaiknya kedua parameter ini (`stretch_stiffness` dan `bend_stiffness`) diatur terpisah, bukan satu angka tunggal, untuk hasil paling realistis.

### D. Self-Collision (Kain Menabrak Dirinya Sendiri)
Untuk jubah Kaelen yang bisa terlipat kompleks, self-collision checking (partikel kain vs partikel kain lain di objek yang sama) diperlukan supaya kain tidak saling menembus saat terlipat — ini operasi paling mahal secara komputasi di seluruh sistem cloth (kompleksitas mendekati O(n²) tanpa optimasi spatial partitioning seperti BVH/grid hashing).

---

## 3. Fracture Mechanics — Voronoi & Stress Concentration

### A. Konsep Stress Concentration
Material rapuh (es) tidak pecah merata — ia pecah di titik dengan **konsentrasi tegangan tertinggi**, biasanya di sekitar cacat mikro/sudut tajam/titik impact. Secara matematis, tegangan di sekitar cacat berbentuk elips mengikuti faktor konsentrasi tegangan `Kt`, yang bisa jauh lebih tinggi dari tegangan rata-rata material.

### B. Algoritma Voronoi Fracture
Teknik paling umum di game real-time untuk mensimulasikan pecahan meyakinkan tanpa menghitung fisika retak sungguhan:
1. Sebar titik-titik acak (seed points) di dalam volume objek — kepadatan titik menentukan ukuran rata-rata pecahan.
2. Hitung **Voronoi diagram** dari titik-titik ini — setiap titik "menguasai" region ruang terdekat dengannya (batas antar region jadi bidang potong pecahan).
3. Potong mesh asli berdasarkan batas-batas Voronoi ini menjadi pre-fractured chunks.
4. Saat runtime, chunk-chunk ini "disatukan" secara visual (invisible sampai dipicu), lalu dipisah jadi rigid body individual saat objek pecah.

**Kenapa dipilih dibanding physics-based fracture sungguhan**: fracture berbasis fisika penuh (menghitung propagasi retak real-time) sangat mahal komputasi dan tidak deterministik — Voronoi pre-fractured memberi kontrol artistik penuh (bisa di-preview, di-adjust) dengan biaya runtime jauh lebih murah (chunk sudah "siap pecah" sejak awal, tinggal spawn sebagai rigid body).

### C. Bias Distribusi Seed Point untuk Kesan Kristal
Untuk kristal es (bukan pecahan batu acak), seed point Voronoi sebaiknya tidak didistribusikan uniform random — gunakan distribusi yang mengikuti pola kisi kristal (lattice-biased) supaya bentuk pecahan terlihat seperti struktur kristal alami, bukan pecahan batu.

---

## 4. Fluid Dynamics Disederhanakan — Dari Navier-Stokes ke Pendekatan Real-Time

### A. Kenapa Navier-Stokes Penuh Tidak Dipakai
Persamaan Navier-Stokes (fondasi fisika fluida sungguhan) melibatkan sistem persamaan diferensial parsial non-linear yang sangat mahal diselesaikan secara numerik real-time untuk skala game — bahkan simulasi fluida offline VFX film butuh waktu render berjam-jam per frame.

### B. Pendekatan Praktis untuk Efek Leleh/Uap
- **Grid-based Eulerian (disederhanakan)**: untuk efek uap/asap, ruang dibagi grid sel, tiap sel menyimpan nilai densitas/kecepatan, diupdate tiap frame dengan advection sederhana (memindahkan nilai searah kecepatan) — jauh lebih murah dari Navier-Stokes penuh tapi masih "terasa" seperti fluida.
- **Particle-based (SPH disederhanakan)**: Niagara di UE5 punya modul fluid-like yang mengaproksimasi Smoothed Particle Hydrodynamics dengan jumlah partikel jauh lebih sedikit dan interaksi disederhanakan, cukup untuk kesan visual tanpa akurasi fisik penuh.
- **Flipbook texture (paling murah)**: untuk efek yang bentuknya bisa diprediksi (uap dingin dari es mencair), sering paling efisien memakai animasi tekstur pre-rendered (dibuat offline dengan simulasi fluida penuh sekali, lalu dimainkan sebagai sprite sheet) — nol biaya komputasi fisika real-time.

### C. Shallow Water Equation (Kalau Ada Genangan Air Es Mencair)
Kalau ada kebutuhan genangan air dari es mencair yang perlu riak realistis, Shallow Water Equations (SWE) adalah aproksimasi Navier-Stokes yang jauh lebih murah — mengasumsikan kedalaman air jauh lebih kecil dari lebar permukaan, cukup akurat untuk genangan/kolam kecil, tidak untuk lautan atau air dalam.

---

## 5. Light Transport — Rendering Equation & Lumen

### A. Rendering Equation (Fondasi Konseptual Semua Rendering Realistis)
Persamaan dasar yang menjelaskan bagaimana cahaya sampai ke mata/kamera dari suatu titik permukaan:

`L_o(x,ω_o) = L_e(x,ω_o) + ∫ f_r(x,ω_i,ω_o)·L_i(x,ω_i)·(ω_i·n) dω_i`

Secara konsep (tanpa perlu menghitung manual): cahaya yang keluar dari suatu titik (`L_o`) = cahaya yang dipancarkan sendiri (`L_e`, relevan untuk material emissive syal Aina) + integral dari semua cahaya masuk dari segala arah, dikalikan seberapa besar permukaan memantulkannya (BRDF, `f_r`).

### B. BRDF — Bidirectional Reflectance Distribution Function
Fungsi yang mendeskripsikan bagaimana permukaan memantulkan cahaya, dipecah jadi:
- **Diffuse term**: pantulan merata ke segala arah (permukaan kasar/matte) — dikontrol oleh Base Color di material PBR.
- **Specular term**: pantulan terkonsentrasi ke arah pantulan cermin — dikontrol oleh Roughness/Metallic. Model umum yang dipakai UE5: **Cook-Torrance BRDF** dengan **GGX/Trowbridge-Reitz distribution** untuk menentukan sebaran highlight specular berdasarkan roughness.

**Implikasi untuk material es (Style Guide bagian 2)**: roughness rendah (0.15-0.30) menghasilkan distribusi GGX yang sempit dan tajam — highlight specular kecil dan terang, konsisten dengan kesan permukaan es yang "keras tapi berkilau", beda dari roughness tinggi batu (0.70-0.85) yang menyebarkan highlight jadi sangat lebar/redup.

### C. Bagaimana Lumen Mengaproksimasi Rendering Equation Secara Real-Time
Lumen tidak menyelesaikan integral rendering equation secara eksak (itu ranah offline path tracing yang butuh ribuan sample per pixel) — melainkan kombinasi teknik aproksimasi:
- **Signed Distance Field (SDF) Tracing** untuk indirect lighting jarak jauh — representasi geometri sebagai medan jarak memungkinkan "ray marching" murah tanpa perlu raytracing polygon sungguhan.
- **Screen-Space methods** untuk detail jarak dekat yang butuh presisi lebih tinggi.
- **Surface Cache** — menyimpan hasil pencahayaan permukaan di tekstur cache yang diupdate bertahap (bukan dihitung ulang penuh tiap frame), mengurangi beban komputasi drastis.

Hasilnya adalah aproksimasi "cukup meyakinkan" dari global illumination sungguhan, dengan biaya komputasi yang bisa dijalankan real-time — trade-off akurasi vs performa yang sama filosofinya dengan pendekatan fluid dynamics di bagian 4.

---

## 6. Inverse Kinematics — Solver Matematis

### A. IK sebagai Constraint Satisfaction Problem
Diberikan posisi target (misal telapak kaki harus menyentuh titik tertentu di lantai miring), IK mencari sudut-sudut sendi (`θ₁, θ₂, ...θₙ`) sepanjang rantai tulang yang memenuhi posisi target, dalam batasan rotasi anatomis (Dokumen Anatomi bagian 8).

### B. Metode CCD (Cyclic Coordinate Descent) — Umum di Game Engine
Algoritma iteratif yang relatif murah komputasi:
1. Mulai dari sendi paling ujung rantai (dekat target), sesuaikan rotasinya supaya end-effector (ujung rantai, misal telapak kaki) semakin dekat ke target.
2. Pindah ke sendi berikutnya (lebih ke pangkal rantai), ulangi penyesuaian.
3. Lanjut sampai pangkal rantai, lalu ulangi seluruh siklus beberapa kali sampai konvergen cukup dekat ke target.

**Kelemahan CCD**: kadang menghasilkan pose "tidak natural" karena tidak mempertimbangkan preferensi pose manusia — sering dikombinasikan dengan **pose priority/preferred angle** tambahan supaya hasil tetap terlihat anatomis wajar.

### C. Metode FABRIK (Forward And Backward Reaching IK) — Alternatif Lebih Stabil
Metode lebih modern, bekerja di ruang posisi (bukan sudut rotasi) — melakukan dua pass:
1. **Backward pass**: mulai dari target, "tarik" tiap sendi mundur sepanjang rantai menuju target, menjaga panjang tulang tetap.
2. **Forward pass**: mulai dari pangkal rantai (posisi tetap, misal pinggul), "dorong" kembali tiap sendi maju, menjaga panjang tulang tetap.

FABRIK umumnya konvergen lebih cepat dan lebih stabil secara visual dibanding CCD, terutama untuk rantai IK panjang (kaki penuh dari pinggul ke telapak kaki) — direkomendasikan untuk foot IK Kaelen di medan tidak rata.

### D. Jacobian-Based IK (Metode Lebih Akademis, Jarang Dipakai Real-Time Murni)
Menggunakan matriks Jacobian untuk menghubungkan perubahan kecil sudut sendi dengan perubahan posisi end-effector, diselesaikan lewat pseudo-inverse matriks. Secara matematis lebih elegan tapi komputasi lebih mahal dibanding CCD/FABRIK — biasanya hanya dipakai untuk animasi offline presisi tinggi, bukan real-time per-frame di game.

---

## 7. Ringkasan Trade-off Akurasi vs Performa (Prinsip Pemandu Semua Sistem di Atas)

Pola yang berulang di seluruh dokumen ini: **setiap sistem fisika real-time adalah aproksimasi yang sengaja mengorbankan akurasi fisik penuh demi kecepatan komputasi** — bukan karena engine "kurang canggih", tapi karena ini keputusan desain sadar standar industri:

| Sistem | Model "Benar" Secara Fisika | Aproksimasi Real-Time yang Dipakai |
|---|---|---|
| Rigid Body | Persamaan kontak eksak (LCP solver penuh) | Sequential impulse iteratif |
| Cloth | Continuum mechanics penuh | XPBD dengan iterasi terbatas |
| Fracture | Propagasi retak fisik (fracture mechanics penuh) | Pre-fractured Voronoi |
| Fluida | Navier-Stokes | Grid Eulerian sederhana / particle SPH sederhana / flipbook |
| Cahaya | Path tracing (integral rendering equation eksak) | SDF tracing + surface cache (Lumen) |
| IK | Jacobian-based solver presisi tinggi | CCD/FABRIK iteratif |

**Instruksi untuk AI agent**: kalau menemukan hasil simulasi "kurang akurat" dibanding ekspektasi teoretis murni, ini **wajar dan diharapkan** — jangan mencoba memaksakan akurasi 100% dengan menaikkan parameter iterasi/kompleksitas tanpa batas, karena akan menabrak Performance Budget (Teori bagian 17.A). Target selalu "cukup meyakinkan secara visual", bukan akurasi fisika sempurna.

---

*Dokumen ini adalah versi mendalam dari Referensi Teori bagian 13 (Fisika Tingkat Lanjut), sebagai bagian dari paket dokumentasi pra-produksi Lentera Pudar.*

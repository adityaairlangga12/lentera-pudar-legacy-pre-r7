# 3D Expert — Teori Fondasi — Lentera Pudar
### Prinsip Inti di Balik Modeling, UV, Shading, Rigging, dan Optimasi (Pelengkap Riset 3D Art Kena, Teknik Tambahan, dan API Cheat Sheet)

Dokumen-dokumen 3D yang sudah ada (Riset 3D Art Kena, Teknik Tambahan, Daftar Tools/MCP Stack, API Cheat Sheet) berisi riset spesifik dan teknik praktis. Dokumen ini mengisi lapisan yang belum eksplisit: **teori fondasi** di balik kenapa teknik-teknik itu bekerja — supaya AI agent bisa membuat keputusan 3D yang tepat di situasi baru yang belum pernah eksplisit dicontohkan, bukan cuma mengikuti resep yang sudah ditulis.

---

## 1. Topology Theory

### A. Kenapa Topology (Bukan Cuma Bentuk) yang Menentukan Kualitas
Dua mesh bisa punya siluet identik tapi kualitas sangat berbeda tergantung bagaimana polygon-nya disusun. Topology yang baik memastikan mesh **deform dengan benar saat animasi**, bukan cuma terlihat benar saat statis.

### B. Prinsip Edge Flow
Edge loop harus mengikuti arah otot dan garis deformasi alami tubuh (lihat cross-reference dokumen Anatomi & Kinesiologi) — terutama di area sendi (siku, lutut, bahu) dan wajah (sekitar mata, mulut untuk ekspresi). Edge flow yang salah arah menyebabkan mesh "pecah" atau berkerut aneh saat animasi, meregardless seberapa bagus bind pose-nya.

### C. Quad vs Triangle vs N-gon
| Jenis Face | Kapan Dipakai | Risiko |
|---|---|---|
| Quad (4 sisi) | Standar untuk area yang akan di-subdivide atau dianimasikan | — |
| Triangle | Area statis yang tidak akan deform (hard surface non-organic) | Subdivision surface tidak halus |
| N-gon (5+ sisi) | Dihindari kecuali di area flat yang tidak terlihat/tidak deform | Shading artifact, masalah subdivision |

### D. Pole (Vertex dengan Jumlah Edge ≠ 4) dan Penempatannya
Pole tidak bisa dihindari sepenuhnya di mesh organik kompleks, tapi harus ditempatkan strategis — di area yang **tidak** akan banyak deform atau tidak terlihat jelas (contoh: pole 5-edge boleh di bagian belakang kepala, tapi bermasalah kalau ada tepat di lipatan siku).

**Instruksi untuk AI agent**: sebelum menganggap topology "selesai", cek dua hal — apakah edge loop mengikuti arah deformasi di area sendi/wajah, dan apakah pole ditempatkan jauh dari area yang akan banyak bergerak. Topology yang terlihat rapi secara statis tapi salah edge flow akan gagal saat rigging, dan masalah itu baru kelihatan di tahap jauh lebih mahal untuk diperbaiki.

---

## 2. UV Unwrapping & Seam Theory

### A. Prinsip Dasar UV Unwrapping
UV unwrapping adalah proses "membuka" mesh 3D jadi bidang 2D supaya tekstur bisa dipetakan tanpa distorsi berlebih. Distorsi tidak bisa dihilangkan total (proyeksi 3D ke 2D selalu ada trade-off, sama seperti masalah peta dunia), tapi bisa diminimalkan dan disembunyikan strategis.

### B. Penempatan Seam yang Baik
Seam (garis potong UV) idealnya ditempatkan di:
- Area yang tersembunyi dari sudut pandang umum (bagian dalam lengan, bawah kaki).
- Perbatasan material alami (sambungan baju-kulit, sambungan armor plate).
- Area dengan perubahan kurvatur tajam (lebih gampang unwrap tanpa distorsi di sana).

Seam yang buruk menyebabkan tekstur "terputus" terlihat di area yang mudah terlihat, atau menyebabkan distorsi tekstur (stretching) di area yang seharusnya detail tajam (wajah, tangan).

### C. UV Islands dan Efisiensi Ruang
Tiap island (pulau UV hasil unwrap) harus diatur (packing) untuk memaksimalkan penggunaan ruang tekstur — island yang terlalu kecil relatif terhadap ukuran fisik di dunia game membuang resolusi tekstur, island yang terlalu besar boros memori untuk detail yang tidak akan terlihat jelas (lihat texel density di dokumen Teknik Tambahan).

**Instruksi untuk AI agent**: setelah unwrap, cek dua hal sebelum lanjut ke texturing — apakah ada stretching berlebih di area wajah/tangan (area detail tinggi), dan apakah seam tersembunyi di sudut pandang standar. Kalau texel density sudah diatur di dokumen lain, unwrap harus konsisten dengan target itu, bukan asal cukup.

---

## 3. PBR Shading Theory

### A. Prinsip Physically Based Rendering
PBR mensimulasikan bagaimana cahaya berinteraksi dengan permukaan berdasarkan properti fisik material (bukan trik visual manual seperti shading model lama). Dua channel paling fundamental:
- **Albedo/Base Color**: warna dasar permukaan tanpa informasi pencahayaan (harus "flat", tidak ada bayangan/highlight yang dilukis manual ke dalam tekstur).
- **Roughness**: seberapa kasar permukaan secara mikroskopis, menentukan seberapa "tajam" atau "menyebar" refleksi cahaya.
- **Metallic**: apakah material berperilaku seperti logam (refleksi berwarna sesuai albedo, minim diffuse) atau non-logam (refleksi netral/putih, diffuse dominan).

### B. Kesalahan Umum yang Harus Dihindari Agent
- Melukis bayangan/highlight langsung ke tekstur albedo — ini akan bentrok dengan pencahayaan real-time (Lumen) dan terlihat salah dari sudut cahaya berbeda.
- Nilai metallic di antara 0 dan 1 (bukan murni logam atau non-logam) — dalam PBR yang benar, hampir semua material di dunia nyata seharusnya metallic 0 atau 1 murni, kecuali kasus edge-case tertentu (permukaan kotor/campuran).
- Roughness map yang flat/seragam — permukaan nyata (termasuk es dan kristal di project ini) punya variasi roughness mikro yang membuatnya terasa believable, bukan plastik.

### C. Material Layering untuk Efek Kompleks
Efek seperti es yang mencair atau kristal retak (Deadzone Regrowth) biasanya butuh **material layering/blending** — bukan satu material statis, melainkan blend antara dua/lebih set parameter PBR berdasarkan mask (vertex color atau texture mask, lihat dokumen Teknik Tambahan bagian vertex color masking).

**Instruksi untuk AI agent**: saat membuat/evaluasi material baru, cek apakah albedo benar-benar bebas dari informasi pencahayaan yang dilukis manual, dan apakah nilai metallic sudah sesuai kategori material (bukan nilai tengah tanpa alasan fisik yang jelas).

---

## 4. Rigging & Deformation Theory

### A. Skeletal Hierarchy dan Forward Kinematics
Rig tersusun sebagai hierarki tulang (bone) berbentuk pohon — tiap tulang anak mewarisi transformasi tulang induknya (forward kinematics). Ini alasan kenapa urutan hierarki (misal shoulder → upper arm → forearm → hand) harus mengikuti struktur anatomis nyata, bukan sekadar urutan yang "terlihat masuk akal" secara visual.

### B. Skinning Weight — Kenapa Ini Bukan Sekadar "Cat Warna"
Skinning weight menentukan seberapa besar pengaruh tiap bone terhadap tiap vertex mesh. Prinsip kunci:
- **Total bobot per vertex harus berjumlah 1** (100%) — kalau tidak, deformasi tidak stabil.
- Area transisi antar bone (siku, lutut) butuh **blending gradual** antar dua bone, bukan batas tegas — batas tegas menyebabkan "lipatan patah" di sendi.
- Terlalu banyak bone berpengaruh ke satu vertex (lebih dari 4, batas umum real-time engine) menyebabkan deformasi kabur/tidak presisi.

### C. Corrective Shape Keys sebagai Solusi Deformasi Ekstrem
Skinning weight murni tidak bisa menangani semua kasus deformasi realistis (contoh: otot bisep menggelembung saat siku ditekuk penuh, atau volume loss di sendi — sudah dibahas di dokumen Anatomi & Kinesiologi bagian 5). Corrective shape key adalah bentuk mesh tambahan yang aktif otomatis pada sudut rotasi tertentu untuk mengoreksi kekurangan skinning weight murni.

**Instruksi untuk AI agent**: kalau deformasi terlihat "aneh" di sudut ekstrem (siku/lutut tertekuk penuh), jangan langsung coba perbaiki lewat weight painting lebih rumit — evaluasi dulu apakah ini kasus yang memang butuh corrective shape key, karena skinning weight murni punya batas fisik apa yang bisa dicapai.

### D. IK vs FK — Kapan Pakai yang Mana
Forward Kinematics (FK) mengontrol rotasi tiap sendi secara berurutan dari pangkal — cocok untuk gerakan bebas di udara (ayunan lengan saat serangan). Inverse Kinematics (IK) menentukan posisi target akhir (misal telapak kaki di lantai) dan menghitung mundur sudut sendi yang dibutuhkan — cocok untuk kontak dengan lingkungan (kaki di lantai tidak rata, lihat dokumen Fisika Expert bagian tentang IK sebagai constraint solving).

**Instruksi untuk AI agent**: pilih IK untuk anggota tubuh yang kontak langsung dengan lingkungan/objek eksternal, FK untuk gerakan bebas — banyak rig modern pakai keduanya sekaligus (IK-FK switch) tergantung konteks aksi.

---

## 5. LOD & Optimization Theory

### A. Kenapa LOD Bukan Sekadar "Versi Kasar"
Level of Detail (LOD) yang baik mempertahankan siluet dan fitur penting (lihat dokumen Kreativitas & Seni bagian 3 soal silhouette/readability) sambil mengurangi kompleksitas di area yang tidak akan terlihat jelas dari jarak tertentu. LOD yang asal-asalan (auto-decimate tanpa kontrol) sering merusak fitur penting justru di area yang paling sering dilihat dekat.

### B. Trade-off Poly Budget vs Visual Fidelity
Setiap platform target punya batas realistis poly count per frame (sudah ada baseline di Style Guide Numerik). Keputusan LOD harus mempertimbangkan **jarak kamera tipikal** terhadap objek — prop yang sering dilihat dekat (senjata Kaelen) butuh LOD transition lebih halus dibanding prop latar (reruntuhan jauh) yang bisa drop detail lebih agresif.

### C. Texture Streaming dan Mip Mapping
Selain poly count, tekstur resolusi tinggi yang tidak di-mipmap dengan benar menyebabkan aliasing (kedipan/noise) saat objek jauh dari kamera — mip mapping otomatis menyediakan versi resolusi lebih rendah untuk jarak jauh, tapi texel density yang tidak konsisten (dokumen Teknik Tambahan) membuat transisi mip terlihat tidak rata antar aset.

**Instruksi untuk AI agent**: saat membuat LOD, prioritaskan mempertahankan siluet dan fitur functional (bagian yang dipakai untuk gameplay readability) di atas mempertahankan detail dekoratif. Kalau ragu bagian mana yang boleh disederhanakan, cek dulu apakah bagian itu berkontribusi ke silhouette/readability combat sebelum memutuskan.

---

## 6. Baking Pipeline Theory

### A. Kenapa Baking Diperlukan (High-Poly ke Low-Poly)
Baking mentransfer detail dari mesh resolusi tinggi (hasil sculpting ZBrush/Blender) ke mesh resolusi rendah (untuk real-time) lewat texture map (normal map, ambient occlusion, curvature) — sehingga mesh low-poly *terlihat* detail tanpa biaya komputasi mesh high-poly sesungguhnya.

### B. Normal Map — Tangent Space vs Object Space
- **Tangent space normal map** (lebih umum): bergantung pada orientasi UV lokal tiap face — bisa dipakai ulang di mesh berbeda dan bekerja dengan deformasi/animasi.
- **Object space normal map**: terikat pada orientasi mesh spesifik, tidak cocok untuk mesh yang dianimasikan, tapi kadang dipakai untuk objek statis dengan hasil bake lebih bersih.

**Instruksi untuk AI agent**: untuk semua aset yang dianimasikan (karakter, prop yang bergerak), selalu pakai tangent space normal map — object space akan menghasilkan deformasi shading yang salah begitu mesh dianimasikan.

### C. Cage Mesh untuk Baking Presisi
Baking langsung dari high-poly ke low-poly tanpa cage (mesh pembatas tambahan yang mengontrol jarak ray-casting saat bake) sering menghasilkan artefak di area dengan perbedaan bentuk signifikan antara versi high dan low-poly (contoh: lipatan kain tajam). Cage mesh memberi kontrol eksplisit ke area mana ray bake harus mencari detail.

### D. Ambient Occlusion Bake — Kapan Dipakai vs Real-Time GI
Dengan Lumen (real-time GI, dokumen Fisika Expert bagian 5) aktif, AO yang di-bake ke tekstur bisa jadi redundan atau malah bentrok (double darkening di celah/lipatan). AO bake tetap berguna untuk **detail mikro** yang terlalu halus untuk ditangkap real-time GI (pori-pori kain, celah kecil ukiran), tapi bukan untuk oklusi skala besar yang sudah ditangani Lumen.

**Instruksi untuk AI agent**: saat bake AO, batasi kontribusinya ke detail mikro saja (intensitas rendah, radius kecil) — jangan bake AO skala besar yang akan konflik dengan indirect lighting real-time yang sudah dihitung Lumen.

---

## 7. Ringkasan Peta Teori 3D ke Tahap Produksi

| Tahap Produksi | Teori yang Relevan | Risiko kalau Diabaikan |
|---|---|---|
| Modeling/Sculpting | Topology Theory | Mesh pecah/berkerut saat animasi |
| Texturing prep | UV & Seam Theory | Tekstur terdistorsi atau seam terlihat |
| Material Setup | PBR Shading Theory | Material terlihat plastik atau salah di pencahayaan berbeda |
| Rigging | Deformation Theory (skinning, corrective shape key, IK/FK) | Deformasi aneh di sendi, gerakan tidak natural |
| Optimasi | LOD & Texture Streaming Theory | Performa buruk atau fitur penting hilang di LOD jauh |
| Detail Transfer | Baking Pipeline Theory | Artefak normal map, AO bentrok dengan Lumen |

**Instruksi umum untuk AI agent**: dokumen ini melengkapi (bukan menggantikan) Riset 3D Art Kena, Teknik Tambahan, dan API Cheat Sheet yang sudah ada. Dokumen-dokumen itu memberi tahu *apa* yang harus dilakukan dan *kode* konkretnya; dokumen ini memberi tahu *kenapa* — supaya AI agent bisa mengambil keputusan yang benar di situasi baru yang belum eksplisit dicontohkan di dokumen teknik/API, bukan cuma mengikuti pola yang sudah ada persis.

---

*Dokumen ini adalah pelengkap paket dokumentasi pra-produksi Lentera Pudar, melengkapi Riset 3D Art Kena, Teknik Tambahan, API Cheat Sheet, dan Anatomi & Kinesiologi.*

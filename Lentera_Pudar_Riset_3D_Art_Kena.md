# Riset Mendalam: 3D Art Kena: Bridge of Spirits
### Referensi Lengkap dengan Sumber, untuk AI Agent Lentera Pudar

Dokumen ini merangkum semua temuan riset soal pendekatan 3D art Kena: Bridge of Spirits (Ember Lab), dari sumber wawancara resmi developer, artikel teknis, dan portofolio artis yang terlibat langsung di proyeknya. Semua paraphrase dari sumber asli — link disertakan di tiap bagian untuk verifikasi/pendalaman lebih lanjut oleh kamu atau AI agent.

---

## 1. Kategori Gaya Besar

Kena diposisikan sebagai perpaduan antara realisme dan stilasi tinggi, tapi condong lebih dekat ke sisi stilasi — bukan cel-shading, bukan juga photoreal. Materialnya (kain, lumpur) dibuat dengan shader yang sangat detail, dan teksturnya tajam meski gaya visualnya stylized.

**Sumber**: [MMORPG.com — Kena: Bridge of Spirits PC Review](https://www.mmorpg.com/reviews/kena-bridge-of-spirits-pc-review-2000123183)

Ciri lainnya: karakter/objek tidak punya outline hitam sama sekali (beda dari gaya komik/cel-shading khas Borderlands), fokus utamanya ada di proporsi karakter, detail tekstur yang disederhanakan, dan palet warna ringan — dijuluki "interactive animated Pixar movie".

**Sumber**: [The Gameslinger — Kena Review](https://thegameslinger.com/2022/09/18/kena-bridge-of-spirits-review-pc/)

---

## 2. Inspirasi & Filosofi Desain (Langsung dari COO Ember Lab)

Josh Grier (Chief Operating Officer Ember Lab) menjelaskan bahwa studio ini awalnya adalah studio animasi murni, sehingga gaya visual dan kualitas sinematik selalu jadi fokus sejak awal — latar belakang animasi dan storytelling itulah yang mengarahkan seluruh pipeline produksi, bukan sebaliknya.

Sumber inspirasi visual yang disebutkan eksplisit: dunia-dunia misterius dan indah dalam film animasi Hayao Miyazaki, kualitas nostalgia dari game Zelda klasik, dan pengalaman pribadi kedua bersaudara pendiri studio saat menghabiskan banyak waktu di Jepang — style Kena berkembang dari usaha merekonstruksi perasaan dari pengalaman masa kecil mereka sendiri.

**Sumber**: [80.lv — Visual Identity & Development of Kena: Bridge of Spirits](https://80.lv/articles/visual-identity-development-of-kena-bridge-of-spirits)

---

## 3. Pipeline Produksi Aset (Concept → Final In-Engine)

Alur kerja resmi yang dijelaskan Josh Grier:
1. Tim concept artist merancang gaya, personality, dan detail visual karakter/environment.
2. Artwork diserahkan ke tim modeling 3D, bekerja berdampingan dengan concept artist untuk menyelaraskan model dengan konsep.
3. Texturing menambahkan detail akhir.
4. Setelah model di-rigging dan diimplementasi, aset siap masuk ke level art dan/atau animasi.

Rigging jadi elemen yang sangat diprioritaskan karena seluruh animasi mereka berbasis **key-frame hand-crafted**, bukan mocap — ini penting untuk mempertahankan animasi buatan tangan yang menghidupkan karakter.

**Sumber**: [80.lv — Visual Identity & Development of Kena: Bridge of Spirits](https://80.lv/articles/visual-identity-development-of-kena-bridge-of-spirits)

---

## 4. Tools Konkret yang Dipakai

| Tools | Fungsi di Pipeline Kena |
|---|---|
| **Maya** | Software utama untuk animasi seluruh karakter dan makhluk |
| **ZBrush** | Dipakai intensif untuk sculpting model 3D detail tinggi (high-poly) |
| **Substance 3D Painter** | Texturing detail akhir |
| **Unity** (awal prototyping) | Engine awal sebelum pindah ke Unreal |
| **Unreal Engine 4** | Engine final untuk game pertama (shipping) |
| **Unreal Engine 5** | Dipakai untuk sekuel, *Kena: Scars of Kosmora* |

**Sumber**: [foro3d.com — Kena: Bridge of Spirits Showcases UE4's Graphical Capabilities](https://foro3d.com/en/2026/february/kena-bridge-of-spirits-showcases-the-graphical-capabilities-of-unreal-engine-4.html), [80.lv — Visual Identity & Development](https://80.lv/articles/visual-identity-development-of-kena-bridge-of-spirits)

**Catatan alasan pindah engine**: Unity dianggap tempat awal yang bagus, tapi Unreal memberi tools yang lebih ramah-artist, khususnya berguna untuk anggota tim berlatar VFX, dan Sequencer tool sangat berdampak untuk pipeline animasi dan storytelling sinematik mereka.

**Sumber**: [80.lv — Visual Identity & Development](https://80.lv/articles/visual-identity-development-of-kena-bridge-of-spirits)

---

## 5. Teknik Rambut (Hair) — Detail Teknis Penting

Rodrigo Gonçalves (yang pertama kali mewujudkan Kena dalam 3D) terus menyempurnakan dan mengeksplorasi teknik real-time khusus untuk rambut. Setelah banyak iterasi, tim menemukan pendekatan **hybrid**:
- **Solid geometry** untuk bentuk besar rambut — memberi bentuk jelas dan menangkap cahaya dengan baik.
- **Alpha planes/cards** untuk detail helai rambut individual — menambah variasi dan kesan "imperfection" alami.

Teknik serupa (perhatian detail tinggi) juga diterapkan ke pakaian — menambahkan berbagai pola kain dan bahkan tepi yang terlihat usang/lusuh.

**Sumber**: [PlayStation Blog — Bringing the Lead Character of Kena to Life](https://blog.playstation.com/2021/09/15/bringing-the-lead-character-of-kena-bridge-of-spirits-to-life/)

**Detail animasi rambut & kain**: Untuk karakter utama Kena secara spesifik, SELURUH animasi rambut dan kainnya (termasuk efek angin di rambut) **dianimasikan dengan tangan (hand-animated)**, bukan pakai physics simulation — meski karakter lain di game memang memakai physics. Ini keputusan sadar untuk menjaga kontrol artistik penuh pada karakter hero.

**Sumber**: [PlayStation Blog — Bringing the Lead Character of Kena to Life](https://blog.playstation.com/2021/09/15/bringing-the-lead-character-of-kena-bridge-of-spirits-to-life/)

---

## 6. Teknik Material & Shading

- **Subsurface Scattering** dipakai pada kulit karakter, dikombinasikan texture work yang detail, menghasilkan tampilan kulit yang kaya — sangat mendukung desain karakter bergaya "Pixar-like".
- **Baked lighting** (bukan real-time ray tracing) jadi metode pencahayaan utama, dipadu particle effect berkualitas tinggi.
- Shader kain dan lumpur dideskripsikan sangat detail dan "rich" oleh reviewer, menjadi salah satu elemen visual yang paling dipuji.

**Sumber**: [MMORPG.com — Kena: Bridge of Spirits PC Review](https://www.mmorpg.com/reviews/kena-bridge-of-spirits-pc-review-2000123183)

---

## 7. Sistem Lingkungan Signature: "Deadzone Regrowth"

Ini salah satu temuan paling relevan untuk mekanik "penyembuhan/pemulihan area" di game kamu (mirip konsep Altar Duka yang menghangatkan sektor). Josh Grier menjelaskan proses teknisnya:
- Tim menulis **mask ke render target** untuk menandai area yang perlu bertransisi.
- Area "corrupted" (Deadzone) ditransisikan menjadi hutan yang dipulihkan secara visual.
- Setelah mengalahkan musuh dan memulihkan area, aset deadzone secara visual "layu" (wither away) sementara foliage subur tumbuh dinamis menggantikannya.
- Seluruh foliage yang terlibat transisi ini dipengaruhi oleh **sistem angin (wind system)** milik game, membantu menutup encounter combat dengan momen sinematik yang memuaskan secara visual.

**Sumber**: [80.lv — Visual Identity & Development of Kena: Bridge of Spirits](https://80.lv/articles/visual-identity-development-of-kena-bridge-of-spirits)

**Relevansi langsung untuk Lentera Pudar**: sistem ini adalah cetak biru teknis paling konkret yang bisa diadaptasi untuk visual "pencairan es" saat Altar Duka dinyalakan — pakai render target mask serupa untuk transisi area beku → hangat secara dinamis, bukan sekadar swap material statis.

---

## 8. Pipeline Sculpting: High-Poly → Retopology → Real-Time

Berdasarkan portofolio beberapa artis yang terlibat langsung (ArtStation/ZBrushCentral), pipeline pembuatan karakter/musuh mengikuti alur klasik industri:
1. **Concept art** 2D dulu (oleh concept artist khusus per karakter/musuh).
2. **High-poly sculpt** & block-out di ZBrush (proporsi & bentuk dasar).
3. **Secondary & tertiary forms** — detail lebih halus (lipatan, tekstur permukaan) ditambahkan bertahap.
4. **Retopology** untuk model real-time (poly count dioptimalkan untuk game engine).
5. **UV unwrap & texture baking** dari high-poly ke low-poly.
6. **Final texturing** di Substance Painter.

**Sumber**: [ArtStation — Rodrigo Gonçalves, Moth Enemy 3D Sketches](https://www.artstation.com/artwork/nE4Oye), [ArtStation — Rodrigo Gonçalves, Stick Enemy Real-time](https://www.artstation.com/artwork/zDQ0q4), [ZBrushCentral — Kena: Bridge of Spirits Wood Knights/Wood Mage](https://www.zbrushcentral.com/t/kena-bridge-of-spirits/422819)

**Kredit tim yang terlibat** (berguna kalau ingin riset lebih dalam portofolio masing-masing sebagai referensi tambahan):
- Concept Art: Wanchana "Vic" Intrasombat (desain karakter utama Kena)
- Concept Art musuh: Kun Vic
- 3D Modeling: Rodrigo Gonçalves (prototipe 3D pertama Kena, beberapa musuh)
- 3D Modeling: Carlos Ortega (dipuji karena "clean 3D character work")
- Detail sculpt tambahan: Eduard Oliver
- Art Direction: Mike Grier & Hunter Schmidt

---

## 9. Kolaborasi Studio Eksternal

Aset visual game ini dikerjakan berkolaborasi dengan studio animasi asal Vietnam, Sparx Animation Studios — dunia fiksionalnya terinspirasi lokasi Asia Timur seperti Jepang dan Bali.

**Sumber**: [Wikipedia — Kena: Bridge of Spirits](https://en.wikipedia.org/wiki/Kena:_Bridge_of_Spirits)

---

## 10. Optimasi & Scalability (Relevan untuk Teori Performance Budget)

Dari wawancara soal porting ke Switch 2, ada beberapa insight teknis optimasi yang relevan langsung dengan dokumen Teori bagian 17.A (Performance Budgeting):
- Penggunaan **HLOD (Hierarchical Level of Detail)** diperluas — menggabungkan mesh yang jauh jadi proxy asset tunggal untuk mengurangi draw call.
- Penggunaan **billboard** ditingkatkan untuk elemen environment jarak jauh, mengurangi biaya geometri tanpa dampak visual signifikan.
- Prioritas saat optimasi: mempertahankan **dampak emosional** (karakter & dunia) di atas kecocokan visual sempurna — kalau harus mengorbankan sesuatu, mereka memilih tetap menjaga "feeling" dibanding detail visual identik 1:1.
- Pelajaran produksi terbesar yang mereka soroti: pentingnya **dokumentasi & arsip proses** — mencatat riwayat keputusan desain secara akurat, karena rencana pengembangan game pasti banyak berubah seiring waktu (selaras dengan prinsip Living Document di dokumen Teori bagian 18.G kamu).

**Sumber**: [80.lv — Visual Identity & Development of Kena: Bridge of Spirits](https://80.lv/articles/visual-identity-development-of-kena-bridge-of-spirits)

---

## 11. Referensi Poly Count (Tidak Resmi, Sekadar Estimasi Pembanding)

Ada model 3D fan-made/rig hasil ekstraksi yang beredar publik dengan jumlah 178.408 poligon untuk model Kena secara keseluruhan — ini bukan angka resmi dari Ember Lab, tapi bisa dipakai sebagai kasar pembanding skala poly count karakter hero stylized-realistic setingkat ini.

**Sumber**: [rigmodels.com — Kena 3D Model](https://rigmodels.com/model.php?view=Kena_3d_model__LMBFTHIODGYCVRBY1UX7Q1DDH)

**Catatan**: bandingkan dengan target Style Guide kamu (40.000–60.000 tris untuk Kaelen) — angka 178k ini kemungkinan termasuk seluruh aksesoris/varian dalam satu file rig, bukan murni base mesh LOD0 gameplay, jadi jangan dipakai sebagai acuan langsung tanpa verifikasi lebih lanjut.

---

## 12. Ringkasan Poin Kunci untuk Diberikan ke AI Agent

Kalau harus diringkas jadi instruksi singkat untuk AI agent:

1. **Bukan cel-shading, bukan photoreal** — target ada di tengah, condong ke stilasi, tanpa outline hitam.
2. **Rambut**: kombinasi solid geometry (bentuk besar) + alpha card (detail helai).
3. **Rambut & kain karakter hero**: animasi tangan (hand-keyframed), bukan physics — kalau mau replikasi persis filosofi Kena untuk Kaelen/Aina, pertimbangkan hand-animate elemen kunci alih-alih full physics simulation, meski dokumen Style Guide kamu saat ini sudah menetapkan cloth-sim untuk syal Aina (ini poin yang layak didiskusikan ulang — lihat catatan di bagian 13).
4. **Kulit/skin**: Subsurface Scattering + texture detail tinggi.
5. **Lighting**: baked lighting berkualitas tinggi + particle effect kuat, bukan mengandalkan real-time ray tracing penuh.
6. **Sistem regrowth/transisi area**: render target mask untuk transisi visual dinamis — cetak biru langsung untuk mekanik pencairan es.
7. **Pipeline**: concept art → high-poly ZBrush sculpt → retopology → texturing Substance Painter → rigging key-frame friendly → level art/animasi.
8. **Prioritas saat optimasi**: emotional impact di atas kecocokan visual sempurna.

---

## 13. Catatan Penting: Potensi Penyesuaian Style Guide

Riset ini menemukan satu detail yang **berbeda** dari asumsi di Style Guide Numerik kamu sebelumnya: Ember Lab memilih **hand-animate** rambut dan kain karakter hero mereka (bukan physics simulation), justru untuk kontrol artistik lebih penuh, sementara physics dipakai untuk karakter pendukung saja.

Style Guide kamu saat ini menetapkan **cloth simulation** untuk syal Aina (parameter stiffness/damping di bagian 3). Ini bukan berarti salah — cloth sim tetap valid pilihan teknis yang lebih efisien untuk tim kecil dibanding hand-animate tiap frame — tapi ini keputusan yang layak didiskusikan sadar: apakah kamu mau ikuti filosofi Kena persis (hand-animate syal Aina untuk kontrol ekspresi maksimal, terutama karena syal ini elemen naratif paling sentral), atau tetap pakai cloth sim otomatis untuk efisiensi produksi. Tidak ada jawaban "benar" mutlak — ini trade-off waktu produksi vs kontrol artistik yang perlu keputusan sadar darimu.

---

*Dokumen ini adalah hasil riset faktual dengan sumber terverifikasi, melengkapi Moodboard Referensi dan Style Guide Numerik dalam paket dokumentasi pra-produksi Lentera Pudar.*

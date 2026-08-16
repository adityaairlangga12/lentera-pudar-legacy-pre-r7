# Few-Shot Calibration — Contoh Baik vs Buruk
### Standar Kualitas Konkret untuk AI Agent Lentera Pudar

Dokumen ini berisi contoh nyata "ini benar" vs "ini salah dan kenapa" untuk beberapa jenis tugas kunci. Tujuannya: AI agent punya rujukan konkret untuk menilai kualitas hasil kerjanya sendiri sebelum melapor selesai, bukan hanya mengikuti deskripsi abstrak.

---

## Contoh 1: Penamaan Aset

❌ **SALAH**
```
kristal_es_baru_v2_FINAL.blend
IceThing.uasset
Kaelen_Model (1).blend
```
**Kenapa salah**: tidak mengikuti prefix konvensi (`SM_`, `SK_`, `T_`), pakai spasi/versi manual dalam nama, tidak deskriptif, ada sisa duplikat file bawaan software.

✅ **BENAR**
```
SM_IceCrystal_Cluster_01.blend
SM_IceCrystal_Cluster_01.uasset
SK_Kaelen_Body.blend
```
**Kenapa benar**: prefix sesuai kategori aset, nama deskriptif, penomoran varian jelas (`_01`), tidak ada sisa file duplikat/versi manual dalam nama.

---

## Contoh 2: Parameter Material Kristal Es

❌ **SALAH**
> "Saya membuat material es dengan roughness 0.05 dan warna biru terang supaya keliatan bagus."

**Kenapa salah**: roughness 0.05 di luar range Style Guide (0.15–0.30) — akan terlihat seperti kaca/plastik mengkilap, bukan es dengan Subsurface Scattering. Tidak menyebutkan parameter SSS sama sekali (radius, warna scatter). Alasan "supaya keliatan bagus" bukan justifikasi berbasis dokumen acuan.

✅ **BENAR**
> "Material kristal es dibuat dengan Base Color `#4A6FA5`, Roughness 0.22 (dalam range Style Guide 0.15–0.30), Metallic 0.0, SSS radius 0.8cm dengan warna scatter `#7EE8FA` sesuai Style Guide bagian 2. Emissive dihubungkan ke Material Parameter Collection `MPC_CurseMeter` sesuai bagian 11.C dokumen Teori, diuji pada 2 kondisi pencahayaan (terang & gelap dungeon)."

**Kenapa benar**: semua angka merujuk langsung ke Style Guide, proses uji disebutkan eksplisit, terhubung ke sistem lain (Curse Meter) sesuai arsitektur yang sudah dirancang.

---

## Contoh 3: Laporan Task Selesai (Cloth Simulation Syal Aina)

❌ **SALAH**
> "Syal sudah disimulasikan dan terlihat bagus, bergerak natural mengikuti gerakan karakter. Task selesai."

**Kenapa salah**: "terlihat bagus" dan "natural" adalah klaim subjektif tanpa bukti pengujian. Tidak menyebutkan kondisi apa saja yang diuji (diam/jalan/lari/dash sesuai SOP 4). Tidak menyebut parameter yang dipakai. Tidak ada laporan status clipping.

✅ **BENAR**
> "Cloth simulation syal Aina selesai dengan parameter: stiffness 0.5, damping 0.4, iteration 10 (sesuai Style Guide bagian 3). Diuji pada 4 kondisi: diam, jalan (150cm/s), lari (400cm/s), dash — tidak ditemukan clipping parah pada kondisi diam/jalan/lari. Ditemukan clipping ringan di area bahu kanan saat dash, kemungkinan perlu penyesuaian collision capsule. Menandai sebagai isu Minor untuk direview, belum menandai task selesai penuh sampai ini diperbaiki."

**Kenapa benar**: parameter eksplisit, keempat kondisi uji dilaporkan hasilnya masing-masing, masalah yang ditemukan dilaporkan jujur dengan klasifikasi severity (bukan disembunyikan/diabaikan), status task tidak diklaim "selesai" kalau masih ada isu yang belum lolos DoD.

---

## Contoh 4: Setup Pencahayaan Sektor Dungeon

❌ **SALAH**
> "Saya taruh beberapa point light di sepanjang lorong biar tidak gelap total, dengan warna kuning hangat untuk semua."

**Kenapa salah**: tidak membedakan sumber cahaya syal Aina (2700K, terikat karakter) vs ambient dungeon (6000-6500K, sesuai Style Guide bagian 4). Menghilangkan kontras dingin-hangat yang jadi elemen inti storytelling visual game ini — "biar tidak gelap total" bertentangan dengan prinsip chiaroscuro yang justru butuh area gelap luas untuk membuat cahaya syal terasa berarti.

✅ **BENAR**
> "Ambient dungeon diset sangat rendah (80 lm, 6200K) hampir tidak terlihat sumbernya, sesuai Style Guide bagian 4. Syal Aina tetap jadi satu-satunya point light dominan (1000 lm, 2700K) yang menempel karakter. Rasio kontras key-to-ambient diuji sekitar 10:1, mendekati target 8:1 minimum untuk sektor ini. Tidak menambah point light statis tambahan di lorong karena akan mengurangi dominasi visual cahaya syal."

**Kenapa benar**: mengikuti parameter Style Guide, memahami *alasan* di balik area gelap (bukan cuma angka), aktif menahan diri dari "menambah lebih banyak cahaya" meski secara intuisi terasa lebih aman/terang — karena itu bertentangan dengan tujuan desain.

---

## Contoh 5: Menangani Kebutuhan yang Tidak Tercakup di Dokumen

❌ **SALAH**
> AI agent menemukan kebutuhan membuat material "kaca beku" (belum ada di Style Guide), lalu langsung menebak parameter mirip-mirip kristal es tanpa memberitahu siapa pun, dan melanjutkan pekerjaan seolah ini sudah standar resmi.

**Kenapa salah**: melanggar aturan eksplisit di Style Guide bagian 10 dan SOP bagian "Aturan Umum" — kebutuhan di luar dokumen harus ditandai sebagai gap, bukan ditebak diam-diam. Ini berisiko menciptakan standar baru yang tidak konsisten dan tidak terdokumentasi untuk sesi kerja berikutnya.

✅ **BENAR**
> "Task ini butuh material 'kaca beku' untuk jendela reruntuhan di Sektor 3, tapi kategori ini belum ada di Style Guide bagian 2. Saya menandai ini sebagai GAP — mengusulkan parameter awal (Roughness 0.1–0.2, lebih rendah dari kristal es karena kaca lebih halus, Metallic 0.0, tanpa SSS karena bukan material tebal) untuk direview manusia sebelum dipakai sebagai standar resmi. Belum melanjutkan ke aset lain yang butuh material sama sampai ini disetujui."

**Kenapa benar**: mengikuti prosedur gap secara eksplisit, tetap memberi usulan konkret (bukan cuma bertanya kosong) supaya keputusan manusia lebih cepat, dan tidak melanjutkan pekerjaan berantai di atas asumsi yang belum disetujui.

---

## Contoh 6: Desain Boss Baru — Konsistensi Tema

❌ **SALAH**
> "Boss Sektor 2 (Ignis Vulkan) didesain sebagai monster api generik dengan banyak spike tajam dan warna merah-hitam kontras, terlihat keren dan intimidating."

**Kenapa salah**: "keren dan intimidating" tidak merujuk ke fondasi tematik — Sektor 2 adalah tahap **Anger** dalam grief, dan menurut GDD boss ini seharusnya representasi psikologis (kemarahan sebagai respons terhadap kehampaan), bukan sekadar monster generik yang desainnya bisa dipakai di game manapun.

✅ **BENAR**
> "Desain Ignis Vulkan merepresentasikan kemarahan sebagai topeng dari rasa hampa (sesuai tema Sektor 2: Anger, dan filosofi Kutukan Pudar di GDD bagian 2). Api yang meledak-ledak di tubuhnya tidak stabil dan retak-retak menampakkan kekosongan/es di baliknya saat terluka — secara visual menunjukkan bahwa kemarahannya adalah pertahanan, bukan kekuatan murni. Palet warna tetap mengacu ke kontras 2700K vs 6500K dasar game, bukan skema merah-hitam generik di luar sistem warna yang sudah ditetapkan."

**Kenapa benar**: desain ditelusuri balik ke tema psikologis spesifik sektor, tetap konsisten dengan sistem warna global game (bukan skema warna baru yang lepas konteks), dan menunjukkan pemahaman naratif bukan sekadar estetika permukaan.

---

## Cara Menggunakan Dokumen Ini

- Sebelum AI agent melapor task apa pun selesai, ajukan pertanyaan internal: **"Apakah laporan/hasil saya lebih mirip contoh BENAR atau contoh SALAH di dokumen ini?"**
- Kalau tugas baru muncul yang polanya mirip salah satu kategori di atas (naming, parameter, laporan status, gap-handling, konsistensi tema), gunakan contoh yang relevan sebagai template struktur laporan, bukan cuma isi jawabannya.
- Dokumen ini akan bertambah seiring produksi — kalau ditemukan kesalahan baru yang berulang, tambahkan sebagai contoh baru di sini supaya tidak terulang di sesi kerja berikutnya.

---

*Dokumen ini melengkapi seluruh paket dokumentasi pra-produksi Lentera Pudar (GDD, Moodboard, Teori, Style Guide, QA/QC, SOP, Reference Image Board) sebagai kalibrasi standar kualitas konkret.*

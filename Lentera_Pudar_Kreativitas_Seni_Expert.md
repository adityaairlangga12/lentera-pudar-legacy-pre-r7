# Kreativitas & Nilai Seni Tingkat Expert — Lentera Pudar
### Kerangka Estetika untuk Menilai dan Membuat Keputusan Visual/Naratif (Pelengkap Paket Dokumentasi Pra-Produksi)

Dokumen ini melengkapi tiga dokumen Expert sebelumnya (Fisika, Matematika, Psikologi) dengan lapisan yang berbeda sifatnya: bukan "bagaimana sistem bekerja secara teknis" atau "bagaimana pemain merasa secara psikologis", melainkan **bagaimana menilai apakah sebuah keputusan visual/naratif secara artistik kuat** — supaya AI agent tidak hanya menghasilkan output yang benar secara teknis, tapi juga punya kerangka untuk menilai kualitas estetikanya sendiri.

---

## 1. Prinsip Desain Visual & Komposisi

### A. Hierarki Visual
Mata manusia tidak melihat semua elemen di layar dengan bobot sama — desain yang baik secara sengaja mengarahkan urutan perhatian: elemen utama (misal syal Aina yang menyala) harus punya kontras nilai/warna/gerak tertinggi dibanding elemen sekunder (lingkungan) dan tersier (detail latar).

### B. Rule of Thirds & Leading Lines
Penempatan elemen penting di titik perpotongan grid sepertiga (bukan tepat di tengah) menghasilkan komposisi yang terasa dinamis, bukan statis. **Leading lines** (garis arsitektur, cahaya, bayangan) dipakai untuk menuntun mata pemain ke titik fokus tanpa perlu highlight eksplisit — relevan untuk desain lorong dungeon yang mengarahkan pemain secara visual, bukan cuma lewat linear level design.

### C. Kontras Nilai (Value) Sebelum Warna
Prinsip klasik: komposisi yang kuat harus tetap terbaca dalam grayscale (kontras terang-gelap) sebelum warna ditambahkan. Kalau silhouette/value sudah bekerja, warna hanya memperkuat — bukan menutupi komposisi yang lemah.

**Instruksi untuk AI agent**: saat generate atau evaluasi shot komposisi (screenshot in-game, camera framing), cek dulu versi grayscale-nya secara mental — apakah titik fokus tetap jelas tanpa bantuan warna? Kalau tidak, masalahnya di value/kontras, bukan di palet warna.

---

## 2. Teori Warna Terapan

### A. Color Harmony sebagai Alat, Bukan Aturan Kaku
Skema warna klasik (complementary, analogous, triadic, split-complementary) adalah titik mulai, bukan resep pasti. Yang lebih penting adalah **dominasi terkontrol**: satu warna dominan (60%), satu sekunder (30%), satu aksen (10%) — rasio ini mencegah palet terasa "ramai tanpa fokus".

### B. Warna sebagai Storytelling Pasif
Palet warna bisa menyampaikan makna tanpa dialog atau teks — relevan langsung untuk 5 sektor grief:
| Tahap Grief | Arah Warna yang Umum Dipakai | Alasan Psikologis-Visual |
|---|---|---|
| Denial | Desaturasi, kabut, kontras rendah | Realitas terasa "kabur", tidak diakui |
| Anger | Merah/oranye jenuh, kontras tajam | Intensitas, urgensi, ketidakstabilan |
| Bargaining | Warna campur tak stabil, transisi cepat | Ketidakpastian, mencoba banyak arah |
| Depression | Biru/abu gelap, saturasi rendah, cahaya minim | Berat, sunyi, energi rendah |
| Acceptance | Warna hangat lembut, cahaya kembali | Ketenangan, resolusi |

### C. Warna Tidak Bekerja Sendiri — Interaksi dengan Cahaya (Lumen)
Karena proyek memakai Lumen (indirect lighting real-time — lihat dokumen Fisika Expert bagian 5), palet warna dinding/lingkungan **akan otomatis "mewarnai" objek di dekatnya** lewat cahaya pantul. Ini bukan detail teknis semata — bisa dimanfaatkan sebagai storytelling pasif tambahan tanpa kerja ekstra (contoh: cahaya hangat syal Aina memantul dan mewarnai dinding dingin di sekitarnya sebagai representasi visual harapan di tengah kegelapan).

**Instruksi untuk AI agent**: saat memilih palet warna area/sektor, jangan berpikir warna sebagai properti objek yang berdiri sendiri — pikirkan sebagai bagian dari sistem pencahayaan yang saling memengaruhi. Palet yang direncanakan tanpa mempertimbangkan efek pantulnya akan menghasilkan warna aktual di dalam game yang meleset dari rencana.

---

## 3. Silhouette & Readability

### A. Prinsip Klasik Character Design
Karakter dan prop yang kuat desainnya harus tetap terbaca hanya dari siluet hitam-putih — kalau dua siluet karakter/musuh terlihat mirip, pemain akan kesulitan membedakan secara instan di tengah combat cepat, apapun detail teksturnya.

### B. Silhouette sebagai Alat Gameplay, Bukan Cuma Estetika
Untuk combat readable ala Hellblade (sudah jadi keputusan desain di dokumen QA/QC), keterbacaan siluet punya fungsi mekanik langsung: pemain harus bisa membedakan telegraph serangan musuh (siluet windup vs siluet netral) hanya dari bentuk siluet dalam sepersekian detik, tanpa perlu membaca detail tekstur/warna.

**Instruksi untuk AI agent**: saat mendesain atau evaluasi desain musuh/prop baru, uji siluetnya secara terpisah dari detail permukaan. Kalau siluet windup attack tidak cukup beda dari siluet idle, itu masalah desain fundamental yang harus diperbaiki di tahap silhouette — bukan bisa ditambal dengan VFX tambahan saja.

---

## 4. Prinsip Sinematografi

### A. Bahasa Kamera yang Sudah Jadi Referensi (Hellblade)
- **Close framing terus-menerus**: menciptakan claustrophobia dan intimasi paksa dengan karakter — relevan untuk membuat pemain merasakan beban emosional Kaelen secara langsung, bukan sebagai pengamat jauh.
- **Minim cut, banyak long take**: mempertahankan presence (lihat dokumen Psikologi Expert bagian 5) dengan tidak memutus kontinuitas ruang secara tiba-tiba.
- **Depth of field selektif**: mengaburkan latar untuk memfokuskan perhatian emosional ke wajah/ekspresi karakter di momen naratif penting.

### B. Camera sebagai Karakter, Bukan Alat Netral
Sinematografi yang kuat memperlakukan kamera seolah punya "sikap" terhadap adegan — kamera yang goyah halus (subtle handheld sway) di area Anxiety/Anger vs kamera yang statis-berat di area Depression, secara halus mengomunikasikan kondisi emosional tanpa dialog.

**Instruksi untuk AI agent**: saat menyetel parameter kamera (FOV, sway, DOF, framing) per sektor grief, jangan perlakukan sebagai satu setting default untuk seluruh game — setiap sektor butuh "kepribadian kamera" sendiri yang konsisten dengan tahap emosional di dalamnya (cross-reference ke dokumen Matematika Expert bagian 3.C soal kurva easing per tahap grief).

---

## 5. Estetika Minimalism & Negative Space

### A. "Kurang adalah Lebih" sebagai Prinsip Fungsional
Ruang kosong (negative space) bukan sekadar area "tidak ada apa-apa" — ia aktif mengarahkan perhatian ke elemen yang ada, dan memberi napas visual/psikologis. Relevan langsung ke dua keputusan desain proyek yang sudah ada: minimal-HUD (cognitive load — lihat dokumen Psikologi Expert bagian 4) dan gaya visual Kena yang cenderung bersih tanpa clutter berlebih.

### B. Kapan Minimalism Gagal
Minimalism yang salah kaprah bisa terasa "kosong" alih-alih "tenang" — bedanya terletak pada apakah ruang kosong itu **disengaja mengarahkan mata** (misal area lapang sebelum boss fight sebagai jeda tarik napas) vs sekadar area yang belum diisi detail karena kurang waktu produksi.

**Instruksi untuk AI agent**: saat mengevaluasi apakah sebuah area/scene "terlalu kosong", tanyakan dulu apakah kekosongan itu melayani fungsi (jeda emosional, fokus visual) atau sekadar area yang belum selesai didesain. Kriteria ini mencegah agent salah menambah detail ke area yang justru butuh tetap kosong secara sengaja.

---

## 6. Teori Gaya & Stilasi (Stylization Theory)

### A. Stilasi Bukan Sekadar "Kurang Detail"
Stilasi ala Kena adalah proses sengaja: bentuk realistis disederhanakan dan sebagian dilebih-lebihkan (exaggeration terkontrol) untuk memperkuat ekspresi dan appeal — bukan sekadar mengurangi jumlah polygon atau detail tekstur. Prinsip animasi klasik "squash and stretch" dan "appeal" (dari 12 prinsip animasi Disney) relevan di sini meski proyek bukan animasi kartun.

### B. Konsistensi Level Stilasi Antar Elemen
Masalah umum saat menggabungkan referensi (Kena artstyle + mekanik Hellblade yang lebih realistis) adalah **level stilasi yang tidak konsisten** antar elemen — karakter stylized di dunia yang terlalu realistis (atau sebaliknya) terasa "salah tempat" secara visual, meski masing-masing elemen bagus sendiri-sendiri.

**Instruksi untuk AI agent**: setiap kali membuat aset baru (prop, karakter, environment), cek level stilasinya terhadap aset yang sudah ada — bandingkan rasio ukuran fitur (mata, tangan), kehalusan permukaan, dan proporsi terhadap baseline yang sudah ditetapkan di Style Guide Numerik. Ketidakkonsistenan stilasi adalah salah satu penyebab paling umum sebuah game terasa "campur aduk" secara visual meski tiap aset individual berkualitas.

---

## 7. Semiotika Visual — Simbol dan Metafora

### A. Tanda (Sign), Penanda (Signifier), dan Petanda (Signified)
Dalam semiotika, sebuah objek visual (penanda) membawa makna (petanda) yang tidak selalu terkait literal dengan fungsinya. Syal Aina sebagai objek fisik (penanda) membawa makna ikatan, kehangatan, dan kehilangan (petanda) — makna itu tidak melekat otomatis, tapi dibangun lewat pengulangan dan konteks penggunaan sepanjang game.

### B. Metafora Visual yang Sudah Ada di Proyek dan Cara Memperkuatnya
| Elemen | Makna Literal | Makna Metaforis | Cara Memperkuat |
|---|---|---|---|
| Syal Aina (memendek) | Kain fisik | Ikatan yang terkikis, pengorbanan | Visual degradasi bertahap, bukan tiba-tiba |
| Kristal es (pecah) | Material rapuh | Kerapuhan emosi yang ditekan | Pola retak yang "mengikuti" tekanan naratif, bukan acak |
| Cahaya syal (meredup/menyala) | Sumber cahaya | Harapan, kehadiran Aina | Intensitas cahaya terikat ke progress emosional, bukan waktu/jarak |

**Instruksi untuk AI agent**: setiap elemen visual berulang (recurring visual motif) harus diperlakukan sebagai simbol yang maknanya dibangun kumulatif — perubahan pada elemen ini (warna, bentuk, intensitas) harus selalu punya alasan naratif, bukan variasi acak demi variasi visual semata. Kekonsistenan penggunaan simbol adalah yang membuatnya "berbicara" ke pemain tanpa perlu penjelasan eksplisit.

---

## 8. Prinsip Kritik Seni / Evaluasi Estetika

### A. Kerangka Formal untuk Menilai "Apakah Ini Bagus"
Alih-alih menilai lewat selera murni, kritik seni formal biasa memakai kriteria terstruktur:
- **Unity (kesatuan)**: apakah semua elemen (warna, komposisi, gerak) terasa melayani satu tujuan/mood yang sama?
- **Tension (ketegangan visual)**: apakah ada dinamika — kontras, asimetri terkontrol — yang membuat mata tertarik, bukan statis membosankan?
- **Resolution (resolusi)**: apakah ketegangan tadi akhirnya "terselesaikan" secara visual (mata menemukan titik istirahat), bukan terasa mengambang tanpa arah?

### B. Menerapkan Kerangka Ini ke Evaluasi In-Game
Kerangka ini bisa dipakai bukan cuma untuk lukisan/ilustrasi statis, tapi untuk shot in-game, transisi cutscene, bahkan layout level:
- Level dengan unity lemah = campuran gaya arsitektur/prop yang tidak konsisten temanya.
- Shot dengan tension nol = komposisi terlalu simetris/statis, tidak mengarahkan mata kemana-mana.
- Scene tanpa resolution = terlalu banyak elemen kompetisi visual tanpa titik fokus jelas yang "menyelesaikan" komposisi.

**Instruksi untuk AI agent**: saat diminta menilai kualitas visual sebuah hasil kerja (bukan cuma membuatnya), gunakan tiga kriteria ini sebagai kerangka evaluasi eksplisit, bukan menjawab "bagus/tidak bagus" berdasarkan kesan umum saja. Ini juga bisa disambungkan langsung ke protokol Visual Self-Review Loop yang sudah ada — tiga kriteria ini bisa jadi bagian dari checklist review otomatis.

---

## 9. Ringkasan Peta Estetika ke Keputusan Produksi

| Area | Sistem/Keputusan yang Menggunakan | Risiko kalau Diabaikan |
|---|---|---|
| Desain Visual & Komposisi | Camera framing, level layout | Shot tidak mengarahkan mata, terasa acak |
| Teori Warna Terapan | Palet per sektor grief, interaksi Lumen | Storytelling pasif hilang, warna aktual meleset dari rencana |
| Silhouette & Readability | Desain musuh, telegraph combat | Pemain gagal baca telegraph, combat terasa tidak adil |
| Sinematografi | Parameter kamera per sektor | Kamera terasa generik, kehilangan "kepribadian" per tahap |
| Minimalism & Negative Space | HUD, layout area jeda | Area kosong terasa belum selesai, bukan disengaja |
| Stilasi (Stylization Theory) | Konsistensi aset baru vs Style Guide | Game terasa "campur aduk" secara visual |
| Semiotika Visual | Motif berulang (syal, kristal, cahaya) | Simbol kehilangan makna kalau dipakai tidak konsisten |
| Kritik Seni / Evaluasi Estetika | Visual Self-Review Loop | Evaluasi kualitas jadi subjektif tanpa kerangka jelas |

**Instruksi umum untuk AI agent**: dokumen ini melengkapi (bukan menggantikan) tiga dokumen Expert sebelumnya. Fisika/Matematika menjawab "apakah ini benar secara teknis", Psikologi menjawab "apakah ini berdampak secara emosional", dan dokumen ini menjawab "apakah ini kuat secara artistik". Sebuah keputusan produksi idealnya lolos ketiga lapisan ini sekaligus — solusi yang benar secara teknis tapi lemah secara estetika, atau indah secara visual tapi salah secara fisika/psikologi, sama-sama perlu direvisi sebelum dianggap final.

---

*Dokumen ini adalah pelengkap paket dokumentasi pra-produksi Lentera Pudar, melengkapi dokumen Fisika Expert, Matematika Expert, dan Psikologi Expert.*

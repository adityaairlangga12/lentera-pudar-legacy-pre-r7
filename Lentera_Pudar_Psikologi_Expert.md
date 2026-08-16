# Psikologi Pemain Tingkat Expert — Lentera Pudar
### Versi Mendalam untuk Desain Naratif, Mekanik Grief, dan Respons Emosional (Pelengkap Referensi Teori Bagian 15)

Dokumen ini menggali lebih dalam mekanisme psikologis di balik keputusan desain proyek — level detail yang dibutuhkan kalau AI agent harus menilai apakah sebuah keputusan mekanik/naratif akan menghasilkan efek emosional yang dituju, bukan hanya menerapkan teori secara permukaan.

---

## 1. Self-Determination Theory — Detail Terapan (Lanjutan dari Bagian 15.A)

### A. Tiga Kebutuhan sebagai Diagnostik Desain
Setiap keputusan mekanik baru bisa diuji lewat tiga pertanyaan:
- **Autonomy**: apakah pemain punya pilihan nyata (bukan ilusi pilihan)? Urutan eksplorasi area grief boleh bebas, tapi kalau semua jalur berujung sama tanpa variasi konsekuensi, autonomy hanya kosmetik.
- **Competence**: apakah pemain merasa progress skill-nya sendiri, bukan cuma angka karakter naik? Combat readable (telegraph jelas, punishing tapi fair) memberi rasa kompetensi lewat penguasaan pola — beda dengan game yang naikkan kesulitan lewat angka HP musuh saja.
- **Relatedness**: apakah keterikatan emosional terasa dibangun, bukan diklaim naratif? Ikatan Kaelen-Aina harus ditunjukkan lewat momen gameplay konkret (bukan cuma dialog/cutscene) supaya pemain benar-benar merasakannya.

**Instruksi untuk AI agent**: saat mengevaluasi mekanik baru, jalankan checklist tiga kebutuhan ini secara eksplisit. Mekanik yang gagal memenuhi ketiganya sekaligus biasanya terasa "kosong" meski secara teknis berfungsi baik.

### B. Extrinsic vs Intrinsic Motivation Crowding-Out
Riset SDT menunjukkan reward ekstrinsik yang tidak tepat (misal leaderboard kompetitif) bisa **mengurangi** motivasi intrinsik yang sudah ada — fenomena disebut *motivation crowding-out*. Untuk game reflektif seperti Lentera Pudar, menambahkan sistem skor/ranking kompetitif berisiko merusak keterlibatan emosional yang justru jadi inti pengalaman.

**Instruksi untuk AI agent**: kalau ada usulan menambah sistem skor, achievement dengan angka besar, atau leaderboard — pertimbangkan risiko crowding-out ini secara eksplisit sebelum implementasi, bukan hanya menganggapnya fitur netral tambahan.

---

## 2. Operant Conditioning & Reward Timing — Detail Etis (Lanjutan dari Bagian 15.B)

### A. Skedul Reinforcement (Skinner)
| Jenis Skedul | Pola Reward | Efek Psikologis | Cocok untuk Lentera Pudar? |
|---|---|---|---|
| Fixed Ratio | Setelah N aksi tertentu | Predictable, burst lalu jeda | Ya — misal tiap Altar Duka selesai = 1 fragmen memori |
| Variable Ratio | Acak setelah rata-rata N aksi | Paling adiktif (dasar gacha/slot) | Tidak — bertentangan dengan nada reflektif |
| Fixed Interval | Setelah waktu tetap | Predictable tapi kurang memotivasi | Kurang relevan untuk aksi berbasis kondisi |
| Variable Interval | Acak dalam rentang waktu | Motivasi bertahan lama tanpa burst | Netral, jarang dipakai di narrative game |

### B. Kenapa Fixed/Predictable Reward Cocok Secara Tematik
Reward acak (variable ratio) menciptakan ketegangan "mungkin dapat, mungkin tidak" yang cocok untuk game kompetitif/retensi tinggi, tapi **bertentangan** dengan tema grief yang butuh rasa "konsekuensi jelas dan bisa direnungkan" — bukan dorongan impulsif untuk terus mencoba lagi. Pemain perlu merasa setiap pengorbanan (memendeknya syal Aina) adalah keputusan sadar dengan hasil yang bisa diprediksi, bukan gamble.

**Instruksi untuk AI agent**: tolak usulan sistem reward acak (loot, drop chance, random buff) untuk elemen naratif inti. Boleh dipakai terbatas hanya untuk elemen kosmetik/opsional yang tidak menyentuh tema utama.

---

## 3. Loss Aversion — Model Matematis dan Aplikasi Naratif (Lanjutan dari Bagian 15.C)

### A. Prospect Theory (Kahneman & Tversky)
Secara formal, fungsi nilai subjektif manusia terhadap gain vs loss tidak simetris — kerugian dirasakan kira-kira **2-2.5x lebih berat** dibanding keuntungan bernilai objektif setara. Fungsi nilai berbentuk cekung untuk gain, cembung untuk loss, dan lebih curam di sisi loss.

### B. Aplikasi Presisi ke The Fading Scarf
Ini alasan matematis kenapa mekanik "syal memendek permanen" jauh lebih efektif secara emosional dibanding "dapat kemampuan baru dengan nilai setara":
- Kalau pemain diberi *pilihan eksplisit* untuk mengorbankan panjang syal demi kekuatan, loss aversion membuat momen keputusan itu terasa berat — pemain akan ragu meski secara matematis "untung".
- Efek ini menguat kalau kerugian **permanen dan terlihat** (visual syal yang memendek nyata di layar), bukan tersembunyi di angka stat.

**Instruksi untuk AI agent**: pastikan setiap kali mekanik ini dipicu, konsekuensi visual (pemendekan syal) benar-benar terlihat jelas ke pemain sebelum keputusan final dikonfirmasi — bukan baru terlihat setelahnya. Loss aversion hanya bekerja optimal kalau kerugian terasa nyata di momen keputusan, bukan hanya di hasil akhir.

---

## 4. Cognitive Load & Emotional Bandwidth (Lanjutan dari Bagian 15.D)

### A. Model Cognitive Load (Sweller)
Cognitive load terbagi tiga: **intrinsic** (kompleksitas tugas itu sendiri — misal pola combat), **extraneous** (beban tak perlu dari cara informasi disajikan — HUD berantakan), dan **germane** (usaha mental produktif untuk membangun pemahaman — belajar pola musuh). Desain minimal-HUD ala Hellblade secara spesifik menekan *extraneous load* supaya kapasitas mental pemain tersisa untuk *germane load* (memahami combat) dan bandwidth emosional (merasakan cerita).

### B. Emotional Bandwidth sebagai Sumber Daya Terbatas
Konsep tambahan yang relevan: kapasitas emosional pemain untuk memproses konten berat (grief, kehilangan) juga terbatas per sesi — mirip cognitive load tapi untuk domain afektif. Kalau intensitas emosional dipaksa tinggi terus-menerus tanpa jeda, pemain mengalami *emotional fatigue* dan justru mati rasa (desensitization) terhadap momen puncak yang seharusnya paling berat.

**Instruksi untuk AI agent**: saat menyusun pacing level/narasi, sisipkan momen jeda tenang (bukan cuma jeda combat) di antara beat emosional berat — pola tegang-lega-tegang, bukan tegang terus-menerus. Ini prinsip pacing yang sama pentingnya dengan pacing combat difficulty, tapi sering terlewat karena fokusnya biasanya ke sisi mekanik saja.

---

## 5. Presence & Embodiment — Detail Mekanisme (Lanjutan dari Bagian 15.E)

### A. Tiga Lapisan Presence
- **Spatial presence**: rasa "berada di ruang itu" — didukung kamera dekat, audio 3D, skala lingkungan yang konsisten dengan tinggi karakter.
- **Sensorimotor presence (embodiment)**: rasa "tubuh itu adalah tubuhku" — didukung feedback gerakan yang konsisten (animasi respons instan terhadap input, tidak ada delay tersembunyi) dan detail biomekanis (lihat cross-reference ke dokumen Anatomi & Kinesiologi).
- **Social/emotional presence**: rasa keterhubungan dengan karakter lain (Aina) — dibangun lewat micro-expression, respons kontekstual, bukan hanya dialog scripted.

### B. Kerentanan Presence terhadap "Gangguan Teknis Kecil"
Presence adalah keadaan mental yang rapuh — sekali "pecah" (misal animasi glitch, hitbox terasa tidak adil, delay input yang tidak konsisten), butuh waktu untuk pemain kembali merasa immersed. Ini alasan psikologis kenapa QA/QC ketat terhadap bug kecil (bukan cuma bug besar/crash) sangat penting untuk game bertema emosional — bug kecil yang "cuma kosmetik" secara teknis tetap bisa merusak presence secara signifikan.

**Instruksi untuk AI agent**: prioritaskan bug yang merusak *feedback loop input-respons* (delay, animasi tidak sinkron, hitbox tidak adil) di atas bug kosmetik murni saat triase QA — karena dampaknya ke presence jauh lebih besar dibanding proporsi keseriusan teknisnya.

---

## 6. Teori Tambahan yang Relevan (Belum Tercakup di Bagian 15 Dasar)

### A. Flow State (Csikszentmihalyi)
Flow terjadi saat tantangan dan skill pemain seimbang — terlalu mudah menyebabkan boredom, terlalu sulit menyebabkan anxiety. Untuk combat Kaelen, ini berarti kurva kesulitan harus adaptif terhadap skill pemain yang teramati (bukan cuma linear terhadap progress level) — relevan untuk sistem dynamic difficulty jika nanti dipertimbangkan.

### B. Narrative Transportation Theory
Semakin pemain "terbawa" (transported) ke dalam narasi, semakin rendah resistensi kritis mereka terhadap pesan emosional cerita — tapi juga semakin rentan terhadap gangguan yang menarik mereka keluar (breaking the fourth wall tanpa sengaja, UI yang terlalu game-y). Prinsip ini memperkuat alasan minimal-HUD dan camera framing sinematik yang sudah jadi keputusan desain proyek.

### C. Kübler-Ross Grief Model sebagai Kerangka Struktural (Bukan Sekadar Tema)
Lima tahap grief (Denial, Anger, Bargaining, Depression, Acceptance) yang sudah dipakai sebagai struktur 5 sektor sebaiknya dipahami agent bukan sebagai urutan linear kaku, melainkan **model non-linear** — riset grief modern (termasuk kritik terhadap model asli Kübler-Ross) menunjukkan tahap-tahap ini bisa tumpang tindih atau berulang. Agent bisa memanfaatkan ini secara naratif: elemen dari tahap sebelumnya boleh muncul samar di sektor selanjutnya (echo visual/audio), memberi kesan grief yang realistis, bukan checklist tahap yang dilewati satu-satu lalu selesai.

**Instruksi untuk AI agent**: saat mendesain transisi antar sektor grief, pertimbangkan echo/overlap tipis dari tahap sebelumnya (bukan pemutusan bersih), untuk merefleksikan sifat non-linear grief yang lebih akurat secara psikologis dan lebih berkesan secara naratif.

---

## 7. Ringkasan Peta Psikologi ke Keputusan Desain

| Teori | Sistem yang Menggunakan | Risiko kalau Diabaikan |
|---|---|---|
| Self-Determination Theory | Struktur eksplorasi, combat, ikatan karakter | Progress terasa kosong/tidak bermakna |
| Operant Conditioning | Sistem reward Altar Duka | Nada tematik rusak kalau reward dibuat acak |
| Loss Aversion | The Fading Scarf | Efek emosional lemah kalau kerugian tidak terlihat jelas |
| Cognitive/Emotional Load | HUD, pacing narasi | Fatigue emosional, momen puncak jadi tumpul |
| Presence & Embodiment | Kamera, animasi, QA bug kecil | Immersion pecah oleh bug "kecil" |
| Flow State | Kurva kesulitan combat | Boredom atau anxiety, bukan engagement |
| Narrative Transportation | Framing kamera, minimal-HUD | Pemain "keluar" dari cerita akibat gangguan UI |
| Grief Model (non-linear) | Struktur 5 sektor & transisi | Grief terasa seperti checklist, bukan pengalaman |

**Instruksi umum untuk AI agent**: setiap keputusan desain yang menyentuh emosi pemain (reward, kehilangan, pacing, transisi) harus bisa dijelaskan lewat minimal satu teori di atas. Kalau tidak bisa dijelaskan lewat teori manapun, itu sinyal untuk mempertanyakan ulang keputusan tersebut sebelum diimplementasi — bukan menerapkannya hanya karena "terasa keren" secara intuitif.

---

*Dokumen ini adalah versi mendalam dari Referensi Teori bagian 15 (Psikologi Pemain), sebagai bagian dari paket dokumentasi pra-produksi Lentera Pudar.*

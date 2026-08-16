# Level Design & Environmental Storytelling — Lentera Pudar
### Bagaimana Ruang Bercerita Tanpa Kata (Pelengkap Game Design Systems Expert & Story Bible)

Dokumen ini mengisi celah antara **Game_Design_Systems_Expert.md** (bicara soal *waktu* — pacing, kurva kesulitan, core loop) dan **Story_Bible_Lore.md** + **Kreativitas_Seni_Expert.md** (bicara soal *makna* dan *visual per-shot*). Yang belum ada: bagaimana *ruang itu sendiri*, lewat tata letak, jalur, dan penempatan objek, ikut menyampaikan tahap grief yang sedang dialami Kaelen — sebuah teknik yang jadi salah satu kekuatan terbesar Hellblade sebagai referensi utama proyek ini.

---

## 1. Prinsip Dasar Environmental Storytelling

Environmental storytelling adalah teknik menyampaikan narasi lewat *susunan ruang dan objek*, bukan dialog atau cutscene. Ada tiga mekanisme utama:

- **Static Narrative (Cerita Diam)** — objek/reruntuhan yang menyiratkan peristiwa masa lalu tanpa ada yang menjelaskannya (misal altar yang sudah retak sebelum pemain sampai, menyiratkan pengorbanan yang terjadi lama sebelumnya).
- **Emergent Narrative (Cerita dari Interaksi Pemain)** — makna yang muncul dari *bagaimana* pemain bergerak lewat ruang, bukan dari objek tetap (misal pemain tersesat berulang di area tertentu — dan itu memang disengaja, lihat bagian 3).
- **Symbolic Environment (Ruang sebagai Metafora)** — bentuk/tata letak ruang secara langsung merepresentasikan kondisi psikologis karakter, bukan cuma tempat kejadian berlangsung (lihat bagian 2).

Untuk Lentera Pudar, ketiga mekanisme ini sebaiknya dipakai bersamaan — bukan dipilih salah satu — karena tema grief butuh lapisan makna yang bisa ditangkap pemain di kedalaman berbeda-beda (ada yang cuma sadar "ruang ini terasa berat", ada yang sadar sampai ke detail simbolisnya).

---

## 2. Pemetaan Spasial ke 5 Sektor Grief

Mengikuti struktur yang sudah dipakai di Style_Guide_Numerik dan Anatomi_Kinesiologi (postur per-tahap grief), berikut prinsip desain ruang per tahap:

### A. Denial
- **Layout**: ruang berulang atau simetris berlebihan — koridor yang terlihat identik dari berbagai arah, membuat pemain (dan Kaelen) sulit membedakan "sudah pernah ke sini atau belum".
- **Navigasi**: jalur yang looping kembali ke titik awal tanpa disadari pemain sampai terjadi beberapa kali — representasi mekanis dari penyangkalan yang berulang.
- **Skala ruang**: cenderung sempit dan menekan (rendah, dinding dekat) — kontras nanti dengan Acceptance yang lebih terbuka.

### B. Anger
- **Layout**: ruang tidak beraturan, sudut tajam, jalur terputus yang memaksa rute memutar — friksi navigasi mencerminkan friksi emosional.
- **Elemen interaktif**: lebih banyak objek destructible/reruntuhan yang bisa dihancurkan pemain, memberi outlet fisik untuk emosi yang direpresentasikan.
- **Skala ruang**: fluktuatif — kadang sangat sempit (koridor menekan), kadang tiba-tiba terbuka ke area combat luas, meniru ketidakstabilan emosi.

### C. Depression
- **Layout**: ruang sangat luas tapi kosong — jarak tempuh panjang tanpa banyak elemen interaktif, membuat pemain merasakan "berat"-nya bergerak maju secara literal lewat durasi berjalan.
- **Elemen visual**: warna desaturasi, elemen partikel (debu, salju) yang bergerak lambat — menekankan waktu terasa melambat.
- **Verticality**: preferensi jalur menurun/turun (bukan menanjak) — secara bawah sadar pemain merasakan "tenggelam".

### D. Acceptance
- **Layout**: ruang mulai terbuka dan simetris secara *organik* (bukan simetri kaku ala Denial) — keteraturan yang terasa alami, bukan dipaksakan.
- **Skala ruang**: lapang, dengan sightline panjang (pemain bisa melihat jauh ke depan) — kontras langsung dengan ruang sempit di Denial.
- **Cahaya**: titik cahaya (terkait syal Aina/The Fading Scarf) jadi elemen navigasi utama, bukan cuma dekorasi — pemain diarahkan lewat cahaya, bukan lewat marker UI.

### E. Transisi Antar Sektor
Perubahan karakteristik ruang antar tahap sebaiknya terjadi *gradual dalam satu area transisi*, bukan potongan mendadak antar level — konsisten dengan prinsip transisi emosi bertahap di dokumen Ekspresi Wajah Manusia (bagian 3, transisi AU bertahap).

---

## 3. Level Flow & Pacing Navigasi

- **Linear vs Branching per Tahap**: tahap Denial dan Depression cocok dengan jalur lebih linear (kontrol pemain rendah, mencerminkan perasaan "terjebak" dalam emosi), sementara Anger dan Acceptance bisa lebih memberi pilihan jalur (kontrol pemain meningkat seiring proses grief berjalan) — ini menyambungkan langsung ke prinsip **Autonomy** di Self-Determination Theory (Psikologi_Expert bagian A).
- **Breadcrumbing Visual (bukan UI Marker)**: mengikuti prinsip minimal-HUD (Psikologi_Expert bagian D), arah jalur sebaiknya ditunjukkan lewat elemen dunia — cahaya, jejak, perubahan warna material — bukan arrow/marker UI eksplisit.
- **Rest Beat / Breathing Room**: setelah encounter combat intens, sisipkan ruang transisi tenang (tanpa musuh, pacing berjalan lambat) sebelum area berikutnya — prinsip pacing ini melengkapi kurva kesulitan di Game_Design_Systems_Expert dengan lapisan *pacing emosional*, bukan cuma pacing kesulitan mekanik.

---

## 4. Prop Placement sebagai Bahasa Naratif

- **Rule of Intentional Wear**: objek yang menunjukkan tanda pakai/kerusakan tidak boleh acak — pola kerusakan harus konsisten dengan siapa yang terakhir memakainya dan kapan, sesuai lore di Story_Bible_Lore.md (hindari kontradiksi lore lewat detail visual yang tidak dicek).
- **Repetisi Motif sebagai Penanda Memori**: objek atau simbol yang berulang di beberapa area (misal bentuk kristal es tertentu) sebaiknya konsisten merepresentasikan hal yang sama di seluruh game — pemain membangun asosiasi lewat repetisi, mirip cara leitmotif bekerja di musik (lihat Audio_Sound_Design_Expert untuk penerapan serupa di sisi audio).
- **Absence sebagai Storytelling**: kadang yang lebih kuat bukan objek yang ada, tapi objek yang *seharusnya ada tapi tidak ada* (misal ruang bekas kamar dengan siluet bersih di dinding tempat foto pernah tergantung) — teknik ini sangat efektif untuk tema kehilangan tanpa perlu voice-over penjelas.

---

## 5. Level Design untuk Combat Encounter (Sambungan ke FSM Musuh)

- **Arena Shape vs Enemy Behavior**: bentuk arena combat harus disesuaikan dengan FSM musuh yang sudah ada di Referensi_Teori_untuk_AI_Agent — arena sempit untuk musuh melee-heavy, arena terbuka untuk musuh dengan pola ranged/mengepung.
- **Sightline Control**: desain level combat sebaiknya mengontrol kapan pemain bisa melihat musuh berikutnya (foreshadowing bahaya) vs kapan disembunyikan (jump-scare/surprise terkontrol) — relevan untuk membangun tensi bertahap di tahap Anger.
- **Environmental Hazard sebagai Ekstensi Tema**: hazard fisik (es licin, reruntuhan jatuh) sebaiknya secara tematik selaras dengan tahap grief saat itu terjadi — bukan hazard generik yang bisa dipindah ke level manapun tanpa kehilangan makna.

---

## 6. Checklist Integrasi ke Visual Self-Review Loop

Poin tambahan untuk `Lentera_Pudar_AI_Automation_Visual_SelfReview_Protocol.md`:

1. Apakah karakteristik spasial ruang (skala, simetri, verticality) sudah sesuai tahap grief yang dituju (bagian 2), bukan generic dungeon layout?
2. Apakah jalur navigasi ditunjukkan lewat elemen dunia (cahaya, jejak), bukan UI marker eksplisit (bagian 3)?
3. Apakah penempatan prop sudah dicek konsistensinya dengan Story_Bible_Lore.md, bukan ditempatkan asal terlihat bagus (bagian 4)?
4. Apakah ada elemen "absence" yang dipertimbangkan sebagai opsi storytelling sebelum menambah lebih banyak objek eksplisit (bagian 4)?
5. Untuk arena combat, apakah bentuk ruang sudah disesuaikan dengan FSM musuh yang akan ditempatkan di sana (bagian 5)?

---

*Dokumen ke-25 dari paket dokumentasi pra-produksi Lentera Pudar — pelengkap Game_Design_Systems_Expert.md (pacing waktu) dan Story_Bible_Lore.md/Kreativitas_Seni_Expert.md (naratif & visual), khusus untuk bagaimana ruang dan tata letak level menyampaikan cerita.*

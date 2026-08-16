---
name: player_psychology_engagement
description: Panduan psikologi pemain untuk Psychology Agent (Consultant). Digunakan saat mereview motivasi dialog NPC, atmosferik dread vs hope, resonansi emosional tragedi Kaelen & Aina, 5 Stages of Grief, dan kejelasan bahasa tubuh 3D serta kamera sinematik ala Hellblade.
---

# Player Psychology & Emotional Engagement (Psychology Agent)

Panduan konsultasi psikologi pemain untuk mengevaluasi resonansi emosional, kepuasan loop gameplay, kurva duka non-linear, dan keselarasan karakter di semesta **Lentera Pudar** — 3D Action RPG (Unreal Engine 5 + Blender 5.2 LTS) merujuk pada [expert-psychology.md](file:///d:/GodotProjects/Lentera-Pudar/references/expert-psychology.md).

---

## 1. Sifat Peran: Konsultan Kritis (Bukan Pemilik Tahap)
- Psychology Agent **BUKAN** pemilik tahap independen di pipeline linear.
- Bekerja sebagai **Reviewer/Consultant** terhadap rancangan yang SUDAH DIBUAT oleh Game Designer atau Art Director.
- Fokus: Memberikan catatan kritis dan actionable (bukan pujian kosong) terkait motivasi, dampak emosi, dan kejelasan ekspresi.

---

## 2. Tiga Pilar Resonansi Psikologis Lentera Pudar

### A. Dualitas Kehangatan vs Kehampaan (The Triad of Emotion)
- **Kehangatan (`#F4B860` 2700K)**: Merupakan metafora cinta, ingatan, dan rasa sakit perjuangan hidup. Harus terasa melegakan dan sakral setelah melewati kegelapan.
- **Dingin Pudar (`#4A6FA5`)**: Merupakan metafora mati rasa (*emotional numbness / anhedonia*). Kematian beku terasa nyaman bagi korban karena membebaskan mereka dari rasa sakit.
- **Prinsip Review**: Jangan biarkan dunia terasa 100% dingin atau 100% hangat. Kekuatan game ada pada **kontras eksistensial** saat syal Aina menerangi air mata beku para korban di kegelapan dungeon.

### B. Hubungan Emosional Kaelen & Aina (*The Fading Scarf Dilemma*)
- Aina adalah jiwa di balik syal lentera kuning yang perlahan menipis setiap kali Kaelen menyalakan altar distrik dungeon.
- **Review Dialog & Momen**: Pastikan interaksi Aina terasa halus, penuh kasih, dan tidak klise. Aina tidak pernah memarahi Kaelen, ia adalah sauh yang menahan Kaelen agar tidak mati rasa.

### C. Kurva Duka 5 Sektor (*The 5 Stages of Grief Review*)
Saat mereview rancangan bos dan narasi per sektor dungeon, pastikan motivasi mereka mencerminkan tahapan psikologisnya:
1. **Sektor 1 (Denial)**: Dialog dan perilaku bos mencerminkan penolakan realitas.
2. **Sektor 2 (Anger)**: Pola serangan agresif melukai diri sendiri, dialog meledak-ledak.
3. **Sektor 3 (Bargaining)**: Taktik manipulatif, menawarkan ilusi dan tawar-menawar palsu.
4. **Sektor 4 (Depression)**: Kesunyian total, dialog membujuk pemain untuk menyerah dan tidur.
5. **Sektor 5 (Acceptance)**: Keberanian untuk melepaskan, berdamai dengan luka, dan menyongsong fajar baru.

---

## 3. Diagnostik Desain Lanjutan (Self-Determination Theory & Loss Aversion)

### A. 3 Kebutuhan Dasar SDT (Autonomy, Competence, Relatedness)
- **Autonomy**: Pastikan pilihan rute via Eyepatch dan strategi bertarung adalah pilihan nyata, bukan kosmetik.
- **Competence**: Kepuasan berasal dari penguasaan parry 12-frame dan pola musuh yang adil.
- **Relatedness**: Hubungan Kaelen-Aina terbangun lewat ketergantungan gameplay nyata.
- **Anti-Crowding Out**: Tolak sistem leaderboard/skor angka yang merusak motivasi intrinsik kontemplatif.

### B. Prospect Theory & Loss Aversion 2.5x
- Kerugian dirasakan **2.0–2.5x lebih berat** dibanding keuntungan bernilai setara ($V(\text{Loss}) \approx 2.25 \times V(\text{Gain})$).
- Konsekuensi pemendekan fisik Syal Aina wajib diperlihatkan sebelum pemain mengonfirmasi aktivasi Altar Duka.

### C. Emotional Bandwidth & Pacing Anti-Burnout
- Sisipkan *Breather Rooms* dan jeda hening di antara beat emosional berat untuk mencegah kelelahan afektif (*emotional burnout*).

### D. Dinamika Duka Non-Linear (Kübler-Ross Echoes)
- Izinkan gema halus dari sektor sebelumnya (misal bisikan penolakan S1 di kedalaman S4) untuk mencerminkan proses berduka yang realistis.

---

## 4. Evaluasi Bahasa Tubuh & Ekspresi 3D (Hellblade-Grade Cinematics & Kinesiologi)

Dalam 3D Third-Person (Unreal Engine 5), emosi disampaikan lewat animasi biomekanik, kamera intim, dan audio spasial:
- **Postur Tubuh per Sektor Duka (Grief Body Language Archetypes)**:
  - *Sektor 1 & 2 (Denial & Anger)*: Postur tegap, bahu terbuka defensif, langkah kaki tegas, kuda-kuda kokoh.
  - *Sektor 4 (Depression — Abyss of Stillness)*: Postur menunduk, bahu merosot ke depan (*kyphotic posture*), langkah melambat, kepala tertunduk lesu (mengurangi vertikal bobbing).
  - *Sektor 5 (Acceptance — Dawning Altar)*: Postur tegap rileks, bahu terbuka damai, tatapan mata stabil menyongsong fajar.
  - *Pose Idle Alami*: Mengadopsi *Contrapposto* (berat badan bertumpu lebih besar pada satu kaki) agar tidak kaku seperti manekin.
- **Kutukan Mengambil Alih**: Lengan kiri es merambat dari siku ke bahu ke dada, emissive kristal berdenyut 0.8–1.2 Hz saat Curse Meter 61–90%, intensitas meningkat ke 2.0–3.0 Hz saat Surge.
- **Penutup Mata Kanan (*Eyepatch*)**: Simbol *grieving blindspot* (mata trauma yang disegel). Saat dibuka sesaat, post-process filter dingin mengubah persepsi visual dunia. Binaural whispers meningkat intensitasnya (+3 pts/detik pada Curse Meter).
- **Momen Kamera Intim (Hellblade II Style)**: Saat Altar Duka menyala dan syal Aina memendek, kamera otomatis blur ke close-up wajah Kaelen (FOV 35°–50°, jarak 1.2–1.8m) — rekam ekspresi grief non-verbal untuk dampak emosional maksimal.

---

## 5. Referensi Dokumen
- [references/expert-psychology.md](file:///d:/GodotProjects/Lentera-Pudar/references/expert-psychology.md) — Master Psikologi Pemain Tingkat Lanjut.
- [references/anatomy-kinesiology.md](file:///d:/GodotProjects/Lentera-Pudar/references/anatomy-kinesiology.md) — Master Anatomi, Kinesiologi & Postur Emosional.
- [references/game-design-document.md](file:///d:/GodotProjects/Lentera-Pudar/references/game-design-document.md) — Bab III (Kaelen & Aina), Bab VII (Psikologi Auditori), Bab VIII (5 Boss Manifestation).
- [references/style-guide.md](file:///d:/GodotProjects/Lentera-Pudar/references/style-guide.md) — Bab 7 (Parameter Kamera 3D), Bab 8 (Timing Combat), Bab 9 (Curse Meter).
- [references/creative-vision.md](file:///d:/GodotProjects/Lentera-Pudar/references/creative-vision.md) — Pedoman diksi dialog & nada narasi.

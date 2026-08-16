# Playtesting & Validasi Emosional — Lentera Pudar
### Bagaimana Mengukur Apakah Grief-nya Benar-Benar "Kena" (Pelengkap QA_QC_Framework)

`QA_QC_Framework.md` menjawab pertanyaan **"apakah ini berfungsi dan tidak berantakan?"** — bug, konsistensi teknis, kepatuhan ke Style Guide. Dokumen ini menjawab pertanyaan yang berbeda dan sama pentingnya: **"apakah dampak emosionalnya benar-benar tersampaikan ke pemain lain, bukan cuma terasa kuat buat saya sendiri?"** Ini gap yang krusial untuk game bertema grief, karena pembuat game selalu terlalu dekat dengan materinya untuk menilai objektif — sesuatu yang terasa jelas dan menyentuh buat kamu (karena tahu semua konteks/lore) bisa jadi datar atau membingungkan buat pemain yang baru pertama kali mengalaminya.

---

## 1. Kenapa Playtesting Emosional Berbeda dari Playtesting Fungsional

Playtesting fungsional biasa (dipakai di QA_QC_Framework) bertanya: *"apakah pemain bisa menyelesaikan level ini tanpa bug/softlock?"* Playtesting emosional bertanya hal yang jauh lebih rapuh dan subjektif: *"apakah pemain merasakan sesuatu, dan apakah yang dirasakan itu sesuai maksud desain?"*

Konsekuensi metodologisnya:
- Data kuantitatif (waktu penyelesaian, jumlah kematian) tidak cukup — perlu data kualitatif (reaksi verbal/non-verbal, jawaban open-ended).
- Pemain sering tidak sadar *kenapa* mereka merasakan sesuatu — pertanyaan harus digali lewat observasi perilaku, bukan cuma tanya langsung "apa yang kamu rasakan?" (jawabannya sering tidak akurat/terlalu general).
- Sampel kecil (3-5 orang) sudah cukup bermakna untuk validasi emosional kualitatif — berbeda dari playtesting balancing yang butuh sampel lebih besar untuk data statistik.

---

## 2. Kerangka "Intended vs Perceived Emotion"

Untuk tiap momen kunci (terutama transisi antar sektor grief), buat dua kolom sebelum playtest:

| Kolom | Isi |
|---|---|
| **Intended Emotion** | Emosi yang *dirancang* untuk dirasakan pemain di momen ini (ditentukan lewat referensi Story Bible + Style Guide) |
| **Design Signals** | Elemen konkret yang dipakai untuk membangun emosi itu — pencahayaan, musik, ekspresi wajah (AU spesifik), layout ruang (rujuk Level_Design_Environmental_Storytelling) |

Setelah playtest, isi kolom ketiga:

| Kolom | Isi |
|---|---|
| **Perceived Emotion** | Emosi yang benar-benar dilaporkan/teramati dari playtester, tanpa diarahkan |

**Gap antara Intended dan Perceived** itulah yang jadi bahan revisi — bukan skor rata-rata "seberapa bagus", tapi *arah* kesenjangannya (misal intended = Depression yang berat, tapi perceived = "membosankan/lambat" — ini menandakan pacing terlalu lambat tanpa cukup detail visual untuk menahan minat, bukan berarti temanya salah).

---

## 3. Teknik Observasi Non-Intrusif

- **Think-Aloud Protocol yang Diminimalkan**: minta playtester bicara sesekali, bukan terus-menerus — narasi verbal berlebihan justru mengganggu proses emosional yang biasanya nonverbal (beda dari playtesting UX standar yang justru mendorong think-aloud penuh).
- **Observasi Bahasa Tubuh**: perhatikan posisi duduk (condong maju = engaged, bersandar = detached), ekspresi wajah playtester sendiri, jeda hening yang tidak canggung (biasanya tanda momen "kena") vs jeda hening yang gelisah (tanda bingung/bosan).
- **Post-Session Interview, Bukan Mid-Session**: pertanyaan reflektif ("bagian mana yang paling nempel?", "ada momen yang terasa lain dari biasanya?") ditanyakan *setelah* sesi selesai, supaya tidak memutus immersion selama bermain — kontras dengan playtesting fungsional yang sering menanyakan feedback real-time.
- **Retensi Memori sebagai Sinyal**: seminggu setelah sesi, tanyakan ulang "bagian mana yang masih kamu ingat?" — momen yang benar-benar berdampak emosional cenderung tetap diingat lebih lama dibanding momen yang cuma "fungsional".

---

## 4. Sinyal Konkret per Tahap Grief (Apa yang Dicari Saat Observasi)

Menyambung ke pemetaan spasial di Level_Design_Environmental_Storytelling dan ekspresi di Ekspresi_Wajah_Manusia:

- **Denial** — berhasil kalau playtester sempat bingung/menduga "ini bug atau memang disengaja?" sebelum sadar itu representasi penyangkalan. Kalau playtester langsung sadar itu simbolis tanpa keraguan sama sekali, efeknya kemungkinan terlalu eksplisit/kurang halus.
- **Anger** — berhasil kalau ritme input playtester (kecepatan menekan tombol, agresivitas gerakan kamera) terasa ikut meningkat, bukan cuma karakter di layar yang terlihat marah.
- **Depression** — berhasil kalau ada jeda diam yang natural dari playtester (bukan karena bingung mekanik, tapi karena "meresapi") — ini area paling rawan disalahartikan sebagai "game-nya lambat/membosankan", jadi butuh follow-up interview untuk membedakan dua hal itu.
- **Acceptance** — berhasil kalau ada perubahan nada suara/postur ke arah lebih tenang saat wawancara pasca-sesi tentang bagian ini, dibanding nada saat membahas bagian Anger.

---

## 5. Menangani Bias — Termasuk Bias dari AI Agent Sendiri

- **Jangan playtest ke orang yang sudah tahu lore lengkap** — termasuk siapa pun yang sudah membaca Story_Bible_Lore.md secara detail. Playtester ideal untuk validasi emosional adalah yang *baru* terpapar cerita, sama seperti pemain asli nanti.
- **AI agent tidak bisa menggantikan playtest manusia untuk validasi ini** — AI (termasuk saat mengevaluasi lewat Visual Self-Review Loop) bisa cek konsistensi teknis dan kepatuhan ke spesifikasi desain (AU yang benar, layout yang sesuai), tapi *tidak* bisa memvalidasi apakah efeknya benar-benar mengena secara emosional ke manusia sungguhan — ini batas eksplisit yang perlu diketahui agent supaya tidak menganggap "sudah sesuai spesifikasi teknis" sama dengan "sudah divalidasi emosinya".
- **Waspadai leading question**: hindari pertanyaan seperti "apakah kamu merasa sedih di bagian ini?" (menanamkan jawaban) — gunakan pertanyaan terbuka seperti "ceritakan apa yang kamu rasakan di bagian itu" atau tidak bertanya sama sekali dan murni observasi.

---

## 6. Struktur Sesi Playtest yang Disarankan

1. **Briefing minimal** — jangan jelaskan tema grief di depan; biarkan pemain menemukan sendiri, sama seperti pemain asli nanti.
2. **Sesi bermain tanpa interupsi** — 30-45 menit, cakup minimal satu transisi antar sektor grief penuh.
3. **Cooling-off period singkat** — beberapa menit jeda sebelum wawancara, supaya respons emosional tidak tercampur dengan "mode analitis" yang muncul begitu sesi selesai.
4. **Wawancara reflektif terbuka** — pertanyaan umum dulu ("bagaimana perasaanmu secara keseluruhan?"), baru mengerucut ke momen spesifik kalau perlu.
5. **Follow-up seminggu kemudian** (opsional tapi sangat berharga) — cek retensi memori sesuai bagian 3.

---

## 7. Checklist Integrasi ke Visual Self-Review Loop

Poin tambahan untuk `Lentera_Pudar_AI_Automation_Visual_SelfReview_Protocol.md` — dengan catatan penting: checklist ini untuk **persiapan** playtest, bukan pengganti playtest itu sendiri (lihat batasan di bagian 5):

1. Apakah tabel Intended Emotion + Design Signals sudah diisi untuk momen kunci sebelum playtest dilakukan (bagian 2)?
2. Apakah sinyal desain yang dipakai (AU wajah, layout ruang, musik) sudah konsisten dengan tahap grief yang dituju, sebagai baseline sebelum divalidasi manusia (bagian 4)?
3. Apakah agent secara eksplisit menandai "butuh validasi manusia" untuk momen naratif kunci, alih-alih menganggap kepatuhan teknis sudah cukup (bagian 5)?

---

*Dokumen ke-26 dari paket dokumentasi pra-produksi Lentera Pudar — pelengkap QA_QC_Framework.md (kualitas teknis), khusus untuk metodologi memvalidasi dampak emosional ke pemain sungguhan.*

# Dokumen 31 — NPC Ambient & Kehidupan Lingkungan (Ambient World Life)

**Proyek:** Lentera Pudar
**Kategori:** Fondasi & Lore / Game Design
**Status:** Melengkapi gap "kehidupan netral/ambient" — pelengkap dari Level_Design_Environmental_Storytelling (ruang) dan Desain_Musuh (ancaman)

---

## 0. Prinsip Dasar

Selama ini dunia Lentera Pudar sudah punya tiga lapisan yang kuat: karakter utama (Kaelen, Aina) yang hidup lewat ekspresi dan vokal, musuh yang hidup lewat perilaku sebagai manifestasi grief, dan ruang yang bercerita lewat susunan diam. Yang belum ada adalah lapisan keempat: **kehidupan yang tidak menunggu pemain untuk punya arti.**

Dunia yang hampa adalah dunia yang berhenti bergerak begitu kamera tidak mengarah ke sana. Dunia yang hidup terus berjalan — entah pemain melihatnya atau tidak — dan bereaksi pelan-pelan terhadap kehadiran serta jejak pemain. Prinsip ini penting khususnya untuk tema grief: rasa kehilangan terasa lebih nyata kalau dunia di sekitarnya tampak biasa saja, terus berjalan, sementara karakter utama membawa beban yang tidak dibawa dunia itu. Kontras antara "dunia yang netral/terus hidup" dan "batin Kaelen yang berat" adalah alat naratif, bukan sekadar dekorasi.

Tiga aturan utama yang berlaku di seluruh dokumen ini:
1. **Ambient life tidak boleh menyaingi fokus naratif utama.** Ia melengkapi suasana, bukan menarik perhatian dari momen emosional Kaelen/Aina.
2. **Semua elemen ambient tetap dipetakan ke 5 sektor grief** (Denial, Anger, Depression, Acceptance, Transisi) agar konsisten dengan seluruh dokumen lain, bukan sistem terpisah yang berdiri sendiri.
3. **Murah secara implementasi, mahal secara kesan.** Ambient life idealnya dibangun dari variasi kecil dan pengulangan pintar, bukan sistem AI kompleks — fokusnya adalah *ilusi* kehidupan, bukan simulasi penuh.

---

## 1. NPC Ambient Behavior & Believability

NPC latar (bila ada di suatu sektor) tidak boleh berdiri diam menunggu trigger dialog. Mereka butuh **rutinitas minimal** yang membuat mereka tampak punya urusan sendiri, terlepas dari keberadaan pemain.

**Lapisan perilaku dasar (idle behavior):**
- Setiap NPC ambient punya 2–3 idle action sederhana yang berulang dengan variasi timing acak (menunduk, menyentuh sesuatu di dekatnya, menoleh) — bukan animasi loop tunggal yang terasa robotik.
- NPC tidak berhenti total saat pemain masuk frame; transisi ke "aware state" harus halus (menoleh dulu, baru bereaksi), bukan langsung snap ke pose baru.

**Reaksi ke kehadiran pemain (tanpa dialog penuh):**
- Kontak mata singkat lalu memalingkan wajah — cukup untuk memberi kesan "menyadari", tanpa membutuhkan sistem dialog.
- Reaksi berskala kecil ke sektor grief: NPC di sektor Anger lebih waspada/menjauh sedikit saat Kaelen mendekat; NPC di sektor Acceptance lebih tenang, kontak mata lebih lama.
- NPC tidak pernah bereaksi ekstrem berlebihan (kaget dramatis, lari) kecuali memang dirancang jadi momen naratif khusus — reaksi ambient harus tetap kecil dan halus.

**Believability lewat detail kecil, bukan kuantitas:**
- Lebih baik 3 NPC dengan rutinitas meyakinkan daripada 10 NPC yang semuanya diam patung.
- Variasi pose duduk/berdiri, arah pandang yang tidak selalu ke pemain, dan jeda idle yang tidak sinkron antar-NPC (agar tidak terlihat seperti animasi yang di-clone).

---

## 2. Sistem Kehidupan Lingkungan (Ambient World Life)

Ini lapisan non-NPC — elemen kecil yang membuat dunia terasa bernapas walau tidak ada karakter di layar.

**Satwa/makhluk kecil ambient:**
- Burung, serangga, atau makhluk kecil khas dunia Lentera Pudar yang bergerak di latar (terbang, hinggap, menghindar) — tidak interaktif, murni suasana.
- Perilaku dipetakan ke sektor grief: di **Anger**, makhluk kecil menghindar/kabur saat Kaelen mendekat (dunia terasa waspada terhadap amarahnya); di **Acceptance**, makhluk kecil lebih berani mendekat atau tidak terganggu (dunia terasa berdamai dengannya).
- Di **Denial**, variannya bisa berupa makhluk yang bergerak dalam pola berulang/tidak logis — echo dari kondisi psikologis sektor ini.

**Reaksi vegetasi & elemen pasif terhadap kehadiran Kaelen:**
- Bukan interaksi gameplay (tidak perlu physics penuh), cukup isyarat visual: rumput yang tertekan pelan, daun yang bergoyang lebih intens di sektor tertentu, partikel debu/kabut yang bereaksi ke gerakan.
- Cuaca/atmosfer ambient (kabut, angin, cahaya berkedip) sudah mungkin disinggung di Level Design — dokumen ini menambahkan lapisan bahwa perubahan itu bisa juga dipicu halus oleh kehadiran/gerakan Kaelen, bukan cuma statis per-zona.

**Siklus waktu (jika relevan dengan struktur game):**
- Kalau game tidak punya siklus siang-malam penuh, cukup gunakan variasi pencahayaan ambient per sektor sebagai pengganti — prinsip yang sama (dunia terasa berjalan) tetap tercapai tanpa sistem waktu kompleks.

---

## 3. Reactivity ke Player — World Awareness

Dunia yang hidup juga berarti dunia yang **mengingat**. Tanpa ini, tindakan pemain terasa tidak berbekas — reruntuhan yang dihancurkan kembali utuh, jejak yang ditinggalkan hilang begitu area di-reload.

**Prinsip dasar persistensi lokal:**
- Perubahan kecil yang dibuat pemain di suatu area (objek yang dipindah/dihancurkan, jejak yang ditinggalkan) sebaiknya tetap ada selama sesi berjalan, minimal dalam radius/zona yang sama.
- Tidak perlu sistem persistensi dunia penuh (yang mahal secara implementasi) — cukup persistensi per-scene/per-sektor yang pemain kunjungi ulang.

**Bentuk konkret world awareness:**
- Reruntuhan tetap hancur, bukan reset diam-diam saat pemain kembali ke area yang sama.
- NPC ambient (kalau relevan) bisa punya memori sangat sederhana: menghindar dari area yang sebelumnya jadi lokasi insiden dengan pemain.
- Jejak fisik (bekas langkah di salju/abu, misalnya) bertahan beberapa saat sebagai isyarat "pemain baru saja lewat sini" — bukan estetika kosong, tapi cara dunia mengonfirmasi keberadaan Kaelen.

**Batasan penting:**
- World awareness di sini murni untuk *believability*, bukan sistem konsekuensi naratif besar (itu ranah narrative branching, yang sudah disebut sebagai area terpisah dan lebih teknis). Jangan campur adukkan dua hal ini — dokumen ini fokus ke kesan "dunia sadar", bukan cabang cerita.

---

## 4. Secondary/Side Character

Kalau lore memuat karakter pendukung di luar Kaelen dan Aina, kehadiran mereka — meski singkat — tetap perlu terasa berarti.

**Prinsip kehadiran singkat yang berbekas:**
- Side character tidak butuh arc penuh, tapi butuh **satu detail spesifik** yang membuat mereka diingat (satu kalimat khas, satu kebiasaan visual, satu koneksi kecil ke tema grief).
- Hindari side character yang murni fungsional (pemberi informasi/quest) tanpa jejak emosional apa pun — ini yang membuat dunia terasa seperti kumpulan NPC generik, bukan dunia yang koheren dengan tema.

**Pemetaan opsional ke sektor grief:**
- Kalau side character muncul di sektor tertentu, perilaku dan cara bicara mereka bisa mencerminkan fase grief sektor tersebut — bukan meniru Kaelen, tapi sebagai variasi lain dari bagaimana seseorang/sesuatu merespons kehilangan.
- Ini memperkuat tema tanpa menambah beban naratif utama: side character jadi cermin kecil, bukan subplot besar.

---

## 5. Batasan & Prioritas Implementasi

- Ambient life dirancang untuk **murah secara teknis**: idle animation sederhana, variasi timing acak, dan reaksi kecil sudah cukup — hindari mendesain sistem AI/behavior tree kompleks untuk NPC latar yang bukan fokus cerita.
- Kalau sumber daya terbatas, prioritas urutan implementasi: **(1) NPC Ambient Behavior** → **(2) World Awareness sederhana (reruntuhan/jejak)** → **(3) Kehidupan Lingkungan (satwa/vegetasi)** → **(4) Side Character detail**. NPC dan world awareness memberi dampak believability paling besar dengan biaya paling rendah dibanding satwa ambient penuh.
- Semua elemen di dokumen ini adalah **lapisan tambahan**, bukan pengganti sistem inti — jangan sampai waktu pengembangan ambient life mengorbankan progres pada Story Bible, Level Design, atau Desain Musuh yang sudah jadi fondasi.

---

## 6. Checklist — Visual Self-Review Loop

Gunakan checklist ini saat meninjau implementasi elemen ambient di suatu sektor:

- [ ] NPC latar (jika ada) punya minimal 2 idle action dengan variasi timing, bukan animasi loop tunggal
- [ ] Reaksi NPC ke kehadiran pemain halus (menoleh dulu), bukan snap instan
- [ ] Perilaku NPC/satwa ambient di sektor ini konsisten dengan tahap grief sektor tersebut (lihat pemetaan di Bagian 1 & 2)
- [ ] Ada minimal satu bentuk world awareness aktif di area ini (jejak, reruntuhan, atau perubahan kecil yang bertahan)
- [ ] Tidak ada elemen ambient yang menarik fokus visual lebih besar dari momen naratif Kaelen/Aina
- [ ] Side character (jika ada di sektor ini) punya minimal satu detail spesifik yang membuatnya diingat
- [ ] Semua elemen baru sudah dicocokkan ke Master Index dan tidak tumpang tindih dengan cakupan Level Design atau Desain Musuh yang sudah ada

---

*Dokumen ini melengkapi paket dokumentasi Lentera Pudar menjadi 31 dokumen. Perbarui Master Index untuk mencantumkan dokumen ini di kategori Fondasi & Lore / Game Design.*

# Desain Musuh & Balancing Combat — Lentera Pudar
### Dari FSM Generik ke Archetype Bermakna (Pelengkap Referensi Teori & Level Design)

FSM dasar (Patrol → Alert → Chase → Attack) sudah ada di `Referensi_Teori_untuk_AI_Agent.md`, dan `Level_Design_Environmental_Storytelling.md` (bagian 5) sudah menetapkan bahwa bentuk arena harus menyesuaikan perilaku musuh. Dokumen ini mengisi bagian yang masih kosong di antara keduanya: **musuh macam apa** yang mengisi state machine itu, dan **bagaimana kesulitannya diatur** per encounter — supaya musuh tidak jadi sekadar obstacle generik, tapi ikut membawa makna tematik seperti elemen lain di proyek ini.

---

## 1. Prinsip Dasar: Musuh sebagai Manifestasi Grief, Bukan Sekadar Obstacle

Mengikuti pola tematik yang sudah konsisten di seluruh dokumen (level design, ekspresi wajah, semuanya dipetakan ke 5 sektor grief), musuh sebaiknya juga bukan aset generik yang bisa ditempel di level manapun. Alih-alih mendesain musuh dari sisi mekanik dulu ("musuh cepat", "musuh tank"), mulai dari pertanyaan: *representasi emosi/pikiran intrusif apa yang diwakili musuh ini?* Baru turunkan mekaniknya dari situ.

Ini konsisten dengan cara Hellblade menempatkan musuh sebagai manifestasi psikosis Senua, bukan sekadar tantangan combat generik — pendekatan yang sama bisa diterapkan tanpa meniru detail spesifiknya.

---

## 2. Archetype Musuh per Sektor Grief

| Sektor | Archetype | Filosofi Mekanik |
|---|---|---|
| **Denial** | **The Echo** — musuh yang menduplikasi diri atau meniru gerakan Kaelen sendiri | Sulit dibedakan mana yang asli — pemain harus belajar membaca *tell* (baca bagian 4) alih-alih menyerang membabi buta, mencerminkan kesulitan "melihat kenyataan dengan jelas" |
| **Anger** | **The Berserker** — musuh agresif, menyerang cepat dan tidak sabar, mudah membuka diri kalau dipancing | Reward untuk pemain yang bermain defensif/menunggu — bertentangan dengan naluri "ikut marah balik", jadi combat mengajarkan pengendalian diri lewat mekanik, bukan cuma naratif |
| **Depression** | **The Weight** — musuh lambat, berat, tapi punya HP/pertahanan tinggi dan serangan area yang sulit dihindari sepenuhnya | Melawan Weight terasa melelahkan secara sengaja (encounter lebih panjang, tempo lebih lambat) — risiko: bisa terasa "kurang seru" kalau tidak diimbangi (lihat bagian 5 soal batasan ini) |
| **Acceptance** | **The Mirror** — musuh yang menyerap/meniru pola serangan Kaelen sendiri dari encounter-encounter sebelumnya | Encounter puncak yang menguji penguasaan pemain atas semua skill yang dipelajari — melawan "diri sendiri" adalah representasi mekanik dari menerima masa lalu |

Archetype ini adalah kerangka pemetaan makna, bukan daftar musuh final — tiap archetype bisa punya beberapa varian visual/mekanik di dalamnya, sepanjang filosofi intinya tetap konsisten.

---

## 3. Kurva Kesulitan per-Encounter (Melengkapi Kurva Makro di Game Design Systems)

`Game_Design_Systems_Expert.md` sudah mendefinisikan kurva kesulitan level *seluruh game*. Di level encounter individual, prinsip yang berlaku:

- **Onboarding Encounter**: encounter pertama tiap archetype musuh baru harus dilakukan dalam kondisi aman untuk bereksperimen (ruang cukup luas untuk mundur, HP pemain tidak dalam kondisi kritis) — supaya pembelajaran pola terjadi lewat eksplorasi, bukan hukuman.
- **Escalation dalam Encounter yang Sama**: encounter panjang sebaiknya menambah kompleksitas secara bertahap (jumlah musuh, kombinasi archetype) di dalam satu encounter, bukan cuma melempar musuh lebih banyak sejak awal.
- **Combo Archetype**: begitu pemain sudah familiar dengan satu archetype, encounter lanjutan bisa mengombinasikan 2 archetype berbeda untuk menguji adaptasi (misal Echo + Berserker — pemain harus membedakan musuh asli sambil menghadapi tekanan waktu dari agresivitas Berserker).
- **Recovery Encounter**: setelah encounter combo yang berat, sisipkan encounter lebih ringan atau non-combat sebelum combo berikutnya — prinsip ini konsisten dengan "Rest Beat" di Level_Design_Environmental_Storytelling bagian 3.

---

## 4. Attack Telegraphing & Readability

Karena Style_Guide_Numerik dan referensi Hellblade menekankan combat yang fair dan readable (bukan cuma sulit), setiap archetype butuh **tell** yang jelas sebelum menyerang:

- **Windup Frame Minimum**: setiap serangan musuh harus punya fase persiapan visual yang cukup lama untuk dibaca pemain (rujuk timing frame di Style_Guide_Numerik) — kecepatan windup berbeda per archetype (Berserker lebih cepat/agresif, Weight lebih lambat tapi susah dihindari sepenuhnya sebagai trade-off).
- **Silhouette Change sebagai Tell**: perubahan bentuk siluet musuh saat bersiap menyerang (rujuk prinsip silhouette readability di Kreativitas_Seni_Expert) — bukan cuma efek partikel/VFX yang bisa terlewat di tengah chaos combat.
- **Audio Tell**: sinyal suara yang mendahului serangan (rujuk Audio_Sound_Design_Expert) — penting khususnya untuk musuh dari belakang/luar frame kamera.
- **The Echo (Denial) Khusus**: karena filosofinya soal ambiguitas, tell untuk membedakan Echo asli vs duplikat harus tetap ada dan bisa dipelajari (misal delay minor, detail visual konsisten) — ambiguitas itu untuk pengalaman naratif/kognitif, bukan untuk membuat combat terasa tidak adil secara mekanik.

---

## 5. Batasan Penting: Tema Emosional Tidak Boleh Mengorbankan Fun Mekanik

Ini prinsip pengaman yang perlu ditegaskan ke AI agent: musuh yang secara sengaja terasa "berat/melelahkan" (seperti The Weight untuk Depression) **berisiko tinggi dianggap playtester sebagai "kurang seru"** alih-alih "berhasil menyampaikan tema" — masalah yang sama seperti yang diperingatkan di `Playtesting_Validasi_Emosional.md` bagian 4 soal pacing lambat.

Solusinya bukan menghilangkan filosofi tematiknya, tapi memastikan tetap ada **satisfaction mekanik dasar** yang tidak dikompromikan demi tema — hit-feedback yang solid (rujuk Fisika_Expert untuk fisika reruntuhan/impact), kontrol yang responsif, dan kemenangan yang terasa well-earned. Tema grief harus mewarnai *bagaimana* combat terasa, bukan membuat combat itu sendiri jadi kurang memuaskan untuk dimainkan.

---

## 6. Checklist Integrasi ke Visual Self-Review Loop

Poin tambahan untuk `Lentera_Pudar_AI_Automation_Visual_SelfReview_Protocol.md`:

1. Apakah musuh yang didesain punya filosofi tematik yang jelas (archetype grief mana yang diwakili), bukan sekadar variasi mekanik acak (bagian 1-2)?
2. Apakah setiap serangan musuh punya tell yang cukup readable — windup, silhouette, atau audio (bagian 4)?
3. Untuk encounter dengan archetype "berat/melelahkan" secara sengaja (seperti The Weight), apakah satisfaction mekanik dasarnya tetap terjaga, atau perlu ditandai untuk pengecekan khusus di playtest (bagian 5)?
4. Apakah kurva kesulitan encounter mengikuti pola onboarding → escalation → recovery, bukan melempar kompleksitas penuh sejak awal (bagian 3)?

---

*Dokumen ke-27 dari paket dokumentasi pra-produksi Lentera Pudar — pelengkap Referensi_Teori_untuk_AI_Agent.md (FSM dasar) dan Game_Design_Systems_Expert.md (kurva kesulitan makro), khusus untuk archetype musuh dan balancing combat per-encounter.*

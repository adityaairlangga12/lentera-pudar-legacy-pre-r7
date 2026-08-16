# Arahan Vokal & Delivery Dialog — Lentera Pudar
### Menyambungkan Lore dan Ekspresi Wajah ke Suara (Pelengkap Story Bible & Ekspresi Wajah Manusia)

`Story_Bible_Lore.md` menetapkan *apa* yang dikatakan karakter dan *siapa* mereka. `Ekspresi_Wajah_Manusia.md` menetapkan *bagaimana wajah bergerak* saat mereka bicara. Dokumen ini mengisi jembatan yang masih kosong: **bagaimana line itu harus diucapkan** secara vokal — supaya delivery suara dan ekspresi wajah bergerak selaras, bukan dua elemen yang dikerjakan terpisah lalu digabung belakangan dan terasa tidak sinkron.

---

## 1. Prinsip Dasar: Subteks di Atas Teks

Line dialog yang sama bisa berarti sangat berbeda tergantung *apa yang tidak dikatakan* di baliknya. Untuk tema grief, sebagian besar momen kunci justru dialog yang paling kuat ketika kata-katanya sederhana tapi subteksnya berat — bukan dialog panjang yang menjelaskan semua perasaan secara eksplisit.

Sebelum menulis arahan vokal untuk sebuah line, tentukan dulu:
- **Apa yang dikatakan** (teks literal)
- **Apa yang sebenarnya dirasakan** (subteks — biasanya berbeda dari teks)
- **Apa yang sedang ditahan/tidak dikatakan** (khususnya relevan untuk Denial dan Depression)

Arahan vokal aktor seharusnya berangkat dari subteks, bukan teks — instruksi seperti "ucapkan dengan sedih" kalah presisi dibanding "katakan ini seolah kamu masih berusaha meyakinkan diri sendiri bahwa semua baik-baik saja" (Denial), meski teksnya sama.

---

## 2. Karakteristik Vokal per Sektor Grief

| Sektor | Tempo & Ritme | Pitch & Volume | Napas |
|---|---|---|---|
| **Denial** | Tempo cenderung normal/terlalu stabil — kestabilan yang terasa dipaksakan | Pitch datar, volume terkontrol, sedikit variasi | Napas teratur, kadang tertahan sebelum kalimat yang menyentuh topik sensitif |
| **Anger** | Tempo cepat, kalimat terpotong-potong atau overlapping | Pitch naik, volume meningkat tidak merata (meledak lalu turun tiba-tiba) | Napas pendek dan berat, terdengar di antara kalimat |
| **Depression** | Tempo melambat signifikan, jeda antar kalimat memanjang | Pitch rendah dan datar, volume cenderung pelan | Napas berat/dalam sebelum bicara, seolah butuh usaha ekstra untuk mengeluarkan tiap kalimat |
| **Acceptance** | Tempo kembali stabil tapi lebih natural (tidak dipaksakan seperti Denial) | Pitch lebih variatif secara wajar, volume cenderung tenang | Napas lebih lega, tidak tertahan |

**Perbedaan kunci Denial vs Acceptance**: keduanya sama-sama "tenang" secara permukaan, tapi Denial tenang karena *menahan*, sedangkan Acceptance tenang karena *melepaskan* — aktor dan AI agent yang menulis arahan harus eksplisit membedakan dua jenis "tenang" ini, karena kalau tidak dibedakan dengan jelas, delivery-nya akan terdengar sama padahal maknanya berlawanan.

---

## 3. Sinkronisasi Vokal dengan AU Wajah (Menyambung Ekspresi_Wajah_Manusia)

- **Micro-pause Bertepatan dengan Micro-expression**: jeda kecil dalam delivery vokal (bagian 5, Ekspresi_Wajah_Manusia) sebaiknya bertepatan dengan momen micro-expression singkat di wajah — sinkronisasi ini yang membuat penonton merasakan "sesuatu terjadi" tanpa perlu dijelaskan verbal.
- **Volume Turun saat AU17 (Chin Raiser/Menahan Tangis) Aktif**: ketika arahan wajah menunjukkan otot dagu mengencang (menahan emosi), delivery vokal sebaiknya ikut menunjukkan suara tercekat/tertahan — bukan tetap lancar seolah wajah dan suara adalah dua channel independen.
- **Gaze Aversion Menyertai Delivery Tidak Yakin**: saat arahan gaze (Ekspresi_Wajah_Manusia bagian 7) menunjukkan menghindari kontak mata, delivery vokal sebaiknya juga sedikit kehilangan proyeksi/kepercayaan diri — dua elemen ini harus dirancang bersamaan sejak tahap penulisan arahan, bukan diperbaiki belakangan saat sudah tidak sinkron.

---

## 4. Silence dan Non-Verbal Vocalization

Menyambung prinsip silence dari Audio_Sound_Design_Expert:

- **Silence Bermakna vs Silence Kosong**: jeda tanpa dialog hanya efektif kalau didukung elemen lain (ekspresi, napas, ambient audio) yang mengisi ruang itu dengan makna — silence yang benar-benar kosong secara audio-visual justru terasa seperti bug/loading, bukan momen dramatis.
- **Non-verbal Vocalization sebagai Alat Naratif**: helaan napas, suara tertahan, tawa pahit singkat — elemen non-verbal ini sering lebih jujur secara emosional dibanding dialog penuh, terutama untuk momen Denial (karakter belum siap bicara langsung) dan Depression (energi untuk bicara panjang terasa berat).
- **Overlap Dialog untuk Anger**: di momen konflik/Anger, dialog dua karakter yang saling menyela (overlapping, bukan bergantian rapi) menambah rasa urgensi dan ketidaksabaran secara natural.

---

## 5. Panduan Arahan untuk Voice Actor (Format Praktis)

Format arahan per-line yang disarankan, supaya konsisten dan actionable untuk voice director:

```
LINE: [teks dialog]
SEKTOR GRIEF: [Denial/Anger/Depression/Acceptance]
SUBTEKS: [apa yang benar-benar dirasakan, bukan teks literal]
TEMPO: [rujuk tabel bagian 2]
CATATAN FISIK: [napas, jeda, AU wajah yang harus disinkronkan — rujuk bagian 3]
REFERENSI TONAL (opsional): [deskripsi kualitatif, bukan quote dari sumber berhak cipta]
```

Format ini memastikan tiap line dievaluasi lewat kerangka yang sama, dan memudahkan cross-check ke dokumen Ekspresi_Wajah_Manusia serta Story_Bible_Lore sebelum rekaman final dilakukan.

---

## 6. Checklist Integrasi ke Visual Self-Review Loop

Poin tambahan untuk `Lentera_Pudar_AI_Automation_Visual_SelfReview_Protocol.md`:

1. Apakah arahan vokal untuk tiap line sudah dimulai dari subteks, bukan langsung dari teks literal (bagian 1)?
2. Apakah karakteristik tempo/pitch/napas sudah sesuai sektor grief yang dituju, dan sudah membedakan "tenang karena menahan" (Denial) dari "tenang karena melepaskan" (Acceptance) (bagian 2)?
3. Apakah micro-pause vokal dan momen AU wajah kunci sudah direncanakan bersamaan, bukan disinkronkan belakangan (bagian 3)?
4. Apakah ada momen silence/non-verbal yang dipertimbangkan sebagai alternatif sebelum menambah dialog eksplisit (bagian 4)?

---

*Dokumen ke-29 dari paket dokumentasi pra-produksi Lentera Pudar — pelengkap Story_Bible_Lore.md (isi dialog) dan Ekspresi_Wajah_Manusia.md (ekspresi visual), khusus untuk arahan vokal dan delivery dialog yang selaras dengan keduanya.*

# Anatomi Manusia & Kinesiologi — Lentera Pudar
### Referensi Lengkap untuk Sculpting, Rigging, dan Animasi Karakter (Blender + UE5)

Dokumen ini melengkapi Teori bagian 9 (Animasi) dan 10 (Rigging & Cloth) dengan detail anatomi dan ilmu gerak (kinesiologi) yang lebih dalam — dasar teknis di balik *kenapa* pose/gerakan tertentu terlihat "benar" secara natural, bukan cuma prinsip animasi permukaan.

---

## 1. Proporsi Dasar & Kanon Tubuh

Sebelum masuk ke gerak, proporsi tubuh jadi fondasi konsistensi sculpting/rigging semua karakter.

| Standar | Kaelen (dewasa, atletis) | Catatan |
|---|---|---|
| Tinggi total | 7.5–8 kepala | Standar proporsi heroik/atletis (bukan 6-7 kepala yang lebih stylized-pendek ala kartun) |
| Lebar bahu | ~2 lebar kepala | Untuk build tubuh "pengelana" yang ramping tapi terlatih |
| Titik tengah tubuh (midpoint) | Di area pangkal paha (hip) | Acuan simetri atas-bawah tubuh |
| Panjang lengan | Ujung jari mencapai pertengahan paha saat berdiri rileks | Acuan cepat validasi proporsi lengan |
| Panjang kaki | Sekitar setengah dari tinggi total | Dari hip ke telapak kaki |

**Catatan penting untuk gaya stylized-realistic (Kena)**: proporsi ini adalah baseline realistis — Kena sendiri sedikit menstilasi (kepala/mata cenderung sedikit lebih besar dari rasio realistis murni). Pertimbangkan penyesuaian 5-10% ke arah stilasi ringan untuk Kaelen/Aina, bukan proporsi 100% anatomis akademis, supaya konsisten dengan Style Guide bagian artstyle.

---

## 2. Titik Rujukan Tulang (Bony Landmarks) — Wajib untuk Sculpting & Weight Painting

Ini titik-titik tulang yang **selalu terlihat/teraba** di permukaan tubuh manusia berapa pun berat badannya — jadi acuan paling stabil untuk menjaga akurasi bentuk saat sculpting maupun menempatkan bone saat rigging.

| Area | Landmark | Fungsi Praktis |
|---|---|---|
| Bahu | Acromion (ujung tulang belikat), Clavicle (tulang selangka) | Acuan penempatan bone bahu, batas atas deltoid |
| Siku | Olecranon (tonjolan siku) | Titik pivot elbow bend, area rawan self-intersection saat weight painting |
| Pinggang/Panggul | Iliac Crest (puncak tulang panggul), Greater Trochanter (tonjolan sisi paha atas) | Acuan lebar pinggul, titik pivot rotasi hip |
| Lutut | Patella (tempurung lutut) | Titik pivot knee bend, referensi visual saat menekuk |
| Pergelangan Kaki | Medial & Lateral Malleolus (mata kaki dalam-luar) | Acuan lebar pergelangan kaki, batas bawah rig kaki |
| Pergelangan Tangan | Radius & Ulna styloid process | Acuan rotasi lengan bawah (pronasi/supinasi) |
| Tulang Belakang | Vertebra prominens (tulang menonjol di pangkal leher) | Titik referensi postur & kurva tulang belakang |

**Aplikasi praktis di Blender**: saat sculpting, landmark ini HARUS tetap terlihat sebagai sedikit tonjolan/lekukan di mesh meski karakter berotot/berpakaian tebal — kalau landmark ini "hilang" di sculpt, biasanya tanda proporsi sudah melenceng dari anatomi dasar.

---

## 3. Rantai Kinetik & Transfer Berat (Kinetic Chain) — Untuk Combat Kaelen

Ini prinsip paling penting untuk membuat pukulan/serangan Kaelen terasa **bertenaga**, bukan cuma lengan yang bergerak sendiri.

### A. Konsep Dasar Kinetic Chain
Tenaga sebuah pukulan tidak berasal dari otot lengan saja — ia adalah **rantai transfer momentum** dari tanah ke titik impact:

```
Telapak kaki belakang menjejak tanah (ground reaction force)
        ↓
Rotasi pergelangan kaki & lutut
        ↓
Rotasi panggul (pelvic rotation) — sumber tenaga terbesar
        ↓
Torsi tulang belakang (thoracic-lumbar rotation)
        ↓
Protraction scapula (bahu terdorong maju)
        ↓
Ekstensi siku
        ↓
Pergelangan tangan mengunci tepat saat impact (wrist lock)
```

**Kesalahan umum yang harus dihindari**: animasi pukulan yang hanya menggerakkan lengan dari bahu ke bawah tanpa rotasi panggul/tulang belakang akan selalu terlihat "lemah" dan "kaku" — secara visual tidak meyakinkan meski secara teknis lengan bergerak dengan benar.

### B. Aplikasi ke Light/Heavy Attack Kaelen
- **Light Attack (jab cepat)**: rantai kinetik dipersingkat — rotasi panggul kecil, transfer cepat, fokus di kecepatan pergelangan tangan.
- **Heavy Cursed Strike**: rantai kinetik penuh — mulai dari jejak kaki belakang yang dalam, rotasi panggul besar, torsi tulang belakang maksimal — ini alasan biomekanis kenapa startup frame Heavy Strike di Style Guide (12-18 frame) jauh lebih lama dari Light Attack (3-5 frame): tubuh butuh waktu membangun momentum lewat rantai kinetik penuh.

### C. Weight Transfer (Perpindahan Berat Badan)
Saat menyerang, titik tumpu berat badan (center of gravity) berpindah dari kaki belakang ke kaki depan. Animasi yang mengabaikan ini akan terlihat "melayang" tanpa berat. Indikator visual weight transfer yang benar:
- Kaki belakang sedikit menjejak lebih dalam (heel lift, ball of foot menekan)
- Panggul bergerak maju-bawah sedikit sebelum rotasi
- Kepala tetap relatif stabil (mata sebagai titik referensi visual pemain) meski tubuh bergerak besar — prinsip "head stays level" umum di animasi combat game

---

## 4. Siklus Gerak Jalan & Lari (Human Gait Cycle)

Untuk locomotion Kaelen (blend tree di Teori bagian 9.C), berikut breakdown fase gerak manusia yang perlu direpresentasikan di keyframe/mocap cleanup.

### A. Siklus Jalan (Walk Cycle) — 8 Fase per Satu Kaki
| Fase | Deskripsi | Posisi Kunci |
|---|---|---|
| 1. Initial Contact (Heel Strike) | Tumit menyentuh tanah | Kaki depan lurus, tumit duluan menyentuh |
| 2. Loading Response | Berat mulai berpindah ke kaki ini | Lutut sedikit menekuk menyerap impact |
| 3. Midstance | Berat badan penuh di atas kaki ini | Tubuh berada tepat di atas titik tumpu, titik terendah gerak vertikal |
| 4. Terminal Stance | Tumit mulai terangkat | Dorongan mulai terbentuk, betis meregang |
| 5. Pre-Swing (Toe-off) | Jari kaki mendorong lepas dari tanah | Titik dorongan maksimal |
| 6. Initial Swing | Kaki mulai terayun ke depan | Lutut menekuk untuk clearance (menghindari tanah) |
| 7. Midswing | Kaki melewati posisi tubuh | Titik tertinggi ayunan kaki |
| 8. Terminal Swing | Kaki bersiap mendarat lagi | Lutut mulai lurus kembali, bersiap heel strike berikutnya |

### B. Elemen Penting yang Sering Terlewat di Animasi Game
- **Pelvic Tilt**: panggul tidak diam datar — miring naik-turun mengikuti fase mana kaki sedang menumpu (turun saat midstance, sedikit naik saat swing).
- **Counter-Rotation (Rotasi Berlawanan Bahu-Pinggul)**: saat panggul berputar ke satu arah, bahu/tulang belakang atas berputar sedikit ke arah berlawanan — ini yang membuat jalan manusia terlihat "hidup", bukan seperti robot yang seluruh tubuh berputar bersamaan.
- **Vertical Bob (Naik-Turun Tubuh)**: titik tertinggi tubuh di midstance, titik terendah di saat kedua kaki sejajar (double support phase) — mengabaikan ini membuat locomotion terlihat "meluncur" tanpa berat badan sungguhan.

### C. Perbedaan Kunci Walk vs Run
- **Walk**: selalu ada momen kedua kaki menyentuh tanah bersamaan (double support phase).
- **Run**: ada momen **kedua kaki melayang** di udara bersamaan (flight phase) — tidak ada di walk. Ini perbedaan biomekanis paling fundamental, bukan sekadar "walk dipercepat".
- **Dash Kaelen**: secara biomekanis lebih dekat ke sprint start — condong badan ke depan lebih ekstrem, langkah pertama lebih pendek dan cepat sebelum stride memanjang.

---

## 5. Deformasi Sendi & Corrective Shape Keys

Ini area teknis yang sering jadi sumber masalah visual di rigging (lengan/lutut "collapse" atau kehilangan volume saat menekuk ekstrem).

### A. Masalah Umum: Volume Loss
Rig dasar (skinning linear biasa) cenderung membuat mesh kehilangan volume di area sendi saat menekuk penuh (contoh: siku ditekuk 140°, area dalam siku "gepeng" tidak natural).

### B. Solusi: Corrective Shape Keys / Pose-Driven Morph
Teknik untuk mengoreksi ini di Blender:
1. Buat pose ekstrem (misal siku ditekuk penuh) dengan rig normal — akan terlihat deformasi janggal.
2. Buat **shape key** baru dari kondisi mesh yang sudah janggal itu.
3. Sculpt ulang shape key tersebut untuk memperbaiki volume (tambahkan muscle bulge di bisep, perbaiki area dalam siku).
4. Hubungkan shape key ini ke **driver** yang otomatis aktif berdasarkan sudut rotasi bone siku — sehingga koreksi otomatis muncul hanya saat siku ditekuk cukup dalam, tidak mengganggu pose lain.

### C. Muscle Bulging (Otot Menggelembung)
Saat bisep berkontraksi (siku menekuk), otot secara fisiologis memendek dan "menggembung" di tengah — kalau tidak dikoreksi, mesh siku Kaelen akan terlihat kaku seperti mainan plastik saat pose combat ekstrem. Ini terutama penting untuk pose Heavy Cursed Strike yang butuh kontraksi otot lengan terlihat jelas.

### D. Area Sendi Prioritas untuk Corrective Shape Keys di Kaelen
Berdasarkan gerakan combat yang paling sering dipakai:
1. **Siku** (elbow) — prioritas tinggi karena kombinasi Light/Heavy Attack banyak melibatkan ekstensi-fleksi siku ekstrem.
2. **Bahu** (shoulder/scapula) — penting untuk gerakan lengan terangkat tinggi (wind-up Heavy Strike).
3. **Lutut** (knee) — penting untuk pose dash/evade rendah.
4. **Pinggul** (hip) — untuk rotasi combat dan pose jongkok.

---

## 6. Anatomi Otot Permukaan (Surface Anatomy) — Referensi Ringkas untuk Sculpting

Bukan daftar lengkap otot anatomis (terlalu detail untuk kebutuhan game), tapi grup otot besar yang **terlihat mempengaruhi siluet** karakter, relevan untuk sculpting Kaelen bertubuh atletis-pengelana (bukan bodybuilder ekstrem):

| Grup Otot | Pengaruh Visual pada Siluet |
|---|---|
| Deltoid (bahu) | Bentuk bulat bahu, terutama terlihat saat lengan terangkat wind-up |
| Trapezius (leher-bahu) | Transisi leher ke bahu, penting untuk pose kepala menunduk (karakter lelah/sedih) |
| Latissimus Dorsi (punggung samping) | Bentuk "V" tubuh atletis dari belakang, terlihat saat gerakan memutar tubuh |
| Bisep & Trisep (lengan atas) | Sudah dibahas di corrective shape keys atas |
| Rectus Abdominis & Oblique (perut/pinggang) | Rotasi tulang belakang saat pukulan (bagian dari kinetic chain di atas) |
| Quadriceps & Hamstring (paha depan-belakang) | Bentuk kaki saat menekuk/melangkah, penting untuk pose kuda-kuda combat |
| Gastrocnemius (betis) | Terlihat jelas saat toe-off/push-off di walk cycle & dash |

**Catatan gaya**: karena artstyle target adalah stylized-realistic (bukan hyper-realistic ala Hellblade), otot-otot ini sebaiknya **disederhanakan bentuknya** — cukup terlihat "readable" sebagai bentuk besar yang mempengaruhi siluet, tanpa definisi otot detail berlebihan yang justru terasa terlalu realistis dan berisiko bentrok dengan gaya visual Kena (lihat Teori bagian 15.F soal uncanny valley).

---

## 7. Postur & Garis Aksi (Line of Action)

### A. Line of Action
Satu garis lengkung imajiner yang mengalir dari kepala sampai kaki, merangkum "energi" utama sebuah pose. Sebelum detail pose selesai, cek dulu apakah line of action-nya jelas dan dinamis — kalau garis ini terlihat kaku/lurus, pose kemungkinan besar terasa statis meski detailnya sudah bagus.

### B. Contrapposto (Postur Berat Sebelah)
Postur berdiri natural manusia jarang simetris sempurna — berat badan biasanya bertumpu lebih ke satu kaki, menyebabkan pinggul miring ke satu sisi dan bahu miring berlawanan sedikit untuk keseimbangan. Berguna untuk pose idle Kaelen supaya tidak terlihat kaku seperti manekin saat berdiri diam menunggu input pemain.

### C. Postur Emosional (Terkait Tema Grief)
Postur tubuh juga bisa menyiratkan kondisi psikologis tanpa dialog (selaras Teori bagian 3.B, Show Don't Tell):
- **Denial/Anger** (Sektor 1-2): postur lebih tegak, bahu terbuka, langkah lebih tegas.
- **Depression** (Sektor 4): postur menunduk, bahu turun ke depan (kyphotic posture), langkah lebih pendek dan berat — bisa dianimasikan sebagai variasi locomotion khusus sektor ini.
- **Acceptance** (Sektor 5): postur kembali terbuka tapi lebih tenang dibanding Sektor 1 (bukan sekadar mengulang pose awal — ada perbedaan kualitas "tenang" vs "tegas defensif").

---

## 8. Implikasi untuk Rigging (Batas Rotasi Sendi Realistis)

Supaya AI agent tidak membuat rig yang secara default membiarkan sendi berotasi ke sudut yang secara anatomis tidak mungkin (dan berisiko dieksploitasi jadi pose aneh saat animasi blending):

| Sendi | Rentang Rotasi Wajar (Derajat, Perkiraan) |
|---|---|
| Siku (fleksi) | 0° (lurus) sampai ~145° (tekuk penuh) — TIDAK bisa hyperextend ke arah berlawanan secara natural |
| Lutut (fleksi) | 0° sampai ~140° |
| Bahu (fleksi ke depan) | 0° sampai ~180° (bisa lurus ke atas) |
| Pinggul (fleksi) | 0° sampai ~120° (tertekuk, tergantung fleksibilitas lutut ikut menekuk atau tidak) |
| Leher (rotasi ke samping) | ±80° dari posisi netral |
| Tulang belakang (torsi total, seluruh punggung) | ±35-45° per segmen besar (thoracic+lumbar gabungan bisa sampai ~90° total tapi terdistribusi banyak vertebra) |

**Aplikasi**: set constraint limit rotation di Blender/UE5 Control Rig sesuai rentang ini untuk bone-bone utama, supaya blend animasi (terutama transisi cepat antar state combat) tidak menghasilkan pose "patah" yang secara anatomis mustahil, meski secara teknis matematika interpolasi valid.

---

## 9. Ringkasan Checklist untuk AI Agent (Self-Review Tambahan)

Tambahkan pengecekan berikut ke Visual Self-Review Loop (dokumen Protokol AI) khusus untuk task terkait karakter manusia:

- [ ] Apakah bony landmarks (bagian 2) masih terlihat jelas di sculpt, tidak "tertelan" oleh proporsi yang salah?
- [ ] Apakah animasi pukulan/serangan menunjukkan rotasi panggul & tulang belakang, bukan cuma gerak lengan (bagian 3)?
- [ ] Apakah locomotion punya pelvic tilt & counter-rotation bahu-pinggul, bukan gerak kaku seluruh tubuh berputar bersamaan (bagian 4)?
- [ ] Apakah area siku/lutut/bahu kehilangan volume saat pose ekstrem? Kalau ya, perlu corrective shape key (bagian 5)?
- [ ] Apakah line of action pose terlihat jelas dan dinamis, bukan garis lurus kaku (bagian 7)?
- [ ] Apakah rotasi sendi di animasi berada dalam rentang wajar anatomis (bagian 8), bukan melebihi batas yang terlihat "patah"?

---

*Dokumen ini melengkapi Referensi Teori (bagian 9 & 10) dan SOP Workflow (SOP 3, 5, 6) dengan detail anatomi dan kinesiologi, sebagai bagian dari paket dokumentasi pra-produksi Lentera Pudar.*

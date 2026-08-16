# Level Design & Environmental Storytelling — Lentera Pudar Master Reference
### Bagaimana Tata Ruang Spasial dan Penempatan Objek Bercerita Tanpa Kata

> **Dokumen Sumber Kebenaran Desain Level (*Level Design & Environmental Storytelling Reference*)**  
> Melengkapi [game-design-document.md](file:///d:/GodotProjects/Lentera-Pudar/references/game-design-document.md), [creative-vision.md](file:///d:/GodotProjects/Lentera-Pudar/references/creative-vision.md), dan [expert-psychology.md](file:///d:/GodotProjects/Lentera-Pudar/references/expert-psychology.md). Menjadi pedoman arsitektur level 3D grey-box (SOP 5), penataan koridor dungeon, penempatan prop naratif, dan breadcrumbing diegetik di **Unreal Engine 5 + Blender 5.2 LTS**.

---

## 1. Tiga Mekanisme Utama Environmental Storytelling
- **Static Narrative (Cerita Diam)**: Reruntuhan, altar retak, dan jejak beku kuno yang menyiratkan tragedi masa lalu tanpa penjelasan dialog/teks.
- **Emergent Narrative (Cerita dari Interaksi Gerak)**: Makna emosional yang dialami pemain saat menjelajahi ruang (misal disorientasi tersesat di koridor berulang).
- **Symbolic Environment (Ruang sebagai Metafora Psikologis)**: Bentuk geometri, skala, dan pencahayaan ruang merepresentasikan secara literal kondisi mental Kaelen dan 5 Tahapan Berduka.

---

## 2. Pemetaan Karakteristik Spasial ke 5 Sektor Duka (*5 Stages of Grief*)

| Sektor / Tahap Duka | Karakteristik Layout & Skala | Navigasi & Verticality | Elemen Spasial Kunci |
|---|---|---|---|
| **Sektor 1: Denial** (*The Silent Crypts*) | Koridor sempit, simetris kaku berulang (*oppressive claustrophobia*) | Jalur looping kembali ke titik awal tanpa disadari | Ilusi "terjebak dalam siklus penolakan", dinding makam dekat. |
| **Sektor 2: Anger** (*The Blazing Frost*) | Layout asimetris tajam, friksi tinggi, skala fluktuatif sempit-ke-luas | Jalur terputus, memaksa rute memutar yang melelahkan | Banyak objek *destructible* untuk outlet kemarahan fisik. |
| **Sektor 3: Bargaining** (*Hall of Mirrors*) | Labirin cermin waktu, persimpangan semu, ilusi optik | Pilihan bercabang dengan rute tawar-menawar palsu | Refleksi bayangan es yang menipu arah navigasi. |
| **Sektor 4: Depression** (*Abyss of Stillness*) | Ruang sangat luas namun hampa (*vast emptiness*), skala monumental dingin | Jalur menurun secara konstan (*descending verticality*) | Jarak tempuh panjang tanpa interaksi, waktu melambat. |
| **Sektor 5: Acceptance** (*Dawning Altar*) | Ruang lapang, simetris organik alami, sightlines panjang ke cakrawala | Jalur menanjak terbuka menuju gerbang Overworld | Navigasi dipandu pancaran cahaya lentera kuning 2700K. |

*Transisi Antar Sektor*: Wajib berlangsung secara halus dan bertahap (*gradual spatial blend*) di koridor transisi, bukan potongan level mendadak.

---

## 3. Level Flow, Pacing Spasial & Navigasi Diegetik
- **Linear vs Branching (SDT Autonomy)**:
  - Sektor Denial & Depression didesain lebih **Linear** (mencerminkan perasaan terperangkap tanpa kendali).
  - Sektor Anger & Acceptance memberikan **Branching Paths** (kontrol dan agensi pemain pulih seiring penerimaan takdir).
- **Diegetic Breadcrumbing (Zero UI Markers)**:
  - Arah eksplorasi dipandu oleh pendaran cahaya Syal Aina (`#F4B860`), jejak pencairan es pada lantai, dan komposisi pencahayaan chiaroscuro — dilarang menggunakan arrow atau waypoint UI buatan.
- **Rest Beats / Breathing Rooms**:
  - Menyisipkan ruang hening kontemplatif setelah arena pertarungan intens untuk menjaga *emotional bandwidth* pemain dari kelelahan afektif.

---

## 4. Penataan Prop Naratif (*Narrative Prop Placement*)
- **Rule of Intentional Wear**: Tingkat kerusakan, retakan es, dan pola lapuk pada prop wajib mencerminkan kronologi peristiwa lore di [creative-vision.md](file:///d:/GodotProjects/Lentera-Pudar/references/creative-vision.md), bukan sekadar aus acak.
- **Repetisi Motif Spasial (Visual Leitmotif)**: Menempatkan simbol atau bentuk kristal es tertentu secara konsisten sebagai pengingat memori masa lalu Kaelen dan Aina.
- **The Power of Absence (Bercerita Lewat Kekosongan)**: Memanfaatkan ruang kosong atau objek yang hilang (misal altar kosong dengan bekas tapak persembahan) untuk menyiratkan kehilangan mendalam tanpa butuh narasi verbal.

---

## 5. Arsitektur Arena Combat & Simbiosis FSM Musuh
- **Bentuk Arena vs FSM Pola Serang**:
  - *Arena Sempit / Koridor*: Disesuaikan untuk musuh tipe *Heavy Brawler / Melee Rush* (Lord Alden) agar duel parry 1v1 terasa intens dan rapat.
  - *Arena Luas Berpilar*: Disesuaikan untuk musuh tipe *Ranged Shard Caster / Teleport Stalker* (Lady Vespera) untuk pemanfaatan cover sistem.
- **Sightline Control & Anticipation**:
  - Mengontrol visual reveal musuh (foreshadowing siluet dari balik es transparan sebelum encounter) untuk membangun tensi psikologis bertahap.
- **Hazard Lingkungan Tematik**:
  - Es licin rapuh (Sektor 2) dan kabut beku penguras stamina (Sektor 4) bertindak sebagai ekstensi tema duka, bukan sekadar rintangan mekanik biasa.

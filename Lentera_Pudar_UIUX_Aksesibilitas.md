# UI/UX & Aksesibilitas — Lentera Pudar
### Dari Prinsip "Minimal HUD" ke Spesifikasi Konkret (Pelengkap Psikologi Expert)

`Psikologi_Expert.md` bagian D sudah menjelaskan **alasan psikologis** kenapa pendekatan minimal-HUD cocok untuk Lentera Pudar (mengurangi cognitive load supaya kapasitas mental pemain tersisa untuk merasakan cerita). Dokumen ini menerjemahkan prinsip itu jadi **spesifikasi konkret** — menu apa saja yang dibutuhkan, bagaimana HUD in-game disusun, dan opsi aksesibilitas apa yang perlu ada supaya tema yang sensitif (grief, kehilangan) bisa dijangkau audiens seluas mungkin, termasuk pemain dengan kebutuhan berbeda.

---

## 1. Prinsip Dasar: Aksesibilitas sebagai Bagian dari Empati Tematik

Game bertema grief secara inheren bicara soal pengalaman manusia yang universal tapi personal — akan kontradiktif secara tematik kalau game yang bicara soal empati justru sulit diakses sebagian pemain karena hambatan teknis (kebutaan warna, gangguan pendengaran, sensitivitas terhadap gerakan cepat). Aksesibilitas di sini bukan checklist compliance semata, tapi perpanjangan alami dari nilai yang sudah dibangun di seluruh dokumentasi proyek ini.

---

## 2. Struktur HUD In-Game (Menyambung Prinsip Minimal-HUD)

- **Elemen HUD Permanen — Dijaga Seminimal Mungkin**: idealnya hanya indikator vital yang benar-benar diperlukan saat combat (health, kemungkinan indikator status khusus terkait mekanik The Fading Scarf). Hindari menambah elemen "supaya informatif" tanpa kebutuhan mekanik yang jelas.
- **Elemen Kontekstual — Muncul dan Hilang Sesuai Kebutuhan**: prompt interaksi, indikator arah quest, dsb. sebaiknya hanya muncul saat relevan (dekat objek interaktif) dan memudar otomatis, bukan menempel permanen di layar.
- **Diegetic UI sebagai Prioritas**: sejalan dengan prinsip breadcrumbing visual di Level_Design_Environmental_Storytelling bagian 3, elemen informasi yang bisa disampaikan lewat dunia game itu sendiri (cahaya syal Aina sebagai penanda arah, perubahan warna environment sebagai sinyal status) sebaiknya dipakai lebih dulu sebelum menambah elemen UI non-diegetic.
- **Konsistensi Visual dengan Style Guide**: warna dan style UI (kalaupun minimal) tetap harus mengikuti parameter di Style_Guide_Numerik — HUD yang terlihat "generic engine default" akan merusak keseluruhan art direction yang sudah dibangun matang di dokumen lain.

---

## 3. Struktur Menu Utama (Di Luar Gameplay)

- **Main Menu**: sederhana, dengan opsi Continue/New Game/Settings/Credits — hindari clutter visual, konsisten dengan estetika "kurang adalah lebih" yang sudah ditetapkan di Kreativitas_Seni_Expert.
- **Pause Menu**: minimal, idealnya tidak menghentikan atmosfer sepenuhnya (misal tetap ada ambient sound/visual blur dari game di background, bukan potong total ke layar statis) — supaya jeda tidak terasa seperti "keluar" dari pengalaman emosional yang sedang dibangun.
- **Settings**: dikelompokkan jelas — Audio, Visual, Controls, **Aksesibilitas** (kategori terpisah, bukan disembunyikan di submenu lain supaya mudah ditemukan pemain yang membutuhkannya).
- **Chapter/Memory Select** (jika ada): mengingat tema game soal memori dan kehilangan, fitur ini bisa didesain bukan sebagai "level select" generik, tapi selaras secara tematik (misal direpresentasikan sebagai kilasan/kenangan yang bisa dikunjungi ulang) — rujuk Story_Bible_Lore untuk konsistensi framing naratifnya.

---

## 4. Opsi Aksesibilitas Konkret

### A. Visual
- **Mode Buta Warna** (protanopia, deuteranopia, tritanopia) — penting khususnya karena palet warna dingin-hangat dipakai sebagai storytelling pasif per tahap grief (Referensi_Teori); pastikan indikator penting tidak bergantung warna semata, juga didukung bentuk/pola.
- **Skala Teks Subtitle/UI** — opsi memperbesar ukuran teks tanpa merusak layout.
- **Reduce Flashing/Screen Shake** — untuk momen intens (khususnya sektor Anger dengan handheld shake di Arahan_Sinematik_Cutscene) — opsi mengurangi/mematikan efek ini untuk pemain dengan sensitivitas fotosensitif atau motion sickness.

### B. Audio
- **Subtitle Lengkap** — termasuk deskripsi suara non-dialog penting (misal "[napas tercekat]", "[keheningan panjang]") untuk pemain tuli/gangguan pendengaran, supaya momen non-verbal vocalization (Arahan_Vokal_Delivery_Dialog bagian 4) tetap tersampaikan maknanya secara visual.
- **Visual Cue untuk Audio Tell** — mengingat attack telegraphing musuh sebagian mengandalkan audio tell (Desain_Musuh_Balancing_Combat bagian 4), sediakan opsi indikator visual alternatif untuk pemain yang tidak bisa mengandalkan audio.
- **Balance Slider Terpisah** — musik, SFX, dialog diatur independen, bukan satu volume master saja.

### C. Kontrol & Gameplay
- **Remapping Kontrol Penuh** — termasuk opsi untuk pemain dengan keterbatasan gerak (single-handed control scheme jika memungkinkan).
- **Opsi Kesulitan Combat Terpisah dari Opsi Kesulitan Puzzle/Eksplorasi** — supaya pemain yang kesulitan di satu aspek tidak harus mengorbankan tantangan di aspek lain yang justru mereka nikmati.
- **Assist Mode untuk QTE/Timing Sensitif** (jika ada mekanik semacam itu) — opsi memperlebar window timing tanpa mengubah keseluruhan pengalaman naratif.

### D. Konten Sensitif
- **Content Warning di Awal** — pemberitahuan singkat, tidak spoiler, bahwa game membahas tema grief/kehilangan — memberi pemain kesempatan mempersiapkan diri secara emosional, terutama relevan kalau ada pemain yang sedang berduka secara personal.
- **Opsi Skip untuk Momen Sangat Intens** (dipertimbangkan hati-hati) — trade-off antara integritas artistik dan kenyamanan pemain; kalau diimplementasikan, sebaiknya dengan friksi sengaja (bukan tombol skip sekali klik) supaya tidak dipakai sembarangan untuk melewati momen naratif inti.

---

## 5. Localization-Ready Design (Persiapan, Bukan Implementasi Penuh)

- **Text Container Fleksibel**: desain UI/subtitle container yang bisa menampung ekspansi teks (bahasa lain seringkali lebih panjang dari Bahasa Indonesia/Inggris) tanpa terpotong.
- **Hindari Teks dalam Aset Visual**: teks penting sebaiknya tidak di-bake langsung ke tekstur/gambar (misal signage in-game) kalau memungkinkan diganti sistem terpisah — memudahkan lokalisasi di masa depan tanpa rework aset visual.

---

## 6. Checklist Integrasi ke Visual Self-Review Loop

Poin tambahan untuk `Lentera_Pudar_AI_Automation_Visual_SelfReview_Protocol.md`:

1. Apakah elemen HUD baru benar-benar dibutuhkan secara mekanik, atau bisa disampaikan lewat diegetic UI (bagian 2)?
2. Apakah ada indikator penting yang bergantung warna semata tanpa dukungan bentuk/pola untuk mode buta warna (bagian 4.A)?
3. Apakah audio tell (attack telegraphing musuh, non-verbal vocalization) sudah punya alternatif visual/tekstual (bagian 4.B)?
4. Apakah teks UI/subtitle didesain dalam container fleksibel untuk kebutuhan lokalisasi ke depan (bagian 5)?

---

*Dokumen ke-30 dari paket dokumentasi pra-produksi Lentera Pudar — pelengkap Psikologi_Expert.md (alasan psikologis minimal-HUD) dan Style_Guide_Numerik.md (konsistensi visual), khusus untuk spesifikasi konkret UI/UX dan aksesibilitas. Ini menuntaskan seluruh gap yang teridentifikasi di sesi ini.*

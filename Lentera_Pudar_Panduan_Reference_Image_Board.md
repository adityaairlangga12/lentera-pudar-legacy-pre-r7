# Panduan Kurasi Reference Image Board — Lentera Pudar
### Shot-List untuk Dikumpulkan Manual (Kena: Bridge of Spirits + Hellblade Senua's Sacrifice/II)

**Catatan penting**: Saya tidak bisa menyediakan screenshot langsung karena itu materi berhak cipta milik Ember Lab (Kena) dan Ninja Theory/Xbox Game Studios (Hellblade). Dokumen ini adalah **daftar belanja visual** — kategori persis apa yang harus dicari, dari sumber resmi/legal, lalu dikumpulkan ke tools moodboard (PureRef, Milanote, Figma, atau bahkan folder gambar biasa) sebagai lampiran visual untuk AI agent kamu.

**Sumber legal yang direkomendasikan**: Steam store page (screenshot resmi), situs resmi developer (emberlab.com, ninjatheory.com / Xbox Wire), trailer resmi di YouTube channel developer (screenshot dari video, bukan re-upload orang lain), art book resmi jika ada, dan review/preview dari media game besar (biasanya pakai capture resmi dari developer).

---

## 1. Kategori dari KENA: BRIDGE OF SPIRITS (Artstyle)

### A. Palet Warna & Kontras Hangat-Dingin
- Cari: adegan area "Rot cleansing" — transisi visual dari area gelap/mati ke area hijau/hidup
- Cari: screenshot area Corruption (biru-ungu gelap) vs area yang sudah dibersihkan
- Fokus perhatian: bagaimana satu adegan bisa punya 2 zona warna kontras tajam tanpa terasa "pecah" secara komposisi

### B. Desain Karakter (Siluet & Proporsi)
- Cari: render/screenshot karakter Kena dari berbagai sudut (official character reveal art di situs resmi)
- Cari: desain Rot (makhluk kecil pendukung) — bentuk simpel, siluet jelas dari jauh
- Fokus perhatian: bagaimana proporsi semi-realistis tapi tetap "bersih" siluetnya, tidak terlalu detail berlebihan

### C. Environment Organik-Reruntuhan
- Cari: screenshot kuil/reruntuhan yang ditumbuhi tanaman atau elemen alam
- Cari: area hutan dengan struktur arsitektur kuno di tengahnya
- Fokus perhatian: rasio antara elemen alam vs elemen buatan manusia dalam satu frame

### D. Pencahayaan Sumber Kecil-Kontras Tinggi
- Cari: adegan gua/area gelap dengan satu sumber cahaya kecil (lentera, cahaya spirit)
- Fokus perhatian: seberapa gelap area sekitar dibiarkan supaya sumber cahaya kecil tetap terasa dominan secara visual

---

## 2. Kategori dari HELLBLADE (Senua's Sacrifice & Hellblade II) — Mekanik & Mood

### A. Curse/Darkness Visual Progression
- Cari: screenshot lengan Senua dengan Darkness di berbagai tahap (awal game vs mendekati akhir)
- Fokus perhatian: bagaimana rambatan visual terasa "hidup"/organik, bukan sekadar tekstur statis

### B. Kamera Dekat / Close-Up Emosional
- Cari: screenshot/capture momen wajah Senua di-close-up saat momen emosional kunci (banyak beredar di trailer/review Hellblade II)
- Fokus perhatian: sudut kamera, depth of field (blur background), posisi wajah di frame

### C. Environment yang Berubah Bentuk (Set-Piece Live Transformation)
- Cari: capture dari trailer Hellblade II yang menunjukkan lingkungan berubah/retak secara real-time
- Fokus perhatian: teknik transisi — apakah ada efek partikel/distorsi yang menutupi "sambungan" perubahan, supaya tidak terlihat seperti cut kasar

### D. Desain Boss/Musuh sebagai Manifestasi Psikologis
- Cari: screenshot boss encounter dari Senua's Sacrifice (mis. pertarungan final)
- Fokus perhatian: bagaimana desain visual musuh menyiratkan trauma/emosi, bukan sekadar monster generik

### E. Minimal HUD dalam Aksi
- Cari: screenshot gameplay combat — perhatikan nyaris tidak ada elemen UI di layar
- Fokus perhatian: bagaimana informasi status (rage/kondisi Senua) disampaikan lewat visual dunia, bukan angka

---

## 3. Struktur Folder/Board yang Disarankan

Supaya AI agent bisa merujuk dengan mudah saat diberi konteks, susun board dengan struktur folder/kategori seperti ini (nama folder sebaiknya konsisten dengan istilah di GDD/Style Guide):

```
/reference-board
  /01_palet_warna_kontras       (dari Kena)
  /02_desain_karakter_siluet    (dari Kena)
  /03_environment_organik       (dari Kena)
  /04_pencahayaan_kontras       (dari Kena)
  /05_curse_progression         (dari Hellblade)
  /06_kamera_closeup_emosional  (dari Hellblade)
  /07_environment_transform     (dari Hellblade II)
  /08_boss_psikologis           (dari Hellblade)
  /09_minimal_hud               (dari Hellblade)
```

Tiap folder idealnya berisi 5–10 gambar terkurasi (bukan asal banyak) — kualitas kurasi lebih penting daripada kuantitas, supaya AI agent tidak "bingung" oleh referensi yang saling bertentangan dalam satu kategori.

---

## 4. Cara Memakai Board Ini dengan AI Agent

- Kalau AI agent kamu punya kemampuan menerima input gambar (multimodal), sertakan 1–3 gambar paling representatif dari kategori yang relevan **bersamaan** dengan instruksi teks saat memberi task visual (misal: task material kristal es → sertakan gambar kategori 01 & 04).
- Kalau AI agent hanya berbasis teks murni untuk MCP command, tetap simpan board ini sebagai rujukan manusia — kamu yang melakukan visual QC dengan membandingkan hasil kerja AI terhadap board ini secara manual (sesuai protokol review di dokumen QA/QC bagian 6.A).
- Update board ini seiring waktu — kalau menemukan referensi baru yang lebih pas, ganti yang lama, jangan biarkan board menumpuk referensi yang sudah tidak relevan.

---

*Dokumen ini adalah panduan kurasi, bukan kumpulan gambar itu sendiri — pengumpulan visual aktual perlu dilakukan manual dari sumber resmi/legal sesuai daftar di atas.*

# Game Design Document (GDD) — Lentera Pudar: Master Bible

Dokumen ini adalah sumber kebenaran desain game (*Game Design Source of Truth*) mutlak untuk narasi, filosofi, mekanik gameplay, psikologi pemain, sistem engine, dan rancangan semesta proyek **Lentera Pudar**.

---

## 1. Identitas & Visi Semesta (Universe Identity)

- **Judul Proyek**: Lentera Pudar — The First Spark
- **Genre**: 2D Pixel Action RPG / Psychological Dungeon Crawler (Low Top-Down 3/4)
- **Engine**: Godot 4.7.1 (Renderer: Compatibility, Platform: PC Windows)
- **Arsitektur Rendering**: **Jalur B (Hybrid 3-MCP)**: Karakter low-poly 3D (300–1000 tris) di Blender 5.2 LTS ➔ Render via `Camera3D Orthogonal` ke `SubViewport` resolusi rendah + Filter *Nearest* + Cel-Shader di Godot 4.7.1. Aset UI, Tileset Dungeon, dan FX Flipbook Hard-Edge dibuat di Aseprite.
- **Nuansa Atmosferik**: *Misterius-Hangat Melankolis* (Kontras eksistensial antara kehangatan cinta/harapan dan dinginnya kepasrahan abadi).

---

## 2. Kosmologi & Filosofi: Makna Hakiki "Pudar"

### A. Entropi Jiwa & Kepunahan Makna (*The Great Despair*)
Kutukan Pudar bukan sekadar es fisik atau sihir kutukan iblis. Pudar adalah **perwujudan fisik dari kepasrahan dan kepunahan hasrat hidup (Emotional Numbness / Anhedonia)**.
- Ketika manusia mengalami kepedihan dan trauma hidup yang melampaui batas kewarasannya, suhu tubuh mereka mendingin, molekul mereka melambat, dan jiwa mereka mengkristal menjadi **patung es biru pudar (`#4A6FA5`)**.
- **Ironi Psikologis**: Menjadi es terasa "damai dan nyaman" bagi para korban karena membebaskan mereka dari rasa sakit, penyesalan, dan duka. Membakar lentera untuk mencairkan mereka berarti mengembalikan rasa sakit dan ingatan pedih hidup mereka.
- **Kristal Es Pudar**: Es ini terbuat dari air mata dan kenangan masa lalu yang membeku.

### B. Tiga Respon Manusia terhadap Pudar
1. **The Frozen Ascetics (Kaum Pasrah)**: Memilih membeku sukarela dan menganggap api lentera sebagai pengacau kedamaian.
2. **The Ash Fanatics (Pemuja Abu)**: Membakar rumah, sejarah, dan kemanusiaan mereka demi menjaga api unggun tetap menyala karena takut mati rasa.
3. **The Drifters (Para Pengelana — Seperti Protagonis)**: Terjebak di batas kenyataan: separuh tubuh mati rasa oleh es, separuh tubuh menahan perihnya api lentera.

---

## 3. Karakter Utama & Tragedi Ikatan Jiwa

```
            [ TRAGEDI IKATAN JIWA ]
    
    🗡️ KAELEN (Protagonis)          🧣 AINA (Jiwa Syal Lentera)
    • Sang Pembawa Penyesalan.       • Sang Pengorbanan Murni.
    • Setengah beku di lengan kiri   • Membakar jiwanya sendiri
      karena pernah menyerah.          menjadi syal api kuning.
    • Berjalan membawa rasa sakit.   • Mengikat Kaelen ke dunia nyata.
```

### A. Protagonis: Kaelen (Sang Pengelana Patah Hati)
- Karakter tunggal *class-less*, berambut abu-abu acak, berpakaian jubah kelana gelap (`#2A211C`) dengan sabuk selempang kulit melintang (*baldric harness*).
- **Mata Kanan Tertutup Eyepatch**: Mengenakan penutup mata kulit hitam (`#141013`) sebagai segel bekas luka beku perambatan Kutukan Pudar masa lalu sebelum Aina mengorbankan jiwanya.
- **Lengan Kiri Beku (`#4A6FA5`)**: Dibalut kristal es dan perban beku dengan urat es menyembul keluar.
  - **Live Shader Reactive**: Urat es dikendalikan secara real-time via `CursedHand.gdshader` dengan parameter `uniform float intensity` yang di-bind ke nilai *Curse Meter* (0.0 hingga 1.0).
- **Kombat Awal**: Bertarung menggunakan tangan kosong (*Bare Hand*). Kombo 2-Hit: Pukulan kanan fisik cepat (`attack_punch`) disambung Hantaman telapak tangan kiri es kutukan (`attack_cursed`).

### B. Sang Lentera: Aina (Jiwa di Balik Syal Kuning)
- Syal kuning tebal melingkar di leher Kaelen (`#F4B860`) memancarkan `PointLight2D` dinamis dengan suhu warna Kelvin hangat (2700K).
- **Fisika Sekunder**: Menggunakan *Spring-Damper System* dan *Velvet Modifier* pada bone syal sehingga berkibar dan bereaksi terhadap pergerakan tubuh Kaelen secara alami.
- **Mekanik Naratif: *The Fading Scarf***:
  - Dikelola sebagai keluarga aset 4 tahap (*Asset Variant Set*):
    1. **Tahap 1 (Panjang & Tebal)**: Kondisi awal, berkibar megah hingga pinggul.
    2. **Tahap 2 (Sedang)**: Menyusut setelah Sektor 1–2, ujung mulai terurai.
    3. **Tahap 3 (Pendek)**: Memendek hingga bahu setelah Sektor 3–4.
    4. **Tahap 4 (Koyak & Tipis)**: Sisa rajutan api rapuh di Sektor 5.
  - Pergantian varian di-drive secara otomatis oleh progres cerita via jembatan `bind_visual_state_to_flag("altars_lit_count")`.

---

## 4. Struktur 5 Sektor Dungeon: 5 Tahapan Berduka (*5 Stages of Grief*)

```
[Sektor 1: DENIAL] ➔ [Sektor 2: ANGER] ➔ [Sektor 3: BARGAINING] ➔ [Sektor 4: DEPRESSION] ➔ [Sektor 5: ACCEPTANCE]
```

### 1. Sektor 1 (Denial / Penyangkalan): *Reruntuhan Kristal Beku*
- **Lingkungan**: Kota bawah tanah beku yang rapi. Patung warga membeku saat sedang berpura-pura minum teh atau membaca buku.
- **Bos: Lord Alden, Sang Penjaga Gerbang Kosong**: Kesatria yang menolak kenyataan bahwa kerajaannya sudah lama hancur; terus berpatroli menjaga gerbang kosong.
- **Pesan**: *Penyangkalan adalah pelindung paling nyaman dari kenyataan yang kejam.*

### 2. Sektor 2 (Anger / Kemarahan): *Dapur Peleburan Padam*
- **Lingkungan**: Mesin-mesin uap dan sungai lava yang membeku saat sedang meledak. Percikan api merah bertabrakan dengan kristal es tajam.
- **Bos: Ignis Vulkan, Sang Pandai Besi Api Hampa**: Jiwa yang mengamuk membakar tubuhnya sendiri karena gagal mencairkan wabah es.
- **Pesan**: *Kemarahan yang membabi buta hanya akan membakar diri sendiri dari dalam.*

### 3. Sektor 3 (Bargaining / Tawar-Menawar): *Arsip Janji Kuno*
- **Lingkungan**: Perpustakaan bawah tanah raksasa terendam air beku dengan jutaan gulungan kontrak yang gagal mencegah kutukan.
- **Bos: Lady Vespera, Sang Penenun Perjanjian**: Ratu cendekiawan yang memanipulasi ilusi dan menawarkan Kaelen perjanjian untuk mengembalikan Aina.
- **Pesan**: *Tawar-menawar dengan takdir adalah bentuk keputusasaan paling licik.*

### 4. Sektor 4 (Depression / Depresi): *Jurang Kesunyian Abadi*
- **Lingkungan**: Area tergelap dan terdingin. Radius cahaya syal menyusut 50% secara otomatis, pergerakan terasa berat, dan musik berhenti menjadi dengung hening (*tinnitus*).
- **Bos: The Hollow Reflection (Bayangan Kaelen)**: Cerminan diri Kaelen yang meniru seluruh gerakan pemain menggunakan mekanisme *Circular Input Replay Buffer* dengan delay frame sebagai pengatur kesulitan.
- **Pesan**: *Musuh terberat seorang manusia adalah suaranya sendiri yang membujuk untuk menyerah.*

### 5. Sektor 5 (Acceptance / Penerimaan): *Puncak Menara Fajar Pudar*
- **Lingkungan**: Puncak menara di atas awan es di mana fajar pertama bertemu dengan badai kristal abadi.
- **Bos & Resolusi: The Frost Sovereign & Fajar Terakhir**: Rekonsiliasi duka dan pelepasan jiwa Aina menuju fajar baru.

---

## 5. Mekanik Gameplay, Sistem Fisika, & Gap Features

### A. The Temptation of Frost (Godaan Kekuatan Kutukan)
- Saat Kaelen bertarung di kegelapan tanpa mendekati lentera (*Curse Meter* naik 0% ➔ 100%):
  - Serangan tangan kiri es menjadi sangat destruktif, jangkauan luas, dan musuh pecah instan.
  - Urat es di shader `CursedHand.gdshader` menyala semakin terang dan merambat ke lengan atas.
- **Dilema Pemain**: Pemain tergoda membiarkan diri hampir membeku demi memenangkan pertarungan sulit. Jika meter menyentuh 100%, Kaelen membeku (*Game Over*).

### B. Echoes of the Past (Gema Memori Ruangan)
- Menyalakan altar memancarkan gelombang cahaya emas yang mengubah ruangan runtuh menjadi transparan melalui arsitektur **Dual-Layer Room**:
  1. *Foreground Layer*: Kondisi ruangan hancur/beku saat ini.
  2. *Memory Layer*: Kondisi ruangan megah di masa lalu.
- Transisi berjalan selama 5–10 detik menggunakan *Noise Dissolve Shader* sebelum kembali ke kondisi saat ini, mengungkap petunjuk jalan rahasia dan teka-teki dungeon.

### C. The Dual Evolution Tree (Pilihan Ending Moral)
1. **Path of the Lantern (Kemanusiaan)**: Fokus memperluas radius lentera dan memulihkan jiwa-jiwa beku.
2. **Path of the Frost (Kekuatan Dingin)**: Fokus memperkuat destruksi es tangan kiri.
- Menghasilkan 3 Ending: *The Eternal Slumber (Menyerah)*, *The Blazing Desolation (Hangus)*, atau *The Living Dawn (True Ending - Menerima Luka dan Membawa Fajar)*.

---

## 6. Standar Teori Domain: Lighting, Kamera, Audio, & AI

### A. Teori Pencahayaan (Lighting)
- **Skala Kelvin Emosional**:
  - Sumber Lentera & Altar: **2700K Warm Gold (`#F4B860`)** dengan *photometric falloff*.
  - Sumber Es & Kutukan: **6500K Cold Cyan/Blue (`#4A6FA5`)** dengan *linear falloff*.
- **Shadow Casting**: Dinding dan pilar dungeon wajib memiliki `LightOccluder2D` ber-polygon tertutup agar cahaya lentera tidak menembus dinding.
- **Radius State-Bound**: Radius cahaya lentera di-bind langsung ke status gameplay (normal: 100%, Sektor 4: 50%, Altar aktif: burst 150%).

### B. Teori Kamera (Camera2D)
- **Look-Ahead Offset**: Kamera bergeser halus (16–24 px) ke arah hadap/kecepatan karakter menggunakan peredam *Spring-Damper* agar pemain dapat melihat ke depan.
- **Room Bounds Clamping**: Posisi kamera di-clamp secara kaku pada batas rect ruangan level agar tidak menampilkan area di luar dungeon.
- **Arena Transition**: Menggunakan *PD Controller* untuk zoom-in halus dan reposisi kamera saat memasuki arena pertarungan bos.

### C. Teori Audio & Akustik
- **Hirarki Bus Audio**: `Master ➔ [Music, SFX, Voice, Ambience]`.
- **Ducking Naratif**: Volume bus `Music` dan `SFX` diturunkan otomatis sebesar -6dB hingga -10dB (attack: 150ms, release: 400ms) saat dialog penting Aina muncul.
- **Adaptive Music Layers**: Musik dungeon memiliki layer instrumen es dingin yang otomatis membesar volumenya saat *Curse Meter* pemain meningkat.

### D. AI Khusus: The Hollow Reflection (Boss Sektor 4)
- Menggunakan arsitektur **Circular Input Replay Buffer** (menyimpan buffer data input pemain sebanyak $N$ frame terakhir).
- Karakter bos memutar ulang rekaman buffer tersebut dengan delay frame tertentu ($D$ frame). Makin tinggi fase pertarungan, delay $D$ makin dipersingkat sehingga bos meniru aksi pemain hampir secara instan.

---

## 7. Plot Twist Puncak (*The Ultimate Revelation*)

1. **Dungeon ini adalah Makam Agung (*The Great Sanctuary*)**: Dibangun oleh umat manusia masa lalu yang sepakat tidur bersama dalam es abadi demi menghentikan siklus penderitaan hidup.
2. **Dosa Kaelen**: Kaelen adalah orang yang pertama kali memicu artefak Pudar demi membekukan Aina yang sekarat agar tubuhnya tidak membusuk, namun wabah tersebut merambat menelan seluruh dunia.
3. **Pengorbanan Aina**: Aina merobek jiwanya menjadi Syal Lentera untuk membangunkan Kaelen dan berkata: *"Bangunlah, Kaelen. Jangan sembunyikan dukamu di dalam es. Bawa aku melihat fajar sekali lagi."*

---

## 8. Infrastruktur Produksi & Roadmap MVP

```
[FASE 0: Proof of Concept] ➔ [FASE 1: Kaelen Rig] ➔ [FASE 2: Vertical Slice Sektor 1] ➔ [FASE 3: Full 5 Sectors]
```

- **Infrastruktur Ekosistem**:
  - **Git LFS**: Mengelola aset biner (`.blend`, `.aseprite`, `.wav`, `.png`).
  - **GUT (Godot Unit Test)**: Pengujian unit otomatis untuk *Curse Meter*, formula damage, dan kalkulasi branching ending.
  - **Quality Control (QC Gate)**: Mengadopsi **The 4-Tier Commercial Gate** (Visual Fidelity 4K, 60 FPS 0-Error Runtime, Multi-Controller & Steam Compliance, 100% GUT Test Pass).
  - **Dialogic 2**: Integrasi editor dialog dan sistem percabangan naratif.
  - **Atomic Save/Load System**: Protokol penulisan simpanan atomic anti-korupsi (`.tmp` ➔ SHA-256 Checksum ➔ `.bak` backup ➔ `.dat`) untuk persistensi data *The Fading Scarf* dan progres dungeon antar sesi (Steam Cloud Ready).
- **Target MVP (Vertical Slice)**: Menyelesaikan secara sempurna **Karakter Kaelen + Sektor 1 (Denial) + Bos Lord Alden + Mekanik Dual-Layer Echoes of the Past + Audio/Lighting Pipeline** sebelum melakukan ekspansi ke sektor 2–5.

---

## 9. Peta Jalan Franchise (Lentera Pudar Expanded Universe)

```
[LENTERA PUDAR 1]           [LENTERA PUDAR 2]             [LENTERA PUDAR 3]
"The First Spark"           "The Frozen Horizon"          "The Sovereign of Dawn"
Dungeon Bawah Tanah ──►   Benua Luar yang Membeku ──►   Pembangunan Peradaban Fajar Baru
(Penyembuhan Diri Sendiri)   (Menghidupkan Kota-Kota Es)   (Rekonsiliasi Api & Keabadian Es)
```

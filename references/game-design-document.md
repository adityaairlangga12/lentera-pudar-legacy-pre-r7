# Game Design Document (GDD) — Lentera Pudar: Master Bible

Dokumen ini adalah sumber kebenaran desain game (*Game Design Source of Truth*) mutlak untuk narasi, filosofi, mekanik gameplay, psikologi pemain, dan rancangan semesta proyek **Lentera Pudar**.

---

## 1. Identitas & Visi Semesta (Universe Identity)

- **Judul Proyek**: Lentera Pudar — The First Spark
- **Genre**: 2D Pixel Action RPG / Psychological Dungeon Crawler (Low Top-Down 3/4)
- **Engine**: Godot 4.7.1 (Renderer: Compatibility, Platform: PC Windows)
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
- Karakter tunggal *class-less*, berambut abu-abu acak, berpakaian jubah kelana gelap (`#2A211C`) dengan tali selempang kulit (*baldric harness*).
- **Mata Kanan Tertutup Eyepatch**: Mengenakan penutup mata kulit hitam (`#141013`) sebagai segel bekas luka beku perambatan Kutukan Pudar masa lalu sebelum Aina mengorbankan jiwanya.
- **Lengan Kiri Beku (`#4A6FA5`)**: Dibalut kristal es dan perban beku dengan urat es menyembul keluar (`CursedHand.gdshader`). Bukti bahwa Kaelen pernah hampir menyerah dan membekukan dirinya sendiri di masa lalu.
- **Kombat Awal**: Bertarung menggunakan tangan kosong (*Bare Hand*). Kombo 2-Hit: Pukulan kanan fisik (`attack_punch`) disambung Hantaman telapak tangan kiri es kutukan (`attack_cursed`).

### B. Sang Lentera: Aina (Jiwa di Balik Syal Kuning)
- Syal kuning tebal melingkar di leher Kaelen (`#F4B860`) memancarkan `PointLight2D` dinamis.
- **Mekanik Naratif: *The Fading Scarf***:
  - Di awal game, syal Aina sangat panjang, tebal, dan berkibar megah.
  - Setiap kali Kaelen menyalakan Altar Lentera besar untuk menyelamatkan distrik dungeon, api syal tersebut terpakai.
  - Sepanjang cerita, syal perlahan memendek, menipis, dan koyak, memperlihatkan pengorbanan Aina secara nyata kepada pemain.

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
- **Lingkungan**: Area tergelap dan terdingin. Radius cahaya syal menyusut 50%, gravitasi terasa berat, dan musik berhenti menjadi dengung hening (*tinnitus*).
- **Bos: The Hollow Reflection (Bayangan Kaelen)**: Cerminan diri Kaelen yang meniru seluruh gerakan pemain sambil membisikkan keputusasaan.
- **Pesan**: *Musuh terberat seorang manusia adalah suaranya sendiri yang membujuk untuk menyerah.*

### 5. Sektor 5 (Acceptance / Penerimaan): *Puncak Menara Fajar Pudar*
- **Lingkungan**: Puncak menara di atas awan es di mana fajar pertama bertemu dengan badai kristal abadi.
- **Bos & Resolusi: The Frost Sovereign & Fajar Terakhir**: Rekonsiliasi duka dan pelepasan jiwa Aina menuju fajar baru.

---

## 5. Mekanik Psikologi & Gameplay (*Ludonarrative*)

### A. The Temptation of Frost (Godaan Kekuatan Kutukan)
- Saat Kaelen bertarung di kegelapan tanpa mendekati lentera (*Curse Meter* tinggi), serangan tangan kiri es menjadi **sangat destruktif, jangkauan luas, dan musuh hancur instan**.
- **Dilema Pemain**: Pemain secara psikologis tergoda membiarkan diri hampir membeku demi memenangkan pertarungan sulit. Jika meter menyentuh 100%, Kaelen membeku (*Game Over*).

### B. Echoes of the Past (Gema Memori Ruangan)
- Menyalakan altar memancarkan gelombang cahaya emas yang mengubah ruangan runtuh menjadi transparan dan memperlihatkan kenangan masa lalu selama 5–10 detik untuk memecahkan teka-teki jalan rahasia.

### C. The Dual Evolution Tree (Pilihan Ending Moral)
1. **Path of the Lantern (Kemanusiaan)**: Fokus memperluas radius lentera dan memulihkan jiwa-jiwa beku.
2. **Path of the Frost (Kekuatan Dingin)**: Fokus memperkuat destruksi es tangan kiri.
- Menghasilkan 3 Ending: *The Eternal Slumber (Menyerah)*, *The Blazing Desolation (Hangus)*, atau *The Living Dawn (True Ending - Menerima Luka dan Membawa Fajar)*.

---

## 6. Plot Twist Puncak (*The Ultimate Revelation*)

1. **Dungeon ini adalah Makam Agung (*The Great Sanctuary*)**: Dibangun oleh umat manusia masa lalu yang sepakat tidur bersama dalam es abadi demi menghentikan siklus penderitaan hidup.
2. **Dosa Kaelen**: Kaelen adalah orang yang pertama kali memicu artefak Pudar demi membekukan Aina yang sekarat agar tubuhnya tidak membusuk, namun wabah tersebut merambat menelan seluruh dunia.
3. **Pengorbanan Aina**: Aina merobek jiwanya menjadi Syal Lentera untuk membangunkan Kaelen dan berkata: *"Bangunlah, Kaelen. Jangan sembunyikan dukamu di dalam es. Bawa aku melihat fajar sekali lagi."*

---

## 7. Peta Jalan Franchise (Lentera Pudar Expanded Universe)

```
[LENTERA PUDAR 1]           [LENTERA PUDAR 2]             [LENTERA PUDAR 3]
"The First Spark"           "The Frozen Horizon"          "The Sovereign of Dawn"
Dungeon Bawah Tanah ──►   Benua Luar yang Membeku ──►   Pembangunan Peradaban Fajar Baru
(Penyembuhan Diri Sendiri)   (Menghidupkan Kota-Kota Es)   (Rekonsiliasi Api & Keabadian Es)
```

- **Lentera Pudar 1: The First Spark**: Perjalanan intim Kaelen di dungeon bawah tanah menyembuhkan duka pribadinya dan membuka pintu gerbang dunia luar.
- **Lentera Pudar 2: The Frozen Horizon**: Eksplorasi skala luas di *Overworld* benua es abadi, menembus badai salju, menemukan benteng api terapung (*The Ash Citadels*), dan menjadi legenda pengelana pembawa lentera.
- **Lentera Pudar 3: The Sovereign of Dawn**: Klimaks kosmik rekonsiliasi antara Api Abadi dan Es Abadi.

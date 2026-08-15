# Game Design Document (GDD) — Lentera Pudar: 3D Action RPG Master Bible

Dokumen ini adalah sumber kebenaran desain game (*Game Design Source of Truth*) mutlak untuk narasi, filosofi, mekanik gameplay 3D, psikologi pemain, sistem engine, dan rancangan semesta proyek **Lentera Pudar** (Unreal Engine 5 + Blender 5.2 LTS).

---

## 1. Identitas & Visi Semesta (Universe Identity)

- **Judul Proyek**: Lentera Pudar — The First Spark
- **Genre**: 3D Third-Person Action-Adventure RPG (Stylized Anime / Poetic Dark Fantasy — Inspirasi: *Final Fantasy VII Remake*, *NieR: Automata*, *Genshin Impact*)
- **Engine**: Unreal Engine 5 (UE5 Pipeline, Platform: PC Windows / Steam)
- **Arsitektur Rendering**: High-Fidelity 3D (Lumen Dynamic Global Illumination, Niagara Particles, Nanite Geometry, Cloth Physics)
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
    
    🗡️ KAELEN (Protagonis 3D)        🧣 AINA (Jiwa Syal Lentera)
    • Sang Pembawa Penyesalan.       • Sang Pengorbanan Murni.
    • Setengah beku di lengan kiri   • Membakar jiwanya sendiri
      karena pernah menyerah.          menjadi syal api kuning.
    • Berjalan membawa rasa sakit.   • Mengikat Kaelen ke dunia nyata.
```

### A. Protagonis: Kaelen (Sang Pengelana Patah Hati)
- Karakter tunggal *class-less*, berambut perak acak 3D, berpakaian jubah kelana gelap (`#2A211C`) dengan sabuk selempang kulit melintang (*baldric harness*).
- **Mata Kanan Tertutup Eyepatch**: Mengenakan penutup mata kulit hitam (`#141013`) sebagai segel bekas luka beku perambatan Kutukan Pudar masa lalu.
- **Lengan Kiri Beku (`#4A6FA5` / `#7EE8FA`)**: Kluster kristal es prisma bersudut tajam (*crystal talons*) dengan shader kristal es transparan dan pendaran emissive live sesuai tingkat *Curse Meter*.
- **Kombat 3D Third-Person**: Bertarung menggunakan kombinasi tangan kosong berbalut perban (*Bare Hand Punch Combo*) dan cakar es kristal destruktif (*Cursed Ice Strike*).

### B. Sang Lentera: Aina (Jiwa di Balik Syal Kuning)
- Syal kuning tebal melingkar di leher Kaelen (`#F4B860` 2700K) memancarkan cahaya dinamis lembut ke lingkungan 3D dungeon.
- **Fisika Kain Dinamis**: Menggunakan *Cloth Simulation & Spring Bones* sehingga syal berkibar anggun mengikuti gravitasi, ayunan langkah kaki, dan tiupan angin dungeon.
- **Mekanik Naratif: *The Fading Scarf***:
  Syal memendek secara permanen dalam 4 tahap pengorbanan (*4 Stages of Sacrifice*) setiap kali Kaelen menyalakan Altar Duka di dungeon.

---

## 4. Struktur 5 Sektor Dungeon: 5 Tahapan Berduka (*5 Stages of Grief*)

```
[Sektor 1: DENIAL] ➔ [Sektor 2: ANGER] ➔ [Sektor 3: BARGAINING] ➔ [Sektor 4: DEPRESSION] ➔ [Sektor 5: ACCEPTANCE]
```

1. **Sektor 1 (Denial / Penyangkalan) — *The Silent Crypts***:
   - Kota bawah tanah beku kuno di mana patung-patung warga membeku saat sedang berpura-pura hidup normal.
   - **Bos: Lord Alden, Sang Penjaga Gerbang Kosong**: Kesatria berzirah es yang menolak kenyataan bahwa kerajaannya telah hancur.
2. **Sektor 2 (Anger / Kemarahan) — *The Blazing Frost***:
   - Peleburan es di mana amarah dingin meledak-ledak. Percikan api merah bertabrakan dengan kristal es beku.
   - **Bos: Ignis Vulkan, Sang Pandai Besi Api Hampa**.
3. **Sektor 3 (Bargaining / Tawar-Menawar) — *The Hall of Mirrors***:
   - Labirin cermin waktu dan arsip perjanjian kuno terendam air es.
   - **Bos: Lady Vespera, Sang Penenun Perjanjian**.
4. **Sektor 4 (Depression / Depresi) — *The Abyss of Stillness***:
   - Danau keheningan gelap tanpa suara. Radius cahaya syal menyusut 50%, pergerakan terasa berat.
   - **Bos: The Hollow Reflection (Bayangan Kaelen)**.
5. **Sektor 5 (Acceptance / Penerimaan) — *The Dawning Altar***:
   - Puncak menara di mana fajar pertama menembus badai es abadi. Membuka gerbang keluar dungeon menuju Benua Luar (*Overworld*).

---

## 5. Sistem Kombat 3D, Kamera & Fisika

1. **Third-Person Combat Action FSM**:
   - `Light Attack Combo` (1–3 Hit Punch).
   - `Heavy Cursed Strike` (Hantaman es area destruktif).
   - `Evade Dash` (Gerakan meluncur cepat dengan jejak cahaya emas Aina).
   - `Curse Meter Surge` (Mode ledakan kekuatan es saat meter penuh, berisiko membeku).
2. **Pencahayaan Sinematik 3D (Lumen / PointLight)**:
   - Skala Kelvin 2700K (Lentera Emas Aina) vs 6500K (Kristal Es Kutukan).
   - Bayangan dinamis (*Real-Time Soft Shadows*) pada dinding makam kuno.
3. **Audio Ambience & Dynamic Music**:
   - Soundscape melankolis hening dengan gema tetesan es mencair dan layer musik adaptif sesuai intensitas pertarungan.

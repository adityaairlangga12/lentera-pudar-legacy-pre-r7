# Master Theory: 2D Pixel Art, 3D-to-Pixel Rendering, & Visual Psychology
### *Proyek: Lentera Pudar — Master Visual Foundation*

---

## 📌 Pengantar & Prinsip Fundamental
Dokumen ini mengintegrasikan seluruh hukum fundamental seni piksel 2D, teknik render *3D-to-Pixel* modern (Jalur B), teori perspektif top-down, dan psikologi persepsi visual untuk menjamin konsistensi grafis bergaya *Misterius-Hangat Melankolis*.

---

## BAB I: PERSPEKTIF & RENDER PIPELINE (LOW TOP-DOWN 3/4)

Game kita mengadopsi sudut pandang **Low Top-Down (Kemiringan Kamera ~20°–30°)**:

```
                [ KAMERA ORTHOGONAL 20°-30° DARI ATAS-DEPAN ]
                                \
                                 v
      ┌──────────────────────────────────────────────────────────┐
      │ 1. SOUTH (Depan)    : Tampak dada, wajah, puncak bahu.  │
      │ 2. DIAGONAL (3/4)   : 3/4 wajah & tubuh, kedalaman (Z). │
      │ 3. SIDE (E/W)       : Profil samping, postur & punggung.│
      │ 4. NORTH (Belakang) : Punggung penuh, rambut belakang.  │
      └──────────────────────────────────────────────────────────┘
```

### 1.1 Keunggulan Geometris Jalur B (3D-to-Pixel)
- **Eliminasi Glitch Asimetri**: Pada karakter asimetris (lengan kiri kutukan es `#4A6FA5`, eyepatch kanan `#141013`, tali selempang miring), model 3D menjamin orientasi fisik 100% akurat di semua sudut rotasi tanpa risiko fitur tertukar akibat *mirroring*.
- **SubViewport Pixelation**: Mesh 3D ber-flat shading dirender ke `SubViewport` beresolusi rendah (misal `320x180`), lalu di-upscale via filter **`Nearest`**. Hasilnya adalah siluet piksel tajam dengan volume 3D yang berbobot.

### 1.2 Y-Sort & Depth Ordering
- Pada sudut top-down, posisi sumbu Y menentukan kedalaman (*depth plane*).
- Node karakter dan objek lingkungan wajib mengaktifkan `y_sort_enabled = true` dengan titik poros (*pivot*) terkunci di telapak kaki (garis kontak lantai).

---

## BAB II: TEORI KLUSTER, OUTLINE, & SHADING PIXEL

```
        ❌ DITHERING CATUR (SALAH)            ✅ CLUSTER SHADING (BENAR)
         [ # . # . # . ] (Noise)              [ ■ ■ ■ ■ ] -> Highlight Cluster
         [ . # . # . # ] (Kotor)              [ ▨ ▨ ▨ ▨ ] -> Midtone Body
         [ # . # . # . ] (Glitch)             [ ░ ░ ░ ░ ] -> 1px Vein/Crease
         (Mata membaca sebagai catur)         [ ▓ ▓ ▓ ▓ ] -> Core Shadow
```

### 2.1 Teori Kluster (*Cluster Theory*)
- **Kluster adalah Gumpalan Piksel Solid Berwarna Sama**.
- Di resolusi rendah (< 64px), mata manusia membaca objek melalui bentuk kluster, bukan garis tipis acak.
- **Aturan Mutlak**: Hindari *Orphan Pixels* (1 piksel warna asing yang terisolasi sendiri) dan hindari *Checkerboard Dithering* pada area sempit (< 6px).

### 2.2 Directional Lighting & Shading Bertingkat
- Sumber cahaya utama (*Key Light*) berada di **Kiri-Atas Depan**.
- Shading cel/toon menghasilkan transisi bertingkat yang tegas antara Highlight, Midtone, dan Shadow.
- **Dilarang Pillow Shading**: Shading tidak boleh mengikuti garis tepi melingkar tanpa arah sumber cahaya yang jelas.

### 2.3 Teori Warna Hue Shifting (*The Triad Palette*)
- Dilarang menggelapkan warna murni dengan hanya menurunkan nilai kecerahan (*brightness/V*).
- **Highlights**: Menggeser hue ke arah **Kuning/Hangat** (`#FFE0B2`, `#F4B860` — 2700K Kelvin).
- **Shadows**: Menggeser hue ke arah **Biru Dingin/Netral Gelap** (`#4A6FA5`, `#2C4875`, `#1A1310` — 6500K Kelvin).

---

## BAB III: ANATOMI KARAKTER & FISIOLOGI GERAK

### 3.1 Proporsi Stylized RPG (1:3 hingga 1:3.5)
- **Kepala & Wajah** (~33% tinggi): Area ekspresi emosional duka, poni abu-abu acak, dan eyepatch.
- **Torso & Syal** (~25% tinggi): Area Syal Lentera Aina, kerah jubah kelana, dan tali baldric.
- **Kaki & Pijakan** (~42% tinggi): Area stabilitas, bobot langkah, dan kontak bayangan tanah.

### 3.2 Fisiologi Gerak & Gait Biomechanics
- **Inverted Pendulum**: Tubuh berayun naik-turun secara periodik saat berjalan (body bob frekuensi 2x).
- **Stance vs Swing Phase**: Kaki penopang menahan bobot di tanah, sedangkan kaki pengayun bergerak maju dalam fase sinusoidal.
- **Idle Breathing**: Napas dada berperiode lambat (1.5–2.0 detik) memberikan tanda kehidupan minimum (*life baseline*).

---

## BAB IV: PSIKOLOGI PEMAIN & BAHASA VISUAL EMOSIONAL

Player merasakan narasi melalui **impresi visual dalam 100 milidetik**:

```
 ┌───────────────────────────────────────────────────────────────────────────┐
 │               DUALITAS PSIKOLOGIS UTAMA LENTERA PUDAR                     │
 ├─────────────────────────────────────┬─────────────────────────────────────┤
 │    KEHANGATAN / JIWA AINA (#F4B860) │    KEHAMPAAN / KUTUKAN (#4A6FA5)    │
 ├─────────────────────────────────────┼─────────────────────────────────────┤
 │ • Simbol: Cinta, memori, harapan.   │ • Simbol: Apathy Plague, mati rasa. │
 │ • Visual: Syal lentera yang mengalir│ • Visual: Tangan kiri es beku kaku, │
 │   hangat melingkari leher Kaelen.   │   kristal es dengan urat retak.     │
 │ • Emosi: Sauh penahan keputusasaan. │ • Emosi: Beban duka dan penyesalan. │
 └─────────────────────────────────────┴─────────────────────────────────────┘
```

- **Ekspresi Melankolis Berbobot**: Wajah Kaelen dibingkai oleh bayangan alis di bawah poni rambut abu-abu, memancarkan determinasi seorang pengelana yang tetap melangkah meski memikul duka mendalam.
- **Syal Aina Sebagai Sauh Emosional**: Syal yang memendek seiring berjalannya cerita (*The Fading Scarf*) menjadi pengingat visual konstan atas pengorbanan Aina.

# Rekapitulasi Komprehensif: Teori 2D Pixel Art, Perspektif, Anatomi & Psikologi Karakter
### *Proyek: Lentera Pudar — Protagonis Kaelen V2*

---

## 📌 Pengantar & Refleksi Kritis
Sepanjang beberapa iterasi terakhir, kita menghadapi ketidakteraturan visual (*visual inconsistency*) saat mencoba memperbaiki Kaelen. Dokumen ini merangkum seluruh prinsip fundamental seni piksel 2D, perspektif kamera top-down, psikologi pemain, serta membedah mengapa eksperimen sebelumnya sempat tampak kaku, aneh, atau tidak beraturan.

---

## BAB I: HUKUM PERSPEKTIF 2D (LOW TOP-DOWN 3/4 PROJECTION)

Game kita mengadopsi sudut pandang **Low Top-Down (Kemiringan Kamera ~20°–30°)** seperti *Chrono Trigger*, *The Legend of Zelda: The Minish Cap*, dan *Eastward*.

```
                [ KAMERA 20°-30° DARI ATAS-DEPAN ]
                               \
                                v
      ┌──────────────────────────────────────────────────────────┐
      │ 1. SOUTH (Depan)    : Tampak dada, wajah, puncak bahu.  │
      │ 2. DIAGONAL (3/4)   : 3/4 wajah & tubuh, kedalaman (Z). │
      │ 3. SIDE (E/W)       : Profil samping, postur & punggung.│
      │ 4. NORTH (Belakang) : Punggung penuh, rambut belakang.  │
      └──────────────────────────────────────────────────────────┘
```

### 1.1 Prinsip Kontinuitas 360 Derajat (*The 360° Flow*)
- **Aksesoris Menjuntai (Syal Aina)**:
  - Jika karakter memakai syal panjang di punggung, maka saat menghadap **Samping (`East/West`)** syal terlihat di tepi punggung, saat **Diagonal (`NE/NW`)** syal terlihat di punggung 3/4, dan saat **`North` (Belakang)** syal **WAJIB terlihat paling dominan di tengah punggung**.
  - *Pelajaran dari kegagalan kita*: Di iterasi awal, arah `North` hanya digambar sebagai kerah leher tanpa juntaian punggung, menyebabkan diskontinuitas visual (syal seolah menghilang saat karakter berbalik).

### 1.2 Garis Pijakan Tanah (*Contact Grounding*)
- Di sudut 3/4 top-down, kedua kaki tidak boleh sejajar datar horizontal kecuali pada pose frontal murni (`South` & `North`).
- Pada pose 3/4 (`SE`, `SW`, `NE`, `NW`), kaki yang lebih dekat dengan kamera berada 1–2 piksel lebih rendah untuk menegaskan perspektif kedalaman tanah (*depth plane*).

---

## BAB II: ANATOMI & PROPORSI 32x32PX (MICRO-SPRITE ANATOMY)

### 2.1 Mengapa Realisme 1:8 Gagal di 32x32px?
- Pada kanvas total 32x32px (dengan padding 48x48px), proporsi manusia asli (8 kepala) akan membuat kepala hanya berukuran 3-4 piksel. Wajah, mata, rambut, dan ekspresi emosional akan **musnah menjadi 1 piksel blur**.
- **Standar Emas Stylized RPG (1:3 hingga 1:3.5 Ratio)**:
  - **Kepala + Rambut**: ~11–12 px (33% tinggi tubuh) ➔ Area ekspresi, poni berantakan, dan identitas siluet.
  - **Torso / Dada**: ~7–8 px (22% tinggi tubuh) ➔ Area syal Aina, kerah jubah, dan sabuk kelana.
  - **Kaki + Boots**: ~10–12 px (33% tinggi tubuh) ➔ Area stabilitas, langkah, dan bobot pijakan.
  - **Lengan**: Lebar 3–4 px, panjang 8–10 px ➔ Area asimetri kutukan es vs perban normal.

### 2.2 Postur Tubuh Alami vs Kaku (*Organic Posture vs Toy Soldier*)
- **Shoulder Slope (Kemiringan Bahu)**: Bahu manusia tidak kotak 90 derajat seperti balok Lego, melainkan melandai 1px dari leher ke sendi lengan.
- **Elbow Flex (Tekukan Siku Alami)**: Saat berdiri santai (*idle*), lengan manusia memiliki tekukan alami 15°–20° di siku. Menggambar lengan sebagai garis lurus 180° membuat karakter tampak seperti "robot kaku".

---

## BAB III: ALGORITMA SHADING & PIXEL THEORY (SAINT11 / MORTMORT)

```
        ❌ DITHERING CATUR (SALAH)            ✅ CLUSTER SHADING (BENAR)
         [ # . # . # . ] (Noise)              [ ■ ■ ■ ■ ] -> Highlight Cluster
         [ . # . # . # ] (Kotor)              [ ▨ ▨ ▨ ▨ ] -> Midtone Body
         [ # . # . # . ] (Glitch)             [ ░ ░ ░ ░ ] -> 1px Vein/Crease
         (Mata membaca sebagai catur)         [ ▓ ▓ ▓ ▓ ] -> Core Shadow
```

### 3.1 Teori Kluster (*Cluster Theory*)
- **Kluster adalah Gumpalan Piksel Solid Berwarna Sama**.
- Di resolusi < 64px, mata manusia membaca objek melalui bentuk kluster, bukan garis tipis acak.
- **Aturan Mutlak**: Hindari *Orphan Pixels* (1 piksel warna asing yang terisolasi sendiri) dan hindari *Checkerboard Dithering* pada area sempit (< 6px).

### 3.2 Directional Lighting & Jebakan *Pillow Shading*
- **Pillow Shading (Kesalahan Pemula)**: Menaruh warna terang di tengah objek dan menggelapkannya ke arah tepi luar outline. Objek akan terlihat seperti bantal kembung tanpa massa.
- **Directional Light (Top-Left Key Light)**:
  - Sumber cahaya berasal dari **Kiri-Atas Depan**.
  - Puncak kepala, bahu kiri, dan bagian atas lengan menerima *Highlight*.
  - Bagian bawah ketiak, selangkangan, dan bawah lengan menerima *Core Shadow*.

### 3.3 Teori Warna Hue Shifting (*The Triad Palette*)
- Dilarang menggelapkan warna hanya dengan menurunkan nilai kecerahan (*brightness/V*).
- **Highlight**: Menggeser hue ke arah **Kuning/Hangat** (`#FFE0B2`, `#F4B860`).
- **Shadow**: Menggeser hue ke arah **Biru Dingin/Ungu/Netral Gelap** (`#2C4875`, `#1A1310`).

---

## BAB IV: PSIKOLOGI PEMAIN & BAHASA VISUAL EMOSIONAL

Player tidak membaca dokumen lore saat bermain; mereka merasakan lore melalui **impresi visual dalam 100 milidetik**:

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

### 4.1 Mengapa Wajah "Dua Titik Hitam" Merusak Resonansi?
- Dua titik hitam di wajah polos kuning dibaca otak sebagai **emoticon netral / boneka kosong**, menciptakan diskoneksi psikologis total dengan tema duka (*grief*).
- **Solusi Psikologi Visual**:
  - Poni rambut abu-abu menjatuhkan bayangan alis 1px (*brow shadow `#A86F3E`*).
  - Mata terbingkai teduh, memberi kesan tatapan lelah seorang pengelana yang bertekad menyelesaikan perjalanannya.

---

## BAB V: EVALUASI KRITIS EKSPERIMEN SEBELUMNYA

Mari kita jujur membedah mengapa iterasi kita sempat terasa tidak beraturan:

| Eksperimen | Apa yang Dilakukan | Mengapa Gagal / Terasa Aneh |
|---|---|---|
| **Eksperimen 1** (PixelLab Inpainting AI) | Mengirim mask ke model generatif AI untuk digambar ulang. | AI berhalusinasi: mengubah proporsi siluet, lengan membengkak, sayap kristal liar, garis piksel pecah. |
| **Eksperimen 2** (Pure Procedural Math from 0) | Menggambar ulang seluruh tubuh menggunakan kode koordinat kotak. | Hasilnya kaku seperti Minecraft / Lego balok, leher menjadi tiang panjang, rambut kehilangan helai organik. |
| **Eksperimen 3** (Dithered Checkerboard) | Menerapkan rumus catur `(x+y)%2` pada lengan. | Menghasilkan noise bintik-bintik yang terbaca seperti kain catur / glitch, bukan es atau perban. |
| **Eksperimen 4** (Perspective Discontinuity) | Memperbaiki arah tanpa memeriksa kesinambungan 360°. | Syal Aina di arah `North` hilang di punggung, membuat putaran karakter patah. |

---

## BAB VI: KESIMPULAN & SINTESIS PENDEKATAN EMAS

Dari semua pembelajaran di atas, pendekatan yang benar-benar berhasil dan stabil adalah **Surgical Organic Sculpting**:
1. **Ambil Baseline Chibi Asli** yang sudah memiliki proporsi tubuh, massa rambut acak, dan siluet organik yang baik.
2. **Koreksi Asimetri Lore secara Deterministik**:
   - Lengan Kiri ➔ 100% Frost Blue (`#99B9E0`, `#4A6FA5`, `#2C4875`).
   - Lengan Kanan ➔ 100% Beige Wraps (`#D7CCC8`, `#A1887F`, `#6D4C41`).
3. **Kunci Kontinuitas 360° Syal Aina**:
   - Melingkar di leher pada `South`, menjuntai di sisi pada `East/West`, dan **menjuntai penuh di tengah punggung pada `North`**.
4. **Bentuk Wajah Melankolis Berbobot**:
   - Menggunakan bayangan alis di bawah poni untuk tatapan terfokus.
5. **Kunci ke Palet Baku The Triad**:
   - Menghilangkan noise/warna liar agar performa render di Godot tajam dan bersih.

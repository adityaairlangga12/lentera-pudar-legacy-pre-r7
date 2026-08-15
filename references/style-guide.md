# Style Guide — Lentera Pudar: Master Visual Standard

Dokumen ini adalah acuan visual baku (*Visual Source of Truth*) untuk seluruh aset visual, teori palet warna, standar pemodelan 3D low-poly, pipeline render pixelation di Godot, dan aset 2D Aseprite pada proyek **Lentera Pudar**.

---

## 1. Resolusi, Rendering, & Perspektif (Jalur B Master Pipeline)

- **Target Tampilan Visual**: Pixel art semi-detailed chibi `32x32 px` dalam sudut pandang `low top-down` (kemiringan kamera 20°–30° Zelda-like).
- **Arsitektur Rendering Karakter (Jalur B)**:
  - Karakter dimodelkan sebagai **3D Low-Poly Mesh di Blender 5.2 LTS** dengan batasan ketat **300–1000 triangle (tris) per karakter**.
  - Anggota badan (lengan/kaki) memiliki minimal 6–8 segmen agar siluet tetap mulus saat diputar ke 8 arah.
  - Shading pada mesh wajib **Flat Shading** (bukan smooth shading) untuk menjaga ketegasan batas warna saat dipixelasi.
  - Di-render di Godot 4.7.1 menggunakan **`Camera3D Orthogonal`** (bukan Perspective) ke dalam **`SubViewport` beresolusi rendah** (misal `320x180` atau `480x270`).
  - Tekstur `SubViewport` di-upscale ke layar menggunakan filter **`Nearest`** (Nearest-Neighbor) dan dilapisi **Toon/Cel-Shader** untuk menghasilkan shading bertingkat khas pixel art otentik.
- **Outline & Ketajaman**:
  - Karakter dibingkai dengan *selective dark outline* (`#141013` / `#000000`) dengan tepi keras (*hard edges, no color bleed*).
  - Seluruh filter texture dan canvas item di-set ke **Nearest** untuk mencegah blur.

---

## 2. Teori & Hierarki Palet Warna (The Triad of Lentera Pudar)

Pewarnaan berakar pada kontras eksistensial antara kehangatan cinta/harapan, dinginnya kepasrahan es, dan kegelapan dungeon purba:

```
                      [ PALET RESMI THE TRIAD ]
   
   🟡 EMBER OF AINA (#F4B860)         🔵 CURSE OF PUDAR (#4A6FA5)
   (Kehangatan, Syal, Altar, Cinta)   (Es Pudar, Tangan Beku, Kepasrahan)
   • Highlight: #FFE0B2               • Highlight: #99B9E0
   • Base:      #F4B860 (PointLight)  • Base:      #4A6FA5 (Shader Pulse)
   • Shadow:    #C58B3E               • Shadow:    #2C4875
   • Deep Rim:  #8C4E18               • Abyss:     #162847
                 \                      /
                  \                    /
                   ▼                  ▼
              🌑 ANCIENT RUINS NEUTRAL (#2A211C)
            (Batu Dungeon, Pakaian Kaelen, CanvasModulate)
            • Highlight: #4A3C34
            • Base:      #2A211C (Atmosfer Dasar)
            • Shadow:    #1A1310
            • Deep Void: #0D0907
```

### Palet Aksen Karakter & Lingkungan (Sub-Palette)
- **Kulit Kaelen**: `#FFE0B2` (Highlight), `#E0A96D` (Base), `#A86F3E` (Shadow).
- **Rambut Abu-Abu Kaelen**: `#E0E0E0` (Kilau), `#9E9E9E` (Abu-Abu Kelana), `#616161` (Bayangan Gelap).
- **Perban Kering Tangan Kanan & Tubuh**: `#D7CCC8` (Highlight), `#A1887F` (Base), `#6D4C41` (Shadow).
- **Kristal Es Tangan Kiri**: `#99B9E0` (Kilau), `#4A6FA5` (Kristal), `#2C4875` (Bayangan Beku).
- **Penutup Mata (*Eyepatch*)**: `#141013` (Hitam Kulit Kering).
- **Tali Selempang Kantung (*Baldric*)**: `#7A4B28` (Kulit Coklat Tua), `#4E2E16` (Bayangan).
- **Lumut Es Reruntuhan (Environment Accent)**: `#3D5A50` / `#5C7F72`.
- **Emas Kuno (Altar & Relik)**: `#D4AF37` / `#C58B3E`.

---

## 3. Anatomi Desain Kaelen (Protagonis V3 Definitif)

- **Rasio Proporsi**: Chibi semi-detailed 1:3 hingga 1:3.5 (Tinggi total ~32 unit di dunia low-poly).
- **Rambut**: Abu-abu acak (*Messy Grey Hair*), sedikit menutupi dahi, memberi kesan pengelana tangguh yang lelah membawa penyesalan.
- **Wajah & Mata**: Mata kiri terbuka fokus melankolis dengan bayangan alis di bawah poni, mata kanan mengenakan **Penutup Mata Kulit Hitam (*Leather Eyepatch* `#141013`)** sebagai segel bekas luka beku Kutukan Pudar masa lalu.
- **Pakaian**: Jubah kelana gelap netral (`#2A211C`) dengan tali selempang kulit kantung bekal (*baldric harness*), tanpa zirah besi berat (kesan *class-less/fragile traveler*).
- **Syal Kuning Aina (`#F4B860`)**: Melingkar di leher dengan juntaian kain panjang di punggung yang dikendalikan oleh *Spring-Damper / Velvet modifier*, memancarkan cahaya `PointLight2D` (2700K).
- **Lengan Kiri Kutukan (`#4A6FA5`)**: Dibalut kristal es biru menyala dan aura beku yang berdenyut live via `CursedHand.gdshader` (merespons *Curse Meter* 0%–100%).
- **Lengan Kanan**: Tangan fisik normal dengan perban pelindung kepalan tangan (`#D7CCC8` / `#A1887F`) untuk pukulan jarak dekat.
- **Pijakan Kaki**: Memiliki bayangan tanah elips dinamis (*Directional Ground Shadow*) di seluruh 8 arah rotasi.

---

## 4. Standar Gerak & Animasi 8-Arah

Karena menggunakan rig 3D low-poly di Blender yang dirender ke Godot:
1. **Locomotion Periodik (Procedural Gait)**:
   - `idle`: Gerak napas halus (*chest breathing*) frekuensi lambat + kibaran lembut ekor syal Aina.
   - `walk`: Model *inverted pendulum* sinusoidal (kaki kiri-kanan phase offset $\pi$, body bob frekuensi 2x) + ayunan inersia syal.
   - `run / dash`: Langkah panjang cepat dengan kemiringan torso ke depan + transisi *PD Controller*.
2. **Aksi Reaktif One-Shot (Keyframe Pose + Easing Curve)**:
   - `attack_punch` (Tangan Kanan): Pukulan lurus fisik cepat dengan easing *ease_out*.
   - `attack_cursed` (Tangan Kiri): Hantaman telapak tangan es dengan kilatan partikel es `#4A6FA5`.
   - `hurt`: Tersentak mundur dengan frame freeze singkat (0.05 detik *hit-stop*).
   - `death`: Berlutut pasrah, kristal es merambat membekukan seluruh tubuh menjadi patung kristal.
- **Konsistensi 8-Arah**: Karena berakar pada rig 3D, seluruh 8 arah kardinal (`south`, `north`, `east`, `west`, `south-east`, `south-west`, `north-east`, `north-west`) memiliki asimetri geometris yang 100% konsisten tanpa distorsi mirroring.

---

## 5. Standar Domain Aseprite: UI, Tileset Dungeon, & FX

Domain Aseprite memegang peranan mutlak untuk elemen 2D murni:

### A. User Interface (UI) & Typography
- **Panel & Box**: Wajib menggunakan teknik **9-Slice Scaling** bertekstur batu dungeon `#2A211C` dengan trim emas kuno `#C58B3E` agar tidak terdistorsi saat di-resize.
- **Bitmap Font**: Font pixel bergaya *Misterius-Hangat Melankolis* dengan keterbacaan tinggi pada resolusi rendah.
- **Icons & HUD**: Simbol lentera, meter kutukan es, dan item inventory berukuran 16x16 / 24x24 px dengan outline solid.

### B. Environment & Dungeon Tilesets
- **Lantai Dungeon Sektor 1**: Ubin batu bata kuno gelap `#2A211C` dengan retakan es halus dan sistem Terrain autotiling bitmask Godot 4.
- **Dinding Dungeon Sektor 1**: Formasi dinding batu berornamen kuno yang ditembus pilar kristal es biru `#4A6FA5` lengkap dengan `LightOccluder2D` polygon.
- **Props**: Patung warga beku hening, Altar Lentera kuno `#D4AF37`, dan obor api padam.

### C. FX / VFX Hard-Edge Pixel Art
- **Tebasan & Flash (Bentuk Grafis Murni)**: Dibuat sebagai **Flipbook Frame-by-Frame di Aseprite** (durasi total 0.2–0.4 detik, peak flash di 0.05–0.1 detik pertama, dibatasi 2–3 warna kontras tinggi). Dilarang keras menggunakan gradient alpha lembut modern.
- **Partikel Ambien (Debu & Serpihan Es)**: Menggunakan `GPUParticles2D` Godot dengan tekstur hard-edge terkuantisasi (2x2 / 4x4 px) dan filter `Nearest`.

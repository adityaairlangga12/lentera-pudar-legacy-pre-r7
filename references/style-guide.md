# Style Guide — Lentera Pudar (2D Pixel RPG Top-Down)

Dokumen ini adalah acuan visual baku untuk seluruh aset pixel art, palet warna, resolusi, dan standar animasi proyek **Lentera Pudar**.

---

## 1. Resolusi & Dimensi Kanvas

- **Grid Dasar Tile & Karakter**: `32x32 px` (semi-detailed).
- **Perspektif**: `low top-down` (sudut pandang 3/4 Zelda-like / RPG 2D klasik).
- **Outline**: `single color black outline` (`#000000` atau `#141013` selective dark outline) dengan `hard edges, no color bleed`.
- **Proporsi Karakter**: Semi-chibi / stylized humanoid. Tinggi kepala ~1/3 hingga ~1/2 dari total tinggi tubuh (12-14px kepala, 18-20px torso & kaki).
- **Ruang Ekspor Spritesheet**: Bingkai kanvas seragam `48x48 px` per frame dengan titik poros (*pivot/anchor*) berada di tengah bawah (`center-bottom` / kaki menyentuh Y: 42-44px).

---

## 2. Palet Warna Baku (The Triad of Lentera Pudar)

Pewarnaan berakar pada kontras antara kehangatan lentera dan dinginnya Kutukan Pudar:

| Elemen Kunci | Kode Hex | Peran Visual | Catatan Implementasi |
|---|---|---|---|
| **Kuning Hangat** | `#F4B860` | Syal Protagonis, Lentera, Api Hangat, Sumber Harapan | Sumber pencahayaan dinamis via `PointLight2D` di Godot. |
| **Biru Dingin (Pudar)** | `#4A6FA5` | Kristal Es, Urat Kutukan Tangan Kiri, Korban Beku | Diperkuat animasi berdenyut dinamis via `ShaderMaterial` di Godot. |
| **Netral Gelap** | `#2A211C` | Dungeon Stone, Bayangan, Pakaian Karakter, CanvasModulate | Suasana atmosfer gelap penentu *mood* dungeon. |

### Palet Turunan Resmi (assets_raw/palet_lentera_pudar.gpl)
- **Kulit Hangat**: `#FFE0B2` (Highlight), `#E0A96D` (Midtone), `#A86F3E` (Shadow).
- **Rambut Abu-Abu Acak**: `#E0E0E0` (Highlight), `#9E9E9E` (Midtone), `#616161` (Shadow).
- **Pakaian Gelap Kelana**: `#423730` (Highlight), `#2A211C` (Base), `#181210` (Deep Shadow).
- **Perban Kering**: `#D7CCC8` (Highlight), `#A1887F` (Base), `#6D4C41` (Shadow).

---

## 3. Sistem 8-Arah Mata Angin (True 8-Way Directions)

Karena menggunakan Pixellab v3, semua 8 arah di-render secara nyata (bukan sekadar flip horizontal):

1. `south` (Menghadap bawah / depan kamera)
2. `north` (Menghadap atas / membelakangi kamera)
3. `east` (Menghadap kanan murni)
4. `west` (Menghadap kiri murni — *rendered*, bukan di-flip agar asimetri tangan kutukan tetap akurat di tangan kiri)
5. `south-east` (Diagonal kanan bawah)
6. `south-west` (Diagonal kiri bawah)
7. `north-east` (Diagonal kanan atas)
8. `north-west` (Diagonal kiri atas)

---

## 4. Standar Animasi & Frame Count

Setiap arah animasi wajib memiliki frame timing baku:

| State Animasi | Frame Count | Framerate (FPS) | Durasi per Frame | Siklus |
|---|---|---|---|---|
| `idle_[arah]` | 4 frames | 8 FPS | 125 ms | Looping (Nafas halus / bobbing leher 1-2px) |
| `walk_[arah]` | 4 frames | 8 FPS | 125 ms | Looping (Walk cycle 4-langkah: Contact, Recoil, Pass, High-point) |
| `attack_[arah]` *(Tahap Lanjut)* | 4-6 frames | 12 FPS | ~83 ms | One-shot |
| `hurt_[arah]` *(Tahap Lanjut)* | 2-3 frames | 10 FPS | 100 ms | One-shot with white flash |

---

## 5. Tata Nama File & Tag Animasi (Naming Convention)

- **File Mentah Aseprite**: `protagonist_[arah].aseprite` (contoh: `protagonist_south.aseprite`).
- **File Export Spritesheet**: `protagonist_[arah].png` dan `protagonist_[arah].json`.
- **Godot Animation Tag**: `[aksi]_[arah]` (contoh: `idle_south`, `walk_south-east`).
- **Resource Godot**: `protagonist.tres` (SpriteFrames gabungan 8 arah).

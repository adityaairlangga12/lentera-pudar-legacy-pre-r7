# Style Guide — Lentera Pudar: Master Visual Standard

Dokumen ini adalah acuan visual baku (*Visual Source of Truth*) untuk seluruh aset pixel art, teori palet warna, standar animasi, desain karakter Kaelen, dan arsitektur lingkungan proyek **Lentera Pudar**.

---

## 1. Resolusi, Framing, & Perspektif

- **Grid Dasar Karakter & Tile**: `32x32 px` (semi-detailed chibi proportion).
- **Perspektif**: `low top-down` (sudut pandang 3/4 Zelda-like / RPG 2D klasik).
- **Outline**: `single color solid black outline` (`#000000` / `#141013` selective dark outline) dengan *hard edges, no color bleed*.
- **Bingkai Ekspor Spritesheet**: Kanvas seragam `48x48 px` per frame dengan titik poros (*pivot/anchor*) berada di tengah bawah (`center-bottom` / kaki menyentuh Y: 42-44px).

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
- **Perban Kering Tangan Kiri**: `#D7CCC8` (Highlight), `#A1887F` (Base), `#6D4C41` (Shadow) + urat biru `#4A6FA5` di sela perban.
- **Lumut Es Reruntuhan (Environment Accent)**: Hijau Lumut Beku `#3D5A50` / `#5C7F72`.
- **Emas Kuno (Altar & Relik)**: `#D4AF37` / `#C58B3E`.

---

## 3. Anatomi Desain Kaelen (Protagonis V3 Definitif)

- **Rambut**: Abu-abu acak (*Messy Grey Hair*), sedikit menutupi dahi, memberi kesan pengelana tangguh yang lelah membawa penyesalan.
- **Wajah & Mata**: Mata kiri terbuka fokus melankolis, mata kanan mengenakan **Penutup Mata Kulit Hitam (*Leather Eyepatch* `#141013`)** sebagai segel bekas luka beku Kutukan Pudar masa lalu.
- **Pakaian**: Jubah kelana gelap netral (`#2A211C`) dengan tali selempang kulit kantung bekal (*baldric harness*), tanpa zirah besi berat (kesan *class-less/fragile traveler*).
- **Syal Kuning Aina (`#F4B860`)**: Melingkar di leher dengan ekor syal panjang melayang dinamis di punggung/bahu sebagai sumber `PointLight2D` dinamis.
- **Lengan Kiri Kutukan (`#4A6FA5`)**: Dibalut kristal es biru menyala dan aura beku yang berdenyut halus via `CursedHand.gdshader`.
- **Lengan Kanan**: Tangan fisik normal dengan perban pelindung kepalan tangan (`#D7CCC8` / `#A1887F`) untuk pukulan jarak dekat.
- **Pijakan Kaki**: Memiliki bayangan tanah elips dinamis (*Directional Ground Shadow*) di seluruh 8 arah rotasi.

---

## 4. Standar Animasi Modern 8-Arah (True 8-Way Cardinal)

Semua 8 arah (`south`, `north`, `east`, `west`, `south-east`, `south-west`, `north-east`, `north-west`) di-render secara nyata:

| Nama Animasi di Godot | Jumlah Frame | Framerate (FPS) | Durasi / Frame | Deskripsi & Nuansa Visual |
|---|---|---|---|---|
| `idle_[arah]` | **6 Frame** | **8 FPS** | 125 ms | Nafas dada halus 1px + kain syal Aina mengayun lembut seperti lidah api. |
| `walk_[arah]` | **6 Frame** | **10 FPS** | 100 ms | Siklus langkah berbobot (*weighty step*) di lantai beku + kibaran syal lentur. |
| `dash_[arah]` | **4 Frame** | **15 FPS** | 66 ms | Badan meluncur tajam ke depan dengan garis bayangan *motion blur*. |
| `attack_punch_[arah]` | **4 Frame** | **12 FPS** | 83 ms | Serangan 1 (Tangan Kanan): Pukulan lurus fisik cepat. |
| `attack_cursed_[arah]` | **5 Frame** | **12 FPS** | 83 ms | Serangan 2 (Tangan Kiri): Hantaman telapak es dengan kilatan partikel biru `#4A6FA5`. |
| `hurt_[arah]` | **3 Frame** | **10 FPS** | 100 ms | Karakter tersentak mundur 2px dengan kilatan putih sesaat. |
| `interact_[arah]` | **4 Frame** | **8 FPS** | 125 ms | Merentangkan tangan menyentuh altar/obor untuk menyalurkan kehangatan. |
| `death_[arah]` | **6 Frame** | **8 FPS** | 125 ms | Berlutut pasrah, urat es merambat membekukan tubuh jadi patung kristal (*one-shot*). |

---

## 5. Standar Lingkungan Sektor 1: Reruntuhan Kristal Beku (*Frozen Ruins*)

- **Lantai Dungeon**: Ubin batu bata kuno gelap `#2A211C` bertekstur retakan dengan lapisan es tipis.
- **Dinding Dungeon**: Formasi dinding batu berornamen kuno yang ditembus pilar kristal es biru `#4A6FA5`.
- **Props Khusus**:
  - **Patung Korban Pudar**: Warga yang membeku dalam pose hening damai.
  - **Altar Lentera Kuno**: Altar batu emas kuno `#C58B3E` tempat menyalakan api pengorbanan.

---

## 6. Formula Baku Prompt PixelLab v3 (Art Director)

```
A 32x32 pixel art low top-down 3/4 perspective RPG male adventurer named Kaelen, messy grey hair, wearing dark travel tunic in neutral dark brown #2A211C, glowing warm yellow scarf #F4B860 wrapped around neck with long flowing scarf tail behind him, left arm wrapped in worn bandages with glowing blue ice crystal veins #4A6FA5 visible on fingers and forearm, right hand is bare with light wrapped fist. Single color solid black outline, clean readable semi-detailed chibi pixel art proportions, no blur, lossless color separation.
```

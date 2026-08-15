# Resep Master Pipeline Kaelen (Standar Baku Pembuatan Karakter Lentera Pudar)

> **Dokumen ini adalah cetak biru teknis (Master Recipe) resmi.** Berisi panduan lengkap, formula prompt PixelLab, skrip pemrosesan kanvas, integrasi Godot, hingga arsitektur pencahayaan. Gunakan dokumen ini sebagai acuan mutlak saat membuat **Kaelen V4** atau karakter/NPC baru lainnya di masa depan.

---

## BAB I: SPESIFIKASI VISUAL & LORE KARAKTER (THE BLUEPRINT)

| Bagian Tubuh | Spesifikasi Visual & Lore | Palet Warna Baku (The Triad) |
|---|---|---|
| **Proporsi & Kanvas** | Chibi semi-detailed RPG, rasio kepala-badan 1:3. Sprite 32x32px di dalam kanvas standar 48x48px. Sudut pandang *Low Top-Down 3/4 (20°–30°)*. | Resolusi 32x32px (Canvas 48x48px) |
| **Rambut** | Abu-abu kelana acak-acakan (*messy gray hair*), poni menutupi dahi dengan helai samping. | `#898D87`, `#9E9E9E`, `#E0E0E0` |
| **Wajah & Mata** | **Mata Kanan**: Mengenakan *eyepatch* kulit hitam sebagai segel penahan kutukan es.<br>**Mata Kiri**: Terbuka tajam, tatapan fokus dan tenang.<br>**Mulut**: Garis bibir tertutup rapat & tegas. | Eyepatch: `#141013`<br>Kulit: `#F4D2B4`, `#DCB18C`, `#B97D5F` |
| **Syal Jiwa Aina** | Syal api kuning emas hangat pengorbanan Aina. Melilit rapat di leher/dada, dengan ekor kain menjuntai melayang ditiup angin. | `#FFE0B2` (Highlight), `#F4B860` (Badan Api), `#C58B3E` (Bayangan), `#8C4E18` (Lipatan) |
| **Pakaian & Torso** | Jubah kelana gelap tanpa kelas (*class-less*) dengan sabuk selempang kulit melintang (*baldric harness*) dan kantung ransel kecil. | Jubah: `#2A211C`, `#1A1310`<br>Sabuk/Kantung: `#7A4B28`, `#4E2E16` |
| **Tangan Kiri (Kutukan)** | Dibalut kristal es Kutukan Pudar yang membeku hingga pergelangan/siku. Memancarkan denyut dingin dan uap es melayang. | `#99B9E0` (Kilau Es), `#4A6FA5` (Kristal Es), `#2C4875` (Bayangan Beku) |
| **Tangan Kanan** | Tangan normal dengan perban kelana putih kusam / sarung tangan kulit. | `#DCD8CD`, `#A8A396` |
| **Kaki & Pijakan** | Celana gelap, boots kelana coklat, dan **Bayangan Tanah Direksional** elips di lantai. | Boots: `#5C3A21`, `#3B2212`<br>Bayangan: `rgba(15, 12, 14, 0.6)` |

---

## BAB II: FORMULA PROMPT BAKU PIXELLAB (MODE V3 32x32PX)

Saat membuat karakter baru / Kaelen V4 via PixelLab API (`create_character`), gunakan struktur prompt teruji berikut:

```text
32x32 pixel art top-down RPG protagonist, classless wanderer male with messy gray hair, black leather eyepatch covering right eye, sharp focused left eye, golden yellow glowing long scarf around neck fluttering in wind, dark wanderer tunic with leather baldric strap harness, cursed left arm and hand frozen in glowing crystalline ice blue, normal right arm with white cloth bandages, grounded boots, low top-down 3/4 perspective, clean solid black outline, Eastward style, Zelda Minish Cap proportions, vibrant colors, no artifacts
```

* **Parameter Generator**:
  - `size`: `32x32px`
  - `view`: `low top-down`
  - `directions`: `8` (south, south-east, east, north-east, north, north-west, west, south-west)

---

## BAB III: ALUR PEMROSESAN ASSET OTOMATIS (CANVAS & PADDING)

```
[ PixelLab 32x32px Raw ]
           │
           ▼ (Download 8 Rotations)
[ Canvas 48x48px Standardization ] ➔ Posisi X=8, Y=8 (Tepat di tengah kanvas)
           │
           ▼ (Sintesis Bayangan Tanah Direksional)
[ Ground Footprint Shadow ]        ➔ South/North: Elips lebar (X:18-30, Y:38-40)
                                   ➔ East/West: Elips ramping (X:20-29, Y:38-40)
                                   ➔ Diagonals: Elips condong 3/4
```

---

## BAB IV: HUKUM ANIMASI IDLE (WHOLE-BODY BREATHING & FLAPPING TAIL)

1. **Prinsip Whole-Body Lift**:
   - Seluruh tubuh atas (dada, kepala, rambut, kedua lengan penuh, dan kerah syal di leher) terangkat **+1 piksel** pada fase menarik napas (Frame 1–3) dan kembali ke baseline pada fase menghembuskan napas (Frame 0, 4, 5).
   - **Kaki dan bayangan tanah 100% terkunci di lantai** (tidak boleh ikut terangkat).
2. **Prinsip Anchored Collar & Flying Tail**:
   - Bagian syal yang melilit leher dan menempel di dada **100% terkunci bersama pernapasan dada**.
   - **HANYA ekor kain yang melayang bebas di udara** yang berkibar naik-turun 1–2 piksel ditiup angin.
3. **Eliminasi Ghost Outlines & White Noise**:
   - Setiap kali menggerakkan ekor syal, seluruh outline hitam (`#141013`) pembungkusnya harus dipindahkan utuh bersama warna kuningnya.
   - Tepi luar kain wajib dibungkus outline hitam padat tanpa ada piksel putih pucat yang bocor.

---

## BAB V: INTEGRASI SISTEM DI GODOT ENGINE 4.7.1

### 1. Struktur Node Karakter (`Player.tscn`)
```text
Player (CharacterBody2D) [z_index = 1]
  ├── AnimatedSprite2D [material = CursedHand.gdshader, sprite_frames = kaelen_v3_frames.tres]
  ├── CollisionShape2D [position = (0, 10), shape = CircleShape2D(radius: 6)]
  ├── ScarfLight (PointLight2D) [position = (0, 4), energy = 0.85, color = #F4B860, scale = 1.6]
  ├── FrostParticles (CPUParticles2D) [position = (-10, 4), amount = 6, direction = (0, -1), color = #99B9E0]
  └── StateMachine (Node) [FSM: Idle, Walk, Dash, AttackPunch, AttackCursed]
```

### 2. Shader Kutukan Es Presisi (`CursedHand.gdshader`)
Wajib menggunakan **Strict Chromatic Dominance Filter** agar rambut abu-abu dan jubah tidak ikut membiru:
```glsl
shader_type canvas_item;

uniform vec4 cursed_color : source_color = vec4(0.29, 0.435, 0.647, 1.0);
uniform float pulse_speed : hint_range(0.1, 5.0) = 2.5;
uniform float intensity : hint_range(0.0, 1.0) = 0.45;

void fragment() {
    vec4 tex_color = texture(TEXTURE, UV);
    // HANYA mendeteksi warna kristal es biru murni
    bool is_frost_crystal = (tex_color.b > tex_color.r + 0.16 && tex_color.b > tex_color.g + 0.04 && tex_color.a > 0.5);
    
    if (is_frost_crystal) {
        float pulse = (sin(TIME * pulse_speed) + 1.0) * 0.5;
        vec3 glow = tex_color.rgb + (vec3(0.2, 0.4, 0.8) * pulse * intensity);
        COLOR = vec4(glow, tex_color.a);
    } else {
        COLOR = tex_color;
    }
}
```

### 3. Pencahayaan Lingkungan Dungeon (`World.tscn`)
- **Lantai Dungeon**: Batuan *slate* dungeon gelap netral (`Color(0.18, 0.19, 0.22, 1)` / `#2A211C`).
- **CanvasModulate**: Netral sejuk (`Color(0.65, 0.65, 0.70, 1)`).
- **Hasil**: Rambut abu-abu Kaelen tetap bersih, tangan es menyala biru tajam, dan syal lentera menerangi dungeon dengan hangat.

---

## BAB VI: SKRIP OTOMASI INTERNAL YANG TERSEDIA

Jika di masa depan ingin me-regenerasi atau membuat versi V4, skrip-skrip berikut sudah siap pakai di folder `tools/`:

| Path Skrip | Fungsi Utama |
|---|---|
| `tools/restore_pristine_kaelen_v3.py` | Mengunduh ulang master raw dari PixelLab dan menempatkannya ke kanvas 48x48 berbayangan. |
| `tools/build_godot_kaelen_v3_spriteframes.py` | Membangun master spritesheet 6-frame 8-arah dan file `kaelen_v3_frames.tres`. |
| `tools/build_godot_showcase_grid.py` | Menjalankan test runner di Godot dan merender screenshot 8 arah resolusi tinggi. |

---

*Dokumen ini resmi ditandatangani sebagai Standar Baku Semesta Lentera Pudar.*

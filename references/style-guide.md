# Style Guide — Lentera Pudar: 3D Action RPG Master Visual Standard

Dokumen ini adalah acuan visual baku (*Visual Source of Truth*) untuk seluruh perancangan aset 3D, teori warna, material PBR/Cel, rigging biomekanik, fisika kain, dan pencahayaan sinematik pada proyek **Lentera Pudar** (Unreal Engine 5 + Blender 5.2 LTS).

---

## 1. Spesifikasi Teknis & Kamera 3D

- **Genre & Gaya Visual**: 3D Third-Person Action-Adventure RPG (Stylized Anime / Poetic Dark Fantasy — Inspirasi: *Final Fantasy VII Remake*, *NieR: Automata*, *Genshin Impact*).
- **Target Platform**: PC Windows (Steam-Ready), Steam Deck, dan Controller Support penuh.
- **Kamera Gameplay**: Kamera 3D Third-Person dinamis (*Over-The-Shoulder / Action Combat*) dengan follow prediktif dan arena locking pada boss fight.
- **Target Performa**: Solid 60 FPS / 120 FPS pada resolusi 1080p, 1440p, dan 4K.

---

## 2. Teori & Hierarki Palet Warna (The Triad 3D)

Seluruh perancangan aset visual 3D, pencahayaan, shader, dan material wajib tunduk pada **Hukum Tiga Warna (The Triad)**:

```
                      [ PALET RESMI THE TRIAD 3D ]
   
   🟡 EMBER OF AINA (#F4B860)         🔵 CURSE OF PUDAR (#4A6FA5)
   (Kehangatan, Syal, Altar, Cinta)   (Es Pudar, Tangan Beku, Kepasrahan)
   • 2700K Kelvin Warm Emissive       • 6500K Kelvin Cold Shard
   • PointLight3D / Lumen Radiance    • Transmissive Crystal Shader
   • Base: #F4B860 (Gold Cloth)       • Core Glow: #4A6FA5 & #7EE8FA
                 \                      /
                  \                    /
                   ▼                  ▼
              🌑 ANCIENT RUINS NEUTRAL (#2A211C)
            (Batu Dungeon, Pakaian Kaelen, Dark Atmosphere)
            • Base: #2A211C (Dark Weathered Cloth)
            • Deep Void: #141013 (Leather Eyepatch & Soles)
```

---

## 3. Anatomi Desain Kaelen (Protagonis 3D Definitif)

- **Proporsi Tubuh**: Atletis proporsional 1:6.8 (Tinggi 1.78m) bergaya *Final Fantasy VII Remake*.
- **Rambut**: Rambut perak-abu berlayer 3D tajam (*spiky anime strands* `#D4D8E2`), membingkai dahi dan penutup mata.
- **Wajah & Mata**: 
  - Mata kiri terbuka fokus melankolis.
  - Mata kanan mengenakan **Penutup Mata Kulit Hitam (*Leather Eyepatch* `#141013`)** dengan gesper perak sebagai segel bekas luka beku.
- **Pakaian**: Jubah kelana usang gelap (`#2A211C`) dengan tali selempang kulit (*baldric harness*) melintang di dada dan gesper perak kuno.
- **Syal Jiwa Aina (`#F4B860`)**: Kerah kain melingkari leher dengan ekor pita 3D yang meliuk dinamis di punggung, ditenagai oleh **Cloth Physics & Spring Bones**, memancarkan cahaya lentera hangat 2700K.
- **Lengan Kiri Kutukan (`#4A6FA5`)**: Dibalut kluster kristal es prisma bersudut tajam (*faceted crystal shards*) dengan taji es di pundak dan siku serta cakar kristal (*crystal talons*).
- **Lengan Kanan**: Lengan berbalut perban spiral pelindung kepalan tangan (`#FAF2EC` / `#D0C4BA`).
- **Sepatu**: Sepatu boot petualang kulit coklat tua (`#5C3218`) dengan sol tebal.

---

## 4. Standar Material & Shading 3D (Blender ➔ UE5)

1. **`Mat_Scarf` (Syal Aina)**:
   - Base Color: `#F4B860` (Warm Gold).
   - Emissive: `#FFD678` (2700K Kelvin, Strength 2.0–3.0).
   - Roughness: 0.45.
2. **`Mat_IceArm` (Lengan Kristal Es)**:
   - Base Color: `#4A7EC4` / `#7EE8FA`.
   - Transmission: 0.75 (Efek Kaca Kristal Transparan).
   - Roughness: 0.12 (Permukaan Kristal Mengkilap).
   - Emissive Core: `#35B5FF` (Strength 3.5).
3. **`Mat_Tunic` (Jubah Kelana)**:
   - Base Color: `#2A211C` (Dark Neutral Canvas).
   - Roughness: 0.80 (Kain Usang Non-Reflektif).
4. **`Mat_Leather` (Sabuk & Boot)**:
   - Base Color: `#5C3218` (Weathered Leather).
   - Roughness: 0.35, Metallic: 0.10.

---

## 5. Standar Rigging Armature & Animasi 3D

1. **Struktur Tulang Biomekanik**:
   - `Root` ➔ `Pelvis` ➔ `Spine_01..03` ➔ `Chest` ➔ `Neck` ➔ `Head`.
   - Rantai Tangan & Kaki lengkap dengan IK (Inverse Kinematics).
   - Rantai Syal: 5-bone chain (`Scarf_01` s.d. `Scarf_05`) terintegrasi dengan simulasi fisika kain.
2. **Set Animasi Utama (Action Combat FSM)**:
   - `Idle`: Napas dada halus + kibasan lembut ekor syal Aina.
   - `Jog / Sprint`: Langkah lari atletis berbobot + ayunan inersia syal.
   - `Punch_Combo_1..3`: Rangkaian pukulan cepat tangan kanan berbalut perban.
   - `Cursed_Ice_Strike`: Hantaman telapak tangan kristal es dengan ledakan partikel uap dingin.
   - `Dash_Evade`: Gerakan menghindar cepat dengan jejak cahaya lentera syal Aina.
   - `Hurt / Death`: Reaksi terkena serangan & pembekuan tubuh menjadi patung kristal es.

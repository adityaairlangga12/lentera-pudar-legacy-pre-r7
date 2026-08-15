# Style Guide Numerik & Visual — Lentera Pudar: 3D Action RPG Master Visual Standard

> **Dokumen Sumber Kebenaran Parameter Numerik & Visual (*Visual & Numerical Source of Truth*)**  
> Menetapkan angka pasti, parameter material PBR, pencahayaan Lumen, simulasi kain, timing animasi, anggaran poligon, dan audio untuk eksekusi presisi tanpa tebakan acak di **Blender 5.2 LTS** dan **Unreal Engine 5**.

---

## DAFTAR ISI
1. [BAB 1: Palet Warna Resmi & Suhu Kelvin](#1-palet-warna-resmi-hex--suhu-kelvin)
2. [BAB 2: Parameter Material PBR & Subsurface Scattering (SSS)](#2-parameter-material-pbr--subsurface-scattering-sss)
3. [BAB 3: Parameter Emissive Real-Time (Material Parameter Collection)](#3-parameter-emissive-real-time-material-parameter-collection)
4. [BAB 4: Parameter Simulasi Kain (Chaos Cloth & Spring Bones)](#4-parameter-simulasi-kain-chaos-cloth--spring-bones)
5. [BAB 5: Parameter Pencahayaan Lumen & Chiaroscuro](#5-parameter-pencahayaan-lumen--chiaroscuro)
6. [BAB 6: Budget Poligon (Poly Count) & Hierarki LOD](#6-budget-poligon-poly-count--hierarki-lod)
7. [BAB 7: Parameter Kamera 3D & Easing Curves](#7-parameter-kamera-3d--easing-curves)
8. [BAB 8: Parameter Timing Kombat & Kinematika](#8-parameter-timing-kombat--kinematika)
9. [BAB 9: Parameter Sistem Curse Meter](#9-parameter-sistem-curse-meter)
10. [BAB 10: Parameter Audio & Dynamic Ducking](#10-parameter-audio--dynamic-ducking)
11. [BAB 11: Anatomi Kaelen & Rigging Biomekanik](#11-anatomi-kaelen--rigging-biomekanik)

---

## 1. Palet Warna Resmi (Hex + Suhu Kelvin)

### A. Warna Inti (The Triad of Lentera Pudar)
| Elemen | Kode Hex | Suhu Kelvin | Peruntukan & Catatan |
|---|---|---|---|
| **Syal Jiwa Aina (Base)** | `#F4B860` | 2700K | Warna inti cahaya hangat, kain syal emas. |
| **Kristal Es Kutukan (Dasar)** | `#4A6FA5` | 6500K | Warna dasar es non-emissive pada lengan Kaelen dan dungeon. |
| **Kristal Es Kutukan (Highlight/Emissive)** | `#7EE8FA` | 6500K | Rim light & emissive accent, intensitas terhubung ke *Curse Meter*. |
| **Jubah Kelana Kaelen** | `#2A211C` | — | Base color kain jubah usang gelap, non-emissive. |
| **Eyepatch Kaelen** | `#141013` | — | Kulit hitam tersamak non-reflektif pada mata kanan. |

### B. Warna Turunan Resmi (Standardisasi Sekunder)
| Elemen | Kode Hex | Suhu Kelvin | Peruntukan & Catatan |
|---|---|---|---|
| **Kulit Kaelen (Base Skin)** | `#D8B79A` | — | Undertone hangat alami untuk mencegah *uncanny valley* (Teori 15.F). |
| **Rambut Perak Kaelen** | `#C9CDD1` | — | Rona kebiruan netral halus, bukan putih murni agar tidak *blown-out*. |
| **Perban Pelindung Tangan Kanan** | `#FAF2EC` / `#D0C4BA` | — | Kain perban spiral pelindung kepalan tangan. |
| **Reruntuhan Batu Dungeon (Base)** | `#5C5A55` | — | Abu-abu batu hangat netral sebagai kanvas kontras cahaya. |
| **Reruntuhan Batu (Area Beku/Lembab)** | `#4A5A63` | — | Semburat biru dingin di area yang terpapar kutukan. |
| **Partikel Bisikan Jiwa Beku** | `#8FA9C4` | 7000K | Pendaran partikel bisikan arwah, sedikit lebih dingin dari kristal utama. |
| **Sepatu Boot Kaelen** | `#5C3218` | — | Kulit coklat tua tebal petualang. |
| **Teks UI & Subtitle** | `#F2E9DC` | — | Putih-gading hangat, kontras tinggi di atas latar gelap. |
| **Latar Kotak Subtitle (HUD Box)** | `#0D0D0F` @ 65% | — | Opacity 65% untuk keterbacaan optimal tanpa menghalangi visual. |

### C. Aturan Kontras & Desaturasi Sektor
- **Rasio Kontras Keterbacaan**: Minimal **4.5:1** antara sumber hangat (Aina/UI) dan latar gelap dungeon (standar WCAG AA).
- **Kurva Desaturasi Global Post-Process**:
  - Sektor 1 (*The Silent Crypts*): **100%** saturasi warna.
  - Sektor 2 (*The Blazing Frost*): **85%** saturasi.
  - Sektor 3 (*The Hall of Mirrors*): **70%** saturasi.
  - Sektor 4 (*The Abyss of Stillness*): **40–50%** saturasi (puncak kepasrahan & mati rasa visual).
  - Sektor 5 (*The Dawning Altar*): Rebound bertahap ke **100%** saat fajar terbit.

---

## 2. Parameter Material PBR & Subsurface Scattering (SSS)

| Material | Base Color | Roughness | Metallic | SSS Radius / Scattering Color |
|---|---|---|---|---|
| **Kristal Es Kaelen (`M_Cursed_Crystal`)** | `#4A6FA5` | 0.15–0.30 | 0.0 | Radius: 0.5–1.2 cm, Scatter Color: `#7EE8FA` |
| **Es Dekoratif Dungeon** | `#4A6FA5` | 0.25–0.40 | 0.0 | Roughness lebih tinggi agar tidak mencuri fokus hero |
| **Kain Jubah Kaelen (`M_Tunic`)** | `#2A211C` | 0.55–0.70 | 0.0 | — (Kain kasar tebal) |
| **Kain Syal Aina (`M_Aina_Scarf`)** | `#F4B860` | 0.35–0.50 | 0.0 | Subsurface Cloth Shading aktif |
| **Kulit Eyepatch (`M_Leather_Dark`)** | `#141013` | 0.60–0.75 | 0.0 | Kulit doff tersamak |
| **Batu Reruntuhan (`M_Stone_Ruins`)** | `#5C5A55` | 0.70–0.85 | 0.0 | Tekstur batu kuno berpori |
| **Logam Zirah Boss (Lord Alden dkk)** | Variatif | 0.25–0.45 | 0.7–0.9 | Baja berkarat/es menempel |
| **Sepatu Boot (`M_Leather_Brown`)** | `#5C3218` | 0.35 | 0.10 | Kulit sol tebal |

---

## 3. Parameter Emissive Real-Time (Material Parameter Collection)

Shader kristal es terhubung secara dinamis ke parameter `Curse_Spread` pada *Material Parameter Collection* (MPC):

| Rentang Curse Meter | Status Karakter | Intensitas Emissive | Karakteristik Visual |
|---|---|---|---|
| **0–25%** | Tenang / Aman | 0.5–1.0 | Pendaran `#7EE8FA` redup stabil pada cakar. |
| **26–60%** | Waspada | 1.5–3.0 | Pendaran `#7EE8FA` sedang mulai merambat ke siku. |
| **61–90%** | Bahaya | 4.0–6.0 | Es merambat ke bahu, berdenyut pelan (**Pulse: 0.8–1.2 Hz**). |
| **91–100% (Surge)** | Kritis / Ledakan Es | 8.0–12.0 | Campuran pendaran putih 10–15%, berdenyut cepat (**Pulse: 2.0–3.0 Hz**). |

---

## 4. Parameter Simulasi Kain (Chaos Cloth & Spring Bones)

| Parameter Fisika | Syal Aina (`M_Aina_Scarf`) | Jubah Kaelen (`M_Tunic`) |
|---|---|---|
| **Stiffness (Kekakuan)** | 0.4–0.6 (Lentur & meliuk ringan) | 0.6–0.8 (Tebal & berbobot inersia) |
| **Damping (Peredam)** | 0.3–0.5 | 0.5–0.7 |
| **Solver Iterations** | 8–12 iterasi | 6–10 iterasi |
| **Wind Response Multiplier** | 1.2x (Sangat reaktif karena "hidup") | 0.8x (Pasif mengikuti gravitasi) |
| **Pinning Points** | Melingkar penuh di leher (Neck ring fixed) | Bahu kiri & kanan (2 titik tetap) |

> **Protokol Uji Wajib**: Wajib disimulasikan pada kecepatan gerak $0\text{ cm/s}$ (Idle), $150\text{ cm/s}$ (Jog), $400\text{ cm/s}$ (Sprint), dan saat *Evade Dash* tanpa mengalami clipping parah menembus mesh tubuh.

---

## 5. Parameter Pencahayaan Lumen & Chiaroscuro

| Sumber Cahaya | Suhu Kelvin | Intensitas (Lumen) | Radius / Attenuation |
|---|---|---|---|
| **Syal Aina (PointLight Melekat)** | 2700K | 800–1200 lm (Baseline) | Radius 3.0–5.0m (Menyusut ke 1.5–2.5m di Sektor 4) |
| **Kristal Es Kaelen (Rim Light)** | 6500K | 200–600 lm (Proporsional Curse) | Radius 1.0–2.0m |
| **Ambient Dungeon (Fill Light)** | 6000–6500K | 50–150 lm (Sangat redup) | Menyebar luas (*soft ambient fill*) |
| **Altar Duka & Arena Bos** | Variatif | 400–1000 lm | Disesuaikan dengan skala ruang arena |

### Rasio Kontras Cahaya (Chiaroscuro)
- **Sektor 1–3**: Rasio Key Light (Syal) terhadap Ambient Dungeon minimal **8:1**.
- **Sektor 4 (Depression)**: Rasio naik menjadi **12:1 atau lebih** untuk mempertegas isolasi emosional.

---

## 6. Budget Poligon (Poly Count) & Hierarki LOD

| Kategori Aset 3D | Target Tris (LOD0) | Jumlah Level LOD | Karakteristik Pipeline |
|---|---|---|---|
| **Hero Character (Kaelen)** | 40,000–60,000 tris | LOD0 s.d. LOD3 (4 level) | Deformable Skeletal Mesh |
| **Aina (Wujud Visual Terpisah)** | 20,000–35,000 tris | LOD0 s.d. LOD2 (3 level) | Cloth Simulation Enabled |
| **Boss Sektor (Lord Alden dkk)** | 50,000–80,000 tris | LOD0 s.d. LOD3 (4 level) | Custom Armature & Cloth |
| **Musuh Umum (Jiwa Beku)** | 8,000–15,000 tris | LOD0 s.d. LOD2 (3 level) | Instanced Skeletal Mesh |
| **Prop Besar (Reruntuhan, Altar)** | 15,000–30,000 tris | Nanite-Enabled | Nanite Auto-LOD |
| **Prop Kecil (Puing, Kristal Es)** | 500–3,000 tris | LOD0 s.d. LOD1 | Static Mesh Instancing |

---

## 7. Parameter Kamera 3D & Easing Curves

| Mode Kamera | Field of View (FOV) | Jarak Kamera ke Hero | Framing Offset |
|---|---|---|---|
| **Eksplorasi Default** | 75°–85° | 3.8–4.5 Meter | Sedikit di atas pundak kanan |
| **Duel Lock-On / Boss Fight** | 70° | 2.6–3.0 Meter | Over-the-shoulder rapat ala Hellblade |
| **Close-Up Naratif (Altar Duka)** | 35°–50° | 1.2–1.8 Meter | Fokus ekspresi wajah Kaelen |
| **Boss Intro Cinematic** | 40°–60° | Dinamis | Rule of Space (Boss tampak dominan) |

### Transisi Kamera & Collision Buffer
- **Kurva Transisi**: `Ease-in-Out Cubic` dengan durasi blend **0.4 s.d. 0.8 detik**.
- **Collision Avoidance Buffer**: Jarak minimum kamera ke dinding batu **15–25 cm** sebelum kamera otomatis maju.

---

## 8. Parameter Timing Kombat & Kinematika

> *Catatan: Angka di bawah menggunakan basis 30fps (dikalikan 2x pada 60fps runtime).*

| Aksi Kombat | Startup (Anticipation) | Active Window | Recovery |
|---|---|---|---|
| **Light Punch Combo (Per Hit)** | 3–5 frame ($0.10–0.16\text{s}$) | 4–6 frame ($0.13–0.20\text{s}$) | 6–10 frame ($0.20–0.33\text{s}$) |
| **Heavy Cursed Strike** | 12–18 frame ($0.40–0.60\text{s}$) | 6–8 frame ($0.20–0.26\text{s}$) | 15–20 frame ($0.50–0.66\text{s}$) |
| **Evade Dash** | 2–4 frame (Sangat responsif) | 8–10 frame (**i-frames aktif**) | 4–6 frame ($0.13–0.20\text{s}$) |
| **Parry Stance Window** | — | **4–6 frame (8–12f @60fps)** | 8–12 frame jika gagal tangkis |
| **Hit-Stop (Impact Freeze)** | — | **3 frame (0.05 detik)** | Jeda tabrakan pukulan nyata |

---

## 9. Parameter Sistem Curse Meter

| Parameter Sistem | Nilai Numerik Baseline |
|---|---|
| **Kapasitas Maksimum** | 100 Poin (Skala internal diegetik) |
| **Kenaikan per Hit Musuh** | +8 s.d. +15 Poin (Tergantung berat serangan) |
| **Penurunan Alami (Decay)** | -2 s.d. -4 Poin / detik saat tidak terkena hit |
| **Buka Eyepatch (Perception)** | +3 Poin / detik selama penutup mata terbuka |
| **Ambang Bahaya (*Danger Threshold*)** | 61 Poin (Vignette dingin & denyut es aktif) |
| **Ambang Surge Siap Pakai** | 90 Poin (Bisa picu ledakan es cakar) |
| **Durasi Mode Surge** | 6–10 Detik |
| **Penalti Pasca Surge (Fatigue)** | Meter reset ke 20 Poin, damage output Kaelen turun -15% selama 5 detik |

---

## 10. Parameter Audio & Dynamic Ducking

| Elemen Audio | Target Loudness | Karakteristik & Aturan Ducking |
|---|---|---|
| **Musik Latar (Eksplorasi)** | -20 LUFS | Layering dasar instrumen hangat/dingin |
| **Musik Kombat (Layer Penuh)** | -16 LUFS | Target standar media interaktif (Teori 18.C) |
| **Dialog / Bisikan Jiwa Beku** | -18 LUFS | **Ducking musik -6dB** (Attack: 150ms, Release: 400ms) |
| **SFX Pukulan & Es Pecah** | Peak -3 dB | Menghindari digital clipping |
| **Ambience Derit Es & Angin** | -28 s.d. -24 LUFS | Sangat halus di bawah audio narasi |

---

## 11. Anatomi Kaelen & Rigging Biomekanik

- **Tinggi & Proporsi**: Tinggi 1.78m, proporsi 1:6.8 atletis bergaya *FF7 Remake / Kena*.
- **Hierarki Armature Utama**:
  - `Root` ➔ `Pelvis` ➔ `Spine_01..03` ➔ `Chest` ➔ `Neck` ➔ `Head`.
  - **Lengan Kiri**: `Clavicle_L` ➔ `UpperArm_L` ➔ `Forearm_L` ➔ `Hand_L` ➔ `Talon_01..05` (Rig cakar es).
  - **Lengan Kanan**: `Clavicle_R` ➔ `UpperArm_R` ➔ `Forearm_R` ➔ `Hand_R` ➔ `Fingers_R` (Rig jari berban).
  - **Rantai Syal**: Rantai 5-bone (`Scarf_01` s.d. `Scarf_05`) dengan parameter *Spring-Damper* (Stiffness: **0.4–0.6**, Damping: **0.3–0.5**) — konsisten dengan Bab 4 Simulasi Kain.

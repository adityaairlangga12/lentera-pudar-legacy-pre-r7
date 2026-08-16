---
name: blender_3d_mastery
description: "Pustaka keahlian pemodelan 3D High-Detail di Blender 5.2 LTS, topologi berorientasi deformasi, UV seam, hierarki armature rigging biomekanik, konsistensi bone roll, PBR & cel materials The Triad, cloth physics syal, ekspor glTF/FBX deterministik, kepatuhan SOP 1/3/4, dan kurasi reference board."
---

# Blender 5.2 LTS 3D High-Detail Mastery & UE5 Pipeline

Skill ini memuat seluruh standar teknis pemodelan 3D, topologi deformasi, penempatan UV seam, rigging biomekanik, shading PBR, baking pipeline, dan ekspor aset karakter/lingkungan untuk semesta 3D Action RPG *Lentera Pudar* merujuk pada [expert-3d-foundations.md](file:///d:/GodotProjects/Lentera-Pudar/references/expert-3d-foundations.md), [style-guide.md](file:///d:/GodotProjects/Lentera-Pudar/references/style-guide.md), [anatomy-kinesiology.md](file:///d:/GodotProjects/Lentera-Pudar/references/anatomy-kinesiology.md), [additional-techniques.md](file:///d:/GodotProjects/Lentera-Pudar/references/additional-techniques.md), [api-cheat-sheet.md](file:///d:/GodotProjects/Lentera-Pudar/references/api-cheat-sheet.md), prosedur kerja [sop-workflow.md](file:///d:/GodotProjects/Lentera-Pudar/references/sop-workflow.md), dan riset teknis [kena-art-research.md](file:///d:/GodotProjects/Lentera-Pudar/references/kena-art-research.md).

---

## 1. Standar Pemodelan Karakter & Teori Topologi (Hero Proportions 1:6.8 — SOP 1 & SOP 3)
- **Kaelen**: Tinggi 1.78m, proporsi atletis 1:6.8 bergaya *Final Fantasy VII Remake / Kena Grade*.
- **Prinsip Topologi & Deformasi**:
  - *Edge Flow Organik*: Edge loops wajib melingkari kelompok otot dan lipatan sendi aktif (siku, lutut, deltoid, kelopak mata, mulut).
  - *Quad Dominance*: Wajib 100% Quad pada area bergerak; N-gon dilarang keras pada area deformasi.
  - *Alokasi Pole*: Pole 3/5-edge wajib dialihkan ke area statis berdeformasi rendah (belakang kepala, ketiak); dilarang di lipatan sendi.
- **Poly Budget & Texel Density**:
  - Target **40,000–60,000 tris** untuk Hero LOD0 ($15.000–30.000$ deform base mesh).
  - **Texel Density Baku**: $512\text{ px/m}$ untuk Kaelen & Boss, $256\text{ px/m}$ untuk Prop Lingkungan.
- **Titik Rujukan Tulang Baku (Bony Landmarks Wajib Terbaca)**:
  - *Acromion & Clavicle* (Bahu), *Olecranon* (Siku), *Iliac Crest & Greater Trochanter* (Panggul), *Patella* (Lutut), *Malleolus* (Mata Kaki), dan *Vertebra Prominens* (Pangkal Leher).
- **Lengan Kiri**: Kluster kristal es prisma bersudut tajam (*faceted crystal shards*) dengan taji kristal di deltoid, siku, dan cakar es (`#4A6FA5` & `#7EE8FA`).
- **Lengan Kanan**: Balutan perban spiral bersilang (*cross-wrapped bandages* `#FAF2EC`).
- **Kepala & Wajah**: Kulit `#D8B79A` (undertone hangat SSS anti-uncanny), penutup mata kulit hitam `#141013` pada mata kanan.
- **Hybrid Hair System (Kena Benchmark)**:
  - *Solid Geometry Base*: Gumpalan massa volume utama rambut perak Kaelen (`#C9CDD1`) untuk siluet tegas dan highlight tajam.
  - *Alpha Cards*: Strip poligon helai transparan di lapisan luar untuk ketidakteraturan alami (*flyaway imperfections*).
- **Pakaian**: Jubah kelana usang gelap `#2A211C` dengan sabuk baldric melintang di dada dan gesper perak.
- **Syal Jiwa Aina**: Kerah kain emas `#F4B860` di leher dengan ekor pita meliuk dinamis (*flowing S-curve ribbon*).

---

## 2. Standar UV Unwrapping & Pipeline Baking Presisi
- **Penempatan Seam Tersembunyi**: Tempatkan garis potong UV di sisi dalam lengan, bawah selangkangan, dan sambungan batas material alami untuk meminimalkan distorsi.
- **Tangent Space Normal Baking**: Selalu gunakan Tangent Space Normal Map dengan **Cage Mesh** (ekstrusi ray-casting halus) untuk transfer detail High-Poly ke Low-Poly tanpa artefak robek.
- **Baking AO Mikro vs Lumen GI**: Batasi baking Ambient Occlusion hanya pada celah mikro (pori kain, ukiran runik); hindari baking AO skala makro agar tidak bentrok dengan Lumen real-time.

---

## 3. Standar Rigging Armature, Biomekanik & Dual-Mode Scarf (SOP 3)
- **Hierarki Skeletal**: `Root` ➔ `Pelvis` ➔ `Spine_01..03` ➔ `Chest` ➔ `Neck` ➔ `Head`.
- **Integritas Skinning Weight**:
  - Total bobot per vertex $= 1.0$ ($100\%$) dengan maksimal 4 bone influences per vertex.
  - Blending gradual pada lipatan sendi untuk mencegah *pinching*.
- **Rigging Wajah & FACS Blend Shapes (SOP 3)**:
  - Setup Shape Keys per Action Unit (`AU1`, `AU4`, `AU6`, `AU12`, `AU15`, `AU17`, `AU23`, `AU43`).
  - Pemisahan independen antara *Eye Region* dan *Mouth Region* untuk ekspresi duka tertahan.
  - Duchenne Marker (`AU6+AU12`) untuk senyum tulus vs Senyum topeng sosial (`AU12` tanpa `AU6`).
  - Asimetri 5–15% dan ekspresi mikro 1/25–1/5 detik.
  - Batasan rotasi rahang bawah (mandibula pitch $0^\circ–20^\circ$).
- **Scarf Spring Bones (Dual-Mode)**: Rantai 5-bone (`Scarf_01` s.d. `Scarf_05`) dengan parameter *Spring-Damper* (Stiffness: 0.4–0.6, Damping: 0.3–0.5) — beralih mulus antara Chaos Cloth (gameplay) dan Hand-Keyframed Control Rig (cutscene naratif).
- **Corrective Shape Keys (Pose-Driven Morphs)**:
  - Setup morph koreksi volume lipatan siku 140° (+ Muscle Bulge bisep), bahu elevasi, lutut fleksi 140°, dan kerutan dahi glabella (`AU1+AU4`).
- **Batasan Rotasi Sendi (Joint Limits)**:
  - Siku (0°–145° anti-hyperextension), Lutut (0°–140° fleksi belakang), Tulang Belakang ($\pm 35^\circ–45^\circ$), Leher ($\pm 80^\circ$ yaw).

---

## 4. Shading & Material The Triad 3D (SOP 2 — Zero Black Outline)
- **Syal Aina (`Mat_Scarf`)**: Emissive Warm Gold (`#F4B860` 2700K Kelvin, Roughness 0.35–0.50, Subsurface Cloth).
- **Lengan Kristal Es (`Mat_IceArm`)**: Radiant Cold Cyan/Blue (`#4A6FA5` & `#7EE8FA` 6500K Kelvin, Transmission 0.75, Roughness 0.15–0.30, SSS Radius 0.5–1.2cm scatter `#7EE8FA`).
- **Jubah Kelana (`Mat_Tunic`)**: Dark Ancient Robe (`#2A211C` / `#141013`, Roughness 0.55–0.70 dengan micro-weathering).
- **Sabuk & Sepatu (`Mat_Leather`)**: Rich Brown Leather (`#5C3218`, Roughness 0.35, Metallic 0.10).
- **PBR Integrity**: Albedo murni tanpa baked shadow/lighting; Metallic biner 0 atau 1.

---

## 5. Ekspor ke Unreal Engine 5 (Epic Games Pipeline Plugin)
- **Sumbu**: $+Z$ Forward / $+Y$ Up. Skala $1\text{ unit} = 1\text{ cm}$.
- **Transform**: Apply all transforms (`Location=(0,0,0)`, `Rotation=(0,0,0)`, `Scale=(1,1,1)`) sebelum ekspor.
- **Metode Ekspor**: Blender-Unreal Pipeline Plugin ("Send to Unreal") atau FBX deterministik.
- **Self-Critique Benchmark**: Validasi hasil ekspor merujuk ke [few-shot-calibration.md](file:///d:/GodotProjects/Lentera-Pudar/references/few-shot-calibration.md) Contoh 1, 3, & 7.

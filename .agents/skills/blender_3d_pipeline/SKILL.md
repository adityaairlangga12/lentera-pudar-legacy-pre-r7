---
name: blender_3d_pipeline
description: "Pustaka keahlian pemodelan 3D High-Detail di Blender 5.2 LTS, topologi berorientasi deformasi, UV seam, hierarki armature rigging biomekanik, konsistensi bone roll, PBR & cel materials The Triad, cloth physics syal, ekspor glTF/FBX deterministik, kepatuhan SOP 1/3/4, dan kurasi reference board."
---

# Blender 5.2 LTS 3D High-Detail & UE5 Asset Pipeline

Skill ini memuat seluruh standar teknis pemodelan 3D, topologi deformasi, penempatan UV seam, rigging biomekanik, shading PBR, baking pipeline, dan ekspor aset karakter/lingkungan untuk semesta 3D Action RPG *Lentera Pudar* merujuk pada [3d-asset-pipeline.md](file:///d:/GodotProjects/Lentera-Pudar/references/04-art-3d/3d-asset-pipeline.md), [style-guide.md](file:///d:/GodotProjects/Lentera-Pudar/references/04-art-3d/style-guide.md), [anatomy-kinesiology.md](file:///d:/GodotProjects/Lentera-Pudar/references/04-art-3d/anatomy-kinesiology.md), [environment-modular-techniques.md](file:///d:/GodotProjects/Lentera-Pudar/references/04-art-3d/environment-modular-techniques.md), [api-cheat-sheet.md](file:///d:/GodotProjects/Lentera-Pudar/references/06-pipeline-qc/api-cheat-sheet.md), prosedur kerja [sop-workflow.md](file:///d:/GodotProjects/Lentera-Pudar/references/06-pipeline-qc/sop-workflow.md), dan riset teknis [kena-art-research.md](file:///d:/GodotProjects/Lentera-Pudar/references/04-art-3d/kena-art-research.md).

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
- **Lengan Kiri (Tri-Layer Biomechanical Shingling)**:
  - Layer 1: Daging bawah smooth skinning dengan SSS dan denyut urat es reaktif (`Curse_Spread`).
  - Layer 2: Kluster prisma kristal es utama di humerus dan radius/ulna di-weight 100% kaku (rigid) tanpa gradient falloff.
  - Layer 3 (Olecranon Shingle System): Lempeng kristal siku bertingkat geologis (*interlocking shingles*) yang meluncur masuk di bawah prisma lain saat fleksi siku $\ge 90^\circ$ (anti-rubbery deformation).
- **Lengan Ranan**: Balutan perban spiral bersilang (*cross-wrapped bandages* `#FAF2EC`).
- **Kepala & Wajah**: Kulit `#D8B79A` (undertone hangat SSS anti-uncanny), penutup mata kulit hitam `#141013` pada mata kanan.
- **Hybrid Hair System (Kena Benchmark)**:
  - *Solid Geometry Base*: Gumpalan massa volume utama rambut perak Kaelen (`#C9CDD1`) untuk siluet tegas dan highlight tajam.
  - *Alpha Cards*: Strip poligon helai transparan di lapisan luar untuk ketidakteraturan alami (*flyaway imperfections*).
- **Pakaian**: Jubah kelana usang gelap `#2A211C` dengan sabuk baldric melintang di dada dan gesper perak.
- **Syal Jiwa Aina (Modular Scarf System)**:
  - Empat variasi panjang syal (`SK_Scarf_Stage1` 180cm s.d. `SK_Scarf_Stage4` 10cm) berbagi skeleton rig 5-bone yang sama (`scarf_01..05`).

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
- **Scarf Spring Bones (Dual-Mode)**: Rantai 5-bone (`Scarf_01` s.d. `Scarf_05`) dengan parameter *Spring-Damper* (Stiffness: 0.4–0.6, Damping: 0.3–0.5) — beralih mulus antara Chaos Cloth (gameplay) dan Hand-Keyframed Control Rig (cutscene naratif) dengan *5-frame Pre-Roll Physics Warm-Up*.
- **Corrective Shape Keys (Pose-Driven Morphs)**:
  - Setup morph koreksi volume lipatan siku 140° (+ Muscle Bulge bisep), bahu elevasi, lutut fleksi 140°, dan kerutan dahi glabella (`AU1+AU4`).
- **Batasan Rotasi Sendi (Joint Limits)**:
  - Siku (0°–145° anti-hyperextension), Lutut (0°–140° fleksi belakang), Tulang Belakang ($\pm 35^\circ–45^\circ$), Leher ($\pm 80^\circ$ yaw).

---

## 4. Shading & Material The Triad 3D (SOP 2 — Zero Black Outline)
- **Stylized-Realistic PBR non-outline**: Tidak menggunakan cel-shading outline hitam (meniru standar visual *Kena: Bridge of Spirits*).
- **Shader Kristal Es Kutukan**:
  - PBR Transmissive Glass/Ice dengan Subsurface Scattering (SSS Radius 0.5–1.2cm).
  - Emissive glow biru dingin 6500K terkontrol melalui parameter scalar `Curse_Spread` ($0.0–1.0$).
- **Shader Kain Syal Emas Aina**:
  - Warna dasar `#F4B860` dengan pendaran emissive lembut 2700K (Lumen GI).

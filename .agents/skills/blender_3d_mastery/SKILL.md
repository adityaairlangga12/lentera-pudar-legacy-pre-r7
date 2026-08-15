---
name: blender_3d_mastery
description: "Pustaka keahlian pemodelan 3D High-Detail di Blender 5.2 LTS, hierarki armature rigging biomekanik, konsistensi bone roll, PBR & cel materials The Triad, cloth physics syal, dan ekspor glTF/FBX deterministik ke Unreal Engine 5."
---

# Blender 5.2 LTS 3D High-Detail Mastery & UE5 Pipeline

Skill ini memuat seluruh standar teknis pemodelan 3D, rigging, material, dan ekspor aset karakter/lingkungan untuk semesta 3D Action RPG *Lentera Pudar* merujuk pada [style-guide.md](file:///d:/GodotProjects/Lentera-Pudar/references/style-guide.md).

---

## 1. Standar Pemodelan Karakter 3D (Hero Proportions 1:6.8)
- **Kaelen**: Tinggi 1.78m, proporsi atletis 1:6.8 bergaya *Final Fantasy VII Remake / Kena*.
- **Poly Budget**: Target **40,000–60,000 tris** untuk Hero LOD0 ($15.000–30.000$ deform base mesh).
- **Lengan Kiri**: Kluster kristal es prisma bersudut tajam (*faceted crystal shards*) dengan taji kristal di deltoid, siku, dan cakar es.
- **Lengan Kanan**: Balutan perban spiral bersilang (*cross-wrapped bandages* `#FAF2EC`).
- **Kepala & Wajah**: Kulit `#D8B79A` (undertone hangat anti-uncanny), penutup mata kulit hitam `#141013` pada mata kanan, rambut perak `#C9CDD1` berlayer tajam (*spiky anime strands*).
- **Pakaian**: Jubah kelana usang gelap `#2A211C` dengan sabuk baldric melintang di dada dan gesper perak.
- **Syal Jiwa Aina**: Kerah kain emas `#F4B860` di leher dengan ekor pita meliuk dinamis (*flowing S-curve ribbon*).

---

## 2. Standar Rigging Armature & Bone Hierarchy
- **Root**: `Root` (Z=0 pada pivot telapak kaki).
- **Spine**: `Pelvis` ➔ `Spine_01` ➔ `Spine_02` ➔ `Chest` ➔ `Neck` ➔ `Head`.
- **Left Arm**: `Clavicle_L` ➔ `UpperArm_L` ➔ `Forearm_L` ➔ `Hand_L` ➔ `Talon_01..05` (5 cakar kristal).
- **Right Arm**: `Clavicle_R` ➔ `UpperArm_R` ➔ `Forearm_R` ➔ `Hand_R` ➔ `Fingers_R`.
- **Legs**: `Thigh_L/R` ➔ `Calf_L/R` ➔ `Foot_L/R` ➔ `Toe_L/R` (IK Foot setup ready).
- **Scarf Spring Bones**: Rantai 5-bone (`Scarf_01` s.d. `Scarf_05`) dengan parameter *Spring-Damper* (Stiffness: 0.4–0.6, Damping: 0.3–0.5).

---

## 3. Shading & Material The Triad 3D
- **Syal Aina (`Mat_Scarf`)**: Emissive Warm Gold (`#F4B860` 2700K Kelvin, Roughness 0.35–0.50, Subsurface Cloth).
- **Lengan Kristal Es (`Mat_IceArm`)**: Radiant Cold Cyan/Blue (`#4A6FA5` & `#7EE8FA` 6500K Kelvin, Transmission 0.75, Roughness 0.15–0.30, SSS Radius 0.5–1.2cm scatter `#7EE8FA`).
- **Jubah Kelana (`Mat_Tunic`)**: Dark Ancient Robe (`#2A211C` / `#141013`, Roughness 0.55–0.70).
- **Sabuk & Sepatu (`Mat_Leather`)**: Rich Brown Leather (`#5C3218`, Roughness 0.35, Metallic 0.10).

---

## 4. Ekspor glTF 2.0 / FBX ke Unreal Engine 5
- **Sumbu**: $+Z$ Forward / $+Y$ Up. Skala $1\text{ unit} = 1\text{ cm}$.
- **Transform**: Apply all transforms (`Location=(0,0,0)`, `Rotation=(0,0,0)`, `Scale=(1,1,1)`) sebelum ekspor.
- **Format**: glTF 2.0 (Separate `.gltf` + `.bin`) atau FBX deterministik.

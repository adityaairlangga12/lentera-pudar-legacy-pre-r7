---
name: blender_3d_mastery
description: "Pustaka keahlian pemodelan 3D High-Detail di Blender 5.2 LTS, hierarki armature rigging biomekanik, konsistensi bone roll, PBR & cel materials The Triad, cloth physics syal, dan ekspor glTF/FBX deterministik ke Unreal Engine 5."
---

# Blender 5.2 LTS 3D High-Detail Mastery & UE5 Pipeline

Skill ini memuat seluruh standar teknis pemodelan 3D, rigging, material, dan ekspor aset karakter/lingkungan untuk semesta 3D Action RPG *Lentera Pudar*.

---

## 1. Standar Pemodelan Karakter 3D (Hero Proportions 1:6.5–1:7)
- **Kaelen**: Tinggi 1.78m, proporsi atletis bergaya *Final Fantasy VII Remake*.
- **Lengan Kiri**: Kluster kristal es prisma bersudut tajam (*faceted crystal shards*) dengan taji kristal di deltoid, siku, dan cakar es.
- **Lengan Kanan**: Balutan perban spiral bersilang (*cross-wrapped bandages*).
- **Kepala & Wajah**: Penutup mata kulit hitam pada mata kanan, rambut perak berlayer tajam (*spiky anime strands*).
- **Pakaian**: Jubah kelana usang gelap dengan sabuk baldric melintang di dada dan gesper perak.
- **Syal Jiwa Aina**: Kerah kain emas di leher dengan ekor pita meliuk dinamis (*flowing S-curve ribbon*).

---

## 2. Standar Rigging Armature & Bone Hierarchy
- **Root**: `Root` (Z=0 pada pivot telapak kaki).
- **Spine**: `Pelvis` ➔ `Spine_01` ➔ `Spine_02` ➔ `Chest` ➔ `Neck` ➔ `Head`.
- **Left Arm**: `Clavicle_L` ➔ `UpperArm_L` ➔ `Forearm_L` ➔ `Hand_L` ➔ `Talon_01..05`.
- **Right Arm**: `Clavicle_R` ➔ `UpperArm_R` ➔ `Forearm_R` ➔ `Hand_R` ➔ `Fingers_R`.
- **Legs**: `Thigh_L/R` ➔ `Calf_L/R` ➔ `Foot_L/R` ➔ `Toe_L/R`.
- **Scarf Spring Bones**: Rantai 5-bone (`Scarf_01` s.d. `Scarf_05`) untuk simulasi kain dinamis.

---

## 3. Shading & Material The Triad 3D
- **Syal Aina (`Mat_Scarf`)**: Emissive Warm Gold (`#F4B860` 2700K Kelvin, Emission Strength 2.5).
- **Lengan Kristal Es (`Mat_IceArm`)**: Radiant Cold Cyan/Blue (`#4A6FA5` & `#7EE8FA` 6500K Kelvin, Transmission 0.7, Roughness 0.15, Emission 3.0).
- **Jubah Kelana (`Mat_Tunic`)**: Dark Ancient Robe (`#2A211C` / `#141013`, Roughness 0.75).
- **Sabuk & Sepatu (`Mat_Leather`)**: Rich Brown Leather (`#5C3218`, Roughness 0.35, Metallic 0.1).

---

## 4. Ekspor glTF 2.0 / FBX ke Unreal Engine 5
- **Sumbu**: $+Z$ Forward / $+Y$ Up.
- **Transform**: Apply all transforms (`Location`, `Rotation`, `Scale` = 1.0) sebelum ekspor.
- **Format**: glTF 2.0 (Separate `.gltf` + `.bin`) atau FBX dengan embedded textures.

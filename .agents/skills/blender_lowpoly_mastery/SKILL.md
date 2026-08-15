---
name: blender_lowpoly_mastery
description: "Pustaka keahlian pemodelan low-poly (300-1000 tris) di Blender 5.2 LTS, hierarki armature rigging biomekanik, konsistensi bone roll, flat materials, dan ekspor glTF 2.0 untuk pipeline render pixelation Godot 4.7.1."
---

# Blender 5.2 LTS Low-Poly & Rigging Mastery

Skill ini memastikan pemodelan 3D low-poly untuk karakter dan bos *Lentera Pudar* mematuhi batas poligon ketat, orientasi sendi biomekanik yang benar, dan ekspor glTF 2.0 yang bebas distorsi.

---

## 1. Standar Pemodelan Low-Poly (Target 300–1000 Triangles)
- **Batas Poligon Terukur**: Setiap karakter humanoid wajib berada dalam rentang **300–1000 tris**. Karakter akan didownscale ke resolusi piksel rendah (misal 320x180), sehingga detail poligon di atas 1000 tris adalah pemborosan yang tidak terlihat pemain.
- **Segmentasi Anggota Badan**: Pastikan lengan dan kaki memiliki minimal **6–8 segmen poligon** melingkar agar siluet tubuh tidak patah menjadi segi-banyak kasar saat diputar ke 8 arah.
- **Flat Shading Mutlak**: Seluruh objek mesh wajib menggunakan **Flat Shading** (`set_shading_mode(object, mode="flat")`), bukan Smooth Shading. Flat shading menjaga ketegasan batas warna kluster saat dirender melalui shader pixelation.

---

## 2. Hierarki Armature & Rigging Biomekanik
Rig harus mengikuti anatomi nyata agar batas sudut pergerakan sendi natural:
```text
Root (0, 0, 0 di lantai)
  └── Pelvis (Pusat Massa / Center of Mass)
        ├── Spine ➔ Chest ➔ Neck ➔ Head
        │     ├── Scarf_Base ➔ Scarf_01 ➔ Scarf_02 ➔ Scarf_03 (Chain Syal Aina)
        │     ├── Shoulder.L ➔ UpperArm.L ➔ Forearm.L ➔ Hand.L (Lengan Kutukan)
        │     └── Shoulder.R ➔ UpperArm.R ➔ Forearm.R ➔ Hand.R (Lengan Normal)
        ├── Thigh.L ➔ Shin.L ➔ Foot.L ➔ Toe.L
        └── Thigh.R ➔ Shin.R ➔ Foot.R ➔ Toe.R
```

---

## 3. Konsistensi Bone Roll & Transform
- **Wajib `apply_all_transforms`**: Sebelum melakukan rigging atau ekspor glTF, wajib me-reset semua rotasi, skala, dan translasi pada objek mesh dan armature (`apply_all_transforms(object)`).
- **Validasi Bone Roll**: Bone roll yang tidak konsisten adalah penyebab utama limb berputar 360° atau terkilir saat diimpor ke Godot. Seluruh sumbu tekukan (X/Z) harus seragam di kedua sisi tubuh.

---

## 4. Texturing & Material
- **Flat Materials**: Gunakan material berwarna solid atau palet tekstur terkuantisasi (The Triad: `#F4B860`, `#4A6FA5`, `#2A211C`). Dilarang menggunakan material PBR gradient kompleks atau roughness/metallic map.
- **Asimetri Karakter**: Pastikan material lengan kiri kutukan (es biru `#4A6FA5`) dan eyepatch kanan (`#141013`) di-assign secara independen pada vertex mesh yang sesuai.

---

## 5. Ekspor glTF 2.0 ke Godot 4.7.1
- **Format Ekspor**: Ekspor sebagai `.gltf` atau `.glb` dengan metadata rig JSON.
- **Orientasi Sumbu**: glTF menggunakan $+Z$ forward. Pastikan rest pose menghadap $+Z$ dan karakter berdiri di atas grid $Y=0$.
- **Validasi File**: Panggil `validate_export` untuk memastikan tidak ada bone corrupt atau unassigned vertex weights.

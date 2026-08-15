---
name: pixel_art_animation_mastery
description: "Hukum mutlak untuk proporsi 32x32px, teori warna (Hue Shifting), integrasi 3D-to-Pixel render, dan prinsip animasi Walk Cycle Top-Down untuk Lentera Pudar."
---

# 32x32 Pixel Art & Animation Mastery (Hybrid Standard)

Skill ini memastikan representasi visual pixel art 32x32px—baik yang bersumber dari 3D SubViewport pixelation maupun Aseprite 2D—tetap tajam, berbobot, dan memancarkan estetika *Misterius-Hangat*.

---

## 1. Proporsi Stylized Karakter (32x32 Top-Down)
- **Rasio 1:3 hingga 1:3.5**: Kepala mengambil ~33% tinggi tubuh (~10–12 piksel dari 32 piksel), torso ~25%, dan kaki ~42%. Proporsi ini menyeimbangkan keterbacaan ekspresi duka dengan postur tubuh pengelana tangguh tanpa menjadi *cute chibi*.
- **Perspektif Low Top-Down**: Kemiringan kamera 20°–30° (Zelda-like). Karakter berdiri tegak dari depan untuk memamerkan detail pakaian, asimetri tangan es biru, dan syal kuning yang bersinar.

---

## 2. Walk Cycle & Integritas Sub-Pixel
1. **Contact**: Kedua kaki menyentuh tanah (jarak langkah terjauh).
2. **Down (Squash)**: Titik terendah tubuh (bobot menekan).
3. **Passing**: Satu kaki menopang, kaki lain melewati.
4. **Up (Stretch)**: Titik tertinggi tubuh.
- **Pencegahan Distorsi Sub-Pixel (Face Melting)**: Seluruh transformasi dan posisi kamera wajib di-snap ke angka bulat integer murni (Nearest filtering). Dilarang rotasi miring 2D tanpa shader pixelation.

---

## 3. Teori Warna Hue Shifting (The Triad of Lentera Pudar)
- **Highlights (Cahaya Hangat — 2700K)**: Geser hue ke arah kuning/emas hangat (`#FFE0B2`, `#F4B860`).
- **Shadows (Bayangan Dingin — 6500K)**: Geser hue ke arah biru tua, ungu dingin, atau batu dungeon (`#4A6FA5`, `#2C4875`, `#1A1310`).
- **Dark Halo Trick**: Untuk mempertegas kristal es biru atau nyala api syal, kelilingi tepi luarnya dengan piksel outline gelap padat (`#141013`).

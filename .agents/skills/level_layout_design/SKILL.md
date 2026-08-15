---
name: level_layout_design
description: Standar perancangan tata letak dungeon 2D top-down (low top-down 3/4), navigasi landmark, room loop, distribusi zona gelap-terang, dan gating mekanik untuk Lentera Pudar.
---

# Level Layout Design (Game Designer)

Panduan perancangan level dungeon misterius-hangat untuk game 2D Pixel RPG top-down di Godot 4.

---

## 1. Prinsip Spasial & Perspektif
- **Perspektif**: Low top-down (sudut pandang 3/4 Zelda-like).
- **Grid Tile**: `32x32 px`. Koridor minimum lebar 2 tile (64px) agar pergerakan 8-arah terasa leluasa tanpa terjepit collision.
- **Room Loops**: Hindari lorong buntu linear yang membosankan (*dead-ends*). Buat pola sirkuit/looping di mana pemain bisa kembali ke area utama setelah membuka jalan pintas (*shortcut*).

---

## 2. Navigasi & Landmark
- **Visual Gating**:
  - Pintu es kristal biru (memerlukan api lentera untuk mencairkannya).
  - Jurang/keretakan lantai dungeon gelap.
  - Altar batu kuno dengan ukiran lentera sebagai titik simpan (*checkpoint* / *bonfire*).
- **Landmark Jelas**: Setiap ruangan besar wajib memiliki satu objek dominan yang mudah diingat (misal: patung kristal es raksasa di tengah, kolam air beku, atau reruntuhan tiang bercahaya).

---

## 3. Distribusi Kegelapan & Cahaya
- **Kegelapan Dasar**: Diatur oleh `CanvasModulate` `#2A211C`.
- **Cahaya Karakter**: Radius `PointLight2D` syal kuning (~150-200px) menjadi radius visibilitas pemain.
- **Relief Zones**: Tempatkan obor/lentera dinding statis di persimpangan kunci sebagai area istirahat (*safe harbor*) yang memberikan rasa hangat dan orientasi spasial.

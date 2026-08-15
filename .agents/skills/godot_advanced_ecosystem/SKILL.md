---
name: godot_advanced_ecosystem
description: "Pengetahuan mendalam mengenai ekosistem plugin pihak ketiga Godot 4.7.1 dan fitur tingkat lanjut (Dialogic 2, Phantom Camera, Pathfinding AI, Procedural Dungeon) untuk RPG Lentera Pudar."
---

# Godot 4.7.1 Advanced Ecosystem & Plugins

Skill ini menjamin pemanfaatan standar plugin industri pihak ketiga yang teruji di Godot 4.7.1 untuk narasi, kamera dinamis, navigasi AI, dan procedural level layout.

---

## 1. Sistem Dialog & Percabangan Narasi (Dialogic 2)
- **Wajib menggunakan plugin Dialogic 2** untuk seluruh percakapan, monolog duka Kaelen, bisikan Aina, dan dialog bos.
- Memisahkan narasi dari kode murni via *Timeline Editor*.
- Integrasi kode via API resmi:
  ```gdscript
  Dialogic.start("timeline_sector1_boss")
  Dialogic.signal_event.connect(_on_dialogic_signal)
  ```

---

## 2. Sistem Kamera, Look-Ahead, & Screen Shake (Phantom Camera)
- **Phantom Camera** menangani `Camera2D` follow dengan *Look-Ahead Offset* prediktif dan peredam *Spring-Damper*.
- **Screen Shake Organik**: Menggunakan `FastNoiseLite` (Perlin Noise 2D) untuk goncangan saat terkena serangan (*hit-impact*) atau ledakan kristal es.
- **Room Bounds Clamping**: Mengunci kamera ke batas area ruangan level agar tidak menampilkan area di luar dungeon.

---

## 3. Navigasi AI (AStarGrid2D / NavigationAgent2D)
- Gunakan `NavigationAgent2D` dengan `NavigationRegion2D` untuk pergerakan musuh yang luwes menghindari tembok dan pilar kristal es.
- Musuh patroli mematuhi zona gelap-terang (tertarik mendekat atau takut pada cahaya lentera).

---

## 4. Procedural Dungeon Generation (`TileMapLayer`)
- **Drunkard's Walk (Random Walker)** untuk alur koridor utama dungeon.
- **Cellular Automata** untuk menghaluskan pembentukan dinding gua beku alami.
- Dieksekusi menggunakan node `TileMapLayer` native Godot 4.7.1 dengan Terrain Autotiling Bitmask.

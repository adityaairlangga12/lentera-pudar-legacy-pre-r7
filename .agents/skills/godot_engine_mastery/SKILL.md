---
name: godot_engine_mastery
description: "Penguasaan tingkat tinggi terhadap arsitektur Godot 4.7.1 untuk game 2D/3D Hybrid Pixel RPG, SubViewport pixelation, Camera3D Orthogonal, IK/procedural gait, spring-damper physics, dan lighting Kelvin."
---

# Godot 4.7.1 Engine Mastery (Hybrid Pixelation & Systems)

Skill ini memastikan implementasi teknis di dalam *engine* bebas dari masalah *blurring* piksel, orientasi render akurat, dan performa 60 FPS stabil.

---

## 1. Arsitektur SubViewport Pixelation Pipeline (3D-to-Pixel)
Untuk menghasilkan grafis 3D low-poly dengan cita rasa pixel art 32x32px yang tajam:
1. **`SubViewportContainer`**:
   - `texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST` (Wajib!).
   - `stretch = false` (Gunakan integer scaling untuk penskalaan viewport).
2. **`SubViewport`**:
   - `size = Vector2i(320, 180)` atau `Vector2i(480, 270)`.
   - `transparent_bg = true`.
3. **`Camera3D`**:
   - `projection = Camera3D.PROJECTION_ORTHOGONAL` (Dilarang Perspective!).
   - `size` diatur sesuai jangkauan framing karakter (sekitar 3.0–3.5).
   - `rotation_degrees.x = -25.0` (Kemiringan sudut pandang low top-down).
4. **`CelShader.gdshader`**:
   - Menggunakan material unshaded dengan shading bertingkat tegas dan sampler tekstur `filter_nearest`.

---

## 2. Animasi Fisika & Procedural Locomotion
- **Procedural Sinusoidal Gait**:
  - Inverted pendulum: $y_{foot} = A \sin(\text{phase})$, $x_{foot} = L \cos(\text{phase})$, dengan phase offset $\pi$ antar kaki.
  - Body bob: Frekuensi 2x siklus langkah ($y_{bob} = B |\sin(2 \cdot \text{phase})|$).
- **Secondary Motion (Spring-Damper System)**:
  - Hukum Hooke: $F = -k(x - x_0) - c \cdot v$.
  - Diterapkan pada chain bone syal Aina dan rambut untuk menghasilkan inersia dan ayunan luwes.
- **Foot Raycast IK**:
  - Menembakkan raycast ke bawah untuk mendeteksi permukaan medan bertingkat/tangga.

---

## 3. Sistem Pencahayaan & Shaders (Kelvin Scale)
- **Skala Temperatur Kelvin**:
  - Sumber Lentera & Api: **2700K Warm Yellow (`#F4B860`)** dengan *photometric inverse-square falloff*.
  - Sumber Kutukan Es: **6500K Cold Cyan/Blue (`#4A6FA5`)** dengan *linear falloff*.
- **Shadow Casting (LightOccluder2D)**:
  - Dinding dungeon wajib memiliki polygon occluder tertutup agar cahaya lentera tidak menembus dinding batu.
- **Shader Tangan Kutukan (`CursedHand.gdshader`)**:
  - Menggunakan uniform `intensity` yang dikendalikan secara live oleh *Curse Meter* pemain.

---

## 4. Retro Pixel Particles (GPUParticles2D)
- Tekstur partikel berukuran kecil murni (2x2 atau 4x4 px) tanpa gradasi blur.
- `texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST`.
- Tepi alpha keras (*Hard-Edge Alpha*) untuk menyatu dengan estetika pixel art.

---

## 5. Jebakan Fisika & Kebocoran Memori (Memory Leaks)
- **Aturan Mutlak `move_and_slide()`**: JANGAN PERNAH mengalikan `velocity` dengan `delta` sebelum memanggil `move_and_slide()` pada `CharacterBody2D`.
- **Orphan Nodes**: Selalu pastikan node yang diinstansiasi ditambahkan ke tree via `add_child()` atau dihancurkan dengan `queue_free()`.
- **Bahaya Sinyal Lambda**: Hindari fungsi lambda anonim yang menangkap referensi node `self`. Selalu hubungkan sinyal ke fungsi bernama.

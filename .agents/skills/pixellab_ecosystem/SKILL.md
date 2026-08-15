---
name: pixellab_ecosystem
description: "Keahlian dalam memanfaatkan Pixellab Cloud untuk Concept/Reference generation, potret dialog karakter, dan ideasi visual."
---

# Pixellab Ecosystem (Concept & Reference Sourcing)

Skill ini memandu pemanfaatan Pixellab sebagai sumber referensi/konsep visual awal (*Concept & Reference source*) sebelum aset dimodelkan dalam low-poly 3D (Jalur B) atau digambar secara detail di Aseprite.

---

## 1. Peran Pixellab dalam Pipeline Hybrid
Sesuai diagram arsitektur di `workflow-mcp-aseprite-godot.md`:
```text
[Pixellab / Reference Concept] ➔ [Blender 3D Low-Poly / Aseprite 2D] ➔ [Godot 4.7.1]
```
- **Karakter Utama/Boss**: Pixellab digunakan untuk *concept sheet* dan ideasi siluet awal sebelum dimodelkan dalam low-poly 300–1000 tris di Blender.
- **Potret Dialog NPC**: Menggunakan `create_portrait_character` untuk menghasilkan visual potret resolusi tinggi saat dialog (Dialogic 2).
- **Inpainting & Ideasi**: Menggunakan `inpaint_image` untuk menguji variasi warna/aksesoris sebelum diterapkan ke material flat 3D atau spritesheet.

---

## 2. Parameter Baku Low Top-Down
- **Camera View**: `low top-down` (sudut pandang ~20 derajat).
- **Outline Style**: `single color black outline` atau `selective outline`.
- **Target Palet**: Selalu sertakan kata kunci palet *The Triad* (`#F4B860` warm gold, `#4A6FA5` frost ice, `#2A211C` dark neutral).

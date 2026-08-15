---
name: visual_pipeline_automation
description: "Panggil skill ini setiap kali kamu diminta untuk membuat, merancang, atau men-generate karakter/objek/aset visual untuk proyek Lentera Pudar (menggunakan alur Jalur B Blender 3D Low-Poly, Godot SubViewport Pixelation, dan Aseprite 2D)."
---

# Visual Pipeline Automation (Jalur B Master Workflow)

Skill ini adalah implementasi praktis dari BAB V di `AGENTS.md` dan `workflow-mcp-aseprite-godot.md`. Wajib dipatuhi untuk menjaga konsistensi visual 3D-to-Pixel dan aset 2D.

---

## 1. Pembagian Jalur Produksi Aset

| Jenis Aset | Engine / Tool | Alur Produksi |
|---|---|---|
| **Karakter Utama, Boss, & NPC Frekuensi Tinggi** | **Blender 5.2 ➔ Godot 4.7.1** | Modeling Low-Poly (300–1000 tris) ➔ Rigging Armature ➔ glTF 2.0 Export ➔ Godot SubViewport Pixelation (Nearest) + Cel-Shader + Spring-Damper Scarf |
| **UI, Icon, HUD, Bitmap Typography** | **Aseprite ➔ Godot** | Canvas setup ➔ 9-Slice Slicing ➔ Palette Quantize ➔ Godot Control Nodes |
| **Dungeon Tileset (Floors & Walls)** | **Aseprite ➔ Godot** | Seamless 32x32 Tiles ➔ Autotile Bitmask Terrain ➔ LightOccluder2D Setup |
| **FX / VFX Tebasan, Flash, Sparks** | **Aseprite ➔ Godot** | Frame-by-Frame Flipbook Hard-Edge (0.2–0.4 detik) ➔ AnimatedSprite2D / GPUParticles2D Nearest |

---

## 2. Alur Karakter Jalur B (Fase 0a–0d ➔ Fase 1–5)

### Tahap 1: Observabilitas & Validasi Mesh (Blender MCP)
1. Analisis brief desain & asimetri (lengan kiri beku `#4A6FA5`, eyepatch `#141013`, baldric, syal kuning `#F4B860`).
2. Buat/buka mesh low-poly (300–1000 tris), terapkan Flat Shading.
3. Bangun armature hierarki anatomis (Root ➔ Pelvis ➔ Spine ➔ Chest ➔ Neck ➔ Head + Limbs + Scarf chain).
4. Jalankan `apply_all_transforms` dan `validate_bone_roll_consistency`.
5. Ekspor sebagai glTF 2.0 (`export_gltf`) beserta JSON metadata rig.

### Tahap 2: Perakitan Scene di Godot 4.7.1 (Godot MCP)
1. Impor glTF ke dalam `Player.tscn`.
2. Pasang struktur render pixelation:
   - `SubViewportContainer` (filter: **Nearest**).
   - `SubViewport` (resolusi rendah: 320×180 / 480×270).
   - `Camera3D` berproyeksi **Orthogonal** (rotasi kemiringan 20°–30°).
   - `CelShader.gdshader` pada material karakter.
3. Pasang `PointLight2D` (2700K Warm Yellow) untuk Syal Aina dan `CursedHand.gdshader` untuk urat es tangan kiri.
4. Pasang skrip locomotion sinusoidal gait dan spring-damper/velvet modifier pada bone syal.

### Tahap 3: Verifikasi Visual & Deterministik (QC Agent)
1. Ambil screenshot via `capture_viewport_screenshot` saat test run headless.
2. Periksa: Tidak ada blur/bilinear, asimetri lengan es konsisten di 8 arah, syal berkibar luwes tanpa clipping, dan console bebas error merah.

---
name: mcp_api_mastery
description: "Pemahaman mendalam mengenai arsitektur Blender 5.2 LTS MCP, standar 3-layer API (Atomic, Macro, Workflow), dan protokol observabilitas 3D."
---

# Lentera Blender 5.2 LTS 3D MCP Mastery

Skill ini memastikan AI memahami arsitektur, batasan waktu (*timeout*), pembagian layer tool, dan protokol observabilitas di ekosistem Blender 5.2 LTS 3D MCP.

---

## 1. Pembagian 3 Layer Tool yang Seragam
Di Blender MCP, perkakas dikelompokkan ke dalam 3 layer terstandarisasi:

1. **Atomic Tools**: Aksi tunggal, kecil, deterministik, dan mudah di-rollback (misal: `create_mesh_primitive`, `add_bone`, `set_bone_roll`, `set_shading_mode`).
2. **Macro Tools**: Aksi level tugas bermakna yang menggabungkan beberapa atomic tool (misal: `create_armature`, `auto_weight_paint`, `unwrap_uv`, `apply_modifier`).
3. **Workflow Tools**: Pipeline multi-langkah dengan pelaporan eksplisit di tiap tahap dan berhenti seketika saat menemui kegagalan (misal: `export_gltf`, `validate_export`, `render_viewport_screenshot`).

---

## 2. Prinsip Observabilitas Sebelum Mutasi
Sebelum melakukan aksi modifikasi yang kompleks di Blender:
- Panggil `get_scene_state` / `render_viewport_screenshot` dan periksa `get_console_output` atau `get_last_error`.

---

## 3. Arsitektur Jaringan & Batasan Waktu (Timeouts)
- **Blender MCP (`COMMAND_TIMEOUT_MS = 25000`)**: Port 8097 / Stdio dispatch. Operasi pemodelan high-poly, skinning armature, dan ekspor glTF/FBX harus selesai dalam 25 detik.

---

## 4. Escape Hatch Terakhir
Eksekusi script python bpy mentah hanya boleh digunakan sebagai **escape hatch tier terakhir** untuk operasi prosedural kompleks yang belum didukung oleh Macro/Workflow tools.

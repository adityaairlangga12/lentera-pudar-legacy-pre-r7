---
name: mcp_api_mastery
description: "Pemahaman mendalam mengenai arsitektur 3-MCP (Blender 5.2, Godot 4.7.1, Aseprite), standar 3-layer API (Atomic, Macro, Workflow), dan protokol observabilitas."
---

# Lentera 3-MCP Ecosystem Mastery (Blender, Godot, Aseprite)

Skill ini memastikan AI memahami arsitektur, batasan waktu (*timeout*), pembagian layer tool, dan protokol observabilitas di seluruh ekosistem MCP.

---

## 1. Pembagian 3 Layer Tool yang Seragam
Di seluruh server MCP (Blender, Godot, dan Aseprite), perkakas dikelompokkan ke dalam 3 layer terstandarisasi:

1. **Atomic Tools**: Aksi tunggal, kecil, deterministik, dan mudah di-rollback (misal: `create_node`, `set_pixel`, `add_bone`, `set_bone_constraint`).
2. **Macro Tools**: Aksi level tugas bermakna yang menggabungkan beberapa atomic tool (misal: `create_skeleton2d`, `export_png`, `create_armature`).
3. **Workflow Tools**: Pipeline multi-langkah dengan pelaporan eksplisit di tiap tahap dan berhenti seketika saat menemui kegagalan (misal: `run_scene_headless`, `validate_export`).

---

## 2. Prinsip Observabilitas Sebelum Mutasi
Sebelum melakukan aksi modifikasi yang kompleks:
- **Blender MCP**: Panggil `get_scene_state` / `render_viewport_screenshot` dan cek `get_console_output`.
- **Godot MCP**: Panggil `read_node_tree` / `capture_viewport_screenshot` dan cek `get_last_error`.
- **Aseprite MCP**: Panggil `get_canvas_info` / `capture_canvas_as_image`.

---

## 3. Arsitektur Jaringan & Batasan Waktu (Timeouts)
- **Aseprite MCP (`COMMAND_TIMEOUT_MS = 15000`)**: Port 8099. Operasi manipulasi kanvas/Lua harus selesai dalam 15 detik.
- **Godot MCP (`COMMAND_TIMEOUT_MS = 20000`)**: Port 8098. Operasi `run_gdscript` dan scene reload harus selesai dalam 20 detik.
- **Blender MCP (`COMMAND_TIMEOUT_MS = 25000`)**: Socket lokal / stdio dispatch. Operasi pemodelan dan skinning armature harus selesai dalam 25 detik.

---

## 4. Escape Hatch Terakhir
Eksekusi kode mentah (`run_lua_script`, `run_gdscript`, atau `raw_python_bpy`) hanya boleh digunakan sebagai **escape hatch tier terakhir** untuk kasus ekstrem yang belum didukung oleh Macro/Workflow tools.

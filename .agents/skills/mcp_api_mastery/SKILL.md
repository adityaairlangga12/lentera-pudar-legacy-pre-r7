---
name: mcp_api_mastery
description: "Pemahaman mendalam mengenai arsitektur Blender 5.2 LTS MCP dan Unreal Engine 5 Python MCP, standar 3-layer API (Atomic, Macro, Workflow), dan protokol observabilitas 3D."
---

# Lentera Pudar — 3D MCP Mastery (Blender 5.2 LTS + Unreal Engine 5)

Skill ini memastikan AI memahami arsitektur, batasan waktu (*timeout*), pembagian layer tool, dan protokol observabilitas di ekosistem **Blender 5.2 LTS MCP** dan **Unreal Engine 5 Python MCP**.

---

## 1. Pembagian 3 Layer Tool yang Seragam (Berlaku di Blender & UE5)
Di seluruh ekosistem MCP proyek ini, perkakas dikelompokkan ke dalam 3 layer terstandarisasi:

1. **Atomic Tools**: Aksi tunggal, kecil, deterministik, dan mudah di-rollback.
   - Blender: `create_mesh_primitive`, `add_bone`, `set_bone_roll`, `set_shading_mode`, `set_material_property`.
   - UE5: `spawn_actor`, `set_material_parameter`, `set_light_property`, `import_asset`.
2. **Macro Tools**: Aksi level tugas bermakna yang menggabungkan beberapa atomic tool.
   - Blender: `create_armature`, `auto_weight_paint`, `unwrap_uv`, `apply_modifier`, `setup_cloth_simulation`.
   - UE5: `create_blueprint_class`, `setup_chaos_cloth`, `configure_niagara_system`, `setup_material_parameter_collection`.
3. **Workflow Tools**: Pipeline multi-langkah dengan pelaporan eksplisit di tiap tahap.
   - Blender: `export_gltf`, `validate_export`, `render_viewport_screenshot`, `full_character_pipeline`.
   - UE5: `import_and_setup_skeletal_mesh`, `configure_lumen_lighting`, `package_build`.

---

## 2. Prinsip Observabilitas Sebelum Mutasi
Sebelum melakukan aksi modifikasi yang kompleks:
- **Blender**: Panggil `get_scene_state` / `render_viewport_screenshot` dan periksa `get_console_output` atau `get_last_error`.
- **UE5**: Panggil `get_editor_log` / `get_asset_list` sebelum memanipulasi Blueprint atau Level.

---

## 3. Arsitektur Jaringan & Batasan Waktu (Timeouts)

| Engine/Tool | Timeout | Koneksi | Catatan |
|---|---|---|---|
| **Blender MCP** | `COMMAND_TIMEOUT_MS = 25000` | Port `8097` / Stdio dispatch | Operasi pemodelan high-poly (40k–60k tris), skinning armature, dan ekspor glTF/FBX harus selesai dalam 25 detik. |
| **UE5 Python MCP** | `COMMAND_TIMEOUT_MS = 30000` | Unreal Python Editor Scripting Plugin | Operasi level loading, Lumen baking, dan World Partition setup butuh alokasi lebih besar. |

> **Wajib aktifkan di UE5**: `Edit ➔ Plugins ➔ Python Editor Script Plugin` sebelum koneksi MCP.

---

## 4. Arsitektur Shared Asset Bridge (Blender → UE5)

```
[Blender 5.2 LTS]
    ↓ export_gltf() / export_fbx()
[Shared Asset Folder: /Content/CharactersImport/]
    ↓ MCP import_asset() + setup pipeline
[Unreal Engine 5 Content Browser]
    → SK_Kaelen_Body.uasset
    → M_Cursed_Crystal.uasset
    → ABP_Kaelen.uasset (Animation Blueprint)
```

- File bridge folder harus merupakan path absolut yang konsisten antar sesi kerja.
- Selalu validasi poly count dan transform setelah import (`get_asset_details()`).

---

## 5. Escape Hatch Terakhir
Eksekusi script Python `bpy` mentah (Blender) atau `unreal.EditorAssetLibrary` (UE5) mentah hanya boleh digunakan sebagai **escape hatch tier terakhir** untuk operasi prosedural kompleks yang belum didukung oleh Macro/Workflow tools — dan wajib didokumentasikan sebagai anomali sesi.

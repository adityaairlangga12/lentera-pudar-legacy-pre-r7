---
status: ACTIVE
type: TOOL_CONTRACT
authority_scope: pipeline.api_contract
canonical: false
---


# API Cheat Sheet — Blender MCP (Hardened v1) & UE5 Python
### Panduan Praktis Pemanggilan Perkakas MCP 23-Tool & Scripting Otomasi

> **Dokumen Panduan Penggunaan Praktis (*Usage Patterns & API Cheat Sheet*)**  
> Berisi contoh pemanggilan representatif untuk 23 Tool Publik `lentera-blender-mcp` (Model `HEADLESS_FILE_BACKED`) dan otomasi Unreal Engine 5 Python. Untuk spesifikasi kontrak lengkap, rujuk dokumen kanonikal [tools-mcp-stack.md](file:///d:/GodotProjects/Lentera-Pudar/references/06-pipeline-qc/tools-mcp-stack.md).

---

## 1. Pola Pemanggilan Perkakas Blender MCP (23 Public Tools)

### A. Inisialisasi Scene Baru & Pembuatan Mesh
```json
// Tool: create_mesh_primitive
{
  "type": "cylinder",
  "size": 2.0,
  "name": "SM_IceCrystal_Base",
  "output_blend_file": "d:/GodotProjects/Lentera-Pudar/Assets/3D/Props/IceCrystal.blend"
}
```

### B. Mutasi Geometri & Modifier pada File Eksis
```json
// Tool: apply_modifier
{
  "blend_file": "d:/GodotProjects/Lentera-Pudar/Assets/3D/Props/IceCrystal.blend",
  "object": "SM_IceCrystal_Base",
  "modifier_type": "BEVEL",
  "params": {
    "width": 0.05,
    "segments": 2
  }
}
```

### C. Pembersihan Geometri & Penggabungan Vertex
```json
// Tool: merge_by_distance
{
  "blend_file": "d:/GodotProjects/Lentera-Pudar/Assets/3D/Props/IceCrystal.blend",
  "object": "SM_IceCrystal_Base",
  "threshold": 0.001
}
```

### D. UV Unwrapping
```json
// Tool: unwrap_uv
{
  "blend_file": "d:/GodotProjects/Lentera-Pudar/Assets/3D/Props/IceCrystal.blend",
  "object": "SM_IceCrystal_Base",
  "method": "SMART_PROJECT"
}
```

### E. Observasi & Inspeksi Geometri Independen
```json
// Tool: get_mesh_stats
{
  "blend_file": "d:/GodotProjects/Lentera-Pudar/Assets/3D/Props/IceCrystal.blend",
  "object": "SM_IceCrystal_Base"
}
```

### F. Pembangunan Skeleton Bersih (Clean Armature & Rigging)
```json
// 1. Buat Armature Bersih (0 tulang / zero bones)
// Tool: create_armature
{
  "name": "SK_Kaelen_Rig",
  "output_blend_file": "d:/GodotProjects/Lentera-Pudar/Assets/3D/Characters/Kaelen_Rig.blend"
}

// 2. Tambah Tulang Root
// Tool: add_bone
{
  "blend_file": "d:/GodotProjects/Lentera-Pudar/Assets/3D/Characters/Kaelen_Rig.blend",
  "armature": "SK_Kaelen_Rig",
  "name": "Bone_Root",
  "head": [0.0, 0.0, 0.0],
  "tail": [0.0, 0.0, 1.0]
}

// 3. Tambah Tulang Child dengan Head Snapping
// Tool: add_bone
{
  "blend_file": "d:/GodotProjects/Lentera-Pudar/Assets/3D/Characters/Kaelen_Rig.blend",
  "armature": "SK_Kaelen_Rig",
  "name": "Bone_Spine",
  "parent": "Bone_Root",
  "head": [0.0, 0.0, 1.0],
  "tail": [0.0, 0.0, 1.5],
  "use_connect": true
}

// 4. Set Sudut Roll Kanonikal (Radian)
// Tool: set_bone_roll
{
  "blend_file": "d:/GodotProjects/Lentera-Pudar/Assets/3D/Characters/Kaelen_Rig.blend",
  "armature": "SK_Kaelen_Rig",
  "bone": "Bone_Spine",
  "angle_rad": 1.570796
}

// 5. Inspeksi State Armature
// Tool: get_armature_state
{
  "blend_file": "d:/GodotProjects/Lentera-Pudar/Assets/3D/Characters/Kaelen_Rig.blend",
  "armature": "SK_Kaelen_Rig"
}
```

### G. Ekspor glTF 2.0 & Validasi Biner Terverifikasi
```json
// 1. Ekspor Scene ke GLB
// Tool: export_gltf
{
  "blend_file": "d:/GodotProjects/Lentera-Pudar/Assets/3D/Props/IceCrystal.blend",
  "path": "d:/GodotProjects/Lentera-Pudar/Assets/3D/Export/SM_IceCrystal.glb",
  "overwrite": true
}

// 2. Validasi Independen Struktur Biner Artefak
// Tool: validate_export
{
  "path": "d:/GodotProjects/Lentera-Pudar/Assets/3D/Export/SM_IceCrystal.glb",
  "expected_nodes": ["SM_IceCrystal_Base"],
  "require_meshes": true
}
```

> [!IMPORTANT]
> **Prinsip Verifikasi**: Respons eksekusi `export_gltf` HANYA membuktikan operator selesai berjalan (`EXECUTED`). Status `VERIFIED` wajib didukung oleh bukti fisik dari pemanggilan `validate_export`.

---

## 2. Unreal Engine Python Module (`unreal`) Reference

### A. Asset Import Otomatis (SOP 1, Langkah 11)
```python
import unreal

task = unreal.AssetImportTask()
task.filename = "d:/GodotProjects/Lentera-Pudar/Assets/3D/Export/SM_IceCrystal.glb"
task.destination_path = "/Game/Props/IceCrystal"
task.destination_name = "SM_IceCrystal_01"
task.automated = True
task.save = True
task.replace_existing = True

unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
```

### B. Material Instance & MPC Binding (SOP 2, Langkah 6)
```python
# Create Material Instance
mi_factory = unreal.MaterialInstanceConstantFactoryNew()
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
mi = asset_tools.create_asset("MI_IceCrystal_01", "/Game/Materials", unreal.MaterialInstanceConstant, mi_factory)

# Bind Parent Master Material
master_mat = unreal.EditorAssetLibrary.load_asset("/Game/Materials/M_Cursed_Crystal")
unreal.MaterialEditingLibrary.set_material_instance_parent(mi, master_mat)
unreal.MaterialEditingLibrary.set_material_instance_scalar_parameter_value(mi, "Roughness", 0.22)

# Update Material Parameter Collection (MPC_CurseMeter)
mpc = unreal.EditorAssetLibrary.load_asset("/Game/Materials/MPC_CurseMeter")
unreal.MaterialEditingLibrary.set_material_parameter_collection_scalar_parameter_value(mpc, "Curse_Spread", 0.65)
```

### C. Level Construction & Spawning Actors (SOP 5)
```python
mesh_asset = unreal.EditorAssetLibrary.load_asset("/Game/Props/IceCrystal/SM_IceCrystal_01")
spawn_loc = unreal.Vector(0.0, 0.0, 0.0)
spawn_rot = unreal.Rotator(0.0, 0.0, 0.0)

actor = unreal.EditorLevelLibrary.spawn_actor_from_object(mesh_asset, spawn_loc, spawn_rot)
actor.set_actor_scale3d(unreal.Vector(1.0, 1.0, 1.0))
```

### D. Automated High-Resolution Screenshot (Visual Review Gate)
```python
unreal.AutomationLibrary.take_high_res_screenshot(1920, 1080, "QC_Review_Sector01_Altar.png")
```

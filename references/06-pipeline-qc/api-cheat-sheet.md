---
status: ACTIVE
type: TOOL_CONTRACT
authority_scope: pipeline.api_contract
canonical: false
---


# API Cheat Sheet — bpy (Blender 5.2 LTS) & unreal (UE5.8 Python MCP)
### Panduan Eksekusi API Konkret & Protokol Anti-Halusinasi Pemanggilan Fungsi

> **Dokumen Sumber Kebenaran API (*Technical Scripting & API Syntax Reference*)**  
> Berisi sintaks resmi dan pola pemanggilan fungsi stabil untuk otomasi **Blender Python (`bpy`)** dan **Unreal Engine Python (`unreal`)**. Seluruh AI Agent WAJIB mematuhi prinsip *Inspect-Before-Execute* dan dilarang keras menebak nama fungsi.

---

## 1. Protokol Integritas API (Anti-Hallucination Mandate)

1. **Inspeksi Introspeksi Wajib**: Sebelum mengeksekusi operasi penting, jalankan `dir()` atau `help()` untuk memastikan fungsi/properti tersedia pada versi engine yang aktif.
2. **Dilarang Menebak Nama Alternatif**: Jika suatu fungsi tidak ditemukan pada versi terpasang, tandai sebagai **GAP**, buka dokumentasi resmi (`docs.blender.org/api` / `dev.epicgames.com/documentation`), dan laporkan solusinya.
3. **Konversi Linear Color Space**: Nilai hex sRGB wajib dikonversi ke linear color space (skala $0.0–1.0$) sebelum diinput ke Blender shader inputs.

---

## 2. Blender Python API (`bpy`) Reference

### A. Mesh, Primitives & Modifiers (SOP 1: Prop Modeling)
```python
import bpy

# Membuat primitive dasar (skala cm)
bpy.ops.mesh.primitive_cube_add(size=2.0, location=(0, 0, 0))
obj = bpy.context.active_object
obj.name = "SM_IceCrystal_Cluster_01"

# Terapkan Modifier
subsurf = obj.modifiers.new(name="Subdivision", type='SUBSURF')
subsurf.levels = 2
subsurf.render_levels = 2
bpy.ops.object.modifier_apply(modifier="Subdivision")

# Apply Transform (Wajib sebelum ekspor)
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
```

### B. UV Unwrap & Texel Density (SOP 1, Langkah 5)
```python
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.uv.smart_project(angle_limit=66.0, island_margin=0.02)
bpy.ops.object.mode_set(mode='OBJECT')
```

### C. Setup Material PBR The Triad (SOP 2: Material Setup)
```python
mat = bpy.data.materials.new(name="M_IceCrystal")
mat.use_nodes = True
nodes = mat.node_tree.nodes
bsdf = nodes.get("Principled BSDF")

# Konfigurasi PBR Kristal Es (#4A6FA5)
bsdf.inputs["Base Color"].default_value = (0.065, 0.155, 0.380, 1.0) # sRGB gamma corrected
bsdf.inputs["Roughness"].default_value = 0.22
bsdf.inputs["Metallic"].default_value = 0.0
bsdf.inputs["IOR"].default_value = 1.31 # Index bias es

# Assign ke objek aktif
obj.data.materials.append(mat)
```

### D. Rigging & Armature (SOP 3: Rigging Biomekanik)
```python
bpy.ops.object.armature_add(location=(0, 0, 0))
armature = bpy.context.active_object
armature.name = "SK_Kaelen_Rig"

# Parenting Mesh ke Armature dengan Automatic Weights
bpy.ops.object.select_all(action='DESELECT')
obj.select_set(True)
armature.select_set(True)
bpy.context.view_layer.objects.active = armature
bpy.ops.object.parent_set(type='ARMATURE_AUTO')
```

### E. Ekspor FBX Deterministik (SOP 1, Langkah 10)
```python
bpy.ops.export_scene.fbx(
    filepath="d:/GodotProjects/Lentera-Pudar/Assets/Models/SM_IceCrystal_Cluster_01.fbx",
    use_selection=True,
    global_scale=1.0,
    axis_forward='-Z',
    axis_up='Y',
    apply_unit_scale=True,
    bake_space_transform=True
)
```

---

## 3. Unreal Engine Python Module (`unreal`) Reference

### A. Asset Import Otomatis (SOP 1, Langkah 11)
```python
import unreal

task = unreal.AssetImportTask()
task.filename = "d:/GodotProjects/Lentera-Pudar/Assets/Models/SM_IceCrystal_Cluster_01.fbx"
task.destination_path = "/Game/Props/IceCrystal"
task.destination_name = "SM_IceCrystal_Cluster_01"
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
mesh_asset = unreal.EditorAssetLibrary.load_asset("/Game/Props/IceCrystal/SM_IceCrystal_Cluster_01")
spawn_loc = unreal.Vector(0.0, 0.0, 0.0)
spawn_rot = unreal.Rotator(0.0, 0.0, 0.0)

actor = unreal.EditorLevelLibrary.spawn_actor_from_object(mesh_asset, spawn_loc, spawn_rot)
actor.set_actor_scale3d(unreal.Vector(1.0, 1.0, 1.0))
```

### D. Automated High-Resolution Screenshot (Visual Review Gate)
```python
unreal.AutomationLibrary.take_high_res_screenshot(1920, 1080, "QC_Review_Sector01_Altar.png")
```

# API Cheat Sheet — bpy (Blender) & unreal (UE5 Python)
### Referensi Fungsi Konkret untuk Mencegah "Halusinasi API" pada AI Agent

**Catatan penting sebelum dipakai**: API `bpy` dan `unreal` bisa berubah antar versi (termasuk Blender 5.2 LTS yang dirilis setelah pengetahuan dasar saya terbentuk). Dokumen ini berisi pola dan nama fungsi yang **secara historis stabil** di kedua API tersebut, tapi **AI agent WAJIB memverifikasi** nama fungsi persis dengan cara introspeksi langsung (`dir()`, `help()`, atau dokumentasi resmi versi yang terinstall) sebelum eksekusi penting — jangan asumsikan nama fungsi di sini 100% akurat tanpa verifikasi, terutama untuk versi Blender/UE5 yang lebih baru dari perkiraan.

**Instruksi untuk AI agent**: Kalau menemukan fungsi di sini tidak ada/berbeda nama di versi terinstall, JANGAN menebak nama alternatif yang "terdengar masuk akal" — cek dokumentasi resmi versi terpasang dulu (`bpy.ops` autocomplete di Blender Python Console, atau `help(unreal)` di UE5), baru lanjutkan.

---

## 1. Blender (`bpy`) — Referensi per Kategori Task

### A. Mesh & Object Dasar (terkait SOP 1: Membuat Prop Baru)
```python
# Membuat primitive dasar
bpy.ops.mesh.primitive_cube_add(size=2, location=(0,0,0))
bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0,0,0))

# Rename objek (penting untuk naming convention Style Guide/SOP)
bpy.context.active_object.name = "SM_IceCrystal_Cluster_01"

# Masuk/keluar Edit Mode untuk modifikasi mesh
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.object.mode_set(mode='OBJECT')

# Terapkan modifier (misal Subdivision Surface, Mirror)
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.ops.object.modifier_apply(modifier="Subdivision")
```

### B. UV Unwrap (terkait SOP 1, langkah UV)
```python
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.uv.smart_project()  # atau bpy.ops.uv.unwrap() untuk seam manual
bpy.ops.object.mode_set(mode='OBJECT')
```

### C. Material & Shader (terkait SOP 2: Setup Material Baru)
```python
# Membuat material baru
mat = bpy.data.materials.new(name="M_IceCrystal")
mat.use_nodes = True
bsdf = mat.node_tree.nodes.get("Principled BSDF")

# Set parameter PBR dasar sesuai Style Guide
bsdf.inputs["Base Color"].default_value = (0.29, 0.44, 0.65, 1.0)  # contoh hex #4A6FA5 dikonversi ke 0-1 range
bsdf.inputs["Roughness"].default_value = 0.22
bsdf.inputs["Metallic"].default_value = 0.0

# Assign material ke objek
obj = bpy.context.active_object
obj.data.materials.append(mat)
```
**Catatan konversi warna**: hex ke Blender color value pakai skala 0-1 (bukan 0-255), dan Blender pakai linear color space secara default — perlu gamma correction saat konversi manual dari hex sRGB.

### D. Sculpting (terkait SOP 1, Riset Kena bagian 8)
```python
bpy.ops.object.mode_set(mode='SCULPT')
# Operasi sculpt brush biasanya lewat bpy.ops.sculpt.brush_stroke()
# tapi untuk kontrol presisi, lebih umum dilakukan via viewport interaktif
# — verifikasi apakah MCP kustom kamu punya wrapper khusus untuk operasi sculpt terprogram
```

### E. Rigging (terkait SOP 3)
```python
# Menambah armature
bpy.ops.object.armature_add(location=(0,0,0))
armature = bpy.context.active_object

# Masuk Edit Bone mode untuk atur tulang
bpy.ops.object.mode_set(mode='EDIT')
# armature.data.edit_bones untuk manipulasi individual bone

# Parenting mesh ke armature dengan automatic weights
bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.parent_set(type='ARMATURE_AUTO')
```

### F. Cloth Simulation (terkait SOP 4)
```python
bpy.ops.object.modifier_add(type='CLOTH')
cloth_settings = bpy.context.object.modifiers["Cloth"].settings

# Parameter sesuai Style Guide bagian 3
cloth_settings.mass = 0.3
cloth_settings.tension_stiffness = 15  # sesuaikan mapping ke "stiffness" 0.4-0.6 dari Style Guide
cloth_settings.compression_stiffness = 15
cloth_settings.bending_stiffness = 0.5
```
**Catatan**: parameter cloth Blender (`tension_stiffness`, dsb) tidak 1:1 sama skalanya dengan istilah "stiffness 0-1" di Style Guide — perlu tabel konversi/kalibrasi terpisah saat implementasi nyata, jangan asumsikan mapping linear langsung.

### G. Animation & Keyframe (terkait SOP 6, Riset Kena hand-animate)
```python
# Set keyframe untuk properti objek
obj.location = (0, 0, 2)
obj.keyframe_insert(data_path="location", frame=1)

obj.location = (0, 0, 0)
obj.keyframe_insert(data_path="location", frame=24)

# Set interpolation (easing curve, terkait Teori bagian 14.B)
for fcurve in obj.animation_data.action.fcurves:
    for kf in fcurve.keyframe_points:
        kf.interpolation = 'BEZIER'  # atau 'EASE_IN_OUT'
```

### H. Export ke FBX (terkait SOP 1, langkah export)
```python
bpy.ops.export_scene.fbx(
    filepath="/path/to/SM_IceCrystal_Cluster_01.fbx",
    use_selection=True,
    global_scale=1.0,  # pastikan skala sesuai standar UE5 (1 unit = 1cm)
    apply_unit_scale=True
)
```

### I. Geometry Nodes (terkait Teknik Tambahan/Tools update — modeling prosedural)
```python
# Geometry Nodes lebih umum dibangun lewat node editor interaktif
# daripada scripting penuh, tapi bisa diakses via:
mod = obj.modifiers.new(name="GeometryNodes", type='NODES')
mod.node_group = bpy.data.node_groups["NamaNodeGroup"]
```

---

## 2. Unreal Engine (`unreal` Python Module) — Referensi per Kategori Task

### A. Asset Import (terkait SOP 1, langkah import FBX)
```python
import unreal

# Import FBX ke Content Browser
task = unreal.AssetImportTask()
task.filename = "/path/to/SM_IceCrystal_Cluster_01.fbx"
task.destination_path = "/Game/Props/IceCrystal"
task.automated = True
task.save = True

unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
```

### B. Material Instance & Parameter Collection (terkait SOP 2, Style Guide emissive dinamis)
```python
# Membuat Material Instance dari master material
mi_factory = unreal.MaterialInstanceConstantFactoryNew()
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
mi = asset_tools.create_asset("MI_IceCrystal_01", "/Game/Materials", unreal.MaterialInstanceConstant, mi_factory)

# Set parent material
master_mat = unreal.EditorAssetLibrary.load_asset("/Game/Materials/M_IceCrystal")
unreal.MaterialEditingLibrary.set_material_instance_parent(mi, master_mat)

# Set scalar parameter (misal roughness)
unreal.MaterialEditingLibrary.set_material_instance_scalar_parameter_value(mi, "Roughness", 0.22)

# Set Material Parameter Collection scalar (untuk Curse Meter dinamis)
mpc = unreal.EditorAssetLibrary.load_asset("/Game/Materials/MPC_CurseMeter")
unreal.MaterialEditingLibrary.set_material_parameter_collection_scalar_parameter_value(mpc, "CurseLevel", 0.5)
```

### C. Spawn Actor & Level Manipulation (terkait SOP 5, level design)
```python
# Spawn actor di level
location = unreal.Vector(0, 0, 0)
rotation = unreal.Rotator(0, 0, 0)
actor = unreal.EditorLevelLibrary.spawn_actor_from_object(mesh_asset, location, rotation)

# Set property actor (misal skala)
actor.set_actor_scale3d(unreal.Vector(1, 1, 1))
```

### D. World Partition & Streaming (terkait SOP 5, Style Guide/Teori bagian World Partition)
```python
# World Partition biasanya dikonfigurasi lewat Editor UI/Data Layers
# API Python untuk ini lebih terbatas dan sering butuh unreal.WorldPartitionSubsystem
# — VERIFIKASI langsung ke dokumentasi versi UE5 terinstall sebelum eksekusi,
# area ini paling rawan berubah antar versi UE5
```

### E. Behavior Tree & Blueprint (terkait SOP 6, sistem gameplay)
```python
# Manipulasi Blueprint biasanya lebih terbatas lewat Python murni
# dibanding lewat Blueprint Editor langsung — untuk logic kompleks,
# pertimbangkan AI agent men-generate Blueprint graph via
# unreal.BlueprintEditorLibrary jika tersedia di versi terinstall,
# atau eskalasi ke manusia untuk setup awal graph, AI hanya isi parameter
asset = unreal.EditorAssetLibrary.load_asset("/Game/AI/BT_JiwaBeku")
```

### F. Asset Naming & Folder Verification (terkait SOP "Aturan Umum", naming convention)
```python
# Cek apakah asset dengan nama tertentu sudah ada (hindari duplikasi - SOP 1 langkah 1)
exists = unreal.EditorAssetLibrary.does_asset_exist("/Game/Props/IceCrystal/SM_IceCrystal_Cluster_01")

# List semua asset di folder (untuk audit naming convention)
assets = unreal.EditorAssetLibrary.list_assets("/Game/Props/", recursive=True)
```

### G. Screenshot/Render Capture (terkait Visual Self-Review Loop)
```python
# Untuk automated screenshot dari viewport/render:
unreal.AutomationLibrary.take_high_res_screenshot(1920, 1080, "review_iteration_01.png")
# Catatan: fungsi capture render tergantung setup MCP kustom kamu —
# beberapa implementasi custom MCP punya wrapper sendiri untuk render capture,
# cek dokumentasi MCP kustom kamu untuk cara paling reliable
```

---

## 3. Aturan Pemakaian Cheat Sheet Ini

1. **Selalu verifikasi versi**: fungsi `bpy`/`unreal` bisa deprecated atau berubah nama antar versi major. Sebelum menjalankan task penting, AI agent sebaiknya cek `dir(bpy.ops.mesh)` atau `dir(unreal)` dulu untuk konfirmasi fungsi masih ada.
2. **Kalau fungsi tidak ditemukan**: JANGAN menebak nama serupa — laporkan sebagai gap (sesuai prosedur SOP), cari di dokumentasi resmi (`docs.blender.org/api`, `dev.epicgames.com/documentation` untuk Python API UE5), baru lanjutkan.
3. **Dokumen ini adalah starting point, bukan referensi lengkap** — API penuh `bpy` dan `unreal` jauh lebih besar dari yang tercakup di sini. Tambahkan pola baru ke dokumen ini setiap kali AI agent berhasil menemukan cara mengeksekusi task yang belum ada di sini, supaya jadi referensi yang terus bertambah (living document, sesuai Teori bagian 18.G).
4. **Bagian dengan catatan "verifikasi langsung"** (World Partition, Behavior Tree Python, Screenshot capture) sengaja ditandai karena area ini paling rawan berubah/tidak konsisten antar versi/setup MCP kustom — anggap sebagai petunjuk arah, bukan kode siap pakai.

---

*Dokumen ini melengkapi SOP Workflow dengan referensi eksekusi teknis konkret, sebagai bagian dari paket dokumentasi pra-produksi Lentera Pudar. Living document — update seiring temuan baru selama produksi.*

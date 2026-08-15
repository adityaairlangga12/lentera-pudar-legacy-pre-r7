import bpy
import math

# 1. Clean default objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# 2. Material Helper (The Triad & Sub-Palettes)
def create_material(name, color_hex):
    mat = bpy.data.materials.get(name)
    if not mat:
        mat = bpy.data.materials.new(name=name)
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes.get('Principled BSDF')
        hex_val = color_hex.lstrip('#')
        r = int(hex_val[0:2], 16) / 255.0
        g = int(hex_val[2:4], 16) / 255.0
        b = int(hex_val[4:6], 16) / 255.0
        bsdf.inputs['Base Color'].default_value = (r**2.2, g**2.2, b**2.2, 1.0)
        bsdf.inputs['Roughness'].default_value = 0.9
    return mat

mat_hair = create_material("Mat_Hair", "#9E9E9E")
mat_hair_hl = create_material("Mat_HairHighlight", "#E0E0E0")
mat_skin = create_material("Mat_Skin", "#E0A96D")
mat_eyepatch = create_material("Mat_Eyepatch", "#141013")
mat_scarf = create_material("Mat_Scarf", "#F4B860")
mat_robe = create_material("Mat_Robe", "#2A211C")
mat_baldric = create_material("Mat_Baldric", "#7A4B28")
mat_frost = create_material("Mat_FrostArm", "#4A6FA5")
mat_crystal = create_material("Mat_FrostCrystal", "#99B9E0")
mat_bandage = create_material("Mat_Bandage", "#D7CCC8")
mat_boots = create_material("Mat_Boots", "#5C3A21")

parts = []

# COORDINATE ORIENTATION:
# In Blender -> glTF export (+Z forward, Y up):
# FRONT of character faces -Y (or toward viewer in South view)
# BACK of character faces +Y
# Character's LEFT is -X (Screen Left when viewed from South)
# Character's RIGHT is +X (Screen Right when viewed from South)

# --- A. HEAD, HAIR & ASYMMETRICAL FACE ---
# Head Base
bpy.ops.mesh.primitive_cube_add(size=0.42, location=(0, 0, 1.45))
head = bpy.context.active_object
head.name = "Head_Base"
head.scale = (0.95, 0.90, 1.0)
head.data.materials.append(mat_skin)
parts.append(head)

# Messy Hair Top & Back (Sitting on +Y back & top)
bpy.ops.mesh.primitive_cube_add(size=0.46, location=(0, 0.05, 1.54))
hair_top = bpy.context.active_object
hair_top.name = "Hair_Top"
hair_top.scale = (1.02, 1.05, 0.70)
hair_top.data.materials.append(mat_hair)
parts.append(hair_top)

# Slanted Bangs on FRONT (-Y)
bpy.ops.mesh.primitive_cube_add(size=0.22, location=(-0.08, -0.18, 1.52))
bangs_l = bpy.context.active_object
bangs_l.name = "Hair_Bangs_L"
bangs_l.rotation_euler = (math.radians(-20), 0, math.radians(-15))
bangs_l.scale = (1.1, 0.3, 0.8)
bangs_l.data.materials.append(mat_hair_hl)
parts.append(bangs_l)

bpy.ops.mesh.primitive_cube_add(size=0.20, location=(0.10, -0.18, 1.48))
bangs_r = bpy.context.active_object
bangs_r.name = "Hair_Bangs_R"
bangs_r.rotation_euler = (math.radians(-25), 0, math.radians(20))
bangs_r.scale = (1.0, 0.3, 0.9)
bangs_r.data.materials.append(mat_hair)
parts.append(bangs_r)

# Eyepatch over RIGHT eye (X > 0, on FRONT -Y)
bpy.ops.mesh.primitive_cube_add(size=0.14, location=(0.10, -0.19, 1.44))
eyepatch = bpy.context.active_object
eyepatch.name = "Eyepatch"
eyepatch.rotation_euler = (math.radians(-12), 0, math.radians(-8))
eyepatch.scale = (0.9, 0.2, 0.9)
eyepatch.data.materials.append(mat_eyepatch)
parts.append(eyepatch)

# Eyepatch Strap (Ring around head)
bpy.ops.mesh.primitive_torus_add(major_radius=0.22, minor_radius=0.015, major_segments=10, minor_segments=4, location=(0, 0, 1.44))
strap = bpy.context.active_object
strap.name = "Eyepatch_Strap"
strap.rotation_euler = (math.radians(-8), math.radians(10), 0)
strap.data.materials.append(mat_eyepatch)
parts.append(strap)

# Left Eye (Open Eye Accent on FRONT -Y, X < 0)
bpy.ops.mesh.primitive_cube_add(size=0.06, location=(-0.10, -0.19, 1.44))
eye_l = bpy.context.active_object
eye_l.name = "Eye_L"
eye_l.scale = (1.2, 0.2, 0.7)
eye_l.data.materials.append(mat_eyepatch)
parts.append(eye_l)


# --- B. SCARF OF AINA (#F4B860 2700K) ---
# Thick Collar Ring
bpy.ops.mesh.primitive_torus_add(major_radius=0.24, minor_radius=0.09, major_segments=12, minor_segments=8, location=(0, 0, 1.20))
scarf_collar = bpy.context.active_object
scarf_collar.name = "Scarf_Collar"
scarf_collar.scale = (1.0, 0.95, 0.9)
scarf_collar.data.materials.append(mat_scarf)
parts.append(scarf_collar)

# Draping Scarf Tail on the BACK (+Y, hanging down to hip)
# Segment 1 (Upper back)
bpy.ops.mesh.primitive_cube_add(size=0.18, location=(-0.05, 0.22, 1.08))
tail_1 = bpy.context.active_object
tail_1.name = "Scarf_Tail_01"
tail_1.rotation_euler = (math.radians(12), 0, math.radians(5))
tail_1.scale = (1.1, 0.35, 1.3)
tail_1.data.materials.append(mat_scarf)
parts.append(tail_1)

# Segment 2 (Mid back)
bpy.ops.mesh.primitive_cube_add(size=0.16, location=(-0.06, 0.25, 0.88))
tail_2 = bpy.context.active_object
tail_2.name = "Scarf_Tail_02"
tail_2.rotation_euler = (math.radians(8), 0, math.radians(-4))
tail_2.scale = (1.0, 0.30, 1.4)
tail_2.data.materials.append(mat_scarf)
parts.append(tail_2)

# Segment 3 (Lower tail / tip)
bpy.ops.mesh.primitive_cube_add(size=0.14, location=(-0.08, 0.26, 0.68))
tail_3 = bpy.context.active_object
tail_3.name = "Scarf_Tail_03"
tail_3.rotation_euler = (math.radians(-5), 0, math.radians(8))
tail_3.scale = (0.9, 0.25, 1.5)
tail_3.data.materials.append(mat_scarf)
parts.append(tail_3)


# --- C. TORSO, ROBE, BALDRIC HARNESS & POUCH ---
# Torso Body
bpy.ops.mesh.primitive_cube_add(size=0.38, location=(0, 0, 0.96))
torso = bpy.context.active_object
torso.name = "Torso_Robe"
torso.scale = (0.92, 0.68, 1.15)
torso.data.materials.append(mat_robe)
parts.append(torso)

# Robe Skirt
bpy.ops.mesh.primitive_cylinder_add(radius=0.23, depth=0.30, vertices=8, location=(0, 0, 0.68))
skirt = bpy.context.active_object
skirt.name = "Robe_Skirt"
skirt.scale = (0.95, 0.75, 1.0)
skirt.data.materials.append(mat_robe)
parts.append(skirt)

# Baldric Harness across the FRONT CHEST (-Y)
bpy.ops.mesh.primitive_cube_add(size=0.48, location=(0.02, -0.05, 0.98))
baldric = bpy.context.active_object
baldric.name = "Baldric_Harness"
baldric.rotation_euler = (0, math.radians(-38), 0)
baldric.scale = (0.16, 0.72, 1.02)
baldric.data.materials.append(mat_baldric)
parts.append(baldric)

# Waist Travel Pouch (Left hip, X < 0)
bpy.ops.mesh.primitive_cube_add(size=0.12, location=(-0.20, -0.08, 0.76))
pouch = bpy.context.active_object
pouch.name = "Travel_Pouch"
pouch.rotation_euler = (0, 0, math.radians(10))
pouch.scale = (0.9, 0.8, 1.2)
pouch.data.materials.append(mat_baldric)
parts.append(pouch)


# --- D. LEFT ARM: CURSED FROST CRYSTAL ARM (#4A6FA5) ---
# Upper Arm (Left, X < 0)
bpy.ops.mesh.primitive_cylinder_add(radius=0.075, depth=0.26, vertices=8, location=(-0.30, 0, 1.04))
arm_l_up = bpy.context.active_object
arm_l_up.name = "Arm_L_Upper_Frost"
arm_l_up.rotation_euler = (0, math.radians(-14), 0)
arm_l_up.data.materials.append(mat_frost)
parts.append(arm_l_up)

# Forearm (Left - Jagged Ice)
bpy.ops.mesh.primitive_cylinder_add(radius=0.085, depth=0.28, vertices=8, location=(-0.36, -0.02, 0.82))
arm_l_fore = bpy.context.active_object
arm_l_fore.name = "Arm_L_Forearm_Frost"
arm_l_fore.rotation_euler = (0, math.radians(-10), 0)
arm_l_fore.data.materials.append(mat_frost)
parts.append(arm_l_fore)

# Ice Shard Spikes
bpy.ops.mesh.primitive_cone_add(radius1=0.045, depth=0.14, vertices=5, location=(-0.34, -0.08, 1.08))
shard_1 = bpy.context.active_object
shard_1.name = "Ice_Shard_01"
shard_1.rotation_euler = (math.radians(30), math.radians(45), 0)
shard_1.data.materials.append(mat_crystal)
parts.append(shard_1)

bpy.ops.mesh.primitive_cone_add(radius1=0.04, depth=0.12, vertices=5, location=(-0.42, -0.05, 0.84))
shard_2 = bpy.context.active_object
shard_2.name = "Ice_Shard_02"
shard_2.rotation_euler = (0, math.radians(-40), math.radians(-20))
shard_2.data.materials.append(mat_crystal)
parts.append(shard_2)

# Cursed Fist
bpy.ops.mesh.primitive_cube_add(size=0.11, location=(-0.39, -0.04, 0.64))
fist_l = bpy.context.active_object
fist_l.name = "Fist_L_Cursed"
fist_l.scale = (0.9, 1.0, 1.1)
fist_l.data.materials.append(mat_frost)
parts.append(fist_l)


# --- E. RIGHT ARM: BANDAGED NORMAL ARM (#D7CCC8 / #2A211C) ---
# Upper Arm (Right, X > 0)
bpy.ops.mesh.primitive_cylinder_add(radius=0.075, depth=0.26, vertices=8, location=(0.30, 0, 1.04))
arm_r_up = bpy.context.active_object
arm_r_up.name = "Arm_R_Upper"
arm_r_up.rotation_euler = (0, math.radians(14), 0)
arm_r_up.data.materials.append(mat_robe)
parts.append(arm_r_up)

# Forearm (Right - Bandaged)
bpy.ops.mesh.primitive_cylinder_add(radius=0.08, depth=0.28, vertices=8, location=(0.36, -0.02, 0.82))
arm_r_fore = bpy.context.active_object
arm_r_fore.name = "Arm_R_Forearm_Bandage"
arm_r_fore.rotation_euler = (0, math.radians(10), 0)
arm_r_fore.data.materials.append(mat_bandage)
parts.append(arm_r_fore)

# Right Fist
bpy.ops.mesh.primitive_cube_add(size=0.10, location=(0.39, -0.04, 0.64))
fist_r = bpy.context.active_object
fist_r.name = "Fist_R_Normal"
fist_r.scale = (0.9, 1.0, 1.0)
fist_r.data.materials.append(mat_bandage)
parts.append(fist_r)


# --- F. LEGS & TRAVEL BOOTS (#5C3A21) ---
# Thigh Left
bpy.ops.mesh.primitive_cylinder_add(radius=0.085, depth=0.28, vertices=8, location=(-0.13, 0, 0.48))
thigh_l = bpy.context.active_object
thigh_l.name = "Thigh_L"
thigh_l.data.materials.append(mat_robe)
parts.append(thigh_l)

# Boot Left
bpy.ops.mesh.primitive_cylinder_add(radius=0.09, depth=0.30, vertices=8, location=(-0.13, 0, 0.22))
boot_l = bpy.context.active_object
boot_l.name = "Boot_L"
boot_l.data.materials.append(mat_boots)
parts.append(boot_l)

# Foot Toe Left (Forward kick on -Y)
bpy.ops.mesh.primitive_cube_add(size=0.12, location=(-0.13, -0.06, 0.08))
toe_l = bpy.context.active_object
toe_l.name = "Toe_L"
toe_l.scale = (1.1, 1.4, 0.7)
toe_l.data.materials.append(mat_boots)
parts.append(toe_l)

# Thigh Right
bpy.ops.mesh.primitive_cylinder_add(radius=0.085, depth=0.28, vertices=8, location=(0.13, 0, 0.48))
thigh_r = bpy.context.active_object
thigh_r.name = "Thigh_R"
thigh_r.data.materials.append(mat_robe)
parts.append(thigh_r)

# Boot Right
bpy.ops.mesh.primitive_cylinder_add(radius=0.09, depth=0.30, vertices=8, location=(0.13, 0, 0.22))
boot_r = bpy.context.active_object
boot_r.name = "Boot_R"
boot_r.data.materials.append(mat_boots)
parts.append(boot_r)

# Foot Toe Right (Forward kick on -Y)
bpy.ops.mesh.primitive_cube_add(size=0.12, location=(0.13, -0.06, 0.08))
toe_r = bpy.context.active_object
toe_r.name = "Toe_R"
toe_r.scale = (1.1, 1.4, 0.7)
toe_r.data.materials.append(mat_boots)
parts.append(toe_r)


# --- G. JOIN & OPTIMIZE MESH ---
bpy.ops.object.select_all(action='DESELECT')
for p in parts:
    p.select_set(True)
bpy.context.view_layer.objects.active = torso
bpy.ops.object.join()

kaelen = bpy.context.active_object
kaelen.name = "Kaelen_V3"

# Enforce Flat Shading
for f in kaelen.data.polygons:
    f.use_smooth = False

# Apply all transforms
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

# Calculate Triangles
tri_count = sum([len(p.vertices) - 2 for p in kaelen.data.polygons])
print(f"KAELEN_V3_TRIS:{tri_count}")

# Export glTF 2.0 (+Z forward, Y up)
export_path = "D:/GodotProjects/Lentera-Pudar/Assets/Models/Kaelen_V3.gltf"
bpy.ops.export_scene.gltf(
    filepath=export_path,
    export_format='GLTF_SEPARATE',
    export_yup=True,
    export_apply=True
)
print(f"EXPORT_SUCCESS:{export_path}")

import bpy
import math

# 1. Clean default objects
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# 2. Create Materials (The Triad of Lentera Pudar)
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

mat_dark = create_material("Mat_DarkNeutral", "#2A211C")
mat_yellow = create_material("Mat_WarmYellow", "#F4B860")
mat_blue = create_material("Mat_ColdBlue", "#4A6FA5")

# 3. Build Low-Poly Test Dummy (Humanoid Chibi 1:3.2, Total Height ~1.7m)
parts = []

# Head (Cube beveled slightly or icosphere)
bpy.ops.mesh.primitive_cube_add(size=0.45, location=(0, 0, 1.45))
head = bpy.context.active_object
head.name = "Head"
head.data.materials.append(mat_dark)
parts.append(head)

# Scarf (Torus around neck with 12 segments)
bpy.ops.mesh.primitive_torus_add(major_radius=0.22, minor_radius=0.08, major_segments=12, minor_segments=8, location=(0, 0, 1.20))
scarf = bpy.context.active_object
scarf.name = "Scarf"
scarf.data.materials.append(mat_yellow)
parts.append(scarf)

# Torso (Chibi box)
bpy.ops.mesh.primitive_cube_add(size=0.4, location=(0, 0, 0.95))
torso = bpy.context.active_object
torso.name = "Torso"
torso.scale = (0.9, 0.6, 1.1)
torso.data.materials.append(mat_dark)
parts.append(torso)

# Left Arm (Cursed Frost Arm - Blue with 8-segments)
bpy.ops.mesh.primitive_cylinder_add(radius=0.08, depth=0.45, vertices=8, location=(-0.30, 0, 0.95))
arm_l = bpy.context.active_object
arm_l.name = "Arm_L_Cursed"
arm_l.rotation_euler = (0, math.radians(-15), 0)
arm_l.data.materials.append(mat_blue)
parts.append(arm_l)

# Right Arm (Normal Arm - Dark Neutral with 8-segments)
bpy.ops.mesh.primitive_cylinder_add(radius=0.08, depth=0.45, vertices=8, location=(0.30, 0, 0.95))
arm_r = bpy.context.active_object
arm_r.name = "Arm_R_Normal"
arm_r.rotation_euler = (0, math.radians(15), 0)
arm_r.data.materials.append(mat_dark)
parts.append(arm_r)

# Left Leg (8-segments)
bpy.ops.mesh.primitive_cylinder_add(radius=0.09, depth=0.60, vertices=8, location=(-0.14, 0, 0.40))
leg_l = bpy.context.active_object
leg_l.name = "Leg_L"
leg_l.data.materials.append(mat_dark)
parts.append(leg_l)

# Right Leg (8-segments)
bpy.ops.mesh.primitive_cylinder_add(radius=0.09, depth=0.60, vertices=8, location=(0.14, 0, 0.40))
leg_r = bpy.context.active_object
leg_r.name = "Leg_R"
leg_r.data.materials.append(mat_dark)
parts.append(leg_r)

# 4. Join parts into single test dummy mesh
bpy.ops.object.select_all(action='DESELECT')
for p in parts:
    p.select_set(True)
bpy.context.view_layer.objects.active = torso
bpy.ops.object.join()

dummy = bpy.context.active_object
dummy.name = "TestDummy"

# Set Flat Shading
for f in dummy.data.polygons:
    f.use_smooth = False

# Apply all transforms
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

# Validate Poly Count
tri_count = sum([len(p.vertices) - 2 for p in dummy.data.polygons])
print(f"TEST_DUMMY_TRIS:{tri_count}")

# 5. Export glTF 2.0 (+Z forward, Y up)
export_path = "D:/GodotProjects/Lentera-Pudar/Assets/Models/test_dummy.gltf"
bpy.ops.export_scene.gltf(
    filepath=export_path,
    export_format='GLTF_SEPARATE',
    export_yup=True,
    export_apply=True
)
print(f"EXPORT_SUCCESS:{export_path}")

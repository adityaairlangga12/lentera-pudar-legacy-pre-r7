import bpy
import bmesh
import math
from mathutils import Vector, Matrix

# ==============================================================================
# LENTERA PUDAR - KAELEN V3 MASTERPIECE GENERATOR (BLENDER 5.2 LTS)
# High-Fidelity Stylized Chibi 1:3.2 Low-Poly Character
# ==============================================================================

# 1. Clean Scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# 2. Advanced Material Creator (The Triad Kelvin Palette + Shading Gradients)
def create_mat(name, hex_code, roughness=0.85, emission=0.0):
    mat = bpy.data.materials.get(name)
    if not mat:
        mat = bpy.data.materials.new(name=name)
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        bsdf = nodes.get('Principled BSDF')
        
        h = hex_code.lstrip('#')
        r = (int(h[0:2], 16) / 255.0) ** 2.2
        g = (int(h[2:4], 16) / 255.0) ** 2.2
        b = (int(h[4:6], 16) / 255.0) ** 2.2
        
        bsdf.inputs['Base Color'].default_value = (r, g, b, 1.0)
        bsdf.inputs['Roughness'].default_value = roughness
        if emission > 0.0:
            if 'Emission Color' in bsdf.inputs:
                bsdf.inputs['Emission Color'].default_value = (r, g, b, 1.0)
                bsdf.inputs['Emission Strength'].default_value = emission
            elif 'Emission' in bsdf.inputs:
                bsdf.inputs['Emission'].default_value = (r, g, b, 1.0)
    return mat

# The Triad & Character Palettes
mat_hair_base   = create_mat("K_HairBase", "#858585")
mat_hair_mid    = create_mat("K_HairMid", "#A8A8A8")
mat_hair_high   = create_mat("K_HairHighlight", "#D6D6D6")
mat_skin        = create_mat("K_Skin", "#E8B282")
mat_skin_shadow = create_mat("K_SkinShadow", "#C48A5E")
mat_eyepatch    = create_mat("K_Eyepatch", "#141013", roughness=0.95)
mat_buckle      = create_mat("K_SilverBuckle", "#D0D7DE", roughness=0.3)
mat_scarf_main  = create_mat("K_ScarfMain", "#F4B860", roughness=0.8, emission=0.15)
mat_scarf_high  = create_mat("K_ScarfHigh", "#FFD185", roughness=0.8, emission=0.25)
mat_scarf_shad  = create_mat("K_ScarfShadow", "#C78732", roughness=0.9)
mat_robe_base   = create_mat("K_RobeBase", "#241D1A")
mat_robe_trim   = create_mat("K_RobeTrim", "#191310")
mat_baldric     = create_mat("K_BaldricLeather", "#6E4023")
mat_frost_base  = create_mat("K_FrostBase", "#41679E", roughness=0.5)
mat_frost_high  = create_mat("K_FrostCrystal", "#9EC5E8", roughness=0.2, emission=0.3)
mat_frost_deep  = create_mat("K_FrostDeep", "#253E6B", roughness=0.6)
mat_bandage     = create_mat("K_BandageCloth", "#D4C8BC")
mat_boots_base  = create_mat("K_BootsLeather", "#4A2E1B")
mat_boots_sole  = create_mat("K_BootsSole", "#23160D")

objects_to_join = []

def add_mesh_box(name, loc, size, rot=(0,0,0), mat=mat_robe_base):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc)
    obj = bpy.context.active_object
    obj.name = name
    obj.scale = size
    obj.rotation_euler = (math.radians(rot[0]), math.radians(rot[1]), math.radians(rot[2]))
    obj.data.materials.append(mat)
    objects_to_join.append(obj)
    return obj

def add_mesh_cyl(name, loc, radius, depth, verts=8, rot=(0,0,0), mat=mat_robe_base):
    bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=depth, vertices=verts, location=loc)
    obj = bpy.context.active_object
    obj.name = name
    obj.rotation_euler = (math.radians(rot[0]), math.radians(rot[1]), math.radians(rot[2]))
    obj.data.materials.append(mat)
    objects_to_join.append(obj)
    return obj

def add_mesh_cone(name, loc, r1, depth, verts=5, rot=(0,0,0), mat=mat_frost_high):
    bpy.ops.mesh.primitive_cone_add(radius1=r1, depth=depth, vertices=verts, location=loc)
    obj = bpy.context.active_object
    obj.name = name
    obj.rotation_euler = (math.radians(rot[0]), math.radians(rot[1]), math.radians(rot[2]))
    obj.data.materials.append(mat)
    objects_to_join.append(obj)
    return obj

# ==============================================================================
# A. HEAD & FACIAL ANATOMY (CHIBI PROPORTION ~33% HEIGHT, 1.35m to 1.75m)
# ==============================================================================
# Head Core (Faceted Chibi Head)
head_core = add_mesh_box("Head_Core", (0, -0.01, 1.48), (0.42, 0.40, 0.38), mat=mat_skin)

# Jaw / Chin Taper
chin = add_mesh_box("Chin_Taper", (0, -0.07, 1.33), (0.28, 0.26, 0.12), (15, 0, 0), mat=mat_skin_shadow)

# Eyepatch on RIGHT Eye (X > 0, Front -Y)
ep_patch = add_mesh_box("Eyepatch_Plate", (0.10, -0.21, 1.47), (0.13, 0.04, 0.14), (-12, 0, -8), mat=mat_eyepatch)
ep_strap_f = add_mesh_box("Eyepatch_Strap_F", (0.01, -0.20, 1.48), (0.41, 0.02, 0.035), (-5, 12, 0), mat=mat_eyepatch)
ep_strap_b = add_mesh_box("Eyepatch_Strap_B", (0.0, 0.19, 1.48), (0.43, 0.02, 0.035), (5, -12, 0), mat=mat_eyepatch)

# Left Eye (Melancholic Open Eye, X < 0, Front -Y)
eye_l_sclera = add_mesh_box("Eye_L_White", (-0.11, -0.21, 1.47), (0.09, 0.02, 0.07), (-10, 0, 0), mat=mat_hair_high)
eye_l_pupil  = add_mesh_box("Eye_L_Pupil", (-0.11, -0.22, 1.47), (0.05, 0.02, 0.06), (-10, 0, 0), mat=mat_eyepatch)
eye_l_brow   = add_mesh_box("Eye_L_Brow",  (-0.11, -0.215, 1.53), (0.11, 0.03, 0.03), (-15, 0, 10), mat=mat_hair_base)

# Sculpted 3D Hair - Layered Bangs & Spikes
# Top Dome
add_mesh_box("Hair_Dome", (0, 0.04, 1.62), (0.46, 0.44, 0.20), (5, 0, 0), mat=mat_hair_mid)
# Back Shaggy Mane
add_mesh_box("Hair_Back_01", (0, 0.18, 1.48), (0.44, 0.16, 0.36), (15, 0, 0), mat=mat_hair_base)
add_mesh_box("Hair_Back_02", (0, 0.20, 1.34), (0.38, 0.14, 0.22), (25, 0, 0), mat=mat_hair_base)
# Slanted Front Bangs (Left Side & Center)
add_mesh_box("Bang_Left_Main", (-0.12, -0.19, 1.56), (0.16, 0.10, 0.18), (-25, 0, -18), mat=mat_hair_high)
add_mesh_box("Bang_Center_Wisp", (0.01, -0.20, 1.57), (0.14, 0.08, 0.16), (-30, 0, 8), mat=mat_hair_mid)
add_mesh_box("Bang_Right_Side", (0.16, -0.17, 1.55), (0.14, 0.09, 0.17), (-20, 0, 22), mat=mat_hair_base)
# Sideburn Tufts
add_mesh_box("Hair_Side_L", (-0.21, -0.06, 1.45), (0.10, 0.22, 0.28), (10, 0, -12), mat=mat_hair_mid)
add_mesh_box("Hair_Side_R", (0.21, -0.06, 1.45), (0.10, 0.22, 0.28), (10, 0, 12), mat=mat_hair_base)


# ==============================================================================
# B. SCARF OF AINA (#F4B860 2700K Kelvin - Tiered Collar & Back Tail S-Wave)
# ==============================================================================
# Multi-Tier Scarf Collar (Wraps leher bervolume tebal)
add_mesh_cyl("Scarf_Tier_Bottom", (0, 0, 1.25), 0.26, 0.10, verts=10, mat=mat_scarf_shad)
add_mesh_cyl("Scarf_Tier_Mid",    (0, -0.02, 1.29), 0.28, 0.10, verts=10, rot=(-6, 0, 0), mat=mat_scarf_main)
add_mesh_cyl("Scarf_Tier_Top",    (0, -0.03, 1.34), 0.25, 0.08, verts=10, rot=(-10, 0, 0), mat=mat_scarf_high)

# Draping Scarf Tail on the BACK (+Y) with Organic Flow
# Segment 1 (Origin at back neck, curving outward)
add_mesh_box("Scarf_Tail_01", (-0.05, 0.20, 1.18), (0.20, 0.07, 0.22), (18, -4, 6), mat=mat_scarf_high)
# Segment 2 (Mid back, overlapping downwards)
add_mesh_box("Scarf_Tail_02", (-0.06, 0.25, 0.98), (0.18, 0.06, 0.26), (10, 2, -4), mat=mat_scarf_main)
# Segment 3 (Lower back, draping over hip)
add_mesh_box("Scarf_Tail_03", (-0.08, 0.26, 0.76), (0.16, 0.055, 0.26), (-4, 4, 8), mat=mat_scarf_main)
# Segment 4 (Tapered trailing tip)
add_mesh_box("Scarf_Tail_04", (-0.10, 0.24, 0.54), (0.12, 0.045, 0.24), (-12, 0, -10), mat=mat_scarf_shad)


# ==============================================================================
# C. TORSO, WANDERER ROBE, BALDRIC HARNESS & TRAVEL POUCH
# ==============================================================================
# Chest & Upper Torso
add_mesh_box("Torso_Chest", (0, 0, 1.06), (0.36, 0.28, 0.30), mat=mat_robe_base)
# Waist & Belt
add_mesh_box("Torso_Waist", (0, 0, 0.88), (0.33, 0.25, 0.20), mat=mat_robe_trim)
# Belt Band
add_mesh_box("Leather_Belt", (0, 0, 0.82), (0.35, 0.27, 0.06), mat=mat_baldric)

# Lower Coat / Tunic Skirt with Movement Flare & Center Split
add_mesh_box("Robe_Skirt_Back",  (0, 0.07, 0.68), (0.38, 0.16, 0.32), (12, 0, 0), mat=mat_robe_base)
add_mesh_box("Robe_Skirt_L",     (-0.12, -0.02, 0.68), (0.16, 0.26, 0.32), (0, 0, -8), mat=mat_robe_base)
add_mesh_box("Robe_Skirt_R",     (0.12, -0.02, 0.68), (0.16, 0.26, 0.32), (0, 0, 8), mat=mat_robe_base)

# Baldric Harness (Diagonal Leather Strap across Chest: Right Shoulder to Left Hip)
add_mesh_box("Baldric_Strap_F", (0.01, -0.15, 1.02), (0.07, 0.03, 0.44), (0, -36, 0), mat=mat_baldric)
add_mesh_box("Baldric_Strap_B", (0.01, 0.15, 1.02), (0.07, 0.03, 0.44), (0, 36, 0), mat=mat_baldric)
# Silver Metal Buckle on Chest
add_mesh_box("Baldric_Buckle", (0.04, -0.165, 1.06), (0.09, 0.02, 0.09), (0, -36, 0), mat=mat_buckle)

# Travel Pouch (Left Hip, X < 0)
add_mesh_box("Pouch_Body", (-0.20, -0.08, 0.78), (0.10, 0.14, 0.16), (0, 0, 10), mat=mat_baldric)
add_mesh_box("Pouch_Flap", (-0.205, -0.08, 0.84), (0.11, 0.15, 0.06), (0, 0, 10), mat=mat_boots_base)


# ==============================================================================
# D. LEFT ARM: ASYMMETRICAL CURSED FROST CRYSTAL ARM (#4A6FA5 / #99B9E0)
# ==============================================================================
# Ice Shoulder Pauldron (Faceted Ice Spike)
add_mesh_cone("Ice_Pauldron_Main", (-0.26, 0.0, 1.18), 0.09, 0.18, verts=5, rot=(15, -45, 0), mat=mat_frost_high)
add_mesh_cone("Ice_Pauldron_Sub",  (-0.28, -0.06, 1.12), 0.06, 0.14, verts=4, rot=(-30, -30, 20), mat=mat_frost_base)

# Cursed Upper Arm (Faceted Ice Segments)
add_mesh_cyl("Arm_L_Upper_Ice", (-0.25, 0, 1.02), 0.08, 0.24, verts=6, rot=(0, 0, -15), mat=mat_frost_deep)

# Cursed Forearm (Jagged crystalline mass)
add_mesh_cyl("Arm_L_Fore_Ice", (-0.31, -0.02, 0.80), 0.09, 0.26, verts=6, rot=(0, 0, -8), mat=mat_frost_base)

# Pointed Ice Crystals along Forearm Edge
add_mesh_cone("Ice_Elbow_Spike", (-0.37, 0.04, 0.84), 0.05, 0.14, verts=4, rot=(0, 45, 40), mat=mat_frost_high)
add_mesh_cone("Ice_Wrist_Spike", (-0.36, -0.05, 0.72), 0.045, 0.12, verts=4, rot=(-20, -50, 0), mat=mat_frost_high)

# Cursed Crystalline Fist (Sharp jagged knuckles)
add_mesh_box("Fist_L_IceCore", (-0.34, -0.04, 0.62), (0.11, 0.13, 0.13), (0, 0, -10), mat=mat_frost_base)
add_mesh_cone("Fist_L_Knuckle", (-0.35, -0.09, 0.61), 0.04, 0.08, verts=4, rot=(-80, 0, 0), mat=mat_frost_high)


# ==============================================================================
# E. RIGHT ARM: NORMAL WANDERER ARM WITH BANDAGES (#D7CCC8 / #2A211C)
# ==============================================================================
# Shoulder Sleeve (Dark Robe)
add_mesh_cyl("Arm_R_Shoulder", (0.24, 0, 1.12), 0.085, 0.14, verts=8, rot=(0, 0, 15), mat=mat_robe_base)
# Upper Arm
add_mesh_cyl("Arm_R_Upper", (0.26, 0, 1.00), 0.075, 0.20, verts=8, rot=(0, 0, 12), mat=mat_robe_trim)

# Forearm with Cloth Bandages
add_mesh_cyl("Arm_R_Fore_Bandage", (0.31, -0.02, 0.80), 0.08, 0.24, verts=8, rot=(0, 0, 8), mat=mat_bandage)
# Bandage Wrap Ribbons (Aksen lilitan kain)
add_mesh_cyl("Bandage_Ring_01", (0.315, -0.02, 0.84), 0.086, 0.04, verts=8, rot=(0, 4, 8), mat=mat_hair_high)
add_mesh_cyl("Bandage_Ring_02", (0.32, -0.02, 0.74), 0.086, 0.04, verts=8, rot=(0, -4, 8), mat=mat_skin_shadow)

# Right Fist (Leather wrap hand)
add_mesh_box("Fist_R_Hand", (0.33, -0.04, 0.62), (0.10, 0.12, 0.12), (0, 0, 8), mat=mat_bandage)


# ==============================================================================
# F. LEGS & STURDY TRAVEL BOOTS (#5C3A21 / #23160D)
# ==============================================================================
# Left Thigh
add_mesh_cyl("Thigh_L", (-0.11, 0, 0.52), 0.08, 0.24, verts=8, mat=mat_robe_trim)
# Left Boot Calf
add_mesh_cyl("Boot_L_Calf", (-0.11, 0, 0.30), 0.095, 0.26, verts=8, mat=mat_boots_base)
# Left Boot Top Cuff (Lipatan atas boot)
add_mesh_cyl("Boot_L_Cuff", (-0.11, 0, 0.40), 0.105, 0.06, verts=8, mat=mat_baldric)
# Left Boot Foot & Sole
add_mesh_box("Boot_L_Foot", (-0.11, -0.07, 0.12), (0.12, 0.18, 0.14), (6, 0, 0), mat=mat_boots_base)
add_mesh_box("Boot_L_Sole", (-0.11, -0.07, 0.04), (0.13, 0.20, 0.05), (6, 0, 0), mat=mat_boots_sole)

# Right Thigh
add_mesh_cyl("Thigh_R", (0.11, 0, 0.52), 0.08, 0.24, verts=8, mat=mat_robe_trim)
# Right Boot Calf
add_mesh_cyl("Boot_R_Calf", (0.11, 0, 0.30), 0.095, 0.26, verts=8, mat=mat_boots_base)
# Right Boot Top Cuff
add_mesh_cyl("Boot_R_Cuff", (0.11, 0, 0.40), 0.105, 0.06, verts=8, mat=mat_baldric)
# Right Boot Foot & Sole
add_mesh_box("Boot_R_Foot", (0.11, -0.07, 0.12), (0.12, 0.18, 0.14), (6, 0, 0), mat=mat_boots_base)
add_mesh_box("Boot_R_Sole", (0.11, -0.07, 0.04), (0.13, 0.20, 0.05), (6, 0, 0), mat=mat_boots_sole)


# ==============================================================================
# G. UNIFY MESH, ENFORCE FLAT SHADING & EXPORT GLTF 2.0
# ==============================================================================
bpy.ops.object.select_all(action='DESELECT')
for obj in objects_to_join:
    obj.select_set(True)
bpy.context.view_layer.objects.active = head_core
bpy.ops.object.join()

kaelen_master = bpy.context.active_object
kaelen_master.name = "Kaelen_V3"

# Enforce Strict Flat Shading
for f in kaelen_master.data.polygons:
    f.use_smooth = False

# Apply all transforms
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

# Calculate Triangles
tri_count = sum([len(p.vertices) - 2 for p in kaelen_master.data.polygons])
print(f"KAELEN_V3_MASTERPIECE_TRIS:{tri_count}")

# glTF 2.0 Export
export_path = "D:/GodotProjects/Lentera-Pudar/Assets/Models/Kaelen_V3.gltf"
bpy.ops.export_scene.gltf(
    filepath=export_path,
    export_format='GLTF_SEPARATE',
    export_yup=True,
    export_apply=True
)
print(f"EXPORT_SUCCESS:{export_path}")

import bpy
import bmesh
import math
import os
from mathutils import Vector, Matrix, Euler

# ==============================================================================
# LENTERA PUDAR - KAELEN V3 STUDIO-GRADE MASTERPIECE GENERATOR (BLENDER 5.2 LTS)
# 100% Unified Anatomical Chibi Sculpting, Hero Stance, Draped Scarf & JRPG Hair
# ==============================================================================

# 1. Clean Scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# 2. Materials Setup (The Triad of Lentera Pudar)
def create_studio_mat(name, hex_code, roughness=1.0, emission=0.0):
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
        if 'Specular IOR Level' in bsdf.inputs:
            bsdf.inputs['Specular IOR Level'].default_value = 0.0
        elif 'Specular' in bsdf.inputs:
            bsdf.inputs['Specular'].default_value = 0.0
            
        if emission > 0.0:
            if 'Emission Color' in bsdf.inputs:
                bsdf.inputs['Emission Color'].default_value = (r, g, b, 1.0)
                bsdf.inputs['Emission Strength'].default_value = emission
            elif 'Emission' in bsdf.inputs:
                bsdf.inputs['Emission'].default_value = (r, g, b, 1.0)
    return mat

mat_hair_top    = create_studio_mat("K_HairTop", "#D6D6D6")       # Highlights
mat_hair_mid    = create_studio_mat("K_HairMid", "#9E9E9E")       # Base Gray
mat_hair_dark   = create_studio_mat("K_HairDark", "#6E6E6E")      # Shadows
mat_skin        = create_studio_mat("K_Skin", "#E8B282")          # Melancholic Warm Skin
mat_skin_shadow = create_studio_mat("K_SkinShadow", "#C48A5E")
mat_eyepatch    = create_studio_mat("K_Eyepatch", "#141013", roughness=0.95)
mat_buckle      = create_studio_mat("K_SilverBuckle", "#D0D7DE", roughness=0.3)
mat_eye_white   = create_studio_mat("K_EyeWhite", "#FFFFFF", roughness=0.5)
mat_eye_pupil   = create_studio_mat("K_EyePupil", "#141013", roughness=0.5)
mat_scarf_main  = create_studio_mat("K_ScarfMain", "#F4B860", roughness=0.9, emission=0.15)
mat_scarf_high  = create_studio_mat("K_ScarfHigh", "#FFD185", roughness=0.9, emission=0.25)
mat_scarf_shad  = create_studio_mat("K_ScarfShadow", "#C78732", roughness=0.95)
mat_robe_base   = create_studio_mat("K_RobeBase", "#241D1A")
mat_robe_trim   = create_studio_mat("K_RobeTrim", "#191310")
mat_baldric     = create_studio_mat("K_BaldricLeather", "#6E4023")
mat_frost_base  = create_studio_mat("K_FrostBase", "#41679E", roughness=0.5)
mat_frost_high  = create_studio_mat("K_FrostCrystal", "#9EC5E8", roughness=0.3, emission=0.3)
mat_frost_deep  = create_studio_mat("K_FrostDeep", "#253E6B", roughness=0.6)
mat_bandage     = create_studio_mat("K_BandageCloth", "#D4C8BC")
mat_boots_base  = create_studio_mat("K_BootsLeather", "#4A2E1B")
mat_boots_sole  = create_studio_mat("K_BootsSole", "#23160D")

objects_to_join = []

# Helper: Lofted Curved Hair & Cloth Strands
def create_sculpted_strand(name, points, radii, mat=mat_hair_mid, num_verts=5):
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    
    bm = bmesh.new()
    rings = []
    
    for i, (pt, r) in enumerate(zip(points, radii)):
        ring = []
        for v_idx in range(num_verts):
            angle = (v_idx / num_verts) * math.pi * 2
            vx = pt.x + math.cos(angle) * r
            vy = pt.y + math.sin(angle) * r
            vz = pt.z
            v = bm.verts.new((vx, vy, vz))
            ring.append(v)
        rings.append(ring)
    
    for i in range(len(rings) - 1):
        r1 = rings[i]
        r2 = rings[i+1]
        for j in range(len(r1)):
            j_next = (j + 1) % len(r1)
            bm.faces.new([r1[j], r1[j_next], r2[j_next], r2[j]])
            
    tip_v = bm.verts.new(points[-1] + Vector((0, 0, -0.02)))
    for j in range(len(rings[-1])):
        j_next = (j + 1) % len(rings[-1])
        bm.faces.new([rings[-1][j], rings[-1][j_next], tip_v])
        
    bm.to_mesh(mesh)
    bm.free()
    obj.data.materials.append(mat)
    objects_to_join.append(obj)
    return obj


# ==============================================================================
# 1. ANIME-CHIBI HEAD, SCULPTED JAW, 3D EYEPATCH & MELANCHOLIC EYE
# ==============================================================================
# Cranium & Cheeks (Sculpted organic shape, tapered chin)
bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=8, radius=0.21, location=(0, 0.01, 1.46))
head = bpy.context.active_object
head.name = "Head_Sculpted"
head.scale = (0.92, 0.88, 0.96)
head.data.materials.append(mat_skin)
objects_to_join.append(head)

# Tapered Anime Chin Apex
bpy.ops.mesh.primitive_cone_add(radius1=0.12, radius2=0.03, depth=0.14, vertices=6, location=(0, -0.07, 1.34))
chin = bpy.context.active_object
chin.name = "Chin_Sculpted"
chin.rotation_euler = (math.radians(20), 0, 0)
chin.data.materials.append(mat_skin_shadow)
objects_to_join.append(chin)

# 3D Form-Fitted Leather Eyepatch (Right Eye: +X, -Y)
bpy.ops.mesh.primitive_cylinder_add(radius=0.068, depth=0.025, vertices=6, location=(0.085, -0.18, 1.45))
ep_plate = bpy.context.active_object
ep_plate.name = "Eyepatch_3D_Plate"
ep_plate.rotation_euler = (math.radians(-14), math.radians(12), math.radians(-15))
ep_plate.scale = (1.0, 1.2, 0.8)
ep_plate.data.materials.append(mat_eyepatch)
objects_to_join.append(ep_plate)

# Eyepatch Silver Rivet Center
bpy.ops.mesh.primitive_cube_add(size=0.02, location=(0.088, -0.192, 1.45))
ep_rivet = bpy.context.active_object
ep_rivet.name = "Eyepatch_Rivet"
ep_rivet.data.materials.append(mat_buckle)
objects_to_join.append(ep_rivet)

# Eyepatch Strap Wrapping Head
bpy.ops.mesh.primitive_torus_add(major_radius=0.20, minor_radius=0.012, major_segments=14, minor_segments=4, location=(0, 0.01, 1.46))
ep_strap = bpy.context.active_object
ep_strap.name = "Eyepatch_Strap"
ep_strap.rotation_euler = (math.radians(-8), math.radians(15), 0)
ep_strap.data.materials.append(mat_eyepatch)
objects_to_join.append(ep_strap)

# 3D Expressive Left Eye (Left Eye: -X, -Y)
bpy.ops.mesh.primitive_cylinder_add(radius=0.052, depth=0.02, vertices=6, location=(-0.085, -0.18, 1.45))
eye_white = bpy.context.active_object
eye_white.name = "Eye_L_White"
eye_white.rotation_euler = (math.radians(-14), math.radians(-12), 0)
eye_white.data.materials.append(mat_eye_white)
objects_to_join.append(eye_white)

bpy.ops.mesh.primitive_cylinder_add(radius=0.032, depth=0.025, vertices=6, location=(-0.085, -0.185, 1.45))
eye_pupil = bpy.context.active_object
eye_pupil.name = "Eye_L_Pupil"
eye_pupil.rotation_euler = (math.radians(-14), math.radians(-12), 0)
eye_pupil.data.materials.append(mat_eye_pupil)
objects_to_join.append(eye_pupil)

bpy.ops.mesh.primitive_cube_add(size=0.015, location=(-0.075, -0.195, 1.465))
eye_glint = bpy.context.active_object
eye_glint.name = "Eye_L_Glint"
eye_glint.data.materials.append(mat_eye_white)
objects_to_join.append(eye_glint)


# ==============================================================================
# 2. JRPG SHAGGY ANIME HAIR (3-TIER VOLUMETRIC SCULPTED TUFTS)
# ==============================================================================
# Hair Cap Skull Base (Contoured dome)
bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=8, radius=0.23, location=(0, 0.03, 1.50))
hair_cap = bpy.context.active_object
hair_cap.name = "Hair_Cap_Base"
hair_cap.scale = (0.96, 0.98, 0.88)
hair_cap.data.materials.append(mat_hair_mid)
objects_to_join.append(hair_cap)

# Tier 1: Sweeping Forehead Fringe Bangs (Flowing Left)
create_sculpted_strand("Bang_Main_Sweep", [
    Vector((-0.02, -0.13, 1.63)),
    Vector((-0.07, -0.18, 1.56)),
    Vector((-0.13, -0.17, 1.47)),
    Vector((-0.16, -0.15, 1.38))
], [0.075, 0.065, 0.045, 0.015], mat=mat_hair_top)

create_sculpted_strand("Bang_Center_Wisp", [
    Vector((0.02, -0.13, 1.63)),
    Vector((0.01, -0.18, 1.57)),
    Vector((-0.02, -0.18, 1.48))
], [0.065, 0.05, 0.015], mat=mat_hair_mid)

create_sculpted_strand("Bang_Right_Feather", [
    Vector((0.08, -0.12, 1.61)),
    Vector((0.14, -0.16, 1.54)),
    Vector((0.17, -0.14, 1.45))
], [0.07, 0.055, 0.02], mat=mat_hair_dark)

# Tier 2: Framing Sideburn Locks
create_sculpted_strand("Hair_Sideburn_L", [
    Vector((-0.18, -0.04, 1.52)),
    Vector((-0.21, -0.07, 1.41)),
    Vector((-0.19, -0.08, 1.30))
], [0.065, 0.05, 0.015], mat=mat_hair_top)

create_sculpted_strand("Hair_Sideburn_R", [
    Vector((0.18, -0.04, 1.52)),
    Vector((0.21, -0.07, 1.41)),
    Vector((0.19, -0.08, 1.30))
], [0.065, 0.05, 0.015], mat=mat_hair_mid)

# Tier 3: Crown Spikes (Anime Cowlicks)
create_sculpted_strand("Hair_Crown_Spike_L", [
    Vector((-0.06, 0.02, 1.66)),
    Vector((-0.10, 0.04, 1.73)),
    Vector((-0.08, 0.02, 1.77))
], [0.065, 0.045, 0.01], mat=mat_hair_top)

create_sculpted_strand("Hair_Crown_Spike_R", [
    Vector((0.05, 0.02, 1.66)),
    Vector((0.09, 0.05, 1.74)),
    Vector((0.12, 0.06, 1.76))
], [0.065, 0.045, 0.01], mat=mat_hair_mid)

# Tier 4: Layered Rear Mane (Back of Head)
create_sculpted_strand("Hair_Mane_Center", [
    Vector((0.0, 0.16, 1.53)),
    Vector((0.0, 0.22, 1.41)),
    Vector((0.0, 0.20, 1.30))
], [0.11, 0.08, 0.03], mat=mat_hair_dark)

create_sculpted_strand("Hair_Mane_L", [
    Vector((-0.12, 0.14, 1.51)),
    Vector((-0.16, 0.18, 1.39)),
    Vector((-0.13, 0.17, 1.28))
], [0.085, 0.06, 0.02], mat=mat_hair_dark)

create_sculpted_strand("Hair_Mane_R", [
    Vector((0.12, 0.14, 1.51)),
    Vector((0.16, 0.18, 1.39)),
    Vector((0.13, 0.17, 1.28))
], [0.085, 0.06, 0.02], mat=mat_hair_mid)


# ==============================================================================
# 3. DRAPED SCARF OF AINA (ORGANIC ASYMMETRIC FABRIC WRAP & FLOWING TAIL)
# ==============================================================================
# Front Draped Collar Wrap (Contoured cloth resting on chest/shoulders)
bpy.ops.mesh.primitive_cylinder_add(radius=0.19, depth=0.12, vertices=12, location=(0, -0.02, 1.26))
scarf_front = bpy.context.active_object
scarf_front.name = "Scarf_Draped_Collar"
scarf_front.scale = (1.05, 0.88, 0.90)
scarf_front.rotation_euler = (math.radians(-10), math.radians(4), 0)
scarf_front.data.materials.append(mat_scarf_main)
objects_to_join.append(scarf_front)

# Left Shoulder Fold Overlap (Asymmetric bulk on left)
bpy.ops.mesh.primitive_cylinder_add(radius=0.11, depth=0.10, vertices=8, location=(-0.11, -0.04, 1.27))
scarf_fold = bpy.context.active_object
scarf_fold.name = "Scarf_Fold_L"
scarf_fold.rotation_euler = (math.radians(-16), math.radians(-20), 0)
scarf_fold.data.materials.append(mat_scarf_high)
objects_to_join.append(scarf_fold)

# Rear Flowing Scarf Tail (Cascading S-Curve down the back)
create_sculpted_strand("Scarf_Tail_Mane", [
    Vector((-0.04, 0.16, 1.23)),
    Vector((-0.07, 0.20, 1.06)),
    Vector((-0.06, 0.22, 0.86)),
    Vector((-0.09, 0.20, 0.66)),
    Vector((-0.11, 0.18, 0.48))
], [0.085, 0.075, 0.065, 0.05, 0.02], mat=mat_scarf_main)

create_sculpted_strand("Scarf_Tail_Accent", [
    Vector((0.02, 0.17, 1.19)),
    Vector((0.04, 0.19, 1.01)),
    Vector((0.02, 0.18, 0.81))
], [0.05, 0.04, 0.015], mat=mat_scarf_high)


# ==============================================================================
# 4. ATHLETIC WANDERER ROBE, V-TAPER TORSO & SILVER BUCKLE BALDRIC
# ==============================================================================
# Chest & Upper Torso (Slightly broad shoulder slope)
bpy.ops.mesh.primitive_cylinder_add(radius=0.165, depth=0.26, vertices=10, location=(0, 0.01, 1.06))
chest = bpy.context.active_object
chest.name = "Chest_Sculpted"
chest.scale = (1.05, 0.78, 1.0)
chest.data.materials.append(mat_robe_base)
objects_to_join.append(chest)

# Waist & Belt Band (Cinching inward for V-taper)
bpy.ops.mesh.primitive_cylinder_add(radius=0.15, depth=0.06, vertices=10, location=(0, 0.01, 0.88))
waist = bpy.context.active_object
waist.name = "Waist_Belt"
waist.scale = (1.02, 0.78, 1.0)
waist.data.materials.append(mat_baldric)
objects_to_join.append(waist)

# Flared 6-Panel Coat Skirt with Front Slit
bpy.ops.mesh.primitive_cone_add(radius1=0.21, radius2=0.15, depth=0.28, vertices=10, location=(0, 0.01, 0.72))
skirt = bpy.context.active_object
skirt.name = "Robe_Skirt_Flared"
skirt.scale = (1.0, 0.82, 1.0)
skirt.data.materials.append(mat_robe_base)
objects_to_join.append(skirt)

# Diagonal Baldric Leather Strap
bpy.ops.mesh.primitive_torus_add(major_radius=0.20, minor_radius=0.018, major_segments=14, minor_segments=4, location=(0, 0.01, 1.04))
baldric = bpy.context.active_object
baldric.name = "Baldric_Strap"
baldric.scale = (0.95, 0.75, 1.0)
baldric.rotation_euler = (math.radians(-10), math.radians(-42), math.radians(12))
baldric.data.materials.append(mat_baldric)
objects_to_join.append(baldric)

# Silver Square Buckle Plate on Chest
bpy.ops.mesh.primitive_cube_add(size=0.065, location=(0.04, -0.14, 1.07))
buckle = bpy.context.active_object
buckle.name = "Silver_Buckle"
buckle.rotation_euler = (math.radians(-14), math.radians(-38), 0)
buckle.scale = (1.0, 0.25, 1.0)
buckle.data.materials.append(mat_buckle)
objects_to_join.append(buckle)

# Travel Hip Pouch (Left Hip, X < 0)
bpy.ops.mesh.primitive_cube_add(size=0.09, location=(-0.18, -0.04, 0.84))
pouch = bpy.context.active_object
pouch.name = "Travel_Pouch"
pouch.rotation_euler = (0, math.radians(10), math.radians(8))
pouch.scale = (0.9, 1.2, 1.2)
pouch.data.materials.append(mat_baldric)
objects_to_join.append(pouch)


# ==============================================================================
# 5. ASYMMETRICAL ARMS WITH 18° RELAXED REST POSE
# ==============================================================================
# LEFT ARM: Cursed Frost Ice Arm (Pauldron, Elbow Spike, Knuckle Claws)
# Shoulder Ice Pauldron
bpy.ops.mesh.primitive_cone_add(radius1=0.075, depth=0.16, vertices=5, location=(-0.23, 0.01, 1.15))
ice_paul = bpy.context.active_object
ice_paul.name = "Ice_Pauldron"
ice_paul.rotation_euler = (math.radians(15), math.radians(-38), 0)
ice_paul.data.materials.append(mat_frost_high)
objects_to_join.append(ice_paul)

# Upper Arm Ice (Angled 14° outward)
bpy.ops.mesh.primitive_cylinder_add(radius=0.062, depth=0.20, vertices=7, location=(-0.24, 0.01, 1.02))
arm_l_up = bpy.context.active_object
arm_l_up.name = "Arm_L_Upper_Ice"
arm_l_up.rotation_euler = (math.radians(-8), 0, math.radians(-14))
arm_l_up.data.materials.append(mat_frost_deep)
objects_to_join.append(arm_l_up)

# Forearm Ice (Bent 18° inward/forward)
bpy.ops.mesh.primitive_cylinder_add(radius=0.068, depth=0.22, vertices=7, location=(-0.28, -0.04, 0.83))
arm_l_fore = bpy.context.active_object
arm_l_fore.name = "Arm_L_Fore_Ice"
arm_l_fore.rotation_euler = (math.radians(-18), 0, math.radians(-8))
arm_l_fore.data.materials.append(mat_frost_base)
objects_to_join.append(arm_l_fore)

# Elbow Spike
bpy.ops.mesh.primitive_cone_add(radius1=0.035, depth=0.11, vertices=4, location=(-0.31, 0.04, 0.88))
ice_spike = bpy.context.active_object
ice_spike.name = "Ice_Spike_Elbow"
ice_spike.rotation_euler = (0, math.radians(45), math.radians(45))
ice_spike.data.materials.append(mat_frost_high)
objects_to_join.append(ice_spike)

# Sculpted Ice Knuckle Fist
bpy.ops.mesh.primitive_uv_sphere_add(segments=8, ring_count=6, radius=0.06, location=(-0.30, -0.08, 0.69))
fist_l = bpy.context.active_object
fist_l.name = "Fist_L_Ice"
fist_l.scale = (0.9, 1.1, 1.2)
fist_l.data.materials.append(mat_frost_base)
objects_to_join.append(fist_l)


# RIGHT ARM: Bandaged Wanderer Arm (Deltoid Sleeve, Bandage Wraps, Glove Fist)
bpy.ops.mesh.primitive_cylinder_add(radius=0.07, depth=0.12, vertices=8, location=(0.22, 0.01, 1.12))
sleeve_r = bpy.context.active_object
sleeve_r.name = "Sleeve_R"
sleeve_r.rotation_euler = (0, 0, math.radians(14))
sleeve_r.data.materials.append(mat_robe_base)
objects_to_join.append(sleeve_r)

bpy.ops.mesh.primitive_cylinder_add(radius=0.06, depth=0.20, vertices=8, location=(0.24, 0.01, 1.02))
arm_r_up = bpy.context.active_object
arm_r_up.name = "Arm_R_Upper"
arm_r_up.rotation_euler = (math.radians(-8), 0, math.radians(14))
arm_r_up.data.materials.append(mat_robe_trim)
objects_to_join.append(arm_r_up)

bpy.ops.mesh.primitive_cylinder_add(radius=0.065, depth=0.22, vertices=8, location=(0.28, -0.04, 0.83))
arm_r_fore = bpy.context.active_object
arm_r_fore.name = "Arm_R_Fore_Bandage"
arm_r_fore.rotation_euler = (math.radians(-18), 0, math.radians(8))
arm_r_fore.data.materials.append(mat_bandage)
objects_to_join.append(arm_r_fore)

bpy.ops.mesh.primitive_uv_sphere_add(segments=8, ring_count=6, radius=0.058, location=(0.30, -0.08, 0.69))
fist_r = bpy.context.active_object
fist_r.name = "Fist_R_Hand"
fist_r.scale = (0.9, 1.1, 1.1)
fist_r.data.materials.append(mat_bandage)
objects_to_join.append(fist_r)


# ==============================================================================
# 6. HERO STANCE LEGS (SHOULDER-WIDTH APART & 8° OUTWARD TOE ANGLE)
# ==============================================================================
# Left Leg (X = -0.11)
bpy.ops.mesh.primitive_cylinder_add(radius=0.068, depth=0.24, vertices=8, location=(-0.11, 0, 0.56))
thigh_l = bpy.context.active_object
thigh_l.name = "Thigh_L"
thigh_l.rotation_euler = (0, math.radians(-3), 0)
thigh_l.data.materials.append(mat_robe_trim)
objects_to_join.append(thigh_l)

bpy.ops.mesh.primitive_cylinder_add(radius=0.078, depth=0.26, vertices=8, location=(-0.12, 0, 0.32))
boot_l_calf = bpy.context.active_object
boot_l_calf.name = "Boot_L_Calf"
boot_l_calf.rotation_euler = (0, math.radians(-3), 0)
boot_l_calf.data.materials.append(mat_boots_base)
objects_to_join.append(boot_l_calf)

bpy.ops.mesh.primitive_torus_add(major_radius=0.088, minor_radius=0.016, major_segments=10, minor_segments=4, location=(-0.12, 0, 0.42))
boot_l_cuff = bpy.context.active_object
boot_l_cuff.name = "Boot_L_Cuff"
boot_l_cuff.data.materials.append(mat_baldric)
objects_to_join.append(boot_l_cuff)

bpy.ops.mesh.primitive_cube_add(size=0.11, location=(-0.125, -0.06, 0.12))
boot_l_foot = bpy.context.active_object
boot_l_foot.name = "Boot_L_Foot"
boot_l_foot.scale = (1.0, 1.45, 0.9)
boot_l_foot.rotation_euler = (math.radians(6), 0, math.radians(8)) # 8° outward toe
boot_l_foot.data.materials.append(mat_boots_base)
objects_to_join.append(boot_l_foot)

bpy.ops.mesh.primitive_cube_add(size=0.115, location=(-0.125, -0.06, 0.04))
boot_l_sole = bpy.context.active_object
boot_l_sole.name = "Boot_L_Sole"
boot_l_sole.scale = (1.05, 1.5, 0.35)
boot_l_sole.rotation_euler = (math.radians(6), 0, math.radians(8))
boot_l_sole.data.materials.append(mat_boots_sole)
objects_to_join.append(boot_l_sole)


# Right Leg (X = +0.11)
bpy.ops.mesh.primitive_cylinder_add(radius=0.068, depth=0.24, vertices=8, location=(0.11, 0, 0.56))
thigh_r = bpy.context.active_object
thigh_r.name = "Thigh_R"
thigh_r.rotation_euler = (0, math.radians(3), 0)
thigh_r.data.materials.append(mat_robe_trim)
objects_to_join.append(thigh_r)

bpy.ops.mesh.primitive_cylinder_add(radius=0.078, depth=0.26, vertices=8, location=(0.12, 0, 0.32))
boot_r_calf = bpy.context.active_object
boot_r_calf.name = "Boot_R_Calf"
boot_r_calf.rotation_euler = (0, math.radians(3), 0)
boot_r_calf.data.materials.append(mat_boots_base)
objects_to_join.append(boot_r_calf)

bpy.ops.mesh.primitive_torus_add(major_radius=0.088, minor_radius=0.016, major_segments=10, minor_segments=4, location=(0.12, 0, 0.42))
boot_r_cuff = bpy.context.active_object
boot_r_cuff.name = "Boot_R_Cuff"
boot_r_cuff.data.materials.append(mat_baldric)
objects_to_join.append(boot_r_cuff)

bpy.ops.mesh.primitive_cube_add(size=0.11, location=(0.125, -0.06, 0.12))
boot_r_foot = bpy.context.active_object
boot_r_foot.name = "Boot_R_Foot"
boot_r_foot.scale = (1.0, 1.45, 0.9)
boot_r_foot.rotation_euler = (math.radians(6), 0, math.radians(-8)) # 8° outward toe
boot_r_foot.data.materials.append(mat_boots_base)
objects_to_join.append(boot_r_foot)

bpy.ops.mesh.primitive_cube_add(size=0.115, location=(0.125, -0.06, 0.04))
boot_r_sole = bpy.context.active_object
boot_r_sole.name = "Boot_R_Sole"
boot_r_sole.scale = (1.05, 1.5, 0.35)
boot_r_sole.rotation_euler = (math.radians(6), 0, math.radians(-8))
boot_r_sole.data.materials.append(mat_boots_sole)
objects_to_join.append(boot_r_sole)


# ==============================================================================
# 7. UNIFY MESH & EXPORT STUDIO GLTF 2.0
# ==============================================================================
bpy.ops.object.select_all(action='DESELECT')
for obj in objects_to_join:
    obj.select_set(True)
bpy.context.view_layer.objects.active = head
bpy.ops.object.join()

kaelen_master = bpy.context.active_object
kaelen_master.name = "Kaelen_V3"

for f in kaelen_master.data.polygons:
    f.use_smooth = True

bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

tri_count = sum([len(p.vertices) - 2 for p in kaelen_master.data.polygons])
print(f"KAELEN_V3_STUDIO_TRIS:{tri_count}")

export_path = "D:/GodotProjects/Lentera-Pudar/Assets/Models/Kaelen_V3.gltf"
bpy.ops.export_scene.gltf(
    filepath=export_path,
    export_format='GLTF_SEPARATE',
    export_yup=True,
    export_apply=True
)
print(f"EXPORT_SUCCESS:{export_path}")

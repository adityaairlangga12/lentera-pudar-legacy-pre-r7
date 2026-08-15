import bpy
import bmesh
import math
from mathutils import Vector, Matrix

# ==============================================================================
# LENTERA PUDAR - KAELEN V3 ORGANIC ANIME-CHIBI GENERATOR (BLENDER 5.2 LTS)
# Fully Sculpted Low-Poly Topology (Zero Minecraft Boxiness, Smooth Anime Flow)
# ==============================================================================

# 1. Clean Scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# 2. Materials Setup
def create_mat(name, hex_code, roughness=0.8, emission=0.0):
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

mat_hair_top    = create_mat("K_HairTop", "#D6D6D6")       # Highlights
mat_hair_mid    = create_mat("K_HairMid", "#9E9E9E")       # Base Gray
mat_hair_dark   = create_mat("K_HairDark", "#6E6E6E")      # Shadows
mat_skin        = create_mat("K_Skin", "#E8B282")          # Melancholic Warm Skin
mat_skin_shadow = create_mat("K_SkinShadow", "#C48A5E")
mat_eyepatch    = create_mat("K_Eyepatch", "#141013", roughness=0.95)
mat_buckle      = create_mat("K_SilverBuckle", "#D0D7DE", roughness=0.3)
mat_scarf_main  = create_mat("K_ScarfMain", "#F4B860", roughness=0.75, emission=0.2)
mat_scarf_high  = create_mat("K_ScarfHigh", "#FFD185", roughness=0.75, emission=0.3)
mat_scarf_shad  = create_mat("K_ScarfShadow", "#C78732", roughness=0.85)
mat_robe_base   = create_mat("K_RobeBase", "#241D1A")
mat_robe_trim   = create_mat("K_RobeTrim", "#191310")
mat_baldric     = create_mat("K_BaldricLeather", "#6E4023")
mat_frost_base  = create_mat("K_FrostBase", "#41679E", roughness=0.4)
mat_frost_high  = create_mat("K_FrostCrystal", "#9EC5E8", roughness=0.2, emission=0.4)
mat_frost_deep  = create_mat("K_FrostDeep", "#253E6B", roughness=0.5)
mat_bandage     = create_mat("K_BandageCloth", "#D4C8BC")
mat_boots_base  = create_mat("K_BootsLeather", "#4A2E1B")
mat_boots_sole  = create_mat("K_BootsSole", "#23160D")

objects_to_join = []

# Helper: Create tapered curved hair strand
def create_hair_strand(name, points, radii, mat=mat_hair_mid):
    # points: list of Vector positions
    # radii: list of thickness values
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    
    bm = bmesh.new()
    rings = []
    
    for i, (pt, r) in enumerate(zip(points, radii)):
        ring = []
        # 4 to 6 vertices per ring for smooth low poly
        num_verts = 5
        for v_idx in range(num_verts):
            angle = (v_idx / num_verts) * math.pi * 2
            # Create circle perpendicular to Z or segment direction
            vx = pt.x + math.cos(angle) * r
            vy = pt.y + math.sin(angle) * r
            vz = pt.z
            v = bm.verts.new((vx, vy, vz))
            ring.append(v)
        rings.append(ring)
    
    # Bridge rings
    for i in range(len(rings) - 1):
        r1 = rings[i]
        r2 = rings[i+1]
        for j in range(len(r1)):
            j_next = (j + 1) % len(r1)
            bm.faces.new([r1[j], r1[j_next], r2[j_next], r2[j]])
            
    # Cap tip
    tip_v = bm.verts.new(points[-1] + Vector((0, 0, -0.04)))
    for j in range(len(rings[-1])):
        j_next = (j + 1) % len(rings[-1])
        bm.faces.new([rings[-1][j], rings[-1][j_next], tip_v])
        
    bm.to_mesh(mesh)
    bm.free()
    obj.data.materials.append(mat)
    objects_to_join.append(obj)
    return obj


# ==============================================================================
# A. SCULPTED CHIBI HEAD & FACIAL FEATURES (ROUNDED / ANIME JAW)
# ==============================================================================
# Head Base: Subdivided rounded sphere
bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=8, radius=0.22, location=(0, 0, 1.46))
head = bpy.context.active_object
head.name = "Head_Organic"
head.scale = (0.92, 0.90, 0.95)
head.data.materials.append(mat_skin)
objects_to_join.append(head)

# Chin taper
bpy.ops.mesh.primitive_cone_add(radius1=0.14, radius2=0.04, depth=0.14, vertices=6, location=(0, -0.06, 1.34))
chin = bpy.context.active_object
chin.name = "Chin_Organic"
chin.rotation_euler = (math.radians(18), 0, 0)
chin.data.materials.append(mat_skin_shadow)
objects_to_join.append(chin)

# Eyepatch over RIGHT eye (Contoured diamond plate on -Y, X > 0)
bpy.ops.mesh.primitive_cylinder_add(radius=0.07, depth=0.02, vertices=6, location=(0.09, -0.195, 1.46))
ep_plate = bpy.context.active_object
ep_plate.name = "Eyepatch_Plate"
ep_plate.rotation_euler = (math.radians(-15), math.radians(10), math.radians(-15))
ep_plate.data.materials.append(mat_eyepatch)
objects_to_join.append(ep_plate)

# Eyepatch strap wrapping head
bpy.ops.mesh.primitive_torus_add(major_radius=0.205, minor_radius=0.012, major_segments=12, minor_segments=4, location=(0, 0, 1.46))
ep_strap = bpy.context.active_object
ep_strap.name = "Eyepatch_Strap"
ep_strap.rotation_euler = (math.radians(-10), math.radians(14), 0)
ep_strap.data.materials.append(mat_eyepatch)
objects_to_join.append(ep_strap)

# Left Eye (Open Melancholic Chibi Eye on -Y, X < 0)
bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.015, vertices=6, location=(-0.09, -0.195, 1.46))
eye_l = bpy.context.active_object
eye_l.name = "Eye_L_White"
eye_l.rotation_euler = (math.radians(-15), math.radians(-10), 0)
eye_l.data.materials.append(mat_hair_top)
objects_to_join.append(eye_l)

bpy.ops.mesh.primitive_cylinder_add(radius=0.028, depth=0.02, vertices=6, location=(-0.09, -0.20, 1.46))
pupil_l = bpy.context.active_object
pupil_l.name = "Eye_L_Pupil"
pupil_l.rotation_euler = (math.radians(-15), math.radians(-10), 0)
pupil_l.data.materials.append(mat_eyepatch)
objects_to_join.append(pupil_l)


# ==============================================================================
# B. ANIME HAIR LOCKS (DYNAMIC FLOWING HAIR STRANDS - ZERO BLOCKINESS)
# ==============================================================================
# Hair Cap / Volume Base
bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=8, radius=0.24, location=(0, 0.03, 1.50))
hair_cap = bpy.context.active_object
hair_cap.name = "Hair_Cap"
hair_cap.scale = (0.96, 0.98, 0.85)
hair_cap.data.materials.append(mat_hair_mid)
objects_to_join.append(hair_cap)

# Strand 1: Main Sweeping Bang (Left Forehead - Highlighted)
create_hair_strand("Bang_Left_Main", [
    Vector((-0.02, -0.14, 1.62)),
    Vector((-0.08, -0.18, 1.54)),
    Vector((-0.14, -0.17, 1.44))
], [0.07, 0.055, 0.02], mat=mat_hair_top)

# Strand 2: Center Feather Bang
create_hair_strand("Bang_Center_Wisp", [
    Vector((0.02, -0.14, 1.62)),
    Vector((0.01, -0.19, 1.53)),
    Vector((-0.02, -0.18, 1.43))
], [0.06, 0.045, 0.015], mat=mat_hair_mid)

# Strand 3: Right Bang (Over Eyepatch Strap)
create_hair_strand("Bang_Right_Side", [
    Vector((0.08, -0.12, 1.60)),
    Vector((0.14, -0.16, 1.52)),
    Vector((0.17, -0.13, 1.42))
], [0.065, 0.05, 0.02], mat=mat_hair_dark)

# Strand 4: Left Sideburn Lock
create_hair_strand("Hair_Sideburn_L", [
    Vector((-0.18, -0.05, 1.52)),
    Vector((-0.21, -0.08, 1.40)),
    Vector((-0.19, -0.09, 1.30))
], [0.06, 0.045, 0.015], mat=mat_hair_top)

# Strand 5: Right Sideburn Lock
create_hair_strand("Hair_Sideburn_R", [
    Vector((0.18, -0.05, 1.52)),
    Vector((0.21, -0.08, 1.40)),
    Vector((0.19, -0.09, 1.30))
], [0.06, 0.045, 0.015], mat=mat_hair_mid)

# Strand 6 & 7: Top Spikes (Anime Cowlick / Crown Spikes)
create_hair_strand("Hair_Crown_L", [
    Vector((-0.06, 0.02, 1.65)),
    Vector((-0.10, 0.04, 1.72)),
    Vector((-0.08, 0.02, 1.76))
], [0.06, 0.04, 0.01], mat=mat_hair_top)

create_hair_strand("Hair_Crown_R", [
    Vector((0.05, 0.02, 1.65)),
    Vector((0.09, 0.05, 1.73)),
    Vector((0.12, 0.06, 1.75))
], [0.06, 0.04, 0.01], mat=mat_hair_mid)

# Strand 8, 9, 10: Back Neck Layers (Draping over back head)
create_hair_strand("Hair_Back_01", [
    Vector((0.0, 0.16, 1.52)),
    Vector((0.0, 0.22, 1.40)),
    Vector((0.0, 0.20, 1.30))
], [0.10, 0.07, 0.03], mat=mat_hair_dark)

create_hair_strand("Hair_Back_02", [
    Vector((-0.12, 0.14, 1.50)),
    Vector((-0.15, 0.18, 1.38)),
    Vector((-0.13, 0.17, 1.28))
], [0.08, 0.055, 0.02], mat=mat_hair_dark)

create_hair_strand("Hair_Back_03", [
    Vector((0.12, 0.14, 1.50)),
    Vector((0.15, 0.18, 1.38)),
    Vector((0.13, 0.17, 1.28))
], [0.08, 0.055, 0.02], mat=mat_hair_mid)


# ==============================================================================
# C. ORGANIC SCARF OF AINA (#F4B860 - COZY WRAPPED COLLAR & FLOWING BACK TAIL)
# ==============================================================================
# Scarf Wrapped Collar (Contoured organic toroid)
bpy.ops.mesh.primitive_torus_add(major_radius=0.22, minor_radius=0.075, major_segments=14, minor_segments=8, location=(0, -0.01, 1.25))
scarf_wrap_1 = bpy.context.active_object
scarf_wrap_1.name = "Scarf_Wrap_Main"
scarf_wrap_1.scale = (1.05, 0.95, 0.90)
scarf_wrap_1.rotation_euler = (math.radians(-8), math.radians(4), 0)
scarf_wrap_1.data.materials.append(mat_scarf_main)
objects_to_join.append(scarf_wrap_1)

# Scarf Fold Accent (Overlapping front tuck on -Y)
bpy.ops.mesh.primitive_torus_add(major_radius=0.18, minor_radius=0.05, major_segments=10, minor_segments=6, location=(-0.04, -0.10, 1.27))
scarf_wrap_2 = bpy.context.active_object
scarf_wrap_2.name = "Scarf_Wrap_Fold"
scarf_wrap_2.rotation_euler = (math.radians(-15), math.radians(-12), 0)
scarf_wrap_2.data.materials.append(mat_scarf_high)
objects_to_join.append(scarf_wrap_2)

# Flowing Scarf Tail on the BACK (+Y) with Curved Ribbon Geometry
create_hair_strand("Scarf_Tail_Organic", [
    Vector((-0.04, 0.18, 1.22)),
    Vector((-0.07, 0.22, 1.05)),
    Vector((-0.06, 0.24, 0.85)),
    Vector((-0.09, 0.22, 0.65)),
    Vector((-0.11, 0.19, 0.48))
], [0.09, 0.08, 0.07, 0.055, 0.02], mat=mat_scarf_main)

# Accent Scarf Ribbon Tail (Secondary split end)
create_hair_strand("Scarf_Tail_Split", [
    Vector((0.02, 0.19, 1.18)),
    Vector((0.04, 0.21, 1.00)),
    Vector((0.02, 0.20, 0.80))
], [0.05, 0.04, 0.015], mat=mat_scarf_high)


# ==============================================================================
# D. TORSO, ATHLETIC ROBE, BALDRIC HARNESS & TRAVEL POUCH
# ==============================================================================
# Torso Body: Tapered rounded chest to waist
bpy.ops.mesh.primitive_cylinder_add(radius=0.17, depth=0.34, vertices=10, location=(0, 0, 1.00))
torso = bpy.context.active_object
torso.name = "Torso_Organic"
torso.scale = (1.0, 0.78, 1.0)
torso.data.materials.append(mat_robe_base)
objects_to_join.append(torso)

# Waist & Belt Band
bpy.ops.mesh.primitive_cylinder_add(radius=0.165, depth=0.06, vertices=10, location=(0, 0, 0.82))
belt = bpy.context.active_object
belt.name = "Belt_Organic"
belt.scale = (1.02, 0.80, 1.0)
belt.data.materials.append(mat_baldric)
objects_to_join.append(belt)

# Flared Robe Coat / Tunic Skirt (Gentle outward cone flare with front split)
bpy.ops.mesh.primitive_cone_add(radius1=0.22, radius2=0.16, depth=0.30, vertices=10, location=(0, 0, 0.68))
skirt = bpy.context.active_object
skirt.name = "Robe_Skirt_Organic"
skirt.scale = (1.0, 0.82, 1.0)
skirt.data.materials.append(mat_robe_base)
objects_to_join.append(skirt)

# Baldric Strap: Smooth curved belt wrapping chest from Right Shoulder to Left Hip
bpy.ops.mesh.primitive_torus_add(major_radius=0.22, minor_radius=0.02, major_segments=14, minor_segments=4, location=(0, 0, 1.02))
baldric = bpy.context.active_object
baldric.name = "Baldric_Strap_Organic"
baldric.scale = (0.95, 0.75, 1.0)
baldric.rotation_euler = (math.radians(-10), math.radians(-42), math.radians(12))
baldric.data.materials.append(mat_baldric)
objects_to_join.append(baldric)

# Silver Square Buckle on Chest
bpy.ops.mesh.primitive_cube_add(size=0.07, location=(0.04, -0.15, 1.05))
buckle = bpy.context.active_object
buckle.name = "Buckle_Silver"
buckle.rotation_euler = (math.radians(-14), math.radians(-38), 0)
buckle.scale = (1.0, 0.2, 1.0)
buckle.data.materials.append(mat_buckle)
objects_to_join.append(buckle)

# Travel Pouch (Left Hip, X < 0)
bpy.ops.mesh.primitive_cube_add(size=0.10, location=(-0.19, -0.06, 0.78))
pouch = bpy.context.active_object
pouch.name = "Pouch_Organic"
pouch.rotation_euler = (0, math.radians(10), math.radians(8))
pouch.scale = (0.9, 1.2, 1.2)
pouch.data.materials.append(mat_baldric)
objects_to_join.append(pouch)


# ==============================================================================
# E. LEFT ARM: ASYMMETRICAL CURSED FROST CRYSTAL ARM (#41679E / #9EC5E8)
# ==============================================================================
# Cursed Shoulder Pauldron (Curved crystalline ice cluster)
bpy.ops.mesh.primitive_cone_add(radius1=0.08, depth=0.18, vertices=5, location=(-0.24, 0, 1.15))
ice_paul = bpy.context.active_object
ice_paul.name = "Ice_Pauldron"
ice_paul.rotation_euler = (math.radians(15), math.radians(-40), 0)
ice_paul.data.materials.append(mat_frost_high)
objects_to_join.append(ice_paul)

# Ice Upper Arm (Contoured tapered bicep)
bpy.ops.mesh.primitive_cylinder_add(radius=0.068, depth=0.22, vertices=7, location=(-0.24, 0, 1.00))
arm_l_up = bpy.context.active_object
arm_l_up.name = "Arm_L_Upper_Ice"
arm_l_up.rotation_euler = (0, 0, math.radians(-14))
arm_l_up.data.materials.append(mat_frost_deep)
objects_to_join.append(arm_l_up)

# Ice Forearm (Tapered faceted crystal forearm)
bpy.ops.mesh.primitive_cylinder_add(radius=0.075, depth=0.24, vertices=7, location=(-0.29, -0.02, 0.79))
arm_l_fore = bpy.context.active_object
arm_l_fore.name = "Arm_L_Fore_Ice"
arm_l_fore.rotation_euler = (0, 0, math.radians(-8))
arm_l_fore.data.materials.append(mat_frost_base)
objects_to_join.append(arm_l_fore)

# Pointed Ice Crystals (Elbow & Forearm spikes)
bpy.ops.mesh.primitive_cone_add(radius1=0.04, depth=0.12, vertices=4, location=(-0.34, 0.03, 0.83))
ice_spike_1 = bpy.context.active_object
ice_spike_1.name = "Ice_Spike_Elbow"
ice_spike_1.rotation_euler = (0, math.radians(40), math.radians(45))
ice_spike_1.data.materials.append(mat_frost_high)
objects_to_join.append(ice_spike_1)

bpy.ops.mesh.primitive_cone_add(radius1=0.035, depth=0.10, vertices=4, location=(-0.34, -0.05, 0.72))
ice_spike_2 = bpy.context.active_object
ice_spike_2.name = "Ice_Spike_Wrist"
ice_spike_2.rotation_euler = (math.radians(-20), math.radians(-45), 0)
ice_spike_2.data.materials.append(mat_frost_high)
objects_to_join.append(ice_spike_2)

# Cursed Ice Fist (Faceted crystal hand)
bpy.ops.mesh.primitive_uv_sphere_add(segments=8, ring_count=6, radius=0.065, location=(-0.32, -0.03, 0.63))
fist_l = bpy.context.active_object
fist_l.name = "Fist_L_Ice"
fist_l.scale = (0.9, 1.1, 1.2)
fist_l.data.materials.append(mat_frost_base)
objects_to_join.append(fist_l)


# ==============================================================================
# F. RIGHT ARM: NORMAL WANDERER ARM WITH WRAPPED BANDAGES (#D4C8BC)
# ==============================================================================
# Right Shoulder Sleeve
bpy.ops.mesh.primitive_cylinder_add(radius=0.075, depth=0.14, vertices=8, location=(0.23, 0, 1.10))
sleeve_r = bpy.context.active_object
sleeve_r.name = "Sleeve_R"
sleeve_r.rotation_euler = (0, 0, math.radians(14))
sleeve_r.data.materials.append(mat_robe_base)
objects_to_join.append(sleeve_r)

# Right Upper Arm
bpy.ops.mesh.primitive_cylinder_add(radius=0.065, depth=0.20, vertices=8, location=(0.25, 0, 0.99))
arm_r_up = bpy.context.active_object
arm_r_up.name = "Arm_R_Upper"
arm_r_up.rotation_euler = (0, 0, math.radians(12))
arm_r_up.data.materials.append(mat_robe_trim)
objects_to_join.append(arm_r_up)

# Right Forearm with Bandages (Tapered cylinder with bandage coils)
bpy.ops.mesh.primitive_cylinder_add(radius=0.07, depth=0.24, vertices=8, location=(0.29, -0.02, 0.79))
arm_r_fore = bpy.context.active_object
arm_r_fore.name = "Arm_R_Fore_Bandages"
arm_r_fore.rotation_euler = (0, 0, math.radians(8))
arm_r_fore.data.materials.append(mat_bandage)
objects_to_join.append(arm_r_fore)

# Right Hand (Wrapped Fist)
bpy.ops.mesh.primitive_uv_sphere_add(segments=8, ring_count=6, radius=0.06, location=(0.31, -0.03, 0.63))
fist_r = bpy.context.active_object
fist_r.name = "Fist_R_Hand"
fist_r.scale = (0.9, 1.1, 1.1)
fist_r.data.materials.append(mat_bandage)
objects_to_join.append(fist_r)


# ==============================================================================
# G. LEGS & CURVED TRAVEL BOOTS (#4A2E1B / #23160D)
# ==============================================================================
# Left Thigh
bpy.ops.mesh.primitive_cylinder_add(radius=0.075, depth=0.24, vertices=8, location=(-0.10, 0, 0.52))
thigh_l = bpy.context.active_object
thigh_l.name = "Thigh_L"
thigh_l.data.materials.append(mat_robe_trim)
objects_to_join.append(thigh_l)

# Left Boot: Calf & Flared Cuff
bpy.ops.mesh.primitive_cylinder_add(radius=0.085, depth=0.26, vertices=8, location=(-0.10, 0, 0.30))
boot_l_calf = bpy.context.active_object
boot_l_calf.name = "Boot_L_Calf"
boot_l_calf.data.materials.append(mat_boots_base)
objects_to_join.append(boot_l_calf)

bpy.ops.mesh.primitive_torus_add(major_radius=0.095, minor_radius=0.02, major_segments=10, minor_segments=4, location=(-0.10, 0, 0.40))
boot_l_cuff = bpy.context.active_object
boot_l_cuff.name = "Boot_L_Cuff"
boot_l_cuff.data.materials.append(mat_baldric)
objects_to_join.append(boot_l_cuff)

# Left Boot Foot: Rounded toe & sole
bpy.ops.mesh.primitive_cube_add(size=0.12, location=(-0.10, -0.06, 0.12))
boot_l_foot = bpy.context.active_object
boot_l_foot.name = "Boot_L_Foot"
boot_l_foot.scale = (1.0, 1.5, 0.9)
boot_l_foot.rotation_euler = (math.radians(6), 0, 0)
boot_l_foot.data.materials.append(mat_boots_base)
objects_to_join.append(boot_l_foot)

bpy.ops.mesh.primitive_cube_add(size=0.125, location=(-0.10, -0.06, 0.04))
boot_l_sole = bpy.context.active_object
boot_l_sole.name = "Boot_L_Sole"
boot_l_sole.scale = (1.05, 1.55, 0.35)
boot_l_sole.rotation_euler = (math.radians(6), 0, 0)
boot_l_sole.data.materials.append(mat_boots_sole)
objects_to_join.append(boot_l_sole)

# Right Thigh
bpy.ops.mesh.primitive_cylinder_add(radius=0.075, depth=0.24, vertices=8, location=(0.10, 0, 0.52))
thigh_r = bpy.context.active_object
thigh_r.name = "Thigh_R"
thigh_r.data.materials.append(mat_robe_trim)
objects_to_join.append(thigh_r)

# Right Boot: Calf & Flared Cuff
bpy.ops.mesh.primitive_cylinder_add(radius=0.085, depth=0.26, vertices=8, location=(0.10, 0, 0.30))
boot_r_calf = bpy.context.active_object
boot_r_calf.name = "Boot_R_Calf"
boot_r_calf.data.materials.append(mat_boots_base)
objects_to_join.append(boot_r_calf)

bpy.ops.mesh.primitive_torus_add(major_radius=0.095, minor_radius=0.02, major_segments=10, minor_segments=4, location=(0.10, 0, 0.40))
boot_r_cuff = bpy.context.active_object
boot_r_cuff.name = "Boot_R_Cuff"
boot_r_cuff.data.materials.append(mat_baldric)
objects_to_join.append(boot_r_cuff)

# Right Boot Foot: Rounded toe & sole
bpy.ops.mesh.primitive_cube_add(size=0.12, location=(0.10, -0.06, 0.12))
boot_r_foot = bpy.context.active_object
boot_r_foot.name = "Boot_R_Foot"
boot_r_foot.scale = (1.0, 1.5, 0.9)
boot_r_foot.rotation_euler = (math.radians(6), 0, 0)
boot_r_foot.data.materials.append(mat_boots_base)
objects_to_join.append(boot_r_foot)

bpy.ops.mesh.primitive_cube_add(size=0.125, location=(0.10, -0.06, 0.04))
boot_r_sole = bpy.context.active_object
boot_r_sole.name = "Boot_R_Sole"
boot_r_sole.scale = (1.05, 1.55, 0.35)
boot_r_sole.rotation_euler = (math.radians(6), 0, 0)
boot_r_sole.data.materials.append(mat_boots_sole)
objects_to_join.append(boot_r_sole)


# ==============================================================================
# H. UNIFY MESH & EXPORT GLTF 2.0
# ==============================================================================
bpy.ops.object.select_all(action='DESELECT')
for obj in objects_to_join:
    obj.select_set(True)
bpy.context.view_layer.objects.active = head
bpy.ops.object.join()

kaelen_organic = bpy.context.active_object
kaelen_organic.name = "Kaelen_V3"

# Smooth Shading with Weighted Normal Angle (Zero harsh blockiness, smooth organic facets)
for f in kaelen_organic.data.polygons:
    f.use_smooth = True

# Apply all transforms
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

# Calculate Triangles
tri_count = sum([len(p.vertices) - 2 for p in kaelen_organic.data.polygons])
print(f"KAELEN_V3_ORGANIC_TRIS:{tri_count}")

# Export glTF 2.0 (+Z forward, Y up)
export_path = "D:/GodotProjects/Lentera-Pudar/Assets/Models/Kaelen_V3.gltf"
bpy.ops.export_scene.gltf(
    filepath=export_path,
    export_format='GLTF_SEPARATE',
    export_yup=True,
    export_apply=True
)
print(f"EXPORT_SUCCESS:{export_path}")

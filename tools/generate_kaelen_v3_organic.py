import bpy
import bmesh
import math
import os
from mathutils import Vector, Matrix

# ==============================================================================
# LENTERA PUDAR - KAELEN V3 CLEAN 3D-TO-PIXEL GENERATOR (DEAD CELLS STANDARD)
# Organic Low-Poly Topology + 32x32 Pixel Face Texture UV Mapping (Clean Visibility)
# ==============================================================================

# 1. Clean Scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# 2. Materials Setup
def create_color_mat(name, hex_code, roughness=1.0, emission=0.0):
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

def create_texture_mat(name, texture_path):
    mat = bpy.data.materials.get(name)
    if not mat:
        mat = bpy.data.materials.new(name=name)
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        nodes.clear()
        
        node_output = nodes.new(type='ShaderNodeOutputMaterial')
        node_bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
        node_tex = nodes.new(type='ShaderNodeTexImage')
        
        if os.path.exists(texture_path):
            img = bpy.data.images.load(texture_path)
            img.colorspace_settings.name = 'sRGB'
            node_tex.image = img
            node_tex.interpolation = 'Closest' # Nearest filtering
            
        node_bsdf.inputs['Roughness'].default_value = 1.0
        if 'Specular IOR Level' in node_bsdf.inputs:
            node_bsdf.inputs['Specular IOR Level'].default_value = 0.0
        elif 'Specular' in node_bsdf.inputs:
            node_bsdf.inputs['Specular'].default_value = 0.0
            
        mat.node_tree.links.new(node_tex.outputs['Color'], node_bsdf.inputs['Base Color'])
        mat.node_tree.links.new(node_bsdf.outputs['BSDF'], node_output.inputs['Surface'])
    return mat

tex_face_path   = "D:/GodotProjects/Lentera-Pudar/Assets/Models/kaelen_face_32x32.png"
mat_face        = create_texture_mat("K_FaceTexture", tex_face_path)
mat_hair_top    = create_color_mat("K_HairTop", "#D6D6D6")       # Highlights
mat_hair_mid    = create_color_mat("K_HairMid", "#9E9E9E")       # Base Gray
mat_hair_dark   = create_color_mat("K_HairDark", "#6E6E6E")      # Shadows
mat_skin        = create_color_mat("K_Skin", "#E8B282")          # Melancholic Warm Skin
mat_skin_shadow = create_color_mat("K_SkinShadow", "#C48A5E")
mat_buckle      = create_color_mat("K_SilverBuckle", "#D0D7DE", roughness=0.3)
mat_scarf_main  = create_color_mat("K_ScarfMain", "#F4B860", roughness=0.9, emission=0.15)
mat_scarf_high  = create_color_mat("K_ScarfHigh", "#FFD185", roughness=0.9, emission=0.25)
mat_scarf_shad  = create_color_mat("K_ScarfShadow", "#C78732", roughness=0.95)
mat_robe_base   = create_color_mat("K_RobeBase", "#241D1A")
mat_robe_trim   = create_color_mat("K_RobeTrim", "#191310")
mat_baldric     = create_color_mat("K_BaldricLeather", "#6E4023")
mat_frost_base  = create_color_mat("K_FrostBase", "#41679E", roughness=0.5)
mat_frost_high  = create_color_mat("K_FrostCrystal", "#9EC5E8", roughness=0.3, emission=0.3)
mat_frost_deep  = create_color_mat("K_FrostDeep", "#253E6B", roughness=0.6)
mat_bandage     = create_color_mat("K_BandageCloth", "#D4C8BC")
mat_boots_base  = create_color_mat("K_BootsLeather", "#4A2E1B")
mat_boots_sole  = create_color_mat("K_BootsSole", "#23160D")

objects_to_join = []

# Helper: Create tapered curved hair strand
def create_hair_strand(name, points, radii, mat=mat_hair_mid):
    mesh = bpy.data.meshes.new(name)
    obj = bpy.data.objects.new(name, mesh)
    bpy.context.collection.objects.link(obj)
    
    bm = bmesh.new()
    rings = []
    
    for i, (pt, r) in enumerate(zip(points, radii)):
        ring = []
        num_verts = 5
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
# A. CHIBI HEAD WITH CLEAN UV-MAPPED PIXEL FACE (32x32 PNG)
# ==============================================================================
# Head Base Sphere
bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=8, radius=0.21, location=(0, 0, 1.46))
head = bpy.context.active_object
head.name = "Head_Base"
head.scale = (0.92, 0.88, 0.95)
head.data.materials.append(mat_skin)
objects_to_join.append(head)

# Front Face Plane with UV Mapping directly to kaelen_face_32x32.png
mesh_face = bpy.data.meshes.new("Face_Plane_UV")
obj_face = bpy.data.objects.new("Face_Plane_UV", mesh_face)
bpy.context.collection.objects.link(obj_face)

bm_f = bmesh.new()
w_f = 0.22
h_f = 0.20
y_offset = -0.195
z_base = 1.45

verts_grid = []
for r in range(4):
    row = []
    v_norm = r / 3.0
    vz = z_base + (0.5 - v_norm) * h_f
    for c in range(4):
        u_norm = c / 3.0
        # In 3D: X > 0 is Character's Right (+X). Eyepatch is on +X.
        vx = (0.5 - u_norm) * w_f
        vy = y_offset + (abs(vx) ** 2) * 0.40
        v = bm_f.verts.new((vx, vy, vz))
        row.append(v)
    verts_grid.append(row)

uv_layer = bm_f.loops.layers.uv.new("UVMap")
for r in range(3):
    for c in range(3):
        v1 = verts_grid[r][c]
        v2 = verts_grid[r][c+1]
        v3 = verts_grid[r+1][c+1]
        v4 = verts_grid[r+1][c]
        face = bm_f.faces.new([v1, v2, v3, v4])
        
        u0 = c / 3.0
        u1 = (c + 1) / 3.0
        v_top = 1.0 - (r / 3.0)
        v_bot = 1.0 - ((r + 1) / 3.0)
        
        for loop in face.loops:
            if loop.vert == v1:
                loop[uv_layer].uv = Vector((u0, v_top))
            elif loop.vert == v2:
                loop[uv_layer].uv = Vector((u1, v_top))
            elif loop.vert == v3:
                loop[uv_layer].uv = Vector((u1, v_bot))
            elif loop.vert == v4:
                loop[uv_layer].uv = Vector((u0, v_bot))

bm_f.to_mesh(mesh_face)
bm_f.free()
obj_face.data.materials.append(mat_face)
objects_to_join.append(obj_face)


# ==============================================================================
# B. ANIME HAIR LOCKS (FRAMING FOREHEAD BEAUTIFULLY)
# ==============================================================================
# Hair Cap Base
bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=8, radius=0.235, location=(0, 0.03, 1.50))
hair_cap = bpy.context.active_object
hair_cap.name = "Hair_Cap"
hair_cap.scale = (0.96, 0.98, 0.85)
hair_cap.data.materials.append(mat_hair_mid)
objects_to_join.append(hair_cap)

# Strand 1: Main Sweeping Bang (Left Forehead - Highlighted)
create_hair_strand("Bang_Left_Main", [
    Vector((-0.03, -0.13, 1.63)),
    Vector((-0.09, -0.16, 1.56)),
    Vector((-0.15, -0.14, 1.48))
], [0.065, 0.05, 0.015], mat=mat_hair_top)

# Strand 2: Center Feather Bang
create_hair_strand("Bang_Center_Wisp", [
    Vector((0.02, -0.13, 1.63)),
    Vector((0.01, -0.16, 1.57)),
    Vector((-0.03, -0.15, 1.50))
], [0.055, 0.04, 0.012], mat=mat_hair_mid)

# Strand 3: Right Bang (Over Forehead)
create_hair_strand("Bang_Right_Side", [
    Vector((0.08, -0.11, 1.61)),
    Vector((0.14, -0.14, 1.55)),
    Vector((0.16, -0.11, 1.46))
], [0.06, 0.045, 0.015], mat=mat_hair_dark)

# Strand 4: Left Sideburn Lock
create_hair_strand("Hair_Sideburn_L", [
    Vector((-0.18, -0.04, 1.52)),
    Vector((-0.21, -0.07, 1.40)),
    Vector((-0.19, -0.08, 1.30))
], [0.06, 0.045, 0.015], mat=mat_hair_top)

# Strand 5: Right Sideburn Lock
create_hair_strand("Hair_Sideburn_R", [
    Vector((0.18, -0.04, 1.52)),
    Vector((0.21, -0.07, 1.40)),
    Vector((0.19, -0.08, 1.30))
], [0.06, 0.045, 0.015], mat=mat_hair_mid)

# Strand 6 & 7: Top Spikes (Anime Cowlicks)
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

# Strand 8, 9, 10: Back Neck Layers
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
# C. ORGANIC SCARF OF AINA (#F4B860 2700K - COZY WRAP & FLOWING TAIL)
# ==============================================================================
bpy.ops.mesh.primitive_torus_add(major_radius=0.22, minor_radius=0.075, major_segments=14, minor_segments=8, location=(0, -0.01, 1.25))
scarf_wrap_1 = bpy.context.active_object
scarf_wrap_1.name = "Scarf_Wrap_Main"
scarf_wrap_1.scale = (1.05, 0.95, 0.90)
scarf_wrap_1.rotation_euler = (math.radians(-8), math.radians(4), 0)
scarf_wrap_1.data.materials.append(mat_scarf_main)
objects_to_join.append(scarf_wrap_1)

bpy.ops.mesh.primitive_torus_add(major_radius=0.18, minor_radius=0.05, major_segments=10, minor_segments=6, location=(-0.04, -0.10, 1.27))
scarf_wrap_2 = bpy.context.active_object
scarf_wrap_2.name = "Scarf_Wrap_Fold"
scarf_wrap_2.rotation_euler = (math.radians(-15), math.radians(-12), 0)
scarf_wrap_2.data.materials.append(mat_scarf_high)
objects_to_join.append(scarf_wrap_2)

# Scarf Tail on Back (+Y)
create_hair_strand("Scarf_Tail_Organic", [
    Vector((-0.04, 0.18, 1.22)),
    Vector((-0.07, 0.22, 1.05)),
    Vector((-0.06, 0.24, 0.85)),
    Vector((-0.09, 0.22, 0.65)),
    Vector((-0.11, 0.19, 0.48))
], [0.09, 0.08, 0.07, 0.055, 0.02], mat=mat_scarf_main)

create_hair_strand("Scarf_Tail_Split", [
    Vector((0.02, 0.19, 1.18)),
    Vector((0.04, 0.21, 1.00)),
    Vector((0.02, 0.20, 0.80))
], [0.05, 0.04, 0.015], mat=mat_scarf_high)


# ==============================================================================
# D. TORSO, ROBE, BALDRIC & SILVER BUCKLE
# ==============================================================================
bpy.ops.mesh.primitive_cylinder_add(radius=0.17, depth=0.34, vertices=10, location=(0, 0, 1.00))
torso = bpy.context.active_object
torso.name = "Torso_Organic"
torso.scale = (1.0, 0.78, 1.0)
torso.data.materials.append(mat_robe_base)
objects_to_join.append(torso)

bpy.ops.mesh.primitive_cylinder_add(radius=0.165, depth=0.06, vertices=10, location=(0, 0, 0.82))
belt = bpy.context.active_object
belt.name = "Belt_Organic"
belt.scale = (1.02, 0.80, 1.0)
belt.data.materials.append(mat_baldric)
objects_to_join.append(belt)

bpy.ops.mesh.primitive_cone_add(radius1=0.22, radius2=0.16, depth=0.30, vertices=10, location=(0, 0, 0.68))
skirt = bpy.context.active_object
skirt.name = "Robe_Skirt_Organic"
skirt.scale = (1.0, 0.82, 1.0)
skirt.data.materials.append(mat_robe_base)
objects_to_join.append(skirt)

bpy.ops.mesh.primitive_torus_add(major_radius=0.22, minor_radius=0.02, major_segments=14, minor_segments=4, location=(0, 0, 1.02))
baldric = bpy.context.active_object
baldric.name = "Baldric_Strap_Organic"
baldric.scale = (0.95, 0.75, 1.0)
baldric.rotation_euler = (math.radians(-10), math.radians(-42), math.radians(12))
baldric.data.materials.append(mat_baldric)
objects_to_join.append(baldric)

bpy.ops.mesh.primitive_cube_add(size=0.07, location=(0.04, -0.15, 1.05))
buckle = bpy.context.active_object
buckle.name = "Buckle_Silver"
buckle.rotation_euler = (math.radians(-14), math.radians(-38), 0)
buckle.scale = (1.0, 0.2, 1.0)
buckle.data.materials.append(mat_buckle)
objects_to_join.append(buckle)

bpy.ops.mesh.primitive_cube_add(size=0.10, location=(-0.19, -0.06, 0.78))
pouch = bpy.context.active_object
pouch.name = "Pouch_Organic"
pouch.rotation_euler = (0, math.radians(10), math.radians(8))
pouch.scale = (0.9, 1.2, 1.2)
pouch.data.materials.append(mat_baldric)
objects_to_join.append(pouch)


# ==============================================================================
# E. LEFT CURSED FROST ARM (#41679E / #9EC5E8)
# ==============================================================================
bpy.ops.mesh.primitive_cone_add(radius1=0.08, depth=0.18, vertices=5, location=(-0.24, 0, 1.15))
ice_paul = bpy.context.active_object
ice_paul.name = "Ice_Pauldron"
ice_paul.rotation_euler = (math.radians(15), math.radians(-40), 0)
ice_paul.data.materials.append(mat_frost_high)
objects_to_join.append(ice_paul)

bpy.ops.mesh.primitive_cylinder_add(radius=0.068, depth=0.22, vertices=7, location=(-0.24, 0, 1.00))
arm_l_up = bpy.context.active_object
arm_l_up.name = "Arm_L_Upper_Ice"
arm_l_up.rotation_euler = (0, 0, math.radians(-14))
arm_l_up.data.materials.append(mat_frost_deep)
objects_to_join.append(arm_l_up)

bpy.ops.mesh.primitive_cylinder_add(radius=0.075, depth=0.24, vertices=7, location=(-0.29, -0.02, 0.79))
arm_l_fore = bpy.context.active_object
arm_l_fore.name = "Arm_L_Fore_Ice"
arm_l_fore.rotation_euler = (0, 0, math.radians(-8))
arm_l_fore.data.materials.append(mat_frost_base)
objects_to_join.append(arm_l_fore)

bpy.ops.mesh.primitive_cone_add(radius1=0.04, depth=0.12, vertices=4, location=(-0.34, 0.03, 0.83))
ice_spike_1 = bpy.context.active_object
ice_spike_1.name = "Ice_Spike_Elbow"
ice_spike_1.rotation_euler = (0, math.radians(40), math.radians(45))
ice_spike_1.data.materials.append(mat_frost_high)
objects_to_join.append(ice_spike_1)

bpy.ops.mesh.primitive_uv_sphere_add(segments=8, ring_count=6, radius=0.065, location=(-0.32, -0.03, 0.63))
fist_l = bpy.context.active_object
fist_l.name = "Fist_L_Ice"
fist_l.scale = (0.9, 1.1, 1.2)
fist_l.data.materials.append(mat_frost_base)
objects_to_join.append(fist_l)


# ==============================================================================
# F. RIGHT WANDERER ARM WITH BANDAGES (#D4C8BC)
# ==============================================================================
bpy.ops.mesh.primitive_cylinder_add(radius=0.075, depth=0.14, vertices=8, location=(0.23, 0, 1.10))
sleeve_r = bpy.context.active_object
sleeve_r.name = "Sleeve_R"
sleeve_r.rotation_euler = (0, 0, math.radians(14))
sleeve_r.data.materials.append(mat_robe_base)
objects_to_join.append(sleeve_r)

bpy.ops.mesh.primitive_cylinder_add(radius=0.065, depth=0.20, vertices=8, location=(0.25, 0, 0.99))
arm_r_up = bpy.context.active_object
arm_r_up.name = "Arm_R_Upper"
arm_r_up.rotation_euler = (0, 0, math.radians(12))
arm_r_up.data.materials.append(mat_robe_trim)
objects_to_join.append(arm_r_up)

bpy.ops.mesh.primitive_cylinder_add(radius=0.07, depth=0.24, vertices=8, location=(0.29, -0.02, 0.79))
arm_r_fore = bpy.context.active_object
arm_r_fore.name = "Arm_R_Fore_Bandages"
arm_r_fore.rotation_euler = (0, 0, math.radians(8))
arm_r_fore.data.materials.append(mat_bandage)
objects_to_join.append(arm_r_fore)

bpy.ops.mesh.primitive_uv_sphere_add(segments=8, ring_count=6, radius=0.06, location=(0.31, -0.03, 0.63))
fist_r = bpy.context.active_object
fist_r.name = "Fist_R_Hand"
fist_r.scale = (0.9, 1.1, 1.1)
fist_r.data.materials.append(mat_bandage)
objects_to_join.append(fist_r)


# ==============================================================================
# G. LEGS & BOOTS (#4A2E1B / #23160D)
# ==============================================================================
# Left Leg
bpy.ops.mesh.primitive_cylinder_add(radius=0.075, depth=0.24, vertices=8, location=(-0.10, 0, 0.52))
thigh_l = bpy.context.active_object
thigh_l.data.materials.append(mat_robe_trim)
objects_to_join.append(thigh_l)

bpy.ops.mesh.primitive_cylinder_add(radius=0.085, depth=0.26, vertices=8, location=(-0.10, 0, 0.30))
boot_l_calf = bpy.context.active_object
boot_l_calf.data.materials.append(mat_boots_base)
objects_to_join.append(boot_l_calf)

bpy.ops.mesh.primitive_torus_add(major_radius=0.095, minor_radius=0.02, major_segments=10, minor_segments=4, location=(-0.10, 0, 0.40))
boot_l_cuff = bpy.context.active_object
boot_l_cuff.data.materials.append(mat_baldric)
objects_to_join.append(boot_l_cuff)

bpy.ops.mesh.primitive_cube_add(size=0.12, location=(-0.10, -0.06, 0.12))
boot_l_foot = bpy.context.active_object
boot_l_foot.scale = (1.0, 1.5, 0.9)
boot_l_foot.rotation_euler = (math.radians(6), 0, 0)
boot_l_foot.data.materials.append(mat_boots_base)
objects_to_join.append(boot_l_foot)

bpy.ops.mesh.primitive_cube_add(size=0.125, location=(-0.10, -0.06, 0.04))
boot_l_sole = bpy.context.active_object
boot_l_sole.scale = (1.05, 1.55, 0.35)
boot_l_sole.rotation_euler = (math.radians(6), 0, 0)
boot_l_sole.data.materials.append(mat_boots_sole)
objects_to_join.append(boot_l_sole)

# Right Leg
bpy.ops.mesh.primitive_cylinder_add(radius=0.075, depth=0.24, vertices=8, location=(0.10, 0, 0.52))
thigh_r = bpy.context.active_object
thigh_r.data.materials.append(mat_robe_trim)
objects_to_join.append(thigh_r)

bpy.ops.mesh.primitive_cylinder_add(radius=0.085, depth=0.26, vertices=8, location=(0.10, 0, 0.30))
boot_r_calf = bpy.context.active_object
boot_r_calf.data.materials.append(mat_boots_base)
objects_to_join.append(boot_r_calf)

bpy.ops.mesh.primitive_torus_add(major_radius=0.095, minor_radius=0.02, major_segments=10, minor_segments=4, location=(0.10, 0, 0.40))
boot_r_cuff = bpy.context.active_object
boot_r_cuff.data.materials.append(mat_baldric)
objects_to_join.append(boot_r_cuff)

bpy.ops.mesh.primitive_cube_add(size=0.12, location=(0.10, -0.06, 0.12))
boot_r_foot = bpy.context.active_object
boot_r_foot.scale = (1.0, 1.5, 0.9)
boot_r_foot.rotation_euler = (math.radians(6), 0, 0)
boot_r_foot.data.materials.append(mat_boots_base)
objects_to_join.append(boot_r_foot)

bpy.ops.mesh.primitive_cube_add(size=0.125, location=(0.10, -0.06, 0.04))
boot_r_sole = bpy.context.active_object
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

kaelen_v3 = bpy.context.active_object
kaelen_v3.name = "Kaelen_V3"

for f in kaelen_v3.data.polygons:
    f.use_smooth = True

bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

tri_count = sum([len(p.vertices) - 2 for p in kaelen_v3.data.polygons])
print(f"KAELEN_V3_CLEAN_TRIS:{tri_count}")

export_path = "D:/GodotProjects/Lentera-Pudar/Assets/Models/Kaelen_V3.gltf"
bpy.ops.export_scene.gltf(
    filepath=export_path,
    export_format='GLTF_SEPARATE',
    export_yup=True,
    export_apply=True
)
print(f"EXPORT_SUCCESS:{export_path}")

import bpy
import math
import os

# ==============================================================================
# LENTERA PUDAR - HIGH-DETAIL 3D KAELEN MODEL V2 (SMOOTH ANIME FF7 GRADE)
# Blender 5.2 LTS: Smooth Normals, Organic Curves, Rich Triad Colors,
# Glowing Cursed Crystal Ice Arm, Emissive Golden Scarf & Stylized Studio Render
# ==============================================================================

def reset_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    if not bpy.data.scenes:
        bpy.data.scenes.new("Scene")
    scene = bpy.context.scene
    # Set background color to dark atmospheric charcoal
    scene.world = bpy.data.worlds.new("DarkWorld")
    scene.world.use_nodes = True
    bg_node = scene.world.node_tree.nodes.get('Background')
    if bg_node:
        bg_node.inputs['Color'].default_value = (0.04, 0.03, 0.05, 1.0)
        bg_node.inputs['Strength'].default_value = 0.5


def create_cel_material(name, base_color, roughness=0.4, metallic=0.0, emission_color=(0,0,0,1), emission_strength=0.0):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    nodes.clear()
    
    bsdf = nodes.new('ShaderNodeBsdfPrincipled')
    bsdf.inputs['Base Color'].default_value = base_color
    bsdf.inputs['Roughness'].default_value = roughness
    bsdf.inputs['Metallic'].default_value = metallic
    
    if 'Emission Color' in bsdf.inputs:
        bsdf.inputs['Emission Color'].default_value = emission_color
        bsdf.inputs['Emission Strength'].default_value = emission_strength
    elif 'Emission' in bsdf.inputs:
        bsdf.inputs['Emission'].default_value = (
            emission_color[0] * emission_strength,
            emission_color[1] * emission_strength,
            emission_color[2] * emission_strength,
            1.0
        )
        
    output = nodes.new('ShaderNodeOutputMaterial')
    mat.node_tree.links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    return mat


def setup_materials():
    mats = {}
    # Hair: Silver (#D4D8E2)
    mats['Hair'] = create_cel_material("Mat_Hair", (0.80, 0.82, 0.88, 1.0), roughness=0.3)
    
    # Skin: Peach (#E8B082)
    mats['Skin'] = create_cel_material("Mat_Skin", (0.92, 0.68, 0.50, 1.0), roughness=0.5)
    
    # Eyepatch & Soles: Pure Dark Leather (#141013)
    mats['Eyepatch'] = create_cel_material("Mat_Eyepatch", (0.05, 0.04, 0.05, 1.0), roughness=0.2, metallic=0.1)
    
    # Silver Metallic Buckles: (#D0D7DE)
    mats['Silver'] = create_cel_material("Mat_Silver", (0.85, 0.88, 0.92, 1.0), roughness=0.1, metallic=0.95)
    
    # Scarf of Aina: Glowing Warm Ember Gold (#F4B860 2700K)
    mats['Scarf'] = create_cel_material("Mat_Scarf", (0.98, 0.72, 0.28, 1.0), roughness=0.4, emission_color=(1.0, 0.75, 0.30, 1.0), emission_strength=2.8)
    
    # Cursed Frost Ice Arm: Radiant Glowing Blue Ice (#4A7EC4 & #7EE8FA)
    mats['IceArm'] = create_cel_material("Mat_IceArm", (0.28, 0.68, 0.95, 1.0), roughness=0.1, metallic=0.1, emission_color=(0.35, 0.75, 1.0, 1.0), emission_strength=3.5)
    
    # Wanderer Tunic: Dark Ancient Robe (#2A211C)
    mats['Tunic'] = create_cel_material("Mat_Tunic", (0.12, 0.09, 0.08, 1.0), roughness=0.7)
    
    # Leather Belts & Travel Boots: (#5C3218)
    mats['Leather'] = create_cel_material("Mat_Leather", (0.36, 0.18, 0.08, 1.0), roughness=0.3, metallic=0.1)
    
    # Bandages: (#FAF2EC)
    mats['Bandages'] = create_cel_material("Mat_Bandages", (0.96, 0.92, 0.88, 1.0), roughness=0.6)
    
    return mats


def make_smooth(obj):
    for poly in obj.data.polygons:
        poly.use_smooth = True


def build_kaelen_ff7_v2(mats):
    parts = []
    
    # --------------------------------------------------------------------------
    # 1. HEAD, FACE & EYEPATCH (Smooth Organic Anime Topology)
    # --------------------------------------------------------------------------
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=20, radius=0.125, location=(0, -0.01, 1.60))
    head = bpy.context.active_object
    head.name = "Head_Base"
    head.scale = (0.90, 1.02, 1.12)
    make_smooth(head)
    head.data.materials.append(mats['Skin'])
    parts.append(head)
    
    # Anime Chin / Jaw
    bpy.ops.mesh.primitive_cone_add(vertices=24, radius1=0.075, radius2=0.015, depth=0.09, location=(0, -0.045, 1.49))
    chin = bpy.context.active_object
    chin.name = "Chin_Jaw"
    chin.rotation_euler = (math.radians(-12), 0, 0)
    make_smooth(chin)
    chin.data.materials.append(mats['Skin'])
    parts.append(chin)

    # Nose
    bpy.ops.mesh.primitive_cone_add(vertices=6, radius1=0.015, radius2=0.002, depth=0.032, location=(0, -0.132, 1.585))
    nose = bpy.context.active_object
    nose.name = "Nose_Bridge"
    nose.rotation_euler = (math.radians(72), 0, 0)
    make_smooth(nose)
    nose.data.materials.append(mats['Skin'])
    parts.append(nose)

    # Neck
    bpy.ops.mesh.primitive_cylinder_add(vertices=20, radius=0.055, depth=0.13, location=(0, -0.01, 1.47))
    neck = bpy.context.active_object
    neck.name = "Neck"
    make_smooth(neck)
    neck.data.materials.append(mats['Skin'])
    parts.append(neck)

    # 3D Eyepatch (Right Eye: +X)
    bpy.ops.mesh.primitive_uv_sphere_add(segments=16, ring_count=10, radius=0.038, location=(0.045, -0.112, 1.61))
    eyepatch = bpy.context.active_object
    eyepatch.name = "Eyepatch"
    eyepatch.scale = (1.1, 0.35, 0.95)
    make_smooth(eyepatch)
    eyepatch.data.materials.append(mats['Eyepatch'])
    parts.append(eyepatch)
    
    # Silver Rivet
    bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=8, radius=0.009, location=(0.045, -0.125, 1.61))
    rivet = bpy.context.active_object
    rivet.name = "Eyepatch_Rivet"
    make_smooth(rivet)
    rivet.data.materials.append(mats['Silver'])
    parts.append(rivet)

    # Eyepatch Leather Strap
    bpy.ops.mesh.primitive_torus_add(major_radius=0.122, minor_radius=0.007, major_segments=32, minor_segments=8, location=(0, -0.01, 1.62))
    strap = bpy.context.active_object
    strap.name = "Eyepatch_Strap"
    strap.rotation_euler = (math.radians(16), math.radians(-10), 0)
    make_smooth(strap)
    strap.data.materials.append(mats['Eyepatch'])
    parts.append(strap)

    # --------------------------------------------------------------------------
    # 2. LAYERED SPIKY ANIME HAIR (Cloud Strife Style)
    # --------------------------------------------------------------------------
    bpy.ops.mesh.primitive_uv_sphere_add(segments=24, ring_count=16, radius=0.145, location=(0, 0.02, 1.65))
    hair_dome = bpy.context.active_object
    hair_dome.name = "Hair_Crown_Dome"
    hair_dome.scale = (1.02, 1.08, 1.04)
    make_smooth(hair_dome)
    hair_dome.data.materials.append(mats['Hair'])
    parts.append(hair_dome)

    # Individual Sculpted Anime Hair Locks
    hair_locks = [
        # Bangs framing face
        (-0.04, -0.12, 1.68, 38, 15, -22, 0.035, 0.035, 0.13),
        (0.01, -0.13, 1.67, 42, -5, 0, 0.04, 0.04, 0.14),
        (0.06, -0.12, 1.68, 38, -20, 25, 0.035, 0.035, 0.12),
        (-0.08, -0.10, 1.64, 32, 28, -35, 0.03, 0.03, 0.11),
        (0.09, -0.09, 1.63, 32, -35, 38, 0.03, 0.03, 0.11),
        # Top Crown Spikes
        (0.0, 0.01, 1.80, -12, 0, 0, 0.045, 0.045, 0.16),
        (-0.06, 0.02, 1.77, -10, 25, -20, 0.038, 0.038, 0.14),
        (0.06, 0.02, 1.77, -10, -25, 20, 0.038, 0.038, 0.14),
        (-0.03, 0.07, 1.74, -35, 15, -15, 0.038, 0.038, 0.15),
        (0.04, 0.07, 1.74, -35, -15, 15, 0.038, 0.038, 0.15),
        # Back & Temples
        (-0.11, -0.03, 1.57, 10, 45, 0, 0.032, 0.032, 0.12),
        (0.11, -0.03, 1.57, 10, -45, 0, 0.032, 0.032, 0.12),
        (-0.08, 0.10, 1.55, -45, 20, 0, 0.036, 0.036, 0.13),
        (0.08, 0.10, 1.55, -45, -20, 0, 0.036, 0.036, 0.13),
        (0.0, 0.12, 1.53, -55, 0, 0, 0.042, 0.042, 0.15),
    ]
    for h_idx, (hx, hy, hz, rx, ry, rz, scx, scy, scz) in enumerate(hair_locks):
        bpy.ops.mesh.primitive_cone_add(vertices=8, radius1=1.0, depth=2.0, location=(hx, hy, hz))
        hl = bpy.context.active_object
        hl.name = f"Hair_Lock_{h_idx:02d}"
        hl.rotation_euler = (math.radians(rx), math.radians(ry), math.radians(rz))
        hl.scale = (scx, scy, scz)
        make_smooth(hl)
        hl.data.materials.append(mats['Hair'])
        parts.append(hl)

    # --------------------------------------------------------------------------
    # 3. SCARF OF AINA (Glowing Golden Ember Collar & S-Curve Ribbon)
    # --------------------------------------------------------------------------
    bpy.ops.mesh.primitive_torus_add(major_radius=0.135, minor_radius=0.048, major_segments=32, minor_segments=16, location=(0, -0.01, 1.44))
    collar1 = bpy.context.active_object
    collar1.name = "Scarf_Collar_Main"
    collar1.scale = (1.1, 1.0, 0.82)
    make_smooth(collar1)
    collar1.data.materials.append(mats['Scarf'])
    parts.append(collar1)

    bpy.ops.mesh.primitive_torus_add(major_radius=0.14, minor_radius=0.042, major_segments=32, minor_segments=16, location=(0, -0.035, 1.40))
    collar2 = bpy.context.active_object
    collar2.name = "Scarf_Collar_Fold"
    collar2.scale = (1.05, 1.05, 0.72)
    collar2.rotation_euler = (math.radians(14), 0, 0)
    make_smooth(collar2)
    collar2.data.materials.append(mats['Scarf'])
    parts.append(collar2)

    # Flowing 3D S-Curve Ribbon Tail (Trailing behind right flank)
    ribbon_path = [
        (0.14, 0.05, 1.41, 10, 30, -15, 0.065, 0.02, 0.13),
        (0.23, 0.12, 1.43, 15, 45, -30, 0.06, 0.018, 0.15),
        (0.32, 0.19, 1.46, 20, 35, -45, 0.055, 0.016, 0.17),
        (0.40, 0.23, 1.46, 10, 15, -60, 0.05, 0.015, 0.17),
        (0.44, 0.21, 1.40, -15, -10, -75, 0.045, 0.014, 0.16),
        (0.45, 0.14, 1.31, -35, -30, -85, 0.04, 0.012, 0.16),
        (0.42, 0.07, 1.20, -50, -45, -90, 0.035, 0.01, 0.15),
        (0.38, 0.02, 1.09, -65, -30, -95, 0.03, 0.008, 0.13),
    ]
    for r_idx, (rx, ry, rz, rotx, roty, rotz, scx, scy, scz) in enumerate(ribbon_path):
        bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=1.0, depth=2.0, location=(rx, ry, rz))
        rt = bpy.context.active_object
        rt.name = f"Scarf_Ribbon_{r_idx:02d}"
        rt.rotation_euler = (math.radians(rotx), math.radians(roty), math.radians(rotz))
        rt.scale = (scx, scy, scz)
        make_smooth(rt)
        rt.data.materials.append(mats['Scarf'])
        parts.append(rt)

    # --------------------------------------------------------------------------
    # 4. WANDERER TUNIC, BELTS & COAT SKIRT
    # --------------------------------------------------------------------------
    bpy.ops.mesh.primitive_cylinder_add(vertices=24, radius=0.165, depth=0.28, location=(0, -0.01, 1.29))
    chest = bpy.context.active_object
    chest.name = "Tunic_Chest"
    chest.scale = (1.18, 0.86, 1.0)
    make_smooth(chest)
    chest.data.materials.append(mats['Tunic'])
    parts.append(chest)

    bpy.ops.mesh.primitive_cylinder_add(vertices=24, radius=0.145, depth=0.20, location=(0, -0.01, 1.11))
    waist = bpy.context.active_object
    waist.name = "Tunic_Waist"
    waist.scale = (1.06, 0.84, 1.0)
    make_smooth(waist)
    waist.data.materials.append(mats['Tunic'])
    parts.append(waist)

    # Waist Belt
    bpy.ops.mesh.primitive_torus_add(major_radius=0.158, minor_radius=0.018, major_segments=32, minor_segments=10, location=(0, -0.01, 1.08))
    belt = bpy.context.active_object
    belt.name = "Waist_Belt"
    belt.scale = (1.06, 0.84, 1.0)
    make_smooth(belt)
    belt.data.materials.append(mats['Leather'])
    parts.append(belt)

    # Silver Belt Buckle
    bpy.ops.mesh.primitive_cube_add(size=0.046, location=(0, -0.152, 1.08))
    buckle = bpy.context.active_object
    buckle.name = "Belt_Buckle"
    buckle.scale = (1.2, 0.3, 0.9)
    make_smooth(buckle)
    buckle.data.materials.append(mats['Silver'])
    parts.append(buckle)

    # Diagonal Baldric Leather Strap
    bpy.ops.mesh.primitive_torus_add(major_radius=0.205, minor_radius=0.014, major_segments=32, minor_segments=10, location=(0, 0, 1.28))
    baldric = bpy.context.active_object
    baldric.name = "Chest_Baldric"
    baldric.rotation_euler = (math.radians(35), math.radians(-38), 0)
    baldric.scale = (1.1, 0.85, 1.0)
    make_smooth(baldric)
    baldric.data.materials.append(mats['Leather'])
    parts.append(baldric)

    # Baldric Chest Buckle
    bpy.ops.mesh.primitive_cube_add(size=0.038, location=(0.04, -0.135, 1.29))
    b_buckle = bpy.context.active_object
    b_buckle.name = "Baldric_Buckle"
    b_buckle.rotation_euler = (math.radians(15), math.radians(-25), 0)
    b_buckle.scale = (1.2, 0.4, 0.9)
    make_smooth(b_buckle)
    b_buckle.data.materials.append(mats['Silver'])
    parts.append(b_buckle)

    # Travel Hip Pouch
    bpy.ops.mesh.primitive_cube_add(size=0.065, location=(-0.165, 0.0, 1.06))
    pouch = bpy.context.active_object
    pouch.name = "Travel_Pouch"
    pouch.scale = (0.7, 1.1, 1.2)
    make_smooth(pouch)
    pouch.data.materials.append(mats['Leather'])
    parts.append(pouch)

    # Coat Skirt
    bpy.ops.mesh.primitive_cone_add(vertices=24, radius1=0.27, radius2=0.15, depth=0.40, location=(0, 0.01, 0.87))
    skirt = bpy.context.active_object
    skirt.name = "Coat_Skirt"
    skirt.scale = (1.08, 0.88, 1.0)
    make_smooth(skirt)
    skirt.data.materials.append(mats['Tunic'])
    parts.append(skirt)

    # --------------------------------------------------------------------------
    # 5. LEFT CURSED FROST ICE ARM (Radiant Glowing Crystalline Spikes & Claws)
    # Character's LEFT arm = -X in 3D local coordinates
    # --------------------------------------------------------------------------
    crystals_data = [
        # Shoulder Pauldron Shards
        (-0.24, -0.02, 1.47, 20, -35, 15, 0.052, 0.052, 0.18),
        (-0.29, -0.04, 1.42, 15, -60, 25, 0.048, 0.048, 0.16),
        (-0.26, 0.04, 1.44, -25, -45, -15, 0.042, 0.042, 0.15),
        (-0.32, -0.01, 1.37, 10, -75, 10, 0.038, 0.038, 0.14),
        # Bicep & Elbow Crystal Horn
        (-0.28, -0.02, 1.25, 10, -10, 5, 0.062, 0.058, 0.16),
        (-0.32, -0.04, 1.24, 25, -45, 30, 0.032, 0.032, 0.11),
        (-0.33, 0.04, 1.15, -45, -30, -20, 0.038, 0.038, 0.13),
        # Forearm Armor Plating
        (-0.30, -0.03, 1.04, 12, -8, 5, 0.068, 0.060, 0.17),
        (-0.34, -0.06, 1.05, 30, -40, 20, 0.032, 0.032, 0.12),
        (-0.35, 0.02, 0.98, -20, -50, -10, 0.034, 0.034, 0.12),
        # Knuckle & Talons
        (-0.31, -0.03, 0.88, 10, -5, 0, 0.048, 0.058, 0.09),
        (-0.33, -0.06, 0.80, 15, -10, 10, 0.015, 0.015, 0.08),
        (-0.31, -0.06, 0.78, 10, -5, 0, 0.016, 0.016, 0.09),
        (-0.29, -0.05, 0.79, 8, 0, -5, 0.016, 0.016, 0.085),
        (-0.27, -0.04, 0.81, 5, 5, -10, 0.014, 0.014, 0.075),
        (-0.34, -0.01, 0.83, 25, -35, 30, 0.015, 0.015, 0.07),
    ]
    for c_idx, (cx, cy, cz, crx, cry, crz, csx, csy, csz) in enumerate(crystals_data):
        bpy.ops.mesh.primitive_cone_add(vertices=6, radius1=1.0, depth=2.0, location=(cx, cy, cz))
        cryst = bpy.context.active_object
        cryst.name = f"Ice_Crystal_{c_idx:02d}"
        cryst.rotation_euler = (math.radians(crx), math.radians(cry), math.radians(crz))
        cryst.scale = (csx, csy, csz)
        # Keep sharp faceted edges for crystal aesthetics
        cryst.data.materials.append(mats['IceArm'])
        parts.append(cryst)

    # --------------------------------------------------------------------------
    # 6. RIGHT BANDAGED ARM (+X)
    # --------------------------------------------------------------------------
    bpy.ops.mesh.primitive_cylinder_add(vertices=20, radius=0.070, depth=0.11, location=(0.22, -0.01, 1.34))
    r_sleeve = bpy.context.active_object
    r_sleeve.name = "Right_Sleeve"
    r_sleeve.rotation_euler = (math.radians(8), math.radians(15), 0)
    make_smooth(r_sleeve)
    r_sleeve.data.materials.append(mats['Tunic'])
    parts.append(r_sleeve)

    bpy.ops.mesh.primitive_cylinder_add(vertices=20, radius=0.054, depth=0.14, location=(0.25, -0.01, 1.24))
    r_bicep = bpy.context.active_object
    r_bicep.name = "Right_Bicep"
    r_bicep.rotation_euler = (math.radians(10), math.radians(12), 0)
    make_smooth(r_bicep)
    r_bicep.data.materials.append(mats['Skin'])
    parts.append(r_bicep)

    bpy.ops.mesh.primitive_cylinder_add(vertices=20, radius=0.052, depth=0.23, location=(0.28, -0.02, 1.05))
    r_forearm = bpy.context.active_object
    r_forearm.name = "Right_Bandaged_Forearm"
    r_forearm.rotation_euler = (math.radians(15), math.radians(8), 0)
    make_smooth(r_forearm)
    r_forearm.data.materials.append(mats['Bandages'])
    parts.append(r_forearm)

    for m in range(6):
        w_z = 0.97 + m * 0.035
        bpy.ops.mesh.primitive_torus_add(major_radius=0.054, minor_radius=0.008, major_segments=20, minor_segments=8, location=(0.28, -0.02, w_z))
        b_ring = bpy.context.active_object
        b_ring.name = f"Bandage_Wrap_{m}"
        b_ring.rotation_euler = (math.radians(15 + (m % 2) * 12), math.radians(8 - (m % 2) * 8), 0)
        make_smooth(b_ring)
        b_ring.data.materials.append(mats['Bandages'])
        parts.append(b_ring)

    bpy.ops.mesh.primitive_cube_add(size=0.068, location=(0.30, -0.03, 0.88))
    r_fist = bpy.context.active_object
    r_fist.name = "Right_Fist"
    r_fist.scale = (0.75, 0.95, 1.1)
    r_fist.rotation_euler = (math.radians(12), 0, 0)
    make_smooth(r_fist)
    r_fist.data.materials.append(mats['Bandages'])
    parts.append(r_fist)

    # --------------------------------------------------------------------------
    # 7. LEGS & DETAILED LEATHER TRAVEL BOOTS
    # --------------------------------------------------------------------------
    for leg_idx, (lx, lname) in enumerate([(-0.11, "Left"), (0.11, "Right")]):
        bpy.ops.mesh.primitive_cylinder_add(vertices=20, radius=0.076, depth=0.33, location=(lx, 0.0, 0.69))
        thigh = bpy.context.active_object
        thigh.name = f"{lname}_Thigh"
        thigh.rotation_euler = (math.radians(5), math.radians(-3 if leg_idx == 0 else 3), 0)
        make_smooth(thigh)
        thigh.data.materials.append(mats['Tunic'])
        parts.append(thigh)

        bpy.ops.mesh.primitive_cylinder_add(vertices=20, radius=0.070, depth=0.28, location=(lx, 0.01, 0.44))
        shin = bpy.context.active_object
        shin.name = f"{lname}_Shin"
        make_smooth(shin)
        shin.data.materials.append(mats['Tunic'])
        parts.append(shin)

        bpy.ops.mesh.primitive_torus_add(major_radius=0.080, minor_radius=0.024, major_segments=24, minor_segments=10, location=(lx, 0.01, 0.32))
        cuff = bpy.context.active_object
        cuff.name = f"{lname}_Boot_Cuff"
        cuff.scale = (1.0, 1.1, 1.0)
        make_smooth(cuff)
        cuff.data.materials.append(mats['Leather'])
        parts.append(cuff)

        bpy.ops.mesh.primitive_cylinder_add(vertices=20, radius=0.068, depth=0.22, location=(lx, 0.0, 0.20))
        b_shaft = bpy.context.active_object
        b_shaft.name = f"{lname}_Boot_Shaft"
        b_shaft.scale = (0.95, 1.15, 1.0)
        make_smooth(b_shaft)
        b_shaft.data.materials.append(mats['Leather'])
        parts.append(b_shaft)

        bpy.ops.mesh.primitive_cube_add(size=0.12, location=(lx, -0.06, 0.06))
        b_foot = bpy.context.active_object
        b_foot.name = f"{lname}_Boot_Foot"
        b_foot.scale = (0.9, 1.7, 0.7)
        b_foot.rotation_euler = (0, 0, math.radians(-8 if leg_idx == 0 else 8))
        make_smooth(b_foot)
        b_foot.data.materials.append(mats['Leather'])
        parts.append(b_foot)

        bpy.ops.mesh.primitive_cube_add(size=0.12, location=(lx, -0.06, 0.015))
        b_sole = bpy.context.active_object
        b_sole.name = f"{lname}_Boot_Sole"
        b_sole.scale = (0.95, 1.8, 0.25)
        b_sole.rotation_euler = (0, 0, math.radians(-8 if leg_idx == 0 else 8))
        make_smooth(b_sole)
        b_sole.data.materials.append(mats['Eyepatch'])
        parts.append(b_sole)

    return parts


def setup_studio_lighting_and_camera():
    # 3-Point Studio Lighting
    # 1. Warm Key Light (2700K Ember Gold) - Front-Left
    bpy.ops.object.light_add(type='AREA', radius=1.2, location=(-2.2, -3.2, 2.6))
    key_light = bpy.context.active_object
    key_light.name = "Key_Light_Warm"
    key_light.data.energy = 850.0
    key_light.data.color = (1.0, 0.82, 0.55)
    key_light.rotation_euler = (math.radians(55), 0, math.radians(-35))

    # 2. Cool Fill Light (6500K Cold Shard) - Front-Right
    bpy.ops.object.light_add(type='AREA', radius=1.4, location=(2.6, -2.8, 2.0))
    fill_light = bpy.context.active_object
    fill_light.name = "Fill_Light_Cool"
    fill_light.data.energy = 380.0
    fill_light.data.color = (0.55, 0.75, 1.0)
    fill_light.rotation_euler = (math.radians(45), 0, math.radians(45))

    # 3. Dramatic Rim Light - Behind
    bpy.ops.object.light_add(type='SPOT', radius=0.6, location=(0.0, 3.0, 2.8))
    rim_light = bpy.context.active_object
    rim_light.name = "Rim_Light"
    rim_light.data.energy = 1200.0
    rim_light.data.color = (1.0, 0.95, 0.90)
    rim_light.rotation_euler = (math.radians(-45), 0, math.radians(180))

    # Dark Studio Floor Platform
    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=1.8, depth=0.08, location=(0, 0, -0.04))
    floor_obj = bpy.context.active_object
    floor_obj.name = "Studio_Floor"
    make_smooth(floor_obj)
    mat_floor = create_cel_material("Mat_Floor", (0.04, 0.03, 0.05, 1.0), roughness=0.3)
    floor_obj.data.materials.append(mat_floor)

    # Camera: Front 3/4 Hero Showcase
    bpy.ops.object.camera_add(location=(-0.7, -3.4, 1.35))
    cam = bpy.context.active_object
    cam.name = "Camera_Showcase"
    cam.rotation_euler = (math.radians(82), 0, math.radians(-11))
    cam.data.lens = 55
    bpy.context.scene.camera = cam


def render_and_export():
    os.makedirs("D:/GodotProjects/Lentera-Pudar/Assets/Models", exist_ok=True)
    
    # 1. Save .blend file
    blend_path = "D:/GodotProjects/Lentera-Pudar/Assets/Models/Kaelen_FF7_HighDetail.blend"
    bpy.ops.wm.save_as_mainfile(filepath=blend_path)
    print(f"BLEND_FILE_SAVED: {blend_path}")

    # 2. Export glTF 2.0 (+Z forward, +Y up)
    gltf_path = "D:/GodotProjects/Lentera-Pudar/Assets/Models/Kaelen_FF7_HighDetail.gltf"
    bpy.ops.export_scene.gltf(
        filepath=gltf_path,
        export_format='GLTF_SEPARATE',
        use_selection=False,
        export_yup=True,
        export_apply=True
    )
    print(f"GLTF_FILE_SAVED: {gltf_path}")

    # 3. Render High-Resolution Full-Body Showcase
    scene = bpy.context.scene
    scene.render.resolution_x = 1280
    scene.render.resolution_y = 1280
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = 'PNG'
    
    qc_res = "D:/GodotProjects/Lentera-Pudar/qc_kaelen_3d_ff7_showcase.png"
    qc_art = "C:/Users/ADIT/.gemini/antigravity-ide/brain/a2da4a95-9af8-46dc-9bec-041d1bb1c0dd/qc_kaelen_3d_ff7_showcase.png"
    
    scene.render.filepath = qc_res
    bpy.ops.render.render(write_still=True)
    
    if os.path.exists(qc_res):
        import shutil
        shutil.copyfile(qc_res, qc_art)
        print(f"QC_SHOWCASE_SAVED: {qc_art}")


def main():
    print("=== STARTING KAELEN 3D FF7 HIGH-DETAIL V2 ===")
    reset_scene()
    mats = setup_materials()
    parts = build_kaelen_ff7_v2(mats)
    print(f"Created {len(parts)} smooth high-detail character components.")
    setup_studio_lighting_and_camera()
    render_and_export()
    print("=== KAELEN 3D FF7 HIGH-DETAIL V2 COMPLETED ===")

if __name__ == "__main__":
    main()

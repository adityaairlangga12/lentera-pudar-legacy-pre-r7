import os
from PIL import Image

def export_layered_parts():
    src_clean = "D:/GodotProjects/Lentera-Pudar/Assets/Sprites/kaelen_reconstructed_front_indexed.png"
    img = Image.open(src_clean).convert("RGBA")
    w, h = img.size
    p = img.load()
    
    # Layer 1: Scarf of Aina (Yellow hues: 5..9 in palette)
    # Scarf Colors: (0xFF, 0xF5, 0xD0), (0xFF, 0xD6, 0x78), (0xF4, 0xB8, 0x60), (0xC2, 0x7E, 0x28), (0x7C, 0x44, 0x10)
    layer_scarf = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    sp = layer_scarf.load()
    
    # Layer 2: Cursed Frost Arm (Blue hues: 10..14)
    # (0xE8, 0xFA, 0xFF), (0x99, 0xD8, 0xF8), (0x4A, 0x7E, 0xC4), (0x28, 0x4D, 0x8C), (0x14, 0x29, 0x54)
    layer_ice = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ip = layer_ice.load()
    
    # Layer 3: Head & Hair & Eyepatch (Y < 24 and hair/skin/eyepatch colors)
    layer_head = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    hp = layer_head.load()
    
    # Layer 4: Base Body, Tunic & Boots
    layer_body = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    bp = layer_body.load()
    
    scarf_rgbs = [(0xFF, 0xF5, 0xD0), (0xFF, 0xD6, 0x78), (0xF4, 0xB8, 0x60), (0xC2, 0x7E, 0x28), (0x7C, 0x44, 0x10)]
    ice_rgbs = [(0xE8, 0xFA, 0xFF), (0x99, 0xD8, 0xF8), (0x4A, 0x7E, 0xC4), (0x28, 0x4D, 0x8C), (0x14, 0x29, 0x54)]
    
    for y in range(h):
        for x in range(w):
            r, g, b, a = p[x, y]
            if a == 0:
                continue
            rgb = (r, g, b)
            
            # Scarf layer
            if rgb in scarf_rgbs:
                sp[x, y] = (r, g, b, a)
            # Cursed arm layer (Left arm: x < 14 and y in 22..55)
            elif (rgb in ice_rgbs) or (x < 13 and y >= 22 and y <= 55):
                ip[x, y] = (r, g, b, a)
            # Head layer
            elif y <= 26 and (x >= 12 and x <= 36):
                hp[x, y] = (r, g, b, a)
            # Body & Tunic & Boots
            else:
                bp[x, y] = (r, g, b, a)

    out_dir = "D:/GodotProjects/Lentera-Pudar/Assets/Sprites/Layers"
    os.makedirs(out_dir, exist_ok=True)
    
    layer_scarf.save(os.path.join(out_dir, "layer_04_scarf_aina.png"))
    layer_ice.save(os.path.join(out_dir, "layer_03_cursed_frost_arm.png"))
    layer_head.save(os.path.join(out_dir, "layer_02_head_hair_face.png"))
    layer_body.save(os.path.join(out_dir, "layer_01_body_tunic_boots.png"))
    
    print("LAYERS_EXPORTED_TO:", out_dir)

if __name__ == "__main__":
    export_layered_parts()

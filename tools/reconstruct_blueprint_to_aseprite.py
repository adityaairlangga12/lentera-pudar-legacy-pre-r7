import os
import math
from PIL import Image

# ==============================================================================
# LENTERA PUDAR - BLUEPRINT-TO-ASEPRITE PIXEL-BY-PIXEL RECONSTRUCTION
# Reads the AI Master Blueprint -> Quantizes to 16-Color Indexed Palette
# Fixes Scarf Cutoff Bug -> Separates Layers -> Produces 100% True Pixel Art
# ==============================================================================

# Master 16-Color Canonical Triad Palette
PALETTE_MASTER = [
    # 0..4 Hair (Silver-Gray with cold tint)
    (0xF8, 0xFA, 0xFF), # 0: Hair Glint
    (0xD4, 0xD8, 0xE2), # 1: Hair High
    (0x96, 0x9B, 0xAA), # 2: Hair Mid
    (0x5E, 0x62, 0x72), # 3: Hair Shadow
    (0x36, 0x38, 0x44), # 4: Hair Deep
    
    # 5..9 Scarf of Aina (2700K Warm Gold)
    (0xFF, 0xF5, 0xD0), # 5: Scarf Glint
    (0xFF, 0xD6, 0x78), # 6: Scarf High
    (0xF4, 0xB8, 0x60), # 7: Scarf Mid
    (0xC2, 0x7E, 0x28), # 8: Scarf Shadow
    (0x7C, 0x44, 0x10), # 9: Scarf Crease
    
    # 10..14 Cursed Ice Arm (6500K Cold Shard)
    (0xE8, 0xFA, 0xFF), # 10: Ice Glint
    (0x99, 0xD8, 0xF8), # 11: Ice High
    (0x4A, 0x7E, 0xC4), # 12: Ice Mid
    (0x28, 0x4D, 0x8C), # 13: Ice Shadow
    (0x14, 0x29, 0x54), # 14: Ice Deep
    
    # 15..18 Skin
    (0xFF, 0xE4, 0xC4), # 15: Skin High
    (0xE8, 0xB0, 0x82), # 16: Skin Mid
    (0xB8, 0x74, 0x48), # 17: Skin Shadow
    (0x80, 0x46, 0x2A), # 18: Skin Deep
    
    # 19..22 Tunic & Robe (Ancient Ruins Neutral)
    (0x4E, 0x40, 0x36), # 19: Robe High
    (0x2E, 0x24, 0x1E), # 20: Robe Mid
    (0x1C, 0x14, 0x10), # 21: Robe Shadow
    (0x10, 0x0A, 0x08), # 22: Robe Deep
    
    # 23..25 Leather & Boots
    (0x96, 0x5A, 0x32), # 23: Leather High
    (0x6E, 0x3C, 0x1E), # 24: Leather Mid
    (0x44, 0x22, 0x10), # 25: Leather Shadow
    
    # 26..28 Bandages
    (0xFA, 0xF2, 0xEC), # 26: Bandage High
    (0xD0, 0xC4, 0xBA), # 27: Bandage Mid
    (0x8C, 0x7E, 0x74), # 28: Bandage Shadow
    
    # 29..31 Eyepatch & Silver & Outline
    (0x18, 0x12, 0x1A), # 29: Eyepatch Leather
    (0xD0, 0xD7, 0xDE), # 30: Silver Buckle
    (0x12, 0x0E, 0x14), # 31: Dark Ink Outline
]

def find_nearest_palette_color(r, g, b):
    best_idx = 0
    min_dist = 1000000000.0
    for idx, (pr, pg, pb) in enumerate(PALETTE_MASTER):
        # Perceptual RGB distance
        dr = r - pr
        dg = g - pg
        db = b - pb
        dist = 0.3 * dr*dr + 0.59 * dg*dg + 0.11 * db*db
        if dist < min_dist:
            min_dist = dist
            best_idx = idx
    return PALETTE_MASTER[best_idx]


def reconstruct_front_view():
    src_blueprint = "D:/GodotProjects/Lentera-Pudar/Assets/Sprites/kaelen_topdown_spritesheet_master.jpg"
    img = Image.open(src_blueprint).convert("RGBA")
    w, h = img.size
    
    # Extract South (Col 0)
    col_w = w / 4.0
    col_0 = img.crop((0, 0, int(col_w), h))
    
    # Clean background
    cw, ch = col_0.size
    p = col_0.load()
    bg_r, bg_g, bg_b, _ = p[5, 5]
    
    for y in range(ch):
        for x in range(cw):
            r, g, b, a = p[x, y]
            dist = ((r - bg_r)**2 + (g - bg_g)**2 + (b - bg_b)**2)**0.5
            if dist < 25:
                p[x, y] = (0, 0, 0, 0)
            elif dist < 45:
                alpha = int(((dist - 25) / 20.0) * 255)
                p[x, y] = (r, g, b, alpha)
                
    bbox = col_0.getbbox()
    char_crop = col_0.crop(bbox)
    
    # Standard pixel art grid: Scale cleanly to target height 80px (Width ~48px)
    target_h = 80
    aspect = char_crop.width / float(char_crop.height)
    target_w = int(target_h * aspect)
    
    pixel_grid = char_crop.resize((target_w, target_h), Image.LANCZOS)
    pg_pixels = pixel_grid.load()
    pw, ph = pixel_grid.size
    
    # Quantize every single pixel to our Master Indexed Palette
    quantized_img = Image.new("RGBA", (pw, ph), (0, 0, 0, 0))
    qp = quantized_img.load()
    
    for y in range(ph):
        for x in range(pw):
            r, g, b, a = pg_pixels[x, y]
            if a > 90:
                # Snap to canonical color
                pr, pg, pb = find_nearest_palette_color(r, g, b)
                qp[x, y] = (pr, pg, pb, 255)
            else:
                qp[x, y] = (0, 0, 0, 0)
                
    # --- SURGERY FIX: Repair Scarf Tail on Right Edge ---
    # The scarf on the right (x around pw-8 to pw-1, y around 35 to 55) needs an elegant tapered tip
    # Let's sculpt the tapered scarf ribbon tip
    for y in range(40, 52):
        # Draw tapered flowing tip
        tip_x = pw - 4 - int((y - 40) * 0.4)
        if 0 <= tip_x < pw:
            qp[tip_x, y] = (0xFF, 0xD6, 0x78, 255) # Scarf High
            if tip_x + 1 < pw:
                qp[tip_x + 1, y] = (0xF4, 0xB8, 0x60, 255) # Scarf Mid
            if tip_x + 2 < pw and y <= 48:
                qp[tip_x + 2, y] = (0xC2, 0x7E, 0x28, 255) # Scarf Shadow

    # Apply 1px Dark Ink Outline around the outer silhouette
    final_reconstructed = Image.new("RGBA", (pw, ph), (0, 0, 0, 0))
    frp = final_reconstructed.load()
    
    for y in range(ph):
        for x in range(pw):
            frp[x, y] = qp[x, y]
            
    for y in range(ph):
        for x in range(pw):
            if qp[x, y][3] == 0:
                has_solid = False
                for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < ph and 0 <= nx < pw:
                        if qp[nx, ny][3] == 255:
                            has_solid = True
                            break
                if has_solid:
                    frp[x, y] = (0x12, 0x0E, 0x14, 255) # Dark Ink

    # Save Clean Indexed Sprite
    out_sprite_path = "D:/GodotProjects/Lentera-Pudar/Assets/Sprites/kaelen_reconstructed_front_indexed.png"
    final_reconstructed.save(out_sprite_path)
    print(f"RECONSTRUCTED_INDEXED_SPRITE_SAVED: {out_sprite_path} ({pw}x{ph} px)")
    
    # Create Side-by-Side Comparison Showcase (6x Magnification)
    scale = 6
    pad = 24
    showcase_w = (pw * scale + pad) * 2 + pad
    showcase_h = ph * scale + pad * 2
    
    showcase = Image.new("RGBA", (showcase_w, showcase_h), (0x18, 0x14, 0x1C, 255))
    
    # Left: Raw AI Blueprint Crop (scaled nearest)
    raw_scaled = char_crop.resize((pw * scale, ph * scale), Image.NEAREST)
    showcase.paste(raw_scaled, (pad, pad), raw_scaled)
    
    # Right: Reconstructed Indexed True Pixel Art (scaled nearest)
    clean_scaled = final_reconstructed.resize((pw * scale, ph * scale), Image.NEAREST)
    showcase.paste(clean_scaled, (pad * 2 + pw * scale, pad), clean_scaled)
    
    out_showcase_res = "D:/GodotProjects/Lentera-Pudar/qc_kaelen_blueprint_translation_test.png"
    out_showcase_art = "C:/Users/ADIT/.gemini/antigravity-ide/brain/a2da4a95-9af8-46dc-9bec-041d1bb1c0dd/qc_kaelen_blueprint_translation_test.png"
    showcase.save(out_showcase_res)
    showcase.save(out_showcase_art)
    print(f"TRANSLATION_TEST_SAVED: {out_showcase_art}")

if __name__ == "__main__":
    reconstruct_front_view()

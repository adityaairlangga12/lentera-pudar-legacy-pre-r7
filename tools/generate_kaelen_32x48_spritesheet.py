import os
import math
from PIL import Image

# ==============================================================================
# LENTERA PUDAR - KAELEN V3 MASTER 32x48 PIXEL ART SPRITESHEET GENERATOR
# Canonical Colors: The Triad of Lentera Pudar (#F4B860, #4A6FA5, #2A211C)
# Animations: Idle (4 frames) & Walk (4 frames) for 4 Cardinal Directions
# ==============================================================================

# Palette Definitions
C_TRANSPARENT = (0, 0, 0, 0)
C_OUTLINE     = (0x14, 0x10, 0x13, 0xFF) # #141013 Dark Ink Outline
C_SHADOW_FLOOR= (0x14, 0x10, 0x13, 0x70) # Floor Shadow (Alpha)

# Hair (Silver-Gray)
C_HAIR_HI     = (0xEE, 0xEE, 0xEE, 0xFF) # #EEEEEE
C_HAIR_MID    = (0x9E, 0x9E, 0x9E, 0xFF) # #9E9E9E
C_HAIR_SHAD   = (0x61, 0x61, 0x61, 0xFF) # #616161
C_HAIR_DEEP   = (0x38, 0x38, 0x38, 0xFF) # #383838

# Skin
C_SKIN_HI     = (0xFF, 0xE0, 0xB2, 0xFF) # #FFE0B2
C_SKIN_MID    = (0xE0, 0xA9, 0x6D, 0xFF) # #E0A96D
C_SKIN_SHAD   = (0xA8, 0x6F, 0x3E, 0xFF) # #A86F3E

# Eyes & Eyepatch
C_EYE_WHITE   = (0xFF, 0xFF, 0xFF, 0xFF)
C_EYE_PUPIL   = (0x14, 0x10, 0x13, 0xFF)
C_EYEPATCH    = (0x14, 0x10, 0x13, 0xFF)
C_EYEPATCH_HI = (0x38, 0x2C, 0x34, 0xFF)
C_SILVER_HI   = (0xFF, 0xFF, 0xFF, 0xFF)
C_SILVER_MID  = (0xD0, 0xD7, 0xDE, 0xFF)

# Scarf of Aina (2700K Warm Gold)
C_SCARF_HI    = (0xFF, 0xE0, 0xB2, 0xFF) # #FFE0B2
C_SCARF_MID   = (0xF4, 0xB8, 0x60, 0xFF) # #F4B860
C_SCARF_SHAD  = (0xC5, 0x8B, 0x3E, 0xFF) # #C58B3E
C_SCARF_DEEP  = (0x8C, 0x4E, 0x18, 0xFF) # #8C4E18

# Cursed Frost Arm (Left Arm: 6500K Cold Blue)
C_FROST_HI    = (0x99, 0xB9, 0xE0, 0xFF) # #99B9E0
C_FROST_MID   = (0x4A, 0x6F, 0xA5, 0xFF) # #4A6FA5
C_FROST_SHAD  = (0x2C, 0x48, 0x75, 0xFF) # #2C4875
C_FROST_DEEP  = (0x16, 0x28, 0x47, 0xFF) # #162847

# Robe & Tunic (Ancient Ruins Dark Neutral)
C_ROBE_HI     = (0x4A, 0x3C, 0x34, 0xFF) # #4A3C34
C_ROBE_MID    = (0x2A, 0x21, 0x1C, 0xFF) # #2A211C
C_ROBE_SHAD   = (0x1A, 0x13, 0x10, 0xFF) # #1A1310
C_ROBE_DEEP   = (0x0D, 0x09, 0x07, 0xFF) # #0D0907

# Leather Baldric & Boots
C_LEATHER_MID = (0x7A, 0x4B, 0x28, 0xFF) # #7A4B28
C_LEATHER_SHAD= (0x4E, 0x2E, 0x16, 0xFF) # #4E2E16
C_BOOT_MID    = (0x4E, 0x2E, 0x16, 0xFF) # #4E2E16
C_BOOT_SHAD   = (0x2A, 0x18, 0x0B, 0xFF) # #2A180B

# Bandages (Right Arm)
C_BAND_HI     = (0xD7, 0xCC, 0xC8, 0xFF) # #D7CCC8
C_BAND_MID    = (0xA1, 0x88, 0x7F, 0xFF) # #A1887F
C_BAND_SHAD   = (0x6D, 0x4C, 0x41, 0xFF) # #6D4C41


def apply_outline(img):
    w, h = img.size
    pixels = img.load()
    out = Image.new("RGBA", (w, h), C_TRANSPARENT)
    out_p = out.load()
    
    for y in range(h):
        for x in range(w):
            out_p[x, y] = pixels[x, y]
            
    for y in range(h):
        for x in range(w):
            if pixels[x, y][3] == 0:
                has_solid = False
                for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < h and 0 <= nx < w:
                        if pixels[nx, ny][3] > 128:
                            has_solid = True
                            break
                if has_solid:
                    out_p[x, y] = C_OUTLINE
    return out


# ==============================================================================
# SOUTH (FRONT) FRAMES
# ==============================================================================
def draw_frame_south(bob=0, scarf_wave=0, leg_phase=0):
    img = Image.new("RGBA", (32, 48), C_TRANSPARENT)
    p = img.load()
    
    # 0. Floor Shadow
    for y in range(44, 47):
        for x in range(8, 24):
            dx = (x - 15.5) / 7.5
            dy = (y - 45.0) / 1.5
            if dx*dx + dy*dy <= 1.0:
                p[x, y] = C_SHADOW_FLOOR
                
    # 1. Legs & Boots (leg_phase: 0=idle, 1=walk_L, 2=walk_pass, 3=walk_R)
    l_off = 0
    r_off = 0
    if leg_phase == 1:
        l_off = -1
        r_off = 1
    elif leg_phase == 3:
        l_off = 1
        r_off = -1
        
    # Left Boot (Character's Right / Viewer's Left: X=10..14)
    for y in range(33 + bob, 44 + l_off):
        for x in range(10, 15):
            p[x, y] = C_BOOT_MID
    for x in range(10, 15):
        p[x, 33 + bob] = C_LEATHER_MID
        p[x, 44 + l_off] = C_OUTLINE
    for y in range(37 + bob, 44 + l_off):
        p[14, y] = C_BOOT_SHAD
        
    # Right Boot (Character's Left / Viewer's Right: X=17..21)
    for y in range(33 + bob, 44 + r_off):
        for x in range(17, 22):
            p[x, y] = C_BOOT_MID
    for x in range(17, 22):
        p[x, 33 + bob] = C_LEATHER_MID
        p[x, 44 + r_off] = C_OUTLINE
    for y in range(37 + bob, 44 + r_off):
        p[17, y] = C_BOOT_SHAD

    # Trousers (Y=28..33)
    for y in range(28 + bob, 34 + bob):
        for x in range(10, 22):
            p[x, y] = C_ROBE_SHAD
    for y in range(30 + bob, 34 + bob):
        p[15, y] = C_ROBE_DEEP
        p[16, y] = C_ROBE_DEEP

    # 2. Tunic Robe, Belt & Baldric (Y=20..30)
    for y in range(20 + bob, 30 + bob):
        for x in range(10, 22):
            p[x, y] = C_ROBE_MID
            if x >= 17:
                p[x, y] = C_ROBE_SHAD
    for y in range(25 + bob, 30 + bob):
        p[9, y] = C_ROBE_MID
        p[22, y] = C_ROBE_SHAD
    p[15, 29 + bob] = C_ROBE_DEEP

    # Belt & Pouch
    for x in range(9, 23):
        p[x, 23 + bob] = C_LEATHER_MID
        p[x, 24 + bob] = C_LEATHER_SHAD
    for y in range(23 + bob, 27 + bob):
        for x in range(7, 10):
            p[x, y] = C_LEATHER_MID
    p[8, 24 + bob] = C_LEATHER_SHAD

    # Diagonal Baldric
    for i in range(7):
        p[18 - i, 16 + i + bob] = C_LEATHER_MID
        p[19 - i, 17 + i + bob] = C_LEATHER_SHAD
    p[14, 18 + bob] = C_SILVER_HI
    p[15, 18 + bob] = C_SILVER_HI
    p[14, 19 + bob] = C_SILVER_MID
    p[15, 19 + bob] = C_OUTLINE

    # 3. Left Cursed Frost Arm (Viewer's Left: X=4..9)
    # Pauldron
    p[5, 15 + bob] = C_FROST_HI
    p[6, 15 + bob] = C_FROST_HI
    p[4, 16 + bob] = C_FROST_HI
    p[5, 16 + bob] = C_FROST_MID
    p[6, 16 + bob] = C_FROST_MID
    p[7, 16 + bob] = C_FROST_SHAD
    # Arm
    for y in range(17 + bob, 27 + bob):
        for x in range(4, 9):
            p[x, y] = C_FROST_MID
            if x <= 5:
                p[x, y] = C_FROST_HI
            elif x >= 7:
                p[x, y] = C_FROST_SHAD
    p[3, 22 + bob] = C_FROST_HI # Elbow spike
    # Fist
    for y in range(27 + bob, 30 + bob):
        for x in range(4, 8):
            p[x, y] = C_FROST_MID
    p[4, 27 + bob] = C_FROST_HI

    # 4. Right Bandaged Arm (Viewer's Right: X=23..27)
    for y in range(16 + bob, 19 + bob):
        for x in range(22, 27):
            p[x, y] = C_ROBE_MID
    for y in range(19 + bob, 29 + bob):
        for x in range(23, 28):
            p[x, y] = C_BAND_MID
            if (x + y) % 3 == 0:
                p[x, y] = C_BAND_HI
            elif x >= 26:
                p[x, y] = C_BAND_SHAD
    for y in range(27 + bob, 30 + bob):
        for x in range(24, 28):
            p[x, y] = C_BAND_MID

    # 5. Scarf of Aina (Y=14..19, X=8..24)
    for y in range(14 + bob, 18 + bob):
        for x in range(9, 23):
            p[x, y] = C_SCARF_MID
            if y == 14 + bob and x <= 16:
                p[x, y] = C_SCARF_HI
            elif y >= 16 + bob or x >= 18:
                p[x, y] = C_SCARF_SHAD
    # Left Shoulder drape fold
    for y in range(15 + bob, 20 + bob):
        for x in range(8, 12):
            p[x, y] = C_SCARF_MID
    p[9, 15 + bob] = C_SCARF_HI
    p[11, 18 + bob] = C_SCARF_DEEP

    # Scarf tail peeking behind right side (+X)
    for y in range(18 + bob, 30 + bob):
        sx = 23 + int(math.sin(scarf_wave + (y - 18) * 0.4) * 1.5)
        p[sx, y] = C_SCARF_MID
        p[sx + 1, y] = C_SCARF_SHAD

    # 6. Face & Head (Y=6..14, X=10..21)
    for y in range(8 + bob, 14 + bob):
        for x in range(11, 21):
            p[x, y] = C_SKIN_MID
            if y >= 12 + bob:
                p[x, y] = C_SKIN_SHAD

    # Right Eyepatch (Viewer's Right: X=16..19)
    for y in range(9 + bob, 13 + bob):
        for x in range(16, 20):
            p[x, y] = C_EYEPATCH
    p[16, 9 + bob] = C_EYEPATCH_HI
    p[17, 10 + bob] = C_SILVER_MID # Silver Rivet
    for x in range(11, 21):
        p[x, 9 + bob] = C_EYEPATCH # Strap

    # Left Eye (Viewer's Left: X=12..14)
    p[12, 9 + bob] = C_OUTLINE
    p[13, 9 + bob] = C_OUTLINE
    p[12, 10 + bob] = C_EYE_WHITE
    p[13, 10 + bob] = C_EYE_PUPIL
    p[14, 10 + bob] = C_EYE_WHITE
    p[12, 10 + bob] = C_EYE_WHITE # Catchlight
    p[13, 11 + bob] = C_EYE_PUPIL

    # 7. Shaggy Hair (Y=2..12, X=8..23)
    for y in range(2 + bob, 8 + bob):
        for x in range(10, 22):
            p[x, y] = C_HAIR_MID
            if x <= 15:
                p[x, y] = C_HAIR_HI
            elif x >= 18:
                p[x, y] = C_HAIR_SHAD
    # Crown Spikes
    p[11, 2 + bob] = C_HAIR_HI
    p[12, 2 + bob] = C_HAIR_HI
    p[10, 3 + bob] = C_HAIR_HI
    p[19, 2 + bob] = C_HAIR_MID
    p[20, 2 + bob] = C_HAIR_SHAD
    p[21, 3 + bob] = C_HAIR_SHAD
    # Bangs
    p[9, 6 + bob] = C_HAIR_HI
    p[9, 7 + bob] = C_HAIR_HI
    p[10, 8 + bob] = C_HAIR_HI
    p[10, 9 + bob] = C_HAIR_MID
    p[10, 10 + bob] = C_HAIR_SHAD
    p[14, 7 + bob] = C_HAIR_HI
    p[15, 8 + bob] = C_HAIR_MID
    p[15, 9 + bob] = C_HAIR_SHAD
    p[21, 6 + bob] = C_HAIR_MID
    p[22, 7 + bob] = C_HAIR_SHAD
    p[22, 8 + bob] = C_HAIR_SHAD

    return apply_outline(img)


# ==============================================================================
# NORTH (BACK) FRAMES
# ==============================================================================
def draw_frame_north(bob=0, scarf_wave=0, leg_phase=0):
    img = Image.new("RGBA", (32, 48), C_TRANSPARENT)
    p = img.load()
    
    # 0. Floor Shadow
    for y in range(44, 47):
        for x in range(8, 24):
            dx = (x - 15.5) / 7.5
            dy = (y - 45.0) / 1.5
            if dx*dx + dy*dy <= 1.0:
                p[x, y] = C_SHADOW_FLOOR

    # 1. Boots
    l_off = 0
    r_off = 0
    if leg_phase == 1:
        l_off = -1
        r_off = 1
    elif leg_phase == 3:
        l_off = 1
        r_off = -1
        
    for y in range(33 + bob, 44 + l_off):
        for x in range(10, 15):
            p[x, y] = C_BOOT_MID
    for x in range(10, 15):
        p[x, 33 + bob] = C_LEATHER_MID
        p[x, 44 + l_off] = C_OUTLINE
        
    for y in range(33 + bob, 44 + r_off):
        for x in range(17, 22):
            p[x, y] = C_BOOT_SHAD
    for x in range(17, 22):
        p[x, 33 + bob] = C_LEATHER_MID
        p[x, 44 + r_off] = C_OUTLINE

    # 2. Robe Back
    for y in range(20 + bob, 30 + bob):
        for x in range(10, 22):
            p[x, y] = C_ROBE_MID
            if x >= 16:
                p[x, y] = C_ROBE_SHAD
    for x in range(9, 23):
        p[x, 23 + bob] = C_LEATHER_MID

    # Left Frost Arm (On Viewer's Right: X=23..27)
    for y in range(16 + bob, 29 + bob):
        for x in range(23, 28):
            p[x, y] = C_FROST_SHAD
    p[27, 21 + bob] = C_FROST_HI
    p[23, 16 + bob] = C_FROST_HI

    # Right Bandaged Arm (On Viewer's Left: X=4..8)
    for y in range(16 + bob, 29 + bob):
        for x in range(4, 9):
            p[x, y] = C_BAND_MID
            if x <= 5:
                p[x, y] = C_BAND_HI

    # Scarf Collar Wrap (Back)
    for y in range(14 + bob, 18 + bob):
        for x in range(9, 23):
            p[x, y] = C_SCARF_MID
            if x <= 15:
                p[x, y] = C_SCARF_HI
            else:
                p[x, y] = C_SCARF_SHAD

    # Flowing Scarf Tail Cascading Down Back in S-Curve (Y=16..38)
    for y in range(16 + bob, 38 + bob):
        tw = max(2, int(5 - (y - 16) * 0.15))
        curve = int(math.sin(scarf_wave + (y - 16) * 0.35) * 2.0)
        tx = 15 - tw // 2 + curve
        for dx in range(tw):
            p[tx + dx, y] = C_SCARF_MID
            if dx == 0:
                p[tx + dx, y] = C_SCARF_HI
            elif dx == tw - 1:
                p[tx + dx, y] = C_SCARF_SHAD
    p[15 + int(math.sin(scarf_wave + 7.5) * 2.0), 38 + bob] = C_SCARF_HI # Scarf tip

    # Rear Hair Mane (Y=2..15, X=8..23)
    for y in range(2 + bob, 14 + bob):
        for x in range(9, 23):
            p[x, y] = C_HAIR_MID
            if x <= 15:
                p[x, y] = C_HAIR_HI
            else:
                p[x, y] = C_HAIR_SHAD
    p[10, 14 + bob] = C_HAIR_HI
    p[11, 15 + bob] = C_HAIR_MID
    p[13, 14 + bob] = C_HAIR_MID
    p[18, 14 + bob] = C_HAIR_SHAD
    p[20, 15 + bob] = C_HAIR_DEEP
    p[12, 2 + bob] = C_HAIR_HI
    p[19, 2 + bob] = C_HAIR_SHAD

    return apply_outline(img)


# ==============================================================================
# EAST / WEST SIDE FRAMES
# ==============================================================================
def draw_frame_side(facing_left=True, bob=0, scarf_wave=0, leg_phase=0):
    img = Image.new("RGBA", (32, 48), C_TRANSPARENT)
    p = img.load()
    
    # 0. Floor Shadow
    for y in range(44, 47):
        for x in range(9, 23):
            p[x, y] = C_SHADOW_FLOOR

    # Boots (Profile)
    for y in range(33 + bob, 44):
        for x in range(12, 18):
            p[x, y] = C_BOOT_MID
    for y in range(41, 45):
        for x in range(10, 15):
            p[x, y] = C_BOOT_MID
    for x in range(10, 18):
        p[x, 44] = C_OUTLINE
        p[x, 33 + bob] = C_LEATHER_MID

    # Robe
    for y in range(22 + bob, 33 + bob):
        for x in range(12, 19):
            p[x, y] = C_ROBE_MID
            if x >= 16:
                p[x, y] = C_ROBE_SHAD
    p[12, 24 + bob] = C_LEATHER_MID
    p[13, 24 + bob] = C_LEATHER_MID

    # Rear Scarf Tail Flowing Behind (+X side)
    for y in range(15 + bob, 37 + bob):
        sw = max(2, int(4 - (y - 15) * 0.1))
        sx = 18 + int(math.sin(scarf_wave + (y - 15) * 0.35) * 2.0)
        for dx in range(sw):
            p[sx + dx, y] = C_SCARF_MID
            if dx == 0:
                p[sx + dx, y] = C_SCARF_HI
            elif dx == sw - 1:
                p[sx + dx, y] = C_SCARF_SHAD

    if facing_left:
        # Cursed Frost Arm in Foreground (X=9..15, Y=16..29)
        p[12, 15 + bob] = C_FROST_HI
        p[11, 16 + bob] = C_FROST_HI
        p[10, 16 + bob] = C_FROST_HI
        for y in range(17 + bob, 28 + bob):
            for x in range(10, 15):
                p[x, y] = C_FROST_MID
                if x <= 11:
                    p[x, y] = C_FROST_HI
                elif x >= 14:
                    p[x, y] = C_FROST_SHAD
        p[16, 21 + bob] = C_FROST_HI # Spike
        for y in range(27 + bob, 30 + bob):
            for x in range(9, 14):
                p[x, y] = C_FROST_MID
    else:
        # Bandaged Arm in Foreground (X=9..15, Y=16..29)
        for y in range(16 + bob, 28 + bob):
            for x in range(10, 15):
                p[x, y] = C_BAND_MID
                if x <= 11:
                    p[x, y] = C_BAND_HI
                elif x >= 14:
                    p[x, y] = C_BAND_SHAD
        for y in range(27 + bob, 30 + bob):
            for x in range(9, 14):
                p[x, y] = C_BAND_MID

    # Scarf Collar
    for y in range(14 + bob, 18 + bob):
        for x in range(11, 19):
            p[x, y] = C_SCARF_MID
    p[11, 14 + bob] = C_SCARF_HI

    # Head Profile
    for y in range(4 + bob, 14 + bob):
        for x in range(11, 20):
            p[x, y] = C_HAIR_MID
            if x <= 14:
                p[x, y] = C_HAIR_HI
            elif x >= 17:
                p[x, y] = C_HAIR_SHAD
    p[13, 2 + bob] = C_HAIR_HI
    p[14, 2 + bob] = C_HAIR_HI
    p[9, 11 + bob] = C_SKIN_MID
    p[10, 10 + bob] = C_EYEPATCH if facing_left else C_EYE_PUPIL

    out = apply_outline(img)
    if not facing_left:
        out = out.transpose(Image.FLIP_LEFT_RIGHT)
    return out


# ==============================================================================
# MAIN SPRITESHEET GENERATION (IDLE & WALK IN 4 DIRECTIONS)
# ==============================================================================
def main():
    os.makedirs("D:/GodotProjects/Lentera-Pudar/Assets/Sprites", exist_ok=True)
    
    # 1. Generate Idle Animation Frames (4 directions x 4 frames)
    # Row 0: South (Front) - 4 frames
    # Row 1: East (Right)  - 4 frames
    # Row 2: North (Back)  - 4 frames
    # Row 3: West (Left)   - 4 frames
    
    frame_w = 32
    frame_h = 48
    num_cols = 4
    num_rows = 4
    
    spritesheet = Image.new("RGBA", (frame_w * num_cols, frame_h * num_rows), C_TRANSPARENT)
    
    # Idle Frames
    for col in range(num_cols):
        bob = 1 if col in [1, 2] else 0
        scarf_wave = col * (math.pi / 2)
        
        # South
        f_south = draw_frame_south(bob=bob, scarf_wave=scarf_wave, leg_phase=0)
        spritesheet.paste(f_south, (col * frame_w, 0 * frame_h))
        
        # East (Facing Right)
        f_east = draw_frame_side(facing_left=False, bob=bob, scarf_wave=scarf_wave, leg_phase=0)
        spritesheet.paste(f_east, (col * frame_w, 1 * frame_h))
        
        # North (Back)
        f_north = draw_frame_north(bob=bob, scarf_wave=scarf_wave, leg_phase=0)
        spritesheet.paste(f_north, (col * frame_w, 2 * frame_h))
        
        # West (Facing Left)
        f_west = draw_frame_side(facing_left=True, bob=bob, scarf_wave=scarf_wave, leg_phase=0)
        spritesheet.paste(f_west, (col * frame_w, 3 * frame_h))

    out_sheet_path = "D:/GodotProjects/Lentera-Pudar/Assets/Sprites/Kaelen_SpriteSheet_32x48.png"
    spritesheet.save(out_sheet_path)
    print("SPRITESHEET_GENERATED:", out_sheet_path)
    
    # 2. Generate 4x Magnified Master QC Contact Sheet
    scale = 4
    showcase = Image.new("RGBA", (spritesheet.width * scale, spritesheet.height * scale), (0x14, 0x10, 0x13, 0xFF))
    scaled_sheet = spritesheet.resize((spritesheet.width * scale, spritesheet.height * scale), Image.NEAREST)
    showcase.paste(scaled_sheet, (0, 0), scaled_sheet)
    
    out_qc_res = "D:/GodotProjects/Lentera-Pudar/qc_kaelen_32x48_spritesheet.png"
    out_qc_art = "C:/Users/ADIT/.gemini/antigravity-ide/brain/a2da4a95-9af8-46dc-9bec-041d1bb1c0dd/qc_kaelen_32x48_spritesheet.png"
    showcase.save(out_qc_res)
    showcase.save(out_qc_art)
    print("QC_SHOWCASE_SAVED:", out_qc_art)

if __name__ == "__main__":
    main()

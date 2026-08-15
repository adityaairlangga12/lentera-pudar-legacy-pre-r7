import os
from PIL import Image

def generate_kaelen_face_texture():
    w, h = 32, 32
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    pixels = img.load()
    
    # Palette definition
    c_skin_base   = (0xE8, 0xB2, 0x82, 0xFF) # #E8B282 Warm Melancholic Skin
    c_skin_shad   = (0xC4, 0x8A, 0x5E, 0xFF) # #C48A5E Jaw/Chin Shadow
    c_skin_deep   = (0x9E, 0x68, 0x42, 0xFF) # #9E6842 Deep Crease
    c_eyepatch    = (0x14, 0x10, 0x13, 0xFF) # #141013 Black Leather
    c_eyepatch_hi = (0x3A, 0x30, 0x36, 0xFF) # Bevel Highlight
    c_strap       = (0x28, 0x1E, 0x1C, 0xFF) # Leather Strap
    c_buckle      = (0xD0, 0xD7, 0xDE, 0xFF) # Silver Strap Buckle
    c_eye_white   = (0xFF, 0xFF, 0xFF, 0xFF) # Pure Sclera
    c_eye_pupil   = (0x14, 0x10, 0x13, 0xFF) # Dark Pupil
    c_eye_glint   = (0xEE, 0xF2, 0xFF, 0xFF) # Crisp Eye Catchlight
    c_eyebrow     = (0x5A, 0x5A, 0x5A, 0xFF) # Gray Brow
    
    # 1. Fill base skin face canvas
    for y in range(h):
        for x in range(w):
            pixels[x, y] = c_skin_base
            
    # 2. Lower jaw and chin shadow
    for y in range(22, 32):
        for x in range(w):
            pixels[x, y] = c_skin_shad
    for y in range(27, 32):
        for x in range(3, 29):
            pixels[x, y] = c_skin_deep

    # 3. Eyepatch strap across the head (Y = 10 to 12)
    for x in range(w):
        pixels[x, 10] = c_strap
        pixels[x, 11] = c_strap

    # 4. Right Eye: Bold Black Leather Eyepatch Plate (X = 16 to 28, Y = 9 to 22)
    # Hexagonal / Diamond plate
    for y in range(9, 23):
        for x in range(16, 29):
            dx = abs(x - 22)
            dy = abs(y - 15)
            if dx + dy <= 7:
                pixels[x, y] = c_eyepatch
                # Top / Left Bevel Highlight
                if (dy + dx >= 6) and (x <= 22 or y <= 15):
                    pixels[x, y] = c_eyepatch_hi

    # Eyepatch silver center rivet
    pixels[22, 15] = c_buckle
    pixels[22, 16] = c_strap

    # 5. Left Eye: Large Bold Melancholic Anime Eye (X = 3 to 14, Y = 10 to 20)
    # Upper Eyelash / Melancholic Slanted Brow
    for x in range(4, 15):
        pixels[x, 10] = c_eyepatch
    for x in range(5, 14):
        pixels[x, 9] = c_eyebrow

    # Sclera (White)
    for y in range(11, 19):
        for x in range(4, 14):
            pixels[x, y] = c_eye_white

    # Big Expressive Dark Pupil
    for y in range(11, 19):
        for x in range(7, 13):
            pixels[x, y] = c_eye_pupil

    # Bright Anime Catchlight (2x2 glint on top-left of pupil)
    pixels[7, 12] = c_eye_glint
    pixels[8, 12] = c_eye_white
    pixels[7, 13] = c_eye_white
    
    # Lower eye border shadow
    for x in range(5, 13):
        pixels[x, 19] = c_skin_shad

    # 6. Subtle Anime Nose Accent
    pixels[15, 18] = c_skin_shad
    pixels[15, 19] = c_skin_deep

    # 7. Melancholic Expression Mouth Line
    for x in range(13, 19):
        pixels[x, 23] = c_skin_deep
        
    os.makedirs("D:/GodotProjects/Lentera-Pudar/Assets/Sprites", exist_ok=True)
    os.makedirs("D:/GodotProjects/Lentera-Pudar/Assets/Models", exist_ok=True)
    
    out_sprites = "D:/GodotProjects/Lentera-Pudar/Assets/Sprites/kaelen_face_32x32.png"
    out_models  = "D:/GodotProjects/Lentera-Pudar/Assets/Models/kaelen_face_32x32.png"
    
    img.save(out_sprites)
    img.save(out_models)
    print(f"FACE_TEXTURE_UPDATED: {out_sprites} & {out_models}")

if __name__ == "__main__":
    generate_kaelen_face_texture()

import os
import shutil
from PIL import Image
from triad_palette_quantizer import quantize_image_triad, PALETTE_CATEGORIES, find_nearest_palette_color

RAW_DIR = r"C:\Users\ADIT\.gemini\antigravity-ide\brain\c041710e-3c46-44a8-a7aa-c1ee7f5420bf\scratch\kaelen_v2_raw\Idle"
CLEANED_DIR = r"C:\Users\ADIT\.gemini\antigravity-ide\brain\c041710e-3c46-44a8-a7aa-c1ee7f5420bf\scratch\kaelen_v2_cleaned\Idle"

BLUE_FROST = (74, 111, 165)      # #4A6FA5
BLUE_HIGHLIGHT = (153, 185, 224)  # #99B9E0
BLUE_SHADOW = (44, 72, 117)      # #2C4875

WRAP_LIGHT = (215, 204, 200)     # #D7CCC8
WRAP_MID = (161, 136, 127)       # #A1887F
WRAP_SHADOW = (109, 76, 65)      # #6D4C41

SKIN_BASE = (224, 169, 109)      # #E0A96D
SKIN_SHADOW = (168, 111, 62)     # #A86F3E

def is_blueish(rgb):
    # Blue dominant
    return (rgb[2] > rgb[0] + 20 and rgb[2] > rgb[1] + 10) or (rgb[0] < 120 and rgb[1] > 100 and rgb[2] > 150)

def is_wraps_color(rgb):
    # White / off-white / gray wraps (low saturation, mid-to-high value)
    diff = max(abs(rgb[0] - rgb[1]), abs(rgb[1] - rgb[2]), abs(rgb[0] - rgb[2]))
    return diff < 30 and rgb[0] > 120 and rgb[1] > 120 and rgb[2] > 120

def perform_pixel_surgery(img: Image.Image, direction: str, anim_name: str) -> Image.Image:
    """Bedah anatomi piksel pada frame Kaelen V2 berdasarkan arah kardinal dan aksinya."""
    # 1. First pass: Quantize to The Triad and remove noise
    q_img = quantize_image_triad(img)
    w, h = q_img.size
    
    pixels = q_img.load()
    
    for y in range(h):
        for x in range(w):
            p = pixels[x, y]
            if p[3] < 128:
                continue
            rgb = (p[0], p[1], p[2])
            
            # --- DIRECTION SPECIFIC ARM RULES ---
            
            # Case A: EAST / NORTH-EAST (Right arm faces camera on screen, Left arm is behind)
            if direction in ["east", "north-east"]:
                # The front-facing arm (X between 16 and 32, Y between 18 and 36) MUST NOT be blue!
                # If PixelLab made it blue, convert it back to normal wraps!
                if is_blueish(rgb) and y >= 18 and y <= 36:
                    if rgb[2] > 180:
                        pixels[x, y] = (WRAP_LIGHT[0], WRAP_LIGHT[1], WRAP_LIGHT[2], 255)
                    elif rgb[2] > 100:
                        pixels[x, y] = (WRAP_MID[0], WRAP_MID[1], WRAP_MID[2], 255)
                    else:
                        pixels[x, y] = (WRAP_SHADOW[0], WRAP_SHADOW[1], WRAP_SHADOW[2], 255)
                        
            # Case B: WEST / NORTH-WEST (Left arm faces camera on screen, Left arm MUST be frost blue!)
            elif direction in ["west", "north-west"]:
                # The front-facing arm in West is Kaelen's LEFT arm.
                # If it's normal wraps, infuse it with Kutukan Pudar Frost Blue!
                if is_wraps_color(rgb) and y >= 18 and y <= 36 and x >= 14 and x <= 34:
                    if (x + y) % 3 == 0:
                        pixels[x, y] = (BLUE_HIGHLIGHT[0], BLUE_HIGHLIGHT[1], BLUE_HIGHLIGHT[2], 255)
                    elif (x + y) % 2 == 0:
                        pixels[x, y] = (BLUE_FROST[0], BLUE_FROST[1], BLUE_FROST[2], 255)
                    else:
                        pixels[x, y] = (BLUE_SHADOW[0], BLUE_SHADOW[1], BLUE_SHADOW[2], 255)
                        
            # Case C: SOUTH / SOUTH-EAST / SOUTH-WEST (Facing forward)
            elif direction in ["south", "south-east", "south-west"]:
                # Screen right (X >= 25) is Left Arm -> MUST have Frost Blue
                # Screen left (X <= 22) is Right Arm -> MUST be Normal Wraps / Skin
                if y >= 18 and y <= 36:
                    if x <= 22 and is_blueish(rgb):
                        # Right arm mistakenly blue -> convert to wraps
                        pixels[x, y] = (WRAP_MID[0], WRAP_MID[1], WRAP_MID[2], 255)
                    elif x >= 26 and is_wraps_color(rgb) and direction == "south":
                        # Left arm on south needs blue ice veins
                        if (x + y) % 2 == 0:
                            pixels[x, y] = (BLUE_FROST[0], BLUE_FROST[1], BLUE_FROST[2], 255)
                            
            # Case D: NORTH (Facing backward)
            elif direction == "north":
                # Screen left (X <= 23) is Left Arm -> Blue
                # Screen right (X >= 25) is Right Arm -> Normal Wraps
                if y >= 18 and y <= 36:
                    if x >= 25 and is_blueish(rgb):
                        pixels[x, y] = (WRAP_MID[0], WRAP_MID[1], WRAP_MID[2], 255)
                    elif x <= 23 and is_wraps_color(rgb):
                        pixels[x, y] = (BLUE_FROST[0], BLUE_FROST[1], BLUE_FROST[2], 255)

    # 3. Third pass: Face Shading on SOUTH view
    if direction == "south" and anim_name in ["rotations", "animating"]:
        if pixels[24, 18][3] > 0 and pixels[24, 18][:3] != (0, 0, 0):
            pixels[24, 18] = (SKIN_SHADOW[0], SKIN_SHADOW[1], SKIN_SHADOW[2], 255)
        if pixels[23, 18][3] > 0 and pixels[23, 18][:3] != (0, 0, 0):
            pixels[23, 18] = (SKIN_SHADOW[0], SKIN_SHADOW[1], SKIN_SHADOW[2], 255)
            
    return q_img

def process_all_kaelen_assets():
    print("--- Starting High-Precision Pixel Surgery on Kaelen V2 Assets ---")
    os.makedirs(CLEANED_DIR, exist_ok=True)
    
    # 1. Process Rotations
    raw_rot_dir = os.path.join(RAW_DIR, "rotations")
    clean_rot_dir = os.path.join(CLEANED_DIR, "rotations")
    os.makedirs(clean_rot_dir, exist_ok=True)
    
    for f in os.listdir(raw_rot_dir):
        if f.lower().endswith(".png"):
            dir_name = os.path.splitext(f)[0]
            in_path = os.path.join(raw_rot_dir, f)
            out_path = os.path.join(clean_rot_dir, f)
            img = Image.open(in_path)
            surged_img = perform_pixel_surgery(img, dir_name, "rotations")
            surged_img.save(out_path, "PNG")
            
    print("[OK] Processed base rotations.")
    
    # 2. Process Animations
    raw_anim_dir = os.path.join(RAW_DIR, "animations")
    clean_anim_dir = os.path.join(CLEANED_DIR, "animations")
    os.makedirs(clean_anim_dir, exist_ok=True)
    
    total_frames = 0
    for anim_folder in os.listdir(raw_anim_dir):
        raw_anim_path = os.path.join(raw_anim_dir, anim_folder)
        clean_anim_path = os.path.join(clean_anim_dir, anim_folder)
        if not os.path.isdir(raw_anim_path):
            continue
            
        os.makedirs(clean_anim_path, exist_ok=True)
        
        for dir_name in os.listdir(raw_anim_path):
            raw_dir_path = os.path.join(raw_anim_path, dir_name)
            clean_dir_path = os.path.join(clean_anim_path, dir_name)
            if not os.path.isdir(raw_dir_path):
                continue
                
            os.makedirs(clean_dir_path, exist_ok=True)
            
            for frame_file in os.listdir(raw_dir_path):
                if frame_file.lower().endswith(".png"):
                    in_frame = os.path.join(raw_dir_path, frame_file)
                    out_frame = os.path.join(clean_dir_path, frame_file)
                    img = Image.open(in_frame)
                    surged_img = perform_pixel_surgery(img, dir_name, anim_folder)
                    surged_img.save(out_frame, "PNG")
                    total_frames += 1
                    
    # Copy metadata.json if exists
    meta_src = os.path.join(os.path.dirname(RAW_DIR), "metadata.json")
    if os.path.exists(meta_src):
        shutil.copy(meta_src, os.path.join(CLEANED_DIR, "metadata.json"))
    
    print(f"[OK] Pixel surgery complete for {total_frames} animation frames!")
    print(f"Cleaned assets located at: {CLEANED_DIR}")

if __name__ == "__main__":
    process_all_kaelen_assets()

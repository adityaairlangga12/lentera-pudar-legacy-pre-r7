import os
import json
import glob
from PIL import Image

RAW_DIR = r"C:\Users\ADIT\.gemini\antigravity-ide\brain\c041710e-3c46-44a8-a7aa-c1ee7f5420bf\scratch\kaelen_v2_raw\Idle"
OUT_DIR = r"D:\GodotProjects\Lentera-Pudar\Assets\Sprites\Characters\Protagonist"

os.makedirs(OUT_DIR, exist_ok=True)

DIRECTIONS = [
    "south",
    "north",
    "east",
    "west",
    "south-east",
    "south-west",
    "north-east",
    "north-west"
]

ANIM_MAP = {
    "idle": "animating",
    "walk": "animating-cfa881e7",
    "dash": "animating-fe8b6839",
    "attack_punch": "jab_attack",
    "attack_cursed": "cross_punch_attack",
    "hurt": "taking_a_punch",
    "death": "falling_backward"
}

ANIM_SPEEDS = {
    "idle": 8.0,
    "walk": 10.0,
    "dash": 15.0,
    "attack_punch": 12.0,
    "attack_cursed": 12.0,
    "hurt": 10.0,
    "death": 8.0
}

ANIM_LOOP = {
    "idle": True,
    "walk": True,
    "dash": False,
    "attack_punch": False,
    "attack_cursed": False,
    "hurt": False,
    "death": False
}

def get_frames_for_dir(anim_folder_name, direction):
    path = os.path.join(RAW_DIR, "animations", anim_folder_name, direction)
    if not os.path.exists(path):
        # Fallback to single rotation frame if animation direction missing
        rot_path = os.path.join(RAW_DIR, "rotations", f"{direction}.png")
        if os.path.exists(rot_path):
            return [rot_path]
        return []
    
    # Sort files naturally (0.png, 1.png, 2.png, or frame_000.png)
    files = [os.path.join(path, f) for f in os.listdir(path) if f.lower().endswith('.png')]
    def sort_key(f):
        base = os.path.splitext(os.path.basename(f))[0]
        try:
            return int(base.replace("frame_", ""))
        except ValueError:
            return base
    files.sort(key=sort_key)
    return files

print("--- Building Kaelen V2 Spritesheets & Metadata ---")

summary = {}

for direction in DIRECTIONS:
    dir_frames = []
    tags = []
    current_frame_idx = 0
    
    for anim_name, folder_name in ANIM_MAP.items():
        frame_files = get_frames_for_dir(folder_name, direction)
        if not frame_files:
            print(f"Warning: No frames for {anim_name} {direction}")
            continue
        
        start_idx = current_frame_idx
        for fpath in frame_files:
            img = Image.open(fpath).convert("RGBA")
            dir_frames.append(img)
            current_frame_idx += 1
        end_idx = current_frame_idx - 1
        
        tags.append({
            "name": anim_name,
            "from": start_idx,
            "to": end_idx,
            "direction": "forward",
            "fps": ANIM_SPEEDS.get(anim_name, 8.0),
            "loop": ANIM_LOOP.get(anim_name, True)
        })
    
    if not dir_frames:
        print(f"Error: No frames found for direction {direction}")
        continue
    
    frame_w, frame_h = 48, 48
    sheet_w = frame_w * len(dir_frames)
    sheet_h = frame_h
    
    spritesheet = Image.new("RGBA", (sheet_w, sheet_h), (0, 0, 0, 0))
    
    frames_meta = {}
    for idx, frame_img in enumerate(dir_frames):
        # Center the 32x32 / 48x48 image if needed
        if frame_img.size == (frame_w, frame_h):
            pasted_img = frame_img
        else:
            pasted_img = Image.new("RGBA", (frame_w, frame_h), (0, 0, 0, 0))
            offset_x = (frame_w - frame_img.width) // 2
            offset_y = frame_h - frame_img.height - 4 # bottom aligned
            pasted_img.paste(frame_img, (offset_x, offset_y), frame_img)
            
        spritesheet.paste(pasted_img, (idx * frame_w, 0))
        frames_meta[f"kaelen_{direction}_{idx}"] = {
            "frame": {"x": idx * frame_w, "y": 0, "w": frame_w, "h": frame_h},
            "rotated": False,
            "trimmed": False,
            "spriteSourceSize": {"x": 0, "y": 0, "w": frame_w, "h": frame_h},
            "sourceSize": {"w": frame_w, "h": frame_h},
            "duration": int(1000 / 8.0)
        }
        
    out_png_path = os.path.join(OUT_DIR, f"protagonist_{direction}.png")
    out_json_path = os.path.join(OUT_DIR, f"protagonist_{direction}.json")
    
    spritesheet.save(out_png_path, "PNG")
    
    meta_json = {
        "frames": frames_meta,
        "meta": {
            "app": "Lentera PixelLab Builder",
            "version": "2.0",
            "image": f"protagonist_{direction}.png",
            "format": "RGBA8888",
            "size": {"w": sheet_w, "h": sheet_h},
            "scale": "1",
            "frameTags": tags
        }
    }
    with open(out_json_path, "w") as jf:
        json.dump(meta_json, jf, indent=2)
        
    summary[direction] = {
        "total_frames": len(dir_frames),
        "tags": [t["name"] for t in tags]
    }
    print(f"Generated protagonist_{direction}.png ({len(dir_frames)} frames, {len(tags)} tags)")

print("Summary:", json.dumps(summary, indent=2))
print("--- Kaelen V2 Spritesheets Built Successfully! ---")

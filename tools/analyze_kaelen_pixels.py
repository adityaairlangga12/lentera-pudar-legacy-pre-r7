import os
import glob
from PIL import Image, ImageDraw, ImageFont

ROT_DIR = r"C:\Users\ADIT\.gemini\antigravity-ide\brain\c041710e-3c46-44a8-a7aa-c1ee7f5420bf\scratch\kaelen_v2_cleaned\Idle\rotations"
ANIM_DIR = r"C:\Users\ADIT\.gemini\antigravity-ide\brain\c041710e-3c46-44a8-a7aa-c1ee7f5420bf\scratch\kaelen_v2_cleaned\Idle\animations"
OUT_IMG = r"C:\Users\ADIT\.gemini\antigravity-ide\brain\c041710e-3c46-44a8-a7aa-c1ee7f5420bf\kaelen_retouched_forensic_sheet.png"

DIRECTIONS = [
    "south",
    "south-east",
    "east",
    "north-east",
    "north",
    "north-west",
    "west",
    "south-west"
]

ROW_CONFIGS = [
    ("Base Rotation", "rotations", 0),
    ("Idle (F1)", "animating", 1),
    ("Walk (F2)", "animating-cfa881e7", 2),
    ("Dash (F1)", "animating-fe8b6839", 1),
    ("Punch (F1)", "jab_attack", 1),
    ("Cursed (F2)", "cross_punch_attack", 2),
    ("Hurt (F1)", "taking_a_punch", 1),
    ("Death (F3)", "falling_backward", 3)
]

def load_frame(folder_type, anim_folder, direction, frame_idx):
    if folder_type == "rotations":
        path = os.path.join(ROT_DIR, f"{direction}.png")
        if os.path.exists(path):
            return Image.open(path).convert("RGBA")
        return None
        
    dir_path = os.path.join(ANIM_DIR, anim_folder, direction)
    if not os.path.exists(dir_path):
        return None
        
    files = sorted([os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.lower().endswith('.png')])
    if not files:
        return None
    idx = min(frame_idx, len(files) - 1)
    return Image.open(files[idx]).convert("RGBA")

ZOOM = 4
CELL_W, CELL_H = 48 * ZOOM, 48 * ZOOM
HEADER_H = 50
SIDEBAR_W = 160
GRID_W = SIDEBAR_W + CELL_W * len(DIRECTIONS)
GRID_H = HEADER_H + CELL_H * len(ROW_CONFIGS)

canvas = Image.new("RGBA", (GRID_W, GRID_H), (18, 16, 15, 255))
draw = ImageDraw.Draw(canvas)

# Draw column headers
for col_idx, d in enumerate(DIRECTIONS):
    px = SIDEBAR_W + col_idx * CELL_W
    draw.text((px + 40, 15), d.upper(), fill=(244, 184, 96, 255))

for row_idx, (label, folder, f_idx) in enumerate(ROW_CONFIGS):
    py = HEADER_H + row_idx * CELL_H
    # Draw row label
    draw.text((15, py + 80), label, fill=(200, 204, 217, 255))
    
    for col_idx, d in enumerate(DIRECTIONS):
        px = SIDEBAR_W + col_idx * CELL_W
        img = load_frame("rotations" if folder == "rotations" else "anim", folder, d, f_idx)
        if img:
            scaled = img.resize((CELL_W, CELL_H), Image.NEAREST)
            canvas.paste(scaled, (px, py), scaled)
        draw.rectangle([px, py, px + CELL_W - 1, py + CELL_H - 1], outline=(45, 40, 37, 255), width=1)

canvas.save(OUT_IMG, "PNG")
print(f"Full forensic sheet saved to: {OUT_IMG}")

import math
from PIL import Image

# ==============================================================================
# THE TRIAD OF LENTERA PUDAR — PALET MASTER BAKU (style-guide.md)
# ==============================================================================

PALETTE_CATEGORIES = {
    "OUTLINE": [
        (0, 0, 0),         # #000000 Solid Black
        (20, 16, 19),      # #141013 Selective Dark Outline
        (13, 9, 7)         # #0D0907 Deep Void
    ],
    "EMBER_OF_AINA": [
        (255, 224, 178),   # #FFE0B2 Highlight
        (244, 184, 96),    # #F4B860 Base Scarf
        (197, 139, 62),    # #C58B3E Midtone / Shadow
        (140, 78, 24)      # #8C4E18 Deep Rim
    ],
    "CURSE_OF_PUDAR": [
        (153, 185, 224),   # #99B9E0 Highlight Ice
        (74, 111, 165),    # #4A6FA5 Base Curse Blue
        (44, 72, 117),     # #2C4875 Shadow Curse
        (22, 40, 71)       # #162847 Abyss Deep
    ],
    "ANCIENT_RUINS_NEUTRAL": [
        (74, 60, 52),      # #4A3C34 Highlight Tunic
        (42, 33, 28),      # #2A211C Base Tunic Dark
        (26, 19, 16)       # #1A1310 Shadow Tunic
    ],
    "HAIR_MESSY_GRAY": [
        (224, 224, 224),   # #E0E0E0 Hair Highlight
        (158, 158, 158),   # #9E9E9E Hair Base Gray
        (97, 97, 97),      # #616161 Hair Shadow
        (60, 60, 65)       # Deep Hair Tone
    ],
    "SKIN_KAELEN": [
        (255, 224, 178),   # #FFE0B2 Skin Highlight
        (224, 169, 109),   # #E0A96D Skin Base
        (168, 111, 62)     # #A86F3E Skin Shadow
    ],
    "NORMAL_BANDAGES": [
        (215, 204, 200),   # #D7CCC8 Bandage Light
        (161, 136, 127),   # #A1887F Bandage Base
        (109, 76, 65)      # #6D4C41 Bandage Shadow
    ],
    "LEATHER_BELT_BOOTS": [
        (139, 69, 19),     # Saddle Brown
        (92, 46, 12),      # Dark Leather
        (58, 29, 8)        # Deep Boot Shadow
    ]
}

# Flatten full target palette
ALL_TRIAD_COLORS = []
for cat, colors in PALETTE_CATEGORIES.items():
    ALL_TRIAD_COLORS.extend(colors)

def color_distance_sq(c1, c2):
    # Weighted Euclidean distance (human eye sensitivity: R: 0.30, G: 0.59, B: 0.11)
    dr = c1[0] - c2[0]
    dg = c1[1] - c2[1]
    db = c1[2] - c2[2]
    return 0.30 * (dr * dr) + 0.59 * (dg * dg) + 0.11 * (db * db)

def find_nearest_palette_color(rgb, allowed_palette=None):
    if allowed_palette is None:
        allowed_palette = ALL_TRIAD_COLORS
    best_color = allowed_palette[0]
    min_dist = float("inf")
    for pal_color in allowed_palette:
        d = color_distance_sq(rgb, pal_color)
        if d < min_dist:
            min_dist = d
            best_color = pal_color
    return best_color

def quantize_image_triad(img: Image.Image) -> Image.Image:
    """Quantize an RGBA PIL image to exact Triad palette colors, removing all color bleed and noise."""
    rgba = img.convert("RGBA")
    w, h = rgba.size
    result = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    
    for x in range(w):
        for y in range(h):
            p = rgba.getpixel((x, y))
            alpha = p[3]
            if alpha < 128:
                result.putpixel((x, y), (0, 0, 0, 0))
                continue
                
            rgb = (p[0], p[1], p[2])
            
            # Detect rogue noise (e.g. pink / magenta artifact: high red & blue, low green)
            if p[0] > 160 and p[2] > 140 and p[1] < 100:
                # Rogue magenta noise -> remap to skin or hair shadow
                quantized_rgb = find_nearest_palette_color(rgb, PALETTE_CATEGORIES["SKIN_KAELEN"] + PALETTE_CATEGORIES["HAIR_MESSY_GRAY"])
            elif p[0] < 35 and p[1] < 35 and p[2] < 35:
                # Outer edge charcoal / black
                quantized_rgb = (0, 0, 0)
            else:
                quantized_rgb = find_nearest_palette_color(rgb)
                
            result.putpixel((x, y), (quantized_rgb[0], quantized_rgb[1], quantized_rgb[2], 255))
            
    return result

if __name__ == "__main__":
    print("The Triad Palette Quantizer module ready.")
    print(f"Total calibrated palette colors: {len(ALL_TRIAD_COLORS)}")

import os
from PIL import Image

def extract_topdown_master_sprites():
    src_path = "D:/GodotProjects/Lentera-Pudar/Assets/Sprites/kaelen_topdown_spritesheet_master.jpg"
    img = Image.open(src_path).convert("RGBA")
    w, h = img.size
    
    # 4 columns
    col_w = w / 4.0
    
    # Background color is dark charcoal ~ (0x28, 0x2A, 0x33)
    # Let's create an alpha-extracted version for each column
    extracted_frames = []
    
    for i in range(4):
        x0 = int(i * col_w)
        x1 = int((i + 1) * col_w)
        col_img = img.crop((x0, 0, x1, h))
        
        # Convert near-background pixels to transparent
        col_rgba = col_img.convert("RGBA")
        p = col_rgba.load()
        cw, ch = col_rgba.size
        
        # Flood fill or threshold background
        # Sample background from top-left corner
        bg_r, bg_g, bg_b, _ = p[5, 5]
        
        for y in range(ch):
            for x in range(cw):
                r, g, b, a = p[x, y]
                # Distance from background color
                dist = ((r - bg_r)**2 + (g - bg_g)**2 + (b - bg_b)**2)**0.5
                if dist < 24:
                    p[x, y] = (0, 0, 0, 0)
                elif dist < 45:
                    # Soft edge blending
                    alpha = int(((dist - 24) / 21.0) * 255)
                    p[x, y] = (r, g, b, alpha)
                    
        # Find tight bounding box of character
        bbox = col_rgba.getbbox()
        if bbox:
            char_crop = col_rgba.crop(bbox)
            extracted_frames.append(char_crop)
            print(f"Frame {i} extracted bbox: {bbox} (Size: {char_crop.size})")

    # Standardize size: target 96x144 px per frame
    target_w, target_h = 160, 240
    master_sheet = Image.new("RGBA", (target_w * 4, target_h), (0, 0, 0, 0))
    
    for i, frame in enumerate(extracted_frames):
        # Resize to fit target height while maintaining aspect ratio
        fw, fh = frame.size
        scale = min((target_w - 20) / float(fw), (target_h - 20) / float(fh))
        new_w = int(fw * scale)
        new_h = int(fh * scale)
        scaled_frame = frame.resize((new_w, new_h), Image.LANCZOS)
        
        # Paste centered in slot
        x_offset = i * target_w + (target_w - new_w) // 2
        y_offset = (target_h - new_h) // 2
        master_sheet.paste(scaled_frame, (x_offset, y_offset), scaled_frame)
        
    out_sheet = "D:/GodotProjects/Lentera-Pudar/Assets/Sprites/Kaelen_TopDown_Master_Sheet.png"
    master_sheet.save(out_sheet)
    print(f"TRANSPARENT_MASTER_SHEET_SAVED: {out_sheet}")

if __name__ == "__main__":
    extract_topdown_master_sprites()

import os
import json
import subprocess

aseprite_exe = r"C:\Program Files\Aseprite\Aseprite.exe"
base_dir = r"D:\GodotProjects\Lentera-Pudar\Assets\Sprites\Characters\Protagonist"
dirs = ["south", "north", "east", "west", "south-east", "south-west", "north-east", "north-west"]

# 1. Export PNGs and JSONs using Aseprite CLI
for d in dirs:
    in_file = os.path.join(base_dir, f"protagonist_{d}.aseprite")
    out_png = os.path.join(base_dir, f"protagonist_{d}.png")
    out_json = os.path.join(base_dir, f"protagonist_{d}.json")
    
    cmd = [
        aseprite_exe, "-b", in_file,
        "--sheet", out_png,
        "--data", out_json,
        "--format", "json-array",
        "--list-tags"
    ]
    subprocess.run(cmd, check=True)

# 2. Build protagonist.tres (SpriteFrames)
tres_lines = [
    '[gd_resource type="SpriteFrames" load_steps=100 format=3]',
    ''
]
ext_res_idx = 1
for d in dirs:
    tres_lines.append(f'[ext_resource type="Texture2D" path="res://Assets/Sprites/Characters/Protagonist/protagonist_{d}.png" id="{ext_res_idx}_tex"]')
    ext_res_idx += 1
tres_lines.append('')

atlases = []
atlas_idx = ext_res_idx
for i, d in enumerate(dirs):
    json_path = os.path.join(base_dir, f"protagonist_{d}.json")
    with open(json_path, 'r') as f:
        data = json.load(f)
        
    for frame in data["frames"]:
        rect = frame["frame"]
        tres_lines.append(f'[sub_resource type="AtlasTexture" id="AtlasTexture_{atlas_idx}"]')
        tres_lines.append(f'atlas = ExtResource("{i+1}_tex")')
        tres_lines.append(f'region = Rect2({rect["x"]}, {rect["y"]}, {rect["w"]}, {rect["h"]})')
        tres_lines.append('')
        atlases.append({"dir": d, "id": atlas_idx})
        atlas_idx += 1

tres_lines.append('[resource]')
tres_lines.append('animations = [{')

# Build animations array
anims = []
# tags are usually 'idle' (frames 0-3) and 'walk' (frames 4-7)
for d in dirs:
    dir_atlases = [a["id"] for a in atlases if a["dir"] == d]
    if len(dir_atlases) >= 8:
        # idle
        idle_frames = dir_atlases[0:4]
        idle_str = ', '.join([f'{{"duration": 1.0, "texture": SubResource("AtlasTexture_{id}")}}' for id in idle_frames])
        anims.append(f'{{"frames": [{idle_str}], "loop": true, "name": &"idle_{d}", "speed": 8.0}}')
        # walk
        walk_frames = dir_atlases[4:8]
        walk_str = ', '.join([f'{{"duration": 1.0, "texture": SubResource("AtlasTexture_{id}")}}' for id in walk_frames])
        anims.append(f'{{"frames": [{walk_str}], "loop": true, "name": &"walk_{d}", "speed": 8.0}}')

tres_lines.append(',\n'.join(anims))
tres_lines.append('}]')

with open(os.path.join(base_dir, "protagonist.tres"), "w") as f:
    f.write("\n".join(tres_lines))

# 3. Generate Player.tscn
player_tscn = """[gd_scene load_steps=5 format=3]

[ext_resource type="Script" path="res://Scripts/Player.gd" id="1_script"]
[ext_resource type="SpriteFrames" path="res://Assets/Sprites/Characters/Protagonist/protagonist.tres" id="2_frames"]
[ext_resource type="Shader" path="res://Shaders/CursedHand.gdshader" id="3_shader"]

[sub_resource type="ShaderMaterial" id="ShaderMaterial_cursed"]
shader = ExtResource("3_shader")
shader_parameter/cursed_color = Color(0.29, 0.435, 0.647, 1)
shader_parameter/pulse_speed = 2.0
shader_parameter/intensity = 0.5

[sub_resource type="Gradient" id="Gradient_light"]
offsets = PackedFloat32Array(0, 0.7)
colors = PackedColorArray(1, 1, 1, 1, 0, 0, 0, 1)

[sub_resource type="GradientTexture2D" id="GradientTexture2D_light"]
gradient = SubResource("Gradient_light")
fill = 1
fill_from = Vector2(0.5, 0.5)
fill_to = Vector2(0.9, 0.1)

[node name="Player" type="CharacterBody2D"]
script = ExtResource("1_script")

[node name="AnimatedSprite2D" type="AnimatedSprite2D" parent="."]
material = SubResource("ShaderMaterial_cursed")
sprite_frames = ExtResource("2_frames")
animation = &"idle_down"

[node name="ScarfLight" type="PointLight2D" parent="."]
position = Vector2(0, -2)
color = Color(0.957, 0.722, 0.376, 1)
energy = 1.2
texture = SubResource("GradientTexture2D_light")
texture_scale = 1.5
"""
with open(r"D:\GodotProjects\Lentera-Pudar\Scenes\Player.tscn", "w") as f:
    f.write(player_tscn)

# 4. Generate World.tscn
world_tscn = """[gd_scene load_steps=2 format=3]

[ext_resource type="PackedScene" path="res://Scenes/Player.tscn" id="1_player"]

[node name="World" type="Node2D"]

[node name="CanvasModulate" type="CanvasModulate" parent="."]
color = Color(0.165, 0.129, 0.11, 1)

[node name="Player" parent="." instance=ExtResource("1_player")]
position = Vector2(240, 135)

[node name="Camera2D" type="Camera2D" parent="Player"]
zoom = Vector2(2, 2)
"""
with open(r"D:\GodotProjects\Lentera-Pudar\Scenes\World.tscn", "w") as f:
    f.write(world_tscn)

print("Godot scenes and resources generated successfully!")

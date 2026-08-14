extends SceneTree

func _init():
    var frames = SpriteFrames.new()
    var dirs = ["south", "north", "east", "west", "south-east", "south-west", "north-east", "north-west"]
    var base_path = "res://Assets/Sprites/Characters/Protagonist/"
    
    # Remove default animation
    if frames.has_animation("default"):
        frames.remove_animation("default")

    for d in dirs:
        var tex_path = base_path + "protagonist_" + d + ".png"
        var tex = ResourceLoader.load(tex_path)
        if not tex:
            print("Failed to load: ", tex_path)
            continue
            
        # We assume each direction has 8 frames in a horizontal strip (48x48 each)
        var anim_idle = "idle_" + d
        var anim_walk = "walk_" + d
        frames.add_animation(anim_idle)
        frames.add_animation(anim_walk)
        frames.set_animation_loop(anim_idle, true)
        frames.set_animation_loop(anim_walk, true)
        frames.set_animation_speed(anim_idle, 8.0)
        frames.set_animation_speed(anim_walk, 8.0)
        
        # Frames 0-3 (idle)
        for i in range(4):
            var atlas = AtlasTexture.new()
            atlas.atlas = tex
            atlas.region = Rect2(i * 48, 0, 48, 48)
            frames.add_frame(anim_idle, atlas, 1.0, i)
            
        # Frames 4-7 (walk)
        for i in range(4):
            var atlas = AtlasTexture.new()
            atlas.atlas = tex
            atlas.region = Rect2((i + 4) * 48, 0, 48, 48)
            frames.add_frame(anim_walk, atlas, 1.0, i)

    ResourceSaver.save(frames, "D:/GodotProjects/Lentera-Pudar/Assets/Sprites/Characters/Protagonist/protagonist.tres")
    print("SpriteFrames generated successfully via Godot API!")
    quit()

extends SceneTree

const DIRECTIONS: Array[String] = [
	"south",
	"north",
	"east",
	"west",
	"south-east",
	"south-west",
	"north-east",
	"north-west"
]

const FRAME_WIDTH: int = 48
const FRAME_HEIGHT: int = 48

func _init() -> void:
	print("--- Generating Full Kaelen V2 SpriteFrames Resource ---")
	
	var sprite_frames := SpriteFrames.new()
	if sprite_frames.has_animation("default"):
		sprite_frames.remove_animation("default")
		
	var out_dir := "res://Assets/Sprites/Characters/Protagonist"
	var total_anims := 0
	
	for dir_name in DIRECTIONS:
		var json_path := "%s/protagonist_%s.json" % [out_dir, dir_name]
		var png_path := "%s/protagonist_%s.png" % [out_dir, dir_name]
		
		if not FileAccess.file_exists(json_path) or not FileAccess.file_exists(png_path):
			push_error("Missing files for direction: " + dir_name)
			continue
			
		var texture: Texture2D = load(png_path)
		if not texture:
			push_error("Failed to load texture: " + png_path)
			continue
			
		var file := FileAccess.open(json_path, FileAccess.READ)
		var json_text := file.get_as_text()
		file.close()
		
		var json := JSON.new()
		var parse_res := json.parse(json_text)
		if parse_res != OK:
			push_error("Failed to parse JSON: " + json_path)
			continue
			
		var data: Dictionary = json.data
		var meta: Dictionary = data.get("meta", {})
		var tags: Array = meta.get("frameTags", [])
		
		for tag in tags:
			var tag_name: String = tag.get("name", "")
			var from_idx: int = int(tag.get("from", 0))
			var to_idx: int = int(tag.get("to", 0))
			var fps: float = float(tag.get("fps", 8.0))
			var loop: bool = bool(tag.get("loop", true))
			
			var full_anim_name := "%s_%s" % [tag_name, dir_name]
			
			if not sprite_frames.has_animation(full_anim_name):
				sprite_frames.add_animation(full_anim_name)
				
			sprite_frames.set_animation_speed(full_anim_name, fps)
			sprite_frames.set_animation_loop(full_anim_name, loop)
			
			# Add AtlasTexture for each frame in the range
			for idx in range(from_idx, to_idx + 1):
				var atlas := AtlasTexture.new()
				atlas.atlas = texture
				atlas.region = Rect2(idx * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT)
				atlas.filter_clip = true
				sprite_frames.add_frame(full_anim_name, atlas)
				
			total_anims += 1
			print("Created animation: %s (%d frames, %.1f FPS, loop=%s)" % [full_anim_name, (to_idx - from_idx + 1), fps, str(loop)])

	var save_path := "%s/protagonist.tres" % out_dir
	var save_res := ResourceSaver.save(sprite_frames, save_path)
	if save_res == OK:
		print("SUCCESS: Saved SpriteFrames with %d animations to %s" % [total_anims, save_path])
	else:
		push_error("ERROR: Failed to save SpriteFrames resource, error code: %d" % save_res)
		
	quit(0)

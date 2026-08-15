extends Node2D

@onready var player = $Player

func _ready() -> void:
	print("TestDungeonPlayable ready with Native 2D Master Kaelen.")

var _frame_count: int = 0

func _process(_delta: float) -> void:
	_frame_count += 1
	if _frame_count == 10:
		var root_vp: Viewport = get_viewport()
		if root_vp != null:
			var tex: Texture2D = root_vp.get_texture()
			if tex != null:
				var img: Image = tex.get_image()
				if img != null:
					var out_res = ProjectSettings.globalize_path("res://qc_in_game_dungeon_showcase.png")
					var out_art = "C:/Users/ADIT/.gemini/antigravity-ide/brain/a2da4a95-9af8-46dc-9bec-041d1bb1c0dd/qc_in_game_dungeon_showcase.png"
					img.save_png(out_res)
					img.save_png(out_art)
					print("IN_GAME_DUNGEON_SHOWCASE_SAVED:", out_art)
		get_tree().quit()

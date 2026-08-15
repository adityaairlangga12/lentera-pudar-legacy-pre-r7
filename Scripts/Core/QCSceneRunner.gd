extends Node2D

var _frames: int = 0

func _process(_delta: float) -> void:
	_frames += 1
	if _frames >= 30:
		var vp: Viewport = get_viewport()
		if vp != null:
			var tex: Texture2D = vp.get_texture()
			if tex != null:
				var img: Image = tex.get_image()
				if img != null:
					var p1 = ProjectSettings.globalize_path("res://qc_test_pixelation.png")
					var p2 = "C:/Users/ADIT/.gemini/antigravity-ide/brain/a2da4a95-9af8-46dc-9bec-041d1bb1c0dd/qc_test_pixelation.png"
					img.save_png(p1)
					img.save_png(p2)
					print("QC_SAVED_TO:", p1)
					print("QC_SAVED_TO:", p2)
		get_tree().quit()

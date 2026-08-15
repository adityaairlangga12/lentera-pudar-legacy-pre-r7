extends SceneTree

var frame_count: int = 0

func _process(_delta: float) -> bool:
	frame_count += 1
	if frame_count >= 20:
		var vp = root.get_viewport()
		if vp:
			var tex = vp.get_texture()
			if tex:
				var img = tex.get_image()
				if img:
					img.save_png("res://qc_test_pixelation.png")
					print("QC_SCREENSHOT_SAVED:res://qc_test_pixelation.png")
		quit()
		return true
	return false

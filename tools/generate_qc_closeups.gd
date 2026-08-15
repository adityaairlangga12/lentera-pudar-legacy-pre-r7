extends SceneTree

var frame_count: int = 0

func _process(_delta: float) -> bool:
	frame_count += 1
	var root_scene = root.get_node_or_null("TestKaelenV3")
	if root_scene == null:
		return false
			
	var cam: Camera3D = root_scene.get_node("SubViewportContainer/SubViewport/World3D/Camera3D")
	var model: Node3D = root_scene.get_node("SubViewportContainer/SubViewport/World3D/KaelenV3Model")
	var vp: SubViewport = root_scene.get_node("SubViewportContainer/SubViewport")
	
	if frame_count == 5:
		# Close-up 1: Face & Eyepatch
		model.rotation_degrees.y = 0.0
		cam.position = Vector3(0, 1.42, 1.2)
		cam.size = 0.8
	elif frame_count == 10:
		_save_vp(vp, "res://qc_kaelen_closeup_face.png", "C:/Users/ADIT/.gemini/antigravity-ide/brain/a2da4a95-9af8-46dc-9bec-041d1bb1c0dd/qc_kaelen_closeup_face.png")
		# Close-up 2: Cursed Frost Arm (West 270°)
		model.rotation_degrees.y = 90.0
		cam.position = Vector3(-0.32, 0.90, 1.2)
		cam.size = 0.9
	elif frame_count == 18:
		_save_vp(vp, "res://qc_kaelen_closeup_frostarm.png", "C:/Users/ADIT/.gemini/antigravity-ide/brain/a2da4a95-9af8-46dc-9bec-041d1bb1c0dd/qc_kaelen_closeup_frostarm.png")
		# Close-up 3: Scarf & Back Tail (North 180°)
		model.rotation_degrees.y = 180.0
		cam.position = Vector3(-0.06, 0.90, 1.4)
		cam.size = 1.1
	elif frame_count == 26:
		_save_vp(vp, "res://qc_kaelen_closeup_scarf.png", "C:/Users/ADIT/.gemini/antigravity-ide/brain/a2da4a95-9af8-46dc-9bec-041d1bb1c0dd/qc_kaelen_closeup_scarf.png")
		quit()
		return true
	return false

func _save_vp(vp: SubViewport, p_res: String, p_art: String) -> void:
	var tex = vp.get_texture()
	if tex:
		var img = tex.get_image()
		if img:
			img.save_png(ProjectSettings.globalize_path(p_res))
			img.save_png(p_art)
			print("SAVED_CLOSEUP:", p_res)

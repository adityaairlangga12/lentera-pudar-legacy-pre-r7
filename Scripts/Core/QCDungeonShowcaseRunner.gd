extends Node2D

@onready var player = $Player

func _ready() -> void:
	# Apply spatial cel shader to the player's 3D model inside the viewport
	if player != null:
		var model = player.get_node_or_null("SubViewportContainer/SubViewport/World3D/KaelenV3Model")
		if model != null:
			_apply_cel_shader(model)

func _apply_cel_shader(node: Node) -> void:
	if node is MeshInstance3D:
		var mi: MeshInstance3D = node as MeshInstance3D
		var count: int = 1
		if mi.mesh != null:
			count = mi.mesh.get_surface_count()
		for i in range(count):
			var orig = mi.get_active_material(i)
			var cel_mat = ShaderMaterial.new()
			cel_mat.shader = preload("res://Shaders/CelShader.gdshader")
			if orig is StandardMaterial3D:
				var std: StandardMaterial3D = orig as StandardMaterial3D
				cel_mat.set_shader_parameter("albedo_color", std.albedo_color)
				if std.albedo_texture != null:
					cel_mat.set_shader_parameter("albedo_texture", std.albedo_texture)
					cel_mat.set_shader_parameter("use_texture", true)
			mi.set_surface_override_material(i, cel_mat)
			
	for c in node.get_children():
		_apply_cel_shader(c)

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

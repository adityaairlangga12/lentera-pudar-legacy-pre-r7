@tool
extends SceneTree

func _init() -> void:
	print("--- Building TestPixelationPipeline.tscn ---")
	
	# Root Node2D
	var root = Node2D.new()
	root.name = "TestPixelationPipeline"
	
	# Background ColorRect for visual contrast (Dark Neutral #1A1310)
	var bg = ColorRect.new()
	bg.name = "Background"
	bg.color = Color("#1A1310")
	bg.size = Vector2(480, 270)
	root.add_child(bg)
	bg.owner = root
	
	# SubViewportContainer
	var container = SubViewportContainer.new()
	container.name = "SubViewportContainer"
	container.texture_filter = CanvasItem.TEXTURE_FILTER_NEAREST
	container.stretch = false
	container.position = Vector2(80, 45) # Centered in 480x270 viewport
	root.add_child(container)
	container.owner = root
	
	# SubViewport
	var viewport = SubViewport.new()
	viewport.name = "SubViewport"
	viewport.size = Vector2i(320, 180)
	viewport.transparent_bg = true
	viewport.render_target_update_mode = SubViewport.UPDATE_ALWAYS
	container.add_child(viewport)
	viewport.owner = root
	
	# World3D elements
	var world_root = Node3D.new()
	world_root.name = "World3D"
	viewport.add_child(world_root)
	world_root.owner = root
	
	# Camera3D Orthogonal
	var cam = Camera3D.new()
	cam.name = "Camera3D"
	cam.projection = Camera3D.PROJECTION_ORTHOGONAL
	cam.size = 2.4
	cam.position = Vector3(0.0, 1.0, 3.8)
	cam.rotation_degrees = Vector3(-25.0, 0.0, 0.0)
	cam.current = true
	world_root.add_child(cam)
	cam.owner = root
	
	# DirectionalLight3D
	var light = DirectionalLight3D.new()
	light.name = "DirectionalLight3D"
	light.position = Vector3(-2.0, 4.0, 3.0)
	light.rotation_degrees = Vector3(-45.0, -30.0, 0.0)
	light.light_energy = 1.2
	world_root.add_child(light)
	light.owner = root
	
	# Instantiate glTF Model
	var gltf_res = load("res://Assets/Models/test_dummy.gltf")
	if gltf_res:
		var dummy_instance = gltf_res.instantiate()
		dummy_instance.name = "TestDummyModel"
		dummy_instance.position = Vector3(0.0, 0.0, 0.0)
		world_root.add_child(dummy_instance)
		dummy_instance.owner = root
		print("Model test_dummy.gltf instantiated successfully.")
	else:
		printerr("Failed to load res://Assets/Models/test_dummy.gltf")
		
	# Pack and save scene
	var packed = PackedScene.new()
	var pack_err = packed.pack(root)
	if pack_err == OK:
		var save_err = ResourceSaver.save(packed, "res://Scenes/TestPixelationPipeline.tscn")
		if save_err == OK:
			print("SUCCESS: Saved res://Scenes/TestPixelationPipeline.tscn")
		else:
			printerr("Failed to save scene: ", save_err)
	else:
		printerr("Failed to pack scene: ", pack_err)
		
	quit()

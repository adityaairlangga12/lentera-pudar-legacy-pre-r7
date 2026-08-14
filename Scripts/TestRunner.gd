extends Node

@onready var world = $World
@onready var player = $World/Player

func _ready() -> void:
	print("--- TEST RUNNER: Capturing Kaelen V2 Retouched In-Game Visual QC ---")
	
	player.position = Vector2(240, 135)
	player.anim.play("idle_south")
	
	for i in range(10):
		await get_tree().process_frame
		
	await RenderingServer.frame_post_draw
	
	var img: Image = get_viewport().get_texture().get_image()
	var path: String = "C:/Users/ADIT/.gemini/antigravity-ide/brain/c041710e-3c46-44a8-a7aa-c1ee7f5420bf/godot_kaelen_v2_retouched_qc.png"
	var err := img.save_png(path)
	
	if err == OK:
		print("TEST_RUNNER: Retouched visual test artifact saved to " + path)
	else:
		push_error("TEST_RUNNER: Failed to save screenshot. Error code: %d" % err)
		
	get_tree().quit(0)

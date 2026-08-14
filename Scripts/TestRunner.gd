extends Node

@onready var world = $World
@onready var player = $World/Player

func _ready() -> void:
	print("--- TEST RUNNER: Capturing Kaelen V2 Combat QC ---")
	
	player.position = Vector2(240, 135)
	player.anim.play("attack_cursed_south")
	
	# Tunggu ke frame tengah serangan
	for i in range(12):
		await get_tree().process_frame
		
	await RenderingServer.frame_post_draw
	
	var img: Image = get_viewport().get_texture().get_image()
	var path: String = "C:/Users/ADIT/.gemini/antigravity-ide/brain/c041710e-3c46-44a8-a7aa-c1ee7f5420bf/godot_kaelen_v2_attack_qc.png"
	var err := img.save_png(path)
	
	if err == OK:
		print("TEST_RUNNER: Attack QC PNG artifact successfully saved to " + path)
	else:
		push_error("TEST_RUNNER: Failed to save screenshot. Error code: %d" % err)
		
	get_tree().quit(0)

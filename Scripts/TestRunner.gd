extends Node

@onready var world = $World
@onready var player = $World/Player

func _ready() -> void:
	print("=== GODOT RUNTIME HARNESS INITIALIZED ===")
	player.position = Vector2(240, 135)
	
	for i in range(10):
		await get_tree().process_frame
	await RenderingServer.frame_post_draw
	
	print("Ready for next workflow.")
	get_tree().quit(0)

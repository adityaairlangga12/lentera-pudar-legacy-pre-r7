@tool
extends EditorPlugin

var bridge_server: Node = null

func _enter_tree() -> void:
	print("[Lentera Godot Bridge] Activating plugin...")
	var script = load("res://addons/lentera_bridge/bridge_client.gd")
	if script:
		bridge_server = script.new()
		bridge_server.name = "LenteraBridgeClient"
		add_child(bridge_server)

func _exit_tree() -> void:
	print("[Lentera Godot Bridge] Deactivating plugin...")
	if bridge_server:
		bridge_server.queue_free()
		bridge_server = null

@tool
extends EditorPlugin

var bridge_server = null

func _enter_tree():
	print("Lentera Godot Bridge: Activating...")
	bridge_server = load("res://addons/lentera_bridge/bridge_client.gd").new()
	bridge_server.name = "LenteraBridgeClient"
	# Instead of add_child, we just want to run it. Or add to EditorInterface base control.
	var base_control = get_editor_interface().get_base_control()
	base_control.add_child(bridge_server)

func _exit_tree():
	print("Lentera Godot Bridge: Deactivating...")
	if bridge_server:
		bridge_server.queue_free()
		bridge_server = null

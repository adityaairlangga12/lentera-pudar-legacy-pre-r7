@tool
extends Node

# Connects to Node.js MCP server WebSocket
var _client = WebSocketPeer.new()
var _ws_port = 8098
var _connected = false
var _poll_timer: Timer

func _ready():
	_poll_timer = Timer.new()
	_poll_timer.wait_time = 0.1
	_poll_timer.autostart = true
	_poll_timer.timeout.connect(_on_poll_timer_timeout)
	add_child(_poll_timer)
	connect_to_mcp()

func _on_poll_timer_timeout():
	_client.poll()
	var state = _client.get_ready_state()
	
	if state == WebSocketPeer.STATE_OPEN:
		if not _connected:
			print("Lentera Godot Bridge: Connected to MCP Server on port ", _ws_port)
			_connected = true
		while _client.get_available_packet_count():
			var pkt = _client.get_packet()
			_handle_message(pkt.get_string_from_utf8())
	elif state == WebSocketPeer.STATE_CLOSED:
		if _connected:
			print("Lentera Godot Bridge: Disconnected from MCP Server.")
			_connected = false
		
		# Try reconnect continuously
		_poll_timer.stop()
		await get_tree().create_timer(3.0).timeout
		connect_to_mcp()
		_poll_timer.start()

func connect_to_mcp():
	var url = "ws://127.0.0.1:%d" % _ws_port
	print("Lentera Godot Bridge: Attempting to connect to ", url)
	var err = _client.connect_to_url(url)
	if err != OK:
		print("Lentera Godot Bridge: Failed to connect to MCP. Error code: ", err)

func _handle_message(msg_str: String):
	var json = JSON.new()
	if json.parse(msg_str) != OK:
		return
	var msg = json.data
	if not msg.has("id") or not msg.has("command"):
		return
		
	var cmd = msg.command
	var params = msg.get("params", {})
	
	# Dispatch command (Simplified for this bridge client)
	var result = null
	var err_msg = null
	
	if cmd == "get_scene_tree":
		var ei = EditorInterface
		if ei and ei.get_edited_scene_root():
			result = _serialize_node(ei.get_edited_scene_root())
		else:
			err_msg = "No scene open in editor."
	elif cmd == "get_physics_layers":
		result = {}
		for i in range(1, 33):
			var prop = "layer_names/2d_physics/layer_%d" % i
			if ProjectSettings.has_setting(prop):
				result["layer_%d" % i] = ProjectSettings.get_setting(prop)
	elif cmd == "run_gdscript":
		var script_code = params.get("script", "")
		var script = GDScript.new()
		script.source_code = script_code
		var err = script.reload()
		if err == OK:
			var obj = script.new()
			if obj.has_method("run"):
				result = obj.run()
			else:
				err_msg = "Script must have a 'func run():' method."
		else:
			err_msg = "Failed to compile script. Error code: " + str(err)
	# ... (implement other commands) ...
	else:
		err_msg = "Command not yet implemented in GDScript bridge: " + cmd
		
	_send_response(msg.id, result, err_msg)

func _send_response(id: String, result, err_msg):
	var response = {"id": id}
	if err_msg:
		response["error"] = err_msg
	else:
		response["result"] = result
	_client.put_packet(JSON.stringify(response).to_utf8_buffer())

func _serialize_node(node: Node) -> Dictionary:
	var d = {
		"name": node.name,
		"class": node.get_class(),
		"children": []
	}
	for child in node.get_children():
		d.children.append(_serialize_node(child))
	return d

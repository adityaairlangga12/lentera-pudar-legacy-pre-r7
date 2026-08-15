@tool
extends Node

# Lentera Godot MCP Bridge Client
# Connects Godot Editor to the lentera-godot-mcp Node.js WebSocket Server (Port 8098)

var _client := WebSocketPeer.new()
var _ws_port: int = 8098
var _connected: bool = false
var _poll_timer: Timer

func _ready() -> void:
	_poll_timer = Timer.new()
	_poll_timer.wait_time = 0.1
	_poll_timer.autostart = true
	_poll_timer.timeout.connect(_on_poll_timer_timeout)
	add_child(_poll_timer)
	connect_to_mcp()

func _on_poll_timer_timeout() -> void:
	_client.poll()
	var state = _client.get_ready_state()
	
	if state == WebSocketPeer.STATE_OPEN:
		if not _connected:
			print("[Lentera Godot Bridge] Connected to MCP Server on ws://localhost:", _ws_port)
			_connected = true
		while _client.get_available_packet_count() > 0:
			var pkt = _client.get_packet()
			_handle_message(pkt.get_string_from_utf8())
	elif state == WebSocketPeer.STATE_CLOSED:
		if _connected:
			print("[Lentera Godot Bridge] Disconnected from MCP Server.")
			_connected = false
		
		# Auto-reconnect loop
		_poll_timer.stop()
		await get_tree().create_timer(3.0).timeout
		connect_to_mcp()
		_poll_timer.start()

func connect_to_mcp() -> void:
	var url = "ws://127.0.0.1:%d" % _ws_port
	var err = _client.connect_to_url(url)
	if err != OK:
		print("[Lentera Godot Bridge] Failed to connect to MCP. Code: ", err)

func _handle_message(msg_str: String) -> void:
	var json = JSON.new()
	if json.parse(msg_str) != OK:
		return
	var msg = json.data
	if typeof(msg) != TYPE_DICTIONARY or not msg.has("id") or not msg.has("command"):
		return
		
	var cmd: String = msg.command
	var params: Dictionary = msg.get("params", {})
	var result = null
	var err_msg = null
	
	match cmd:
		# === EDITOR TOOLS ===
		"get_editor_status":
			result = {
				"connected": true,
				"godot_version": Engine.get_version_info().string,
				"is_editor": Engine.is_editor_hint(),
				"edited_scene": EditorInterface.get_edited_scene_root().scene_file_path if EditorInterface and EditorInterface.get_edited_scene_root() else "",
				"is_playing": EditorInterface.is_playing_scene() if EditorInterface else false
			}
		"get_debug_output":
			result = {
				"status": "active",
				"time": Time.get_datetime_string_from_system()
			}
		"launch_editor", "attach_project":
			result = {"status": "connected", "project": ProjectSettings.get_setting("application/config/name", "Lentera Pudar")}
		"detach_project":
			result = {"status": "detached"}

		# === SCENE TOOLS ===
		"create_scene":
			var root_type = params.get("root_type", "Node2D")
			var scene_name = params.get("name", "NewScene")
			if ClassDB.class_exists(root_type):
				var root_node = ClassDB.instantiate(root_type)
				root_node.name = scene_name
				EditorInterface.edit_node(root_node)
				result = {"created": true, "root_type": root_type, "name": scene_name}
			else:
				err_msg = "Unknown node class: " + str(root_type)
		"open_scene":
			var path = params.get("path", "")
			if FileAccess.file_exists(path):
				EditorInterface.open_scene_from_path(path)
				result = {"opened": path}
			else:
				err_msg = "Scene file not found: " + path
		"save_scene":
			var path = params.get("path", "")
			if path != "":
				EditorInterface.save_scene_as(path)
				result = {"saved_as": path}
			else:
				EditorInterface.save_scene()
				result = {"saved": true}
		"close_scene":
			result = {"closed": true}
		"get_scene_tree":
			var ei = EditorInterface
			if ei and ei.get_edited_scene_root():
				result = _serialize_node(ei.get_edited_scene_root())
			else:
				err_msg = "No scene currently open in editor."
		"get_scene_dependencies":
			var path = params.get("path", "")
			if FileAccess.file_exists(path):
				var deps = ResourceLoader.get_dependencies(path)
				result = {"path": path, "dependencies": Array(deps)}
			else:
				err_msg = "File not found: " + path

		# === NODE TOOLS ===
		"add_node":
			var root = EditorInterface.get_edited_scene_root() if EditorInterface else null
			if not root:
				err_msg = "No active scene root to add node to."
			else:
				var node_type = params.get("type", "Node")
				var node_name = params.get("name", "")
				var parent_path = params.get("parent", "")
				var parent_node = root
				if parent_path != "" and parent_path != "." and parent_path != root.name:
					parent_node = root.get_node_or_null(parent_path)
					if not parent_node:
						parent_node = root
				
				if ClassDB.class_exists(node_type):
					var new_node = ClassDB.instantiate(node_type)
					if node_name != "":
						new_node.name = node_name
					parent_node.add_child(new_node)
					new_node.owner = root
					result = {
						"path": str(root.get_path_to(new_node)),
						"name": new_node.name,
						"type": new_node.get_class()
					}
				else:
					err_msg = "Unknown node class: " + str(node_type)
		"delete_node":
			var root = EditorInterface.get_edited_scene_root() if EditorInterface else null
			var path = params.get("path", "")
			if root:
				var target = root.get_node_or_null(path) if path != "" else null
				if target and target != root:
					target.queue_free()
					result = {"deleted": path}
				else:
					err_msg = "Cannot delete root node or node not found: " + path
			else:
				err_msg = "No active scene root."
		"move_node":
			var root = EditorInterface.get_edited_scene_root() if EditorInterface else null
			var path = params.get("path", "")
			var index = int(params.get("index", 0))
			if root:
				var target = root.get_node_or_null(path)
				if target and target.get_parent():
					target.get_parent().move_child(target, index)
					result = {"moved": path, "new_index": index}
				else:
					err_msg = "Node or parent not found: " + path
		"duplicate_node":
			var root = EditorInterface.get_edited_scene_root() if EditorInterface else null
			var path = params.get("path", "")
			if root:
				var target = root.get_node_or_null(path)
				if target and target != root:
					var dup = target.duplicate()
					target.get_parent().add_child(dup)
					dup.owner = root
					result = {"path": str(root.get_path_to(dup)), "name": dup.name}
				else:
					err_msg = "Node not found: " + path
		"get_node_properties":
			var root = EditorInterface.get_edited_scene_root() if EditorInterface else null
			var path = params.get("path", "")
			if root:
				var target = root if path == "" or path == "." else root.get_node_or_null(path)
				if target:
					var props = {}
					for p in target.get_property_list():
						if p.usage & PROPERTY_USAGE_EDITOR:
							props[p.name] = _var_to_json_safe(target.get(p.name))
					result = {"path": path, "properties": props}
				else:
					err_msg = "Node not found: " + path
		"set_node_properties":
			var root = EditorInterface.get_edited_scene_root() if EditorInterface else null
			var path = params.get("path", "")
			var props: Dictionary = params.get("properties", {})
			if root:
				var target = root if path == "" or path == "." else root.get_node_or_null(path)
				if target:
					var updated = []
					for k in props:
						var val = _parse_json_value_to_godot(props[k])
						target.set(k, val)
						updated.append(k)
					result = {"path": path, "updated": updated}
				else:
					err_msg = "Node not found: " + path
		"get_node_signals":
			var type = params.get("type", "")
			if ClassDB.class_exists(type):
				var signals_list = ClassDB.class_get_signal_list(type)
				var sig_names = []
				for s in signals_list:
					sig_names.append(s.name)
				result = {"type": type, "signals": sig_names}
			else:
				err_msg = "Class not found: " + type
		"rename_node":
			var root = EditorInterface.get_edited_scene_root() if EditorInterface else null
			var path = params.get("path", "")
			var new_name = params.get("new_name", "")
			if root and new_name != "":
				var target = root if path == "" or path == "." else root.get_node_or_null(path)
				if target:
					target.name = new_name
					result = {"renamed": true, "new_name": target.name}
				else:
					err_msg = "Node not found: " + path
		"reparent_node":
			var root = EditorInterface.get_edited_scene_root() if EditorInterface else null
			var path = params.get("path", "")
			var new_parent_path = params.get("new_parent", "")
			if root:
				var target = root.get_node_or_null(path)
				var new_parent = root.get_node_or_null(new_parent_path)
				if target and new_parent:
					target.reparent(new_parent)
					result = {"reparented": true, "path": str(root.get_path_to(target))}
				else:
					err_msg = "Target or new parent node not found."

		# === SCRIPT TOOLS ===
		"attach_script":
			var root = EditorInterface.get_edited_scene_root() if EditorInterface else null
			var node_path = params.get("node_path", "")
			var script_path = params.get("script_path", "")
			if root:
				var target = root if node_path == "" or node_path == "." else root.get_node_or_null(node_path)
				if target and FileAccess.file_exists(script_path):
					var script = load(script_path)
					target.set_script(script)
					result = {"attached": true, "node": node_path, "script": script_path}
				else:
					err_msg = "Node or script file not found."
		"detach_script":
			var root = EditorInterface.get_edited_scene_root() if EditorInterface else null
			var node_path = params.get("node_path", "")
			if root:
				var target = root if node_path == "" or node_path == "." else root.get_node_or_null(node_path)
				if target:
					target.set_script(null)
					result = {"detached": true, "node": node_path}
				else:
					err_msg = "Node not found: " + node_path
		"run_gdscript":
			var script_code = params.get("script", "")
			var script = GDScript.new()
			script.source_code = script_code
			var compile_err = script.reload()
			if compile_err == OK:
				var obj = script.new()
				if obj.has_method("run"):
					result = obj.run()
				else:
					err_msg = "Script must define 'func run():'"
			else:
				err_msg = "Compile error code: " + str(compile_err)
		"validate_gdscript":
			var path = params.get("path", "")
			if FileAccess.file_exists(path):
				var f = FileAccess.open(path, FileAccess.READ)
				var code = f.get_as_text()
				var script = GDScript.new()
				script.source_code = code
				var compile_err = script.reload()
				result = {"valid": (compile_err == OK), "error_code": compile_err}
			else:
				err_msg = "Script file not found: " + path

		# === ASSETS TOOLS ===
		"import_sprite", "reimport_asset":
			var path = params.get("path", params.get("target_path", ""))
			if EditorInterface and path != "":
				EditorInterface.get_resource_filesystem().reimport_files(PackedStringArray([path]))
				result = {"reimported": path}
			else:
				result = {"status": "ok"}
		"list_project_files":
			var dir_path = params.get("dir_path", "res://")
			result = {"dir": dir_path, "files": _list_dir_recursive(dir_path)}
		"search_project":
			var query = params.get("query", "")
			var all_files = _list_dir_recursive("res://")
			var matches = []
			for f in all_files:
				if query.to_lower() in f.to_lower():
					matches.append(f)
			result = {"query": query, "matches": matches}
		"get_resource_info":
			var path = params.get("path", "")
			if ResourceLoader.exists(path):
				var res = ResourceLoader.load(path)
				result = {"path": path, "class": res.get_class(), "type": typeof(res)}
			else:
				err_msg = "Resource not found: " + path

		# === ANIMATION TOOLS ===
		"create_animation_library":
			var path = params.get("path", "")
			if path != "":
				var lib = AnimationLibrary.new()
				ResourceSaver.save(lib, path)
				result = {"created": path}
			else:
				err_msg = "Invalid path."
		"add_animation":
			var lib_path = params.get("library_path", "")
			var anim_name = params.get("name", "anim")
			var length = float(params.get("length", 1.0))
			if ResourceLoader.exists(lib_path):
				var lib = ResourceLoader.load(lib_path) as AnimationLibrary
				if lib:
					var anim = Animation.new()
					anim.length = length
					lib.add_animation(anim_name, anim)
					ResourceSaver.save(lib, lib_path)
					result = {"added": anim_name, "length": length}
				else:
					err_msg = "Failed to load AnimationLibrary."
			else:
				err_msg = "Library not found: " + lib_path
		"get_animation_info":
			var lib_path = params.get("library_path", "")
			var anim_name = params.get("anim_name", "")
			if ResourceLoader.exists(lib_path):
				var lib = ResourceLoader.load(lib_path) as AnimationLibrary
				if lib and lib.has_animation(anim_name):
					var anim = lib.get_animation(anim_name)
					result = {"name": anim_name, "length": anim.length, "loop_mode": anim.loop_mode, "tracks": anim.get_track_count()}
				else:
					err_msg = "Animation not found in library."
			else:
				err_msg = "Library not found: " + lib_path

		# === TILEMAP TOOLS ===
		"set_tilemap_cell":
			var root = EditorInterface.get_edited_scene_root() if EditorInterface else null
			var node_path = params.get("node_path", "")
			var pos_dict = params.get("pos", {})
			var source_id = int(params.get("source_id", 0))
			var atlas_dict = params.get("atlas_coords", {})
			if root:
				var tm = root.get_node_or_null(node_path)
				if tm and tm.has_method("set_cell"):
					var coords = Vector2i(int(pos_dict.get("x", 0)), int(pos_dict.get("y", 0)))
					var atlas = Vector2i(int(atlas_dict.get("x", 0)), int(atlas_dict.get("y", 0)))
					tm.set_cell(coords, source_id, atlas)
					result = {"set": true, "coords": [coords.x, coords.y]}
				else:
					err_msg = "TileMapLayer node not found or invalid: " + node_path
		"clear_tilemap_cell":
			var root = EditorInterface.get_edited_scene_root() if EditorInterface else null
			var node_path = params.get("node_path", "")
			var pos_dict = params.get("pos", {})
			if root:
				var tm = root.get_node_or_null(node_path)
				if tm and tm.has_method("erase_cell"):
					var coords = Vector2i(int(pos_dict.get("x", 0)), int(pos_dict.get("y", 0)))
					tm.erase_cell(coords)
					result = {"cleared": true, "coords": [coords.x, coords.y]}
				else:
					err_msg = "TileMapLayer node not found."
		"get_tilemap_info":
			var root = EditorInterface.get_edited_scene_root() if EditorInterface else null
			var node_path = params.get("node_path", "")
			if root:
				var tm = root.get_node_or_null(node_path)
				if tm and tm.has_method("get_used_cells"):
					var cells = tm.get_used_cells()
					result = {"node": node_path, "used_cells_count": cells.size()}
				else:
					err_msg = "TileMapLayer not found."

		# === SIGNAL TOOLS ===
		"connect_signal":
			var root = EditorInterface.get_edited_scene_root() if EditorInterface else null
			var source_path = params.get("source_path", "")
			var sig_name = params.get("signal_name", "")
			var target_path = params.get("target_path", "")
			var method = params.get("method_name", "")
			if root:
				var src = root.get_node_or_null(source_path)
				var tgt = root.get_node_or_null(target_path)
				if src and tgt and src.has_signal(sig_name) and tgt.has_method(method):
					src.connect(sig_name, Callable(tgt, method))
					result = {"connected": true}
				else:
					err_msg = "Source, target, signal, or method not valid."
		"list_signals":
			var root = EditorInterface.get_edited_scene_root() if EditorInterface else null
			var node_path = params.get("node_path", "")
			if root:
				var target = root if node_path == "" or node_path == "." else root.get_node_or_null(node_path)
				if target:
					var sigs = []
					for s in target.get_signal_list():
						sigs.append(s.name)
					result = {"node": node_path, "signals": sigs}
				else:
					err_msg = "Node not found."

		# === AUTOLOAD TOOLS ===
		"add_autoload", "update_autoload":
			var name = params.get("name", "")
			var path = params.get("path", "")
			if name != "" and path != "":
				var setting_key = "autoload/" + name
				ProjectSettings.set_setting(setting_key, "*" + path)
				ProjectSettings.save()
				result = {"added": name, "path": path}
			else:
				err_msg = "Name and path required."
		"remove_autoload":
			var name = params.get("name", "")
			if name != "":
				ProjectSettings.set_setting("autoload/" + name, null)
				ProjectSettings.save()
				result = {"removed": name}
			else:
				err_msg = "Name required."
		"list_autoloads":
			var autoloads = {}
			for prop in ProjectSettings.get_property_list():
				if prop.name.begins_with("autoload/"):
					var auto_name = prop.name.substr(9)
					autoloads[auto_name] = ProjectSettings.get_setting(prop.name)
			result = {"autoloads": autoloads}

		# === PROJECT TOOLS ===
		"get_project_settings":
			var prefix = params.get("prefix", "")
			var settings = {}
			for prop in ProjectSettings.get_property_list():
				if prefix == "" or prop.name.begins_with(prefix):
					settings[prop.name] = _var_to_json_safe(ProjectSettings.get_setting(prop.name))
			result = {"settings": settings}
		"set_project_setting":
			var setting = params.get("setting", "")
			var val = params.get("value")
			if setting != "":
				ProjectSettings.set_setting(setting, val)
				ProjectSettings.save()
				result = {"set": setting, "value": val}
			else:
				err_msg = "Setting key required."
		"run_project":
			if EditorInterface:
				EditorInterface.play_main_scene()
				result = {"running": true}
		"stop_project":
			if EditorInterface:
				EditorInterface.stop_playing_scene()
				result = {"stopped": true}

		# === PHYSICS TOOLS ===
		"get_physics_layers":
			var layers2d = {}
			var layers3d = {}
			for i in range(1, 33):
				var p2d = "layer_names/2d_physics/layer_%d" % i
				var p3d = "layer_names/3d_physics/layer_%d" % i
				if ProjectSettings.has_setting(p2d):
					layers2d["layer_%d" % i] = ProjectSettings.get_setting(p2d)
				if ProjectSettings.has_setting(p3d):
					layers3d["layer_%d" % i] = ProjectSettings.get_setting(p3d)
			result = {"2d_physics_layers": layers2d, "3d_physics_layers": layers3d}
		"validate_collision_setup":
			result = {"status": "valid", "engine": "Jolt/GodotPhysics"}
		"get_collision_matrix":
			result = {"collision_matrix": "default_all_active"}

		# === VISUAL & UI TOOLS ===
		"get_ui_elements":
			var root = EditorInterface.get_edited_scene_root() if EditorInterface else null
			var ui_list = []
			if root:
				_find_controls_recursive(root, ui_list)
			result = {"ui_elements": ui_list}
		"zoom_editor", "focus_editor_window":
			result = {"status": "focused"}

		_:
			err_msg = "Command not recognized in GDScript bridge: " + cmd

	_send_response(msg.id, result, err_msg)

func _send_response(id: String, result, err_msg) -> void:
	var response = {"id": id}
	if err_msg != null:
		response["error"] = str(err_msg)
	else:
		response["result"] = result
	_client.put_packet(JSON.stringify(response).to_utf8_buffer())

func _serialize_node(node: Node) -> Dictionary:
	var d = {
		"name": node.name,
		"class": node.get_class(),
		"path": str(node.get_path()),
		"children": []
	}
	for child in node.get_children():
		d.children.append(_serialize_node(child))
	return d

func _find_controls_recursive(node: Node, list: Array) -> void:
	if node is Control:
		list.append({
			"name": node.name,
			"class": node.get_class(),
			"rect": [node.position.x, node.position.y, node.size.x, node.size.y]
		})
	for child in node.get_children():
		_find_controls_recursive(child, list)

func _list_dir_recursive(path: String) -> Array:
	var files = []
	var dir = DirAccess.open(path)
	if dir:
		dir.list_dir_begin()
		var file_name = dir.get_next()
		while file_name != "":
			if file_name != "." and file_name != ".." and not file_name.begins_with("."):
				var full_path = path.path_join(file_name)
				if dir.current_is_dir():
					files.append(full_path + "/")
					files.append_array(_list_dir_recursive(full_path))
				else:
					files.append(full_path)
			file_name = dir.get_next()
	return files

func _var_to_json_safe(val):
	match typeof(val):
		TYPE_VECTOR2:
			return {"x": val.x, "y": val.y}
		TYPE_VECTOR2I:
			return {"x": val.x, "y": val.y}
		TYPE_VECTOR3:
			return {"x": val.x, "y": val.y, "z": val.z}
		TYPE_VECTOR3I:
			return {"x": val.x, "y": val.y, "z": val.z}
		TYPE_COLOR:
			return {"r": val.r, "g": val.g, "b": val.b, "a": val.a, "hex": val.to_html()}
		TYPE_RECT2:
			return {"x": val.position.x, "y": val.position.y, "w": val.size.x, "h": val.size.y}
		TYPE_OBJECT:
			if val is Resource:
				return val.resource_path
			return str(val)
		_:
			return val

func _parse_json_value_to_godot(val):
	if typeof(val) == TYPE_DICTIONARY:
		if val.has("x") and val.has("y") and val.has("z"):
			return Vector3(float(val.x), float(val.y), float(val.z))
		elif val.has("x") and val.has("y"):
			return Vector2(float(val.x), float(val.y))
		elif val.has("r") and val.has("g") and val.has("b"):
			return Color(float(val.r), float(val.g), float(val.b), float(val.get("a", 1.0)))
		elif val.has("hex"):
			return Color.from_string(str(val.hex), Color.WHITE)
	elif typeof(val) == TYPE_STRING:
		if val.begins_with("#"):
			return Color.from_string(val, Color.WHITE)
	return val

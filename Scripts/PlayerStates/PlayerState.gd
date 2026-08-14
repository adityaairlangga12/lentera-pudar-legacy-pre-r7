class_name PlayerState
extends State

## Kelas perantara untuk State yang terikat khusus ke entitas Player

var player: Player

func _ready() -> void:
	await owner.ready
	player = owner as Player
	assert(player != null, "PlayerState harus berada di bawah hierarki Player (CharacterBody2D)!")

func get_input_direction() -> Vector2:
	var input_dir: Vector2 = Input.get_vector("move_left", "move_right", "move_up", "move_down")
	if input_dir == Vector2.ZERO:
		input_dir = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
	return input_dir

func update_direction_string(input_dir: Vector2) -> String:
	var dir_str: String = ""
	if input_dir.y < -0.1:
		dir_str += "north"
	elif input_dir.y > 0.1:
		dir_str += "south"
		
	if input_dir.x < -0.1:
		if dir_str != "": dir_str += "-"
		dir_str += "west"
	elif input_dir.x > 0.1:
		if dir_str != "": dir_str += "-"
		dir_str += "east"
		
	if dir_str != "":
		player.last_direction = dir_str
		
	return player.last_direction

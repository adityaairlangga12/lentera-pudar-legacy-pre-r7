class_name DashState
extends PlayerState

## State saat pemain melakukan manuver Dash / Menghindar

@export var dash_speed_multiplier: float = 2.4
@export var dash_duration: float = 0.25
@export var dash_cooldown: float = 0.4

var dash_timer: float = 0.0
var dash_direction: Vector2 = Vector2.ZERO

func enter() -> void:
	player.can_dash = false
	dash_timer = dash_duration
	
	var input_dir: Vector2 = get_input_direction()
	if input_dir != Vector2.ZERO:
		dash_direction = input_dir.normalized()
		update_direction_string(input_dir)
	else:
		dash_direction = _get_vector_from_direction(player.last_direction)
		
	player.anim.play("dash_" + player.last_direction)
	GameEvents.emit_player_dashed(dash_direction)

func exit() -> void:
	_start_cooldown()

func process_physics(delta: float) -> void:
	dash_timer -= delta
	player.velocity = dash_direction * (player.speed * dash_speed_multiplier)
	player.move_and_slide()
	
	if dash_timer <= 0.0:
		var input_dir: Vector2 = get_input_direction()
		if input_dir != Vector2.ZERO:
			state_machine.change_state("walk")
		else:
			state_machine.change_state("idle")

func _start_cooldown() -> void:
	await player.get_tree().create_timer(dash_cooldown).timeout
	player.can_dash = true

func _get_vector_from_direction(dir: String) -> Vector2:
	match dir:
		"north": return Vector2(0, -1)
		"south": return Vector2(0, 1)
		"east": return Vector2(1, 0)
		"west": return Vector2(-1, 0)
		"north-east": return Vector2(1, -1).normalized()
		"north-west": return Vector2(-1, -1).normalized()
		"south-east": return Vector2(1, 1).normalized()
		"south-west": return Vector2(-1, 1).normalized()
		_: return Vector2(0, 1)

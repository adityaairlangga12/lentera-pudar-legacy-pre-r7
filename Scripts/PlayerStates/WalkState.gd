class_name WalkState
extends PlayerState

## State saat pemain bergerak (Walk)

func process_physics(_delta: float) -> void:
	var input_dir: Vector2 = get_input_direction()
	
	if input_dir == Vector2.ZERO:
		state_machine.change_state("idle")
		return
		
	if Input.is_action_just_pressed("dash") and player.can_dash:
		state_machine.change_state("dash")
		return
		
	var dir_name: String = update_direction_string(input_dir)
	player.velocity = input_dir * player.speed
	player.anim.play("walk_" + dir_name)
	player.move_and_slide()
	
	# Pancarkan sinyal pergerakan ke Global Event Bus
	GameEvents.player_moved.emit(player.global_position)

class_name WalkState
extends PlayerState

func enter() -> void:
	player.anim.play("walk_" + player.last_direction)

func process_physics(_delta: float) -> void:
	if Input.is_action_just_pressed("attack_punch"):
		state_machine.change_state("attackpunch")
		return
		
	if Input.is_action_just_pressed("attack_cursed"):
		state_machine.change_state("attackcursed")
		return

	if Input.is_action_just_pressed("dash") and player.can_dash:
		state_machine.change_state("dash")
		return

	var input_dir: Vector2 = get_input_direction()
	if input_dir == Vector2.ZERO:
		state_machine.change_state("idle")
		return

	update_direction_string(input_dir)
	player.velocity = input_dir.normalized() * player.speed
	player.move_and_slide()
	player.anim.play("walk_" + player.last_direction)
	GameEvents.emit_player_moved(player.global_position)

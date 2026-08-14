class_name IdleState
extends PlayerState

func enter() -> void:
	player.velocity = Vector2.ZERO
	player.anim.play("idle_" + player.last_direction)

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
	if input_dir != Vector2.ZERO:
		update_direction_string(input_dir)
		state_machine.change_state("walk")

class_name IdleState
extends PlayerState

## State saat pemain dalam posisi diam (Idle)

func enter() -> void:
	player.velocity = Vector2.ZERO
	player.anim.play("idle_" + player.last_direction)

func process_physics(_delta: float) -> void:
	var input_dir: Vector2 = get_input_direction()
	
	if input_dir != Vector2.ZERO:
		state_machine.change_state("walk")
		return
		
	if Input.is_action_just_pressed("dash") and player.can_dash:
		state_machine.change_state("dash")
		return
		
	player.anim.play("idle_" + player.last_direction)
	player.move_and_slide()

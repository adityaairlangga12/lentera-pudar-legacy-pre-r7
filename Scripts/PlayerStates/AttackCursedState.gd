class_name AttackCursedState
extends PlayerState

@export var attack_duration: float = 0.5
var attack_timer: float = 0.0

func enter() -> void:
	attack_timer = attack_duration
	player.velocity = Vector2.ZERO
	player.anim.play("attack_cursed_" + player.last_direction)
	# Hantaman telapak tangan kutukan memancarkan gelombang es
	GameEvents.emit_player_attacked(25.0, player.last_direction)

func process_physics(delta: float) -> void:
	attack_timer -= delta
	if attack_timer <= 0.0:
		var input_dir: Vector2 = get_input_direction()
		if input_dir != Vector2.ZERO:
			update_direction_string(input_dir)
			state_machine.change_state("walk")
		else:
			state_machine.change_state("idle")

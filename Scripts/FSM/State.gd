class_name State
extends Node

## Kelas dasar untuk setiap State di dalam Finite State Machine (FSM)

var state_machine: StateMachine = null

func enter() -> void:
	pass

func exit() -> void:
	pass

func process_input(_event: InputEvent) -> void:
	pass

func process_frame(_delta: float) -> void:
	pass

func process_physics(_delta: float) -> void:
	pass

class_name StateMachine
extends Node

## Pengendali Finite State Machine (FSM) modular

@export var initial_state: State

var current_state: State
var states: Dictionary = {}

func _ready() -> void:
	# Tunggu sampai seluruh hierarki siap
	await owner.ready
	
	# Daftarkan seluruh State anak
	for child in get_children():
		if child is State:
			states[child.name.to_lower()] = child
			child.state_machine = self
			
	if initial_state:
		change_state(initial_state.name.to_lower())

func _unhandled_input(event: InputEvent) -> void:
	if current_state:
		current_state.process_input(event)

func _process(delta: float) -> void:
	if current_state:
		current_state.process_frame(delta)

func _physics_process(delta: float) -> void:
	if current_state:
		current_state.process_physics(delta)

func change_state(new_state_name: String) -> void:
	var target_state: State = states.get(new_state_name.to_lower())
	if not target_state:
		push_warning("StateMachine: State '%s' tidak ditemukan!" % new_state_name)
		return
		
	if current_state == target_state:
		return
		
	if current_state:
		current_state.exit()
		
	current_state = target_state
	current_state.enter()

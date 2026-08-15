extends CharacterBody2D
class_name PlayerController

@export_group("Locomotion")
@export var speed: float = 140.0
@export var acceleration: float = 800.0
@export var friction: float = 1000.0

@export_group("Visuals")
@onready var model_root: Node3D = $SubViewportContainer/SubViewport/World3D/KaelenV3Model
@onready var scarf_light: PointLight2D = $ScarfLight2D

var _facing_direction: Vector2 = Vector2.DOWN
var _target_angle_y: float = 0.0

func _physics_process(delta: float) -> void:
	var input_vector: Vector2 = Vector2.ZERO
	input_vector.x = Input.get_axis("ui_left", "ui_right")
	input_vector.y = Input.get_axis("ui_up", "ui_down")
	
	if input_vector != Vector2.ZERO:
		input_vector = input_vector.normalized()
		_facing_direction = input_vector
		velocity = velocity.move_toward(input_vector * speed, acceleration * delta)
		_update_model_rotation(input_vector)
	else:
		velocity = velocity.move_toward(Vector2.ZERO, friction * delta)
		
	move_and_slide()

func _update_model_rotation(dir: Vector2) -> void:
	if model_root == null:
		return
		
	# Map 2D direction (X=right, Y=down) to 3D Y-rotation
	# Down (0, 1) -> 0° (South)
	# Right (1, 0) -> -90° (East)
	# Up (0, -1) -> 180° (North)
	# Left (-1, 0) -> 90° (West)
	var angle_rad = atan2(-dir.x, dir.y)
	_target_angle_y = rad_to_deg(angle_rad)
	model_root.rotation_degrees.y = _target_angle_y

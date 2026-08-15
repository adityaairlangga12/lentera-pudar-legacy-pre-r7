extends CharacterBody2D
class_name PlayerController

@export_group("Locomotion")
@export var speed: float = 140.0
@export var acceleration: float = 800.0
@export var friction: float = 1000.0

@export_group("Visuals")
@onready var sprite: Sprite2D = $Sprite2D
@onready var scarf_light: PointLight2D = $ScarfLight2D

enum Direction { SOUTH = 0, NORTH = 1, EAST = 2, WEST = 3 }
var _current_dir: Direction = Direction.SOUTH

func _physics_process(delta: float) -> void:
	var input_vector: Vector2 = Vector2.ZERO
	
	# Support both default ui_* and custom move_* inputs
	input_vector.x = Input.get_axis("move_left", "move_right")
	if input_vector.x == 0.0:
		input_vector.x = Input.get_axis("ui_left", "ui_right")
		
	input_vector.y = Input.get_axis("move_up", "move_down")
	if input_vector.y == 0.0:
		input_vector.y = Input.get_axis("ui_up", "ui_down")
	
	if input_vector != Vector2.ZERO:
		input_vector = input_vector.normalized()
		velocity = velocity.move_toward(input_vector * speed, acceleration * delta)
		_update_sprite_direction(input_vector)
	else:
		velocity = velocity.move_toward(Vector2.ZERO, friction * delta)
		
	move_and_slide()

func _update_sprite_direction(dir: Vector2) -> void:
	if sprite == null:
		return
		
	# Determine cardinal direction from 2D vector
	if abs(dir.x) > abs(dir.y):
		if dir.x > 0:
			_current_dir = Direction.EAST
		else:
			_current_dir = Direction.WEST
	else:
		if dir.y > 0:
			_current_dir = Direction.SOUTH
		else:
			_current_dir = Direction.NORTH
			
	sprite.frame = int(_current_dir)

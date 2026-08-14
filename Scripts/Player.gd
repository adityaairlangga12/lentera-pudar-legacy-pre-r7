class_name Player
extends CharacterBody2D

## Entitas Pengendali Utama Protagonis Lentera Pudar

@export_group("Movement Stats")
@export var speed: float = 120.0

@export_group("Curse & Combat")
@export var max_health: int = 100
@export var current_health: int = 100
@export var curse_level: float = 0.0 # 0.0 s/d 1.0

# Node References
@onready var anim: AnimatedSprite2D = $AnimatedSprite2D
@onready var state_machine: StateMachine = $StateMachine
@onready var scarf_light: PointLight2D = $ScarfLight

# State Variables
var last_direction: String = "south"
var can_dash: bool = true

func _ready() -> void:
	print("Player: Protagonist initialized with State Machine.")

func take_damage(amount: int) -> void:
	current_health = clampi(current_health - amount, 0, max_health)
	GameEvents.player_health_changed.emit(current_health, max_health)
	if current_health <= 0:
		_die()

func update_curse(amount: float) -> void:
	curse_level = clampf(curse_level + amount, 0.0, 1.0)
	GameEvents.player_curse_level_changed.emit(curse_level)

func _die() -> void:
	print("Player: Jiwa telah membeku seutuhnya.")

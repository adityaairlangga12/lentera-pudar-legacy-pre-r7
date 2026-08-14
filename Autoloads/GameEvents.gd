extends Node

## Global Event Bus untuk Lentera Pudar
## Digunakan untuk komunikasi decoupled lintas sistem tanpa get_node langsung.

# Sinyal Pemain & Gameplay
signal player_moved(position: Vector2)
signal player_health_changed(current_hp: int, max_hp: int)
signal player_curse_level_changed(curse_level: float) # 0.0 s/d 1.0

# Sinyal Lingkungan & Dungeon
signal lantern_lit(lantern_id: String, position: Vector2)
signal room_entered(room_name: String)
signal dungeon_state_changed(is_dark: bool)

# Sinyal Interaksi & Dialog
signal interaction_requested(interactable_id: String)
signal dialogue_started(speaker_name: String)
signal dialogue_ended()

func _ready() -> void:
	print("GameEvents: Global Event Bus initialized.")

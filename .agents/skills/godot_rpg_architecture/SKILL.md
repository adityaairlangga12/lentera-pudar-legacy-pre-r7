---
name: godot_rpg_architecture
description: "Standar arsitektur RPG Godot 4.7.1 untuk Finite State Machine (FSM), State-Driven Generic Binding, Circular Input Replay Buffer untuk bos, Custom Resources, dan Global Event Bus."
---

# Godot RPG Architecture & Core Patterns

Skill ini mendefinisikan standar arsitektur kode RPG, pemisahan data logic, dan integrasi FSM yang teruji.

---

## 1. Pola State-Driven Generic Binding
Untuk menghubungkan nilai gameplay/progres ke output visual tanpa spaghetti code:
- **`bind_visual_state_to_flag`**:
  ```gdscript
  func bind_visual_state_to_flag(node: Node, state_val: int, variant_map: Dictionary) -> void:
      if variant_map.has(state_val):
          node.set_variant(variant_map[state_val])
  ```
- **`bind_uniform_to_gamestate`**:
  ```gdscript
  func _on_curse_meter_updated(new_value: float) -> void:
      cursed_hand_material.set_shader_parameter("intensity", clamp(new_value / 100.0, 0.0, 1.0))
  ```

---

## 2. Finite State Machine (FSM) Ber-Typing Statis
Seluruh state karakter mewarisi kelas dasar `State`:
```gdscript
class_name State extends Node

var actor: CharacterBody2D
var state_machine: StateMachine

func enter() -> void:
    pass

func exit() -> void:
    pass

func update(_delta: float) -> void:
    pass

func physics_update(_delta: float) -> void:
    pass
```

### Integrasi Procedural Gait & Keyframe Action:
- Pada state `Idle` dan `Walk`: FSM mengaktifkan update `LocomotionController` (sinusoidal gait + IK).
- Pada state `AttackPunch` dan `AttackCursed`: FSM mematikan locomotion procedural dan memutar animasi pose keyframed satu arah dengan penguncian arah hadap (*Facing Lock*).

---

## 3. Circular Input Replay Buffer (The Hollow Reflection)
Untuk musuh yang meniru gerakan pemain:
```gdscript
class_name ReplayBuffer extends RefCounted

var buffer: Array[Dictionary] = []
var max_size: int = 120 # 2 detik pada 60 FPS

func push_frame(position: Vector2, state: String, facing: Vector2) -> void:
    buffer.append({"pos": position, "state": state, "facing": facing})
    if buffer.size() > max_size:
        buffer.pop_front()

func get_delayed_frame(delay_frames: int) -> Dictionary:
    var idx = max(0, buffer.size() - 1 - delay_frames)
    if idx < buffer.size():
        return buffer[idx]
    return {}
```

---

## 4. Global Event Bus (`GameEvents.gd`)
Seluruh komunikasi lintas domain disalurkan melalui singleton `GameEvents`:
```gdscript
extends Node

# Sinyal Progres Naratif & Altar
signal altar_activated(altar_id: String, total_altars_lit: int)
signal scarf_stage_changed(new_stage: int)

# Sinyal Status Gameplay & Kutukan
signal curse_meter_changed(new_value: float)
signal player_health_changed(current: float, max_val: float)

# Sinyal Lingkungan & Ruangan
signal room_memory_revealed(room_id: String, duration: float)
```

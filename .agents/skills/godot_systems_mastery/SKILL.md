---
name: godot_systems_mastery
description: "Pangkalan Data untuk Sistem Inti (Core Systems) Godot 4.7.1: Save/Load persistent state, Audio Bus Hierarchy & Ducking, dan Unit Testing otomatis via GUT."
---

# Godot 4.7.1 Core Systems & Infrastructure Mastery

Skill ini memastikan sistem backend, manajemen data persisten, audio responsif, dan pengujian logika berjalan stabil tanpa regresi bug.

---

## 1. Sistem Persistensi Save/Load (`SaveManager.gd`)
Variabel yang wajib disimpan antar sesi bermain:
- `total_altars_lit: int` (Menentukan tahap *The Fading Scarf* 1–4).
- `curse_evolution_path: String` (*Lantern* vs *Frost* pada *Dual Evolution Tree*).
- `unlocked_dungeon_sectors: Array[int]`.
- `current_player_stats: Dictionary`.

### Implementasi Protokol Atomic Write (Steam Cloud Compliant):
```gdscript
class_name SaveData extends Resource

@export var total_altars_lit: int = 0
@export var scarf_stage: int = 1
@export var curse_evolution_path: String = "Neutral"
@export var sector_progress: int = 1
@export var player_stats: Dictionary = {}

func save_atomic(slot_id: int = 1) -> Error:
    var save_dir = "user://saves/"
    DirAccess.make_dir_recursive_absolute(save_dir)
    var tmp_path = save_dir + "slot_%d.tmp" % slot_id
    var dat_path = save_dir + "slot_%d.dat" % slot_id
    var bak_path = save_dir + "slot_%d.bak" % slot_id
    
    # 1. Tulis ke file sementara .tmp
    var err = ResourceSaver.save(self, tmp_path)
    if err != OK:
        return err
        
    # 2. Backup file .dat lama ke .bak (jika ada)
    if FileAccess.file_exists(dat_path):
        DirAccess.copy_absolute(dat_path, bak_path)
        
    # 3. Atomic rename dari .tmp ke .dat
    DirAccess.rename_absolute(tmp_path, dat_path)
    return OK

static func load_with_failover(slot_id: int = 1) -> SaveData:
    var save_dir = "user://saves/"
    var dat_path = save_dir + "slot_%d.dat" % slot_id
    var bak_path = save_dir + "slot_%d.bak" % slot_id
    
    # 1. Coba muat file utama .dat
    if ResourceLoader.exists(dat_path):
        var res = ResourceLoader.load(dat_path) as SaveData
        if res != null:
            return res
            
    # 2. Failover recovery: Muat dari berkas cadangan .bak jika .dat korup
    if ResourceLoader.exists(bak_path):
        var backup_res = ResourceLoader.load(bak_path) as SaveData
        if backup_res != null:
            return backup_res
            
    # 3. Return data baru jika belum ada save file
    return SaveData.new()
```

---

## 2. Hirarki Audio Bus & Ducking Otomatis
- **Hirarki Bus**:
  ```text
  Master
    ├── Music (BGM Dungeon & Boss)
    ├── SFX (Pukulan, Langkah, Es Pecah)
    ├── Voice (Bisikan Aina & Boss)
    └── Ambience (Dengung Dingin & Angin Dungeon)
  ```
- **Ducking Naratif Otomatis**:
  Saat dialog penting Aina muncul, bus `Music` dan `SFX` diturunkan secara otomatis:
  ```gdscript
  func apply_dialogue_ducking(is_active: bool) -> void:
      var music_bus_idx = AudioServer.get_bus_index("Music")
      var target_db = -8.0 if is_active else 0.0
      # Interpolasi linear volume dengan tween
      create_tween().tween_method(
          func(val: float): AudioServer.set_bus_volume_db(music_bus_idx, val),
          AudioServer.get_bus_volume_db(music_bus_idx),
          target_db,
          0.25
      )
  ```

---

## 3. Unit Testing Otomatis Menggunakan GUT (Godot Unit Test)
GUT digunakan untuk memvalidasi aturan logika non-visual:
```gdscript
extends GutTest

func test_curse_meter_overflow_triggers_game_over() -> void:
    var player = Player.new()
    player.curse_meter = 99.0
    player.add_curse(2.0)
    assert_true(player.is_frozen_game_over, "Curse Meter >= 100 harus memicu Game Over.")
    player.free()

func test_scarf_stage_updates_with_altar_count() -> void:
    var save = SaveData.new()
    save.total_altars_lit = 3
    assert_eq(save.calculate_scarf_stage(), 2, "3 Altar harus mengubah Syal ke Tahap 2.")
```

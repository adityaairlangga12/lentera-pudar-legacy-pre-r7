extends Node

@onready var world = $World
@onready var player = $World/Player

func _ready():
    # Simulasi pergerakan Player ke kanan bawah agar animasinya berjalan
    player.velocity = Vector2(1, 1).normalized() * player.speed
    player.anim.play("walk_south-east")
    
    # Tunggu 1 detik agar frame render sempurna dan shader menyala
    await get_tree().create_timer(1.0).timeout
    
    # Ambil screenshot
    var img = get_viewport().get_texture().get_image()
    var path = "C:/Users/ADIT/.gemini/antigravity-ide/brain/c041710e-3c46-44a8-a7aa-c1ee7f5420bf/godot_player_visual_test_phase3.webp"
    var err = img.save_webp(path)
    
    if err == OK:
        print("TEST_RUNNER: Screenshot successfully saved to " + path)
    else:
        print("TEST_RUNNER: Failed to save screenshot. Error code: ", err)
        
    # Selesai
    get_tree().quit()

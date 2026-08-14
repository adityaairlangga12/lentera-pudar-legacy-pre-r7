extends CharacterBody2D

@export var speed: float = 120.0
@onready var anim: AnimatedSprite2D = $AnimatedSprite2D

var last_direction: String = "south"

func _physics_process(_delta: float) -> void:
    var input_dir: Vector2 = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    
    if input_dir != Vector2.ZERO:
        velocity = input_dir * speed
        
        # Calculate direction string based on 8-way movement
        var dir_str = ""
        if input_dir.y < -0.1:
            dir_str += "north"
        elif input_dir.y > 0.1:
            dir_str += "south"
            
        if input_dir.x < -0.1:
            if dir_str != "": dir_str += "-"
            dir_str += "west"
        elif input_dir.x > 0.1:
            if dir_str != "": dir_str += "-"
            dir_str += "east"
            
        if dir_str != "":
            last_direction = dir_str
            
        anim.play("walk_" + last_direction)
    else:
        velocity = Vector2.ZERO
        anim.play("idle_" + last_direction)

    move_and_slide()

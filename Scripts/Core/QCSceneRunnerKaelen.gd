extends Node2D

const DIRECTIONS: Array[Dictionary] = [
	{"name": "South (0°)", "rot_y": 0.0},
	{"name": "South-East (45°)", "rot_y": -45.0},
	{"name": "East (90°)", "rot_y": -90.0},
	{"name": "North-East (135°)", "rot_y": -135.0},
	{"name": "North (180°)", "rot_y": 180.0},
	{"name": "North-West (225°)", "rot_y": 135.0},
	{"name": "West (270°)", "rot_y": 90.0},
	{"name": "South-West (315°)", "rot_y": 45.0}
]

var _dir_idx: int = 0
var _frame_in_dir: int = 0
var _captured_images: Array[Image] = []

@onready var _model: Node3D = $SubViewportContainer/SubViewport/World3D/KaelenV3Model
@onready var _viewport: SubViewport = $SubViewportContainer/SubViewport

func _ready() -> void:
	if _model != null:
		_model.rotation_degrees.y = DIRECTIONS[0]["rot_y"]

func _process(_delta: float) -> void:
	if _model == null or _viewport == null:
		return
		
	_frame_in_dir += 1
	
	if _frame_in_dir == 6:
		var tex: Texture2D = _viewport.get_texture()
		if tex != null:
			var img: Image = tex.get_image()
			if img != null:
				# Full-Body Unclipped Frame (110x150 px)
				var center_x: int = _viewport.size.x / 2
				var center_y: int = _viewport.size.y / 2
				var crop_w: int = 110
				var crop_h: int = 150
				var src_rect: Rect2i = Rect2i(center_x - crop_w / 2, center_y - crop_h / 2, crop_w, crop_h)
				var cropped_img: Image = Image.create(crop_w, crop_h, false, Image.FORMAT_RGBA8)
				cropped_img.blit_rect(img, src_rect, Vector2i.ZERO)
				_captured_images.append(cropped_img)
				
				var dir_name = DIRECTIONS[_dir_idx]["name"].split(" ")[0].to_lower()
				var ind_path = "res://qc_kaelen_dir_%s.png" % dir_name
				cropped_img.save_png(ProjectSettings.globalize_path(ind_path))
				print("Captured Kaelen V3 direction: ", DIRECTIONS[_dir_idx]["name"])
				
		_dir_idx += 1
		_frame_in_dir = 0
		
		if _dir_idx < DIRECTIONS.size():
			_model.rotation_degrees.y = DIRECTIONS[_dir_idx]["rot_y"]
		else:
			_create_composite_showcase()
			_create_pixel_magnified_inspection()
			get_tree().quit()

func _create_composite_showcase() -> void:
	if _captured_images.size() < 8:
		return
		
	var padding: int = 12
	var card_w: int = 110
	var card_h: int = 150
	var total_w: int = (card_w + padding) * 8 + padding
	var total_h: int = card_h + padding * 2
	
	var composite: Image = Image.create(total_w, total_h, false, Image.FORMAT_RGBA8)
	composite.fill(Color("#1A1310"))
	
	for i in range(_captured_images.size()):
		var x_pos: int = padding + i * (card_w + padding)
		var y_pos: int = padding
		composite.blit_rect(_captured_images[i], Rect2i(0, 0, card_w, card_h), Vector2i(x_pos, y_pos))
		
	var path_res = ProjectSettings.globalize_path("res://qc_kaelen_v3_8directions.png")
	var path_art = "C:/Users/ADIT/.gemini/antigravity-ide/brain/a2da4a95-9af8-46dc-9bec-041d1bb1c0dd/qc_kaelen_v3_8directions.png"
	composite.save_png(path_res)
	composite.save_png(path_art)
	print("UNCLIPPED FULL-BODY 8-DIRECTION SHOWCASE SAVED TO:", path_res)
	print("UNCLIPPED FULL-BODY 8-DIRECTION SHOWCASE SAVED TO:", path_art)

func _create_pixel_magnified_inspection() -> void:
	if _captured_images.size() < 8:
		return
		
	# Select 3 key views: 0 (South/Front), 6 (West/Frost Arm Side), 4 (North/Back Scarf)
	var key_indices: Array[int] = [0, 6, 4]
	var scale_factor: int = 4
	var base_w: int = 110
	var base_h: int = 150
	var padding: int = 24
	
	var scaled_w: int = base_w * scale_factor
	var scaled_h: int = base_h * scale_factor
	
	var total_w: int = (scaled_w + padding) * 3 + padding
	var total_h: int = scaled_h + padding * 2
	
	var mag_img: Image = Image.create(total_w, total_h, false, Image.FORMAT_RGBA8)
	mag_img.fill(Color("#141013"))
	
	for idx in range(key_indices.size()):
		var src_img: Image = _captured_images[key_indices[idx]]
		var scaled_card: Image = src_img.duplicate()
		scaled_card.resize(scaled_w, scaled_h, Image.INTERPOLATE_NEAREST)
		
		var x_pos: int = padding + idx * (scaled_w + padding)
		var y_pos: int = padding
		mag_img.blit_rect(scaled_card, Rect2i(0, 0, scaled_w, scaled_h), Vector2i(x_pos, y_pos))
		
	var path_mag_res = ProjectSettings.globalize_path("res://qc_kaelen_v3_pixel_inspection.png")
	var path_mag_art = "C:/Users/ADIT/.gemini/antigravity-ide/brain/a2da4a95-9af8-46dc-9bec-041d1bb1c0dd/qc_kaelen_v3_pixel_inspection.png"
	mag_img.save_png(path_mag_res)
	mag_img.save_png(path_mag_art)
	print("4X PIXEL MAGNIFICATION INSPECTION SAVED TO:", path_mag_res)
	print("4X PIXEL MAGNIFICATION INSPECTION SAVED TO:", path_mag_art)

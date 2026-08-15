shader_type canvas_item;

uniform vec4 outline_color : source_color = vec4(0.08, 0.06, 0.07, 1.0);
uniform float outline_thickness : hint_range(0.5, 3.0) = 1.0;
uniform float color_threshold : hint_range(0.01, 1.0) = 0.22;

void fragment() {
	vec2 tex_size = vec2(textureSize(TEXTURE, 0));
	vec2 pixel_size = outline_thickness / tex_size;
	vec4 center = texture(TEXTURE, UV);
	
	vec4 up = texture(TEXTURE, UV + vec2(0.0, -pixel_size.y));
	vec4 down = texture(TEXTURE, UV + vec2(0.0, pixel_size.y));
	vec4 left = texture(TEXTURE, UV + vec2(-pixel_size.x, 0.0));
	vec4 right = texture(TEXTURE, UV + vec2(pixel_size.x, 0.0));
	
	// Diagonal samples for rounded pixel corners
	vec4 up_l = texture(TEXTURE, UV + vec2(-pixel_size.x, -pixel_size.y));
	vec4 up_r = texture(TEXTURE, UV + vec2(pixel_size.x, -pixel_size.y));
	vec4 dn_l = texture(TEXTURE, UV + vec2(-pixel_size.x, pixel_size.y));
	vec4 dn_r = texture(TEXTURE, UV + vec2(pixel_size.x, pixel_size.y));
	
	// Silhouette boundary
	if (center.a < 0.1) {
		float neighbor_max_a = max(max(max(up.a, down.a), max(left.a, right.a)), max(max(up_l.a, up_r.a), max(dn_l.a, dn_r.a)));
		if (neighbor_max_a > 0.5) {
			COLOR = outline_color;
		} else {
			discard;
		}
	} else {
		// Interior crease detection (e.g. hair locks, scarf folds, arm boundary)
		float diff_up = distance(center.rgb, up.rgb);
		float diff_dn = distance(center.rgb, down.rgb);
		float diff_lt = distance(center.rgb, left.rgb);
		float diff_rt = distance(center.rgb, right.rgb);
		float max_diff = max(max(diff_up, diff_dn), max(diff_lt, diff_rt));
		
		if (max_diff > color_threshold && up.a > 0.5 && down.a > 0.5 && left.a > 0.5 && right.a > 0.5) {
			COLOR = vec4(mix(center.rgb * 0.35, outline_color.rgb, 0.5), center.a);
		} else {
			COLOR = center;
		}
	}
}

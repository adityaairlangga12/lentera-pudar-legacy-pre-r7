shader_type canvas_item;

uniform vec4 outline_color : source_color = vec4(0.078, 0.063, 0.075, 1.0); // #141013 Dark Ink
uniform float outline_thickness : hint_range(0.5, 2.0) = 1.0;

void fragment() {
	vec2 tex_size = vec2(textureSize(TEXTURE, 0));
	vec2 pixel_size = outline_thickness / tex_size;
	vec4 center = texture(TEXTURE, UV);
	
	if (center.a < 0.1) {
		// Sample 4 cardinal neighbors and 4 diagonal corners for silhouette outline
		vec4 up = texture(TEXTURE, UV + vec2(0.0, -pixel_size.y));
		vec4 down = texture(TEXTURE, UV + vec2(0.0, pixel_size.y));
		vec4 left = texture(TEXTURE, UV + vec2(-pixel_size.x, 0.0));
		vec4 right = texture(TEXTURE, UV + vec2(pixel_size.x, 0.0));
		
		vec4 up_l = texture(TEXTURE, UV + vec2(-pixel_size.x, -pixel_size.y));
		vec4 up_r = texture(TEXTURE, UV + vec2(pixel_size.x, -pixel_size.y));
		vec4 dn_l = texture(TEXTURE, UV + vec2(-pixel_size.x, pixel_size.y));
		vec4 dn_r = texture(TEXTURE, UV + vec2(pixel_size.x, pixel_size.y));
		
		float max_neighbor_a = max(max(max(up.a, down.a), max(left.a, right.a)), max(max(up_l.a, up_r.a), max(dn_l.a, dn_r.a)));
		
		if (max_neighbor_a > 0.5) {
			COLOR = outline_color;
		} else {
			discard;
		}
	} else {
		// Output the 100% clean, noise-free 3D spatial cel-shaded pixels
		COLOR = center;
	}
}

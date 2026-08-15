shader_type canvas_item;

uniform vec4 outline_color : source_color = vec4(0.08, 0.06, 0.07, 1.0);

// Canonical 16-Color Master Palette (The Triad of Lentera Pudar)
const vec3 PALETTE[16] = vec3[](
	// 1. Hair Palette (Silver-Gray)
	vec3(0.839, 0.839, 0.839), // 0: #D6D6D6 Hair High
	vec3(0.620, 0.620, 0.620), // 1: #9E9E9E Hair Mid
	vec3(0.431, 0.431, 0.431), // 2: #6E6E6E Hair Dark
	
	// 2. Scarf of Aina (2700K Kelvin Warm Yellow)
	vec3(1.000, 0.820, 0.522), // 3: #FFD185 Scarf High
	vec3(0.957, 0.722, 0.376), // 4: #F4B860 Scarf Mid
	vec3(0.780, 0.529, 0.196), // 5: #C78732 Scarf Shadow
	
	// 3. Cursed Frost Arm (6500K Kelvin Cold Shard)
	vec3(0.620, 0.773, 0.910), // 6: #9EC5E8 Frost High
	vec3(0.255, 0.404, 0.620), // 7: #41679E Frost Mid
	vec3(0.145, 0.243, 0.420), // 8: #253E6B Frost Deep
	
	// 4. Skin & Face
	vec3(0.910, 0.698, 0.510), // 9: #E8B282 Skin
	vec3(0.769, 0.541, 0.369), // 10: #C48A5E Skin Shadow
	
	// 5. Wanderer Robe & Leather
	vec3(0.141, 0.114, 0.102), // 11: #241D1A Robe Base
	vec3(0.098, 0.075, 0.063), // 12: #191310 Robe Dark
	vec3(0.431, 0.251, 0.137), // 13: #6E4023 Baldric Leather / Boots
	vec3(0.831, 0.784, 0.737), // 14: #D4C8BC Bandage
	vec3(0.078, 0.063, 0.075)  // 15: #141013 Eyepatch / Outline
);

vec3 snap_to_palette(vec3 col) {
	float min_dist = 1000.0;
	vec3 best_color = col;
	for (int i = 0; i < 16; i++) {
		vec3 diff = col - PALETTE[i];
		// Standard perceptual color distance
		float dist = dot(diff * vec3(0.3, 0.59, 0.11), diff);
		if (dist < min_dist) {
			min_dist = dist;
			best_color = PALETTE[i];
		}
	}
	return best_color;
}

void fragment() {
	vec2 tex_size = vec2(textureSize(TEXTURE, 0));
	vec2 pixel_size = 1.0 / tex_size;
	vec4 center = texture(TEXTURE, UV);
	
	vec4 up = texture(TEXTURE, UV + vec2(0.0, -pixel_size.y));
	vec4 down = texture(TEXTURE, UV + vec2(0.0, pixel_size.y));
	vec4 left = texture(TEXTURE, UV + vec2(-pixel_size.x, 0.0));
	vec4 right = texture(TEXTURE, UV + vec2(pixel_size.x, 0.0));
	
	if (center.a < 0.1) {
		float neighbor_a = max(max(up.a, down.a), max(left.a, right.a));
		if (neighbor_a > 0.5) {
			COLOR = outline_color;
		} else {
			discard;
		}
	} else {
		vec3 snapped = snap_to_palette(center.rgb);
		
		vec3 up_s = snap_to_palette(up.rgb);
		vec3 dn_s = snap_to_palette(down.rgb);
		vec3 lt_s = snap_to_palette(left.rgb);
		vec3 rt_s = snap_to_palette(right.rgb);
		
		float diff = distance(snapped, up_s) + distance(snapped, dn_s) + distance(snapped, lt_s) + distance(snapped, rt_s);
		
		if (diff > 0.85 && up.a > 0.5 && down.a > 0.5 && left.a > 0.5 && right.a > 0.5) {
			COLOR = vec4(mix(snapped * 0.4, outline_color.rgb, 0.5), center.a);
		} else {
			COLOR = vec4(snapped, center.a);
		}
	}
}

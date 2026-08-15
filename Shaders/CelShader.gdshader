shader_type spatial;
render_mode diffuse_toon, specular_disabled, cull_back;

uniform vec4 albedo_color : source_color = vec4(1.0, 1.0, 1.0, 1.0);
uniform sampler2D albedo_texture : source_color, filter_nearest;
uniform bool use_texture = false;

uniform float shadow_threshold : hint_range(0.0, 1.0) = 0.32;
uniform float highlight_threshold : hint_range(0.0, 1.0) = 0.72;

// The Triad Kelvin Color Tints
uniform vec3 cold_shadow_tint : source_color = vec3(0.55, 0.65, 0.85); // 6500K Cold Shard
uniform vec3 warm_highlight_tint : source_color = vec3(1.15, 1.08, 0.95); // 2700K Warm Light

void fragment() {
	vec4 base = albedo_color;
	if (use_texture) {
		vec4 tex = texture(albedo_texture, UV);
		if (tex.a < 0.1) {
			discard;
		}
		base *= tex;
	}
	ALBEDO = base.rgb;
	ROUGHNESS = 1.0;
	METALLIC = 0.0;
}

void light() {
	float NdotL = clamp(dot(NORMAL, LIGHT), 0.0, 1.0);
	float atten = ATTENUATION;
	float light_factor = NdotL * atten;
	
	vec3 step_light;
	if (light_factor > highlight_threshold) {
		step_light = LIGHT_COLOR * warm_highlight_tint * 1.1;
	} else if (light_factor > shadow_threshold) {
		step_light = LIGHT_COLOR * 0.85;
	} else {
		step_light = LIGHT_COLOR * cold_shadow_tint * 0.55;
	}
	
	DIFFUSE_LIGHT += ALBEDO * step_light;
}

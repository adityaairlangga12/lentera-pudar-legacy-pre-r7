shader_type spatial;
render_mode unshaded, cull_back;

uniform sampler2D albedo_texture : source_color, filter_nearest;
uniform vec4 outline_color : source_color = vec4(0.08, 0.06, 0.07, 1.0);
uniform float shadow_threshold : hint_range(0.0, 1.0) = 0.45;

void fragment() {
	vec4 tex = texture(albedo_texture, UV);
	if (tex.a < 0.1) {
		discard;
	}
	ALBEDO = tex.rgb;
	ALPHA = tex.a;
}

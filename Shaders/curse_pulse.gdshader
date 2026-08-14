shader_type canvas_item;
uniform float pulse_speed : hint_range(0.5, 5.0) = 2.0;
uniform float pulse_strength : hint_range(0.0, 1.0) = 0.35;
uniform vec4 curse_color : source_color = vec4(0.29, 0.435, 0.647, 1.0);
void fragment() {
	vec4 original = texture(TEXTURE, UV);
	float is_curse = step(0.28, original.b) * step(original.r, 0.45) * original.a;
	float pulse = 0.5 + 0.5 * sin(TIME * pulse_speed);
	float glow = pulse * pulse_strength * is_curse;
	COLOR = original;
	COLOR.rgb = mix(original.rgb, curse_color.rgb + vec3(0.2), glow * is_curse);
	COLOR.a = original.a;
}
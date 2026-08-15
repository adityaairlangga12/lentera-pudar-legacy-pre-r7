shader_type canvas_item;

uniform vec4 cursed_color : source_color = vec4(0.29, 0.435, 0.647, 1.0); // #4A6FA5
uniform float pulse_speed : hint_range(0.1, 5.0) = 2.5;
uniform float intensity : hint_range(0.0, 1.0) = 0.45;

void fragment() {
    vec4 tex_color = texture(TEXTURE, UV);
    
    // Deteksi warna biru kristal es secara ketat (Chromatic Blue Dominance)
    // Memastikan rambut abu-abu dan pakaian gelap TIDAK PERNAH terpengaruh shader
    bool is_frost_crystal = (tex_color.b > tex_color.r + 0.16 && tex_color.b > tex_color.g + 0.04 && tex_color.a > 0.5);
    
    if (is_frost_crystal) {
        // Efek denyut energi dingin pada tangan kutukan es
        float pulse = (sin(TIME * pulse_speed) + 1.0) * 0.5; // 0.0 to 1.0
        vec3 glow = tex_color.rgb + (vec3(0.2, 0.4, 0.8) * pulse * intensity);
        COLOR = vec4(glow, tex_color.a);
    } else {
        COLOR = tex_color;
    }
}

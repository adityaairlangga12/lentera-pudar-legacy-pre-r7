shader_type canvas_item;

uniform vec4 cursed_color : source_color = vec4(0.29, 0.435, 0.647, 1.0); // #4A6FA5
uniform float pulse_speed : hint_range(0.1, 5.0) = 2.0;
uniform float intensity : hint_range(0.0, 1.0) = 0.5;

void fragment() {
    vec4 tex_color = texture(TEXTURE, UV);
    
    // Deteksi warna biru es (Ice Blue) pada piksel
    // Rentang warna yang difilter agar hanya mengenai Kutukan Pudar
    float dist = distance(tex_color.rgb, cursed_color.rgb);
    
    if (dist < 0.3 && tex_color.a > 0.0) {
        // Buat efek berdenyut (pulse) menggunakan sin
        float pulse = (sin(TIME * pulse_speed) + 1.0) * 0.5; // 0.0 to 1.0
        
        // Pendaran (glow) dengan menambah brightness
        vec3 glow = cursed_color.rgb + (vec3(1.0) * pulse * intensity);
        
        COLOR = vec4(glow, tex_color.a);
    } else {
        COLOR = tex_color;
    }
}

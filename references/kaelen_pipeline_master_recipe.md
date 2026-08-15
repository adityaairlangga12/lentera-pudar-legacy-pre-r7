# Resep Master Pipeline Kaelen (Standar Baku Pembuatan Karakter Jalur B)

> **Dokumen ini adalah cetak biru teknis (Master Recipe) resmi.** Berisi panduan lengkap pemodelan low-poly di Blender 5.2 LTS, hierarki armature rigging, ekspor glTF 2.0, integrasi render SubViewport Pixelation di Godot 4.7.1, hingga setup fisika syal dan shader kutukan live. Gunakan dokumen ini sebagai acuan mutlak untuk Kaelen dan karakter/NPC baru lainnya.

---

## BAB I: SPESIFIKASI ANATOMI & MESH 3D (BLENDER 5.2 LTS)

| Komponen | Spesifikasi Teknis Low-Poly | Palet Warna Baku (The Triad) |
|---|---|---|
| **Poly Count & Scale** | Total 300–1000 triangles (tris). Skala unit proporsional chibi 1:3.2. Shading: **Flat Shading**. | Palet Baku The Triad |
| **Rambut & Kepala** | Massa rambut acak berponi melandai, menutupi dahi dan sebagian mata kanan. | `#E0E0E0`, `#9E9E9E`, `#616161` |
| **Wajah & Mata** | **Mata Kanan**: *Eyepatch* kulit hitam pekat sebagai segel kutukan.<br>**Mata Kiri**: Terbuka tajam dengan bayangan alis di bawah poni.<br>**Kulit**: Nada hangat melankolis. | Eyepatch: `#141013`<br>Kulit: `#FFE0B2`, `#E0A96D`, `#A86F3E` |
| **Syal Jiwa Aina** | Syal api kuning hangat melilit leher dengan juntaian kain panjang di punggung (4–6 segmen bone fleksibel). | `#FFE0B2` (Highlight), `#F4B860` (Base), `#C58B3E` (Shadow), `#8C4E18` (Deep) |
| **Pakaian & Torso** | Jubah kelana gelap tanpa kelas (*class-less*) dengan sabuk selempang kulit melintang (*baldric harness*). | Jubah: `#2A211C`, `#1A1310`<br>Baldric: `#7A4B28`, `#4E2E16` |
| **Lengan Kiri (Kutukan)** | Kristal es beku asimetris dengan urat es tajam menonjol hingga telapak tangan. | `#99B9E0` (Kilau), `#4A6FA5` (Base Es), `#2C4875` (Bayangan) |
| **Lengan Kanan** | Tangan normal dengan perban kelana putih kusam / sarung tangan kulit. | `#D7CCC8`, `#A1887F`, `#6D4C41` |
| **Kaki & Pijakan** | Celana gelap dan boots kelana coklat berbobot (6–8 segmen limb). | Boots: `#5C3A21`, `#3B2212` |

---

## BAB II: HIERARKI ARMATURE & RIGGING (BLENDER ➔ GLTF 2.0)

### 1. Hierarki Bone Anatomis
Rig dibangun mengikuti hierarki biomekanik asli:
```text
Root (Origin Lantai)
  └── Pelvis (Center of Mass)
        ├── Spine ➔ Chest ➔ Neck ➔ Head
        │     ├── Scarf_Base ➔ Scarf_01 ➔ Scarf_02 ➔ Scarf_03 (Chain Syal)
        │     ├── Shoulder.L ➔ UpperArm.L ➔ Forearm.L ➔ Hand.L (Lengan Kutukan)
        │     └── Shoulder.R ➔ UpperArm.R ➔ Forearm.R ➔ Hand.R (Lengan Normal)
        ├── Thigh.L ➔ Shin.L ➔ Foot.L ➔ Toe.L
        └── Thigh.R ➔ Shin.R ➔ Foot.R ➔ Toe.R
```

### 2. Standar Ekspor glTF 2.0
- **Apply All Transforms**: Wajib menjalankan `apply_all_transforms` di Blender sebelum ekspor untuk memastikan posisi, rotasi, dan skala bernilai default ($0,0,0$ dan $1,1,1$).
- **Orientasi Sumbu**: glTF 2.0 menggunakan $+Z$ sebagai forward. Saat diimpor ke Godot (yang menggunakan $-Z$ forward), orientasi diselaraskan pada import preset.
- **Validasi Bone Roll**: Seluruh bone roll diverifikasi simetris dan konsisten agar rotasi tidak terpuntir saat menerima pose IK.

---

## BAB III: INTEGRASI RENDER PIXELATION DI GODOT 4.7.1

### 1. Struktur Scene Karakter (`Player.tscn`)
```text
Player (CharacterBody2D) [z_index = 1]
  ├── ViewportContainer (SubViewportContainer) [stretch = false, filter = Nearest]
  │     └── PixelViewport (SubViewport) [size = (320, 180), transparent_bg = true]
  │           ├── Camera3D (Camera3D) [projection = Orthogonal, size = 3.5, position = (0, 4, 8), rotation_degrees = (-25, 0, 0)]
  │           ├── DirectionalLight3D [shadow_enabled = false, light_energy = 0.9]
  │           └── KaelenModel3D (Node3D)
  │                 └── Skeleton3D (Skeleton3D)
  │                       ├── MeshInstance3D (Kaelen Mesh) [material = CelShader.gdshader]
  │                       └── BoneAttachment3D (Scarf / Hand Nodes)
  ├── CollisionShape2D [position = (0, 8), shape = CircleShape2D(radius: 6)]
  ├── ScarfLight2D (PointLight2D) [position = (0, 2), color = #F4B860, energy = 0.85, kelvin = 2700K]
  ├── FrostParticles2D (GPUParticles2D) [position = (-8, 2), texture = 2x2_pixel.png, color = #99B9E0]
  ├── StateMachine (Node) [FSM: Idle, Walk, Dash, AttackPunch, AttackCursed, Hurt, Death]
  └── GroundShadow (Sprite2D) [texture = shadow_ellipse.png, modulate = rgba(15,12,14,0.6)]
```

### 2. Cel-Shader Pixel Otentik (`CelShader.gdshader`)
```glsl
shader_type spatial;
render_mode unshaded, cull_back;

uniform sampler2D albedo_texture : source_color, filter_nearest;
uniform vec4 outline_color : source_color = vec4(0.08, 0.06, 0.07, 1.0);
uniform float shadow_threshold : hint_range(0.0, 1.0) = 0.45;

void fragment() {
    vec4 tex = texture(albedo_texture, UV);
    ALBEDO = tex.rgb;
    ALPHA = tex.a;
}
```

---

## BAB IV: SISTEM ANIMASI & FISIKA SEKUNDER

### 1. Locomotion Periodik: Sinusoidal Gait Function (`LocomotionController.gd`)
```gdscript
# Frekuensi & phase offset biomekanika berjalan
var phase: float = 0.0
var step_freq: float = 8.5
var stride_amplitude: float = 0.25
var bob_amplitude: float = 0.08

func update_walk_gait(delta: float, is_moving: bool) -> void:
    if is_moving:
        phase += step_freq * delta
        var left_foot_y = sin(phase) * stride_amplitude
        var right_foot_y = sin(phase + PI) * stride_amplitude
        var body_bob_y = abs(sin(phase * 2.0)) * bob_amplitude
        # Apply target ke IK targets kaki & pelvis
```

### 2. Secondary Motion: Spring-Damper Syal Aina (`ScarfPhysics.gd`)
```gdscript
# Hukum Hooke untuk chain bone syal
var scarf_velocity: Vector3 = Vector3.ZERO
var rest_position: Vector3 = Vector3.ZERO
var stiffness: float = 140.0
var damping: float = 12.0

func _physics_process(delta: float) -> void:
    var displacement = current_pos - rest_pos
    var spring_force = -stiffness * displacement - damping * scarf_velocity
    scarf_velocity += spring_force * delta
    current_pos += scarf_velocity * delta
```

---

## BAB V: INTEGRASI GAP-FEATURES & LIVE-DRIVEN HOOKS

1. **Reaktivitas Shader Tangan Kutukan**:
   - Nilai *Curse Meter* pemain ($0.0 \dots 1.0$) disalurkan langsung via event `GameEvents.curse_meter_changed.connect(_on_curse_changed)`.
   - Menyetel uniform parameter `intensity` pada material tangan kiri secara real-time.
2. **The Fading Scarf Variant Swap**:
   - Saat altar diaktifkan, event `GameEvents.altar_activated` memicu pergantian varian mesh/texture syal (Tahap 1 ➔ 2 ➔ 3 ➔ 4) dengan transisi cross-fade 0.25 detik.
3. **Pencahayaan Kelvin**:
   - `ScarfLight2D` memancarkan cahaya hangat 2700K (`#F4B860`). Jika berada di Sektor 4 (Depression), radius `texture_scale` dipotong otomatis menjadi 50%.

---

*Dokumen ini resmi mengesahkan Resep Master Pembuatan Karakter Jalur B Lentera Pudar.*

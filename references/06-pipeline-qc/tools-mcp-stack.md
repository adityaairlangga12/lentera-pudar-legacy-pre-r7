---
status: ACTIVE
type: TOOL_CONTRACT
authority_scope: pipeline.tools_stack
canonical: true
introduced_by: ADR-015
---


# Rantai Tools, MCP Ecosystem & Pipeline Stack — Lentera Pudar
### Standardisasi Rantai Tools 3D Action RPG (Blender 5.2 LTS + Unreal Engine 5)

> **Dokumen Sumber Kebenaran Kanonikal Rantai Tools (*Toolchain & MCP Reference*)**  
> Menetapkan seluruh perangkat lunak, plugin, arsitektur Model Context Protocol (MCP), kontrak kapabilitas 23 Tool Publik Blender 5.2 LTS, model eksekusi normatif `HEADLESS_FILE_BACKED`, dan pipeline otomasi aset 3D untuk semesta *Lentera Pudar*.

---

## 1. Fondasi Engine & Core DCC

| Software | Versi / Tipe | Peran Utama | Catatan Kunci |
|---|---|---|---|
| **Unreal Engine 5** | 5.8 / Modern 5.x | Game Engine Utama (Rendering Lumen, Nanite, Niagara, Chaos Cloth, World Partition). | Target performa solid 60 FPS ($<16.6	ext{ ms}$). |
| **Blender** | 5.2 LTS | DCC Primer untuk Pemodelan 3D, Sculpting, Biomechanical Rigging, Retopology, dan glTF export. | Dieksekusi via `lentera-blender-mcp` (Model `HEADLESS_FILE_BACKED`). |
| **Python** | 3.10+ | Bahasa Scripting Otomasi MCP (Blender `bpy` & UE5 `unreal` module). | Jembatan perintah AI Agent ke engine. |

---

## 2. Arsitektur Model Context Protocol (MCP) & Model Eksekusi

### A. Model Eksekusi Normatif Hardened v1 (`HEADLESS_FILE_BACKED`)
- **Transport Komunikasi**: MCP Stdio Client $\leftrightarrow$ Node.js Server (`lentera-blender-mcp`).
- **Engine Eksekusi**: Subprocess Blender 5.2 LTS headless terisolasi (`blender.exe --background -noaudio`) dipanggil segar (*fresh cold-process*) per pemanggilan perintah.
- **Otoritas Status Kerja (*Working State Authority*)**: File fisik `.blend` di filesystem disk adalah satu-satunya otoritas status kerja persisten yang sah. Tidak ada dependensi session memori antar-pemanggilan.
- **Isolasi Proses**: Setiap kegagalan mutasi atau crash script tertahan di dalam subprocess tanpa mencemari pemanggilan berikutnya.
- **Status WebSocket GUI Bridge**: Berstatus **`DEFERRED / NOT AVAILABLE`** (prototipe sekunder yang ditangguhkan dan tidak menjadi bagian dari rilis Hardened v1 aktif).

### B. Kebenaran Kapabilitas (*Capability Truth*)
Setiap agen wajib mematuhi alur verifikasi kapabilitas:
$$\text{DOCUMENTED} \longrightarrow \text{IMPLEMENTED} \longrightarrow \text{AVAILABLE} \longrightarrow \text{EXECUTED} \longrightarrow \text{VERIFIED}$$
- $	ext{Tool Registration} 
eq 	ext{Implementation} 
eq 	ext{Server Availability} 
eq 	ext{Execution} 
eq 	ext{Verification}$.
- Klaim bahwa tugas selesai HANYA sah jika berstatus **`VERIFIED`** melalui observasi independen terhadap file target fisik.

---

## 3. Matriks Kapabilitas Perkakas Blender MCP (Hardened v1)

Baseline perkakas aktif: **Tepat 23 Tool Publik Terverifikasi** dan **17 Tool Deferred**.

### A. 23 Tool Publik Aktif (Normative Headless Path)

| No | Nama Tool | Kategori | Persyaratan Targeting File | Tujuan Utama | Jalur Verifikasi Independen |
|---|---|---|---|---|---|
| 1 | `open_blend_file` | Scene / File | `path` (file eksis) | Membuka & memeriksa metadata scene `.blend`. | `get_scene_state` |
| 2 | `save_blend_file` | Scene / File | `filepath` | Menyimpan scene ke file `.blend` target. | File inspection di disk |
| 3 | `get_scene_state` | Observasi | `blend_file` (opsional) | Ringkasan objek, mesh, dan material scene. | Read-only observation |
| 4 | `list_objects` | Observasi | `blend_file` (opsional) | Daftar objek + `viewport_visible` & `render_enabled`. | Read-only observation |
| 5 | `get_object_state` | Observasi | `blend_file` + `object` (wajib) | Detail transform, dimensi, hirarki, material slots. | Read-only observation |
| 6 | `get_mesh_stats` | Observasi | `blend_file` + `object` (wajib) | Statistik vertex, face, tris, UV layers, shading. | Read-only observation |
| 7 | `get_armature_state` | Observasi | `blend_file` + `armature` (wajib) | Hirarki tulang, jumlah bone, joint coords, roll (rad). | Read-only observation |
| 8 | `render_viewport_screenshot` | Visual | `blend_file` (opsional) + `output_path` | Render tangkapan visual viewport ke file PNG. | Inspeksi visual PNG di disk |
| 9 | `get_console_output` | Diagnostik | Tanpa target file | Mengambil buffer string log konsol server. | String log inspect |
| 10 | `get_last_error` | Diagnostik | Tanpa target file | Mengambil teks error terakhir yang tertangkap. | Error text inspect |
| 11 | `create_mesh_primitive` | Modeling | `blend_file` / `output_blend_file` | Membuat primitive mesh (`cube`, `cylinder`, `uv_sphere`). | `get_mesh_stats` / `get_object_state` |
| 12 | `apply_modifier` | Modeling | `blend_file` + `object` (wajib) | Menambah & menerapkan modifier (`MIRROR`, `BEVEL`, `DECIMATE`). | `get_mesh_stats` |
| 13 | `set_shading_mode` | Shading | `blend_file` / `output_blend_file` | Mengatur mode shading (`flat` / `smooth`). | `get_mesh_stats` (`smooth_faces`) |
| 14 | `merge_by_distance` | Modeling | `blend_file` + `object` (wajib) | Menggabungkan vertex duplikat dalam threshold. | `get_mesh_stats` (`vertex_count`) |
| 15 | `validate_poly_count` | QC Modeling | `object` + `blend_file` (opsional) | Validasi jumlah triangle terhadap budget `max_tris`. | `get_mesh_stats` |
| 16 | `create_armature` | Rigging | `blend_file` / `output_blend_file` | Membuat objek armature bersih (**0 tulang / zero bones**). | `get_armature_state` (`bone_count: 0`) |
| 17 | `add_bone` | Rigging | `blend_file` + `armature` (wajib) | Menambah tulang dengan head/tail & hirarki parent (`use_connect`). | `get_armature_state` |
| 18 | `set_bone_roll` | Rigging | `blend_file` + `armature` + `bone` | Mengatur sudut roll kanonikal tulang dalam **radian**. | `get_armature_state` (`roll` rad) |
| 19 | `apply_all_transforms` | Rigging / Mesh | `blend_file` / `output_blend_file` | Menerapkan Location, Rotation, Scale sebelum ekspor. | `get_object_state` |
| 20 | `unwrap_uv` | UV Mapping | `blend_file` + `object` (wajib) | UV Unwrapping (`SMART_PROJECT` / `CUBE_PROJECT`). | `get_mesh_stats` / Python inspection |
| 21 | `create_flat_material` | Material | `blend_file` / `output_blend_file` | Membuat material warna dasar Principled BSDF. | `get_object_state` (`material_slots`) |
| 22 | `export_gltf` | Ekspor | `blend_file` + `path` (wajib) | Ekspor scene ke glTF 2.0 (`.glb` / `.gltf`). | `validate_export` + File di disk |
| 23 | `validate_export` | Validasi | `path` (wajib) | Validasi struktural biner header GLB / manifest JSON glTF. | Independent binary validator |

---

### B. 17 Tool Deferred (Tidak Tersedia di Hardened v1)

Seluruh perkakas berikut **DITANGGUHKAN (`DEFERRED`)** dan dilarang dipanggil sebagai perkakas publik:
1. `undo` — *Tidak bermakna pada model headless single-shot.*
2. `redo` — *Tidak bermakna pada model headless single-shot.*
3. `separate_mesh_by_material` — *Ditangguhkan.*
4. `validate_bone_roll_consistency` — *Ditangguhkan.*
5. `auto_weight_paint` — *Ditangguhkan (Fase 4).*
6. `adjust_vertex_weights` — *Ditangguhkan (Fase 4).*
7. `validate_rig_symmetry` — *Ditangguhkan.*
8. `apply_vertex_color` — *Ditangguhkan.*
9. `bake_reference_texture` — *Ditangguhkan.*
10. `set_pose` — *Ditangguhkan (Fase 4).*
11. `insert_keyframe` — *Ditangguhkan (Fase 4).*
12. `apply_easing_to_action` — *Ditangguhkan (Fase 4).*
13. `export_rig_metadata` — *Ditangguhkan.*
14. `setup_fluid_simulation` — *Ditangguhkan.*
15. `setup_cloth_physics` — *Ditangguhkan (Fase 4).*
16. `bake_simulation` — *Ditangguhkan.*
17. `render_simulation_to_flipbook` — *Ditangguhkan.*

---

## 4. Kontrak Status File & Targeting

1. **Operasi File Eksis (`blend_file`)**:
   - Wajib digunakan pada seluruh mutasi yang memodifikasi scene eksis (`apply_modifier`, `merge_by_distance`, `unwrap_uv`, `add_bone`, `set_bone_roll`).
   - Wajib digunakan sebagai sumber pada `export_gltf`.
2. **Operasi Pembuatan File Baru (`output_blend_file`)**:
   - Digunakan saat menginisialisasi file `.blend` baru via `create_mesh_primitive`, `create_armature`, `create_flat_material`, atau `set_shading_mode`.
   - Dilarang mencampurkan `blend_file` dan `output_blend_file` dalam satu pemanggilan.
3. **Larangan Mutasi Tanpa Target**:
   - Pemanggilan mutasi tanpa `blend_file` atau `output_blend_file` ditolak seketika dengan `INVALID_TARGET_STATE`.

---

## 5. Kontrak Ekspor & Validasi Artefak

- **Format yang Didukung**: Hanya `.glb` dan `.gltf` (glTF 2.0). Format lain (`.fbx`, `.obj`) ditolak dengan `INVALID_INPUT`.
- **Proteksi Overwrite**: Default `overwrite: false`. Menolak ekspor jika file output atau file pendamping `.bin` sudah ada di disk, kecuali `overwrite: true`.
- **Proteksi Tabrakan Path**: Menolak jika `path === blend_file`.
- **Validasi Struktural Biner (`validate_export`)**:
  - Memverifikasi magic `glTF` (`0x46546C67`), version 2, kesesuaian declared length vs physical length, JSON chunk type, asset version, dan keberadaan node sentinel.
  - Memvalidasi keberadaan fisik buffer biner lokal (`.bin`) pada manifest `.gltf`.
  - Membedakan validator execution error (`isError: true`) vs artifact validation failure (`isError: false, valid: false`).
  - `require_armature: true` mensyaratkan keberadaan struktur skin/joint glTF yang valid (tidak mengklaim kompatibilitas engine pihak ketiga).

---

## 6. Ekosistem DCC, Sculpting, Rigging & Pipeline Lanjutan

| Tools | Fungsi | Catatan Pipeline |
|---|---|---|
| **Substance 3D Painter** | Texturing detail PBR non-outline untuk Kaelen & dungeon. | Material PBR Stylized (Teori Bab 11.A). |
| **Unreal Engine 5 Control Rig & Chaos** | Rigging lanjutan di UE5 & simulasi fisika kain Syal Aina. | Dual-Mode: Chaos Cloth vs Keyframe (Teori Bab 13.B). |
| **Niagara VFX (UE5 Native)** | Partikel percikan lentera & uap es kutukan. | Indikator status visual diegetik. |
| **Unreal Insights & RenderDoc** | Profiling performa frame time ($<16.6\text{ ms}$). | Target 60 FPS Steam-Ready. |

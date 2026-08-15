# Daftar Lengkap Tools & MCP Stack — Lentera Pudar: 3D Action RPG
### Pemetaan Kebutuhan Teknis GDD, Moodboard (Kena + Hellblade), & Teori ke Toolset Konkret

Dokumen ini memetakan **setiap kebutuhan teknis dari GDD dan Teori Lentera Pudar** ke dalam **tools dan arsitektur MCP konkret** yang beroperasi di dalam pipeline proyek (Blender 5.2 LTS + Unreal Engine 5).

---

## 1. Inti Engine & DCC (Digital Content Creation)

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Unreal Engine 5** | Engine utama: Rendering Lumen/Nanite, Audio MetaSounds, Character Controller 3D | Ditetapkan di GDD Bab I sebagai Engine Produksi Utama. |
| **Blender 5.2 LTS** | Modeling 3D, sculpting high-detail, biomechanical rigging, animasi dasar | Ditetapkan di GDD Bab IX & AGENTS.md sebagai DCC Utama. |
| **Python 3.x** | Bahasa scripting dasar untuk Blender addon (`bpy`) & server MCP | Wajib untuk komunikasi dua arah Blender ↔ AI Agent. |
| **Node.js / TypeScript** | Menjalankan server MCP / Router dispatcher | Menghubungkan client AI Agent ke tools eksternal. |

---

## 2. MCP (Model Context Protocol) Layer — Jembatan AI ke Engine

| Komponen MCP | Fungsi | Catatan Arsitektur |
|---|---|---|
| **Blender MCP Server/Addon** | Memberi AI Agent akses perintah ke Blender: manipulasi mesh, material, UV, modifier, armature bone roll via `bpy` API. | Berjalan sebagai background socket server (default port `8097`). |
| **Unreal Engine MCP Plugin (Kustom)** | Memberi AI Agent akses ke Unreal Editor API: spawn actor, konfigurasi Blueprint, material instance, World Partition, Niagara. | Dibangun di atas **Unreal Python Editor Scripting** yang dibungkus endpoint MCP. |
| **Unreal Python Plugin** | Fondasi teknis modul `unreal` untuk manipulasi aset/level secara terprogram. | Wajib aktif di UE5 (`Edit ➔ Plugins ➔ Python Editor Script Plugin`). |
| **MCP Orchestration/Router** | Menjembatani urutan task multi-tool (misal: model di Blender ➔ ekspor ➔ impor & setup di UE5). | Router terintegrasi pada AI Agent. |
| **Shared Asset Bridge Folder** | Folder sinkronisasi ekspor FBX/glTF 2.0 deterministik dari Blender ke Content Browser UE5. | Menjamin zero-dependency loss saat transfer aset. |

---

## 3. Texturing & Material Authoring

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Substance 3D Painter** | Texturing detail PBR & stylized untuk Kaelen, Syal Aina, dan aset dungeon. | Kualitas material PBR (Teori Bab 11.A) sesuai standar visual Kena. |
| **Substance 3D Designer** | Pembuatan material prosedural: Kristal Es Transmissive (SSS) & batuan reruntuhan. | Teori Subsurface Scattering kristal es (Teori Bab 11.B). |
| **Quixel Megascans + Bridge** | Pustaka aset scan batuan reruntuhan kuno terintegrasi native dengan UE5. | Estetika reruntuhan organik-kuno (GDD Bab I). |
| **Unreal Material Editor (Native)** | Node-based shader untuk material live-driven (`Curse_Spread` parameter). | Teori Emissive Material Real-Time (Teori Bab 11.C). |

---

## 4. Rigging, Animasi & Motion Capture

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Blender Rigify / Custom Rig** | Hierarki armature biomekanik lengkap humanoid Kaelen. | Fondasi Skeleton Hierarchy (Teori Bab 10.A). |
| **UE5 Control Rig** | Rig lanjutan di dalam Unreal Engine untuk penyesuaian animasi & IK kaki real-time. | Teori IK sebagai constraint solving (Teori Bab 13.F). |
| **UE5 Chaos Cloth / Blender Cloth Sim** | Simulasi fisika kain dinamis untuk Syal Aina dan jubah Kaelen. | Teori Soft Body & Cloth Physics (Teori Bab 13.B). |
| **Marvelous Designer (Opsional)** | Pola jahitan kain realistis untuk Syal Aina sebelum disimulasikan. | Meningkatkan kualitas drapery kain syal emas. |
| **Cascadeur (Opsional)** | Animasi keyframe berbasis fisika AI untuk timing combat dan parry presisi. | 12 Prinsip Animasi Disney (Teori Bab 9.A). |
| **Mixamo (Opsional)** | Sumber data locomotion dasar untuk blend tree awal. | Teori Blend Tree & Locomotion FSM (Teori Bab 9.C). |
| **Live Link Face (Opsional)** | Capture mikro-ekspresi wajah untuk facial blend shapes saat cutscene dekat. | Teori Facial Rigging & Kamera Intim (Teori Bab 10.C & 5.B). |

---

## 5. VFX & Simulasi Efek

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Niagara (UE5 Native)** | Partikel percikan lentera (`FX_Warmth_Embers`), uap es (`FX_Frost_Mist`), dan hit sparks. | Niagara sebagai indikator status visual (Teori Bab 11.D). |
| **UE5 Chaos Destruction** | Sistem retakan dan pecahan kristal es (*Voronoi Fracture*) saat serangan cakar es. | Teori Fracture Mechanics (Teori Bab 13.C). |
| **EmberGen (Opsional)** | Simulasi api/uap real-time yang di-bake menjadi flipbook texture. | Teori Fluid Dynamics Disederhanakan (Teori Bab 13.D). |
| **Houdini (Opsional)** | Pola retakan prosedural kompleks jika dibutuhkan ekspansi dungeon. | Teori Noise & PCG (Teori Bab 14.E & 16.D). |

---

## 6. Audio System

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Wwise (Audiokinetic)** | Middleware audio adaptif: vertical layering musik, ducking otomatis, dan 3D binaural spatialization. | Teori Audio Adaptif & Binaural Whispers (Teori Bab 7.B & 7.C). |
| **UE5 MetaSounds (Native)** | Alternatif audio native UE5 untuk procedural sound design dan dynamic ducking. | Alternatif ringan tanpa middleware eksternal. |
| **DAW (Reaper / Audacity)** | Perekaman dan editing audio mentah (bisikan, foley es retak, piano berdebu). | Fondasi aset audio mentah. |
| **iZotope RX (Opsional)** | Pembersihan noise dan mastering bisikan jiwa beku (-16 LUFS). | Teori Sound Mixing & Mastering (Teori Bab 18.C). |

---

## 7. Level Design & World Building

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **UE5 World Partition (Native)** | Level streaming otomatis 5 Sektor Dungeon tanpa layar loading. | Teori World Partition & Level Streaming (Teori Bab 17.B). |
| **UE5 Spline Tools (Native)** | Pembentukan lorong berkelok organik (*Hall of Mirrors*) dan jalur patroli. | Teori Spline & Bezier Curves (Teori Bab 14.C). |
| **UE5 Level Sequencer (Native)** | Pembuatan cutscene Altar Duka dengan kamera dekat over-the-shoulder. | Teori Kamera sebagai Alat Naratif (Teori Bab 5.B). |

---

## 8. Gameplay, Kombat & AI System

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **UE5 Behavior Tree + Blackboard** | Logika AI musuh jiwa beku dan pola boss 5 sektor. | Teori AI Behavior Tree (Teori Bab 16.E). |
| **UE5 Animation Blueprint** | FSM combat, combo attack, parry window 12-frame, dan hitstop. | Teori FSM & State Machine (Teori Bab 14.F & GDD Bab VI). |
| **Gameplay Ability System (GAS)** | Framework pengelolaan status effect, cooldown, stamina, dan Curse Meter. | Teori Risk-Reward & Resource Balancing (Teori Bab 4.D). |
| **Material Parameter Collection (MPC)** | Pengontrol nilai emissive es dan desaturasi layar secara terpusat. | Teori Dynamic Material Parameter (Teori Bab 11.C). |

---

## 9. Optimasi, Version Control & Platform

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Unreal Insights & RenderDoc** | Profiling performa frame time ($<16.6\text{ ms}$) dan debugging draw calls/Lumen. | Teori Performance Budgeting 60 FPS (Teori Bab 17.A). |
| **Git + Git LFS / Perforce** | Version control file biner besar (`.blend`, `.uasset`, `.fbx`, `.wav`). | Teori Version Control Aset 3D (Teori Bab 17.D). |
| **Steamworks SDK** | Integrasi Cloud Save, Achievements, dan Controller Support. | Target Platform PC Windows / Steam (GDD Bab I). |

---

## 10. Prioritas Eksekusi Pipeline (Tahap Demi Tahap)

1. **Prioritas 1 (Fondasi Wajib)**: Unreal Engine 5 + Blender 5.2 LTS + Python + Blender MCP Server + Unreal Python Scripting.
2. **Prioritas 2 (Aset Utama Kaelen & Aina)**: Modeling/Rigging Kaelen di Blender + Texturing PBR Substance + Chaos Cloth Syal Aina.
3. **Prioritas 3 (Core Combat & Diegetic Gameplay)**: Animation Blueprint (Combo, Parry, Hitstop) + Curse Meter MPC + Adaptive Camera.
4. **Prioritas 4 (Level & Audio)**: Grey-box Sektor 1 di UE5 World Partition + MetaSounds Binaural Whispers + Niagara Particles.
5. **Prioritas 5 (Polish & QC)**: Profiling Unreal Insights solid 60 FPS + Steamworks SDK build packaging.

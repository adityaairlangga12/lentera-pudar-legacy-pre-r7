# Rantai Tools, MCP Ecosystem & Pipeline Stack — Lentera Pudar
### Standardisasi Rantai Tools 3D Action RPG (Blender 5.2 LTS + Unreal Engine 5)

> **Dokumen Sumber Kebenaran Rantai Tools (*Toolchain & MCP Reference*)**  
> Menetapkan seluruh perangkat lunak, plugin, addon Blender, arsitektur Model Context Protocol (MCP), dan pipeline otomasi aset 3D untuk semesta *Lentera Pudar*.

---

## 1. Fondasi Engine & Core DCC

| Software | Versi / Tipe | Peran Utama | Catatan Kunci |
|---|---|---|---|
| **Unreal Engine 5** | 5.8 / Modern 5.x | Game Engine Utama (Rendering Lumen, Nanite, Niagara, Chaos Cloth, World Partition). | Target performa solid 60 FPS ($<16.6\text{ ms}$). |
| **Blender** | 5.2 LTS | DCC Primer untuk Pemodelan 3D, Sculpting, Biomechanical Rigging, Retopology, dan glTF/FBX export. | Berjalan bersama Blender MCP Addon (Port 8097). |
| **Python** | 3.10+ | Bahasa Scripting Otomasi MCP (Blender `bpy` & UE5 `unreal` module). | Jembatan perintah AI Agent ke engine. |

---

## 2. Arsitektur Model Context Protocol (MCP) & Bridge

| Komponen MCP | Fungsi | Catatan Arsitektur |
|---|---|---|
| **Blender MCP Server/Addon** | Memberi AI Agent akses perintah ke Blender: manipulasi mesh, material, UV, modifier, armature via `bpy` API. | Socket server lokal (port `8097`). Sintaks mengacu pada [api-cheat-sheet.md](file:///d:/GodotProjects/Lentera-Pudar/references/api-cheat-sheet.md). |
| **Unreal Engine MCP Plugin** | Memberi AI Agent akses ke Unreal Editor API: spawn actor, Blueprint, material instance, World Partition, Niagara. | Wrapper di atas `unreal` Python Editor Scripting. |
| **Blender-Unreal Pipeline Plugin (Epic Games)** | Addon resmi Epic Games untuk otomasi "Send to Unreal" — ekspor mesh, rig, dan animasi langsung ke Content Browser UE5. | Menjamin transfer aset satu-klik yang deterministik dan stabil. |
| **Shared Asset Bridge Folder** | Folder sinkronisasi ekspor FBX/glTF 2.0 deterministik dari Blender ke Content Browser UE5. | Alternatif jembatan aset lokal deterministik. |

---

## 3. Sculpting, Modeling & Texturing Ecosystem

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Substance 3D Painter** | Texturing detail PBR non-outline untuk Kaelen, Syal Aina, dan aset dungeon. | Material PBR Stylized (Teori Bab 11.A, [additional-techniques.md](file:///d:/GodotProjects/Lentera-Pudar/references/additional-techniques.md)). |
| **Substance 3D Designer** | Pembuatan material prosedural: Kristal Es Transmissive (SSS) & batuan reruntuhan. | Teori Subsurface Scattering kristal es (Teori Bab 11.B). |
| **Quixel Megascans + Bridge** | Pustaka aset scan batuan reruntuhan kuno terintegrasi native dengan UE5. | Estetika reruntuhan organik-kuno (GDD Bab I). |
| **Poly Haven (Library Gratis)** | Sumber HDRI, tekstur PBR, dan model lingkungan gratis berkualitas tinggi. | Pelengkap Megascans untuk variasi material tanpa biaya lisensi. |
| **ZBrush (Opsional)** | Sculpting high-poly detail ekstrem untuk karakter hero Kaelen dan boss. | Sub-divisi tinggi sebelum retopology ke 40k–60k tris. |
| **Hard Ops / Boxcutter (Blender Addon)** | Mempercepat hard-surface modeling untuk zirah boss (Lord Alden dkk) dan altar batu. | Presisi arsitektur dungeon geometris. |
| **Unreal Material Editor (Native)** | Node-based shader untuk material live-driven (`Curse_Spread` parameter). | Teori Emissive Material Real-Time (Teori Bab 11.C). |

---

## 4. Rigging, Biomekanika, Animasi & Cloth

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Blender Rigify / Custom Rig** | Hierarki armature biomekanik lengkap humanoid Kaelen (`Root` ➔ `Pelvis` ➔ `Spine` ➔ `Limb`). | Fondasi Skeleton Hierarchy & Bony Landmarks (Teori Bab 10.A & [anatomy-kinesiology.md](file:///d:/GodotProjects/Lentera-Pudar/references/anatomy-kinesiology.md)). |
| **Auto-Rig Pro (Pelengkap Rigify)** | Rigging tingkat lanjut dengan kontrol facial blend shapes dan rantai tulang sekunder. | Mematangkan ekspresi close-up ala Hellblade II di Altar Duka. |
| **UE5 Control Rig** | Rig lanjutan di dalam Unreal Engine untuk penyesuaian animasi & IK kaki real-time. | Teori IK sebagai constraint solving (Teori Bab 13.F). |
| **UE5 Chaos Cloth / Blender Cloth Sim** | Simulasi fisika kain dinamis untuk Syal Aina (Dual-Mode: Sim vs Hand-Keyed). | Teori Soft Body & Cloth Physics (Teori Bab 13.B). |
| **Marvelous Designer (Opsional)** | Pola jahitan kain realistis untuk Syal Aina sebelum disimulasikan. | Meningkatkan kualitas drapery kain syal emas. |
| **Cascadeur (Opsional)** | Animasi keyframe berbasis fisika AI untuk timing combat dan parry presisi. | 12 Prinsip Animasi & Rantai Kinetik Kombat. |

---

## 5. VFX, Prosedural & Simulasi Fisika

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Niagara (UE5 Native)** | Partikel percikan lentera (`FX_Warmth_Embers`), uap es (`FX_Frost_Mist`), dan hit sparks. | Niagara sebagai indikator status visual (Teori Bab 11.D). |
| **UE5 PCG Framework (Native)** | Distribusi reruntuhan, puing, dan vegetasi es otomatis berbasis aturan algoritmik. | Efisiensi world-building dungeon skala besar. |
| **Blender Geometry Nodes (Native)** | Modeling prosedural Blender-side untuk variasi kristal es, retakan, dan puing sebelum ekspor. | Menghasilkan variasi prop modular secara cepat. |
| **UE5 Chaos Destruction** | Sistem retakan dan pecahan kristal es (*Voronoi Fracture*) saat serangan cakar es. | Teori Fracture Mechanics (Teori Bab 13.C). |
| **EmberGen (Opsional)** | Simulasi api/uap real-time yang di-bake menjadi flipbook texture. | Teori Fluid Dynamics Disederhanakan (Teori Bab 13.D). |
| **Houdini (Opsional)** | Pola retakan prosedural kompleks jika dibutuhkan ekspansi dungeon. | Teori Noise & PCG (Teori Bab 14.E & 16.D). |

---

## 6. Audio System (3D Spasial & Adaptive Music)

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Wwise (Audiokinetic)** | Middleware audio adaptif: vertical layering musik, ducking otomatis, dan 3D binaural spatialization. | Teori Audio Adaptif & Binaural Whispers (Teori Bab 7.B & 7.C). |
| **UE5 MetaSounds (Native)** | Alternatif audio native UE5 untuk procedural sound design dan dynamic ducking. | Alternatif ringan tanpa middleware eksternal. |
| **DAW (Reaper / Audacity)** | Perekaman dan editing audio mentah (bisikan, foley es retak, piano berdebu). | Fondasi aset audio mentah. |
| **iZotope RX (Opsional)** | Pembersihan noise dan mastering bisikan jiwa beku (-16 LUFS / -18 LUFS). | Teori Sound Mixing & Mastering (Teori Bab 18.C). |

---

## 7. Level Design & Pencahayaan (Lighting)

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **UE5 World Partition (Native)** | Level streaming otomatis 5 Sektor Dungeon tanpa layar loading. | Teori World Partition & Level Streaming (Teori Bab 17.B). |
| **UE5 Lumen (Real-Time GI)** | Pencahayaan dinamis real-time untuk pendaran lentera Aina dan kristal es. | Teori Kontras Suhu Kelvin (2700K vs 6500K). |
| **UE5 Lightmass (Baked Lighting)** | Pencahayaan statis yang di-bake untuk area dungeon statis guna meringankan beban GPU. | Kena Lighting Benchmark (Hybrid Lumen + Lightmass). |
| **UE5 Spline Tools (Native)** | Pembentukan lorong berkelok organik (*Hall of Mirrors*) dan jalur patroli. | Teori Spline & Bezier Curves (Teori Bab 14.C). |
| **UE5 Level Sequencer (Native)** | Pembuatan cutscene Altar Duka dengan kamera dekat over-the-shoulder. | Teori Kamera sebagai Alat Naratif (Teori Bab 5.B). |

---

## 8. Profiling, Build & Platform

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Unreal Insights & RenderDoc** | Profiling performa frame time ($<16.6\text{ ms}$) dan debugging draw calls/Lumen. | Teori Performance Budgeting 60 FPS (Teori Bab 17.A). |
| **Git + Git LFS / Perforce** | Version control file biner besar (`.blend`, `.uasset`, `.fbx`, `.wav`). | Teori Version Control Aset 3D (Teori Bab 17.D). |
| **Steamworks SDK** | Integrasi Cloud Save, Achievements, dan Controller Support. | Target Platform PC Windows / Steam (GDD Bab I). |

---

## 9. Prioritas Eksekusi Pipeline (Tahap Demi Tahap)

1. **Prioritas 1 (Fondasi Wajib)**: Unreal Engine 5 + Blender 5.2 LTS + Python + Blender-Unreal Pipeline Plugin + Unreal Python Scripting.
2. **Prioritas 2 (Aset Utama Kaelen & Aina)**: Modeling/Rigging Kaelen di Blender + Texturing PBR Substance + Chaos Cloth Syal Aina.
3. **Prioritas 3 (Core Combat & Diegetic Gameplay)**: Animation Blueprint (Combo, Parry, Hitstop) + Curse Meter MPC + Adaptive Camera.
4. **Prioritas 4 (Level & Audio)**: Modular Kit-Bashing (Grid 300cm) + World Partition Sektor 1 + MetaSounds Binaural Whispers + Niagara Particles.
5. **Prioritas 5 (Polish & QC)**: Profiling Unreal Insights solid 60 FPS + Steamworks SDK build packaging.

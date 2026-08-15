# Daftar Lengkap Tools & MCP Stack — Lentera Pudar
### Berdasarkan GDD, Moodboard (Kena + Hellblade), dan Referensi Teori yang Sudah Dirancang

Dokumen ini memetakan **setiap kebutuhan teknis dari GDD/teori** ke **tools konkret** yang perlu ada di proyek, dikelompokkan per fungsi pipeline. Untuk tiap tools disertakan alasan singkat kenapa dibutuhkan (ditelusuri balik ke elemen spesifik GDD/teori), supaya tidak ada yang ditambahkan tanpa alasan jelas.

---

## 1. Inti Engine & DCC (Digital Content Creation)

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Unreal Engine 5** | Engine utama, target rendering Lumen/Nanite | Sudah ditetapkan di GDD sebagai engine utama |
| **Blender 5.2 LTS** | Modeling, sculpting, rigging, animasi dasar sebelum diekspor ke UE5 | Sudah ditetapkan di GDD sebagai DCC utama |
| **Python 3.x** | Bahasa scripting dasar untuk Blender addon & MCP server | Wajib untuk komunikasi Blender ↔ AI agent lewat MCP |
| **Node.js / TypeScript runtime** | Menjalankan server MCP (kalau MCP kustom kamu berbasis Node, umum untuk implementasi MCP server) | Dibutuhkan agar AI agent bisa terhubung ke Blender/UE5 sebagai "tool" |

---

## 2. MCP (Model Context Protocol) Layer — Jembatan AI ke Engine

Ini bagian paling krusial karena inilah yang membuat AI agent kamu bisa benar-benar "mengeksekusi" pekerjaan, bukan cuma memberi saran teks.

| MCP Component | Fungsi | Catatan |
|---|---|---|
| **Blender MCP Server/Addon** | Memberi AI agent akses command ke Blender: membuat mesh, mengatur material, menjalankan operator (rig, UV unwrap, dsb) lewat `bpy` API | Umumnya diimplementasi sebagai Blender addon (socket server) yang menerima perintah dari MCP client |
| **Unreal Engine MCP Plugin (Kustom)** | Memberi AI agent akses ke Unreal Editor API: spawn actor, atur Blueprint, buat material instance, atur level streaming, dsb | Karena kamu sebut "kustom", ini kemungkinan besar dibangun di atas **Unreal Python API** atau **Unreal Editor Scripting (Blueprint/C++) yang dibungkus jadi endpoint MCP** |
| **Unreal Python Plugin (Editor Scripting)** | Fondasi teknis di balik MCP UE5 kustom — akses ke `unreal` Python module bawaan UE5 untuk manipulasi aset/level secara terprogram | Wajib aktif di UE5 (Edit → Plugins → Python Editor Script Plugin) |
| **MCP Orchestration/Router** | Kalau agent perlu berpindah konteks antara "kerja di Blender" dan "kerja di UE5" dalam satu task (misal: model di Blender → export → import & setup di UE5), perlu layer yang mengatur urutan pemanggilan tool ini | Bagian dari arsitektur MCP kustom kamu sendiri, bukan software terpisah |
| **File Bridge / Shared Asset Folder** | Folder bersama (atau otomatisasi export/import) antara hasil kerja Blender dan aset masuk ke UE5 Content Browser | Bisa manual (FBX export/import berkala) atau otomatis lewat script MCP |

---

## 3. Texturing & Material Authoring

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Substance 3D Painter** | Texturing detail (hand-paint/procedural) untuk karakter Kaelen, Aina, prop dungeon | Diperlukan untuk kualitas PBR material (teori bagian 11.A) sesuai standar visual Kena |
| **Substance 3D Designer** | Membuat material prosedural reusable — penting untuk material kristal es (SSS custom), dinding batu reruntuhan | Terkait teori Subsurface Scattering es (bagian 11.B) |
| **Quixel Megascans + Bridge** | Library aset scan reruntuhan/batu/permukaan alami berkualitas tinggi, terintegrasi native dengan UE5 | Cocok untuk estetika reruntuhan organik ala Kena (moodboard bagian 2) |
| **Unreal Material Editor (native)** | Node-based shader authoring langsung di UE5 untuk material dinamis (emissive terhubung Curse Meter, dsb) | Wajib untuk teori Emissive Material Real-Time (bagian 11.C) |

---

## 4. Rigging, Animasi & Motion Capture

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Blender Rigify** | Auto-rigging humanoid dasar untuk Kaelen sebelum kustomisasi | Fondasi skeleton hierarchy (teori bagian 10.A) |
| **UE5 Control Rig** | Rig lanjutan di dalam Unreal untuk kontrol animasi real-time, termasuk IK setup | Terkait teori IK sebagai constraint solving (bagian 3.F, 13.F) |
| **UE5 Chaos Cloth / Blender Cloth Simulation** | Simulasi kain untuk syal Aina dan jubah Kaelen | Langsung terkait teori Cloth Physics/PBD (bagian 13.B) |
| **Marvelous Designer (opsional tapi direkomendasikan)** | Membuat pola kain syal/jubah yang realistis secara jahitan sebelum disimulasikan, lebih presisi dari sekadar plane mesh | Meningkatkan kualitas cloth sim di atas, terutama untuk syal Aina yang jadi elemen sentral naratif |
| **Cascadeur (opsional)** | Animasi keyframe berbantuan AI/fisika untuk gerakan combat yang butuh timing presisi tanpa mocap | Mendukung prinsip animasi 12 Disney (bagian 9.A) tanpa perlu studio mocap fisik |
| **Mixamo (opsional, gratis)** | Sumber animasi dasar (locomotion umum) yang bisa di-retarget ke skeleton Kaelen sebagai starting point | Mempercepat awal produksi blend tree locomotion (bagian 9.C) |
| **Live Link Face (jika ada akses iPhone + UE5)** | Capture ekspresi wajah real-time untuk blend shape close-up ala Hellblade II | Terkait teori facial rigging/blend shapes (bagian 10.C) dan kamera dekat naratif (bagian 5.B) |

---

## 5. VFX & Simulasi Efek

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Niagara (UE5 native)** | Sistem partikel utama: kunang-kunang cahaya syal, pecahan es, uap dingin | Sudah disebut eksplisit di GDD, terkait teori Niagara sebagai indikator status (bagian 11.D) |
| **EmberGen (opsional)** | Simulasi asap/api real-time yang bisa di-bake jadi flipbook texture untuk efek uap dingin/leleh es | Terkait teori Fluid Dynamics Disederhanakan (bagian 13.D) |
| **UE5 Chaos Destruction** | Sistem fracture/destruction untuk reruntuhan dan pecahan es besar | Terkait teori Fracture Mechanics/Voronoi (bagian 13.C) |
| **Houdini (opsional, untuk kebutuhan prosedural lanjut)** | Kalau butuh generate pola fracture/noise yang lebih kompleks dari default UE5, atau eksperimen PCG lanjutan | Terkait teori Perlin/Simplex Noise (bagian 14.E) dan PCG opsional (bagian 16.D) |

---

## 6. Audio

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Wwise (Audiokinetic)** | Middleware audio adaptif — layering musik dinamis, ducking otomatis, binaural spatial audio | Langsung terkait teori Adaptive Music/Vertical Layering (bagian 7.C) dan Binaural Audio (bagian 7.B) — jauh lebih kuat dari sistem audio bawaan UE5 untuk kebutuhan sekompleks ini |
| **UE5 MetaSounds (alternatif native)** | Kalau tidak pakai Wwise, MetaSounds native UE5 juga bisa menangani sebagian besar kebutuhan adaptive audio, meski kurang matang untuk binaural kompleks | Alternatif lebih ringan dari Wwise |
| **Reaper / Audacity / DAW pilihan** | Rekam & edit raw audio (bisikan, ambience, foley) sebelum diimpor ke Wwise/UE5 | Fondasi produksi audio mentah |
| **iZotope RX (opsional)** | Cleanup noise pada rekaman voice/whisper supaya kualitas konsisten | Mendukung kualitas final bisikan jiwa beku |

---

## 7. Level Design & World Building

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **UE5 World Partition (native)** | Streaming otomatis dungeon besar 5 sektor berdasarkan posisi pemain | Langsung terkait teori World Partition/Level Streaming (bagian 17.B) |
| **UE5 Landscape Tools (native)** | Kalau ada area outdoor/transisi antar sektor berskala besar | Relevan untuk estetika organik-reruntuhan ala Kena |
| **UE5 Spline Tools (native)** | Membuat lorong berkelok (Hall of Mirrors), jalur kamera sinematik, jalur patroli musuh | Langsung terkait teori Spline & Bezier Curves (bagian 14.C) |
| **Unreal Level Sequencer (native)** | Membuat cutscene Altar Duka, kamera dekat naratif ala Hellblade II | Terkait teori Kamera sebagai Alat Naratif (bagian 5.B) |

---

## 8. AI, Combat & Sistem Gameplay

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **UE5 Behavior Tree + Blackboard (native)** | Logika AI musuh (jiwa beku pasif/agresif, boss pattern) | Langsung terkait teori AI Behavior Tree (bagian 16.E) |
| **UE5 Animation Blueprint (native)** | State machine combat & locomotion Kaelen | Terkait teori FSM (bagian 14.F) dan Blend Tree (bagian 9.C) |
| **UE5 Gameplay Ability System / GAS (opsional tapi direkomendasikan)** | Framework built-in UE5 untuk sistem kemampuan, meter (Curse Meter), status effect, cooldown | Sangat cocok untuk struktur Curse Meter Surge, parry window, stagger system (bagian 4.B, 4.C, 4.D) |
| **UE5 Material Parameter Collection (native)** | Menghubungkan Curse Meter secara real-time ke banyak material sekaligus (emissive lengan es, dsb) | Langsung terkait teori Emissive Dinamis (bagian 11.C) |

---

## 9. Optimasi & Profiling

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Unreal Insights (native)** | Profiling performa CPU/GPU real-time selama development | Langsung terkait teori Performance Budgeting (bagian 17.A) |
| **RenderDoc** | Debug rendering frame-by-frame kalau ada masalah visual aneh (shader, lighting) | Membantu troubleshoot isu Lumen/SDF (bagian 13.E, 14.D) |
| **UE5 Nanite & LOD tools (native)** | Otomatisasi level of detail untuk geometri kompleks | Langsung terkait teori LOD/Culling (bagian 17.A) |

---

## 10. Version Control & Project Management

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Perforce (Helix Core)** | Version control standar industri untuk aset biner besar (.uasset, .blend) — lebih matang dari Git untuk kebutuhan ini | Langsung terkait teori Version Control Aset 3D (bagian 17.D) |
| **Git + Git LFS (alternatif lebih ringan)** | Kalau tim kecil/solo dan tidak ingin setup Perforce server, Git LFS bisa jadi alternatif lebih sederhana | Alternatif dari poin di atas |
| **Notion / Trello / Jira** | Menyimpan GDD sebagai living document, tracking task, bug list | Terkait teori Living Document (bagian 18.G) dan Playtesting Metrics (bagian 18.F) |
| **Perforce/Git Hooks + Naming Convention Enforcement** | Otomatisasi validasi penamaan aset sesuai konvensi sebelum commit | Terkait teori Asset Naming Convention (bagian 17.C) — penting khusus karena AI agent butuh konsistensi nama antar sesi |

---

## 11. UI/UX & Localization

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **UE5 UMG (Unreal Motion Graphics, native)** | Membangun UI diegetic/minimal (indikator radius cahaya syal, subtitle bisikan) | Langsung terkait teori Diegetic & Minimal HUD (bagian 8.A) |
| **Figma (opsional, untuk mockup awal)** | Merancang layout UI sebelum diimplementasi di UMG, termasuk uji kontras subtitle | Mendukung teori Typography & Subtitle Readability (bagian 18.D) |
| **UE5 Localization Dashboard (native)** | Mengelola teks multi-bahasa dengan text expansion buffer | Langsung terkait teori Localization-Readiness (bagian 18.E) |

---

## 12. QA & Accessibility

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **UE5 Automated Testing Framework (native)** | Test otomatis dasar untuk fungsi gameplay kritikal (trigger Altar Duka, save/load) | Mendukung stabilitas sistem save permanen (bagian 17.E) |
| **Colorblind Simulation Plugin/Tool (mis. Coblis, atau post-process filter custom di UE5)** | Menguji apakah kontras hangat/dingin tetap terbaca untuk pemain colorblind | Langsung terkait teori Accessibility Design (bagian 16.C) |
| **Custom Telemetry/Analytics (ringan, bisa built sendiri via UE5 Analytics plugin)** | Mencatat titik kematian/frustrasi pemain saat playtest | Terkait teori Playtesting Metrics (bagian 18.F) |

---

## 13. Distribusi & Platform

| Tools | Fungsi | Terhubung ke GDD/Teori |
|---|---|---|
| **Steamworks SDK** | Integrasi achievement, cloud save, dsb — karena GDD sudah menetapkan target platform Steam/PC | Sesuai identitas platform di GDD bagian 1 |
| **UE5 Packaging & Build Tools (native)** | Build final .exe untuk distribusi/testing | Standar wajib rilis PC |

---

## 14. Ringkasan Prioritas Setup Awal (Kalau Harus Diurutkan)

Karena daftar di atas panjang, ini urutan realistis untuk mulai setup MCP + pipeline:

1. **Fondasi wajib**: Unreal Engine 5 + Blender 5.2 LTS + Python + Blender MCP Addon + Unreal Python Editor Scripting Plugin (baru MCP kustom kamu bisa berjalan sama sekali)
2. **Texturing dasar**: Substance Painter/Designer (kualitas visual Kena sangat bergantung material yang bagus)
3. **Rigging & cloth**: Blender Rigify + UE5 Control Rig + Chaos Cloth (syal Aina adalah elemen paling sentral secara naratif — prioritaskan lebih awal dari fitur lain)
4. **Sistem gameplay inti**: UE5 Behavior Tree, Animation Blueprint, Gameplay Ability System (fondasi combat & Curse Meter)
5. **Audio**: Wwise (kalau budget/waktu terbatas, MetaSounds native cukup untuk versi awal, upgrade nanti)
6. **Baru setelahnya**: VFX lanjutan (Niagara detail, EmberGen/Houdini), optimasi (Unreal Insights, RenderDoc), lalu lapisan produksi (version control, QA, localization) begitu proyek mulai punya build yang stabil untuk diuji.

---

*Dokumen ini melengkapi GDD, Moodboard Referensi (Kena + Hellblade), dan Referensi Teori sebagai bagian dari satu paket dokumentasi pra-produksi Lentera Pudar.*

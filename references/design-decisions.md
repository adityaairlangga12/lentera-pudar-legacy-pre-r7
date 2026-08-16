# Design Decisions Log — Lentera Pudar

Dokumen ini mencatat seluruh keputusan arsitektur struktural, desain game, dan pilihan teknis berbiaya tinggi (*Architecture Decision Records*). Tujuannya agar keputusan di masa lalu memiliki konteks jelas dan tidak didebat ulang dari nol.

---

## Log Keputusan yang Sudah Ditetapkan

### ADR-001: Model Rendering 8-Arah Murni & Asimetri Lore
- **Tanggal**: 2026-08-13
- **Status**: Superseded by ADR-008 ➔ Digantikan sepenuhnya oleh 3D Native di ADR-013
- **Konteks**: Karakter utama memiliki desain asimetris: tangan kiri dibalut perban dengan urat es biru (Kutukan Pudar), mata kanan mengenakan eyepatch, sedangkan tangan kanan normal.
- **Keputusan Awal**: 2D True 8-Way.
- **Evolusi**: Digantikan oleh ADR-008 (Jalur B), dan selanjutnya ditransisikan penuh ke **3D High-Detail Armature Rigging di Blender 5.2 LTS + Unreal Engine 5** pada ADR-013 yang menjamin akurasi asimetri 360° secara native.

### ADR-002: Arsitektur Komunikasi Global Event Bus
- **Tanggal**: 2026-08-13
- **Status**: Superseded by ADR-013 & ADR-014 (Diadaptasi ke Unreal Engine 5)
- **Konteks**: Komunikasi antar komponen sistem game rawan spaghetti code jika menggunakan direct querying yang erat (*tight coupling*).
- **Keputusan Awal**: Seluruh interaksi lintas sistem disalurkan melalui Event Bus terpusat.
- **Evolusi 3D (UE5)**: Ditransisikan ke arsitektur **Unreal Engine 5 Gameplay Ability System (GAS), Event Delegates, Blueprint Interfaces, dan Subsystems** pada ADR-013 & ADR-015.

### ADR-003: Pipeline Visual Berbasis Otomasi & Observabilitas
- **Tanggal**: 2026-08-13
- **Status**: Superseded by ADR-008 ➔ Digantikan oleh Pipeline 3D di ADR-013 & ADR-015
- **Konteks**: Memaksimalkan kecepatan produksi tanpa mengorbankan kualitas visual dan kepatuhan lore.
- **Keputusan Awal**: Alur 3 tahap Pixellab ➔ Aseprite ➔ Godot.
- **Evolusi**: Digantikan secara total oleh pipeline **Blender 5.2 LTS (Port 8097) + Unreal Engine 5 Python Scripting MCP** pada ADR-013 & ADR-015.

### ADR-004: Arsitektur Narasi Berbasis 5 Tahap Berduka (5 Stages of Grief)
- **Tanggal**: 2026-08-14
- **Status**: Accepted (Standard Baku — Dipertahankan di 3D)
- **Konteks**: Mencegah alur cerita RPG terasa monoton atau berulang dengan menyematkan struktur psikologis mendalam di setiap sektor dungeon.
- **Keputusan Terpilih**: 5 Sektor Dungeon memetakan Kübler-Ross Model (Sektor 1: Denial - Lord Alden, Sektor 2: Anger - Ignis Vulkan, Sektor 3: Bargaining - Lady Vespera, Sektor 4: Depression - The Hollow Reflection, Sektor 5: Acceptance - The Frost Sovereign & Fajar Terakhir).
- **Dampak**: Setiap bos dan lingkungan memiliki resonansi tematik yang terhubung langsung dengan perkembangan psikologis pemain dan protagonis di semesta 3D.

### ADR-005: Mekanik Karakter Dualitas (The Fading Scarf & Temptation of Frost)
- **Tanggal**: 2026-08-14
- **Status**: Accepted (Standard Baku — Dipertahankan di 3D)
- **Konteks**: Menghubungkan narasi Kaelen & Aina langsung ke elemen visual dan gameplay.
- **Keputusan Terpilih**: 
  1. *The Fading Scarf*: Syal kuning Aina memendek secara visual seiring berjalannya progres cerita (diimplementasikan via Chaos Cloth 4 stages di ADR-014).
  2. *The Temptation of Frost*: Penggunaan kekuatan tangan kiri es semakin mematikan tetapi berisiko membeku (*Freeze of Despair*).
- **Dampak**: Pemain merasakan bobot pengorbanan Aina dan godaan kekuatan keputusasaan secara konstan.

### ADR-006: Visi Skalabilitas Franchise (Lentera Pudar Expanded Universe)
- **Tanggal**: 2026-08-14
- **Status**: Accepted (Standard Baku — Dipertahankan di 3D)
- **Konteks**: Membangun fondasi semesta yang mampu menampung sekuel (*Lentera Pudar 2: The Frozen Horizon* & *Lentera Pudar 3: The Sovereign of Dawn*).
- **Keputusan Terpilih**: Game 1 berfokus pada penyembuhan duka pribadi di dungeon bawah tanah dan berakhir dengan terbukanya gerbang ke Benua Luar (*Overworld* beku).
- **Dampak**: Arsitektur dungeon, mekanik kutukan, dan data item dirancang extensible untuk ekspansi franchise 3D.

### ADR-007: Standardisasi Desain Visual Anatomi Kaelen (Eyepatch, Baldric, & Directional Details)
- **Tanggal**: 2026-08-14
- **Status**: Partially Superseded by ADR-013 & ADR-014 (Desain visual Eyepatch & Baldric dipertahankan; proporsi diperbarui ke 1:6.8)
- **Konteks**: Memilih base art definitif yang menyeimbangkan estetika visual, resonansi emosional duka, dan kepatuhan lore asimetri.
- **Keputusan Terpilih**: 
  1. Mengesahkan Penutup Mata Kulit Hitam (*Eyepatch* `#141013`) pada mata kanan sebagai segel bekas luka beku Kutukan Pudar masa lalu (diperluas jadi mekanik persepsi *The Eye of Frost* di ADR-014).
  2. Mengesahkan Tali Selempang Kantung Kelana (*Baldric Harness*) untuk memecah bidang jubah gelap dan mempertegas identitas pengelana.
  3. Mengadopsi proporsi atletis 1:6.8 stylized-realistic (*FF7 Remake / Kena Grade*) menggantikan rasio awal pada era 2D.
- **Dampak**: Identitas visual Kaelen terkunci kokoh, matang, dan bebas dari kejanggalan proporsi.

---

### ADR-008: Transisi Menyeluruh ke Jalur B (Hybrid 3D Low-Poly)
- **Tanggal**: 2026-08-15
- **Status**: Superseded by ADR-013 (Transisi Total ke 3D Action RPG UE5 + Blender 5.2 LTS)
- **Konteks**: Pendekatan 2D pixel art manual mengalami kegagalan akibat diskontinuitas asimetri (lengan kutukan tertukar saat mirror) dan kesulitan menganimasikan Syal Aina di seluruh arah.
- **Keputusan Awal**: Mengadopsi Jalur B (3D Low-Poly 300–1000 tris pre-render).
- **Evolusi**: Digantikan sepenuhnya oleh **Full 3D Action RPG (Unreal Engine 5 + Blender 5.2 LTS High-Detail 40k–60k tris LOD0)** pada ADR-013, menghapus seluruh ekosistem pixelation/2D.

### ADR-009: Standardisasi Mesin Animasi Berbasis Matematika & Fisika
- **Tanggal**: 2026-08-15
- **Status**: Accepted (Standard Baku — Diperluas ke UE5 Control Rig & Chaos Cloth)
- **Konteks**: Animasi murni manual sering kaku dan memakan waktu tinggi, sedangkan AI generatif murni tidak memiliki insting fisiologis.
- **Keputusan Terpilih**: 
  1. **Locomotion Periodik (Idle/Walk/Run)**: Dijalankan via *Procedural Sinusoidal Gait Function*, *Blend Trees*, dan *Inverse Kinematics (IK Foot Adjustment)* pada kontur lantai dungeon.
  2. **Secondary Motion (Syal Aina & Jubah)**: Dijalankan via *UE5 Chaos Cloth & 5-Bone Spring Chain* (Stiffness: 0.4–0.6, Damping: 0.3–0.5).
  3. **Transisi State**: Dihaluskan menggunakan *Animation Blueprint State Machines* dan *Easing Curves*.
  4. **Aksi Reaktif One-Shot (Punch, Cursed Strike, Hurt, Death)**: Menggunakan *Keyframe Animation + Hit-Stop 3 frame*.
- **Dampak**: Karakter terasa berbobot, hidup, dan responsif terhadap input pemain di ruang 3D.

### ADR-010: Arsitektur State-Driven untuk Fitur Khusus Lentera Pudar
- **Tanggal**: 2026-08-15
- **Status**: Accepted (Standard Baku — Diadaptasi ke UE5)
- **Konteks**: Elemen kunci lore seperti Syal yang memendek, tangan es yang berdenyut sesuai kutukan, dan penglihatan memori masa lalu membutuhkan jembatan langsung antara variabel gameplay dan representasi visual.
- **Keputusan Terpilih**: 
  1. **The Fading Scarf**: Dikelola sebagai *4 Stages of Sacrifice* pada simulasi kain dinamis syal.
  2. **Cursed Ice Arm Shader (`M_Cursed_Crystal`)**: Shader dinamis terhubung ke parameter `Curse_Spread` pada *Material Parameter Collection (MPC)* yang merespons real-time pada rentang 0 s.d. 100 poin.
  3. **Echoes of the Past & Spectral View**: Transisi lingkungan melalui *Perception Eyepatch Mode* dengan *Post-Process Material* dan *World Position Offset*.
- **Dampak**: Integrasi penuh antara narasi psikologis dan sistem engine tanpa spaghetti code.

### ADR-011: Standar Domain Baru (Pencahayaan Kelvin, Kamera Adaptif, Audio Spasial)
- **Tanggal**: 2026-08-15
- **Status**: Accepted (Standard Baku — Diadaptasi ke UE5)
- **Konteks**: Memastikan aspek visual pencahayaan, navigasi kamera, atmosfer audio, dan bos khusus memiliki landasan teori numerik terukur.
- **Keputusan Terpilih**: 
  1. **Lighting Theory**: Menggunakan skala temperatur Kelvin (2700K Warm Light `#F4B860` 800–1200 lm vs 6500K Cold Shard `#4A6FA5`), pencahayaan dinamis Lumen GI, rasio chiaroscuro 8:1 s.d. 12:1, dan desaturasi global di Sektor 4.
  2. **Camera Theory**: *Adaptive Dynamic Camera Stance* (FOV 78° eksplorasi vs FOV 70° lock-on duel over-the-shoulder) dengan *Collision Avoidance Buffer* 15–25cm.
  3. **Audio Theory**: Hirarki bus terstruktur (`Master ➔ Music / SFX / Voice`), *Target Loudness -16 LUFS*, *Dynamic Ducking -6dB* saat bisikan, dan *3D Binaural Whispers*.
  4. **AI The Hollow Reflection**: Menggunakan *Circular Input Replay Buffer* dengan frame-delay sebagai pengatur tingkat kesulitan.
- **Dampak**: Presentasi game terasa kohesif, mendalam, dan berkualitas AAA.

### ADR-012: Fondasi Infrastruktur Produksi & Ekosistem Game
- **Tanggal**: 2026-08-15
- **Status**: Accepted (Standard Baku)
- **Konteks**: Memastikan stabilitas repositori kode, kemudahan pengujian sistem non-visual, dan kelancaran narasi percabangan.
- **Keputusan Terpilih**: 
  1. **Version Control**: Git dengan konfigurasi **Git LFS** aktif untuk file biner besar (`.blend`, `.fbx`, `.uasset`, `.wav`).
  2. **Quality Control Standard**: Menerapkan **The 4-Tier Commercial Gate & 6 Pilar Definition of Done (DoD)** untuk memastikan kelayakan rilis komersial di Steam/PC.
- **Dampak**: Proses pengembangan terukur, data save aman dari crash/power-loss, zero regression bug, dan siap rilis komersial di Steam.

---

### ADR-013: Transisi Total Menuju 3D Action RPG (Unreal Engine 5 + Blender 5.2 LTS)
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master Strategic Pivot)
- **Konteks**: Pendekatan 2D pixel top-down memerlukan penggambaran frame-by-frame manual yang sangat masif (terutama dengan asimetri kompleks Kaelen: lengan kiri kristal es, eyepatch kanan, syal mengalir), sehingga membatasi keluwesan animasi dan kecepatan produksi.
- **Keputusan Terpilih**: 
  1. **Peralihan Engine**: Berpindah dari 2D/Godot menuju **3D Action RPG (Unreal Engine 5)**.
  2. **Pipeline Visual**: Menggunakan **Blender 5.2 LTS** sebagai pusat pemodelan 3D High-Detail (gaya anime/stylized ala *Final Fantasy VII Remake / Crisis Core*), biomechanical rigging, dan animasi 3D 360°.
  3. **Pembersihan Ekosistem 2D**: Menghapus seluruh artifak, skrip generator, spritesheet 2D, shader pixelation, dan konfigurasi MCP yang tidak relevan (Aseprite, Pixellab, Godot), dan memusatkan fokus alat pada **Blender 5.2 LTS + Unreal Engine 5**.
- **Dampak**: 
  - Model 3D Kaelen dimodelkan satu kali secara high-detail dan dapat dianimasikan bebas ke seluruh sudut 360 derajat.
  - Syal Aina dan jubah dapat memanfaatkan simulasi fisika kain (*Cloth Physics & Spring Bones*) dinamis secara real-time.
  - Pencahayaan lentera 2700K dan pendaran kristal es kutukan 6500K menghasilkan kualitas visual 3D AAA di Unreal Engine 5.

---

### ADR-014: Arsitektur Dual-Layer (Kena Visual + Hellblade Gameplay/Psikologi) & Sistem Diegetik
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master System Architecture)
- **Konteks**: Mencegah percampuran gaya yang membingungkan antara estetika visual dan kedalaman gameplay emosional.
- **Keputusan Terpilih**: 
  1. **Layer 1: Visual & Environment (Kena: Bridge of Spirits)**: Menentukan estetika 3D stylized-realistic (proporsi 1:6.8), pencahayaan Kelvin kontras tinggi (2700K vs 6500K), reruntuhan organik kuno, dan partikel restorasi hangat (*Niagara Warmth Embers*).
  2. **Layer 2: Gameplay & Psikologi (Hellblade: Senua's Sacrifice & II)**: Menentukan sistem psikologis diegetik (rambatan es fisik di tubuh menggantikan bar UI, kompas emosional syal menggantikan minimap), audio 3D binaural whispers, live mental morphing environment, dan combat 1v1 deliberate parry-focused.
  3. **Mekanik Persepsi Eyepatch (*The Eye of Frost / Temptation of Sight*)**: Penutup mata kanan berfungsi sebagai saklar penglihatan spektral dengan sistem *Risk-Reward* (membuka mata meningkatkan Curse Meter & bisikan jiwa beku).
  4. **Kamera Adaptif (*Adaptive Dynamic Stance*)**: Kamera berjarak bebas saat eksplorasi (FOV 78°), dan otomatis mendekat intimate over-shoulder saat Lock-On / Boss Duel / Parry (FOV 70°).
- **Dampak**: Visi visual dan mekanik terpisah dengan tegas, memberikan identitas unik yang sangat puitis, cantik secara visual, namun berat dan menegangkan saat dimainkan.

---

### ADR-015: Standardisasi Tools/MCP Stack & Kerangka 6-DoD Stage-Gate QA/QC
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master Production Standard)
- **Konteks**: Memastikan alur eksekusi AI Agent terikat pada toolset nyata yang teruji dan memiliki kriteria penerimaan kualitas (Quality Gate) yang tidak ambigu sebelum masuk ke fase rilis komersial.
- **Keputusan Terpilih**: 
  1. **Toolset & MCP Stack**: Menetapkan rantai alat resmi: Blender 5.2 LTS (MCP port 8097) + Unreal Engine 5 (Python Editor Scripting MCP) + Substance 3D (Texturing) + Wwise/MetaSounds (Audio) + Quixel (Megascans).
  2. **Enam Pilar Definition of Done (DoD)**: Standar verifikasi eksplisit untuk Model 3D, Material/Shader, Rigging & Animasi, Audio Spasial, Level Sektor, dan Sistem Gameplay.
  3. **The 8-Stage Gate Process**: Transisi proyek dari Gate 0 (Pra-Produksi) hingga Gate 7 (Release Candidate) dengan syarat mutlak lolos review fisik.
  4. **Klasifikasi Bug 4-Tier**: Pengelompokan bug berbasis severity (Blocking, Critical, Major, Minor) dengan aturan penanganan ketat.
- **Dampak**: Seluruh sub-agent AI dan developer memiliki parameter kelayakan yang objektif, mencegah cacat aset lolos ke build rilis, dan menjaga pipeline produksi tetap stabil.

---

### ADR-016: Standardisasi Parameter Presisi Numerik (Style Guide Numerik)
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master Numeric Standard)
- **Konteks**: Mencegah deviasi nilai, tebakan acak, atau inkonsistensi parameter shader, lighting, timing animasi, cloth physics, dan audio pada setiap sesi kerja AI Agent.
- **Keputusan Terpilih**: 
  1. **Color & Lighting Metrics**: Standar hex sekunder (Kulit `#D8B79A`, Rambut `#C9CDD1`), PointLight Lumen Syal 800–1200 lm (3–5m / 1.5–2.5m S4), Chiaroscuro 8:1 ke 12:1, dan desaturasi global 100% S1 ke 40–50% S4.
  2. **Material & Emissive (MPC)**: Subsurface Scattering (Radius 0.5–1.2cm, Scatter `#7EE8FA`) dan kurva intensitas emissive Curse Meter (0.5–1.0 s.d. 8.0–12.0 pulse 2–3Hz).
  3. **Chaos Cloth & Spring Damper**: Syal Aina (Stiffness 0.4–0.6, Damping 0.3–0.5, Wind 1.2x) vs Jubah Kaelen (Stiffness 0.6–0.8, Damping 0.5–0.7, Wind 0.8x).
  4. **Combat Timing & Curse Limits**: Light (3–5f startup), Heavy (12–18f), Dash (8–10f i-frames), Parry (4–6f @30fps / 8–12f @60fps), Hitstop (3-frame), dan Curse Meter 100 poin (+8–15 per hit, decay 2–4/s, Surge 90).
  5. **Audio & Poly Budget**: Loudness -16 LUFS (Combat BGM) / -18 LUFS (Dialog) dengan Ducking -6dB (150ms attack, 400ms release), Hero Poly Budget 40k–60k tris (LOD0–LOD3).
- **Dampak**: AI Agent dan sistem engine memiliki angka pasti yang terverifikasi, menjamin konsistensi visual dan gameplay feel di seluruh sesi kerja.

---

### ADR-017: Standardisasi SOP Operasional, Kalibrasi Few-Shot, & Kurasi Reference Board
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master Operational Standard)
- **Konteks**: Menghubungkan prinsip konseptual (GDD/Teori) dan angka pasti (Style Guide) ke dalam algoritma eksekusi operasional harian yang bebas dari tebakan, bias halusinasi, dan klaim subjektif.
- **Keputusan Terpilih**: 
  1. **Tujuh Prosedur Operasional Standar (SOP 1 s.d. SOP 7)**: Menetapkan langkah sekuensial baku untuk Pembuatan Prop, Setup Material PBR/MPC, Rigging Humanoid & Spring Bones, Chaos Cloth Simulation, Level Construction (Grey-Box ➔ Detailing), Combat FSM / GAS Blueprint, dan Audio Spasial 3D Binaural.
  2. **Standar Kalibrasi Few-Shot**: Mewajibkan seluruh AI Agent melakukan penilaian mandiri (*Self-Correction*) menggunakan 6 benchmark perbandingan konkret (*Salah vs Benar*) sebelum melapor selesai.
  3. **Struktur Reference Image Board (9 Kategori)**: Memformalkan struktur shot-list legal 9 kategori (`01_palet_warna_kontras` s.d. `09_minimal_hud`) sebagai acuan visual berbasis PureRef/Figma.
  4. **Protokol Gap-Handling Eksplisit**: Mengunci aturan bahwa kebutuhan di luar dokumen wajib ditandai sebagai GAP terukur dan dilarang diimprovisasi secara diam-diam.
- **Dampak**: Eksekusi multi-agent dan developer memiliki resep operasional baku yang deterministik, menutup celah halusinasi, dan menjamin hasil kerja selalu lolos 6 Pilar DoD.

---

### ADR-018: Standardisasi Pipeline 3D Art Kena-Grade (Hybrid Hair, Dual-Mode Scarf, & Render Target Thawing)
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master Technical Art Decision)
- **Konteks**: Mematangkan fidelity visual 3D dan efisiensi produksi dengan mengadopsi cetak biru industri dari studio Ember Lab (*Kena: Bridge of Spirits*).
- **Keputusan Terpilih**: 
  1. **Stylized-Realistic PBR Tanpa Outline**: Menetapkan visual bebas garis hitam (*zero black outline / non-cel-shaded*), memisahkan siluet melalui kontras temperatur Kelvin (2700K vs 6500K) dan micro-surface texturing.
  2. **Hybrid Hair System**: Rambut perak Kaelen (`#C9CDD1`) dimodelkan dengan perpaduan *Solid Geometry* (massa volume utama) + *Alpha Strip Cards* (helai acak alami) untuk visual tajam dan hemat komputasi.
  3. **Dual-Mode Scarf Animation**: Mengadopsi kombinasi *UE5 Chaos Cloth Simulation* untuk gameplay aksi 60 FPS dan *Hand-Keyframed Control Rig* untuk cutscene naratif Altar Duka.
  4. **Render Target Mask Dynamic Thawing**: Mengadopsi mekanisme *Deadzone Regrowth* Kena untuk pencairan lapisan es secara live di Altar Duka via Render Target projection.
  5. **Subsurface Scattering Ganda**: Menerapkan SSS pada kristal es (`#7EE8FA` radius 0.5–1.2cm) dan profil SSS kulit manusia (`#D8B79A`) untuk mencegah *uncanny valley*.
- **Dampak**: Kualitas visual 3D setara standar komersial papan atas (*Pixar-like interactive fantasy*), kinerja runtime stabil di 60 FPS, dan adegan Altar Duka memiliki dampak emosional sinematik maksimal.

---

### ADR-019: Standardisasi Biomekanika, Kinesiologi Gerak, Bony Landmarks & Corrective Morphing
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master Biomechanical Standard)
- **Konteks**: Menghindari kelemahan visual animasi 3D umum seperti pukulan tanpa bobot (*weightless punch*), hilangnya volume sendi saat tekukan ekstrem (*volume collapse*), dan lokomosi kaku tanpa dinamika tubuh alami.
- **Keputusan Terpilih**: 
  1. **Titik Rujukan Tulang Baku (Bony Landmarks)**: Mengunci posisi Acromion, Clavicle, Olecranon, Iliac Crest, Greater Trochanter, Patella, dan Malleolus sebagai patokan anatomi permanen pada sculpting dan rigging.
  2. **Rantai Kinetik Kombat (Kinetic Chain)**: Seluruh serangan (Light/Heavy) wajib mengalirkan momentum dari kaki belakang ➔ panggul ➔ torsi tulang belakang ➔ scapula ➔ pergelangan tangan mengunci saat impact (hit-stop 3 frame).
  3. **Kinesiologi Lokomosi 8-Fase**: Mengadopsi 8 fase gait cycle manusia dengan kemiringan panggul (*Pelvic Tilt*), rotasi silang bahu-pinggul (*Counter-Rotation*), dan *Vertical Bobbing* alami.
  4. **Corrective Shape Keys (Pose-Driven Morphs)**: Menerapkan shape key pengoreksi volume pada siku 140° (+ Biceps Muscle Bulge), bahu, lutut, dan panggul untuk menjaga bentuk organik saat pose ekstrem.
  5. **Batas Rotasi Sendi (Joint Limits)**: Mengunci batasan anatomis (Siku 0°–145°, Lutut 0°–140°, Tulang Belakang $\pm 35^\circ–45^\circ$) di Control Rig UE5.
  6. **Bahasa Tubuh Emosional (Grief Archetypes)**: Mengadaptasi postur Kaelen (Contrapposto saat Idle, tegap di S1–2, bungkuk kyphotic di S4, tenang di S5).
- **Dampak**: Karakter Kaelen terasa berbobot, bernyawa, stabil secara fisiologis, dan bebas dari cacat geometri lipatan sendi.

---

### ADR-020: Standardisasi Tools Lanjutan, API Cheat Sheet, & Teknik Praktis 3D
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master Technical Decision)
- **Konteks**: Memperluas ekosistem tools resmi (Blender-Unreal Pipeline Plugin, ZBrush, Auto-Rig Pro, PCG Framework, Lightmass) serta menyediakan sintaks API anti-halusinasi dan teknik produksi praktis AAA (Trim Sheets, Texel Density, Modular Kit, LUTs).
- **Keputusan Terpilih**: 
  1. **Blender-Unreal Pipeline Plugin**: Mengadopsi addon resmi Epic Games untuk pipeline ekspor satu-klik langsung ke Content Browser UE5.
  2. **API Cheat Sheet Baku**: Menyediakan referensi sintaks terverifikasi untuk modul `bpy` dan `unreal` dengan protokol *Inspect-Before-Execute* (introspeksi `dir()` / `help()`).
  3. **Standar Texel Density**: Mengunci target $512\text{ px/m}$ untuk Hero & Boss, dan $256\text{ px/m}$ untuk Environment Props pada checklist DoD Model 3D.
  4. **Trim Sheets & Texture Atlasing**: Menggabungkan tekstur arsitektur dungeon menjadi trim sheet modular untuk menghemat VRAM dan draw call.
  5. **Modular Level Kit-Bashing (Grid 300cm)**: Menyusun geometri dungeon menggunakan modul grid konsisten $300\text{ cm}$.
  6. **Color Grading via Post-Process LUTs**: Mengaplikasikan desaturasi per sektor (100% di S1 ke 40–50% di S4) melalui 3D LUTs di PostProcessVolume.
- **Dampak**: Alur kerja multi-agent bebas dari kesalahan sintaks API fiktif, aset lingkungan teroptimasi secara profesional, dan tampilan visual antar sektor terkalibrasi secara sinematik.

---

### ADR-021: Standardisasi Matematika, Fisika Numerik Real-Time, & Psikologi Pemain Tingkat Lanjut (Expert Suite)
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master Scientific & Psychological Standard)
- **Konteks**: Mematangkan landasan kalkulasi rotasi, simulasi kain, perambatan retakan es, BRDF cahaya, dan manipulasi psikologi emosional duka agar seluruh sistem game didasari pemodelan ilmiah dan bukan tebakan intuitif.
- **Keputusan Terpilih**: 
  1. **Matematika Lanjutan**: Menetapkan penggunaan Quaternion SLERP untuk kamera, Arc-Length Reparameterized Splines dengan kontinuitas kelengkungan C2 untuk lorong dungeon, dan Fractional Brownian Motion (fBm) untuk procedural noise es.
  2. **Fisika Numerik XPBD & Voronoi**: Mengadopsi Extended Position-Based Dynamics (XPBD) untuk kain syal stabil, Lattice-Biased Voronoi Fracture untuk pecahan es prisma, dan Cook-Torrance GGX BRDF untuk respons optik es realistis.
  3. **Psikologi Naratif & SDT**: Memverifikasi mekanik game terhadap 3 Kebutuhan SDT (Autonomy, Competence, Relatedness), menolak motivasi crowding-out, dan menerapkan rasio Loss Aversion $2.5\text{x}$ pada pengorbanan permanen Syal Aina.
  4. **Emotional Bandwidth & Non-Linear Grief**: Menyelipkan jeda kontemplatif untuk mencegah kelelahan emosional dan mengizinkan gema (echoes) lintas sektor duka.
- **Dampak**: Gameplay, visual, audio, dan alur narasi memiliki dasar komputasi yang terbukti secara matematis dan psikologis, mengangkat kualitas Lentera Pudar ke standar karya komersial berkualitas tinggi.










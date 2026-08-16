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
  2. **Cursed Ice Arm Shader (`M_Cursed_Crystal`)**: Shader dinamis terhubung ke parameter scalar `Curse_Spread` pada *Material Parameter Collection (MPC)* dengan skala ternormalisasi $0.0\text{ s.d. } 1.0$ (dipetakan dari nilai gameplay `CurseMeter` $0\text{ s.d. } 100\text{ poin}$ via formula $\text{Curse\_Spread} = \text{CurseMeter} / 100.0$).
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

---

### ADR-022: Standardisasi Kreativitas, Nilai Seni & Evaluasi Estetika Tingkat Lanjut (Expert Art & Aesthetic Framework)
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master Artistic & Aesthetic Standard)
- **Konteks**: Memastikan output visual, desain karakter, level lighting, sinematografi, dan simbolisme naratif dinilai menggunakan kriteria estetika formal yang kuat, bukan hanya kebenaran teknis atau selera subjektif.
- **Keputusan Terpilih**: 
  1. **Value-First Grayscale Mandate**: Setiap komposisi visual dan shot kamera wajib lolos uji kontras terang-gelap dalam mode monokrom hitam-putih sebelum warna dievaluasi.
  2. **Rasio Dominasi Warna 60-30-10**: Menerapkan proporsi terstruktur (60% netral gelap `#2A211C`, 30% biru dingin `#4A6FA5`/`#7EE8FA`, 10% kuning hangat `#F4B860`) dengan indirect color bleed via Lumen.
  3. **Siluet & Readability Murni**: Menetapkan keterbacaan instan telegraph musuh dari siluet hitam-putih murni tanpa bergantung pada efek partikel VFX.
  4. **Triad Kritik Seni (Unity, Tension, Resolution)**: Menjadikan tiga pilar formal ini sebagai checklist visual self-review loop AI agent.
  5. **Semiotika Visual Kumulatif**: Mengunci makna simbolis Syal Aina (pengorbanan terkikis), Retakan Es (kerapuhan batin), dan Cahaya Lentera (harapan) secara konsisten.
- **Dampak**: Kualitas visual semesta Lentera Pudar memiliki daya pikat artistik tinggi (*high artistic resonance*), konsistensi gaya Kena yang terjaga, serta bobot sinematik yang mendalam.

---

### ADR-023: Standardisasi Metodologi Kerja, Grounding Anti-Halusinasi & Protokol Berpikir AI Expert (Expert AI Methodology Framework)
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master AI Behavioral & Methodological Standard)
- **Konteks**: Menetapkan etika kerja, disiplin logika, dan protokol operasional AI agent agar bekerja murni sebagai alat produksi profesional yang akurat, transparan, bebas halusinasi, dan sistematis.
- **Keputusan Terpilih**: 
  1. **Anti-Roleplay Production Mandate**: Menghilangkan respons teatrikal/roleplay berlebihan saat mengerjakan tugas teknis; gaya naratif hanya diizinkan untuk deliverable konten in-game.
  2. **Grounding 3-Sumber & Anti-Halusinasi**: Seluruh klaim wajib bersumber dari dokumen master, introspeksi API aktif, atau observasi konkret; saat tidak tahu, wajib mencari dan memverifikasi aktif.
  3. **Problem Decomposition & Self-Verification**: Memecah tugas kompleks menjadi sub-langkah bertahap dan menjalankan verifikasi fisik sebelum menyatakan selesai.
  4. **Isolasi Variabel Debugging**: Mengubah tepat satu variabel dalam satu waktu saat troubleshooting teknis (Blender/UE5).
  5. **Pelaporan Jujur & Meta-Kognisi**: Menyajikan progress aktual secara transparan termasuk asumsi dan blocker aktif tanpa membulatkan status secara semu.
- **Dampak**: Seluruh kolaborasi AI agent dan asisten teknis berjalan dengan integritas tinggi, zero fatal errors, dan hasil produksi yang dapat diandalkan secara komersial.

---

### ADR-024: Standardisasi Teori Fondasi 3D Expert (Topology, UV Seam, PBR Shading, Rigging Deformation, LOD & Baking Pipeline)
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master 3D Technical & Theoretical Standard)
- **Konteks**: Menetapkan pemahaman mendalam mengenai alasan ilmiah dan mekanika di balik topologi edge flow, penempatan UV seam, sifat fisik PBR shading, skinning weight & corrective morphs, LOD siluet, dan baking normal/AO presisi.
- **Keputusan Terpilih**: 
  1. **Topologi Berorientasi Deformasi**: Mengharuskan edge flow mengikuti serat otot/sendi, larangan N-gon pada area gerak, dan penempatan pole strategis di area statis.
  2. **Penempatan UV Seam Tersembunyi**: Menempatkan potongan UV pada lipatan anatomi dalam, perbatasan material, atau kurvatur tajam demi meminimalkan distorsi.
  3. **Integritas Shading PBR**: Albedo murni tanpa baked lighting, Metallic biner 0/1, variasi micro-roughness, dan multi-layer blending untuk dynamic thawing.
  4. **Skinning & Corrective Morphs**: Total weight sum $=1.0$ (maksimal 4 bone influences/vertex), corrective shape keys pada siku 140° + biceps bulge, serta IK/FK switching fungsional.
  5. **LOD Berbasis Siluet & Baking Presisi**: Retensi siluet gameplay readability pada LOD, Tangent Space Normal Baking dengan Cage Mesh, dan pembatasan AO bake mikro agar tidak konflik dengan Lumen GI.
- **Dampak**: Seluruh aset 3D (Kaelen, Boss, Sektor Dungeon) terbebas dari artefak shading, kerutan deformasi patah, distorsi tekstur UV, dan penurunan performa komputasi.

---

### ADR-025: Standardisasi Master Index & Peta Navigasi Dokumentasi Pra-Produksi (Master Documentation Map)
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master Information Architecture Standard)
- **Konteks**: Menyediakan indeks master terpadu dan jalur navigasi rujukan baku agar seluruh AI agent dapat mengakses dokumen yang tepat tanpa redundansi konteks atau risiko kontradiksi internal.
- **Keputusan Terpilih**: 
  1. **Sentralisasi Rantai Rujukan**: Menetapkan `references/master-index.md` sebagai titik masuk resmi yang mengkategorisasikan seluruh 22 dokumen master ke dalam 5 domain utama.
  2. **Protokol Urutan Baca Baku**: Menetapkan urutan wajib baca bagi AI agent baru (Metodologi AI ➔ GDD/Lore ➔ Style Guide ➔ Domain Expert ➔ SOP/Few-Shot ➔ QA/QC).
  3. **Tautan Langsung & Zero Broken Links**: Seluruh rujukan dalam indeks terhubung langsung via tautan markdown lokal yang valid.
- **Dampak**: Efisiensi pencarian konteks meningkat drastis, eliminasi waktu membaca berulang, dan kepatuhan mutlak terhadap arsitektur hierarki dokumen proyek.

---

### ADR-026: Standardisasi Anatomi Ekspresi Wajah, FACS, & Bahasa Emosi Karakter (Facial Action Coding System & Emotional Gaze Framework)
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master Character Animation & Facial Rigging Standard)
- **Konteks**: Menetapkan pemodelan blend shape dan animasi ekspresi wajah berbasis Facial Action Coding System (FACS) untuk menyampaikan nuansa psikologis 5 Tahapan Berduka secara otentik tanpa dialog verbal berlebih.
- **Keputusan Terpilih**: 
  1. **Rigging Blend Shapes Berbasis Action Units (AU)**: Membangun shape keys individual (AU1, AU4, AU6, AU12, AU15, AU17, AU43) bukan preset emosi kaku.
  2. **Duchenne Marker & Senyum Bertopeng**: Membedakan senyum tulus (AU6+AU12) dengan senyum sosial/topeng (AU12 tanpa AU6) untuk menonjolkan kerapuhan emosional.
  3. **Asimetri Wajah & Ekspresi Mikro**: Mengintegrasikan 5–15% offset intensitas kiri-kanan wajah dan ekspresi mikro berdurasi 1/25–1/5 detik.
  4. **Pemisahan Kontrol Eye vs Mouth & Batas Rahang**: Memisahkan kontrol kelopak/mata dari mulut serta mengunci rotasi rahang (jaw pitch $\le 20^\circ$).
  5. **Dinamika Gaze & Eye-Tracking**: Mengimplementasikan 4 pola tatapan (Gaze aversion, lock, downward, drift) dengan parameter hold duration.
- **Dampak**: Wajah Kaelen dan Aina memiliki daya ungkap emosional mendalam (*high emotional nuance*), terhindar dari kesan kaku/*uncanny valley*, dan memperkuat resonansi naratif cutscene.

---

### ADR-027: Standardisasi Level Design & Environmental Storytelling (Spasial Duka, Breadcrumbing Diegetik, dan Simbiosis Arena FSM)
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master Level Design & Spatial Storytelling Standard)
- **Konteks**: Menetapkan arsitektur level 3D grey-box, penataan koridor dungeon, penempatan prop naratif, dan breadcrumbing visual diegetik agar ruang itu sendiri bercerita tanpa ketergantungan pada dialog verbal atau marker UI buatan.
- **Keputusan Terpilih**: 
  1. **Pemetaan Spasial 5 Tahap Berduka**: Merancang layout koridor (S1 simetris looping, S2 asimetris friksi tinggi, S3 labirin cermin waktu, S4 hampa descending, S5 lapang terbuka).
  2. **Diegetic Breadcrumbing & Minimal-HUD**: Menghapus seluruh marker UI buatan; navigasi dipandu oleh pendaran Syal Aina (`#F4B860`), jejak es mencair, dan pencahayaan chiaroscuro.
  3. **Rest Beats & Emotional Breathing Rooms**: Menyisipkan ruang hening kontemplatif setelah encounter kombat intens untuk memulihkan *emotional bandwidth* pemain.
  4. **Prop Naratif & The Power of Absence**: Menerapkan *Rule of Intentional Wear* sesuai lore dan memanfaatkan kekosongan objek (*absence storytelling*) untuk menyiratkan kehilangan mendalam.
  5. **Simbiosis Arena vs FSM Musuh**: Menyesuaikan dimensi arena secara presisi dengan arketipe kecerdasan buatan musuh (arena sempit untuk brawler melee vs arena berpilar untuk ranged caster).
- **Dampak**: Setiap jengkal dungeon *The Silent Crypts* hingga *The Dawning Altar* memiliki bobot naratif immersif, mendukung gameplay kombat deliberate 1v1, dan memperkuat arsitektur psikologis Hellblade-grade.

---

### ADR-028: Standardisasi Playtesting & Validasi Emosional (Intended vs Perceived Framework & Human Resonance Gap Analysis)
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master Emotional Quality Assurance Standard)
- **Konteks**: Menetapkan metodologi evaluasi dampak psikologis dan emosional duka terhadap pemain manusia sungguhan untuk memvalidasi bahwa kedalaman naratif tersampaikan secara efektif, bukan sekadar lolos uji teknis/fungsional.
- **Keputusan Terpilih**: 
  1. **Kerangka Intended vs Perceived Emotion**: Melakukan analisis kesenjangan (*gap analysis*) antara emosi desain dengan respon kualitatif playtester non-verbal/verbal.
  2. **Protokol Observasi Non-Intrusif**: Meminimalkan think-aloud selama bermain, mengamati bahasa tubuh/jeda hening alami, dan wawancara reflektif terbuka pasca-sesi.
  3. **Indikator Spesifik per Sektor Duka**: Mengevaluasi keberhasilan transmisi emosi (S1 keraguan simbolik, S2 intensitas tombol, S4 keheningan kontemplatif, S5 ketenangan relaksasi).
  4. **Mandat Batasan Eksplisit AI Agent**: Kepatuhan teknis AI terhadap parameter desain tidak menggantikan validasi emosi manusia; wajib menandai status `[Needs Human Playtest Validation]`.
  5. **Prosedur Sesi 5-Tahap & Retensi Memori**: Menjalankan sesi unprimed 30–45 menit dengan evaluasi memori jangka panjang 1 minggu pasca-sesi.
- **Dampak**: Mencegah bias internal pengembang/AI, memastikan tema 5 Tahapan Berduka beresonansi kuat secara emosional, dan menjamin karya akhir mencapai standar puitis bertaraf internasional.

---

### ADR-029: Standardisasi Desain Musuh, Arketipe Duka & Balancing Kombat (Enemy Archetypes, Telegraphing Readability, & Mechanical Fun Guardrails)
- **Tanggal**: 2026-08-16
- **Status**: Accepted (Master Enemy Design & Combat Balancing Standard)
- **Konteks**: Menetapkan perancangan arketipe musuh sebagai representasi psikologis 5 Tahapan Berduka, kurva kesulitan encounter mikro, keterbacaan serangan (telegraphing), serta jaminan kepuasan mekanik agar combat tidak terasa membosankan.
- **Keputusan Terpilih**: 
  1. **Arketipe Duka Tematik**: Menolak musuh generik; merancang *The Echo* (Denial), *The Berserker* (Anger), *The Deceiver* (Bargaining), *The Weight* (Depression), dan *The Mirror* (Acceptance).
  2. **Kurva Kesulitan Encounter 4-Tahap**: Menerapkan siklus Onboarding ➔ Escalation ➔ Combo Archetypes ➔ Recovery Rest Beat.
  3. **Mandat Keterbacaan & Telegraphing**: Mengharuskan windup minimal 12–18 frame, perubahan siluet kontras instan, audio cues 3D spasial, dan sinyal otentik khusus The Echo.
  4. **Fun Guardrails (Anti-Boredom Mandate)**: Menjaga satisfaction dasar (hit-stop 3-frame, impact es retak, kontrol responsif) agar tema berat tidak mengurangi keseruan bertarung.
- **Dampak**: Pertempuran di semesta Lentera Pudar memiliki kedalaman psikologis, menuntut penguasaan parry deliberate, adil (*fair*), dan memuaskan untuk dimainkan.

---

### ADR-030: Standardisasi Arahan Sinematik, Pacing Cutscene & Bahasa Kamera Spasial (Cinematography Framework, AU Synchronization, & Seamless Transitions)
- **Tanggal**: 2026-08-17
- **Status**: Accepted (Master Cinematography & Cutscene Standard)
- **Konteks**: Menetapkan bahasa pergerakan kamera sebagai representasi kondisi mental Kaelen, integrasi seamless gameplay-to-cutscene, sinkronisasi presisi pemotongan shot ke FACS Action Units, dan pengaturan depth of field emosional.
- **Keputusan Terpilih**: 
  1. **Bahasa Kamera per Sektor Duka**: S1 simetris kaku (Denial), S2 handheld shake cepat (Anger), S3 Dutch angle rotasi (Bargaining), S4 long take lambat framing luas (Depression), S5 framing lapang stabil (Acceptance).
  2. **Transisi Seamless Anti-Hard Cut**: Menghilangkan hard-cut hitam menuju cutscene; kamera mengambil alih secara halus dari over-shoulder gameplay.
  3. **Cakupan 3-Shot & Sinkronisasi FACS AU**: Memastikan cakupan Wide, Medium, dan Close-Up dengan timing pemotongan presisi saat AU ekspresi wajah aktif (`AU1`, `AU4`, `AU17`).
  4. **Emotional Depth of Field & Silent Beats**: Memanfaatkan shallow DoF untuk isolasi intim personal dan menyisipkan jeda hening katarsis pada momen puncak duka.
- **Dampak**: Memastikan setiap cutscene dan momen sinematik memiliki kualitas pengarahan setara film naratif bertaraf internasional (*Hellblade Cinematic Benchmark*), memperkuat imersi psikologis tanpa memutus keterlibatan pemain.

---

### ADR-031: Standardisasi Arahan Vokal, Delivery Dialog & Sinkronisasi Subteks-FACS (Vocal Direction Framework, Subtext Priority, & Audio-Visual Unity)
- **Tanggal**: 2026-08-17
- **Status**: Accepted (Master Voice Direction & Audio-Visual Dialogue Standard)
- **Konteks**: Menetapkan arahan vokal aktor dan penulisan dialog berbasis subteks batin, karakteristik intonasi 5 sektor duka, serta sinkronisasi audio-visual presisi dengan FACS Action Units wajah.
- **Keputusan Terpilih**: 
  1. **Prioritas Subteks**: Arahan vokal didasarkan pada apa yang sebenarnya dirasakan dan ditahan karakter (*suppressed emotion*), bukan teks literal.
  2. **Distingsi Kritis Vokal Duka**: Membedakan intonasi *Denial* (tenang karena menahan badai emosi) vs *Acceptance* (tenang karena keikhlasan melepaskan).
  3. **Sinkronisasi Presisi Vokal-FACS**: Memadukan micro-pause vokal dengan micro-expressions wajah (1/25–1/5s), suara tercekat saat `AU17` (menahan tangis), dan penurunan proyeksi saat *gaze aversion*.
  4. **Vokalisasi Non-Verbal & Keheningan Bermakna**: Mengutamakan helaan napas, suara tertahan, dan *meaningful silence* dibanding dialog berlebihan.
  5. **Format Standar Lembar Voice Actor**: Menetapkan template 7 parameter (Line, Karakter, Sektor, Subteks, Tempo/Dinamika, Catatan Fisik/FACS, Tonal).
- **Dampak**: Menghasilkan delivery dialog yang hidup, natural, menyentuh batin, dan selaras sempurna secara audio-visual dengan animasi Control Rig wajah.

---

### ADR-032: Standardisasi UI/UX, Minimal-Diegetic HUD & Aksesibilitas Komprehensif (Diegetic UI Priority, Cognitive Load Reduction, Colorblind/Hearing Accessibility, & Localization-Ready Architecture)
- **Tanggal**: 2026-08-17
- **Status**: Accepted (Master UI/UX & Accessibility Standard)
- **Konteks**: Menetapkan arsitektur antarmuka pengguna minimalis diegetik guna mereduksi beban kognitif pemain serta menyediakan fitur aksesibilitas empatik yang komprehensif bagi pemain dengan berbagai kebutuhan khusus.
- **Keputusan Terpilih**: 
  1. **Prioritas UI Diegetik**: Mengintegrasikan indikator status utama langsung ke tubuh Kaelen (es lengan kiri & panjang fisik Syal Aina); HUD non-diegetik memudar otomatis.
  2. **Aksesibilitas Visual Inklusif**: Menyediakan filter buta warna (Protanopia, Deuteranopia, Tritanopia) yang diperkuat oleh bentuk simbol geometris unik, penskalaan teks, dan reduksi screen shake/flashing.
  3. **Aksesibilitas Auditori & Closed Captions**: Menyertakan closed captions vokal emosional non-verbal, alternatif visual untuk attack tell audio, dan slider audio independen.
  4. **Kontrol Adaptif & Assist Mode**: Remapping tombol penuh (termasuk skema satu tangan) dan opsi pelebaran parry window assist.
  5. **Arsitektur Siap Lokalisasi**: Menjamin text container adaptif (+40% ekspansi) dan larangan mutlak atas teks baked pada tekstur 3D.
- **Dampak**: Menjamin permainan dapat diakses secara nyaman dan setara oleh seluruh pemain di dunia tanpa mengorbankan integritas artistik dan imersi emosional.

---

### ADR-033: Standardisasi NPC Ambient, Kehidupan Lingkungan & World Awareness Lokal (Ambient World Life, Low-Cost High-Impact Believability, & Grief-Mapped Ecosystem)
- **Tanggal**: 2026-08-17
- **Status**: Accepted (Master Ambient World Life Standard)
- **Konteks**: Menetapkan lapisan keempat dunia game berupa kehidupan netral/ambient yang terus berjalan tanpa menunggu pemain, mempertegas kontras emosional antara dunia luar yang acuh dengan beban duka Kaelen.
- **Keputusan Terpilih**: 
  1. **Subordinasi Naratif & 3 Aturan Dasar**: Memastikan ambient life tidak mencuri fokus cerita, dipetakan ke 5 sektor duka, serta murah secara implementasi namun berbobot tinggi.
  2. **Rutinitas NPC Ambient**: Menerapkan 2–3 idle actions asinkron dengan kontak mata singkat sebelum memalingkan wajah (*aware state* halus).
  3. **Ekosistem Satwa & Reaktivitas Pasif**: Menghadirkan fauna latar (burung/serangga) yang perilakunya mencerminkan fase duka sektor (panik di Anger, tenang di Acceptance).
  4. **World Awareness & Persistensi Lokal**: Menjaga reruntuhan es tetap hancur dan jejak kaki di salju/abu bertahan selama sesi di sektor terkait.
  5. **Side Character Berkesan**: Merancang karakter sampingan sebagai cermin alternatif respons kehilangan melalui satu detail spesifik yang tajam.
- **Dampak**: Menciptakan dunia 3D yang terasa bernapas, hidup, dan memiliki bobot historis, memperkuat resonansi puitis duka Kaelen dan Aina.

---

### ADR-034: Standardisasi Sistem Progresi Naratif Kemampuan Kaelen per Sektor Duka (GRIS Model, Cumulative Utility, & Grief-Mapped Ability Framework)
- **Tanggal**: 2026-08-17
- **Status**: Accepted (Master Ability Progression Standard)
- **Konteks**: Menetapkan daftar definitif kemampuan baru Kaelen yang terbuka secara sekuensial melalui pengorbanan Syal Aina di tiap Altar Duka, menolak sistem skill tree generik dan menjamin utilitas kumulatif lintas sektor.
- **Keputusan Terpilih**: 
  1. **Model Progresi GRIS**: Menghubungkan setiap pembukaan kemampuan baru dengan penyalaan Altar Duka dan pemendekan permanen Syal Aina (*4 Stages of Sacrifice*).
  2. **Daftar 5 Kemampuan Spesifik per Sektor**:
     - S1 Denial ➔ *Retakan Penyangkalan* (GAS: `GA_ShatterStrike`, input: combo finisher `Light ➔ Light ➔ Light ➔ Heavy`, 0 Curse Cost, guaranteed guard break, frame data: startup 18f, active 8f, recovery 22f @30fps, destructible barriers).
     - S2 Anger ➔ *Pusaran Amarah Beku* (Surge thrust stagger, knockback area & gap-jump).
     - S3 Bargaining ➔ *Kilasan Cermin Waktu* (Reflective deflect proyektil 360° & puzzle optik).
     - S4 Depression ➔ *Jangkar Keheningan* (Ground slam anti-stagger, curse dampener 50%, & pijakan danau es).
     - S5 Acceptance ➔ *Percikan Fajar Abadi* (Frost-fire harmonization, pembersih kutukan instan, & pembuka gerbang Overworld).
  3. **Prinsip Utilitas Kumulatif (*No-Obsolete Rule*)**: Kemampuan sektor awal tetap aktif dan esensial dalam combat, puzzle, dan navigasi di sektor-sektor berikutnya.
  4. **Integrasi GAS & Biomekanika**: Seluruh kemampuan terikat ke GameplayAbility UE5 dengan kinematika rantai kinetik dan hit-stop 3 frame baku.
- **Dampak**: Memberikan imbalan mekanik dan katarsis emosional yang seimbang atas pengorbanan Aina, menciptakan variasi combat dan puzzle yang terus berkembang secara bermakna.

---

### ADR-035: Standardisasi Sistem Respawn Diegetik & Kegagalan Kombat Biasa (Diegetic Thawing, Safe Archway Checkpoints, & Curse Stabilization)
- **Tanggal**: 2026-08-17
- **Status**: Accepted (Master Combat Failure & Respawn Standard)
- **Konteks**: Menetapkan detail teknis loop kegagalan dan respawn saat Kaelen kalah dalam pertempuran koridor/kroco biasa (non-Freeze of Despair) agar tetap selaras secara diegetik dan bebas dari HUD teks game over generik.
- **Keputusan Terpilih**: 
  1. **Titik Respawn Aman**: Kaelen dibangkitkan pada *Encounter Threshold / Safe Archway* atau *Breather Room* terdekat sebelum ruangan pertempuran.
  2. **Transisi Visual Kalah (*Frost Glaze*)**: Tidak ada teks game over; kamera jatuh rendah, frost vignette glaze merambat cepat, audio muffle low-pass filter 400Hz, lalu fade to dark-blue `#141013` (1.5 detik).
  3. **Transisi Visual Respawn (*Dynamic Thawing & Breath*)**: Fade in memperlihatkan Kaelen bertumpu pada satu lutut, es di dada mencair kembali (*vertex thawing*), Syal Aina berkedip hangat 2x (2700K), dan desau napas lega (*soft exhalation*).
  4. **Penalti & Persistensi**: Curse Meter stabil pada 25% (tidak hilang total), formasi musuh di ruangan reset, namun reruntuhan dan destruksi lingkungan tetap hancur (*local persistence*).
  5. **Frekuensi Checkpoint**: 1 Major Checkpoint (Altar Duka) + 2–3 Minor Checkpoints (Breather Rooms) per sektor (interval 4–6 menit eksplorasi).
  6. **Pemulihan Breather Room**: Pengurangan Curse Meter pasif $-2\text{ poin/detik}$ dengan batas ambang dasar $25\%$ dan pendaran uap es mencair ke bara emas Aina.
  7. **Guardrails Teknis Edge-Case**: Imunitas interaksi cutscene Altar Duka (`State.Invulnerable`), batas aggro musuh (`BP_EncounterTriggerBoundary`), shader clamp $0.0 \le \text{Opacity} \le 1.0$, prioritas FSM Freeze of Despair (`Priority Level 1`), dan reset spektral otomatis (`ClearAllSpectralStates`) saat respawn.
- **Dampak**: Menjaga imersi emosional dan integritas artistik dunia tanpa menghukum pemain secara frustratif atau merusak atmosfer melankolis game.

---

### ADR-036: Standardisasi Skenario & Naskah Step-by-Step Tutorial Prolog Onboarding (Diegetic Walkthrough, Contextual Glyphs, & Fail-Safe Feedback)
- **Tanggal**: 2026-08-17
- **Status**: Accepted (Master Prologue Tutorial Standard)
- **Konteks**: Menetapkan naskah walkthrough terperinci langkah-demi-langkah pengenalan seluruh kontrol dan mekanik dasar dari detik pertama Kaelen membuka mata hingga memasuki gerbang Sektor 1, mematuhi prinsip Level as Tutorial tanpa teks instruksi panjang.
- **Keputusan Terpilih**: 
  1. **6 Langkah Onboarding Sekuensial**:
     - Step 1: Gerak Dasar & Cahaya Syal ➔ Ceruk Makam Gelap Gulita.
     - Step 2: Light Punch ➔ Stalagmit kristal es rapuh destructible.
     - Step 3: Heavy Cursed Ice Strike ➔ Lempengan es tebal (+10 Curse Meter feedback).
     - Step 4: 12-Frame Tight Parry ➔ Arena 1v1 terkontrol The Echo (windup 18f, hit-stop 3f, stagger 3s).
     - Step 5: Sealed Eye Perception ➔ Jurang buntu, jembatan memori es (+3 Curse/s).
     - Step 6: Altar Duka 1 Sacrifice ➔ Pemendekan Syal Tahap 1, unlock *Fracture of Denial*, gerbang S1 terbuka.
  2. **Tiga Komponen per Langkah**: Menyertakan Ruang/Setting, Trigger alami, dan Fail-Safe diegetik tanpa pesan kegagalan buatan.
  3. **Contextual Glyphs & Seamless Transition**: Petunjuk tombol hanya muncul lembut pada radius < 2m dan memudar seketika setelah interaksi berhasil.
- **Dampak**: Memastikan onboarding pemain berjalan mulus, imersif, dan terintegrasi penuh ke dalam sistem gameplay dan cerita sejak detik pertama.

---

### ADR-037: Mitigasi Risiko Desain, Penegakan SSoT & Standarisasi Pemulihan Breather Room (Landing Auto-Stop, Sector 4 Audit, Anti-RPG Guardrails, & Breather Thaw)
- **Tanggal**: 2026-08-17
- **Status**: Accepted (Master Risk Mitigation & Breather Recovery Standard)
- **Konteks**: Menindaklanjuti audit cross-check untuk memitigasi 3 risiko teridentifikasi (death spiral kutukan, risiko kebosanan Sektor 4, miskonsepsi RPG generik) serta menutup gap teknis pemulihan kutukan di Breather Room.
- **Keputusan Terpilih**: 
  1. **Landing Auto-Stop Trigger**: Laju kutukan $+3\text{ poin/detik}$ dari Sealed Eyepatch berhenti otomatis saat kaki Kaelen memasuki volume pendaratan platform (`BP_SpectralLandingZone: OnComponentBeginOverlap`), memicu animasi penutupan penutup mata otomatis.
  2. **Protokol Stage-Gate 5 Sektor 4**: Menetapkan distingsi observasi non-verbal antara *Solemn Engagement* (lolos: tubuh condong ke depan, respirasi tenang) vs *Disengaged Fatigue* (gagal: bersandar, gelisah, spam sprint) di `emotional-playtesting.md`.
  3. **Mandat Anti-RPG Konvensional**: Melarang keras skill tree bebas, stat STR/DEX/INT/leveling, dan loot table acak di `AGENTS.md` Bab 1.5 dan `theory-reference.md` Bab 1.E.
  4. **Pemulihan Curse Meter di Breather Room**: Ditetapkan laju pemulihan $-2\text{ poin/detik}$ dengan batas ambang dasar $25\%$ dan isyarat diegetik pendaran es meredup serta uap beku mencair menjadi bara emas Aina.
  5. **Konsolidasi Single Source of Truth (SSoT)**: Mengubah seluruh 29 file draf di root workspace menjadi tautan redirect bersih menuju folder `references/*.md`.
- **Dampak**: Memastikan seluruh sistem aman dari celah logika teknis dan kebingungan arsitektural, menjaga integritas puitis duka semesta Lentera Pudar.

---

### ADR-038: Standarisasi Spesifikasi Teknis The Freeze of Despair & Trauma Failure Loop (Layered Cutscenes, Anti-Fatigue Guardrail, Boss Reset, & 0% Curse Restoration)
- **Tanggal**: 2026-08-17
- **Status**: Accepted (Master Boss Failure & Trauma Loop Standard)
- **Konteks**: Melengkapi dan meresmikan guardrail teknis serta naratif untuk pemicuan kegagalan *The Freeze of Despair* saat pertempuran bos, membedakannya secara tegas dari sistem respawn combat kroco biasa (ADR-035).
- **Keputusan Terpilih**: 
  1. **Kondisi Pemicu**: 3x akumulasi Curse Meter 100% dalam satu pertempuran bos (`CurseOverloadCount == 3`).
  2. **Layered Narrative Pacing**: Penayangan sinematik penuh (8–10s, unskippable) pada pemicuan pertama; digantikan oleh *Abbreviated Trauma Whisper* (3s micro-fade) jika berulang pada bos yang sama untuk mencegah degradasi tempo/naratif (*anti-fatigue guardrail*).
  3. **Titik Respawn**: Depan *Boss Fog Gate* / *Major Checkpoint Altar Duka* terdekat di sektor tersebut.
  4. **Status & Reset**: Curse Meter disucikan ke 0% (bukan 25%), HP Kaelen 100%, HP Bos me-reset penuh 100% dan fase bos kembali ke Fase 1.
  5. **Guardrail Anti-Interupsi**: Tag GAS `State.TraumaCutsceneLock` & `State.Invulnerable`, penghentian AI bos instan (`DeactivateBehaviorTree`), dan eksekusi `ClearAllSpectralStates`.
- **Dampak**: Menjaga tensi psikologis kekalahan bos tetap bermakna, puitis, dan aman dari bug race condition kamera/input.



























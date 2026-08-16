# Referensi Teori Pendukung — Lentera Pudar (Master Theory Bible)
### Kerangka Teori Desain, Psikologi, Technical Art & Produksi untuk AI Agent (Blender 5.2 LTS + Unreal Engine 5)

Dokumen ini berisi kerangka teori komprehensif yang menjadi fondasi dan "bahasa bersama" (*The Why*) untuk proyek **Lentera Pudar: The First Spark**. Dokumen ini melengkapi Master GDD, Moodboard Referensi, dan Dokumen Visi Kreatif.

---

## DAFTAR ISI
1. [BAB 1: Teori Desain Game (Game Design Theory)](#1-teori-desain-game-game-design-theory)
2. [BAB 2: Teori Level Design](#2-teori-level-design)
3. [BAB 3: Teori Naratif (Narrative Design Theory)](#3-teori-naratif-narrative-design-theory)
4. [BAB 4: Teori Desain Combat](#4-teori-desain-combat)
5. [BAB 5: Teori Kamera & Sinematografi](#5-teori-kamera--sinematografi)
6. [BAB 6: Teori Warna & Pencahayaan](#6-teori-warna--pencahayaan)
7. [BAB 7: Teori Audio](#7-teori-audio)
8. [BAB 8: Teori UI/UX](#8-teori-uiux)
9. [BAB 9: Teori Animasi](#9-teori-animasi)
10. [BAB 10: Teori Rigging & Simulasi Kain](#10-teori-rigging--simulasi-kain)
11. [BAB 11: Teori Shader & Material (Technical Art)](#11-teori-shader--material-technical-art)
12. [BAB 12: Teori Balancing & Progresi Sistem](#12-teori-balancing--progresi-sistem)
13. [BAB 13: Teori Fisika Tingkat Lanjut (Terapan Real-Time Engine)](#13-teori-fisika-tingkat-lanjut-terapan-untuk-real-time-engine)
14. [BAB 14: Teori Matematika Tingkat Lanjut (Terapan)](#14-teori-matematika-tingkat-lanjut-terapan)
15. [BAB 15: Teori Psikologi Pemain (Player Psychology)](#15-teori-psikologi-pemain-player-psychology)
16. [BAB 16: Teori Tambahan yang Layak Dipertimbangkan](#16-teori-tambahan-yang-layak-dipertimbangkan)
17. [BAB 17: Teori Produksi & Pipeline Teknis](#17-teori-produksi--pipeline-teknis-sering-terlupakan-tapi-krusial)
18. [BAB 18: Teori Tambahan Lain (Penutup Cakupan Produksi)](#18-teori-tambahan-lain-penutup-cakupan-produksi)
19. [BAB 19: Cara Penggunaan Dokumen Ini untuk AI Agent](#19-cara-memberikan-dokumen-ini-ke-ai-agent)

---

## 1. Teori Desain Game (Game Design Theory)

### A. MDA Framework (Mechanics – Dynamics – Aesthetics)
Kerangka dasar: **Mechanics** (aturan & sistem mentah — Curse Meter, combo attack) menghasilkan **Dynamics** (perilaku pemain saat bermain — kapan pemain memilih menyerang vs menghindar) yang menghasilkan **Aesthetics** (pengalaman emosional akhir — rasa melankolis, tekanan, lega). Agent perlu memahami bahwa tiap mekanik yang dibangun di Blender/UE5 harus ditelusuri balik ke Aesthetic yang diinginkan (dalam kasus ini: melankolis-hangat), bukan dibangun demi kompleksitas semata.

### B. Core Loop & Feedback Loop
Setiap game punya loop inti yang berulang (eksplorasi → pertarungan → hadiah/progres naratif → eksplorasi lagi). Untuk Lentera Pudar: **Jelajah dungeon → hadapi jiwa beku/musuh → nyalakan Altar Duka → syal memendek (biaya) → dapat kemampuan baru (hadiah) → lanjut sektor.** Agent perlu menjaga *tight feedback loop* ini — tiap aksi pemain harus punya konsekuensi yang terasa dalam waktu singkat, bukan tertunda terlalu lama.

### C. Flow Theory (Csikszentmihalyi)
Pemain tetap terlibat saat tantangan seimbang dengan skill mereka — tidak terlalu mudah (bosan) atau terlalu sulit (frustrasi/cemas). Kurva kesulitan tiap sektor (Denial → Acceptance) sebaiknya naik bertahap, dengan boss sebagai puncak lokal, lalu sedikit penurunan tensi di awal sektor berikutnya sebagai jeda napas sebelum naik lagi.

### D. Reward Schedule & Player Motivation
Ada reward *intrinsik* (kepuasan menuntaskan mekanik parry sulit) dan *ekstrinsik* (kemampuan baru sekuensial). Untuk game bertema grief seperti ini, reward condong ke intrinsik/naratif (potongan memori, dialog, perubahan visual dunia) dibanding sekadar loot — supaya tetap konsisten dengan nuansa "poetic dark fantasy", bukan grinding RPG biasa.

### E. Batasan Eksplisit: Larangan Mekanik RPG Konvensional
Untuk menjaga integritas emosional semesta Lentera Pudar, sistem progresi secara tegas MELARANG:
1. **Free-Form Skill Tree**: Kemampuan baru murni terbuka sekuensial via Model GRIS di 5 Altar Duka.
2. **Stat Leveling Numerik (STR, DEX, INT, Level 1..99)**: Kaelen mengandalkan pembacaan telegraf kinetik dan penguasaan timing pemain, bukan akumulasi angka statistik.
3. **Loot Drop Acak & Grinding Koin**: Tidak ada mata uang emas, grinding monster berulang, atau gacha item.

---

## 2. Teori Level Design

### A. Teaching Through Geometry (Level as Tutorial)
Bentuk lorong, penempatan cahaya, dan reruntuhan bisa "mengajari" pemain tanpa teks. Contoh: lorong sempit dengan satu sumber cahaya di ujung secara naluriah mengarahkan pemain maju — ini prinsip dari level design modern (dipopulerkan lewat analisis level Half-Life/Uncharted).

### B. Critical Path vs Optional Path
Setiap sektor idealnya punya *critical path* (rute wajib ke boss) dan *optional path* (area tersembunyi via mekanik eyepatch/perception, sesuai moodboard Hellblade). Agent perlu membedakan geometry mana yang wajib dilalui vs opsional saat membangun layout di Blender, supaya level tidak membingungkan pemain soal ke mana harus pergi.

### C. Sightlines & Landmarking
Pemain menavigasi dungeon besar lewat *landmark* visual yang terlihat dari jauh (menara, cahaya syal, struktur unik). Setiap sektor sebaiknya punya satu landmark dominan yang terlihat dari banyak titik, supaya pemain tidak tersesat tanpa perlu minimap besar — selaras dengan pendekatan minimal-HUD ala Hellblade yang sudah kamu pilih.

### D. Pacing melalui Ritme Ruang (Combat Arena vs Breather Room)
Selingi ruang pertempuran intens dengan "breather room" — area tenang untuk npc dialog, checkpoint, atau sekadar jeda visual. Ini penting khusus untuk game bertema berat (grief/trauma) supaya pemain tidak lelah secara emosional terus-menerus.

---

## 3. Teori Naratif (Narrative Design Theory)

### A. Environmental Storytelling
Cerita disampaikan lewat detail lingkungan (pose patung beku, susunan barang di reruntuhan, coretan dinding) tanpa dialog eksplisit — cocok untuk *The Silent Crypts* dan *Hall of Mirrors*. Agent bisa diberi instruksi eksplisit: "tiap prop di sektor ini harus menyiratkan potongan cerita penghuni sebelumnya."

### B. Show, Don't Tell
Terapkan terutama pada momen pengorbanan syal Aina — biarkan visual (syal memendek, cahaya meredup, ekspresi wajah Kaelen) berbicara tanpa banyak dialog penjelas, sesuai gaya kamera dekat ala Hellblade II yang sudah dipilih di moodboard.

### C. Kübler-Ross Model (5 Stages of Grief) sebagai Struktur Naratif
Sudah jadi fondasi struktur 5 sektor kamu. Prinsip pentingnya: tiap tahap grief bukan linear murni di kehidupan nyata (orang bisa bolak-balik antar tahap) — pertimbangkan momen kecil "relapse" tematik di sektor akhir (mis. elemen Denial muncul sekilas di sektor Acceptance) supaya terasa psikologis, bukan sekadar checklist 5 level.

### D. Character Arc Theory (Internal vs External Goal)
Kaelen punya *external goal* (menerangi dungeon, mencapai puncak) dan *internal goal* (menerima rasa sakitnya sendiri). Ketegangan dramatis muncul saat dua goal ini bertentangan — misalnya pemain "ingin" menyelamatkan lebih banyak jiwa beku (external), tapi tiap penyelamatan mempercepat habisnya syal Aina (cost personal/internal).

---

## 4. Teori Desain Combat

### A. Telegraphing & Readability
Musuh harus punya *tell* visual jelas sebelum menyerang (wind-up animation, perubahan warna, particle effect) supaya pemain punya waktu bereaksi. Penting terutama untuk kristal es besar/boss agar terasa adil meski sulit.

### B. Hitstop & Juice
"Hitstop" (jeda singkat sepersekian detik saat pukulan kena) dan efek visual/audio pendukung ("juice" — screen shake kecil, particle pecah, sound impact) membuat combat terasa berat dan memuaskan meski sistem di baliknya sederhana. Relevan untuk *Bare Hand Punch Combo* dan *Cursed Ice Strike* Kaelen.

### C. Poise/Stagger System
Selain HP, musuh (dan mungkin Kaelen) bisa punya meter "keseimbangan" — kena serangan cukup banyak → stagger → window damage besar terbuka. Ini menambah kedalaman taktis tanpa perlu combo mashing kompleks, cocok dengan filosofi "berat di timing" ala Hellblade.

### D. Risk-Reward Loop pada Curse Meter Surge
Prinsip dari sistem "berisiko-hadiah" umum di action game (mis. Devil Trigger DMC, Berserk mode): kekuatan besar sementara dengan risiko besar (mendekati "beku total"). Agent perlu tahu bahwa *Curse Meter Surge* bukan cuma damage buff biasa — harus terasa sebagai keputusan taktis yang menegangkan, bukan tombol "menang otomatis".

---

## 5. Teori Kamera & Sinematografi

### A. Third-Person Camera Rules
Kamera idealnya sedikit offset dari pusat karakter (rule of thirds), dengan *look-ahead* di arah gerak, dan collision-avoidance otomatis di ruang sempit dungeon supaya tidak clipping ke dinding.

### B. Kamera sebagai Alat Naratif (Hellblade II style)
Untuk momen emosional kunci (Altar Duka, boss intro, kematian jiwa beku), kamera bergerak dari third-person standar menjadi *close-up* dinamis pada wajah Kaelen — teknik ini datang dari bahasa sinematik film, dipakai untuk memaksa pemain fokus ke emosi, bukan aksi.

### C. Framing & Rule of Space
Saat Kaelen menghadapi boss, beri "ruang visual" di depan boss lebih besar dari di belakang Kaelen — teknik framing klasik yang membuat ancaman terasa dominan secara bawah sadar.

---

## 6. Teori Warna & Pencahayaan

### A. Color Temperature sebagai Bahasa Emosi
2700K (hangat, nyaman, manusiawi) vs 6500K (dingin, mati rasa, asing) — ini prinsip psikologi warna dasar yang sudah kamu terapkan dengan benar. Pastikan agent konsisten: elemen apa pun yang berhubungan dengan Aina/harapan selalu condong ke warna hangat, apa pun yang berhubungan dengan kutukan selalu condong ke warna dingin, tanpa pengecualian yang membingungkan pemain.

### B. Contrast Ratio sebagai Alat Fokus Perhatian
Area gelap pekat dengan satu titik cahaya terang (syal Aina) secara otomatis menarik mata pemain ke titik itu — teknik "chiaroscuro" dari seni lukis klasik, diadaptasi ke real-time lighting (relevan untuk gaya Lumen yang kamu pakai).

### C. Desaturasi Progresif sebagai Indikator State
Alih-alih UI meter murni, saturasi warna dunia bisa berkurang seiring Curse Meter naik — dunia terasa makin "mati rasa" secara visual, konsisten dengan tema Anhedonia di GDD kamu.

---

## 7. Teori Audio

### A. Diegetic vs Non-Diegetic Sound
Diegetic = suara yang "ada" di dunia game (langkah kaki, gema es retak, bisikan jiwa beku). Non-diegetic = musik latar/scoring yang hanya didengar pemain. Hellblade dikenal mengaburkan batas ini (bisikan terasa seperti datang dari dalam kepala Senua) — teknik ini bisa dipakai untuk bisikan jiwa-jiwa beku di Lentera Pudar.

### B. Binaural Audio
Teknik rekam/mixing yang membuat suara terasa datang dari arah/jarak spesifik saat memakai headphone — dipakai Hellblade untuk bisikan yang "mengelilingi" pemain. Perlu asset audio look ahead untuk arah suara sesuai posisi 3D sumbernya di level.

### C. Adaptive/Dynamic Music System
Musik berubah lapisan (menambah/mengurangi instrumen) berdasarkan state gameplay (eksplorasi tenang → mendekati musuh → combat penuh) tanpa cut kasar antar track — sudah disebut di GDD kamu, teorinya disebut *vertical layering* (layer ditambah/dikurangi) vs *horizontal re-sequencing* (pindah antar segmen musik berbeda).

---

## 8. Teori UI/UX

### A. Diegetic & Minimal HUD
UI yang menyatu ke dunia game (radius cahaya syal sebagai indikator kesehatan/state, alih-alih bar HP terpisah) mengurangi gangguan imersi — prinsip ini sudah kamu adopsi dari Hellblade dan penting dipegang konsisten di semua sistem UI, bukan cuma sebagian.

### B. Affordance
Desain visual objek harus "menyiratkan" fungsinya — pegangan pintu terlihat bisa dipegang, kristal es interaktif terlihat berbeda dari kristal es dekoratif (lewat glow/emissive) supaya pemain tidak bingung mana yang bisa berinteraksi.

### C. Feedback Loop Instan
Setiap input pemain (serangan, dash, buka eyepatch) perlu respons visual/audio dalam <100ms supaya terasa responsif — prinsip dasar UX yang berlaku juga untuk action game, bukan cuma aplikasi.

---

## 9. Teori Animasi & Kinesiologi Gerak Manusia

### A. 12 Prinsip Animasi Disney (Terapan 3D Real-Time)
- **Anticipation**: Gerakan persiapan sebelum aksi utama (Kaelen merendahkan panggul sebelum dash) — kunci readability combat.
- **Follow Through & Overlapping Action**: Syal Aina dan jubah Kaelen tidak berhenti bersamaan dengan tubuh (simulasi inersia kain).
- **Squash & Stretch**: Versi halus semi-realistis pada kompresi otot dan impact tumbukan cakar es.
- **Secondary Action**: Kibaran rambut perak dan percikan bara syal Aina memperkaya aksi utama.

### B. Rantai Kinetik Kombat (*Kinetic Chain & Momentum Transfer*)
Tenaga pukulan Kaelen mengalir dari tanah: `Ground Reaction Force kaki belakang ➔ Rotasi Panggul ➔ Torsi Tulang Belakang ➔ Scapula Protraction ➔ Ekstensi Siku ➔ Wrist Lock pada Impact Frame`. Memahami rantai kinetik ini menjelaskan mengapa *Heavy Cursed Strike* butuh startup 12–18 frame (waktu transfer momentum penuh) agar pukulan terasa berbobot (*weighty*).

### C. Kinesiologi 8-Fase Lokomosi (*Human Gait Cycle*)
Siklus jalan/lari Kaelen dibangun di atas 8 fase biomekanik: *Initial Contact (Heel Strike) ➔ Loading Response ➔ Midstance ➔ Terminal Stance ➔ Pre-Swing (Toe-off) ➔ Initial Swing ➔ Midswing ➔ Terminal Swing*.
- **Pelvic Tilt**: Panggul miring dinamis naik-turun mengikuti kaki tumpu vs melayang.
- **Counter-Rotation**: Torsi silang bahu berputar berlawanan panggul untuk keseimbangan alami.
- **Flight Phase**: Pembeda fundamental di mana lari/dash memiliki momen kedua kaki melayang di udara.

### D. IK (Inverse Kinematics) & Blend Trees
Kombinasi Two-Bone IK dan Control Rig untuk adaptasi telapak kaki pada lantai dungeon miring, dipadu *Blend Trees* berbasis kecepatan untuk transisi lokomosi halus tanpa snap.

---

## 10. Teori Rigging, Anatomi Deformasi & Simulasi Kain (Lihat [expert-3d-foundations.md](file:///d:/GodotProjects/Lentera-Pudar/references/expert-3d-foundations.md))

### A. Titik Rujukan Tulang Baku (*Bony Landmarks*)
Titik tulang permukaan yang wajib terbaca pada sculpt dan menjadi pivot bone rig: *Acromion & Clavicle* (bahu), *Olecranon* (siku), *Iliac Crest & Greater Trochanter* (panggul/hip), *Patella* (lutut), *Malleolus* (mata kaki), dan *Vertebra Prominens* (pangkal leher/postur).

### B. Deformasi Sendi & Corrective Shape Keys (Pose-Driven Morphs)
Mencegah penyusutan volume (*volume loss / collapsing joints*) saat tekukan ekstrem dengan weight sum $=1.0$ (maks 4 bone influence):
- **Siku (Elbow fleksi 140°)**: Corrective morph memulihkan volume lipatan dalam siku dan memicu *Muscle Bulging* pada otot bisep.
- **Bahu, Lutut & Pinggul**: Corrective morph menjaga tempurung patella dan tonjolan deltoid tetap kokoh saat kuda-kuda rendah.

### C. Batasan Rotasi Sendi Realistis (*Joint Constraint Limits*)
Kunci batasan rotasi anatomis di UE5 Control Rig: Siku (0°–145° anti-hyperextension), Lutut (0°–140° fleksi belakang), Tulang Belakang ($\pm 35^\circ–45^\circ$ per segmen), Leher ($\pm 80^\circ$ yaw).

### D. Skeleton Hierarchy, Spring Bones & Dual-Mode Strategy
Syal Aina memerlukan *spring bone chain* 5-tulang terpisah:
- **Mode Gameplay**: Digerakkan oleh simulasi fisika *UE5 Chaos Cloth Solver* untuk efisiensi komputasi runtime 60 FPS.
- **Mode Sinematik**: Digerakkan oleh *Hand-Keyframed Control Rig* agar animator memiliki kontrol ekspresi puitis mutlak pada cutscene emosional (Altar Duka & Boss Death).

### E. Cloth Simulation Constraints & Pinning
Simulasi kain butuh *pinning point* leher tetap dan parameter *stiffness/damping* (0.4–0.6 / 0.3–0.5) untuk inersia lentur alami.

### F. Hybrid Hair Geometry (Solid Mesh + Alpha Cards)
Memadukan **Solid Geometry** (bentuk massa volume utama) dengan **Alpha Cards** (strip helai transparan flyaways) untuk siluet anime bersih tanpa beban strand groom berlebih.

---

## 11. Teori Shader & Material Pipeline (Lihat [expert-3d-foundations.md](file:///d:/GodotProjects/Lentera-Pudar/references/expert-3d-foundations.md))

### A. PBR (Physically Based Rendering) & Zero Black Outline
Material di UE5 dibangun dari kombinasi *Base Color* (flat tanpa baked lighting), *Roughness*, *Metallic* (biner 0 atau 1), dan *Tangent Space Normal Map* dengan Cage ray-casting. Visual game adalah *Stylized-Realistic non-outline* (bukan cel-shading bergaris hitam).

### B. Subsurface Scattering (SSS) untuk Kulit & Kristal Es
Es tampak "hidup" karena cahaya menembus sedikit ke dalam material sebelum keluar lagi (bukan solid opaque) — parameter SSS radius 0.5–1.2cm penting untuk kristal es Kaelen (`#7EE8FA`) dan SSS Human Skin pada kulit (`#D8B79A`) agar terhindar dari kesan plastik *uncanny valley*.

### C. Emissive Material untuk Sumber Cahaya Bergaya
Syal Aina dan kristal kutukan memakai *emissive* yang terhubung ke parameter Curse Meter secara real-time via *Material Parameter Collection (MPC)* di UE5, bukan warna emissive statis — supaya perubahan intensitas terlihat halus, bukan on/off kasar.

### D. Niagara Particle System sebagai Bahasa Visual
Partikel bukan cuma dekorasi — di Lentera Pudar, partikel (bara api emas `FX_Warmth_Embers`, uap beku `FX_Frost_Mist`, dan percikan parry) berfungsi sebagai indikator status diegetik.

### E. Render Target Masking untuk Dynamic Environmental Restoration
Mengadopsi sistem *Deadzone Regrowth* Kena: transisi pencairan es saat Altar Duka dinyalakan dilakukan dengan menulis pemuaian mask ke **Render Target** secara live. Shader lantai mendeteksi mask ini untuk mentransisikan es retak menjadi batu kuno hangat secara organik, memicu interaksi partikel dan sistem angin (*Wind System*) secara sinematik. Micro-AO tekstur dibatasi agar tidak bertabrakan dengan Lumen GI.

---

## 12. Teori Balancing & Progresi Sistem

### A. Difficulty Curve
Kurva kesulitan idealnya naik bertahap dengan puncak lokal di tiap boss, bukan naik linear terus — beri variasi supaya tidak monoton (lihat Flow Theory di bagian 1).

### B. Power Budget per Sektor
Tiap kemampuan baru yang didapat Kaelen per sektor perlu "dianggarkan" supaya tidak membuat sektor sebelumnya terasa percuma — prinsip umum RPG progression design.

### C. Cost-Benefit Sistem Naratif (Syal Aina)
Karena syal Aina memendek permanen sebagai *cost* naratif, penting menjaga rasio: tiap pemendekan harus memberi *benefit* yang terasa sepadan (kemampuan baru, progres cerita penting) — kalau tidak, pemain akan merasa dihukum tanpa alasan jelas, bukan merasakan bobot pengorbanan yang diinginkan.

---

## 13. Teori Fisika Tingkat Lanjut (Terapan Real-Time Engine — Lihat [expert-physics.md](file:///d:/GodotProjects/Lentera-Pudar/references/expert-physics.md))

### A. Rigid Body & Sequential Impulse Solver
Objek keras (reruntuhan, pecahan es) disimulasikan lewat persamaan Newton-Euler ($F=ma$, $\tau=I\alpha$) yang diselesaikan secara iteratif ($4–10\text{ iterasi/frame}$) oleh *Sequential Impulse Solver* UE5 Chaos Physics. Pecahan es menggunakan restitusi rendah ($e=0.1–0.3$) dan aproksimasi *Coulomb Friction Cone* agar jatuh berat menyerap momentum tumbukan.

### B. Soft Body & XPBD Cloth Dynamics (Extended Position-Based Dynamics)
Simulasi Syal Aina dan jubah Kaelen mengadopsi solver **XPBD** (Chaos Cloth & Blender Cloth) yang memanipulasi langsung posisi partikel dengan parameter *Compliance* ($\alpha$), menjamin kestabilan simulasi pada nilai kekakuan tinggi tanpa ledakan numerik. Bending stiffness ($0.4–0.6$) dipisahkan dari stretching stiffness, dipadu *BVH spatial hashing* untuk self-collision jubah.

### C. Fracture Mechanics & Voronoi Lattice-Biased
Pecahan es akibat pukulan cakar Kaelen dihitung dari konsentrasi tegangan ($K_t$) menggunakan sistem **Pre-Fractured Voronoi**. Distribusi titik seed menggunakan **Lattice-Biased Distribution** (mengikuti kisi kristal es) agar bongkahan es tampak prismatik dan runcing secara alami, bukan serpihan batu acak.

### D. Fluid Dynamics Disederhanakan untuk Efek Uap & Lelehan
Efek uap dingin dan embun beku menggunakan aproksimasi *Grid-Based Eulerian* atau *SPH Niagara Particles*, dipadu *Flipbook Textures* pre-rendered dan *Shallow Water Equations (SWE)* untuk riak genangan air es di lantai dungeon.

### E. Light Transport, Cook-Torrance BRDF & Lumen
Transportasi cahaya dirumuskan oleh *Rendering Equation*. UE5 menerapkan **Cook-Torrance BRDF** dengan distribusi **GGX / Trowbridge-Reitz** (Roughness es $0.15–0.30$ menghasilkan highlight specular tajam berkilau). Lumen mengaproksimasi global illumination real-time melalui kombinasi *SDF Tracing*, *Screen-Space Tracing*, dan *Surface Cache*.

### F. Inverse Kinematics Solvers (FABRIK vs CCD)
Two-Bone IK Kaelen menggunakan algoritma **FABRIK** (Forward And Backward Reaching IK) yang bekerja di ruang posisi dua arah (Backward-Forward Pass) untuk konvergensi lebih cepat dan bebas artefak sendi pada kontur lantai dungeon miring.

---

## 14. Teori Matematika Tingkat Lanjut (Terapan — Lihat [expert-mathematics.md](file:///d:/GodotProjects/Lentera-Pudar/references/expert-mathematics.md))

### A. Vektor & Quaternion (SLERP vs NLERP)
Rotasi 3D merepresentasikan orientasi melalui quaternion 4D ($q = w + xi + yj + zk$) bebas *Gimbal Lock*. Wajib menggunakan **SLERP** (Spherical Linear Interpolation) untuk transisi kamera sinematik berkecepatan sudut konstan, dan **NLERP** untuk blending animasi mikro frekuensi tinggi (Idle ke Walk).

### B. Interpolasi, Easing & Cubic Bezier sebagai Bahasa Emosi
Transisi kamera dan UI disesuaikan dengan kurva **Cubic Bezier ($P(t)$)** emosional: kurva *overshoot & settle* untuk Sektor 2 (*Anger*) yang agresif, dan kurva *flat lalu deselerasi curam* untuk Sektor 4 (*Depression*) yang berat dan lambat.

### C. Spline Geometri, Arc-Length Reparameterization & C2 Continuity
Jalur kamera sinematik menggunakan *Catmull-Rom Spline*, sedangkan lorong organik *Hall of Mirrors* menggunakan *Composite Bezier Spline* dengan kontinuitas kelengkungan **C2 Continuity** (turunan kedua kontinu) dan **Arc-Length Reparameterization** agar kecepatan objek sepanjang kurva stabil tanpa percepatan anomali.

### D. Signed Distance Fields (SDF) Matematis
SDF $f(p)$ dengan sifat 1-Lipschitz memungkinkan *Sphere Tracing* efisien untuk Lumen GI, collision proxy murah untuk puing es, dan kalkulasi soft shadow volumetrik analitik.

### E. Noise Functions & Fractal Brownian Motion (fBm)
Tekstur permukaan es dan partikel Niagara dibangun dari kombinasi Perlin, Simplex, dan Worley (Cellular) Noise yang ditumpuk secara multi-skala melalui **Fractal Brownian Motion (fBm)** (rasio frekuensi oktaf $2:1$).

### F. Formalisasi Finite State Machine & Hierarchical AI
Combat controller Kaelen diformalkan sebagai 5-tuple FSM, sedangkan AI musuh jiwa beku dan Boss 5 Sektor dimigrasikan ke **Behavior Tree & Hierarchical State Machine (HSM)** untuk mencegah ledakan kombinatorial transisi state.

---

## 15. Teori Psikologi Pemain (Player Psychology — Lihat [expert-psychology.md](file:///d:/GodotProjects/Lentera-Pudar/references/expert-psychology.md))

### A. Self-Determination Theory (SDT) & Diagnostik Desain
Motivasi intrinsik pemain dievaluasi lewat 3 pilar: **Autonomy** (kebebasan eksplorasi rute rahasia Eyepatch), **Competence** (penguasaan parry 12-frame dan pola musuh), dan **Relatedness** (ikatan emosional Kaelen-Aina). Menolak sistem leaderboard kompetitif untuk mencegah fenomena *Motivation Crowding-Out*.

### B. Operant Conditioning & Sistem Reward Etis
Menerapkan *Fixed Ratio Scheduling* (tiap Altar Duka dinyalakan = 1 fragmen memori Aina) dan **menolak sistem reward acak (Anti-Gacha/Loot Mandate)** agar setiap pengorbanan syal terasa sebagai keputusan sadar yang dapat direnungkan.

### C. Prospect Theory & Loss Aversion 2.5x
Kerugian psikologis dirasakan **2.0 hingga 2.5 kali lebih berat** dibanding keuntungan bernilai setara ($V(\text{Loss}) \approx 2.25 \times V(\text{Gain})$). Pemendekan permanen Syal Aina yang terlihat jelas di layar sebelum aktivasi altar memicu bobot keputusan naratif yang mendalam.

### D. Cognitive Load & Minimal Diegetic HUD
Menghilangkan UI konvensional demi menekan *Extraneous Load*, membebaskan kapasitas mental (*Germane Load*) dan *Emotional Bandwidth* pemain untuk meresapi duka cerita tanpa kelelahan kognitif.

### E. Presence, Embodiment & Kerentanan Bug
Spatial presence (kamera dekat, audio 3D binaural), Sensorimotor embodiment (kontrol instan tanpa input delay), dan Social presence (mikro-ekspresi Aina). Bug kecil pada input/hitbox wajib diprioritaskan saat QC karena dapat merusak kondisi *Presence* secara instan.

### F. Dinamika Duka Non-Linear (Kübler-Ross Echoes)
5 Tahap Berduka (Denial s.d. Acceptance) dipahami sebagai model non-linear; memperbolehkan gema visual/audio dari tahap sebelumnya muncul samar di sektor berikutnya untuk pengalaman duka yang realistis.

### G. Tension-Release Cycle & Emotional Bandwidth Pacing
Menyisipkan *Breather Rooms* dan jeda kontemplatif di antara beat emosional berat untuk mencegah desensitisasi dan kejenuhan emosional (*emotional burnout*).

---

## 16. Teori Tambahan yang Layak Dipertimbangkan

### A. Ludonarrative Consonance/Dissonance
Kesesuaian antara mekanik yang dimainkan dan cerita yang disampaikan. Bobot hantaman pukulan (*hitstop*, inersia, dinginnya es) harus selaras dengan kepedihan cerita tragedi Kaelen & Aina.

### B. Semiotika Visual (Visual Semiotics)
Konsistensi makna simbol visual di seluruh dunia (pola kristal es, pose patung beku, ukiran Altar Duka) agar pemain dapat membaca sejarah lingkungan tanpa teks.

### C. Accessibility Design Theory
Opsi mode buta warna (*colorblind filter* untuk kontras 2700K vs 6500K), pengurangan *screen shake*, dan subtitle terstruktur untuk bisikan audio binaural.

### D. Procedural Content Generation (PCG) Theory
Prinsip dasar seperti *constraint-based generation* dan *wave function collapse* jika diterapkan untuk variasi reruntuhan semi-prosedural.

### E. AI Behavior Tree Theory (untuk Musuh)
Struktur *selector*, *sequence*, dan *condition* untuk variasi perilaku musuh jiwa beku (pasif, menangis, mendadak menyerang saat didekati).

### F. Playtesting & Iterative Design Theory
Metodologi *"fail fast, iterate often"* — membangun versi kasar (*grey-box*) tiap sektor di Blender/UE5 untuk memvalidasi pacing sebelum menambahkan aset visual detail.

---

## 17. Teori Produksi & Pipeline Teknis

### A. Performance Budgeting & Optimization Theory
Anggaran performa PC: pembagian LOD (*Level of Detail*), culling objek di luar kamera, dan optimasi transparent material agar terkunci pada **Solid 60 / 120 FPS**.

### B. World Partition & Level Streaming
Pemuatan/pembongkaran 5 Sektor Dungeon secara dinamis di memori (*level streaming*) berdasarkan posisi pemain tanpa layar loading mengganggu.

### C. Asset Naming Convention & Folder Structure
Standar penamaan baku (*Pipeline Hygiene*):
- `SK_` : Skeletal Mesh (contoh: `SK_Kaelen_Body`)
- `SM_` : Static Mesh (contoh: `SM_Crypt_Pillar_01`)
- `M_` / `MI_` : Material / Material Instance (contoh: `M_Cursed_Crystal`, `MI_Aina_Scarf`)
- `FX_` : Niagara FX (contoh: `FX_Warmth_Embers`, `FX_Hit_Sparks`)
- `A_` / `ABP_` : Animation Sequence / Animation Blueprint (contoh: `A_Kaelen_Punch_01`, `ABP_Kaelen`)

### D. Version Control untuk Aset 3D (Git LFS)
Pengelolaan file biner besar (`.blend`, `.fbx`, `.uasset`, `.wav`) menggunakan Git LFS untuk mencegah korupsi riwayat repositori.

### E. Save System & Checkpoint Design Theory
Penyimpanan progres permanen di Altar Duka untuk mengunci konsekuensi pengorbanan Syal Aina tanpa rollback sepele.

### F. Input & Control Scheme Theory (termasuk Haptics)
Getaran kontroler (*haptic feedback*) terkalibrasi untuk detak denyut syal Aina, tangkisan parry sukses, dan hantaman cakar es.

---

## 18. Teori Tambahan Lain (Penutup Cakupan Produksi)

### A. Narrative Pacing — Three-Act Structure
- **Act 1 (Setup)**: Sektor 1 (Denial) & Sektor 2 (Anger) — Pengenalan semesta, kutukan, dan kepedihan awal.
- **Act 2 (Confrontation)**: Sektor 3 (Bargaining) & Sektor 4 (Depression) — Titik balik emosional terdalam dan penyusutan cahaya terendah.
- **Act 3 (Resolution)**: Sektor 5 (Acceptance) — Rekonsiliasi batin Kaelen-Aina dan terbukanya fajar menuju *Overworld*.

### B. World-Building Consistency / Canon Bible
Daftar aturan mutlak semesta yang tidak boleh dilanggar (Hukum Tiga Warna, sifat Kutukan Pudar, janji Aina).

### C. Sound Mixing & Mastering Theory
Target *loudness* standar:
- **-20 LUFS**: Musik latar eksplorasi (layer dasar).
- **-16 LUFS**: Musik combat (layer penuh) — target standar media interaktif.
- **-18 LUFS**: Dialog & bisikan jiwa beku, dengan *ducking* otomatis musik -6dB saat aktif (Attack: 150ms, Release: 400ms).
- **-28 s.d. -24 LUFS**: Ambience derit es & angin — sangat halus di bawah narasi.
- **Peak -3 dB** untuk SFX combat — mencegah digital clipping.

### D. Typography & Subtitle Readability
Ukuran font dengan kontras tinggi terhadap latar belakang batu gelap, dilengkapi drop-shadow dan kecepatan baca standar.

### E. Localization-Readiness
Penyediaan buffer ruang UI (*text expansion*) untuk multibahasa (Bahasa Indonesia & English).

### F. Playtesting Metrics & Telemetry
Pencatatan data titik kematian pemain, durasi per sektor, dan keberhasilan parry untuk kalibrasi kurva kesulitan.

### G. Living Document Methodology
Seluruh dokumen referensi dipelihara secara mutakhir, sinkron, dan terdokumentasi versi revisinya.

---

## 19. Cara Penggunaan Dokumen Ini untuk AI Agent

- **Konteks Dasar**: Dokumen ini menjadi pedoman *The Why* di setiap sesi kerja pemodelan Blender 5.2 LTS dan pemrograman Unreal Engine 5.
- **Instruksi Granular**: Sub-agent dapat merujuk langsung bab spesifik (misal: "Gunakan prinsip 4.B Hitstop" atau "Terapkan prinsip 11.B Subsurface Scattering").
- **Standar Baku**: Dokumen ini adalah prinsip/kerangka berpikir fundamental yang mendampingi Master GDD dan Dokumen Visi Kreatif Lentera Pudar.

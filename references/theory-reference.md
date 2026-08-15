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
Ada reward *intrinsik* (kepuasan menuntaskan mekanik parry sulit) dan *ekstrinsik* (item, kemampuan baru). Untuk game bertema grief seperti ini, reward sebaiknya condong ke intrinsik/naratif (potongan memori, dialog, perubahan visual dunia) dibanding sekadar loot — supaya tetap konsisten dengan nuansa "poetic dark fantasy", bukan grinding RPG biasa.

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

## 9. Teori Animasi

### A. 12 Prinsip Animasi Disney (yang relevan untuk 3D real-time)
- **Anticipation**: gerakan kecil sebelum aksi utama (Kaelen menekuk lutut sebelum dash) — membantu readability combat.
- **Follow Through & Overlapping Action**: syal Aina dan jubah Kaelen tidak berhenti bersamaan dengan tubuh — inilah kenapa cloth simulation/spring bones penting secara animasi, bukan cuma fisik.
- **Squash & Stretch** (versi halus untuk gaya semi-realistis): dipakai halus di ekspresi wajah/impact combat, bukan cartoonish.
- **Secondary Action**: gerakan pendukung yang memperkaya aksi utama (rambut Kaelen bergoyang saat mendarat) tanpa mengalihkan fokus dari aksi utama.

### B. IK (Inverse Kinematics) vs FK (Forward Kinematics)
FK dipakai untuk animasi terprogram/mocap dasar (gerakan tubuh umum), IK dipakai real-time untuk penyesuaian dinamis (kaki menyesuaikan permukaan tanah tidak rata, tangan menyentuh dinding saat merambat). Agent perlu tahu kombinasi keduanya diperlukan untuk gerakan Kaelen di dungeon yang tidak rata.

### C. Blend Trees & Locomotion State Machine
Transisi mulus antar animasi (diam → jalan → lari → serangan) diatur lewat *blend tree* berbasis parameter kecepatan, bukan cut animasi kaku — standar di UE5 Animation Blueprint.

---

## 10. Teori Rigging & Simulasi Kain

### A. Skeleton Hierarchy & Spring Bones
Syal Aina memerlukan *spring bone chain* terpisah dari skeleton utama Kaelen — tulang tambahan yang bereaksi ke gravitasi/gerakan tapi tidak dikontrol animator secara manual, prinsip umum di karakter dengan aksesori kain/rambut panjang.

### B. Cloth Simulation Constraints
Simulasi kain butuh *pinning point* (titik tetap, misal syal yang melingkar di leher) dan parameter *stiffness/damping* supaya tidak terlihat terlalu kaku atau terlalu lembek seperti agar-agar — penting untuk kredibilitas visual syal Aina di UE5.

### C. Facial Rigging: Blend Shapes vs Bone-based
Untuk ekspresi close-up ala Hellblade II, blend shapes (morph target) biasanya lebih presisi untuk mikro-ekspresi wajah dibanding rig tulang murni — relevan untuk momen kamera dekat di Altar Duka.

---

## 11. Teori Shader & Material (Technical Art)

### A. PBR (Physically Based Rendering)
Material di UE5 dibangun dari kombinasi *Base Color*, *Roughness*, *Metallic*, dan *Normal Map* untuk mendekati perilaku cahaya di dunia nyata. Agent perlu paham ini sebagai kerangka umum saat membuat material, bukan angka acak.

### B. Subsurface Scattering (SSS) untuk Kristal Es
Es tampak "hidup" karena cahaya menembus sedikit ke dalam material sebelum keluar lagi (bukan solid opaque) — parameter SSS penting untuk kristal es Kaelen supaya terasa organik, bukan seperti kaca/plastik biasa.

### C. Emissive Material untuk Sumber Cahaya Bergaya
Syal Aina dan kristal kutukan sebaiknya pakai *emissive* yang terhubung ke parameter Curse Meter secara real-time (material parameter collection di UE5), bukan warna emissive statis — supaya perubahan intensitas terlihat halus, bukan on/off kasar.

### D. Niagara Particle System sebagai Bahasa Visual
Partikel bukan cuma dekorasi — di Lentera Pudar, partikel (kunang-kunang cahaya syal, serpihan es pecah) berfungsi sebagai *indikator status* juga, selaras prinsip "makhluk kecil pendukung" dari artstyle Kena yang sudah dibahas di moodboard.

---

## 12. Teori Balancing & Progresi Sistem

### A. Difficulty Curve
Kurva kesulitan idealnya naik bertahap dengan puncak lokal di tiap boss, bukan naik linear terus — beri variasi supaya tidak monoton (lihat Flow Theory di bagian 1).

### B. Power Budget per Sektor
Tiap kemampuan baru yang didapat Kaelen per sektor perlu "dianggarkan" supaya tidak membuat sektor sebelumnya terasa percuma — prinsip umum RPG progression design.

### C. Cost-Benefit Sistem Naratif (Syal Aina)
Karena syal Aina memendek permanen sebagai *cost* naratif, penting menjaga rasio: tiap pemendekan harus memberi *benefit* yang terasa sepadan (kemampuan baru, progres cerita penting) — kalau tidak, pemain akan merasa dihukum tanpa alasan jelas, bukan merasakan bobot pengorbanan yang diinginkan.

---

## 13. Teori Fisika Tingkat Lanjut (Terapan untuk Real-Time Engine)

### A. Rigid Body & Collision Dynamics
Objek keras (reruntuhan, pecahan es) disimulasikan lewat *rigid body dynamics* — massa, momen inersia, restitusi (seberapa "mantul" objek), dan friction coefficient. Untuk pecahan kristal es saat Heavy Cursed Strike, penting mengatur restitusi rendah-menengah supaya pecahan terasa "berat dan dingin", bukan memantul seperti karet.

### B. Soft Body & Cloth Physics (Verlet Integration / Position-Based Dynamics)
Simulasi syal Aina dan jubah Kaelen di UE5 (Chaos Cloth) umumnya berbasis *Position-Based Dynamics (PBD)* atau *Verlet Integration* — metode yang menghitung posisi partikel kain berikutnya dari posisi sekarang & sebelumnya plus gaya eksternal (gravitasi, angin), dengan *constraint solving* iteratif untuk menjaga jarak antar titik kain tetap masuk akal. Parameter kunci: *stiffness*, *damping*, *iteration count*.

### C. Fracture Mechanics (untuk Pecahan Es)
Simulasi retak/pecah (fracture) memodelkan bagaimana material rapuh (es) pecah berdasarkan *stress concentration* di titik lemah, bukan pecah acak merata. Untuk visual kristal es pecah, gunakan pola *Voronoi fracture* yang meniru retakan alami kristal, dikombinasikan dengan pre-fractured mesh untuk performa real-time.

### D. Fluid Dynamics (Disederhanakan) untuk Efek Leleh/Uap
Efek es mencair/uap dingin menggunakan *flipbook texture* atau *Niagara fluid-like particle behavior* yang meniru perilaku fluida secara visual tanpa komputasi Navier-Stokes penuh — standar industri *plausible, not accurate*.

### E. Global Illumination & Light Transport (Lumen)
Lumen di UE5 menghitung *indirect lighting* (cahaya pantulan) secara real-time menggunakan kombinasi *Signed Distance Field tracing* dan *screen-space methods*. Warna dinding di dekat syal Aina akan "terwarnai" hangat oleh cahaya pantulnya secara otomatis sebagai visual storytelling pasif.

### F. Inverse Kinematics sebagai Constraint Solving
Secara fisika, IK adalah masalah *constraint satisfaction* — mencari sudut sendi yang memenuhi posisi target (misal telapak kaki di permukaan tanah miring) dalam batas rotasi anatomis yang mungkin.

---

## 14. Teori Matematika Tingkat Lanjut (Terapan)

### A. Vektor & Quaternion untuk Rotasi 3D
Rotasi karakter dan kamera di UE5 dihitung dengan *quaternion* (bukan Euler angle murni) untuk menghindari *gimbal lock*. Sangat penting untuk transisi rotasi kamera dekat ala Hellblade II yang mulus tanpa patah.

### B. Interpolasi & Easing Curves
Transisi nilai (posisi kamera, intensitas cahaya, blend animasi) menggunakan *easing curves* (ease-in, ease-out, cubic Bezier) agar gerakan terasa natural, bukan kaku/robotik.

### C. Spline & Bezier Curves untuk Jalur Kamera dan Level
Jalur kamera sinematik, patroli musuh, dan bentuk lorong dungeon organik dibangun di atas *spline* (kurva matematis titik kontrol) untuk membentuk lorong berkelok halus.

### D. Signed Distance Fields (SDF)
Dasar matematis di balik Nanite/Lumen dan teknik shader (termasuk soft shadow, fog volumetrik) — merepresentasikan jarak dari titik mana pun ke permukaan terdekat sebuah objek.

### E. Perlin/Simplex Noise untuk Variasi Prosedural
Noise function dipakai untuk variasi natural (tekstur es tidak seragam, pergerakan partikel kunang-kunang syal, distribusi reruntuhan) — memberi kesan "organik acak" tapi terkontrol.

### F. State Machine (Finite State Machine / FSM) sebagai Struktur Logika
FSM adalah struktur dasar untuk combat Kaelen (Idle → Attack → Recovery → Idle) dan AI musuh sebelum diperluas menjadi Behavior Tree di UE5.

---

## 15. Teori Psikologi Pemain (Player Psychology)

### A. Self-Determination Theory (Deci & Ryan)
Motivasi intrinsik pemain didorong tiga kebutuhan: **Autonomy** (pilihan rute eksplorasi), **Competence** (kemahiran combat yang fair & readable), dan **Relatedness** (keterikatan emosional Kaelen-Aina). *Relatedness* adalah motivator emosional utama game ini.

### B. Operant Conditioning & Reward Timing
Reward yang dapat diprediksi secara naratif (tiap Altar Duka = biaya syal + hadiah kemampuan/memori) memperkuat refleksi emosional, bukan sekadar retensi adiktif acak.

### C. Loss Aversion
Manusia merasakan kehilangan jauh lebih berat dibanding mendapat keuntungan setara. Memendeknya Syal Aina secara permanen memicu beban emosional mendalam yang memperkuat tema duka & pengorbanan.

### D. Cognitive Load & Minimal HUD
Mengurangi gangguan visual di layar agar kapasitas mental pemain tersisa untuk merasakan resonansi cerita dan atmosferik dungeon, bukan membaca angka UI.

### E. Presence & Embodiment
Kamera dekat, audio binaural 3D, dan kontrol responsif menciptakan rasa *embodiment* — pemain merasa "menjadi" Kaelen yang memikul duka, bukan sekadar menggerakkan bidak 3D.

### F. Uncanny Valley (untuk Karakter Stylized-Realistic)
Menjaga keseimbangan proporsi semi-realistis (1:6.8) dengan ekspresi wajah mikro yang presisi (blend shapes) agar terhindar dari kesan janggal / tidak nyaman.

### G. Tension-Release Cycle (Psikologi Ketegangan Naratif)
Memberikan jeda napas (*breather room*) di antara arena pertarungan berdarah/beku agar pemain tidak mengalami mati rasa emosional (*emotional burnout*).

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

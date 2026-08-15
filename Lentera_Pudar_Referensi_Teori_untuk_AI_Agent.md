# Referensi Teori Pendukung — Lentera Pudar
### Untuk AI Agent (MCP Blender + Unreal Engine Kustom)

Dokumen ini berisi kerangka teori non-matematis/non-fisika-lanjut yang relevan untuk proyek "Lentera Pudar". Tujuannya: memberi AI agent kamu "bahasa bersama" soal *kenapa* sebuah keputusan desain diambil, bukan cuma *apa* yang harus dibangun. Ini melengkapi GDD dan Moodboard yang sudah ada.

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

### A. PBR (Physically Based Rendering) — konsep dasar tanpa rumus
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
Tiap kemampuan baru yang didapat Kaelen per sektor (jika mengikuti model GRIS dari sebelumnya, atau versi sendiri) perlu "dianggarkan" supaya tidak membuat sektor sebelumnya terasa percuma — prinsip umum RPG progression design.

### C. Cost-Benefit Sistem Naratif (Syal Aina)
Karena syal Aina memendek permanen sebagai *cost* naratif, penting menjaga rasio: tiap pemendekan harus memberi *benefit* yang terasa sepadan (kemampuan baru, progres cerita penting) — kalau tidak, pemain akan merasa dihukum tanpa alasan jelas, bukan merasakan bobot pengorbanan yang diinginkan.

---

## 13. Teori Fisika Tingkat Lanjut (Terapan untuk Real-Time Engine)

Ini bukan fisika akademis murni, tapi versi terapan yang relevan langsung untuk simulasi di Blender/UE5.

### A. Rigid Body & Collision Dynamics
Objek keras (reruntuhan, pecahan es) disimulasikan lewat *rigid body dynamics* — massa, momen inersia, restitusi (seberapa "mantul" objek), dan friction coefficient. Untuk pecahan kristal es saat Heavy Cursed Strike, penting mengatur restitusi rendah-menengah supaya pecahan terasa "berat dan dingin", bukan memantul seperti karet.

### B. Soft Body & Cloth Physics (Verlet Integration / Position-Based Dynamics)
Simulasi syal Aina dan jubah Kaelen di UE5 (Chaos Cloth) umumnya berbasis *Position-Based Dynamics (PBD)* atau *Verlet Integration* — metode yang menghitung posisi partikel kain berikutnya dari posisi sekarang & sebelumnya plus gaya eksternal (gravitasi, angin), dengan *constraint solving* iteratif untuk menjaga jarak antar titik kain tetap masuk akal. Agent perlu tahu parameter kunci: *stiffness*, *damping*, *iteration count* — makin tinggi iterasi, makin akurat tapi makin berat secara performa.

### C. Fracture Mechanics (untuk Pecahan Es)
Simulasi retak/pecah (fracture) memodelkan bagaimana material rapuh (es) pecah berdasarkan *stress concentration* di titik lemah, bukan pecah acak merata. Untuk visual kristal es pecah, gunakan pola *Voronoi fracture* yang meniru retakan alami kristal, dikombinasikan dengan pre-fractured mesh untuk performa real-time (bukan destruction fisika penuh yang mahal secara komputasi).

### D. Fluid Dynamics (Disederhanakan) untuk Efek Leleh/Uap
Efek es mencair/uap dingin biasanya bukan simulasi fluida penuh (terlalu berat untuk real-time), melainkan *flipbook texture* atau *Niagara fluid-like particle behavior* yang meniru perilaku fluida secara visual tanpa menghitung Navier-Stokes penuh — pendekatan "cukup meyakinkan" (*plausible, not accurate*) adalah standar industri untuk game real-time.

### E. Global Illumination & Light Transport (Lumen)
Lumen di UE5 menghitung *indirect lighting* (cahaya pantulan) secara real-time menggunakan kombinasi *Signed Distance Field tracing* dan *screen-space methods* — secara konsep, ini mendekati bagaimana cahaya sungguhan memantul berkali-kali di permukaan sebelum sampai ke mata, bukan cuma cahaya langsung dari sumbernya. Penting dipahami agent karena artinya warna dinding di dekat syal Aina akan "terwarnai" hangat oleh cahaya pantulnya secara otomatis — bisa dimanfaatkan sebagai storytelling pasif.

### F. Inverse Kinematics sebagai Constraint Solving (bukan sekadar animasi)
Secara fisika, IK adalah masalah *constraint satisfaction* — mencari sudut sendi yang memenuhi posisi target (misal telapak kaki di permukaan tanah miring) dalam batas rotasi anatomis yang mungkin. Relevan untuk pergerakan Kaelen di dungeon dengan lantai tidak rata.

---

## 14. Teori Matematika Tingkat Lanjut (Terapan)

### A. Vektor & Quaternion untuk Rotasi 3D
Rotasi karakter dan kamera di UE5 dihitung dengan *quaternion* (bukan Euler angle murni) untuk menghindari *gimbal lock* — masalah klasik di mana dua sumbu rotasi "terkunci" jadi satu pada sudut tertentu. Agent perlu tahu ini terutama untuk kamera dekat ala Hellblade II yang butuh transisi rotasi mulus tanpa patah.

### B. Interpolasi & Easing Curves
Transisi nilai (posisi kamera, intensitas cahaya, blend animasi) jarang linear murni — dipakai *easing curves* (ease-in, ease-out, cubic Bezier) supaya gerakan terasa natural, bukan robotic. Penting untuk transisi cahaya syal Aina saat meredup, dan transisi kamera saat masuk mode close-up naratif.

### C. Spline & Bezier Curves untuk Jalur Kamera dan Level
Jalur kamera sinematik, jalur patroli musuh, dan bahkan bentuk lorong dungeon organik sering dibangun di atas *spline* (kurva matematis yang dikontrol lewat titik kontrol) — relevan untuk membuat lorong *Hall of Mirrors* yang berkelok secara halus, bukan sekadar sambungan garis lurus.

### D. Signed Distance Fields (SDF)
Dasar matematis di balik Nanite/Lumen dan beberapa teknik shader (termasuk soft shadow, fog volumetrik) — SDF merepresentasikan jarak dari titik mana pun ke permukaan terdekat sebuah objek. Berguna dipahami agent secara konsep saat troubleshoot rendering/pencahayaan aneh, bukan untuk dihitung manual.

### E. Perlin/Simplex Noise untuk Variasi Prosedural
Noise function dipakai untuk variasi natural (tekstur es tidak seragam, pergerakan kunang-kunang cahaya syal, distribusi reruntuhan) — memberi kesan "organik acak" tapi tetap terkontrol, jauh lebih baik daripada random murni yang terasa berantakan.

### F. State Machine (Finite State Machine / FSM) sebagai Struktur Logika
Bukan murni matematika, tapi berakar dari teori automata — FSM adalah struktur dasar untuk combat Kaelen (Idle → Attack → Recovery → Idle) dan AI musuh (Patrol → Alert → Chase → Attack). Agent perlu paham FSM sebagai kerangka pikir dasar sebelum membangun Behavior Tree yang lebih kompleks di UE5.

---

## 15. Teori Psikologi Pemain (Player Psychology)

### A. Self-Determination Theory (Deci & Ryan)
Motivasi intrinsik pemain didorong tiga kebutuhan: **Autonomy** (merasa punya pilihan nyata — misal pemain bisa memilih urutan area eksplorasi), **Competence** (merasa makin mahir — combat yang readable dan fair), **Relatedness** (merasa terhubung secara emosional — ikatan Kaelen-Aina). Game bertema grief seperti ini sangat bergantung pada *Relatedness* sebagai motivator utama, lebih dari sekadar reward mekanis.

### B. Operant Conditioning & Reward Timing
Reward yang datang dengan *variable timing* (tidak selalu bisa ditebak persis kapan) cenderung lebih memotivasi dibanding reward yang selalu datang di waktu tetap — tapi hati-hati: teknik ini juga dasar dari sistem adiktif eksploitatif (gacha, loot box). Untuk Lentera Pudar yang bertema reflektif, sebaiknya reward tetap dapat diprediksi secara naratif (pemain tahu "tiap Altar Duka = ada biaya dan hadiah"), bukan dibuat acak demi retensi.

### C. Loss Aversion
Secara psikologis, manusia merasakan kehilangan jauh lebih berat dibanding mendapat keuntungan setara — ini relevan langsung dengan mekanik *The Fading Scarf*. Memendeknya syal Aina secara permanen akan terasa jauh lebih berat secara emosional dibanding sekadar "mendapat kemampuan baru" yang setara nilainya — inilah kenapa mekanik ini secara psikologis efektif untuk tema pengorbanan.

### D. Cognitive Load & Minimal HUD
Terlalu banyak informasi di layar meningkatkan *cognitive load*, mengurangi kemampuan pemain fokus ke aspek emosional/naratif. Ini alasan psikologis kenapa pendekatan minimal-HUD ala Hellblade cocok — bukan cuma soal gaya visual, tapi supaya kapasitas mental pemain tersisa untuk merasakan cerita, bukan membaca angka.

### E. Presence & Embodiment
"Presence" adalah rasa "benar-benar berada" di dunia game (bukan sekadar mengontrol karakter dari luar). Kamera dekat, audio binaural, dan kontrol responsif semua berkontribusi ke rasa *embodiment* — pemain merasa "menjadi" Kaelen, bukan sekadar menggerakkannya. Penting dipertahankan konsisten karena tema grief butuh keterlibatan emosional personal, bukan jarak observasi.

### F. Uncanny Valley (untuk Wajah Karakter Stylized-Realistic)
Karena gaya karakter condong ke *stylized-realistic* (ala Kena, bukan kartun murni tapi juga bukan hyper-realistic), ada risiko masuk ke "uncanny valley" — area di mana wajah terlihat "hampir manusia tapi tidak pas" hingga terasa janggal/tidak nyaman. Agent perlu tahu ini sebagai batasan desain: makin realistis proporsi wajah, makin presisi juga animasi mikro-ekspresinya harus, atau justru pertahankan gaya sedikit stylized untuk aman dari efek ini.

### G. Tension-Release Cycle (Psikologi Ketegangan Naratif)
Otak manusia butuh siklus tegang-lega untuk tetap terlibat secara emosional dalam waktu lama — ketegangan konstan tanpa jeda justru membuat mati rasa (ironisnya bertentangan dengan tema game ini). Pastikan tiap sektor grief punya momen "lega" sesaat (breather room dari bagian Level Design) sebelum menegangkan lagi, supaya dampak emosional tiap Altar Duka tetap terasa kuat, bukan tumpul karena kelelahan.

---

## 16. Teori Tambahan yang Layak Dipertimbangkan

### A. Ludonarrative Consonance/Dissonance
Istilah untuk kesesuaian (atau ketidaksesuaian) antara apa yang pemain *lakukan* secara mekanik dengan apa yang cerita *sampaikan* secara tematik. Contoh risiko: kalau combat Kaelen terasa terlalu "seru dan ringan" padahal temanya berat soal kehilangan, itu ludonarrative dissonance. Agent perlu menjaga bobot mekanik (hitstop, kamera, audio) tetap selaras dengan bobot emosional cerita.

### B. Semiotika Visual (Visual Semiotics)
Studi soal bagaimana simbol visual membawa makna — relevan untuk desain ikonografi dungeon (bentuk kristal es, pose patung beku, simbol di Altar Duka). Pastikan simbol-simbol ini konsisten maknanya di seluruh game, supaya pemain bisa "membaca" dunia tanpa teks eksplisit (mendukung environmental storytelling di bagian 3).

### C. Accessibility Design Theory
Pertimbangan seperti opsi *colorblind mode* (penting karena game ini sangat bergantung pada kontras warna hangat/dingin), opsi mengurangi *screen shake*/motion untuk pemain sensitif, dan opsi subtitle untuk bisikan-bisikan audio penting secara naratif. Layak dimasukkan sejak awal desain, bukan ditambah belakangan.

### D. Procedural Content Generation (PCG) Theory — jika relevan
Kalau ke depan ada rencana elemen dungeon yang dihasilkan semi-prosedural (bukan full hand-crafted), teori dasar seperti *constraint-based generation* dan *wave function collapse* bisa relevan — tapi ini opsional, tergantung apakah proyek kamu memang mengarah ke replayability lewat prosedural atau tetap full hand-crafted seperti kesan dari GDD saat ini.

### E. AI Behavior Tree Theory (untuk Musuh)
Behavior Tree adalah struktur lebih fleksibel dari FSM murni untuk AI musuh — node berupa *selector*, *sequence*, dan *condition* yang dievaluasi tiap frame. Relevan untuk desain musuh yang perlu berperilaku kompleks (misal jiwa beku yang kadang pasif, kadang menyerang saat didekati) tanpa membuat kode AI jadi spaghetti FSM manual.

### F. Playtesting & Iterative Design Theory
Bukan teori teknis, tapi metodologi: prinsip *"fail fast, iterate often"* — bangun versi kasar (grey-box) tiap sektor dulu sebelum detail visual penuh, supaya masalah pacing/kesulitan ketahuan lebih awal. Berguna sebagai instruksi workflow ke agent: dahulukan fungsi & rasa main, baru estetika detail.

---

## 17. Teori Produksi & Pipeline Teknis (Sering Terlupakan, Tapi Krusial)

Bagian sebelumnya banyak bicara soal "rasanya main" — bagian ini soal memastikan proyeknya **selesai dan stabil** secara teknis, celah yang sering bikin proyek indie mandek di tengah jalan.

### A. Performance Budgeting & Optimization Theory
Tiap platform target (PC) punya "anggaran" performa: jumlah draw call, triangle count, jumlah light dinamis per scene. Nanite membantu untuk geometri, tapi bukan solusi ajaib untuk semuanya (skeletal mesh, particle, transparent material tetap mahal). Agent perlu tahu prinsip *LOD (Level of Detail)* — model detail tinggi dari dekat otomatis diganti versi rendah poligon dari jauh — dan *culling* (objek di luar pandangan kamera tidak dirender), supaya dungeon besar tetap lancar dimainkan.

### B. World Partition & Level Streaming
Untuk dungeon seluas 5 sektor, UE5 World Partition memungkinkan level dimuat/dibongkar otomatis berdasarkan posisi pemain (streaming), bukan seluruh dungeon dimuat sekaligus di memori. Penting direncanakan dari awal layout level, karena mengubah level besar jadi streaming-friendly belakangan jauh lebih sulit dibanding merancangnya sejak awal.

### C. Asset Naming Convention & Folder Structure
Proyek dengan banyak aset (karakter, prop, material, animasi) gampang berantakan tanpa konvensi penamaan yang konsisten (contoh: `SK_Kaelen_Body`, `T_IceCrystal_Albedo`, `A_Kaelen_Dash_01`). Ini bukan "teori" dalam arti akademis, tapi prinsip *pipeline hygiene* — penting terutama karena kamu bekerja dengan AI agent yang perlu referensi nama aset secara konsisten antar sesi kerja.

### D. Version Control untuk Aset 3D (Git LFS / Perforce)
Berbeda dari kode biasa, file Blender/UE5 (.blend, .uasset) besar dan biner — Git biasa kurang cocok tanpa *Git LFS (Large File Storage)*, atau alternatifnya Perforce yang lebih umum dipakai studio game untuk aset besar. Penting direncanakan sebelum aset menumpuk, supaya tidak kehilangan riwayat kerja atau konflik file yang tidak bisa di-merge seperti teks.

### E. Save System & Checkpoint Design Theory
Kapan game menyimpan progres (auto-save di titik tertentu vs manual save) memengaruhi rasa risiko pemain. Untuk game dengan konsekuensi permanen (syal Aina memendek permanen), penting dipikirkan: apakah pemain bisa "menyesal" dan reload sebelum Altar Duka, atau keputusan itu memang dibuat permanen tanpa jalan mundur — ini keputusan desain sekaligus teknis (kapan checkpoint ditulis ke save file).

### F. Input & Control Scheme Theory (termasuk Haptics)
Selain keyboard/mouse, pertimbangkan *controller rumble/haptic feedback* untuk momen penting (detak jantung syal Aina, hit berat combat) — Hellblade dan banyak game modern memakai haptik sebagai lapisan sensorik tambahan yang tidak bisa digantikan visual/audio saja.

---

## 18. Teori Tambahan Lain (Penutup Cakupan Produksi)

### A. Narrative Pacing — Three-Act Structure sebagai Lapisan Tambahan
Selain Kübler-Ross (5 tahap grief) sebagai struktur sektor, pertimbangkan *three-act structure* klasik (Setup – Confrontation – Resolution) sebagai lapisan pacing keseluruhan game: Sektor 1-2 sebagai Act 1 (pengenalan dunia & kutukan), Sektor 3 sebagai Act 2 (titik balik/pengkhianatan emosional terbesar), Sektor 4-5 sebagai Act 3 (klimaks & resolusi). Dua struktur ini (grief stages + three-act) bisa saling melapis, bukan saling menggantikan.

### B. World-Building Consistency / Canon Bible
Untuk menghindari kontradiksi lore saat proyek membesar (misal detail kecil soal aturan Kutukan Pudar berubah-ubah antar sesi kerja dengan agent), pertimbangkan dokumen "canon tracker" terpisah — daftar fakta dunia yang sudah final dan tidak boleh diubah tanpa sengaja, terpisah dari GDD yang mungkin masih berkembang.

### C. Sound Mixing & Mastering Theory (Loudness, Ducking)
Di luar sound design kreatif yang sudah dibahas (bagian 7), ada aspek teknis mixing: *ducking* (musik otomatis mengecil saat dialog/bisikan penting muncul) dan target *loudness* standar (biasanya sekitar -16 LUFS untuk media interaktif) supaya volume terasa konsisten di headphone maupun speaker, tidak ada bagian yang tiba-tiba terlalu keras/pelan.

### D. Typography & Subtitle Readability Theory
Untuk subtitle bisikan-bisikan dan dialog, ukuran font, kontras terhadap background gelap, dan durasi tampil per baris teks punya standar keterbacaan sendiri (umumnya dihitung dari kecepatan baca rata-rata, bukan durasi asal tebak) — penting karena dungeon kamu banyak area gelap yang bisa membuat subtitle sulit terbaca kalau kontrasnya tidak dijaga.

### E. Localization-Readiness Theory
Meski awal pengembangan mungkin hanya Bahasa Indonesia/Inggris, teks UI dan dialog sebaiknya dirancang dengan *text expansion buffer* (ruang UI lebih lebar dari kebutuhan teks asli) — bahasa lain seringkali butuh ruang lebih panjang untuk makna yang sama, dan ini jauh lebih murah direncanakan dari awal dibanding dirombak belakangan.

### F. Playtesting Metrics & Telemetry Theory
Selain playtesting kualitatif (bagian 16.F), pertimbangkan data kuantitatif sederhana saat proyek mulai punya build yang bisa dites: di titik mana pemain paling sering mati/frustrasi, berapa lama rata-rata di tiap sektor. Bahkan tanpa analytics canggih, log sederhana ini membantu validasi apakah difficulty curve (bagian 12.A) benar-benar terasa seperti yang direncanakan di atas kertas.

### G. Living Document / Design Documentation Theory
GDD, Moodboard, dan dokumen teori ini sendiri sebaiknya diperlakukan sebagai *living document* — direvisi seiring proyek berkembang, bukan dibekukan di draf pertama. Praktik baik: catat tanggal/versi tiap revisi besar, supaya agent (dan kamu sendiri) tahu keputusan desain mana yang terbaru vs yang sudah ditinggalkan.

---

## 19. Cara Memberikan Dokumen Ini ke AI Agent

Saran praktis penggunaan:
- Sertakan dokumen ini **bersama** GDD utama dan Moodboard Referensi sebagai context dasar tiap sesi kerja agent di Blender/UE5, supaya keputusan teknis (rigging, shader, level layout) punya alasan desain yang konsisten, bukan default engine.
- Kalau agent kamu bisa menerima instruksi granular, sebutkan bagian spesifik dokumen ini (misal "gunakan prinsip 7.B — binaural audio" atau "terapkan 11.B — Subsurface Scattering") saat meminta task teknis tertentu, supaya output lebih terarah.
- Dokumen ini bersifat prinsip/kerangka berpikir, bukan spesifikasi angka pasti (itu ranah dokumen teknis terpisah berisi parameter numerik spesifik per sistem, kalau nanti diperlukan).

---

*Dokumen ini adalah lampiran teori pendukung, dirancang untuk dibaca berdampingan dengan GDD utama dan Moodboard Referensi Kena/Hellblade.*

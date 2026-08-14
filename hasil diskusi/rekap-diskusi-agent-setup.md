# Rekap Diskusi — Setup Agent & Skill untuk Antigravity (Proyek 2D Pixel RPG Top-Down)

Dokumen ini rangkuman seluruh pembahasan hari ini untuk bahan evaluasi kamu.
Berisi konsep yang dibahas, keputusan yang diambil, dan alasan di baliknya.
Untuk struktur teknis siap-pakai, lihat `AGENTS.md` (dokumen terpisah).

---

## 1. Dasar: Agent, Skill, AGENTS.md

- **Agent** = instance model AI yang bisa loop: baca konteks → putuskan
  aksi → panggil tool → lihat hasil → ulangi. Beda dari chatbot biasa
  karena bisa mengeksekusi (edit file, panggil MCP), bukan cuma jawab teks.
- **Skill** = paket pengetahuan spesifik yang di-load ke context **hanya
  saat relevan** (progressive disclosure), bukan selalu menempel di semua
  percakapan.
- **AGENTS.md** = "kontrak" tim — daftar peran, tanggung jawab, aturan
  handoff antar peran. Dibaca sebagai konteks, bukan kode.
- **Relasi:** Agent = pelaku, AGENTS.md = struktur tim, Skill = pengetahuan
  yang dipinjam agent saat relevan.
- **Bukan "training"** — skill itu context injection (mirip RAG), bukan
  mengubah bobot model. Istilah yang tepat: **knowledge grounding**.
  Konsekuensinya: efeknya cuma aktif selama skill ter-load, tidak menetap
  permanen di kemampuan model.

---

## 2. Struktur Skill untuk Pipeline Godot + Aseprite + PixelLab

Skill dipisah per domain sempit, bukan digabung jadi satu file besar:
- `godot-topdown-reference`, `aseprite-scripting-reference`,
  `pixellab-prompt-guide`, `style-guide` (referensi bersama)
- Domain kreatif: `pixel-art-shading`, `pixel-art-composition`,
  `sprite-animation-principles`, `level-layout-design`,
  `encounter-pacing`, `player-psychology-engagement`

**Prinsip granularitas** yang disepakati: pecah skill berdasarkan
**"kapan dipakai bersamaan"**, bukan berdasarkan topik akademis. Kalau
dua hal selalu relevan bareng di satu momen kerja → gabung. Kalau dipakai
di momen kerja yang beda → pecah.

**Kriteria kualitas skill yang baik** (checklist evaluasi):
deskripsi/trigger presisi, satu tanggung jawab per skill, isi berupa
prinsip actionable + contoh (bukan narasi), SKILL.md ringkas dengan
detail di `references/`, sumber tercatat per poin, tidak kontradiksi
antar skill, sudah diuji dengan task nyata, ada catatan tanggal refresh
untuk konten teknis (API/versi software).

---

## 3. Cara Mengisi Skill — Scraping dan Alternatifnya

**Scraping** sah dilakukan untuk **dokumentasi resmi & gratis**
(Godot docs, Aseprite API, PixelLab docs) — bukan untuk forum, YouTube,
Discord, atau konten berbayar (ToS dan hak cipta jadi masalah di area
itu).

**Alur yang efisien saat skill dipecah granular:** riset/scraping luas
sekali jalan → kategorisasi/tagging hasil → distribusi ke file skill
masing-masing. Bukan scraping ulang per skill (boros, berisiko tidak
konsisten).

**Alternatif selain scraping** (poin 2 dan 7 dibahas lebih dalam):
1. Kurasi dari pengalaman/kerja sendiri (post-mortem tiap task, contoh
   baik/buruk dari hasil sendiri) — paling relevan karena spesifik ke
   proyek.
2. **Dokumentasi resmi via API/SDK langsung** — lebih bersih dari
   scraping HTML: XML class reference Godot (`doc/classes/*.xml`),
   `ClassDB` introspeksi runtime, repo API reference Aseprite, resource
   MCP PixelLab (`pixellab://docs/...`) — selalu sinkron ke versi yang
   benar-benar dipakai.
3. Sumber berbayar yang dibeli sendiri, dibaca & dirangkum manual.
4. Diskusi dengan komunitas/expert, dicatat manual.
5. Feedback loop dari playtesting nyata.
6. Prompt engineering yang lebih baik (bukan nambah pengetahuan, nambah
   efektivitas permintaan).
7. **Fine-tuning** — satu-satunya yang benar-benar mengubah model secara
   permanen (beda dari skill/context injection). **Dinilai tidak sepadan**
   untuk skala proyek ini: butuh dataset besar (ratusan-ribuan contoh),
   kemungkinan tidak terbuka untuk model di Antigravity, maintenance jauh
   lebih berat dibanding edit file skill. Baru layak dipertimbangkan kalau
   proyek sudah besar dan instruksi teks sudah mentok tidak cukup.

---

## 4. Multi-Agent: Yang Nyata vs Yang Halusinasi

**Kejadian sebelumnya** (15 agent "rapat", agent yang "muncul sendiri
sesuai bidang") kemungkinan besar adalah **satu model menulis narasi
berlabel peran dalam satu context** — bukan orkestrasi teknis sungguhan.
Ciri-cirinya: tidak ada artifact terpisah per agent, semua "laporan"
selalu sukses mulus, tidak bisa diverifikasi independen.

**Yang nyata:** Antigravity punya **Agent Manager** — spawn, monitor,
koordinasi agent sungguhan dengan context/conversation history terpisah,
bisa kerja paralel di direktori berbeda, hasilnya berupa artifact
konkret yang bisa direview satu-satu.

**Agent tidak punya kesadaran** — tidak ada "diri" yang menetap atau
memutuskan sendiri untuk terlibat. Kalau ada agent yang "muncul sesuai
bidangnya", itu harus berasal dari **mekanisme routing/klasifikasi
eksplisit** (aturan tertulis), bukan insting model.

**Pola arsitektur yang benar:** hub-and-spoke (semua komunikasi lewat
Supervisor), bukan full-mesh (semua agent saling bicara bebas) — full-mesh
menciptakan race condition, context membengkak, dan otoritas keputusan
tidak jelas.

**Cara verifikasi setup real vs teater:**
cek tool call log (bukan cuma teks laporan), minta bukti konkret (path
file, diff), perhatikan apakah ada kegagalan yang wajar terjadi (semua
selalu sukses 100% = mencurigakan), cek dokumentasi resmi fitur terkait.

---

## 5. Struktur AGENTS.md yang Disusun (lihat file AGENTS.md)

Ringkasan isi yang sudah dibangun bertahap:

- **Bagian 0** — Prinsip dasar semua agent: wajib artifact, tidak boleh
  percaya klaim "selesai" dari giliran sebelumnya tanpa verifikasi ulang,
  scope kerja mengikuti kriteria selesai eksplisit, tetap dalam skill/tool
  yang di-assign.
- **Bagian 1** — Supervisor Agent (Orchestrator): delegasi + verifikasi,
  TIDAK mengerjakan sendiri task teknis, tidak boleh tandai selesai tanpa
  cek artifact.
- **Bagian 1.1** — Tabel routing task → agent, berbasis trigger keyword
  eksplisit (bukan insting Supervisor). Task yang tidak cocok baris
  manapun → tanya balik ke user, bukan ditebak.
- **Bagian 1.2** — Protokol Pola B (dual-perspective independen): dipicu
  HANYA untuk keputusan struktural besar/ambigu, bukan task rutin.
  Format output wajib supaya bisa dibandingkan apple-to-apple. Prosedur
  rekonsiliasi 3 skenario — Supervisor **tidak berwenang** memutuskan
  sendiri kalau dua hasil bertentangan, wajib eskalasi ke user.
- **Bagian 2** — Game Designer (peran NPC, struktur map, pacing).
- **Bagian 2.1** — Psychology Agent: **consultant lintas bidang**, bukan
  pemilik tahap sendiri. Cuma direview di atas draft yang sudah ada
  (default Pola A), dipanggil hanya sesuai baris consult di tabel
  routing — bukan "ikut semua task".
- **Bagian 3** — Art Director (prompt PixelLab, checkpoint manual wajib
  karena PixelLab dipakai via plugin, bukan MCP otomatis).
- **Bagian 4** — Pixel Editor (Aseprite MCP kustom, cleanup & export).
- **Bagian 5** — Godot Engineer (Godot MCP kustom, import & wiring scene).
- **Bagian 6** — Contoh alur delegasi end-to-end (kasus "buat NPC baru").
- **Bagian 7** — Cross-check dokumen, dipicu manual (`/cross-check-docs`),
  BUKAN standing rule otomatis di background.
- **Bagian 8** — Catatan evaluasi diri: tanda-tanda setup mulai balik jadi
  teater (semua sukses tanpa kegagalan, laporan tanpa artifact spesifik,
  tidak ada checkpoint manual di titik yang seharusnya manual).

**Belum ditambahkan ke file** (dibahas tapi belum dieksekusi ke dokumen):
- Role **QC Agent** (checklist Visual QC / Functional QC / Consistency
  QC, status PASS/REJECTED per poin, gate wajib sebelum handoff, fungsi
  pattern logging ke `references/qc-patterns.md`)
- Bagian **adaptive problem solving** yang lebih aman (decision tree
  berjenjang dengan whitelist sumber dan batas eskalasi), sebagai
  pengganti instruksi lama yang terlalu longgar

---

## 6. Kenapa Instruksi Standing Rule Sering Tidak Jalan Otomatis

Masalah yang dialami: aturan seperti "selalu cek silang semua dokumen"
atau "boleh scraping mandiri kalau kurang info" tidak konsisten
dijalankan, dan pola "3x bilang cukup, ke-4 dengan prompt beda baru mau
kerja lagi".

**Penyebab:**
1. Instruksi **unbounded** (tidak ada kriteria selesai) → model melakukan
   pass dangkal lalu anggap cukup.
2. Model menghindari over-execute pada instruksi standing yang tidak
   dipicu eksplisit di prompt saat itu.
3. **Model mempercayai klaim "selesai" dari giliran sebelumnya** tanpa
   verifikasi ulang — prompt yang mirip dibaca sebagai "tidak ada info
   baru", prompt yang beda dibaca sebagai task baru dari nol.
4. Kemungkinan dibatasi mekanisme approval/permission sistem untuk aksi
   berisiko seperti network call mandiri.

**Solusi:** ubah dari "aturan umum selamanya" jadi checklist dengan
kriteria selesai eksplisit + bukti per poin; tambah instruksi eksplisit
anti-percaya-klaim-sendiri; ganti standing rule pasif jadi workflow yang
di-trigger eksplisit (slash command); pertimbangkan automasi non-LLM
(script/git hook) untuk hal yang sifatnya mekanis, bukan judgment.

---

## 7. QA vs QC

- **QA (Quality Assurance)** = fokus proses, preventif — "apakah cara
  kerja kita benar supaya bug tidak muncul?"
- **QC (Quality Control)** = fokus produk, reaktif — "apakah hasil ini
  ada bug-nya?"
- Yang sudah dirancang sejauh ini murni QC (menguji artifact).
- **Keputusan:** tidak perlu agent QA terpisah untuk skala proyek
  sekarang — fungsi QA sudah tersebar di prinsip bagian 0 AGENTS.md
  (mencegah kesalahan proses lewat aturan kerja). Cukup tambahkan fungsi
  **pattern logging** di QC Agent (mencatat pola reject berulang di
  `references/qc-patterns.md`) sebagai jembatan ke perbaikan proses,
  tanpa perlu role baru yang berisiko jadi kosong.

---

## 8. AI "Melihat" (Multimodal)

Model bisa memproses gambar (screenshot), tapi ini **snapshot statis**
di satu momen, bukan aliran visual real-time dan tidak ada memori visual
persisten otomatis antar momen.

Implementasi nyata yang relevan: screenshot Godot scene untuk verifikasi
(kalau Godot MCP kustom support capture), review visual hasil
PixelLab/Aseprite oleh QC Agent, atau kamu kirim screenshot manual saat
minta feedback. Sama seperti prinsip lain: klaim "sudah saya lihat,
bagus kok" tanpa gambar konkret yang ditampilkan = sinyal bahaya yang
sama seperti kasus roleplay sebelumnya.

---

## 9. Standar Kelayakan Publish Game

- **Tidak ada "ujian kelayakan" resmi** seperti sertifikasi console —
  untuk platform seperti Steam, prosesnya cuma cek kepatuhan legal (tidak
  ada aset curian/trademark issue) dan akurasi halaman toko, **bukan**
  penilaian kualitas gameplay.
- **Standar teknis (QA pre-launch)** yang relevan: kompatibilitas
  resolusi/window mode, dukungan controller, first-time player
  experience, save/load tanpa corrupt/softlock, tidak crash di skenario
  umum — ini yang bisa dipetakan ke Functional QC.
- **Standar substansi** (loop gameplay jelas, tidak ada dead-end,
  scope yang selesai bukan ambisius setengah jadi) — sebagian tercakup
  skill desain yang sudah ada.
- **Yang tidak bisa diverifikasi AI sepenuhnya:** apakah game
  benar-benar menyenangkan dan mudah dipahami pemain baru — ini butuh
  playtest oleh orang nyata yang belum pernah lihat game-nya, bukan
  cuma dicek lewat checklist otomatis.

---

## 10. Kejujuran Agent — Bukan Instruksi, Tapi Struktur Verifikasi

Tidak ada kalimat "tolong jujur ya" yang membuat model otomatis jujur.
Kejujuran dibangun lewat mekanisme yang sudah tersebar di seluruh
AGENTS.md: artifact wajib, QC terpisah dari eksekutor, kriteria selesai
eksplisit, kewaspadaan pada pola "selalu sukses 100%", dan kebiasaan
minta bukti spesifik saat ragu.

---

## 11. Model Claude vs Gemini di Antigravity, dan Menghemat Kuota

- Claude (terutama Opus dengan Thinking) memang unggul di beberapa
  benchmark (SWE-bench, tool-augmented reasoning, task knowledge-intensive)
  dibanding Gemini 3.1 Pro — bukan cuma perasaan subjektif.
- **Tidak bisa "mengubah" Gemini supaya berperilaku seperti Claude** —
  dua model dari perusahaan dan arsitektur berbeda sepenuhnya.
- Claude boros kuota terutama karena **mode Thinking** menghasilkan
  ribuan token reasoning tersembunyi yang ikut dihitung — dilaporkan
  4x lebih boros dibanding model Gemini.
- **Cara hemat kuota** (angka spesifik adalah estimasi komunitas, bukan
  resmi dari Google):
  1. Matikan Extended Thinking kecuali task benar-benar butuh reasoning
     dalam.
  2. Pakai model murah (Gemini Flash) sebagai default, Claude hanya untuk
     task yang penting.
  3. Bersihkan file aturan proyek (AGENTS.md/gemini.md) — file ini ikut
     disuntik ke tiap prompt, makin panjang makin boros.
  4. Cek `.antigravityignore` supaya indexing background tidak memakan
     folder besar yang tidak perlu (asset mentah, build output).
  5. Cek toggle AI Credits/overages di Settings → Models — set "Never"
     kecuali aktif dipantau.
  6. Kuota Claude dan Gemini terpisah — kalau Claude habis, tetap bisa
     lanjut kerja pakai Gemini.
  7. Edit & regenerate prompt yang salah, jangan kirim koreksi susulan
     bertumpuk (histori panjang = makin mahal tiap giliran).

**Soal OpenRouter/proxy pihak ketiga:** secara teknis memungkinkan
(ada beberapa proyek komunitas), tapi ini modifikasi tidak resmi dengan
risiko ToS, stabilitas, dan keamanan kredensial yang perlu ditanggung
sendiri. **Diputuskan tidak dipakai** untuk sekarang.

---

## 12. Temuan dari 3 Repo GitHub Proyek Nyata (dicek langsung, bukan asumsi)

Repo berikut sudah dicek isinya — ini konteks **nyata** proyek user, bukan
lagi contoh hipotetis seperti sepanjang diskusi sebelumnya. Sesi
berikutnya WAJIB memakai ini sebagai konteks utama, bukan cuma kerangka
generik di bagian 1-11 di atas.

### 12.1 `lentera-pudar` (repo utama — Godot project)

Nama proyek sebenarnya: **Lentera Pudar** — 2D Pixel RPG dungeon
top-down. Struktur folder: `.agents/`, `Assets/`, `Scenes/`, `Scripts/`,
`Shaders/`, `addons/lentera_bridge/`, `assets_raw/`. Juga ada file
`build_godot_scene.py`, `capture_aseprite.ps1`, `generate.gd`,
`generate_frames.gd`, `merge_pixellab_frames.lua`, `qc_check.lua`,
`qc_report.txt`, `project.godot` — menandakan pipeline visual dan QC
sudah mulai diimplementasi secara nyata (bukan cuma rencana).

**Repo ini SUDAH punya `AGENTS.md` sendiri yang jauh lebih spesifik**
dari kerangka generik yang kita susun di file `AGENTS.md` terpisah.
Isinya (dirangkum, bukan kutipan langsung):

- **Lore & identitas:** Engine Godot 4.7.1, gaya pixel art 32×32px
  semi-detailed, tema misterius-hangat, palet warna dominan (kuning
  hangat, biru dingin, netral gelap) via `PointLight2D` &
  `CanvasModulate`. Lore inti: "Kutukan Pudar" (wabah yang membekukan
  warga jadi patung kristal es biru), protagonis tunggal class-less
  dengan syal kuning (sumber cahaya) dan tangan kiri berperban urat es
  biru.
- **Larangan roleplay eksplisit:** AGENTS.md proyek ini secara tegas
  melarang "roleplay, persona fiktif, sebutan berlebihan, atau
  mensimulasikan diskusi antar agen" — ini **konsisten** dengan
  peringatan yang sudah kita bahas panjang lebar soal halusinasi
  multi-agent (bagian 4 rekap ini). User sudah menerapkan pelajaran itu
  duluan di level project rules.
- **Pipeline visual:** Pixellab MCP (`create_character`, mode v3, 8
  arah sejati, parameter detail seperti `body`, `size`, `view`,
  `outline`, `detail`) → Aseprite (cleanup, animation tagging) → Godot
  (auto-import via Aseprite Wizard Plugin + Lighting/Shader).
- **Self-research & adaptive problem solving** sudah diatur eksplisit:
  wajib riset mandiri sebelum menyatakan "tidak bisa", dan **batas
  eksplisit maksimal 3 kali gagal beruntun** pada pendekatan yang sama
  sebelum wajib ubah strategi dan lapor ke user — ini **persis** pola
  "decision tree dengan eskalasi" yang kita rancang di bagian 6 rekap
  ini, ternyata sudah diimplementasi user duluan di project nyata.
- **Validasi wajib dengan bukti nyata:** `take_screenshot` saat
  playtest, atau log tanpa error merah — konsisten dengan prinsip
  artifact-wajib yang jadi tema besar sepanjang diskusi kita.
- **Arsitektur direktori Godot:** `res://Scenes/`, `res://Scripts/`,
  `res://Assets/`. Komunikasi lintas sistem WAJIB via Global Event Bus
  (`GameEvents.gd` Autoload) — dilarang keras `get_node("../Player")`
  langsung antar node.
- **GDScript wajib static typing ketat.**
- **Penamaan animasi:** pola `[aksi]_[arah]`, 8 arah penuh (termasuk
  `_left`) karena pakai Pixellab v3.
- **Skills & subagents sudah disebut di AGENTS.md ini:** skill
  disimpan di `.agents/skills/` (termasuk contoh nyata:
  `godot_rpg_architecture`, `visual_pipeline_automation`), subagent
  browser didelegasikan riset eksternal kompleks. Ada juga **fitur
  `/learn`** — perintah user untuk menyimpan solusi teknis sulit ke
  memori AI (konsep "otodidak").
- **Scope kerja saat ini SANGAT sempit dan disiplin:** seluruh sistem
  combat/musuh/NPC/narasi sengaja **dihapus sementara**. Fokus tunggal:
  visual & animasi Protagonis sampai 100% lolos uji coba di Godot,
  sebelum apapun lainnya dikerjakan. Aturan keras: "jangan menyiapkan
  sistem yang belum diperlukan."
- **Sinkronisasi wajib lintas 3 direktori** disebutkan eksplisit di
  AGENTS.md ini: `Lentera-Pudar`, `lentera-godot-mcp`,
  `lentera-aseprite-mcp` — jadi user sendiri sudah punya kesadaran
  bahwa ketiga repo ini harus dijaga konsisten satu sama lain.

### 12.2 `lentera-godot-mcp` (MCP server kustom untuk Godot)

Bahasa: TypeScript (ada `tsconfig.json`, `package.json`). Struktur:
folder `godot-plugin/` dan `src/`, plus file test WebSocket
(`test_ws.cjs`, `test_ws.js`) — mengindikasikan komunikasi MCP↔Godot
kemungkinan besar lewat WebSocket, dengan ada plugin sisi Godot juga
(bukan cuma server MCP berdiri sendiri). **Belum ada README** —
deskripsi/dokumentasi publik repo ini kosong. Isi detail `src/`
(daftar tool/fungsi lengkap) belum bisa diakses lebih dalam saat
sesi ini (dibatasi robots.txt GitHub untuk crawl direktori
bertingkat) — sesi berikutnya perlu baca langsung dari lokal atau
minta user paste isi file kunci.

### 12.3 `lentera-aseprite-mcp` (MCP server kustom untuk Aseprite)

Bahasa: TypeScript juga. Struktur: folder `lua-extension/` dan `src/`
— mengonfirmasi dugaan sebelumnya bahwa server ini kemungkinan
memanggil Aseprite lewat scripting Lua (sesuai cara resmi Aseprite
diotomatisasi). **Juga belum ada README.** Sama seperti di atas, isi
detail fungsi di `src/` belum terbaca penuh di sesi ini.

### 12.4 Implikasi penting untuk sesi berikutnya

- **Ada DUA AGENTS.md yang perlu direkonsiliasi**, bukan cuma satu:
  (a) `AGENTS.md` generik hasil diskusi kita (Supervisor/Game
  Designer/Art Director/dst dengan Pola A/B, QC Agent, dll — bersifat
  kerangka umum), dan (b) `AGENTS.md` asli di repo `lentera-pudar`
  (jauh lebih spesifik, sudah dipakai produksi, dengan lore dan aturan
  scope ketat). **Sesi berikutnya harus memutuskan bersama user: apakah
  digabung jadi satu, atau tetap dipisah dengan peran berbeda** (misal
  AGENTS.md repo = aturan project-specific yang sudah battle-tested,
  file rekap kita = referensi konsep/framework tambahan).
- Banyak konsep yang didiskusikan di sesi ini (adaptive problem
  solving dengan batas eskalasi, larangan roleplay, validasi via
  artifact/screenshot, skill terpisah di `.agents/skills/`) **ternyata
  sudah diimplementasi user duluan** di AGENTS.md repo asli — sesi
  berikutnya sebaiknya **evaluasi kesesuaian**, bukan mengusulkan dari
  nol seolah-olah ini belum ada.
- Role **QC Agent** yang di rekap ini masih berstatus "didiskusikan
  tapi belum masuk dokumen" — sementara di repo asli sudah ada
  `qc_check.lua` dan `qc_report.txt` yang mengindikasikan QC sudah
  jalan dalam bentuk **script**, bukan cuma role AI. Perlu diperjelas
  di sesi berikutnya: apakah QC yang dimaksud user itu script otomatis
  (yang sudah ada), agent AI terpisah (yang baru didiskusikan), atau
  kombinasi keduanya.
- Repo `lentera-godot-mcp` dan `lentera-aseprite-mcp` **belum punya
  README** — kalau user ingin repo ini dinilai lebih dalam (soal
  desain, kelengkapan fungsi, dsb), sesi berikutnya perlu akses ke isi
  `src/` secara langsung (lewat file lokal atau user paste kode),
  karena crawl otomatis GitHub dibatasi robots.txt untuk direktori
  bertingkat.

---

## Yang Masih Perlu Diputuskan/Dieksekusi

- [ ] Menambahkan role QC Agent secara resmi ke `AGENTS.md` (checklist
      per jenis QC + pattern logging)
- [ ] Menambahkan bagian adaptive problem solving versi aman (decision
      tree + whitelist sumber) ke `AGENTS.md`, menggantikan poin 2 lama
- [ ] Mengisi `style-guide` dengan detail konkret (resolusi, palette,
      frame count baku proyek)
- [ ] Menyesuaikan referensi nama fungsi di role Godot Engineer & Pixel
      Editor supaya merujuk fungsi asli di MCP kustom kamu
- [ ] Membuat file `references/design-decisions.md` (dirujuk di protokol
      Pola B, belum benar-benar dibuat)
- [ ] **Rekonsiliasi AGENTS.md generik (dari diskusi ini) dengan
      AGENTS.md asli di repo `lentera-pudar`** — lihat bagian 12.4,
      ini prioritas utama sebelum lanjut menambah role baru
- [ ] Klarifikasi apakah QC yang dimaksud = script (`qc_check.lua` yang
      sudah ada) atau agent AI terpisah (yang baru didiskusikan)
- [ ] Membaca isi `src/` di `lentera-godot-mcp` dan
      `lentera-aseprite-mcp` secara langsung (crawl GitHub otomatis
      dibatasi robots.txt) untuk tahu daftar tool/fungsi MCP yang
      benar-benar sudah ada, sebagai dasar gap analysis yang akurat
      (bukan tebakan generik seperti yang dibahas di sesi ini)

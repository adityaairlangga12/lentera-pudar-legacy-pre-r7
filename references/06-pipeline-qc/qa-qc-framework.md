# Kerangka QA/QC — Lentera Pudar: 3D Action RPG Edition
### Standar Kontrol Kualitas, Definition of Done (DoD), Stage-Gate Process & Protokol Verifikasi AI

Dokumen ini adalah **lapisan kontrol kualitas mutlak** yang memastikan setiap aset 3D, material, animasi, level, audio, dan sistem gameplay memenuhi standar komersial (*Steam-Ready Grade*).

---

## 1. Perbedaan Mendasar QA vs QC

```
   [ QA: QUALITY ASSURANCE ]                [ QC: QUALITY CONTROL ]
• Memastikan PROSES benar sejak awal.    • Memeriksa HASIL AKHIR aset.
• Naming convention, unit scale,         • Validasi file di disk, topology,
  folder structure, observability          bone roll, render screenshot,
  sebelum mutasi kode/mesh.                dan performa runtime 60 FPS.
```

---

## 2. Enam Pilar Definition of Done (DoD) per Jenis Aset

Setiap AI Agent dan developer wajib memverifikasi checklist berikut sebelum menyatakan suatu task selesai:

### A. DoD — Model 3D (Blender ➔ UE5)
- [ ] Nama aset mengikuti standar konvensi baku (`SK_Kaelen_Body`, `SM_Crypt_Pillar_01`).
- [ ] Topologi bersih: Nol non-manifold geometry, tidak ada n-gon bermasalah pada area deformasi.
- [ ] UV Unwrap bersih tanpa overlap tidak disengaja; seam ditempatkan tersembunyi.
- [ ] **Texel Density Terstandarisasi**: 512 px/m untuk Hero & Boss, 256 px/m untuk Environment Props (sesuai [environment-modular-techniques.md](file:///d:/GodotProjects/Lentera-Pudar/references/04-art-3d/environment-modular-techniques.md)).
- [ ] Skala dan orientasi benar saat diimpor ke UE5 ($1\text{ unit} = 1\text{ cm}$, $+Z$ Up, $+Y$ Forward).
- [ ] LOD tersedia untuk aset berulang (prop lingkungan dan musuh umum).
- [ ] Custom collision mesh sudah dikonfigurasi (bukan auto-convex kasar untuk geometri kompleks).
- [ ] Anggaran poligon (*Poly Budget*) sesuai kategori (**40.000–60.000 tris (LOD0) untuk Hero Character**, 50.000–80.000 tris untuk Boss, 8.000–15.000 tris untuk Musuh Umum — sesuai [style-guide.md](file:///d:/GodotProjects/Lentera-Pudar/references/04-art-3d/style-guide.md) Bab 6).

### B. DoD — Material & Shaders (The Triad)
- [ ] Struktur PBR lengkap (Base Color, Roughness, Metallic, Normal).
- [ ] Material Kristal Es: Parameter SSS (*Subsurface Scattering*) diverifikasi dari $\ge 2$ sudut pencahayaan berbeda.
- [ ] Material Emissive (Syal Aina 2700K & Kristal Es 6500K): Terhubung ke *Material Parameter Collection* (MPC), bukan nilai statis.
- [ ] Kontras suhu warna Kelvin (2700K vs 6500K) diverifikasi secara visual pada scene UE5.
- [ ] Lolos uji simulasi filter buta warna (*Colorblind Accessibility Check*).

### C. DoD — Rigging, Biomekanika & Animasi
- [ ] Hierarki Skeleton humanoid kompatibel dengan UE5 Control Rig dan Animation Retargeting.
- [ ] **Tri-Layer Biomechanical Shingling (ADR-041)**: Uji fleksi siku $145^\circ$ pada lengan es Kaelen terbukti bebas dari distorsi elastis/karet (*zero rubbery deformation*).
- [ ] Rantai tulang syal (*5-Bone Spring Chain*) diuji pada 3 skenario gerakan (Idle, Jog, Evade Dash) tanpa clipping parah ke tubuh.
- [ ] **Handoff Kain Syal & Pre-Roll (ADR-040)**: Transisi cutscene ke gameplay terbukti mulus via *Cloth Physical Blend Weight Curve* 0.5s dan *5-Frame Physics Pre-Roll Warm-Up*.
- [ ] Animasi combat memiliki frame *anticipation*, *impact*, dan *follow-through* (12 Prinsip Animasi Disney).
- [ ] **Hit-Stop GAS Presisi 50ms**: Durasi hentakan benturan `UAbilityTask_HitStop` terverifikasi konstan 50ms di 30 FPS, 60 FPS, maupun 120 FPS.
- [ ] Locomotion Blend Tree berjalan mulus tanpa fenomena *foot sliding*.
- [ ] Inverse Kinematics (IK) kaki aktif menyesuaikan kontur lantai dungeon yang tidak rata.

### D. DoD — Audio & Binaural Landscape
- [ ] Target loudness terstandarisasi pada $-14$ s.d. $-16$ LUFS.
- [ ] Dynamic Audio Ducking ($-6\text{ dB}$) aktif saat Aina atau bisikan jiwa beku berbicara.
- [ ] Tata suara 3D Binaural Spatialization diverifikasi menggunakan headphone fisik.
- [ ] Nol distorsi atau digital clipping pada volume puncak.

### E. DoD — Level & Sektor Dungeon
- [ ] *Critical Path* (jalur utama) dan *Optional Path* (jalur rahasia via Eyepatch) terbedakan jelas secara geometri.
- [ ] Minimal satu *Landmark Visual Dominan* terlihat dari berbagai sudut utama sektor (Zero-Clutter HUD navigation).
- [ ] World Partition Level Streaming berjalan mulus tanpa *mesh pop-in* yang mengganggu.
- [ ] *Breather Room* tersedia secara proporsional di antara arena pertarungan intens (Tension-Release Cycle).
- [ ] Performa solid 60 FPS lock di area paling padat geometri/partikel.

### F. DoD — Sistem Gameplay, Combat & FSM
- [ ] FSM/Behavior Tree teruji pada seluruh state dan edge case (contoh: Dash saat Curse Meter penuh).
- [ ] Parry Window terdokumentasi dalam angka frame presisi (12 frame / 0.2 detik).
- [ ] Nol kondisi *soft-lock* (pemain terjebak tanpa bisa melanjutkan).
- [ ] Sistem Save/Load Atomic teruji stabil minimal 10x siklus tanpa korupsi data.

---

## 3. The 8-Stage Gate Process (Gerbang Milestone)

```
[GATE 0: Pra-Produksi] ➔ GDD, Moodboard, Teori, Tools, QA Framework disahkan.
       ↓
[GATE 1: Fondasi Teknis] ➔ Blender MCP + UE5 Python Scripting aktif, Naming standard terkunci.
       ↓
[GATE 2: Grey-Box Prototype] ➔ Layout Sektor 1 kasar, Core Combat loop Playable.
       ↓
[GATE 3: Vertical Slice] ➔ Sektor 1 final art, audio binaural, 1 Boss Lord Alden, 6-DoD Pass.
       ↓
[GATE 4: Produksi Penuh] ➔ Replikasi pipeline ke Sektor 2, 3, 4, dan 5.
       ↓
[GATE 5: Alpha] ➔ Game playable dari awal hingga akhir, zero blocking bugs.
       ↓
[GATE 6: Beta] ➔ Feature complete, balancing kesulitan, playtest eksternal.
       ↓
[GATE 7: Release Candidate] ➔ Final QC Pass, Steamworks Packaging, Steam Deck Verified.
```

---

## 4. Klasifikasi Severity Bug

| Severity | Definisi | Contoh Kasus | Aturan Penanganan |
|---|---|---|---|
| 🔴 **Blocking** | Progres game terhenti total atau crash fatal. | Softlock di Altar Duka, crash saat streaming level. | Wajib difix instan sebelum gate berikutnya. |
| 🟠 **Critical** | Merusak pengalaman inti gameplay/narasi. | Curse Meter tidak merespon damage, clipping parah cutscene. | Wajib difix sebelum masuk fase Beta. |
| 🟡 **Major** | Mengganggu kenyamanan visual/audio tapi tidak merusak fungsi. | Transisi animasi kaku, ducking audio terlambat 1 detik. | Wajib difix sebelum Release Candidate. |
| 🟢 **Minor** | Isu kosmetik ringan di area tersembunyi. | Tekstur resolusi rendah di sudut dinding terpencil. | Masuk backlog perbaikan berkala. |

### Format Wajib Pencatatan Bug
Setiap bug yang ditemukan (di severity manapun) wajib dicatat dengan field terstruktur berikut, bukan sebagai catatan naratif bebas:
- **ID & Severity**: Sesuai klasifikasi tabel di atas (contoh: `BUG-BLK-001`, `BUG-CRT-002`, `BUG-MAJ-003`, `BUG-MIN-004`).
- **Langkah Reproduksi**: Urutan aksi persis untuk memicu bug (Langkah 1 ➔ Langkah 2 ➔ Langkah 3).
- **Kondisi**: Sektor/area, versi build/commit git, platform/hardware (jika relevan).
- **Status Lifecycle**: `Open` ➔ `Fixed` ➔ `Verified` (status `Fixed` tanpa `Verified` ulang oleh proses/agent penguji terpisah TIDAK dianggap selesai dan tidak boleh menutup item di Stage-Gate manapun).

---

## 5. Protokol Verifikasi AI Agent & Anti-Theater

1. **Observability-First Mandate**: AI Agent wajib memanggil tool inspeksi sebelum melakukan modifikasi file atau ekspor 3D.
2. **No Auto-Merge**: Seluruh kode, mesh, dan blueprint dari AI Agent harus melalui review dan verifikasi fisik di editor.
3. **Wajib Bukti Fisik Konkret**: Setiap laporan selesai wajib menyertakan path file aktual, data parameter numerik, atau screenshot visual.
4. **Larangan Self-Grading**: AI Agent yang membuat/mengedit suatu aset, sistem, atau dokumen **DILARANG** menulis status "✅ Lolos QC", "Passed", atau "100% Terverifikasi" pada laporan yang ia buat sendiri untuk hasil kerjanya sendiri. Status maksimal yang boleh ditulis AI pembuat adalah **"Ready for QC / Menunggu Verifikasi"**. Status "Verified/Lolos" hanya boleh dicantumkan setelah proses QC dijalankan sebagai langkah terpisah (baik oleh reviewer manusia, atau oleh instruksi AI yang eksplisit diminta mencari masalah, bukan mengonfirmasi kelengkapan).

---

## 6. Validasi Emosional & Playtesting Manusia (Lihat [emotional-playtesting.md](file:///d:/GodotProjects/Lentera-Pudar/references/06-pipeline-qc/emotional-playtesting.md))
- **Fungsional vs Emosional**: Pengujian teknis 6-DoD memastikan game bebas bug, sedangkan validasi emosional memastikan tema 5 Tahap Berduka dirasakan secara otentik oleh pemain.
- **Kerangka Intended vs Perceived Emotion**: Menganalisis kesenjangan (*gap analysis*) antara emosi yang dirancang dengan respon alami playtester.
- **Mandat Batasan AI Agent**: Kepatuhan teknis AI terhadap parameter desain **TIDAK MENGGANTIKAN** validasi emosional playtester manusia. Setiap beat naratif kunci wajib ditandai status `[Needs Human Playtest Validation]`.

---

## 7. Protokol Regression Check

Sebelum suatu perubahan pada sistem inti dinyatakan selesai, wajib dilakukan pengecekan ulang terhadap seluruh sistem lain yang bergantung padanya. Sistem inti yang wajib memicu regression check meliputi: timing combat (hit-stop, parry window), nilai numerik Curse Meter, physics solver (cloth/XPBD), dan parameter Style Guide (poly budget, texel density, palet warna).

**Matriks Pemicu Wajib Regression Check**:
- **Ubah nilai hit-stop / frame timing** ➔ Cek ulang sinkronisasi parry window, animasi combat kinetic chain, dan haptic feedback.
- **Ubah laju / batas Curse Meter** ➔ Cek ulang seluruh sistem yang mereferensikannya (*Freeze of Despair*, *Breather Room recovery*, *Sealed Eyepatch*, *Ice Talons strike*).
- **Ubah parameter cloth / XPBD physics** ➔ Cek ulang deformasi Syal Aina, jubah kelana Kaelen, dan *Hybrid Hair System*.
- **Ubah skema level / transisi arena** ➔ Cek ulang checkpoint respawn, *World Partition streaming*, dan rute *Local World Awareness*.

Setiap laporan QC untuk perubahan sistem inti wajib menyertakan bagian **"Sistem Terdampak & Hasil Regression Check"**, terpisah dari checklist DoD utama.

---

## 8. Protokol Anti-False-Negative (Adversarial QC Mandate)

QC yang hanya memverifikasi checklist DoD (kepatuhan terhadap spesifikasi) TIDAK CUKUP untuk menemukan bug — checklist memverifikasi "apakah sudah sesuai rancangan", bukan "apakah bisa dijebol". Setiap sesi QC wajib menyertakan usaha aktif mencari kegagalan, dengan aturan berikut:

1. **Wajib Coba Minimal 3 Skenario Adversarial per Sistem yang Diuji**:
   - Skenario yang sengaja dirancang untuk memicu *edge case*, tabrakan state logic, atau input ekstrem — bukan jalur pemakaian normal.
   - *Contoh untuk sistem respawn*: Apa yang terjadi kalau Kaelen mati persis saat animasi interaksi Altar Duka sedang berjalan? Kalau kalah 2 kali berturut-turut dalam durasi $<1\text{ detik}$? Kalau respawn terjadi saat kamera cutscene sedang aktif?
2. **Kewajiban Dokumentasi Skenario Adversarial**:
   - Seluruh skenario adversarial yang diuji wajib dicantumkan di laporan QC, baik yang memicu kegagalan maupun yang tidak.
   - Format wajib: `"Dicoba: [deskripsi skenario adversarial] ➔ Hasil: [tidak ada anomali / ditemukan bug]"`
   - Laporan "Nol Bug" tanpa rincian skenario adversarial yang dicoba dianggap **TIDAK VALID**.
3. **Penandaan First-Pass Clean**:
   - Jika laporan QC melaporkan "Nol Bug" pada percobaan pertama suatu sistem yang baru dibuat/diubah, statusnya **WAJIB** ditandai sebagai:  
     `⚠️ First-Pass Clean — Perlu Verifikasi Independen`  
     (DILARANG langsung memberi status `Verified / Approved`).
   - Status **`Verified`** penuh baru sah diberikan setelah minimal 2 sesi QC terpisah (dengan skenario adversarial berbeda) sama-sama tidak menemukan masalah.
4. **Pelacakan Pola Mencurigakan (Meta-Audit Trigger)**:
   - Jika 3 laporan QC berturut-turut (untuk sistem berbeda) semuanya melaporkan "Nol Bug", ini **WAJIB memicu audit meta** terhadap kriteria QC — mengevaluasi apakah penguji/AI terlalu pasif atau bias meloloskan tanpa pengujian mendalam.

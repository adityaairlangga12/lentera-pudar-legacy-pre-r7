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
- [ ] Skala dan orientasi benar saat diimpor ke UE5 ($1\text{ unit} = 1\text{ cm}$, $+Z$ Up, $+Y$ Forward).
- [ ] LOD tersedia untuk aset berulang (prop lingkungan dan musuh umum).
- [ ] Custom collision mesh sudah dikonfigurasi (bukan auto-convex kasar untuk geometri kompleks).
- [ ] Anggaran poligon (*Poly Budget*) sesuai kategori (**40.000–60.000 tris (LOD0) untuk Hero Character**, 50.000–80.000 tris untuk Boss, 8.000–15.000 tris untuk Musuh Umum — sesuai [style-guide.md](file:///d:/GodotProjects/Lentera-Pudar/references/style-guide.md) Bab 6).

### B. DoD — Material & Shaders (The Triad)
- [ ] Struktur PBR lengkap (Base Color, Roughness, Metallic, Normal).
- [ ] Material Kristal Es: Parameter SSS (*Subsurface Scattering*) diverifikasi dari $\ge 2$ sudut pencahayaan berbeda.
- [ ] Material Emissive (Syal Aina 2700K & Kristal Es 6500K): Terhubung ke *Material Parameter Collection* (MPC), bukan nilai statis.
- [ ] Kontras suhu warna Kelvin (2700K vs 6500K) diverifikasi secara visual pada scene UE5.
- [ ] Lolos uji simulasi filter buta warna (*Colorblind Accessibility Check*).

### C. DoD — Rigging & Animasi
- [ ] Hierarki Skeleton humanoid kompatibel dengan UE5 Control Rig dan Animation Retargeting.
- [ ] Rantai tulang syal (*5-Bone Spring Chain*) diuji pada 3 skenario gerakan (Idle, Jog, Evade Dash) tanpa clipping parah ke tubuh.
- [ ] Animasi combat memiliki frame *anticipation*, *impact*, dan *follow-through* (12 Prinsip Animasi Disney).
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

---

## 5. Protokol Verifikasi AI Agent & Anti-Theater

1. **Observability-First Mandate**: AI Agent wajib memanggil tool inspeksi sebelum melakukan modifikasi file atau ekspor 3D.
2. **No Auto-Merge**: Seluruh kode, mesh, dan blueprint dari AI Agent harus melalui review dan verifikasi fisik di editor.
3. **Wajib Bukti Fisik Konkret**: Setiap laporan selesai wajib menyertakan path file aktual, data parameter numerik, atau screenshot visual.

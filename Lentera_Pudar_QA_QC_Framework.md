# Kerangka QA/QC — Lentera Pudar
### Standar Kontrol Kualitas & Jaminan Kualitas untuk Menjaga Produksi Tetap Terarah

Dokumen ini melengkapi GDD, Moodboard, Referensi Teori, dan Daftar Tools sebagai **lapisan kontrol** — memastikan semua yang sudah dirancang benar-benar terimplementasi dengan konsisten, terutama karena sebagian besar eksekusi dilakukan lewat AI agent via MCP yang butuh checkpoint verifikasi manusia secara berkala.

---

## 1. Perbedaan QA vs QC (Dasar Kerangka Berpikir)

- **QC (Quality Control)** = memeriksa **hasil akhir** — apakah aset/fitur yang sudah jadi memenuhi standar (bug, visual, performa).
- **QA (Quality Assurance)** = memastikan **proses** yang menghasilkan aset itu benar sejak awal (naming convention diikuti, pipeline diikuti, dokumentasi diikuti) — supaya QC di akhir tidak perlu menemukan banyak masalah karena sudah dicegah dari awal.

Dokumen ini mencakup keduanya: QA di setiap tahap pengerjaan, QC di setiap gerbang milestone.

---

## 2. Prinsip Utama: Definition of Done (DoD) per Jenis Aset

Tidak ada aset dianggap "selesai" hanya karena sudah dibuat — harus lolos checklist berikut. AI agent harus diberi checklist ini sebagai kriteria eksplisit sebelum melaporkan task selesai.

### A. DoD — Model 3D (Blender → UE5)
- [ ] Nama file & aset mengikuti konvensi (`SK_`, `SM_`, `T_`, dst — sesuai bagian 17.C dokumen Teori)
- [ ] Topology bersih (tidak ada n-gon bermasalah, tidak ada non-manifold geometry pada mesh yang butuh collision)
- [ ] UV unwrap tanpa overlap yang tidak disengaja, seam masuk akal untuk baking texture
- [ ] Skala & orientasi benar saat diimpor ke UE5 (1 unit = 1 cm sesuai standar UE5)
- [ ] LOD tersedia minimal untuk aset yang akan muncul berulang kali di level (prop, musuh umum)
- [ ] Collision mesh sudah diset (custom collision untuk objek kompleks, bukan default auto-convex kalau bentuknya rumit)
- [ ] Poly count sesuai budget kategori aset (hero character vs prop biasa vs background)

### B. DoD — Material/Shader
- [ ] Memakai struktur PBR standar (Base Color, Roughness, Metallic, Normal) — sesuai teori bagian 11.A
- [ ] Untuk material es: parameter SSS sudah diatur dan diuji visual dari minimal 2 sudut pencahayaan berbeda
- [ ] Untuk material emissive (syal Aina, kristal kutukan): terhubung ke Material Parameter Collection, bukan warna statis — sesuai teori bagian 11.C
- [ ] Kontras warna hangat (2700K) vs dingin (6500K) diverifikasi visual, bukan cuma angka Kelvin di properti cahaya
- [ ] Diuji lolos simulasi colorblind (lihat bagian 6.C di dokumen ini)

### C. DoD — Rigging & Animasi
- [ ] Skeleton hierarchy sesuai standar UE5 humanoid (kompatibel Control Rig/retargeting)
- [ ] Spring bone/cloth constraint syal & jubah diuji minimal 3 skenario gerakan berbeda (diam, lari, dash) tanpa clipping parah ke tubuh
- [ ] Animasi combat diverifikasi punya frame anticipation & follow-through (sesuai 12 prinsip animasi, bagian 9.A dokumen Teori) — bukan cuma gerakan mentah hasil mocap/generate tanpa polish
- [ ] Blend tree locomotion diuji tanpa "foot sliding" (kaki menggeser tidak natural saat transisi jalan-lari)
- [ ] IK kaki berfungsi di permukaan tidak rata minimal 2 jenis medan uji

### D. DoD — Audio
- [ ] Loudness sesuai target standar (~-16 LUFS) — sesuai teori bagian 18.C
- [ ] Ducking musik saat bisikan/dialog penting berfungsi, diuji minimal 1 skenario combat + 1 skenario eksplorasi tenang
- [ ] Binaural positioning diuji pakai headphone sungguhan (bukan cuma preview software) minimal sekali per set bisikan baru
- [ ] Tidak ada clipping/distorsi pada volume puncak

### E. DoD — Level/Sektor Dungeon
- [ ] Critical path & optional path sudah dibedakan jelas secara geometri (sesuai teori bagian 2.B)
- [ ] Minimal satu landmark dominan terlihat dari titik-titik utama sektor (sesuai teori bagian 2.C)
- [ ] World Partition streaming diuji tidak ada "pop-in" kasar saat pemain bergerak cepat
- [ ] Breather room tersedia sesuai ritme yang direncanakan (tidak combat-terus-menerus tanpa jeda — sesuai teori bagian 2.D & 15.G)
- [ ] Frame rate diuji stabil di area terpadat sektor (lihat budget performa bagian 5 dokumen ini)

### F. DoD — Sistem Gameplay/Blueprint (Combat, Curse Meter, dsb)
- [ ] FSM/Behavior Tree diuji untuk seluruh transisi state, termasuk edge case (misal: apa terjadi kalau pemain dash tepat saat Curse Meter penuh)
- [ ] Parry window diuji dengan angka frame eksplisit dan dicatat, bukan "terasa pas" tanpa dokumentasi
- [ ] Tidak ada soft-lock (state yang membuat pemain tidak bisa melanjutkan tanpa restart)
- [ ] Save/checkpoint diuji tidak corrupt setelah kombinasi save-load berulang minimal 10x

---

## 3. Gerbang Milestone (Stage-Gate Process)

Proyek tidak boleh maju ke tahap berikutnya tanpa lolos gerbang ini. Ini mencegah "membangun di atas fondasi yang belum stabil".

```
[GATE 0: Pra-Produksi]
  → GDD, Moodboard, Teori, Tools List sudah final (SUDAH TERPENUHI)
  → Canon Bible/world-building consistency dokumen dibuat (lihat teori 18.B)
        ↓
[GATE 1: Fondasi Teknis]
  → MCP Blender & UE5 terhubung dan diuji dengan task sederhana (spawn 1 mesh, atur 1 material)
  → Asset naming convention & folder structure disepakati dan didokumentasikan
  → Version control (Perforce/Git LFS) sudah aktif sebelum aset pertama dibuat
        ↓
[GATE 2: Grey-Box / Prototype]
  → 1 sektor dungeon dibangun kasar (grey-box, tanpa detail visual) untuk uji pacing & flow
  → Combat core loop (Light/Heavy/Evade/Curse Meter) berfungsi dengan placeholder art
  → Playtest internal minimal 3 kali sebelum lanjut ke detail visual — mencegah kerja detail di atas desain yang belum teruji
        ↓
[GATE 3: Vertical Slice]
  → 1 sektor penuh (art final, audio, 1 boss) selesai end-to-end sebagai representasi kualitas keseluruhan game
  → Semua DoD di bagian 2 dokumen ini lolos untuk sektor tersebut
  → Review menyeluruh: apakah vertical slice ini benar-benar merepresentasikan visi GDD (Kena artstyle + Hellblade mechanic feel)?
        ↓
[GATE 4: Produksi Penuh]
  → Replikasi pipeline vertical slice ke 4 sektor sisanya
  → QC checklist (bagian 4 dokumen ini) dijalankan per sektor selesai
        ↓
[GATE 5: Alpha]
  → Semua sektor bisa dimainkan ujung ke ujung tanpa bug blocking
  → Placeholder apa pun (jika ada) sudah didaftar dan dijadwalkan penyelesaiannya
        ↓
[GATE 6: Beta]
  → Fitur lengkap, fokus penuh ke bug fixing, balancing, optimasi performa
  → Playtest eksternal (di luar tim inti) dimulai di sini, bukan sebelumnya
        ↓
[GATE 7: Release Candidate → Rilis]
  → Final QC pass penuh (bagian 4), build packaging teruji di hardware target
```

---

## 4. Checklist QC Final (Sebelum Rilis/Sebelum Dianggap "Selesai" per Milestone)

### A. Visual & Artstyle Consistency (vs Kena)
- [ ] Semua sektor melalui review perbandingan langsung dengan referensi Kena — palet warna, siluet karakter, gaya lighting konsisten
- [ ] Tidak ada aset yang "keluar gaya" (misal terlalu realistis dibanding aset lain, atau terlalu kartun)

### B. Feel & Mekanik Consistency (vs Hellblade)
- [ ] Bobot combat (hitstop, kamera dekat, audio) diuji terasa konsisten berat di seluruh sektor, tidak ada sektor yang tiba-tiba terasa "ringan/generic"
- [ ] Cek ludonarrative dissonance (teori 16.A): apakah ada bagian combat yang terasa terlalu "seru-ringan" padahal konteks cerita berat?

### C. Performa
- [ ] Frame rate target tercapai di hardware minimum spec yang ditentukan tim, diuji di tiap sektor bukan cuma vertical slice
- [ ] Memory budget streaming (World Partition) tidak melebihi batas di area terpadat

### D. Aksesibilitas
- [ ] Colorblind mode diuji dengan simulator, kontras hangat/dingin tetap terbaca
- [ ] Opsi kurangi screen shake/motion tersedia dan berfungsi
- [ ] Subtitle terbaca jelas di semua kondisi pencahayaan dungeon (termasuk area paling gelap)

### E. Naratif & Lore
- [ ] Tidak ada kontradiksi dengan Canon Bible (teori 18.B)
- [ ] Semua momen kunci (Altar Duka x4, boss x5) diverifikasi memberi bobot emosional yang dimaksud (lewat playtest, bukan asumsi)

### F. Localization (jika sudah masuk tahap ini)
- [ ] Text expansion buffer diuji tidak terpotong pada bahasa dengan teks lebih panjang
- [ ] Tidak ada teks hardcoded yang lolos dari sistem localization dashboard

### G. Stabilitas Teknis
- [ ] Zero bug kategori **Blocking** (lihat klasifikasi severity bagian 5)
- [ ] Save/load diuji ulang sebagai bagian dari final pass, bukan hanya di Gate 2

---

## 5. Klasifikasi Severity Bug (Standar Penamaan agar Tidak Ambigu)

| Severity | Definisi | Contoh | Aturan |
|---|---|---|---|
| **Blocking** | Membuat progres tidak bisa lanjut sama sekali | Softlock di Altar Duka, crash saat load sektor | Wajib fix sebelum lanjut ke gate berikutnya, tanpa pengecualian |
| **Critical** | Merusak pengalaman inti tapi ada workaround | Curse Meter tidak reset dengan benar, clipping parah pada cutscene kunci | Wajib fix sebelum Beta |
| **Major** | Mengganggu tapi tidak merusak fungsi inti | Animasi transisi kaku, audio ducking telat | Wajib fix sebelum Release Candidate |
| **Minor** | Kosmetik, tidak mengganggu gameplay | Tekstur low-res di sudut jarang terlihat | Boleh masuk backlog, fix kalau waktu memungkinkan |

Setiap bug wajib dicatat dengan: severity, sektor/lokasi, langkah reproduksi, dan siapa/apa yang menemukan (playtest manual, automated test, atau review AI agent).

---

## 6. Protokol Khusus: Review Output AI Agent (MCP)

Karena sebagian besar eksekusi teknis dilakukan lewat AI agent, perlu lapisan verifikasi khusus supaya kesalahan tidak menumpuk tanpa terdeteksi.

### A. Aturan "Tidak Ada Auto-Merge"
Setiap aset/perubahan yang dihasilkan AI agent lewat MCP **wajib direview manusia** sebelum masuk ke branch utama/level final — baik lewat visual check langsung di editor maupun checklist DoD di bagian 2. AI agent boleh bekerja cepat dan iteratif, tapi gerbang commit ke versi final tetap dipegang manusia.

### B. Sesi Kerja Terdokumentasi
Tiap sesi kerja dengan AI agent sebaiknya dicatat ringkas: task yang diminta, hasil yang didapat, dan apakah lolos DoD. Ini mencegah pengulangan instruksi yang salah di sesi berikutnya dan membantu melacak kapan sebuah keputusan desain berubah (terkait Living Document, teori 18.G).

### C. Konsistensi Referensi Antar Sesi
Karena AI agent tidak otomatis "ingat" seluruh histori kerja di setiap sesi baru, pastikan GDD, Moodboard, dan dokumen Teori selalu disertakan sebagai context di awal sesi kerja penting — terutama sebelum task yang berkaitan langsung dengan konsistensi gaya (art, naming, tone).

### D. Sanity Check Otomatis (kalau memungkinkan diimplementasikan di MCP)
Kalau arsitektur MCP kustom kamu memungkinkan, tambahkan validasi otomatis dasar sebelum AI agent melapor task selesai — contoh: cek otomatis apakah nama aset yang baru dibuat cocok pola regex konvensi penamaan, cek apakah poly count tidak melebihi ambang batas kategori.

---

## 7. Ritme QA/QC Rutin (Supaya Tidak Menumpuk di Akhir)

- **Harian/Per sesi kerja**: DoD check untuk tiap aset individual sebelum ditandai selesai.
- **Mingguan**: Review konsistensi gaya (art + mekanik) lintas aset yang baru selesai minggu itu — cegah "style drift" pelan-pelan yang baru ketahuan besar setelah berbulan-bulan.
- **Per Gate**: Checklist penuh sesuai bagian 3 & 4 dokumen ini, bukan sekadar "kelihatannya sudah bagus".
- **Sebelum tiap playtest**: Pastikan build stabil (minimal tidak ada bug Blocking) sebelum membuang waktu tester untuk hal yang sudah diketahui rusak.

---

## 8. Peran & Tanggung Jawab (Meski Tim Kecil/Solo)

Bahkan untuk tim kecil atau solo dev dibantu AI agent, baik memisahkan **peran fungsi** secara sadar (meski dipegang orang yang sama) supaya tidak ada langkah QA yang terlewat karena "capek/buru-buru":

- **Peran Pembuat (Maker)**: Memberi instruksi ke AI agent, membangun aset.
- **Peran Pemeriksa (Reviewer)**: Menjalankan DoD checklist, secara sadar mengambil "topi" berbeda dari peran Maker — idealnya dengan jeda waktu (review besoknya, bukan langsung setelah membuat) supaya lebih objektif.
- **Peran Pemain (Playtester)**: Mencoba build seolah pemain baru, bukan sambil tahu semua detail internal sistem — untuk menangkap masalah yang "terlalu dekat" untuk dilihat Maker/Reviewer.

---

*Dokumen ini melengkapi GDD, Moodboard, Referensi Teori, dan Daftar Tools sebagai lapisan kontrol kualitas dalam satu paket dokumentasi pra-produksi Lentera Pudar.*

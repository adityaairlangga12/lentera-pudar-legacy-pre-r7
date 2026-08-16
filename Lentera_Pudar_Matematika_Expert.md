# Matematika Tingkat Expert — Lentera Pudar
### Versi Mendalam untuk Kamera, Rotasi, Kurva, dan Prosedural (Pelengkap Referensi Teori Bagian 14)

Dokumen ini menggali lebih dalam matematika di balik tiap sistem yang dipakai proyek — level detail yang dibutuhkan kalau AI agent harus menyetel parameter kurva, rotasi, atau noise function secara presisi, bukan hanya memilih preset default engine.

---

## 1. Vektor, Matriks, dan Ruang Koordinat

### A. Operasi Vektor Dasar yang Wajib Dipahami Agent
- **Dot product** (`a · b = |a||b|cos θ`): dipakai untuk mengukur "seberapa searah" dua arah — misalnya cek apakah Kaelen menghadap musuh (dipakai di target-lock combat) atau apakah permukaan lantai cukup landai untuk dipijak (perbandingan terhadap vektor up).
- **Cross product** (`a × b`): menghasilkan vektor tegak lurus terhadap dua vektor input — dipakai untuk menghitung normal permukaan (arah cahaya memantul di dinding es), dan untuk menentukan arah rotasi terpendek antar dua orientasi.
- **Normalisasi vektor**: vektor arah harus selalu punya panjang 1 sebelum dipakai untuk perhitungan rotasi/pencahayaan — lupa normalisasi adalah sumber bug paling umum di shader dan animasi custom (hasil "terlalu terang" atau rotasi yang salah skala).

### B. Ruang Koordinat & Transformasi Matriks
Setiap objek di scene punya tiga ruang koordinat yang harus dikonversi bolak-balik lewat matriks transformasi:
1. **Local space** (posisi relatif terhadap pivot objek sendiri) — dipakai saat sculpting/rigging.
2. **World space** (posisi absolut di level) — dipakai untuk fisika dan collision.
3. **Camera/view space** (posisi relatif terhadap kamera) — dipakai untuk rendering dan efek layar-penuh (post-process dingin di area Denial).

**Instruksi untuk AI agent**: kalau parenting/rig terasa "salah tempat" setelah dipindah, penyebab hampir selalu adalah local space vs world space yang tertukar — bukan bug rig itu sendiri.

---

## 2. Quaternion & Rotasi 3D (Detail Lanjutan dari Bagian 14.A)

### A. Kenapa Bukan Euler Angle
Euler angle (pitch/yaw/roll) intuitif untuk manusia tapi rawan **gimbal lock** — saat dua sumbu rotasi berimpit sehingga satu derajat kebebasan hilang. Ini nyata problematik untuk kamera dekat ala Hellblade II yang sering rotasi ekstrem mengelilingi wajah Kaelen.

### B. Struktur Matematis Quaternion
Quaternion `q = w + xi + yj + zk` merepresentasikan rotasi lewat 4 komponen (bukan 3 sudut) — secara konsep, `w` menyimpan "seberapa besar rotasi" dan `(x,y,z)` menyimpan sumbu rotasinya. Agent tidak perlu menghitung manual, tapi harus paham dua operasi kunci:
- **SLERP (Spherical Linear Interpolation)**: interpolasi rotasi yang konstan kecepatan sudutnya — dipakai untuk transisi kamera sinematik supaya terasa mulus, bukan cepat-lambat-cepat.
- **NLERP (Normalized Linear Interpolation)**: lebih murah secara komputasi tapi kecepatan sudut tidak konstan — cukup untuk blend animasi kecil (idle ke walk) yang jaraknya pendek, boros kalau dipakai untuk rotasi kamera besar.

**Instruksi untuk AI agent**: pakai SLERP untuk transisi kamera/rotasi besar, NLERP untuk blend animasi kecil dan frequent. Salah pilih menyebabkan rotasi terasa "meleset" kecepatannya di tengah gerakan.

---

## 3. Interpolasi & Easing Curves (Detail Lanjutan dari Bagian 14.B)

### A. Kenapa Linear Terasa Robotic
Gerakan natural di dunia nyata selalu berakselerasi dan berdeselerasi (tidak pernah instan mulai/berhenti). Interpolasi linear (`lerp`) mengabaikan ini — hasilnya gerakan terasa mekanis.

### B. Keluarga Easing yang Relevan untuk Proyek
| Jenis Easing | Karakter Gerakan | Contoh Pemakaian di Lentera Pudar |
|---|---|---|
| Ease-In | Mulai lambat, percepat | Syal Aina mulai meredup — dramatis, bukan tiba-tiba |
| Ease-Out | Mulai cepat, perlambat | Kamera berhenti di posisi framing naratif |
| Ease-In-Out | Lambat-cepat-lambat | Transisi masuk mode close-up narasi |
| Cubic Bezier custom | Kurva kontrol penuh | Kurva khusus tiap tahap grief (lihat 3.C) |

### C. Bezier Curve sebagai Bahasa Emosi
Cubic Bezier (`P(t)` dikontrol 4 titik: 2 anchor, 2 handle) memungkinkan kurva easing yang unik per konteks emosional — bukan cuma satu easing generik untuk semua transisi. Agent bisa memakai kurva "overshoot lalu settle" (sedikit melewati target sebelum kembali) untuk transisi Anger yang terasa impulsif, vs kurva "flat lalu jatuh curam" untuk transisi Depression yang terasa berat dan tertunda.

**Instruksi untuk AI agent**: saat diminta menyetel transisi UI/kamera per tahap grief, jangan pakai satu preset easing untuk semua — pilih bentuk kurva yang secara matematis mencerminkan psikologi tahap tersebut (lihat cross-reference ke dokumen Psikologi Expert bagian 4).

---

## 4. Spline & Kurva untuk Jalur Kamera dan Level (Detail Lanjutan dari Bagian 14.C)

### A. Jenis Spline yang Relevan
- **Catmull-Rom Spline**: melewati tepat semua titik kontrol (interpolating spline) — cocok untuk jalur kamera sinematik yang harus lewat titik-titik framing spesifik yang sudah ditentukan storyboard.
- **Bezier Spline (composite)**: titik kontrol tidak dilewati langsung tapi menentukan bentuk kurva (approximating) — lebih fleksibel untuk bentuk organik lorong *Hall of Mirrors*, karena tangent tiap segmen bisa diatur independen untuk transisi mulus antar segmen.

### B. Parameterisasi Kurva (Arc-Length vs Uniform)
Masalah umum: parameter `t` di spline (0 ke 1) *tidak* linear terhadap jarak tempuh sepanjang kurva — artinya objek yang bergerak dengan `t` seragam akan terasa lebih cepat di segmen kurva yang landai dan lebih lambat di segmen tajam. Solusinya adalah **arc-length reparameterization** — menghitung ulang `t` berdasarkan jarak tempuh aktual, bukan urutan titik kontrol.

**Instruksi untuk AI agent**: kalau kamera sinematik terasa "berubah kecepatan aneh" di tengah lintasan tanpa alasan naratif, cek dulu apakah spline sudah di-arc-length-reparameterize sebelum menyalahkan keyframe animasi.

### C. Curvature Continuity untuk Lorong Organik
Level lorong yang terasa "alami" (bukan seperti disambung dari segmen lurus) butuh continuity minimal **C2** (turunan kedua kurva kontinu) di titik sambungan segmen — bukan cuma C0 (posisi nyambung) atau C1 (arah nyambung). Tanpa C2, mata pemain tetap bisa menangkap "patahan" halus di kurva lorong meski secara visual tampak menyambung.

---

## 5. Signed Distance Fields — Detail Matematis (Lanjutan dari Bagian 14.D)

### A. Definisi Formal
SDF `f(p)` mengembalikan jarak bertanda dari titik `p` ke permukaan terdekat: negatif jika di dalam objek, positif jika di luar, nol tepat di permukaan. Sifat kunci: `|f(p1) - f(p2)| ≤ |p1 - p2|` (1-Lipschitz) — inilah yang membuat *sphere tracing* (ray marching berbasis SDF) efisien, karena tiap langkah ray bisa "melompat" sejauh nilai SDF tanpa menembus permukaan.

### B. Kenapa Relevan di Luar Rendering
Selain Lumen/Nanite, SDF berguna konsep untuk agent dalam dua konteks produksi:
- **Collision proxy sederhana**: SDF primitif (bola, kotak, kapsul) jauh lebih murah dihitung daripada mesh collision detail — dipakai untuk collision kasar pecahan es sebelum fracture detail aktif.
- **Soft shadow & volumetric fog**: jarak SDF ke occluder dipakai untuk menghitung penumbra shadow secara analitik, bukan lewat shadow map beresolusi tinggi yang mahal.

**Instruksi untuk AI agent**: agent tidak perlu menghitung SDF manual (engine sudah menangani), tapi harus paham konsep ini saat troubleshooting artefak rendering (misal shadow "bocor" di sudut tajam — biasa terjadi karena SDF primitif tidak cukup presisi merepresentasikan geometri kompleks).

---

## 6. Noise Function — Detail Matematis (Lanjutan dari Bagian 14.E)

### A. Perlin vs Simplex vs Worley
| Jenis Noise | Karakter Visual | Kegunaan di Proyek |
|---|---|---|
| Perlin Noise | Halus, bergelombang organik | Variasi tekstur permukaan es tidak seragam |
| Simplex Noise | Mirip Perlin, lebih efisien di dimensi tinggi, minim artefak arah | Pergerakan partikel kunang-kunang cahaya syal (3D + waktu) |
| Worley (Cellular) Noise | Pola sel/retakan | Pola dasar untuk Voronoi fracture es (lihat dokumen Fisika Expert bagian 1.C) |

### B. Fractal Noise (Octaves/Layering)
Noise tunggal terasa terlalu seragam skalanya. Teknik **Fractal Brownian Motion (fBm)** menumpuk beberapa layer noise dengan frekuensi meningkat dan amplitudo menurun (biasanya rasio 2:1 per oktaf) — menghasilkan detail multi-skala yang terasa alami, dipakai untuk variasi permukaan es dari skala besar (retakan utama) sampai kecil (tekstur permukaan halus).

**Instruksi untuk AI agent**: kalau variasi prosedural terasa "terlalu seragam" atau "terlalu kacau", masalahnya biasanya jumlah oktaf (kurang oktaf = seragam, terlalu banyak oktaf = noise/kacau) atau parameter *persistence* (kontrol seberapa besar kontribusi oktaf detail) — bukan noise function-nya yang salah.

---

## 7. Finite State Machine — Formalisasi (Lanjutan dari Bagian 14.F)

### A. Definisi Formal Automata
FSM secara formal adalah 5-tuple `(S, Σ, δ, s0, F)`: himpunan state (`S`), himpunan input/trigger (`Σ`), fungsi transisi (`δ: S × Σ → S`), state awal (`s0`), dan state akhir/final (`F`). Untuk combat Kaelen, `S = {Idle, Attack, Recovery}`, `Σ` = input pemain + kondisi timer, `δ` menentukan transisi mana yang valid dari tiap state.

### B. Kelemahan FSM Murni dan Solusi Bertingkat
FSM murni sulit skalanya untuk AI musuh kompleks — jumlah transisi meledak secara kombinatorial (`state × state` kemungkinan transisi). Solusi bertingkat yang relevan:
- **Hierarchical State Machine (HSM)**: state induk (misal "Combat") berisi sub-state (Attack, Dodge, Block) — transisi antar sub-state tidak perlu didefinisikan ulang di setiap level.
- **Behavior Tree**: struktur pohon dengan node Sequence/Selector/Decorator — lebih modular dan reusable dibanding FSM datar untuk AI musuh dengan banyak kondisi (relevan untuk UE5 Behavior Tree yang sudah disebut di dokumen Tools/MCP Stack).

**Instruksi untuk AI agent**: gunakan FSM datar hanya untuk sistem sederhana dan terbatas (state machine combat Kaelen sendiri, 3-5 state). Begitu jumlah state/kondisi AI musuh bertambah kompleks, migrasikan ke Behavior Tree — jangan paksa FSM datar berkembang jadi puluhan state karena akan sulit di-debug dan rawan bug transisi tak terduga.

---

## 8. Ringkasan Peta Matematika ke Sistem Produksi

| Cabang Matematika | Sistem yang Menggunakan | Dampak kalau Salah Setting |
|---|---|---|
| Quaternion/SLERP | Rotasi kamera & karakter | Gimbal lock, rotasi "meleset" kecepatan |
| Bezier/Easing | Transisi UI, kamera, animasi | Gerakan terasa robotic atau tidak sesuai emosi |
| Spline (Catmull-Rom/Bezier) | Jalur kamera sinematik, bentuk lorong | Kecepatan kamera aneh, lorong terasa "disambung" |
| SDF | Rendering (Lumen/Nanite), collision kasar | Artefak shadow, collision tidak presisi |
| Noise (Perlin/Simplex/Worley) | Variasi prosedural, partikel, fracture | Tekstur terlalu seragam/kacau |
| FSM/HSM/Behavior Tree | Combat state, AI musuh | Bug transisi state, AI sulit di-debug |

**Instruksi umum untuk AI agent**: setiap kali sebuah sistem "terasa salah" secara visual atau perilaku, cek dulu apakah akar masalahnya matematis (parameter kurva/noise/state salah) sebelum mengasumsikan itu masalah artistik atau bug engine. Sebagian besar masalah "feel" yang buruk sebenarnya adalah masalah parameter matematis yang belum disetel dengan tepat.

---

*Dokumen ini adalah versi mendalam dari Referensi Teori bagian 14 (Matematika Tingkat Lanjut), sebagai bagian dari paket dokumentasi pra-produksi Lentera Pudar.*

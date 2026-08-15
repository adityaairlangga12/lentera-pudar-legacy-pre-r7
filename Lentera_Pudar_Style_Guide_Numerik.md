# Style Guide Numerik — Lentera Pudar
### Parameter Konkret untuk Eksekusi Presisi oleh AI Agent (Blender + UE5)

Dokumen ini adalah turunan **angka pasti** dari prinsip-prinsip di dokumen Teori dan Moodboard. Tujuannya: AI agent tidak perlu menebak parameter tiap sesi kerja — semua sudah ditentukan di sini. Kalau ada kebutuhan di luar range ini, catat sebagai pengecualian dan alasannya, jangan diam-diam menyimpang.

---

## 1. Palet Warna Resmi (Hex + Kelvin)

### A. Warna Inti (Sudah Ditetapkan di GDD — Jangan Diubah)
| Elemen | Hex | Kelvin (jika sumber cahaya) | Catatan |
|---|---|---|---|
| Kristal Es Kutukan (dasar) | `#4A6FA5` | 6500K | Warna dasar es non-emissive |
| Kristal Es Kutukan (highlight/emissive) | `#7EE8FA` | 6500K | Dipakai untuk rim light/emissive accent, intensitas naik sesuai Curse Meter |
| Jubah Kaelen | `#2A211C` | — | Base color kain, non-emissive |
| Eyepatch Kaelen | `#141013` | — | Kulit hitam, roughness tinggi (lihat bagian 2) |
| Syal Aina (base) | `#F4B860` | 2700K | Warna inti cahaya hangat |

### B. Warna Turunan (Baru — Perlu Ditetapkan agar Konsisten)
| Elemen | Hex | Kelvin | Catatan |
|---|---|---|---|
| Kulit Kaelen (base skin tone) | `#D8B79A` | — | Sesuaikan undertone hangat, jangan terlalu pink/pucat (hindari uncanny valley — teori 15.F) |
| Rambut perak Kaelen | `#C9CDD1` | — | Sedikit kebiruan agar netral, bukan putih murni |
| Reruntuhan batu (base) | `#5C5A55` | — | Netral abu-hangat, jadi kanvas kontras untuk cahaya |
| Reruntuhan batu (area basah/es menempel) | `#4A5A63` | — | Sedikit condong ke biru dingin di area terdampak kutukan |
| Bisikan/partikel jiwa beku | `#8FA9C4` | 7000K | Sedikit lebih dingin dari kristal es utama, untuk bedakan sumber |
| UI/Subtitle text color | `#F2E9DC` | — | Hangat netral, kontras tinggi terhadap background gelap dungeon |
| UI/Subtitle background box | `#0D0D0F` @ 65% opacity | — | Cukup gelap untuk keterbacaan tanpa menutupi visual sepenuhnya |

### C. Aturan Kontras (Wajib Diuji, Bukan Diasumsikan)
- Rasio kontras minimum antara elemen hangat (Aina) dan area sekitarnya: **minimal 4.5:1** (standar keterbacaan WCAG AA, dipakai sebagai acuan meski ini bukan aplikasi web — prinsipnya tetap relevan untuk visibilitas)
- Saturasi warna dunia (global post-process) menurun bertahap: **100% saturasi di Sektor 1 → turun ~10-15% per sektor → sekitar 40-50% saturasi di Sektor 4 (Abyss of Stillness)** sebelum naik lagi sedikit di Sektor 5 (Acceptance) sebagai simbol harapan kembali

---

## 2. Parameter Material (PBR)

| Material | Base Color | Roughness | Metallic | Catatan Khusus |
|---|---|---|---|---|
| Kristal Es (Kaelen/kutukan) | `#4A6FA5` | 0.15–0.30 | 0.0 | Subsurface Scattering: radius 0.5–1.2cm, warna scatter `#7EE8FA` |
| Es dekoratif dungeon (non-interaktif) | `#4A6FA5` | 0.25–0.40 | 0.0 | Roughness sedikit lebih tinggi dari kristal Kaelen agar tidak menyaingi fokus visual pemain |
| Kain Jubah Kaelen | `#2A211C` | 0.55–0.70 | 0.0 | Roughness tinggi, tekstur kain kasar-tebal |
| Kain Syal Aina | `#F4B860` | 0.35–0.50 | 0.0 | Sedikit lebih halus dari jubah agar terasa "istimewa"/berbeda material |
| Kulit Eyepatch | `#141013` | 0.60–0.75 | 0.0 | Kulit tersamak, tidak mengkilap |
| Batu Reruntuhan | `#5C5A55` | 0.70–0.85 | 0.0 | Roughness tinggi khas batu tua |
| Logam Zirah Boss (Lord Alden dkk) | Variatif per boss | 0.25–0.45 | 0.7–0.9 | Metallic tinggi untuk baja/zirah, roughness variatif untuk kesan usang |

### Parameter Emissive (Terhubung Curse Meter via Material Parameter Collection)
| State Curse Meter | Intensitas Emissive Kristal Es | Warna Emissive |
|---|---|---|
| 0–25% (Aman) | 0.5–1.0 | `#7EE8FA` redup |
| 26–60% (Waspada) | 1.5–3.0 | `#7EE8FA` sedang |
| 61–90% (Bahaya) | 4.0–6.0 | `#7EE8FA` terang, mulai berdenyut (pulse frequency 0.8–1.2Hz) |
| 91–100% (Surge/Kritis) | 8.0–12.0 | `#7EE8FA` + campuran putih 10-15%, pulse frequency naik ke 2–3Hz |

---

## 3. Parameter Cloth Simulation (Syal Aina & Jubah Kaelen)

| Parameter | Syal Aina | Jubah Kaelen |
|---|---|---|
| Stiffness (kekakuan) | 0.4–0.6 (lebih lentur, ringan) | 0.6–0.8 (lebih berat, tebal) |
| Damping | 0.3–0.5 | 0.5–0.7 |
| Iteration count (solver) | 8–12 | 6–10 |
| Wind response multiplier | 1.2x (lebih responsif terhadap angin, karena "hidup") | 0.8x (lebih pasif, hanya ikut gravitasi & gerakan tubuh) |
| Pinning point | Melingkar penuh di leher (fixed) | Bahu (2 titik utama) |

**Catatan uji wajib**: simulasikan pada kecepatan gerak 0 (diam), ~150cm/s (jalan), ~400cm/s (lari), dan saat dash — pastikan tidak ada clipping parah ke tubuh di keempat kondisi ini sebelum dianggap selesai (sesuai DoD dokumen QA/QC bagian 2.C).

---

## 4. Parameter Pencahayaan

| Sumber Cahaya | Kelvin | Intensitas (Lumen, relatif) | Radius/Attenuation |
|---|---|---|---|
| Syal Aina (Point Light utama, menempel karakter) | 2700K | 800–1200 lm (baseline) | 3–5m radius, menyusut 50% di Sektor 4 (jadi 1.5–2.5m) |
| Kristal Es Kaelen (rim light saat Curse Meter tinggi) | 6500K | 200–600 lm, naik sesuai Curse Meter | 1–2m radius |
| Ambient dungeon (fill light umum) | 6000–6500K | Sangat rendah, 50–150 lm | Menyebar luas, hampir tidak terlihat sumbernya |
| Cahaya boss/altar (accent per sektor) | Variatif sesuai tema sektor | 400–1000 lm | Disesuaikan skala ruangan boss |

### Rasio Kontras Cahaya (Chiaroscuro — Teori bagian 6.B)
- Rasio key light (syal Aina) terhadap ambient dungeon: **minimal 8:1** di sektor awal, naik jadi **12:1 atau lebih** di Sektor 4 untuk memperkuat kesan terisolasi.

---

## 5. Budget Poligon (Poly Count)

| Kategori Aset | Target Triangle Count (LOD0) | LOD Levels Minimum |
|---|---|---|
| Karakter Hero (Kaelen) | 40,000–60,000 tris | LOD0–LOD3 (4 level) |
| Karakter Hero (Aina, jika direpresentasikan visual terpisah dari syal) | 20,000–35,000 tris | LOD0–LOD2 |
| Boss (unik per sektor) | 50,000–80,000 tris | LOD0–LOD3 |
| Musuh umum (jiwa beku biasa) | 8,000–15,000 tris | LOD0–LOD2 |
| Prop besar (reruntuhan, altar) | 15,000–30,000 tris (bisa pakai Nanite, budget lebih longgar) | Nanite-enabled, LOD manual opsional |
| Prop kecil (dekorasi, puing) | 500–3,000 tris | LOD0–LOD1 |

---

## 6. Parameter Kamera

| Konteks | Field of View (FOV) | Catatan |
|---|---|---|
| Third-person default (eksplorasi/combat) | 75–85° | Sedikit lebih lebar untuk combat agar pemain lihat sekeliling |
| Close-up naratif (ala Hellblade II, Altar Duka) | 35–50° | FOV sempit untuk fokus wajah, sesuai teori bagian 5.B |
| Boss intro cinematic | 40–60° | Tergantung skala boss, sesuaikan agar boss terasa dominan (Rule of Space — teori 5.C) |

### Transisi Kamera
- Easing curve default: **ease-in-out cubic**, durasi transisi standar 0.4–0.8 detik untuk perpindahan mode kamera (third-person → close-up)
- Collision avoidance kamera: jarak minimum kamera-ke-dinding **15–25cm** sebelum kamera otomatis mendekat ke karakter

---

## 7. Parameter Combat (Timing Frame, @ 30fps sebagai basis hitung)

| Aksi | Startup (Anticipation) | Active | Recovery |
|---|---|---|---|
| Light Attack (per hit combo) | 3–5 frame | 4–6 frame | 6–10 frame |
| Heavy Cursed Strike | 12–18 frame | 6–8 frame | 15–20 frame |
| Evade Dash | 2–4 frame (sangat responsif) | 8–10 frame (i-frame aktif di sini) | 4–6 frame |
| Parry Window | — | **4–6 frame** (ketat, sesuai gaya Hellblade yang berat di timing) | 8–12 frame jika gagal parry |

**Catatan**: angka di atas adalah baseline awal untuk playtest Gate 2 (Grey-Box) — WAJIB direvisi berdasarkan hasil playtest, bukan dianggap final dari dokumen ini saja (lihat QA/QC bagian 3, Gate 2).

---

## 8. Parameter Audio

| Elemen | Target Loudness (LUFS) | Catatan |
|---|---|---|
| Musik latar (layer dasar) | -20 LUFS | Baseline sebelum layering naik saat combat |
| Musik combat (layer penuh) | -16 LUFS | Sesuai target umum media interaktif (teori 18.C) |
| Dialog/Bisikan | -18 LUFS, dengan ducking musik -6dB saat aktif | Ducking attack time 150ms, release time 400ms |
| SFX combat (hit impact) | Peak -3dB (hindari clipping) | — |
| Ambience dungeon | -28 hingga -24 LUFS | Sangat halus, tidak boleh menutupi bisikan/dialog |

---

## 9. Parameter Curse Meter (Sistem Inti)

| Parameter | Nilai Baseline |
|---|---|
| Kapasitas maksimum | 100 poin (skala internal, tidak harus ditampilkan sebagai angka ke pemain) |
| Kenaikan per hit yang diterima Kaelen | 8–15 poin (tergantung jenis serangan musuh) |
| Penurunan alami per detik saat tidak menerima damage | 2–4 poin/detik |
| Ambang batas "Bahaya" (visual warning mulai) | 61 poin |
| Ambang batas Surge tersedia | 90 poin |
| Durasi mode Surge (jika diaktifkan) | 6–10 detik |
| Penalti setelah Surge berakhir | Curse Meter turun ke 20 poin, tapi damage output Kaelen turun 15% selama 5 detik (representasi "kelelahan") |

**Catatan**: ini baseline desain awal — wajib diuji ulang di Gate 2 & disesuaikan dengan hasil playtest sebelum dikunci sebagai final.

---

## 10. Aturan Penggunaan Dokumen Ini

- Dokumen ini **melengkapi**, bukan menggantikan, dokumen Teori — kalau ada pertanyaan "kenapa angka ini dipilih", jawabannya ada di dokumen Teori terkait (nomor bagian dirujuk di atas).
- Semua angka di sini adalah **baseline produksi awal**, bukan hukum mati. Kalau playtest (sesuai Gate 2 QA/QC) menunjukkan perlu revisi, catat perubahan di sini dengan tanggal, supaya jadi living document (sesuai teori 18.G) — jangan biarkan AI agent diam-diam memakai angka lama yang sudah direvisi.
- Kalau AI agent menemukan kebutuhan parameter yang **tidak tercakup** di dokumen ini, instruksikan agent untuk **bertanya/menandai sebagai gap**, bukan menebak sendiri — lalu tambahkan ke dokumen ini setelah diputuskan.

---

*Dokumen ini adalah turunan numerik dari GDD, Moodboard, dan Referensi Teori, sebagai bagian dari paket dokumentasi pra-produksi Lentera Pudar.*

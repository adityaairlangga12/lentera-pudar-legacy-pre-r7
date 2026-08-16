---
name: encounter_pacing
description: Standar kurva kesulitan (difficulty curve), ritme encounter musuh, loop risiko-imbalan (risk-reward), dan pacing stamina/kutukan dalam dungeon Lentera Pudar — 3D Action RPG (Unreal Engine 5 + Blender 5.2 LTS).
---

# Encounter Pacing & Combat Rhythm (Game Designer)

Panduan perancangan intensitas pertempuran, pacing musuh, kurva emosi pemain, dan alokasi *Emotional Bandwidth* di dalam dungeon Lentera Pudar merujuk pada [style-guide.md](file:///d:/GodotProjects/Lentera-Pudar/references/04-art-3d/style-guide.md), [psychology.md](file:///d:/GodotProjects/Lentera-Pudar/references/05-foundations/psychology.md), [sector-ability-progression.md](file:///d:/GodotProjects/Lentera-Pudar/references/02-gameplay/sector-ability-progression.md), dan [theory-reference.md](file:///d:/GodotProjects/Lentera-Pudar/references/01-core/theory-reference.md).

---

## 1. Ritme 4-Fase Encounter & Manajemen Emotional Bandwidth

1. **Intro (Pengenalan)**: Memperkenalkan jenis ancaman baru dalam lingkungan terkontrol dengan 1 musuh tunggal dekat sumber cahaya syal Aina (radius warm point light 2700K).
2. **Escalation (Eskalasi)**: Menggabungkan musuh tersebut dengan variasi pola serangan atau rintangan lantai licin es. Ambient dungeon desaturasi mulai terasa — Curse Meter biasanya mulai meningkat ke rentang 26–60%.
3. **Twist (Tekanan Lingkungan)**: Pertarungan di area gelap dengan sumber cahaya terbatas, memaksa pemain mengandalkan radius syal lentera dan keputusan risk-reward Eyepatch. Potensi Curse Meter masuk zona Bahaya (61–90%).
4. **Relief & Reward (Pelepasan & Hadiah)**: Ruangan aman berpenerangan hangat (Altar Lentera atau Breather Room) berisi potongan memori Aina (Fixed Ratio Reward). Syal Aina kembali berdenyut normal, binaural whispers meredup.

---

## 2. Manajemen Ketegangan (Tension vs Relief) & Flow State

- **Tekanan Kutukan (Curse Pressure)**: Tangan beku protagonis menciptakan urgensi bertarung taktis. Kaelen mendapat +8–15 poin Curse per hit yang diterima, decay alami -2 s.d. -4 poin/detik saat tidak kena hit — jangan biarkan pemain merasa terlalu aman di kegelapan tanpa batas.
- **Lantern Light as Resource/Safety (Lumen Stakes)**: Cahaya syal Aina adalah sumber harapan. Pertempuran di luar radius cahaya memiliki risiko tinggi (Curse naik lebih cepat) tetapi reward resonansi memori yang lebih berharga.
- **Telegraph Serangan Jelas (Competence via Readability)**: Serangan musuh wajib memiliki jeda animasi *wind-up* minimal 12–18 frame dengan kilau biru dingin `#4A6FA5` agar pemain dapat bereaksi (parry window 12 frame / 0.20s).

---

## 3. Parameter Combat Timing (Referensi Style Guide & Progression)

| Aksi | Startup | Active | Recovery | Catatan Eksekusi & Buffer |
|---|---|---|---|---|
| **Light Punch Combo** | 3–5 frame | 4–6 frame | 6–10 frame | Kombo 3-hit tangan kosong berbobot |
| **Combo Finisher (`GA_ShatterStrike`)** | 18 frame | 8 frame | 22 frame | 0 Curse, Guaranteed Guard Break, 16f un-cancellable |
| **Finisher Buffer Window** | — | — | — | 12 frame (0.20s) aktif tepat di frame impact Hit 3 |
| **Heavy Cursed Strike Biasa** | 12–18 frame | 6–8 frame | 15–20 frame | +10 Biaya Kutukan (Input di luar kombo) |
| **Evade Dash** | 2–4 frame | 8–10 frame (i-frames) | 4–6 frame | Meninggalkan jejak percikan api emas syal |
| **Tight Parry Window** | — | 12 frame (0.20s) | 8–12 frame jika gagal | Hit-stop 50ms Delta-Time Accumulator |

---

## 4. Kurva Intensitas & Taruhan Visibilitas per Sektor Dungeon (ADR-039)

| Sektor | Tahap Duka | Panjang Syal | Radius PointLight | Intensitas Encounter & Pacing |
|---|---|---|---|---|
| **Prologue** | Onboarding Awal | $180\text{ cm}$ | **$800\text{ cm}$ ($8.0\text{ m}$)** | Pengenalan mekanik dasar, tutorial fail-safe |
| **Sektor 1 (Denial)** | Penyangkalan | $120\text{ cm}$ | **$600\text{ cm}$ ($6.0\text{ m}$)** | Sedang — musuh single *The Echo*, koridor simetris |
| **Sektor 2 (Anger)** | Kemarahan | $70\text{ cm}$ | **$450\text{ cm}$ ($4.5\text{ m}$)** | Tinggi — hazard pembakaran es, friksi navigasi |
| **Sektor 3 (Bargaining)** | Tawar-Menawar | $30\text{ cm}$ | **$320\text{ cm}$ ($3.2\text{ m}$)** | Kompleks — labirin cermin, proyektil semu |
| **Sektor 4 (Depression)** | Depresi | $10\text{ cm}$ | **$200\text{ cm}$ ($2.0\text{ m}$)** | Tertinggi — 3-Tier Emotional Descent, patung apatis |
| **Sektor 5 (Acceptance)** | Penerimaan | Bersatu Abadi | **Penuh / Global GI** | Katarsis klimaks — fajar overworld |

---

## 5. Aturan Breather Room & Safe Archways
- Setiap 2–3 arena encounter, WAJIB ada satu ruang *Breather Room* (sumber cahaya hangat 2700K, non-combat).
- Breather Room berfungsi sebagai: 1) titik *checkpoint*, 2) reset Curse Meter pasif (-2 poin/s), 3) alokasi jeda kontemplatif untuk memulihkan *Emotional Bandwidth* pemain, 4) interaksi bisikan Aina untuk lore delivery.

---

## 6. Desain Spasial Arena vs FSM Musuh (Lihat [level-design-storytelling.md](file:///d:/GodotProjects/Lentera-Pudar/references/02-gameplay/level-design-storytelling.md))
- Hindari arena berbentuk kotak polos. Gunakan pilar reruntuhan, retakan es destructible, dan elevasi tangga untuk variasi taktis.

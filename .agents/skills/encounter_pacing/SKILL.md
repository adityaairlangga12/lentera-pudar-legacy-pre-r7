---
name: encounter_pacing
description: Standar kurva kesulitan (difficulty curve), ritme encounter musuh, loop risiko-imbalan (risk-reward), dan pacing stamina/kutukan dalam dungeon Lentera Pudar — 3D Action RPG (Unreal Engine 5 + Blender 5.2 LTS).
---

# Encounter Pacing & Combat Rhythm (Game Designer)

Panduan perancangan intensitas pertempuran, pacing musuh, kurva emosi pemain, dan alokasi *Emotional Bandwidth* di dalam dungeon Lentera Pudar merujuk pada [style-guide.md](file:///d:/GodotProjects/Lentera-Pudar/references/style-guide.md), [expert-psychology.md](file:///d:/GodotProjects/Lentera-Pudar/references/expert-psychology.md), dan [theory-reference.md](file:///d:/GodotProjects/Lentera-Pudar/references/theory-reference.md).

---

## 1. Ritme 4-Fase Encounter & Manajemen Emotional Bandwidth

1. **Intro (Pengenalan)**: Memperkenalkan jenis ancaman baru dalam lingkungan terkontrol dengan 1 musuh tunggal dekat sumber cahaya syal Aina (radius 3–5m warm point light 2700K).
2. **Escalation (Eskalasi)**: Menggabungkan musuh tersebut dengan variasi pola serangan atau rintangan lantai licin es. Ambient dungeon desaturasi mulai terasa — Curse Meter biasanya mulai meningkat ke rentang 26–60%.
3. **Twist (Tekanan Lingkungan)**: Pertarungan di area gelap dengan sumber cahaya terbatas, memaksa pemain mengandalkan radius syal lentera dan keputusan risk-reward Eyepatch. Potensi Curse Meter masuk zona Bahaya (61–90%).
4. **Relief & Reward (Pelepasan & Hadiah)**: Ruangan aman berpenerangan hangat (Altar Lentera atau Breather Room) berisi potongan memori Aina (Fixed Ratio Reward). Syal Aina kembali berdenyut normal, binaural whispers meredup.

---

## 2. Manajemen Ketegangan (Tension vs Relief) & Flow State

- **Tekanan Kutukan (Curse Pressure)**: Tangan beku protagonis menciptakan urgensi bertarung taktis. Kaelen mendapat +8–15 poin Curse per hit yang diterima, decay alami -2 s.d. -4 poin/detik saat tidak kena hit — jangan biarkan pemain merasa terlalu aman di kegelapan tanpa batas.
- **Lantern Light as Resource/Safety**: Cahaya syal Aina (800–1200 lm, radius 3–5m) adalah zona harapan. Pertempuran di luar radius cahaya memiliki risiko tinggi (Curse naik lebih cepat) tetapi reward kristal energi yang lebih berharga.
- **Telegraph Serangan Jelas (Competence via Readability)**: Serangan musuh wajib memiliki jeda animasi *wind-up* minimal 12 frame (0.40 detik @30fps) dengan warna kilau biru dingin `#4A6FA5` agar pemain dapat bereaksi (dodge: 2–4f startup, parry: 4–6f active window).

---

## 3. Parameter Combat Timing (Referensi Style Guide Bab 8)

| Aksi | Startup | Active | Recovery |
|---|---|---|---|
| Light Punch Combo | 3–5 frame | 4–6 frame | 6–10 frame |
| Heavy Cursed Strike | 12–18 frame | 6–8 frame | 15–20 frame |
| Evade Dash | 2–4 frame | 8–10 frame (i-frames) | 4–6 frame |
| Parry Window | — | 4–6 frame (@30fps) | 8–12 frame jika gagal |

> **Catatan baseline**: Angka di atas wajib direvisi berdasarkan hasil playtest Gate 2 (Grey-Box).

---

## 4. Kurva Intensitas per Sektor Dungeon

| Sektor | Tahap Grief | Saturasi World | Radius Syal | Intensitas Encounter |
|---|---|---|---|---|
| Sektor 1 (Denial) | Penyangkalan | 100% | 3–5m | Sedang — enemy single, pola straightforward |
| Sektor 2 (Anger) | Kemarahan | 85% | ~3.5m | Tinggi — serangan AoE, arena berubah |
| Sektor 3 (Bargaining) | Tawar-menawar | 70% | ~3m | Kompleks — puzzle, klon musuh, ilusi |
| Sektor 4 (Depression) | Depresi | 40–50% | 1.5–2.5m | Tertinggi — kesunyian mencekam, boss mirror |
| Sektor 5 (Acceptance) | Penerimaan | Naik ke 100% | Kembali ke 5m | Klimaks katarsis — tempo melandai menuju rekonsiliasi |

---

## 5. Aturan Breather Room (Tension-Release & Anti-Burnout)
- Setiap 2–3 arena encounter, WAJIB ada satu ruang *Breather Room* (sumber cahaya hangat, non-combat).
- Breather Room berfungsi sebagai: 1) titik *save/checkpoint*, 2) reset Curse Meter alami, 3) alokasi jeda afektif untuk memulihkan *Emotional Bandwidth* pemain, 4) interaksi dialog Aina untuk lore delivery.

---

## 6. Desain Spasial Arena vs FSM Musuh (Lihat [level-design-storytelling.md](file:///d:/GodotProjects/Lentera-Pudar/references/level-design-storytelling.md))
- **Arena Sempit / Koridor Rapat**: Disesuaikan untuk musuh bertipe melee brawler (Lord Alden) agar duel tight parry 1v1 terasa intens.
- **Arena Terbuka Berpilar**: Disesuaikan untuk ranged casters / teleporting enemies (Lady Vespera) untuk pemanfaatan cover sistem.
- **Sightline & Anticipation**: Kontrol visual reveal siluet musuh sebelum encounter untuk membangun tensi terukur.
- **Diegetic Breadcrumbing**: Pandu alur eksplorasi menggunakan cahaya syal lentera 2700K dan jejak pencairan es tanpa marker UI.

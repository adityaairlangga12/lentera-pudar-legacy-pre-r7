---
name: encounter_pacing
description: "Standar kurva kesulitan (difficulty curve), ritme encounter musuh, loop risiko-imbalan (risk-reward), dan pacing stamina/kutukan dalam dungeon Lentera Pudar — 3D Action RPG (Unreal Engine 5 + Blender 5.2 LTS)."
---

# Encounter Pacing & Combat Rhythm

## Purpose
Skill ini mengatur **prosedur perancangan intensitas pertempuran, ritme encounter musuh, kurva emosi pemain, dan alokasi emotional bandwidth** di dungeon *Lentera Pudar*.

Seluruh parameter timing kombat, frame data kemampuan GAS, daftar arketipe musuh, dan spesifikasi visibilitas sektor diatur secara kanonikal di [enemy-design-balancing.md](references/02-gameplay/enemy-design-balancing.md), [sector-ability-progression.md](references/02-gameplay/sector-ability-progression.md), dan [style-guide.md](references/04-art-3d/style-guide.md).

---

## Activate When
- Merancang komposisi gelombang musuh dan tata letak pertarungan per ruang dungeon.
- Mengevaluasi kurva kesulitan, keadilan wind-up telegraf musuh, dan parry window.
- Menentukan penempatan Breather Room dan interval pelepasan ketegangan (*relief*).
- Menyelaraskan arsitektur spasial arena terhadap state machine AI musuh.

---

## Do Not Use When
- Penulisan naskah cutscene naratif tanpa elemen pertempuran.
- Rigging armature 3D atau pemodelan topologi aset.

---

## Canonical Dependencies
- [references/02-gameplay/enemy-design-balancing.md](references/02-gameplay/enemy-design-balancing.md) — 5 Arketipe Duka, Telegraphing Readability & Balancing Kombat.
- [references/02-gameplay/sector-ability-progression.md](references/02-gameplay/sector-ability-progression.md) — 5 Kemampuan Naratif GRIS & Frame Data Kombat.
- [references/02-gameplay/level-design-storytelling.md](references/02-gameplay/level-design-storytelling.md) — Spasial Duka, Breadcrumbing Diegetik & Breather Rooms.
- [references/04-art-3d/style-guide.md](references/04-art-3d/style-guide.md) — Timing Kombat Numerik, Radius Cahaya Syal & Parameter Curse Meter.
- [references/05-foundations/psychology.md](references/05-foundations/psychology.md) — Teori Flow, Loss Aversion & Emotional Bandwidth.

---

## Prosedur Analisis & Perancangan Pacing

### 1. Ritme 4-Fase Encounter
1. **Intro (Pengenalan)**: Kenalkan ancaman/musuh baru dalam lingkungan terkontrol (1 musuh tunggal) di dekat radius cahaya syal Aina.
2. **Escalation (Eskalasi)**: Gabungkan musuh dengan variasi pola serangan atau rintangan spasial; Curse Meter mulai naik ke zona menengah.
3. **Twist (Tekanan Lingkungan)**: Pertarungan di area dengan visibilitas terbatas atau ancaman lingkungan, memaksa keputusan taktis antara perlindungan cahaya vs risiko penggunaan Eyepatch.
4. **Relief & Reward (Pelepasan & Hadiah)**: Ruangan aman (Altar Duka atau Breather Room) dengan pencahayaan hangat untuk memulihkan emotional bandwidth pemain.

### 2. Manajemen Ketegangan (Tension vs Relief)
- **Tekanan Kutukan (Curse Pressure)**: Tangan es menciptakan urgensi taktis. Pemain harus mengelola akumulasi kutukan dari serangan yang diterima vs peluruhan pasif saat menghindari bahaya merujuk ke [style-guide.md](references/04-art-3d/style-guide.md) Bab 9.
- **Lantern Light as Resource / Safety (Lumen Stakes)**: Radius cahaya syal Aina bertindak sebagai zona keamanan psikologis. Semakin dalam sektor yang dijelajahi, semakin terbatas radius penerangan (merujuk ke tabel visibilitas di [style-guide.md](references/04-art-3d/style-guide.md) Bab 7.C).
- **Keterbacaan Telegraf Serangan (Competence via Readability)**: Seluruh serangan musuh wajib memiliki jeda telegraf visual/audio yang jelas sebelum frame aktif merujuk ke [enemy-design-balancing.md](references/02-gameplay/enemy-design-balancing.md) Bab 3 agar pemain dapat merespons secara adil.

### 3. Penegakan Frame Data Kombat
- Evaluasi rangkaian kombo Kaelen, buffer window finisher (`GA_ShatterStrike`), parry window, dan hit-stop presisi terhadap tabel kanonikal di [sector-ability-progression.md](references/02-gameplay/sector-ability-progression.md) dan [enemy-design-balancing.md](references/02-gameplay/enemy-design-balancing.md).

### 4. Aturan Wajib Breather Room & Safe Archways
- Validasi keberadaan dan interval kemunculan ruang **Breather Room** (area non-combat berpenerangan hangat) terhadap spesifikasi aktif di [level-design-storytelling.md](references/02-gameplay/level-design-storytelling.md) dan [design-decisions.md](references/01-core/design-decisions.md).
- Breather Room berfungsi untuk: 1) titik checkpoint diegetik, 2) pemulihan pasif Curse Meter, 3) alokasi jeda kontemplatif untuk mencegah kelelahan afektif pemain (*emotional burnout*), 4) penyampaian lore puitis Aina.

### 5. Simbiosis Spasial Arena vs FSM Musuh
- Hindari arena datar berbentuk kotak polos. Integrasikan pilar reruntuhan, elevasi tangga, dan retakan es destructible untuk memberi opsi navigasi taktis bagi pemain merujuk ke [level-design-storytelling.md](references/02-gameplay/level-design-storytelling.md).

---

## Output Expectations (Encounter Pacing Audit)

```markdown
# ⚔️ Encounter Pacing & Combat Rhythm Audit
- **Sektor / Ruang Dungeon**: [Nama Area / Sektor Duka]
- **Status Evaluasi**: [BALANCED / HIGH FATIGUE / LOW TENSION]

### 1. Evaluasi Struktur 4-Fase & Alokasi Bandwidth
- [Analisis alur Intro ➔ Escalation ➔ Twist ➔ Relief]

### 2. Keterbacaan Telegraf & Keadilan Respon
- [Evaluasi wind-up musuh dan jendela reaksi parry/evade]

### 3. Evaluasi Taruhan Visibilitas & Curse Stakes
- [Kesesuaian radius cahaya syal dan interval Breather Room]

### 4. Rekomendasi Penyesuaian Ritme (Action Items)
- [Langkah balancing konkret]
```

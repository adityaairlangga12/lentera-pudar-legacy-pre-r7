---
name: creative_vision_direction
description: "Pustaka keahlian arahan visi kreatif, filosofi seni melankolis-hangat The Triad, resonansi puitis tragedi Kaelen & Aina, diksi dialog emosional, kurasi visual reference board, dan kalibrasi mutu Few-Shot untuk semesta Lentera Pudar — 3D Action RPG (Unreal Engine 5 + Blender 5.2 LTS)."
---

# Creative Vision & Poetic Narrative Direction

Skill ini membimbing seluruh agen (*Art Director*, *Game Designer*, *Psychology Agent*, *3D Modeler*) untuk melahirkan karya, dialog, desain level, dan visual yang memiliki jiwa puitis, resonansi duka mendalam, dan kehangatan khas *Lentera Pudar* merujuk pada [reference-board-guide.md](file:///d:/GodotProjects/Lentera-Pudar/references/04-art-3d/reference-board-guide.md), [few-shot-calibration.md](file:///d:/GodotProjects/Lentera-Pudar/references/06-pipeline-qc/few-shot-calibration.md), dan [expert-art-creativity.md](file:///d:/GodotProjects/Lentera-Pudar/references/05-foundations/art-creativity.md).

---

## 1. Hukum Dualitas Suhu & Emosi (The Triad Emotional Law)

Setiap karya kreatif (baik itu siluet model 3D, efek partikel, tata cahaya Lumen, maupun baris dialog) wajib memancarkan kontras antara **Dua Kutub Suhu**:

1. **Kutub Dingin (6500K Kelvin — `#4A6FA5` & `#7EE8FA`):**
   - Mewakili keputusasaan, kristal es, mati rasa batin (*apathy*), penyesalan masa lalu, dan kebekuan dungeon.
   - Bahasa visual: Sudut-sudut tajam (*angular faceted shards*), uap beku Niagara, shader distorsi live, desaturasi global post-process menurun per sektor (Kategori `01_palet_warna_kontras` & `05_curse_progression`).
2. **Kutub Hangat (2700K Kelvin — `#F4B860`):**
   - Mewakili jiwa pengorbanan Aina, api syal lentera, dan penerimaan duka.
   - Bahasa visual: Cahaya lembut melingkar (*soft Lumen emissive glow*), partikel percikan bara api melayang (`FX_Warmth_Embers`), liukan kain syal yang lentur (Chaos Cloth Spring Bones 0.4–0.6 stiffness).
3. **Kutub Netral (`#2A211C` / `#141013`):**
   - Mewakili makam kuno, batuan dungeon, jubah kelana, dan realitas dunia yang fana (Kategori `03_environment_organik`).

---

## 2. Kerangka Estetika & Kritik Seni Expert

### A. Uji Nilai Grayscale (*Value-First Mandate*)
- Setiap shot sinematik, komposisi kamera, dan desain level wajib diuji dalam mode **Grayscale**.
- Titik fokus utama (Syal Aina / Landmark Altar) harus tetap kontras dan terbaca jelas tanpa bantuan warna.

### B. Rasio Dominasi Warna Terkontrol 60-30-10
- **60% Dominan**: Netral Gelap (`#2A211C` & `#141013`) — batuan dan bayangan.
- **30% Sekunder**: Biru Dingin Kutukan (`#4A6FA5` & `#7EE8FA`) — es dan kabut.
- **10% Aksen**: Kuning Hangat Jiwa Aina (`#F4B860`) — pendaran syal dan percikan bara.

### C. Triad Kritik Seni Formal (Unity, Tension, Resolution)
- **Unity**: Seluruh aset melayani satu mood melankolis yang koheren.
- **Tension**: Kontras suhu 2700K vs 6500K dan asimetri cakar es vs perban.
- **Resolution**: Mata selalu diarahkan pada titik istirahat/harapan yang jelas (Altar Duka / Syal).

### D. Semiotika Visual Kumulatif
- Perubahan visual pada motif berulang (pemendekan syal, pembesaran retakan es, intensitas pendaran bara) wajib memiliki dasar naratif yang dibangun secara kumulatif.

---

## 3. Standar Karakterisasi & Diksi Dialog

### A. Kaelen (Protagonis — Pengelana Tangan Beku)
- **Ciri Khas**: Dingin di luar, hancur di dalam. Menolak mati rasa demi menepati janji pada Aina.
- **Prinsip Penulisan**:
  - Dilarang menulis dialog bersemangat heroik atau arogan.
  - Kalimat Kaelen harus padat, berat, dan reflektif.
  - Sering merespons dunia melalui bahasa tubuh 3D (menggenggam syal, menatap tangan esnya, menghela napas panjang — bukan melalui teks deskriptif).
- **Contoh Diksi**:
  > *"Syal ini... semakin pendek. Tapi langkahku belum boleh berhenti."*  
  > *"Jangan membeku di sini. Duka ini memang sakit, tapi kau harus tetap merasakannya."*

### B. Aina (Jiwa Syal Lentera)
- **Ciri Khas**: Lembut, bijaksana, penuh penerimaan (*acceptance*), mencintai Kaelen tanpa syarat.
- **Prinsip Penulisan**:
  - Nada bicara puitis dan menenangkan, seperti pelukan di tengah badai salju.
  - Tidak pernah menuntut atau menyalahkan Kaelen atas tragedi masa lalu.
  - Suaranya selalu disertai audio ducking (-6dB musik ambient, attack 150ms) agar terasa sakral.
- **Contoh Diksi**:
  > *"Jangan takut saat apiku memendek, Kaelen. Setiap percikan yang hilang sedang menyalakan kembali dunia yang sempat padam."*

---

## 4. Integrasi Estetika ke Dalam Gameplay & Mekanik 3D

- **The Fading Scarf (Pengorbanan Mekanik — SOP 4)**:
  - Pemendekan syal Aina di tiap altar bukan sekadar penurunan stat visual, melainkan momen emosional yang diperkuat oleh kamera close-up wajah Kaelen (FOV 35°–50°, jarak 1.2–1.8m ala Hellblade II — Kategori `06_kamera_closeup_emosional`), melodi piano berdebu yang semakin intim, dan desaturasi dunia progresif.
- **Cursed Hand Strike (Kutukan Sebagai Senjata — SOP 6)**:
  - Saat Kaelen menggunakan tangan kirinya (Heavy Cursed Strike), ada harga emosional yang dibayar: Curse Meter naik +10%, emissive kristal meningkat ke level Waspada (1.5–3.0), binaural whispers meningkat intensitasnya. Serangan es terasa kuat namun menyakitkan bagi Kaelen.
- **Eyepatch Risk-Reward (Penglihatan Spektral — Kategori 09)**:
  - Membuka penutup mata kanan = menatap keindahan dunia yang tersembunyi, sekaligus +3 poin Curse/detik. Ini adalah metafora visual: melihat lebih banyak kebenaran selalu memiliki harga.

---

## 5. Panduan Konsistensi Artstyle 3D (Kena Benchmark — SOP 5)
- Siluet karakter (Kaelen) harus selalu terbaca bersih dari kejauhan — syal kuning Aina harus kontras terhadap jubah gelap `#2A211C`.
- Setiap environment yang "dipulihkan" oleh syal Aina mendapat rona hangat bertahap — partikel `FX_Warmth_Embers` menyebar organik di area yang dilalui Kaelen.
- Rasio kontras cahaya hangat vs ambient dungeon minimum **8:1** (Sektor 1–3) hingga **12:1** (Sektor 4) — verifikasi via [few-shot-calibration.md](file:///d:/GodotProjects/Lentera-Pudar/references/06-pipeline-qc/few-shot-calibration.md) Contoh 4.
- Desain boss wajib merefleksikan manifestasi duka 5 tahap (Denial s.d. Acceptance) merujuk ke Contoh 6 pada Few-Shot Calibration.

---

## 6. Arahan Sinematik & Bahasa Kamera (Lihat [cinematics-cutscenes.md](file:///d:/GodotProjects/Lentera-Pudar/references/03-narrative/cinematics-cutscenes.md))
- **Kamera Representasi Mental**: Sudut pengambilan gambar dipilih berdasarkan kejujuran kondisi psikologis Kaelen.
- **Bahasa Kamera per Sektor**:
  - *S1 Denial*: Framing simetris kaku & statis (menolak melihat dari sudut lain).
  - *S2 Anger*: Handheld shake dinamis & cut cepat.
  - *S3 Bargaining*: Dutch angle & rotasi cermin manipulatif.
  - *S4 Depression*: Long take lambat, framing luas (karakter tenggelam dalam kehampaan).
  - *S5 Acceptance*: Framing lapang stabil & transisi fajar mulus.
- **Transisi Seamless**: Blend mulus over-shoulder gameplay ke shot sinematik tanpa hard cut hitam.
- **Shot Coverage & FACS Sync**: Rencanakan 3 shot (Wide, Medium, Close-Up) dengan cut presisi ke AU ekspresi wajah (`AU1`, `AU4`, `AU17`).

---

## 7. Referensi Dokumen Lengkap
- [references/03-narrative/cinematics-cutscenes.md](file:///d:/GodotProjects/Lentera-Pudar/references/03-narrative/cinematics-cutscenes.md) — Master Arahan Sinematik & Cutscene.
- [references/05-foundations/art-creativity.md](file:///d:/GodotProjects/Lentera-Pudar/references/05-foundations/art-creativity.md) — Master Kerangka Estetika & Kritik Seni Expert.
- [references/01-core/creative-vision.md](file:///d:/GodotProjects/Lentera-Pudar/references/01-core/creative-vision.md) — Pedoman artistik penuh & dualitas combat feel.
- [references/01-core/game-design-document.md](file:///d:/GodotProjects/Lentera-Pudar/references/01-core/game-design-document.md) — Master GDD 9 Bab.
- [references/04-art-3d/style-guide.md](file:///d:/GodotProjects/Lentera-Pudar/references/04-art-3d/style-guide.md) — Style Guide Numerik 11 Bab.
- [references/06-pipeline-qc/sop-workflow.md](file:///d:/GodotProjects/Lentera-Pudar/references/06-pipeline-qc/sop-workflow.md) — 7 SOP Operasional.
- [references/06-pipeline-qc/few-shot-calibration.md](file:///d:/GodotProjects/Lentera-Pudar/references/06-pipeline-qc/few-shot-calibration.md) — Benchmark Mutu Benar vs Salah.
- [references/04-art-3d/reference-board-guide.md](file:///d:/GodotProjects/Lentera-Pudar/references/04-art-3d/reference-board-guide.md) — 9 Kategori Shot-List Legal.

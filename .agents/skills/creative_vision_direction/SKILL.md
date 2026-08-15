---
name: creative_vision_direction
description: "Pustaka keahlian arahan visi kreatif, filosofi seni melankolis-hangat The Triad, resonansi puitis tragedi Kaelen & Aina, dan diksi dialog emosional untuk semesta Lentera Pudar — 3D Action RPG (Unreal Engine 5 + Blender 5.2 LTS)."
---

# Creative Vision & Poetic Narrative Direction

Skill ini membimbing seluruh agen (*Art Director*, *Game Designer*, *Psychology Agent*, *3D Modeler*) untuk melahirkan karya, dialog, desain level, dan visual yang memiliki jiwa puitis, resonansi duka mendalam, dan kehangatan khas *Lentera Pudar*.

---

## 1. Hukum Dualitas Suhu & Emosi (The Triad Emotional Law)

Setiap karya kreatif (baik itu siluet model 3D, efek partikel, tata cahaya Lumen, maupun baris dialog) wajib memancarkan kontras antara **Dua Kutub Suhu**:

1. **Kutub Dingin (6500K Kelvin — `#4A6FA5`):**
   - Mewakili keputusasaan, kristal es, mati rasa batin (*apathy*), penyesalan masa lalu, dan kebekuan dungeon.
   - Bahasa visual: Sudut-sudut tajam (*angular faceted shards*), uap beku Niagara, shader distorsi live, desaturasi global post-process menurun per sektor.
2. **Kutub Hangat (2700K Kelvin — `#F4B860`):**
   - Mewakili jiwa pengorbanan Aina, api syal lentera, dan penerimaan duka.
   - Bahasa visual: Cahaya lembut melingkar (*soft Lumen emissive glow*), partikel percikan bara api melayang (`FX_Warmth_Embers`), liukan kain syal yang lentur (Chaos Cloth Spring Bones 0.4–0.6 stiffness).
3. **Kutub Netral (`#2A211C`):**
   - Mewakili makam kuno, batuan dungeon, pakaian kelana, dan realitas dunia yang fana.

---

## 2. Standar Karakterisasi & Diksi Dialog

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

## 3. Integrasi Estetika ke Dalam Gameplay & Mekanik 3D

- **The Fading Scarf (Pengorbanan Mekanik)**:
  - Pemendekan syal Aina di tiap altar bukan sekadar penurunan stat visual, melainkan momen emosional yang diperkuat oleh kamera close-up wajah Kaelen (FOV 35°–50°, jarak 1.2–1.8m ala Hellblade II), melodi piano berdebu yang semakin intim, dan desaturasi dunia progresif.
- **Cursed Hand Strike (Kutukan Sebagai Senjata)**:
  - Saat Kaelen menggunakan tangan kirinya (Heavy Cursed Strike), ada harga emosional yang dibayar: Curse Meter naik +10%, emissive kristal meningkat ke level Waspada (1.5–3.0), binaural whispers meningkat intensitasnya. Serangan es terasa kuat namun menyakitkan bagi Kaelen.
- **Eyepatch Risk-Reward (Penglihatan Spektral)**:
  - Membuka penutup mata kanan = menatap keindahan dunia yang tersembunyi, sekaligus +3 poin Curse/detik. Ini adalah metafora visual: melihat lebih banyak kebenaran selalu memiliki harga.

---

## 4. Panduan Konsistensi Artstyle 3D (Kena Benchmark)
- Siluet karakter (Kaelen) harus selalu terbaca bersih dari kejauhan — syal kuning Aina harus kontras terhadap jubah gelap `#2A211C`.
- Setiap environment yang "dipulihkan" oleh syal Aina mendapat rona hangat bertahap — partikel `FX_Warmth_Embers` menyebar organik di area yang dilalui Kaelen.
- Rasio kontras cahaya hangat vs ambient dungeon minimum **8:1** (Sektor 1–3) hingga **12:1** (Sektor 4).

---

## 5. Referensi Dokumen Lengkap
- [references/creative-vision.md](file:///d:/GodotProjects/Lentera-Pudar/references/creative-vision.md) — Pedoman artistik penuh, contoh dialog per sektor, dan dualitas combat feel.
- [references/game-design-document.md](file:///d:/GodotProjects/Lentera-Pudar/references/game-design-document.md) — Bab II (Kosmologi & 5 Sektor), Bab III (Kaelen & Aina), Bab VII (Psikologi Auditori).
- [references/style-guide.md](file:///d:/GodotProjects/Lentera-Pudar/references/style-guide.md) — Bab 1 (Palet Warna Resmi), Bab 5 (Pencahayaan Lumen), Bab 10 (Audio).

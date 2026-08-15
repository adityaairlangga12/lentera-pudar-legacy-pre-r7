---
name: cross_check_docs
description: "Skill audit konsistensi silang yang dipicu via /cross-check-docs. Memeriksa konsistensi antara lore Lentera Pudar, GDD, AGENTS.md, file skill, dan kode implementasi Godot/Aseprite/Blender."
---

# Cross-Check Documentation Protocol (/cross-check-docs)

Skill ini memastikan seluruh dokumen master di `references/`, aturan sistem `AGENTS.md`, dan pustaka keahlian di `.agents/skills/` berada dalam kondisi 100% selaras tanpa adanya kontradiksi internal.

---

## 1. Titik Kritis Audit Konsistensi (Sync Checklist)

1. **Arsitektur Rendering Jalur B**:
   - Memastikan `AGENTS.md`, `references/design-decisions.md` (ADR-008), `references/game-design-document.md`, `references/style-guide.md`, dan `references/kaelen_pipeline_master_recipe.md` semuanya mengadopsi model **Blender 5.2 Low-Poly ➔ Godot 4.7.1 SubViewport Pixelation + Aseprite 2D**.
   - Tidak boleh ada dokumen yang masih menggunakan instruksi lama *prompt-only 2D generation tanpa validasi*.
2. **Kepatuhan Palet The Triad**:
   - Nilai hex `#F4B860` (Kuning Jiwa Aina), `#4A6FA5` (Biru Kutukan Pudar), `#2A211C` (Netral Gelap Batu/Jubah) tercantum seragam.
3. **Mekanik Khusus Lentera Pudar**:
   - *The Fading Scarf* (4-stage variant set), *CursedHand.gdshader* (live-driven uniform), *Echoes of the Past* (dual-layer room & dissolve), dan *The Hollow Reflection* (circular input replay buffer) terdokumentasi konsisten di GDD, Style Guide, dan Skills.
4. **Standar Penamaan 8-Arah Kardinal**:
   - Format `[aksi]_[arah]` kardinal (`south`, `north`, `east`, `west`, `south-east`, `south-west`, `north-east`, `north-west`) dipatuhi di seluruh skrip dan resource.

---

## 2. Output Audit
Laporan audit wajib menyajikan:
- Status sinkronisasi antar dokumen (100% In-Sync atau Divergence Detected).
- Daftar file yang telah diaudit beserta tautan markdown yang dapat diklik.

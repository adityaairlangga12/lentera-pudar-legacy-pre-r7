---
name: cross_check_docs
description: "Skill audit konsistensi silang yang dipicu via /cross-check-docs. Memeriksa konsistensi antara lore Lentera Pudar, GDD, AGENTS.md, file skill, dan kode implementasi 3D Blender 5.2 LTS / Unreal Engine 5."
---

# Cross-Check Documentation Protocol (/cross-check-docs)

Skill ini memastikan seluruh dokumen master di `references/`, aturan sistem `AGENTS.md`, dan pustaka keahlian di `.agents/skills/` berada dalam kondisi 100% selaras tanpa adanya kontradiksi internal untuk **3D Action RPG (Unreal Engine 5 + Blender 5.2 LTS)**.

---

## 1. Titik Kritis Audit Konsistensi (Sync Checklist)

1. **Arsitektur 3D Action RPG**:
   - Memastikan `AGENTS.md`, `references/design-decisions.md` (ADR-013), `references/game-design-document.md`, `references/style-guide.md`, dan `references/creative-vision.md` semuanya mengadopsi model **3D High-Detail di Blender 5.2 LTS + Unreal Engine 5 Pipeline**.
   - Tidak boleh ada dokumen atau skill yang masih menggunakan instruksi lama 2D/Godot/Aseprite/Pixellab.
2. **Kepatuhan Palet The Triad 3D**:
   - Nilai hex `#F4B860` (Kuning Jiwa Aina 2700K), `#4A6FA5` & `#7EE8FA` (Biru Kutukan Pudar 6500K), `#2A211C` / `#141013` (Netral Gelap Batu/Jubah/Eyepatch) tercantum seragam.
3. **Mekanik Khusus Lentera Pudar 3D**:
   - *The Fading Scarf* (Cloth Simulation & Spring Bones 4-stage sacrifice), *Cursed Ice Crystal Talons* (shader emissive live-driven), *Echoes of the Past*, dan *The Hollow Reflection* terdokumentasi konsisten di GDD, Style Guide, dan Skills.

---

## 2. Output Audit
Laporan audit wajib menyajikan:
- Status sinkronisasi antar dokumen (100% In-Sync atau Divergence Detected).
- Daftar file yang telah diaudit beserta tautan markdown yang dapat diklik.

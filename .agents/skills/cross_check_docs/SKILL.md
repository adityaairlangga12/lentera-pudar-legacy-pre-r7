---
name: cross_check_docs
description: "Skill audit konsistensi silang yang dipicu via /cross-check-docs. Memeriksa konsistensi antara lore Lentera Pudar, GDD, AGENTS.md, SOP Workflow, Few-Shot Calibration, Kena Art Research, Reference Board, dan seluruh master references 3D Blender 5.2 LTS / Unreal Engine 5."
---

# Cross-Check Documentation Protocol (/cross-check-docs)

Skill ini memastikan seluruh dokumen master di `references/`, aturan sistem `AGENTS.md`, dan pustaka keahlian di `.agents/skills/` berada dalam kondisi 100% selaras tanpa adanya kontradiksi internal untuk **3D Action RPG (Unreal Engine 5 + Blender 5.2 LTS)**.

---

## 1. Titik Kritis Audit Konsistensi (Sync Checklist)

1. **Arsitektur Dual-Layer 3D Action RPG**:
   - Memastikan `AGENTS.md`, [design-decisions.md](file:///d:/GodotProjects/Lentera-Pudar/references/design-decisions.md) (ADR-013 s.d. **ADR-018**), [game-design-document.md](file:///d:/GodotProjects/Lentera-Pudar/references/game-design-document.md), [theory-reference.md](file:///d:/GodotProjects/Lentera-Pudar/references/theory-reference.md), [tools-mcp-stack.md](file:///d:/GodotProjects/Lentera-Pudar/references/tools-mcp-stack.md), [qa-qc-framework.md](file:///d:/GodotProjects/Lentera-Pudar/references/qa-qc-framework.md), [style-guide.md](file:///d:/GodotProjects/Lentera-Pudar/references/style-guide.md), [sop-workflow.md](file:///d:/GodotProjects/Lentera-Pudar/references/sop-workflow.md), [few-shot-calibration.md](file:///d:/GodotProjects/Lentera-Pudar/references/few-shot-calibration.md), [reference-board-guide.md](file:///d:/GodotProjects/Lentera-Pudar/references/reference-board-guide.md), dan [kena-art-research.md](file:///d:/GodotProjects/Lentera-Pudar/references/kena-art-research.md) mengadopsi model **Dual-Layer Benchmark (Kena Visual + Hellblade Psikologi)** dan **Pipeline 3D (Blender 5.2 LTS + Unreal Engine 5)**.
2. **Kepatuhan Palet The Triad 3D**:
   - Nilai hex `#F4B860` (Kuning Jiwa Aina 2700K Warm Emissive), `#4A6FA5` & `#7EE8FA` (Biru Kutukan Pudar 6500K Cold Shard), `#2A211C` / `#141013` (Netral Gelap Batu/Jubah/Eyepatch) tercantum seragam.
3. **Mekanik Khusus Lentera Pudar 3D**:
   - *The Fading Scarf* (Chaos Cloth & Spring Bones 4-stage sacrifice & Dual-Mode cutscene), *Cursed Ice Talons* (shader emissive live-driven MPC), *The Sealed Eyepatch* (Perception mechanic Risk-Reward +3 pts/s), *Render Target Mask Dynamic Thawing*, *Live Mental Morphing Environment*, *Binaural Spatial Whispers*, dan *The Hollow Reflection* terdokumentasi konsisten di seluruh dokumen.
4. **Standar QA/QC 6-DoD & Stage-Gate**:
   - Menegakkan verifikasi 6 pilar Definition of Done (DoD), Stage-Gate 0 s.d. 7, dan klasifikasi bug 4-tier (Blocking, Critical, Major, Minor).
5. **Kepatuhan Prosedural SOP 7-Tahap**:
   - Menegakkan kepatuhan terhadap 7 SOP baku di `sop-workflow.md` (SOP 1: Prop, SOP 2: Material, SOP 3: Rigging, SOP 4: Cloth, SOP 5: Level Grey-Box, SOP 6: Gameplay GAS, SOP 7: Audio).
6. **Standar Parameter Numerik & Kena-Grade Art**:
   - Verifikasi konsistensi angka pasti di seluruh dokumen:
     - **Poly Budget Hero**: 40k–60k tris LOD0 (BUKAN 15k–30k — angka itu hanya deform base mesh pra-subdivisi).
     - **Hybrid Hair System**: Solid Geometry (Volume) + Alpha Strip Cards (Flyaways).
     - **Scarf Stiffness**: 0.4–0.6 (Syal Aina) vs 0.6–0.8 (Jubah Kaelen).
     - **Parry Window**: 4–6 frame @30fps / 8–12 frame @60fps (12 frame total = 0.2 detik adalah cara menyebutnya di GDD).
     - **Curse Meter +Eyepatch**: +3 poin/detik (bukan +3%, persentase hanya metafora naratif).
     - **Audio Target**: -16 LUFS combat BGM / -18 LUFS dialog / Ducking -6dB (attack 150ms, release 400ms).
     - **Chiaroscuro**: Key Light vs Ambient minimal 8:1 (Sektor 1–3), 12:1 (Sektor 4).

---

## 2. Output Audit
Laporan audit wajib menyajikan:
- Status sinkronisasi antar dokumen (✅ 100% In-Sync atau ⚠️ Divergence Detected).
- Daftar file yang telah diaudit beserta tautan markdown yang dapat diklik.
- Daftar gap yang ditemukan beserta klasifikasi severity (Kritis / Major / Minor) dan tindakan perbaikan yang dilakukan.

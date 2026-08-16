---
name: qc_check
description: "Standar eksekusi Quality Control (QC Gate) Komersial / Steam-Ready Grade via perintah /qc-check untuk 3D Action RPG (Unreal Engine 5 + Blender 5.2 LTS). Menjalankan 6 Pilar Definition of Done (DoD), 4-Tier Inspection, dan Klasifikasi Severity Bug."
---

# Commercial Release Quality Control (3D QC Gate Protocol)

> **Standar Mutu Komersial (Steam-Ready Grade)**: Setiap aset 3D, armature rig, material shader, skrip gameplay, level, dan audio diuji dengan tolok ukur kelayakan rilis publik di PC/Steam merujuk pada [qa-qc-framework.md](file:///d:/GodotProjects/Lentera-Pudar/references/qa-qc-framework.md), alur eksekusi [sop-workflow.md](file:///d:/GodotProjects/Lentera-Pudar/references/sop-workflow.md), [additional-techniques.md](file:///d:/GodotProjects/Lentera-Pudar/references/additional-techniques.md), dan kalibrasi mutu [few-shot-calibration.md](file:///d:/GodotProjects/Lentera-Pudar/references/few-shot-calibration.md).

---

## 1. Enam Pilar Definition of Done (DoD) & 4-Tier Inspection

```mermaid
flowchart TD
    A["3D Asset / Blueprint / Audio Under Test"] --> B["Tier 1: 3D Visual & Material Fidelity (The Triad & Texel Density)"]
    B -->|PASS| C["Tier 2: Functional & Runtime Performance (60 FPS / 0 Errors)"]
    C -->|PASS| D["Tier 3: Input, Save & Platform Compliance (Steam-Ready)"]
    D -->|PASS| E["Tier 4: Rigging, Bone Roll & glTF/FBX Export Integrity"]
    E -->|ALL PASS| F["APPROVED FOR COMMERCIAL 3D BUILD"]
    B -->|FAIL| R["REJECT & LOG TO qc-patterns.md"]
    C -->|FAIL| R
    D -->|FAIL| R
    E -->|FAIL| R
```

---

### 🎨 Tier 1: 3D Visual & Material Fidelity (Standar Grafis, The Triad & Texel Density)
- [ ] **Kepatuhan Palet The Triad 3D**:
  - Kuning Jiwa Aina: `#F4B860` (2700K Kelvin Warm Emissive pada syal, terhubung ke MPC).
  - Biru Kutukan Pudar: `#4A6FA5` & `#7EE8FA` (6500K Kelvin Cold Shard kristal es transparan dengan Subsurface Scattering).
  - Netral Gelap: `#2A211C` / `#141013` (Jubah kelana, eyepatch, batu dungeon).
- [ ] **Kualitas Shading, Siluet & Texel Density (Kena Benchmark)**:
  - Material PBR terdefinisi presisi (Roughness, Metallic, Transmission, SSS teruji dari $\ge 2$ sudut cahaya).
  - **Texel Density**: $512\text{ px/m}$ untuk Hero & Boss, $256\text{ px/m}$ untuk Prop Lingkungan.
  - Pencahayaan dinamis Lumen/PointLight tidak overexposed (Chiaroscuro 8:1 s.d. 12:1).
  - Lolos uji simulasi filter buta warna (*Colorblind Accessibility Check*).
- [ ] **Konsistensi Asimetri 3D**:
  - Lengan kiri kluster kristal es prisma $(-X)$ dan eyepatch mata kanan $(+X)$ konsisten secara geometris di seluruh sudut pandang kamera 360°.

---

### ⚡ Tier 2: Functional & Runtime Performance (Stabilitas Mesin & 60 FPS)
- [ ] **Nol Error Konsol & Zero Blocking Bugs**:
  - Runtime bersih dari error fatal, warning memori, dan zero softlock.
- [ ] **Penguncian Frame Rate Solid 60 FPS / 120 FPS**:
  - Waktu frame persentil ke-99 ($99^{th}$ percentile frame time) $< 16.6\text{ ms}$ di area terpadat sektor.
- [ ] **Animasi & Kinematika Biomekanik**:
  - Siklus gerak 8-fase lokomosi mulus dengan *Pelvic Tilt* dan *Counter-Rotation* tanpa *foot sliding*.
  - Simulasi fisika kain Syal Aina (*Chaos Cloth & 5-Bone Spring Chain*) berkibar alami tanpa distorsi atau clipping parah pada gerakan Idle, Jog, dan Evade Dash.
  - IK kaki aktif menyesuaikan kontur tanah/lantai dungeon.

---

### 🎮 Tier 3: Input, Save-State, Audio & Platform Compliance (Standar Steam & PC)
- [ ] **Dukungan Input Komprehensif**:
  - Kontrol Keyboard + Mouse dan Gamepad (Xbox, DualSense, Steam Deck) responsif dengan button glyphs dinamis.
  - Kamera Third-Person Adaptif (Eksplorasi FOV 78° vs Duel Boss FOV 70°) mulus dengan collision clipping prevention.
- [ ] **Integritas Save/Load (Steam Cloud Ready)**:
  - Protokol penulisan simpanan atomic anti-korupsi teruji stabil $\ge 10\text{x}$ siklus.
- [ ] **Audio Dynamic Ducking & Binaural Spatialization**:
  - Normalisasi loudness $-16\text{ LUFS}$ (Combat BGM) / $-18\text{ LUFS}$ (Dialog) dengan audio ducking ($-6\text{ dB}$, attack 150ms, release 400ms) saat narasi/bisikan jiwa beku.
  - Tata suara 3D binaural terverifikasi via headphone fisik.

---

### 🧪 Tier 4: Rigging, Bone Roll, Bony Landmarks & glTF/FBX Export Integrity
- [ ] **Armature & Transforms**:
  - Transform ter-apply 100% (`Location=(0,0,0)`, `Rotation=(0,0,0)`, `Scale=(1,1,1)`).
  - Orientasi rest pose $+Z$ forward / $+Y$ up.
- [ ] **Weight Painting & Bony Landmarks**:
  - Bony landmarks terbaca jelas (Acromion, Clavicle, Olecranon, Iliac Crest, Patella, Malleolus).
  - Corrective shape keys aktif pada fleksi siku 140° (+ Biceps Muscle Bulge) tanpa pinching atau volume loss.

---

## 2. Klasifikasi Severity Bug & Aturan Penanganan

| Severity | Dampak | Aturan Tindakan |
|---|---|---|
| 🔴 **Blocking** | Softlock, crash saat streaming level, progres terhenti total. | Wajib difix instan sebelum gate berikutnya. |
| 🟠 **Critical** | Pengalaman gameplay/narasi rusak (Curse Meter macet, clipping parah). | Wajib difix sebelum masuk fase Beta. |
| 🟡 **Major** | Transisi animasi kaku, ducking audio terlambat. | Wajib difix sebelum Release Candidate. |
| 🟢 **Minor** | Masalah kosmetik minor pada area tersembunyi. | Masuk backlog pemeliharaan. |

---

## 3. Format Laporan QC Wajib

```markdown
# 🛡️ 3D Quality Control Inspection Report

- **Target Inspeksi**: [Nama Asset 3D / Mesh / Scene]
- **Kategori**: [3D Visual / Rigging / Combat / Audio / Level]
- **Waktu Eksekusi**: [Timestamp]

### 📋 Checklist Evaluation (6-DoD & 4-Tier):
- [x] Tier 1: 3D Visual & Material Fidelity (The Triad & Texel Density) — PASS
- [x] Tier 2: Functional & Runtime Performance (60 FPS) — PASS
- [x] Tier 3: Input, Save & Platform Compliance — PASS
- [x] Tier 4: Rigging & Export Integrity — PASS

### 🎯 Keputusan Akhir:
**STATUS: [PASS / REJECTED]**
- **Severity (Jika Reject)**: [Blocking / Critical / Major / Minor]
- **Tindakan Perbaikan**: [Langkah teknis perbaikan]
```

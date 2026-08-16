---
name: orchestration_protocol
description: Protokol orkestrasi untuk Supervisor Agent dalam memecah task besar, mendelegasikan ke sub-agent (Hub-and-Spoke), menetapkan kriteria selesai eksplisit, memverifikasi artifact fisik, mengawasi kepatuhan SOP 7-tahap, dan kalibrasi mutu Few-Shot.
---

# Orchestration Protocol (Supervisor Agent)

Pustaka protokol untuk memandu Supervisor dalam mengelola alur kerja multi-agent secara sekuensial, terukur, dan bebas dari halusinasi/teater. Didesain untuk pipeline **3D Action RPG (Blender 5.2 LTS + Unreal Engine 5)** Lentera Pudar.

---

## 1. Prinsip Hub-and-Spoke
- Seluruh komunikasi berpusat pada Supervisor.
- Sub-agent tidak berkomunikasi langsung secara bebas (mencegah race condition dan context bloat).
- Supervisor bertanggung jawab menyintesis hasil dan melaporkan ke pengguna.

---

## 2. Siklus Delegasi 5 Langkah

1. **Identifikasi & Dekomposisi Prosedural (SOP Alignment)**:
   - Pecah tujuan pengguna menjadi sub-task berurutan dengan mengacu pada 7 alur baku di [sop-workflow.md](file:///d:/GodotProjects/Lentera-Pudar/references/sop-workflow.md) (SOP 1: Prop, SOP 2: Material, SOP 3: Rigging, SOP 4: Cloth, SOP 5: Level Grey-box, SOP 6: Gameplay GAS, SOP 7: Audio).
2. **Penugasan dengan Kriteria Selesai Eksplisit & Benchmark Few-Shot**:
   - Delegasikan ke agent yang tepat dengan instruksi yang merujuk pada standar [few-shot-calibration.md](file:///d:/GodotProjects/Lentera-Pudar/references/few-shot-calibration.md) dan shot-list [reference-board-guide.md](file:///d:/GodotProjects/Lentera-Pudar/references/reference-board-guide.md).
   - Contoh instruksi 3D terukur:
     - *"Model mesh karakter Kaelen di Blender 5.2 LTS mengikuti SOP 1 & SOP 3, hero proportions 1:6.8, target 40k–60k tris LOD0, ekspor ke `Content/Characters/SK_Kaelen_Body.fbx` — konfirmasi path file aktual dan poly count."*
     - *"Setup Material `M_Cursed_Crystal` di UE5 mengikuti SOP 2 dengan SSS Radius 0.5–1.2cm, Roughness 0.15–0.30, dan terhubung ke MPC `Curse_Spread` — lampirkan screenshot material graph."*
3. **Verifikasi Bukti Fisik (Artifact Gate)**:
   - Setelah sub-agent melapor, periksa keberadaan artifact fisik di filesystem (path file aktual, diff, tool call log, atau render screenshot dari `render_viewport_screenshot`). Dilarang percaya klaim naratif semata tanpa data numerik.
4. **Penanganan Kegagalan & Rejection Loop**:
   - Jika artifact tidak memenuhi standar QC (lihat [qa-qc-framework.md](file:///d:/GodotProjects/Lentera-Pudar/references/qa-qc-framework.md)), kembalikan ke sub-agent dengan feedback baris/poin spesifik. Maksimal 3x percobaan sebelum mengubah strategi dan eskalasi ke user.
5. **Laporan Akhir Faktual**:
   - Sajikan rangkuman ringkas berisi daftar tautan artifact nyata kepada pengguna.

---

## 3. Protokol Pola B (Dual-Perspective)
- **Kapan Digunakan**: Hanya untuk keputusan arsitektur struktural berbiaya tinggi (contoh: combat FSM architecture, save system, atau pemilihan antara Wwise vs MetaSounds) atau saat diminta eksplisit oleh user.
- **Format Output Wajib**:
  1. Pendekatan Utama (1-2 kalimat)
  2. Alasan & Pertimbangan
  3. Trade-off yang Dikorbankan
  4. Keselarasan dengan `style-guide.md`, `sop-workflow.md`, dan Lore
- **Pencatatan**: Setiap keputusan Pola B wajib didokumentasikan ke `references/design-decisions.md`.

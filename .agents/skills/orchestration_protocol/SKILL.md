---
name: orchestration_protocol
description: Protokol orkestrasi untuk Supervisor Agent dalam memecah task besar, mendelegasikan ke sub-agent (Hub-and-Spoke), menetapkan kriteria selesai eksplisit, memverifikasi artifact fisik, mengawasi kepatuhan SOP 7-tahap, kalibrasi mutu Few-Shot, dan menjalankan metodologi AI expert.
---

# Orchestration Protocol (Supervisor Agent)

Pustaka protokol untuk memandu Supervisor dalam mengelola alur kerja multi-agent secara sekuensial, terukur, transparan, dan bebas dari halusinasi/teater merujuk pada [expert-ai-methodology.md](file:///d:/GodotProjects/Lentera-Pudar/references/06-pipeline-qc/expert-ai-methodology.md). Didesain untuk pipeline **3D Action RPG (Blender 5.2 LTS + Unreal Engine 5)** Lentera Pudar.

---

## 1. Prinsip Dasar & Mode Kerja (Anti-Roleplay Mandate)
- **AI Sebagai Alat Produksi**: Bertindak murni sebagai instrumen rekayasa profesional fungsional, tanpa basa-basi teatrikal, roleplay semu, atau emosi buatan saat merespons tugas teknis.
- **Grounding 3-Sumber**: Seluruh keputusan dan parameter wajib tertelusur ke master references di `references/`, dokumentasi API resmi, atau observasi konkret di disk. Saat tidak tahu, lakukan verifikasi aktif; dilarang mengarang (*anti-hallucination*).
- **Prinsip Hub-and-Spoke**: Seluruh koordinasi dan sintesis berpusat pada Supervisor untuk mencegah context bloat dan race conditions.

---

## 2. Siklus Delegasi 5 Langkah

1. **Identifikasi & Dekomposisi Prosedural (Problem Decomposition & SOP Alignment)**:
   - Pecah tugas kompleks menjadi sub-task berurutan terstruktur: tentukan hasil akhir konkret, urutan dependensi, titik verifikasi, dan potensi risiko mengacu pada 7 SOP di [sop-workflow.md](file:///d:/GodotProjects/Lentera-Pudar/references/06-pipeline-qc/sop-workflow.md).
2. **Penugasan dengan Kriteria Selesai Eksplisit & Benchmark Few-Shot**:
   - Delegasikan ke agent dengan instruksi yang merujuk pada standar [few-shot-calibration.md](file:///d:/GodotProjects/Lentera-Pudar/references/06-pipeline-qc/few-shot-calibration.md) dan shot-list [reference-board-guide.md](file:///d:/GodotProjects/Lentera-Pudar/references/04-art-3d/reference-board-guide.md).
   - Contoh instruksi 3D terukur:
     - *"Model mesh karakter Kaelen di Blender 5.2 LTS mengikuti SOP 1 & SOP 3, hero proportions 1:6.8, target 40k–60k tris LOD0, ekspor ke `Content/Characters/SK_Kaelen_Body.fbx` — konfirmasi path file aktual dan poly count."*
     - *"Setup Material `M_Cursed_Crystal` di UE5 mengikuti SOP 2 dengan SSS Radius 0.5–1.2cm, Roughness 0.15–0.30, dan terhubung ke MPC `Curse_Spread` — lampirkan screenshot material graph."*
3. **Verifikasi Bukti Fisik (Self-Verification Loop & Artifact Gate)**:
   - Setelah sub-agent melapor, periksa keberadaan artifact fisik di filesystem (path file aktual, diff, tool call log, atau render screenshot dari `render_viewport_screenshot`). Dilarang percaya klaim naratif semata tanpa data numerik.
4. **Penanganan Kegagalan & Rejection Loop (Isolasi Variabel Debugging)**:
   - Jika artifact tidak memenuhi standar QC (lihat [qa-qc-framework.md](file:///d:/GodotProjects/Lentera-Pudar/references/06-pipeline-qc/qa-qc-framework.md)), lakukan debugging sistematis: ubah tepat satu variabel dalam satu waktu untuk mengisolasi penyebab masalah. Maksimal 3x percobaan sebelum eskalasi ke user.
5. **Laporan Akhir Faktual & Transparan**:
   - Sajikan rangkuman ringkas berisi: 1) apa yang pasti selesai dan terverifikasi, 2) apa asumsi yang diambil (dinyatakan eksplisit), 3) blocker/isu aktif jika ada.

---

## 3. Protokol Penanganan Ambiguitas (*Ambiguity Handling*)
- **Tanya ke User**: Jika keputusan berisiko tinggi, memiliki beberapa interpretasi arsitektur besar, atau bersifat destruktif/irreversible.
- **Putuskan Mandiri**: Jika ambiguitas bernilai minor, ada preseden jelas di dokumen master, dan asumsi yang diambil **disebutkan secara eksplisit** dalam laporan.

---

## 4. Protokol Pola B (Dual-Perspective Architectural Decisions)
- **Kapan Digunakan**: Hanya untuk keputusan arsitektur struktural berbiaya tinggi (contoh: combat FSM architecture, save system, atau pemilihan antara Wwise vs MetaSounds) atau saat diminta eksplisit oleh user.
- **Format Output Wajib**:
  1. Pendekatan Utama (1-2 kalimat)
  2. Alasan & Pertimbangan
  3. Trade-off yang Dikorbankan
  4. Keselarasan dengan `style-guide.md`, `sop-workflow.md`, dan Lore
- **Pencatatan**: Setiap keputusan Pola B wajib didokumentasikan ke [design-decisions.md](file:///d:/GodotProjects/Lentera-Pudar/references/01-core/design-decisions.md).

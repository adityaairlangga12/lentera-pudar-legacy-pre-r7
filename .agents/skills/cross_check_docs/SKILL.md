---
name: cross_check_docs
description: "Skill audit konsistensi silang yang dipicu via /cross-check-docs. Memeriksa konsistensi seluruh dokumen Lentera Pudar berbasis bukti fisik kutipan langsung, deteksi open gaps, deteksi duplikasi file, penilaian risiko/titik lemah, dan kepatuhan 8 aturan audit tanpa asumsi."
---

# Cross-Check Documentation Protocol (/cross-check-docs)

> **Dokumen Protokol Audit Konsistensi Silang (Master Cross-Check Standard)**  
> Menegakkan standar audit berbasis bukti fisik (*evidence-driven*), anti-halusinasi, pelaporan gap jujur, deteksi duplikasi, dan mitigasi risiko teknis/naratif di seluruh semesta *Lentera Pudar — 3D Action RPG (Unreal Engine 5 + Blender 5.2 LTS)*.

---

## 1. Delapan Aturan Baku Protokol Audit (The 8 Mandatory Audit Rules)

Setiap agen yang menjalankan tugas audit `/cross-check-docs` WAJIB mematuhi 8 aturan tanpa pengecualian:

### 1. Sumber Kebenaran Wajib dari Isi File Aktual (No-Session-Memory Mandate)
- Audit HARUS membaca ulang isi file yang relevan secara langsung menggunakan tool pembaca file (`view_file`, `grep_search`), bukan mengandalkan ringkasan percakapan sebelumnya atau asumsi judul file semata.
- Klaim yang tidak dapat ditelusuri ke isi file yang dibaca saat sesi berlangsung dilarang diberi status sinkron.

### 2. Wajib Bukti Kutipan Konkret untuk Setiap Klaim "Sinkron / Ada"
- Setiap baris verifikasi wajib mencantumkan bukti fisik dengan format minimal:
  - **Tautan File Markdown**: `[master-index.md](file:///d:/GodotProjects/Lentera-Pudar/references/01-core/master-index.md)`
  - **Nomor Bab / Seksi / Baris** yang tepat.
  - **Cuplikan Teks Kutipan Singkat** yang membuktikan klaim tersebut.
- **Aturan Baku Kolom Status Keselarasan & Larangan Self-Reference Cross-Check**:
  - Kolom `Status Keselarasan ✅` **HANYA boleh diisi** jika istilah/kode yang diklaim (nama variabel, tag GAS, event, Blueprint class) ditemukan **tertulis kata-per-kata di file eksternal yang dirujuk** saat pengecekan langsung dijalankan.
  - Jika klaim hanya berasal dari file yang sedang diedit/diaudit itu sendiri (*self-reference*) atau belum ditulis di file rujukan eksternal, **WAJIB ditulis `⚠️ Self-Reference / Belum Ada di File Eksternal` atau `❌ Belum Ada Referensi Eksternal`** apa adanya.
  - Dilarang keras menyimpulkan "selaras" dari kesamaan topik atau nama sistem yang mirip.
- Klaim tanpa kutipan teks dianggap **TIDAK VALID** dan harus diberi label `[Perlu Verifikasi]`.

### 3. Eksplisit Menyatakan Gap (Anti-Smoothing & No-Assumption Mandate)
- Dilarang keras menyimpulkan suatu topik "sudah cukup relevan / tercakup" hanya karena bersinggungan dengan sistem lain (misalnya: menganggap respawn otomatis ada karena combat feel sudah ada).
- Jika belum ada pembahasan langsung dan spesifik, topik tersebut WAJIB dicatat sebagai **OPEN GAP** tanpa dihalus-haluskan.

### 4. Larangan Klaim Ringkasan "100% Zero Gaps" Tanpa Bukti Rinci per Item
- Laporan audit yang hanya menampilkan kesimpulan optimis atau tabel checklist centang tanpa rincian kutipan per baris adalah **OUTPUT TIDAK VALID**.
- Status selesai hanya sah jika setiap parameter pendukung diverifikasi dengan kutipan aktual.

### 5. Penempatan "Open Gaps" di Bagian Awal Laporan
- Laporan audit wajib memisahkan secara tegas antara daftar **Open Gaps** dan daftar **Telah Terverifikasi Sinkron**.
- Bagian **Open Gaps** WAJIB diletakkan di bagian atas/awal laporan agar menjadi perhatian utama pembaca, bukan disembunyikan di akhir dokumen.

### 6. Siklus Audit Ulang Mandiri per Gap (Incremental Verification Cycle)
- Menutup satu gap di suatu modul TIDAK PERNAH mengasumsikan gap di modul lain otomatis selesai.
- Setiap gap memiliki siklus verifikasi mandiri: `Rancang ➔ Integrasikan ➔ Audit Ulang dengan Bukti Kutipan Baru`.

### 7. Deteksi Duplikasi File & Penegakan Single Source of Truth
- Audit wajib memindai file di root workspace (misal: `32_Daftar_Kemampuan...`, `33_Skenario_Tutorial...`) vs file di folder `references/`.
- Jika ditemukan duplikasi isi atau potensi tumpang tindih sumber kebenaran, audit wajib melaporkannya sebagai **Anomali Duplikasi** dan menetapkan file master di `references/` sebagai *Single Source of Truth (SSoT)* utama.

### 8. Bagian Wajib "Titik Lemah, Asumsi Kritis & Risiko Implementasi" (Deep Critical Reasoning Mandate)
- Setiap laporan audit WAJIB menjalankan analisis metakognitif mendalam (*deep critical reasoning*, bukan sekadar mendata keluhan umum) yang mencakup 4 pilar evaluasi kritis:
  1. **Analisis Tarikan Filosofis (*Core Tension Analysis*)**: Membedah potensi benturan filosofis antar pilar desain (misal: menjaga tensi duka lambat dan hening ala *Hellblade* tanpa mengorbankan kepuasan agensi mekanik ala *GRIS/Kena*).
  2. **Titik Rapuh Handoff Antar-Sistem (*System-Boundary Failure Modes*)**: Mengidentifikasi titik rawan kegagalan integrasi antar modul/engine (misal: transisi *Chaos Cloth vs Control Rig*, *Local CustomTimeDilation vs Global/Niagara Time*, live update *Material Parameter Collection*). **Setiap titik rapuh WAJIB langsung disertai rancangan mitigasi teknis konkret**.
  3. **Pencegahan Bias Generik AI (*Agent Alignment Guard*)**: Menilai kerentanan dokumen terhadap *creeping features* atau bias generik model AI (seperti kecenderungan mengusulkan skill tree/toko koin RPG konvensional).
  4. **Asumsi Psikologis yang Membutuhkan Validasi Playtest Manusia (`[Needs Human Playtest Validation]`)**: Mengidentifikasi hipotesis emosional yang tidak bisa divalidasi oleh AI semata (misal: *Pacing Monumental Sektor 4 / Solemn Engagement vs Disengaged Fatigue*, efektivitas *Loss Aversion $2.5\times$* dari penyempitan radius cahaya syal).

---

## 2. Struktur Format Laporan Audit Standar

Setiap laporan `/cross-check-docs` wajib mengikuti struktur berikut:

```markdown
# Laporan Audit Konsistensi Dokumentasi (/cross-check-docs)
*Tanggal Audit: YYYY-MM-DD | Auditor: [Nama Agent/Role]*

## 1. Daftar Open Gaps & Kebutuhan Desain Terbuka (Diletakkan di Awal)
(Tabel/Daftar gap terbuka, topik yang belum dibahas langsung, dan tingkat keparahan)

## 2. Deteksi Duplikasi File & Status Single Source of Truth (SSoT)
(Daftar file di root workspace vs references/, status sinkronisasi teks, dan penegakan SSoT)

## 3. Matriks Verifikasi Lintas-Sistem (Wajib Disertai Kutipan File & Bab)
| Parameter / Topik | Status | Tautan File & Bab/Baris | Bukti Kutipan Teks Aktual |
|---|---|---|---|

## 4. Evaluasi Titik Lemah, Asumsi Kritis & Risiko Implementasi
### A. Titik Rapuh Teknis, Kinesiologi & Integrasi Engine (dengan Solusi Arsitektur)
- [Masalah Handoff / Boundary] ➔ Solusi Teknis Terukur
### B. Analisis Tarikan Filosofis & Pencegahan Bias AI Sub-Agent
- Penegakan Anti-RPG Mandate & Grounded Kinetic Commitment
### C. Asumsi Emosional yang Membutuhkan Validasi Playtest Manusia ([Needs Human Playtest Validation])
- Hipotesis Emosional Intended vs Perceived & Indikator Lolos Uji

## 5. Rekomendasi Tindakan Selanjutnya (Action Items)
```

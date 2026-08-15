---
name: orchestration_protocol
description: Protokol orkestrasi untuk Supervisor Agent dalam memecah task besar, mendelegasikan ke sub-agent (Hub-and-Spoke), menetapkan kriteria selesai eksplisit, memverifikasi artifact fisik, dan mengeksekusi Pola B.
---

# Orchestration Protocol (Supervisor Agent)

Pustaka protokol untuk memandu Supervisor dalam mengelola alur kerja multi-agent secara sekuensial, terukur, dan bebas dari halusinasi/teater.

---

## 1. Prinsip Hub-and-Spoke
- Seluruh komunikasi berpusat pada Supervisor.
- Sub-agent tidak berkomunikasi langsung secara bebas (mencegah race condition dan context bloat).
- Supervisor bertanggung jawab menyintesis hasil dan melaporkan ke pengguna.

---

## 2. Siklus Delegasi 5 Langkah
1. **Identifikasi & Dekomposisi**: Pecah tujuan pengguna menjadi sub-task berurutan dengan dependensi yang jelas (lihat tabel routing di `AGENTS.md`).
2. **Penugasan dengan Kriteria Selesai Eksplisit**: Delegasikan ke agent yang tepat. Sertakan batas kerja yang tidak ambigu (misal: "Hasilkan 8 file spritesheet PNG 48x48 dan konfirmasi palet heksadesimal").
3. **Verifikasi Bukti Fisik (Artifact Gate)**: Setelah sub-agent melapor, periksa keberadaan artifact fisik di filesystem (path file, diff, tool call log, atau screenshot). Dilarang percaya klaim naratif semata.
4. **Penanganan Kegagalan & Rejection Loop**: Jika artifact tidak memenuhi standar QC, kembalikan ke sub-agent dengan feedback baris/poin spesifik. Maksimal 3x percobaan sebelum mengubah strategi dan eskalasi ke user.
5. **Laporan Akhir Faktual**: Sajikan rangkuman ringkas berisi daftar tautan artifact nyata kepada pengguna.

---

## 3. Protokol Pola B (Dual-Perspective)
- **Kapan Digunakan**: Hanya untuk keputusan arsitektur struktural berbiaya tinggi (contoh: save system, combat core architecture) atau saat diminta eksplisit oleh user.
- **Format Output Wajib**:
  1. Pendekatan Utama (1-2 kalimat)
  2. Alasan & Pertimbangan
  3. Trade-off yang Dikorbankan
  4. Keselarasan dengan `style-guide.md` dan Lore
- **Pencatatan**: Setiap keputusan Pola B wajib didokumentasikan ke `references/design-decisions.md`.

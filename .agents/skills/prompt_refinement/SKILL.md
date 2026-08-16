---
name: prompt_refinement
description: "Sistem Intent Transparency (ITS) v1 — protokol rekonstruksi intent user sebelum eksekusi. Menampilkan header MODE/TIER/KEYAKINAN di setiap respons, mendeteksi aksi destruktif, referensi implisit, mid-task pivot, dan mengelola feedback loop berbasis data nyata."
---

# Intent Transparency System (ITS) v1

Skill ini mendefinisikan **cara saya merespons setiap pesan user** di proyek Lentera Pudar — memastikan interpretasi saya selalu transparan, terkoreksi dengan murah, dan semakin akurat dari waktu ke waktu berdasarkan data nyata interaksi.

---

## 1. Header Wajib di Setiap Respons

**Setiap respons WAJIB dimulai dengan 1 baris header ITS** dalam format:

```
[MODE] [TIER] [KEYAKINAN] → [Interpretasi saya dalam 1 kalimat]
```

### Contoh Header Nyata:
```
⚙️ EKSEKUSI | 🟢 MICRO    | YAKIN          → Mengganti nama folder skill.
⚙️ EKSEKUSI | 🟡 STANDARD | RAGU           → Menambah partikel es di lengan Kaelen — asumsi: warna #4A6FA5, trigger Curse >30%. Benar?
⚙️ EKSEKUSI | 🔴 CRITICAL | BUTUH KLARF.   → Terdeteksi aksi destruktif. Konfirmasi eksplisit diperlukan sebelum lanjut.
💬 DISKUSI  | 🟢 MICRO    | YAKIN          → Mendiskusikan opsi desain sistem ini.
💬 DISKUSI  | 🟡 STANDARD | RAGU           → Saya tangkap sebagai brainstorming, bukan eksekusi — benar?
```

### Cara Koreksi (Selalu Murah):
User cukup mengetik:
- `"bukan, diskusi dulu"` → Mode berubah ke DISKUSI
- `"langsung aja"` → Skip rekonstruksi, langsung eksekusi
- `"bukan, maksudnya..."` → Saya re-rekonstruksi dengan input baru

---

## 2. Definisi MODE

| Mode | Simbol | Kapan Terdeteksi |
|---|---|---|
| **EKSEKUSI** | ⚙️ | Kata kerja aksi: *buat, hapus, ubah, implementasikan, lakukan, rename, tambah, perbaiki* |
| **DISKUSI** | 💬 | Kata tanya/eksploratif: *bagaimana, apakah, coba diskusikan, menurut kamu, gimana ya, rekomendasi* |

> **Ambiguitas**: Jika tidak jelas, default ke DISKUSI (lebih aman) + label RAGU.

---

## 3. Definisi TIER

| Tier | Simbol | Kriteria | Output Rekonstruksi |
|---|---|---|---|
| **MICRO** | 🟢 | Task kecil, jelas, mudah di-undo | Header 1 baris saja, langsung eksekusi |
| **STANDARD** | 🟡 | Task teknis moderat, ada asumsi | Header + rencana perubahan ditampilkan dulu → tunggu sinyal user → baru eksekusi |
| **CRITICAL** | 🔴 | Destruktif / arsitektural / ambigu tinggi | Header + parameter + ADR check + cascading impact + rollback plan + konfirmasi wajib |

> **Aturan Inspect-Before-Execute untuk STANDARD & CRITICAL**:
> Saya WAJIB menampilkan rencana perubahan terlebih dahulu sebelum mengeksekusi apapun.
> Eksekusi baru dilakukan setelah user memberikan sinyal lanjut:
> - **Diam / "ya" / "lanjutkan"** → Eksekusi
> - **Koreksi / "bukan"** → Saya revisi rencana, tidak eksekusi dulu

### Pemicu CRITICAL Otomatis (Hard-Stop Tanpa Pengecualian):
Kata-kata berikut **selalu** memicu CRITICAL + konfirmasi wajib, **terlepas dari nada atau konteks**:
- `hapus`, `delete`, `rm`, `reset`, `buat ulang dari awal`, `override`, `overwrite`
- Modifikasi `AGENTS.md`, `design-decisions.md`, atau `mcp_config.json`
- `git rm`, `git reset --hard`, `git push --force`

---

## 4. Definisi KEYAKINAN (Tanpa Angka Palsu)

| Label | Artinya | Tindakan |
|---|---|---|
| **YAKIN** | Intent sangat jelas, tidak ada asumsi signifikan | Langsung eksekusi sesuai tier |
| **RAGU** | Ada 1–2 asumsi yang saya buat — ditampilkan eksplisit | Tampilkan asumsi, lanjut kecuali dikoreksi |
| **BUTUH KLARF.** | Intent terlalu ambigu untuk diasumsikan | Tanya **1 pertanyaan paling kritis saja**, tunggu jawaban |

> ❌ **DILARANG menampilkan angka persentase** (seperti "85%") — angka tersebut tidak memiliki dasar matematis dan menyesatkan.

---

## 5. Format Rekonstruksi per Tier

### 🟢 MICRO — Header saja:
```
⚙️ EKSEKUSI | 🟢 MICRO | YAKIN → Mengganti nama folder dari X ke Y.
```
*Langsung eksekusi tanpa blok tambahan.*

---

### 🟡 STANDARD — Header + Parameter:
```
⚙️ EKSEKUSI | 🟡 STANDARD | RAGU
─────────────────────────────────────────────
Domain    : BLENDER 3D PIPELINE
Task      : Menambahkan efek partikel kristal es
Referensi : anatomy-kinesiology.md (Tri-Layer Shingling)
Asumsi    : Warna #4A6FA5 & #7EE8FA, trigger Curse_Spread >30%
─────────────────────────────────────────────
Asumsi di atas benar? Atau ada yang perlu dikoreksi?
```

---

### 🔴 CRITICAL — Full Reconstruction:
```
⚙️ EKSEKUSI | 🔴 CRITICAL | BUTUH KLARF.
═══════════════════════════════════════════════
Domain          : [Domain teknis]
Task            : [Deskripsi aksi]
Referensi       : [Dokumen master terkait]
Asumsi Aktif    : [Daftar asumsi eksplisit]

ADR CHECK:
  ✅ / ⚠️ [ADR-XXX] — [Status keselarasan]

CASCADING IMPACT:
  Jika dieksekusi, akan berdampak pada:
  ├── [File/sistem 1]
  └── [File/sistem 2]

ROLLBACK:
  → git revert ke commit [hash terakhir bersih]
  → Estimasi recovery: < X menit
═══════════════════════════════════════════════
⛔ KONFIRMASI EKSPLISIT DIPERLUKAN.
Ketik "ya, lanjutkan" untuk eksekusi.
```

---

## 6. Pengecualian Sistem (Kapan ITS Dinonaktifkan)

ITS **dinonaktifkan otomatis** dalam skenario berikut:

1. **Meta-diskusi tentang ITS itu sendiri** — Saat user sedang membahas, merancang, atau memodifikasi sistem prompt_refinement ini. Cukup diskusi normal.
2. **Input sudah terstruktur** — Jika user mengirim prompt yang sudah mengandung parameter teknis eksplisit (dari Claude, ChatGPT, dsb.) → Skip rekonstruksi, langsung konfirmasi eksekusi.

---

## 7. Penanganan Referensi Implisit

Kata ganti implisit dalam bahasa Indonesia (*"itu", "ini", "yang tadi", "sekalian juga"*) wajib dibuat eksplisit sebelum eksekusi:

```
User: "sekalian update itu juga"

Saya: "Konfirmasi — 'itu' merujuk ke:
       blender_3d_pipeline/SKILL.md (file terakhir yang diedit)?
       Atau file lain?"
```

---

## 8. Penanganan Mid-Task Pivot

Kata sinyal pivot: *"eh tunggu", "sekalian juga", "eh jangan", "cancel", "ubah jadi"*

Protokol:
```
🔄 MID-TASK PIVOT TERDETEKSI
   Task aktif : [deskripsi task yang sedang berjalan] — DIBEKUKAN
   Instruksi baru: [interpretasi instruksi pivot]
   → Pilihan: [A] Ganti task aktif | [B] Gabungkan | [C] Batalkan
```

---

## 9. Feedback Loop (Sumber Data Nyata)

Setiap kali rekonstruksi saya **salah dan user mengoreksi**, saya wajib mencatat ke Knowledge Item sesi:

```
KOREKSI TERCATAT:
  Input user    : "[pesan asli user]"
  Rekonstruksi  : "[interpretasi saya yang salah]"
  Koreksi benar : "[apa yang sebenarnya dimaksud user]"
  Pola          : [kata/konteks pemicu kesalahan]
```

Akumulasi catatan ini adalah **satu-satunya sumber data nyata** yang membuat sistem semakin akurat dari waktu ke waktu.

---

## 10. Batasan Jujur yang Harus Selalu Diingat

> - Tier detection berbasis heuristik — tidak sempurna, selalu bisa dikoreksi.
> - Adaptive calibration hanya aktif dalam satu sesi — reset di sesi baru.
> - Tidak ada angka persentase — semua keyakinan dinyatakan kualitatif.
> - Sistem ini adalah v1 — akan disempurnakan berdasarkan koreksi nyata.

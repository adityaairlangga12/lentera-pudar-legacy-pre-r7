# Aturan Scoped AI & Konfigurasi Ekosistem (.agents/)

Dokumen ini adalah aturan yang di-scope khusus saat AI Agent bekerja atau memodifikasi file di dalam direktori `.agents/`.

---

## 1. Proteksi Mutlak Hook Keamanan Git (Anti-Force-Push Guard)
- **Larangan Modifikasi/Penonaktifan**: AI Agent **DILARANG KERAS** menghapus, menonaktifkan (`"enabled": false`), atau mengubah logika pemeriksaan pada `hooks/block-force-push.sh` dan `hooks.json` tanpa izin eksplisit tertulis dari User.
- **Rasional Keamanan**: Hook ini adalah pertahanan terakhir yang mencegah eksekusi perintah destruktif `git push --force` atau `git push -f` yang berpotensi merusak riwayat repositori utama.

---

## 2. Konsistensi Format & Arsitektur Skill (`skills/*/SKILL.md`)
- **Struktur Frontmatter Wajib**: Setiap file skill baru di dalam `skills/*/SKILL.md` WAJIB memiliki YAML frontmatter yang valid dengan field `name` dan `description` yang terdefinisi jelas, konsisten dengan 9 skill utama yang sudah ada:
  ```yaml
  ---
  name: <nama_skill>
  description: "<Ringkasan fungsi dan pemicu pemanggilan skill>"
  ---
  ```
- **Prinsip Anti-Duplikasi (Single Source of Truth)**: Isi instruksi di dalam `SKILL.md` **WAJIB merujuk balik via tautan dokumen master** di folder `references/*.md`, bukan menduplikasi atau menulis ulang teori/spesifikasi desain secara mandiri.
- **Observability Protocol**: Setiap skill operasional wajib mematuhi standar *Inspect-Before-Execute* dan *Evidence-Driven* sesuai protokol utama proyek.

---

## 3. Proteksi Konfigurasi MCP Server (`mcp_config.json`)
- **Larangan Penghapusan Penanda `_TODO_lentera-ue5`**: AI Agent **DILARANG** menghapus entri `_TODO_lentera-ue5` secara diam-diam saat mengedit `mcp_config.json`.
- **Rasional Konfigurasi**: Entri `_TODO_lentera-ue5` adalah penanda sengaja (*intentional placeholder*) bahwa MCP Server untuk Unreal Engine 5 belum dikonfigurasi dan akan diaktifkan saat plugin Unreal Python Editor Scripting siap di Fase 4 Roadmap (merujuk pada `references/06-pipeline-qc/tools-mcp-stack.md` Bab 2).
- **Protokol Mutasi MCP**: Perubahan pada konfigurasi MCP server `lentera-blender` (Port 8097) atau penambahan server baru harus melalui verifikasi status server lokal sebelum dieksekusi.

---

## 4. Intent Transparency System (ITS) — Protokol Komunikasi Wajib

Seluruh respons AI Agent di proyek ini **WAJIB** mematuhi protokol komunikasi dan eksekusi Intent Transparency System v2 (ITS v2) yang terdefinisi secara kanonikal di [skills/prompt_refinement/SKILL.md](skills/prompt_refinement/SKILL.md).

**Prinsip Operasional Utama:**
1. **Transparansi Adaptif (*Adaptive Transparency*)**: Respons disajikan secara natural tanpa memaksakan header seragam. Penanda khusus (`[Asumsi Teknis: ...]`, `⛔ KONFIRMASI TINDAKAN KRITIS`, `⚠️ [CONFLICT]`, `⚠️ [CAPABILITY LIMIT]`) hanya dimunculkan secara proporsional sesuai tingkat risiko dan konteks.
2. **Evaluasi Risiko Semantik & Reversibilitas**: Risiko dinilai dari dampak semantik riil, blast radius, dan reversibilitas tindakan (bukan sekadar pencocokan nama file atau kata kunci).
3. **Disiplin Klarifikasi & Konfirmasi**: Klarifikasi hanya diajukan jika terjadi *Material Ambiguity* yang mengubah hasil tindakan secara signifikan. Konfirmasi eksplisit diwajibkan untuk aksi destruktif atau perubahan tata kelola.
4. **Kepatuhan Kebenaran Kapabilitas & Verifikasi**: Tool yang berstatus `STUB` atau `UNAVAILABLE` dilarang dieksekusi secara pura-pura. Klaim penyelesaian tugas wajib didukung bukti verifikasi independen fisik (`VERIFIED`).

**Pengecualian**: ITS dinonaktifkan saat user sedang membahas sistem ITS itu sendiri (meta-diskusi).

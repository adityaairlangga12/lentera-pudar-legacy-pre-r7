---
name: mcp_tools_pipeline
description: "Pemahaman arsitektur Blender 5.2 LTS MCP dan tata kelola integrasi tool 3D, standar layer API (Atomic, Macro, Workflow), prinsip observabilitas, dan kepatuhan kapabilitas 5-dimensi."
---

# Lentera Pudar — 3D MCP Tools Pipeline

## Purpose
Skill ini mengatur **protokol orkestrasi perkakas 3D MCP, pembagian layer API, targeting file fisik persisten (`blend_file`), prinsip observabilitas sebelum mutasi, dan tata kelola kebenaran kapabilitas perkakas** di semesta *Lentera Pudar*.

Seluruh spesifikasi antarmuka API, kontrak 23 Tool Publik, dan arsitektur MCP diatur secara kanonikal di [tools-mcp-stack.md](references/06-pipeline-qc/tools-mcp-stack.md) dan [master-index.md](references/01-core/master-index.md) Bab I (§1.5 & §1.6).

---

## Activate When
- Menjalankan operasi pemodelan, rigging, shading, atau ekspor melalui server MCP Blender 5.2 LTS (`lentera-blender-mcp`).
- Melakukan inspeksi scene state dan penanganan error/timeout pada eksekusi perkakas.
- Mengorkestrasi pipeline multi-langkah (*workflow tools*) yang melibatkan interaksi DCC.

---

## Do Not Use When
- Pengeditan dokumentasi konseptual murni yang tidak memerlukan pemanggilan tool MCP.
- Mengasumsikan eksekusi pada server perkakas yang belum diimplementasikan atau berstatus deferred.

---

## Canonical Dependencies
- [references/06-pipeline-qc/tools-mcp-stack.md](references/06-pipeline-qc/tools-mcp-stack.md) — Spesifikasi Rantai Perkakas MCP, Kontrak 23 Tool Publik & Status Implementasi.
- [references/06-pipeline-qc/api-cheat-sheet.md](references/06-pipeline-qc/api-cheat-sheet.md) — API Cheat Sheet & Contoh Pemanggilan MCP.
- [references/01-core/master-index.md](references/01-core/master-index.md) — Arsitektur Kapabilitas 5-Dimensi & Tingkatan Kebenaran Kapabilitas.

---

## Kebijakan Kebenaran Kapabilitas (*Capability Truth Policy*)

Setiap agen wajib membedakan 5 dimensi kapabilitas perkakas sesuai [master-index.md](references/01-core/master-index.md) §1.5:
$$\text{Tool Registration} \neq \text{Implementation} \neq \text{Server Availability} \neq \text{Execution} \neq \text{Verification}$$

### 1. Status Unreal Engine 5 MCP
- Server MCP Unreal Engine 5 berstatus **`PLANNED`** (penanda sengaja `_TODO_lentera-ue5` di `mcp_config.json`, dijadwalkan pada Fase 4 Roadmap).
- AI Agent **DILARANG MENGKLAIM** bahwa UE5 MCP saat ini aktif, tersedia, atau dapat dieksekusi secara otomatis.

### 2. Status Blender 5.2 LTS MCP (Hardened v1)
- Model eksekusi aktif adalah **`HEADLESS_FILE_BACKED`** via stdio MCP server.
- Tepat **23 Tool Publik Aktif** dan **17 Tool Deferred** (merujuk ke [tools-mcp-stack.md](references/06-pipeline-qc/tools-mcp-stack.md) Bab 3).
- Status pendaftaran skema perkakas (*Tool Registration*) tidak sama dengan keberadaan kode eksekusi nyata (*Implemented Handler*).
- Sebelum mengeksekusi operasi mutasi, pastikan tool yang dipanggil termasuk dalam 23 tool publik aktif.
- Respons `{status: "ok"}` atau payload hasil eksekusi HANYA berstatus `EXECUTED` dan dilarang diklaim sebagai tugas selesai sebelum diverifikasi secara independen.

---

## Kontrak Targeting File Fisik

1. **Targeting File Eksis (`blend_file`)**:
   - Seluruh mutasi pada scene yang sudah ada wajib menyertakan path `blend_file` yang valid.
   - Jangan pernah mengasumsikan state memori dari pemanggilan sebelumnya bertahan (*no cross-call in-memory session*).
2. **Targeting File Baru (`output_blend_file`)**:
   - Digunakan saat menginisialisasi scene/mesh baru (misal: `create_mesh_primitive`, `create_armature`).

---

## Pembagian 3 Layer API Terstandarisasi

Perkakas publik diorganisasikan ke dalam 3 layer:
1. **Atomic Tools**: Aksi tunggal deterministik dengan batas lingkup kecil (misal: `set_bone_roll`, `set_shading_mode`, `create_mesh_primitive`).
2. **Macro Tools**: Penggabungan beberapa aksi atomic menjadi satu tugas terarah (misal: alur `create_armature` $
ightarrow$ `add_bone` $
ightarrow$ `set_bone_roll`, atau `apply_modifier` $
ightarrow$ `merge_by_distance` $
ightarrow$ `unwrap_uv`).
3. **Workflow Tools**: Eksekusi alur sekuensial multi-tahap dengan pelaporan status per langkah (misal: `export_gltf` $
ightarrow$ `validate_export` $
ightarrow$ `render_viewport_screenshot`).

---

## Prinsip Observabilitas Sebelum Mutasi (*Inspect-Before-Mutate*)

Sebelum dan sesudah mengeksekusi operasi mutasi pada scene 3D:
1. **Inspeksi Awal**: Panggil tool observasi seperti `get_scene_state`, `list_objects`, atau `get_mesh_stats` dengan menyertakan `blend_file`.
2. **Eksekusi Terisolasi**: Jalankan mutasi dengan parameter terikat ketat.
3. **Inspeksi Diagnostik Pasca-Eksekusi**: Jika terjadi anomali, periksa log via `get_console_output` atau `get_last_error`.
4. **Verifikasi Independen**:
   $$\mathbf{VERIFIED} = \text{Task Acceptance Criteria} + \text{Observed Target State} + \text{Independent Evidence}$$
   - Modeling: `get_mesh_stats` / `get_object_state`
   - Rigging: `get_armature_state`
   - Ekspor: `validate_export`

---

## Output Expectations
- Pelaporan pemanggilan tool yang jujur mencantumkan status kapabilitas riil.
- Penggunaan alat observasi secara konsisten sebelum dan sesudah mutasi.

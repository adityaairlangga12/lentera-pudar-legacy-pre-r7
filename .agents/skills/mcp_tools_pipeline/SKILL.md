---
name: mcp_tools_pipeline
description: "Pemahaman arsitektur Blender 5.2 LTS MCP dan tata kelola integrasi tool 3D, standar layer API (Atomic, Macro, Workflow), prinsip observabilitas, dan kepatuhan kapabilitas 5-dimensi."
---

# Lentera Pudar — 3D MCP Tools Pipeline

## Purpose
Skill ini mengatur **protokol orkestrasi perkakas 3D MCP, pembagian layer API, batasan waktu (timeout), prinsip observabilitas sebelum mutasi, dan tata kelola kebenaran kapabilitas perkakas** di semesta *Lentera Pudar*.

Seluruh spesifikasi antarmuka API, kontrak perkakas, dan arsitektur MCP diatur secara kanonikal di [tools-mcp-stack.md](references/06-pipeline-qc/tools-mcp-stack.md) dan [master-index.md](references/01-core/master-index.md) Bab I (§1.5 & §1.6).

---

## Activate When
- Menjalankan operasi pemodelan, rigging, shading, atau ekspor melalui server MCP Blender 5.2 LTS.
- Melakukan inspeksi scene state dan penanganan error/timeout pada eksekusi perkakas.
- Mengorkestrasi pipeline multi-langkah (*workflow tools*) yang melibatkan interaksi DCC.

---

## Do Not Use When
- Pengeditan dokumentasi konseptual murni yang tidak memerlukan pemanggilan tool MCP.
- Mengasumsikan eksekusi pada server perkakas yang belum diimplementasikan atau belum tersedia.

---

## Canonical Dependencies
- [references/06-pipeline-qc/tools-mcp-stack.md](references/06-pipeline-qc/tools-mcp-stack.md) — Spesifikasi Rantai Perkakas MCP, Kontrak API & Status Implementasi.
- [references/06-pipeline-qc/api-cheat-sheet.md](references/06-pipeline-qc/api-cheat-sheet.md) — API Cheat Sheet & Tata Nama Fungsi.
- [references/01-core/master-index.md](references/01-core/master-index.md) — Arsitektur Kapabilitas 5-Dimensi & Tingkatan Kebenaran Kapabilitas.

---

## Kebijakan Kebenaran Kapabilitas (*Capability Truth Policy*)

Setiap agen wajib membedakan 5 dimensi kapabilitas perkakas sesuai [master-index.md](references/01-core/master-index.md) §1.5:
$$\text{Tool Registration} \neq \text{Implementation} \neq \text{Server Availability} \neq \text{Execution} \neq \text{Verification}$$

### 1. Status Unreal Engine 5 MCP
- Server MCP Unreal Engine 5 berstatus **`PLANNED`** (penanda sengaja `_TODO_lentera-ue5` di `mcp_config.json`, dijadwalkan pada Fase 4 Roadmap).
- AI Agent **DILARANG MENGKLAIM** bahwa UE5 MCP saat ini aktif, tersedia, atau dapat dieksekusi secara otomatis.

### 2. Status Blender 5.2 LTS MCP
- Implementasi perkakas Blender MCP berstatus perkakas eksekusi parsial saat ini.
- Ketersediaan proses server runtime wajib diverifikasi di lingkungan kerja aktif sebelum eksekusi dan tidak boleh diasumsikan otomatis tersedia.
- Status pendaftaran skema perkakas (*Tool Registration*) tidak sama dengan keberadaan kode eksekusi nyata (*Implemented Handler*).
- Gunakan jalur transport/eksekusi yang terkonfigurasi pada kontrak aktif di [tools-mcp-stack.md](references/06-pipeline-qc/tools-mcp-stack.md) dan lingkungan runtime saat ini.
- Sebelum mengeksekusi operasi mutasi, verifikasi apakah fungsi handler terkait berstatus `IMPLEMENTED` atau masih berupa `STUB` merujuk ke [tools-mcp-stack.md](references/06-pipeline-qc/tools-mcp-stack.md) Bab 3.
- Respons `{status: "ok"}` dari stub mock HANYA berstatus `EXECUTED` dan dilarang diklaim sebagai mutasi selesai.

---

## Pembagian 3 Layer API Terstandarisasi

Perkakas diorganisasikan ke dalam 3 layer:
1. **Atomic Tools**: Aksi tunggal deterministik dengan batas lingkup kecil (misal: `set_bone_roll`, `set_shading_mode`, `create_mesh_primitive`).
2. **Macro Tools**: Penggabungan beberapa aksi atomic menjadi satu tugas bermakna (misal: `create_armature`, `auto_weight_paint`, `unwrap_uv`, `apply_modifier`).
3. **Workflow Tools**: Eksekusi alur sekuensial multi-tahap dengan pelaporan status per langkah (misal: `export_gltf`, `validate_export`, `render_viewport_screenshot`).

---

## Prinsip Observabilitas Sebelum Mutasi (*Inspect-Before-Mutate*)

Sebelum mengeksekusi operasi mutasi yang kompleks pada scene 3D:
1. **Inspeksi Awal**: Panggil tool observasi seperti `get_scene_state` atau `render_viewport_screenshot` untuk memeriksa kondisi objek aktif.
2. **Eksekusi dengan Guard Batas Waktu**: Operasi perkakas dibatasi oleh batas waktu (*timeout*) aktif yang didefinisikan secara kanonikal pada kontrak MCP di [tools-mcp-stack.md](references/06-pipeline-qc/tools-mcp-stack.md).
3. **Inspeksi Error Pasca-Eksekusi**: Jika terjadi anomali atau kegagalan, segera periksa output log via `get_console_output` atau `get_last_error`.
4. **Verifikasi Hasil Fisik**: Validasi target geometri aktual sebelum menyatakan task selesai.

---

## Output Expectations
- Pelaporan pemanggilan tool yang jujur mencantumkan status kapabilitas riil.
- Penggunaan alat observasi secara konsisten sebelum dan sesudah mutasi.

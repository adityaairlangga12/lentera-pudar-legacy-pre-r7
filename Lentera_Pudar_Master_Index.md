# Master Index — Lentera Pudar
### Peta Lengkap Paket Dokumentasi Pra-Produksi (23 Dokumen)

Dokumen ini adalah titik masuk pertama untuk AI agent atau siapa pun yang mengerjakan proyek **Lentera Pudar**. Gunakan tabel di bawah untuk menemukan dokumen mana yang harus dirujuk untuk tugas tertentu, supaya tidak perlu membaca ulang 23 dokumen setiap kali, dan supaya tidak ada keputusan yang terlewat atau bertentangan antar dokumen.

---

## A. Fondasi Desain & Lore

| Dokumen | Isi | Rujuk Saat |
|---|---|---|
| **Lentera_Pudar_Moodboard_Referensi_Mekanik.md** | Referensi visual dan mekanik gabungan Kena (artstyle) + Hellblade 1 & 2 (mekanik combat) | Menentukan arah visual atau mekanik dasar sebuah fitur baru |
| **Lentera_Pudar_Referensi_Teori_untuk_AI_Agent.md** | Kumpulan teori non-matematis dasar (game dev, desain, produksi) yang jadi fondasi seluruh dokumen lain — termasuk rujukan awal ke bagian Fisika (13), Matematika (14), Psikologi (15) | Titik rujuk umum sebelum masuk ke dokumen expert yang lebih dalam |
| **Lentera_Pudar_Story_Bible_Lore.md** | Sumber kebenaran tunggal untuk lore: bio karakter (Kaelen, Aina), timeline cerita, aturan dunia, glosarium istilah (Altar Duka, The Fading Scarf, Hall of Mirrors, Deadzone Regrowth) | Menulis dialog, deskripsi environment, atau elemen naratif apa pun — wajib dicek supaya lore tidak dikarang/tidak konsisten |

---

## B. Teori Sains & Psikologi Tingkat Expert

| Dokumen | Isi | Rujuk Saat |
|---|---|---|
| **Lentera_Pudar_Fisika_Expert.md** | Matematika/mekanika di balik rigid body, cloth (PBD), fracture, fluid, global illumination, IK — plus tabel trade-off akurasi vs performa | Menyetel parameter solver fisika secara presisi di UE5/Blender |
| **Lentera_Pudar_Matematika_Expert.md** | Versi mendalam quaternion, easing/spline, SDF, noise, state machine — level detail lanjutan dari dasar di Referensi Teori bagian 14 | Implementasi teknis yang butuh landasan matematis (kamera, animasi, prosedural) |
| **Lentera_Pudar_Psikologi_Expert.md** | Versi mendalam Self-Determination Theory, loss aversion, reward timing, cognitive load, presence — dari dasar di Referensi Teori bagian 15 | Mendesain sistem reward, pacing emosional, atau UI/HUD |
| **Lentera_Pudar_Anatomi_Kinesiologi.md** | Proporsi tubuh, bony landmarks, rantai kinetik, gait cycle, deformasi sendi, batas rotasi realistis untuk Kaelen | Sculpting, weight-painting, rigging, atau animasi karakter |

---

## C. Seni, Visual & Produksi 3D

| Dokumen | Isi | Rujuk Saat |
|---|---|---|
| **Lentera_Pudar_Style_Guide_Numerik.md** | Parameter numerik konkret: warna, material, cloth, lighting, poly budget, timing frame combat | Kebutuhan angka pasti — bukan deskripsi kualitatif |
| **Lentera_Pudar_Panduan_Reference_Image_Board.md** | Shot-list kurasi referensi visual dari Kena dan Hellblade per kategori | Mengumpulkan/menyusun referensi visual terstruktur |
| **Lentera_Pudar_Riset_3D_Art_Kena.md** | Riset mendalam gaya 3D art Kena: Bridge of Spirits, lengkap dengan sumber/link | Memahami atau mereplikasi gaya 3D art acuan |
| **Lentera_Pudar_3D_Expert_Fondasi.md** | Teori fondasi 3D expert: topology, UV, PBR shading, rigging/deformation, LOD/optimasi, baking pipeline | Kerja teknis 3D model — pelengkap Riset 3D Art Kena dan Teknik Tambahan |
| **Lentera_Pudar_Kreativitas_Seni_Expert.md** | Nilai seni dan kreativitas tingkat expert, 8 area yang disepakati (komposisi, mood, dsb.) | Keputusan artistik yang butuh justifikasi lebih dari sekadar "terlihat bagus" |
| **Lentera_Pudar_Teknik_Tambahan.md** | Trim sheet, vertex color masking, kit-bashing, baking, texel density | Teknik produksi 3D spesifik yang belum tercakup di dokumen lain |

---

## D. Game Design & Audio

| Dokumen | Isi | Rujuk Saat |
|---|---|---|
| **Lentera_Pudar_Game_Design_Systems_Expert.md** | Teori level makro: core gameplay loop, kurva kesulitan/pacing seluruh game, struktur pacing 5 sektor grief secara gameplay | Merancang struktur permainan secara keseluruhan, bukan per-shot |
| **Lentera_Pudar_Audio_Sound_Design_Expert.md** | Teori audio dan sound design: musik adaptif, sound design, silence sebagai alat naratif | Domain audio — sebelumnya kosong sama sekali di paket dokumentasi |

---

## E. Tools, Pipeline & Referensi Teknis

| Dokumen | Isi | Rujuk Saat |
|---|---|---|
| **Lentera_Pudar_Daftar_Tools_MCP_dan_Software.md** | Daftar awal tools/MCP server dan software pendukung | Referensi historis — sudah digantikan oleh versi Stack di bawah |
| **Lentera_Pudar_Daftar_Tools_MCP_Stack.md** | Daftar lengkap dan terkini tools, software, dan MCP integrations (Blender, Unreal, Godot, texturing, rigging, VFX, optimasi) | Setup environment atau menambah tool baru ke pipeline |
| **Lentera_Pudar_API_Cheat_Sheet.md** | Referensi fungsi `bpy` (Blender Python) dan `unreal` (UE5 Python) | Scripting/automasi langsung di Blender atau UE5 |

---

## F. Proses AI, QA & Metodologi

| Dokumen | Isi | Rujuk Saat |
|---|---|---|
| **Lentera_Pudar_QA_QC_Framework.md** | Kerangka QA/QC ketat untuk menjaga produksi tetap terarah dan tidak berantakan | Sebelum dan sesudah setiap tugas produksi |
| **Lentera_Pudar_SOP_Workflow.md** | SOP/workflow step-by-step untuk tugas berulang (bikin prop baru, dsb.) | Mengerjakan tugas rutin — supaya konsisten setiap kali |
| **Lentera_Pudar_FewShot_Calibration.md** | Contoh baik vs buruk (few-shot) untuk beberapa jenis tugas kunci | Mengkalibrasi AI sebelum mulai tugas baru yang rawan salah arah |
| **Lentera_Pudar_AI_Automation_Visual_SelfReview_Protocol.md** | Protokol Visual Self-Review Loop — AI mengecek ulang hasil kerjanya sendiri (screenshot/render) sebelum dianggap selesai | Tugas visual yang butuh verifikasi hasil, bukan cuma eksekusi |
| **Lentera_Pudar_Metodologi_AI_Expert.md** | Cara berpikir dan bekerja AI level expert: grounding/anti-halusinasi, problem-solving, verifikasi, komunikasi, anti-roleplay | Prinsip dasar perilaku AI di seluruh proyek — paling fondasional dari semua dokumen |

---

## Urutan Baca yang Disarankan (untuk AI Agent Baru)

1. **Metodologi_AI_Expert** — cara berpikir dasar sebelum menyentuh dokumen lain
2. **Referensi_Teori_untuk_AI_Agent** + **Story_Bible_Lore** — konteks proyek dan dunia
3. **Moodboard_Referensi_Mekanik** + **Style_Guide_Numerik** — arah visual dan mekanik konkret
4. Dokumen expert sesuai domain tugas yang sedang dikerjakan (Fisika/Matematika/Psikologi/Anatomi/3D/Audio/Game Design)
5. **QA_QC_Framework** + **SOP_Workflow** — sebelum eksekusi
6. **AI_Automation_Visual_SelfReview_Protocol** — setelah eksekusi, untuk verifikasi hasil

---

*Dokumen ke-23 dari paket dokumentasi pra-produksi Lentera Pudar. Jika ada dokumen baru ditambahkan di kemudian hari, perbarui tabel di atas supaya index ini tetap jadi peta yang akurat.*

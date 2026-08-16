# Playtesting & Validasi Emosional — Lentera Pudar Master Reference
### Metodologi Pengukuran Resonansi Duka (*Grief Impact*), Observasi Non-Intrusif, & Evaluasi Intended vs Perceived

> **Dokumen Sumber Kebenaran Validasi Emosional (*Emotional Playtesting Reference*)**  
> Melengkapi [qa-qc-framework.md](file:///d:/GodotProjects/Lentera-Pudar/references/qa-qc-framework.md), [expert-psychology.md](file:///d:/GodotProjects/Lentera-Pudar/references/expert-psychology.md), dan [creative-vision.md](file:///d:/GodotProjects/Lentera-Pudar/references/creative-vision.md). Menjawab pertanyaan krusial: *"Apakah dampak emosional duka Kaelen & Aina benar-benar tersampaikan kepada pemain manusia, bukan sekadar berfungsi tanpa bug secara teknis?"*

---

## 1. Perbedaan Mendasar: Playtesting Fungsional vs Emosional
- **Playtesting Fungsional (QA/QC)**: Mengukur stabilitas sistem, ketiadaan softlock, konsistensi frame rate (60 FPS), dan kepatuhan style guide.
- **Playtesting Emosional**: Mengukur keterlibatan afektif, keselarasan emosi yang dirasakan pemain dengan maksud desain (*intended emotion*), dan kedalaman resonansi tema duka (*Kübler-Ross 5 Stages of Grief*).
- **Prinsip Metodologis**:
  - Sampel kecil kualitatif (3–5 playtester baru yang belum membaca lore) sudah memadai untuk mendeteksi kesenjangan emosi.
  - Data perilaku non-verbal dan jeda hening lebih akurat dibanding jawaban kuesioner tertulis langsung.

---

## 2. Kerangka "Intended vs Perceived Emotion" (Gap Analysis)
Untuk setiap momen kunci dan cutscene transisi sektor duka, tim menyusun matriks evaluasi:

| Elemen Evaluasi | Definisi & Komponen |
|---|---|
| **Intended Emotion** | Emosi yang dirancang untuk dirasakan pemain (misal: *Denial* = rasa tersesat & penolakan; *Depression* = kepasrahan beku). |
| **Design Signals** | Sinyal terukur: Pencahayaan Kelvin, musik adaptif, FACS Action Units (`AU1`, `AU15`, `AU43`), layout level spasial. |
| **Perceived Emotion** | Respon emosional murni yang dilaporkan/teramati dari playtester manusia tanpa diarahkan (*unprimed*). |

*Analisis Kesenjangan (Gap)*: Kesenjangan antara *Intended* dan *Perceived* menjadi dasar revisi desain (contoh: bila Sektor 4 *Depression* dipersepsikan sebagai "bosan/monoton", bukan "keheningan berbobot", maka pacing audio dan detail mikrotekstur es perlu disetel ulang).

---

## 3. Protokol Observasi Non-Intrusif (*Non-Intrusive Observation*)
- **Minimal Think-Aloud**: Menghindari instruksi berbicara terus-menerus yang dapat memecah perenungan batin pemain.
- **Observasi Bahasa Tubuh Playtester**:
  - *Condong ke Depan*: Keterlibatan tinggi / tensi (*engaged*).
  - *Bersandar / Menghela Nafas*: Kelelahan mental atau pelepasan emosional (*catharsis*).
  - *Jeda Hening Alami*: Indikator keberhasilan transmisi momen duka tanpa kata (*The Power of Silence*).
- **Post-Session Reflection Interview**: Pertanyaan terbuka diajukan *setelah* sesi selesai (bukan di tengah gameplay) untuk menjaga imersi.
- **Uji Retensi Memori Jangka Panjang**: Evaluasi follow-up satu minggu setelah sesi untuk menguji momen mana yang melekat secara permanen di memori pemain.

---

## 4. Indikator Keberhasilan Emosional per Sektor Duka

| Sektor Duka | Indikator Keberhasilan Observasi Playtest Manusia |
|---|---|
| **Sektor 1: Denial** | Playtester sempat meragukan apakah koridor berulang adalah bug sebelum menyadari makna simbolis penolakan. |
| **Sektor 2: Anger** | Frekuensi input tombol dan kecepatan gerak kamera playtester meningkat secara fisik/agresif. |
| **Sektor 3: Bargaining** | Playtester ragu-ragu di persimpangan cermin dan mengevaluasi konsekuensi tawar-menawar ilutif. |
| **Sektor 4: Depression** | Terjadi hening kontemplatif yang natural; playtester merasakan beban langkah kaki Kaelen yang berat. |
| **Sektor 5: Acceptance** | Relaksasi postur tubuh, nada bicara tenang saat wawancara, dan rasa keikhlasan melepaskan. |

---

## 5. Batasan Eksplisit AI Agent & Eliminasi Bias
- **Mandat Batasan AI**: AI Agent (termasuk Visual Self-Review) HANYA dapat memverifikasi kepatuhan teknis desain (FACS AU, layout grey-box, parameter lighting). AI **DILARANG MENGANGGAP** kepatuhan teknis sama dengan validasi emosional manusia yang berhasil.
- **Penandaan Wajib Human Validation**: Setiap rancangan cutscene atau transisi altar duka wajib ditandai status: `[Needs Human Playtest Validation]`.
- **Anti-Leading Questions**: Dilarang mengajukan pertanyaan sugestif ("Apakah Anda merasa sedih?"); wajib menggunakan pertanyaan terbuka non-direktif.

---

## 6. Prosedur Standar Sesi Playtest 5-Langkah
1. **Briefing Minimal**: Tanpa membocorkan tema grief atau lore mendalam.
2. **Sesi Bermain Murni (30–45 Menit)**: Tanpa interupsi eksternal.
3. **Cooling-Off Period (3–5 Menit)**: Jeda hening sebelum transisi ke mode evaluasi.
4. **Wawancara Reflektif Terbuka**: Menggali momen yang paling membekas secara subjektif.
5. **Follow-Up Retensi (1 Minggu Pasca-Sesi)**: Mengidentifikasi resonansi memori jangka panjang.

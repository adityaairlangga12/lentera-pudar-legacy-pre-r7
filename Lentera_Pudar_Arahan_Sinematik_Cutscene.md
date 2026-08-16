# Arahan Sinematik & Cutscene — Lentera Pudar
### Menyambungkan Ekspresi, Ruang, dan Lore ke Bahasa Kamera (Pelengkap Kreativitas Seni Expert)

`Kreativitas_Seni_Expert.md` sudah menyebut prinsip sinematografi secara umum (framing, depth of field, bahasa kamera ala Hellblade). Dokumen ini turun ke level lebih teknis dan actionable: **kapan** memakai teknik kamera tertentu, bagaimana menyusun pacing antara cutscene dan gameplay, dan bagaimana menyambungkan momen sinematik ke aset yang sudah dibangun (ekspresi wajah dengan AU, level design spasial, lore di Story Bible) supaya cutscene tidak berdiri sendiri, tapi memperkuat semua keputusan yang sudah dibuat sebelumnya.

---

## 1. Prinsip Dasar: Kamera sebagai Sudut Pandang Emosional, Bukan Cuma Alat Tampil

Mengikuti pendekatan Hellblade sebagai referensi, kamera di Lentera Pudar sebaiknya tidak dianggap sebagai "alat netral menampilkan aksi", tapi sebagai representasi *keadaan mental Kaelen saat itu*. Pertanyaan yang perlu dijawab sebelum menentukan shot: bukan "sudut mana yang paling terlihat bagus?", tapi "sudut mana yang paling jujur menunjukkan apa yang Kaelen rasakan/lihat di momen ini?"

---

## 2. Bahasa Kamera per Sektor Grief

Menyambung pola pemetaan yang konsisten di dokumen lain:

| Sektor | Karakteristik Kamera | Alasan |
|---|---|---|
| **Denial** | Framing simetris kaku, jarak kamera-karakter konsisten/tidak berubah, sedikit variasi angle | Kekakuan kamera meniru "menolak melihat dari sudut lain" — visual dari penyangkalan |
| **Anger** | Handheld shake ringan, cut lebih cepat, close-up mendadak | Ketidakstabilan kamera meniru ketidakstabilan emosi — konsisten dengan referensi kamera dekat Hellblade II |
| **Depression** | Long take (durasi shot lebih panjang tanpa cut), kamera statis atau bergerak sangat lambat, framing lebih jauh/kecil (karakter "tenggelam" dalam frame) | Durasi shot yang panjang secara literal membuat penonton merasakan "beratnya waktu", konsisten dengan skala ruang luas-kosong di Level_Design bagian 2.C |
| **Acceptance** | Framing mulai terbuka, kamera lebih stabil dan halus, transisi antar shot lebih mulus (bukan hard cut) | Stabilitas kamera merepresentasikan ketenangan yang dicapai — kontras eksplisit dengan Denial (kaku) dan Anger (goyang) |

---

## 3. Pacing: Gameplay vs Cutscene

- **Minimalkan Hard Cut Gameplay→Cutscene**: mengikuti tren desain modern (termasuk Hellblade), transisi ke cutscene sebaiknya seamless — kamera "mengambil alih" secara halus dari perspektif gameplay, bukan potongan tiba-tiba ke layar hitam lalu cutscene baru mulai.
- **Interactive Cutscene sebagai Default, Cutscene Penuh sebagai Pengecualian**: pemain tetap punya kontrol minor (gerakan kepala/kamera terbatas) selama momen naratif berlangsung jika memungkinkan — cutscene yang benar-benar mengambil kontrol penuh sebaiknya dipakai hemat, khusus untuk momen puncak (transisi antar sektor grief besar, bukan tiap dialog kecil).
- **Durasi Cutscene Proporsional ke Bobot Naratif**: cutscene panjang untuk momen berat (transisi sektor), cutscene singkat/bahkan tanpa cutscene formal (cukup scripted moment dalam gameplay) untuk beat naratif kecil — hindari treatment yang sama untuk semua momen dialog.
- **Sisipkan Silent Beat**: mengikuti prinsip silence sebagai alat naratif dari Audio_Sound_Design_Expert, sengaja sisipkan jeda tanpa dialog/musik di titik emosional puncak — cutscene tidak harus selalu "penuh" secara audio-visual.

---

## 4. Shot Planning untuk Momen Naratif Kunci

- **Coverage Minimum per Beat Emosional**: untuk tiap beat dialog/momen penting, rencanakan minimal 3 jenis shot — wide (konteks ruang, rujuk Level_Design), medium (bahasa tubuh), close-up (ekspresi wajah dengan AU spesifik, rujuk Ekspresi_Wajah_Manusia) — supaya ada fleksibilitas editing tanpa harus render ulang.
- **Close-up Timing Terkait AU**: waktu cut ke close-up sebaiknya presisi ke saat AU kunci muncul (misal cut ke close-up tepat saat AU17/menahan tangis aktif), bukan close-up generik yang timing-nya asal — sinkronisasi ini yang membuat cutscene terasa disutradarai dengan cermat, bukan kebetulan.
- **Reaction Shot sebagai Prioritas**: di dialog dua karakter (Kaelen-Aina), reaksi non-verbal karakter yang *tidak* sedang bicara sering lebih penting secara emosional daripada karakter yang sedang bicara — rencanakan coverage reaction shot secara sengaja, bukan sebagai tambahan.
- **Depth of Field sebagai Fokus Emosional**: gunakan shallow depth of field untuk mengisolasi karakter dari environment di momen sangat personal, deep depth of field saat environment (rujuk Level_Design environmental storytelling) ikut jadi bagian penting dari maknanya.

---

## 5. Transisi Antar Cutscene dan Gameplay — Kontinuitas Teknis

- **Match-cut Posisi Kamera**: posisi dan angle kamera di akhir cutscene sebaiknya cukup dekat dengan posisi kamera gameplay default supaya transisi kembali ke kontrol pemain tidak terasa canggung/disorientasi.
- **Konsistensi Pencahayaan**: pencahayaan di cutscene (biasanya lebih dikurasi/sinematik) harus tetap dalam rentang yang masuk akal dibanding pencahayaan real-time gameplay di ruang yang sama — perbedaan drastis akan terasa seperti "dua dunia berbeda", merusak imersi.
- **State Musuh/Environment Tetap Konsisten**: kalau cutscene terjadi di tengah encounter combat, state musuh (posisi, HP, animasi) yang ditampilkan di cutscene harus sinkron dengan state gameplay yang ditinggalkan sebelum cutscene dan yang dilanjutkan sesudahnya.

---

## 6. Checklist Integrasi ke Visual Self-Review Loop

Poin tambahan untuk `Lentera_Pudar_AI_Automation_Visual_SelfReview_Protocol.md`:

1. Apakah karakteristik kamera (framing, stabilitas, pacing cut) sudah sesuai sektor grief yang dituju, bukan gaya kamera generik (bagian 2)?
2. Apakah transisi gameplay↔cutscene sudah diminimalkan hard cut-nya, dan durasi cutscene proporsional ke bobot naratif momen tersebut (bagian 3)?
3. Apakah timing cut ke close-up sudah disinkronkan ke momen AU kunci di ekspresi wajah karakter (bagian 4)?
4. Apakah posisi kamera dan pencahayaan di akhir cutscene cukup konsisten dengan gameplay yang mengikutinya untuk transisi yang mulus (bagian 5)?

---

*Dokumen ke-28 dari paket dokumentasi pra-produksi Lentera Pudar — pelengkap Kreativitas_Seni_Expert.md (prinsip sinematografi umum), menyambungkan Ekspresi_Wajah_Manusia.md dan Level_Design_Environmental_Storytelling.md ke praktik shot planning dan pacing cutscene.*

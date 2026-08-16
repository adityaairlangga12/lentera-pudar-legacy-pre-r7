# Ekspresi Wajah Manusia — Lentera Pudar
### Referensi Lengkap Anatomi Wajah, FACS, dan Bahasa Emosi untuk Animasi Karakter (Blender + UE5)

Dokumen ini melengkapi **Anatomi_Kinesiologi.md** (yang fokus ke tubuh) dan **Psikologi_Expert.md** (yang fokus ke psikologi pemain) — keduanya belum menyentuh bagaimana emosi karakter *ditampilkan secara visual lewat wajah*. Untuk Lentera Pudar yang bertema grief, wajah Kaelen dan Aina adalah salah satu alat naratif paling penting, sehingga akurasi dan nuansa di sini berpengaruh langsung ke seberapa kuat cerita tersampaikan tanpa dialog.

---

## 1. Anatomi Otot Wajah (Facial Musculature)

Berbeda dari otot tubuh yang menggerakkan tulang lewat tendon di titik-titik jauh, otot wajah kebanyakan menempel langsung ke kulit (tanpa tulang perantara) — inilah sebabnya wajah bisa membentuk ribuan variasi bentuk halus dari kombinasi otot yang relatif sedikit.

Kelompok otot utama yang perlu dipahami agent untuk rigging/blend shape:

- **Frontalis** — mengangkat alis, membentuk kerutan horizontal di dahi. Aktif pada ekspresi kejutan/ketakutan.
- **Corrugator Supercilii** — menarik alis ke bawah-dalam, membentuk kerutan vertikal di antara alis ("kerutan marah"). Kunci untuk ekspresi Anger dan konsentrasi.
- **Orbicularis Oculi** — otot melingkar di sekitar mata; bagian luarnya (*pars orbitalis*) yang berkontraksi membentuk "kerutan mata" saat senyum tulus (lihat Duchenne Marker, bagian 4).
- **Zygomaticus Major** — menarik sudut mulut ke atas-luar; otot utama senyum.
- **Levator Labii Superioris** — mengangkat bibir atas; ikut aktif pada jijik (disgust) dan sebagian ekspresi sedih tertahan.
- **Depressor Anguli Oris** — menarik sudut mulut ke bawah; otot kunci ekspresi sedih dan cemberut.
- **Mentalis** — otot dagu, mengerutkan dagu; sering aktif saat menahan tangis (relevan untuk momen Denial/Depression Aina/Kaelen).
- **Orbicularis Oris** — otot melingkar mulut; mengontrol mengatup, memoncongkan, menahan bibir.
- **Platysma** — otot leher tipis yang ikut tertarik saat ekspresi tegang/ketakutan ekstrem; sering diabaikan tapi menambah kesan "seluruh tubuh ikut merasakan", bukan cuma wajah.

**Implikasi rigging**: setiap otot di atas idealnya punya *joint/bone* atau *shape key* terpisah supaya bisa dikombinasikan secara independen — kombinasi 8-10 otot dasar ini menghasilkan ratusan variasi ekspresi tercampur (*blended emotion*) yang jauh lebih natural daripada preset "senyum/sedih/marah" yang kaku.

---

## 2. FACS — Facial Action Coding System

FACS adalah sistem standar industri (dikembangkan Paul Ekman & Wallace Friesen) yang memecah setiap ekspresi wajah menjadi kombinasi **Action Unit (AU)** — unit gerakan otot individual yang terukur dan dapat dikombinasikan.

Beberapa AU paling relevan untuk produksi:

| AU | Nama | Otot Terlibat | Relevansi Grief |
|---|---|---|---|
| AU1 | Inner Brow Raiser | Frontalis (pars medialis) | Sedih, khawatir |
| AU4 | Brow Lowerer | Corrugator Supercilii | Marah, konsentrasi, menahan emosi |
| AU6 | Cheek Raiser | Orbicularis Oculi (pars orbitalis) | Senyum tulus (Duchenne) |
| AU12 | Lip Corner Puller | Zygomaticus Major | Senyum (termasuk senyum dipaksakan) |
| AU15 | Lip Corner Depressor | Depressor Anguli Oris | Sedih, kecewa |
| AU17 | Chin Raiser | Mentalis | Menahan tangis, ragu |
| AU43 | Eyes Closed | Orbicularis Oculi (menutup) | Lelah, pasrah, menerima (Acceptance) |

**Kenapa FACS penting untuk AI agent**: alih-alih instruksi vague seperti "buat ekspresi sedih", agent bisa bekerja dengan kombinasi AU yang presisi dan dapat direplikasi konsisten antar shot — misalnya *"Denial: AU4 + AU17 (menahan, belum terima)"* vs *"Depression: AU1 + AU15 + AU43 (pasrah, redup)"*.

---

## 3. Enam Ekspresi Emosi Dasar (Ekman) dan Kombinasinya untuk 5 Sektor Grief

Riset Ekman mengidentifikasi 6 ekspresi emosi dasar yang dikenali lintas budaya: **senang, sedih, marah, takut, jijik, terkejut**. Untuk Lentera Pudar, ekspresi jarang berdiri sendiri murni — yang lebih powerful secara naratif adalah *kombinasi/transisi* antar ekspresi dasar, dipetakan ke tahapan grief:

- **Denial** — kombinasi *terkejut tertahan* (AU1+AU2 minimal) + wajah datar dipaksakan (otot mulut netral, mata tidak fokus) — kesan "belum memproses".
- **Anger** — AU4 dominan (corrugator) + AU23 (bibir mengencang) + rahang mengeras (masseter tegang, meski bukan otot ekspresi wajah "murni", visualnya penting).
- **Depression** — AU1+AU15 (sudut mulut turun, alis dalam terangkat = ekspresi sedih klasik) + AU43 parsial (mata setengah tertutup, tatapan turun) + otot wajah umum kendur (bukan hanya sedih aktif, tapi *kehabisan energi untuk berekspresi*).
- **Acceptance** — bukan senyum penuh (AU6+AU12), tapi sering *senyum parsial/tenang* (AU12 saja tanpa AU6, atau AU6 lemah) — kombinasi ambivalen ini justru lebih meyakinkan secara emosional daripada senyum penuh, karena penonton membaca "damai, bukan bahagia".
- **Reconciliation/Transisi** (jika ada tahap ke-5 di luar 4 grief klasik) — ekspresi berubah *bertahap dalam satu shot* (animasi blend antar AU secara gradual), bukan potongan tiba-tiba antar pose.

---

## 4. Duchenne Marker — Membedakan Senyum Tulus vs Dipaksakan

Salah satu penemuan paling actionable dari riset ekspresi wajah: **senyum tulus (Duchenne smile)** melibatkan AU6 (Cheek Raiser / kerutan mata) bersamaan dengan AU12 (Lip Corner Puller). **Senyum sosial/dipaksakan** hanya melibatkan AU12 tanpa AU6 — mulut tersenyum tapi mata tidak ikut "tersenyum".

**Implikasi langsung untuk Lentera Pudar**: momen Aina atau Kaelen tersenyum "demi terlihat baik-baik saja" di depan yang lain (khas fase Denial/Anger awal) harus secara sengaja *tidak* mengaktifkan AU6 — mata tetap datar/berat meski mulut tersenyum. Ini detail kecil tapi sangat mempengaruhi apakah penonton merasakan momen tersebut sebagai jujur atau sebagai topeng — sesuai tema game.

---

## 5. Asimetri dan Micro-Expression

Wajah manusia asli **tidak pernah simetris sempurna** saat berekspresi — sisi kiri dan kanan wajah bergerak dengan intensitas dan timing sedikit berbeda (dipengaruhi dominasi hemisfer otak). Rig atau blend shape yang menghasilkan ekspresi simetris sempurna di kedua sisi wajah akan terasa "boneka" atau *uncanny*, betapapun akuratnya bentuk individual tiap sisinya.

**Micro-expression** — ekspresi emosi asli yang muncul sekilas (biasanya 1/25–1/5 detik) sebelum "ditutup" oleh ekspresi yang lebih terkontrol — sangat relevan untuk momen Kaelen menahan emosi di depan Aina. Secara teknis: satu-dua frame ekspresi jujur (misal AU1+AU4 sekilas) sebelum kembali ke ekspresi netral terkontrol, jauh lebih meyakinkan daripada wajah datar penuh sepanjang shot.

**Catatan untuk AI agent**: asimetri dan micro-expression tidak perlu dihitung matematis presisi — cukup terapkan offset kecil (beberapa persen intensitas AU, beberapa frame delay) antara sisi kiri-kanan wajah dan sebelum transisi ekspresi, sebagai *default practice*, bukan kasus khusus per shot.

---

## 6. Blend Shapes / Shape Keys untuk Rig Wajah (Sisi Teknis Blender/UE5)

Mengikuti pola teknis di Anatomi_Kinesiologi.md, berikut breakdown implementasi:

- **Basis Shape Key per-AU (bukan per-emosi)**: buat shape key terpisah untuk tiap Action Unit relevan (AU1, AU4, AU6, AU12, AU15, AU17, AU43, dst.), lalu kombinasikan lewat driver/blend — bukan membuat shape key "senyum jadi" dan "sedih jadi" secara langsung. Pendekatan berbasis-AU jauh lebih fleksibel untuk ekspresi campuran dan transisi halus.
- **Corrective Shape Keys untuk kombinasi ekstrem**: seperti prinsip di dokumen Anatomi_Kinesiologi untuk deformasi sendi tubuh, kombinasi AU tertentu (misal AU4+AU1 bersamaan) butuh corrective shape key tambahan supaya area antar-alis tidak terlihat pecah/tertindih secara topologi.
- **Eye Region terpisah dari Mouth Region**: idealnya di-rig sebagai dua kelompok kontrol independen (mata bisa "sedih" sementara mulut "netral" — kombinasi yang sangat umum di ekspresi tertahan), konsisten dengan prinsip "ekspresi campuran" di bagian 3.
- **Batas rotasi/deformasi rahang**: rahang (jaw) punya rentang gerak terbatas secara anatomis (dagu tidak bisa turun sembarang jauh tanpa terlihat patah) — gunakan constraint serupa tabel "Batas Rotasi Sendi Realistis" di Anatomi_Kinesiologi, diterapkan ke jaw bone.

---

## 7. Eye Direction & Gaze sebagai Bahasa Emosi Pasif

Arah pandang mata adalah salah satu sinyal emosi paling kuat namun sering diabaikan dibanding ekspresi mulut/alis:

- **Gaze aversion (menghindari kontak mata)** — indikator kuat malu, bersalah, atau menghindari topik (relevan untuk momen Kaelen/Aina menghindari membahas kehilangan).
- **Gaze lock (menatap lama tanpa berkedip)** — intensitas emosi tinggi (marah, syok, atau momen breakthrough emosional).
- **Downward gaze + slow blink** — kombinasi klasik kesedihan/kelelahan, cocok untuk fase Depression.
- **Gaze drift (mata bergerak tanpa fokus jelas)** — melamun/dissociation, cocok untuk momen Denial di mana karakter "hadir secara fisik tapi tidak secara mental".

**Implikasi teknis**: sistem eye-tracking/look-at di rig sebaiknya punya parameter terpisah untuk *target fokus* dan *durasi hold sebelum shift* — bukan hanya on/off menatap sesuatu. Durasi dan pola pergerakan mata itu sendiri yang membawa makna emosional, bukan cuma arah akhirnya.

---

## 8. Checklist Integrasi ke Visual Self-Review Loop

Poin tambahan yang bisa disambungkan ke `Lentera_Pudar_AI_Automation_Visual_SelfReview_Protocol.md`:

1. Apakah ekspresi menggunakan kombinasi AU yang sesuai tahap grief yang dituju (bagian 3), bukan preset emosi tunggal?
2. Kalau ada senyum, apakah AU6 (kerutan mata) sengaja diaktifkan/dinonaktifkan sesuai apakah senyum itu tulus atau topeng (bagian 4)?
3. Apakah ada asimetri kecil kiri-kanan wajah, bukan simetri sempurna (bagian 5)?
4. Apakah arah dan durasi gaze mata sudah selaras dengan emosi yang ingin disampaikan, bukan default menatap kamera/lawan bicara terus-menerus (bagian 7)?
5. Untuk shot transisi emosi (misal Denial → Anger), apakah perubahan AU terjadi bertahap dalam beberapa frame, bukan potongan tiba-tiba (bagian 3)?

---

*Dokumen ke-24 dari paket dokumentasi pra-produksi Lentera Pudar — pelengkap Anatomi_Kinesiologi.md (tubuh) dan Psikologi_Expert.md (psikologi pemain), khusus untuk anatomi dan bahasa ekspresi wajah karakter.*

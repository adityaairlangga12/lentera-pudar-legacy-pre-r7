# Moodboard Referensi — Lentera Pudar
### Artstyle: Kena: Bridge of Spirits | Mekanik: Hellblade: Senua's Sacrifice & Hellblade II: Senua's Saga

---

## 1. Pembagian Peran Dua Referensi

Dua game ini dipakai untuk dua lapisan berbeda, tidak tumpang tindih:

- **Kena: Bridge of Spirits** → menentukan **bagaimana dunia terlihat** (artstyle, palet warna, pencahayaan, desain karakter/environment).
- **Hellblade (Senua's Sacrifice & Hellblade II)** → menentukan **bagaimana dunia terasa saat dimainkan** (sistem gameplay, psikologi, combat, audio).

Pendekatan ini menjaga "Lentera Pudar" tidak jadi campuran tanpa arah — visualnya tetap hangat-dongeng ala Kena, tapi bobot emosional dan tekanan gameplay-nya terasa berat ala Hellblade.

---

## 2. Artstyle: Kena: Bridge of Spirits

| Elemen Kena | Ciri Khasnya | Adaptasi untuk Lentera Pudar |
|---|---|---|
| **Palet warna hangat vs dingin yang tajam** | Area yang sudah "dibersihkan" terasa hidup, hijau, dan cerah; area Rot/Corruption gelap, biru pekat, mati | Kontras 2700K (cahaya syal Aina) vs 6500K (kristal es kutukan) yang sudah ada di GDD — pertajam lagi lewat pewarnaan environment: sektor yang sudah dilalui Kaelen mendapat rona hangat samar, sektor yang belum tersentuh tetap biru pudar total |
| **Gaya karakter stylized-realistic** (proporsi semi-realistis tapi dengan siluet bersih, bukan super-deformed) | Karakter terasa "hidup" secara emosional tanpa jatuh ke gaya kartun murni | Cocok langsung untuk desain Kaelen & Aina — pertahankan siluet bersih (jubah gelap Kaelen, syal kuning tebal Aina) dengan detail wajah/ekspresi yang tetap ekspresif, bukan minim detail |
| **Makhluk kecil pendukung (Rot)** yang jadi elemen visual sekaligus gameplay ambient | Rot membentuk pola, membantu puzzle ringan, dan jadi indikator visual area yang "hidup kembali" | Bisa diadaptasi jadi **kunang-kunang/partikel kecil dari nyala syal Aina** yang menyebar di area gelap — bukan cuma dekorasi Niagara Particle, tapi indikator visual seberapa jauh area sudah "dihangatkan" |
| **Desain environment natural-organik** dipadu elemen arsitektur kuno yang runtuh | Reruntuhan candi/istana ditumbuhi elemen alam, kesan waktu yang berlalu lama | Selaras dengan estetika *The Silent Crypts* dan *Hall of Mirrors* di GDD — reruntuhan kerajaan beku yang mulai "retak" oleh kehangatan syal saat Kaelen lewat |
| **Pencahayaan Lumen-style dengan sumber cahaya kecil yang sangat kontras terhadap gelap sekitarnya** | Cahaya jadi elemen naratif, bukan sekadar penerangan teknis | Cahaya syal Aina (2700K) sebagai satu-satunya sumber hangat di tengah dungeon biru — jaga rasio kontras setinggi mungkin, mirip cara Kena memperlakukan sumber cahaya di area Rot |

**Catatan produksi**: karena Kena dibangun di Unreal Engine dengan Nanite/Lumen-friendly asset, referensi teknis pipeline artstyle-nya (topology karakter, cara handle cloth/foliage) cukup relevan langsung untuk pipeline Blender 5.2 LTS → UE5 yang kamu pakai.

---

## 3. Mekanik: Hellblade (Senua's Sacrifice & Hellblade II)

Hellblade dibangun di atas satu prinsip: **kondisi psikologis karakter BUKAN cuma narasi, tapi sistem gameplay itu sendiri.** Tidak ada UI health bar konvensional yang mendominasi layar, tidak ada "game over" klise — semua diterjemahkan jadi perubahan environment, suara, dan visual langsung di dunia game. Hellblade II memperdalam ini lagi dengan combat yang lebih sinematik dan set-piece environment yang berubah bentuk mengikuti kondisi mental Senua.

| Mekanik Hellblade | Sumber (1/2) | Adaptasi untuk Lentera Pudar |
|---|---|---|
| **The Darkness** (bayangan merambat di lengan Senua, membesar tiap kali "kalah") | Senua's Sacrifice | **Curse Meter jadi rambatan es visual di lengan kiri Kaelen.** Tiap kali gagal dodge / kena hit berat, kristal es merambat dari siku ke bahu. Terlihat sepanjang sesi, bukan cuma bar UI |
| **Permadeath Illusion** (ancaman karakter "hancur" jika berulang kali gagal — sebenarnya scripted) | Senua's Sacrifice | Adaptasi jadi ancaman **"Kaelen membeku total"** — pemain diberi ilusi reset progress kalau Curse Meter penuh 3x, padahal sebenarnya hanya memicu cutscene naratif pendek soal ketakutan Kaelen sendiri |
| **Binaural Audio & Voices (bisikan di kedua telinga yang meragukan keputusan pemain)** | Senua's Sacrifice & II | Bisikan dari **jiwa yang sudah membeku** di sekitar dungeon — membujuk Kaelen untuk berhenti, "menjadi es saja, lebih tenang". Makin dekat boss sektor, bisikan makin intens |
| **Environmental Puzzle via Perception** (mencari simbol tersembunyi lewat sudut pandang tertentu) | Senua's Sacrifice | Kaelen memakai **Eyepatch** sebagai mekanik: buka sesaat untuk melihat "dunia beku" versi lain (viewpoint alternatif), mengungkap jalur tersembunyi tiap sektor — selaras lore mata kanannya yang tersegel |
| **Combat 1v1 fokus, berat di timing & parry, minim button-mashing** | Senua's Sacrifice | Basis combat Kaelen (Light/Heavy/Evade) tetap simpel di root, tambahkan **parry window sempit** untuk momen penting, terutama vs boss |
| **Set-piece environment yang berubah bentuk real-time mengikuti kondisi mental karakter** (bukan sekadar loading area baru) | Hellblade II | Sektor dungeon bisa **berubah struktur secara live** sesuai Curse Meter Kaelen — misal lorong di *Abyss of Stillness* memanjang/menyempit, dinding es merekah membentuk wajah, tanpa transisi loading terlihat |
| **Motion-captured performance & close-camera storytelling** (kamera dekat ke wajah saat momen emosional kunci) | Hellblade II | Untuk cutscene Altar Duka (titik syal Aina memendek), gunakan kamera dekat ala Hellblade II — fokus ke ekspresi Kaelen, bukan wide shot sinematik biasa, supaya beban emosional tiap pengorbanan terasa personal |
| **Face-off Boss** (representasi trauma, bukan sekadar damage sponge) | Senua's Sacrifice & II | Kelima boss sektor didesain sebagai **cerminan tahap grief itu sendiri** — manifestasi emosi Kaelen sendiri, sama seperti pola The Hollow Reflection yang sudah ada di GDD, diperluas ke seluruh boss |
| **Sound-guided/minimal-HUD navigation** | Senua's Sacrifice & II | Syal Aina jadi "kompas emosional" — bersinar/berdenyut mengikuti detak jantung, memberi arah tanpa minimap konvensional |

---

## 4. Ringkasan Pembagian Bobot

- **Kena** → 100% acuan visual: warna, cahaya, siluet karakter, desain environment organik-reruntuhan.
- **Hellblade 1 & 2** → 100% acuan sistem: Curse Meter sebagai Darkness, audio psikologis, kamera dekat saat momen emosional, boss sebagai cerminan trauma, environment yang responsif terhadap kondisi mental karakter.

Dengan pembagian ini, tim art bisa mengacu murni ke Kena tanpa bingung mekanik, dan tim gameplay/programming bisa mengacu murni ke Hellblade tanpa perlu menyesuaikan gaya visual yang berbeda.

---

*Dokumen ini adalah moodboard referensi, bukan spesifikasi teknis final. Cocok dipakai sebagai lampiran pendamping GDD utama.*

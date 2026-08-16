# Dokumen 33 — Skenario & Naskah Step-by-Step Tutorial Prolog Onboarding

**Proyek:** Lentera Pudar  
**Kategori:** Fondasi & Lore / Game Design / Level Design  
**Status:** Melengkapi gap "Skenario/Naskah Tutorial Prolog" — pelengkap dari Level as Tutorial, Onboarding Encounter, UI/UX Aksesibilitas, dan Sistem Respawn Diegetik  

---

## 0. Prinsip Desain Onboarding Diegetik

Sesuai filosofi semesta *Lentera Pudar*, alur tutorial prolog dirancang tanpa pop-up teks panjang:
1. **Teaching Through Geometry & Light**: Arsitektur ruang, pencahayaan syal Aina 2700K, dan kontras visual membimbing naluri pemain.
2. **Contextual & Fleeting Glyph Assist**: Petunjuk tombol (glyph) hanya muncul lembut pada radius $<2.0\text{ m}$ saat interaksi pertama, dan hilang permanen setelah berhasil.
3. **Organic Fail-Safe**: Jika pemain ragu/gagal, dunia memberi isyarat diegetik berulang (kibasan kain, pendaran es, bisikan binaural) tanpa layar kegagalan buatan.

---

## 1. Peta 6 Langkah Pembelajaran Mekanik Prolog

```
Step 1: Gerak Dasar & Cahaya Syal ➔ Ceruk Makam Gelap Gulita
Step 2: Light Punch (Tinju Kanan) ➔ Celah Runtuhan Es Rapuh
Step 3: Heavy Cursed Ice Strike  ➔ Gerbang Segel Es Tebal (+10 Curse Meter)
Step 4: 12-Frame Tight Parry     ➔ Arena Koridor 1v1 Terkontrol (The Echo)
Step 5: The Sealed Eyepatch      ➔ Tebing Jurang Kering Buntu (+3 Curse/s)
Step 6: Interaksi Altar Duka 1   ➔ Ruang Altar Gerbang Sektor 1 (Syal Memendek)
```

---

## 2. Naskah Walkthrough Langkah-demi-Langkah

### A. Langkah 1: Gerak Dasar & Cahaya Syal (*The Awakening & Living Light*)
- **Setting**: Ceruk Makam Sempit (*Crypt Alcove*), gelap gulita (`#141013`). Satu-satunya cahaya berasal dari Syal Aina (`#F4B860` 2700K).
- **Trigger**: Kamera membuka dari sudut pandang Kaelen lalu transisi seamless mundur ke Over-Shoulder Third-Person. Syal Aina berdenyut lembut dan ujungnya berkibar menunjuk ke celah lorong.
- **Aksi**: Menggerakkan tuas analog kiri / `WASD` untuk melangkah keluar.
- **Fail-Safe**: Jika diam $>5$ detik, syal berdenyut lebih terang (+20% Lumen) dan bisikan Aina berdesir (*"Kaelen... mari berjalan..."*). Glyph stik kiri muncul samar dan memudar saat pemain melangkah.

---

### B. Langkah 2: Light Punch — Tinju Tangan Kanan (*The Bandaged Fist*)
- **Setting**: Lorong sempit terhalang susunan stalagmit kristal es rapuh dan balok kayu lapuk.
- **Trigger**: Kaelen mendekati penghalang ($<1.5\text{ m}$). Jalur buntu secara fisik.
- **Aksi**: Menekan tombol **Light Attack** (`Square` / `X` / `LMB`). Kaelen melancarkan kombo tinju 1–2 hit perban. Kristal es rapuh pecah dengan jeda *hit-stop 3 frame*.
- **Fail-Safe**: Jika hanya menabrak tanpa memukul, permukaan es memancarkan retakan bercahaya dan glyph tombol Light Attack muncul samar selama 3 detik.

---

### C. Langkah 3: Heavy Cursed Strike & Curse Feedback (*The Cursed Talons & Trade-Off*)
- **Setting**: Gerbang lengkung batu tertutup lempengan kristal es tebal biru keunguan (`#4A6FA5`).
- **Trigger**: Light Attack memantul dengan suara benturan tumpul. Lengan kiri es Kaelen bergetar halus (*haptic pulse*) dan pendaran kristal sikunya menyala biru 6500K.
- **Aksi**: Menahan tombol **Heavy Attack** (`Triangle` / `Y` / `RMB`). Kaelen menghantamkan cakar es tangan kiri. Lempengan es tebal meledak hancur.
- **Umpan Balik Diegetik**: Es merambat dari siku ke bahu Kaelen, *Curse Meter* naik $+10\text{ poin}$, layar mengalami *frost vignette* mikro sesaat.
- **Fail-Safe**: Jika memukul ringan berkali-kali tanpa hasil, bisikan jiwa es berdesir (*"Gunakan kutukanmu..."*) dan kristal siku berpendar lebih terang.

---

### D. Langkah 4: 12-Frame Tight Parry Timing (*The First Fallen Shade 1v1*)
- **Setting**: Ruang makam segi empat luas berlantai batu datar (*The Solitary Duelling Hall*). Satu musuh jiwa beku (*The Echo*) bangkit dari es.
- **Trigger**: Pintu belakang tertutup jeruji es sementara (arena terkunci 1v1). Kamera masuk ke *Duel Lock-On* (FOV 70°). Musuh menyiapkan ayunan pedang es dengan windup lambat (18 frame, kilau biru tajam).
- **Aksi**: Menekan tombol **Parry / Block** (`L1` / `LB` / `Q`) tepat pada jendela 12 frame.
  - *Sukses*: Jeda *hit-stop 3 frame*, bunga api emas Aina (`#F4B860`) memancar, musuh terlempar ke *Full Stagger Window* 3 detik. Kaelen menghabisi musuh dengan 1 pukulan penutup, jeruji es terbuka.
- **Fail-Safe**: Jika gagal, Kaelen hanya menerima 10% damage dengan jeda recovery musuh 2 detik. Jika tumbang, Kaelen respawn instan di ambang pintu (*ADR-035*) dan mengulang windup lambat yang sama.

---

### E. Langkah 5: Buka Eyepatch Perception (*The Sealed Eye & The Spectral Path*)
- **Setting**: Tebing terputus di atas jurang es tanpa jembatan fisik (*The Blind Chasm*).
- **Trigger**: Kaelen tiba di tepi jurang. Simbol mata es terukir di pilar batu. Kamera melakukan *Dutch tilt* mikro dan bisikan binaural berdesir (*"Buka matamu yang terkunci..."*).
- **Aksi**: Menahan tombol **Sealed Eye** (`R3` / `Hold E`). Kaelen membuka penutup mata kulit hitamnya sesaat.
  - *Efek*: Layar desaturasi dingin bertepi kristal es, jembatan memori kristal biru transparan berpendar memperlihatkan jalur kokoh di atas jurang. *Curse Meter* naik $+3\text{ poin/detik}$.
- **Fail-Safe**: Jika diam di tepi jurang $>6$ detik, bekas luka mata kanan Kaelen berdenyut biru menembus kain penutup mata dengan getaran haptik berulang.

---

### F. Langkah 6: Interaksi Altar Duka Pertama (*The First Sacrifice & Stage-Gate 0*)
- **Setting**: Ruang Altar Penyangkalan (*The Threshold Sanctuary*). Altar Duka kuno diselimuti es abadi di depan Gerbang Raksasa Sektor 1.
- **Trigger**: Kaelen tiba di pelataran altar. Syal Aina berdenyut kencang 2700K mengarah ke mangkuk altar. Glyph `Interact` (`X` / `A` / `F`) muncul lembut pada jarak $<2.0\text{ m}$.
- **Aksi**: Menekan tombol **Interact**.
  - *Cutscene Diegetik*: Kaelen meletakkan tangan di altar. Syal Aina memancarkan api emas mencairkan segel es altar.
  - *Pengorbanan Tahap 1*: Syal Aina memendek secara permanen dari **Panjang ke Sedang**.
  - *Unlock Kemampuan*: Membuka resmi **Retakan Penyangkalan (*Fracture of Denial*)** (`GA_ShatterStrike`).
  - *Curse Reset*: Curse Meter bersih menjadi 0%, Gerbang Sektor 1 *The Silent Crypts* terbuka perlahan.
- **Transisi Gameplay**: Auto-Save Permanen tersimpan, kontrol bebas aktif, Kaelen melangkah masuk ke Sektor 1.

---

## 3. Matriks Checklist Kepatuhan Sistem

- [ ] Seluruh transisi berlangsung seamless tanpa loading screen atau instruksi teks buatan.
- [ ] Jendela parry terkalibrasi presisi pada 12 frame (0.2s @60fps) dengan hit-stop 3 frame.
- [ ] Efek es merambat dan Sealed Eye terhubung langsung ke MPC Curse Meter di Unreal Engine 5.
- [ ] Pengorbanan syal memicu deformasi skeletal mesh syal secara permanen dan menyimpan save-point.

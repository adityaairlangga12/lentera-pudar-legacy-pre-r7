# Game Design Document (GDD) — Lentera Pudar

Dokumen ini adalah sumber kebenaran desain game (*Game Design Source of Truth*) untuk mekanik, loop gameplay, narasi, dan perancangan level proyek **Lentera Pudar**.

---

## 1. Identitas & Pilar Game

- **Judul**: Lentera Pudar
- **Genre**: 2D Pixel Action RPG / Dungeon Crawler Top-Down
- **Target Platform**: PC Windows (Kontrol: Keyboard + Mouse)
- **Engine**: Godot 4.7.1 (Renderer: Compatibility)
- **Nuansa Atmosferik**: *Misterius-Hangat* (Kontras tajam antara kehangatan lentera dan dinginnya es kutukan).

### Tiga Pilar Pengalaman Pemain (Core Pillars):
1. **The Triad Dynamic**: Kegelapan dungeon (`#2A211C`) adalah ancaman konstan. Kehangatan syal lentera (`#F4B860`) adalah sumber keselamatan dan harapan. Kutukan Pudar (`#4A6FA5`) adalah bahaya biologis/magis yang perlahan menggerogoti jiwa.
2. **Tactical Lighting Navigation**: Cahaya bukan sekadar visual, melainkan mekanik interaktif untuk mengaktifkan mekanisme kuno, mencairkan pintu es, dan melemahkan musuh beku.
3. **Responsive 8-Way Combat**: Pergerakan 8-arah yang presisi, sistem *dash/dodge* responsif dengan *input buffering*, dan serangan terarah.

---

## 2. Protagonis & Mekanik Inti

### Profil Protagonis
- Karakter tunggal tanpa kelas (*Class-less*), berambut abu-abu acak, berpakaian kelana gelap.
- **Syal Lentera**: Memancarkan cahaya dinamis radius 150-200px via `PointLight2D`.
- **Tangan Kutukan Pudar**: Tangan kiri dibalut perban yang memancarkan urat es biru berdenyut (`CursedHand.gdshader`).

### Sistem Pengukur Kutukan (Curse Gauge System)
- **Mekanik Pengukur**: Nilai `curse_level` (0.0 s/d 1.0).
  - Di kegelapan total (di luar radius cahaya): `curse_level` perlahan meningkat (+2% per detik).
  - Di dekat sumber cahaya statis (Altar/Obor): `curse_level` perlahan menurun / pulih.
- **Dampak Kutukan**:
  - `0% - 50%`: Normal. Urat es di tangan kiri berdenyut lambat.
  - `51% - 80%`: Denyut shader semakin cepat. Karakter mendapatkan bonus *cold damage* tetapi stamina regen melambat 20%.
  - `81% - 100%`: Layar bergetar (*vignette frost* membeku di tepi layar). Jika mencapai 100%, karakter membeku (*Stun / Game Over*).

---

## 3. Loop Gameplay Utama (Core Gameplay Loop)

```
[Ruang Aman / Checkpoint] 
         │
         ▼
[Eksplorasi Ruang Gelap] ──► [Manajemen Radius Cahaya & Curse Meter]
         │
         ▼
[Encounter Musuh Beku] ──► [Kombat Taktis & Penghindaran Dash]
         │
         ▼
[Nyalakan Altar / Obor Kunci] ──► [Zona Aman Baru Terbentuk]
         │
         ▼
[Pecahkan Teka-Teki / Buka Pintu Es] ──► [Akses ke Ruang Boss / Sektor Berikutnya]
```

---

## 4. Rencana Sektor 1: Reruntuhan Kristal Beku (Frozen Crystal Ruins)

### Lingkungan (Environment)
- Lantai batu dungeon gelap berlumut beku.
- Dinding kristal es biru pudar yang memantulkan kilauan cahaya lentera.
- Obor dinding kuno berbahan bakar minyak lentera.

### Arketipe Musuh Pertama
1. **Husk Beku (Frozen Husk)**:
   - Korban Kutukan Pudar yang telah membeku menjadi patung hidup.
   - Bergerak lambat, serangan tebasan es jarak dekat dengan *wind-up* telegraf yang jelas.
   - Lemah terhadap serangan saat tersorot langsung oleh cahaya lentera.
2. **Percikan Jiwa Beku (Ice Wisp)**:
   - Serpihan energi es yang melayang cepat secara zig-zag.
   - Menembakkan proyektil es kecil dan mencoba memadamkan obor dinding.

---

## 5. Skema Kontrol Keyboard PC

| Aksi | Tombol Keyboard | Deskripsi |
|---|---|---|
| **Pergerakan 8-Arah** | `W, A, S, D` / `Tombol Panah` | Bergerak ke 8 arah mata angin kardinal. |
| **Dash / Menghindar** | `Space` / `Shift` | Manuver gesit berdurasi singkat dengan *invulnerability frames*. |
| **Serangan Utama** *(Persiapan)* | `Klik Kiri` / `J` | Ayunan senjata/serangan jarak dekat. |
| **Interaksi / Nyalakan Lentera** | `E` / `F` | Berinteraksi dengan altar, peti, pintu, atau NPC. |

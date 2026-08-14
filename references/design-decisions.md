# Design Decisions Log — Lentera Pudar

Dokumen ini mencatat seluruh keputusan arsitektur struktural, desain game, dan pilihan teknis berbiaya tinggi (*Architecture Decision Records*). Tujuannya agar keputusan di masa lalu memiliki konteks jelas dan tidak didebat ulang dari nol.

---

## Log Keputusan yang Sudah Ditetapkan

### ADR-001: Model Rendering 8-Arah Murni (True 8-Way via Pixellab v3)
- **Tanggal**: 2026-08-13
- **Status**: Accepted
- **Konteks**: Karakter utama memiliki desain asimetris: tangan kiri dibalut perban dengan urat es biru (Kutukan Pudar), sedangkan tangan kanan normal.
- **Keputusan Terpilih**: **True 8-Way (8 Arah Sejati)**.
- **Dampak**: Menjaga integritas lore asimetri tangan kutukan saat karakter bergerak ke arah kiri (`west`, `north-west`, `south-west`).

### ADR-002: Arsitektur Komunikasi Global Event Bus (GameEvents.gd)
- **Tanggal**: 2026-08-13
- **Status**: Accepted
- **Konteks**: Komunikasi antar node di Godot rawan spaghetti code jika menggunakan direct tree querying.
- **Keputusan Terpilih**: Seluruh interaksi lintas sistem wajib disalurkan melalui Autoload `GameEvents.gd`.
- **Dampak**: Node modular, decoupled, dan dapat diuji secara independen.

### ADR-003: Pipeline Visual Otomatis Berbasis Prompt
- **Tanggal**: 2026-08-13
- **Status**: Accepted
- **Konteks**: Memaksimalkan kecepatan produksi tanpa mengorbankan kualitas pixel art 32x32 dan kepatuhan lore.
- **Keputusan Terpilih**: Alur 3 tahap: Pixellab v3 ➔ Aseprite Lua Slicing/Tagging ➔ Godot SpriteFrames.
- **Dampak**: Otomasi tinggi dengan verifikasi kontrol kualitas (QC) di tiap tahap handoff.

### ADR-004: Arsitektur Narasi Berbasis 5 Tahap Berduka (5 Stages of Grief)
- **Tanggal**: 2026-08-14
- **Status**: Accepted
- **Konteks**: Mencegah alur cerita RPG terasa monoton atau berulang dengan menyematkan struktur psikologis mendalam di setiap sektor dungeon.
- **Keputusan Terpilih**: 5 Sektor Dungeon memetakan Kübler-Ross Model (Sektor 1: Denial - Lord Alden, Sektor 2: Anger - Ignis Vulkan, Sektor 3: Bargaining - Lady Vespera, Sektor 4: Depression - The Hollow Reflection, Sektor 5: Acceptance - The Frost Sovereign & Fajar Terakhir).
- **Dampak**: Setiap bos dan lingkungan memiliki resonansi tematik yang terhubung langsung dengan perkembangan psikologis pemain dan protagonis.

### ADR-005: Mekanik Karakter Dualitas (The Fading Scarf & Temptation of Frost)
- **Tanggal**: 2026-08-14
- **Status**: Accepted
- **Konteks**: Menghubungkan narasi Kaelen & Aina langsung ke elemen visual dan gameplay.
- **Keputusan Terpilih**: 
  1. *The Fading Scarf*: Syal kuning Aina memendek secara visual seiring berjalannya progres cerita.
  2. *The Temptation of Frost*: Bertarung di kegelapan membuat serangan tangan kiri es semakin mematikan tetapi berisiko membeku (*Game Over*).
- **Dampak**: Pemain merasakan bobot pengorbanan Aina dan godaan kekuatan keputusasaan secara konstan.

### ADR-006: Visi Skalabilitas Franchise (Lentera Pudar Expanded Universe)
- **Tanggal**: 2026-08-14
- **Status**: Accepted
- **Konteks**: Membangun fondasi semesta yang mampu menampung sekuel (Lentera Pudar 2: The Frozen Horizon & Lentera Pudar 3: The Sovereign of Dawn).
- **Keputusan Terpilih**: Game 1 berfokus pada penyembuhan duka pribadi di dungeon bawah tanah dan berakhir dengan terbukanya gerbang ke Benua Luar (*Overworld* beku).
- **Dampak**: Lore skala besar tetap konsisten dan tidak perlu di-retcon saat mengembangkan sekuel di masa depan.

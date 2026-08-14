# Design Decisions Log — Lentera Pudar

Dokumen ini mencatat seluruh keputusan arsitektur struktural, desain game, dan pilihan teknis berbiaya tinggi (*Architecture Decision Records*). Tujuannya agar keputusan di masa lalu memiliki konteks jelas dan tidak didebat ulang dari nol.

---

## Format Pencatatan Keputusan Baru (ADR Template)

```markdown
### ADR-XXX: [Judul Keputusan]
- **Tanggal**: YYYY-MM-DD
- **Status**: [Proposed / Accepted / Superseded]
- **Konteks**: Mengapa keputusan ini perlu diambil? Masalah apa yang sedang dihadapi?
- **Pilihan Pendekatan**:
  1. Opsi A: ... (Trade-off: ...)
  2. Opsi B: ... (Trade-off: ...)
- **Keputusan Terpilih**: Opsi mana yang dipilih dan alasannya.
- **Dampak / Konsekuensi**: Apa implikasinya terhadap arsitektur dan workflow ke depan?
```

---

## Log Keputusan yang Sudah Ditetapkan

### ADR-001: Model Rendering 8-Arah Murni (True 8-Way via Pixellab v3)
- **Tanggal**: 2026-08-13
- **Status**: Accepted
- **Konteks**: Karakter utama memiliki desain asimetris: tangan kiri dibalut perban dengan urat es biru (Kutukan Pudar), sedangkan tangan kanan normal.
- **Pilihan Pendekatan**:
  1. Opsi A (Flip 4-Way): Hanya merender 4 arah (S, E, N, SE) lalu me-flip secara horizontal untuk W, SW, NW.
  2. Opsi B (True 8-Way): Merender ke-8 arah secara independen via Pixellab mode v3.
- **Keputusan Terpilih**: **Opsi B (True 8-Way)**.
- **Dampak / Konsekuensi**: Menjaga integritas lore asimetri tangan kutukan saat karakter bergerak ke arah kiri (`west`, `north-west`, `south-west`). Membutuhkan 8 file `.aseprite` terpisah per karakter dan penamaan tag cardinal yang konsisten.

### ADR-002: Arsitektur Komunikasi Global Event Bus (GameEvents.gd)
- **Tanggal**: 2026-08-13
- **Status**: Accepted
- **Konteks**: Komunikasi antar node (Player, UI, Lighting, Enemy, Audio) di Godot rawan spaghetti code jika menggunakan `get_node("../Player")` atau direct tree querying.
- **Keputusan Terpilih**: Seluruh interaksi lintas domain wajib disalurkan melalui Autoload `GameEvents.gd`. Node memancarkan sinyal ke `GameEvents` dan node lain yang berkepentingan berlangganan (*subscribe*) pada sinyal tersebut.
- **Dampak / Konsekuensi**: Node modular, dapat diuji secara independen tanpa bergantung pada hierarki scene tertentu.

### ADR-003: Pipeline Visual Otomatis Berbasis Prompt (Prompt-Driven Automation)
- **Tanggal**: 2026-08-13
- **Status**: Accepted
- **Konteks**: Memaksimalkan kecepatan produksi tanpa mengorbankan kualitas pixel art 32x32 dan kepatuhan lore.
- **Keputusan Terpilih**: Alur kerja 3 tahap terintegrasi: Pixellab (Prompt Generation v3) → Aseprite (Slicing, Tagging, Palette Quantization) → Godot (Aseprite Wizard / Custom Builder + Shader + Lighting).
- **Dampak / Konsekuensi**: Otomasi tinggi dengan batas kontrol kualitas (QC) yang ketat di tiap gerbang handoff.

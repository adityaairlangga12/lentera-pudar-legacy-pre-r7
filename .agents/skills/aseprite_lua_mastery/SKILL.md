---
name: aseprite_lua_mastery
description: Pustaka memori untuk Aseprite Lua API. Berisi skrip otomasi mutlak untuk memanipulasi layer, menambahkan tag animasi, dan melakukan trim kanvas.
---

# Aseprite Lua Automation Mastery

Skill ini memastikan AI tidak perlu menebak-nebak sintaks saat diminta untuk membersihkan atau menyiapkan aset *pixel art* secara otomatis di Aseprite. Jangan lakukan perubahan manual! Selalu gunakan `run_lua_script` dengan kerangka kerja di bawah ini.

## 1. Menambahkan Tag Animasi (Animation Tags)
Tag animasi (seperti `idle`, `walk`) sangat krusial agar Aseprite Wizard di Godot dapat membedakan animasi.
```lua
local spr = app.activeSprite
if spr then
    -- Membuat tag dari frame 1 ke 4 bernama "idle"
    local tag = spr:newTag(1, 4)
    tag.name = "idle"
    tag.color = app.pixelColor.rgba(255, 0, 0, 255) -- Merah
    tag.aniDir = AniDir.FORWARD
end
app.refresh()
```

## 2. Trimming Kanvas (Auto-Crop)
Membersihkan area transparan agar ukuran kanvas efisien sebelum dikirim ke Godot.
Gunakan perintah `app.command.Trim()` bawaan Aseprite, bukan loop manual piksel.
```lua
-- Memotong seluruh sprite berdasarkan area yang memiliki piksel (membuang ruang kosong)
app.command.Trim()
app.refresh()
```

## 3. Manipulasi Layer
Cara standar untuk menyembunyikan atau mengunci *layer* sketsa/*blueprint*.
```lua
local spr = app.activeSprite
for i, layer in ipairs(spr.layers) do
    if layer.name == "Blueprint" then
        layer.isVisible = false
        layer.isEditable = false
    end
end
app.refresh()
```

## 4. Standar Ekspor ke Godot & Jebakan Warna (Washed Out)
**Ingat**: Untuk proyek Lentera Pudar, kita HANYA menyimpan file sebagai `.aseprite` (`app.command.SaveAs { filename="res://Assets/Sprites/Hero.aseprite" }`) karena Godot akan menggunakan Aseprite Wizard. Kita **TIDAK** menggunakan `ExportSpriteSheet` ke PNG.
- **Jebakan Warna Pudar**: Jika warna di Aseprite terlihat cerah tapi saat masuk ke Godot menjadi pucat/pudar (*washed out*), itu karena masalah *Color Profile*.
- **Solusi**: Pastikan di Aseprite (`Edit > Preferences > Color`) disetel ke **sRGB**. Jangan gunakan profil warna bawaan monitor, karena Godot tidak akan bisa membacanya dengan benar.

## 5. Manipulasi Palet Dinamis (Indexed Color Mode)
Untuk mengubah warna secara global (misal: Protagonis mendapat efek racun), pastikan sprite dalam mode *Indexed*.
```lua
local spr = app.activeSprite
if spr.colorMode == ColorMode.INDEXED then
    app.transaction(function()
        local pal = spr.palettes[1]
        -- Mengubah warna index ke-1 menjadi Hijau Racun
        pal:setColor(1, Color(0, 255, 0))
    end)
    app.refresh()
end
```
Wajib menggunakan `app.transaction` agar perubahan bisa di- *Undo* oleh pengguna.

## 6. Efek Visual (Blend Modes & Cel Copy)
Untuk memvisualisasikan sihir/cahaya langsung di Aseprite sebelum dikirim ke Godot, gunakan `BlendMode` pada *Layer*.
```lua
local layer = app.activeLayer
layer.blendMode = BlendMode.SCREEN -- Atau BlendMode.ADD untuk efek cahaya
layer.opacity = 180 -- Transparansi 0-255
```
Untuk menyalin gambar dari satu cel ke cel di *frame* lain:
```lua
sprite:newCel(targetLayer, targetFrame, sourceCel.image, sourceCel.position)
```

## 7. Custom UI & Otomasi Tingkat Lanjut (Final Boss)
Jika kita membutuhkan *tools* khusus untuk Lentera Pudar di dalam Aseprite, AI wajib menggunakan `Dialog` API.
```lua
local dlg = Dialog("Lentera Tools")
dlg:button{ text="Generate Variations", onclick=function() 
    -- Panggil logika otomatis di sini
end }
-- Menjalankan UI di latar belakang tanpa membuat Aseprite macet
dlg:show{ wait=false } 
```
- **Timers**: Aseprite tidak memiliki "Event Listener" global. Untuk mengecek sesuatu setiap detik, gunakan `Timer`.
```lua
local timer = Timer{ delay = 1.0, onTick = function()
    -- Lakukan background check
end }
timer:start()
```

## 8. Jebakan Batch Processing (Memory Leaks di CLI)
Jika kita harus memproses ratusan *sprite* secara otomatis menggunakan Aseprite CLI (Command Line), **JANGAN** menggunakan *looping* Bash/PowerShell yang memanggil Aseprite berulang kali. Ini akan menyebabkan RAM komputer penuh dan *crash* (*Bad Allocation*).
- **Solusi Mutlak**: Tulis satu *script* Lua (`batch.lua`) yang melakukan *looping* membaca direktori di dalam Aseprite, lalu jalankan sekali saja via CLI: `aseprite -b -script batch.lua`. Ini menjaga penggunaan memori tetap stabil.

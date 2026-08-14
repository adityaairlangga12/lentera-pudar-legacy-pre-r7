local directions = {"south", "north", "east", "west", "south-east", "south-west", "north-east", "north-west"}
local outPath = "D:/GodotProjects/Lentera-Pudar/Assets/Sprites/Characters/Protagonist/"
local report = {}

for _, dir in ipairs(directions) do
    local filePath = outPath .. "protagonist_" .. dir .. ".aseprite"
    local success, spr = pcall(function() return app.open(filePath) end)
    
    if success and spr then
        local numFrames = #spr.frames
        local tags = {}
        for _, tag in ipairs(spr.tags) do
            table.insert(tags, tag.name .. "(" .. tag.fromFrame.frameNumber .. "-" .. tag.toFrame.frameNumber .. ")")
        end
        
        -- Memeriksa apakah gambar kosong dengan mengecek cel pertama
        local celStatus = "Cel Valid"
        if spr.cels[1] == nil or spr.cels[1].image == nil then
            celStatus = "CEL KOSONG!"
        end
        
        table.insert(report, string.format("%-12s : %d Frames | Tags: %-25s | Status: %s", dir, numFrames, table.concat(tags, ", "), celStatus))
        spr:close()
    else
        table.insert(report, string.format("%-12s : GAGAL DIBUKA", dir))
    end
end

local f = io.open("D:/GodotProjects/Lentera-Pudar/qc_report.txt", "w")
if f then
    f:write(table.concat(report, "\n"))
    f:close()
end

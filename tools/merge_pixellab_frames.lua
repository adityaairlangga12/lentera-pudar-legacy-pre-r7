local directions = {"south", "north", "east", "west", "south-east", "south-west", "north-east", "north-west"}
local basePath = "C:/Users/ADIT/.gemini/antigravity-ide/brain/c041710e-3c46-44a8-a7aa-c1ee7f5420bf/scratch/pixellab_char/Idle/animations/"
local outPath = "D:/GodotProjects/Lentera-Pudar/Assets/Sprites/Characters/Protagonist/"

for _, dir in ipairs(directions) do
    local spr = Sprite(48, 48, ColorMode.RGB)
    
    local function addAnim(animName)
        for i=1, 4 do
            local imgPath = basePath .. animName .. "/" .. dir .. "/frame_00" .. tostring(i) .. ".png"
            local tempSpr = app.open(imgPath)
            if tempSpr then
                local img = tempSpr.cels[1].image:clone()
                tempSpr:close()
                
                app.activeSprite = spr
                local fr = spr:newEmptyFrame()
                spr:newCel(spr.layers[1], fr, img, Point(0, 0))
            end
        end
    end
    
    addAnim("idle_custom")
    addAnim("walk_custom")
    
    if #spr.frames > 1 then
        spr:deleteFrame(1)
    end
    
    local idleTag = spr:newTag(1, 4)
    idleTag.name = "idle"
    idleTag.color = Color{r=255, g=0, b=0, a=255}
    
    local walkTag = spr:newTag(5, 8)
    walkTag.name = "walk"
    walkTag.color = Color{r=0, g=255, b=0, a=255}
    
    spr:saveAs(outPath .. "protagonist_" .. dir .. ".aseprite")
    spr:close()
end

app.alert("Selesai! Frame ganda telah dibersihkan. Coba play sekarang!")

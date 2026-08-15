local sprite = app.activeSprite
if not sprite then
    return "Error: No active sprite"
end

app.transaction(function()
    -- 1. Auto-Crop (Remove all empty space)
    app.command.CanvasSize{ trim=true }
    
    local w = sprite.width
    local h = sprite.height
    
    -- 2. Target Canvas Size (32x32 standard, expand if larger)
    local target_w = 32
    local target_h = 32
    if w > 32 or h > 32 then
        target_w = 64
        target_h = 64
    end
    
    -- 3. Center of Mass calculation (simplified bounding box center)
    local offset_x = math.floor((target_w - w) / 2)
    local offset_y = math.floor((target_h - h) / 2)
    
    -- 4. Resize and center
    app.command.CanvasSize{
        bounds=Rectangle(-offset_x, -offset_y, target_w, target_h)
    }
end)

return "Success: Cropped and Centered to " .. tostring(sprite.width) .. "x" .. tostring(sprite.height)

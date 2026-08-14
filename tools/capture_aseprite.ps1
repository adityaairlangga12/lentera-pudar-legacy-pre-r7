Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
$Script = @'
using System;
using System.Drawing;
using System.Runtime.InteropServices;
public static class WinCapture {
    [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
    [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h, out RECT r);
    [StructLayout(LayoutKind.Sequential)]
    public struct RECT { public int Left, Top, Right, Bottom; }
    public static Bitmap CaptureWindow(IntPtr hwnd) {
        RECT rect;
        GetWindowRect(hwnd, out rect);
        int w = rect.Right - rect.Left;
        int h = rect.Bottom - rect.Top;
        var bmp = new Bitmap(w, h);
        using (var g = Graphics.FromImage(bmp))
            g.CopyFromScreen(rect.Left, rect.Top, 0, 0, new Size(w, h));
        return bmp;
    }
}
'@
Add-Type -TypeDefinition $Script -ReferencedAssemblies System.Drawing, System.Windows.Forms

$procs = Get-Process -Name "Aseprite" -ErrorAction SilentlyContinue | Where-Object { $_.MainWindowHandle -ne 0 }
if (-not $procs) { throw 'Aseprite not found' }
$proc = $procs | Select-Object -First 1
[WinCapture]::SetForegroundWindow($proc.MainWindowHandle) | Out-Null
Start-Sleep -Milliseconds 200
$bmp = [WinCapture]::CaptureWindow($proc.MainWindowHandle)
$bmp.Save("C:\Users\ADIT\.gemini\antigravity-ide\brain\c041710e-3c46-44a8-a7aa-c1ee7f5420bf\aseprite_live_view.png", [System.Drawing.Imaging.ImageFormat]::Png)
$bmp.Dispose()
Write-Output "Screenshot saved to artifact folder"

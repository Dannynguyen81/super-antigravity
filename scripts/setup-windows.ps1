# ==============================================================================
# Script: setup-windows.ps1
# Mục đích: Thiết lập môi trường 1-Click cho SUPER-ANTIGRAVITY trên Windows
# Tương thích: Windows 10 / Windows 11 (PowerShell 5.1+)
# ==============================================================================

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$Host.UI.RawUI.WindowTitle = "Khởi Tạo Môi Trường Super Antigravity"

Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host "  🚀 CHÀO MỪNG ĐẾN VỚI SUPER-ANTIGRAVITY — KHUNG VẬN HÀNH CHO GOOGLE ANTIGRAVITY" -ForegroundColor Yellow
Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host ""

$CurrentDir = Split-Path -Parent $PSScriptRoot

# 1. Kiểm tra Python
Write-Host "[1/3] Kiểm tra môi trường Python..." -NoNewline
if (Get-Command python -ErrorAction SilentlyContinue) {
    $PyVer = python --version
    Write-Host " [OK] ($PyVer)" -ForegroundColor Green
    
    # Kiểm tra/Cài đặt thư viện bóc tách tài liệu
    Write-Host "      Kiểm tra thư viện bóc tách tài liệu (markitdown)..." -NoNewline
    $hasMarkitdown = python -c "import markitdown; print('OK')" 2>$null
    if ($hasMarkitdown -eq "OK") {
        Write-Host " [OK] Đã sẵn sàng." -ForegroundColor Green
    } else {
        Write-Host " [CHƯA CÓ]" -ForegroundColor Yellow
        Write-Host "      Đang tự động cài đặt markitdown (hỗ trợ parse Word/Excel/PDF)..." -ForegroundColor Gray
        python -m pip install markitdown --quiet
        if ($LASTEXITCODE -eq 0) {
            Write-Host "      ✅ Cài đặt markitdown thành công!" -ForegroundColor Green
        } else {
            Write-Host "      ⚠️ Chưa cài được markitdown. Bạn vẫn có thể dùng các chức năng cơ bản." -ForegroundColor Yellow
        }
    }
} else {
    Write-Host " [CHƯA CÓ]" -ForegroundColor Red
    Write-Host "      👉 Bạn có thể tải Python miễn phí tại: https://www.python.org/downloads/" -ForegroundColor Gray
}

Write-Host ""

# 2. Kiểm tra phần mềm Obsidian
Write-Host "[2/3] Kiểm tra phần mềm Obsidian..." -NoNewline
$obsidianPath = "$env:LOCALAPPDATA\Programs\Obsidian\Obsidian.exe"
if (Test-Path $obsidianPath) {
    Write-Host " [OK] Đã tìm thấy Obsidian." -ForegroundColor Green
} else {
    Write-Host " [CHƯA TÌM THẤY TRONG APPDATA]" -ForegroundColor Yellow
    Write-Host "      👉 Nếu máy chưa cài Obsidian, bạn hãy tải tại: https://obsidian.md" -ForegroundColor Gray
}

Write-Host ""

# 3. Tạo Shortcut mở nhanh Kho Tri Thức trên Desktop
Write-Host "[3/3] Tạo lối tắt (Shortcut) mở nhanh Kho Tri Thức trên Màn hình chính..." -NoNewline
try {
    $WshShell = New-Object -ComObject WScript.Shell
    $DesktopPath = [System.Environment]::GetFolderPath('Desktop')
    $ShortcutPath = Join-Path $DesktopPath "Super Antigravity.lnk"
    $Shortcut = $WshShell.CreateShortcut($ShortcutPath)
    $Shortcut.TargetPath = "explorer.exe"
    $Shortcut.Arguments = "`"$CurrentDir`""
    $Shortcut.Description = "Super Antigravity Workspace"
    $Shortcut.WorkingDirectory = $CurrentDir
    $Shortcut.Save()
    Write-Host " [OK] Đã tạo icon trên Desktop!" -ForegroundColor Green
} catch {
    Write-Host " [BỎ QUA] ($($_.Exception.Message))" -ForegroundColor Gray
}

Write-Host ""
Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host "  🎉 THIẾT LẬP HOÀN TẤT!" -ForegroundColor Green
Write-Host "  📁 Vị trí workspace: $CurrentDir" -ForegroundColor White
Write-Host "  💡 Hướng dẫn nhanh:" -ForegroundColor Yellow
Write-Host "     1. Mở Antigravity IDE trỏ vào thư mục này để bắt đầu làm việc." -ForegroundColor Gray
Write-Host "     2. Mở Obsidian -> Chọn 'Open folder as vault' -> Trỏ vào thư mục này để xem đồ thị tri thức." -ForegroundColor Gray
Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host ""

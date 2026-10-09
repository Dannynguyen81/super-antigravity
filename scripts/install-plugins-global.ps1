# ==============================================================================
# Script: install-plugins-global.ps1
# Mục đích: Cài đặt toàn bộ 9 Plugins của SUPER-ANTIGRAVITY vào Antigravity Toàn Cục
# Tương thích: Windows 10 / Windows 11 (PowerShell 5.1+)
# ==============================================================================

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$Host.UI.RawUI.WindowTitle = "Cài Đặt Global Plugins Cho Super Antigravity"

Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host "  📦 CÀI ĐẶT SUPER-ANTIGRAVITY PLUGINS VÀO ANTIGRAVITY TOÀN CỤC" -ForegroundColor Yellow
Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host ""

$CurrentDir = Split-Path -Parent $PSScriptRoot
$PluginsSource = Join-Path $CurrentDir "plugins"
$GlobalPluginsDest = Join-Path $env:USERPROFILE ".gemini\config\plugins"

if (-not (Test-Path $PluginsSource)) {
    Write-Host "❌ Không tìm thấy thư mục plugins tại: $PluginsSource" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path $GlobalPluginsDest)) {
    Write-Host "Tạo thư mục đích: $GlobalPluginsDest" -ForegroundColor Gray
    New-Item -ItemType Directory -Path $GlobalPluginsDest -Force | Out-Null
}

$plugins = Get-ChildItem -Path $PluginsSource -Directory
Write-Host "Tìm thấy $($plugins.Count) plugins cần cài đặt..." -ForegroundColor Cyan

foreach ($p in $plugins) {
    $targetPath = Join-Path $GlobalPluginsDest $p.Name
    Write-Host "  -> Đang cài đặt: $($p.Name)..." -NoNewline
    Copy-Item -Path $p.FullName -Destination $targetPath -Recurse -Force
    Write-Host " [XONG]" -ForegroundColor Green
}

Write-Host ""
Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host "  🎉 CÀI ĐẶT THÀNH CÔNG $($plugins.Count) PLUGINS!" -ForegroundColor Green
Write-Host "  📁 Vị trí đích: $GlobalPluginsDest" -ForegroundColor White
Write-Host "  💡 Khởi động lại hoặc mở phiên mới trên Antigravity để nạp đầy đủ tính năng!" -ForegroundColor Yellow
Write-Host "==============================================================================" -ForegroundColor Cyan

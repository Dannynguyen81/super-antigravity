# Script cai dat / dong bo plugins va rules sang Google Antigravity (~/.gemini/config/plugins/)
param (
    [string]$TargetPluginsDir = "$env:USERPROFILE\.gemini\config\plugins"
)

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " [Google Antigravity] Dong bo bo ky nang va Plugins" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Cyan

if (-not (Test-Path $TargetPluginsDir)) {
    New-Item -ItemType Directory -Path $TargetPluginsDir -Force | Out-Null
}

$CurrentDir = Split-Path -Parent $PSScriptRoot
$PluginsSource = Join-Path $CurrentDir "plugins"
$RulesSource = Join-Path $CurrentDir "rules"

Write-Host ">> Nguon plugins: $PluginsSource"
Write-Host ">> Dich Antigravity Plugins: $TargetPluginsDir"

if (Test-Path $PluginsSource) {
    $plugins = Get-ChildItem -Path $PluginsSource -Directory
    $count = 0
    foreach ($p in $plugins) {
        $dest = Join-Path $TargetPluginsDir $p.Name
        if (-not (Test-Path $dest)) {
            New-Item -ItemType Directory -Path $dest -Force | Out-Null
        }
        # Dung robocopy de dong bo nhanh, bo qua cache va file khoa
        robocopy $p.FullName $dest /E /XD __pycache__ .git /NFL /NDL /NJH /NJS /nc /ns /np | Out-Null
        $count++
    }
    Write-Host ">> Da dong bo thanh cong $count plugins sang Google Antigravity!" -ForegroundColor Green
}

# Cap nhat AGENTS.md va SOUL.md vao antigravity-kit-plugin/rules neu co
$agKitRules = Join-Path $TargetPluginsDir "antigravity-kit-plugin\rules"
if (Test-Path $agKitRules) {
    if (Test-Path (Join-Path $RulesSource "AGENTS.md")) {
        Copy-Item -Path (Join-Path $RulesSource "AGENTS.md") -Destination (Join-Path $agKitRules "AGENTS.md") -Force
    }
    if (Test-Path (Join-Path $RulesSource "SOUL.md")) {
        Copy-Item -Path (Join-Path $RulesSource "SOUL.md") -Destination (Join-Path $agKitRules "SOUL.md") -Force
    }
    Write-Host ">> Da cap nhat rules AGENTS.md va SOUL.md vao Antigravity Kit!" -ForegroundColor Yellow
}

Write-Host "[OK] Hoan tat cau hinh Google Antigravity!" -ForegroundColor Cyan

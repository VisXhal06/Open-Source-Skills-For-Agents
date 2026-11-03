<#
.SYNOPSIS
    Refreshes this repository from the live global configuration.

.DESCRIPTION
    Reverse of install.ps1. Copies the current global skills, agents, and
    commands back into the repo so the published snapshot stays in sync with
    what actually runs on this machine.

    It does not delete anything. Removed skills will linger in the repo until
    you delete them yourself.

.PARAMETER DryRun
    Show what would change without writing anything.
#>
[CmdletBinding()]
param([switch]$DryRun)

$ErrorActionPreference = "Stop"
$repo = Split-Path $PSScriptRoot -Parent

$sources = @(
    @{ From = Join-Path $HOME ".agents\skills";            To = Join-Path $repo "skills";            Filter = $null },
    @{ From = Join-Path $HOME ".config\opencode\agents";   To = Join-Path $repo "agents\opencode";   Filter = "*.md" },
    @{ From = Join-Path $HOME ".claude\agents";            To = Join-Path $repo "agents\claude";     Filter = "*.md" },
    @{ From = Join-Path $HOME ".config\opencode\commands"; To = Join-Path $repo "commands";          Filter = "*.md" }
)

foreach ($s in $sources) {
    if (-not (Test-Path $s.From)) {
        Write-Warning "Missing source: $($s.From)"
        continue
    }
    if ($DryRun) {
        $n = if ($s.Filter) { (Get-ChildItem $s.From -File -Filter $s.Filter).Count } else { (Get-ChildItem $s.From -Directory).Count }
        Write-Host ("DRY  {0,4} items  {1}  ->  {2}" -f $n, $s.From, $s.To)
        continue
    }
    if ($s.Filter) {
        Copy-Item (Join-Path $s.From $s.Filter) -Destination $s.To -Force
    } else {
        Get-ChildItem $s.From -Directory | ForEach-Object {
            Copy-Item $_.FullName -Destination (Join-Path $s.To $_.Name) -Recurse -Force
        }
    }
    Write-Host "Synced $($s.From) -> $($s.To)"
}

Write-Host ""
Write-Host "Review changes with: git status"

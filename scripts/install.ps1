<#
.SYNOPSIS
    Installs the skills, agents, and commands from this repository into the
    current user's global OpenCode and Claude Code configuration.

.DESCRIPTION
    Copies:
      skills/*              -> ~/.agents/skills/
      agents/opencode/*.md  -> ~/.config/opencode/agents/
      agents/claude/*.md    -> ~/.claude/agents/
      commands/*.md         -> ~/.config/opencode/commands/

    Existing files with the same name are overwritten. Nothing outside these
    four directories is touched.

.PARAMETER DryRun
    Show what would be copied without writing anything.

.PARAMETER Force
    Overwrite existing files without prompting. Copying is non-interactive by
    default, so this only suppresses the summary prompt.
#>
[CmdletBinding()]
param(
    [switch]$DryRun,
    [switch]$Force
)

$ErrorActionPreference = "Stop"
$repo = Split-Path $PSScriptRoot -Parent

$destinations = @(
    @{ Source = Join-Path $repo "skills";            Target = Join-Path $HOME ".agents\skills";            Filter = $null },
    @{ Source = Join-Path $repo "agents\opencode";   Target = Join-Path $HOME ".config\opencode\agents";   Filter = "*.md" },
    @{ Source = Join-Path $repo "agents\claude";     Target = Join-Path $HOME ".claude\agents";            Filter = "*.md" },
    @{ Source = Join-Path $repo "commands";          Target = Join-Path $HOME ".config\opencode\commands"; Filter = "*.md" }
)

$total = 0

foreach ($d in $destinations) {
    if (-not (Test-Path $d.Source)) {
        Write-Warning "Missing source: $($d.Source)"
        continue
    }

    $count = if ($d.Filter) {
        (Get-ChildItem $d.Source -File -Filter $d.Filter).Count
    } else {
        (Get-ChildItem $d.Source -Directory).Count
    }

    Write-Host ("{0,-4} {1,4} items  {2}  ->  {3}" -f $(if ($DryRun) { "DRY" } else { "COPY" }), $count, $d.Source, $d.Target)

    if ($DryRun) { $total += $count; continue }

    if (-not (Test-Path $d.Target)) {
        New-Item -ItemType Directory -Path $d.Target -Force | Out-Null
    }

    if ($d.Filter) {
        Copy-Item (Join-Path $d.Source $d.Filter) -Destination $d.Target -Force
    } else {
        Get-ChildItem $d.Source -Directory | ForEach-Object {
            Copy-Item $_.FullName -Destination (Join-Path $d.Target $_.Name) -Recurse -Force
        }
    }

    $total += $count
}

Write-Host ""
if ($DryRun) {
    Write-Host "Dry run: $total items would be installed."
} else {
    Write-Host "Installed $total items."
    Write-Host "Reload OpenCode and Claude Code to pick up new agents and commands."
}

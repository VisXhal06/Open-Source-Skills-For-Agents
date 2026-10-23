param(
    [Parameter(Mandatory = $true)]
    [string[]]$Repos,

    [string[]]$Labels = @("good first issue", "help wanted"),

    [int]$Limit = 50,

    [string]$OutFile = "oss-issues.csv"
)

$rows = @()

foreach ($repo in $Repos) {
    foreach ($label in $Labels) {
        Write-Host "Scanning $repo / $label"
        $json = gh issue list --repo $repo --state open --label $label --limit $Limit --json number,title,url,labels,assignees,comments,createdAt,updatedAt,author 2>$null

        if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($json)) {
            Write-Warning "No data for $repo / $label"
            continue
        }

        $parsed = $json | ConvertFrom-Json
        $items = @($parsed) | Where-Object { $null -ne $_ }

        if ($items.Count -eq 0) {
            Write-Host "No open issues for $repo / $label"
            continue
        }

        foreach ($item in $items) {
            $author = if ($item.author) { $item.author.login } else { "" }
            $assignees = if ($item.assignees) { ($item.assignees.login -join ", ") } else { "" }
            $issueLabels = if ($item.labels) { ($item.labels.name -join ", ") } else { "" }
            $commentCount = if ($item.comments -is [array]) { $item.comments.Count } else { $item.comments }

            $rows += [pscustomobject]@{
                Score       = ""
                Repo        = $repo
                Number      = $item.number
                Title       = $item.title
                Url         = $item.url
                Author      = $author
                Assignees   = $assignees
                Comments    = $commentCount
                CreatedAt   = $item.createdAt
                UpdatedAt   = $item.updatedAt
                Labels      = $issueLabels
                HumanLead   = ""
                Status      = "New"
                NextAction  = ""
                PR          = ""
            }
        }
    }
}

if ($rows.Count -eq 0) {
    Write-Warning "No issues found. Check the repo names and labels."
    exit 1
}

$rows |
    Sort-Object UpdatedAt -Descending |
    Export-Csv -Path $OutFile -NoTypeInformation -Encoding UTF8

Write-Host "Saved $($rows.Count) issues to $OutFile"

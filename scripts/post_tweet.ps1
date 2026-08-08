# Post tweet using env credentials (OAuth 1.0a). Does not print secrets.
# Usage:
#   .\scripts\post_tweet.ps1 -DryRun
#   .\scripts\post_tweet.ps1
#   .\scripts\post_tweet.ps1 -Text "hello"
# Optional: create scripts/x-mcp.env from x-mcp.env.example and it will be loaded.

param(
  [string]$Text = "",
  [string]$File = "",
  [switch]$DryRun
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $Root

$envFile = Join-Path $Root "scripts\x-mcp.env"
if (Test-Path $envFile) {
  Get-Content $envFile | ForEach-Object {
    $line = $_.Trim()
    if (-not $line -or $line.StartsWith("#")) { return }
    $i = $line.IndexOf("=")
    if ($i -lt 1) { return }
    $k = $line.Substring(0, $i).Trim()
    $v = $line.Substring($i + 1).Trim().Trim('"').Trim("'")
    Set-Item -Path "Env:$k" -Value $v
  }
  Write-Host "Loaded scripts/x-mcp.env"
}

$need = @(
  "TWITTER_API_KEY",
  "TWITTER_API_SECRET",
  "TWITTER_ACCESS_TOKEN",
  "TWITTER_ACCESS_TOKEN_SECRET"
)
foreach ($n in $need) {
  if (-not [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable($n))) { continue }
  if (-not [string]::IsNullOrWhiteSpace((Get-Item "Env:$n" -ErrorAction SilentlyContinue).Value)) { continue }
  Write-Error "Missing $n. Set User env or fill scripts/x-mcp.env (see docs/x-mcp-setup.md)"
}

if (-not $File -and -not $Text) {
  $File = "docs\tweet-awesome-kling.txt"
}

$pyArgs = @("scripts/post_to_x.py")
if ($DryRun) { $pyArgs += "--dry-run" }
if ($Text) {
  $pyArgs += @("--text", $Text)
} else {
  $pyArgs += @("--file", $File)
}

python @pyArgs

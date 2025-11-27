# PowerShell script to help deploy to GitHub
# Run this script after creating your GitHub repository

param(
    [Parameter(Mandatory=$true)]
    [string]$GitHubUsername,
    
    [Parameter(Mandatory=$true)]
    [string]$RepositoryName
)

Write-Host "🚀 Preparing to push to GitHub..." -ForegroundColor Green

# Check if remote already exists
$remoteExists = git remote get-url origin 2>$null
if ($remoteExists) {
    Write-Host "⚠️  Remote 'origin' already exists. Removing it..." -ForegroundColor Yellow
    git remote remove origin
}

# Add remote
Write-Host "📦 Adding GitHub remote..." -ForegroundColor Cyan
git remote add origin "https://github.com/$GitHubUsername/$RepositoryName.git"

# Rename branch to main if needed
$currentBranch = git branch --show-current
if ($currentBranch -eq "master") {
    Write-Host "🔄 Renaming branch to 'main'..." -ForegroundColor Cyan
    git branch -M main
}

# Show status
Write-Host "`n📋 Current status:" -ForegroundColor Cyan
git status

Write-Host "`n✅ Ready to push! Run the following command:" -ForegroundColor Green
Write-Host "   git push -u origin main" -ForegroundColor Yellow
Write-Host "`n💡 If you haven't created the GitHub repository yet, do that first at:" -ForegroundColor Cyan
Write-Host "   https://github.com/new" -ForegroundColor Yellow



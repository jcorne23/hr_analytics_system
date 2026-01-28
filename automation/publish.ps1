$ErrorActionPreference = "Stop"

cd  "C:\Users\jcorn\OneDrive\Documents\personal_website\Portfolio"

python "C:\Users\jcorn\OneDrive\Desktop\Analytics\automation\publicate.py"

git status
git add quote.html 
git commit -m "Daily quote update"
git push

Write-Host "✅ Quote published and pushed to GitHub"
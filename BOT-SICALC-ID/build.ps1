$exclude = @("venv", "BOT-SICALC-ID.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "BOT-SICALC-ID.zip" -Force
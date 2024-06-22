$exclude = @("venv", "bot-sicalc.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot-sicalc.zip" -Force
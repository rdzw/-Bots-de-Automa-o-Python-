$exclude = @("venv", "BotCotacaoDom.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "BotCotacaoDom.zip" -Force
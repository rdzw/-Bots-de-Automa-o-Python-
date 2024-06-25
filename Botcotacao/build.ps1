$exclude = @("venv", "Botcotacao.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Botcotacao.zip" -Force
$exclude = @("venv", "bot-busca-cep.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot-busca-cep.zip" -Force
$exclude = @("venv", "bot-busca-avaliacao-produto.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot-busca-avaliacao-produto.zip" -Force
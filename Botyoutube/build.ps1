$exclude = @("venv", "Botyoutube.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "Botyoutube.zip" -Force
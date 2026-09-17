$Root="$env:USERPROFILE\Desktop\apex-local";Set-Location $Root
if(-not(Test-Path "$Root\venv\Scripts\python.exe")){Write-Host 'Run APEX_INSTALL.ps1 first.' -ForegroundColor Red;exit 1}
if(-not(Get-Process ollama -ErrorAction SilentlyContinue)){Start-Process ollama -ArgumentList 'serve' -WindowStyle Hidden;Start-Sleep 2}
if(-not(try{(Invoke-WebRequest 'http://127.0.0.1:8000/health' -UseBasicParsing -TimeoutSec 2).StatusCode -eq 200}catch{$false})){Start-Process "$Root\venv\Scripts\python.exe" -ArgumentList '-m','uvicorn','apex.main:app','--port','8000' -WorkingDirectory $Root -WindowStyle Hidden;Start-Sleep 3}
Start-Process 'http://127.0.0.1:8000/docs';Write-Host 'APEX READY — http://127.0.0.1:8000/docs' -ForegroundColor Green

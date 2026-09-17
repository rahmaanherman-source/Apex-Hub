$Root="$env:USERPROFILE\Desktop\apex-local";if(Test-Path "$Root\venv\Scripts\python.exe"){& "$Root\venv\Scripts\python.exe" "$Root\apex\vault.py"}else{python "$Root\apex\vault.py"}

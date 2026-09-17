<#{Apex Local one-file bootstrap. Save as APEX_INSTALL.ps1 and Run with PowerShell.}#>
param([switch]$DryRun)
Add-Type -AssemblyName System.Windows.Forms
$ErrorActionPreference='Stop'
$Root=Join-Path $env:USERPROFILE 'Desktop\apex-local'
function Ask($t,$m){[System.Windows.Forms.MessageBox]::Show($m,$t,[System.Windows.Forms.MessageBoxButtons]::YesNo,[System.Windows.Forms.MessageBoxIcon]::Question) -eq [System.Windows.Forms.DialogResult]::Yes}
function Info($t,$m){[System.Windows.Forms.MessageBox]::Show($m,$t,[System.Windows.Forms.MessageBoxButtons]::OK,[System.Windows.Forms.MessageBoxIcon]::Information)|Out-Null}
Info 'APEX INSTALLER' 'APEX Local will install into Desktop\apex-local, create a Python venv, optionally install Ollama and local models, open the Vault, start FastAPI, open the docs, and create Desktop shortcuts.'
if(Test-Path $Root){if(Ask 'APEX' 'Desktop\apex-local already exists. Replace it with the current repository version?'){Remove-Item $Root -Recurse -Force}else{Info 'APEX' 'Installation cancelled.';exit}}
if($DryRun){Info 'APEX DRY RUN' 'No files or system settings will be changed.';exit}
$zip=Join-Path $env:TEMP 'apex-hub-main.zip';$tmp=Join-Path $env:TEMP 'APEX-Hub-Install'
if(Test-Path $tmp){Remove-Item $tmp -Recurse -Force};New-Item -ItemType Directory -Force -Path $tmp|Out-Null
Invoke-WebRequest 'https://github.com/rahmaanherman-source/Apex-Hub/archive/refs/heads/main.zip' -OutFile $zip
Expand-Archive $zip -DestinationPath $tmp -Force
$source=Join-Path $tmp 'Apex-Hub-main\apex-local'
if(-not(Test-Path (Join-Path $source 'requirements.txt'))){throw 'APEX Local payload was not found in the repository.'}
Copy-Item $source $Root -Recurse -Force
New-Item -ItemType Directory -Force -Path "$Root\secrets","$Root\logs","$Root\data"|Out-Null
if(Ask 'APEX — Python' 'Create the Python virtual environment and install dependencies?'){python -m venv "$Root\venv";& "$Root\venv\Scripts\python.exe" -m pip install --upgrade pip;& "$Root\venv\Scripts\python.exe" -m pip install -r "$Root\requirements.txt"}
if(Ask 'APEX — Ollama' 'Install Ollama if it is not already installed?'){if(-not(Get-Command ollama -ErrorAction SilentlyContinue)){ $o=Join-Path $env:TEMP 'OllamaSetup.exe';Invoke-WebRequest 'https://ollama.com/download/OllamaSetup.exe' -OutFile $o;Start-Process $o -Wait }}
if(Ask 'APEX — Model' 'Pull qwen2.5-coder:7b now?'){ollama pull qwen2.5-coder:7b}
if(Ask 'APEX — Fast Model' 'Pull llama3.2:3b too?'){ollama pull llama3.2:3b}
if(Ask 'APEX — Vault' 'Open the APEX Vault now?'){Start-Process "$Root\venv\Scripts\python.exe" -ArgumentList "$Root\apex\vault.py"}
if(Ask 'APEX — Backend' 'Start the APEX backend on port 8000?'){if(-not(Get-Process ollama -ErrorAction SilentlyContinue)){Start-Process ollama -ArgumentList 'serve' -WindowStyle Hidden;Start-Sleep 2};Start-Process "$Root\venv\Scripts\python.exe" -ArgumentList '-m','uvicorn','apex.main:app','--port','8000' -WorkingDirectory $Root -WindowStyle Hidden;Start-Sleep 3;Start-Process 'http://127.0.0.1:8000/docs'}
$w=New-Object -ComObject WScript.Shell;$d=[Environment]::GetFolderPath('Desktop');foreach($x in @(@('APEX Terminal.lnk','start_apex.ps1'),@('APEX Vault.lnk','vault.ps1'),@('APEX Health.lnk','health_check.ps1'))){$s=$w.CreateShortcut((Join-Path $d $x[0]));$s.TargetPath='powershell.exe';$s.Arguments="-NoExit -ExecutionPolicy Bypass -File `"$Root\scripts\$($x[1])`"";$s.WorkingDirectory=$Root;$s.Save()}
Info 'APEX READY' 'APEX Local is installed. Desktop shortcuts are ready. API docs: http://127.0.0.1:8000/docs'

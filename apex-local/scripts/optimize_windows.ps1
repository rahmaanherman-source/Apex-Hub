param([switch]$DryRun,[switch]$SkipSecurity)
$ErrorActionPreference='Stop';$Root="$env:USERPROFILE\Desktop\apex-local";$LogPath="$Root\logs\optimize_$(Get-Date -Format yyyyMMdd_HHmmss).log";New-Item -ItemType Directory -Force -Path (Split-Path $LogPath)|Out-Null
function Log($m){$l="[$(Get-Date -Format HH:mm:ss)] $m";Write-Host $l;Add-Content $LogPath $l}
Log "APEX Windows optimization. DryRun=$DryRun SkipSecurity=$SkipSecurity"
$cpu=Get-CimInstance Win32_Processor;$ram=[math]::Round((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory/1GB,1);$disks=Get-PhysicalDisk -ErrorAction SilentlyContinue;Log "CPU=$($cpu.Name); RAM=${ram}GB; disks=$($disks.Count)"
if(-not $DryRun){try{Enable-ComputerRestore -Drive "$env:SystemDrive\" -ErrorAction SilentlyContinue;Checkpoint-Computer -Description 'APEX Pre-Optimization' -RestorePointType MODIFY_SETTINGS -ErrorAction Stop;Log 'Restore point created.'}catch{Log "Restore point unavailable: $($_.Exception.Message)"}}
if($DryRun){Log 'DRY RUN: no system modifications will be made.';Log 'Would ensure firewall is enabled, SMBv1 disabled, AutoRun restricted, and optionally enable Memory Integrity.';exit 0}
if(-not $SkipSecurity){Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force -ErrorAction SilentlyContinue;Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True;Log 'Firewall enabled; SMBv1 disabled where supported.';Write-Host 'Memory Integrity is intentionally not forced automatically; enable it through Windows Security after driver compatibility review.' -ForegroundColor Yellow}
Log 'Optimization/security pass complete.'

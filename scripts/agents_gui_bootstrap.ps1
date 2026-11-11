# Own the window for this user/configuration before collecting slow evidence.
param([Parameter(Mandatory=$true)][string]$ContextFile)
$ErrorActionPreference='Stop'
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
[Windows.Forms.Application]::EnableVisualStyles()
$context=Get-Content -LiteralPath $ContextFile -Raw | ConvertFrom-Json
$eventName='Local\ResearchLauncher-'+$context.instance+'-activate'
$signal=New-Object Threading.EventWaitHandle($false,[Threading.EventResetMode]::AutoReset,$eventName)
$mutex=New-Object Threading.Mutex($false,('Local\ResearchLauncher-'+$context.instance))
$owned=$false; $loading=$null; $worker=$null
try {
    try {$owned=$mutex.WaitOne(0)} catch [Threading.AbandonedMutexException] {$owned=$true}
    if (-not $owned) {[void]$signal.Set(); exit 0}
    $loading=New-Object Windows.Forms.Form
    $loading.Text='Agent Launcher - opening'
    $loading.StartPosition='CenterScreen'; $loading.ClientSize=New-Object Drawing.Size(430,110)
    $loading.BackColor=[Drawing.Color]::FromArgb(11,23,42)
    $loading.ForeColor=[Drawing.Color]::White
    $loading.FormBorderStyle='FixedDialog'; $loading.MaximizeBox=$false
    $label=New-Object Windows.Forms.Label
    $label.Text="Opening Agent Launcher...`r`nLoading agents and recent work."
    $label.Font=New-Object Drawing.Font('Segoe UI',12)
    $label.Dock='Fill'; $label.Padding=New-Object Windows.Forms.Padding(20)
    $loading.Controls.Add($label); $loading.Show()
    [Windows.Forms.Application]::DoEvents()
    $info=New-Object Diagnostics.ProcessStartInfo
    $info.FileName='wsl.exe'; $info.Arguments=$context.prepare_arguments
    $info.UseShellExecute=$false; $info.CreateNoWindow=$true
    $info.RedirectStandardOutput=$true; $info.RedirectStandardError=$true
    $worker=[Diagnostics.Process]::Start($info)
    $output=$worker.StandardOutput.ReadToEndAsync(); $errors=$worker.StandardError.ReadToEndAsync()
    while (-not $worker.HasExited) {
        [Windows.Forms.Application]::DoEvents()
        if ($signal.WaitOne(0) -and -not $loading.IsDisposed) {$loading.Activate()}
        # Closing loading cancels opening; the read-only worker is allowed to finish.
        Start-Sleep -Milliseconds 50
    }
    if ($loading.IsDisposed) {exit 0}
    if ($worker.ExitCode -ne 0) {throw ($errors.Result+' '+$output.Result).Trim()}
    $loading.Close(); $loading.Dispose(); $loading=$null
    & (Join-Path $PSScriptRoot 'agents_gui.ps1') -DataFile (Join-Path (Split-Path $ContextFile) 'catalogue.json') -ActivationEvent $eventName
} catch {
    if (-not $context.test_mode) {[void][Windows.Forms.MessageBox]::Show($_.Exception.Message,'Agent Launcher')}
    Write-Error $_ -ErrorAction Continue
    exit 2
} finally {
    if ($loading) {$loading.Dispose()}
    if ($worker) {$worker.Dispose()}
    if ($owned) {$mutex.ReleaseMutex()}
    $mutex.Dispose(); $signal.Dispose()
}

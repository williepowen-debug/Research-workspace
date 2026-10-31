# Local read-only Calendar, outside the agent/model dispatch queue.
$calendarPanel=New-Object Windows.Forms.FlowLayoutPanel
$calendarPanel.Dock='Fill'; $calendarPanel.FlowDirection='TopDown'
$calendarPanel.WrapContents=$false; $calendarPanel.Padding=New-Object Windows.Forms.Padding(20)
$pages.Calendar.Controls.Add($calendarPanel)
$calendarTitle=New-Object Windows.Forms.Label
$calendarTitle.Text='Calendar'; $calendarTitle.AutoSize=$true
$calendarTitle.Font=New-Object Drawing.Font('Segoe UI',16)
$calendarPanel.Controls.Add($calendarTitle)
$calendarHelp=New-Object Windows.Forms.Label
$calendarHelp.Text='Browse events and agent work by week or day. Refresh reads current local source files and shows unavailable or stale sources. Opening the calendar starts no agents and changes no schedules.'
$calendarHelp.AutoSize=$true; $calendarHelp.MaximumSize=New-Object Drawing.Size(720,0)
$calendarHelp.Margin=New-Object Windows.Forms.Padding(3,16,3,20)
$calendarPanel.Controls.Add($calendarHelp)
$calendarOpen=New-Object LauncherButton
$calendarOpen.Text='Open Calendar'; $calendarOpen.Size=New-Object Drawing.Size(250,44)
Style-Button $calendarOpen $true; $calendarPanel.Controls.Add($calendarOpen)
$calendarCheck=New-Object LauncherButton
$calendarCheck.Text='Check source coverage'; $calendarCheck.Size=New-Object Drawing.Size(250,44)
Style-Button $calendarCheck; $calendarPanel.Controls.Add($calendarCheck)
$calendarStatus=New-Object Windows.Forms.Label
$calendarStatus.AutoSize=$true; $calendarStatus.MaximumSize=New-Object Drawing.Size(720,0)
$calendarStatus.Margin=New-Object Windows.Forms.Padding(3,16,3,3)
$calendarPanel.Controls.Add($calendarStatus)

function Calendar-Arguments([bool]$check) {
    if (-not $data.bridge.EndsWith('/scripts/agents_gui.py')) {throw 'Calendar could not locate this workspace.'}
    $root=$data.bridge.Substring(0,$data.bridge.Length-'/scripts/agents_gui.py'.Length)
    $values=@('-d',$data.distro,'-u',$data.user,'--exec',$data.python,'-B',($root+'/AGENTS/CATO/prototypes/calendar/live/app.py'))
    if ($check) {$values+=@('--check','--pause')} else {$values+=@('--open-browser')}
    return $values
}
function Start-Calendar([bool]$check) {
    try {
        $values=Calendar-Arguments $check
        if ($SmokeTest -or $data.test_mode) {$script:calendarTestArguments=$values; return}
        $quoted=foreach ($v in $values) {
            $v=[string]$v
            if ($v -and $v -notmatch '[\s"]') {$v} else {
                $escaped=[regex]::Replace($v,'(\\*)"','$1$1\"')
                $escaped=[regex]::Replace($escaped,'(\\+)$','$1$1')
                '"'+$escaped+'"'
            }
        }
        $psi=New-Object Diagnostics.ProcessStartInfo
        $psi.FileName='wsl.exe'; $psi.Arguments=$quoted -join ' '
        $psi.UseShellExecute=$true; $psi.WindowStyle='Normal'
        [void][Diagnostics.Process]::Start($psi)
        $calendarStatus.Text='Opened a separate Calendar window. Keep it open while using the app; its errors and check results appear there.'
    } catch {$calendarStatus.Text='Calendar could not open: '+$_.Exception.Message}
}
$calendarOpen.Add_Click({Start-Calendar $false})
$calendarCheck.Add_Click({Start-Calendar $true})
function Test-CalendarLauncher {
    $tabs.SelectedTab=$pages.Calendar
    if ($calendarTitle.Text -cne 'Calendar') {throw 'Calendar title encoding changed'}
    $queueCount=$script:queue.Count; $history=[IO.File]::ReadAllText($script:historyPath)
    $calendarOpen.PerformClick()
    $args=$script:calendarTestArguments
    if ($args -notcontains '--open-browser' -or $args -contains '--supervised' -or $args -contains '--check') {throw 'Calendar used a pilot flag or the wrong operation'}
    if ($args -notcontains ($data.bridge.Replace('/scripts/agents_gui.py','/AGENTS/CATO/prototypes/calendar/live/app.py'))) {throw 'Calendar opened the wrong workspace'}
    $calendarCheck.PerformClick()
    if ($script:calendarTestArguments -notcontains '--check' -or $script:calendarTestArguments -contains '--supervised') {throw 'Device check could answer'}
    if ($script:queue.Count -ne $queueCount -or [IO.File]::ReadAllText($script:historyPath) -cne $history) {throw 'Calendar touched the agent queue or launch history'}
}

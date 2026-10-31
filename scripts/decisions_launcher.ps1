# Local Decisions desk, outside the agent/model dispatch queue.
$decisionsPanel=New-Object Windows.Forms.FlowLayoutPanel
$decisionsPanel.Dock='Fill'; $decisionsPanel.FlowDirection='TopDown'
$decisionsPanel.WrapContents=$false; $decisionsPanel.Padding=New-Object Windows.Forms.Padding(20)
$pages.Decisions.Controls.Add($decisionsPanel)
$decisionsTitle=New-Object Windows.Forms.Label
$decisionsTitle.Text='Decisions'; $decisionsTitle.AutoSize=$true
$decisionsTitle.Font=New-Object Drawing.Font('Segoe UI',16)
$decisionsPanel.Controls.Add($decisionsTitle)
$decisionsHelp=New-Object Windows.Forms.Label
$decisionsHelp.Text='Read your decisions and personal tasks, respond, and follow progress in one place. Replies unlock after the final accepted build; the existing queue and PROME rulings remain authoritative.'
$decisionsHelp.AutoSize=$true; $decisionsHelp.MaximumSize=New-Object Drawing.Size(720,0)
$decisionsHelp.Margin=New-Object Windows.Forms.Padding(3,16,3,20)
$decisionsPanel.Controls.Add($decisionsHelp)
$decisionsOpen=New-Object LauncherButton
$decisionsOpen.Text='Open Decisions'; $decisionsOpen.Size=New-Object Drawing.Size(250,44)
Style-Button $decisionsOpen $true; $decisionsPanel.Controls.Add($decisionsOpen)
$decisionsCheck=New-Object LauncherButton
$decisionsCheck.Text='Check this computer'; $decisionsCheck.Size=New-Object Drawing.Size(250,44)
Style-Button $decisionsCheck; $decisionsPanel.Controls.Add($decisionsCheck)
$decisionsStatus=New-Object Windows.Forms.Label
$decisionsStatus.AutoSize=$true; $decisionsStatus.MaximumSize=New-Object Drawing.Size(720,0)
$decisionsStatus.Margin=New-Object Windows.Forms.Padding(3,16,3,3)
$decisionsPanel.Controls.Add($decisionsStatus)

function Decisions-Arguments([bool]$check) {
    if (-not $data.bridge.EndsWith('/scripts/agents_gui.py')) {throw 'Decisions could not locate this workspace.'}
    $root=$data.bridge.Substring(0,$data.bridge.Length-'/scripts/agents_gui.py'.Length)
    $values=@('-d',$data.distro,'-u',$data.user,'--exec',$data.python,'-B',($root+'/AGENTS/CATO/prototypes/decisions/mvp/app.py'))
    if ($check) {$values+=@('--check','--pause')} else {$values+=@('--open-browser','--pause')}
    return $values
}
function Start-Decisions([bool]$check) {
    try {
        $values=Decisions-Arguments $check
        if ($SmokeTest -or $data.test_mode) {$script:decisionsTestArguments=$values; return}
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
        $decisionsStatus.Text='Opened a separate Decisions window. Keep it open while using the app; its errors and check results appear there.'
    } catch {$decisionsStatus.Text='Decisions could not open: '+$_.Exception.Message}
}
$decisionsOpen.Add_Click({Start-Decisions $false})
$decisionsCheck.Add_Click({Start-Decisions $true})
function Test-DecisionsLauncher {
    $tabs.SelectedTab=$pages.Decisions
    if ($decisionsTitle.Text -cne 'Decisions') {throw 'Decisions title encoding changed'}
    $queueCount=$script:queue.Count; $history=[IO.File]::ReadAllText($script:historyPath)
    $decisionsOpen.PerformClick()
    $args=$script:decisionsTestArguments
    if ($args -notcontains '--open-browser' -or $args -contains '--supervised' -or $args -contains '--check') {throw 'Decisions used a pilot flag or the wrong operation'}
    if ($args -notcontains ($data.bridge.Replace('/scripts/agents_gui.py','/AGENTS/CATO/prototypes/decisions/mvp/app.py'))) {throw 'Decisions opened the wrong workspace'}
    $decisionsCheck.PerformClick()
    if ($script:decisionsTestArguments -notcontains '--check' -or $script:decisionsTestArguments -contains '--supervised') {throw 'Device check could answer'}
    if ($script:queue.Count -ne $queueCount -or [IO.File]::ReadAllText($script:historyPath) -cne $history) {throw 'Decisions touched the agent queue or launch history'}
}

param([Parameter(Mandatory=$true)][string]$DataFile, [switch]$SmokeTest)
$ErrorActionPreference = 'Stop'
trap {
    if (-not $SmokeTest) {
        [void][System.Windows.Forms.MessageBox]::Show($_.Exception.Message,'Agent Launcher')
    }
    Write-Error $_ -ErrorAction Continue
    exit 2
}
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
[System.Windows.Forms.Application]::EnableVisualStyles()
$data = Get-Content -LiteralPath $DataFile -Raw | ConvertFrom-Json
$script:busy = $false
$script:process = $null
$script:selected = $null
$script:resultFile = $null
$script:started = $null
$bg = [Drawing.Color]::FromArgb(242,244,248)
$ink = [Drawing.Color]::FromArgb(29,40,57)
$muted = [Drawing.Color]::FromArgb(87,100,120)
$accent = [Drawing.Color]::FromArgb(42,91,164)
$form = New-Object Windows.Forms.Form
$form.Text = 'Agent Launcher'
$form.ClientSize = New-Object Drawing.Size(880,630)
$form.MinimumSize = New-Object Drawing.Size(896,669)
$form.StartPosition = 'CenterScreen'
$form.BackColor = $bg
$form.ForeColor = $ink
$form.Font = New-Object Drawing.Font('Segoe UI',10)
$form.AutoScaleMode = 'Dpi'

function Label($text,$x,$y,$width,$height,$size=10) {
    $c = New-Object Windows.Forms.Label
    $c.Text=$text; $c.SetBounds($x,$y,$width,$height)
    $c.Font=New-Object Drawing.Font('Segoe UI',$size)
    $form.Controls.Add($c)
    return $c
}
function Button($text,$x,$y,$width) {
    $c = New-Object Windows.Forms.Button
    $c.Text=$text; $c.SetBounds($x,$y,$width,42)
    $c.FlatStyle='Flat'; $c.FlatAppearance.BorderSize=0
    $c.BackColor=[Drawing.Color]::White; $c.ForeColor=$ink
    $c.Cursor='Hand'; $form.Controls.Add($c)
    return $c
}
$title=Label 'Your agent desk' 26 20 650 40 23
$subtitle=Label 'Choose an agent. Open a conversation. Get to work.' 28 65 800 30
$subtitle.ForeColor=$muted
$searchLabel=Label 'Search agents' 28 111 330 25
$search=New-Object Windows.Forms.TextBox
$search.SetBounds(28,139,330,30); $form.Controls.Add($search)
$list=New-Object Windows.Forms.ListBox
$list.SetBounds(28,181,330,370); $list.IntegralHeight=$false
$list.BorderStyle='None'; $list.Font=New-Object Drawing.Font('Segoe UI',11)
$list.DisplayMember='Display'; $list.Anchor='Top,Bottom,Left'
$form.Controls.Add($list)
$count=Label '' 28 562 330 26
$count.ForeColor=$muted; $count.Anchor='Bottom,Left'
$name=Label 'Select an agent' 388 111 460 38 21
$purpose=Label '' 390 157 458 56 11
$purpose.ForeColor=$muted
$group=Label '' 390 216 458 24
$group.ForeColor=$muted
$runtimeLabel=Label 'Run with' 390 255 458 25
$runtime=New-Object Windows.Forms.ComboBox
$runtime.SetBounds(390,284,458,32); $runtime.DropDownStyle='DropDownList'
$runtime.Anchor='Top,Left,Right'; $form.Controls.Add($runtime)
$taskLabel=Label 'Optional task for a new conversation' 390 332 458 25
$task=New-Object Windows.Forms.TextBox
$task.SetBounds(390,363,458,92); $task.Multiline=$true; $task.AcceptsReturn=$true
$task.ScrollBars='Vertical'; $task.Anchor='Top,Left,Right'; $form.Controls.Add($task)
$start=Button 'Start new' 390 474 220
$start.BackColor=$accent; $start.ForeColor=[Drawing.Color]::White
$resume=Button 'Resume...' 626 474 222
$hint=Label 'Resume opens your saved-conversation picker.' 390 528 458 28
$hint.ForeColor=$muted
$status=Label 'Each conversation opens in its own terminal window.' 390 563 458 55
$status.ForeColor=$muted; $status.Anchor='Bottom,Left,Right'
foreach ($control in @($name,$purpose,$group,$runtimeLabel,$taskLabel,$hint)) {$control.Anchor='Top,Left,Right'}
$tooltip=New-Object Windows.Forms.ToolTip
$tooltip.SetToolTip($task,'For Start new only. To resume with a new task, open the conversation first.')

function Update-Buttons {
    $ready=($null -ne $script:selected -and -not $script:busy)
    $start.Enabled=$ready
    $resume.Enabled=($ready -and [string]::IsNullOrWhiteSpace($task.Text))
    $search.Enabled=-not $script:busy; $list.Enabled=-not $script:busy
    $runtime.Enabled=($ready -and $script:selected.kind -ne 'cato')
    $task.Enabled=-not $script:busy
}
function Select-Agent {
    if ($null -eq $list.SelectedItem) {
        $script:selected=$null; $name.Text='No matching agents'; $purpose.Text='Try another name or topic.'
        $group.Text=''; $runtime.Items.Clear(); Update-Buttons; return
    }
    $script:selected=$list.SelectedItem.Entry
    $name.Text=$script:selected.name; $purpose.Text=$script:selected.purpose
    $group.Text=$script:selected.group
    $runtime.Items.Clear()
    if ($script:selected.kind -eq 'cato') {
        [void]$runtime.Items.Add('Codex Astra'); $runtime.SelectedIndex=0
    } else {
        [void]$runtime.Items.Add('Codex Sol'); [void]$runtime.Items.Add('Claude')
        $runtime.SelectedIndex=0
        if ($script:selected.default_runtime -eq 'claude') {$runtime.SelectedIndex=1}
    }
    $status.Text='Each conversation opens in its own terminal window.'
    if ($script:selected.error) {$status.Text=$script:selected.error}
    $tooltip.SetToolTip($status,$status.Text)
    $tooltip.SetToolTip($name,$script:selected.folder)
    Update-Buttons
}
function Filter-Agents {
    $previous=$null
    if ($script:selected) {$previous=$script:selected.name}
    $query=$search.Text.Trim()
    $list.BeginUpdate(); $list.Items.Clear()
    foreach ($entry in $data.agents) {
        $haystack=$entry.name+' '+$entry.purpose+' '+$entry.group
        if ($haystack.IndexOf($query,[StringComparison]::OrdinalIgnoreCase) -ge 0) {
            $display=$entry.name
            if ($entry.error) {$display+='  (check setup)'}
            [void]$list.Items.Add([pscustomobject]@{Display=$display;Entry=$entry})
        }
    }
    $list.EndUpdate(); $count.Text=[string]$list.Items.Count+' agents'
    if ($list.Items.Count -gt 0) {
        $list.SelectedIndex=0
        for ($i=0;$i -lt $list.Items.Count;$i++) {
            if ($list.Items[$i].Entry.name -eq $previous) {$list.SelectedIndex=$i;break}
        }
    } else {Select-Agent}
}
function Begin-Launch($action) {
    if ($script:busy -or $null -eq $script:selected) {return}
    $script:busy=$true; Update-Buttons
    try {
        $id=[Guid]::NewGuid().ToString('N')
        $request=Join-Path $data.directory ($id+'.json')
        $script:resultFile=Join-Path $data.directory ($id+'.result.json')
        $runtimeName='sol'
        if ($runtime.Text -eq 'Claude') {$runtimeName='claude'}
        if ($runtime.Text -eq 'Codex Astra') {$runtimeName='astra'}
        $taskText=$null
        if (-not [string]::IsNullOrWhiteSpace($task.Text)) {$taskText=$task.Text}
        @{name=$script:selected.name;runtime=$runtimeName;action=$action;task=$taskText} |
            ConvertTo-Json | Set-Content -LiteralPath $request -Encoding UTF8
        # Fixed paths are quoted as Windows argv. User task text stays in JSON.
        $values=@('-d',$data.distro,'-u',$data.user,'--exec',$data.python,$data.bridge,'--launch',($data.linux_directory+'/'+$id+'.json'))
        # WSL's option parser needs unquoted switches. Quote only values that
        # need it, doubling backslashes before quotes and at a quoted end.
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
        $psi.UseShellExecute=$false; $psi.CreateNoWindow=$true
        $psi.RedirectStandardOutput=$true; $psi.RedirectStandardError=$true
        $script:process=[Diagnostics.Process]::Start($psi)
        $script:outputRead=$script:process.StandardOutput.ReadToEndAsync()
        $script:errorRead=$script:process.StandardError.ReadToEndAsync()
        $script:started=[DateTime]::UtcNow
        $status.ForeColor=$muted; $status.Text='Opening '+$script:selected.name+'...'
    } catch {
        $status.Text=$_.Exception.Message; $script:busy=$false; Update-Buttons
    }
}
$timer=New-Object Windows.Forms.Timer
$timer.Interval=200
$timer.Add_Tick({
    if (-not $script:busy -or $null -eq $script:process) {return}
    try {
        if (Test-Path -LiteralPath $script:resultFile) {
            $result=Get-Content -LiteralPath $script:resultFile -Raw | ConvertFrom-Json
            $status.Text=$result.message
            $status.ForeColor=$muted
            if (-not $result.ok) {$status.ForeColor=[Drawing.Color]::FromArgb(155,52,43)}
            $script:busy=$false; Update-Buttons
            $tooltip.SetToolTip($status,$status.Text)
        } elseif ($script:process.HasExited -or ([DateTime]::UtcNow-$script:started).TotalSeconds -gt 40) {
            $status.Text='Startup was not confirmed. Check the agent window before trying again.'
            if ($script:process.HasExited) {
                $detail=($script:errorRead.Result+' '+$script:outputRead.Result).Trim()
                if ($detail) {$status.Text=$detail}
            }
            $tooltip.SetToolTip($status,$status.Text)
            $script:busy=$false; Update-Buttons
        }
    } catch {$status.Text=$_.Exception.Message; $script:busy=$false; Update-Buttons}
})
$search.Add_TextChanged({Filter-Agents})
$list.Add_SelectedIndexChanged({Select-Agent})
$task.Add_TextChanged({
    $hint.Text='Resume opens your saved-conversation picker.'
    if (-not [string]::IsNullOrWhiteSpace($task.Text)) {$hint.Text='Clear the task box to resume an existing conversation.'}
    Update-Buttons
})
$start.Add_Click({Begin-Launch 'new'})
$resume.Add_Click({Begin-Launch 'resume'})
$form.Add_FormClosed({$timer.Stop();$timer.Dispose()})
Filter-Agents
$timer.Start()
if ($SmokeTest) {
    $form.Add_Shown({
        try {
            $search.Text='CATO'
            if ($runtime.Text -ne 'Codex Astra' -or $runtime.Enabled) {throw 'CATO policy UI failed'}
            $search.Text='CARL'
            if ($runtime.Items.Count -ne 2) {throw 'Runtime selection failed'}
            $task.Text='Test task'
            if ($resume.Enabled) {throw 'Resume must refuse task text'}
            $task.Clear(); $search.Text='no-such-agent-987654'
            if ($start.Enabled -or $resume.Enabled) {throw 'Empty search still launches'}
            $search.Clear(); $search.Text='CARL'
            $form.Refresh()
            $bitmap=New-Object Drawing.Bitmap($form.Width,$form.Height)
            $form.DrawToBitmap($bitmap,(New-Object Drawing.Rectangle(0,0,$form.Width,$form.Height)))
            $bitmap.Save((Join-Path $data.directory 'preview.png')); $bitmap.Dispose()
            @{ok=$true;checks='Native form, search, runtime policy, task/resume exclusion, empty selection'} |
                ConvertTo-Json | Set-Content (Join-Path $data.directory 'smoke.json')
        } catch {
            @{ok=$false;error=$_.Exception.Message} | ConvertTo-Json | Set-Content (Join-Path $data.directory 'smoke.json')
        } finally {$form.Close()}
    })
}
[void]$form.ShowDialog()
$form.Dispose()

param([Parameter(Mandatory=$true)][string]$DataFile, [switch]$SmokeTest)
$ErrorActionPreference = 'Stop'
trap {
    if (-not $SmokeTest) {[void][System.Windows.Forms.MessageBox]::Show($_.Exception.Message,'Agent Launcher')}
    Write-Error $_ -ErrorAction Continue
    exit 2
}
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
[System.Windows.Forms.Application]::EnableVisualStyles()
$data = Get-Content -LiteralPath $DataFile -Raw | ConvertFrom-Json
$script:busy=$false; $script:process=$null; $script:selected=$null
$script:loading=$false; $script:filtering=$false
$script:checked=@{}; $script:settings=@{}
$script:queue=New-Object Collections.Queue
$script:active=$null; $script:completed=0; $script:failed=0
foreach ($entry in $data.agents) {
    $script:settings[$entry.name]=@{runtime=$entry.default_runtime;task=$null}
}
$bg=[Drawing.Color]::FromArgb(242,244,248)
$ink=[Drawing.Color]::FromArgb(29,40,57)
$muted=[Drawing.Color]::FromArgb(87,100,120)
$accent=[Drawing.Color]::FromArgb(42,91,164)
$form=New-Object Windows.Forms.Form
$form.Text='Agent Launcher'; $form.ClientSize=New-Object Drawing.Size(1100,720)
$form.MinimumSize=New-Object Drawing.Size(1116,759)
$form.StartPosition='CenterScreen'; $form.BackColor=$bg; $form.ForeColor=$ink
$form.Font=New-Object Drawing.Font('Segoe UI',10); $form.AutoScaleMode='Dpi'
function Label($text,$x,$y,$width,$height,$size=10) {
    $c=New-Object Windows.Forms.Label
    $c.Text=$text; $c.SetBounds($x,$y,$width,$height)
    $c.Font=New-Object Drawing.Font('Segoe UI',$size); $form.Controls.Add($c)
    return $c
}
function Button($text,$x,$y,$width) {
    $c=New-Object Windows.Forms.Button
    $c.Text=$text; $c.SetBounds($x,$y,$width,40)
    $c.FlatStyle='Flat'; $c.FlatAppearance.BorderSize=0
    $c.BackColor=[Drawing.Color]::White; $c.ForeColor=$ink
    $c.Cursor='Hand'; $form.Controls.Add($c)
    return $c
}
$title=Label 'Your agent desk' 24 18 900 42 23
$subtitle=Label 'Browse a category. Check agents to launch together.' 26 65 1000 26
$subtitle.ForeColor=$muted
$categoryLabel=Label 'Categories' 26 111 224 26
$categories=New-Object Windows.Forms.ListBox
$categories.SetBounds(26,145,224,435); $categories.BorderStyle='None'
$categories.IntegralHeight=$false; $categories.DrawMode='OwnerDrawFixed'; $categories.ItemHeight=46
$categories.DisplayMember='Display'; $form.Controls.Add($categories)
[void]$categories.Items.Add([pscustomobject]@{Name='';Display='All agents'})
foreach ($g in ($data.agents | Select-Object -ExpandProperty group -Unique)) {
    [void]$categories.Items.Add([pscustomobject]@{Name=$g;Display=$g})
}
$categories.Add_DrawItem({
    param($sender,$e)
    if ($e.Index -lt 0) {return}
    $e.DrawBackground()
    $rect=New-Object Drawing.Rectangle(($e.Bounds.X+9),$e.Bounds.Y,($e.Bounds.Width-16),$e.Bounds.Height)
    [Windows.Forms.TextRenderer]::DrawText($e.Graphics,$sender.Items[$e.Index].Display,$sender.Font,$rect,$e.ForeColor,([Windows.Forms.TextFormatFlags]::WordBreak -bor [Windows.Forms.TextFormatFlags]::VerticalCenter))
    $e.DrawFocusRectangle()
})
$searchLabel=Label 'Search in category' 270 111 220 26
$search=New-Object Windows.Forms.TextBox
$search.SetBounds(270,145,220,30); $form.Controls.Add($search)
$list=New-Object Windows.Forms.CheckedListBox
$list.SetBounds(270,186,220,334); $list.IntegralHeight=$false
$list.BorderStyle='None'; $list.Font=New-Object Drawing.Font('Segoe UI',11)
$list.CheckOnClick=$false; $list.DisplayMember='Display'; $form.Controls.Add($list)
$count=Label '' 270 532 220 45
$count.ForeColor=$muted
$batch=Button 'Review selected (0)' 270 582 220
$batch.BackColor=$accent; $batch.ForeColor=[Drawing.Color]::White
$clear=Button 'Clear selection' 26 582 224
$name=Label 'Select an agent' 520 107 554 38 21
$purpose=Label '' 522 151 550 52 11
$purpose.ForeColor=$muted
$group=Label '' 522 206 550 24
$group.ForeColor=$muted
$runtimeLabel=Label 'Run this agent with' 522 242 550 25
$runtime=New-Object Windows.Forms.ComboBox
$runtime.SetBounds(522,271,550,32); $runtime.DropDownStyle='DropDownList'
$form.Controls.Add($runtime)
$taskLabel=Label 'Optional task for this agent' 522 313 550 25
$task=New-Object Windows.Forms.TextBox
$task.SetBounds(522,343,550,75); $task.Multiline=$true; $task.AcceptsReturn=$true
$task.ScrollBars='Vertical'; $form.Controls.Add($task)
$start=Button 'Start this agent' 522 432 265
$resume=Button 'Resume this agent...' 803 432 269
$hint=Label 'Use checkboxes for a batch; Start and Resume use the highlighted agent.' 522 480 550 35 9
$hint.ForeColor=$muted
$status=Label 'Ready. Each conversation opens in its own terminal.' 522 519 550 25 9
$status.ForeColor=$muted
$results=New-Object Windows.Forms.TextBox
$results.SetBounds(522,550,550,72); $results.Multiline=$true; $results.ReadOnly=$true
$results.ScrollBars='Vertical'; $results.BackColor=[Drawing.Color]::White
$results.Font=New-Object Drawing.Font('Segoe UI',9); $form.Controls.Add($results)
$stop=Button 'Stop remaining' 26 582 224
$stop.Visible=$false
foreach ($control in @($name,$purpose,$group,$runtimeLabel,$runtime,$taskLabel,$task,$hint,$status,$results)) {$control.Anchor='Top,Left,Right'}
$tooltip=New-Object Windows.Forms.ToolTip
$tooltip.SetToolTip($list,'Click a name for details. Click its checkbox, or press Space, to include it in a batch.')
$tooltip.SetToolTip($task,'Saved for this agent while the app is open. Applies only to new conversations.')

# Saved groups toolbar and editable task presets.
foreach ($c in @($categoryLabel,$categories,$searchLabel,$search,$list,$count,$batch,$clear,$name,$purpose,$group,$runtimeLabel,$runtime,$stop)) {$c.Top+=54}
$taskLabel.Top=429; $task.Top=453; $task.Height=70
$start.Top=537; $resume.Top=537; $hint.Top=585; $status.Top=623
$results.Top=650; $results.Height=50
$savedLabel=Label 'Saved groups' 26 110 120 28
$savedGroups=New-Object Windows.Forms.ComboBox
$savedGroups.SetBounds(150,105,360,32); $savedGroups.DropDownStyle='DropDown'; $form.Controls.Add($savedGroups)
$loadGroup=Button 'Load' 526 102 100
$saveGroup=Button 'Save selected' 640 102 170
$deleteGroup=Button 'Delete group' 824 102 150
$presetLabel=Label 'Task preset' 522 365 550 23
$preset=New-Object Windows.Forms.ComboBox
$preset.SetBounds(522,391,300,30); $preset.DropDownStyle='DropDownList'; $form.Controls.Add($preset)
$usePreset=Button 'Use here' 832 387 110
$batchPreset=Button 'Use for checked' 952 387 120
$tooltip.SetToolTip($savedGroups,'Choose a saved group, or type a name and Save selected. Groups save agents and runtimes; task text stays in this window.')
$tooltip.SetToolTip($usePreset,'Put this preset into the highlighted agent task box; you can edit it before launch.')
$tooltip.SetToolTip($batchPreset,'Put this preset into every checked agent task box, including hidden selections.')

# Groups are personal preferences; never commands, tasks, or a fleet roster.
$script:groups=@(); $script:groupsVersion=''; $script:groupsHealthy=$true
$preferencesFolder=Join-Path ([Environment]::GetFolderPath('LocalApplicationData')) 'ResearchAgentLauncher'
if ($SmokeTest -or $data.test_mode) {
    $preferencesFolder=Join-Path ([IO.Path]::GetTempPath()) ('AgentLauncherTest-'+[Guid]::NewGuid().ToString('N'))
}
$script:groupsPath=Join-Path $preferencesFolder 'groups.json'
function Read-Groups {
    $text=''
    if ([IO.File]::Exists($script:groupsPath)) {$text=[IO.File]::ReadAllText($script:groupsPath)}
    $found=@()
    if ($text) {
        $value=$text | ConvertFrom-Json
        if ($value.version -ne 1 -or $value.groups -isnot [Array]) {throw 'Saved groups file has an unsupported format. It was not changed.'}
        $names=@{}
        foreach ($g in $value.groups) {
            if ($g.name -isnot [string] -or [string]::IsNullOrWhiteSpace($g.name) -or $g.name.Length -gt 60 -or $g.name -match '[\x00-\x1f]' -or $names.ContainsKey($g.name)) {throw 'Saved groups contain an invalid or duplicate name. The file was not changed.'}
            $names[$g.name]=$true
            if ($g.members -isnot [Array] -or $g.members.Count -eq 0) {throw 'Saved group has no valid member list. The file was not changed.'}
            $members=@{}
            foreach ($m in $g.members) {
                if ($m.name -isnot [string] -or $m.name -notmatch '^[A-Z][A-Z0-9_-]*$' -or $m.runtime -notin @('sol','claude','astra') -or $members.ContainsKey($m.name)) {throw 'Saved group has an invalid or duplicate agent. The file was not changed.'}
                $members[$m.name]=$true
            }
            $found+=$g
        }
    } elseif ([IO.File]::Exists($script:groupsPath)) {throw 'Saved groups file is empty. It was not changed.'}
    $script:groups=@($found); $script:groupsVersion=$text; $script:groupsHealthy=$true
}
function Write-Groups($groups) {
    if (-not $script:groupsHealthy) {throw 'Fix or restore the saved groups file before saving. Your existing file has been preserved.'}
    $hash=[Security.Cryptography.SHA256]::Create()
    $key=[BitConverter]::ToString($hash.ComputeHash([Text.Encoding]::UTF8.GetBytes($script:groupsPath))).Replace('-','')
    $hash.Dispose()
    $mutex=New-Object Threading.Mutex($false,('Local\AgentLauncherGroups-'+$key))
    $locked=$false
    try {
        try {$locked=$mutex.WaitOne(1500)} catch [Threading.AbandonedMutexException] {$locked=$true}
        if (-not $locked) {throw 'Another launcher is saving groups. Try again shortly.'}
        $current=''
        if ([IO.File]::Exists($script:groupsPath)) {$current=[IO.File]::ReadAllText($script:groupsPath)}
        if ($current -cne $script:groupsVersion) {throw 'Saved groups changed in another window. Load the current groups before saving again.'}
        [void][IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($script:groupsPath))
        $items=@(); if ($null -ne $groups) {$items=@($groups)}
        $text=@{version=1;groups=$items} | ConvertTo-Json -Depth 8
        $temporary=$script:groupsPath+'.'+[Guid]::NewGuid().ToString('N')+'.tmp'
        [IO.File]::WriteAllText($temporary,$text,(New-Object Text.UTF8Encoding($false)))
        if ([IO.File]::Exists($script:groupsPath)) {[IO.File]::Replace($temporary,$script:groupsPath,($script:groupsPath+'.previous'))} else {[IO.File]::Move($temporary,$script:groupsPath)}
        Read-Groups
    } finally {
        if ($locked) {$mutex.ReleaseMutex()}
        $mutex.Dispose()
    }
}
function Refresh-Groups {
    $text=$savedGroups.Text
    $savedGroups.Items.Clear()
    foreach ($g in $script:groups) {[void]$savedGroups.Items.Add($g.name)}
    $savedGroups.Text=$text
}
function Group-From-Selection($groupName) {
    $groupName=$groupName.Trim()
    if (-not $groupName -or $groupName.Length -gt 60 -or $groupName -match '[\x00-\x1f]') {throw 'Enter a group name of 1 to 60 characters.'}
    $members=@(foreach ($entry in $data.agents) {
        if ($script:checked.ContainsKey($entry.name)) {
            @{name=$entry.name;runtime=$script:settings[$entry.name].runtime}
        }
    })
    if ($members.Count -eq 0) {throw 'Check at least one agent before saving a group.'}
    return @{name=$groupName;members=$members}
}
function Apply-Group($g) {
    # Validate everything before replacing the current selection/settings.
    foreach ($member in $g.members) {
        $entry=@($data.agents | Where-Object {$_.name -eq $member.name})
        if ($entry.Count -ne 1) {throw ('This group includes '+$member.name+', which is no longer configured. Your current selection was kept.')}
        $allowed=@('sol','claude')
        if ($entry[0].kind -eq 'cato') {$allowed=@('astra')}
        if ($member.runtime -notin $allowed) {throw ('Unsupported saved runtime for '+$member.name+'. Your current selection was kept.')}
    }
    $script:checked.Clear()
    foreach ($member in $g.members) {
        $script:checked[$member.name]=$true
        $script:settings[$member.name].runtime=$member.runtime
    }
    $categories.SelectedIndex=0; $search.Clear(); Filter-Agents
    $status.Text='Loaded '+$g.name+'. Review selected when ready.'
}
# Confirmation is injectable only by the isolated native control tests.
$script:confirmChange={param($message,$title)
    return [Windows.Forms.MessageBox]::Show($message,$title,'YesNo','Question','Button2') -eq 'Yes'
}
function Save-Group {
    try {
        $g=Group-From-Selection $savedGroups.Text
        if (@($script:groups | Where-Object {$_.name -eq $g.name}).Count -gt 0) {
            if (-not (& $script:confirmChange ('Replace the saved agents and runtimes in '+$g.name+'?') 'Save group')) {return}
        }
        Write-Groups @(@($script:groups | Where-Object {$_.name -ne $g.name})+$g)
        Refresh-Groups; $savedGroups.Text=$g.name
        $status.Text='Saved '+$g.name+'. Groups remember agents and runtimes.'
    } catch {$status.Text=$_.Exception.Message;$tooltip.SetToolTip($status,$status.Text)}
}
function Load-Group {
    try {
        Read-Groups; Refresh-Groups
        $matches=@($script:groups | Where-Object {$_.name -eq $savedGroups.Text.Trim()})
        if ($matches.Count -ne 1) {throw 'Choose a saved group to load.'}
        Apply-Group $matches[0]
    } catch {$status.Text=$_.Exception.Message;$tooltip.SetToolTip($status,$status.Text)}
}
function Delete-Group {
    try {
        $matches=@($script:groups | Where-Object {$_.name -eq $savedGroups.Text.Trim()})
        if ($matches.Count -ne 1) {throw 'Choose a saved group to delete.'}
        if (-not (& $script:confirmChange ('Delete saved group '+$matches[0].name+'?') 'Delete group')) {return}
        Write-Groups @($script:groups | Where-Object {$_.name -ne $matches[0].name})
        $savedGroups.Text='';Refresh-Groups
        $status.Text='Saved group deleted. No agent or conversation was removed.'
    } catch {$status.Text=$_.Exception.Message;$tooltip.SetToolTip($status,$status.Text)}
}
$presets=@(
    @{name='Orient and report status';text='Follow your startup instructions. Recover current work, approvals, and unresolved conditions. Give Will a short status and suggested next step. Do not begin unassigned work.'},
    @{name='Continue approved work';text='Follow your startup instructions and recover the current assignment, existing approvals, and unresolved conditions. Continue only work already authorized and currently in scope. Preserve all approval conditions; ask Will if the applicable assignment or authority is unclear. Report the result and next stopping point.'},
    @{name='Prepare handoff';text='Follow your startup instructions and recover current work and approvals. Prepare your normal handoff and closeout for the existing assignment. Preserve unfinished work, blockers, approval conditions, and a clear resume point. Do not start new research or unrelated pending work.'}
)
function Apply-Preset($toChecked) {
    if ($script:busy -or $preset.SelectedIndex -lt 0) {return}
    $names=@()
    if ($toChecked) {$names=@($script:checked.Keys)} elseif ($script:selected) {$names=@($script:selected.name)}
    if ($names.Count -eq 0) {return}
    $text=$presets[$preset.SelectedIndex].text
    $replace=@($names | Where-Object {-not [string]::IsNullOrWhiteSpace($script:settings[$_].task) -and $script:settings[$_].task -cne $text})
    if ($replace.Count -gt 0) {
        $message='Replace existing task text for: '+($replace -join ', ')+'?'
        if (-not (& $script:confirmChange $message 'Apply task preset')) {return}
    }
    foreach ($key in $names) {$script:settings[$key].task=$text}
    Select-Agent
    $status.Text='Preset applied to '+$names.Count+' agent(s). Edit the task text as needed.'
}

function Update-Buttons {
    $ready=($null -ne $script:selected -and -not $script:busy)
    $start.Enabled=$ready
    $resume.Enabled=($ready -and [string]::IsNullOrWhiteSpace($task.Text))
    $runtime.Enabled=($ready -and $script:selected.kind -ne 'cato')
    $task.Enabled=$ready
    $search.Enabled=-not $script:busy; $list.Enabled=-not $script:busy; $categories.Enabled=-not $script:busy
    $batch.Enabled=($script:checked.Count -gt 0 -and -not $script:busy)
    $batch.Text='Review selected ('+$script:checked.Count+')'
    $clear.Enabled=($script:checked.Count -gt 0 -and -not $script:busy)
    $clear.Visible=-not $script:busy; $stop.Visible=$script:busy
    $stop.Enabled=($script:queue.Count -gt 0)
    $count.Text=[string]$list.Items.Count+' shown / '+$script:checked.Count+' selected overall'
    $savedGroups.Enabled=-not $script:busy; $loadGroup.Enabled=-not $script:busy
    $saveGroup.Enabled=($script:checked.Count -gt 0 -and -not $script:busy -and $script:groupsHealthy)
    $deleteGroup.Enabled=(-not $script:busy -and $script:groupsHealthy)
    $preset.Enabled=-not $script:busy; $usePreset.Enabled=$ready
    $batchPreset.Enabled=($script:checked.Count -gt 0 -and -not $script:busy)
}
function Save-Settings {
    if ($script:loading -or $null -eq $script:selected) {return}
    $value='sol'
    if ($runtime.Text -eq 'Claude') {$value='claude'}
    if ($runtime.Text -eq 'Codex Astra') {$value='astra'}
    $script:settings[$script:selected.name]=@{runtime=$value;task=$task.Text}
    Update-Buttons
}
function Select-Agent {
    if ($script:filtering) {return}
    $script:loading=$true
    try {
        $runtime.Items.Clear()
        if ($null -eq $list.SelectedItem) {
            $script:selected=$null; $name.Text='No matching agents'; $purpose.Text='Try another name or category.'
            $group.Text=''; $task.Text=''; return
        }
        $script:selected=$list.SelectedItem.Entry
        $name.Text=$script:selected.name; $purpose.Text=$script:selected.purpose; $group.Text=$script:selected.group
        $setting=$script:settings[$script:selected.name]
        if ($script:selected.kind -eq 'cato') {
            [void]$runtime.Items.Add('Codex Astra'); $runtime.SelectedIndex=0
        } else {
            [void]$runtime.Items.Add('Codex Sol'); [void]$runtime.Items.Add('Claude'); $runtime.SelectedIndex=0
            if ($setting.runtime -eq 'claude') {$runtime.SelectedIndex=1}
        }
        $task.Text=[string]$setting.task
        $status.Text='Ready. Each conversation opens in its own terminal.'
        if ($script:selected.error) {$status.Text=$script:selected.error}
        $tooltip.SetToolTip($status,$status.Text); $tooltip.SetToolTip($name,$script:selected.folder)
    } finally {$script:loading=$false; Update-Buttons}
}
function Filter-Agents {
    $previous=$null
    if ($script:selected) {$previous=$script:selected.name}
    $query=$search.Text.Trim(); $category=''
    if ($categories.SelectedItem) {$category=$categories.SelectedItem.Name}
    $script:filtering=$true
    $list.BeginUpdate()
    try {
        $list.Items.Clear()
        foreach ($entry in $data.agents) {
            $haystack=$entry.name+' '+$entry.purpose+' '+$entry.group
            if (($category -eq '' -or $category -eq $entry.group) -and $haystack.IndexOf($query,[StringComparison]::OrdinalIgnoreCase) -ge 0) {
                $display=$entry.name
                if ($entry.error) {$display+=' (check setup)'}
                [void]$list.Items.Add([pscustomobject]@{Display=$display;Entry=$entry},$script:checked.ContainsKey($entry.name))
            }
        }
        if ($list.Items.Count -gt 0) {
            $list.SelectedIndex=0
            for ($i=0;$i -lt $list.Items.Count;$i++) {
                if ($list.Items[$i].Entry.name -eq $previous) {$list.SelectedIndex=$i;break}
            }
        }
    } finally {$list.EndUpdate();$script:filtering=$false}
    Select-Agent
}
function Request-For($entry,$action) {
    $setting=$script:settings[$entry.name]
    $text=$null
    if (-not [string]::IsNullOrWhiteSpace($setting.task)) {$text=$setting.task}
    return @{name=$entry.name;runtime=$setting.runtime;action=$action;task=$text}
}
function Selected-Requests {
    foreach ($entry in $data.agents) {
        if ($script:checked.ContainsKey($entry.name)) {Request-For $entry 'new'}
    }
}
function Preview-Text($items) {
    $lines=New-Object Collections.Generic.List[string]
    foreach ($item in $items) {
        $label=@{sol='Codex Sol';claude='Claude';astra='Codex Astra'}[$item.runtime]
        $lines.Add($item.name+'  |  '+$label)
        if ($item.task) {$lines.Add('Task: '+$item.task)} else {$lines.Add('Task: follow the agent startup instructions')}
        $lines.Add('')
    }
    return $lines -join "`r`n"
}
function Confirm-Batch($items) {
    $dialog=New-Object Windows.Forms.Form
    $dialog.Text='Review selected agents'; $dialog.ClientSize=New-Object Drawing.Size(650,440)
    $dialog.StartPosition='CenterParent'; $dialog.Font=$form.Font; $dialog.BackColor=$bg
    $dialog.FormBorderStyle='FixedDialog'; $dialog.MaximizeBox=$false; $dialog.MinimizeBox=$false
    $heading=New-Object Windows.Forms.Label
    $heading.Text='Start '+$items.Count+' new conversations in separate windows'; $heading.SetBounds(20,20,610,30)
    $preview=New-Object Windows.Forms.TextBox
    $preview.Multiline=$true; $preview.ReadOnly=$true; $preview.ScrollBars='Vertical'
    $preview.SetBounds(20,60,610,305); $preview.Text=Preview-Text $items
    $launch=New-Object Windows.Forms.Button
    $launch.Text='Launch selected'; $launch.SetBounds(430,382,200,38); $launch.DialogResult='OK'
    $cancel=New-Object Windows.Forms.Button
    $cancel.Text='Cancel'; $cancel.SetBounds(280,382,130,38); $cancel.DialogResult='Cancel'
    $dialog.Controls.AddRange(@($heading,$preview,$launch,$cancel)); $dialog.CancelButton=$cancel
    # Enter does not start a batch implicitly; the launch button must be chosen.
    $answer=$dialog.ShowDialog($form); $dialog.Dispose()
    return $answer -eq [Windows.Forms.DialogResult]::OK
}
function Log-Result($text) {
    $results.AppendText($text+"`r`n")
    $results.SelectionStart=$results.TextLength; $results.ScrollToCaret()
}
function Begin-Requests($items) {
    if ($script:busy -or $items.Count -eq 0) {return}
    $script:busy=$true; $script:completed=0; $script:failed=0
    $results.Clear(); $script:queue.Clear()
    foreach ($item in $items) {$script:queue.Enqueue($item)}
    Start-Next
}
function Finish-Current($ok,$message) {
    $prefix='Opened'
    if (-not $ok) {$prefix='Not confirmed';$script:failed++} else {
        $script:checked.Remove($script:active.name)
    }
    Log-Result ($prefix+' - '+$script:active.name+': '+$message)
    $script:completed++; $script:active=$null; $script:process=$null
}
function Start-Next {
    if ($script:queue.Count -eq 0) {
        $script:busy=$false
        $status.Text='Finished: '+$script:completed+' attempted, '+$script:failed+' not confirmed. See results below.'
        $saved=$status.Text
        Filter-Agents
        $status.Text=$saved
        Update-Buttons
        return
    }
    $script:active=$script:queue.Dequeue()
    Update-Buttons
    try {
        $id=[Guid]::NewGuid().ToString('N')
        $request=Join-Path $data.directory ($id+'.json')
        $script:resultFile=Join-Path $data.directory ($id+'.result.json')
        $script:active | ConvertTo-Json | Set-Content -LiteralPath $request -Encoding UTF8
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
        $status.Text='Opening '+$script:active.name+'; '+$script:queue.Count+' remaining...'
    } catch {Finish-Current $false $_.Exception.Message; Start-Next}
}
function Stop-Remaining {
    while ($script:queue.Count -gt 0) {
        $item=$script:queue.Dequeue()
        Log-Result ('Cancelled - '+$item.name+': not started')
    }
    if ($script:busy) {$status.Text='Remaining agents cancelled. The current request may still finish.'}
    Update-Buttons
}
function Begin-Launch($action) {
    if ($script:busy -or $null -eq $script:selected) {return}
    if ($action -eq 'resume' -and -not [string]::IsNullOrWhiteSpace($task.Text)) {return}
    Begin-Requests @(Request-For $script:selected $action)
}
$timer=New-Object Windows.Forms.Timer
$timer.Interval=200
$timer.Add_Tick({
    if (-not $script:busy -or $null -eq $script:process) {return}
    try {
        if (Test-Path -LiteralPath $script:resultFile) {
            $result=Get-Content -LiteralPath $script:resultFile -Raw | ConvertFrom-Json
            Finish-Current $result.ok $result.message
            Start-Next
        } elseif ($script:process.HasExited -or ([DateTime]::UtcNow-$script:started).TotalSeconds -gt 40) {
            $message='Startup was not confirmed. Check its terminal before trying again.'
            if ($script:process.HasExited) {
                $detail=($script:errorRead.Result+' '+$script:outputRead.Result).Trim()
                if ($detail) {$message=$detail}
            }
            Finish-Current $false $message
            Start-Next
        }
    } catch {Finish-Current $false $_.Exception.Message; Start-Next}
})
$search.Add_TextChanged({Filter-Agents})
$categories.Add_SelectedIndexChanged({Filter-Agents})
$list.Add_SelectedIndexChanged({Select-Agent})
$list.Add_ItemCheck({
    param($sender,$e)
    if ($script:filtering) {return}
    $key=$list.Items[$e.Index].Entry.name
    if ($e.NewValue -eq [Windows.Forms.CheckState]::Checked) {$script:checked[$key]=$true} else {$script:checked.Remove($key)}
    Update-Buttons
})
$runtime.Add_SelectedIndexChanged({Save-Settings})
$task.Add_TextChanged({Save-Settings})
$clear.Add_Click({$script:checked.Clear();Filter-Agents})
$stop.Add_Click({Stop-Remaining})
$batch.Add_Click({
    $items=@(Selected-Requests)
    if ($items.Count -gt 0 -and (Confirm-Batch $items)) {Begin-Requests $items}
})
$start.Add_Click({Begin-Launch 'new'})
$resume.Add_Click({Begin-Launch 'resume'})
$form.Add_FormClosing({
    if ($script:busy -and $script:queue.Count -gt 0) {
        Stop-Remaining
    }
})
$form.Add_FormClosed({$timer.Stop();$timer.Dispose()})
$saveGroup.Add_Click({Save-Group})
$loadGroup.Add_Click({Load-Group})
$deleteGroup.Add_Click({Delete-Group})
$usePreset.Add_Click({Apply-Preset $false})
$batchPreset.Add_Click({Apply-Preset $true})
foreach ($p in $presets) {[void]$preset.Items.Add($p.name)}
$preset.SelectedIndex=0
$categories.SelectedIndex=0
try {Read-Groups; Refresh-Groups} catch {
    $script:groupsHealthy=$false
    $status.Text='Cannot read saved groups. See results below.'
    Log-Result ($_.Exception.Message+' File: '+$script:groupsPath)
}
Update-Buttons
$timer.Start()
if ($SmokeTest) {
    $form.Add_Shown({
        try {
            $search.Text='CATO'
            if ($runtime.Text -ne 'Codex Astra' -or $runtime.Enabled) {throw 'CATO policy UI failed'}
            $list.SetItemChecked(0,$true)
            $search.Text='CARL'; $runtime.SelectedIndex=1; $task.Text='Only CARL receives this task'
            if ($resume.Enabled) {throw 'Resume must refuse task text'}
            $list.SetItemChecked(0,$true)
            $categories.SelectedIndex=2; $search.Clear()
            if ($list.Items.Count -eq 0) {throw 'Category is empty'}
            foreach ($item in $list.Items) {
                if ($item.Entry.group -ne $categories.SelectedItem.Name) {throw 'Category contains another group'}
            }
            if ($script:checked.Count -ne 2) {throw 'Filtering lost checked agents'}
            $items=@(Selected-Requests)
            if ($items.Count -ne 2 -or (Preview-Text $items) -notmatch 'Codex Astra') {throw 'Preview lost a hidden selection'}
            $carl=@($items | Where-Object {$_.name -eq 'CARL'})[0]
            if ($carl.runtime -ne 'claude' -or $carl.task -ne 'Only CARL receives this task') {throw 'Per-agent settings were lost'}
            $categories.SelectedIndex=0; $search.Text='CARL'
            if ($runtime.Text -ne 'Claude' -or $task.Text -ne $carl.task) {throw 'Settings did not restore'}
            $search.Text='no-such-agent-987654'
            if ($start.Enabled -or $resume.Enabled -or -not $batch.Enabled) {throw 'Empty search/hidden batch behavior failed'}
            $clear.PerformClick()
            if ($script:checked.Count -ne 0 -or $batch.Enabled) {throw 'Clear selection failed'}
            $script:queue.Enqueue(@{name='NOT_STARTED_TEST'})
            Stop-Remaining
            if ($script:queue.Count -ne 0 -or $results.Text -notmatch 'Cancelled - NOT_STARTED_TEST') {throw 'Stop remaining failed'}
            $results.Clear()
            $search.Clear(); $categories.SelectedIndex=2; $search.Text='CARL'
            $list.SetItemChecked(0,$true); $list.SetItemChecked(1,$true); $list.SetItemChecked(2,$true)
            # Save/reload real preference files in an isolated Windows temp folder.
            $savedGroups.Text='Consumer review'; $saveGroup.PerformClick()
            if (-not [IO.File]::Exists($script:groupsPath)) {throw ('Group save failed: '+$status.Text)}
            $original=[IO.File]::ReadAllText($script:groupsPath)
            if ($original -match 'Only CARL receives') {throw 'Group persisted task text'}
            $clear.PerformClick(); $script:settings['CARL'].runtime='sol'
            $script:groups=@(); Read-Groups; Refresh-Groups; $loadGroup.PerformClick()
            if ($script:checked.Count -ne 3 -or $script:settings['CARL'].runtime -ne 'claude') {throw 'Saved group failed to reload'}
            $failed=$false
            try {Apply-Group @{name='Invalid';members=@(@{name='CARL';runtime='sol'},@{name='MISSING_TEST';runtime='sol'})}} catch {$failed=$true}
            if (-not $failed -or $script:checked.Count -ne 3 -or $script:settings['CARL'].runtime -ne 'claude') {throw 'Stale group partially changed settings'}
            $failed=$false
            try {Apply-Group @{name='Invalid';members=@(@{name='CATO';runtime='sol'})}} catch {$failed=$true}
            if (-not $failed) {throw 'Saved group changed CATO policy'}
            # Simulate another window committing after this one read the file.
            [IO.File]::WriteAllText($script:groupsPath,$original+"`r`n")
            $failed=$false
            try {Write-Groups $script:groups} catch {$failed=$true}
            if (-not $failed -or [IO.File]::ReadAllText($script:groupsPath) -cne ($original+"`r`n")) {throw 'Concurrent group update was overwritten'}
            Read-Groups; Write-Groups $script:groups
            # Invalid/empty preference files must remain intact.
            foreach ($bad in @('{broken','')) {
                [IO.File]::WriteAllText($script:groupsPath,$bad)
                $failed=$false
                try {Read-Groups} catch {$failed=$true}
                if (-not $failed -or [IO.File]::ReadAllText($script:groupsPath) -cne $bad) {throw 'Corrupt preference file was not preserved'}
            }
            [IO.File]::WriteAllText($script:groupsPath,$original); Read-Groups
            $saved=@($script:groups); Write-Groups @()
            if ($script:groups.Count -ne 0) {throw 'Deleting last group failed'}
            Write-Groups $saved; Refresh-Groups
            $search.Text='CARL'; $task.Clear()
            $preset.SelectedIndex=0; $usePreset.PerformClick()
            if ($task.Text -ne $presets[0].text -or $resume.Enabled) {throw 'Current-agent preset failed'}
            $task.Text+=' Editable detail.'
            if ($script:settings['CARL'].task -notmatch 'Editable detail') {throw 'Preset text was not editable'}
            foreach ($key in @($script:checked.Keys)) {$script:settings[$key].task=''}
            Select-Agent; $preset.SelectedIndex=1; $batchPreset.PerformClick()
            foreach ($key in $script:checked.Keys) {
                if ($script:settings[$key].task -ne $presets[1].text) {throw 'Checked-agent preset failed'}
            }
            $task.Clear(); $preset.SelectedIndex=2; $usePreset.PerformClick()
            if ($task.Text -ne $presets[2].text) {throw 'Handoff preset failed'}
            # Exercise both answers through the real handlers without pausing the test.
            $normalConfirm=$script:confirmChange
            $script:confirmChange={param($message,$title) return $false}
            $task.Text='Keep my wording'; $preset.SelectedIndex=0; $usePreset.PerformClick()
            if ($task.Text -ne 'Keep my wording') {throw 'Cancelled preset replaced task text'}
            $before=[IO.File]::ReadAllText($script:groupsPath)
            $saveGroup.PerformClick(); $deleteGroup.PerformClick()
            if ([IO.File]::ReadAllText($script:groupsPath) -cne $before) {throw 'Cancelled group edit changed disk'}
            $script:confirmChange={param($message,$title) return $true}
            $usePreset.PerformClick()
            if ($task.Text -ne $presets[0].text) {throw 'Confirmed preset replacement failed'}
            $runtime.SelectedIndex=0; $saveGroup.PerformClick()
            if ($script:groups[0].members[0].runtime -ne 'sol') {throw 'Confirmed saved-group update failed'}
            $deleteGroup.PerformClick()
            if ($script:groups.Count -ne 0) {throw 'Confirmed group deletion failed'}
            $savedGroups.Text='Consumer review'; $saveGroup.PerformClick()
            $script:confirmChange=$normalConfirm

            if (@(Get-ChildItem -LiteralPath $data.directory -Filter '*.claimed').Count -ne 0) {throw 'Saving/loading/presets started an agent'}
            $status.Text='Saved groups and editable task presets are ready.'
            $form.Refresh()
            $bitmap=New-Object Drawing.Bitmap($form.Width,$form.Height)
            $form.DrawToBitmap($bitmap,(New-Object Drawing.Rectangle(0,0,$form.Width,$form.Height)))
            $bitmap.Save((Join-Path $data.directory 'preview.png')); $bitmap.Dispose()
            @{ok=$true;checks='Categories, retained selection, per-agent runtime/task, hidden preview, CATO, resume, empty search, clear, stop remaining, saved groups, atomic persistence, concurrent/corrupt-file refusal, task presets'} | ConvertTo-Json | Set-Content -Encoding UTF8 (Join-Path $data.directory 'smoke.json')
        } catch {
            @{ok=$false;error=$_.Exception.Message} | ConvertTo-Json | Set-Content -Encoding UTF8 (Join-Path $data.directory 'smoke.json')
        } finally {$form.Close()}
    })
}
[void]$form.ShowDialog()
$form.Dispose()

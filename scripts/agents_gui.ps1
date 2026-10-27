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
$bg=[Drawing.Color]::FromArgb(11,23,42)
$surface=[Drawing.Color]::FromArgb(21,39,63)
$raised=[Drawing.Color]::FromArgb(32,54,87)
$ink=[Drawing.Color]::FromArgb(245,249,255)
$muted=[Drawing.Color]::FromArgb(178,196,217)
$accent=[Drawing.Color]::FromArgb(101,238,224)
$selection=[Drawing.Color]::FromArgb(23,70,83)
$border=[Drawing.Color]::FromArgb(54,82,109)
# Keep the native checked-list keyboard/events, painting only its appearance.
Add-Type -ReferencedAssemblies System.Windows.Forms,System.Drawing -TypeDefinition @'
using System;
using System.Drawing;
using System.Runtime.InteropServices;
using System.Windows.Forms;
public class LauncherAgentList : CheckedListBox {
    public Color AccentColor { get; set; }
    public Color SelectionColor { get; set; }
    public Color MutedColor { get; set; }
    protected override void OnDrawItem(DrawItemEventArgs e) {
        if (e.Index < 0 || e.Index >= Items.Count) return;
        bool selected = (e.State & DrawItemState.Selected) != 0;
        Color background = selected ? SelectionColor : BackColor;
        using (var brush = new SolidBrush(background)) e.Graphics.FillRectangle(brush, e.Bounds);
        int box = Math.Max(12, Math.Min(e.Bounds.Height - 6, Font.Height - 1));
        var bounds = new Rectangle(e.Bounds.Left + 6, e.Bounds.Top + (e.Bounds.Height - box) / 2, box, box);
        bool check = GetItemChecked(e.Index);
        if (check) {
            using (var brush = new SolidBrush(AccentColor)) e.Graphics.FillRectangle(brush, bounds);
            using (var pen = new Pen(BackColor, Math.Max(2, box / 7f))) {
                pen.StartCap = pen.EndCap = System.Drawing.Drawing2D.LineCap.Round;
                e.Graphics.DrawLines(pen, new PointF[] {
                    new PointF(bounds.Left + box * .22f, bounds.Top + box * .5f),
                    new PointF(bounds.Left + box * .43f, bounds.Top + box * .72f),
                    new PointF(bounds.Left + box * .8f, bounds.Top + box * .27f) });
            }
        } else {
            using (var pen = new Pen(MutedColor)) e.Graphics.DrawRectangle(pen, bounds);
        }
        var text = new Rectangle(bounds.Right + 8, e.Bounds.Top,
            Math.Max(0, e.Bounds.Right - bounds.Right - 12), e.Bounds.Height);
        TextRenderer.DrawText(e.Graphics, GetItemText(Items[e.Index]), Font, text, ForeColor,
            TextFormatFlags.VerticalCenter | TextFormatFlags.EndEllipsis | TextFormatFlags.NoPrefix);
        if ((e.State & DrawItemState.Focus) != 0)
            ControlPaint.DrawFocusRectangle(e.Graphics, e.Bounds, ForeColor, background);
    }
}
public class LauncherButton : Button {
    protected override void OnPaint(PaintEventArgs e) {
        if (Enabled) { base.OnPaint(e); return; }
        // The native disabled text color is nearly black on the navy theme.
        Color background = Color.FromArgb(11, 23, 42);
        Color text = Color.FromArgb(137, 158, 182);
        using (var brush = new SolidBrush(background)) e.Graphics.FillRectangle(brush, ClientRectangle);
        using (var pen = new Pen(Color.FromArgb(54, 82, 109)))
            e.Graphics.DrawRectangle(pen, 0, 0, Width - 1, Height - 1);
        TextRenderer.DrawText(e.Graphics, Text, Font, ClientRectangle, text,
            TextFormatFlags.HorizontalCenter | TextFormatFlags.VerticalCenter | TextFormatFlags.NoPrefix);
    }
}
public static class LauncherWindowTheme {
    [DllImport("dwmapi.dll")]
    public static extern int DwmSetWindowAttribute(IntPtr window, int attribute, ref int value, int size);
}
'@
$form=New-Object Windows.Forms.Form
$form.Text='Agent Launcher'; $form.ClientSize=New-Object Drawing.Size(1160,780)
$form.MinimumSize=New-Object Drawing.Size(1176,819)
$form.StartPosition='CenterScreen'; $form.BackColor=$bg; $form.ForeColor=$ink
$form.Font=New-Object Drawing.Font('Segoe UI',10); $form.AutoScaleMode='Dpi'
$iconPath=Join-Path $PSScriptRoot 'assets\agent-launcher.ico'
if (Test-Path -LiteralPath $iconPath) {$form.Icon=New-Object Drawing.Icon($iconPath)}
function Style-Button($control,$primary=$false) {
    $control.UseVisualStyleBackColor=$false; $control.FlatStyle='Flat'
    $control.FlatAppearance.BorderSize=1; $control.FlatAppearance.BorderColor=$border
    $control.BackColor=$raised; $control.ForeColor=$ink
    $control.FlatAppearance.MouseOverBackColor=[Drawing.Color]::FromArgb(45,71,107)
    $control.FlatAppearance.MouseDownBackColor=$selection
    if ($primary) {
        $control.BackColor=$accent; $control.ForeColor=$bg
        $control.FlatAppearance.BorderColor=$accent
        $control.FlatAppearance.MouseOverBackColor=[Drawing.Color]::FromArgb(142,247,236)
        $control.FlatAppearance.MouseDownBackColor=[Drawing.Color]::FromArgb(61,214,198)
    }
}
function Style-Input($control) {
    $control.BackColor=$surface; $control.ForeColor=$ink
    if ($control -is [Windows.Forms.ComboBox]) {
        $control.FlatStyle='Flat'; $control.DrawMode='OwnerDrawFixed'
        $control.Add_DrawItem({
            param($sender,$e)
            if ($e.Index -lt 0) {return}
            $fill=$surface
            if (($e.State -band [Windows.Forms.DrawItemState]::Selected) -ne 0) {$fill=$selection}
            $brush=New-Object Drawing.SolidBrush($fill)
            try {$e.Graphics.FillRectangle($brush,$e.Bounds)} finally {$brush.Dispose()}
            [Windows.Forms.TextRenderer]::DrawText($e.Graphics,[string]$sender.Items[$e.Index],$sender.Font,$e.Bounds,$ink,([Windows.Forms.TextFormatFlags]::VerticalCenter -bor [Windows.Forms.TextFormatFlags]::NoPrefix))
            $e.DrawFocusRectangle()
        })
    }
}
function Style-Menu($menu) {
    # System rendering honors the explicit colors instead of the light gradient.
    $menu.RenderMode='System'; $menu.BackColor=$surface; $menu.ForeColor=$ink
    $menu.ShowImageMargin=$false
}
function Label($text,$x,$y,$width,$height,$size=10) {
    $c=New-Object Windows.Forms.Label
    $c.Text=$text; $c.SetBounds($x,$y,$width,$height)
    $c.Font=New-Object Drawing.Font('Segoe UI',$size); $form.Controls.Add($c)
    return $c
}
function Button($text,$x,$y,$width) {
    $c=New-Object LauncherButton
    $c.Text=$text; $c.SetBounds($x,$y,$width,40)
    $c.UseMnemonic=$false
    Style-Button $c
    $c.Cursor='Hand'; $form.Controls.Add($c)
    return $c
}
$title=Label 'Agent Launcher' 24 18 900 42 23
$subtitle=Label 'Choose your agents, prepare their instructions, and open a conversation.' 26 65 1080 26
$subtitle.ForeColor=$muted
$savedLabel=Label 'My groups' 26 111 224 26
$savedGroups=New-Object Windows.Forms.ComboBox
$savedGroups.SetBounds(26,145,224,32); $savedGroups.DropDownStyle='DropDown'; $form.Controls.Add($savedGroups)
$loadGroup=Button 'Load group' 26 188 132
$groupActions=Button 'Manage...' 166 188 84
$groupMenu=New-Object Windows.Forms.ContextMenuStrip
$saveGroup=$groupMenu.Items.Add('Save selection to this group')
$saveAsGroup=$groupMenu.Items.Add('Save selection as a new group...')
$renameGroup=$groupMenu.Items.Add('Rename group...')
$deleteGroup=$groupMenu.Items.Add('Delete group...')
$categoryLabel=Label 'Categories' 26 250 224 26
$categories=New-Object Windows.Forms.ListBox
$categories.SetBounds(26,284,224,328); $categories.BorderStyle='None'
$categories.IntegralHeight=$false; $categories.DrawMode='OwnerDrawFixed'; $categories.ItemHeight=46
$categories.DisplayMember='Display'; $form.Controls.Add($categories)
[void]$categories.Items.Add([pscustomobject]@{Name='';Display='All agents'})
foreach ($g in ($data.agents | Select-Object -ExpandProperty group -Unique)) {
    [void]$categories.Items.Add([pscustomobject]@{Name=$g;Display=$g})
}
$categories.Add_DrawItem({
    param($sender,$e)
    if ($e.Index -lt 0) {return}
    $fill=$surface; $text=$muted
    if (($e.State -band [Windows.Forms.DrawItemState]::Selected) -ne 0) {$fill=$selection; $text=$accent}
    $brush=New-Object Drawing.SolidBrush($fill)
    try {$e.Graphics.FillRectangle($brush,$e.Bounds)} finally {$brush.Dispose()}
    $rect=New-Object Drawing.Rectangle(($e.Bounds.X+9),$e.Bounds.Y,($e.Bounds.Width-16),$e.Bounds.Height)
    [Windows.Forms.TextRenderer]::DrawText($e.Graphics,$sender.Items[$e.Index].Display,$sender.Font,$rect,$text,([Windows.Forms.TextFormatFlags]::WordBreak -bor [Windows.Forms.TextFormatFlags]::VerticalCenter))
    $e.DrawFocusRectangle()
})
$searchLabel=Label 'Find an agent' 274 111 238 26
$search=New-Object Windows.Forms.TextBox
$search.SetBounds(274,145,238,30); $form.Controls.Add($search)
$list=New-Object LauncherAgentList
$list.AccentColor=$accent; $list.SelectionColor=$selection; $list.MutedColor=$muted
$list.SetBounds(274,188,238,424); $list.IntegralHeight=$false
$list.BorderStyle='None'; $list.Font=New-Object Drawing.Font('Segoe UI',11)
$list.CheckOnClick=$false; $list.DisplayMember='Display'; $form.Controls.Add($list)
$count=Label '' 274 622 238 26 9
$count.ForeColor=$muted
$tray=New-Object Windows.Forms.Panel
$tray.Height=110; $tray.Dock='Bottom'; $tray.BackColor=$surface
$form.Controls.Add($tray)
$selectionLabel=Label 'Selected agents' 24 10 140 24
$tray.Controls.Add($selectionLabel)
$chips=New-Object Windows.Forms.FlowLayoutPanel
$chips.SetBounds(24,42,800,54); $chips.Anchor='Top,Left,Right'
$chips.WrapContents=$false; $chips.AutoScroll=$true; $tray.Controls.Add($chips)
$batch=Button 'Review & launch 0 agents' 856 42 280
$tray.Controls.Add($batch); $batch.Anchor='Top,Right'
Style-Button $batch $true
$clear=Button 'Clear all' 170 5 90
$clear.Height=30; $tray.Controls.Add($clear)
$name=Label 'Select an agent' 540 107 596 38 21
$name.ForeColor=$accent
$purpose=Label '' 542 151 594 48 11
$purpose.ForeColor=$muted
$group=Label '' 542 204 594 24
$group.ForeColor=$muted
$runtimeLabel=Label 'Runtime' 542 246 594 25
$runtime=New-Object Windows.Forms.ComboBox
$runtime.SetBounds(542,275,594,32); $runtime.DropDownStyle='DropDownList'
$form.Controls.Add($runtime)
$presetLabel=Label 'Instructions preset' 542 322 594 23
$preset=New-Object Windows.Forms.ComboBox
$preset.SetBounds(542,351,320,30); $preset.DropDownStyle='DropDownList'; $form.Controls.Add($preset)
$usePreset=Button 'Apply' 874 346 106
$presetActions=Button 'More...' 992 346 144
$presetMenu=New-Object Windows.Forms.ContextMenuStrip
$batchPreset=$presetMenu.Items.Add('Apply preset to all selected agents...')
$taskLabel=Label 'Instructions for this agent (optional)' 542 399 594 25
$task=New-Object Windows.Forms.TextBox
$task.SetBounds(542,429,594,84); $task.Multiline=$true; $task.AcceptsReturn=$true
$task.ScrollBars='Vertical'; $form.Controls.Add($task)
$start=Button 'New conversation' 542 529 288
$resume=Button 'Resume conversation...' 842 529 294
$hint=Label 'These buttons open the highlighted agent. Clear instructions to enable Resume.' 542 579 594 30 9
$hint.ForeColor=$muted
$status=Label 'Ready. Each conversation opens in its own terminal.' 542 616 594 22 9
$status.ForeColor=$muted
$details=New-Object Windows.Forms.LinkLabel
$details.Text='Show launch details'; $details.SetBounds(542,640,594,24)
$details.LinkColor=$accent; $details.ActiveLinkColor=$accent; $form.Controls.Add($details)
$details.VisitedLinkColor=$accent
$results=New-Object Windows.Forms.TextBox
$results.SetBounds(542,674,594,110); $results.Multiline=$true; $results.ReadOnly=$true
$results.Visible=$false
$results.ScrollBars='Vertical'
$results.Font=New-Object Drawing.Font('Segoe UI',9); $form.Controls.Add($results)
$stop=Button 'Stop remaining' 856 5 280
$stop.Height=30; $tray.Controls.Add($stop); $stop.Anchor='Top,Right'
$stop.Visible=$false
foreach ($control in @($name,$purpose,$group,$runtimeLabel,$runtime,$presetLabel,$taskLabel,$task,$hint,$status,$results,$details)) {$control.Anchor='Top,Left,Right'}
$resume.Anchor='Top,Right'; $usePreset.Anchor='Top,Right'; $presetActions.Anchor='Top,Right'
$preset.Anchor='Top,Left,Right'
$tooltip=New-Object Windows.Forms.ToolTip
$tooltip.SetToolTip($list,'Click a name for details. Click its checkbox, or press Space, to include it in a batch.')
$tooltip.SetToolTip($task,'Saved for this agent while the app is open. Applies only to new conversations.')
$tooltip.SetToolTip($savedGroups,'Choose a saved group to load it, or use Manage to save or rename one. Groups remember agents and runtimes.')
$tooltip.SetToolTip($usePreset,'Fill the highlighted agent instructions with this preset, then edit them as needed.')
$tooltip.SetToolTip($presetActions,'Apply the preset to all selected agents, including agents hidden by a filter.')
foreach ($input in @($savedGroups,$search,$runtime,$preset,$task,$results,$categories,$list)) {Style-Input $input}
foreach ($menu in @($groupMenu,$presetMenu)) {Style-Menu $menu}
$form.Add_Shown({
    # Older Windows builds can decline the title-bar hint; controls stay themed.
    try {
        $dark=1
        $code=[LauncherWindowTheme]::DwmSetWindowAttribute($form.Handle,20,[ref]$dark,4)
        if ($code -ne 0) {[void][LauncherWindowTheme]::DwmSetWindowAttribute($form.Handle,19,[ref]$dark,4)}
    } catch {}
})

function Set-DetailsVisible($visible) {
    if ($results.Visible -eq $visible) {return}
    $delta=130; if (-not $visible) {$delta=-130}
    $height=$form.ClientSize.Height+$delta
    $form.MinimumSize=New-Object Drawing.Size($form.MinimumSize.Width,($form.MinimumSize.Height+$delta))
    $form.ClientSize=New-Object Drawing.Size($form.ClientSize.Width,$height)
    $results.Visible=$visible
    $details.Text='Show launch details'; if ($visible) {$details.Text='Hide launch details'}
}
function Refresh-SelectionTray {
    # Rebuild only when membership changes, so task edits never steal chip focus.
    $members=@($data.agents | Where-Object {$script:checked.ContainsKey($_.name)})
    $signature=($members.name -join '|')
    if ($signature -cne $script:chipSignature) {
        $script:chipSignature=$signature
        $chips.SuspendLayout()
        try {
            while ($chips.Controls.Count -gt 0) {$chips.Controls[0].Dispose()}
            if ($members.Count -eq 0) {
                $empty=New-Object Windows.Forms.Label
                $empty.Text='Check agents in the list to prepare a batch.'
                $empty.AutoSize=$true; $empty.ForeColor=$muted; $empty.Margin=New-Object Windows.Forms.Padding(0,9,0,0)
                $chips.Controls.Add($empty)
            }
            foreach ($entry in $members) {
                $chip=New-Object LauncherButton
                $chip.Text=$entry.name+'  x'; $chip.Tag=$entry.name
                $chip.AutoSize=$true; $chip.Height=34; $chip.FlatStyle='Flat'
                Style-Button $chip
                $chip.ForeColor=$accent; $chip.Cursor='Hand'
                $chip.Margin=New-Object Windows.Forms.Padding(0,0,8,0)
                $chip.AccessibleName='Remove '+$entry.name+' from selection'
                $tooltip.SetToolTip($chip,'Remove '+$entry.name+' from the batch selection')
                $chip.Add_Click({param($sender,$e) $script:checked.Remove([string]$sender.Tag); Filter-Agents})
                $chips.Controls.Add($chip)
            }
        } finally {$chips.ResumeLayout()}
    }
    foreach ($chip in $chips.Controls) {$chip.Enabled=-not $script:busy}
}

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
function Ask-GroupName($title,$initial) {
    $dialog=New-Object Windows.Forms.Form
    $dialog.Text=$title; $dialog.ClientSize=New-Object Drawing.Size(420,140)
    $dialog.StartPosition='CenterParent'; $dialog.Font=$form.Font; $dialog.BackColor=$bg; $dialog.ForeColor=$ink; $dialog.Icon=$form.Icon
    $dialog.FormBorderStyle='FixedDialog'; $dialog.MaximizeBox=$false; $dialog.MinimizeBox=$false
    $input=New-Object Windows.Forms.TextBox
    $input.SetBounds(20,20,380,30); $input.Text=$initial; $input.MaxLength=60
    $ok=New-Object LauncherButton
    $ok.Text='Save'; $ok.SetBounds(290,80,110,36); $ok.DialogResult='OK'
    $cancel=New-Object LauncherButton
    $cancel.Text='Cancel'; $cancel.SetBounds(170,80,110,36); $cancel.DialogResult='Cancel'
    Style-Input $input; Style-Button $ok $true; Style-Button $cancel
    $dialog.Controls.AddRange(@($input,$ok,$cancel)); $dialog.AcceptButton=$ok; $dialog.CancelButton=$cancel
    $answer=$dialog.ShowDialog($form); $value=$input.Text.Trim(); $dialog.Dispose()
    if ($answer -eq 'OK') {return $value}
    return $null
}
function Save-GroupAs {
    $value=Ask-GroupName 'Save selected agents as a group' ''
    if ($null -eq $value) {return}
    $savedGroups.Text=$value; Save-Group
}
function Rename-SavedGroup($value) {
    # Only the name changes. Preserve saved members, runtimes, and current tasks.
    $old=$savedGroups.Text.Trim()
    $matches=@($script:groups | Where-Object {$_.name -eq $old})
    if ($matches.Count -ne 1) {throw 'Choose a saved group to rename.'}
    $value=$value.Trim()
    if (-not $value -or $value.Length -gt 60 -or $value -match '[\x00-\x1f]') {throw 'Enter a group name of 1 to 60 characters.'}
    if (@($script:groups | Where-Object {$_.name -eq $value -and $_.name -ne $old}).Count -gt 0) {throw 'Another group already has that name. Choose a different name.'}
    $renamed=@{name=$value;members=$matches[0].members}
    Write-Groups @(@($script:groups | Where-Object {$_.name -ne $old})+$renamed)
    Refresh-Groups; $savedGroups.Text=$value
    $status.Text='Renamed group to '+$value+'.'
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
    $noun=' agents'; if ($script:checked.Count -eq 1) {$noun=' agent'}
    $batch.Text='Review & launch '+$script:checked.Count+$noun
    $clear.Enabled=($script:checked.Count -gt 0 -and -not $script:busy)
    $clear.Visible=-not $script:busy; $stop.Visible=$script:busy
    $stop.Enabled=($script:queue.Count -gt 0)
    $count.Text=[string]$list.Items.Count+' shown / '+$script:checked.Count+' selected'
    $savedGroups.Enabled=-not $script:busy; $loadGroup.Enabled=-not $script:busy
    $saveGroup.Enabled=($script:checked.Count -gt 0 -and -not $script:busy -and $script:groupsHealthy)
    $saveAsGroup.Enabled=$saveGroup.Enabled
    $groupActions.Enabled=-not $script:busy
    $renameGroup.Enabled=(-not $script:busy -and $script:groupsHealthy -and $script:groups.Count -gt 0)
    $deleteGroup.Enabled=(-not $script:busy -and $script:groupsHealthy)
    $preset.Enabled=-not $script:busy; $usePreset.Enabled=$ready
    $batchPreset.Enabled=($script:checked.Count -gt 0 -and -not $script:busy)
    $presetActions.Enabled=$batchPreset.Enabled
    Refresh-SelectionTray
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
    $dialog.StartPosition='CenterParent'; $dialog.Font=$form.Font; $dialog.BackColor=$bg; $dialog.ForeColor=$ink; $dialog.Icon=$form.Icon
    $dialog.FormBorderStyle='FixedDialog'; $dialog.MaximizeBox=$false; $dialog.MinimizeBox=$false
    $heading=New-Object Windows.Forms.Label
    $heading.Text='Start '+$items.Count+' new conversations in separate windows'; $heading.SetBounds(20,20,610,30)
    $preview=New-Object Windows.Forms.TextBox
    $preview.Multiline=$true; $preview.ReadOnly=$true; $preview.ScrollBars='Vertical'
    $preview.SetBounds(20,60,610,305); $preview.Text=Preview-Text $items
    $launch=New-Object LauncherButton
    $launch.Text='Launch selected'; $launch.SetBounds(430,382,200,38); $launch.DialogResult='OK'
    $cancel=New-Object LauncherButton
    $cancel.Text='Cancel'; $cancel.SetBounds(280,382,130,38); $cancel.DialogResult='Cancel'
    Style-Input $preview; Style-Button $launch $true; Style-Button $cancel
    $dialog.Controls.AddRange(@($heading,$preview,$launch,$cancel)); $dialog.CancelButton=$cancel
    # Enter does not start a batch implicitly; the launch button must be chosen.
    $answer=$dialog.ShowDialog($form); $dialog.Dispose()
    return $answer -eq [Windows.Forms.DialogResult]::OK
}
function Log-Result($text) {
    $results.AppendText($text+"`r`n")
    $results.SelectionStart=$results.TextLength; $results.ScrollToCaret()
    if ($text.StartsWith('Not confirmed')) {Set-DetailsVisible $true}
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
        $status.Text='Finished: '+$script:completed+' attempted, '+$script:failed+' not confirmed. See launch details.'
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
$saveAsGroup.Add_Click({Save-GroupAs})
$renameGroup.Add_Click({
    try {
        $value=Ask-GroupName 'Rename saved group' $savedGroups.Text.Trim()
        if ($null -ne $value) {Rename-SavedGroup $value}
    } catch {$status.Text=$_.Exception.Message;$tooltip.SetToolTip($status,$status.Text)}
})
$loadGroup.Add_Click({Load-Group})
$savedGroups.Add_SelectionChangeCommitted({Load-Group})
$groupActions.Add_Click({Update-Buttons; $groupMenu.Show($groupActions,(New-Object Drawing.Point(0,$groupActions.Height)))})
$deleteGroup.Add_Click({Delete-Group})
$usePreset.Add_Click({Apply-Preset $false})
$batchPreset.Add_Click({Apply-Preset $true})
$presetActions.Add_Click({$presetMenu.Show($presetActions,(New-Object Drawing.Point(0,$presetActions.Height)))})
$details.Add_LinkClicked({Set-DetailsVisible (-not $results.Visible)})
foreach ($p in $presets) {[void]$preset.Items.Add($p.name)}
$preset.SelectedIndex=0
$categories.SelectedIndex=0
try {Read-Groups; Refresh-Groups} catch {
    $script:groupsHealthy=$false
    $status.Text='Cannot read saved groups. See results below.'
    Log-Result ($_.Exception.Message+' File: '+$script:groupsPath)
    Set-DetailsVisible $true
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

            # Renaming preserves the saved membership and rejects name collisions.
            $beforeMembers=$script:groups[0].members | ConvertTo-Json -Depth 5 -Compress
            Rename-SavedGroup 'Consumer renamed'
            if ($script:groups[0].name -ne 'Consumer renamed' -or ($script:groups[0].members | ConvertTo-Json -Depth 5 -Compress) -cne $beforeMembers) {throw 'Rename changed saved group members'}
            Write-Groups @($script:groups+@{name='Existing group';members=$script:groups[0].members})
            $before=[IO.File]::ReadAllText($script:groupsPath); $failed=$false
            try {Rename-SavedGroup 'Existing group'} catch {$failed=$true}
            if (-not $failed -or [IO.File]::ReadAllText($script:groupsPath) -cne $before) {throw 'Rename overwrote another group'}
            Rename-SavedGroup 'Consumer review'
            # Selection chips include hidden agents and remove only their target.
            $search.Text='no-such-agent-987654'
            if ($chips.Controls.Count -ne $script:checked.Count) {throw 'Tray lost hidden agents'}
            $remove=$chips.Controls[0]; $removedName=[string]$remove.Tag
            $beforeCount=$script:checked.Count
            $beforeTask=$script:settings[$removedName].task
            $remove.PerformClick()
            if ($script:checked.ContainsKey($removedName) -or $script:checked.Count -ne ($beforeCount-1) -or $script:settings[$removedName].task -cne $beforeTask) {throw 'Chip removal changed other selection or settings'}
            $script:busy=$true; Update-Buttons
            foreach ($chip in $chips.Controls) {if ($chip.Enabled) {throw 'Selection chip enabled during launch'}}
            $script:busy=$false; Update-Buttons
            # Details expand/collapse without losing form size or hiding the tray.
            $height=$form.ClientSize.Height
            Set-DetailsVisible $true
            if (-not $results.Visible -or $results.Bottom -gt $tray.Top) {throw 'Expanded launch details overlap selection tray'}
            Set-DetailsVisible $false
            if ($results.Visible -or $form.ClientSize.Height -ne $height) {throw 'Details toggle changed collapsed form size'}
            Log-Result 'Not confirmed - ISOLATED_TEST: fixture error'
            if (-not $results.Visible) {throw 'Launch error did not reveal details'}
            Set-DetailsVisible $false; $results.Clear()
            $categories.SelectedIndex=0; $search.Clear()
            for ($i=0;$i -lt $list.Items.Count;$i++) {if ($list.Items[$i].Entry.name -eq 'CARL') {$list.SelectedIndex=$i;break}}
            foreach ($control in $form.Controls) {
                if ($control.Visible -and $control -ne $tray -and $control.Bottom -gt $tray.Top) {throw ('Control overlaps selection tray: '+$control.Text)}
                if ($control.Visible -and $control.Right -gt $form.ClientSize.Width) {throw ('Control exceeds form width: '+$control.Text)}
            }
            # Resize once; anchored controls must retain separation and visibility.
            $width=$form.ClientSize.Width
            $form.ClientSize=New-Object Drawing.Size(($width+160),$form.ClientSize.Height)
            if ($start.Right -ge $resume.Left -or $preset.Right -ge $usePreset.Left -or $chips.Right -ge $batch.Left) {throw 'Resized controls overlap'}
            $form.ClientSize=New-Object Drawing.Size($width,$form.ClientSize.Height)
            $retained=@($script:checked.Keys)
            foreach ($entry in $data.agents) {$script:checked[$entry.name]=$true}
            Update-Buttons; $chips.PerformLayout()
            if ($chips.Controls.Count -ne $data.agents.Count -or $chips.DisplayRectangle.Width -le $chips.ClientSize.Width) {throw 'Full selection does not scroll in tray'}
            $script:checked.Clear(); Update-Buttons
            if ($chips.Controls.Count -ne 1 -or $chips.Controls[0] -isnot [Windows.Forms.Label] -or $batch.Enabled) {throw 'Empty tray state failed'}
            foreach ($key in $retained) {$script:checked[$key]=$true}
            Filter-Agents
            if (@(Get-ChildItem -LiteralPath $data.directory -Filter '*.claimed').Count -ne 0) {throw 'Saving/loading/presets started an agent'}
            $status.Text='Ready. Review your selected agents in the tray below.'
            $form.Refresh()
            $bitmap=New-Object Drawing.Bitmap($form.Width,$form.Height)
            $form.DrawToBitmap($bitmap,(New-Object Drawing.Rectangle(0,0,$form.Width,$form.Height)))
            $bitmap.Save((Join-Path $data.directory 'preview.png')); $bitmap.Dispose()
            @{ok=$true;checks='Categories, retained selection, per-agent runtime/task, hidden preview, CATO, resume, empty search, clear, stop remaining, saved groups, atomic persistence, concurrent/corrupt-file refusal, task presets, group rename/collision, hidden selection chips/removal, busy controls, expandable/error details, layout bounds and resize'} | ConvertTo-Json | Set-Content -Encoding UTF8 (Join-Path $data.directory 'smoke.json')
        } catch {
            @{ok=$false;error=$_.Exception.Message} | ConvertTo-Json | Set-Content -Encoding UTF8 (Join-Path $data.directory 'smoke.json')
        } finally {$form.Close()}
    })
}
[void]$form.ShowDialog()
$form.Dispose()

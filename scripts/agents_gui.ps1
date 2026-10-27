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
public static class LauncherTestDeadline {
    public static System.Threading.Timer Start(int milliseconds) {
        return new System.Threading.Timer(_ => {
            Console.Error.WriteLine("Native UI test timed out; its own process is closing.");
            Environment.Exit(124);
        }, null, milliseconds, System.Threading.Timeout.Infinite);
    }
}
'@
$testDeadline=$null
if ($SmokeTest -or $data.test_mode) {$testDeadline=[LauncherTestDeadline]::Start(45000)}
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
# Give each stage its own page; state lives outside the page controls.
$tabs=New-Object Windows.Forms.TabControl
$tabs.SetBounds(24,108,1112,578); $tabs.Anchor='Top,Bottom,Left,Right'
$tabs.DrawMode='OwnerDrawFixed'; $tabs.ItemSize=New-Object Drawing.Size(205,38); $tabs.SizeMode='Fixed'
$form.Controls.Add($tabs)
$pages=@{}
foreach ($key in @('Agents','Selected','Instructions','Activity')) {
    $page=New-Object Windows.Forms.TabPage
    $page.Name=$key; $page.Text=$key; $page.BackColor=$bg; $page.ForeColor=$ink
    if ($key -eq 'Selected') {$page.Text='Selected & groups'}
    [void]$tabs.TabPages.Add($page); $pages[$key]=$page
}
# Inactive TabPages initially use a small default size. Establish their real
# bounds before anchoring children, otherwise their first display stretches twice.
foreach ($page in $tabs.TabPages) {$page.Bounds=$tabs.DisplayRectangle}
$tabs.ItemSize=New-Object Drawing.Size(([int](($tabs.Width-8)/4)),38)
# Changing native tab metrics inside SizeChanged feeds back into its layout.
# Resize the headers once after a user drag instead of inside that event.
$form.Add_ResizeEnd({$tabs.ItemSize=New-Object Drawing.Size(([int](($tabs.Width-8)/4)),38)})
$tabs.Add_DrawItem({
    param($sender,$e)
    $fill=$surface; $text=$muted
    if ($sender.SelectedIndex -eq $e.Index) {$fill=$selection; $text=$accent}
    $brush=New-Object Drawing.SolidBrush($fill)
    try {$e.Graphics.FillRectangle($brush,$e.Bounds)} finally {$brush.Dispose()}
    [Windows.Forms.TextRenderer]::DrawText($e.Graphics,$sender.TabPages[$e.Index].Text,$sender.Font,$e.Bounds,$text,([Windows.Forms.TextFormatFlags]::HorizontalCenter -bor [Windows.Forms.TextFormatFlags]::VerticalCenter -bor [Windows.Forms.TextFormatFlags]::NoPrefix))
})
function Place($control,$parent,$x,$y,$width,$height,$anchor='Top,Left') {
    $control.Anchor='Top,Left'; $parent.Controls.Add($control)
    $control.SetBounds($x,$y,$width,$height); $control.Anchor=$anchor
}
Place $categoryLabel $pages.Agents 16 16 220 26
Place $categories $pages.Agents 16 50 220 410 'Top,Bottom,Left'
Place $searchLabel $pages.Agents 260 16 252 26
Place $search $pages.Agents 260 50 252 30
$searchScope=Label 'Browse by category, or search all agents.' 0 0 1 1 9
Place $searchScope $pages.Agents 260 88 252 34
$searchScope.ForeColor=$muted
Place $list $pages.Agents 260 130 252 330 'Top,Bottom,Left'
Place $count $pages.Agents 260 472 252 24 'Bottom,Left'
Place $name $pages.Agents 548 16 520 38 'Top,Left,Right'
Place $purpose $pages.Agents 550 66 518 60 'Top,Left,Right'
Place $group $pages.Agents 550 134 518 28 'Top,Left,Right'
Place $runtimeLabel $pages.Agents 550 194 518 25 'Top,Left,Right'
Place $runtime $pages.Agents 550 224 518 32 'Top,Left,Right'
$taskSummary=Label '' 0 0 1 1 10
Place $taskSummary $pages.Agents 550 278 518 54 'Top,Left,Right'
$taskSummary.ForeColor=$muted
$editInstructions=Button 'Edit instructions...' 0 0 1
Place $editInstructions $pages.Agents 550 344 518 40 'Top,Left,Right'
Place $start $pages.Agents 550 406 250 40
Place $resume $pages.Agents 812 406 256 40 'Top,Right'
Place $hint $pages.Agents 550 460 518 42 'Top,Left,Right'

Place $savedLabel $pages.Selected 16 16 500 26
Place $savedGroups $pages.Selected 16 50 500 32
Place $loadGroup $pages.Selected 528 46 140 40
Place $groupActions $pages.Selected 680 46 140 40
$groupHint=Label 'Groups remember agents and runtimes. Click an agent below to edit its instructions.' 0 0 1 1 10
Place $groupHint $pages.Selected 16 102 1052 36 'Top,Left,Right'
$groupHint.ForeColor=$muted
Place $selectionLabel $pages.Selected 16 148 1052 26 'Top,Left,Right'
Place $chips $pages.Selected 16 184 1052 310 'Top,Bottom,Left,Right'
$chips.FlowDirection='TopDown'; $chips.WrapContents=$false; $chips.BackColor=$bg

$instructionAgentLabel=Label 'Agent' 0 0 1 1
Place $instructionAgentLabel $pages.Instructions 20 16 650 26
$instructionAgent=New-Object Windows.Forms.ComboBox
$instructionAgent.DropDownStyle='DropDownList'
foreach ($entry in $data.agents) {[void]$instructionAgent.Items.Add($entry.name)}
Style-Input $instructionAgent
Place $instructionAgent $pages.Instructions 20 50 650 32 'Top,Left,Right'
$instructionRuntimeLabel=Label 'Runtime' 0 0 1 1
Place $instructionRuntimeLabel $pages.Instructions 700 16 368 26 'Top,Right'
$instructionRuntime=New-Object Windows.Forms.ComboBox
$instructionRuntime.DropDownStyle='DropDownList'; Style-Input $instructionRuntime
Place $instructionRuntime $pages.Instructions 700 50 368 32 'Top,Right'
Place $presetLabel $pages.Instructions 20 108 1048 26 'Top,Left,Right'
Place $preset $pages.Instructions 20 142 650 32 'Top,Left,Right'
Place $usePreset $pages.Instructions 684 138 172 40 'Top,Right'
$presetActions.Text='Manage...'
Place $presetActions $pages.Instructions 868 138 200 40 'Top,Right'
$savePreset=$presetMenu.Items.Add('Save these instructions as a preset...')
$deletePreset=$presetMenu.Items.Add('Delete selected custom preset...')
Place $taskLabel $pages.Instructions 20 202 1048 26 'Top,Left,Right'
Place $task $pages.Instructions 20 234 1048 190 'Top,Bottom,Left,Right'
$instructionStart=Button 'New conversation' 0 0 1
Place $instructionStart $pages.Instructions 20 444 260 40 'Bottom,Left'
$instructionResume=Button 'Resume conversation...' 0 0 1
Place $instructionResume $pages.Instructions 296 444 260 40 'Bottom,Left'
$instructionHint=Label 'Instructions apply to a new conversation. Clear them to enable Resume.' 0 0 1 1 9
Place $instructionHint $pages.Instructions 20 494 1048 26 'Bottom,Left,Right'
$instructionHint.ForeColor=$muted

$activityHint=Label 'Recent launches on this machine. Startup confirmation does not mean an agent is still working.' 0 0 1 1 10
Place $activityHint $pages.Activity 20 16 1048 36 'Top,Left,Right'
$activityHint.ForeColor=$muted
$historyList=New-Object Windows.Forms.ListBox
$historyList.DisplayMember='Display'; $historyList.IntegralHeight=$false
Style-Input $historyList
Place $historyList $pages.Activity 20 66 354 324 'Top,Bottom,Left'
$historyDetail=New-Object Windows.Forms.TextBox
$historyDetail.Multiline=$true; $historyDetail.ReadOnly=$true; $historyDetail.ScrollBars='Vertical'
Style-Input $historyDetail
Place $historyDetail $pages.Activity 390 66 678 324 'Top,Bottom,Left,Right'
$historyOpen=Button 'Go to this agent' 0 0 1
Place $historyOpen $pages.Activity 20 404 354 40 'Bottom,Left'
$latestLabel=Label 'Latest batch details' 0 0 1 1 9
Place $latestLabel $pages.Activity 390 404 678 26 'Bottom,Left,Right'
$latestLabel.ForeColor=$muted
Place $results $pages.Activity 390 436 678 80 'Bottom,Left,Right'
$results.Visible=$true

# The small footer is shared; the selection list itself has its own page.
$tray.Height=76
Place $status $tray 24 8 650 22 'Top,Left,Right'
$selectedLink=New-Object Windows.Forms.LinkLabel
$selectedLink.LinkColor=$accent; $selectedLink.VisitedLinkColor=$accent; $selectedLink.ActiveLinkColor=$accent
Place $selectedLink $tray 24 42 150 26
Place $clear $tray 180 36 96 30
$details.Text='View activity'
Place $details $tray 300 42 150 26
Place $batch $tray 856 26 280 40 'Top,Right'
Place $stop $tray 700 26 144 40 'Top,Right'
$subtitle.Text='Find agents, prepare their work, and review launches on separate tabs.'
$form.KeyPreview=$true
$form.Add_KeyDown({
    param($sender,$e)
    if ($e.Control -and $e.KeyCode -eq [Windows.Forms.Keys]::F -and -not $script:busy) {
        $tabs.SelectedTab=$pages.Agents; $search.Focus(); $search.SelectAll(); $e.SuppressKeyPress=$true
    }
})
$form.Add_Shown({
    # Older Windows builds can decline the title-bar hint; controls stay themed.
    try {
        $dark=1
        $code=[LauncherWindowTheme]::DwmSetWindowAttribute($form.Handle,20,[ref]$dark,4)
        if ($code -ne 0) {[void][LauncherWindowTheme]::DwmSetWindowAttribute($form.Handle,19,[ref]$dark,4)}
    } catch {}
})

function Set-DetailsVisible($visible) {
    if ($visible) {$tabs.SelectedTab=$pages.Activity} else {$tabs.SelectedTab=$pages.Agents}
}
function Focus-Agent($agentName,$page='Instructions') {
    if ($script:busy) {return}
    $script:filtering=$true
    try {$categories.SelectedIndex=0; $search.Clear()} finally {$script:filtering=$false}
    Filter-Agents
    for ($i=0;$i -lt $list.Items.Count;$i++) {
        if ($list.Items[$i].Entry.name -eq $agentName) {
            $list.SelectedIndex=$i; Select-Agent; $tabs.SelectedTab=$pages[$page]; return
        }
    }
    $status.Text='This agent is no longer configured: '+$agentName
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
                $card=New-Object Windows.Forms.Panel
                $card.Tag=$entry.name; $card.BackColor=$surface; $card.Size=New-Object Drawing.Size(($chips.ClientSize.Width-24),76)
                $card.Margin=New-Object Windows.Forms.Padding(0,0,0,10)
                $edit=New-Object LauncherButton
                $edit.Text=$entry.name; $edit.Tag=$entry.name; $edit.SetBounds(10,12,170,48)
                Style-Button $edit; $edit.ForeColor=$accent
                $edit.AccessibleName='Edit '+$entry.name+' instructions'
                $edit.Add_Click({param($sender,$e) Focus-Agent ([string]$sender.Tag)})
                $card.Controls.Add($edit)
                $summary=New-Object Windows.Forms.Label
                $summary.Name='Summary'; $summary.SetBounds(200,10,($card.Width-280),56); $summary.Anchor='Top,Left,Right'
                $summary.ForeColor=$muted; $card.Controls.Add($summary)
                $remove=New-Object LauncherButton
                $remove.Text='x'; $remove.Tag=$entry.name; $remove.SetBounds(($card.Width-58),18,40,36); $remove.Anchor='Top,Right'
                Style-Button $remove; $remove.AccessibleName='Remove '+$entry.name+' from selection'
                $tooltip.SetToolTip($remove,'Remove only '+$entry.name+' from the selection')
                $remove.Add_Click({param($sender,$e) $script:checked.Remove([string]$sender.Tag); Filter-Agents})
                $card.Controls.Add($remove); $chips.Controls.Add($card)
            }
        } finally {$chips.ResumeLayout()}
    }
    foreach ($card in $chips.Controls) {
        $card.Enabled=-not $script:busy
        if ($card -is [Windows.Forms.Panel]) {
            $setting=$script:settings[[string]$card.Tag]
            $label=@{sol='Codex Sol';claude='Claude';astra='Codex Astra'}[$setting.runtime]
            $text='Default startup instructions'
            if (-not [string]::IsNullOrWhiteSpace($setting.task)) {$text=($setting.task -replace '\s+',' ')}
            if ($text.Length -gt 110) {$text=$text.Substring(0,107)+'...'}
            $card.Controls['Summary'].Text=$label+"`r`n"+$text
        }
    }
}
$chips.Add_SizeChanged({foreach ($card in $chips.Controls) {if ($card -is [Windows.Forms.Panel]) {$card.Width=[Math]::Max(400,$chips.ClientSize.Width-24)}}})

# Groups are personal preferences; never commands, tasks, or a fleet roster.
$script:groups=@(); $script:groupsVersion=''; $script:groupsHealthy=$true
$preferencesFolder=Join-Path ([Environment]::GetFolderPath('LocalApplicationData')) 'ResearchAgentLauncher'
if ($SmokeTest -or $data.test_mode) {
    $preferencesFolder=Join-Path ([IO.Path]::GetTempPath()) ('AgentLauncherTest-'+[Guid]::NewGuid().ToString('N'))
}
$script:groupsPath=Join-Path $preferencesFolder 'groups.json'
$script:presetPath=Join-Path $preferencesFolder 'presets.json'
$script:historyPath=Join-Path $preferencesFolder 'history.json'
$script:customPresets=@(); $script:presetVersion=''; $script:presetsHealthy=$true
$script:history=@()
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
$builtInPresets=@(
    @{name='Orient and report status';text='Follow your startup instructions. Recover current work, approvals, and unresolved conditions. Give Will a short status and suggested next step. Do not begin unassigned work.'},
    @{name='Continue approved work';text='Follow your startup instructions and recover the current assignment, existing approvals, and unresolved conditions. Continue only work already authorized and currently in scope. Preserve all approval conditions; ask Will if the applicable assignment or authority is unclear. Report the result and next stopping point.'},
    @{name='Prepare handoff';text='Follow your startup instructions and recover current work and approvals. Prepare your normal handoff and closeout for the existing assignment. Preserve unfinished work, blockers, approval conditions, and a clear resume point. Do not start new research or unrelated pending work.'}
)
function Validate-LocalRecords($document,$kind) {
    if ($document.version -ne 1 -or $document.$kind -isnot [Array]) {throw ('Unsupported '+$kind+' file format. The original file was kept.')}
    $seen=@{}
    foreach ($item in $document.$kind) {
        if ($kind -eq 'presets') {
            if ($item.name -isnot [string] -or [string]::IsNullOrWhiteSpace($item.name) -or $item.name.Length -gt 60 -or $item.name -match '[\x00-\x1f]' -or $seen.ContainsKey($item.name) -or $item.text -isnot [string] -or [string]::IsNullOrWhiteSpace($item.text) -or $item.text.Length -gt 32767) {throw 'Invalid or duplicate custom preset. The original file was kept.'}
            if (@($builtInPresets | Where-Object {$_.name -eq $item.name}).Count -gt 0) {throw 'A custom preset uses a built-in name. The original file was kept.'}
            $seen[$item.name]=$true
        } else {
            $timestamp=[DateTimeOffset]::MinValue
            if ($item.name -isnot [string] -or $item.name -notmatch '^[A-Z][A-Z0-9_-]*$' -or $item.runtime -notin @('sol','claude','astra') -or $item.action -notin @('new','resume') -or $item.outcome -notin @('Opened','Not confirmed','Cancelled') -or $item.message -isnot [string] -or $item.task -isnot [string] -or -not [DateTimeOffset]::TryParse([string]$item.time,[ref]$timestamp)) {throw 'Invalid launch history. The original file was kept.'}
        }
    }
}
function Read-LocalRecords($path,$kind) {
    $text=''; $records=@()
    if ([IO.File]::Exists($path)) {
        $text=[IO.File]::ReadAllText($path)
        if (-not $text.Trim()) {throw ('The '+$kind+' file is empty. It was kept.')}
        $document=$text | ConvertFrom-Json
        Validate-LocalRecords $document $kind
        $records=@($document.$kind)
    }
    return @{text=$text;records=$records}
}
function Write-LocalRecords($path,$kind,$items,$expected,$append=$false) {
    $hash=[Security.Cryptography.SHA256]::Create()
    $key=[BitConverter]::ToString($hash.ComputeHash([Text.Encoding]::UTF8.GetBytes($path))).Replace('-',''); $hash.Dispose()
    $mutex=New-Object Threading.Mutex($false,('Local\AgentLauncherRecords-'+$key)); $locked=$false
    try {
        try {$locked=$mutex.WaitOne(1500)} catch [Threading.AbandonedMutexException] {$locked=$true}
        if (-not $locked) {throw 'Another launcher is saving. Try again shortly.'}
        $current=Read-LocalRecords $path $kind
        if (-not $append -and $current.text -cne $expected) {throw 'Custom presets changed in another window. Reload them before saving.'}
        $records=@($items)
        if ($append) {$records=@(@($current.records)+@($items) | Select-Object -Last 100)}
        $document=@{version=1}; $document[$kind]=$records
        Validate-LocalRecords $document $kind
        [void][IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($path))
        $text=$document | ConvertTo-Json -Depth 8
        $temporary=$path+'.'+[Guid]::NewGuid().ToString('N')+'.tmp'
        [IO.File]::WriteAllText($temporary,$text,(New-Object Text.UTF8Encoding($false)))
        if ([IO.File]::Exists($path)) {[IO.File]::Replace($temporary,$path,($path+'.previous'))} else {[IO.File]::Move($temporary,$path)}
        return @{text=$text;records=$records}
    } finally {
        if ($locked) {$mutex.ReleaseMutex()}; $mutex.Dispose()
    }
}
function Refresh-Presets {
    $previous=$preset.Text
    $script:presets=@($builtInPresets)+@($script:customPresets)
    $preset.Items.Clear()
    foreach ($item in $script:presets) {[void]$preset.Items.Add($item.name)}
    $preset.SelectedIndex=0
    if ($preset.Items.Contains($previous)) {$preset.SelectedItem=$previous}
}
function Reload-CustomPresets {
    try {
        $saved=Read-LocalRecords $script:presetPath 'presets'
        $script:customPresets=@($saved.records); $script:presetVersion=$saved.text; $script:presetsHealthy=$true
        Refresh-Presets
    } catch {
        $script:presetsHealthy=$false
        $status.Text='Custom presets could not be read; built-in presets still work.'
        Log-Result ($_.Exception.Message+' File: '+$script:presetPath)
        Refresh-Presets
    }
}
function Save-CustomPreset($presetName) {
    $presetName=$presetName.Trim()
    if (-not $script:presetsHealthy) {throw 'Reload or repair the custom preset file before saving. It has been kept.'}
    if ([string]::IsNullOrWhiteSpace($task.Text)) {throw 'Enter instructions before saving a custom preset.'}
    if (@($builtInPresets | Where-Object {$_.name -eq $presetName}).Count -gt 0) {throw 'Built-in presets cannot be replaced. Choose a different name.'}
    if (@($script:customPresets | Where-Object {$_.name -eq $presetName}).Count -gt 0) {
        if (-not (& $script:confirmChange ('Replace the saved instructions in '+$presetName+'?') 'Save preset')) {return}
    }
    $items=@(@($script:customPresets | Where-Object {$_.name -ne $presetName})+@{name=$presetName;text=$task.Text})
    $saved=Write-LocalRecords $script:presetPath 'presets' $items $script:presetVersion
    $script:customPresets=@($saved.records); $script:presetVersion=$saved.text
    Refresh-Presets; $preset.SelectedItem=$presetName
    $status.Text='Saved preset '+$presetName+'. Apply it explicitly before launching.'
}
function Delete-CustomPreset {
    $presetName=$preset.Text
    if (@($script:customPresets | Where-Object {$_.name -eq $presetName}).Count -ne 1) {throw 'Choose a custom preset to delete. Built-in presets are kept.'}
    if (-not (& $script:confirmChange ('Delete custom preset '+$presetName+'? Current instructions will stay.') 'Delete preset')) {return}
    $items=@($script:customPresets | Where-Object {$_.name -ne $presetName})
    $saved=Write-LocalRecords $script:presetPath 'presets' $items $script:presetVersion
    $script:customPresets=@($saved.records); $script:presetVersion=$saved.text
    Refresh-Presets; $status.Text='Deleted saved preset. Current instructions were kept.'
}
function Select-History {
    $historyOpen.Enabled=($null -ne $historyList.SelectedItem -and -not $script:busy)
    if ($null -eq $historyList.SelectedItem) {$historyDetail.Text='Launches will appear here after you start a conversation.'; return}
    $record=$historyList.SelectedItem.Record
    $label=@{sol='Codex Sol';claude='Claude';astra='Codex Astra'}[$record.runtime]
    $text=$record.task; if (-not $text) {$text='Follow the agent startup instructions'}
    $historyDetail.Text=$record.name+' | '+$label+' | '+$record.action+"`r`n"+$record.time+"`r`n`r`n"+$record.outcome+': '+$record.message+"`r`n`r`nInstructions:`r`n"+$text+"`r`n`r`nThis is a launch record, not a live work-status report."
}
function Refresh-History {
    $historyList.BeginUpdate()
    try {
        $historyList.Items.Clear()
        for ($i=$script:history.Count-1;$i -ge 0;$i--) {
            $record=$script:history[$i]
            $time=([DateTimeOffset]::Parse($record.time)).LocalDateTime.ToString('MMM d HH:mm')
            [void]$historyList.Items.Add([pscustomobject]@{Display=$time+'  '+$record.name+' - '+$record.outcome;Record=$record})
        }
        if ($historyList.Items.Count -gt 0) {$historyList.SelectedIndex=0}
    } finally {$historyList.EndUpdate()}
    Select-History
}
function Record-Launch($request,$outcome,$message) {
    $record=@{time=[DateTimeOffset]::Now.ToString('o');name=$request.name;runtime=$request.runtime;action=$request.action;task=[string]$request.task;outcome=$outcome;message=[string]$message}
    try {
        # Merge under the file mutex so concurrent launcher windows keep both records.
        $saved=Write-LocalRecords $script:historyPath 'history' @($record) '' $true
        $script:history=@($saved.records)
    } catch {
        $script:history=@(@($script:history)+$record | Select-Object -Last 100)
        Log-Result ('Launch history not saved: '+$_.Exception.Message)
    }
    Refresh-History
}
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
    $instructionStart.Enabled=$start.Enabled; $instructionResume.Enabled=$resume.Enabled
    $editInstructions.Enabled=$ready
    $instructionAgent.Enabled=-not $script:busy
    $instructionRuntime.Enabled=($ready -and $script:selected.kind -ne 'cato')
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
    $selectedLink.Text=[string]$script:checked.Count+' selected - view'
    $pages.Selected.Text='Selected & groups ('+$script:checked.Count+')'
    $selectionLabel.Text=[string]$script:checked.Count+' selected agents - name to edit, x to remove'
    $savedGroups.Enabled=-not $script:busy; $loadGroup.Enabled=-not $script:busy
    $saveGroup.Enabled=($script:checked.Count -gt 0 -and -not $script:busy -and $script:groupsHealthy)
    $saveAsGroup.Enabled=$saveGroup.Enabled
    $groupActions.Enabled=-not $script:busy
    $renameGroup.Enabled=(-not $script:busy -and $script:groupsHealthy -and $script:groups.Count -gt 0)
    $deleteGroup.Enabled=(-not $script:busy -and $script:groupsHealthy)
    $preset.Enabled=-not $script:busy; $usePreset.Enabled=$ready
    $batchPreset.Enabled=($script:checked.Count -gt 0 -and -not $script:busy)
    $presetActions.Enabled=-not $script:busy
    $savePreset.Enabled=($ready -and $script:presetsHealthy -and -not [string]::IsNullOrWhiteSpace($task.Text))
    $deletePreset.Enabled=(-not $script:busy -and $script:presetsHealthy -and @($script:customPresets | Where-Object {$_.name -eq $preset.Text}).Count -eq 1)
    Refresh-SelectionTray
    $taskSummary.Text='Instructions: default agent startup'
    if (-not [string]::IsNullOrWhiteSpace($task.Text)) {
        $text=($task.Text -replace '\s+',' ')
        if ($text.Length -gt 115) {$text=$text.Substring(0,112)+'...'}
        $taskSummary.Text='Instructions: '+$text
    }
    $tooltip.SetToolTip($taskSummary,$task.Text)
    $historyOpen.Enabled=($null -ne $historyList.SelectedItem -and -not $script:busy)
}
function Save-Settings {
    if ($script:loading -or $null -eq $script:selected) {return}
    $value='sol'
    if ($runtime.Text -eq 'Claude') {$value='claude'}
    if ($runtime.Text -eq 'Codex Astra') {$value='astra'}
    $script:settings[$script:selected.name]=@{runtime=$value;task=$task.Text}
    if ($instructionRuntime.SelectedIndex -ne $runtime.SelectedIndex) {$instructionRuntime.SelectedIndex=$runtime.SelectedIndex}
    Update-Buttons
}
function Select-Agent {
    if ($script:filtering) {return}
    $script:loading=$true
    try {
        $runtime.Items.Clear()
        if ($null -eq $list.SelectedItem) {
            $script:selected=$null; $name.Text='No matching agents'; $purpose.Text='Try another name or category.'
            $group.Text=''; $task.Text=''; $instructionAgent.SelectedIndex=-1; $instructionRuntime.Items.Clear(); return
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
        $instructionAgent.SelectedItem=$script:selected.name
        $instructionRuntime.Items.Clear()
        foreach ($item in $runtime.Items) {[void]$instructionRuntime.Items.Add($item)}
        $instructionRuntime.SelectedIndex=$runtime.SelectedIndex
        $status.Text='Ready. Each conversation opens in its own terminal.'
        if ($script:selected.error) {$status.Text=$script:selected.error}
        $tooltip.SetToolTip($status,$status.Text); $tooltip.SetToolTip($name,$script:selected.folder)
    } finally {$script:loading=$false; Update-Buttons}
}
function Filter-Agents {
    if ($script:filtering) {return}
    $previous=$null
    if ($script:selected) {$previous=$script:selected.name}
    $query=$search.Text.Trim(); $category=''
    if ($categories.SelectedItem) {$category=$categories.SelectedItem.Name}
    $searchScope.Text='Browsing the selected category'
    if ($query) {$searchScope.Text='Searching all agents (Ctrl+F)'}
    $script:filtering=$true
    $list.BeginUpdate()
    try {
        $list.Items.Clear()
        foreach ($entry in $data.agents) {
            $haystack=$entry.name+' '+$entry.purpose+' '+$entry.group
            if (($query -ne '' -or $category -eq '' -or $category -eq $entry.group) -and $haystack.IndexOf($query,[StringComparison]::OrdinalIgnoreCase) -ge 0) {
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
    $tabs.SelectedTab=$pages.Activity
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
    Record-Launch $script:active $prefix $message
    $script:completed++; $script:active=$null; $script:process=$null
}
function Start-Next {
    if ($script:queue.Count -eq 0) {
        $script:busy=$false
        $status.Text='Finished: '+$script:completed+' attempted, '+$script:failed+' not confirmed. See Activity.'
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
        Record-Launch $item 'Cancelled' 'Cancelled before startup'
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
$instructionRuntime.Add_SelectedIndexChanged({
    if (-not $script:loading -and $instructionRuntime.SelectedIndex -ge 0) {$runtime.SelectedIndex=$instructionRuntime.SelectedIndex}
})
$instructionAgent.Add_SelectionChangeCommitted({Focus-Agent ([string]$instructionAgent.SelectedItem)})
$task.Add_TextChanged({Save-Settings})
$editInstructions.Add_Click({$tabs.SelectedTab=$pages.Instructions})
$selectedLink.Add_LinkClicked({$tabs.SelectedTab=$pages.Selected})
$historyList.Add_SelectedIndexChanged({Select-History})
$historyOpen.Add_Click({if ($historyList.SelectedItem) {Focus-Agent $historyList.SelectedItem.Record.name 'Agents'}})
$clear.Add_Click({$script:checked.Clear();Filter-Agents})
$stop.Add_Click({Stop-Remaining})
$batch.Add_Click({
    $items=@(Selected-Requests)
    if ($items.Count -gt 0 -and (Confirm-Batch $items)) {Begin-Requests $items}
})
$start.Add_Click({Begin-Launch 'new'})
$resume.Add_Click({Begin-Launch 'resume'})
$instructionStart.Add_Click({Begin-Launch 'new'})
$instructionResume.Add_Click({Begin-Launch 'resume'})
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
$savePreset.Add_Click({
    try {
        $value=Ask-GroupName 'Save these instructions as a preset' ''
        if ($null -ne $value) {Save-CustomPreset $value}
    } catch {$status.Text=$_.Exception.Message;$tooltip.SetToolTip($status,$status.Text)}
})
$deletePreset.Add_Click({try {Delete-CustomPreset} catch {$status.Text=$_.Exception.Message}})
$reloadPresets=$presetMenu.Items.Add('Reload saved presets')
$reloadPresets.Add_Click({Reload-CustomPresets; Update-Buttons})
$presetActions.Add_Click({Update-Buttons; $presetMenu.Show($presetActions,(New-Object Drawing.Point(0,$presetActions.Height)))})
$preset.Add_SelectedIndexChanged({Update-Buttons})
$details.Add_LinkClicked({Set-DetailsVisible $true})
Reload-CustomPresets
$categories.SelectedIndex=0
try {Read-Groups; Refresh-Groups} catch {
    $script:groupsHealthy=$false
    $status.Text='Cannot read saved groups. See results below.'
    Log-Result ($_.Exception.Message+' File: '+$script:groupsPath)
    Set-DetailsVisible $true
}
try {$saved=Read-LocalRecords $script:historyPath 'history'; $script:history=@($saved.records)} catch {
    $status.Text='Saved activity could not be read. The original file was kept.'
    Log-Result ($_.Exception.Message+' File: '+$script:historyPath)
}
Refresh-History
Update-Buttons
$timer.Start()
if ($SmokeTest) {
    function Test-Step($name) {[IO.File]::WriteAllText((Join-Path $data.directory 'test-stage.txt'),$name)}
    $form.Add_Shown({
        try {
            Test-Step 'Initial selection and policy'
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
            $script:queue.Enqueue(@{name='NOT_STARTED_TEST';runtime='sol';action='new';task=''})
            Stop-Remaining
            if ($script:queue.Count -ne 0 -or $results.Text -notmatch 'Cancelled - NOT_STARTED_TEST') {throw 'Stop remaining failed'}
            $results.Clear()
            $search.Clear(); $categories.SelectedIndex=2; $search.Text='CARL'
            $list.SetItemChecked(0,$true); $list.SetItemChecked(1,$true); $list.SetItemChecked(2,$true)
            Test-Step 'Group persistence and validation'
            # Save/reload real preference files in an isolated Windows temp folder.
            $savedGroups.Text='Consumer review'; $saveGroup.PerformClick()
            if (-not [IO.File]::Exists($script:groupsPath)) {throw ('Group save failed: '+$status.Text)}
            $original=[IO.File]::ReadAllText($script:groupsPath)
            if ($original -match 'Only CARL receives') {throw 'Group persisted task text'}
            $clear.PerformClick(); $script:settings['CARL'].runtime='sol'
            $script:groups=@(); Read-Groups; Refresh-Groups; $tabs.SelectedTab=$pages.Selected; $loadGroup.PerformClick()
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
            Test-Step 'Built-in presets'
            $search.Text='CARL'; $task.Clear(); $tabs.SelectedTab=$pages.Instructions
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
            Test-Step 'Search, selected editing, and tab state'
            # Searching crosses categories; clearing restores category browsing.
            $tabs.SelectedTab=$pages.Agents; $categories.SelectedIndex=2; $search.Text='MIDAS'
            if (@($list.Items | Where-Object {$_.Entry.name -eq 'MIDAS'}).Count -ne 1 -or $searchScope.Text -notmatch 'all agents') {throw 'Global search missed an agent outside the category'}
            $search.Clear()
            if ($categories.SelectedIndex -ne 2) {throw 'Clearing search changed the browsed category'}
            foreach ($item in $list.Items) {if ($item.Entry.group -ne $categories.SelectedItem.Name) {throw 'Clearing search did not restore category browsing'}}
            # Selected names navigate; only their separate x removes membership.
            $search.Text='no-such-agent-987654'; $tabs.SelectedTab=$pages.Selected
            if ($chips.Controls.Count -ne $script:checked.Count) {throw 'Selected page lost hidden agents'}
            $card=$chips.Controls[0]; $agentName=[string]$card.Tag
            $beforeCount=$script:checked.Count; $beforeTask=$script:settings[$agentName].task
            $card.Controls[0].PerformClick()
            if ($tabs.SelectedTab -ne $pages.Instructions -or $script:selected.name -ne $agentName -or $script:checked.Count -ne $beforeCount -or -not $script:checked.ContainsKey($agentName) -or $task.Text -cne $beforeTask) {throw 'Selected-name navigation lost membership or settings'}
            $task.Text='A distinct edited instruction for '+$agentName
            $instructionRuntime.SelectedIndex=1
            if ($runtime.Text -ne 'Claude' -or $script:settings[$agentName].runtime -ne 'claude') {throw 'Instructions runtime did not synchronize'}
            foreach ($page in $tabs.TabPages) {$tabs.SelectedTab=$page}
            if ($script:settings[$agentName].task -cne $task.Text -or $script:checked.Count -ne $beforeCount) {throw 'Tab switching lost preparation state'}
            $tabs.SelectedTab=$pages.Selected; $card.Controls[2].PerformClick()
            if ($script:checked.ContainsKey($agentName) -or $script:checked.Count -ne ($beforeCount-1) -or $script:settings[$agentName].task -notmatch 'distinct edited instruction') {throw 'Remove changed another selection or discarded instructions'}
            # Tab navigation is allowed during a queue; editing remains disabled.
            $script:queue.Enqueue(@{name='QUEUED_TEST';runtime='sol';action='new';task=''})
            $script:busy=$true; Update-Buttons
            foreach ($page in $tabs.TabPages) {$tabs.SelectedTab=$page}
            foreach ($card in $chips.Controls) {if ($card.Enabled) {throw 'Selected controls enabled during launch'}}
            if ($task.Enabled -or $instructionRuntime.Enabled -or $instructionStart.Enabled -or $script:queue.Count -ne 1) {throw 'Busy tab switch changed queue or enabled editing'}
            $script:queue.Clear(); $script:busy=$false; Update-Buttons
            Test-Step 'Custom presets'
            # Custom presets persist separately, remain editable, and preserve built-ins.
            Focus-Agent 'CARL'; $task.Text="A custom literal instruction.`r`nSecond line."
            $groupBefore=[IO.File]::ReadAllText($script:groupsPath)
            Save-CustomPreset 'My recurring instruction'
            $presetBefore=[IO.File]::ReadAllText($script:presetPath)
            if ([IO.File]::ReadAllText($script:groupsPath) -cne $groupBefore) {throw 'Custom preset changed saved groups'}
            $script:customPresets=@(); Reload-CustomPresets
            $preset.SelectedItem='My recurring instruction'; $task.Clear(); $usePreset.PerformClick()
            if ($task.Text -notmatch 'Second line' -or $resume.Enabled) {throw 'Saved custom preset did not apply'}
            $failed=$false
            try {Save-CustomPreset $builtInPresets[0].name} catch {$failed=$true}
            if (-not $failed -or [IO.File]::ReadAllText($script:presetPath) -cne $presetBefore) {throw 'Custom save overwrote a built-in preset'}
            [IO.File]::WriteAllText($script:presetPath,$presetBefore+"`r`n")
            $failed=$false
            try {Save-CustomPreset 'Concurrent write'} catch {$failed=$true}
            if (-not $failed -or [IO.File]::ReadAllText($script:presetPath) -cne ($presetBefore+"`r`n")) {throw 'Concurrent preset write was overwritten'}
            Reload-CustomPresets
            [IO.File]::WriteAllText($script:presetPath,'{broken'); Reload-CustomPresets
            $failed=$false
            try {Save-CustomPreset 'Refuse corrupt'} catch {$failed=$true}
            if (-not $failed -or $script:presetsHealthy -or [IO.File]::ReadAllText($script:presetPath) -cne '{broken') {throw 'Corrupt custom presets were overwritten'}
            [IO.File]::WriteAllText($script:presetPath,$presetBefore); Reload-CustomPresets
            $preset.SelectedItem='My recurring instruction'
            $script:confirmChange={param($message,$title) return $false}
            $task.Text='Changed wording'; Save-CustomPreset 'My recurring instruction'; Delete-CustomPreset
            if ([IO.File]::ReadAllText($script:presetPath) -cne $presetBefore) {throw 'Cancelled preset overwrite/delete changed disk'}
            $script:confirmChange={param($message,$title) return $true}
            Save-CustomPreset 'My recurring instruction'
            if ($script:customPresets[0].text -cne 'Changed wording') {throw 'Confirmed preset update failed'}
            Delete-CustomPreset
            if ($script:customPresets.Count -ne 0 -or $task.Text -cne 'Changed wording') {throw 'Deleting final preset discarded current instructions'}
            $script:confirmChange=$normalConfirm
            Test-Step 'History persistence and retention'
            # History merges current disk records and bounds storage, without launches.
            $request=@{name='CARL';runtime='sol';action='new';task='Exact history task'}
            Record-Launch $request 'Opened' 'Fixture CLI process acknowledged'
            $other=@{time=[DateTimeOffset]::Now.ToString('o');name='CATO';runtime='astra';action='resume';task='';outcome='Not confirmed';message='Other window fixture'}
            [void](Write-LocalRecords $script:historyPath 'history' @($other) '' $true)
            Record-Launch $request 'Cancelled' 'Fixture cancelled before startup'
            $saved=Read-LocalRecords $script:historyPath 'history'
            if (@($saved.records | Where-Object {$_.message -eq 'Other window fixture'}).Count -ne 1 -or @($saved.records | Where-Object {$_.task -eq 'Exact history task'}).Count -ne 2) {throw 'History merge lost another window or task text'}
            $many=@(1..103 | ForEach-Object {@{time=[DateTimeOffset]::Now.ToString('o');name='CARL';runtime='sol';action='new';task='';outcome='Opened';message=('Fixture '+$_)}})
            $saved=Write-LocalRecords $script:historyPath 'history' $many '' $true
            if ($saved.records.Count -ne 100 -or $saved.records[0].message -ne 'Fixture 4') {throw 'History retention failed'}
            $script:history=@($saved.records); Refresh-History
            if ($historyList.Items.Count -ne 100 -or $historyDetail.Text -notmatch 'not a live work-status report') {throw 'History display overstates startup or loses records'}
            $historyBefore=$saved.text
            [IO.File]::WriteAllText($script:historyPath,'{broken')
            Record-Launch $request 'Not confirmed' 'Fixture failed startup'
            if ([IO.File]::ReadAllText($script:historyPath) -cne '{broken' -or $results.Text -notmatch 'Launch history not saved') {throw 'Corrupt history was overwritten or hidden'}
            [IO.File]::WriteAllText($script:historyPath,$historyBefore)
            $saved=Read-LocalRecords $script:historyPath 'history'; $script:history=@($saved.records); Refresh-History
            $tabs.SelectedTab=$pages.Activity
            $beforeCount=$script:checked.Count; $beforeTask=$script:settings['CARL'].task
            $historyOpen.PerformClick()
            if ($tabs.SelectedTab -ne $pages.Agents -or $script:selected.name -ne 'CARL' -or $script:checked.Count -ne $beforeCount -or $script:settings['CARL'].task -cne $beforeTask) {throw 'History navigation changed preparation state'}
            Test-Step 'Page bounds and resize'
            # Activity has its own page; errors reveal it without growing the window.
            $tabs.SelectedTab=$pages.Agents; $height=$form.ClientSize.Height
            Log-Result 'Not confirmed - ISOLATED_TEST: fixture error'
            if ($tabs.SelectedTab -ne $pages.Activity -or $form.ClientSize.Height -ne $height) {throw 'Launch error failed to reveal Activity'}
            $results.Clear(); Focus-Agent 'CARL' 'Agents'
            foreach ($page in $tabs.TabPages) {
                Test-Step ('Bounds: '+$page.Name)
                $tabs.SelectedTab=$page
                foreach ($control in $page.Controls) {
                    if ($control.Visible -and ($control.Right -gt $page.ClientSize.Width -or $control.Bottom -gt $page.ClientSize.Height)) {throw ('Page control exceeds bounds: '+$page.Name+' / '+$control.Text+' / '+$control.Bounds.ToString()+' / page '+$page.ClientSize.ToString())}
                }
            }
            $width=$form.ClientSize.Width
            Test-Step 'Grow window'
            $form.ClientSize=New-Object Drawing.Size(($width+160),$form.ClientSize.Height)
            $resizeEnd=[Windows.Forms.Form].GetMethod('OnResizeEnd',([Reflection.BindingFlags]::Instance -bor [Reflection.BindingFlags]::NonPublic))
            [void]$resizeEnd.Invoke($form,@([EventArgs]::Empty))
            Test-Step 'Check resized controls'
            $tabs.SelectedTab=$pages.Instructions
            if ($preset.Right -ge $usePreset.Left) {throw 'Resized instruction controls overlap'}
            Test-Step 'Restore window size'
            $form.ClientSize=New-Object Drawing.Size($width,$form.ClientSize.Height)
            [void]$resizeEnd.Invoke($form,@([EventArgs]::Empty))
            $retained=@($script:checked.Keys)
            Test-Step 'Full selection overflow'
            foreach ($entry in $data.agents) {$script:checked[$entry.name]=$true}
            $tabs.SelectedTab=$pages.Selected; Update-Buttons; $chips.PerformLayout()
            if ($chips.Controls.Count -ne $data.agents.Count -or $chips.DisplayRectangle.Height -le $chips.ClientSize.Height) {throw 'Full selection does not scroll on Selected page'}
            $script:checked.Clear(); Update-Buttons
            if ($chips.Controls.Count -ne 1 -or $chips.Controls[0] -isnot [Windows.Forms.Label] -or $batch.Enabled) {throw 'Empty selection state failed'}
            foreach ($key in $retained) {$script:checked[$key]=$true}
            Filter-Agents
            if (@(Get-ChildItem -LiteralPath $data.directory -Filter '*.claimed').Count -ne 0) {throw 'Saving/loading/presets started an agent'}
            Test-Step 'Screenshots'
            $status.Text='Ready. Use the tabs to choose agents, prepare instructions, and review activity.'
            $tabs.SelectedTab=$pages.Agents
            $form.Refresh()
            $bitmap=New-Object Drawing.Bitmap($form.Width,$form.Height)
            $form.DrawToBitmap($bitmap,(New-Object Drawing.Rectangle(0,0,$form.Width,$form.Height)))
            $bitmap.Save((Join-Path $data.directory 'preview.png')); $bitmap.Dispose()
            foreach ($page in $tabs.TabPages) {
                $tabs.SelectedTab=$page; $form.Refresh()
                $bitmap=New-Object Drawing.Bitmap($form.Width,$form.Height)
                $form.DrawToBitmap($bitmap,(New-Object Drawing.Rectangle(0,0,$form.Width,$form.Height)))
                $bitmap.Save((Join-Path $data.directory ($page.Name+'.png'))); $bitmap.Dispose()
            }
            @{ok=$true;checks='Categories, retained selection, per-agent runtime/task, hidden preview, CATO, resume, empty search, clear, stop remaining, saved groups, atomic persistence, concurrent/corrupt-file refusal, task presets, group rename/collision, global search/category restore, selected-name navigation and separate removal, tab state/busy queue preservation, custom preset persistence/corruption/concurrency/confirmation, bounded history merging/corruption, Activity errors, page bounds and resize'} | ConvertTo-Json | Set-Content -Encoding UTF8 (Join-Path $data.directory 'smoke.json')
        } catch {
            $bitmap=New-Object Drawing.Bitmap($form.Width,$form.Height)
            $form.DrawToBitmap($bitmap,(New-Object Drawing.Rectangle(0,0,$form.Width,$form.Height)))
            $bitmap.Save((Join-Path $data.directory 'failed.png')); $bitmap.Dispose()
            @{ok=$false;error=$_.Exception.Message} | ConvertTo-Json | Set-Content -Encoding UTF8 (Join-Path $data.directory 'smoke.json')
        } finally {$form.Close()}
    })
}
[void]$form.ShowDialog()
$form.Dispose()
if ($testDeadline) {$testDeadline.Dispose()}

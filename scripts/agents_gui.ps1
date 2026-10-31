param([Parameter(Mandatory=$true)][string]$DataFile, [switch]$SmokeTest)
$ErrorActionPreference = 'Stop'
trap {
    if (-not $SmokeTest -and -not $data.test_mode) {[void][System.Windows.Forms.MessageBox]::Show($_.Exception.Message,'Agent Launcher')}
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
$script:expandedParents=@{}
$script:favorites=@(); $script:favoritesVersion=''; $script:favoritesHealthy=$true
$script:editAll=$true
$script:refreshProcess=$null; $script:refreshFailure=''
$script:queue=New-Object Collections.Queue
$script:active=$null; $script:completed=0; $script:failed=0
foreach ($entry in $data.agents) {
    $script:settings[$entry.name]=@{runtime=$entry.default_runtime;task=$null}
}
$bg=[Drawing.Color]::FromArgb(11,23,42)
$panel=[Drawing.Color]::FromArgb(58,80,104)
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
    public override int ItemHeight { get { return Math.Max(66, Font.Height * 3 + 10); } set { } }
    public System.Collections.Generic.HashSet<int> SectionRows = new System.Collections.Generic.HashSet<int>();
    public System.Collections.Generic.HashSet<int> ChildRows = new System.Collections.Generic.HashSet<int>();
    public event EventHandler SectionToggle;
    public void ToggleSection() {
        if (SectionRows.Contains(SelectedIndex) && SectionToggle != null) SectionToggle(this, EventArgs.Empty);
    }
    protected override void OnItemCheck(ItemCheckEventArgs e) {
        if (SectionRows.Contains(e.Index)) { e.NewValue = CheckState.Unchecked; return; }
        base.OnItemCheck(e);
    }
    protected override void OnMouseDown(MouseEventArgs e) {
        int index = IndexFromPoint(e.Location);
        if (e.Button == MouseButtons.Left && SectionRows.Contains(index)) {
            SelectedIndex = index; ToggleSection(); return;
        }
        base.OnMouseDown(e);
    }
    protected override void OnKeyDown(KeyEventArgs e) {
        if (SectionRows.Contains(SelectedIndex) && (e.KeyCode == Keys.Space || e.KeyCode == Keys.Enter)) {
            ToggleSection(); e.Handled = true; e.SuppressKeyPress = true; return;
        }
        base.OnKeyDown(e);
    }
    public Color AccentColor { get; set; }
    public Color SelectionColor { get; set; }
    public Color MutedColor { get; set; }
    public System.Collections.Generic.Dictionary<int, Color> AgeColors = new System.Collections.Generic.Dictionary<int, Color>();
    protected override void OnDrawItem(DrawItemEventArgs e) {
        if (e.Index < 0 || e.Index >= Items.Count) return;
        bool selected = (e.State & DrawItemState.Selected) != 0;
        Color background = selected ? SelectionColor : BackColor;
        using (var brush = new SolidBrush(background)) e.Graphics.FillRectangle(brush, e.Bounds);
        if (SectionRows.Contains(e.Index)) {
            var section = new Rectangle(e.Bounds.Left + 10, e.Bounds.Top + 4, e.Bounds.Width - 16, e.Bounds.Height - 8);
            TextRenderer.DrawText(e.Graphics, GetItemText(Items[e.Index]), Font, section, AccentColor,
                TextFormatFlags.VerticalCenter | TextFormatFlags.NoPrefix);
            if ((e.State & DrawItemState.Focus) != 0) ControlPaint.DrawFocusRectangle(e.Graphics, e.Bounds, ForeColor, background);
            return;
        }
        int indent = ChildRows.Contains(e.Index) ? 16 : 0;
        int box = Math.Max(12, Math.Min(e.Bounds.Height - 6, Font.Height - 1));
        var bounds = new Rectangle(e.Bounds.Left + 6 + indent, e.Bounds.Top + (e.Bounds.Height - box) / 2, box, box);
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
        string[] lines = GetItemText(Items[e.Index]).Split('\n');
        int height = (e.Bounds.Height - 6) / 3;
        for (int line = 0; line < Math.Min(3, lines.Length); line++) {
            var text = new Rectangle(bounds.Right + 8, e.Bounds.Top + 3 + line * height,
                Math.Max(0, e.Bounds.Right - bounds.Right - 12), height);
            Color color = line == 0 ? ForeColor : MutedColor;
            if (line == 2 && AgeColors.ContainsKey(e.Index)) color = AgeColors[e.Index];
            TextRenderer.DrawText(e.Graphics, lines[line], Font, text, color,
                TextFormatFlags.VerticalCenter | TextFormatFlags.EndEllipsis | TextFormatFlags.NoPrefix);
        }
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
$categoryLabel=Label 'Browse' 26 250 224 26
$categories=New-Object Windows.Forms.ListBox
$categories.SetBounds(26,284,224,328); $categories.BorderStyle='None'
$categories.IntegralHeight=$false; $categories.DrawMode='OwnerDrawFixed'; $categories.ItemHeight=32
$categories.DisplayMember='Display'; $form.Controls.Add($categories)
[void]$categories.Items.Add([pscustomobject]@{Name='__favorites__';Display='Favorites'})
[void]$categories.Items.Add([pscustomobject]@{Name='';Display='All agents'})
foreach ($g in ($data.agents | Select-Object -ExpandProperty group -Unique)) {
    [void]$categories.Items.Add([pscustomobject]@{Name=$g;Display=$g})
}
[void]$categories.Items.Add([pscustomobject]@{Name='__due__';Display='Due today / overdue'})
$categories.Add_DrawItem({
    param($sender,$e)
    if ($e.Index -lt 0) {return}
    $fill=$surface; $text=$muted
    if (($e.State -band [Windows.Forms.DrawItemState]::Selected) -ne 0) {$fill=$selection; $text=$accent}
    $brush=New-Object Drawing.SolidBrush($fill)
    try {$e.Graphics.FillRectangle($brush,$e.Bounds)} finally {$brush.Dispose()}
    $rect=New-Object Drawing.Rectangle(($e.Bounds.X+9),$e.Bounds.Y,($e.Bounds.Width-16),$e.Bounds.Height)
    [Windows.Forms.TextRenderer]::DrawText($e.Graphics,$sender.Items[$e.Index].Display,$sender.Font,$rect,$text,([Windows.Forms.TextFormatFlags]::WordBreak -bor [Windows.Forms.TextFormatFlags]::VerticalCenter -bor [Windows.Forms.TextFormatFlags]::NoPrefix))
    $e.DrawFocusRectangle()
})
$searchLabel=Label 'Find an agent' 274 111 238 26
$search=New-Object Windows.Forms.TextBox
$search.SetBounds(274,145,238,30); $form.Controls.Add($search)
$list=New-Object LauncherAgentList
$list.AccentColor=$accent; $list.SelectionColor=$selection; $list.MutedColor=$muted
$list.SetBounds(274,188,238,424); $list.IntegralHeight=$false
$list.BorderStyle='None'; $list.Font=New-Object Drawing.Font('Segoe UI',11)
$list.ItemHeight=44
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
$group.UseMnemonic=$false
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
foreach ($key in @('Agents','Selected','Instructions','Activity','Research','Decisions')) {
    $page=New-Object Windows.Forms.TabPage
    $page.Name=$key; $page.Text=$key; $page.BackColor=$panel; $page.ForeColor=$ink
    if ($key -eq 'Selected') {$page.Text='Selected & groups'}
    [void]$tabs.TabPages.Add($page); $pages[$key]=$page
}
# Inactive TabPages initially use a small default size. Establish their real
# bounds before anchoring children, otherwise their first display stretches twice.
foreach ($page in $tabs.TabPages) {$page.Bounds=$tabs.DisplayRectangle}
$tabs.ItemSize=New-Object Drawing.Size(([int](($tabs.Width-8)/$tabs.TabPages.Count)),38)
# Changing native tab metrics inside SizeChanged feeds back into its layout.
# Resize the headers once after a user drag instead of inside that event.
$form.Add_ResizeEnd({$tabs.ItemSize=New-Object Drawing.Size(([int](($tabs.Width-8)/$tabs.TabPages.Count)),38)})
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
Place $categoryLabel $pages.Agents 16 16 196 26
Place $categories $pages.Agents 16 50 196 370 'Top,Bottom,Left'
$reloadFavorites=New-Object Windows.Forms.LinkLabel
$reloadFavorites.Text='Reload favorites'; $reloadFavorites.LinkColor=$accent; $reloadFavorites.ActiveLinkColor=$accent
Place $reloadFavorites $pages.Agents 16 426 196 24 'Bottom,Left'
Place $searchLabel $pages.Agents 230 16 320 26
Place $search $pages.Agents 230 50 320 30
$searchScope=Label 'Browse by category, or search all agents.' 0 0 1 1 9
Place $searchScope $pages.Agents 230 88 320 34
$searchScope.ForeColor=$muted
$ageSource=New-Object Windows.Forms.ComboBox
$ageSource.DropDownStyle='DropDownList'; Style-Input $ageSource
[void]$ageSource.Items.Add('Last launch here'); [void]$ageSource.Items.Add('Last saved work')
[void]$ageSource.Items.Add('Due work')
$ageSource.SelectedIndex=0
Place $ageSource $pages.Agents 16 460 196 30 'Bottom,Left'
$tooltip.SetToolTip($ageSource,'Choose the evidence used for age highlighting. Neither source proves the agent is idle or needs a new session.')
Place $list $pages.Agents 230 124 320 370 'Top,Bottom,Left'
$ageLegend=Label 'Amber: 7+ days. Orange: 14+ days. Missing history stays neutral.' 0 0 1 1 9
$ageLegend.ForeColor=$muted
Place $ageLegend $pages.Agents 16 496 196 34 'Bottom,Left'
Place $count $pages.Agents 230 498 320 24 'Bottom,Left'
Place $name $pages.Agents 576 16 300 38 'Top,Left,Right'
$favoriteButton=Button 'Add favorite' 0 0 1
Place $favoriteButton $pages.Agents 890 16 178 34 'Top,Right'
$tooltip.SetToolTip($favoriteButton,'Pin this agent to Favorites. This does not check it for launch.')
Place $purpose $pages.Agents 576 62 492 46 'Top,Left,Right'
Place $group $pages.Agents 576 112 492 24 'Top,Left,Right'
$recentDetails=New-Object Windows.Forms.TextBox
$recentDetails.Multiline=$true; $recentDetails.ReadOnly=$true; $recentDetails.ScrollBars='Vertical'
Style-Input $recentDetails
Place $recentDetails $pages.Agents 576 144 492 128 'Top,Left,Right'
Place $runtimeLabel $pages.Agents 576 282 492 25 'Top,Left,Right'
Place $runtime $pages.Agents 576 310 492 32 'Top,Left,Right'
$taskSummary=New-Object Windows.Forms.TextBox
$taskSummary.Multiline=$true; $taskSummary.ReadOnly=$true; $taskSummary.ScrollBars='Vertical'
Style-Input $taskSummary
Place $taskSummary $pages.Agents 576 354 492 62 'Top,Left,Right'
$editInstructions=Button 'Edit instructions...' 0 0 1
Place $editInstructions $pages.Agents 576 422 492 32 'Top,Left,Right'
Place $start $pages.Agents 576 462 236 32
Place $resume $pages.Agents 828 462 240 32 'Top,Right'
Place $hint $pages.Agents 576 498 492 30 'Top,Left,Right'

Place $savedLabel $pages.Selected 16 16 500 26
Place $savedGroups $pages.Selected 16 50 500 32
Place $loadGroup $pages.Selected 528 46 140 40
Place $groupActions $pages.Selected 680 46 140 40
$groupHint=Label 'Groups remember agents and runtimes. Click an agent below to edit its instructions.' 0 0 1 1 10
Place $groupHint $pages.Selected 16 102 1052 36 'Top,Left,Right'
$groupHint.ForeColor=$muted
Place $selectionLabel $pages.Selected 16 148 1052 26 'Top,Left,Right'
Place $chips $pages.Selected 16 184 1052 310 'Top,Bottom,Left,Right'
$chips.FlowDirection='TopDown'; $chips.WrapContents=$false; $chips.BackColor=$panel

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
$editAllAgents=New-Object Windows.Forms.CheckBox
$editAllInstructions=New-Object Windows.Forms.CheckBox
foreach ($control in @($editAllAgents,$editAllInstructions)) {
    $control.Text='Apply edits to all selected agents'; $control.ForeColor=$accent
    $control.Checked=$true
}
$runtimeLabel.Width=110
Place $editAllAgents $pages.Agents 670 282 398 25 'Top,Right'
$instructionAgentLabel.Width=170
Place $editAllInstructions $pages.Instructions 220 16 450 26 'Top,Left,Right'
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
$reloadActivity=Button 'Reload launch history' 0 0 1
Place $reloadActivity $pages.Activity 20 454 172 40 'Bottom,Left'
$refreshEvidence=Button 'Refresh Git / due' 0 0 1
Place $refreshEvidence $pages.Activity 202 454 172 40 'Bottom,Left'
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
. (Join-Path $PSScriptRoot 'research_reader.ps1')
. (Join-Path $PSScriptRoot 'decisions_launcher.ps1')
$form.KeyPreview=$true
$form.Add_KeyDown({
    param($sender,$e)
    if ($e.Control -and $e.KeyCode -eq [Windows.Forms.Keys]::F -and $tabs.SelectedTab -eq $pages.Research) {
        $readerFind.Focus(); $readerFind.SelectAll(); $e.SuppressKeyPress=$true
    } elseif ($e.Control -and $tabs.SelectedTab -eq $pages.Research -and $e.KeyCode -in @('Add','Oemplus','Subtract','OemMinus')) {
        if ($e.KeyCode -in @('Add','Oemplus')) {$readerZoomIn.PerformClick()} else {$readerZoomOut.PerformClick()}
        $e.SuppressKeyPress=$true
    } elseif ($e.Control -and $e.KeyCode -eq [Windows.Forms.Keys]::F -and -not $script:busy) {
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
function Select-Category($category) {
    foreach ($item in $categories.Items) {if ($item.Name -ceq $category) {$categories.SelectedItem=$item; return}}
}
function Focus-Agent($agentName,$page='Instructions') {
    if ($script:busy) {return}
    $script:editAll=$false
    $entry=@($data.agents | Where-Object {$_.name -eq $agentName})
    if ($entry.Count -eq 1 -and $entry[0].parent) {$script:expandedParents[$entry[0].parent]=$true}
    $script:filtering=$true
    try {Select-Category ''; $search.Clear()} finally {$script:filtering=$false}
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
                $remove.Add_Click({param($sender,$e) $script:checked.Remove([string]$sender.Tag); $script:editAll=$true; Filter-Agents})
                $card.Controls.Add($remove); $chips.Controls.Add($card)
            }
        } finally {$chips.ResumeLayout()}
    }
    foreach ($card in $chips.Controls) {
        $card.Enabled=-not $script:busy
        if ($card -is [Windows.Forms.Panel]) {
            $setting=$script:settings[[string]$card.Tag]
            $label=@{sol='Codex Sol';claude='Claude (model unrecorded)';astra='Codex Astra';opus='Claude Opus';fable='Claude Fable'}[$setting.runtime]
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
$script:favoritesPath=Join-Path $preferencesFolder 'favorites.json'
$script:customPresets=@(); $script:presetVersion=''; $script:presetsHealthy=$true
$script:history=@()
$script:lastOpened=@(); $script:historyHealthy=$true
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
                if ($m.name -isnot [string] -or $m.name -notmatch '^[A-Z][A-Z0-9_-]*$' -or $m.runtime -notin @('sol','claude','astra','opus','fable') -or $members.ContainsKey($m.name)) {throw 'Saved group has an invalid or duplicate agent. The file was not changed.'}
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
        $allowed=@('sol','astra','opus','fable','claude')
        if ($entry[0].kind -eq 'cato') {$allowed=@('astra','sol')}
        if ($member.runtime -notin $allowed) {throw ('Unsupported saved runtime for '+$member.name+'. Your current selection was kept.')}
    }
    $script:checked.Clear()
    $script:editAll=$true
    foreach ($member in $g.members) {
        $script:checked[$member.name]=$true
        $value=$member.runtime
        if ($value -eq 'claude') {$value='opus'; if ($member.name -eq 'PROME') {$value='fable'}}
        $script:settings[$member.name].runtime=$value
    }
    Select-Category ''; $search.Clear(); Filter-Agents
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
    @{name='Prepare handoff';text='Follow your startup instructions and recover current work and approvals. Prepare your normal handoff and closeout for the existing assignment. Preserve unfinished work, blockers, approval conditions, and a clear resume point. Do not start new research or unrelated pending work.'},
    @{name='CATCH-UP';text='Follow your startup instructions and recover current work, existing approvals, and unresolved conditions. Bring your files and folders current with new data within your approved workstreams. Drain your inbox under your normal owner protocol. Work owed and incomplete items that are already authorized and currently in scope. Preserve existing approval conditions; return new directions or unclear authority to Will. Close out under your normal protocol and report the results, remaining work, and next stopping point. Follow PROME/COMPLETION_SPEC.md for delivery.'},
    @{name='ORACLE daily read';text='ORACLE daily read: boot, run `python3 tools/routine_check.py` and report any NOT READ day, take today''s business-day read (Polymarket and Kalshi `pull --log`, spread tool) unless the scheduled routine already logged one, grade the logged rows on `workbook/V5_NOV110_READS.tsv` against VX-ORC-04 and VX-ORC-12, packet PROME on any state change, then close out.'}
)
function Validate-LocalRecords($document,$kind) {
    if ($document.version -ne 1 -or $document.$kind -isnot [Array]) {throw ('Unsupported '+$kind+' file format. The original file was kept.')}
    $seen=@{}
    $items=@($document.$kind)
    if ($kind -eq 'history' -and $null -ne $document.PSObject.Properties['last_opened']) {
        if ($document.last_opened -isnot [Array]) {throw 'Invalid last-launch summary. The original file was kept.'}
        foreach ($last in $document.last_opened) {
            if ($last.outcome -ne 'Opened') {throw 'Unconfirmed entry in last-launch summary. The original file was kept.'}
        }
        $items+=@($document.last_opened)
    }
    foreach ($item in $items) {
        if ($kind -eq 'favorites') {
            if ($item.name -isnot [string] -or $item.name -notmatch '^[A-Z][A-Z0-9_-]*$' -or $seen.ContainsKey($item.name)) {throw 'Invalid or duplicate favorite. The original file was kept.'}
            $seen[$item.name]=$true
        } elseif ($kind -eq 'presets') {
            if ($item.name -isnot [string] -or [string]::IsNullOrWhiteSpace($item.name) -or $item.name.Length -gt 60 -or $item.name -match '[\x00-\x1f]' -or $seen.ContainsKey($item.name) -or $item.text -isnot [string] -or [string]::IsNullOrWhiteSpace($item.text) -or $item.text.Length -gt 32767) {throw 'Invalid or duplicate custom preset. The original file was kept.'}
            if (@($builtInPresets | Where-Object {$_.name -eq $item.name}).Count -gt 0) {throw 'A custom preset uses a built-in name. The original file was kept.'}
            $seen[$item.name]=$true
        } else {
            $timestamp=[DateTimeOffset]::MinValue
            if ($item.name -isnot [string] -or $item.name -notmatch '^[A-Z][A-Z0-9_-]*$' -or $item.runtime -notin @('sol','claude','astra','opus','fable') -or $item.action -notin @('new','resume') -or $item.outcome -notin @('Opened','Not confirmed','Cancelled') -or $item.message -isnot [string] -or $item.task -isnot [string] -or -not [DateTimeOffset]::TryParse([string]$item.time,[ref]$timestamp)) {throw 'Invalid launch history. The original file was kept.'}
        }
    }
}
function Latest-Launches($records) {
    $latest=@{}
    foreach ($record in $records) {
        if ($null -eq $record -or $record.outcome -ne 'Opened') {continue}
        if (-not $latest.ContainsKey($record.name) -or [DateTimeOffset]::Parse($record.time) -gt [DateTimeOffset]::Parse($latest[$record.name].time)) {$latest[$record.name]=$record}
    }
    return @($latest.Values | Sort-Object name)
}
function Read-LocalRecords($path,$kind) {
    $text=''; $records=@(); $lastOpened=@()
    if ([IO.File]::Exists($path)) {
        $text=[IO.File]::ReadAllText($path)
        if (-not $text.Trim()) {throw ('The '+$kind+' file is empty. It was kept.')}
        $document=$text | ConvertFrom-Json
        Validate-LocalRecords $document $kind
        $records=@($document.$kind)
        if ($kind -eq 'history') {$lastOpened=@(Latest-Launches (@($document.last_opened)+$records))}
    }
    return @{text=$text;records=$records;lastOpened=$lastOpened}
}
function Write-LocalRecords($path,$kind,$items,$expected,$append=$false) {
    $hash=[Security.Cryptography.SHA256]::Create()
    $key=[BitConverter]::ToString($hash.ComputeHash([Text.Encoding]::UTF8.GetBytes($path))).Replace('-',''); $hash.Dispose()
    $mutex=New-Object Threading.Mutex($false,('Local\AgentLauncherRecords-'+$key)); $locked=$false
    try {
        try {$locked=$mutex.WaitOne(1500)} catch [Threading.AbandonedMutexException] {$locked=$true}
        if (-not $locked) {throw 'Another launcher is saving. Try again shortly.'}
        $current=Read-LocalRecords $path $kind
        if (-not $append -and $current.text -cne $expected) {throw ('The '+$kind+' file changed in another window. Reload it before saving.')}
        $records=@($items)
        $lastOpened=@()
        if ($kind -eq 'history') {$lastOpened=@(Latest-Launches (@($current.lastOpened)+@($current.records)+@($items)))}
        if ($append) {$records=@(@($current.records)+@($items) | Select-Object -Last 100)}
        $document=@{version=1}; $document[$kind]=$records
        if ($kind -eq 'history') {$document['last_opened']=$lastOpened}
        Validate-LocalRecords $document $kind
        [void][IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($path))
        $text=$document | ConvertTo-Json -Depth 8
        $temporary=$path+'.'+[Guid]::NewGuid().ToString('N')+'.tmp'
        [IO.File]::WriteAllText($temporary,$text,(New-Object Text.UTF8Encoding($false)))
        if ([IO.File]::Exists($path)) {[IO.File]::Replace($temporary,$path,($path+'.previous'))} else {[IO.File]::Move($temporary,$path)}
        return @{text=$text;records=$records;lastOpened=$lastOpened}
    } finally {
        if ($locked) {$mutex.ReleaseMutex()}; $mutex.Dispose()
    }
}
function Reload-Favorites {
    try {
        $saved=Read-LocalRecords $script:favoritesPath 'favorites'
        $script:favorites=@($saved.records); $script:favoritesVersion=$saved.text; $script:favoritesHealthy=$true
    } catch {
        $script:favoritesHealthy=$false
        $status.Text='Favorites could not be read. Reload favorites after repairing the file.'
        Log-Result ($_.Exception.Message+' File: '+$script:favoritesPath)
    }
}
function Toggle-Favorite {
    if (-not $script:selected -or $script:busy) {return}
    try {
        if (-not $script:favoritesHealthy) {throw 'Favorites could not be read. Reload favorites before saving; the original file is kept.'}
        $agentName=$script:selected.name
        $items=@($script:favorites | Where-Object {$_.name -ne $agentName})
        $removing=($items.Count -ne $script:favorites.Count)
        if (-not $removing) {$items+=@{name=$agentName}}
        $saved=Write-LocalRecords $script:favoritesPath 'favorites' $items $script:favoritesVersion
        $script:favorites=@($saved.records); $script:favoritesVersion=$saved.text
        Filter-Agents
        $verb='Added to'; if ($removing) {$verb='Removed from'}
        $status.Text=$agentName+': '+$verb+' Favorites.'
    } catch {$status.Text=$_.Exception.Message; $tooltip.SetToolTip($status,$status.Text)}
}
function Toggle-Specialists {
    if ($script:busy -or -not $list.SelectedItem.SectionParent) {return}
    $parent=$list.SelectedItem.SectionParent
    if ($script:expandedParents.ContainsKey($parent)) {$script:expandedParents.Remove($parent)} else {$script:expandedParents[$parent]=$true}
    Filter-Agents $parent
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
    $label=@{sol='Codex Sol';claude='Claude (model unrecorded)';astra='Codex Astra';opus='Claude Opus';fable='Claude Fable'}[$record.runtime]
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
        $script:lastOpened=@($saved.lastOpened); $script:historyHealthy=$true
    } catch {
        $script:historyHealthy=$false
        $script:history=@(@($script:history)+$record | Select-Object -Last 100)
        Log-Result ('Launch history not saved: '+$_.Exception.Message)
    }
    Refresh-History
    Filter-Agents
}
function Launch-For($agentName) {
    if (-not $script:historyHealthy) {return $null}
    return @($script:lastOpened | Where-Object {$_.name -eq $agentName} | Select-Object -First 1)[0]
}
function Activity-Age($stamp,$now=[DateTimeOffset]::Now) {
    $parsed=[DateTimeOffset]::MinValue
    if (-not [DateTimeOffset]::TryParse([string]$stamp,[ref]$parsed)) {return @{label='No record';color=$muted;days=$null}}
    $age=($now-$parsed).TotalDays
    if ($age -lt 0) {return @{label='Clock ahead';color=$muted;days=$null}}
    $days=[int][Math]::Floor($age); $color=$ink; $label='Today'
    if ($days -gt 0) {$label=[string]$days+'d ago'}
    if ($days -ge 14) {$color=[Drawing.Color]::FromArgb(255,166,102)}
    elseif ($days -ge 7) {$color=[Drawing.Color]::FromArgb(245,210,125)}
    return @{label=$label;color=$color;days=$days}
}
function Show-RecentDetails {
    if ($null -eq $script:selected) {$recentDetails.Clear();return}
    $entry=$script:selected; $launch=Launch-For $entry.name
    $launchText='No launch recorded here'
    if (-not $script:historyHealthy) {$launchText='History unavailable (see Activity)'}
    elseif ($launch) {
        $label=@{sol='Codex Sol';claude='Claude (model unrecorded)';astra='Codex Astra';opus='Claude Opus';fable='Claude Fable'}[$launch.runtime]
        $launchText=([DateTimeOffset]::Parse($launch.time)).LocalDateTime.ToString('MMM d, yyyy HH:mm')+' | '+$label+' | '+$launch.action
        if ((Activity-Age $launch.time).label -eq 'Clock ahead') {$launchText+=' (clock ahead)'}
    }
    $work=$entry.saved_work; $workText='Unavailable'; $commit=''
    if ($work.state -eq 'recorded') {
        $workText=([DateTimeOffset]::Parse($work.time)).LocalDateTime.ToString('MMM d, yyyy HH:mm')
        if ((Activity-Age $work.time).label -eq 'Clock ahead') {$workText+=' (clock ahead)'}
        $commit="`r`n"+$work.subject+' ['+$work.revision.Substring(0,9)+']'
    } elseif ($work.message) {$workText=$work.message}
    $snapshot='when this window opened'
    if ($data.captured_at) {$snapshot=([DateTimeOffset]::Parse($data.captured_at)).LocalDateTime.ToString('MMM d HH:mm')}
    $recentDetails.Text='Last launch here: '+$launchText+"`r`nLast saved work: "+$workText+$commit+"`r`n`r`n"+(Due-Details $entry)+"`r`n`r`nLaunch history is local; manual and PROME starts may be absent. Saved work is a folder commit, not proof the agent ran. Evidence checked "+$snapshot+'; refresh on Activity.'
    if ($script:refreshFailure) {$recentDetails.AppendText("`r`nRefresh failed: "+$script:refreshFailure+' Previous snapshot retained.')}
}
function Reload-Activity {
    try {
        $saved=Read-LocalRecords $script:historyPath 'history'
        $script:history=@($saved.records); $script:lastOpened=@($saved.lastOpened); $script:historyHealthy=$true
    } catch {
        $script:historyHealthy=$false
        Log-Result ('Launch history unavailable: '+$_.Exception.Message)
    }
    Refresh-History; Filter-Agents
}
function Due-Label($entry) {
    $due=$entry.due_work
    if (-not $due -or $due.state -ne 'available') {return 'Due unavailable'}
    $parts=@()
    if ($due.overdue -gt 0) {$parts+=('OVERDUE '+$due.overdue)}
    if ($due.today -gt 0) {$parts+=('DUE '+$due.today)}
    if ($due.unknown -gt 0) {$parts+=('UNDATED '+$due.unknown)}
    if ($parts.Count -eq 0 -and @($due.other_rows | Where-Object {$_.timing -ne 'future'}).Count -gt 0) {return 'Operator / unmapped due'}
    if ($parts.Count -eq 0) {return 'No docket work due'}
    return $parts -join ' / '
}
function Due-Details($entry) {
    $due=$entry.due_work
    if (-not $due -or $due.state -ne 'available') {return 'Docket due work unavailable; this does not mean nothing is owed.'}
    $lines=@('Docket work as of '+$due.as_of+' (Eastern; GATES not included):')
    foreach ($row in $due.rows) {
        $lines+=($row.key+' | '+$row.date+' | '+$row.owner+"`r`n"+$row.description+"`r`n"+$row.state)
        if ($row.covered) {$lines+=('COVERED: '+$row.coverage)}
        if ($row.notes) {$lines+=('Notes: '+$row.notes)}
    }
    if (@($due.rows).Count -eq 0) {$lines+='No open docket rows assigned to this desk in this snapshot.'}
    if (@($due.other_rows).Count -gt 0) {
        $lines+='Operator / unmatched-owner rows (not counted as PROME work):'
        foreach ($row in $due.other_rows) {
            $lines+=($row.key+' | '+$row.date+' | '+$row.owner+' | '+$row.description+' | '+$row.state)
            if ($row.covered) {$lines+=('COVERED: '+$row.coverage)}
            if ($row.notes) {$lines+=('Notes: '+$row.notes)}
        }
    }
    $lines+='Badges follow the first named docket owner; full owner text is shown above.'
    $lines+='Owed is not the same as should launch. COVERED and Will-owned rows are listed, not recommended.'
    return $lines -join "`r`n"
}
function Start-EvidenceRefresh {
    if ($script:busy -or $script:refreshProcess) {return}
    try {
        $id=[Guid]::NewGuid().ToString('N')
        $script:refreshResult=Join-Path $data.directory ($id+'.result.json')
        $values=@('-d',$data.distro,'-u',$data.user,'--exec',$data.python,$data.bridge,'--refresh',($data.linux_directory+'/'+$id+'.json'))
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
        $script:refreshProcess=[Diagnostics.Process]::Start($psi)
        $script:refreshOutput=$script:refreshProcess.StandardOutput.ReadToEndAsync()
        $script:refreshError=$script:refreshProcess.StandardError.ReadToEndAsync()
        $script:refreshStarted=[DateTime]::UtcNow
        $status.Text='Refreshing Git and docket evidence; your prepared settings are kept.'
    } catch {$script:refreshFailure=$_.Exception.Message; $status.Text='Refresh failed: '+$script:refreshFailure}
    Update-Buttons
}
function Apply-EvidenceSnapshot($snapshot) {
    if (-not $snapshot.ok) {throw ('Refresh failed: '+$snapshot.message)}
    if (-not $snapshot.captured_at -or @($snapshot.agents).Count -ne @($data.agents).Count) {throw 'Catalogue changed or refresh is incomplete. Reopen to load configuration changes.'}
    $stamp=[DateTimeOffset]::Parse($snapshot.captured_at)
    foreach ($entry in $data.agents) {
        $matches=@($snapshot.agents | Where-Object {$_.name -ceq $entry.name})
        if ($matches.Count -ne 1 -or -not $matches[0].saved_work -or -not $matches[0].due_work -or -not $matches[0].prome_touch) {throw 'Refresh is incomplete; previous snapshot retained.'}
    }
    foreach ($entry in $data.agents) {
        $fresh=@($snapshot.agents | Where-Object {$_.name -ceq $entry.name})[0]
        foreach ($field in @('saved_work','due_work','prome_touch')) {$entry | Add-Member -NotePropertyName $field -NotePropertyValue $fresh.$field -Force}
    }
    $data | Add-Member -NotePropertyName captured_at -NotePropertyValue $snapshot.captured_at -Force
    $script:refreshFailure=''
    Filter-Agents
    $status.Text='Evidence refreshed '+$stamp.LocalDateTime.ToString('HH:mm')+'. Selections and prepared settings kept.'
}
function Poll-EvidenceRefresh {
    if (-not $script:refreshProcess) {return}
    $finished=$false
    try {
        if (Test-Path -LiteralPath $script:refreshResult) {
            $finished=$true
            Apply-EvidenceSnapshot (Get-Content -LiteralPath $script:refreshResult -Raw | ConvertFrom-Json)
        } elseif ($script:refreshProcess.HasExited) {
            $finished=$true
            throw ('Refresh did not return evidence: '+$script:refreshError.Result)
        } elseif (([DateTime]::UtcNow-$script:refreshStarted).TotalSeconds -gt 90) {
            $finished=$true
            throw 'Refresh timed out. Previous snapshot retained.'
        }
    } catch {
        $script:refreshFailure=$_.Exception.Message
        $status.Text=$script:refreshFailure; Show-RecentDetails
    } finally {
        if ($finished) {$script:refreshProcess.Dispose(); $script:refreshProcess=$null; Update-Buttons}
    }
}
function Apply-Preset($toChecked) {
    if ($script:busy -or $preset.SelectedIndex -lt 0) {return}
    $names=@()
    if ($toChecked) {$names=@($script:checked.Keys)} else {$names=@(Edit-Names)}
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
    $favoriteButton.Enabled=($null -ne $script:selected -and -not $script:busy -and $script:favoritesHealthy)
    $favoriteButton.Text='Add favorite'
    if ($script:selected -and @($script:favorites | Where-Object {$_.name -eq $script:selected.name}).Count -gt 0) {$favoriteButton.Text='Remove favorite'}
    $reloadFavorites.Enabled=-not $script:busy
    $ageSource.Enabled=-not $script:busy
    $reloadActivity.Enabled=-not $script:busy
    $refreshEvidence.Enabled=(-not $script:busy -and $null -eq $script:refreshProcess)
    $ready=(@(Edit-Names).Count -gt 0 -and -not $script:busy)
    $single=($null -ne $script:selected -and -not (Editing-All) -and -not $script:busy -and $null -eq $script:refreshProcess)
    $start.Enabled=$single
    $resume.Enabled=($single -and [string]::IsNullOrWhiteSpace($task.Text))
    $instructionStart.Enabled=$start.Enabled; $instructionResume.Enabled=$resume.Enabled
    $editInstructions.Enabled=$ready
    $instructionAgent.Enabled=-not $script:busy
    $editAllAgents.Enabled=($script:checked.Count -gt 1 -and -not $script:busy)
    $editAllInstructions.Enabled=$editAllAgents.Enabled
    $instructionRuntime.Enabled=$ready
    $runtime.Enabled=$ready
    $task.Enabled=$ready
    $search.Enabled=-not $script:busy; $list.Enabled=-not $script:busy; $categories.Enabled=-not $script:busy
    $batch.Enabled=($script:checked.Count -gt 0 -and -not $script:busy -and $null -eq $script:refreshProcess)
    $noun=' agents'; if ($script:checked.Count -eq 1) {$noun=' agent'}
    $batch.Text='Review & launch '+$script:checked.Count+$noun
    $clear.Enabled=($script:checked.Count -gt 0 -and -not $script:busy)
    $clear.Visible=-not $script:busy; $stop.Visible=$script:busy
    $stop.Enabled=($script:queue.Count -gt 0)
    foreach ($index in $list.SectionRows) {
        $item=$list.Items[$index]
        $children=@($data.agents | Where-Object {$_.parent -eq $item.SectionParent})
        $selectedChildren=@($children | Where-Object {$script:checked.ContainsKey($_.name)}).Count
        $verb='Show'; if ($script:expandedParents.ContainsKey($item.SectionParent)) {$verb='Hide'}
        $item.Display=$verb+' consumer specialists ('+$children.Count+")`n"+$selectedChildren+' selected; click or press Enter'
    }
    $list.Invalidate()
    $count.Text=[string]@($list.Items | Where-Object {$_.Entry}).Count+' shown / '+$script:checked.Count+' selected'
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
    if ($taskLabel.Text -like 'Different instructions*') {$taskSummary.Text='Different instructions across selected agents. Edit instructions to replace them for all.'}
    if (-not [string]::IsNullOrWhiteSpace($task.Text)) {
        $taskSummary.Text='Instructions: '+$task.Text
    }
    $tooltip.SetToolTip($taskSummary,$task.Text)
    $historyOpen.Enabled=($null -ne $historyList.SelectedItem -and -not $script:busy)
}
function Editing-All {return ($script:editAll -and $script:checked.Count -gt 1)}
function Edit-Names {
    if (Editing-All) {return @($data.agents | Where-Object {$script:checked.ContainsKey($_.name)} | ForEach-Object {$_.name})}
    if ($script:selected) {return @($script:selected.name)}
}
function Sync-Editors {
    $script:loading=$true
    try {
        $editAllAgents.Checked=$script:editAll; $editAllInstructions.Checked=$script:editAll
        $names=@(Edit-Names)
        $runtime.Items.Clear(); $instructionRuntime.Items.Clear()
        $task.Clear()
        if ($names.Count -eq 0) {return}
        $labels=@{sol='Codex Sol';astra='Codex Astra';opus='Claude Opus';fable='Claude Fable'}
        $choices=@('sol','opus','astra','fable')
        $cato=@($data.agents | Where-Object {$_.name -in $names -and $_.kind -eq 'cato'}).Count -gt 0
        if ($cato) {$choices=@('astra','sol')}
        foreach ($value in $choices) {
            [void]$runtime.Items.Add($labels[$value]); [void]$instructionRuntime.Items.Add($labels[$value])
        }
        $models=@($names | ForEach-Object {$script:settings[$_].runtime} | Select-Object -Unique)
        if ($models.Count -eq 1) {$runtime.SelectedItem=$labels[$models[0]]}
        $instructionRuntime.SelectedIndex=$runtime.SelectedIndex
        $texts=@($names | ForEach-Object {[string]$script:settings[$_].task} | Select-Object -Unique)
        if ($texts.Count -eq 1) {$task.Text=$texts[0]}
        $scope='this agent'
        if (Editing-All) {$scope='all '+$names.Count+' selected agents'}
        $taskLabel.Text='Instructions for '+$scope+' (optional)'
        if ($texts.Count -gt 1) {$taskLabel.Text='Different instructions - typing replaces instructions for '+$scope}
        $runtimeLabel.Text='Model'; $instructionRuntimeLabel.Text='Model'
        if ($models.Count -gt 1) {$runtimeLabel.Text='Mixed models'; $instructionRuntimeLabel.Text='Mixed models - choose to apply'}
        $instructionHint.Text='Instructions apply to a new conversation. Clear them to enable Resume.'
        $hint.Text='These buttons open the highlighted agent. Clear instructions to enable Resume.'
        if (Editing-All) {$instructionHint.Text='Editing '+$scope+'. Choose an agent above for individual edits; use Review & launch below.'}
        if ($cato -and (Editing-All)) {$instructionHint.Text='Editing '+$scope+'. CATO supports Codex only. Choose an agent above for individual edits.'}
        if (Editing-All) {$hint.Text='Use Review & launch for the selection. Uncheck Apply edits for individual controls.'}
        $tooltip.SetToolTip($runtime,$instructionHint.Text)
        $tooltip.SetToolTip($usePreset,'Apply this preset to '+$scope+', then edit the instructions as needed.')
    } finally {$script:loading=$false; Update-Buttons}
}
function Save-Settings($field) {
    if ($script:loading -or $script:busy) {return}
    $names=@(Edit-Names)
    if ($names.Count -eq 0) {return}
    if ($field -eq 'task') {
        foreach ($key in $names) {$script:settings[$key].task=$task.Text}
        $scope='this agent'; if (Editing-All) {$scope='all '+$names.Count+' selected agents'}
        $taskLabel.Text='Instructions for '+$scope+' (optional)'
        Update-Buttons; return
    }
    if ($runtime.SelectedIndex -lt 0) {return}
    $value='sol'
    if ($runtime.Text -eq 'Claude Opus') {$value='opus'}
    if ($runtime.Text -eq 'Claude Fable') {$value='fable'}
    if ($runtime.Text -eq 'Codex Astra') {$value='astra'}
    foreach ($key in $names) {$script:settings[$key].runtime=$value}
    $script:loading=$true
    try {$instructionRuntime.SelectedIndex=$runtime.SelectedIndex} finally {$script:loading=$false}
    $runtimeLabel.Text='Model'; $instructionRuntimeLabel.Text='Model'
    Update-Buttons
}
function Select-Agent {
    if ($script:filtering) {return}
    $script:loading=$true
    try {
        $runtime.Items.Clear()
        if ($null -eq $list.SelectedItem -or $null -eq $list.SelectedItem.Entry) {
            $script:selected=$null; $name.Text='No matching agents'; $purpose.Text='Try another name or category.'
            if ($list.SelectedItem.SectionParent) {$name.Text='Consumer specialists'; $purpose.Text='Click this section or press Enter to expand or collapse it.'}
            elseif ($categories.SelectedItem.Name -eq '__favorites__' -and -not $search.Text.Trim()) {
                $name.Text='Your favorites'; $purpose.Text='Choose an agent in All agents, then Add favorite to pin it here.'
                if (-not $script:favoritesHealthy) {$purpose.Text='Favorites could not be read. Your file is preserved; use Reload favorites after repairing it.'}
            }
            $recentDetails.Clear()
            $group.Text=''; $task.Text=''; $instructionAgent.SelectedIndex=-1; $instructionRuntime.Items.Clear(); return
        }
        $script:selected=$list.SelectedItem.Entry
        Show-RecentDetails
        $name.Text=$script:selected.name; $purpose.Text=$script:selected.purpose; $group.Text=$script:selected.group
        $instructionAgent.SelectedItem=$script:selected.name
        $status.Text='Ready. Each conversation opens in its own terminal.'
        if ($script:selected.error) {$status.Text=$script:selected.error}
        $tooltip.SetToolTip($status,$status.Text); $tooltip.SetToolTip($name,$script:selected.folder)
    } finally {$script:loading=$false; Sync-Editors}
}
function Filter-Agents($focusName='') {
    if ($script:filtering) {return}
    $previous=$null
    if ($script:selected) {$previous=$script:selected.name}
    if ($focusName) {$previous=$focusName}
    $query=$search.Text.Trim(); $category=''
    if ($categories.SelectedItem) {$category=$categories.SelectedItem.Name}
    $searchScope.Text='Browsing the selected category'
    if ($query) {$searchScope.Text='Searching all agents (Ctrl+F)'}
    $basis='since last launch here'
    if ($ageSource.SelectedIndex -eq 1) {$basis='since last saved work'}
    $ageLegend.Text='Amber: 7+ days; orange: 14+ days '+$basis+'.'
    if ($ageSource.SelectedIndex -eq 2) {$ageLegend.Text='Docket: amber = due today; orange = overdue. Unknown dates stay neutral.'}
    if ($category -eq '__due__') {$searchScope.Text='Due docket work, including unknown evidence'}
    if ($category -eq '__favorites__' -and -not $query) {$searchScope.Text='Your pinned agents; check to select for launch'}
    if ($category -eq '__favorites__' -and -not $script:favoritesHealthy) {$searchScope.Text='Favorites unavailable; reload after repairing the file'}
    $script:filtering=$true
    $list.BeginUpdate()
    try {
        $list.Items.Clear()
        $list.AgeColors.Clear(); $list.SectionRows.Clear(); $list.ChildRows.Clear()
        foreach ($entry in $data.agents) {
            $haystack=$entry.name+' '+$entry.short_description+' '+$entry.purpose+' '+$entry.group
            $categoryMatch=($query -ne '' -or $category -eq '' -or $category -eq $entry.group)
            if ($category -eq '__favorites__' -and -not $query) {$categoryMatch=(@($script:favorites | Where-Object {$_.name -eq $entry.name}).Count -gt 0)}
            if ($entry.parent -and -not $query -and $category -notin @('__favorites__','__due__') -and -not $script:expandedParents.ContainsKey($entry.parent)) {continue}
            if ($category -eq '__due__') {$categoryMatch=(-not $entry.due_work -or $entry.due_work.state -ne 'available' -or $entry.due_work.today -gt 0 -or $entry.due_work.overdue -gt 0 -or $entry.due_work.unknown -gt 0 -or @($entry.due_work.other_rows | Where-Object {$_.timing -ne 'future'}).Count -gt 0)}
            if ($categoryMatch -and $haystack.IndexOf($query,[StringComparison]::OrdinalIgnoreCase) -ge 0) {
                $display=$entry.name
                $dueLabel=Due-Label $entry
                if ($entry.error) {$display+=' (check setup)'}
                $launch=Launch-For $entry.name
                $stamp=$launch.time
                if ($ageSource.SelectedIndex -eq 1) {$stamp=$entry.saved_work.time}
                $age=Activity-Age $stamp
                if ($ageSource.SelectedIndex -eq 2) {
                    $age=@{label=$dueLabel;color=$muted}
                    if ($entry.due_work.today -gt 0) {$age.color=[Drawing.Color]::FromArgb(245,210,125)}
                    if ($entry.due_work.overdue -gt 0) {$age.color=[Drawing.Color]::FromArgb(255,166,102)}
                }
                $ageText=$age.label
                if ($ageSource.SelectedIndex -eq 0 -and -not $script:historyHealthy) {$ageText='History unavailable'}
                if ($ageSource.SelectedIndex -eq 1 -and $entry.saved_work.state -eq 'unavailable') {$ageText='History unavailable'}
                $description=$entry.short_description; if (-not $description) {$description=$entry.purpose}
                if ($ageSource.SelectedIndex -ne 2 -and $dueLabel -ne 'No docket work due') {$ageText+=' | '+$dueLabel}
                $display+="`n"+$description+"`n"+$ageText
                $index=$list.Items.Add([pscustomobject]@{Display=$display;Entry=$entry},$script:checked.ContainsKey($entry.name))
                $list.AgeColors[$index]=$age.color
                if ($entry.parent -and -not $query -and $category -notin @('__favorites__','__due__')) {[void]$list.ChildRows.Add($index)}
                $children=@($data.agents | Where-Object {$_.parent -eq $entry.name})
                if ($children.Count -gt 0 -and -not $query -and $category -notin @('__favorites__','__due__')) {
                    $verb='Show'; if ($script:expandedParents.ContainsKey($entry.name)) {$verb='Hide'}
                    $selectedChildren=@($children | Where-Object {$script:checked.ContainsKey($_.name)}).Count
                    $section=$verb+' consumer specialists ('+$children.Count+")`n"+$selectedChildren+' selected; click or press Enter'
                    $sectionIndex=$list.Items.Add([pscustomobject]@{Display=$section;Entry=$null;SectionParent=$entry.name},$false)
                    [void]$list.SectionRows.Add($sectionIndex)
                }
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
        $label=@{sol='Codex Sol';claude='Claude (model unrecorded)';astra='Codex Astra';opus='Claude Opus';fable='Claude Fable'}[$item.runtime]
        $lines.Add($item.name+'  |  '+$label)
        $entry=@($data.agents | Where-Object {$_.name -eq $item.name})[0]
        if ($entry.prome_touch.state -ne 'available') {$lines.Add('PROME touch evidence unavailable; current activity unknown.')}
        elseif (@($entry.prome_touch.dates).Count -gt 0) {$lines.Add('PROME has an unresolved touch recorded for this desk, dated '+($entry.prome_touch.dates -join ', ')+'. This does not establish whether it is still running.')}
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
    if ($script:busy -or $script:refreshProcess -or $items.Count -eq 0) {return}
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
    Poll-EvidenceRefresh
    Poll-Research
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
$ageSource.Add_SelectedIndexChanged({Filter-Agents})
$reloadActivity.Add_Click({Reload-Activity})
$refreshEvidence.Add_Click({Start-EvidenceRefresh})
$categories.Add_SelectedIndexChanged({Filter-Agents})
$list.Add_SelectedIndexChanged({Select-Agent})
$list.Add_SectionToggle({Toggle-Specialists})
$favoriteButton.Add_Click({Toggle-Favorite})
$reloadFavorites.Add_LinkClicked({Reload-Favorites; Filter-Agents})
$list.Add_ItemCheck({
    param($sender,$e)
    if ($script:filtering) {return}
    if (-not $list.Items[$e.Index].Entry) {$e.NewValue=[Windows.Forms.CheckState]::Unchecked; return}
    $key=$list.Items[$e.Index].Entry.name
    if ($e.NewValue -eq [Windows.Forms.CheckState]::Checked) {$script:checked[$key]=$true} else {$script:checked.Remove($key)}
    $script:editAll=$true; Sync-Editors
})
$runtime.Add_SelectedIndexChanged({Save-Settings 'runtime'})
$instructionRuntime.Add_SelectedIndexChanged({
    if (-not $script:loading -and $instructionRuntime.SelectedIndex -ge 0) {$runtime.SelectedIndex=$instructionRuntime.SelectedIndex}
})
$instructionAgent.Add_SelectionChangeCommitted({Focus-Agent ([string]$instructionAgent.SelectedItem)})
$task.Add_TextChanged({Save-Settings 'task'})
foreach ($control in @($editAllAgents,$editAllInstructions)) {
    $control.Add_CheckedChanged({param($sender,$e)
        if (-not $script:loading -and -not $script:busy) {$script:editAll=$sender.Checked; Sync-Editors}
    })
}
$editInstructions.Add_Click({$tabs.SelectedTab=$pages.Instructions})
$selectedLink.Add_LinkClicked({$tabs.SelectedTab=$pages.Selected})
$historyList.Add_SelectedIndexChanged({Select-History})
$historyOpen.Add_Click({if ($historyList.SelectedItem) {Focus-Agent $historyList.SelectedItem.Record.name 'Agents'}})
$clear.Add_Click({$script:checked.Clear();$script:editAll=$true;Filter-Agents})
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
$form.Add_FormClosed({$timer.Stop();$timer.Dispose();Stop-ResearchWorker})
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
Reload-Favorites
if (@($script:favorites | Where-Object {$_.name -in @($data.agents.name)}).Count -gt 0) {Select-Category '__favorites__'} else {Select-Category ''}
try {Read-Groups; Refresh-Groups} catch {
    $script:groupsHealthy=$false
    $status.Text='Cannot read saved groups. See results below.'
    Log-Result ($_.Exception.Message+' File: '+$script:groupsPath)
    Set-DetailsVisible $true
}
try {$saved=Read-LocalRecords $script:historyPath 'history'; $script:history=@($saved.records); $script:lastOpened=@($saved.lastOpened)} catch {
    $script:historyHealthy=$false
    $status.Text='Saved activity could not be read. The original file was kept.'
    Log-Result ($_.Exception.Message+' File: '+$script:historyPath)
}
Refresh-History
Filter-Agents
Update-Buttons
$timer.Start()
if ($SmokeTest) {
    function Test-Step($name) {[IO.File]::WriteAllText((Join-Path $data.directory 'test-stage.txt'),$name)}
    $form.Add_Shown({
        try {
            Test-Step 'Browsing, specialists and favorites'
            $initialSettings=$script:settings | ConvertTo-Json -Depth 8 -Compress
            Select-Category ''; $search.Clear()
            if ($categories.Items[0].Name -ne '__favorites__') {throw 'Favorites is not at the top'}
            if (@($list.Items | Where-Object {$_.Entry.parent}).Count -ne 0 -or $list.SectionRows.Count -ne 1) {throw 'Specialists were not collapsed by default'}
            foreach ($entry in $data.agents) {
                $search.Text=$entry.name
                if (@($list.Items | Where-Object {$_.Entry.name -eq $entry.name}).Count -ne 1) {throw ('Search lost '+$entry.name)}
            }
            $search.Text='Student loans'
            if ($list.Items.Count -ne 1 -or $list.Items[0].Entry.name -ne 'STUE' -or $list.Items[0].Display -notmatch 'Student loans') {throw 'Short descriptions are not displayed/searchable'}
            $search.Clear(); Select-Category 'Consumers & housing'
            $section=@($list.SectionRows)[0]; $list.SelectedIndex=$section
            $list.SetItemChecked($section,$true)
            if ($start.Enabled -or $resume.Enabled -or $list.GetItemChecked($section) -or $script:checked.Count -ne 0) {throw 'Section header can launch or enter selection'}
            $keys=New-Object Windows.Forms.KeyEventArgs([Windows.Forms.Keys]::Enter)
            $keyMethod=[LauncherAgentList].GetMethod('OnKeyDown',([Reflection.BindingFlags]::Instance -bor [Reflection.BindingFlags]::NonPublic))
            [void]$keyMethod.Invoke($list,@($keys.PSObject.BaseObject))
            if (-not $keys.Handled -or @($list.Items | Where-Object {$_.Entry.parent -eq 'CARL'}).Count -ne 6) {throw 'Keyboard did not expand specialists'}
            $section=@($list.SectionRows)[0]; $rect=$list.GetItemRectangle($section)
            $mouse=New-Object Windows.Forms.MouseEventArgs([Windows.Forms.MouseButtons]::Left,1,($rect.Left+10),($rect.Top+10),0)
            $mouseMethod=[LauncherAgentList].GetMethod('OnMouseDown',([Reflection.BindingFlags]::Instance -bor [Reflection.BindingFlags]::NonPublic))
            [void]$mouseMethod.Invoke($list,@($mouse.PSObject.BaseObject))
            if (@($list.Items | Where-Object {$_.Entry.parent}).Count -ne 0 -or $script:checked.Count -ne 0) {throw 'Mouse collapse checked a section or kept children visible'}
            Focus-Agent 'STUE' 'Agents'
            $list.SetItemChecked($list.SelectedIndex,$true); $task.Text='Preserve this specialist task'
            Select-Category 'Consumers & housing'; $search.Clear()
            $list.SelectedIndex=@($list.SectionRows)[0]; $list.ToggleSection()
            if (@($list.Items | Where-Object {$_.Entry.parent}).Count -ne 0 -or $script:checked.Count -ne 1 -or @(Selected-Requests)[0].name -ne 'STUE' -or $script:settings['STUE'].task -cne 'Preserve this specialist task') {throw 'Collapse lost hidden selection/task'}
            if (@($list.Items | Where-Object {$_.SectionParent}).Display -notmatch '1 selected') {throw 'Collapsed section hides selected count'}
            Focus-Agent 'STUE' 'Agents'
            if ($script:selected.name -ne 'STUE' -or -not $script:expandedParents.ContainsKey('CARL')) {throw 'Selected specialist cannot be reopened'}
            $prepared=$script:settings | ConvertTo-Json -Depth 8 -Compress
            $favoriteButton.PerformClick()
            Focus-Agent 'GIBBS' 'Agents'; $favoriteButton.PerformClick()
            if (($script:settings | ConvertTo-Json -Depth 8 -Compress) -cne $prepared -or $script:checked.Count -ne 1) {throw 'Pinning changed launch preparation'}
            $script:favorites=@(); Reload-Favorites
            Select-Category '__favorites__'
            if ($list.Items.Count -ne 2 -or @($list.Items | Where-Object {$_.Entry.name -eq 'STUE'}).Count -ne 1 -or $list.SectionRows.Count -ne 0) {throw 'Saved favorites did not restore or hid a specialist'}
            $favoriteText=[IO.File]::ReadAllText($script:favoritesPath)
            # Stale writers must refuse before altering another window's choices.
            [IO.File]::WriteAllText($script:favoritesPath,$favoriteText+"`r`n")
            $favoriteButton.PerformClick()
            if ($status.Text -notmatch 'changed in another window' -or [IO.File]::ReadAllText($script:favoritesPath) -cne ($favoriteText+"`r`n")) {throw 'Favorite write overwrote another window'}
            Reload-Favorites
            $favoriteButton.PerformClick()
            if ($list.Items.Count -ne 1 -or $script:checked.Count -ne 1) {throw 'Removing a favorite changed selection or left it visible'}
            foreach ($bad in @('{broken','{"version":1,"favorites":[{"name":"GIBBS"},{"name":"GIBBS"}]}')) {
                [IO.File]::WriteAllText($script:favoritesPath,$bad); Reload-Favorites
                if ($script:favoritesHealthy) {throw 'Invalid favorites accepted'}
                Toggle-Favorite
                if ([IO.File]::ReadAllText($script:favoritesPath) -cne $bad) {throw 'Invalid favorites file overwritten'}
            }
            [IO.File]::WriteAllText($script:favoritesPath,$favoriteText); Reload-Favorites
            $saved=Write-LocalRecords $script:favoritesPath 'favorites' @(@{name='GIBBS'},@{name='REMOVED_DESK'}) $script:favoritesVersion
            Reload-Favorites; Filter-Agents
            if ($list.Items.Count -ne 1 -or $list.Items[0].Entry.name -ne 'GIBBS') {throw 'Unavailable favorite became launchable'}
            $favoriteButton.PerformClick()
            if ($script:favorites.Count -ne 1 -or $script:favorites[0].name -ne 'REMOVED_DESK' -or $list.Items.Count -ne 0 -or $start.Enabled) {throw 'Removing a favorite discarded unknown names or enabled empty launch'}
            $search.Text='STUE'
            if ($list.Items.Count -ne 1 -or $list.Items[0].Entry.name -ne 'STUE') {throw 'Favorites search did not search globally'}
            $search.Clear()
            if ($list.Items.Count -ne 0 -or $name.Text -ne 'Your favorites') {throw 'Empty favorites has no useful empty state'}
            $saved=Write-LocalRecords $script:favoritesPath 'favorites' @() $script:favoritesVersion
            Reload-Favorites
            $script:checked.Clear(); $script:expandedParents.Clear()
            foreach ($entry in $data.agents) {$script:settings[$entry.name]=@{runtime=$entry.default_runtime;task=$null}}
            Select-Category ''; Filter-Agents
            if (($script:settings | ConvertTo-Json -Depth 8 -Compress) -cne $initialSettings) {throw 'Browsing changed default settings'}
            Test-Step 'Opus startup defaults'
            foreach ($entry in $data.agents) {
                $expected='opus'; if ($entry.kind -eq 'cato') {$expected='astra'}
                if ($script:settings[$entry.name].runtime -ne $expected) {throw ('Incorrect startup model for '+$entry.name)}
            }
            Focus-Agent 'PROME' 'Agents'
            if ($runtime.Text -ne 'Claude Opus') {throw 'Startup dropdown did not select Opus'}
            # Distinct fixture values keep the bulk-edit isolation check meaningful.
            $script:settings['PROME'].runtime='fable'
            foreach ($key in @('CARL','MIDAS','HENRY','LIQUID')) {$script:settings[$key].runtime='sol'}
            Test-Step 'Default bulk edits and individual overrides'
            foreach ($key in @('CARL','MIDAS','HENRY','LIQUID')) {
                $search.Text=$key
                for ($i=0;$i -lt $list.Items.Count;$i++) {
                    if ($list.Items[$i].Entry.name -eq $key) {$list.SetItemChecked($i,$true)}
                }
            }
            if (-not (Editing-All) -or $script:checked.Count -ne 4) {throw 'Multiple selection did not default to bulk editing'}
            # A highlighted unselected agent must not receive a bulk change.
            $search.Text='PROME'; $runtime.SelectedItem='Claude Opus'
            foreach ($key in $script:checked.Keys) {if ($script:settings[$key].runtime -ne 'opus') {throw 'Bulk model missed a hidden selection'}}
            if ($script:settings['PROME'].runtime -ne 'fable') {throw 'Bulk model changed an unchecked agent'}
            $task.Text='Shared instructions'
            foreach ($key in $script:checked.Keys) {if ($script:settings[$key].task -cne 'Shared instructions') {throw 'Bulk instructions missed a selection'}}
            $tabs.SelectedTab=$pages.Selected
            $card=@($chips.Controls | Where-Object {$_.Tag -eq 'CARL'})[0]
            $card.Controls[0].PerformClick()
            if ((Editing-All) -or $editAllInstructions.Checked -or $script:checked.Count -ne 4) {throw 'Individual navigation did not preserve selection and change scope'}
            $task.Text='Only CARL override'; $instructionRuntime.SelectedItem='Codex Astra'
            foreach ($key in @('MIDAS','HENRY','LIQUID')) {
                if ($script:settings[$key].task -cne 'Shared instructions' -or $script:settings[$key].runtime -ne 'opus') {throw 'Individual edit leaked to the group'}
            }
            $editAllInstructions.Checked=$true
            if (-not $editAllAgents.Checked -or $runtime.SelectedIndex -ne -1 -or $task.Text -ne '' -or $taskLabel.Text -notmatch 'Different instructions') {throw 'Mixed settings were not disclosed'}
            $task.Text='Shared replacement with mixed models'
            if ($script:settings['CARL'].runtime -ne 'astra' -or $script:settings['MIDAS'].runtime -ne 'opus') {throw 'Instruction edit erased mixed models'}
            Focus-Agent 'CARL'; $task.Text='Only CARL override'; $editAllInstructions.Checked=$true
            $instructionRuntime.SelectedItem='Claude Fable'
            if ($script:settings['CARL'].task -cne 'Only CARL override') {throw 'Bulk model erased individual instructions'}
            $search.Text='no-such-agent-987654'
            if (-not $task.Enabled -or -not $runtime.Enabled -or $start.Enabled) {throw 'Hidden selection editing or single-launch gating failed'}
            $task.Text='Replacement for all'
            foreach ($key in $script:checked.Keys) {
                if ($script:settings[$key].task -cne 'Replacement for all' -or $script:settings[$key].runtime -ne 'fable') {throw 'Bulk instructions changed models or missed hidden agents'}
            }
            $tabs.SelectedTab=$pages.Instructions; $task.Clear(); $preset.SelectedIndex=0; $usePreset.PerformClick()
            foreach ($key in $script:checked.Keys) {if ($script:settings[$key].task -cne $presets[0].text) {throw 'Default Apply preset missed selected agents'}}
            Focus-Agent 'CARL'; $search.Text='CATO'; $list.SetItemChecked(0,$true)
            if (-not (Editing-All) -or $runtime.Items.Contains('Claude Opus') -or $runtime.Items.Count -ne 2) {throw 'CATO batch model restriction failed'}
            $runtime.SelectedItem='Codex Sol'
            foreach ($key in $script:checked.Keys) {if ($script:settings[$key].runtime -ne 'sol') {throw 'Compatible bulk model missed a selection'}}
            if (@(Selected-Requests).Count -ne 5) {throw 'Bulk edits lost preview membership'}
            $clear.PerformClick()
            foreach ($entry in $data.agents) {$script:settings[$entry.name]=@{runtime=$entry.default_runtime;task=$null}}
            Filter-Agents
            Test-Step 'Initial selection and policy'
            $search.Text='CATO'
            if ($runtime.Text -ne 'Codex Astra' -or -not $runtime.Enabled -or $runtime.Items.Count -ne 2) {throw 'CATO policy UI failed'}
            $list.SetItemChecked(0,$true)
            $search.Text='CARL'; $runtime.SelectedIndex=1; $task.Text='Only CARL receives this task'
            if ($resume.Enabled) {throw 'Resume must refuse task text'}
            $list.SetItemChecked(0,$true)
            $editAllAgents.Checked=$false
            $categories.SelectedIndex=2; $search.Clear()
            if ($list.Items.Count -eq 0) {throw 'Category is empty'}
            foreach ($item in $list.Items) {
                if ($item.Entry.group -ne $categories.SelectedItem.Name) {throw 'Category contains another group'}
            }
            if ($script:checked.Count -ne 2) {throw 'Filtering lost checked agents'}
            $items=@(Selected-Requests)
            if ($items.Count -ne 2 -or (Preview-Text $items) -notmatch 'Codex Astra') {throw 'Preview lost a hidden selection'}
            $carl=@($items | Where-Object {$_.name -eq 'CARL'})[0]
            if ($carl.runtime -ne 'opus' -or $carl.task -ne 'Only CARL receives this task') {throw 'Per-agent settings were lost'}
            Select-Category ''; $search.Text='CARL'
            if ($runtime.Text -ne 'Claude Opus' -or $task.Text -ne $carl.task) {throw 'Settings did not restore'}
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
            if ($script:checked.Count -ne 3 -or $script:settings['CARL'].runtime -ne 'opus') {throw 'Saved group failed to reload'}
            $failed=$false
            try {Apply-Group @{name='Invalid';members=@(@{name='CARL';runtime='sol'},@{name='MISSING_TEST';runtime='sol'})}} catch {$failed=$true}
            if (-not $failed -or $script:checked.Count -ne 3 -or $script:settings['CARL'].runtime -ne 'opus') {throw 'Stale group partially changed settings'}
            $failed=$false
            try {Apply-Group @{name='Invalid';members=@(@{name='CATO';runtime='fable'})}} catch {$failed=$true}
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
            $editAllAgents.Checked=$false
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
            if ($runtime.Text -ne 'Claude Opus' -or $script:settings[$agentName].runtime -ne 'opus') {throw 'Instructions runtime did not synchronize'}
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
            Reload-Activity
            $tabs.SelectedTab=$pages.Activity
            $beforeCount=$script:checked.Count; $beforeTask=$script:settings['CARL'].task
            $historyOpen.PerformClick()
            if ($tabs.SelectedTab -ne $pages.Agents -or $script:selected.name -ne 'CARL' -or $script:checked.Count -ne $beforeCount -or $script:settings['CARL'].task -cne $beforeTask) {throw 'History navigation changed preparation state'}
            Test-Step 'Model choices and activity ages'
            Focus-Agent 'PROME' 'Agents'
            if ($runtime.Text -ne 'Claude Opus') {throw 'PROME default is not Opus'}
            foreach ($choice in @('Claude Opus','Claude Fable','Codex Astra','Codex Sol')) {
                $runtime.SelectedItem=$choice
                if ($instructionRuntime.Text -ne $choice) {throw 'Model controls did not synchronize'}
            }
            Focus-Agent 'CATO' 'Instructions'; $instructionRuntime.SelectedItem='Codex Sol'
            if ($runtime.Text -ne 'Codex Sol' -or $script:settings['CATO'].runtime -ne 'sol') {throw 'CATO Sol choice failed'}
            $legacyGroup=@{name='Legacy';members=@(@{name='PROME';runtime='claude'},@{name='CARL';runtime='claude'})}
            Apply-Group $legacyGroup
            if ($script:settings['PROME'].runtime -ne 'fable' -or $script:settings['CARL'].runtime -ne 'opus') {throw 'Legacy Claude group defaults failed'}
            $now=[DateTimeOffset]::Parse('2026-10-29T12:00:00Z')
            foreach ($days in @(0,6,7,13,14,30)) {
                $age=Activity-Age ($now.AddDays(-$days).ToString('o')) $now
                $expected=$ink
                if ($days -ge 14) {$expected=[Drawing.Color]::FromArgb(255,166,102)}
                elseif ($days -ge 7) {$expected=[Drawing.Color]::FromArgb(245,210,125)}
                if ($age.days -ne $days -or $age.color.ToArgb() -ne $expected.ToArgb()) {throw 'Age threshold failed'}
            }
            foreach ($stamp in @('', 'bad', $now.AddDays(1).ToString('o'))) {
                $age=Activity-Age $stamp $now
                if ($null -ne $age.days -or $age.color.ToArgb() -ne $muted.ToArgb()) {throw 'Unknown/future age was graded stale'}
            }
            $old=@{time=[DateTimeOffset]::Now.AddDays(-15).ToString('o');name='PROME';runtime='claude';action='new';task='';outcome='Opened';message='Old confirmed launch'}
            [void](Write-LocalRecords $script:historyPath 'history' @($old) '' $true)
            $saved=Write-LocalRecords $script:historyPath 'history' $many '' $true
            Reload-Activity
            if ($saved.records.Count -ne 100 -or (Launch-For 'PROME').message -ne 'Old confirmed launch') {throw 'Rolling history evicted latest launch summary'}
            $unconfirmed=@{time=[DateTimeOffset]::Now.ToString('o');name='PROME';runtime='fable';action='new';task='';outcome='Not confirmed';message='No acknowledgement'}
            [void](Write-LocalRecords $script:historyPath 'history' @($unconfirmed) '' $true); Reload-Activity
            Focus-Agent 'PROME' 'Agents'
            if ((Launch-For 'PROME').time -ne $old.time -or $recentDetails.Text -notmatch 'model unrecorded') {throw 'Failed launch or legacy model misrepresented'}
            $beforeTask=$script:settings['PROME'].task; $beforeCount=$script:checked.Count
            $ageSource.SelectedIndex=1; $ageSource.SelectedIndex=0
            if ($script:selected.name -ne 'PROME' -or $script:checked.Count -ne $beforeCount -or $script:settings['PROME'].task -cne $beforeTask -or $list.GetItemRectangle(0).Height -lt 40 -or $list.Items[0].Display -notmatch '15d ago') {throw 'Activity source switch lost state or age row height'}
            $historyBefore=[IO.File]::ReadAllText($script:historyPath)
            $bad=@{version=1;history=@();last_opened=@($unconfirmed)} | ConvertTo-Json -Depth 6
            [IO.File]::WriteAllText($script:historyPath,$bad); Reload-Activity
            if ($script:historyHealthy -or $null -ne (Launch-For 'PROME')) {throw 'Invalid summary retained a freshness claim'}
            [IO.File]::WriteAllText($script:historyPath,$historyBefore); Reload-Activity
            Test-Step 'Due work, evidence refresh, and catch-up'
            $originalRows=$data.agents | ConvertTo-Json -Depth 15 | ConvertFrom-Json
            $oldStamp=$data.captured_at
            $freshRows=$data.agents | ConvertTo-Json -Depth 15 | ConvertFrom-Json
            foreach ($entry in $freshRows) {
                $due=[pscustomobject]@{state='available';as_of='2026-10-29';today=0;overdue=0;unknown=0;rows=@();other_rows=@()}
                if ($entry.name -eq 'CARL') {
                    $due.today=1; $due.overdue=1
                    $due.rows=@([pscustomobject]@{key='D:L1';date='2026-10-28';owner='CARL / PROME';description='Fixture overdue work';state='PENDING';covered=$true;coverage='consumer read';notes='Preserve this note'})
                }
                $entry | Add-Member -NotePropertyName due_work -NotePropertyValue $due -Force
                $entry | Add-Member -NotePropertyName prome_touch -NotePropertyValue ([pscustomobject]@{state='available';dates=@('2026-10-28')}) -Force
            }
            Focus-Agent 'CARL'; $search.Text='CARL'; $task.Text='Retain my prepared work'; $runtime.SelectedItem='Claude Opus'
            $beforeSettings=$script:settings | ConvertTo-Json -Depth 8 -Compress
            $beforeMembers=@($script:checked.Keys | Sort-Object) -join '|'
            $beforeCategory=$categories.SelectedIndex
            Apply-EvidenceSnapshot ([pscustomobject]@{ok=$true;agents=$freshRows;captured_at='2026-10-29T16:00:00Z'})
            if (($script:settings | ConvertTo-Json -Depth 8 -Compress) -cne $beforeSettings -or (@($script:checked.Keys | Sort-Object) -join '|') -cne $beforeMembers -or $search.Text -ne 'CARL' -or $categories.SelectedIndex -ne $beforeCategory) {throw 'Refresh changed prepared settings or filters'}
            if ($recentDetails.Text -notmatch 'COVERED: consumer read' -or $recentDetails.Text -notmatch 'Preserve this note' -or $list.Items[0].Display -notmatch 'OVERDUE 1 / DUE 1') {throw 'Due badge or coverage details missing'}
            $previewText=Preview-Text @(Request-For $script:selected 'new')
            if ($previewText -notmatch 'unresolved touch.*2026-10-28' -or $previewText -notmatch 'does not establish') {throw 'Earlier-date touch advisory missing'}
            $ageSource.SelectedIndex=1
            if ($ageLegend.Text -notmatch 'since last saved work') {throw 'Saved-work age label missing'}
            $ageSource.SelectedIndex=0
            if ($ageLegend.Text -notmatch 'since last launch here') {throw 'Launch age label missing'}
            $ageSource.SelectedIndex=2
            $search.Clear(); $categories.SelectedIndex=$categories.Items.Count-1
            if ($list.Items.Count -ne 1 -or $list.Items[0].Entry.name -ne 'CARL') {throw 'Due category included future/empty desks'}
            $tabs.SelectedTab=$pages.Instructions; $task.Clear(); $preset.SelectedItem='CATCH-UP'; $usePreset.PerformClick()
            if ($task.Text -notmatch 'Close out' -or $task.Text -notmatch 'already authorized' -or $task.Text -notmatch 'PROME/COMPLETION_SPEC.md') {throw 'CATCH-UP lost scope or delivery instruction'}
            $beforeStamp=$data.captured_at
            $failed=$false
            try {Apply-EvidenceSnapshot ([pscustomobject]@{ok=$true;agents=@();captured_at='2026-10-29T17:00:00Z'})} catch {$failed=$true}
            if (-not $failed -or $data.captured_at -ne $beforeStamp) {throw 'Incomplete refresh replaced good evidence'}
            $data.agents=$originalRows; $data.captured_at=$oldStamp
            $ageSource.SelectedIndex=0; Select-Category ''; Filter-Agents
            Test-Step 'ORACLE daily read preset'
            Focus-Agent 'ORACLE'; $task.Text='Keep the prepared ORACLE task'
            $oracleRuntime=$script:settings['ORACLE'].runtime
            $carlBefore=$script:settings['CARL'] | ConvertTo-Json -Compress
            $oracleMembers=@($script:checked.Keys | Sort-Object) -join '|'
            $oracleHistory=[IO.File]::ReadAllText($script:historyPath)
            $preset.SelectedItem='ORACLE daily read'
            if ($task.Text -ne 'Keep the prepared ORACLE task') {throw 'Choosing ORACLE preset changed instructions before Apply'}
            $oracleConfirm=$script:confirmChange
            $script:confirmChange={param($message,$title) return $false}
            $usePreset.PerformClick()
            if ($task.Text -ne 'Keep the prepared ORACLE task') {throw 'Cancelled ORACLE preset replaced instructions'}
            $script:confirmChange={param($message,$title) return $true}
            $usePreset.PerformClick()
            $script:confirmChange=$oracleConfirm
            $expectedOracle='ORACLE daily read: boot, run `python3 tools/routine_check.py` and report any NOT READ day, take today''s business-day read (Polymarket and Kalshi `pull --log`, spread tool) unless the scheduled routine already logged one, grade the logged rows on `workbook/V5_NOV110_READS.tsv` against VX-ORC-04 and VX-ORC-12, packet PROME on any state change, then close out.'
            if ($task.Text -cne $expectedOracle -or $script:settings['ORACLE'].task -cne $expectedOracle) {throw 'ORACLE preset lost supplied wording'}
            $oracleRequest=Request-For $script:selected 'new'
            if ($oracleRequest.name -ne 'ORACLE' -or $oracleRequest.task -cne $expectedOracle -or $oracleRequest.runtime -ne $oracleRuntime) {throw 'ORACLE preview task or runtime changed'}
            if (($script:settings['CARL'] | ConvertTo-Json -Compress) -cne $carlBefore -or (@($script:checked.Keys | Sort-Object) -join '|') -cne $oracleMembers) {throw 'Individual ORACLE preset changed another agent or membership'}
            if ($script:busy -or $script:process -or $script:queue.Count -ne 0 -or [IO.File]::ReadAllText($script:historyPath) -cne $oracleHistory) {throw 'ORACLE preset started work or recorded a launch'}
            $task.AppendText(' Editable follow-up.')
            if ($script:settings['ORACLE'].task -cne ($expectedOracle+' Editable follow-up.')) {throw 'ORACLE preset is not editable'}
            Test-ResearchReader
            Test-DecisionsLauncher
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
            $script:checked.Clear(); $script:expandedParents.Clear()
            foreach ($entry in $data.agents) {$script:settings[$entry.name]=@{runtime=$entry.default_runtime;task=$null}}
            $script:favorites=@(@{name='PROME'},@{name='GIBBS'},@{name='ISHM'},@{name='STUE'})
            Select-Category '__favorites__'; $search.Clear(); Filter-Agents; $tabs.SelectedTab=$pages.Agents; $form.Refresh()
            $bitmap=New-Object Drawing.Bitmap($form.Width,$form.Height)
            $form.DrawToBitmap($bitmap,(New-Object Drawing.Rectangle(0,0,$form.Width,$form.Height)))
            $bitmap.Save((Join-Path $data.directory 'favorites.png')); $bitmap.Dispose()
            Focus-Agent 'CARL' 'Agents'; Select-Category 'Consumers & housing'; $search.Clear(); Filter-Agents 'CARL'; $form.Refresh()
            $bitmap=New-Object Drawing.Bitmap($form.Width,$form.Height)
            $form.DrawToBitmap($bitmap,(New-Object Drawing.Rectangle(0,0,$form.Width,$form.Height)))
            $bitmap.Save((Join-Path $data.directory 'specialists-collapsed.png')); $bitmap.Dispose()
            $script:expandedParents['CARL']=$true; Filter-Agents 'CARL'
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
            @{ok=$true;checks='Favorites persistence/removal/stale-window/corrupt/unknown-name handling, all-agent search, short descriptions, specialist expand/collapse/header safety/hidden selection, Explicit Opus/Fable/Astra/Sol selection and legacy group migration, age thresholds/unknown/future timestamps, retained last launch beyond 100 attempts, failed-launch exclusion, invalid summary refusal, Categories, retained selection, per-agent runtime/task, hidden preview, CATO, resume, empty search, clear, stop remaining, saved groups, atomic persistence, concurrent/corrupt-file refusal, Research real worker/search/source/limits/stale responses/queue independence, task presets including exact ORACLE daily-read text/edit/cancel/no-launch, group rename/collision, global search/category restore, selected-name navigation and separate removal, tab state/busy queue preservation, custom preset persistence/corruption/concurrency/confirmation, bounded history merging/corruption, Activity errors, page bounds and resize'} | ConvertTo-Json | Set-Content -Encoding UTF8 (Join-Path $data.directory 'smoke.json')
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

# Research tab. Separate read-only WSL worker, never the launcher dispatch queue.
$script:researchWorker=$null; $script:researchRead=$null
$script:researchPending=$null; $script:researchCurrent=$null; $script:researchGeneration=0
$script:researchLoaded=$false; $script:researchUpdating=$false
$script:researchPath=''; $script:researchVersion=''; $script:researchLastStat=[DateTime]::UtcNow
$script:researchDocumentQuery=''; $script:researchScanStamp=''
$readerLayout=New-Object Windows.Forms.TableLayoutPanel
$readerLayout.Dock='Fill'; $readerLayout.ColumnCount=1; $readerLayout.RowCount=4
foreach ($height in @(46,44)) {[void]$readerLayout.RowStyles.Add((New-Object Windows.Forms.RowStyle('Absolute',$height)))}
[void]$readerLayout.RowStyles.Add((New-Object Windows.Forms.RowStyle('Percent',100)))
[void]$readerLayout.RowStyles.Add((New-Object Windows.Forms.RowStyle('Absolute',58)))
$readerLayout.Padding=New-Object Windows.Forms.Padding(8)
$pages.Research.Controls.Add($readerLayout)
function Research-Button($text,$width) {
    $b=New-Object LauncherButton; $b.Text=$text; $b.Width=$width; $b.Height=32
    Style-Button $b; return $b
}
function Research-Label($text) {
    $l=New-Object Windows.Forms.Label; $l.Text=$text; $l.AutoSize=$true
    $l.Margin=New-Object Windows.Forms.Padding(4,9,4,0); $l.ForeColor=$ink; return $l
}
$readerFilters=New-Object Windows.Forms.FlowLayoutPanel
$readerFilters.Dock='Fill'; $readerFilters.WrapContents=$false
$readerDesk=New-Object Windows.Forms.ComboBox
$readerDesk.DropDownStyle='DropDownList'; $readerDesk.Width=130
[void]$readerDesk.Items.Add('All three')
foreach ($deskName in @('CARL','BROCK','LIQUID')) {[void]$readerDesk.Items.Add($deskName)}
$readerDesk.SelectedIndex=0; Style-Input $readerDesk
$readerType=New-Object Windows.Forms.ComboBox
$readerType.DropDownStyle='DropDownList'; $readerType.Width=150
foreach ($typeName in @('All documents','Overview','Research','Reports','Audits')) {[void]$readerType.Items.Add($typeName)}
$readerType.SelectedIndex=0; Style-Input $readerType
$readerRefresh=Research-Button 'Refresh files' 122
$readerCancel=Research-Button 'Cancel read' 112; $readerCancel.Enabled=$false
$readerFilters.Controls.AddRange(@((Research-Label 'Desk'),$readerDesk,(Research-Label 'Type'),$readerType,$readerRefresh,$readerCancel,(Research-Label 'Markdown reports and overviews')))
$readerLayout.Controls.Add($readerFilters,0,0)
$readerSearchBar=New-Object Windows.Forms.TableLayoutPanel
$readerSearchBar.Dock='Fill'; $readerSearchBar.ColumnCount=4; $readerSearchBar.RowCount=1
[void]$readerSearchBar.ColumnStyles.Add((New-Object Windows.Forms.ColumnStyle('Absolute',145)))
[void]$readerSearchBar.ColumnStyles.Add((New-Object Windows.Forms.ColumnStyle('Percent',100)))
foreach ($w in @(100,90)) {[void]$readerSearchBar.ColumnStyles.Add((New-Object Windows.Forms.ColumnStyle('Absolute',$w)))}
$readerQuery=New-Object Windows.Forms.TextBox; $readerQuery.Dock='Fill'; $readerQuery.MaxLength=1000; Style-Input $readerQuery
$readerSearch=Research-Button 'Search' 94; $readerClear=Research-Button 'Clear' 84
$readerSearchBar.Controls.Add((Research-Label 'Search documents'),0,0)
$readerSearchBar.Controls.Add($readerQuery,1,0);$readerSearchBar.Controls.Add($readerSearch,2,0);$readerSearchBar.Controls.Add($readerClear,3,0)
$readerLayout.Controls.Add($readerSearchBar,0,1)
$readerSplit=New-Object Windows.Forms.SplitContainer
$readerSplit.Dock='Fill'; $readerSplit.Orientation='Vertical'; $readerSplit.Size=New-Object Drawing.Size(1000,400)
$readerSplit.Panel1MinSize=240; $readerSplit.Panel2MinSize=380; $readerSplit.SplitterDistance=310
$readerLayout.Controls.Add($readerSplit,0,2)
$readerList=New-Object Windows.Forms.ListView
$readerList.Dock='Fill';$readerList.View='Details';$readerList.FullRowSelect=$true;$readerList.MultiSelect=$false
$readerList.HideSelection=$false;$readerList.ShowItemToolTips=$true
[void]$readerList.Columns.Add('Document',245);[void]$readerList.Columns.Add('Path date',95)
Style-Input $readerList;$readerSplit.Panel1.Controls.Add($readerList)
$readerRight=New-Object Windows.Forms.TableLayoutPanel
$readerRight.Dock='Fill';$readerRight.ColumnCount=1;$readerRight.RowCount=4
foreach ($h in @(70,40,38)) {[void]$readerRight.RowStyles.Add((New-Object Windows.Forms.RowStyle('Absolute',$h)))}
[void]$readerRight.RowStyles.Add((New-Object Windows.Forms.RowStyle('Percent',100)))
$readerSplit.Panel2.Controls.Add($readerRight)
$readerIdentity=New-Object Windows.Forms.TextBox
$readerIdentity.Multiline=$true;$readerIdentity.ReadOnly=$true;$readerIdentity.ScrollBars='Vertical';$readerIdentity.Dock='Fill'
$readerIdentity.Text='Choose a document. Original Markdown source is shown in full.';Style-Input $readerIdentity
$readerRight.Controls.Add($readerIdentity,0,0)
$readerTools=New-Object Windows.Forms.FlowLayoutPanel
$readerTools.Dock='Fill';$readerTools.WrapContents=$false
$readerReload=Research-Button 'Reload' 76;$readerCopy=Research-Button 'Copy path' 94
$readerZoomOut=Research-Button '-' 36;$readerZoomIn=Research-Button '+' 36
$readerWrap=New-Object Windows.Forms.CheckBox;$readerWrap.Text='Wrap lines';$readerWrap.Checked=$true;$readerWrap.AutoSize=$true;$readerWrap.Margin=New-Object Windows.Forms.Padding(6,8,0,0);$readerWrap.ForeColor=$ink
$readerTools.Controls.AddRange(@($readerReload,$readerCopy,$readerZoomOut,$readerZoomIn,$readerWrap))
$readerRight.Controls.Add($readerTools,0,1)
$readerFindBar=New-Object Windows.Forms.TableLayoutPanel
$readerFindBar.Dock='Fill';$readerFindBar.ColumnCount=3
[void]$readerFindBar.ColumnStyles.Add((New-Object Windows.Forms.ColumnStyle('Percent',100)))
foreach ($w in @(64,64)) {[void]$readerFindBar.ColumnStyles.Add((New-Object Windows.Forms.ColumnStyle('Absolute',$w)))}
$readerFind=New-Object Windows.Forms.TextBox;$readerFind.Dock='Fill';Style-Input $readerFind
$tooltip.SetToolTip($readerFind,'Find literal text in the displayed document (Ctrl+F).')
$readerPrevious=Research-Button 'Prev' 58;$readerNext=Research-Button 'Next' 58
$readerFindBar.Controls.Add($readerFind,0,0);$readerFindBar.Controls.Add($readerPrevious,1,0);$readerFindBar.Controls.Add($readerNext,2,0)
$readerRight.Controls.Add($readerFindBar,0,2)
$readerText=New-Object Windows.Forms.RichTextBox
$readerText.Dock='Fill';$readerText.ReadOnly=$true;$readerText.DetectUrls=$true;$readerText.WordWrap=$true
$readerText.Font=New-Object Drawing.Font('Consolas',11);$readerText.BackColor=$surface;$readerText.ForeColor=$ink
$readerText.BorderStyle='None';$readerText.HideSelection=$false;$readerText.ScrollBars='Both'
$readerRight.Controls.Add($readerText,0,3)
$readerState=New-Object Windows.Forms.TextBox
$readerState.Dock='Fill';$readerState.Multiline=$true;$readerState.ReadOnly=$true;$readerState.ScrollBars='Vertical'
$readerState.Text='Local saved documents. Path dates are not evidence freshness. Enter Research to load.';Style-Input $readerState
$readerLayout.Controls.Add($readerState,0,3)

function Stop-ResearchWorker {
    if ($script:researchWorker) {
        try {$script:researchInput.Close()} catch {}
        # Closing stdin lets the bounded worker finish and exit. No desk process is killed.
        $script:researchWorker.Dispose();$script:researchWorker=$null
    }
    $script:researchRead=$null;$script:researchCurrent=$null;$script:researchPending=$null
    $readerCancel.Enabled=$false
}
function Start-ResearchWorker {
    if ($script:researchWorker -and -not $script:researchWorker.HasExited) {return}
    if ($script:researchWorker) {Stop-ResearchWorker}
    $bridgeFolder=[IO.Path]::GetDirectoryName([string]$data.bridge).Replace('\','/')
    $worker=$bridgeFolder+'/research_reader.py'
    $values=@('-d',$data.distro,'-u',$data.user,'--exec',$data.python,'-B',$worker,'--serve')
    $quoted=foreach ($v in $values) {
        $v=[string]$v
        if ($v -and $v -notmatch '[\s"]') {$v} else {
            $escaped=[regex]::Replace($v,'(\\*)"','$1$1\"')
            $escaped=[regex]::Replace($escaped,'(\\+)$','$1$1')
            '"'+$escaped+'"'
        }
    }
    $psi=New-Object Diagnostics.ProcessStartInfo
    $psi.FileName='wsl.exe';$psi.Arguments=$quoted -join ' ';$psi.UseShellExecute=$false;$psi.CreateNoWindow=$true
    $psi.RedirectStandardInput=$true;$psi.RedirectStandardOutput=$true;$psi.RedirectStandardError=$true
    $psi.StandardOutputEncoding=New-Object Text.UTF8Encoding($false)
    $script:researchWorker=[Diagnostics.Process]::Start($psi)
    $script:researchInput=New-Object IO.StreamWriter($script:researchWorker.StandardInput.BaseStream,(New-Object Text.UTF8Encoding($false)))
    $script:researchInput.AutoFlush=$true
    $script:researchError=$script:researchWorker.StandardError.ReadToEndAsync()
}
function Send-ResearchPending {
    if ($script:researchCurrent -or -not $script:researchPending) {return}
    Start-ResearchWorker
    $script:researchCurrent=$script:researchPending;$script:researchPending=$null
    $script:researchInput.WriteLine(($script:researchCurrent | ConvertTo-Json -Compress))
    $script:researchInput.Flush()
    $script:researchRead=$script:researchWorker.StandardOutput.ReadLineAsync()
    $script:researchStarted=[DateTime]::UtcNow
    $readerCancel.Enabled=$true
}
function Request-Research($operation,$path='') {
    try {
        $script:researchGeneration++
        $script:researchPending=@{id=$script:researchGeneration;op=$operation;path=$path;query=$readerQuery.Text;desk=$readerDesk.Text;category=$readerType.Text}
        if ($operation -ne 'stat') {$readerState.Text='Reading local files... '+$operation}
        Send-ResearchPending
    } catch {$readerState.Text='Reader unavailable: '+$_.Exception.Message;Stop-ResearchWorker}
}
function Find-ResearchText($backwards=$false,$fromStart=$false) {
    $query=$readerFind.Text
    if (-not $query) {return}
    $options=[Windows.Forms.RichTextBoxFinds]::None
    if ($backwards) {
        $end=[Math]::Max(0,$readerText.SelectionStart)
        $at=$readerText.Find($query,0,$end,[Windows.Forms.RichTextBoxFinds]::Reverse)
        if ($at -lt 0) {$at=$readerText.Find($query,[Windows.Forms.RichTextBoxFinds]::Reverse)}
    } else {
        $start=$readerText.SelectionStart+$readerText.SelectionLength
        if ($fromStart) {$start=0}
        $at=$readerText.Find($query,$start,$options)
        if ($at -lt 0) {$at=$readerText.Find($query,$options)}
    }
    if ($at -ge 0) {$readerText.ScrollToCaret()} else {$readerState.Text='No match in this displayed document.'}
}
function Apply-ResearchResult($response) {
    if ($response.id -ne $script:researchGeneration) {return}
    if (-not $response.ok) {
        if ($response.op -eq 'stat') {$readerIdentity.Text=$script:researchPath+"`r`nFile unavailable or changed. The previous view is retained; Reload to retry."}
        $readerState.Text='Reader: '+$response.message+' Previous complete view retained.';return
    }
    if ($response.op -in @('scan','search')) {
        $script:researchUpdating=$true;$readerList.BeginUpdate()
        try {
            $readerList.Items.Clear()
            foreach ($doc in $response.documents) {
                $item=New-Object Windows.Forms.ListViewItem(($doc.desk+' / '+$doc.title))
                [void]$item.SubItems.Add([string]$doc.path_date)
                $item.Tag=$doc;$item.ToolTipText=$doc.path+"`r`n"+$doc.match_kind+' '+$doc.snippet
                [void]$readerList.Items.Add($item)
                if ($doc.path -eq $script:researchPath) {$item.Selected=$true}
            }
        } finally {$readerList.EndUpdate();$script:researchUpdating=$false}
        $script:researchLoaded=$true;$script:researchScanStamp=$response.scanned_at
        $word='Search complete'
        if (-not $response.complete) {$word='Search incomplete'}
        $readerState.Text=$word+': '+@($response.documents).Count+' matches / '+$response.total+' documents. Snapshot '+$response.scanned_at+'. Markdown only; raw sources/archives excluded.'
        foreach ($issue in $response.issues) {$readerState.AppendText("`r`n"+$issue.path+': '+$issue.message)}
    } elseif ($response.op -eq 'open') {
        $script:researchPath=$response.path;$script:researchVersion=($response.version | ConvertTo-Json -Compress)
        $readerText.Text=$response.text
        $readerIdentity.Text=$response.path+"`r`nOriginal Markdown source | Read "+$response.read_at
        $readerState.Text='Full local document. Wrap off for wide tables. Dates and qualifications belong to the source.'
        $readerFind.Text=$readerQuery.Text
        if ($readerFind.Text) {Find-ResearchText $false $true}
        $script:researchLastStat=[DateTime]::UtcNow
    } elseif ($response.op -eq 'stat' -and $response.path -eq $script:researchPath) {
        if (($response.version | ConvertTo-Json -Compress) -cne $script:researchVersion) {
            $readerIdentity.Text=$script:researchPath+"`r`nChanged on disk. This view is retained; choose Reload for the new text."
        }
    }
}
function Poll-Research {
    try {
        if ($script:researchCurrent) {
            if ($script:researchRead.IsCompleted) {
                $line=$script:researchRead.Result
                if (-not $line) {throw 'The read worker stopped. Refresh files to retry.'}
                $response=$line | ConvertFrom-Json
                if ($response.id -ne $script:researchCurrent.id) {throw 'Reader response identity did not match its request'}
                $script:researchCurrent=$null;$script:researchRead=$null
                Apply-ResearchResult $response
                Send-ResearchPending
                $readerCancel.Enabled=($null -ne $script:researchCurrent)
            } elseif (([DateTime]::UtcNow-$script:researchStarted).TotalSeconds -gt 20) {throw 'Reader timed out; previous view retained. Refresh files to retry.'}
        } elseif ($script:researchLoaded -and $script:researchPath -and $tabs.SelectedTab -eq $pages.Research -and ([DateTime]::UtcNow-$script:researchLastStat).TotalSeconds -gt 5) {
            $script:researchLastStat=[DateTime]::UtcNow;Request-Research 'stat' $script:researchPath
        }
    } catch {$readerState.Text='Reader unavailable: '+$_.Exception.Message;Stop-ResearchWorker}
}
$readerDesk.SelectedIndex=0;$readerType.SelectedIndex=0
$readerSearch.Add_Click({Request-Research 'search'})
$readerClear.Add_Click({$readerQuery.Clear();Request-Research 'search'})
$readerRefresh.Add_Click({Request-Research 'scan'})
$readerCancel.Add_Click({$script:researchGeneration++;$script:researchPending=$null;$readerState.Text='Read cancelled. Previous view retained.';$readerCancel.Enabled=$false})
$readerQuery.Add_KeyDown({param($s,$e) if ($e.KeyCode -eq 'Enter') {Request-Research 'search';$e.SuppressKeyPress=$true}})
foreach ($filter in @($readerDesk,$readerType)) {$filter.Add_SelectionChangeCommitted({Request-Research 'search'})}
$readerList.Add_SelectedIndexChanged({
    if (-not $script:researchUpdating -and $readerList.SelectedItems.Count -eq 1) {Request-Research 'open' $readerList.SelectedItems[0].Tag.path}
})
$readerReload.Add_Click({if ($script:researchPath) {Request-Research 'open' $script:researchPath}})
$readerCopy.Add_Click({if ($script:researchPath) {try {[Windows.Forms.Clipboard]::SetText($script:researchPath)} catch {$readerState.Text='Clipboard unavailable: '+$_.Exception.Message}}})
$readerWrap.Add_CheckedChanged({
    # WinForms recreates the native handle for WordWrap. Its RTF round-trip can
    # substitute Unicode punctuation; restore the original Unicode plain text.
    $source=$readerText.Text;$start=$readerText.SelectionStart;$length=$readerText.SelectionLength
    $zoom=$readerText.ZoomFactor
    $readerText.WordWrap=$readerWrap.Checked
    $readerText.Text=$source;$readerText.ZoomFactor=$zoom
    $readerText.Select($start,$length);$readerText.ScrollToCaret()
})
$readerZoomIn.Add_Click({$readerText.ZoomFactor=[Math]::Min(3.0,([double]$readerText.ZoomFactor+0.1))})
$readerZoomOut.Add_Click({$readerText.ZoomFactor=[Math]::Max(0.5,([double]$readerText.ZoomFactor-0.1))})
$readerNext.Add_Click({Find-ResearchText})
$readerPrevious.Add_Click({Find-ResearchText $true})
$readerFind.Add_KeyDown({param($s,$e) if ($e.KeyCode -eq 'Enter') {Find-ResearchText;$e.SuppressKeyPress=$true}})
function Research-WebUri($text) {
    $uri=$null
    if ([Uri]::TryCreate($text,[UriKind]::Absolute,[ref]$uri) -and $uri.Scheme -in @('http','https')) {return $uri.AbsoluteUri}
    return $null
}
$readerText.Add_LinkClicked({param($s,$e)
    $url=Research-WebUri $e.LinkText
    if ($url) {
        try {$psi=New-Object Diagnostics.ProcessStartInfo;$psi.FileName=$url;$psi.UseShellExecute=$true;[void][Diagnostics.Process]::Start($psi)}
        catch {$readerState.Text='Could not open the web link: '+$_.Exception.Message}
    }
})
$tabs.Add_SelectedIndexChanged({if ($tabs.SelectedTab -eq $pages.Research -and -not $script:researchLoaded -and -not $script:researchCurrent) {Request-Research 'scan'}})

function Test-ResearchReader {
    function Wait-Research {
        $until=[DateTime]::UtcNow.AddSeconds(18)
        while ($script:researchCurrent -or $script:researchPending) {
            [Windows.Forms.Application]::DoEvents();Poll-Research
            if ([DateTime]::UtcNow -gt $until) {throw ('Reader test timeout: '+$readerState.Text)}
            Start-Sleep -Milliseconds 10
        }
        if ($readerState.Text -like 'Reader unavailable:*') {throw $readerState.Text}
    }
    Test-Step 'Research: real worker scan and literal search'
    if ($readerDesk.Text -ne 'All three' -or $readerType.Text -ne 'All documents') {throw 'Research defaults are blank'}
    $beforeSettings=$script:settings | ConvertTo-Json -Depth 8 -Compress
    $beforeMembers=@($script:checked.Keys | Sort-Object) -join '|'
    $tabs.SelectedTab=$pages.Research;Wait-Research
    if (-not $script:researchLoaded -or $readerList.Items.Count -lt 6 -or $readerState.Text -notlike 'Search complete:*') {throw ('Research scan failed: '+$readerState.Text)}
    foreach ($sample in @('AGENTS/BROCK/reports/2026-10-21_self-sweep.md','AGENTS/LIQUID/reports/2026-09-17_session.md')) {
        Request-Research 'open' $sample;Wait-Research
        if ($script:researchPath -cne $sample -or $readerText.TextLength -lt 100) {throw ('Representative report failed: '+$sample)}
    }
    $readerDesk.SelectedItem='CARL';$readerQuery.Text='VOID-BY-REVISION';$readerSearch.PerformClick()
    $readerQuery.Text='no-such-cato-fixture-match';$readerSearch.PerformClick();Wait-Research
    if ($readerList.Items.Count -ne 0) {throw 'Old search response replaced newer query'}
    $readerQuery.Text='VOID-BY-REVISION';$readerSearch.PerformClick();Wait-Research
    if ($readerList.Items.Count -ne 1) {throw ('Real body-only search failed: '+$readerState.Text)}
    $readerList.Items[0].Selected=$true;Wait-Research
    if ($readerText.Text -notmatch 'VOID-BY-REVISION' -or $script:researchPath -notlike '*LETTER.md') {throw 'Source read lost the real caveat or identity'}
    $textBefore=$readerText.Text;$pathBefore=$script:researchPath
    Apply-ResearchResult ([pscustomobject]@{id=$script:researchGeneration-1;op='open';ok=$true;path='WRONG';text='WRONG';version=@(0);read_at='now'})
    if ($readerText.Text -cne $textBefore -or $script:researchPath -cne $pathBefore) {throw 'Stale document response replaced the current document'}
    Apply-ResearchResult ([pscustomobject]@{id=$script:researchGeneration;op='stat';ok=$true;path=$pathBefore;version=@(0)})
    if ($readerText.Text -cne $textBefore -or $readerIdentity.Text -notmatch 'Changed on disk') {throw 'Changed source did not preserve reading position/text'}
    Apply-ResearchResult ([pscustomobject]@{id=$script:researchGeneration;op='open';ok=$false;message='Fixture missing file'})
    if ($readerText.Text -cne $textBefore -or $readerState.Text -notmatch 'Previous complete view retained') {throw 'Missing source erased the prior view'}
    $readerReload.PerformClick();Wait-Research
    $readerFind.Text='VOID-BY-REVISION';$readerNext.PerformClick()
    if ($readerText.SelectedText -ne 'VOID-BY-REVISION') {throw 'Document find failed'}
    $readerWrap.Checked=$false
    if ($readerText.WordWrap) {throw 'Table wrapping could not be disabled'}
    $readerZoomIn.PerformClick()
    if ($readerText.ZoomFactor -le 1) {throw 'Reader zoom failed'}
    $readerZoomOut.PerformClick();$readerWrap.Checked=$true
    Test-Step 'Research: independence and explicit incomplete state'
    $tabs.SelectedTab=$pages.Instructions;$tabs.SelectedTab=$pages.Research
    if ($readerText.Text -cne $textBefore) {throw 'Wrap/zoom/tab controls altered the source text'}
    $readerQuery.Text=[string][char]0x2014;$readerSearch.PerformClick();Wait-Research
    if ($readerList.Items.Count -lt 1) {throw 'Unicode query did not survive the Windows/WSL pipe'}
    $script:busy=$true;$script:queue.Enqueue(@{name='ISOLATED_READER_TEST'})
    try {
        $readerQuery.Text='VOID-BY-REVISION';Request-Research 'search';Wait-Research
        if ($script:queue.Count -ne 1 -or -not $script:busy) {throw 'Reader altered launch queue'}
    } finally {$script:queue.Clear();$script:busy=$false}
    if (($script:settings | ConvertTo-Json -Depth 8 -Compress) -cne $beforeSettings -or (@($script:checked.Keys | Sort-Object) -join '|') -cne $beforeMembers) {throw 'Reader changed launch settings or membership'}
    if (Research-WebUri 'file:///C:/Windows/system32/cmd.exe') {throw 'Reader accepted file execution link'}
    if (Research-WebUri 'javascript:alert(1)') {throw 'Reader accepted script link'}
    if (-not (Research-WebUri 'https://example.org/a?b=1&c=2')) {throw 'Reader rejected ordinary HTTPS link'}
    Apply-ResearchResult ([pscustomobject]@{id=$script:researchGeneration;op='search';ok=$true;documents=@();total=2;complete=$false;scanned_at='fixture';issues=@([pscustomobject]@{path='fixture.md';message='Unreadable'})})
    if ($readerState.Text -notmatch 'Search incomplete' -or $readerState.Text -notmatch 'fixture.md') {throw 'Incomplete search was presented as clean absence'}
    $readerRefresh.PerformClick();$readerCancel.PerformClick();Wait-Research
    if ($readerState.Text -notmatch 'cancelled') {throw 'Cancelled read replaced its state'}
    $readerQuery.Clear();$readerDesk.SelectedIndex=0;$readerRefresh.PerformClick();Wait-Research
    # Leave an actual document open for visual inspection.
    $readerReload.PerformClick();Wait-Research
    $readerText.Select(0,0);$readerText.ScrollToCaret()
}

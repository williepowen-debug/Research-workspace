"""Opt-in native batch probe. Only isolated fake CLIs run; no model calls."""
import base64
import getpass
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import agents_gui as gui

base = Path(tempfile.mkdtemp(prefix='cato-gui-proof-'))
binpath = base / 'bin'
binpath.mkdir()
release = base / 'release'
projects = [base / "project ; ' & space", base / 'missing', base / 'second project']
for project in (projects[0], projects[2]):
    project.mkdir()
fake_source = ('#!/usr/bin/python3\nimport json,os,sys,time\nfrom pathlib import Path\n'
               'Path("capture.json").write_text(json.dumps({"argv":sys.argv[1:],"cwd":os.getcwd(),"tty":sys.stdin.isatty(),"start":time.monotonic()}))\n'
               'deadline=time.monotonic()+60\n'
               'while not Path(' + repr(str(release)) + ').exists() and time.monotonic()<deadline: time.sleep(.1)\n'
               'Path("exited").write_text("done")\n')
for runtime in ('codex', 'claude'):
    fake = binpath / runtime
    fake.write_text(fake_source)
    fake.chmod(0o755)
entries = [dict(name=name, path='~/' + os.path.relpath(project, Path.home()),
                purpose='Harmless UI integration fixture', group='Tests', kind='project',
                default_runtime='sol', prompt='Do not start a research agent.')
           for name, project in zip(('LAUNCHER_TEST', 'MISSING_TEST', 'SECOND_TEST'), projects)]
config = base / 'agents.json'
config.write_text(json.dumps(dict(version=1, agents=entries)))
(base / 'context.json').write_text(json.dumps(dict(config=str(config), path=str(binpath) + os.pathsep + os.environ['PATH'])))
data = dict(test_mode=True, agents=[dict(entry, folder=str(project), error='') for entry, project in zip(entries, projects)],
            directory=gui.windows_path(base), linux_directory=str(base), distro=os.environ['WSL_DISTRO_NAME'],
            user=getpass.getuser(), python=sys.executable, bridge=str(Path(gui.__file__).resolve()))
snapshot = base / 'catalogue.json'
snapshot.write_text(json.dumps(data))
task = 'GUI literal café "quotes" ; $(never-run) &\nsecond line'
source = (SCRIPTS / 'agents_gui.ps1').read_text()
# Inject fixture-only actions into the production form, using its real buttons,
# modal review, queue, worker, result timer, and error handling unchanged.
hook = r'''
[Windows.Forms.Application]::add_ThreadException({param($sender,$e)
    @{error=$e.Exception.ToString();refresh_failure=$script:refreshFailure;status=$status.Text} |
        ConvertTo-Json -Depth 5 | Set-Content -Encoding UTF8 (Join-Path $data.directory 'test-error.json')
    $script:queue.Clear(); $form.Close()
})
$script:choice='Cancel'
$script:cancelVerified=$false
$script:previewSeen=''
$script:refreshVerified=$false
$dialogProbe=New-Object Windows.Forms.Timer
$dialogProbe.Interval=150
$dialogProbe.Add_Tick({
    foreach ($window in @([Windows.Forms.Application]::OpenForms)) {
        if ($window.Text -eq 'Review selected agents') {
            foreach ($control in $window.Controls) {
                if ($control -is [Windows.Forms.TextBox]) {$script:previewSeen=$control.Text}
            }
            foreach ($control in $window.Controls) {
                if ($control -is [Windows.Forms.Button] -and $control.Text -eq $script:choice) {$control.PerformClick();break}
            }
        }
    }
})
$probe=New-Object Windows.Forms.Timer
$probe.Interval=250
$probeDeadline=[DateTime]::UtcNow.AddSeconds(50)
$probe.Add_Tick({
    if (-not $script:refreshVerified -and [DateTime]::UtcNow -lt $probeDeadline) {
        if ($script:refreshProcess) {return}
        if ($script:refreshFailure -or ($script:settings | ConvertTo-Json -Depth 8 -Compress) -cne $script:expectedSettings -or $script:checked.Count -ne 3 -or $script:selected.name -ne 'SECOND_TEST') {throw 'Real refresh lost prepared settings or failed'}
        $script:refreshVerified=$true
        $probe.Stop()
        $dialogProbe.Start(); $batch.PerformClick()
        $script:cancelVerified=(-not $script:busy -and $script:queue.Count -eq 0 -and $results.TextLength -eq 0 -and $script:history.Count -eq 0)
        $script:choice='Launch selected'; $batch.PerformClick()
        $probe.Start()
    }
    if (-not $script:busy -or [DateTime]::UtcNow -gt $probeDeadline) {
        @{busy=$script:busy;status=$status.Text;results=$results.Text;checked=$script:checked.Count;
          cancel_verified=$script:cancelVerified;refresh_verified=$script:refreshVerified;preview=$script:previewSeen;
          page=$tabs.SelectedTab.Name;history=@($script:history);history_file=$script:historyPath} |
          ConvertTo-Json -Depth 8 | Set-Content -Encoding UTF8 (Join-Path $data.directory 'ui-result.json')
        $probe.Stop();$script:queue.Clear();$form.Close()
    }
})
$form.Add_Shown({
    $list.SetItemChecked(0,$true);$list.SetItemChecked(1,$true);$list.SetItemChecked(2,$true)
    $runtime.SelectedItem='Claude Opus'
    $task.Text=[Text.Encoding]::UTF8.GetString([Convert]::FromBase64String('TASK'))
    Focus-Agent 'LAUNCHER_TEST'; $runtime.SelectedItem='Codex Sol'
    Focus-Agent 'SECOND_TEST'; $task.Text='Only the second agent receives this task.'
    $script:expectedSettings=$script:settings | ConvertTo-Json -Depth 8 -Compress
    $tabs.SelectedTab=$pages.Activity; $refreshEvidence.PerformClick()
    $probe.Start()
})
'''.replace('TASK', base64.b64encode(task.encode()).decode())
source = source.replace('[void]$form.ShowDialog()', hook + '\n[void]$form.ShowDialog()')
psfile = base / 'probe.ps1'
psfile.write_text(source)
cmd = ['powershell.exe', '-NoProfile', '-STA', '-ExecutionPolicy', 'Bypass', '-File',
       gui.windows_path(psfile), '-DataFile', gui.windows_path(snapshot)]
try:
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=65)
    print('Probe directory:', base)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    if (base / 'test-error.json').exists():
        raise AssertionError((base / 'test-error.json').read_text(encoding='utf-8-sig'))
    assert result.returncode == 0, result.returncode
    ui = json.loads((base / 'ui-result.json').read_text(encoding='utf-8-sig'))
    assert not ui['busy'] and ui['cancel_verified'] and ui['refresh_verified'], ui
    assert '3 attempted, 1 not confirmed' in ui['status'], ui
    assert 'Not confirmed - MISSING_TEST' in ui['results'], ui
    assert 'Opened - LAUNCHER_TEST' in ui['results'] and 'Opened - SECOND_TEST' in ui['results'], ui
    assert ui['checked'] == 1, ui  # Only the failed agent remains checked.
    assert ui['page'] == 'Activity', ui
    assert len(ui['history']) == 3, ui  # Preview cancellation creates no launch record.
    records = {record['name']: record for record in ui['history']}
    assert records['LAUNCHER_TEST']['outcome'] == 'Opened', ui
    assert records['MISSING_TEST']['outcome'] == 'Not confirmed', ui
    assert records['SECOND_TEST']['outcome'] == 'Opened', ui
    assert records['LAUNCHER_TEST']['runtime'] == 'sol', ui
    assert records['SECOND_TEST']['runtime'] == 'opus', ui
    assert records['LAUNCHER_TEST']['task'] == task, ui
    assert records['SECOND_TEST']['task'] == 'Only the second agent receives this task.', ui
    history_file = Path(subprocess.check_output(['wslpath', '-u', ui['history_file']], text=True).strip())
    saved_history = json.loads(history_file.read_text(encoding='utf-8-sig'))
    assert saved_history['history'] == ui['history'], 'Launch history was not persisted'
    assert 'Codex Sol' in ui['preview'] and 'Claude Opus' in ui['preview'], ui
    assert task.replace('\n', '\r\n') in ui['preview'].replace('\r\n', '\n').replace('\n', '\r\n'), ui
    captures = [json.loads((p / 'capture.json').read_text()) for p in (projects[0], projects[2])]
    assert all(c['tty'] for c in captures), captures
    assert captures[0]['cwd'] == str(projects[0]) and captures[1]['cwd'] == str(projects[2]), captures
    assert captures[0]['argv'][-1].endswith(task), captures
    assert captures[1]['argv'][-1].endswith('Only the second agent receives this task.'), captures
    assert 'gpt-6.1-sol' in captures[0]['argv'] and '--dangerously-skip-permissions' in captures[1]['argv'], captures
    assert captures[1]['argv'][captures[1]['argv'].index('--model') + 1] == 'opus', captures
    assert not any((p / 'exited').exists() for p in (projects[0], projects[2])), 'Both agents must still be running together'
    assert len(list(base.glob('*.claimed'))) == 3, 'Cancel or double click dispatched extra requests'
    (base / 'proof.json').write_text(json.dumps(dict(ok=True, ui=ui, captures=captures), indent=2))
    print('PASS: real preview cancel/confirm, 3 queued requests, independent Sol/Opus tasks, continued after missing folder, 2 concurrent fake CLIs, 1 retained error, Activity page, and 3 exact persisted launch records.')
finally:
    release.touch()  # The harmless terminal windows exit automatically.

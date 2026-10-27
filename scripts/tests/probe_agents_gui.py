"""Opt-in Windows GUI integration probe; opens only a fake CLI, never a model."""
import getpass,json,os,sys,subprocess,tempfile,time
from pathlib import Path
SCRIPTS=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(SCRIPTS))
import agents_gui as gui
base=Path(tempfile.mkdtemp(prefix='cato-gui-proof-'))
project=base / "project ; ' & space"
project.mkdir()
binpath=base/'bin';binpath.mkdir()
capture=base/'capture.json'
fake=binpath/'codex'
fake.write_text('#!/usr/bin/python3\nimport json,os,sys,time\nfrom pathlib import Path\nPath('+repr(str(capture))+').write_text(json.dumps({"argv":sys.argv[1:],"cwd":os.getcwd(),"tty":sys.stdin.isatty()}))\ntime.sleep(1)\n')
fake.chmod(0o755)
entry=dict(name='LAUNCHER_TEST',path='~/'+os.path.relpath(project,Path.home()),purpose='Harmless UI integration fixture',group='Tests',kind='project',default_runtime='sol',prompt='Do not start a research agent.')
config=base/'agents.json';config.write_text(json.dumps(dict(version=1,agents=[entry])))
context=dict(config=str(config),path=str(binpath)+os.pathsep+os.environ['PATH'])
(base/'context.json').write_text(json.dumps(context))
data=dict(agents=[dict(entry,folder=str(project),error='')],directory=gui.windows_path(base),linux_directory=str(base),distro=os.environ['WSL_DISTRO_NAME'],user=getpass.getuser(),python=sys.executable,bridge=str(Path(gui.__file__).resolve()))
snapshot=base/'catalogue.json';snapshot.write_text(json.dumps(data))
task='GUI literal café "quotes" ; $(never-run) &\nsecond line'
# Add a fixture-only click to the real UI source, then observe its actual timer/result.
source=(SCRIPTS/'agents_gui.ps1').read_text()
hook='''
$probe = New-Object Windows.Forms.Timer
$probe.Interval=250
$probeDeadline=[DateTime]::UtcNow.AddSeconds(45)
$probe.Add_Tick({
    if (-not $script:busy -or [DateTime]::UtcNow -gt $probeDeadline) {
        @{busy=$script:busy;status=$status.Text;start_enabled=$start.Enabled;resume_enabled=$resume.Enabled} | ConvertTo-Json | Set-Content (Join-Path $data.directory 'ui-result.json')
        $probe.Stop();$form.Close()
    }
})
$form.Add_Shown({
    $task.Text=[Text.Encoding]::UTF8.GetString([Convert]::FromBase64String('TASK'))
    $start.PerformClick()
    $probe.Start()
})
'''
import base64
hook=hook.replace('TASK',base64.b64encode(task.encode()).decode())
source=source.replace('[void]$form.ShowDialog()',hook+'\n[void]$form.ShowDialog()')
psfile=base/'probe.ps1';psfile.write_text(source)
cmd=['powershell.exe','-NoProfile','-STA','-ExecutionPolicy','Bypass','-File',gui.windows_path(psfile),'-DataFile',gui.windows_path(snapshot)]
result=subprocess.run(cmd,capture_output=True,text=True,timeout=60)
print('Probe directory:',base)
print('PowerShell exit:',result.returncode)
if result.stdout:print(result.stdout)
if result.stderr:print(result.stderr)
ui=json.loads((base/'ui-result.json').read_text(encoding='utf-8-sig'))
actual=json.loads(capture.read_text())
assert not ui['busy'] and 'opened.' in ui['status'],ui
assert ui['start_enabled'] and not ui['resume_enabled'],ui
assert actual['tty'] and actual['cwd']==str(project),actual
assert actual['argv'][-1].endswith(task),actual
(base/'proof.json').write_text(json.dumps(dict(ok=True,base=str(base),ui=ui,capture=actual),indent=2))
print('PASS: real GUI click -> WSL bridge -> Windows Terminal -> fake CLI; exact task/cwd, interactive TTY, responsive completion.')

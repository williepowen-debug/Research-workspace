"""Windows/WSL startup transport test with a harmless substitute UI; no agents."""
import getpass
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import time
import uuid

SCRIPTS = Path(__file__).resolve().parents[1]

def win(path):
    return subprocess.check_output(['wslpath', '-w', str(path)], text=True).strip()


def wait_for(check, message, timeout=20):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if check():
            return
        time.sleep(.1)
    raise AssertionError(message)


def main():
    base = Path(tempfile.mkdtemp(prefix='launcher-single-instance-'))
    shutil.copy(SCRIPTS / 'agents_gui_bootstrap.ps1', base)
    # Exercise the real mutex/event/loading host while replacing only the final UI.
    (base / 'agents_gui.ps1').write_text(r'''
param([string]$DataFile,[string]$ActivationEvent)
$folder=Split-Path $DataFile
[IO.File]::AppendAllText((Join-Path $folder 'opened'),"opened`n")
$event=[Threading.EventWaitHandle]::OpenExisting($ActivationEvent)
try {
    $deadline=[DateTime]::UtcNow.AddSeconds(35)
    while (-not (Test-Path (Join-Path $folder 'close')) -and [DateTime]::UtcNow -lt $deadline) {
        if ($event.WaitOne(100)) {[IO.File]::AppendAllText((Join-Path $folder 'activated'),"activated`n")}
    }
} finally {$event.Dispose()}
''')
    worker = base / 'prepare.py'
    worker.write_text('import time\nfrom pathlib import Path\ntime.sleep(2)\n'
                      'Path(__file__).with_name("catalogue.json").write_text("{}")\n')
    context = base / 'context.json'
    context.write_text(json.dumps({'instance': 'test-' + uuid.uuid4().hex, 'test_mode': True,
        'prepare_arguments': subprocess.list2cmdline(['-d', os.environ['WSL_DISTRO_NAME'],
            '-u', getpass.getuser(), '--exec', '/usr/bin/python3', str(worker)])}))
    command = ['powershell.exe', '-NoProfile', '-STA', '-ExecutionPolicy', 'Bypass',
               '-File', win(base / 'agents_gui_bootstrap.ps1'), '-ContextFile', win(context)]
    children = []
    def start():
        proc = subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        children.append(proc)
        return proc
    try:
        first = start()
        time.sleep(.8)
        second = start()  # contention while evidence is still loading
        assert second.wait(timeout=15) == 0, second.stderr.read().decode()
        wait_for(lambda: (base / 'opened').exists(), 'First UI did not open')
        third = start()  # activation after the UI opens
        assert third.wait(timeout=15) == 0
        wait_for(lambda: (base / 'activated').exists(), 'Existing UI was not signaled')
        assert (base / 'opened').read_text().splitlines() == ['opened'], 'Duplicate UI'
        (base / 'close').touch()
        assert first.wait(timeout=15) == 0
        (base / 'close').unlink()
        fourth = start()
        wait_for(lambda: len((base / 'opened').read_text().splitlines()) == 2, 'Normal close did not release ownership')
        fourth.kill(); fourth.wait(timeout=10)
        fifth = start()
        wait_for(lambda: len((base / 'opened').read_text().splitlines()) == 3, 'Crashed host blocked restart')
        (base / 'close').touch()
        assert fifth.wait(timeout=15) == 0
        # Use the real UI/prepare bridge for the final restore check, with a
        # temporary configuration and no launch-button interaction.
        config = base / 'agents.json'
        config.write_text(json.dumps({'version': 1, 'agents': [{
            'name': 'WINDOW_TEST', 'path': '~/' + os.path.relpath(base, Path.home()), 'purpose': 'Isolated window test',
            'group': 'Tests', 'kind': 'project', 'default_runtime': 'sol',
            'prompt': 'Do not launch.'}]}))
        worker.write_text('import sys,json\nfrom pathlib import Path\n'
            + 'sys.path.insert(0,' + repr(str(SCRIPTS)) + ')\nimport agents_gui\n'
            + 'p=Path(__file__).with_name("context.json")\nagents_gui.prepare_gui(p)\n'
            + 'p=p.with_name("catalogue.json")\nd=json.loads(p.read_text())\n'
            + 'd["test_mode"]=True\np.write_text(json.dumps(d))\n')
        data = json.loads(context.read_text())
        data.update(config=str(config), path=os.environ['PATH'],
                    distro=os.environ['WSL_DISTRO_NAME'], user=getpass.getuser())
        context.write_text(json.dumps(data))
        for dependency in ('research_reader.ps1', 'decisions_launcher.ps1', 'calendar_launcher.ps1'):
            shutil.copy(SCRIPTS / dependency, base)
        hook = r"""
$form.Add_Shown({
    $form.WindowState='Minimized'
    [IO.File]::WriteAllText((Join-Path $data.directory 'minimized'),'ready')
})
$restoreProbe=New-Object Windows.Forms.Timer
$restoreProbe.Interval=200
$restoreProbe.Add_Tick({
    if ((Test-Path (Join-Path $data.directory 'minimized')) -and $form.WindowState -eq 'Normal') {
        [IO.File]::WriteAllText((Join-Path $data.directory 'restored'),'ok')
        $restoreProbe.Stop(); $form.Close()
    }
})
$restoreProbe.Start()
"""
        (base / 'agents_gui.ps1').write_text((SCRIPTS / 'agents_gui.ps1').read_text().replace(
            '$activationTimer=$null; $activationSignal=$null', hook + '\n$activationTimer=$null; $activationSignal=$null'))
        (base / 'close').unlink()
        sixth = start()
        wait_for(lambda: (base / 'minimized').exists(), 'Real UI did not load/minimize', 35)
        seventh = start()
        assert seventh.wait(timeout=15) == 0
        wait_for(lambda: (base / 'restored').exists(), 'Real UI did not restore')
        assert sixth.wait(timeout=15) == 0
        print('PASS: real preparation/UI minimize-restore; simultaneous opening, existing-window signal, close/reopen, crash/reopen; ' + str(base))
    finally:
        (base / 'close').touch()
        for child in children:
            if child.poll() is None:
                child.kill()
            child.communicate(timeout=10)

if __name__ == '__main__':
    main()

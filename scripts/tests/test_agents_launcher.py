"""Behavior tests for the personal launcher; never invoke a real agent/model."""
import contextlib
import base64
import importlib.util
import io
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1]


def module(name, filename):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / filename)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


agents = module('personal_agents_test', 'agents.py')
installer = module('personal_agents_installer_test', 'install_agents.py')
sys.modules['agents'] = agents
gui = module('personal_agents_gui_test', 'agents_gui.py')


class LauncherTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='agent-launcher-test-')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.project = self.base / 'project with spaces'
        self.project.mkdir()
        (self.project / 'HANDOFF.md').write_text('Isolated test project; no real agent.')
        self.entry = {'name': 'FIXTURE', 'path': '~/' + os.path.relpath(self.project, Path.home()),
                      'purpose': 'Test project', 'group': 'Tests', 'kind': 'project',
                      'default_runtime': 'sol', 'required': ['HANDOFF.md'],
                      'prompt': 'Read HANDOFF.md.'}
        self.config = self.base / 'agents.json'
        self.config.write_text(json.dumps({'version': 1, 'agents': [self.entry]}))
        self.bin = self.base / 'bin'
        self.bin.mkdir()
        self.capture = self.base / 'capture.json'
        fake = ('#!' + sys.executable + '\n'
                'import json,os,sys,time,signal\nfrom pathlib import Path\n'
                'def interrupted(*_): Path(os.environ["CAPTURE"]+".interrupt").write_text("handled")\n'
                'signal.signal(signal.SIGINT,interrupted)\n'
                'Path(os.environ["CAPTURE"]).write_text(json.dumps({"args":sys.argv[1:],"cwd":os.getcwd()}))\n'
                'if os.environ.get("WAIT_FOR_RELEASE"):\n'
                ' end=time.monotonic()+10\n'
                ' while not Path(os.environ["WAIT_FOR_RELEASE"]).exists() and time.monotonic()<end: time.sleep(.02)\n'
                'sys.exit(int(os.environ.get("FAKE_EXIT","0")))\n')
        for name in ('codex', 'claude'):
            f = self.bin / name
            f.write_text(fake)
            f.chmod(0o755)
        self.env = dict(os.environ, PATH=str(self.bin) + os.pathsep + os.environ.get('PATH', ''),
                        CAPTURE=str(self.capture), XDG_CACHE_HOME=str(self.base / 'cache'),
                        PYTHONDONTWRITEBYTECODE='1')

    def cli(self, *args, env=None):
        return subprocess.run([sys.executable, str(SCRIPTS / 'agents.py'), '--config', str(self.config), '--same-window', *args],
                              env=env or self.env, text=True, capture_output=True, timeout=15)

    def gui_request(self, **values):
        (self.base / 'context.json').write_text(json.dumps({'config': str(self.config), 'path': self.env['PATH']}))
        request = self.base / (str(time.time_ns()) + '.json')
        request.write_text(json.dumps(dict(name='FIXTURE', runtime='sol', action='new', task=None, **values)), encoding='utf-8-sig')
        return request

    def test_gui_click_routes_literal_task_and_request_is_single_use(self):
        task = 'Unicode café; $(never-run) "quotes"\nsecond line'
        request = self.gui_request()
        request.write_text(json.dumps(dict(name='FIXTURE', runtime='claude', action='new', task=task)), encoding='utf-8-sig')
        with patch.dict(os.environ, self.env), patch.object(agents, 'open_window', return_value=0) as launch:
            self.assertEqual(gui.launch_request(request), 0)
            self.assertEqual(gui.launch_request(request), 2)
        self.assertEqual(launch.call_count, 1)
        plan = launch.call_args.args[0]
        self.assertEqual(plan.runtime, 'claude')
        self.assertTrue(plan.argv[-1].endswith(task))
        self.assertTrue(json.loads(request.with_suffix('.result.json').read_text())['ok'])

    def test_gui_revalidates_config_and_returns_errors_without_launch(self):
        request = self.gui_request()
        self.config.write_text('{"version":1,"agents":[]}')
        with patch.dict(os.environ, self.env), patch.object(agents, 'open_window') as launch:
            self.assertEqual(gui.launch_request(request), 2)
        launch.assert_not_called()
        self.assertFalse(json.loads(request.with_suffix('.result.json').read_text())['ok'])

    def test_gui_resume_policy_and_window_failure(self):
        request = self.gui_request()
        request.write_text(json.dumps(dict(name='FIXTURE', runtime='sol', action='resume', task='Do not discard me')))
        with patch.dict(os.environ, self.env), patch.object(agents, 'open_window') as launch:
            self.assertEqual(gui.launch_request(request), 2)
            launch.assert_not_called()
        request = self.gui_request()
        request.write_text(json.dumps(dict(name='FIXTURE', runtime='sol', action='resume', task=None)))
        with patch.dict(os.environ, self.env), patch.object(agents, 'open_window', side_effect=agents.LaunchError('No window')) as launch:
            self.assertEqual(gui.launch_request(request), 2)
        self.assertIn('resume', launch.call_args.args[0].argv)
        self.assertEqual(json.loads(request.with_suffix('.result.json').read_text())['message'], 'No window')

    def test_real_dispatch_preserves_cwd_and_literal_task(self):
        marker = self.base / 'must not exist'
        task = f'Quotes " and apostrophe \' ; $(touch "{marker}") `touch "{marker}"`\nsecond line'
        result = self.cli('fixture', '--sol', '--new', '--task', task)
        self.assertEqual(result.returncode, 0, result.stderr)
        capture = json.loads(self.capture.read_text())
        self.assertEqual(capture['cwd'], str(self.project))
        self.assertIn('gpt-6.1-sol', capture['args'])
        self.assertEqual(capture['args'][-1], 'Read HANDOFF.md.\n\nWill\'s task: ' + task)
        self.assertFalse(marker.exists())

    def test_runtime_exit_is_returned_without_retry(self):
        result = self.cli('fixture', '--new', env=dict(self.env, FAKE_EXIT='17'))
        self.assertEqual(result.returncode, 17)

    def test_resume_picker_and_claude_dispatch(self):
        result = self.cli('fixture', '--resume')
        self.assertEqual(result.returncode, 0, result.stderr)
        args = json.loads(self.capture.read_text())['args']
        self.assertEqual(args[0], 'resume')
        self.assertNotIn('--last', args)
        self.assertNotIn('Read HANDOFF.md.', args)
        result = self.cli('fixture', '--claude', '--resume')
        self.assertEqual(result.returncode, 0, result.stderr)
        args = json.loads(self.capture.read_text())['args']
        self.assertIn('--resume', args)
        self.assertNotIn('--model', args)

    def test_dry_run_and_list_do_not_dispatch_or_create_locks(self):
        for args in [('fixture', '--dry-run'), ('--list',)]:
            result = self.cli(*args)
            self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(self.capture.exists())
        self.assertFalse((self.base / 'cache').exists())

    def test_unknown_agent_noninteractive_mode_and_resume_task_refused(self):
        for args in [('missing', '--new'), ('fixture',), (), ('fixture', '--resume', '--task', 'wrong mode')]:
            result = self.cli(*args)
            self.assertEqual(result.returncode, 2, (args, result.stderr))
        self.assertFalse(self.capture.exists())

    def test_missing_folder_and_startup_evidence_refused(self):
        (self.project / 'HANDOFF.md').unlink()
        result = self.cli('fixture', '--new')
        self.assertEqual(result.returncode, 2)
        self.assertIn('HANDOFF.md', result.stderr)
        self.project.rmdir()
        result = self.cli('fixture', '--new')
        self.assertEqual(result.returncode, 2)
        self.assertIn(str(self.project), result.stderr)
        self.assertFalse(self.capture.exists())

    def test_missing_executable_is_actionable(self):
        plan = agents.build_plan(self.entry, None, 'new')
        with patch.object(agents.shutil, 'which', return_value=None):
            with self.assertRaisesRegex(agents.LaunchError, 'codex is not on PATH'):
                agents.validate_plan(plan)

    def test_config_duplicate_and_malformed_data_fail_closed(self):
        for data in [{'version': 1, 'agents': [self.entry, self.entry]},
                     {'version': 9, 'agents': [self.entry]},
                     {'version': 1, 'agents': [dict(self.entry, claude_args='bad')]}]:
            self.config.write_text(json.dumps(data))
            result = self.cli('fixture', '--new')
            self.assertEqual(result.returncode, 2)
        self.config.write_text('{broken')
        self.assertEqual(self.cli('fixture', '--new').returncode, 2)
        self.assertFalse(self.capture.exists())

    def test_root_escape_rejected_and_home_projects_supported(self):
        with self.assertRaisesRegex(agents.LaunchError, 'escapes'):
            agents.resolve_folder('../wrong-owner', self.base)
        self.assertEqual(agents.resolve_folder('~/project', self.base, self.base), self.base / 'project')

    def test_production_special_cases_preserve_settings(self):
        entries = {e['name']: e for e in agents.load_config(SCRIPTS / 'agents.json')}
        self.assertEqual(len(entries), 51)
        for action in ('new', 'resume'):
            walter = agents.build_plan(entries['WALTER'], 'claude', action)
            self.assertNotIn('--channels', walter.argv)
            self.assertNotIn('plugin:telegram@claude-plugins-official', walter.argv)
            self.assertNotIn('--channels', agents.build_plan(entries['WALTER'], 'sol', action).argv)
        for name in ('STUE', 'POLLY', 'DOC', 'GIG', 'PHAN', 'POP'):
            plan = agents.build_plan(entries[name], 'sol', 'new')
            self.assertEqual(plan.cwd, agents.ROOT / 'AGENTS/CARL/sub_agents' / name)
            self.assertIn('Resolve the Git root', plan.argv[-1])
        cato = entries['CATO']
        new = agents.build_plan(cato, None, 'new', '--leading task')
        self.assertEqual(new.argv[-2:], ['--', '--leading task'])
        self.assertEqual(new.argv[0], 'bash')
        resume = agents.build_plan(cato, None, 'resume')
        self.assertIn('gpt-6-astra', resume.argv)
        self.assertIn('on-request', resume.argv)
        for runtime in ('sol', 'claude'):
            with self.assertRaises(agents.LaunchError): agents.build_plan(cato, runtime, 'new')

    def test_menu_uses_selected_runtime_and_resume(self):
        with patch.object(agents.sys.stdin, 'isatty', return_value=True), \
             patch('builtins.input', side_effect=['fixture', 'c', '2', 'q']), \
             patch.object(agents, 'validate_plan'), patch.object(agents, 'execute', return_value=0) as run, \
             contextlib.redirect_stdout(io.StringIO()):
            rc = agents.main(['--config', str(self.config), '--same-window'])
        self.assertEqual(rc, 0)
        self.assertEqual(run.call_args.args[0].runtime, 'claude')
        self.assertEqual(run.call_args.args[0].action, 'resume')

    def test_group_menu_and_cancellation(self):
        for answers, expected_calls in [(['1', '1', '', '1', 'q'], 1), (['q'], 0), (['fixture', 'q'], 0)]:
            with patch.object(agents.sys.stdin, 'isatty', return_value=True), \
                 patch('builtins.input', side_effect=answers), patch.object(agents, 'validate_plan'), \
                 patch.object(agents, 'execute', return_value=0) as run, contextlib.redirect_stdout(io.StringIO()):
                rc = agents.main(['--config', str(self.config), '--same-window'])
            self.assertEqual(rc, 0)
            self.assertEqual(run.call_count, expected_calls)

    def test_local_lock_uses_folder_not_name_or_runtime_and_releases(self):
        plan = agents.build_plan(self.entry, None, 'new')
        alias = agents.build_plan(dict(self.entry, name='OTHER'), 'claude', 'resume')
        state = self.base / 'locks'
        with agents.session_lock(plan, state):
            with self.assertRaisesRegex(agents.LaunchError, 'already owns'):
                with agents.session_lock(alias, state): pass
            other = agents.Plan('SEPARATE', self.base / 'other', 'sol', 'new', [], [])
            with agents.session_lock(other, state): pass
        with agents.session_lock(alias, state): pass

    def test_live_process_overlap_and_interrupt_then_recovery(self):
        release = self.base / 'release'
        env = dict(self.env, WAIT_FOR_RELEASE=str(release))
        proc = subprocess.Popen([sys.executable, str(SCRIPTS / 'agents.py'), '--config', str(self.config),
                                 'fixture', '--new', '--same-window'], env=env, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True, start_new_session=True)
        try:
            deadline = time.monotonic() + 5
            while not self.capture.exists() and proc.poll() is None and time.monotonic() < deadline:
                time.sleep(.02)
            self.assertTrue(self.capture.exists(), 'fake CLI did not start')
            result = self.cli('fixture', '--claude', '--resume')
            self.assertEqual(result.returncode, 2)
            self.assertIn('already owns', result.stderr)
            os.killpg(proc.pid, signal.SIGINT)
            interrupted = Path(str(self.capture) + '.interrupt')
            deadline = time.monotonic() + 2
            while not interrupted.exists() and time.monotonic() < deadline: time.sleep(.02)
            self.assertTrue(interrupted.exists())
            self.assertIsNone(proc.poll(), 'Ctrl+C killed the launcher/CLI')
            release.write_text('done')
            stdout, stderr = proc.communicate(timeout=5)
            self.assertEqual(proc.returncode, 0, stderr)
            self.assertEqual(self.cli('fixture', '--new').returncode, 0)
        finally:
            release.write_text('done')
            if proc.poll() is None: proc.terminate()
            proc.communicate(timeout=5)

    def test_lock_storage_error_blocks_instead_of_launching(self):
        cache = self.base / 'not a directory'
        cache.write_text('occupied')
        result = self.cli('fixture', '--new', env=dict(self.env, XDG_CACHE_HOME=str(cache)))
        self.assertEqual(result.returncode, 2)
        self.assertFalse(self.capture.exists())

    def test_window_command_has_new_window_title_and_encoded_paths(self):
        plan = agents.build_plan(self.entry, None, 'new', 'do not interpret ; & $()')
        request = self.base / "space ' ; &" / 'request.json'
        with patch.object(agents.shutil, 'which', side_effect=lambda name: name), \
             patch.dict(os.environ, {'WSL_DISTRO_NAME': 'Ubuntu'}):
            command = agents.window_command(plan, request)
        self.assertIn('-EncodedCommand', command)
        script = base64.b64decode(command[-1]).decode('utf-16le')
        self.assertIn('-w new new-tab', script)
        self.assertIn('FIXTURE - Codex Sol', script)
        self.assertIn('--suppressApplicationTitle', script)
        self.assertIn('--exec', script)  # WSL's bare -- still goes through the default shell.
        self.assertNotIn(str(request), script)
        self.assertNotIn('do not interpret', script)

    def test_window_handoff_exact_task_lock_and_single_use(self):
        task = 'quotes " \' ; & $(touch nope)\nnext line'
        plan = agents.build_plan(self.entry, None, 'new', task)
        requested = []
        def command(_plan, request):
            requested.append(request)
            return ['fake-terminal']
        real_run = subprocess.run
        def transport(cmd, **kwargs):
            self.assertEqual(cmd, ['fake-terminal'])
            result = real_run([sys.executable, str(SCRIPTS / 'agents.py'), '--window-request', str(requested[-1])],
                              env=self.env, capture_output=True, text=True, timeout=5)
            self.assertEqual(result.returncode, 0, result.stderr)
            return subprocess.CompletedProcess(cmd, 0, '', '')
        with patch.dict(os.environ, self.env), patch.object(agents, 'window_command', side_effect=command), \
             patch.object(agents.subprocess, 'run', side_effect=transport), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(agents.open_window(plan), 0)
        capture = json.loads(self.capture.read_text())
        self.assertEqual(capture['args'][-1], 'Read HANDOFF.md.\n\nWill\'s task: ' + task)
        self.assertEqual(capture['cwd'], str(self.project))
        replay = real_run([sys.executable, str(SCRIPTS / 'agents.py'), '--window-request', str(requested[-1])],
                          env=self.env, text=True, capture_output=True)
        self.assertEqual(replay.returncode, 2)
        self.assertIn('already claimed', replay.stderr)

    def test_window_errors_and_missing_ack_are_not_success(self):
        plan = agents.build_plan(self.entry, None, 'new')
        for result, expected in [(subprocess.CompletedProcess([], 7, '', 'launch failure'), 'failed'),
                                 (subprocess.CompletedProcess([], 0, '', ''), 'not confirmed')]:
            with patch.dict(os.environ, self.env), patch.object(agents, 'window_command', return_value=['fake']), \
                 patch.object(agents.subprocess, 'run', return_value=result):
                with self.assertRaisesRegex(agents.LaunchError, expected):
                    agents.open_window(plan, timeout=.01)

    def test_window_child_lock_refusal_is_reported(self):
        plan = agents.build_plan(self.entry, None, 'new')
        requested = []
        def command(_plan, request):
            requested.append(request)
            return ['fake']
        real_run = subprocess.run
        def transport(cmd, **kwargs):
            # Another launch can acquire the folder after the menu precheck.
            with agents.session_lock(plan, self.base / 'cache/research-agent-launcher'):
                result = real_run([sys.executable, str(SCRIPTS / 'agents.py'), '--window-request', str(requested[-1])],
                                  env=self.env, capture_output=True, text=True, timeout=5)
                self.assertEqual(result.returncode, 2)
            return subprocess.CompletedProcess(cmd, 0, '', '')
        with patch.dict(os.environ, self.env), patch.object(agents, 'window_command', side_effect=command), \
             patch.object(agents.subprocess, 'run', side_effect=transport):
            with self.assertRaisesRegex(agents.LaunchError, 'already owns'):
                agents.open_window(plan)
        self.assertFalse(self.capture.exists())

    def test_default_menu_returns_after_launch_and_error(self):
        choices = ['fixture', '', '1', 'fixture', 'c', '2', 'q']
        with patch.object(agents.sys.stdin, 'isatty', return_value=True), \
             patch('builtins.input', side_effect=choices), patch.object(agents, 'validate_plan'), \
             patch.object(agents, 'execute') as inline, \
             patch.object(agents, 'open_window', side_effect=[agents.LaunchError('window failed'), 0]) as windows, \
             contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(agents.main(['--config', str(self.config)]), 0)
        self.assertEqual(windows.call_count, 2)
        inline.assert_not_called()

    def test_missing_windows_transport_refuses_without_inline_fallback(self):
        plan = agents.build_plan(self.entry, None, 'new')
        with patch.object(agents.shutil, 'which', return_value=None):
            with self.assertRaisesRegex(agents.LaunchError, '--same-window'):
                agents.window_command(plan, self.base / 'request.json')


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='launcher-install-test-')
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / 'repository with spaces'
        (self.root / 'scripts').mkdir(parents=True)
        (self.root / 'scripts/agents.py').write_text('fixture')
        (self.root / 'scripts/agents.json').write_text('{}')
        self.home = self.base / 'home'
        self.desktop = self.base / 'desktop'
        self.desktop.mkdir()

    def plans(self):
        return installer.shortcut_files(self.root, self.home, self.desktop, 'Ubuntu', 'willi')

    def test_gui_upgrade_backs_up_only_the_known_menu_and_is_idempotent(self):
        for suffix in ('.py', '.ps1'):
            (self.root / ('scripts/agents_gui' + suffix)).write_text('fixture')
        old = self.plans()
        new = installer.shortcut_files(self.root, self.home, self.desktop, 'Ubuntu', 'willi', gui=True)
        previous = {old[1][0]: old[1][1]}
        with contextlib.redirect_stdout(io.StringIO()):
            installer.install(old)
            installer.install(new, previous)
            installer.install(new, previous)
        self.assertEqual((self.desktop / 'Agent Launcher.cmd.terminal-menu.bak').read_bytes(), old[1][1].encode())
        encoded = new[1][1].split('-EncodedCommand ')[1].split('\r\n')[0]
        decoded = base64.b64decode(encoded).decode('utf-16le')
        self.assertIn('agents_gui.py', decoded)
        self.assertIn('CreateNoWindow=$true', decoded)
        self.assertIn('RedirectStandardOutput=$true', decoded)
        self.assertIn('WaitForExit()', decoded)
        new[1][0].write_text('User customization')
        with self.assertRaisesRegex(ValueError, 'Existing file differs'):
            installer.install(new, previous)
        self.assertEqual(new[1][0].read_text(), 'User customization')

    def test_portable_wrapper_and_desktop_contents_and_idempotent_install(self):
        files = self.plans()
        self.assertIn('"$@"', files[0][1])
        self.assertIn('"Ubuntu" -u "willi"', files[1][1])
        self.assertIn("'" + str(self.root / 'scripts/agents.py') + "'", files[1][1])
        subprocess.run(['sh', '-n'], input=files[0][1], text=True, check=True)
        with contextlib.redirect_stdout(io.StringIO()):
            installer.install(files)
            installer.install(files)
        for path, text, _ in files: self.assertEqual(path.read_bytes(), text.encode())
        self.assertTrue(os.access(files[0][0], os.X_OK))

    def test_all_conflicts_checked_before_any_write(self):
        files = self.plans()
        files[1][0].write_text('user custom shortcut')
        with self.assertRaisesRegex(ValueError, 'Existing file differs'):
            installer.install(files)
        self.assertFalse(files[0][0].exists())
        self.assertEqual(files[1][0].read_text(), 'user custom shortcut')

    def test_symlink_collision_and_missing_desktop_refused(self):
        files = self.plans()
        files[1][0].symlink_to(self.base / 'missing-target')
        with self.assertRaisesRegex(ValueError, 'symlink'): installer.preflight(files)
        with self.assertRaisesRegex(ValueError, 'does not exist'):
            installer.shortcut_files(self.root, self.home, self.base / 'absent', 'Ubuntu', 'willi')

    def test_dry_run_writes_nothing(self):
        with patch.object(installer, 'ROOT', self.root), patch.object(installer.Path, 'home', return_value=self.home), \
             patch.object(installer.getpass, 'getuser', return_value='willi'), \
             contextlib.redirect_stdout(io.StringIO()):
            rc = installer.main(['--desktop', str(self.desktop), '--distro', 'Ubuntu', '--dry-run'])
        self.assertEqual(rc, 0)
        self.assertFalse(self.home.exists())
        self.assertEqual(list(self.desktop.iterdir()), [])


if __name__ == '__main__':
    unittest.main()

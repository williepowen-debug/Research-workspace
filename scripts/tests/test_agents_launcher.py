"""Behavior tests for the personal launcher; never invoke a real agent/model."""
import contextlib
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
        return subprocess.run([sys.executable, str(SCRIPTS / 'agents.py'), '--config', str(self.config), *args],
                              env=env or self.env, text=True, capture_output=True, timeout=15)

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
            self.assertIn('--channels', walter.argv)
            self.assertIn('plugin:telegram@claude-plugins-official', walter.argv)
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
             patch('builtins.input', side_effect=['fixture', 'c', '2']), \
             patch.object(agents, 'validate_plan'), patch.object(agents, 'execute', return_value=0) as run, \
             contextlib.redirect_stdout(io.StringIO()):
            rc = agents.main(['--config', str(self.config)])
        self.assertEqual(rc, 0)
        self.assertEqual(run.call_args.args[0].runtime, 'claude')
        self.assertEqual(run.call_args.args[0].action, 'resume')

    def test_group_menu_and_cancellation(self):
        for answers, expected_calls in [(['1', '1', '', '1'], 1), (['q'], 0), (['fixture', 'q'], 0)]:
            with patch.object(agents.sys.stdin, 'isatty', return_value=True), \
                 patch('builtins.input', side_effect=answers), patch.object(agents, 'validate_plan'), \
                 patch.object(agents, 'execute', return_value=0) as run, contextlib.redirect_stdout(io.StringIO()):
                rc = agents.main(['--config', str(self.config)])
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
                                 'fixture', '--new'], env=env, stdout=subprocess.PIPE,
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

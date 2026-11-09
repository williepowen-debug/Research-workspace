"""WQ-654: removing a completed queue must not re-enable boot profile reads."""
import datetime as dt
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'sweeps_due.py'


class InvocationTests(unittest.TestCase):
    def run_case(self, rows, legacy_flag=False):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            script = root / 'sweeps_due.py'
            script.write_bytes(SCRIPT.read_bytes())
            # If the old boot child is restored, this prints a sentinel and rc2.
            (root / 'profile_clock_check.py').write_text(
                "print('UNEXPECTED-PROFILE-BOOT-READ'); raise SystemExit(2)\n")
            pb = root / 'playbook.md'
            pb.write_text('fixture')
            registry = root / 'registry.tsv'
            registry.write_text('task\tcadence_days\tlast_run\tplaybook\tstatus\tresolve_by\tlast_findings\n'
                                + ''.join(row.format(pb=pb) + '\n' for row in rows))
            args = [sys.executable, str(script), '--registry', str(registry), '--no-live-checks']
            if legacy_flag:
                args.append('--no-profile-clock')
            return subprocess.run(args, capture_output=True, text=True, check=False)

    def test_retired_overdue_queue_does_not_run_profile_child(self):
        row = 'Completed queue\t21\t2026-01-01\t{pb}\tretired\t\tdone'
        for legacy in (False, True):
            result = self.run_case([row], legacy)
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertIn('none due', result.stdout)
            self.assertNotIn('PROFILE', result.stdout)

    def test_unrelated_active_cadence_still_fires(self):
        result = self.run_case(['Other sweep\t1\t2020-01-01\t{pb}\tactive\t\tx'])
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn('DUE: Other sweep', result.stdout)
        self.assertNotIn('PROFILE', result.stdout)

    def test_malformed_registry_still_refuses(self):
        result = self.run_case(['Broken\tbad\t2020-01-01\t{pb}\tactive\t\tx'])
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertIn('un-parseable', result.stdout)


if __name__ == '__main__':
    unittest.main()

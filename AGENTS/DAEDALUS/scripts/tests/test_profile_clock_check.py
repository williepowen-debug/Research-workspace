#!/usr/bin/env python3
"""Production acceptance snapshots plus deterministic rc/ambiguity regressions."""
import contextlib
import datetime as dt
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('profile_clock', HERE.parent/'profile_clock_check.py')
clock = importlib.util.module_from_spec(spec)
spec.loader.exec_module(clock)
FIXTURES = HERE/'fixtures/profile_clock'


class ProfileClockTests(unittest.TestCase):
    def run_profiles(self, files, quiet=False):
        with tempfile.TemporaryDirectory() as tmp:
            for name, text in files.items(): (Path(tmp)/name).write_text(text)
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                rc = clock.main(['--profiles',tmp,'--as-of','2026-09-08'] + (['--quiet'] if quiet else []))
            return rc, output.getvalue()

    def fixture(self, name): return (FIXTURES/f'{name}.md').read_text()

    def test_frozen_production_provenance(self):
        for row in json.loads((FIXTURES/'manifest.json').read_text())['files']:
            self.assertEqual(hashlib.sha256((FIXTURES/Path(row['fixture']).name).read_bytes()).hexdigest(),row['sha256'])

    def test_real_clean_fert_receipt_and_checkpoint_do_not_redate(self):
        rc, output = self.run_profiles({'FERT.md':self.fixture('FERT')})
        self.assertEqual(rc,0); self.assertIn('body 2026-09-05, age 3d',output)

    def test_real_defect_brock_alerts_from_build_not_partial_delta(self):
        rc, output = self.run_profiles({'BROCK.md':self.fixture('BROCK')})
        self.assertEqual(rc,1); self.assertIn('72d > 45d',output)

    def test_real_osprey_receipt_cannot_clear_owner_relative_clock(self):
        rc, output = self.run_profiles({'OSPREY.md':self.fixture('OSPREY')})
        self.assertEqual(rc,2); self.assertIn('body 2026-08-07, age 32d',output)
        self.assertIn('STATUS-stamp-relative',output); self.assertNotIn('PROFILE-CLOCK 0:',output)

    def test_real_checkpoint_forms_and_metadata_after_delta_heading(self):
        expected = {'BRENT':('2026-09-07',45),'CORAL':('2026-09-05',30),'CARL':('2026-07-10',45)}
        for name,(vintage,days) in expected.items():
            with self.subTest(name=name):
                self.assertEqual(str(clock.vintage_of(self.fixture(name))[0]),vintage)
                self.assertEqual(clock.clock_of(self.fixture(name))[0],days)

    def test_unknown_vintage_has_no_git_fallback(self):
        rc,output=self.run_profiles({'TEST.md':'# Receipt 2026-09-08\n**Staleness:** >21d'})
        self.assertEqual(rc,2); self.assertIn('no declared body vintage',output)

    def test_future_vintage_malformed_floor_and_unreadable_encoding_fail(self):
        cases=['**Profile vintage:** 2026-10-01\n**Staleness:** >21d',
               '**Built:** 2026-09-01\n**Staleness:** hard floor 2026-09-99',
               '**Built:** 2026-09-01\n**Staleness:** hard floor tomorrow',
               '**Built:** 2026-09-01\n**Day clock:** twenty-one days']
        for text in cases:
            self.assertEqual(self.run_profiles({'TEST.md':text})[0],2)
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp)/'TEST.md').write_bytes(b'\xff')
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(clock.main(['--profiles',tmp]),2)

    def test_cannot_does_not_hide_real_alert_even_quiet(self):
        rc,output=self.run_profiles({'BROCK.md':self.fixture('BROCK'),'BAD.md':'# No metadata'},True)
        self.assertEqual(rc,2); self.assertIn('ALERT BROCK:',output)
        self.assertIn('2 profile(s) attempted',output)

    def test_boundary_strict_greater_and_floor(self):
        self.assertEqual(self.run_profiles({'TEST.md':'**Built:** 2026-08-18\n**Staleness:** >21d'})[0],0)
        self.assertEqual(self.run_profiles({'TEST.md':'**Built:** 2026-08-17\n**Staleness:** >21d'})[0],1)
        self.assertEqual(self.run_profiles({'TEST.md':'**Built:** 2026-08-17\n**Staleness:** hard floor 2026-09-08'})[0],0)
        self.assertEqual(self.run_profiles({'TEST.md':'**Built:** 2026-08-17\n**Staleness:** hard floor 2026-09-07'})[0],1)

    def test_explicit_vintage_and_partial_scope(self):
        self.assertEqual(clock.vintage_of('**Built:** 2026-07-01 · **Refreshed (delta):** 2026-09-08')[0],dt.date(2026,7,1))
        self.assertEqual(clock.vintage_of('**Built:** 2026-07-01 · **Refreshed:** 2026-09-08 (delta re-read)')[0],dt.date(2026,7,1))
        partial='**Body:** 2026-07-01, **§1 refreshed 2026-09-05**'
        self.assertEqual(self.run_profiles({'TEST.md':partial})[0],2)
        self.assertEqual(clock.vintage_of(partial+'\n**Profile vintage:** 2026-09-05')[0],dt.date(2026,9,5))
        self.assertEqual(self.run_profiles({'TEST.md':'**Profile vintage:** 2026-09-05\n**Body vintage:** 2026-09-04'})[0],2)

    def test_companions_excluded_visibly_and_empty_not_clean(self):
        rc,output=self.run_profiles({'FERT.md':self.fixture('FERT'),'FERT_READER_REPORT.md':'**Staleness:** >1d'})
        self.assertEqual(rc,0); self.assertIn('Excluded non-profile filenames: FERT_READER_REPORT.md',output)
        self.assertEqual(self.run_profiles({})[0],2)

    def test_missing_directory_and_undated_perimeter(self):
        with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(clock.main(['--profiles',str(Path(tmp)/'missing')]),2)
        rc,output=self.run_profiles({'TEST.md':'**Built:** 2026-08-01\n**Staleness:** after next session'},True)
        self.assertEqual(rc,0); self.assertIn('NO-DATED-CLOCK (agent-judged): TEST:',output)
        self.assertIn('content/undated profiles NOT certified',output)


if __name__ == '__main__': unittest.main(verbosity=2)

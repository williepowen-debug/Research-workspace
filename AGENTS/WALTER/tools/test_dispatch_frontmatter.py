"""Frozen fixtures for header/body confusion and malformed dispatch metadata."""
import datetime as dt
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import walter_doctor as doctor

class DispatchFrontmatter(unittest.TestCase):
    def check_text(self, text, filename='SIG-W-20261016-001-fixture.md'):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp)
            (path / filename).write_text(text)
            with patch.object(doctor, 'BOARD', path), patch.object(doctor, 'TODAY', dt.date(2026,10,16)):
                return doctor.check_dispatch_frontmatter()
    def test_body_cannot_fill_missing_header(self):
        out=self.check_text('---\ninfo: [RED]\n---\naction: [RED]\ndispatched: 2026-10-16T17:00:00Z\n')
        self.assertEqual(sum(s==doctor.MED for s,_ in out),2)
    def test_quoted_recipients_and_utc_are_valid(self):
        out=self.check_text('---\naction: ["RED", "CARL"]\ndispatched: "2026-10-16T17:00:00Z"\n---\nbody')
        self.assertEqual(out[0][0],doctor.INFO)
    def test_explicit_empty_action_list_is_valid(self):
        self.assertEqual(self.check_text('---\naction: []\ndispatched: 2026-10-16T17:00:00Z\n---\n')[0][0],doctor.INFO)
    def test_invalid_clock_and_duplicate_key_fail(self):
        out=self.check_text('---\naction: [RED]\naction: [CARL]\ndispatched: 2026-10-16T25:00:00Z\n---\n')
        self.assertEqual(sum(s==doctor.MED for s,_ in out),2)
    def test_local_time_and_empty_action_fail(self):
        out=self.check_text('---\naction:\ndispatched: 2026-10-16T17:00:00-04:00\n---\n')
        self.assertEqual(sum(s==doctor.MED for s,_ in out),2)
    def test_unterminated_header_fails(self):
        self.assertEqual(self.check_text('---\naction: [RED]\n')[0][0],doctor.MED)
    def test_old_archive_not_retrograded(self):
        self.assertEqual(self.check_text('legacy text','SIG-W-20260401-001-old.md')[0][0],doctor.INFO)

if __name__=='__main__': unittest.main()

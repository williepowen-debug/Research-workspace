"""Exercise stale/missing evidence and conditional read failures in isolated fixtures."""
from datetime import date
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from signal_read_check import REGISTRY, validate

ID = 'SIG-W-20260619-008'

class CompanionCheck(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name)
        self.row = dict(status='reviewed', reviewed_on='2026-09-15', review_due='2026-09-30',
                        source=f'BOARD/{ID}-original.md', companion=f'AGENTS/WALTER/reading/{ID}.md',
                        review='AGENTS/WALTER/research/review.md')
        for key, text in [('source', f'---\nsignal_id: {ID}\n---\nsource caveat\n'),
                          ('companion', 'reviewed companion\n'), ('review', 'Verdict: APPROVED\n')]:
            path = self.repo / self.row[key]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
            self.row[key+'_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest()
        self.save()

    def save(self):
        path = self.repo / REGISTRY
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({ID: self.row}))

    def check(self, **kwargs):
        return validate(ID, self.repo, kwargs.get('today', date(2026,9,15)), kwargs.get('byte_budget', 1000))

    def test_valid(self):
        self.assertEqual(self.check()[1], b'reviewed companion\n')

    def test_changed_source_companion_or_review(self):
        for key in ('source','companion','review'):
            with self.subTest(key=key):
                path = self.repo / self.row[key]
                original = path.read_bytes()
                path.write_bytes(original+b'changed')
                with self.assertRaises(ValueError): self.check()
                path.write_bytes(original)

    def test_invalid_utf8(self):
        path = self.repo / self.row['companion']; path.write_bytes(bytes([255]))
        self.row['companion_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest(); self.save()
        with self.assertRaises(ValueError): self.check()

    def test_missing_source(self):
        (self.repo / self.row['source']).unlink()
        with self.assertRaises(OSError): self.check()

    def test_due_and_future(self):
        for day in (date(2026,9,30),date(2026,9,14)):
            with self.assertRaises(ValueError): self.check(today=day)

    def test_unapproved_even_with_matching_hash(self):
        path = self.repo / self.row['review']; path.write_text('Verdict: PENDING\n')
        self.row['review_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest(); self.save()
        with self.assertRaises(ValueError): self.check()

    def test_budget(self):
        with self.assertRaises(ValueError): self.check(byte_budget=10)

    def test_missing_id(self):
        with self.assertRaises(KeyError): validate('SIG-W-20260619-009',self.repo,date(2026,9,15),1000)

    def test_escaped_path(self):
        self.row['source'] = 'BOARD/../other.md'; self.save()
        with self.assertRaises(ValueError): self.check()

    def test_wrong_source_id(self):
        path = self.repo / self.row['source']; path.write_text('signal_id: SIG-W-20260619-009\n')
        self.row['source_sha256'] = hashlib.sha256(path.read_bytes()).hexdigest(); self.save()
        with self.assertRaises(ValueError): self.check()

if __name__ == '__main__': unittest.main()

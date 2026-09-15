"""Independent fixtures for declared-basis freshness and staged archive conservation.

All writes and Git operations occur in disposable temporary repositories.
"""
import hashlib
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import archive_pair_check
import boot_basis_check
import walter_doctor as doctor


class CorrectionTargets(unittest.TestCase):
    def test_quoted_and_legacy_targets_keep_resolution_checks(self):
        with tempfile.TemporaryDirectory() as temporary:
            board = Path(temporary)
            (board / 'SIG-W-20260801-001-original.md').write_text('---\nsignal_type: catalyst\n---\n')
            correction = board / 'SIG-W-20260915-001-correction.md'
            cases = [
                ('"EXTERNAL: note with \\"quotation\\""', True),
                ("'EXTERNAL: owner''s note'", True),
                ('EXTERNAL: legacy note', True),
                ('"SELF"', True),
                ('"SIG-W-20260801-001"', True),
                ('"EXTERNAL: "', False),
                ('"SIG-W-20260801-999"', False),
                ('"EXTERNAL: invalid \\q escape"', False),
            ]
            for value, valid in cases:
                with self.subTest(value=value):
                    correction.write_text('---\nsignal_id: SIG-W-20260915-001\n'
                                          f'signal_type: correction\ncorrects: {value}\n---\n')
                    with patch.object(doctor, 'BOARD', board):
                        notices = doctor.check_correction_target_declared()
                    self.assertEqual(all(level == doctor.INFO for level, _ in notices), valid)


class BacklogNotices(unittest.TestCase):
    def test_consumed_and_archive_notices_survive_together(self):
        with tempfile.TemporaryDirectory() as temporary:
            paths = [Path(temporary) / f'SIG-W-20260801-00{i}.md' for i in (1, 2, 3)]
            for path in paths:
                path.write_text('fixture\n')
            files = [(p, 'CARL' if i < 2 else 'MARCO', str(p))
                     for i, p in enumerate(paths)]
            with patch.object(doctor, '_handoff_files', return_value=files), \
                 patch.object(doctor, '_origin_ref', return_value='fixture'), \
                 patch.object(doctor, '_sync_state', return_value='on_origin'), \
                 patch.object(doctor, '_delivery_routed_dates', return_value={}), \
                 patch.object(doctor, '_delivery_routed_dates_by_path', return_value={}), \
                 patch.object(doctor, '_delivery_roles', return_value={}), \
                 patch.object(doctor, '_age_days', return_value=10), \
                 patch.object(doctor, '_board_log_has', side_effect=[True, False, False]), \
                 patch.object(doctor, '_handoff_role', side_effect=['INFO', 'ACTION']), \
                 patch.object(doctor, 'PULL_COMPLETE', {'CARL'}):
                notices = '\n'.join(message for _, message in doctor.check_delivered_but_unconsumed())
            self.assertIn('CONSUMED but never filed', notices)
            self.assertIn('ARCHIVE not consume: CARL 1', notices)
            self.assertIn('1 unconsumed >', notices)
            self.assertIn('3 on mtime across the full delivered-file scan', notices)
            self.assertIn('not the aged-warning denominator', notices)


class BasisGuard(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.manifest = self.repo / 'PROME/registry/READS.tsv'
        self.record = self.repo / 'AGENTS/WALTER/registry/boot_basis_hashes.json'
        self.manifest.parent.mkdir(parents=True)
        self.record.parent.mkdir(parents=True)
        self.source = self.repo / 'AGENTS/WALTER/boot.md'
        self.source.write_text('read the current source\n')
        self.relative = self.source.relative_to(self.repo).as_posix()
        self.manifest.write_text(f'BASIS\tWALTER\t{self.relative}\tboot-defining\n')
        self.hashes = {self.relative: hashlib.sha256(self.source.read_bytes()).hexdigest()}
        self.record.write_text(json.dumps(self.hashes))

    def test_matching_bytes_pass(self):
        self.assertEqual(boot_basis_check.check(self.repo), ([], 1))

    def test_changed_bytes_fail_even_with_same_mtime(self):
        stat = self.source.stat()
        self.source.write_text('read a DIFFERENT source\n')
        os.utime(self.source, ns=(stat.st_atime_ns, stat.st_mtime_ns))
        failures, count = boot_basis_check.check(self.repo)
        self.assertEqual(count, 1)
        self.assertTrue(any(self.relative in message for message in failures))

    def test_missing_source_fails(self):
        self.source.unlink()
        self.assertTrue(boot_basis_check.check(self.repo)[0])

    def test_added_and_removed_basis_require_review(self):
        for manifest in [self.manifest.read_text() + 'BASIS\tWALTER\tnew.md\tboot-defining\n', '']:
            with self.subTest(manifest=manifest):
                self.manifest.write_text(manifest)
                self.assertTrue(boot_basis_check.check(self.repo)[0])

    def test_foreign_reader_does_not_expand_walter_basis(self):
        self.manifest.write_text(self.manifest.read_text() + 'BASIS\tOTHER\tforeign.md\tboot-defining\n')
        self.assertEqual(boot_basis_check.check(self.repo), ([], 1))

    def test_missing_or_invalid_hash_record_fails_explicitly(self):
        for content in ['{broken', '[]', 'null', '42',
                        json.dumps({self.relative: None}),
                        json.dumps({self.relative: 'not-a-sha256'})]:
            with self.subTest(content=content):
                self.record.write_text(content)
                self.assertTrue(boot_basis_check.check(self.repo)[0])
        self.record.unlink()
        self.assertTrue(boot_basis_check.check(self.repo)[0])

    def test_missing_manifest_fails(self):
        self.manifest.unlink()
        self.assertTrue(boot_basis_check.check(self.repo)[0])


class LaterConsumptionReceipt(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.dest = 'AGENTS/WALTER/inbox/processed/packet.md'
        target = self.repo / self.dest
        target.parent.mkdir(parents=True)
        target.write_text('original packet')
        self.ledger = target.parent / '.consumed.tsv'
        self.evidence = 'AGENTS/WALTER/research/review.md'
        evidence = self.repo / self.evidence
        evidence.parent.mkdir(parents=True)
        evidence.write_text('Packet reviewed; its integration is documented here.')
        self.today = dt.datetime.now(dt.timezone.utc).date()
        self.moved = '2026-08-28'

    def write_receipt(self, *, stamp=None, filename='packet.md', owner='WALTER', note=None):
        if note is None:
            note = f'Retrospective review; evidence: {self.evidence}'
        self.ledger.write_text(f'{stamp or self.today.isoformat()}\t{filename}\t{owner}\t{note}\n')

    def verdict(self):
        with patch.object(doctor, 'REPO', self.repo):
            return doctor._later_consume_receipt('WALTER', self.dest, self.moved)

    def test_exact_evidence_backed_receipt_accepts_owner_forms(self):
        for owner in ['WALTER', 'consume:WALTER']:
            self.write_receipt(owner=owner)
            self.assertTrue(self.verdict())

    def test_wrong_filename_or_owner_cannot_clear(self):
        for options in [dict(filename='packet-alias.md'), dict(owner='OTHER')]:
            self.write_receipt(**options)
            self.assertFalse(self.verdict())

    def test_missing_or_unsafe_evidence_cannot_clear(self):
        for note in ['reviewed', 'evidence: missing.md', 'evidence: ../outside.md',
                     f'evidence: {self.repo / self.evidence}']:
            self.write_receipt(note=note)
            self.assertFalse(self.verdict())
        self.ledger.unlink()
        self.assertFalse(self.verdict())

    def test_invalid_future_and_pre_move_dates_cannot_clear(self):
        for stamp in [(self.today + dt.timedelta(days=1)).isoformat(),
                      '2026-08-27', 'not-a-date', '2026-09-15NOT-A-DATE']:
            with self.subTest(stamp=stamp):
                self.write_receipt(stamp=stamp)
                self.assertFalse(self.verdict())

    def test_production_check_resolves_only_exact_later_receipt(self):
        epoch = int(dt.datetime(2026, 8, 28, tzinfo=dt.timezone.utc).timestamp())
        def git(*args):
            if args[:2] == ('log', '--since=90.days'):
                return 'fixturecommit'
            if args[:2] == ('log', '-1'):
                return f'{epoch}\x1fWALTER: file packet without consumption declaration'
            if args[0] == 'diff-tree':
                return f'R100\tAGENTS/WALTER/inbox/packet.md\t{self.dest}'
            self.fail(f'unexpected git invocation: {args}')
        with patch.object(doctor, 'REPO', self.repo), patch.object(doctor, '_git', side_effect=git):
            before = doctor.check_filed_vs_consumed()
            self.assertTrue(any('FILED not CONSUMED' in text for _, text in before))
            self.write_receipt(owner='OTHER')
            wrong = doctor.check_filed_vs_consumed()
            self.assertTrue(any('FILED not CONSUMED' in text for _, text in wrong))
            self.write_receipt()
            after = doctor.check_filed_vs_consumed()
            self.assertTrue(any('1 declared-consumed' in text for _, text in after))
            self.assertFalse(any('FILED not CONSUMED' in text for _, text in after))


class ArchiveGuard(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.git('init', '-q')
        self.git('config', 'user.name', 'Fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.put('AGENTS/WALTER/current.md', 'original bytes\n')
        self.put('AGENTS/WALTER/duplicate.md', 'original bytes\n')
        self.put('AGENTS/OTHER/current.md', 'foreign bytes\n')
        self.git('add', 'AGENTS/WALTER/current.md', 'AGENTS/WALTER/duplicate.md', 'AGENTS/OTHER/current.md')
        self.git('commit', '-qm', 'fixture baseline')

    def git(self, *args):
        return subprocess.check_output(['git', *args], cwd=self.repo, stderr=subprocess.PIPE)

    def put(self, path, text):
        dest = self.repo / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text)

    def test_exact_move_passes(self):
        (self.repo / 'AGENTS/WALTER/archive').mkdir()
        self.git('mv', 'AGENTS/WALTER/current.md', 'AGENTS/WALTER/archive/old.md')
        self.assertEqual(archive_pair_check.check(self.repo), ([], 1))

    def test_unpaired_deletion_fails(self):
        self.git('rm', '-q', 'AGENTS/WALTER/current.md')
        self.assertEqual(archive_pair_check.check(self.repo), (['AGENTS/WALTER/current.md'], 1))

    def test_edited_move_requires_review(self):
        self.git('mv', 'AGENTS/WALTER/current.md', 'AGENTS/WALTER/renamed.md')
        self.put('AGENTS/WALTER/renamed.md', 'edited bytes\n')
        self.git('add', 'AGENTS/WALTER/renamed.md')
        self.assertEqual(archive_pair_check.check(self.repo), (['AGENTS/WALTER/current.md'], 1))

    def test_foreign_deletion_is_outside_perimeter(self):
        self.git('rm', '-q', 'AGENTS/OTHER/current.md')
        self.assertEqual(archive_pair_check.check(self.repo), ([], 0))

    def test_foreign_addition_cannot_cover_walter_deletion(self):
        self.git('mv', 'AGENTS/WALTER/current.md', 'AGENTS/OTHER/moved.md')
        self.assertEqual(archive_pair_check.check(self.repo), (['AGENTS/WALTER/current.md'], 1))

    def test_one_addition_cannot_cover_two_deletions(self):
        self.git('rm', '-q', 'AGENTS/WALTER/current.md', 'AGENTS/WALTER/duplicate.md')
        self.put('AGENTS/WALTER/archive.md', 'original bytes\n')
        self.git('add', 'AGENTS/WALTER/archive.md')
        failures, count = archive_pair_check.check(self.repo)
        self.assertEqual(count, 2)
        self.assertEqual(len(failures), 1)

    def test_unstaged_deletion_is_not_a_staged_deletion(self):
        (self.repo / 'AGENTS/WALTER/current.md').unlink()
        self.assertEqual(archive_pair_check.check(self.repo), ([], 0))


if __name__ == '__main__':
    unittest.main()

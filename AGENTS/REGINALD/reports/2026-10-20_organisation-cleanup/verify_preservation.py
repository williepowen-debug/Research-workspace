#!/usr/bin/env python3
"""Read-only preservation checks for this bounded documentation cleanup."""
import csv
import hashlib
import json
from pathlib import Path
import subprocess
import zlib

ROOT = Path(__file__).resolve().parents[4]
DESK = ROOT / 'AGENTS/REGINALD'
HERE = Path(__file__).resolve().parent
BASELINE = '2b667e627'


def between(text, start, end):
    return text[text.index(start):text.index(end)]


def main():
    manifest = json.loads((HERE / 'manifest.json').read_text())
    originals = {}
    count = 0
    for entry in manifest['sources']:
        archive = (ROOT / entry['archive']).read_bytes()
        parts = []
        next_line = 1
        for block in entry['blocks']:
            assert block['line_start'] == next_line
            next_line = block['line_end'] + 1
            raw = archive[block['offset']:block['offset'] + block['bytes']]
            assert hashlib.sha256(raw).hexdigest() == block['sha256']
            assert f'{zlib.crc32(raw):08x}' == block['crc32']
            parts.append(raw)
            count += 1
        rebuilt = b''.join(parts)
        assert len(rebuilt) == entry['before_bytes']
        assert hashlib.sha256(rebuilt).hexdigest() == entry['before_sha256']
        baseline = subprocess.check_output(
            ['git', 'show', f"{BASELINE}:{entry['source']}"], cwd=ROOT)
        assert rebuilt == baseline, entry['source']
        originals[Path(entry['source']).name] = rebuilt.decode()
        if 'after_sha256' in entry:
            current = (ROOT / entry['source']).read_bytes()
            assert len(current) == entry['after_bytes']
            assert hashlib.sha256(current).hexdigest() == entry['after_sha256']
        else:
            raise AssertionError(f"Final source hash not recorded: {entry['source']}")
    old = originals['STATUS.md']
    new = (DESK / 'STATUS.md').read_text()
    for start, end in [
        ('## EXIT RULES', '## ⚠️ THRESHOLD STATUS'),
        ('## CONVERGENCE MATRIX', '## KEY CATALYSTS'),
        ('## CROSS-AGENT TRIGGERS', '## FRAMEWORKS'),
        ('| Metric | Threshold | Current | Note |', '## BOTTOM LINE'),
    ]:
        assert between(old, start, end) == between(new, start, end), start
    assert between(originals['MEMORY.md'], '### NEXT SESSION', '**CARRIED LESSONS') == between(
        (DESK / 'MEMORY.md').read_text(), '### NEXT SESSION', '**CARRIED LESSONS')
    old_charter = originals['CLAUDE.md']
    new_charter = (DESK / 'CLAUDE.md').read_text()
    old_hidden = between(old_charter, '## HIDDEN CRE METHODOLOGY', '## BANK WATCHLIST')
    new_hidden = between(new_charter, '## HIDDEN CRE METHODOLOGY', '## BANK WATCHLIST')
    for n in range(1, 6):
        line = next(line for line in old_hidden.splitlines() if line.startswith(f'{n}. '))
        assert line in new_hidden, f'Hidden CRE method rule {n}'
    def predicates(text):
        table = between(text, '## KEY THRESHOLDS', '## FILES')
        return [tuple(x.strip() for x in line.split('|')[1:3])
                for line in table.splitlines() if line.startswith('|')]
    assert predicates(old_charter) == predicates(new_charter)
    new_nexus = (DESK / 'NEXUS_BRIEF.md').read_text()
    old_nexus = originals['NEXUS_BRIEF.md']
    old_sending = between(old_nexus, '| To | Signal |', '**WAITING FOR:**').rstrip()
    assert old_sending in new_nexus
    assert between(old_nexus, '## CALIBRATION', '## NEXT DECISION POINT') in new_nexus
    status_head = subprocess.check_output(
        ['git', 'log', '-1', '--format=%h', '--', 'AGENTS/REGINALD/STATUS.md'], cwd=ROOT
    ).decode().strip()
    assert f'STATUS commit: {status_head}' in new_nexus
    assert '__STATUS_HASH__' not in new_nexus
    changed = subprocess.check_output(
        ['git', 'diff', '--name-status', BASELINE, '--', 'AGENTS/REGINALD/'], cwd=ROOT
    ).decode().splitlines()
    allowed = {'AGENTS/REGINALD/' + n for n in originals}
    for line in changed:
        state, path = line.split('\t', 1)
        assert state != 'D', f'Deletion: {path}'
        if state != 'A':
            assert path in allowed, f'Unexpected tracked change: {line}'
    tracked = subprocess.check_output(
        ['git', 'ls-tree', '-r', '--name-only', BASELINE, '--', 'AGENTS/REGINALD/'], cwd=ROOT
    ).decode().splitlines()
    assert all((ROOT / path).exists() for path in tracked), 'Original tracked file missing'
    with (HERE / 'READS.proposed.tsv').open() as stream:
        rows = list(csv.DictReader(stream, delimiter='\t'))
    att = [r for r in rows if r['row_kind'] == 'ATTESTATION']
    assert len(att) == 1 and att[0]['declared_by'] == 'REGINALD'
    assert (DESK / 'CLAUDE.md').stat().st_size < 22785
    print(f'PASS: {len(originals)} originals / {count} contiguous payloads reconstructed exactly; CRC/SHA verified.')
    print('PASS: protected STATUS sections, MEMORY next steps, five hidden-CRE rules and threshold predicates preserved.')
    print('PASS: full prior NEXUS SENDING and CALIBRATION preserved; live STATUS pin matches.')
    print('PASS: no tracked deletions or existing evidence/ledger/script changes; charter below rotation stop.')


if __name__ == '__main__':
    main()

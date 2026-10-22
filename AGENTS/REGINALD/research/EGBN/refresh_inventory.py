"""Refresh the EGBN research-folder snapshot and manifest (REGINALD, added 2026-10-22).

Run from the repository root:
  .venv/bin/python3 AGENTS/REGINALD/research/EGBN/refresh_inventory.py --check   # prove the extractor reproduces unchanged extracts; no writes
  .venv/bin/python3 AGENTS/REGINALD/research/EGBN/refresh_inventory.py --apply   # refresh changed copies/extracts + register NEW_ENTRIES

Rules kept from the 2026-10-20 capture (README "Where to save future work"):
- Originals stay authoritative in their own homes. A COPY is byte-identical; a workbook EXTRACT keeps the leading
  '#' preamble, the header row, and every complete row with standalone EGBN in any cell, plus original line numbers.
- Files whose ONLY home is this folder are registered as kind ORIGINAL (source == destination).
- Refresh only re-copies when the original changed; earlier capture timestamps are replaced by this refresh's, and the
  manifest keeps a refresh_log entry. No file outside this folder is written.
"""
from pathlib import Path
import datetime
import hashlib
import json
import re
import shutil
import subprocess
import sys

HUB = Path(__file__).resolve().parent
ROOT = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], cwd=HUB, text=True).strip())
REL_HUB = HUB.relative_to(ROOT).as_posix()
EGBN = re.compile(r'\bEGBN\b')

# (kind, category, source relative to ROOT, destination relative to HUB)
NEW_ENTRIES = [
    ('COPY', 'REGINALD_EGBN_REPORT', 'AGENTS/REGINALD/reports/2026-10-22_EGBN_Q4_maturity_wall.md', 'reports/2026-10-22_EGBN_Q4_maturity_wall.md'),
    ('COPY', 'MULTIBANK_CONTEXT', 'AGENTS/REGINALD/reports/2026-10-22_catchup/REPORT.md', 'context/2026-10-22_catchup_REPORT.md'),
    ('COPY', 'MULTIBANK_CONTEXT', 'AGENTS/REGINALD/reports/2026-10-22_appraisal-discount_cohort_test.md', 'context/2026-10-22_appraisal-discount_cohort_test.md'),
    ('COPY', 'MULTIBANK_CONTEXT', 'AGENTS/REGINALD/reports/2026-10-13_review-response_forward-judgments.md', 'context/2026-10-13_review-response_forward-judgments.md'),
    ('ORIGINAL', 'SOURCE_COLLECTION', None, 'sources/2026-10-22_Q3_8K'),
    ('ORIGINAL', 'EGBN_DATA_TABLE', None, 'data/EGBN_asset_quality_quarterly.tsv'),
    ('ORIGINAL', 'EGBN_DATA_TABLE', None, 'data/loan_level'),
]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def extract(src):
    lines = src.read_text().split('\n')
    out, nums, i = [], [], 0
    while i < len(lines) and lines[i].startswith('#'):
        out.append(lines[i]); i += 1
    if i < len(lines):
        out.append(lines[i]); i += 1  # header row
    for j in range(i, len(lines)):
        if lines[j] and any(EGBN.search(c) for c in lines[j].split('\t')):
            out.append(lines[j]); nums.append(j + 1)
    return '\n'.join(out) + '\n', nums


def main(mode):
    man_path = HUB / 'INVENTORY.json'
    man = json.loads(man_path.read_text())
    entries = man['entries']
    stamp = now()
    # 1. extractor self-test on extracts whose source is unchanged
    tested = mismatched = 0
    for e in entries:
        if e['category'] != 'EGBN_REFERENCING_WORKBOOK_ROWS':
            continue
        src = ROOT / e['source']
        if sha(src) != e['source_sha256']:
            continue
        text, nums = extract(src)
        tested += 1
        if hashlib.sha256(text.encode()).hexdigest() != e['destination_sha256'] or nums != e['source_line_numbers']:
            mismatched += 1
            print('EXTRACTOR MISMATCH on unchanged source:', e['source'])
    print(f'extractor self-test: {tested} unchanged extracts re-derived, {mismatched} mismatched')
    if mismatched:
        print('STOP: extractor does not reproduce the 2026-10-20 method; nothing written.')
        return 2
    if mode == '--check':
        return 0
    # 2. refresh changed COPY / EXTRACT entries
    refreshed = []
    for e in entries:
        if e['kind'] not in ('COPY', 'EXTRACT'):
            continue
        src, dst = ROOT / e['source'], ROOT / e['destination']
        if not src.is_file() or sha(src) == e['source_sha256']:
            continue
        if e['kind'] == 'COPY':
            shutil.copy2(src, dst)
        elif e['category'] == 'EGBN_REFERENCING_WORKBOOK_ROWS':
            text, nums = extract(src)
            dst.write_text(text)
            e['selected_rows'], e['source_line_numbers'] = len(nums), nums
        else:
            print('SKIP (no refresh rule for this extract category):', e['source'])
            continue
        e.update(source_sha256=sha(src), destination_sha256=sha(dst), bytes=dst.stat().st_size, captured_at_utc=stamp)
        refreshed.append(e['source'])
    # 3. register new entries (one manifest entry per file)
    added = []
    have = {e['destination'] for e in entries}
    for kind, cat, src_rel, dst_rel in NEW_ENTRIES:
        dst = HUB / dst_rel
        if kind == 'COPY':
            src = ROOT / src_rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            files = [(src, dst)]
        else:
            paths = sorted(p for p in dst.rglob('*') if p.is_file()) if dst.is_dir() else [dst]
            files = [(p, p) for p in paths]
        for s, d in files:
            drel = d.relative_to(ROOT).as_posix()
            entry = dict(kind=kind, category=cat, source=s.relative_to(ROOT).as_posix(), destination=drel,
                         source_sha256=sha(s), destination_sha256=sha(d), bytes=d.stat().st_size, captured_at_utc=stamp)
            if drel in have:
                for e in entries:
                    if e['destination'] == drel:
                        e.update(entry)
            else:
                entries.append(entry); have.add(drel)
            added.append(drel)
    man['last_refreshed_at_utc'] = stamp
    man.setdefault('refresh_log', []).append({
        'at_utc': stamp, 'by': 'REGINALD refresh_inventory.py',
        'refreshed_changed_originals': refreshed, 'registered_or_updated': len(added),
        'note': 'Q3-2026 evidence added (8-K images, loan-level tables, quarterly metrics, Q4-wall and cohort reports); WORKOUT bridge rows WOB-REG-023..026 appended at the original ledger.'})
    man_path.write_text(json.dumps(man, indent=1) + '\n')
    print(f'refreshed {len(refreshed)} changed originals; registered/updated {len(added)} files; manifest now {len(entries)} entries')
    return 0


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('--check', '--apply'):
        print(__doc__); sys.exit(1)
    sys.exit(main(sys.argv[1]))

"""Rebuild LAST_COMPLETION's CLOSEOUT RECEIPT from commands, never from typed figures."""
import csv, hashlib, json, re, subprocess
from pathlib import Path
R = Path('/home/willi/Research-workspace')
lc = R / 'AGENTS/WALTER/LAST_COMPLETION.md'
t = lc.read_text(encoding='utf-8')
m = re.search(r'<!-- CLOSEOUT_RECEIPT_JSON\n(.*?)\nEND_CLOSEOUT_RECEIPT -->', t, re.S)
as_of = re.search(r'Updated (\S+Z)', t).group(1)
full = lambda c: subprocess.check_output(['git', 'rev-parse', c], cwd=R, text=True).strip()
sha = lambda p: hashlib.sha256((R / p).read_bytes()).hexdigest()
pub = [('ee7cc2297', 'Cards 001-004.'), ('725479117', 'Cards 005-006.'), ('838cce505', 'Cards 007-008.'),
       ('a49eecc0b', 'FLASH 016.'), ('a575b1449', 'FLASH 017; safe-push on a verified-clean tree carried 009-017.'),
       ('c5bc40381', 'Cards 020-023.'), ('8acf77a2f', 'Closeout records; safe-push on a verified-clean tree carried 018-023.')]
for c, _ in pub:
    assert subprocess.run(['git', 'merge-base', '--is-ancestor', c, 'origin/master'], cwd=R).returncode == 0, c
rows = [r for r in csv.DictReader(open(R / 'AGENTS/WALTER/routed/delivery_log.tsv', encoding='utf-8'), delimiter='\t') if r['signal_id'].startswith('SIG-W-20261105')]
dv = sum(r['written_state'] == 'delivered' for r in rows)
ev = ['AGENTS/WALTER/research/2026-11-05_morning/THRESHOLD-SCAN.md', 'AGENTS/WALTER/research/2026-11-05_morning/CALENDAR-RECONCILIATION.tsv',
      'AGENTS/WALTER/research/2026-11-05_morning/STEP7-REVIEW.md', 'AGENTS/WALTER/research/2026-11-05_morning/DISCOVERY.md',
      'AGENTS/WALTER/research/2026-11-05_morning/VERIFY-IRAN.md', 'AGENTS/WALTER/research/2026-11-05_morning/VERIFY-AI-TAPE.md',
      'AGENTS/WALTER/research/2026-11-05_bookmarks/REVIEW.md', 'AGENTS/WALTER/research/2026-11-05_L334/REPORT.md']
receipt = dict(schema=1, as_of=as_of, next_review='2026-11-06',
    publication=[dict(commit=full(c), state='published', note=n) for c, n in pub],
    delivery=dict(signal_date='20261105', total=len(rows), delivered=dv,
                  note='All day handoffs origin-proven and reconciled. Owner commits show HENRY, VIOLET, LIQUID, BOND, TERRY, REGINALD, CREED, AEOLUS, VULCAN and CARL read at least part; recipient use otherwise separate.'),
    owner_review=dict(scope='manual evidence review; no automatic completion', evidence=[dict(path=p, sha256=sha(p)) for p in ev]),
    procedure=dict(tier='full',
        boot='PARTIAL: step 7 ran after cards 001-015; desk STATUS reads partial; READS UNKNOWN on a stale attestation; November 5 collector run and close pass not reviewed.',
        session='CLOSED on Will request; no active helper, study or unattended work.'),
    manual_duties={
        '11': 'Cards 001-023 including FLASH 016 and 017. Batches BM-20261105-01 and -02 closed.',
        '13': 'Owner leads compared; BRENT, HENRY, LIQUID, VIOLET, BOND, PROME, CREED, AEOLUS, RED, TERRY, VULCAN, REGINALD and self refreshed before NETWORK.',
        '12(a,b)': 'Counts and NETWORK refreshed; last tape row is vendor intraday, no settled close claimed.',
        '12(c)': 'BALANCED baseline, labor LOOSE for November 6; standing flags unchanged.',
        '12(d,e)': 'FULL session entry and current bottom line.',
        '12(f)': 'STATUS and Iran anchor rotated verbatim. Charter 80% of budget stands: READ_CAP rule 20 does not bind it, earlier owed wording corrected.',
        '14': 'MEMORY #62 added, #7 extended, #39 extended; calendar check stays November 12.',
        'root.retirement': 'No safe unused-source retirement identified; no deletion sweep.',
        '15': 'Duties and approvals retained; resume list and calendar cutoff updated; close pass carried first.',
        '16': 'Will requested closeout; safe-push at verified-clean tree; reconcile applied.',
        'checks': 'Results in research/2026-11-05_final/closeout/checks.json. Doctor MED carried: consumption backlog and DEWEY 003R PARKED.',
        'Tier1': 'Last vendor tape 11:55 ET; no close read.'})
block = '<!-- CLOSEOUT_RECEIPT_JSON\n' + json.dumps(receipt, indent=2, ensure_ascii=False) + '\nEND_CLOSEOUT_RECEIPT -->'
t = t.replace(m.group(0), block)
t = t.replace('FULL desktop-switch closeout. Operational coverage PARTIAL. Publication is not consumption.', 'FULL closeout on Will request. Operational coverage PARTIAL. Publication is not consumption.')
lc.write_text(t, encoding='utf-8'); print(len(rows), dv)

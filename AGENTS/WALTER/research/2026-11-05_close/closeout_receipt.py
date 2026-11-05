"""Rebuild LAST_COMPLETION's CLOSEOUT RECEIPT from commands, never from typed figures."""
import hashlib
import json
import re
import subprocess
from pathlib import Path

R = Path('/home/willi/Research-workspace')
lc = R / 'AGENTS/WALTER/LAST_COMPLETION.md'
t = lc.read_text(encoding='utf-8')
m = re.search(r'<!-- CLOSEOUT_RECEIPT_JSON\n(.*?)\nEND_CLOSEOUT_RECEIPT -->', t, re.S)
old = json.loads(m.group(1))
as_of = re.search(r'Updated (\S+Z)', t).group(1)


def full(c):
    return subprocess.check_output(['git', 'rev-parse', c], cwd=R, text=True).strip()


def sha(p):
    return hashlib.sha256((R / p).read_bytes()).hexdigest()


pub = [(c, n) for c, n in [
    ('eef62c0009', 'FLASH 077 and IMMEDIATE 078 published by safe-push, verified-clean tree.'),
    ('0caa70e548', 'IMMEDIATE 079, sweep and anchor; published on a later push.'),
    ('3a0ca52a38', 'PRIORITY 080, DEWEY handoffs filed; published on a later push.'),
    ('05d47a8c8e', 'WQ-598 install; published on a later push.'),
] if subprocess.run(['git', 'merge-base', '--is-ancestor', c, 'origin/master'], cwd=R).returncode == 0]
assert len(pub) == 4, pub
ev = ['AGENTS/WALTER/research/2026-11-04_evening-boot/BOOT-RECEIPT.md',
      'AGENTS/WALTER/research/2026-11-04_evening-boot/crack-window-vwap.json',
      'AGENTS/WALTER/research/2026-11-04_evening-boot/basis-review.json',
      'AGENTS/WALTER/research/2026-11-05_iran-full-sweep/SWEEP.md',
      'AGENTS/TERRY/research/2026-11-04_vlo-leg-a/NOTE.md',
      'AGENTS/FALCON/reports/2026-11-04_weekly-review-gate001-fal07.md',
      'AGENTS/DEWEY/output/2026-11-04_carl-dr1-cof-q3-fdm-three-issuer-final.md']
receipt = dict(
    schema=1, as_of=as_of, next_review='2026-11-05',
    publication=[dict(commit=full(c), state='published', note=n) for c, n in pub],
    delivery=dict(signal_date='20261104', total=226, delivered=226,
                  note='All 226 day handoffs origin-proven. Named owner commits show TERRY, BRENT, FALCON, RED and CARL acted; recipient use otherwise separate.'),
    owner_review=dict(scope='manual evidence review; no automatic completion',
                      evidence=[dict(path=p, sha256=sha(p)) for p in ev]),
    procedure=dict(tier='full',
                   boot='PARTIAL: reads and intake complete; X scan recovered after re-authorization; European dailies, official settlements and step 8 narrative were deferred to this closeout; November 5 morning pass not run.',
                   session='CLOSED for desktop switch on Will request; no active helper, study or unattended work.'),
    manual_duties={
        '11': 'Cards 077-080 and 17 handoffs. No intake batch opened; 15 bookmarks staged, no manifest until reviewed.',
        '13': 'Nine changed owner leads compared; CARL, DAEDALUS, FALCON, ORACLE, RED, TERRY and self refreshed before NETWORK.',
        '12(a,b)': 'Counts and NETWORK refreshed; market rows retain observation dates, no fresh scan claimed.',
        '12(c)': 'BALANCED baseline, labor LOOSE for November 6; standing flags unchanged.',
        '12(d,e)': 'FULL session entry and current bottom line.',
        '12(f)': 'STATUS, MEMORY and LAST_COMPLETION under the rotation trigger. Charter 80% of budget, rotation owed and carried.',
        '14': 'MEMORY calendar check done; #60, #61 added; #26 re-pointed to step 7i.',
        'root.retirement': 'No safe unused-source retirement identified; no deletion sweep.',
        '15': 'Duties and approvals retained; 003R PARKED recorded; desktop resume list and calendar cutoff added.',
        '16': 'Will requested the machine switch; publication outcome recorded in the final report, foreign uncommitted files untouched.',
        'checks': 'Results in research/2026-11-05_close/closeout/checks.json. Doctor MED: consumption backlog, 003R parked, RED/ORACLE registry row now refreshed.',
        'Tier1': 'No new market pull at closeout.',
    })
new = '<!-- CLOSEOUT_RECEIPT_JSON\n' + json.dumps(receipt, indent=2, ensure_ascii=False) + '\nEND_CLOSEOUT_RECEIPT -->'
t = t[:m.start()] + new + t[m.end():]
t = t.replace('FULL approved-maintenance closeout; light narrative debt cleared.', 'FULL desktop-switch closeout.')
lc.write_text(t, encoding='utf-8')
print(as_of, len(pub), len(ev))

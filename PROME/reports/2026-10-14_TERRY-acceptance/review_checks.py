from pathlib import Path
import ast, hashlib, importlib.util, json, subprocess, sys, tempfile, zlib
from decimal import Decimal as D
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT = Path('/home/willi/Research-workspace')
OUT = ROOT / 'PROME/reports/2026-10-14_TERRY-acceptance'
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / 'AGENTS/TERRY/scripts'))
import ledger_sweep as ledger
import boot

checks = []
def record(name, value, detail=None):
    checks.append({'check': name, 'result': 'PASS' if value else 'FAIL', 'detail': detail})
def git(*args, cwd=ROOT):
    return subprocess.check_output(['git', *args], cwd=cwd)
def blob(rev, path):
    return git('show', rev + ':' + path)
def sha(data):
    return hashlib.sha256(data).hexdigest()

# Reviewer-devised counterexamples, no writes to the owner's working files.
for current, other in [('CONDITIONAL', 'CLOSED'), ('STAGED', 'DEAD'), ('FIRED', 'CLOSED')]:
    claims = {'MGMT-REVIEW': {'card(test)': current + ' — different MGMT-OTHER is ' + other,
                              'INDEX.md': other}}
    record('foreign narrative cannot conceal ' + current + '/' + other,
           len(ledger.check_state_agreement(claims)) == 1)
mixed = ('**Ids:** `MGMT-REVIEW-A` · `MGMT-REVIEW-B`\n'
         '**Current state [MGMT-REVIEW-A]:** CLOSED\n'
         '**Current state [MGMT-REVIEW-B]:** CONDITIONAL\n'
         '**Terry verdict:** CLOSED — historical aggregate\n')
states = ledger.management_states(mixed)
record('combined card explicit states override misleading aggregate verdict',
       states == {'MGMT-REVIEW-A': 'CLOSED', 'MGMT-REVIEW-B': 'CONDITIONAL'})
missing = ledger.management_states(mixed.replace('**Current state [MGMT-REVIEW-B]:** CONDITIONAL\n', ''))
record('combined card missing survivor cannot inherit terminal aggregate',
       bool(ledger.check_unparseable_claims({k: {'card(test)': v} for k, v in missing.items()})))
with tempfile.TemporaryDirectory(prefix='prome-inbox-review-') as td:
    desk = Path(td); inbox = desk / 'inbox'
    names = ['receipt.JSON', 'desk/sub/attachment.bin', 'desk/processed/old.json',
             'WILL/drop.json', 'README.md', '.gitkeep', 'desk/processed-data.txt']
    for name in names:
        path = inbox / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(b'fixture')
    old_l, old_t, old_b = ledger.INBOX, ledger.TERRY, boot.TERRY_DIR
    try:
        ledger.INBOX, ledger.TERRY, boot.TERRY_DIR = inbox, desk, desk
        rows = ledger.open_inbox_packets()
        listed = {p.removeprefix('inbox/') for p, _, _ in rows}
        record('nested binary and uppercase JSON boot/closeout agreement with exclusions',
               listed == set(boot.unprocessed_inbox()) == {'receipt.JSON', 'desk/sub/attachment.bin', 'desk/processed-data.txt'})
        record('untracked synthetic packets remain UNCOMMITTED', all('UNCOMMITTED' in label for _, label, _ in rows))
    finally:
        ledger.INBOX, ledger.TERRY, boot.TERRY_DIR = old_l, old_t, old_b

path = 'AGENTS/TERRY/scripts/ledger_sweep.py'
old_tree, new_tree = ast.parse(blob('fda97c793^', path)), ast.parse((ROOT/path).read_bytes())
def constant(tree, name):
    return next(ast.dump(n.value, include_attributes=False) for n in tree.body
                if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name) and n.target.id == name)
record('STATES and COMPATIBLE AST identical to pre-repair',
       all(constant(old_tree, n) == constant(new_tree, n) for n in ['STATES', 'COMPATIBLE']))
claims, cards, _ = ledger.gather_live()
record('live management coverage 17 IDs', sum(k.startswith('MGMT-') for k in claims) == 17)
for identity, expected in [('MGMT-QQQ745P-OCT15','CLOSED'), ('MGMT-QQQ740P-OCT15','CONDITIONAL'),
                           ('MGMT-TLT82P-OCT16','CLOSED'), ('MGMT-DURSHORT-EXIT-WQ291','CONDITIONAL')]:
    record(identity + ' distinct live state', all(ledger.state_of(v) == expected for v in claims[identity].values()), claims[identity])

original = blob('fda97c793^', 'AGENTS/TERRY/STATUS.md')
archive = (ROOT/'AGENTS/TERRY/archive/STATUS_ARCHIVE_2026-10-14.md').read_bytes()
body = archive.split(b'<!-- VERBATIM BODY -->\n',1)[1].rstrip(b'\n')
record('archived body is contiguous original bytes and independently matches CRC',
       body in original and len(body)==1780 and f'{zlib.crc32(body):08x}'=='5a06a5b9')
record('STATUS below existing 70 percent stop', (ROOT/'AGENTS/TERRY/STATUS.md').stat().st_size < 32550 * .7)

vp = 'AGENTS/TERRY/setups/VLO-SHARE_management-proposal_2026-09-28.md'
ruling = blob('5a8168f95','PROME/proposals/2026-10-11_wq418-420-RULED.md').decode()
quoted = ruling.split('## Approved exact insert\n\n',1)[1].split('\n\n## Execution',1)[0]
raw_insert = '\n\n'.join(p.removeprefix('> ') for p in quoted.split('\n>\n'))
pinned = blob('31f9f3d1a','AGENTS/TERRY/research/2026-10-11_WQ419-VLO-precision-bar-PROPOSAL.md').decode()
encoded = blob('08158a2c4',vp).decode()
current = (ROOT/vp).read_text()
insert = quoted + '\n\n'
record('WQ420 exact three-paragraph approved quote encoded and still present', quoted in encoded and quoted in current)
record('WQ420 proposal and ruling paragraphs agree', all(p.removeprefix('> ') in pinned for p in quoted.split('\n>\n')))
without = encoded.replace(insert,'',1)
lines = without.splitlines(keepends=True)
index = next(i for i,line in enumerate(lines) if line.startswith('> **CURRENT AMENDMENT — WQ-420'))
del lines[index:index+2]
record('WQ420 removal of only insert and dated banner restores prior entire card', ''.join(lines).encode()==blob('08158a2c4^',vp))
# Independent boundary arithmetic demonstrating why the approved precision matters.
crack = D('4.9990') * 42 - D('114.96')
record('WQ420 near-boundary counterexample retained: 94.998 is below 95 despite display 95.00',
       crack == D('94.9980') and crack < D('95') and crack.quantize(D('.01')) == D('95'))
record('WQ420 equality at 90.16 does not fire strict exit', not (D('90.16') < D('90.16')))

source = (ROOT/'PROME/data/2026-10-14_broker-capture-TRANSCRIPTION.json').read_bytes()
owner_source = (ROOT/'AGENTS/TERRY/research/2026-10-14_broker-receipt-source.json').read_bytes()
record('October14 owner source equals sender transcription exactly', source == owner_source, sha(source))
packet = (ROOT/'AGENTS/TERRY/inbox/2026-10-14_from-PROME_QQQ-filled-exits.json').read_bytes()
record('QQQ packet matches already-consumed saved hash prefix', sha(packet).startswith('9397b92c'), sha(packet))
record('QQQ proceeds and incremental realized arithmetic',
       D('670.32')+D('821.32')==D('1491.64') and D('821.32')-D('275.66')==D('545.66')
       and D('670.32')-(D('2122.65')-D('1591.99'))==D('139.66'))

# Additional Git counterexample: foreign staged deletion plus distinct binary
# staged/unstaged bytes and untracked file; only an owned path may be committed.
with tempfile.TemporaryDirectory(prefix='prome-git-independent-') as td:
    repo=Path(td)
    git('init','--initial-branch=master',cwd=repo)
    git('config','user.name','PROME disposable reviewer',cwd=repo)
    git('config','user.email','review@example.invalid',cwd=repo)
    for name,data in [('owned.txt',b'base'),('foreign binary.bin',b'\0base'),('foreign deleted.txt',b'base')]:
        (repo/name).write_bytes(data)
    git('add','--','owned.txt','foreign binary.bin','foreign deleted.txt',cwd=repo)
    git('commit','-m','fixture baseline',cwd=repo)
    (repo/'foreign deleted.txt').unlink()
    (repo/'foreign binary.bin').write_bytes(b'\0staged')
    git('add','--','foreign binary.bin','foreign deleted.txt',cwd=repo)
    (repo/'foreign binary.bin').write_bytes(b'\0unstaged')
    (repo/'foreign untracked.txt').write_bytes(b'private work')
    def snapshot():
        return (git('ls-files','--stage','-z','--','foreign binary.bin','foreign deleted.txt',cwd=repo),
                git('diff','--cached','--binary','--','foreign binary.bin','foreign deleted.txt',cwd=repo),
                git('diff','--binary','--','foreign binary.bin','foreign deleted.txt',cwd=repo),
                (repo/'foreign binary.bin').read_bytes(), (repo/'foreign untracked.txt').read_bytes(),
                (repo/'foreign deleted.txt').exists())
    before=snapshot(); (repo/'owned.txt').write_text('changed')
    git('commit','-m','owned-only','--','owned.txt',cwd=repo)
    record('independent Git binary/staged-deletion/untracked counterexample preserved',
           snapshot()==before and git('show','--format=','--name-only','HEAD',cwd=repo).strip()==b'owned.txt')

files=['AGENTS/TERRY/scripts/ledger_sweep.py','AGENTS/TERRY/scripts/boot.py','AGENTS/TERRY/scripts/inbox_paths.py',
       'AGENTS/TERRY/CLOSEOUT.md',vp,'AGENTS/TERRY/STATUS.md','AGENTS/TERRY/TRADE_BOOK.md','AGENTS/TERRY/setups/INDEX.md']
report={'reviewer':'PROME / Codex / root; independent from TERRY author',
        'observed_at':datetime.now(ZoneInfo('America/New_York')).isoformat(),
        'checks':checks,'input_sha256':{p:sha((ROOT/p).read_bytes()) for p in files},
        'scope':'Reviewer counterexamples and deterministic evidence checks; no broker freshness, order execution, scoring authority or remote publication claim.'}
(OUT/'independent-checks.json').write_text(json.dumps(report,indent=2)+'\n')
for c in checks: print(c['result'],c['check'])
sys.exit(any(c['result']=='FAIL' for c in checks))

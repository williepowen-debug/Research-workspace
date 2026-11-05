import dispatch as d
from pathlib import Path

BODY = '''DEWEY research-output, commission CARL-DR-1 / DOCKET L567; report `AGENTS/DEWEY/output/2026-11-04_carl-dr1-cof-q3-fdm-three-issuer-final.md`, commit 42a73710e2. Three-issuer Q3 card refresh complete.

Verdict: Capital One's domestic modified-card cohort delinquent balance rose $645M to $993M in one quarter (+54.0%; domestic book +11.1%). Delinquent share 25.2% versus 15.7-18.0% at five prior period-ends. Spot-checked at 10-Q Table 4.9. Synchrony and Bread show no matching move. Scale ratio 113.31 bp (June 119.27).

Cause UNKNOWN; the filing gives none. Class-wide causal test NOT COMPUTABLE. Prior-year rows may hold pre-closing Discover loans.

Do NOT relay as hidden delinquency, a class-wide card signal, a Capital One credit break, evidence of misstatement, or the scale-ratio fall as an improvement. Do not pool the three issuers.

ACTION CARL: consume the report within the existing card leg. DEWEY's stub is in CARL's inbox. INFO REGINALD, GIBBS: large-bank card context, no grade change. Next filing dates are owner-held.'''

d.CARDS = [dict(
    n=80,
    slug='DEWEY-Capital-One-modified-card-cohort',
    title='Capital One modified-card cohort delinquency rose 54% in Q3; cause unknown',
    action=['CARL'],
    info=['REGINALD', 'GIBBS', 'RED', 'PROME'],
    precedence='PRIORITY',
    signal_type='research',
    confidence=0.9,
    cluster='CONSUMER_STAGFLATION',
    domain='CONSUMER_CREDIT',
    entities=['COF', 'Capital-One', 'CARL-DR-1', 'SYF', 'BFH'],
    body=BODY,
    sources='https://www.sec.gov/Archives/edgar/data/927628/000092762826000152/cof-20260930.htm ; AGENTS/DEWEY/research/2026-11-04_cards/COF-Q3-2026-tables.json',
    note='Phase 2.8b return. Table 4.9 row checked at primary; arithmetic reproduced; no conflict found in CARL STATUS. DEWEY wrote the CARL copy, REGINALD and GIBBS backfilled as INFO.',
    extra={'verify_verdict': 'VERIFIED-PRIMARY', 'deep_research_ref': 'CARL-DR-1'},
)]
d.ORIGIN = 'DEWEY research-output / CARL-DR-1 L567'
d.NO_HANDOFF_ANY = {'TERRY', 'PROME', 'CARL'}  # CARL: DEWEY's create-only copy already delivered.
d.OUT = Path(d.OUT.parent / '2026-11-04_evening-boot/dewey-return')
d.OUT.mkdir(exist_ok=True)
d.main()

p = d.ROOT / 'BOARD/SIG-W-20261104-080-DEWEY-Capital-One-modified-card-cohort.md'
t = p.read_text()
assert t.count('source: "WALTER"') == 1
p.write_text(t.replace('source: "WALTER"', 'source: "DEWEY"'))

log = d.W / 'registry/DEEP_RESEARCH_FLAGGED_LOG.tsv'
rows = log.read_text().split('\n')
n = 0
for i, r in enumerate(rows):
    c = r.split('\t')
    if len(c) > 11 and c[1] == 'REQ-DEWEY-20261022-003R':
        c[9] = ('2026-11-04 PARKED by DEWEY, method and capacity; row stays PARTIAL and overdue; no report produced, no Q3 placement computed. '
                'Availability 20:47 ET: FFIEC 4,259 of 4,268 Q3 filers (DEWEY measurement, not reproduced by WALTER); FDIC BankFind 0 rows for 20260930 '
                'against June control 4,313 (WALTER reproduced 2026-11-04). The unavailable-data kill rule is NOT met. DEWEY re-checks FDIC at its next touch and runs the residual on the original definitions when Q3 loads; '
                'EGBN parent/bank and old VLY relay stay open. PRIOR: ' + c[9])
        n += 1
    if len(c) > 11 and c[1] == 'CARL-DR-1':
        c[9] = ('2026-11-04 CARD LEG COMPLETE, delivered as SIG-W-20261104-080 (three-issuer Q3 refresh, L567); causal class-wide test still NOT COMPUTABLE, row stays PARTIAL. PRIOR: ' + c[9])
        n += 1
    rows[i] = '\t'.join(c)
assert n == 2, n
log.write_text('\n'.join(rows))
print('ledger rows updated', n)

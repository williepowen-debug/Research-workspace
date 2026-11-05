"""One-shot FULL closeout text for the November 5 desktop switch. Exact-match edits; fails loud."""
import csv
import re
import subprocess
from pathlib import Path

W = Path('/home/willi/Research-workspace/AGENTS/WALTER')
STAMP = subprocess.check_output(['date', '-u', '+%Y-%m-%dT%H:%M:%SZ'], text=True).strip()


def sub1(text, old, new):
    assert text.count(old) == 1, old[:70]
    return text.replace(old, new)


# Step 13: REGISTRY, from owner leads read this session.
reg = W / 'REGISTRY.tsv'
rows = list(csv.reader(reg.open(encoding='utf-8', newline=''), delimiter='\t', quoting=csv.QUOTE_MINIMAL))
hdr = rows[0]
ui, fi = hdr.index('Updated'), hdr.index('Focus')
upd = {
    'WALTER': ('2026-11-05', 'November 5 FULL CLOSED for desktop switch; 80 November 4 cards, 226 published handoffs. Morning pass not run; 15 bookmarks staged unread. Runtime varies, tonight Claude Code.'),
    'CARL': ('2026-11-05', 'November 5 card-reports read: Capital One modified-card row added; no score, test or prediction moved.'),
    'DAEDALUS': ('2026-11-05', 'WQ-602 blueprints applied; WQ-601 applied except FALCON by packet; WQ-600 complete on the laptop.'),
    'FALCON': ('2026-11-05', 'November 4 weekly review: FAL-07 CONFIRMED, census 7 (SELAT STORM provisional, IMO conflict carried), marks held; November 5 FAL-06 search first pass only.'),
    'ORACLE': ('2026-11-04', 'November 4 full rewrite; Kalshi unsigned, public market data. Prediction-market probabilities are independent calibration evidence.'),
    'RED': ('2026-11-04', 'S58-b November 4 closed: HOLD 72, net-bear 68 unchanged; next wake November 6 after jobs, sooner on a signed Hormuz deal or new US strike.'),
    'TERRY': ('2026-11-04', 'November 4: VLO HELD-01 leg A FIRED on accepted November 2 reading, one-share SELL rec for November 5, Will\'s hand; CME unread. No order.'),
}
seen = set()
for r in rows[1:]:
    if r and r[0] in upd:
        r[ui], r[fi] = upd[r[0]]
        seen.add(r[0])
assert seen == set(upd)
with reg.open('w', encoding='utf-8', newline='') as f:
    csv.writer(f, delimiter='\t', lineterminator='\n').writerows(rows)

# Step 12: STATUS.
st = W / 'STATUS.md'
t = st.read_text(encoding='utf-8')
t = re.sub(r'\*\*Updated:\*\* .*\n', f'**Updated:** {STAMP} — CLOSED for desktop switch on Will request; FULL closeout. Coverage PARTIAL. Duties: LAST_COMPLETION.md.\n', t, count=1)
t = re.sub(r'## BOTTOM LINE\n\n.*?\n\n## DATED', '''## BOTTOM LINE

CLOSED for the desktop switch. November 4: 80 cards, 226 origin-proven handoffs; recipient use is separate. Evening finds: oil fell about 9% with no deal established (078); the December crack put held-VLO's exit through its line, TERRY graded FIRED (077); full Iran sweep found unrecorded hulls (079). WQ-598 steps 7i and 7e(g) installed.

BALANCED baseline; labor intake LOOSE for November 6 payrolls. November 5 morning pass NOT run; 15 bookmarks staged unread. Desktop resume list: top of LAST_COMPLETION.md.

## DATED''', t, count=1, flags=re.S)
row = ('| November 4 evening boot (pull November 5 01:18Z; vendor rows are not settlements) | FRED HY 340 / CCC 1,316 / VIXCLS 20.83 / SOFR−IORB +7 bp [Nov 3]; T5YIFR 2.22 [Nov 4]; SKEW 150.01 [Nov 3]; ICSA 194,000 [w/e Oct 24]; Cushing 27.250M [w/e Oct 30]; AGSI gap −15.772pp [Nov 3]. '
       'CNBC November 4 settlements Brent $94.62 (−8.7%), WTI $88.12 (−8.3%), months unnamed. Vendor S&P 7,688.62, VIX 16.61, KRE 74.13, WAL 79.24, USO 145.41, VLO 365.34. Matched December ULSD crack: Nov 2 $89.2472 TERRY-accepted (HELD-01 leg A FIRED), Nov 3 $94.1952, Nov 4 ESTIMATE $88.5451; CME unread. '
       'REG-T-04 10 bp watch. No new WALTER fire; European dailies, TTF and official settlements not re-pulled. Evidence: research/2026-11-04_evening-boot/. |\n')
t = sub1(t, '| November 4 catch-up | FRED November 3:', row + '| November 4 catch-up | FRED November 3:')
t = sub1(t, '- Current closeout evidence: `research/2026-11-04_catchup/closeout/`;', '- Current closeout evidence: `research/2026-11-05_close/closeout/`; evening boot `research/2026-11-04_evening-boot/`; Iran sweep `research/2026-11-05_iran-full-sweep/SWEEP.md`; prior `research/2026-11-04_catchup/closeout/`;')
t = re.sub(r'REGISTRY refreshed before NETWORK at .*?\n\nComplete cross-runtime lifecycle visibility remains UNKNOWN\. No active WALTER helper, study or unattended task\.',
           f'REGISTRY refreshed before NETWORK at {STAMP}. Owner leads changed since the prior close and mirrored: CARL, DAEDALUS, FALCON, ORACLE, RED, TERRY; NEXUS and WAL already current; BRENT consumed by commit, STATUS lead still dated November 2. Colors/classes unchanged. HENRY and VIOLET hold unread ACTION items on cards 077/078.\n\nComplete cross-runtime lifecycle visibility remains UNKNOWN. No active WALTER helper, study or unattended task.', t, count=1, flags=re.S)
t = sub1(t, 'through the November 6 payroll release window (within 72 hours as of November 4).', 'through the November 6 payroll release window (within 72 hours as of November 5).')
st.write_text(t, encoding='utf-8')

# Step 12(d): SESSION_LOG.
sl = W / 'SESSION_LOG.md'
entry = (f'# FULL CLOSEOUT — {STAMP} — closed for desktop switch on Will request\n\n'
         'Claude Code Opus 5.5 session walter-dc, booted November 4 20:14 ET PARTIAL. Cards 077 FLASH (December crack below held-VLO line), 078 oil/VIX move, 079 full Iran sweep, 080 DEWEY Capital One; 17 handoffs. TERRY graded HELD-01 leg A FIRED; FALCON confirmed FAL-07 and census 7. 003R PARKED by DEWEY. X re-authorized on the laptop, 15 bookmarks staged unread. WQ-598 A: boot step 7i and CRUISE_CAPITAL_REVIEW installed. November 5 morning pass not run.\n\n')
sl.write_text(entry + sl.read_text(encoding='utf-8'), encoding='utf-8')

# Step 14: MEMORY.
m = W / 'MEMORY.md'
t = m.read_text(encoding='utf-8')
t = sub1(t, 'next calendar check 2026-11-05.', 'calendar check done 2026-11-05 (22.6 KB, no rotation); next 2026-11-12.')
t = sub1(t, '→ `LAST_COMPLETION.md` OPEN DESIGN DECISIONS (a); raised to PROME 9/17.', '→ charter step 7i (installed 11/04, WQ-598 A); raised to PROME 9/17.')
t = sub1(t, '**✅ RETIRED 2026-09-01 — the two-branch-test', '''60. **A level without its change can hide the week's biggest move.** 11/04: catch-up logged Brent 95.07 while the tool withheld the return; January Brent had fallen 16.7% in three sessions and no card said so. Read the prior row by hand, labelled unverified; a withheld field is not a quiet tape. → BOARD 078
61. **After any sharp move, read the registered gates on held names at their letter.** 11/04: nobody asked; the December crack had already crossed the held-VLO exit on 11/2, unseen for two days. The oil headline was the smaller story. Vendor date rows can be evening sessions: check volume, then use the gate's own settle window. → BOARD 077 · PROME/GATES.tsv

**✅ RETIRED 2026-09-01 — the two-branch-test''')
t = re.sub(r'## Session Notes\n\n.*\Z', '''## Session Notes

November 5 FULL CLOSED for desktop switch. LAST_COMPLETION owns duties and the desktop resume list. 80 November 4 cards, 226 published handoffs. VLO exit FIRED-UNEXECUTED pending Will. Morning pass not run; 15 bookmarks staged unread. X token and FFIEC token are machine-local: both need the desktop step. Steps 7i and 7e(g) run first at the next launched boot.
''', t, count=1, flags=re.S)
m.write_text(t, encoding='utf-8')

# Step 15: LAST_COMPLETION body; receipt JSON is rebuilt by closeout_receipt.py.
lc = W / 'LAST_COMPLETION.md'
t = lc.read_text(encoding='utf-8')
t = re.sub(r'\AUpdated? .*?\n|\A# WALTER — LAST COMPLETION\n\nUpdated .*?\n', f'# WALTER — LAST COMPLETION\n\nUpdated {STAMP}, Claude Code Opus 5.5, session walter-dc. CLOSED for desktop switch on Will request; FULL closeout, coverage PARTIAL.\n', t, count=1)
head = f'''## DESKTOP RESUME — do these first on the other machine

1. `git pull --rebase` at root, then ordinary boot. Research-Intake is a separate clone: step 7e(a) pulls it.
2. **X login:** `AGENTS/WALTER/.env` does not travel and X replaces its token at each use, so expect a refresh failure. Will re-authorizes with `x_bookmarks_scan.py --authorize`; seen-set and stage are tracked and safe.
3. **FFIEC login:** per PROME/MACHINE_LOCAL.md the laptop token was renewed November 1, expires January 31; the desktop holds the dead August 7 token. Paste the new one into `FORGE/tools/market-data/.env` there. PROME owns that file; WQ-495's "by November 5" text predates or misses this, ask PROME to reconcile.
4. **Morning pass, NOT run:** boot step 7i from the cutoff below, then 6c. November 5 claims, Challenger, BoE, NREF and the November 4 HY and VIXCLS prints are unreviewed; VIXCLS likely resets RED-FT-06 to 0/5, RED owns it.
5. **15 bookmarks:** staged, unread beyond headlines, unmarked. Finish via `--review-template`, then `--mark --review`. CoreWeave first.
6. **CRUISE queue:** one open candidate, `cruise:7126564b0db4`, Sandals joint venture; check event date against SIG-W-20261014-028.

Calendar coverage cutoff: 2026-11-04T21:01:17Z (last collector run reviewed; step 7i has not yet run).

## STATUS'''
t = sub1(t, '## STATUS', head)
t = re.sub(r'(## STATUS\n\n).*?(\n## GAPS)', r'''\1Session CLOSED for desktop switch on Will request. No active WALTER helper, study or unattended task. Evidence: research/2026-11-04_evening-boot/BOOT-RECEIPT.md and research/2026-11-05_iran-full-sweep/SWEEP.md.

November 4 total: 80 BOARD cards, 226 origin-proven handoffs. WAL Q3 source recovery remains CLOSED — NOT RECOVERED, accepted by Will; do not expand or restart.

## CHANGED

Cards 077 FLASH, 078 and 079 IMMEDIATE, 080 PRIORITY, 17 handoffs. Iran anchor updated, next full sweep about November 12. DEEP_RESEARCH rows CARL-DR-1 and 003R updated; two DEWEY handoffs and PROME's WQ-598 packet consumed. WQ-598 A installed: charter steps 7i and 7e(g), BOOT_PROTOCOL, SPEC_OWNERSHIP, intake_scan queue, 15 tests, basis hashes. X re-authorized on the laptop.

## RESULT

December ULSD crack fell below the held-VLO line: TERRY accepted November 2 $89.2472 and graded HELD-01 leg A FIRED; one-share SELL rec for November 5, Will's hand. CME unread; a final November 2 settle at or above $90.16 reverses. Oil fell on November 4 (Brent settle $94.62, −8.7%) with no signed text, reopening or public US answer. FALCON: FAL-07 CONFIRMED, census 7, SELAT STORM provisional, IMO table conflict carried. BRENT: fade test NOT MET, flow basis UNRESOLVED. Capital One modified-card delinquent balances +54.0% in Q3, cause UNKNOWN; CARL thesis NOT YET. Evidence is not trade authority.
\2''', t, count=1, flags=re.S)

# GAPS: replace only bullets the session superseded.
t = re.sub(r'- Publication: all 209 November 4 handoffs.*?\n', '- Publication: all 226 November 4 handoffs are origin-proven and reconciled; no consumption inferred except named owner commits: TERRY, BRENT, FALCON, RED and CARL acted on their cards. HENRY and VIOLET hold 077/078 unread. Current publication is in the receipt below.\n', t, count=1)
t = re.sub(r'- Reader basis: four changed boot-defining files.*?\n', '- Reader basis: PROME renewed READS at a457899537 and added step 7i reads at 88829d531e. Three changed boot files reviewed, hashes renewed (evening-boot/basis-review.json). Charter is 25,922 B, 80% of budget; rotation to <22,785 B owed and needs a scoped pass, not done here. Complete fleet lifecycle visibility UNKNOWN; no DARK inference.\n', t, count=1)
t = re.sub(r'- DEWEY reconciliation complete: 005R RESOLVED.*?\n', '- DEWEY: 005R RESOLVED through VULCAN L800 and DEWEY L834, method omissions and WQ-551.FIRM deferral survive. 003R PARKED by DEWEY November 4, row stays PARTIAL and doctor MED stays until it runs: FDIC BankFind 0 Q3 rows against June control 4,313 (WALTER reproduced); FFIEC 4,259 of 4,268 is DEWEY\'s measurement. Not an unavailable-data deferral; no Q3 placement exists. DEWEY re-checks FDIC at next touch.\n', t, count=1)
t = sub1(t, ' Full Iran sweep still due November 5; bounded anchor update did not reset its clock.', ' Full Iran sweep completed November 5 01:44Z; ukmto.org 403, warnings 192-26 onward unseen, FT and Bloomberg originals unread.')
t = sub1(t, ' Iran November 5 full-sweep date unchanged, no guard reset.', '')
t = sub1(t, 'FALCON WQ-559/UKMTO 188/November 4 gate; CREED T-01a/Kernel;', 'CREED T-01a/Kernel;')

t = re.sub(r'## WILL_NEEDS\n\n.*?\n## SOURCE-SEARCH', '''## WILL_NEEDS

Held-VLO one-share sale: FIRED-UNEXECUTED, Will's hand, tell PROME the result. CREED launch permission for T-01a. X re-authorization and FFIEC token paste on the desktop. Existing WQ-573, WQ-556 C, WQ-401/WQ-508 and source-search limits remain binding.

## FOLLOW-UP

1. PROME: wake recommendation for HENRY (077 line and basis) and VIOLET (078 vol regime) raised; no wake logged at close. DEWEY 003R residual stays with DEWEY. L907 remains the bridge repair; L920 quote tolerance kept, intermittent refusals open at PROME.
2. November 5: morning pass per DESKTOP RESUME. November 6: payrolls, L334 predictive leg and WQ-556 C check, STWD/ACRE cohort releases. November 7: Friedberg/coverage-level and reserve/modification breadth pass. Supply dated prediction IDs/sources at the relevant owner's next authorized session per COMPLETION_SPEC; no historical registration sweep.
3. November 11: Veterans Day HY non-session bridge. About November 12: full Iran sweep, MEMORY calendar check, staleness sweep; UNG reversal deadline remains November 12. November 13: WQ-556 C remeasurement and REG-T-06 CFR grade. Mid-December ERCOT audit and WATT EO 14421 before December 24 remain unchanged.
4. FLG/REGINALD first reviews are complete; FLG M3 allocation waits for T-02/10-Q, REGINALD filing/cause questions and November 7 detector fix survive. CORAL/other semantic consumption is unproved. Sinokor legal-action, dated Iran answer/Qatar draft and LIQUID October issuance retain normal owner review; no unresolved headline becomes a new commissioned study.
5. Prior cleanup/L845/VPS/transcription and boundary 7 repairs remain complete; no repeat repair. Prior CATO substantive evidence lacks an exact receipt; backlog alone does not authorize a wake. No continuing helper or unattended WALTER activity.
6. Idea, not installed: show prior-day change for key instruments in the boot scan, labelled unverified when the vendor withholds it. Extends an existing step; needs Will's word.

## SOURCE-SEARCH''', t, count=1, flags=re.S)

t = re.sub(r'\*\*Coverage reviews completed November 4; recommendations not deployed:\*\*\n.*?(- P2 lifecycle-candidate)', r'''**Coverage fixes, WQ-598 RULED A (Will November 4 20:59 ET):** calendar catch-up (step 7i) and CRUISE_CAPITAL_REVIEW (step 7e(g)) installed at 05d47a8c8e, unrun until the next launched boot; PROME deploys the two supplier queries. No scheduler, unattended run or wake authority.
\1''', t, count=1, flags=re.S)
lc.write_text(t, encoding='utf-8')
print(STAMP)

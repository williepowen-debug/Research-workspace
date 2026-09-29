# WALTER → CREED: set up a CRE case ledger (Will-directed, 2026-09-29)

**ASK (CREED):** own and set up a ledger of named CRE distress cases, one row per property/loan, so patterns and connections across cases become visible. Design is yours.

## Will's word (terminal, this session, verbatim)

> "Yeah I think we should probably start trying to track major cases. My thought process being that perhaps we can search for patterns or other helpful connextions."
> "okay what I will do is probably spawn CREED and try to have him organize it?"

Context: said after WALTER dispatched `SIG-W-20260929-015` (5400 Westheimer Court, Houston) and noted it matches the shape of your `KB-CREED-046` (3000 Post Oak): a large older single-tenant office building failing at tenant exit.

## Why CREED
You already hold named cases (KB-046), grade the CRE triggers, and own national CRE/CMBS. WALTER routes; it does not own analysis.

## WALTER's side (proposed, starts on your go)
Every signal naming a specific distressed property/loan gets CREED on the recipient lines as a case feed, **in addition to** its normal owner (CORAL for Florida, HOMER for multifamily, WAL/FLG/OZK for their own loans), plus a `case:` tag in the signal. Nothing about ownership of those desks' cases changes; the ledger just sees them.

## A starting column set (suggestion only)
property · address · city/state · type · vintage · size · tenant/occupancy · **trigger** (TENANT_EXIT / MATURITY_DEFAULT / RATE_RESET / OPERATING_SHORTFALL / FRAUD_OR_LEGAL) · loan amount · originator · **holder** (CMBS trust / bank / debt fund) · special servicer · dated event timeline · latest status (with as-of) · value marks (basis + date) · implied loss · **fleet links** (WAL, OZK, FLG, LADR and the mREIT cohort, any trigger id) · sources · source quality.

The pattern questions this is built to answer: same lender/holder/servicer across cities; trigger mix (tenant exit vs maturity default); vintage; time from special servicing to resolution; loss severity by type.

## Seed (in progress)
WALTER is building a DRAFT seed from BOARD (80 signals carry distress-event language, 61 in `BANK_COLLATERAL`) and read-only greps of CREED/REGINALD/CORAL/HOMER/WAL/FLG/OZK/BROCK files:
- `AGENTS/WALTER/research/2026-09-29_cre-case-seed.tsv`
- `AGENTS/WALTER/research/2026-09-29_cre-case-seed-NOTES.md` (counts, repeats, contradictions, unrowable candidates)

⚠️ **Not ready at the time of writing.** WALTER will send you a message when it lands. It is a seed: every row cites its source, UNKNOWN where the files are silent, **nothing from the web**. Verify before adopting; your registry rules govern.

## Already in your queue
`inbox/WALTER/SIG-W-20260929-015.md` (5400 Westheimer Ct: the first new case) · `SIG-W-20260929-007` (HOMER's answer, info).

$0. No trigger, band or score is touched by this.

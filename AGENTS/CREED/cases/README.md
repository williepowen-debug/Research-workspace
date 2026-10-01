# CREED Case Ledger — named CRE distress cases

**Created:** 2026-09-29 · **Owner:** CREED · **Directed by:** Will, 2026-09-29, in WALTER's session, relayed in `inbox/processed/2026-09-29_from-WALTER_cre-case-ledger-will-directed.md` @`dffcb78e0`: *"start trying to track major cases ... search for patterns or other helpful connextions."*
**Not a boot read.** Open it on demand and grep by `case_id`. The read-cap budget doesn't bind it (it binds only surfaces a boot reads whole). *(This line said "keep each file under 32,550 B anyway" until the 2026-09-29 seed adoption took `CASES.tsv` to ~50 KB; the aim was dropped rather than cutting verified content.)*

## What it's for

It holds one row per named distressed property or loan, so connections *across* cases become visible: the same lender, holder or special servicer turning up in different cities; the mix of triggers (tenant exit vs. maturity default); building vintage and loan vintage; time from special servicing to resolution; and loss severity by property type.

## ⚠️ The limit that governs every pattern read (read before counting anything)

**This is a sample of cases that got reported, not a sample of the market.** A case enters because a newsletter, a court filing or a news story named it. That over-weights large, dramatic office cases in major metros, and cases whose outcome is already public. Cases that resolve quietly (a modification, a discounted payoff, a bank loan nobody writes about) are under-weighted.

⇒ **Frequencies computed here measure what gets reported.** "70% of our cases are tenant exits" is a fact about press coverage until it's tested against an aggregate (Trepp / CREFC by trigger, MBA, FDIC).
⇒ **A pattern found here is a HYPOTHESIS with a named test, never a finding on its own.** Write the aggregate that would test it beside it.
⇒ **Never quote a ledger severity as "the loss rate" for a property type.** The same-basis severity distribution is `KB-CREED-041` (CREFC monthlies).

## Rules

1. **One case = one loan on one property.** For a portfolio loan: one case, with the properties listed in `notes`. For senior + mezz on one property: one case, with both loans in `loan_amount_usd`.
2. **UNKNOWN, never blank.** A blank cell can't be told apart from "not checked".
3. **Status carries a date.** `latest_status` is paired with `status_as_of`, the date the status was *true*, not the date we read it.
4. **Every value mark names its basis and date** (appraisal / sale price / net proceeds / tax-assessor value / model value). **Never compare across bases** (root trap #2: a real number on the wrong basis).
5. **Implied loss names its basis** (e.g. "net proceeds vs senior balance, BEFORE servicer advances"). A figure without a basis goes in `notes` as UNRECONCILED, not in `implied_loss_pct`.
6. **Originator ≠ holder.** A lender's name on a loan does NOT say whose balance sheet carries it. `holder_type` stays UNKNOWN until the trust or bank is established. A Ladder-originated CMBS loan is not Ladder's credit loss (the -015 caveat).
7. **Source tier on every row**: `PRIMARY-READ` / `PRIMARY-CITED` / `SECONDARY` / `SEARCH-SUMMARY` / `LEAD` *(added 2026-09-30 for Will's workbook import: a row with NO source link, e.g. a social-post compilation; recorded so it is not lost, NOT citable until a source is found)*. The search-summary tier exists so a figure seen only in a search listing isn't dressed up as read.
8. **Events are dated separately from when they were reported.** *(Enforced 2026-09-29: every event has a `reported` date + `reported_basis`; a fleet-file date is labelled as such, never passed off as the publication date.)* `CASE_EVENTS.tsv` carries `event_date` (when it happened; `UNKNOWN` or `≤YYYY-MM-DD` allowed) and `reported` (the source date). Duration statistics use `event_date` only.
9. **The ledger is not a trigger instrument.** No case moves a CREED score, band or trigger by being entered. `trigger_eligibility` states, per case, whether a registered trigger's own rules would count it (e.g. `CREED-T-06`: excludes obsolete/vacant collateral by name).
10. **Other desks keep their cases.** CORAL (Florida), HOMER (multifamily) and the bank desks (WAL, FLG, OZK, REGINALD) own their named credits. A row here cites their record in `fleet_links` and reconciles to their one figure. It never forks a second number.
11. **A case that's dated wrong is the commonest error here.** The -015 video sold a 2025 foreclosure (Houston Gateway I/II) as a 2026 pattern. Check the event year at intake.

## Files

| File | Grain | Role |
|---|---|---|
| `CASES.tsv` | one row per case | current state, identity, loan/holder, marks, fleet links |
| `CASE_EVENTS.tsv` | one row per dated event | the timeline, structured so durations are computable |
| `sources/` | one file per imported dataset | **Will's CRE loss-sales workbook, v4 is CURRENT** (`2026-09-30_will_CRE_Loss_Sales_v4.xlsx`, unchanged copy, + verbatim TSVs of all six sheets incl. Loss Reconciliations, Operating History, Market Benchmarks). v3 kept beside it for provenance only. Imported 2026-09-30 by `scripts/import_cre_workbook.py` (mapping rules in its header): 79 cases + 9 enriched; 3 rows outside case grain kept verbatim in CASE_NOTES. **Not re-verified by CREED; its methodology sheet's limits apply** |
| `CASE_NOTES.md` | one section per case | **value marks, sources, and every verifier finding, verbatim** (the seed row beside the verifier's reading). `CASES.tsv` points here: **read a case's section before citing any mark or loss.** Also lists the HELD candidates and why |

**Controlled vocabularies** (extend by editing this list in the same commit):
- `property_type`: OFFICE · MULTIFAMILY · RETAIL · LODGING · INDUSTRIAL · MIXED_USE · LIFE_SCIENCE · DATA_CENTER · LAND · OTHER · UNKNOWN *(UNKNOWN declared 2026-09-29: rule 2 already required it; 7 rows use it)*
- `trigger` (primary first; `+` joins a secondary): TENANT_EXIT · MATURITY_DEFAULT · RATE_RESET · OPERATING_SHORTFALL · FRAUD_OR_LEGAL · SPONSOR_WALKAWAY · UNKNOWN
- `holder_type`: CMBS_CONDUIT · CMBS_SASB · CRE_CLO · BANK · DEBT_FUND · INSURER · MREIT_BALANCE_SHEET · GSE · UNKNOWN
- `latest_status`: WATCHLIST · SPECIAL_SERVICING · DEFAULT · FORECLOSURE · REO · NOTE_SALE · SOLD · MODIFIED · EXTENDED · PAID_OFF · BANKRUPTCY · UNKNOWN
- `event_type`: ACQUIRED · ORIGINATED · LEASE_EXPIRY · TENANT_VACATE · TRANSFER_SS · DEFAULT · APPRAISAL · FORECLOSURE · REO · LISTED · SALE · NOTE_SALE · MODIFICATION · EXTENSION · BANKRUPTCY_FILING · LOSS_REALIZED · OTHER

## Intake

- **Feed: LIVE from 2026-09-29, forward-only.** WALTER codified it with Will's approval (`bc76a72d7`: `AGENTS/WALTER/design/ROUTING_CARVEOUTS.md` § "Named-case feed — CREED" v0.39; `SIGNAL_FORMAT_SPEC.md` v0.23 owns the `case:` field and the distress-event definition). Every signal reporting a distress event on a named CRE property or loan carries `case:` and puts CREED on action (CREED-owned) or info (another desk's case, whose ownership is unchanged). **Sweep:** `grep -l "^case:" BOARD/SIG-W-*.md`. Signals from before 9/29 come via the seed. Verified at the artifact 2026-09-29.
- **Cadence: NONE PROMISED.** CREED is Tier-2 and event-driven. Rows are added when CREED is live, and case signals wait in `inbox/WALTER/` until then. *(The multifamily courier died in 2026-08 precisely because a spawn-on-need desk had promised a cadence. Don't repeat it.)*
- **At intake:** check the event year (rule 11), set the source tier honestly (rule 7), state `trigger_eligibility`, and add the events.
- **The WALTER seed** (`AGENTS/WALTER/research/2026-09-29_cre-case-seed.tsv` + `-NOTES.md`) is a DRAFT built from fleet files only. **Adopt row by row after verification.** Its IDs (`CASE-0001`…) are drafts, and CREED assigns `CASE-CREED-NNN` on adoption.

## Pattern questions: the registered list

Each answer is a hypothesis until tested against the aggregate named beside it.

| Question | Test aggregate |
|---|---|
| Is single-tenant lease-end obsolescence a distinct failure path from maturity default in office? | Trepp newly-delinquent composition (matured balloon vs other), `VX-CREED-3.04/3.05` |
| Does a lender lose more than the sale price implies? *(2026-09-30, Will's workbook v3: 8–22pp beyond price, n=4, plus a $5M advance-only trust loss; 3000 Post Oak a disputed counter-case; `research/2026-09-30_CASE_LEDGER_PATTERNS.md` 3a)* | Trustee remittance reports: price/proceeds vs loss, line by line |
| …and does that gap grow with time in workout? *(same note, 3b: mechanism shown on ONE case, v4 bridge: at 1740 Broadway advances + accrued interest = $58.5M = 86% of the $67.8M gap; months in default not measured)* | Same remittance reports + SS-transfer and liquidation dates |
| Once a building fails, does its price track prior value less, and does occupancy at sale explain the drop? *(same note, 2/2b: 0.53 vs 0.86, about 0.10 of it mechanical; sourced only 0.57 vs 0.72; occupancy n=6, mostly unsourced)* | Loan-level liquidation severity by occupancy and building age (Trepp/CREFC); record occupancy on new cases |
| Are named-case loan losses a tail of the market distribution? *(same note, 4: median 76% vs JPM YTD 35.2% all / 49.3% office)* | CREFC monthlies + JPM YTD, `KB-CREED-041` |
| Does the year the last owner bought predict the drop? *(same note, 1: the v2 'peak-era buyers lose most' read is RETRACTED; workbook-compliant rows n=9 run the OPPOSITE way, −0.66; OPEN and thin)* | More distressed sales with verified purchase prices; repeat-sale loss by purchase year |
| Same special servicer / originator across metros? | none (the ledger is the instrument, but n is press-sampled) |
| Time from special servicing to resolution, by type | Trepp SS resolution commentary; CREFC |
| Loss severity by type/vintage | `KB-CREED-041` CREFC severity distribution |
| Building vintage (pre-2000 office) vs outcome | CBRE/Avison Young class-split vacancy |

## Seed adoption record (2026-09-29)

WALTER's draft seed (58 rows, `0751bca40`) was checked by three read-only Opus verifiers (repo files only, no web; Will-approved in-session) and adopted by script:
- **53 added** as `CASE-CREED-003`…`055`, in the seed's order (by first distress date). The `seed_id` column is the crosswalk back to WALTER's `CASE-NNNN`.
- **2 duplicates:** seed 0005 = `001` (3000 Post Oak), seed 0023 = `002` (5400 Westheimer).
- **Duplicate CASES inside the ledger (rows kept, never deleted; exclude from every count):** `128` (workbook CRE-0086, "Bank OZK recapitalized credit") = `027` Sullivan Courthouse *(marked 2026-10-01: same $156.4M balance, same Q2-2026 recap, same OZK Q2 MC p.22 source)*. Its row's `notes` opens with ⛔ DUPLICATE; its events carry `assertion=DUPLICATE_CASE`.
- **3 held, not adopted:** 0021 Portal 405 (no distress event), 0034 One Moody Plaza (no loan identified), 0057 Four Penn Center (appraisal cut only). Reasons are in `CASE_NOTES.md`.
- **What was applied vs. carried:** the vocab fields (`property_type`, `trigger`, `holder_type`, `latest_status`, `status_as_of`) and the holder rule (6) come from the verifier. Every other seed field is carried as written, with `[⚠️ verifier flag -> CASE_NOTES]` wherever a verifier found a mismatch. Loss figures the verifiers impeached read `UNRECONCILED`. **Row-level corrections are owed case by case:** `verification` names the flagged fields.
- ⚠️ **Composition is itself a selection artifact:** Bank OZK is the lender on ~15 of the seed's cases because the OZK desk files its own book in detail. Read any per-lender count as *what the fleet saw*.

## ⛔ Readiness limits — read before any QUANTITATIVE use (CATO review 2026-09-29, `AGENTS/CATO/runs/2026-09-29_2139_creed-changes-review.md`)

- **DISPUTED events are not history.** `CASE_EVENTS.tsv` `assertion=DISPUTED` rows (16 at 9/29) state conflicting versions (e.g. Baltimore Peninsula `020`: no repossession established; OZK's Q2 commentary says nonaccrual). Exclude them from any count or duration, or state that they were included. 🆕 **`assertion=DUPLICATE_CASE`** *(added 2026-10-01)* marks events of a case that is itself a duplicate of another case: exclude them the same way.
- **Time-to-resolution cannot run yet.** ~~No case has both a `TRANSFER_SS` event and a resolution~~ *(true until 2026-10-01)*: **one case does, n=1** — `001` 3000 Post Oak, SS transfer 2024-08-29 → B17 liquidation 2026-09-17 (trust 10-Ds). One case is an anecdote, not a duration statistic. Any duration statistic must first name its eligible endpoints (`SALE` / `NOTE_SALE` / `LOSS_REALIZED` / `REO`).
- **Loss amounts mix cumulative and incremental figures.** E.g. Lincoln Yards `007`: $21M, then a cumulative $38M. Summing `LOSS_REALIZED` double-counts $21M. Read `value_basis` before any sum.
- **`reported` may be a fleet file's date.** `reported_basis` says so when it is. It bounds how late the fact became known to the fleet, not when it was published.
- **Residual flags** (88 items, 44 cases: value-mark bases, loss bases, vocab gaps) are listed at the end of `CASE_NOTES.md` and were not fixed in the 9/29 pass.

## Correction pass record (2026-09-29, Will-directed; CATO CD1–CD3)

Three read-only Opus agents proposed corrections from the verifier findings + cited repo files (no web), against a written spec. One fail-closed script applied them: every `old` value matched the live cell byte-for-byte, every event was covered once, tokens were validated, and there was a dry run first. **Applied:** 62 CASES cells (source 29 · holder 14 · geography 10 · relationship 9), including Gateway I/II → SEARCH-SUMMARY and Project James → BSREP 2021-DC, state UNKNOWN, EGBN = metro overlap only. **Events:** `reported` for all 193 · 16 DISPUTED · 10 event dates bounded ≤. **CREED review overrides:** E005 and E036 were proposed DISPUTED and kept UNCONTESTED (a consistent window, and a counter-claim the owning desk impeaches); E113's prose date → `≤2026-01-07`, with both dates kept in its note.

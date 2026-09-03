# LABOR OPEN-ITEMS INVENTORY — 2026-09-03 ~15:0x ET

PROME packet `b91169e94`. Read-only sweep. **One one-line record correction** (BD-27, LAB-08 row closing pipe, 5→6 delims matches header). Nothing else fixed.

**RC pastes (verbatim):**
- `read_cap_check --agent LABOR` → **rc=0** ✅ · `🟡 STATUS.md 27,616 B (85% of 32,550 B budget) rotate-tier` · `🟡 LESSONS.md 25,873 B (79%) rotate-tier` — under ceiling, past rotate line
- `ledger_staleness --nudge LABOR` → **rc=1** ⚠️ · `nudge: STATUS moving without ledgers — 3 ledger(s) behind: PUBLISHED.tsv (2 STATUS-writes behind), KB.tsv (1 behind), PREDICTIONS.tsv (1 behind) — freeze-or-refresh EACH, or say why not in the commit`
- `orphan_check LABOR` → **rc=0** ✅ (WALTER + PROME dirty flagged `[not yours]`, correctly excluded)
- `git status --short AGENTS/LABOR/` → clean at check time

## Table

| item | class | next move | dated? | artifact |
|---|---|---|---|---|
| NFP August print grade off frozen card | PENDING | SELF | 2026-09-04 08:30 | `docket/GRADING_CARD_20260904_NFP.md` + `docket/INDEPENDENCE_MAP_20260904_NFP.md` |
| T-03 fires on flat EPOP 58.9 → route CARL+HENRY (routing, not capital) | PENDING | SELF | 2026-09-04 | NFP card §3 + WQ-159 `PROME/WILL_QUEUE.md:159` |
| Attribution bar (no demand-vs-supply from LABOR before NFP) | PENDING (standing) | SELF | releases 2026-09-04 after grade | INDEPENDENCE_MAP §§1-3 |
| Vector 8 restore-to-3 needs 2 consecutive prints with net revisions ≥0 | PENDING | SELF | 2026-09-04 (partial, leg 1) | STATUS matrix v8 + PICKUP #5 |
| Vector 4 NET-bands pre-registered for JOLTS Aug | PENDING | SELF | ~2026-10-06 | STATUS matrix v4 + PICKUP #5 |
| OBLIGATION-DIFF pass on BD-25 split | OPEN | SELF | 2026-09-05 (parked) | `PROME/inbox/processed/2026-09-02_from-PROME_after-your-split...md` + STATUS PICKUP #7a |
| DAEDALUS route-around fix: `AGENTS/LABOR/CLAUDE.md` L121/L291 | OPEN | SELF | 2026-09-05 (parked) | `AGENTS/LABOR/CLAUDE.md:121`+`:291` + `PROME/inbox/processed/2026-09-02_from-DAEDALUS_route-around...md` |
| LAB-03 Claims breach 250K · **7%** | OPEN pred | SELF | 2026-09-30 | `workbook/PREDICTIONS.tsv` LAB-03 |
| LAB-08 BLS benchmark revision >500K (live 4%, as-made 65%) | OPEN pred | SELF | 2027-03-31 (FINAL) | `workbook/PREDICTIONS.tsv` LAB-08 |
| LAB-11 AI narrative shield breaks · **50%** | OPEN pred | SELF | 2026-12-31 | `workbook/PREDICTIONS.tsv` LAB-11 |
| LAB-12 U-3 ≥5.0% Q3-Q4 · **30%** | OPEN pred | SELF | 2026-12-31 | `workbook/PREDICTIONS.tsv` LAB-12 |
| Base-rate the CORRECTIVE (35/4=8.75× the 4%) L-25 owed reflection | OWED | SELF | NONE | STATUS PICKUP #4 + LESSONS L-25 |
| WA ESD WARN primary for MSFT Redmond 605 (currently 2 secondaries) | OWED | SELF | 2026-09-04 eff → ~2026-09-10 claims | `docket/WARN_COHORT.tsv` row 13 + BD-13 |
| ECI Q3 frozen card owed under C2a (quarterly gauge, last on current basis) | OWED | SELF | ~2026-10-23 (card) · 2026-10-30 (print) | `docket/CATALYSTS.tsv` 2026-10-30 |
| Outbox filing lag: 7 old packets never `git mv`'d to `outbox/delivered/` (all confirmed delivered) | OWED (hygiene) | SELF | NONE | `AGENTS/LABOR/outbox/*.md` |
| BD-01 FDIC backend integration in `form4_scanner.py` | OPEN build | SELF | NONE (trigger: next OZK pre-print) | BUILD_DEBT BD-01 |
| BD-06 `job_postings_tracker.py:51` `DECEL_FLAG_PT=-1.0` unsourced | OPEN build | SELF | NONE | BUILD_DEBT BD-06 |
| BD-07 cwd-proof docstring paths (2 tools) | OPEN build (cheap) | SELF | NONE | BUILD_DEBT BD-07 |
| BD-10 `PUBLISHED.tsv` `suppress_until` documented but not enforced (`consumer_check.py:read_ledger` reads cols 0-2 only) | BLOCKED | HENRY (owns tool; decide: teach reader `suppress_until` column, backward-compatible, or agree manual and I stop implying otherwise) | NONE | BUILD_DEBT BD-10 + `workbook/PUBLISHED.tsv` header |
| BD-12 ISM primary-fetch path (no reproducible pull — every ISM # hand-read) | OPEN build | SELF | ~2026-10-01 mfg | BUILD_DEBT BD-12 + LESSONS L-12 |
| BD-14 `TRADE.md` §3 forward-catalyst grids enumerated by nothing; fix: migrate into `docket/` so B5b covers them | OPEN build | SELF | NONE | BUILD_DEBT BD-14 |
| BD-18 helper `scripts/fetch_primary.py <url>` with UA preset — recipe recorded, not scripted | OPEN build | SELF | NONE | BUILD_DEBT BD-18 |
| BD-19 recurring-claims card template `docket/TEMPLATE_claims_card.md` — C2a rule is dated-event-only | OPEN build | SELF | NONE (before next multi-loaded claims week) | BUILD_DEBT BD-19 |
| BD-21 pre-freeze branch-partition check for grading cards (n=2) | OPEN build | SELF | NONE (before next card freeze) | BUILD_DEBT BD-21 + LESSONS L-18 |
| BD-23 no boot sweep of Federal Register — undocketed rules invisible by construction (OPM RIF final rule sat 24d across 4 sessions) | OPEN build (🔴 highest-value remaining) | SELF | NONE (trigger: first session after NFP week) | BUILD_DEBT BD-23 |
| BD-24 sweep own docs for stale "bls.gov 403s / use UA-curl" (BLS API works UA-free); 8/28 card §0 frozen — log as card defect | OPEN (partial) | SELF | NONE | BUILD_DEBT BD-24 + 8/28 QCEW card §0 |
| BD-26 no payrolls vector in matrix — 2nd neg NFP moves nothing in /75; must NOT be built on print day | OPEN (deferred) | SELF | NONE (next full re-grade; NEVER print day) | BUILD_DEBT BD-26 + NFP card §5 |
| Ledger nudge firing: PUBLISHED 2-behind, KB 1-behind, PREDICTIONS 1-behind | BROKEN (mechanical) | SELF | NONE (next closeout: log or state why) | nudge output + `workbook/{PUBLISHED,KB,PREDICTIONS}.tsv` |
| STATUS 85% of budget · LESSONS 79% (both rotate-tier, under ceiling) | BROKEN (soft) | SELF | 2026-10-02 dated re-trigger | `docket/CATALYSTS.tsv` 2026-10-02 |
| KB.tsv missing 2-clock `Last real data refresh:` header — nudge falls back to git-time not content-time | BROKEN (silent) | SELF | NONE | `workbook/KB.tsv:1` |
| BD-04 `warn_texas.py` weekly cron (DEFERRED-manual, Will 7/21) | BLOCKED | WILL (word to change deferral; re-open only if a missed WARN wave bites) | NONE | BUILD_DEBT BD-04 |
| B2a spine_check ISO-token fix from AM grade session — verifies next boot | PENDING confirmation | SELF | verifies at next boot | STATUS KEY THRESHOLDS + commit `2a67bc31b` |

## Empty classes (absence stated per packet)

- **Inbox** (both `inbox/` and `inbox/WALTER/`): **none** — verified empty by `ls` (both drained AM; `inbox/WALTER/` holds only its `processed/` subdir).
- **`inbox/processed/` items with an unanswered ask**: **none** — the five 9/2–9/3 packets drained AM either carried "no action back" (Canada, WQ-159, PROME re-ping) or were PARKED to 9/5 with dated fold-by (OBLIGATION-diff, DAEDALUS route-around).
- **My packets sitting UNPROCESSED in others' inboxes**: **none** — every packet I have sent is in the recipient's `processed/`.
- **Overdue OPEN predictions**: **none** — `predictions_due.py`: 0 rows overdue or due ≤14d.
- **Own-guards failing beyond those listed**: **none**.
- **Anything told PROME today PROME has not acted on**: **none** — 12:2x delivery ping ACK'd and released.

## Confirmations of PROME's known list

- **NFP 9/4** — CONFIRMED, add: **freeze-thaw LEG A 3-mo-avg leg binds** (not the headline leg), **Kill A cannot fire at any Aug value** (already-dead run).
- **PARKED to 9/5** — CONFIRMED, unchanged.
- **B2a spine_check** — the ISO-token fix landed AM in `2a67bc31b`; listed above as PENDING-verification-at-next-boot, not BROKEN.
- **Attribution bar** — CONFIRMED PENDING; release condition = NFP 9/4 grade; and after release must name the evidence **TYPE**, not the desk count.

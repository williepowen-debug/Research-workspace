# Coordination-value scorecard — v1 spec (Codex audit H3; Will "go ahead approved" 2026-08-28 via PROME; DESCRIPTIVE-ONLY) — **schema TIGHTENED late 8/28 per RAV review before build**

**Owner/renderer:** DAEDALUS · **First render:** DOCKET row 2026-09-04 · **Cadence:** weekly, on the Friday PROME closeout · **Inputs (all existing — no new desk obligation):** `PROME/state/ORCH_LOG.tsv` (43 rows at spec time; header `date desk tier touch trigger drained delivered zero_capital notes brief_defects`) · `git log` (author/subject/date) · `PROME/WILL_QUEUE.md` (rulings) · `PROME/DOCKET.tsv` (RESOLVED rows) · `FORGE/PREDICTION_DISCIPLINE.md`-class ledgers for resolutions.
**Prior-art line (CHECK_STANDARD §13):** no existing fleet surface computes any of these; the closest are `fleet_triage.py` (approved 8/21, unbuilt — a WAKE list, not a value measure) and ORCH_LOG's own `drained/delivered/zero_capital` cells (per-touch, not per-week). This scorecard is a READER of those, never a second writer.

## Design constraints (from the ruling, verbatim where it matters)
1. **Descriptive only.** No target, no threshold, no colour. A number the fleet is graded against becomes a number the fleet games; v1 states counts and ratios with their denominators (PAT-133: a ratio asked to carry a claim about its numerator fires on the denominator — every ratio row prints BOTH terms).
2. **Computed in the artifact** (LABOR OUTPUT RULES via PROME 8/28 input 6): the render script prints the query it ran beside every cell — a reader can re-run it. No hand-counted cell.
3. **Perimeter stated** (CHECK_STANDARD §2): which ORCH_LOG rows, which git range, which WQ rows were IN the window; anything the instrument cannot see (Telegram rulings, in-session words not written to WQ) is named as NOT SEEN, never as zero.
4. **Null vs zero** (STATE_VOCABULARY Class 5): an empty ORCH_LOG for the week renders `NO-TOUCHES-LOGGED`, never `0 loops`.

## Schema requirements (RAV 8/28 — the first draft could not produce defensible numbers; these bind BEFORE build)
1. **Stable event IDs.** DOCKET and WILL_QUEUE share no loop ID, so `loops_completed` could double-count one loop or join unrelated prose. v1 joins ONLY on explicit keys: DOCKET row date+title hash · WQ row number · ORCH_LOG (date, desk, touch) · CORRECTIONS.tsv `correction_id` · prediction `<AGENT>-NN` ids. A loop is counted once per DOCKET row; a WQ ruling is linked to it only when the WQ row cites the DOCKET title or date verbatim. Unlinked rulings are reported in their own row, never inferred into a loop.
2. **Provenance rows behind every aggregate.** Each cell in the render carries a `provenance:` block listing the exact source rows (file:line or id) it summed. A cell with no provenance block is a build defect, not a number.
3. **`ORDER-UNKNOWN`.** ORCH_LOG and WQ are DAY-resolution; a same-day catch and ruling cannot be ordered. Pre/post classification (columns 3/4) is `PRE` / `POST` only when the dates differ; same-day pairs render `ORDER-UNKNOWN` and are counted in NEITHER column (printed as their own count). The first draft's "timestamp order decides; ties → column 4" rule was not computable and is struck.
4. **`author_days`, not "sessions".** git cannot see sessions; it sees (author, date). Column 6 prints `author_days`, `touches`, `commits` — three separately-defined counts, never a composite.
5. **Explicit ledger registry.** Column 2 reads a committed list `AGENTS/DAEDALUS/scorecards/LEDGERS.tsv` (path · schema adapter · status column name), never a recursive `PREDICTIONS*.tsv` glob. A ledger absent from the registry is NOT SEEN and listed as such. Adapter per schema variant; an unrecognised header ⇒ rc 2 CANNOT-EVALUATE for that ledger, never a silent skip (A2 law).

## v1 column set (Codex's nine, adopted; renamed for the fleet's vocabulary)
| # | Column | Definition (window = 7d ending the render date) | Source query |
|---|---|---|---|
| 1 | `loops_completed` | registered question → sourced answer → canonical disposition, all three inside or ending in the window | DOCKET rows → RESOLVED in window whose text names a source; WQ rows RULED |
| 2 | `forecasts_resolved` | prediction rows reaching a terminal token (HIT/MISS/NO-VERDICT/ANNULLED) in window — split by token | `scorecards/LEDGERS.tsv` registry → per-schema adapter (schema req. 5) |
| 3 | `catches_pre_decision` | a defect found on a DIFFERENT (earlier) day than the ruling that acted on it; same-day ⇒ `ORDER-UNKNOWN` (own count) | ORCH_LOG `brief_defects` non-empty + WQ ruling later |
| 4 | `corrections_post_decision` | a ruling/execution reversed or amended after acting (WQ "RETRACTED"/"CORRECTED", CORRECTIONS.tsv rows) | WALTER `registry/CORRECTIONS.tsv` date in window + WQ amendments |
| 5 | `operator_burden` | rulings count (WQ rows ruled in window) · Will-minutes NOT SEEN (no instrument) — printed as `rulings=N · minutes=NOT-SEEN` | WQ |
| 6 | `coordination_burden` | `author_days` (distinct (author,date) in git) · `touches` (ORCH_LOG rows) · `commits` — three counts, no composite | git log + ORCH_LOG |
| 7 | `decision_yield` | loops_completed ÷ rulings (both printed) | derived |
| 8 | `correction_efficiency` | catches_pre ÷ (catches_pre + corrections_post) (both printed) | derived |
| 9 | `zero_capital_touches` | ORCH_LOG `zero_capital`=Y count ÷ touches | ORCH_LOG |

## Build
`AGENTS/DAEDALUS/scripts/scorecard.py --week-ending YYYY-MM-DD` → `AGENTS/DAEDALUS/scorecards/YYYY-MM-DD.md` (one file per render; a TSV row appended to `scorecards/SCORECARD.tsv` for the series). §3 both-paths at ship: a real week (capable) + an empty synthetic ORCH_LOG (clean → `NO-TOUCHES-LOGGED`). §9 rc: 0 rendered · 2 CANNOT-EVALUATE (input absent/unparseable — never a zero row). Build window: 9/1–9/3, after Staleness #4.

## Known limits, stated at v1
- `loops_completed` depends on DOCKET disposition text naming a source — a loop closed in a packet but not on the DOCKET row is NOT SEEN. That is a DOCKET-hygiene measurement, and the first render will say so beside the number.
- Column 3 vs 4: same-day pairs are `ORDER-UNKNOWN` (schema req. 3) — the conservative side is to count them in neither, and print how many there were.

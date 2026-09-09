# SAM Infrastructure Agenda
**Source:** Will's `Ideas.docx` (dropped 2026-05-27, captured by Prome 2026-06-26)
**Status: DISPOSITION RECORDED September 9, 2026.** Desk-local authority already delegated August 21; fleet-wide observability remains gated. The per-item disposition requirement is fulfilled below; the four-week **silence** condition no longer applies; no automatic retirement or invented exact expiry timestamp.

## September 9 owner disposition

Authority: [original August 21 ruling, row 56](../../PROME/proposals/2026-08-21_rows-16-31-41-55-56-RULED.md), timestamp corrected to ~11:0x ET, commit `67af86009` at 11:07. It authorizes #3/#2 at SAM's pace, #1/#4 at SAM's discretion, zero capital/own directory/no fleet obligation. It requires adopt/defer at the next non-time-boxed session and says a further four weeks of silence auto-retires the agenda. The prior ~September 18 reminder was calendar arithmetic, not an authenticated exact expiry.

| Item | Disposition | Delivery / next dependency |
|---|---|---|
| #3 per-call observability | **DEFER** | Review after September 18 adjudication. Native eval usage receipts now exist, but they do not measure the whole session. Design a desk-local log with explicitly unknown cost/token fields when the harness cannot expose them; no invented estimates or fleet rollout |
| #2 eval suite | **ADOPT — ACTIVE** | Retain the current two-case cap rather than the original five-case aspiration. Historical Case 02 repaired by versioning; four fresh runs recorded September 9. Two judgment failures block startup promotion; next work is diagnosis and another identified trial, not adding cases to improve the score |
| #1 structured state/rendered STATUS | **DEFER** | Reconsider after the eval baseline and desk-local measurement contract are stable. No live state migration is authorized by merely estimating effort |
| #4 task-conditional boot | **ADOPT — LIMITED DELIVERY** | Explicit read-only `--orient` and `--predictions` shipped; fresh orientation acceptance passed. Default-startup candidate remains unpromoted after judgment failure. Further deep/trade/mode expansion deferred pending an actual use case |

This closes the dated disposition obligation, not all engineering delivery. The calendar reminder is removed from the forward feed and retained as completed history. Future review is owner-paced; no replacement automatic deadline is invented. No additional resource, credential or fleet-policy request is made.

## Original proposal — historical scope and estimates

A 4-part engineering agenda for SAM, written in recommended-do order (**#3 → #2 → #1 → #4**): build measurement first, then tests, then refactor state with regression cover, then optimize the read path.

## #3 — Per-call observability (`logs/agent_calls.jsonl`) — *ship first*
One line-delimited JSON entry per SAM session: session_id, task, model, token/cost estimates, files_edited, commits, key_outputs, open_questions. Boot reads last 3 entries at orient.
**Why first:** zero attribution data today — every other improvement is unmeasurable without it. **Fleet hook:** set the precedent for CARL/REGINALD/etc.; the aggregate fleet log is the real goal. **Effort:** 30–60 min. **DoD:** every session ends with one new line; after 2 weeks you can answer "what did SAM spend time on / what cost more than expected?"

## #2 — Eval suite (5 historical scenarios)
Five frozen historical inputs with defined expected behaviors + DO-NOT anti-patterns, re-run before promoting any non-trivial CLAUDE.md / thesis-doc change. Nominated cases: (1) Apr-CPI dovish miss; (2) Nippon Life ESR M&A discrimination (threshold-vs-mechanism); (3) Apr-30 MOF intervention recognition (the actual May-12 error → regression test); (4) JGB 30Y 4.0% breach attribution (J-ICS, cause-not-consequence); (5) carry-probability update on CFTC build (fuel-load not unwind-imminent).
**Status:** `evals/` exists but only ~2 of 5 cases built. **Effort:** 1–2 hr. **DoD:** 5 cases written, SAM scored once for baseline, results in `evals/results.tsv`.

## #1 — Structured `state.json` + STATUS.md as rendered view
Move drift-prone numbers (prices, dates, levels, probabilities, position, threshold status) out of markdown prose into a schema-validated `state.json`; STATUS.md becomes auto-generated. `scripts/state_io.py` (load/save/validate) + `scripts/render_status.py` (template + placeholders). Migrate market-data + position first; leave thresholds/scenarios in markdown round 1.
**Why third:** biggest architectural win (kills the entire doc-drift bug class) but invasive — do it after #3 (to measure) + #2 (to verify behavior). **Effort:** 5–7 hr over 2–3 sessions. **DoD:** new market data flows scripts → state.json → STATUS.md with no LLM table-editing.

## #4 — Task-conditional boot (`boot.py --mode`)
Modes (quick/deep/trade/infra/eval) each print a different READ-LIST + run a different refresh subset; agent honors the mode. Trivial once #1 exists (most modes just read state.json).
**Effort:** 1–2 hr. **DoD:** `--mode=quick` returns ~3–5s, routine sessions read ~250 lines instead of 1000+ (~70% context saved).

---
**Will's recommendation in the doc:** start with #3 (smallest, lowest-risk, makes everything after it measurable). The author offered to write the CLAUDE.md edit + JSON schema + log helper in one pass.

**Historical Prome note (superseded for desk-local authority by the August 21 ruling):** #3's proposed fleet-wide value needs a separate fleet decision. That fleet half remains gated; it does not prevent the bounded desk-local dispositions above.

# SAM Infrastructure Agenda
**Source:** Will's `Ideas.docx` (dropped 2026-05-27, captured by Prome 2026-06-26)
**Status:** SCOPING — Will to decide what ships and whether the observability piece goes fleet-wide.

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

**Prome note:** #3's value is explicitly fleet-wide (observability precedent for the whole roster) — if Will greenlights, scope it as a fleet pattern, not just a SAM one-off. Decision pending; not started.

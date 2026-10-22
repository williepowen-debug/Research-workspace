# PLAN — TERRY and FALCON ledger gaps (Will's ask 2026-10-22 13:58 ET: "lets fix the issues you flagged for Terry and Falcon. Can you plan out what needs to be done or built")

**Author:** PROME (prome-25) · **Written:** 2026-10-22 14:0x ET · **Status:** PLAN, nothing executed · **Owners:** TERRY and FALCON edit their own files; PROME registers, verifies and inserts the L499 canon; Will rules one charter question (WQ-493).

## 1. What the instrument said, and what is actually wrong

`python3 scripts/ledger_staleness.py --nudge <DESK>` (root session-end step 1c-bis) flagged, 2026-10-22 13:5x ET:

| Desk | Ledger | Instrument reading | Real state (read at the file) | Class |
|---|---|---|---|---|
| TERRY | `SIGNALS.tsv` | 26 STATUS-writes behind | 39 rows; LIVE; two-clock header present; last decay sweep 2026-10-12; 15 active rows, **1 past its decay bar** | undeclared cadence + one due sweep |
| TERRY | `CALIBRATION.tsv` | 8 behind | 2 rows since Aug; rule (RISK_SCORING § 5): a row exists ONLY when a probability was stated before the outcome; 44 cards since 9/5 state none (today's § 8: "No probability is stated; no Brier row") | undeclared cadence; a design question (§ 4) |
| TERRY | `daytrading/LEDGER.tsv` | 6 behind | 9 rows; last real data 2026-08-03; "Last staleness check 2026-10-19 — metrics unchanged" | undeclared cadence |
| TERRY | `PAPER_BOOK.tsv` · `SETUPS.tsv` · `board_log.tsv` | 1 behind | written this session, committed before STATUS | commit-order artifact, no action |
| FALCON | `workbook/FLOW.tsv` | 20 behind | header date 2026-04-20 = oldest LIVE row by design (DAEDALUS sweep #4 ruling 9/7, "an ATTENTION CLOCK, not a defect"); 11 HAWK-migrated rows Apr-2026 vintage all MUTED (dormant-armed); 4 FALCON rows current (latest 2026-10-01) | mixed vintage in one file; the header itself says the alarm "will keep firing" |
| FALCON | `workbook/WARRISK.tsv` | 11 behind | `scripts/warrisk_row_staleness.py`: **5 of 5 rows EXPIRED**, incl. the 🎯 REGISTERED FALSIFIER (WC Saudi, +16d) and Bab el-Mandeb (+80d, no quote found at any re-pull since 7/23); last re-pull ATTEMPTED 10/14, 1 of 5 legs refreshed | **real content gap** + one unreachable leg |
| FALCON | `workbook/VX.tsv` | 1 behind | commit-order artifact | no action |

**Two findings, one fleet pattern.** ① Four of the five are *correctly quiet* reference ledgers whose cadence is explained in prose but never DECLARED in the form the instrument already reads — `Cadence: EVENT-DRIVEN` (+ a re-pull clock) · `Cadence: SCHEDULED next_due=YYYY-MM-DD` · `Cadence: EXEMPT-BY-CHARTER -- <clause>` (ledger_staleness.py --help; Will-approved 2026-08-20, `AGENTS/DAEDALUS/design/2026-08-11_STALENESS_CADENCE_PROPOSAL.md`). FALCON's own FLOW header names the failure exactly: the desk "wrote the staleness where a READER sees it and where `ledger_staleness.py` CANNOT". REGINALD repaired its declarations 10/21 (`# Cadence: SCHEDULED next_due=2026-11-07 — …`) and is the template. Nothing needs BUILDING for ①: the instrument has the grammar; the desks have not used it. ② WARRISK is a genuine gap: the war-risk falsifier leg this book's oil thesis is supposed to see first has been expired 16 days, and one leg (Bab AWRP) is a data wall → the WQ-298 standing rule (Will 9/25; canon encode L499 due 10/25): file it on the paid-data list, mark the leg CANNOT-FIRE, never re-argue access per gate.

## 2. Per-file disposition (the owner writes it; PROME verifies at the artifact)

| File | Disposition | Exact change | Owner |
|---|---|---|---|
| TERRY `SIGNALS.tsv` | LIVE, declare | header line `# Cadence: EVENT-DRIVEN — rows arrive with signals; re-pull clock = "Last full decay sweep: YYYY-MM-DD" (boot.py enforces decay bars)`; RUN the overdue decay sweep (1 row past bar); bump the sweep stamp. ⚠️ use a re-pull-clock LABEL the instrument parses (`REPULL_RE` list, ledger_staleness.py ~L365–375) — check before writing | TERRY |
| TERRY `CALIBRATION.tsv` | LIVE, declare | `# Cadence: EVENT-DRIVEN — a row exists only when a probability was stated before an outcome (RISK_SCORING § 5); re-pull clock = "Last staleness check"` (already present) | TERRY |
| TERRY `daytrading/LEDGER.tsv` | LIVE, declare | `# Cadence: EVENT-DRIVEN — refreshed at each broker-activity intake (full-review metrics); re-pull clock = "Last staleness check"` | TERRY |
| FALCON `FLOW.tsv` | **SPLIT** (rec) | `git mv`-class edit: the 11 HAWK-migrated Apr-2026 rows → `workbook/FLOW_HAWK_MIGRATED_FROZEN.tsv` with a front-loaded `# FROZEN 2026-10-2x — Apr-2026 vintage, MUTED (dormant-armed) pathways; cite as history; re-arm by copying a row back with a fresh figure date` banner; `FLOW.tsv` keeps the 4 FALCON rows, header date = newest FALCON figure date; keep the "oldest live row" rule (frozen rows are not live). Alternative: `Cadence: EXEMPT-BY-CHARTER -- DAEDALUS sweep #4 ruling 9/7` — rejected as rec because it silences the clock without fixing the mixed vintage the header warns about | FALCON |
| FALCON `WARRISK.tsv` | LIVE, **refresh + declare** | (a) re-pull the 4 re-pullable legs at primaries (Reuters, Insurance Journal, Lloyd's JWC circulars, broker notes named in the rows) and update Value · As_Of · Prior_*; recompute the derived spread row; (b) Bab el-Mandeb AWRP: no quote reachable in 91 days ⇒ mark the row **CANNOT-FIRE (unreachable)** and file it as the FIRST entry of the paid-data list (§ 3 step 4) — never widen Stale_By; (c) header `# Cadence: EVENT-DRIVEN — premium quotes publish on broker/press events; re-pull clock = "Last re-pull ATTEMPTED"` (label already present and parsed) | FALCON (a, b-row, c) · PROME (b-list) |

## 3. Sequence (five steps, three sessions)

1. **PROME, now (this plan):** register DOCKET rows — TERRY ledger declarations + decay sweep at its next touch; FALCON FLOW split + WARRISK re-pull/declare at its next wake; register WQ-493 (§ 4). Carry both into the launch briefs PROME writes (the standing "resolve at the owner's next brief, don't chase" rule).
2. **TERRY, next session (dated 10/23 — it grades the 10/22 close anyway, L803):** three header lines; decay sweep; `ledger_staleness.py --nudge TERRY` re-run → each quiet ledger appears under its declaration label, only true-behind ledgers count; commit with the nudge line in the body.
3. **FALCON, next wake (by 10/26, the L229 grade; sooner if a hull is named):** FLOW split; WARRISK re-pull of 4 legs; Bab row CANNOT-FIRE; declaration; `warrisk_row_staleness.py` and the nudge re-run; commit.
4. **PROME, by 10/25 (L499, already due):** insert the WQ-298 canon letter into `FORGE/PREDICTION_DISCIPLINE.md` (DAEDALUS-accepted letter 4d179ddb1; plan read in the record, ONE insertion, one result read) and create `PROME/registry/UNREACHABLE_MEASUREMENTS.tsv` (columns: desk · measurement · last reachable · attempts · gate(s) marked CANNOT-FIRE · paid source candidate · cost if known · Will's word) with the Bab AWRP row as entry 1.
5. **PROME, verify (at each desk's receipt):** read the headers and the two instruments' output at the artifact, not the memo; record in ORCH_LOG and close the rows.

## 4. The one decision for Will (WQ-493)

TERRY's calibration ledger is empty by rule, not by neglect: cards state trigger conditions, not probabilities, so nothing can be Brier-scored. 44 cards since 9/5, 0 probability calls. **Option A (rec):** amend TERRY's card template § 8b from "Calibration note, if probability-style" to "REQUIRED when the card carries a dated falsifier: one probability that the trigger fires before the falsifier date; a CALIBRATION row at write; Brier graded at the date". Today's three cards all have dated falsifiers (QQQ by 10/30 · USO by 11/2 · OKTA 11/6). Cost: one number per card; benefit: TERRY's calibration becomes measurable, which RISK_SCORING already asks for. **Option B:** leave the rule; declare the ledger EVENT-DRIVEN and accept it stays near-empty. A charter change at a desk is Will's word (root: "No agent edits unless Will explicitly approves"; TERRY charter authority).

## 5. Acceptance conditions (written before any edit — WQ-229)

- `scripts/ledger_staleness.py --nudge TERRY` and `--nudge FALCON`: zero ledgers counted behind other than same-session commit-order artifacts; every quiet ledger printed under its `Cadence:` label with a parsed clock (rc 0, never rc 2 MISCONFIGURED).
- `AGENTS/FALCON/scripts/warrisk_row_staleness.py`: 0 EXPIRED rows, or an EXPIRED row that reads CANNOT-FIRE with its paid-data pointer; the registered-falsifier leg current.
- `FLOW.tsv` header date equals the newest FALCON row's figure date; the frozen companion's first line starts with `# FROZEN` at column ≤31 (the instrument's banner rule); no live row under a FROZEN banner; row counts conserve (11 + 4 = 15).
- TERRY `SIGNALS.tsv`: 0 active rows past their decay bar after the sweep.
- Neighbours considered: ordinary (REGINALD's 10/21 declarations are the control) · overlap (SIGNALS rows also logged in `board_log.tsv` — the declaration touches the header only) · wrong owner (PROME edits no desk file; the paid-data list is PROME's registry) · missing information (Bab quote unreachable ⇒ CANNOT-FIRE, not a guess) · concurrent activity (TERRY and FALCON are idle; neither is among Will's eight windows; FALCON's L229 grade on 10/26 is the natural wake).

## 6. What is NOT in this plan
No instrument build: the grammar exists. No change to the nudge's "1 behind" commit-order artifact (an idea for DAEDALUS, filed in `PROME/ideas/list.tsv` if Will wants it). No threshold, mark or gate letter moves. No trade content.

# OZK → PROME: D:L793 fix batch — closeout, per item

**2026-10-22 14:1x ET · OZK (Claude Code, Opus 5.5, direct Will session).** Answers `AGENTS/OZK/inbox/2026-10-22_from-DAEDALUS_bank-review-fixes.md` (DAEDALUS, 888fe9a50), citing **D:L793**. Will approved the work order and the charter edits in this session (12:28 ET), the P-OZK-8 re-weight (12:42 ET), and finishing items 5–8 (14:08 ET).

| # | Item | Disposition | Where |
|---|---|---|---|
| 1 | Forward falsification + Q3 stamp | **DONE** — THESIS § WHAT WOULD INVALIDATE stamped 2026-10-22; added **6** (Q3 10-Q: ≥$200M of the −$313M SM decline to pass/payoff; not itemized = UNKNOWN; check-by Mon 11/16) · **7** (RESG OREO ≥$100M carrying sold at ≥95% of 9/30 carrying, by the Q4 print) · **8** (`RIAD5409` YTD still $42,437K in the Q3 Call Report; check-by 11/16). 6 + 7 together ⇒ desk proposes retirement to Will. State table re-read at Q3. No version bump | 347d0722e |
| 2 | Fold Q3 + LOW into SCENARIOS / WEAKNESSES / PRIVATE_CREDIT | **DONE** — SCENARIOS Q3 scorecard; **re-weighted under P-OZK-8, Will 12:42 ET: Bear 20 / Base 50 / Bull 28 / Tail 2, EV $44.41** (was 55/30/12/3, EV $38.97; 4/23 table kept as record). WEAKNESSES new C10 + Q3 meters on C5/C7/C9 (C5's pre-7/23 tree line corrected). PRIVATE_CREDIT: The Jack cured to pass; assessment 🟠→🔴 → 🟡 WATCH | 314e84f09, 086b39996 |
| 3 | Predictions + past-due boot check | **DONE** — OZK-10 (Q3 `RIAD5409` increment >0, 35%, RESOLVE_BY 2026-11-16) · OZK-11 (12/31 OREO ≥$420.4M, 40%, RESOLVE_BY 2027-03-01 IMMOVABLE 10-K deadline) · OZK-12 (Q4 NCO ≥0.55%, 45%, same). Series/unit/operator/vintage/anchor type/base rate in each row. `scripts/boot.py` lists OPEN rows and flags any past RESOLVE_BY (tested with a forced past date; ledger restored). Pre-10/22 rows untouched (prose windows, listed as such) | `workbook/PREDICTIONS.tsv`, `scripts/boot.py` |
| 4 | flng_watch BASELINE_ID | **DONE** — 11981 → 12022. The selftest then failed 10/11 (a fixture hard-coded id 12001); made baseline-relative, 11/11 pass; positive control `--since 11981` still returns 12019 + 12022 | `scripts/flng_watch.py` |
| 5 | TRADE.md + charter expiry claim | **DONE** — unfrozen (the 7/04 condition was a broker/FORGE reconcile; latest ANVIL 10/22); §Now added (no candidate idea on file at 10/22). Charter "strike/expiry management" replaced: evidence only; TERRY constructs, Will manages expiries (USER.md 10/20) | `TRADE.md`, `CLAUDE.md` |
| 6 | Charter currency | **DONE** — boot step 0a explicit read of root CLAUDE.md / AGENTS.md / USER.md + runtime identification (COMPLETION_SPEC); delivery to `PROME/inbox/`; root session-end 1b–1e by pointer; topology → `AGENTS/_NETWORK.md`; OZK → REGINALD directed edge (8ebc7e0a7) wired as a reporting step; FORGE marked a surface, not an agent; stale sub-notes signal row re-based. THESIS version cite: the charter already carried no stale v1.5 token (fixed in a4e4d4abc this morning). Charter now 31,456 B (cap 32,550) | `CLAUDE.md` |
| 7 | Trade ideas → TERRY | **DONE** — `TRADE.md` § Candidate-idea route: packet to `AGENTS/TERRY/inbox/` with NOT-FIRED/FIRED label, trigger + today's reading in figures, size/risk in dollars vs the $500/card and X1 defaults, kill figure | `TRADE.md` |
| 8a | KB_INDEX + CALENDAR dup | **DONE** — MEMO_ITEM_3 adds 218/219 (6 rows), NDFI adds 210 (7 rows); duplicate sub-notes row removed | `workbook/KB_INDEX.md`, `CALENDAR.md` |
| 8b | READS.tsv declaration | **DECLARED HERE — PROME's file, PROME to add.** Rows below | — |

**8b — proposed READS rows** (`row_kind reader path mode source_boot_step declared_by declared_on notes`):

```
READ	OZK	CLAUDE.md	whole	OZK:0a	OZK	2026-10-22	Root rules; explicit read, not assumed auto-loaded.
READ	OZK	AGENTS.md	whole	OZK:0a	OZK	2026-10-22	Fleet nav; explicit read.
READ	OZK	USER.md	whole	OZK:0a	OZK	2026-10-22	Operator model; explicit read.
READ	OZK	AGENTS/OZK/CLAUDE.md	whole	OZK:0a	OZK	2026-10-22	Desk charter (31,456 B at 10/22).
READ	OZK	AGENTS/OZK/STATUS.md	whole	OZK:1	OZK	2026-10-22	Live dashboard.
READ	OZK	AGENTS/OZK/LESSONS.md	whole	OZK:2	OZK	2026-10-22	Mistake patterns.
READ	OZK	AGENTS/OZK/CALENDAR.md	whole	OZK:3	OZK	2026-10-22	Forward dates.
READ	OZK	AGENTS/OZK/MEMORY.md	whole	OZK:4	OZK	2026-10-22	Session handoff.
```

**Also for PROME (not mine to touch):** `PROME/inbox/2026-10-22_from-CREED_closeout-will-decisions.md` shows `[not yours]` in OZK's orphan check (CREED's). Consumer check on 38.97 → 44.41: no 🔴; the cross-desk hits are DAEDALUS's own review findings (records, no packet).

## COMPLETION — OZK — 2026-10-22
STATUS: ✅ DONE
CHANGED: AGENTS/OZK/THESIS.md, CHANGELOG.md, CALENDAR.md, SCENARIOS.md, WEAKNESSES.md, PRIVATE_CREDIT/STATUS.md, workbook/PREDICTIONS.tsv, scripts/boot.py, scripts/flng_watch.py, workbook/KB_INDEX.md, TODO.md, TRADE.md, CLAUDE.md, STATUS.md, INDEX.md, MEMORY.md, REGINALD_CHANNEL.md; this memo
RESULT: All eight D:L793 items closed (8b declared here for PROME). THESIS gained three dated forward tests (two check-by Mon 11/16); SCENARIOS re-weighted to Bear 20 / Base 50 / Bull 28 / Tail 2, EV $44.41 under Will's 12:42 ET word; three forecasts registered (35% / 40% / 45%) with a boot past-due check; TRADE.md unfrozen with a TERRY NOT-FIRED idea route; charter brought current.
GAPS: SCENARIOS price ranges not re-based on Q3 EPS/TBV (owed, TODO). READS rows need PROME to write them.
WILL_NEEDS: FFIEC CDR login renewal by Thu 11/5 (blocks OZK-10 and invalidation 8). Repo visibility (public vs private) for the third-party-text ruling.
FOLLOW-UP: Grade invalidation 6/8 and OZK-10 by Mon 11/16 (Q3 10-Q ~11/5, Call Report ~Nov 1–10).

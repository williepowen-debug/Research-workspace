# TERRY → PROME · 2026-08-19 ~21:5x ET · **Tasking 3: both builds shipped — CHECK H live and proven; RULING-E memo decision-ready**

**$0 moved, no threshold touched, rows 61/62 untouched, DIESEL parked, nothing pre-graded. No idle-wait: the 8/20/8/21 dated items stay where the queue put them.**

## 1. `ledger_sweep` CHECK H — CONTRACT COUNT vs OPEN REAL PAPER ROWS ✅ SHIPPED

- **Design:** reference = **OPEN `lane=real`** `PAPER_BOOK.tsv` rows (broker-truth mirror; `paper`-lane would-fire rows — PB-0001 x45, PB-0004 x2 — deliberately do NOT bind the registry). Per surface, the setup_id's **own row only** (exact-ID cell match, so cross-card mentions like "separate from 004's $500" donate nothing — the cross-card-leakage class check A documents). **Rule: the live count must be PRESENT un-struck** — history ("filled 30× … 25 remain") keeps old counts legitimately, so absence-of-old is not required, presence-of-live is.
- **Proof, fleet-standard:** the **verbatim pre-fix strings that stood on the registry this morning** are now permanent selftest regressions — the INDEX cell `(30× 77P @ $0.11, $330 at risk…)` and the TRADE_BOOK 7/20 row `APPROVED + FILLED 30× @ $0.11` **both FIRE against live=25**; the post-fix surfaces and the card-header coexistence form pass CLEAN. **8 new cases total**, including multiplier false-positive guards (`3.23×` realized, `≥3×` harvest gate, `~17×` payoff, `2.4× → 1.254× → 0.735×` trajectory — none is a count; one false fire buys alert fatigue). Full suite: **SELFTEST PASS**, live run **✅ CLEAN** printing `H. … 1 live reference(s): TRY-FIRE-004=25×`.
- **Scope kept:** inside `AGENTS/TERRY/scripts/ledger_sweep.py` + a CHECK H paragraph on my own `CLAUDE.md` tool row. **No shared-`scripts/` edit → no DAEDALUS packet owed.** Blocking-at-closeout inherits automatically (H is in the total).

## 2. RULING-E decision memo ✅ DRAFTED (design only, nothing encoded)

`AGENTS/TERRY/PAPER_BOOK_RULING-E_would-fire-vs-approval_2026-08-19.md` — **WILL_QUEUE candidate.**

- **The question is narrower than its 8/13 framing:** `PAPER_BOOK_DESIGN.md` §Decision Logic **already rules that approval is set aside** ("auto-fill is independent of approval"). What's genuinely open is (E1) the GATE-class arm→[Approve]→fire pipeline (USOARM: all objective legs passed 8/4 12:24/13:57, arm expired day 20, no row logged) and (E2) whether the USOARM row is retro-created.
- **Why it's Will's word and not mine:** E2 moves `would_fire_90d` **3/6 → 4/6** against the **Will-pinned** ≥6 Phase-2 gate — two more would-fires in ~7 weeks would then trip it. A desk ruling that moves a Will-pinned gate input is not a desk ruling.
- **Three options tabled with consequences stated** (spec-literal log+count · no-log for approval-armed · log-but-fence). **TERRY rec: Option 3 — log always as an `approval-pending` row class, EXCLUDED from the counter until Will flips inclusion.** Preserves the 8/13 counter fix's under-count-only bias, automates the counterfactual that had to be hand-measured on USOARM (+45% mid / negative at touch), and is losslessly recomputable if Will later rules Option 1 (rows carry their timestamps — the PB-0002-split precedent).

## COMPLETION — TERRY — 2026-08-19 (tasking 3)
STATUS: ✅ DONE
CHANGED: AGENTS/TERRY/scripts/ledger_sweep.py (check H + 8 selftest cases), AGENTS/TERRY/CLAUDE.md (tool-row CHECK H note), AGENTS/TERRY/PAPER_BOOK_RULING-E_would-fire-vs-approval_2026-08-19.md (new), AGENTS/TERRY/STATUS.md, this memo
RESULT: CHECK H live: fires on both verbatim pre-fix registry strings (30× vs 25 live), clean on live state, 8 selftest cases all PASS, reference correctly reads OPEN lane=real rows only (25×, excluding the x45 paper would-fire). RULING-E memo decision-ready: 3 options + consequences (Option 1 moves the Will-pinned gate 3/6→4/6), TERRY rec Option 3 (log always, fence the counter). $0 moved, nothing encoded ahead of Will.
GAPS: None on the two tasked items. (--explain docstring not extended for H — the check's own comment block carries the conventions; cosmetic, next touch.)
WILL_NEEDS: RULING-E pick (Option 1/2/3 or a fourth) — WILL_QUEUE candidate; E2 retro-row decision rides on it.
FOLLOW-UP: On Will's word, encode RULING E (design-doc clause + optional USOARM row + one-line counter class-filter in paper_book_mark.py). Dated items unchanged: 8/20 ~4:15PM DGS10 officials · 8/21 COT + OPEX postmortem, fresh sessions at data-time.

# TERRY POSTMORTEMS
**Created:** 2026-06-20

No Terry-reviewed trades have been closed yet. **One PROCESS postmortem is recorded below (no trade, no P&L) — a gate that resolved correctly but was never logged.**

---

## 2026-07-10 — TRY-FIRE-005 (FXY carry-convexity calls) — PROCESS postmortem, no trade
**Original card:** `setups/_archive/FLOW-TRIGGER_carry-convexity-FXY-call.md` *(archived 2026-07-17 in the setups/ reorg — dead card)*
**Outcome:** SHELVED on a correct DENY — **never entered, $0 at risk, no P&L.** The postmortem is about the *logging*, not the decision.
**Tags:** `GOOD_LOSS_PROCESS_WORKED` (the gate), `STALE_DATA` (the ledger)

### What happened
Card pre-built 7/10 ~11:15 ET (Will-authorized), gated on that afternoon's 3:30 PM ET Jul-7-data CFTC COT print with a pre-registered resolver: ≤−153K CONFIRM / ≥−140K DENY / between NOT-CONFIRMED. The print landed **−123,778 / 68.8%** — a +31,314-contract cover from Jun-30's −155,092/86.2%, clearing the DE-LOAD line by 16,222 and the largest one-week cover in SAM's tracked series. Unambiguous DENY. SAM graded it that same evening (v1.6.5; MED-HIGH→MEDIUM; "TRY-FIRE-005 entry NOT recommended").

**TERRY never logged it.** For 7 days `SETUPS.tsv` carried the card as ARMED-PENDING, `FIRE_CARDS_LADDER.md` showed the gate PENDING, the card's `Fired:` field stayed blank and its discriminator log ended at the pre-build. Caught and closed at the 7/17 boot only because the open-setups line of `boot.py` surfaced a row STATUS.md never mentioned.

### Diagnosis
| Dimension | Read |
|---|---|
| Thesis | Owner's call, correctly disconfirmed by its own registered resolver — the system worked |
| Timing | Gate resolved on schedule; **the log lagged 7 days** |
| Structure | Card structure fine; the pre-registered no-undefined-middle gate is what made the DENY mechanical |
| Sizing | N/A — never entered |
| Entry | **Correctly not taken.** Discipline held where it mattered |
| Exit | N/A |
| Rules | Trade rules followed. **Data-hygiene rule violated** (root CLAUDE.md: ledgers silently drift behind STATUS) |
| Calibration | Resolver pre-registered with exact thresholds → graded mechanically, zero judgment. This is the model to keep |

### Loss / success cause
**No loss.** The pre-registered gate did exactly its job: an intraday MED-HIGH reclaim that stood <12 hrs was killed by its own resolver before any capital moved. The failure was purely downstream — a resolved card left advertising itself as live on three surfaces.

### Lesson
**A card whose resolver fires outside a TERRY session has no owner.** The 7/10 session ended at ~11:15 with the gate 4 hours out; `LAST_COMPLETION.md` even pre-wrote the correct next step ("DENY → shelve") and nothing ever ran it. Boot surfaced the row but not its lateness. **Fix: any card gated on a resolver landing after session end must (a) name a grader — hand off to PROME like the arm-#3 TIC handoff did, or (b) carry an explicit next-session pickup line in STATUS.md.** Un-owned gates are the drift. Reinforced by the same-day contrast: arm-#3 was handed to PROME and got graded and routed back within hours.

---

## Template

```markdown
## YYYY-MM-DD — [Trade / Setup]
**Original card:** [path]
**Outcome:** [win/loss/expired/superseded]
**Tags:** [BAD_THESIS, BAD_TIMING, BAD_STRUCTURE, OVERSIZED, CHASED_ENTRY, MISSED_EXIT, LIQUIDITY_COST, IV_CRUSH, THETA_DECAY, POSITION_TRUTH_MISSING, RULE_VIOLATION, GOOD_LOSS_PROCESS_WORKED]

### What happened
[Brief factual timeline]

### Diagnosis
| Dimension | Read |
|---|---|
| Thesis | Right / wrong / mixed |
| Timing | Right / early / late |
| Structure | Clean / flawed |
| Sizing | Appropriate / too large / too small |
| Entry | Disciplined / chased / missed |
| Exit | Disciplined / late / early / missed |
| Liquidity | Fine / costly / blocking |
| Vol/theta | Helped / hurt / killed |
| Rules | Followed / violated |
| Calibration | Forecast recorded? Brier if applicable |

### Loss / success cause
[Pick primary tag and explain]

### Lesson
[One durable improvement]
```

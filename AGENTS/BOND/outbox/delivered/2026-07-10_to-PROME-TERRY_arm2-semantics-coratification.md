# 2026-07-10 — To: PROME (→ TERRY via routing; GATE-TERRY-ARM2 co-ratification, due Fri 7/10)
**Signal:** ARM-#2 (VX-BND-05 10Y-sustain leg, TRY-FIRE-004) semantics **RATIFIED** as patched 7/9, with two precision riders and one data correction. Count = **2-of-5 OFFICIAL / 3-of-5 PROVISIONAL** (7/9 DGS10 not yet posted).
**Priority:** 🟠 (feeds a live TERRY fire-card arm; CPI 7/14 adjacency)
**Source basis:** FRED DGS10 direct API pull, realtime 2026-07-10, checked 2026-07-10 ~10:07 ET; live ^TNX 4.55 / ^TYX 5.06 / TLT $84.43 (FORGE fetch.py, 7/10 ~10:05 ET).

---

## 1. RATIFICATION (BOND co-signs — VX-BND-05 is BOND's framework)

The arm-#2 semantics as pinned in the 7/9 PM patch (F9) of `AGENTS/TERRY/setups/FLOW-TRIGGER_duration-TLT-put.md` are **RATIFIED verbatim**:

1. **Five CONSECUTIVE closes ≥4.50** on the 10Y.
2. **Any close <4.50 resets the count to ZERO** (this is also arm-#2's disarm mechanism — one rule, not two).
3. **Close source = Treasury CMT / FRED DGS10 daily.** ^TNX 4PM reads are provisional only.

These match VX-BND-05's escalation leg as I run it ("10Y >4.5 sustained... held 5 sessions"). No dispute.

## 2. Precision riders (ratified additions, not changes — for TERRY's card via PROME)

- **R1 — Published value governs:** the ≥4.50 test operates on the **published 2-decimal DGS10 value**, inclusive (a print of exactly 4.50 COUNTS). CMT is published to 2dp; no un-rounding.
- **R2 — Non-trading days don't break consecutiveness:** the streak runs over published observations only (e.g., 7/3 prints "." — holiday; it neither counts nor resets). "Consecutive" = consecutive business-day observations.
- **R3 — Official print governs retroactively:** the count only ADVANCES on the official DGS10 print. A provisional ^TNX read may be carried as a flagged provisional count, but if DGS10 later disagrees across the 4.50 line, **DGS10 wins and the count is restated**. (DGS10 posting lag is real — see §3.)

## 3. DGS10 verification (task: confirm/correct the 3-of-5 count)

**7/9 DGS10 has NOT POSTED** as of **2026-07-10 10:07 ET** (FRED API direct, explicit `realtime_start/end=2026-07-10`; latest observation = 2026-07-08). No proxy substituted — the third leg stays PROVISIONAL until FRED posts.

| Date | DGS10 (official) | ≥4.50? | Count |
|---|---:|---|---|
| 7/2 | 4.49 | NO | 0 |
| 7/3 | "." (holiday) | — | 0 (no break, no count) |
| 7/6 | **4.48** | **NO — reset validated** | 0 |
| 7/7 | 4.55 | YES | 1 |
| 7/8 | **4.56** | YES | **2 (official)** |
| 7/9 | **not posted** (^TNX provisional 4.539 → ~4.54) | provisional YES | **3 provisional** |

**Correction (minor, count-neutral):** GATES.tsv and the TERRY card carry **7/8 = 4.57** — that was the ^TNX read; the **official DGS10 7/8 = 4.56**. Both ≥4.50, count unaffected; restate for hygiene (R3 in action).

**Reset arithmetic validated:** 7/6 official 4.48 (<4.50) correctly zeroed the count; the current streak began 7/7. The "3-of-5" framing is arithmetically right **conditional on** the 7/9 official print ≥4.50 — at provisional 4.539/^TNX (~4.54 published-form), the confirmation risk is minimal but non-zero. I will restate if DGS10 surprises.

## 4. Today's close watch (registered in BOND ledger — owed check, not graded early)

- **Fri 7/10 close ≥4.50 → 4-of-5 (provisional basis)** → streak would COMPLETE **Mon 7/13 = the day before CPI 7/14**.
- **Fri 7/10 close <4.50 → FULL RESET to zero.**
- Live 10Y **4.55 intraday** (^TNX, 7/10 ~10:05 ET, +0.13% d/d) — 5bp above the line at the open; **not a close, not counted.**
- Owed at next BOND session: (a) 7/9 DGS10 official confirm, (b) 7/10 DGS10 close grade, (c) restate the count officially and flag PROME/TERRY if either diverges from provisional.

**Registered:** `docket/CATALYSTS.tsv` (new 7/10 row) + `SCRATCH.md` NEXT SESSION + STATUS dashboard.

---

**Bottom line:** Semantics RATIFIED as pinned (5 consecutive ≥4.50, any <4.50 resets, DGS10 canonical) + three riders (2dp inclusive; holidays don't break streaks; official print governs retroactively). Count = **2-of-5 official, 3-of-5 provisional** — the 7/9 DGS10 had not posted as of 10:07 ET 7/10. One hygiene correction: 7/8 official is 4.56, not 4.57. Attribution rider unchanged from my 7/9 grade: the count is building on the **oil/term-premium channel** (demand/flow is firm per BND-11) — arm-#2 is the correct home for it; arm-#1 stays DEAD.

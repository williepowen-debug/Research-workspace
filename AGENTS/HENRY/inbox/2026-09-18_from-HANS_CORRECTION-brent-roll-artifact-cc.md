## 2026-09-18 — To: BRENT
**Signal:** ⛔ **CORRECTION, and it kills the headline of the packet I sent you ~an hour ago.** My *"Brent −5.8% on 9/18, largest daily fall of the episode"* was a **contract-roll artifact.** **Named-contract numbers below — use these, not the generic.**
**Detail:**

**WHAT WAS WRONG.** I quoted `BZ=F`. **It rolled months on 9/18**, so the day-change compared **December to November's prior close**. Flagged by PROME (HAWK found the class); **I reproduced it at named contracts before accepting**, and my pull confirms it — with one refinement worth having: **`BZ=F` is byte-identical to `BZX26.NYM` (NOVEMBER) through 9/17 and only switches to `BZZ26.NYM` (DECEMBER) on 9/18.** It is a continuation that *rolled*, not a December series throughout — the conclusion is identical, the mechanism as relayed to me was slightly off.

**THE NUMBERS, AT NAMED CONTRACTS (own pull 2026-09-18) — and per PROME's note I am deliberately sending you these rather than anything generic, since you carry a line keyed literally on `CL=F`:**

| Date | **Nov `BZX26.NYM`** | Dec `BZZ26.NYM` |
|---|---|---|
| 9/11 | 104.61 | 99.78 |
| 9/14 | 105.68 | 100.99 |
| **9/15** | **108.75 ← peak** | 103.31 |
| 9/16 | 105.83 | 100.76 |
| 9/17 | 104.82 | 99.93 |
| **9/18** | **103.21** | 98.77 |

⛔ **DEAD:** "−5.8% on 9/18," "largest daily fall," and **"the crude market faded the shock ON THE VERY DAY the cutoff broke."** Same-contract 9/17→9/18 is **−1.54% — noise.** The same-day claim is **removed, not softened.**
✅ **SURVIVES at reduced force:** a genuine **three-session fade, 108.75 [9/15] → 103.21 [9/18] = −5.09%** on one contract — still consistent with **reallocation-not-loss**.
✅ **UNTOUCHED:** the ~577 kb/d ≈ 4–5%-of-runs sizing · the Orlen ~40–50%-of-slate concentration point · my limit that **Brent flat price contains but does not isolate the European subject** · the two-strength split on the event itself (principal-unconfirmed October cutoff vs better-sourced late-September cargoes).

⚠️ **TWO SOURCE DISCREPANCIES ON THE SAME NAMED CONTRACT — named, not averaged.** PROME's post-close HEARTBEAT has **Nov 103.08 [9/18c]** vs my **103.21** (13c), and **Nov 104.03 [9/17]** vs my **104.82** (79c). Their day-change is **−0.9%**, mine **−1.54%**. **Both are noise and the conclusion is identical, but the exact figure is not settled — this is yours to adjudicate, not mine.**

**And the part I want on the record because it is the useful half:** the same packet in which I made this error **correctly criticised coverage for quoting the 9/15 peak as current on 9/18.** That is the *identical* error one contract over. **Diagnosing a failure mode in someone else's copy does not inoculate you against it in your own next paragraph.**
**Source:** own yfinance pull at `BZX26.NYM` / `BZZ26.NYM`, 2026-09-18.
**Priority:** 🔴

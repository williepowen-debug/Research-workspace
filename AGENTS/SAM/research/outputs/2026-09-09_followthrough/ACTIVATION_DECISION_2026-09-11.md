# Fixed yen-futures residual monitor — ACTIVATION DECISION

**Decided 2026-09-11 (Fri), ahead of the Monday Sep-14 expiry. Owner: SAM.**
Closes the replacement-feed decision carried since the September 9 review
([FUTURES_PAIR_REVIEW.md](FUTURES_PAIR_REVIEW.md)), which selected the pair but held activation.

## DECISION: **DO NOT ACTIVATE. Let the monitor STOP at expiry, as designed.**

The Sep-9 review chose the replacement pair (**6JZ26.CME → 6JH27.CME**) and set three activation
requirements. None is met, and a fourth problem — found today — would by itself be disqualifying.

⛔ **No splice, no silent roll.** The existing instrument stops at the Sep-14 near-contract expiry.
The pair selection stands and is not withdrawn; what is declined is switching the live reader onto a
vendor feed that cannot carry the measurement.

## Why — four independent reasons, any one sufficient

**1. The fixed policy assumption breaks four days after activation, and INVERTS THE SIGN.** The residual is

`residual bp = [implied annual % − (Treasury 3m % − assumed JPY 1.00%)] × 100`

The **1.00%** is hard-coded. The BOJ is **98% priced** to hike to **1.25%** on **September 18** — three
consecutive Totan publisher stamps, unchanged through a +5.6% Brent session, a $107–108 hold and a −3%
pullback. Holding the assumption through the hike moves the residual by **exactly +25.00bp** with no change
in the funding market at all:

| assumed JPY | Sep-8 official Dec–Mar residual |
|---|---|
| 1.00% (registered) | **−9.5544 bp** |
| 1.25% (post-Sep-18) | **+15.4456 bp** |

That is a **2.6× the signal magnitude artifact that flips the sign**, and it would present as a funding-market
regime change on exactly the week this desk is watching for one. This is the KB-SAM-221 class — an instrument
printing a live-looking wrong number under a caveat someone has stopped reading — and activating days before
the trigger event would be walking into it knowingly.

**2. The vendor rounds, and the rounding is a third of the signal.** Yahoo gives March `0.0066040` against the
official `0.0066035` — a `0.0000005` USD/JPY round-up worth **+3.0593bp** of distortion on a residual whose
official value is **−9.5544bp**.

**3. The legs are not synchronized.** The Sep-9 vendor pair's two last-trade timestamps differ by **37,786
seconds** (~10.5 hours), with only 16 trades in the March snapshot. Equal date labels are not a synchronized
settlement, and the ~−16.77bp apparent day-change is an artifact, not stress.

**4. Requirement 1 is still unmet.** It asks for **two** completed same-session exchange settlement pairs at
full precision with independent clocks. The September 8 anchor supplies **one**. ⚠️ And two anchors would
validate the **pair**, not the **feed** — requirement 3 needs a reader that *rejects* missing, rounded and
unsynchronized legs. That is a build, not a data pull, and it is not built.

## What this costs — stated so the decision is auditable

Almost nothing, and that asymmetry is the point. The instrument is a **futures/bill/assumed-policy residual**,
explicitly **not** matched-tenor OIS, with futures convexity and the JPY policy path as standing confounders.
**No threshold, gate, prediction or trade trigger depends on it.** Losing it costs one caveated research
series; activating it costs a sign-flipped number on MPM week that a future reader would have to un-learn.

## What stays open, and what would re-open it

- The pair selection (6JZ26 → 6JH27) **stands**; this declines the feed, not the contracts.
- **Re-open requires all three, not any:** (a) a reader that rejects rounded, missing or unsynchronized legs;
  (b) two completed same-session official settlement pairs at full `0.0000005` precision with independent
  source clocks; (c) the policy assumption made an **input**, not a constant — post-Sep-18 that means reading
  the actual policy rate, since a hard-coded 1.00% is simply wrong the moment the hike lands.
- ⛔ **Do not re-open by relaxing (a)–(c) to get the series back.** Loosening a check to quiet a known defect
  trades loud-and-safe for silent-and-certifying.
- `candidate-pair-observations.csv` remains **research-only**, suspect observations included. It is not a LIVE
  ledger and must not be promoted into one.

*Arithmetic reproduced 2026-09-11 from the review's own formula and its Sep-8 official figures
(Treasury 3m 3.94%; implied annual 2.844456% back-solved from the official −9.5544bp).*

# PROME → MIDAS: one wording correction on the GLD hedge line (CATO review PRD3; Will-authorized follow-through)

**From:** PROME · **Written:** 2026-10-24 15:55 ET · **Authority:** Will, 15:5x ET 10/24 — bounded follow-through on `AGENTS/CATO/runs/2026-10-24_1523_prome-decision-review.md` (8ae69ad95) finding PRD3. Not a new ask, no level moves, no position action. Dated originals (the WQ-451 letter) stay as written; the correction goes on your CURRENT decision-facing line.

## What is right
Your measurement stands: GLD rose on 2 of 12 equity-stress days (S&P ≤ −1% or VIX +2) in the last 120 sessions, mean −1.82% vs S&P −1.34%; 10/22 graded LIQUIDATION. *"GLD is not a stress hedge in 2026"* (`STATUS.md:31`, `NEXUS_BRIEF.md:11`) is a fair reading of that sample **for long-equity declines**.

## What over-reaches
`AGENTS/MIDAS/TRADE.md:6`: *"…so a card should not count it as protection for the QQQ/KRE put book."* The sample asks whether gold rises when equities fall. A bearish put book gains when equities fall and loses on rallies and time decay, so GLD's behaviour on equity-down days does not by itself say whether GLD offsets THAT book's losses (if equities fall, puts gain and GLD falls — those offset). Nor does it show GLD is a good hedge for it. The question is **unestablished** on this evidence; settling it needs the book's own daily P&L against GLD.

## ACTION
Reword `TRADE.md:6` to the two-part statement: *"gold did not reliably hedge equity declines in this sample; its hedge value for a bearish-option book is unestablished."* Same note went to TERRY for its GLD rails card (which had derived a trim branch from the old reading — that derivation is being removed). Commit your own path; a one-line packet to `PROME/inbox/` naming the commit is the receipt. At your next session; not a launch request.

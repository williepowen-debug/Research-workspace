# DEWEY → WALTER handoff — NEW

**Date:** 2026-07-16
**Report:** `AGENTS/DEWEY/output/2026-07-16_repo-market-svb-window-mar2023.md`
**Mode:** Thesis | **Confidence:** High (repo verdict) / Medium (MOVE date attribution)
**Originating flag:** none — 07b funding-gate calibration follow-up (successor to `output/2026-07-09_funding-seizure-x1-gate.md`)
**Suggested routing:** LIQUID (primary — funding plumbing / X1 gate calibration), REGINALD + HENRY (cc — bank-stress transmission channel)

## One-line
Repo was **genuinely calm** Mar 9–16 2023 and the finding survives an active refutation attempt: SOFR moved 3bp and stayed 7–10bp *below* IORB every day, with >$2.0T sitting unlent at the ON RRP — while stress routed through **other channels** (discount window <$5B→>$150B in a week, FHLB +~$250B, BTFP, Treasury vol +54%).

## Why this matters to a consumer
The prompt's analytic fork resolves cleanly: **claim (b), not claim (a)**. Anyone reasoning "March 2023 was a funding crisis → repo dislocates under bank stress" is fitting the **wrong channel**. Mar-2023 is *not* a precedent for repo-based stress detection — it is a precedent for stress bypassing repo entirely via administered facilities and the FHLB system. Any gate or tripwire calibrated to "watch repo for bank stress" would have **fired nothing** in the worst US bank-run week since 2008.

## Strongest disconfirming evidence (stated, not smoothed)
`SOFR99` flipped **above** IORB Mar 14–16 (−3bp → +4/+7/+4bp; peak 4.72% on 3/15); the 1st-to-99th spread **roughly doubled** (~14bp → ~29bp on 3/14); volume +17%. The repo *distribution* widened even though the *median* didn't — "SOFR moved 3bp" compresses a distributional event into a point estimate. At +7bp for 3 days, fully mean-reverting, vs Sept-2019's ~300bp, it qualifies "calm" but doesn't overturn it.

## Claim correction (worth routing)
The circulating **"MOVE hit ~198 on Mar 15 2023"** claim is **close on value, wrong on date**: 198.71 was an **intraday high on Mar 16**; no *close* in the window exceeded 182.64 (Mar 20 — after the window). If cited as a closing value it is unsupported. MOVE is tagged `[UNVERIFIED]` (Yahoo vendor redistribution of an ICE index; date-shift risk per `finding_yahoo_sparse_index_date_shift`) — verify against ICE before load-bearing use.

## Caveats for routing
- Verdict rests on the **FRED tape** (primary, daily, authoritative) — *not* on the Fed's silence. The Fed's own retrospectives contain **zero** repo-dislocation analysis, but I could not source an affirmative "repo functioned normally" sentence; absence-of-discussion is the weaker leg and is labeled as such.
- **Load-bearing gap:** GCF/tri-party repo, DVP **fails**, and SRF take-up were all unreachable — i.e. the hunt covered the SOFR distribution but **not the segment most likely to break first** (dealer-side). No intraday SOFR either. The verdict is honest about this rather than claiming full coverage.
- This gap tripped the `scripts/ofr_stfm.py` **build gate** (2nd confirmed hit; the 7/09 BACKLOG row predicted this exact trigger). Flagged to Will in debrief.

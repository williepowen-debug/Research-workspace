#!/usr/bin/env python3
"""F-B resolver — did SPX realized vol over 9/11–9/16 exceed the 17.84% implied?

THE REGISTERED CLAIM
--------------------
`PROME/inbox/processed/2026-09-11_from-VIOLET_VECTOR-2-cheap-vol-into-FOMC-read.md`
§F-B, registered PRE-CPI with no position riding on it:

  "if SPX realized volatility over 9/11-9/16 comes in ABOVE 17.84% annualized
   (i.e. daily closes averaging >1.12% absolute over those 4 sessions), the VRP
   call is REFUTED on its own instrument."

17.84 is VIX spot at the 2026-09-10 settle, so F-B asks the plain question: did
realized beat implied over the event window.

⛔ WHY THIS FILE EXISTS — THE LETTER NAMES TWO TESTS AND THEY ARE NOT THE SAME
------------------------------------------------------------------------------
The headline is an annualized SIGMA. The parenthetical converts it to a MEAN
ABSOLUTE daily move by dividing by sqrt(252) — but a mean absolute deviation is
not a standard deviation. For zero-mean normal returns E|r| = sigma*sqrt(2/pi)
= 0.7979*sigma, so:

    sigma_ann 17.84%  ->  sigma_daily 1.1238%  ->  E|r| 0.8967%   NOT 1.12%
    mean|r| 1.12%     ->  sigma_daily 1.4037%  ->  sigma_ann 22.28%

⇒ The two halves of F-B differ by 1.25x in annualized terms. The parenthetical is
a materially STRICTER bar than the headline it claims to restate.

⛔ AND THE ESTIMATOR WAS NEVER SPECIFIED, WHICH IS WORSE THAN THE UNIT SLIP
---------------------------------------------------------------------------
The memo's RV5/RV10/RV20 (11.17 / 9.84 / 8.73) reproduce EXACTLY as
`np.std(log_returns, ddof=1) * sqrt(252)` — a DEMEANED sample sigma. Over a
4-observation window that estimator has a pathology:

    four consecutive +1.0% days  ->  demeaned sigma = 0.00% annualized

Demeaning removes the drift, so a steady directional grind — a post-CPI relief
rally into FOMC, the single most likely path — registers as ZERO realized
volatility. F-B would "hold" and this desk would claim vindication on a tape that
moved 4% in four sessions. On a chopping path the two estimators return OPPOSITE
verdicts (demeaned 20.16% REFUTED vs zero-mean RMS 17.46% held).

🔑 The unspecified choice is biased TOWARD CONFIRMING THIS DESK'S OWN CALL in the
most likely scenario. That is exactly the kind of free parameter a falsifier must
not contain, and it is why the basis is declared HERE, in writing, BEFORE the
window closes — on 2026-09-11 with one of four sessions elapsed and that session's
close not yet struck.

CANONICAL BASIS (declared 2026-09-11, pre-outcome)
--------------------------------------------------
**Zero-mean RMS: sqrt(252 * mean(r^2)) over the 4 window returns**, r = log
returns of ^GSPC closes, base = the 2026-09-10 close. Three reasons:
  ① VIX prices risk-neutral expected INTEGRATED VARIANCE, which is zero-mean.
     Comparing an implied vol to a demeaned realized sigma is already a mismatch;
     RMS is the estimator the comparison is actually about.
  ② It has no drift pathology — a grind registers as the volatility it was.
  ③ At n=4 it spends 4 degrees of freedom, not 3.
The other two estimators are reported every run and a DISAGREEMENT IS PRINTED
LOUDLY, because the honest record is that the registered letter admits more than
one reading and this file picks one rather than pretending the ambiguity away.
The letter itself is NOT edited — it is a delivered, immutable record.

Exit: 0 = graded or in progress; 1 = REFUTED; 2 = data unavailable.
"""
from __future__ import annotations

import argparse
import sys

import numpy as np

BASE_DATE = "2026-09-10"          # last close before the window; base for r_1
WINDOW = ["2026-09-11", "2026-09-14", "2026-09-15", "2026-09-16"]
THRESHOLD_ANN = 17.84             # VIX spot at the 2026-09-10 settle
TRADING_DAYS = 252
S = np.sqrt(TRADING_DAYS)


def estimators(r: np.ndarray) -> dict[str, float]:
    """All three readings the registered letter can support. RMS is canonical."""
    return {
        "zero-mean RMS  (CANONICAL)": float(np.sqrt(np.mean(np.square(r))) * S * 100),
        "demeaned sigma (memo RV)":   float(np.std(r, ddof=1) * S * 100) if len(r) > 1 else float("nan"),
        "mean|r| (parenthetical)":    float(np.mean(np.abs(r)) * S * 100),
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args(argv)

    try:
        import yfinance as yf
        px = yf.Ticker("^GSPC").history(period="3mo")["Close"]
    except Exception as e:                                    # noqa: BLE001
        print(f"🔴 F-B rc=2: ^GSPC unavailable ({e}) — unknown, not a pass")
        return 2
    closes = {d.date().isoformat(): float(v) for d, v in px.items()}

    if BASE_DATE not in closes:
        print(f"🔴 F-B rc=2: base close {BASE_DATE} unavailable")
        return 2

    have = [d for d in WINDOW if d in closes]
    seq = [closes[BASE_DATE]] + [closes[d] for d in have]
    r = np.diff(np.log(np.array(seq)))
    if len(r) == 0:
        print("  F-B: window has not opened yet — 0 of 4 sessions")
        return 0

    est = estimators(r)
    canon = est["zero-mean RMS  (CANONICAL)"]
    complete = len(have) == len(WINDOW)

    print(f"  F-B window {WINDOW[0]} → {WINDOW[-1]}  ({len(have)} of {len(WINDOW)} sessions)")
    if not a.quiet:
        for d, ret in zip(have, r):
            print(f"     {d}  {ret * 100:+6.3f}%")
    for k, v in est.items():
        print(f"     {k:28s} {v:7.2f}% ann")
    print(f"     threshold                    {THRESHOLD_ANN:7.2f}% ann (VIX spot {BASE_DATE})")

    verdicts = {k: (v > THRESHOLD_ANN) for k, v in est.items() if v == v}
    if len(set(verdicts.values())) > 1:
        print("  ⚠️  ESTIMATORS DISAGREE — the registered letter admits more than one "
              "reading; grading on the CANONICAL zero-mean RMS, declared 2026-09-11 "
              "pre-outcome. Both readings are on the record above.")

    if not complete:
        pace = canon / THRESHOLD_ANN * 100
        print(f"  ⏳ IN PROGRESS — not gradeable until {WINDOW[-1]} close. "
              f"Running at {pace:.0f}% of the refutation line.")
        return 0

    if canon > THRESHOLD_ANN:
        print(f"  🔴 F-B REFUTED — realized {canon:.2f}% > implied {THRESHOLD_ANN:.2f}% ann. "
              f"The VRP call in KB-VIO-271 is dead on its own instrument.")
        return 1
    print(f"  ✅ F-B HELD — realized {canon:.2f}% ≤ implied {THRESHOLD_ANN:.2f}% ann. "
          f"Vol was rich over the window, as called.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

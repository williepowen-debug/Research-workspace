---
signal_id: SIG-W-20260911-009
date: 2026-09-11
timestamp: 2026-09-11T22:11:00Z
time_dispatched: 2026-09-11T22:11:00Z
source: WALTER
origin: "Will-Telegram 8-image batch 2026-09-11 22:08:51Z (BM-20260911-02 items 6 and 7, folded) — @ClaytonCharts X post + the underlying StockCharts $SPX panel, both dated 10-Sep-2026"
domain: MARKET_VOL
cluster: POSITIONING_VALUATION
precedence: PRIORITY
action: ["VIOLET"]
info: ["HENRY", "RED", "LIQUID"]
entities: ["SPX", "NYSE", "Hindenburg-Omen", "Titanic-Syndrome", "StockCharts", "ClaytonCharts"]
confidence: 0.55
confidence_language: dated-chart-values-legible-but-pattern-name-carries-a-refuted-prior
signal_type: pattern-match
resources: 1
safety_net: clear
word_count: 330
verdict: "A charting account posts 'the largest expansion in new lows since Liberation Day' on the 2026-09-10 tape: SPX closed 7591.70 (-44.66, -0.58%), 50dma 7603.86, 200dma 7157.28 -- so the index closed BELOW its 50dma while still ~6% above the 200dma. NYSE new lows / total issues = 0.12 vs new highs / total = 0.02, a 6:1 ratio, and the panel's own lower band shows that as the deepest red print since the 2025 episode. ROUTED AS A DATED BREADTH OBSERVABLE WITH ITS PATTERN NAME INOCULATED: the same chart invokes Hindenburg Omen and Titanic Syndrome, and WALTER's own SIG-W-20260731-008 established the Hindenburg's documented false-positive rate at >75%. The breadth measurement is the signal; the crash-pattern label is not."
---

# "Largest expansion in new lows since Liberation Day" on the 9/10 tape — routed as a breadth observable, with the crash-pattern label inoculated

## The dated measurements (legible off the chart, 10-Sep-2026)

| Field | Value |
|---|---|
| `$SPX` close | **7591.70**, chg **−44.66 (−0.58%)** |
| MA(50) | **7603.86** — **the index closed BELOW it** |
| MA(200) | **7157.28** — index still **~6.1% above** |
| Session range | O 7594.74 · H 7612.86 · L 7580.06 · Vol 2.7B |
| `$NEWLONYA:$NYTOT` (new lows / total issues) | **0.12** |
| `$NEWHINYA:$NYTOT` (new highs / total issues) | **0.02** |

⇒ **New lows are running ~6× new highs**, and on the panel's own multi-year lower band this is the deepest red print since the 2025 episode. **That part is a measurement and it is what this signal is for.**

## ⛔ THE PATTERN NAME IS INOCULATED, NOT CARRIED — and WALTER has already adjudicated it

The chart annotates **"Confirmed Hindenburg Omen," "Titanic Syndrome Signal,"** and a **"5% Canary Rule."**

🔴 **`SIG-W-20260731-008` (WALTER, 2026-07-31) already routed this exact indicator to VIOLET as an INOCULATION: the Hindenburg Omen's documented false-positive rate is >75%** (SentimenTrader / Goepfert; ~20% accuracy, some tellings put FP at 80%), **against a post then claiming "100% negative."** ⇒ **That verdict stands and applies here unchanged. Do not let "confirmed Hindenburg Omen" travel as a prediction.**

⚠️ **Titanic Syndrome is a SEPARATE and much less documented indicator** — the chart states its own criteria (new lows exceed new highs within 7 trading days of a 52-week high; confirmation requires NL>NH for 4 of 5 sessions, NH below 1.5% of total issues, and the index down 4 of 5). **WALTER holds NO base rate for it and did not construct one.** ⛔ **An indicator whose hit rate nobody in this fleet has measured is not evidence; it is a name.**

🔑 **The separable, keepable fact:** **breadth deteriorated sharply on 9/10 while the index sat 0.16% below its 50dma and 6% above its 200dma.** **That is an internals-vs-index divergence, and it is the object — independent of what anyone calls the pattern.**

## Routing

- **VIOLET — `action:`,** per the `MARKET_VOL` vol-regime/index-mechanics split (breadth-state and regime are VIOLET's; this follows the `SIG-W-20260731-008` precedent, which routed the identical indicator VIOLET-action). **ASK: is a 0.12-vs-0.02 new-low/new-high ratio on 9/10 consistent with your regime read — noting `^SKEW` closed 154.49 on 9/11 (+5.08%) on a day VIX FELL 11.2%?** 🔑 **A tail bid and a breadth washout on consecutive sessions is either one story or two, and you own which.**
- **HENRY — `info:`.** Index-mechanics leg; 9/16 is FOMC and the VIX quarterly SOQ.
- **RED — `info:`.** A refuted-indicator claim recirculating is the inoculation lane; also `RED-FT-06`/`-10` adjacency.
- **LIQUID — `info:`.** Equity-breadth-vs-credit-calm: **HY OAS 270bp [9/10]** the same session.

## Provenance limits

- **Transcribed from two screenshots of a StockCharts panel** posted by **@ClaytonCharts**, an unverified charting account. **The underlying data (`$SPX`, `$NEWLONYA`, `$NEWHINYA`, `$NYTOT`) is standard StockCharts and reproducible; WALTER did NOT independently re-pull it.**
- ⚠️ **"Since Liberation Day" is the poster's framing and WALTER did not verify the superlative.** **The 9/10 print being the deepest since 2025 is read off the chart's own band, not from a computed series.**
- **The two images are ONE claim** (a post and the full-size version of its chart) and are folded into this single signal — recorded as items 6 and 7 of `BM-20260911-02`, not silently merged.

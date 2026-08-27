## 2026-08-27 — LIQUID → REGINALD, HENRY, BOND (cc PROME)
**Signal:** The overnight repo distribution has gone from ~10bp below the IORB ceiling to ~1bp below it since 2023 — **while the policy rate itself fell.** The cushion between repo and the ceiling has been consumed.
**Priority:** 🟠 — structural, slow. **This is NOT a fire and NOT a threshold fire.** No gate is implicated; SOFR−IORB is **−1bp [obs 8/26]** and GATE-LIQ-079 needs +30bp. Routed because it is a five-year state change nobody has a row for, not because something broke.

### The measurement
`SOFR − IORB`, **median by year**, non-quarter-end sessions only (±4d around quarter ends excluded — Q-end turns print wide mechanically). Own FRED pull, full IORB era (IORB begins 2021-07-29):

| | 2021 | 2022 | 2023 | 2024 | 2025 | 2026 |
|---|---|---|---|---|---|---|
| **SOFR − IORB (median)** | −10bp | −11bp | −10bp | **−8bp** | **−5bp** | **−1bp** |
| IORB level (median) | 0.15% | 1.65% | 5.15% | 5.40% | 4.40% | 3.65% |

**Monotonic from 2023.** ★ **The load-bearing feature is that it runs AGAINST the policy level**: IORB *fell* 5.40% → 3.65% across the same span while the spread *rose* ~9bp. A rates-level or ZIRP artifact would move the other way, so the obvious deflationary explanation does not reach this series. That asymmetry is the reason I am routing it at all.

### What it means, mechanically
Repo is the marginal use of cash for anyone who can also leave it at the Fed. IORB is the ceiling that arbitrage is supposed to enforce. **When the whole repo distribution sits 10bp below the ceiling there is a fat cushion of reserves willing to be lent into repo; at ~1bp there is almost none.** The cushion is not a forecast — it is the observable width of that arbitrage, and it has been closing for three years without interruption.

⇒ **This corroborates my Leg A** (KB-LIQ-067 / KB-LIQ-070: RRP exhausted → post-QT, reserves absorb TGA/settlement swings directly with no buffer) **from an instrument Leg A does not use.** Leg A was built on RRP and reserve *balances*; this is the *price* saying the same thing independently.

### Per desk — why you specifically
- **REGINALD** — this is your banks' marginal funding arbitrage measured directly. The incentive to lend reserves into repo rather than park at the Fed is ~1bp wide. It does not tell you a bank is stressed; it tells you the shock absorber between a funding shock and bank funding costs has thinned to almost nothing. Reconcile to one figure with me if you carry a repo-vs-IORB read.
- **HENRY** — amplification input. The same event that cost 5bp in 2022 has less room to be absorbed before it moves a price. No cascade threshold implicated; this changes the *conversion rate* from shock to move, not any level you hold.
- **BOND** — front-end / floor-system relevance, and it is adjacent to the sb0607 buyback question you are adjudicating. Yours if you want it; I am not making a rates call.

### ⛔ Explicitly retracted — do NOT carry this half
Earlier today I circulated a second leg: *"the 75th percentile is pulling away from the mean = dispersion widening, the tail paying up."* **That is retracted.** The wedge (SOFR75−IORB minus SOFR−IORB) by year is **+0 · +2 · +5 · +6 · +6 · +6** — one move, 2022→2023, which is exactly the exit from ZIRP (at IORB 0.15% there is no room for bp dispersion). **Flat for four years. There is no ongoing dispersion widening.** It was the more eye-catching half and it was the wrong half. If you received the earlier version from me or from PROME, this supersedes it.

### Provenance, stated plainly
This finding was **born inside a correction of my own error** and I got it wrong twice before it was right. My original claim rested on a base rate computed over a window I had truncated with a fetch limit (I quoted 59.9%; the true full-window figure is 30.7%). The surviving leg above is the part that passed an adversarial test — specifically the ZIRP/level alternative, which killed its sibling and could not touch it. **Weight it as one instrument agreeing with Leg A, not as confirmation of anything.**

### Instrument
`AGENTS/LIQUID/scripts/sofr_dispersion.py` — deviation (base-rated robust z) and drift (slope + percentile, deliberately unbanded) reported separately. `--selftest` (10 checks) · `--baserate` (reprints realised fire rates). Live read: **🟢 z +0.0, ordinary for the current regime · regime tightening +7.1bp/yr (p75 of its own history)** — i.e. today is unremarkable, the *trend* is the datum.

**Source:** own FRED pull (SOFR, SOFR75, IORB), full IORB era through obs 2026-08-26. **Basis:** FRED end-of-day, T+1; non-quarter-end filtered.

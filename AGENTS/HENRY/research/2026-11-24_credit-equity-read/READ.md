# HENRY — D:L1249 grade + credit-to-equity read, Tue 2026-11-24 night (23:20–23:5x ET)

Session henry-desk-agent-2026-11-24, woken by PROME (prome-77) on Will's word 23:19 ET ("wake LIQUID and HENRY now"). Claude Code, Opus 5.5 (`claude-opus-5-5`), laptop. Markets closed; every quote below is labelled with its session and basis. The fleet was offline about 20:55 ET 11/23 to 22:20 ET 11/24, so this due row is a day late.

## 1. The answer first

**Equities and credit are on two different clocks.** The 11/20 high-yield jump (+24bp to 376) and its partial retrace on 11/23 (−13bp to 363) are an echo of the Nvidia governance shock: they move with the chip complex day by day. The larger widening is not an echo of that shock. High-yield spreads rose about 100bp from 266 (9/21) to 363 (11/23), and the move started in late September, about two weeks before the S&P peak of 10/6 and eight weeks before the Nvidia episode. Over that same widening, the average S&P stock (equal-weight RSP) is flat: 212.68 (9/21) to 213.96 (11/24). The cap-weighted index fell 7.90% from its peak through 11/24, and almost all of that is the AI and chip complex (SMH −32.5% from 10/6). **So at the broad level equities are diverging from credit, not following it; what the market has priced is a mix change (defensives up 10–12%, cyclicals and small caps down about 5%), not a level change.**

Tonight's tape (11/24) is the cleanest single-day picture of the one-complex shock: chips −7.3% (SMH), Nvidia −5.86%, AMD −8.86%, while equal-weight +0.54%, the Dow +0.85%, small caps +0.53%, KRE +0.32%, and HYG −0.12% (vendor closes, 11/24 session). Credit did not follow chips down tonight.

## 2. D:L1249 grades, by their written letters (no level, operator, instrument or consequence changed)

| Marker (where written) | Letter | Observation (session, basis) | Grade |
|---|---|---|---|
| 11/21 upside marker (`research/2026-11-21_close-read/CLOSE.md` line 72) | "a close over about 7,200 with VIX under 30" | **11/23: S&P 7,237.17, VIX 26.62 (FRED SP500 and VIXCLS 11/23, first published).** 11/24: S&P 7,201.09, VIX 26.36 (vendor ^GSPC and ^VIX daily bars of the 11/24 session, read 23:21 ET; FRED 11/24 not posted) | **MET on 11/23 on FRED** (37.17 over 7,200; VIX 3.38 under 30). **11/24 held by 1.09 points on the vendor bar, PROVISIONAL until FRED.** Consequence as written: the index is back in the thinner part of the negative book (see gamma row) |
| 11/23 line, V side (`research/2026-11-23_monday-read/READ.md` line 72) | "FRED HY 11/23 ≤ ~355 **and** an S&P close over the 200-day 7,331 and the flip band ~7,500" | HY 363 [FRED 11/23]; S&P 7,237.17 [FRED 11/23], 7,201.09 [vendor 11/24] | **NOT MET on both legs** (HY 8 over 355; S&P under 7,331) |
| 11/23 line, retest side (same line) | "HY 11/23 ≥ 376 while equities hold up, NVDA under ~146, or an S&P close back under 7,100" | HY 363; NVDA 165.05 [11/23], 155.38 [11/24 vendor]; S&P closes 7,237.17 / 7,201.09 | **NOT MET on any limb** (HY 13 under 376; NVDA 9.38 over 146; S&P 101.09 over 7,100) |
| ⚠️ Outcome-space disclosure | The 11/23 line named ≤355 and ≥376 and **named no verdict for 355 < HY < 376** | HY 363 landed in the unnamed middle | **NO VERDICT, by omission in my own letter.** This is the defect my LESSONS § "Enumerate the OUTCOME SPACE" names, n=5 now. I do not supply a reading after the fact. |
| HEN-65 (PREDICTIONS.tsv) | close ≤ 6,700.00 on any of 9 sessions 11/23–12/4 | 11/23 7,237.17 (FRED), 11/24 7,201.09 (vendor) | **OPEN, not hit.** 2 of 9 sessions done; 6,700 is 6.96% under the 11/24 close. Letter frozen at 0.40 |
| Red line (−10% from cycle peak, WQ-609 A) | 7,037.04 (peak 7,818.93 [FRED 10/6]) | 11/23 7,237.17 (200.13 over); 11/24 7,201.09 (164.05 over, vendor) | **Reclaimed on two closes** after the 11/20 fire (6,910.39). Yellow 7,200 and orange 7,100 also back above, yellow by 1.09 on the vendor bar |
| Dealer-gamma flip | `gamma_flip.py --both --source vendor`, 23:27 ET 11/24, vendor chain, after the close, **not published** (Cboe refuses this box since 11/20) | flip band **7,300–7,439** (14d / 35d); net gamma NEGATIVE at both (−17.7 / −54.6 $B per 1%, free-tier, assumption-dependent); put 7,000 at both horizons; call withheld (7,250 vs 7,400) | **Spot 99–237 points UNDER the flip: dealers still amplify moves both ways.** Flip lower than 11/23 midday (~7,443 / ~7,497); compare flips, not $B, across days |

Other levels, own calc on vendor ^GSPC closes through 11/24: **200-day 7,351.29, 50-day 7,609.91** (the 7,331.08 in STATUS was an 11/10 basis). VIX term: VIX 26.36, VIX9D 26.68, VIX3M 25.47 (vendor closes 11/24): still inverted (VIX3M/VIX 0.966). Treasury par 11/24: 2Y 4.63, 10Y 4.91, 30Y 5.30 (11/23: 4.63, 4.92, 5.29) — rates did not move on the chip selloff.

⚠️ The VIX printed 30.00–30.40 in the vendor pre-open feed 08:13–08:20 ET 11/24 (WALTER SIG-W-20261124-001; preceded by a five-bar 32.38 run WALTER reads as a bad tick). The regular-session high was 29.57 and the close 26.36, so the marker's "VIX under 30" is a close condition and is met; the early-session print is disclosed, not graded.

## 3. Evidence table — breadth and leadership (vendor daily closes, yfinance, 11/24 session read 23:23 ET; file `closes_vendor_2026-10-01_to_11-24.csv`)

| Series | 10/06 peak → 11/12 | 11/12 → 11/19 | 11/19 → 11/20 (shock) | 11/20 → 11/24 | 11/24 day | 10/06 → 11/24 |
|---|---:|---:|---:|---:|---:|---:|
| S&P 500 (cap-weight) | −2.90% | −5.49% | −3.70% | +4.21% | −0.50% | **−7.90%** |
| RSP (equal-weight) | +3.95% | −4.12% | −1.98% | +3.14% | +0.54% | **+0.77%** |
| SMH (chips) | −20.68% | −10.81% | −10.60% | +6.67% | −7.26% | **−32.53%** |
| NVDA | −30.53% | −12.16% | −14.01% | +23.78% | −5.86% | −35.05% |
| IWF growth / IWD value | −10.06 / +4.37 | −6.84 / −4.27 | −6.02 / −1.63 | +6.07 / +2.64 | −1.77 / +0.63 | −16.49 / +0.88 |
| IWM (small caps) | −1.03% | −5.11% | −2.88% | +4.10% | +0.53% | −5.05% |
| XLP / XLV (defensives) | +11.32 / +12.41 | −1.32 / −5.52 | +0.67 / −0.12 | +1.57 / +4.22 | +1.66 / +2.95 | **+12.32 / +10.55** |
| XLI / XLE (cyclicals) | −1.25 / +0.91 | −4.77 / −5.35 | −3.09 / −0.62 | +3.35 / −0.10 | −0.53 / +0.97 | −5.81 / −5.18 |
| XLY / XLF | +7.82 / +7.78 | −3.80 / −4.52 | −2.95 / −1.82 | +4.68 / +2.82 | +0.68 / +0.83 | +5.37 / +3.89 |
| KRE (regional banks) | +3.50% | −4.50% | −1.36% | +2.11% | +0.32% | −0.44% |
| HYG / LQD | −0.38 / +0.89 | −0.58 / +0.03 | −0.26 / +0.59 | +0.13 / +0.10 | −0.12 / −0.13 | −1.09 / +1.62 |
| **HY OAS (FRED, bp)** | 303 → 320 | 320 → 352 | 352 → 376 | 376 → 363 [11/23] | not posted | **303 → 363** |

RSP/SPY ratio: 0.2725 (10/6) → 0.3007 (11/20, the high of the window) → 0.2977 (11/24), +9.2% for equal-weight. HY OAS 9/21 266 → 10/1 324 (+58 in eight sessions, before the equity peak) → 10/6 303 → 10/30 344 → 11/12 320 → 11/20 376 → 11/23 363 (FRED first-published).

**Reading by window:**
- **9/21 → 10/6:** credit widened about 37bp while the S&P made its high and chips rose: credit early, equities not following.
- **10/6 → 11/12:** cap-weight −2.9%, equal-weight +3.95%, chips −20.7%, defensives +11–12%. A concentrated AI de-rate with a defensive rotation; credit drifted 303 → 320.
- **11/12 → 11/19:** broad decline (equal-weight −4.12%, KRE −4.50%, small caps −5.11%) with HY 320 → 352. This window is **not** one-company: it is the hot CPI and PPI, 10Y over 5%, hawkish minutes week, and credit and the broad market fell together.
- **11/20:** the Nvidia shock: chips −10.6%, equal-weight −1.98%, HY +24. Credit moved with the shock.
- **11/23 → 11/24:** the broad market recovered all of 11/20 (equal-weight +3.14% from the 11/20 close) and credit recovered half (HY −13 of +24; HYG +0.13% after −0.26%). Chips gave back most of the 11/23 jump on 11/24 without credit or the broad market following.

**Verdict on PROME's two framings:** tonight's evidence fits **"credit is an echo of a one-company equity shock" for the 11/20 spike only.** It does **not** fit it for the trend: about 86bp of the 97bp widening since 9/21 happened before 11/20 (266 → 352), and it began before the equity peak. Nor does the evidence say "equities have not priced it" cleanly: the defensive-over-cyclical mix (XLP +12.3%, XLV +10.6% vs XLI −5.8%, XLE −5.2%, IWM −5.1% since 10/6) is a partial pricing of slower growth, while discretionary (+5.4%), financials (+3.9%) and KRE (−0.4%) are not pricing a credit cycle. **Best statement: credit has been leading a slow, rates-and-tail-driven tightening that the broad equity market has priced only in its mix; the headline index fall is a separate AI-complex story that credit echoed for one day.**

⚠️ What this does not establish: cause. I have no instrument here that splits the HY widening into rates, AI-financing issuers, and the consumer-credit tail. CCC moved +356bp over about three months against BB +63bp (credit_monitor.py, FRED 11/23), so the tail carries much of it; DEWEY's 10/23 read was that the rated CCC tier is not AI-led. WALTER's 11/24 small items (CoreWeave CDS +293bp on 11/20, GPU lenders cutting loan-to-value to 50–60%, a $500M data-center debt auction fizzling) are titles and posts, unverified. REGINALD's WQ-512 single-issuer rider and LIQUID's funding read are the owners of that split.

## 4. What a credit fire of this kind has been followed by (own calc; `hy_fire_event_study.py`, outputs beside it)

**Definition (mine, chosen in this session, unregistered):** HY OAS over 350bp on three consecutive closes (REG-T-04's shape) with no earlier completed three-close run in the prior 60 sessions — a "fresh" fire from a calmer regime. Data: FRED BAMLH0A0HYM2 spliced with VIOLET's frozen archive 1996-12-31 → 2026-04-09 (exact agreement on all 621 overlap days); S&P = vendor ^GSPC closes.

| Fire (3rd close) | HY at fire | HY change that day | S&P off 120-day high at fire | S&P +10 / +20 / +40 / +60 sessions | Worst within 40 | HY +10 sessions | HY peak within 60 |
|---|---:|---:|---:|---|---:|---:|---:|
| 1998-08-11 | 375 | +17 | −9.9% | +2.2 / −5.9 / −9.2 / +4.6 | −10.4% | +48 | 678 |
| 2005-04-04 | 359 | +4 | −4.0% | −2.6 / −1.2 / +1.3 / +2.2 | −3.3% | +39 | 457 |
| 2007-07-26 | 413 | +42 | −4.5% | −2.0 / −1.4 / +2.9 / +1.2 | −5.1% | −9 | 479 |
| 2021-11-30 | 367 | +14 | −2.9% | +1.5 / +4.9 / −5.3 / −4.0 | −5.3% | −32 | 393 |
| 2024-08-06 | 367 | **−26** | −7.5% | +6.8 / +5.3 / +9.0 / +10.9 | −0.8% | −42 | 367 |
| 2025-04-07 | 461 | +16 | −17.6% | +4.5 / +10.8 / +17.9 / +24.0 | −1.6% | −62 | 461 |
| **2026-11-23** | **363** | **−13** | **−7.4%** | — | — | — | — |

- **n = 6.** Medians: +1.85% at 10 sessions, +1.85% at 20, +2.1% at 40, +3.4% at 60; the S&P was higher 60 sessions later in 5 of 6. With a 120-session lookback n = 5 and the picture is the same.
- **The split that matters is the next ten sessions of credit, not the fire itself:** where HY kept widening (1998, 2005), the S&P was lower 20 sessions out in both; where HY narrowed within ten sessions (2021, 2024, 2025), it was higher 20 sessions out in all three. 2007 is the warning case: HY eased briefly, the S&P was up modestly at 60 sessions, and the bear market started in October, outside the window.
- **The only fire whose third close was itself a narrowing is 2024-08-06** (the yen-carry shock), the closest shape to today: S&P +5.3% at 20 sessions. That is one case.
- **Limits:** six cases across very different regimes; the definition and lookback were chosen in-session (my first version excluded 2025-04-07 through a definitional error — a single print over 350 four sessions earlier — and I corrected the rule to "no earlier completed run", disclosed here); worst-within-40 of about −4.2% is near the unconditional rate (35% of all days since 1997 see a 4.2% dip within 40 sessions, n=7,521); none of the six had today's AI concentration. This is a description of the record, not a forecast instrument.

**H4 (Credit-Primary Rule) read-through:** if 376 [11/20] was the HY peak, the S&P low 6,910.39 [11/20] coincided with it, which is consistent with H4, not a test of it. H4 stays untested.

## 5. Forward view, proportionate (unscored; nothing registered)

**Horizon 11/25 → 12/16.** Dated events: Wed 11/25 08:30 ET October PCE, Q3 GDP second estimate and durable goods (PCE is mine to log); Thanksgiving 11/26; half-day 11/27; ISM 12/1 and 12/3; payrolls 12/4 (LABOR); Nvidia's late quarterly report about 12/4 (date per PROME's brief, not verified here; VULCAN's read); FOMC 12/9 (HEN-63, a hike, 0.70); CPI 12/10; PPI 12/15; the Optimum grace period ending about 12/16 (REGINALD/LIQUID's single-issuer item; a default would add to the HY index mechanically); quarterly options expiry 12/18.

| Path | My odds | What it looks like | Why |
|---|---:|---|---|
| **Narrow, two-way range (base case)** | about 50% | S&P mostly 7,000–7,450; chips swing on Nvidia and AMD news; equal-weight holds; HY 340–380 without a new high | Breadth is intact and credit narrowed on the fire day; dealers short gamma under 7,300–7,440 make the swings large both ways, worse in thin holiday sessions |
| **Credit-led broadening** | about 30% | HY closes over 376 (a new 2026 high), equal-weight, small caps and KRE join the fall, S&P closes under 7,037.04 and tests 6,910 | A hot PCE 11/25 and a hike with hawkish projections 12/9 (Williams 11/23 would not exclude consecutive moves, WALTER 012) tighten financing; an Nvidia disappointment; the Optimum date |
| **V repair** | about 20% | HY back to 330 or lower (REG-T-04's exit is five closes ≤330), S&P over the 200-day 7,351 and the flip ~7,440 | Base rates after fresh fires lean up at 20–60 sessions (5 of 6); the 2024 shape |

- **S&P close under the red line 7,037.04 by 12/4: about 35%** (base rate 41%, n=115: closes since 1990 with VIX 23–30 and a 6–12% drawdown, any of the next 7 closes 2.28% under; shaded down for breadth and the narrowing credit fire). **By 12/16: about 45%** (base 55% over 15 sessions). Down from my 11/23 figure of about 45% to 12/4.
- **HEN-65 (≤6,700 by 12/4): current view about 5%** (base 2%, same sample; 11% over 15 sessions). The letter stays frozen at 0.40; if it resolves NO it scores Brier 0.16.
- **What would change my mind toward broadening:** HY over 376 on a day equal-weight also falls; KRE under $65 (yellow); HYG under about $75.50 (my 11/21 downside marker); CCC−BB widening while the S&P rises. **Toward the V:** HY at or under 330 and falling with an S&P close over 7,351 and ~7,440; RSP/SPY holding near 0.30 while chips stabilise.
- **Material and resolvable, but not registered tonight:** the broadening call (HY new high and equal-weight down together by 12/16) is a candidate letter. I did not register it: a letter needs its outcome space enumerated first (§2's middle-region miss is tonight's reminder), and the session is already late. Named as UNSCORED.

## 6. Gaps

- FRED SP500 and VIXCLS 11/24 and FRED HY 11/24 not posted at 23:2x ET; the 11/24 grade is PROVISIONAL on vendor bars.
- Gamma is a vendor chain after the close, not publishable; Cboe refuses this box (403 since 11/20). ⚠️ My boot ran `boot.py` with the default `--source auto`, which sent one request to Cboe before falling back; the refusal was not worked around. Next session runs `--source vendor`.
- No instrument splits the HY widening by cause (rates / AI-financing / consumer tail); owners REGINALD and LIQUID.
- The Nvidia report date (about 12/4) is from PROME's brief, unverified here.
- Breadth used sector ETFs and RSP; no advance-decline or new-highs data was pulled.

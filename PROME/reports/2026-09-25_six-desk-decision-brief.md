# Six-desk decision brief — the rates break, what transmitted, and what is still unproven
**Written:** 2026-09-25 01:13 ET (`prome-fa`) · **Authority:** Will 01:01 ET 9/25, *"Coordinate one bounded follow-up across the current group … return one decision-focused brief."* · **Inputs (verbatim owner artifacts, cited never re-derived):** VIOLET `6f867bc94` · HENRY `AGENTS/HENRY/research/2026-09-25_rates-move-and-hike-alignment.md` · BOND `AGENTS/BOND/analysis/2026-09-25_rates-move-TP-columns_and_FR2004-timing-RESOLVED.md` · LIQUID `AGENTS/LIQUID/reports/2026-09-25_credit-transmission-persistence.md` · ORACLE `AGENTS/ORACLE/research/2026-09-25_oct-hike-alignment-with-HENRY.md` · CATO `c93a66608`. **Every level is the 9/24 close or the 9/23 FRED cell; nothing here is live (root rule #4).** /bin/bash moved; no gate, threshold or position changed by this brief.

## The story in four sentences
Between the 9/22 and 9/24 closes the 10-year Treasury yield rose 22bp, every basis point of it real yield, and the futures curve for 2027–28 moved by about the same amount while the October meeting barely moved. That is a market pricing a higher policy path for years, not a bet on one meeting. The credit and volatility complexes moved with it on the day but nothing has followed through: only the weakest credit tier is unusual, funding is calm on every gauge we observe, and the MOVE-shock study that claimed a forward VIX signal was wrong. The one thing that changed for a decision in front of you is the statistic under WQ-157 leg ②, which does not survive a corrected instrument (WQ-290).

> ⚖️ **WQ-290** — Fix the FR2004 join window before ruling on WQ-157 leg ②? BOND resolved the settlement-timing question at the Fed's own instructions: dealer positions are trade-date, an award counts from the award day. Its join tool windows Wednesday auctions wrong (a third of the sample), and on the corrected window the "pairing inverts, p=0.009" headline reads −4.5bp, p=0.248. **Rec: YES, let BOND fix it, keep the old numbers as history, and rule leg ② on the corrected ones. Leg-② rec stays PARK.** Needed by 10/1.

## 1. Observed changes (measured, dated, owner-sourced)

| What moved | Figure | Dates / basis | Owner |
|---|---|---|---|
| 10Y nominal | 4.96 → 5.18 (+22bp) | 9/22c → 9/24c, Treasury par | HENRY |
| 10Y real | 2.63 → 2.85 (+22bp); breakeven 2.33 flat | same; Treasury real curve (FRED DFII10 9/24 publishes ~9/25 16:15 — the T12S anchor cell) | HENRY · BOND |
| Curve | 2Y +16 · 5Y +20 · 10Y +22 · 30Y +18: bear-steepening, belly-led | 9/22→9/24 | HENRY |
| Futures policy path | post-Oct EFFR **+4.0bp** · post-Dec **+4.0** · 3M SOFR Dec-27 **+19.0** · Dec-28 **+22.5** | vendor last trade ≤15:00 ET, not CME settlement | HENRY |
| ACM term premium | 9/15→9/23: path +16.0, TP **−6.4** · **but 9/22→9/23 alone: TP +7.0 of +15** | NY Fed daily, frontier 9/23; ACM 9/24 unpublished | BOND |
| KW term premium | 9/15→9/18: −0.5 (vs ACM −7.3 = 6.9bp model gap) | FRED weekly, frontier 9/18 | BOND · HENRY |
| 9/23 5Y auction | indirect 54.31% (lowest since 3/2020) · BTC 2.21 · dealer 15.77% (ordinary) | BOND | BOND |
| Dealer long-end stock | −.8B total; +.7B in 11–21Y (the 20Y award's bucket) | FR2004 as-of 9/16, **now admissible** (trade-date) | BOND |
| Credit ladder | IG 77 · BBB 95 · BB 159 · B 278 · CCC 1,093 · HY 273; 15-session: CCC +40 (82nd pct), B +2, BB +6, BBB −4, IG −4 | FRED 9/23; 9/24 cells ~9/25 16:15 | LIQUID |
| Funding | SOFR−IORB −3 · SOFR99−IORB +5 · SRF ~/bin/bash · RRP /bin/bash.46B · reserves ,930B (−3.6B w/w on TGA +00B) | 9/23, date-matched | LIQUID |
| Vol complex | VIX 15.67 · VVIX 90.57 · MOVE 104.58 | 9/24; **CBOE has not published 9/23 or 9/24 history** (checked 01:08 ET) | VIOLET |
| October hike, aligned | futures **+18.0bp** vs Polymarket **+16.5** vs Kalshi **+16.1–16.6** expected change | 15:00 ET 9/24, same event, same units | HENRY · ORACLE |

## 2. Inferred mechanisms — competing explanations, what supports each, what cuts against it

**(A) Policy-path repricing, "higher for longer" in 2027–28.** *Support:* the far futures moved as much as the 10Y while the near path moved 4bp; breakeven flat, so not inflation compensation; ACM assigns the FOMC week to path and shows premium falling in net; funding calm; the 5Y dealer takedown ordinary; the 9/16 dealer print shows no warehousing. *Against it:* on the single biggest day, 9/23, ACM puts +7.0bp of the +15 into term premium, on the day of the weakest 5Y foreign share since 2020; on 9/24 the 10Y rose 7bp while the futures path moved 1–2bp at every horizon (HENRY's own instrument disowns that day); and the 2027–28 SOFR contracts carry their own risk premium, so they cannot separate (A) from (B) at that horizon. **Preferred by both HENRY and BOND, for the window as a whole; both say 9/23–9/24 is contested.**

**(B) Term premium / supply absorption.** *Support:* belly-led bear-steepening (a hiking repricing classically flattens, as 8/26→9/16 did); the move landed on the 5Y composition failure; 30Y at a 2004 high; KW premium at a 2026 high on 9/16. *Against it:* over the FOMC week both models put premium down or flat; funding never moved; dealers did not warehouse the 20Y; and every "premium" figure is a model output, with the two models 6.9bp apart on the only window they share.

**Credit and vol are not a third mechanism; they are the same day.** LIQUID: transmission CONTINUES at the bottom rung only, at an ordinary pace, not BROADENS (IG and BBB tightened over three weeks), not REVERSES (CCC at 2026 highs); the reach into B was one day. VIOLET: rates vol and equity vol moved on the same days with rates moving further; the RQ #8 study that claimed a forward VIX signal had a return-clock defect (CATO found it, PROME verified at the saved data, VIOLET corrected) and **the corrected ten-event sample does not establish a forward VIX signal in either direction.** ORACLE: the venues and futures agree on the October meeting once aligned; the ~1.5–2bp residual sits inside the event basis and is not a disagreement.

## 3. What is unresolved, who owns it, and the next observation that decides it

| Question | Owner | Next useful observation | When |
|---|---|---|---|
| Was 9/23–9/24 path or premium? | BOND · HENRY | ACM 10Y for 9/24 (≈T+1); KW for 9/21–9/25 (weekly) | ~9/25 · next KW post |
| Did dealers absorb the failed 5Y? | BOND | FR2004 as-of **9/23** (the corrected window; not 9/30) | ~Thu 10/1 16:15 ET |
| Does credit transmission broaden, stall or reverse? | LIQUID | the 9/24 ICE OAS cells, graded on the pre-registered §1c rule (fourth outcome STALLS added) | ~9/25 16:15 ET |
| Quarter-end: seasonal turn or persistent pressure? | LIQUID | P1–P5 registered: SOFR−IORB ≥+1 on 10/5 AND ≥0 on 10/7 · SOFR99−IORB ≥+22 on 10/2 · SRF >B 10/1–10/5 · reserves <.8T — **PERSISTENT = (P1∧P2) ∨ P3 ∨ P4 ∨ P5, else SEASONAL** | verdict on the 10/8 prints |
| Is the vol complex where the delayed quotes say? | VIOLET | CBOE history CSVs for 9/23 + 9/24; CFTC TFF VIX as-of 9/22 | next post-close boot · Fri 15:30 ET |
| Is the real-rate leg a regime? | NEXUS (BOND data) | the 9/24 DFII10 cell = `GATE-NEXUS-T12S-DFII10` anchor (±10bp band over 15 cells) | ~9/25 16:15 ET |
| Does WQ-157 leg ② survive the corrected instrument? | Will (WQ-290) · BOND | BOND's re-run is already on file; the fix is the decision | by 10/1 |

## 4. Kept visible — today's and next week's obligations (unchanged by this brief)
- **Fri 9/25:** BG-02 grades **17:00 ET** (BRENT; lapse modal) · **VLO F1 crack at the CME settle** (TERRY grades; HENRY's estimate sat ~/bin/bash.36 above the line 9/24; estimate-only within ±/bin/bash.15 = UNKNOWN, blocks a fire) · **gamma board re-measure at the close** (HENRY; no current gamma-sign claim is publishable until then) · COT #7 ~15:30 · rigs · FLG-T08 pre-fire check (PROME) · the T12S anchor cell.
- **Wed 9/30:** **004 TLT Sep-30 77P ×20 expires** (TERRY's card; 77P bid /bin/bash.01 / ask /bin/bash.02 [TERRY 9/24 13:51, one vendor]; thesis-side exit MOOT; **NO ADD, WQ-280**) · WPSR · FERT-G5 · LIQ-072/076 · quarter-end turn (LIQUID's null).
- **Mon 9/28:** ORACLE's October 10 re-pin (DOCKET L299) — if no October market lists by the 10/1 03:59Z September close, v5 dies and a new strike is Will's call.
- **Thu 10/1 → Thu 10/8:** FR2004 as-of 9/23 · LIQUID's P1–P5 prints.

## 5. Corrections made tonight, so no stale figure travels
- VIOLET RQ #8 v1 (+12.4% / 1.68σ) **WITHDRAWN**; KB-VIO-312 supersedes; PARKED per Will (schema has no PARKED token — CONFIRMED with an operational annotation; a DAEDALUS schema question, not VIOLET's).
- ORACLE KB-ORC-097 (~11–12pp venues-under-CME) **SUPERSEDED** by KB-ORC-100 (aligned bp).
- BOND KB-BND-327 (FR2004 excludes unsettled awards) **CORRECTED** by KB-BND-332; the 9/23 5Y dealer read moves from ~10/8 to ~10/1.
- HENRY's first draft ("both models say premium did not rise") **corrected in-file** before delivery: a window net hid the 9/23 day.
- LIQUID's 9/17-vintage BOTTOM LINE re-cut to obs 9/23; banner removed.
- **Not quotable:** "72% October" without its basis (HENRY computation, FedWatch method, vendor last trade, ±2pp); "venues lag futures by X"; any Brent 9/23–9/24 level not published by BRENT; any current gamma sign.

## 6. Verification repair (Will's item 5, WQ-289 (b), DOCKET L473)
IMPLEMENTED · TESTED (16 new tests + 84 existing pass) · **independent-reader state and residue are recorded in the closeout receipt, not asserted here in advance.**

## Coverage gaps that survive (owners' own lists, not softened)
FRED ICE history is a rolling ~3 years, so every credit percentile is ranked against a calm window (LIQUID) · tri-party volumes/haircuts, sponsored repo, dealer balance sheets, MMF flows, FX basis not observed (LIQUID) · futures prices are vendor last trade, CME settlement blocked (HENRY) · ACM 9/24 and KW 9/21+ unpublished (BOND) · the 9/17 p=0.009 came from an unsaved script at n=224; the as-shipped reproduction at n=228 gives p=0.019 (BOND) · CBOE 9/23–9/24 history unpublished; delayed quotes can differ from the history close by up to 0.25 (VIOLET) · the RQ #8 low-VIX analog rests on n=1 (VIOLET).

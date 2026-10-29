# MANAGEMENT CARD — GLD 25 shares — decision rails (Will's choices; no recommendation)
**Date:** 2026-10-24 Sat (written 14:4x ET, clock from `date`) · PROME spawn, WQ-513/514 workstream
**Setup ID:** `MGMT-GLD-SHARES-OCT24`
**Terry verdict:** CONDITIONAL — management rails for a held line; Will's choices, no recommendation, nothing approved by this card.

> **Holding update 2026-10-29 (Will's Fidelity capture):** 28 shares (was 25), basis $10,489.53, value $10,315.48 at $368.41 = 28.04% of the account. Rails unchanged; every choice stays Will's.
**Commission:** PROME's reading of an ask Will made (PROME SCRATCH "Will's ask, not given"); Will may correct the reading. $0 moves; any order is Will's hand (root rule #5).
**Thesis owner:** MIDAS. WQ-451 decomposition letter `AGENTS/MIDAS/gold/research/2026-10-23_WQ451-decomposition-letter.md` (committed `a35faa6f8`; header stamp corrected `829683272`, invalidation lines unchanged between the two). 10/20 outlook `AGENTS/MIDAS/analysis/2026-10-20_GLD-OUTLOOK.md`.
**Data freshness:** GLD **$366.61 = 10/23 regular-session close** (`FORGE/tools/market-data/fetch.py price GLD`, pulled 2026-10-24 14:42 ET; HEARTBEAT's $366.00 was an intraday read). Position truth: **25 shares, basis $9,390.78 (avg $375.63)**, Fidelity Traditional IRA, 10/22 11:01 ET capture (`PROME/data/2026-10-22_broker-capture-TRANSCRIPTION.md` row 13; FORGE `ec5a7058b`); the 10/23 activity shows no GLD order. DFII10, DXY and trust tonnes are MIDAS's 10/22 readings.

## 0. Missing inputs / hard caveats
- [x] Live price checked (10/23 close; markets closed) · [x] position truth (10/22 capture + 10/23 activity) · [ ] a positions capture after 10/23
- [x] Entry half: the 24 + 1 shares were bought by Will before this card. Entry fields are **UNRECOVERABLE** and are not reconstructed (construction rule #20); this card is management-only
- [ ] GLD trust tonnes for 10/23 not read (latest 1,045.64 t, 10/22, PRIMARY issuer via MIDAS)
- ⚠️ MIDAS's beta has R² 0.15 (about 85% of daily variance is outside the model); haven and liquidation samples are n = 5 and n = 11. Dollar figures keyed to the beta are MODEL

## 1. What the holding expresses (MIDAS's reading, not TERRY's)
GLD is **a bet on falling real interest rates and long-run demand for gold** (central-bank buying shows up monthly, not daily). Gold did not reliably hedge equity declines in MIDAS's 120-session sample (**2 of 12** stress days up, S&P ≤ −1% or VIX +2; average −1.82%; 6 of 24 in 2026). **Its hedge value for this bearish-option book is unestablished:** that needs the book's own daily P&L against GLD, including rallies and time decay, not equity-stress days. **10/22 graded LIQUIDATION:** GLD −2.63%, residual −4.46% (3.2 sd), trust −11.98 t, while the 10-year real yield fell 12 bp (MIDAS letter §6). That one observation does not resolve the book-offset question.

## 2. Position, in figures (10/23 close)
| Item | Figure |
|---|---|
| Value | 25 × $366.61 = **$9,165.25** |
| Open P/L | **−$225.53** vs $9,390.78 basis |
| Share of account | **23.0%** of $39,876.06 (10/22 displayed total; 10/23 total unknown) — the book's largest line |
| Versus the $500-per-card default | 18.3× one card by value (the default binds TERRY's cards; the shares were Will's hand) |
| 2026 record close | $495.90 (2026-01-29, MIDAS) — the line is 26% below it |
| Account type | Traditional IRA: a sale has no tax consequence; realized P/L only moves cash inside the account |

## 3. MIDAS's invalidation lines, and what each means for 25 shares
| Line (MIDAS §5) | Reading | Distance | Dollars for 25 shares | What it invalidates |
|---|---|---|---|---|
| **1-month downside:** GLD close **< $360.71** | $366.61 | **−1.61%** (one −1.6% day) | at the line: value $9,017.75 = **−$147.50** from the 10/23 close, **−$373.03** vs basis | the 10/20 "neutral to slightly lower" one-month path; a **price-path** line, not the thesis |
| **1-month upside:** GLD close **> $391.08** | — | +6.67% | value $9,777.00 = +$611.75 from close, **+$386.22** vs basis | the "slightly lower" path on the upside |
| **3-month:** trust **< 1,035.70 t** | 1,045.64 t [10/22] | 9.94 t of room | no price mapping | **the accumulation premise** (structural demand) |
| **3-month:** DFII10 **≥ 3.00%** ×5 Treasury prints | 2.64% [10/22] | +36 bp | MODEL at −0.1526%/bp: −5.49% ⇒ ≈ $346.47, value $8,661.75 = **−$503.50** from close, −$729.03 vs basis | **the real-rate leg** (rates surge) |
| **3-month:** DXY **≥ 105.0** ×5 closes | ~101.8 | +3.1% | no fitted DXY sensitivity in the letter; not converted | the dollar leg |
| **3-month:** a **second LIQUIDATION day** by 11/05 **and** tonnes ≤ −20 t since 9/30 | first case 10/22; ~−10 t since 9/30 | — | a day like 10/22 (−2.63%) costs ≈ **−$241** on 25 shares | de-risking is continuing, not one day |

**MIDAS's consequence:** any 3-month line crossed ⇒ MIDAS withdraws its positive lean to neutral and reports to PROME and TERRY. The 1-month lines re-price the outlook only.

**Other dated reads on this line:** MIDAS L1 grade at the 11/05 close (retrieved 11/06): SUPPORTED if the S&P closes ≥ 7,757.17 on any session through 11/05 and tonnes ≥ 1,045.64 t; FALSIFIED if stress clears and tonnes ≤ 1,035.64 t · SAFE October reserves ~11/07 (≥ +10 t supports) · TIC ~11/18 (sign only, ZHAO/SAM) · MIDAS-13: any GLD close ≥ $378.95 by 11/20, P 0.50 (MIDAS `workbook/PREDICTIONS.tsv`).

## 4. The rule TERRY applies to shares, and why
Root rule #7 (*"Roll duration, don't trim size. Trimming = thesis broken. Rolling = timeline uncertain"*) is written for options: a share has no expiry, so there is no duration to roll. **What carries over is its test: size changes on a THESIS break, not on price noise.** Applied here:
1. **The 1-month lines are price-path lines.** Crossing $360.71 says the near-term path is worse than MIDAS's outlook; it does not break the real-rate / structural-demand thesis. On TERRY's rule it is **not by itself a trim signal**.
2. **The 3-month lines are MIDAS's registered premise tests.** Any one crossed makes MIDAS withdraw its positive lean to neutral. A neutral outlook does not by itself falsify every premise or select a position action; read which premise failed with MIDAS's grade.
3. **Construction rule #23 (name the driver):** if GLD rallies, name the class (RATE / HAVEN / DE-DOLLAR proxy / UNEXPLAINED) on MIDAS's instrument before any add; a rally the thesis did not underwrite is evidence about the tape, not for the holding.
4. **The purpose question is Will's.** The equity-stress sample does not test whether GLD protects a bearish put book against its losses, so no position-action branch follows from the 2-of-12 count. For the real-rate and long-run-demand reading, no 3-month line was crossed in the 10/22–10/23 inputs. Any subsequent owner grade must name the affected premise; a change to neutral alone is not a blanket thesis-break finding.

## 5. Will's choices, with sizes (none recommended)
| Choice | Size | Dollars at $366.61 (10/23 close) | Effect |
|---|---|---|---|
| **HOLD** | 25 shares | $9,165.25 at risk to the lines in §3 | GLD stays 23% of the account; a 3-month line or a second liquidation day re-opens the question |
| **TRIM — small** | sell 5 | ≈ $1,833 to cash; realized ≈ −$45 vs avg cost | GLD ≈ 18.4% of the account |
| **TRIM — half** | sell 12 | ≈ $4,399 to cash; realized ≈ −$108 | GLD ≈ 12.0% |
| **EXIT** | sell 25 | ≈ $9,165 to cash; realized ≈ −$226 | no gold exposure; the real-rate bet is gone with it |
| **ADD** | 1 share (≈ $367, inside the $500 default) | — | **no fired trigger exists for a gold add**; under the standing rule fresh capital deploys only on a fired trigger, so an add is Will's choice outside the default. A trigger he could choose (PROPOSED here, not registered): MIDAS L1 grades SUPPORTED at 11/06, with the add's driver named per #23 |

Limit prices for any sale or add come from the broker at the time (durable finding 5b); every figure above is the 10/23 close, **refresh Monday before any use**. Day colour: root rule #6 governs puts and calls; this card applies no day-colour rule to shares.

## 6. Effective-N and book overlap
| Field | Entry |
|---|---|
| N_claimed | 2: real-rate leg · structural (official) demand leg |
| Shared antecedent | a real-rate surge (DFII10 ≥ 3.00%) also drives the dollar and ETF outflows: one event hits both legs |
| N_eff | ≈ 1.3 → read as ONE view |
| Book overlap | **Offset value is unestablished**; the 10/22 joint loss is one dated observation (GLD −2.63%, KRE +2.53%), not a hedge test. A real-rate surge would hurt GLD on MIDAS's real-yield fit (R² 0.15), while a rising nominal 10-year helps the regional puts on REGINALD's fit (KRE −0.72% per +10 bp, R² 0.13). Those are distinct yield measures and weak fitted associations, not proof of an offset |

## 7. Decision
- [ ] HOLD 25 · [ ] TRIM 5 · [ ] TRIM 12 · [ ] EXIT 25 · [ ] ADD 1 on a named trigger · [ ] REWORK: ____

**APPROVAL REQUIRED — Will must approve/reject before execution.**

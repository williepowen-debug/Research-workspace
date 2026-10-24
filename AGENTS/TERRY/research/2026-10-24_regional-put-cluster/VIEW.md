# Regional-bank put cluster — ONE bet, in figures (a VIEW, not a recommendation)
**TERRY · 2026-10-24 Sat (written 14:4x ET, clock from `date`) · PROME spawn, WQ-513/514 workstream.** Commission is PROME's reading of an ask Will made ("Will's ask, not given" in PROME SCRATCH); Will may correct the reading. **$0 moved. No card, no order, no sell or roll language on any held line** (`USER.md` § No expiry nagging — Will manages his own expiries).

> ⚠️ **Weekend data.** Underlyings are **10/23 regular-session closes** (`FORGE/tools/market-data/fetch.py price`, pulled 2026-10-24 14:42 ET). **Option bid/ask, marks and open interest are UNAVAILABLE**: the vendor feed returns Friday-vintage quotes with no timestamp, five of the eight held strikes show `NOBID` or a 160–200% spread (`chains/` not kept; durable finding 5b). Option values below are the **broker's 10/22 11:01 ET last**, the newest broker-verified mark. **Refresh Monday before any use.**

## 1. The lines (open per TERRY's ledger)
Source: the 10/22 11:01 ET Fidelity capture (`PROME/data/2026-10-22_broker-capture-TRANSCRIPTION.md`, mirrored at FORGE `ec5a7058b`). The 10/23 activity transcription (`PROME/data/2026-10-23_broker-activity-TRANSCRIPTION.md`, booked by TERRY `ff4a57005`) shows **no regional-bank order or fill**, so all ten lines are carried as open. A positions capture to confirm is owed (FORGE is not reconciled for 10/23).

| Line | Qty | Basis | 10/22 value | Strike vs 10/23 close | Breakeven at expiry |
|---|---:|---:|---:|---|---|
| KRE Nov-20 66P | 3 | $133.99 | $120.00 | 8.9% OTM ($72.46) | $65.55 (−9.5%) |
| KRE Nov-27 67P | 4 | $510.65 | $200.00 | 7.5% OTM | $65.72 (−9.3%) |
| KRE Nov-27 70P | 2 | $281.33 | $244.00 | 3.4% OTM | $68.59 (−5.3%) |
| KRE Dec-18 60P (two lots) | 2 + 3 | $1,391.36 | $145.00 | 17.2% OTM | $57.43 / $57.07 (−21%) |
| KRE Dec-31 65P | 2 | $337.33 | $164.00 | 10.3% OTM | $63.31 (−12.6%) |
| OZK Nov-20 40P | 4 | $322.65 | $20.00 | 21.0% OTM ($50.61) | $39.19 (−22.6%) |
| ZION Nov-20 62.5P | 2 | $435.33 | $130.00 | 5.6% OTM ($66.20) | $60.32 (−8.9%) |
| WAL Dec-18 65P | 4 | $682.65 | $220.00 | 14.6% OTM ($76.12) | $63.29 (−16.9%) |
| WAL Dec-18 70P | 2 | $551.33 | $320.00 | 8.0% OTM | $67.24 (−11.7%) |
| **Cluster** | **28** | **$4,646.62** | **$1,563.00** | — | **−11.76% uniform fall** |

**Not in the figures:** Robinhood WAL Dec-18 70P ×1 (`TRY-WAL-ROLL70`; Robinhood holdings unverified since 9/29) · FLG Mar-19-2027 10P ×4, limit $0.52, an OPEN order at the 10/23 capture, not a position (≈ $210 if filled; same lane).

## 2. Size, loss and share of the book
| Measure | Figure | Basis |
|---|---|---|
| Total basis (sunk) | **$4,646.62** | 10/22 capture |
| Max loss from here (forward) | **$1,563.00** = the remaining mark (construction rule #20(d)); all of it if every line expires out of the money | 10/22 broker last; 10/23 marks UNAVAILABLE |
| Already lost on paper | −$3,083.62 (−66%) | value − basis, 10/22 |
| Share of account | basis **11.65%**, mark **3.92%** of $39,876.06 | 10/22 displayed total; 10/23 account total unknown |
| Expiry clock | $1,683.95 of basis (36%) expires 11/20–11/27, 19–24 sessions out; $2,962.67 in Dec | |
| Versus the $500-per-card default | **9.3× one card** by basis, **3.1×** by forward risk; 5 of the 10 lines are individually over $500 | `PROME/STATUS.md` § Restrictions |
| In risk units (1R = $250) | **18.6R** basis, 6.3R forward | TERRY `STATUS.md` standing rules |
| Versus X1 | X1 is **CLOSED — DON'T-SIZE**; none of these lines was opened on a fired card trigger | `PROME/STATUS.md` § Restrictions |

These lines were placed by Will's hand; the defaults bind TERRY's cards, not his orders. The point of the comparison is that **nothing caps the cluster**: every card limit is per card, and ten lines on one falsifier behave as one position (same finding as the 9/11 shared-falsifier grouping, `archive/STATUS_ARCHIVE_2026-09-14b.md`).

## 3. What it takes to pay (MODEL: expiry intrinsic, every name falls the same %)
| Uniform fall by each line's expiry | Intrinsic | Versus basis |
|---|---:|---:|
| 5% | $233 | −$4,414 |
| 10% | $2,790 | −$1,857 |
| **11.76%** | $4,647 | **breakeven** |
| 15% | $8,275 | +$3,628 |
| 20% | $16,222 | +$11,575 |

Simplifications: equal % fall for KRE, OZK, ZION and WAL (single names move more than the ETF); no time value, so before expiry the marks sit above intrinsic. Script and output: `cluster.py`, `cluster_output.txt`.

**Base rate for the breakeven move** (`base_rate_output.txt`; KRE closes 2006-07-03 → 2026-10-23, 5,110 bars, overlapping windows): a close **≥ 11.76% lower 19 sessions later** (≈ the November expiries) **4.9%** of the time, **39 sessions later** (≈ December) **9.0%**; any close that low within 39 sessions **19.1%**. Since 2024 the same close-at-horizon rate is **2.2% / 2.8%**. The 2006+ figure includes 2008–09 and March 2023; the post-2024 figure has no crisis in it. Both are base rates, not a forecast.

## 4. One driver, two paths, both weak on the evidence
**⚠️ Direction check first.** REGINALD's 57-session fit (8/4 → 10/22, `AGENTS/REGINALD/reports/2026-10-23_boot/REPORT.md` §4, committed `8bcdaa8e5`; `TRADE.md` §4): KRE moves about **−0.72% per +10 bp on the 10-year** (correlation −0.36, **R² 0.13**) and **+0.02% per +10 bp of HY spread** (correlation +0.07). So the puts gain on a **RISING** 10-year; **a FALLING 10-year is the falsifier** (rate relief lifts KRE). The spawn brief's phrase "keys on a falling 10-year" is read here as "its falsifier is a falling 10-year"; if a different meaning was intended, this section needs the correction.

| Path | What the evidence says | What it would take to pay the cluster |
|---|---|---|
| **Rates** (rising 10-year) | the only channel with a measurable fit, and the fit explains 13% of KRE's daily variance; outside the last 4 weeks the slope is −0.4% to −1.3% per +10 bp by window, weak (REGINALD answer, consumed 10/23) | the 11.76% breakeven ≈ **+160 bp** on the 10-year on this fit, in 4–8 weeks. Not a plausible rate path; at most the rate channel shades the marks. **The cluster pays only on something the fit does not contain.** |
| **Credit** (REG-T-04: HY > 350 bp ×3 published closes; 340 at 10/22; earliest fire the 10/27 close, published ~10/28) | REGINALD reads **BANK-ABSENT** (~0.7 confidence): HY widened 266 → 340 bp (9/21 → 10/22) while KRE rose 0.6%; on 10/22, the widest HY day of the month, KRE rose 2.53% | a REG-T-04 fire is information for the HYG card (WQ-513 A), **not demonstrated** information for bank puts. It pays this cluster only if credit stress reaches bank funding or deposits, a channel no desk has measured opening |

**Net:** both named paths are weak on the 57-session sample. The cluster is a bet on a **regime break** (a 2023-class funding or deposit event) inside 4–8 weeks. That is a legitimate tail bet, and it should be read as one: the base rate above, not the two channels, is the honest prior.

## 5. The named falsifiers and what each does to the cluster
From REGINALD `TRADE.md` §4 (refuters for any bank put) plus the rate falsifier:

| Falsifier | Reading now | Effect on the cluster |
|---|---|---|
| **10-year falls** | ^TNX 4.96 [10/22 vendor close] | −25 bp ⇒ KRE ≈ +1.8% on the fit (to ≈ $73.76); the Nov-27 70P goes from 3.4% to 5.1% out of the money. Marks fall; the November lines need a bigger move in fewer days. FOMC 10/28 is the dated event |
| **KRE reclaims $72.74** (the 9/16 gap-down close) | **$72.46 [10/23 close], 0.4% below** | the closest refuter to firing: one +0.4% day. A close above it says the gap is repaired; the strikes move further out of the money |
| HY back < 280 bp / B-tier OAS < 300 | HY 340 [10/22] | kills the credit path outright (and with it the REG-T-04 route to bank stress) |
| REG-T-04 exit, HY ≤ 330 ×5 | 340 [10/22], 10 bp above | the credit gate stands down before it fires |
| Clean Q3 print cluster | not clean: problem loans up at 7 of 10 names read, coverage down at 6 of 8 (REGINALD `STATUS.md` 10/23) | **not fired**; this one currently supports the thesis |
| H.8 non-bank lending re-accelerates with small-bank deposits stable | not read this session | removes the funding channel the tail bet needs |

A falsifier firing changes what the cluster is worth and what it is betting on; **what to do with any line is Will's decision**, and this view carries no management instruction.

## 6. Overlap with the rest of the book
The QQQ Nasdaq-downside bet (basis $2,255.69, `IDEA-QQQ-PUTWALL-OCT22` + Oct-26 710P/705P) is a separate driver. The 10/23 KRE/QQQ study found the book pays only on a JOINT fall (to 11/13: flat −$1,693, both rally −$3,032, MODEL; 0 of 13 joint ≥ 5% falls in 40 sessions, 2006+), `research/2026-10-23_KRE-QQQ-report/FINDINGS_2026-10-23_pm.md`. **GLD is not a hedge for this cluster** (MIDAS WQ-451: GLD rose on 2 of 12 equity-stress days in the last 120 sessions); see `setups/GLD-SHARES_management-rails_2026-10-24.md`.

## 7. What could not be verified
Option marks after 10/22 and all bid/ask/OI (weekend) · 10/23 account total · whether any regional line changed after the 10/23 activity capture · Robinhood WAL 70P ×1 · H.8 reading · HY OAS for 10/23 (not published at read). Every option figure: **refresh Monday before any use.**

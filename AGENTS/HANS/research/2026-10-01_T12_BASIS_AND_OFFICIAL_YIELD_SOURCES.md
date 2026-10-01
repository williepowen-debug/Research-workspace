# HANS — T-12 (EUR/USD basis) source test · official FR/IT 10Y sources · 10/02 periphery pre-registration

**Written:** 2026-10-01 12:55 ET (16:55Z) · PROME re-ping touch 2 (Will 12:49 ET, *"go for the six"*). **Pre-registration in §3 is timestamped BEFORE the 10/02 close; this file's commit is its receipt.**
**Split with LIQUID (proposed 10/01 12:3x, by SendMessage):** HANS owns the T-12 row and the EUROPEAN-side pulls. LIQUID owns the US side (the Fed central-bank swap line draw by the ECB, SOFR/IORB). Each cites the other and neither re-pulls. *(No reply from LIQUID by 12:55 ET. The split stands as PROPOSED.)*

## 1. EUR/USD basis / dollar-funding: what is reachable today (each pull named)

| # | Source | Endpoint | Result 10/01 | Lag | Use |
|---|---|---|---|---|---|
| A | **ECB USD 7-day operations, per tender** | `ecb.europa.eu/mopo/implement/omo/html/<ref>.en.html` (keyless HTML) | ✅ **Allotted, bid amount, NUMBER OF BIDDERS, fixed rate, spot.** Latest `20260087`: tendered 9/30, settled 10/01, **$207mn, 3 bidders, 4.13%** | Same day (tender ~10:55 CET Wed) | **LIVE leg** |
| A′ | ECB full operations history | `omo/html/tops.zip` → `tops.csv` (5,280 rows) | ✅ columns `t_alloted_amount` · `t_number_of_bidders` · settlement date. **USD rows only from 2022-11-10 (220 ops)**, so March 2020 is NOT in it | — | Calibration |
| A″ | ECB Data Portal `OMO` | `data-api.ecb.europa.eu/service/data/OMO/B.U2.T.OT.USD_7_D.O..USD` | ✅ outstanding amounts only (USD mn). **No bidder count in the portal** | D+1 | Cross-check |
| B | **ECB Data Portal `EMMS` FX-swap segment** | `EMMS/B.U2._X._Z.S122.S1ZV._Z.F._X.SFXT._X.{FA,FC,FE}._Z._Z.EUR.USD._Z._Z._Z` + `SFXO._X.KO` | ✅ **Exactly the right quantity:** *"Spread between the EUR/USD FX swaps implied rate and the SOFR OIS rate"* (1W/1M/3M/overnight, transaction-based). 🔴 **Last observation 2025-12-31.** Last values: 3M **1.357**, 1M **3.192** (units not stated in the metadata, presumably bp) | **~9 months** | **Calibration only, never an alarm** |
| C | ECB `CISS` daily | `CISS/D.U2.Z0Z.4F.EC.SS_FXN.CON` (FX-market contribution to CISS) | ✅ 0.007 [9/30]. The overall CISS is 0.013 [9/30], falling | D+1 | Context. It is FX *volatility*, not basis |
| D | ECB `FM` | `FM` series keys | ❌ only USD 3M (monthly) and policy rates. **No basis and no forwards** | — | — |
| E | Vendor CIP (spot + 3M forward points + €STR/SOFR OIS) | — | ⛔ **not tested**: no forward-points source is wired on this desk. It would be a VENDOR derivation | — | Possible later leg |

**What the live leg says now (A, last 12 ops, 7/16→10/01):** **$72–378mn per week, 2–5 bidders**, at the fixed penalty rate (OIS+25, 3.88–4.15%). Across all 220 reachable USD ops (2022-11-10→2026-10-01) the maximum is **$1,357mn (2023-12-21, year-end)** and the most bidders is **6**. **⇒ No euro-area bank is paying up for dollars at the ECB backstop.** ⚠️ **Calibration is weak:** in March 2023 (SVB/Credit Suisse) allotments never exceeded **$484mn / 5 bidders**. The tell then was a **REGIME change: the ECB moved to DAILY 7-day operations: settlements every business day from 2023-03-21** (visible in A′ as 0–5-bidder daily rows), not size. March 2020 (the one true dollar squeeze) is **outside the reachable history.**

### Proposed T-12 replacement (PROPOSAL ONLY. No registration without Will's word)
- **Leg A (live, weekly, official):** ECB USD operations. **WATCH:** any single op **allotment > $1.5bn** (above the post-2022 maximum, $1.357bn at a year-end) **or bidders ≥ 8** (above the max of 6). **ORANGE:** the ECB **switches to daily operations or adds a longer USD tenor** (the 2023 tell, a published policy event), or allotment > $10bn. **No RED until March-2020 data is obtained.**
- **Leg B (lagged, official):** EMMS FX-swap implied − SOFR OIS. **Calibration only, never graded.** It is how a future vendor basis leg would be checked.
- **Leg C (LIQUID's):** the Fed swap-line draw by the ECB, the same event from the US end. HANS cites it and does not pull it.
- **Acceptance conditions, written first (WQ-229):** (1) a pull returns allotment, bidders and the date for a tender whose page says **USD**, and it **fails closed**: a missing page or a header without USD reads BLIND, never "0 bidders". (2) An op older than 9 days reads STALE. (3) Replayed over A′, the WATCH fires on **zero** of 220 ops. ✅ **Checked 10/01: zero fires, year-ends included.** The ORANGE regime test fires on the **2023-03-21** daily switch. ⚠️ **Zero fires also means the WATCH is UNVALIDATED against a real squeeze**: it is shown quiet, never shown to fire. March 2020 data is needed before it is trusted. (4) Leg B is never graded. (5) Neighbours: ordinary (weekly op), overlap (a daily and a weekly op on the same date), wrong owner (a Fed-side number entering HANS's row, which is refused), missing (no op that week = holiday, not zero), concurrent (two tenders in one day both counted).
- **What it does NOT measure:** the market basis itself (no live source), and non-bank or non-euro-area dollar demand. **A clean Leg A is "the backstop is unused", not "the basis is calm".**

## 2. Official FR / IT 10-year yields: reachability and lag

| Source | Test | Result | Lag | Verdict for tomorrow |
|---|---|---|---|---|
| **ECB YC** (daily) | `YC/B.U2.EUR.4F.G_N_A…SR_10Y` | ✅ euro-area **AAA** and **all-issuers** curves only, **no per-country curve** | D+1 (~noon CET) | **Bund-leg referee** (AAA ≈ Bund) |
| **Bundesbank** (daily) | `BBSIS…R10XX` | ✅ German 10Y Svensson. Already carries 10/01 | same day; **fixing time unverified** | Second Bund referee |
| ECB `IRS` (monthly) | `IRS/M.{FR,IT}.L.L40…` | ✅ Aug-2026: FR 4.000, IT 3.986 | ~1 month | Too slow |
| Eurostat `irt_lt_mcby_m` (monthly) | API | ✅ (updated 2026-09-11); the daily variant `irt_lt_mcby_d` returns **404 "not available for dissemination"** | ~1 month | Too slow |
| **Banque de France webstat** | catalog API | ⚠️ catalog reachable; dataset **`fm-d-fr-eur-fr2-bb-frmoytec10-hsta`** (TEC 10, daily) **exists but serves 0 records** (records + CSV export empty; metadata modified 2026-06-25) | — | **UNREACHABLE for data** |
| **AFT** (aft.gouv.fr) | TEC10 page | ❌ **HTTP 403, Cloudflare challenge** (same as 9/25) | — | UNREACHABLE |
| **Banca d'Italia** infostat | `infostat.bancaditalia.it/inquiry/` | ⚠️ 200 but a JavaScript UI. No data endpoint found in this pass | — | NOT REACHED |
| **MEF (Italian Treasury) auction results** | `dt.mef.gov.it/…/risultati_aste_btp_10_anni/` → PDF | ✅ **10Y BTP auction 9/29: gross yield 4.58%, bid-to-cover 1.56, €3,000mn allotted** (IT0005729931, 4.00% Oct-2036) | per auction (monthly) | Official level check, not daily |
| **ECB `CISS` SovCISS** (daily, per country) | `CISS/D.{FR,IT,DE,ES}.Z0Z.4F.EC.SOV_CIN.IDX` | ✅ **official daily sovereign-stress index.** 9/30: **FR 0.260 (86th pct since 2010, 94th over 5y) · IT 0.132 (53rd / 78th) · ES 0.036 · DE 0.018** | D+1 | **Official periphery referee** (an index, not a yield) |

**⇒ No official DAILY French or Italian 10Y yield is reachable.** Tomorrow's T-10 re-grade still rests on a vendor spread, but **each leg now has an official referee:** the vendor's Bund leg is checked against ECB AAA (D+1) and the Bundesbank. The French and Italian direction is checked against SovCISS (D+1).
**Re-grade rule for 10/02 (desk practice, within T-10's existing letter, not a new threshold):** grade the spread on the single vendor screen (i-i / TE / CNBC) **whose Bund leg is within 5bp of the ECB AAA 10Y for the same date.** If none qualifies, report the level as a RANGE across screens. **The state stands only if every screen sits on the same side of 100bp / 4.50.**

## 3. PRE-REGISTRATION: what a same-direction 10/02 close would and would not mean (written 2026-10-01 12:55 ET, before the print)

**"Same direction"** = the 10/02 close repeats 10/01: OAT–Bund **and** BTP–Bund each wider by **≥5bp**, **and** the Bund yield **lower by ≥3bp**. These are same-vendor day changes, with the vendor chosen by the §2 Bund-referee rule.

| Outcome on 10/02 | It WOULD mean, on my letters | Official confirmation (read 10/05, D+1) |
|---|---|---|
| **(a) Same direction** | Day 2 of **broad periphery stress with a flight-to-quality bid**. T-10 stays MET (level updated). The 10/01 read (KB-HANS-106) is confirmed as a pattern, not a one-day print | SovCISS IT **and** FR up on 10/01 and 10/02 |
| (b) OAT wider, BTP flat or tighter (<2bp) | **France-specific re-asserts** (budget). Italy's 10/01 was sympathy | SovCISS FR up, IT flat |
| (c) Spreads wider with the Bund **higher** | **Common-mode fiscal/duration sell-off** (the 9/24 shape), not flight to quality | SovCISS DE up with FR/IT |
| (d) Spreads tighter by ≥5bp | 10/01 was a one-day spike. T-10 stays MET (exit needs <90 AND <4.40 for 5 sessions) | SovCISS FR/IT down |

**What a same-direction close would NOT mean, stated before the print:**
1. **Not a T-09 fire or near-fire.** Italy needs >200bp AND >5.50, about 80bp away on both legs. Two days of +16bp do not close that.
2. **Not a change of T-10's state.** MET is binary; only the level moves. **Not an exit**, by construction.
3. **Not dollar-funding stress.** Sovereign spreads are not the basis. That needs §1 Leg A (the 10/07 ECB USD op: allotment > $1.5bn, bidders ≥ 8, or a move to daily ops) or LIQUID's Fed-side draw. **The 10/08 settlement is the first reading after this episode.**
4. **Not a cause.** The budget link stays HEADLINE-ONLY.
5. **Not a reason to re-mark HNS-08** (Bund does not close ≥4.00 by 12/31). A flight-to-quality bid moves the Bund *away* from 4.00, which is the anti-chase clause: one or two days is not a trigger.
6. **Not a regime.** Two days is two days. My letters carry sustain 1 for T-09 and T-10. Nothing here builds a "trend" claim.

## ADDENDUM 2026-10-01 13:1x ET: ownership ruled, letter reconciled (supersedes §1's "Proposed T-12 replacement")
- **PROME ruled:** LIQUID OWNS the dollar swap-line USAGE instrument (`AGENTS/LIQUID/scripts/usd_swapline.py`: NY Fed per-op API 2014→ plus FRED SWPT). It caught 2020-03 ($75.8B ECB) and 2022-10 ($11.1B SNB) and MISSED 2023-03 (max $0.48B). HANS CITES those amounts and keeps two legs of its own: **bidders ≥8** per ECB USD tender, and **ORANGE = a European CB moves to daily USD ops or adds a longer tenor** (the only leg that caught 2023-03).
- **My ">$1.5bn" amount line is WITHDRAWN** in favour of LIQUID's ≥$1.0B WATCH / ≥$5.0B ALERT.
- **Base rate cross-checked from my side:** the only ECB USD ops ≥$1bn since 2022-11 are 20230175 ($1,357mn, 14d) and 20240119 ($1,119.7mn, 21d). Both are year-end turn ops (≤21d spanning a quarter-end), so they are correctly excluded.
- **Amendment sent (c):** the same two ops would trip a literal "adds a longer tenor". Proposed wording: longer tenor = ≥28 days, or a non-7-day tenor NOT spanning a quarter-end. LIQUID sends PROME the one text, marked "HANS AGREE with amendment (c)". **Nothing is registered until Will rules.**

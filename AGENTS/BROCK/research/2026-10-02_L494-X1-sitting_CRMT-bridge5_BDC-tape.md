# 2026-10-02 — L479 CRMT grade · 10/1 BDC tape read · L494 X1 wrapper-half re-adjudication SITTING · L182 W1 state

**Written:** 2026-10-02 Fri from 08:34 ET by BROCK (Tier-1 due-row wake, WQ-184, spawned by PROME `prome-70`). $0. No trade view. Position facts are Will's (APO Dec-18-2026 $95P, Will-ruled HOLD 8/13).

---

## A. L479 — CRMT fourth-bridge STD (10/1): GRADED AT PRIMARY — A FIFTH BRIDGE

**Source:** full submissions feed `https://data.sec.gov/submissions/CIK0000799850.json`, pulled 2026-10-02 08:30 ET; filing index + document text read.

| Field | Value |
|---|---|
| Filing | **8-K 0001171843-26-006326**, Items 1.01 + 8.01, document `f8k_093026.htm` |
| Accepted | **2026-10-01 08:30:14 ET** (EDGAR index page, ET) — before the 10/1 open |
| Date of report | **2026-09-30** |
| Operative text | *"On September 30, 2026, the Agent and Lenders agreed to further extend the Scheduled Termination Date and the temporary relief with respect to the minimum liquidity thresholds and minimum Collateral Coverage Ratio through **October 8, 2026**"* |
| Item 8.01 | unchanged language: *"significant progress towards a transaction … discussions remain active with third-parties, the Agent, and the Lenders"*; events of default *"experienced, or anticipates experiencing"* |
| Other filings since 9/25 | four Form 4s 9/25 (e.g., CEO Campbell 130,293 sh, CFO Persichetti 10,329 sh — code **A**, price $0, transaction date 9/23 = annual-meeting equity grants, not open-market) — nothing else |

**Ladder (STD):** 9/7 → 9/11 → 9/18 → 9/24 → 10/1 → **10/8** (+4/+7/+6/+7/**+7**d). **Decision lead time** (agreement date vs expiring STD): 3d → 1d → 0d → 0d → **1d**. **Disclosure latency** (agreement → acceptance): bridges 1–4 0d; bridge 5 **+1d** (agreed 9/30, filed 10/1 08:30 ET). n=5 is not a policy.

**Reading:** bilateral weekly rollover of the same Silver Point facility for the fifth time. Same "significant progress" sentence for the second consecutive 8-K — the language has not advanced. No permanent waiver, no transaction agreement, no acceleration. Path (a) new permitted warehouse / (b) refinancing: NOT satisfied (no such text).

**L480 (Item 1.01 backstop #2, 10/7):** the agreement this backstop was built to catch (a bridge dated ≤10/1) **has already reached Form 8-K** (dated 9/30, filed 10/1). The row stays PENDING only for any OTHER agreement dated ≤10/1 (e.g., a transaction agreement) — silence through 10/7 still grades nothing. **Successor dates needed:** STD **Thu 10/8**; Item 1.01 backstop for an agreement dated ≤10/8 = **Thu 10/15** (business days Fri 10/9 · Tue 10/13 · Wed 10/14 · Thu 10/15 — Mon 10/12 Columbus Day treated as an EDGAR non-business day: INFERRED from the federal-holiday calendar, not checked against an SEC notice).

⚠️ **Instrument note (VERIFIED at artifact, 2026-10-02):** the submissions JSON's `acceptanceDateTime` for this filing reads `2026-10-01T16:30:14.000Z` while the EDGAR index page reads `Accepted 2026-10-01 08:30:14` (ET); the prior bridges now read `…T00:05:15Z` / `…T00:05:18Z` against index `16:05:15` / `16:05:18` ET. **The JSON field currently sits +8h from ET, i.e. +4h from true UTC** — on 9/25 I recorded the same 9/24 filing as `20:05:15Z`. ⇒ the JSON clock is not a stable instrument; **grade acceptance times from the index page.** (Same class as `[[finding_negative_reachability_is_a_claim_about_your_request]]` — the feed changed under the same URL.)

**Tape:** CRMT **$0.98** (−3.92%) [10/1 close, `fetch.py` 10/2 08:3x ET] — the 10/1 tape already knew about bridge 5 (pre-open filing). Was $1.10 [9/25 live], $1.36 [9/24c].

---

## B-pre. 10/1 BDC complex read (asked by PROME)

**Source:** `FORGE/tools/market-data/fetch.py price` (10/1 closes, pulled 10/2 08:30 ET) + yfinance dividends/total return (pulled 08:31 ET).

| Name | 10/1 close | 10/1 Δ (price) |
|---|---:|---:|
| **BIZD** | **$12.46** | **−3.34%** |
| ARCC | $19.16 | +0.31% |
| FSK | $11.11 | +1.09% |
| OBDC | $10.44 | −0.48% |
| BXSL | $23.92 | −0.25% |
| MAIN · HTGC · OCSL · CSWC · TSLX | — | +1.11 · +0.77 · +0.76 · +0.73 · +0.39% |
| OTF · PSEC | — | −0.61 · −1.44% |
| **APO** | **$114.34** | **−1.48%** |
| OWL | $8.95 | −1.54% |
| ARES · BX · KKR | $116.57 · $112.24 · $91.24 | +0.34 · +0.13 · −0.07% |

**1. BIZD's −3.3% is its ex-distribution date, not a selloff.** BIZD went ex **$0.437** on 2026-10-01 (yfinance dividends). $12.89 [9/30c] − $0.437 = $12.453; close $12.46 ⇒ **total return ≈ +0.06%**. Its constituents were mostly UP on the day. ⚠️ PROME's prompt figure $12.47 vs `fetch.py` $12.46 — the tool's figure is used.

**2. APO −1.48%** extends a −5.3% run from $120.69 [9/24c] to $114.34 [10/1c]; OWL −1.54% same day while ARES/BX/KKR were flat. **No APO-specific 10/1 catalyst found** (SEARCH-NOT-FOUND: web search 10/2; a secondary piece frames APO's 2026 weakness as private-credit redemption pressure and names Q3 earnings **2026-11-03** [stockanalysis/ad-hoc-news, secondary, undated body]). Over the full HY widening 9/24→9/30 APO fell −3.84% with a beta-adjusted residual of −0.3σ (noise; §B W1 table). **INFERRED:** a manager-beta/rates move (10Y 5.29 [FRED 9/30]), not a new private-credit event.

**3. Letters touched?** **None.** APO $100 (`ALL 🔴` alert) is 12.5% away; the 8/12 $130 reclaim exit already fired and was ruled HOLD 8/13. BIZD's drop is mechanical. The BDC wrapper basket did NOT lead the managers (§B). **APO Dec-18-2026 $95P:** last trade **$1.35 (2026-09-30 14:54 ET)**, OI 266; no bid/ask published pre-open (yfinance 10/2 08:3x) ⇒ no live mark today; the FORGE mirror's mark is its own vintage. Read only — no trade view.

---

## B. L494 — X1 WRAPPER-HALF RE-ADJUDICATION SITTING (BROCK convenes)

**Sitting question (DOCKET L494):** does a THIRD absolute instrument firing (GATE-BRK-R2 (a), North Haven PIF 3rd consecutive sub-100%, 43.8% Q3 prelim) change the 8/28 STRUCTURAL verdict (wrapper half NOT ARMED because a RELATIVE "wrappers lead managers" threshold cannot be graded by an ABSOLUTE card), or only the LEVEL?

**Inputs read before ruling:** LIQUID position (`AGENTS/LIQUID/analysis/2026-09-29_L494-X1-card-owner-position.md`, packet 9/29) · PROME WQ-318 packet (9/28) · GATES L22 · my 9/25 W1 (`research/2026-09-25_HY-280-touch_wrapper-half.md`) · REGINALD re-arm SIG-W-20260927-002 + BOARD full signal · LIQ-07 SIG-W-20261001-005 + BOARD full signal · BOND READ-FIRST (`AGENTS/BOND/analysis/2026-09-28_CCC-refi-wall-2027-28.md`, head + narrowing block).

### B1. New evidence since 9/25 (FRED fredgraph CSV pulled 2026-10-02 08:31 ET; LIQUID owns the series — cited, not scored)

| FRED close | HY | BB | B | CCC | CCC/BB | 10Y |
|---|---:|---:|---:|---:|---:|---:|
| 9/22 | 268 | 156 | 271 | 1,075 | 6.891 | 4.96 |
| 9/24 | 280 | 164 | 286 | 1,112 | 6.780 | 5.18 |
| 9/25 | **293** | 176 | 300 | 1,128 | 6.409 | 5.17 |
| 9/28 | **302** | 183 | 309 | 1,146 | 6.262 | 5.24 |
| 9/29 | **308** | 189 | 316 | 1,157 | 6.122 | 5.26 |
| 9/30 | **312** | 194 | 316 | 1,179 | **6.077** | 5.29 |

- HY: **four consecutive closes strictly >280** (9/25–9/30).
- CCC 1,179 [9/30] = high of FRED's public window (starts 2023-09-30 per LIQUID/WALTER; not an all-time high).
- **CCC/BB compressed again, 6.780 → 6.077**: BB +30bp (+18%) vs CCC +67bp (+6%) since 9/24. The widening is **BB-led** — quality-broad, not tail-led.

**W1-B re-run (yfinance `auto_adjust=True` total return, pulled 10/2 08:32 ET; same baskets and same out-of-sample OLS on HYG+SPY, 250 sessions to 9/16 — the 9/22→9/24 row reproduces my 9/25 figures exactly, which validates the re-run):**

| Window (HY OAS) | HYG | Wrappers (ARCC·FSK·OBDC·BIZD) / resid | Six-BDC card / resid | Managers (APO·ARES) / resid | Test (b) price leg: wrappers fall MORE? |
|---|---:|---:|---:|---:|---|
| 9/22→9/24 (268→280) | −0.99 | −1.75 / +0.47 (+0.3σ) | −1.98 / +0.24 | −3.23 / −0.74 (−0.2σ) | ❌ managers led by 1.5pp |
| **9/24→9/30 (280→312)** | −0.87 | **−0.46 / +1.59 (+0.7σ)** | −0.99 / +1.08 | **−3.56 / −1.20 (−0.3σ)** | ❌ **managers led by 3.1pp — 7th wrong-sign print** |
| 9/22→9/30 (268→312) | −1.86 | −2.21 / +2.02 (+0.7σ) | −2.95 / +1.29 | −6.67 / −1.89 (−0.4σ) | ❌ managers led by 4.5pp |
| 9/30→10/1 (no FRED cell yet) | +0.04 | +0.25 / +0.17 | +0.18 | −0.57 / −0.69 | ❌ |

Per-name 9/24→9/30: ARCC −0.16 · FSK −1.61 · OBDC −0.00 · OTF −1.11 · OCSL −1.49 · MFIC −1.58 · BXSL +0.67 · BIZD −0.08 (total return) · APO −3.84 · ARES −3.28 · OWL −1.73. The Blue Owl sponsor tilt of 9/22–9/24 did **not** persist (OBDC flat).

### B2. RULING

**① The structural verdict is UNCHANGED. A third absolute instrument firing changes the LEVEL, not the STRUCTURE. The X1 wrapper half stays NOT ARMED.** Concur with LIQUID (card owner).

| # | Ground | Evidence |
|---|---|---|
| 1 | Category: R2 (a) is a single-vehicle tender-satisfaction count with no manager leg; LIQ-07 is a spread-breadth test; REGINALD's 18.04-ESC is a CCC/HY level conjunction. **None compares wrappers to managers.** N absolute fires measure the level of PC liquidity stress; they carry zero information on lead/lag. R2's own letter: "evidence FOR RE-ADJUDICATION, not a re-arm" — the re-adjudication is this sitting, and it finds no relative evidence. | GATES L22; registers |
| 2 | **The only relative test that exists has now failed on the WHOLE widening, not just its first leg** — and by more: managers led by 3.1pp on 280→312, 4.5pp on 268→312; wrapper residual POSITIVE (+0.7σ), manager residual negative. | §B1 table |
| 3 | **Test (b)'s second leg also failed harder:** CCC/BB fell 6.780 → 6.077 across the move. BB-led. | FRED 9/24–9/30 |
| 4 | LEVEL is higher, and is recorded as such: R2 (a) fired (gates vector already at the 5 ceiling — no rescore); LIQ-07 fired 9/30 (LIQUID's); 18.04-ESC re-armed 9/24 (REGINALD's); HY 312. | signals above |

**Self-check against the flattering reading** (`[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]`): "NOT ARMED" is the verdict that keeps my own 8/28 ruling intact; the evidence that would embarrass it — wrappers falling more than managers on a widening — was looked for on the largest available window and points the other way at +0.7σ. The verdict does not rest on the weak "wrappers are beta-insensitive" explanation; it rests on (1) category and (2) the measured sign.

**② LIQUID ask 1 — the missing "sustained" count on X1's HY leg.** The sitting **RECOMMENDS** LIQUID's text: *"sustained = 3 consecutive published observations strictly >280.0 bp (FRED BAMLH0A0HYM2 ×100, as first published); a print ≤280.0 resets the count to 0."*
- ⚠️ **Contamination declared:** this is ruled AFTER four qualifying closes are known (293/302/308/312), so any N ≤4 is decided by data already seen. N=3 is adopted because it is the **7/27–7/29 PRACTICE that pre-dates the data**, not for its outcome — and it **changes no state**: X1 is an AND and its wrapper leg fails (①). Under the recommended count the HY leg reads **MET at the 9/29 print (3 of 3), 4 at 9/30**; on the letter as it stands it is "TAGGED, never MET".
- **Authority:** adding a count is adding an OPERATOR to a gate letter. The sitting can recommend; it cannot encode. Encoding is LIQUID's on its card, and whether that needs Will's word is PROME's classification (WQ-348's ask-first list names "a new or changed … operator … on any desk gate"). **No sizing consequence either way.**

**③ LIQUID ask 2 — a NEW relative instrument.** Agreed in principle; **NOT registered by this sitting** (a new instrument goes through PROME). Candidate design, written before any further data, for PROME to register or decline:
> **X1-R (candidate):** over any window in which HY OAS widens ≥25bp from its start close (FRED), compute wrapper-basket (ARCC·FSK·OBDC·BIZD, total return) β-residual MINUS manager-basket (APO·ARES) β-residual, betas from OLS on HYG+SPY over the 250 sessions ending 5 sessions before the window start. **FIRE** = that spread ≤ −1.0σ (σ = the spread's own daily-residual sd × √n) on **two consecutive** qualifying windows, AND CCC/BB higher at window end than start. Universe and n declared here; no tuning to 9/22–9/30.
> **Reading on the only qualifying window to date (9/22→9/30, +44bp):** spread = +2.02 − (−1.89) = **+3.91pp — the wrong sign**; CCC/BB fell. Would not fire.

**④ X1 SIZING GATE: CLOSED / DON'T-SIZE — unchanged, and not the sitting's to change.** A sizing change is Will's (Tier 3). Will's 8/13 stand-down stands.

**⑤ What would re-open the wrapper half (pre-registered, unchanged from LIQUID's (i)/(ii)):** a registered relative instrument fires, or test (a) — manager marks vs wrapper marks at Q3 reporting **~10/28–11/10** — shows wrapper marks falling by more; AND the HY leg sustains under a ruled count.

### B3. REGINALD `VX-REG-18.04-ESC` re-arm (SIG-W-20260927-002) — DISPOSITIONED

- **Received.** The re-arm MET on 9/24 (CCC 1,093/1,112 ≥1,050 AND HY 273/280 ≥272, two closes) and is **encoded on REGINALD's register** (`AGENTS/REGINALD/workbook/VX.tsv` row VX-REG-18.04: "★ RE-ARM `VX-REG-18.04-ESC` MET 2026-09-24"). LIQUID dispositioned its half 9/28.
- **What my rows do with it:** the escalation hands the CCC/HY question back to LIQUID/BROCK. **On my side the tail is NOT leading** — CCC/BB compressed 6.780 → 6.077 since the re-arm; the widening reaches B and BB, which is breadth, not tail transmission. ⇒ **No BROCK score, threshold or letter moves.** X1 stays closed (①/④). Will's 8/13 stand-down is not lifted by it (its own scope line). It is not a BROCK state and I do not encode it.
- **BOND READ-FIRST, the loan half (mine):** BOND's point that the weakest 2028 debt is largely floating-rate loans already paying today's rates (so stress shows now in interest coverage, not at maturity) is the PIK channel's mechanism — consistent with my 🟠(3) PIK vector and its three named understatement mechanisms. **No rescore:** BOND's §4 concentration claim was narrowed by CATO 9/28, and the CCC-only 2027 wall is a GAP.

---

## C. L182 W1 — BROCK leg (price-producing-exit denominator): STATE = NOT RUN, still owed

- **Mine:** yes — FORUM ruling ① leg (c), "enumerate PRICE-PRODUCING exits to give the no-print counter a denominator" (`FORUM/…/01_BROCK_joint-synthesis-DRAFT.md` L131; approved 8/13). My SCRATCH carried it as "RUN NEXT SESSION" since 8/13; it was not run on 8/28, 9/3, 9/12, 9/18, 9/21, 9/25 or 9/26 sessions. **OVERDUE since 9/30.**
- **Not rushed today** (PROME's instruction). Why it matters: the tally is CREED 1 + SHADE (a) functional = 2 of 4 (withdrawal test met on the functional reading) or 1 of 4 strict. **A BROCK FOUND makes ≥2 under either reading; a BROCK NOT-FOUND sends strict-vs-functional to Will.**
- **Expected result PRE-STATED here, before the search, so it cannot be spun after:** I expect **FOUND (functionally)** — BDC 10-Q/10-K schedules of investments and realized-gain/loss notes name exited positions with proceeds vs cost each quarter, which is a public surface of price-producing exits. Whether it is USABLE as the ratio's denominator (it covers BDC exits only, not the whole PC market, and needs quarter-on-quarter name matching) is the open question; a FOUND-but-perimeter-limited result would be reported as such, not as a clean FOUND.
- **Proposed:** run at my next wake as a bounded pass on the six-name set (OCSL·OBDC·OTF·ARCC·FSK·MFIC) Q2 10-Qs; PROME to re-date the L182 BROCK leg.

---

## WQ-318 — NAMED-FACILITY QUESTION (from existing work only; no new pulls)

| # | Lender | Borrower | Facility / size | What changed | Source · date | Fits the ask? |
|---|---|---|---|---|---|---|
| 1 | **Western Alliance Bank** (WAL) | a finance borrower that purchased First Brands receivables (not named in my record) | receivables-financing loan, **$126.4M** remaining balance | **(c) attributable loss:** charged off in full, H1-26; forbearance (Oct-2025) failed; litigating | WAL 10-Q filed 2026-07-31 (KB-BRK-225, A1) | **PARTIAL** — a named bank loss on a trade-finance / NDFI credit; the borrower is not a BDC or PC fund |
| 2 | **Bank OZK** | debt-on-debt book (loans to CRE debt funds); credits named by property, not by fund | book $1.20B (6/25) → **$0.43B** (6/26), −64% | **(c) INFERRED:** H1-26 charge-offs $42.4M ≈ The Jack $27.7M (Q1) + San Carlos $14.8M (Q2); utilization FELL, not rose | OZK 10-Qs / Call Reports, read 9/25 (KB-BRK-299/300) | **PARTIAL, INFERRED** — attribution is a sum match; no filing names the fund borrower |
| 3 | **Citizens (CFG)** | capital-call + secured PC finance, aggregate | $8,756M (+2.1% QoQ) + $4,096M (+3.4%) = $12.85B | (a)-shaped growth, but provision fell, coverage 152% | CFG Q2 8-K/EX-99 via REGINALD 7/25 (KB-BRK-195) | **NO** — aggregate line, no named vehicle |
| — | Silver Point Finance (a private-credit lender, **not a bank**) | America's Car-Mart (an operating company) | Credit & Guaranty Agt 10/30/2025 | (b) five weekly bridges + covenant relief | 8-Ks 6/25–10/1 (KB-BRK-297/309) | **NO** — wrong direction (PC lender → corporate), excluded |

**Named bank facility to a BDC / non-traded PC fund (BCRED · OCIC · North Haven PIF · ADS · OBDC · OTF etc.) with increased utilization, tighter terms or attributable losses: NONE FOUND.**
**Checked:** `workbook/KB.tsv` (facility/revolver/warehouse/subscription-line grep: KB-BRK-028, 046, 195, 205, 225, 262/266/275, 297, 299, 300) · `workbook/PC_REDEMPTION_REGISTER.tsv` · North Haven PIF SC TO-I/A 0001193125-26-395654 (tender terms only) · `research/2026-09-25_HY-280-touch_wrapper-half.md`. ⚠️ **NOT checked:** the BDCs' own 10-Q credit-facility notes (borrowings tables, amendment exhibits) — that is where a named lender + utilization change would appear, and reading them is a new pull, outside WQ-318's "existing work only". **This NONE FOUND is a statement about my record, not about the market** (SEARCH-NOT-FOUND, not VERIFIED).

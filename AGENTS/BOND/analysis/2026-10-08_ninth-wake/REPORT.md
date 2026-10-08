# BOND — October 8 ninth wake: 30Y reopening · F2 buyback · FR2004 9/30 · PMMS · official curve

Written 2026-10-08T16:42:27-04:00 (ET, `date` at write). Authority: WQ-390 (Will APPROVE 08:31 ET; one Opus desk wake on DOCKET L617), spawned by PROME `prome-7c`. $0 capital; no trade proposal, no threshold move, no score change, no new direction. Raw primaries, hashes-by-file and tool transcripts: `raw/` beside this file.

## Decision relevance (the five things)
1. **The 30Y reopening graded CLEAN on every frozen letter.** Indirect 72.32% of competitive accepted vs the frozen pooled I′ bar 63.89% (+8.43pp); the convention band (61.20–63.89) is not in play. Cleared at **5.618%, the highest 30Y auction high yield since 2000-08-10 (5.697%)** in Treasury's own record — expensive, not broken, again.
2. **Convergence-downgrade counter 1 → 2** (indirect ≥ median 66.69, dealer ≤ median 11.34). Three consecutive are required; the next nominal coupon (10/21 20Y-R) could make it 3. No score moves today; composite **17/35 unchanged**.
3. **The FR2004 3–6Y build that MET the WQ-291 kill letter reversed in one week:** $60.079B [9/23, unrevised] → **$52.885B [9/30], −$7.194B**. The letter is a single trade-date window already graded MET on the first-published print (10/1); it is **not re-graded**. The reversal is evidence for rider ① (a net-inventory build is not proof of warehousing) and leaves the operational exit recommendation exactly where Will's 10/14 clock holds it.
4. **The second $6B 20–30Y buyback filled 100% of its cap, all off-the-run** (recent_share 0.00%; 94.70% into ≤2.50% coupons). F2 = OFF-THE-RUN, the fourth OFF of four in-scope ops. Routed to RED.
5. **The long end rallied after the auction:** official 30Y **5.60% (−7bp)**, 10Y 5.22% (−6), 2Y 4.75% (−2) — a bull flattener; 30Y real 3.31% (−5), 6bp under the 3.37% [10/5] 2026 high. PMMS 7.40% (+12bp w/w) sits 218bp over the same-date 10Y, inside the 180–230bp VX-BND-17 band.

## 1 · 30Y reopening `912810UW6` (10/8 13:00 ET) — primary TreasuryDirect `securities/search?cusip=912810UW6`, fetched 16:35:28 ET

**Allotment-share basis (named, per the WQ-162 declaration in `monitors/AUCTION_HEALTH.md`): % of COMPETITIVE ACCEPTED = indirect ÷ (PD + direct + indirect) = $21.9396036B.** That is the basis every frozen bar was computed on. WALTER -036 uses the same basis (72.32 / 20.89 / 6.79). PROME's TreasuryDirect read used **total accepted incl. SOMA add-on and noncompetitive** ($22.5225353B: 70.45 / 20.35 / 6.62) — a different denominator, not a different auction. % of offering ($22B): 72.12 / 20.83 / 6.78. **The verdict is basis-invariant:** on total-accepted the indirect still clears 63.89 by +6.56pp.

| Field / test | Value | Letter (frozen 10/1, 2dp, STRICT) | Verdict |
|---|---:|---|---|
| High yield · BTC | 5.618% · 2.54 (Sept 5.308% · 2.61) | — | — |
| Indirect / direct / dealer | **72.316983 / 20.889366 / 6.793651%** | — | — |
| Pooled I′ | 72.32 | indirect < **63.89** | **NOT MET, +8.426983pp** |
| Reopening-only alternate | 72.32 | < 61.20 | NOT MET, +11.116983pp (conventions agree) |
| OLD conjunctive | 72.32 / 6.79 | indirect < 59.95 AND dealer > 14.74 | neither leg: +12.366983 / −7.946349pp |
| Cover marker | 2.54 | BTC < 2.29 | NOT MET, +0.25 |
| Downgrade test | 72.32 / 6.79 | indirect ≥ median 66.69 AND dealer ≤ median 11.34 | **both pass ⇒ counter 1 → 2** |

`grade_auction.py --cusip 912810UW6` (venv, numpy) reproduces every bar exactly (P15 63.89, alt 61.20, OLD 59.95/14.74, cover 2.29, window 2025-10-09 → 2026-09-10, n=12) and prints CLEAN; no print sat in the ≤0.005pp tie band, so the open tool tie-band defect does not touch this grade. Dealer 6.79% is 3.07× September's 2.21% — descriptive only (dealer take is not a bearish criterion since 8/27; it sits under the trailing median).

**Tail: UNVERIFIED and unscoreable by rule.** WALTER's +0.1bp vs a 5.617% WI is secondary; TreasuryDirect publishes no when-issued yield and auction tails were retired 2026-07-28 — no gate may key on it.

**"Highest since at least 2001" — BOND's own claim, from the dataset:** Treasury Fiscal Data `od/auctions_query`, `security_type=Bond`, nominal 30Y terms (`30-Year*`/`29-Year*`, TIPS excluded), 294 rows 1979-11-01 → 2026-10-08. The last 30Y auction with a high yield ≥ 5.618% was **2000-08-10, `912810FM5` reopening, 5.697%**. Every 30Y auction from 2001-02-08 (5.460%) through 2026-09-10 cleared lower. ⇒ **"highest since August 2000" is established; "since at least 2001" is true.** ⚠️ WALTER -036's "Treasury's dataset lacks 2000 auctions" is contradicted by this pull — the 2000 rows carry `29-Year 9-Month` / `30-Year 3-Month` term strings, so a filter on the literal `30-Year` would miss the August 2000 reopening. Packeted to WALTER. Scope: auction high yield, not secondary-market yield; pre-1998 rows are multiple-price auctions (the field is still the stop).

## 2 · F2 buyback, 20Y–30Y Liquidity Support (13:40–14:00 ET; settles 10/9) — primary Fiscal Data `od/buybacks_operations` + `od/buybacks_security_details`, re-pulled by hand 16:36 ET

| Item | Value |
|---|---:|
| Offered / max / accepted | **$14.886B / $6.000B / $6.000B = 100% of cap** (offer cover vs cap 2.48×) |
| Issues accepted / eligible | 10 / 34 (34 detail rows, 0 null, detail par sums to $6.000B exactly) |
| recent_share (newest quartile by ORIGINAL ISSUE DATE, ≥2024-05-15) | **0.00% ⇒ F2 OFF-THE-RUN** (cut > 50% STRICT) |
| Companions (descriptive, never a verdict) | legacy ≤2.50% coupon 94.70% · top-3 86.25% |
| Largest | 912810SJ8 2.25% 2049-08 $2.623B (43.72%) · 912810SZ2 2.00% 2051-08 $1.851B (30.85%) · 912810SX7 2.375% 2051-05 $0.701B (11.68%) |

Four of four in-scope stepped-up long-end ops are OFF-THE-RUN (9/10 · 9/24 · 10/1 · 10/8). First full fill of a 20–30Y op since the cap rose (9/24: $4.078B, 68%). ⚠️ A full fill is a SIZE fact; it is not evidence that a price cap bound or that yields were targeted. Base rate for the on-the-run cut on the vintage rank stays **1 of 53** long-end LS ops through 9/24 (not re-base-rated today); the tool's packet stub still prints the superseded "0/52" — corrected in the RED packet, tool text not edited this session. **RED-FT-11 suppressor input = these op facts; RED grades its own row.**

## 3 · FR2004 as-of 2026-09-30 (published Thu 10/8; NY Fed `markets.newyorkfed.org/api/pd/get/…`, pulled 16:37 ET)

| Bucket ($B) | 9/16 | 9/23 | **9/30** | Δ w/w |
|---|---:|---:|---:|---:|
| 2–3Y `PDPOSGSC-G2L3` | 29.579 | 25.791 | **22.396** | −3.395 |
| **3–6Y `PDPOSGSC-G3L6`** | 47.986 | **60.079** (unrevised) | **52.885** | **−7.194** |
| 6–7Y `PDPOSGSC-G6L7` | 27.845 | 23.199 | **23.304** | +0.105 |
| Long end (7–11 / 11–21 / >21) | 144.4 | 140.5 | **133.1** (38.6 / 57.0 / 37.5) | −7.5 |

**WQ-291 kill letter:** FR2004 3–6Y, trade-date window PRE < auction ≤ POST, MET iff Δ ≥ +$8.6B — ruled for the 9/23 5Y I′ fire, graded MET 10/1 on the first-published 9/23 cell ($60.079B vs $56.586B, +$3.493B; 9/23 cell still unrevised today). **No new 5Y I′ fire exists** (next 5Y 10/27), so no window is open and nothing is graded. The 10/6 3Y I′ marker has no ruled dealer leg (the letter names a 5Y fire; a 3Y award books mostly in 2–3Y) — not extended. **Funding leg:** the 9/23 funding window stays UNGRADED by ruling; latest shared-date SOFR−IORB = **−2bp [10/7: 3.88 − 3.90]**, context only, LIQUID's interpretation. Read: the 9/23 build unwound within a week while the long end kept falling — the BENIGN-distribution pattern (falling inventory with firm indirect at auction: 10/7 10Y 80.34%, 10/8 30Y 72.32%), not forced de-risking. Dealer-absorption row 3 stays 2.

## 4 · PMMS 7.40% [10/8] (Freddie Mac primary, `PMMS_history.csv` + pmms page, fetched 16:37 ET)
30Y 7.40% (7.28% 10/1; 6.30% a year ago); 15Y 6.73%. **Survey minus same-date Treasury official 10Y 5.22% [10/8] = 218bp**, +14bp w/w, inside the VX-BND-17 180–230bp re-arm band (12bp from the top). `rates_context.py` prints 212bp because it pairs the survey with DGS10 [10/7] 5.28 (FRED T+1) — same direction, different 10Y date; the same-date official cell governs here. Not MBS OAS. VX-BND-17 stays 1; the GSE-execution and Fed-sales legs are unwatched by the tool.

## 5 · VX-BND-19 "disorderly" qualifier (docket row, due 10/8) — NOT defined, candidate prepared
The brief joins PMMS to VX19; they are separate items (PMMS is VX-BND-17's leg; VX-BND-19 is the euro-area rates vector). **No bar is set: no new bar is authorized this wake, and VX-BND-19's red-leg level (Bund 10Y > 3.25) has been met since 9/9, so any qualifier chosen now is chosen knowing the level.** The red leg stays **UNFIREABLE AS WRITTEN**; score held 3. Base rate prepared for the decision (Bundesbank `BBSIS.D.I.ZST.ZI.EUR.S1311.B.A604.R10XX.R.A.A._Z._Z.A`, Svensson-fitted 10.0Y residual maturity, daily 1997-08-07 → 2026-10-08, n=7,405; observation time unverified; a fitted point, not the benchmark Bund):

| 5-session rise (bp) | p90 | p95 | p99 | max |
|---|---:|---:|---:|---:|
| Full 1997→ | 12 | 17 | 28 | 55 |
| Trailing 10y | 12 | 18 | 30 | 53 |
| Trailing 3y | 12 | 15 | 21.4 | 45 |

Latest: 3.57% [10/8], 5-session change **−9bp** (2026 high 3.69% [9/28]; highest level since 2011-04-15 3.62%). **Candidate for a ruling (not adopted): "disorderly" = a 5-session rise > p95 of the full sample (+17bp), STRICT** — would not fire today under any candidate, and last exceeded on 9/29 (+18bp). The other branch is to retire the word and let the 3.25 level stand alone (which fires the red leg at once). Owner decision via PROME; HANS consulted on the series.

## 6 · Official Treasury curves, 10/8 (Treasury `daily-treasury-rates.csv/2026`, fetched 16:38 ET)

| | 2Y | 5Y | 10Y | 20Y | 30Y | 2s10s | 2s30s |
|---|---:|---:|---:|---:|---:|---:|---:|
| Nominal 10/8 | **4.75** | **4.99** | **5.22** | **5.64** | **5.60** | 47bp | 85bp |
| Δ vs 10/7 | −2 | −4 | −6 | −7 | −7 | −4 | −5 |

Real: 5Y 2.62 / 10Y **2.87** / 30Y **3.31** (each −4/−5bp). Same-date nominal − real: 10Y 2.35% (−1bp), 30Y 2.29% (−2bp) ⇒ the rally was mostly real-led. **30Y real 3.31% vs the 3.37% [10/5] window high: 6bp below; 3.37% remains the 2026 high of the official real 30Y series** (2026 scan, n=194 — no claim before 2026). Nominal 30Y 2026 high stays 5.67% [10/7]. Treasury 2026 scan: 30Y ≥ 5.00 on 83/194 dates, current run 67; real 10Y ≥ 2.50 run 21 (WQ-246 sustain MET; NO-ADD). The 30Y closed under the 5.618% stop — the official par cell is a fitted curve, not the reopened bond's own yield.

Credit (FRED ICE, 10/7 latest vintage): HY 309 / CCC 1229 / IG 82 / BBB 102 / BB 189 / B 308bp; CCC−BB 1040bp. HY 41bp below 350; +46 from 263 (credit-equity lead leg unmet). Fed path (CBOT ZQ vendor bars, today's evolving bar 16:41 ET, NOT settlement): Nov 3.925 / Dec 4.065 ⇒ calendar-weighted YE ≈ +24.2bp vs EFFR 3.88 [10/7]; October hold/+25 proxy 18%. ACM 10Y TP 0.9848% [10/7], KW 1.0847% [10/2] — different models and windows.

## 7 · Gilt read-across (WALTER -005/-022/-032/-037; HANS grades T-13/T-06 on its own close source)
UK 30Y touched 6.047% intraday; vendor end-of-day reads (TE 5.9384 / Investing 5.938) sit ~6bp under 6.00, but HANS's own London-close path read ~5.99–6.00 — a too-close-to-call close carried to DOCKET L637. **BOND's leg: the US 30Y reopening cleared the same afternoon with indirect 72.32%, +8.43pp over its bar, and the US long end rallied 7bp** ⇒ no transmission of gilt stress into US long-end auction demand on this print. Cross-section (mixed bases, vendor UK): US 30Y 5.60 [Treasury 10/8] vs UK 30Y ~5.94–6.00 ⇒ US ~34–40bp under; Bund 10Y 3.57 [Bundesbank fitted 10/8] vs US 10Y 5.22 ⇒ 165bp. UK Budget is **28 Oct** (WALTER -005, secondary, gov.uk not opened) — the same day as the October FOMC decision; noted on the 10/28 docket row. JGB levels from -005 superseded by -021 (MOF basis: 30Y record 4.168% [10/6]); BOND carried none.

## 8 · Inbox drain (12 WALTER-lane packets, every one logged in `board_log.tsv`)
-036 integrated (§1–2; "2000 lacks" claim contradicted, packeted) · -030 integrated (credit/PMMS re-pulled at FRED/Freddie; HY near-trigger is LIQUID/RED's) · -013 integrated: **verified at Fiscal Data** — 10/6 2Y–3Y LS nominal: $14.763B offered, $1.327B accepted of a $4.0B max (33% fill), 12/33 issues; accepted/offered 8.99% is the 2nd-lowest of 10 ops in that bucket (min 7.54% 2026-04-23; median 22.5%); offered is the largest of the 10 · -005/-022/-032/-037 read-across (§7) · -021 correction read (no BOND Japan figure) · -011 LOG_ONLY: the 6%-coupon conversion-factor CTD switch is the standard futures mechanic; the "18→23-year duration" figures are a secondary's, unverified, and BOND holds no contract-level data; 30Y par 5.60 is 40bp under 6% · -034 LOG_ONLY (Iran/oil tape; BRENT/FALCON) · -033 receipt command adopted (7 receipts written in the WQ-399 form; charter 7b line updated) · -032 [10/2] closed PARTIAL: an independent dated FedWatch/OIS comparator was never obtained; own vendor strip is the only basis and is not settlement. -019/-020 do not name BOND (BOARD scan) — nothing owed.

## Limits
Independent FedWatch/OIS, true CDX, paid MBS OAS, a failed-deal census, a WI yield and executable broker data remain unavailable. Gilt figures are vendor reads. Bund series is a fitted curve point. No future result graded; no order, fill or position change inferred.

# Where market odds disagree most with the fleet's registered forecasts — 2026-11-18

**Desk:** ORACLE (Claude Code, Opus 5.5, desktop `DESKTOP-BC6EF81`, Kalshi SIGNED lane) · **Written:** Wed 2026-11-18, 10:4x ET (wall clock 10:45 at the packet step) · **Commission:** WQ-704 (Will 2026-11-16 23:20 ET, verbatim "yes"; brief `inbox/processed/2026-11-16_from-PROME_research-commission-WQ-704.md`; wake DOCKET line 1173) · **Cost:** $0 · **Moves:** no score, band, gate, threshold, prediction letter or charter. Fleet probabilities are quoted as each desk registered them, never adjusted here.

**Market read used throughout:** ORACLE pull 2026-11-18T15:33Z (10:33 ET; a later same-date pull, so CONTEXT beside the routine's 15:15Z gate read), plus Gamma and CLOB reads 15:35–15:45Z. "PM" = Polymarket. Depth: PM liquidity (liq) and volume (vol); Kalshi open interest (OI). ⚠️ = thin book (<$5K liquidity), never marked on one print.

---

## The answer first

1. **The two largest disagreements are the same shape: a December central-bank hike that a desk registered at 70% on 11/06 and the market now prices near-certain.** The ECB raising its deposit rate on 12/17 (HANS, HNS-13, 70%) is priced at **98.4** on Polymarket, a gap of **28 points**. The Fed raising its target range on 12/9 (HENRY, HEN-63, 0.70) is priced at **97** on Kalshi under the identical letter, **97.6** on Polymarket, and fed funds futures imply **+26.8bp**, a gap of **27 points**.
2. **Most of each gap is new information since registration, not a disagreement at registration.** On 11/06 the markets stood at 82 (ECB) and 78 (Fed): the desks had shaded 8 to 12 points under the market on purpose. The other 16 to 19 points arrived later, mostly in one day each (the Fed on 11/10, the day October CPI printed; the ECB between 11/10 and 11/11, when Lane's backing for December was reported). Neither desk has re-marked. **My read: on today's information the fleet side is the stale side in both cases**, not the market.
3. **Third, France (HANS, HNS-14, 30%) sits 20 points over a related market (9.5), but the two are not the same event and I cannot tell which side is wrong.** The decider is a fact nobody has verified: whether S&P has a France review dated before 11/30.
4. **A resolution-timing problem, not a disagreement:** AEOLUS's El Niño call (AEO-17, 40%) needs the October-to-December RONI value by 12/20, but on CPC's cadence that value most likely first prints in early January 2027. If so, the row closes NO-VERDICT by its own clause (INFERRED; AEOLUS to check).
5. **Coverage is the bigger finding.** Of **129 open fleet predictions** in 21 desk ledgers, only **10** have a priced market I could read. The deepest markets ORACLE tracks (Iran invasion, $80.5M traded; Hormuz traffic, $18.0M) have **no registered fleet forecast at all**; the fleet's registered calls sit mostly where no market exists (company filings, data prints, bank roll-forwards).

**Investment implication: none** (section 6). The big gaps are cases where the fleet's number is out of date, not where the market is wrong.

---

## 1. Method and universe

| Step | What I did | Source, time |
|---|---|---|
| Fleet universe | Every `AGENTS/*/workbook/PREDICTIONS.tsv`, rows whose Status is OPEN, ACTIVE, PENDING, LIVE, WATCH or blank: **129 rows, 21 desks** (AEOLUS 12, BROCK 13, CORAL 3, CREED 3, CRUISE 3, CYPHER 8, FERT 5, FLG 1, HANS 8, HENRY 2, LABOR 8, LIQUID 5, MIDAS 9, OZK 6, RED 6, REGINALD 10, VIOLET 2, VULCAN 5, WAL 5, WATT 7, ZHAO 8). NEXUS's `PREDICTIONS_MONITOR.md` read too (PRED-41, PRED-45: no market). | ledgers as of the working tree, read 2026-11-18 10:4x ET |
| Market search | Polymarket `search` on 13 themes; Kalshi `search` on 7 (⚠️ every Kalshi search hit its 70-page cap, so a zero there is NOT a verified absence) plus Kalshi series lists for Economics and Financials | 15:35–15:45Z |
| Match test | Same threshold, same resolution source, same date. Graded SAME / PARTIAL (overlapping but different events) / SUPERSET (market event contains the fleet event) / DERIVED (no market for the event; implied from related ones) | rule text read at the API for each pair |
| Gap | market minus fleet, points, at today's read; plus the same at the fleet row's registration date where a price history exists (PM CLOB `prices-history`, 6-hour fidelity; ORACLE's own `ODDS_LOG.tsv` / `KALSHI_ODDS_LOG.tsv`) | |

Desks with no prediction ledger (HAWK, FALCON, BRENT, SAM, among others) have probabilities in their STATUS or KB files, but those are not registered forecasts and are out of this universe.

---

## 2. Every pair found, ranked by size of gap

| # | Fleet row (owner) | Registered | Market today | Depth | Match | Gap now | Gap at registration |
|---|---|---|---|---|---|---|---|
| 1 | **HNS-13** (HANS): ECB deposit rate ≥2.75% at the 12/17 decision (now 2.50%, ECB 10/29, per HANS) | **70%**, 11/06 | PM "ECB Interest Rates: December 2026": +25bp **97.15** (bid 96.4 / ask 97.9) + 50bp or more **1.2** ⇒ **98.4**; no change 2.1 | +25 leg liq $9.7K, vol $41.6K; event vol $99.9K. No Kalshi December 2026 ECB event (series KXECB's newest event is September 2025) | **SAME** (PM resolves on the deposit-rate change at the 12/16–17 meeting) | **−28.4** | −12.0 (PM 82.0 at 11/06 18Z) |
| 2 | **HEN-63** (HENRY): FOMC upper bound above 4.00% after the 12/9 statement | **0.70**, 11/06 15:33 ET | Kalshi `KXFED-26DEC-T4.00` "upper bound above 4.00%" **97** (bid 96 / ask 97); PM hold **2.9** ⇒ any hike **97.1** (+25 92.5, +50 or more 5.1); PM "another hike in 2026" 96.9; futures **+26.8bp** | Kalshi OI 182.9K; PM +25 liq $644.3K, vol $9.8M | **SAME** (Kalshi's letter is HENRY's letter) | **−27** | −8 (Kalshi 78, PM 77.5 at 11/06 20:26Z) |
| 3 | **HNS-14** (HANS): S&P cuts France below A+ or moves its outlook to negative, 11/06–11/30 | **30%**, 11/06 | PM "Moody's or S&P downgrades France by November 30" **9.5** (bid 9 / ask 10) | ⚠️ liq $1.2K, vol $8.2K | **PARTIAL**: PM counts a rating cut by Moody's or S&P and excludes an outlook change; HANS counts an S&P cut or outlook change and excludes Moody's | −20.5 raw, not a like-for-like gap | +0.5 (PM 30.5 at 11/06 12Z) |
| 4 | **AEO-17** (AEOLUS): October–December 2026 RONI first print ≥ +2.50 | **40%**, 11/06 | PM "peak RONI for the 2026–27 El Niño" ≥2.5 **56** (bid 55 / ask 57); "strongest on record" (>2.40) **57** | ⚠️ liq $1.35K, vol $74.6K; ⚠️ liq $2.2K, vol $21.1K | **SUPERSET**: PM takes the highest first print of five seasons (ASO through DJF); OND is one of them | −16 raw; consistent, since P(OND ≥2.5) ≤ P(peak ≥2.5) | −31 to −32 (PM 71.0–72.5 at 11/06) |
| 5 | **LAB-12** (LABOR): U-3 ≥5.0% in a Q3–Q4 print | **8%** (re-marked 9/04) | Kalshi Nov U-3 above 4.2% **11**; PM November ladder ≥4.6% bucket **0.6** ⇒ November ≥5.0 under 1 | Kalshi OI 47.1K; PM ≥4.6% leg liq $2.6K ⚠️, event vol $11.8K | **PARTIAL**: November priced, December print (January 2027) unpriced | about −7 on the November leg | n/a |
| 6 | **HEN-61** (HENRY, 0.28, 11/06) and **RED-26** (RED, 33%, 11/05): S&P 500 record close above 7,818.93 by year-end | 28% / 33% | No market for a record close. Kalshi year-end buckets: 7,800–7,999.99 **10**, 8,000–8,199.99 **3**, five higher buckets at the 1¢ floor; PM "SPX hit $8,000 (HIGH) in December" (1-minute high) **10.5** | Kalshi bucket OI 319.0K; PM liq $9.6K, vol $3.6K | **DERIVED**: P(close above 7,800 on 12/31) about 13–18; a level not yet touched is roughly twice as likely to be touched as to be held at the date, less for closes and for a downside-skewed index, ⇒ about **22–30** | HEN-61 about −6 to +2; RED-26 about −11 to −3; inside my derivation error | market fell toward the fleet: PM $8,000 leg 26.0 (11/06 12Z) → 11.5 (11/18 12Z) |
| 7 | **LAB-22** (LABOR): at least one of 8 advance claims prints ≤185,000 | 40%, 11/05; LABOR's own per-print rate 6.2% | Kalshi `KXJOBLESSCLAIMS-26NOV19` (week ending 11/14, prints 11/19): "at least 185,000" **93**, "at least 180,000" **94** ⇒ about 6–7 that this print is under 185,000 | ⚠️ the 185,000 rung OI 4, 9¢ spread; 180,000 rung OI 3.1K | **PARTIAL**: one of eight draws priced | about 0 per draw | n/a |
| 8 | **AEO-01** (AEOLUS, 96%): below-normal season, ACE <110.3 AND ≤7 hurricanes | 96% | PM hurricane count 1–3 **99.2** | event vol $77.9K | PARTIAL: the count leg is priced (agrees); the ACE leg is not | about +3 on the count leg | n/a |
| 9 | **AEO-02** (AEOLUS, 99%): NDJ ONI ≥1.5 | 99% | PM peak-RONI buckets below 2.0 at **0.0** | as row 4 | PARTIAL: different index (RONI vs ONI) and season; same direction | about +1 | n/a |

**Excluded although a market exists:** MIDAS-13 (MIDAS, 0.50, 10/23: GLD issuer close ≥ $378.95 between 10/26 and 11/20). Vendor closes (Yahoo) show GLD **379.53 on 11/09**, above the target, so the row looks met already; MIDAS's letter grades it from the issuer archive on 11/23. There is no open question left for a market to price. GLD 344.01 at 11/18 intraday.

**No reachable market (named, not searched exhaustively):** VIOLET's VIX ≥30 by 11/20 and SKEW <140 (no VIX series in Kalshi's Financials list; Polymarket search empty); every bank, BDC, insurer and company-filing row (BROCK, REGINALD, OZK, WAL, FLG, CREED, CRUISE); credit and funding rows (LIQUID, RED-27, REG-34); CYPHER, FERT, WATT, VULCAN, CORAL; HANS's Bund, OAT–Bund and gas-storage rows; ZHAO's TIC, PMI, HKMA and PBOC rows (ZHA-01, USD/CNY 7.30, has no resolution date, so no match is possible).

---

## 3. The largest three: which side is wrong

### 3.1 ECB, December 17 (HNS-13, 70% vs 98.4): the fleet side is stale

| Date (PM CLOB, 6-hourly) | +25 | 50+ | No change |
|---|---|---|---|
| 11/06 18Z (HNS-13 registered that day) | 81.5 | 0.5 | 16.0 |
| 11/10 12Z | 81.5 | 0.5 | 19.0 |
| 11/11 00Z | 92.0 | 0.9 | 7.5 |
| 11/14 00Z | 95.9 | 0.7 | 4.0 |
| 11/18 15Z | 97.2 | 1.2 | 2.1 |

- **Established:** the market and HNS-13 resolve on the same thing (the deposit rate after the 12/16–17 meeting; HANS's row also counts an inter-meeting hike, which would pay HANS and not PM, a negligible case). HANS sat 12 points under the market at registration on purpose: "Brent fell from 117.64 [10/30] to ~97 and Lagarde said data will tell" (HNS-13 notes).
- **Established:** the 10.5-point step came between 11/10 12Z and 11/11 00Z. HANS's 11/11 note records the reported news: Lane backing a December hike (Trading Economics, secondary) and Nagel calling it "very likely" (11/06). WALTER's card SIG-W-20261116-005 repeats "Nagel hike likely".
- **Inferred:** the reasons HANS gave for sitting under the market came before the Lane and Nagel statements, and HANS's 11/11 note says "No re-mark". So the 70 is a 11/06 view, not a current one.
- **Unknown, and it limits this read:** Polymarket is the only venue (no Kalshi December ECB event); the leg has $9.7K of liquidity and a 1.5¢ spread; I did not read euro short-rate futures or overnight-index swaps, which is where the deep money prices the ECB. What would change it: a soft euro-area November flash inflation print (early December, date not verified) or a walk-back by Lane or Lagarde.

### 3.2 Fed, December 9 (HEN-63, 0.70 vs 97): the fleet side is stale

| Read (ORACLE logs) | Kalshi above 4.00 | PM +25 | PM +50 or more |
|---|---|---|---|
| 11/06 20:26Z (HEN-63 registered 15:33 ET that day) | 78 | 77.5 | — |
| 11/09 15:15Z | 78 | 77.5 | — |
| 11/10 15:15Z (October CPI printed 08:30 ET that day) | **96** | 84.5 | — |
| 11/12 15:15Z | 95 | 90.5 | 6.15 |
| 11/16 15:15Z | 97 | 87.5 | 9.25 |
| 11/18 15:33Z | **97** | **92.5** | **5.05** |

- **December priced path (ORACLE's figure, WQ-671 A), 11/18:** PM hold 2.9 / +25 92.5 / +50 or more 5.1. Kalshi above 4.00 97, above 4.25 5 ⇒ hold 3 / +25 92 / +50 5. Venues about **+25.5bp** expected. Futures: `ZQZ26` 95.93 and `ZQF27` 95.835, EFFR 3.88 (11/17, NY Fed) ⇒ December meeting **+26.8bp**, January average +28.5bp. ⚠️ The futures figures are Yahoo last trades on 11/18, not exchange settlements (CME blocks this box). ⚠️ Futures give an expected size of move, not odds. Unit check: `ZQX26` 96.12 ⇒ November average 3.88 = EFFR.
- **Established:** Kalshi's market is HENRY's letter (upper bound above 4.00%). Three instruments that do not share a crowd (Kalshi, Polymarket, CME futures via Yahoo) agree.
- **Established:** 18 of Kalshi's 19 points (78 → 96) came between the 11/09 and 11/10 reads, the day October CPI printed; Polymarket's +25 leg moved 7 of its 15 points that day and the rest by 11/12. The cause is inferred from timing; I did not read the CPI release.
- **HENRY's three reasons for shading, tested against what has happened since:** (a) "4.5 weeks of CPI, PCE and payrolls": October CPI has printed; November payrolls (12/04) and the PCE release remain; November CPI (12/10) comes after the meeting. (b) "The October precedent (72% for an October hike on 9/24, then a hold)": that miss was five weeks out. Three weeks before the October meeting the market had already moved to the hold (Kalshi `KXFED-26OCT-T4.00` 18 on 10/09, 12 on 10/22; hold delivered 10/28). One case, but at three weeks out the market was on the right side. (c) "My own soft core CPI expectation (HEN-57)": HENRY grades HEN-57; secondary relays put October core at +0.3.
- **My read:** 0.70 understates on today's information; the residual risk of a hold is real but on the order of the 3 the market charges, not 30. **Unknown:** what the Fed says before its blackout; a weak November payrolls print could reopen the gap, and I would see it first in the +25 leg.

### 3.3 France rating (HNS-14, 30% vs 9.5): cannot tell

- **Not the same event.** PM pays on a rating cut by Moody's or S&P; an outlook change alone does not count (rule text). HNS-14 pays on an S&P cut or an S&P outlook change to negative; Moody's does not count. The only shared outcome is an S&P rating cut, which PM caps at about 9.5 (and that 9.5 includes Moody's).
- **The market moved, not HANS:** PM was 30.5 at 11/06 12Z, the same as HANS's 30, then fell to 7.0 by 11/07 00Z and held 6.5–7.0 to 11/16, spiked to 18.0 at 11/17 00Z and has been 9.5 since. ⚠️ $1.2K of liquidity: the 11/06–11/07 fall has held 11 days, so it passes my three-day re-check, but the 11/17 spike does not. **The cause of the 11/06–11/07 fall is not established.**
- **The fact that decides it, unverified by anyone:** whether S&P has a France review dated in the window. HANS's 11/27 date has no 2026 source (HNS-14 notes, 11/11; aft.gouv.fr returned 403). If there is no review, HNS-14 resolves MISS by its own rule and the market's 9.5 is generous. If there is one, HANS's outlook branch (Fitch went negative on 10/30, Moody's is Aa3 negative) carries most of the 30, and no market prices that branch.

---

## 4. A resolution-timing problem in AEO-17 (for AEOLUS)

- **Established:** CPC's `RONI.ascii.txt`, read 2026-11-18 15:4xZ, ends at **ASO 2026 1.97** (AMJ 0.49, MJJ 0.97, JJA 1.36, JAS 1.69). ASO ends on 10/31 and was already in the file when AEO-17 was written on 11/06.
- **Inferred from that cadence (not from a CPC calendar):** each update adds the three-month season that ended the month before. SON (ending 11/30) should first print in early December and **OND (ending 12/31) in early January 2027**. AEO-17 expects the OND row "~12/7" and resolves NO-VERDICT "if no OND 2026 row by 2026-12-20".
- **So the row will most likely close NO-VERDICT.** The PM peak market (row 4) has the right calendar: it waits for DJF. Nothing here re-grades AEOLUS's call; AEOLUS owns the letter and any repair.

---

## 5. What the comparison says about the fleet's registered forecasts

| Finding | Evidence | Status |
|---|---|---|
| Registered probabilities are point-in-time and are not re-marked when deep markets move | HNS-13 "No re-mark" 11/11 while PM went 82 → 92; HEN-63 unchanged while Kalshi went 78 → 96 in one day | established for these two rows |
| At registration, desks shaded deliberately under the market on central-bank calls, by 8 to 12 points | HEN-63 −8, HNS-13 −12, both with stated reasons | established; whether the shading has skill needs more than n=2 |
| Most fleet forecasts sit where no market exists | 10 of 129 open rows paired | established |
| The deepest priced theaters (Iran, Hormuz, oil tail) have no registered fleet forecast | Iran invasion $80.5M vol, Hormuz normal by 12/31 $18.0M vol, WTI $110 November $122.5K vol: none paired | established; whether that matters is PROME's and the owning desks' call |

Nothing here proposes a rule. If PROME wants it, the cheap version is for a desk that registers against a deep market to re-read that market at its own next session; that is a choice for the desks and PROME, not a finding.

---

## 6. Trade-assessment handoff (WQ-696 form, in my own words)

**This evidence supports no investment implication.**

- **Why:** the large gaps are cases where the fleet's number is out of date, not cases where the market looks wrong. Taking the fleet's side (a Fed hold at about 3¢ on Kalshi, an ECB no-change at about 2.1¢ on Polymarket) pays only if a hold is about ten times likelier than priced, and nothing I can read supports that. Taking the market's side earns at most 2 to 3¢ a contract against a tail that is genuine, before fees.
- **Horizon:** to the Fed statement 12/9 and the ECB decision 12/17.
- **What would invalidate this reading:** the venues falling back under about 85 on either meeting (a soft November payrolls print on 12/04, a soft euro-area flash, or Fed or ECB speakers walking back) would reopen a real disagreement, and I would re-run this comparison then.
- **Unknown:** euro short-rate futures and swap pricing for the ECB (not read); whether S&P reviews France before 11/30; the cause of the 11/06–07 fall in the France market.
- **France and El Niño:** both books are thin (⚠️ $1.2K and $1.35K of liquidity) and neither gap is like-for-like. No implication.

Sent to TERRY for the tradeability read the fleet's standing practice asks for (Will 2026-11-10), with the expectation of NO CARD.

---

## 7. Sources

| Item | Source | Read |
|---|---|---|
| Fleet rows | `AGENTS/{HANS,HENRY,AEOLUS,LABOR,RED,MIDAS}/workbook/PREDICTIONS.tsv`; `AGENTS/HANS/STATUS.md` (deposit rate 2.50%) | 2026-11-18 10:4x ET |
| PM and Kalshi prices | `polymarket.py pull --log` and `kalshi.py pull --log` at 15:33Z; Gamma `/markets?slug=` rule text and depth; Kalshi `/markets`, `/events` | 15:33–15:45Z |
| Price histories | PM CLOB `prices-history` (6-hour fidelity, 11/04–11/18); `workbook/ODDS_LOG.tsv`, `workbook/KALSHI_ODDS_LOG.tsv` | 15:40Z |
| Futures, EFFR | Yahoo via yfinance (`ZQZ26.CBT`, `ZQF27.CBT`, `ZQX26.CBT`, last trades 11/18); NY Fed EFFR API (3.88, 11/13–11/17) | 15:4xZ |
| S&P 500, GLD, VIX | Yahoo (`^GSPC` 7,323 intraday 11/18, close 7,340.53 on 11/17; `GLD` 379.53 on 11/09; `^VIX` about 24 intraday) | 15:4xZ |
| RONI | `cpc.ncep.noaa.gov/data/indices/RONI.ascii.txt` | 15:4xZ |
| Context cards | WALTER SIG-W-20261116-005 (Nagel), SIG-W-20261117-022/-028 (Qeshm strike 11/17) | titles read |

KB rows: KB-ORC-140 (December priced path), KB-ORC-141 (this ranking), KB-ORC-142 (Iran pause leg resolution and diplomacy drift).

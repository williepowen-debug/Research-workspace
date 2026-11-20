# NEXUS due-row grades — 2026-11-20 (D:L574, D:L632)

**Grade stamp 2026-11-20T11:43:46-05:00** (from `date`). Wake: PROME prome-77 task letter (11:36:52 ET, laptop), due-row class under PROME C6. Runtime: Claude Code, Opus 5.5 (`claude-opus-5-5`), laptop; session `f99603cd-5ec2-41e2-aa66-84663880556a`. Bounded session: grades, intake, two registrations. No matrix review, no digest readers.

## Summary

| Letter | Due | Result | Consequence |
|---|---|---|---|
| **PRED-45** (arms-length private-credit loan-level transfer ≤ 90.0¢, documented by 11/20) | 11/20 | **❌ MISS** — no court sale order or filed realized-sale disclosure found that documents one | row closes; 35% was the standing number |
| **M-11** (same documents; UP p ≤ 90.0¢ · NO-VERDICT (90, 95] · DOWN none ≤ 95.0¢) | 11/20 | **DOWN, n = 0** (no documented transfer at any price ≤ 95.0¢) | **51 → 47 (−4 pp)**, then the number is **withdrawn, no successor** (M-07 precedent 11/4); 47 historical |
| **M-08b** (UP B ≥ 358 AND CCC ≥ 1,416 on the same 2 cells · DOWN B ≤ 328 AND CCC ≤ 1,296) | cells obs ≤ 11/20 | **⚪ NEITHER** — no single cell met either conjunction | **83 held, EARNED once**; then **withdrawn, no successor** (Disc-J; M-01/M-05 precedent 11/10); 83 historical |

PRED-45 and M-11 read one set of documents: **one observation, two letters** (Disc-F/H). M-08b reads the ICE credit family that L16, M-01 and M-07 also read; it adds no root.

## 1. PRED-45 and M-11 — the document sweep

**Letter (re-registered 10/1, `PREDICTIONS_MONITOR.md`; M-11 `research/2026-10-08_disc-J_letters.md` row M-11):** HIT if a court sale order or a filed realized-sale disclosure documents an arms-length loan-level transfer ≤ 90.0¢ by 11/20; MISS if none. A mark at any level is not a transfer.

**Sweep, 2026-11-20 11:38–11:43 ET:** SEC EDGAR full-text search (efts.sec.gov), 10-Q filings accepted 2026-10-25 to 2026-11-20, then 8-K for two phrases; SEC contact string per WQ-565 A (Will 10/31), `scripts/sec_contact.py`, about 3 requests per second, one process. Phrases: "sold" + "of par" + "realized loss" (69 hits) · "cents on the dollar" (0) · "sold our first lien" (1) · "sale of our first lien" (0) · "sale of our debt investment" (2, both HTGC) · "sold the loan" (2, neither a lender of private credit) · "sold our loan" (0) · "at a price of" + "of par" + "sold" (62) · "sold" + "at a discount to par" (25) · "sold our position" / "sold our debt" / "sold our debt investment" / "sold our second lien" (0) · "realized loss" + "sold the" (71) · "loss on the sale of" + "first lien" (24) · "exited our" + "realized loss" (6) · "sold" + "below par" + "loan" (41) · "discount to par" + "sold" + "realized loss" (13) · 8-K "sold" + "of par" + "loan" + "realized loss" (21, earnings releases and trust exhibits) · 8-K "loan sale" + "of par" (3, agreement exhibits). Hit lists for the later batches: `PRED45_efts_phrases.txt`. Text windows read in full at the filings below.

**Candidates, none qualifying:**

| Candidate | Document | Why it does not count |
|---|---|---|
| HTGC Simon Data debt sale (Q3) | 10-Q 0001280784-26-000054 (10/29) | Sale disclosed; **price, buyer and arms-length status not disclosed**. Bound from aggregates (10/31 RECORD §7): at least about 63¢; can sit either side of 90¢ and of 95¢. BROCK KB388–392: prices not obtained. Not a documented price. |
| Franklin BSP Capital: "In January 2026, we sold our first lien debt position of MGTF Radio Company, LLC", realized loss $33.0M | 10-Q 0001825248-26-000029 (11/12); first disclosed in the Q1 10-Q 0001825248-26-000017 (5/13) | **Two grounds:** the sale is January 2026, before the April original and the 10/1 re-registration (documented since 5/13, so it is not a forward observation); and MGTF Radio sits in FBCC's affiliated/controlled investment table beside MGTF Holdco equity, so arms-length status is not established. Price not computed (not needed). ⚠️ The letter names no window START; see §4. |
| Steele Creek Capital: 164 broadly syndicated loans sold 8/18 by BWIC to over 22 dealers, gross proceeds about $73.0M, net realized loss about $1.7M, "income of approximately $462 thousand above the June 30, 2026 valuation"; 37 more 10/22, proceeds about $13.776M | 10-Q 0001213900-26-119533 (11/13) | Arms-length auction, but **aggregate proceeds only, no loan-level price**; broadly syndicated loans, not private credit; sold above marks in aggregate. **First Brands still held at 9/30** (two tranches, fair value $1K each), so it was not in the auction. |
| GECC Flexsys: $4.1M loss on sale | 10-Q 0001193125-26-443697 (11/2) | "our investment in Flexsys Cayman Holdings, LP": a fund/LP interest, not a loan-level transfer; no price. |
| TCPC to Pantheon, about $523M across 78 companies at 95% of 12/31/2025 gross fair value | 8-K 0001193125-26-336845 (8/6) | A pool priced to fair value, not a loan priced to par (10/31 RECORD §7). |
| ING about $500M sale of 12 data-center loans, bids 11/19 | press via WALTER SIG-W-20261106-004 (BROCK KB-BRK-444) | Bank-held; no filed or court document; no price. |

**Not swept:** court dockets (no court sale order of a private-credit loan is known to the fleet: OTTO's STATUS [committed 11/19] lists asset sales only, Tricolor vehicles and the First Brands McHenry wind-down sale hearing 12/09, no loan transfer); every BDC realized-loss note read line by line (full-text phrase search is the instrument; a sale described in other words could be missed). **Residual window:** filings accepted on 11/20 after 11:43 ET are inside the letter. NEXUS re-runs the same phrase set over 11/20 acceptances at the L554 wake Tue 11/24; a qualifying document would be recorded as a labelled correction to this grade.

**WQ-619 A line (on the MISS):** nothing surprised me in the outcome; what surprised me is how close to blind the instrument is. BDC 10-Qs report realized losses in aggregate and almost never state a loan's sale price, so "none documented" says little about where loans would actually trade. **Change for the next comparable call:** key a transfer-price call on documents that itemize prices (court sale orders, liquidating-fund line-item disclosures, auction results), not on the 10-Q realized-loss notes.

**M-11 Disc-A (mechanism):** the DOWN branch's meaning, "no documented recognition event by 11/20", holds as observed. Whether that reflects marks being accurate or the instrument's blindness cannot be told from these documents ⇒ mechanism **RESOLUTION-UNVERIFIED**. The −4 pp applies as written.

## 2. M-08b — FRED first-published cells

`fetch.py fred <ID> --first-published`, pulled 2026-11-20 11:37:42 ET; raw JSON in this folder; no missing dates (short = False). Anchors (obs 10/23): **B 343 · CCC 1,356 · BB 206** (qualified 10/26). Edges: UP B ≥ 358 AND CCC ≥ 1,416; DOWN B ≤ 328 AND CCC ≤ 1,296; same two consecutive cells.

| Obs | B | CCC | BB | HY | UP cell? | DOWN cell? |
|---|---|---|---|---|---|---|
| 10/26 | 336 | 1,345 | 198 | 330 | no | no |
| 10/27 | 322 | 1,321 | 187 | 318 | no | B yes, CCC no |
| 10/28 | 318 | 1,307 | 184 | 314 | no | B yes, CCC no (11 bp short) |
| 10/29 | 332 | 1,325 | 194 | 326 | no | no |
| 10/30 | 360 | 1,327 | 209 | 344 | B yes, CCC no | no |
| 11/2 | 363 | 1,319 | 206 | 343 | B yes, CCC no | no |
| 11/3 | 362 | 1,316 | 203 | 340 | B yes, CCC no | no |
| 11/4 | 351 | 1,297 | 199 | 332 | no | CCC 1 bp short, B no |
| 11/5 | 367 | 1,320 | 213 | 348 | B yes, CCC no | no |
| 11/6 | 361 | 1,317 | 208 | 342 | B yes, CCC no | no |
| 11/9 | 350 | 1,311 | 200 | 334 | no | no |
| 11/10 | 347 | 1,331 | 193 | 330 | no | no |
| 11/11 | 347 | 1,330 | 193 | 330 | no | no |
| 11/12 | 339 | 1,314 | 183 | 320 | no | no |
| 11/13 | 344 | 1,316 | 186 | 323 | no | no |
| 11/16 | 357 | 1,310 | 196 | 334 | no | no |
| 11/17 | 368 | 1,329 | 204 | 343 | B yes, CCC no | no |
| 11/18 | 373 | 1,353 | 205 | 347 | B yes, CCC no | no |
| 11/19 | 380 | 1,361 | 210 | 352 | B yes, CCC 55 short | no |

**No cell met either conjunction; runs 0 ⇒ ⚪ NEITHER.** CCC max 1,361 [11/19]; CCC min 1,297 [11/4].

**Final despite the unpublished 11/20 cell** (publishes about Mon 11/23): a run needs two consecutive qualifying cells, and 11/19 qualifies on neither branch, so the only pair the 11/20 cell could finish (11/19–11/20) cannot qualify; a lone qualifying 11/20 cell is the letter's n = 1 case, which grades NEITHER. Same reasoning as the 8/28 successor-falsifier FINAL (`PREDICTIONS_COLD.md`).

**Consequence:** the letter's "neither ⇒ hold, EARNED once": M-08 83% held. No second successor exists, and a successor needs new thresholds and Will's word, so under Disc-J the number is **withdrawn now** (judgment, no number; 83 historical), as M-01 and M-05 were on 11/10. No mechanism grade (no fire).

**What the letter could not see (Disc-A, recorded, no regrade):** from the anchor, B +37 bp, CCC +5, BB +4 [10/23 → 11/19]; since 11/12, B +41, BB +27, CCC +47. LIQUID 11/20 (its pull 11:22:56 ET): "the move is now in B and BB, not CCC"; CCC−B 981 at the 57.5th percentile ("the tail did not lead"); B−BB 170, 15-session +36 at the 99.2nd. The conjunction needed CCC +60, so it could not register a B-led widening. A successor keyed on B and BB would, if Will wants one; draft idea only, nothing registered.

## 3. Context on the day (WALTER SIG-W-20261120-001, intraday vendor reads, not closes)

VIX crossing 30 (30.19 at 16:24:04Z, 29.58 at 16:28:34Z; VIXCLS 28.44 [11/19]); S&P 500 7,069.61 (−1.48%), SMH −6.97%, NVDA −6.38%, AMD −10.62%; KOSPI −5.21%; gold Dec −3.76% with the dollar flat; **10-year yield about −9 bp**; KRE +0.23%, HYG −0.10%. No single sourced cause. HY 352 [11/19] is REGINALD's REG-T-04 day 1 of 3 (owner grades). LIQUID 11/20: financing constraint NOT SHOWN; tier rule BROADENS a fourth time. **Disc-D counter-signal:** banks up, cash high-yield ETF nearly flat and a bond bid on a 7% chip fall: today's stress is in equity volatility and AI names, not yet in funding or banks. Effective N unchanged (1 established root plus 2 candidates); no alert; no other row re-marked (bounded pass).

## 4. Letter defect found while grading (BOOT 0b test iv)

PRED-45's re-registered text names a deadline ("by 11/20") and no window START. A transfer before the as-made date (FBCC's January MGTF sale) would read as a HIT under a literal reading. Graded on the forward intent (an observation after registration); MGTF also fails arms-length, so the grade does not turn on it. **Correction for future letters (own rule, no new check):** every transfer- or event-count letter names its start as well as its end.

## 5. New registrations (WQ-596 / D:L930; WQ-715 probability stated)

Both pass BOOT 0b's four tests; five-case counterexamples on the rows in `PREDICTIONS_MONITOR.md`.

| ID | Question graded | Instrument and vintage | Resolves | P | Base rate |
|---|---|---|---|---|---|
| **PRED-51** | Does the November credit widening persist to year end? YES if the HY OAS cell with the latest observation date ≤ 2026-12-31 is ≥ 352 bp | FRED `BAMLH0A0HYM2`, first-published, integer bp | first boot on or after the cell publishes (about Mon 2027-01-04) | **40%** | 2 of 4: episodes of +25 bp in 15 sessions to a six-month high, still at or above that level 29 sessions later, in FRED's ICE window from 2023-11-21 (n too small to lean on) |
| **PRED-52** | Does the tape stress reach labor by year end? YES if any initial-claims first print for a week ending 11/21 through 12/26/2026 is ≥ 240,000 | DOL weekly claims `ICSA`, SA, FIRST PRINT (resolving vintage named; later revisions annotated, never re-graded) | first boot on or after the w/e 12/26 release (about Wed 12/30 or Thu 12/31) | **8%** | 8 of 178 six-week windows starting ≤ 215,000 reached ≥ 240,000 (FRED latest-revised, 1969–2026 excluding 2020–21); November starts 2 of 10. Latest 203,000 [w/e 11/14, latest-revised] |

## 6. FORWARD VIEW — PROJECTION (not evidence; moves no score, band, gate or trade)

**What I expect (2 to 6 weeks):** the tape stays ahead of the substance. Equity volatility and public high-yield middle tiers (B, BB) stay wider than October; funding prints stay calm; labor stays near 200,000 claims; private-credit marks stay untested by priced transactions until the Q4 10-K cycle (February–March 2027). **Why:** one repricing class (AI and chips plus policy) has driven every leg so far; credit follows it by tier, not by default or funding, and no issuer in the AI financing chain has had financing refused. **Meaningful alternative:** a named financing event in the AI chain (a pulled deal, a downgrade, a vehicle forced to sell private loans) turns tape into substance; the first prints would be SOFR99−IORB, a priced private-loan sale, or claims. **Numbers:** PRED-51 40% and PRED-52 8% above, each its own event and horizon. **Unscored (not registered, owner holds the question):** REG-T-04 completing on the 11/20 and 11/23 cells (HY over 350 for three closes): about 55% by my judgment; REGINALD owns that line and its REG-37 row asks a different question (30% by 12/14). **What would change my mind:** a funding print, a financing refusal with a name on it, or a documented private loan sale at a deep discount.

## 7. Intake

WALTER lane 2 cards: SIG-W-20261120-001 (FLASH, VIX over 30) acted: §3 context, HY/B/CCC cells cross-checked against my own pull; SIG-W-20261120-005 (Russian missiles in southeast Poland, Polish government) noted: R9 context, no measured US market transmission; no US break vote. Top-level inbox empty.

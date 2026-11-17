# REGINALD 2026-11-17: Q3 full-universe counts (FFIEC bulk 9/30) and the SEC FHLB-borrower panel re-run

**Written:** 2026-11-17 12:27 ET (from `date`). **Session:** Will direct ("yes go ahead", 12:21 ET), Claude Code, Opus 5.5. Research only: no gate, level, band, score, prediction, card or charter moves. Runs owed items (a) and (e) of the 11/07 plan (CALENDAR archive BLOCK C24; method `reports/2026-11-01_Q3-call-report_VLY-EGBN-HBAN/REPORT.md` §4) and the Q3 SEC-panel re-run owed by `reports/2026-11-16_UFB-and-FHLB-deeper-read.md` §D. Items (d) and (f) were done 11/16 (KB ML-REG-301).

## 1. Data and reproducibility

| Source | Retrieved | Facts |
|---|---|---|
| FFIEC CDR bulk, Call Reports single period, TSV | 12:2x ET 11/17 (page: "Call Updated: 11/14/2026") | 9/30/2026 **posted**: 4,267 filers in POR. 6/30: 4,297. 3/31: 4,336. zip sha256: 9/30 `ffe88345…a3a2`, 6/30 `0a375473…e1ad`, 3/31 `abf5f0c0…0fc`. The 6/30 and 3/31 files are the CURRENT versions (later amendments included), not what was public on 10/13 |
| FDIC BankFind API (`api.fdic.gov/banks/financials`) | 12:21 ET 11/17 | 9/30: **0 rows**; 6/30: 4,313. FFIEC is the route, as DEWEY said 11/11 |
| SEC XBRL frames `us-gaap:AdvancesFromFederalHomeLoanBanks` CY2025Q4I / CY2026Q2I / CY2026Q3I | 12:21 ET 11/17 | 162 / 113 / 107 filers |
| FRED DGS10 / DGS5 | 12:2x ET 11/17 | 10Y 4.30 [3/31], 4.44 [6/30], **5.29 [9/30]**; 5Y 3.92, 4.19, **5.09** |

Script `universe_counts.py` (this folder), output `output.txt`. Values in $ thousands as filed; RCFD where present, else RCON; POR filers only. **Tie-out:** Amerant Bank (RSSD 83638) available-for-sale cost minus fair value, after 21% tax: $26.2M [6/30], $125.3M [9/30], against the holding company's own deck figure of $23.7M and $118.9M (8-K 11/13, acc 0001734342-26-000093). Bank versus holding company and a 21% tax rate explain the gap; the size and the fivefold Q3 jump both reproduce.

## 2. SEC panel, FHLB advances (REG-T-06 breadth measure 2), re-run after the 11/16 10-Q deadline

| Endpoints | Matched | Zero-start | n | **Median** | Up / down / flat | Panel sum | Excluding top three gainers |
|---|---:|---:|---:|---:|---|---|---|
| *H1 control* | 109 | 8 | 101 | 0.0% | 36 / 49 / 16 | $100.1B → $135.5B | +$2.18B across 106 (**reproduces 10/10 and 11/16 exactly**) |
| **YTD 12/31/25 → 9/30/26** | 105 (was 102) | 8 | 97 | **0.0%** (was −0.4%) | 36 / 47 / 14 | $93.4B → $124.4B | −$0.20B across 102 |
| **Q3 6/30 → 9/30/26** | 102 (was 100) | 11 | 91 | **0.0%** (unchanged) | 30 / 35 / 26 | $126.2B → $123.9B | −$6.60B across 99 |

Still absent from the Q3 frame, 11 filers: Raymond James and TFS (September fiscal years), Stifel, Webster, United Community, Consumers, Timberland, Home Federal of Louisiana, First Seacoast, Gouverneur, Monroe Federal. The large ones filed 10-Qs, so their absence is a tagging or frame-selection question, not a missing filing (not chased). **Reading unchanged: borrowing growth is concentrated, not broad; no breadth-supported escalation.** The 11/16 report's −0.4% YTD median is superseded by 0.0% on a three-filer-larger panel; both are "flat".

## 3. (a) The Friedberg "95 of 4,295" test: no candidate measure reproduces it

The claim surfaced 10/13, when 6/30 was the newest universe, so the identification test is on 6/30 (Q1 → Q2 for C). Q3 is shown beside it.

| Measure | 6/30 (the claim's quarter) | 9/30 |
|---|---|---|
| A. Existing unrealized securities loss ≥ 20% of GAAP equity, pretax / after 21% tax | **872 / 622** of 4,296 (20.3% / 14.5%) | 1,405 / 1,113 of 4,263 (33.0% / 26.1%) |
| A on tangible equity (3210 − 2143), pretax / after tax | 912 / 665 **of 4,295** | 1,480 / 1,184 of 4,263 |
| B. Additional loss from a parallel shock alone ≥ 20% of equity (duration PROXY) | not run on 6/30 | +100bp 539 (12.6%) · +200bp 1,518 (35.6%) · +300bp 2,169 (50.9%) |
| C. Actual equity decline ≥ 20% in the quarter | **8** of 4,290 (Q1 → Q2) | **109** of 4,260 (2.56%; Q2 → Q3) |
| D. A (after tax) ≥ 20% of CET1 | not run on 6/30 | 887 of 4,245; **all 887 have opted out of AOCI in capital**, so for them it is not a regulatory capital loss unless sold |

**Verdict: UNIDENTIFIED.** The population matches: 4,295 is exactly the 6/30 count of filers with positive tangible equity. No 6/30 count comes near 95 (A gives 622–912, C gives 8). The closest number anywhere is C on Q3 (109 of 4,260, 2.6% vs the claim's 2.2%), a quarter **after** the claim was made. The primary statement is still SEARCH-NOT-FOUND (11/01 report §4). The claim stays unauthenticated and is not cited.
B uses stated bucket durations (RC-B Memo 2; script `DUR`), not measured ones; hedges are invisible in Call Report securities lines, so A, B and D overstate for hedged banks.

**What the 109 Q3 equity drops are:** for 93 of them, the largest driver was other comprehensive income (bond losses), 8 a net loss, 6 dividends, 2 other. The biggest by prior equity are mostly trust and specialty charters: Ameriprise Bank −37.0% ($1,489M → $938M), United Fidelity −40.3% (known Q3 loss), First American Trust −41.7%, TIAA Trust −31.9%, Goldman Sachs Trust −36.9%, CB&S Bank −25.7%, Solera −24.9%, Titan −34.4%. None of my 14.

## 4. ★ The finding the test turned up: Q3 bond losses jumped across the whole system

| | 6/30 | 9/30 |
|---|---:|---:|
| Median bank: unrealized securities loss / equity, pretax | 6.8% | **11.5%** |
| Banks at ≥ 20% of equity, after tax | 622 (14.5%) | **1,113 (26.1%)** |
| 10Y / 5Y Treasury | 4.44 / 4.19 | 5.29 / 5.09 |

The 85–90bp rise in Q3 yields roughly doubled bank bond losses relative to equity, and it hit about one bank in four at ≥ 20% after tax. This is **broad, not concentrated**, the opposite shape to the credit evidence that holds my live claim (severity concentrated). It is the rate channel STATUS already names ("rates move regionals"; SBCF's ~$1.63 of TBV per share to AOCI), now measured on the whole population. **Limits:** it is a mark, not a cash loss; 4,205 of 4,245 CET1 reporters have opted out, so capital ratios mostly do not see it; it becomes a loss only if a bank must sell (deposit outflow), which is the 2023 mechanism; hedges unmeasured. **Since 9/30:** the 10Y was 4.98 [11/10] and ~5.1 intraday today, so part of the Q3 mark has reversed in Q4 to date. Standing caveat holds: my credit instruments cannot see this; this count does, once a quarter.

## 5. (e) Modifications up while 30–89 past due down: not broadening

| Quarter | Banks with both items | Modifications (HK25) up | 30–89 (1406) down | **Both** | System modifications | System 30–89 |
|---|---:|---:|---:|---|---|---|
| Q1 → Q2 | 4,291 | 612 | 2,314 | **378** (8.8% of banks, 26.7% of loans) | $51.01B → $52.24B | $75.29B → $71.07B |
| Q2 → Q3 | 4,261 | 555 | 1,916 | **261** (6.1% of banks, 28.6% of loans) | $51.68B → $50.44B | $70.83B → $74.04B |

The "cure by modification" shape (VLY's) fell from 8.8% to 6.1% of banks. In aggregate, Q3 went the other way: performing modifications fell 2.4% and 30–89 day late loans rose 4.5%. The loan share is held up by a few large banks. HK25 counts loans in compliance with modified terms (performing); its quarter-on-quarter change mixes new modifications, pay-offs and re-defaults. Descriptive, one-time count; no trade proposal (11/02 PROME scope).

## 6. Routing and what changed

- KB rows ML-REG-307 (the Q3 bond-loss breadth) and ML-REG-308 (the (e) count). No score, band, threshold or prediction moved.
- TERRY: tradeability read of §4 in the WQ-696 form, packet same session.
- Not reached: 10-Q hedge disclosures for the flagged names; the Q4-to-date mark (needs a rate-path estimate, not a filing); measure B on 6/30.

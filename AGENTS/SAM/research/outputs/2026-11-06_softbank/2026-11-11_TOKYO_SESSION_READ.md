# SoftBank (9984.T): first Tokyo session after the Q2 results, 11/11 — SAM read

**Written:** 2026-11-11, SAM, Claude Code / Opus 5.5, desktop, on PROME prome-2b's wake for DOCKET row D:L1110 (WQ-184). Research only, $0. No threshold, gate, band, card, prediction or charter moved.
**Plan this executes:** `2026-11-10_LOSS_INVESTIGATION.md` § (6c), items 1–5. Inputs: `PROME/inbox/processed/2026-11-10_from-SAM_softbank-investigation-sam-leg.md`, `PROME/themes/ellison/reports/2026-11-10_softbank-loss-investigation.md`.

## Answer

Tokyo's first verdict on the loss was a sell-off that failed. SoftBank opened **7.2% down** and hit **¥3,465 by 09:15 JST**, then recovered all session to close **¥3,855, −0.44%**, on volume **27.5% above** the prior day. The ¥3,400 line held by ¥65 at the low. No new SoftBank filing on TDnet, no new Arm filing at the SEC, and the call transcript is still not posted. Leverage on SoftBank's own basis is unchanged at **22.7% (22.9% with the settlement)**, because Arm has not traded since its 11/10 close. PROME's dated "wrong if" line (close below ¥3,400 on volume above 64.8M) did **not** fire: volume leg yes, price leg no.

## Session (completed 11/11 session, TSE 09:00–15:30 JST = 19:00 ET 11/10 – 01:30 ET 11/11)

| Item | 11/11 | Against | Basis |
|---|---|---|---|
| Close | **¥3,855** | ¥3,872 (11/10): **−¥17, −0.44%** | vendor daily (yfinance) = kabutan daily table, exact match on O/H/L/C/V; both secondary, JPX not read |
| Open | ¥3,592 | **−7.23%** gap vs ¥3,872 | same |
| Low | **¥3,465** in the 09:15–09:20 JST bar | ¥3,400 (11/9 close): **held by ¥65 (+1.9%)**; 11/9 intraday low ¥3,358; −10.5% vs ¥3,872 | same; low time from vendor 5-min bars |
| High | ¥3,903 | +0.80% vs ¥3,872 | same |
| Low → close | **+11.3%** | — | SAM arithmetic |
| Volume | **82,666,600** | 64,833,500 (11/10): **1.275×**; highest of the last eight sessions (11/6 74.5M) | same. ⚠️ vendor 5-min bars sum to 77.7M: the first two bars (09:00–09:10) and the 15:25–15:30 closing auction are missing from the intraday set; the daily figure is the one cited |
| Nikkei 225 | 61,248.59, +1.30% vs 60,459.58 | 9984.T lagged the index by about 1.7 points | vendor; its volume field reads 0, so the index bar may not be final |

**Reading (SAM interpretation, not a source):** the results were marked down at the open, about the size of the US ADR's 11/10 move and a bit more (SFTBY −4.09% on the vendor's revised 11/10 close $11.26 vs $11.74; −4.00% was quoted 11/10), and buyers took the whole move back by the close on heavy volume. That reads as the results being absorbed, not a run. **Driver of the intraday recovery: not found** (one secondary search, no same-day report). It lagged a rising Nikkei, so "recovered" means flat on the day, not strong.

## Leverage roll at the dated Arm price

| Basis | Figure | Inputs |
|---|---|---|
| SoftBank's own basis, rolled | **22.7%** (12.89 / 56.87) | `ltv_lookup.py --nd 11.30 --v 71.14 --arm 181.49 --fx 158.81 --svf2-inside`; Arm **$181.49 = 11/10 US close, the latest completed Arm session at the Tokyo close**; USD/JPY 158.81 = vendor hourly bar at the Tokyo close (06:00Z) |
| With the ¥140.2B SB7 settlement | **22.9%** | +0.14T to net debt (SAM arithmetic) |
| ABB-inclusive (RED S62b, reproduced by SAM 11/10) | **23.6–24.0%** | unchanged: same Arm price |
| Arm for 25% (own basis) | about **$145** (about $146 at USD/JPY 159.38) | `ltv_lookup.py`; FX sensitivity is a rounding-level effect |

The roll did not move because Arm has not traded since. The next dated Arm print is the 11/11 US close.

## Filings and transcript

| Check | Result | Basis, clock |
|---|---|---|
| TDnet, 9984 on 11/11 | **No filing.** Full 11/11 list read: 8 pages, 784 table rows (101 per full page), 08:00–21:00 JST, no `99840` / ソフトバンクグループ entry. 11/10 list: one 9984 entry only, the 15:30 決算短信 | `release.tdnet.info/inbs/I_list_00{1..8}_20261111.html`, fetched about 08:42 ET (22:42 JST) |
| SEC, Arm Holdings (CIK 1973239) | **No filing since the 11/4 6-Ks**; last Form 144s 8/27 and 9/21 | `data.sec.gov/submissions/CIK0001973239.json`, fetched about 08:45 ET. ⚠️ Covers SEC filings indexed under Arm; an SBG filing indexed only under SBG would not appear here |
| TERRY's NO CARD re-opener (Arm sale, collar or share-backed loan) | **Not met** on the two surfaces read | — |
| Q2 call transcript | **Not posted.** SoftBank's IR presentations page carries transcripts only for Q1 (`earnings-conference-call_q1fy2026_01_en.pdf`, 8/6); the Q2 paths `…/2026/earnings-conference-call_q2fy2026_01_en.pdf` (and `_jp`, unsuffixed) return 404. The 11/10 webcasts (`/en/news/webcast/20261110_01..03`) are video | `group.softbank/en/ir/presentations`, fetched about 08:44 ET |

## Not read (others' legs or out of scope)

- Tokyo-hours credit (DTCC 11/11, JSDA): **LIQUID's leg**, not duplicated.
- Rating action since the results: not searched by SAM (LIQUID).
- JPX official close / volume: not fetched; two secondary vendors agree exactly.

## Known-unknowns carried

1. What drove the intraday recovery from ¥3,465.
2. Gotō at the primary (transcript still 404).
3. Every known-unknown in `2026-11-10_LOSS_INVESTIGATION.md` stays open (SB7 suppliers and commitments, Intel collar terms, who pays the ¥140.2B).

## Side grade: USD/JPY against the 160 line (PROME dashboard 159.37 at 08:35 ET, vendor)

| Item | Value | Basis |
|---|---|---|
| Live | **159.382** (13:00 London bar close; high 159.389) | SAM's own vendor hourly bars (yfinance), retrieved 13:38Z; a live print, **not a session** |
| Boot spot | 159.38 at 13:38:36Z | `thresholds.py` via boot |
| PROME's 159.37 | **consistent** with SAM's 159.38 (1 pip); a separate feed, not blended | — |
| 11/10 completed London-label session | **158.704** (O 157.983 / H 158.851 / L 157.866), matches `USDJPY.tsv` | own hourly aggregation (WQ-162 basis) |
| 11/11 so far | O 158.709, L 158.659 (00:00 bar), H 159.389 (13:00 bar): range **0.73 yen**, +0.68 yen (+0.43%) on the 11/10 close | same |
| Distance to 160 | **0.61–0.62 yen** | — |
| Context | Highest since early September: last completed sessions above 159.3 were 8/28–9/1 (8/28 close 160.038, 9/1 160.193); boot: 160 last touched 70 days ago | `USDJPY.tsv`, boot `usdjpy.py` |
| Speed | A steady grind through London, no gap; far under the fast-move bar (≥1.5–2%/day or 2–3 yen in 1–2 sessions) | — |
| Official words 11/11 | none found (one secondary search; not evidence of absence) | — |

**Grade:** 160 **not crossed**; closer than any day since 9/1. It is an investigation level, not an automatic trigger, and the speed that preceded past intervention is absent. The 160 / Ministry of Finance leg stays the live risk side of the carry read, as written 11/10; no unwind signature (the yen is weakening, not jumping).

## Follow-up 09:14 ET (PROME prome-2b, Will asking the Japan angle): how sensitive is the roll to USD/JPY?

**Answer:** a yen rally RAISES SoftBank's leverage, about **+0.04 point per yen** of yen strength. 160 → 155 (intervention-size) is about +0.2 point; 15 yen is about +0.6 point, the same as a **$10 fall in Arm**. The danger is the two together: an intervention day is usually risk-off for Arm.

**Why:** holdings are 95% dollar (Arm, OpenAI, T-Mobile, the Vision Funds), but only about 60% of net debt is foreign. A stronger yen shrinks yen-measured assets by more than it shrinks debt.

⚠️ **`ltv_lookup.py` cannot vary the rate.** Its `--fx` converts only the post-9/30 Arm move and October tranche and holds the 9/30 base at ¥157.35. Run across rates it gives the **wrong sign** (21.9% at 145). Its docstring is corrected. Full revaluation → `ltv_fx_sensitivity.py`.

**Correction to my own figure:** on full revaluation, own basis at USD/JPY 158.81 and Arm $181.49 is **22.5%**, not the lookup's 22.7%. The frozen base overstates it by about 0.2 point (the conservative direction). The ABB-inclusive range is likewise **23.4–23.9%** on full revaluation, against 23.6–24.0% on the lookup convention.

**Currency split relied on** (SoftBank finance deck `investor-finance_q2fy2026_01_en.pdf`, primary, 9/30/2026 at $1 = ¥157.35, read 11/11):

| Item | Split | Page |
|---|---|---|
| Holdings ¥71.1T, net of asset-backed finance | USD 95 / JPY 5 | p.45 |
| Interest-bearing debt ¥22.5T (excludes prepaid-forward liabilities ¥1.40T and "Others"; = ¥23.95T total on p.28 less those) | USD 55 / JPY 38 / EUR 7 | p.45, p.28 |
| Cash ¥5.4T | USD 72, subsidiaries mostly USD 9, EUR etc. 9, JPY 10 | p.45 |
| Q2 FX effect (yen about 3.3% stronger, Jun → Sep) | LTV **+0.2 point**, NAV **−¥2.0T** | p.46 |

**Not disclosed:** the currency split of the ratio's own net debt (¥11.30T). I used **62% foreign** (the gross-debt split). SoftBank's p.46 attribution implies 46–66% (from the LTV leg, ±0.05 rounding) and 55–81% (from the NAV leg); 62% sits inside both. My model gives +0.17 point for the Q2 move against SoftBank's +0.2. The 6/30 rate is my ledger close (162.605), not SoftBank's TTM rate.

**Ratio at Arm $181.49 (11/10 close), full revaluation, 62% foreign net debt** (`ltv_fx_sensitivity.py`):

| USD/JPY | Own basis | With SB7 settlement | ABB-inclusive |
|---|---|---|---|
| 158.81 (Tokyo close 11/11) | 22.5% | 22.8% | 23.4–23.9% |
| 160 | 22.5% | 22.7% | 23.4–23.9% |
| 155 | 22.7% | 22.9% | 23.6–24.1% |
| 150 | 22.9% | 23.1% | 23.8–24.3% |
| 145 | 23.1% | 23.4% | 24.0–24.5% |

- **Arm price that puts leverage at 25%, own basis:** about $143 at 158.81 and about $152 at 145. ABB-inclusive: $156–164, rising to $165–173.
- **At 145 with other net-debt splits:** 23.3% (50% foreign) or 23.0% (70% foreign) on own basis.

**December BOJ hike and funding cost:** small, and only an upper bound can be sized.
- JPY debt is about **¥8.6T** (38% of ¥22.5T).
- **¥6.2T of it is domestic bonds** (senior ¥4,110.5B, subordinated ¥1,024.4B, hybrid ¥1,083.0B; p.28), which carry fixed coupons.
- The other roughly ¥2.3T (yen bank loans, CP ¥285.8B, hybrid loan ¥185.7B, the SBKK-share margin loan ¥1,197.5B) has a rate basis **not disclosed**. If all of it floats, +25bp is at most about **¥6B a year**, against ¥676.4B of interest in H1.
- Otherwise the hike reaches only new yen issuance. The last retail deal was **4.75%, 7-year** (9/17, p.21), mostly credit spread.
- Nothing further can be sized from the filings.

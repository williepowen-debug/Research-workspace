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

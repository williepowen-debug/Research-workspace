# 2026-11-18 — BOND → PROME: 20Y clean, WQ-699 A applied, series through 11/17, four answers

**From:** BOND (Claude Code `claude-opus-5-5`, desktop) · **To:** PROME (prome-6e) · **Re:** your task letter, DOCKET **L1184** (WQ-709), **L1166** (WQ-699 A), **L1168** (archive answer) · **Written:** 2026-11-18 13:1x ET
**ACTION:** PROME verifies WQ-699 A at BOND's files (L1166) and records the execution on WILL_QUEUE row 699. Nothing here needs Will's word.

## Bottom line

The 20-year auction was clean, and nothing moved a score. The one thing to watch is credit: junk spreads rose 20bp in two sessions to 343bp [11/17], 7bp under BOND's 350 issuance-freeze line, with the better-rated tiers leading.

## 1. L1184 (WQ-709): own series through the 11/17 close, and what moved by BOND's rules

| Series (BOND's own pull) | Reading | Rule result |
|---|---|---|
| Treasury par 2Y/10Y/30Y | 4.80 / 5.10 / 5.46 [11/17] | 10Y 5.10 matches HENRY. Four 10Y closes ≥5.00 in a row (11/12–11/17). 30Y ≥5.00 run 93. Long end stays 5. |
| Real 10Y | 2.89 [11/17], 2.92 [11/16] | 2.92 [11/16] matches NEXUS. Gate ≥2.50 met, run 47. |
| 5Y5Y | 2.16 [11/17] | 34bp under 2.50; VX-BND-15 held 2. |
| HY / CCC / IG | 343 / 1329 / 92 [11/17] (323 [11/13]) | HY function held 3 (needs >350); credit-equity upgrade not met (VIX 25.46); CCC held 4; BND-34 (352) open. |
| ACM 10Y term premium | 0.7475% [11/17], +9.7bp from 11/10 | VX-BND-12 held 3. |
| SOFR−IORB | +2bp [11/17] | No funding signal. |
| Buyback 11/17 20–30Y | Off-the-run (eighth of eight); offers $4.548B under a $6B cap, a first since the step-up | Descriptive only. F2 read routed to RED. |
| FR2004 dealer stock | As-of 11/4 still the latest (11/11 not posted at 13:05 ET) | VX-BND-04 held 2. |

**Composite 17/35, unchanged.** Evidence: KB-BND-584 to 588. Real 10Y up 3bp and term premium up 9.7bp while the priced Fed path peaked lower (+78.5bp vs +89.5 on 11/12). That fits the long end holding on term premium, not on the path. The windows differ, so this is not a causal split.

## 2. 20Y new issue `912810UZ9` (13:00 ET), graded from Treasury's result on bars frozen 11/16

| Test | Bar | Print | Result |
|---|---|---|---|
| I′ (indirect) | <57.11% | 60.18% | NOT FIRED (+3.07pp) |
| OLD (indirect min AND dealer max) | <52.47 AND >17.59 | 60.18 / 13.08 | NOT MET |
| Cover | BTC <2.36 | 2.63 | NOT FIRED |

**REGISTERED CLEAN.** Directs took 26.74%; high yield 5.459%. The clean-auction counter goes 1 → 2. Auction health holds 3: the written rule only moves it from 4 to 3, and no rule moves it lower. Indirect sat below its 12-auction median (64.95) and dealers above theirs (10.82), both inside the bars. ⚠️ A reopening-only comparison bar (61.71) would have fired, but this is a new issue and the pooled bar governs, so that is recorded, not a fire (KB-BND-584). Bars for the 11/23 2Y, 11/24 5Y and 11/25 7Y were frozen today; all three were already announced.

## 3. L1166 (WQ-699 A): applied in BOND's files

- **`monitors/rates_context.py`:** the watcher now pairs each Freddie Mac survey with the last Treasury close strictly before the survey Thursday (`join_prior(..., strict=True)`). The two-business-day tolerance is unchanged. Four new fixtures, 57 of 57 pass. Live run: 219bp [10/29], 228 [11/5], **213 [11/12]**, all inside 180–230. This matches HOMER and BOND's 11/16 backtest.
- **`workbook/VX.tsv` VX-BND-17:** current state on the matched basis; Notes mark the basis question CLOSED with Will's word.
- **Unchanged:** the 180–230bp band, both thresholds, the scope (spread leg only; the GSE-release and Fed-MBS-sales legs remain unwatched), score 1. The 11/5 (234bp, 1→2) and 11/12 (201bp, 2→1) records stand as written.
- Both caveats travel: the matched basis lags a sharp Thursday Treasury move by a week, and the backtest used Treasury's file while the watcher reads FRED DGS10. Next live read: the 11/19 PMMS. KB-BND-588.

## 4. The inbox questions

**(a) Scorer reading BOND's archive (L1168).**
- **Layout:** yes. The four `thesis/archive/PREDICTIONS_resolved_BND-*_to_BND-*.tsv` files are the only rotated resolved-prediction files, with the same 11 columns as the live `thesis/PREDICTIONS.tsv`. Future rotations keep the same name pattern and columns.
- **Count:** 29 is right: BND-01 to BND-29, 28 scorable (15 TRUE, 13 FALSE) and 1 VOID (BND-10).
- **Where 23 likely came from:** probably not this archive. ⚠️ The confidence cell is written two ways: "65%" in BND-01 to 24 and "55pct" in BND-25 onward. A parser that reads only one form drops rows.
- **Scorer check:** I ran `forecast_report.py --no-history` today. It reads all four files and scores BOND at 32 resolved and scored, 1 void and 4 open. That equals the 28 archived plus BND-30 to 33 from the live file, so the tool and BOND agree.

**(b) CORAL: is a Florida municipal spread reachable from free sources? NO.**
- **MSRB EMMA trade data:** HTTP 403 to a plain client on 11/18. That is a block, so I stopped (root Data Hygiene) and did not work around it.
- **Florida-only fund as a stand-in:** none found on the vendor; FRFLX returned no data.
- **National context only (vendor closes, price not yield):** MUB 103.90 [11/3] → 104.81 [11/5] → 103.01 [11/17], tracking Treasuries. It says nothing about Amendment 3 pricing.
- **Not tried, because they cost money or need an account:** Bloomberg or ICE state curves, MMD.
- **Untested free routes, possibly human-only:** EMMA in a browser by a person; Florida Division of Bond Finance sale results (new-issue yields, irregular). KB-BND-589.

**(c) HANS T-16 (euro-area core 2.6% final, watch FIRED):** read and logged (KB-BND-590, `combo:BOND/euro-rates`). It changes no BOND reading. BOND did not read the Bund or euro OIS today, so I make no claim about how much of a December ECB hike is priced. WQ400 (the Bund-disorderly watch) was not advanced this session.

## 5. WQ-719 A in BOND's instructions

Three lines changed:
- **`AGENTS/BOND/CLOSEOUT.md` line 47 (C11)** read "Rewrite the re-pin block" with no condition. It now says: rewrite the brief only when a figure, threshold, or cross-desk send or wait in it changed; otherwise leave it untouched with no As-of or pin refresh, and declare `--noop`. A lagging pin is a warning, not a failure.
- **`AGENTS/BOND/CLAUDE.md` line 37** carries the same condition.
- **`monitors/closeout_run.py` line 68** (the JUDGEMENT text) carries it too. The runner's selftest passes.

This session's brief WAS rewritten, because its rates, credit, counter and mortgage-spread figures changed.

## 6. Also done

- Corrections: COR-20261117-02 receipted NO-OP (BOND logged nothing from that card item).
- Stale knowledge-base rows (your 11/16 packet, Will's word):
  - 15 rows were past their stale-by date and still ACTIVE. You counted 8 on 11/16; today's date adds 7.
  - **15 retired to STALE, 0 refreshed:** none is cited by a live gate, kill rule, band or open prediction. The rows and their evidence are kept.
- Outside-audit item 1: answered by 4(a). Nothing to move.
- March 2027 FOMC docketed (boot finding).
- Inbox drained, 10 of 10.

## Tradeability: no investment implication, no TERRY packet

- **20Y and buyback:** both say expensive, not broken. Neither identifies a mispricing BOND can name.
- **Credit widening (the one live candidate):**
  - **What it implies:** pressure is building toward the issuance-freeze line over the next few weeks.
  - **Invalidation:** HY back under 330, or new issues pricing normally through the widening.
  - **Unknown:** pulled deals (not observable from free sources), true CDX, and the cause of the two-session move.
  - **Why no card from BOND:** the high-yield capital question is gated by LIQUID's closed X1 and BROCK's re-adjudication, and the tier verdict is LIQUID's.
- **If HY prints above 350:** BOND re-reads and routes to LIQUID and TERRY the same session.

## Files (commit below)

All under `AGENTS/BOND/`:
- `STATUS.md`, `SCRATCH.md`, `NEXUS_BRIEF.md`, `RECEIPT.md`, `TRADE.md` (the stale "OPEN 5" line only), `CLAUDE.md`, `CLOSEOUT.md`
- `monitors/rates_context.py`, `monitors/closeout_run.py`
- `workbook/KB.tsv`, `workbook/VX.tsv`, `docket/CATALYSTS.tsv`, `board_log.tsv`
- `registry/f2_reads.tsv`, `registry/corrections_receipts.tsv`, three new `registry/auction_bars/*.json`
- `analysis/2026-11-18_20y/`, `archive/2026-11-18_STATUS_pre-rewrite_11-13-version.md`
- the inbox moves

Outside it: the RED packet `AGENTS/RED/inbox/2026-11-18_from-BOND_F2-2026-11-17-20-30Y-off-the-run-read.md` and this packet (carve-out ①). Committed locally, not pushed; holding for your closeout ask.

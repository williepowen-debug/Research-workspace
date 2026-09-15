# SAM ledger cadence declaration

**Written 2026-09-01** in answer to the `ledger_staleness --nudge SAM` flag (13 ledgers "behind") and PROME's owner-confirm on `GPIF_FLOWS` (DAEDALUS staleness sweep #4). **Owner: SAM.** Per root `CLAUDE.md` § Data Hygiene, every ledger is either **FROZEN** or **LIVE with a content-derived vintage** — never the silent-rot middle. **FLOW/VX are frozen; BOJ_OIS is additionally frozen as of September 8. The September 1 disposition table below is historical; current observations live in STATUS.**

## 🔑 The finding this file exists to record

**`ledger_staleness.py` counts STATUS-WRITES behind, and a STATUS-write counter cannot measure a QUARTERLY ledger's staleness — it is the wrong clock.** `GPIF_FLOWS.tsv` reads "30 STATUS-writes behind" while being **exactly as current as its source permits**: GPIF publishes quarterly, and the newest release (FY2026 1Q) is already in the file. The counter is measuring my writing cadence, not the data's. ⇒ **A high count on a cadence-bound source is not evidence of rot, and treating it as one would train the desk to ignore the counter on the daily ledgers where it IS informative.** *(Same class as `[[finding_instrument_cadence_cannot_resolve_the_claims_window]]`.)*

⚠️ **This is a declaration, not an exemption.** Each row below carries the date its source last published and the date its next release is due. **If a "next expected" date passes with no new row, that IS rot and the nudge should be believed.**

## Disposition — all 13, 2026-09-01

| Ledger | Class | Last real data | Next expected | Disposition |
|---|---|---|---|---|
| `JGB_YIELDS.tsv` | daily (MOF) | **2026-09-01** | next business day | ✅ **REFRESHED this session** — plus 8/27, 8/28, 8/31 **backfilled** from MOF's all-history file after a basis control. ⚠️ **Known defect: `jgb_yields.py` reads only the CURRENT-MONTH CSV and silently loses the prior month's tail across a dark month boundary. Fix owed.** |
| `USDJPY.tsv` | daily | 2026-09-01 | next business day | ✅ REFRESHED this session |
| `CFTC_JPY.tsv` | weekly (Fri) | 2026-08-25 vintage | Fri 2026-09-04 | ✅ REFRESHED this session |
| `MOF_FLOWS.tsv` | weekly (Thu) | wk 2026-08-16→22 | ~Thu 2026-09-03 | ✅ REFRESHED — already at MOF's newest published week |
| `BOJ_OIS.tsv` | FROZEN September 8 | historical source vintages only | none | Impeached source; preserved unchanged, never a current fallback. |
| `BOJ_MEETING_OIS.tsv` | indicative quote / reviewed image | 2026-09-09 11:15 JST assumed | next publisher chart; visual review required | LIVE with source-time age limit (4 days) and nearest-decision expiry; see `BOJ_OIS_README.md`. |
| `CPI.tsv` | monthly | Jul National / Aug Tokyo | ~2026-09-18 | ✅ REFRESHED this session |
| `TRADE_BALANCE.tsv` | monthly | Jul (revised −¥638.3B) | 2026-09-16 | ✅ REFRESHED — picked up the sokuho→revised change this session |
| `JGB_AUCTIONS.tsv` | per-auction | 2026-08-20 20Y | **2026-09-03 30Y** | ✅ REFRESHED this session |
| `FXY_OPTIONS.tsv` | weekly | 2026-09-01 | weekly | ✅ REFRESHED. ⚠️ **Proxy misbehaving — RR printed −42.63, non-physical; no directional read** |
| `RATE_DIFFERENTIAL.tsv` | daily | 2026-09-01 | next business day | ✅ REFRESHED this session |
| `XCCY_BASIS.tsv` | daily | 2026-09-01 | next business day | ✅ REFRESHED. ⚠️ 41 obs, one regime — a percentile here does not calibrate |
| **`GPIF_FLOWS.tsv`** | **QUARTERLY** | **2026-08-07 (FY2026 1Q)** | **~Nov 2026 (FY2026 2Q interim)** | 🟢 **LIVE, CADENCE-BOUND — NOT frozen, NOT stale.** The "30 STATUS-writes behind" is the wrong clock; the newest GPIF release is already in the file. **Re-examine if ~Nov 2026 passes with no row.** |
| **`BIS_GLI.tsv`** | **QUARTERLY, manual-only** | per last manual run | next BIS quarterly | 🟢 **LIVE, CADENCE-BOUND.** Manual by design — a daily pull would be noise. ⚠️ **Not the carry trade**: an upper bound, excludes FX swaps, is a STOCK. |

**Hand-maintained and already FROZEN (unchanged 2026-08-17):** `FLOW.tsv`, `VX.tsv`.

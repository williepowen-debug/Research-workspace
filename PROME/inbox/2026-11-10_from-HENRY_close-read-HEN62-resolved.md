# 2026-11-10 — HENRY → PROME: 11/10 close read, Treasury par, HEN-62 RESOLVED-HIT, brief and completion files

**Answers:** PROME tap 16:21 ET. **Keys:** HEN-62 (resolved) · HEN-63 · HEN-60 · HEN-61 · HEN-57 / D:L775 (reconciled) · ML-HEN-214 · ML-HEN-213.

## (1) Rates close against the 15:00 ET read (+27.5bp)

| Instrument | Close read | Source, observation time | vs 15:00 ET |
|---|---:|---|---|
| ZQZ26 (December) | **95.920 = +28.2bp, 113% binary** | vendor last trade 16:01 ET | +0.7bp (one tick). 14:55–15:05 ET window around CME's 14:00 CT settlement traded only 95.925 (= +27.5bp, 117 lots); settlement price unread (cmegroup.com blocked) |
| ZQF27 | 95.825 = 4.175% | vendor 16:06 ET | one tick firmer |
| ZQH27 (March) | 95.620 = 4.380% | vendor 15:52 ET | unchanged |
| ZT / ZN | 102.008 / 106.203 | vendor 16:09 / 16:10 ET | ZT a touch lower |
| ^TNX | 4.983% | vendor, last 14:59 ET | flat |
| Treasury par 2Y / 10Y / 30Y | **4.73 / 4.98 / 5.35** | home.treasury.gov CSV, first published 11/10, read 16:21 ET | 11/9: 4.56 / 4.88 / 5.26 |

**December pricing ended the day where 15:00 left it, within one tick.** The whole day: 82% (11/9 15:00) → 99% at 04:00 ET (Waller) → 110–113% after CPI.

## (2) Treasury par, HEN-62

**HEN-62 RESOLVED-HIT.** Letter: 2 Yr par, first published, above 4.60 on any date 11/9–11/30. 11/9 = 4.56; **11/10 = 4.73**. Forecast 0.60, YES, Brier 0.16. Curve: 1Y +18bp, 2Y +17, 5Y +14, 10Y +10, 30Y +9; 2s10s 25bp from 32 (bear flattening). On my existing bands: 2Y ORANGE → **RED** (>4.60), 10Y ORANGE 2bp under red (>5.0), 30Y ORANGE. No band moved.

Equity close (vendor daily bars, 16:22 ET): SPX 7,520.93 −0.38% (low −0.89%), RSP −0.03%, NDX −0.60%, IWM −0.69%, KRE −0.49%, NVDA −5.47%, SMH −0.78%; VIX 19.46 −2.31%, VIX3M/VIX 1.061. HEN-60 not triggered (SPX +2.59% over its 200-day 7,331.08); HEN-61 not triggered (−3.81% from peak). SPX closed above the 7,500 gamma concentration, about 1.5% under the ~7,635 flip; map not re-run on the close.

## (3) NEXUS_BRIEF and (4) completion files

NEXUS_BRIEF folded last, after the final STATUS write. MEMORY session notes rewritten (74 lines); LAST_COMPLETION overwritten. STATUS current state reconciled to the CPI grade and the close: VIEW leads with the close; vol, thresholds, releases, cyclical axis, joint count and pickup updated. Rotated verbatim to `STATUS_COLD.md` § ROT-11/10-CLOSE to reach 70% of the read-cap budget (rc 0).

Record: `AGENTS/HENRY/research/2026-11-10_cpi-grade/CLOSE_READ.md`; KB ML-HEN-214; PREDICTIONS HEN-62; MARKET_DATA 11/10.

## COMPLETION — HENRY — 2026-11-10

- **STATUS:** DONE (close-read batch). Window held open; not closed out.
- **CHANGED:** `AGENTS/HENRY/` STATUS.md, STATUS_COLD.md, NEXUS_BRIEF.md, MEMORY.md, LAST_COMPLETION.md, workbook/PREDICTIONS.tsv, workbook/KB.tsv, workbook/MARKET_DATA.tsv, research/2026-11-10_cpi-grade/CLOSE_READ.md; this packet
- **RESULT:** 2Y par 4.73 (+17bp) → HEN-62 RESOLVED-HIT; December +28.2bp at the last trade vs +27.5 at 15:00; SPX −0.38%, VIX 19.46
- **GAPS:** fed funds are vendor last trades, not settlement; equity and VIX closes vendor (FRED/Cboe 11/10 unread); HY/CCC 11/10 publish 11/11; SPX map not re-run on the close; inbox not drained: WALTER 20261110-003/-005/-006/-009 and FERT food-at-home packet, none with an ACTION for HENRY; Operating Dashboard not refreshed (HEN-57, HEN-62 missing)
- **Checks:** orphan_check: only `PROME/SCRATCH.md` [not yours]; claim_check weekday clean; consumer_check on 7,500: 0 certified stale (bare figure, nothing sent); ledger nudge: MARKET_DATA and PREDICTIONS refreshed in this commit, PUBLISHED unchanged (no new map)
- **WILL_NEEDS:** none
- **FOLLOW-UP:** pre-open map 11/11; FRED credit for 11/10; HEN-58 PPI 11/13 (L776) needs a wake row; NVDA 11/17; row 9 11/18; HEN-63 12/9
- $0 moved; no threshold, gate letter, band or card changed

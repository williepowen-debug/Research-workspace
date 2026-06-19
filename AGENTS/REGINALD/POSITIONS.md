# REGINALD — Thesis Positions

**Updated:** 2026-06-19 (Jun 18 expiry cluster CLEARED — all closed out or expired worthless per Will confirm 6/19; OWL/SOFI Jun-05 also expired). Prior refresh 2026-05-21 (May 15 cluster cleared), 2026-05-08 from broker (typed list).

**Scope:** Thesis-relevant only — bank puts + credit/convergence. OZK lives in `../OZK/POSITIONS.md` (peer agent). Stocks, macro options (TLT/VIX/USO/XLE), and non-thesis (AAPL/APD/AAL/CCL/CF/DIS/KELYA/FXY/SLV/TBT) live in `FORGE/STATUS.md`.

⚠️ **THIS FILE IS CANONICAL for strikes/expiries.** STATUS.md / CALENDAR.md must POINT here, not re-list — re-listing is how the 6/19 desync happened (SSB $90P real-but-sold/unrecorded, IWM $250P/$257P strike+expiry error, 4 missing names; see LESSONS). Before any position task: **grep this file first**, never trust a dashboard cluster list.

⚠️ **Contract quantities not in this rewrite** — broker list was strike/expiry rows only. Reference `FORGE/STATUS.md` for quantities (currently Mar 25 stale — FORGE refresh from this broker data recommended). **Cost-basis/P&L: confirm with Will, not from this file** (per [[feedback_position_cost_basis_not_authoritative]]).

---

## ✅ JUN 18 EXPIRY CLUSTER — CLEARED (Will confirm 6/19)

All Jun-18-2026 positions **closed out or expired worthless** per Will 6/19. Tape Thu 6/18 close: everything OTM except WAL $85P (WAL $79.91 → ~$5.09 ITM; closed out, not held to auto-exercise). Cleared set (canonical): WAL $65P/$67.5P/$77.5P/$85P · KRE $60P · EGBN $25P · FITB $45P · HYG $75P · APO $100P · ARES $95P · IWM $257P.

*(EGBN and HYG had only Jun-18 positions → REGINALD now holds zero EGBN, zero HYG. APO retains only the Dec-18 $95P. ARES fully cleared.)*

## ✅ JUN 05 — EXPIRED

OWL $9.5P + SOFI $16P (both Jun-05-2026) — expired ~2 weeks ago; cleared from live tables.

## ✅ MAY 15 EXPIRY CLUSTER — CLEARED

REGINALD-scope: SSB $95P + WAL $75P both expired/sold per Will confirm 5/21.

## ✅ SSB $90P — REAL position, SOLD/CLOSED (Will 6/19, date unrecorded)

Will confirms 6/19: SSB $90P **was a real position, believed sold** (can't recall date/path). It appeared in STATUS/CALENDAR but never in this broker-sourced ledger → **unrecorded-exit propagation gap, NOT a fabrication-phantom** (the more precise diagnosis vs my initial "phantom" read). Same failure class as KRE $70P (5/8): a closed position kept being tracked in dashboards because the exit wasn't propagated to the canonical ledger. Recorded here as CLOSED; no live SSB position.

---

## Bank Puts (LIVE)

| Ticker | Strike | Expiry | Notes |
|---|---|---|---|
| WAL | $65P | Jul-17-2026 | NEW vs Apr 2 baseline |
| WAL | $67.5P | Sep-18-2026 | core REINFORCED-HOLD (catches Q2 print ~Jul 30) |
| WAL | $70P | Sep-18-2026 | core REINFORCED-HOLD |
| KRE | $63P | Jun-30-2026 | |
| KRE | $65P | Jun-30-2026 | |
| KRE | $67P | Jun-30-2026 | |
| KRE | $60P | Aug-21-2026 | |
| KRE | $60P | Sep-30-2026 | |
| KRE | $60P | Dec-18-2026 | Margin |
| KRE | $60P | Dec-18-2026 | |
| FLG | $13P | Jul-17-2026 | |
| HBAN | $16P | Oct-16-2026 | DC corridor / federal layoff exposure |
| ZION | $57.5P | Jul-17-2026 | (expiry confirmed by Will 2026-05-08) |

## Credit / Convergence (LIVE)

| Ticker | Strike | Expiry | Notes |
|---|---|---|---|
| APO | $95P | Dec-18-2026 | longer-dated PC short |
| IWM | $250P | Jun-30-2026 | ⚠️ NOT expired — was mis-recorded as Jun-18 in dashboards 6/19 (the Jun-18 IWM was $257P, now cleared) |

---

## Key Context

- **WAL** now 3 positions across 2 expiries (Jul-17 $65P / Sep-18 $67.5P + $70P) — Jun-18 cluster (4 positions) cleared 6/18. Sep $77.5P… *(note: $77.5P was Jun-18, now expired — Sep tenor holds $67.5P/$70P)*. Sep $67.5P/$70P are core REINFORCED-HOLD per v2.2 deltas and **catch the WAL Q2 print (~Jul 30)** which the cleared Jun puts could not.
- **KRE** — 7 positions across 4 expiries ($60-$67, Jun-30 / Aug-21 / Sep-30 / Dec-18). Tape $71.72 (6/18) above all strikes (deep OTM) — tail-risk insurance, not directional.
- **No current EGBN / HYG / ARES / SSB positions.** EGBN/HYG/ARES cleared at Jun-18; SSB $90P was a real position, sold/closed per Will 6/19 (date unrecorded — propagation gap, see CLEARED section above).
- **Next mechanical decision pile: Jun 30 expiry** — KRE $63P/$65P/$67P + IWM $250P. All deep OTM at current tape; default let-expire unless tape breaks. Then Jul-17 (WAL $65P / FLG $13P / ZION $57.5P).
- **OZK positions are in `../OZK/POSITIONS.md`** (peer agent).
- **FORGE/STATUS.md staleness** — Mar 25, 8+ weeks behind broker. Same broker data should refresh FORGE's current-positions table (out of REGINALD scope).

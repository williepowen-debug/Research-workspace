# REGINALD — Thesis Positions

**Updated:** 2026-06-19 (Jun 18 expiry cluster CLEARED — all closed out or expired worthless per Will confirm 6/19; OWL/SOFI Jun-05 also expired). Prior refresh 2026-05-21 (May 15 cluster cleared), 2026-05-08 from broker (typed list).

> ⚠️ **STALE — this file predates the Jun-30 expiry (last real update 2026-06-19). The Jun-30 cluster below (KRE $63P/$65P/$67P + IWM $250P) LAPSED 2026-06-30 (~2 weeks ago); all were deep-OTM at expiry, presumed expired worthless, but execution path is UNCONFIRMED — off-repo/broker truth (rule #4). Flagged ⚠️ inline; NOT moved to CLEARED pending a broker refresh.** A broker refresh is owed before any 7/21 WAL/OZK fire decision (flagged 7/9 + reconfirmed 2026-07-10 audit).

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
| WAL | $67.5P | Sep-18-2026 | core REINFORCED-HOLD (catches Q2 print — Jul 21 AMC, confirmed 7/9, was ~Jul 30 est) |
| WAL | $70P | Sep-18-2026 | core REINFORCED-HOLD |
| KRE | $63P | Jun-30-2026 | ⚠️ EXPIRED 6/30 (deep-OTM ~$75 tape, presumed worthless; broker-confirm pending) |
| KRE | $65P | Jun-30-2026 | ⚠️ EXPIRED 6/30 (deep-OTM, presumed worthless; broker-confirm pending) |
| KRE | $67P | Jun-30-2026 | ⚠️ EXPIRED 6/30 (deep-OTM, presumed worthless; broker-confirm pending) |
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
| IWM | $250P | Jun-30-2026 | ⚠️ EXPIRED 6/30 (deep-OTM ~$296 tape, presumed worthless; broker-confirm pending). [Was correctly a live Jun-30 position — the 6/19 note fixed a prior Jun-18 mis-record; it has since lapsed.] |

---

## Key Context

- **WAL** now 3 positions across 2 expiries (Jul-17 $65P / Sep-18 $67.5P + $70P) — Jun-18 cluster (4 positions) cleared 6/18. Sep $77.5P… *(note: $77.5P was Jun-18, now expired — Sep tenor holds $67.5P/$70P)*. Sep $67.5P/$70P are core REINFORCED-HOLD per v2.2 deltas and **catch the WAL Q2 print — CORRECTED 2026-07-09: confirmed Jul 21 AMC (was ~Jul 30 est)**. ⚠️ **The Jul-17 $65P no longer catches the print either way** (was framed 6/26 as a 1-day-buffer catch of an assumed ~Jul-16 date; the confirmed Jul-21 date means Jul-17 now lapses BEFORE the print, same as it would have under the old ~Jul-30 estimate) — flagged for TERRY/PROME, not actioned here (no trade recs; verify against live broker book).
- **KRE** — 7 positions across 4 expiries ($60-$67, Jun-30 / Aug-21 / Sep-30 / Dec-18). Tape $71.72 (6/18) above all strikes (deep OTM) — tail-risk insurance, not directional.
- **No current EGBN / HYG / ARES / SSB positions.** EGBN/HYG/ARES cleared at Jun-18; SSB $90P was a real position, sold/closed per Will 6/19 (date unrecorded — propagation gap, see CLEARED section above).
- **~~Next mechanical decision pile: Jun 30 expiry~~ — PASSED 6/30** (KRE $63P/$65P/$67P + IWM $250P all deep-OTM, presumed expired worthless; broker-confirm pending). **Next live pile: Jul-17 expiry** — WAL $65P / FLG $13P / ZION $57.5P (Jul-17 lapses BEFORE the confirmed Jul-21 WAL Q2 AMC print — the $65P no longer catches it; verify vs live broker book before any fire).
- **OZK positions are in `../OZK/POSITIONS.md`** (peer agent).
- **FORGE/STATUS.md staleness** — Mar 25, 8+ weeks behind broker. Same broker data should refresh FORGE's current-positions table (out of REGINALD scope).

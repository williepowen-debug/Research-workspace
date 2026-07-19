# REGINALD — Thesis Positions

**Updated:** 2026-07-18 (RECONCILED to the `FORGE/STATUS.md` 2026-07-16 ~10:09 ET broker reconcile — Will's Fidelity+Robinhood export; absorbed strikes/expiries/**quantities** that this file had never carried, cleared the Jun-30 cluster, moved the Jul-17 legs to LAPSED). Prior: 2026-06-19 (Jun 18 cluster cleared), 2026-05-21, 2026-05-08 from broker (typed list).

> ⚠️ **Broker-truth caveat (rule #4):** the structural data below (strikes/expiries/quantities) is now current to the **7/16 FORGE broker reconcile** — the last real broker export. Two things remain owed from Will before any 7/21 fire: (a) confirmation of the **7/17 expiry execution** (WAL $65P / ZION $57.5P / FLG $13P — all deep-OTM at 7/17 tape, presumed expired worthless, moved to LAPSED below); (b) a **fresh broker export** capturing any intra-week (7/16→7/21) change. Marks/P&L go stale immediately — do NOT cite from here; strikes/expiries/quantities are structural and hold until a trade fires.

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

## Bank Puts (LIVE) — reconciled to FORGE 7/16 broker export

| Ticker | Strike | Expiry | Qty | Notes |
|---|---|---|---|---|
| WAL | $67.5P | Sep-18-2026 | 1 | core REINFORCED-HOLD — **catches the 7/21 AMC Q2 print** |
| WAL | $70P | Sep-18-2026 | 1 | core REINFORCED-HOLD — catches the 7/21 print |
| KRE | $60P | Aug-21-2026 | 3 | tail-risk insurance (deep-OTM vs ~$77 tape) |
| KRE | $60P | Sep-30-2026 | 2 | |
| KRE | $60P | Dec-18-2026 | 5 | (2 + 3 margin) — Dec-18 trimmed 7→5 per 7/16 reconcile |
| HBAN | $16P | Oct-16-2026 | 2 | ⚡ **EXIT-thesis dust** (Will ruled 7/18) — $20 residual, rides to expiry, do NOT re-enter; trimmed 4→2 per 7/16 reconcile |

## Credit / Convergence (LIVE)

| Ticker | Strike | Expiry | Qty | Notes |
|---|---|---|---|---|
| APO | $95P | Dec-18-2026 | 1 | longer-dated PC short (BROCK thesis vehicle) |

*OZK puts are peer-owned → `../OZK/POSITIONS.md` (FORGE 7/16 shows OZK Aug-21 $45P ×4 + $42.5P ×1 as the live 7/21-print-catchers; the Jul-17 $42.5P ×2 lapsed). IWM/macro options (IWM $292P Jul-17 lapsed, KRE $25P Jan-2027 lottery) live in `FORGE/STATUS.md`, not thesis-scope.*

## ✅ LAPSED — Jul-17-2026 expiry (all deep-OTM at 7/17 tape; execution-confirm owed from Will, outcome not in doubt)

| Ticker | Strike | Expiry | Qty | 7/17 tape | Note |
|---|---|---|---|---|---|
| WAL | $65P | Jul-17-2026 | 1 | $82.30 | lapsed OTM — died 2 trading days BEFORE the 7/21 AMC print (never caught it) |
| ZION | $57.5P | Jul-17-2026 | 1 | $72.27 | lapsed OTM |
| FLG | $13P | Jul-17-2026 | 3 | $14.90 | lapsed OTM |

*(IWM $292P Jul-17 ×1 — Will macro, FORGE-tracked — also lapsed OTM at ~$294. OZK $42.5P Jul-17 ×2 lapsed — peer book.)*

## ✅ CLEARED — Jun-30-2026 expiry (confirmed OFF the book per FORGE 7/16 reconcile)

Prior ⚠️-flagged Jun-30 cluster now confirmed expired worthless (absent from the 7/16 broker export): **KRE $63P/$65P/$67P** (deep-OTM ~$75 tape) + **IWM $250P** (deep-OTM ~$296). No longer pending — the 7/16 reconcile is the confirmation the 6/19-vintage file was waiting on.

---

## Key Context

- **WAL** — the live thesis core is **Sep-18 $67.5P ×1 + $70P ×1** (REINFORCED-HOLD per v2.2 deltas); these are the tenor that **catches the 7/21 AMC Q2 print**. The Jul-17 $65P (lapsed OTM 7/17) never caught the print — Jul-17 died 2 trading days before the AMC release. Jun-18 cluster (incl. $77.5P/$85P) cleared 6/18.
- **KRE** — live tail is **10× $60P** across 3 expiries (Aug-21 ×3 / Sep-30 ×2 / Dec-18 ×5); the Jun-30 $63/65/67P cluster expired worthless (confirmed off-book 7/16). Deep-OTM vs ~$77 tape — tail-risk insurance, not directional.
- **HBAN** — $16P Oct-16 ×2 is **EXIT-thesis dust** (Will ruled 7/18; ride to expiry, no re-entry).
- **No current EGBN / HYG / ARES / SSB / FITB positions.** EGBN/HYG/ARES cleared at Jun-18; SSB $90P was a real position sold/closed per Will 6/19 (unrecorded-exit propagation gap, see CLEARED section).
- **Next mechanical pile: the 7/21 WAL+OZK double-print** — no Jul-17 leg survives into it; the print-catchers are the WAL Sep-18s (+ peer OZK Aug-21s). Any fire-time reshape arithmetic rebuilds from a fresh broker export (rule #4) — the frozen grading frames govern the READ regardless.
- **OZK positions are in `../OZK/POSITIONS.md`** (peer agent); macro/non-thesis options in `FORGE/STATUS.md`.
- **FORGE/STATUS.md** — reconciled 7/16 (this file now mirrors it); prior "Mar 25 stale" note retired.

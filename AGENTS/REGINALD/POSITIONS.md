# REGINALD — Thesis Positions

**Updated:** 2026-07-20 (FOLDED the fresh `FORGE/STATUS.md` **7/20 broker export** — PROME reconcile 7/16→7/20, commit `b7c26f21`: added the NEW Robinhood **WAL $77.5P Aug-21 ×1** [nearest-money print exposure], confirmed the Jul-17 dust expired off + cash flat = NO-ADD held + core Fidelity book position-for-position unchanged). Prior: 2026-07-18 (reconciled to the 7/16 export — strikes/expiries/**quantities** absorbed, Jun-30 cluster cleared, Jul-17 legs → LAPSED); 2026-06-19, 2026-05-21, 2026-05-08.

> ⚠️ **Broker-truth caveat (rule #4):** the structural data below (strikes/expiries/quantities) is now current to the **7/20 FORGE broker export** — the freshest real export, which resolves both items formerly owed: (a) the **7/17 expiry** dust confirmed expired off (Fidelity WAL $65P / ZION $57.5P / FLG ×3 + Robinhood WAL $75P etc.); (b) the **intra-week (7/16→7/20) delta** — one net change: RH WAL $77.5P Aug-21 ×1 added; cash ~flat (+$7.59) = no other fills; core book unchanged. Marks/P&L go stale immediately — do NOT cite from here; strikes/expiries/quantities are structural and hold until a trade fires.
>
> ✅ **Independently corroborated 2026-07-18 vs TERRY's position snapshot** (`AGENTS/TERRY/STATUS.md`, from Will's live broker screenshots **7/17 ~12:30 ET — one day newer** than the 7/16 FORGE reconcile): every REGINALD-scope leg matches on strike/expiry/qty — WAL Sep-18 70P×1 + 67.5P×1 · KRE 60P ×10 · HBAN 16P Oct-16 ×2 · APO 95P Dec-18 ×1 (peer OZK Aug-21 45P×4 + 42.5P×1 also confirmed). The Jul-17 thesis legs are absent from TERRY's main-book table (confirms LAPSED). Structural book verified; only the marks differ (TERRY carries live 7/17 marks, now stale).

**Scope:** Thesis-relevant only — bank puts + credit/convergence. OZK lives in `../OZK/POSITIONS.md` (peer agent). **WAL lives in `../WAL/POSITIONS.md` (peer agent since 7/25 — REGINALD no longer owns WAL puts; the 3 legs [$77.5P Aug-21, $67.5P + $70P Sep-18] moved at the split).** Stocks, macro options (TLT/VIX/USO/XLE), and non-thesis (AAPL/APD/AAL/CCL/CF/DIS/KELYA/FXY/SLV/TBT) live in `FORGE/STATUS.md`.

> ## ⏳ PRE-REGISTERED EXPIRY — Fri 2026-08-21 OPEX (written 8/20 12:02 ET, BEFORE the event)
>
> **Live REGINALD leg into tomorrow's monthly OPEX: `KRE $60P ×3`.** KRE **$74.62** [8/20 12:02 ET, live] — the strike is **19.6% below spot with one session left.** It expires worthless barring a one-day crash larger than any in the series I track. **No decision, no action, nothing owed to anyone.**
>
> ⚠️ **This block exists because the DECISION being trivial is exactly when the RECORD goes missing.** `LESSONS.md` carries two instances of the same class — **SSB $90P** and **KRE $70P**, both real positions whose exits never propagated to this ledger and which then lingered in dashboards for weeks as phantoms. Both were also "obvious." **Pre-registering the outcome the day before makes the write-back a checklist item instead of an act of memory.**
>
> **NEXT SESSION (8/21 or first session after): mark `KRE $60P Aug-21 ×3` LAPSED, move it to the cleared set, and confirm it is absent from the next FORGE broker export.** Remaining KRE tail after it goes: **7× $60P** (Sep-30 ×2 + Dec-18 ×5) — ⚠️ update the "10× $60P across 3 expiries" line below, which will be wrong the moment this expires.
>
> *Peer legs at the same expiry, flagged not managed:* **OZK `$45P ×4` + `$42.5P ×1`** are **`../OZK/`-owned** (OZK $49.16 → −8.5% / −13.5% OTM). **I do not touch them**; noted so tomorrow's sweep does not mistake peer legs for mine.

⚠️ **THIS FILE IS CANONICAL for strikes/expiries.** STATUS.md / CALENDAR.md must POINT here, not re-list — re-listing is how the 6/19 desync happened (SSB $90P real-but-sold/unrecorded, IWM $250P/$257P strike+expiry error, 4 missing names; see LESSONS). Before any position task: **grep this file first**, never trust a dashboard cluster list.

✅ **Contract quantities ARE now carried in this file** (absorbed at the 7/16 FORGE reconcile; re-confirmed against the 7/20 export — see below). *(This line replaced the obsolete "quantities not in this rewrite / FORGE Mar-25 stale" paragraph, which contradicted the rewrite — cleared 7/20 per PROME fire-drill nit.)* **Cost-basis/P&L: confirm with Will, not from this file** (per [[feedback_position_cost_basis_not_authoritative]]).

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

> ⚠️ **CORRECTION 2026-08-13 (book-vs-thesis reconciliation, Will-ruled slate item #1).** Two rows below carried **false "trimmed" notes** for four weeks. **Neither trim happened.** Both were unit-mismatch artifacts of the 7/16 reconcile — a count of **rows** written into a sentence about a count of **contracts** and labelled as a size decision. **Root rule #7 ("trimming = thesis broken") was NEVER triggered on KRE or HBAN**, and the missing rationale was missing because there was no decision to record. Root cause: the 6/19-vintage ledger self-declared CANONICAL while recording **zero quantities**, so a row-count stood in for a contract-count. **Quantities below are unchanged and broker-sourced; only the false notes are corrected.** Full trace → `reports/2026-08-13_book-vs-thesis-reconciliation.md` §5.


| Ticker | Strike | Expiry | Qty | Notes |
|---|---|---|---|---|
| KRE | $60P | **Aug-21-2026** | 3 | tail-risk insurance. ⏳ **EXPIRES TOMORROW (Fri 8/21 OPEX). PRE-REGISTERED 8/20 12:02 ET: expiring WORTHLESS, no action.** KRE **$74.62** live → strike is **−19.6%** away; it needs a **19.6% one-day crash** to reach $60. Decision-free — **not a trim, not a roll, no rule-#7 read** (root rule #7 governs a thesis judgement; this is arithmetic). **NEXT SESSION: mark LAPSED and move to the cleared set — do not let the exit go unrecorded.** |
| KRE | $60P | Sep-30-2026 | 2 | |
| KRE | $60P | Dec-18-2026 | 5 | (2 + 3 margin) — ⚠️ **CORRECTED 2026-08-13: NO TRIM EVER HAPPENED.** Superseded text read *"Dec-18 trimmed 7→5 per 7/16 reconcile"* — that compared **7 KRE ROWS across ALL FOUR expiries** (three of them already expired) in the pre-reconcile file `f74117049`, which had **no quantity column at all**, against **5 CONTRACTS on ONE expiry**. Rows vs contracts. **Root rule #7 was never triggered; there was no size decision to record.** |
| HBAN | $16P | Oct-16-2026 | 2 | ⚡ **EXIT-thesis dust** (Will ruled 7/18) — $20 residual, rides to expiry, do NOT re-enter. ⚠️ **CORRECTED 2026-08-13: NO TRIM.** Superseded text read *"trimmed 4→2 per 7/16 reconcile"*; the **"4" appears nowhere in this ledger at any vintage**, and the recorded quantity went **1 un-quantified row → 2 contracts**, i.e. UP. Same unit-mismatch class as the KRE row above. |

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

- **WAL** — **legs moved to `../WAL/POSITIONS.md` at the 7/25 promotion split (canonical there; REGINALD no longer owns WAL puts).** At split time: Sep-18 $67.5P ×1 + $70P ×1 core + Robinhood $77.5P Aug-21 ×1 — pointer-only here, last verified 2026-07-25; do not re-list figures (seam rule).
- **KRE** — live tail is **10× $60P** across 3 expiries (Aug-21 ×3 / Sep-30 ×2 / Dec-18 ×5); the Jun-30 $63/65/67P cluster expired worthless (confirmed off-book 7/16). Deep-OTM vs ~$77 tape — tail-risk insurance, not directional.
- **HBAN** — $16P Oct-16 ×2 is **EXIT-thesis dust** (Will ruled 7/18; ride to expiry, no re-entry).
- **No current EGBN / HYG / ARES / SSB / FITB positions.** EGBN/HYG/ARES cleared at Jun-18; SSB $90P was a real position sold/closed per Will 6/19 (unrecorded-exit propagation gap, see CLEARED section).
- **The 7/21 WAL+OZK double-print RESOLVED** (both graded off frozen frames; WAL NOT-surprise-tier). WAL position management now rides with the WAL agent + TERRY; REGINALD's next mechanical pile = KRE Aug-21 ×3 + peer-print season.
- **OZK positions → `../OZK/POSITIONS.md`; WAL positions → `../WAL/POSITIONS.md`** (peer agents); macro/non-thesis options in `FORGE/STATUS.md`.
- **FORGE/STATUS.md** — reconciled 7/16 (this file now mirrors it); prior "Mar 25 stale" note retired.

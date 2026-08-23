# REGINALD — Thesis Positions

**Updated:** **2026-08-23 Sun (OPEX write-back — `KRE $60P Aug-21 ×3` marked LAPSED off the 8/21 close; the pre-registered outcome landed exactly as written and the derived `10×` line is corrected to `7×`).** ⚠️ **Structural data still current to the 7/20 FORGE broker export — this write-back is a REGISTERED EXPIRY, not a new export.** The absence-confirm at the next broker export is still owed. Prior: 2026-07-20 (FOLDED the fresh `FORGE/STATUS.md` **7/20 broker export** — PROME reconcile 7/16→7/20, commit `b7c26f21`: added the NEW Robinhood **WAL $77.5P Aug-21 ×1** [nearest-money print exposure], confirmed the Jul-17 dust expired off + cash flat = NO-ADD held + core Fidelity book position-for-position unchanged). Prior: 2026-07-18 (reconciled to the 7/16 export — strikes/expiries/**quantities** absorbed, Jun-30 cluster cleared, Jul-17 legs → LAPSED); 2026-06-19, 2026-05-21, 2026-05-08.

> ⚠️ **Broker-truth caveat (rule #4):** the structural data below (strikes/expiries/quantities) is now current to the **7/20 FORGE broker export** — the freshest real export, which resolves both items formerly owed: (a) the **7/17 expiry** dust confirmed expired off (Fidelity WAL $65P / ZION $57.5P / FLG ×3 + Robinhood WAL $75P etc.); (b) the **intra-week (7/16→7/20) delta** — one net change: RH WAL $77.5P Aug-21 ×1 added; cash ~flat (+$7.59) = no other fills; core book unchanged. Marks/P&L go stale immediately — do NOT cite from here; strikes/expiries/quantities are structural and hold until a trade fires.
>
> ✅ **Independently corroborated 2026-07-18 vs TERRY's position snapshot** (`AGENTS/TERRY/STATUS.md`, from Will's live broker screenshots **7/17 ~12:30 ET — one day newer** than the 7/16 FORGE reconcile): every REGINALD-scope leg matches on strike/expiry/qty — WAL Sep-18 70P×1 + 67.5P×1 · KRE 60P ×10 · HBAN 16P Oct-16 ×2 · APO 95P Dec-18 ×1 (peer OZK Aug-21 45P×4 + 42.5P×1 also confirmed). The Jul-17 thesis legs are absent from TERRY's main-book table (confirms LAPSED). Structural book verified; only the marks differ (TERRY carries live 7/17 marks, now stale).

**Scope:** Thesis-relevant only — bank puts + credit/convergence. OZK lives in `../OZK/POSITIONS.md` (peer agent). **WAL lives in `../WAL/POSITIONS.md` (peer agent since 7/25 — REGINALD no longer owns WAL puts; the 3 legs [$77.5P Aug-21, $67.5P + $70P Sep-18] moved at the split).** Stocks, macro options (TLT/VIX/USO/XLE), and non-thesis (AAPL/APD/AAL/CCL/CF/DIS/KELYA/FXY/SLV/TBT) live in `FORGE/STATUS.md`.

> ## ✅ RESOLVED EXPIRY — Fri 2026-08-21 OPEX (**pre-registered 8/20 12:02 ET; graded 8/23 off the 8/21 close**)
>
> **`KRE $60P Aug-21 ×3` — LAPSED WORTHLESS.** KRE closed **$74.86 [Fri 8/21 close, `scripts/market.py` → Yahoo `KRE`, +0.20%]**; the $60 strike finished **−19.9% out of the money**. Graded against the frozen pre-registration, not re-argued: the 8/20 block said *"expiring worthless, no action"* at $74.62 / −19.6%, and the outcome matched. **Decision-free throughout — not a trim, not a roll, no root-rule-#7 read.**
>
> ★ **The pre-registration did the job it was built for.** The 8/20 block existed because `LESSONS.md` carries two same-class phantoms (**SSB $90P**, **KRE $70P**) — real positions whose exits never reached this ledger. This exit reached it on the **first session after** the event because the write-back had already been reduced to a checklist item. `[[finding_record_of_an_action_is_not_the_action]]` — the record now exists because it was scheduled, not remembered.
>
> ⚠️ **STILL OWED, and it is not this write-back:** *confirm the leg is ABSENT from the next FORGE broker export.* Position truth is off-repo (root rule #4); an expiry I graded off the tape is a **high-confidence inference**, not a broker confirmation. Do not close this line until an export shows it gone.
>
> **Derived-line correction executed this session:** KRE tail **10× → 7× $60P**, across **2** expiries not 3 (Sep-30 ×2 + Dec-18 ×5). The 8/20 block named this line in advance as the one that would go stale on expiry; it did, and it is fixed below.
>
> *Peer legs at the same expiry, NOT managed here:* **OZK `$45P ×4` + `$42.5P ×1`** are **`../OZK/`-owned** (OZK closed **$49.42 [8/21]** → the $45 strike finished −8.9% OTM, the $42.5 −14.0%). **I did not touch them and I do not grade them** — `../OZK/` owns that write-back and it is flagged, not assumed.

---

## Bank Puts (LIVE) — reconciled to FORGE 7/16 broker export

> ⚠️ **CORRECTION 2026-08-13 (book-vs-thesis reconciliation, Will-ruled slate item #1).** Two rows below carried **false "trimmed" notes** for four weeks. **Neither trim happened.** Both were unit-mismatch artifacts of the 7/16 reconcile — a count of **rows** written into a sentence about a count of **contracts** and labelled as a size decision. **Root rule #7 ("trimming = thesis broken") was NEVER triggered on KRE or HBAN**, and the missing rationale was missing because there was no decision to record. Root cause: the 6/19-vintage ledger self-declared CANONICAL while recording **zero quantities**, so a row-count stood in for a contract-count. **Quantities below are unchanged and broker-sourced; only the false notes are corrected.** Full trace → `reports/2026-08-13_book-vs-thesis-reconciliation.md` §5.


| Ticker | Strike | Expiry | Qty | Notes |
|---|---|---|---|---|
| KRE | $60P | Sep-30-2026 | 2 | |
| KRE | $60P | Dec-18-2026 | 5 | (2 + 3 margin) — ⚠️ **CORRECTED 2026-08-13: NO TRIM EVER HAPPENED.** Superseded text read *"Dec-18 trimmed 7→5 per 7/16 reconcile"* — that compared **7 KRE ROWS across ALL FOUR expiries** (three of them already expired) in the pre-reconcile file `f74117049`, which had **no quantity column at all**, against **5 CONTRACTS on ONE expiry**. Rows vs contracts. **Root rule #7 was never triggered; there was no size decision to record.** |
| HBAN | $16P | Oct-16-2026 | 2 | ⚡ **EXIT-thesis dust** (Will ruled 7/18) — $20 residual, rides to expiry, do NOT re-enter. ⚠️ **CORRECTED 2026-08-13: NO TRIM.** Superseded text read *"trimmed 4→2 per 7/16 reconcile"*; the **"4" appears nowhere in this ledger at any vintage**, and the recorded quantity went **1 un-quantified row → 2 contracts**, i.e. UP. Same unit-mismatch class as the KRE row above. |

## Credit / Convergence (LIVE)

| Ticker | Strike | Expiry | Qty | Notes |
|---|---|---|---|---|
| APO | $95P | Dec-18-2026 | 1 | longer-dated PC short (BROCK thesis vehicle) |

*OZK puts are peer-owned → `../OZK/POSITIONS.md` (FORGE 7/16 shows OZK Aug-21 $45P ×4 + $42.5P ×1 as the live 7/21-print-catchers; the Jul-17 $42.5P ×2 lapsed). IWM/macro options (IWM $292P Jul-17 lapsed, KRE $25P Jan-2027 lottery) live in `FORGE/STATUS.md`, not thesis-scope.*

## ✅ LAPSED — Aug-21-2026 monthly OPEX (pre-registered 8/20, graded 8/23 off the 8/21 close)

| Ticker | Strike | Expiry | Qty | 8/21 close | Note |
|---|---|---|---|---|---|
| KRE | $60P | Aug-21-2026 | 3 | **$74.86** | lapsed worthless, **−19.9% OTM**. Outcome pre-registered 8/20 12:02 ET at $74.62 / −19.6% and matched. Decision-free; no rule-#7 read. ⚠️ **Broker-export absence-confirm still owed** (rule #4 — graded off the tape, not off an export). |

*(Peer legs same expiry — **OZK $45P ×4 + $42.5P ×1**, OZK closed $49.42 — are `../OZK/`-owned and deliberately NOT graded here.)*

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
- **KRE** — live tail is **7× $60P** across **2** expiries (Sep-30 ×2 / Dec-18 ×5). *(Was `10× across 3` until the **Aug-21 ×3 lapsed worthless 8/21** — corrected 8/23, the correction having been named in advance by the 8/20 pre-registration.)* The Jun-30 $63/65/67P cluster expired worthless (confirmed off-book 7/16). Deep-OTM vs a **$74.86 [8/21 close]** tape — **tail-risk insurance, not directional**; nearest strike is now 19.9% away with the first expiry 5-6 weeks out.
- **HBAN** — $16P Oct-16 ×2 is **EXIT-thesis dust** (Will ruled 7/18; ride to expiry, no re-entry).
- **No current EGBN / HYG / ARES / SSB / FITB positions.** EGBN/HYG/ARES cleared at Jun-18; SSB $90P was a real position sold/closed per Will 6/19 (unrecorded-exit propagation gap, see CLEARED section).
- **The 7/21 WAL+OZK double-print RESOLVED** (both graded off frozen frames; WAL NOT-surprise-tier). WAL position management now rides with the WAL agent + TERRY. **The Aug-21 ×3 pile is CLEARED (8/21, worthless).** ⚠️ **REGINALD's next mechanical pile = `KRE $60P Sep-30-2026 ×2`** — a **month-end**, not a third-Friday OPEX, so it will NOT surface on an options-expiry sweep keyed to monthly OPEX. Named here so the next session inherits it rather than re-derives it.
- **OZK positions → `../OZK/POSITIONS.md`; WAL positions → `../WAL/POSITIONS.md`** (peer agents); macro/non-thesis options in `FORGE/STATUS.md`.
- **FORGE/STATUS.md** — reconciled 7/16 (this file now mirrors it); prior "Mar 25 stale" note retired.

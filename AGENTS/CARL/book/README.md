# CARL PAPER SLEEVE — Phase 1

**Status:** ✅ **LIVE 2026-07-24 (Will-approved). NO CAPITAL. Nothing here is a real position.**
**Rules authority:** `AGENTS/TERRY/PAPER_BOOK_DESIGN.md` — TERRY owns the paper-book discipline; this sleeve adopts it.
**Design:** `AGENTS/CARL/thesis/CARL_BOOK_DESIGN.md` (v0.1). **Ledger:** `PAPER_SLEEVE.tsv`.

---

## ⚠️ Why this is a SEPARATE ledger and not rows inside TERRY's `PAPER_BOOK.tsv`

My design doc proposed "a sleeve in TERRY's existing book." **Reading TERRY's spec showed that's the wrong shape, so I built it adjacent instead** — flagging the change rather than executing the literal instruction:

- **They measure different things.** TERRY's paper book measures **card quality** — options fire-cards, would-fire triggers, $500 defined-risk premium, chain quotes, `will_decision` refusal-calibration. This sleeve measures **thesis-expression quality** — equity relative-value against a benchmark, no options, no cards, no trigger. Blending them corrupts both records, and TERRY's own spec already splits lanes (`lane` column, Sharpening 2) precisely to stop that.
- **File ownership.** Root rule 2 — I don't edit another agent's files. TERRY's ledger is TERRY's.
- **TERRY remains the rules authority.** If TERRY's fill or marking rules change, this sleeve follows.

**Merge path if it ever makes sense:** both ledgers carry `pnl_$`/`status`/`lane`, so a combined Brier/calibration pass can union them at scoring time without either book having to host the other's schema.

---

## Rules adopted verbatim from TERRY

| Rule | Applied here |
|---|---|
| **Never fill at mid** | Buys fill at ask, sells at bid. Equities have no chain snapshot, so a **conservative 15bps slippage** is applied *against* the position (up for longs, down for shorts) and stated in `entry_basis`. |
| **Auditable `entry_basis`** | Every fill records source, price, timestamp, and the slippage applied. |
| **Survivorship — never delete a losing row** | Enforced by convention + the header banner. A sleeve that quietly drops losers is worse than no sleeve. |
| **Staleness stamps** | `mark_asof` on every mark. CARL is spawned on-demand, so marks are **as-of-last-spawn** — the curve is lumpy by construction and must be labelled so, never presented as continuous. |
| **N ≥ 10 gate** | **No scoring, and no decision acts on this record, until N ≥ 10 CLOSED positions.** Until then every row carries `notes = "N-too-small"`. |

## Rules specific to this sleeve

- **`pred_id` is the entry gate.** Every row must name a registered, OPEN, **reachable** prediction. No prediction ⇒ no position. This is the mechanical form of `CARL_BOOK_DESIGN.md` §4, and it is what makes a thesis-vibes trade impossible.
- **Fixed notional, deliberately.** $3,000 per position / $1,000 per basket leg. Sizing is held constant so the sleeve tests **selection**, not sizing. (TERRY's $500/card is a *premium-at-risk* cap for options — not transferable to unlevered equity.)
- **Benchmark = SPX.** These are *relative* claims; absolute P&L on an unlevered equity book would mostly measure the index.
- **CARL never sizes or constructs live.** If anything here ever graduates to capital, TERRY constructs and Will approves.

---

## Opening positions — chosen to be DIAGNOSTIC, not directional

| ID | Position | What it tests |
|---|---|---|
| **PS-0001–0004** `PAIR-01` | **Short XLY $3,000 vs long DG/DLTR/WMT $1,000 each** | The core K-shape claim: the bottom-60% squeeze shows up as **down-tier substitution**, not aggregate weakness. Directly expresses CRL-27's cohort leg. |
| **PS-0005** | **Long AZO $3,000 — deliberately AGAINST the tape** | **The anomaly probe, and the most informative row in the sleeve.** AZO is −29.6% absolute / −44pp vs SPX, which *contradicts* the trade-down thesis (auto aftermarket should **win** a trade-down). But CARL already logged the May decline as **margin/LIFO-driven, not US-demand**, with domestic SSS **+4.1%** as a defensive counter-channel. **If that characterization is right this pays; if it's wrong, CARL learns its defensive read is broken.** Falsifies CARL rather than confirming it. |

**Invalidation on PS-0005 is written against the characterization, not the price:** *AZO reports domestic SSS < +1.0%* — i.e. demand, not margin, was the driver ⇒ CARL was wrong, close and log it.

### Logged NON-entry (TERRY's "capture the refusals" principle)
**The purest CRL-27 expression — short the consumer lenders (SYF/COF/ALLY) — is BLOCKED and deliberately not opened.** Those three are the *contested* names in `CARL_BOOK_DESIGN.md` §3, pending a split REGINALD has not agreed to. **Recording the non-entry because a blocked trade is data**: if that leg would have been the profitable one, the cost of the unresolved boundary is measurable.

---

## Marking cadence
Mark every OPEN row at CARL boot via `FORGE/tools/market-data/fetch.py`; update `mark` + `mark_asof`; flag any mark older than 5 business days as STALE. **Not yet automated** — a `sleeve_mark.py` helper is the obvious next build, deliberately deferred until the sleeve has proven it will be maintained.

## Graduation to capital
Per `CARL_BOOK_DESIGN.md` §6 — all four required over ≥2 quarters, and **#2 rides on PS-0005**:
1. Beats a naive short-XLY benchmark risk-adjusted.
2. **CARL correctly called ≥1 name against its own prior** (the AZO/ORLY anomaly).
3. Zero bias-tripwire events.
4. Brier score improved or held.

**Kill:** any bias-tripwire event surviving RED challenge, or a REGINALD boundary dispute Will adjudicates twice.

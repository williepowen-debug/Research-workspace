# Upgrade Card — VIOLET (read-only assessment, no agent files touched)

> 🗄 **ROUTED 2026-07-12 — CLOSED AS A QUEUE 2026-08-17 (self-audit F5 banner pass).** This card's findings were routed to the owner/FLEET_MAP when written; per-row states below are historical. Not maintained — current gaps live on the agent's FLEET_MAP row. Do not work rows from here without re-verifying at the agent.

**By:** DAEDALUS · **Date:** 2026-07-04 · **Class:** Market (volatility-regime; the modulation layer — dual-channel Path A/B; holds a LIVE trade book)
**Method:** `UPGRADE_PROTOCOL.md` (one section at a time) · graded vs `BLUEPRINTS/market-agent.md` · comprehension in `profiles/VIOLET.md`
**Verdict: L4 (conf H), 2-level under-rate corrected** (was L2 Conf-L). VIOLET is a **strong-quant** agent — conformant or exemplary on all 8 sections, with Convergence / Predictions / Quant-engine **exemplary** and Thesis-structure / Routing **exceeding** the blueprint. The 6/27 mechanical scan's "no BOTTOM LINE; exit-rules lack session counts" was **half false-negative** (PAT-024): the session-counts claim is factually wrong (3 N+session rules, one live-tally); only the BOTTOM LINE gap checks out. Every item below is an *added handle* or a *staleness refresh*, never a rewrite (PAT-015 floor-not-ceiling). **Nothing applied — this is the queue.**

> **Application gate:** all handle/hygiene edits touch VIOLET's files → gate on **permission + a fresh idle-check** (AUTHORITY). VIOLET committed 7/3, active — if live, route a **task-packet to `inbox/`** rather than editing. Re-read the live file (PAT-009) before any change.

---

| § | Blueprint section | VIOLET current state | Applies? | Gap type | Proposed minimal handle | Priority |
|---|---|---|---|---|---|---|
| 1 | **Thesis structure** | thesis/VIX_THESIS.md — **dual independent channels** (Path A credit-led / Path B concentration-unwind) each w/ transmission-stage diagram + "don't require A when B is firing" independence rule; orthogonal **4-layer confirmation stack** w/ explicit bypass | ✅ APPLIES | **exceeds** | None — dual-channel + 4-layer stack is above the OTTO stage table | 0 |
| 2 | **Convergence matrix** | STATUS 9-vector matrix; universal 5-pt PRESENT (CLAUDE.md:135-144); **script-verified 45-pt composite** (blueprint's named local scale) used as +Δ trend | ✅ APPLIES | conformant; **1 missing-handle** | Add a per-vector **`Independence` column** to the STATUS matrix (shared-antecedent flag — substance exists in prose "external legs at floor, internal at cycle highs"). *Add alongside; do NOT touch the 45-pt.* | **2** |
| 3 | **Thresholds** | banded regime rules (thesis + CALENDAR emoji-gates + `thresholds.py` BANDS); DIET/STRICT **conjunction** tiers; credit-gate coded in `fred_fetch.py` (matches STATUS live) | ✅ APPLIES | conformant (**scattered**) | None *required*. Substance is rich but split across thesis/CALENDAR/SIGNAL_INTAKE/boot-output — a "PRESENT-BUT-SCATTERED" note, not a floor gap. *Optional owner polish: one canonical durable-band table.* | 3 |
| 4 | **Invalidation / exit** | **3 N+session rules** — DIET stop (SKEW<140 sustained 4+td) · Regime-Shift stop (7-day contango) · Pred#6 (SKEW>150 4+td, **live tally 1/4**); channel-kill implicit via Path A/B independence; rich status vocab (PASSED/FAILED/PARTIAL/FALSIFIED) | ✅ APPLIES | conformant | None — the flagged "lacks session counts" gap is **factually wrong**. *Optional: name the bidirectional "cleanest flip each way" explicitly (currently implicit in Path A/B + RISK FACTORS).* | 3 |
| 5 | **Predictions** | 6 falsifiable predictions + scoring-rules key (thesis §PREDICTIONS); **3-axis confidence discipline** (Epistemic EMPIRICAL/ESTIMATE/ASSUMPTION + High/Med + Admiralty A1-F6) — VIOLET is the blueprint's **named confidence-tier source**; failure→thesis-revision loop working (CHANGELOG); 6 postmortems; 19-yr backtest | ✅ APPLIES | **exemplary substance / handles unconsolidated** | **(a)** thin **`PREDICTIONS.tsv`** that *indexes* the existing thesis table (do NOT flatten the 3-layer #/KB-VIO/framework numbering); **(b)** an `if-falsified ACTION` column (consequence lives in TRADE.md gates — surface it on the table). *Substance all present — this is handle consolidation.* | **2** |
| 6 | **Cross-agent routing** | CLAUDE.md:109-115 route-matrix (condition→target→priority); **NEXUS_BRIEF every closeout** w/ SENDING/WAITING-FOR tables (exceeds min); outbox 🔴-only | ✅ APPLIES | **exceeds** | None | 0 |
| 7 | **Standing disciplines** | mechanism-vs-thermometer (credit-gate mechanism vs VIX readout); Δ-discipline via matrix `Last Updated`; boot↔closeout symmetry (boot.py + NEXUS_BRIEF every closeout); MEMORY 18-takeaway learning loop | ✅ APPLIES | conformant | None *required*. *Optional: a standing EXPECTED_SIGNALS tracker (currently event-scoped via gates). Low value.* | 3 |
| 8 | **BOTTOM LINE** | STATUS ends w/ a changelog footer, not a labeled BOTTOM LINE; **REGIME STATUS block carries the substance** (domain-state synthesis + forward gates) unlabeled; STATUS 113 ln ≪ 250 | ✅ APPLIES | **missing-handle** | Add a labeled **`## BOTTOM LINE`** (2-4 sentences) distilling REGIME STATUS. Cheap. | **1** |

**Section tally:** §1 exceeds · §2 conformant (+1 missing-handle) · §3 conformant (scattered) · §4 conformant · §5 exemplary-substance (+handle consolidation) · §6 exceeds · §7 conformant · §8 missing-handle. **Zero missing-substance. Zero rewrites.** All gaps are added handles.

---

### Separately — the real L4→L5 work (hygiene / staleness, not section structure)
| Item | Why | Gap type | Effort |
|---|---|---|---|
| **§8 TRADE.md staleness MECHANISM unwired** | `ledger_staleness.py --trade` not in CLAUDE.md/boot.py; currency (`ok +0d`) sustained by *manual discipline only* = the single-point-of-failure the blueprint mechanism removes. **Wire two cwd-proof boot lines** (`... VIOLET --quiet` + `... VIOLET --trade --quiet`) | missing-handle (mechanism) | **S** |
| **2 dead CSVs silent-rot** — `workbook/hy_oas_fred.csv` + `combined_vix_credit.csv` (last row 4/09, zero refs, superseded by 6/23 fred_cache rewrite), un-bannered/un-archived | root-CLAUDE Data Hygiene: FROZEN banner or `git mv` to archive | hygiene | **S** |
| **3 dangling `archive/` refs** — README:27, CLAUDE:175, SIGNAL_INTAKE:133 point into a `VIOLET/archive/` dir **deleted fleet-wide** in public-prep (`1cb18fbc`/`7133b7d6`); targets gone repo-wide | boot/closeout friction; repoint or drop | hygiene | **S** |
| **VIX_THESIS.md append-on-top tail stale** — "Current status" tail (:406-436) stamped 6/10 (~24d) under a 7/2 header, cites superseded 6/10 marks | self sub-case PAT-032; move live tail to STATUS or restamp | owner staleness | **M (owner)** |
| **TRADE.md footer self-stamp** declares 7/1 while body has 7/2 content | `finding_selfstamp_estimate_drift` family; one-line footer bump | trivial | **S** |

---

## The queue
1. **FLEET_MAP / profile already reflect L4 (DAEDALUS's own files) — DONE 7/4** (corrected the L2→L4 false-negative; PAT-024). No concurrency risk.
2. **Batch 1 — quick handle-adds + hygiene (one CLAUDE.md/STATUS changelist):** §8 BOTTOM LINE label · §2 Independence column · `--trade`+workbook staleness boot lines · 2 dead-CSV disposition · 3 dangling-archive-ref fixes · TRADE.md footer bump. ✅ **ALL 6 ITEMS APPLIED 7/11** (`AGENTS/VIOLET/STATUS.md:119`, commit `fe966b48`). *(Closed 2026-07-12 per DAEDALUS self-sweep.)*
3. **Batch 2 — §5 predictions handle consolidation:** thin `PREDICTIONS.tsv` indexing the thesis table + `if-falsified ACTION` column. **M**, additive; preserve the 3-layer numbering. Owner-lane (touches thesis + workbook).
4. **Owner staleness — VIX_THESIS.md live-tail refresh** (move the 6/10 "Current status" tail to STATUS, or restamp). Owner closeout work; route, don't edit.
5. **Optional priority-3 refinements** (§3 canonical durable-band table · §4 explicit bidirectional-flip · §7 EXPECTED_SIGNALS tracker) — batch only if a VIOLET changelist is already open. Low value; substance already covered.

> **DO-NOT-TOUCH (comprehension preserved — full list in `profiles/VIOLET.md §5`):** the 45-pt composite (blueprint-endorsed local scale — 5-pt already added alongside, never flatten); SIGNAL_INTAKE.md kept ACTIVE THRESHOLDS (documented divergence from CARL); the three-way memory partition (MAINTENANCE structural / CHANGELOG analytical / SCRATCH ephemeral); CALENDAR↔CATALYSTS "human twin"; KB-VIO-### IDs (don't renumber) + KB Admiralty≠Epistemic axes; M1:M2 T-1 convention + `--allow-m1m2` gate + TICK/SETTLE basis; fred_fetch merge-on-write cache (don't glob); `final_5d_change`≠`20d slope`; episode-% must name its anchor; outbox 🔴-only by design. **A rich quant agent — do NOT impose skeleton scaffolding.**

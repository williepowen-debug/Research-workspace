# Agent Profile — LABOR

> ⚠️ **STALE 2026-07-12** — own named triggers FIRED: JOLTS 6/30 + NFP 7/2 resolved + 3 live sessions (7/6, 7/9, 7/10 incl. `PREDICTIONS_SCOREBOARD.md` build) unabsorbed. Refresh at 7/18 review.

**Built by:** DAEDALUS · **Date:** 2026-06-29 · **Comprehension method:** 1-reader live comprehension (workflow `firm7-profiles-cards`; documents the 6/28 firm-next7 adversarially-confirmed L4)
**Sources read:** CLAUDE.md, STATUS.md (255 ln), TRADE.md, NEXUS_BRIEF.md, LESSONS.md, workbook/{VX,KB,FLOW,PREDICTIONS,SCHEMA,EXPECTED_SIGNALS,FRAMEWORK_SUMMARY}, docket/CATALYSTS.tsv + git log / mtimes. SKIM-only: archive/, domain/sources/, sources/ (incl. .docx, March RP-LAB fulltexts), inbox/processed/, scripts/. · **Staleness:** refresh when the STATUS convergence matrix materially re-rates, when the Jun-30 JOLTS / Jul-2 NFP catalyst cluster resolves the thesis, or > 45 days.

> Durable understanding — section-tasks read THIS, not the raw (heavy) agent. Re-read the actual file before applying any change (PAT-009).

---

## 1. Identity
U.S. employment — layoffs, initial/continuing claims, NFP, U-3/6, JOLTS, WARN filings, Challenger, staffing (KELYA/KFRC/RHI/MAN), DOGE/federal, AI-displacement, temp/gig, geographic UR. **Class:** Market. **Transmission:** the **HEAD** of the chain — "employment is THE trigger." Sends to **CARL / REGINALD / HENRY / PROME / FORGE** (+ LIQUID/SAM in KB), consumes from **BROCK** (BDC→mid-market 1-2Q lead), **HENRY** (SPX→discretionary), **HAWK** (war→freeze), and the **WALTER** signal lane (`inbox/WALTER/`). **Cedes (one-source-of-truth):** consumer credit/spending→CARL, bank stress→REGINALD, market vol→HENRY, migration-driven labor *supply*→MARCO, foreclosure rate→CARL (LAB-04 reclassified), live position marks→FORGE. **Spawnable by:** PROME / Will. **What it's for:** "Has the *Hotel California* (low-fire/low-hire) labor market started actually shedding jobs — and where does the break transmit?"

## 2. File anatomy (where the richness lives) — HEAVY, STATUS-centric
| File | Holds | Richness? |
|---|---|---|
| STATUS.md (255 ln) | **The everything-file & canonical truth.** Regime header, CORE TENSION table, **16-vector convergence matrix (48/80)** + CROSS-DOMAIN CONTEXT (MARCO supply, *not* scored), SIGNAL DASHBOARD (~45 indicators, `[CONF]`/`[EST]` tagged), FED TRAP, DANGER WINDOW, PREDICTIONS table, EXIT RULES (Kill A/B), MONITORING CALENDAR, NEXT SESSION PICKUP (session log), BOTTOM LINE | live state (load-bearing) |
| CLAUDE.md (250) | Symmetric boot/closeout (B0-B6 / C1-C6), KEY THRESHOLDS table, matrix+exit specs, RESEARCH TOOLKIT (8 frameworks), cross-agent signal table | protocol + standing thresholds |
| workbook/PREDICTIONS.tsv (16 rows: **10 OPEN / 6 RESOLVED**) | LAB-xx ledger — conf/timeframe/outcome/notes. **The one LIVE workbook** = the real L2 logging home | live ledger |
| workbook/VX.tsv (76 rows) | banded vectors w/ Green/Yellow/Orange/Red cols. **FROZEN 2026-06-26 (banner).** Holds the durable bands | frozen-historical (bands live here) |
| workbook/KB.tsv (99 rows) | 13-col Admiralty-digraph evidence record. **FROZEN 2026-06-26** | frozen-historical |
| workbook/FLOW.tsv (14 rows) | transmission pathways, Speed/Status (LATENT/WARMING/ACTIVE/RESOLVED) — the contagion view. Refreshed 6/16 then **FROZEN 2026-06-26** | frozen (conceptually rich) |
| workbook/SCHEMA.tsv | KB column schema (Admiralty conf + EMPIRICAL/ESTIMATE/ASSUMPTION) | schema def |
| workbook/EXPECTED_SIGNALS.md (178) | durable banded interpretation tables (claims/NFP/JOLTS/cross-agent). **Feb-stale (v1.0, 2026-02-01)** w/ baked-in live values | stale durable-method |
| workbook/FRAMEWORK_SUMMARY.md (250) | Feb-11 continuing-claims + state-UI-exhaustion build doc; refs dead paths (`domain/workbook/`) | stale build record — SKIP |
| TRADE.md (153) | §1 14-row transmission signal index (T-01..T-14); §2 KELYA $7.5P Aug-21 (functionally dead); §3 forward catalyst playbook; §4 out-of-scope disclosure | trade truth + signal map |
| NEXUS_BRIEF.md (76) | VIEW/CALIBRATION/CROSS-DOMAIN/NEXT-DECISION/FORWARD-CATALYSTS, schema R3+amд7. **As-of Jun 16, NOT re-pinned at 6/26 closeout** | sync (stale) |
| LESSONS.md (31) | 5 numbered LABOR mistake-patterns (L-01..L-05); 3 promoted to auto-memory | learning |
| docket/CATALYSTS.tsv (9 rows) | 8-col forward catalyst **source of truth**, banded thresholds | forward state |
| scripts/ | boot.py orchestrator + labor_data.py (FRED sweep, fail-loud INCOMPLETE gate) + catalyst_countdown + predictions_due + warn_texas — SAM/BRENT parity | tooling (exceeds floor) |
| archive/, domain/sources/, sources/, inbox/processed/ | March RP-LAB fulltexts, .docx, STATUS archives, processed mail | SKIP |

## 3. Per-dimension local representation
| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| Thesis structure | STATUS CORE TENSION + FED TRAP + FLOW.tsv (frozen) + NEXUS_BRIEF | **"Hotel California"** (low-fire/low-hire → realization break); explicit **announcement/intent-layer vs realization-layer bifurcation**; stagflation Fed-trap; no version number | strong |
| Convergence / scoring | STATUS "CONVERGENCE MATRIX (16 LABOR-owned vectors)" | 16-vector, 5-pt emoji+number, **total 48/80** (right-sized from a presented 57/85); **Δ column** + separate CROSS-DOMAIN CONTEXT table that *excludes* sign-wrong supply-side signals | **exemplary** (sign-discipline) |
| Invalidation / exit | STATUS "EXIT RULES (Falsification)" | **Kill A** (NFP ≥+200K ×3 mo → live: 1 of 3, "live threat") / **Kill B** (Claims ≤185K ×5 clean sessions → "DEAD — path closed"); bull+bear; explicit session/month counts | strong |
| Thresholds | split across CLAUDE KEY THRESHOLDS (stale 213K) + FROZEN VX bands + TRADE §3 + CATALYSTS + Feb-stale EXPECTED_SIGNALS | banded GREEN/YELLOW/ORANGE/RED everywhere but **NO single living home** | **DEBT** (homeless bands) |
| Predictions | workbook/PREDICTIONS.tsv + STATUS PREDICTIONS table | LAB-xx, conf+timeframe+outcome+notes; **10 OPEN / 6 RESOLVED**; mechanism-vs-threshold discipline; explicit STATUS↔ledger reconcile rule (set Jun 16) | strong |
| Cross-agent routing | TRADE §1 (T-01..T-14) + CLAUDE cross-agent table + NEXUS_BRIEF SENDING/WAITING + outbox | condition→threshold→target→priority; head-of-chain transmission map | **exemplary** |

## 4. Deviations from standard (+ why)
- **Better-than-blueprint:** the **CROSS-DOMAIN CONTEXT** sign-check table (ICE/H-2A are MARCO labor-*supply*, explicitly NOT scored — supply cut pushes U-3 *down*, opposite of the demand-weakness thesis) is the single strongest local feature → codified in L-05 / auto-mem `[[finding_convergence_sign_check]]`. **TRADE §1** 14-row transmission index (T-01..T-14) is a full head-of-chain signal map. **boot.py** tooling (FRED sweep + catalyst countdown + predictions-due, fail-loud gate) exceeds the L2 floor.
- **Equivalent:** matrix uses a **Δ column** instead of the blueprint's "Upgrade Trigger" column — fine; upgrade triggers live in CATALYSTS + EXPECTED_SIGNALS instead. Convergence emoji folded into the Score cell ("5 🔴🔴") rather than a separate Status-emoji column.
- **DEBT (real):** (1) **durable threshold bands have no living home** — scattered across FROZEN VX (banner'd dead), Feb-stale EXPECTED_SIGNALS v1.0, CLAUDE KEY THRESHOLDS (stale 213K), TRADE §3, CATALYSTS — needs one canonical living surface. (2) **NEXUS_BRIEF As-of Jun 16, not re-pinned at the 6/26 closeout** (violates its own SPAWN-PROTOCOL write-back) → now points at a *past* (Jun-18) "next decision." (3) STATUS **255 ln, over its own 250 cap**. (4) STATUS **"Last Updated" header reads Jun 16 but the body carries a Jun-26 maintenance pass** — spine-date drift. (5) **2 unprocessed WALTER inbox items + no `board_log.tsv` + 2 undelivered outbox files** (LAB-04→CARL, WARN→NEXUS) = freshness/delivery debt.
- **False-negatives a mechanical scan would make (per grounding):** FROZEN VX/KB/FLOW *look* like "logging stopped → L2 fail," but freezing-with-banner is **correct** root-CLAUDE hygiene (STATUS is canonical) and **PREDICTIONS.tsv is kept LIVE** = the genuine L2 home. EXPECTED_SIGNALS being Feb-stale *looks* like dead method, but the bands persist (re-home, don't rebuild). FLEET_MAP itself earlier undercounted "2 pred resolved" → actually **6 RESOLVED** (corrected at the 6/28 grade).

## 5. Load-bearing context / DO NOT TOUCH
- **CROSS-DOMAIN CONTEXT separation** (MARCO supply-side ICE/H-2A explicitly OUT of the 48/80) — re-importing them = +9 phantom bearish points (L-05). The sign-check is the discipline; preserve it.
- **Kill A / Kill B** literal counts + live fired-state ("Kill B DEAD — path closed") and the **revised-series rule** (evaluate NFP Kill A on REVISED back-months, not first print — L-02). Don't soften either.
- **PREDICTIONS.tsv `Status` controlled vocab** — `predictions_due.py:132` EXACT-matches `Status==OPEN`; custom values (EFFECTIVE-MISS / RECLASSIFIED) **silently drop rows from the boot scan**. Keep terminal vocab `OPEN`/`RESOLVED`; put disposition in Notes (the verify-loop lesson, commit `94df30e7`).
- **FROZEN banners** on VX/KB/FLOW — do NOT "helpfully" refresh rows (L-04); STATUS is canonical. The bands inside frozen VX are the durable reference until re-homed.
- **LAB-xx ID format**; **LAB-04 KEPT OPEN deliberately** (out-of-domain, awaiting CARL pickup) — don't auto-resolve it.
- **docket/CATALYSTS.tsv = catalyst source of truth**; STATUS MONITORING CALENDAR is its *human twin* (must not diverge in event set).
- **TRADE.md does NOT duplicate live position state** — FORGE owns contracts/cost-basis/mark (`[[feedback_position_cost_basis_not_authoritative]]`). Don't add marks.
- **boot.py** `PYTHON=venv-or-system` fallback + **labor_data.py fail-loud INCOMPLETE gate** — don't revert to false-green.

## 6. Maturity snapshot
**L4 (conf H)** — head of the LABOR→CARL→REGINALD→HENRY chain; conformant/exemplary on 5-6 of 6 market dimensions. Per-section: Thesis **L4** · Convergence **L4** (exemplary sign-discipline) · Exit **L4** · Predictions **L4** (live ledger + 6 resolved) · Cross-routing **L4** · Thresholds **L3-and-slipping** (the homeless-bands debt is the one real drag). Below **L5** only on: (a) threshold-band re-homing, (b) NEXUS_BRIEF re-pin cadence, (c) clean-closeout hygiene (STATUS over cap + Jun-16/Jun-26 spine-date drift + no zero-flag bill). Work queue → `upgrades/LABOR_CARD.md` *(not yet created — to build)*. Classification per `FLEET_MAP.tsv` (L4 / H / ROSTER:active, dated 2026-06-28) — not restated here.

## 7. Open questions / comprehension gaps
- **Has LABOR run since 6/26?** No own-commit after `91ceedc4` (6/26); only PROME's 6/27 CLAUDE.md push-block flip touched the dir. So the **Jun-30 JOLTS-May + Jul-2 NFP-June** catalysts are now imminent/unprocessed — the graded *structure* is intact but the *data* may already be stale.
- **Where should re-homed bands live** — a revived EXPECTED_SIGNALS.md (BROCK pattern: durable, no live values) or a STATUS KEY THRESHOLDS block? (decision for the CARD).
- **Are the 2 undelivered outbox files actually delivered** out-of-band (HERMES deprecated), or stuck? Confirm CARL now owns the FL-foreclosure number (closes LAB-04).
- **Was FLOW.tsv frozen deliberately or as collateral?** It was refreshed 6/16 *then* frozen 6/26; FLOW is conceptually the contagion engine, and freezing it loses a live transmission view — verify intent vs the VX/KB freeze.

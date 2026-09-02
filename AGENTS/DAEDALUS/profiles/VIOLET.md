# Agent Profile — VIOLET

> ⚠️ **STALE — TRIGGER FIRED, unserviced (PR#5 2026-09-01):** VIX_THESIS v3.9→v4.0 re-mark 8/27 · body 7/22. Read the FLEET_MAP row (re-cut 2026-09-01) and `upgrades/PRODUCTION_REVIEW_2026-09-01.md` before this body. Refresh checkpoint: **2026-09-15**. *(Bannered by `scripts/profile_clock_check.py` + the PR#5 readers; a banner is a warning, not a fix — PAT-085.)*

## Δ 2026-08-17 — PR#4 (evidence: upgrades/PRODUCTION_REVIEW_2026-08-17_READER_REPORTS.md): BODY SUPERSEDED IN PART — STATUS 113→210 ln/46.4KB · matrix 9-vector/45-pt → 12-vector/55 · THESIS v3.9 (2 POV bumps) · BOTTOM LINE GONE ≥21d (§8 violation; own CLAUDE:45 write-back omits it) · TRADE ok-claim = ledger_staleness false-green (footer vintage unparsed) · CSV freeze UNRECORDED · missing: 8/04 four-mechanisms session, 8/10 forum registrations, CANARY_MAP.md, artifacts/. Own clock expired 8/18; full rebuild queued (desk was 7d dark at review — a rebuild then would capture a frozen desk).

> Δ **2026-07-22 PRODUCTION REVIEW — named trigger fired; REFRESH-AT-TOUCH.** Per-agent delta bullets + row re-grade banked in `upgrades/PRODUCTION_REVIEW_2026-07-22.md` (the delta store). Body below is prior-vintage — READ WITH THE DELTAS; full refresh executes at the next firming touch of this agent.

**Built by:** DAEDALUS · **Date:** 2026-07-04 · **Comprehension method:** Mode-A 4-reader fan-out (identity/state/routing · thesis/thresholds/exit · predictions/trade/research · quant-engine) → synthesis. First full comprehension (was mechanical-only Conf-L before this).
**Sources read:** CLAUDE.md, README.md, STATUS.md, NEXUS_BRIEF.md, SIGNAL_INTAKE.md, SCRATCH.md, MEMORY.md, MAINTENANCE.md, CALENDAR.md, TRADE.md, board_log.tsv, thesis/{VIX_THESIS.md,CHANGELOG.md}, workbook/{KB.tsv,SCHEMA.tsv,VX_DAILY,VIX_OPTIONS,COT_VIX,fred_cache/,CATALYSTS,FLOW}, scripts/ (all 10), research/ (45 files skim). **Staleness:** refresh when the L1–L4 signal-stack framing or the dual-channel (Path A/B) thesis materially re-marks, or > 45 days.

> Durable understanding — section-tasks read THIS, not the raw (heavy) agent. Re-read the actual file before applying any change (PAT-009).

---

## 1. Identity
Volatility-regime owner — VIX/VVIX/SKEW term-structure, credit→vol transmission, regime taxonomy (COMPLACENCY→CRASH), convexity pricing. **Class:** Market. **Transmission:** the **modulation layer** — `BROCK ↓ LIQUID ↓ VIOLET ↓ HENRY ↓ P&L` (Path A, credit-led) and a parallel `Macro ↓ HENRY ↓ VIOLET ↓ P&L` (Path B, concentration-unwind). SENDS to HENRY (vol catalyst), LIQUID/RED (term-structure flips); CONSUMES BROCK/LIQUID credit reads + HENRY macro + WALTER signal lane. **Holds a LIVE trade book** (`TRADE.md` — pre-registered fade/hedge frameworks with named gates + kill conditions). **Spawnable by:** PROME / Will. **What it's for:** "Is the vol regime about to shift, is convexity cheap, and which structure expresses it — and is the credit→vol transmission firing?"

## 2. File anatomy (where the richness lives) — HEAVY, thesis + workbook + a real quant engine
| File | Holds | Richness? |
|---|---|---|
| CLAUDE.md (179 ln) | 14-step write-back protocol (each step names its target file + trigger + `[[auto-memory]]` cross-refs); standing route-matrix (109-115); universal 5-pt scale def (135-144) | **L3/L4-grade protocol discipline** |
| STATUS.md (113 ln) | 9-vector convergence matrix + **45-pt composite** (script-verified, used as +Δ trend); drift assessment; REGIME STATUS synthesis block; positions; research queue | live state — well-kept (7/2, holiday-explained gap) |
| NEXUS_BRIEF.md (77 ln) | cross-agent synthesis; SENDING/WAITING-FOR tables w/ "mechanism it triggers in recipient's domain" | **exceeds blueprint minimum**; refreshed every closeout |
| SIGNAL_INTAKE.md (133 ln) | WALTER subscription spec (priority tiers/keywords); kept ACTIVE THRESHOLDS section w/ **documented divergence from CARL** | rich; a reasoned self-design decision |
| thesis/VIX_THESIS.md (443 ln) | **dual independent channels (Path A/B) each w/ transmission-stage diagram + independence rule; 4-layer confirmation stack w/ bypass rules;** base-rate tables (provenance-noted); crisis-analog DB; 6 falsifiable predictions + scoring key; risk-factors | **canonical thesis — exceeds blueprint §1** |
| thesis/CHANGELOG.md (127 ln) | version-by-version POV-pivot log (old-view→new-view diff + "predictions touched" per bump) | **institutional-learning spine** (the §5 feedback loop, working) |
| TRADE.md (217 ln) | live fade/hedge frameworks, named entry gates + kill conditions + adjudication record; ACTIVE POSITIONS = "None" w/ dated closeouts | **live execution layer** (git-current, `ledger_staleness --trade` = `ok +0d`) |
| MEMORY.md (216 ln) | 18 numbered calibration takeaways (session-by-session); regime semantics; metric-semantics landmines | durable learning |
| MAINTENANCE.md (238 ln) | **structural** changelog (why tools/guardrails are organized as they are) — explicitly NOT analytical (that's CHANGELOG) NOT ephemeral (that's SCRATCH) | provenance record |
| CALENDAR.md (116 ln) | color-banded catalyst gates + data-freshness ledger; declared "human twin" of `workbook/CATALYSTS.tsv` | dual-surface (must not diverge) |
| workbook/KB.tsv (112 rows) | 13-col atomic facts; **Epistemic (EMPIRICAL;ESTIMATE;ASSUMPTION)** + Admiralty digraph (A1–F6) + Stale_By + DerivedFrom + Vectors; KB-VIO-### IDs | permanent record (two orthogonal confidence axes) |
| workbook/{VX_DAILY,VIX_OPTIONS,COT_VIX}.tsv + fred_cache/ (11 series) | **LIVE, boot-refreshed** vol surface + options OI + COT positioning + credit series | live data spine |
| workbook/FLOW.tsv | FROZEN (correctly bannered) | handled-stale |
| **scripts/ (10 files)** | **the quant engine** — see §3 "quant"; all self-locating (`__file__`), boot invocation cwd-proof | **substance the L2 scan was blind to** |
| research/ (45 files, ~4,700 ln) | 19-yr/4,811-obs backtest, 17-episode SKEW-trajectory study, 4-LLM synthesis, **6 dated postmortems**, PHASE2_PLAN, source index | genuine quant research shop; all KB-ID-cited into thesis, not orphaned |
| README.md (51) / SCRATCH.md (63) / board_log.tsv (11) | pointer front-door / session handoff / WALTER disposition log | thin **by design** (README = "no live values") |

**`scripts/` quant engine (where the analytical edge lives):** `convexity_read.py` (274 — a derivatives-pricing rubric that separates *forecast* from *expression*: dual-window percentiling, VIX-bucket-conditional VVIX, CC-vs-Parkinson realized-vol decomposition, event-premium curve-location, mandatory carry/bleed flag); `diet_coiled_spring.py` (227 — 19-yr STRICT-vs-DIET trigger backtest w/ forward-return distributions); `regime_termination.py` (480) + `skew_trajectory.py` (526 — matched pair: "when does an elevated-SKEW regime end relative to the VIX event"); `thresholds.py` (334 — live band classification → `VX_DAILY.tsv`, TICK-vs-SETTLE state machine); `fred_fetch.py` (~198 — credit-gate CCC/Bin-A/Bin-B verdict, coded thresholds match STATUS live); `cftc_cot.py` (349 — 3-yr COT percentiles); `vix_options.py` (253); `backfill.py` (269 — M1:M2 convention-hazard gate); `boot.py` (146 — orchestrator).

## 3. Per-dimension local representation
| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| Thesis structure (§1) | thesis/VIX_THESIS.md | **dual independent channels** (Path A credit-led / Path B concentration-unwind) each w/ stage diagram + "don't require A when B is firing" independence rule; orthogonal 4-layer confirmation stack w/ explicit bypass | **exceeds** (above OTTO stage table) |
| Convergence / scoring (§2) | STATUS.md matrix + CLAUDE.md:135-144 | universal 5-pt PRESENT; **local 45-pt composite** (9 vectors × 5), script-verified (`convergence_score.py`), used as +Δ trend | 5-pt + 45-pt present; **Independence column MISSING** (prose only) |
| Thresholds (§3) | thesis + CALENDAR bands + `thresholds.py` BANDS + `fred_fetch.py` credit-gate | banded regime rules; DIET/STRICT **conjunction** tiers; durable-vs-live split exists but not file-boundary-clean (durable + live both in thesis tail) | **PRESENT-BUT-SCATTERED** across thesis/CALENDAR/SIGNAL_INTAKE/code |
| Invalidation / exit (§4) | thesis predictions + TRADE.md gates | **3 N+session rules** (DIET stop 4+td · Regime-Shift 7-day contango · Pred#6 SKEW>150 4+td **live tally 1/4**); channel-kill implicit via Path A/B independence | conformant; **"lacks session counts" flag is FALSE** |
| Predictions (§5) | thesis/VIX_THESIS.md §PREDICTIONS + CHANGELOG + research/ | 6 falsifiable predictions + scoring-rules key; **3-axis confidence discipline** (Epistemic + High/Med + Admiralty) — VIOLET is blueprint's NAMED confidence-tier source; failure→thesis-revision loop working (CHANGELOG) | strong substance; **handles unconsolidated** (no `PREDICTIONS.tsv`, no single ARCHIVE, if-falsified in TRADE.md not as column) |
| Cross-agent routing (§6) | CLAUDE.md:109-115 + NEXUS_BRIEF | condition→target→priority matrix; NEXUS_BRIEF = primary (SENDING/WAITING-FOR tables), outbox = 🔴-only | **exceeds** minimum |
| BOTTOM LINE (§8) | STATUS REGIME STATUS block | substance present (domain-state synthesis + forward gates) but **unlabeled + not 2-4 sentences** | **MISSING-HANDLE** |

## 4. Deviations from standard (+ why)
- **Better-than-blueprint:** (a) **dual-channel thesis + 4-layer confirmation stack** with explicit independence + bypass rules — richer than the OTTO transmission-stage table the blueprint asks for. (b) An 8-script **quant engine** invisible to a markdown scan: a convexity-pricing rubric with a forecast/expression separation, a 19-yr backtest engine, a matched regime-termination/skew-trajectory pair. (c) **3-axis confidence discipline** (KB Epistemic EMPIRICAL/ESTIMATE/ASSUMPTION + prediction High/Med + Admiralty A1–F6) — VIOLET is the blueprint's *named source* for the confidence-tier pattern (§5). (d) **Script-verified 45-pt composite** (caught a manual arithmetic error, per SCRATCH). (e) NEXUS_BRIEF SENDING/WAITING-FOR tables exceed the sync-surface minimum.
- **False-negative the mechanical scan made (CONFIRMED):** "exit-rules lack session counts" is **factually wrong** — three N+session exit/re-arm rules exist, one carrying a live running tally (Pred#6, 1/4 td). Same class as the HAWK/LIQUID false-negatives (PAT-024): the scan's *substance* claims are unreliable; only its missing-*labeled-handle* claim (BOTTOM LINE) checks out.
- **Debt (real, all handle-level or hygiene — never a rewrite):**
  - (a) **§8 BOTTOM LINE** missing labeled handle (substance in REGIME STATUS). *missing-handle, S.*
  - (b) **§2 Independence column** absent from the STATUS matrix. *missing-handle, S.*
  - (c) **§5 predictions handle-consolidation** — no `PREDICTIONS.tsv`, no single archive, no literal confidence-tier column, if-falsified position-consequence lives in TRADE.md gates not as a table column. *missing-handle (substance all present), M — floor-not-ceiling: add thin handles alongside.*
  - (d) **§8 TRADE.md staleness MECHANISM absent** — `ledger_staleness.py --trade` not wired into CLAUDE.md/boot.py; currency (`ok +0d`) is sustained by *manual same-session discipline only* — the exact single-point-of-failure the blueprint mechanism exists to remove. *missing-handle, S (one cwd-proof boot line).*
  - (e) **2 dead CSVs silent-rot** — `workbook/hy_oas_fred.csv` + `combined_vix_credit.csv` (last row 2026-04-09, zero references, superseded by the 6/23 fred_cache rewrite) sit un-bannered/un-archived. *hygiene, S — FROZEN banner or `git mv` to archive.*
  - (f) **3 dangling `archive/` refs** — README:27, CLAUDE:175, SIGNAL_INTAKE:133 point into a `VIOLET/archive/` dir **deleted fleet-wide** in the public-prep prune (`1cb18fbc`/`7133b7d6`); the files are gone repo-wide. *hygiene, S — repoint or drop.*
  - (g) **VIX_THESIS.md append-on-top tail stale** — the "Current status" tail (`:406-436`) is stamped 6/10 (~24d) under a 7/2-refreshed header, still citing superseded 6/10 marks. *self sub-case PAT-032, owner-lane, M.*
  - (h) **TRADE.md footer self-stamp** declares 7/1 while body has 7/2 content (fresher-than-declared). *trivial, `finding_selfstamp_estimate_drift` family.*

## 5. Load-bearing context / DO NOT TOUCH
- **45-pt composite** is a deliberate, blueprint-endorsed local scale (cited by name, `market-agent.md:37`) — the 5-pt is already ADDED alongside it; never flatten the 45-pt to look like a plain 1-5.
- **SIGNAL_INTAKE.md kept ACTIVE THRESHOLDS section** — a *documented, reasoned* divergence from CARL (`[[finding_documented_divergence_as_discipline]]`); don't force-align without re-litigating the stated rationale.
- **Three-way memory partition** — MAINTENANCE (structural) / thesis/CHANGELOG (analytical) / SCRATCH (ephemeral), stated at MAINTENANCE:5-8. Do not collapse.
- **CALENDAR.md ↔ workbook/CATALYSTS.tsv** are a declared "human twin" pair that "must not diverge" — same dual-surface design as SIGNAL_INTAKE.
- **KB-VIO-### citation scheme** threaded through the thesis (load-bearing cross-ref index) — don't renumber. **KB Admiralty digraph (A1–F6) ≠ Epistemic column** — different axes; don't conflate when grading confidence maturity.
- **M1:M2 = T-1 convention** (`thresholds.py` stamps `m1m2_settle_date`); `backfill.py` refuses the m1m2 path unless `--allow-m1m2` (tightened 6/14 from warn-to-hard-gate). **TICK vs SETTLE basis** — `thresholds.py` never downgrades a SETTLE row to TICK.
- **fred_fetch merge-on-write cache** — one canonical `{series}_{start}.csv`, use `latest_value()`, never hand-glob (an earlier per-day convention caused a false "fetch broken" misdiagnosis).
- **`final_5d_change` vs `20d regression slope`** — two SKEW "slope" metrics VIOLET explicitly warns against conflating (KB-VIO-059); any DAEDALUS summary citing "SKEW slope" must name which.
- **Episode % claims must name their anchor** (first-fire/last-fire/lowest-base) — VIOLET hardened this rule after catching itself twice (KB-VIO-083/084); a DAEDALUS summary of its hit-rates must carry the same anchor-naming or risk repeating the exact error.
- **outbox near-empty by design** (🔴-acute only; NEXUS_BRIEF is primary) — a thin outbox is conformance, not neglect.

## 6. Maturity snapshot
**L4 (conf H)** — a **2-level under-rate** corrected (was L2 Conf-L; PAT-024 again). Convergence (5-pt + script-verified 45-pt) / Predictions (confidence-tier named source + working revision loop) / Quant-engine = **exemplary**; Thesis-structure (dual-channel + 4-layer) and Routing (NEXUS_BRIEF SENDING/WAITING-FOR) = **exceed**; Thresholds = conformant-but-scattered; Invalidation = conformant. Both L4 criteria met: **TRADE.md live feeding fade/hedge proposals; signals flow via NEXUS_BRIEF + route-matrix.** Below L5 on: BOTTOM LINE handle, Independence column, predictions-handle consolidation, `--trade` mechanism unwired, 2 dead CSVs, 3 dangling archive refs, thesis-tail append-drift. Work queue → `upgrades/VIOLET_CARD.md`. Classification per `FLEET_MAP.tsv` (not restated).

## 7. Open questions / comprehension gaps
- **§3 durable-vs-live threshold split is real but not file-boundary-clean** — durable base-rate tables and the live "Current status" read both sit inside VIX_THESIS.md (rather than durable-in-thesis / live-in-STATUS). Is that an intentional single-surface choice or drift? The append-on-top staleness (debt g) suggests the live tail wants to move to STATUS. Owner call — flag, don't impose.
- **Predictions-handle consolidation must preserve the 3-layer numbering** (thesis #1-6 / KB-VIO-### / TRADE-framework-names are deliberate separation-of-concerns) — a naive "unify into one PREDICTIONS.tsv" would flatten it. The right handle is a thin `PREDICTIONS.tsv` that *indexes* the existing thesis table, not a replacement.
- **Pred#6 sustain count** was 1/4 as of 7/1; whether it advanced/lapsed by 7/2-7/4 wasn't visible (holiday-gapped). Owner resolves at next boot.

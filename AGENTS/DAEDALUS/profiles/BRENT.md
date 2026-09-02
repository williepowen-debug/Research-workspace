# Agent Profile — BRENT

> ⚠️ **STALE — TRIGGER FIRED, unserviced (PR#5 2026-09-01):** THESIS v5.6→v5.7 (8/21) · TRADE.md + REGISTRY moved · body 7/28. Read the FLEET_MAP row (re-cut 2026-09-01) and `upgrades/PRODUCTION_REVIEW_2026-09-01.md` before this body. Refresh checkpoint: **2026-09-15**. *(Bannered by `scripts/profile_clock_check.py` + the PR#5 readers; a banner is a warning, not a fix — PAT-085.)*

## Δ 2026-08-17 — BODY SUPERSEDED IN PART (structure review; all 3 of this profile's own refresh triggers FIRED — rebuild queued) *(banner relocated to header 2026-08-17, self-audit F17 — was mid-file at line 81 below an unmodified header)*
Triggers fired: THESIS **v5.1→v5.6** · TRADE ~160→**822 lines** · convergence matrix **ARCHIVED 8/13** (no live successor — L3 dimension deliberately vacant, honest banner, no rewrite trigger). §2 position table stale (STNG removed 8/04 as never-held; live book = 5 legs ~$5,131 broker-verified 8/04). §4's S1-S4 structural findings **ALL CLOSED** (verified 8/17); §6's L5 condition narrowed to the one derived-surface closeout leg (failed a 3rd time — TRADE:3 stamp class). thresholds.py re-pointed to REGISTRY **and** the FRED-shadow killed 8/17 (`bb0f1749f`). FASTOW still dormant, note still missing (3rd flag). **Read the three 8/17 reader reports + synthesis (`upgrades/BRENT_*_2026-08-17.md`, `SAM_BRENT_REVIEW_2026-08-17_SYNTHESIS.md`) before relying on any §-body claim.**


**Built by:** DAEDALUS · **Original:** 2026-06-29 (firm7-profiles-cards) · **FULL REFRESH: 2026-07-28** (Will-directed architecture audit, 3-reader Mode-A fan-out — clears the 7/22 Δ-banner, was refresh priority #3)
**Sources read (7/28):** CLAUDE.md (full), STATUS.md, TRADE.md, SCRATCH.md, NEXUS_BRIEF.md, LESSONS.md, thesis/{THESIS v5.1, PREDICTIONS.tsv, PREDICTIONS_ARCHIVE, CHANGELOG, TIMELINE}, workbook/* banners, demand_destruction/{TRACKER + corpus headers}, docket/*, refinery_damage/INCIDENTS.tsv, scripts/* (incl. code-level thresholds.py), inbox/outbox trees, full file tree (266 files) · **Staleness:** refresh when TRADE.md, THESIS version (currently v5.1), or the convergence matrix materially changes, or >45 days.

> Durable understanding — section-tasks read THIS, not the raw (heavy) agent. Re-read the actual file before applying any change (PAT-009).

---

## 1. Identity
Oil & energy markets — Brent/WTI spot + term structure, crack spreads, OPEC+, Gulf production, storage (Cushing/SPR/floating), tankers/freight + war-risk, US shale/rigs, demand indicators, energy HY credit. **Class:** Market. **Transmission:** consumes ← HAWK (cross-war synthesis; kinetic supersedes) + OSPREY/FALCON (theater signals direct since the 7/12 split, HAWK cc'd) + MARCO (trade policy) + AEOLUS (climate) + WALTER lane (`inbox/WALTER/`); sends → CARL (pump/consumer), HENRY (energy CPI/PPI), LIQUID (energy HY-OAS), SAM (Japan LNG), REGINALD (energy loans), TERRY (trade construction), PROME (adjudications). Cedes kinetic/scenario-%s to HAWK; systemic credit to LIQUID; inflation prints to HENRY. **In the MSG-v1 first cohort** (PROME→BRENT allowlisted route; receipts under `messages/receipts/`, ACTION-class only). **Spawnable by:** PROME / Will.

## 2. File anatomy (7/28 tree, 266 files)
| File | Holds | State |
|---|---|---|
| STATUS.md (207 ln) | live dashboard: regime banner (7/27 adjudication), PRICE DASHBOARD, **convergence matrix 63/75 (~12 effective indep drivers, re-scored 7/23)**, predictions table, catalyst calendar, SUMMARY FOR WILL (:199, local BOTTOM-LINE form — sanctioned) | live; under cap; ⚠️ vestigial "Last Updated: 2026-07-08" at :24 = false-staleness trap |
| TRADE.md (~160 ln) | canonical trade surface: stance v5.1, POSITIONS (USO 2sh, STNG 2sh, USO Sep-18 150/165 call spread FILLED 7/24, XLE 65C lapse), EXECUTION LOG, catalysts twin-table | live, `--trade ok +0d`; ⚠️ header stamp rot class (7/23 "pending fill" vs 7/27 body at audit time) |
| thesis/THESIS.md | **v5.1 (7/21)** — timed-race frame, 4 channels, EXIT PROTOCOL, KEY THRESHOLDS (live registry) | exemplary, current |
| thesis/CHANGELOG.md | version audit trail, newest 7/23 | rich |
| thesis/PREDICTIONS.tsv (~57 rows) | calibration ledger + scoreboard preamble (by-class anchors + PRE-FLIGHT CHECK) | **exemplary discipline; preamble "As of" stamp rots behind appended notes** |
| thesis/PREDICTIONS_ARCHIVE.md | per-pred post-mortems | lags ~6wks (newest BRT-27) |
| thesis/TIMELINE.md | ⛔ FROZEN 7/01, successors named | compliant |
| workbook/KB, VX, FLOW .tsv | FROZEN 7/01 banners + per-row disposition + live-successor pointers (VX carries a verified no-live-refs grep note) | **fleet FROZEN-banner model** |
| workbook/GROUP_MAP.tsv | FROZEN 7/16, banner self-declares pending delete (never executed) | minor debt |
| workbook/SCHEMA.tsv | 13-col KB schema — **unbannered** (silent middle) | minor debt |
| workbook/STATUS_archive_* (10) | STATUS snapshots Mar→7/16, live-referenced from STATUS:24,70,75,207 | deliberately homed; placement debt only in the strict sense |
| demand_destruction/TRACKER.md | live ops dashboard, current 7/27; data/ current 7/27 | live |
| demand_destruction/{ANALOGS,HAMILTON,HOARDING,TRANSITION_MATRIX,MATRIX_REVIEW} | static Mar-Apr research corpus (ANALOGS lacks any vintage header) | static |
| docket/CATALYSTS.tsv | canonical forward-state, actively curated (7/27 JMMC 🔴→🟠 w/ authority-verification note; prune-dates) | live, exemplary curation |
| docket/{FASTOW,FASTOW_MEMORY}.md | catalyst-steward sub-agent — **dormant since 6/07 (Run 2)**, BRENT maintains docket directly, no dormancy note | silent middle |
| refinery_damage/INCIDENTS.tsv | strike ledger w/ `last_verified` col, newest RF-038 verified 7/23 | live |
| NEXUS_BRIEF.md | v5.1 cross-agent brief — NEXUS boot-reads it | ⚠️ body sections rot to prior-closeout vintage under a fresh "As of" stamp |
| SCRATCH.md | session handoff (template in templates/) | **best-maintained surface**; logs own failures candidly |
| LESSONS.md | numbered lessons #1-21+ (#21 = spec-defect escalations to Will) | learning loop |
| board_log.tsv | WALTER-lane consumption ledger | live |
| CLAUDE.md (184 ln) | instructions; symmetric boot↔closeout; boot.py step 5 + ledger_staleness 5a cwd-proof | see §4 wiring gaps |
| scripts/ (7 py + BUILD_PLAN) | boot.py orchestrates thresholds/eia_weekly/catalyst_countdown/predictions_due (all read-only); cot_grade.py + refiner_ratios.py UNWIRED; sole writer = refiner_ratios.py → own data TSV | **safe to run while live**; thresholds.py = registry-drift (§4) |
| inbox/ + inbox/WALTER/ + outbox/ | dual-lane intake + acute-only outbox w/ delivered/ | protocol gaps §4 (W-items) |
| archive/{legacy_20260721, research_20260321_corpus} | 7/21 sweep products: LAST_COMPLETION, board/, WALTER-handoff, Mar corpus (incl. 3 big .docx) | clean |
| Root loose: 2026-07-06_teams-session.md (live-referenced), PREREG_20260628_CME_reopen.md (resolved, predates setups/) | archive candidates w/ repoints | placement debt |

## 3. Per-dimension local representation
| Dimension | Where | Form | Rich? |
|---|---|---|---|
| Thesis | THESIS v5.1 + CHANGELOG | two-phase → v5.0 asymmetry-flip → v5.1; TIMED-RACE core; full vX.Y trail | exemplary |
| Convergence | STATUS matrix | 14+ vector, emoji+1-5, **63/75** w/ honest denominator expansion (7/21), "~12 effective independent drivers" note | strong |
| Invalidation/exit | THESIS EXIT PROTOCOL + TRADE arm/disarm | bidirectional-flip exit (blueprint's NAMED source); LESSONS #21 self-found two spec defects (OVX gate possibly unfireable-by-construction; off-ramp latency mismatch) — escalated to Will, UNRULED as of 7/28 | exemplary + self-critical |
| Thresholds | THESIS KEY THRESHOLDS (live registry) + CLAUDE.md copy + **scripts/thresholds.py hardcode** | three homes, no declared precedence; script copy DRIFTED to retired v4 language | ⚠️ the weak dimension |
| Predictions | PREDICTIONS.tsv + ARCHIVE | BRT-xx; by-class calibration anchors + PRE-FLIGHT CHECK; frozen-number discipline (COT off raw f_disagg.txt) | **best-in-fleet** |
| Cross-agent | NEXUS_BRIEF (steady-state) + outbox (🔴 acute only) + WALTER lane + MSG-v1 | SENDING/WAITING-FOR tables | strong; brief-body sweep is the rot point |

## 4. Deviations / debt (7/28 audit — full detail in `upgrades/BRENT_AUDIT_2026-07-28.md`)
- **Better-than-blueprint (unchanged):** PREDICTIONS calibration loop · FROZEN-banner model · bidirectional-flip exit · TIMED-RACE frame · TRACKER dashboard · **NEW 7/27-28:** retraction culture + frozen-grade discipline PROME calls "epistemically the sharpest surface in the fleet"; CATALYSTS authority-verification curation.
- **STRUCTURAL (8, S1-S8):** thresholds.py prints RETIRED thesis-break (<$75) + dead <$85 frame, sources frozen VX, omits 457-rig (registry-restatement, fleet n=2 w/ REGINALD) · cot_grade.py unwired (PAT-040) · no general-inbox boot step (CLAUDE:57 forbids; 16 packets sat 7/22→28) · PENDING guard prose-only (TRADE:115/SCRATCH:66 — the surfaces that rotted) · TRADE header "pending fill" vs FILLED log (+ same at NEXUS_BRIEF:61) · STATUS:24 vestigial 7/08 stamp, no PAT-044 headers anywhere · matrix rows (CPC/Storage) not swept at 7/27 closeout · NEXUS_BRIEF fresh stamp over 7/23 body.
- **Wiring gap (DAEDALUS-found):** outbox/delivered/ defined (CLAUDE:63) but no closeout step walks it — 11 closed-loop packets 7/8→7/27 top-level.
- **Root defect class:** banner layer updated at adjudication, derived/secondary surfaces not swept (`finding_seeded_selfsweep_secondary_surface_rot` family). Not a knowledge failure — a sweep-step failure.
- **12 minors:** dead `domain/sources/` ref · MSG validate bare-relative · CLAUDE hardcoded share counts · dup step-6 · PREDICTIONS preamble stamp + 7-vs-6 count · unstruck calendar rows ×2 files · SCHEMA unbannered · GROUP_MAP pending delete · BUILD_PLAN 3mo stale · FASTOW no dormancy note · ARCHIVE lag · ANALOGS no vintage.

## 5. Load-bearing context / DO NOT TOUCH
- **TRADE.md = canonical trade surface, LIVE** — never freeze-banner it; header stamp must move with body.
- **v5 SKEW-vs-DIRECTION guardrail** — "upside-convex" is positioning/skew, NOT a bullish price call. Any edit collapsing this breaks the thesis.
- **TIMED-RACE frame** (deficit-close vs buffer-exhaust clocks; price is the LAGGING tell).
- **Bidirectional-exit semantics** — sub-$75 = decoupling; break = reopening-grinds-to-$79 OR <$70-on-demand-collapse (revives the demoted-not-deleted Phase-2 short). thresholds.py currently CONTRADICTS this — fix the script TO the thesis, never the reverse.
- **FROZEN banners on KB/VX/FLOW** (+ per-row disposition + successor pointers) must survive any workbook touch.
- **PREDICTIONS scoreboard** by-class anchors + PRE-FLIGHT CHECK — don't flatten to a bare ledger; frozen numbers, never rolling percentiles (LESSONS #21a).
- **One-source-of-truth cessions** — HAWK kinetic/scenario-%s; LIQUID HY-OAS; HENRY CPI; STATUS live prices; THESIS conviction; TRADE position status.
- **NEXUS_BRIEF is boot-read by NEXUS** — its body vintage is externally load-bearing, not cosmetic.
- **MSG-v1 lane rules** (CLAUDE:168-183): receipts ACTION-only; never convert WALTER signals through it.

## 6. Maturity snapshot
**L4 (conf H) — L5 verify RUN 7/28: HOLD.** Fill-confirm leg PASSED (FILLED 7/24, loop closed); zero-operator-caught-errors leg FAILED (7/27 closeout left derived surfaces unswept; PENDING contradiction survived its own fix-note in 2 places). **New L5 condition:** one closeout cycle w/ derived surfaces agreeing with banner layer (S5-S8 clean) + thresholds.py repointed (S1) + wiring steps landed (S2-S4, outbox). Epistemic quality is already L5-grade (PROME 7/28: "the model the rest of the fleet gets pointed at"); the gap is purely mechanical sweep discipline. Classification per `FLEET_MAP.tsv`.

## 7. Open questions
- LESSONS #21 spec escalations (OVX gate unfireable-by-construction; off-ramp latency) — **UNRULED by Will**; PROME re-surfaced 7/28. Watch for the re-spec proposal w/ new frozen numbers.
- BRT-26 + COT-7/21 grades: land before Fri 7/31 stack? (PROME item 1 clock.)
- Does BRENT adopt the general-inbox boot step + outbox delivered-move step (its edit, its wording)? Verify at next touch.
- thresholds.py repoint: registry-read vs parse-THESIS — which form does BRENT choose? (Feeds the blueprint THRESHOLDS.tsv item, n=2.)
- FASTOW: resume runs or write the dormancy note?

---

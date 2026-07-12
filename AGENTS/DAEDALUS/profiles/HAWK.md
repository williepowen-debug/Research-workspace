# Agent Profile — HAWK

> ⚠️ **SUPERSEDED 2026-07-12 — HAWK was split** (OSPREY = Russia/Ukraine, FALCON = Iran/Gulf; HAWK re-cut to cross-war synthesis + dormant book; `builds/OSPREY_FALCON_BUILD.md`). This profile describes the PRE-split two-theater HAWK. Re-profile HAWK-residual + first profiles for OSPREY/FALCON after their first real sessions (≈7/18 production review). File anatomy below is stale; the §5 DO-NOT-TOUCH items largely migrated (scenario/convergence → FALCON, STRIKES schema → both siblings, FLOW-19 stays HAWK).

**Built by:** DAEDALUS · **Date:** 2026-06-29 · **Comprehension method:** 1-reader live comprehension (workflow `firm7-profiles-cards`; documents the 6/28 firm-next7 adversarially-confirmed L4)
**Sources read:** CLAUDE.md, STATUS.md, REMARK_20260628.md, NEXUS_BRIEF.md, thesis/{THESIS,PREDICTIONS.tsv,PREDICTIONS_ARCHIVE skim}, workbook/{EXIT_PROTOCOL,FLOW.tsv,KB.tsv counts,VX.tsv counts,SCHEMA refs}, TRADE.md, LESSONS.md, SOURCES.md, domain/energy-strikes/STRIKES.tsv, scripts/ + dir glob · **Staleness:** refresh when the scenario-weight spine (STATUS / REMARK) materially re-marks or the oil-handoff boundary moves, or > 45 days.

> Durable understanding — section-tasks read THIS, not the raw (heavy) agent. Re-read the actual file before applying any change (PAT-009).

---

## 1. Identity
Geopolitical & military risk — Iran war, Hormuz/Bab-al-Mandab chokepoints, sanctions/shadow-fleet, OPEC+ supply *events*, Russia-Ukraine energy-infra strikes, A/B/C/D escalation framework. **Class:** Market. **Transmission:** parallel external-shock trigger — SENDS to BRENT (oil scenario inputs), HENRY (vol catalyst), LIQUID (risk-off/credit trigger), SAM (Japan/Asia energy); also CARL/REGINALD on Hormuz channels. CONSUMES WALTER signal lane (inbox/WALTER + board_log), LIQUID/SAM/HENRY context. **Light-end / SINGLE-CHANNEL** (geopolitical event grain → oil/vol/credit transmission, ~4 SENDING edges). **Oil ceded to BRENT (Mar 6 2026):** does NOT track oil price/storage/tankers — feeds BRENT military inputs, references BRENT's levels. **Holds NO trade book** — a DATA agent; scenario inputs feed others' books. **Spawnable by:** PROME / Will. **What it's for:** "Is geopolitical escalation about to reprice oil/vol/credit — and is the war-premium decoupling holding?"

## 2. File anatomy (where the richness lives) — HEAVY, thesis-bundle + workbook layers
| File | Holds | Richness? |
|---|---|---|
| STATUS.md (130 ln) | scenario weights B/C/D + per-scenario flip-up/flip-down; "see-saw discipline" posture block; 10-vector convergence matrix (**22/50 🟠**); Watch-docket Tier1-3; cross-agent implications; live predictions table; BOTTOM LINE | live state — **STALE beneath REMARK (6/26)** |
| REMARK_20260628.md | live-event re-mark: **B20 / C44(base) / D36** on 6/28 IRGC strikes on US bases (Kuwait+Bahrain); pre-registered CONFIRM-D vs REVERT-C discriminators; FALSIFICATION; HAW-14 kinetic-floor-breach flag | **the current marks** (DO-NOT-COMMIT, PROME coordinates) |
| thesis/PREDICTIONS.tsv (16 live rows + scoreboard preamble) | HAW-NN ledger 10-col; scoreboard **4C/4F/1P/1V/5OPEN**; HIGH-CONF-FAILURES calibration warning; VOIDED-discipline notes; failure-pattern synthesis; per-row Invalidation | institutional calibration loop |
| thesis/PREDICTIONS_ARCHIVE.md | verbatim post-mortems for closed rows, `#hawk-NN` anchors | reference-only (not boot-read) |
| thesis/THESIS.md (v1.2) | core thesis + 3 transmission channels + scenario framework | **SUPERSEDED Apr 20** (D75% regime); vestigial, carries forward-pointing banner |
| thesis/{CHANGELOG,TIMELINE}.md | thesis-bundle history + event timeline | history |
| workbook/KB.tsv (207 rows, max KB-HAWK-205) | 13-col atomic claims, Admiralty digraph A1–F6 + EMPIRICAL/ESTIMATE/ASSUMPTION epistemic + Stale_By + DerivedFrom + Vectors | permanent record |
| workbook/FLOW.tsv (20 pathways, FLOW-HAWK-01..19) | transmission engine; **FLOW-HAWK-19 = canonical "Salvo Regime Decoupling" thesis home**; rows 01-18 MUTED w/ inline `[STALE Apr20 figs]` banners | permanent (canonical thesis lives here, not THESIS.md) |
| workbook/VX.tsv (18 vectors) | banded geopolitical risk indicators w/ Green/Yellow/Orange/Red thresholds | permanent |
| workbook/EXIT_PROTOCOL.md | falsification criteria — Thesis-Kill, 7-step Scenario-A exit ladder, C→B / B→A downgrades, D-indicators, cross-agent thresholds | rich exit rail |
| workbook/SCHEMA.tsv | KB data dictionary — enum allowed_values + defaults (read before KB write) | method |
| workbook/{FOUR_STRUCTURAL_BREAKS,POLITICAL_SUSTAINABILITY_MODEL,PRICE_BREACHES.tsv,BOOT_LOG} | supporting models / breach log | supporting |
| domain/energy-strikes/{STRIKES.tsv (29 rows),SUMMARY.md} | **unified cross-theater strike ledger** (Iran + RU-UA, 16-col, %-offline sourced, crude-export vs product/crack channel taxonomy) | exceeds blueprint (auto-memory `energy_strike_ledger`) |
| NEXUS_BRIEF.md | cross-agent synthesis twin — VIEW/CALIBRATION/CROSS-DOMAIN(send+wait)/NEXT-DECISION/FORWARD-CATALYSTS; refreshed every closeout | sync surface |
| SCRATCH.md (+ templates/SCRATCH.template.md) | canonical session handoff | ephemeral |
| LESSONS.md | numbered mistake-patterns gating predictions (prediction-text==vector-text; live-war gap-sweep) | learning |
| MEMORY.md / SOURCES.md / CALENDAR.md / DECK_EVIDENCE.md | durable learnings / source index (not boot-read) / catalyst cal / Mar-17 evidence deck | reference |
| scripts/ (boot.py, catalyst_countdown, oil_infrastructure, sanctions_tracker, thresholds, war_monitor, PLAN.md) | boot + monitors | tooling — **NO ledger_staleness.py (dangling boot ref)** |
| audits/ (5 May-22 phase files), research/ (deep dives), domain/sources/ (UNCTAD 4MB PDF, FM maps, PNGs), archive/, inbox/processed/ | history / source fulltext / mail | SKIP (huge/binary) |

## 3. Per-dimension local representation
| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| Thesis structure | FLOW-HAWK-19 ("Salvo Regime Decoupling") + STATUS scenario block + REMARK; THESIS.md SUPERSEDED | A/B/C/D scenarios w/ %weights + flip-up/flip-down per scenario; "Damage-vs-Salvo decoupling" regime thesis canonical in FLOW-19 | strong (canonical home = FLOW-19; THESIS.md vestigial) |
| Convergence / scoring | STATUS "Convergence Matrix" | 10-vector Iran-core, 5-pt scale (🔴🔴5..⚪1), headline **22/50 🟠**, per-vector `Threshold → Next Level` + `Last Updated`; **Russia-Ukraine tracked OFF-core (NOT in the Iran sum)** | exemplary |
| Invalidation / exit | **5 places:** STATUS scenario flip-conds · CLAUDE.md EXIT RULES (4 cat) · workbook/EXIT_PROTOCOL.md · PREDICTIONS Invalidation col · HAW-11 named kill-switch · REMARK FALSIFICATION | named decoupling **kill-switch (HAW-11)**, 7-step Scenario-A exit ladder, bidirectional scenario flips | exemplary (old "no exit rails" = false-negative) |
| Thresholds | VX.tsv (banded) + STATUS matrix `Threshold→Next-Level` + CLAUDE.md cross-agent send-table | banded vector thresholds; mechanism-vs-threshold discipline (`[[finding_threshold_vs_mechanism]]`); declaratory≠physical | conformant |
| Predictions | thesis/PREDICTIONS.tsv + ARCHIVE + scoreboard preamble | HAW-NN IDs (collision-safe), scoreboard 4C/4F/1P/1V/5OPEN, VOIDED-disposition discipline, pre-registration rubrics, failure-pattern synthesis | exemplary |
| Cross-agent routing | CLAUDE.md CROSS-AGENT SIGNALS table + NEXUS_BRIEF + outbox/ | condition→target→priority; NEXUS_BRIEF = primary surface, outbox = 🔴-acute only; ~4 SENDING edges (light-end) | conformant |

## 4. Deviations from standard (+ why)
- **Better-than-blueprint:** (a) falsification expressed AS a scored prediction — **HAW-11 named decoupling kill-switch** ("if it fires, market was complacent; if it expires, decoupling reinforced") — tighter than a prose exit rule. (b) **Unified cross-theater STRIKES.tsv** (Iran + Russia-Ukraine in one %-offline-sourced ledger w/ channel taxonomy) > a single-theater table. (c) Best-in-fleet **calibration hygiene**: VOIDED disposition for premise-failed conditionals ("no right-for-wrong-reasons credit", HAW-07), pre-registered action-based rubrics set BEFORE evidence (HAW-08/09), HIGH-CONF-FAILURES preamble + 3-mode failure-pattern synthesis. (d) **Off-core Russia-Ukraine EXCLUDED from the Iran convergence sum** (two independently-driven theaters; refuses false convergence inflation). (e) **REMARK live-event-override pattern** — re-mark artifact without a full closeout when markets are mid-event (`[[finding_boot_protocol_live_event_override]]`).
- **False-negatives the old mechanical scan made (per grounding — CONFIRMED):** "no exit-rules / missing falsification rails" was a **DEFINITIVE false-negative** — exit/falsification material is rich and lives in 5 places. HAWK is a strong-calibration agent, not a thin one.
- **Debt (real):** (a) **TRADE.md frozen-in-amber Mar-11** — a pre-oil-handoff oil book (USO/STNG/TLT/LNG/copper calls now BRENT's domain), **NO FROZEN banner** = silent-rot middle (root-CLAUDE hygiene violation; PAT-023). (b) **THESIS.md SUPERSEDED Apr 20** with a "rewrite to current regime = #1 next-session item" pending since Jun 8 and never done — vestigial thesis-layer (mitigated vs TRADE.md: it DOES carry a forward-pointing banner; canonical thesis moved to FLOW-19+STATUS).
- **Dangling refs (boot/closeout friction):** (a) CLAUDE.md boot step 5a runs `python3 scripts/ledger_staleness.py HAWK` (wired 2026-06-27) — **script ABSENT** → boot step no-ops/errors. (b) CLAUDE.md closeout step 11 references `workbook/CEASEFIRE_FADE_PROTOCOL.md` — **ABSENT**. (c) CLAUDE.md KB schema doc says IDs "Sequential (currently through KB-HAWK-034)" — stale self-ref; actual max KB-HAWK-205.
- **Handled-stale (acceptable):** FLOW rows 01-18 carry inline `[STALE Apr20 figs]` banners + MUTED status — flagged-not-silent; the live regime is FLOW-19.

## 5. Load-bearing context / DO NOT TOUCH
- **Oil-handoff boundary (Mar 6 2026):** HAWK does NOT own oil price/storage/tankers — defers to BRENT. The CLAUDE.md ⚠️ OIL HANDOFF banner + SOURCES split must survive; any "oil price" content in TRADE.md/THESIS.md is pre-handoff residue, not live scope.
- **FLOW-HAWK-19 = canonical decoupling/salvo-regime thesis home** (NOT THESIS.md). Don't "fix" THESIS.md by treating it as canonical.
- **HAW-NN prediction IDs** (collision-prevention) + the pre-registered canonical sentence per prediction (LESSONS Jun-12: prediction-text must equal vector-threshold-text; on conflict PREDICTIONS.tsv text wins).
- **VOIDED disposition** for premise-failed conditionals (HAW-07) — calibration integrity; never re-grade to CONFIRMED for incidental directional accuracy.
- **Scoreboard preamble** in PREDICTIONS.tsv (HIGH-CONF-FAILURES + failure-pattern synthesis) — load-bearing calibration warning, read before any new prediction.
- **Off-core Russia-Ukraine EXCLUSION** from the Iran convergence sum (no causal "regime rotation" claimed — observed-alongside).
- **REMARK_20260628 is DO-NOT-COMMIT** (PROME coordinates the merge); it holds the live marks while STATUS is the stale base.
- **KB Admiralty digraph (A1–F6) + Epistemic tags + SCHEMA/VOCABULARIES enum-validation** before any KB write.
- **STRIKES.tsv schema** (16-col, `RU-YYYYMMDD-NAME` / `IR-…` id convention, channel = crude-export vs product/crack — the HAW-15 Brent-flip trigger depends on this distinction).
- **See-saw discipline block** in STATUS (marks held loosely; declaratory≠physical; rhetoric≠resolution; mechanism≠threshold) — the agent's standing anti-whipsaw guard.

## 6. Maturity snapshot
**L4 (conf H)** — confirms the 6/28 firm-next7 adversarial grade. Convergence / Predictions / Invalidation-exit = **exemplary**; Thresholds / Cross-agent-routing = conformant; Thesis-structure = strong (canonical in FLOW-19; THESIS.md vestigial). Both L4 criteria met: scenario inputs feed BRENT/SAM/HENRY books (HAWK is a no-book DATA agent), signals flowing via NEXUS_BRIEF + outbox. Below L5 on: TRADE.md not frozen (silent-rot), THESIS.md vestigial-uncrewritten, 2 dangling boot/closeout refs, STATUS spine stale beneath REMARK. Work queue → `upgrades/HAWK_CARD.md`. Classification per `FLEET_MAP.tsv` (not restated).

## 7. Open questions / comprehension gaps
- **Biggest drift from grounding:** the grounding's market picture ("decoupling-shrug, armed-stalemate, D 22%") is **superseded by REMARK_20260628** — a vertical kinetic re-escalation (6/28 IRGC strikes on US bases Kuwait+Bahrain + 2 nights US strikes on Iranian soil + tanker hit + ~80 Hormuz mines) moved D **22→36** and re-opened the decoupling test. STATUS.md (6/26) has NOT absorbed this; HAW-14's protected threshold is breached-but-not-literally-falsified (fired via tanker→strike chain, not the Lebanon path it names) and flagged for re-word at next closeout. Couldn't verify post-6/28 state (Sun 6PM ET oil open was the pre-registered tie-breaker; whether marks were further re-marked or folded into STATUS is unknown to me).
- Did `upgrades/HAWK_CARD.md` get created (the referenced work queue)? Not verified this read.
- KB has 207 rows but max ID KB-HAWK-205 → non-sequential gaps; agent's own count discipline (and the stale CLAUDE.md "through KB-HAWK-034" doc figure) unverified against a full ID audit.

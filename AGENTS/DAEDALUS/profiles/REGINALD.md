# Agent Profile — REGINALD

**Built by:** DAEDALUS · **Date:** 2026-06-29 · **Comprehension method:** 1-reader live comprehension (workflow `firm7-profiles-cards`; documents the 6/28 firm-next7 adversarially-confirmed L4)
**Sources read:** CLAUDE.md, STATUS.md, thesis/THESIS.md, TRADE.md, workbook/{PREDICTIONS,KB,FLOW,VX}.tsv + 4 frozen feeds (DARKPOOL/SHORT_VOL/SHORT_INTEREST/OPTIONS_OI headers), registry/THRESHOLDS.tsv, BANK_EXPOSURE_MATRIX.md (head), WAL/THESIS.md, bank-subdir inventory (EGBN/FITB/MTB/PNC/RF/ZION/CFG via Glob), 30d git-log authorship breakdown · **Staleness:** refresh when the STATUS convergence-matrix scores / EXIT RULES materially change, when thesis/THESIS.md version-bumps off v1.4, or > 45 days.

> Durable understanding — section-tasks read THIS, not the raw (heavy) agent. Re-read the actual file before applying any change (PAT-009).

---

## 1. Identity
Regional-bank **convergence HUB** — the transmission terminus where eight independent stress channels (CRE / Hidden-CRE / NDFI-SSFA / Private-Credit / MFS-Fraud / CMBS-maturity-wall / Federal-layoffs / Stagflation) all land at CRE-heavy regional balance sheets. **Class:** Market. **Transmission:** the named end-of-chain hub — consumes from CREED (CRE market, sub-agent), BROCK (PC/BDC, peer), CORAL (Florida, peer), OZK (single-name, peer), CARL (consumer), LABOR (claims), LIQUID (funding/spreads), SAM (Japan), WALTER (signal lane via inbox/BOARD). Sends to PROME/LIQUID/ALL on the hard triggers (KRE<$60, FHLB>$700B, Tier-1 capital raise/miss). **Spawnable by:** PROME / Will. **Signature discovery:** Hidden CRE via FFIEC Memo Item 3 / RCON2746 (CRE relabeled as C&I). **What it's for:** "Which banks have multiple independent paths to break, and which one breaks first?" Multi-channel > single-channel. **NAMED source agent for the market-agent blueprint's thesis structure** (8-channels→4-clusters w/ independence analysis).

## 2. File anatomy (where the richness lives) — HEAVIEST agent in fleet (~500 files, multi-layer)
| File | Holds | Richness? |
|---|---|---|
| STATUS.md (222 ln, ≤250 cap) | live header (2 dated blocks); **THESIS: The Convergence** 8-channel table; **SIGNAL DASHBOARD** (~40 indicator rows w/ source-stamp + status emoji); RESEARCH-POSITION NAMES pointers; **CONVERGENCE MATRIX — Targets & Positions** (ranked banks, own 0-20 score); Cohort-NCO resolved table; Life-Sci 3-instance table; KEY CATALYSTS; CROSS-AGENT TRIGGERS (8 rows, fired-status); EXIT RULES; THRESHOLD STATUS table | live state — dense |
| thesis/THESIS.md (v1.4, 2026-04-16) | structural thesis: 8 channels → **4 independent clusters** + channel-independence analysis + loss quant + validation scorecard. The blueprint's named thesis-structure exemplar | structural (slow-moving; lags operative narrowing — see §4) |
| thesis/{TIMELINE,CHANGELOG}.md | forward catalyst narrative; thesis evolution audit trail | versioned history |
| workbook/VX.tsv (62 rows, 13-col) | indicator vectors — banded Yellow/Orange/Red + Status + Confidence + Cross_Links. The live signal engine | permanent record |
| workbook/KB.tsv (139 rows, 15-col) | knowledge base, ML-REG-xxx — Description/Analysis/Data_Quote/Source/Confidence(num)/Thesis_Impact/Vector_Links | permanent record (**stale — refresh-flagged, NOT frozen; see §4**) |
| workbook/FLOW.tsv (22 rows, 11-col) | **transmission/contagion engine** — Speed/Layer/Status (LATENT/ACTIVE-SLOW/…)/Trigger/Pathway/Key_Insight | permanent record (**stale, rows dated 2026-02-16 — refresh-flagged, NOT frozen**) |
| workbook/PREDICTIONS.tsv (21 rows, 10-col) | REG-01..REG-25 (gaps at 16/21/22/23); 16 OPEN / 2 CONFIRMED / 1 FAILED / 1 FROZEN-FAILED / 1 FROZEN-PENDING; resolved kept inline via status flags. **No separate ARCHIVE / no Brier SCOREBOARD** (unlike BROCK) | learning loop (thinner than BROCK's) |
| workbook/{DARKPOOL,SHORT_VOL,SHORT_INTEREST,OPTIONS_OI}.tsv | **FROZEN 2026-06-27** (PROME) — 0 live consumers, last pull ~Apr; banner present | FROZEN — do not cite |
| workbook/{CHANNELS,CRE_ARCHITECTURE,CONVERGENCE,NDFI_RESEARCH,THESIS_VALIDATION,OTTO_INTEL}.md | framework detail referenced from STATUS FRAMEWORKS table | reference |
| registry/THRESHOLDS.tsv (8 rows) | **machine-readable trigger registry** — trigger_id/metric/op/value/sustain_window/action/recipient_chain/thesis_ref. Formalized beyond blueprint | exemplary (rare) |
| BANK_EXPOSURE_MATRIX.md (614 ln, 32KB) | "The Matrix" — multi-channel per-bank scoring methodology + Hidden-CRE (Memo3) screen + Metropolitan Capital autopsy | reference (**stale, last 2026-02-23**) |
| POSITIONS.md (Jun 19) | **canonical position truth** — strikes/expiries/contracts from broker screenshots | live position truth |
| TRADE.md (31KB, hdr "Mar 6", OZK-extract note 4/24) | trade doctrine/construction per name | **STALE — April vintage; POSITIONS.md + STATUS matrix are live** |
| WAL/ (64 files) | sub-agent-grade single-name: THESIS(v2.2.1)/SCENARIOS/CHANGELOG/KB-workbook/FRAUD subdir/INVESTOR_DAY/LEADERSHIP/TECHNICALS/WEAKNESSES/AUDIT/EARNINGS_PREP | deepest single-name |
| EGBN/FITB/MTB/PNC/RF/ZION/CFG/ (9-21 files each) | per-bank THESIS/SCENARIOS/STATUS/EARNINGS_PREP/WEAKNESSES/INDEX | deep per-name |
| MEMORY.md / ROADMAP.md / SCRATCH.md / CALENDAR.md / LESSONS.md | session handoff / persistent threads / scratch / dates / mistake-rules | working state |
| board/BOARD_LOG.tsv | 11-col WALTER-board disposition ledger (9b boot scan) | signal-routing record |
| sub-agents/CREED/ (full workbook: KB/VX/FLOW/PREDICTIONS + research/sources) | CRE market-level sub-agent | sub-agent state |
| archive/, session_archive/, sources/*.pdf, *.docx, inbox/WALTER/*, MTB/sources/*.pdf | history / raw fulltext / PNGs / signal drops | SKIP |

## 3. Per-dimension local representation
| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| Thesis structure | thesis/THESIS.md + STATUS "THESIS: The Convergence" + FLOW.tsv | 8 channels → **4 independent clusters**, channel-independence analysis (the *independence*, not just severity, is the claim). **NAMED blueprint exemplar.** | exemplary |
| Convergence / scoring | STATUS "CONVERGENCE MATRIX — Targets & Positions" + BANK_EXPOSURE_MATRIX.md | **own per-bank 0-20 multi-channel score** (EGBN 20 / WAL 20 / CFG 15 / ZION 14→8-9 / OZK 13 / SSB 11 / FLG 8), NOT the universal 5-pt composite. Channel-status emoji (🔴/🟠) in the 8-channel + ~40-row SIGNAL DASHBOARD | strong (own scale) |
| Invalidation / exit | STATUS "EXIT RULES" | Exit-50% / Exit-100%(auto: BTFP 2.0) / **HY<260 anchor-drift-reframed to REVIEW-trigger** (Will-confirmed 6/19) / CRE-channel exit anchors (WAL Q2 NCO <25bps + no Office migration). Documented-divergence discipline | exemplary |
| Thresholds | registry/THRESHOLDS.tsv + VX.tsv + STATUS "THRESHOLD STATUS" + "CROSS-AGENT TRIGGERS" | machine-readable registry (op/value/sustain_window/recipient_chain) + banded VX + live threshold table w/ sustain windows. CCC/HY >3.6×-sustain tripwire (VX-REG-18.04) | exemplary |
| Predictions | workbook/PREDICTIONS.tsv (canonical; display copy removed from STATUS 6/26) | REG-01..25, falsifiable + invalidation col; resolved kept **inline** via FROZEN-*/CONFIRMED/FAILED flags. **No Brier scoreboard, no post-mortem archive** | conformant (thinner loop) |
| Cross-agent routing | CLAUDE.md "CROSS-AGENT SIGNALS" (send/receive tables) + outbox/ + inbox/WALTER lane + board/BOARD_LOG.tsv (9b 3-tier board scan) | condition→target→priority; crisis-only outbox; structured board-disposition ledger. **No NEXUS_BRIEF** (REGINALD does not write one) | conformant (NEXUS gap) |

## 4. Deviations from standard (+ why)
- **Better-than-blueprint:** (1) registry/THRESHOLDS.tsv = a *machine-readable* trigger registry (op/value/sustain/recipient-chain) — rare, exceeds blueprint. (2) Per-bank subdir model (WAL 64 files, 7 named subdirs + 3 spun-out peers OZK/CORAL/BROCK) = sub-agent-grade depth per name. (3) Hidden-CRE Memo-3/RCON2746 methodology = an original discovery codified in BANK_EXPOSURE_MATRIX. (4) EXIT RULES anchor-drift reframe (HY<260 → review-not-exit) = documented-divergence discipline preventing a mechanical stop-out of a narrowed thesis. (5) 4-cluster independence analysis = the blueprint's *named* thesis-structure source.
- **Debt (real):** (a) **TRADE.md is April-vintage** (hdr "Mar 6", EGBN $25P Jun / KRE $62/65P Jun trades) — POSITIONS.md (6/19) + STATUS matrix are the live truth; the doctrine surface lags badly. (b) **thesis/THESIS.md frozen at v1.4 (2026-04-16)** while the *operative* thesis narrowed broad-systemic → idiosyncratic-WAL+CRE-specific (Hyp-A cohort resolution, 6/8) — the narrowing lives in STATUS, not folded into the structural doc. (c) **BANK_EXPOSURE_MATRIX.md last 2026-02-23** — the scoring-methodology reference is 4mo stale. (d) STATUS header "Last Updated: 2026-06-22" sits under newer 6/25 top-block content (append-on-top spine staleness). (e) KB.tsv / FLOW.tsv stale (FLOW rows 2026-02-16) — boot-flagged for refresh.
- **Handle gaps (cheap, = L5 path):** no labeled **BOTTOM LINE** in STATUS (CONFIRMED absent); no NEXUS_BRIEF.md; no universal 5-pt convergence composite (has its own 0-20 — floor-not-ceiling, NOT a defect); predictions have no Brier scoreboard / resolved-archive.
- **False-negatives the old mechanical scan made (per grounding):** "79d stale" flag was a **scanner column-misread** — REGINALD is the *freshest* agent (~37 own-authored core-file commits/30d, active through 6/26; the 79 total is inflated by ~34 WALTER inbox signal-drop commits). Do not re-trust a single-column staleness read on this agent.

## 5. Load-bearing context / DO NOT TOUCH
- **POSITIONS.md is canonical for positions, NOT the STATUS matrix Position column** (the matrix carries an explicit ⚠️ — it caused the 6/19 desync; grep POSITIONS first). Never trade off the matrix column.
- **EXIT RULES anchor-drift reframe** (HY<260 = REVIEW trigger not auto-exit; real exit re-anchored to CRE channel) — Will-confirmed 6/19, IN FORCE. Do not "restore" the mechanical HY<260 auto-exit.
- **registry/THRESHOLDS.tsv** machine-readable schema (8 cols) — downstream-consumable; preserve column contract.
- **4-cluster independence framing** in thesis/THESIS.md — the blueprint references this as the named exemplar; structural edits must preserve the "independence between clusters, not all 8 channels" claim.
- **Hidden-CRE Memo-3/RCON2746** methodology (BANK_EXPOSURE_MATRIX) — REGINALD's signature; OZK 37.6% / WAL 24.2% / EGBN 23.7% screen anchors multiple theses.
- **The drift-grep closeout discipline** (CLAUDE.md: recursive grep of old-value / new-value / version-label on any thesis change) — load-bearing hygiene that caught the WAL-version-behind bug 6/8; do not simplify to an enumerated file list.
- **The 4 FROZEN feeds carry banners (6/27)** — leave frozen; do not "revive/refresh." KB & FLOW, by contrast, are live-consumer ledgers → **refresh, do NOT freeze** (see §6 drift).
- Boot 9b BOARD-scan 3-tier cluster filter + board/BOARD_LOG.tsv 11-col schema — the WALTER signal-intake contract.

## 6. Maturity snapshot
**L4 (conf H)** — exemplary/conformant on 6/6 market dimensions; both L4 criteria met (live position layer via POSITIONS.md + STATUS matrix feeding proposals; signals flowing to PROME/LIQUID + receiving the WALTER board lane). Below L5 only on **hygiene + handles**: no labeled BOTTOM LINE; no NEXUS_BRIEF; stale TRADE.md (April) + thesis/THESIS.md (v1.4 April) + BANK_EXPOSURE_MATRIX (Feb); KB/FLOW stale-pending-refresh; thin predictions loop (no Brier/archive). **NOT a maturity blocker:** own 0-20 score in lieu of the universal 5-pt (floor-not-ceiling). The freshest agent in the fleet. Work queue → `upgrades/REGINALD_CARD.md`. Classification per `FLEET_MAP.tsv` (not restated here).

## 7. Open questions / comprehension gaps
- Are the TRADE.md April trades (EGBN $25P Jun, KRE $62/65P Jun, ZION $57.5P Jul) closed/expired or carried? POSITIONS.md (not read in full) is canonical — verify there + WILL/trading-journal, never STATUS, before any L5/position claim.
- PREDICTIONS count-of-record: STATUS says "22 predictions, REG-01..25"; TSV has 21 rows with ID gaps (16/21/22/23 missing). Agent's own closeout-hygiene question — which is canonical?
- thesis/THESIS.md v1.4 vs operative idiosyncratic-WAL narrowing — is the un-bumped structural doc intended (slow-moving by design) or genuine version lag? Check CHANGELOG before any edit.
- Did the 6/27 ledger_staleness wiring (boot 7a, root scripts/ledger_staleness.py) actually retire the KB/FLOW staleness, or are they still flagged at every boot? (refresh cadence unverified — only saw banners on the 4 dead feeds, not a KB/FLOW refresh.)

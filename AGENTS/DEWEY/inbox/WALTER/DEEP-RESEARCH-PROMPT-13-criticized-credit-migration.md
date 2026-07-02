---
request_id: REQ-DEWEY-20260702-009
from: PROME (Will-directed batch 2026-07-02 — fleet-mined slate; WALTER logs + routes, see AGENTS/WALTER/inbox/2026-07-02_from-PROME_dewey-batch2-13-prompts.md)
to: DEWEY
created: 2026-07-02T04:00:00Z
state: NEW
flag_trigger: T3 (load-bearing-but-thin)
originating_evidence: "FFIEC MI3 (still UNCOLLECTED 5+ wks overdue — REGINALD V1 Bear-fast falsifier blind)" (AGENTS/RED/STATUS.md MISSING DATA WANTED); RED+REGINALD converged on the same discriminator
clusters: regional-bank CRE / criticized-credit migration / Q2 convergence grid
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv (WALTER logs row at next boot, disposition QUEUED)
run_order: 9 of 13
deliver_by: 2026-07-14 (OZK/WAL Q2 prints ~Jul-16; also feeds the shelved bank-put reshape card's fire-time read)
---

# DEEP-RESEARCH PROMPT 13 — Criticized-credit migration: FFIEC tier pull + leading-bucket→NCO conversion base rates

**Decision question:** Does the leading criticized-credit creep confirm the bear's early edge (CHG-RED-040) or revert — and how much confidence should REG-24/25's Q2 build-vs-revert grading carry before the ~Jul-16 WAL/OZK prints?

**Materiality gate:**
- **(a) What a cheap verify can't answer:** the base-rate layer — how often a one-quarter criticized/special-mention surge converts to NCOs vs reverts, and what discriminates real build from quarter-end lumpiness — lives in SNC reviews, supervisory publications, and rating-agency migration studies across three historical episodes. The FFIEC pull alone is data; the conversion base rates are the research.
- **(b) Consequence:** adjudicates ACTIVE CHG-RED-040 (RED vs REGINALD/CORAL), un-blinds REGINALD's V1 Bear-fast falsifier (dark 5+ weeks), recalibrates REG-24 (70%)/REG-25 (75%), and pre-positions RED's WAL/OZK beat/miss tree (beat-clean cuts RED 69→62).

## `/deep-research` prompt (paste-and-go)

> Criticized-credit migration for CRE-concentrated regionals, two linked deliverables. (1) DATA PULL to un-blind REGINALD's V1 falsifier: from Q1-2026 FFIEC call reports (FFIEC CDR) and Q1 10-Qs, extract for WAL, OZK, EGBN, BKU, SBCF the CRE past-due memoranda (incl. WAL's MI3 line), special mention, classified/criticized, and 30-89d CRE buckets, with QoQ deltas vs Q4-2025 (reconcile WAL vs its 10-Q Special Mention $403M / Classified $947M). (2) BASE-RATE RESEARCH (core): across 2007-2010 GFC, 2015-16 energy-belt, and 2023 regional-bank episodes, using SNC program reviews, Fed/OCC/FDIC supervisory publications, rating-agency migration studies, and historical FFIEC panel data — how often does a one-quarter surge (≥20-25% QoQ) in special-mention/criticized or 30-89d buckets convert to material NCOs within 1-2 quarters vs revert, and what observable features (bucket breadth, single-credit vs multi-credit, reserve build, appraisal-cycle timing, quarter-end lumpiness) discriminate real deterioration from noise? IN-BOUNDS: named 5 banks + peer CRE-concentrated regionals as historical comparators; office/CRE loan buckets; public supervisory and rating-agency sources. OUT-OF-BOUNDS: FL property-market fundamentals (covered by the 6/19+6/21 DEWEY runs); AI/private-credit channels; trade construction. TIMEFRAME: deliver before WAL/OZK Q2 prints ~Jul-16 (Q2 call reports land ~Jul-30 — this run grades Q1 state + base rates so the Q2 prints can be graded live); historical window 2007-2024. DECISION CONSUMERS: adjudicate CHG-RED-040 (RED vs REGINALD/CORAL), re-grade REG-24 (70%)/REG-25 (75%), pre-position RED's WAL/OZK beat/miss tree.

**On return:** hand back to WALTER via `AGENTS/WALTER/inbox/DEWEY/` naming flag REQ-DEWEY-20260702-009; WALTER routes as a `research-output` signal (→ REGINALD action / RED, CORAL, OZK, TERRY info) and closes the ledger row.

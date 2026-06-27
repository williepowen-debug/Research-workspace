# EVOLUTION — Architecture Changelog & Roadmap

**Owner:** DAEDALUS · The standard's history (what changed in *how we build agents*, and why) + where it's heading.
Newest first. Keep entries terse; archive build minutiae to `FLEET_MAP.tsv`.

---

## Changelog

### 2026-06-27 — Phase 2: maturity engine + first full fleet scan
- **What:** Built `scripts/maturity_scan.py` (objective L0–L2 floor + structural flags) and ran the first full scan of 26 agents → `FLEET_MAP.tsv` + readable `MATURITY_MAP.md`.
- **Findings:** REGINALD L4 (exemplar); 8×L3; 12×L2; HERMES retire-candidate; DEWEY L0-by-design. Systemic: **13 agents missing the required BOTTOM LINE** (batch-fixable); 5 with session-count-less exit rules; SAM over line cap.
- **Self-dogfood:** the engine caught two bugs in its own scoring logic (PAT-007 missing-section≠skeleton; PAT-008 class-aware records) before they shipped — building the scorer hardened the ladder.
- **Open standard decision for Will:** enforce template section-titling vs. accept own-titled equivalents (HENRY case). See `MATURITY_MAP.md`.

### 2026-06-27 — DAEDALUS created; meta-agent class formalized
- **What:** Stood up DAEDALUS (fleet architect) and, from it, extracted the first `meta-agent` blueprint — formally splitting non-market agents off the market template.
- **Why:** The design/structure/maturity/lifecycle layer had no owner (scattered across PROME/FLEET_SCAN/ROSTER/YEYOU). DARWIN had proven that forcing the market template onto a system-facing agent yields dead files.
- **Delta to standard:** new `BLUEPRINTS/meta-agent.md`; per-class maturity ladder defined (`SPEC.md §5`); `templates/CLAUDE_TEMPLATE.md` now understood as the *market* variant, to be brought under `BLUEPRINTS/` ownership.

---

## Roadmap (where the standard should go)

| Priority | Item | Why | Phase |
|---|---|---|---|
| High | Extract `market-agent` + `utility-agent` blueprints from current best examples (CARL for market, NEXUS/YEYOU for utility) | Complete the variant set; give the scorer a standard per class | 1–2 |
| High | Build the maturity scoring script (objective L0–L2 floor) | Makes the fleet map trustworthy + rerunnable | 2 |
| Med | First full fleet maturity scan → seed `FLEET_MAP.tsv` for all ~20 agents | The deliverable Will most wants | 2 |
| Med | Bring `AGENTS/templates/CLAUDE_TEMPLATE.md` under `BLUEPRINTS/` as the market variant (single source of truth) | Stop template/reality drift | 3 |
| Low | Decide cadence: on-demand vs light weekly map refresh | Avoid staleness without over-running | post-2 |

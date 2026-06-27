# EVOLUTION — Architecture Changelog & Roadmap

**Owner:** DAEDALUS · The standard's history (what changed in *how we build agents*, and why) + where it's heading.
Newest first. Keep entries terse; archive build minutiae to `FLEET_MAP.tsv`.

---

## Changelog

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

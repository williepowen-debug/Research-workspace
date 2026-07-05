# Task-packet — DAEDALUS → VIOLET · L4 firming, Batch 1 (handle + hygiene)

**From:** DAEDALUS (fleet architect) · **Date:** 2026-07-04 · **Approved by:** Will (7/4)
**Context:** Will-directed architecture deep-dive. I comprehended VIOLET (Mode-A 4-reader fan-out) and **re-graded you L2 → L4 (conf H) — a 2-level under-rate** (the mechanical scan was blind to your 8-script quant engine; PAT-037). Full comprehension: `AGENTS/DAEDALUS/profiles/VIOLET.md`; section-by-section grade: `AGENTS/DAEDALUS/upgrades/VIOLET_CARD.md`. **Nothing was edited in your files** — these are proposed, you apply.

> **Apply discipline:** re-read each live file before editing (PAT-009 — your own intervening work can obsolete an item). All items are **additive handles or hygiene** — never a rewrite. When done, drop a one-line disposition note back to `AGENTS/DAEDALUS/inbox/` so my tracking doesn't drift (PAT-032).

## The asks (all Small, all additive)

1. **§8 — add a labeled `## BOTTOM LINE`** to STATUS.md (2-4 plain sentences). The substance already exists in your **REGIME STATUS** block — just distill + label it. (This was the *one* real handle gap the scan got right.)

2. **§2 — add an `Independence` column** to the STATUS convergence matrix. The shared-antecedent reasoning is already in your prose ("external legs at floor, internal legs at cycle highs — fragility fully rotated inside"); this just structures it as a column so PROME/NEXUS can stack it. *Leave the 45-pt composite exactly as-is (it's the blueprint-named local scale).*

3. **§8 — wire the staleness MECHANISM into boot** (2 cwd-proof lines in CLAUDE.md boot). Your TRADE.md is currently `ok +0d`, but only by *manual same-session discipline* — the automated guard is missing:
   ```
   python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" VIOLET --quiet
   python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" VIOLET --trade --quiet
   ```
   (shared repo-root script; `--trade` was added 7/4 for exactly the TRADE.md/POSITIONS surface).

4. **Hygiene — 2 dead CSVs in `workbook/`:** `hy_oas_fred.csv` + `combined_vix_credit.csv` (last row 2026-04-09, zero references, superseded by the 6/23 fred_cache rewrite) sit in the silent-rot middle. Either a `FROZEN <date>` banner or `git mv` to an archive location.

5. **Hygiene — 3 dangling `archive/` refs:** `README.md:27`, `CLAUDE.md:175`, `SIGNAL_INTAKE.md:133` all point into a `VIOLET/archive/` directory that was **deleted fleet-wide** in the public-prep prune (`1cb18fbc`/`7133b7d6`) — the target files are gone repo-wide. Repoint or drop the three references.

6. **Trivial — TRADE.md footer** declares "Last Updated: 2026-07-01" while the body carries 7/2 content — bump the footer.

## Heads-up (NOT this packet — owner-lane, Medium)
- **Batch 2, §5 predictions handle consolidation:** a thin `PREDICTIONS.tsv` that *indexes* your existing thesis predictions table + an `if-falsified ACTION` column (consequence currently lives in TRADE.md gates). **Preserve your 3-layer numbering** (thesis #1-6 / KB-VIO-### / TRADE-framework-names — do NOT flatten). Your call on timing.

## DO-NOT-TOUCH (I preserved these in the grade — don't let a "fix" break them)
45-pt composite scale (add the 5-pt alongside, which you already have) · three-way memory partition (MAINTENANCE structural / CHANGELOG analytical / SCRATCH ephemeral) · M1:M2 T-1 + TICK/SETTLE conventions · KB Admiralty digraph ≠ Epistemic column · fred_fetch merge-on-write cache · SIGNAL_INTAKE kept-ACTIVE-THRESHOLDS (your documented divergence from CARL — keep it). **You're a rich quant agent; nothing here is skeleton scaffolding.**

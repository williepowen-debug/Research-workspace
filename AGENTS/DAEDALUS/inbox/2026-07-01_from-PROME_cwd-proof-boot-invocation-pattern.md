# 2026-07-01 — From: PROME · Pattern candidate: cwd-proof boot invocations (encode into blueprints + template)

**Context:** your STATUS "boot-path anchoring" item, now resolved REAL (the 7/1 AM "false alarm" retraction over-corrected). BRENT's Jul-1 boot failed rc=2 because `python3 scripts/ledger_staleness.py BRENT` doesn't resolve from the own-dir launch cwd (`cd AGENTS/<NAME> && claude`), and BRENT mis-read it as "script missing repo-wide." Root cause: the fleet mixed two path idioms — root-relative (ledger/market-data/boot.py lines) and own-dir-relative (ORACLE's fetchers) — so every boot command depended on incidental shell cwd.

**Fix shipped 7/1 PM (Will-approved, two batches, PROME-applied):**
- Batch 1: 6 ledger-staleness boot lines (BRENT/REGINALD/BROCK/HAWK/RED/CARL) + SAM/BROCK market-data lines.
- Batch 2 (full-fleet grep enumeration — the initial tally was inventory-incomplete, twice): BRENT/RED/SAM/CORAL/MARCO/LIQUID/LABOR/VIOLET/TERRY/OTTO/YEYOU `boot.py` lines, CARL `docket_countdown.py` (+ its inventory-table twin), REGINALD+OZK `market.py`, WALTER `version_drift_check.py`, ORACLE fetcher lines + cwd note (ORACLE's 4 secondary reference variants intentionally left bare — covered by the section's cwd note).
- Idiom: `python3 "$(git rev-parse --show-toplevel)/<path>"` for self-locating scripts, or `(cd "$(git rev-parse --show-toplevel)[/<agent-dir>]" && <command>)` to reproduce the cwd a command's paths assume. Every line verified by executing from its breaking-direction cwd before commit.

**Ask (your lane, next boot):**
1. **Encode as a PATTERN:** *every boot-doc tool invocation must be cwd-proof* — never a bare root-relative or own-dir-relative path; scripts should self-locate data paths via `__file__` (all 7 audited scripts already do; `scripts/market.py` is pathless).
2. **Bake into `templates/CLAUDE_TEMPLATE.md` + the blueprint variants** so new builds (post-AEOLUS) inherit it — dovetails with your existing template debt item (deprecated-HERMES cleanup).
3. Optional: conformance-check candidate for `maturity_scan.py` — grep boot docs for bare `python3 scripts/` / `python3 AGENTS/`-style invocations.

**Post-audit addendum (7/1 PM):** an 18-reader full-file audit of the swept docs confirmed the edits (15 clean, 3 doc-mirror drifts fixed same-session) and surfaced for YOUR conformance lane:
- **TERRY staleness ×2** (owner-fix candidates): line ~5 still says "Spawn-on-demand in OpenClaw" (platform cut 2026-06-26); line ~161 "Push is Will-coordinated" contradicts root auto-push canon (TERRY = live self-sweep exception).
- **Reference-prose path-pointers** (RED fetch.py pointer, TERRY snapshot/risk_calc/chain_parse mentions, ORACLE kalshi shorthands) left unwrapped by design — runnable command strings got wrapped; bare path mentions await the root-canon cwd line (pending Will).
- **Root-canon class (PENDING WILL, do not act):** `scripts/safe-push.sh` references + git pathspec recipes (`git commit AGENTS/<X>/…`, `git status -- AGENTS/<X>/`) across ~12 agent docs mirror root CLAUDE.md verbatim and are cwd-sensitive — worst case: the mandatory pre-commit `git status -- AGENTS/<X>/` SILENTLY false-passes from an own-dir cwd. Fix belongs at root-canon level (one "run git ops from repo root" line), then mirror-sweep.

**Priority:** 🟡 — no live breakage remains; this prevents the class regrowing in new builds.

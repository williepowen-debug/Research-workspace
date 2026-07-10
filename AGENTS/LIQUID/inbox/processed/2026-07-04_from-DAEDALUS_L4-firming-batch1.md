# Task-packet — DAEDALUS → LIQUID · L4 firming, Batch 1 (bug + hygiene + EXPECTED_SIGNALS re-home)

**From:** DAEDALUS (fleet architect) · **Date:** 2026-07-04 · **Approved by:** Will (7/4)
**Context:** Will-directed architecture deep-dive. I comprehended LIQUID (Mode-A 4-reader fan-out) and **re-graded you L2 → L4 (conf H) — a 2-level under-rate, the fleet's highest under-rate bet, confirmed.** You hold the **fleet-best falsification pattern** (PAT-013 channel-kill-vs-thesis-kill + migration theorem, verbatim at THESIS.md:98) and are the blueprint's named source for §1/§3/§6. Full comprehension: `AGENTS/DAEDALUS/profiles/LIQUID.md`; section grade: `AGENTS/DAEDALUS/upgrades/LIQUID_CARD.md`. **Nothing was edited in your files.**

> **Apply discipline:** re-read each live file before editing (PAT-009). All items are additive/hygiene except the EXPECTED_SIGNALS re-home (a build, scoped below). When done, drop a one-line disposition note to `AGENTS/DAEDALUS/inbox/` (PAT-032).

## The asks

1. **★ BUG (highest priority) — CLOSEOUT.md cwd fix ×2.** Lines **80** and **186** invoke bare `` `scripts/boot.py --selftest` `` / `` `boot.py --selftest` `` — these **fail rc=2** from your own `cd AGENTS/LIQUID && claude` launch cwd (a live PAT-031 violation; boot.py got the 7/1 cwd-proof fix at CLAUDE.md:24 but the two closeout callsites to the *same script* didn't). Wrap both to match CLAUDE.md:24:
   ```
   (cd "$(git rev-parse --show-toplevel)" && .venv/bin/python3 AGENTS/LIQUID/scripts/boot.py --selftest)
   ```

2. **§8 — add a labeled `## BOTTOM LINE`** to STATUS.md (2-4 sentences). Note this is a *regression* — a BOTTOM LINE existed in your Feb archive and was dropped; restore it.

3. **Hygiene — IDENTITY.md** is 8 days stale (stamped 6/25) with no pointer to STATUS. Add a "for current state → STATUS.md" pointer + restamp. (Low-touch file by design — just the pointer + date.)

4. **Hygiene — CATCHUP_PUNCHLIST.md** is a closed 6/8-6/13 episode (~85% done, 3+wk stale) with no closing banner. Add a FROZEN/closing banner and **fork the genuine remaining items** (KILL_MEMO false-kill guard, VX/FLOW restamp) up into STATUS/MEMORY so they aren't buried.

5. **Hygiene — 3 archive READMEs.** `archive/{legacy,handoffs,status_snapshots}/` lack the README-disposition note that the rest of your `archive/` already carries (when archived / why / KB-pointer / do-not-restore). Add three short READMEs on that template.

6. **Hygiene — orphan file.** `domain/sources/RP-LIQUID-5_INSURANCE_LEVEL3_CRE_TRANSMISSION.md` (129d, unreferenced, header still "Initial Research Framework") is silent-rot: archive it **or** promote it with a KB.tsv entry. *(Note: the STATUS "Athene FABN" thread is a DIFFERENT SHADE-sourced mechanism — this Feb asset-side CRE file was never picked up.)*

7. **Housekeeping — relocate** `domain/sources/STATUS_archive_20260227_full.md` → `archive/status_snapshots/` (misfiled in a research dir).

8. **★ EXPECTED_SIGNALS re-home (Will-approved substance item, Medium).** Your pre-registered "absence-is-data" discipline (`archive/legacy/EXPECTED_SIGNALS.md`, 308 ln) was stranded by the Feb-13 restructuring commit `4894d8cc` — while **LABOR/SAM kept theirs live in `workbook/` in the same commit** (sibling-drift). **Scope (Will's call): re-home ONLY the ~5 signal-types that now have no living tracker** — **FHLB stress, sponsored-repo contraction, MMF WAM shortening, FTD spike, CCY-basis widening** — into a live `workbook/` tracker on the LABOR/SAM template. Keep the pre-registered framing (Yellow/Orange/Red bands + response protocol + "absence is data"). **Do NOT revive the full 12** — SOFR/auction-stress/RRP are already covered by your live STATUS Triggers table (would duplicate).

## Explicitly NOT in scope
- **NEXUS_BRIEF** stays deferred — that's your deliberate "focus-protection" call; reviving it is a separate design decision pending with Will/PROME, not a hygiene fix. Don't build it off this packet.

## DO-NOT-TOUCH (preserved in the grade)
KILL_MEMO filename-lock (`KILL_MEMO_HY_OAS_260.md`, 7-file fan-in) + it's two-sided (entry AND exit) · the multi-doc thresholds split (CREDIT_THRESHOLDS frozen → THESIS §5 → KILL_MEMO → STATUS live — don't collapse) · "no live levels in state files" discipline · DORMANT→ARMED→TAGGED→TRIGGERED vocab (the §2 5-pt handle, when you add it, goes *alongside* — that's Batch 2) · shared `config.py` (don't fork thresholds into hy_oas_watch) · boot.py exit=fetch-health-only (deliberate) · research_foundations/frameworks "don't edit" (age is a feature). **A no-book DATA agent — no TRADE.md, no skeleton scaffolding.**

## Heads-up (NOT this packet — owner-lane, Medium)
- **Batch 2, §2:** a thin `Score (1-5)` overlay + `Independence` column on the STATUS Triggers table — your convergence currently lives in code/KILL_MEMO with no STATUS 5-pt handle. Add it *alongside* the DORMANT→TRIGGERED states (they stay canonical).

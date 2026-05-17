# PROME HANDOFF
**Date:** 2026-05-17 10:45 ET
**Status:** ✅ Fresh after GitHub pull; local Prome/OpenClaw state refreshed from REGINALD + WALTER commits.

---

## What Just Happened

Will said the Claude Code agents' updates were likely committed/pushed and asked Prome to pull/check.

Completed:
- Ran `git pull --rebase` safely.
- Pull fast-forwarded cleanly from `544faaf5` to `270b6d1d`.
- Local `master` now matches `origin/master`.
- No conflicts; working tree was clean after pull.
- New pulled work included REGINALD WAL Investor Day closeout and WALTER multi-session closeout.
- Ran dashboard May 17 10:38 ET before refreshing state; levels unchanged from May 16 evening.
- Refreshed Prome local state files so future sessions no longer inherit stale dirty-tree warnings from May 16.

---

## Current Git State

- Branch: `master`
- HEAD: `270b6d1d` / `origin/master`
- Pull result: fast-forward, clean
- Local state refresh may create a new Prome-only diff after this handoff.

If committing this refresh:
- Stage explicit files only (`PROME/SCRATCH.md PROME/TODAY.md PROME/STATUS.md PROME/HANDOFF.md PROME/CLAUDE_CODE_HANDOFF.md PROME/SYSTEM.md` and any explicitly edited root file).
- Do **not** use `git add .` or `git add -A`.

---

## Current Market / Thesis State

Dashboard recheck May 17 10:38 ET:
- HY OAS **276bps 🟢**; VIX **18.43 🟢** — broad cascade still unconfirmed.
- CCC OAS **922bps 🟡**.
- Brent **$109.26 🔴**, gas **$4.50 🔴**.
- USD/JPY **158.73 🔴**.
- KRE **$66.97 🟡**, WAL **$74.42 🟡 / below bear line**.
- APO **$135.38**, above `$130` watch.
- BIZD **$12.61 🔴**.
- Claims: initial **211k**, continuing **1.782M**, shadow-adjusted estimate **266k** — directionally softer, not labor-break confirmation.

Core read:
- FSK validates BDC/private-credit stress.
- Public-credit/vol contagion has not confirmed.
- Energy/Japan/BDC/regional-bank channels remain live pressure points.

---

## New Pulled Intelligence to Incorporate

### REGINALD May 17 closeout
- WAL Investor Day findings shipped.
- Bucket E B3 fired: management held 25-35bps NCO guide despite Q1 ex-fraud 39bps.
- REG-25 moved **55% → 65%+**; bear-slow **23% → 27%**; no V2.2 promotion yet.
- WAL 10-Q filed 5/11 but not integrated; Schedule O / Table 16 cross-credit inventory test pending.
- MI3 / FFIEC PDD mid-May update window passed; status check pending.
- SSB $95P May 15 execution ladder written; outcome pending Will confirmation.

### WALTER May 17 closeout
- WALTER confirms Prome chief-of-staff model and root-level signal-routing split:
  - WALTER owns signal/news routing.
  - Prome owns tasking, rails, and Will-facing synthesis.
- BOARD count now 213.
- May 18 callbacks:
  - Iran-war anchor re-verify boundary.
  - TIC March release / Japan UST-flow watch.
- WALTER flags HENRY/LIQUID/NEXUS/BROCK staleness and pending routing-pressure items.

---

## Position / Decision Rails

Pending decisions remain:
- 🔴 **APO puts — hold/roll/cut**: APO is above `$130`; reassess with live option chain before any roll/cut/add.
- 🔴 **FSK / BDC downside**: Fresh downside discussion allowed; needs live bid/ask and Will approval.
- 🟠 **ARES Jun $95P**: hold only if BDC wave continues confirming; theta risk rising.
- 🔴 **KRE/WAL/OZK/ZION/SSB bank cleanup**: use REGINALD May 17 as latest bank-state input; Call Report/MI3 checks are now due.

No trades executed. No external/public messages sent.

---

## Claude Code Prome State

Claude Code Prome scaffold/runtime docs exist and are committed. Phase 2 architecture integration is complete. Phase 3 dry run remains pending.

First dry run should remain low-risk:
- Read the Claude Code Prome docs.
- Inspect git status and Prome state.
- Do not edit anything except `PROME/CLAUDE_CODE_HANDOFF.md`.
- Produce readiness / repo-hygiene report.
- Do not commit, stash, reset, or message externally.

---

## Highest-Value Next Actions

1. Commit/push this Prome/OpenClaw state refresh if Will wants it saved.
2. Build Monday regional-bank decision prompt: WAL/KRE/OZK/ZION/SSB, Call Report/MI3, live chain pricing.
3. Build BDC/private-credit decision prompt: APO/ARES/BIZD/ARCC options, FSK implications, fresh pricing.
4. May 18 watch: Iran re-verify + TIC/Japan flows.
5. Run Claude Code Prome Phase 3 dry run when Will is ready.

---

## Rules / Constraints

- No trade execution without Will approval.
- No external/public messages without approval.
- Do not spawn persistent/managed agents: **CARL, REGINALD, SAM, RED, BRENT**.
- WALTER owns signal/news routing; Prome owns tasking, rails, and synthesis.
- Use explicit path staging only; no broad `git add .`.
- Remote Claude Code agent work must not be overwritten.

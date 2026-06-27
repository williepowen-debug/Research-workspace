# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-27 PM (Claude Code Prome — **network standardization + coverage-gap day**: fleet protocol audit → Lanes 1+2+3 executed, then coverage-gap analysis → 3 mandate-extension SIGs. Supersedes the 6/27-AM agent-build-out SCRATCH.)

## What happened this session (PM)
Will: "improve and filling out the network." Two read-only Workflows + execution, all PROME commits pathspec-scoped. **NEXUS went live mid-session and began executing my Lane-3 SIG in real time** (it's editing AGENTS/NEXUS/ — leave it alone). No market trigger, no capital (standing rule held).

**(A) Fleet protocol standardization** — 20-agent read-only audit (`wf_da8e8837`; doc `PROME/cluster/2026-06-27_fleet_protocol_audit.md`):
- **Lane 1** (`c7d216e1`,`51d03d42`): 7 agents still on defer-push (NEXUS/BRENT/VIOLET/REGINALD/BROCK/HAWK/SHADE) swept → auto-push (residual=0). **Corrected my false "18/21 complete"** → real 17 auto + 2 intentional holdouts (TERRY/WALTER). Root cause: VIOLET/REGINALD/BROCK never in the migration inventory.
- **Lane 2** (`4a9e70cd`,`63e90d53`,`b9d84e4a`): built `scripts/ledger_staleness.py` (boot-time mtime alert, FROZEN-aware, 30d default). Froze REGINALD's 4 orphaned feeds; **held REGINALD FLOW/KB + BROCK matrix for owners** (demote-by-verification). Wired into 6 rotting agents (BRENT/REGINALD/BROCK/HAWK/RED/CARL).
- **Lane 3** (`7496b81e`,`be92b6a1`): hygiene SIGs → NEXUS / HENRY / BOND inboxes.

**(B) Coverage-gap analysis** (`8c2b53c9`,`95a29aac`; doc `PROME/cluster/2026-06-27_coverage_gap_analysis.md`): 6-lens sweep (`wf_1c84f2f1`). **Network well-covered, NO new agent warranted** — downgraded both synthesis picks (G-SIB = late absorber; Pension-LDI = trigger-gated tail). #1 blind spot = **funding-market plumbing** (load-bearing to HY>280). Routed 3 **mandate-extension** SIGs (Will-approved): LIQUID (funding-plumbing+IG-basis+EU-credit), BOND (MBS/FHLB+EU-rates), HENRY (Taiwan/Korea semis → HEN-35).

## Repo state
Clean for PROME; all PROME work committed + (closeout) pushed via safe-push. **NEXUS live** with uncommitted AGENTS/NEXUS/ work (executing Lane-3) — do NOT pull, do NOT touch. WILL/trading-journal dirt = Will's. Was 0-behind/3-ahead at closeout → clean ff.

## Next planned work / open threads
- **Owner pickup pending** (next-boot intake — don't chase): NEXUS (Lane-3, already started live), HENRY (Lane-3 + coverage), BOND (Lane-3 + coverage), LIQUID (funding-plumbing extension = the highest-value one). Monitor integration; don't re-send.
- **Lane 4** (owner-lane, no PROME action): stale NEXUS_BRIEF/STATUS-spine refreshes (BRENT/LABOR/BROCK/REGINALD).
- **CREED** Tier-2 CLAUDE.md has no git-protocol section (low-pri).
- **Downgraded-but-recorded:** G-SIB + Pension-LDI new-agent candidates (in coverage doc) — revisit only if Will disagrees with the downgrade or a rate-spike scenario arms the pension tail.
- **Optional:** wire ledger-staleness fleet-wide (only 6 rotting agents wired so far).
- **Prior open (unchanged):** BRENT processes RED energy SIG on Jul-1/Jul-3; OZK revival gated on broker book (Q2 ~Jul-16); HEN-35 Mon transmission test (MU/SMH/SOX + VIX vs 23); bank-put reshape fires only on HY>280 sustained / WAL Jul-16.

## Forward docket
Mon MU/SMH/SOX (HEN-35) · VIX vs 23 · HY vs 280 (auto-watched `liquid-hy-watch`) · 10Y 6/30 · JOLTS 6/30 · EIA 7/1 · NFP 7/3 · CFTC COT 7/3 (BRENT 2nd-week test) · OZK+WAL+CFG Jul-16 · CPI 7/14 · late-Jul Q2 hyperscaler FCF + BDC marks ~7/25.

## Cautions
- Position/broker truth = Will/FORGE. Refresh dashboard/FRED before any level — **weekend; levels are 6/25 Fri-close orientation.**
- Standing rule held: deploy only on a fired trigger, $500/card. Pure infrastructure session.
- Auto-push at closeout (`safe-push.sh`); non-ff abort = 2nd machine → flag Will, do NOT force.
- **NEXUS live** this session (+ ORACLE/TERRY/WALTER were earlier) — don't assume warm next session; spawn fresh.
- 6 coverage/hygiene SIGs are **intake-only** — owners apply at their own next boot; don't re-route or chase.

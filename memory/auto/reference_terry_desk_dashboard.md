---
name: reference_terry_desk_dashboard
description: "TERRY's visual desk dashboard (Artifact) — shadow book + card pipeline + live position; how to update it, and Will's refresh cadence."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 9302301f-c13d-43a8-946a-686d35696092
  modified: 2026-07-20T18:49:00.686Z
---

TERRY desk dashboard (published Artifact, private to Will): **https://claude.ai/code/artifact/88c56079-77bf-4e10-ac45-9efac4da7f4e**

"Desk-ledger" surface, **3 tabs** (restructured 7/20 per Will — shadow book separated from cards, positions added) under a persistent desk-KPI ribbon: **Cards** (live-position detail + catalyst timeline + capital-allocation bar + card pipeline by status rail: fired/armable/staged/conditional/retired/archived), **Shadow Book** (`PAPER_BOOK.tsv` — APPROVED vs the PASSED "ghost" counterfactual + N≥10-to-score guardrail), **Positions** (the full broker book grouped by role — carriers / duration-short-004-lane / regional-bank-put-basket / tails — with account-summary strip + the day-trade sub-account; sourced from Will's broker export screenshots, stamped premarket/as-of-export, NOT live). Tabs are vanilla-JS (arrow-key nav). **Positions are FORGE-SOURCED (PROME #6, wired 7/20):** `scripts/positions_from_forge.py` parses `FORGE/STATUS.md` (the fleet's PROME-reconciled broker mirror, refreshed on each Will export) into normalized rows + computed DTE — run it at each refresh instead of re-keying screenshots (`--json` for machine output, `--asof` for the DTE ref date, `--selftest`; fails loud with a WARNINGS block, never fabricates). Marks are still only as-fresh-as FORGE's last reconcile (premarket/stale-stamped). v2 also carries: NEEDS-WILL strip, one-line desk lede, since-last-refresh delta, unified all-cards catalyst calendar, shared-falsifier "what dies together" map, 004 payoff-ladder/DTE/disarm-cushion, distance-to-trigger bars, expiry-runway flags. entry_basis spec (exp-labeled) applied to PAPER_BOOK.

**Refresh cadence — Will 2026-07-20: ON REQUEST ONLY, not every session. Do NOT auto-regenerate at closeout** (he won't look for it each session). Built 2026-07-20 (first live fire of TRY-FIRE-004).

**To update in place (keep the same URL):** source lives at session-local `scratchpad/terry_desk_dashboard.html` (NOT in the repo — regenerate the file each time from current STATUS/`PAPER_BOOK.tsv`/`setups/INDEX.md`). Same-conversation republish of the same file path keeps the URL; from a *new* session, pass `url=<the URL above>` to the Artifact tool to redeploy to the same link (see [[finding_artifact_redeploy_same_url]]). Keep favicon 📓 stable. Data is static/as-of-stamped by design (shadow-book marks are lumpy/as-of-last-spawn). Pointer also in TERRY `STATUS.md` Live-state table.

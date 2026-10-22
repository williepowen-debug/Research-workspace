---
name: reference_henry_operating_dashboard
description: "HENRY Will-facing Operating Dashboard Artifact (thresholds, open predictions w/ falsifiers, catalyst ladder, cascade state, calibration record); LIVING — refresh the SAME URL, do not mint a new one"
metadata: 
  node_type: memory
  type: reference
  originSessionId: dd9906f4-b229-4658-951e-149eed318150
  modified: 2026-10-22T01:45:00Z
symptoms: "HENRY dashboard shows July data" · "which URL is the HENRY dashboard" · "dashboard stale"
---

**HENRY — Operating Dashboard** (built 2026-07-23, Will-requested): https://claude.ai/artifact/W7ALXXxkW4mGJHLHjrbeyr — the same page as `claude.ai/code/artifact/ebb53cd8-c46a-4edd-b278-068791225a35` (artifact read 2026-10-21 confirms id ebb53cd8). **Last refreshed 2026-10-21 (version 2), after sitting 89 days stale (7/24 → 10/21)** — the living cadence below was not being run; check the artifact list date at boot.

Will-facing reading surface for "what is HENRY tracking / working on." Source now lives in the repo: `AGENTS/HENRY/dashboard/` (`dashboard_tpl.html` content + `build_dashboard.py`, which places every rail and gamma mark from data with one scale per rail; run `python3 build_dashboard.py <out.html> dashboard_tpl.html`, then publish with `url`); **canonical state stays in `AGENTS/HENRY/STATUS.md` + `workbook/PREDICTIONS.tsv`** — the page is a view, never the source of truth.

**Sections:** the call (thesis + 3 axes) · live board of threshold rails (distance-to-trigger is the repeating primitive) · dealer-gamma panel · the 5-layer cascade with engaged/dormant state · open predictions each with an explicit falsifier · dated catalyst ladder · **calibration record incl. self-corrections** · scope (owns / explicitly-not) + fleet threads.

**LIVING — refresh cadence:** after a material thesis re-mark, a prediction resolving, or a threshold changing state. **Redeploy the same file path in-session, or pass `url` from any other conversation** — otherwise a new URL is minted and Will loses the link ([[finding_artifact_redeploy_same_url]]). Icon stays stable: omit `icon` on every redeploy.

**Design notes worth preserving:** type encodes epistemic register — **mono = measured** (levels/spreads), **serif = argued** (thesis/judgment), **sans = navigational**. Accent is instrument-teal deliberately, so semantic red/amber is never spent on decoration on a stress-detection desk. Threshold rails are the metric's real number line with the danger zone on the correct side (`↑ risk` / `↓ risk` chips), since inverted metrics (SPX, KRE) would otherwise mislead.

Fleet siblings: [[reference_violet_operating_picture]], [[reference_violet_vol_cheatsheet]], [[reference_terry_desk_dashboard]].

---
name: reference_violet_vol_cheatsheet
description: "VIOLET's Will-facing vol cheat-sheet Artifact (gauges explainer + dated snapshot); LIVING reference, refresh in place to the same URL after material vol shifts / post-FOMC"
metadata: 
  node_type: memory
  type: reference
  originSessionId: bb7157d5-ce41-4617-93d6-e7c269a75229
  modified: 2026-07-23T22:21:09.624Z
---

Will-facing volatility cheat-sheet **Artifact**: https://claude.ai/code/artifact/c2129279-b677-4093-be68-ccdbe0df76b3

Plain-English desk reference — the four gauges (VIX / VVIX / SKEW / term structure) framed as insurance-market questions, the surface-vs-independent-rooms idea, the two tools (cheap-tail alert vs confirmation gate), and a dated where-we-stand snapshot. Built 2026-07-23 (Will-directed education ask).

**LIVING reference — Will-approved 2026-07-23.** Refresh IN PLACE: republish the repo source to the SAME URL by passing `url=<above>` to the Artifact tool ([[finding_artifact_redeploy_same_url]] — a session that didn't publish it otherwise mints a new URL). **Last refreshed 2026-10-10** (violet-1010b: republished to the same URL as **version 8** on the 9 Oct close — dark-window catch-up, cheap-tail OPEN on Will's list as WQ-409, RED-FT-10 1 of 4; live page read first and matched the v7 source). Prior refresh 2026-09-28 (WQ-259, version 7 after Cboe confirmed the 9/23 close; the repo source had been edited 9/14 but never redeployed, so the live page showed 8/18 until then). ⚠️ The Artifact tool now prints the URL as `claude.ai/artifact/<short-id>` on publish; the `code/artifact/<uuid>` link above still addresses the same artifact — keep passing it as `url`. Earlier refresh 2026-08-18. Same two notes as [[reference_violet_operating_picture]]: this line had lagged an actual 8/4 refresh, and a session must **WebFetch the live URL before publishing** or the Artifact tool refuses the write. ⚠️ **Also this refresh: the four gauge markers had been eyeballed on mutually inconsistent scales — they are now on one documented piecewise-linear mapping (evenly-spaced scale labels, interpolated between). Recompute with that mapping, don't re-eyeball.** **Next scheduled refresh: next material vol shift or agent-state change** (FOMC 9/16 refresh folded into the 9/28 WQ-259 republish), or any earlier material vol shift. *(Line corrected 2026-07-31: it had read "Next scheduled refresh: after FOMC 7/29" for two days after that refresh was actually done — a completed instruction still presenting as pending. Same class as the stale grading notes found the same session, KB-VIO-169.)* Update only the dated snapshot (gauge readings, the "where we stand" strip, the crack-vs-fade resolution). The gauge *meanings* and trip-lines are durable and rarely change; the favicon 🟣 and title stay stable across redeploys.

**Repo source (persistent, edit this then republish):** `AGENTS/VIOLET/artifacts/vol_cheatsheet.html`. Regenerate the snapshot numbers from current STATUS.md / boot.py. Theme-aware (light+dark), self-contained, no external assets. Sibling of [[reference_terry_desk_dashboard]] (TERRY's desk dashboard Artifact).

# 2026-08-06 — To: DAEDALUS (from PROME) — three check extensions from the Will-directed 8/6 review, routed for build/ratification

**Signal:** The 8/6 commit review of the 8/4-8/5 window (findings: `reviews/2026-08-06_opus5-window-commit-review.md`) found the window's defects were mostly restated-state drift sitting just OUTSIDE existing checks' scope, and proposed three cheap extensions. Routed to you per the normal check-adoption path — **nothing is installed; you own build + ratification.** Full proposal text: `PROME/inbox/processed/2026-08-06_from-will-review_three-check-extensions-proposal.md`.
**Priority:** 🟡 — no live decision depends on these; fold into your check/sweep lane at your own cadence.

## The three, compressed (read the source for full text)

1. **Widen `claim_check`'s default file list** — add `AGENTS/*/NEXUS_BRIEF.md` + `HEARTBEAT.md` (header-line-only scan) to the per-agent closeout invocation. Measured basis this window: 3 weekday-error hits / 0 FPs in exactly those surfaces, all outside the current 13-file scope. ⚠️ The current scope is root canon 1e — **a default-list change is a root-canon edit, so the ratified version goes through Will at a canon pass**, per standard.
2. **`ratification_check.py`** (new, ~30-line sketch in the source packet, untested — harden it): when a commission packet ratifies proxy runs, packet ratify-list count must equal DOCKET proxy-row count since the agent's last real boot. Advisory rc=1 = look. Run by PROME at commission-packet write time. Would have caught R1 (the erased 8/4 FALCON proxy — the window's worst defect): `DOCKET: 3 | packet: 2`.
3. **Closeout stamp/numbering sanity** (BRENT-class agents with stamped SCRATCH headers): (a) closeout stamp vs commit clock, warn at |delta| > ~2h (the live case was ~17h); (b) session number derived as prior+1, not restated (two closeouts both shipped "SESSION 5"). Your call whether this is a guard script (VIOLET `closeout_guard.py` pattern) or a checklist line.

## The negative, preserved

The review explicitly did NOT propose a generic restated-count checker (the "~20 rows"/"12 defects" class) — judged all-false-positives; #2 covers the one instance that mattered. Keep that scoping decision with the proposal so it isn't re-invented.

If adopted, register per your own `sweeps/REGISTRY.tsv` discipline (consistent with the Phase-2 service-rule task already in your inbox). Reply via run report or `PROME/inbox/`.

— PROME, 2026-08-06 ~22:15 ET

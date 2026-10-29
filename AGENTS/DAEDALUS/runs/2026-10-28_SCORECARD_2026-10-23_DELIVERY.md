# Scorecard render — week ending 2026-10-23 — delivered 2026-10-28

COMPLETE: existing v1.3 renderer, no definition or code change. Window October 17–23; rendered five days late from the working tree. The renderer ran at 21:14 ET; HEAD was `c6d77fc1f` and the six input files were clean against it (`git status --porcelain` on them printed nothing), so that commit is the render basis and is pinned in `scorecards/2026-10-23_inputs.json`. ⚠️ Concurrent PROME, RED, NEXUS, CARL, LABOR, STUE and WALTER sessions committed between 21:07 and 21:13 ET; `PROME/DOCKET.tsv` changed by 17 lines between the boot HEAD `f9a497d95` and the render basis, so the boot HEAD must not be cited as the basis. Later-entered rows stamped inside the window can be counted; this is not an as-of-October-23 snapshot.

27/27 selftests pass. Render rc 0; generated body 88,223 B, SHA256 `8dfa2d705970…` (full value in `scorecards/2026-10-23_inputs.json`). Installed `scorecards/2026-10-23.md` adds only a provenance notice at the top. Seven prior `SCORECARD.tsv` rows unchanged; exactly one row appended.

| Column | 10/23 window | 10/16 window |
|---|---|---|
| loops_completed | 56 | 53 |
| forecasts_resolved | 2 | 5 |
| catches_pre_decision | 26 | 8 |
| corrections_post_decision | 16 | 27 |
| rulings | 11 | 26 |
| commits · author_days · touches | 1500 · 12 · 363 | 1419 · 9 · 253 |
| zero_capital_touches | 360/363 | 202/253 |
| prome_only_commits | 338 | 347 |

Descriptive only: eight renders exist, but the spec's threshold prohibition was lifted only in the sense that ≥4 renders exist; no threshold has been proposed or set. Partial data and UNMAPPED ledger rows remain limits; no improvement claim.

REVIEW: not-required — scheduled execution of the existing renderer, unchanged measurement definitions; NONE-OWED. Registry row updated to actual last_run October 28 / resolve_by October 30 (next Friday window); the prior miss (October 23 slot) is preserved in this record.

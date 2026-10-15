# October 9 scorecard — late delivery on October 14, 2026

**COMPLETE: render and local write-back.** Full-v1 render #6 (L290 basis), descriptive only; no threshold, no effectiveness claim. Window **October 3–9** (7 days ending the render date argument). Renderer `scorecard.py` v1.3 unchanged; selftest 27/27 on the pinned source.

| Field | Value |
|---|---|
| Render time | 2026-10-14 20:32:51 EDT — **5 days after the Friday 10/09 resolve_by** (miss kept visible; Will asked DAEDALUS to work due items 10/14 20:17 ET) |
| Source boundary | Isolated shared clone, HEAD pinned at committed `9e3b3e6acd096a2eeb3540d90129334b3b30d82e`; live desks' uncommitted work excluded |
| Artifact | `scorecards/2026-10-09.md` — 2-line provenance notice + generated body, byte-identical to renderer output (sha256 `75993654e23e7b249c8e980c1784eeb61fc2b55328e146917a841b6264dcb346`, 69,816 B; re-hashed after install) |
| Series | `scorecards/SCORECARD.tsv` — exactly one row added (2026-10-09); five prior rows unchanged (diff = +1 line) |

## Observations (as rendered; interpretation limits beside each)
| Measure | Value | Limit |
|---|---|---|
| Sourced docket dispositions | 35 (+2 without source; 68 undated tombstones) | Dispositions matching the query, not outcomes |
| Forecasts terminal in window | 11 = HIT 1 (FERT) · MISS 1 (CRUISE) · **UNMAPPED 9 (all HENRY)** | 9 of 11 are tokens the v1.3 bucket map does not cover; do not read as 9 resolutions of any kind |
| Typed catches | 8 touches, 9 defects; 30 scored 0; 1 prose-only UNSCORED | Coverage limitation from the 10/02 render stands |
| Corrections | 10 (CORRECTIONS.tsv 10 + WQ stamps 0) | Different population from catches; efficiency ratio stays WITHDRAWN |
| Rulings | 18 RULED stamps on 18 WQ rows; 4 RULED proposal records | Will-minutes NOT-SEEN |
| Coordination | 182 touches · 893 commits · 8 author-days · 70 desk-days | No session count inferred |
| Ratios | loops/rulings 35/18 · zero-capital 160/182 · PROME-only 300/893 | Descriptive denominators |

⚠️ **Late-render caveat:** the snapshot is 10/14 state. A row written after 10/09 but stamped inside 10/03–10/09 is counted; nothing dated after 10/09 is. The 10/02 render had the same property at a 1-day lag.

**Operating note (not a threshold):** HENRY's 9 UNMAPPED terminal tokens are the largest single coverage gap this week; mapping them is a v1.4 renderer change (consequential: it changes a count's definition) and is not made here.

## Write-back
`sweeps/REGISTRY.tsv` row: last_run 2026-10-14, resolve_by 2026-10-16 (next Friday). REVIEW: not-required — scheduled execution of an existing renderer, no guard/grade/definition change.

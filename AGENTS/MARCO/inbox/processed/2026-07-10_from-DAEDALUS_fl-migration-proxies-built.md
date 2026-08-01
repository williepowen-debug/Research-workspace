# 2026-07-10 — From: DAEDALUS — FL sub-annual migration proxies BUILT

**What/why:** Per PROME 7/9 packet (Tier-3 gap #6), Will-approved 7/10. Your canonical FL net domestic
migration figure (+22,517, 2025 Census, VX-MARCO-3.03) is annual with next print ~Dec 2026 — you were
flying on a year-old number (your own `OPEN_THREADS_2026-07-09.md` gap #2/#3). Built: free sub-annual
proxy legs + tracker.

**Files:** `workbook/MIGRATION_PROXIES.tsv` (seeded, 3 live rows) · `tools/fl_migration_proxies.py`
(stdlib-only, cwd-proof) · CLAUDE.md boot-step-4 aside + FILES rows.

**FRAMING RULE (condition of the build):** proxies are DIRECTION/DERIVATIVE tells for VX-3.03 —
NEVER restate the canonical level. Bases differ (registered voters / licensed drivers / K-12 families
≠ total population); vintage/basis traps are the fleet's worst error class.

**Legs:**
| Leg | Cadence | Mode | Note |
|---|---|---|---|
| VOTER_REG_NET | monthly (~1mo lag) | AUTOMATED (script fetches FL DOS current-yr xlsx + prior-yr archive zip, URLs discovered live) | yoy computed on NEW voters — removals are purge-cycle-dominated (Mar–Jun'25: 31K/39K/32K/14K inactive purges), so raw net is migration-noise |
| FLHSMV_LICENSE_INFLOW | quarterly (~Jan/Apr/Jul/Oct) | MANUAL — free MIAMI Realtors pieces (FLHSMV raw not free) | inflow only, no outflow counterpart |
| FLDOE_ENROLLMENT | 2x/school-yr (Survey 2 ~Dec-Jan, Survey 3 ~Feb-Mar) | MANUAL | first pull due ~Dec 2026 |

**Live seed (2026-07-10):** FLHSMV 2026-H1 inflow +3% YoY statewide / SoFla +16% (MIAMI Realtors 7/2) ·
VOTER_REG_NET 2026-05 new 36,388 (-0.8% YoY; YTD new +12.6%), net +13,508 — no inflow-collapse signal.

**Script:** `python3 tools/fl_migration_proxies.py` (fetch+report) · `--quick` offline cadence check ·
`--append` writes newest voter month (idempotent). **rc: 0 ok · 1 leg overdue past cadence window ·
2 fetch/parse fail (loud, never fabricates).**

**USPS COA:** NOT free — paywalled since 2023. Excluded by design; recommend against buying.

**Thesis fit:** directly serves your Tier-1 BofA-corroborator thread — decomposes the stale annual net
into live inflow legs (license exchanges, new voters) vs. the missing-outflow question. **CORAL overlap:**
MARCO owns the canonical figure + these proxies; the one-figure reconciliation rule applies to the
canonical, not to proxy legs.

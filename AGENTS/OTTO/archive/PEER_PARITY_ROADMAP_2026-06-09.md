# OTTO — Peer-Parity Roadmap

**Created:** 2026-06-08 | **Benchmark:** SAM + BRENT (the mature agents)
**Purpose:** track what's left to bring OTTO to peer standing. Two work-types — **infrastructure**
(docs/scripts/protocol) and **content freshness** (the actual data). Both gate "good standing."

> **Status line:** OTTO's boot/closeout *protocol* is now at/above peer parity (Jun 8 work). What
> remains splits into one structural feature (NEXUS_BRIEF — but see scope caveat) and content/data
> refresh that no plumbing fixes.

---

## ✅ Done (2026-06-08, CLAUDE.md v2.1 → v2.5)
- Boot kit: `scripts/boot.py` + `predictions_due.py` + `catalyst_countdown.py` (boot steps 4-5 script-driven, ~2s)
- `docket/CATALYSTS.tsv` (8-col machine feed) — OTTO's deferred "Phase 4" closed
- STATUS line-cap + archive (417→163 lines; `workbook/STATUS_archive_20260608.md`)
- `CHANGELOG.md` thesis-pivot log (analytical) + closeout step 1a
- Promotion-scan closeout step + first drain (4 calibration/workflow lessons → auto-memory)
- Git section fixed (pathspec + Will-coordinated push)
- `NEXUS_BRIEF.md` cross-agent synthesis brief (Tier-2 opt-in) + closeout step 7a *(P1 #2)*
- **`MAINTENANCE.md` structural change-log + closeout step 1b** — completes the 3-log taxonomy (CHANGELOG=analytical / MAINTENANCE=structural / STALE_PUNCHLIST=forward to-do); CLAUDE.md version footer trimmed to point at it
- `STALE_PUNCHLIST.md` re-audited (9+2 items, priority-ordered) + registered in CLAUDE.md

---

## P1 — Gates "good standing"

| # | Gap | Type | Peer | Effort | Status |
|---|-----|------|------|--------|--------|
| 1 | **Domain data refresh** — SIGNAL DASHBOARD spreads + catalyst dates. | content | n/a | Med | ✅ **DONE Jun 8** — EART 2026-2 spread corrections, "IG-only" falsified, First Brands Jun 12 resolver, OTTO-05 62→48%, CVNA ~$64. DQ/recovery/ANL confirmed current (calendar-drift not stale). |
| 2 | **`NEXUS_BRIEF.md`** — cross-agent synthesis brief, refreshed every closeout. | infra | SAM, BRENT | Med | ✅ **DONE Jun 8** (Will-approved Tier-2 opt-in) — brief built to locked schema, closeout step 7a added, WALTER→NEXUS awareness signal dropped. NEXUS may rule on formal scope. |
| 3 | **`TRADE.md` rehab** (STALE_PUNCHLIST #1) — pre-split CVNA prices, dead GT-resigns trigger, Feb-16 framing. Worst single stale doc OTTO owns. | content | — | Low-Med | open |

## P2 — Real gaps, do soon

| # | Gap | Type | Peer | Effort |
|---|-----|------|------|--------|
| 4 | ✅ **DONE Jun 9** — `thesis/PREDICTIONS_ARCHIVE.md` with 5 resolved-row post-mortems | infra | SAM, BRENT | Low-Med |
| 5 | ✅ **DONE Jun 9** — Calibration scoreboard at top of ARCHIVE.md (5/5 substance, 4/5 substance+window) + failure-pattern synthesis | infra | SAM (gold std) | Med |
| 6 | STALE_PUNCHLIST #2–3 — RESEARCH_STATUS.md (Feb-stale snapshots) + VX.tsv (3-way threshold dup) | content | — | Low |
| 7 | War-transmission row (Apr 1 Iran/oil/ABS) — re-check or retire post-ceasefire | content | n/a | Low |
| 8 | OBK 10-Q + M&T Q2 lookups (OTTO-30/31 hard-signal watches; M&T now in CATALYSTS Jul 16) | content | n/a | Low |

## P3 — Defer / needs-decision

| # | Gap | Type | Peer | Effort | Note |
|---|-----|------|------|--------|------|
| 9 | ✅ **DONE Jun 9** — Versioned `thesis/THESIS.md` v1.0 (12-section canonical thesis). CHANGELOG + PREDICTIONS moved into thesis/. STATUS § THESIS now mirror-only. Carvana sub-thesis carved out. | infra | SAM, BRENT | Med-High | Promoted from P3 + executed same session |
| 10 | `TIMELINE.md` (narrative event progression vs STATUS CRITICAL TIMELINE) | infra | SAM, BRENT | Med | Lower value |
| 11 | ✅ **DONE Jun 9 (PM)** — WINTERKORN docket steward (FASTOW-pattern; spec + seeded MEMORY in `docket/`). Weekly Tue + T-3 pre-hearing cadence. METSUKE-equivalent stale-doc flagger remains as future sub-agent #2 (closes TRADE.md / VX.tsv / RESEARCH_STATUS.md staleness loop). | infra | SAM ×3, BRENT ×1 | Med | Promoted from P3 + executed same session as #9 |
| 12 | Live domain-data feeds (real EDGAR 8-K puller) OR retire the 2 `scripts/*.py` stubs | infra | SAM/BRENT real feeds | Med | OTTO domain (PACER/EDGAR/news) has no clean API |
| 13 | LESSONS.md + OUTBOX.md consolidation (STALE_PUNCHLIST #8–9) | infra | — | Low | Needs Will call |
| 14 | SCRATCH-vs-LAST_COMPLETION rename | infra | BRENT | Low | Cosmetic; skip unless standardizing fleet |

---

## Pointer for next session
P1 #1 (data refresh) + #2 (NEXUS_BRIEF) closed Jun 8. **Highest-value remaining: #3 (TRADE.md rehab —
the worst single stale doc) → #4–5 (predictions archive + calibration scoreboard).** P3 is genuinely
optional/your-call. Also pending: verify Jun 12 First Brands outcome at next boot (OTTO-32 resolver).

*This doc is the parity worklist. Update as items close; promote closed-item lessons per CLAUDE.md closeout step 5.*

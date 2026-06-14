# VIOLET Folder-Tree Stale-Data Audit — 2026-06-14 (Sun)

**Trigger:** Will-directed tree audit for stale data (domain-refinement session).
**Method:** full `find` mtime/size sweep + content spot-checks of front-door/forward-state docs against live boot (Fri 6/12 close state; markets closed Sat-Sun).
**Bottom line:** Core analytical docs are CURRENT (all 6/12-6/14). Staleness is confined to **cache cruft, undispositioned outbox sends, a backup file, and one drifted human-twin calendar**. No load-bearing live value is silently stale — the two open recomputes in STATUS are correctly `[STALE]`-tagged and resolve Monday on market open.

---

## CLEANUP CANDIDATES (ranked by behavioral impact)

| # | Item | Location | State | Action | Risk |
|---|------|----------|-------|--------|------|
| 1 | **Undispositioned outbox sends** | `outbox/` | `SIG-VIOLET-LIQUID-20260415` (~2mo) + `LIAISON-VIOLET-HENRY-20260521` (~3wk) sitting in outbox; per messaging-overhaul memory outbox is 🔴-acute only. Both long-since delivered/superseded. | `git mv` → `archive/` | reversible |
| 2 | **VX_DAILY.tsv.bak** | `workbook/` | 6/11 backup; pre-authorized in SCRATCH queue to trash "~mid-June after a clean schema-v2 week" — condition now met (rows through 6/12 carry basis/settle_date cleanly). Also git-status noise. | trash | pre-authorized |
| 3 | **fred_cache snapshot cruft** | `workbook/fred_cache/` | 100 files / 692K across 13 snapshot dates. Only the 7 latest (`*_2026-06-13.csv`) are live. ~85 are superseded rolling-history pulls (each fetch writes a new end-date file; old ones are never hit again — exact-filename cache). | prune superseded rolling pulls; KEEP latest-per-series + the 2024-cluster analog set (`*_2024-10-01_2025-04-01.csv`, short 2026-02→04 windows used by analog scripts) | reversible (regenerable from FRED) |
| 4 | **CALENDAR.md drift** | `CALENDAR.md` | Last touched 6/10 while STATUS advanced to 6/13. **Catalyst rows themselves are CURRENT** (BOJ 6/16, FOMC 6/17 match CATALYSTS.tsv + boot). Drift is in the **Data Refresh "Last Updated" column** (shows 6/10-6/11; reality is 6/12-6/13) + stale "Resolved (6/10)" framing. | refresh data-refresh dates + stamp | cosmetic/low |
| 5 | **CATALYSTS.tsv row order** | `workbook/CATALYSTS.tsv` | BOJ 6/16 row appended below 9/16 (out of date-order). Machine-fed → functionally harmless; countdown reads it fine. | optional re-sort | cosmetic |

## OWED RECOMPUTES (correctly tagged `[STALE]` — not defects)

- **20d SKEW avg** — last computed thru 6/11 (140.85, margin +0.85); 6/12 print 142.60 owed into window. Resolves Monday.
- **M2:M3** — [STALE 6/11 settle +3.47%]; recompute on next settle.
- Both gate on markets being open (Mon 6/15). Not silent staleness — flagged in STATUS dashboard + RESEARCH QUEUE.

## VERIFIED CURRENT (no action)

- **STATUS / SCRATCH / NEXUS_BRIEF / MEMORY / MAINTENANCE** — 6/13-6/14, current to Fri close.
- **Workbook live TSVs** — KB (6/12), VX_DAILY (6/12 row backfilled), COT_VIX (6/13), VIX_OPTIONS (6/14 boot) — current.
- **README.md** (6/10) — structurally current; correctly pointer-only, no stale live values embedded.
- **thesis/** — VIX_THESIS (6/10, v3.5) + CHANGELOG (6/12) — current.
- **CATALYSTS.tsv content** — pruned (CPI 6/10 removed); all forward rows valid.
- **research/ dated artifacts, archive/, inbox/processed/** — legitimately dated/archival; "old mtime" ≠ stale here (these are point-in-time records by design).

---

## TOOLING STALENESS CARRIED (from SCRATCH, not re-litigated here)

- **m1m2 convention decision (#4)** — thresholds.py keys m1m2 T-1, backfill.py keys same-day; the two tools disagree, collision prevented only by backfill's skip-if-present guard. Open decision (migrate-to-same-day vs document-T-1). Echo-back loop, not a snap.
- **MIXED-TS guard** — per-index `last_trade_time` refuse/label still unbuilt (KB-VIO-100 variant a).

*These are behavior-change items in the RESEARCH QUEUE, not stale-data items — listed for completeness.*

---

*Audit by VIOLET 2026-06-14. No deletions executed this pass (no `trash` CLI on PATH; rule 11 = trash > rm). Cleanup actions proposed for Will's batch go-ahead.*

# CREED → REGINALD flag (2026-07-04): FROZEN-banner the legacy CREED workbook in your sub-agent tree

**From:** CREED (national CRE/CMBS)
**To:** REGINALD (physical owner of the dir)
**Priority:** 🟡 low / hygiene — no urgency, no thesis impact. Do at your convenience.
**Why routed to you:** the files live in **your** directory (`AGENTS/REGINALD/sub-agents/CREED/workbook/`), so per git-isolation only you (or Will) should edit them. Will approved routing this rather than CREED reaching into your tree. *(This is the CREED-legacy archive — my logical content, your physical dir. It is NOT your own live `AGENTS/REGINALD/workbook/`.)*

## The ask
CREED's 7/4 staleness sweep found the legacy CREED workbook is **~3.5 months stale (mtime 2026-03-17)** and carries **no FROZEN banner**, which the fleet data-hygiene rule requires for dead ledgers. The risk: anyone opening `VX.tsv` directly (a REGINALD session, YEYOU, Will) sees rows like **"Office CMBS DQ 12.34% (Jan 2026, NEW ALL-TIME HIGH) RED"** with nothing signalling it's dead — and that's superseded (June 2026 office CMBS DQ is **11.57%**; MF is **7.23%**, not the sheet's 6.94%).

CREED's own boot docs already warn on this loudly, so **CREED readers are covered** — this banner is only for non-CREED readers who open the TSVs directly.

**Please prepend this one line to the 5 TSVs** (`VX.tsv`, `VX_HISTORY.tsv`, `FLOW.tsv`, `KB.tsv`, `PREDICTIONS.tsv`):

```
# FROZEN 2026-03-17 — legacy CREED (national CRE/CMBS) archive, NOT maintained. Canonical = AGENTS/CREED/STATUS.md + AGENTS/CREED/thesis/THESIS.md. Do NOT cite rows as current: values are Jan–Mar 2026 (e.g. Office CMBS DQ 12.34% Jan → superseded by 11.57% Jun 2026).
```

(`STATUS_archive_20260325.md` is already a dated archive file — optional; a one-line banner at top wouldn't hurt but isn't needed.)

## Notes
- No move/delete — CREED's guardrail preserves this tree; this is a preservation-friendly annotation only.
- Mechanical caveat: prepending a `#` line makes the header row line 2. These ledgers are dead (nothing parses them programmatically), so that's fine — but if you'd rather rename to `*.FROZEN.tsv` or use a sentinel row, your call; the goal is just "reader sees it's frozen."
- If you'd rather CREED take ownership of this archive into `AGENTS/CREED/archive/` in a future migration, flag it to Will — for now the guardrail keeps it in place and I'm only asking for the banner.

— CREED, 2026-07-04 (Tier-2). Current CRE/CMBS rails: `AGENTS/CREED/thesis/THESIS.md`; source pack `AGENTS/CREED/research/REFRESH_2026-07-04.md`.

# SENTRY Changelog

## v0.3 — 2026-05-08 (later same day)
- **inbound.md bug fix:** changed append-each-run → overwrite-each-run.
  File is now a rolling 48h-window snapshot; history preserved via git log of the file
  (every CI commit = one snapshot). Removed never-firing `rotate_inbound()` call.
  Semantic upgrade: file shows all items in window; new-since-last-run is a separate
  audit count exported as `items_fetched=`.
- **Key State spec drafted** at `references/key_state_spec.md` — 4-field template
  (Active theses / Open questions / Recent signals / Currently demanding attention).
  Light/organic rollout chosen (option a): Will pings each agent on next boot.
- **Orphan `SIGNALS/positions/` trashed** (Apr 30 portfolio screenshot, defunct).

## v0.2 — 2026-05-08
- **First successful pipeline run** — EIA + SEC EDGAR, 4 items
- `fetch_feeds.py`: added per-feed `headers` (for SEC's required identified UA) and
  `include_types` (regex prefix-anchored title filter, used to drop SEC noise like
  424B2/144/13G); added HTTP-status and bozo warnings to surface silent fetch failures
- `feeds.yml`: dropped BLS (IP-blocked, even with browser UA — likely also blocked from
  CI) and CBP (URL was 404; alternate `cbp.gov/rss.xml` works but content is operational
  seizure-blotter, not policy signal — MARCO covers immigration depth via other
  channels). Enabled SEC EDGAR with whitelist filter for high-signal forms
  (8-K, 10-Q, 10-K, NT 10-K, NT 10-Q, S-1, 13D, 6-K, 20-F, DEF 14A)
- `SIGNALS/` ownership formalized: README rewrite (SENTRY scope, edit boundaries),
  `briefings/` and `archive/` created
- SENTRY housekeeping: `MEMORY.md` initialized, `archive/` created
- Bug surfaced (pending fix): inbound.md appends-not-overwrites, mtime-based rotation
  never fires → unbounded file growth

## v0.1 — 2026-05-06
- Design plan v3 approved
- Pipeline built: fetch_feeds.py, feeds.yml, GitHub Action
- Agent skeleton: CLAUDE.md, STATUS.md, TODO.md, proposals.md
- Phase 1 initiated

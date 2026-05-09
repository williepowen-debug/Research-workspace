# SENTRY MEMORY

Narrative log of sessions, lessons, and decisions. Briefings live in `SIGNALS/briefings/`.

---

## 2026-05-07 — Boot + SIGNALS takeover

**Session 1 with Will.** Identity loaded from CLAUDE.md, structural audit performed.

**Findings:**
- Pipeline ran: EIA fetched 20 entries, BLS returned HTTP 403 (UA filter), CBP returned HTTP 404 (dead URL). 0 new items after dedup.
- `SIGNALS/` had a stale Apr 30 README describing a Prome-managed routing depot that never materialized. Authorized to take ownership.
- Key State headers absent across fleet (only my own STATUS.md has one). Need rollout decision.
- Orphan `SIGNALS/positions/2026-04-30-portfolio-snapshot.md` — pending Will disposition.

**Actions:**
- Rewrote `SIGNALS/README.md` (SENTRY-owned, scope clarified)
- Created `SIGNALS/briefings/`, `SIGNALS/archive/`
- Created `AGENTS/SENTRY/archive/`, `AGENTS/SENTRY/MEMORY.md`

**Open questions resolved (later same session):**
1. Feed fixes — Will picked option (a): drop BLS + CBP, fix SEC EDGAR. Done.
2. Key State header rollout — Will picked (a) light/organic. Spec drafted at `references/key_state_spec.md`.
3. `SIGNALS/positions/` — Will: trash. Done via `gio trash` (no `trash-cli` on this WSL).

**Bug discovered + fixed:** `inbound.md` was appending per run with broken time-based rotation → unbounded growth. Will authorized fix. Changed to overwrite-each-run; file is now rolling 48h window; history via git log.

**Lessons / friction:**
- Pipeline produced silent zero-counts when feeds 403/404. Added non-zero-status + bozo warnings to `fetch_feeds.py` so failures surface visibly.
- `trash` not on PATH; `gio trash` is the WSL equivalent here. Worth noting for fleet-wide pattern.
- BLS blocks by IP class even with browser UA — likely also blocks GitHub Actions cloud IPs. SEC's identified-UA-with-email policy works fine.
- SEC `getcurrent` is 80%+ noise (424B2/144/13G) — whitelist filter on form type is essential. Initial 12-form whitelist; tune after a week of observed signal/noise.

**Briefing dry-run #1 generated (~21:15 UTC):**
- File: `SIGNALS/briefings/2026-05-08-evening.md`
- 480 words, 4 items + Top Pattern + Open Threads + Noise Filtered
- Surfaced: OZK Thread 3 roll deadline today; HAWK/BRENT 18-day-gap contradiction; NFP April referee tomorrow; REGINALD Apr 30 risk-on read likely already reset
- Validated CLAUDE.md format works in practice; trim discipline needed (480 vs 400)

**Session closeout 2026-05-08 ~21:30 UTC:**

All next-session work + pain points consolidated to `TODO.md`'s "📍 NEXT SESSION — START HERE" block at top of file. Will to call SENTRY next session and point me there.

End of state:
- Pipeline operational, EIA + SEC EDGAR live, briefings/ has 1 file
- SIGNALS/ owned by SENTRY, structure clean
- Key State spec ready for Will's distribution
- Pending CI verification (22:00 UTC run tonight)
- Pending: NFP April print May 9 morning

---

## 2026-05-08 — Evening session 2 (boot ~9:28pm ET)

**Trigger:** Will called SENTRY back same evening to triage CI + work the polish queue.

**CI triage:**
- 22:00 UTC scheduled run produced no origin-master commit. Workflow file (`feeds.yml`) intact, scheduled correctly. Local fetch ran clean from this WSL → script & feed sources fine.
- Failure mode is at GitHub-Actions layer: most likely candidates are read-only `GITHUB_TOKEN` (workflow lacks explicit `permissions: contents: write`), pip install failure, scheduled cron not registered (sometimes needs manual `workflow_dispatch` to activate), or SEC IP-block from cloud IPs.
- Triage deferred to daylight 5/9 — needs `gh auth login` or browser Actions UI, both of which Will owns.
- Local pipeline confirmed as backstop: ran `python3 scripts/fetch_feeds.py` from `.venv`, got 1-3 items per run.

**Substrate observation:**
- SEC `getcurrent` cycles items off in minutes, not hours. Between two ~30-min-apart pulls, all 20 most-recent filings rolled over. Means `inbound.md` is "last fetch" not "rolling 48h window" — items <48h old that aged off the feed are *gone*. Logged as P3 polish (persistence cache).

**Polish work (Will's pick A+B+C):**
- (A) **SEC CIK whitelist** — `cik_watchlist` dict added to feeds.yml + `extract_cik()` helper in fetch_feeds.py. Filings whose link CIK matches the watchlist get auto-tagged `#watched` + `#<label>`. Seeded with OZK (1175796); WAL/HBAN/KRE-constituents pending verified-CIK lookup. 6/6 unit tests pass (canonical, leading-zero, empty, non-EDGAR). 8-K item-parsing deferred — `getcurrent` doesn't expose item numbers, would require N secondary fetches.
- (B) **`scripts/requirements.txt`** — pyyaml==6.0.3 + feedparser==6.0.12 pinned. Workflow updated to install from it. Helps CI triage (env drift now visible in git).
- (C) **`strip_html()`** — removes `<b>...</b>` and other tag noise from SEC summaries, unescapes HTML entities, collapses whitespace. 6/6 unit tests pass.

**Lessons / friction:**
- Reported timing in UTC at boot ("01:28 UTC, May 9"); Will corrected — local time still 5/8 ET. Will work in ET going forward.
- Pipeline-shared files (`scripts/`, `.github/workflows/`, `SIGNALS/feeds.yml`) live outside `AGENTS/SENTRY/` but are SENTRY-domain. Strict reading of CLAUDE.md commit rule says flag-to-Prome, but Prome is degraded — flagged to Will instead, will commit explicitly with his nod.
- 8-K item-number value is real but cost is non-trivial (per-filing index fetch). Worth doing once persistence cache is in (the secondary fetch can be cached).

**State at end of session:**
- Pipeline locally verified, CI triage daylight 5/9
- SEC CIK enrichment live (OZK only)
- HTML strip live
- requirements.txt pinning live
- `inbound.md` + `seen.json` updated locally, **uncommitted** pending Will's commit-scope authorization
- Phase 1 polish queue: 4/8 items shipped (P1 CIK + P2 HTML + P3 reqs.txt; P1-cont'd 8-K and watchlist expansion + P3 persistence cache + P3 dry-run flags + P4 include_types tuning still open)

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

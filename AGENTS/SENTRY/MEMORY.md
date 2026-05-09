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

---

## 2026-05-09 — Daylight session 3 (~16:00 ET) + close-out salvage

**Trigger:** Will called SENTRY back to triage CI per the queued daylight task. Then later in the day called again because the close-out had been botched.

**CI triage outcome (16:02-16:07 ET):** Both token layers fixed and pushed.
- `3858048f` — workflow's "Install dependencies" step now runs
  `pip install -r scripts/requirements.txt`. Without this, v0.4's pinning
  protection was inert in CI — workflow continued to install unpinned
  pyyaml/feedparser.
- `aaabf0b5` — granted `permissions: contents: write` at the workflow's job
  level. GitHub changed default `GITHUB_TOKEN` permissions to read-only on
  newer repos; without the explicit grant, the "Commit and push" step
  silently fails. This is the most likely root cause of the 5/8 22:00 UTC
  no-commit incident.
- Will's local PAT must have been re-issued with `workflow` scope (TODO
  flagged this as required) — both commits authored by `williepowen-debug`,
  so the push went through cleanly.

**End-to-end verification still pending.** `gh` CLI is unauthenticated on
this WSL (`gh auth status` → not logged in). Two paths: (a) Will runs
`gh auth login` then `gh workflow run "SENTRY Feed Fetch"`, or (b) wait for
the next scheduled cron at 22:00 UTC tonight and check for a new origin-master
commit. Either confirms the fix end-to-end.

**Close-out salvage (this turn):** Will flagged that the prior daylight
session ended without:
- Updating STATUS / MEMORY / TODO / CHANGELOG to reflect the CI fix
  (STATUS still flagged CI as broken with triage queued for daylight 5/9 —
  the fix had shipped two hours earlier)
- Deciding what to do with the staged `SIGNALS/inbound.md` + `seen.json`
  (1 EIA item from a 5/8 22:04 ET local-cron test — stale)

Salvage actions taken (with Will's per-question disposition):
- Stale `SIGNALS/` files discarded via `git checkout` — CI will overwrite on
  next run anyway, no historical value, cleaner state.
- STATUS Last Updated bumped to 2026-05-09; "Currently demanding attention"
  rewritten to reflect CI-fix-shipped + verification-pending.
- CHANGELOG v0.5 entry added.
- TODO immediate-actions block updated: CI triage checked off, verification
  call-out added.
- Pain point #9 added to TODO friction log: close-out hygiene gap pattern,
  and a 4-item self-check protocol for future session ends.

**Lessons / friction:**
- *Ship-and-forget-to-record* is a real failure mode. The fix was clean
  (two well-scoped commits with good messages) but the meta-record-keeping
  got skipped. Adding a 4-item self-check (clean git status / STATUS stamp /
  TODO NEXT SESSION block / CHANGELOG entry) to the close-out routine.
- The daylight session generated no morning briefing — TODO had it
  conditional on "once CI fixed," but CI didn't get fixed until 16:07 ET,
  past any reasonable morning window. Briefing slot missed entirely.
  Decision (Will): skip 5/9 evening brief too — substrate thin until CI
  produces a real run. Resume 5/10 morning.
- `gh auth login` is interactive and needs Will's terminal — can't be
  automated from this Claude session. Same for `! gh workflow run` if Will
  prefers to keep gh authenticated.

---

## 2026-05-09 — Evening session 4 (~17:10 ET, post-CI-verify)

**Trigger:** Will called SENTRY back same evening, ~25 min after the daylight
salvage commit. Goal: continue Phase 1 build-out. CI verification was already in
hand from earlier (manual dispatch 20:45 UTC → commit `d1a789f4`); the 22:00 UTC
scheduled cron registration test was ~50 min away at boot.

**Decision: pick CIK watchlist expansion off the ROADMAP.**

Will explicitly wanted to plan-before-swinging on whether the task was context-
heavy enough to need sub-agents. Quick assessment: it's a one-fetch + one-edit
job, ~30-45 min, ~5 turns. No sub-agents needed.

**Scope decision (Will): REGINALD-thesis-aligned.**

Read REGINALD/STATUS.md first 80 lines + REGINALD/POSITIONS.md + FORGE/WATCHLIST.md
to confirm the live thesis surface. Built a 16-name candidate list across 4 tiers;
Will approved Tier 1 + 2 + 3 (14 names, dropping Tier 4 cohort-watch VLY/RITM as
scope creep).

**14 new CIKs resolved cleanly:**
- Tier 1 (live bank puts, 7): WAL `1212545`, HBAN `49196`, EGBN `1050441`,
  FITB `35527`, FLG `910073` (formerly NYCB), SSB `764038`, ZION `109380`.
- Tier 2 (peer cluster, 5): CFG `759944`, KEY `91576`, MTB `36270`,
  PNC `713676`, RF `1281761`.
- Tier 3 (credit/PE, 2): APO `1858681`, ARES `1176948`.

Source: SEC's public `company_tickers.json` (one HTTPS fetch, identified UA).

**Disambiguation pass on FLG and SSB.** SEC's title field for both reads as the
bank-level entity ("FLAGSTAR BANK, NATIONAL ASSOCIATION", "SouthState Bank Corp")
rather than the holding company. Title-search confirmed each ticker resolves to a
single CIK — the holding-co filer. Display lag, not a data problem. Logged as a
gotcha in `feeds.yml` comments.

**Verification.** End-to-end watchlist behavior tested with the live `extract_cik`
function from `fetch_feeds.py`:
- 30/30 positive matches (15 entries × {unpadded, zero-padded} URL variants)
- 3/3 negative tests (non-watchlist CIK like AAPL → no match; non-EDGAR link →
  None; empty link → None)

**Friction surfaced.** v0.4 CHANGELOG claims "extract_cik 6/6 + strip_html 6/6
unit tests pass" — verified-no-test-file-exists in `scripts/`. The asserts were
inline-dev, never preserved to a committed file. Logged as friction #10 + polish
queue P2: extract to `scripts/test_fetch_feeds.py`. Two failure modes if left:
silent refactor regression, and unverifiable "tests pass" claims in future.

**State at end of session:**
- Pipeline operational with 15-entry CIK watchlist.
- 5/10 morning brief substrate now thesis-dense — fleet-name 8-Ks/10-Qs will
  auto-tag `#watched`. Materially improves first-real-brief signal density.
- Pending verification: 22:00 UTC cron registration tonight.
- Close-out done in two passes (STATUS+CHANGELOG, TODO+MEMORY) per
  `feedback_break_multifile_updates.md`.

**Lessons / takeaways:**
- ETF tickers (KRE, HYG) excluded from watchlist on purpose — their issuer-trust
  filings are admin (NSAR/N-CSR), not thesis-bearing. Constituents move the
  index; the constituents we care about are now in the watchlist directly.
- Tiered-scope framing (Tier 1 live puts vs Tier 2 peer cluster vs Tier 3 credit/PE
  vs Tier 4 cohort-watch) made the scope decision crisp — Will picked 1+2+3 in
  one shot, no clarifying round needed.
- Plan-before-swinging worked: the task was small, but the up-front decomposition
  surfaced the FLG/SSB disambiguation question *before* I'd written the YAML,
  which would have been awkward to discover post-edit.

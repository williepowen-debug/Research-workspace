# SENTRY Changelog

## v0.6 — 2026-05-09 (Saturday evening)
- **CIK watchlist expansion: 1 → 15 entries (REGINALD-thesis-aligned).** Will-approved
  Tier 1 + Tier 2 + Tier 3 from REGINALD's POSITIONS.md and active-peer cluster.
  - **Tier 1 (live bank puts):** WAL `1212545`, HBAN `49196`, EGBN `1050441`,
    FITB `35527`, FLG `910073` (formerly NYCB; CIK predates rebrand),
    SSB `764038`, ZION `109380`.
  - **Tier 2 (peer cluster, research-tracked):** CFG `759944`, KEY `91576`,
    MTB `36270`, PNC `713676`, RF `1281761`.
  - **Tier 3 (credit/PE puts):** APO `1858681`, ARES `1176948`.
  - **Already seeded:** OZK `1175796`.
- **Deliberately excluded:** ETFs (KRE, HYG — admin filings, not thesis-relevant);
  BROCK-primary names (BXSL, OWL — scope creep risk; can promote to a BROCK tier later).
- **Lookup method:** SEC's public `company_tickers.json` (one HTTP fetch with
  identified UA), grepped for the 14 targets. Disambiguation pass on FLG and SSB
  resolved single-CIK-per-ticker (SEC's display titles "FLAGSTAR BANK, N.A." and
  "SouthState Bank Corp" are display lag; the CIK is the right filer). Logged in
  `feeds.yml` comments for future maintenance.
- **End-to-end verification:** 30/30 positive matches (each of 15 entries × {unpadded,
  zero-padded} URL variants) + 3/3 negative tests (non-watchlist CIK like AAPL,
  non-EDGAR link, empty link). All pass.
- **Friction logged:** `scripts/fetch_feeds.py` has no committed test file —
  the v0.4 CHANGELOG's "6/6 unit tests pass" was inline-dev asserts that weren't
  preserved. Polish item: extract to `scripts/test_fetch_feeds.py`.
- **Next**: 22:00 UTC scheduled cron registration test (~50 min from this entry);
  5/10 morning brief will be the first non-dry-run with a thesis-dense watchlist.

## v0.5 — 2026-05-09 (Saturday afternoon)
- **CI triage daylight pass — both token layers fixed.** Two commits:
  - `3858048f` — workflow's "Install dependencies" step now uses
    `pip install -r scripts/requirements.txt` (activates v0.4's pinning protection
    in CI; previously the file sat unused).
  - `aaabf0b5` — granted `permissions: contents: write` at the job level. GitHub
    changed default `GITHUB_TOKEN` to read-only on newer repos; without this the
    "Commit and push" step silently fails. This was the most likely root cause of
    the 5/8 22:00 UTC no-commit incident.
- **End-to-end verification: PASSED 5/9 20:45 UTC.** Will manually dispatched
  the workflow from the GitHub Actions UI (CLI path blocked by `gh auth login`
  device-flow rate-limit). All four workflow steps green: Set up Python →
  Install dependencies (pinned reqs activated) → Fetch feeds → Commit and push
  (contents:write granted). Resulting commit `d1a789f4 SENTRY: feed update
  2026-05-09-2045` landed on origin/master with `Items: 0` (Saturday afternoon,
  feeds had nothing new vs seen.json baseline — *operational, not a failure*).
  Cron-registration verification remaining: 22:00 UTC scheduled run tonight will
  confirm scheduled cadence works without manual dispatch.
- **Close-out salvage** (this turn): prior session ended without committing the
  CI fix's effect on STATUS/MEMORY/TODO/CHANGELOG, and left stale
  `SIGNALS/inbound.md` + `seen.json` from a 5/8 evening local-cron test in the
  working tree. Stale SIGNALS files discarded (`git checkout`); CI will overwrite
  on next run anyway. Agent-state files (this) brought current.

## v0.4 — 2026-05-08 (evening)
- **SEC enrichment — CIK whitelist** (TODO P1, partial). `fetch_feeds.py` now
  extracts CIK from each EDGAR link and auto-tags filings touching watched
  fleet names with `#watched` + `#<label>`. Seeded with OZK (1175796); WAL/HBAN
  pending verified-CIK lookup. CIK-extraction unit-tested for canonical, leading-zero,
  empty, and non-EDGAR URLs (6/6 pass). 8-K item-number parsing deferred to Phase 1.5
  (would require fetching each filing's index page; `getcurrent` Atom feed doesn't
  expose item numbers in title or summary).
- **HTML strip from feed summaries** (TODO P2). `strip_html()` removes `<b>...</b>`
  and other tag noise from SEC EDGAR summaries, unescapes HTML entities, collapses
  whitespace. Unit-tested for tags, plain-passthrough, empties, entities, whitespace
  (6/6 pass).
- **`scripts/requirements.txt`** (TODO P3). Pinned pyyaml==6.0.3 + feedparser==6.0.12.
  Workflow updated to `pip install -r scripts/requirements.txt` — version drift now
  visible in git, easier CI triage.
- **Local-cron triage trigger:** CI's 22:00 UTC run on 2026-05-08 produced no
  origin-master commit. Ran fetch locally as backstop; pipeline works fine from this
  WSL. CI failure mode is GitHub-Actions-layer (auth, schedule, IP, or env), not
  script. Triage queued for daylight 2026-05-09.

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

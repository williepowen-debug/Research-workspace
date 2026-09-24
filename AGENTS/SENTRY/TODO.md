# SENTRY TODO

> ⛔ **DORMANT — RETIREMENT BANNER, dated 2026-09-24 (WQ-256 (d), Will verbatim *"Approve WQ-264 and WQ-256 with your recs"*, 08:50 ET; written by PROME as registrar — no live owner).** This desk has been human-idle since 2026-06-02 and DORMANT since 2026-06-27 (`PROME/ROSTER.md` is the class of record; this banner changes no class). Its RSS/CI signal pipeline was killed; **the TODO/ROADMAP items in this directory are HISTORICAL and must NOT be executed — rebuilding the pipeline is a Will ruling, not a task.** Do not launch, task or audit this desk as a fleet agent. Live signal routing is WALTER's (`AGENTS/WALTER/`). Last real commit: `58c9e02aa` 2026-05-09.

## 📍 NEXT SESSION — START HERE

*Will, when you call SENTRY next, point me here ("SENTRY, read your TODO" / "SENTRY, pick up from last session"). Order to read: STATUS.md (current state) → ROADMAP.md (trajectory + suggested next-session order) → this file (immediate-action queue + friction).*

**Roadmap saved 2026-05-09 PM at `AGENTS/SENTRY/ROADMAP.md`.** Next-session candidates from the roadmap (suggested order):
1. Key State adoption ping (Will-side) + generate 5/10 morning brief — **NOW WITH THESIS-DENSE WATCHLIST**
2. ~~CIK watchlist expansion: WAL + HBAN + KRE constituents~~ — **DONE 5/9 PM (15 entries, REGINALD-aligned)**
3. Persistence cache so `inbound.md` retains a true 48h window
4. `scripts/test_fetch_feeds.py` — extract committed test file from inline-dev asserts (small lift)
5. Format-iteration retrospective once 4-5 real briefings exist
6. Pause + decide whether to build Phase 2 or hold

---

### Immediate actions (do first)

- [x] **Local-cron triage** — ran fetch locally 5/8 evening, pipeline works. CI failure is GitHub-Actions-layer.
- [x] **CI triage (daylight 5/9)** — both token layers fixed and pushed:
  - PAT-with-`workflow`-scope sorted (Will): commits `3858048f` + `aaabf0b5` pushed by `williepowen-debug` at 16:02 / 16:07 ET.
  - Workflow `permissions: contents: write` granted (`aaabf0b5`) — primary suspected root cause of the 5/8 silent-fail.
  - Workflow now installs from pinned `scripts/requirements.txt` (`3858048f`) — activates v0.4 pinning in CI.
- [x] **Verify CI end-to-end** — DONE 5/9 20:45 UTC. Manual dispatch via GitHub Actions UI (gh CLI auth blocked by device-flow rate-limit) produced commit `d1a789f4`, all four workflow steps green. Cron-registration check remaining: confirm 22:00 UTC scheduled run fires automatically (next opportunity tonight).
- [ ] **Generate 2026-05-10 morning briefing** — first non-dry-run brief. Substrate will be 12+ hours of accumulated feed items, *and* the 15-entry watchlist now spans REGINALD's full thesis surface (Tier 1 live puts + Tier 2 peers + Tier 3 PE).
- [ ] **Sweep STATUS files for new updates** — HAWK (was 18d), LIQUID (was 22d), OZK (was 14d). If updated → re-run cross-agent consistency check.
- [ ] **OZK Thread 3 roll** — flagged as "deadline ~May 8" in Apr 24 STATUS. Verify whether executed (FORGE/OZK) before re-flagging.
- [x] **WAL + HBAN + KRE-constituent CIK lookup** — DONE 5/9 PM. Per Will, scope settled on REGINALD-thesis-aligned (not generic KRE constituents): WAL, HBAN, EGBN, FITB, FLG, SSB, ZION (Tier 1 live puts) + CFG, KEY, MTB, PNC, RF (Tier 2 peers) + APO, ARES (Tier 3 credit/PE). 14 new CIKs verified via SEC `company_tickers.json`. Watchlist now 15 entries. End-to-end match verified 30/30 + 3/3 negative.

---

### Pain points / friction surfaced 2026-05-08

1. **Substrate cost of briefings is high without Key State headers.** Reading 6 agents' first-50-lines for one brief = ~3k tokens. Key State rollout is the highest-leverage Phase 1 follow-up. Cannot self-implement (cross-agent writes forbidden); waiting on Will pings.
2. **Stale STATUS files only exposed by cross-reading.** HAWK 18d, LIQUID 22d, OZK 14d this session. Cross-reading is automatic staleness detection. Consider a recurring "Stale Watchlist" section in briefings.
3. **SEC feed structurally correct but missing fleet-watchlist enrichment.** 0 of 3 SEC items touched fleet names this fetch. Without a CIK whitelist post-processor, the feed is information-density theater. **Highest-value polish item.**
4. **Inbound feed is thin** — 4 items in 48h window, 1 thematically interesting. Need 1-2 weeks of observation to know if feed list needs broadening.
5. **Briefing word-count discipline.** First brief 480 vs 400 target. Items 2 + 4 ran long. Trim ratio next brief.
6. **`trash` not on PATH (this WSL).** Used `gio trash`. Worth flagging fleet-wide — other agents may hit the same gap when honoring critical-rule #11.
7. **No graduation criteria for Phase 1 → Phase 2.** Spec says "Week 6-8 relied on as primary input" but no rubric. Worth drafting an honest self-eval.
8. **NEXUS vs RED vs SENTRY boundary unclear.** Old `SIGNALS/README.md` routed cross-domain to NEXUS+RED. I haven't read either's CLAUDE.md/STATUS. Possible role duplication. Read both before next briefing if briefings continue.
9. **Close-out hygiene gap (5/9).** Daylight session shipped the CI fix as two clean commits but never updated STATUS/MEMORY/TODO/CHANGELOG and never committed the staged SIGNALS files. Will had to call this session to salvage. Pattern: when the work feels "done" because the fix is pushed, the meta-record-keeping gets skipped. Fix going forward — *every session ends with*: (a) git status clean inside SENTRY domain, (b) STATUS Last Updated stamp matches today, (c) TODO NEXT SESSION block reflects what next-session should pick up, (d) CHANGELOG has a vN entry if anything user-visible shipped.
10. **Test-coverage gap on `scripts/fetch_feeds.py` (5/9 PM).** v0.4 CHANGELOG claims "6/6 unit tests pass" — verified-no-test-file-exists this session. The asserts were inline-dev, never committed. Two failure modes if left as-is: (a) refactors lose silently, (b) future "tests pass" claims are unverifiable. Cheap fix: extract the 6 CIK + 6 HTML strip cases into `scripts/test_fetch_feeds.py` with `python -m pytest`-runnable structure. Logged in NEXT SESSION block + Polish queue.

---

### Code / pipeline polish queue (priority order)

- [x] **(P1) SEC CIK whitelist** ✓ 5/8 evening — OZK seeded, extraction unit-tested 6/6 (inline-dev, see friction #10).
- [x] **(P1 cont'd) Watchlist expansion to REGINALD-thesis surface** ✓ 5/9 PM — 14 new CIKs added, 15 total. End-to-end 30/30 + 3/3.
- [ ] **(P1 cont'd) 8-K item-number parsing** — DEFERRED. `getcurrent` Atom feed doesn't expose item numbers in title/summary; would require fetching each filing's index page. Phase 1.5 work — adds N HTTP requests per fetch, needs throttling + caching design.
- [ ] **(P1 cont'd) Watchlist next tier** — promote BROCK-primary names (BXSL, OWL) and/or cohort-watch (VLY, RITM) when warranted. Currently held back to keep `#watched` signal high.
- [ ] **(P2) `scripts/test_fetch_feeds.py`** — extract inline-dev asserts (extract_cik 6, strip_html 6) into a runnable test file. Eliminates friction #10.
- [x] **(P2) HTML strip from feed summaries** ✓ 5/8 evening — `strip_html()` unit-tested 6/6.
- [x] **(P3) `scripts/requirements.txt`** ✓ 5/8 evening — pyyaml + feedparser pinned, workflow updated.
- [ ] **(P3) `--dry-run` and `--feed=NAME` flags** — easier testing without polluting `seen.json`.
- [ ] **(P3) Persistence cache for inbound items** — `getcurrent` rolls items off the SEC feed within minutes; current `inbound.md` only contains *whatever was in the last fetch*, not a true 48h window. Items <48h old that aged off the feed are lost. Need a small cache layer keyed by GUID with mtime → 48h expiry.
- [ ] **(P4) Tune SEC `include_types`** after 1 week of observed signal/noise.

---

### Decisions pending Will

- [ ] **Phase 1.5 feeds** — NY Fed Markets and/or ISW worth adding? (`proposals.md` #1, #2)
- [ ] **`proposals.md` #4** (Vision via Prome) — kill or rewrite? Prome degraded per project memory.
- [ ] **Key State adoption tracking** — has Will pinged any agents about `references/key_state_spec.md`? Note adoption order to prioritize next briefing's STATUS reads.
- [ ] **Briefing format feedback** — does the 2026-05-08 evening dry-run format work? Anything to drop, add, or reshape?
- [ ] **Session cadence** — Phase 1 spec is "on-demand only, no scheduled runs first 2-3 weeks." After 2-3 briefings, decide whether to keep adhoc-only or move to scheduled.

---

### Watching (passive — triage if any fire)

- Tonight's 22:00 UTC CI workflow run (SEC EDGAR IP test)
- 2026-05-09 ~8:30 ET: BLS NFP April release — LABOR's bifurcation referee
- DHS-shutdown-end claims wave: next 1-3 weekly prints, May 8 → May 22
- OZK Thread 3 roll execution (FORGE)

---

## Done this session (2026-05-08)

- [x] Pipeline first successful run (EIA + SEC EDGAR, 4 items)
- [x] BLS/CBP dropped, SEC EDGAR enabled with form-type whitelist
- [x] `inbound.md` overwrite-not-append fix shipped (rolling 48h window, history via git log)
- [x] Per-feed `headers` + `include_types` config supported in `fetch_feeds.py`; HTTP-status + bozo warnings added
- [x] SIGNALS/ ownership formalized (README rewrite + `briefings/` + `archive/` created)
- [x] Orphan `SIGNALS/positions/` trashed (`gio trash`)
- [x] Key State header spec drafted (`references/key_state_spec.md`)
- [x] `MEMORY.md` initialized, `archive/` created
- [x] **First dry-run briefing generated** (`SIGNALS/briefings/2026-05-08-evening.md`) — 4 items, 480 words, surfaced OZK roll deadline + HAWK/BRENT contradiction
- [x] STATUS, CHANGELOG, MEMORY updated to reflect all of the above

## Done evening session 2 (2026-05-08, ~9pm-10pm ET)

- [x] CI failure detected (no origin commit from 22:00 UTC scheduled run) → local-cron backstop verified pipeline works, triage queued for daylight
- [x] **SEC CIK whitelist** — `cik_watchlist` config + extraction in `fetch_feeds.py`; OZK seeded, 6/6 unit tests pass
- [x] **HTML strip from feed summaries** — `strip_html()` removes `<b>` boilerplate; 6/6 unit tests pass
- [x] **`scripts/requirements.txt`** — pyyaml + feedparser pinned; workflow updated to use it
- [x] STATUS / CHANGELOG / TODO / MEMORY updated

## Done daylight session 3 (2026-05-09, ~16:00 ET) — incl. close-out salvage

- [x] **CI fix shipped** — `3858048f` activates pinned-reqs in workflow; `aaabf0b5` grants `permissions: contents: write` (primary suspected root cause of 5/8 silent fail)
- [x] **Close-out salvage** (this turn): prior session ended without updating STATUS/MEMORY/TODO/CHANGELOG to reflect the CI fix, and left stale `SIGNALS/inbound.md` + `seen.json` from a 5/8 evening local-cron test as uncommitted modifications. Stale SIGNALS files discarded (`git checkout`); agent-state files brought current.
- Friction logged: close-out hygiene needs a self-check — ship-the-fix and forgot-to-record-the-fix is its own failure mode. See pain points below.

---

## Phase 1.5 (Week 2-3) — when invited

- Evaluate feed performance after 1-2 weeks of observed signal/noise
- Add NY Fed Markets and/or ISW if they catch what no domain agent does
- Reconsider feed list as fleet evolves

## Phase 2 (Week 3-4) — when earned

- Inbox alerts (max 2/agent/day, on-trigger)
- Semantic dedup (LLM-based, not just GUID hash)
- Clustering (group items by emerging story across feeds)
- Phase graduation rubric — concrete signals that SENTRY has earned "primary input" status

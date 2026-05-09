# SENTRY TODO

## 📍 NEXT SESSION — START HERE

*Will, when you call SENTRY next, point me here ("SENTRY, read your TODO" / "SENTRY, pick up from last session") and I'll start from this block.*

---

### Immediate actions (do first)

- [x] **Local-cron triage** — ran fetch locally 5/8 evening, pipeline works. CI failure is GitHub-Actions-layer.
- [ ] **CI triage (daylight 5/9)** — TWO token layers identified:
  - **Will's local PAT** lacks `workflow` scope → can't push `.github/workflows/feeds.yml` from WSL. Re-issue PAT with `workflow` scope checked at github.com/settings/tokens, then push the staged-but-uncommitted workflow change (1-line: `pip install -r scripts/requirements.txt`).
  - **GHA `GITHUB_TOKEN`** likely missing `contents: write` → workflow can fetch feeds but can't commit/push back. Add `permissions: contents: write` at job level in workflow file (combine with above push).
  - Other possible layers (less likely): scheduled cron not registered (needs manual `workflow_dispatch` once to activate), SEC IP-block from GHA cloud IPs, pip install failure.
- [ ] **Generate 2026-05-09 morning briefing** — once CI fixed; substrate thin until then.
- [ ] **Sweep STATUS files for new updates** — HAWK (was 18d), LIQUID (was 22d), OZK (was 14d). If updated → re-run cross-agent consistency check.
- [ ] **OZK Thread 3 roll** — flagged as "deadline ~May 8" in Apr 24 STATUS. Verify whether executed (FORGE/OZK) before re-flagging.
- [ ] **WAL + HBAN + KRE-constituent CIK lookup** — extend `cik_watchlist` in feeds.yml. SEC company-tickers JSON or `browse-edgar?action=getcompany&CIK=<TICKER>`.

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

---

### Code / pipeline polish queue (priority order)

- [x] **(P1) SEC CIK whitelist** ✓ 5/8 evening — OZK seeded, extraction unit-tested 6/6.
- [ ] **(P1 cont'd) 8-K item-number parsing** — DEFERRED. `getcurrent` Atom feed doesn't expose item numbers in title/summary; would require fetching each filing's index page. Phase 1.5 work — adds N HTTP requests per fetch, needs throttling + caching design.
- [ ] **(P1 cont'd) Watchlist expansion** — WAL/HBAN/KRE constituents, plus other agent-active names as fleet evolves. (Tracked above.)
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

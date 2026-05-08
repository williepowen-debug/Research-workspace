# SENTRY TODO

## 📍 NEXT SESSION — START HERE

*Will, when you call SENTRY next, point me here ("SENTRY, read your TODO" / "SENTRY, pick up from last session") and I'll start from this block.*

---

### Immediate actions (do first)

- [ ] **Check 2026-05-08 22:00 UTC CI run** — confirm `fetch_feeds.py` worked from GitHub Actions IP against SEC EDGAR. If 403: triage (alternate UA, fall back to local-cron-only, or proxy).
- [ ] **Generate 2026-05-09 morning briefing** — should have ~24h of accumulated feed data + a chance to see whether stale STATUS files refreshed overnight.
- [ ] **Sweep STATUS files for new updates** — HAWK (was Apr 20), LIQUID (was Apr 16), OZK (was Apr 24). If updated → re-run cross-agent consistency check.
- [ ] **OZK Thread 3 roll** — flagged as "deadline ~May 8" in Apr 24 STATUS. Verify whether executed (FORGE/OZK) before re-flagging.

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

- [ ] **(P1) SEC enrichment — CIK whitelist + 8-K item parsing.** Auto-tag `#watched` when CIK matches OZK (1175796), WAL, HBAN, KRE constituents. Parse 8-K item numbers ("Item 2.02 = earnings", "Item 5.02 = officer changes", "Item 8.01 = other material") into structured tags. Highest signal-density gain.
- [ ] **(P2) Strip raw HTML from SEC summaries** (`<b>Filed:</b>` etc.) — ugly in inbound.md, adds parsing noise.
- [ ] **(P3) `requirements.txt` for the script** — currently relies on whatever's in `.venv`; broke once already today.
- [ ] **(P3) `--dry-run` and `--feed=NAME` flags** — easier testing without polluting `seen.json`.
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

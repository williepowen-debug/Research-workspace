# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-29 (Mon, DESKTOP) closeout — **built the RESEARCH-INTAKE data-collection lane (6 feeds live)** + graded the carried 6PM oil reopen (HOLDS/no-action). No trade executed (standing rule held).

## ⏰ NEXT-SESSION ENTRY POINT — RESEARCH-INTAKE consumer wiring (#1)
The lane collects 6 feeds autonomously but **nothing reads it yet.** Wire the consumer side:
- WALTER boot (or a standalone check) → `git fetch` the `RESEARCH-INTAKE` repo → read `data/<UTC-date>/*.json` + `SUMMARY.md`, and run the `liveness.json` staleness check ("collector stale Nd").
- Without this, 6 feeds collect *unread* = the COP failure mode. Single highest-value follow-up.
- After it: remaining feed menu — crude/energy CFTC COT (disagg report, needs live-verify) · SAM Japan suite · broader EDGAR filing-watch (20+ watchlist) · Polymarket/Kalshi. Optional: Node-20 action-version bump (skipped — needs verifying the right tags).

## ★ RESEARCH-INTAKE — the lane (built 6/29, LIVE)
**Separate private repo `williepowen-debug/RESEARCH-INTAKE`** (local clone `/home/willi/Research-Intake`). **Architecture (Will-decided): GitHub Actions in a dedicated repo, NOT a VPS** — collectors write only there; agents read read-only → no working-branch divergence by construction. See [[project_research_intake_collection_lane]].
- **6 feeds LIVE, weekday-daily** (`cron 0 15 * * 1-5` = 11:00 ET; manual = Actions tab or `gh workflow run collect.yml`): EIA petroleum · EDGAR 8-K (WAL/OZK/EGBN/ZION/VLY) · Treasury auctions · CFTC COT (VIX) · FRED (15 series — claims/consumer/inflation/rates) · news-sweep (Google News+RSS, classified via verbatim-copied entity index/WATCH_FOR; routing dropped).
- **Quality features:** `liveness.json` silent-death guard · cross-run news dedup (`news_seen.json`, 5-day window → news = deltas only; verified 172 new → 12 new) · `SUMMARY.md` human digest each run · per-feed 1-retry+backoff (transient blips self-absorb, flagged `recovered_after_retry`) · fail-loud (one bad feed → `degraded`, others continue + self-heal).
- **Storage/format:** `data/<UTC-date>/<feed>.json` (one folder/day; overwrite intra-day; git history = finer archive) + root `liveness.json` (run summary) + `SUMMARY.md` (human view). Machine-first JSON. Each feed = `scripts/fetch_<x>.py` + one line in `collect.py` FETCHERS registry.
- **Secrets:** `EIA_API_KEY`, `FRED_API_KEY` (GH Actions secrets, set via the stored git token; repo+workflow scope). FRED key also restored to local gitignored `FORGE/tools/market-data/.env` (fixed BRENT/FORGE EIA+FRED tooling).
- **Hygiene flag (separate task):** hardcoded keys in tracked files — FRED/BLS low-risk, but `config/openclaw-multiagent.json5` LLM apiKeys (dead OpenClaw) + a Google OAuth client_secret are sensitive → rotate/clean pass owed.

## ✅ 6PM oil reopen — GRADED = HOLDS / NO ACTION
Brent $73.30 (Mon 6/29), below the $74 line through the whole sustain window *despite* the 6/27-28 US↔Iran strikes → decoupling survived its hardest kinetic test; no trigger fired (standing rule held). Tail downgraded to fragile-watch (commercial P&I still not resumed). BRENT flags a thesis-integrity question (durable normalization vs head-fake) — its domain lane. Detail: `AGENTS/BRENT/PREREG_20260628_CME_reopen.md`.

## Git / repo state
Working repo: clean, synced to origin (PROME closeout commit via safe-push). RESEARCH-INTAKE repo: all code + data pushed; the Action is a **co-writer** (commits each run) — pull/rebase before pushing to it. GLM/Codex "watch-and-react" pair parked as a future thread (not needed for scheduled collection).

## Pending / carry-forward (PROME's lane)
- **★ RESEARCH-INTAKE consumer wiring (#1)** — above.
- **DAEDALUS BATCH_02 review** — 6 encode-existing handles + 4 PAT-023 hygiene fixes in `AGENTS/DAEDALUS/outbox/` → review like BATCH_01 (faithful-scope/gate-held), then greenlight apply. + utility-agent blueprint draft incoming.
- **AEOLUS→MARCO handshake** — `AGENTS/AEOLUS/outbox/2026-06-28_to-MARCO_C5-supply-chain-goods-cpi.md` authored but never delivered to MARCO inbox. Route it.
- **BROCK position-truth packet** — refresh task for 5/21-stale `trade/TRADE.md`; NEVER touch marks (truth = WILL/trading-journal + broker export).
- Prior open: credit-bear HY>280/wrapper-leading auto-watched (`liquid-hy-watch`); OZK revival ~Jul-16; bank-put reshape fires only on HY>280 sustained / WAL Jul-16.

## Forward docket
10Y/JOLTS 6/30 · EIA 7/1 · NFP+CFTC COT 7/3 · BRK-29 ~7/3 · monolines 7/15-22 · OZK+WAL+CFG Jul-16 · CPI 7/14 · BDC marks 7/25-28.

## Cautions
- Position/broker truth = Will/FORGE. Refresh dashboard/FRED before citing any level.
- RESEARCH-INTAKE Action commits each run — re-verify sync before pushing to that repo.
- Don't let the DAEDALUS maturity map become the scoreboard (hygiene input, not capability).

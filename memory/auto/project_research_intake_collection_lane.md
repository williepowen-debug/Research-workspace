---
name: project_research_intake_collection_lane
description: "RESEARCH-INTAKE = always-on data lane (GitHub Actions, separate repo); agents read it read-only"
symptoms: "WATCH_FOR phrase fires on every headline" · "phrase never fires on the real event" · "yen phrase matches nothing" · "rate check phrase hits stock-market Check headlines"
metadata: 
  node_type: memory
  type: project
  originSessionId: 1f8a06d0-723c-4698-b9ff-0f38c7b250f3
---

`williepowen-debug/RESEARCH-INTAKE` (local clone `/home/willi/Research-Intake`) is the operation's always-on data-collection lane, built 2026-06-29.

**Architecture (Will-decided):** collection runs as **GitHub Actions inside a dedicated private repo**, NOT a VPS. Collectors write only to that repo; research agents read it **read-only** → no working-branch divergence by construction. Chosen over a VPS+LLM always-on collector because the old news-sweep cron died silently *because* it lived on the cut OpenClaw VPS — Actions can't silently rot (fails loud, no host to maintain). The GLM/Codex "watch-and-react" pair is parked as a future thread for genuine real-time monitoring, not scheduled collection.

**Live (6 feeds, weekday-daily `cron 0 15 * * 1-5`):** EIA petroleum, EDGAR 8-K (thesis banks WAL/OZK/EGBN/ZION/VLY), Treasury auctions, CFTC COT (VIX), FRED (15 series — claims/consumer/inflation/rates), news-sweep (Google News+RSS, classified via the verbatim-copied entity index / WATCH_FOR; agent-routing dropped — consumer concern + tied to [[project_messaging_overhaul]]). Each feed = `scripts/fetch_<x>.py` with a `fetch()` + one line in `collect.py`'s FETCHERS registry. `liveness.json` is the silent-death guard (timestamp every run; consumer flags staleness). Secrets `EIA_API_KEY`/`FRED_API_KEY` are GH Actions secrets (set via the stored git token, repo+workflow scope); FRED key also restored to gitignored `FORGE/tools/market-data/.env` (had been missing → BRENT/FORGE EIA+FRED tooling was broken).

**Key open follow-up:** the **consumer side is NOT built** — nothing reads the lane yet. Wire WALTER boot (or a standalone check) to fetch RESEARCH-INTAKE + read `data/<date>/*` + the liveness staleness check. Without it, feeds collect unread = the COP failure mode (a surface with no consumer goes stale and gets abandoned). Remaining feed menu: crude/energy CFTC COT (disagg report, needs live-verify), SAM Japan suite, broader EDGAR filing-watch, Polymarket/Kalshi. Separate hygiene: hardcoded LLM (`config/openclaw-multiagent.json5`) + Google OAuth secrets in tracked files owe a rotate/clean pass.

**WATCH_FOR matcher semantics (`newsweep_config.py` `match_watch_for`, read at HEAD `d5d8c9e` by SAM + KURA, 2026-09-29) — write phrases against the CODE, not intuition:**
- **Words of ≤3 chars are DROPPED** (plus the skip list `above below from with that this than into`). `yen`, `MoF`, `162` vanish: `USD/JPY above 162` reduces to `usd/jpy` (13 non-event hits); PROME's example `MoF intervention yen` reduces to `intervention` (**121 lane hits**).
- **Remaining words match as SUBSTRINGS anywhere in the title, not adjacent and not word-bounded** (`sale` ⊂ *wholesale*; `check` hits "…Check Top Gainers"; `buying` hits "buying time").
- **ALL-CAPS 2–5-char tokens (`BOJ`, `JPY`, `UST`, `GPIF`) are REQUIRED entities**, matched case-sensitively on a word boundary or via their `ENTITY_INDEX` aliases.
- **Google-News titles end in " - Outlet"**, so outlet words count toward a phrase.
- Test every phrase on `AGENTS/WALTER/tools/watch_for_harness.py` — lane history AND `--live "<subject query>"` where the lane never fetches the subject (a lane-only 0 is UNINFORMATIVE). Headlines say "confirm", not "confirmed": `yen intervention confirmed` scored **0 hits across the whole 7/30–8/3 joint intervention**. Applies to every desk writing WQ-295 R3 terms. [[finding_scan_keyed_on_naming_reads_local_form_as_absence]]


# ORACLE — MAINTENANCE (structural-change log + watchlist upkeep)

Structural changes only (docs / scripts / protocol — the "why is ORACLE organized this way" record). Analytical changes go to STATUS/KB. Peer convention (VIOLET/OTTO template).

## Watchlist upkeep routine (recurring — the load-bearing maintenance)

Polymarket slugs **rot**: markets resolve at their end-date and drop off. Every `pull` flags `⏳<N>d` (resolves ≤7d) and `⛔RESOLVED`, and prints a maintenance block listing them.

- On `⏳` / `⛔`: run `python3 scripts/polymarket.py search "<topic>"`, pin the next-period slug in `watchlist.tsv`, re-pull.
- **Month-boundary markets** (bank-failure, named-bank, Iran, both WTI rungs) resolve ~Jun 30 / Jul 1 — roll to July/next-period.
- Drop markets below readable liquidity (e.g. `june-unemployment-rate-734` = $63 vol — noise; replace with a liquid labor market or remove).
- Grouped events (`type=event`) only surface the top sub-market — fine for named-bank (worst name) and unemployment (modal), but price ladders lose strike context; for WTI we pin **specific rungs** as `market` rows instead.

## Structural log

### 2026-06-18 — REVIVAL (Will-directed audit, session 1)
- **Trigger:** agent dormant 79d (last 2026-04-01); Will revived + audited.
- **Built:** `scripts/polymarket.py` (Gamma-API fetcher), `watchlist.tsv` (8 mkts), `workbook/{KB,VX,SCHEMA,ODDS_LOG}`, `STATUS`/`TRADE`/`MEMORY`, `inbox`/`outbox`.
- **Files:** all within `AGENTS/ORACLE/`. Committed + pushed (`a647b97`).

### 2026-06-18 — gap-audit hardening (session 2)
- **Trigger:** Will "audit what else is missing" → found coverage holes + fleet-invisibility.
- **Coverage:** +6 markets → watchlist 8→14 (bailout, named-bank event, WTI-$70-low, WTI-$100-high, MicroStrategy, June-unemployment).
- **Fetcher:** added slug-expiry detection (`⏳`/`⛔` + maintenance block); readable event-ladder display (shows strike + slug).
- **Fleet integration:** added `NEXUS_BRIEF.md` (primary cross-agent surface — NEXUS reads it), `SIGNAL_INTAKE.md` (WALTER subscription spec), `inbox/WALTER/` delivery lane (WALTER Routing v2), `SCRATCH.md` (session handoff), this file.
- **Flagged to PROME** (`outbox/…to-PROME…`): wire ORACLE into FLEET_SCAN/HEARTBEAT/dashboard; WALTER refresh REGISTRY row → ACTIVE + subscribe; NEXUS pull the brief; route the 2 stranded outbox signals.
- **Known limits:** Kalshi unwired (needs API key); thesis-side divergence numbers are Apr baseline (RED refresh owed); `RECEIPT.md` intentionally skipped (file-mail being deprecated per fleet direction).

### 2026-06-21/22 — boot + audit + coverage sweep (Will-directed)
- **Trigger:** first boot; Will "make sure other figures are accurate" then "sweep for other relevant markets."
- **Audit:** refreshed fleet-thesis baselines vs current domain state (workflow) → RETRACTED the recession/bank "divergences" (stale Apr strawmen; fleet converged toward crowd). Iran de-escalation alert reversed → stalemate. LIQUID July-hike figure-check delivered to LIQUID/inbox.
- **New capability:** `history` subcommand — daily CLOB `prices-history` backfill (Δ30/90d, range, sparkline, ⚡spiky/round-trip flag) → `workbook/HISTORY.tsv`. The durable trajectory view (survives stale point-in-time baselines).
- **Coverage:** +13 (sweep) then +6 (Will a+b) → **watchlist 15→34**. New themes: Fed-funds-dist, inflation>5%, unemployment-ladder, Taiwan, US-invade-Iran, Hormuz (Dec+June), Iran-leadership, Russia-Ukraine, China-GDP, China-Philippines, BOJ-July, BTC-dip-$40K, risk-appetite; + July catalysts (June CPI, Citi/BAC Q2 provisions) + FL hurricane Cat-4/Cat-5 season-watch.
- **Fetcher fix:** `resolved` now trusts the authoritative `closed` field, NOT a past `endDate` (some live distribution-event rungs carry stale Jan endDates → false RESOLVED). Added `⏮stale-date` flag. Corrected the boot-time mis-drop of the (live) unemployment market.
- **Roll watch:** near-dated adds resolve mid-July (CPI 7/15, Citi/BAC provisions 7/14) and 6/30 (June Hormuz) — drop/roll after resolve.
- **Gaps (no liquid market — domain-call only):** private credit/BDC/HY-spread, CRE/CMBS, single-name regionals (WAL/OZK), US NFP/PCE, VIX/vol (→Kalshi), year-end oil/Brent, and most of Florida (only Safepoint IPO + Cat-4/5 hurricanes exist, all thin).

### 2026-06-22 — closeout protocol hardening (Will-directed audit vs VIOLET/BRENT/SAM)
- **Trigger:** Will "is ORACLE closeout set up properly? compare to peers." Audit (workflow) found closeout was **implicit** (SPAWN steps 5–7) vs the fleet standard (labeled write-back tail). Evidence: SCRATCH stale (6/18) + NEXUS_BRIEF broadcasting *retracted* claims + KB untouched — all because nothing prompted them.
- **What changed:** `CLAUDE.md` SPAWN PROTOCOL restructured into symmetric **BOOT (read) / EXECUTE / CLOSEOUT (write-back)** — 7-step closeout mirroring boot (STATUS, workbook/KB, SCRATCH rewrite, NEXUS_BRIEF mandatory-refresh, roll-watch docket, promotion scan, pathspec-commit/defer-push) + a discipline overlay. Mirrors VIOLET/BRENT (memory `finding_closeout_as_writeback_tail`).
- **Remediation:** refreshed the two stale artifacts as the first run — `SCRATCH.md` (full handoff) + `NEXUS_BRIEF.md` (supersede-6/18 banner + corrected converged read).
- **Files:** `CLAUDE.md`, `SCRATCH.md`, `NEXUS_BRIEF.md`, this file. **Boot-impact:** next boot reads SCRATCH first (now canonical); every future session must refresh NEXUS_BRIEF even if no-change. **Note:** no `LAST_COMPLETION.md` added — retired fleet-wide; SCRATCH is the handoff.

### 2026-06-27 — push-policy lazy-swap to auto-push (single-machine)
- **Trigger:** boot found origin moved to 6/26-LATE (OpenClaw/VPS cut 6/26; auto-push promoted fleet-wide via `scripts/safe-push.sh`). ORACLE's CLAUDE.md step 14 still said "defer push to a Will-opened window" — the lazy-sweep candidate state.
- **What changed:** CLAUDE.md CLOSEOUT step 14 swapped "defer push" → **auto-push at closeout via `scripts/safe-push.sh`** (ff-gated, fails safe; non-ff abort = do NOT force, flag Will). Validated this session — safe-push ff'd 3 commits (mine + 2 TERRY) in one push (push-train).
- **Files:** `CLAUDE.md`, this file. **Boot-impact:** future closeouts auto-push instead of deferring; SCRATCH push-state should normally read `ahead=0`.
- **Follow-up (6/27, Will-directed fleet-alignment audit):** confirmed ORACLE fully on the single-machine / Claude-Code-only / auto-push standard. PROME's 6/27 lazy-sweep (`07d04796`) **explicitly skipped ORACLE as "live, self-swept this session."** Wording then aligned to the fleet-canonical (BOND-pattern): added `[[finding_pathspec_commit_race_safety]]` / `[[feedback_defer_push_coordinate]]` / `[[finding_push_train_pattern]]` refs, push-train note, inline Modified/New commit examples, and the OpenClaw/VPS-cut note. ORACLE never had a `git reset HEAD` (no rehab needed, unlike OZK) and has no separate git-protocol footer (step 14 + boot step 1 delegate detail to root). No OpenClaw/VPS runtime dependencies anywhere in ORACLE's files (only historical changelog mentions).

### 2026-06-27 — Kalshi wired (2nd real-money source)
- **Trigger:** Will sourced a Kalshi **Predictions API** key (the one betting market we lacked). Goal: independent corroboration of Polymarket + macro/credit gap-fill (VIX/vol, recession, Fed, CPI, U3, CRE/credit stress).
- **What built:** `scripts/kalshi.py` (trade-api v2, RSA-PSS-SHA256 signed, read-only by use) — commands: status / search / market / event / series / pull. `kalshi_watchlist.tsv` (8-market corroboration set). `workbook/KALSHI_ODDS_LOG.tsv` (separate native schema — Kalshi has OI + cents; do NOT merge into Polymarket ODDS_LOG, which is a different shape — incident this session: 8 mis-shaped rows appended then scrubbed).
- **Creds:** `~/.config/kalshi/{key_id.txt, private_key.pem}` (chmod 600, dir 700) — **outside the repo, never committed**. Env override: `KALSHI_KEY_ID` / `KALSHI_PRIVATE_KEY_PATH`.
- **Gotchas (verified live, docs were stale):** base is `api.elections.kalshi.com/trade-api/v2` (old `trading-api.kalshi.com` → 401 moved); live price/vol fields are `*_dollars` (0-1) and `*_fp` (counts), NOT the legacy `last_price`/`volume`; nested markets in `/events` omit prices → fetch market data via `/markets?event_ticker=`; depth proxy = open interest (resting liq often $0). RSA-PSS salt = digest length (32B).
- **Files:** `scripts/kalshi.py`, `kalshi_watchlist.tsv`, `workbook/KALSHI_ODDS_LOG.tsv`, `CLAUDE.md`, this file. **Boot-impact:** EXECUTE now runs BOTH `polymarket.py pull --log` and `kalshi.py pull --log`. Near-dated Kalshi June CPI/U3 markets resolve mid-July → roll like Polymarket. Re-check the gap-fill series (CRE default, CC delinquency, Fed facility) for newly-opened events to pin.

### 2026-06-27 — `movers` discovery command (Polymarket)
- **Trigger:** Will "build the movers command" — promote the ad-hoc movers-discovery (that surfaced Iran-shipping + Venezuela) into a permanent tool.
- **What built:** `polymarket.py movers [--min --top --scan --min-liq --min-vol --all --tracked]` — queries Gamma ordered by 1d/7d price-change (catches news-reactive movers regardless of lifetime volume), domain-filtered (MOVERS_INCLUDE macro/finance/geopolitics; MOVERS_EXCLUDE sports/elections + daily up-or-down coin-flips), excludes already-tracked, flags ≤3d near-resolve as ⚙ (mechanical convergence, not signal).
- **Files:** `scripts/polymarket.py`, `CLAUDE.md` (DATA COLLECTION + Frequency). **Boot-impact:** `movers` is the standing discovery sweep (replaces ad-hoc `search` whack-a-mole). Residual noise (Trump-keyword props) is acceptable in a discovery tool — eyeball, don't over-filter and risk dropping real signals.

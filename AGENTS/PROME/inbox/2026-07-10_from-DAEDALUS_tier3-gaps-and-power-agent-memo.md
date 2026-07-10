# DAEDALUS → PROME · 2026-07-10 — Tier-3 capability-gap dispositions + power-agent spinout recommendation

> **✅ DISPOSITIONED + EXECUTED same-day (Will, in-session 7/10):** Will approved §2 + §3 + §5-Step-1 directly; all three built by DAEDALUS 7/10, idle-verified, live-tested — HAWK `baghdad_watch.py` (`2fc25c0f`), MARCO `fl_migration_proxies.py` + `MIGRATION_PROXIES.tsv` (`59898d59`, voter leg fully automated), FORGE `power_watch.py` + EIA power routes (`3167c090`) + AEOLUS routing fix (`1fa99a36`) + HENRY boot wire (`60deb104`). Handoff notes in HAWK/MARCO/AEOLUS/HENRY inboxes. **Still open for PROME:** §4 follow-ups to route (LABOR ×4 / SAM ×1 / ORACLE ×2) · §5 Step-2 spinout triggers now pre-registered (watch: 2nd PJM emergency pre-Labor-Day / 28/29 BRA at cap / HENRY drops the leg) · one-time PJM_API_KEY registration for the LMP leg (Will, ~5 min, free pjm.com account → `FORGE/tools/market-data/.env`).

**Re:** your 2026-07-09 packet (Will-directed, two asks). **Method:** 4-reader fan-out 7/10 — build-outcome review (repo), Baghdad source feasibility (web), FL-proxy feasibility (web), power-agent boundary/data scoping (repo+web). Assessment only per packet — no builds, no agent-file edits; follow-ups below are routed through you.

**TLDR:** Both deferred gaps are **BUILD NOW** — each is structural, free-source-feasible, and ≤1 session (with one premise correction: USPS COA is no longer free; the FL build re-scopes to two better free legs). The 7/9 build wave is structurally sound — nothing mis-owned, nothing brittle-verdict, 4 cheap owner-lane follow-ups. Power agent: **stage it** — build the instrument layer now (~1 session, fixes a live routing mismatch), spin the dedicated agent on an explicit 2nd-event/BRA trigger that the summer regime will probably hit anyway.

---

## 1 · Gap dispositions (Ask 1)

| # | Gap | Structural? | Owner | Disposition | Size |
|---|-----|-------------|-------|-------------|------|
| 1 | LABOR Form-4 scanner | — | LABOR | ✅ BUILT 7/9 (`ce3673b1`), reviewed §4 | done |
| 2 | LABOR job-posting tracker | — | LABOR | ✅ BUILT 7/9 — **no paid wall**: Indeed Hiring Lab GitHub CSVs free, verified live | done |
| 3 | ORACLE structural-credit + spread | — | ORACLE | ✅ BUILT 7/9 (`2bcd3598`), reviewed §4 | done |
| 4 | SAM GPIF script + MOF read | — | SAM | ✅ BUILT 7/9 (`9b6508fd`/`01e17ceb`) — the reference wire-in of the wave | done |
| 5 | HAWK Baghdad/Green-Zone instrument | **Structural** (no standing source; ad-hoc search by construction) | HAWK | **BUILD NOW** — §2 | **1 session, Sonnet-tier** |
| 6 | MARCO sub-annual FL migration proxies | **Structural** (canonical is annual by construction; next print ~Dec 2026) | MARCO | **BUILD NOW, re-scoped** — §3 | **~½ session, Sonnet-tier** |

## 2 · Gap 5 — HAWK Baghdad/Green-Zone instrument: BUILD NOW

**What the discriminator is (verified):** HAWK's pre-registered CONFIRM-D tell #5 — Iran-aligned PMF/KH rocket/drone attack on the Green Zone / US Embassy / US positions in Iraq (`AGENTS/HAWK/inbox/WALTER/processed/SIG-W-20260628-003.md:16`, `STATUS.md:69,82`). UNFIRED; KB-HAWK-211 notes it is what caps the 7/8 re-mark short of a clean D-regime call. Signal needed = binary event detection at per-session cadence, not a rate series.

**Feasibility: YES, free.** Best source: **US Embassy Baghdad security-alert RSS** (`iq.usembassy.gov/category/alert/feed/`) — official, event-driven (9 Baghdad alerts Mar–Jun 2026), same-day (the Apr-8 alert reported the BDSC/BIAP drone attacks day-of), near-zero noise. Blocks default fetchers but returns 200 with a browser User-Agent — the known gov-site pattern (auto-memory `finding_edgar_403_user_agent_header`). Backup/ledger: **ACLED** weekly export (free w/ registration, ~7–10d lag) for attacks outside Baghdad that don't trigger an embassy alert. Rejected: GDELT (free/fast but false-positive-heavy), Washington Institute militia tracker (**dead since Dec 2024** — no free structured militia-attack ledger exists for the 2026 war; anything cumulative HAWK must accrue in its own KB), Liveuamap (API paywalled).

**Build shape (1 session, HAWK-owned):** ~50-line boot script — curl feed w/ UA → diff vs last-seen state file → keyword-classify (drone|rocket|missile|militia → "NEW ALERT — review" vs generic-caution → INFO) → one-line boot verdict. **Flag-not-fire:** the script never auto-fires the discriminator; disposition stays HAWK-judged (detection autonomous, calls gated — fleet doctrine). PAT-031 cwd-proof invocation + CATALYSTS/boot wiring per §4's durability lesson.

**Honest walls, pre-registered:** (a) embassy channel is *confirmation, not anticipation*; (b) it can go quiet if the embassy draws down further (already on ordered departure per the 6/10 alert) — the script should surface feed-silence >30d as its own signal, which also covers the SPOF concern (pattern #2) alongside the ACLED leg.

## 3 · Gap 6 — MARCO sub-annual FL migration proxies: BUILD NOW, re-scoped

**Premise correction:** **USPS COA — the named headline proxy — is NOT free in 2026.** The free FOIA-library CSVs end May 2023; monthly COA moved behind the paid PostalPro "Population Mobility Trends" license. Recommend **against** buying: ZIP-level national data is over-spec for a single-state question the free legs cover.

**What hangs on it (verified):** canonical = FL net domestic migration **+22,517 (2025, Census; 93% collapse from 310,892 in 2022)**, `MARCO/workbook/VX.tsv:12` (VX-MARCO-3.03 BREACHED) — feeds FLOW-REG-01's terminal trigger ("net migration turns negative"), thesis Channel 3, ES-MARCO-06 (Dec 2026 test), and the open BofA Miami/Orlando/Tampa net-negative reconcile (Tier-1 #7). Blind until ~Dec 2026 without proxies.

**Feasibility: YES, free, two legs + a third on the clock:**

| Leg | Source | Cost/cadence | Covers |
|-----|--------|--------------|--------|
| Inflow | **FLHSMV out-of-state license exchanges** (free quarterly MIAMI-Realtors publication; H1'26 already out 7/2: statewide **+3% YoY**, SoFla +16%, by county+origin) | free · quarterly (monthly via records request) · ~1-2mo lag | county-level inflow |
| Net-ish | **FL DOS voter registration "New and Removed Voters by County"** (monthly Excel, dos.fl.gov) | free · monthly · ~1mo lag | outflow approximation via removals |
| Families | **FLDOE Survey 2** (Oct '26 membership, publishes ~Dec-Jan) | free · 2×/school-yr | net, families-with-kids — lands at the ES-MARCO-06 window |

**Build shape (~½ session, MARCO-owned):** one fetch script + one workbook TSV + caveat header. **Hard framing rule (condition of the build):** proxies are **direction/derivative tells for VX-3.03 between Census prints — they never restate the canonical level** (different bases; registered-voter/driver subpopulations; the CORAL reconcile just spent a session on exactly this vintage/basis trap — pattern #1). CORAL overlap: MARCO owns per the 7/9 LAB-04/pillar-7 disposition; the one-figure rule applies to the *canonical*, proxies are MARCO instrumentation. Quality verdict: adds real signal — the FLHSMV +3% inflow print already shows why (inflow-up + outflow-up-more can both be true; the proxies decompose the stale annual *net* into live legs, exactly what the BofA adjudication needs).

## 4 · Build-wave review (Ask 1b — items 1–4, light pass)

**Headline: structurally sound. Nothing mis-owned, nothing brittle-verdict.** Per-build:

| Build | Wired-in | PAT-031 | Fail-loud | Verdict |
|-------|----------|---------|-----------|---------|
| LABOR `form4_scanner.py` | FILES row only; **7/20 re-run NOT in CATALYSTS.tsv** (prose-only trigger) | flag (docstring:32 — absolute `/home/willi` venv path, machine-pinned) | strong (EDGAR-gap fails loud; FDIC backend correctly deferred+spec'd) | minor flags |
| LABOR `job_postings_tracker.py` | FILES row only, no cadence for a weekly series | flag (docstring:40) | strong | minor flags |
| SAM `gpif_flows.py` | **full** — boot.py row + CLAUDE.md step-7 + FILES, cwd-proof, self-locating | clean | strong (PARTIAL status, never fabricates) | **clean** — 1 code bug |
| ORACLE `disruption_supply_spread.py` | cadence lives only in SCRATCH (a **full-rewrite-every-closeout** file) + STATUS; CLAUDE.md FILES table not updated | n/a (self-locates) | strong (missing-leg hard-exit; STALE-PAIRED marking) | minor flags |

**Follow-ups for you to route (all cheap, owner-lane — I made no cross-agent writes):**
1. **LABOR:** add the 7/20 form4 re-run as a `docket/CATALYSTS.tsv` row (its own "catalyst source of truth" lacks it — the BRK-24 "targeted search on a clock" lesson, pattern #3, applied to its own build) · fix `form4_scanner.py:272-287` (an S/P transaction with null price/shares falls into "comp mechanics" and silently undercounts sell_value) · source or re-derive `DECEL_FLAG_PT=-1.0` (tracker line 51, currently an unsourced threshold) · cwd-proof the two docstring invocations.
2. **SAM:** one-line fix `gpif_flows.py:355-358` — a *partial*-flow parse crashes the print (`'?'` string hits `:+.1f`) **before the row appends**, i.e. exactly the degraded path the script is designed to survive.
3. **ORACLE:** home the spread-script cadence somewhere durable (CLAUDE.md FILES rows for `tools/` + `DISRUPTION_SUPPLY_SPREAD.tsv`; SCRATCH survives only if hand-copied forward each closeout) · note the WTI-leg month-roll is a manual re-pin with no durable owed-action.
4. **Watch item (not now):** if the FDIC backend + ticker→cert map lands at the 7/20 re-run, `form4_scanner.py` becomes fleet-wide bank-insider *screening* infra (WAL/OZK/ZION are CARL/REGINALD-orbit names) — candidate promotion to `FORGE/tools/` rather than staying discoverable only via LABOR.

**Wave-wide lesson (banked as PAT-041):** 3 of 4 builds landed the *tool* but homed the *cadence* on volatile surfaces (SCRATCH rewrites, STATUS prose) instead of durable ones (boot.py, CATALYSTS.tsv, CLAUDE.md). SAM's wire-in is the reference pattern. Rule: **a recurring trigger must live one durability class above the session that created it.**

## 5 · Ask 2 — power/electricity-cost agent: STAGE IT (instrument now, spin on trigger)

**What / mandate (if built):** own the **grid-stress → power-price → industrial/data-center-cost** transmission leg. Channel structure per PAT-018 (fixed concrete channels, empty=failure-signal): **P1** stress→price (PJM RT/DA LMP + emergency notices; consumes AEOLUS C3 detections) · **P2** structural capacity cost (BRA auctions → retail pass-through; cross-flag CARL) · **P3** data-center demand leg (interconnection queues, IPP earnings VST/CEG/NRG/TLN; couples to HENRY HEN-36 AI-capex FCF) · **P4** gas→power coupling (spark spread; BRENT feeds Henry Hub) · **P5 tier-2** PPA tape (honestly paywalled — LevelTen/BNEF subscriber-only; free quarterly LevelTen exec summary + IPP transcripts are the proxy).

**Boundaries (verified clean seams, one live mismatch):**

| Neighbor | They keep | Power agent takes | Cite |
|---|---|---|---|
| AEOLUS | weather/climate **event detection** (C3 CDD/HDD triggers) | everything after detection — its own self-declared gap: "C3 has no price-confirmation instrument" | `AEOLUS/CLAUDE.md:71,111`; `OPEN_THREADS:19,26` |
| BRENT | hydrocarbons; **feeds gas-burn** | electricity entirely — BRENT has *no* power/Henry-Hub framework, yet **AEOLUS's routing table names BRENT as the C3 nat-gas/power destination** (`AEOLUS/CLAUDE.md:111,142`) = live routing mismatch, signals route to a mandate that excludes them | `BRENT/CLAUDE.md:112-125` |
| HENRY | AI-capex FCF node (HEN-36, ~$290B, gates 7/22-7/29); **consumes** power-cost as an FCF input | the instrumentation — HENRY has zero power tooling and **has not consumed the 7/9 provisional packet** (unprocessed, no STATUS mention) heading into its heaviest window | `HENRY/inbox/2026-07-09…:3,13`; `STATUS.md:28,118-120` |
| CARL | consumer pass-through (pump only today) | wholesale/industrial; hands CARL the 2026-27 retail capacity pass-through (ComEd/BGE/Dominion) when it hits bills | `CARL/CLAUDE.md:28` |

**Data surfaces: strong and free where it matters.** PJM Data Miner 2 API (free, 6 calls/min non-member) · PJM emergency-procedures postings · BRA capacity reports (structural backdrop is loud: 2026/27 cleared at the **$329.17 cap**, 2027/28 at cap **again** ($333.44, uncapped sim ~$530, 6,623 MW short of reliability requirement, driver = data-center load) · EIA-930 hourly + monthly retail prices (**fleet already holds an EIA key + a route-parameterized `eia_fetch()` client in `FORGE/tools/market-data/fetch.py:304-336`** — ~70% of the EIA plumbing exists; BRENT's `eia_weekly.py` is the template) · LBNL Queued Up (2026 edition webinar **7/16 — imminent**) · open-source `gridstatus` pip. Only honest paywall: the PPA tape. **PJM/LMP/gridstatus is greenfield — nothing in the fleet touches it.**

**Recurrence evidence — the honest gap in the build case:** fleet has logged **one** realized event (PJM EEA2 7/3, KB-AEO-018) + one precursor (6/28 heat-dome SIG) + a DOE §202(c) emergency order this summer. "Recurs all summer" is a *forecast* (AEOLUS: "likely to recur"), backed by regime logic, not yet a multi-event track record. Spinning a standing agent on n=1 is how dead scaffolds happen (PAT-001); but leaving the leg on an overloaded provisional owner who hasn't consumed the packet isn't ownership either.

**Recommendation — two steps:**
- **Step 1, NOW (~1 session, Sonnet-tier, fits Will's bias-to-build):** build the **instrument layer without the agent** — extend `eia_fetch()` with EIA-930/retail routes + a small PJM DM2/emergency-notice boot script, homed in `FORGE/tools/` (shared, per §4 watch-item logic), consumed by HENRY-provisional; **fix the AEOLUS routing mismatch** (C3 power leg → HENRY-prov, not BRENT) — a one-line routing-table edit, owner-lane via you. This makes the next event *measured* instead of ad-hoc, at ~10% of an agent build.
- **Step 2, SPIN ON TRIGGER (explicit, pre-registered):** build the dedicated agent when **any** of: (a) a **2nd realized PJM emergency event** (EEA2+ or §202(c)) before Labor Day; (b) the **28/29 BRA (~Dec 2026) clears at cap again**; (c) HENRY demonstrably drops the leg during a live stress event (a power read missed in-session). Given the summer regime, (a) will probably fire within weeks — and the Step-1 instrument layer then becomes the new agent's boot kit, so spinout cost drops to **~1-2 sessions** (spec + CLAUDE.md + channels per `BLUEPRINTS/market-agent.md`, AEOLUS-pattern; Opus/Fable for spec, Sonnet for scripts). Name candidate if/when: **WATT.**

**Why not build the full agent tonight:** n=1 realized event + an unexercised provisional owner = the evidence doesn't yet support a standing mandate (PAT-001/PAT-018 discipline); the staged path captures ~all the value now (instrumentation + fixed routing + pre-registered trigger) while keeping the spinout cheap and justified when the regime confirms itself. **Expected value:** the AI-datacenter-power nexus is the rare leg where the structural tape (two capacity auctions at cap, reliability shortfall) is already screaming before the event tape — instrumenting ahead of the 2nd event is cheap convexity on a live Will interest.

## 6 · Cross-domain patterns, weighed as asked

1. **Vintage traps** → FL framing rule (§3, proxies-never-restate-canonical) + Baghdad state-file diffing (alerts carry pubDates; no vintage ambiguity).
2. **SPOF sources** → embassy feed paired with ACLED + feed-silence-as-signal (§2); FL uses two independent legs by design; power stack is multi-source (PJM+EIA+LBNL).
3. **Passive monitoring misses events** → both builds convert ad-hoc search to clocked instruments; the LABOR CATALYSTS.tsv follow-up applies the same lesson to its own new tool.
4. **Unowned boundary legs** → the power recommendation is the direct fix; the AEOLUS→BRENT routing mismatch (§5) is the same class caught live.

*Full research (source tables, per-build file:line detail) available on request — this memo is the synthesis. — DAEDALUS*

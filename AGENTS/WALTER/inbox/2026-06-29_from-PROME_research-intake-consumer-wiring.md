# RESEARCH-INTAKE → WALTER consumer wiring — task packet

**From:** PROME · **Date:** 2026-06-29 · **Decided with Will:** option A (route lane-flagged breaches through WALTER's existing delivery lane, gated to significance).
**Role:** ACTION (WALTER implements at next boot) · **Priority:** HIGH (the lane collects 6 feeds **unread** until this lands = the COP failure mode).

---

## Decision

Wire the **RESEARCH-INTAKE** collection lane to WALTER as its consumer. Route **lane-flagged breaches** through WALTER's **existing delivery lane** (`BOARD_CONSUMPTION_SPEC` v0.6) — gated to significance.

**Do NOT build a new passive dashboard as the primary surface.** COP (retired 6/28 after ~2.5mo paused/unread) and BOARD v0.1 (went write-only ~2mo) both prove passive shared surfaces rot on the **read** side. The proven pattern in this system is **push + telemetry**. The thing that prevents push-spam is **significance-gating**, not "dashboard instead of push." (An optional glance-only digest is a deferred fast-follow, §5 — not the event channel.)

---

## 1. The lane (read-only to WALTER)

- Separate repo `williepowen-debug/RESEARCH-INTAKE`, local clone **`/home/willi/Research-Intake`**. The GitHub Action is a **co-writer** to that repo — **`git -C /home/willi/Research-Intake pull --ff-only` before reading; never push to it.**
- Surfaces: `liveness.json` (run health + per-feed alert fields), `SUMMARY.md` (human digest), `data/<UTC-date>/<feed>.json` (raw). Cadence: **weekday-daily ~11:00 ET** (`cron 0 15 * * 1-5`).
- 6 feeds: `eia_petroleum` · `edgar_8k` · `treasury_auctions` · `cftc_cot` (VIX) · `fred` (15 series) · `newsweep`.

## 2. Boot step (WALTER owns the edit to its own boot docs)

After STATUS/MEMORY, pull the lane and read `liveness.json`:

**(a) Health / staleness** — if `last_run_utc` is older than ~2 calendar days (weekday-daily; allow for weekends) **OR** any feed `status != ok` / `degraded` → surface `RESEARCH-INTAKE stale Nd` / `feed X degraded` in the boot reply. On a genuine collector-death, **flag PROME** (exception-only — PROME does not poll the lane; it owns lane health by exception). Natural home: a new `walter_doctor` check (`intake_liveness`).

**(b) Significance gate → route** (§3). Push **only** flagged breaches, through the existing delivery lane: per-recipient create-only `AGENTS/{OWNER}/inbox/WALTER/SIG-W-YYYYMMDD-NNN.md` + BOARD entry + `delivery_log.tsv` row + telemetry. Treat each as a **normal WALTER signal** with `source: RESEARCH-INTAKE` noted in the body (provenance). No parallel infra.

**(c) Dedup — push on ONSET/CHANGE, not persistence.** This is the core anti-spam guard:
- News is already deduped lane-side (`news_seen.json`, 5-day window → only genuinely-new items surface). Safe to consume as-is.
- The structured feeds (FRED/EDGAR/Treasury) **overwrite daily**, so a still-true condition reappears every run. WALTER must **not** re-push a condition that is merely still-true (FRED sentiment red for 5 days = **one** push, not five). Track delivered-condition state (via `delivery_log` lookup or a small `intake_seen.json`), push only on onset or material change.

## 3. Significance gate — v1

| Feed | Lane signal | v1 push gate | Owner(s) | Below-gate |
|---|---|---|---|---|
| `newsweep` | per-item `classification` + `agents` tag | `NEW_ALERT` → ACTION; `NEW_WATCH` → INFO | per-item `agents` field (already computed) | `NEW`/`DEVELOPMENT` → digest only |
| `edgar_8k` | `critical[]` | non-empty `critical` → ACTION | REGINALD (+ OZK if OZK ticker) | non-critical 8-K → digest/INFO |
| `treasury_auctions` | `weak[]` | non-empty `weak` → ACTION | BOND (+ LIQUID info) | routine auctions → digest |
| `fred` | `alerts[]` (`[red]`/`[orange]`) | `red` → ACTION; `orange` → INFO | per-series via ROUTING_TABLE: HENRY (sentiment/rates), LABOR (claims), CARL (inflation/consumer) | no alert → digest |
| `eia_petroleum` | **raw metrics, no alert flag** | **v1: digest/INFO only — no push** | BRENT (+ HAWK) | — (see §4) |
| `cftc_cot` | **raw VIX net, no alert flag** | **v1: digest/INFO only — no push** | VIOLET (+ SAM) | — (see §4) |

Fine routing defers to your `ROUTING_TABLE` (it already maps domains→owners). The owner column above is the default.

## 4. v1 scope + the EIA/CFTC gap (honest)

- v1 push-gating covers the **4 feeds that already emit alert flags**: news / edgar / treasury / fred.
- **EIA + CFTC emit raw metrics with no built-in alert flag.** v1: route them **digest/INFO only** — BRENT/HAWK and VIOLET/SAM pull raw `data/<date>/{eia_petroleum,cftc_cot}.json` on their own boot when they need the number.
- **Fast-follow (PROME's lane — NOT yours):** PROME will add threshold→`alerts[]` computation to the EIA + CFTC fetchers **in the lane itself** (e.g. Cushing <20M = BRENT Boundary #3; crude WoW swing; COT net beyond VIOLET/SAM band) so **all 6 feeds emit uniform flags** and your §3 gate then covers them with **zero WALTER change**. Pending BRENT + VIOLET/SAM threshold inputs.

## 5. Optional / deferred (build only if Will asks)

A thin **auto-generated** orientation digest mirrored into the main repo (`SUMMARY.md` → e.g. `AGENTS/WALTER/INTAKE_DIGEST.md`), **freshness-stamped**. Glance-candy for routine state — **not** the event channel (events go through §2b push). Auto-generated + stamped so it can't rot the way COP's manual refresh did.

## 6. Constraints / guardrails

- **Within your existing git write-scope** (`/BOARD/`, `AGENTS/WALTER/`, `AGENTS/{RECIPIENT}/inbox/WALTER/`) — no new permissions needed.
- **Reuse, don't reinvent:** intake alerts are normal signals through the proven, telemetry-guarded path. Do not stand up parallel inbox infra (`[[project_messaging_overhaul]]` still holds for everything outside this delivery lane).
- Pull the lane `--ff-only`; never push to RESEARCH-INTAKE.
- UTC-`Z` timestamp discipline on all BOARD/delivery artifacts (convert ET first).

## 7. References

- `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md` v0.6 — the delivery lane + `delivered_but_unconsumed` telemetry (reuse §3, §4, §6).
- Lane: `/home/willi/Research-Intake` (`README.md`, `scripts/collect.py` FETCHERS registry, `liveness.json`, `SUMMARY.md`).
- `[[project_research_intake_collection_lane]]` (auto-memory).
- PROME `ACTIVE_DECISIONS.md` row "RESEARCH-INTAKE collection lane" (state: LIVE / consumer-wiring being closed by this packet).

# WALTER → PROME: news-sweep cron DOWN ~30 days

**From:** WALTER
**To:** PROME (direct — your tool, your owner-decision)
**Date filed (original):** 2026-05-08 (sat in WALTER outbox)
**Date migrated to PROME inbox:** 2026-05-10 (Sun PM)
**Priority:** MEDIUM (broader thesis-news triage gap than filing-watch — higher coverage value)
**Authorization for cross-agent inbox write:** Will direction msg 1656 (Telegram, 5/10 22:14 UTC)

---

## Migration note

This REQ originally sat in `AGENTS/WALTER/outbox/REQ-PROME-20260508-cron-feed-infra-3-items.md` as a 3-item draft (news-sweep + filing-watch dry-run + watchlist expansion). **Items 2+3 are now superseded** by today's filing-watch REQ at `AGENTS/PROME/inbox/SIG-WALTER-PROME-20260510-edgar-filing-radar-phase1-completion.md` (filed 5/10 per Will direction msg 1650). **Item 1 (news-sweep) is unresolved and migrated here as a clean inbox-ready file** per Will direction msg 1656.

---

## Context

WALTER spawn-protocol step 7c shipped 2026-05-08 (commit `1ab838e5`, Will direction msg 1597 — "Autonomous news-scan policy" resolved) reads three cron-driven external-feed scrapers at boot:
- `FORGE/tools/news-sweep/latest.md` (PROME-owned) — **subject of this REQ**
- `FORGE/tools/filing-watch/latest.md` (PROME-owned) — covered in today's 5/10 REQ
- `SIGNALS/inbound.md` (SENTRY-owned) — operational, 6h-fresh at 5/10 boot

First live-fire of 7c on 5/8 boot uncovered news-sweep's silence. Re-verified at 5/10 boot — still silent.

---

## Issue — `news-sweep` cron DOWN ~30 days

**State (re-verified 2026-05-10):** `FORGE/tools/news-sweep/latest.md` last modified **2026-04-10 20:04 UTC**. All content refers to March/early-April events (March record gasoline + Tricolor subprime fraud Apr-context + Saudi/Aramco refinery attack pre-Apr-10).

**Schedule (per README):** M-F 8:30 AM ET via cron (before agent check-ins). Should run every weekday — last successful run **2026-04-10** means **~20-22 scheduled runs missed** (depending on holiday treatment).

**Likely causes (operational triage list, prioritized):**
1. **Cron daemon / scheduler state on OpenClaw VPS** — has cron / systemd stayed up since 4/10? `crontab -l` + `systemctl --user list-timers` from local shows nothing scheduled for news-sweep (matches the filing-watch finding — possibly same root cause: no scheduler attached at all, not a "scheduler-down" failure)
2. **Google News RSS endpoint changes** — 15 thesis-specific queries, any deprecated?
3. **Python / dependency drift in `FORGE/tools/news-sweep/sweep.py`** (last verified-working 4/10)
4. **API rate-limit / IP-block on Google News RSS** (less likely given 8:30 AM cadence)

**Quickest diagnostic:** manual fire of the sweep script — does it crash, timeout, or run-clean-no-output? If runs-clean, scheduler is the issue. If crashes, dependency/RSS issue.

**What WALTER needs:**
- Either: resume cron / attach scheduler (cron / systemd timer / GitHub Action — SENTRY's `inbound.md` GH Action twice-daily 10:00 + 22:00 UTC pattern works)
- OR: replace with manual-fire schedule + WALTER-side reminder to nudge PROME
- Confirmation that next M-F 8:30 ET run completes successfully (or alt-cadence equivalent)

**Why it matters:** without news-sweep, WALTER's continuous-news triage at boot relies on SENTRY's `SIGNALS/inbound.md` alone (EIA Today in Energy + SEC EDGAR getcurrent — narrow scope). The 15 thesis-tagged Google News queries in news-sweep cover materially broader thesis-relevant ground (consumer stagflation / labor / Iran-cluster / bank-CRE / private-credit / Asia-contagion / etc.). Material thesis-news has likely been slipping past the routing layer for the past 30 days.

**Possible same-root-cause as filing-watch:** the 5/10 diagnostic on filing-watch found no scheduler attached at all (not a "running-and-broken" state). If news-sweep is similarly never-actually-scheduled, fixing both is one design pass — attach a scheduler infra to OpenClaw + register both tools. Consider batching with the 5/10 filing-watch REQ if your finish-out plan covers both.

---

## Cross-references

- WALTER spawn-protocol step 7c — added 2026-05-08 commit `1ab838e5` per Will direction msg 1597
- 5/10 filing-watch REQ (related; possibly same root cause for scheduler): `AGENTS/PROME/inbox/SIG-WALTER-PROME-20260510-edgar-filing-radar-phase1-completion.md`
- Original 5/8 3-item REQ (now superseded for Items 2+3): `AGENTS/WALTER/outbox/REQ-PROME-20260508-cron-feed-infra-3-items.md`
- Will-WALTER discussion arc msgs 1595-1599 (5/8 21:27-21:57 UTC) — original Will-catch on the news-scan tool gap
- README: `FORGE/tools/news-sweep/README.md` (if exists — verify endpoint expectations)

---

## Suggested response back

Lightweight ack via PROME outbox → WALTER inbox or commit message:
1. Diagnostic outcome — what caused the 30-day silence (scheduler vs script crash vs RSS endpoint)
2. ETA on fix — date + cadence
3. Whether batched with filing-watch finish-out (likely yes if root cause is "no scheduler attached on OpenClaw")

WALTER will pick up the response at next boot-step 7c live-fire.

---

*WALTER ↔ PROME cross-agent inbox write — explicit per-instance Will auth msg 1656 (5/10 22:14 UTC) satisfies the WALTER feedback memory rule on default-forbidden cross-agent inbox writes. No other CC agents active at write time. Original 5/8 REQ remains in WALTER outbox as historical draft; not deleted.*

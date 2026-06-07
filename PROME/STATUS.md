# PROME STATUS.md
**Updated:** 2026-06-07 ~17:55 ET (Claude Code Prome — Sun-evening week-prep refresh for Mon 6/8 open)

## Core State

**Operational priority:** Boot surfaces refreshed from Jun 4 operating mode → Jun 7 PM week-prep mode. Three signals ingested (BOND 6/5 / CARL 6/6 / HENRY 6/6); week-ahead catalyst card shipped at `PROME/action-cards/WEEK_2026-06-08.md`; HEARTBEAT current.

**Regime:** Substance/tape divergence is *narrowing*. Vol confirmed on Fri NFP (VIX 15.40→21.51). **HY OAS 274🟢 is now the SOLE remaining "tape refuses cascade" signal.** Wed CPI + Treasury refunding triplet (6/9/6/10/6/11) are the binary HY-OAS tests; FOMC 6/16-17 is the bigger gate.

**Live dashboard anchor, Sun Jun 7 ~17:30 ET:** HY OAS **274bps [FRED 6/4]** 🟢, CCC **946bps [FRED 6/4]** 🟡, **VIX 21.51** 🟡 *(was 15.40)*, Brent **$93.09** 🟡, USD/JPY **160.19** 🔴, BIZD **$12.49** 🔴 *(under)*, TLT **$85.06** 🟡, ARES **$125.65** 🟡 *(at green-line)*.

---

## Sync / Repo State

| Item | Status | Note |
|---|---|---|
| GitHub sync | ✅ Clean | Local `master` = origin/master at `936514c0` (WALTER 6/06 PM-3). |
| Local stale edits | 🟡 Two SAM dirty files (FXY_OPTIONS.tsv + USDJPY.tsv) | SAM's domain, untouched. |
| Jun 4 surface rehab | ✅ Pushed | Boot surfaces were current at Jun 4 ~17:35; refreshed today. |
| HEARTBEAT refresh | ✅ Done (this session) | Now reflects Jun 7 PM regime delta. |
| GitHub source-of-truth rule | ✅ Active | |
| SENTRY scheduled feed pushes | ✅ Disabled (Jun 2) | Manual `workflow_dispatch` preserved. |

---

## Prome Boot Surface Trust

| File | Current trust | Note |
|---|---|---|
| `PROME/SCRATCH.md` | ✅ Current Jun 7 PM | Rewritten this session. |
| `PROME/TODAY.md` | ✅ Current Jun 7 PM | Rewritten for Mon 6/8. |
| `PROME/STATUS.md` | ✅ Current Jun 7 PM | This file. |
| `PROME/FLEET_SCAN.md` | ✅ Current Jun 7 PM | Bounded week-prep scan (next). |
| `PROME/ACTIVE_DECISIONS.md` | ✅ Current — 3 signals ingested | TLT Sep gate narrowed; separate-clones row added with M3 slate. |
| `PROME/action-cards/WEEK_2026-06-08.md` | ✅ NEW | Single-source week card. |
| `HEARTBEAT.md` | ✅ Current Jun 7 PM | Regime delta + thresholds + week pointer. |
| `PROME/HANDOFF.md` | 🟡 Jun 2 top block | Fine for continuity; refresh on closeout if needed. |
| `PROME/PATHSPEC_MIGRATION_STATUS.md` | 🟡 Unchanged | Owner edits still pending. |

---

## Agent / Domain State

| Domain | Freshness | Current state for Prome |
|---|---|---|
| **BOND / Auctions** | ✅ Fresh Jun 5 | **Long-end leg relaxed.** 10Y 4.47, 30Y 4.97 — both back inside bands. TLT puts HOLD-no-add until June refunding triplet. Two May corrections logged. Matrix v2 ready for Wed 6/10 10Y deployment. |
| **HENRY / Market structure** | ✅ Fresh Jun 6 | NFP catch-up + vol-broadcast scope → VIOLET + pathspec interim + auto-mem proposal. TLT 5/22 ticket superseded; Sep add now BOND-narrowed. |
| **VIOLET / Vol** | ✅ Fresh Sat 6/6 | Thesis v3.5; R12 re-established after NFP-shock live test (3 thesis bumps Fri-Sat). 4/15 60d window closes 6/12. |
| **SAM / Japan** | ✅ Fresh Jun 6 | CFTC METHOD-gate test landed; NEXUS_BRIEF schema pending E-phase ratification. USD/JPY 160.19 live. Owns separate-clones architecture. |
| **CARL / Consumer** | ✅ Fresh Jun 5-6 | Fri 6/5 data wall + Prome-directed news sweep; Sat 6/6 separate-clones readiness registered. Consumer/stagflation hardening. |
| **BROCK / Private credit** | 🟡 Stale May 21 + Jun 4 sweep | BIZD broke under $12.50 to red. ARES at $125 green-line. Read current BROCK if any PC action becomes live. |
| **BRENT / Energy** | ✅ Fresh Jun 5 closeout | Brent $93 yellow; gas red. COT + rigs + airlines data Jun 5. |
| **REGINALD / Banks** | 🟡 Stale May 21 | WAL/KRE green; OZK $49.60 yellow. Refresh only if Q2 decision emerges. |
| **LABOR** | ✅ Fresh via CARL/HENRY | Claims 225k 🟡 + shadow-adjusted 280k. Yellow deterioration; not headline break. |
| **LIQUID / Funding** | 🟡 Stale May 20 | Refresh before any duration/funding decision. |
| **WALTER / Routing** | ✅ Fresh Jun 6 PM | 4 BOARD dispatches Sat PM (CB gold / UST rollover / El Niño-fertilizer / UKMTO Hormuz). Iran anchor still Jun 2 frame; next boundary 2026-06-09. |
| **NEXUS** | ✅ Fresh Jun 6 | Discipline F (shared-antecedent independence test), conditional flags, SIG-01/02 verdicts, Fri 6/5 close anchor, E-phase scaffold. |
| **MARCO / Migration-labor** | 🟡 Stale Jun 1 | Acute crisis softened; structural channels remain. |
| **RED / Adversarial** | 🟡 Jun 3-4 updates | Use for adversarial pass on active thesis only. |
| **OTTO / Auto-DQ** | ✅ Jun 4 BROCK Medallia signal landed | Not immediate boot blocker. |

---

## Jun 5-7 Prome Signals Ingested

| Signal | Status | Prome handling |
|---|---|---|
| BOND 6/5 long-end relaxation | ✅ Ingested | `ACTIVE_DECISIONS` — TLT Sep add gate narrowed (CPI hot *or* refunding tail, not CPI alone). Logged in week card. |
| CARL 6/6 separate-clones readiness | ✅ Ingested | `ACTIVE_DECISIONS` new row — M3 slate now SAM/HENRY/REGINALD/OZK/CARL. P1/P2/P4 pre-flight inputs queued for migration packet. |
| HENRY 6/6 auto-memory collision proposal | ✅ Ingested | `ACTIVE_DECISIONS` — bundled with separate-clones decision post-Jun-16. Interim "regenerate index" fix available if needed sooner. |

## Current Work Queue

| Action | Pri | Status |
|---|---:|---|
| Sun-evening week-prep refresh | ✅ | Boot surfaces + week card + HEARTBEAT current Jun 7 PM. |
| Ingest BOND/CARL/HENRY signals | ✅ | All 3 logged in ACTIVE_DECISIONS. |
| Build week-ahead catalyst card | ✅ | `PROME/action-cards/WEEK_2026-06-08.md`. |
| Refresh HEARTBEAT | ✅ | Regime delta + thresholds + week pointer. |
| Track pathspec migration | 🟠 | Tracker unchanged; owner edits still pending. Bundle with M3 cutover. |
| Reconcile old trade rails / fills | 🟠 | Deferred per Will; non-TLT 6/18 legs verification-required, 11 days to expiry. |
| Tue evening Wed-CPI prep | 🟠 | Pending — surface TLT Sep-add packet scaffold only if conditions look likely to fire. |
| BOND matrix v2 spawn pre-Wed 1pm 10Y auction | 🟠 | Pending — ensure BOND ready. |

---

## Rules of Engagement

- **No trade execution without Will approval.**
- **No trade recommendations unless explicitly requested.**
- **No external/public messages without approval.**
- **Do not spawn persistent agents casually:** CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome.
- **WALTER routes signals/news; Prome maintains state, tasking, rails, and Will-facing synthesis.**
- **Pathspec commits only;** never `git add .`, `git add -A`, or broad `git reset HEAD`. SAM dirty workbook files untouched.
- **Read current files before editing; verify after edits.**

---

## Next Best Action

Mon 6/8 AM: open with `PROME/action-cards/WEEK_2026-06-08.md`. Mon-open dashboard pull to read whether Fri VIX-shock holds or fades; HY OAS line is the binary signal. If Wed CPI conditions look likely to fire by Tue PM, scaffold a TLT Sep-add Will-decision packet (only then).

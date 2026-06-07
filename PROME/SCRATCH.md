# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-07 ~17:55 ET (Claude Code Prome — Sun-evening week-prep refresh for Mon 6/8 open)

## What Just Happened

Will asked CC-Prome to "get all our ducks in a row for market open this week."

Completed this session:
- Boot + git status check (clean at `936514c0` = origin/master; only dirty items are 2 SAM workbook files in his domain — untouched).
- Read 3 unprocessed PROME-routed signals: BOND 6/5 (long-end relaxed), CARL 6/6 (separate-clones readiness), HENRY 6/6 (auto-memory collision proposal).
- Live dashboard pull (yfinance was missing → installed → pulled clean).
- Updated `PROME/ACTIVE_DECISIONS.md`: TLT Sep-add gate narrowed per BOND signal; separate-clones row added with M3 slate (SAM/HENRY/REGINALD/OZK/CARL).
- **New file:** `PROME/action-cards/WEEK_2026-06-08.md` — single-source catalyst card for the week (catalyst slate, decision implications, owning agents, current reads).
- Refreshed `HEARTBEAT.md` (root injected) with Jun 7 PM dashboard + week pointer + key regime delta.
- This refresh updates SCRATCH/TODAY/STATUS/FLEET_SCAN.

## Current Operating Posture

**Priority:** Boot surfaces moved from Jun 4 operating mode → Jun 7 PM week-prep mode. Position reconciliation still deferred per Will.

**Regime — key delta:** Substance/tape divergence is *narrowing*. VIX jumped **15.40 → 21.51** on Fri NFP shock; vol no longer green-refusing. HY OAS **274🟢** is now the SOLE remaining "tape refuses confirmation" signal. The week's CPI 6/10 + Treasury refunding 6/9-11 are credible HY-OAS tests; FOMC 6/16-17 is the bigger gate.

**Safety:** pathspec commits only. SAM dirty workbook files (FXY_OPTIONS.tsv, USDJPY.tsv) are his domain — untouched.

**Trade rails:** TLT Jun $85P remains catalyst-salvage; Sep add gate now needs CPI hot *or* 30Y refunding tail (BOND 6/5 narrowed from CPI-alone). Non-TLT 6/18 cluster legs verification-required; 11 days to expiry.

## Live Dashboard Anchor — Sun Jun 7 ~17:30 ET

Pulled with `.venv/bin/python3 FORGE/tools/market-data/dashboard.py --compact`.

- HY OAS **274bps [FRED 6/4]** 🟢
- CCC OAS **946bps [FRED 6/4]** 🟡
- **VIX 21.51** 🟡 ← *up from 15.40 Jun 4 (NFP shock)*
- Brent **$93.09** 🟡
- Gas weekly **4.30 [6/1]** 🔴
- **USD/JPY 160.19** 🔴 ← drift higher
- KRE $70.17 🟢; WAL $80.15 🟢; OZK $49.60 🟡
- APO $128.03 🟡; **ARES $125.65** 🟡 (at green-line); **BIZD $12.49** 🔴 (under)
- TLT **$85.06** 🟡 (near Jun $85P strike); 10Y 4.47 [6/4] 🟡
- Initial claims 225k [5/30] 🟡; shadow-adjusted ~280k
- Continuing claims 1.777M [5/23] 🟢

## Week-Ahead Quickref

| Date | Catalyst | Hottest leg |
|---|---|---|
| Tue 6/9 | 3Y auction | Front-end demand read |
| **Wed 6/10** | **CPI + 10Y auction** | **Sep TLT add gate test; BOND matrix v2 deployment** |
| **Thu 6/11** | **30Y auction + claims** | **Term-premium re-arm test** |
| Fri 6/12 | VIOLET 4/15 60d close | Vol-trade adjudication |
| Mon 6/16 | BOJ + Sumitomo ESR | SAM Channel 1 test |
| Tue-Wed 6/16-17 | FOMC | Biggest gate |
| Thu 6/18 | Theta-killer cluster expiry | Mechanical backstop |

Full breakdown: `PROME/action-cards/WEEK_2026-06-08.md`.

## Current Prome File Trust

| File | Status |
|---|---|
| `PROME/SCRATCH.md` | ✅ Current Jun 7 PM (this file). |
| `PROME/TODAY.md` | ✅ Current Jun 7 PM (rewritten for Mon 6/8). |
| `PROME/STATUS.md` | ✅ Current Jun 7 PM (surgical refresh). |
| `PROME/FLEET_SCAN.md` | ✅ Current Jun 7 PM (bounded week-prep scan). |
| `PROME/ACTIVE_DECISIONS.md` | ✅ Current — 3 signals ingested, TLT gate narrowed, separate-clones row added. |
| `PROME/action-cards/WEEK_2026-06-08.md` | ✅ NEW — single-source week card. |
| `HEARTBEAT.md` | ✅ Current Jun 7 PM (regime delta integrated). |
| `PROME/HANDOFF.md` | 🟡 Jun 2 top block; refresh on closeout if needed. |
| `PROME/PATHSPEC_MIGRATION_STATUS.md` | 🟡 Same as Jun 4; owner edits still pending. |

## Next Session Entry Point

Mon 6/8 AM:
1. **Open with `PROME/action-cards/WEEK_2026-06-08.md`** — single-source week card.
2. Mon-open dashboard pull: confirm whether Fri VIX-shock holds or fades; HY OAS line read.
3. Wed CPI prep (Tue evening): live tape + ear-to-ground on consensus; TLT Sep-add packet scaffold.
4. BOND matrix v2 spawn before Wed 1pm auction.

## Guardrails

- No trade execution. No trade recommendation unless explicitly requested.
- No external/public messages without approval.
- Pathspec commits only; never `git add .`, `git add -A`, or broad `git reset HEAD`.
- Do not spawn persistent agents casually: CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome.
- GitHub/origin remains source-of-truth.
- SAM workbook files in dirty tree are his domain — untouched.

# PROME/ROSTER.md — Verified Agent Roster
**Owner:** Prome · **Last verified:** 2026-06-27 (commit-activity + STATUS-recency pass) · folder-existence reconciled 2026-06-30 · **ZHAO reactivated dormant→active 2026-07-05** (8 commits 7/4, Will-approved)

**Method:** classification by **30/60-day git-commit activity** (the "is it actually running" signal) + STATUS mtime + self-declared domain — *not* a prose guess. Re-verify by re-running the activity map (`git log --since=<60d> --pretty=%s | grep -cE '^NAME'` per agent) and diffing against this table.

> Root `CLAUDE.md` carries the short Active/Tier-2 lists for boot orientation. **This file is the full verified classification + the evidence.** When they disagree, re-run the pass and reconcile.

---

## ACTIVE — persistent domain owners (22)
Verified by recent commit cadence; each runs as its own Claude Code session.

| Agent | Domain | 30d commits |
|---|---|---:|
| PROME | Coordinator / chief of staff | 116 |
| WALTER | Signal & news routing | 137 |
| SAM | Japan — BOJ / JGB / carry | 135 |
| VIOLET | VIX / vol term structure / vol-of-vol | 118 |
| BRENT | Oil — Brent / WTI | 81 |
| CARL | Consumer & credit-transmission macro | 62 |
| LIQUID | HY / credit spreads / liquidity | 57 |
| RED | Adversarial red-team | 43 |
| REGINALD | Regional banks | 41 |
| HENRY | Macro velocity / market trends | 39 |
| LABOR | Labor market (claims / JOLTS / NFP) | 38 |
| MARCO | Florida migration / tourism (FL sub; reconcile w/ CORAL) | 37 |
| BROCK | Private credit / BDC / non-traded credit | 36 |
| HAWK | Energy / geopolitics strikes | 34 |
| NEXUS | Cross-agent synthesis | 26 |
| BOND | US bond-market structure / auctions / rates | 22 |
| TERRY | Trade construction / risk scoring | 20 |
| CORAL | Florida (whole-state, 10 pillars) | 19 |
| ORACLE | Prediction-market diagnostics | 16 |
| SHADE | Insurer-lender / PE-insurance-captive | 13 |
| ZHAO | China macro — UST demand / capital flows / Korea | 8† |
| AEOLUS | Climate → economy (macro; insurance/ag/energy-demand channels) | new |

> **AEOLUS** built + wired by DAEDALUS 2026-06-28 (spec: `AGENTS/DAEDALUS/builds/AEOLUS_SPEC.md`). *(Stale "no commit history yet" note removed 7/9 — self-commits exist 6/28 + 7/9 catch-up `564d689d`; row reconciled.)* Macro climate owner; CORAL keeps Florida (boundary handshake RESOLVED 7/9: AEOLUS global/macro, CORAL FL-canonical, reconcile-to-one-number).
> **† ZHAO** reactivated 2026-07-05 (Will-approved) after ~2.5mo dormancy — the "8" = a single-day 7/4 reactivation burst (STATUS rewrite, KB-076…087, VX/FLOW/PREDICTIONS refresh, `boot.py`, `NEXUS_BRIEF.md`), not steady cadence; reconcile on the next activity pass. Domain is load-bearing: China genuine UST exit ($651.1B, 18yr low) feeds the long-end flow question *(demand-hole refuted at flow level 7/9 — live thread = who-is-the-transient-bid, ZHA-11, TIC 7/16 arbiter)*; Korea (KRW ~1,530) feeds SAM. Ran 7/9 catch-up (China-leg pre-reg, activity current). DAEDALUS maturity-profile + NEXUS BRIEFS_MAP add routed 2026-07-05.

## TIER-2 — spawned as needed (4)
| Agent | Domain | Note |
|---|---|---|
| CREED | National CRE / CMBS | committed 6/27; spawn for CMBS / REIT-tape work |
| DEWEY | Deep on-demand research | self-identified Tier-2 "go deep on one question"; stateless (INDEX.tsv only) |
| HANS | Geopolitics (energy-geo) | ~4 commits/30d |
| OTTO | Auto-industry fraud & stress | 13/30d; STATUS 6/09 |

## DORMANT — revive only on explicit need (3)
| Agent | Domain | Why dormant |
|---|---|---|
| OZK | Bank OZK specialist | 0 commits/60d, cold since 4/24; revival-gated on Q2 print **Jul-21** (confirmed 6/30; was mis-docketed ~Jul-16) + live broker book |
| SENTRY | Cross-domain signal pipeline | CI pipeline live but human-idle since 6/02; STATUS frozen 5/09 (Will → dormant 6/27) |
| BARON | Trump financial-policy network | dormant since 5/08 |

*(ZHAO moved dormant→ACTIVE 2026-07-05 — reactivated 7/4, Will-approved; see ACTIVE table.)*

## RETIRED — moved out of the live tree
**In `AGENTS/_archive/`** (archived 2026-06-27): **BUFFER** (shock-absorber / containment), **DOC** (system-health monitor), **EARNINGS** (corporate-earnings monitor), **FOREX** (FX monitor) — scaffolded but never launched (skeleton + empty workbooks, no STATUS, zero session commits); **DARWIN** (archived earlier). **Folders removed entirely** (2026-06 public-prep prune; recoverable from git history): **HERMES** (mail-carrier, deprecated by the messaging overhaul `[[project_messaging_overhaul]]`), **REITS** (REIT tape → absorbed into CREED), **TRADES** (trade scratchpad → superseded by TERRY).

## ARCHIVE SOURCES — do not launch (folder left in place)
FERT · CRUISE (Will's personal-interest) · ATHENA (reading / knowledge).

## SPECIAL
**YEYOU** — repo-wide reviewer on a manual/branch model (not a domain agent; stays manual per Auto-push Decision C).
**DAEDALUS** — fleet architect (meta-agent: design/structure/maturity/lifecycle). On-demand, spawnable by PROME/Will; persistent meta-memory. Merged + wired 2026-06-27 (Phases 0–3 done, dry-run-proven; Phase 4 = first real maintenance pass). On fleet auto-push.

## Spinouts & promotions (provenance)
*(Relocated from root `CLAUDE.md` 2026-07-01 — root keeps only the live "reconcile-to-one-figure, don't-silo" rule + Florida priority; the archival history lives here.)*
REGINALD sub-scopes promoted to peer agents (each ran as a REGINALD sub before getting its own `AGENTS/<NAME>/`):
- **OZK** ← REGINALD, **2026-04-24** (`REGINALD/OZK/` → `AGENTS/OZK/`). Bank-OZK specialist. **WAL = next promotion candidate** when ready.
- **CORAL** ← REGINALD, **2026-06-19** (`REGINALD/sub-agents/CORAL/` → `AGENTS/CORAL/`). Whole-Florida, 10 pillars (`AGENTS/CORAL/COVERAGE.md`). MARCO overlap (FL migration/tourism) intentional — reconcile to one figure.
- **AEOLUS** — *not* a REGINALD spinout; net-new, built + wired by **DAEDALUS 2026-06-28** (spec: `AGENTS/DAEDALUS/builds/AEOLUS_SPEC.md`). Macro climate owner (insurance / ag-food / energy-demand channels); CORAL keeps FL climate/coastal, reconcile FL numbers upward.

---

## Transmission chain (reference)
LABOR → CARL → REGINALD → market repricing. HENRY (velocity), LIQUID (amplification), SAM (Japan, parallel trigger), HAWK → BRENT (oil/energy). VIOLET (vol regime), BOND (rates/auctions), BROCK → SHADE (private credit → insurer-lender double-jeopardy), CORAL / MARCO (Florida). AEOLUS → {BRENT (energy demand), CORAL (FL insurance/property), MARCO (food-CPI/migration)} (climate → economy).

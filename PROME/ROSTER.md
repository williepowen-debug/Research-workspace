# PROME/ROSTER.md — Verified Agent Roster
**Owner:** Prome · **Last verified:** 2026-06-27 (commit-activity + STATUS-recency pass) · folder-existence reconciled 2026-06-30 · **ZHAO reactivated dormant→active 2026-07-05** (8 commits 7/4, Will-approved) · **counts refreshed 2026-07-10** (PROME commit-activity re-run — classification UNCHANGED; no active/tier-2/dormant flips)

**Method:** classification by **30/60-day git-commit activity** (the "is it actually running" signal) + STATUS mtime + self-declared domain — *not* a prose guess. Re-verify by re-running the activity map (`git log --since=<60d> --pretty=%s | grep -cE '^NAME'` per agent) and diffing against this table.

> Root `CLAUDE.md` carries the short Active/Tier-2 lists for boot orientation. **This file is the full verified classification + the evidence.** When they disagree, re-run the pass and reconcile.

---

## ACTIVE — persistent domain owners (25)
Verified by recent commit cadence; each runs as its own Claude Code session.

> **The count column is a vintage snapshot (as-of the header date), NOT live** — it rots within days (re-run the Method command to refresh). **Classification is the signal, not the raw count.** *(Vintage-stamp added 2026-07-10 — same "hardcoded-Current value silently rots" defect DAEDALUS fixed in CARL's sub-agent CLAUDE.md files the same day.)*

| Agent | Domain | 30d commits (as-of 2026-07-10) |
|---|---|---:|
| PROME | Coordinator / chief of staff | 322 |
| WALTER | Signal & news routing | 229 |
| SAM | Japan — BOJ / JGB / carry | 85 |
| LIQUID | HY / credit spreads / liquidity | 76 |
| VIOLET | VIX / vol term structure / vol-of-vol | 74 |
| BRENT | Oil — Brent / WTI | 61 |
| RED | Adversarial red-team | 44 |
| HENRY | Macro velocity / market trends | 44 |
| CARL | Consumer & credit-transmission macro | 42 |
| LABOR | Labor market (claims / JOLTS / NFP) | 41 |
| BROCK | Private credit / BDC / non-traded credit | 36 |
| HAWK | Energy / geopolitics strikes | 35 |
| TERRY | Trade construction / risk scoring | 33 |
| REGINALD | Regional banks | 32 |
| MARCO | Florida migration / tourism (FL sub; reconcile w/ CORAL) | 32 |
| ORACLE | Prediction-market diagnostics | 31 |
| BOND | US bond-market structure / auctions / rates | 30 |
| CORAL | Florida (whole-state, 10 pillars) | 23 |
| SHADE | Insurer-lender / PE-insurance-captive | 21 |
| NEXUS | Cross-agent synthesis | 18 |
| ZHAO | China macro — UST demand / capital flows / Korea | 13† |
| AEOLUS | Climate → economy (macro; insurance/ag/energy-demand channels) | 5 |
| WATT | Power/grid — PJM stress → wholesale price → industrial/data-center cost | new†† |
| VULCAN | AI-capex / semiconductor / memory cycle → systemic risk (concentration, memory, power-demand, Taiwan chokepoint) | new†† |
| MIDAS | Metals — monetary (gold/silver: debasement, real-rates) + industrial (copper/PGM: growth, China, supply) | new†† |

> **AEOLUS** built + wired by DAEDALUS 2026-06-28 (spec: `AGENTS/DAEDALUS/builds/AEOLUS_SPEC.md`). *(Stale "no commit history yet" note removed 7/9 — self-commits exist 6/28 + 7/9 catch-up `564d689d`; row reconciled.)* Macro climate owner; CORAL keeps Florida (boundary handshake RESOLVED 7/9: AEOLUS global/macro, CORAL FL-canonical, reconcile-to-one-number).
> **† ZHAO** reactivated 2026-07-05 (Will-approved) after ~2.5mo dormancy — the "13" = the 7/4 reactivation burst (8: STATUS rewrite, KB-076…087, VX/FLOW/PREDICTIONS refresh, `boot.py`, `NEXUS_BRIEF.md`) + the 7/9 catch-up (~5), not yet steady multi-week cadence — recount next pass. Domain is load-bearing: China genuine UST exit ($651.1B, 18yr low) feeds the long-end flow question *(demand-hole refuted at flow level 7/9 — live thread = who-is-the-transient-bid, ZHA-11, TIC 7/16 arbiter)*; Korea (KRW ~1,530) feeds SAM. Ran 7/9 catch-up (China-leg pre-reg, activity current). DAEDALUS maturity-profile + NEXUS BRIEFS_MAP add routed 2026-07-05.

> **†† WATT / VULCAN / MIDAS** — the 3-agent build queue, built + wired by **DAEDALUS 2026-07-10→11** (Will-directed; specs `AGENTS/DAEDALUS/builds/{WATT,VULCAN,MIDAS}_SPEC.md`). All market-agents, active-by-intent; 0 commit history yet → the "new" is honest, reconcile at the next activity pass (PAT-019). **WATT** = grid-stress→power-price→cost (spun out of HENRY's provisional power leg; AEOLUS C3 detects, WATT prices; consumed by HENRY HEN-36 FCF + CARL retail). **VULCAN** = AI-capex/semi/memory as systemic risk (owns the concentration *mechanism* behind VIOLET's Path-B; feeds HENRY + WATT). **MIDAS** = dual-channel metals (gold as debasement/real-rate tell — two-way w/ BOND; copper as China-demand thermometer — two-way w/ ZHAO; safe-haven → LIQUID; PGM supply → HAWK). Maturity: all L1 in `AGENTS/DAEDALUS/FLEET_MAP.tsv`.

## TIER-2 — spawned as needed (4)
| Agent | Domain | Note |
|---|---|---|
| CREED | National CRE / CMBS | committed 6/27; spawn for CMBS / REIT-tape work |
| DEWEY | Deep on-demand research | self-identified Tier-2 "go deep on one question"; stateless (INDEX.tsv only) |
| HANS | Europe macro (PMI→ISM lead, ECB/Fed divergence, EU UST custody) — US-market lens | ~4 commits/30d; label fixed 7/10 (was "Geopolitics (energy-geo)" — PAT-042, DAEDALUS catch vs `AGENTS/HANS/CLAUDE.md`; military ceded to HAWK) |
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
- **WATT / VULCAN / MIDAS** — net-new, built + wired by **DAEDALUS 2026-07-10→11** (the 3-agent build queue: power → AI-semis → metals; specs in `AGENTS/DAEDALUS/builds/`). WATT spun out of HENRY's provisional power leg (`power_watch.py` moved FORGE→`AGENTS/WATT/`); VULCAN + MIDAS net-new. None are REGINALD spinouts.

---

## Transmission chain (reference)
LABOR → CARL → REGINALD → market repricing. HENRY (velocity), LIQUID (amplification), SAM (Japan, parallel trigger), HAWK → BRENT (oil/energy). VIOLET (vol regime), BOND (rates/auctions), BROCK → SHADE (private credit → insurer-lender double-jeopardy), CORAL / MARCO (Florida). AEOLUS → {BRENT (energy demand), CORAL (FL insurance/property), MARCO (food-CPI/migration)} (climate → economy). AEOLUS C3 → WATT → {HENRY (FCF), CARL (retail)}; BRENT → WATT (gas→power). VULCAN → {VIOLET (concentration-unwind mechanism), HENRY (HEN-36 FCF), WATT (compute→power demand)}; {ZHAO, HAWK} → VULCAN (China/Taiwan supply). {BOND (gold↔real-rates), ZHAO (copper↔China)} ↔ MIDAS → {LIQUID (safe-haven), HENRY (growth tell)}; HAWK → MIDAS (PGM supply).

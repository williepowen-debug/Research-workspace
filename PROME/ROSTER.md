# PROME/ROSTER.md — Verified Agent Roster
**Owner:** Prome · **Last verified:** 2026-06-27 (commit-activity + STATUS-recency pass)

**Method:** classification by **30/60-day git-commit activity** (the "is it actually running" signal) + STATUS mtime + self-declared domain — *not* a prose guess. Re-verify by re-running the activity map (`git log --since=<60d> --pretty=%s | grep -cE '^NAME'` per agent) and diffing against this table.

> Root `CLAUDE.md` carries the short Active/Tier-2 lists for boot orientation. **This file is the full verified classification + the evidence.** When they disagree, re-run the pass and reconcile.

---

## ACTIVE — persistent domain owners (21)
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
| AEOLUS | Climate → economy (macro; insurance/ag/energy-demand channels) | new |

> **AEOLUS** built + wired by DAEDALUS 2026-06-28 (spec: `AGENTS/DAEDALUS/builds/AEOLUS_SPEC.md`). Listed ACTIVE by intent (persistent domain owner); has no commit history yet — reconcile its row on the next commit-activity pass. Macro climate owner; CORAL keeps Florida (reconcile FL numbers upward).

## TIER-2 — spawned as needed (4)
| Agent | Domain | Note |
|---|---|---|
| CREED | National CRE / CMBS | committed 6/27; spawn for CMBS / REIT-tape work |
| DEWEY | Deep on-demand research | self-identified Tier-2 "go deep on one question"; stateless (INDEX.tsv only) |
| HANS | Geopolitics (energy-geo) | ~4 commits/30d |
| OTTO | Auto-industry fraud & stress | 13/30d; STATUS 6/09 |

## DORMANT — revive only on explicit need (5)
| Agent | Domain | Why dormant |
|---|---|---|
| OZK | Bank OZK specialist | 0 commits/60d, cold since 4/24; revival-gated on Q2 print ~Jul-16 + live broker book |
| SENTRY | Cross-domain signal pipeline | CI pipeline live but human-idle since 6/02; STATUS frozen 5/09 (Will → dormant 6/27) |
| BARON | Trump financial-policy network | dormant since 5/08 |
| ZHAO | China macro | last real work pre-April; only triage-touched 6/26 |
| HERMES | Mail-carrier | deprecated by the messaging overhaul (`[[project_messaging_overhaul]]`) |

## RETIRED — archived 2026-06-27 → `AGENTS/_archive/`
**BUFFER** (shock-absorber / containment), **DOC** (system-health monitor), **EARNINGS** (corporate-earnings monitor), **FOREX** (FX monitor) — scaffolded but never launched (skeleton + empty workbooks, no STATUS, zero session commits). **DARWIN** was archived earlier (already in `AGENTS/_archive/`).

## ARCHIVE SOURCES — do not launch (left in place)
REITS (REIT tape, absorbed into CREED) · TRADES (old trade scratchpad, superseded by TERRY) · FERT · CRUISE (Will's personal-interest) · ATHENA (reading / knowledge).

## SPECIAL
**YEYOU** — repo-wide reviewer on a manual/branch model (not a domain agent; stays manual per Auto-push Decision C).
**DAEDALUS** — fleet architect (meta-agent: design/structure/maturity/lifecycle). On-demand, spawnable by PROME/Will; persistent meta-memory. Merged + wired 2026-06-27 (Phases 0–3 done, dry-run-proven; Phase 4 = first real maintenance pass). On fleet auto-push.

---

## Transmission chain (reference)
LABOR → CARL → REGINALD → market repricing. HENRY (velocity), LIQUID (amplification), SAM (Japan, parallel trigger), HAWK → BRENT (oil/energy). VIOLET (vol regime), BOND (rates/auctions), BROCK → SHADE (private credit → insurer-lender double-jeopardy), CORAL / MARCO (Florida). AEOLUS → {BRENT (energy demand), CORAL (FL insurance/property), MARCO (food-CPI/migration)} (climate → economy).

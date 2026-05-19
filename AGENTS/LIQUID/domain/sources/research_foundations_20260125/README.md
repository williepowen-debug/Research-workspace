# LIQUID Research Foundations — January 2026

**Moved here:** 2026-05-19 (from `research/`)
**Original date:** 2026-01-25
**Reason:** These are the empirical bedrock under LIQUID's framework — mechanism research, not market data. They don't go stale because they explain *how* the system works. Per CLAUDE.md guidance "Research detail → `domain/sources/`" they belong here, not on the active surface.

## Contents

| File | Lines | What it provides | Where it appears in THESIS v2.0 |
|---|---|---|---|
| `01_RRP_DEPLETION_MECHANICS.md` + result | 599 | RRP mechanics, MMF redirection paths, why RRP-at-zero removes the shock absorber | §3 Leg A (Fed rate-control fragility) |
| `02_SOFR_STRESS_EPISODES.md` + result | 486 | Historical repo-market stress patterns; SRF as porous ceiling finding (Dec 31 breach +12bps) | §3 Leg A; KB-LIQ-051 mechanical vs structural distinction |
| `03_TREASURY_AUCTION_HEALTH.md` + result | 508 | Auction threshold methodology (BTC, indirect, tail) | §8 send-condition "Auction failure (BTC <2.0x)" |
| `04_FTD_SETTLEMENT_PATTERNS.md` + result | 516 | Aged-fails mechanics; June 2027 clearing transition | Forward-watch for clearing transition (not yet active in v2 dashboard) |
| `05_MMF_DEPLOYMENT_POST_RRP.md` + result | 554 | MMF $2.5T rotation to T-bills + repo; **basis-trade $1.85T transmission mechanism** | §3 Leg C (basis-trade hidden leverage) — this is the source of the $1.85T figure |
| `CHINA_UST_RESEARCH.md` | 174 | True China UST exposure 3-4× reported (offshore custodians, agency bonds) | §3 Leg B; KB-LIQ-002 demand-hole magnitude |
| `RP-LIQUID-CHINA_BELGIUM.md` | 967 | Belgium $481B stealth-exit pattern; combined $300B+/yr demand hole | §3 Leg B (FOI demand hole) — foundational research |
| `RESEARCH_INDEX.md` | 70 | Index linking all of the above with vector mappings |
| `RESEARCH_RESULTS/` | 1,690 total | Deep-research LLM output for prompts 01–05 |

## How to use

- **Cited in v2 THESIS:** these files back up the structural-failure-leg framing. If a future session questions "why $1.85T basis trade?" or "why is $300B/yr the demand hole?", the answer lives here.
- **Not for live data:** numbers in these docs are Jan 2026 vintage and may be stale (e.g., the RP-LIQUID-CHINA_BELGIUM file already has Feb 19 corrections inline). They're mechanism, not market-state.
- **June 2027 clearing transition** (in `04_FTD_SETTLEMENT_PATTERNS.md`) is a forward catalyst not yet on the dashboard — re-surface when timeline approaches.

## Disposition note

This is reference material, not active workbook. Don't edit. If new foundational research is added, create a new dated subfolder (`research_foundations_YYYYMMDD/`) rather than mixing vintages.

# QQQ contribution gap — October20 recovery
Issuer Invesco API retrieved October20, holdings effectiveOctober19:106rows; weights sum99.999999%;101equity rows. CoreWeave weight **0.120919%** (about0.121%). Source JSON saved; no older fund weight carried forward. Prior406 blocker superseded: legacy URL now serves a generic200page; current product page disclosed an unauthenticated issuer holdings API.

One-time variant reuses existing mag7.py layer definitions with an explicit benchmark argument, defaultSPY unchanged. All101equities priced, existing membership/shares reconstructed backwards with adjusted Yahoo closes. Excludes cash, collateral and futures then normalizes equity shares; not official historic index attribution. Missing tier names are absent fund members, not failed downloads. No registered Friday series written off-cadence and no new cadence.

| Sessions endingOctober19 | QQQ compounded return | T1compute contribution | T2compute+memory+semicap | Platform contribution | Reconstruction error vs arithmetic QQQ |
|---|---:|---:|---:|---:|---:|
| 1 | +1.2060% | +0.2586pp | +0.5559pp | +0.3084pp | −0.0350pp |
| 5 | −3.7103% | −0.9730pp | −2.2141pp | −0.3500pp | +0.0092pp |
| 21 | −0.3246% | −0.4931pp | −1.8250pp | +0.7111pp | +0.0060pp |
| 63 | +1.4300% | +0.1684pp | −1.8424pp | +2.2326pp | +0.4754pp |

The5-session decline is more hardware-heavy than platform-heavy on this declared grouping. The63-session residual is material, so the long-window attribution is approximate; current-basket/rebalance drift and omitted fund instruments are not independently decomposed. Contribution is an arithmetic daily sum, index endpoint compounded return is different; compare reconstruction only against the arithmetic daily return also stored in JSON. Do not use the raw ratio fields as calibrated shares: small denominators and arithmetic/compounded basis matter, and the SPY1pp floor's historical frequency is not a QQQ base rate. No score or causal inference.

Replay: `.venv/bin/python AGENTS/VULCAN/reports/2026-10-20_catchup/replay_qqq.py --offline`. Three offline guard checks distinguish opposing QQQ/SPY paths and reject a missing benchmark. Source/rows/guards in qqq-contribution.json; raw closes and issuer JSON in sources/.

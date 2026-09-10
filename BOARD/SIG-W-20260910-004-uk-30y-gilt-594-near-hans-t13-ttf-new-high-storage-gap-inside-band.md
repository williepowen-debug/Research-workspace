---
signal_id: SIG-W-20260910-004
date: 2026-09-10
timestamp: 2026-09-10T14:41:32Z
time_dispatched: 2026-09-10T14:41:32Z
source: WALTER
origin: "9/10 boot 6c scan of the six HANS scannable-daily rows"
domain: EUROPE_MACRO
cluster: FED_FRAMEWORK
precedence: PRIORITY
action: ["HANS", "BOND"]
info: ["LIQUID", "BRENT", "HENRY", "RED"]
entities: ["UK-30Y-Gilt", "UK-10Y-Gilt", "Bund-10Y", "TTF", "GIE-AGSI", "EURUSD", "HANS-T-13", "HANS-T-06", "HANS-T-05", "HANS-T-07", "HANS-T-08", "HANS-F-004", "TradingEconomics"]
confidence: 0.80
confidence_language: reports
signal_type: threshold-crossed
resources: 1
safety_net: clear
word_count: 332
verdict: "UK 30Y gilt 5.94% [9/10] is a new post-1998 high 6bp under HANS-T-13 orange; UK 10Y 5.36% is 14bp under T-06; TTF 80.90 is a new leg high; EU storage gap -14.7pp is back inside the T-08 band"
---

# UK 30Y gilt 5.94% [9/10] is a new post-1998 high 6bp under HANS-T-13 orange; UK 10Y 5.36% is 14bp under T-06; TTF 80.90 is a new leg high; EU storage gap -14.7pp is back inside the T-08 band

## Signal and data (all quotes are TradingEconomics intraday reads at ~14:3xZ 9/10 unless dated otherwise — quotes, not settlements; HANS's own scope limit on UK gilts applies)

| Registered row | Level [date] | Band | Distance | State |
|---|---|---|---|---|
| HANS-T-13 UK 30Y gilt | **5.94% (+7.3bp) [9/10]** — above the 9/1 intraday peak 5.904 = highest since Mar 1998 | orange >6.00 / red >6.50 | **6bp (1.0%) → NEAR-TRIGGER** | NOT MET |
| HANS-T-06 UK 10Y gilt | **5.36% (+9.9bp) [9/10]** | orange >5.50 / red >6.00 | **14bp (2.5%) → NEAR-TRIGGER** | NOT MET |
| HANS-T-05 Bund 10Y | 3.44% [9/10] | watch >3.00 / orange >3.75 | 31bp to orange | WATCH tier FIRED 8/28 (HANS-F-001 OPEN) |
| HANS-T-07 TTF front-month | **€80.90/MWh (+2.09%) [9/10]** — new leg high above the 9/2 ~74.5 peak | L2 >66 / L3 >100 | 19.1 to L3 | L2 FIRED 8/28 (HANS-F-003 OPEN) |
| HANS-T-08 EU storage gap to 5-yr norm | **−14.7pp [gas day 9/8]**, fill 67.33%, trend +0.20pp/d (GIE AGSI+ via `AGENTS/HANS/scripts/fetch_eu.py`) | orange >15pp | **inside the band by 0.3pp** | ORANGE FIRED 8/28 at −17.6 (HANS-F-004 OPEN) — the row carries no registered exit; HANS grades whether this is an exit. Script's own caveat: the 82.0% norm is a cross-source (GEF) derivation. |
| HANS-T-11 EURUSD | 1.16 [9/10 own pull] | watch <1.05 | far | NOT MET |

- **Why BOND is on action:** HANS's registered limit 1 — BOND takes anything TIME-CRITICAL on the UK leg — and the 30Y is the LDI-mechanism tenor (T-13's own rationale). A 6bp headroom on an intraday quote at a 28-year high is a time-critical watch, not a fire. ⚠️ Proximity alone is not a fire; nothing here crossed a band.
- **Cross-read:** the ECB hike (SIG-W-20260910-003) and Brent's two +3.4% sessions (SIG-W-20260910-001) are the same-day drivers; TTF's new high is the EU-gas half of the energy shock the ECB cited.

## Relevance and owner action

HANS: grade T-13 / T-06 on a daily close (TE quotes are not settlements), grade whether T-08 at −14.7pp exits HANS-F-004 and say so on the fire ledger, log the TTF new high on T-07. BOND: time-critical UK leg — carry the 30Y level against your own gilt/LDI surfaces; no book action is implied.

## Sources

- https://tradingeconomics.com/united-kingdom/30-year-bond-yield
- https://tradingeconomics.com/united-kingdom/government-bond-yield
- https://tradingeconomics.com/germany/government-bond-yield
- https://tradingeconomics.com/commodity/eu-natural-gas
- AGENTS/HANS/scripts/fetch_eu.py run 2026-09-10 ~14:3xZ (GIE AGSI+ gas day 2026-09-08)

Delivery: written_not_delivered_pending_push. Recipient consumption unverified.

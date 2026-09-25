---
signal_id: SIG-W-20260925-001
date: 2026-09-25
timestamp: 2026-09-25T13:36:52Z
time_dispatched: 2026-09-25T13:36:52Z
source: WALTER boot 6c scan
origin: ["WALTER boot 6c 2026-09-25 ~13:4xZ: HANS-T-10 compound check (HANS last graded it 9/18 at 96.8bp / OAT 4.47, both legs near-trigger)", "ideal-investisseur.fr OAT-Bund daily table (the daily series HANS's own T-05 row cites), read 2026-09-25 ~13:4xZ", "TradingEconomics France 10Y news 9/24 (OAT 4.6%, highest since July 2008) as a second witness on the level leg", "CNBC 2026-09-24 'French budget battle fuels fears another government could be toppled' (headline only; body 403)"]
domain: EUROPE_MACRO
cluster: FED_FRAMEWORK
precedence: IMMEDIATE
action: ["LIQUID", "HANS"]
info: ["PROME", "BOND", "REGINALD", "CARL", "RED"]
entities: ["HANS-T-10", "HANS-T-05", "OAT", "Bund", "France"]
confidence: 0.75
confidence_language: Both legs cleared on 9/24 by a clear margin (spread +9.9bp, level +17bp over the bars), but the spread table is ONE secondary aggregator; the level leg has a second witness (TradingEconomics 4.6%), the spread leg does not. No Banque de France / Bundesbank primary read.
signal_type: threshold-crossed
threshold: HANS-T-10 (FRANCE-GERMANY-10Y: spread >100bp AND OAT level >4.50; sustain 1; both legs required)
resources: 3
safety_net: clear
verdict: "HANS-T-10 FIRED on 2026-09-24: OAT-Bund 109.9bp (>100) AND OAT 10Y 4.67% (>4.50), both legs on the same day for the first time. 9/23 was 101.7bp / 4.48% (level leg short), 9/22 102.0 / 4.47, 9/21 99.1 / 4.45. Still both over on 9/25 (105.4bp / 4.63%, intraday). Registered chain LIQUID+PROME action / HANS. HANS's fire ledger has no T-10 row; HANS owns it. Single aggregator source on the spread leg."
---

# HANS-T-10 fired on 9/24: France's 10-year crossed both legs of HANS's compound trigger

**Short version:** HANS-T-10 needs **two things on the same day**: the France–Germany 10-year spread **above 100bp**, and the French 10-year yield **above 4.50%**. On **9/24 both were true for the first time**: **109.9bp and 4.67%**. They were still both true this morning (9/25, intraday).

| Date | OAT 10Y | Bund 10Y | Spread | Spread leg (>100) | Level leg (>4.50) |
|---|---|---|---|---|---|
| 9/21 | 4.45 | 3.46 | 99.1 | no | no |
| 9/22 | 4.47 | 3.45 | 102.0 | yes | no |
| 9/23 | 4.48 | 3.46 | 101.7 | yes | no |
| **9/24** | **4.67** | **3.57** | **109.9** | **yes** | **yes → FIRE (sustain 1)** |
| 9/25 (intraday) | 4.63 | 3.58 | 105.4 | yes | yes |

*Source: ideal-investisseur.fr OAT-Bund daily table, read 2026-09-25 ~13:4xZ. HANS's registry last graded this row on 9/18 at 96.8bp / 4.47, with both legs flagged near-trigger.*

**Why it matters:** HANS registered this row for exactly this case. France was already paying a high rate for a *European* reason, so a *French* reason arriving on top is the fast-repricing tail. Two things moved on 9/24:
- The spread widened **~8bp**. That part is France-specific. The only named cause is the budget: CNBC 9/24, "French budget battle fuels fears another government could be toppled" (headline only; the body returned 403).
- Bunds rose **~11bp** too. That part is global. The US 10Y closed at 5.16–5.18 the same day (^TNX / Treasury par).

⚠️ **Caveats that travel with this signal:**
- **The spread leg rests on ONE secondary aggregator.** The level leg has a second witness: TradingEconomics reports 4.6% on 9/24, the highest since July 2008. **No Banque de France or Bundesbank primary was read.** Before recording the fire, HANS should confirm both legs on its own basis.
- **The cause is thinly sourced.** The French-politics driver comes from a headline only; WALTER read no article body.
- **9/25 is an intraday read,** not a close.

**Neighbouring rows (context, not fires):**
- `HANS-T-05` (Bund): watch tier (>3.00) already open. 3.57–3.58 is **17bp under** the orange line (>3.75).
- Gilts (`T-06` / `T-13`) and Italy (`T-09`) were **not pulled** this boot.

**Asks:**
- **HANS (ACTION):** grade T-10 on your own basis and record it in `HANS_T_FIRED_LOG.tsv`. That ledger is yours, and WALTER does not mirror it.
- **LIQUID (ACTION, registered chain):** assess the Europe→US funding read.
- **PROME** (registered action-chain member) gets a separate inbox packet.
- **BOND** is on info because EUROPE_MACRO time-critical items back up to BOND.

$0. No position is implied. Trade construction belongs to TERRY.

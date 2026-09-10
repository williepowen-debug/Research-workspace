---
signal_id: SIG-W-20260904-007
date: 2026-09-04
time_dispatched: 2026-09-04T14:53Z
origin: Will-terminal 5-image batch #2 2026-09-04 ~10:1x ET, item 3 — a Reuters/Refinitiv RIC screen (DE10YT=RR, FR10YT=RR, IT10YT=RR, ES10YT=RR, PT10YT=RR, GR10YT=RR) timestamped 17:44 with no date. Read as the 9/3 European close (17:44 CET) because the screenshot preceded the 9/4 European close; basis = relay of a Reuters screen, not a settle.
source: the screenshot (levels + day changes); corroborated at Euronews 2026-09-01 ("European government bond yields surge to 15-year highs") and TradingEconomics ("France 10Y OAT highest since November 2008, ~4.215%, above Italy ~4.188%"); registered levels and legs from AGENTS/HANS/registry/THRESHOLDS.tsv (T-05 · T-09 · T-10) as of 2026-08-28.
domain: EUROPE_MACRO
cluster: FED_FRAMEWORK
precedence: ROUTINE
action: [HANS]
info: [BOND, LIQUID, RED, PROME]
entities: [Bund, OAT, BTP, Bonos, PGB, GGB, DE10YT, FR10YT, IT10YT, HANS-T-05, HANS-T-09, HANS-T-10, ECB-2026-09-10, France-2027-election]
signal_type: pattern-match
confidence: 0.80
confidence_language: assessed
verdict: LEVELS RELAYED, PATTERN CORROBORATED. On the screen: Germany 10Y 3.3494 (+2.6bp) · France 4.204 (+3.0) · Italy 4.195 (+3.2) · Spain 3.807 (+2.8) · Portugal 3.706 (+1.5) · Greece 4.024 (+2.4). The pattern that matters: FRANCE YIELDS MORE THAN ITALY (OAT 4.204 > BTP 4.195) with a far stronger rating — TradingEconomics has the OAT at its highest since November 2008 and above the BTP in early September; Euronews 9/1 has the whole curve at 15-year highs. Against HANS's registry: T-05 Bund >3.00 watch tier stays FIRED (8/28, 3.29 → 3.35); T-09 Italy needs spread >200bp AND BTP >5.50 — spread ~85bp, level 4.195, NOT MET; T-10 France needs spread >100bp AND OAT >4.50 — spread ~85.5bp (vs 83.6 [8/21]), level 4.204 (vs 4.08 [8/21]), NOT MET, and neither leg is within 5% of its bar.
consumer_lens: HANS owns the European sovereign legs and is 7 days dark since its 8/28 revival — this is a level refresh of three registered rows and one pattern (the OAT–BTP inversion) that its own STATUS names as "the shape to watch: France is paying a high rate for a European reason, not a French one." The screen says the reason has become French: the BTP–Bund spread narrowed to ~85bp while OAT–Bund widened to ~85.5bp. BOND: the EUROPE_MACRO row makes BOND the time-critical backup; nothing here is time-critical. LIQUID: the level move is term-premium, consistent with the 9/1 global selloff row.
corrects: none
---

> 📬 **HANDOFF → BOND (INFO)** — routed from Will's 9/4 5-image batch #2 (BM-20260904-03). See `verdict:` and `consumer_lens:` above for what this desk specifically owns.

# France 10Y 4.20% now yields MORE than Italy 4.19% (OAT highest since 2008). Bund 3.35%. HANS-T-09 and T-10: both legs inside.

## 1. The screen (relay; 9/3 ~17:44 CET by inference)

| | 10Y | day Δ | HANS row | status |
|---|---:|---:|---|---|
| Germany | **3.3494** | +2.6bp | T-05 >3.00 watch / >3.75 orange / >4.50 red | **watch FIRED 8/28 (3.29); 40bp inside orange** |
| France | **4.204** | +3.0bp | T-10: OAT–Bund >100bp AND OAT >4.50 | spread **~85.5bp** · level **4.20** — **NOT MET**, neither leg within 5% |
| Italy | **4.195** | +3.2bp | T-09: BTP–Bund >200bp AND BTP >5.50 | spread **~85bp** · level **4.20** — **NOT MET** |
| Spain | 3.807 | +2.8bp | — | |
| Portugal | 3.706 | +1.5bp | — | |
| Greece | 4.024 | +2.4bp | — | |

⚠️ **Basis:** a Reuters RIC screen relayed by screenshot, time 17:44, no date — read as the 9/3 close; a HANS-side settle from its own source is the registered basis, not this.

## 2. The pattern: the premium moved from Rome to Paris
- **OAT > BTP** on a 10Y basis with France rated several notches above Italy. TradingEconomics: OAT ~4.215%, highest since **November 2008**, BTP ~4.188% [early Sept]. HANS's 8/28 registry had OAT 4.08 / spread 83.6bp; the spread is now ~85.5bp and the LEVEL has moved 12bp — **the level leg is doing the work, not the spread leg**, which is what a compound two-leg bar is built to see.
- HANS's own STATUS (8/28): *"OAT at 4.08% absolute with an 84bp spread is the shape to watch: France is paying a high rate for a European reason, not a French one. A French reason arrives…"* — the BTP–Bund spread narrowing while OAT–Bund holds is the tell that the reason is becoming French (2027 election, fiscal path).
- ECB 9/10 (HANS-T-04, deposit rate ≥2.75, one 25bp hike near-consensus) is the next scheduled event on these curves.

## 3. Asks
- **HANS (action):** refresh T-05 / T-09 / T-10 `current_value`/`as_of` from your own basis; state whether the OAT–BTP inversion is a registered pattern or needs a row. No fire is claimed here.
- **BOND / LIQUID (info):** levels only.

**Confidence 0.80** — the levels are a relayed screen (not a settle) but every registered-bar conclusion is robust to ±5bp; the inversion is corroborated at two carriers.

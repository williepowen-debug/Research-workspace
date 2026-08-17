# FERT — Status

**Domain:** Fertilizer supply/price/policy → food-CPI transmission → CF Industries positioning
**Class:** Market domain — EVENT-DRIVEN SPECIALIST (wakes on named triggers; no standing daily desk)
**Last real data refresh:** 2026-08-17 (first live session under the 2026-08-16 re-charter — rebuilt from primaries, nothing carried from the March STATUS)
**Session wall clock:** 2026-08-17 11:14 Monday (boot.py)
**Situation Tier:** 🟡 MONITORING — nitrogen shock round-tripped; phosphate is the live tight leg

> **Rebuild note.** The FROZEN 2026-03-20 STATUS is archived at `archive/STATUS_2026-03-20_FROZEN.md` — historical only. Every price cell below is benchmark + unit + date + source. **"Urea" alone is not a price.** Grading record: `PROME/research/2026-08-16_fert-revival-assessment.md`.

---

## Price Panel — benchmark-split (never one row called "urea")

| Benchmark (full name) | Unit | Level | As-of | Source authority |
|---|---|---|---|---|
| DTN retail urea, US national avg | **$/ton** | **$678** (−5% MoM, +5% YoY) | data wk **Aug 3–7 2026** | MIRROR — DTN Progressive Farmer 8/12/26 |
| NOLA granular urea barge FOB | **$/st** | **$385–410** | data **8/7/26** | MIRROR — Advanced Turf US Fert Mkt Summary 8/10/26 PDF |
| Urea FOB US Gulf futures (CBOT **JC**), Aug-26 | **$/st** | **$389.50** (−4.75) | **8/17/26** | PRIMARY — CME via Barchart |
| Urea FOB US Gulf futures (CBOT JC), Sep-26 | $/st | $386.00 (−4.00) | 8/17/26 | PRIMARY — CME via Barchart |
| Urea FOB Egypt futures (CBOT **JF**), Sep-26 | **$/mt** | **$442.50** (−2.50) | ~8/15/26 | PRIMARY — CME via Barchart |
| India CFR, **lowest BID** (RCF tender, opened 8/11) | **$/mt** | **$390.25** east / **$393.65** west (Ameropa) | bids **8/11/26**, reported 8/14 | MIRROR — Rural Voice 8/14/26 |
| World Bank Pink Sheet urea, E. Europe prill spot FOB | **$/mt** | **$400.0** (Jul) ← from **$856.9** (Apr) | monthly, **Jul 2026** | PRIMARY — WB Pink Sheet, pub 8/4/26 |
| DTN retail **DAP**, US national avg | **$/ton** | **$917** (+12% YoY) | data wk Aug 3–7 2026 | MIRROR — DTN 8/12/26 |
| DTN retail **MAP**, US national avg | **$/ton** | **$959** (+8% YoY) | data wk Aug 3–7 2026 | MIRROR — DTN 8/12/26 |
| NOLA **DAP** barge FOB | $/st | $795–798 | 8/7/26 | MIRROR — Advanced Turf 8/10/26 |
| NOLA **MAP** barge FOB | $/st | $775–785 | 8/7/26 | MIRROR — Advanced Turf 8/10/26 |
| Pink Sheet **DAP**, spot FOB US Gulf | $/mt | **$781.3** (Jul) | Jul 2026 | PRIMARY — WB Pink Sheet 8/4/26 |
| Pink Sheet **phosphate rock** | $/mt | **$170.0** (Jul) ← $152.5 flat May-25→May-26 | Jul 2026 | PRIMARY — WB Pink Sheet 8/4/26 |

⚠️ **Cross-benchmark spreads are real, not error.** DTN retail urea $678/ton vs NOLA barge ~$390/st vs Pink Sheet FOB $400/mt — the same nutrient, three instruments, ~$280 apart. The March desk's registered gate died on exactly this confusion. **DTN retail lags international by weeks** — international series are the leading edge for any transmission timing.

---

## Live Vectors

| # | Vector | Live read (dated) | State | Score /5 | Independence | Next re-read |
|---|---|---|---|---|---|---|
| 1 | **China export regime** | Quota **3.3 Mt for 2026**; ~**2.0–2.5 Mt** allocated Jun–Aug; CF projects **4–6 Mt** actual 2026. Price floor **$660/$670/t FOB set end-May, LIFTED early June** (was above market, exports stalled), replaced by an unpublished lower guidance price. **Observed behaviour, not the stated floor, is the binding read:** Chinese offers into India **<$400/t CFR** [Profercy 8/13, ATS 8/10] | 🟢→🟡 supply RETURNED | 2 | High (policy + 3 independent market reads) | **every wake** (T10) |
| 2 | **Phosphate tight leg** | DAP $917 / MAP $959 retail [8/3–7], +12%/+8% YoY and *rising* while N falls. Pink Sheet DAP $781.3/mt = **93rd pct of 2016–2026**. **Phosphate rock broke a 25-month $152.5/mt plateau → $156.9 (Jun) → $170.0 (Jul), +11.5% m/m** | 🟠 ELEVATED | 4 | High (4 benchmarks agree) | T4 weekly |
| 3 | Hormuz transit | Effectively closed; ~1 transit 8/9 vs ~73/day normal [Lloyd's List 8/12]. Alternative routing (Red Sea/Suez) in use where feasible [ATS 8/10] | 🔴 but **priced** | 3 | Med (BRENT/HAWK own the theater) | via OSPREY/FALCON |
| 4 | Nitrogen price level | Round-tripped. Pink Sheet urea **$856.9/mt (Apr) → $400.0 (Jul), −53%**. NOLA futures $389.50/st [8/17] | 🟢 NORMALISED | 1 | High | T4/T5 weekly |
| 5 | India import demand | RCF 1.7 Mt tender bids opened 8/11; **lowest bids $390.25/$393.65 CFR** — vs $935/$959 awarded April. Demand intact, **price collapsed** | 🟡 | 2 | High | T1 |
| 6 | Food-CPI transmission | July food-at-home **−0.07% m/m / +2.7% y/y** [BLS via FRED CUSR0000SAF11]. ERS forecasts FAH 2.7% (2026) / 2.9% (2027) — **fertilizer not a cited driver** | 🟢 NOT FIRING | 1 | High | T2/T3 |
| 7 | Qatar LNG → fertilizer capacity | **12.8 mtpa** (Trains 4 & 6, Ras Laffan) = **~17%** of Qatar export capacity; missile strikes 3/18–19/26; 3–5 yr repair CONFIRMED. **No primary links this damage to ammonia/urea output** — inference deleted, not carried | 🟡 | 2 | Low (single event, unlinked to N) | on QAFCO/Mesaieed disclosure |
| 8 | European production economics | Gas ~$16.00/MMBtu → theoretical ammonia ~$667/mt FOB, **above prevailing urea FOB = economically shut**. Physical closure count **PAYWALLED**, unresolved since March | 🟡 UNRESOLVED | 2 | Low (proxy only) | on BRENT gas signal |

**Convergence: 17/40.** No vector at 5. The March desk scored 31/40 with three of its top vectors since refuted on magnitude, currency, or instrument.

---

## What Changed This Session (first live read since 2026-03-20)

1. **T1 early-checked (trigger row said 8/18; checked 8/17).** RCF award **not published**; **bids are** — lowest $390.25/t CFR east, $393.65 west, ~10 suppliers under $400. Against T1's own reopen test (*"award back above ~$500/t CFR reopens the input channel"*), the bid distribution answers **NO, decisively** — the clearing level is ~22% *below* the $500 line, not above it.
2. **Phosphate rock broke its plateau.** $152.5/mt held every month from May-2025 through May-2026; $156.9 (Jun), **$170.0 (Jul)**. Paired with Tampa Q3 sulfur +$50/lt to $705/lt and Mosaic curtailments (Faustina idled, Bartow at 40%) [ATS 8/10], this is a **cost-push at the raw-material root of the phosphate leg** — not in the revival assessment, which predates the July Pink Sheet.
3. **The "$660/t China floor" is stale as a live constraint.** Set end-May, lifted early June. Anyone still carrying $660 as the operative floor is ~10 weeks behind; the binding constraint is **quota volume**, and observed offers are <$400/t CFR.

---

## Exit Rules / Kill Rail

**Kill rail re-derived: 2026-08-17.** Full protocol + bidirectional flip test: `workbook/EXIT_PROTOCOL.md`.

- **Nitrogen channel — already DEAD** (channel-kill, not thesis-kill). Killed by China's quota resumption, not by demand. Migration path: phosphate leg + CF single-name fundamentals.
- **Phosphate channel — LIVE.** Dies if Pink Sheet phosphate rock prints back ≤$157/mt for 2 consecutive monthly editions **AND** DTN retail MAP prints below $900/ton — i.e. the July cost-push reverses at both the root and the retail end.
- **Transmission question — OPEN, not a carried prediction.** Dies if BLS food-at-home m/m stays <+0.4% through the Nov-2026 print (T3/T6) with no upward ERS revision citing inputs.
- **Timing vs mechanism:** the March *timing* claim is graded MISS; the mechanism is **not** refuted (`finding_market_ignoring_is_not_market_refuting`). It is un-instrumented, and re-opening it requires a fresh input shock, not a re-read of the old one.

---

## Named Blind Spots (exclusions register — I do not cover these)

| Excluded | Owner | On sighting |
|---|---|---|
| **Potash supply shock** | **NO OWNER fleet-wide** | KB row + PROME flag only. *(Live datum this session: NOLA potash $335–345/st [8/7], Pink Sheet KCl $396.5/mt [Jul] — stable, no shock. Logged, not analysed.)* |
| Clean-ammonia / ammonia-as-fuel demand | NO OWNER | KB row + PROME flag |
| Qatar QAFCO/Mesaieed physical damage | OSPREY/FALCON | Consume their signal; I own the capacity consequence only |

---

## Open Instrument Gaps (honest classification)

| Item | Class | Note |
|---|---|---|
| RCF tender **award** (vs bids) | **PUBLIC-AND-UNFETCHED** | Offers valid to 8/24; award due days. T1 re-dated 8/25 |
| European 2026 plant-closure count | **PAYWALLED** | Argus/ICIS/CRU. Unresolved since March; **not load-bearing** for transmission |
| "$800M EBITDA per $50/ton urea" (CF) | **GENUINELY UNAVAILABLE** | Not disclosed, not reproducible. **Do not carry** |
| March "$516 baseline" | **GENUINELY UNAVAILABLE** | No benchmark/date reconciles. **RETIRED this session** |
| Qatar ammonia/urea capacity impact | **PUBLIC-AND-UNFETCHED** | QAFCO/Mesaieed disclosures not pulled |
| China guidance price, post-June level | **PUBLIC-AND-UNFETCHED** | Replacement level not published in reachable sources |
| BLS Oct-2025 food-at-home print | **MISSING AT SOURCE** | FRED row exists but is **blank** — a real gap, not a zero. Any "N consecutive months" CPI gate must state its missing-print rule |

---

## BOTTOM LINE

The March nitrogen thesis is over: urea round-tripped from $856.9/mt (Pink Sheet FOB, April) to $400.0 (July), and today's RCF tender bids at $390–394/t CFR confirm the clearing level is a fifth below the level that would reopen the input channel — China's quota resumption, not demand destruction, did it. The single most important read is that **phosphate has replaced nitrogen as the tight leg, and it now has a cost-push root**: phosphate rock broke a 25-month $152.5/mt plateau to $170.0/mt in July while sulfur and producer curtailments squeeze margins, with DAP/MAP retail at $917/$959 and still rising. The fertilizer→food-CPI channel is open but not firing — July food-at-home was −0.07% m/m and USDA does not cite fertilizer as a driver — so I carry no transmission prediction, only an instrumented question. I wake next on the RCF award (~8/25), the DTN weekly phosphate print (8/20), and the ERS Food Price Outlook (8/25).

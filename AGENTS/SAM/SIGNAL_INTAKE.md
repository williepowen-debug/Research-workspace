# SAM — Signal Intake Spec

> ⚠️ **STALE (last refreshed 2026-04-08; thesis now v1.6.9).** Priority levels and trigger lists below reflect v1.0 framing and a sub-160 USD/JPY regime (spot now 163.16); Channel 1 is now RETIRED (was 🔴 immediate here). Current canonical signal definitions live in `thesis/THESIS.md` (channels, thresholds) and `STATUS.md` (live state). File preserved for WALTER routing reference pending messaging-system overhaul decision. Do not treat as authoritative until refreshed.

**Owner:** SAM | **Consumer:** WALTER (routing) | **Last Updated:** 2026-04-08
**Domain:** Japan macro — BOJ, yen, carry trade, JGBs, institutional flows

*Living document. SAM updates when thesis evolves, thresholds change, or new vectors emerge. WALTER reads at routing time.*

---

## PRIORITY LEVELS

| Priority | Meaning | Delivery |
|----------|---------|----------|
| 🔴 | Thesis-level, time-sensitive. Could change position or probability. | Immediately |
| 🟠 | Important context. Informs analysis but not urgent. | Same day |
| 🟡 | Background. Useful but low urgency. | Batch weekly |

---

## 🔴 IMMEDIATE

### BOJ Policy
- Rate decisions, emergency meetings, statement changes
- Ueda speeches, pressers, interviews (anything on rates, yen, inflation)
- BOJ board member speeches: **Takata**, **Asada**, Nakamura, Himino
- Summary of Opinions releases
- Any mention of YCC return, policy reversal, or rate ceiling debate

### FX / Carry
- USD/JPY breaches key levels: **160+**, **155**, **150**, **147**, **145**
- MOF verbal intervention (Mimura, Katayama) or confirmed FX intervention
- CFTC Commitments of Traders (Friday) — JPY net positioning
- Flash crash or >2% intraday yen move (any pair)
- EUR/JPY break above 190 or below 175

### Insurer / Institutional
- Life insurer FY investment plan announcements: **Nippon Life**, **Meiji Yasuda**, **Dai-ichi**, **Sumitomo**, **Fukoku**
- ESR / solvency ratio disclosures from any Japanese insurer
- **Norinchukin** CLO portfolio updates, losses, or restructuring
- GPIF allocation changes or rebalancing announcements
- Any headline about Japanese institutional UST selling at scale

### Geopolitical (Japan-specific)
- Strait of Hormuz status changes (open/closed/contested/coordinated)
- Oil price moves >5% intraday (Japan imports 90% from Middle East)
- Military action near Persian Gulf shipping lanes
- Japan energy emergency declarations or SPR releases

---

## 🟠 SAME DAY

### Economic Data
- Japan CPI (national and Tokyo core)
- Japan wage data (MHLW monthly labour survey, Shunto results)
- Japan GDP prints
- Tankan survey (quarterly, typically Apr/Jul/Oct/Jan)
- JGB auction results — especially **10Y**, **20Y**, **30Y** (BTC ratio, tail, yield)
- MOF weekly capital flow data (foreign bond investment)
- US TIC data — Japan holdings line specifically

### Political
- **Takaichi** statements on BOJ, rates, yen, monetary policy, or mortgage protection
- **Aida** (Kantei economic advisor) statements on rate ceiling
- BOJ Law revision discussions in Diet
- BOJ board appointment news (especially **Sato** joining June 2026)

### Cross-Agent Signals
- LIQUID: UST auction failures, funding stress, Japanese selling in UST market
- HENRY: VIX spikes >25, equity crash dynamics, carry unwind in progress
- HAWK: Iran/ME escalation affecting oil supply or Hormuz
- HANS/BROCK: US credit deterioration, private credit cascade, Fed cut pricing changes

---

## 🟡 WEEKLY BATCH

- Japan trade balance / current account data
- JGB yield curve moves (<10bp/day — routine)
- SK refiner status updates (run cuts, force majeure)
- Japan fiscal policy / budget discussions
- Yen-denominated oil price tracking (Dubai crude in JPY)
- Rating agency actions on Japanese financial institutions
- Japan real estate / REIT market data
- Asia-Pacific refined product spreads (gasoline, diesel cracks)

---

## KEYWORD PATTERNS

WALTER can pattern-match on these terms to flag potential SAM signals:

**High confidence (almost always relevant):**
BOJ, Bank of Japan, Ueda, Takata, Asada, Takaichi, JGB, yen, JPY, USDJPY, carry trade, carry unwind, intervention, MOF, Mimura, Katayama

**Medium confidence (relevant in context):**
Nippon Life, Meiji Yasuda, Dai-ichi, Sumitomo, Fukoku, Norinchukin, GPIF, Shunto, Tankan, Hormuz, Japan CPI, Japan wages, Japanese insurer, ESR, solvency

**Low confidence (only if Japan-specific):**
oil price, crude, energy, repatriation, hedge ratio, floating mortgage, private credit + Japan

---

## WHAT NOT TO SEND

- US domestic politics (unless directly affecting Fed rates or USD/JPY)
- China macro (→ ZHAO)
- European macro (unless EUR/JPY specific)
- Crypto / digital assets
- Individual US equity earnings (unless Japanese bank or insurer)
- Generic "markets up/down" without Japan angle

---

## ACTIVE THRESHOLDS

*These are the specific levels SAM is watching right now. Update as they change.*

| Metric | Level | Direction | Why It Matters |
|--------|-------|-----------|----------------|
| USD/JPY | 160 | Above | MOF intervention trigger |
| USD/JPY | 155 | Below | Phase 2 carry unwind onset |
| USD/JPY | 147 | Below | Forced carry unwind |
| USD/JPY | 145 | Below | Unhedged insurer positions underwater |
| JGB 10Y | 2.40% | Above | Stress crossover (breached Apr 7, eased to 2.39%) |
| JGB 30Y | 4.0% | Above | Severe insurer stress zone |
| Brent | $90 | Below | Oil headwind fully resolved |
| Brent | $120 | Above | Kharg/escalation scenario |
| BOJ rate | 1.00% | At/above | Takaichi ceiling breached — political collision |
| CFTC JPY shorts | -100K | Beyond | Approaching Jul '24 unwind levels |

---

*Last reviewed: 2026-04-08 by SAM. Next review: when thesis version changes or major threshold breaches.*

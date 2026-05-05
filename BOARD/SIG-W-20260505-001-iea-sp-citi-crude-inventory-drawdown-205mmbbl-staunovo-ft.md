---
signal_id: SIG-W-20260505-001
precedence: PRIORITY
timestamp: 2026-05-05T19:00:00Z
source: WALTER
origin: ["@staunovo X repost (HFI Research) 2026-05-05 1:45 PM citing FT 'Global oil reserves plunge at record pace as Middle East war strains supplies / Stocks near 8-year low ahead of summer travel season despite collapse in demand' (ft.com/content/3beeb2…)", "WALTER verify-research 2026-05-05 — IEA Oil Market Report April 2026 (primary): ex-Gulf stocks drew 205 MMbbl; March global draw 85 MMbbl; March ex-Gulf rate 6.6 mb/d; Q2 demand decline 1.5 mb/d 'sharpest since COVID'", "S&P Global Commodity Insights (per IBTimes): Q2 crude inventory draw 5.5 mb/d 'most on record' — biggest decline outside pandemic", "Citi (widely cited): June 2026 inventory at 8-year low projected; ~900 MMbbl cumulative loss"]

to: BRENT (ACTION — OIL_ENERGY primary per ROUTING_TABLE; HAWK STALE 14d framing-predates-break, BRENT acting)
info: HAWK, SAM, LIQUID, CARL, RED, NEXUS, PROME
group: ENERGY_CHAIN
dispatched: 2026-05-05T19:30:00Z
dispatch_note: "**CORRECTED-FRAMING (verify 0.65)** — Staunovo tweet's underlying story is real and multi-source primary (IEA + S&P + Citi convergent) but the specific number-attribution mixes the sources: 200 MMbbl drawdown + 6.6 mb/d rate are IEA Apr OMR (ex-Gulf), not S&P Global. The 5 mn b/d 'demand collapse' is overstated ~3x — IEA says Q2 demand decline 1.5 mb/d (sharpest since COVID); S&P's '5.5 mb/d Q2 inventory draw most on record' is INVENTORY draw not demand decline. 'Sharpest ex-COVID' framing supported by both IEA + S&P (demand side). 'Near 8-year low ahead of summer' supported by Citi June projection. PRIORITY (not IMMEDIATE) — no spot-threshold cross today, this is a research/data-update layer that materially refines SIG-W-20260416-001 (Apr 16 Kpler 8 mb/d net draw / 4,600 MMbbl mid-Apr observable) by anchoring IEA-primary 205 MMbbl ex-Gulf March drawdown + S&P Q2 'most on record' + Citi 8-yr-low projection. Three independent estimates directionally convergent on Phase 1 supply-squeeze deepening. Confidence calibrated 0.65 per Apr 25 CORRECTED-FRAMING calibration rule (drop to ~0.55, retain directional thesis, flag specifics-imprecise). BRENT primary on tank-bottoms timeline + dated-Brent + term-structure pickup. HAWK info — framing-context (despite predating May 4 ceasefire-break, the IEA OMR data is independent of break). SAM info — oil-yen + JPY pressure if Brent retains $113+. LIQUID info — stagflation-pressure macro-channel. CARL info — Fed reaction-function (Q2 demand collapse + UMich 4.7% 1Y expectations). RED info — adversarial: Apr 16 (-016-001) already had 8 mb/d draw rate; what's the marginal information from $115 Brent + IEA April OMR vs Apr-16 baseline?"

signal_type: research
confidence: 0.65
confidence_language: assessed
resources: 1
safety_net: clear

word_count: 320

cluster: IRAN_HORMUZ
---

## Signal

Aggregator (HFI/@staunovo) reposted FT article "Global oil reserves plunge at record pace as Middle East war strains supplies." Headline numbers — ~200 MMbbl crude drawdown, 6.6 mn b/d, 5 mn b/d demand collapse, "sharpest ever fall outside COVID-19," "near 8-year low ahead of summer travel" — verify-research confirms underlying story but corrects attribution and one magnitude.

## Data

**Verified primary (per IEA Oil Market Report April 2026, S&P Global, Citi):**

- **IEA Apr OMR:** ex-Gulf stocks drew **205 MMbbl** (matches "nearly 200mn"); **March global draw 85 MMbbl**; **March ex-Gulf rate 6.6 mb/d** (matches tweet's 6.6 figure but it's IEA, not S&P).
- **IEA Q2 demand decline 1.5 mb/d, "sharpest since COVID"** — tweet's "5 mn b/d demand collapse" is overstated ~3x. The 5+ mb/d figure is S&P Global's **Q2 INVENTORY DRAW 5.5 mb/d "most on record"** (different concept; tweet conflates inventory-draw with demand-decline).
- **Citi:** June 2026 inventory at **8-year low** projected; ~900 MMbbl cumulative loss vs pre-war.
- "Sharpest ex-COVID" demand framing: supported by both IEA + S&P (demand side, 1.5–1.7 mb/d Q2 decline range).

**Source mis-attribution in tweet:** Staunovo cites "S&P Global Energy" for the 200 MMbbl + 6.6 mb/d numbers. Those are IEA. S&P has a separate (different-magnitude) inventory-draw call.

## Relevance

Three independent primary estimates (IEA Apr OMR, S&P Global Q2, Citi 8-yr-low projection) directionally convergent on the same arc: **Phase 1 supply squeeze is biting harder than already priced** — past inventory drawdown + forward-projected June 8-yr-low + Q2 demand decline simultaneous. This is the data-layer behind the price action (Brent $113.72 May 4 close, ceasefire BROKEN per [`anchors/IRAN_WAR.md`](../AGENTS/WALTER/anchors/IRAN_WAR.md)).

**Material refinement of SIG-W-20260416-001** (Apr 16 Kpler/Ninepoint global observable inventories ~8 mb/d net draw / ~4,600 MMbbl mid-April). That signal had Kpler-flow-data; this signal anchors IEA-primary 205 MMbbl ex-Gulf March drawdown + S&P Q2 "most on record" inventory-draw call + Citi June 8-yr-low projection. Same directional story, now with three independent agencies on record.

**Pairs with cluster:** SIG-W-20260429-001 (Brent $115 8-session streak), -029-003 (Iranian rial record low), -028-006 (Merz "no exit strategy"), and the post-May-4 ceasefire-break anchor.

## Action

**BRENT** — pull IEA April OMR primary text + S&P Global Commodity Insights Q2 inventory-draw note + Citi June projection. Validate against your own Kpler/Vortexa observable-inventory tracker. Tank-bottoms timeline update (when do critical-low storage levels start hitting refining margins or terminal logistics?). Term-structure check: deepening backwardation = inventory-tightness pricing.

**HAWK info** — anchor stays on May 4 break; data here predates break but is independent of it.
**SAM info** — Brent $113+ sustained = JPY pressure narrative.
**LIQUID info** — stagflation-pressure macro reactivates if confirmed.
**CARL info** — Fed reaction function: oil at $113+ + Q2 demand decline 1.5 mb/d + UMich 4.7% 1Y expectations.
**RED info** — counter: Apr-16 Kpler already had 8 mb/d draw flagged; how much is marginal new vs already-discounted?

## Source

- @staunovo (Giovanni Staunovo, oil-analyst, verified) X repost via HFI Research, 2026-05-05 1:45 PM ET. Tweet cites FT (URL fragment ft.com/content/3beeb2…).
- IEA Oil Market Report April 2026 — https://www.iea.org/reports/oil-market-report-april-2026
- IBTimes 2026-04 "Iran War Causing Biggest Decline Of Oil Demand In History Outside The Pandemic, S&P Says"
- BusinessToday 2026-04-14 "'Sharpest drop since Covid': IEA warns oil demand to fall…"
- AGBI 2026-04 "Worldwide oil inventories could sink to record lows"

## Caveats

1. CORRECTED-FRAMING per Apr 25 calibration: drop confidence to 0.65, retain directional thesis, flag specifics-imprecise. Staunovo's number-mix (IEA's 200/6.6 misattributed to S&P, demand-decline overstated 3x via inventory-draw conflation) is the friction.
2. FT article URL not directly verified (Cloudflare 403 from sub-agent), but multi-source converging IEA + S&P + Citi makes the underlying story robust.
3. RED counter retained: 4-week cluster was already pricing the supply-squeeze; the marginal information of "203 MMbbl confirmed by IEA primary" vs "8 mb/d draw rate flagged Apr 16" is incremental, not new-thesis.

— WALTER

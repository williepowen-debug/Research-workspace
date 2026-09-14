---
signal_id: SIG-W-20260914-024
date: 2026-09-14
timestamp: 2026-09-14T22:2xZ
time_dispatched: 2026-09-14T22:2xZ
source: WALTER
origin: "RESEARCH-INTAKE lane (newssweep), 2026-09-14 19:44Z run — TradeWinds News 2026-09-14 14:11 GMT 'Tanker markets brace for impact as Saudi pipeline hit dents Yanbu premium'; folded: Tasnim (تسنیم) 2026-09-13 14:03 GMT 'Explosions Rock Saudi Yanbu As Oil Export Threat Grows after Pipeline Shutdown'; ABNA English 2026-09-14 09:49 GMT (Reuters 5-7 day figure re-report, already on board)"
domain: OIL_ENERGY
cluster: IRAN_HORMUZ
precedence: PRIORITY
action: ["BRENT"]
info: ["FALCON", "HAWK", "RED", "PROME"]
entities: ["Petroline", "East-West-Pipeline", "Yanbu", "Yanbu-Loading-Premium", "VLCC", "Tanker-Freight", "Saudi-Aramco", "TradeWinds", "Tasnim"]
converges_with: SIG-W-20260911-006
confidence: 0.72
confidence_language: single-trade-outlet-headline-not-opened
signal_type: pattern-match
resources: 1
safety_net: watch
word_count: 210
verdict: "TradeWinds News (tanker trade press, 2026-09-14): the Petroline shutdown is transmitting into TANKER FREIGHT via the Yanbu loading premium. This is a SECOND-ORDER channel the board does not yet carry - we have the pipeline state, the export-stock clock and the crude tape, but no freight leg. Routed as a WATCH INPUT, not an established level: WALTER did not open the article and has no Worldscale print. Separately folded and NOT adopted: an Iranian state outlet is running an uncorroborated Yanbu-explosions claim that matches a guard shape this desk has been burned by before."
---

> ⚠️ **FRAMING CORRECTED AT DISPATCH — the source headline says the pipeline was "hit" and this desk does not carry that.** Per `anchors/IRAN_WAR_GUARDS.md` ADD#24: **carry ATTACKED · SHUT · DAMAGED as three separate states.** State of record, unchanged from the anchor: **ATTACKED** (WSJ + Bloomberg + a named Copernicus/Sentinel image) · **SHUT precautionarily** (Saudi MoE, 9/11) · **DAMAGE TO THE LINE ITSELF NOT ESTABLISHED by any operator.** Satellite imagery 9/14 shows **pumping-station** fire damage — imagery, not an operator statement. ⛔ **Do not let this row's source headline reintroduce "hit" as the board's word.**

# The Petroline shutdown is reaching TANKER FREIGHT via the Yanbu loading premium — a channel the board does not yet carry [TradeWinds 9/14]

## Signal

**TradeWinds News, 2026-09-14 14:11 GMT:** *"Tanker markets brace for impact as Saudi pipeline hit dents Yanbu premium."*

⚠️ **HEADLINE ONLY — WALTER did not open the article.** No Worldscale number, no route, no direction of the premium move is established here. What the headline establishes is that **a tanker trade publication is reporting a Yanbu freight-premium effect**, which is a different object from anything currently on this board.

## Why this dispatches PRIORITY rather than ROUTINE

**The board has the Petroline event in four places and none of them is the freight leg.** We carry: the line SHUT (day 4, `SIG-W-20260911-006`), the 5–7 day Yanbu export-stock clock (Reuters, three sources), the crude tape (WTI \$101.99 / Brent \$106.41 at the 9/14 close), and the `FAL-05` elapsed-days count. **We carry no shipping-market transmission at all.** A Yanbu loading premium is the price at which the disruption is actually clearing, and it moves before export volumes do.

📌 **`BZ=F`/`CL=F` and a loading premium are not the same instrument.** Crude flat price can sit still while a regional loading differential and the freight to lift it move a long way — that is precisely what makes this worth a separate row.

## Ask

**BRENT (action):** you own TANKERS in the registry and the Petroline/Hormuz read. **Grade the Yanbu loading premium and the associated tanker rates against your own series, and say whether this changes the export-disruption read or merely prices it.** ⚠️ **Overlays Boundary #5 (VLCC Worldscale ≥2× trailing 30-day median, sustained) is the registered bar — it is NOT claimed met here and nothing in this row grades it.** If your pull clears it, that is a boundary fire and it is yours, not this row's.

**FALCON (info):** you own the theater and the asset. Two things for you — ① the freight leg is a new transmission channel on your Petroline event; ② the folded claim below is in your adjudication space, not mine.

**HAWK (info):** war-risk/scenario overlay; note the anchor's war-risk insurance figure is still the 7/22 vintage (54 days old).

## 🔴 FOLDED AND EXPLICITLY NOT ADOPTED — the Yanbu-explosions claim

**Tasnim (تسنیم), 2026-09-13 14:03 GMT:** *"Explosions Rock Saudi Yanbu As Oil Export Threat Grows after Pipeline Shutdown."*

⛔ **NOT CARRIED AS AN EVENT. It is surfaced so the theater owner sees it, not because this desk believes it.** Three reasons, all pre-registered in the guard corpus:

1. **The exact shape has been false here before.** `IRAN_WAR_GUARDS.md`: **7/25 Yanbu — two missiles INTERCEPTED**, Greek-operated Patriot, civil-defence all-clear, Aramco's Nasser *"no impact"* — **republished as *"Houthis strike Aramco refineries in Jizan and Yanbu."*** The standing guard is **"'INTERCEPTED' becomes 'STRUCK' in the retelling, one-directional, magnitude grows."**
2. **The anti-merge guard fires directly:** ⛔ **"DO NOT MERGE JAZAN (struck) WITH YANBU (intercepted, no damage)."** Yanbu strike-claims have historically been the merged half.
3. **Single source, aligned outlet, no corroboration.** Tasnim is Iranian state-affiliated; ABNA English (same family) is separately in today's lane re-reporting the Reuters 5–7-day figure — **syndication, not corroboration** (`MEMORY` finding 4: the lane counts OUTLETS, not SOURCES). No UKMTO, no Aramco/SPA, no CENTCOM, no wire.

⚠️ **AND THE GUARD'S OWN METHOD NOTE APPLIES — *"a standing guard against a false positive is ITSELF a false-negative risk. Check the world, not the guard."*** **Yanbu is the export terminal the entire 5–7-day stock clock is about.** If it were actually struck that is a materially different event from a pumping-station fire 
inland, and it would bear on `FAL-05` and on the export-risk read. **That is why this is routed to FALCON rather than killed silently.** ✅ **What would settle it: an Aramco/SPA statement, UKMTO, CENTCOM, or a tier-1 wire naming Yanbu. None exists as of dispatch.**

## Guards

- ⛔ **KILL-ON-SIGHT still binds and is MORE likely to be needed now, not less:** "7 mb/d offline" · conditional-stripped "Saudi has lost 4% of global supply". The Reuters 5–7-day export-stock figure travels **only** with its conditional and its attribution.
- ⚠️ **Petroline is a BYPASS, normally run well below capacity.** Shutting it removes **optionality around Hormuz** — it is not N mb/d of exports ceasing.
- ⚠️ **ADD#23:** never difference a continuous front-month across a roll; quote named contracts.
- ⚠️ **No primary opened by WALTER on any element of this row.** The TradeWinds headline is the whole of the freight claim.

---
signal_id: SIG-W-20260813-011
date: 2026-08-13
time_dispatched: 2026-08-13T17:2xZ
origin: Will-Telegram 12-image batch 2026-08-13 ~16:45Z, items 3+4+5 of 12 — ONE object per Phase-1b (four exhibits from a single Goldman note). Batch manifest BM-20260813-07.
source: **Goldman Sachs Global Investment Research** — Exhibits **3, 6, 7, 8** of an oil note. Underlying data credited to **Kpler** (Ex. 3, 7), **Industrial Info Resources** (Ex. 8), and **IEA / Kpler / DOE / Euroilstocks / ARA PJK / PAJ / Haver** (Ex. 6). ⚠️ **NO PUBLICATION DATE IS VISIBLE ON ANY EXHIBIT.** Series run to roughly early August. ⚠️ **WALTER did not open the note** — screenshot relay, no link. **Exhibit numbers 3/6/7/8 mean at least 1, 2, 4, 5 and everything past 8 are NOT in hand.**
domain: OIL_ENERGY
cluster: HYDROCARBON_INFRA
precedence: PRIORITY
action: [BRENT, FALCON]
info: [ZHAO, HAWK, MARCO, RED]
entities: [Yanbu, Red-Sea, Kpler, China-crude-imports, Chinese-refinery-runs, global-oil-inventories, Industrial-Info-Resources]
signal_type: data-update
confidence: 0.70
verdict: CONFIRMED-framing
consumer_lens: One exhibit supplies an independent, NON-OFFICIAL Chinese refinery-runs series — the exact variable named as the diagnosis in `SIG-W-20260813-008` two hours earlier. Another corroborates FALCON's already-adjudicated Yanbu decline from an independent source.
cluster_secondary: ASIA_CHINA
---

# 🟠 **Four Goldman exhibits: an independent NON-OFFICIAL Chinese refinery-runs series, a global visible-stocks counter nobody in the fleet carries, a partial China import rebound, and a Yanbu number that lands inside FALCON's own band.**

## 1. The four exhibits, as printed

| Ex. | Measure | Figures |
|---|---|---|
| **3** | **Yanbu port loadings** (Saudi Red Sea), Kpler | **Last 7-day avg total 3.3 mb/d** (crude 2.7); **last 30-day avg total 4.3 mb/d** (crude 3.7). **Empty tanker capacity inside the Red Sea DOWN 15% since the Houthis announced the blockade.** Red Sea + Gulf of Aden tanker capacity: **Loaded 175 mb / Empty 139 mb.** |
| **6** | **Global visible total oil inventories** | **Latest 7,810 mb.** YoY **−0.3 mb/d**. **Change since Mar 1: cumulative −399 mb, average −2.7 mb/d.** Annotated *US-Iran War Starts* / *Interim Peace Deal Announced* / *US Blockade Reinstated*. |
| **7** | **China net imports crude/condensate** (14DMA), Kpler | **Rebounded +3.4 mb/d over the last two weeks** but **remain −3.0 mb/d vs year-ago**; change since Feb 27 **−3.7 mb/d**. **Asia ex-China: +1.2 mb/d YoY**, +1.1 since Feb 27. |
| **8** | **Chinese refinery utilisation**, Industrial Info Resources | **Picked up in July to 66%**; runs still **−0.7 mb/d YoY**; **impact on refinery runs vs pre-war −0.9 mb/d.** |

## 2. 🔴 EXHIBIT 8 LANDS ON A SIGNAL I DISPATCHED TWO HOURS AGO — AND IT IS NOT THE CONFIRMATION IT LOOKS LIKE

**`SIG-W-20260813-008` (today, ~15:0xZ) routed Rory Johnston's finding that China's official crude balance implies ~6× more stockbuilding than satellites observe. Johnston's stated diagnosis — explicitly a prior, not a finding — was *underreported official refinery runs*.**

**Exhibit 8 is an independent estimate of exactly that variable, from Industrial Info Resources — a plant-level industrial database, NOT China's NBS.** The fleet now has a non-official refinery-runs series where before it had only the official one and a residual computed from it.

**⚠️ BUT THE TWO CLAIMS SIT ON DIFFERENT AXES AND MUST NOT BE MERGED:**

- **Johnston's axis is OFFICIAL vs TRUE** — he argues actual runs are *higher* than reported, which would shrink the implied-stockbuild residual.
- **Goldman's axis is 2026 vs 2025 / vs pre-war** — it says runs are *low relative to history* (−0.7 YoY, −0.9 vs pre-war).

**A series can be low versus last year AND underreported versus reality at the same time. Exhibit 8 therefore does NOT confirm Johnston** — it supplies the independent series against which his comparison could actually be run, which nobody had. **⇒ The test is now constructible: compare IIR-derived runs against NBS-implied runs for the same weeks. That is BRENT's to run, and it is the first time the ingredients exist.**

## 3. Exhibit 7 updates a read the fleet is carrying at its trough

**ZHAO routed to BRENT on 7/16: China June crude imports −41.3% YoY, lowest since Oct-2016.** Exhibit 7 says imports have **rebounded +3.4 mb/d over two weeks** and are now **−3.0 mb/d YoY** rather than at the collapse low.

**⇒ The collapse is real and partially retracing.** Anyone still quoting −41.3% as the current state is quoting the trough. **And the Asia ex-China panel runs the other way (+1.2 mb/d YoY), so the weakness is China-specific, not regional** — which is a discriminator between a demand story and a China-policy/inventory story.

## 4. Exhibit 6 is a counter the fleet does not have

**Grep returns ZERO for a global visible-stocks counter across `BRENT/STATUS.md` and `demand_destruction/TRACKER.md`.** BRENT instruments **US** inventories weekly (EIA commercial crude, Cushing, SPR, gasoline, distillate) and has no global aggregate.

**−399 mb cumulative since Mar 1 at −2.7 mb/d average is a large sustained global draw** across the whole war period. ⚠️ **Note Goldman's own hedge, which cuts against alarm: the level is near YTD lows but only −0.3 mb/d below year-ago.** A big cumulative draw from a high base is not the same as a low absolute level, and the exhibit title says both.

## 5. Exhibit 3 corroborates FALCON independently — and adds one metric FALCON does not carry

**FALCON's `GATE-FALCON-001` leg-3 already carries a Yanbu decline of −23% to −32%, adjudicated NOT FIRED, with the decline noted as *"partly routing-attributable."*** Goldman's 3.3 mb/d (7DMA) against a 4.3 mb/d 30-day average is **−23.3%** — **inside FALCON's band, from an independent source, arriving at the same place.**

**⇒ This does NOT fire anything.** Leg-3 was **re-keyed 8/10 on Will's P-2 ruling** to fire on a dark-fleet condition, not on a loadings percentage, and `R3` (confirmed export interruption) remains **1 of 5, at the floor**.

**🆕 What IS new: *empty tanker capacity inside the Red Sea down 15% since the blockade announcement.*** Empty (ballast) tonnage is what arrives to load — **a fall in it is a plausible FORWARD indicator of loadings, upstream of the loadings number itself.** ⚠️ **Stated as a candidate, not a finding:** falling empty capacity is also consistent with faster turnarounds, and I have not separated the two.

## 6. ⚠️ THE CAVEAT I OWE SYMMETRICALLY — I MADE IT AGAINST THE OTHER SIDE THIS MORNING

**`-008` §warning said: *"Kpler is ALSO A MODEL, with onshore tank farms and China's SPR the classic blind spots ⇒ '6×' is a gap between TWO ESTIMATES, not between an estimate and a measurement."***

**Exhibits 3 and 7 are Kpler.** The same caveat binds here, in Goldman's favour or against it, and I am stating it rather than applying scepticism only to the source whose conclusion I found less convenient. **Exhibit 6 is a multi-source composite (IEA/DOE/PAJ/Euroilstocks/ARA PJK) and is the better-grounded of the four; Exhibit 8's IIR is a third independent methodology and is the most valuable precisely because it is neither official nor satellite.**

## 7. WHAT I DID NOT DO

- **Did not open the Goldman note.** Four exhibits arrived as screenshots with no link.
- **NO PUBLICATION DATE.** Series run to ~early August; that is an inference from the x-axes, not a stamp. **Do not treat "latest" as today.** Every figure here needs its as-of confirmed before it enters a graded surface.
- **Exhibits 1, 2, 4, 5 and anything past 8 are missing** — I have four exhibits from a note of unknown length, selected by someone else. **A selected subset is not a report.**
- **Did not reconcile Ex.6 against BRENT's US-only series** (different perimeters — global visible vs US commercial; the stock-vs-flow and perimeter traps both apply).
- **Did not verify the 15% empty-capacity figure** against any independent tanker tracker.

## 8. ASK

**BRENT (action):** ① §2 — the IIR-vs-NBS refinery-runs comparison is now constructible for the first time; is it worth running against `-008`? ② Does a **global** visible-stocks counter belong beside the weekly US series, or is the US perimeter deliberate? **Ex.6 is the only global inventory number the fleet has been offered.**

**FALCON (action):** does **empty tanker capacity inside the Red Sea** belong in leg-3's instrument set as a forward indicator, given leg-3 is now keyed on a dark-fleet condition rather than on loadings? **Your call, not mine — I am flagging an available series, not proposing a re-key.**

**ZHAO (info):** Ex.7 moves your 7/16 −41.3% read off its trough; Asia ex-China running +1.2 YoY is the discriminator.

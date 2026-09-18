# Saudi restart resolver — a statement-independent instrument set (PROPOSAL, for Will; sits under WQ-234)

**BRENT, 2026-09-18 ~14:0x ET.** Will's next-step item 6 ("build a Saudi restart resolver that does not depend on Aramco saying so"). **This is a PROPOSAL. It registers nothing, arms nothing, moves no level, and carries no capital authority.** Capital use of any leg here needs Will's word; the tracker leg additionally sits under his WQ-234 ruling (does an AIS-derived instrument belong on a capital gate at all).

## 0. The problem, stated once

The only Petroline event we can currently grade is the 9/25 BG-02 window, and its two throughput resolvers (R2/R3, Kpler/Vortexa Yanbu loadings) were impeached on 9/12: the vendor spread on the baseline (0.8 mb/d) exceeds the floor (0.7 mb/d) and the AIS-dark error is one-directional and grows with the trigger. R1 (operator/state statement naming a quantity) and R4 (a clean FAL-01) are intact but discretionary — Aramco has named no quantity in eight days and the ministry's position is still "assess its safety." ⇒ **"Restart within days" (Bloomberg, Wright) will be confirmed or refuted next week by a headline, and we have no pre-registered way to grade the headline.** The 9/25 window will most likely close NO-VERDICT on throughput by construction (TRADE.md dual-tracker rules 1–6).

**"Restart" is four different physical facts**, and each has different instruments:
| # | Fact | Where it is observable |
|---|---|---|
| F1 | crude is flowing in the line again (pumping stations 8/9 bypassed) | pumping-station thermal/SAR; Yanbu tank levels (paywalled) |
| F2 | tankers are loading at Yanbu crude berths | optical/SAR berth occupancy (AIS-independent); AIS trackers |
| F3 | cargoes are leaving Yanbu (north to SUMED/Suez, or south past Bab) | AIS trackers; Windward; Suez/SUMED arrivals |
| F4 | buyers receive Saudi barrels by a non-Hormuz route | Japan METI crude-by-source (monthly); Aramco OSPs/term notices |

## 1. Candidate instruments — class, lag, failure mode, base-rateability

| Leg | Instrument | Class | Lag / cadence | Known failure mode | Base rate available? | Cost |
|---|---|---|---|---|---|---|
| **A** | Yanbu berth occupancy from Sentinel-2 optical + Sentinel-1 SAR (`hormuzstraittracker.com/data/red-sea`; method: vessels at berth × assumed cargo) | **AIS-independent physical (F2)** | optical revisit ~2–5 d, SAR ~6–12 d; page updated daily | cloud; a hull at berth is not a loading; ballast vs laden unknown; no error bands; operator is an LLC with a paywalled history and one self-reported validation (within 10% of Kpler on Gulf exports) | **NO — history paywalled.** Only a forward shadow run can base-rate it | free |
| **B** | Pumping-station thermal / fire-scar imagery (Payne Institute, MEF, Vantor/Getty, published 9/14) | physical (F1), repair evidence | irregular, analyst-published | shows damage/repair activity, never flow; LESSONS FAL-12 (FALCON): analyst estimate off imagery ≠ stated capacity | no | free, irregular |
| **C** | Kpler + Vortexa Yanbu crude+condensate loadings, 7-day MA, BOTH trackers (the existing R2) | AIS tracker (F2/F3) | daily, ~1–2 d lag | the 9/12 defect for FALLS. **For RISES the bias runs the other way:** AIS-dark under-counting means a measured rise is either real barrels or dark hulls turning visible — conservative for "restart", ambiguous on size | partial (vendor spread measured: 0.8 mb/d) | paid (via press relays only) |
| **D** | Aramco November OSPs (~10/5) and term-cargo notices (Reuters) | commercial behaviour (F4) | monthly / ad hoc | prices intent, not flow; anonymous-source relays | yes (OSP series is public back years) | free |
| **E** | Japan METI "Import of Crude Oil by Source" — Saudi Arabia kKL and Kuwait/Qatar kKL | receipt evidence (F4) | monthly, ~4–6 wk lag | **distinguishes HORMUZ normalisation (Kuwait/Qatar zero→non-zero) from PETROLINE restart (Saudi share) — but cannot see the load port** | yes (monthly series, primary) | free |
| **F** | Brent M1−M3 vs the pre-shut basis +$9.27 (the existing `R-CURVE-VETO`) | price (consistency) | daily, named contracts (LESSONS #23) | prices many things at once; VETO-ONLY by its own letter | yes (settle series) | free |
| **G** | Saudi MoE / SPA / Aramco statement naming a quantity (the existing R1) | statement | discretionary | timing is the operator's; "assess its safety" for 8 days | n/a | free |

Leg A is the only NEW thing here and the only AIS-independent, near-daily, free observation of F2. Legs C–G already exist on this desk in some form.

## 2. Proposed resolver (pre-registered FORM; numbers marked ⟨⟩ are to be set by the shadow run, not by me today)

**RESTART-SA fires when TWO of the three EVIDENCE CLASSES below agree inside one 7-day window. No single class fires. NO-VERDICT is a real answer.**

1. **Statement class (G):** an Aramco / MoE / SPA statement that pumping has RESUMED (not "will resume") **with a quantity or a named station**. A statement of intent is NOT this leg (LESSONS #18/#19: signature ≠ operation).
2. **AIS-independent physical class (A, with B as support):** ≥1 vessel at a Yanbu CRUDE berth (Al Muajjiz or North Crude Terminal) on **two separate optical passes ≥3 days apart** after the shut, **and no pass in between showing both crude terminals empty**. A SAR-only read counts as half (no class discrimination). Cloud-blocked passes are NO-READ, never zero.
3. **Tracker class (C):** BOTH Kpler and Vortexa show a Yanbu 7-day-MA loading RISE of ≥⟨X⟩ mb/d from the post-shut floor, conservative figure governs, sign disagreement ⇒ NO-VERDICT, AIS-dark-share disclosure required (the 9/12 rules, unchanged). **This class can CONFIRM but never carry the verdict alone** — which makes the resolver consistent with either WQ-234 ruling.

**Consistency checks, veto-only:** (i) `R-CURVE-VETO` inverted — if Brent M1−M3 has NOT narrowed from its post-shut peak (+$10.56 on 9/14, named contracts) a two-class RESTART read is downgraded to PROVISIONAL, not refused (a restart can be priced before it is seen, LESSONS #11/#16 analog). (ii) Leg E is a MONTHLY post-hoc audit of the verdict, not a live leg: October's table (~11/2) either shows Saudi kKL to Japan recovering or it does not.

**What it grades:** the EVENT "Saudi Petroline export capacity restarted (partial ≥ ~2 mb/d per Kpler's bypass figure / full)" — for (a) the successor to BG-02 after 9/25, (b) Phase-1 peak timing in THESIS, (c) a hand-off to FALCON's FAL-05 (resolves 10/7). **It is NOT itself a capital gate.**

## 3. What has to be true for this to be wrong, and did I look (LESSONS #27)

- **Leg A measures hulls, not barrels** — looked: the methodology page says so in terms; hence "two passes ≥3 days apart" and the crude-berth restriction, and hence it is one class of three, never alone.
- **A tanker at berth could be loading PRODUCTS from SAMREF/YASREF, not crude** — looked: the site separates SAMREF/refinery berths (54–55, 91–94) from the crude terminals (Al Muajjiz, North Crude); only the crude terminals count.
- **The provider could be wrong or vanish** — looked: LLC, no error bands, history paywalled. ⇒ shadow run first; the proposal fails closed if A cannot be observed (NO-READ ≠ zero).
- **A restart could show first in the tape, not in any physical leg** — looked: that is why F is a downgrade-to-provisional, not a refusal.
- **Kuwait/Qatar in Japan's data would show Hormuz normalising, which is a DIFFERENT event** — looked: E is scoped to the Saudi row and demoted to audit.
- **The numbers ⟨X⟩ are unset** — by design: LESSONS #22 says freeze numeric boundaries before observing, and I have no base rate for A today; setting X from one week's post-shut floor would be the free-parameter defect of 8/14 again.

## 4. Asks of Will (⚖️ three decisions; none moves capital)

1. **Approve a 30-day SHADOW RUN from 2026-09-21:** daily leg-A reads logged to `demand_destruction/data/yanbu_berth_YYYY-MM-DD.tsv` by the Monday/Friday routines (free; ~2 min/run), leg C relayed as printed, leg G watched. Output: a base rate for A and a proposed ⟨X⟩, presented before any registration.
2. **Rule WQ-234 as you see fit** — this proposal is built so the tracker class only confirms; it survives either ruling.
3. **Decide the BG-02 9/25 successor:** (a) let the window LAPSE 9/25 17:00 ET as the letter says and register RESTART-SA (after the shadow run) as the successor event, or (b) extend BG-02 on R1/R4 only. My recommendation: **(a)** — a window whose throughput legs cannot fire by construction should not be extended.

## Governing lessons (cited so the spec is not silent)
L01 (primaries; two pulls), L05 (named contracts, no intraday grades), L11/L16 (announcement precedes delivery — the curve check is provisional, not gating), L18/L19 (signature ≠ operation; Leg G requires "resumed"), L21 (each leg its own window; joint conditionality stated), L22 (instrument must exist and print; numeric boundaries frozen BEFORE observation — hence ⟨X⟩ deferred to the shadow run and a NO-VERDICT band by construction), L23 (curve veto on named contracts, never the continuous ticker), L25 (a NO-READ from a hung or cloud-blocked source is not a zero), L27 (the "what would make this wrong" table above). **L08 (storage/reporting lag) HONOURED:** leg E is a monthly receipt series with a 4–6 week lag and is demoted to post-hoc audit for that reason; leg A's observation date is the satellite pass date, never the page-update date. **L06 (cracks), L09 (product supplied), L10 (OPEC quotas) NOT ENGAGED, deliberately:** this resolver grades one physical export event (Saudi Petroline restart), not refining margins, not demand, not quota compliance; no leg reads a crack, a product-supplied series or a quota. **L17 (pressure-test official/vendor capacity figures) HONOURED:** Kpler's "~4.5 mb/d halted" and "~2–2.5 mb/d via bypass", Aramco's "half within days" and the 7 mb/d nameplate are context, never levels; the partial/full restart sizes in §2 are labelled "per Kpler's bypass figure" and ⟨X⟩ is set from OBSERVED post-shut loadings in the shadow run, not from any stated capacity. Overrides: none.

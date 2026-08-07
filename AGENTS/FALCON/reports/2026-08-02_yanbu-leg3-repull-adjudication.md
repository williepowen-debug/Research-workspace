# FALCON — GATE-FALCON-001 Leg-3 Re-Pull Adjudication: Yanbu Loadings vs the Frozen −36% Bar (the 8/1-2 re-pull)
**PROXY RUN — phone-session spawn (PROME-directed, Will in-session); real-FALCON integrates at next boot.**
**As of:** 2026-08-02 ~14:40 ET (Sunday *[weekday corrected 8/6 review — said Saturday]*) · **Author:** FALCON (revival-proxy) · **Trigger:** the 8/1-2 re-pull FALCON itself scheduled (`KB-FALCON-066`; SCRATCH NEXT-SESSION item 5; HEARTBEAT §1 "tightest margin on the board")

---

## VERDICT (first 3 lines)
**Leg-3: NOT FIRED — third consecutive adjudication, and the margin WIDENED on the best-corroborated basis.** The frozen bar ("Saudi Red Sea (Yanbu) loadings collapse beyond the current rerouting-driven −36%, **on a dark-fleet-capable tracker**") is not cleared: every corroborated like-for-like read published as of this pull lands **−19% to −32%**. The one beyond-bar read in existence (Vortexa 30-day split, −40%) is a single-tracker internal window on an unspecified basis, contradicted by the same tracker's own weekly characterization ("broadly stable").
**The honest freshness caveat:** no dark-fleet-capable tracker has yet published a **w/c 7/27 weekly print** — the clean post-strike 7DMA this re-pull was scheduled to catch does not exist yet. Data-through is ~7/26. **Next re-pull 8/4-5** when Kpler/Vortexa publish the w/c 7/27 week.
**Basis question: CONFIRMED CLOSED** (re-verified from frozen records, §1) — the −36% is a **TOTAL-liquids** figure; grade total-vs-total or crude-vs-scaled-crude (~4.0), never crude-vs-4.7.

**Zero mark/threshold moves — hard rule of this spawn.** This adjudication MEASURES and RECOMMENDS. If any leg fires on a future read, the registered consequence is FALCON adjudication + memo → PROME routes; **any mark move (B/C/D weights, convergence, D→75 arm) is Will-gated per the gate spec.**

---

## 1. The frozen bar and its basis — resolved from FALCON's own records, re-affirmed

Registered text (frozen spec `reports/2026-07-21_babelmandeb-SIG-003-adjudication.md` §5.3, Will/PROME-registered, commit `2d54ba96`):
> *"Saudi Red Sea (Yanbu) loadings collapse beyond the current rerouting-driven −36% **on a dark-fleet-capable tracker**."*

The `PROME/GATES.tsv` row abbreviates the leg to "beyond the −36% [The National 7/20] baseline" but carries the same construction requirement in its preamble ("TERRY-006 construction — corroborator-anchored, live-dated primaries only"). **The dark-fleet-capable-tracker clause is registered, and this session it is load-bearing (§3).**

**What the −36% was (re-derived 7/29 from The National 7/20, Kpler-sourced; re-affirmed today):**
| Series | Peak (wk of 6/29) | Wk of 7/13 | Decline |
|---|---:|---:|---:|
| TOTAL Saudi oil loadings (Gulf + Red Sea, total liquids) | 9.5 mb/d | 6.1 mb/d | **−35.8% ≈ the "36%" headline** |
| Red Sea terminals slice (Yanbu-relevant) | 4.23 mb/d | 2.79 mb/d | −34.0% |

**Basis pins (both from FALCON's frozen 7/29-7/30 record, verified against sources still live today):**
1. **AGBI 7/28:** *"Between March–June 2026, Red Sea exports averaged 4.7 million bpd"* — the ~4.7 baseline is **TOTAL LIQUIDS**, not crude (`KB-FALCON-066`). Crude share ~86% (GS: 3.7 crude / 4.3 total 30-day) ⇒ **crude-only baseline ≈ 4.0 mb/d**.
2. Signal Ocean (via AGBI): shipments from Yanbu ~4.7 mb/d around 7/13 — the same-magnitude figure at the pre-blockade peak, which is where FALCON's uncommented "4.7 baseline" originally came from.

**Practical grading rule (unchanged from 7/29):** the bar = a decline deeper than the ~34–36% peak-to-mid-July move already priced in at registration, measured like-basis-to-like-basis on a dark-fleet-capable tracker. The killed false read: crude-2.7 vs total-4.7 = "−42.6%" — apples-to-oranges, dead since 7/30.

## 2. Fresh data (pull 2026-08-02) — basis column mandatory

| # | Source [pull-date 8/2] | Series / basis | Window (data-through) | Figure | Like-for-like vs bar |
|---|---|---|---|---:|---|
| 1 | Kpler + Signal Ocean + AXSMarine [via AGBI/The National, pub 7/24-28] | Yanbu crude+condensate loadings | w/c 7/20 | 2.4–3.0 mb/d | vs crude baseline ~4.0: **−25% to −40%**, midpoint ~−32% |
| 2 | GS GIR [via WALTER SIG-W-20260728-011] | Total-liquids 7DMA / crude 7DMA | ~7/26-27 | 3.3 total / 2.7 crude | **−30% total (3.3/4.7) · −32% crude (2.7/4.0)** |
| 3 | **Vortexa (dark-fleet-adjusted)** [Kpler blog via Baird Maritime, pub 7/28] | Yanbu loadings incl. dark fleet | w/c 7/20 | **3.8 mb/d, "broadly stable"**; dark ~⅓ of volume (4 VLCC + 1 Suezmax + 1 Aframax AIS-off) | vs 4.7: **−19%** · vs Vortexa's own pre-level 5.16: **−26%** |
| 4 | Vortexa 30-day split [Windward pub 7/26; IndexBox pub 7/29] | Yanbu loading volumes, basis UNSPECIFIED | pre-7/19 avg vs post-7/19 (thru ~7/25) | ~5.16 → ~3.09 mb/d | **−40% — the ONLY beyond-bar read; see §3 weighing** |
| 5 | Lloyd's List Intelligence Red Sea Brief **30 July** | **AIS-VISIBLE ONLY** port calls / transits | thru 7/28 | **0 AIS-active arrivals at Saudi Red Sea ports 7/28** vs ~13/day pre-ban; 1 crude tanker tracked calling since 7/23; **11 ballast crude tankers went AIS-DARK approaching Yanbu 7/27**; Bab traceable transits 225/wk (−28% w/w), 263 incl. 38 dark | **DISQUALIFIED as firing instrument** by the frozen dark-fleet-capable clause — and the 11-going-dark datum shows loading INTENT continuing |
| 6 | USNI News 7/31 (citing Lloyd's List Intelligence) | Qualitative loading behavior | 7/31 | Tankers loading at Yanbu taking **lighter loads** to transit **Suez** rather than risk Bab | Loadings CONTINUING; volume-per-hull down for draft/route reasons — a routing adaptation, not terminal collapse |
| 7 | Kpler corporate blog (late July) | ⚠️ Bab **TRANSITS** of WC-Saudi-loaded crude — headline says "loadings," body measures **crossings** | 6 days post-7/22 | 3.0 → 1.5 mb/d, 6 vessels (**−50%**) | **NOT a loadings series — LOADING ≠ LIFTING. Leg-2-adjacent. Citing the headline would false-fire leg-3** |

**Dark-share migration, and it changes the instrument landscape permanently:** dark loadings were ~⅓ of Yanbu volume w/c 7/20 → by 7/24, 8 dark at berth + 3 dark waiting, zero AIS-active confirmed → by 7/26, **11 dark at berth + 3 dark waiting, ALL vessels dark** [Windward 7/26, IndexBox 7/29] → 7/27, 11 ballast tankers cut AIS on approach [Lloyd's 7/30] → 7/28, zero AIS-active arrivals [Lloyd's 7/30]. **The AIS-visible Yanbu series is now DEAD as a loadings measure — it measures transponder policy, not barrels.** The frozen spec's dark-fleet-capable clause, written 7/21 off `[[finding_ais_port_export_darkfleet_blind]]`, is doing exactly the job it was designed for.

## 3. Weighing — why NOT FIRED, and why the one −40% doesn't carry

1. **Everything corroborated lands under the bar.** Kpler, GS (total and crude, correctly scaled), and Vortexa-weekly converge on **−19% to −32%** like-for-like. Two independent delivery paths (my live pulls; WALTER's GS relay) — genuine corroboration.
2. **The single beyond-bar read (row 4, −40%) fails on four grounds:** (a) **single tracker, single delivery** — no second path reports it; (b) **internal pre/post-7/19 30-day window**, not the bar's peak-reference — its 5.16 baseline is higher than any other tracker's, so its % is not commensurable with the registered −36%; (c) **basis unspecified** (crude vs total unstated in both carrying sources); (d) **the same tracker's own weekly print for the same period (3.8, "broadly stable") reads mild** — when one source yields two figures and the interpretive characterization sits with the milder one, firing a frozen gate on the harsher one is rubric drift.
3. **Direction of dark-fleet blindness cuts toward over-stating decline, not under-stating it** — unchanged from 7/29, and now stronger: with the entire berth line-up dark, every AIS-inclusive estimate undercounts. Vortexa (dark-capable) is the most complete-coverage read and it is the mildest.
4. **Behavioral tells say loading continues:** 11 ballast (i.e., empty, inbound-to-load) tankers going dark ON APPROACH [Lloyd's 7/30] and lighter-load-for-Suez routing [USNI 7/31] are what a functioning terminal under blockade looks like — not what a loading collapse looks like.

**Leg-3 = NOT FIRED.** Margin on the best-corroborated basis: current ~−30% vs bar −36% — **~6 points, wider than the 7/29 "tightest margin" read once the basis was pinned and Vortexa's dark-adjusted read entered.**

**Leg-2 note (not tasked, one line):** still NOT FIRED and still not adjudicable on the registered metric — Lloyd's 7/30 gives Bab ALL-vessel weekly transits (225 AIS / 263 total, −28% w/w), Kpler gives Saudi-crude-only crossings (6 hulls / 6 days); **neither is the registered TANKER-specific ≥2-print-day sub-~8/day series.** The −50% Saudi-crude-transit collapse advances it directionally.

## 4. What would change this verdict

| Datum | Effect |
|---|---|
| **Kpler or Vortexa w/c 7/27 weekly print** (expect ~8/4-5) showing total-liquids ≤ ~3.0 (vs 4.7) or crude ≤ ~2.55 (vs ~4.0) | **FIRES** (that is −36% like-for-like) — adjudicate + memo, mark moves Will-gated |
| Same prints holding ≥ ~3.3 total / ~2.7 crude | NOT FIRED with margin held; drop the "tightest margin" framing |
| A second independent dark-fleet-capable source reproducing the −40% on a stated basis | Re-open this adjudication immediately |
| Official Saudi/Aramco Red Sea loading suspension ≥72h at a named terminal | Fires R3-class, bigger than leg-3 — route acute |

## 5. Context reads (same session, per spawn brief)

### 5a. Encelia/Layla sinking watch — RESOLVED: NO SINKING (window closed 7/26; swept through 8/2)
- **Encelia:** fire at bow contained by crew, **did not spread to oil tanks, vessel afloat, crew safe, authorities secured vessel** [SPA/Saudi Transport Authority via BOE Report 7/22-23; Seatrade; multi-source]. No sinking, salvage, or abandonment report on any live-dated source through 8/2.
- **Layla:** the claimed second strike was **never independently confirmed** (Houthi claim only; UKMTO could not verify) — nothing to resolve.
- **Consequence:** the pre-registered D→75 sinking trip (7/23 adjudication §4) did NOT trip on this pair. Sinking-watch is CLOSED-NO-EVENT.
- 🚨 **New vintage trap registered:** searches for "Red Sea tanker salvage/towed to safety" surface the **SOUNION — August-September 2024** (Greek-flagged, Hodeida). Any "stricken Red Sea tanker towed" story attaching to Encelia is 2024 residue.

### 5b. Co-belligerency falsifier — WINDOW OPEN, day 4, NO fire either way
Registered 7/29 (advisory, for BRENT/HAWK/Will): *does the next Saudi-oil-infra attack originate from the Iraq corridor within ~7-14d of 7/29 (confirms RAISES) — or does the corridor stay quiet on oil targets 14+ days (evidence for LOWERS)?*
- Swept 8/2: **no new Saudi-oil-infra attack from ANY corridor since 7/29.** The last corridor events remain 7/27-28 (Abqaiq-area drones from Iraq + second-wave Eastern Province interception, Saudi cabinet "decisive response" 7/28 [bne IntelliNews]; US+Saudi counter-strike on Iraqi militia sites 7/29).
- **Neither branch resolves before ~8/5 at the earliest (7-day mark); LOWERS-evidence accrues at 8/12 (14-day mark) if the quiet holds.**
- **Displacement observation (assessment, not a falsifier input):** since 7/29 the kinetic locus against energy/shipping has moved to the **HORMUZ enforcement corridor** (IRGC 7/31 tanker claims; GasLog Shanghai struck 8/1) — consistent with the 7/29 CENTCOM wave degrading Iranian capability being answered at sea rather than via the Iraq corridor. Watch both.

### 5c. NEW theater datum — GasLog Shanghai struck in Hormuz 8/1 (UKMTO + operator confirmed; NOT a gate input)
- **8/1:** LNG carrier **GasLog Shanghai** (Qatari cargo) struck by an **unknown projectile** ~11nm NE of Lima, Musandam (Strait of Hormuz); engine-room damage, blackout, fire extinguished, **not under command**, no casualties [UKMTO; vessel's shipping manager; Bloomberg 8/1; multi-source 8/1-2]. Second same-day incident: large splash/explosion close to another vessel ~21nm NE of Khasab [UKMTO].
- **Theater-check before gate-check:** Hormuz, not Bab — **touches NO GATE-FALCON-001 leg.** Attribution unclaimed.
- **Molecule pattern, third instance:** Ras Laffan trains (March, FM live) → GasLog **Salem** at Damietta (7/29) → GasLog **Shanghai** in Hormuz (8/1). **The LNG event class identified as the structural blind spot on 7/30 is now generating events at ~2/week, and twice in 4 days against the same operator's hulls.** `VX-FALCON-GASLNG-01` is the (new, correct) home. Read-through: SAM (Qatari LNG transit risk now kinetic INSIDE Hormuz, on top of the 17%-capacity FM), BRENT (tape), HAWK (cross-war).

### 5d. IRGC 7/31 "two tankers struck under US escort" — CLAIM-ONLY, guard held (full disposition §6)

## 6. Inbox dispositions

**① WALTER SIG-W-20260731-009 (IRGC claims two tankers struck under US escort, 7/31)** — full vintage + theater + corroboration discipline run:
- **Corroboration as of 8/2: NONE for the specific claim.** No hull names/flags/operators, no neutral authority (UKMTO/CENTCOM/Lloyd's), no damage assessment. CENTCOM's 7/31 statement dismisses it ("the Strait of Hormuz remains open... thousands of ships have sailed through in the past four months") [Maritime Executive 7/31 16:10]. **"Disabled" is a damage claim, not a loss; no sinking claimed. GATE 2 stays NOT FIRED — WALTER's read confirmed.**
- **⚠️ The 8/1 GasLog Shanghai strike does NOT corroborate this claim** — different day, one hull not two, no escort element, unclaimed. It corroborates the *pattern* (live kinetic enforcement in the corridor) while the 7/31 claim stays claimant-only. **Grade them apart** — same discipline as fatality-vs-Nasr-2 (`KB-FALCON-071`).
- WALTER's three date-traps (July-7 CBS/Hill "80-target retaliation"; July-7 Al Rekayyat; July-26 mine claim) **held** — none absorbed. The insurance-directive leg (IRGC telling shippers/insurers to ignore CENTCOM) noted as an information-layer attack; watch on WARRISK surfaces, no instrument built (proxy scope).
- **Blockade-count discrepancy flagged, not reconciled:** CENTCOM-attributed counts circulate as **20 redirected / 2 disabled / 2 boarded** [Maritime Executive 7/31] AND **24 redirected / 4 disabled+boarded** [Anadolu, "Thursday" = 7/30] vs 18/2/2 [UANI 7/28]. Cite with source+date until one series stabilizes.
- Disposition: **acted** (this report + KB rows). Board-logged, moved to `inbox/WALTER/processed/`.

**② DAEDALUS 7/30 (war-split findings — all three accepted, fixes shipped)** — informational; no action owed by FALCON (fixes live in DAEDALUS's build docs; OSPREY flags are OSPREY's). One durable point worth the next real session's attention: DAEDALUS confirmed **"the L-grade of an agent says nothing about its scope coverage"** and adopted the row-shape check fleet-wide. Disposition: **noted**, moved to `inbox/processed/`.

## 7. Routing recommendations (PROME routes; I write to no other agent's dir)
- **BRENT** (🟠): leg-3 NOT FIRED, margin ~6pts on pinned basis; Yanbu loading continues dark + lighter-loads-via-Suez; the Kpler "loadings cut in half" headline is a TRANSIT series — don't let it into a loadings-keyed gate. GasLog Shanghai 8/1 = kinetic event INSIDE Hormuz on an LNG hull; tape is yours.
- **SAM** (🟠): third LNG kinetic event; Qatari transit risk now demonstrated inside Hormuz on top of the Ras Laffan FM. Premium-vs-physical on the gas molecule keeps degrading.
- **HAWK** (cc): Hormuz-corridor displacement read (5b); cross-war synthesis. NEXUS_BRIEF was NOT refreshed this proxy run — real FALCON owes it at next boot.
- **OSPREY** (info-only, via PROME if warranted): nothing cross-theater this session.

---
*Method: frozen-semantics discipline (bar re-derived, never re-set); `[[finding_ais_port_export_darkfleet_blind]]` now load-bearing (dark-fleet-capable clause disqualifies the AIS-visible collapse); LOADING≠LIFTING (row 7 trap); `[[finding_theater_check_before_gate_check]]` (GasLog Shanghai = Hormuz, no Bab leg); `[[finding_subagent_year_verification]]` (April-2026 Baird "loadings stumble" caught + Sounion-2024 salvage trap registered + WoodMac March→June −41% flagged as wrong-window); claim-vs-event grading (IRGC 7/31 vs GasLog 8/1). ZERO mark moves — proxy hard rule.*

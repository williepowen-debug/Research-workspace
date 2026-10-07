# BRENT — October 7 news catch-up (WALTER -002/-007/-008/-009/-014)

**Session:** 2026-10-07 11:06–~12:00 ET, PROME-spawned wave 2 (Will's 10:40 ET "go"), Claude Code cloud container. **Scope:** dated evidence and owner reads only. No trade proposal, no deploy re-ask, no threshold or gate-letter change. **$0.**
**Vintages:** vendor quotes 11:02 ET futures / 11:12 ET equities (yfinance, NOT CME settles; [snapshot.json](snapshot.json), reader [pull.py](pull.py)); EIA WPSR week ending 10/2 read at `ir.eia.gov/wpsr/{summary.txt,table1.csv,table4.csv,table7.csv}` 11:0x ET (EIA API key absent; the WPSR highlights PDF is discontinued since 9/23); NHC Advisory 4 (10:00 CDT); MMA/BSEE release 10/6 11:30 CDT.

## 1. Tape (vendor, 11:02 ET futures)

| Item | Level | Note |
|---|---|---|
| Dec Brent (BZZ26) | **$101.65** | Jan $98.61 · Feb $96.22 ⇒ **Dec–Feb +$5.43** (10/5: +$6.20) — backwardation narrowed |
| Nov WTI (CLX26) | **$89.47** | Dec $88.64 ⇒ Nov–Dec +$0.83; **Dec WTI–Brent −$13.01** (10/5: −$13.31) |
| Nov ULSD (HOX26) | **$4.7178/gal** | +3.2% vs 10/6 settle-window VWAP $4.5709; intraday high $4.7603 |
| Nov RBOB (RBX26) | $3.2973/gal | ≈ +0.3% vs 10/6 window |
| USO | **$144.97** (11:12 ET) | 10/6 close $144.91 |
| VLO | $424.79 (11:12 ET) | 10/6 close $419.22 |

## 2. Nov ULSD crack (HOX26×42 − CLX26) — settle-window proxy, source ③ ESTIMATE

| Session | HO VWAP 14:28–14:30 | CL VWAP | **Crack** | Cross-check |
|---|---|---|---|---|
| Fri 10/2 | 4.5020 | 91.090 | **$97.99** | TERRY ⑫-bis proxy $97.97 (agrees $0.02) |
| Mon 10/5 | 4.5413 | 89.333 | **$101.40** | Yahoo daily bar dated 10/5: $101.47 (PROME GATES read) — $0.07 apart |
| Tue 10/6 | 4.5709 | 89.426 | **$102.55** | Yahoo daily bar dated 10/6: $102.47 — $0.08 apart |
| Wed 10/7 | — (window not yet open) | — | **≈$108.5–108.7 intraday** (10:57–11:02 ET bars) | not a settle; graded only from the 14:28–14:30 window or CME |

**VLO-HELD-01 read (TERRY grades; BRENT supplies):** every session 10/2–10/6 sits **$7.8–12.4 above the $90.16 sell line and $3.0–7.6 above the $95 notice**, outside the ±$0.15 UNKNOWN band. B1: Trump's 10/5 EO "Emergency Tax Relief on Diesel Fuel" is an excise deferral with no export text (WALTER PRIMARY) — a federal diesel excise action is named NOT-B1 in the letter. ⚠️ The vendor's `previousClose` for 10/6 (HO 4.6396, CL 90.21 ⇒ $104.65) is the **23:58 ET evening-session last trade**, not the settle; do not use it as a settle basis.

**What drove the 10/7 diesel bid — DRIVER NOT ESTABLISHED.** Facts from the 1-min path (30-min marks): crack $102.5 at the 10/6 window → $104.6 by 21:30 ET → $106.7 at 04:00 → **$109.3 at 05:30 ET** (the 04:00–05:30 leg = London morning) → $109.2 at 10:00 → **EIA 10:30 took ~$0.8 off** → $108.5 at 11:00. Over the same span **CL −$0.04, RB crack only +$0.7, HO crack +$6.0** ⇒ a distillate-specific bid, not a crude or gasoline move, and not timed to a US data release. Coincident candidates, none attributed by a wire I found: (a) Isaias' Gulf Coast refinery exposure (CNN 10/6 track story; OilPrice 10/7 02:30 ET evacuation story; Pascagoula inside the hurricane watch issued 11:01 ET); (b) Russia — Interfax 10/6 says the diesel export ban may *ease* for some companies (diesel-bearish, so not this); (c) the excise deferral (demand-side, small). One web search returned only a 10/1 Trading Economics item. **Working read: the market is pricing Gulf Coast distillate-output risk ahead of a storm aimed at the Mississippi/Alabama refinery coast — labelled interpretation, not attribution.**

## 3. TS Isaias — Gulf production and refining exposure

**Forecast (NHC Advisory 4, 10:00 CDT 10/7, PRIMARY):** 22.4N 93.6W, 45 mph, 1000 mb, ENE 8 mph; "rapid strengthening is forecast". Track: 65 kt 08/1200Z 23.4N 90.8W → 80 kt 09/0000Z 24.6N 89.2W → **95 kt 09/1200Z (Fri 08:00 ET) 26.6N 88.1W** → 90 kt 10/0000Z (Fri 20:00 ET) 29.2N 87.5W → inland 32.2N 87.6W Sat. **Hurricane Watch: Bay St. Louis to Indian Pass. Storm Surge Watch: Mouth of the Mississippi to Yankeetown (5–7 ft Ocean Springs–Indian Pass incl. Mobile Bay). TS Watch: Jefferson/Plaquemines Parish line to west of Bay St. Louis; east of Indian Pass to Aucilla River.** TS conditions midday Friday; hurricane conditions late Friday. Next: intermediate 13:00 CDT, full 16:00 CDT. ⚠️ Day-2/3 track error is large; the earlier OilPrice/search text "landfall most likely near New Orleans" is a superseded forecast.

**Offshore production (PRIMARY, MMA/BSEE release 10/6, operator reports as of 11:30 CDT):** **185,120 b/d oil shut in = 9.24%** (implies a ~2.00 mb/d current Gulf base); gas 72 MMcf/d = 3.36%; **0 of 371 manned platforms evacuated; 0 of 10 non-DP rigs; 0 of 17 DP rigs moved. "Reflective of 1 company's reports."** Next update **13:00 CDT daily** (10/7 update not yet out at this read). Operators (press, not BSEE): Chevron relocating non-essential personnel, "production from Chevron-operated assets remains at normal levels" (OE Digital 10/7); Shell non-essential staff off six platforms — Stones, Mars, Olympus, Ursa, Vito, Appomattox (search summary of press, SINGLE, not opened); BP evacuating non-essential (OilPrice 10/7 01:30 CDT, SINGLE).

**Geometry [EST, no platform-coordinate file read this session]:** the 95 kt point (26.6N 88.1W) and the run to 29.2N 87.5W pass just east of the Mississippi Canyon / DeSoto Canyon deepwater hubs (Mars/Ursa/Olympus, Thunder Horse, Na Kika, Appomattox, Vito) — inside the hurricane-force field, on the weaker west side. Green Canyon hubs further west sit in the tropical-storm field; Perdido/Whale (~95W) are behind the storm.

**Analog [MULTI, BSEE via S&P Global/Offshore 9/16/2020]:** Hurricane Sally (Cat 2, landfall Gulf Shores — near-identical landfall) peaked at **508,366 b/d = 27.48%** oil shut in. **Isaias range [EST]: 25–50% ≈ 0.5–1.0 mb/d for ~3–4 days ⇒ ~1.5–4M bbl lost**, set against 424.1M US commercial crude and 243.6M PADD 3 (EIA wk 10/2). Isaias is forecast stronger in the central Gulf than Sally but faster-moving (shorter outage). Pre-storm shut-ins before Friday: **likely to rise from 9.24% on Thursday's 13:00 CDT update** given the hurricane watch; size UNMODELED beyond the analog band.

**Refineries [EST capacities from memory, not re-read this session]:** the one large plant inside the hurricane watch is **Chevron Pascagoula, MS (~0.36 mb/d, a large distillate/jet producer)**, on the west (weaker) side of a Mobile Bay–Pensacola landfall. The Mobile-area plant is small. The Louisiana river belt (Garyville, Norco, Convent, Baton Rouge, Chalmette, Meraux) is west of the hurricane watch; only the Plaquemines fringe is in the TS watch. LOOP (~28.9N 90.0W) is ~2° west of the track; offloading pauses on sea state are likely but unconfirmed. ⚠️ OilPrice's "six Gulf Coast refineries … 14.1 mb/d, half of US capacity" is internally inconsistent and is not used.

**Read-through:**
| Channel | Sign | Size [EST] | Timing |
|---|---|---|---|
| Offshore crude shut-in | WTI/USO + | ~1.5–4M bbl, transient | Thu–Sat; restart days after |
| Refinery run cuts (Pascagoula ± Mobile) | crack +, crude − at the margin | ≤ ~0.4 mb/d for days if hit | Fri–Sun |
| Port/LOOP pauses | mixed, local | small | Thu–Sat |

**USO before Fri 15:00 ET (energy read only; TERRY owns the card):** USO $144.97 needs **+3.5% to $150**, ≈ +$3.1 on the front WTI. Isaias is a **crack catalyst more than a WTI catalyst**: the offshore loss is small against inventories and partly offset by refinery run cuts, and it is already partly priced (hurricane watch public 11:01 ET). On realized volatility alone (USO 20-day 2.83%/day, 45% annualized; ~2.2 sessions left), a +3.5% move by Friday 15:00 is roughly a **1-in-5 outcome [EST, lognormal, no drift; not a valuation or a recommendation]**. The larger WTI swing factors this week are the Middle East (more Hormuz hits vs Trump's "end very soon" and Qatar mediation) — not the storm.

## 4. EIA WPSR, week ending 10/2 (PRIMARY, released 10/7 10:30 ET)

| Series | Level | w/w |
|---|---|---|
| Commercial crude | **424.134M** | **−3.186M** |
| SPR | 282.983M | −0.784M |
| **Cushing** | **24.745M** | **+0.444M** (API +0.87M) |
| Gasoline | 204.744M | +0.382M |
| Distillate | **105.138M** | **−0.042M** (12% below 5-yr avg) |
| Jet | 42.504M | −1.108M |
| Refinery utilization | 92.7% | inputs 16.480 mb/d (+0.223) |
| Crude exports | 4.765 mb/d | +1.195 |
| Total product exports | 8.073 mb/d | +0.579 |
| Distillate product supplied | 3.650 mb/d | −0.299 (4-wk −1.6% y/y) |
| Crude production | 13.979 mb/d | +0.024 |

Gasoline 4-wk product supplied −0.3% y/y — **outside BRT-31's window (the 10/2 print is not graded; first window week 10/9, release 10/15).** **Cushing <20.0M re-activation: NOT re-activated — 24.745M is 4.745M above the line;** state stays RESCINDED / ARMED-FOR-REACTIVATION (single print <20.0M re-activates; REGISTRY CUSHING-20M). ⚠️ boot's CUSHING-20M "STALE human stamp" finding is a keyless-container artefact (probe reads the EIA API); this read is at the primary CSV.

## 5. Khurais / East-West line — Petroline flow book (new event, record-only)

| Claim | Source / grade | Note |
|---|---|---|
| A Khurais **pumping station** on the East-West line was hit ~10/4 | AFP via FMT 10/5 (MULTI on the strike, per WALTER) | Not a production-plant hit on this evidence |
| The line "stopped again" | AFP | duration UNVERIFIED |
| Flows normal 10/5 | Bloomberg/Reuters anonymous sources | anonymous; binds nothing |
| Throughput ~5.8 mb/d 10/6 | Saudi energy minister via Reuters (lane, not re-read at primary this session) | a ministerial figure — the R1 source class — but an *availability* statement, not a loss figure |
| "East-West at 5.5mn b/d; temporary bypass around the struck station; >75% of capacity" | Argus (search summary only; article body not retrievable; date unconfirmed) | context for the 9/10 instance |

**Owner position:** ⛔ BG-02's throughput resolver for instance (4) **LAPSED 9/25 ⇒ NOT MET, no extension (WQ-264 ③)**; this event **cannot fire it** and does not re-open it. **No new letter is proposed here.** The successor restart resolver (`setups/2026-09-18_saudi-restart-resolver-PROPOSAL.md`) stays queued behind the WQ-264 shadow (→10/24) and is the only Saudi-relief grader (WQ-331 P4). Deploy question **CLOSED** (WQ-192 STAND DOWN). **Net flow read:** the conflicting reports converge on a short interruption at most; the minister's 5.8 mb/d sits above the ~5.5 mb/d pre-9/10 rate reported 9/28 — **no measured new Saudi loss** (UNKNOWN stays UNKNOWN). Gulf exports back near pre-war (Kpler 18.3 mb/d 7-day by 9/30; Shell CEO "80-plus percent" of pre-war) against continuing hits (≈9 UKMTO reports in October, latest number found 156-26; none sunk) — a premium, not a supply loss, which matches the tape: Dec–Feb Brent backwardation narrowed $6.20 → $5.43 since 10/5. **INCIDENTS.tsv:** not logged — no primary damage confirmation, and FALCON's live STRIKES.tsv has no 10/4 Khurais row (its Khurais rows are the April production-facility hits). FALCON adjudicates.

## 6. Context only (no BRENT line moved)

- **-008 supply measures:** SPR exchange up to 40M bbl (10/5) — part of the March 172M commitment per Rigzone (SINGLE); whether it counts toward the G7 100M is UNVERIFIED; awards not found. CATALYSTS rows 10/6 (STEO, SPR bids) remain **ungraded** — an expired date is not completion. Russia: ban "extended through October" (9/30 reports) vs Interfax 10/6 "may be lifted for some companies in October" — both lane headlines; diesel-bearish if true.
- **-009 Black Sea:** Alfa Watan type unstated ⇒ the vessel-sunk frame-breaker has no object; Ukraine's "51% of Russian refining out" is a belligerent claim (OSPREY owns). Directionally consistent with the EXPORT-SIGN WARNING row (refinery outages free crude, tighten products) and with a distillate-led tape.
- **-014 El Niño:** AEOLUS-owned correction (CPC 9/10 >90% very strong; update Thu 10/8). Winter heating-demand context only.

## 7. Armed state (later prints this session will not see)

| When (ET) | Print | What it decides | Owner |
|---|---|---|---|
| Wed 10/7 14:00 (13:00 CDT) | MMA/BSEE shut-in update | first evacuation counts | BRENT read, next session |
| Wed 10/7 14:28–14:30 | Nov crack settle window | VLO-HELD-01 A (≈$108 intraday, far above $90.16/$95) | TERRY |
| Wed 10/7 17:00; Thu 10/8 | NHC Adv 5–8; BSEE update 14:00 | shut-in size before Friday | BRENT |
| Fri 10/9 15:00 | USO Oct-09 $150C stop | Will's hand, TERRY card | TERRY / Will |
| Fri 10/9 ~15:30 | CFTC COT as-of 10/6 (vintage #9) | COT-FUEL-35B grade: `cot_grade.py --expect 2026-10-06`, raw f_disagg.txt cross-check | BRENT |
| Fri 10/9 13:00 | Baker Hughes | context only (BRT-26 retired) | BRENT |
| Thu 10/15 (Columbus Day shift; BRT-31 letter registers 12:00) | WPSR wk 10/9 | Cushing <20.0M single-print re-activation · BRT-31 first eligible print | BRENT |

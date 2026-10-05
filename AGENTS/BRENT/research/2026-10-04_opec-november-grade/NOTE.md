# BRENT — 2026-10-04 · OPEC+ NOVEMBER GRADE (DOCKET L297 / CATALYSTS 2026-10-04) — OUTCOME (1) NOVEMBER HELD

**Session:** PROME (prome-ed) Tier-1 WQ-184 due-row spawn, L0. Sun 2026-10-04, markets closed. Graded on day zero at the primary the frozen letter names; nothing provisional, no re-read owed.
**$0 moved. No trade proposed. No threshold, gate, falsifier or score created or moved.**

## 1. Verdict

| Letter outcome (CATALYSTS 2026-10-04 row, registered 2026-09-06) | Verdict | Evidence |
|---|---|---|
| **(1) NOVEMBER HELD at October's required production** | ✅ **MET** | Statement: *"decided to maintain September 2026 required production for November 2026."* The 9/6 statement held October at September. So Nov = Oct = Sept: the **second consecutive monthly hold**. |
| (2) A November increment resumed | ❌ NOT MET | No kb/d adjustment in the text. |
| (3) No November decision / deferred | ❌ NOT MET | A November number was decided. Next meeting **1 November 2026**. |

Per the letter, a second consecutive hold is the first evidence that lets this desk use the word **"pause"**. That word now applies to the **paper quota path (Sept→Oct→Nov)**. It does not apply to any physical supply claim (see §3).

## 2. Primary, read whole

- **Seven-country statement:** `https://www.opec.org/pr-detail/1891616-4-october-2026.html`. urllib GET returned 200, 233,464 B, 2026-10-04 11:36 ET. Entered via the root page `https://www.opec.org/` (200, 247,409 B, 11:36:49 ET), as the 9/6 routing note says. Local copy in this dir, sha256 `833fd0d8…570557`.
  > The seven OPEC+ countries … Saudi Arabia, Russia, Iraq, Kuwait, Kazakhstan, Algeria, and Oman met virtually on 4 October 2026 … **The seven participating countries decided to maintain September 2026 required production for November 2026 as detailed in the table below.** … The next meeting will be held on **1 November 2026**.
- **68th JMMC (same date):** `https://www.opec.org/pr-detail/1870617-4-october-2026.html` (200, 232,025 B; sha256 `00da2cb7…3fa316f`). Notable sentences (observation, not graded): the JMMC *"expressed concern regarding attacks on energy infrastructure, noting that restoring damaged energy assets to full capacity is both costly and takes a long time, thereby affecting overall supply availability."* It reviewed July/August data and noted "overall conformity". **Next JMMC (69th): 29 November 2026.**
- **No 2027-baseline or ONOMM decision** appears in either release (SEARCH-NOT-FOUND on the root page's 4 October list, which carries only these two). This matches the letter's premise that 2027 quotas are a November matter.
- **The wire WALTER relayed** (SIG-W-20261004-002, CNBC 13:01Z "keep November targets steady") agrees with the primary on direction. **The grade uses the Secretariat text, not the wire.**

## 3. Deliverability gate: fresh pull, not carried forward

| Read | Value | Basis |
|---|---|---|
| EIA STEO `COPS_OPEC` (OPEC total spare crude capacity), Oct–Dec 2026 | **0.02 mb/d** each month; 0.03 Jan–Mar 2027; **2.38 from Apr 2027** | EIA API v2 `steo` route, pulled 2026-10-04 15:37:40Z. Response saved in `eia_api_COPS_OPEC.json` with the key redacted. |
| Vintage of that read | STEO released **2026-09-09**, forecast completed 2026-09-03; **next release 2026-10-06** | EIA STEO overview page, fetched 11:37 ET today (`steo_overview.html`). |
| `COPS_R05` (Middle East OPEC) via the API | No rows returned | API facet not populated. The 9/9 xlsx read (zero through Mar 2027) stands as the last read of that series. |
| Second agency (IEA OMR / OPEC MOMR spare figure) | **SEARCH-NOT-FOUND** | One web search found no dated Sept-2026 IEA spare figure. The 9/11 oilandgas360 piece has no number. The figure is still **single-agency** (LESSONS #17 binds: cross-reference not available this cycle). |

**Applied, with a population limit:** `COPS_OPEC` covers OPEC, while the seven-country decision also includes Russia, Kazakhstan and Oman. The September-vintage **0.02 mb/d** observation therefore supports only a conditional inference that the OPEC subset had little modeled spare capacity; it does **not** measure the seven participants' counterfactual deliverable increment or the hold's physical effect. The verified result is the November paper-quota hold. Any physical-barrel estimate awaits a matched participant-level counterfactual; the October STEO will update only the OPEC series.

⚠️ **Fresh is not the same as new vintage.** The figure re-pulled today is the current published vintage (9/9). The October STEO lands Tue 10/6 and supersedes it. That read is already on CATALYSTS 2026-10-06.

## 4. Position-relevant read (consumer read, no action)

- **Expected direction; price effect unmeasured.** Pre-meeting sourcing expected a hold: two Bloomberg delegates and two Reuters sources on 9/29 (CATALYSTS 10/2 data refresh), plus Reuters via EnergyNow "set to keep output targets steady at Sunday meeting". That establishes consensus direction, not a zero expectations gap or an absence of signaling effects. No event-window pricing test was run and markets were closed at the grade.
- **USO 37 sh / USO Oct-09 $150C ×1:** the OPEC+ outcome does not change a registered line for either position. The 150C's 10/09 sell-or-roll rail and TERRY's 15:00 stop are untouched. The order is Will's.
- **VLO 1 sh / GATE-TERRY-VLO-HELD-01:** no bearing. Crude quota policy at ~0 spare does not move the Nov ULSD crack's leg-A line ($90.16 settle).
- **WQ-192 STAND DOWN:** unchanged. Nothing here re-arms anything.
- **Registered lines moved: NONE.** No futures settle exists today (markets closed). No vendor read was taken for this grade.

## 5. Successors registered (CATALYSTS)
- **2026-11-01** seven-country meeting: the **December** required-production decision. Same three-outcome shape. A third hold vs resumed increment vs deferral, graded on the statement text with a re-pulled spare figure.
- **2026-11-29** 69th JMMC: monitoring only. Watch for any ONOMM call or 2027-baseline language.

## 6. Declared non-verifications
| Claim | Token |
|---|---|
| Per-country November required-production table ("the table below") | **UNKNOWN-AT-PRIMARY**: no `<table>` and no PDF link in the static HTML, same as 9/6. The verdict does not depend on it. |
| Spare figure agreed by a second agency | **SEARCH-NOT-FOUND** (one search, not exhaustive) |
| "Pause" as a Q4 claim | Defensible only for the **paper quota path through November**. December is decided 11/1. |

## 7. Inbox drain: the action items' assessments (all 11 dispositions are in `board_log.tsv` and the PROME packet)

**-003 RE-ROUTE (Riyadh Aramco refinery fire, 10/03), ACTION.** Searches on 10/04 found **FIRE witnessed**: a Reuters witness ("large plume of smoke and fire … in the vicinity of an Aramco facility in Riyadh on Saturday") and an AFP journalist ("flames and smoke rising from a facility … south of … Riyadh"), carried by Business Today, Kurdistan24, Türkiye Today and Malay Mail on 10/04. The Houthis **claimed** the attack (ballistic missiles + drones). **No Saudi or Aramco statement found** ("no immediate confirmation"). **DAMAGE / CAPACITY IMPACT: NOT ESTABLISHED.** Date trap noted: a 2022 Houthi-claimed Riyadh refinery fire that Aramco called "an operational incident" resurfaces on the same search. That earlier fire is not this one.
- **Scale and transmission, not outage materiality:** EIA's Saudi profile lists Riyadh nameplate at **126 kb/d** and total Saudi domestic refining capacity at **3,291 kb/d for 2023**; the matched capacity comparison is about **3.8%**. Capacity is not actual throughput, and neither figure is confirmed loss. If an outage exists, a domestic-supply refinery could tighten the Saudi product balance and reach exports through lower product exports or higher imports; the registered leg-A referent is the **NYMEX Nov ULSD (HO) crack vs CLX26**, so transmission would be second-order. **Damage, actual throughput loss, duration and yield remain UNKNOWN; present evidence cannot grade materiality or move `GATE-TERRY-VLO-HELD-01`.** Reassess only if an operator/counting source establishes loss.
- **Not logged to `refinery_damage/INCIDENTS.tsv`:** LESSONS #1 requires verification at a primary, and damage is unestablished. **Owed:** log it as ATTACKED (FIRE witnessed, damage UNKNOWN) once FALCON's Gulf strike ledger or an operator statement exists. FALCON owns the attack adjudication.
- Futures are not open yet. No price read was taken.

**-004 (VLCC ~$1.3M/day), INFO.** Not verified at a Baltic, Clarksons or Lloyd's primary; those are paywalled or unreached. The search layer has **TD3C TCE ~$1.21M/day as of 9/17** (Sparta Commodities snippet) and a TD3C print of **WS600 ≈ $17.7/bbl** ex-Ras Tanura (Hellenic Shipping, undated snippet). So **$1.3M/day is the right order of magnitude for TD3C TCE. The "$33/bbl" figure does NOT reconcile** with the WS600 ≈ $17.7/bbl route figure and is not carried. Boundary #5 stays NO INSTRUMENT (retired 2026-07-31). This is not a boundary trip.

**-009 (JPM Oil Markets Weekly, 9/9), ACTION.** The view is 25 days old.
- **DUPLICATES** the desk's read on the main mechanism: the shock is absorbed down the barrel through record product cracks. That is THESIS v5.11's crack-led channel and the reason the refiner leg exists.
- **ADDS** one dated number to weigh, not adopt: ~13.5 mb/d of Middle East flows including reroutes, ~10 mb/d below normal. It is JPM's estimate. This desk does not hold a matched aggregate, and it is not reconciled to FALCON's Petroline or Hormuz figures.
- **CONTRADICTS on curve shape:** JPM's "front ~$6 too high / back ~$10 too low" is a view against the backwardation this desk reads as physical tightness. It is recorded as a dissenting dated view. The **$87 forever-conflict vs $64 peace 2027** scenarios are logged as context, not as targets. No registered line moves.

**-016 (Qatar Ras Laffan "not back for winter"), ACTION.** The Bloomberg primary was **not reached**. One search returned only 2015–2021 articles: SEARCH-NOT-FOUND, paywalled. WALTER's framing caveat stands: it is a **buyer's** expectation, not a Qatar statement. The desk's gas read is unchanged. The existing Qatar force-majeure state stays with HANS (T-07 TTF and T-08 storage gap are both already fired), so this deepens a fired mechanism and does not change it. **DEFERRED:** verify at the Bloomberg primary when it is reachable.

**-011 (Trump "not going to be doing a diesel export ban", Reuters 10/02 22:19 GMT per WALTER), INFO.** One own search did not surface the exact quote (SEARCH-NOT-FOUND for the verbatim). Argus "Trump moderates calls for diesel export ban" and the WaPo/EU-optimism coverage support the direction. ⚠️ **Sign note for TERRY:** WALTER frames this as "a bullish-diesel policy catalyst withdrawn". That is the global framing. For a **US refiner (VLO)**, a US export ban was the **bearish** tail, because barrels kept at home lower the US crack. That is exactly why `GATE-TERRY-VLO-HELD-01` leg B1 = a signed restriction text ⇒ SELL. So a principal-level denial **lowers the probability of B1 firing**. It does not grade B1, and an unsigned denial can be reversed. TERRY grades.

## 8. Governing lessons (`lessons_check.py --spec`, run on this note)
- **L10 HONOURED: paper quotas are not physical production.** This is the whole of §3. The hold is graded as a paper event; the 0.02 mb/d OPEC-only forecast is contextual and does not quantify the seven-country physical effect.
- **L17 HONOURED and still binding.** The spare figure is one agency's, and the cross-reference was SEARCH-NOT-FOUND again. The 11/01 successor row requires another re-pull and a search for a second agency.
- **L11 / L16 HONOURED, scope stated:** they govern **price at announcement**. Pre-meeting sourcing establishes an expected direction, but no event-window price gap or signaling effect was measured; markets were closed at the grade.
- **L22 HONOURED:** the successor letter names its instrument (the Secretariat text, URL pattern, entry route), three exhaustive outcomes, and a binding re-pull. It is not a BRT-xx.
- **L06 HONOURED (Riyadh, §7):** the crack read, not crude, carries the refinery-fire assessment.
- **L23 HONOURED:** no `=F` continuous ticker is used anywhere in this grade; no price is used at all.
- **L18 / L19 / L21 / L25:** deliberately not applicable. There is no reopening or tanker-liveness claim, no threshold spec was written, and no source hung. The opec.org root and both releases returned 200.

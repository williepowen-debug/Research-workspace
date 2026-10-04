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

**Applied:** at ~20 kb/d of spare, holding November at September's level removes about nothing physical relative to an increment, and an increment would have been ~90% paper. **The hold is a near-zero physical event.** What it does mean: the producer group did not choose to add paper barrels into a $100+ Brent tape. That is consistent with capacity they cannot deliver, which the JMMC's damaged-assets sentence also implies. It is not a supply-support decision.

⚠️ **Fresh is not the same as new vintage.** The figure re-pulled today is the current published vintage (9/9). The October STEO lands Tue 10/6 and supersedes it. That read is already on CATALYSTS 2026-10-06.

## 4. Position-relevant read (consumer read, no action)

- **Expected, so a non-event for Monday's open on the expectations gap.** Pre-meeting sourcing expected a hold: two Bloomberg delegates and two Reuters sources on 9/29 (CATALYSTS 10/2 data refresh), plus Reuters via EnergyNow "set to keep output targets steady at Sunday meeting". No increment was priced to be removed.
- **USO 37 sh / USO Oct-09 $150C ×1:** the OPEC+ outcome does not change the oil read for either line. The hold was expected and carries ~0 barrels. The 150C's 10/09 sell-or-roll rail and TERRY's 15:00 stop are untouched. The order is Will's.
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
- **Crack materiality, assessed:** Riyadh is a domestic-supply refinery. Its nameplate is ~126 kb/d **[EST, desk prior, NOT re-verified at primary this session]**, which is ~1% of Saudi crude runs. A full outage would mainly tighten the Saudi domestic product balance. It would touch the export market only through lower Saudi product exports or higher imports. The registered leg-A referent is the **NYMEX Nov ULSD (HO) crack vs CLX26**, so transmission from Riyadh is second-order. **Assessment: directionally crack-SUPPORTIVE (against the leg-A sell line), magnitude small and unestablished. NOT material to `GATE-TERRY-VLO-HELD-01` on present evidence.** It becomes material only if an operator statement establishes multi-week loss of a larger unit set.
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
- **L10 HONOURED: paper quotas are not physical production.** This is the whole of §3. The hold is graded as a paper event at ~0.02 mb/d of spare.
- **L17 HONOURED and still binding.** The spare figure is one agency's, and the cross-reference was SEARCH-NOT-FOUND again. The 11/01 successor row requires another re-pull and a search for a second agency.
- **L11 / L16 HONOURED, scope stated:** they govern **price at announcement**. The near-zero reading here concerns **barrels**, not the tape. The hold was expected, which is a separate reason no price gap is forecast, and this is not a forecast that Monday's tape ignores OPEC.
- **L22 HONOURED:** the successor letter names its instrument (the Secretariat text, URL pattern, entry route), three exhaustive outcomes, and a binding re-pull. It is not a BRT-xx.
- **L06 HONOURED (Riyadh, §7):** the crack read, not crude, carries the refinery-fire assessment.
- **L23 HONOURED:** no `=F` continuous ticker is used anywhere in this grade; no price is used at all.
- **L18 / L19 / L21 / L25:** deliberately not applicable. There is no reopening or tanker-liveness claim, no threshold spec was written, and no source hung. The opec.org root and both releases returned 200.

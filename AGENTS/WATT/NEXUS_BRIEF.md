# WATT — NEXUS Brief

**Status:** P1/P2/P3/P4 = **3**/5/4/2; **composite 14/20** (was 16/20). P1 de-escalated 5→3 November 5, D:L866 MET on the registered letter.
**Domain:** Grid stress → wholesale price → industrial/data-center cost.
**Thesis refinement:** Distinguish delayed/cancelled forecast load from the generation queue, and planned supply from delivered capacity.
**As of:** verified 5-min tape October 23–November 4 (window n=2,028 of 2,028); unverified 5-min to 18:15 EPT November 5; EIA-930 demand to 22Z November 5; posting ids, DOE index, Inside Lines and winter outlook read 18:23–18:33 ET November 5; P3 as read October 20. **STATUS commit c153b55a6.**

## CROSS-DOMAIN

**SENDING:**

| To | Finding | Consequence and limit |
|---|---|---|
| HENRY / AEOLUS / PROME / NEXUS | **P1 5→3 November 5 (D:L866 MET):** no real EEA-class posting, no 202(c), no RED re-fire October 28–November 3 on a complete verified tape [KB191/193] | ⚠️ Not an all-clear: November 1 00:25–00:35 verified $1,273.52/$2,015.32/$2,015.32 at 92.6–91.1% of trailing peak met price only, no posting, cause unknown [KB192]. November 3 EEA-labelled postings are PJM's winter drill |
| CARL / HENRY / VULCAN / PROME | **2029/30 BRA: window December 9–15, results December 22, cap $337.83, Reliability Requirement 158,712 MW** [KB196]. WATT-14 clear at cap 88%, WATT-15 shortfall above 6,831 MW 45% | PJM or FERC can move it. Maryland OPC argues the February 2027 forecast could undercut the target; Exelon's complaint leaves December as planned |
| CARL / VULCAN / PROME | Amended RBP filed October 29: bid window March 1–28, 2027, results May 10, allocation on Large Load growth, about 6,800 MW target to be recalculated [KB197] | Proposal, not approved; docket and order date unread. 630 MW is Jefferies' scenario |
| HENRY / AEOLUS / TERRY | WATT-16: RED letter fires November 6–December 15, 55%. PJM outlook 182,426 MW vs about 147,500 MW forecast peak; November–December 2025 had 0 hours ≥$500 [KB195] | PJM's forecast, one baseline year; hourly cannot show a 5-minute run |
| HENRY / AEOLUS / PROME / NEXUS | **P1 3→5 October 29 (fire October 27):** $2,026.73 / $1,970.77 / $2,297.21 at 18:50/18:55/19:00 EPT (unverified 5-min) with demand 97.9–99.8% of trailing-24h peak; verified HB18 $719.87 [KB181/182] | Letter met as written; KILL_MEMO C1 NOT fired. No emergency posting (ids 105577–105760 blank), no 202(c), retraced by 19:15, October 28–29 quiet. Outage-driven (69.5–72.7 GW forecast out, forced 12.9–13.4 GW), the same root as 10/7 and 10/13: count once. Demand limb weak in shoulder-season evenings (recorded, not changed). Found 2 days late (desk dark 10/24–28). De-escalation graded on/after 11/04 |
| HENRY / AEOLUS / NEXUS / VULCAN | **Year over year the tail got worse** (Sep 1–Oct 28 verified hourly): hours ≥$500 19 vs 1 (2025), ≥$1,000 7 vs 0; median flat ($36.78 vs $34.79), gas flat. At equal load the ≥$200 rate is higher (90–100 GW 4.3% vs 0.7%) [KB186] | Maintenance stack the same all three years (Oct 65.7/64.7/67.3 GW); the difference is demand +6.1 GW mean and October forced outages 7.0→9.4→11.6 GW while October planned fell 50.3→47.0 [KB189, corrects KB187's mixed windows]. So 'outage-driven' names the trigger, not the worsening. ⚠️ One baseline year (2024 unobtainable); fleet-size and pricing-rule changes not checked; weather vs load growth not separated (AEOLUS). Fleet: firm capacity flat ~181 GW summer 2024–26, all growth solar (12.6→19.3 GW), zero at an autumn 19:00 peak [KB188; EIA perimeter, not PJM's accredited figure]. No PJM shortage-pricing rule change found between the autumns; RCSTF reform pending [KB190, bounded search]. Evidence sent to TERRY (NOT-FIRED, no trade) |
| ISHM / PROME | Grid-equipment figure custody ACCEPT (WQ-506): Eaton Electrical + GE Vernova Power/Electrification orders/backlog are WATT's P3 supply-chain evidence [KB184] | No current figure: KB-097 (Sept 2) is stale until the next issuer print. CAT power-gen stays ISHM's |
| HENRY / AEOLUS / PROME | (history) P1 5→3 October 22: October 15–21 had no EEA-class posting, no renewed or new PJM 202(c) (202-26-50 lapsed October 16), zero of 2,008 five-minute prints ≥$1,000 (max $471.98) | The rule paying out, not an all-clear: 71.5 GW forecast offline October 22, above the October 13–14 emergency days; a RED or EEA2+ re-fire returns P1 to 5. Posting-id read cannot tell unissued from withdrawn; DOE negative bounded to the public index |
| AEOLUS / PROME | Interchange test (your 9/28 hand-back), EIA-930: on the 9/16–17 afternoons PJM imported from TVA (−404/−246 MW), exported to MISO below 9/15's level (+3,034/+2,161 vs +4,343), net interchange +742/−34 MW. Export pull NOT SUPPORTED as an incremental driver [KB177] | The outage-driven read stands, and AEOLUS's heat answer is unchanged. ⚠️ Pair flows do not reconcile to total interchange (+3.2–6.2 GW); read directions only. Hourly, not 5-min |
| HENRY / AEOLUS | October 22 complete day max $79.98, 0 ≥$500 despite a 71.5 GW outage forecast; October 23 overnight quiet [KB179] | P1 stays 3; NOT-FIRED. Unverified 5-min |
| AEOLUS / PROME | L650: PJM has not published a DR-verified July 2 peak; DM2 RTO metered hour beginning 17:00 = 162,186 MW, still is_verified=False | Record holds only on the preliminary unrestricted 168,158 MW; metered below the 2006 record of 165,563 on every basis read. 2006 comparator basis unestablished |
| VULCAN / HENRY | IMM tracks 4,016.9 MW cancelled OR delayed data-center projects as of September 21; about 42% of 9,481 MW forecast growth | Demand-realization counterevidence, not 42% of all load. IIR/public tracking; no EDC project-level adjustments or independent WATT audit. Scenario 3 shortfall 3,055 MW is not PJM's adopted forecast |
| VULCAN / HENRY | Google 890 MW new nuclear uprates expected from 2028; Amazon 190 MW new within 690 MW total, expected 2030–32 | Supply response, no current relief. Google's separate 2,700 MW agreement covers existing capacity. Issuer announcements, no inspected PPAs/permits or energized MW; no nameplate-to-UCAP netting |
| CARL / PROME | RBP accepted for filing and suspended to February 28, 2027, subject to refund/further proceedings | No September 30 procurement start or final household allocation. October 22 consultation is not approval. RBP is distinct from IRAS, EL26-67 and generator compliance |
| PROME / NEXUS / WALTER | (history) Next 2029/30 BRA moved from WATT's old mid-2027 timing to December 2026 | Exact dates now above. October 21 FERC conference was an agenda, not a ruling |

November 5 packets: DAEDALUS and VULCAN in c153b55a6. October 29 packets: ISHM 80f2aa06a, HENRY 19e6e2a4b, AEOLUS 99efd5f8d, NEXUS a862a30c4, PROME 52ad011a4. October 23 packets: AEOLUS interchange result (579588e3c), CYPHER boundary confirmed (7f94e64f4); PROME memo `PROME/inbox/2026-10-23_from-WATT_L789-touch.md`. October 22 packets: HENRY and AEOLUS (18d35b69b). File publication does not prove native notification or recipient consumption.

**WAITING FOR:**

| From | Input / date | Effect |
|---|---|---|
| PJM / FERC | Action on the amended RBP; docket and requested order date unread | Proposal, not approved. RBP outcome wake closed November 5 |
| PJM / utilities | Current total active generation queue/transition remainder and large-load verification | Old 212 GW / 1.32× and 250 GW / 1.56× estimates are historical; 168.6 GW is Cycle 1 only. IMM scenario is not an adopted forecast |
| Issuers / contracts | Nuclear approvals/in-service evidence, hedge shares and firm grid rights | No realized FCF relief or firm capacity removal inferred from announcements/reporting |
| PJM / FERC | IRAS registry compliance; EL26-67 responses November 16 / answers December 16 | Qualifying section 205 filing may suspend affected respondent duty; WATT-09 outer November 30 unchanged |

## VIEW

- Historical auction shortfalls remain real. Prospective shortage magnitude is less certain: IMM combines project delay and cancellation, while buyers fund planned supply additions. Do not rewrite auction history using a scenario.
- Nuclear uprates are expected from 2028–32; no 2026/27 online capacity, contract price or insulation of other customers from infrastructure costs is established.
- EIA October 6 forecast, input cutoff October 1: US 11-hub mean $52/MWh in 2026 and $49 in 2027; PJM 2026 +41% was already known, now primary checked. These are forecasts, not spot prices or a model including the October 13–14 emergency.
- PJM October 28–November 3 verified daily max $305.75 / $95.72 / $248.16 / $193.76 / $2,015.32 / $419.33 / $393.84. Verified feed closed the 10/24 and 10/27 gaps (max $82.19, $17.06: no hidden RED run) and the blank-id limit: ids were unissued, no posting of any class between October 16 and November 2 [KB193/194].
- (history) PJM October 15–22 complete: October 15–21 n=2,008 of 2,016, zero ≥$1,000, max $471.98 October 16; October 22 n=285 of 288, max $79.98; missing stamps isolated, no adjacent pair. Unverified five-minute tape, not settlement. P1 = 3 since October 22.
- September 17 EEA2 is primary verified; historical C1 MET, now replayed on the verified feed: 23 consecutive intervals ≥$1,000, 18:15–20:05 [KB194]. PJM October 15 says large-load backup authority unused to date, covering October 13–14; no later negative. Hedge shares unknown; Amazon rebuttal/private-record limits and Loughton firm-rights uncertainty retained.

## CALIBRATION

- **Conviction:** strong on what the cited primary documents state; provisional on project realization, future shortfall and funding-to-delivery conversion. No independent IIR census or inspected nuclear PPAs.
- **Market divergence:** unmeasured; no security/option valuation or entry edge.
- **Scores:** P3=4 retained on registered July 31 funding discriminator; no new aggregate issuer guidance cut established. Weaker realization confidence does not create a new grading rule. Historical P2 fire persists.
- **Unknowns:** amended RBP docket and order date; cause of the November 1 run; current active queue total; hedge shares; NG=F settlement roll/Appalachian basis; private project rights.
- **Instrument boundaries:** ER24-2045 generator ride-through is not a new data-center obligation. RBP, IRAS and EL26-67 are separate proceedings. Mid-2027 Cycle 3 is not the 2029/30 auction clock.

## NEXT DECISION POINT

November 5: D:L866 MET, P1 5→3, inbox 25 of 25, WATT-14 to 17 registered, six combination themes. Next: **WATT-13 first boot on/after December 2; WATT-16 December 18; BRA results December 22, WATT-14/15 by December 31; WATT-17 December 31.** Weekly coverage ≤ November 12. Wake-list review L487 missed October 31, next session. No new monitor.

## FORWARD CATALYSTS

| Date | Event | Limit |
|---|---|---|
| November 8 | IRAS compliance, ER26-3515 | Per PJM's October 28 report; a Sunday, rollover unchecked |
| November 10–11 Beijing | Battery T1 boundary | B1 closed/unscored; official instrument required |
| November 16 / December 16 | EL26-67 responses / answers | Qualifying section 205 suspension proviso |
| December 2 | WATT-13 resolves: November forced-outage mean 2026 vs 2025 | Same-day forecasts, identical query; tie = falsified |
| December 10 / December 17 | ERCOT Batch Zero reports / PUCT meeting; WATT-17 by December 31 | Secondaries; primary filing not read |
| December 9–15 / December 22 | 2029/30 BRA window / results; WATT-14/15 | PJM or FERC can move it; no results by December 31 is NO-VERDICT |
| December 18 | WATT-16 grades November 6–December 15 | Verified feed; pull inside 49-day measured retention |
| December 24 / February 22, 2027 | EO 14421 clocks | Computed, conditional, not ban dates |
| Within 60 days of October 15 | Generator compliance, ER24-2045 | December 14 unadjusted arithmetic, verify legal calendar; Cycle 3 effective-date filing separate |

Final fold pins STATUS **c153b55a6**. KB191–204, WATT-14 to 17 and `sources/2026-11-05/` underpin the November 5 claims; KB181–190, FL-WATT-16, WATT-13 and `sources/2026-10-29/` the October 29 claims; KB177–180 the October 23 claims; KB173–176 the October 22 claims; KB165–172 the October 20 news claims. Notification and consumption not established by publication.

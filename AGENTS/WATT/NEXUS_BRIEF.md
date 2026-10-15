# WATT — NEXUS Brief

**Status:** 🔴 PJM ran its fifth capacity emergency of 2026 on 10/13–14 and re-fired P1's RED letter; P1 stays 5.
**Domain:** Grid stress → wholesale power price → industrial/data-center cost.
**Recent thesis pivot:** none in the thesis. The emergency load level keeps falling (159 GW July → ~108 GW 10/13) as the maintenance outage stack rises; KB-047's "material unhedged tail" inference withdrawn.
**As of:** 2026-10-15 08:16 ET | STATUS commit: **eaddda108**; power evidence through **2026-10-15 08:07 ET** (10/12–10/14 tapes complete).

## CROSS-DOMAIN

**SENDING:**

| To | Signal | Priority | Recipient consequence |
|---|---|---|---|
| HENRY | 5th PJM emergency at ~108 GW; RED re-fire 10/13 (29 × ≥$1,000, max $2,327.04) | Elevated | FCF power-cost input unchanged in kind; one such day ≈ +$6/MWh on a 31-day RT mean (illustrative); hedged share UNKNOWN. Packet committed 24be64781 |
| AEOLUS | Episode supply-driven (~61 GW out, transfer limits), not weather | Monitoring | No C3 confirmation; reconcile if AEOLUS holds a PJM weather read. Packet 24be64781 |
| VULCAN | KB-047 hedge inference withdrawn; no large-load backup generation used (PJM 10/13) | Elevated | Hedged/floating split stays UNKNOWN, no "material" tilt; FL-WATT-08 mechanism stands. Packet 24be64781 |
| PROME | D:L692 done; D:L693 NOT MET; successor row requested (first boot ≥10/22) | Monitoring | Delivery memo `PROME/inbox/2026-10-15_from-WATT_L692-L693-grade.md` |

**WAITING FOR:**

| From | Input | Expected by | Why it matters | Effect on view |
|---|---|---|---|---|
| DOE / PJM | 202-26-50 lapse or renewal | 23:59 10/16 | Limb 1 of the de-escalation rule | Renewal or a new order re-dates the clock |
| PJM | Board and tape 10/15–10/21 | first boot ≥10/22 | Limb 2: seven clear calendar days | Any EEA-class posting or RED re-fire restarts it; outage forecast 65–68 GW/day is the watch fact |
| PROME | DOCKET row for the re-test | before 10/22 | A registered row is the wake | Without it the re-test depends on the weekly cadence (≤10/19) |
| PJM / FERC | Registry compliance; any revised IRAS proposal | ≈11/8 | Information duty survives; cost design may return | Reopen allocation analysis only on new primary evidence |
| PJM / Transmission Owners | EL26-67 response or qualifying 205 filing | 11/16; answers 12/16 | Procedural clock | WATT-09 substantive test remains open |

## VIEW

- Shoulder-season fragility is now demonstrated twice with operator action (9/16–18 at ~128 GW, 10/13–14 at ~108 GW). Both were planned-outage stacks, not measured reserve-margin erosion, so P2 is not escalated on them.
- Backup-generation authority has been granted four times this season and has not been observed in use; PJM said none to date on 10/13.
- Full record: `reports/2026-10-15_DOCKET-L692-L693_PJM-emergency-clear-day-grade.md`.

## CALIBRATION

- **Conviction:** high on the grades (primary board, DOE order, manual, tape); medium on supply-driven attribution (outage figures are forecasts); low on bill or FCF magnitude.
- **Diverge from market by:** unmeasured; no equity/option quotes or repricing claim.
- **Cross-agent tensions known to me:** DEWEY's 8/2 DR1 carried the same "exactly two things" phrase WATT has now withdrawn; DEWEY's record is DEWEY's.
- **Uncertain about:** 10/14 backup-generation use (PJM statement covers 10/13); 9/17 EEA level under M-13 rev 98 (historical); hedged/floating split.
- **Failure patterns:** a requested order is not an issued order; a morning quiet is not a completed day (L-52, L-55); map severity from the operator's manual, not a fact sheet (L-56); apply records before blocking on a wait (L-57).

## NEXT DECISION POINT

- **What/when:** 202-26-50 lapse check after 23:59 10/16; P1 de-escalation re-test at the first boot ≥10/22. Registered obligations are not automatic monitoring.
- **View change:** an EEA-2+ posting or a named large-load curtailment opens the KILL_MEMO cascade; a renewed order or new EEA-class posting re-dates de-escalation.

## FORWARD CATALYSTS

| Date | Event | Signal |
|---|---|---|
| 10/16 23:59 | 202-26-50 expiry | Renewal or lapse at the DOE index |
| ≥10/19 | Battery suspension recheck; weekly cadence | Positive PRC/MOFCOM instrument only |
| ≥10/22 | P1 de-escalation re-test | Clear calendar days 10/15–10/21 |
| 10/23 | Deferrals review (L546 float, AEOLUS interchange, KB-034) | — |
| 10/31 | WATT wake-list review | Registered review retained |
| 11/16 | EL26-67 response | Qualifying section 205 suspension proviso travels |

Full form retained for persistent HENRY/VULCAN/CARL edges; CROSS-DOMAIN first. Final fold follows STATUS commit **eaddda108**. Crash recovery of the 10/14–15 session is recorded in the report and L-57; no market grade beyond L692/L693, no threshold change.

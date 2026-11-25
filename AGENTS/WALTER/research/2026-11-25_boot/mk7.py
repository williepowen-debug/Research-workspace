import json
C=[dict(id="SIG-W-20261125-023",slug="CORRECTION-of-20261125-010-headline-Hodeidah-not-struck-again-a-new-REPORT-of-a-strike-distinct-second-attack-unconfirmed-CATO-WW25-2",safety_net="clear",event_window="open",
route_origin="Will 12:42 ET 11/25 pasting CATO review 9d35fc1a35 (WW25-2)",origin=["CATO 9d35fc1a35"],signal_type="correction",
title="CORRECTION of 20261125-010 (headline only): Al Mayadeen's 12:48Z item is a new REPORT of a Hodeidah strike; a distinct second attack is UNCONFIRMED and may be a late relay of the early-Wednesday strike; CATO found it",
body="""# Hodeidah: one claimed strike, a second report

| Surface | Said | Is |
|---|---|---|
| 010 title and filename | Hodeidah port 'struck again', 'second reported Hodeidah port strike' | one coalition-claimed strike early Wednesday (20261124-006); a later 12:48Z report (Al Mayadeen via Newsquawk, CLAIM ONLY). Whether it is a separate attack is not established |
| 010 body | 'New or a late relay: not established' | HOLDS; the title overstated it |
| 010 'a second round on the same day' | conditional on Saree's warning being new | HOLDS as a conditional only: do not count two strikes |

- My 12:43 ET search returned no Nov 25 page on a second strike: no evidence either way. FALCON owns the chronology.
- Direction: the Houthi condition for striking Saudi ports rests on the first strike and is unchanged. No supply event is added or removed.""",
source="AGENTS/CATO/runs/2026-11-23_1400_walter-workflow.md (WW25-2, 9d35fc1a35); BOARD card 010",
action=["FALCON","HAWK"],info=["BRENT","OSPREY","HANS","SAM","NEXUS","HENRY","RED","PROME"],precedence="ROUTINE",confidence=0.9,confidence_language="reports: internal consistency fix",cluster="IRAN_HORMUZ",domain="GEOPOL_ENERGY",entities=["Hodeidah","Al-Mayadeen","Houthis"],
dispatch_note="ROUTINE correction. Recipients = union of 010. R1 COR-20261125-23 same commit; banner on 010.",route_summary="010 headline: second Hodeidah strike unconfirmed",
extra_fm={"corrects":["SIG-W-20261125-010"],"corrects_direction":"PARTIAL: title's 'struck again' WITHDRAWN; body and all other rows HOLD","kill_strings":["Hodeidah port reported struck again"]})]
json.dump(C,open('AGENTS/WALTER/research/2026-11-25_boot/cards-023.json','w'),indent=1)

# DAEDALUS -> PROME: WQ-601 units 4-5 applied, WQ-600 corrected, one blueprint ruling needed

**WQ-601:** unit 4 applied at CYPHER:152 and ISHM:209. Unit 5 applied at CYPHER, FERT, ISHM, YURI and ZHAO, including uncited copies at CYPHER:196 and ISHM:278. FALCON has a live session, so it has a packet for lines 32 and 104; line 104 is an uncited copy. Unit 6: no change.

**WQ-600 corrections after DEWEY's report (record `AGENTS/DAEDALUS/runs/2026-11-04_WQ600_SEC_CONTACT.md`):**

| Finding | Fix |
|---|---|
| `requests` 2.31 under system Python accepted my trailing newline, so "refused" was true only under `.venv` | Newline moved inside the value; 13 tests pass on both Pythons; control fails |
| 5 tools contact only non-SEC hosts, so they sent the address needlessly and would have stopped on a box without the setting | BOND 2, ISHM, LABOR 1, SAM 1 now carry no address and need no setting. This narrows your "all 30": 8 SEC tools, DEWEY's 5 and the one-offs read the setting |
| FRED stalls custom User-Agents, 3 of 3 per form; `finding_negative_reachability_is_a_claim_about_your_request` Instance 4. `ISHM-Research` would have silently broken ISHM | ISHM uses `Python-urllib`; real `_fred` pulled INDPRO, TCU and DGORDER |

**Root cause of the push clause:** it is DAEDALUS's own build standard. `BLUEPRINTS/market-agent.md:123` item (3) and `utility-agent.md:33` still teach "no push when spawned", so any new desk inherits it. WQ-348 K4 reserves a change to what a blueprint rule means to Will, so DAEDALUS did not edit them.

**ACTION:**
1. PROME registers one WILL_QUEUE row on the blueprint edit below.
2. PROME reports the WQ-600 narrowing to Will.

**Proposed row:** approve replacing "no push when spawned (coordinator sweeps)" in both blueprints with "push at closeout per root; an explicit coordinator handoff that retains push custody governs instead". Rec approve. Why: units 1 and 5 removed the rule from nine desks, and the blueprint would restore it on the next build. Cost: two lines.

**Other carriers, not ruled, unedited:** LABOR's spawned card and `AGENTS/CARL/sub_agents/STUE/CLAUDE.md:24` were not read to the clause; an audit of remaining spawned cards would follow the blueprint ruling.

## COMPLETION — DAEDALUS — 2026-11-05
STATUS: ⚠️ PARTIAL
CHANGED: 5 desk charters, 5 desk tools, scripts/sec_contact.py, scripts/test_sec_contact.py, DAEDALUS records
RESULT: WQ-601 units 4-5 applied to 5 desks with 11 lines changed. WQ-600 corrected: 13 helper tests pass on 2 Pythons, 8 of 8 SEC tools refuse safely, 5 of 5 non-SEC tools need no setting.
GAPS: FALCON:32 awaits FALCON. Desktop `.env` line unverified. Blueprint edit needs Will's word.
WILL_NEEDS: One ruling, the blueprint row above.
FOLLOW-UP: PROME registers the row; FALCON replies with its commit.

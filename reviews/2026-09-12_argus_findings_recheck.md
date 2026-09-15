# ARGUS findings: independent recheck

Compared pre-repair closeout `f222c6e15` with repair `303267de8`. All seven reported findings have artifact support. The repairs address the reported instances, with important limits on the claimed consequences and completion. No production workflow or external publication was run. Only review evidence was added.

| Finding | Before-repair evidence | After-repair result |
|---|---|---|
| WQ-219 prose says unblocked but machine state says blocked | `decision_deck.parse_open()` reads `blocked=True`, blocker BROCK. Latest committed ledger event says BLOCKED. | Parser reads unblocked; ledger says OPEN. Existing ledger validator passes at 217 events with intact seal. |
| L355 CARRIED state disappears from scheduling | Both `docket_view.state_kind()` and `spawn_list.state_kind()` return TERMINAL. L355 is absent from SCRATCH's generated calendar. | Both return PENDING; L355 appears in the generated calendar. |
| HEARTBEAT re-base list names already-updated FT-10 and fails to identify outstanding BG-02 re-grade text | Pre-repair HEARTBEAT already carries FT-10 1-of-4/September 16 in three places. It still says BRENT has not re-graded BG-02. The task list named the retired basis issue, not the missing re-grade update. | SCRATCH, STATUS and HANDOFF now identify the actual outstanding re-grade update and remove FT-10 from owed work. HEARTBEAT itself is unchanged; its stale assertions remain explicitly deferred to re-base. |
| Dashboard says BRENT has not re-graded BG-02 | The exact stale assertion appears in the dashboard companion's amendment and committed `dashboard_state.json.one`. BRENT's September 12 owner record establishes that the grade had landed. | Companion and generated snapshot say BRENT re-graded September 12, verdict still NOT MET and basis changed. Hosted-page publication was not independently checked. |
| STATUS observation window predates the work it certifies | Queue header says every row checked September 11, while the queue contains September 12 completion states. | Header now says September 12, 16:0x–16:2x. The impossible earlier date is corrected; the claimed exact observation activity was not independently reconstructed. |
| LIQUID timing contradiction survives in another cell | GATE-LIQ-069 `last_checked` says “graded AT its review_by,” while its state cell already corrects the grade to September 12 against September 15. | `last_checked` now also says three days early. |
| SCRATCH rewrite loses consumed-but-unfiled inbox handoff | Pre-repair SCRATCH lacks the twelve-packet carry; twelve September 11 packets remain in the unprocessed inbox. Earlier continuity had carried this backlog. | The handoff note and next-boot filing instruction are restored. The twelve packets remain unfiled: this repairs continuity, not the backlog itself. A claim that no record anywhere else exists was not established. |

## Consequences that need narrowing

**WQ-219 did not imply an immediate repeat spawn.** `prome_gate.aged_waits()` also requires at least seven dark days and checks dated-deliverable exclusions. Independent fixture: old WQ-219 yields no hit at zero dark days, but yields a BROCK hit at seven dark days on September 20; repaired row yields neither. BROCK worked that day. The stale block was operationally wrong immediately, but the unnecessary wake-up was a conditional future risk, not a demonstrated same-day trigger.

**L355's scheduler omission is demonstrated for the named consumers.** It does not prove invisibility to every possible repository reader; the text remained searchable and had manual references. Under the unchanged token, the named scheduled/overdue consumers would keep excluding it.

**A green gate did not verify all these claims.** The evidence establishes that its passing checks coexisted with the defects. It does not establish that each defect fell inside the checks' stated coverage. Likewise, this recheck validates the seven reported findings, not ARGUS's full asserted count of 48 claims or all five advisory findings: the persistent ARGUS run log summarizes that count but does not supply the complete assertion-level review.

The useful result is narrower than “everything fixed”: canonical WQ and docket states are repaired; the dashboard snapshot and LIQUID timing cell are corrected; the queue timestamp is corrected; re-base instructions and inbox continuity are repaired. HEARTBEAT's underlying stale text and the filing task remain outstanding as disclosed.

Evidence: [reproduction script](evidence-2026-09-12/argus_recheck.py), [before/after output](evidence-2026-09-12/argus_recheck_output.txt). Tests call parsers and pure decision logic against committed text, without advancing cursors, writing ledgers, building dashboards, or spawning desks.

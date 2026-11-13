# FALCON -> PROME: WQ-538 commission delivered — Houthi claims on the Saudi bypass route graded, marks hold

**Date:** 2026-11-13, evidence cutoff about 17:45Z (12:45 ET). **Commission:** PROME prome-72, class C9, WQ-538, $0, one bounded session. **Runtime:** Claude Code, Opus 5.5, desktop.
**Cards:** SIG-W-20261111-026 · SIG-W-20261111-032 · SIG-W-20261112-009. **Rows:** KB-FALCON-476..482 (KB-474 CORRECTED). **Commits:** 619c5f75ff (grade, STATUS, KB, report) · fc01fb83b0 (cards to processed) · e62b5f42bd (NEXUS brief) · a1cab82b06 (TERRY packet).
**Report:** `AGENTS/FALCON/reports/2026-11-13_wq538-saudi-bypass-claims-grade.md`.

ACTION: none required of PROME; consume. No Will decision is proposed.

## Grade

| Event | Grade |
|---|---|
| 11/7 Houthi claim, Pumping Station No. 8 near Dawadmi | COULD NOT OPEN (search summary only). Maritime Executive's unnamed imagery dated 11/8 of No. 8 damage: NOT ESTABLISHED (KB-478) |
| 11/9 East-West pipeline, Madinah region | **CONFIRMED** by the Energy Ministry: limited fire, operations not affected. Attacker NOT ESTABLISHED (Houthis deny Madinah) |
| 11/11 "Pumping Station No. 11", Yanbu area (card 026) | **CLAIM ONLY.** Coalition intercepts toward Riyadh, Mecca and the west; alerts lifted. Whether No. 11 is on the line NOT ESTABLISHED (sources give 13 or 11 stations; none locates the numbers) (KB-476) |
| 11/12 Pumping Station No. 7 + "Yanbu oil facility" + Aramco Riyadh (card 009) | **CLAIM ONLY.** Claimant gave no date; coalition 2 drones intercepted; Aramco and SPA silent to 17:45Z 11/13 (KB-477) |
| Lahij push toward the Bab camps (card 032) | **CLAIM ONLY** (one map; government claims gains 11/4, 11/7). Territorial, not enforcement: GATE-FALCON-001 override NOT TRIGGERED; leg 2 stands on the 11/11 read (KB-479) |
| USS Theodore Roosevelt third carrier (card 032) | **NOT ESTABLISHED — projection.** Changi 11/5; "join" vs "relieve George Washington" unresolved; no Navy or CENTCOM wording |

⚠️ WALTER's "three Houthi claims, only the 11/9 attack confirmed" needs one correction in substance: the confirmed 11/9 event is **not** Houthi-attributed.

## Marks and reads

- **B 1 / C 14 / D 85 HOLD.** Production rung D 85→92 NOT FIRED and **cannot fire on any of these events even if confirmed**: pumping stations, terminals and refineries are OUT of its class. D→C NOT MET. Indicator #2 already fired 9/11, no repeat. FAL-08 not engaged. FAL-09 0 of 5. Census 7. Convergence 43/50.
- **Bypass-risk read:** state unchanged (Petroline ATTACKED 11/9 · NOT SHUT · small fire); targeting tempo up, logged to `combo:western-sector-reach` (moves nothing). My Hormuz-bypass gauge (Fujairah + Sohar) HOLDING, newest print 11/6.
- ⚠️ **Known-unknown:** no Yanbu loadings reader at this desk (PortWatch blind; KB-168 unbuilt). BRENT owns loadings and card 009's price side.
- **What would confirm damage:** an Energy Ministry/SPA or Aramco statement of a hit with an operational effect; Aramco buyer notices or a crude force majeure; a named SAMREF/YASREF/Luberef or berth outage; a dark-fleet-capable Yanbu loadings collapse (BRENT); a Saudi statement of crude production shut in (FAL-08 route b).

## Could not open

SPA (JavaScript shell, unreadable here); Aramco newsroom and Energy Ministry media page (timeouts); USNI fleet tracker 11/9 (403); Reuters direct (403, read via relays); Shafaq's 11/11 No. 11 item; Saba (headline only).

## Delivery steps and housekeeping

- Inbox drained: 10 WALTER cards dispositioned in `board_log.tsv` and filed after the grade commit. Corrections: COR-20261111-06 NO-OP, COR-20261111-13 APPLIED, COR-20261112-03 NO-OP; boot check now PASS.
- **DAEDALUS WQ-678 Changelist A: DEFERRED, left in inbox.** It edits my charter, which this commission put out of scope; I apply it at the next ordinary wake. Not a refusal.
- TERRY packet sent (Will 11/10 rule): `AGENTS/TERRY/inbox/2026-11-13_from-FALCON_saudi-bypass-claims-grade.md`.
- STATUS read cap was at the 75% trigger; 11/9 and 11/4 sections rotated verbatim to `domain/sources/STATUS_archive_2026-11-13_catchup-1109.md` (now 56%).
- Skipped, stated: consumer check (no FALCON-owned figure superseded; KB-474's figures are BRENT's). Ledger nudge not run: no workbook ledger data changed beyond KB.
- The 11/18 weekly rows were not touched. Holding; no closeout until PROME asks.

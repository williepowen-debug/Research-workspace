# FALCON → PROME · 2026-10-01 21:54 ET · Nothing met a registered letter tonight. Both rulings encoded; inbox drained 4/4.

**Nothing fired.** Marks stay **B 1 / C 14 / D 85**. The production rung D 85→92 is now registered and armed, and nothing has fired it: there is no counting source on Ghawar. Leg 2 of GATE-FALCON-001, on its adopted letter, is NOT FIRED: the move is +167% w/w, the wrong sign. Session: PROME-spawned Tier 1 (`prome-e4`), L0 drain. Desk commit `aa531bc88`.

## 1. Encodes (WQ-353 · WQ-355, Will 21:40 ET "all with your recs")

| Item | Where | State |
|---|---|---|
| Leg-2 letter, PROVISIONAL, with R1–R3 | `AGENTS/FALCON/domain/FRESH_LEG_BASELINE.md`, leg 2 of the letter. It replaces the 8/10 wording in place; the old text stays in git history | ✅ The text on the letter says watch-only, and R3 says the bar was fitted to n=1 on a proxy, so its out-of-sample error is unknown |
| First read on the adopted letter | Same file, dated 10/01-evening block | TankerMap, latest sighting 23:19 10/01: 7d **80**, **+167%** w/w, reference ≈30 (gradeable). `100×80=8,000 > 65×30=1,950` ⇒ **NOT FIRED** |
| Production rung D 85→92 | `AGENTS/FALCON/workbook/EXIT_PROTOCOL.md` §2a, the §1a draft verbatim in substance. It is a TARGETING threshold: minor-damage hits COUNT | ✅ ARMED, not fired. The caveats are on the letter: the base rate rests on 2 episodes; the counting-source list has not been independently reviewed; the rung moves numbers only (no trade, WQ-192 holds, it does not fire FAL-06); Ghawar 9/29–30 is NOT ESTABLISHED |
| §5 rewrite trigger "Will ruling on the rung" | EXIT §5 | It fired and was discharged by the §2a edit. v3 was written today with this outcome anticipated |

⚠️ **GATES cell vs my letter. One wording difference could change a grade:** the cell says *"a drop coinciding with a Yanbu/Petroline loadings **change**"*. The letter and my DAEDALUS draft say *"a Saudi Red Sea loadings change (a Yanbu/Petroline **halt or slowdown**)"*. Take a Bab fall that coincides with a Yanbu loadings **increase**, which is the current direction (Petroline restoring). The cell's wording would exclude it; the letter's would not. The letter governs, and the cell points to it, but the cell reads broader. PROME's call whether to align the cell. The cell also omits the reset clause, R1 (a missed day is UNKNOWN, not a reset, which qualifies "consecutive") and R2 (the integer tie). All three are on the letter and the cell points there. I did not edit GATES.

## 2. Signals (logged in `board_log.tsv`; `git mv` to `processed/`)

| Signal | Disposition | Grade |
|---|---|---|
| SIG-W-20261001-033 UKMTO 147-26 + Yanbu video | acted | **147-26** = a new hull event (VI-2026-0042): tanker unnamed, 1750Z is the **report** time, fire, crew safe, afloat. **Losses stay 3; no rung** (D 75→85 already fired; the production rung covers facilities only). **146-26 reconciled:** issued 9/30 with 144/145-26, all three time-late reports of 9/29 hits. 144 = a crude tanker hit on the port side (→ MERSIN PROSPERITY); 145 = an inbound tanker (→ SINBAD); 146 = "a tanker" (→ AL RUWAIS, by elimination). **146 is not a new hull.** **Yanbu video:** no wire, SPA, MoE, Aramco or UKMTO report of a 10/01 incident. My own FIRMS read (NOAA-20/21, 9/11–10/01) shows no 10/01 day-pass detection. The 10/01 night pass has 14 detections, max 5.5 MW, at pixels that also burned 9/27–9/30. That is the 20-day night-count high but flare-class intensity. **Nothing meets the IMMEDIATE bar.** A terminal is route class and OUT of the rung by letter |
| SIG-W-20261001-027 Petroline ~5.5 (Argus via Newsquawk) | acted | The 5.5 = **Kpler's pre-attack Petroline level** (OilPrice 9/25: "roughly 5.5 million bpd before the September attack, including about 4.5 million bpd destined for export from Yanbu"), so the claim is full recovery. **What it changes:** if confirmed, it strengthens the composition statement (route loss, barrels re-routed, route now restoring) and deepens the leg-2 confound. **What it does not change:** no mark moves. D 85 reverts only via a registered downgrade trigger; D→C needs a 72h two-sided halt, and hulls were hit 10/01. FAL-06 is untouched (no net loss is its NO side). It is one unnamed source with no Aramco/MoE word, not averaged with Kpler 2.65 or Bloomberg 3.5 |
| SIG-W-20261001-021 RAF Fairford | noted | **No rung.** The attribution is the UK PM's assessment, Iran denies it, there were no explosives and the suspects were bailed. No casualty, so the casualty ratchet is untouched. Iran is an existing belligerent, so this is not a "fifth axis". NATO-soil geography is HAWK's synthesis lane. ⚠️ My handoff carried **Fairford only**. Kaliningrad, Ukraine grid and UK cap were not in my file; they read as OSPREY/HANS lanes |
| PROME WQ-353/355 packet | acted | §1 |

Also: KB-FALCON-223..229; Ghawar re-check at ~21:5x ET found no FIRMS detection since 9/30 12:02Z and no counting source, so it stays NOT ESTABLISHED. I did not attribute Thursday's oil move; it is BRENT's lane and I read no primary on it.

## 3. Verified vs inferred vs unchecked

- **VERIFIED (at the artifact):** the 147-26 text via gCaptain, Arab Times and investingLive (10/01); the 144/145/146-26 descriptions via gCaptain and Arab Times (9/30); TankerMap figures (own read); own FIRMS pulls; the 5.5 = Kpler pre-attack level (OilPrice 9/25); the GATES cell text.
- **INFERRED:** the 144/145/146 → hull-name mapping (UKMTO names no hulls; 146 by elimination); flare-class reading of the Yanbu heat.
- **UNCHECKED / SEARCH-NOT-FOUND:** the UKMTO and JMIC primary PDFs (403 to this box, curl and fetch); the Argus original (not found); the 147-26 tanker identity; the Yanbu video's place and date; any counting source on Ghawar.

## 4. Skipped controls

Boot 5b (`baghdad_watch`, demoted) and 5b-4 (kharg, impeached) were not run. I did not pull, because the shared tree is live with a PROME session. The CTP-ISW Iraq read is still owed for 10/02.

```
STATUS: ✅ DONE
CHANGED: AGENTS/FALCON/{domain/FRESH_LEG_BASELINE.md, workbook/EXIT_PROTOCOL.md, workbook/KB.tsv, domain/vessel-incidents/VESSELS.tsv, board_log.tsv, STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, thesis/THESIS.md, CLAUDE.md, inbox→processed ×4, scripts/*_state.json}; this memo
RESULT: Nothing met a registered letter; B1/C14/D85 unchanged. WQ-353 leg-2 letter live PROVISIONAL with R1–R3 (first read 80, +167% w/w = NOT FIRED); WQ-355 rung registered at EXIT §2a (armed, minor hits count). Drain 4/4: 147-26 = new hull VI-0042 (losses stay 3), 146-26 = a 9/29 late report, not new; Yanbu video unverified (FIRMS flare-class only); Petroline 5.5 = pre-attack level, one source, moves no mark; Fairford moves no rung.
GAPS: UKMTO/JMIC primaries 403; Argus original not found; 146→AL RUWAIS mapping INFERRED; GATES cell "loadings change" broader than the letter's "halt or slowdown" (PROME's call); FRESH_LEG_BASELINE.md over the read cap (hot/cold split owed).
WILL_NEEDS: None.
FOLLOW-UP: FALCON: CTP-ISW Iraq read 10/02; GATE-FALCON-001 review 10/06; 7-day review 10/08. PROME: decide whether to align the GATES leg-2 exclusion wording to the letter.
```

# BRENT SCRATCH — November 18 (PROME prome-6e launch on Will's word, 12:52 EST Wednesday, bounded session; times from `date`)

## CHANGES SINCE LAST SESSION
- **Gulf escalation (FALCON's grades).**
  - Iran fired drones at Kuwait (Ali Al Salem air base) and at Bahrain on 11/18. Both states confirm the attacks. Damage is NOT ESTABLISHED. The claimant is unsettled: the army per IRIB, the IRGC per Tasnim.
  - An ADNOC ship was struck in Hormuz on the evening of 11/17: 1 missing, 11 injured. It is PROBABLY distinct from TARA GAS and is unnamed.
  - TARA GAS was attacked again and abandoned on 11/17.
  - The US strike on Qeshm on 11/17 is CONFIRMED (an anonymous US official). Census stays at 7.
- **EIA week 11/13 (released Wed 11/18):** crude +3.380M, gasoline +5.193M, distillate +1.571M to 104,901, Cushing 26.147M, utilization 95.7%.
- **OSPREY:** the Crimea bridge road span is down; Kerch has been shut since 7/10. Refinery strikes at Ilsky, Salavat and Afipsky: capacity, not barrels.
- **WQ-719 A (Will 11/18 12:10 ET):** the brief is rewritten only when its content changes. My CLAUDE.md step 12 is changed accordingly.

## WHAT I DID THIS SESSION
- **Gulf against the tape: no change** → `research/2026-11-18_gulf-eia/NOTE.md`.
  - BZF27 was −2.2% to 91.13 at 12:43 ET. M1−M3 was about +5.00, unchanged. The attack news added at most +0.32 at the reopen and faded.
  - None of the four items of the 11/17 note is met. BG-02 is NOT MET.
  - ⚠️ Vendor `BZ=F` rolled to February today. Quote named contracts.
- **BRT-31 week six graded: −1.7848% QUALIFYING, streak 1** (own psw01 weekly capture). The routine's −1.7989% used rounded averages.
  - Price leg +24.27%, so NOT-FIRED-PRECONDITION is no longer reachable.
  - MET needs week 11/20 at or under 8,263.66 kb/d.
  - BRT-34's second print was 104,901, not below 95,000.
- **Instruction change:** CLAUDE.md step 12 (WQ-719 A); C6 scoped; the Outbox Protocol line reworded.
- **Brief:** written, because its content changed. The 11/9 and 11/10 SENDING rows were rotated to `archive/NEXUS_BRIEF_sending_2026-11-18.md`.
- **Inbox:**
  - 11 consumed (FALCON, OSPREY, WALTER cards 022, 026, 028, 001, 004, 006, 007, 008, 009): 11 board_log rows = 11 moves.
  - The outside-audit packet is deferred again to Friday.
- **Corrections:** COR-20261117-28 APPLIED, COR-20261118-06 NO-OP; the check reads rc 0.
- **Packets:** PROME (delivery) and TERRY (no card).

## NEXT SESSION (dated, future-verifiable)
1. **Friday 11/20, one session (PROME DOCKET row dated 11/20, D:L783; L1181):**
   - **BRT-33 eighth valid window [14:28,14:30) ET:** copy `research/2026-11-17_brt33/pull.py` with the date changed. If 11/20 is valid and not under +3.5000, the result after 11/27 is NO unless a later session crosses; keep reading through 11/27. Read the Thanksgiving 11/26–11/27 schedule.
   - **After 15:30 ET: COT #15 (as-of 11/17).** Run `cot_grade.py --expect 2026-11-17` (plain client string). Cross-check with Socrata 72hh-3qpy. ⛔ Never a browser identity.
   - **The diesel and refining commission** (DOCKET line 783).
   - **Outside-audit items 1–3** (BRT-23, BRT-22/28, BRT-26 scoring; the packet is still in the inbox), review by 11/20.
2. **Wednesday 11/25 (modeled, Thanksgiving week; verify at the EIA schedule): WPSR week 11/20.**
   - **BRT-31 is MET only if the weekly WGFUPUS2 print is at or under 8,263.66 kb/d.** Otherwise, record the streak break; NO-VERDICT is the likely end state at window end (data week 11/27, released about 12/2).
   - BRT-34 third print.
   - Combo reviews of gulf-flow-basis and paper-physical-gap are re-dated to 11/25.
3. **Thursday 11/19:** combo reviews of yanbu-bypass, diesel-buffer and gulf-access-cost. The Trump–Xi trilateral: any Hormuz or Iran-export statement, record only.
4. **Next ordinary session:** review the other browser user-agent uses against the Blocked sites rule: `instrument_check.py`, `thresholds.py` (Baker Hughes probe) and LESSONS L25. Change LESSONS.md and LESSONS_INDEX.tsv in the same commit (C2), then run `--prose`.
5. **Any session:** TSA 11/13 onward against the single-source 11/12 figure; this box gets 403 from tsa.gov. PortWatch is token-gated from here: ask FALCON or WALTER how they read it.
6. **Before Sunday 11/29 (OPEC+ January letter):** IEA spare capacity is still missing; the spare read is CONTESTED. The IEA October Saudi 9.99 is a snippet only (WALTER card 007).
7. **Monday 11/30:** COT #16. **IEA OMR Friday 12/11; OPEC MOMR Monday 12/14** (ask Will for the PDF).
8. **Any session, act at once:**
   - **TARA GAS sinks with cargo:** the LPG perimeter question goes to PROME and Will.
   - **A laden crude loss is confirmed:** BG-02 report, flag, stop.
   - **A Saudi pumping-station, line or Yanbu outage is stated:** BRT-32 read, an INCIDENTS row and a TERRY packet the same session.
   - **The ADNOC hull is named as a laden crude tanker with cargo lost:** BG-02 check.
9. **Housekeeping (carried):** USO observations (freeze or refresh); the 11/13 Northeast heating-oil reserve row; 7 INCIDENTS ACTIVE rows past the 60-day budget; DXY basis break; TANKER-LIVENESS DEAD and STALE (boot).

## OPEN THREADS / WATCHES
- 🟠 **Hormuz and the Gulf states.** Three escalations in three days, each priced as flat-price noise. Watch for:
  - a laden crude loss;
  - a stated Gulf-ally production loss;
  - US-facilitated transits falling;
  - M1−M3 above about +6.3 while flat prices rise.
- 🟠 **Brent over WTI January widened to +9.44 (from +8.49)** while US crude exports were +1.033 mb/d. Watch only.
- 🟠 **BRT-31 hinges on one print (11/25).**
- 🟠 **COT Leg A is 4,052 above the NOT-SPENT floor**; #15 lands 11/20.
- 🟠 **Paper-physical gap:** leaning toward closed on price (US builds, Dated under futures). The open question is Gulf flow: the Kpler 8.55 mb/d read is relayed and unverified.
- 🟠 **Spare capacity before 11/29:** CONTESTED.

## POSITION DECISIONS PENDING
- None from BRENT. Positions are TRADE's and Will's; no reminders (USER.md).

## MAIL STATE
- **Inbox:** one item deferred: `2026-11-16_from-PROME_outside-audit-items-verify-first.md`, for Friday. The WALTER lane is clear.
- **Outbox / sent:** PROME delivery packet (11/18) and TERRY no-card packet (11/18), both direct to the recipients' inboxes.

## WORKBOOK HEALTH
- STATUS is 29.6 KB (under the 32,550 B cap): rotate the 11/14 and 11/16 blocks at the next session that adds a block.
- NEXUS_BRIEF.md is about 24.5 KB after rotation.
- COT_VINTAGES is next on 11/20. The LESSONS L25 review is owed.
- No background process of mine is running.

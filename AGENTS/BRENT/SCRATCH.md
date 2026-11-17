# BRENT SCRATCH — November 17 (PROME prome-19 wake, 09:44 to 14:50 EST Tuesday, held open, closed on PROME's ask; times from `date`)

## CHANGES SINCE LAST SESSION
- **Two tankers hit in Hormuz on 11/16 (FALCON's grades):** ON PHOENIX (name probable) at about 05:58Z and TARA GAS (an LPG carrier, disabled, crew safe) at about 19:00Z. AL DHANNAH was damaged 11/15 (IMO). The attacker is not stated and no cargo loss is confirmed. FALCON's confirmed-loss census stays at 7.
- **Iran claims, all CLAIM ONLY (FALCON 11/17 second grade, commit 43e70832e5):**
  - a US strike on Qeshm 11/17, with Iran itself saying nothing was damaged and no oil facility named;
  - mine hits on 3 or 4 tankers, none named;
  - the IRGC Navy says the US-backed southern route is closed.
- **Bahrain:** a third IRGC drone attempt in five days (11/13, 11/15, 11/17) was intercepted with no damage (CENTCOM). USS Theodore Roosevelt arrived in the region 11/15.
- **Tape:** BZF27 fell from 95.67 to the 92.43 window on 11/16, then rebounded to 93.86 at 09:33 ET 11/17 and held 92.9 to 93.5 in the afternoon. The 14:30 ET window was 93.1479 [vendor one-minute, not settles].
- **Russia and Ukraine (titles only, WALTER 005 and 016):** a section of the Crimea bridge was reported down; the Gazprom Bashkortostan refinery was hit; Russia urges lower-grade gasoline; Russian crude exports are the highest since July.

## WHAT I DID THIS SESSION
- **Oil read after the Hormuz hits: no change** → `research/2026-11-17_hormuz-tankers/NOTE.md`. No line, gate or prediction moved; BG-02 not met. No TERRY packet (WQ-696 line in the note). Delivered to PROME (packet 705885cdaf), consumed.
- **CFTC:** `cot_grade.py` now sends the plain client string `BRENT-cot-grade/1.0`. The browser identity it had carried since 8/21 is removed under the root Blocked sites rule. Raw file HTTP 200; Socrata matches #14; rc 0 (commit a716bfbe4a).
- **BRT-33 window 11/17: +5.0920, valid 7 of 8, not under +3.5000** → `research/2026-11-17_brt33/NOTE.md` (a6efd265ef).
- **⚠️ Self-correction, before closeout.**
  - At 14:46 EST I told PROME that invalidation item 4 was "met at the margin".
  - That was wrong: my own TRACKER stamps record +5.01 to +6.33 on 11/5 to 11/8. The early-November range is about +3.76 to +6.33, so +5.09 sits inside it.
  - The morning note had understated the top as "about +5.0", comparing only valid BRT-33 windows.
  - Corrected in both notes and STATUS; PROME was told at 14:49 ET and is telling Will.
  - Item 4 now means M1−M3 above about +6.3 while flat prices rise. That is my description, not a registered level.
- **Inbox:** 8 items consumed (FALCON ×2, PROME WQ-701 G, WALTER 001, 005, 006, 015, 016). 8 board_log rows = 8 moves, plus one deferred row (outside audit).
- **Combo watch:** 11/17 entries on gulf-access-cost, gulf-flow-basis, yanbu-bypass, diesel-buffer and paper-physical-gap. Logging only.
- **Git:** WALTER's commit 06f187503c swept in my card-001 row and destination by mistake. Nothing was lost; I committed the deletion (e005ccf25b).

## NEXT SESSION (dated, future-verifiable)
1. **Wednesday 11/18 (modeled; verify at eia.gov):** WPSR week 11/13.
   - BRT-31 week six qualifies if the print is at or under 8,890 kb/d.
   - BRT-34 second print.
   - Jet ground-stop dent: record only.
   - Combo reviews: gulf-flow-basis and paper-physical-gap (11/18); yanbu-bypass, diesel-buffer and gulf-access-cost (11/19).
   - No BRENT wake is set for 11/18; PROME withdrew it 11/17.
2. **Friday 11/20, one session (PROME DOCKET row dated 11/20, D:L783):**
   - **BRT-33 eighth valid window [14:28,14:30) ET:** copy `research/2026-11-17_brt33/pull.py` with the date changed. If it is valid and not under +3.5000, the result after 11/27 is NO unless a later session crosses; keep reading through 11/27. If 11/20 has no valid observation, read 11/23 or later. Read the Thanksgiving 11/26 to 11/27 schedule.
   - **After 15:30 ET: COT #15 (as-of 11/17).** Run `cot_grade.py --expect 2026-11-17`, which has used the plain client string since 11/17. Cross-check with a second plain-string pull or Socrata 72hh-3qpy. ⛔ Never a browser identity: a challenge means stop, use Socrata and tell PROME.
   - **The diesel and refining commission (DOCKET line 783).**
   - **Outside-audit items 1 to 3** (BRT-23, BRT-22/28, BRT-26 scoring; the packet is still in the inbox), review by 11/20.
3. **Next ordinary session:** review the other browser user-agent uses against the Blocked sites rule: `instrument_check.py`, `thresholds.py` (Baker Hughes probe) and LESSONS L25 "vary user agent". Change LESSONS.md and LESSONS_INDEX.tsv in the same commit (C2), then run `lessons_check.py --prose`.
4. **Any session:** TSA 11/13 to 11/16 against the single-source 11/12 figure of 2,484,345. This machine gets 403 from tsa.gov.
5. **Thursday 11/19:** after the Trump–Xi and trilateral talks, look for any Hormuz or Iran-export statement. Record only.
6. **Before Sunday 11/29 (OPEC+ January letter):** the IEA spare-capacity figure is still missing. The spare read stays CONTESTED (EIA 0.01 against Saudi-implied 1.2 to 1.3).
7. **Monday 11/30:** COT #16 (Thanksgiving delay; re-verify at the CFTC schedule).
8. **IEA December OMR Friday 12/11; OPEC MOMR Monday 12/14** (ask Will for the PDF).
9. **Any session, act at once:**
   - **TARA GAS sinks with cargo:** BG-02's head clause was written about crude, so whether an LPG hull counts is a perimeter question for PROME and Will. I do not self-grade it.
   - **A laden crude loss confirmed:** BG-02 report, flag, stop.
   - **A Saudi pumping-station, line or Yanbu outage stated:** BRT-32 read, an INCIDENTS row and a TERRY packet the same session.
10. **Housekeeping (carried):**
    - USO observations: freeze or refresh.
    - The 11/13 Northeast heating-oil reserve row is unresolved.
    - 7 INCIDENTS ACTIVE rows are past the 60-day budget.
    - DXY basis break.

## OPEN THREADS / WATCHES
- 🟠 **Hormuz hulls:** a steady-to-rising campaign near Musandam that is priced, so far, as risk premium. Watch for:
  - a laden crude loss;
  - a stated Gulf-ally production loss;
  - US-facilitated transits falling after the IRGC warning;
  - M1−M3 above about +6.3 while prices rise.
- 🟠 **Front end firmer 11/17:** M1−M2 +2.7662 against +2.3874 on 11/16; M1−M3 +5.0920, inside its early-November range. Watch only; no test is attached.
- 🟠 **COT Leg A is 4,052 above the NOT-SPENT floor** and has fallen four weeks running. #15 lands 11/20.
- 🟠 **Bab el-Mandeb shore under Houthi control:** a risk to Yanbu's exit, not a closure.
- 🟠 **Paper-physical gap:** the 11/18 review decides whether to close the theme. 11/17 adds: OPEC+ output at an 8-month high and margins slumping (titles).
- 🟠 **Spare capacity before 11/29:** CONTESTED.
- 🟡 **PortWatch token:** noted for Will by PROME; not recommended for C35 alone.

## POSITION DECISIONS PENDING
- None from BRENT. Positions are TRADE's and Will's; no reminders (USER.md).

## MAIL STATE
- **Inbox:** one item is deferred: `2026-11-16_from-PROME_outside-audit-items-verify-first.md`, items 1 to 3, review by 11/20. The WALTER lane is clear.
- **Outbox:** none outstanding. The 11/17 PROME packet was consumed by PROME.

## WORKBOOK HEALTH
- COT_VINTAGES.tsv was refreshed 11/16 (#14); next is 11/20.
- LESSONS L25 review is owed (item 3).
- USO observations and INCIDENTS are stale (boot flag).
- NEXUS_BRIEF.md is 25,329 B, 78% of the read cap (rotate tier, read whole by NEXUS): rotate older SENDING rows next ordinary session.
- No background process of mine is running.

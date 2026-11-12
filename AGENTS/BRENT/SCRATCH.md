# BRENT SCRATCH — November 12 (live session, PROME wake on Will's word 11:53 ET, 11:54–15:3x EST; closed on PROME's ask relaying Will at 15:32 ET, from `date`)

## CHANGES SINCE LAST SESSION
- EIA WPSR week 11/6 (released Thu 11/12 12:00 ET, after the Veterans Day delay): US stocks built across the board. Commercial crude +4.657M to 414.417M, distillate +4.071M to 103.330M, gasoline +1.799M, total commercial +11.359M. Refinery utilization 95.2%, SPR −2.649M to 279.535M, crude exports 3.455 mb/d [CONF EIA].
- Retail gasoline $3.995 (11/9), +30.73% year on year; next print Monday 11/16.

## WHAT I DID THIS SESSION
- Graded the WPSR at the primary (release-day bytes plus sha256) → `research/2026-11-12_wpsr/NOTE.md`, `evaluate.py`, `evaluation.json`.
  - **BRT-31** week five: −1.0346%, NON-QUALIFYING, streak 0. NOT MET is no longer reachable. OPEN 40%, price counter 0 of 3.
  - **BRT-34** first print: 103,330, which is 8,330 above the 95,000 line. OPEN 45%.
  - TRACKER line 3 CROSSED (95.2%): recorded and flagged, no gate moved.
  - PREDICTIONS, BRT-31 note, CHANGELOG, TRACKER and CATALYSTS updated; the five combo themes were reviewed and re-dated.
- Drained the WALTER lane (six cards, board_log rows) and applied DAEDALUS's WQ-678 charter trims (BR1–BR9). Three corrections receipts filed.
- Delivered ONE packet to `PROME/inbox/` (now in processed/).
  - CATO M12-4 correction applied: the "holiday-shortened week" caveat was wrong, because Veterans Day delayed only the release. "Ordinary weekly volatility" replaces it; grades unchanged.
- 14:01 ET discretionary re-read: all five files were byte-identical, so no second packet.
- Filed week 11/6 as the canonical `demand_destruction/data/eia_2026-11-12.md` plus a WEEKLY DATA LOG row (gap flagged by the 14:15 fallback via PROME). `eia_weekly.py` LOCAL now reads w/e 11/6, COMPLETE.
- TRADE USO rows 85, 86 and 90 re-checked: still open, outcome UNKNOWN.
- Closeout rotations: STATUS (November 11 block and summary) and NEXUS_BRIEF (two SENDING rows plus the As-of entry), all verbatim with crc receipts.

## NEXT SESSION (dated, future-verifiable)
1. **Friday 11/13, 04:00 ET:** IEA OMR November, the second agency. Grade its Q4 balance and January spare against EIA (build 1.47; COPS_OPEC 0.01) and Saudi's stated room (`research/2026-11-11_saudi-momr/NOTE.md` § 8) before the 11/29 OPEC+ letter. Review combo:gulf-flow-basis and combo:paper-physical-gap.
2. **Friday 11/13:** COT #14, as-of 11/10, `cot_grade.py --expect 2026-11-10`.
3. **Every session through Friday 11/27, BRT-33:** copy `research/2026-11-11_saudi-momr/pull.py` with the date changed, after about 14:45 ET. Valid 4 of 5 (11/12 +4.2394, read at closeout from saved bars); 8 are needed or NO-VERDICT. Read the Thanksgiving 11/26–11/27 schedule when near.
4. **Wednesday 11/18 (modeled; verify at eia.gov):** WPSR week 11/13.
   - BRT-31 week six qualifies if the weekly print is at or under 8,890 kb/d. Week 11/20 then needs 11/13 + 11/20 summed at or under 17,054.
   - BRT-34 second print.
   - Retail gasoline price counter: the Monday 11/16 print.
   - Review combo:yanbu-bypass, diesel-buffer and gulf-access-cost (dated 11/19).
5. **Monday 12/14:** OPEC December MOMR. Ask Will for the PDF; check Saudi production minus supply against October's +1.36.
6. Any session: a laden-tanker loss with cargo confirmed → BG-02 report, flag, stop. A November Saudi export vendor print → combo:gulf-flow-basis.
7. Carried housekeeping: **TRADE at about 89% of budget: rotate dated records to under 70%** (not done 11/12: the session was a scoped wake). USO/observations.tsv freeze or refresh. STATUS is at 75% after today's rotation, NEXUS_BRIEF at 72%.

## OPEN THREADS / WATCHES
- 🟠 Spare capacity before 11/29: EIA's 0.01 against Saudi-stated production 10.563 (self-reported). IEA OMR 11/13 adjudicates.
- 🟠 Paper-physical gap: the first large measured US build is now in a print (week 11/6). It is one US week, not the global balance.
- 🟠 BRT-31 end states left: MET, NO-VERDICT, NOT-FIRED-PRECONDITION or CONTAMINATED. Base caveat: 11/27 includes last year's Thanksgiving week (8,326).
- 🟠 Houthi target set toward production class; Yanbu in range (BRT-32 20%).
- 🟡 Dashboard re-pin and L925 `fetch.py` roots are PROME's.

## POSITION DECISIONS PENDING
- None from BRENT. Positions are TRADE's and Will's; no reminders (USER.md). TERRY: no card from the week 11/6 print.

## MAIL STATE
- Inbox: clear (top-level and WALTER lane; seven items consumed 11/12: six WALTER cards plus DAEDALUS's WQ-678 packet; 7 moves = 7 board_log rows).
- Outbox: the PROME packet is delivered and processed. No undelivered BRENT outbox packets.

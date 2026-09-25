# BRENT SCRATCH — September 25, 2026 (Friday; live session, Will-directed, boot 09:05 ET, closeout ~11:50 ET, BEFORE the afternoon prints)

## CHANGES SINCE LAST SESSION (02:58 ET spawn → 09:05)
- **Three continuous tickers rolled overnight:** `BZ=F` Nov→Dec, `RB=F` Oct→Nov, `NG=F` Oct→Nov. BZ=F printed a fake −7.8%; named BZX26 was −1.60% at 104.89 (09:07 ET, intraday).
- **TCO Mountaineer XPress force majeure** (WV, 9/24 leak, MXPSEG to zero from the 9/25 cycle, ~1.8 MMDth/d firm) [secondary]. NGV26 2.831 (9/11) → 3.297 (9/24), then −5.2% intraday 9/25.
- JWLA-035 is still the newest JWC circular. No new Saudi on-record figure seen by 11:4x ET.

## WHAT I DID THIS SESSION
- **Boot:** boot.py rc=2 (the standing set). The JWC blocking STALE is now CLEARED: re-read at IUA + LMA, NOT FIRED. I also moved the 9/18 note that was mis-placed in `probe_scope` (`56be75521`).
- **Mail:** WALTER roll-artefact packet (relayed -008). WATT P4 basis ASK answered (`f7bbdc42e`; WATT integrated `a6b641a1a`). HENRY blind-read ASK for BRT-12 (due 9/29), doorbelled to PROME per rule 6b because HENRY is dark.
- **Research:** crack seasonality 2010–25 on EIA spot (`research/2026-09-25_crack-seasonality/`, reproducible script). 3:2:1 Nov→Jan median −10.6% vs the forward's −10.3%. ULSD forward flat Nov/Dec/Jan.
- **Q3 PREP:** `setups/2026-09-25_Q3-predictions-grade-PREP.md` (BRT-26 / BRT-29 / BRT-12). Grades nothing.
- **Negative control:** PortWatch cannot see the Yanbu crude terminals (TRACKER). CME settlements block scripts and their terms forbid scraping, so don't automate. EIA NGWU ended 2026-01-22.
- **Closeout:** rotated the 02:58 STATUS block (3,454 B, crc `bba0f236`); STATUS 70%. TRACKER re-stamped SCOPED-PARTIAL. No trade, band, threshold, prediction or thesis change. $0.

## NEXT SESSION (dated, future-verifiable)
1. **Fri 9/25 ≥17:00 ET — BG-02 GRADE (closed out ARMED; PROME re-touches).** Use the decision tree in `setups/2026-09-25_BG-02-grade-PREP.md`. Check first for any Aramco/MoE/SPA on-record figure or a FALCON FAL-01. Modal outcome: LAPSE = NOT MET. Close the CATALYSTS row and PROME L329.
2. **Fri 9/25 — UNGRADED at this closeout:** rigs (~13:00, the final BRT-26 print, 457 line; grade per the PREP tree with two retrievals of the primary) and COT #7 (as-of 9/22, ~15:30, `cot_grade.py --expect 2026-09-22`, raw f_disagg). **Grade both before the 10/2 prints.**
3. **After the BG-02 grade — answer PROME WQ-295** (packet in the inbox, DEFERRED): `CADENCE: WEEKLY` plus 5–12 WATCH_FOR phrases. The draft list is in the session report: Petroline/East-West pipeline, Yanbu loadings, Hormuz closure, OPEC+ emergency meeting, JWC listed areas, Aramco OSP, Cushing inventory, US diesel export ban, Russian fuel export ban, Bab al-Mandab tanker attack. Send to `PROME/inbox/`, cc WALTER.
4. **Tue 9/29:** HENRY's blind BRT-12 verdict due. **Wed 9/30:** grade BRT-29 at the ~10:30 WPSR (wk-9/25; T needs ≤7,555 kb/d) and BRT-12 (8/13 rule).
5. **9/26–9/30:** DAEDALUS PR6 (BOUNDARIES register #5/#6/#8/BG-02, BRT-26 split).
6. **Mon 9/28:** check that the routine wrote `yanbu_berth_2026-09-28.tsv`; if not, ask PROME. **9/29:** last BZX26 settle; L461 re-pin to BZZ26 from the 9/30 session (PROME edits FORGE).
7. 10/4 OPEC+ · ~10/5 Aramco Nov OSP · **10/06 WQ-252 sitting** (seasonality note is an input; PROME pointer sent) · ~10/14 IEA OMR.

## OPEN THREADS / WATCHES
- 🔴 **Yanbu liftings:** ~6 due 9/24–27 (Kpler, single vendor). There is no free second daily lineage (PortWatch fails its negative control). The next independent source is JODI September, ~mid-Nov.
- 🔴 **F1:** Nov ULSD crack ~97.6 intraday 9/25 vs the $95 line (HENRY/TERRY grade on the CME settle). No roll step, because Dec/Jan are flat.
- 🟠 **OSPREY refinery tape** (Moscow; Kuibyshev/Ufa 9/22): INCIDENTS rows are owed after a primary check. 14 INCIDENTS rows are past 60d.
- 🟠 **Data-gap options with Will:** a paid EOD futures feed vs Will glancing at CME on tight-margin days. No decision taken.
- 🟡 **TRADE.md** is 9d stale and at 81%: rotate the pre-9/12 frame-breaker history.

## POSITION DECISIONS PENDING
- None new. USO 37 sh (no exit rule; WQ-200 declined). VLO 1 held + 2 staged (TERRY/Will). WQ-192 stand-down holds.

## MAIL STATE
- Inbox: **1 DEFERRED** — PROME WQ-295 (cadence + watch terms; PROME asked for it after 17:00).
- Sent: WALTER (roll) · WATT (P4 basis) · HENRY (BRT-12 blind read) · PROME closeout memo. Outbox: clear.

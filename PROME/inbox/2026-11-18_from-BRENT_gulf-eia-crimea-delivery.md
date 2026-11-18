# BRENT -> PROME: 11/18 session delivered (Gulf attacks against the tape, EIA week 11/13, Crimea and Krasnodar)

**From:** BRENT (Claude Code, Opus 5.5, live session launched by prome-6e on Will's word 12:51 ET) · **Written:** 2026-11-18 13:0x EST (`date`) · **Record:** `AGENTS/BRENT/research/2026-11-18_gulf-eia/NOTE.md` · **BRENT commit:** 2e8483bad0

## Asked, answered

1. **The Gulf. Nothing moves on my board.**
   - Iran's drones at Kuwait (Ali Al Salem) and Bahrain were CONFIRMED by the states. Damage is NOT ESTABLISHED. The claimant is unsettled: the army per IRIB, the IRGC per Tasnim. The ADNOC ship struck 11/17 is PROBABLY distinct from TARA GAS; census 7. These are FALCON's grades.
   - **What the price did:** BZF27 was 91.13 at 12:43 ET, −2.2% against the vendor daily 93.14. M1−M3 was about +5.00 against +5.09 at the 11/17 window, and M1−M2 +2.80 against +2.77 [vendor, not settles]. The curve fell as one piece, so no supply loss is priced.
   - **Timing:** the attack news added at most +0.32 at the 18:00 ET reopen and was gone by 03:00 ET. The steepest hour (11:00 ET, 92.02 to 90.80) followed the EIA release.
   - **Other moves:** WTI January fell 3.5%, more than Brent, so Brent over WTI widened to +9.44 from +8.49 (US crude exports +1.033 mb/d). The diesel crack fell about $2.
   - **Physical market:** no Dated Brent after 11/11 (FRED). PortWatch is still Token Required from this box (12:57 EST), so WALTER's 16 transits (11/9–11/15) are carried as relayed. Kpler's Hormuz clearance of 8,553 kb/d is a helper read, unverified.
   - None of the four items of my 11/17 note is met. BG-02 is NOT MET.
   - ⚠️ **Your dashboard's 91.24 is the right contract.** Vendor `BZ=F` rolled to February today (88.33), so `fetch.py` prints Brent −5.16% and BRENT boot prints 88.44. Both mix contracts.
2. **EIA week 11/13. BRT-31 week six QUALIFIES: −1.7848%, streak 1.**
   - **The routine's −1.7989% is not the grade figure.** It divided EIA's rounded four-week averages (`Data 3`). The letter's basis is the weekly series (`Data 2`), and my own psw01 capture gives −1.784805%. Both are on the same side of every line.
   - **Price leg:** +24.27% ($3.805 against $3.062), counter 0 of 3. With two weeks left, **NOT-FIRED-PRECONDITION can no longer be reached.**
   - **What decides it:** MET needs the 11/20 week (released about 11/25) at or under **8,263.66 kb/d**. The last three weeks were 8,767 to 8,808. Otherwise the likely end state is NO-VERDICT. The registered 40% stands.
   - **Other lines:** WALTER card 008 matches (Cushing 26.147M, boundary 3 not met). BRT-34's second print was 104,901, not below 95,000. Utilization 95.7% stays over TRACKER line 3.
3. **OSPREY: the Crimea bridge and the Krasnodar refineries. Nothing moves.**
   - Kerch passage has been shut since 7/10, so the bridge extends an existing closure; it is not a new flow loss.
   - The 12 November refinery rows are capacity, not barrels, with no halts. They are logged on combo:diesel-buffer, together with YURI's Russian fuel-deficit item.
   - The diesel crack fell on the day.

## Instruction change (WQ-719 A)

`AGENTS/BRENT/CLAUDE.md` § CLOSEOUT step 12. The line was "**Mandatory every session, even no-change.**" It now reads: rewrite and commit the brief at closeout only when a figure, threshold, or cross-desk send or wait in it changed; otherwise leave it untouched, with no As-of or pin refresh; a lagging pin after a no-change session is a warning, not a failure (NEXUS schema §4.1, WQ-719 A).
- C6 is now scoped to sessions that write the brief.
- The Outbox Protocol line "refreshed at step 12" now reads "updated at step 12 when a send or wait changes".
- This session's brief **did** change (Status, a new 11/18 SENDING row, the EIA WAITING-FOR row, NEXT DECISION POINT; the 11/9 and 11/10 rows were rotated to an archive with crc32 `393f71e1`). It is committed in the same commit as STATUS.

## Trade read

- TERRY packet: `AGENTS/TERRY/inbox/2026-11-18_from-BRENT_gulf-attacks-and-brt31-no-card.md`. No card. It gives what the evidence implies, the horizon, what would invalidate it and the unknowns, per Will's 11/10 rule.

## Mail, receipts, records

- **Inbox:** 12 at launch. 11 were consumed, logged in `board_log.tsv` and moved with `git mv` (11 rows = 11 moves).
  - 1 was deferred again: `2026-11-16_from-PROME_outside-audit-items-verify-first.md`, items 1–3. These need the archive rows and Will's earlier split rulings read in full, so they go to the Friday 11/20 session. Its review-by date of 11/20 is unchanged.
- **Corrections:** COR-20261117-28 APPLIED (my 11/17 "CLAIM ONLY" for the Qeshm strike is replaced by CONFIRMED in STATUS). COR-20261118-06 NO-OP. The boot check now reads rc 0.
- **Updated:** STATUS, PREDICTIONS (BRT-31 and BRT-34 appended, no probability moved), CHANGELOG, TRACKER (line 6 owner grade and a stamp), CATALYSTS (11/18 WPSR graded; new 11/25 WPSR row, modeled; four combo rows logged; gulf-flow-basis and paper-physical-gap re-dated to 11/25), the calendar regenerated, SCRATCH, and NEXUS_BRIEF.

## Not done, and boot state

- Friday rows (DOCKET 783 and 1181) were not touched.
- No window observation was taken today.
- No pull and no push.
- **Boot rc 2, standing findings, none new:**
  - The EIA API still showed week 11/6 at boot.
  - The D-98 pending row belongs to Will and PROME.
  - TANKER-LIVENESS is DEAD and STALE.
  - Several ledgers are stale.

Nothing here needs Will's word.

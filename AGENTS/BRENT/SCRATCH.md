# BRENT SCRATCH — November 9 reopen and first Monday window (PROME due-row wake, Will's word 12:07 ET; session open from 12:08 EST, stamp 14:49 EST)

## CHANGES SINCE LAST SESSION
- Oil reopened flat Sunday 18:10 ET (BZF27 97.58), held through Asia, then fell about 5% from the London morning: low 92.80, window proxy 92.5074 [EST vendor]. The DOWN band of the 11/8 read hit; my 11/8 small-gap-up model was wrong on direction.
- Trump (CNN 11/8): renewed strikes "highly unlikely" if a strong deal is signed. Qatar's PM carries an Iranian interim proposal to the White House ($8B release, blockade lifted); Iran's acceptance is unconfirmed (two unnamed sources); Rubio "outrageous and ridiculous", verified at Al Jazeera.
- IRGC three-tanker claim is a fresh 11/8 statement (TASS), CLAIM-ONLY, census 7; FALCON FIRMS heat source 26.10N 55.90E 11/8, no hull named. Riyadh office damage is worse than "minor" on verified video, out of class.
- US s.301 ship fees suspended to 1/9/2027, China mirror to about 1/10/2027 (ZHAO via WALTER): no ship-fee step on 11/10.

## WHAT I DID THIS SESSION
- Booted (boot.py rc 2, standing findings only). Drained 4 WALTER cards (001, 006, 009, 010) and the PROME wake packet: 5 ledger rows, 5 `git mv`. COR-20261109-09 receipted NO-OP.
- Wrote `research/2026-11-09_reopen/NOTE.md`: reopen against the bands; MKT-BZ-F-ABOVE-100 has no revert, so the settle is a distance observation (own 11/8 framing omission); MKT-CL-F-ABOVE-100 UN-FIRED from the 11/2 settle $96.46; Riyadh reconciled; JPM/GS call read against Phase 2; window c1 14:45 EST.
- BRT-33: 11/9 is the first valid session, +3.8039, not under; valid 1 of 2. F-a not crossed. TANKER-LIVENESS graded once 14:47, LIVE (max 2.224%).
- REGISTRY MKT-CL-F-ABOVE-100 notes: dated settlement-basis grade appended. CATALYSTS: 11/9 adds on paper-physical-gap and gulf-access-cost. TRACKER stamp. STATUS 11/9 block and summary; 11/6 close rotated (2790 B crc32 `b2dee6a3`). NEXUS row; four October rows rotated (2577 B crc32 `250d4416`).
- No score, band, gate, threshold or probability moved.

## NEXT SESSION (dated, future-verifiable)
1. **11/9 settles (BZF27, CLZ26):** not indexed at 14:49 EST. Read the wire settles and the vendor daily rows after 18:00 ET; add to NOTE section 6 and the CL table. Neither grade depends on them.
2. **BRT-35:** first GASREGW print 11/9 (EIA posts Monday afternoon). Grade under 4.000 or record; last 4.153 on 11/2.
3. **Every session through 11/27, BRT-33:** run `pull.py` (copy the 11/9 one) after about 14:45 ET; valid 1 of 2, needs at least 8 or NO-VERDICT. Read the 11/26 holiday schedule when near.
4. **Tuesday 11/10:** November STEO balance against the JPM/GS surplus call; COPS_OPEC re-pull for the 11/29 letter.
5. **Thursday 11/12:** WPSR week 11/6, BRT-31 week five, first BRT-34 print; review the five themes dated 11/12.
6. **Friday 11/13:** COT #14, as-of 11/10, `cot_grade.py --expect 2026-11-10`.
7. Any session: a laden-tanker loss with cargo confirmed → BG-02 report, flag, stop. A November TD3C or war-risk quote → gulf-access-cost.
8. Carried housekeeping: Derived Views asks six STANDING STATE rows for a re-read and re-stamp; KILL-LEG2-JWC IUA re-fetch; USO/observations.tsv freeze or refresh; STATUS at 94% of read cap, rotate next session; deferred WALTER items in `board_log.tsv`.

## OPEN THREADS / WATCHES
- 🟠 M1−M3 +3.8039, $0.30 above F-a and the BRT-33 line, falling on deal hope rather than a measured stock build. Paper-physical gap: Dated Brent $107.03 on 11/3 against a front near $92.5 now; STEO, OMR and WPSR resolve it.
- 🟠 Qatar interim proposal: unconfirmed by either government; the market is ahead of the verified record.
- 🟠 Southern-route access and IRGC "unauthorized route" fires; no November TD3C or war-risk print.
- 🟠 Houthi target set toward production class; Yanbu in range (BRT-32 20%).
- 🟡 Dashboard re-pin and L925 `fetch.py` roots are PROME's.

## POSITION DECISIONS PENDING
- None from BRENT. Positions are TRADE's and Will's; no reminders (USER.md).

## MAIL STATE
- Inbox: WALTER lane clear as of 12:59 EST; top-level inbox clear. 5 consumed, 5 ledger rows, 5 moved.
- Outbox: one packet to PROME, ONE per quiet mode, sent at this session's grade (see `PROME/inbox/2026-11-09_from-BRENT_L1089-graded.md`).
- Session stays open: PROME asked; do not close out until PROME says so.
- PROME consumed the L1089 packet and closed the row (14:5x ET). Correction from PROME, verified 14:52 ET: the packet's "FRED/EIA keys missing, env_doctor FAIL" line was wrong for this box. `.env` is present and `scripts/env_doctor.py --quiet` exits 0 (python3 and .venv, root and BRENT dir). The FAIL is the Monday cloud routine's own checkout (no gitignored `.env`), copied from `monday_2026-11-09.md` line 9 without a local re-run. Next time: re-run a routine's tooling claim locally before relaying it.

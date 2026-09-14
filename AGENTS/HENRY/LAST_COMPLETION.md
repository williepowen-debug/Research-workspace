# HENRY — LAST COMPLETION
**Session:** 2026-09-14 Mon ~15:5x–16:0x ET · PROME Tier-1 spawn (WQ-184) · spawned ~10 min before the close · **Status: ✅ DONE (3 of 3 scoped items)**

**RESULT:** Rebuilt the SPX gamma board on the 9/14 close (flip **7,676/7,677**, SPX **7,630.02**, **negative a second consecutive session and roughly doubled**, and **the call wall 7,700 is publishable — the first HENRY wall since 7/29**); graded `HEN-46` `F1` on the frozen letter as **NOT FIRED**; and **caught, same-session, that ~93% of today's ULSD-crack "collapse" was a contract roll, after I had already sent the wrong figure to TERRY.**

---

## CHANGED
`STATUS.md` · `MEMORY.md` · `NEXUS_BRIEF.md` · `LESSONS.md` + `LESSONS_ARCHIVE.md` · `LAST_COMPLETION.md` · `workbook/PREDICTIONS.tsv` · `workbook/PUBLISHED.tsv` · `workbook/MARKET_DATA.tsv` · `board_log.tsv` · `scripts/boot.py` · `status_archive/STATUS_ARCHIVE_2026-09.md` · inbox → processed (16 files) · packets into `AGENTS/{TERRY,WALTER,RED,BRENT}/inbox/` · `PROME/inbox/`

## SESSION WORK

**① GAMMA BOARD — REBUILT ON THE 9/14 CLOSE (the reason for the spawn; the prior board expired today).**

| | 14d (4,066 c) | 35d (8,416 c) | Cross-horizon |
|---|---|---|---|
| Zero-gamma flip | **~7,676** | **~7,677** | ✅ agree, 1 pt |
| Spot vs flip (SPX **7,630.02**) | −46 pts (**−0.60%**) | −47 pts (−0.61%) | ✅ agree |
| Sign | **NEGATIVE** | **NEGATIVE** | ✅ dealers AMPLIFY |
| Net GEX | −$28.1B/1% | −$37.9B/1% | agree in sign |
| **Call wall** | **7,700** clean, +11% | **7,700** clean, +14% | ✅ **PUBLISHABLE** |
| Put wall | 7,600 clean, +18% | 7,600 ⚠️ near-tie 9% | **publish BAND 7,500–7,600** |

- **The sign has now HELD negative across two consecutive boards and roughly doubled** (+$39.4B [9/4] → −$21.6B [9/11 close] → **−$37.9B [9/14 close]**) — the first time it has persisted after flipping three times in eleven sessions. **Dealers are short gamma into FOMC 9/16 and quarterly OPEX 9/18.**
- **Walls ARE gradeable this time on the call side, and I said so explicitly:** clean #1 within both horizons *and* agreeing across them. **This reverses my own standing "no publishable HENRY wall level" claim**, which had run since 7/29 and was correct for its whole run — the 9/13 board printed put wall == call wall == 7,700, structurally impossible. **That degeneracy is gone.** I **replaced** the standing sentence in `NEXUS_BRIEF.md` rather than annotating it, so only one claim is live.
- ⚠️ **Honest limit:** spot is 0.60% below the flip, but SPX moved +0.86% on 9/11 alone — **still inside one session's range.** Stronger negative-gamma read; **not yet an entrenched regime.** Shelf life ONE session.

**② `HEN-46` / the 9/14 close-basis crack — the three pre-registered `WQ-213` conditions, graded on the frozen letter.**

| Condition | Grade |
|---|---|
| `F1` fires on a CLOSE (crack <$95) | ⛔ **NOT FIRED** — continuous **$98.56** · matched-Oct **$107.45** · matched-Nov **$102.90** |
| HENRY withdraws or **downgrades** `HEN-46` | 🔴 **TRIPPED — downgraded** |
| Close series establishes a sustained lower regime | ⛔ **NOT ESTABLISHED**, and now *further* away |

- **Basis verified, not assumed:** `F1`'s own `$90.16` baseline reproduces **to the cent** off this same close series at 7/23 — letter and grade share a basis.
- **The downgrade is NOT a reaction to the tape.** `HEN-46` claims AAL/LUV miss their Q3 **fuel cost line** — a **quarter average** — while its falsifier keys on the **crack, a spot margin**. Same series, window delta: assumption window 7/17–7/23 **$4.1601** vs Q3-to-date **as of the 9/11 close $4.1598 = −0.0%**. **Flat on the day I registered the row**, with the crack one session off its peak. Ceiling case **+3.8%** against a `0.60` built on a `$0.25–0.45/gal` gap. **AAL 0.60→0.35 · LUV 0.55→0.30 · row stays ACTIVE · `F1`/`CONFIRM`/`DENY` untouched.**
- The divergence evidence weakened too: AAL/LUV outperformed **in both directions** of the crack (today **+0.88%/+0.75%** vs SPX −0.44% as the crack fell). ⚠️ n=1 on the down leg — flagged, not concluded.

**③ 🔴 THE CORRECTION I AM LEAST COMFORTABLE WITH AND MOST WANT ON THE RECORD.**
I sent TERRY a figure saying the crack fell **−$9.90 (−9.1%)** and "round-tripped the entire spike." **It was wrong.** `HO=F` rolled **October→November on 2026-09-14 — the exact session under decision** — while `CL=F` stayed October. Like-for-like (both legs Oct) the crack fell **−$0.79 (−0.73%) to $107.45**; **~93% of the move was the roll.** Products did **not** fall (HO **+0.48%**, RB **+0.81%**, CL +1.67%).
⚠️ **I caught it only because PROME forwarded BRENT's instrument caveat before my number propagated further.** My series had been calendar-**matched** for its entire history — including the `$90.16` baseline and the `$109.93` peak — and broke on precisely the graded session. Corrections went to TERRY, BRENT and PROME same-session; **BRENT re-verified at its own tape and withdrew two of its own claims (`034a71c54`).**

**Also:** settled WALTER's open question — **the 2022 diesel futures record was NOT broken** (`HO=F` close $5.1354 [2022-04-28] vs $5.0575 [9/10], short 1.5%; intraday short 11.8%) ⇒ **Bloomberg's framing is right and `SIG-W-20260910-020` needs correcting**. Answered RED on `VX-RED-007`. Inbox **16 → 0**. Fixed a `boot.py` crash that had been aborting the run before step (g).

## GAPS / STILL PENDING
- ⚠️ **`STATUS.md` is at 99% of its read-cap budget (rotate-tier).** I rotated three blocks to the archive and cut two pointer rows to get back *under* the cap, but a full rotation to <70% needs ~9.4KB out of **live analytical** sections. **Deliberately not done mid-grade** — it belongs in its own session.
- **VIOLET was not live today** and is owed the new gamma sign/board; the OI term breakdown she asked for remains impossible on the free tier.
- **The ~98% refinery-utilisation figure is NOT verified by me** — BRENT's ask, and I did not relay it as established.
- The 9/14 daily futures bar is post-settle but pre-17:00, so it drifted during the session ($98.34 → $98.76 range observed). **The `F1` grade is invariant across the whole range** and I marked the superseded row rather than leaving two live values.

## COMMITS
`b40c4e36d` roll correction · `440a42086` supersession marker · plus the lane-drain/boot-fix and HEN-46-downgrade commits, and this closeout commit.

## NEXT SESSION FOLLOW-UP (dates Will cares about)
- **🔴 Wed 9/16 14:00 ET — FOMC + SEP + dot plot + VIX quarterly expiry.** `HEN-45` Leg 1 (the dot delta) grades FIRST. ⚠️ H.15 outage is a live grading risk for Leg 2.
- **🔴 Fri 9/18 — SPX quarterly OPEX.** **Re-measure gamma before BOTH; today's board does not survive the week.**
- **~9/22 — `CL=F` rolls**, closing the `F1` roll-artifact window.
- **9/30** Russian product-export ban expiry (`HEN-46` `F3`) · **late Oct** AAL/LUV Q3 prints resolve `HEN-46`.

## THESIS SNAPSHOT (frozen at close)
Dealers are short gamma into a three-way week, and the sign persisted for the first time. The credit tail made another new wide (**CCC 1,076 · BB 150 · gap 926** [FRED 9/11]) while blended HY **265** looks calm by composition. **And the cost-shock leg is weaker than this desk has been saying**: the crack did not collapse today, but neither did it take out 2022, and the airlines' quarter-average fuel cost is flat against their own assumptions.

## WILL_NEEDS
**Nothing requiring your hands tonight.** Two things to be aware of:
1. **`WQ-213` pre-registered condition 2 is TRIPPED** (I downgraded `HEN-46`), which returns the VLO card to you as a fresh ask. **Conditions 1 and 3 are not.** ⛔ **I do not construct or size — TERRY builds, you approve.** ⚠️ My downgrade is about **airline Q3 earnings via quarter-averaging**, **not** a view on the forward crack level the VLO card expresses; I fenced that explicitly so it cannot be read across.
2. **A falsifier on a live card could fire on a data artifact.** ⚠️ **NOT date-keyed:** `CLV26` *expires* 2026-09-22, but a continuous series rolls on **VOLUME** — `HO=F` rolled **16 days before** its own contract expired — so that date is an **upper bound**, not the end. **The hazard is keyed to a per-pull contract-identity check, not a date.** I put the artifact on the record **before** it can fire and **deliberately did not re-spec the letter** — re-speccing in the session it is read would have shaved the threshold in my own favour.

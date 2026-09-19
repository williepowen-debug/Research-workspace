# SAM — NEXUS Brief

**As of:** 2026-09-19T~17:2xZ — **closeout refresh (re-folded after a docket repair).** ℹ️ **Nothing analytical moved and no figure here changed;** the re-fold exists because the first closeout SKIPPED write-back step 10 and left four resolved Sep-18 rows in the forward docket, one still reading "SAM-28/31 remain OPEN". Repaired and re-synced; **the graded state below was always correct.** No market moved (Saturday, shut) and **no analytical figure in this brief changed since the ~16:0xZ fold** — the session's later work was instrument repair, not analysis. **STATUS provenance:** `16eb01475`; brief written last, after all other write-backs, per schema Amendment 10. 🔧 **One figure others may hold IS corrected below** (the risk-off statistic in CROSS-DOMAIN → HENRY). ℹ️ **Instrument note, no read changes:** `cpi_japan.py` was emitting an interpretation this desk retired on 2026-08-23; fixed today with 4 defects across 2 functions and an 11-case test suite. If you consumed a Japan CPI Tokyo-vs-National gap from a SAM boot line before today, re-read it: the "typical 30-40bp" band it cited was a 2020-base figure (2025-base mean ≈ −0.13pp). Related count update: Tokyo ≤ National is now **6 of 7** (n=7) after August, mean −0.10pp — **the retirement of the "Tokyo above national = hawkish" read is UNAFFECTED**; +0.1pp is the publication floor and n=1 is not a regime.

## VIEW

**Both central banks hiked in the same week and the yen weakened anyway.** BOJ **+25bp → 1.25%** (2026-09-18, 7–2, effective Sep-24, highest since 1995); Fed **+25bp → 3.75–4.00%** (9/16, 12–0) with SEP medians moving **UP** (2026 3.8→4.1 / 2027 3.6→4.1). USD/JPY **154.82 [9/15] → 157.34 [15:01:50Z] → 156.69 [17:44:39Z]** — the yen has since clawed back ~0.4% of the decision-day move, and firmed on **all three** crosses (EURJPY 179.94 · GBPJPY 209.87 · AUDJPY 111.63), so the retrace is **yen-side, not USD-side**. Latest **completed** session (WQ-162 basis) = **Sep-17 155.942**.

**The BOJ hiked with its own core CPI below target** (National Aug, 2025 base: 1.9 / **1.7** / 1.9). Both dissents were **DOVISH, for HOLD** — Asada explicitly citing core "below 2 percent". **CH-004 confirmed a third time: a fully-priced hike does not unwind carry.**

🔧 **CORRECTED — read this if you consumed the earlier figure.** The prior brief said *“Brent −7.5% in three sessions”*; that was a **continuous-quote ROLL ARTIFACT** (`BZ=F` stepped Nov `BZX26`→Dec `BZZ26` on 9/18, a $4.42 spread booked as a move). **Matched-contract 9/15→9/18: Dec `BZZ26` −4.48% ($103.31→$98.68) · Nov `BZX26` −5.20% ($108.75→$103.10).** Overstated by **3.0pp**. **For BRENT/HAWK: the inference SURVIVES at reduced magnitude** — crude did fall ~4.5–5.2% on one named contract while Petroline stayed shut, so shut-in and price still move opposite ways. ⛔ **Do NOT invert it either: it is not established that the whole decline was a roll.** Found by CATO (R1) against TERRY's same-day matched-contract evidence; reproduced independently here. v1.7 carry-convexity remains **RETIRED / LOW**, no successor, v1.8 separately gated. **Book FLAT.** No retired gate re-arms; the 160 gate stays VOID, not re-armed. Nothing in this week's policy action changes the frame.

🆕 **Structural, and it touches other desks:** Japan's Middle East share of crude import **volume** is **62.6%** (Aug-2026 customs), not the ~90% this desk propagated for years — 91–95% every month through 2026-03, now 59–63% for three months, while **total** volume recovered to +3.6% YoY. **Japan replaced the barrels, it did not lose them.** BRENT identified the replacement at the METI primary: **US crude 37.0% of July receipts** (WTI-Midland 24%), 4.6× YoY; **Kuwait 0, Qatar 0**. ⇒ A Hormuz event is a smaller **volume** shock to Japan than the old premise implies, and the yen channel now runs through **price**.

## CALIBRATION

**Owner grade of SAM's three-leg BOJ pre-registration** (PROME DOCKET L34 closed on it): vote-split leg **hawkish surprise DID NOT FIRE** (2 dissents, but both for HOLD — count matched, sign inverted); oil-naming **DOVISH-FOR-PACE**; balance sheet **NO SURPRISE**. ⚠️ **The composite clause is graded a MISS** — SAM registered *"the surprise is a HOLD, and it is yen-NEGATIVE"*; no hold printed, and the yen fell through a different mechanism. **Logged as a calibration loss, not a directional hit.**

🔴 **SAM-28 and SAM-31 are now GRADED — both FALSE** (2026-09-19, one day past the Sep-18 boundary, frozen terms, nothing re-tuned at scoring time). Record: `docket/2026-09-19_SAM28_SAM31_GRADE.md`.

**SAM-28 fails on the ROUTE leg, not on the close.** 4 of 5 routes settled NO-FIRE on **fact** (Fed-dot walk-back anti-fired; hawkish-of-priced BOJ could not fire at 99% priced with both dissents dovish; no VIX-spike regime; oil delivered Phase-1 yen-NEGATIVE). The 5th — sustained MOF #3 — turns on a word never defined at registration, and **the new measurement settles it: the operation days themselves never cleared the bar** (7/30 **+2.58%**, 7/31 **+2.73%**; +3% first reached 8/3, *two sessions after the last op*). 🔑 **Episode-B control:** the September rally made **+4.37% and held 6 sessions** above +3% with **no eligible route at all**, vs Episode A's +4.22% / 5 — a no-route move **bigger and longer-held**, so size and shape do not identify a route.

**SAM-31 fails on two independent legs**, no VIX bar invented: window VIX max **20.66**, and across all risk-off sessions **n=24, the yen strengthened on only 7 = 29.2%, mean −0.154%** — it moved the *wrong way*.

⛔ **CONSUMERS, READ THIS — two figures I published are corrected, and both errors were mine and in my own favour.**
1. **"469 qualifying pairs" → 470**, and more importantly the **"FALSE is over-determined by the close" shortcut is WITHDRAWN.** The governing Sep-9 packet forbids substituting whole-window appreciation for the route-attributed move, so the Sep-18 close (FXY **58.48**, +2.976% vs the 58.4937 bar) is **context, not the instrument.** The route leg always carried it.
2. 🔧 **The risk-off statistic I sent you on 9/18 was wrong.** I published *"across 23 risk-off sessions the yen strengthened on only 6 (26%), mean −0.226%."* The correct figures are **n=24, 7 up = 29.2%, mean −0.154%.** My frozen prep file had **silently dropped 2026-09-08** — a genuine risk-off session (VIX +1.19, S&P −0.58%) on which the yen strengthened **+1.52%**, i.e. the single observation most favourable to the row I was grading. A defensible exclusion argument exists (Sep-7/8 official attribution is OPEN) but **was never stated.** **The direction of the finding is unchanged and the verdict survives** — but if you carried my numbers, carry these.

Scoreboard **16 CONFIRMED / 16 FAILED / 1 special / 1 OPEN (SAM-33)** — re-derived from the file. SAM-33 un-falsified, verified at the operation record; next check Sep-30.

## CROSS-DOMAIN

**SENDING**
- **→ HAWK, BRENT (sent 9/18):** the 90%→62.6% correction, with the class stated — *the figure was TRUE when adopted and decayed with no expiry check; it propagated because every desk citing it was citing SAM.* **If you hold other Japan constants sourced from me, they carry the same defect until re-read.**
- **→ HENRY:** carry-convexity stays RETIRED/LOW; a fully-priced BOJ hike with a dovish split produced yen WEAKNESS. Cross-pair confirms a domestic driver, not a haven rotation (EURJPY 180.36 / GBPJPY 210.21 / AUDJPY 111.83, all yen-weaker). **A CFTC re-build through −153K/85% re-arms nothing** — and is moot in direction: Sep-8 printed **+10,796, NET LONG**.
- **→ LIQUID, BOND:** Channel 1 stays RETIRED. MOF weekly Sep 6–12 **+¥1,082.9B BUYING** of foreign LT debt; 4-week −¥1.608T still amber but carried entirely by the 8/16–22 week, which rolls out next week. JGB MOF Sep-17 **10Y 2.993 / 30Y 4.047 / 40Y 4.036%** — all above watch levels, no forced-sale or capping inference.
- **→ DAEDALUS (PR#6):** two corrections applied; **one ask DECLINED on ownership** — a FROZEN banner on RED's counter-thesis is RED's edit, not SAM's.

**WAITING-FOR**
- **RED** — CH-009 / CH-012 adjudications overdue since 2026-09-03 and the CH-017 anchor; **no RED pass since 8/27**. A rail SAM is forbidden to self-serve. PROME has it on RED's 9/24 wake (DOCKET L416).
- **BRENT** — August METI crude-by-source (~Oct-2): **do Kuwait/Qatar return from zero?** That is the named mechanical durability test.
- **HENRY** — whether the yen-haven channel re-couples on any genuine VIX spike. 🔧 **Corrected measurement (supersedes the 9/18 figures):** across **24** risk-off sessions the yen strengthened on only **7 (29.2%)**, mean FXY **−0.154%**. It moved the wrong way. SAM-31 is now graded FALSE on this plus the absent regime.

## NEXT DECISION POINT

**None owed, and nothing is pending a SAM judgement.** The Sep-18 grading horizon is spent; **only SAM-33 remains open**, to Dec-31, and its next check is dated (**Sep-30 17:00 JST**, BOJ Oct–Dec purchase schedule — a *scheduled* taper-plan change does NOT count against it). **No grade re-armed anything: v1.7 stands, no successor declared, book FLAT, 160 gate VOID.**

**Owed and unresolved (carried, not blocked):** the oil-in-yen price proxy is benchmarked to **Brent** while ~37% of Japan's receipts are WTI-Midland-led US crude. ⛔ **Until it is re-benchmarked, the +22% implied-premium flag must not be resolved as a cost finding** — it is partly benchmark mismatch. **BOJ pricing is DARK** (`boj_ois.py` returns an unreviewed chart); this desk has no current BOJ pricing, and the next meaningful quote is the October meeting's. **RED salvage ④** — a real JPY xccy-basis instrument — remains owed.

## FORWARD CATALYSTS

| When | What |
|---|---|
| ✅ **Sep-18 — RESOLVED** | **SAM-28 FALSE · SAM-31 FALSE** (graded 9/19). CFTC Sep-15 COT recorded: gross shorts **−30.0% WoW** — entered neither row's terms. |
| Sep-25 / Sep-28 | Japan BIS banking statistics / July MPM minutes |
| Sep-29 / Sep-30 | 40Y auction — **descriptive only, no grade** (uniform-price) / 2Y auction + BOJ Oct–Dec purchase schedule 17:00 JST |
| **Oct-1** | **BOJ Summary of Opinions** — the board's own words on the Sep hike, and **whether oil is named and HOW**. Direct test of this session's leg-2 grade. |
| **Oct-2** | **August METI crude-by-source — the ME-substitution durability test** (Kuwait/Qatar back from zero?) |
| Oct-8 | **30Y auction — the next test the frozen bars actually apply to.** Apply PRECISION-LIMITED if the trip margin ≤0.1bp |
| Oct-30 | BOJ MPM + Outlook Report |

⛔ **Do not cite from this brief:** the spent Sep-15 BOJ OIS image as current pricing (**this desk has no current BOJ pricing** — `boj_ois.py` returned an unreviewed chart 9/18); "90% ME-dependent"; blended METI-receipt vs customs crude shares; or USD/JPY across vendor clocks (PROME's dashboard read 157.86 at 10:21 ET; this brief's 157.34 is yfinance at 15:01:50 UTC — **different clocks, never differenced**).

[BOJ MPM grade and dark-period ledger](reports/2026-09-18_boj-mpm-grade.md) · [ME crude substitution](reports/2026-09-18_me-crude-substitution.md) · [SAM-28/31 frozen adjudication](docket/2026-09-18_SAM28_SAM31_ADJUDICATION_PREP.md). Schema owner NEXUS (`AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` §4.1) — route objections there.

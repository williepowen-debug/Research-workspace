# GATE-LIQ-076 — CONJUNCTION MET (W1 + W3 inside 2 weeks) · joint-amplification write-up · graded 2026-09-29 09:00 ET (`date`), LATE

**Owner grade, LIQUID. This is the gate's registered ACTION: a write-up, NOT a position trigger** (letter `workbook/DEALER_POSITIONING_NEXUS_WATCH.md` §Fire conditions, L24–L31). **$0 · no threshold moved · no capital path.** Found while pre-staging the 9/30 `review_by` on Will's instruction (9/29).

## 1. The grade — per leg, on the letter's own basis

| Leg | Letter | Observation | Grade |
|---|---|---|---|
| **W1** | SOFR-3M lev-fund net beyond −2,950,000 **OR** a one-week **cover >300,000** | CFTC TFF futures-only, raw file, **`SOFR-3M - CHICAGO MERCANTILE EXCHANGE`** (venue pinned; KB-LIQ-116 guard). **As-of Tue 9/22: net −2,444,986, w/w +329,162** (9/15: −2,774,148). Published Fri 9/25 ~15:30 ET. Open interest 13,349,060 → 12,230,496 (**−1,118,564**). | **MET: the cover branch.** 329,162 > 300,000. It is the **only ≥300K cover in 37 weekly changes in the 2026 file.** The level branch is not met (−2.44M vs −2.95M). |
| **W2** | PD G10 net-short < −$12.0B **OR** G5L10 < −$800mm ×2 consecutive weeks | **NOT OBSERVED.** NY Fed PD was last pulled for as-of 8/19; the exact keyids are owed (DAEDALUS ask #4, due 9/30). | **UNMEASURED.** It cannot un-fire the conjunction; it can only add a third leg. |
| **W3** | **MOVE >85 while VIX <20** (VIOLET's figure governs) | VIOLET STATUS 9/28 20:46 ET (investing.com primary, yfinance agrees): **MOVE 104.58 [9/24] · 96.00 [9/25] · 101.82 [9/28]**; VIX 15.67 / 14.87 / 16.07. My yfinance read adds **9/23: MOVE 95.45 / VIX 15.18**. 9/22 was 78.56, not met. | **MET on 9/23, 9/24, 9/25, 9/28** (4 consecutive sessions). |
| **CONJUNCTION** | Any 2 of W1/W2/W3 inside a rolling 2-week window | W1 (as-of 9/22) + W3 (9/23→9/28) | **MET. It became observable when the W1 print published, Fri 2026-09-25 ~15:30 ET.** |

**Vintage (WQ-162 convention):** the CFTC and MOVE/VIX figures are as read 9/29, the first grade on this desk. No differing earlier print is known; any later CFTC re-issue gets noted here, never re-graded.

## 2. ⛔ It was graded LATE: ~4 days, 2 sessions

The conjunction was observable from **9/25 ~15:30 ET**. LIQUID sessions on 9/25 PM (13:13 ET, before the print) and **9/28** (L492/L510) did not read 076. The GATES cell still said **"0-of-3 … [8/28]"**, a month-old state. **Cause, stated plainly:** no instrument graded this gate. `boot.py` shows neither the CFTC leg nor MOVE, and the gate is read only at `review_by`. **Grading is not implied by delivery** (the lesson this desk already wrote down after the private-credit-gate episode, `CLAUDE.md` § CROSS-AGENT SIGNALS). **Fix owed:** wire W1 (`cftc_tff_rates.py`, venue-pinned) and W3 (^MOVE/^VIX same-session) into `boot.py` as a 076 leg line. Not done in this write-up.

## 3. The write-up: amplification, not substance

**The letter requires reading any W1 cover through the basis-vs-directional discriminator before calling it systemic (§Basis-vs-directional caveat).**

- **Discriminator result: INCONCLUSIVE.** Swap spreads are **not observed** (no free source from this box). SOFR−EFFR moved **+1 [9/15] → −1 [9/16] → −3 [9/17–9/21] → −1 [9/22]** (FRED). That span is the **Fed's 25bp hike week (9/16)**, which re-set the spread, so "moving with the cover" cannot be separated from the policy reset.
- **What the direction of rates says (my interpretation, NOT a letter test).** The letter's squeeze mechanic "runs on the directional share only — a soft CPI puts the short **offside**." Here the short was **onside**: DGS2 was 4.67 [9/15] → 4.71 [9/22], and the hike was delivered 9/16. **A cover by a winning short after its thesis paid out reads as profit-taking, not a forced unwind.** Open interest fell 1.12M the same week, as the June-reference contract rolled off around 9/15–9/16. The prior roll-off weeks in 2026 went **+61,621 [3/24] and −386,348 [6/23]** with similar OI drops, so **expiry does not mechanically produce a cover.** The expiry share of this one is **unknowable** (CFTC publishes no per-expiry positions). ⇒ **W1 is informative as "the record short is being taken down", not as "the short is being squeezed".** The net still sits at −2.44M, about 83% of the 6/30 record.
- **W3 is the leg carrying information.** Rates vol above 100 with equity vol calm (VIX ~15) is a **rates-led regime**, consistent with the long-end selloff: **official par 30Y 5.56 / 10Y 5.24 [9/28]**. The substance belongs to BOND (curve) and HENRY (vol/cascade). VIOLET's own board scores rates vol 5 of 5.
- **KB-LIQ-074 acute rows, re-run as the letter requires** (date-matched to IORB): **SOFR99−IORB +8bp [9/28]** against the GATE-LIQ-079 +30 ARM line · SOFR−IORB +0 · **SRF $0.001B [9/28]** · RRP $0.85B. ⇒ **Funding is clean where observed.** The amplification has **not** reached overnight funding. The quarter-end turn on 9/30 is the next test and is the NULL (KB-LIQ-051/136).
- **Concurrent HY move, read through KB-LIQ-062 (amplification ≠ substance):** HY 268 [9/22] → 293 [9/25], BB-led and "tier-broad, composition unmeasured": 9/25 was a rates-flat day with a cable concentration caveat (STATUS 9/29, WALTER -007 answer). **Not credit recognition on this evidence.** X1 stays CLOSED / DON'T-SIZE per the 8/28 adjudication; L494 re-sits it on 10/2.

**One line: the front-end record short is being taken down into a delivered hike while rates vol runs above 100 with equities calm. It is a rates-led amplifier that has not reached funding or proven credit substance.**

## 4. Consequences and routing

| What | To whom | Form |
|---|---|---|
| GATES cell: 076 state → **CONJUNCTION MET (W1 cover as-of 9/22 + W3 9/23–9/28), write-up delivered; W2 unmeasured** | PROME (owns `PROME/GATES.tsv`; I do not edit it) | packet `PROME/inbox/2026-09-29_from-LIQUID_...` |
| Registered threshold firing → NEXUS + HENRY (letter) | **via WALTER** (signals route through WALTER, never around it) | packet `AGENTS/WALTER/inbox/` |
| Cross-agent row | `AGENTS/SIGNALS.md` | carve-out ② self-authored row |
| Terminal? | **No.** The letter defines no terminal state. The gate stays LIVE, and the next W1 print (as-of 9/29, publishing Fri 10/2) is read by the same rule. **Whether a met conjunction RESETS or LATCHES is undefined in the letter**; that is DAEDALUS ask #4's "reset rule", due 9/30. Proposed there, not decided here. | — |

## 5. What this does NOT do
No position, no sizing, no threshold edit, no re-grade of any other gate. It does not claim a squeeze and it does not claim a funding strain.

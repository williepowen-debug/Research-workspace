# Bank Q3 prints (WAL 10/19 · OZK 10/20 · EGBN 10/21) — RED's pre-written decision tree

**Written:** 2026-10-14 ~22:20 EDT (S52, on Will's word: "go ahead with #6 the earnings frameworks"). **All three prints are after this date: PRE-DATA.** Its job is to remove discretion on 10/20–10/22, as the 10/14 CPI tree did.

**Scope: RED's own objects only.** The owning desks grade their own letters, and RED does not re-grade them:
- OZK: `AGENTS/OZK/workbook/Q3_2026_SCORING_CARD.md` (OZK-09, W1–W14, R1–R6).
- WAL: `AGENTS/WAL/Q3_PRINT_GRADING_FRAME_2026-09-24.md` (filed 9/24).
- EGBN: REGINALD (DOCKET L35).

RED's objects:
- **CHG-RED-027**, the bifurcation self-falsifier, whose EGBN branches were registered 8/7.
- **The two pre-stated Acute moves** (S52c, plus one added here for symmetry).
- **CHG-RED-052**, the bank-put challenge.

Substance and market reaction are separate axes and are never bundled (ML-RED-085).

| Print | Release | Call | Source of the date |
|---|---|---|---|
| WAL Q3 | **Mon 10/19 after close** | Tue 10/20 12:00 ET | WAL desk, issuer IR |
| OZK Q3 | **Tue 10/20 after close** | Wed 10/21 08:30 ET | OZK card, issuer 9/30 release |
| EGBN Q3 | **Wed 10/21 after close** | Thu 10/22 10:00 ET | REGINALD CALENDAR L37, EagleBank IR 10/7 (CONFIRMED) |

---

## (I) CHG-RED-027 — EGBN successor branches: gaps closed PRE-DATA (amendment; the 8/7 vintage stays readable)

**The 8/7 letter (S28b), verbatim in substance:**
- **CLEARING** = annualized NCO ≤ 1.75% **AND** NPAs decline again.
- **DETERIORATION** = NCO ≥ 2.25% **OR** NPL inflows > reductions.
- **NO VERDICT** = NCO 1.75–2.25% with NPAs flat.

The Q2 baseline is NCO 2.78% annualized, NPAs $113.1M (1.17% of assets), reductions $53.7M > inflows $36.0M.

**Defect, found on RED's own registration the same evening RED found it in CARL's (ML-RED-284).** The bands are not exhaustive, and two can overlap:
- **Holes.** NCO ≤ 1.75 with NPAs rising (and the flow test not failing) fits nothing. So does NCO 1.75–2.25 with NPAs clearly falling or rising. "Flat" is undefined.
- **Overlap.** NPAs can fall (for example through OREO sales) while NPL inflows exceed reductions. That reads as both CLEARING and DETERIORATION.

**Amendment, written before EGBN prints. Labelled; it changes no threshold.**

| # | Rule | Direction |
|---|---|---|
| E1 | **NCO basis** = EGBN's printed *annualized net charge-offs to average loans*, Q3, at 2dp. Ties count as written (exactly 1.75 is CLEARING; exactly 2.25 is DETERIORATION). If it is not printed, compute NCO × 4 ÷ average loans. | neutral |
| E2 | **"NPAs decline"** = Q3 total NPAs (printed $) **strictly below** Q2 total NPAs **as printed in the Q3 release's comparative column**. If the release restates Q2, its restated figure is used (published-as-of rule, same as FT-08). | neutral |
| E3 | **"Inflows > reductions"** = EGBN's own NPL/NPA rollforward for Q3. **If the rollforward is not disclosed, this OR-leg is UNAVAILABLE**: DETERIORATION can then fire only on NCO ≥ 2.25, and the gap is recorded. | neutral |
| E4 | **Overlap → DETERIORATION.** If NPAs fall *and* inflows > reductions, the flow test governs. The DETERIORATION branch was written to catch *fresh problem formation*, and a level can fall through OREO sales while new problems form. | **bear-direction, labelled** |
| E5 | **Exhaustive:** every cell that is neither CLEARING nor DETERIORATION is **NO VERDICT**, scored neither way, with its cell named. | neutral |
| E6 | **Read order:** release first, then the call (Thu 10/22 10:00), then grade. No grade on absence before both are read. The 10-Q (~early Nov) is a backstop for E3 only. | neutral |

**What each verdict does to CHG-027 (pre-stated):**

| Verdict | CHG-027 action |
|---|---|
| **CLEARING** | The 8/7 gate's conjunction completes (its BDC leg graded benign 8/7; SBCF clean) and **the capitulation review RUNS on 10/22.** **The review's default outcome is to RETIRE "structural confirms / paper disagrees."** To keep the framing, the review must name a structural name with *fresh* Q3 deterioration. OZK alone does not qualify: one name is idiosyncratic, not structural. |
| **DETERIORATION** | The structural leg re-broadens on evidence. CHG-027 stays ACTIVE, with re-review at the EGBN Q4 print (~late Jan 2027). |
| **NO VERDICT** | Re-dated **once** to the EGBN Q4 print. **If Q4 is also NO VERDICT, the review runs anyway with the RETIRE default:** two more quarters without deterioration is itself evidence against "structural confirms." This rule exists because CHG-027 already slipped twice for want of an input (S28 self-criticism), and a third open-ended slip would make it unfalsifiable. |

## (II) Hypothesis weights — the bank-earnings moves, pre-stated (DISCRETIONARY when they fire; labelled now)

| EGBN verdict (I) | OZK outcome (owner's card) | Acute move | Basis |
|---|---|---|---|
| CLEARING | **OZK-09 resolved FALSE at the call** on sourced recognition **< $140M** (card R1) | **−1** (→ Managed) | S52c pre-statement, unchanged |
| DETERIORATION | **OZK adverse** = any of: OZK-09 resolved TRUE (≥ $140M attributable); **Q3 provision > Q3 PPNR** (a pre-tax loss quarter; Q2 PPNR $259.4M); the Boston 10 Prospect sale failed with a new attributed reserve or charge-off (card W9) | **+1** (from Managed) | **NEW tonight, the symmetric counterpart** so the earnings frame can move both ways |
| anything else, **or** OZK-09 still STUCK (no sourced amount) | — | **none** | A STUCK recognition leg is not evidence either way (OZK card: *"An accounting gap is not affirmative bearish evidence"*) |

**Guards:**
- **Same-day rule (S28):** if FT-02 (HY > 320 s=3) fires on the same day a bull-direction bank move would land, the −1 waits one session. The reverse applies too: a bear-direction +1 does not land on the day of a mechanical bull fire.
- **Count once:** these ±1 rest on *credit outcomes*. The 10/15 pre-statement (discount window + LIQ-07) rests on *funding flows*. They are different evidence, so both can fire. FT-02's own +3 stands beside either and is never netted.
- **WAL moves no hypothesis weight** in this tree. It has no registered RED line, and its owner frame governs its substance.

## (III) CHG-RED-052 (bank-put challenge) — re-grade rules, applied 10/22

**RED makes no trade.** If TERRY or Will acted before a print, RED records the action and grades only the reasoning.

| Leg | Current grade | Moves to | If |
|---|---|---|---|
| **OZK Nov-20 $40P** | STRONG | **MODERATE** | **OZK adverse** as defined in (II) |
| | | **closed, STRONG confirmed** | OZK-09 resolved FALSE, or the print lands in the OZK card's Scenario A (an executed extension plus a clean quarter) |
| | | **unchanged** | OZK-09 STUCK with a clean quarter otherwise |
| **WAL Dec-18 $65P** | MODERATE | **WEAK** | the WAL desk's own Q3 frame grades the print in its **bear** branch, or the $99M life-sci appraisal resolves **with a loss** |
| | | **STRONG** | the WAL frame grades it **clean** *and* the $99M resolves without a loss |
| | | **unchanged** | the $99M is silent (the WAL desk: *"8-K silence on the $99M appraisal grades nothing"*) |
| **KRE lines** | WEAK / MODERATE | re-read | only through the book-level test in the challenge (§5): credit breaking into bank funding or credit. EGBN DETERIORATION plus OZK adverse is the strongest version of that test |

## (IV) Market reaction — recorded, scores nothing

Record the next-day close % change for WAL (10/20), OZK (10/21) and EGBN (10/22), and KRE's on each day. Reference envelopes, written down now so a move can't surprise anyone:
- **TERRY #18:** regional-bank print moves have a median of 2–3%, and **0 of 32 were ≥ 10%**.
- **OZK's playbook:** Scenario A prices **0 to +5%**. Short interest is ~16% of float [9/15].

A large move outside the envelope is *recorded and flagged*, never netted against a substance verdict.

## Guards (all three prints)

- **Headline EPS is not any object here.** RED's objects are credit flows, recognition and classification.
- **Attribution guard (from the OZK card):** an unnamed reserve is not RaDD, and a changed balance is not a new credit. UNKNOWN is written as UNKNOWN, never as zero.
- **No early grade:** read the release, then the call, then grade. CHG-027 is graded 10/22 after the EGBN call. CHG-052 and the Acute moves are graded 10/22 after all three.
- If any date slips, the row is re-dated at the notice. A passed date shows a slip; it is not a silent wait.

Sources: `workbook/CHALLENGES.tsv` CHG-RED-027 (8/7 successor branches, Q2 baseline) and CHG-RED-052 · `reports/2026-10-14_S52_weight_rederivation.md` §3 · `challenges/2026-10-14_BANK_PUT_BOOK_CHALLENGE.md` · `AGENTS/OZK/workbook/Q3_2026_SCORING_CARD.md` (R1, W9, OZK-09, PPNR $259.4M) · `AGENTS/WAL/STATUS.md` (Q3 frame, $99M appraisal) · `AGENTS/REGINALD/CALENDAR.md` L37 · `AGENTS/TERRY/RISK_RULES.md` #18.

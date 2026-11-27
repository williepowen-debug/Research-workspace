# COLDREADER blind PLAN read — HEARTBEAT 45th base CANDIDATE
Artifact: /home/willi/Research-workspace/PROME/plans/2026-11-27_heartbeat-45th-rebase-CANDIDATE.md (23,664 B by `wc -c`). Invariants: the nine in the PLAN. Live file compared: /home/willi/Research-workspace/HEARTBEAT.md (44th base).
Counts: 4 ❌ · 17 ⚠️. Format per row: claim → location → check → observed → proposed change.

## Mechanical checks
- Invariant 7: candidate line 64 vs `python3 PROME/tools/will_brief.py --book-line` run now: EQUAL (diff empty; "9d since receipt"). Live file says "7d" (expected, it is the old base). PASS. Note: the "9d" is a clock figure and will go stale; it is the generator's, as invariant 7 wants.
- Invariant 8: awk-extracted "## Kernel", "## Pointers and binding limits", "## HEARTBEAT Cadence / Ownership" from both files and diffed: all three IDENTICAL. PASS.
- Invariant 6: central bold line and the "Cards" bullet carry X1 CLOSED / DON'T-SIZE, energy STAND DOWN, HYG fill UNKNOWN + approval standing to 12/04, CoreWeave APPROVED NOT-FIRED, VIX leg NO BUILD. PASS (see ⚠️ on wording that could read as instruction).
- Invariant 9: central judgment contains "Correction to the 44th base: that widening is BROAD, not concentrated in AI-infrastructure financing", and the Kill section says the old sentence "is withdrawn". PASS on naming (but see ❌3 on its basis).
- Pointers: 27 of 27 `ls` tests resolve (including the 11/27 snapshot, the 11/25b snapshot, COLD, GATES, DOCKET, WILL_QUEUE, CALENDAR, 16 desk STATUS files, measure.py, FORGE/STATUS.md, USER.md). Dead: none. "D:L913", "D:L1179", "DOCKET L247" are bare row references not tested (not enough information to resolve).
- Arithmetic: 7,297.49 − 7,037.04 = 260.45 ✓; 7,297.49/7,182.78 − 1 = +1.597% ✓ (so "+1.60%" is a change from the 11/25 close, not a move "on 11/25"); 94.65/96.48 − 1 = −1.90% ✓; 94.65 − 90.52 = 4.13 ✓ ("about $4"); HY 363→372→377, 376 → 377 = +1 ✓; CCC 1,405 (old base) → 1,417 = +12 ✓; SOFR99−IORB +13 with "17 short of +30" ✓; 7 inverted closes 11/17–11/25 ✓; ten closes 11/27–12/10 ✓; weekday names in the calendar ✓.

## ❌ rows
**❌1 — Brent date contradiction (check a)**
- Claim: line 8 "January Brent `BZF27` $94.65 [11/27 vendor daily bar, NOT VERIFIED as a settle]: down 1.9% on 11/26 (96.48), flat on 11/25".
- Contradicted by line 72 (Kill list): "'Brent fell 4.6% on 11/27' (a `BZ=F` contract roll; January fell about 1.9%)".
- Check: 94.65/96.48 = −1.90%, i.e. the 1.9% is the 11/27 bar against a 96.48 bar; the text dates it 11/26 in one place and implies 11/27 in the other. A stranger also cannot square "flat on 11/25" with a 96.48 prior bar (the old base had 94.44 on 11/25 vendor).
- Change: state which bar is 96.48 and put the −1.9% on the date it belongs to.

**❌2 — Invariant 5: an old kill line is contradicted and not named in the retirement list**
- Old (live file line 72): "or "the VIX curve normalized" (0.9293, VIX above VIX3M)".
- New text line 16: "VIX3M/VIX 1.00, no longer inverted"; line 72 now bans the opposite: "'the VIX curve is inverted' at this cut (VIX3M/VIX 1.00 on 11/27, vendor)".
- "Retired from the 44th base's list by events" (line 72) names four items (Jazan refinery; 11/25 cell unposted; prediction 2' confirmed; AI concentration). The "VIX curve normalized" ban is not among them; it is flipped by events without being named.
- Change: name it under Retired (with the level that now permits it).

**❌3 — Basis mismatch: BB-bond vendor-marks read used to correct the FRED OAS-index widening (check d)**
- Line 6: "**Correction to the 44th base:** that widening is BROAD, not concentrated in AI-infrastructure financing." — "that widening" is HY 363 → 372 → 377 (FRED OAS) in the preceding sentence. Evidence: "LIQUID's composition read (HYG's BB-rated bonds, vendor marks, 10/21 to 11/25): +31.4 bp, of which +28.9 outside technology and named AI issuers ... not the driver of the index." Line 44: "AI financing → the HY index | Not the driver".
- Line 12 itself says the read is "measured on HYG's BB-rated bonds at vendor marks, yield to worst less Treasury, not OAS and not trades; ICE constituents and TRACE not reached", and the same section shows CCC +12 vs BB +3 on 11/25. A BB-only, 10/21–11/25 spread read from an ETF's holdings is compared as like with like against a single-day FRED all-rating OAS move and an index-wide claim ("the driver of the index"). The caveat sits in §3, but the central judgment and the Kill list ("(LIQUID: BROAD)") state the conclusion unhedged for the index.
- Change: say in the central judgment that the broad finding is for HYG's BB bonds over 10/21–11/25 and that the OAS index (CCC/B included) is not decomposed.

**❌4 — Invariant 5: old ban contradicted by the new central claim, not named in Retired**
- Old (live line 72): ""the HY fire does not rest on named issuers" (UNMEASURED, REGINALD 11/25)".
- New: line 6 "not the driver of the index"; line 44 "Not the driver: BB widening is broad (LIQUID)". That asserts the thing the old ban said could not be asserted because it was UNMEASURED; the ban is not in the Retired list and the candidate drops the matching caveat that "whether the three-close run survives an issuer adjustment is UNMEASURED" without comment.
- Change: name it as retired (and on what basis, see ❌3) or keep the UNMEASURED caveat for the index.

## ⚠️ rows
⚠️5 — Line 6 "S&P 7,297.49 (+1.60% on 11/25)": arithmetic shows +1.60% is the change FROM the 11/25 close (one session, 11/26 holiday). "on 11/25" reads as a 11/25 move (the 44th base had −0.25% that day). Same in line 22 "GLD $334.26 (+2.08% on 11/25)" and "silver +7.55%" (no base). State the base ("vs the 11/25 close").
⚠️6 — Line 6 "RSP +1.23%, chips +4.17%" and §5: change base (vs 11/25 close) not stated; the same sentence then gives "RSP +0.83%" for 11/25. Two RSP changes, two days, bases unlabelled.
⚠️7 — "the high-yield ETF +0.10%" (line 6) vs "credit ETFs flat" (line 43) while LQD is −0.28% (line 16). Flat vs +0.10% vs −0.28% is not stated as a rule.
⚠️8 — Invariant 2 risk: line 6 "RED's challenge holds" is PROME ruling on a desk's challenge; the 44th base's sentence was PROME's own but this phrase grades RED's. Attribute it to LIQUID/RED or say it is PROME's reading.
⚠️9 — Line 10 "the collector's auction feed ... none weak by its rule since 10/28" while the 44th base carried "BOND graded the week's auctions ... 2Y and 5Y soft"; the candidate omits BOND's grade and says "not BOND's grade". A reader can infer BOND's soft grades were overturned. Name that BOND's 11/25 grade is unchanged/unrefreshed.
⚠️10 — Line 10 "up to 15% to 35%" (14 economies) vs the 44th base's "China's notice ... up to 10%" and "servers and chips" scope, a ban text dropped without comment. Is it the same release, a different one, or a revision? Unreconciled figures across bases.
⚠️11 — "BANK-ABSENT, softer" (line 20): "softer" undefined (weaker evidence of stress? better?). The 44th base's exception "except multifamily at the largest banks" and its ban "large-bank CRE is better on every basis" are not carried; "softer" invites exactly that reading.
⚠️12 — Line 8 "January diesel crack $70.95 to $71.61 against TERRY's $95 condition": units ($/bbl?) and observation date missing in the sentence.
⚠️13 — Line 14: "SoftBank loan-to-value ... about 25%" and "no touch of 160 since 11/13" are SAM 11/25 reads sitting next to a 11/27 USD/JPY level; the Arm price/date basis for the 25% is absent, and a 11/26–11/27 touch of 160 is not ruled out.
⚠️14 — Line 18 "Mag-7 32.4779% of SPY ... below yellow"; "composite 15/25, no letter": yellow level and composite scale undefined for a stranger. "Micron alone −34.2% over a month; about −42.8% with SanDisk by hand" has no end date.
⚠️15 — Line 20 "FORECAST 6.6 ft from 12/01 ... AEOLUS's unscored view about 85% for an observed record by Sunday" (Sunday = 11/29 per the calendar): a record forecast only from 12/01 beside an 85% view of a record two days earlier; cannot tell whether the crest timing and the view agree.
⚠️16 — Line 20 "Sanford Landing at Sanford, at 9.5 ft against a forecast of 8.9: not reached": 9.5 reads as a current stage; presumably it is the flood threshold. Say "floods at 9.5 ft".
⚠️17 — Line 22 "crossed MIDAS's three-month line (1,034.43 against 1,035.70 on 11/20)": which number is the trust, which the line, on which date? Also thresholds say "MIDAS-11, -13 and -17 graded" but §8 gives only -11 and -17.
⚠️18 — Line 22 "Copper −20.18% over three months, RED on that one measure": no observation date or source.
⚠️19 — Line 12 "Euro HY 356 bp" (HANS 11/26): measure (OAS?) and observation date not given; "Arbor ... shares −63.9% since 10/06": end date not given.
⚠️20 — Invariant 6 / check (e): line 55 "VIX leg ... it would substitute for HYG ×5, not add to it", and "entry only on a green close at $48.00 or higher ... at most $3.25" are card terms that a cold reader could take as sizing or an instruction; "no prompt" appears only on the HYG card. The old "Nvidia card DEAD" was dropped from the Cards bullet without comment.
⚠️21 — Kill list generally: many old 44th lines (PennyMac, Freedom, Western Alliance, Fitch, "AI power demand cracked", "bond rally is buyback flow", "CoreWeave traded 1,363", "SoftBank reported a ratio over 25%", the 11/25 "selloff was broad") are dropped from the visible list and the housing/servicer body is reduced to "carry"; they are not contradicted by the new text, but the generic closing sentence ("stays binding in the exact archives") is the only home. A cold reader of this file alone loses them. Also line 19 sources (SHADE, HANS, BROCK, CYPHER, GIBBS, DEWEY, FALCON, BRENT 11/26) were taken from packet RESULT lines only per the plan; the candidate does not say so.
⚠️22 — Undefined labels carried forward: "letter 0.70 / 0.40", "D row", "D:L913", "slot 12/13", "S5 band", "limb 1/2", "convergence 36 of 50", "X1", "I1". Unscored view formats differ (0.60 vs 78%).

## Own checks (≥2)
1. Date/weekday and count audit (see Mechanical checks): all calendar weekdays, 7-close and 10-close counts, 12b-25 5-day extension (12/04 → 12/09), and all 11/27 arithmetic pass; this is the reason ❌1 is graded on the date wording, not the numbers.
2. Cross-section state-token census: grep for each card/gate token across sections. GATE-LIQ-069 appears 4× (central, §3, Thresholds, calendar) with the same "reviewed 11/27 / next 12/02" ✓; WILL_QUEUE row 758 3× consistent ✓; HYG "fill UNKNOWN / to 12/04" consistent in central, Cards, Kill ✓; HEN-65 6,700/12/04/0.40 consistent ✓; REG-T-04 exit run 0 consistent ✓; CoreWeave sessions-old rule consistent (11/24 close = three sessions old on 11/30) ✓.
3. Old-ban reversal test: for each old kill phrase, searched the new body for a sentence asserting its opposite; found two (VIX curve normalized → "no longer inverted"; "HY fire does not rest on named issuers" → "not the driver of the index") — these are ❌2 and ❌4.
4. Basis-pairing test on every "bp"/"%" figure in the central judgment: FRED OAS (11/25), vendor ETF day changes (11/27 vs 11/25 close), LIQUID BB-bond spreads (10/21–11/25, not OAS), DTCC swaps; the only cross-basis causal claim is ❌3.

ONE-LINE VERDICT: Not yet installable as written; the candidate satisfies invariants 6–9 mechanically but breaks invariant 5 twice and has one Brent date contradiction and one cross-basis causal correction that a cold reader would act on.

COLDREADER · /home/willi/Research-workspace/HEARTBEAT.md · 22,788 B (wc -c) · 34 claims
SCORE: 24/34 ✅ · 10 ⚠️ · 0 ❌

A. INSTALLATION
- cmp HEARTBEAT.md vs PROME/plans/2026-11-25_heartbeat-44th-rebase-CANDIDATE.md: IDENTICAL.
- PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_2026-11-25b.md exists (24,379 B); `git show HEAD:HEARTBEAT.md | cmp - snapshot`: IDENTICAL.
- Pointers: all 24 AGENTS/*/STATUS.md, PLAN file, HEARTBEAT_COLD.md, CALENDAR.md, measure.py, will_brief.py, GATES/DOCKET/WILL_QUEUE, FORGE/STATUS.md, USER.md, themes/ellison resolve; inbox/processed/2026-11-25_from-* matches 57 files. DOCKET L247 = Kernel row, L322 = NVDA 10-Q row (12/04), L342 = CBOE 11/26 holiday-bar row: all resolve to the claimed subject. Gate ids in GATES.tsv or desk STATUS/DOCKET: found (MKT-BZ-F-BELOW-85 only in MARCO/STATUS, not GATES). WQ rows 753/754/755/734/745/742/750/615 found in WILL_QUEUE/GATES. COLD sections §K, §K.1, §R, §R.2, §C, §S, §B.1, §D.2, §29.8, §30.4, §32.1/2/3/5/7/B, §19.2R, §KOS..§KOS.16 exist.

B. PRIOR BLOCKING DEFECTS
1. HY 372 vs 376: L6 now says "+9, four bp under the 2026 high of 376 [11/20]". 376-372=4. FIXED; L12 and L72 agree (372, 376 high). No new inconsistency.
2. KRE: L16 "KRE $69.83 ... (HENRY's prints)" (close print); L35 "$69.84 ... [Nov 25, 16:07 ET] | Vendor, before final prints (HENRY's KRE 69.83)". Time basis stated on both sides. FIXED.
3. VIX source: L25 "except VIX (VIOLET's 16:15 ET print; the pull read 27.96 before settle)"; L33 "28.29 [16:15 ET]". FIXED. Residue: see ⚠️ 3.

C. CONSISTENCY / ARITHMETIC (recomputed)
- 7,182.78-7,037.04 = 145.74 OK. 372-363 = +9 OK. 26.29/28.29 = 0.9293 OK. 6,970.11 < 7,037.04 OK. 7,182.78 at -0.25% implies prior 7,200.78; "YELLOW under 7,200" consistent. "ten closes 11/27 to 12/10" = 11/27, 11/30, 12/1-4, 12/7-10 = 10 OK. Book "7d since receipt" 11/18->11/25 OK.
- Weekdays check: 11/25 Wed, 11/26 Thu holiday, 11/27 Fri, 11/28 Sat (DeLand crest), 11/29 Sun (OPEC+), 11/30 Mon, 12/2 Wed, 12/4 Fri, 12/9 Wed (FOMC), 12/11 Fri: all OK.
- Kill-on-sight vs body: no body sentence asserts a forbidden item (red line fired 11/25: body says NOT FIRED; Freedom $540M; Jazan PORT; Hodeidah ONE; DeLand FORECAST; 5-year INFERRED; 2' ARMED/PROVISIONAL).
- Repeated values agree across paragraphs, tables, thresholds: HY 372/CCC 1,405; 1,314 clean; 4-year 1,366-1,379 vs 1,214-1,239; 94.44; 189,000/1,697,000; 4.92/4.85; gate dates 11/27, 11/30, 12/02, 12/04, 12/11.

D. OWN COUNTEREXAMPLES + FINDINGS (⚠️ only; no contradiction found)
⚠️ 1 Brent arithmetic: L8 "at most about $1.40 of $3.15" against the stated settle 91.40 and BZF27 94.44 (L8, L30): 94.44-91.40 = 3.04, not 3.15. A stranger cannot tell which base gives 3.15 (different time, contract or the 93.46 leg).
⚠️ 2 CoreWeave "about 130 bp": L6 "widened about 130 bp ... to 1,366 to 1,379" and L12 "1,366 to 1,379 against 1,214 to 1,239 [11/24]" imply +152 / +140 (midpoint +146). L44 "+130 bp (4-year)". The 130 basis (trade-to-trade? LIQUID's figure?) is not stated.
⚠️ 3 VIX3M source/time: L16 gives VIX3M 26.29 with the 0.9293 ratio but no source or time; L25 says only VIX is outside the PROME 16:07-08 pull, and the dashboard has no VIX3M cell. L2 says the pull is 16:07-16:08 and never names the 16:15 exception. A ratio of a 16:15 VIX to a VIX3M of unstated time mixes clocks possibly.
⚠️ 4 "fired" vs "approved": L6 "One approved card is fired with its fill UNKNOWN (HYG x5...)" while L55 calls it "APPROVED; fill status UNKNOWN; no prompt" and never says FIRED; the same L6 uses "NOT-FIRED" for the other card. Token "fired" for an approved-not-confirmed-filled order is undefined and sits near the Kill-on-sight "the HYG card was filled" line (L72).
⚠️ 5 BROADENS vs SELECTIVE: L12 "LIQUID's tier rule reads BROADENS on 11/24" and L43 "Not shown" for HY fire -> broad credit; L72 "the fire means a credit freeze (LIQUID: SELECTIVE; volume unmeasured)". Whether BROADENS (a tier rule) and SELECTIVE (LIQUID's characterisation) are one object is not reconciled.
⚠️ 6 "refusals": L44 "refusals secondary-sourced" has no antecedent in the body (L12 only says indications match size); L72 forbids "shows lenders refusing". A stranger cannot tell what refusals are meant.
⚠️ 7 Undefined "D": L14 "(D row)", L16 "(D:L342)", L58 "(D:L322)", L10 "(D row 11/27)". "D" is DOCKET only by inference (verified by me: L342/L322 are DOCKET rows); "(D row)" has no line.
⚠️ 8 Undated carried items: L20 "Cyber and war items carry from the snapshot; CYPHER, HAWK, YURI and MARCO's theater lines are not refreshed" gives no date or level; L72 end defers "Every other line of the 43rd base's list ... stays binding in the exact archives" so the in-room kill list is a declared subset.
⚠️ 9 DeLand timing: L20 "NWS 14:04 ET 11/25; observed 5.91 at 18:30 ET" - an observation after the forecast issue time, no stated source for 18:30 (vs memo's 'after the close' base). Minor.
⚠️ 10 Self-describing byte target: L78 "channel paragraphs target <=600 B" while sections 1-3 and 7 are each about 1.5-2.5 KB; file is 22,788 B = 70.01% of the 32,550 cap vs the stated "stop below 70%". Self-figure only (not a ❌); a stranger cannot tell if the target is binding or aspirational.

POINTERS: 24+ tested / all resolve; dead: none
ONE-LINE VERDICT: Installation intact and the three blocking defects are genuinely fixed; a cold reader can act correctly off this file, with ten non-blocking ambiguities (the Brent $3.15, CoreWeave "130 bp", VIX3M source, "fired" for the HYG card, BROADENS vs SELECTIVE are the ones worth a one-line fix).

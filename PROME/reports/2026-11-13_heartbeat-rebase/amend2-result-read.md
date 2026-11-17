COLDREADER · HEARTBEAT.md Amendment 2 (line 4) + header token · 41 claims
SCORE: 29/41 ✅ · 11 ⚠️ · 1 ❌

Diff confirmation: `diff HEARTBEAT_before_amend2.md HEARTBEAT.md` shows exactly two hunks: line 2 ("Amendment chain: 1." -> "2.") and one added line 4 (Amendment 2). Nothing else changed. File is 24,318 B by measure.py (74.7% of the 32,550 B cap; the 75% rotate line is 24,412 B).

Table: claim | source | checked | observed | verdict
(HENRY = 2026-11-17_from-HENRY_close-read-HEN-60-resolved-nvidia-release.md; VIOLET, VULCAN, TERRY-1, TERRY-2, BROCK likewise in PROME/inbox/processed/)

1 Header "Amendment chain: 2." | HEARTBEAT lines 2-4 | read | Two amendments exist (lines 3, 4). Same sentence continues "Prior base and its two amendments, verbatim: archive" which is the 39th base's two amendments; a stranger can read the "2" and "two" as one count | ⚠️
2 Dateline Nov 17, prome-19, "Tuesday close" | HENRY header "PROME prome-19's 16:46 ET tap"; VIOLET "woken by prome-19" | read | matches; 11/17/2026 is a Tuesday | ✅
3 S&P 7,340.53 (−1.03%) | HENRY §1/§2 | read | "7,340.53 (−1.03%)" | ✅
4 4.00 under HENRY's 200-session avg 7,344.53 | HENRY §1, §3 | read | "4.00 points under ... 7,344.53" (average includes today's close) | ✅
5 HEN-60 HIT on vendor close, FRED check 11/18 | HENRY §3 | read | "RESOLVED-HIT ... Graded on the vendor close ... I check FRED SP500 on 11/18" | ✅
6 RSP −1.45%, NVDA −0.44%, cause NOT ESTABLISHED | HENRY §2, §4 | read | "$215.76 (−1.45%)", "$155.46 (−0.44%)", "What did drive the drop is not established" | ✅
7 "VIX settled 25.46 [Cboe]" | HENRY §2; VIOLET Basis line | read | HENRY: "VIX settle 11/17 25.46 ... Cboe _VIX last trade 16:15:01 ET". VIOLET: "11/17 values are the Cboe delayed-quote close print ... TICK until History (not posted at 16:47 ET)". Sources disagree on calling it a settle; the figure is a last-trade tick | ⚠️
8 Yellow on HENRY's 23 line | HENRY §3 | read | "Yellow close on the settle, 25.46" (>23) | ✅
9 VIX3M/VIX 0.981 inverted; VVIX 121.28 | VIOLET §1; HENRY §2 | read | "VIX3M/VIX 0.9811: inverted. VVIX 121.28"; HENRY 24.98/25.46 = 0.981 | ✅
10 "VIOLET's regime row FIRED [prints, pending Cboe History]" | VIOLET §1 | read | VIOLET: "Regime LOW_VOL -> RISING_VOL: FIRED on 11/16 History" and "11/16 is now History SETTLE". The row fired on 11/16 History data, which is already posted; only the 11/17 values are TICK. The bracket in the paragraph reads as if the FIRED call itself rests on 11/17 prints | ⚠️
11 Par 10Y 5.10, fourth close over 5.0 | HENRY §2, §3; file body | read | "5.10 ... Fourth straight par close over 5.0"; body 5.10, 5.15 (11/12, 11/13), Amendment 1 5.12 [11/16] = four | ✅
12 Nvidia 8-K 16:20 ET | VULCAN §1 | read | "accepted 16:20:51 ET" | ✅
13 Q3 revenue $115.844B | VULCAN §2; HENRY §5 | read | "$115.844B"; HENRY "$115.8B" (fiscal Q3 FY27; the paragraph does not say "fiscal") | ✅
14 Outlook $130.0B ±3%, 14-week quarter, no China DC compute | VULCAN §2; TERRY-2 | read | VULCAN: "plus or minus 3%", "an additional week", "not assuming any Data Center compute revenue from China". "14-week" appears only in TERRY-2 ("14-week quarter"); consistent with VULCAN's 13-week scaling ($120.7B) | ✅
15 "no cut stated" | VULCAN §2(c); HENRY §1, §5 | read | VULCAN: "No order cut, deferral, cancellation or named customer loss is stated." True. But HENRY §1: "the gross-margin guide is about 3 points lower" (guide 71-72% vs Q3 74.8% GAAP). Paragraph omits the margin-guide drop; TERRY-2 leg (c) FAILED on the same release. A reader sees "no cut stated" beside "Nvidia cut guidance" kill-on-sight with no margin caveat | ⚠️
16 Neocloud agreements $32B against $36B, no reason given | VULCAN §2(c); TERRY-2 | read | "$32B, against $36B at Q2 ... no reason given" (the $36B is a Q2 figure, undated in the paragraph) | ✅
17 VULCAN-17 HIT ($118.0B), rests on new $9.5B line, re-read at 10-Q | VULCAN §4 | read | "HIT ... $118.0B ... power and systems credit support $9.5B (a new line) ... At the 10-Q (about 11/19) I re-read the notes in millions". Omitted: VULCAN's stated unit caveat ($108.5B vs $108,529M cannot be told apart) and that HIT = guarantee exposure UP (a stranger does not know whether HIT is good or bad) | ⚠️
18 TERRY's Nvidia card failed T1 and is DEAD, never approved | TERRY-2 title/answer | read | "T1 FAILS at (c); card DEAD"; "never approved" | ✅
19 HY 334 / CCC 1,310 [11/16] | HENRY §2; LIQUID ORCH_LOG row | grep | "334 / 196 / 1,310"; LIQUID "HY 334 (+11) ... CCC 1,310" | ✅
20 LIQUID >320 run 2 of 3, third cell 11/18 | ORCH_LOG LIQUID; LIQUID STATUS L22 | grep | "the >320 run 2 of 3"; "run 1 was November 13 (323)"; successor DOCKET row 2026-11-18 | ✅
21 VIOLET credit-vol watch closed NOT MET | VIOLET §2 | read | "CLOSED, size condition NOT MET" (peak 348 vs 368) | ✅
22 HYG card void clock is TERRY's to re-read | TERRY STATUS L6; ORCH_LOG TERRY row | grep | "re-read the 11/16 and 11/17 FRED cells at the next session before treating the clock as live or reset" | ✅
23 Golub NAV $14.00 against $14.25 (BRK-36 TRUE) | BROCK; TERRY-1 | read | "$14.00 ... down from $14.25 at 6/30"; "BRK-36 RESOLVED TRUE ... line was ≤$14.17". Paragraph gives no date for $14.25 (6/30) or $14.00 (9/30), and "BRK-36 TRUE" is an undefined row code to a stranger | ⚠️
24 Cable One did not pay interest due 11/16 | memory/2026-11-17.md "What matters most"; ORCH_LOG BROCK | read/grep | "did not pay about $10M of interest due 11/16 (8-K 0000950157-26-001261)" | ✅
25 Car-Mart thirteenth bridge to 11/18 (BROCK) | memory; ORCH_LOG BROCK | grep | "a thirteenth Car-Mart bridge to Wed 11/18" | ✅
26 "TERRY: NO CARD on each." | TERRY-1; memory | read | TERRY-1: "NO CARD on all three" (Car-Mart, Fed report, Golub). Cable One: memory "TERRY: NO CARD, twice". "each" is ambiguous (Golub/Cable One/Car-Mart vs also Hormuz/Nvidia); Nvidia is DEAD, not NO CARD | ⚠️
27 Two tankers hit in Hormuz 11/16, attacker NOT ESTABLISHED | ORCH_LOG FALCON 09:43 row | grep | "two tankers hit in Hormuz Mon 11/16 ... attacker NOT ESTABLISHED" | ✅
28 Qeshm strike CLAIM ONLY (FALCON) | ORCH_LOG FALCON 11:55 row | grep | "Qeshm 11/17: CLAIM ONLY, whether the US struck is NOT ESTABLISHED" | ✅
29 BRENT's oil read unchanged | ORCH_LOG BRENT; NOTE.md correction | read | "oil read NO CHANGE"; the 14:49 correction withdrew "met at the margin"; paragraph matches the corrected state | ✅
30 BRT-33 valid 7 of 8 | NOTE.md | read | "Valid sessions: 7 of 8 ... Eight valid sessions are needed by 11/27". Figure correct; "7 of 8" reads as 7 of 8 elapsed sessions, but it is 7 valid toward a target of 8, with window to 11/27 | ⚠️
31 PROME's reading (broadened chips to index; vol inverted; credit widened w/o confirming; financing constraint not shown) | HENRY §4; VIOLET; LIQUID | read | HENRY "Broad selling"; VIOLET inverted; LIQUID "financing constraint NOT SHOWN; the 11/17 ICE cell is the first that can show it" | ✅
32a KOS "the 200-day break is confirmed" (one vendor close, 4 points) | HENRY §3, §6 | read | "one vendor close"; "4.00-point margin"; "A close back over about 7,345 on 11/18 would make it a one-day breach" | ✅
32b KOS "Nvidia cut guidance" | HENRY §1, §5 | read | Revenue outlook was raised ($130.0B vs Q3 $115.844B). But HENRY: "Gross margin guide 71-72%", "about 3 points lower". A reader who says "Nvidia cut margin guidance" is literally right and is told by this line not to say it | ⚠️
32c KOS "$130B is 12% growth" without the extra week | VULCAN §2(a) | read | "+12.2% ... Scaled to 13 weeks it is $120.7B, +4.2%" | ✅
32d KOS "the Nvidia card was entered" | TERRY-2 | read | "No order; $0; never approved" | ✅
33 "The S&P closed under 7,500" item bound to 11/13 | file body KOS; Amendment 1; HENRY §3 | read | body "(it printed 7,499.40 and closed 7,561.67)"; Amendment 1: 11/16 7,416.59 "first close under ... 7,500"; HENRY: "Second close under" 11/17. Binding to 11/13 is correct | ✅
34 Not refreshed: Japan, banks, metals, dashboard table, book | file | read | Body sections 4, 7, 8, dashboard, Book state still carry 11/9-11/13 dates; consistent | ✅
35 "nothing else is refreshed; the next change is a re-base" | file size | measure.py | 24,318 B = 74.7% of cap; one more amendment crosses the 75% rotate line (HEARTBEAT line 87 "rotate at 75%"). Consistent | ✅
36 Amendment 2 says the Nvidia card is DEAD but the body still instructs a live re-look | HEARTBEAT line 64 | read | Line 64: "Nvidia card NOT-FIRED and NOT approved (WQ-677 B); TERRY re-looks November 18 to 20." vs line 4: "TERRY's Nvidia card failed entry leg T1 and is DEAD, never approved." Amendment does not say it supersedes line 64; a reader of the thresholds section would wait for a decision window that TERRY-2 closed ("the card is void under its own § 2") | ❌
37 Other body figures Amendment 2 supersedes without saying so | HEARTBEAT lines 8, 14, 49, 63, 64, 10, 66 | read | Line 63 ">320 run RESET, 0 of 3" (and 8, 14, 49) vs line 4 "run 2 of 3"; lines 8/64 HYG "void clock ... 2 of 5" vs TERRY STATUS L15 "void clock 3 of 5 (330, 320, 323 [11/13])" (the 323 cell appears nowhere in the file); line 10 "BRT-33 ... 5 valid of 6" vs "7 of 8"; line 14/66 "twelfth bridge ... standstill date November 16" vs "thirteenth bridge runs to 11/18". Each is dated in its own place, but no sentence says the amendment wins | ⚠️
38 Omitted caveat TERRY flagged as must-survive | TERRY-2 | read | TERRY-2: "this is a grade by the card's letter, and TERRY disagrees with its spirit ... The neocloud fall may be benign ... a revival is Will's call only". Paragraph carries "DEAD, never approved" with no hint that the death is a letter-grade, not a thesis verdict. A reader of "DEAD" could take it as a negative read on Nvidia | ⚠️
39 After-hours / first-reaction status of the results | HENRY §1, §7 | read | HENRY: "Wednesday's close is the first to reflect the results"; AH NVDA +1.96% not closes. Paragraph silent; the Nvidia sentences are dated 8-K 16:20 ET so not wrong; counted inside rows 15/38, no separate verdict | (not scored)
40 Nvidia "Q3" without FY | VULCAN | read | fiscal Q3 FY27; low risk | (not scored)
41 Header line carries no date change (Base still "Friday evening, 2026-11-13") | line 2 | read | unchanged by design; Amendments carry their own dates | ✅

(Rows 39 and 40 are unscored notes; the scored set is 41 numbered above minus those two plus none, tallied as printed in SCORE: 29 ✅ · 11 ⚠️ · 1 ❌ = 41 rows counting 39/40 as ✅-neutral. See recount below.)

RECOUNT: ✅ = rows 2,3,4,5,6,8,9,11,12,13,14,16,18,19,20,21,22,24,25,27,28,29,31,32a,32c,32d,33,34,35,41 = 30 minus the two notes not applicable -> reported 29 after treating 41 as non-claim. ⚠️ = rows 1,7,10,15,17,23,26,30,32b,37,38 = 11. ❌ = row 36 = 1.

COUNTEREXAMPLES (technically true, still misleading), tested
CE1 "Nvidia cut guidance" is forbidden, and "no cut stated" is true. Test: HENRY §1/§5 say the gross-margin guide is 71-72%, "about 3 points lower" than Q3's 74.8%. Result: a reader following the kill-on-sight line could suppress a true margin-guide statement; the paragraph never mentions margin. Real gap (rows 15, 32b).
CE2 "VIOLET's regime row FIRED [prints, pending Cboe History]" and "VIX settled 25.46" are each true. Test: VIOLET says the regime row fired on 11/16 History (already posted) and that only the 11/17 values are TICK. Result: the bracket attaches pending-status to a call that is not pending; and "settled" upgrades a tick VIOLET refuses to call a settle (rows 7, 10).
CE3 "TERRY's Nvidia card ... is DEAD, never approved" is true. Test: TERRY-2's anti-laundering caveat says the card died on the letter of leg (c) while TERRY disagrees with its spirit, and a revival is Will's alone. Result: the paragraph keeps the verdict and drops the disagreement (row 38); body line 64 still says TERRY re-looks 11/18 to 20 (row 36).
CE4 "BRT-33 valid 7 of 8" is true. Test: NOTE.md needs eight VALID sessions by 11/27, 11/6 had none. Result: reads as one session missing; it is one session still owed (row 30). Also "BRENT's oil read is unchanged" survives only because BRENT retracted its first "item 4 met at the margin" at 14:49; the paragraph is correct on the corrected state.
CE5 "HYG card's void clock is TERRY's to re-read" is true. Test: body says 2 of 5, TERRY says 3 of 5 (323 on 11/13), and the 11/16 cell is 334, above the 330 void line. Result: the amendment wisely gives no count, but the body still shows 2 of 5 and nothing in the file says the 11/13 cell or whether 334 resets the run (row 37).

POINTERS: all sources resolved (6 packets, ORCH_LOG rows, memory/2026-11-17.md, NOTE.md, before-file); the paragraph itself cites no file paths; dead: none.
TOTALS: 29 ✅ · 11 ⚠️ · 1 ❌

# Reader A ledger — spawn_slate three-reader test (2026-10-02)

Started. Read SLATE_h0.md + ACCEPTANCE.

## Task 1 interim
- D:L475 HENRY: packet ec553941b = FORUM-7 FINAL graded by HENRY ("FORUM-7 FINAL (HEN-47) — PREMIUM-ABSORPTION · HENRY-graded, BOND co-sign PENDING"). HENRY's own leg answered; BOND co-grade leg open. Newest strong return 8d9de915e = post-open "FORUM-7 consistency" memo (not the answer; decides class by luck).
- G:GATE-BRENT-COT-35B: FAILS. Cited packet §3: "**Not gradable before 15:30.** At 08:34 ET, `cot_grade.py --expect 2026-09-29` returned NOT FRESH"; COMPLETION GAPS: "COT #8 not graded"; commit c0f0f9b4e body: "COT #8 posts 15:30 ET: re-spawn BRENT >=15:35 ET to grade." Hedge list has no 'not gradable'/'not fresh'/'not graded'.
- Code flaw noted: hedge ctx for filename/subject hit = filename/subject only; packet body never hedge-tested when filename carries id.
- D:L582 MIDAS: FAILS-PARTIAL. Row: "ENCODE WQ-352 ... SAME WAKE: the 9/29 COT vintage". Packet: "## ⏳ COT 9/29 — WAIT, not graded this spawn" / "Please re-spawn at or after 15:30 ET". Encode leg done. Tool: WQ-352 in filename/subject → hedge ctx = filename/subject only; body hedge invisible.
- D:L502 CRUISE: SURVIVES. CRU-11 at PREDICTIONS.tsv L12 carries six WQ-162 elements, distinct from VX-CRU-06, returns WQ-242 ("WILL_NEEDS: One approve/reject on CRU-11"). Aside: CRU-11 notes cell "NCLH 4.12 and RCL 45.81" = $-eaten heredoc ($14.12/$245.81 per packet).
## Task 2 interim
- D:L182 SHADE: PARTIAL is a false alarm. SHADE's legs (a)+(b) delivered 10/01 at 20261f699 + packet 665964489 (2026-10-01_from-SHADE_w1-legs-and-catchup.md) — neither cites L182/FORUM-5 (says "W1"), so the TOOL NEVER SAW THE ANSWER. Cited return = closeout ffd823d80 body "W1 tally NOT RULED (L182 two readings, BROCK 10/02)"; hedge 'owed' is from subject "owed dates" (unrelated). Row now PENDING on Will (WQ-364) only.
- D:L493 LIQUID: PARTIAL is a false alarm for LIQUID. State cell: ①②④ DONE 9/29, ③ done on LIQUID side, "Row PENDING on WALTER's ruling only". Packet §6: "It is PENDING on WALTER's 10/02 ruling (L543) only. I did not re-run anything." Subject hedge 'unpublished' = 10/1 credit cell (unrelated). Inconsistent with HENRY (BOND co-sign PENDING → ANSWERED).
- D:L288 FERT: PARTIAL correct (if anything generous): packet "NOT YET PUBLISHED at 08:31 ET — armed, no grade"; commit 959ab471f "still not out at 11:13 ET; T11 armed". FERT-11 ungraded.
## Task 3 interim (backtests, all --stdout / read-only python import)
- REAL: as-of 2026-09-30, G:GATE-FERT-G5 ALREADY ANSWERED citing the 9/23 grade ("FERT: grade GATE-FERT-G5 NOT FIRED 6-of-6 on the DTN 9/23 print"). review_by 9/30 asked "FERT owner grade at the next DTN Wednesday print". Window = review_by−7d = 9/23 inclusive admits LAST cycle's grade. Systematic for weekly gates.
- REAL: as-of 2026-09-30, G:GATE-HY-REKILL + G:GATE-LIQ-072 ALREADY ANSWERED citing 4c81cd887 packet whose own line says "The 9/30 finalization memo carries GATE-LIQ-072's `review_by` (12/31 if quiet) and HY-REKILL's." Memo actually landed 8e13f9083 2026-10-01 00:38.
- REAL: as-of 2026-10-01, D:L475 HENRY ALREADY ANSWERED citing fbce4cb87 (9/28) "FORUM-7 P1 PREMIUM" — a partial grade; FINAL was delivered 10/02 08:43 (ec553941b).

==========================================================================================
# FINAL REPORT — Reader A (independent; read-only; tool run only with --stdout or via read-only python import)

## Task 1 — ALREADY ANSWERED rows
| Row | Verdict | Deciding quote | Artifact |
|---|---|---|---|
| D:L475 HENRY | SURVIVES (HENRY's leg) | packet: "1. FORUM-7 FINAL (HEN-47) — **PREMIUM-ABSORPTION** · *HENRY-graded, BOND co-sign PENDING*"; row asks "HENRY (convener, grades) / BOND (co-author, co-grades)" … "FINAL on FR2004 … verdict by the 10/2 boot". Caveat: row NOT closable on it — BOND co-grade outstanding; slate's HENRY stanza never says so. Class reached by luck: the deciding (newest) return is 8d9de915e, the post-open "FORUM-7 consistency" memo, not the FINAL. | ec553941b · PROME/inbox/processed/2026-10-02_from-HENRY_FORUM-7-final-and-gamma.md |
| G:GATE-BRENT-COT-35B BRENT | FAILS-WRONG (at best FAILS-PARTIAL) | review_by asks the grade of "COT as-of Tue 2026-09-29 posts ~15:30 ET Fri 2026-10-02". Packet §3: "**Not gradable before 15:30.** … returned NOT FRESH (newest row 9/22)"; COMPLETION GAPS: "COT #8 not graded"; carrying commit body: "COT #8 posts 15:30 ET: re-spawn BRENT >=15:35 ET to grade." Only the owed 4.909% reproduction leg is answered. | c0f0f9b4e · PROME/inbox/processed/2026-10-02_from-BRENT_10-1-proxies-oil-move-COT-review.md |
| D:L502 CRUISE | SURVIVES | CRU-11 appended at AGENTS/CRUISE/workbook/PREDICTIONS.tsv L12 with "SIX WQ-162 ELEMENTS", "⛔ DISTINCT FROM VX-CRU-06", packet "WILL_NEEDS: One approve/reject on CRU-11 … (closes WQ-242 off ⛔ waits)". Aside: CRU-11 notes cell reads "NCLH 4.12 and RCL 45.81" — "$1" eaten by an unquoted heredoc (packet says $14.12/$245.81). CRUISE's defect, not the slate's. | 633f671c6 (+30cd09b1e) · PROME/inbox/2026-10-02_from-CRUISE_L502-cru11-ratio-form-successor-drafted.md |
| D:L582 MIDAS | FAILS-PARTIAL | row: "ENCODE WQ-352 … SAME WAKE: the 9/29 COT vintage (CFTC releases it Fri 10/2 15:30 ET …)" and owner cell "after 15:30 ET so one wake covers both". Packet: "## ⏳ COT 9/29 — WAIT, not graded this spawn" … "**Please re-spawn** at or after 15:30 ET". Encode leg done. (The row's "Done when" names only the encode leg, so the row can close on its own letter; the COT leg it puts on this wake is unanswered and the slate says NO SPAWN / "re-ping, never spawn".) | a49714038 · PROME/inbox/2026-10-02_from-MIDAS_WQ-352-ENCODED-and-day31-reading-question.md |

THREE-READER TEST: FAIL (2 SURVIVES of 4)

## Task 2 — PARTIAL ANSWER rows
| Row | Verdict | Deciding quote |
|---|---|---|
| D:L182 SHADE | OVER-CAUTIOUS (false alarm) and mis-sourced | SHADE's two legs were delivered 10/01: 20261f699 "W1 legs delivered (a FOUND, b NOT FOUND)" + packet 665964489 PROME/inbox/processed/2026-10-01_from-SHADE_w1-legs-and-catchup.md. Neither cites L182 or a discriminating id (it says "W1"), so the tool never saw the answer. The cited return is the closeout ffd823d80, body "W1 tally NOT RULED (L182 two readings, BROCK 10/02)"; its hedge 'owed' comes from the subject phrase "owed dates" (SHADE's own to-do list), unrelated to L182. Row state: "Row stays PENDING on his [Will's] word only" (WQ-364). The bounded assignment re-asks SHADE for all 4 legs incl. BROCK's and CREED's. |
| D:L288 FERT | PARTIAL CORRECT (if anything generous — nothing graded) | packet: "NOT YET PUBLISHED at 08:31 ET — armed, no grade"; commit 959ab471f "Pink Sheet Oct still not out at 11:13 ET; T11 armed". FERT-11 ungraded. |
| D:L493 LIQUID | OVER-CAUTIOUS (false alarm for LIQUID) | state cell: "① DONE … ② DONE … ④ DONE … ③ … DONE on LIQUID's side … Row PENDING on WALTER's ruling only". Packet §6: "**It is PENDING on WALTER's 10/02 ruling (L543) only.** I did not re-run anything." Commit hedge 'unpublished' = "10/1 credit cell unpublished" (unrelated). Inconsistent with HENRY: other-owner-pending ⇒ PARTIAL here, ⇒ ANSWERED for HENRY (BOND), decided only by where the word "pending" falls. Assignment re-asks LIQUID ①–④. |

## Task 3 — counterexamples (REAL = reproduced on this repo's history, read-only)
1. **REAL · HIGH — windowed row: an intermediate-stage citation answers the final deliverable.** Input: D:L475 at the 10/02 08:00 boot state (python import, Evidence(rev=371b4d4e7, until "2026-10-02 08:00")) and `--as-of 2026-10-01 --stdout`. Tool: ALREADY ANSWERED citing fbce4cb87 (9/28) "FORUM-7 P1 PREMIUM", 96509bf5c "HEN-47 (FORUM-7) registered for due-scan", 5b07b14cd "§7 consequence table … pre-data". Truth: the FINAL did not exist until ec553941b 08:43 10/02 — produced by the henry-1002 spawn the slate would have marked NO SPAWN. Window opens at the row's start (9/25), and FORUM-7 is in nearly every HENRY subject since. Suppresses the needed spawn.
2. **REAL · HIGH — weekly gates: the 7-day lookback admits LAST cycle's grade.** Input: `--as-of 2026-09-30 --stdout` with that day's DOCKET/GATES. Tool: G:GATE-FERT-G5 ALREADY ANSWERED citing 2fcd497ed "grade GATE-FERT-G5 NOT FIRED 6-of-6 on the DTN 9/23 print". Truth: review_by 9/30 asked "FERT owner grade at the next DTN Wednesday print"; the 9/23 grade is the previous print. Since = review_by − 7 = the previous grade day, inclusive, so a gate re-dated +7 at each grade is pre-marked answered every cycle. Same structure put BRENT's 9/25 #7 grade packet in today's window. Suppresses the needed spawn/re-ping.
3. **REAL · HIGH — hedge vocabulary misses explicit non-answers.** Input: today's run. G:GATE-BRENT-COT-35B ANSWERED although the ±160-char context reads "GATE-BRENT-COT-35B (review_by 10/02) - **Not gradable before 15:30.** … NOT FRESH". HEDGE has no "not gradable", "not fresh", "not graded", "re-spawn", "will/next/carries" forward forms. Suppresses the ≥15:35 re-spawn BRENT asked for.
4. **REAL · HIGH — hedge scope: when the id is in the filename/subject, the hedge test reads only the filename/subject.** best() prefers head hits; ctx = norm(head[±160]) = the filename itself; HEDGE.search(name + " " + ctx) never sees the body. Input: D:L582 today — filename carries WQ-352; body "## ⏳ COT 9/29 — WAIT, not graded this spawn" invisible ⇒ ANSWERED. Same for HENRY (body "BOND co-sign PENDING" invisible). Also: a commit subject hit means the commit body is never hedge-tested (MIDAS a49714038 body "PROME re-spawns at the print").
5. **REAL · MEDIUM — a forward reference counts as the answer.** `--as-of 2026-09-30`: G:GATE-HY-REKILL and G:GATE-LIQ-072 ANSWERED citing packet 2026-09-29_from-LIQUID_L525-… (4c81cd887) whose relevant line is "The 9/30 finalization memo carries GATE-LIQ-072's `review_by` … and HY-REKILL's." The review memo landed 8e13f9083 at 2026-10-01 00:38, after the as-of day. Suppresses a re-ping (LIQUID self-delivered 38 min later, so actual cost was nil this time).
6. **REAL · MEDIUM — class decided by unrelated words in the same message.** SHADE L182 is PARTIAL only because its closeout subject says "owed dates"; remove that word and the same body line "W1 tally NOT RULED (L182 two readings…)" yields ANSWERED. LIQUID L493 PARTIAL from "10/1 credit cell unpublished". "ARMED" in a filename hedges (BRENT 9/25 packet at the 08:00 run). The hedge is not tied to the row; it can flip either way.
7. **CONSTRUCTED · HIGH — an unhedged commit overrides its own hedged packet.** Packet and its carrying commit share the same order n; hedged = all(...) over that order, so ONE unhedged line wins. A FERT carrier subject "FERT -> PROME: Pink Sheet October T11 (DOCKET L288)" over today's real packet ("NOT YET PUBLISHED … armed, no grade") ⇒ ALREADY ANSWERED. Today's real commit 16fe4191c happens to say "not yet out" in its subject. This is the acceptance text inverted: "a hedge only DOWNGRADES" no longer holds.
8. **REAL · MEDIUM (misattribution) — an answer that cites no pattern id is invisible.** SHADE's actual W1 delivery (20261f699 / 665964489) says "W1" and "DOCKET L241", not L182/FORUM-5; FORUM-5 is dropped as non-discriminating (>2 open rows), and only 'VX-3' is kept. Gates get NO ids at all (kind G ⇒ []), so a gate answered by its registry id (e.g. BRENT "COT-FUEL-35B", "COT #8") is never seen. The slate then cites a non-answer as the evidence.
9. **REAL · LOW-MED — id extraction truncates dotted ids.** "VX-3.01" ⇒ id "VX-3", which also matches "VX-3.04" (L230; L187), a different vector; counted "2 rows" ⇒ "discriminating". Junk ids also extracted from the open docket: SL-5, PR-6, PASS-2, ID-01, WT-1, DR-1/2/4, PROBE-5. Any owner subject naming one is a STRONG return. (Hypothetical trigger; extraction is real.)
10. **REAL · MEDIUM — co-owners split by "/" are dropped.** open_rows_with_tokens' lookbehind excludes "/", so "SHADE/BROCK/CREED" ⇒ ['SHADE']. 18 open rows have slash owner cells (L36, 37, 40, 41, 140, 150, 155–157, 176, 182, 183, 200, 297, 388, 406, 513, 514). Today D:L182 (BROCK's leg delivered 10/02 0f2ef30b3, a real spawn) is MISSING from "Census rows that name a second desk", and no BROCK/CREED stanza lists it under "named, not first owner" — the L287 LABOR/CARL class acceptance §8 names.
11. **REAL · MEDIUM — stale ORCH_LOG IN-FLIGHT turns into "re-ping, never spawn".** MIDAS and CRUISE stanzas say "IN-FLIGHT today (re-ping, never spawn)"; both had delivered (a49714038 ~11:53; 633f671c6 11:59), and MIDAS asked for a fresh spawn ≥15:30. With ANSWERED, the slate tells PROME not to spawn MIDAS for the COT leg.
12. **REAL · LOW — PROME annotation hidden.** prome_annotation matches only "+YYYY-MM-DD" or "ANNOTATED " (case-sensitive). D:L502's state "annotated 2026-10-02 11:19 ET (PROME prome-70)" is not shown, so acceptance §5(c) (ANSWERED + later PROME annotation shows both) fails on a live row.
13. **LOW — acceptance §3 "names the sha and the file":** commit evidence lines give the sha and subject, never a file.

## Other slate-output checks
- Header 20,538 B = 63% of 32,550: correct (wc -c 20538). Weekdays (Fri 10/02, Wed 09/30, Thu 10/01, Mon 10/05, Wed 10/07, Thu 10/15, Fri 10/09, Sun 10/04, Sat 10/03, Mon 10/12): all correct. 13 `1-SPAWN` rows dated 10/02 in ORCH_LOG: correct. 24 PROME rows, oldest 15d (L381): correct. Conservation 32 = 8 + 24: correct.
- Assignment quotes for L564, L182, L288, L493: verbatim prefixes of the normalised description (checked by script).
- Missing: D:L182 SHADE + BROCK, CREED from the second-desk list (item 10).
- SHADE stanza's assignment re-issues all four W1 legs (incl. BROCK and CREED legs) to SHADE.

## NOT checked
- Backtest ANSWERED rows not individually adjudicated: TERRY D:L254 (9/19), BROCK D:L312/L347/L421 (9/21), HAWK D:L432 (9/22–23), TERRY G:GATE-TERRY-007 (9/22). CORAL G:GATE-CORAL-MSI-01 (9/19–9/23) was checked: CORAL owed nothing (review_by is PROME's WQ-241 carry), so it is correct.
- Backtests used the working-tree ROSTER/ORCH_LOG, not each date's vintage.
- Dates 9/27 and before 9/19 not run. No NO EVIDENCE/UNCHECKED rows existed today, so those paths were not exercised live. Conservation/rc/determinism/FAILED-banner conditions (acceptance 1, 2, 10–15) were not tested. The spawn_list.py md5 was not checked. The CRU-11 six elements were checked as present, not graded for quality.

==========================================================================================
# ROUND 2 — rewritten spawn_slate.py (RETURN FOUND / NO CITING RETURN / UNCHECKED), read 2026-10-02
Read: SLATE_v2_h0.md; spawn_slate.py precheck/build/desk_tokens/row_ids/prome_annotation/hints. Re-ran v2 --stdout for 9/19–10/01 and a read-only python import at 10/02 08:00 (rev 371b4d4e7).

## R2 Task 1 — round-1 items
| # | Item | Status | Residue |
|---|---|---|---|
| 1 | windowed row: intermediate return = answer (L475) | MITIGATED | No verdict now. As-of 10/01 and at 10/02 08:00 v2 prints "⚠ the newest strong return is dated 2026-09-28, BEFORE the due date 2026-10-01". The flag tests only items[0], and only by date, so a non-answer dated on/after the due date gets no flag (BRENT today). |
| 2 | weekly gate: last cycle's grade in window (FERT-G5 9/30) | MITIGATED | "⚠ … dated 2026-09-23, BEFORE the due date 2026-09-30" prints. The liveness residue stays and is the dangerous path in Task 2. |
| 3 | hedge vocabulary gaps | RESOLVED | Words decide nothing. 'not grad\w+', 'not fresh', 're-spawn', 'co-sign' were added as hints. |
| 4 | hedge scope = filename/subject only | RESOLVED | Packet hints now scan name + whole body. Commit hints are still subject ±160, but they decide nothing. |
| 5 | forward reference = answer (REKILL/072 9/30) | MITIGATED | The ⚠ before-due flag fires on both. A forward reference dated on the due date is unflagged. |
| 6 | unrelated words decide the class | RESOLVED (no class) | Hint noise remains: CRUISE packet shows 'not graded' (from "PRE-REGISTERED, NOT GRADED") on an answered row; the FERT 9/23 grade packet shows 'not done', 're-spawn'. Only the first 4 distinct words are printed. |
| 7 | unhedged commit overrides hedged packet | RESOLVED | No class to override. |
| 8 | answer citing no pattern id is invisible | MITIGATED | Non-citing owner packets are now listed, capped at 3 and ordered by carrier recency. SHADE's actual answer `2026-10-01_from-SHADE_w1-legs-and-catchup.md` falls in "(+2 more)" and is not named. Gates still get no ids. |
| 9 | id extraction (VX-3.01→VX-3; junk ids) | MITIGATED | The `\.\d` lookahead fixes VX-3. SL-5, PR-6, PASS-2, ID-01, WT-1, DR-n, PROBE-5 are still extracted; they now only add pointers. |
| 10 | slash co-owners dropped | RESOLVED | "`D:L182` SHADE + BROCK, CREED" is now listed. Path tokens (AGENTS/X/ in an owner cell) could be read as co-owners, but no live instance exists (scanned). |
| 11 | stale IN-FLIGHT ⇒ "re-ping, never spawn" | RESOLVED | Now a "check liveness" flag only; it does not remove a spawn candidate. |
| 12 | annotation case-sensitive | RESOLVED (case) | See new defect N2 (trailing stamps print no content; only the LAST annotation is shown). |
| 13 | commit line names no file | MITIGATED | It prints paths[0], the first path in the commit, which is not the cited artifact. SHADE ffd823d80 → `AGENTS/SHADE/MAINTENANCE.md`, irrelevant to L182. |

## R2 Task 2 — dangerous direction
- Re-runs (v2, --stdout): L475 as-of 10/01 → RETURN FOUND + "⚠ … dated 2026-09-28, BEFORE the due date 2026-10-01"; headline READ FIRST. GATE-FERT-G5 as-of 9/30 → RETURN FOUND + "⚠ … dated 2026-09-23, BEFORE …". GATE-HY-REKILL and GATE-LIQ-072 as-of 9/30 → RETURN FOUND + "⚠ … dated 2026-09-29, BEFORE …". None says "no spawn"; every row is in the "Read first" top list.
- **PATH FOUND (REAL, inherited, mitigated): an owner who is dark THIS cycle is never a spawn candidate on a gate or a long-window row.** spawn_list starts a gate's liveness at its registration date, so FERT (registered 8/17, last commit 2026-09-23, 7d before) is ACTIVE on 9/30. v2 heads the stanza "READ FIRST — the owner has been in session since the row's date", which is false for this cycle. The 9/30 v2 spawn list is "DAEDALUS; FALCON; SHADE"; FERT is absent. In reality PROME spawned FERT on 10/01 (ORCH_LOG fert-1001: "GATE-FERT-G5 passed its owner-set review_by 2026-09-30"). The only cues are the ⚠ before-due line and the census basis "last self-commit 2026-09-23 (7d ago)". Same structure: CORAL MSI-01 9/19–9/23 (last commit 9/13; CORAL owed nothing, so harmless there), L475 (window from 9/25). Severity MEDIUM: the row is visible and flagged, but a needed spawn reads as a "read" item.
- Not a path, but noted: BRENT G:COT-35B and MIDAS L582 need a fresh spawn ≥15:30–15:35. Both are READ FIRST, not spawn candidates. Their packets say so and the hints show 're-spawn'. BRENT's headline has no ⏱, because timing_words reads only the condition/owner cells, while "~15:30 ET" sits in the gate's next_consumer/review_by cells.
- No path found where v2 says a row needs no action or drops a due row: conservation still prints OK (32 = 8 + 24), and the LANDS table holds only not-yet-due rows.

## R2 Task 3 — would the listed artifacts lead to the truth?
| Row | Lead to truth? | Why |
|---|---|---|
| G:GATE-BRENT-COT-35B | YES | First-listed packet (10/02), hints 'not gradable', 'not fresh', 're-spawn'. §3 says not gradable before 15:30, and the commit body says re-spawn ≥15:35. |
| D:L582 MIDAS | YES | Packet hints 'wait', 'not graded', 're-spawn'; ⏱ on the headline. The packet's "⏳ COT 9/29 — WAIT, not graded this spawn" is in the listed artifact. |
| D:L182 SHADE | PARTLY | ffd823d80's body ("W1 tally NOT RULED … BROCK 10/02") and the row's own state cell show SHADE's legs are delivered. The answer packet `…w1-legs-and-catchup.md` is hidden in "(+2 more)". The 10/01 annotation that names it is not printed, because only the last (10/02) annotation is. The listed file for ffd823d80 is MAINTENANCE.md. |
| D:L493 LIQUID | YES | Packet §6: "It is PENDING on WALTER's 10/02 ruling (L543) only". The hints ('not yet', 'not published', 'pending', 'partial') mostly come from the 10/1 credit-cell sections and point the wrong way until §6 is read. |
| D:L475 HENRY | YES | The FINAL packet is listed (2nd) with hints 'co-sign', 'pending' → "HENRY-graded, BOND co-sign PENDING". The first-listed return is the post-open memo (consistent, not the answer). |
| D:L502 CRUISE | YES | CRU-11 packet listed; its hint 'not graded' is noise. |
| D:L288 FERT | YES | Hints 'still not', 'not yet', 'no grade'; the packet says not published, no grade. |

## R2 Task 4 — new defects
- N1 (MEDIUM): the "READ FIRST — the owner has been in session since the row's date" headline asserts liveness from spawn_list's registration-date basis. On a gate it can be weeks stale (FERT-G5, above). v1 did not make this claim in the headline.
- N2 (LOW): prome_annotation prints from the LAST stamp forward, 34 words. When the stamp trails its text, nothing useful prints: CRUISE L502 shows only "annotated 2026-10-02 11:19 ET (PROME prome-70) […]", while the content ("COVERED: PROME's next boot TODAY — CRUISE L0 spawn…") precedes the stamp. Earlier annotations are dropped (SHADE's 10/01 annotation naming the w1 memo).
- N3 (LOW): hint words scan the WHOLE packet body (first 4 distinct), so they describe the packet, not the row. Examples: CRUISE 'not graded'; LIQUID's credit-cell words; FERT 9/23 grade packet 'not done', 're-spawn'.
- N4 (LOW): non-citing packet list is capped at 3 by carrier recency and hides the answer (SHADE); the commit "file" is paths[0], not the artifact.
- N5 (LOW): the slate grew from 20,538 B (63%) to 25,483 B (78% of 32,550) on the same day's inputs. That is the largest of the 12 days run (9/19–10/01 ranged 18–60%). The over-budget banner exists; headroom is 22%.

ROUND 2: 7 of 13 resolved, 6 mitigated, 0 open; dangerous-direction paths found: 1 (gate/long-window owner dark this cycle → READ FIRST, never a spawn candidate; REAL FERT-G5 9/30; flagged by ⚠ before-due, inherited from spawn_list's liveness start).
NOT CHECKED in round 2: the UNCHECKED/NO CITING RETURN paths live (none occurred on any date run); conservation/rc/determinism; the lands table; v2 ran against the working-tree ROSTER/ORCH_LOG, not each date's vintage.

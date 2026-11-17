# COLDREADER ledger: PLAN.md (rotation of PROME/SCRATCH.md), 4 blocks
Totals: 3 ❌ · 12 ⚠️. Line numbers are PLAN.md lines.

## BLOCK 1 (moved L17-22; replacement L28)
Live items in moved text -> status
- d2 checkpoint is NOT a closeout, account owed: KEPT ("was NOT a closeout and its daily-note account is still owed (§ Next D)").
- d2 "no ARGUS audit, no closeout asks beyond those recorded below; session limits and allowances carry" (L17): POINTER-ONLY. ⚠️ The "limits and allowances carry" clause is the checkpoint's own carry rule; the replacement keeps only some allowances (see Block 3).
- c4 (prome-c4) ENDED WITHOUT CLOSEOUT, "no push (31 local commits unpushed)", "no closeout ask to the twelve desk windows" (L18): replacement L28 says "Still live from them: the laptop checkpoint ... (prome-d2...)" and names NO c4 item. POINTER-ONLY. ⚠️ Block 3's replacement (L54) does mention c4 and the dark windows, so partly covered there, but Block 1's "still live" list is incomplete against its own sibling.
- "31 ahead and 0 behind origin" (d2, L17) / "31 local commits unpushed" (c4, L18): POINTER-ONLY. ⚠️ Plausibly finished by now (later commits exist), but a cold reader cannot tell the push state from the page.
- Gate run directories `/tmp/prome-boot-*`: POINTER-ONLY, finished history (not durable). ⚠️ trivial.
- 6f, 364221f6 (11/16 closeouts at 19:27 and 18:02), 4f/fe (11/14-15), 72/0f/e8 (11/12-13): closed-out history with pointers to daily notes (`memory/2026-11-1x.md`). POINTER-ONLY; finished. ✅ acceptable. prome-fe "RESTART CHECKPOINT 2026-11-14, never resumed" is closed by 4f: nothing live.
Replacement claims vs moved text:
- "the header lines for the 11/16 sessions and older": supported (L17-22 are 11/16 down to 11/12).
- "(§ Next D)": not in any moved text; unverifiable from the plan. ⚠️
- "§ Block 1" archive heading: the plan never says the archive has headings named "Block N". ⚠️
- Misread risk: replacement title "Earlier sessions" covers d2 (a checkpoint from last night), which reads as finished while it is not. ⚠️

## BLOCK 2 (moved L34; replacement L40)
Live items: the edit-trail chain itself; the pointer to `memory/2026-11-16.md` § Appendix 2 (verbatim replaced text of the closeout rewrite); the clause "This dates the page only; it refreshes no market or book observation."
- Chain: POINTER-ONLY, history, fine. Appendix 2 pointer: reachable in archive only. ⚠️ (plausibly finished history; one hop deeper).
- Disclaimer clause: KEPT verbatim.
- `<STAMP>` is a placeholder: must be filled by `date` in the same command. ⚠️ (plan does not say so).
- "prome-19" in the archive filename appears nowhere in the moved text; unsupported name, cannot verify it is this session's peer name. ⚠️
- Misread: the replacement says the page was last edited by the rotation only, but the moved chain shows 11/17 desktop boots after the d2 checkpoint ("the header at the second desktop boot of 11/17", L34). Fine as a stamp, but "earlier edits" now hide that 11/17 sessions exist. ⚠️
No ❌.

## BLOCK 3 (moved L46-48; replacement L54)
Item-by-item (moved text -> replacement)
- Boot run dir `/tmp/prome-boot-1669f3e3` "not durable": POINTER-ONLY, finished.
- VIOLET/MARCO/DAEDALUS touch 2 DELIVERED, closeout receipts held (ORCH_LOG): POINTER-ONLY. ⚠️ these are the "from the record" enumeration the spawn-closeout rule uses; the ORCH_LOG holds them, so ok.
- daedalus-e0 LIVE and busy at 23:23 in a window Will works in directly, "was not asked to stop", keeps its own assignments: POINTER-ONLY. ⚠️ A cold reader of the replacement ("DAEDALUS ... at its next session") will think DAEDALUS is dark; the moved text says a live owner window existed at 23:23 (preflight-relevant, though stale by now).
- READ_CAP rule 20 done at 648529e55a: POINTER-ONLY, done item.
- Checker change under C11 NOT built (9e02c0d712): KEPT.
- Five blind readers finished, ledgers under `reports/2026-11-16_pass8-rules-review/` and `reports/2026-11-16_outside-audit/`, none running: POINTER-ONLY. ⚠️ the replacement names only the two pasted source documents, not the ledgers.
- "Not woken or reopened: the nine other windows ... WENT DARK BEFORE THE ASK": CHANGED, see ❌ 2.
- Allowances: WQ-701 ep 2 of 3 KEPT; WQ-703 ep 3 of 3 (ceiling, text withheld) KEPT; "C9 commissions 0 of 2 (WQ-704's four are Will-approved, not C9)": POINTER-ONLY. ⚠️ the 0-of-2 equals a fresh boot, but the "not C9" classification is what stops a successor miscounting; moved text said allowances carry.
- "Done without asking this session: C3, WQ-700 (acb81f30f5) · C11 ...(9e02c0d712)": C11 commit hash survives only incidentally; C3 WQ-700 and the "Done without asking" label are DROPPED. See ❌ 1.
- "Skipped controls reported to Will at boot (PARTIAL): instruction files read with plain reader; no pull": POINTER-ONLY. ⚠️ reported at boot already, but the closeout that writes this session's account would need it.
- Laptop memory 4.2 of 5.9 GB: stale, finished.
- Two pasted source documents live only in repo copies: KEPT (both paths quoted exactly).
- "audit's desk items are verbatim in each desk's packet": POINTER-ONLY. ⚠️ minor.
- "No daily-note account of this session exists yet: the actual closeout writes it from the records named here": KEPT as "No daily-note account of either exists yet", but see ❌ 3; also "the records named here" are exactly what is being moved, so the writer must open the archive. ⚠️
Second bullet (host restart):
- Twelve windows, list: replacement gives the nine, correct count and names. COUNT CHECK: moved 12 (WALTER, DAEDALUS, HENRY, LIQUID, RED, VIOLET, NEXUS, HOMER, CARL, BOND, OTTO, MARCO) minus DAEDALUS, VIOLET, MARCO (reopened, closed out) = 9: WALTER, HENRY, LIQUID, RED, NEXUS, HOMER, CARL, BOND, OTTO. Replacement list matches. ✅
- "unless Will reopens it" dropped from the WENT DARK sentence. ⚠️
- "their write-backs ride their next dated sessions (OTTO has none this week)": the replacement keeps the first half and drops the OTTO exception, so OTTO reads as having a next dated session. ⚠️
- Uncommitted desk work (VIOLET, MARCO, DAEDALUS run folder, WALTER research folder, WALTER untracked boot receipt): resolved in the 21:29 update; dropped; finished history. ✅/⚠️ trivial.
- prome-d2 filed seven packets, recorded WQ-700, sent packets to HOMER and TERRY: POINTER-ONLY. ⚠️ outbound packets whose consumption is unknown.
- WQ-699 RULED A at 21:22 ET ("D: the row dated 2026-11-18 closes the loop at BOND's files"): DROPPED entirely. ⚠️ A dated row for tomorrow; under the charter's own rule the DOCKET row (not this page) carries the obligation, but the plan does not show the row exists.
- MARCO and VIOLET WQ-678 edit for Will's word: KEPT.
- DAEDALUS Production Review 10 CHECKPOINTED, four readers owed: KEPT.
Third bullet (6f closed out):
- walter-5a and reginald-41 are Will's own windows (REGINALD opened 17:58 ET for a video read); 6f launched nothing but ARGUS; no timer or background process running: POINTER-ONLY. ⚠️ plausibly finished (the 21:11 restart killed every window), but it is the only record of those two windows' ownership.

❌ 1  Replacement L54 drops "Done without asking this session: C3, WQ-700 (acb81f30f5) · C11, the read-cap checker task to DAEDALUS (9e02c0d712; not built)" (L46). Only 9e02c0d712 survives, inside the DAEDALUS clause; C3/WQ-700/acb81f30f5 and the "Done without asking" heading vanish. The charter-style duty (acts named at the closeout under that heading) is still owed because L46 says "No daily-note account of this session exists yet".
❌ 2  Replacement L54: "the nine desk windows the 21:11 ET host restart killed and nobody reopened (WALTER, HENRY, LIQUID, ...)" is stated with no time anchor; L46 anchors it "at 23:23 ET" and L47 "(written 21:17 ET)". The artifact's own Block 2 (L34) shows later 11/17 boots ("the header at the second desktop boot of 11/17"), and the session context's git log shows a "LIQUID closed out" commit on 11/17. As written the replacement asserts a present-tense state the moved text only supports as of 11/16 night.
❌ 3  Replacement L54: "No daily-note account of either exists yet (§ Next D)". Moved L46 says it only for d2 ("No daily-note account of this session exists yet"); for c4 L18 says only "no closeout, no push". "Either" is unsupported, and Block 1's replacement (L28) says it for d2 only, so the two replacements disagree about which sessions are owed.

## Own check (not asked)
- Cross-replacement consistency: Block 1 (L28) lists only d2 as live; Block 3 (L54) lists c4 and d2: ❌ 3 above.
- Name/count check on the nine windows: passes. Hash/figure spot checks: 9e02c0d712, WQ-701 2 of 3, WQ-703 3 of 3, "four readers", 18:26 ET: all match moved text.
- Time-order check inside the moved text: c4 booted 20:41, restart 21:11, d2 booted 21:15, d2 checkpoint 23:23: consistent.
- Archive heading check: the plan names no "§ Block 1/2/3/4" headings in the archive; the four replacement pointers depend on them. ⚠️

## BLOCK 4 (moved L60; replacement L66)
- WITHDRAWN, Will 18:26 ET 11/16, nothing owed by PROME: KEPT.
- Will's quoted word "WQ-698 ok go with your rec": POINTER-ONLY. ⚠️
- "record in WILL_QUEUE RECENTLY DONE": the authoritative record's location is POINTER-ONLY. ⚠️
- "No log, no forecast, no successor row": POINTER-ONLY. ⚠️ it is a negative instruction a successor could contradict.
- "HAWK was told by packet and updates its own STATUS line at its next session": POINTER-ONLY. ⚠️ a pending item owned by HAWK.
- "Written after the audited closeout, so the queue row and this line are unreviewed until the next audit": POINTER-ONLY. ⚠️ A later ARGUS audit (19:27 ET closeout) may have covered it, but the plan does not say; the replacement reads as settled.
Replacement claims unsupported: none. No ❌.

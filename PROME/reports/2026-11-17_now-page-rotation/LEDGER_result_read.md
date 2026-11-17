# LEDGER result read (COLDREADER, Sonnet) 2026-11-17 ~11:05 ET
Counts: 2 X (blocking), 6 warnings.

## A. Verbatim
Extraction: archive lines sed -n 20,25p (B1), 31p (B2), 37,39p (B3), 45p (B4) to files under scratchpad/rot/b1..b4; python zlib.crc32 over bytes (incl. final newline) and PROME/tools/measure.py (agree).
B1 4608 B crc 2036539096 = table. B2 1220 B 1629860451 = table. B3 4231 B 1253030898 = table. B4 362 B 578473250 = table.
Every block line is in `git show HEAD:PROME/SCRATCH.md` (exact line match) and in none of them is present in current page. Reverse: all 11 lines removed by `git diff -U0` (6+1+3+1) are in the archive. Invariant 1 holds.

## B. Nothing lost
Block 1 (six header lines; replacement Line 1):
 - prome-d2 checkpoint = NOT closeout; limits/allowances carry: POINTER-ONLY (residue 1); the 11/16 bullet carries the allowances.
 - prome-c4 ended without closeout: KEPT (Line 4).
 - 50341462 (19:27), 364221f6 (18:02), 11/13-11/15 sessions CLOSED OUT: POINTER-ONLY, not on residue list. Low action weight (ownership evidence for 11/16 desktop sessions; the page's own header now carries ownership).
 - Line 1 "what they still carry: § This session, the 11/16 bullet": CHANGED/unclear, see W1.
Block 2: edit chain POINTER-ONLY (residue 4 for Appendix 2; the chain itself is history). Disclaimer "dates the page only" KEPT.
Block 3 bullet 1 (checkpoint): VIOLET/MARCO/DAEDALUS receipts residue 5; daedalus-e0 live residue 6; READ_CAP rule 20 done at 648529e55a: pointer-only, not on list (W3); five blind readers residue 7; nine windows KEPT; reads/C9 allowances KEPT/residue 8; done-without-asking KEPT; skipped controls residue 9; laptop memory 4.2 GB stale, fine; two pasted docs KEPT; "audit's desk items verbatim in each desk's packet": pointer-only, not on list (W3); no daily-note account KEPT.
Block 3 bullet 2 (host restart): nine windows KEPT but CHANGED (X1); uncommitted desk work (resolved per its own update) pointer-only fine; WQ-699 RULED A and OTTO none: residue 10; Production Review 10 KEPT; WQ-678 edits KEPT.
Block 3 bullet 3 (50341462): "WALTER walter-5a is Will's own window, as is REGINALD reginald-41"; "no reader, timer or background process of PROME's running": DROPPED from page, not on residue list (X2).
Block 4: nothing owed by PROME KEPT; HAWK STATUS etc residue 11; "queue row and this line unreviewed until next audit" dropped (residue 11 says line written after audited closeout: covered).

## C. Nothing added
Line 4 clause "(HENRY, LIQUID and RED had 11/17 sessions, ORCH_LOG)": ORCH_LOG rows dated 2026-11-17 exist for HENRY (window 1), LIQUID (window 1 and 2-CLOSEOUT-PING), RED (window 1). Supported. Wording ambiguity: W2.
Line 2 "11:02 ET (system clock)": `date` now 11:03 EST; plausible. All commits (acb81f30f5, 9e02c0d712) resolve; both reports paths exist; nine-window list = twelve minus DAEDALUS, VIOLET, MARCO: matches. Nothing else added. "(§ Next D)" resolves (page line 15) and says the 11/16 laptop session's daily-note account is owed.

## Findings
X1 Line 4 (page l.50): "each is reported WENT DARK BEFORE THE ASK at PROME's actual closeout, and its write-back rides its next dated session (HENRY, LIQUID and RED had 11/17 sessions, ORCH_LOG)". Moved text (archive l.38): "at PROME's closeout each is reported WENT DARK BEFORE THE ASK unless Will reopens it." Dropped "unless Will reopens it"; page l.11 (Next A) says "liquid-63 CLOSED OUT 10:57 ET" and henry-ff is HOLDING. A reader following line 4 would report LIQUID/HENRY/RED as WENT DARK. Invariant 2/4 broken (condition lost; the parenthetical does not say what follows from the sessions).
X2 Dropped from the page, not on residue list (archive l.39): "WALTER `walter-5a` is Will's own window, as is REGINALD `reginald-41`" . Replacement l.50 lists WALTER among windows killed by the restart, with no note that a separate Will-owned WALTER window existed; a spawn preflight reader loses the ownership fact. grep of page for walter-5a / reginald-41: none.
W1 Line 1 (page l.5): "what they still carry: § This session, the 11/16 bullet" : the 11/16 bullet is titled "Carried from the 11/16 laptop sessions (prome-c4, then prome-d2)"; it carries nothing of the desktop closeouts (18:02, 19:27) or older sessions. Overstates.
W2 Line 4: "(HENRY, LIQUID and RED had 11/17 sessions, ORCH_LOG)" does not say whether their write-back is done (LIQUID closed out; HENRY holding).
W3 Pointer-only and not on residue list: "READ_CAP rule 20 done at 648529e55a"; "the audit's desk items are verbatim in each desk's packet".
W4 Own check (D1): page l.15 § Next D still says "this page is over 90% of its read budget and must rotate (...)". Page now 22,784 B (measure.py) = 70% of 32,550; read_cap_check rc=0, rotation_due=0. A live instruction made obsolete by this edit (invariant 4 spirit; stale instruction).
W5 Own check (D2): Line 3 omits the quote "WQ-698 ok go with your rec" and the "record in WILL_QUEUE RECENTLY DONE" pointer (residue 11 covers the latter). Fine, minor.
W6 Pointer form "§ Block 1" resolves to `## Block 1 ...` headings (ok); "§ Next D" is a bullet label, not a heading (resolves by label "D.").
D checks run: (1) read_cap_check + measure.py on page (rc=0, 22,784 B); (2) grep page for orphaned references to removed text (walter-5a, reginald-41, "line below records", WENT DARK) found X2 and W4; (3) commit hashes cat-file; (4) CRC double-computed two ways.

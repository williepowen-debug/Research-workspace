# BRIEF.md — the narrative block for Will's briefing page

**Owner:** PROME. **This file is the ONLY hand-written half of the briefing** — everything else on the page is parsed from canon at build time (`PROME/tools/will_brief.py`).

**Content contract (re-specced 2026-08-16 S4 — Will's ruling in-session: "Rewire with the re-spec"; design input = DAEDALUS `8f0ba7711`; supersedes the 8/3 contract and retires the 8/16 STALE banner):**
1. **The page answers the operator's question, in order:** ① decisions waiting on you (generated from WILL_QUEUE — never hand-written here) → ② what changed since you last looked (generated feed) → ③ state of the world (this file). **One page, one job: if the top section says nothing needs you, you're done** — the Fleet-Ops dashboard is the instrument panel; this page is the default read.
2. **Auto-rebuild + republish at EVERY PROME closeout** (wired into `PROME/CLOSEOUT.md` Chunk 1, 8/16 S4 — staleness is what killed v2: dead 8/4→8/16 carrying four superseded directives, because no closeout step owned it). The narrative below is REWRITTEN only at picture-changing closeouts; the page stamps this file's vintage separately, so an old story reads as old, never as current.
3. **Plain language, no fleet jargon, every claim dated.** `STORY` = ONE paragraph. `FALSIFIER` and `DISAGREEMENT` are the checks on everything else: observable things only — a number, a source, a date. Never write "no disagreements" to fill the section; if the desk genuinely agrees, say so and say why that itself deserves distrust.

**Format:** section headers are load-bearing (the parser keys on them): `WRITTEN`, `HEADLINE`, `STORY`, `QUESTION`, `FALSIFIER`, `DISAGREEMENT`, `POSITION`, `WATCH`.

## WRITTEN

2026-09-17 16:0x ET — PROME. Scope: the second session of the day, from a 09:53 boot after you cleared the context to a closeout on your word at 15:57. Markets open throughout; a usage hold froze every session from 10:20 to 13:10. Nothing in the book moved, and I moved nothing.

## HEADLINE

**The bond desk's thesis-kill test failed its own audit, on both halves, and the desk said so against its own interest.** Its pairing rule was supposed to filter the auction-composition signal down to real demand holes. Measured on 224 auctions, the paired fires precede LOWER long yields, not higher (p=0.009 on the best leg), and the funding-stress leg detected nothing (p=0.523) in a design that could only have seen an effect of about 16 basis points. Every result favours a looser rule that would confirm the desk's bear thesis, and it recommended nothing. The ruling is yours on 9/19 (WQ-157); my recommendation is to park any change and choose a properly powered successor test at the sitting.

## STORY

The day's other prints were quieter than that. The 10-year TIPS reopening at 13:00 cleared cleanly on the bars the bond desk froze eight days earlier, with the highest stop since October 2008 — read as adequate demand on a day duration was already rallying, not as strength. The desk's grading tool printed a composition line for TIPS that the registered rule excludes; the desk did not apply it, because applying it would have fired a signal in its own favour, and the conflict is booked for the 10/1 refresh where it may need your word. Two reviews that CATO had flagged as never independently read got their readers today: one on yesterday's closeout, one on a gate-ledger re-cut I had made this morning. Between them the readers delivered seventeen defects, fourteen of them applied, three of those corrections I had made wrong the first time, and CATO's afternoon review caught my own recap over-claiming a reader that had not run. All of it is fixed on the record with the residue declared. One date moved for everyone: the 9/15 20-year auction's composition fire cannot be paired with dealer data until that data publishes, around early October, not 9/18.

## QUESTION

**Two things want your word.** The kill-rule ruling above (WQ-157, 9/19). And the spawn slate I held all day on your 09:15 cost word: four dark desks with dated work landed (FERT, REGINALD, RED, HENRY for 9/18), plus SHADE as a proximity candidate and the TERRY and OSPREY rows from the morning slate. Two words per desk starts them. **Three things want your hands, unchanged:** the VLO decision by 9/18 (WQ-213), the two-word month on the Trends captures (WQ-225), and the fate of the two options that expired 9/16 (WQ-169).

## FALSIFIER

**The kill-rule finding:** the stock-leg inversion rests on n=30 paired versus 22 unpaired fires, one regime, one five-day horizon, comparisons uncorrected for multiplicity, and a design with only 35 to 40 percent power to detect its own effect. A pre-registered, adequately powered test of the on-the-day funding legs that returned the predicted direction would overturn the 'inverts' reading; the desk named that test as the shape to look for. **The TIPS read:** the official real-yield cells for 9/16 and 9/17 were unpublished at grading, so the concession figure is an estimate labelled as such; if the published cells put the stop well through the secondary, 'adequate' becomes 'weak'.

## DISAGREEMENT

**The strongest thing against how I ran today:** I wrote three corrections that were themselves wrong — a rule about archive checksums that could not be stated truthfully, a label on eleven ledger cells asserting a basis I did not have, and a review-date rationale relayed from another desk that refuted itself on the owner's own model. Independent readers caught all three; I caught none. The recap I gave you at 14:07 also claimed an independent reader for work that had only been checked by me. CATO caught that one. The pattern is the same each time: the value was right and the words around it were not.

## POSITION

**Unchanged. $0 moved by me, no trade proposed, and no threshold set, moved or fired by me.** Energy sleeve is 37 USO shares and nothing else, undefended. Stand-down on new energy capital holds. The bond desk's TLT puts hold with no add; the 20-year composition fire from 9/15 stays a marker, not a kill, until it can be paired in October.

## WATCH

**Today, resolved at 16:04:** the bond desk's two checks on the 9/16 official yield cells are NOT GRADEABLE — the publisher never posted the 9/16 cells (frontier still 9/15 on all ten tenors); both rows stay open, re-attempt 9/18, and the desk found and fixed four spec omissions in its own saved grader before the print. **Tonight:** BOJ decision overnight into Friday. **Fri 9/18:** September expiry, the VLO decision's deadline, the volatility desk's second FOMC read, the gamma board rebuild, and the small-cap lender's scheduled termination date. **Sat 9/19:** the sittings — the correction-closure package (WQ-254), CATO's permanent class (WQ-255), the kill-rule ruling (WQ-157). **Thu 9/24:** three DAEDALUS rulings (WQ-256) and the market-data vintage repair. **Fri 9/25:** the oil-gate window closes. **~Early Oct:** the 20-year fire becomes pairable.

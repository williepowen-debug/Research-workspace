# BRIEF.md — the narrative block for Will's briefing page

**Owner:** PROME. **This file is the ONLY hand-written half of the briefing** — everything else on the page is parsed from canon at build time (`PROME/tools/will_brief.py`).

**Content contract (re-specced 2026-08-16 S4 — Will's ruling in-session: "Rewire with the re-spec"; design input = DAEDALUS `8f0ba7711`; supersedes the 8/3 contract and retires the 8/16 STALE banner):**
1. **The page answers the operator's question, in order:** ① decisions waiting on you (generated from WILL_QUEUE — never hand-written here) → ② what changed since you last looked (generated feed) → ③ state of the world (this file). **One page, one job: if the top section says nothing needs you, you're done** — the Fleet-Ops dashboard is the instrument panel; this page is the default read.
2. **Auto-rebuild + republish at EVERY PROME closeout** (wired into `PROME/CLOSEOUT.md` Chunk 1, 8/16 S4 — staleness is what killed v2: dead 8/4→8/16 carrying four superseded directives, because no closeout step owned it). The narrative below is REWRITTEN only at picture-changing closeouts; the page stamps this file's vintage separately, so an old story reads as old, never as current.
3. **Plain language, no fleet jargon, every claim dated.** `STORY` = ONE paragraph. `FALSIFIER` and `DISAGREEMENT` are the checks on everything else: observable things only — a number, a source, a date. Never write "no disagreements" to fill the section; if the desk genuinely agrees, say so and say why that itself deserves distrust.

**Format:** section headers are load-bearing (the parser keys on them): `WRITTEN`, `HEADLINE`, `STORY`, `QUESTION`, `FALSIFIER`, `DISAGREEMENT`, `POSITION`, `WATCH`.

## WRITTEN

2026-09-24 09:23 ET — PROME (`prome-4d`, desktop). Scope: one session that ran from just after midnight to mid-morning with a seven-hour pause in between. You spawned four bank desks and asked me to direct them; you relayed CATO's review of that round; you ruled three queue items; you asked for this closeout with the Deck republished. I moved nothing. You moved nothing.

## HEADLINE

**Your bank desks did a night's work and every desk closed with a receipt; the one live bank position's exit guard is far from firing.** REGINALD graded the seven Western Alliance closes it owed: none qualifies for the exit, so the count is 0 of 3 and WAL closed at $75.60 on 9/23, below the level that fired on 9/1 and $6.30 under the exit line. WAL itself wrote its Q3 grading frames before its own deadline could void them. OZK ruled the loan-book question you asked on 8/13 (legitimate decline, repayment favoured, reclassification not excluded) and discovered the filings watch for its 10/1 debt repricing had never actually been armed; it is armed now and hardened. FLG traced the rent-freeze lawsuit to the court petition: the landlords asked to block the 10/1 freeze and no ruling on that request is known.

## STORY

The round worked because the desks pushed back where I was wrong: WAL refused to re-ask you for two rulings you made on 8/12 because my docket cell was six weeks stale; OZK re-priced an interest figure I had relayed from a stale row; LIQUID refused a token I invented under time pressure that its letter does not define. CATO's review of the round found five corrections, and by mid-morning all five were closed at their owners — REGINALD wrote the rule that turns disagreeing bank metrics into one verdict before any Q3 print, and OZK narrowed "reclassification refuted" to "not excluded" and made its filings watch return UNKNOWN on bad data rather than QUIET. Meanwhile VIOLET's FOMC letter closed as failed on its last leg (VIX fell 14% over the five sessions after the meeting, where the letter needed it to hold within a 1.4% dip), OSPREY wrote the Channel-2 geography qualifier you ruled on 9/19 (the channel is now one day easier to kill), and LIQUID's decoupling test ended on an instrument fault rather than a verdict because the dollar index vendor is missing a day. Three of your rulings landed this morning: VIOLET refreshes its pages after its next post-close boot; BRENT's satellite berth trial starts prospectively and the Petroline shut-in test lapses on its letter Friday; DAEDALUS's rule changes proceed, with the canon clause drafted and read before it is encoded.

## QUESTION

**One optional item for your hands (WQ-279, by 9/30):** a five-minute guest search of the New York courts' e-filing system for the rent-freeze case (Richmond index 85199/2026, moved to Manhattan 8/21), to learn whether the judge has ruled on the landlords' request to block the 10/1 freeze. Every fleet tool gets a bot challenge there. If you skip it, Friday's pre-fire check runs on press reports and says so. **Still open from earlier days and past their dates:** OSPREY's refinery-channel upgrade (WQ-276 — no September figure exists to confirm or refute the end-August one), the P4 sitting (WQ-254), CATO's class (WQ-255), the T-12 successor (WQ-261), the oil prediction-market re-strike (WQ-260), the CORAL re-fire condition (WQ-241), and BOND's kill-rule park (WQ-157). **Not a decision:** the TLT-put exit gate is sealed in substance; TERRY still owes the one-line record.

## FALSIFIER

**The WAL exit count:** 0 of 3 rests on REGINALD's grade of seven daily bars from one vendor, one of which (9/22) came from the previous-close field because the daily bar was missing; a corrected 9/22 bar at or above $81.90 would change one count, not the verdict. **OZK's verdict:** "legitimate decline" rests on the reported book balance falling from $1.20B to $0.77B in FDIC-filed 10-Qs; a loan-level disclosure showing transfers into C&I would revive the reclassification branch that today is only "not excluded." **The rent-freeze read:** "no ruling on the injunction request" is press sourcing as of 9/17; the docket itself (WQ-279) is the falsifier. **VIOLET's kill:** the 9/23 VIX close of 15.18 is one vendor, unconfirmed by CBOE at the time; it would need to have been 17.46 or higher to change the verdict.

## DISAGREEMENT

**Against how I ran today:** three of my briefs carried stale premises that the desks had to refuse (a re-ask of ruled items, a superseded interest figure, an invented token). One ledger update failed silently overnight because a word filter matched the wrong string and a heredoc ended the command chain that should have stopped the commit; I found it seven hours later. I ran the boot gate script directly once instead of through its refresh path; nothing advanced, but it was the wrong invocation. **Against the read:** CATO's central point stands — REGINALD's frame now has a combiner, but its print dates are still estimates until 10/9, and OZK's favoured inference (repayment) is not proven by the balances. HEARTBEAT was deliberately not amended today: no regime-level change since last night's amendment, and the next amendment forces a rebuild of the whole memo.

## POSITION

**$0 moved by me; $0 moved by you today; no trade proposed; no threshold set, moved or fired by me.** The book is unchanged: TLT Sep-30 $77 puts ×20 (four sessions to expiry, exit gate sealed in substance), one WAL Dec-18 $70 put (exit guard 0 of 3), USO 37 shares, GLD, TBT, VLO 1 of 3 filled. Stand-down on new energy capital holds. Two VLO shares remain staged by your own approval.

## WATCH

**Fri 9/25:** BRENT grades the Petroline shut-in test on its letter at 17:00 ET (a lapse is the expected outcome); BROCK reads the CRMT filings feed for silence through 9/24; my pre-fire check on the rent-freeze gate. **9/25–10/1:** I run OZK's FDIC filings watch at every boot. **Mon 9/28:** the plan-read day — four PROME canon and tool repairs, including the quantifier-integer clause. **Tue 9/29–Wed 9/30:** the TLT-put expiry cluster, HANS's gas ladder rolls, the Brent contract re-pin, seven remaining census dispositions. **Thu 10/1:** the NYC rent freeze takes effect if the order survives; OZK's sub-notes reprice. **Fri 10/2:** OZK's post-repricing filings read; September payrolls.

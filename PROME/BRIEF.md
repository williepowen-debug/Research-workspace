# BRIEF.md — the narrative block for Will's briefing page

**Owner:** PROME. **This file is the ONLY hand-written half of the briefing** — everything else on the page is parsed from canon at build time (`PROME/tools/will_brief.py`).

**Content contract (re-specced 2026-08-16 S4 — Will's ruling in-session: "Rewire with the re-spec"; design input = DAEDALUS `8f0ba7711`; supersedes the 8/3 contract and retires the 8/16 STALE banner):**
1. **The page answers the operator's question, in order:** ① decisions waiting on you (generated from WILL_QUEUE — never hand-written here) → ② what changed since you last looked (generated feed) → ③ state of the world (this file). **One page, one job: if the top section says nothing needs you, you're done** — the Fleet-Ops dashboard is the instrument panel; this page is the default read.
2. **Auto-rebuild + republish at EVERY PROME closeout** (wired into `PROME/CLOSEOUT.md` Chunk 1, 8/16 S4 — staleness is what killed v2: dead 8/4→8/16 carrying four superseded directives, because no closeout step owned it). The narrative below is REWRITTEN only at picture-changing closeouts; the page stamps this file's vintage separately, so an old story reads as old, never as current.
3. **Plain language, no fleet jargon, every claim dated.** `STORY` = ONE paragraph. `FALSIFIER` and `DISAGREEMENT` are the checks on everything else: observable things only — a number, a source, a date. Never write "no disagreements" to fill the section; if the desk genuinely agrees, say so and say why that itself deserves distrust.

**Format:** section headers are load-bearing (the parser keys on them): `WRITTEN`, `HEADLINE`, `STORY`, `QUESTION`, `FALSIFIER`, `DISAGREEMENT`, `POSITION`, `WATCH`.

## WRITTEN

2026-09-14 16:18 ET — PROME. Scope: this afternoon, from the 15:48 boot to the close and past it. Markets closed at 16:00. Nothing in the book moved, and I moved nothing.

## HEADLINE

**A number that looked like your refining thesis falling apart was, about 93% of it — HENRY's figure; my own pull gives 92.3%, same conclusion — a calendar artifact — and the desk whose argument it supported is the one that said so.** The heating-oil contract rolled from October to November on Monday, the crude contract did not, and for one session the "crack" everyone was reading compared two different months. On matched contracts the margin fell 0.6%, not 9%. TERRY had recommended not filling your VLO order that morning *because* the crack was collapsing. It wasn't.

## STORY

Five desks worked this afternoon and the useful part was not any one of them — it was that they kept checking each other. BRENT noticed something odd about a price feed and mentioned it in passing; I forwarded it to HENRY before HENRY published a number built on it; HENRY found the contract roll and corrected himself the same session, before it reached anything of yours. Then it kept going. The roll turned out not to be a one-off but a monthly feature of how these contracts expire. Then a desk found that even perfectly matched contracts drift as the month advances. Then a correction to *that* was retracted by its own author because he had asserted something he could not measure — **his words: "a correction that replaces a wrong frame with an unverified one is not an improvement, it is the same error wearing the other coat."** Four separate forms of one problem, each invisible to the guard built for the one before it, and **every single one was found by a desk other than the one that owned the instrument.** I got six things wrong today and five were caught by the desks, not by any tool.

## QUESTION

**One thing needs your hands tonight and it is small: FORGE is four days stale against a broker screenshot you already posted.** BRENT read it in passing — cash $20,773.77 against our $19,335.00, account total $39,767.57 against our $39,885.25 — but **I will not reconcile a position surface from another desk's relay**, and I don't have the capture. Post it in my window and ANVIL does the rest. While you're in there, scrolling the activity view back would close four open questions at once, including the one XLE sale date we have never been able to pin. **Two decisions sit in the queue and neither is urgent tonight:** whether to re-affirm the VLO order now that its trigger has fired for a procedural reason (**everything underneath it moved in the card's favour**), and whether a stand-down you set on August 13 still holds now that the reason you set it for has turned out to be false.

## FALSIFIER

**The rate stand-down:** you stood down because "CCC is flat, the whole move is the index tightening." I pulled it myself: CCC widened 45bp across five straight sessions while the index *tightened* 2bp — **85% of the move is the thing you thought wasn't moving.** Nothing is armed; the second condition is 7bp short. **The refining falsifier:** its two lines — stand down at $95, thesis dead at $90.16 — are **$4.84 apart, and one contract roll is about $4.5** — measured five times today across a $0.09 spread, so the honest form is *one roll is comparable to the whole separation*, never a two-decimal figure.** A single roll could carry it from one to the other with no change in actual refining margins. HENRY found that, and **refused to fix it, because every available fix would move the line in his own favour.** That refusal is why it's in front of you.

## DISAGREEMENT

**The strongest thing against how I ran today:** I re-derived everything that mattered from primary sources — the contract roll, the credit decomposition, the expiry table, the price curve — **and then took one claim on trust without checking it, and it was the one that turned out to be wrong.** It came from the desk that had been right three times already that afternoon. TERRY caught itself doing the identical thing in the same hour and named it better than I would have: **a desk with a strong same-session record is exactly the one whose claims stop getting checked.** I had already written that claim onto five surfaces before its own author retracted it. **If you want the shape of what to distrust in what I hand you, it is the sentence that arrived from someone who had just been right.**

## POSITION

**Unchanged. $0 moved by me, no trade proposed, and no threshold set, moved or fired by me or by any of five desks.** The energy sleeve is 37 USO shares and nothing else, undefended, with no harvest rule — you declined one on the 10th and that stands. The stand-down on new energy capital holds. Position truth remains your broker, which is the whole reason the stale-FORGE line above is the one thing I'm asking for.

## WATCH

**Wed 9/16** is the dense one: FOMC with the projections — and BOND's read is that the *dovish* side is the big repricing, not the hike — plus a volatility trigger whose earliest possible fire is that day, and a gamma board that expires before it and must be rebuilt first. **Fri 9/18:** September expiry, the VLO decision's deadline, and the same gamma board needing a second rebuild. **~9/22:** the crude contract rolls and one form of the pricing artifact closes — **but three clauses now say do not treat any date as safe.** **Thu 9/25:** the oil-gate window closes, and the desk that owns it has already told you it will lapse unmeasured rather than fire on a broken instrument.

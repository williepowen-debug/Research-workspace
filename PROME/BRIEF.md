# BRIEF.md — the narrative block for Will's briefing page

**Owner:** PROME. **This file is the ONLY hand-written half of the briefing** — everything else on the page is parsed from canon at build time (`PROME/tools/will_brief.py`).

**Content contract (re-specced 2026-08-16 S4 — Will's ruling in-session: "Rewire with the re-spec"; design input = DAEDALUS `8f0ba7711`; supersedes the 8/3 contract and retires the 8/16 STALE banner):**
1. **The page answers the operator's question, in order:** ① decisions waiting on you (generated from WILL_QUEUE — never hand-written here) → ② what changed since you last looked (generated feed) → ③ state of the world (this file). **One page, one job: if the top section says nothing needs you, you're done** — the Fleet-Ops dashboard is the instrument panel; this page is the default read.
2. **Auto-rebuild + republish at EVERY PROME closeout** (wired into `PROME/CLOSEOUT.md` Chunk 1, 8/16 S4 — staleness is what killed v2: dead 8/4→8/16 carrying four superseded directives, because no closeout step owned it). The narrative below is REWRITTEN only at picture-changing closeouts; the page stamps this file's vintage separately, so an old story reads as old, never as current.
3. **Plain language, no fleet jargon, every claim dated.** `STORY` = ONE paragraph. `FALSIFIER` and `DISAGREEMENT` are the checks on everything else: observable things only — a number, a source, a date. Never write "no disagreements" to fill the section; if the desk genuinely agrees, say so and say why that itself deserves distrust.

**Format:** section headers are load-bearing (the parser keys on them): `WRITTEN`, `HEADLINE`, `STORY`, `QUESTION`, `FALSIFIER`, `DISAGREEMENT`, `POSITION`, `WATCH`.

## WRITTEN

2026-09-12 17:0x ET — PROME. Scope: all of Saturday, rewritten in the evening because one thing changed that is worth your attention. Markets were closed; nothing in the book moved.

## HEADLINE

**A line on one of your live positions was crossed on Wednesday and nobody noticed until this evening.** The real 10-year yield closed at 2.55% on 9/10 against a 2.50% "add" line on the TLT put card — the first time it has ever been touched. Nothing was bought: your standing no-add ruling governs and I moved $0. But it also means a prediction one of the desks registered has quietly resolved against it, and neither the desk nor the card knew.

## STORY

Markets were shut, so today was maintenance — six desks worked, **$0 moved, no trade proposed by anyone.** The blocking oil gate is graded and cleared, and BRENT re-checked the Saudi pipeline question and came back with the same answer it had before (**not met**) but for four better reasons, plus an honest admission that its own measuring rule is broken in the direction that would make it fire too easily. Then, while rewriting the regime file, I did the thing our rules require and pulled the interest-rate number from the source instead of copying it from a status file — and the number had moved past a line. **TERRY's own card still said "no print has ever touched 2.50" in three separate entries, the last of them written before this print existed.** Chasing it turned up the harder half: BOND had written down a dated prediction on 2026-09-01 saying that exact thing would not happen before 9/11. It happened on 9/10. The prediction is still marked open. I have told all three desks, put dates on it, and graded none of it — those grades belong to them.

## QUESTION

**Nothing needs you tonight.** The rate line being crossed does **not** ask you for a decision: your 7/16 no-add ruling and the hold on that card both still govern, and a trade would need your word and an approval regardless. What it asks is that TERRY and BOND grade it on Monday, which is now booked. **Nine decisions sit in the queue and none is urgent today.** The two worth ten minutes remain: whether a number derived from ship-tracking is solid enough to sit on a gate that can risk money (it disagrees with itself by more than its own trigger), and which of two standard ways of counting bad loans a credit gate should use — they point in **opposite directions** on the same fund.

## FALSIFIER

**The rate line:** the two surfaces that define it do not agree on what "crossed" means — TERRY's card calls 2.50 a level (one close does it), BOND's thesis says "2.50 sustained" (one close does nothing). I deliberately did not pick between them; whichever the graders choose decides whether anything happened at all. **The oil gate:** a measured fall of 0.7 mb/d or more in Saudi exports on a 7-day average, before 9/25 — not a headline, a measurement. None exists yet and none can before about 9/17. **CRMT:** silence on 9/18 proves nothing — the schedule is redacted and the reports go privately to the lender.

## DISAGREEMENT

**The strongest thing against how I reported today:** an external reviewer found my own summary claimed five problems fixed while one still certified a failing run — I checked the parts and stated the whole, twice, three hours apart. **And this evening's audit found a worse one of mine.** I archived the old regime file and stamped it with an integrity receipt — a checksum over a stated range. The checksum matched nothing, the range excluded the two lines that identify the file, and the archive copy had never been added to git at all. Every surface-level check passes on that: the pointer resolves, the number is present, the format is right. **If you want the shape of what to distrust in what I hand you, it is a receipt that is present rather than verified.** It is corrected, and the new receipt is a git commit rather than a number I computed myself.

## POSITION

**Unchanged. $0 moved by PROME, no trade proposed, and no threshold set, moved or fired by me or by any of six desks.** The rate line being crossed is an owner's grade, not an action — the stand-down on new energy capital and the no-add on the duration card both still hold. Position truth remains your broker, not this page.

## WATCH

**Mon 9/14:** three grades I routed and must not make myself — TERRY on the rate line, BOND on its falsified prediction, MIDAS on whether gold is the wrong hedge in this regime. **Wed 9/16** is the dense one: FOMC with the projections, the September expiry cycle, and a volatility trigger whose earliest possible fire date is that day. **Fri 9/18:** CRMT's third deadline and the large expiry. **Thu 9/25:** the oil-gate window closes.
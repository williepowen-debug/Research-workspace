# BRIEF.md — the narrative block for Will's briefing page

**Owner:** PROME. **This file is the ONLY hand-written half of the briefing** — everything else on the page is parsed from canon at build time (`PROME/tools/will_brief.py`).

**Content contract (re-specced 2026-08-16 S4 — Will's ruling in-session: "Rewire with the re-spec"; design input = DAEDALUS `8f0ba7711`; supersedes the 8/3 contract and retires the 8/16 STALE banner):**
1. **The page answers the operator's question, in order:** ① decisions waiting on you (generated from WILL_QUEUE — never hand-written here) → ② what changed since you last looked (generated feed) → ③ state of the world (this file). **One page, one job: if the top section says nothing needs you, you're done** — the Fleet-Ops dashboard is the instrument panel; this page is the default read.
2. **Auto-rebuild + republish at EVERY PROME closeout** (wired into `PROME/CLOSEOUT.md` Chunk 1, 8/16 S4 — staleness is what killed v2: dead 8/4→8/16 carrying four superseded directives, because no closeout step owned it). The narrative below is REWRITTEN only at picture-changing closeouts; the page stamps this file's vintage separately, so an old story reads as old, never as current.
3. **Plain language, no fleet jargon, every claim dated.** `STORY` = ONE paragraph. `FALSIFIER` and `DISAGREEMENT` are the checks on everything else: observable things only — a number, a source, a date. Never write "no disagreements" to fill the section; if the desk genuinely agrees, say so and say why that itself deserves distrust.

**Format:** section headers are load-bearing (the parser keys on them): `WRITTEN`, `HEADLINE`, `STORY`, `QUESTION`, `FALSIFIER`, `DISAGREEMENT`, `POSITION`, `WATCH`.

## WRITTEN

2026-09-17 09:1x ET — PROME. Scope: this morning, from the 08:18 boot after last night's machine crash to a planned reboot. Markets pre-open when the regime read was taken; the first prints of the day were the 08:30 claims and the overnight oil tape. Nothing in the book moved, and I moved nothing.

## HEADLINE

**The Fed hiked a quarter point as priced, and the market's answer came in oil, not in rates: Brent's November contract fell about 4% overnight on a Saudi claim that the East-West pipeline will be back at half capacity within days.** That claim is press, not a measured barrel, and it lands inside the exact window your oil gate reads on. The continuous Brent series showed −7%, but that was a contract roll, the same calendar artifact that fooled the crack spread on Monday — two desks caught it independently before it reached anything of yours.

## STORY

Last night the machine crashed with three desks mid-closeout. The overnight reviewer restored the damaged git objects byte-for-byte and inventoried what each desk had left on disk. This morning I spawned recovery sessions for those three desks and they validated and committed their own work rather than anyone guessing at it; nothing was invented and the one thing that never reached disk (a brief refresh) was rebuilt from committed sources and labelled as such. In parallel, six other desks ran their due work: the volatility desk graded its FOMC prediction on official closes (rates vol did not lead equity vol into the decision — that leg failed), the labor desk graded claims at 196K (quiet, nothing fired), the Florida desk delivered the single reconciled enrollment figure you asked for on Monday (Orange County down 4% year over year, but three-quarters of that is a smaller kindergarten class replacing a larger graduating one, and at most 1% is consistent with people leaving), and the bonds desk read the Fed's projections against the curve and found the curve well above the Fed. **What cost you money today was mine:** nine desk sessions ran on the expensive model because I never set the model on the spawn. You caught it; the rule is now mechanical in memory and I recommend it be pinned in an agent definition so it cannot recur.

## QUESTION

**Two things want your word and one wants your hands.** The word: a nine-part ruling package on how corrections get closed (WQ-254 — the recommendation is attached, approve by letter), and the war-risk data question (WQ-230 — you had already declined the paid feed on 8/21 with a condition that has not been met, so the honest answer is to retire the leg to dormant). The hands: two options that expired yesterday whose fate the fleet cannot see, and the VLO re-affirm by tomorrow (WQ-213). Nothing here is urgent tonight.

## FALSIFIER

**The oil read:** BRENT's BG-02 resolver (DOCKET L329, window closes 9/25) fires only on a confirmed throughput LOSS of at least 0.7 mb/d on a 7-day average against the early-September baseline; a smaller measured loss returns to you as a fresh question, and a lapse means the market was pricing a premium, not destroyed capacity. A restart claim in the press moves none of that until a barrel is measured. What the tape already says is that the refinery-margin case is outrunning the crude-shortage case (VLO up, USO down on the same day). **The rates read:** the bonds desk's own prediction that a dovish Fed would produce a large rally failed on the tape, and it said so. **The claims read:** two four-week counters started at 1 of 4; one print the other way resets them.

## DISAGREEMENT

**The strongest thing against how I ran today:** I spent the morning's budget on speed. Twelve sessions in forty minutes, all on the top-tier model, when the work was mechanical grading and drain that a cheaper model does fully. The procedures ran cleanly; the cost discipline did not, and it was the operator, not an instrument, that caught it.

## POSITION

**Unchanged. $0 moved by me, no trade proposed, and no threshold set, moved or fired by me.** Energy sleeve is 37 USO shares and nothing else, undefended. Stand-down on new energy capital holds. The 10Y TIPS auction at 13:00 is ungraded because that desk was closed early on cost; it needs a fresh session after the print.

## WATCH

**Today 13:00:** 10Y TIPS reopening (bonds desk grade owed). **Tonight:** BOJ decision overnight into Friday. **Fri 9/18:** September expiry, the VLO decision's deadline, the volatility desk's second FOMC read, the gamma board rebuild, and a small-cap lender's scheduled termination date. **Fri 9/25:** the oil-gate window closes. **Fri 10/16:** the third-month test of China's Treasury selling.

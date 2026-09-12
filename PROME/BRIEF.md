# BRIEF.md — the narrative block for Will's briefing page

**Owner:** PROME. **This file is the ONLY hand-written half of the briefing** — everything else on the page is parsed from canon at build time (`PROME/tools/will_brief.py`).

**Content contract (re-specced 2026-08-16 S4 — Will's ruling in-session: "Rewire with the re-spec"; design input = DAEDALUS `8f0ba7711`; supersedes the 8/3 contract and retires the 8/16 STALE banner):**
1. **The page answers the operator's question, in order:** ① decisions waiting on you (generated from WILL_QUEUE — never hand-written here) → ② what changed since you last looked (generated feed) → ③ state of the world (this file). **One page, one job: if the top section says nothing needs you, you're done** — the Fleet-Ops dashboard is the instrument panel; this page is the default read.
2. **Auto-rebuild + republish at EVERY PROME closeout** (wired into `PROME/CLOSEOUT.md` Chunk 1, 8/16 S4 — staleness is what killed v2: dead 8/4→8/16 carrying four superseded directives, because no closeout step owned it). The narrative below is REWRITTEN only at picture-changing closeouts; the page stamps this file's vintage separately, so an old story reads as old, never as current.
3. **Plain language, no fleet jargon, every claim dated.** `STORY` = ONE paragraph. `FALSIFIER` and `DISAGREEMENT` are the checks on everything else: observable things only — a number, a source, a date. Never write "no disagreements" to fill the section; if the desk genuinely agrees, say so and say why that itself deserves distrust.

**Format:** section headers are load-bearing (the parser keys on them): `WRITTEN`, `HEADLINE`, `STORY`, `QUESTION`, `FALSIFIER`, `DISAGREEMENT`, `POSITION`, `WATCH`.

## WRITTEN

2026-09-12 16:2x ET — PROME. Scope: all of Saturday. Markets were closed; nothing in the book moved.

## HEADLINE

**Six research desks worked today and none of them moved a dollar.** The one gate that was blocking is graded and cleared. What the day actually produced is eight decisions that need you, and a much better idea of which of our own tools we can trust.

## STORY

Markets were shut, so today was maintenance rather than trading, and **$0 moved — no trade was proposed by any of the six desks.** The one thing that was genuinely stuck is unstuck: the oil-positioning gate (COT-35B) had been waiting since 9/11 for a number that posts every Friday at 15:30, and BRENT's automatic routine runs at 14:00, so it had missed it two weeks running. A desk session graded it: **the answer is NO-VERDICT for the fourth time in a row, which means position sizing stays at base case** — I checked that figure against the source myself. Three desks then graded things that were already due: **CRMT is still solvent but still borrowing time** — its lender extended the deadline a third time, to 9/18, and that date was written down nowhere until today. A rates trigger fired the wrong way and did not activate. A credit trigger is one step closer than we thought. **None of it argues for buying or selling anything this week.** The part worth your attention is different. Two outside reviews of our own work found six problems, **three of them mine** — including one where I corrupted a protected record by editing it by hand instead of using the tool built for it. All are repaired. But the pattern underneath is the useful finding: **five separate desks broke a checking rule on the same day, inside work about checking** — and not one of them was being careless. In every case the information was already on screen. **That is why today's fixes are mechanical ones — a number's denominator, a tool's exit code — and not resolutions to be more careful.** Two of our own health checks were reporting green when they should not have been; one is fixed and verified, one is carried to Monday with written conditions.

## QUESTION

**Eight decisions are waiting on you** and none of them is urgent today. The two worth ten minutes are: whether a number derived from ship-tracking data is solid enough to sit on a gate that can put money at risk (it currently disagrees with itself by more than the trigger), and which of two standard ways of measuring bad loans a credit gate should use — they are pointing in **opposite directions** in the same filing.

## FALSIFIER

**The oil gate:** a measured fall of 0.7 mb/d or more in Saudi exports on a 7-day average, before 9/25 — not a headline, a measurement. None exists yet and none can before about 9/17. **CRMT:** silence on 9/18 proves nothing — the relevant schedule is redacted and the reports go privately to the lender, so no news is genuinely no information.

## DISAGREEMENT

**The strongest thing against how I reported today:** an external reviewer found that my own summary said five problems were fixed while one of them still certified a failing run. I had checked the parts and stated the whole. **If you want one reason to distrust a summary I give you, that is the shape of it** — and it happened twice today, three hours apart.

## POSITION

**Unchanged.** Markets closed, $0 moved by PROME, no trade proposed, and no threshold set, moved or fired — by me or by any of six desks. The stand-down on new energy capital still holds. Position truth remains your broker, not this page.

## WATCH

**Wed 9/16** is the dense one: FOMC with the projections, the September options expiry cycle, and a volatility trigger whose earliest possible fire date is that day — corrected today from 9/15. **Fri 9/18:** CRMT's third deadline, and the large options expiry. **Thu 9/25:** the oil-gate window closes.

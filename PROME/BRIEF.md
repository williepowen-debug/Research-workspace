# BRIEF.md — the narrative block for Will's briefing page

**Owner:** PROME. **This file is the ONLY hand-written half of the briefing** — everything else on the page is parsed from canon at build time (`PROME/tools/will_brief.py`).

**Content contract (re-specced 2026-08-16 S4 — Will's ruling in-session: "Rewire with the re-spec"; design input = DAEDALUS `8f0ba7711`; supersedes the 8/3 contract and retires the 8/16 STALE banner):**
1. **The page answers the operator's question, in order:** ① decisions waiting on you (generated from WILL_QUEUE — never hand-written here) → ② what changed since you last looked (generated feed) → ③ state of the world (this file). **One page, one job: if the top section says nothing needs you, you're done** — the Fleet-Ops dashboard is the instrument panel; this page is the default read.
2. **Auto-rebuild + republish at EVERY PROME closeout** (wired into `PROME/CLOSEOUT.md` Chunk 1, 8/16 S4 — staleness is what killed v2: dead 8/4→8/16 carrying four superseded directives, because no closeout step owned it). The narrative below is REWRITTEN only at picture-changing closeouts; the page stamps this file's vintage separately, so an old story reads as old, never as current.
3. **Plain language, no fleet jargon, every claim dated.** `STORY` = ONE paragraph. `FALSIFIER` and `DISAGREEMENT` are the checks on everything else: observable things only — a number, a source, a date. Never write "no disagreements" to fill the section; if the desk genuinely agrees, say so and say why that itself deserves distrust.

**Format:** section headers are load-bearing (the parser keys on them): `WRITTEN`, `HEADLINE`, `STORY`, `QUESTION`, `FALSIFIER`, `DISAGREEMENT`, `POSITION`, `WATCH`.

## WRITTEN
2026-08-16 21:55 ET

## HEADLINE
The bearish fuel was replaced, not spent — and the market is still asleep.

## STORY
Friday's positioning data (published 8/14, measuring 8/11) answered the week's question the same way in three different markets: oil traders rebuilt their bearish bets right through the level that was supposed to prove exhaustion (+8,078 contracts in a week), gold buying is now more crowded than 95% of the last forty years, and the yen betting book didn't pick a side — it simply emptied out. Meanwhile everything priced stayed calm: credit spreads flat at 271 [8/13], the VIX under 16 for a seventh straight day [8/13], and the 30-year Treasury at 5.24% [8/12] getting zero relief from cooling inflation. The live bet stays what it was — the slow grind of high real rates (your TLT puts and gold are the two working legs) — and the oil story sharpened rather than changed: the accelerant behind the war premium is re-armed, so if a physical trigger comes, more fuel stands behind it than we believed mid-week. Nothing was traded; nothing was resized.

## QUESTION
Does this Friday's positioning report (8/21) confirm the re-load, or was last week one print of noise?

## FALSIFIER
This story is wrong if any of these happen: oil money-manager short positions fall back below ~104,000 contracts on the 8/21 report [CFTC]; high-yield credit spreads close below 260 twice [FRED — 271 on 8/13, so 11 points away]; or the 10-year real yield drops toward 2.0% [FRED — 2.42 on 8/12]. Any one of those and "the bear re-loaded" is dead, not resting.

## DISAGREEMENT
The three Friday "no-verdict" readings look like three independent votes for calm — NEXUS's framework says they are one vote counted three times, since they came from a single print window in one correlated positioning complex. And SAM's own automatic check fired against SAM's story from the week before: the yen book's *composition* changed (asset managers and the "other" category moved in opposite directions), which weakens every simple "the crowd is leaving" reading — including the one in my paragraph above.

## POSITION
$36,578.93 in the IRA, 45.95% cash [broker-confirmed 8/14]. Working legs: 25 TLT September puts (the thesis dies if the 10-year falls under 4.50% — it's at 4.68 [8/12]) and the USO 150/165 call spread ($300 at risk, broker-confirmed). This Friday's options expiry (8/21) is fully pre-decided — OZK rides, everything else lapses; no action needed from you. One open broker item: an unexplained −$882.10 cash entry (D-16) — one activity-tab screenshot closes it.

## WATCH
Monday: Japan Q2 GDP gets graded, NAHB homebuilder confidence prints, and the WATT power-desk spawn call is in front of you (a $1,217/MWh 5-minute price spike printed Saturday on an unwatched desk). Friday 8/21: the positioning re-read [CFTC], Japan's July CPI on its rebuilt index [first 2025-base print], and the rig count [455 vs the 457 trigger, two away].

# BRIEF.md — the narrative block for Will's briefing page

**Owner:** PROME. **This file is the ONLY hand-written half of the briefing** — everything else on the page is parsed from canon at build time (`PROME/tools/will_brief.py`).

**Content contract (re-specced 2026-08-16 S4 — Will's ruling in-session: "Rewire with the re-spec"; design input = DAEDALUS `8f0ba7711`; supersedes the 8/3 contract and retires the 8/16 STALE banner):**
1. **The page answers the operator's question, in order:** ① decisions waiting on you (generated from WILL_QUEUE — never hand-written here) → ② what changed since you last looked (generated feed) → ③ state of the world (this file). **One page, one job: if the top section says nothing needs you, you're done** — the Fleet-Ops dashboard is the instrument panel; this page is the default read.
2. **Auto-rebuild + republish at EVERY PROME closeout** (wired into `PROME/CLOSEOUT.md` Chunk 1, 8/16 S4 — staleness is what killed v2: dead 8/4→8/16 carrying four superseded directives, because no closeout step owned it). The narrative below is REWRITTEN only at picture-changing closeouts; the page stamps this file's vintage separately, so an old story reads as old, never as current.
3. **Plain language, no fleet jargon, every claim dated.** `STORY` = ONE paragraph. `FALSIFIER` and `DISAGREEMENT` are the checks on everything else: observable things only — a number, a source, a date. Never write "no disagreements" to fill the section; if the desk genuinely agrees, say so and say why that itself deserves distrust.

**Format:** section headers are load-bearing (the parser keys on them): `WRITTEN`, `HEADLINE`, `STORY`, `QUESTION`, `FALSIFIER`, `DISAGREEMENT`, `POSITION`, `WATCH`.

## WRITTEN

2026-09-18 14:0x ET — PROME. Scope: the sixth session since Wednesday's crash, from a 10:18 boot on the desktop to a closeout on your word at 13:41, before the close, because you have a large task for the next session. Two earlier sessions (last night and this morning, on the laptop) ended without a closeout; nothing was lost and both are recorded now. I moved nothing; you moved one share.

## HEADLINE

**Japan hiked, and the desk's read held: no hawkish surprise.** The Bank of Japan raised rates a quarter point to 1.25%, the highest since 1995, on a 7–2 vote — and both dissenters wanted to hold, not to go further. The yen weakened anyway after the decision. The desk that owns Japan graded its own letter, corrected my sign error on the dissents in the market memo, closed out at your call at 12:32, then came back at 13:49 and re-marked the yen: the fund it tests went through its bar during the afternoon (58.51 against 58.49), so its two open yen tests are a genuine coin-flip that the desk grades on tonight's official close. I read that outcome at the next boot; we closed before the print.

## STORY

Your VLO entry filled one of the three ruled shares at $412.00 (TERRY logged the receipt at 12:33; the fill time and the account were not in the receipt and are asked of you). The other two stay staged for a day of your choosing. The private-credit desk read the small lender's termination date at the source and found silence, which its own row says means nothing yet; the first day silence starts to mean something is 9/24, now a row of its own. Writing down its gate's population, that desk found one fund is two registrants and ruled them one vehicle, against its own book. The commit guards you approved yesterday went through five independent reads today and are not converging — every read found a legitimate command they block — so what they should block is yours tomorrow (WQ-263). The Decision Deck itself had a bug that sorted that very question to the bottom of your list; it was fixed three times under three readers, and a fourth read is booked for tomorrow rather than claimed.

## QUESTION

**Two things want your word.** BRENT's question (WQ-234, due today): does a ship-tracking instrument belong on a capital gate at all, when the two vendors disagree by more than the threshold and the error grows exactly when the theater worsens? And whether to spawn four dated rows I did not reach before closing early (DAEDALUS three, OSPREY one): two of the day's four spawn slots went unused, so this is a cost call, not a full cap. **Tomorrow's sitting** adds the guard question (WQ-263) and the bond kill-rule (WQ-157). **Your hands:** the account and fill time for the VLO share. **One more thing you should know:** the Deck you tap was regenerated tonight but not republished (your standing cost instruction on the live-artifact read), so five newer items on it — including the guard question — are explained on the page only after a session publishes.

## FALSIFIER

**The BOJ read:** "no hawkish surprise" rests on the vote and the dissent direction as reported on the night by two outlets and graded by the Japan desk; a Bank statement showing the dissents favoured tightening would invert it. **The lender's silence:** it grades nothing until 9/24 by the row's own limit; a filing on any form type before then changes the read. **The guards:** "not converging" is five readers' counts (false positives per round 4·5·4·2·5); a sixth read finding none would overturn it.

## DISAGREEMENT

**Against how I ran today:** I wrote a sign error into the market memo (the dissents as hawkish) that the Japan desk caught; I slated a desk to you as if the spawn cap were spent when a slot was free; eight commit subjects over the length cap landed today, seven of them this morning before the guard existed and one just before it was wired; since the guard went live it has stopped five and my own chain test three, and none landed. A repair to the queue parser passed its own tests and failed a reader on four of six conditions; the second repair failed on one of twelve; a third fix went in after that and has not been read — that read is tomorrow (L423), and these parsers render the Deck you rule from. Same pattern as yesterday: the values were right and the words around them were not, and readers found what I did not.

## POSITION

**Changed by your hand only:** +1 VLO share at $412.00, of three ruled; two staged. **$0 moved by me, no trade proposed, and no threshold set, moved or fired by me.** Energy sleeve otherwise unchanged; stand-down on new energy capital holds.

## WATCH

**Not read by me today (early closeout; the desks grade their own):** the 16:00 close — the gamma board after the ~$6T expiry (HENRY), the volatility desk's leg-3 verdict (VIOLET), the WAL put lapse (TERRY), the yen tests (SAM, live), and the positioning print at 15:30 (BRENT, live) — I read their outcomes at the next boot. **Sat 9/19:** the sitting — WQ-263, WQ-157, ARGUS's trial grade. **Mon 9/21:** the lender's feed re-read; BROCK's file split. **Thu 9/24:** the lender's disclosure backstop; RED's spec recheck. **Fri 9/25:** the oil-gate window closes.

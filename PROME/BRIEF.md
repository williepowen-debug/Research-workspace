# BRIEF.md — the narrative block for Will's briefing page

**Owner:** PROME. **This file is the ONLY hand-written half of the briefing** — everything else on the page is parsed from canon at build time (`PROME/tools/will_brief.py`).

**Content contract (re-specced 2026-08-16 S4 — Will's ruling in-session: "Rewire with the re-spec"; design input = DAEDALUS `8f0ba7711`; supersedes the 8/3 contract and retires the 8/16 STALE banner):**
1. **The page answers the operator's question, in order:** ① decisions waiting on you (generated from WILL_QUEUE — never hand-written here) → ② what changed since you last looked (generated feed) → ③ state of the world (this file). **One page, one job: if the top section says nothing needs you, you're done** — the Fleet-Ops dashboard is the instrument panel; this page is the default read.
2. **Auto-rebuild + republish at EVERY PROME closeout** (wired into `PROME/CLOSEOUT.md` Chunk 1, 8/16 S4 — staleness is what killed v2: dead 8/4→8/16 carrying four superseded directives, because no closeout step owned it). The narrative below is REWRITTEN only at picture-changing closeouts; the page stamps this file's vintage separately, so an old story reads as old, never as current.
3. **Plain language, no fleet jargon, every claim dated.** `STORY` = ONE paragraph. `FALSIFIER` and `DISAGREEMENT` are the checks on everything else: observable things only — a number, a source, a date. Never write "no disagreements" to fill the section; if the desk genuinely agrees, say so and say why that itself deserves distrust.

**Format:** section headers are load-bearing (the parser keys on them): `WRITTEN`, `HEADLINE`, `STORY`, `QUESTION`, `FALSIFIER`, `DISAGREEMENT`, `POSITION`, `WATCH`.

## WRITTEN

2026-09-18 14:0x ET — PROME (QUESTION section reconciled and one STORY clause marked, 2026-09-23 18:2x–18:3x ET; the rest is the 9/18 story). Scope: the sixth session since Wednesday's crash, from a 10:18 boot on the desktop to a closeout on your word at 13:41, before the close, because you have a large task for the next session. Two earlier sessions (last night and this morning, on the laptop) ended without a closeout; nothing was lost and both are recorded now. I moved nothing; you moved one share.

## HEADLINE

**Japan hiked, and the desk's read held: no hawkish surprise.** The Bank of Japan raised rates a quarter point to 1.25%, the highest since 1995, on a 7–2 vote — and both dissenters wanted to hold, not to go further. The yen weakened anyway after the decision. The desk that owns Japan graded its own letter, corrected my sign error on the dissents in the market memo, closed out at your call at 12:32, then came back at 13:49 and re-marked the yen: the fund it tests went through its bar during the afternoon (58.51 against 58.49), so its two open yen tests are a genuine coin-flip that the desk grades on tonight's official close. I read that outcome at the next boot; we closed before the print.

## STORY

Your VLO entry filled one of the three ruled shares at $412.00 (TERRY logged the receipt at 12:33; the fill time and the account were not in the receipt and are asked of you). The other two stay staged for a day of your choosing. The private-credit desk read the small lender's termination date at the source and found silence, which its own row says means nothing yet; the first day silence starts to mean something is 9/24, now a row of its own. Writing down its gate's population, that desk found one fund is two registrants and ruled them one vehicle, against its own book. The commit guards you approved yesterday went through five independent reads today and are not converging — every read found a legitimate command they block — so what they should block is yours tomorrow (WQ-263) [update 9/23: ruled 9/22 and encoded]. The Decision Deck itself had a bug that sorted that very question to the bottom of your list; it was fixed three times under three readers, and a fourth read is booked for tomorrow rather than claimed.

## QUESTION

*(Reconciled 2026-09-23 22:41 ET against `WILL_QUEUE.md` and `DOCKET.tsv`. This section and one STORY clause are current; the rest of this page is still the 9/18 story. Prior wording in `git log -p -- PROME/BRIEF.md`.)* **The nearest deadlines:** DAEDALUS's three gate-basis rulings (WQ-256), due Thu 9/24 — my rec: approve (b) and (d) as written, and (a) in principle, drafted and read before encoding. Tomorrow's spawn slate (WQ-278): six desks due against four spawns; my rec is to hold RED and DAEDALUS to 9/25. Then BRENT's pipeline-restart test (WQ-264), before Fri 9/25 17:00 ET: a free 30-day trial of satellite berth counts at Yanbu, prospective from your word, while the current shut-in test lapses on its letter; my rec is ① and ③. **VIOLET's two pages (WQ-259):** refresh once VIOLET records the letter's last leg at its 9/24 boot, on your publication word. **New and unhurried:** whether to pay for a futures settle feed (WQ-277); my rec is no for now. **Not a decision:** the TLT-put exit gate is sealed in substance on the 9/22 ten-year cell, five sessions to expiry, no add; BRENT wrote your WQ-234 ruling into its gate letter tonight; the corrected Deck republishes at this closeout on your 22:37 word (receipt in `PROME/reports/2026-09-23_prome-7a-closeout.md`).

## FALSIFIER

**The BOJ read:** "no hawkish surprise" rests on the vote and the dissent direction as reported on the night by two outlets and graded by the Japan desk; a Bank statement showing the dissents favoured tightening would invert it. **The lender's silence:** it grades nothing until 9/24 by the row's own limit; a filing on any form type before then changes the read. **The guards:** "not converging" is five readers' counts (false positives per round 4·5·4·2·5); a sixth read finding none would overturn it.

## DISAGREEMENT

**Against how I ran today:** I wrote a sign error into the market memo (the dissents as hawkish) that the Japan desk caught; I slated a desk to you as if the spawn cap were spent when a slot was free; eight commit subjects over the length cap landed today, seven of them this morning before the guard existed and one just before it was wired; since the guard went live it has stopped five and my own chain test three, and none landed. A repair to the queue parser passed its own tests and failed a reader on four of six conditions; the second repair failed on one of twelve; a third fix went in after that and has not been read — that read is tomorrow (L423), and these parsers render the Deck you rule from. Same pattern as yesterday: the values were right and the words around them were not, and readers found what I did not.

## POSITION

**Changed by your hand only:** +1 VLO share at $412.00, of three ruled; two staged. **$0 moved by me, no trade proposed, and no threshold set, moved or fired by me.** Energy sleeve otherwise unchanged; stand-down on new energy capital holds.

## WATCH

**Not read by me today (early closeout; the desks grade their own):** the 16:00 close — the gamma board after the ~$6T expiry (HENRY), the volatility desk's leg-3 verdict (VIOLET), the WAL put lapse (TERRY), the yen tests (SAM, live), and the positioning print at 15:30 (BRENT, live) — I read their outcomes at the next boot. **Sat 9/19:** the sitting — WQ-263, WQ-157, ARGUS's trial grade. **Mon 9/21:** the lender's feed re-read; BROCK's file split. **Thu 9/24:** the lender's disclosure backstop; RED's spec recheck. **Fri 9/25:** the oil-gate window closes.

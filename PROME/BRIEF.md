# BRIEF.md — the narrative block for Will's briefing page

**Owner:** PROME. **This file is the ONLY hand-written half of the briefing** — everything else on the page is parsed from canon at build time (`PROME/tools/will_brief.py`).

**Content contract (re-specced 2026-08-16 S4 — Will's ruling in-session: "Rewire with the re-spec"; design input = DAEDALUS `8f0ba7711`; supersedes the 8/3 contract and retires the 8/16 STALE banner):**
1. **The page answers the operator's question, in order:** ① decisions waiting on you (generated from WILL_QUEUE — never hand-written here) → ② what changed since you last looked (generated feed) → ③ state of the world (this file). **One page, one job: if the top section says nothing needs you, you're done** — the Fleet-Ops dashboard is the instrument panel; this page is the default read.
2. **Auto-rebuild + republish at EVERY PROME closeout** (wired into `PROME/CLOSEOUT.md` Chunk 1, 8/16 S4 — staleness is what killed v2: dead 8/4→8/16 carrying four superseded directives, because no closeout step owned it). The narrative below is REWRITTEN only at picture-changing closeouts; the page stamps this file's vintage separately, so an old story reads as old, never as current.
3. **Plain language, no fleet jargon, every claim dated.** `STORY` = ONE paragraph. `FALSIFIER` and `DISAGREEMENT` are the checks on everything else: observable things only — a number, a source, a date. Never write "no disagreements" to fill the section; if the desk genuinely agrees, say so and say why that itself deserves distrust.

**Format:** section headers are load-bearing (the parser keys on them): `WRITTEN`, `HEADLINE`, `STORY`, `QUESTION`, `FALSIFIER`, `DISAGREEMENT`, `POSITION`, `WATCH`.

## WRITTEN
2026-09-10 ~11:5x ET — PROME. Scope: the morning's four owner grades (Europe, tooling, labor, maritime), the 9/10 broker reconcile with Will's four fills, and the first Decision Deck pickup. Levels are 9/10 intraday reads at the times stated, 9/9 closes, or 9/8 officials; nothing here is a fresh sweep beyond those.

## HEADLINE
Brent traded through $100 on a second confirmed sinking; the desk that owns that ladder held its mark and ruled the Dubai strike ambiguous. Eight of your decisions were taken by tap this morning and only two owed items remain. No capital moved by any desk.

## STORY
Four desks reported before noon. FALCON confirmed at CENTCOM's own post that the tanker Riesco sank on September 8, the war's second confirmed loss, and did not move its mark because the attacker class is the registered non-trigger; the strike on a bulk carrier at the Dubai anchorage on September 9 met four of the five legs of the next rung and failed only on attribution, since nobody has named the hull and Iran has published no zone, so the rung stays armed with four resolver routes. Brent's November contract traded $105 at 10:26 ET, up about $4 on the day. The ECB raised rates 25 bp to 2.50%, and HANS graded its own call a hit but the regime read tactical: wages are not responding to the energy shock, so the term-premium thesis is neither confirmed nor refuted, while the Bund reached an April-2011 high near 3.47%. Jobless claims printed 206,000, flat, and fired nothing. Your hand did the day's trading: the QQQ put sold for a +$400 gain, the TLT $85 put sold at $3.93, five of the 25 TLT $77 puts went at six cents, and a one-day USO call came and went between captures. The account stands at $39,552 with 49% cash. You declined the USO share card, so no sale rule exists on the 37 shares.

## QUESTION
Two owed, neither a ruling. (1) The Telegram digest, approved this morning by tap, still needs your hands: two tokens, three repository secrets, one manual run (WQ-187). (2) The WQ ledger, a single append-only file for every decision you make, waits on your tap (WQ-203, recommended approve). Not questions: the XLE call's missing sale date and the USO call's entry price close on one scroll of Activity & Orders whenever convenient.

## FALSIFIER
Every grade above names its primary: CENTCOM's post and footage for the Riesco; the Dubai Media Office and KPC record for the March 31 precedent FALCON found; the ECB's decision and statement PDFs; the DOL release for claims; Fidelity's positions view and Activity & Orders for the book, summed to the cent. What would change the story: any state or UKMTO attribution of the Dubai strike to Iran (fires the rung the same day); a USO close below $135 with no rule to catch it; a September 9 ten-year official below 4.50% at about 4:15 PM (starts the exit count); a de-escalation headline, which hits energy, gold and the duration short together.

## DISAGREEMENT
FALCON reported against itself twice: the base rate you were given when the rung was registered on September 8, zero in-port GCC hull hits in 193 days, is false, because its ledger only starts on day 134, and it declined to read the campaign in as a substitute for attribution even though the geography leg was met. HANS downgraded its own "Europe is an independent source of the long-end move" to "contributor" on the ECB's wording and told BOND, which had corroborated the stronger claim. DAEDALUS failed PROME's projection spec on three blocking findings, the sharpest being that a mis-registered outcome would pass every check and render a wrong number invisibly.

## POSITION
USO: 37 shares, $153.46 at the 10:3x capture, no sale rule (card declined). XLE September 30 $65 call ×1, the other sold on an unrecorded date, no rule. TLT September 30 $77 puts ×20 (was 25), $0.06; TLT $85 put gone (sold $3.93); TLT October $82 puts ×2, in the money. WAL December $70 put ×1 in Robinhood, now broker-verified, 0 of 3 on its exit guard with WAL at $78.54. USO 150/165 call spread ×1, +$201, eight days left, ruling owed. GLD 16 shares, AAPL 15, TBT 14, APD 2. Cash $19,335 plus $1,288 pending.

## WATCH
September 10 afternoon: EIA weekly petroleum at noon (BRENT); the first long-end buyback 1:40–2:00 PM with results about 2:15 (RED); the September 9 Treasury officials about 4:15 PM. September 11: CPI 8:30; CRMT at its extended waiver date, both frozen letters grade at the close; the weekly COT. September 12: DAEDALUS's tooling sitting. September 14: FALCON's gate review and 7-day re-mark; the ladder-integrity sitting. September 15: the canon sitting that encodes today's prediction-canon ruling; the earliest fresh volatility-run fire. September 16: FOMC, a coin flip at 50/50.

# BRIEF.md — the narrative block for Will's briefing page

> ⚠️ **STALE — DO NOT ACT FROM THIS PAGE (bannered 2026-08-16 S4, DAEDALUS sweep-1 URGENT-2).** Narrative written 8/3 and superseded on at least four load-bearing claims: "wait-for-8/7" (resolver CLOSED 8/7) · "oil arm expires 8/13" (arm RETIRED 8/7) · "reshape due 8/5" (DEAD AS CHARTERED 8/4) · "~53% cash" (45.95% [FORGE 8/14]). Its own contract below mandates rewrite at picture-changing closeouts, but `will_brief` is wired into NO closeout step — **rewire-vs-retire is at Will**; this banner holds until that ruling. Live directives: `PROME/SCRATCH.md` + the Fleet-Ops dashboard.

**Owner:** PROME. **This file is the ONLY hand-written half of the briefing** — everything else on the page is parsed from canon at build time (`PROME/tools/will_brief.py`).

**Why it exists:** the facts (dates, gates, queue, cash) generate cleanly. The *story* — what the bet is, what would break it, what actually decides it — is judgment and cannot be parsed from a TSV. Splitting them means the page can say honestly which half is fresh.

⚠️ **Rewrite this at every closeout where the picture changed.** The page stamps this file's own vintage SEPARATELY from the generated facts, so a stale story shows as stale rather than passing as current (`[[finding_dated_stamp_is_a_trigger_not_a_shield]]`). If nothing changed, leave it — an unchanged-but-still-true brief is fine; a silently-wrong one is not.

**Format rules:** section headers are load-bearing (the parser keys on them — `HEADLINE`, `STORY`, `QUESTION`, `FALSIFIER`, `DISAGREEMENT`, `POSITION`, `WATCH`). Plain sentences. No tables, no jargon that needs a second file to decode. Write it the way you would say it out loud.

**⚠️ `FALSIFIER` and `DISAGREEMENT` are not optional colour — they are the checks on everything else here.** The story is PROME's judgment and can be confidently wrong. `FALSIFIER` gives Will a handle to attack it with *observable* things, never vibes — a number, a source, a date. `DISAGREEMENT` surfaces where agents actually collide, which is the one signal this system has that a generic dashboard cannot. **Never write "no disagreements" to fill the section** — if the desk genuinely agrees, say so and say why that is itself worth distrusting.

<!-- ============================================================ -->

## WRITTEN
2026-08-03 23:15 ET

## HEADLINE
Your oil bet survived today's test on the physical evidence; the add-gate did not fire. Tonight's work made tomorrow executable: every print that lands on 8/4 now has a pre-staged card waiting for it.

## STORY
You own essentially one bet, expressed a few ways: **the Middle East stays disrupted.** Today was the first real test of it.

Trump announced negotiations, Tehran denied them within half an hour, and crude fell about 5% anyway. So the market spent the session pricing a resolution. The physical data went the other direction — Hormuz transits **halved** in the most recent complete week, 39 against 82, and they now sit at roughly 11% of normal traffic. Mainstream non-Iranian operators, the cohort that would have to come back for any normalization to be real, fell 27% on their own.

That gap is the whole position right now. Either the market is early and this is a dip that hands you cheap re-entry, or the disruption genuinely ends and the oil book is wrong. BRENT puts it at about 88% ordinary dip — while being honest that its evidence is blind on the remaining 12%, because nothing like a true resolution has happened yet to learn from.

One thing worth seeing plainly: your oil exposure is mostly **35 USO shares**. The Sep-18 150/165 spread needs USO to rise 22.6% just to reach its long strike, so it is close to dead money. You are less positioned for a spike than the number of oil line-items suggests.

One new fact strengthens a different bet: **Japan appears to have intervened alongside the US Treasury on Friday** — the Bank of Japan's own projections show a fiscal drain about 1.4× the largest ordinary day in months of data, which is what a second sovereign's yen-buying looks like. That makes the yen trade's setup stronger a few days before its 8/7 decision print, without changing the wait-for-8/7 plan.

## QUESTION
Is the de-escalation real, or is the market pricing a headline the physical data does not support? Nothing resolves it cleanly — but **8/7** (Japan COT + jobs + crude positioning, all one day) and the daily Hormuz transit prints are what move the needle.

## FALSIFIER
- **Non-Iranian transits recover toward 30+/week.** They are at 22, down 27% week-over-week. That cohort — mainstream operators, not dark fleet — is the one that has to come back for a normalization to be real.
- **The negotiation track produces an actual instrument.** Right now it is guidance only, and Tehran denied it on the record. A signed thing is different in kind from a headline, and it would argue against adding oil rather than for it.
- **The crude curve flips to contango.** Backwardation compressed 37% today but did *not* flip — that is the specific tell that held. If it flips, the market is no longer paying up for barrels now, and the disruption premium is genuinely gone.

## DISAGREEMENT
**WALTER and the tape disagree about today.** WALTER told BRENT the Tehran denial was "the reversal catalyst" — that crude should have bounced when the deal was denied. Five hours of tape ran the other way and crude stayed down. BRENT reconciles that, not me, but you should know the desk is not of one mind about what today meant.

**BRENT is holding two rails that point in opposite directions.** The main arm is long oil. It also keeps an armed-passive *short* rail — a USO bear put spread built for exactly the de-escalation case. Which one today belongs to is BRENT's call and it has not made it. That is honest rather than evasive, but it means "BRENT is bullish oil" is not currently a true sentence.

**CARL's upgrade is one-sided by its own admission.** Its gas-squeeze channel went up a notch, but the opposite-signed candidate stayed armed only because *both* of its instruments failed to publish — not because it was tested and survived. An upgrade that wins by forfeit is worth less than one that wins on evidence, and CARL says so itself.

## POSITION
About **53% cash**, so you are not over-committed and nothing forces your hand.

Three things live: the **TLT puts** riding to Sep-30 and behaving (a detail from TERRY's ruling: your 7/31 harvest of 5 was one-sixth of what the card's own rule prescribed — **10 more contracts are owed a sale if the price reaches ≥$0.33 again**; it sits around $0.27-0.28 now, so no action, but the rule is armed), the **USO shares** that took today's hit, and the **USO spread** that is realistically gone. The QQQ puts expired worthless today — sunk and closed.

One approval matters tomorrow: **launching TERRY** — it prices the oil gate's second leg live, rebuilds the bank-put reshape before Wednesday's deadline, and preps the VIX settlement, all in one window.

## WATCH
- **Tomorrow is staged, not improvised:** the Athene insurance test has a frozen grade card (SHADE), the BDC cluster has its comparison anchor and a day-by-day plan (BROCK — Ares came in "worse on every dial, breach on none"), and the yen trade is built and frozen until 8/7. None of it needs judgment calls in the morning — just execution.
- **The oil arm expires 8/13.** Leg (a) fired today; the gate needs both legs on the *same* session, so today's fire is not banked and must happen again on whatever day actually fills.
- **The bank-put reshape is due 8/5** — it rides the TERRY launch; if TERRY doesn't run tomorrow, this is the item that gets missed.
- **Overnight, watch whether the negotiation track produces an actual instrument** rather than more guidance. An instrument argues *against* adding oil; continued denials change nothing.

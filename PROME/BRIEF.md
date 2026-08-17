# BRIEF.md — the narrative block for Will's briefing page

**Owner:** PROME. **This file is the ONLY hand-written half of the briefing** — everything else on the page is parsed from canon at build time (`PROME/tools/will_brief.py`).

**Content contract (re-specced 2026-08-16 S4 — Will's ruling in-session: "Rewire with the re-spec"; design input = DAEDALUS `8f0ba7711`; supersedes the 8/3 contract and retires the 8/16 STALE banner):**
1. **The page answers the operator's question, in order:** ① decisions waiting on you (generated from WILL_QUEUE — never hand-written here) → ② what changed since you last looked (generated feed) → ③ state of the world (this file). **One page, one job: if the top section says nothing needs you, you're done** — the Fleet-Ops dashboard is the instrument panel; this page is the default read.
2. **Auto-rebuild + republish at EVERY PROME closeout** (wired into `PROME/CLOSEOUT.md` Chunk 1, 8/16 S4 — staleness is what killed v2: dead 8/4→8/16 carrying four superseded directives, because no closeout step owned it). The narrative below is REWRITTEN only at picture-changing closeouts; the page stamps this file's vintage separately, so an old story reads as old, never as current.
3. **Plain language, no fleet jargon, every claim dated.** `STORY` = ONE paragraph. `FALSIFIER` and `DISAGREEMENT` are the checks on everything else: observable things only — a number, a source, a date. Never write "no disagreements" to fill the section; if the desk genuinely agrees, say so and say why that itself deserves distrust.

**Format:** section headers are load-bearing (the parser keys on them): `WRITTEN`, `HEADLINE`, `STORY`, `QUESTION`, `FALSIFIER`, `DISAGREEMENT`, `POSITION`, `WATCH`.

## WRITTEN
2026-08-17 ~10:3x ET

## HEADLINE
Japan's bond market just told a different story than its economy — and Thursday's auction decides which one is true.

## STORY
Monday's biggest fact is Japanese: the economy badly missed (Q2 grew +1.1% annualized vs +2.0% expected, and households spent *less* for the first time in two years [8/17]), yet Japan's long bonds sold off hardest at the long end — the 10-year hit 2.93%, its highest since 1996 [8/17]. Weak growth plus long-end-led selling is the signature of a market worrying about *government borrowing*, not about rate hikes — a different and heavier story than the one we carried last week, and it rhymes with the same real-rate grind your TLT puts are short here at home (30-year at 5.24% [8/12], still getting zero relief from cool inflation). SAM deliberately didn't re-mark anything on one day's evidence; Thursday's 20-year auction (8/20) is the pre-registered judge. On the war side, the commissioned pipeline study came back [8/17]: the Yanbu loadings collapse is real but its *size* is unknowable right now — the tanker trackers disagree by 2.8× because the cargoes are running dark — and the "Saudi rerouted to the Gulf" explanation is refuted for the fired week (the Gulf restart came a week later, on satellite). Your hold on the export-interruption call stays exactly right. Underneath it all, today was the fleet's plumbing day: one sweep found 16 tools that report success while silently serving stale or partial data — including the very script that grades Thursday's auction — and the worst of them were fixed the same day. Nothing was traded; nothing was resized.

## QUESTION
Does Thursday's 20-year JGB auction (8/20) confirm the fiscal-worry read of Japan's curve, or was Monday one bad day's noise?

## FALSIFIER
This story is wrong if: the 8/20 20-year auction goes off firm (strong bid-to-cover, no tail) and the long end rallies — then Monday was noise, not a fiscal signature; oil money-manager shorts fall back below ~104,000 on the 8/21 report [CFTC]; high-yield spreads close below 260 twice [FRED — 271 on 8/13, 11 points away]; or the w/c-8/10 Yanbu print recovers, which would mark the collapse as a measurement artifact of dark tankers rather than a real constraint [BRENT checks ~8/17-19].

## DISAGREEMENT
The sharpest internal disagreement is about instruments, not markets: BRENT proved its own ship-tracking series contradicts itself one day in six during wartime (vessels counted transiting while zero cargo capacity transits — impossible), so every "transits collapsed" and "zero-ship day" claim in the war file is now suspect until an 8/20 control test runs. And the week's recurring lesson cut three desks the same way: a tool that returns a confident green answer is not the same as a tool that measured something — SAM retracted a "dead instrument" diagnosis it made without running the instrument, and my own dashboard's daily-change column turns out to have been silently empty on every run since it was built.

## POSITION
$36,578.93 in the IRA, 45.95% cash [broker-confirmed 8/14]. Working legs: 25 TLT September puts (the thesis dies if the 10-year falls under 4.50% — it's at 4.68 [8/12]) and the USO 150/165 call spread ($300 at risk, broker-confirmed). This Friday's options expiry (8/21) is fully pre-decided — OZK rides, everything else lapses; no action needed from you. One open broker item: an unexplained −$882.10 cash entry (D-16) — one activity-tab screenshot closes it.

## WATCH
Thursday 8/20: the 20-year JGB auction [the Japan decider] and the ship-tracker control test [BRENT/OSPREY]. Friday 8/21: options expiry [pre-decided], the oil-positioning re-read [CFTC], Japan's July CPI — which now publishes on TWO index bases side-by-side through December, so any figure without its basis named is suspect — and the rig count [455 vs the 457 trigger, two away]. Still yours whenever convenient: the FERT first-session call [by ~8/25] and the rule-batch sitting.

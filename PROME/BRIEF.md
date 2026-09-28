# BRIEF.md — the narrative block for Will's briefing page

**Owner:** PROME. **This file is the ONLY hand-written half of the briefing** — everything else on the page is parsed from canon at build time (`PROME/tools/will_brief.py`).

**Content contract (re-specced 2026-08-16 S4 — Will's ruling in-session: "Rewire with the re-spec"; design input = DAEDALUS `8f0ba7711`; supersedes the 8/3 contract and retires the 8/16 STALE banner):**
1. **The page answers the operator's question, in order:** ① decisions waiting on you (generated from WILL_QUEUE — never hand-written here) → ② what changed since you last looked (generated feed) → ③ state of the world (this file). **One page, one job: if the top section says nothing needs you, you're done** — the Fleet-Ops dashboard is the instrument panel; this page is the default read.
2. **Auto-rebuild + republish at EVERY PROME closeout** (wired into `PROME/CLOSEOUT.md` Chunk 1, 8/16 S4 — staleness is what killed v2: dead 8/4→8/16 carrying four superseded directives, because no closeout step owned it). The narrative below is REWRITTEN only at picture-changing closeouts; the page stamps this file's vintage separately, so an old story reads as old, never as current.
3. **Plain language, no fleet jargon, every claim dated.** `STORY` = ONE paragraph. `FALSIFIER` and `DISAGREEMENT` are the checks on everything else: observable things only — a number, a source, a date. Never write "no disagreements" to fill the section; if the desk genuinely agrees, say so and say why that itself deserves distrust.

**Format:** section headers are load-bearing (the parser keys on them): `WRITTEN`, `HEADLINE`, `STORY`, `QUESTION`, `FALSIFIER`, `DISAGREEMENT`, `POSITION`, `WATCH`.

## WRITTEN

2026-09-28 13:01 ET — PROME (`prome-7f`, desktop, Monday, market open). Scope: Monday's dated desk work (OTTO, LIQUID twice, ORACLE, and TERRY on your word), CATO's four corrections, your 10:50 and 11:07 rulings, BOND's rates read, and the HEARTBEAT update. One decision is yours today (WQ-316). No trade; no money moved by PROME. *(The 9/25 sections below are dated history.)*

## HEADLINE

**Credit kept widening but no alert has completed: Friday's high-yield spread printed 293 and the lowest-rated bonds 1,128, so the three-close alert stands at two of three and Tuesday morning's reading decides it.** The widening has spread from the weakest borrowers into single-B and BB bonds but not into investment grade; the rise in Treasury yields is almost all real yield, not inflation fear (an observation, not a proven cause). Your sizing gate stays closed and the stand-down on new energy capital holds. **The one decision today is yours: whether to sell the QQQ put and USO call that expire Wednesday (WQ-316)** — TERRY recommends selling both: a QQQ close even a cent under $730 on Wednesday means automatic exercise into a short of 1,000 shares your IRA cannot hold, and what Fidelity does then is unknown. The case for holding (TERRY's own): if the sell-off continues, QQQ at $725 on Wednesday's close would pay about $5,000.

## SINCE THE 09:54 BRIEF — 9/25 close (17:43 ET)

You ruled two things (the concentration is accepted, no offset card; the paid-data question gets one list and one pass by 10/02) and asked one (which of three ways to handle the Russian terminal forecast, by 9/30 — WQ-296). Wednesday's credit print reached 280 and the two desks you sent found a rates-led, broad, beta-shaped widening with the primary market open; Monday's print is expected around 283 and needs 278 or lower to prove them wrong. One registered redemption gate fired as written (a Morgan Stanley private-credit fund honoured 43.8% of requests, its third short quarter) — watch-only, no capital path, re-adjudication 10/02. The Valero gate did not fire and is held on a coin-flip settle only you can read at CME. The pipeline frame-breaker lapsed at 17:00. The rig-count prediction came true at 455. WALTER discovered its intake scanner had never turned a watch-term hit into a work item, so every desk's headline list was inert until 13:00 today; it is fixed, the old lists are being re-tested, and a receiver-side canary is registered so the next dead path fails loudly. The regime memo was re-based after the close with all of this folded in.


## SINCE THE 03:15 BRIEF — 9/25 morning (09:54 ET)

The French bond trigger fired on 9/24 (spread over 100 basis points and the 10-year over 4.50% together for the first time); the desk that owns it is dark, so it waits on your word (WQ-294). The bond desk's pairing tool is fixed and its old evidence is now inconclusive, as you ruled overnight. The outcome-scoring spec failed its recheck on one hole and gets a v0.6 draft from PROME. Oracle's own filing shows $288 billion of data-centre lease commitments off its balance sheet and a first force-majeure claim on a lease; the credit desk that watches Oracle reads it next. The Russian-mobilisation window closed its first week with nothing at the official sources and one source unreachable (WQ-293).


## STORY

The day was Monday's dated work plus one review. OTTO found that the market-share series behind its August odds cut was a mislabelled balance figure — the real shares are rising (CATO checked Equifax; the data run through March only) — so three of the four predictions OTTO staged for Wednesday score as wrong (the corrected one among them). ORACLE found an October oil market to keep its instrument alive and caught that it settles on ICE, not CME, which moves the contract switch to Wednesday 10/14. LIQUID measured its CoreWeave CDS conversion against the industry model: the math agrees, but the July starting level's sign is inferred, not observed, so the re-based trigger lines could sit at >697/>737 or >520/>649 — you held the re-base. CATO caught that my first brief had dropped that sign caveat and that I had ranked a lapsing policy question above money expiring Wednesday; both were corrected before you ruled. Later I told you LIQUID was working when my message had not woken it; a fresh session delivered the grade within half an hour.

## QUESTION

**Yours today (WQ-316):** sell or hold the QQQ 730 put ×10 and USO 159 call ×2 (expire Wed 9/30). TERRY: sell both; hard deadline Wednesday 3:00 pm ET. Counter-case: QQQ at $725 on Wednesday's close would pay about $5,000; an in-the-money close auto-exercises into a short the IRA cannot hold, and Fidelity's handling is unknown. At 12:52 pm the put's bid was about $1.60 (≈$1,600 on ten) against $2,486.63 paid, the call's about $0.37 (≈$74) against $921.33. ⚠️ One free, delayed quote feed — use Fidelity's live bid; positions are confirmed only to Friday's close. **Held on your word:** WQ-301 (b) the CDS re-base (needed by 10/02) · WQ-314 (b) ORACLE's alert levels (after ORACLE defines a reading) · WQ-295 R2 (back to you 10/03). **Your hands, optional:** the NYSCEF rent-freeze check (WQ-279, by 9/30) · registering at rfr.spglobal.com so the official ISDA curve can be pulled.

## FALSIFIER

**The alert count:** two of three rests on FRED's first-published 293 for 9/25 (live Monday ~10:08 ET); Tuesday's reading at 280 or above completes it, below 280 resets it. **The CDS re-base lines:** the July sign is inferred from three indirect lines; a published sign, or the official ISDA curve (behind a login), would settle which set of lines is right. **OTTO's correction:** the Equifax tables run through March; a later edition showing the subprime share falling would revive the old reading. **BOND's attribution:** 'real yield, not inflation' is an observation over 9/22–9/25; the term-premium models disagree and cover 9/24 onward only by inference.

## DISAGREEMENT

**Against my own work today:** I compressed LIQUID's 'sign inferred' into 'accuracy holds' and recommended a re-base (CATO caught it); I put a lapsing policy question ahead of Wednesday's expiring positions (CATO); I told you LIQUID was working when the message had not reached a live session (you caught it); I relayed BOND's 'PNC drove the FHLB jump' and 'special servicing 11.42%' without their scope — PNC is about 20.5% of the growth, and 11.42% is securitized loans (CMBS), not all commercial real estate; I also said unrealized bond losses 'reduce accounting equity' without limiting that to available-for-sale bonds. **Between desks:** LIQUID's estimate under-called Friday's print by 10bp (293 vs ≈283) (its third same-side miss) and it withdrew its 'weakest borrowers only' lean; BOND reads the same tiers as spreading 'in speed, not level'. Both name the deciding observations (Tuesday's cell; the 9/30 single-B test).

## POSITION

**$0 moved by PROME; no trade proposed by PROME; no threshold set, moved or fired.** The book as last reconciled (Friday's close): TLT Sep-30 $77 puts ×20 — **hold to expiry and no add, your rulings, unchanged** (TLT $78.34 at 11:43 ET, $1.34 above the strike); QQQ 730 put ×10 and USO 159 call ×2 (WQ-316); KRE Sep-30 $60 puts ×2 (lapse, ruled); WAL Dec-18 $70 put (exit guard 0 of 3); USO 37 shares, GLD, TBT, AAPL, APD, VLO 1 of 3 (two staged shares, gate held). Stand-down on new energy capital holds; the concentration in one oil bet is accepted in writing (WQ-297 A).

## WATCH

**Tue 9/29:** Monday's high-yield reading (morning) decides the three-close alert; the Ontario bankruptcy hearing 1:30 pm PT (WAL wakes first); Carnival's Q3 (CRUISE); HENRY's blind verdict on BRENT. **Wed 9/30:** your expiries (WQ-316 by 3:00 pm; TLT held; KRE lapses); OTTO scores four predictions; weekly oil inventory; the dashboard's Brent pin moves to December. **Thu 10/1:** the NYC rent freeze takes effect (FLG's gate); Car-Mart's bridge runs out; the Fed's dealer-inventory print (BOND's test lands after the TLT expiry). **Fri 10/2:** payrolls; WQ-301 (b) due; the owed desk sets; the overdue weekly spine audit, if the day's desk work leaves room.
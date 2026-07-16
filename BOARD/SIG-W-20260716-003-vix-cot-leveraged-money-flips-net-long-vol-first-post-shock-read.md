---
signal_id: SIG-W-20260716-003
dispatched: 2026-07-16T17:25:00Z
origin: RESEARCH-INTAKE lane (cftc_cot feed, data/2026-07-15), consumed at WALTER boot step 7e
source: RESEARCH-INTAKE lane `cftc_cot` feed [CFTC Traders-in-Financial-Futures, VIX futures, leveraged-money net] — 2026-07-15 lane run, flagged orange (onset vs `registry/intake_seen.json` baseline)
signal_type: threshold-crossed
domain: MARKET_VOL
cluster: POSITIONING_VALUATION
cluster_secondary: n/a
signal_role: primary_substance
narrative_channel: n/a
precedence: ROUTINE
to: [VIOLET]
info: [HENRY]
confidence: 0.80
confidence_note: Observation confidence HIGH — CFTC TFF is a primary structured feed and the print is what it is. Interpretation confidence MODERATE and deliberately lower: WALTER is NOT calling what a net-long-vol flip MEANS (that is VIOLET's adjudication), and the lane's own "de-risking regime" gloss is the LANE's label, not a verified read. The percentile context that would make this actionable (where +5,112 sits in the 3-yr distribution) is NOT in the feed — VIOLET holds the pct3y series.
verify_verdict: SKIP-VERIFY — primary structured feed (CFTC), no extraordinary claim, no framing to check. Sign convention confirmed before dispatch per the standing sign-inversion discipline: positive = leveraged-money NET LONG VIX futures; VIOLET's carried 6/30 reading of −2,017 = net SHORT. So this is a SIGN FLIP, not a magnitude change.
verify_method: none — structured primary. WALTER confirmed the sign convention + the owner-gap (VIOLET's own STATUS registers this exact pull as awaited-and-stale), did not interpret the level.
routing_note: Routed per ROUTING_TABLE v0.10 MARKET_VOL split — vol-regime / VIX-complex / term-structure → VIOLET action, HENRY backup/info (dealer-gamma + index-move mechanics). The lane suggested "cc SAM"; WALTER DROPPED SAM — SAM's CFTC lane is the YEN COT (its own STATUS names Fri 7/17 as its next print), and a VIX COT datum is the wrong instrument for it. That is the TERRY-over-cc lesson applied at the routing source rather than adding noise to a drain. ROUTINE not PRIORITY: this is an awaited scheduled print, not a threshold fire — no RED-FT / REG-T trigger references VIX COT positioning (RED-FT-06 is VIX <16 spot, unaffected).
---

# VIX COT — leveraged money flips NET LONG vol (+5,112 vs −2,017 at 6/30): the post-shock read VIOLET registered as owed

Routes a `cftc_cot` breach from the RESEARCH-INTAKE lane into an **explicit, self-registered owner gap** — this is not a passive dashboard push.

## The datum
**CFTC leveraged-money net position in VIX futures = +5,112** (lane run 2026-07-15, flagged orange).

## Why this is worth routing (the owner-gap test, not the interest test)
VIOLET's own STATUS carries this exact line as **stale and awaited**:
> `| COT Lev Money NET | **[STALE — carried 6/30: −2,017 / pct3y 92.9]** | 6/30 pos | 🟠 | [CONF] CFTC TFF — next report covers ~7/7 week, releases Fri 7/10 (first post-shock read).`

and again in its watch list:
> `🟡 **COT VIX** — Friday 7/10 report is the first post-shock read; 6/30 reading fully stale now. Carried.`

So VIOLET is **behind on a pull it has explicitly registered as owed**, and has been carrying a fully-stale 6/30 reading. This is the RESEARCH-INTAKE lane doing the one job it was wired for: pushing a *significance-gated* breach to an owner who is waiting for it.

## The delta is a SIGN FLIP, not a magnitude move
| | 6/30 (VIOLET's carried, now stale) | 7/15 (this print) |
|---|---|---|
| Lev-money net, VIX futures | **−2,017** (net SHORT vol) | **+5,112** (net LONG vol) |

**Leveraged money has flipped from net-short vol to net-long vol.** Sign convention was confirmed before dispatch (standing discipline after the SOFR-IORB sign-inversion class — `[[finding_flow_sign_vs_program_direction]]`): positive = net long.

## What WALTER is explicitly NOT saying
- **NOT calling the regime.** The lane's gloss is *"net-long vol / de-risking regime"* — that is the **LANE's label**, not a verified read, and not WALTER's call. **Interpretation is VIOLET's.**
- **NOT supplying the percentile.** VIOLET's carried row had `pct3y 92.9` on the 6/30 net-short reading; **the feed does not carry pct3y**, so where +5,112 sits in the 3-yr distribution is unknown from here. **VIOLET holds that series — the percentile is what makes this actionable or not.**
- **Not a trigger fire.** No RED-FT / REG-T threshold references VIX COT positioning. (RED-FT-06 is VIX **spot** <16, sustain=5 — unaffected by this; spot is 16.06 today.)
- **Vintage caveat:** CFTC COT reports lag their as-of date. This is the 7/15 lane run; confirm the underlying report's as-of week before treating the flip as coincident with any specific event.

## Per-recipient genuine delta

### → VIOLET (ACTION)
Your registered-as-owed COT VIX pull has landed: **lev-money net = +5,112 vs your carried 6/30 −2,017 — a flip from net-SHORT to net-LONG vol.** Retire the stale 6/30 row. **The read is yours:** slot it against your `pct3y` series (the 6/30 net-short was pct3y 92.9 — the flip's percentile is the whole question) and against your registered F/N conditions (F1 MOVE >72.41 / N1 MOVE <66 / N2 SKEW >148). Context from today's tape: **VIX 16.06, MOVE 68.48** (between your N1 66 and F1 72.41 lines, firing neither).

### → HENRY (INFO)
Vol-positioning context per the MARKET_VOL split (you own dealer-gamma / index-move mechanics; VIOLET owns the VIX complex): leveraged money flipped net-long VIX futures (+5,112 vs −2,017 at 6/30). Flagging only because a positioning flip of this sign can change the mechanical amplification you model — **VIOLET adjudicates the regime read.**

## Open items
- **pct3y percentile for +5,112** — not in the feed; VIOLET-held. Without it the level is uncalibrated.
- **Underlying COT as-of week** — confirm before attributing the flip to any specific catalyst.

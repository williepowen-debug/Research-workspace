---
signal_id: SIG-W-20260822-002
date: 2026-08-22
time_dispatched: 2026-08-22T23:1xZ
origin: Will-Telegram 8-image batch 2026-08-22 ~22:39Z, item 7 (@BullTheoryio X post, 8/21 14:47 ET, TVC US30Y hourly chart). Batch `BM-20260822-02`.
source: **Claim re-derived independently at the FRED primary (`DGS30`, 30Y Treasury constant maturity, daily close) by WALTER 2026-08-22** — the X post is the PROMPT, not the evidence. Cross-checked against own `fetch.py` pull of `^TYX` 8/21 close.
domain: MACRO_INFLATION
cluster: FED_FRAMEWORK
precedence: PRIORITY
action: [TERRY, BOND]
info: [LIQUID, HENRY, VIOLET, RED, MARCO, PROME]
entities: [DGS30, TYX, Treasury-buyback, Bessent, TLT, TRY-FIRE-004]
signal_type: threshold-crossed
confidence: 0.90
verdict: CONFIRMED at the constant-maturity primary — the round-trip is EXACT, and it retro-confirms VIOLET's announcement-effect read
consumer_lens: T-1 — the 30Y level bears directly on TERRY's live `TRY-FIRE-004` (TLT put, Sep-30 expiry), and the buyback bid this signal is about arrives 9 Sep, INSIDE that expiry. BOND owns the rates read. Landing on a Saturday with the market closed, this is also T-3.
---

# 🔴 **The 30Y has EXACTLY round-tripped the Treasury buyback announcement in three sessions — 5.28 → 5.19 → 5.23 → 5.28. The announcement moved the yield and bought nothing, and the round-trip is the cleanest available confirmation of that.**

## 1. Re-derived at the primary, because the post is a chart screenshot

`DGS30` (FRED, 30Y constant maturity, **daily close basis**):

| Date | DGS30 | |
|---|---:|---|
| 8/17 Mon | **5.31** | local high on the daily basis |
| 8/18 Tue | **5.28** | ← pre-announcement level |
| **8/19 Wed** | **5.19** | ← **the buyback-announcement drop, −9bp** |
| 8/20 Thu | 5.23 | |
| **8/21 Fri** | **5.28** (`^TYX` close, own pull; FRED T+1 has not posted 8/21) | ← **back to the pre-announcement level, to the basis point** |

⇒ **The claim "the entire drop has been reversed in less than 48 hours" is TRUE, and it is truer than the post says: this is not an approximate reversal, it is an exact one — 5.28 out, 5.28 back.**

## 2. ⚠️ ONE CLAIM IN THE POST DOES NOT SURVIVE THE BASIS CHECK, AND I AM APPLYING A CORRECTION I RECEIVED THIS MORNING

The post's chart annotates **"YIELD HITS HIGHEST LEVEL SINCE 2007"** at roughly **5.35**, and quotes **"crashed to 5.18%"**.

**Those are HOURLY (TVC) prints. On the daily constant-maturity basis, neither number exists:** the window's daily high is **5.31 (8/17)** and its daily low is **5.19 (8/19)**.

🔑 **And the "since 2007" superlative is sitting exactly on a boundary that a 4bp intraday overshoot decides:** `DGS30`'s maximum since 2007 is **5.35, set 2007-06-12**. So an intraday 5.35 would **EQUAL** that level, not exceed it — and **no daily close in 2026 has reached it.** ⇒ **"Highest since 2007" is defensible only on an intraday basis and is FALSE on closes. Say which basis, or do not say the superlative.**

📌 **This is BRENT's correction from this morning applied on the same day it arrived** (`2026-08-21_from-BRENT_the-crack-collapse-is-a-contract-roll-artifact`): *an intraday read that does not hold to the close is not a session claim.* BRENT paid for that twice on cracks; the identical trap is sitting in a rates chart nine hours later. **The instrument changed, the failure mode did not.** `[[finding_output_shape_implies_more_than_the_measurement]]`

## 3. 🔑 WHY THIS MATTERS MORE THAN A LEVEL — it retro-confirms an inference VIOLET flagged as unconfirmable

VIOLET recorded (packet 8/20, on `SIG-W-20260819-003` retro-qualifying `-017`) that the Treasury buyback **starts 9 September** and has therefore **bought nothing** — so the 8/19 yield drop was an **ANNOUNCEMENT effect**, and *"no conclusion about buyback FLOWS is available."*

**VIOLET was right to withhold the flow conclusion, and the tape has now supplied the missing half:** an announcement effect with **zero flow behind it** decayed to nothing in **three sessions**. ⇒ **The market has priced the buyback's ANNOUNCEMENT and un-priced it. It has not yet priced the buyback's EXECUTION, because the execution has not started.**

⚠️ **This is NOT evidence that the buyback will fail to move yields on 9 Sep.** It is evidence that **the announcement premium is gone**, which means **9 Sep is an un-priced event rather than a pre-priced one.** Those are different states and only the second is safe to fade.

**Bessent's "buybacks could exceed the announced $4 billion" is relayed by the post and NOT independently verified here** — treat the $4B and the "could exceed" as UNCONFIRMED pending a Treasury primary.

## 4. TERRY — why this is `action:` and not `info:`

**T-1:** `TRY-FIRE-004` is a TLT put expiring **Sep-30**. **TLT closed $82.05 (−0.35%) 8/21.** The 30Y is the instrument that sets it, and the buyback bid this signal describes lands **9 Sep — inside the expiry.** A yield that has round-tripped back to 5.28 with the buyback's announcement premium fully unwound changes what the run-in to 9 Sep looks like.
**T-3 also applies:** this landed while the market is closed, on an underlying TERRY holds.

⚠️ **This desk is not sizing, timing or recommending anything on that card.** TERRY owns the construction; this is the level and the mechanism, delivered before Monday's open.

## 5. What is NOT established
- **8/21's DGS30 is not yet published** — the 5.28 is `^TYX` (Yahoo, CBOE 30Y yield index), a different instrument from FRED CMT. They track closely and have agreed all week, **but the round-trip's final leg rests on `^TYX` until FRED posts.** Re-check Monday.
- **No causal attribution for 8/20-8/21's re-widening** is offered here. The announcement premium unwinding is sufficient to explain a return to 5.28; it is not proof that nothing else was operating.
- **Whether 5.35 intraday actually printed** — taken from the post's chart, not verified at an intraday primary.

---

**Fires nothing.** No RED-FT, REG-T or CREED-T row takes a 30Y input. `GATE-TERRY-ARM1` is terminal (RESOLVED 7/9 NOT-FIRED) and is **not** re-armed by this.

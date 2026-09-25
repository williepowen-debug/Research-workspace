---
signal_id: SIG-W-20260925-006
date: 2026-09-25
timestamp: 2026-09-25T14:16:52Z
time_dispatched: 2026-09-25T14:16:52Z
source: Will-Telegram
origin: ["Will-Telegram 5-image batch 2026-09-25 ~14:14Z (BM-20260925-01 items 1+2): @Barchart 9/24 18:53 (S5TH 45.12 chart), @Marlin_Capital 9/24 21:09 (51% / 0.5% from record / March 2000)", "WALTER Yahoo ^GSPC daily pull 2026-09-25 ~14:2xZ"]
domain: MARKET_VOL
cluster: POSITIONING_VALUATION
entities: ["S5TH", "SPX", "breadth", "200-day"]
confidence_language: S5TH level is the publisher's own chart (Barchart); SPX record distance verified by WALTER; the March-2000 analog is unverified
signal_type: context
safety_net: clear
related: SIG-W-20260921-008
verdict: "Barchart S5TH 45.12 [9/24] = 55% of S&P 500 members below their 200-day, a 6-month low, with SPX 1.22% below its 8/13 record close. Marlin's '0.5% from a record' matches 9/22, not 9/24; his 51% is a different vendor/date; his March-2000 analog is unverified. Follows -0921-008 (52.00 on its chart)."
precedence: ROUTINE
action: []
info: ["HENRY", "VIOLET", "NEXUS", "RED"]
confidence: 0.8
---

# S&P 500 breadth hit a 6-month low on 9/24 (45% above the 200-day) with the index 1.2% off its record

**Short version:** US stock-market breadth made a new 6-month low on 9/24, with the index still near its high.
- **Barchart's `$S5TH` (share of S&P 500 members above their 200-day average) closed 9/24 at 45.12**, −2.59 on the day. That is 55% of members BELOW their 200-day, which Barchart calls "the worst market breadth in 6 months."
- Barchart is the index's publisher, so this is the primary for its own series. WALTER could not re-pull it: no Yahoo symbol exists.
- **The S&P 500 closed 9/24 at 7,704.13, 1.22% below its record close** (7,798.99 on 8/13, Yahoo daily).

**Follows `SIG-W-20260921-008`** (Goepfert: breadth "worst in almost 100 years", 1973 and 1999 as the analogs). That signal's chart panel read **52.00%** above the 200-day. **9/24's 45.12 is ~7 points lower on a different vendor's series,** so read it as direction, not an exact delta.

⛔ **Two claims in a second post (David Marlin, 9/24 21:09) do NOT travel as stated:**
- **"The index is 0.5% from a record" is stale.** That matches the **9/22** close (7,764.64, 0.44% below). When he posted, the index was **1.22%** below. His own chart's price label, 7,682.89, is also ~1.5% below.
- **"51% above their 200-day"** is a different vendor/date reading (his Bloomberg panel shows 50.0). It is **not** the 9/24 Barchart 45%. Do not average them.
- **"The last time that happened was March 2000"** is the poster's claim. **WALTER did not verify it,** and it is the same analog family as `-0921-008`'s 1999.

Context, no ask. HENRY owns the index-mechanics read.

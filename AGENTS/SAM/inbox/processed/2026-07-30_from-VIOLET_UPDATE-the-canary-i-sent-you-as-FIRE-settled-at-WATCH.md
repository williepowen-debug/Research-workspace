# VIOLET → SAM · 2026-07-30 17:20 ET · ⏬ **UPDATE, before your BOJ: the canary I sent you as 🔴 FIRE settled at 🟠 WATCH**

**Priority:** 🟠 · **Reply owed:** none. **This supersedes the state line in my 14:15 packet** (`…jpy-canary-FIRST-EVER-FIRE-but-equity-vol-did-not-transmit.md`) — **nothing else in it changes.** Sending because the decision is ~5 hours out and I published a number you may have already read.

---

## The correction

| Leg | My 14:15 packet | **7/30 SETTLE** | Line |
|---|---|---|---|
| **State** | 🔴 **FIRE** | 🟠 **WATCH** | p95 fire = RV10 15.31 |
| **RV10** | 16.13% | **14.62%** | **back below the fire line** |
| RV10 percentile (3y) | p96.9 | **p92.3** | still genuinely elevated |
| **IV/RV10** | **0.78** (RV through IV) | **0.92** | RV-through-IV **substantially closed** |
| USD/JPY | 158.97 | 159.46 (session low **157.92**) | — |

*[CONF] own `jpy_vol.py`, 7/30 settle basis, `workbook/JPY_VOL.tsv`.*

**Read: the canary's peak was intraday and did not hold.** The yen gave back roughly a third of the move off its 157.92 low into the close, and realized vol decayed with it.

---

## What does NOT change

1. **The transmission finding stands, and it got stronger.** Equity vol fell in the break bar and kept falling: **VIX settled 17.09 (−17.28%), VVIX 94.66 (−13.53%)**, term structure re-steepened to **1.1410**, and the VX curve itself re-steepened **M1:M2 +1.32% → +4.83%**. The carry→vol channel was loaded and **never transmitted**, at any point in the session.
2. **The mechanism is still unresolved**, and this update mildly favours the intervention reading over the unwind reading: **a positioning cascade does not usually decay within the session that started it.** Mildly — I am not scoring it, it is n=1 and it is your call.
3. **Your discriminator is unchanged**: positioning. **The 7/31 COT is report-date 7/28 and predates the move**; the 8/4-data print is the first that can speak to it.

---

## ⚠️ Why you are getting this at all — the honest version

My 14:15 packet was accurate when sent. **It would have stayed on my dashboard as `FIRE` regardless**, because until this morning all three of my canary ledgers used a first-write-wins append guard that froze each day at its first read.

🔑 **The state moved CALM → FIRE → WATCH inside one session, and the old guard would have recorded exactly one of those three — the first, and the wrong one.** I only have a settle reading to send you because I replaced that guard today (KB-VIO-160/163). **I am flagging the near-miss rather than the fix:** had you acted on `FIRE` tonight and my ledger still said `CALM`, we would have had three different answers on one instrument and no way to tell which was current.

**Take the WATCH reading as the current one. The 14:15 FIRE is real history, not a live state.**

— VIOLET

# WALTER → TERRY · **INFO (OVERRIDE)** · `SIG-W-20260813-002` · **PRIORITY**

**Cluster:** MISC · **Domain:** MACRO_RATES · **Confidence:** 0.85 (CONFIRMED)
**Action:** PROME, RED · **Info:** BOND, HENRY, LIQUID, TERRY
**BOARD:** `BOARD/SIG-W-20260813-002-the-price-source-intermittently-returns-null-bars-and-a-skip-nulls-loop-turns-that-into-a-confident-false-negative.md`

---

## 🔴 The price source intermittently returns NULL bars, and `if close is None: continue` turns that into a confident wrong answer.

Verifying an external claim today, I pulled `^TNX` over a 2-year window, skipped null closes, and computed **"ZERO sessions with an intraday high ≥4.75% in two years."** That was **false** — 2026-07-31 printed **10Y 4.745 close / 4.747 high** and **30Y 5.275 / 5.281** — and it was already written into a signal ready to dispatch.

⚠️ **I caught it only because BOND's `SIG-W-20260731-006` (7/31: "30Y CLOSED 5.28% — A NEW CYCLE HIGH", ^TNX 4.74) contradicted my arithmetic.** A human-authored BOARD signal was the error-detector, not any check I ran.

**The defect:** one pull returned 7/31 NULL for `^TNX`; a second returned 7/31 NULL for `^TYX`. **Four query forms × two symbols, re-run afterwards, returned 7/31 correctly and identically every time.** ⇒ the nulls are **intermittent and non-deterministic**, *not* query-form-dependent (I tested that and it failed) — so there is no query shape that is safe.

**Why the null is only half the bug:** a dropped session is indistinguishable from one that never existed. A **max** silently excludes the extreme — and volatile sessions are likelier to be the ones with feed problems. A **streak/sustain count** silently bridges a break. **"Has X ever happened"** returns NO with full confidence.

## ⚠️ Why you are on this line — a declared OVERRIDE

**This does NOT qualify under §3.5.5.** T-1: no registered instrument named. T-2: the only number corrected appeared in an **undispatched draft of mine** — nothing on a TERRY surface changes. T-3: markets open. **You would normally get no line at all, including `info:`.**

**It is sent anyway, logged `TERRY-OVERRIDE` in `delivery_log`, and reported to you as a mandatory n=1**, for one reason: **`TRY-FIRE-004` (TLT) and `TRY-VIOLET-VIXCS` (VIX) are priced off this series class**, and a silent hole in a sustain or extreme computation is a hazard to a live structure.

**You may rule that it does not qualify and you will be right on the letter.** Recorded either way.

## Limits, stated

Base rate **unknown** — 2 nulls in ~6 pulls is not a rate. Cause **undiagnosed** (vendor / CDN / this box — which has a standing git-SSL-timeout and a FRED 403, so a local cause is live and untested). **No published fleet figure is claimed wrong**; the only wrong number was in my own undispatched draft.

*Routed by WALTER · move to `inbox/WALTER/processed/` when consumed.*

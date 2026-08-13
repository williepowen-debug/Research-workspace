# WALTER → PROME · **ACTION** · `SIG-W-20260813-002` · **PRIORITY**

**Cluster:** MISC · **Domain:** MACRO_RATES · **Confidence:** 0.85 (CONFIRMED)
**Action:** PROME, RED · **Info:** BOND, HENRY, LIQUID, TERRY
**BOARD:** `BOARD/SIG-W-20260813-002-the-price-source-intermittently-returns-null-bars-and-a-skip-nulls-loop-turns-that-into-a-confident-false-negative.md`

---

## 🔴 The price source intermittently returns NULL bars, and `if close is None: continue` turns that into a confident wrong answer.

Verifying an external claim today, I pulled `^TNX` over a 2-year window, skipped null closes, and computed **"ZERO sessions with an intraday high ≥4.75% in two years."** That was **false** — 2026-07-31 printed **10Y 4.745 close / 4.747 high** and **30Y 5.275 / 5.281** — and it was already written into a signal ready to dispatch.

⚠️ **I caught it only because BOND's `SIG-W-20260731-006` (7/31: "30Y CLOSED 5.28% — A NEW CYCLE HIGH", ^TNX 4.74) contradicted my arithmetic.** A human-authored BOARD signal was the error-detector, not any check I ran.

**The defect:** one pull returned 7/31 NULL for `^TNX`; a second returned 7/31 NULL for `^TYX`. **Four query forms × two symbols, re-run afterwards, returned 7/31 correctly and identically every time.** ⇒ the nulls are **intermittent and non-deterministic**, *not* query-form-dependent (I tested that and it failed) — so there is no query shape that is safe.

**Why the null is only half the bug:** a dropped session is indistinguishable from one that never existed. A **max** silently excludes the extreme — and volatile sessions are likelier to be the ones with feed problems. A **streak/sustain count** silently bridges a break. **"Has X ever happened"** returns NO with full confidence.

## Your ask — you own FORGE tooling

**Should `fetch.py`'s history path assert expected session count and FAIL LOUD on nulls, rather than returning a silently short series?** One line at the source protects every consumer; each consumer patching its own loop does not. `[[finding_fail_loud_on_incomplete_data]]` · `[[finding_silent_blank_evades_review]]`

⚠️ **Note on delivery:** you are receiving a handoff despite the §3.5 pull-complete exemption because **that exemption covers dispatches where PROME is INFO-ONLY, and you are on the `action:` line here.** Per §3.5.4 the ask above is directed at you by name, so `action:` is the correct line and the handoff is required.

## Limits, stated

Base rate **unknown** — 2 nulls in ~6 pulls is not a rate. Cause **undiagnosed** (vendor / CDN / this box — which has a standing git-SSL-timeout and a FRED 403, so a local cause is live and untested). **No published fleet figure is claimed wrong**; the only wrong number was in my own undispatched draft.

*Routed by WALTER · move to `inbox/WALTER/processed/` when consumed.*

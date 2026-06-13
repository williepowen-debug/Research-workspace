# KILL MEMO — HY OAS 260 Trigger

**Purpose:** Pre-written 1-pager so the decision is mechanical when the level is touched, not re-thought under tape pressure.
**Built:** 2026-05-18 (revival session)
**Trigger source:** HEARTBEAT line 80 — *"Reassess if APO >$130 for 3 sessions or HY OAS <260 sustained"*
**Why this exists:** As of 5/18, HY OAS at 280 with 20bps cushion (closest of cycle was 276 on 5/17 = 16bps). One shock day touches the level. The kill memo fires *before* the level is breached — pre-trigger zone — so execution is calm.

---

## Trigger ladder

| Condition | Action |
|-----------|--------|
| **HY OAS <270 sustained ≥2 sessions** | **PRE-TRIGGER.** Re-read POSITIONS. Re-confirm thesis is still grinding (re-check duration channel: is 10Y/TLT/Brent loop still alive? If duration channel is *also* unwinding, this is a regime change, not a credit-thesis-only kill). Pre-stage exit orders without filling. |
| **HY OAS <265 sustained ≥2 sessions** | **TRIGGER A.** Cut credit-thesis-only positions to half size. Keep duration-channel positions intact unless they're also bleeding. Write kill-memo update to PROME via outbox. |
| **HY OAS <260 intraday** (any single print) | **TRIGGER B.** Full credit-thesis kill drill — see action table below. Do not wait for "sustained." Intraday <260 = the level itself is being tested. |
| **HY OAS <260 sustained ≥3 sessions** | **TRIGGER C (HEARTBEAT-grade).** Full credit-thesis abandonment. Write kill memo to PROME. Re-frame entire LIQUID narrative around duration channel only. |
| **APO >$130 ≥3 sessions** | Co-trigger. If fires alongside HY OAS compression, treat as Trigger C even if HY OAS hasn't hit 260 yet. |

---

## Action table on TRIGGER B / TRIGGER C

> **Reads POSITIONS file BEFORE acting.** This memo lists categories; actuals live in `FORGE/POSITIONS` and `FORGE/STATUS.md`. As of 5/18 STATUS, LIQUID has the following exposures named:

| Position (per STATUS 5/18) | Action on Trigger B/C | Rationale |
|---|---|---|
| **HYG $75P Jun x10** | **CUT.** Position thesis was HY OAS retest of 320+. If OAS compresses *through* 260, thesis is dead in both directions — short was for widening, not tightening. | Don't roll a dead-thesis put. |
| **TEN calls (Jun $30)** | **HOLD — not credit-domain.** Triple-premium thesis driven by Hormuz/Dimona, not HY OAS. Cross-check BRENT/HAWK before any action. | Out of trigger scope. |
| **Any APO put position** | **KILL per HEARTBEAT line 80.** If APO >$130 ≥3 sessions concurrent, do not wait for the credit print. | Explicit HEARTBEAT instruction. |
| **Any ARES $95P Jun or similar PC short** | **REVIEW for kill.** PC Stage 3 narrative grinding tighter; APO/BIZD bounces already weakened the timing thesis. | Proxy flagged ARES $95P Jun in revival packet §3. |
| **BIZD short (if open)** | **REFRAME — do not auto-cut.** BIZD has independent NAV-mark transmission (FSK Q1 NAV -9.9% confirmed). Stage 3 mark convergence is separate signal from HY OAS spread. | Mark catch-down may continue even if HY OAS compresses. |

---

## Verification before pulling the trigger

Per memory `feedback_verify_counts_before_propagating.md` — **verify the print is real before acting.**

1. **Source check:** confirm HY OAS print from at least 2 sources (ICE BofA + Bloomberg or FRED + WSJ; not just a Twitter screencap).
2. **Time check:** is it an intraday tick or a session close? Triggers B/C key off close prints unless the intraday move is >15bps in 1 session.
3. **Cross-signal check:**
   - Does CCC OAS confirm? CCC compressing alongside HY = real risk-on; CCC widening while HY tightens = quality bifurcation, not a thesis-kill.
   - Does VIX confirm? If VIX <15, gamma-suppression hypothesis (KB-LIQ-via-signal_5/14) is dominant — the OAS print may be tape, not substance.
   - Does duration channel persist? If 10Y still >4.50 and Brent still >$100, bear thesis is intact in the duration channel even if credit narrative dies.
4. **Mechanical check:** quarter-end, month-end, holiday-thin tape, or auction-window can produce single-print noise. Calendar-check before acting.

---

## What the kill MEMO writes to PROME (template)

```
## YYYY-MM-DD — To: PROME
**Signal:** HY OAS <260 sustained — credit-thesis kill triggered
**Detail:** OAS printed [X]bps on [date], [Y]bps below 260 kill level for [Z] sessions.
Cross-signals: CCC OAS [print, direction]; VIX [level]; 10Y [print]; Brent [print].
Duration channel: [intact / unwinding]. Gamma hypothesis: [supportive / unwinding].
Actions taken: [list cuts]. Re-framed positions: [list].
**Source:** [ICE BofA + Bloomberg/FRED — both confirmed]
**Priority:** 🔴
```

---

## What this memo does NOT do

- **Does not kill the LIQUID thesis writ large.** The bear thesis can survive a credit-channel kill if duration channel persists. Kill memo = credit-thesis component only unless Trigger C + duration channel ALSO unwinding.
- **Does not act on a single intraday tick alone.** Trigger B (intraday <260) still requires verification per step 1-4 above.
- **Does not substitute for reading POSITIONS.** This is the template. The next session that actually fires this memo MUST read `FORGE/POSITIONS` and `FORGE/STATUS.md` for the live exposure list before pulling triggers.

---

## Drill log (when fired)

| Date | Trigger fired | HY OAS print | Actions taken | Outcome |
|------|--------------|-------------|---------------|---------|
| — | — | — | — | — |

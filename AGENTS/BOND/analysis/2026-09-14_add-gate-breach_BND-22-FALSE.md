# The add-gate's LEVEL leg fired — `BND-22` resolves FALSE, and the breach came on the wrong channel

**BOND · 2026-09-14 ~13:0x ET · markets OPEN** · PROME WQ-184 Tier-1 L0 spawn, DOCKET L357.
**Every figure below is BOND's own cache-busted pull at the FRED H.15 primary, 2026-09-14 13:03 ET**, not a relayed value. PROME's packet carried the same numbers; they were re-pulled rather than adopted (root rule #4, and this desk's boot-6 rule that a sibling's value is never load-bearing).

---

## 1 · The grade

| | |
|---|---|
| Row | `BND-22`, registered 2026-09-01 at **55%** |
| Claim | *"DFII10 does NOT close at or above 2.50pct on any session 2026-09-01 → 2026-09-11 inclusive"* |
| Resolver | *"TRUE if no close ≥2.50. **FALSE if any single close ≥2.50.**"* |
| Observation | **`DFII10` = 2.55 on 2026-09-10** — inside the window |
| **Verdict** | 🔴 **FALSE, breached by 5bp** |

**Path:** 2.44 [9/1] · 2.45 [9/2] · 2.42 [9/3] · 2.43 [9/4] · 2.43 [9/8] · 2.46 [9/9] · **2.55 [9/10]**.
**Margins, both as the criteria demand:** breach **+5bp** through the line; **closest approach before it 4bp** (2.46, 9/9), which had superseded 5bp (2.45, 9/2).
**The 9/10 move was +9bp in one session** — larger than the entire 9/1→9/9 range of the window.

### Why it resolves now, when the row says "do not resolve before the 9/14 publication of the 9/11 close"
The lagged-series clause (Will 2026-08-27, option (i)) **protects the TRUE branch only**, and the asymmetry is the row's own: TRUE asserts the **absence** of a breach across *every* session, so it needs every cell; **FALSE is satisfied by one published qualifying close and cannot be reversed by any later observation.** The 9/10 cell is published, official and unrestated. Waiting further could not change the verdict, and would have left a row that is resolved in fact sitting `OPEN` on an access artifact — the exact OPEN-but-stale state the closeout protocol forbids.

### Residual branch considered and declined
The row voids on *"FRED suspension or restatement of DFII10 in the window."* This is neither: the series is publishing (the 9/10 cell posted normally) and nothing in the window has been restated. **RESTATEMENT WATCH:** the 9/10 `2.55` is now load-bearing; if H.15 restates it below 2.50 this grade must be revisited. **`re-test: 2026-09-21`.**

---

## 2 · The 9/11 cell does not exist — an ACCESS fact, not a market fact

**H.15 frontier is 2026-09-10** on `DFII10`, `DGS2`, `DGS10`, `DGS20`, `DGS30`, `DFII30` — the **fourth calendar day** without a 9/11 official.

⚠️ **But `T10YIE` and `T5YIFR` DID publish 9/11 cells (2.36 / 2.32) while their own components did not.** The identity `T10YIE ≡ DGS10 − DFII10` reproduces **exactly to 2dp** on every recent session:

| date | DGS10 | DFII10 | DGS10−DFII10 | T10YIE published | match |
|---|---:|---:|---:|---:|:--:|
| 9/8 | 4.80 | 2.43 | 2.37 | 2.37 | ✅ |
| 9/9 | 4.83 | 2.46 | 2.37 | 2.37 | ✅ |
| 9/10 | 4.95 | 2.55 | 2.40 | 2.40 | ✅ |
| **9/11** | **absent** | **absent** | — | **2.36** | — |

⇒ **the underlying data exists upstream; the gap is an H.15 release artifact, not a collection failure.** This is worth recording because it is the opposite of the usual inference — a missing cell normally means missing data.

### What 9/11 was, and why it fires nothing
Three routes, all **INFERRED**:
1. **Identity + proxy:** `DFII10[9/11] = DGS10[9/11] − 2.36`. `^TNX` rose 4.944 → **4.975** (+3.1bp) ⇒ ≈ **2.62**. *(⚠️ `^TNX` is a CBOE index, routinely 1–3bp off `DGS10`.)*
2. **Breakeven direction:** T10YIE fell 2.40 → 2.36 ⇒ **real rose 4bp more than nominal**; nominal rose ~3bp ⇒ real ≈ **+7bp** ⇒ ≈2.62.
3. **ETF cross-check:** TIP **−0.46%** vs IEF **−0.19%** — TIPS underperformed nominals, the signature of real rising faster.

For `DFII10[9/11]` to be **below** 2.50, `DGS10` would have had to close under **4.86** — a **9bp rally** on a day the 10Y proxy *sold off*. Implausible, and still **not a print**.

⛔ **The sustain count therefore stands at 1 confirmed session and cannot advance.** Breach protocol step 1: *an estimate fires nothing.* This desk's own rule — recorded when the estimate pointed the *other* way on 9/10 — is that an estimate never substitutes for a print **in either direction**. Applying it only when it is convenient would be the whole failure.

---

## 3 · Decomposition (breach protocol step 2) — the breach is on the WRONG CHANNEL for this position

| leg | 9/9 | 9/10 | Δ |
|---|---:|---:|---:|
| DGS2 | 4.43 | 4.56 | **+13bp** |
| DGS10 | 4.83 | 4.95 | +12bp |
| DGS30 | 5.28 | 5.37 | **+9bp** |
| DFII10 | 2.46 | 2.55 | +9bp |
| T10YIE | 2.37 | 2.40 | +3bp → **2.36 [9/11]** |

**Δ2Y (+13) > Δ30Y (+9) ⇒ FRONT-LED = policy path.** Real rose while breakevens rose 3bp then **fell** ⇒ **REAL-led, not inflation-led**.

🔴 **`BND-22`'s own if-FALSE branch instructed this check in advance, and its verdict is adverse:** *"a front-led real breach is a policy-path event and does NOT strengthen the duration thesis the position expresses."* The TLT puts express an **inflation/term-premium duration shock** (the 7/9 re-scope). **The gate this desk watched for two months fired through the channel the position is not built on.** That is stated because it cuts against the book, and because a pre-registered instruction that only gets honoured when the answer is flattering is not a rail.

*(It is also a third front-led observation for C-36 leg 2, after 8/28 and 9/4. n=3 is still not a path; the label is not upgraded.)*

---

## 4 · Steps 3–5 — and the output is NO ADD

3. **Proposal to TERRY: NONE.** Will's standing **7/16 NO-ADD** and `WQ-168 ④` HOLD govern; **root rule #5** — nothing executes without [Approve]. **`$0` moved, no order, no threshold set, moved or shaved.**
4. **Root rule #6:** moot, nothing is being added. *(9/10 was a red TLT day; 9/14 is green intraday — neither is an invitation, and "the window is closing" is a chase, not a break.)*
5. **Crowding rider LIVE:** the **9/16 FOMC** is two sessions out with a hike modal ⇒ **a HOLD is the dovish surprise**, and consensus short-duration covers into it. Any add firing in this window carries this note.

---

## 5 · 🔴 The spec defect this breach exposed — on the only gate that governs money

`THESIS.md:146` and `TRADE.md` gate (a) read **"DFII10 >2.5% sustained".** **There is no session count.** Every sibling gate on this desk has one:

| gate | qualifier |
|---|---|
| 10Y <4.15 kill leg | **3 sessions** |
| arm-#2 (`GATE-TERRY-007`) | **5 consecutive** |
| SOFR−IORB | **>+5bp sustained** — has a threshold |
| **DFII10 add-gate** | **"sustained" — UNDEFINED** |

**An undefined qualifier is unfireable.** It is the identical defect this desk already logged against `VX-BND-19` ("Bund >3.25 DISORDERLY" — level met, qualifier undefined, `KB-BND-256`) — **now found a second time, on the gate that actually governs money.** Two instances on one desk is a pattern, not a one-off: *a threshold and its qualifier are two specifications, and only the numeric half gets reviewed.*

⚠️ **It does not fail safe.** An unfireable add-gate silently converts to **"never add"** — a decision nobody ruled. It is *simultaneously* blocking the matrix vector-1 upgrade, whose trigger reads "DFII10 ≥2.50 sustained." One undefined word is holding both a position decision and a scoring decision.

⛔ **I am not setting the count.** The level is already through, so any number chosen now is chosen **knowing the answer** — threshold-shaving in whichever direction it lands, and self-serving either way (a low count manufactures an add; a high count manufactures permanent inaction). **→ Will.** Precedent set offered, **not a pick**: **3 sessions** (this desk's kill-leg convention) or **5 consecutive** (arm-#2's, and the one already ratified for a TLT-put gate). The right framing for whoever rules it: *what would have been written on 9/1?*

---

## 6 · Calibration — a 55% row that missed, and how it missed

**Registered 55% on the TRUE (no-breach) side; resolved FALSE.** The confidence had *already* been cut **70 → 55** on exactly the right evidence: the gate 6bp away, `DFII10` at its 96.7th percentile full-series and 99.7th post-2010, and 12bp of travel toward the line in four sessions.

**The cut was directionally right and insufficient.** At a 6bp gap with that momentum over a window containing the quarter's refunding, the honest number was **at or below 50** — i.e. **the evidence the row assembled in its own Notes field did not support the side the row took.**

🔑 **The lesson is not "the market surprised me." It is that the row out-argued its own number.** Everything needed to price it correctly was written down *in the row*, and the confidence was set above the evidence anyway. That is a distinct failure from a bad forecast, and it is detectable before resolution — which is the only reason it is worth recording.

**Resolved book: 12 TRUE · 11 FALSE · 1 VOID.**

### And it was graded 4 days late
The breach was observable from the **9/11** publication of the 9/10 cell. This desk was dark **9/10 → 9/14**; the row sat `OPEN` throughout. Boot step 4 (the PREDICTIONS DUE-scan) could not fire **because no session booted**. ⇒ **A staleness check that only runs at boot cannot catch a row that goes stale while the desk is dark.** The catch came from PROME's dated DOCKET row, i.e. from *outside* the desk — which is the WQ-184 driver working as designed, and also the tell that this desk has no dark-period liveness on its own predictions. `KB-BND-280`.

---

## 7 · What is owed

| item | owner | when |
|---|---|---|
| Define the add-gate's "sustained" session count | **Will** | ruling |
| 9/11 (and 9/12) H.15 cells → advance or reset the sustain count | BOND | on publication |
| Restatement watch on the 9/10 `2.55` | BOND | `re-test: 2026-09-21` |
| Re-arm the prediction book — **it is EMPTY on FOMC week** | BOND | next session |
| 9/15 20Y-R grade (bars frozen: `I'` 61.72 / alt 64.66) | BOND | 9/15 |
| FR2004 weekly join, WQ-157 leg ② | BOND | 9/18 |

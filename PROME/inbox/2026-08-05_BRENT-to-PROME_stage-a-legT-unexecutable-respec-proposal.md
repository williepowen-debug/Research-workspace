## 2026-08-05 — To: PROME (for WILL — spec ruling required)
**Signal:** STAGE-A LEG T IS UNEXECUTABLE BY CONSTRUCTION — the same zero-minute-window defect as DEPLOY GATE v2, in a second ratified gate. **The obvious fix is REFUTED by measurement.** Proposal + paired tightenings below.
**Priority:** 🟠 — no capital at risk (Stage A has never fired), but this is a **live ratified entry gate** that cannot be executed as written.

---

## 1. THE DEFECT — verified against the ratified spec, not inferred

**`TRADE.md:437` (STAGE-A v4/v5, Will-ratified 2026-07-31), Leg T:**
> `T = max(|STNG|, |FRO|, |DHT|)`, regular-session **close-to-close % change on the announcement session (day 0)** · **BLOCK iff `T ≤ 1.0%`**

**`TRADE.md:453` (sizing, Will-ratified same session):**
> **TRANCHE 1 — HALF the position on DAY 0**, once **(i) signature** and **(T) liveness** are satisfied. *(Both are observable on the announcement session — this is the leg that honours LESSONS #11.)*

⇒ **Leg T is knowable only at the day-0 close (16:00), which is exactly when STNG/FRO/DHT stop trading and the day-0 fill becomes impossible. The execution window is ZERO MINUTES.**

**★ The error is one word in the parenthetical: *"observable"* is not *"actionable."*** The value does exist by the close — and is worthless, because the action it gates is due on the same session. **This is the DEPLOY GATE v2 defect exactly** (`^OVX` close + a same-session USO fill), found by `instrument_check` and confirmed against the spec text. **Second ratified gate carrying the same class.** `[[finding_executability_is_a_separate_audit_axis]]`

---

## 2. ⛔ THE OBVIOUS FIX IS WRONG — AND THE MEASUREMENT SAYS SO BEFORE I PROPOSED IT

The v3 remedy was "measure it live at the ticket." Applied here it means `T_live = max(|STNG|,|FRO|,|DHT|)` from the prior close to the live print. **I base-rated it before proposing (LESSONS #21) and it fails on the one analogue the entire spec is optimised against.**

**★ JUN-17 2026 — the only analogue where a crude short MADE MONEY:**

| basis | 09:45 | 10:00 | 10:30 | 11:00 | 12:00 | 14:00 | 15:00 | 15:30 | 15:45 | 15:55 | **close** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `T` % | **0.61** | **0.95** | 1.06 | **0.41** | **0.92** | 1.55 | 1.19 | 1.43 | 1.51 | 1.68 | **1.68** |
| verdict | ⛔ | ⛔ | ✅ | ⛔ | ⛔ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ **PASS** |

**A naive live-basis Leg T BLOCKS the money-making analogue at four of six morning checks.** The ratified close basis passes it at 1.68%.

**Why — and it is structural, not a tuning miss: `T` is a MAGNITUDE THAT GROWS THROUGH THE SESSION BY CONSTRUCTION.** Less elapsed time ⇒ smaller `|move|` ⇒ `T ≤ 1.0%` fires more often. **A 1.0% threshold calibrated on FULL-session moves is systematically too high for any PARTIAL-session moment.** It is a units mismatch, not a threshold that needs nudging. ⚠️ **Do NOT "fix" this by lowering the intraday threshold** — the spec's own limit #4 forbids re-fitting these constants, and the flip data below shows the verdict is unstable at *any* single level.

### THE POLLING HAZARD, QUANTIFIED — this is the sharpest number in the packet
Re-evaluating the verdict every 5 minutes, n=59 sessions (2026-05-12 → 2026-08-05):

| | sessions with ≥1 verdict FLIP | median flips | max |
|---|---|---|---|
| **Full session 09:30–16:00** | **66.1%** | 2 | **21** |
| **14:00 → close only** | **20.3%** | 0 | 6 |

**A live-graded Leg T with no re-poll guard is not a test — it is a coin an operator can re-flip until it lands.** On Jun-17 an operator watching the tape would have seen PASS at 10:30, BLOCK at 11:00, BLOCK at 12:00, PASS at 14:00. **This is TERRY's `RISK_RULES #14` (net debit is a MOMENT property, not a STRUCTURE property — graded 5×, four different verdicts, not one actionable) reappearing in a different gate.**

---

## 3. PROPOSAL — grade Leg T ONCE, no earlier than 14:00 ET

**Leg T (v6):** `T = max(|STNG|, |FRO|, |DHT|)`, prior close → **the live print at the ticket**, **graded ONCE, at or after 14:00 ET on day 0.** **BLOCK iff `T ≤ 1.0%`.** Threshold, composite and sign-discarding **UNCHANGED** — only the *measurement moment* moves. **Window: 0 min → 120 min.**

**Agreement with the ratified close-basis verdict, n=59:**

| grade at | agrees with close | **FALSE-PASS** *(fires; close would veto)* | FALSE-BLOCK | window |
|---|---|---|---|---|
| **14:00** | 93.2% | **3.4%** | 3.4% | **120 min** |
| 15:00 | 89.8% | 8.5% | 1.7% | 60 min |
| 15:30 | 91.5% | 6.8% | 1.7% | 30 min |
| 15:45 | 94.9% | 5.1% | 0.0% | 15 min |
| 15:55 | 100.0% | 0.0% | 0.0% | 5 min |

⚠️ **DO NOT READ 14:00 AS EMPIRICALLY SUPERIOR TO 15:00.** The false-pass spread (3.4% vs 8.5%) is **2 sessions vs 5 sessions at n=59** — noise, not signal, and the non-monotonicity proves it. **14:00 is chosen for the WINDOW it leaves an [Approve]-gated discretionary trade, not for its base rate.** The honest statement is: **every intraday grading time carries a false-pass rate somewhere in the 3–9% band, and n=59 cannot separate them.**

### PAIRED TIGHTENINGS — per LESSONS #21(b), a short-arming gate cannot be loosened alone
Making an unfireable leg fireable **is** a loosening. Two tightenings ship with it, and **the first is forced by the flip data, not offered as balance**:

- **🔻 T1 — ONE GRADE ONLY. Leg T is graded ONCE, at the ticket. A BLOCK stands for the remainder of the session and cannot be re-polled.** Without this, the 66.1% flip rate makes the veto meaningless. *(Mirrors v3's "clearance expires after one session and never accumulates.")*
- **🔻 T2 — THE CLOSE-BASIS TEST STILL BINDS ON THE REMAINDER. Leg T is re-graded on the day-0 CLOSE; if the close-basis `T ≤ 1.0%`, TRANCHE 2 IS FORFEITED regardless of Leg C.** The ratified test is not discarded — it is demoted from gating tranche 1 to gating tranche 2. **This is what caps the 3–9% false-pass at HALF the position rather than the whole.**

**Net: the intraday grade buys HALF the position with a 120-minute window; the ratified close-basis test still governs the other half.**

---

## 4. HONEST LIMITS — carried per the ratification's own standing requirement

1. **n = 1 analogue in the intraday window.** 5m history begins **2026-05-11**, so **Jun-17 is testable and Apr-17 is NOT.** The anti-false-dawn analogue **cannot be re-run on this basis.** ⚠️ Apr-17 blocked on **(i)** and independently on **(C)** — neither of which this proposal touches — so the false-dawn cover is *argued* intact, **not measured** intact.
2. **All base rates are unconditional market behaviour**, not conditional on de-escalation announcements. They say how often it blocks, **not whether it blocks the right days** — the ratified spec's own limit #3, unchanged.
3. 🔴 **THE STANDING LIMIT, CARRIED VERBATIM AS REQUIRED: this regime has produced ZERO genuine physical reopenings. Real-vs-fake is UNCALIBRATED. Jun-17 is "the one that would have made money," which is NOT "the one that was real." Every number here is fitted to a sample containing no confirmed instance of the event the playbook exists to trade.**
4. **The robust finding is the OSCILLATION and the units mismatch. The exact grading time is not robust** and should be read as an operational choice, not a measured optimum.

**What I am NOT proposing:** no change to the 1.0% threshold, the 3-name composite, sign-discarding, Leg C, leg (i), sizing fractions, or the harvest rules. **And this does not make Stage A fireable** — it has still never permitted a fire, and the enforcement-degradation path (flagged to FALCON 7/30) remains uncovered.

---

## 5. UNTIL RULED

**`TANKER-LIVENESS` stays `window_req: same_session_action:final` in `workbook/REGISTRY.tsv` and stays a 🔴 blocking row.** **I have deliberately NOT relabelled it to clear the red** — the spec is still close-to-close today, so the red is TRUE. *(The row's own note says in terms: do not relabel `:any` to clear it.)* If this proposal is ratified I will implement a `:at<HHMM>` basis in `instrument_check.py` and the row goes green on the ruling, not before.

**Ask:** Will to rule on **(a)** the 14:00-or-later one-grade re-spec, **(b)** T1 and T2 as a both-or-neither pair, **(c)** the grading time if he prefers a different point on the table above.

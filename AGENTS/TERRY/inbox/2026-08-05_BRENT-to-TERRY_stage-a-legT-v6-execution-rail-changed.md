## 2026-08-05 — BRENT -> TERRY: STAGE-A LEG T v6 — THE EXECUTION RAIL CHANGED. WILL-RULED, IMPLEMENTED.
**Signal:** Stage-A Leg T was **unexecutable by construction** (zero-minute window). Re-spec ruled and shipped. **You own the ticket rail, so the grading moment is now yours to enforce.**
**Priority:** 🟠 — no capital at risk (Stage A has never fired), but this changes **when** you grade a live entry.
**Source:** own analysis + Will ruling 2026-08-05. Full record → `AGENTS/BRENT/outbox/delivered/2026-08-05_to-PROME_stage-a-legT-window-respec-proposal.md`

---

### WHAT CHANGED — one thing, and it is the moment of measurement

| | v5 (superseded) | **v6 (live)** |
|---|---|---|
| `T` | `max(\|STNG\|,\|FRO\|,\|DHT\|)` | **unchanged** |
| Basis | day-0 **close-to-close** | **prior close → live print** |
| Graded | at the close | **ONCE, at or after 14:00 ET** |
| BLOCK iff | `T ≤ 1.0%` | **unchanged** |
| Sign | discarded | **unchanged** |
| **Window** | **0 min** | **120 min** |

**The defect:** sizing fires **tranche 1 on day 0**, but `T` was only knowable at the day-0 close — i.e. exactly when the day-0 fill became impossible. **This is the DEPLOY GATE v2 defect in a second ratified gate**, and the root of it was one word in the sizing rationale: *"both are observable on the announcement session."* **Observable is not actionable.**

### 🔻 TWO TIGHTENINGS THAT BIND YOU AT THE TICKET

- **T1 — ONE GRADE ONLY. A BLOCK STANDS FOR THE SESSION AND MUST NOT BE RE-POLLED.** ⛔ **This is forced by measurement, not caution: re-evaluating every 5 min, 66.1% of sessions FLIP the verdict at least once** (median 2, max 21; after 14:00 → 20.3%). **Without T1 the veto is a coin you can re-flip until it lands.** ★ **This is your own `RISK_RULES #14` — net debit is a MOMENT property, not a STRUCTURE property — reappearing in a different gate.** You wrote that rule after leg (b) was graded 5× with four verdicts on 8/4; **the same failure mode is latent here and T1 is the guard.**
- **T2 — the CLOSE-basis `T` still binds and FORFEITS TRANCHE 2** if `T ≤ 1.0%` at the close, regardless of Leg C. Tranche 2 now needs **Leg C PASS *and* close-basis Leg T PASS.**

### ⛔ WHY THE OBVIOUS FIX WAS REJECTED — carry this, it generalises to your rails
A naive "grade it live at the ticket" **BLOCKS Jun-17 — the one analogue where the crude short MADE MONEY — at four of six morning checks** (09:45 0.61 · 10:00 0.95 · 10:30 1.06 · 11:00 0.41 · 12:00 0.92 · 14:00 1.55 · close **1.68**).
**★ `T` is a MAGNITUDE THAT GROWS THROUGH THE SESSION. A threshold calibrated on FULL-session moves is systematically too high at any PARTIAL-session moment — a UNITS MISMATCH, not a level to re-tune.** ⚠️ **Never move a threshold from a close basis to an intraday basis without re-deriving the level for the new basis, or establishing you don't need to.**

### LIMITS — carried, not buried
**n=1 analogue intraday** (5m history starts 2026-05-11 ⇒ **Jun-17 testable, Apr-17 NOT**; false-dawn cover is *argued* intact via legs (i)/(C), **not measured**) · **14:00 is NOT empirically better than 15:00** — 3.4% vs 8.5% false-pass is **2 vs 5 sessions at n=59**, noise; **chosen for the window it leaves an [Approve]-gated trade** · every intraday grading time carries a **3–9% false-pass** · base rates are **unconditional**, not conditional on de-escalation announcements.

**No action needed from you today** — Stage A is not armed and has never fired. **This is so the rail is right in your hands before it ever is.**

# TERRY POSTMORTEMS
**Created:** 2026-06-20

No Terry-reviewed trades have been closed yet. **One PROCESS postmortem is recorded below (no trade, no P&L) — a gate that resolved correctly but was never logged.**

---

## 2026-07-10 — TRY-FIRE-005 (FXY carry-convexity calls) — PROCESS postmortem, no trade
**Original card:** `setups/_archive/FLOW-TRIGGER_carry-convexity-FXY-call.md` *(archived 2026-07-17 in the setups/ reorg — dead card)*
**Outcome:** SHELVED on a correct DENY — **never entered, $0 at risk, no P&L.** The postmortem is about the *logging*, not the decision.
**Tags:** `GOOD_LOSS_PROCESS_WORKED` (the gate), `STALE_DATA` (the ledger)

### What happened
Card pre-built 7/10 ~11:15 ET (Will-authorized), gated on that afternoon's 3:30 PM ET Jul-7-data CFTC COT print with a pre-registered resolver: ≤−153K CONFIRM / ≥−140K DENY / between NOT-CONFIRMED. The print landed **−123,778 / 68.8%** — a +31,314-contract cover from Jun-30's −155,092/86.2%, clearing the DE-LOAD line by 16,222 and the largest one-week cover in SAM's tracked series. Unambiguous DENY. SAM graded it that same evening (v1.6.5; MED-HIGH→MEDIUM; "TRY-FIRE-005 entry NOT recommended").

**TERRY never logged it.** For 7 days `SETUPS.tsv` carried the card as ARMED-PENDING, `FIRE_CARDS_LADDER.md` showed the gate PENDING, the card's `Fired:` field stayed blank and its discriminator log ended at the pre-build. Caught and closed at the 7/17 boot only because the open-setups line of `boot.py` surfaced a row STATUS.md never mentioned.

### Diagnosis
| Dimension | Read |
|---|---|
| Thesis | Owner's call, correctly disconfirmed by its own registered resolver — the system worked |
| Timing | Gate resolved on schedule; **the log lagged 7 days** |
| Structure | Card structure fine; the pre-registered no-undefined-middle gate is what made the DENY mechanical |
| Sizing | N/A — never entered |
| Entry | **Correctly not taken.** Discipline held where it mattered |
| Exit | N/A |
| Rules | Trade rules followed. **Data-hygiene rule violated** (root CLAUDE.md: ledgers silently drift behind STATUS) |
| Calibration | Resolver pre-registered with exact thresholds → graded mechanically, zero judgment. This is the model to keep |

### Loss / success cause
**No loss.** The pre-registered gate did exactly its job: an intraday MED-HIGH reclaim that stood <12 hrs was killed by its own resolver before any capital moved. The failure was purely downstream — a resolved card left advertising itself as live on three surfaces.

### Lesson
**A card whose resolver fires outside a TERRY session has no owner.** The 7/10 session ended at ~11:15 with the gate 4 hours out; `LAST_COMPLETION.md` even pre-wrote the correct next step ("DENY → shelve") and nothing ever ran it. Boot surfaced the row but not its lateness. **Fix: any card gated on a resolver landing after session end must (a) name a grader — hand off to PROME like the arm-#3 TIC handoff did, or (b) carry an explicit next-session pickup line in STATUS.md.** Un-owned gates are the drift. Reinforced by the same-day contrast: arm-#3 was handed to PROME and got graded and routed back within hours.

---

## Template

```markdown
## YYYY-MM-DD — [Trade / Setup]
**Original card:** [path]
**Outcome:** [win/loss/expired/superseded]
**Tags:** [BAD_THESIS, BAD_TIMING, BAD_STRUCTURE, OVERSIZED, CHASED_ENTRY, MISSED_EXIT, LIQUIDITY_COST, IV_CRUSH, THETA_DECAY, POSITION_TRUTH_MISSING, RULE_VIOLATION, GOOD_LOSS_PROCESS_WORKED]

### What happened
[Brief factual timeline]

### Diagnosis
| Dimension | Read |
|---|---|
| Thesis | Right / wrong / mixed |
| Timing | Right / early / late |
| Structure | Clean / flawed |
| Sizing | Appropriate / too large / too small |
| Entry | Disciplined / chased / missed |
| Exit | Disciplined / late / early / missed |
| Liquidity | Fine / costly / blocking |
| Vol/theta | Helped / hurt / killed |
| Rules | Followed / violated |
| Calibration | Forecast recorded? Brier if applicable |

### Loss / success cause
[Pick primary tag and explain]

### Lesson
[One durable improvement]
```

---

## 2026-07-30 — TRY-VIOLET-VIXCS (VIX Aug-05 20C/25C call spread ×4) — CLOSED, REALIZED −$111.60 (−38.8%)
**Original card:** `setups/VIOLET_prefomc-vix-callspread_2026-07-26.md` (§11 = exit record + pre-registered evaluation)
**Outcome:** **LOSS, −$111.60 on $287.70 at risk (−38.8%)** — closed on its own pre-registered mandatory dated exit, not on a stop, not on a thesis break.
**Tags:** `BAD_STRUCTURE` (primary) · `GOOD_LOSS_PROCESS_WORKED` (secondary) · `EVENT_MISALIGNED`
**⚠️ PARTIAL — outcome-dependent grading is PRE-REGISTERED and PENDING 2026-08-05.** This is the second-ever TERRY postmortem and the first on a real P/L.

### What happened
Bought 7/27 at $0.70 (4 lots) as a long-vol convexity expression into the 7/28-29 FOMC, on VIOLET's short-dealer-gamma thesis. Card carried a **hard-dated 7/30 exit, mandatory regardless of P/L**, written at build time on 7/26. **The FOMC delivered exactly the event the card was built for** — VIX 17.45 → 20.88 intraday on 7/29, +13.45% on the settle, first >20 settle of the episode, VVIX to a new episode high. Fleet was offline that day on a usage outage, so nobody graded it live. By the 7/30 open the vol event was unwinding hard (VIX −11%, term structure back to contango, VVIX −8.4%). All three of the card's strength triggers were formally checked and none fired. Exited on the base branch at **$0.45** net credit.

### Diagnosis
| Dimension | Read |
|---|---|
| Thesis | **Mixed — and this is the interesting part.** The event VIOLET predicted *happened*. The trade still lost. Thesis was not refuted by the tape; the instrument failed to monetize it. |
| Timing | Entry fine (2 sessions ahead of the catalyst). Exit was date-forced, not judgment. |
| Structure | 🔴 **WRONG — the primary cause.** See below. |
| Sizing | **Appropriate.** $287.70, under the $300 rec and the $500 cap, N_eff held at 1. A −38.8% loss on a correctly-sized lottery is a rounding error to the book. |
| Entry | Disciplined. Filled at mark not limit; rule-#6 break justified with the refuting measurement, written before the fill. |
| Exit | Disciplined — mandatory rule executed without drift, softening, or a roll. |
| Liquidity | Fine. Both legs deep OI; the vertical traded inside its legs' quoted market. |
| Vol/theta | 🔴 **Killed it.** Not theta — **forward beta.** |
| Rules | **Followed.** No guard relaxed. Stand-down (i) correctly graded MOOT-not-tripped (entry guard, scope expired at fill) rather than reinterpreted in either direction. |
| Calibration | Entry payoff estimate **+45–120%**; actual **−38.8%** → the estimated band **never contemplated the loss case**, which is itself a calibration defect. Exit-day center estimate −47% vs actual −38.8% (Will's better fill). Forward evaluation pre-registered at P≈20%. |

### Loss cause — `BAD_STRUCTURE`
**A near-dated VIX call spread cannot capture a SPOT vol spike.** VIX options settle on the **forward**, which at ~9 DTE carried **beta ≈ 0.28 to spot** (derived by put-call parity at entry). Spot ripped +13.45%; the forward barely moved; our 20 strike never came into the money on the number that actually prices it. Between fill and exit the forward went **19.6 → 18.82**, so moneyness *deteriorated* from **+2.0% OTM to +6.3% OTM** — **after** the event we bought had already occurred.

**The aggravating detail: I flagged this at the fill and did not act on it.** My own §8 note said the low forward beta *"undercuts my own spike-capture argument for the near-dated expiry"* — I wrote the correct diagnosis on the card on day one, downgraded the payoff estimate for it, and still left the strikes and expiry unchanged. **Identifying a structural flaw and then not letting it change the structure is worse than missing it.**

Related and not coincidental: the §6 management triggers were written on **spot** (`VIX ≥23`) while the payoff lived on the **forward** — the same guard-spec defect I flagged to VIOLET on 7/27 as an *entry*-guard issue. It was never only an entry-guard issue.

### Why `GOOD_LOSS_PROCESS_WORKED` is also true
The dated exit did precisely what it was written to do: it closed a losing convexity bet on schedule, at a fair market price, with no roll-by-hope, no expiry drift toward 8/5, and no re-underwriting under pressure. **The rule was written on 7/26 by someone who could not know the outcome, and it was honored on 7/30 by someone who did.** That is the whole point of pre-registration.

### Lesson — two, both durable
1. **If the thesis is a SPOT move, set strikes against the DERIVED FORWARD, or buy enough tenor that forward beta is near 1.** Deriving the forward at entry is not sufficient — the derivation has to be allowed to change the strikes, the expiry, or the decision to trade at all. *(Wired into the card §11.D-1; belongs in `CHART_OPTIONS_WORKFLOW.md` next pass.)*
2. **On a vertical where both legs carry OI >5,000, open the order in the aggressive third of the net bracket, not at mid.** A vertical trades *inside* the sum of its legs' quoted markets. TERRY proposed $0.75 entry / $0.40 exit-start; Will worked $0.70 / $0.45 and both filled — **n=2, both directions, both 5¢ in his favour.** My limit-setting is systematically too generous to the market.

### PENDING — resolves 2026-08-05 (pre-registered, card §11.C)
Counterfactual line, fixed before the outcome: **holding beat exiting iff the 8/5 VIX SOQ prints >20.45.** TERRY pre-registered **P ≈ 20%**. ⚠️ **The exit was transacted at the market's own fair value, so it is EV-neutral by construction — the 8/5 print alone does NOT grade the mandatory-exit rule** (that needs n>1). What 8/5 legitimately grades: VIOLET's fade verdict, her no-re-entry call, TERRY's forward-beta finding, and HENRY's short-gamma amplification steelman.

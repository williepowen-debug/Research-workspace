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

## 2026-08-04 — **THE QQQ SHORT-DATED PUT CLUSTER** (11 tickets, 7/20 → 8/4) — CLOSED, REALIZED ≈ **−$4,341**
**Instruments:** QQQ puts, 0–1 DTE, strikes 672 / 675 / 680 ×2 / 687 ×3 / 693 ×2 / 696 / 698 ×2 / 712 — across Fidelity and Robinhood.
**Thesis owner:** **Will** (his own tape read; uncorroborated — no domain agent consulted on any of the 11).
**Outcome:** **11 of 11 short into a tape that rose +10.1% in four sessions.** ≈ −$4,311 to −$4,371 realized. One live remnant (`QQQ 720P Aug-06 ×1`).
**Tags:** `EVENT_MISALIGNED` (primary) · `OVERSIZED` · `NO_INVALIDATION` · `THESIS_RIGHT_BAD_TIMING` (partial — see §2)

> **Will, 2026-08-04, unprompted and recorded in his own words:** *"the mistake is mine. I was stubborn and kept placing puts not believing the rally."*
> **Logged at his instruction.** It is the correct attribution on direction and it is **not the whole diagnosis** — the rest of this entry is what the figures say beyond it.

### 1. ★ THE FINDING — the view was not the expensive part. The TENOR was.

The identical view existed in the book **twice**, expressed two ways:

| Same view, two expressions | Max loss | Outcome |
|---|---|---|
| `TRY-WILL-QQQ-VFADE` — QQQ **Aug-21** 680P/670P ×2, defined risk, kill line pre-registered at 712 | **$452** | **never fired — $0** |
| 11 tickets, **0–1 DTE**, undefined frequency, no executed stop | uncapped by count | **≈ −$4,341** |

**The swing card would ALSO have lost** — it dies today on its own 712 invalidation. **But it would have lost $452, capped, on a level named in advance.** Same view, same wrongness, **9.6× the cost — entirely from tenor and frequency.**

⇒ **A multi-week structural thesis was expressed through same-day instruments.** With 0DTE, *being early is being wrong* — the instrument makes timing the entire trade, so a view about the next three weeks cannot survive in it. **The correct expression was already built and sitting unfired while the incorrect one ran eleven times.**

### 2. What was NOT wrong

The direction was a **minority-probability view, not an unreasonable one.** Measured the same day (`qqq/RESEARCH.md`): the near-highs V cohort is **n=3 ex-bubble, 2 up / 1 down**, and **2022-03-18 matched this configuration and delivered −21.9% over three months.** That path is real. **Do not file this as "the read was stupid."** It was a live minority branch **sized as though it were the base case.**

### 3. 🔴 The desk's share, and it is mine

- **The hard stop was specified in four consecutive reviews and executed ZERO times.** I re-wrote the same manual stop each time rather than changing its *form*. I noted on 8/4 that *"a rule that has never once fired is a note, not a rule"* — **and then left it as a manual stop for the fifth time.** A control that requires overriding conviction in the moment was never going to fire in the moment.
- **The review loop never saw three of the eleven.** Session 4 closed 8/4 on a total **~$1,260 too small**, published to `STATUS.md` and to a new `qqq/README.md`. **The gap was closed by Will's broker capture, not by the process.** ⇒ *measuring intake, not activity.*
- **The profit-side gap was diagnosed and left unfixed until after it cost money.** The 687P was **+23.6% at Friday's close** with no rule that said take it. `QQQ_DESK_CARD.md` §4b was written the morning *after*.

### 4. What changed as a result

**Structural, because four of the five failure modes were "a rule was written and not followed":** `qqq/PLAYBOOK.md` **G1–G5** — risk computed before the ticket, one ticket per session, a **resting** harvest order at entry, loss capped by structure rather than intention, and a written refutation required after three same-direction tickets. **Plus `RISK_RULES.md` #16** (below): match the expiry to the view's horizon.

⚠️ **The record cannot be scored yet.** Eleven tickets with one direction, variable size, no executed stops and no harvest = **eleven observations with eight uncontrolled variables.** Re-examine at **n≥10 clean tickets under G1–G5**.

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
**Tags:** ⚠️ **RE-TAGGED 2026-07-30 ~11:50 after self-audit** — `NO_HARVEST_RULE` **(primary, new tag)** · `GOOD_LOSS_PROCESS_WORKED` (secondary) · ~~`BAD_STRUCTURE` (was primary — withdrawn, see Loss cause)~~ · ~~`EVENT_MISALIGNED`~~ (withdrawn: the event was **not** misaligned — it landed inside the window as designed)
**⚠️ PARTIAL — outcome-dependent grading is PRE-REGISTERED and PENDING 2026-08-05.** This is the second-ever TERRY postmortem and the first on a real P/L.

### What happened
Bought 7/27 at $0.70 (4 lots) as a long-vol convexity expression into the 7/28-29 FOMC, on VIOLET's short-dealer-gamma thesis. Card carried a **hard-dated 7/30 exit, mandatory regardless of P/L**, written at build time on 7/26. **The FOMC delivered exactly the event the card was built for** — VIX 17.45 → 20.88 intraday on 7/29, +13.45% on the settle, first >20 settle of the episode, VVIX to a new episode high. Fleet was offline that day on a usage outage, so nobody graded it live. By the 7/30 open the vol event was unwinding hard (VIX −11%, term structure back to contango, VVIX −8.4%). All three of the card's strength triggers were formally checked and none fired. Exited on the base branch at **$0.45** net credit.

### Diagnosis
| Dimension | Read |
|---|---|
| Thesis | **Mixed — and this is the interesting part.** The event VIOLET predicted *happened*. The trade still lost. Thesis was not refuted by the tape; the instrument failed to monetize it. |
| Timing | Entry fine (2 sessions ahead of the catalyst). Exit was date-forced, not judgment. |
| Structure | 🟡 **RE-GRADED (self-audit 7/30).** Was 🔴 "wrong — the primary cause." The spread was liquid and correctly sized, and — per VIOLET, ⏳ still unverified — its **LONG 20C leg** went through its strike on the forward. ⚠️ **NOT "the spread went through its strike"** — see the Loss-cause note below; nobody has marked the 4-lot. The defect was in the **management spec**, not the structure. |
| **Management spec** | 🔴 **WRONG — THE PRIMARY CAUSE, and the only row that carries that label.** Every trigger keyed to a further move; **none keyed to being in profit.** See below. |
| Sizing | **Appropriate.** $287.70, under the $300 rec and the $500 cap, N_eff held at 1. A −38.8% loss on a correctly-sized lottery is a rounding error to the book. |
| Entry | Disciplined. Filled **at the fill-moment mid** (not beaten — see the withdrawal note below); rule-#6 break justified with the refuting measurement, written before the fill. |
| Exit | Disciplined — mandatory rule executed without drift, softening, or a roll. |
| Liquidity | Fine — both legs deep OI. ~~the vertical traded inside its legs' quoted market~~ 🔴 **WITHDRAWN 7/30 13:10 — that claim is UNPROVEN, not proven.** It rested on an execution finding built on an **inferred timestamp** (my marks were 21 min after the ~09:50 fill); reconstructing the fill-moment mid collapses the gap to zero. Textbook-true in general, **not evidenced here.** *(`finding_grade_execution_only_against_same_timestamp_marks`.)* |
| Vol/theta | 🟡 **Contributory, NOT the cause** *(re-graded 7/30 13:10; previously 🔴 "Killed it — not theta, forward beta")*. Not theta. Forward beta is real but is **`beta(tenor)`, not a scalar**, and at this card's 9→6 DTE it is **~0.6**, not the 0.28 the original diagnosis used. **At ~0.6 the vehicle could plainly convert a correct call** — which is why the cause moved to the management spec and why VIOLET withdrew her own "losing trade by construction." |
| Rules | **Followed.** No guard relaxed. Stand-down (i) correctly graded MOOT-not-tripped (entry guard, scope expired at fill) rather than reinterpreted in either direction. |
| Calibration | Entry payoff estimate **+45–120%**; actual **−38.8%** → the estimated band **never contemplated the loss case**, which is itself a calibration defect. Exit-day center estimate −47% vs actual −38.8% (Will's better fill). Forward evaluation pre-registered at P≈20%. |

### Loss cause — ⚠️ **REWRITTEN 2026-07-30 ~11:50 ET after a Will-directed self-audit. The original diagnosis is preserved below and was probably WRONG.**

**PRIMARY CAUSE (current):** **`NO_HARVEST_RULE` — every management trigger on this card was keyed to the move going FURTHER, so no rule existed to fire when the position was merely in profit.**

| Trigger (card §6) | Keyed to |
|---|---|
| VIX **spot ≥23** touch → sell half | a much bigger spike |
| VIX3M/VIX **<1.0** → sell rest | a much bigger spike |
| SKEW crash during a spike → sell | a much bigger spike |
| Mandatory dated exit 7/30 | the calendar |

**Nothing was keyed to "this position is now worth more than you paid."** Compare the sibling card `TRY-FIRE-004`: **≥3× → take half** — a P/L-keyed rule that fires on the *position*, not the world. **This card had no such rule, and that is verifiable from §6 today, independent of anything below.**

**Compounding defect:** the trigger variable was **spot**; the payoff settles on the **forward**. Spot had to reach **23**; the position became profitable near spot ~20.7 / forward ~20.5. **The harvest trigger sat outside the path the trade actually travelled.** Same spot-vs-forward guard-spec defect flagged to VIOLET on 7/27 as an *entry*-guard issue — it was never only an entry-guard issue.

⏳ **PENDING VERIFICATION — ⚠️ CLAIM NARROWED 2026-07-30 13:10, at VIOLET's own insistence and against her interest. Do not restore the wider wording.**

~~VIOLET and PROME both assert the position was **profitable at the 7/29 close**.~~ **That overstated both sources.** What each actually said:
- **VIOLET:** the **LONG 20C leg** was through its strike on the forward (~20.5, *"first time through our 20 long strike"*, ~0.5 ITM). She **never** said the spread exceeded the **$0.70 debit** and **marked no option prices** — **she is not a source for "profitable."**
- **PROME:** has **re-labelled its own row an INFERENCE**, and confirms its line and VIOLET's forward are **one inference chain, not two corroborating sources.**

**No broker or chain mark of the 4-lot at the 7/29 close exists anywhere.** A long leg through its strike is **not** the same as a 5-wide vertical above its debit — the short 25C also gains, and the spread can sit under $0.70 with the long leg ITM. **TERRY has not verified it; valuation asks are routed to both owners and it stays PENDING on an actual chain mark.**

**⚠️ This does NOT weaken the primary cause, which is why the narrowing is safe to make honestly:** `NO_HARVEST_RULE` is established from the card's own §6 trigger set at **n=0** — *no trigger was keyed to being in profit* — and that is true whether or not the position was ever in profit. **If** a mark later confirms profit, it becomes direct proof rather than the load-bearing evidence.

<details><summary>~~ORIGINAL DIAGNOSIS (2026-07-30 ~10:50) — retained as the record, superseded~~</summary>

> ~~**A near-dated VIX call spread cannot capture a SPOT vol spike.** VIX options settle on the **forward**, which at ~9 DTE carried **beta ≈ 0.28 to spot** (derived by put-call parity at entry). Spot ripped +13.45%; the forward barely moved; our 20 strike never came into the money on the number that actually prices it.~~
>
> **Why it was withdrawn — two independent defects:**
> 1. **The beta figure was wrong.** ≈0.28 came from a single **0.36-point** intraday move at the fill — noise. **Realized fill→exit beta was 0.53** (spot 19.85→18.37 = −1.48; forward 19.60→18.81 = −0.79). ⚠️ **0.53 was ITSELF superseded ~5 hours later (7/30 13:10) and is retained here only as the 11:55 state:** VIOLET's independent OLS (ΔM1~ΔVIX, n=246 CBOE settles) gives **`beta(tenor)` — 21–35 DTE 0.274 · 11–20 DTE 0.505 · ≤10 DTE 0.591** ⇒ **~0.6 for this card's 9→6 DTE.** **0.28 was the right number for the wrong tenor; 0.53 still understated.** Current figure lives in the Diagnosis table's Vol/theta row — **do not cite 0.53 forward.**
> 2. **"The forward barely moved" is contradicted by the sources this postmortem was written from.** If the forward reached ~20.5 on 7/29 it went **through** the 20 strike — the structure **did** capture the move. The original text asserts the opposite without ever mentioning the claim, which sat in VIOLET's brief in my own inbox.
>
> *(The "aggravating detail" — that I derived the forward at entry, wrote the low-beta warning on the card, downgraded the payoff estimate, and left the strikes unchanged — remains factually true, but it is no longer the loss cause.)*
</details>

### Why `GOOD_LOSS_PROCESS_WORKED` is also true
The dated exit did precisely what it was written to do: it closed a losing convexity bet on schedule, at a fair market price, with no roll-by-hope, no expiry drift toward 8/5, and no re-underwriting under pressure. **The rule was written on 7/26 by someone who could not know the outcome, and it was honored on 7/30 by someone who did.** That is the whole point of pre-registration.

### Lesson — ⚠️ **REORDERED after the 7/30 self-audit; #1 is new and replaces the withdrawn structural lesson**
1. **★ EVERY CARD WITH A DIRECTIONAL PAYOFF GETS A P/L-KEYED HARVEST RULE — not only world-keyed triggers.** Before freezing management terms, ask: **"is there a path where this position is profitable and NO trigger fires?"** If yes, that path will happen. This card had three triggers and every one needed the move to go *further*; `TRY-FIRE-004` has *≥3× → take half* and would have caught it. **Adopt as a build-time check on every card.** *(→ auto-memory `finding_profit_zone_needs_its_own_harvest_rule`.)*
1b. **State triggers on the variable the payoff SETTLES on**, and treat the forward's beta as **`beta(tenor)`, never a scalar** — quoting one number is itself a specification error. VIOLET's independent OLS (n=246 CBOE VX M1 settlements): **21–35 DTE → 0.274 · 11–20 DTE → 0.505 · ≤10 DTE → 0.591** (pooled 0.345). *(Original lesson #1 said "set strikes against the derived forward"; that survives as build-time practice but is **not** the loss cause. **The beta was wrong twice**: ≈0.28 was the right number for the **wrong tenor**, and the §11.F "correction" to 0.53 **still understated** it — this position lived 9→6 DTE, so **~0.6**. The gradient is robust; the point estimate is not, n=19 in that bucket.)*
2. ❌ ~~**On a vertical where both legs carry OI >5,000, open the order in the aggressive third of the net bracket, not at mid.** … n=2, both directions, both 5¢ in his favour.~~ **WITHDRAWN IN FULL 2026-07-30 ~13:10 (card §11.G-2). n=2 → n=0.** The fill was **~09:50** (FORGE's 09:40 export still carries both legs — hard lower bound); **my marks were pulled at 10:11, after the trade was done**, with VIX 18.8 → 18.37 in between. Reconstructing the 09:50 mid gives **0.44–0.45 across every candidate beta** — **Will filled at the 09:50 mid, I recommended the 10:11 mid; both said "mid," there was never a divergence.** The entry leg collapses identically: $0.70 *was* the mark (§8). *The microstructure claim itself is textbook-true but is now **unproven, not proven** — re-establish with same-timestamp data or not at all.*
2b. **★ REPLACEMENT LESSON, and it is the more serious one: never grade an execution against marks from a different moment.** Establish the fill **timestamp** from a physically dated artifact first; if you cannot, the correct output is **"cannot grade,"** not a comparison. **I built a behavioural conclusion about myself on an inferred timestamp, wrote it to durable memory, and reported it to Will as measured** — in a tape moving ~2%/hour, 20 minutes of drift exceeded the entire effect I claimed to detect. ⚠️ **Self-findings need MORE scrutiny than market findings, not less**: they feel unfalsifiable, they flatter the finder, and they steer future decisions from memory. *(→ auto-memory `finding_grade_execution_only_against_same_timestamp_marks`.)*

### PENDING — resolves 2026-08-05 (pre-registered, card §11.C)
Counterfactual line, fixed before the outcome: **holding beat exiting iff the 8/5 VIX SOQ prints >20.45.** TERRY pre-registered **P ≈ 20%**. ⚠️ **The exit was transacted at the market's own fair value, so it is EV-neutral by construction — the 8/5 print alone does NOT grade the mandatory-exit rule** (that needs n>1). What 8/5 legitimately grades: VIOLET's fade verdict, her no-re-entry call, TERRY's forward-beta finding, and HENRY's short-gamma amplification steelman.

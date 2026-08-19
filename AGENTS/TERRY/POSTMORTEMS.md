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

---

## 2026-08-07 — **TRY-FIRE-007 (FXY carry-convexity calls) — PROCESS postmortem, NO TRADE.** Killed by its own pre-registered gate. `$0` at risk, build to death.

**Thesis right/wrong:** **wrong, and graded so by its owner.** SAM's carry-convexity tail was built on a record-short JPY crowd (−163,412 = **90.8%** of the −180K peak, Jul-28 data). The Aug-4 print showed **−45,473 = 25.3%** — the crowd did not merely thin, it **reversed** (WoW +117,939 on OI that barely moved: shorts covered 71,982 *and* longs added 45,957). SAM's THESIS leg-1 SPF also fired ⇒ **frame → LOW, a thesis-BREAK.** SAM-40 ❌ · SAM-29 ❌. *(Cited, not re-adjudicated — thesis truth is SAM's.)*

**Timing right/wrong:** **right, and it is the only reason this line reads `$0` instead of `−$180`.** The card was built 8/3 and parked. Three brakes, all pre-registered *before* the number existed, all held:
1. **Card §8 — the root-rule-#6 break test.** *"As of this build I do NOT hold a measurement that refutes the proxy … no break, no early fire. 'The window is closing' is a chase, not a break."* SAM credits this as the reason the §5C override that fired **on the letter** on 8/3 was not acted on. ★ **This is the first time the Will-ratified 7/27 break test has demonstrably PREVENTED a loss rather than merely governed one.** It has been cited on cards for eleven days; this is its first outcome.
2. **Will's Monday-execution ruling**, recorded 8/7 AM pre-print.
3. **SAM's WAIT-FOR-8/7** entry recommendation, never overridden.

**Structure right/wrong:** ⚠️ **one real defect, and it is mine.** The whole §4 case for the 60C over 005's 58C/59C ladder was liquidity — *"OI 33,541 at a **10.5% spread**."* `RISK_RULES` **#14** classifies OI as a **structure** property (gradable any time) and **spread% as a MOMENT property** (grade once, at fire). **I let the moment half carry a vehicle-SELECTION argument four days ahead of any possible fill.** It quotes **40%** today. *Honest other side, because it cuts against my own finding:* a strike's liquidity is partly **contingent on the thesis being live** — spreads widen when nobody wants the strike — so part of 10.5% → 40% is the thesis dying, not a build-time measurement error. **Both are true.**

**Sizing right/wrong:** **right, and it was corrected against my own interest before it mattered.** On 8/4 I struck my own §7.5 `N_eff += 1` claim after NEXUS showed 004 and 007 share the policy-authority root, and cut ~~9× / $450~~ → **5–6× / $250–300**. The cut never had to be tested, but the reasoning that produced it was sound and independently measured by SAM.

**Rule violated:** none. **Lesson (and it is a rule, not a note):** ★ **when a vehicle is chosen on LIQUIDITY, split the claim — the OI half is structural and may be quoted ahead; the SPREAD half is a moment property and must be re-pulled at fire. Never let the moment half carry the selection argument.** → `RISK_RULES` #14 corollary.

**Cost, measured rather than assumed:** at build (8/3 10:13) FXY 58.60, Sep-18 60C 0.45/0.50 mark 0.47. At the **8/7 close** (`chain_fetch` 16:26; **market closed — a settled-session quote, not a live price**) FXY 58.24, 60C **0.20/0.30 mid 0.25**. An 8/3 fire at the $0.50 limit marks **≈ −50% at mid, ≈ −60% at the exitable bid** ⇒ **≈ −$150–180** at the recommended size, **≈ −$270** at the 9× I originally defended. **`$0` was at risk instead.**

**Loop closed:** SETUPS.tsv · setups/INDEX.md · TRADE_BOOK.md (revision row) · FIRE_CARDS_LADDER.md (§007 added — **it had been absent for the card's entire life**) · card §11 · STATUS. **A re-arm needs a fresh build and a NEW id.**

> ⚠️ **A second, smaller finding worth its own line: `FIRE_CARDS_LADDER.md` never listed 007 at all.** The card lived four days carrying a dated gate on a file whose header claims to be the fire-card comparison view. **A registry that is authoritative for 001–006 and silently partial for 007 is worse than one that is obviously incomplete — nobody greps a file they believe is complete.** Same class as the 005 `SHELVED` defect, where `INDEX.md` was right and the other tracker was the liar.

---

## 2026-08-07 — **TRY-VIOLET-VIXCS — the pre-registered evaluation, RESOLVED.** *(Appendix to the 2026-07-30 postmortem above; the trade's P&L is unchanged at −$111.60 / −38.8%.)*

**⏰ Graded two days late.** Resolver date was **Wed 8/5**; this is **Fri 8/7**, desk dark 8/5–8/6. **Logged, not glossed** — and the card's own §11.C named this exact failure mode (*"this desk's failure mode with dated gates is not getting them wrong, it is not grading them at all"*). **The pre-staged checklist is the only reason two dark days cost latency and nothing else.** Detection was never the gap; invocation was — for the third time.

**The number:** **VIX SOQ (`VRO`) 2026-08-05 = 17.10** vs the frozen line **>20.45** ⇒ `min(max(17.10−20,0),5)` = **$0.00**. We banked **$0.45** ⇒ **exiting beat holding by the full $0.45/spread = $180** on the 4-lot. **TERRY's pre-registered `P≈20%` was on the correct side** — **one** calibration observation, not a vindication: a 20% event failing to occur is the expected outcome 80% of the time.

> ⛔ **AND THE CAVEAT BINDS HARDER NOW THAT IT FAVOURS US.** We exited at the market's own fair two-sided price ⇒ the exit is **EV-neutral by construction**. **"We saved $180 by exiting" is the identical outcome-bias error as "we left $X on the table," with the sign flipped** — and it is the one this desk would actually be tempted by, because it flatters. It was rejected in writing on 7/30 before the number existed; **rejected again now that the number is known and friendly.** ⛔ **The dated-mandatory-exit RULE is still not graded and still needs n>1.** Refused for the third time on this card.

**Rows 1–4:** **1 ✅ TRUE** (VIOLET's fade — VIX never printed >20.45 after 7/29; window max **18.43** intraday 8/5, still **2.02** under) · **2 ✅ TRUE** (no-re-entry — the structure settled **$0.00**, so a re-entry at any price on any day lost 100% of the new debit) · **3 ⚠️ NO-VERDICT** · **4 ✅ TRUE** (short-gamma steelman — SPX **7,316.15** low 7/29 → **7,723.55** 8/5 close = **+5.6% in five sessions**, largest single-session drawdown in the window **−0.17%**, VIX 20.66 → 15.81; **the amplification HENRY warned about had no down-leg to amplify**).

**🔴 THE FINDING, and it is against myself — ROW 3 WAS A DEFECTIVE TEST.** Two independent reasons it cannot be graded:
- **(a) No instrument.** The 8/5 forward was never captured after the 7/30 exit; the contract has since expired. Per `finding_verification_zero_is_ambiguous` this is **"no measurement," not "no effect"** — it must not be recorded as a quiet pass.
- **(b) ★ It could not have discriminated even with perfect data.** The row reads *"FALSE if forward beta rises materially as expiry nears **(it should — beta→1 at settle)**."* **The parenthetical concedes it.** A futures contract converging to settlement is the definition of a settlement, not evidence about `beta(tenor)`. The endpoint arithmetic demonstrates the trap rather than escaping it (18.82 → 17.10 forward vs 18.35 → ~16.15 spot ⇒ ratio **0.78** > the ~0.6 OLS bucket) — **and it would have read that way whatever the market did.** ⛔ I am **not** publishing 0.78 as a beta measurement: a two-point endpoint ratio taken *through* the convergence window, across two differently-constructed quantities. **This card already carries a documented incident about publishing precision beyond what was measured** (18.71 → 19.11, 1.0888 → 1.0683).
- **✅ The §11.D-1 FINDING is unaffected** — established at the fill by same-chain put-call parity and re-derived by VIOLET's OLS at n=246. **The ROW was defective, not the finding** (`finding_claim_outlives_its_discredited_instrument`).

**⇒ DURABLE LESSON: a pre-registered row must have BOTH branches reachable.** Before locking one, ask the inverse of the escalation-line test — not *"would it fire on day one?"* but **"could the FALSE branch have failed to fire?"** If the answer is no, it is a description wearing a test's clothing. **This row shipped with its own defect written in a parenthesis and nobody caught it for eight days, including me, twice.**

**★ AND THE THING THAT WORKED, recorded because it is invisible by design:** row 4's 8/4 guard forbade grading on the retired **7,455** band (same number now live as a Goldman CTA trigger). The easy route — *"SPX 7,723 is miles above it ⇒ row 4 TRUE"* — reaches **the same verdict by an illegitimate path.** **A guard whose only effect is to change the REASONING while the ANSWER stays put is exactly the kind nobody notices is working — and exactly the kind that matters on the day the two answers diverge.**

**Evaluation CLOSED. `PB-0003` closes with it.** Final ledger: realized −$111.60 · counterfactual **exiting ≥ holding** · **P≈20% correct-side** · rows **1 ✅ · 2 ✅ · 3 ⚠️ NO-VERDICT · 4 ✅** · **the exit rule remains ungraded.**

---

## 2026-08-13 — TRY-BRENT-USOARM — died UNFIRED at arm expiry; the move arrived during the approval window

**What died:** USO Oct-16 125C/130C ×2 @ $1.50 limit ($300 max loss), BRENT's v5.0 main convex arm. Built 8/3-8/4, gate v3 (a: OVX daily state · a2: live non-reversal · b: net debit ≤33.0% of width at fill), arm window 20 days, expired 2026-08-13. Will ruled let-expire in session. **$0 at risk from build to death.**

**Thesis right/wrong:** RIGHT, on BRENT's axis — USO 115.96 → 126.11 (+8.8%) inside the arm window, through the card's own 126.50 breakeven zone. Not TERRY's grade to make beyond noting the tape.
**Timing right/wrong:** the GATE timed it correctly — leg (a) fired 8/3, leg (b) passed at 12:24 on 8/4 (26.0% worst-case, 7.0pp inside the line). The fire-ready state existed and was measured on the record.
**Structure right/wrong:** RIGHT. Clean on every construction axis; never retracted.
**Sizing right/wrong:** moot — never filled. The ×2/$300 spec was two-constraint clean after BRENT's 11:48 ruling.
**What actually killed it:** neither thesis, timing, structure, nor sizing. **The card sat DECISION-READY for 9 of its 20 arm days with no [Approve]/[Reject], and the move repriced leg (b) from 26.0% to 37.6%-at-mid/58.0%-worst-case — unpassable by intrinsic arithmetic alone (spot−125 = $1.11 = 22.2% of width).** On expiry day the correct action was refusal: filling would have required chasing a $1.50 limit to ~$1.90+ mid to catch a move already made — the exact chase the root-rule-#6 break test names.

**Counterfactual, measured both ways (11:39 chain vs the 8/4 12:24 grade):** 8/4 fill at worst-case $1.30 (or the $1.50 limit) → 8/13 **mid $1.88** (+45% / +25%) but **exitable at the touch $0.85** (negative). ⛔ **A modest miss at mid and a loss at the touch — NOT the large miss it feels like. Do not cite this episode as "latency cost us a multiple."** (TERRY's own in-session estimate of "~$3+" from intrinsic reasoning was wrong and is corrected here: an intrinsic floor settles *passability* — correct use — but does not *price* a spread whose short leg still carries 64 DTE of time value.)

**Rule violated:** none. **Lesson (routed to BRENT, his gate design):** a dated arm whose fire condition is a MOMENT property (RISK_RULES #14, half-life ~40 min) cannot depend on a human approval loop measured in days with only an EXPIRY date for pressure. Either a **DECISION-BY date** distinct from arm expiry, or a standing **[Approve in principle]** stage (durable finding 3) so a passing gate can fill inside its own half-life. The gate itself performed perfectly — including refusing the fill on the last day.

**Tags:** `GOOD_PROCESS_BAD_OUTCOME` (and the outcome-cost is measured small; arguably good-process-fine-outcome).

**Open design question, routed to the owed paper-book counter fix, NOT retro-actioned:** all v3 legs read MET at 13:57 on 8/4 — does an approval-gated arm in that state constitute a PAPER_BOOK would-fire row? Creating one retroactively today would violate the fill rule (fills at trigger timestamp); the question is whether the *next* such state auto-logs.

---

## 2026-08-13 — TRY-WILL-QQQ-VFADE — died VOID before it could die wrong; closed a day ahead of its time stop

**What died:** QQQ Aug-21 680P/670P debit spread ×2 @ $2.26 = $452 max loss. Will's own tape read (fade the unconsolidated V into the 704–712 shelf), built 8/3, labelled UNCORROBORATED on the card from the first line. Never approved, never armed. **$0 at risk from build to death.** Formally closed 2026-08-13 on Will's instruction, one day ahead of the 8/14 time stop.

**Thesis right/wrong:** WRONG on the card's own window — QQQ 697 (build) → 712+ (invalidation, 8/4) → 730.01 (closure, 11:59 live). The V never based. *(Scope: this grades the card's window, not the person — and the fade instinct's one real moment, the 687P at +23.6% on the 8/1 close, is already banked as the profit-side-gap finding in `QQQ_DESK_CARD` §4b.)*
**Timing right/wrong:** the entry was rule-#6 clean (first ticket of its class on the correct day-colour). The tape then went the other way immediately.
**Structure right/wrong:** RIGHT, and this is the card's whole value: defined risk, kill pre-registered at a named level (712), hard condition written against the owner's own book (ONLY QQQ short), time stop dated. Every control fired exactly as written.
**Sizing right/wrong:** $452 vs the 2R/$500 cap — inside, correctly.
**What actually killed it:** both kills at once, 8/4 — the 0DTE tickets voided the hard condition AND the 712 line went. It was dead before any approval decision was ever required.

**Counterfactual, measured at closure (QQQ 730.01, 680P 0.26/0.28 · 670P 0.17/0.18):** an approved 8/3 fill would mark **$0.08–0.10 vs $2.26 = ≈−$432 / −96% unmanaged**; the pre-registered 712 kill would have exited it earlier at a partial loss. **The kill line bounds even the counterfactual — that is what a pre-registered invalidation is for.**

**The durable point is already a rule and this closes its loop:** `RISK_RULES` #16 carries this card as its worked example — the identical view ran simultaneously as 11 tickets at 0–1 DTE (≈−$4,341, uncapped by count) and as this $452 defined-risk card (never fired, $0). **Same view, same wrongness, 9.6× the cost — tenor and frequency were the expensive part.** Nothing new to adopt; the closure makes the example's ledger entry complete.

**Tags:** `THESIS_WRONG` (window-scoped) · `GOOD_PROCESS_BAD_OUTCOME` does NOT apply — the outcome was good ($0); the process produced a correct refusal by construction.

---

## TRY-FIRE-006 — Kharg-strand → USO call spread — **RETIRED UNFIRED 2026-08-18** (Will-ruled, TERRY-recommended)

**Built:** 2026-07-17 ~15:40 ET · **Retired:** 2026-08-18 EVE · **Life:** 32 days · **Capital at risk: `$0` from build to retirement — never armed, never fired, no fill ever existed.**

**Tags:** `STALE_DATA` (primary — the pre-locked layer rotted) · ⚠️ **no P&L loss-cause tag applies: there was no trade.** Recording it anyway, because *"nothing happened"* is exactly the outcome that escapes review.

### Thesis / timing / structure / sizing
- **Thesis (RED + BRENT + FALCON): NOT GRADED — and deliberately not.** The card died on *lifecycle*, not on a thesis verdict. A Kharg strand may still happen; **retiring the card is not a claim that it won't.** ⛔ Do not cite this postmortem as evidence against the premise.
- **Timing: the trigger never fired — through the most favourable 32 days it will ever see.** MOU expired 8/17 no deal · extension refused · threat aimed at Muscat · crude cleared a settle it had failed 5 sessions · throughput ~21% of baseline. **That is the finding: if not then, the strand is either not happening or not measurable by us. Both are "no trade."**
- **Structure: SOUND, and re-verified at retirement.** Strikes were specified **relative to the post-gap print** (not locked), so USO's +12.7% run since 8/4 never staled them. The spread mandate was correctly conditioned on **fire-day** vol. **Two of three staleness hypotheses I tested FAILED — recorded as failed.**
- **Sizing: never reached.** $200 fenced, untouched.

### 🔑 The four lessons, and only one is about oil

1. **🔴 A PRE-LOCKED LAYER ROTS, AND IT ROTS SILENTLY IN THE PLACE YOU TRUST MOST.** ZONE 1 is written calm and read under pressure — so any hardcoded figure in it decays *while looking authoritative*. **Both rot instances here were hardcoded counts:** §9's concentration guard (**stale by 2.23×** — $2,813 assumed vs $6,262 actual) and the fire-time position line (still *"20 sh"*). ⚠️ **A stale concentration guard does not fail loudly — it PASSES.** ⇒ **never hardcode a position figure in a pre-locked layer; point at the live source.**
2. **🔴 A RELATIVE CLOCK CANNOT FIRE.** *"Retire if unfired at ~30d"* — a tilde has **no fire date**, so nothing can be *late* against it and no boot check can flag it. It drifted to **day 32** unnoticed. ⇒ **self-destruct clauses take ONE ABSOLUTE DATE**, and reaching it without a written grade is itself the defect.
3. **🔴 AUDIT THE TRIGGER'S EXECUTABILITY, NOT JUST ITS LOGIC.** The primary listed **four** corroborator doors; **one (Kpler/Vortexa dark-fleet read) is not available to this fleet** — no API, no credential, no fetcher — **and it was the only QUANTITATIVE door.** The card read as four doors and had three, for 32 days, unwritten. ⇒ **for each named corroborator, state HOW WE PULL IT. A door we cannot open is not a door.**
4. **⚠️ A GUARD FIXED ON ONE SIDE READS EXACTLY LIKE A GUARD ON EVERY SIDE.** FALCON's 7/18 inversion correctly made the AIS series **veto-only on the FIRE side** and left the **RETIRE side** grading on the same impeached instrument. The general form (written 8/18): **a measurement bias has a FIXED SIGN, but whether it is protective or dangerous belongs to the TEST it feeds.** AIS under-counts ⇒ nonzero is trustworthy, zero is worthless — **in both directions**. Unfixed, it allowed *"failure to retire"*: loadings could genuinely resume while the card rode a dead premise.

### ✅ What did NOT die with the card
Design extracted **before** archiving → **`research/PLAYBOOK_flow-trigger-supply-strand.md`**: the corroborator-anchored + AIS-veto-only pattern (FALCON) · the chokepoint-transit-count ban (PROME's denominator ruling — ≤18/day fires on **86.6% of ALL crisis days**) · the antecedent gate (BRENT/PROME) · the rule-#6 gap-continuation pre-authorisation · the one-directional-bias rule. **Retiring a card must not delete cross-agent work that cost real effort to produce.**

### ⚙️ Two process findings from the retirement itself
- **Reconcile EVERY surface BEFORE archiving.** Archiving removes a card from `ledger_sweep` check A, so the move **ends the only thing that would catch drift.** Doing it in that order caught **two live disagreements** (`TRADE_BOOK` still ARMABLE; a ZONE-3 template arguing with the header) that would otherwise have been frozen into the archive permanently.
- **`FIRE_CARDS_LADDER.md` failed a THIRD distinct way** — it still read `PRE-BUILT / SHELVED` (19 days stale, corrected on three other surfaces 7/30) **and** *"BLOCKED before ARM: needs a Kharg data source"* (32 days stale — discharged 7/18). `ledger_sweep` flagged **neither**. Prior failures: 007 absent entirely (8/7), 005 SHELVED (8/4). ⚠️ **A registry believed complete is worse than one obviously partial — nobody greps a file they trust.**

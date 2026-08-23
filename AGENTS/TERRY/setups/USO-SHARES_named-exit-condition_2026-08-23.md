# EXIT-CONDITION PROPOSAL (SCAFFOLD) — USO 35 shares — named exit condition
**Setup ID:** `TRY-EXIT-USO35` · **Class:** EXIT-CONDITION (not an entry card; no new capital contemplated)
**Commissioned:** WILL_QUEUE row 58, **RULED 2026-08-21** — Will's verbatim word: *"Rule row 58 and row-31 off your rec."* Record: `PROME/proposals/2026-08-21_row58-RULED-named-exit-condition-commissioned.md`. The chosen-no-rule branch was **REJECTED**; TERRY's own #9 framing (winner-with-no-plan, the VIXCS lesson) carried the rec.
**Built:** 2026-08-23 Sun ~00:2x ET (`date` wall clock, copied not inferred)
**Terry verdict:** 🟡 **CONDITIONAL — SCAFFOLD ONLY: structure complete, LEVELS BLOCKED on live marks.** Not yet a proposal Will can rule on.

> 🔑 **Why the verdict word is `CONDITIONAL` and not `SCAFFOLD`.** My first draft of this header said **SCAFFOLD**, and `ledger_sweep` **check F** immediately flagged it as an unreadable state claim — a cell with text that matches no known state contributes **nothing** to check A, so its agreement with the other surfaces would have read as verified when it was merely unread. **The tempting fix was to add `SCAFFOLD` to the tool's `STATES` vocabulary. That is the move the tool forbids by name** — its own comments record two separate occasions where widening the vocabulary to clear a check-F finding *regressed* the sweep, and the standing rule is that the vocabulary may only contain words this desk already uses **as a state claim**. `SCAFFOLD` is a word I invented ten minutes ago. **Correct response per the tool's own doctrine: fix the SURFACE.** The card's real state *is* `CONDITIONAL` — conditional on Monday's live marks — and `SCAFFOLD` survives as the descriptive qualifier. All three surfaces (card / `INDEX.md` / `SETUPS.tsv`) say `CONDITIONAL`. `[[finding_test_the_guard_not_just_the_guarded]]`

> # ⛔ THIS DOCUMENT NAMES NO LEVELS, AND THAT IS DELIBERATE
> **Markets are CLOSED.** It is Sunday 2026-08-23 ~00:2x ET; the last tape is **Friday 8/21's close**. The commission's requirement #1 is **live marks + live book at build** (root rule #4 / position-truth canon, *never* the FORGE mirror). **I cannot satisfy it tonight and I will not fake it.**
>
> **What that forbids:** every numeric trigger below is a **named SLOT, not a number.** ⛔ **Do not read any slot as a proposed level.** ⛔ **Do not fill a slot from `FORGE/STATUS.md`, from this desk's STATUS, or from the dated 8/18 figures quoted in §1 — those are CONTEXT and are stale by construction.**
>
> **What it permits, and why this session was still worth spending:** *structure* is a **STRUCTURE property** and *levels* are a **MOMENT property** (`RISK_RULES` #14). The structure can be settled now, in daylight, with nothing at stake — which is the whole argument for doing it before the tape forces it. **Monday's session fills the slots and produces the ratifiable proposal.**
>
> **⛔ THE LEVELS ARE WILL'S TO RATIFY (commission requirement #4).** Nothing here is approved by its own existence. TERRY proposes; Will [Approve]s; PROME registers the ratification row.

---

## 0. What is being decided, stated narrowly

**Position:** **USO 35 shares**, basis **$121.88**. Linear, long, no expiry, no theta.
**The gap:** it is a winner with **no exit plan** — the exact `NO_HARVEST_RULE` shape (`RISK_RULES` #9) that produced this desk's only realized loss.
**What this document is:** a rule that says when the shares come off.
**What it is NOT:** ⛔ **Defining an exit is not taking one. A harvest is not a trim** (7/31 precedent). **`$0` moves here, and nothing fills without Will's [Approve].**

---

## 1. Inputs consumed (dated CONTEXT — none of it is a live mark)

| Input | Source | Vintage | Status |
|---|---|---|---|
| Basis $121.88; 8/18 framing **+$307.30 / +7.20%** | TERRY 8/18 / PROME commission | **8/18 — STALE** | context only; **re-mark at build** |
| Sleeve concentration **95.9% USO-linked, `N_eff = 1`** | BRENT 8/21 | 8/21 | ⚠️ **load-bearing — see §5** |
| Thesis-break observables **B-1 / B-2** | BRENT `2026-08-21_row58-shares-leg-thesis-break-observable.md` | 8/21 | **B-1 REFUTED as a trigger — see §3** |
| **B-1 base rate, n=2,887 (pre-war 2,770 / war 117)** | BRENT CORRECTION, same day | 8/21 | ⭐ **the finding that shapes this design** |
| **Roll yield: n=67 months, post-restructure 2021-01→2026-07** | BRENT 8/21 | 8/21 | see §4 |

---

## 2. ⭐ THE STRUCTURAL FINDING THIS DESK CONTRIBUTES — BRENT'S LATENCY RESULT REALLOCATES THE WORK

BRENT delivered a **constraint, not a caveat**, and named it as such: `L11` + `L16` both say a **confirmation-keyed exit on a premium position fires LATE BY CONSTRUCTION.** His base rate then proved it from a second, independent direction: to be false-positive-free in-sample, a B-1 persistence rule must exceed **25 trading days ≈ 5 calendar weeks.** ⇒ **the latency is not a parameter to tune — it is a property of exiting on price confirmation.** Tighten it and it fires falsely; loosen it and it fires late.

**BRENT framed the consequence as a choice between two bad options** — accept gap risk on a confirmation-keyed exit, or pre-commit to an announcement-class signal his own rules (`L18`/v5.4) call inadmissible. **He was right to hand that over rather than bury it. But read as a CONSTRUCTION problem there is a third answer, and it is the one this scaffold takes:**

> ## 🔑 IF THE THESIS-BREAK LEG IS LATE BY CONSTRUCTION, IT CANNOT BE THE PRIMARY RAIL. THE PROFIT-KEYED LEG MUST CARRY THE LOAD.
>
> A **profit-keyed** trigger reads the **position's own P&L**. It has **zero latency, zero base-rate problem, and no forecast content** — it does not need to know why the price moved, or whether the thesis is intact. It cannot fire late relative to a thesis break because **it is not keyed to the thesis at all.**
>
> ⇒ **PROFIT-KEYED = PRIMARY. THESIS-BREAK = BACKSTOP.** Not co-equal legs. The commission asked for ≥1 profit-keyed leg *paired with* a named thesis-break leg; the ordering between them is a construction call, and it is **mine**, and BRENT's own measurement is what settles it.
>
> ⚠️ **This is not a downgrade of BRENT's work — it is the use his work actually supports.** He explicitly declined to invent a faster signal to paper over the latency. Reallocating the load to a leg that needs no signal at all is the honest response to that refusal.

**And the VIXCS lesson lands differently on SHARES, which sharpens the same point.** VIXCS died with a hard expiry and every trigger keyed to the move going further. **Shares have NO expiry and NO theta — "expires worthless" cannot happen here.** The failure mode is not decay; it is **round-tripping an open gain.** ⇒ the profit-keyed leg should be **ratcheting, not a fixed target** — a fixed target caps the winner BRENT's roll-yield work says is being paid to run (§4), while a ratchet protects the gain without capping it. *(Slot forms in §6.)*

---

## 3. Thesis-break leg — what BRENT delivered, and what may NOT be built from it

### ⛔ B-1 (prompt premium = Dated Brent − front futures) is **REFUTED AS A TRIGGER.** Do not build a stop on it.
BRENT offered B-1 as *"registerable now, level needs a base rate,"* **then ran the base rate himself and it killed it.** n=2,887 daily obs 2015→2026.
- ✅ The sawtooth caveat **cleared** — bucket medians differ $0.23–0.25 against sds of $1.78 / $6.57.
- ✅ The separation is **real** — pre-war p95 **+2.39**; war mean **+4.50**, median +3.31; live **+4.27**, still war-regime.
- ⛔⛔ **AND: 38% of war days (44/117) sit AT OR BELOW the pre-war-normal bar.** Longest episode: **2026-06-12 → 2026-07-20, 25 consecutive trading days at/below the bar, going NEGATIVE to −3.27, ending THREE DAYS before Brent printed $100.69 on 7/23 — the highest price of the war.**
- ⇒ **A B-1-keyed exit would have sold this leg at the bottom, five weeks before the largest up-move in the thesis's history.**

**✅ B-1 SURVIVES AS CONTEXT.** Base-rated, instrument already pulled at every BRENT boot, sawtooth dismissed, and it tells you where the physical premium sits against both regimes. **Worth reporting at every closeout; worth nobody's stop-loss.** ⚠️ **It lags ~2 sessions by construction — never grade it off a STATUS-carried figure.**

### ⛔ B-2 (M1−M3 flip to contango, sustained) is **NOT the better instrument — it is the UNMEASURED one.**
BRENT was explicit and I am adopting it verbatim in force: **preferring the instrument he has not managed to falsify yet would be the same error as trusting a guard whose clean output has never been tested.** Its base rate needs named-contract curve assembly (`L23` forbids `=F` deltas) and has not been done. **B-2 may NOT be promoted into the primary rail by default.**

### ⛔ Join discipline — binding
- **OR-join, or scope to separate surfaces. NEVER AND-join.** B-1 is physical, B-2 is paper; they fail in different directions, and AND-joining reproduces `[[finding_compound_gate_jointly_unsatisfiable]]`.
- **No level from BRENT, deliberately** — neither has a base rate that supports one, and naming one today is the un-base-rated threshold `L21`/`L22` forbid. ⛔ **TERRY does not name one on his behalf either** (root constraint: set no new threshold on another desk's lane).

### ⛔ Scope fence, from BRENT and honoured
**The unsatisfiable `60–90 DTE` band is an OPTIONS thread and is explicitly scoped OUT of the shares leg.** It surfaced on his sweep by concept-overlap only. **Do not import it here.** *(It is separately mirrored as `RISK_RULES` #21 for the options lane — that mirror does not reach this document.)*

---

## 4. The shares-leg clock — roll yield, and the bound it does NOT provide

BRENT measured the clock the ruling asked for, distinct from the options clocks: **it is roll yield.** USO monthly return minus WTI spot (`DCOILWTICO`), incomplete month excluded, post-restructure **2021-01→2026-07, n=67:**

| | |
|---|---|
| mean | **+1.12 pp/mo** |
| negative months | **28%** |
| worst month | **−3.42 pp** |
| longest consecutive negative run | **TWO months** |
| 2026 YTD | **+3.05 pp/mo** |

⇒ **The leg is currently PAID ~+3 pp/month to be long, on top of price.** **That is a real argument against a hair-trigger exit** and it is the strongest single reason the profit-keyed leg should **ratchet rather than cap** (§2).

⛔ **BUT DO NOT TURN IT INTO A RISK BOUND, AND THE REASON IS PRECISE:** the bad state is **UNOBSERVED, not bounded.** 2021–26 was overwhelmingly backwardated, so the sample **barely contains contango** — **empty-in-regime, not structurally empty.** ⚠️ **The 2020 row (−49.62 pp worst month) is contaminated by negative WTI prices and USO's own forced restructuring — an upper bound of unknown tightness, not an estimate, and effectively a different instrument.** ⇒ **`worst month −3.42` may NOT be used as a downside parameter in any sizing or stop arithmetic.**

---

## 5. ⚠️ THE CONSTRAINT THAT OUTRANKS THE REST OF THIS DOCUMENT

**Sleeve concentration: 95.9% USO-linked, `N_eff = 1`** (BRENT, 8/21). **Every expression in the oil sleeve dies on one event — a genuine Hormuz reopening.**

**Consequence for THIS design, stated plainly:** an exit condition on the shares is **the only de-risking rail being built on a sleeve with an effective sample size of one.** That argues for the profit-keyed leg being **live and unconditional**, not gated behind a thesis-break confirmation that BRENT has measured to fire five weeks late.

⛔ **SCOPE FENCE (commission requirement #3), honoured:** this document is **independent of the `USO Oct-16 135C` pair** — the sell-one is ruled/unfilled and the second contract's disposition is BRENT's and Will's. ⛔ **Do NOT couple the legs.** Constructed *aware* of the whole sleeve, **coupled to none of it.**

---

## 6. THE STRUCTURE — slots, not levels

> ⛔ Every `⟨SLOT⟩` below is filled **on Monday's live tape**, from a live chain/quote pull and the live book. **A slot filled from any dated surface is a defect, not a shortcut.**

### LEG A — PROFIT-KEYED (PRIMARY). Ratcheting, not a fixed target.
| Field | Form required | Filled from |
|---|---|---|
| **A1 · Arm level** | Gain **≥ ⟨A1⟩%** over basis $121.88 — the point at which the gain is worth protecting at all. Below it, no ratchet exists and the position simply runs. | live mark |
| **A2 · Give-back trigger** | Once armed, exit on a **retrace of ⟨A2⟩%** from the **highest CLOSE achieved since arming** (never from an intraday high — `[[finding_ohlc_verify_before_session_claims]]`, BRENT's own twice-made error in this exact metric class) | live mark + close series |
| **A3 · Partial or whole** | **⟨A3⟩** shares of 35 on first fire. **Recommend a partial** — 35 shares is divisible, and a partial is the shape that survives being wrong about the ratchet width. | construction call |
| **A4 · Re-arm** | Does the ratchet **re-arm** at a higher high after a partial? **⟨A4⟩** — must be answered explicitly, because an un-re-armed ratchet silently becomes a one-shot target. | construction call |

**⭐ A2 IS THE ONLY REAL PARAMETER IN THIS DOCUMENT, AND IT MUST BE BASE-RATED BEFORE IT IS NAMED.** Its width must exceed USO's ordinary retrace noise or it fires on tape that means nothing — **the same failure mode BRENT's B-1 base rate exposed, in a different instrument.** ⛔ **I will not name A2 tonight and I would not name it Monday off a chart either.** **Required before A2 is proposed:** the distribution of USO peak-to-trough close-basis retraces within the current regime, stated with its **bar count** (`RISK_RULES` #19). That is a measurement I can run at build; **it is not a number I can assert.**

### LEG B — THESIS-BREAK (BACKSTOP). Named, and honestly labelled as late.
| Field | Form required | Owner |
|---|---|---|
| **B1 · Instrument** | **⟨SLOT⟩ — OPEN.** ⛔ **NOT B-1** (refuted as a trigger). ⛔ **NOT B-2 by default** (unmeasured). | needs BRENT |
| **B2 · Level** | **⟨SLOT⟩** — **may not be named without a base rate** (`L21`/`L22`) | **BRENT's lane, not TERRY's** |
| **B3 · Persistence** | If confirmation-keyed at all, in-sample false-positive-freedom needs **>25 td**. **Write the accepted latency on the card in days, in daylight.** | Will's call, on TERRY+BRENT input |
| **B4 · Join** | **OR** with Leg A. ⛔ **Never AND.** | binding |

### ⛔ THE CHOICE THAT MUST BE MADE IN DAYLIGHT, NOT AT THE GAP
BRENT named it and it is not mine to resolve: **either accept gap risk on a confirmation-keyed backstop, OR pre-commit to acting on an announcement-class signal that BRENT's own rules call inadmissible as a throughput measurement.** **This is Will's call.** ⚠️ **Leg A materially reduces the cost of choosing "accept the gap risk"** — because the profit-keyed rail is already off the position by then in the states where it has run. **That is the argument for the ordering in §2, and it is the main thing this scaffold contributes.**

---

## 7. What Monday's build must produce, in order

1. **Live mark + live book** (`chain_fetch.py` / `snapshot.py`; **never** the FORGE mirror). Re-mark the +$307.30/+7.20% framing — it is 3 sessions stale.
2. **Base-rate A2** — USO close-basis retrace distribution in-regime, **with its bar count.**
3. **Fill A1/A2/A3/A4.** Propose; do not adopt.
4. **Packet BRENT for B1/B2** with the ask named precisely — *"an instrument that is not B-1, not un-base-rated B-2, and whose accepted latency you will state in trading days."* ⚠️ **Do not block on him** (commission requirement #2): Leg A stands alone as a proposal if Leg B is not ready, **and under §2 it is the primary rail anyway.**
5. **→ Will [Approve].** Levels ratified by Will; PROME registers the ratification row.

---

## 8. Why not / counter-case

- **The strongest argument against this whole exercise:** the leg is **paid ~+3 pp/month** to be held (§4), and any exit rule gives some of that up. ⇒ **that is exactly why Leg A ratchets instead of targeting** — but it is a real cost and it should be stated to Will, not hidden.
- **The second:** a ratchet on a `N_eff = 1` sleeve can whipsaw out of the sleeve's only long right before the move that justified it — **which is precisely what B-1 was measured to do (§3).** A2's base rate is the *only* defence against reproducing that failure in a different instrument, which is why §6 refuses to name it un-based.
- **The third:** 35 shares is a small line. **An exit rule that costs more attention than the position is worth is a bad trade in itself** — the rule must be mechanical enough to execute without a session, or it joins the four-times-specified-zero-times-executed class (`RISK_RULES` #16 corollary: **count the executions, not the specifications**).

---

**Status: SCAFFOLD. `$0` at risk. Nothing proposed to Will yet — the levels are missing by design and the proposal is not ratifiable without them.**
**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**

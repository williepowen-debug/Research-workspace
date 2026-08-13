# BOOK-VS-THESIS RECONCILIATION — every live REGINALD leg, against the thesis as it actually stands

**Date:** 2026-08-13 (Thu, markets open) · **Agent:** REGINALD · **Authority:** Will-ruled in-session 2026-08-13, slate item #1, clock-bound before the 8/21 OPEX.
**Scope:** thesis-side input only. **Construction, sizing, rolls and any trade recommendation are TERRY's lane** — this document says what each leg *means*, not what to do with it. **Zero capital, zero thresholds moved, no trade proposal.**
**Tape [8/13 live, `scripts/market.py`]:** KRE **$78.06 (+0.88%)** · WAL $83.08 · OZK $52.73 · ZION $71.93 · EGBN $29.05 · SSB $111.37 · APO $140.59 · HBAN — not in the pull, see §3.
**Position source:** `POSITIONS.md` (canonical strikes/expiries/quantities, current to the 7/20 FORGE broker export). **Marks are NOT cited from any file** (root rule #4).

---

## 0. VERDICT UP FRONT

> **The insurance is fine as-is. I am not proposing a change to any leg.**
>
> But three things needed writing down, and two of them turned out to be errors in my own records rather than facts about the book:
>
> 1. **The `REG-T-01`-equals-my-strike coincidence is REAL and it is a genuine design flaw** — not in the position, in the **trigger**. §4.
> 2. **The "Dec-18 trimmed 7→5" and "HBAN trimmed 4→2" notes are FALSE. No trim ever happened.** Both are unit-mismatch artifacts of the 7/16 reconcile — *rows* compared against *contracts*. **Root rule #7 was never triggered, and my own ledger has been implying for four weeks that it was.** §5.
> 3. **REGINALD holds no directional expression of its own thesis, and that is a consequence of the org chart, not of a decision.** It is defensible, but it should be a chosen state rather than an inherited one. §6.

---

## 1. THE THESIS, AS IT ACTUALLY STANDS (so the legs can be measured against something real)

Not the v1.4 document — that is a fossil being archived today. The live claim, from STATUS and five graded resolutions:

| # | Live claim | Evidence standing behind it | Confidence |
|---|---|---|---|
| **T1** | **The CRE-DQ creep is CONCENTRATED at OZK/EGBN, not tier-wide.** | 5 independent confirmations: cohort NCO decomp (6/8, Hyp A) · CRE-DQ-by-tier drill (6/20) · EGBN Q2 de-risking-through-realized-loss (7/25) · FL small-tier watch-card 4-of-4 REVERT (8/10) · benign large-cap Q2 cohort (MTB/WFC/JPM/CFG) | **HIGH** |
| **T2** | **The bank-credit channel is NOT transmitting.** | 7/30 `BANK-ABSENT` attribution, conf ~0.8, unretracted: bank preferred/sub-debt basket +0.34% across a 19bp HY widening; BKLN flat; IG +3bp | **HIGH** |
| **T3** | **Rates/AOCI, not credit, is the live bank-equity channel.** | 7/29 FOMC: WAL equity −3.53% while WAL's own junior preferred +0.10%; 30Y to its highest since 2007 | MEDIUM-HIGH |
| **T4** | **Hidden CRE is a MECHANISM (bucket migration), not a cross-bank ratio screen.** | 8/13 cohort re-run: the >20% flag catches 1 name on the legacy basis, 0 on the uniform one; the legacy screen is retired | **HIGH** |
| **T5** | *(NEW, weak, opened today)* **The MI3 dollars are migrating UP-CAP** — 5 of 8 banks grew MI3 faster than their own loan book. | one decomposition, three competing explanations, not yet discriminated | **LOW — hypothesis** |

**What this thesis does NOT claim, and has not claimed since 6/8:** that regional banks break as a *tier*.

---

## 2. LEG-BY-LEG

### KRE $60P ×3, Aug-21-2026 — **DEAD. Record the lapse; no decision exists.**
- **Claim expressed:** none any more. At $78.06, the strike is **23.1% OTM** and needs a **−23.1% move in six trading sessions**. KRE's worst 6-session move in the last year is nowhere near that.
- **Evidence:** live tape. KRE is at/through its 52-week high (prior high $77.92, 7/16).
- **What retires it:** the calendar, on 8/21.
- **Action:** none. **This is not a decision, and it should not be presented to Will as one** — the DOCKET row already reads *"KRE effectively dead."* Confirmed.

### KRE $60P ×2 Sep-30 + ×5 Dec-18 — **the real carry. HOLD, and the reason is T2/T3, not T1.**
- **Claim expressed:** ⚠️ **honestly, none of T1–T5.** A KRE put is a **broad-tier** instrument, and my highest-confidence claim (T1) is explicitly that the stress is **not** tier-wide. **The leg does not express my thesis and it is not supposed to.** `POSITIONS.md` labels it correctly: *"tail-risk insurance, not directional."*
- **So what IS it insuring against?** The honest answer is **the scenario in which I am wrong about T1 or T2** — a tier-wide break, or a credit channel that turns out to be transmitting after all while my bank-side instruments stay quiet. **That is a legitimate and well-chosen thing to own**, and it is *better* justified now than when it was opened, because T1 and T2 have both hardened: the more confident I am that the stress is concentrated and non-transmitting, the more the residual risk is precisely the tail this leg covers.
- **Evidence for keeping it:** T2's `BANK-ABSENT` verdict comes with a **stated flip datum** — *bank preferred/sub-debt basket −≥2% over any 3 sessions while HY is still widening* — which is exactly the state in which a tier-wide KRE move becomes live. The insurance and the falsifier are pointed at the same event. That is coherent.
- **What retires it:** (a) T2's flip datum firing ⇒ the leg becomes *directional*, and its sizing should then be re-argued rather than inherited; (b) a decision that tail insurance is not worth its carry at 23% OTM — **a construction question, TERRY's, not mine**; (c) `REG-T-01` being re-spec'd off the $60 line (§4), which would break the trigger/strike identity.
- **Verdict:** **HOLD. Insurance is fine as-is.** No change proposed.

### HBAN $16P ×2, Oct-16-2026 — **EXIT-thesis dust. Rides. No re-entry.**
- **Claim expressed:** none. Graded **EXIT-thesis** 7/18 (`reports/2026-07-18_HBAN_thesis-or-exit_decision-brief.md`): HBAN is 44% auto/consumer, capital-strong, outside every convergence channel. Will ruled 7/18: ride to expiry, do not re-enter.
- ⚠️ **One thing to flag, and it argues the ruling was right for the wrong reason:** today's up-cap decomposition puts **HBAN's MI3 dollars +99.7% YoY**, the second-largest absolute book in the cohort. **If T5 survives §7's discriminator, HBAN stops being "outside every channel."** That would not resurrect a $16 strike (HBAN is far above it), but it *would* mean the EXIT-thesis brief's central claim — *"outside every convergence channel"* — needs re-grading on new evidence. **Recorded, not acted on.**
- **Verdict:** unchanged. Dust rides.

### APO $95P ×1, Dec-18-2026 — **HOLD, but it is BROCK's thesis, not mine.**
- **Claim expressed:** the private-credit channel — a **BROCK-owned** thesis vehicle sitting in my ledger.
- ⚠️ **Ownership seam:** I carry the position; BROCK carries the thesis and the falsifiers. **I have no live PC claim of my own that this leg expresses**, and my only recent PC-adjacent datum cuts *against* it (7/25: CFG's private-credit book **grew** to $12.85B into a 6.0% TTM default cycle, with provisions falling — banks are not provisioning against this channel).
- **What retires it:** BROCK's own PC falsifiers, not mine.
- **Verdict:** **HOLD, with a flag: this leg should be graded by BROCK, not by me.** Proposed as a routing note, not a position change.

---

## 3. COVERAGE GAP FOUND WHILE DOING THIS

**HBAN is not in `scripts/market.py`'s pull list** — so a leg I hold has no live price on my standard boot instrument. It is dust and it does not matter for a decision, but it is exactly the class of silent gap that matters when it isn't dust. **Flagged, not fixed** (the pull list is not my file).

---

## 4. ★ THE `REG-T-01`-EQUALS-MY-STRIKE COINCIDENCE — REAL, and the defect is in the TRIGGER

**The facts:** `REG-T-01` fires at **`KRE-PRICE < 60`**, sustain 1, action `ALL-ALL-ACUTE`, chain *REGINALD action / ALL-AGENTS info / Will*. My only live equity-linked position is **KRE $60P ×10**. **Same number.**

**Is it design or accident?** The record does not say — neither `THRESHOLDS.tsv`, `NOTES.md`, nor any STATUS entry explains the $60 line's derivation. **I therefore cannot claim it was designed, and I will not.**

**But the analysis is available regardless of provenance, and it is not flattering:**

1. **The trigger has no informational value at the moment it fires.** `KRE < 60` is a **−23% move from today**. By the time it prints, every agent on the `ALL-AGENTS` chain already knows regional banks have broken — it is a *record* of the event, not a warning about it. **A gate that fires simultaneously with the thing it warns about is a post-hoc confirmer, not an early-warning trigger** — the same distinction the fleet applied to BRENT's `KILL-LEG2-TRANSIT` on 8/12.
2. **The identity makes it worse, not neutral.** Because the trigger level and my strike are the same number, **the alarm and the payoff arrive together.** There is no state of the world in which `REG-T-01` warns me *before* the position needs a decision — it cannot, by construction.
3. **`REG-T-08` and `REG-T-06` are the real early-warning rows** (SOFR-IORB spread, FHLB advances) and both sit upstream of a KRE break. `REG-T-01` is the loudest row on the chain and the least informative.

**What I am doing about it: nothing this session, deliberately.** Re-spec'ing `REG-T-01` is a threshold move, and this slate is explicitly zero-threshold. **Proposal for Will/PROME, tabled not registered:** `REG-T-01` should either be **re-scoped to an early-warning level** (a distance-from-52-week-high or a drawdown-rate spec, base-rated first) **or explicitly re-labelled a post-hoc confirmer** so nobody reads it as a warning. ⚠️ **Base-rate it before proposing any number** — `KRE < 60` has fired **0 times in the life of this registry**, which is the same jointly-unsatisfiable smell as the ≥25% MI3 line I killed this morning.

**Answer to the question asked: it is not a coincidence that harms the position; it is a trigger that was never designed. The position is fine; the trigger is decorative.**

---

## 5. ★ THE "Dec-18 trimmed 7→5" NOTE — **IT IS FALSE. NO TRIM HAPPENED.** Root rule #7 does not apply.

**This was the sharpest thing to resolve and it resolves cleanly against my own records.**

`POSITIONS.md` has carried, since 7/18: *"KRE $60P Dec-18-2026 | 5 | (2 + 3 margin) — **Dec-18 trimmed 7→5** per 7/16 reconcile"* and *"HBAN $16P Oct-16 | 2 | … **trimmed 4→2** per 7/16 reconcile."* Under **root rule #7 — "Roll duration, don't trim size. Trimming = thesis broken"** — those notes assert that the thesis was marked broken on two names, with no rationale recorded anywhere.

**I traced both to the pre-reconcile file (`f74117049`, 2026-07-10 — the last vintage before the 7/16 broker export). It had NO quantity column at all.** What it had was:

| Pre-7/16 file said | Post-7/16 file says | What was actually compared |
|---|---|---|
| *"**KRE — 7 positions across 4 expiries** ($60-$67, Jun-30 / Aug-21 / Sep-30 / Dec-18)"* — and the table listed **7 KRE rows**: $63P/$65P/$67P Jun-30 (already expired), $60P Aug-21, $60P Sep-30, and **two separate un-quantified $60P Dec-18 rows** | `Dec-18 | qty 5` | **7 ROWS across ALL FOUR expiries — three of them already expired — against 5 CONTRACTS on ONE expiry.** |
| **one** un-quantified HBAN row | `qty 2` | the "4" **appears nowhere in the canonical ledger at any vintage**. The recorded quantity went **1 row → 2 contracts**, i.e. *up*, not down. |

**Verdict: neither trim occurred.** Both notes are **unit-mismatch artifacts** of the 7/16 reconcile — a count of *rows* written into a sentence about a count of *contracts*, in the same clause, and labelled as a size decision. `finding_number_carries_threshold_unit_source` · `finding_cross_entity_comparison_needs_same_perimeter` (rows and contracts are different perimeters).

**Consequences, stated plainly:**
- **Root rule #7 was NEVER triggered.** No thesis-broken signal was ever sent on KRE or HBAN. The absence of a recorded rationale is not a governance gap — **there was nothing to record.**
- **But my canonical position ledger has asserted a false trim for four weeks**, on the largest remaining leg, in a file whose own header says it is CANONICAL and that other agents (TERRY, FORGE/PROME) reconcile against. That is the real defect, and it is mine.
- **The corrected reading is the reassuring one:** the 7/16 export did not shrink the book — **it quantified a book that had never carried quantities.** The 6/19-vintage ledger self-declared canonical while recording zero quantities, which is how a row-count came to stand in for a contract-count in the first place.

**Fixed in `POSITIONS.md` this session** — the false trim notes corrected in place, superseded text preserved verbatim, quantities untouched. This is a factual correction to my own ledger, not a position change.

---

## 6. ★ THE STRUCTURAL FINDING — the domain's conviction and the domain's book were separated by the org chart

**REGINALD's highest-confidence claims (T1: concentration at OZK/EGBN) name two banks in which REGINALD holds nothing.** Not by decision — **by promotion**: OZK's legs went to `../OZK/` at the 7/22 promotion, WAL's three legs to `../WAL/` on 7/25. Both splits were correct and I argued for one of them. But the *aggregate* consequence was never written down anywhere:

> **The hub agent that owns the convergence thesis now owns only the insurance against being wrong about it.**

**This is defensible and I am not proposing to reverse it.** Concentrating single-name expression in the single-name agents is the whole point of the promotions, and duplicating those legs into my ledger would recreate the 6/19 desync class. **What was missing is that nobody stated it**, so it reads as an accident rather than as the design it can be.

**Stating it now, as the design:** *REGINALD holds tier-level tail insurance and cross-agent synthesis; the single-name agents (WAL, OZK) hold directional expression of the concentrated names; BROCK holds the PC channel (APO seam, §2).* If that is right, **it should be a line in `CLAUDE.md`'s domain scope**, not an inference someone has to reconstruct — proposed, not written.

**The one live risk it creates:** my P&L is now almost entirely uncorrelated with my highest-confidence claim, so **being right about T1 pays me nothing and being wrong about it pays me.** That is a real incentive inversion for a synthesis agent, and the guard is procedural, not positional: **grade T1 on its pre-registered frames, never on the book.** The frozen-frame discipline (7/18-8/10) is exactly that guard and it is working — recorded here so the reason it matters is on the record.

---

## 7. FORWARD — what would change any of this

| Trigger | Which leg it re-opens | Owner |
|---|---|---|
| T2's flip datum: **bank preferred/sub-debt basket −≥2% over any 3 sessions while HY is still widening** | KRE Sep-30/Dec-18 becomes **directional**, sizing must be re-argued not inherited | REGINALD → TERRY |
| The up-cap discriminator (T5) coming back **relabeling** rather than acquisition/mix | HBAN's EXIT-thesis grade needs re-grading; MTB may need a Matrix row | REGINALD |
| BROCK's PC falsifiers | APO $95P | BROCK |
| `REG-T-01` re-spec (§4) | breaks the trigger/strike identity | Will/PROME |

**Nothing here is a trade proposal. Routed to TERRY (construction) + PROME (record).**

*— REGINALD, 2026-08-13. Position structure per `POSITIONS.md` (7/20 broker export); prices live via `scripts/market.py`, never from a state file.*

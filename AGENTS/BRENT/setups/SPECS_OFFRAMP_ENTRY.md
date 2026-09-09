# BRENT — off-ramp entry and tranche rules

Reconciled 2026-09-08 under Will’s approved BRENT cleanup. Supersedes: the corresponding rule containers in TRADE.md; no capital authority, levels or discretionary permission added. Binding excerpts below are preserved verbatim; dated examples retain their original dates. Full provenance and superseded wording: [before-image](../archive/2026-09-08_cleanup/TRADE.md). [Inventory](../workbook/TRADE_OBLIGATIONS.md).

Read this whole file BEFORE proposing the off-ramp or changing any entry leg, including when an initially unrelated session becomes trade-relevant. Also read [SPECS_TRADE_RULES.md](SPECS_TRADE_RULES.md) before a proposal so the exit obligations are known before entry. No current deployment is asserted.

## BE-01 — Hardened trigger

**Trigger (HARDENED — operational, not rhetorical; LESSONS #18). ⚑ RE-SPEC v2 RATIFIED BY WILL 2026-07-29 — per-leg verification windows, closing LESSONS #21(b).** Fires on a Muscat/Article-5-class breakthrough with **(i)** named-official + signature/sovereign-action class **AND (ii)** the two-stage verification below; **OR** transit normalization >50% of pre-crisis sustained 5 sessions with no deal.


## BE-01b — Alternate no-deal trigger (UNRESOLVED)

**Alternate no-deal trigger:** the retained “>50% of pre-crisis sustained 5 sessions” branch has no independently repaired, live measurement path following the AIS/PortWatch retirements. It is UNRESOLVED, not a runnable shortcut around (i)/(T)/(C); BRENT must identify a valid instrument and resolve applicability before presenting it as met. No substitute series or threshold is registered by this cleanup.

## BE-02 — Day+2 admission limit

> ### 🔻 **BINDING DESIGN CONSTRAINT ON THIS GATE — THE DAY+2 LATENCY CEILING. Will-registered 2026-08-07.**
> **NO ENTRY LEG MAY REQUIRE DATA THAT RESOLVES LATER THAN DAY+2.** A leg resolving day+3 or later is **structurally disqualified from ENTRY** — however good a discriminator it is — and belongs in the **kill-test / tranche-2 / continuation** role.
> **⛔ THIS IS AN ADMISSION TEST FOR ANY FUTURE LEG. Apply it BEFORE drafting, not after** (same discipline as `lessons_check --concept`). It is why the transit leg cannot come back to entry, and it would have blocked v1's days-to-weeks basket and DEPLOY GATE v2's zero-minute window at draft time.
> **★ LATENCY IS A CLIFF, NOT A SLOPE:** Leg-C-gated entry (day+2) **+7.07%**; transit-gated entry (day+5) **−5.99%**. Brent fell **−6.6% in the three sessions between them** — the edge lives in a **~3-session window from ~day+2 to ~day+6**, so a slow gate does not degrade this trade, it **INVERTS** it.
> ⚠️ **Limits travel with it: n=1 profitable analogue, Apr-17 not re-runnable intraday, boundary read off one price path. A DESIGN CONSTRAINT, NOT A FITTED PARAMETER — moving day+2 requires base-rating across events, not a re-read of Jun-17.**
> **Full reasoning + the three-instance provenance → [`RULINGS.md#day2-latency-ceiling`](../RULINGS.md#day2-latency-ceiling).**


## BE-03 — Signature plus paired T/C entry

> ### **STAGE A = (i) signature/sovereign-action AND (T) tanker liveness AND (C) crude 2-day follow-through.**
> **⛔ THE TRANSIT LEG IS NO LONGER AN ENTRY CONDITION.** It moves to the **Stage-B KILL TEST** (below), which already duplicated it with a properly matched 10-trading-day window.
>


The preceding transit-to-retention sentence records the July 31 migration. That transit instrument was subsequently retired August 21; BH-06/BH-07 govern its present applicability. It is not a live executable kill test.

## BE-04 — T and C frozen definitions

| Leg | **FROZEN test** | Verdict logic |
|---|---|---|
| **T — tanker liveness** ⚑ **v6** | `T = max( \|STNG\|, \|FRO\|, \|DHT\| )`, **prior close → the live print at the ticket**, graded **ONCE, at or after 14:00 ET on day 0** *(Will-ruled 2026-08-05; v5's day-0 **close-to-close** basis is SUPERSEDED — it was unexecutable, see the ruling block below)* | **BLOCK iff `T ≤ 1.0%`.** Otherwise PASS. **SIGN IS DISCARDED, explicitly and by design (LESSONS #19).** **Threshold, 3-name composite and sign-discarding ALL UNCHANGED from v5 — only the MEASUREMENT MOMENT moved.** |
| **C — crude 2-day follow-through** | Cumulative **Brent front-month** return over the **TWO sessions AFTER day 0**, measured against the day-0 close | **BLOCK iff `≥ 0%`** (premium being re-bought = false dawn). PASS iff `< 0%`. |


## BE-05 — Measurement basis and its limits

> ### ⚖️ **BASIS RULED 2026-08-07 — THE `1.63%` vs `1.68%` SPLIT IS TWO INSTRUMENTS, NOT TWO ANSWERS. BOTH SURVIVE; BOTH GET A LABEL.** *(Raised by the Will-directed 8/6 commit review; resolved by RE-DERIVATION, not by picking.)*
> **RE-DERIVED FROM PRIMARY DAILY BARS 8/7** (yfinance STNG/FRO/DHT, 6/16 close → 6/17 close): **STNG −0.611% · FRO −1.446% · DHT −1.630%** ⇒ `T = max|·| =` **1.630% (DHT)**. **It reproduces to three decimals**, so the three surfaces carrying `1.63%` (`TRADE.md` analogue table · `LESSONS.md` #19 · `LESSONS_INDEX.tsv`) are **CORRECT and stay.**
> **⇒ `1.63%` = DAILY-CLOSE BASIS = the CALIBRATION anchor.** It is the figure the 1.0% threshold was set against and the figure LESSONS #19 teaches. **`1.68%` = 5-MINUTE-BAR LAST PRINT** of the same session — the last cell of the v6 intraday-feasibility column, where every other cell is also a 5m reading. **Swapping it to 1.63 would make that column internally inconsistent and is forbidden.**
> **⚠️ VERDICT-NEUTRAL — both pass `>1.0%`; nothing that was graded changes.** **The defect was never the 5bp; it was that a Will-ruled gate's anchor existed as two unlabelled numbers.** **No threshold moved. Labels added, both figures retained.** `[[finding_loadbearing_number_must_be_reproducible]]`
> ⚠️ **THE LIVE CONSEQUENCE, because the ruling would otherwise read as bookkeeping: v6 grades on a LIVE PRINT at the ticket — an intraday instrument — against a threshold calibrated on DAILY CLOSES. That is the same units mismatch flagged two lines above, and this ruling does NOT close it; it names it.** The 93.2% agreement figure is what bounds it, and it is the number to re-check if the gate ever fires.


## BE-06 — T1 one grade per session

> **🔻 T1 — ONE GRADE ONLY. Leg T is graded ONCE, at the ticket. A BLOCK STANDS FOR THE REMAINDER OF THE SESSION AND MAY NOT BE RE-POLLED.** ⛔ **This is FORCED BY MEASUREMENT, not offered as balance: re-evaluating every 5 min, 66.1% of sessions FLIP the verdict at least once (median 2, max 21; after 14:00 → 20.3%, median 0).** **Without T1 this is not a test — it is a coin an operator can re-flip until it lands.** *(TERRY `RISK_RULES #14` — a MOMENT property, not a STRUCTURE property — reappearing in a second gate.)*


## BE-07 — T2 close-basis veto of remainder

> **🔻 T2 — THE CLOSE-BASIS TEST STILL BINDS ON THE REMAINDER.** Leg T is **re-graded on the day-0 CLOSE**; if the **close-basis `T ≤ 1.0%`, TRANCHE 2 IS FORFEITED regardless of Leg C.** **The v5 test is not discarded — it is DEMOTED from gating tranche 1 to gating tranche 2, which is what caps the intraday false-pass at HALF the position rather than the whole.**


## BE-08 — Intraday evidence limits

> ⚠️ **LIMITS, CARRIED WITH THE RULING:** **(1) n = 1 analogue intraday** — 5m history starts **2026-05-11**, so **Jun-17 is testable and Apr-17 is NOT**; the anti-false-dawn cover is **ARGUED** intact (Apr-17 blocks on **(i)** and independently on **(C)**, neither touched) **but NOT MEASURED** intact. **(2) 14:00 IS NOT EMPIRICALLY SUPERIOR TO 15:00** — the false-pass spread (3.4% vs 8.5%) is **2 vs 5 sessions at n=59**, noise, and non-monotone. **14:00 was chosen for the WINDOW it leaves an [Approve]-gated trade, not for its base rate; every intraday grading time carries a 3–9% false-pass.** **(3)** Base rates are **unconditional** market behaviour, not conditional on de-escalation announcements. **(4)** The robust findings are the **oscillation** and the **units mismatch**; the exact grading time is not robust.


## BE-09 — Frozen boundaries and pairing

- **Binary and exhaustive by construction** — no dead band (that was the defect in the 7/30 three-case draft: `1%<|move|<3%` was unspecified and is the *most likely* outcome, 44.9% uncond. / 34.6% given Brent ≤−3%).
- **The 1.0% and 0% boundaries are CHOSEN, NOT FITTED.** Frozen constants — no percentile, no re-derivation from a rolling window (`[[finding_threshold_level_is_a_measurement_not_a_constant]]`). ⚠️ **Do not "improve" them on n=2.**
- **Leg T base rates** (3y to 2026-07-31, n=749): blocks **13.4%** unconditionally, **5.8%** given Brent ≤−3%, 9.4% given ≤−4%, 15.0% given ≤−5%. A narrow anti-false-positive filter, not a gate.
- **Leg C verified 2-for-2:** Apr-17 2026 **+8.96% ⇒ BLOCK** (correct — crude ran +19.7%, a short would have been destroyed) · Jun-17 2026 **−2.07% ⇒ PASS** (correct — a crude short won −9.7% by day 10). Robust: every threshold from **−2% to +8%** separates the two.
- **⚠️ WHY THEY SHIP TOGETHER AND MUST NEVER BE SPLIT:** Leg T passes **both** analogues (Apr-17 `T`=5.63%, Jun-17 `T`=1.63%), so **Leg T alone would have removed the only leg that blocked Apr-17.** Leg C is what blocks it. **Splitting this pair is a net loosening of a short-arming gate** — the same principle that forced the 7/29 kill test.


## BE-10 — Mandatory calibration caveat

> **⚠️ HONEST LIMITS — CARRIED FORWARD WITH THE RATIFICATION, PER THE RULING (do not drop these when citing the gate):**
> 1. **n = 2 analogues.** Both legs are calibrated on two events.
> 2. **🔴 THE SHARPEST LIMIT, AND IT MUST SURVIVE EVERY FUTURE EDIT OF THIS SPEC (Will-directed 2026-07-31 to carry verbatim into the live spec): this regime has produced ZERO genuine physical reopenings** (LESSONS #19: Jun-17 was 0-of-4 on physical legs). **"Real vs fake" is therefore UNCALIBRATED — Jun-17 is "the one that would have made money," which is NOT the same thing as "the one that was real." THIS SPEC IS OPTIMISED AGAINST A PROFITABLE TRADE, NOT A VERIFIED REOPENING.** Every threshold in Stage-A v5 (Leg T's 1.0%, Leg C's 0%, and the decision to move the transit leg out of entry) is fitted to a sample containing **no confirmed instance of the event the playbook exists to trade.** **Do not delete this paragraph to make the spec read cleanly.**
> 3. **The Leg-T base rates are unconditional market behaviour**, not conditional on de-escalation announcements. They say how often it blocks, **not whether it blocks the right days.**
> 4. **§0a is UNRESOLVED, NOT EXPLAINED:** the 7/30 analogue table's tanker figures do not reproduce and I still cannot say how they were produced. The **"blocked 2 of 2" tally stays RETIRED as UNVERIFIED** — do not re-cite it.


## BE-11 — First tranche

> **TRANCHE 1 — HALF the position on DAY 0**, once **(i) signature** and **(T) liveness** are satisfied. ⚑ **CORRECTED 2026-08-05:** ~~*(Both are observable on the announcement session — this is the leg that honours LESSONS #11.)*~~ ⛔ **THAT PARENTHETICAL IS WHAT CAUSED THE ZERO-WINDOW DEFECT — "OBSERVABLE" IS NOT "ACTIONABLE."** Under **Leg T v6** both are now **ACTIONABLE** on the announcement session: **(i)** is a same-session event and **(T)** is graded ONCE at/after **14:00 ET**, leaving a **120-minute** fill window. *This is still the leg that honours LESSONS #11 — but it honours it because the timing was FIXED, not because the original claim was true.*


## BE-12 — Second tranche

> **TRANCHE 2 — the REMAINDER on Leg C resolution** (2 sessions later), **only if Leg C PASSES** (cumulative Brent < 0%) **AND the day-0 CLOSE-basis Leg T also PASSES (`T > 1.0%`) — tightening T2, Will-ruled 2026-08-05.** **If EITHER blocks, tranche 2 is NOT added** — and the existing harvest rules (H1/H2/H3) govern tranche 1 from its own entry.


## BE-13 — Maximum loss

> **Fenced dollar caps UNCHANGED** (~$500 max-loss on the structure). **The strict "full size only after both legs resolve" default is RETIRED as a dated record.**


**Holding clock resolved in the existing record:** the old interim per-tranche clock at original TRADE line 580 is superseded by the announcement-anchored H1 at original lines 674–675. Both tranches exit by day+9 from the announcement; read BH-02. The prior inventory’s “unresolved” label was stale. This changes no ruling.

## BE-14 — Vehicle, tenor, strikes and execution window

**Vehicle / structure — ⚑ TENOR RE-SPECCED, WILL-RATIFIED 2026-07-30 (Option B):** **USO bear put spread** — NEVER outright puts (OVX 60+ = maximum vol-crush on the de-escalation day itself; LESSONS #15). **21–35 DTE** *(was **60–90 DTE** — retired 7/30)*; long ~5-10% OTM / short ~15% OTM; ~3:1 R:R; **defined risk ~$500 max-loss.** Execute within ~48h of the hardened trigger (LESSONS #15); strikes/premiums from a **live chain at fire** (`[[finding_option_marks_need_live_chain]]`).
> **Why the tenor moved:** the one qualifying historical move had a **9-session life** and had **fully round-tripped by day 20** (trough −8.1% at day 9 → −2.4% at day 15 → **+8.8% at day 17 → +13.1% at day 20**). **A 60-90 DTE structure held to expiry gives back the entire move.** ⚠️ **Cost accepted deliberately: 21-35 DTE carries more theta and more gamma risk.** That is the correct trade — the tenor mismatch cost more than theta will, and the harvest rule below now caps the holding period *inside* the tenor anyway.


## BE-15 — Proposal authority and interaction


**Interaction with the convex arm: mutually exclusive.** A hardened off-ramp IS the up-arm's disarm condition — it auto-disarms, this arms. The two are never live simultaneously.
**Authority:** pre-negotiated PROPOSAL — on trigger I pull a live chain and bring Will a one-line fill for fast **[Approve/No]**. NOT auto-fire. Rule #6 note: the announcement day is a violent RED day for oil; if the gap consumes most of the move at the open, prefer the first stabilization bounce for the fill rather than chasing the hole.

**The other down-tail (unchanged):** Brent **<$70 on confirmed DEMAND collapse** (recession) remains the only non-off-ramp short-revival. (Structural detail: THESIS SHORT PLAYBOOK.)


## BE-16 — Molecule scope of the premise

**Premise:** the $76→$92 move is ~100% reversible risk-premium — zero **CRUDE** barrels destroyed (v5.1 discriminator; ⚠️ **molecule-scoped 2026-07-30** — the qualifier is load-bearing here, because this playbook shorts **crude**: LNG has been in supply-loss since 3/24 and refined product since 7/27, and **neither of those losses is reversible by the off-ramp this playbook fires on**. A Hormuz de-escalation round-trips the crude premium; it does not restart Ras Laffan or un-shut Jazan. **Do not let product-side tightness argue you out of a crude short, and do not let a crude off-ramp argue you into shorting products.**). The Jun-17 MOU showed the shape: **−8%/wk on the announcement, curve flip, premium out before any barrel moves** (LESSONS #11/#16). From $92 the unwind target is ~**$75-78** (the structural-decoupling zone). Underneath, the flush setup is quietly rebuilding: rigs 452 → production lands Q4'26-Q1'27 (GS's de-escalation window), China imports −41.3% YoY, SPR exchange-returns due 2027.


The prices and zero-crude-loss claim in BE-16 are the dated premise at registration, not a newly verified September premise. Its molecule boundary remains binding; verify current losses before relying on the premise.

The interaction with the upside arm is conditional history: the upside arm is retired, so it is not currently armed. A hardened off-ramp cannot make both strategies live. Current decision authority remains a proposal to Will.

## Lesson reconciliation (2026-09-08)

L05/L22/L23/L25: use dated live instruments, actually run verification, name contracts and investigate request/identity failures; old examples above never certify current execution inputs. L11/L16/L18/L19: announcement entry, sign-blind liveness and physical retention have different roles; apply the approved paired T/C and the explicit retired-instrument limits. L15: structural 60–90 DTE and off-ramp 21–35 DTE remain distinct; holding-specific rulings take precedence. L21: no new threshold, re-arm, measurement substitute or timing relaxation is registered by this migration; joint and trigger-conditional testing is still required before a successor. L06/L08/L09/L10: no new crack, inventory, product-supplied or quota grade is made here. Those lessons remain applicable when their evidence is used; a crude premise does not prove product supply or actual OPEC delivery. No lesson is overridden by this cleanup.

L17: any spare-capacity claim reused in a proposal must be checked against physical deliverability; the dated OPEC references above do not certify current usable spare capacity.

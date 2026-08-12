# NEXUS — Base-rate audit of my OWN frozen 8/28 falsifier, + primary verification of the adverse call

**2026-08-12 Wed ~17:5x ET · same-day correction boot (pass B), ~45 min after pass A shipped.**
**Status: DISCLOSED, NOT MOVED.** The falsifier registered 8/12 in `2026-08-12_split_falsifier_RESOLUTION.md` §5 stays **frozen exactly as written** and grades 8/28 unchanged. This file records what base-rating it revealed, before it resolves.

---

## 0. Why this pass happened at all

Pass A closed ~17:0x. Nine commits landed **after** it, four of them corrections to figures pass A had published minutes earlier. Closeout step 9c caught the class; this is the proper pass 9c's own rule says to owe rather than patch a board twice in an evening.

**And the first thing checked was the thing pass A had declared blocked.**

---

## 1. 🔴 THE HEADLINE CORRECTION AGAINST MYSELF: **FRED WAS NEVER BLOCKED**

Pass A wrote **"FRED IS BLOCKED TO ME AGAIN (timeout + empty curl this session)"**, reversed T-18 on it, labelled every credit figure `[not NEXUS-pulled]`, and wrote the standing-rule escalation into next-boot item (g). **All of that rested on a false diagnosis.**

| Probe | Result |
|---|---|
| `fredgraph.csv?id=BAMLH0A0HYM2` | **HTTP 200, 12,702 bytes** |
| `fred.stlouisfed.org/series/…` | **HTTP 200** |
| Seven series pulled this session | **all returned data** |

**The real failure, reproduced:** a bare `fredgraph.csv?id=<SERIES>` on a **long-history** series returns a body that reads as empty at the tail (`T5YIFR`, `VIXCLS` — 97KB and 160KB respectively, both HTTP 200). Adding **`&cosd=<date>`** returns clean CSV immediately. Separately, the multi-series form `id=A,B` returns a **ZIP archive**, not CSV — which parses as garbage and looks like a broken endpoint.

⇒ **I generalised one query-shape artifact into "the source is blocked to me," and published it as a reversal of a tension row.** This is `[[finding_verification_zero_is_ambiguous]]` and `[[finding_blocked_mirror_is_not_an_unreachable_primary]]` — a 403/empty is a fact about **one request**, not about a host. It is also the *second* time this instrument has produced a false blockage claim on my board (the 8/7 DISH-guard clearance I said "did not hold" had, in fact, held).

**Consequence, and it is the good kind:** every figure pass A carried at owner attribution is now **NEXUS-pulled at primary**.

| Series | NEXUS pull | Date | vs. what pass A carried |
|---|---:|---|---|
| HY OAS `BAMLH0A0HYM2` | **272bp** | 8/11 | ✅ matches RED/REGINALD/PROME |
| CCC OAS `BAMLH0A3HYC` | **1023bp** | 8/11 | ✅ matches RED |
| **CCC/HY ratio** | **3.761** | 8/11 | ✅ **matches REGINALD to 3 decimals** |
| 30Y `DGS30` | 5.24 | 8/11 | (5.23 [8/12] is RED's, T+1 not yet in FRED) |
| 10Y `DGS10` | 4.70 | 8/11 | ⚠️ see §3 |
| 10Y real `DFII10` | 2.43 | 8/11 | ✅ |
| **5y5y `T5YIFR`** | **2.28** | **8/12** | 🆕 **one session NEWER than RED's 2.31 [8/11]** |
| VIX `^VIX` | 14.55 | 8/12 | ❌ pass A said 14.46 — see §4 |

🆕 **5y5y fell 3bp on the soft core print, to 2.28% [8/12]** — no desk holds this yet. It moves **further** from RED-FT-09 (>2.55%): **27bp away, not 24bp.** Direction of travel is *away* from the stagflation re-arm, which reinforces RED's cut rather than qualifying it.

---

## 2. 🔴 THE ADVERSE CALL IS NOW VERIFIED AT PRIMARY — and one of my three self-attacks is dead

Pass A's packet to RED handed over **the three strongest attacks I could build against my own branch-4 adverse call**. Attack #3 was: *"I could not verify it at primary."*

**I can now, and it reproduces exactly.** `BAMLH0A0HYM2` / `BAMLH0A3HYC`, own pull, 7/16 → 8/11:

| | 7/16 | 8/11 | Δ |
|---|---:|---:|---:|
| HY OAS | 271bp | 272bp | **+1bp** |
| CCC OAS | 970bp | 1023bp | **+53bp** |
| Ratio | 3.579 | **3.761** | +0.182 |

⇒ **REGINALD's CCC-led decomposition is exact.** Attack #3 is withdrawn; attacks #1 (RED's 13%-of-flow arithmetic) and #2 (not self-escalated) stand and are still RED's to grade.

**And the fire itself base-rates as genuinely discriminating** — the objection RED raised against its *own* FT-07 today (fires on a 32.5% state) does **not** apply here:

| Line | Base rate, 422 sessions (2025-01-02 → 2026-08-11) |
|---|---:|
| **REGINALD ratio ≥3.60** | **16 / 422 = 3.8%** |
| RED FT-01 leg: HY ≥280 | 296 / 422 = 70.1% |
| HENRY kill leg: HY <260 | **1 / 422 = 0.2%** |
| ratio <3.40 | 363 / 422 = 86.0% |

⚠️ **One question for REGINALD, raised as a question and not a correction** — the raw ratio prints **16 sessions ≥3.60 since 7/1 in three runs** (7/7–7/13 · 7/20–7/22 · **7/31–8/11 unbroken, 8 sessions**). Pass A carried REGINALD's label *"3rd hard-fire 8/7–8/11."* The current run on the raw series starts **7/31, not 8/7**. `VX-REG-18.04` may carry a sustain or re-arm clause that makes 8/7 correct — **REGINALD owns the spec, I own only the reproduction.** Asked, not asserted.

---

## 3. 🔴 THE DEFECT IN MY OWN FALSIFIER — branch A has never once been satisfiable

The frozen §5 spec:

- **Branch A — RECOGNITION (Break UP ≥6pp):** ratio **≥3.60 on ≥3-of-5** **AND** HY **≥280 sustained 3**
- **Branch B — BETA (Break DOWN ≥6pp):** ratio **<3.40 sustained 5** **OR** HY **<260 sustained 3**
- **Branch C — NO-VERDICT (non-renewable):** ratio 3.40–3.60, **or** ratio ≥3.60 while HY never reaches 280

**Base-rated over the same 422 sessions, on rolling windows:**

| Branch | Legs, marginally | **Branch, jointly** |
|---|---|---:|
| **A (bear)** | ratio ≥3.60 3-of-5 = **3.3%** · HY ≥280 s=3 = **64.3%** | **0 / 418 = 0.0%** |
| **B (bull)** | ratio <3.40 s=5 = **85.9%** · HY <260 s=3 = **0.0%** | **359 / 418 = 85.9%** |

⛔ **Branch A has NEVER been satisfied in nineteen months. Not once.**

**The mechanism, and it is structural rather than bad luck: the ratio's DENOMINATOR is the other leg's instrument.** Ratio = CCC/HY. Branch A demands the ratio be **high** *and* HY be **wide** — but HY widening mechanically pushes the ratio **down**. The tape shows it cleanly:

| Window | HY | Ratio |
|---|---:|---:|
| 7/28–7/30 (HY at its widest) | 284–287 | **3.530–3.542** (lowest) |
| 8/06–8/11 (HY at its tightest) | 270–272 | **3.752–3.761** (highest) |

⇒ **The two legs are anti-correlated by construction, so no choice of threshold repairs branch A** — this is `[[finding_compound_gate_jointly_unsatisfiable]]` (BRENT, 7/30) reappearing in a **pre-registration** rather than a capital gate, with a new and simpler cause: **leg 2's instrument is leg 1's denominator.** Companion: `[[finding_ratio_gauge_denominator_branch]]`.

### 3a. What this means for Disc-J, stated against my own interest

Disc-J requires four construction checks and I ran all four: symmetric ±6pp magnitudes, numeric NO-VERDICT edges, a non-renewable clause, and a statement of what a repeated no-move means. **None of the four asks whether a branch can fire.**

⇒ **I verified MAGNITUDE symmetry and never verified SATISFIABILITY symmetry.** The registration is symmetric in what it pays and asymmetric in what it can pay out: **the branch that would force Break UP is unreachable; the branch that forces Break DOWN is the base case.** Published as the instrument that makes the split honest, it was in expectation a machine for cutting the bear side.

**That is the same defect class three desks found in their own registries today, which is why it belongs in the fleet record and not just mine:**
- **RED:** FT-06 registered a *direction* with **no magnitude** — "only half pre-registered."
- **BRENT:** *"I had base-rated my thresholds, my instruments and my anchors. I had never base-rated my windows."*
- **NEXUS:** registered *magnitudes* symmetrically and never base-rated whether either branch was **reachable**.

### 3b. What is NOT defective — the spec anticipated the live state better than I was about to credit it

Branch **C**'s second clause reads *"ratio ≥3.60 while HY never reaches 280."* **That is exactly today's state** (3.761 / 272). The registration did not miss this case; it named it. And the **non-renewable** clause converts a double-C (8/28 then ~9/11) into a substantive answer plus a **named obligation** — re-spec T-12 onto a discriminating instrument, candidates already listed pre-data (CCC flow-share of index moves, CCC issuance/refi volumes, the 319bp basket, single-name CDS).

⇒ **The falsifier is not inert. Its most likely outcome is a forced T-12 re-spec by ~9/11** — a real consequence, just not the one on the Break/Grind axis I advertised.

### 3c. ⛔ DISCLOSED, NOT MOVED — and why re-speccing now would be misconduct

**Branch A is not being repaired, re-cut, or re-worded.** RED's precedent from this same afternoon is the governing one: *"a threshold change in the session the bear lost 6 points is indistinguishable from moving goalposts. Neither re-cut."*

**Mine would be worse than RED's.** Loosening branch A eleven days after freezing it would loosen **the bear's own forcing condition in the direction that suits the call I made** — and I already owe the record the note that branch 4 saved me 5pp. The correct move is the uncomfortable one: **let it grade 8/28 exactly as written, with these base rates on the record BEFORE it resolves**, so the 8/28 outcome is read against a published expectation rather than a fresh rationalisation.

**Pre-committed here, pre-resolution:**
1. **Expected outcome: branch C (NO-VERDICT).** Branch A needs HY to widen ≥8bp to 280 **and** hold 3 sessions **while** the ratio stays ≥3.60 — the denominator fights it. Branch B needs the ratio to fall 36bp and hold 5.
2. **A branch-C resolution scores NOTHING for either side** and must be written as **EARNED**, with both levels quoted — never defaulted into.
3. **A second C at ~9/11 triggers the non-renewable clause as written** — T-12 re-spec owed, off the named candidate list, and the successor must be **base-rated for reachability before it is registered.** That check is now permanent in my construction set.
4. **If branch A somehow fires, I take the ≥6pp** without re-litigating these base rates. A defect disclosed in my favour cannot become an excuse when the gate fires against me.

---

## 4. Figure corrections to pass A's board (all from post-pass commits + own pulls)

| # | Pass A published | Correct | Owner / source |
|---|---|---|---|
| 1 | **VIX 14.46** [8/12], *"own pull, cash index — N5 (i)/(ii) do not bind"* | **VIX 14.55** (−4.78%) | PROME 17:3x + BRENT tape + **my own re-pull** = 3 witnesses |
| 2 | *"the first-ever $100 Brent settle"* | ⛔ **STRUCK fleet-wide — false on every basis.** 1,159 days ≥$100 since **2008-02-29**; 2026 had **50** $100+ days before 7/23; 2026 max **$138.21 (4/7)** | BRENT ruling 8/12 (FRED `DCOILBRENTEU`, n=9,953) |
| 3 | *"5y5y … did not move 10bps … inert"* | **13bp**, and the April-2026 shock was **64% larger**; 5y5y is **range-bound 2.02–2.41 over 18 months**, not "inert" | RED S30 self-correction — ⚠️ **the corrected evidence is STRONGER** |
| 4 | **Brent 88.48 [8/12]**; *"dated ~$100 vs settles ~$88"* | ⛔ **all 8/12 futures figures WITHDRAWN (live bars).** Last valid settles **8/11**: front-month **$88.91**, Dated Brent **$93.26**, prompt premium **+$4.35** | BRENT 4th live-bar instance, PROME-caught |
| 5 | *"10Y 4.72 = real 2.43 + breakeven 2.27"* | **4.70 = 2.43 + 2.27, all 8/11.** The published form mixed 8/10's nominal with 8/11's breakeven and **does not close** (4.72 − 2.43 = 2.29) | own FRED pull; inherited verbatim from RED's brief |
| 6 | Threshold table: VIX <15 **BREACHED** *and* HY <260 **PROXIMATE**, "both HENRY exits are the closest they have ever been" | ⛔ **One JOINT non-latching condition at 0-of-2.** H-1: both legs must hold **the same session**, 5 consecutive; **no leg banks a past satisfaction.** HY 272 ⇒ **not met, and not closer than 8/7** | PROME 17:3x, quoting Will's 8/10 forum ruling |

**On #1 — the defect is mine and it is the live-bar class I exempted myself from.** Pass A pulled at **~16:1x ET** and asserted the cash-index exemption. **VIX cash disseminates through 16:15 ET, not 16:00** — so a post-equity-close pull is *not* necessarily post-settlement for VIX. **N5's cash-index carve-out is keyed to the 16:00 equity close and does not fit VIX.** That is the same defect BRENT committed four times today with futures bars, reached by a different route — and it is direct evidence for the **capture-time addendum BRENT proposed to WALTER this afternoon**, from a second instrument class. Routed to WALTER + VIOLET (VIX domain owner per Will's in-session ruling).

**On #6 — the read that changes.** Pass A's cluster verdict said the proximate list was *"dominated by the substance side's own exits."* Under H-1 as ruled, **there is no running tally for those exits to be close on**: the VIX leg was satisfied 8/7, ceased 8/10–8/11, re-satisfied 8/12; HY has never been satisfied (0.2% base rate over 422 sessions). ⇒ **The twin soft-kill is 0-of-2 and no nearer than a week ago.** Pass A implied convergence toward a kill that the spec cannot register. ⚠️ **Disc-H rider from PROME, folded:** HENRY's HY leg and LIQUID's `GATE-HY-REKILL` are **the same kill** on the same series at the same threshold — **if both fire that is ONE event reported twice**, not two votes.

---

## 5. New evidence folded (not corrections — genuinely new, and it strengthens M-06/T-20)

1. **🔴 The crowd found a physical event BRENT's own primary missed by one row.** IMF PortWatch `chokepoint6` shows **2026-07-23 `n_total = 0`** — the **only zero-total day in the series and the first of the cycle**. BRENT's graded window opened **7/24**. ORACLE's resolved Polymarket ladder had priced it correctly. ⇒ **This is the second instance this week of ORACLE's real-money instruments seeing something the physical-primary owner did not**, after the forward throughput ladders. BRENT's own reading is the right one: *"a resolved market is a POINTER TO A PULL, never a substitute for one"* — and **"no zero-transit day" was never a finding, it was the edge of a scope.** `[[finding_verification_zero_is_ambiguous]]`, third fleet instance this week.
2. **🆕 Seven zero-TANKER days: 7/24 · 7/25 · 7/27 · 8/2 · 8/5 · 8/6 · 8/9** — four of them in August, on non-zero total traffic. **For an oil thesis this is the more relevant object**, and FALCON's `n_total`-keyed bands read each one as an ordinary print. Recorded by BRENT, deliberately **not** promoted to an instrument (no base rate yet).
3. **★★ A NEW INDEPENDENT ROUTE, and it matters for Disc-H route-counting.** BRENT adopted **`PROMPT_PREMIUM = Dated Brent − ICE front-month settle`** as a tracked series (no trigger, no registry row). Clean regime break **7/21**: negative 21-of-21 → **positive 16-of-16 since**. ⛔ **Load-bearing: it peaked at +$7.20 on 8/5 — the price LOW of the ~15% "deal-today-or-tomorrow" selloff. The deal talk repriced paper and did not reprice a single barrel.** ⇒ **This is priced by cargo buyers and is NOT PortWatch-derived**, which answers the circularity that forced BRENT to downgrade ORACLE on 8/10. **M-06's route count genuinely widens by one class** — the first such widening on that row in weeks. ⚠️ Two regimes inside n=50 ⇒ quote the regime, never the +1.20 mean.
4. **✅ Routing Boundary #3 RESCINDED** (BRENT, 8/12) — Cushing 2-of-2 on the frozen letter (20.955M / 22.566M), second independent instrument agrees (WTI−Brent −$5.73, $10.7 from trigger), adverse reading run and rejected. **Re-activation automatic on any single print <20.0M.** Carried by LIQUID/HENRY/RED since 6/24.
5. **BRENT THESIS → v5.5** (minor): v5.4's claim unchanged; it now has a price shadow it did not build.

---

## 6. What did NOT move, and why

**The split stays 21 / 44 / 35.** No re-mark.

- Every item in §4 is a **figure correction with no state change** — VIX still sub-15 and still an episode low; the exam still graded 6-of-8 with 1 adverse; RED's corrected 5y5y evidence is **stronger**, not weaker, and RED itself moved **no weight** at S30 (HOLD 69 / net-bear 60 confirmed twice this afternoon).
- §2 **strengthens** the adverse call (primary-verified, 3.8% base rate) but branch 4 was already the grade; verification does not re-open a resolved exam.
- §3 is a **resolvability defect in the falsifier, not evidence about the world** — and per `[[finding_resolvability_defect_is_status_not_confidence]]` that is a **STATUS mark, never a confidence move.** The split's forcing condition is now flagged **🟠 PARTIALLY DEFECTIVE (branch A unreachable)** on the board; the number itself is untouched.
- §5 widens M-06's route base by one genuinely independent class. **Held rather than banked** — Disc-H says state the class count; a route added at 17:5x on a same-day correction pass is disclosed and graded next pass, not converted into a confidence point on the evening it arrives.

**The one thing a reader should take from this pass:** pass A's board was wrong about its own instrument access, and the cost was not a missing number — it was **a tension row reversed, a standing rule proposed, and eight credit figures downgraded to hearsay, all on a query-shape artifact.** Everything §1 recovered was available the whole time.

---

## 7. ⛔ §3 IS CORRECTED — RED's diagnosis (CHG-RED-046, 17:51 ET, mid-pass) beat mine

**§3 said "branch A cannot fire." That is wrong, and it was wrong in the direction that made my self-catch look bigger than it was.**

RED pulled the same series independently (397 obs) and found the sharper defect:

| Leg | State | Verdict |
|---|---|---|
| A: ratio ≥3.60 on 3-of-5 | **already true, 8 consecutive sessions, at the sample MAX** | 🔴 **SATISFIED ON DAY ONE** |
| B: ratio <3.40 s=5 | needs **CCC −98bp** from 1023 | 🔴 unreachable by 8/28 |

⇒ **Both branches are LIVE. Branch A collapses to "HY ≥280 s=3" (8bp away); branch B to "HY <260 s=3". The ratio contributes NOTHING to either.** The falsifier built to test the CCC-tail thesis was specified so the CCC tail cannot move it.

**Where my §3 went wrong:** an **unconditional joint base rate** (0/418) answers *"has this pair ever co-occurred?"* — a real question, but not the binding one. The binding question is **"does each leg still discriminate, conditional on the state at freeze-time?"** Branch A's ratio leg was true when I froze it and stayed true; conditional on that regime, A needed only +8bp on HY. **My own registered discipline already covers this** — `[[finding_escalation_line_needs_delta_not_level]]`: *would it fire on day one? then it is a descriptor.* I did not run it on my own registration.

⇒ **Two checks, not one: (1) CAN each branch fire, unconditionally; (2) does each LEG discriminate, conditionally.** The denominator finding in §3 stands as the reason the *unconditional* joint is 0.0%; it is not the reason the falsifier is broken.

**RED's proposed repair** — replace A's ratio leg with **"CCC retraces <40% of any HY retracement over the window"** (live: 17% vs 94%). Tests the mechanism, can fail, not true on day one, stays inside REGINALD's ownership.

⚖️ **And my §3c "disclosed, not moved" is itself corrected.** That was right for a change **loosening** the bear branch in my favour. It is **wrong as a blanket rule**: RED proposes this **against its own interest, while the spec is frozen against both of us, and it makes the test harder** — the one class of mid-flight re-spec the goalpost objection cannot reach. ⛔ **But I am the interested party under a registered seat falsifier, so it is routed to PROME/Will with both readings, not self-ruled.**

## 8. The rest of RED's ruling

✅ **BRANCH 4 UPHELD.** On my own Disc-A, run as a two-sided counterfactual: **CCC frozen at 7/16 ⇒ the ratio never reaches 3.60 · HY frozen at 7/16 ⇒ it fires on CCC alone.** Ratio 3.761 = **the maximum of all 397 observations**. **No 8pp owed; none taken.**

⛔ **§4's window-length reconciliation is RETRACTED — RED took down the thing I called the pass's synthesis product, and it was right.** 69% of the month's ratio move landed 7/31→8/6, **a window in which CCC OAS FELL 17bp**; the ratio rose because HY tightened proportionally faster. **Over sub-windows the ratio is a proportional-differential gauge.** ✅ **Replaced by RED's endpoint-invariant form: HY widened +16bp and retraced 94%; CCC widened +64bp and retraced 17%.**

⚠️ **RED declined the branch-2 upgrade I offered** (FSK ex-waiver ⇒ Break UP ≥8pp) on **scope, not benignity** — and flagged that refusal as the only real evidence its ruling was untilted, since branch 2 would have moved the split toward its own book.

⚠️ **One correction owed back to RED:** its §0 opens *"FRED is blocked to you; it is not to me."* **It is not blocked to me either** — §1 above. RED verified my figures believing it was covering a gap that had already closed; the verification is still worth having (two independent pulls), but the premise was mine and wrong.

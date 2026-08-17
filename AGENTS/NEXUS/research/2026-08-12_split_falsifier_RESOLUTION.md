# RESOLUTION — the 8/12 split falsifier, graded against the frozen branches

**Graded:** 2026-08-12 Wed ~16:1x ET (post-close, the registered evaluation point).
**Registrant / grader:** NEXUS. **Frozen spec:** `research/2026-08-03_split_and_coverage_prereg.md` §§1-4, untouched since 2026-08-03 ~19:20 ET.
**Split at freeze:** 25/37/38. **Split entering this grade:** 22/40/38 (re-marked 8/7 on non-exam evidence, permitted by §6).

---

## 1. Coverage — graded member by member against the frozen 8

Counting rule as written: **REPORTED = published AND read at primary by a fleet agent AND recorded on a surface.** Published-but-unread does not count.

| # | Instrument | Verdict | Basis |
|---|---|---|---|
| 1 | **NY Fed Q2 HHDC** ⭐ | ✅ **REPORTED** | Printed 8/11. CARL pulled the PDF **and the `.xlsx` data file** direct (newyorkfed.org; WebFetch 403 → curl+UA), graded against `thesis/HHDC_Q2_2026_GRADING_CARD.md` frozen 7/24. Cover confirms 2026:Q2/Aug-2026; Q1 not revised. |
| 2 | **CCLFX N-23C3A** ⭐ | ✅ **REPORTED** | Filed 7/28, graded by BROCK — 🟠 base case, 5% held, accommodation stays withdrawn. |
| 3 | ARCC Q2 marks | ✅ **REPORTED** | Read + graded; SHADE's own ARCC pre-registration graded 8/4, 0-of-4. |
| 4 | OCSL / OBDC / OTF marks | ✅ **REPORTED** | RED off EDGAR primaries; BROCK same-day independently. |
| 5 | FSK / MFIC marks | ✅ **REPORTED** | Graded **twice, independently** (RED + BROCK), figures reproduce; BROCK corrected RED's lead datum (FSK raise uncovered ex-waiver). |
| 6 | Apollo/Athene Q2 (M-11 dual test) | ❌ **NOT REPORTED** | SHADE dark since 8/4. Leg 2 (ATH Q2 10-Q, re-dated ~8/6-8/10) is **ungraded**. Published-but-unread does not count — the rule binds here exactly as it bound ARCC at freeze. |
| 7 | Fitch auto ABS ATR | ❌ **NOT REPORTED** | **5th consecutive unpublished month.** Will ruled 8/10 to re-point CARL's V2 onto OTTO's SEC 10-D panel *because* of the non-publication — the instrument was abandoned, not read. |
| 8 | HY / CCC OAS (daily) | ✅ **REPORTED** | Read at primary through the window by RED (FRED) and tracked by REGINALD (VX-REG-18.04 ratio). ⚠️ **Not NEXUS-pulled** — FRED is blocked to me again as of this session (timeout + empty curl). Carried at owner attribution. |

> **REPORTED = 6 of 8. Both discriminators (#1 HHDC, #2 CCLFX) are among them.**
> **§2 coverage bar (≥6 of 8 AND both discriminators) is SATISFIED — exactly at the bar, not comfortably above it.**

⇒ **Branch 3 (EXAM DID NOT SIT) does NOT fire.** The §4 non-renewable NO-VERDICT clause is not invoked and remains unspent.

---

## 2. Adverse count

Grading basis as frozen (§1): manager marks grade on **TERMS + KB-083 + BRK-32, not on the printed price. A clean price mark with rotted terms is an ADVERSE reading, not a benign one.**

| # | Reading | Adverse? |
|---|---|---|
| 1 HHDC ⭐ | CC 90+ **12.92%, −20bps** = first decline off the 15-yr high. CARL's CRL-05 cut **85 → 20**. But the card's 4-cell discriminator graded **CELL B = AMBIGUOUS**, and cell C ("bureau improves in step with issuers") **failed on its third conjunct**: CC flow into 30+ **rose** 8.61→8.69%, auto (7.72→7.87 / 2.97→3.00) and mortgage (3.76→3.95 / 1.48→1.52) transitions rose on **both** legs. Denominator guard: **100% of the share decline is denominator growth** — delinquent CC **dollars ROSE $0.23B** on +$21B/+1.7% balances; $43.5B moved **into** severely derogatory (1.754→1.987%); bankruptcies +10.3%. | **NO — AMBIGUOUS.** Not benign either. Taken at the card owner's own pre-committed cell verdict, called "ambiguous not favourable" by CARL against a card frozen 18 days early with seven named self-guards. I do not overrule an owner's frozen discriminator. |
| 2 CCLFX ⭐ | 🟠 base case; 5% held; accommodation stays withdrawn. | No |
| 3 ARCC | Benign; SHADE's pre-reg 0-of-4. | No |
| 4 OCSL/OBDC/OTF | Marks benign. Terms caveat logged: OTF 86% / 60%-cash. | No |
| 5 FSK/MFIC | Zero base cuts, one **raise** — ⚠️ uncovered ex-waiver ($0.039/sh KKR-subsidiary fee waiver inside $0.44 NII) = **sponsor-pocket support, a NEW channel**. But terms graded **5-for-5 renewing** and non-accruals **CONVERGED** (the opposite ordering from migration), by two independent graders. | No — channel logged, not an adverse reading. Two independent owners graded it benign-with-a-label-correction; I record the channel and do not overrule both. |
| 8 HY/CCC | Index price clean (HY 271→**272 [8/11]**, the 7/27-7/31 ≥280 run fully round-tripped). **Tail composition rotted:** CCC **>1000 for a 12th session** since 7/27, and REGINALD's **VX-REG-18.04 in a 3rd HARD-FIRE 8/7-8/11** (3.752 / 3.756 / 3.761, clear of the 3.6× line) with driver-decomposition since the 7/16 baseline of **CCC +53bp vs HY +1bp = CCC-widening-LED — the pre-registered ESCALATION case**, which REGINALD explicitly distinguishes from the HY-tightening-led benign beta of fires #1 (7/13) and #2 (7/22). | ✅ **YES — ADVERSE.** This is the frozen grading basis operating exactly as written: a clean printed price over rotted composition. The call is not mine — it is an owner's registered grade on a pre-existing numbered line, flagged by REGINALD as a "Surprise." ⚠️ **Fence: NOT self-escalated by REGINALD; Will's call on a packet to LIQUID/BROCK.** |

> **ADVERSE = 1, and it sits in a NON-discriminator.**

---

## 3. Branch fired

**§3 BRANCH 4 — MIXED.** Condition as written: *"≥6 reported, both discriminators in, **exactly 1 adverse** or adverse only in non-discriminators."* Both halves of that disjunction are satisfied independently.

**Forced move: NONE.** Obligation as written: *"I must name the adverse print and state in ≤3 sentences why it did not move the split. Silence here is not permitted."*

> **The adverse print is the CCC-led escalation fire on exam member #8 (REGINALD VX-REG-18.04, 3rd hard-fire, CCC +53bp vs HY +1bp since 7/16).** It did not move the split by itself because it is one evidence class on one root (R3 credit-substance) that has **not yet registered on the broad index** — HY sits at 272 with its re-arm line 8bp away, so the divergence is still a tail phenomenon rather than a recognition event. It is nonetheless the **first change-side bear datum in five weeks**, so rather than absorb it into a confidence number I have registered it as the resolving instrument of the successor falsifier in §5 — which is where a datum this shape belongs.

---

## 4. ⚠️ Anti-rationalization guard (§5) — run against MYSELF, on the record

§5 binds symmetrically. The exposure here is **not** an adverse print I am explaining away; it is the reverse, and it is worth more than the guard as literally written:

**Branch 4 saves me 5pp of forced move relative to Branch 1.** Branch 1 (0 adverse) would have forced *"Unresolved CUT by ≥8pp"* — 38 → ≤30. Branch 4 forces nothing, and I am taking Unresolved to 35 (−3). **The single adverse call is therefore worth 5pp to me, and I made it.** That is precisely the configuration in which a grader's judgement should not be trusted on its own recognizance.

**Disposition:** the branch call is **routed to RED for challenge** with this asymmetry stated, rather than banked. Specific challenge invited: *is the CCC-led escalation fire an adverse reading of exam member #8, or did NEXUS promote a tail-composition datum to "adverse" in order to escape a forced 8pp cut?* If RED grades it benign, **Branch 1 fires and Unresolved owes ≥8pp**, and I will take it.

Also recorded, because the frozen spec did not anticipate it: **§3's branch conditions have no AMBIGUOUS category.** The HHDC — the exam's most load-bearing member — resolved to a cell its own card calls ambiguous, and the branch table can only read it as "not adverse," which rounds an ambiguous discriminator toward benign. **That is a spec defect in my own pre-registration, found at resolution.** It did not change the branch (branch 4 fires on the non-discriminator disjunct regardless), but the next registration gets an explicit ambiguous handling rule.

---

## 5. Successor falsifier — REGISTERED (Disc-J)

The 8/3 falsifier has resolved and is spent. Disc-J forbids carrying a standing probability without a registered falsifier, so the new split ships with one, frozen here **before** the instruments print.

**Resolution date: Fri 2026-08-28** (QCEW day — the largest scheduled item in the window, and it gives the credit instrument 12 more sessions).
**Resolution source, per N2 (Will-adopted 8/11 — a routed figure travels with its resolution source and its bar as literally written):** REGINALD's `VX-REG-18.04` row for the ratio; RED's FRED pull for HY/CCC levels. **NEXUS does not own either instrument and does not re-derive them** — FRED is currently blocked to me, and pretending otherwise is how a falsifier becomes ungradable.

| Branch | Condition (on the 8/28 close) | Forced move |
|---|---|---|
| **A — RECOGNITION** | Ratio **≥3.60 on ≥3 of the 5 sessions ending 8/28** **AND** HY OAS **≥280 sustained 3** at any point in the window (RED's FT-01 re-arm, s=3) | **Break UP ≥6pp**, from Grind. The CCC divergence registered on the broad index ⇒ the tail was leading, not idiosyncratic. |
| **B — BETA** | Ratio **<3.40 sustained 5 consecutive sessions** **OR** HY **<260 sustained 3** (HENRY's registered kill leg) | **Break DOWN ≥6pp**, to Grind. The tail re-converged ⇒ the 3rd fire was composition noise and T-12's level leg dies. |
| **C — NO-VERDICT** | Ratio between **3.40 and 3.60**, **OR** ratio ≥3.60 while HY never reaches 280 | **No forced move on Break/Grind.** Unresolved must be stated as **EARNED**, with the ratio and HY level quoted, never defaulted into. ⚠️ **NON-RENEWABLE — see below.** |

**Construction checks (the four Disc-J requires):**
- **Symmetric magnitudes** — ≥6pp in both directions, so the registration smuggles in no lean.
- **NO-VERDICT band has numeric edges** — 3.40 and 3.60, not an adjective. (3.60 is REGINALD's own registered line; 3.40 sits below the 7/16 baseline of 3.579, so branch B requires a real re-convergence, not a drift.)
- **Non-renewable** — if branch C fires at 8/28 **and again at the next evaluation (~9/11 CPI)**, that is not a coverage problem, it is **the answer**: the CCC tail is a permanent structural feature of this index, not a signal, and T-12's level leg is measuring a constant. In that case I owe a **re-spec of T-12 onto an instrument that discriminates** — candidates named in advance: CCC *flow* share of index moves (RED's weight arithmetic, currently 13%), CCC issuance/refi volumes, the 319bp basket, single-name CDS.
- **What a repeated no-move means** — if branch **A or B** fires and I hold Unresolved at 35 anyway, **that is a self-protection tell, not a judgement**, and it must be written as such in the same pass. Unresolved has now sat at 38/38/38/35 across four marks; a fifth hold under a branch that should have moved it is the exact failure the 8/3 registration was built to stop.
- **Disc-A pairing** — the falsifier tests the **mechanism** (does the CCC tail lead the index, or is it composition noise?), not only the threshold. A ratio ≥3.60 that fires because *HY tightened* rather than *CCC widened* resolves **TRUE-in-letter / FALSE-in-spirit** and does not count for branch A. **The driver-decomposition is part of the bar**, exactly as REGINALD grades it.

**Not governed here (§6 carried forward):** QCEW 8/28 itself, the 8/19 FOMC minutes, the war/physical leg, and any policy shock. Those move the split on their own merits.

---

## 6. What the exam actually answered

The recognition question was: *survivor-pool optics / no-print-by-design, or genuine deterioration?* After the full 8-member exam:

**It sat, and it answered "mostly optics — with one instrument dissenting."** Five members read benign on the owners' own grading bases, twice-independently in three cases. The load-bearing discriminator came in ambiguous rather than benign, and its ambiguity is specific and durable: **the level improved while the dollars, the transitions and the terminal bucket did not.** One member read adverse on composition under a clean price.

The frozen T-15 claim — *"no-print-by-design"* — **did not resolve TRUE.** The prints came, most of them, and they were readable. What survives is narrower and better specified than what went in: not that deterioration is being hidden, but that **it is being measured in the wrong unit** — shares rather than dollars, index rather than tail, level rather than flow. That is a live, testable claim, and §5 is now pointed at it.

---

*Frozen sections of the 8/3 registration (§§1-4) were not edited. This file grades against them. Pointer lives in STATUS §T-19 and §LAST RUN. Next evaluation ~2026-08-28 per §5.*

---

## ⚠️ ADDENDUM — 2026-08-12 pass B (~18:1x ET). **§5's BRANCH A IS UNREACHABLE. The spec text above is NOT edited.**

Base-rated at primary after this file was written (`BAMLH0A0HYM2` / `BAMLH0A3HYC`, 422 sessions, 2025-01-02 → 2026-08-11 — **FRED was never blocked; §5's parenthetical saying so was a false diagnosis**):

| §5 branch | Jointly, rolling windows |
|---|---:|
| **A — RECOGNITION → Break UP ≥6pp** | **0 / 418 = 0.0%. Never satisfied in 19 months.** |
| **B — BETA → Break DOWN ≥6pp** | 359 / 418 = **85.9%** |

**Cause is structural: the ratio's denominator IS branch A's other instrument.** HY widening pushes CCC/HY down, so A demands two anti-correlated conditions at once (7/28-7/30: HY widest 284-287, ratio lowest 3.530-3.542; 8/6-8/11: HY tightest 270-272, ratio highest 3.752-3.761). **No threshold choice repairs it.**

⇒ **The four construction checks above verified MAGNITUDE symmetry and never verified SATISFIABILITY symmetry.** A registration symmetric in what it pays, asymmetric in what it can pay out.

⛔ **DISCLOSED, NOT MOVED — §5 is frozen and grades 8/28 exactly as written.** Re-cutting a bear-side forcing condition 11 days after freezing it, in the direction favouring a call already flagged as worth 5pp to its author, is goalpost-moving.

✅ **What survives review:** branch **C**'s second clause (*"ratio ≥3.60 while HY never reaches 280"*) **names the 8/12 state exactly** — the registration did not miss this case, it anticipated it — and the **non-renewable** clause converts a likely double-C into a **forced T-12 re-spec by ~9/11**, off the candidate list already named pre-data.

**Pre-committed, pre-resolution:** expected outcome **branch C**; a C **scores nothing** and must be written **EARNED** with both levels quoted; **if A fires anyway the ≥6pp is taken without re-litigating these base rates.** **Reachability base-rating is now permanent in the construction set.**

✅ **Also verified pass B, and it cuts the other way:** the adverse call §2 rests on **reproduces exactly at primary** (7/16 → 8/11: HY +1bp, CCC +53bp, ratio 3.579 → 3.761), and REGINALD's ≥3.60 line base-rates at **16/422 = 3.8%** — genuinely discriminating. **The "I could not verify at primary" attack handed to RED is withdrawn.**

Full working → `2026-08-12b_falsifier_base_rate_audit.md`.

---

## ✅ ADDENDUM 2 — 2026-08-17. **RULING ⑤ LANDED (Will, 2026-08-13 AM, via PROME): BRANCH A's INERT RATIO LEG IS REPLACED BY RED's DELTA LEG, effective for the 8/28 resolution.** §5's frozen text above is still NOT edited; this addendum is the operative overlay.

**Adopted verbatim as proposed in the pass-B packet and ruled by Will:**

> Branch A's ratio leg (`CCC/HY ≥3.60 on 3-of-5`) is **REPLACED** by: **"CCC retraces <40% of any HY retracement over the window"** *(peak-to-close within the resolution window; live values at proposal: CCC 17% vs HY 94%)*.

**Operative branch set for 2026-08-28, restated in full so no reader reconstructs it:**
- **A — RECOGNITION ⇒ Break UP ≥6pp:** HY (`BAMLH0A0HYM2`) **≥280 sustained 3** AND **CCC retraces <40% of any HY retracement** over the window.
- **B — BETA ⇒ Break DOWN ≥6pp:** HY **<260 sustained 3** *(B's original ratio leg was shown unreachable by 8/28 — CCC −98bp required — and per the same ruling's logic B grades on the HY line; a B-fire's driver-decomposition still applies per Disc-A)*.
- **C — NO-VERDICT (non-renewable):** neither A nor B ⇒ scores NOTHING, written EARNED, and a double-C at ~9/11 forces the T-12 re-spec off the pre-named candidate list.

**Why this survives the goalpost objection (recorded with the ruling):** the change was proposed by the ADVERSARIAL desk against its own interest, while the spec was frozen against both parties, and it makes the test HARDER — the one class of mid-flight re-spec the objection cannot reach. My §3c "disclosed, not moved" position was wrong as a blanket rule for this class and the movement is on the record. **The safe-default option-2 language ("resolves on HY alone") is SUPERSEDED and must not survive on any surface.**

**Scope fences carried from the ruling:** REGINALD's separate 8/13 candidate (pair the ratio with the **CCC level**, never HY — now base-rated by REGINALD at CCC ≥1050 + HY ≥272 2-consecutive = 1.5%, with leg (b) historically non-binding) is **design input for the post-8/28 re-spec only**, NOT adopted for this resolution. Zero thresholds moved by PROME; the leg's words are RED's, the judgment Will's.

**Also binding on the 8/28 grade (REGINALD, 8/13, fire-count adjudication):** the current run began **7/31** (hard-fire criterion met **8/04**; 9 unbroken sessions >3.6× through 8/12 at 3.764), and the CCC-LED attribution is **baseline-sensitive** — CCC-led on the 7/16 baseline; majority HY-tightening on the run-start (7/30) baseline. The escalation to LIQUID/BROCK was **STOOD DOWN (Will-approved 8/13)**; the tripwire itself is unchanged and still firing. Grade the delta leg on the retracement arithmetic, not on the "escalation case" label.

*Encode-confirm owed to PROME per the ruling packet — sent 2026-08-17 (carve-out ①).*

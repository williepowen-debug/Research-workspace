# MIDAS — STATUS

**Last Updated:** 2026-08-14 ~15:4x ET (**MIDAS-07 GRADE SESSION** — PROME-directed spawn after a 7-day dark gap 8/7→8/14; catch-up + the frozen gold-COT frame graded on the 15:30 print) · prior 2026-08-07 (kill-cond #3 FIRED; WGC Q2 + COT baseline) · **Status:** 🟠 elevated — **M1 v2 kill-condition #3 remains FIRED**; fired-count **1/4**
**Class:** Market-agent (metals as macro tells: monetary + industrial) · **Spawnable by:** PROME or Will · **Maturity:** L2 (instrumented — spot/yield/GSR/LME via `metals_watch.py`; **COT now instrumented via `cot_gold.py`, 8/14**)

> **📏 PRICE-LABEL DISCIPLINE (N5 + my own L-16, applied here rather than cited).** COMEX metals settlements are struck **13:30 ET** (gold/copper; silver 13:25) — **not** 18:00 ET, which is the Globex **trade-date roll**. Today's figures were captured ~15:35 ET, *after* the settlement clock ran, **but I hold no settlement source** ⇒ they are **VENDOR BARS, PROVISIONAL — not closes, not settles.** 8/13 and earlier are **T+1 re-pulled and confirmed** (clause (ii) discharged).
>
> **Confirmed prior-session closes [8/13]:** gold **$4,363.60** · silver **$64.873** · copper **$6.593** · Pt **$1,725.20** · Pd **$1,322.60** · GLD **$398.96**.
> **Provisional vendor bars [8/14 ~15:35 ET]:** gold **$4,432.70** · silver **$64.92** · copper **$6.602** · Pt **$1,753.10** · Pd **$1,322.00** · GLD **$401.52** · **GSR 68.28**.
> **DFII10 2.42 [FRED, 8/12, T+1]** · **LME Cu 207,725t [13 Aug] = −14.9% vs the 2yr median (244,025t), −48.4% off the 4/15 peak.**

> **⚖️ 8/7 MARKS RE-BASED BY HEARTBEAT AMENDMENT #2 (2026-08-10, Will-approved) — this file previously carried the superseded provisional bars.** The 8/7 futures marks were unsettled-session bars ~0.3–1.4% high. **Settled 8/7: gold $4,340.70** (was $4,401.30) · **silver $63.33** (was $63.80) · copper $6.570 · Pt $1,750.10 · Pd $1,374.10. **Derived restatements: 3wk gold move +9.68% → +8.18% · leg-B +8.70% → +7.20% · 8/7 session +3.76% → +2.33% · floor cushion 32.7% → 30.9% · DFII10 8/7 = 2.40 ⇒ the 3wk yield leg is +9bp, not +12bp.** **ETF closes were CORRECT — GLD $398.47 [8/7] stands and the Will-facing GLD note is unaffected.** **NO verdict changes.** *(Reached this desk 4 days late because MIDAS was dark; corrected here. I independently re-derived +8.17%/+9bp on 8/14 — that is corroboration, not discovery; provenance is Am.#2's. → KB-038, L-17.)*

---

## 🔴 HEADLINE — MIDAS-07 GRADED: **(d) INDETERMINATE.** The frame said nothing; the tape said plenty; the gap between them is a defect I pre-registered.

**The grade, on the frozen frame, verbatim and unretuned.** COT as-of **Tue 2026-08-11** [CFTC legacy futures-only, raw `deafut.txt`, code-keyed 088691 full-size, in-row vintage verified, totals reconciled]: **OI 400,309 · NC long 250,936 · NC short 32,996 · net NC long 217,940 · net/OI 54.44%**; gold **$4,383.00** [GC=F close, 8/11]. **WoW: OI +28,758 (+7.74%) · net +20,306 · NC short +3,617 · net/OI +1.25pp.**

| Branch | Condition | Result |
|---|---|---|
| **(a) FRAGILE** | net >225,000 **AND** net/OI >56% **AND** OI >400,000 | **1 of 3.** OI **PASS** (400,309, by 309 contracts); net **FAIL** (217,940 — short by **7,060 = 3.2%**); ratio **FAIL** (54.44%) |
| **(b) ABSORBED** | net/OI ≤53.2% **AND** gold ≥$4,300 | **FAIL** on the ratio (54.44%). Price leg **PASSED** on *every* candidate date ($4,383.00 / $4,408.90 / $4,363.60) — **no date discretion exercised** |
| **(c) SQUEEZE-EXHAUSTION** | NC short <20,000 **AND** OI ≤371,551 | **FAIL** on both |
| **(d) INDETERMINATE** | anything else | ✅ **FIRES** |

**No joint satisfaction** — the registered (b)/(c) overlap never arose, so **no Will adjudication is owed** on precedence.

**⚠️ The two failing FRAGILE legs were not independent at the realised OI.** net = 225,000 on OI = 400,309 implies net/OI = **56.21% > 56%** — so clearing the net leg would have *automatically* cleared the ratio leg. **The three-condition conjunction collapsed to a two-condition test and missed on ONE quantity by 3.2%.**

**🔑 SUBSTANTIVE READ — reported separately and explicitly NOT a branch verdict.** **The "spent fuel" claim from the 8/4 baseline is dead.** The 8/11 week was **not** short-covering: **NC short ROSE +3,617**, the exact opposite of the 8/4 mechanism (price-up/OI-**down**). OI built **+7.74% on fresh longs** (NC long +23,923; nonreportable long +6,520). **My own pre-registered sentence was: *"if (a) FRAGILE fires, open interest is up 7.7%, which means the fuel was not spent, it was replaced."* OI printed +7.74% — essentially the number I named — and (a) did not fire.** ⇒ **The frame returns "no read" on a week whose underlying question has a clear answer: specs did chase, with fresh money, at a pace uncommon in forty years — but not quite enough to satisfy a triple conjunction.** That gap is the **pre-registered D-4 defect**, recorded and **NOT repaired** (frozen frame; Will-gated).

**Crowding, on the full 40-year record** (n=1,929, 1986→2026): **net/OI 54.44% vs median 26.3%, p95 48.9%, all-time max 57.7%** ⇒ **top-5% of the entire series, 3.3pp from the extreme.** *(vs the 1/13 blow-off peak: net/OI **+6.8pp** above its 47.6% on **24.1% less** OI; absolute net still **−13.3%** below it.)*

**Action taken: none.** (d) says *hold, no read* — **M1 stays 3 🟠, composite stays 7/20, no threshold moved, zero capital.** The if-falsified escalation clause is keyed to **(a)**, which did not fire, so **no TERRY sizing route is triggered**; the fresh-leverage observation goes to Will as an **observation**, not a fired trigger.

---

## 🔴 SELF-CORRECTION — three of my published base rates were computed on the wrong window

**Root cause: I ran my gold analysis on the 449-week (2018+) window SAM had pulled for JPY. CFTC publishes COMEX gold back to 1986-01-15 — n=1,929, 4.3× longer.** An inherited window is a **free parameter I did not set.**

| Published (forum, 8/11) | **Corrected (full series, 8/14)** |
|---|---|
| P(ΔOI ≥ +28,449 \| OI ≤400,000) = **"0 of 19 — never observed"** | **20 of 1,103 = 1.81%**; all-time max **+67,010 [2009-09-08]**. Uncommon, **not** unprecedented |
| P(c) = **0.00%, "structurally unreachable"** — NC short <20,000 never in 449 weeks | **WRONG AS STATED: 299 occurrences, min 3,174.** Correct claim = **REGIME-EXTINCT** — none since **2009-01-13** (17.5 years), in a structurally far smaller market |
| "the 449-week series" (×4) | understates my own series by **4.3×** |

**⚠️ And the refutation was immediate: the "never observed" event happened on the VERY NEXT PRINT** (+28,758), taking the 2018+ window to **1 of 20 = 5.00%**.

**✅ What held — and it is the argument for keeping the discipline: I refused to quote 0-of-19 as a probability and published a rule-of-three 95% upper bound of 15.8% instead. The corrected full-series rate (1.81%) AND the realised outcome both sit inside that interval.** The point estimate failed; the honest interval did not.

**Consumer-check owed and routed:** P(c)=0 was consumed by **BRENT's joint-cell table** (its *"CORRELATED CONFIRM"* cell was declared **identically empty** on my figure) and by the forum synthesis ⇒ packets to **PROME / BRENT / SAM**. **None of this changes the MIDAS-07 grade** — branch conditions are frozen; base rates are context. → **KB-042, L-18**

---

## CONVERGENCE MATRIX (universal 5-pt + local state)

| # | Channel | Score (1–5) | Local state | Independence | Key signal [src, date] | Upgrade trigger |
|---|---|:---:|---|---|---|---|
| **M1** | Gold — debasement / real-rates (**v2, kill-cond #3 FIRED**) | **3 🟠** = | **DIVERGE holds.** 3wk 7/17→8/7 **+8.18%** gold through **+9bp** DFII10 (cycle high 2.47 [7/31]). **MIDAS-07 = INDETERMINATE ⇒ no score move by the frame's own letter.** Positioning now shows **fresh leverage, not spent fuel** — but that read has no registered branch | monetary root (shared w/ M2) | gold **$4,363.60** [close 8/13]; DFII10 **2.42** [FRED 8/12]; net/OI **54.44%** [COT 8/11] | → 4 if DIVERGE persists past 8/28 (**MIDAS-06**) or repeats on a rising-yield week. Downside: gold <$3,317 w/o yield spike (**33.6% away**) |
| **M2** | Silver + gold/silver ratio | **1 ⚪** | **GSR 68.28**, still falling from 71.46 [7/17]. Silver **$64.873** [8/13] vs $63.33 [8/7 settled]. Far below Yellow(85). **Directionally important, score-neutral:** a falling GSR into a gold bid = broad hard-asset bid, NOT risk-off | monetary root (shared w/ M1) | GSR **68.28**; silver **$64.92** [prov. 8/14] | GSR >85 sustained 3+ sessions → 2; >95 → 4 (moving AWAY from both) |
| **I1** | Copper — Dr. Copper / China | **1 ⚪** | Copper **$6.593** [8/13], flat-to-firm. **LME 207,725t [13 Aug] = −14.9% vs 2yr median (244,025t)**, **−48.4%** off the 4/15 peak — still drawing down hard. Price firm + inventory well below normal = **continued physical tightening** | industrial/China root | copper **$6.593** [8/13]; LME **207,725t** [8/13] | copper QoQ <−5% → 2; conjunction fire (5) needs copper −20% AND inv +100% — both moving AWAY. ⚠️ **no UPSIDE band exists (L-13, AWAITING)** |
| **I2** | PGMs (platinum / palladium) | **2 🟡** | Platinum **$1,725.20** [8/13], **palladium $1,322.60 [8/13] — −3.7% vs the $1,374.10 8/7 settle**, giving back part of the 8/4 spike. **The 8/4 +8% single session remains UNEXPLAINED** (recorded, not back-fitted). No outage evidence. Russia-Pd antidumping 132.83% final (Fed Reg 2026-08487) — priced | supply root (SA/Russia) | Pt **$1,725.20** / Pd **$1,322.60** [closes, 8/13] | confirmed major SA/Russia outage → 4. **No registered trigger fired** |

**Composite: 7/20** *(M1 3 + M2 1 + I1 1 + I2 2). Unchanged from 8/7 — **no score moved this session**, which is the correct consequence of an INDETERMINATE grade.*

**Independence note:** M1 and M2 share the monetary root — **count once.** GSR *falling* while gold is bid means M2 corroborates a **monetary/hard-asset** root, not a risk-off one. I1 tightening is a **separate** (physical/AI-grid) root. **Not a single risk-off shock** — the classic signature is gold UP *and copper DOWN*, and copper is firm.

---

## EXIT / INVALIDATION (standing-rule-vs-state triad)

**Kill rail re-derived: 2026-08-07** *(unchanged this session — MIDAS-07 was a grading frame, not a kill condition; no leg was re-measured, so the stamp is NOT restamped. Per `finding_hygiene_commit_rearms_the_staleness_lie`.)*

| Channel | Standing rule | Current state @ level | FIRED? |
|---|---|---|---|
| M1 (v2) | gold <$3,317 w/o yield spike · WGC Q2 <100t · **gold re-decouples UP 3+wk** | gold **$4,363.60**, **33.6% above** the $3,317 shelf; **CB Q2 288.9t = 2.89× the 100t line**; **UP-decoupling +8.18% over 3wk vs +9bp DFII10** | **🔴 FIRED** (leg 3). Legs 1–2 measured and clear |
| M2 | GSR >95 sustained (risk-off) | GSR **68.28**, falling | NOT-FIRED (moving away) |
| I1 | copper −20% AND LME inventory +100% | copper firm; LME **falling** to −14.9% *below* median | NOT-FIRED (both legs opposite) |
| I2 | major SA/Russia PGM supply outage/sanction | Pd −3.7% off the 8/7 settle, no outage evidence; sanctions priced | NOT-FIRED |

**Fired-count: 1 of 4** *(unchanged).*

**Bidirectional flip, restated on corrected figures:** **falsifies the premium-reassertion read** — gold retraces below **~$4,050** (7/31 shelf) while DFII10 holds ≥2.40 ⇒ re-instates v2's "re-coupled/capped" frame, M1 → 2. **Confirms and escalates** — DIVERGE persists past **8/28** (MIDAS-06) or repeats on a rising-yield week ⇒ M1 → 4.

---

## OPEN ON MIDAS (next session)

1. **🔴 WILL_QUEUE row 51 — `MIDAS-06` branch (a) cites a phantom print.** Its boundary is literally `gold closes >= $4,401.30 (the 8/7 close)`; on the Am.#2-corrected record that close **never printed** ($4,340.70). **OUTCOME-DETERMINATIVE:** at the 8/13 close ($4,363.60, DFII10 2.42) branch (a) **FIRES on the corrected anchor and does NOT on the registered one.** PROME rec = re-key to $4,340.70 preserving letter-intent (row-48 class), riders = dated re-spec + superseded value verbatim + **ruled in a NON-grading session**. **Will rules. I touch nothing.** Must be ruled **before 8/28** — and *cold*, because ruling it after the print would be choosing the outcome. → L-17
2. **MIDAS-06 resolves 8/28** — DIVERGE persistence. **Prep only; do not grade early.** Gated on item 1 and on L-12.
3. **⏳ AWAITING (self-rulable, deliberately deferred 8/14, PROME-endorsed):** **(a) L-12** continuity boundary (continuous vs endpoint) — **must be ruled before MIDAS-06**; **(b) L-13** I1 upside/tightening band. **Deferred because ruling a boundary the same day I grade the channel it governs is tuning-to-tape.** Rule both in a session with no live grade, pre-8/28. **(c) L-15** = ruled UP to fleet scope 8/12, **DAEDALUS owns the encode** — I am the demonstrating case, nothing owed by me.
4. **Consumer-check follow-through** — the corrected base rates (KB-042) must reach **BRENT** (joint-cell table built on P(c)=0) and **SAM** (window provenance). Packets routed 8/14; confirm consumption.
5. **📏 N5/L-16 residue:** Pt/Pd settlement clocks are **PROVISIONAL** (inferred from holiday early-close ordering, not a regular-session rule) — owed. And **no settlement SOURCE exists for metals in `fetch.py`**; knowing 13:30 ET does not deliver the settled price (WALTER §7 item 2, open for metals too).
6. **Miner equities = deliberately OUT OF SCOPE** (ruled 8/14, KB-039). Re-open trigger: **miners diverging >20% from the metal over a quarter.** WALTER asked to stop routing miner artifacts as `action:`.
7. **ZHAO LPR date-fork — day 28, STILL OPEN.** ZHAO STATUS/NEXUS/ZHA-14 still carry 7/21 vs the correct 7/20 Beijing. **Do NOT edit ZHAO's files.**
8. **The 8/4 PGM +8% single session — still unexplained.** Find the cause or record it as permanently unattributed. *(Pd has since given back 3.7%, which weakens any supply-shock reading.)*
9. **Carryover:** China Cu imports −41.3% base-effect (ZHAO's series); WPIC Pt-deficit PROV; sulfur/acid Platts **spot** print owed (current figures are OSP/KSP contract prices — L-14); NEXUS full-schema debt.

---

## BOTTOM LINE

**MIDAS 2026-08-14: the frozen frame returned "no read," and I wrote it down rather than talk a branch into firing.** MIDAS-07 grades **(d) INDETERMINATE** — the pre-registered **modal** outcome. FRAGILE cleared its open-interest leg by 309 contracts and then missed on net long by **7,060 (3.2%)**; ABSORBED failed only on the ratio; SQUEEZE-EXHAUSTION failed on both. **No score moved, no threshold moved, zero capital.**

**But the honest report is that the frame is quieter than the tape.** Specs did not merely hold — **open interest built 7.74% on fresh longs while shorts ADDED**, the precise reversal of the 8/4 short-covering week, which kills the "fuel is spent" reading I carried into this print. My own registered note said an OI build of 7.7% would mean *"the fuel was not spent, it was replaced"* — the number arrived and the branch still did not fire, because FRAGILE demanded three conditions whose interaction I had already measured as self-defeating. **Crowding now sits in the top 5% of the entire 1986–2026 record (net/OI 54.44% vs a 26.3% median), 3.3pp from the all-time extreme.** That is a real state, and my frame has no cell for it.

**The session's sharpest finding is again against myself: three of the base rates I published to the fleet were computed on a 449-week window I inherited from another desk's pull, when my own series runs 1,929 weeks back to 1986.** "Never observed in 449 weeks" became **1.81% across 1,103 comparable weeks** — and the never-observed event then happened **on the very next print**. "Structurally unreachable" became **regime-extinct: 299 occurrences, none since January 2009.** The one thing that survived intact is the guard I nearly skipped — refusing to quote 0-of-19 as zero and publishing a rule-of-three bound of 15.8%, an interval that contains both the corrected rate and the outcome. **The point estimate was wrong in a way the interval was not, which is the whole case for writing the interval down.**

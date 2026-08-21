# MIDAS — STATUS

**Last Updated:** 2026-08-21 ~08:3x ET (**L-12 / L-13 RULING SESSION** — Will-directed, non-grading; row-51 encode landed 8/20, both deferred boundary questions ruled under DELEGATION_TIER) · prior 2026-08-14 ~15:4x ET (**MIDAS-07 GRADE SESSION** — PROME-directed spawn after a 7-day dark gap 8/7→8/14; catch-up + the frozen gold-COT frame graded on the 15:30 print) · prior 2026-08-07 (kill-cond #3 FIRED; WGC Q2 + COT baseline) · **Status:** 🟠 elevated — **M1 v2 kill-condition #3 remains FIRED**; fired-count **1/4**
**Class:** Market-agent (metals as macro tells: monetary + industrial) · **Spawnable by:** PROME or Will · **Maturity:** L2 (instrumented — spot/yield/GSR/LME via `metals_watch.py`; **COT now instrumented via `cot_gold.py`, 8/14**)

> **📏 PRICE-LABEL DISCIPLINE (N5 + my own L-16, applied here rather than cited).** COMEX metals settlements are struck **13:30 ET** (gold/copper; silver 13:25) — **not** 18:00 ET, which is the Globex **trade-date roll**. Today's figures were captured **~08:27 ET — BEFORE the 13:30 settlement clock runs**, so the 8/21 line is an in-flight session bar, the weakest label on this page. **8/20 and earlier are T+1 re-pulled and confirmed** (clause (ii) discharged) — and see the clause-(ii-b) correction below, which is why that re-pull is not a formality.
>
> **Confirmed closes [8/20], T+1 re-pulled and stable across two pulls:** gold **$4,516.30** · silver **$68.026** · copper **$6.460** · Pt **$1,831.00** · Pd **$1,336.30** · GLD **$415.26** · **GSR 66.39**.
> **Provisional vendor bars [8/21 ~08:27 ET — PRE-SETTLE, session in flight and ticking]:** gold **$4,647.10** · silver **$69.50** · copper **$6.611** · Pt **$1,892.30** · Pd **$1,364.00** · **GSR 66.86**.
> **DFII10 2.35 [FRED, 8/19, T+1]** — down from 2.44 [8/17] · **LME Cu 239,925t [20 Aug] = −0.2% vs the 2yr median (240,325t)**, having REVERSED off a −14.7% trough [14 Aug].
>
> 🔴 **N5 CLAUSE (ii-b) FIRED ON MY OWN DESK THIS MORNING — the correction is recorded because I published the bad figure.** A pull at **21:16 ET 8/20** (past the 18:00 ET Globex trade-date roll) returned **$4,570.50 labelled "8/20"**; a 08:18 ET re-pull still showed **$4,571.20** for 8/20. By 08:27 ET the vendor had re-dated it: **8/20 settled at $4,516.30** and the $4,57x print was the **in-flight 8/21 session**. **I reported the $4,570.50 figure to Will last night as an 8/20 level — that was a mislabelled in-flight bar, −$54.90 / −1.2% off the true close.** The *direction* of the report (gold has moved hard since 8/13) stands and is if anything understated. **This is exactly the failure mode L-16/(ii-b) exists to catch, landing on the desk that wrote the clause.**

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
| **M1** | Gold — debasement / real-rates (**v2, kill-cond #3 FIRED**) | **3 🟠** = | **DIVERGE holds on the ruled basis.** L-12 RULED 8/21: weekly unit, **endpoint** basis, daily-continuous excluded as unsatisfiable ⇒ the **7/17→8/7 fire STANDS** (+9bp, +8.17%). Gold has since run to **$4,516.30** [close 8/20] and **$4,647.10** [in-flight 8/21] — **but DFII10 has FALLEN to 2.35 [8/19] from 2.44 [8/17]**, so the current leg is gold-up-through-*falling* yields = the CONVERGE-shaped direction, **which the magnitude test refuses** (8/19: −6bp explains +0.31% of a +2.83% move) | monetary root (shared w/ M2) | gold **$4,516.30** [close 8/20]; DFII10 **2.35** [FRED 8/19]; net/OI **54.44%** [COT 8/11 — **vintage #2 reads today 8/21**] | → 4 if DIVERGE persists past 8/28 (**MIDAS-06**). ⚠️ **Branch (a) now turns on the YIELD leg, not the re-keyed gold leg**: gold clears $4,340.70 by **+4.0%** on the 8/20 close, DFII10 **fails ≥2.40 by 5bp** |
| **M2** | Silver + gold/silver ratio | **1 ⚪** | **GSR 66.39** [8/20 closes], still falling from 68.28 [8/14] and 71.46 [7/17]. Silver **$68.026** [close 8/20], **+7.6% since 8/13**. Far below Yellow(85). **Directionally important, score-neutral:** silver OUTRUNNING gold into a gold bid, with GSR at a fresh low for the window = broad hard-asset bid, **NOT risk-off** | monetary root (shared w/ M1) | GSR **66.39** [8/20]; silver **$68.026** [8/20] | GSR >85 sustained 3+ sessions → 2; >95 → 4 (moving AWAY from both) |
| **I1** | Copper — Dr. Copper / China | **1 ⚪ UNSCOREABLE↑** | 🔴 **STATE CHANGE — the tightening read I carried since 8/7 is DEAD.** LME **239,925t [20 Aug] = −0.2% vs the 2yr median (240,325t)**, having **REVERSED off a −14.7% trough [14 Aug]**: **+17.1% restock in 4 business days** with copper price flat ($6.48→$6.46). The 8/14 STATUS line *"still drawing down hard / continued physical tightening"* **no longer holds.** ⚠️ **Per L-13(a), ruled today: this cell is `UNSCOREABLE↑`, NOT `benign`** — the registered bands are all downside and **cannot score either the tightening or its reversal**; ⚪ here means *my bands are blind*, not *the tape is quiet* | industrial/China root | copper **$6.460** [close 8/20]; LME **239,925t** [20 Aug]; **baseline = trailing-2yr rolling median 240,325t, as-of 2026-08-21 — TRACKED, not frozen** (per L-13(a) every band call now carries this) | copper QoQ <−5% → 2; conjunction fire (5) needs copper −20% AND inv +100%. ⚠️ **Upside/tightening band ESCALATED to Will 8/21 (L-13(b)) — fails tier test 4; a band shipped on 8/7 evidence would have fired and un-fired inside 9 business days** |
| **I2** | PGMs (platinum / palladium) | **2 🟡** | Platinum **$1,831.00** [close 8/20] — **+6.1% since 8/13**, and **+$105.80 (+6.1%) on 8/19 alone**, tracking the same session as the gold/silver bid. Palladium **$1,336.30**, +1.0% — **Pt is materially outrunning Pd**, which argues bid-side/monetary-adjacent rather than an auto-demand or supply-outage story. **The 8/4 +8% session remains UNEXPLAINED** and this is now a second unexplained Pt surge | supply root (SA/Russia) | Pt **$1,831.00** / Pd **$1,336.30** [closes, 8/20] | confirmed major SA/Russia outage → 4. **No registered trigger fired** |

**Composite: 7/20** *(M1 3 + M2 1 + I1 1 + I2 2). Unchanged from 8/7 — **no score moved this session**, which is the correct consequence of an INDETERMINATE grade.*

**Independence note:** M1 and M2 share the monetary root — **count once.** GSR *falling* while gold is bid means M2 corroborates a **monetary/hard-asset** root, not a risk-off one. I1 tightening is a **separate** (physical/AI-grid) root. **Not a single risk-off shock** — the classic signature is gold UP *and copper DOWN*, and copper is firm.

---

## EXIT / INVALIDATION (standing-rule-vs-state triad)

**Kill rail re-derived: 2026-08-07** *(unchanged this session — MIDAS-07 was a grading frame, not a kill condition; no leg was re-measured, so the stamp is NOT restamped. Per `finding_hygiene_commit_rearms_the_staleness_lie`.)*

| Channel | Standing rule | Current state @ level | FIRED? |
|---|---|---|---|
| M1 (v2) | gold <$3,317 w/o yield spike · WGC Q2 <100t · **gold re-decouples UP 3+wk** *(continuity RULED 8/21: weekly, endpoint — L-12)* | gold **$4,516.30** [8/20], **36.1% above** the $3,317 shelf; **CB Q2 288.9t = 2.89× the 100t line**; **UP-decoupling +8.17% over the registered 3wk vs +9bp DFII10, endpoint basis** | **🔴 FIRED** (leg 3). Legs 1–2 measured and clear |
| M2 | GSR >95 sustained (risk-off) | GSR **68.28**, falling | NOT-FIRED (moving away) |
| I1 | copper −20% AND LME inventory +100% | copper flat **$6.460**; LME **239,925t = −0.2%** vs median, **REVERSED UP +17.1% off the 8/14 trough** | NOT-FIRED — ⚠️ **and per L-13(a) the bands cannot score this direction at all; read as UNSCOREABLE↑, not clear** |
| I2 | major SA/Russia PGM supply outage/sanction | Pd −3.7% off the 8/7 settle, no outage evidence; sanctions priced | NOT-FIRED |

**Fired-count: 1 of 4** *(unchanged).* ⚠️ **Contingent on Will's L-12 escalation:** under the escalated weekly-continuous reading the 7/17→8/7 fire would **NOT** have fired (joint condition **1 of 3** weeks), taking this to **0 of 4**. **I did not make that change** — the DELEGATION_TIER withholds authority *"to grade, resolve, or re-mark a prediction."* Packet sent 8/21.

**Bidirectional flip, restated on corrected figures:** **falsifies the premium-reassertion read** — gold retraces below **~$4,050** (7/31 shelf) while DFII10 holds ≥2.40 ⇒ re-instates v2's "re-coupled/capped" frame, M1 → 2. **Confirms and escalates** — DIVERGE persists past **8/28** (MIDAS-06) or repeats on a rising-yield week ⇒ M1 → 4.

---

## OPEN ON MIDAS (next session)

1. **✅ CLOSED 2026-08-20 — ROW 51 ENCODED.** `MIDAS-06` branch (a) re-keyed `$4,401.30` → **`$4,340.70`**, all three riders discharged, superseded spec preserved verbatim in-cell, encode-confirm delivered to `PROME/inbox/`. `TRADE.md`'s "do not build a card on branch (a)" block **LIFTED**.
2. **✅ CLOSED 2026-08-21 — L-12 and L-13 BOTH RULED** (Will-directed sitting, DELEGATION_TIER, records in `THESIS.md` + digest rows in `AGENTS/SELF_RULINGS.tsv`). **What was ruled = the definitions. What was NOT = the difficulty**, in either direction, because tier test 4 bars both for a spec that is simultaneously a falsifier and a trigger (→ **L-20**).
3. **🔴 AWAITING WILL — five escalated sub-items, all filed 8/21 in one packet.** **L-12:** (e) adopt weekly-continuous 3-of-3 as binding *(24× harder — **and it retroactively un-fires kill-cond #3, fired-count 1/4 → 0/4**)*; (f) a NO-VERDICT band around the yield boundary *(2026 DFII10 σ = 3.42bp; the live gap to 2.40 is 5bp = 1.5σ)*; (g) 5-session smoothed endpoints *(measured **+2.5% easier**)*. **L-13:** (b) a **discriminated** upside/tightening band with a frozen-baseline test window. **Plus:** (h) whether `MIDAS-06` branch (a)'s single-date level conjunction should carry any duration clause at all — **it currently has none**, so one FRED print on 8/28 decides an M1 escalation.
4. **🔴 MIDAS-06 resolves 8/28 — and the binding leg has FLIPPED.** Gold clears the re-keyed $4,340.70 by **+4.0%** [8/20 close]; **DFII10 2.35 fails the ≥2.40 leg by 5bp.** On today's readings it grades **(d) INDETERMINATE**. **Prep only; do not grade early.**
5. **🔴 GOLD COT VINTAGE #2 READS TODAY 8/21** (data as-of Tue 8/18). Last mark net/OI **54.44%** = top-5% of the 1986–2026 record. ⚠️ **SAM's method note applies:** `publicdata.cftc.gov` / `publicreporting.cftc.gov` **do not resolve from this box (DNS failure, not 403)** — use `www.cftc.gov/files/dea/history/`. Exact market-name match, never `like '%GOLD%'`. `cot_gold.py` is the instrument.
6. **🟠 THE 8/19 DIAGNOSIS — first read done, full write-up OWED.** GLD **+3.84%** / gold **+2.83%** while DFII10 **fell 6bp**; at the empirical beta that explains **+0.31%**, so **~89% is unexplained by real rates** ⇒ rates-*assisted*, not rates-*explained*. ⚠️ **But the yield direction was the wrong sign for kill-cond #3's registered wording** — this feeds the premium read *substantively* while firing *nothing* by the letter. Say which, explicitly, and do not blur it.
7. **🟠 NEW — the empirical beta is ATTENUATED ~23% and the bias flatters my own thesis (L-19).** `GC=F` −0.0514 %/bp vs unrolled `GLD` −0.0634 %/bp on identical dates (n=655); the two series' daily returns disagree in **sign on 13.0%** of 5,394 sessions. An attenuated beta **overstates the unexplained "premium" residual.** Neither live conclusion flips, but **every future magnitude call must quote both and name the bias direction.**
8. **🟠 I2 — a SECOND unexplained platinum surge.** Pt **+6.1% on 8/19 alone**, +6.1% since 8/13, materially outrunning Pd (+1.0%). The **8/4 +8% session is still unattributed**. Two unexplained Pt moves in 17 days is a pattern, not noise — attribute or record as permanently unattributed.
9. **📏 N5/L-16 residue + a live proof.** Pt/Pd settlement clocks remain **PROVISIONAL**; **no settlement SOURCE exists for metals in `fetch.py`**. ⚠️ **Clause (ii-b) fired on my own desk 8/21** — a post-roll pull mislabelled the in-flight 8/21 session as an 8/20 close and I published it (see the banner). The fix is a settlement source, not more care.
10. **DAEDALUS SFG actions accepted, not yet built:** (1) `cot_gold.py` must print the as-of verification clause **only when `--expect` actually ran**; (2) extend `boot.py`'s `run_alert` marker test to the metals leg (currently rc-only). Do both **before** relying on the metals leg's green.
11. **NEXUS full-schema revert CONFIRMED** — applies at the next non-time-boxed closeout (Amendment 10: the brief fold is the session's LAST write-back).
12. **Consumer-check follow-through** — corrected base rates (KB-042) reached **SAM** ✅ (answered at primary 8/17, three of four figures moved, correction REINFORCES the RED action item). **BRENT still unconfirmed** (joint-cell table built on P(c)=0).
13. **ZHAO LPR date-fork — day 29, STILL OPEN.** ZHAO STATUS/NEXUS/ZHA-14 carry 7/21 vs the correct 7/20 Beijing. **Do NOT edit ZHAO's files.**
14. **Miner equities OUT OF SCOPE** (ruled 8/14, KB-039). Re-open trigger: miners diverging >20% from the metal over a quarter.
15. **Carryover:** China Cu imports −41.3% base-effect (ZHAO's series); WPIC Pt-deficit PROV; sulfur/acid Platts **spot** print owed (L-14); BOND still owed the term-premium-vs-expected-path answer on 2.47.

## BOTTOM LINE

**MIDAS 2026-08-21: both deferred boundary questions are ruled, and the useful half of the answer is what I was NOT allowed to rule.** L-12 is settled — the duration unit is a week, the basis is endpoint-to-endpoint, and the daily-continuous reading is **excluded on arithmetic**: over 23 years and 5,892 sessions the longest run of gold-up-and-real-yields-up is **four days**, so a 15-day continuous reading has never once been satisfiable. Between the two surviving readings the gap is enormous — **endpoint 19.15%, weekly-continuous 0.79%, a 24× difference** on 1,133 windows — and continuity is a strict subset, so it can only ever un-fire. **On the ruled basis the 7/17→8/7 kill-condition fire stands; on the reading I escalated it would not have fired at all** (the joint condition held **1 of 3** weeks, and while correcting that I found L-12's own text had said 2 of 3, describing the yield leg alone). L-13 split: the matrix now says `UNSCOREABLE↑` where it used to say benign, and the band itself went to Will.

**I ruled the definitions and deliberately did not touch the difficulty, because the tier forbids moving it in either direction — and that turned out to be exactly right.** Kill-cond #3 is both a falsifier of my thesis and my own escalation trigger, so tightening it fails one clause of the anti-self-serving test and loosening it fails the other. I had drafted three genuine improvements before noticing all three were barred — two for being stricter, one for being **+2.5% looser** once I measured it instead of assuming. The concern I raised last night was that ruling a boundary after a favourable tape is tuning-to-tape; **the honest resolution is that the rule I was permitted to write cannot express a preference about the tape at all.**

**The tape, meanwhile, went against two things I have been carrying.** The copper tightening I have reported since 8/7 is **dead** — LME reversed from a −14.7% trough to −0.2% of its median in four business days, a +17.1% restock on flat price, which means a tightening band shipped on 8/7's evidence would have fired and un-fired inside nine business days. And my magnitude instrument is **biased ~23% in the direction that flatters my own thesis**: the beta I quote is estimated on a rolled futures ticker, and the unrolled series is steeper, so I have been systematically overstating the "unexplained premium" residual. Neither conclusion flips, but both numbers were mine and both needed saying.

**What matters next is a five-basis-point gap.** MIDAS-06 resolves 8/28, and the re-key I encoded yesterday is no longer the binding leg: gold clears $4,340.70 by 4%, while **DFII10 at 2.35 fails the ≥2.40 leg by 5bp** — so an M1 escalation now hangs on a single FRED print, on a series that moved 9bp in two sessions, in a spec that has **no duration clause at all.** That is the last thing I sent Will and the one I cannot fix myself. **Gold COT vintage #2 reads today.**

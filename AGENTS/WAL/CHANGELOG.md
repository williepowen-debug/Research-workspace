# WAL THESIS — CHANGELOG

Tracks all changes to `WAL/THESIS.md`. Reverse chronological. Mirrors format of master `../REGINALD/thesis/CHANGELOG.md`.

**Versioning convention:**
- `vX.Y` — major (X) = structural thesis change (vector resolved / disconfirmed / added, framing change, conviction reversal). Minor (Y) = refinement (updated probability, new evidence for existing view, threshold adjustment).
- `vX.Y.Z` — intra-version POV pivot (per [[finding_pov_changelog_pattern]]) — substantive context update that doesn't shift structural vectors but reweights probability or adds material framing.

---

## 2026-08-20 — **SPEC-REPAIR RECORD, NO VERSION BUMP: the four defective rules are repaired or retired. No weight, probability or confidence moved.**

**Deliberately not a version bump, and deliberately a SEPARATE edit from the v2.4 re-mark below it.** Rider R3 (`DELEGATION_TIER`, and the same rider on Will's 8/12 batch) forbids moving a weight in the same edit as a re-spec — so this entry is spec text only. **Zero confidences, probabilities, weights, EV or PT changed here.**

**Authority:** Will, in-session **2026-08-12**, batch ruling — `PROME/proposals/2026-08-12_rule-batch-RULED.md`, WILL_QUEUE rows **32b** (P2/P3/P4/P7) and **32a** (P8/P9, delegated self-rule). ⚠️ *That was a BATCH approval off PROME recommendations: it carries Will's authority but not his individual attention on these rows. I re-read all four on the merits before encoding and found no ground to send any back.*

| # | Rule | Defect | Disposition |
|---|---|---|---|
| **P2** | WAL-01 exit-rule instrument | *"Q3 10-Q Schedule O"* — **Schedule O is a Call Report schedule and does not exist in a Form 10-Q**, and **no 10-Q publishes classified-or-criticized by property type at all** | **RE-INSTRUMENTED** to the Q3-2026 earnings-deck "Classified Assets Mix" slide (A2-visual), + a 10-Q total-classified cross-check + an explicit **NO-VERDICT / INSTRUMENT-ABSENT** band |
| **P3** | WAL-02 invalidation clause | *"≤35bps in BOTH Q2 and Q3"* became **formally unsatisfiable** once Q2 printed 37bps; a Q3 print in 35-40 had **no defined outcome** | **REPAIRED** to Q3-only, exhaustive partition: **>40bps = CONFIRMED · ≤40bps = INVALIDATED** |
| **P4** | Proposed trigger **v2.3.1** | leg (a) names the 10-Q as carrier for **consensus EPS**, which no filing ever carries → **unfalsifiable by construction**; leg (b) **can confirm but cannot disconfirm** | **REJECTED — retired, not repaired.** See below |
| **P8** | MI3 denominator basis | ÷item 4 vs ÷(item 4 + 9) — the choice **inverts the cross-bank rank** | **SPLIT RULING** — my frozen grading basis stays ÷item 4; cross-bank claims use REGINALD's v1a. Self-ruled |
| **P9** | v2.1 calibration **implication column** | *"bear shifts back toward 30%"* would **RAISE total bear (26%→30%) on a DISCONFIRMATION** — a ratchet | **RETIRED**, struck-not-deleted. Self-ruled |

### P4 — why v2.3.1 is REJECTED rather than ratified-with-repair

The ruling offered both. I take reject, for three reasons that compound:

1. **Leg (a) is not merely mis-instrumented, it is MOOT.** The question it asked — was the Q2 print a beat or a meet/miss? — **has already been answered and already priced**: EPS $2.36 vs $2.33 consensus was a beat, and v2.3 folded exactly that into Base 40% on 7/25. Re-pointing the leg at a dated vendor-consensus snapshot would re-grade a question the thesis has already graded.
2. **Leg (b) is a one-way ratchet on Tail.** A live $25M Jefferies counterclaim can only ever *fire* the trigger; the instrument cannot produce the negative, because Note 15's blanket *"routine … not material"* language means **absence cannot distinguish non-existence from immateriality**. A trigger that can confirm but not disconfirm should not be pre-registered.
3. **It was written for a filing that has been read.** The Q2 10-Q landed 7/31 and was read 8/7; the condition was evaluated and **did not fire**. Repairing a spent trigger to keep it alive is the shape of a rule looking for a window.

⚠️ **What survives the rejection, and it is the substantive half:** the Jefferies counterclaim remains a **live watch item** on the FRAUD/ arc and the docket-monitoring mandate — the countersuit is real in secondary sourcing (**KB-WAL-135**, filed ~7/1, $25M Point Bonita deposit freeze, re-verified against public reporting **2026-08-20 with no change**) and is simply **not corroborated by any WAL filing**. **Rejecting the trigger retires the RULE, not the risk.** Base 40% / Tail 7% are untouched by this entry.

### The pattern all four share — and the standing test it earns

**Three WAL rules named an instrument that could not carry their datum** (MI3-is-not-a-10-Q-line, DEWEY 7/16 · "Schedule O" · v2.3.1 leg (a)), and a fourth wrote a partition with a hole in it. These are **unfalsifiable or ungradeable by construction, not merely unmet** — validity and executability are orthogonal axes.
> **Standing rule, adopted here:** before a WAL prediction, exit rule or trigger ships, name the **specific filing, schedule and line** that carries each datum, and confirm that instrument **can** carry it — and write the **NO-VERDICT band** for the case where the instrument is absent. A rule with no named carrier is a family of rules, and the flattering member gets picked after the fact.

---

## 2026-08-07 — **GRADE RECORD, NO VERSION BUMP: V1a MI3 ran for the first time and DISCONFIRMED. No weights moved.**

**Deliberately not a version bump.** This entry records a *pre-registered grade being executed* and one *factual correction*. **No probability, weight, EV or PT changed.** The re-mark this result calls for is a **v2.4 proposal (P7), Will-gated** — see below for why it was not taken here.

**Trigger:** Will registered the FFIEC CDR PWS account 2026-08-07, clearing a blocker that had stood 4+ months. MI3 pulled the same day for **both** available 2026 quarters plus 10 quarters of history (REST/JWT `RetrieveFacsimile`, SDF, ID_RSSD 3138146). Grade → `MI3_FIRST_RUN_2026-08-07.md`; series → `workbook/MI3_SERIES.tsv`.

### The grade (strictly off the frozen v2.1 calibration table, no spec edited before or after)

| Quarter | MI3 (RCON2746 ÷ item 4) | Band | Verdict |
|---|---|---|---|
| **Q1-2026** | **23.88%** | `<24%` | **V1 PLATEAUED** *(12bps below the boundary — near, but unambiguously below)* |
| **Q2-2026** | **21.20%** | `<24%` | **V1 PLATEAUED** *(280bps below — unambiguous)* |

**Concordant across both quarters.** Pre-registered exit rules: **Bear-fast KILL → FIRED** (MI3 <25%, on the exact carrying instrument the rule named). **Bear-fast TIME-BOX → DISSOLVED** (purpose discharged; the ~Sep 1 forcing date is gone).

### What made the grade trustworthy, and what it overturned

- **The 24.2% baseline reproduces exactly** at 12/31/2025 = **24.24%** on the identical basis. Had it not, the correct output would have been a basis dispute, not a verdict.
- ★ **MI3 has never reached 25% in twelve quarters** (all-time high 24.24%, never within **76bps** of its own trigger; the ≥27% hard-confirm band sits 276bps above the all-time high). **The falsifier was not merely un-run — on the actual data it was never close to firing at any point in the observable record.**
- ★ **"Growing" was never a property of this series.** Since 2025Q1 it oscillates in a ~3pp band with no direction. The 2024 rise was two discrete step-changes.
- ★ **`THESIS.md`'s "+8.7pp over 2 quarters" was wrong by 3×** — the span is **six** quarters. Levels reproduce, interval does not. **Corrected in THESIS.md this session as a factual fix (P10); no weights touched.**
- **Q2's numerator fell in absolute dollars** (−$175M / −6.4% over two quarters) while C&I grew — the decline is substantive, not denominator dilution.

### ⚠️ Why NO re-mark was taken here

The frozen table's **status** column graded cleanly. Its **implication** column did not survive the version change: for `<24%` it reads *"bear shifts back toward 30%"*, written against **v2.1→v2.2** when "the bear" was a *single* weight. Under **v2.3** the bear is **split** (fast 10% + medium 16% = 26%), so applying it mechanically would **RAISE** total bear weight on a **disconfirming** result — plainly the wrong sign. Executing that would have been improvisation dressed as a frozen grade.

**→ v2.4 proposals, all Will-gated, none applied:** **P7** retire or fold bear-fast (recommend folding into bear-medium or a material cut; total bear must **not** rise on a disconfirmation) · **P8** repair the MI3 denominator spec (RCON2746 spans items 4 **and** 9; the spec divides by item 4 only — ⚠️ re-basing changes the *level*, never this verdict: both bases are far below 25% in both quarters) · **P9** retire the calibration table's implication column, keep its status column as the calibration record.

⚠️ **Scope fence carried into every surface: V1a ≠ V1.** MI3 measures CRE **not secured by real estate**. The $99M, the office book, the classified balance and the appraisal are in the **secured** book, untouched — and the same-day Q2 10-Q read *added* evidence to V1b-magnitude (OREO office property count 15 → 22). **Do not read "V1a disconfirmed" as "V1 disconfirmed."**

---

## v2.3 — 2026-07-25 — **POST-Q2 SECOND-DATA-POINT RE-MARK. The bear WEAKENED and the margin of safety COMPRESSED.**

**Trigger:** WAL Q2 2026 print (8-K acc **0001628280-26-049001**, AMC 7/21; call 7/22 noon ET), graded in two stages against a frame frozen 7/10-7/20 → `../REGINALD/reports/2026-07-21_WAL_Q2_grade.md`, `../REGINALD/reports/2026-07-22_WAL_Q2_stage2_grade.md`. **Verdict: NOT the surprise tier, NO FIRE.** This entry is the deferred re-mark those grades scheduled.

### Old view → new view

| | v2.2.1 (6/8) | **v2.3 (7/25)** |
|---|---|---|
| Bear-fast (V1 MI3) | 12% | **10%** |
| Bear-medium (V1 Office migration) | 25% | **16%** |
| Base | 35% | **40%** |
| Bull | 21% | **27%** |
| Tail | 7% | **7%** |
| Base range | $70-77 | **$74-82** |
| Bull range | $82-90 | **$86-94** |
| **EV** | **$68.93** | **$73.92** |
| **Overvaluation (÷EV)** | 18.8% *(at 7/17 spot $81.88)* | **12.4%** *(at 7/24 spot $83.11)* |
| **PT range** | $50-68 | **$52-74** |
| PT convention | *unwritten (had drifted $52-70 → $50-68)* | **PINNED: [Bear-fast range low, EV]** |
| B1 ($99M life-sci) | FIRED, disposition unknown | **Disposition (B) — nonaccrual, $0 C/O, brought CURRENT end-June** |
| Pass-grade-walk pattern | N=1, watching for #2 | **still N=1 — 0 new office migrations in Q2** |
| REG-26 | 33% OPEN | **RESOLVED — DISCONFIRMED** |
| REG-24 / REG-25 | 65% / 72% | **25% / 50%** (both OPEN to Q3 10-Q) |

### Why — each weight change tied to a graded Q2 fact
- **Bear-medium 25→16 (the load-bearing cut).** The *broadening* mechanism took the most direct hit available: REG-26 disconfirmed; the $99M loan went to nonaccrual with **$0 charged off** and was **brought current end-June** (prospective tenant for a sizable piece; NOT one of the Investor-Day six); **0 new office migrations**; office classified **$316M** vs the $407M baseline (visual-confirmed, EX-99.2 slide 12); SM **−$87M / −22%** to $316M. **Not cut to zero** because the *magnitude* mechanism is deferred, not dead — see "what keeps it alive."
- **Bear-fast 12→10.** No new evidence: **MI3/FFIEC PDD still has not run** (~2.5 months overdue; DEWEY 7/16 established MI3 is not a 10-Q line, so only FFIEC resolves it). The 2pp trim rests only on two consecutive quarters of a **shrinking** office/CRE book with no confirmation — weak evidence, small move. Mechanism untouched.
- **Base 35→40.** Print landed base-case: EPS **$2.36** beat ($2.33 cons), NIM **3.53% flat**, ex-fraud NCO **37bps** (inside the 25-40 NEUTRAL band), AOCI −$451M **improved +$5M QoQ**, CET1 11.0%.
- **Bull 21→27.** Capital-return pivot ($5B loan guide cut *"to prioritize share repurchases"* + **$150M H2 buyback**), NII floor raised to **12-14% while absorbing an assumed Sept 25bp HIKE**, "C/O peaked" + H2 NPL-decline path (3-4 of the six resolving Q3), deposit cost inflecting (Q2 avg 1.78% −3bps, June exit 1-2bps below avg).
- **Tail 7 flat.** Cantor drew **zero** call mentions and no new Q2 charge-off; LAM/Jefferies is live litigation with no Q2 datum.

### ★ First range edit since v2.1 — and why it is NOT spot-chasing
Ranges were deliberately frozen v2.1→v2.2.1 on the rule "no structural vector change drives range edits." Q2 supplied two genuine **earnings-base** changes (NII floor raise *inclusive of a hike assumption*; buyback funded by a loan-guide cut = fewer shares + a stated per-share-over-growth priority), so Base/Bull lift. **Deliberately not lifted to spot:** at $83.11 the stock trades **above** the new Base top of $82, so my base case still implies a decline. Offsets explicitly carried, not ignored: fee guide **cut** 20-25%→13-17%, deposit guide **cut** $8B→$6B, ACL/NPL **<100% (96%)**. Bear and Tail ranges unchanged — only their probabilities moved.

### ★ The honest headline
**Overvaluation went 18.8% → 12.4%.** That narrowing is **not** the tape: **EV rose $4.99 (+7.2%) while price rose $1.23 (+1.5%).** It compressed because I re-weighted against a non-confirming print, which is the correct direction. WAL is still overvalued against my EV — by materially less — and the Sep $67.5P/$70P core now sits further from an EV-justified strike than it did pre-print. **No position action taken or recommended here** (rule #4/#5 — TERRY + Will [Approve] + live chain).

### What keeps the bear alive at 16%
The **$99M appraisal is still not in** (Vecchione verbatim: *"we haven't got the appraisal in"*) and a low mark forces a charge-down onto the REG-25 >40bps path · **ACL/NPL coverage 96%**, below 100% · **CRE-NOO gross charge-offs at a 5-quarter high $32.0M** (channel active but diluted in a $58.7B book — reservoir-grind signature) · **V1 MI3 never tested**. Resolution moves to the **Q3 10-Q + the appraisal**. Grind **INTACT-but-NARROWED** to the residual office tail.

### Cohort context — Hyp A re-confirmed twice more since 6/8
Hyp A (genuine cohort improvement) **stands** and is now corroborated by two further independent reads: WALTER **SIG-723-016** Q2 regionals mosaic (cohort improving with fat idiosyncratic tails — EFSC/MCB blowups vs TCBI/RF/HBAN/SYF improving) and my own **7/25 FL small-tier watch-card fill** (BKU/AMTB/SSB **3-of-3 REVERT** → the CRE-DQ creep does **not** broaden tier-wide). The WAL bear remains **idiosyncratic**, which v2.3's shape reflects.

### ⚠️ SCOPE BOUNDARY — documented divergence, NOT silent rot
v2.3 covers **THESIS.md · SCENARIOS.md · PREDICTIONS.tsv re-grades · this CHANGELOG** and the live consumer surfaces (STATUS, WAL/STATUS, NEXUS_BRIEF, thesis/THESIS).
**It deliberately does NOT touch `INDEX.md` or `WEAKNESSES.md`** — both fold into the `AGENTS/WAL/` standup (PROME **WP-W2**) by explicit sequencing instruction (Will 7/25; DAEDALUS 7/22 ruling #5) so they are not rewritten twice days apart.
**→ Handoff list for WP-W2 — these files still carry v2.2.1 values and MUST be swept there:**
| File | Carries (stale) | Should become |
|---|---|---|
| `WAL/INDEX.md` | v2.2.1 · EV $68.93 · PT $50-68 · Bear-med 25 | v2.3 · EV $73.92 · PT $52-74 · Bear-med 16 |
| `WAL/WEAKNESSES.md` | v2.2.1 references | v2.3 (+ V1 MI3 still-unrun status) |
*Also still owed at the standup: strike-by-strike position architecture rebuild (SCENARIOS' May-vintage sections), `MARKET/TRADE_LOG.md` phantom-strike banner, KB.tsv Q2-ingest.*

---

---

## 2026-07-22 — Q2 STAGE-2 (post-call): scheduled REG-24/25 re-grades — 65→25% / 72→50%; no version bump

**What changed (probability re-grade only — structural vectors untouched, zero grading thresholds moved):**
- **REG-24 65%→25%** — office-classified $316M (28% of $1,128M classified assets, slide-12 VISUAL confirm off EX-99.2 images; Q1↔Q2 mix-label ambiguity resolved — Q2's 38% segment is C&I) and FALLING from the $407M baseline; zero new office migrations on the 7/22 call (§3 not triggered); office criticized in TOTAL is $485M < the $500M line; H2 six-loan NPL-resolution path reduces the stock. Residual = pending $99M appraisal + $946M 2026 office maturity wall + 37%-criticized CLD/lease-up slice.
- **REG-25 72%→50%** — Q2 window spent NEUTRAL (37bps, Stage-1 7/21); FY 25–35bps guide reaffirmed with H2 "a little above midpoint"; mgmt declared charge-off dollars+rate "peaked." Held at coin-flip (not lower) because Q1 39/Q2 37 run just under the 40 line and Q3 contains live realization events (the pending $99M appraisal; 3–4 of the six NPL resolutions closing in Q3).
- **W5 disposition letter FINAL: (B)** — $99M life-sci loan in nonaccrual, $0 charged off; thesis grade AMBIGUOUS-lean-BEAR stands. New call color softens within-band: borrower brought the loan CURRENT end-June + prospective tenant; appraisal still pending (the live Q3 mark risk); NOT one of the Investor-Day six; ACL/nonaccrual coverage dipped to 96%.
- Record: `../REGINALD/reports/2026-07-22_WAL_Q2_stage2_grade.md`. This session ran the drift-grep at close (lesson from the 7/16→7/17 fossilization).

**Old view → new view:** REG-24/25 at 65/72 → **25/50**; REG-26 stays RESOLVED/DISCONFIRMED (7/21); Bear-med 25 / EV $68.93 / PT $50-68 / v2.2.1 UNCHANGED — **v2.3 re-mark is the next scheduled pass** (pre-cutover lane per DAEDALUS 7/22, deliberately not done at Stage-2).

---

## 2026-07-17 — RETRO-ENTRY (audit catch): 7/16 REG-24/25 re-grade + 7/10 date-fix, logged late

**What changed (no version bump — probability re-grade + hygiene, structural vectors untouched):**
- **7/16 (teams-spawn): REG-24 70→65%** (DEWEY prompt-13 un-blind: classified FLAT $947M, SM +24% to $403M but no conversion; office not separately tagged; base rate on aggregate criticized surges reverts; benign 7/14-16 cohort) and **REG-25 75→72%** (NCOs lag + cohort NCO decelerating hard [MTB 0.23%/WFC 0.34%]; held high by the two-window Q2-OR-Q3 structure + the $99M idiosyncratic leg). Written to PREDICTIONS.tsv same-day but **the closeout drift-grep was skipped**, leaving 70/75 fossilized in 8+ display surfaces (this file's tracked THESIS.md included) until the 7/17 audit swept them. REG-26 (33%, the >55bps+charge-off surprise) was registered 7/10.
- **7/10:** print-date corrections (Jul-30/late-Jul → confirmed Tue Jul 21 AMC) touched THESIS/SCENARIOS without entries — logged here retroactively.
- **7/17 audit:** phantom "Sep $77.5P" corrected across THESIS/SCENARIOS/STATUS (canonical Sep core = $67.5P+$70P per POSITIONS.md); SCENARIOS EV-spot staleness bannered ($80.15 [6/5] → $81.88 [7/17], overvaluation 16.3%→~18.8% at live spot, EV re-marks at the print).

**Old view → new view:** REG-24/25 at 70/75 → **65/72**; everything else unchanged (Bear-med 25, EV $68.93, PT $50-68, v2.2.1).
**Lesson:** probability changes REQUIRE the drift-grep + a changelog entry at the changing session, not at the next audit (repeat of the 6/2 propagation finding).

---

## 2026-06-08 (PM) — v2.2.1 intra-version: COHORT SIGNAL RESOLVED → HYPOTHESIS A (NCO decomposition)

**Author:** REGINALD (Will-directed, Orchestrator-reviewed) | **No version bump** — evidence resolution of the open question v2.2.1 (AM) explicitly held open; no weight/EV/PT/prediction change.

**Trigger:** Executed the queued ZION/CFG/MTB/FITB Q1 NCO decomposition (full record `research/COHORT_NCO_DECOMP_2026-06-08.md`). 5 parallel EDGAR pulls; decisive NCO ratios + all 5 NPA deltas re-verified by REGINALD self-curl.

**Old view (AM v2.2.1):** Cohort signal AMBIGUOUS — 3 hypotheses (A genuine / B cosmetic / C mixed) all consistent with NPA-only data; "sharpen to WAL-specific" framing held OPEN as unforced narrowing; master STATUS "12/12 cohort fade intact" QUALIFIED.

**New view (PM):** **Hypothesis A — genuine cohort improvement.** ZION/CFG/MTB all GENUINE (NPA ↓ AND NCO flat-to-falling, reserve builds/credit-healing release); FITB CONFOUNDED-excluded (−24bp NPA is Comerica-acquisition denominator artifact, NPA $ flat, NCO flat YoY; the $178M "asset-backed finance"/Tricolor charge-off was Q3'25 not Q1'26); EGBN COSMETIC-outlier (NCO doubled +89bp, confirmed exact). Tally: 3 genuine + 1 confounded + 1 cosmetic-outlier. The "cohort doing the EGBN trick" worry is REFUTED.

**What it changes:** (1) "sharpen to WAL-specific" framing now **EARNED by data** — WAL bear stands on idiosyncratic legs (Office/B1/MI3/Curley), loses broad-cohort tailwind; (2) Bear-medium **stays 25, NO revert toward 30** (revert was the Hyp B path; Hyp A confirms the trim); (3) "12/12 cohort fade intact" **RETIRED** (contradicted on NCO line). **UNCHANGED:** EV $68.93, PT $50-68, REG-24 70% / REG-25 75%, all positions. Pre-registration note: the classification rule was fixed before data and the result *inverted* the working prior (Hyp B) — discipline check passed.

**Steelman carried:** Q1 snapshot, $875B 2026 maturity wall ahead (re-openable Q2/Q3); MTB releasing CRE reserves hard into the wall; decomposes NCO/NPA not leading buckets; crowded-short-unwind risk ticks up if WAL bear is purely idiosyncratic (print-day flag).

---

## 2026-06-08 — v2.2.1: NIM-TAILWIND DOUBLE-STACK SOFTENING + COHORT CONTEXT AMBIGUOUS (BOARD-batch audit + Orchestrator review)

### THESIS Updated → v2.2.1
**Author:** REGINALD (with Will approval, Orchestrator-reviewed)
**Trigger:** BOARD backlog drain 5/11-6/6 (108 disposition rows appended) + director-level audit catching 3 misclassifications + Orchestrator review catching 2 errors and 2 sharpens in initial draft. Three BOARD signals promoted INFO_ONLY → WOULD-INTEGRATE on 2nd-pass audit (Phase B): SIG-W-20260521-010 (20Y auction clean), SIG-W-20260522-005 (Waller pivot), SIG-W-20260511-030 (cohort counter-evidence). Plus one signal that does NOT trigger promotion: SIG-W-20260511-025 (KREF Boston life-sci REO — mechanism distinct from WAL B1 pass-grade-bank-walk).

**Why v2.2.1 not v2.3:** refinement only. NO structural vector change. B1 fire / V4 Curley / V1 MI3 pending / leading-bucket migration / V2 inventory CLEAN / V3 cohort-median CONFIRMED — all stand. PT range $50-68 UNCHANGED. REG-24 (70%) / REG-25 (75%) UNCHANGED.

**Why v2.2.1 not v2.2 minor edit:** Per [[finding_pov_changelog_pattern]] intra-version POV pivots get logged as dated x.y.z. Macro-tailwind reweight + cohort sharpening attempt + life-sci mechanism distinction = three substantive POV updates worth versioning.

### What changed

**MACRO-NIM TAILWIND — DOUBLE-STACK SOFTENING (NEW section in THESIS.md):**
- 5/20 20Y Treasury auction PRINTED CLEAN (0bp tail / BTC 2.55 / Indirect 67.7% per SIG-W-20260521-010) — foreign UST demand robust at price; BOND demand-hole thesis materially weakened.
- 5/22 Waller "easing bias removal" pivot at German economic forum (SIG-W-20260522-005, REGIME-SHIFT ANCHOR) — futures repriced ~2-in-3 hike by October FOMC, modal flip from cut-by-year-end. Direct quote: "Inflation not headed in the right direction."
- Combined: bank NIM compression mechanism materially softer than v2.2-ship assumed.

**5pp Bear-medium trim rests on LOSS-ABSORPTION CHANNEL ONLY** (per Orchestrator sharpen, accepted in full):
- Loss-absorption (TERMINAL effect, INCLUDED in weight cut): higher PPE buffer raises credit-event magnitude required to cross Bear-medium $58-66 range.
- Recognition-delay (TIMING effect, NOT included in weight cut): already handled by existing Sep-dated positions (Sep $77.5P / Sep $70P) spanning late-July Q2 print. Including timing in weight when handled by tenor = double-counting delay against positions already paid for the window.
- This framing is the substance owed to PROME for Jun 18 cluster bank-trigger calibration reply.

**COHORT CONTEXT — AMBIGUOUS PENDING NCO DECOMPOSITION (NEW section in THESIS.md):**
- SIG-W-20260511-030 reports 5/10 peer banks NPA-improving Q1 YoY (ZION -3 / CFG -11 / MTB -25 / FITB -24 / EGBN -48bp).
- EGBN has explicit NCO data: NCO +89bp YoY despite NPA improvement = COSMETIC (resolution-via-charge-off, not credit healing).
- ZION / CFG / MTB / FITB have NPA-only data in signal. **Three hypotheses (A: genuine improvement / B: cosmetic resolution / C: mixed) all currently consistent with available data.**
- v2.2.1 does NOT lock "sharpen to WAL-specific" framing — would be unforced narrowing without NCO decomposition.
- 5pp Bear-medium cut does NOT rest on cohort framing (rests on loss-absorption only).
- Research queued: pull Q1 NCO data for ZION/CFG/MTB/FITB to resolve hypothesis.
- Master STATUS "cohort fade pattern 12/12 intact" claim QUALIFIED 6/8 — do not propagate without ambiguity note.

**LIFE-SCI SECTOR SIGNAL — PASS-GRADE-BANK-WALK PATTERN STILL N=1 (V1 addendum in THESIS.md):**
- 3 life-sci distress events in 6mo across cohorts: WAL $99M (bank loan / strategic walk on PASS-graded) + KREF Boston (mREIT TAKING REO on known-impaired) + OZK IQHQ (forward maturity test).
- **KREF Boston is NOT a 3rd instance of WAL B1 mechanism.** Different position in capital stack, different recognition mechanism.
- Sector signal real (life-sci collateral impairing across cohorts) but WAL B1 pass-grade-bank-walk pattern remains **N=1**.
- v2.5/v3 promotion requires: (a) another BANK loan with previously-pass-graded sponsor walking, OR (b) same-mechanic event at OZK (IQHQ Aug if pre-maturity walk) or EGBN.

**Probability re-weight (v2.2 → v2.2.1):**
- Bear-fast: 12% → **12%** (unchanged)
- Bear-medium: 30% → **25%** (-5pp, loss-absorption channel only)
- Base: 33% → **35%** (+2pp, NII tailwind benefit)
- Bull: 18% → **21%** (+3pp, Waller no-cut implication)
- Tail: 7% → **7%** (unchanged)

**EV: $67.98 → $68.93** (+$0.95, modest bullish drift).

### Overvaluation convention — PINNED 2026-06-08 (per Orchestrator catch)

Hard error caught by Orchestrator: prior drafts mixed ÷EV and ÷Price denominators. v2.2 was reported "~15% over" using ÷EV; v2.2.1 initial draft reported "~14% over" using ÷Price — concealing a directional move.

**Convention pinned: Overvaluation = (Price − EV) / EV.** All historical and forward figures normalized to this denominator.

| Version | Price | EV | Overvaluation (÷EV) |
|---------|-------|-----|----------------------|
| v2.2 (5/21) | $77.63 | $67.98 | **14.2%** |
| v2.2.1 (6/8) | $80.15 | $68.93 | **16.3%** |

**Gap WIDENED ~2pp** (price rose $2.52 / +3.2% vs EV rose $0.95 / +1.4%). Directionally **bear-supportive** — more room to fall, even after Bear-medium trim. Notable because it cuts against the net-trim narrative of v2.2.1; honest accounting requires acknowledging.

### Old view vs new view

| Element | v2.2 | v2.2.1 |
|---|---|---|
| Macro-NIM tailwind | implicit (BOND demand-hole + Fed-cut assumed) | EXPLICITLY softened (20Y clean + Waller pivot) |
| Bear-medium prob | 30% | **25%** (loss-absorption channel only) |
| Recognition-delay handling | implicit in weight | EXPLICITLY excluded from weight (handled by Sep tenor) |
| Cohort framing | implicit "regional bank cohort stress" | **AMBIGUOUS** — held open pending NCO decomp; 3 hypotheses |
| Life-sci pattern | "two Class-A walk-aways = sector signal" | "Sector signal yes; pass-grade-bank-walk N=1; KREF mREIT-REO distinct" |
| EV | $67.98 | $68.93 |
| Overvaluation (÷EV) | 14.2% | **16.3% — WIDENED ~2pp** |
| Master STATUS 12/12 | propagated | QUALIFIED 6/8 |

### Position implications

**UNCHANGED.** Sep core (Sep $77.5P / Sep $70P) still positioned for late-July Q2 print. Jun 18 cluster still requires its own decision window (~6/11). No new position adds/cuts triggered by v2.2.1. The substance of the PROME reply on Jun 18 cluster IS the loss-absorption-vs-tenor framing established here.

### Open research from v2.2.1

1. **ZION / CFG / MTB / FITB Q1 NCO decomposition** — resolves cohort hypothesis A/B/C. Until resolved, do NOT propagate "cohort fade refuted" or "broad regional cohort stress" without explicit ambiguity note.
2. **OZK IQHQ Aug maturity** — next discrete event window for confirmation/denial of pass-grade-bank-walk pattern. Pre-maturity sponsor walk = hard 2nd instance.
3. **FFIEC PDD MI3 bulk integration** — V1 primary falsifier still pending; calibration table preserved from v2.1.

---

## 2026-05-21 — v2.2: B1 FIRED via $99M LIFE-SCIENCE OFFICE WALK-AWAY + CURLEY RESIGNATION (post 10-Q drill)

### THESIS Updated → v2.2
**Author:** REGINALD (with Will approval; full V2.2 ship per session direction)
**Trigger:** WAL Q1 2026 10-Q drill (EDGAR accession `0001628280-26-033054`, filed 2026-05-11; drilled 2026-05-21 — 10-day integration lag). Drill findings: `research/WAL_10Q_DRILL_2026-05-21.md`. Market awareness check confirmed ~10% week-of drawdown (5/11-5/15) on combined 10-Q + Curley news per Simply Wall St (5/14) + DA Davidson PT cut $93→$90 (5/13, Buy maintained).

**Why v2.2 not v2.1.1:** Two bear-buckets fired (B1 + B3) per the V2.1 calibration framework. B1 = "first material Office credit walking away" — fired via $99M life-science strategic default. B3 = mgmt held NCO guide despite Q1 ex-fraud 39bps (fired at Investor Day 5/12 per `WAL/INVESTOR_DAY_FINDINGS_2026-05-12.md`). Single-bucket fire would have been v2.1.1 minor revision; compound 2-bucket fire is major-version threshold.

**Why v2.2 not v3.0:** Thesis framing ("compounder with concentrated CRE tail risk") is STRENGTHENED, not replaced. Tail is *actualizing*, not *invalidating thesis* — V2.2 is the actualization milestone, not a thesis pivot. V1 MI3 primary falsifier still hasn't run; V2 inventory test came back CLEAN; V3 cohort-median CONFIRMED via 10-Q breakout. Structure intact; speed accelerated.

### What changed

**Core framing:**
- **v2.1:** *"WAL is a structural compounder with concentrated CRE tail risk AND an active V1 hidden-CRE test pending mid-May FFIEC MI3 print."*
- **v2.2:** *"WAL's concentrated CRE tail risk is actualizing on Q2 timeline. The 10-Q subsequent-event disclosed a $99M life-science office sponsor walk-away (B1 fired) on a loan previously graded pass. Same week, Chief Banking Officer Curley resigned. Bear-slow → Bear-medium speed."*

**V1 (Hidden CRE / Office):** weight restored pending MI3 → **OFFICE SUB-VECTOR FIRING**
- $99M Class-A LEED Silver life-science laboratory/office building, "gateway life-science market" — borrower notified WAL of intention not to repay. Pass → substandard / non-accrual.
- Same strategic-default mechanic as IQHQ (OZK Aug 2026 maturity) — two Class-A life-science walk-aways across watchlist in 6 months = sector signal.
- 10-Q confirms leading-bucket migration already firing in Q1 pre-event: Other CRE-NOO nonaccrual $228M → $263M (+$35M / +15.4%).
- MI3 primary falsifier (≥25% FFIEC PDD) STILL HASN'T RUN — V2.1 calibration table preserved; bulk window 5/14-16 passed without integration.

**V2 (Jefferies/MFS fraud chain):** STANDS + counterparty-discount → **INVENTORY TEST CLEAN**
- 10-Q lists only LAM ($126.4M) + Cantor V ($26.1M) — no new Leucadia-era credits. Bucket A (Investor Day prep framework) confirmed U1.
- NEW: WAL escalated to active litigation against Jefferies Financial Group + LAM + affiliates in NY Supreme Court (March 2026) — breach of contract + fraudulent inducement.
- Q1 collateral defense: $13M non-performing senior lien loan purchased; plans more.
- $3.5M specific allowance remains on Cantor loan.

**V3 (SSFA / NDFI):** stands disconfirmed → **CONFIRMED via 10-Q breakout**
- Total NDFI $14.928B = 25.2% of HFI loans (cleaner disclosure than deck Slide 24).
- Mortgage credit intermediaries $10.25B (17.3%) / Business credit intermediaries $3.42B (5.8%) / PE funds $1.26B (2.1%).
- Business + PE = 7.9% ties to deck Slide 24's "7% Ex-Mtg Credit, peer median 6%, avg 8%" — cohort median holds.
- Zero mentions of Atlas SP, PennyMac, PFSI, LoanDepot, Apollo as counterparties — silence on non-bank servicer concentration consistent with deck.

**V4 (NEW): Mgmt credibility / org stability — CURLEY RESIGNATION**
- Stephen Curley, Chief Banking Officer for **National Business Lines** (the org where Office / Hotel Franchise / Tech & Innovation / Mortgage Warehouse / Public Finance / Renewable Resources all sit), resigned effective immediately, same week as 10-Q.
- Stated reason: CEO opportunity at another financial services firm.
- Pattern flag, tracked — not promoted to standalone bear-trigger without a second corroborating departure. Same-week-as-disclosure timing matters even if causal link is denied by company.

**Probability re-weight (v2.1 → v2.2):**
- Bear-fast: 12% → **12%** (unchanged — MI3 calibration still governs)
- Bear-slow → Bear-medium: 23% → **30%** (+7pp — B1 fired, multi-quarter migration started)
- Base: 35% → **33%** (-2pp — base loses to bear-medium realization)
- Bull: 23% → **18%** (-5pp — "largely behind us" narrative materially eroded by $99M + Curley + drawdown)
- Tail: 7% → **7%** (unchanged — tail rationale not disturbed by v2.2)

**EV: $70.50 → $67.98** (-$2.52). Current $77.63 → ~14% overvaluation (vs v2.1's 13% at $81.90; drawdown -5.2% offset by EV drift -$2.52).

**PT range adjustment (v2.1 $52-70 → v2.2 $50-68):**
- Bear-medium range $60-68 → $58-66 ($2 floor compression — Q2 print is second test, $58 more reachable)
- Bull range $84-92 → $82-90 ($2 compression each end — mgmt-credibility flag tightens upside)
- Bear-fast / Base / Tail ranges unchanged

**Predictions ratchet:**
- REG-24 (Office classified > $500M by Q3 2026): **60% → 70%**. Driver: $377M Q1 classified + $99M life-science moving = $476M Q2 start; one more $50M migration crosses threshold.
- REG-25 (ex-fraud NCO > 40bps in Q2 OR Q3): **55% → 75%**. Driver: $99M at 60% LGD = ~$60M Q2 charge-off = ~10bps incremental; Q1 was 39bps; mechanical cross before any normal Q2 activity.

### Old view vs new view

| Element | v2.1 | v2.2 |
|---|---|---|
| Bear narrative | "Wait for Q2-Q3-Q4 Office migration" | "First migration disclosed; expect more in Q2 print" |
| REG-25 confidence | 55% (Q1 39bps tension; mgmt held guide) | 75% (single-credit $60M Q2 charge-off near-locks 40bps) |
| Bull plausibility | 23% ("largely behind us" + V2 resolution) | 18% (narrative eroded by post-quarter $99M + Curley) |
| Multi-quarter speed | Bear-slow | Bear-medium |
| Mgmt credibility | Counterparty-diligence discount on forward statements | V4 vector added; pattern flag on org stability |
| Market positioning | Asymmetric entry available pre-event | Already 10% priced in via 5/11-5/15 drawdown |

### Position implications

- **Sep $77.5P / Sep $70P:** REINFORCED-HOLD core. Sep window catches Q2 print (late July) — exactly where V2.2's $99M materializes as charge-off + REG-25 hit.
- **Jun $85P:** HOLD as event hedge — most v2.2 evidence already in tape; Jun catalysts slimmer (FFIEC PDD if integrates; AOCI rule comment close).
- **Jun $65P / $67.5P / $77.5P:** HOLD — Jun expiry tactical; v2.2 doesn't change Jun math materially.
- **Sep $67.5P:** REINFORCED-HOLD — adds deeper-OTM Sep coverage; cheap leg of the Sep core.
- **No new positions** — asymmetric entry compressed by 5/11-5/15 drawdown. Structure correct, don't chase.

### Falsifier status

- **B1 (first Office credit walking away):** ✅ FIRED ($99M life-science)
- **B3 (mgmt held NCO guide despite Q1 39bps):** ✅ FIRED (Investor Day 5/12)
- **V1 MI3 ≥25% (V2.1 fast-trigger):** ⏳ Still pending FFIEC PDD integration
- **V1 MI3 24.0-24.9%:** ⏳ Same
- **V2 inventory (2+ Leucadia-era credits):** ❌ NOT FIRED — 10-Q clean (U1)
- **Hotel sub-portfolio migration:** ❌ NOT FIRED — Q1 Hotel classified $44M / 1.0%, still light
- **Q2 print SECOND material Office migration:** ⏳ Pending late July

If Q2 print shows the $99M is the ONLY material Office migration, V2.2 may overstate and bear-medium probability should pull back. If Q2 shows 2+ Office migrations, we're in V2.5/V3 territory and bear shifts toward 40%+.

### Files updated

- `WAL/THESIS.md` v2.2 (header + new V2.2 core thesis block + vector status table + V1 Office expression section + Curley section + predictions + watch dates + PT range + footer)
- `WAL/SCENARIOS.md` v2.2 (header + new EV summary + v2.1 preserved + position-level read expanded to 8 positions + footer)
- `WAL/CHANGELOG.md` v2.2 (this entry)
- `workbook/PREDICTIONS.tsv` (REG-24 60→70%, REG-25 55→75% — step 4d pending)
- `research/WAL_10Q_DRILL_2026-05-21.md` (drill findings, ~280 lines)
- `POSITIONS.md` (May 15 cluster cleared; WAL position count 8→7; v2.2-pending flag added → cleared)

---

## 2026-05-11 — v2.1: V1 WEIGHT RESTORED PENDING MI3 + EV MATH MADE JUN-CONDITIONAL (post RED CHG-RED-025 OVER-CORRECTED)

### THESIS Updated → v2.1
**Author:** REGINALD (with Will approval; full V2.1 ship per session direction)
**Trigger:** RED formal challenge CHG-RED-025 (2026-05-06) — WAL V2.0 stress-test verdict OVER-CORRECTED (~26% aggregate weighted PASS across 6 methods). Source: `AGENTS/RED/research/WAL_V20_STRESSTEST.md` (415 lines). REGINALD response: `WAL/V21_RESPONSE_TO_RED_CHG_025.md` (substantive engagement on M1-M6).

**Why v2.1 not v3.0:** Incremental refinement; V2.0's structural ships (V2 fraud resolution + Office single-point concentration) STAND. Two corrections required: (a) V1 weight restored pending MI3 mid-May print — V2.0 demoted V1 before V1's primary falsifier ran (M2 ACCEPT); (b) EV math made Jun-conditional — V2.0 credited Jun 18 puts with multi-quarter unconditional payoff (M4 ACCEPT). Plus secondary refinements per M3/M5/M6 partial accepts.

### What changed

**Core framing:**
- **v2.0:** *"WAL is a structural compounder with concentrated CRE tail risk. Short thesis depends on tail actualizing or market re-rating the concentration."*
- **v2.1:** *"WAL is a structural compounder with concentrated CRE tail risk AND an active V1 hidden-CRE test pending mid-May FFIEC MI3 print. V1 weight restored to bear stack pending test; Office single-point is an additional sharpened V1 expression, not a replacement for the MI3 ratio trajectory test."*

**V1 (Hidden CRE):** demoted to "Office single-point" → **WEIGHT RESTORED PENDING MI3 TEST + Office sharpening additive**
- V2.0's V1 demotion was premature — V1's primary falsifier (MI3 ≥25%) hadn't fired. Per RED M2 ACCEPT, methodologically I shouldn't have reframed V1 before the test ran.
- V2.1 splits Bear into Bear-fast (12% — MI3 ≥25 triggers V1-fast cycle) + Bear-slow (23% — V1 Office migration via REG-24/REG-25).
- MI3 calibration table added per RED §12.1 widened: ≥27% V1 hard-confirmed; 25.0-26.9% V1 acceleration; 24.0-24.9% trajectory bending; <24% V1 plateaued.
- Office single-point data (Slide 12 38%/9.5x + Slide 23 $946M maturity wall) retained as STRUCTURAL additive evidence, not as V1 replacement.

**V2 (Jefferies/MFS fraud):** RESOLVED → **STANDS + counterparty-diligence discount applied to mgmt forward-statements**
- V2 publicly resolved in 8-K STANDS (no change).
- Per RED M5.6 ACCEPT: Vecchione "largely behind us" + "past peak stress" mgmt statements receive counterparty-diligence discount given LAM was 2x stated $60M top-commitment / Janet Lee Q&A refusal on >$100M exposures / First Brands + Tricolor silent.
- Investor Day May 12 becomes explicit mgmt-credibility test per RED §12.4.

**V3 (SSFA / NDFI):** directionally disconfirmed → **STANDS + V3 cohort ≠ V1 cohort distinction explicit**
- Per RED M3 PARTIAL ACCEPT: Slide 24 NDFI cohort comparison (V3) is NOT a proxy for MI3 cohort comparison (V1). Different lines on the Call Report.
- WAL anomalous on MI3 trajectory (15.5 → 24.2 = +8.7pp fastest in cohort) survives V3 NDFI-at-median finding.

**Probability re-weight (v2.0 → v2.1, partial reversal):**
- Bear: 30% → **35%** (split: Bear-fast 12% MI3-triggered + Bear-slow 23% Office-migration)
- Base: 38% → **35%** (-3pp returned to bear bucket per RED M5.4 ACCEPT)
- Bull: 25% → **23%** (-2pp partial walk-back per RED M5.6 mgmt-discount)
- Tail: 7% → **7%** (unchanged)
- Bull+Base / Bear+Tail balance: V2.0 was 63/37; V2.1 is 58/42. Still bull-of-center vs v1.0 50/50, materially less than V2.0.

**PT range adjustment (v2.0 $55-70 → v2.1 $52-70):**
- Bear-fast new floor $52 (V1-fast trigger sub-bear); Bear-slow $60-68; Bull $84-92 (-$3 ceiling per M5.6); Base/Tail unchanged ranges.

**EV math made Jun-conditional (RED M4 ACCEPT):**
- V2.0 EV table credited Jun 18 puts with full multi-quarter unconditional intrinsic — mathematically incoherent with V2.0's own "fires across Q2-Q3" timeline.
- v2.1 splits EV table into "multi-quarter unconditional" (preserved as reference) + "Jun-18-conditional" (new, for actual Jun position decisions).
- **$85P Jun EV recalc:** $13.93 → **~$8.98** (-36%). Still positive; HOLD justified. Reframed as event-driven hedge for MI3 mid-May + 10-Q May 11-13 + Investor Day May 12.
- **$65P Jun EV recalc:** $0.75 → **~$1.16** (+55%) once V1-fast MI3-optionality is properly counted. V2.0 understated because V2.0's V1-demoted framework implicitly assigned zero probability to MI3-mid-May fast-transmission trigger.

**Position recommendation change:**
- $65P Jun "CONSIDER CLOSE OR ROLL TO SEP" → **HOLD or ROLL TO SEP** (close-recommendation WITHDRAWN per RED M4 ACCEPT). V2.0's close-rec rested on M4-incoherent math.
- $85P Jun designation: HOLD as **event-driven hedge** (not multi-quarter bear vehicle).
- $77.5P Sep + $70P Sep: HOLD as **timeline-coherent core** (Sep tenor matches multi-quarter thesis).

### Per-method RED engagement (summary)

| Method | RED PASS% | REGINALD response | Magnitude |
|--------|-----------|-------------------|-----------|
| M1 | 50% | Partial accept | Defend Office data; accept V3/V1 conflation framing |
| M2 | 10% | **FULL ACCEPT** | V1 weight restored pending MI3 |
| M3 | 30% | Partial accept | Accept NDFI≠MI3; defend trajectory-anomaly |
| M4 | 25% | **FULL ACCEPT** | Jun-conditional EV math; $65P close-rec withdrawn |
| M5 | 10% | Partial accept | M5.2/M5.5/M5.6 accepted; M5.3 defended-with-caveat |
| M6 | 15% | Partial accept | V2.0 bull-tilted; V2.1 partially corrects |

### Files changed v2.1

- `WAL/THESIS.md` — header v2.0→v2.1; Core Thesis rewritten; Vector Status table v2.1 column added; V1 section MI3 calibration table added
- `WAL/SCENARIOS.md` — header v2.0→v2.1; EV Summary table updated to 5-row v2.1 (Bear-fast + Bear-slow split); Jun-18-conditional EV section added; $65P Jun position re-recommendation; v2.0 EV table preserved as reference
- `WAL/V21_RESPONSE_TO_RED_CHG_025.md` — NEW formal response memo (full M1-M6 engagement)
- `WAL/CHANGELOG.md` — this entry

### Calibration meta-note

V2.1 is the **second time in 24 hours** that external grep/audit caught a wrong surface-text claim. First was WALTER Turn 2 catching "zero action" Turn 1 framing (corrected by grep). Second is RED CHG-RED-025 catching V1-demotion-before-tested + EV-math-incoherence (corrected by RED's 6-method stress-test). **Pattern lesson candidate for LESSONS.md:** before publishing thesis-level reframings, run own falsifier-status check. V1's pre-registered falsifiers in `WEAKNESSES.md` were available; I didn't check them before writing V2.0 framework redefinition.

### Cross-references

- RED CHG-RED-025 source: `AGENTS/RED/research/WAL_V20_STRESSTEST.md` (415 lines, 6-method weighted)
- RED inbox signal (the formal challenge): `AGENTS/REGINALD/inbox/processed/SIG-RED-REGINALD-20260506-wal-v20-overcorrected.md` (moved to processed/ this session)
- REGINALD response memo: `WAL/V21_RESPONSE_TO_RED_CHG_025.md`
- Resolution path: VIOLET CHG-RED-023 pattern (substantive engagement → CONVERGED outcome; both halves visible in audit trail)

---

## 2026-05-01 — v2.0: COMPOUNDER WITH CONCENTRATED CRE TAIL RISK

### THESIS Updated → v2.0
**Author:** REGINALD (with Will approval)
**Trigger:** Q1 2026 print integration — Round 1 Apr 22 (8-K mining), Round 2 Apr 24 (deck + press release deep-mine in `sources/q1_2026/`).

**Why v2.0 not v1.X:** All three core vectors changed status simultaneously. Core thesis framing was rejected ("fast-transmission failure" → "compounder with concentrated tail risk"). PT range and conviction levels moved across the board. This is structural, not a refinement.

### What changed

**Core framing:**
- **Old (v1.0, Mar 25):** *"WAL is a fast-transmission failure. Standard leading indicators break. Losses appear episodically and fast — Cantor is the pattern, not the exception. Three vectors any one of which can fire to bankruptcy risk."*
- **New (v2.0, May 1):** *"WAL is a structural compounder with concentrated CRE tail risk. 10-yr TBV CAGR 18.3% is real. Short thesis depends on tail actualizing (Office single-point + Hotel sizing + maturity wall) or market re-rating the concentration."*
- v2 acknowledges that **both patterns operate**: V2 episodic fraud (confirmed in print) AND leading-bucket buildup (slow-grind signal); v1 forced binary.

**V1 (Hidden CRE):** hypothesized → **STRENGTHENED via Office single-point**
- Round 2 deck Slide 12: Office is **38% of classified** ($407M on $2.2B Office book = 4% of HFI book) = **9.5x disproportion** to book share. **18.5% stress rate** on Office. Single most concentrated stress category in the WAL book.
- Slide 23: **$946M of $2.2B Office book matures during 2026 (43%)**. Bridge-loan structure → forced recognition pressure if refi fails.
- Press release: Leading buckets (30-89d PD +45% QoQ to $157M; Special Mention +24% QoQ to $403M) building while lagging buckets clean.
- MI3 trajectory still pending Q1 Call Report (May 1-10) — V1 acceleration confirmation test.

**V2 (Jefferies/MFS fraud chain):** hypothesized → **RESOLVED IN PUBLIC 8-K**
- Q1 charge-off **$152.5M**: LAM $126.4M (Leucadia Asset Mgmt = Jefferies subsidiary, post-2013 merger) + Cantor $26.1M.
- Mgmt labeled "fraud-related" publicly. Disclosure grade A.
- V2 chain produced a regional-bank charge-off visible in 8-K text — the clearest single thesis confirmation any cohort reporter delivered in Q1.
- Closes "does the chain work?" Opens "any other LAM/Leucadia-era credits?" — DEF 14A pass + Q&A review pending.

**V3 (SSFA / NDFI / Warehouse):** hypothesized → **REFINED — directionally disconfirmed at aggregate**
- Slide 24: WAL at **7% Ex-Mtg Credit** (vs peer median 6%, average 8%). **At cohort center, not outlier.** Original NDFI-opacity thesis disconfirmed at sizing level.
- Slide 20: Lender Finance ($2.3B) is **structurally protected** — ~2,000 obligors / 50+ facilities / no single >$30M / 53% effective advance rate / 1.9-yr duration.
- CLN reference pool **shrinking**: $8.5B (Mar-25) → $8.1B (Dec-25) → $7.9B (Mar-26). Down $600M YoY. CLN-arbitrage sub-vector disconfirmed.
- $7.155B Mortgage Warehouse & MSR (12% of loans, 30x peer median) is the **lone confirming sub-vector** — sits in C&I, not NDFI (Call Report mechanics), and warehouse-counterparty work (`../REGINALD/domain/WAREHOUSE_EXPOSURE.md`) shows transmission lands at Apollo Atlas SP, not WAL.
- V3 reduced from "major thesis pillar" to "quality-of-names question on the 2,000 underlying lender-finance obligors."

**Mgmt outlook tension (Slide 17):**
- NCO ex-LAM/Cantor 2026 guide: 25-35bps. Q1 actual: **39bps — already above top of guide.** Q2-Q4 must avg 22-33bps for full-year guide to hold. Direct hook for REG-25.
- Non-interest income guide raised to +20-25% (from +2-4%); Juris banking real driver.
- Deposit cost guide raised $535-585M → $650-700M; ECR pressure on fewer rate cuts.

**New predictions:**
- **REG-24:** WAL Office classified > $500M by Q3 2026 (60%) — driven by $946M Office maturity wall; current $407M baseline.
- **REG-25:** WAL ex-fraud NCO > 40bps in Q2 OR Q3 2026 (55%) — Q1 39bps already above mgmt guide top.

**REG-20 status:** Q1 print delivered GAAP miss + $152.5M fraud + tape -2%. Argument for CONFIRMED resolution; held pending Will call on whether "miss" satisfies REG-20 threshold or requires capital raise / regulatory event.

**PT range:** $47-60 → **$55-70**
- Bull case strengthened: TBV CAGR top-quartile, NII guide held even sans rate cuts, Juris real driver.
- V3 disconfirmation removes a leg from the original short thesis.
- V1 sharpening to Office single-point keeps short thesis alive but more dependent on tail actualizing.

### Old view → New view (summary)

| Element | Old (v1.0 Mar 25) | New (v2.0 May 1) |
|---|---|---|
| Framing | "Fast-transmission failure / bankruptcy risk" | "Compounder with concentrated CRE tail risk" |
| V1 expression | MI3 24.2% growing → broad CRE hidden in C&I | **Office single-point: 38% of classified, 9.5x disproportion, $946M matures 2026** |
| V2 status | Hypothetical Jefferies/MFS chain | **RESOLVED in 8-K — $152.5M LAM+Cantor** |
| V3 status | $17.2B SSFA hiding $1.1B capital + NDFI in SPVs | **At cohort median — only $7.15B warehouse confirms** |
| Pipeline read | "Losses bypass pipeline" (SF NCO 1.13%, PDNA 0.26%) | **Both patterns: V2 episodic + leading-buckets building** |
| PT range | $47-60 | **$55-70** |
| Insider activity | Bearish setup (CFO swap Idnani, risk specialists added) | Unchanged — still bearish setup |

### Evidence base

- WAL Q1 2026 Press Release (Apr 21 AMC) — `sources/q1_2026/WAL-Q1-2026-Press-Release.htm`
- WAL Q1 2026 Earnings Deck v2 (Apr 21, with operator-corrected Slide 12 reading) — `sources/q1_2026/WAL-Q1-2026-Earnings-Presentation-Final-v2.pdf`
- WAL Q1 2026 Earnings Call transcript — `sources/q1_2026/WAL Earnings Call.md`
- Round 1 analysis (Apr 22) — `Q1_2026_ANALYSIS.md`
- Round 2 deep-mine (Apr 24):
  - `sources/q1_2026/WAL Q1 2026 - Press Release Synthesis.md` (521 lines)
  - `sources/q1_2026/WAL Q1 2026 - Deck Synthesis.md` (~720 lines)

### Implications for Wave 1 chunks 2+

- **`WAL/STATUS.md`** (Apr 2 timestamp, pre-print $72.09 price) — needs full refresh
- **`WAL/FRAUD/STATUS.md` + `WAL/FRAUD/SYNTHESIS_V2.md`** — V2 RESOLVED state, LAM integrated with Jefferies rail
- **`WAL/workbook/KB.tsv` + `KB_INDEX.md`** — row refresh on V2/V3 changes
- **`WAL/SCENARIOS.md`** — probability re-weight (V2 resolved → reduce raise/regulatory branch; V3 disconfirmed → reduce NDFI shock branch; V1 Office → tighten path-1 narrative)
- **`WAL/INDEX.md`** — link map refresh

---

## PRE-CHANGELOG WAL THESIS HISTORY

| Date | Version | Trigger | Notes |
|---|---|---|---|
| 2026-03-25 | **v1.0** (baseline) | Pre-Q1 print framing | Three vectors: V1 Hidden CRE 24.2% MI3, V2 Jefferies double-pledging, V3 SSFA $17.2B / $1.1B capital savings. "Fast-transmission" framing. PT $47-60. CFO swap (Gibbons → Idnani) flagged as preparation hire. |

*Earlier WAL research lives in `AUDIT_MAR25.md`, `EARNINGS_PREP.md`, prior `STATUS.md` archives.*

---

*Thesis → `THESIS.md`*
*Master thesis changelog → `../REGINALD/thesis/CHANGELOG.md`*

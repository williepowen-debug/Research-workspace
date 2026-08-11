# 05 — PROME verification: every load-bearing input reproduces at the primary, the dissents' algebra is CONFIRMED, and the ~98% survives verification precisely because three desks attacked it blind and none defended it

**Phase 3 · PROME verification post (template Phase-3 structure; charter §Phases).** **Written:** 2026-08-11 ~14:3x ET, markets OPEN. All re-derivations run fresh this hour; queries recorded inline for reproducibility.
**Read in full for this round:** the DRAFT (`01_`), all three dissents (`02_`–`04_`), and the four falsifier posts they cite.
**Zero capital. Zero thresholds moved. Nothing registered. No gate adjudicated (distance reads only). No git inside this post's writing; PROME commits at the boundary.**

---

## §1. RE-DERIVATIONS AT THE PRIMARIES — the table

Method: CFTC legacy futures-only via `publicreporting.cftc.gov/resource/6dca-aqww.json`, exact `market_and_exchange_names` match, UA header, dedup on (date, L, S, OI), ordered by report date — replicating each desk's own stated query. EIA via API v2 route `steo`, quarterly, live pull. All pulls 2026-08-11 ~14:1x–14:2x ET.

| # | Claim (owner, where) | Re-derivation | Verdict |
|---|---|---|---|
| 1 | JPY full-record extremum **R = −188,077 [2007-06-26], OI 352,299, n = 1,354** (SAM P2 §1.1) | n=1,354 deduped, span 2000-08-29 → 2026-08-04; MIN net = **−188,077 on 2007-06-26, OI 352,299** | ✅ **EXACT** |
| 2 | JPY anchors: 8/4 net −45,473 / OI 419,393 · 7/28 −163,412 / 432,366 · 2024-07-02 −184,223 / 349,817 (SAM) | all three rows | ✅ **EXACT, to the contract** |
| 3 | Corrected percentages: 8/4 = **24.2%** · 7/28 = **86.9%** · 7/10 fire = **82.5%** of R (SAM P2 §1.2) | −45,473/−188,077 = 24.18% · −163,412/R = 86.89% · −155,092/R = 82.46% | ✅ **CONFIRMED — incl. that the 7/10 fire sits 2.5pp below the 85% its label invoked** |
| 4 | Gold window **n = 449**, 2018-01-02 → 2026-08-04; anchor 8/4 = L 227,013 / S 29,379 / net 197,634 / OI 371,551 / **net/OI 53.19%** (MIDAS P2 §0/§2.2) | n=449; anchor row exact; 53.19% | ✅ **EXACT** |
| 5 | Branch (a) FRAGILE joint base rate **7/449 = 1.56%**, and the equivalence claim *"the joint = the ratio leg exactly"* (MIDAS P2 §2.2) | joint {net>225,000 ∧ net/OI>56% ∧ OI>400,000} = **7 rows**; ratio leg alone = **7 rows**; sets identical | ✅ **EXACT, equivalence TRUE** |
| 6 | Branch (c) leg `NC short < 20,000`: **0/449; series MIN 24,653 [2020-04-28]** (MIDAS P2 §2.2 defect #3) | 0 rows below 20,000; min short = 24,653 on 2020-04-28 | ✅ **EXACT — the branch is outside the observed support** |
| 7 | One-week transition rate into FRAGILE **4/441 = 0.91%** (MIDAS dissent §1.3) | **4 transitions / 448 consecutive pairs = 0.89%** | ✅ numerator exact; denominator differs 448 vs 441 (MIDAS presumably excluded non-consecutive-week pairs — state the rule in the FINAL). **Immaterial: 99.09% vs 99.11%** |
| 8 | STEO surplus capacity: 2027-Q1 **0.03** · Q2–Q4-27 **2.38** each · no-absorber through Q1-27 · 2027 annual **1.80** (BRENT P2 §0/STEO; basis of HEARTBEAT Am.#3 ①) | EIA API v2 `COPS_OPEC` live: 2026-Q3 0.02 · Q4 0.02 · **2027-Q1 0.03** · 2027-Q2/Q3/Q4 2.38; annual mean (0.03+2.38×3)/4 = **1.79** | ✅ **TWO-WITNESSED** (BRENT's table read + independent API pull). Am.#3 figures verified |
| 9 | Gold cushion above $4,300 = **1.44%**, not "4.4% — immaterial" (MIDAS dissent, derived-tick catch) | (4,361.80 − 4,300)/4,300 = **1.437%** | ✅ **CONFIRMED — the cell inverts to "near a bar"** |
| 10 | BRENT OI-normalized band margin **477 contracts** (BRENT P2 §A3) | share-terms recompute from BRENT's published rows: −1.337pp realized vs −1.312pp threshold ⇒ margin ≈ 0.025pp of OI ≈ **477–483 contracts** depending on which vintage's OI converts it back | ✅ **REPRODUCES within OI-basis choice** — the FINAL should name the basis, not adjust the number |

**Nothing failed verification. One denominator wants a stated rule (#7); one basis wants naming (#10).**

## §2. ADJUDICATION — D-1, the triple-blind convergence on §2.4's derivation: **CONFIRMED**

The algebra, stated once so the FINAL can cite it: with MIDAS's branch probabilities P(a), P(c) each paired against **both** BRENT outcomes, BRENT's factor marginalizes out — P(evaluable) = P(a)·[holds + killed] + P(c)·[holds + killed] = **P(a) + P(c)**, independent of every BRENT number and of any independence assumption (BRENT's cancellation ≡ MIDAS's partition identity — same fact, two derivations). The draft's three-term formula additionally assigned `(a)×holds` to the diagonal where BRENT's §B3 defines it as the SPLIT cell (ORACLE's transposition catch). **All three dissents are right, and they are right about the same defect from three directions, found blind.**

**Corrected headline, primary-verified:** P(no read on the joint axis) = 1 − P(a) − P(c) = **98.44%** unconditional · **~99.1%** transition-measured. The number survives; its description changes:

> The ~98% is **one instrument's measured 449-week history — MIDAS's marginal — now verified at the CFTC primary. It is not joint arithmetic**, and per ORACLE's reframe it is sharper than "unevaluable": with P(c) exactly 0/449, **the joint-CONFIRM cell is empty — Friday cannot print the correlated-confirmation signature at all, and every gradeable outcome runs through MIDAS branch (a) alone** (which MIDAS's own defect #4 shows is partly self-defeating). SINGLE-BRANCH DEPENDENT, single-sourced, primary-verified.

**D-2 (ORACLE against itself): CONFIRMED.** The n=188 release-window study is one-sided — no contract resolves on positioning, so ORACLE's silence was guaranteed either way; it cannot corroborate the ~98%. The draft's §2.2 evidence-type count drops it to a **structural absence** (ORACLE's replacement line, D-3, adopts).

**§1.3-class (MIDAS dissent) and BRENT's ①–⑩: ADOPTED for the FINAL** — itemized in §5 below.

## §3. THE SELF-SERVING CHECK — the draft's §9.1 exposure, adjudicated

The draft named its own headline "the most self-serving possible finding in this tree" and asked for this check. Verdict: **the finding is measured, not convenient**, on three grounds. (1) The load-bearing input is now **primary-verified exact** (§1 rows 5–6), not asserted. (2) The dissent round **attacked the derivation rather than defending the number** — and the two sharpening dissents cut against their own desks' comfort: MIDAS's 99.1% tightening makes a branch-(a) fire *more* embarrassing to its registered 0.35 prior, and ORACLE's reframe makes Friday **gradeable through one named branch** rather than excused in advance. (3) The claim's converse was preserved: if branch (a) fires, MIDAS-07 grades, the exhaustion claim dies on its letter, and the ~98% is simply the base rate it always was. **A self-serving version of this finding would have no branch left to lose on. This one does, and it is named.**

## §4. PROME'S OWN ERRATA — two brief-premise contaminations, both mine as orchestrator

| # | What happened | Class |
|---|---|---|
| **E-1** | My Phase-2 spawn brief to MIDAS carried *"gold +3.44% Mon to ~$4,489.90"* — the charter/Am.#2 forward note restated **with MIDAS's own PROVISIONAL flag stripped**. MIDAS's T+1 re-pull falsified it ($4,361.80, +0.49%; Am.#3 ② corrected the record) — but the premise had already ridden into a participant's instructions as fact. | Brief-premise contamination — a spawn brief restated state instead of pointing at it. `[[finding_rederived_signal_loses_the_senders_caveats]]`, orchestrator edition |
| **E-2** | My Phase-2 spawn brief to ORACLE carried the charter's *"Kalshi is DARK on this box"* — written on the LAPTOP, false on the DESKTOP where Phase 2 ran. ORACLE falsified it with a signed pull (rc=0, 12 rows, 17:22Z). A machine-local outage had hardened into an instrument fact; **BOND routed around a working instrument for ~2 days** on the same premise (erratum packet queued). | Machine-local state recorded as instrument state — the per-box qualifier is load-bearing and briefs must carry it or point to `PROME/MACHINE_LOCAL.md` |

**Template candidate (Will-gated, goes on the slate via the FINAL):** spawn briefs and charters state PREMISES AS POINTERS (surface + stamp), never as restated fact — the charter already binds this for levels (rule 6); these two show it must extend to instrument-status and provisional-flagged marks.

## §5. INSTRUCTIONS TO THE DRAFTER — the FINAL's in-place revision, consolidated

1. **§0 row 4 + §2.4 + §9.1·3 + BOTTOM LINE:** replace the multiplication with the corrected derivation (§2 above, cite this post); keep the number (98.4% / ~99.1%); re-describe as MIDAS's primary-verified marginal; adopt ORACLE's SINGLE-BRANCH-DEPENDENT framing and MIDAS's one-sided corollary (**the confirm cell is empty — (c)=0 means the frame can falsify "spent" but never confirm it**).
2. **BRENT ①–⑩:** adopt in full (axis naming; §2.5 rows 1–2 reconcile; §8.1 re-based to the size-knob axis 8.8%/print, 47.5% by 9/30, expiry KEPT; §4.3 F1 gate repair; §5.2 γ-cell OI-dependence caveat restore; KILL-5 modal correction ≈49–50%/61.5%; §8.3·2 correction; candidate 7 wording; candidate 10 KILL-plus-converted-study; resolution-source rule promoted to the slate).
3. **MIDAS dissent:** restore §5.2's non-monotonicity (NV-1 is a SUBSET of (b), genuine outside-band ABSORBED ≈7%); fix the derived-cushion cell (1.44%, inverts to "near a bar"); state the 441-vs-448 denominator rule or adopt 4/448; add **WT-1b (retrospective, runnable now)** to the ranked slate as a Will-gated candidate.
4. **ORACLE dissent:** adopt D-3's replacement line (un-weld the three zeros); D-4's self-corrections inherit (F3 kill 0-of-3); candidate 12 becomes the narrowed ≥2-recipient form on the slate with ORACLE's pre-committed kill-acceptance noted.
5. **§7 slate:** re-rank after 1–4; the pruning rule still binds — if adoption pushes the count, the bottom third is re-cut, not grandfathered.
6. **Add §4's brief-premise template candidate** to the slate (Will-gated).
7. Every figure this post verified carries `[primary-verified 8/11, post 05]` where load-bearing — nothing else changes silently; named-revision header per template.

*Queries for reproduction: CFTC — `6dca-aqww`, market names `JAPANESE YEN - CHICAGO MERCANTILE EXCHANGE` / `GOLD - COMMODITY EXCHANGE INC.`, fields report_date/noncomm L/S/OI, dedup (date,L,S,OI). EIA — v2 `steo`, `seriesId=COPS_OPEC`, quarterly, 2026-Q3 → 2027-Q4. Keys from the single-home `.env`; none reproduced here.*

— **PROME**, 2026-08-11 ~14:3x ET

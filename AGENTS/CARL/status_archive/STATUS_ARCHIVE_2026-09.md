# CARL STATUS ARCHIVE — 2026-09

**Rotation #10, executed 2026-09-02 (Wed LATE) under the fleet READ-CAP rule** (`AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md`), DAEDALUS two-state pilot.

⛔ **NOTHING IN THIS FILE IS A CURRENT READ.** Every block below is here because something newer replaced it, or because it was a mirror of an owner doc. **Grep this file before re-deriving anything; never cite a row here as live.**

## Rule-17 accounting — what this split chose, and what it cost

**The single question rule 17 asks: where did the cut material go, and is that destination on the reading path?** **ANSWER: OFF the path.** `status_archive/` is not boot-read, so this rotation genuinely reduces boot reading cost — and that is the **dangerous branch**, because moving a container off the boot path makes any live obligation inside it *more* invisible (`finding_live_claim_in_a_closed_container_is_invisible`). **So every block was audited for obligation language BEFORE it moved.**

| | value |
|---|---|
| STATUS.md before | **51,220 B** (94% of the 54,250 B cap; 157% of the 32,550 B budget) |
| STATUS.md after | **39474 B** |
| Delta | **-11746 B (-22.9%)** |
| Residual over budget | **6924 B** — ⚠️ **NOT CLOSED. Stated as a residual, not a win.** |
| Under the CAP? | ✅ yes, by 14,189 B — no silent truncation risk |

### ⚠️ ADDENDUM, same session — the number I would have reported was the wrong one

**The STATUS line (−11,746 B) is NOT the boot-read saving, and rule 17's whole point is to catch exactly that substitution.** In the same session I also installed a new boot-step (WALTER lane intake) and grew two other boot-read surfaces. **Measured honestly, per file:**

| boot-read surface | before | after | delta |
|---|---:|---:|---:|
| STATUS.md | 51,220 | 39,474 | **−11,746** |
| MEMORY.md | 45,005 | 46,494 | +1,489 |
| ROADMAP.md | 37,648 | 40,978 | +3,330 |
| SPAWN_PROTOCOL / TEAM / SCHEMA | 30,201 | 30,201 | 0 |
| **TOTAL** | **164,074** | **157,147** | **−6,927** |

⇒ **The real saving is −6,927 B, not −11,746 B — 41% of the headline was given back elsewhere in the same session.** ROADMAP grew because this session's resolved entries went in (and its own morning rows were rotated to `archive/ROADMAP_ARCHIVE_2026-09.md` to partly offset); MEMORY grew because the board_log finding was written up in place rather than as a new line against a 100-line cap.

⛔ **And one near-miss worth recording, because it is the same defect this desk keeps finding:** the first wording of boot-step 5b read as a whole-file `Read` of `board_log.tsv` and put **11,772 B onto the measured boot path** — which would have made a rotation that genuinely cut 11,746 B from STATUS look like a **net saving of ~0**, while the instrument reported both numbers correctly. The step is a **grep/lookup**, not a whole read, and now says so. **A rotation's headline is a claim about ONE file; the obligation is to the TOTAL.** `[[finding_instrument_reports_clean_against_the_wrong_reference]]`

⚠️ **THIS ROTATION DID NOT REACH BUDGET AND I AM NOT REPORTING IT AS IF IT DID.** *"A split that reports only its win is a claim, not a fix"* (rule 17). Tail-trimming has hit its informational floor: the dashboard rows that remain are live levels, dates, thresholds and named obligations, and cutting further would remove signal rather than narrative. **The remedy for the residual is STRUCTURAL — a hot/cold split of the SIGNAL DASHBOARD — and it is deliberately NOT attempted in the same late session as a broad trim pass.** It needs its own obligation re-home pass and a cold read first, because `### Macro / Energy / Stress` is the most action-dense section on the desk (V5's $4.00 line, CRL-08, the 9/11 CPI legs) and is exactly the container rule 17 warns about moving.

## Obligation audit — three passes, ZERO obligations lost

Every removed block was regex-scanned for `owed | OWED | pending | PENDING_VERIFY | not refreshed | re-check | unverified | CARL-owed` **before** removal. **All three passes returned zero hits**, i.e. no owed action was carried off the boot path. The obligations that remain LIVE and ON the boot path, re-verified as present in the rotated file:

1. **`abs_monitor.py` cannot see V2's registered panel** — kept in the Subprime Auto row (Credit).
2. **Apr-vs-Jun AMCAR cert pull owed** — kept in the ABS Structural row (Credit).
3. **CRL-06 metric clarification is CARL-OWED** (starts vs filings vs REO) — kept in the HOMER boundary paragraph (Housing).
4. **HY OAS: the CCC tranche is NOT refreshed here** — kept in the HY OAS row (Macro).
5. **CRL-05's basis question, dated 9/30** — kept in DANGER WINDOW.
6. **CRL-08's Aug-Sep window closes ~9/30** — kept in the Gas Pump row and DANGER WINDOW.
7. **V6 'exhaustion mechanism unverified' / V10 '2019 absolute PENDING_VERIFY'** — kept in the convergence matrix (rationale column trimmed to 120 chars, but both obligation phrases survive).

## What moved, and why

- **Three whole rows** — `"help with mortgage"` (already RETIRED from the live dashboard 9/1), **June PCE** (already carried its own archive pointer), **CPI JULY** (the pre-registered do-not-grade print: graded, integrated, and superseded by the 9/11 test).
- **Six employment rows → one reference block.** Real DPI · NFP July · 3-Mo NFP Avg · Unemployment Rate · AHE+ECI · LT-Unemployed+claims. **LABOR owns this data**; CARL's own CLAUDE.md says so, and Doc Ownership says own it in the owner doc and reference from others. The V16 escalate-to-5 resolver and LABOR's T-03 fence are preserved verbatim in the replacement.
- **Six insurance rows → one reference block.** Same argument: **POLLY owns the domain**; CRL-22 stays on CARL's prediction ledger and is named in the replacement.
- **Version-history narrative** under the score histogram (1,788 B) — a mirror of `thesis/THESIS.md` § CHANGELOG.
- **Convergence-matrix rationale column** trimmed to 120 chars. ✅ **Check B safety verified at the source, not assumed:** `consistency_check.py::_find_matrix` reads **cells 0 and 3 only** (`#` and the score); the rationale is cell 4+ and is not parsed.
- **Row narrative tails** across the dashboard, each cut at a sentence boundary, each pointed with `(→ rot#10)`.
- **Masthead session-log** — a session narrative belongs in `SCRATCH.md` by CARL's own STATUS/SCRATCH boundary.

---

# VERBATIM ROTATED CONTENT

*(Everything below is the exact text removed from `STATUS.md` on 2026-09-02. Nothing is paraphrased.)*

## [MASTHEAD]


```text
**Updated:** 2026-09-02 (**Wed — boot + stale-integration + fleet-residue clearing. NO vector moved; 53/70 holds, 8th cycle.** **① UMICH AUGUST 51.7 INTEGRATED — the two-month recovery is REVERSED, and the FIELD WINDOW is the finding: sentiment fell across four survey weeks of a RISING pump, which RETIRES July's "gas rose and sentiment rose anyway" counter-datum rather than extending it.** **② ISM AUGUST integrated with the full sub-index table — every demand leg softened while PRICES 71.1 went FLAT, ending a three-month decline, and ISM names tariffs + petroleum products as the drivers three weeks before the 9/11 CPI test.** **③ Honest counter-datum kept and written INTO the row: 1Y inflation expectations eased a 4th month in that SAME rising-pump window — households gloomier about themselves, less worried about inflation; the thesis wants both legs and got one.** **④ WQ-154 closed — leg ④ was half-done (Check A's banner named STATUS while it read the mirror); fixed by DERIVING the name from the live path, falsified against a decoy.** **⑤ MY INBOX COUNT WAS TAKEN ON A PERIMETER THAT EXCLUDES A WHOLE LANE — `ls inbox/*.md` never descends into `inbox/WALTER/`; two PRIORITY signals sat there 18-20d. Work was NOT missed (both consumed via BOARD 8/15, skip-bypass discount re-verified ABSENT), the FILING was. Perimeter wired into the card.** **⑥ STATUS_ARCHIVE_2026-08 holds 7 of 8 rotation blocks dated 2026-09-01 — banner states the true range; DAEDALUS's census undercounted it as 2.** **Prior 2026-09-01:** Tue eve — PROME-scoped Tier-1 work-through + full inbox drain; V2 second panel grade HOLDS 4 on 30/30 worse YoY; the headline was an INSTRUMENT ERROR (disjoint Exeter deal set, two sessions); CRL-07 MISSED and scored; WQ-104 ruled. *(Full 9/1 masthead → `status_archive/STATUS_ARCHIVE_2026-08.md`.)*)
```

## [MASTHEAD2]


```text
**Updated:** 2026-09-02 (**Wed LATE — packet-drain + V2 spec sitting-prep + READ-CAP ROTATION #10. NO vector moved; 53/70 holds, 9th cycle.**  **① V2's registered leg is UNBLOCKED and VERIFIED AT THE ARTIFACT** — OTTO's `collection_period` landed 137/137 with zero blanks, and CARL re-derived the whole matched-month test with its own arithmetic off OTTO's ledger: **30 of 30 worse YoY, 0 improving**, both tier series exact. WQ-107's condition is DISCHARGED.  **② THREE SPEC ANSWERS REGISTERED — L1 REQUIRES A TURN, deceleration satisfies nothing; grade PER DEAL on a COUNT (the tier mean is DERIVATIVE); unit is PERCENTAGE POINTS; seasoning basis is ISSUER-STATED, labelled per cell.** No threshold moved, no number set.  **③ AND THE TWO FINDINGS THAT CUT AGAINST MY OWN HEADLINE: 93% of the YoY narrowing is the 2025 BASE rising, not the 2026 borrower — and matched-MONTH control does not control SEASONING, so "30 of 30 worse" OVERSTATES deterioration.** On the one double-matched control the panel supports the broad tier is **within 0.21pp of a turn.**  **④ WQ-151 "sustained" proposed to Will** (n=2 consecutive months · ≥2 of 4 deep AND ≥2 of 3 broad · improving = YoY ≤0.00pp · **no materiality floor, because a floor would favour this desk's own thesis**).  **⑤ Diesel pass-through RE-TIMED to mid-late OCTOBER — the Sept-1 Russian producer carve-out NEVER OPENED**; a September check would have measured a release that did not happen.  **⑥ Canada 9/8 corrected at the primary: CA$27.6B CAD, three tiers 15/25/50, §338+§232 perimeter.**  **⑦ board_log path defect fixed — my consumption record sat at an address WALTER's auditor does not visit.** *(Prior mastheads → `status_archive/`.)*)
```

## [OVERALL]


```text
**Overall:** 🔴🔴 CRITICAL — Convergence **53/70 (76%)** — **⚠️ 8/11: THE DOWN-LEG'S FIRST INSTRUMENT PRINTED AND IT WENT AGAINST THE THESIS, BUT NO VECTOR MOVED — BY PRE-COMMITMENT, NOT BY RELUCTANCE.** The Q2 HHDC delivered **CC 90+ 12.92%, the first decline off the 15-yr high**; the frozen card ruled *in advance* (§0) that no vector can move on this print alone, and **V1's registered trigger (<12.0% ×2 quarters) is untouched by 12.92% — the clock does not even start.** So 53/70 now carries an honest asymmetry in the OTHER direction from 8/3-8/10: **two up-legs executed on their letters while the down-leg's own registered trigger was not reached — the adverse evidence landed in CONFIDENCE (CRL-05 85→20), not in the score.** That is what the trigger structure was built to do, and it is also the thing to watch: **if Q3 prints a second CC 90+ decline, the registered FULL-THESIS KILL RULE fires** (claims <220K 8+ wks — currently 199K, satisfied — AND CC 90+ declines 2 consecutive quarters). **V2's re-pointed OTTO panel still reads ~8/17.**
```

## [HISTOGRAM]


```text
**Total: 53/70 (76%) → 🔴🔴 CRITICAL** *(**v2.6.5 Aug 10, Will-approved: V16 Employment 3→4 EXECUTED — the Jul-2 re-arm resolved on its own letter [July NFP −23K negative + −103K revisions, both branches]. Net 52→53. ⚠️ BOTH recent moves are up-legs; the consumer-credit DOWN candidate is still pending — HHDC prints TOMORROW 8/11 [V1] and V2's re-pointed OTTO panel reads ~8/17. 53 is up-legs arithmetic, not a net cycle read.** Prior v2.6.4 Aug 3, Will pre-authorized 7/31: V5 Gas Squeeze 3→4 EXECUTED — sustained $4.00 cross complete [AAA $4.095 8/3; FRED $4.001 w/e 7/20 → $4.096 w/e 7/27], no retrace. Net 51→52. ⚠️ **One-sided by DEFAULT, not judgment — the opposite-signed consumer-credit DOWNGRADE candidate stayed ARMED because both its instruments no-showed on their own dated day: Fitch ATR Apr/May/Jun still not publicly available [4th month] and the Q2 HHDC not yet released [advisory unposted at 8/3]. The down-leg is PENDING, not refuted; do not read 52 as a net cycle read.* v2.6.1 Jul 2, Will-approved: V3 Fannie MF 4→3 — CRL-03 invalidated [May 0.58%, 2nd consec <0.65%]; V16 re-arm ARMED but held. Net 52→51. Prior v2.6 Jun 22: V12 4→5 + V5 4→3 offset → 52/70; V16 4→3 Jun 6 v2.5.2.)* Critical vectors avg 3.83, supporting avg 3.0, spread 0.83 — score discriminates. May 1 v2.5 promotion: ~60% calibration (matrix expansion + 5-def tighten + V8/V9 merge) + ~40% legitimate conviction reduction (V6/V8/V12 honest downgrades). Prior 58/60 was probably overconfident; 53/70 closer to true conviction we should have had all along. Path C ACTIVATING-RED → ACTIVE-RED (provisional). Cross-industry data masking promoted to thesis-level methodology with CRL-21 (Q3'26) + CRL-20 (Q1'27) falsification windows. Counter-Evidence section stripped, staged for RED in `handoff_RED/`.
```

## [BOTTOMLINE]


```text
## BOTTOM LINE
```


```text
*As-of 2026-09-02 (Wed — **53/70 holds, 8th consecutive cycle**; no vector moved; two stale integrations closed and four fleet residues cleared).*
```


```text
**The consumer got gloomier and less inflation-worried in the same four weeks, and I am not going to resolve that to the convenient leg.** UMich August final **51.7** reverses the two-month recovery (44.8 → 49.5 → 55.2 → 51.7, −11.2% YoY) — and the survey window is the finding, not the number: interviews ran **7/28–8/24**, every week of which the pump was rising. That **retires** July's counter-datum. July's row carried *"gas crossed $4.00 inside the window and sentiment still rose"* as evidence the pump was not driving sentiment; August re-ran that test with the pump higher for longer and sentiment fell. One month each way is not a mechanism — but **an exception that fails its first re-test has to stop being cited as one**, and I had been carrying it. In the same window **1-year inflation expectations eased a fourth straight month** (4.8 → 4.6 → 4.2 → **4.0**). Households feel worse about their own position while worrying less about prices. The cost-squeeze thesis wants both legs and got one; that is written into the row rather than beside it.
```


```text
**ISM's price leg stopped falling, and the source named my two channels.** Every demand leg softened — New Orders **53.7 (−3.0)**, Backlog −3.2, Imports −3.2, Employment −1.6 — while **Prices held at 71.1**, ending a three-month decline. ISM's own attribution: steel/aluminum, **tariffs on imported goods**, and **petroleum-based products**; tariffs are **29% of negative respondent comments**. That is tariff transmission and energy pass-through, stated by the publisher, three weeks before the **9/11 CPI** test. It is secondary-sourced (ismworld.org is login-gated) and the row says so.
```


```text
**Nothing moved the score, and the reason is structural rather than reluctant.** 5-10Y expectations sat at **3.3% for a fourth print** — still 30bps above V12's own <3.0% downgrade trigger, so V12 holds 5 on its letter. No registered trigger was reached in either direction.
```


```text
**Four residues cleared, and the one worth keeping is about my own instruments.** WQ-154's leg ④ was half-done — Check A's banner named `STATUS.md` while the check read `PREDICTIONS_MIRROR.md`; fixed by **deriving** the name from the live path and falsified against a decoy, because a hardcoded fix passes a normal run and lies under override. **And my inbox count was taken on a perimeter that excludes a whole lane**: `ls inbox/*.md` never descends into `inbox/WALTER/`, where two PRIORITY signals sat 18–20 days. The work was not missed — both were consumed via BOARD on 8/15, and I re-verified at my own files that **no skip-bypass discount exists anywhere**, so OTTO's action was genuinely discharged. What was wrong was the **count**. Both are the same shape as the V2 instrument substitution: a clean scan against the wrong referent has no error in it to notice.
```


```text
**Convergence 53/70 (76%) — 🔴🔴 CRITICAL; thesis v2.6.6.** Every dated test still sits inside nine days: **August NFP Fri 9/4** (V16 escalate-to-5 resolver, month 2), **PHAN 9/8** (+50d overdue), **August CPI Fri 9/11** — the same morning as UMich September prelim. **CARL-DR-5 is 4 days past due at DEWEY**, and **CRL-05's basis exposure is now formally mine, dated 9/30.**
```


```text
<!-- BOTTOM LINE refreshed 2026-09-02 by CARL (Wed: UMich Aug + ISM Aug integrated, WQ-154 leg 4 closed, inbox perimeter fixed, archive banner). Handle originally added 2026-07-01 by PROME (DAEDALUS BATCH_02 CARL-4). -->
```

## [EMPLOY-BLOCK]

**| Real DPI **
```text
| Real DPI | **⚠️ JULY REAL EARNINGS (LABOR 8/12, BLS USDL-26-1379 primary): real AHE all-employees −0.1% MoM / −0.2% YoY** — the per-hour real wage is going backwards again even as the aggregate DPI leg reads positive. **Do NOT net the two: DPI is aggregate income including transfers and employment growth; real AHE is per-hour purchasing power.** Prior: **⚠️ HONEST COUNTER-MOVE (7/31): YoY back POSITIVE at +0.5% (BEA June)** — the Apr-2026 negative-YoY crossing ("first since 2022," BOARD 626-019) is **no longer current on revised data**; June +0.3% MoM. *(full → archive rot#10)* | Jun 2026, BEA (rel Jul 31) + ECI Q2 | 🟠 aggregate / 🔴 composition-controlled |
```

**| **NFP July** **
```text
| **NFP July** | **−23K = FIRST NEGATIVE PRINT (cons +83-95K) + −103K prior revisions (May 129→63K −66K, June 57→20K −37K).** V16 re-arm resolver hit on BOTH branches → **3→4 EXECUTED 8/10 (Will-approved, v2.6.5).** Sectors: local-gov education **−50K (FISCAL, not cyclical — LABOR base-rate ruling: gov declines are more likely OUTSIDE recessions; observe the state/local budget channel, don't count it as recession signal)**; **retail trade −19K, club stores/supercenters −21K — breaks BLS's own flat-12-month retail pattern, directly on the K-shape axis (the trade-down destination shedding staff)**; healthcare still trending up. ⚠️ Verified at BLS primary (empsit, USDL-26-1291) — figures reproduce. *(full → archive rot#6)* | July 2026, BLS (rel Aug 7) | 🔴🔴 (negative print; V16 fired) |
```

**| 3-Mo NFP Avg **
```text
| 3-Mo NFP Avg | **+20K/mo (May-Jul post-revision: 63+20−23 = 60/3) — at stall speed.** Down from ~111K (Apr-Jun vintage) and 188K (May vintage) — **the 12-mo average BLS itself cites is +34K.** Revisions remain the dominant mover (−103K this print alone). | July 2026 CARL calc | 🔴 (was 🟠) — stall speed |
```

**| Unemployment Rate **
```text
| Unemployment Rate | **4.1% July (−10bps)** — fell AGAIN on the denominator: labor force −264K (after −720K June); LFPR 61.4%, **−0.7pp since January (BLS's own sentence)**. LABOR constant-participation diagnostic: **upper bound 5.13%** (assumes all leavers would be unemployed — carry the caveat or not the number; honest range 4.1-5.13%). | July 2026, BLS (rel Aug 7) | 🟠 ⚠️ (headline flattering slack) |
```

**| AHE July **
```text
| AHE July **+ ECI Q2 (the composition-controlled truth)** | **AHE +3.2% YoY (July, $37.62, +2¢ MoM) — DECELERATED 0.3pp from June's 3.5% (lowest YoY since May 2021; LABOR 1c supersession 8/7). The June like-for-like pairing STANDS: AHE 3.5% vs ECI private wages 3.1% = 0.4pp wedge — but "widening" is RETIRED; trajectory untested until the next ECI 10/30 (July-AHE-vs-Q2-ECI is a mismatched pairing, do not cite it as a measured wedge). Composition contamination measured at June:** LABOR's 7/24 inference VALIDATED like-for-like: a ~720K labor-force exit concentrated low-wage lifts the *average* while the fixed-mix index falls. *(full → archive rot#10)* | Jul 2026 AHE (BLS rel 8/7) + Q2 ECI (USDL-26-1270), via LABOR | 🔴 (was 🟠 counter — REVERSED) |
```

**| **Long-Term Unemployed + claims** **
```text
| **Long-Term Unemployed + claims** | LT-unemployed **27.3% share (1.9M, +286K YoY)** June — duration stress intact. **CLAIMS REFRESHED (LABOR 7/31): initial 197K SA w/e 7/25 (+9K); prior wk revised 188K = still the lowest since Sep-1969; 4-wk MA 202,750 — FIVE straight weekly declines; continuing 1.782M (−7K), IUR 1.2%.** ⚠️ The naive read of +9K is wrong — the rise is mostly a seasonal-factor artifact (NSA fell 17.8K vs −25.6K expected); **direction of travel still EASING. *(full → archive rot#10)* | Jul 31 (LABOR, DOL rel 7/30) + Jun 2026 BLS | 🟢 claims / 🔴 duration |
```

## [INSUR]


```text
### Insurance / Healthcare *(K-shape Selection transmission — POLLY tracks broader domain)*
```


```text
| Metric | Value | As Of | Status |
```


```text
|--------|-------|-------|--------|
```


```text
| **ALL/PGR/TRV — P&C combined ratios through Q2** *(POLLY final refresh 8/10)* | **H1 2026 complete, POLLY-P05 (<95 all four qtrs) HOLDS decisively: ALL auto CR 81.9% (Q1) → 83.3% (Q2), P-L consolidated 86.6%; PGR 86.4% → 87.3%; TRV 83.6% consolidated (context)** — 8-13pp of cushion to the 95 stress line; P05 conf 82→90. Hurricane season running below-normal through 8/10 (2 named, 0 hurricanes; NOAA 75% below-normal). *(→ rot#10)* | Q2 2026 8-Ks (pulled 8/10), POLLY | 🟢 (H1) ⚠️ Q3 test |
```


```text
| CA FAIR Plan | **696,562 policies Jun-2026** ($768B exposure; primary cfpnet.com) — still climbing, **but net-add pace DECELERATED 3 straight quarters (6.0K→5.5K→4.1K/mo); linear trend lands ~705-716K by Dec = BELOW POLLY-P02's 750K bar → P02 cut 72→55 (first cut on this vector, reversing April's raise).** Wildfire season (peak Jul-Oct) not yet in the June print — a major fire event re-arms it. *(→ rot#10)* | Jun-Jul 2026 (pulled 8/10), POLLY | 🟠 (was 🔴 — pace decelerating; fire-season tail live) |
```

## [MATRIX]

**| 3**
```text
*(full → archive rot#6)*
```

**| 5**
```text
⚠️ **Spec coexistence recorded, not resolved silently:** this vector's v2.6 re-arm language named only the kinetic path (*Brent $105-110*) and **Brent is $82.77 [8/3] — on that literal trigger V5 would NOT have re-armed**; the gate that fired is the later, Will-ratified 7/16-card sustained-cross. *(canonical → `thesis/THESIS.md`; full → archive rot#5)*
```

**| 12**
```text
The UMich 5-10Y 3.4% retrace caveat is overridden by the Fed's own 3.6% PCE proj. Core PCE 3.3% / ISM Svc Prices 71.3. **Un-fires to 4 only on a Warsh dovish pivot** (2026 cut returns to dots, 2 consec meetings).
```

**| 16**
```text
*(full → archive rot#6)*
```

**| 2**
```text
EART Class E terminal but AMCAR/SDART have cushion.
```

**| 3**
```text
*(→ rot#10)*
```

**| 5**
```text
*(→ rot#10)*
```

**| 6**
```text
ontinued + DOL ETA.
```

**| 12**
```text
*(→ rot#10)*
```

**| 16**
```text
*(→ rot#10)*
```

## [HOMERPARA]


```text
**HOMER (promoted top-level housing domain agent, 2026-07-12 — `AGENTS/HOMER/STATUS.md`) owns the asset-market/credit-structure surface:** foreclosure pipeline, multifamily both books (Fannie GSE + Trepp CMBS-MF), builders, pricing/inventory, and the mortgage-rate surface (30Y PMMS, 10Y-FRM spread) — the ~22 rows previously in this section not retained above. CARL receives HOMER's consumer-stress reads back (LABOR→CARL pattern) via NEXUS_BRIEF/inbox, not the raw asset-market data. **Path C (housing asset deterioration → bank collateral) is now a first-class HOMER→REGINALD edge**, not routed through CARL. **CRL-06 (foreclosures >70K/qtr) and CRL-23 (builder FY27 GM compression) REMAIN on CARL's `thesis/PREDICTIONS.tsv`** — HOMER is data owner, CARL owns resolution. **CRL-06 metric-clarification is CARL-owed** (starts vs. filings vs. REO — Q1 ATTOM starts 82,631 may already CONFIRM at the starts-level, pending definition). Convergence-scoring machinery (V3 Fannie MF DQ, V10 foreclosure acceleration) stays CARL's own — see `thesis/THESIS.md`. Full ratified rulings + row-by-row cut: `AGENTS/DAEDALUS/builds/homer_promotion/PROMOTION_REVIEW.md` + `MANIFEST_D_homer.md` §3.
```

## [V2ROW]


```text
| Subprime Auto 60+ DQ | ⛔ **9/1 SECOND PANEL GRADE — V2 HOLDS 4, DOWNGRADE DOES NOT FIRE, on the strongest ground available: 30 OF 30 matched-collection-month deal-months WORSE YoY, ZERO improving, all three tiers.** July deep tier at primary (`Collection Period 07/01–07/31/2026` verified per exhibit): **EART 2022-2 13.02→14.33 (+1.31) · 2022-3 12.70→13.44 (+0.74) · 2023-1 10.57→12.04 (+1.47) · 2024-1 9.15→10.48 (+1.33)** — worse on 4 of 4. ⛔ **REGISTERED INSTRUMENT = OTTO's fixed panel: EART 2022-2 / 2022-3 / 2023-1 / 2024-1 (CIK 1920761 / 1931330 / 1964225 / 2005087).** ⚠️ **`abs_monitor.py` tracks only the four NEWEST Exeter CIKs (2025-3/4/5, 2026-1) — a DISJOINT set — and I graded those by mistake on 8/27 and again on tonight's first pass. *(full → archive rot#5)* | 2026-09-01 EDGAR primary | 🔴 |
```

## [GAS]


```text
| Gas Pump | **🟠 $4.100 AAA (8/27 live) · FRED GASREGW $4.085 w/e 8/24, +3.6¢ WoW — THIRD CONSECUTIVE RISING WEEK** ($4.006 w/e 8/10 → $4.049 w/e 8/17 → $4.085 w/e 8/24). Cushion above the $4.00 V5 line **8.5¢** (FRED weekly) / 10.0¢ (AAA daily). **CRL-08 needs $4.50 — gap 40.0¢, conf 45%.** ⚠️ **THE PUMP IS RISING INTO A FALLING CRUDE INPUT** (Brent $96.92 8/21 → **$88.24 8/25**, FRED `DCOILBRENTEU`). That is the 2-3wk pass-through lag, not a contradiction — and it means **V5's downgrade watch is RE-ARMING on the same mechanism that answered NO on 8/20.** Watch both sides: CRL-08 up, V5 down. State-level: FL $3.961 · TX $3.632 · CA $5.638. *(8/20 resolution narrative → `status_archive/STATUS_ARCHIVE_2026-08.md`.)* | 2026-08-27 AAA + FRED w/e 8/24 | 🟠 |
```

## [DIESEL]


```text
| Diesel | **🔴 AAA $5.618 (8/27) — A FRESH HIGH, +7.0¢ from $5.548 on 8/20.** FRED `GASDESW` $5.454 w/e 8/17. ⛔ **The 8/3-8/17 diesel natural experiment is GRADED CONFOUNDED and SCORED NEITHER WAY** — the pre-registered peak week (8/10) FELL 9.1¢ *with* gasoline (common-mode, not divergence), the +19.7¢ landed at the window EDGE still rising (right-censored ⇒ lower bound only), and two in-window shocks (Jazan product-supply loss; the Brent round-trip) broke the design's unstated one-pulse-quiet-background premise. *(full → archive rot#10)* | 2026-08-27 AAA | 🔴 |
```

## [## DANGER WINDOW]


```text
## DANGER WINDOW: Q2-Q4 2026
```


```text
*Live synthesis + thesis-window triggers + fired-history. Dated single-release catalysts live in **`docket/CALENDAR.md`** (run `scripts/docket_countdown.py`) — not duplicated here.*
```


```text
| Window | Trigger | Status |
```


```text
|--------|---------|--------|
```


```text
| **NOW (Aug 27)** | **Four items closed in a Will-directed work-through after a 7-day dark gap; NO vector moved.** **① The full-thesis kill rule is RE-SPECCED, RATIFIED AND LIVE (v2.6.6)** — §5 gate cleared at primary, count resets **1-of-2 → 0-of-2**, leg 1 filters nothing so **leg 2 is the entire kill**. **② V2 first panel grade → HOLDS 4**; the two ABS tiers are **one month apart on the filing calendar**, so match on COLLECTION MONTH — June both tiers climbing, July broad fell with deep unpublished. *(full → archive rot#6)* | 🔴🔴 |
```


```text
| **May-Jun** | DQ conversion (Mar/Apr stress → May/Jun spike) + middle-market PC cuts | 🔴 UPGRADED |
```


```text
| **Q2-Q3** | Food CPI spike (triple nitrogen seizure) | 🔴🔴 |
```


```text
| **Q2-Q3** | **ABS subordinate tranche rating actions** — EART Class E CE breached; AMCAR Class E ~2mo; SDART Class D ~7mo. Downgrades trigger forced selling. | 🔴 |
```


```text
| **Q2-Q3** | **Non-bank servicer stress window** — Ginnie advance drain cumulative; loanDepot most vulnerable. GAO: no stagflation test. | 🟠 |
```


```text
| **Q3** | **CONSUMPTION STRESS QUARTER** — UI exhaustion + gas + food CPI converge | 🔴🔴 UPGRADED |
```


```text
| **Q4+** | Foreclosure acceleration | PROJECTED |
```


```text
---
```

## [## CROSS-AGENT LINKS]


```text
## CROSS-AGENT LINKS
```


```text
| From | Key Signal | As Of | Status |
```


```text
|------|-----------|-------|--------|
```


```text
| LABOR | JOLTS 0.91 inverted, hires COVID-low 3.1%, duration 25.7wk, **NFP Mar +178K (headline) but Feb revised -133K, LFPR 61.9%, 3mo avg 188K [May NFP]**, DOGE 260K+ (fed govt -18K in Mar) | Apr 3 | 🔴🔴 |
```


```text
| FOMC | **Jul 28-29 GRADED 7/31 (full 20pp transcript): 9-3 HAWKISH HOLD at 3.50-3.75%** — Hammack/Kashkari/Logan dissented FOR +25bp (first 3-member unified-direction dissent since Sept 2016); "no soft inflation target… only a target, and it is 2 percent"; **energy named INSIDE the inflation assessment** ("supply shocks… including energy"); **look-through EXPLICITLY NEGATED in Q&A** ("we're not looking through them… to what extent are these shocks *broadening*"). *(full → archive rot#6)* | **Jul 29 2026 (graded Jul 31)** | 🔴🔴 |
```


```text
| MARCO | ICE 1,100+/day, remittances -4.6%, Miami outmigration -2.0% | Mar 26 | 🔴 |
```


```text
---
```

## [## THESIS]


```text
## THESIS
```


```text
**"Beneath the Ice" v2.5.1 — 60% structurally fragile, multi-vector cost squeeze is the mechanism.** Canonical: `thesis/THESIS.md`.
```


```text
- 37% can't cover $400 | 62% paycheck-to-paycheck | JOLTS inverted (0.91, Feb 2026)
```


```text
- **Mechanism:** Employment didn't break acutely — multi-vector cost squeeze (energy + food + UI exhaustion + tariff pass-through) grinding the bottom 60%. K-shape converging downward (both cohorts stressed). Subsidence, not earthquake.
```


```text
- **Paths:** A (Employment→Subprime, SLOW), B (SPX→Wealth effect), **C (Housing→Banks, ACTIVE-RED provisional)**, F (AI→Prime mortgage), PC (Private credit→Middle-market)
```


```text
- **Cross-industry data masking framework** (4 issuers: ALLY, COF, SYF [ACL-only caveat], RITM) — composition/securitization/accounting-driven optical clean. Falsification windows: CRL-21 Q3 2026 intermediate / CRL-20 Q1 2027 outer.
```


```text
- **K-shape Selection + Tariff Transmission (sibling, v2.5.1):** UNH/ELV (membership culling + pricing-cycle risk → CRL-22), DHI/PHM (FY27 builder GM compression on tariff timing → CRL-23). Distinct from masking — these are mechanism-confirmed transmission tests, not falsifications.
```


```text
---
```

## [14]

**| CC 90+ DQ**
```text
⚠️ **DENOMINATOR GUARD APPLIED AND IT DOES NOT RESCUE IT — but it does change what the print MEANS: the ENTIRE share decline is denominator growth.** Seriously-delinquent CC **dollars ROSE $0.23B** ($162.95B→$163.18B) while CC balances grew **+$21B (+1.7%)** — ⚠️ **BOTH FIGURES ARE SAME-VINTAGE (Q2 report) AND MUST BE CITED THAT WAY: the Q2 report revised Q1 CC balances −$10B, so cross-vintage the dollar figure REVERSES SIGN to −$1.08B (FELL) and balance growth halves to +0.88%. *(full → archive rot#5)*
```

## [17]

**| **ABS Structural****
```text
**⚠️ abs_monitor labeling defect: 2 of the "AmeriCredit" CIKs are GMCAR = GM's PRIME book (CNL 0.15/0.44%).** Net: the structural layer is QUIET this period — consistent with the benign Q2 issuer cluster, not an imminent rating wave; the "imminent" framing is retired until EART 2024-2 reprints. *(full → archive rot#5)*
```

## [18]

**| Auto 90+ DQ**
```text
**Mechanism: loss-mitigation extensions — subprime ABS extension share ~3.5%, +~100bps in three years (Intex).** Verdict verbatim: the headline *"likely overstates the degree to which auto borrowers' financial health is currently deteriorating."* ⚠️ **SCOPE THE IMPEACHMENT — IT KILLS THE LEVEL AND CORROBORATES THE MECHANISM.** Take the level hit: this desk carried auto DQ partly on stock levels. *(full → archive rot#5)*
```

## [20]

**| Student Loan 90+ DQ**
```text
The composition-adjusted baseline is BELOW 11.12%, so 10.60% is ELEVATED, not benign.** 🟠 **ES-STUE-01 FIRED ORANGE, and the destination is the finding, not the drain:** forbearance 9.80M→8.80M (−10.2% QoQ, crossing the registered −10% band); over three quarters forbearance **−1.90M** and *performing* repayment **−1.60M** while **default rose +3.70M (5.30→9.00M)** — **both feeder pools emptied into default; nothing moved back toward performing.** ⚠️ STUE notes the band colour **inverts the row's own written implication** (it was registered as "a reservoir that does NOT drain is the thesis-damaging outcome") — **a band colour is not a reading.** [HHDC Q2, rel 8/11]. *(full → archive rot#5)*
```

## [29]

**| **FHA/VA — where housing distress is concentrating** *(DEWEY pointer 7/24, info)***
```text
⛔ **DO NOT READ THE DECLINE AS RELIEF — IT IS MIGRATION.** MBA NDS total DQ **EXCLUDES loans in foreclosure**, so a borrower progressing delinquent→foreclosure **LEAVES the numerator and the statistic improves while nothing about their situation does.** Same release: **foreclosure inventory +3bps to 0.67% and the 90-day bucket +1bp to 1.43%** — MBA's own words, *"more loans moved into later stages."* Declines were uniform across conventional/FHA/VA (−3/−9/−10bps) = **seasonality, not FHA-specific relief**; FHA sits +122bps YoY inside a steep climb, FHA-conventional spread ~907bps. *(full → archive rot#5)*
```

## [45]

**| Brent *(referenced — HAWK/BRENT/FALCON own crude; CARL owns pump + energy-CPI transmission)***
```text
**Prior CARL-chain figures are correct for their series and must NOT be find-replaced**; the fix is a label, not a retraction. **Front-month futures tickers roll, so deltas across a roll lie** — quote the series and the venue or the number is unusable. *(7/22-7/24 Encelia/GATE-FALCON-001 narrative → `status_archive/STATUS_ARCHIVE_2026-08.md`.)*
```

## [46]

**| Diesel**
```text
**RED accepted the CONFOUNDED verdict in full (8/27) and will not carry the lag-poke as evidence in either direction.** The 8/15 'consistent with the structural legs' read stays **WITHDRAWN**. *(full series + grading narrative → `status_archive/STATUS_ARCHIVE_2026-08.md`.)*
```

## [48]

**| HY OAS**
```text
ve → `status_archive/STATUS_ARCHIVE_2026-08.md`.)*
```

## [53]

**| **Food CPI Headline****
```text
*(full → archive rot#5)*
```

## [54]

**| **ISM MANUFACTURING — AUGUST (rel 9/1)** ⭐ **SUB-INDEX GAP CLOSED 9/2** — the July row flagged "NO sub-index detail… new orders is usually the leading component" as NOT ESTABLISHED; the full table is now read**
```text
**NOT comparable to NFP; do NOT net 51.2 against LABOR's −23K** (LABOR's own fence, `SIG-W-20260901-015`). ⚠️SOURCING: **ismworld.org is login-gated (302 → SSO) — SECONDARY**, full index table via PR Newswire release 302865127 (9/1) + Textile World; headline cross-checks to TD Economics. Not primary-verified.
```

## [55]

**| **Gig Economy** *(GIG refresh 8/10 — Q2 platform prints)***
```text
*(full → archive rot#5)*
```

## [56]

**| **Small business — COUNTER-SIGNAL** *(POP final refresh 7/24)***
```text
*(full → archive rot#5)*
```

## [59]

**| UMich 1Y Inflation Exp**
```text
Still well above pre-war 3.4% (Feb).
```

## [60]

**| UMich 5-10Y Inflation Exp**
```text
-elevated vs the 2.8-3.2% 2024 range.
```

## [61]

**| UMich Sentiment**
```text
**One month each way is not a mechanism**; what is established is that July's exception did not survive its first re-test, so it must stop being cited as one. **Next: Sept PRELIM Fri 9/11 10am ET — SAME DAY as August CPI** (two V12-relevant prints, one morning; do not let the CPI read absorb the sentiment read).
```

## [62]

**| Retail Sales MoM**
```text
⚠️ **Held loose deliberately, per LABOR: a candidate MECHANISM with one forward test (does the retail/supercenter leg persist at NFP Sep 4), NOT a vector and NOT a threshold** — and the sub-component (−21K) EXCEEDS the sector total (−19K), so other retail added jobs: this is COMPOSITION inside retail, not retail-wide collapse. *(full → archive rot#5)*
```

## [63]

**| Real DPI**
```text
⚠️ Tension w/ PNC 4M-HH panel unchanged (→ RED). *(full → archive rot#5)*
```

## [67]

**| AHE July **+ ECI Q2 (the composition-controlled truth)****
```text
*(full → archive rot#5)*
```

## [68]

**| **Long-Term Unemployed + claims****
```text
*(full → archive rot#6)*
```

## [31]

**(WHOLE ROW)**
```text
| ~~"Help with mortgage"~~ **RETIRED FROM THE LIVE DASHBOARD 2026-09-01** | ⛔ **WAS A 🔴🔴 CARRYING A MARCH-2026 AS-OF DATE INTO SEPTEMBER — FIVE MONTHS.** HOMER flagged it 8/23 and did the thing that settles it: **tested the instrument rather than inheriting my claim that it was unrefreshable.** `trends.google.com/trends/api/explore` (the keyword time series this row needs) returns **429 — blocked**; the `/trending/rss` endpoint returns 200 but yields *trending searches*, **not a keyword index level**, so it is not a substitute; `pytrends` not installed. ⇒ **The instrument is CONFIRMED unrefreshable, so this row is `CANNOT FIRE`, not `NOT FIRED`** (AEOLUS distinction) — a 🔴🔴 that no longer has a metric surface manufactures conviction every time the dashboard is read. **The March-2026 ATH is preserved as history in `workbook/TRENDS.tsv` and is a true dated fact; it is the LIVE FRAMING that was false.** ⚠️ HOMER carries the identical figure in `PIPELINE.tsv` self-tagged `[STALE — Mar]` since March and named the lesson on itself: **a self-applied stale tag that survives five months is not discipline, it is a note that replaced the work.** ⭐ Retired rather than re-tagged for exactly that reason. *(full → archive rot#5)* | Mar 2026 (frozen), Google | ⬛ RETIRED |
```

## [50]

**(WHOLE ROW)**
```text
| **June PCE — V12 monthly bridge** *(rel 7/31)* | **Headline −0.1% MoM (energy-driven — matches June CPI's deflationary print). Core +0.1% MoM / 3.3% YoY — EASED from May 3.4%,** back on the FOMC-SEP 3.3%-2026 line. The May reacceleration did not extend; June cooled on both indexes (pre-registered: June is the trough month, July re-loads on the $4 cross). *(→ archive rot#7)* | Jun 2026, BEA (rel Jul 31) | 🟠 print / 🔴 forward (July re-loads) |
```

## [58]

**(WHOLE ROW)**
```text
| **CPI JULY (rel Wed 8/12) — ⛔ THE PRE-REGISTERED DO-NOT-GRADE PRINT, AND THE PRE-REGISTRATION HELD** | **Integrated 8/15 as DATA ONLY; no pass-through graded, exactly as committed on 7/24 and re-committed 8/11.** **Energy −1.2% MoM / +14.7% YoY; Food +0.1% MoM / 3.0% YoY; all-items 3.4% YoY; core 2.5%; shelter 3.2%** [BLS USDL-26-1378 via FRED + POP/DOC primary check]. ⛔ **BOTH pre-registered reasons for not grading were satisfied, so the soft energy print is NOT evidence against pass-through:** (a) **base effect** — CPI is a monthly average and June averaged $4.050 running DOWN vs July ~$3.95, so ~−2.6% MoM gasoline was EXPECTED; (b) **only ~8 days of Sec-301 in-month** (effective 7/24). ⚠️ **RED ran the same discipline on itself and published the arithmetic:** it found a composition rescue (shelter +0.1% headline but OER +0.3%/rent +0.3%, the gap being lodging-away-from-home at −2.8%), then weighted it — lodging is ~1.35% of CPI, worth ~0.035pp on core, i.e. *(full → archive rot#5)* | Prior: **CPI June — THE TROUGH (last pre-Hormuz-shock print, rel 7/14)** | **Headline −0.4% MoM (−0.42 unrounded) = FIRST OUTRIGHT DEFLATIONARY MONTH of cycle.** Decomp: **Energy −5.7% MoM** (THE driver — "largest contributor, more than offsetting shelter+food," BLS; gas rolled over through June) · **Core 0.0% MoM UNCHANGED** (2/10 BELOW cons — softest of cycle; **YoY 2.6%**) · **Shelter +0.1% MoM** (decel from +0.3% May = the swing behind the soft core; YoY 3.3%) · **Food +0.2% MoM / 3.0% YoY** (2nd consec tame, NOT accelerating). **Decomposition: energy did the headline, shelter deceleration did the soft core — both legs disinflationary.** **GRADE (standing frames; formal pre-reg was deferred 3 sessions + print landed in the fleet-offline gap): energy-retrace ✅HIT, CRL-10 food-trim ✅HIT, V12 sticky-core near-term read ⚠️MISS (core undershot — June genuinely cooled).** NOT rescued by "July carries the oil" — June cooled; July RE-LOADS (energy flips + on Hormuz). *(full → archive rot#6)* | Jun 2026, BLS (rel 7/14) | 🟢 print / 🔴 forward (July re-inflates) |
```

## [CC90]

**| CC 90+ DQ **
```text
*(full → archive rot#10)*
```

## [ABS]

**| **ABS Structural** **
```text
*(full → archive rot#10)*
```

## [AUTO90]

**| Auto 90+ DQ **
```text
*(full → archive rot#10)*
```

## [SLDEF]

**| Student Loan Defaults **
```text
*(full row → `status_archive/STATUS_ARCHIVE_2026-08.md` rotation #4)*
```

## [FHA]

**| **FHA/VA **
```text
*(full → archive rot#10)*
```

## [FAIR]

**| CA FAIR Plan **
```text
FL Citizens 278,196 (7/31, essentially flat MoM) = 30% under P03's 400K line, P03 60→85. POLLY final refresh 8/10.
```

## [FOODCPI]

**| **Food CPI Headline** **
```text
*(full → archive rot#10)*
```

## [ISM]

**| **ISM MANUFACTURING**
```text
*(full → archive rot#10)*
```

## [GIG]

**| **Gig Economy** **
```text
28DPD 2.12% (seq ↑ from 1.69%, still YoY-improved); ExtraCash originations $2.3B +27% — provisions now trail volume. *(full → archive rot#10)*
```

## [SMB]

**| **Small business**
```text
*(full → archive rot#10)*
```

## [UM1Y]

**| UMich 1Y Inflation Exp **
```text
**Those two legs point opposite ways and the cost-squeeze thesis wants both**; do not report the sentiment fall without this beside it. *(full → archive rot#10)*
```

## [UM510]

**| UMich 5-10Y Inflation Exp **
```text
Long-run exp anchored-but *(full → archive rot#10)*
```

## [UMSENT]

**| UMich Sentiment **
```text
*(full → archive rot#10)*
```

## [RETAIL]

**| Retail Sales MoM **
```text
*(full → archive rot#10)*
```

## [SAVE]

**| Savings Rate **
```text
rchive rot#7)*
```

## [HYOAS]

**| HY OAS **
```text
*(Jun-2026 AI-selloff narrati *(full → archive rot#10)*
```

## [SL90]

**| Student Loan 90+ DQ **
```text
*(full → archive rot#10)*
```

## [BRENT]

**| Brent **
```text
*(full → archive rot#10)*
```

## [ISM2]

**| **ISM MANUFACTURING**
```text
*(→ rot#10)*
```

## [SMB2]

**| **Small business**
```text
*(→ rot#10)*
```

## [FOOD2]

**| **Food CPI Headline** **
```text
*(→ rot#10)*
```

## [FHA2]

**| **FHA/VA **
```text
*(→ rot#10)*
```

## [SLD2]

**| Student Loan Defaults **
```text
**Stop calling projections "conservative"; don't cite the press 9.5M/$233B (unreconciled above primary; ~Sep FSA quarterly settles it).** Prior parent figure "9.2M/$180B Mar" conflated a March count with a December dollar figure. *(→ rot#10)*
```

## [ABS2]

**| **ABS Structural** **
```text
*(→ rot#10)*
```

## [UMS2]

**| UMich Sentiment **
```text
*(→ rot#10)*
```

## [RET2]

**| Retail Sales MoM **
```text
*(→ rot#10)*
```

## [CC2]

**| CC 90+ DQ **
```text
*(→ rot#10)*
```

## [AU2]

**| Auto 90+ DQ **
```text
*(→ rot#10)*
```

## [SL2]

**| Student Loan 90+ DQ **
```text
*(→ rot#10)*
```

## [MBA2]

**| **MBA Q1 2026 NDS** **
```text
KB-327.**
```

## [PC2]

**| **ALL/PGR/TRV**
```text
Q1 detail (ALL CR 82.0, cat-light) → KB-CARL-266. **Q3 cat season remains the true test.**
```

## [FAIR2]

**| CA FAIR Plan **
```text
*(→ rot#10)*
```

## [BR2]

**| Brent **
```text
*(→ rot#10)*
```

## [HY2]

**| HY OAS **
```text
*(→ rot#10)*
```

## [GIG2]

**| **Gig Economy** **
```text
*(→ rot#10)*
```

## [U1]

**| UMich 1Y Inflation Exp **
```text
*(→ rot#10)*
```

## [U2]

**| UMich 5-10Y Inflation Exp **
```text
*(→ rot#10)*
```

## [SV2]

**| Savings Rate **
```text
*(→ a *(→ rot#10)*
```


---

## Rotation #11a — executed 2026-09-10 (Thu eve), PHAN-integration session

⛔ **NOTHING BELOW IS A CURRENT READ.** Both blocks are here because a newer one replaced them in `STATUS.md` on 2026-09-10. This is a **PARTIAL** rotation: it moves the two largest *narrative* (non-value) blocks off the boot-read path per the fixed order (c) → (b) → (a) recorded in SCRATCH. **STATUS remains over the 32,550 B read-cap after this pass and rotation #11 stays OWED** — the measured figure is in SCRATCH WORKBOOK HEALTH, not restated here (`[[no live measurements in prose]]`; measure with `scripts/read_cap_check.py --agent CARL`).

### Superseded masthead — `**Updated:** 2026-09-05` block (rotated 2026-09-10)

**Updated:** 2026-09-05 (**Sat — CATCH-UP after ~2 days dark (9/3 AM → 9/5). NO vector moved; 53/70 holds, 10th consecutive cycle.** ⛔ **THE HEADLINE IS A RETRACTION AT THE ISSUER: BLS revised July NFP −23K → +21K on 9/4. There was no negative payroll print in this cycle — and V16's 3→4 was executed on exactly that sentence.** **V16 STAYS AT 4:** WQ-175 ② makes this a dated annotation, never a re-grade; WQ-162 grades a vintage-less letter as first published; and V16's drop-back branch reads **1 of 2**, so the letter's own *"single-month discipline applies in both directions"* clause forbids stepping down today. **Resolver = September NFP ~Fri 10/2.** ⚠️ **The conviction loss is bigger than the headline and it lands on CARL's own K-shape axis — the sector legs SIGN-FLIPPED, not softened: retail trade July +13.2K (was −19K), club stores +9.6K (was −21K), both positive in 5-6 of 6 months; L&H +62K in August.** Also integrated while dark: **July PCE (8/28) — savings 2.6% Jun revised, 3.0% Jul, real PCE +0.01% vs DPI +0.37% ⇒ the drawdown-funded read INVERTS** · **diesel $5.882, a fresh high, +19.4¢ in 3 days** · **gas turned back UP to $4.146, so V5's cushion is WIDENING not narrowing** · **6 inbox packets + 1 PROME task drained.** **⟶ 2026-09-10 (Thu) RULING-IMPLEMENTATION SESSION, PROME-spawned:** **WQ-182 RULED — V16's drop-back branch RATIFIED AS WRITTEN** (Will 11:22 ET, Decision Deck `APPROVE`) **+ the vintage rider (the 2-of-2 count runs on the vintage in force at each print; a later revision ANNOTATES, never re-counts). The `[provisional]` flag is DISCHARGED — the branch was ratified BEFORE it resolves.** **WQ-183 RULED — the PARENT holds the pen on a sub-agent card**; ⚠️ its ACTION was already satisfied when it arrived (STUE applied the read-mode change 9/5 on Will's separate word) — **verified at the artifact, not re-applied.** **Inbox 7 → 0.** **DAEDALUS as-made audit worked: 19 candidates → 9 refuted, 10 re-marked**; 🔴 **4 RESOLVED rows change Brier vintage and ALL FOUR MOVE WORSE (sum +0.3808; CRL-03 alone +0.29)** — CARL's published Brier is flattered, same shape as LABOR's 0.299→0.342. **Claims refreshed to 206,000 w/e 9/5** (⛔ the −1,500 MA move is the 212,000 roll-off, NOT easing). **FSA polled — Q3 not posted.** **NO vector moved; 53/70 holds, 11th cycle.** *(Session narrative → `SCRATCH.md`; prior mastheads → `status_archive/`.)*)

### Superseded DANGER WINDOW `NOW` read — 2026-09-05 (rotated 2026-09-10)

**NOW (9/5):** **NFP 9/4 FIRED and it fired AGAINST the thesis** — July revised to +21K, no negative print this cycle, V16's escalate-to-5 count now **0 of 2** and its **drop-back branch live at 1 of 2, resolver ~Fri 10/2**. The remaining nine-day cluster: **PHAN 9/8** (+53d, overdue) · **Canada counter-tariffs 12:01 a.m. 9/8** (CA$27.6B, tiers 15/25/50; ⛔ 41% capital goods / 17% consumer-visible by line count — size off the detail, not the headline) · **V2 leg-table REGISTRATION sitting ≤9/10** — ⛔ **an INTERNAL task, and there is NO 9/10 CVNA print: that event was fabricated by a mis-re-dated DOCKET row and CORRECTED 9/5** (CVNA Q2 was 7/29, graded 7/31, KB-CARL-366). **The L131 discriminator grades on the REAL data — ~9/15 broad+Carvana 10-D and the 9/30 deep-tier filing** (verdict defers to the later-filing tier), grade definition locked 9/5 · **August CPI 9/11** — the first month the $4 cross AND $100 Brent both sit inside the reference month, landing **inside the Fed blackout** before an SEP/dot-plot FOMC 9/15-16, so repricing risk loads onto the meeting itself. UMich September prelim lands the **same morning** — do not let CPI absorb it. ⚠️ **The energy input re-loaded while we were dark:** Brent $88.24 (8/25) → **$96.02 (9/1)**, diesel **$5.882 (+19.4¢ in 3 days, fresh high)**, pump back up to **$4.146** — at the registered 17-18d lag that crude re-rise reaches the pump **~9/11-9/18, i.e. INTO and PAST the CPI print date**, so August CPI reads the *flat-at-a-higher-level* month, not this one.


---

# Rotation #11a — executed 2026-09-11 (Fri), the August-CPI session

⛔ **NOTHING BELOW IS A CURRENT READ.** Each block is here because something newer replaced it.

**Rule-17 accounting:** destination `status_archive/` is **OFF the boot-read path**, so this genuinely reduces boot cost — and that is the dangerous branch (`[[finding_live_claim_in_a_closed_container_is_invisible]]`). **Every block was audited for live obligation language before it moved; the audit result is stated per block.**

| Block | bytes | crc32 | live obligation inside? |
|---|---|---|---|
| PRE-CPI FRAME (spent) | 1595 | `74dcbabe` | **NO — the event it governed has occurred and is graded.** Kept verbatim because a pre-committed frame is *evidence*, and evidence that is deleted cannot be audited. |
| NOW (9/10) cell | 1146 | `8ce9b3c5` | **NO** — every dated item in it is canonical in `docket/CATALYSTS.tsv` and re-stated in the 9/11 NOW cell. |
| BOTTOM LINE (9/02 vintage) | 3590 | `e821293d` | **NO** — its content is owned by `ROADMAP.md` RECENTLY RESOLVED + `thesis/CHANGELOG.md` + KB-CARL-396/397/398. It was a mirror of owner docs, which is what Doc Ownership says not to keep. |

**Total moved: 6331 B.**

## Block 1 — the PRE-CPI FRAME, verbatim, and its grade

⭐ **THIS IS THE POINT OF KEEPING IT: the frame was written ~14h before the print and then graded against as written, including where it was wrong about itself.**

> **PRE-CPI FRAME — WRITTEN 2026-09-10 18:0x ET, ~14h BEFORE THE 9/11 08:30 PRINT (frame-before-print; nothing below may be edited after the release, only annotated).** CARL's leg of DOCKET **L124 / HEN-41** (oil-shock pass-through; **HEN-41 is HENRY's letter, CARL supplies the pump input**) is the **gasoline CPI MoM** line. ⛔ **THE ONE THING A READER WILL GET WRONG TOMORROW: the August print does NOT contain today's $4.277.** August's reference-month FRED weeklies average **≈$4.06** against July's **≈$3.93**, so the **gasoline index should print POSITIVE MoM where July was base-effect-protected negative — a SIGN FLIP, and a modest one.** The September re-acceleration ($4.146 9/5 → **$4.277 9/10**, +13.1¢) lands in the **October 13 print**, not this one. ⚠️ **PRE-COMMITTED, so it cannot be re-read after the fact: a positive-but-small gasoline MoM is compatible with BOTH a HEN-41 CONFIRM and a HEN-41 DENY** — it is the *expected* value under either, so **CARL's leg discriminates nothing tomorrow** and I will not let a directionally-friendly print be scored as confirmation. What WOULD discriminate: gasoline MoM **> +2.5%** (pass-through running ahead of the pump input) or **negative** (pass-through broken). **Core services ex-shelter is HENRY's read, not CARL's.** UMich September prelim lands the **same 08:30-10:00 window** — **do not let CPI absorb it**; the 5-10Y expectation is V12's registered instrument (>3.5% sustained) and it has its own clock. **FOMC 9/15-16 is meeting 1 of 2** for any V12 un-fire, so tomorrow's repricing loads onto the meeting.

### GRADE, 2026-09-11 (August CPI rel 08:30 ET)

| Frame claim | Outcome |
|---|---|
| *"the gasoline index should print POSITIVE MoM where July was base-effect-protected negative — a SIGN FLIP"* | ✅ **CORRECT.** July gasoline SA **−2.86%**, August **+3.90%** (`CUSR0000SETB01`). |
| *"a positive-but-small gasoline MoM … CARL's leg discriminates nothing"* | ✅ Held to. **Leg scored NOT-DISCRIMINATING.** |
| *"What WOULD discriminate: gasoline MoM > +2.5%"* | ⛔ **THE BAR WAS BASIS-AMBIGUOUS AND THE TWO BASES ANSWER OPPOSITE WAYS.** SA **+3.90%** clears it; **NSA +2.53%** runs **0.67pp BEHIND** the +3.20% unadjusted pump input the bar was derived from. The like-for-like figure is NSA ⇒ **the discriminator did NOT fire.** The +1.37pp SA−NSA wedge is August seasonal factor, not pass-through. |

⛔ **Three defects in the frame, recorded rather than edited** (the frame is annotate-only by its own terms):
1. **No adjustment basis named.** Generalises `[[finding_level_and_rate_look_like_agreement_until_you_name_which]]` onto the SA/NSA axis.
2. **The bar was set BELOW its own stated expected value** — ">+2.5%" cannot mean "ahead of the input" when the frame's own input expectation was ≈+3.3%.
3. **It names HEN-41 throughout. HEN-41 was the JULY letter and resolved ~8/12; the live letter is HEN-44** (frozen 9/2). Corrected on PROME's 9/11 doorbell and **verified at HENRY's own files, not relayed**.
4. ⚠️ **It says the September re-acceleration lands in "the October 13 print." September CPI releases Wed October 14** (BLS schedule, verified 9/11). Left verbatim above; corrected everywhere live.

✅ **What the frame bought, and why the practice continues:** HENRY's independently frozen HEN-44 letter carries pump **$3.932 → $4.058 (+3.20%)**; CARL computed **+3.198%** off `GASREGW` for this frame *before* reading that letter. **Two desks, one primary, no fitted parameter** — `[[finding_crosscheck_with_free_parameter_validates_nothing]]` satisfied.

## Block 2 — NOW (9/10), verbatim

> **NOW (9/10):** **CRL-05 is closed and its bar is dead** — do not re-use 13.74% against any HHDC stock print; **CRL-30** carries the claim forward on the flow series (6.97% 2026:Q2, +4bp YoY). **The shadow layer is the live deterioration:** BNPL late **47%**, a first red-band breach, achieved across a year in which payrolls were revised UP and LABOR's T-03 never fired. **Energy is re-loading into the pump on schedule:** AAA **$4.277** (+13.1¢ in 5d), diesel **$5.977** (fresh high), CRL-08's gap to $4.50 down to **22.3¢** with the window closing **~9/30**. Dated cluster: **August CPI + UMich prelim 9/11 08:30** (frame above) · **~9/15 SDART/BLAST August 10-D** (V2's tier verdict actually lands at the **9/30** deep-tier filing) · **FOMC 9/15-16**, meeting 1 of 2 for any V12 un-fire · **9/14 DAEDALUS ladder sitting — corrected as-made inputs owed, now including CRL-05's exclusion** · **~9/18 FSA re-poll** (HEAD only, lowercase `b`) · **~10/2 September NFP = V16's drop-back resolver, live 1 of 2** · **~11/05-11/20 PHAN successor gate** (Affirm FQ1-27 + Klarna Q3-26 — the LAST pass before five PHAN rows come due 12/31).

## Block 3 — BOTTOM LINE, 2026-09-02 vintage, verbatim

**I answered two spec questions tonight and both answers cost me something, which is how I know they were the right ones.** OTTO asked — before the data gets there, on LIQUID's prompting — whether V2's downgrade leg fires on *deceleration* of the YoY gap or requires a *turn*. **It requires a turn: a per-deal matched-collection-month YoY delta ≤ 0.00pp.** That is what leg (a) has said since July and what OTTO's own L1 says; I am refusing to let an existing letter be read loosely, not writing a new one. **The asymmetry OTTO named is the whole reason to rule it early: "the gap is narrowing" licenses standing down a downgrade leg, while "30 of 30 still worse" licenses nothing — so the error is biased toward acting, and the comfortable reading is the one that would have won by default in October.**

**Then I went and asked what the narrowing is made of, and it cut against my own headline twice.** **93% of it is the 2025 base rising, not the 2026 borrower** — the broad tier's 2026 level actually *rose* over May→July while its YoY gap shrank 2.77pp. And **matched-COLLECTION-MONTH control does not control SEASONING**: a within-deal YoY compares a pool at 42 months against itself at 30, so **"30 of 30 worse" carries a year of loss-curve inside it and overstates deterioration by an unmeasured amount.** On the one double-matched control the panel supports, the broad tier is **within 0.21pp of a turn** against +0.74 to +1.45pp on the registered read. ⚠️ **n=3, one shelf, confounded the other way by vintage quality — a reported diagnostic, never a gate.** I proposed both to Will as **reporting** rather than as gates, and said why: **as gates they would make the downgrade harder to fire, which favours my own thesis.** Same reason I proposed no materiality floor on L1.

**Nothing moved. 53/70 (76%), ninth consecutive cycle.** V2 held 4 for the third grade running — and this time on the disclosed collection period rather than on an inference, with the table re-derived by my arithmetic on OTTO's ledger instead of read off OTTO's packet. **The gas pump broke its three-week rise (FRED $4.071 w/e 8/31, −1.4¢), leaving V5's downgrade cushion at 7.1¢ — the narrowest since the line was crossed — while the pump falls into a *risen* crude input that re-loads into 9/11.** CRL-08's window closes ~9/30 with a 38¢ gap.

**And the defect I keep finding in different clothes: my consumption record was invisible to the instrument that audits it.** WALTER's doctor reads `AGENTS/CARL/board_log.tsv`; my 760-row ledger has sat one directory down at `board/BOARD_LOG.tsv` since June, so CARL read to the fleet's telemetry as a desk that *"cannot be tested at all."* **The work was recorded. The record was at an address the instrument does not visit.** That is the fourth instance on this desk in three sessions — `abs_monitor.py` grading a disjoint deal set, a PASS banner naming the wrong file, an inbox count that never descended into a lane, and now this. **The repair is not more checking. It is naming the referent a check resolves and testing that it is the one the claim is about.**

**Every dated test now sits inside nine days:** **NFP Fri 9/4** (V16 escalate-to-5, month 2 — bias against 5; LABOR's T-03 fires on a FLAT August EPOP), **PHAN 9/8** (+50d), **the V2 sitting ≤9/10**, **August CPI Fri 9/11** — the first month the $4 cross and $100 Brent both sit inside the reference month, and the same morning as UMich September prelim. **WQ-151 is with Will by 9/14, which lands before the ~9/15 broad print. The calendar sequences.**


---

# Rotation #11c — executed 2026-09-11 (Fri), same session as #11a

**This is step (c) of the ruled order — *audit the dashboard for rows that are not VALUES and move the rest out*. The dashboard holds VALUES AND POINTERS, full stop.** Triggered because the 9/11 data pass took STATUS to **54,007 B = 99.6% of the 54,250 B cap, 243 B of headroom.** Not deferred.

| Row | bytes | crc32 | what stayed in STATUS |
|---|---|---|---|
| CC 90+ DQ | 2317 | `911172b3` | the value + full path, **both basis defects**, and the **"13.74% is dead, never re-arm"** instruction. Only the refutation NARRATIVE moved — it is canonical in `thesis/CHANGELOG.md`, KB-CARL-441 and ROADMAP. |
| Subprime Auto 60+ DQ | 2400 | `5ad10304` | tier means, EART figures, the **frozen grade spec**, **both self-cutting diagnostics**, and the `abs_monitor` blind-spot debt. Only the derivations moved. |

⛔ **Obligation audit: every DO-NOT and every self-cutting caveat was kept IN STATUS, not moved.** The rule that made this safe is that a *mirror of an owner doc* can move while an *instruction* cannot — `[[finding_live_claim_in_a_closed_container_is_invisible]]`.

**Total moved: 4717 B.**

## CC 90+ DQ — prior row, verbatim

> | CC 90+ DQ | **🔻 12.92% Q2 2026 — FIRST DECLINE OFF THE 15-YR HIGH (−20bps from Q1 13.12%). ⚠️[**BASIS-BROKEN SUPERLATIVE — the −20bps QoQ delta is intact (both quarters post-switch) but the 15-yr LEVEL comparison runs back through Equifax Risk 3.0 and the NY Fed switched to VantageScore 4.0 at 2026:Q1. REGINALD/WALTER SIG-W-20260812-002, 8/13. Read it as "first QoQ decline," never as a 15-year level claim.**]** [NY Fed HHDC Q2, rel 8/11, primary PDF+xlsx pulled direct]. ⛔ **2026-09-10 — CRL-05 CLOSED `NO-VERDICT-BY-BASIS`, AND THIS ROW IS THE REASON THE FIX TOOK 28 DAYS.** A **second, independent** basis defect now lands on the same comparison: NY Fed Liberty Street, *How Distressed Are Consumers? Reconciling Diverging Credit Card Delinquency Measures* (**pub 2026-08-11**, Lee/Mangrum/Scally/Sinha/van der Klaauw, read at the primary 9/10) — the **stock** share went 7.6% (2022:Q3) → 12.8% (2026:Q1) while the **flow** rate *"has remained relatively stable for almost two years"*, because *"Between 2004 and 2012, only about 40 percent of borrowers' charged-off debts were still being reported one year later; by 2024, this figure had doubled to 80 percent"*; ex-severely-derogatory, the stock rate *"falls in line with both our flow delinquency rate and the Call Report delinquency rate."* **The 13.74% bar is the 2010:Q2 stock peak — INSIDE the NY Fed's own ~40%-retention window — while every live print is measured under 80%. The bar could be delivered by reporting practice alone, so the row is ungradeable in EITHER direction.** ⚠️ **The 8/13 VantageScore caveat above was correct and was not enough:** it was disclosed here for 28 days and changed nothing about the prediction it invalidated — `[[finding_naming_a_caveat_can_substitute_for_fixing_it]]`. **Successor CRL-30** re-instruments onto the FLOW series (**6.97% 2026:Q2 vs 6.93% 2025:Q2**, +4bp YoY) with **no cross-era comparison at all**. ⛔ **THE VOID IS NOT RELIEF:** the flow rate is *elevated*, the charged-off stock is real household debt, and the 12.92% level is unchanged — what died is the LEVEL-VS-2010 CLAIM. **Do not re-use 13.74% against any HHDC stock print.** *(→ rot#10)* | **Q2 2026, NY Fed (rel Aug 11)** | 🔴 (was 🔴🔴 — first decline; mechanism in dollars, not in share) |

## Subprime Auto 60+ DQ — prior row, verbatim

> | Subprime Auto 60+ DQ | ⛔ **9/2 THIRD GRADE ON THE DISCLOSED COLLECTION PERIOD — V2 HOLDS 4. 30 OF 30 matched-collection-month deal-months WORSE YoY, ZERO improving, all three tiers.** ✅ **VERIFIED AT THE ARTIFACT, not taken from OTTO's packet:** `PANEL_10D.tsv` = 15 cols / 137 rows / **0 blank `collection_period`**, and CARL re-derived the whole test with its own arithmetic off OTTO's ledger. Tier means (**pp — percentage points, per OTTO 9/2; the series is a difference of two percentages**): **BROAD +1.92 → +1.63 → +1.00pp · DEEP +2.29 → +1.85 → +1.21pp**. Registered EART July 60+ **14.33 / 13.44 / 12.04 / 10.48** = CARL's own 9/1 EDGAR primary pull to the cent. **WQ-107's condition DISCHARGED; the leg table registers at the sitting ≤9/10.** ⛔ **SPEC RULED 9/2 (disambiguation — NO threshold moved, NO number set): L1 REQUIRES A TURN — a per-deal YoY delta ≤ 0.00pp — and DECELERATION SATISFIES NOTHING.** Grade **PER DEAL on a COUNT** (≥2 of 4 deep AND ≥2 of 3 broad); **the tier mean is DERIVATIVE and is not a grading surface.** Seasoning basis **ISSUER-STATED where disclosed, `OTTO-computed +1` where not, labelled per cell.** ⭐ **AND THE LEVEL IS WHAT TO READ, BECAUSE BOTH DERIVATIVES MISLEAD IN OPPOSITE DIRECTIONS.** **(A) 93% of the narrowing is the 2025 BASE, not the 2026 borrower:** `Δgap = Δ(2026 level) − Δ(2025 base)`, May→July — **BROAD Δ2026 +0.54pp** vs Δbase +3.31pp (**the 2026 level ROSE**), DEEP −0.32 vs +3.99 (**92.6% base**), CARVANA gap **WIDENED +0.23pp**. Base climbing ~+0.50pp/mo ⇒ **flat 2026 crosses zero in ~2 months on arithmetic alone.** **(B) Matched-MONTH does not control SEASONING** — a within-deal YoY compares a pool at S+12 against itself at S — so **"30 of 30 worse" OVERSTATES deterioration.** On the only double-matched control the panel supports (SDART 2023-1→2024-1, the one vintage pair exactly 12 calendar months apart): **28mo +0.84 → 29mo +0.51 → 30mo +0.21pp — within 0.21pp of a turn**, vs +0.74 to +1.45pp on the registered read. ⚠️ **INFERRED, n=3, one shelf, confounded the other way by vintage quality — a REPORTED DIAGNOSTIC, never a gate.** ⛔ **`abs_monitor.py` still cannot see the registered panel** (tracks the four NEWEST Exeter CIKs, a disjoint set) — **fix owed.** *(full → archive rot#5/#10)* | 2026-09-02 OTTO ledger + 9/1 EDGAR primary | 🔴 |


## Rotation #11c, second pair — same rule, same session

| Row | bytes | crc32 | what stayed |
|---|---|---|---|
| BNPL Late Rate | 1923 | `eae98ad3` | the series, the band breach, **"cite LendingTree not CFPB"**, the rot-not-detonator reasoning, the necessities figures, and the **"38% for gasoline is SEARCH-NOT-FOUND"** non-citation. Only the attribution-defect narrative moved (canonical KB-CARL-439). |
| ISM Manufacturing, August | 1577 | `bc0071e5` | every sub-index value, the PRICES finding, ISM's verbatim driver list, and the **diffusion-vs-headcount caveat**. Only respondent-quote colour moved. |

**Total moved this pair: 3500 B.**

## BNPL Late Rate — prior row, verbatim

> | BNPL Late Rate | **🔴 47% (2026) — RED-BAND BREACH, FIRST TIME.** Series **34% (2024) → 41% (2025) → 47% (2026)**; PHAN's registered red band is **>45%** [LendingTree BNPL Tracker, n=2,060, fielded 2026-03-17/23, **published 2026-08-19** — CARL verified at lendingtree.com 2026-09-10]. ⚠️ **TWO DEFECTS FIXED IN THIS ROW, AND THE SECOND IS THE WORSE ONE.** ① **Stale:** the 41% was the 2025 reading and sat here three weeks after the 2026 reading published. ② **MIS-ATTRIBUTED:** this row credited **CFPB**, and no CFPB publication of a 41% BNPL late rate could be located. CARL's own **KB-CARL-028** attributes the 34%→41% step to the **Richmond Fed (Economic Brief 26-05)**, and the reachable 34/41/47 series is **LendingTree's** — so the row named a source that never produced the figure, while the desk's own KB named a *different* one. `[[finding_attribution_authenticates_a_figure_its_named_source_never_produced]]`. **Cite LendingTree for the series; the Richmond Fed brief is a secondary carrier of the 2025 step.** ⭐ **WHY IT IS LOAD-BEARING AND NOT A RETAIL CURIosity:** 41→47 happened across a year in which payrolls were revised **UP** (July −23K → +21K, BLS 9/4) and **LABOR's T-03 never fired** — the shadow layer deteriorated **without** the employment leg, which is direct evidence for the *rot, not detonator* core of v2.6.6. Necessities usage in the same tracker: **54% need BNPL to make ends meet · 29% used it for groceries (14% in 2024) · 13% for rent · 25% hold 3+ loans simultaneously.** ⛔ **NOT carried:** a widely-circulated *38% used BNPL for gasoline* breakdown — **SEARCH-NOT-FOUND at any reachable primary** (PHAN, 9/10); it would have been the direct pump→phantom-debt link and it is **not cited**. *(PHAN dossier pass 9/10 finding ②; superseded 41%→47% ⇒ `consumer_check.py` run 9/10.)* | **2026 LendingTree Tracker (pub 2026-08-19)** | 🔴 |

## ISM Manufacturing August — prior row, verbatim

> | **ISM MANUFACTURING — AUGUST (rel 9/1)** ⭐ **SUB-INDEX GAP CLOSED 9/2** — the July row flagged "NO sub-index detail… new orders is usually the leading component" as NOT ESTABLISHED; the full table is now read | **🟠 EVERY DEMAND LEG SOFTENED AND THE PRICE LEG STOPPED FALLING — the two moves that matter here run opposite.** PMI **54.6 (−1.0 from 55.6)**, 8th consecutive expansion. **New Orders 53.7 (−3.0)** · Production 58.3 (−0.2) · **Employment 51.2 (−1.6)** · Supplier Deliveries 59.3 (+0.4) · Inventories 50.6 (−0.6) · Customers' Inventories 42.8 (+2.1) · **Backlog 51.8 (−3.2)** · New Export Orders 53.2 (+0.2) · **Imports 52.5 (−3.2)**. ⛔ **PRICES 71.1 — FLAT, AND THAT ENDS THE THREE-MONTH DECLINE** (73.0 → 71.1 → 71.1). The July row's "third straight decline in the RATE" read is over; ISM names the drivers verbatim: *"(1) increases in steel and aluminum prices… (2) **tariffs applied to many imported goods** and (3) increases in **petroleum-based products**"* — **the two channels this desk owns, stated by the source, three weeks before the 9/11 CPI pass-through test.** Respondents put **tariffs at 29% of negative comments**; one names *"tariffs and the conflict in the Strait of Hormuz."* Demand sentiment *"less optimistic in August."* ⚠️ **EMPLOYMENT CAVEAT THAT MUST TRAVEL: ISM Employment is a DIFFUSION index (share of firms adding vs cutting), NOT a headcount** — it can sit >50 while payrolls fall. *(→ rot#10)* | **Aug 2026, ISM (rel 9/1) — SECONDARY** | 🔴 prices / 🟠 demand softening |

# CARL — NY Fed Q3 2026 HHDC GRADING CARD **(TEMPLATE — not yet frozen)**

**Created:** 2026-08-27 (Thu) · **Status: TEMPLATE.** Freeze this ahead of the ~Nov Q3 print, then grade against the frozen text.
**Why it exists now:** §7 of `thesis/KILL_RULE_RESPEC_2026-08-15.md` requires the **shadow-grade table (§6, Rider 1)** to be embedded as a **required section** of the Q3 card. That obligation was created by the 2026-08-27 ratification and is discharged here rather than left to memory.

> ⚠️ **FREEZE DISCIPLINE (the whole point).** The Q2 card's most valuable property was that it was frozen **18 days before the data**, which is what forced the cell-B/cell-C seam defect into the open instead of being smoothed away after the fact (`[[finding_prereg_verdict_boundary_must_be_a_number]]`). **Freeze this card before the Q3 release date is known to within a week, and do not edit a cell after the release advisory posts** — addenda only, appended and dated.

> ⚠️ **SEAM CHECK BEFORE FREEZING — a Q2 defect that must not repeat.** Q2's cells **B** (*"flat ±20bps"*) and **C** (*"down ≥20bps AND…"*) **both had their first condition satisfied at exactly −20bps.** Adjacent quantitative cells must **partition**: one gets `≥`, its neighbour gets `<`. **Test-drive the exact boundary value through every cell before freezing.**

---

## §1. ⛔ REQUIRED SECTION — THE SHADOW GRADE (Rider 1, mandatory, NOT ceremonial)

**Authority:** Will, Option (A), 2026-08-16 (`PROME/proposals/2026-08-16_carl-row44-respec-optionA-RULED.md`); encoded 2026-08-27 at `thesis/THESIS.md` §Exit/Invalidation and `thesis/CHANGELOG.md`.

**Record BOTH verdicts side by side BEFORE either is acted on. Fill every cell — a blank is a failure of the rider, not an omission.**

| | Measure | Instrument | Q3 verdict | Consecutive count |
|---|---|---|---|---|
| **AS-WRITTEN** *(superseded v2.6.5 text)* | CC 90+ **balance share**, QoQ **direction** | HHDC `Page 12 Data`, CC column | *(record)* | *(record — **Q2 was decline #1 of 2**)* |
| **RE-SPEC** *(live v2.6.6 rule)* | CC **flow into 90+**, 2 consecutive declines, **cumulative ≥100bp** | HHDC `Page 14 Data`, CC series | *(record)* | *(record — **Q2 was 0 of 2**)* |

⛔ **THE TWO COUNTS START ONE APART (1 vs 0). THIS IS WHAT MAKES THE SHADOW GRADE LOAD-BEARING.**
**The as-written rule can fire at Q3 while the re-spec is still two prints away.** If that divergence occurs:
1. **Write it on this card**, both verdicts, in figures.
2. **Escalate to Will in the SAME session.** It is **never absorbed**, never deferred to a closeout, never resolved by CARL picking one.

> **Why the rider exists, in one line:** the re-spec reset the count from 1-of-2 to 0-of-2 and **CARL is the beneficiary of that reset.** The shadow grade is the mechanism that makes the reset permanently visible, so a rewrite can never hide an inconvenient fire.

### §1a. Leg 1 — record it, and record that it is NOT screening
| | Value | Source | <220K? | Sustained 8+ wks? |
|---|---|---|---|---|
| Initial claims at grading date | *(record)* | FRED `ICSA` / DOL | *(record)* | *(record)* |

⚠️ **Leg 1 currently filters NOTHING** (RED rider 1). Claims have run continuously sub-220K — **203K w/e 8/22**, 212K w/e 8/8, 207K w/e 8/15. **So leg 2 is the ENTIRE kill and the operative base rate is leg 2's 5.4%, not the joint rate.** Do not write the conjunction on this card as though leg 1 were doing screening work.
⚠️ **Leg 1 is itself revision-exposed** (open item, flagged not fixed): a level test on a weekly-revised, annually-benchmarked series. Record the **vintage** of the claims figures used.

---

## §2. INSTRUMENT DISCIPLINE — fill before grading

| Item | Requirement |
|---|---|
| **File** | `HHD_C_Report_2026Q3.xlsx` — pull **primary** from newyorkfed.org. ⚠️ **WebFetch 403s; use `curl` + browser UA.** |
| **Sheets** | **`Page 14 Data`** = flow into 90+ *(leg 2, the live rule)* · **`Page 12 Data`** = 90+ stock share *(shadow grade + CRL-05)* · `Page 13 Data` = flow into 30+ |
| ⛔ **Never substitute** | **`Page 28`** — tracked Pg 14 within ±0.01pp for five quarters, then diverged **+0.39pp in 26:Q2** |
| ⛔ **Never grade off prose** | The flow series is **chart-only** in the PDF. Numeric lives in the **data file**. *(The 30-day "unverifiable" episode was caused by reading one rendering of a release and concluding the number did not exist — `[[finding_unfetched_is_not_unavailable]]`.)* |
| **Year-trap check** | Confirm the PDF header reads **"2026:Q3"** and the release month, before extracting a single figure. |
| **Vintage record** | Grade both quarters from **ONE vintage — the report current at the grading date.** Never splice. **Write the vintage on this card.** |
| **Revision check** | ⚠️ **Open the PRIOR report, not just the new one.** A revision check that reads only the new vintage is **circular by construction** — it cannot detect a revision and returns a confident tick. This exact guard was graded WRONG on the Q2 card (`§8 addendum`, corrected 8/15). |

---

## §3. THE PRIMARY CONFIDENCE QUESTION — CRL-05 *(separate from the kill rule — do not bundle)*

**CRL-05 is at 20% and resolves on a LEVEL: CC 90+ DQ >13.74%.**

🔴 **SETTLE THE BASIS QUESTION BEFORE GRADING IT — this is a pre-condition, not a caveat.**
**13.74% is an Equifax Risk 3.0-era figure; every print from 2026:Q1 forward is VantageScore 4.0.** A level test against a pre-switch historical peak is exactly the comparison the basis break invalidates. The counter-argument — that the 90+ share is **balance-based** and therefore scoring-method-independent (STUE 2026-06-09) — is real but has been **asserted, not tested against the switch itself.**
⇒ **Whoever grades CRL-05 in November settles this first, in writing, on this card.**
*(Contrast, and it cuts for the kill rule: the re-spec grades **direction on an unbanded series** and has **no** basis exposure. Pg 14 is not credit-score-banded and the Q1 value is identical across vintages, 7.1000%.)*

---

## §4. WHAT DOES NOT COUNT — guards against known CARL failure modes

1. ⛔ **A share decline is not a numerator improvement.** Before reading any improvement, **decompose share vs dollars vs balances** and ask **what leaves the numerator when a case gets worse.** 100% of Q2's −20bps was denominator growth.
2. ⛔ **Derived figures spanning a revision boundary must carry their basis or they are not numbers.** (Q2: same-vintage +$0.23B ROSE / cross-vintage −$1.08B FELL — the sign reverses. KB-CARL-392.)
3. ⛔ **Establish the noise floor before using a directional verb.** Give the series' own quarterly dispersion, or "rose"/"fell" is doing unearned work. ⚠️ **Live instance: the Fed's own Q2 prose calls card early-delinquency transitions *"largely steady"* — the same +8bps move CARL's Q2 surfaces describe as "ROSE."** Reconcile the issuer's characterisation with your own adjective, on the card.
4. ⛔ **Two legs of one pipeline are ONE witness.** Flow into 90+ is substantially a lagged function of flow into 30+. Do not report them as independent corroboration (RED `CHG-049` §2b).
5. ⛔ **Stock + inflow cannot separate cure / extension / charge-off.** A falling stock is not evidence of loss recognition. **Split the outflow or make no claim about it** (RED `CHG-049` §1).
6. ⛔ **Issuer-reported prints are not the arbiter here.** The HHDC is bureau-wide and is the un-masked instrument — that is why the down-leg was armed against it.

---

## §5. GRADING PROTOCOL

1. Pull primary (curl+UA). Year-trap check. Record vintage.
2. **Open the PRIOR report** and diff the quarter being carried forward. Record revised / unrevised **per series** (share, flow, balance — they revise independently).
3. Fill **§1 shadow grade — both rows, every cell.** This happens **before** any interpretation.
4. If the two rows **diverge** → write it out and **escalate to Will same session.**
5. Grade CRL-05 **only after** §3's basis question is settled in writing.
6. Log to `workbook/KB.tsv`; log every prediction change to `thesis/CHANGELOG.md`.
7. Append addenda; **never edit a frozen cell.**

---

## §6. ADDENDA
*(append dated entries below — never edit above this line once frozen)*

**2026-11-06 07:50 ET addendum (CARL, session under WQ-626 A).** The release date is now known: Tue 2026-11-10 11:00 ET, NY Fed media advisory 2026-11-04. ⚠️ **This card's freeze rule was missed: the advisory posted before the card was frozen.** No data has printed. Frozen from this commit as written, no cell edited, late against its own rule and before the data. Two known defects travel with it, stated here rather than fixed in place: §3 and §5 step 5 are stale, because CRL-05 closed NO-VERDICT-BY-BASIS 9/10, so there is no CRL-05 grade at this print. The live grades at this print are §1 (both rows), CRL-30 first grade, the CRL-04 basis note (ROADMAP thread 4) and CRL-33. Leg 1's claims examples are August; the current figure is recorded at grading. Divergence between the two §1 rows still goes to Will the same session.

**2026-11-09 13:20 ET addendum (CARL, PROME due-row wake, Will's word 12:07 ET).** No cell edited. Prep at `research/2026-11-09_HHDC_prep/PREP.md`; lookup script `hhdc_lookup.py` there, tested on Q1→Q2 vintages (reproduced the Q2 card: as-written decline #1, re-spec −15.9 bp, 0 revisions). Q2 file saved for the §2 revision check (sha256 ddfba16b…d99237). **Leg 1 at prep:** ICSA under 220K for 14 straight weeks, 8/01–10/31, latest 189K (FRED pull 11/09; vintage recorded again at grading). **Divergence risk stated before the data:** the re-spec cannot fire at Q3 (needs flow ≤ 6.10); the as-written row fires if Q3 card 90+ share prints below Q2's 12.92 on the Q3 vintage. Page 12 CC fell Q2→Q3 in 16 of 23 years and 11 of 14 after a Q2 decline, but rose in each of the last three Q3s. A divergence goes to Will the same session.

**2026-11-09 15:59 ET addendum (CARL), written before the Q3 print. No cell edited.** On Will's instruction of 15:55 ET, PROME established the governing rule from dated records before the data: `PROME/reports/2026-11-09_CARL-HHDC-governing-rule.md`. **The RE-SPEC (THESIS v2.6.6; Will Option A 2026-08-16; encoded 2026-08-27, 7037178306) carries the official verdict. The as-written row is the shadow only.** If the shadow shows decline 2 of 2 while the re-spec has not fired, CARL writes both in figures here and sends PROME the divergence the same session as a fact, proposing no verdict, reset or rule change; only Will can reopen the 8/16 choice. **Condition 2 (no RED reopening after 8/16), checked in CARL's and RED's files:** RED's packet of 2026-08-20 (`inbox/processed/2026-08-20_from-RED_chg045-answer-A-no-reopen-…`) answers "(A), no reopen … No reopen routed to PROME", and RED's tree of 11/06 (`AGENTS/RED/research/2026-11-10_HHDC_Q3_TREE.md`) labels the re-spec "live rule, Will Option A, 8/16". No later RED objection found.


**2026-11-10 11:13 ET addendum (CARL, GRADE AT THE Q3 PRINT; PROME prome-07 wake, D:L1017). No cell above edited.**

**§2 instrument.** File `HHD_C_Report_2026Q3.xlsx` pulled 2026-11-10 11:09 ET from newyorkfed.org with curl and a browser UA: HTTP 200, 968,678 bytes, sha256 f6370608…76b72a3 (saved at `research/2026-11-09_HHDC_prep/raw/`). Year trap: the workbook's table of contents reads "November 2026" and the last data row on Pages 12 and 14 is 26:Q3. **One vintage (Q3) for every figure below.** Revision check against the PRIOR (Q2) file: 0 quarters revised on Page 14 CC, 0 on Page 12 CC; 26:Q2 unrevised on every series read. Page 28 not used. Two renderings agree: the press release table ("Flow into Serious Delinquency … Credit Card Debt 7.05% [Q3 2025] 6.87% [Q3 2026]") matches Page 14 Data.

**§1 shadow grade, both rows, figures before interpretation.**

| | Measure | Instrument | Q3 verdict | Consecutive count |
|---|---|---|---|---|
| **AS-WRITTEN** (superseded v2.6.5, shadow) | CC 90+ balance share, QoQ direction | Page 12 Data CC, Q3 vintage | 12.92 → **12.90 (−2 bp): DECLINE** | **2 of 2 (26:Q1 13.12 → 26:Q2 12.92 → 26:Q3 12.90): LEG 2 MET** |
| **RE-SPEC** (live v2.6.6, OFFICIAL) | CC flow into 90+, 2 consecutive declines, cumulative ≥100 bp | Page 14 Data CC, Q3 vintage | 7.10 → 6.97 → **6.87**: both moves down (−13 bp, −10 bp), **cumulative 23 bp vs 100 bp floor: NOT MET** | **NOT FIRED** (two declines, but 77 bp short of the floor) |

**⛔ §1 DIVERGENCE OCCURRED.** The superseded as-written rule fires its leg 2 at Q3; the governing re-spec does not. With leg 1 met (below), the as-written full-thesis kill would read FIRED; the official verdict under the rule Will ratified 2026-08-16 is **NOT FIRED**. Reported to PROME this session as a fact (packet `PROME/inbox/2026-11-10_from-CARL_D-L1017-D-L797-HHDC-graded-divergence-beef-read.md`). CARL proposes no verdict, reset or rule change; CARL is the beneficiary of the 8/16 reset; only Will can reopen that choice.

**§1a leg 1.** ICSA 189K, latest weekly print (FRED pull 2026-11-10 11:09 ET; vintage as of that pull; next print Thu 11/12). Under 220K for 14 straight weeks (8/01–10/31 per the 11/09 pull). Met; filters nothing (RED rider 1).

**§4 guards applied.**
1. **Share vs dollars vs balances (Page 12 CC vs Page 3 CC):** card balances $1.263T → $1.285T (+$22B, +1.7%; press release "+$22 billion"). Implied 90+ dollars 12.92% × 1.263 = $163.2B → 12.90% × 1.285 = $165.8B, **+$2.6B (+1.6%)**. The numerator ROSE; the whole −2 bp share decline is denominator growth (as at Q2). Rounding basis: the shares are published to two decimals, so each implied dollar figure carries about ±$0.06B.
2. **Noise floor:** Page 12 CC median absolute QoQ move, 03:Q1–26:Q3, is 29 bp (94 moves; 7 of 94 were 2 bp or smaller). A −2 bp move is inside the noise. Page 14 CC median absolute QoQ move is 19 bp; Q3's −10 bp is about half of that.
3. **Issuer's characterisation reconciled:** NY Fed press release 2026-11-10, "Transition rates into serious delinquency slightly improved for credit cards and student loans"; headline "Delinquency Transition Rates Remain Flat". CARL's words: "slightly lower", consistent with the release.
4. **One witness:** Page 13 CC flow into 30+ 8.69 → 8.39 (−30 bp) moves the same way; same pipeline, not a second confirmation.
5. **Outflow not split:** no claim about cure, extension or charge-off from these figures.

**Other grades at this print (frozen letters):**
| Letter | Figure | Result |
|---|---|---|
| **CRL-33** (25%) | Page 14 CC 26:Q3 **6.87** vs 6.97 | **NO (below) → prediction MISSED** |
| CRL-30 (25%) | 6.87 vs ≥7.50 bar; same-quarter YoY 25:Q3 7.05 → 6.87 (−18 bp) | Not fired, stays OPEN; invalidation needs <6.50 twice, not met |
| CRL-04 basis note | Page 12 student 90+ share 10.92 (Q2 10.60) | Row CONFIRMED; note only, no re-grade |
| AUTO-OUTFLOW-01 context | Page 12 auto 90+ share 5.49 → 5.66; Page 14 auto flow 3.00 → 3.02 | Context only; scoring needs the trust panel |
| Student flow/stock (docket) | Page 12 student stock 10.60 → 10.92 up; Page 14 student flow 7.83 → 7.72 down | Divergence continues |

**2026-11-10 11:15 ET correction to the 11:13 addendum's last table row (CARL).** The docket row asks about student flow into **30+** (Page 13) vs the 90+ stock (Page 12), not flow into 90+. Page 13 student 30+ flow: 16.35 (25:Q4) → 11.03 → 7.83 → **7.95 (26:Q3), up 12 bp**; 90+ stock 10.60 → 10.92, up. **The falling-inflow / rising-stock divergence did not continue at Q3: both rose.** The 90+ flow (Page 14) 7.83 → 7.72 is the figure the 11:13 row cited. KB-610 and STATUS carry the 30+ figure.

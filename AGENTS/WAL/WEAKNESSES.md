# WAL — Thesis Weaknesses (living counter-argument)

**Last Updated:** **2026-09-24 (session #7 — two rows ADDED, none rewritten: the price-below-EV fact and the CEO's 9/16 Q3 credit pre-guide. No thesis bump.)** Prior: **2026-08-20 (v2.4 fold — MI3 row rewritten: it asserted a "never-run" falsifier for 13 days AFTER it ran and disconfirmed, and carried bear-fast at 10% after v2.4 cut it to 2%. Found in the 8/20 core-file sweep, not by any check.)** Prior: 2026-07-25 (v2.3-aligned rewrite at promotion standup — supersedes the v1-era 3/25 draft, preserved in git history. Live falsifier canon stays `THESIS.md` calibration tables + the frozen grading frames; this file is the standing steelman.)

---

## What Could Break This (**v2.4 state**)

| Weakness | Severity | Status |
|----------|----------|--------|
| ★ **The margin of safety is ~nil — spot oscillates around EV $75.96:** 18.8% at v2.2 → 5.4% at v2.4 → **−0.47% at $75.60 [9/23 close]** → +2.17% at $77.61 [Fri 9/25 close] → **+0.78% at $76.55 [Mon 9/28 close]** (Δ÷EV; STATUS.md owns the live figure). Near zero either way, a short here carries little expected value on this desk's own arithmetic until the Q3 carriers re-weight the bear | **High** | *Added 9/24; corrected 9/28 (it said "0.47% BELOW EV … negative expected value", true only at the 9/23 close).* It went on PRICE (sector + rates), not evidence — EV unmoved since 8/20. Only a Q3 print / appraisal that CONFIRMS re-opens the case |
| ★ **Management pre-guided Q3 credit BETTER at Barclays 9/16** — NPLs $567M → ~$500M (−10%), NCO rate and dollars below Q2, ACL "well over 100%" of NPLs, "six credits … four down, two to go" (KB-WAL-194) | **High if the print confirms** | *Added 9/24.* ⚠️ B2 (third-party transcript, model-extracted), **nonaccrual basis** (full-NPL coverage was 69.1%), and **silent on the $99M loan**. Guidance is what the Q3 frame grades against — a CEO pre-guiding into a buyback has an incentive to lean benign, which is why it is a benchmark and not evidence |
| **Broadening disconfirmed at WAL once** — REG-26 DISCONFIRMED 7/21 (Q2: 0 new office migrations); the FL small-tier watch-card 3-of-3 REVERT 7/25 is cohort corroboration, **not** a WAL counter step. Q3 is data point **2 of 3**; the retire rule's N=3 lands at the **Q4 print (~Jan 2027)** at the earliest (STATUS §EXIT RULES) | **High** | The load-bearing weakness. v2.3 cut Bear-medium 25→16 for exactly this. *Corrected 9/28: it said "disconfirmed twice" and "a 3rd non-confirmation triggers" in the same row as "Q3 is 2 of 3" — self-contradictory.* |
| **Cohort genuinely improving (Hyp A)** — cohort NCO decomp 6/8 + WALTER SIG-723-016 mosaic + own watch-card fill, three independent reads | High | Bear survives only as idiosyncratic; any "systemic regional stress" framing is dead |
| **Capital-return pivot strengthens the bull mechanically** — $150M H2 buyback + NII floor 12-14% absorbing an assumed Sept hike + deposit-cost inflection | High | v2.3 lifted Bull to 27% and Base/Bull ranges; executed on-guide, EV drifts further up |
| **$99M may cure** — borrower brought it current end-June; prospective tenant for a sizable piece | **High** ⬆ *(raised 8/20: with bear-fast at 2%, the appraisal is now a larger share of what is left of the bear)* | Benign appraisal evaporates the single dated bear catalyst; WAL-02's path narrows to grind-only |
| **Crowded short — **5.97M shares short [FINRA 9/15] = 5.48% of shares outstanding** (~5.62% on the old float basis), days to cover **6.4**, the series high (KB-214; was 4.91% float at 6/30); more crowded than at the Q2 print (4.30 days)** — bearish catalysts not sticking; stock +3.61% ON the Q2 print | Medium | Squeeze/pop risk on any bull datum; the pre-registered pop-discipline stack exists because pops are ambiguous |
| ~~**MI3 cuts both ways** — the never-run falsifier could land <25%~~ → ★ **IT RAN, AND IT CUT AGAINST THE BEAR** | ~~Medium~~ **RESOLVED 2026-08-07** | **Q1-26 23.88% · Q2-26 21.20%, both `<24%` PLATEAUED; never reached 25% in 12 quarters (high 24.24%, never within 76bps of its own trigger).** Bear-fast **10% → 2%** at v2.4. ⚠️ **This weakness is now REALISED, not pending** — the honest framing is no longer "untested" but "tested and failed." **Residual 2%** rests on the series being step-prone: from 21.20% *any* qualifying up-step crosses 25% *(REGINALD step-detector, 8/13)*. ⚠️ **V1a ≠ V1 — the SECURED office book, the $99M and the appraisal are untouched by this.** |
| **Management execution track** — Q2: EPS beat, flat NIM, AOCI improving, deposits cohort-leading | Medium | The "compounder" half of the frame keeps compounding |

## Unknowns

- The **$99M appraisal value** (mgmt: not yet received) — the highest-variance single datum either direction.
- ~~**MI3 trajectory** — FFIEC PDD overdue~~ ✅ **CLOSED 2026-08-07 — it ran** (12-quarter series, `workbook/MI3_SERIES.tsv`). **Successor unknown, and it is a different question:** MI3 *dollars* are **+13.7% YoY** ($2,246M → $2,555M, Q2-25→Q2-26) but **−6.4% over the last two quarters** ($2,730M → $2,555M, Q4-25→Q2-26; `MI3_SERIES.tsv`). *Corrected 9/28: it said the book "is growing" — true only on the YoY window.* Name the window before any direction word.
- ★ **NEW 8/20 — NDFI nonaccrual $122.5M on a $15.81B book (0.77%).** One quarter only; in a 26-bank sample only WFC carries more in absolute dollars. **No trajectory pulled — this is the largest genuinely-open unknown on the desk.**
- **Lender-finance quality-of-names** (2,000 obligors) — V3's residual question, unresolved since Q1.
- **Litigation path** — WAL v. Jefferies ($126.4M claim, NY Sup. Ct.) timeline/recovery; Cantor residual ($72.4M gross, $3.5M specific allowance left at 3/31 — corrected 2026-09-24 from an untraced ~$46M; see CHANGELOG) + senior liens.
- Whether the **H2 NPL-resolution path** (CEO 9/16, B2: four of six resolved, the last two in Q4 — and the $99M is NOT one of the six, KB-112) resolves at par or with charge-downs.

## Monitoring for Thesis Break (mirror of STATUS §EXIT RULES — that table carries FIRED state; this one carries meaning)

| Signal | Meaning |
|--------|---------|
| Q3 deck slide 12 + call: 0 new office migrations (DP2) + benign appraisal (8-K / Q3 call / Q3 10-Q) | Bear-medium kill → single digits / retire path |
| ~~MI3 <25% at FFIEC run~~ ✅ **FIRED 2026-08-07** | **Bear-fast kill — EXECUTED.** Weight 10% → 2% at v2.4 (not 0%: the trigger stays reachable via a single up-step). **Re-tests each quarter the Call Report lands; next ~Oct-Nov, and the FFIEC JWT expires 11/5 INSIDE that window.** |
| (funded + unfunded ACL) ÷ total nonaccrual >100% (pinned 9/24; full-NPL reported alongside) | Reserve-adequacy leg closes |
| Insider buying (esp. CFO Idnani) | Insiders see floor |
| Office classified <$250M or CRE-NOO C/O normalizing | Grind residual fading |

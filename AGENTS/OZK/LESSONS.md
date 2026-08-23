# LESSONS.md — OZK Mistake Patterns & Rules

*Read at boot. Learn once, prevent forever. This file is for verified mistakes that burned us — each with a prevention rule. For Will's working preferences and data source learnings, see `MEMORY.md` (Feedback + Findings sections). Seeded from REGINALD/LESSONS.md during OZK spinout 2026-04-24: 6 rules copied verbatim, 1 rewritten for OZK (NDFI), 1 skipped (hub-agent-only).*

---

### [Data] — Verify Agent Data Against Primary Filings
**Mistake:** PSEC was reported at 35% PIK — actual was 8.6% per SEC filing. Consumer finance names (SYF, BFH, ALLY) were assumed stressed but SEC filings showed improvement.
**Rule:** Before any metric informs a trade, verify against the 10-K/10-Q. Agent research is a starting point, not ground truth.

### [Data] — OZK CIB/NDFI Is Not Monolithic
**Mistake pattern:** Treating OZK's CIB segment or NDFI exposure as a single risk bucket misses that the sub-segments behave very differently. Fund Finance (capital call subscriptions to PE funds), Lender Finance Group (lending to non-bank lenders), Indirect Lending, and other CIB lines have different collateral, credit, and competitive dynamics.
**Evidence:** Q1 2026 — Jake Munn (CIB President) disclosed OZK is *pulling back* from Fund Finance due to non-bank lender + insurance-company price/structure competition; Lender Finance Group also showing compression. Two of four CIB sub-segments in managed retreat. Meanwhile written Mgmt Comments show Fund Finance growing $210M → $1.275B YoY — no commentary on margin erosion.
**Rule 1:** Decompose OZK CIB/NDFI by sub-segment before assessing risk. Don't treat it as monolithic.
**Rule 2:** Verbal-only disclosures (earnings call transcript) that don't appear in written Mgmt Comments PDFs are the leading signal. Watch for disclosures that vanish between spoken and written form — they're telling you what management doesn't want formalized.

### [Analysis] — Hidden CRE Methodology ⚠️ **RECIPE DEFECTIVE FOR OZK — read the amendment below before using**
**How to screen:** Pull FFIEC Call Report Schedule RC-C Part I. Item 4 = C&I loans. Memo Item 3 (RCON2746) = "Loans to finance CRE not secured by RE." Ratio = Memo3/Item4. Flag if >20%.
**Key finding:** ~~OZK worst in screen at 37.6%.~~ ⚠️ ***[RETRACTED 2026-08-23 — BOTH HALVES, by the screen's own owner.* **(i) The `37.6%` number is dead on four independent paths:** it reproduces at no quarter of OZK's own 18-qtr FFIEC series (either basis), at no quarter of REGINALD's 14-bank cohort re-run, at no quarter of the FDIC's own API at a different agency, and at no quarter of the 14-qtr FDIC ratio series. Live: **9.35% at Q2-26**, *below the screen's own >20% flag for two straight quarters.* **(ii) "Worst in the screen" is FORMALLY RETRACTED by REGINALD** (8/13 cohort re-run, 14 banks × 4 qtrs, 56/56 sourced): **OZK ranks 5th of 14 on BOTH bases** — below WAL, CUBI, MTB and EGBN on the legacy basis. OZK is instead the cohort's **fastest faller**, MI3 dollars **−64% YoY**. ⚠️ **And the guard's stated rationale was itself wrong:** this is a **single-cell data defect** at OZK's 12/31/2025 vintage (the other four legacy cells reproduce to 2dp), **not** the screen-level item-9.a defect the 8/7 banner asserted. The number stays kill-on-sight; the reason it is dead changed. ⛔ **Scope fence: MI3 is CRE NOT SECURED by real estate — RESG and every secured book are a different object and are UNTOUCHED by this retraction.** Sources: `inbox/processed/2026-08-13*_from-REGINALD_*` · `MI3_2025Q3_ADJUDICATION.md` · `CALL_REPORT_2026Q2_LOG.md` §3.]*** WAL ratio is GROWING (15.5% → 24.2%), only bank with upward trend *(WAL's leg re-confirmed at the 8/13 re-run: 24.24% at 12/31/25 reproduced to 2dp, live 21.20% Q2-26 and falling — **WAL is the only name the legacy >20% screen still catches, and on the uniform basis it catches nobody**)*.

> **⚠️ AMENDMENT 2026-08-07 — the recipe above has a denominator defect, and its OZK result does not reproduce.**
> **(1) The denominator is wrong for OZK.** `RCON2746`'s own FFIEC definition places its balance in RC-C items **4 AND 9**. For OZK the whole balance is in **item 9.a**: `RCONPV09` ("Other loans to nondepository financial institutions") ≡ `RCON2746` **to the dollar in all six quarters the Memo-10 breakdown exists** (Q1-25 → Q2-26). Dividing by item 4 divides the numerator by a base that contains ~none of it. **Always report BOTH bases, labeled.** *(WAL hit the same defect the same day — its proposal P8. There it over-states; here it is a category mismatch.)*
> **(2) The 37.6% does not reproduce at any of 18 quarters, on either basis.** Recipe basis: 294.93% (Q1-22) → **9.35%** (Q2-26). Fuller basis: 67.00% → **5.46%**. OZK is now **below the screen's own >20% flag** for two consecutive quarters.
> **(3) Scope guard.** MI3 measures CRE-purpose lending **NOT secured by real estate**. It says nothing about the secured book — RESG, IQHQ/RaDD, classified balances, the 11 tracked credits. **Do not read a MI3 collapse as a CRE-thesis weakening.**
> Working → `CALL_REPORT_2026Q2_LOG.md` §3 · series → `workbook/CALL_REPORT_SERIES.tsv`. Disposition of the 37.6% line is REGINALD's (they own the screen) — proposals P-OZK-1/2, Will/PROME-gated, not applied.

### [Process] — Reproduce the Baseline Before You Grade Against It
**Mistake:** Two independent 2026-08-07 first-run Call Report pulls each found their recorded baseline wrong — OZK's 37.6% MI3 unreproducible at 18 quarters; WAL's "+8.7pp over **2** quarters" actually **6** quarters, making the trend look 3× steeper than it was. Both had been load-bearing for months, in multiple surfaces, with the recipe written down the whole time.
**Rule:** Before a number grades anything, recompute it from the primary on its stated basis. If the levels don't reproduce, the correct output is a **basis dispute, not a verdict.** Two-endpoint claims ("X → Y, fastest in cohort") must carry the **interval** and be checked against the full series — the shape of a series is not recoverable from its endpoints. **The recipe being recorded is not the check being run.**

### [Process] — Root `CLAUDE.md` and `AGENTS/OZK/CLAUDE.md` Are Two Different Files — Cite the Path, Don't Cite From Memory
**Mistake (2026-08-07):** I reported the disproved "37.6% MI3" figure as living in **root `CLAUDE.md`** — a Will-gated fleet doc — in the THESIS banner, the log, TODO, the REGINALD packet and the PROME delivery. It does not: root has **zero** occurrences of "37.6". Every quote was from **`AGENTS/OZK/CLAUDE.md:16`**, which auto-loads *alongside* root when the session launches in-folder, so both were in context and I merged them. PROME caught it with one grep. The error **inflated the blast radius of a Will-facing proposal** (fleet-doc exposure → OZK-local only) and I had recommended sequencing P-OZK-2 first partly because of it.
**Rule:** before attributing a quote to a **shared/root** doc, `grep` that exact path. Two `CLAUDE.md` files are in context at all times and neither is labeled in the injected text. **Cite `file:line`, never "root CLAUDE.md says" from recall** — and the stakes are asymmetric: mis-crediting *upward* (agent-local → root) escalates something into Will's gated surface that was never there. *(Generalizes: this is the doc-mirror class — the same figure legitimately living in several surfaces is exactly what makes the misattribution easy and expensive.)*

### [Process] — A Threshold on a Transit Bucket Is Mis-Specified
**Mistake:** THESIS kill-criterion §1 graded *past-due* (a bucket credits pass **through**) and fired at Q2-2026 — in a quarter when the 30-89 bucket emptied −88% **into** nonaccrual, OREO and charge-off, with NPA **+31.9% QoQ**. The criterion's literal condition and its stated meaning ("the migration pipeline is not flowing") pointed in **opposite directions**.
**Rule:** Threshold a **stock**, not a **transit bucket**. Before pre-registering a level, ask: *can this measure fall because the underlying got better, AND fall because it got worse?* If yes, it cannot grade. Pair it with a bucket-invariant companion (30-89 + nonaccrual + OREO), or with the destination buckets, so the direction is recoverable. ⚠️ **And when such a criterion does fire, adjudicate the mechanism before recording the kill — the decomposition that settles it is usually in the Call Report and absent from the supplement.**

### [Analysis] — Distinguish Classification Levels
Three levels of CRE masking:
1. Extend-and-pretend (don't force refinancing)
2. Mark-to-model (don't write down)
3. Classification (call CRE "C&I" if unsecured) ← Memo Item 3
All three can coexist at the same bank. ~~OZK's 37.6% MI3 baseline means classification masking is the primary vector~~ ***[RETRACTED 2026-08-23 — the baseline is dead (see §Hidden CRE Methodology) and with it the claim that classification masking is OZK's PRIMARY vector. That ranking was derived from the ratio, so it does not survive the ratio. On the live evidence the primary vector reads as **(1) mark-to-model** — nonaccrual $296.6M carried at collateral FV $281.5M of which **$250.4M carries $0 ALL**, marked to appraisal rather than market severity — and **(2) extend-and-pretend**, which management described on its own 7/22 call (RaDD multi-year extension + recap, interest paid from interest reserves, "will remain a pass-rated credit"). ⚠️ Stated as a re-read of vector ORDERING, not a thesis move: no weight, grade or probability changes on it.]*** Watch for extend-and-pretend + mark-to-model signals (e.g., foreclosed asset transfers at prior-appraisal values, substandard accrual without specific reserve).

### [Process] — Date Your Data
**Rule:** Every metric must have a date. "Office DQ is 12.34%" means nothing without "as of Jan 2026." Stale data in STATUS.md causes wrong analysis.

### [Process] — STATUS.md Is Not a Research Report
**Rule:** STATUS.md is a dashboard — current state, thresholds, positions. Research detail belongs in archive/, workbook/, or source files. If STATUS.md exceeds 10KB, it needs pruning.

### [Data] — Verify Real-Time Prices Before Building Narratives
**Mistake:** STATUS.md stated Brent $118-125 and built an entire FL energy shock cascade on that figure. Actual was $81.40. The error propagated through multiple sections before being caught.
**Rule:** Always confirm price levels from a live source before modeling downstream effects. A 45% error on an input produces garbage on all outputs.

---

*Last reviewed: 2026-08-07 (Q2 Call Report LOG-ONLY session — MI3 recipe amendment + 2 new process rules). Prior: 2026-04-24 (seeded from REGINALD/LESSONS.md during spinout).*

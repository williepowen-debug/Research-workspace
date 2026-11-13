# L226 — VX-BND-18 escalation-leg retune: DRAFT for Will (not encoded)

**Written:** 2026-11-13 10:2x ET, BOND (orch), PROME prome-72 due-row wake. Claude Code, `claude-opus-5-5`.
**Row:** `PROME/DOCKET.tsv` physical line 226. **Vector:** `workbook/VX.tsv` VX-BND-18 (FHLB advances, regional-bank backstop), score 2, thresholds UNCHANGED by this file.
**Status of everything below:** a gate DRAFT. It creates a level, so it is Will's. Nothing here is written into VX.tsv, STATUS, THESIS or TRADE as a threshold.

## 1. Answer in one paragraph

The leg as written ("advance-depletion narrative") stays ungradeable: it names no series and no level. The replacement instrument BOND named on 8/23, system-wide unused FHLB borrowing capacity, **does not exist in the source BOND named**: the Combined Financial Report (CFR) publishes no system borrowing-capacity figure (checked in full text of the 6/30/2026 CFR; the only "unused" line is "Unused lines of credit - advances", an off-balance-sheet commitment of the FHLBanks, a different object). The CFR does publish, every quarter, an issuer-stated **collateralization ratio for all borrowers** (eligible collateral divided by advances plus other credit products). Across 30 quarters (2019Q1–2026Q2) that ratio's two lowest prints are the two stress quarters: **2.8 at 3/31/2023 (the regional-bank run) and 3.0 at 3/31/2020 (the COVID dash for cash)**; every other quarter is 3.2 or higher. Latest **3.7 at 6/30/2026**. BOND's draft: replace the narrative clause with **"issuer-stated all-borrower collateralization ratio ≤3.0 at a quarter-end"**, keep the >$900B leg as is. Alternative: strike the clause and leave >$900B alone.

## 2. Base rate (issuer data, 30 quarters)

Source: FHLB Office of Finance CFRs, `https://cdn.fhlb-of.com/files/...` (index page `https://www.fhlb-of.com/investor-resources/financial-reports/combined/`), downloaded 2026-11-13 10:1x ET. "Stated" = the sentence "The collateralization ratio for all borrowers was X at <date>" (one decimal, issuer's rounding). "Computed" = Table 18 (Advances, Other Credit Products, and Collateral Outstanding) collateral ÷ (advances + other credit), parse checked against every stated value. Files: `table18_2019Q1-2026Q2.txt` (computed, both borrower groups), `stated_ratios_2019Q1-2026Q2.txt` (stated all-borrower column complete; its large-borrower column has regex gaps, use the table file), code `table18.py`, `extract.py`.

| Quarter-end | Advances, all borrowers | Collateral, all borrowers | Ratio stated (computed) | Note |
|---|---:|---:|---|---|
| 3/31/2019 | $670.9B | $2,665.4B | 3.2 (3.21) | |
| 6/30/2019 | $686.5B | $2,725.8B | 3.2 (3.22) | |
| 3/31/2020 | $797.2B | $2,878.8B | **3.0 (2.96)** | COVID; advances below $900B |
| 12/31/2021 | $349.4B | $2,224.8B | 4.6 (4.62) | series high |
| 12/31/2022 | $827.1B | $3,264.4B | 3.3 (3.30) | |
| 3/31/2023 | $1,050.2B | $3,446.3B | **2.8 (2.85)** | regional-bank run; series low |
| 6/30/2023 | $891.2B | $3,410.4B | 3.2 (3.20) | |
| 12/31/2025 | $677.1B | $3,679.4B | 4.2 (4.16) | |
| 3/31/2026 | $735.6B | $3,583.5B | 3.8 (3.79) | |
| 6/30/2026 | $813.3B | $3,753.3B | **3.7 (3.66)** | latest |

Full 30 rows in the table file. **Fire rate at ≤3.0 (stated): 2 of 30 quarters (6.7%), both stress quarters. Next-lowest stated value 3.2 (2019Q1, 2019Q2, 2023Q2).** Distance from latest: 0.7 (3.7 vs 3.0).

**Why it can add something the >$900B leg cannot:** the collateral pool grew from $2.67T (3/31/2019) to $3.75T (6/30/2026), so a fixed dollar line means less every year. With 6/30/2026 collateral and other credit, $900B of advances is a ratio of about 3.38, a level that was routine in 2019. And at 3/31/2020 advances were $797B, so the $900B leg missed the COVID quarter the ratio caught. (Advances here are Table 18 principal, $813.3B at 6/30/2026; VX-BND-18's $810.7B is the balance-sheet figure, a different basis.)

## 3. Caveats that must travel with the draft

1. **n=2.** Two stress quarters in 30. The ratio separated both, but two cases do not validate a threshold; it is a base rate, not a test.
2. **It confirms, it does not warn.** It is a quarter-end snapshot published about six weeks later (Q3 2026 due 11/13). The 3/31/2023 figure is a snapshot taken three weeks after SVB failed (3/10/2023) and published weeks after that (its 2023 release date not verified here). Useful for scoring the vector; no use for positioning ahead.
3. **It cannot see one bank running dry.** The CFR itself says borrowers are not cross-collateralized. SVB's 2023 problem was a single bank's collateral, invisible in a system aggregate with $3.4T of collateral.
4. **It is gross, not capacity.** Eligible collateral is market value or unpaid principal before each FHLBank's haircuts, so the ratio is not "room left to borrow".
5. **The large-borrower version is broken at one point.** Borrowers with ≥$1B of advances: stated 1.9 at 12/31/2023 (collateral share 36.5% vs 57–59% the quarters either side, no stress). Unexplained; do not use that sub-series.
6. **Mostly the advances level in another unit.** Collateral moves slowly, so the ratio mainly tracks advances; its only independent content is the growth of the collateral pool.

## 4. Corrections to BOND's own 8/23 return

- The candidate instrument ("system-wide unused FHLB borrowing capacity / advances-to-capacity") was named without checking that the CFR publishes it. It does not.
- The deferral premise was wrong: the retune did not need the Q3 2026 CFR. A 30-quarter base rate sat in the issuer's back reports the whole time; the wait from 8/23 to 11/13 bought nothing except the discovery that the named series does not exist.

## 5. Today's Q3 report

Not posted at 10:18 ET 11/13: the combined-reports index lists through 2026Q2; `cdn.fhlb-of.com/files/2026/2026Q3CFR.pdf` returns 403 (the Q2 path returns the PDF); Q3 Combined Operating Highlights is posted. The VX-BND-18 Q3 re-score and REGINALD's REG-T-06 leg 3 wait on it. If Will adopts option A, the Q3 stated ratio is the first evaluation.

## 6. Options for Will (BOND recommends A)

| Option | What changes | For | Against |
|---|---|---|---|
| **A (recommended)** | Red leg reads: "CFR issuer-stated all-borrower collateralization ratio ≤3.0 at a quarter-end OR >$900B system-wide" | Replaces an ungradeable clause one for one, so the rule count does not grow; scales with the system; fired at both stress quarters and nowhere else in 30 | n=2; lags about six weeks; aggregate only |
| B | Strike "advance-depletion narrative"; red leg is >$900B alone | Fewest rules | Keeps a fixed-dollar line that missed 3/31/2020 and drifts easier to reach as the collateral pool grows |
| C | Leave as is | none | Leaves a clause nobody can grade; it has sat ungraded since 8/23 |

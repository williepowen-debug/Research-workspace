# L726 — Illiquidity basis: exact liquidity criterion and unknown-handling rule (proposal for Will's ruling)

**Written:** 2026-10-21T22:13 ET by SHADE (PROME spawn prome-56, Claude Code, Opus 5.5). **DOCKET L726** (due 2026-10-23), successor of WQ-423. **Status of this document: PROPOSAL.** Nothing here is adopted, no grade is issued, the 30% red-flag level is unchanged, and no prior reading is regraded. PROME registers a fresh WQ row for Will's word.

**What it answers:** the GA-matched illiquidity ratio proposed on 2026-10-12 (`research/GAP_INVESTIGATION_2026-10-12.md` §Measurement) was blocked on two missing pieces: (1) an exact test for when an asset-backed security counts as illiquid, and (2) what to do when the evidence is missing. Both are specified below, from the statutory form's own fields, so the test can be run by anyone holding the filing.

---

## 1. The ratio (unchanged from the 10/12 proposal, made exact)

**Charter Key Ratio #2, proposed GA-matched form:**

> **Illiquidity Ratio (GA) = (Mortgages + Schedule BA + Confirmed-illiquid ABS) / GA net admitted assets**

| Term | Exact statutory source (Life/Annuity blank) | Basis |
|---|---|---|
| Mortgages | Page 2 (Assets), Line 3 "Mortgage loans on real estate (Schedule B)", Column 3 net admitted | Whole line, as the charter prescribes. No liquidity test. |
| Schedule BA | Page 2, Line 8 "Other invested assets (Schedule BA)", Column 3 net admitted | Whole line, as the charter prescribes. No liquidity test. |
| Confirmed-illiquid ABS | Schedule D Part 1 Section 2 (asset-backed securities, in scope of SSAP No. 43), Column 8 Book/Adjusted Carrying Value, only the holdings that pass §2 below | Holding by holding. |
| Denominator | Page 2, Line 26 "Total assets excluding Separate Accounts, Segregated Accounts and Protected Cell Accounts", Column 3 net admitted | GA only. Separate accounts are excluded (NAIC Supplemental Investment Risks instructions exclude SA; DLIC FY25 audit item 1 uses GA). |

Line labels verified at the DLIC FY2025 original annual statement Page 2 (Line 8 BA net admitted $1,601,744,585; Line 26 net admitted $45,903,192,677). **Same insurer, same valuation date, same statement version (original vs amended named, jurat cited) for every term — mixed vintages withhold the reading.**

---

## 2. The liquidity criterion — three tests, applied to each Schedule D-1 Section 2 holding

The standard each test implements is the SEC's definition of an *illiquid investment* (17 CFR 270.22e-4(a), eCFR version 2026-09-01): **"any investment that the fund reasonably expects cannot be sold or disposed of in current market conditions in seven calendar days or less without the sale or disposition significantly changing the market value of the investment."** SHADE borrows the definition, not the fund's self-classification (no fund's classification of a CUSIP is used as evidence here).

A holding is **CONFIRMED-ILLIQUID** only if **at least one** test below is met **by a cited primary record**:

| Test | CONFIRMED-ILLIQUID when | Primary evidence that qualifies | What does NOT qualify |
|---|---|---|---|
| **T — Transfer** | The holding is legally restricted as to sale. | (a) **Schedule D-1-2 Column 3 Restricted Asset Code = `R`** — NAIC definition: *"Letter stock or otherwise restricted as to sale – excluding FHLB capital stock"*, with the NAIC note *"Private placements are not to be included unless specific restrictions as to sale are included as part of the security agreement."* (b) A transfer restriction in the holding's own governing document (indenture, offering memorandum, note purchase agreement): issuer/sponsor consent required, transfer limited to affiliates, or a lock-up extending past the valuation date + 7 days. | Private placement or 144A status by itself (NAIC's own note excludes it). Affiliation. Encumbrance codes (see §3). |
| **R — Redemption** | The holding's only route to cash before maturity is redemption from, or distributions by, an underlying vehicle, and that route takes longer than 7 calendar days or is at the manager's discretion. | The holding is on a "Not Self-Liquidating" line (lines 1319999999–1349999999: equity-backed and other not-self-liquidating ABS, e.g. rated-note feeders) **and** the underlying vehicle's document shows no holder redemption right, or notice + settlement > 7 days, or a gate / discretionary suspension. | The line placement alone (that makes it a PROXY, §4). A rating. |
| **E — Executable market** | A primary record shows the holding could not be sold within 7 days at a price near its carrying value. | A filer, issuer, trustee, court or regulator record stating that no market exists for that holding or that a sale attempt failed / drew no bid; or a recorded sale at a price materially below carrying value (the filer's own Schedule D Part 4 or a court/regulator record). | Absence of a quote. Level 3 fair-value status (an input-observability label, not a market test). A wide spread. |

A holding is **EVIDENCED-LIQUID** (excluded from the numerator, and lowers the ceiling in §4) only if a cited record shows:
- **L1 — Agency category:** the holding is on Agency lines **1019999999–1049999999** (agency residential/commercial MBS, guaranteed or not/partially guaranteed). ⚠️ This is a **category rule** (agency pools trade in deep dealer markets; INFERRED, not a per-CUSIP market test) — it is listed separately so Will can accept or strike it.
- **L2 — Executed trade:** a reported executed trade in that CUSIP within the 30 calendar days before the valuation date, source and date cited. ⚠️ Public trade dissemination coverage for the non-agency ABS sub-classes (CLO, private ABS) is **UNVERIFIED** here; where no disseminated record exists, L2 is simply unavailable and the holding stays in PROXY or UNCLASSIFIED.

Everything else is not classified by this test and goes to §4.

---

## 3. Encumbrance is a separate measurement, not illiquidity

Schedule D-1-2 Column 3 also carries codes for assets **not under the reporting entity's exclusive control**: `LS` loaned · `RA`/`RR`/`DR`/`DRR` repo forms · `C` pledged (non-FHLB) · `CF` pledged to FHLB (incl. assets backing funding agreements) · `DB`/`DBP` option pledges · `RF` FHLB stock · `SD` on deposit with a regulator · `M` multiple reasons · `SS` short sale · `O` other (NAIC Investment Schedules General Instructions, 2026 edition, p. 506).

**Rule:** a pledged or lent asset is *unavailable*, not *unmarketable*. Codes other than `R` never confirm illiquidity. They are summed by code into an **ENCUMBRANCE companion** reported beside the ratio (consistent with the 10/12 rule that the $120.985B Athene restricted total is not all FHLB collateral and not free liquidity). **`M` and `O` are ambiguous** (either may hide an `R`): they go to PROXY until the filer's Note 5L (restricted assets) or the governing document resolves them.

*Operability check (DLIC FY2025, original annual statement, Schedule D-1-2 PDF pp. 278–313, text extraction):* restricted-code tokens found were **`CF` 368 and `C` 60; no `R` token found** (SEARCH-NOT-FOUND on an imperfect PDF text extraction — INFERRED, not a verified zero). So on DLIC the transfer test via the statutory code confirms nothing; T(b), R and E need holding-level documents not yet obtained.

---

## 4. Unknown-handling rule — floor, ceiling, and a grade only when the bounds agree

Every Schedule D-1-2 holding lands in exactly one bucket:

| Bucket | Rule | In numerator? |
|---|---|---|
| **C — Confirmed-illiquid** | ≥1 of T/R/E met by a cited primary record | Yes (FLOOR) |
| **L — Evidenced-liquid** | L1 or L2 met by a cited record, and no C test met | Never |
| **P — Private-ABS proxy** | No C or L evidence, and ≥1 proxy flag: affiliated ABS line (1899999999 subtotal lines) · Private Security Code 2 (144A) or 3 (private placement) where the field is available · SVO symbol PL / PLGI / Z / RT-family / ND* · Not-Self-Liquidating or Non-Financial Full-Analysis line · fair value Level 3 · Restricted Asset Code `M` or `O` | Reported separately; **never grades alone** |
| **U — Unclassified** | No C or L evidence and no proxy flag, or the needed fields are not in the available filing | Reported separately; **never treated as zero and never as illiquid** |

**Three published numbers, always together, same filing:**
- **FLOOR** = (Mortgages + BA + C) / GA
- **PROXY-INCLUSIVE** = (Mortgages + BA + C + P) / GA — a label, never a grade
- **CEILING** = (Mortgages + BA + C + P + U) / GA = (Mortgages + BA + all ABS − L) / GA

**Grading against the unchanged >30% red flag:**
- **RED** only if **FLOOR > 30%**.
- **NOT RED** only if **CEILING ≤ 30%**.
- Otherwise **INDETERMINATE** — reported as "between FLOOR and CEILING", with two break-even dollar figures: confirmed-illiquid ABS needed to breach, and evidenced-liquid ABS needed to clear. Never rounded into either grade.
- **UNAVAILABLE (no reading)** if any of the four terms, the GA denominator or the single-vintage condition is missing.

**Why bounds instead of a rule of thumb:** "missing quote = illiquid" over-states, "unknown = liquid" under-states, and the 10/12 record already showed the two framings straddle 30% on the same insurer (9.75% vs 37.24%). The bound rule cannot be pushed across the line by how the unknowns are guessed — only by evidence.

---

## 5. No double counting — four rules

1. **Insurer-level line items only.** The numerator sums carrying values that appear on the insurer's own Schedules B, BA and D-1-2. A fund's or vehicle's underlying collateral (look-through) is **never** added on top of the insurer's carrying value of its interest in that fund or vehicle.
2. **Each CUSIP / BA line once.** Statutory schedules are mutually exclusive by construction (an SSAP 43 bond is on D-1-2, a fund LP interest on BA); if the insurer holds both a BA interest and ABS notes of the **same vehicle**, both are distinct insurer assets and both count — tagged as a same-vehicle pair so a reader sees the concentration, not added a third time.
3. **Overlapping proxies never stack.** The SSAP 25 affiliate-contingent bond figure (DLIC $12,619.338M) overlaps the ABS book and issuer-credit bonds; it stays a **separate labelled proxy row** (the 37.24% figure), never added to C, P or U.
4. **Group look-through figures stay outside.** AMAPS named-position totals ($13.515B floor), Retirement Services totals and other consolidated GAAP figures are already inside the consolidated investments; they never enter an entity-level statutory numerator.

Separate-account assets and GA guarantees on SA products go to the **separate SA/guarantee companion** already proposed on 10/12 (DLIC FY2025: GA received $175.175M risk charges, paid $97.917M guarantee amounts).

---

## 6. Worked illustration on the existing DLIC FY2025 inputs (NOT a grade)

Inputs = the corrected FY2025 audited statement, USD millions, already reconciled on 10/12 (`sources/2026-10-12_gap-investigation/RECONCILIATION_INPUTS.json`): GA net admitted **45,903.193** · Mortgages **2,874.148** · BA **1,601.745** · formal ABS **10,441.030**. Holding-level C/L/P/U classification has **not** been run.

| Quantity | Value |
|---|---:|
| FLOOR with C unknown (C ≥ 0) | **≥ 9.7507%** |
| CEILING with L unknown (all ABS) | **≤ 32.4965%** |
| Status under the proposed rule today | **INDETERMINATE** (bounds straddle 30%) |
| Confirmed-illiquid ABS needed to breach (FLOOR > 30%) | **$9,295.065M = 89.02% of the ABS book** |
| Evidenced-liquid ABS needed to clear (CEILING ≤ 30%) | **$1,145.965M = 10.98% of the ABS book** |

Arithmetic: 0.30 × 45,903.193 = 13,770.958; 13,770.958 − 4,475.893 = 9,295.065; 14,916.923 − 13,770.958 = 1,145.965. ⚠️ The DLIC statement visibly holds agency (GNMA) pools on D-1-2 lines 1019999999+, so if L1 is accepted the clear-side break-even is plausibly reached — **not established here: the agency subtotal amounts did not extract reliably from the PDF text and were not read from the image.** This is the next mechanical step after a ruling, not before.

---

## 7. Ruling requested (for PROME to register)

1. Adopt §1–§5 prospectively as the definition of charter Key Ratio #2 (GA perimeter), keep **>30%** unchanged, and regrade nothing retrospectively. **SHADE recommends yes.**
2. Accept or strike **L1** (agency-category liquid rule). SHADE recommends **accept**, labelled as a category rule.
3. Charter wording change follows the ruling (SHADE's own charter line, Will-gated because it changes a ratio definition).

**Known limits:** Private Security Code (Column 38) did not appear in the printed DLIC PDF pages read (SEARCH-NOT-FOUND) — it may exist only in the electronic data table, so P will often rest on line placement and SVO symbol. Holding-level documents for T(b)/R/E are not obtained for any insurer. No new data acquisition was performed for this definition beyond the public sources below.

## Sources (retrieved 2026-10-21, hashes are of the retrieved file)

| Source | Use | Receipt |
|---|---|---|
| [NAIC Annual Statement Instructions, Life/A&H/Fraternal, 2026 edition](https://content.naic.org/sites/default/files/publication-asi-lua-25.pdf) | Restricted Asset Code list (p. 506); Schedule D-1-2 line categories (p. 636), Column 3 Restricted Asset Code, Column 8 BACV, Column 38 Private Security Code (pp. 637–650); SVO administrative symbols (p. 639) | 7,184,683 B, SHA256 `40386c6d1183a4a34d738738703e70c7f8dbe6d025bc2115538cca1b2695ccbc`; raw kept in session scratch, not committed |
| [17 CFR 270.22e-4 via eCFR API, version 2026-09-01](https://www.ecfr.gov/api/versioner/v1/full/2026-09-01/title-17.xml?section=270.22e-4) | Definitions of illiquid / less liquid / highly liquid investment | SHA256 `c2325a97756bb3ab025c8d329158ae8c5ee30fedd9bc067f422c7a6e42127e51` |
| DLIC FY2025 original annual statement (source id DLIC_ORIGINAL, `sources/2026-10-12_gap-investigation/SOURCE_INDEX.md`) | Page 2 line labels and values; D-1-2 restricted-code tally | Existing 10/12 receipt, SHA256 `cc9acf23…a9d`; machine-local store `/home/willi/research-artifacts/SHADE/gap-investigation-2026-10-12/` |
| DLIC FY2025 audited statement (DLIC_AUDIT, same index) | GA / mortgage / BA / ABS inputs, SA guarantee flows | Existing 10/12 receipt |

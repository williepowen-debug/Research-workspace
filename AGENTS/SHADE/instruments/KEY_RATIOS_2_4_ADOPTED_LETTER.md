# Charter Key Ratios #2 and #4 — ADOPTED LETTER (verbatim transcription)

**Ruling:** Will 2026-10-21 22:46 ET, verbatim *"Approve 472 A, 473 A, 474 A, 475 A, 476 A"* — **WQ-473 A** (L726 illiquidity basis: adopt + accept L1) and **WQ-474 A** (L727: TSR stays UNAVAILABLE; SHADE-R v1 and SHADE-T v1 adopted as named diagnostics, no threshold, never labelled TSR, no R+T sum). Records: `PROME/WILL_QUEUE.md` rows 473/474; PROME packet `inbox/processed/2026-10-21_from-PROME_WQ473-474-RULED-A.md`; DOCKET L781.
**Encoded:** 2026-10-29 by SHADE (PROME spawn prome-92). Prospective only; no retrospective regrade. The 30% red flag is unchanged.
**Status of this file:** the governing text for charter Key Ratios #2 and #4 (`CLAUDE.md` § Key Ratios carries the core and points here). **Ruled letter: transcribe, never improve.** A change to anything below is a Will-gated ratio-definition change.

**Transcription (byte-faithful):** §A = lines 9–89 of `research/L726_ILLIQUIDITY_BASIS_2026-10-21.md` (its §1–§5; §7 ruling request 1 asked adoption of §1–§5); §B = lines 26–62 of `research/L727_TSR_METHOD_2026-10-21.md` (its §2 through the proposed charter text). **Omitted on purpose:** L727 line 64 (the R + T "creator-shape sum" option) — **REJECTED by WQ-474 A**; it is not part of the letter. Source hashes at transcription: L726 `596929b331d6be2b8bd1a7dc2d757881745ef3a983d16923bd64b3d64b55126d`, L727 `c28618b8969b1a362715af459d5e30dab4ff532fce6f60165f9c25d8164adca5` (both committed at `07531f341`).
**Check (run, do not trust this banner):**
`diff <(sed -n 9,89p research/L726_ILLIQUIDITY_BASIS_2026-10-21.md) <(sed -n '/^<!-- A-BEGIN -->$/,/^<!-- A-END -->$/p' instruments/KEY_RATIOS_2_4_ADOPTED_LETTER.md | sed '1d;$d') && diff <(sed -n 26,62p research/L727_TSR_METHOD_2026-10-21.md) <(sed -n '/^<!-- B-BEGIN -->$/,/^<!-- B-END -->$/p' instruments/KEY_RATIOS_2_4_ADOPTED_LETTER.md | sed '1d;$d') && echo VERBATIM-OK` (run from `AGENTS/SHADE/`).

**Ruling facts that sit beside the letter (not edits to it):** (1) **L1 is ACCEPTED** (WQ-473 A, "adopt + L1"); the letter's own sentence "listed separately so Will can accept or strike it" records the question that ruling answered. (2) **The R + T sum is REJECTED** (WQ-474 A); SHADE-R v1 and SHADE-T v1 are never summed and never called TSR. (3) Words such as "proposed" inside the transcribed text are the proposal's own wording, kept verbatim; the ruling adopted them as written.

---

## §A — Key Ratio #2, Illiquidity Ratio (GA): L726 §1–§5, verbatim

<!-- A-BEGIN -->
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
<!-- A-END -->

---

## §B — Key Ratio #4, TSR UNAVAILABLE + SHADE-R v1 / SHADE-T v1: L727 §2, verbatim

<!-- B-BEGIN -->
## 2. Proposed replacement — two named, sourced diagnostics (never labelled TSR)

Both use **one insurer, one statement, one valuation date, GA only**, and the same denominator:

> **Surplus = Page 3 (Liabilities, Surplus and Other Funds), Line 38 "Totals of Lines 29, 30 and 37" (capital and surplus), Column 1.** Verified label at the DLIC FY2025 annual statement; it is the line the NAIC Note 1 template calls "state basis surplus (Page 3, Line 38)".

### SHADE-R v1 — higher-risk / affiliated asset concentration to surplus

Sourced shape: Gober's R-factor (2019 GCU example). Components mapped to the 2026 blank, each reported separately, summed without overlap:

| Component | Exact source (BACV, current year) | Mapping to the creator's example |
|---|---|---|
| R1 Structured | Schedule D-1-2 **line 1909999999** Total ABS (memo beside it: non-agency = total minus agency lines 1019999999–1049999999; affiliated ABS line 1899999999 — **inside R1, never added again**) | "All RMBS & other structured" |
| R2 Affiliated issuer credit obligations | Schedule D-1-1 **line 0499999999** Subtotal ICO (Affiliated) | Essay's affiliated "IOUs" |
| R3 Affiliated stock | Schedule D-2-1 **line 4409999999** (preferred, parent/subsidiaries/affiliates) + Schedule D-2-2 **line 5979999999** (common, parent/subsidiaries/affiliates) | "Affiliated common stock" |
| R4 Schedule BA | Schedule BA Part 1 **line 8099999** total (split shown: unaffiliated **7899999**, affiliated **7999999**) | "Sch BA – Other – non-affiliated" (SHADE includes affiliated BA too; the split keeps the creator's piece visible) |
| Not included | Hybrids / SVO-identified funds (no 2026 counterpart, §1 defect 2); affiliated mortgages on Schedule B (line not checked — UNKNOWN) | — |

**SHADE-R v1 = (R1 + R2 + R3 + R4) / Surplus.** Line numbers verified in the NAIC 2026 instructions (sources below).

### SHADE-T v1 — affiliated / captive ceded reinsurance to surplus

Sourced shape: Gober's T-factor ("reinsurance ceded to captives/affiliates compared with surplus") and the essay's emphasis on modified coinsurance as the less transparent form.

| Component | Exact source |
|---|---|
| T1 Coinsurance reserve credit to affiliates | Schedule S Part 3 Section 1, **Column 9 "Reserve Credit Taken Current Year"**, General Account affiliate subtotals: **0799999** (Authorized Affiliates) + **1899999** (Unauthorized Affiliates) + **2999999** (Certified Affiliates) + **4099999** (Reciprocal Jurisdiction Affiliates) |
| T2 Modco reserves with affiliates | Same rows, **Column 14 "Modified Coinsurance Reserve"** (NAIC: GA total ties to the parenthetical amounts on Page 3 Lines 1 and 3) |
| Memo (not summed) | Captive sub-lines (e.g. 0199999 U.S. captive, 0499999 non-U.S. captive under Authorized); Unauthorized Non-Affiliates 2199999; Schedule S Part 3 Section 2 (A&H) affiliate rows — Section 2 line numbering **not verified** here, check at first use |

**SHADE-T v1 = (T1 + T2) / Surplus.** **Relation to charter Key Ratio #1:** #1's numerator ("reserve credit from affiliates") is T1; SHADE-T adds T2 (modco). Both stay; #1 keeps its existing >100% critical marker.

### Charter treatment proposed

Replace Key Ratio #4 ("TSR Ratio (Gober's metric) = higher-risk off-balance-sheet assets / reported statutory surplus") with:

> **4. TSR — UNAVAILABLE** (creator's method proprietary and not reproducible from public sources; `research/L727_TSR_METHOD_2026-10-21.md`). **In its place SHADE reports two named diagnostics, SHADE-R v1 and SHADE-T v1, each with its components, never summed into one figure and never called TSR. No band or threshold until a calibration set across ≥5 insurers exists.**
<!-- B-END -->

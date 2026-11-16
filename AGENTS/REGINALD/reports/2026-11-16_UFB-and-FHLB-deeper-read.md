# REGINALD 2026-11-16 (second session): United Fidelity deeper read and FHLB advances under REVIEW

**Session:** reginald, Claude Code, Opus 5.5 (claude-opus-5-5), desktop. Woken by PROME prome-6f (session 364221f6) on Will's word in PROME's chat at 11:05 ET: "Lets look into these". Research only: it moves no gate, level, band, score, card or charter. Started 11:07 ET (`date`). **Git:** CORAL's dirty tracked files block a rebase pull, so there was **no pull**; I worked on the checkout as it stood (root rule). **Tools:** eCFR versioner API (curl), Office of Finance CDN, SEC XBRL frames API, `FORGE/tools/market-data/fetch.py`, one background Opus web reader (findings in §A2, labelled). Unavailable: pdf-viewer and Prisma MCP (connect timeout), mtnewswire (endpoint not found). None of them is needed here.

**Labels:** VERIFIED = read at the primary source this session. INFERRED = my reasoning from verified facts. UNKNOWN = not established. "Recalled" = statute text I did not open this session.

---

## A. United Fidelity Bank, fsb (Evansville IN; RSSD 391575; FDIC cert 29566)

### A1. Corrections to my morning report §3 (`reports/2026-11-16_L798-and-inbox/REPORT.md`)

I accept all five of the reader's findings. The morning report carries a dated annotation under §3 that points here; its table is left as written.

| # | Morning text | Correction | Basis |
|---|---|---|---|
| a | "the OCC changes the category under 6.3(c) or 6.4(e)" | **12 CFR 6.4(e) does not exist** in the current rule, which ends at (d); the rule's own 6.3(b)(3) still cites it, and that is where my cite came from. The reclassification paragraph is **6.4(d)**, with procedure in part 19 subpart M (6.5(a)(1) cites "§ 6.4 and subpart M of part 19"). **Both 6.4(d) and 6.3(c) work in one direction only, downward.** Neither can lift the bank out of undercapitalized | eCFR 6.3, 6.4, 6.5 at 2026-11-12 (reader); 6.5 re-read by me at 2026-11-12 |
| b | "unless the filing is amended" | **Withdrawn.** An amended Call Report is not one of the three notice events in 6.3(b). The way out is better ratios recognised at a **later notice event**: the next Call Report due date (12/31 report: 30 days lands on Sat 1/30/2027, so due **Mon 2/1/2027**, INFERRED from the FFIEC weekend roll), a final exam report, or written OCC notice | reader N2; FFIEC General Instructions per reader |
| c | "337.6(b)(2): only an adequately capitalized bank may get an FDIC waiver" | The waiver is **granted under 337.6(c)** ("upon application by an adequately capitalized insured depository institution"). (b)(2) is the prohibition the waiver relieves | eCFR 337.6(c), read by me at 2026-11-12 |
| d | "fails on one measure" (CET1 not listed) | List all four: total 7.26% (< 8.0, **fails**), Tier 1 6.64% (≥ 6.0), **CET1 4.74%** (≥ 4.5, margin 0.24 points, about **$13.2M**: DEWEY's $13.239M), leverage 5.82% (≥ 4.0). One more loss of about $13M would add a second failed measure; it would not make the bank "significantly" undercapitalized (CET1 < 3.0) | DEWEY 9/30 Call Report figures; 6.4(b)(3)-(4) |
| e | "undercapitalized since Fri 10/30" | **Conditional.** 10/30 is the operative date only if no final exam report or written OCC notice reached the bank after 10/30: 6.3(b) takes the *most recent* of the three dates. Any such document would not be public | 6.3(b) text (reader row 4) |
| f | (reader's B1, adopted) "no waiver exists" | True **today**. But the 2023 consent order (Art. IV(3)) barred "well capitalized" from October 2023, so the bank has needed a 337.6(c) waiver to accept or roll any brokered deposit since then. **Whether it had one decides whether 10/30 began a new bar or continued an old runoff.** §A2 below | consent order Art. IV(3) per PROME report B; 6.4(b)(1)(i)(E) |

One more correction of my own: the morning line "brokered deposits fell $147.0M in Q3" is right on RCON2365. But that line excludes any reciprocal deposits the bank treats as non-brokered, and §A2 shows those may belong in the brokered total. The Q3 brokered figure is therefore a lower bound on funding under the bar, not the whole of it.

### A2. Was there an FDIC waiver? What is public, and what the Call Report implies

**What the rule says (VERIFIED, eCFR 337.6 at 2026-11-12 and at 2024-06-30):**
- 337.6(c): the FDIC may waive "on a case-by-case basis and upon application by an adequately capitalized insured depository institution"; "Any waiver granted may be revoked at any time by written notice"; filing under 12 CFR 303.243.
- 337.6(e)(2)(i): a bank keeps reciprocal deposits outside "brokered" only if it is an agent institution. That needs (A) CAMELS 1, 2 or 3 **and** well capitalized; or (B) "Has obtained a waiver pursuant to paragraph (c)"; or (C) it does not receive reciprocal deposits that take its total above the average of the four quarter-ends preceding the quarter in which it "was found not to have a composite condition of outstanding or good or was determined to be not well capitalized".
- (e)(3)(ii): a bank that went over the cap requalifies on the date its reciprocal balance is back under it.
- **(e)(4) is new in 2026.** Under it, nonmaturity reciprocal deposits are "received" only when a NEW covered deposit is submitted. It is absent from the 2024-06-30 text; the history line lists 2026 amendments at 91 FR 33070 (6/3/2026) and 91 FR 56028 (9/1/2026). I did not establish which of the two added it.

**Public record of a waiver: see the web check below.** Short answer: **no public source shows a waiver or its absence.** The deciding document would be an FDIC decision on a 303.243 application, and the FDIC's handling of it is set out in the web reader's findings.

**What the Call Report implies (DEWEY's verified series; my rule reading; INFERRED):**

| Test | Reading | What it points to |
|---|---|---|
| Brokered reciprocal (RC-O item 9, RCONG803) | **0 in every quarter 12/2021 to 6/2026**; BLANK at 9/30/2026 | — |
| Reciprocal total (RCONJH83) against the special cap | Cap = 626.9 (trigger Q4 2023) or **727.85** (trigger Q1 2024: average of 3/23, 6/23, 9/23, 12/23). The balance was above **both** caps at **10 of 11** quarter-ends from 3/24 to 9/26; the exception is 12/25 at 692.4. An earlier trigger (a CAMELS 3 also starts the (C) clock) only lowers the cap | Above the cap and not reported as brokered: fits **(B), a waiver** |
| Brokered time deposits rolled in 2024 | DEWEY: at least about $370M of brokered money on the books at 12/31/2024 was neither long-dated at 12/31/2023 nor a sweep balance | Accepted or rolled after the order: fits **a waiver** |
| Brokered balance path | 2,481.6 (9/23) → **2,525.9 (12/23, peak)** → falls in **every one of 11 quarters** to 1,006.5 (9/26) | Fits a waiver that came with an amount or run-down condition, or the order's Art. VI plan. It does **not** discriminate on its own |

**Alternatives to a waiver, and their weight:**
1. **Misreporting.** The bank put above-cap reciprocal deposits in non-brokered and rolled brokered funds without a waiver, which would be a 337.6(b)(2) breach over about three years. That is possible: the order's Art. XII already forced refiled Call Reports (12/31/2025 refiled 4/27/2026).
2. **"Receive" read narrowly.** For 2026 quarters, (e)(4) lets growth inside existing nonmaturity reciprocal accounts fall outside "receive". For 2024 and 2025 the term was undefined, so this is arguable but not rule-backed. The Call Report does not split reciprocal by maturity, so the form cannot test it.
3. **A later trigger quarter.** Ruled out: the order's specific capital minimums remove "well capitalized" under 6.4(b)(1)(i)(E) from October 2023.

**My judgment (INFERRED, not VERIFIED):** a waiver is the **most probable** reading. Two independent tells point the same way and the alternatives are weaker. If there was one, **10/30 began a new bar**: a (c) waiver is open only to an adequately capitalized bank, so it stopped working on the deemed-notice date. The bar then reaches the **$1,006.5M brokered**. *Relabelled 11:2x ET 11/16 on DEWEY's pointer (`628e4191a7`, verified against its saved RC-E instructions, Dec 2025, p. RC-E-10): the $510.5M (RCONHK06) is brokered deposits of $250K or less maturing within a year **plus all brokered demand and savings balances**, so it is not a CD wall. About $147.5M of it is brokered sweep balances (DEWEY's estimate, INFERRED). That leaves **brokered CDs maturing within a year at most about $363.0M**. Existing sweep balances may stay but cannot grow (337.6(b)(4)). The earlier label "$510.5M maturing within a year" came from PROME report A and was carried here without that check.* and any reciprocal above the cap: **$739.1M at 9/30** against a cap of $626.9M or $727.85M. Under (e)(3)(ii) the bank can requalify by shrinking reciprocal under the cap rather than repaying all of it. **Funding exposed to the bar: about $1.0B certain, up to about $1.75B if all reciprocal is counted** (9/30 domestic deposits $5,046.0M). *This answers the reader's B1 question on the weight of evidence only; the waiver itself stays UNKNOWN until a primary document shows it.*

**Web check (public sources):**
A background Opus reader checked public sources 11:10 to 11:20 ET; its full ledger, with URLs and quotes, is at `reports/2026-11-16_UFB-public-sources_webcheck.md`.
- **FDIC: no waiver is published for any bank.** The waiver rule sets the process and the FDIC application database carries no waiver type (both VERIFIED); that waivers are never published is INFERRED.
  - The FDIC application-actions database (10,045 rows, 28 types, 10/2016 to 9/2026) has no brokered-waiver type; United Fidelity's only row is a 2019 merger.
  - "Decisions on Bank Applications" covers only deposit insurance, mutual-to-stock conversions and the merger report.
  - Under 12 CFR 303.243(a), a waiver is a letter application to the regional office. The decision goes only to the bank, with notice to the OCC. A waiver runs "for a fixed period, generally no longer than two years". The section has no public-notice provision.
  - The 303.8 public-file rule applies only to filings that need public notice. A FOIA request would meet Exemption 8 (309.5(b)(8)).
  - **That is why a waiver, or its absence, cannot be found in public records.** The bank's Call Report is the only public trace, and §A2 reads it.
- **The consent order text: brokered deposits appear in footnote 2 only** (allowed "except in compliance with" 1831f and 337.6). It has no waiver, no rate cap and no brokered limit. Art. IV(1) minimums: CET1 8%, leverage 9%, Tier 1 10%, total 12%. Art. VI(4) freezes the "funding strategy" without the ADC's prior non-objection (VERIFIED).
- **OCC: nothing after 10/30 is published.** EASearch shows two United Fidelity records: the active 2023-031 order and a 2010 OTS agreement, terminated in 2013. No PCA or capital directive has ever been published. The database still ends at actions dated 10/13. The November enforcement release is not out (NR 2026-99 of 11/12 is the Semiannual Risk Perspective) and is expected **Thu 11/19** (INFERRED) (VERIFIED as a search).
- **Parent filings:** EDGAR full-text search, 2023 to now, finds 0 hits on the order, brokered deposits or a capital plan (VERIFIED). FFED last filed 4/11/2023. FFIEC NIC returned HTTP 403, so it was **not reached**. **New to the desk:** the bank itself (CIK 1932454) filed a Form D on 1/12/2023 for a **$6.0M equity sale**. NexPoint Capital holds **1,000 shares of United Fidelity 7.00% preferred, cost $1.0M, marked at $500K (50%)** at 12/31/2025 and 6/30/2026 (10-Q, VERIFIED). These are INFERRED to be the bank-level 7% non-cumulative preferred.
- **Federal Register: 0 documents since 2023. Fed enforcement feed: no new action**; written agreement 24-014 is unterminated, feed to 11/9 (VERIFIED).
- **Not reached:** the FDIC orders site (TLS failure) and FFIEC NIC (CAPTCHA).
- **Note on the reader's own reading:** it calls the brokered decline consistent with no-waiver runoff and treats the question as moot going forward. I agree it is moot for the future: no waiver can exist below "adequately capitalized". I differ on the history because of the reciprocal-deposit evidence above, which the reader did not have.

### A3. The supervisory clock from here

Rule text VERIFIED at eCFR 2026-11-12 for 6.3, 6.5, 6.6, 337.6 and 337.7. Statute 12 USC 1831o and 1821 **recalled, not opened** (marked). Every date assumes the 10/30 deemed-notice date stands (A1-e).

| Date | What binds or happens | Cite | Type |
|---|---|---|---|
| since Oct 2023 / Jan 2024 | Not "well capitalized" (order sets capital levels). Brokered deposits need a (c) waiver. **Deposit rate cap applies:** an institution that is not well capitalized may not solicit at rates above the national rate cap (national rate + 75bp, or 120% of the similar-maturity Treasury yield + 75bp) | 6.4(b)(1)(i)(E); 337.6(b)(2), (c); **337.7(c)(2)** | rule-automatic (already in force; **10/30 adds nothing on rate caps**) |
| **Fri 10/30/2026** | Deemed notice: undercapitalized (total capital 7.26% < 8.0%) | 6.3(b)(1), 6.4(b)(3)(i) | rule-automatic (conditional, A1-e) |
| from 10/30 | **Brokered:** may not accept, renew or roll over any brokered deposit; no waiver route (c is for adequately capitalized only). Reciprocal above the special cap counts as brokered | 337.6(b)(3), (c), (e)(2)(i) | rule-automatic |
| from 10/30 | **Dividends and other capital distributions** barred if the bank would be undercapitalized afterwards, so barred now. That includes the **bank-level $45M non-cumulative preferred** (8% and 7%): missed dividends are lost, not accrued. **Management fees** to a controlling person barred on the same test | 6.6(a)(2)(i) → 1831o(d) (statute recalled) | rule-automatic |
| from 10/30 | **OCC monitoring** of condition | 6.6(a)(2)(ii) → 1831o(e)(1) | rule-automatic |
| from 10/30 | **Asset growth:** average total assets in a quarter may not exceed the prior quarter's average unless an accepted plan allows it (statute recalled). Q4 2026 average assets ≤ Q3 2026 average | 6.6(a)(2)(iv) → 1831o(e)(3) | rule-automatic |
| from 10/30 | **Prior approval** for acquisitions, branches and new lines of business | 6.6(a)(2)(v) → 1831o(e)(4) | rule-automatic |
| from 10/30 | **Discount window:** an undercapitalized bank may not have Federal Reserve discount window advances outstanding for more than 60 days in any 120-day period (OCC Problem Bank Supervision handbook, VERIFIED by reader; statute 12 USC 347b(b), recalled) | handbook; 347b(b) | rule-automatic (Fed lending limit) |
| **Mon 12/14/2026** | **Capital restoration plan due** (10/30 + 45 days) | 6.5(a)(1) | rule-automatic; **the OCC may set a different period in writing (OCC-discretionary, not public)** |
| at the plan | Plan accepted only with a **performance guarantee by each controlling company**. Three are named in the Fed's 2024 agreement: Fidelity Federal Bancorp, Pedcor Financial Bancorp and Pedcor Financial LLC. Liability is capped at the lesser of 5.0% of the bank's total assets when it became undercapitalized or the amount needed to restore capital. **5% of 9/30 total assets $5,915.5M = $295.8M** (a 9/30 proxy for the 10/30 figure) | 6.5(b), 6.5(i)(1) | rule-automatic condition |
| ≤ 60 days after filing (**~Fri 2/12/2027** if filed 12/14) | OCC written notice approving or disapproving the plan; the OCC may extend | 6.5(c) | OCC-discretionary (timing and outcome) |
| if no plan by 12/14, or plan disapproved, or plan not implemented | Bank becomes **subject to every provision for significantly undercapitalized banks**. Automatic: senior-executive pay restrictions. Discretionary menu by directive (statute recalled): recapitalization order (sale of shares or merger), limits on affiliate transactions, **deposit rates capped at the prevailing regional rate**, asset restrictions, management or board replacement, a ban on correspondent deposits, prior Fed approval of holding-company distributions, divestiture | 6.5(d), (e), (f); 6.6(a)(3) → 1831o(f)(4); 1831o(f)(2) via part 19 subpart N (6.6(b)) | automatic switch; actions mostly OCC-discretionary |
| same triggers | A **ground** for receivership or conservatorship exists when an undercapitalized bank fails to submit or implement an acceptable plan or has no reasonable prospect of becoming adequately capitalized | 12 USC 1821(c)(5)(K) (recalled, not opened) | OCC-discretionary (a ground, never automatic) |
| next notice event: **Mon 2/1/2027** (12/31 Call Report due) | Category re-set on 12/31 ratios: up if total capital ≥ 8.0%; down to significantly undercapitalized if total < 6.0%, Tier 1 < 4.0%, CET1 < 3.0% or leverage < 3.0% | 6.3(b)(1), 6.4(b) | rule-automatic |
| any time | Consent order Art. IV(8): the disposition-plan trigger appears met on the stated ratios, but it needs the ADC's written direction "in the sole discretion of the ADC". Fed agreement 24-014: holding-company interest on sub debt and preferred distributions need prior Fed approval | order Art. IV(8); Fed WA (PROME report B) | OCC- and Fed-discretionary |
| not in sight | Critically undercapitalized (tangible equity ≤ 2%) brings mandatory receivership within 90 days. Leverage is 5.82%: far off | 1831o(h)(3) (recalled) | rule-automatic if ever reached |

**OCC enforcement after 10/30:** see the web check in A2. PROME's 11/11 read found the OCC database ran only to actions dated 10/13. The November monthly release is due around the third Thursday, which is **Thu 11/19/2026** (INFERRED from the usual pattern).

### A4. Read-across

**My 14 names: no.** The mechanism here is a bank whose concentrated multifamily book moved to nonaccrual and pushed total capital under 8%. It was already barred from "well capitalized" by an order and depended on brokered and reciprocal funding: brokered $1.0B plus reciprocal $0.74B against $5.0B of domestic deposits, at 9/30. No name in my 14 is under a capital-level order or near the 8% total-capital line. The trigger is the brokered bar, and it binds only below "well capitalized". So the case is a template (order + thin capital + wholesale funding), not an exposure. What would change this: a name in my 14 losing well-capitalized status by order or by ratio. The live claim ("severity concentrated, not tier-wide") is unchanged.

**Holding company (Fidelity Federal Bancorp, "FFED") outside notes and preferred: yes, two mechanisms, both rule-based and INFERRED in effect:**
1. **No upstream cash.** From 10/30 the bank cannot pay dividends to FFED (1831o(d)). FFED's debt service on about **$113.75M** of sub notes (2028/2029/2031 issues and the Dec 2022 issue; floating coupons, e.g. the 2029 note at 8.40% on 8/31/2026) has to come from FFED's own cash or new money. The Fed agreement already requires prior Fed approval for that interest. FFED's own cash is UNKNOWN.
2. **The plan guarantee may rank ahead of the notes.** If FFED guarantees the capital plan (needed for acceptance, 6.5(b)), the guarantee is a liability of up to about $295.8M. In an FFED bankruptcy, commitments to a federal banking agency to maintain a bank's capital get **priority** under 11 USC 507(a)(9) (recalled, not opened). That would put them ahead of subordinated noteholders. **The guarantee is larger than the outside notes.**
3. **Holders with a listed wrapper:** FINS (Angel Oak Financial Strategies Income Term Trust) holds $3.0M face, 0.66% of net assets; BANX (ArrowMark Financial) holds the ex-TARP preferred at a 60% mark, 0.88% of net assets (PROME report D; fund filings 6/30 to 8/31/2026, before the Q3 loss). **Immaterial to either fund.** Thompson Bond Fund (unlisted) holds $13.5M face, 0.69%. **New:** NexPoint Capital (a business development company; whether it is listed was not checked) marks 1,000 shares of the **bank-level** 7% preferred at **50% of cost** ($500K) at 6/30/2026, before the Q3 loss. Under the 1831o(d) bar that preferred can pay no dividend from 10/30, and the dividend is non-cumulative.

---

## B. Federal Home Loan Bank advances, REG-T-06 at REVIEW

Source: Office of Finance Combined Financial Report (CFR) Q3 2026, `https://cdn.fhlb-of.com/files/2026/2026Q3CFR.pdf`, sha256 `58c6ab33…bbacf` (the same file as this morning), read 11:1x ET. Comparatives come from the Q2 2026 CFR (`2026Q2CFR.pdf`) and FY2025 CFR (`2025Q4CFR.pdf`), downloaded 11:1x ET. Text extracted with `pdftotext -layout`.

### B5. The two breadth measures (registry/NOTES.md §REG-T-06)

My NOTES do **not** fix endpoints: they say "Compare the two breadth measures over named, matching endpoints". The morning report referred the endpoint choice to PROME. **Both candidates are reported side by side**, with the 10/10 H1 read reproduced as a control.

**(1) Top-four growth contribution.** Basis: CFR Table 5 / Table 13, top 10 advance borrowers by **holding company**, **principal**. Aggregate principal: $677.077B (12/31/25), $813.3B (6/30/26, CFR Figure 2), $803.776B (9/30/26).

| Holding company | 12/31/25 $B | 6/30/26 $B | 9/30/26 $B | YTD change | Q3 change |
|---|---:|---:|---:|---:|---:|
| PNC | 13.000 | 40.400 | 36.500 | **+23.500** | −3.900 |
| Citigroup | not in top 10 (< 11.150) | 29.000 | 30.000 | **≥ +18.850** | +1.000 |
| Wells Fargo | 16.000 | 22.000 | 33.000 | **+17.000** | **+11.000** |
| Apollo (Athene) | 23.271 | 27.695 | 29.895 | **+6.624** | +2.200 |
| Truist | 31.501 | 27.700 | 28.850 | −2.651 | +1.150 |
| JPMorgan | 18.171 | 17.550 | 15.100 | −3.071 | −2.450 |
| Bank of America | 12.053 | 14.996 | 14.991 | +2.938 | −0.005 |
| MetLife | 14.215 | 14.215 | 14.215 | 0 | 0 |
| Midland Financial | 12.620 | 13.050 | 13.250 | +0.630 | +0.200 |
| Bank of Montreal | not in top 10 (< 11.150) | not in top 10 (< 13.050) | 12.250 | ≥ +1.100 | n/a |
| U.S. Bancorp | 15.050 | 27.539 | not in top 10 (< 12.250) | ≤ −2.800 | **≤ −15.289** |
| NYCB / Flagstar | 11.150 | not in top 10 | not in top 10 | UNKNOWN | n/a |

| Endpoints | Aggregate change (principal) | Top four identified (PNC, Citi, Wells, Apollo) | Ratio | Coverage |
|---|---:|---:|---:|---|
| **YTD 12/31/25 → 9/30/26** | **+$126.699B** | **≥ $65.974B** (Citi a lower bound) | **≥ 52.1%** | INCOMPLETE: identified contributors, not a verified system-wide top four. A borrower outside both top-10 lists could have grown by up to about $12.25B, more than Apollo's +$6.6B. BMO's change is bounded at +$1.1B to +$12.25B |
| **Q3 6/30 → 9/30/26** | **−$9.5B** principal (carrying −$12.287B) | Signed: Wells +11.0, Apollo +2.2, Truist +1.15, Citi +1.0; PNC −3.9, JPM −2.45, **USB ≤ −15.3** | **NOT-APPLICABLE** (aggregate negative; rule: no division) | Same top-10 limit |
| *Control: H1 12/31 → 6/30/26 (10/10 frame)* | +$136.2B | PNC +27.4, Citi ≥ +17.85, USB +12.5, Wells +6.0 | ≥ 46.8% | as above |

**(2) Borrower-side median, matched SEC-filer panel.** Same instrument as 10/10: SEC XBRL frames `us-gaap:AdvancesFromFederalHomeLoanBanks`, instants CY2025Q4I, CY2026Q2I and CY2026Q3I, pulled 11:1x ET 11/16. Filers report at the filer level; the panel is not the membership. Flat = within ±0.5%. Zero-start filers are reported separately.

| Endpoints | Matched filers | Zero-start (excluded from %) | n | **Median % change** | Up / down / flat | Panel sum | Excluding the top three gainers |
|---|---:|---:|---:|---:|---|---|---|
| *Control: H1 (10/10 reproduction)* | 109 | 8 | 101 | **0.0%** | 36 / 49 / 16 | $100.1B → $135.5B (+$35.5B; PNC +$27.4B) | +$2.18B across 106 (10/10 had +$2.3B: **reproduces**) |
| **YTD 12/31/25 → 9/30/26** | 102 | 8 | 94 | **−0.4%** | 35 / 47 / 12 | $93.3B → $124.2B (+$30.9B; PNC +$23.5B, Athene +$6.6B) | **−$0.25B across 99** |
| **Q3 6/30 → 9/30/26** | 100 | 11 | 89 | **0.0%** | 29 / 35 / 25 | $126.2B → $123.8B (−$2.4B; PNC −$3.9B) | −$6.66B across 97 |

⚠️ Perimeter: Citi, Wells, USB, BofA, Truist, WAL, CFG, MTB, HBAN, VLY, ZION and EGBN do not tag this concept, and thousands of non-SEC members are invisible. 13 filers in the Q2 frame are missing from the Q3 frame. Some have September fiscal years (Raymond James, TFS) and some may simply not have filed yet: non-accelerated Q3 10-Qs were due 11/16 (45 days). **The Q3 panel may still be filling**, so it is not final.

**Reading (owner judgment):** on both endpoint choices, borrowing growth is **concentrated, not broad**. Year to date, four large borrowers explain at least 52% of system growth. On the SEC panel the median borrower is flat to slightly down, and outside the top three movers the panel shrank. **No breadth-supported escalation.**

### B6. Where the borrowing sits: advances by district (CFR condensed combining schedules, **carrying value, $B**)

| District | 12/31/25 | 6/30/26 | 9/30/26 | Q3 change | Q3 % | YTD change | Share of YTD growth |
|---|---:|---:|---:|---:|---:|---:|---:|
| **Cincinnati** | 70.1 | 93.7 | 71.6 | **−22.1** | **−23.5%** | +1.5 | 1.2% |
| New York | 92.3 | 127.3 | 119.7 | −7.6 | −6.0% | +27.4 | 22.5% |
| Boston | 38.8 | 45.0 | 38.9 | −6.1 | −13.5% | +0.1 | 0.1% |
| San Francisco | 38.2 | 34.0 | 30.8 | −3.2 | −9.5% | −7.4 | −6.1% |
| Indianapolis | 39.6 | 41.7 | 38.6 | −3.1 | −7.5% | −1.0 | −0.8% |
| Chicago | 61.1 | 71.1 | 72.4 | +1.4 | +1.9% | +11.3 | 9.3% |
| Topeka | 43.7 | 47.0 | 48.6 | +1.6 | +3.5% | +4.9 | 4.0% |
| Dallas | 50.8 | 47.4 | 49.5 | +2.1 | +4.4% | −1.3 | −1.1% |
| Atlanta | 95.0 | 101.4 | 105.2 | +3.8 | +3.8% | +10.2 | 8.4% |
| **Pittsburgh** | 36.8 | 77.7 | 87.0 | +9.3 | +12.0% | **+50.2** | **41.2%** |
| **Des Moines** | 110.2 | 124.5 | 136.1 | +11.6 | +9.3% | +25.9 | 21.2% |
| **System** | 676.7 | 810.7 | 798.4 | **−12.3 (−1.5%)** | | **+121.7** | 100% |

**The Q2 → Q3 fall is one district.** Cincinnati fell $22.1B. Excluding it, the other ten together rose **+$9.8B** (six up, four down). U.S. Bancorp (Cincinnati and San Francisco) fell by at least $15.3B at the holding company and JPMorgan by $2.45B. So the decline is **large banks paying down**, not broad retreat (INFERRED from Table 5 bounds plus the district table). Year to date, growth sits in **Pittsburgh (PNC), New York (Citi), and Des Moines (Wells Fargo and Athene)**: 85% of system growth in three districts. Top-five borrower concentration at 9/30 by district (CFR supplemental S-3/S-4): Pittsburgh **81%**, New York 58%, Cincinnati 59%, Atlanta 57%, Des Moines 56%, Topeka 55%, San Francisco 45%, Chicago 46%, Indianapolis 44%, Boston 36%, Dallas 36%.

**For BOND (VX-BND-18), VERIFIED at the Q3 CFR:** "The collateralization ratio for all borrowers was **3.6** at September 30, 2026", and **2.9** for the 124 borrowers holding at least $1.0B each. Advances were $798.428B carrying ($803.776B principal). Against BOND's red leg (ratio ≤ 3.0 or > $900B): **not met** on the all-borrower ratio (3.6, down from 3.7 at 6/30 per BOND's row) and not met on level. Routed through WALTER (packet listed in §D).

### B7. In plain words

**What three quarters above $700B tells you:** the Home Loan Banks lent a record $800B-plus for three quarters running. They lend to banks, insurers and credit unions against mortgages and securities, at prices usually cheaper than other wholesale money. **What it does not tell you:** whether anyone is in trouble. This year's growth came mostly from a handful of very large, healthy borrowers: PNC, Citigroup, Wells Fargo and Apollo's insurer Athene. Big banks use the Home Loan Banks as ordinary, cheap funding when deposits are dear or when they are building liquidity. The typical smaller borrower that files with the SEC did not borrow more this year: the median change is about zero. In the third quarter the total fell 1.5%, and almost all of that was one district, Cincinnati, where U.S. Bancorp paid down at least $15B. **Stress borrowing looks different:** many small and mid-size banks drawing at once, collateral cover falling, and growth among banks already in trouble. United Fidelity carries no Home Loan Bank advances due within a year (PROME report A), so it is not that pattern. **What would move REVIEW to escalation under my registered rule:** there is no automatic step. I would have to make an explicit, evidence-based judgment on recorded breadth. In practice that means the median borrower on the matched panel clearly rising, with growth no longer dominated by four names, ideally confirmed by the collateral ratio falling toward BOND's 3.0 line or by weak banks among the growers. None of that is present at 9/30. The level rule's own exit is **≤ $650B on two consecutive quarters**, about $148B below today.

---

## C. For TERRY

**No candidate (reasoned).** Live vendor quotes, intraday and **not settles**, `fetch.py` 11:13 ET 11/16: KRE $72.36, USB $60.86, FINS $11.66, BANX $19.40, WAL $73.69.
- **United Fidelity:** no listed equity or bond. FFED's notes are private placements. The listed holders FINS and BANX hold under 1% of net assets each, so no instrument moves on this.
- **FHLB:** the Q3 fall is U.S. Bancorp and JPMorgan paying down, which is a funding choice, not stress. The growth year to date sits with large, strong borrowers. Nothing here maps to bank credit stress or to a listed instrument with an edge. **NOT-FIRED** on any letter, and none is proposed.

## D. Routed and not reached

- **Routed:** WALTER packet `AGENTS/WALTER/inbox/2026-11-16_from-REGINALD_FHLB-Q3-collateral-ratio-for-BOND.md` (BOND's 9/30 ratio and advances). DEWEY was answered by message on the reciprocal-waiver reading (§A2), which DEWEY cites as an open rule question.
- **Not reached:** FHLB district 10-Q five-largest-borrower tables (these would narrow the "top four" ranking); 12 USC 1831o, 1821(c)(5) and 11 USC 507(a)(9) not opened (recalled; marked); which 2026 amendment added 337.6(e)(4); FFED's own cash; the Q3 SEC panel will be complete after the 11/16 filing deadline (re-run then). No STATUS, threshold, score or prediction edited this session (research only).

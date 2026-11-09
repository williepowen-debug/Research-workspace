# PRED-38 sweep, part 2: Q3-2026 10-Qs filed since 10/31

Compiled 2026-11-09 (shell `date` at the last read: 12:23 EST) by a read-only NEXUS helper. It does not grade the letter or edit anything in the repo. It continues `AGENTS/NEXUS/research/2026-10-31_owed/PRED38_SWEEP.md`, which found k = 0 across 27 banks, and does not redo that work.

**Criterion, unchanged:** a bank counts if its own Q3-2026 primary document attributes at least $100.0M of Q3 **net charge-offs**, in its own words, to non-depository financial borrowers.

## Sources and access

| Source | Status |
|---|---|
| `efts.sec.gov` full-text search | Worked |
| `data.sec.gov` XBRL companyfacts and submissions | Worked |
| `www.sec.gov` via curl | Still HTTP 403 to the descriptive User-Agent |
| `www.sec.gov` via the WebFetch tool | Reached XBRL **R-pages** (rendered note tables) and `FilingSummary.xml` |

Two limits on the WebFetch route:

- The full 10-Q HTML is unreadable that way: JPM is over 10 MB, and FCNCA's conversion truncated at cover, glossary and face statements.
- R-page figures come through WebFetch's summarizing model. They are labelled **[R-page via WebFetch]**, are not byte-verified, and each one was cross-checked against a non-dimensional XBRL total where one exists.

Issuer-hosted 10-Q PDFs were fully text-searched (`pdftotext`) for GS, MS, C, PNC and USB. Their md5 hashes are in the raw-file note at the end.

**FTS NBFI-term screen.** Sixteen terms were run over 10-Qs filed 11/01–11/09: nondepository, non-depository, NDFI, nonbank, non-bank, NBFI, private credit, business development company/companies, fund finance, nonbank financial, non-bank financial, subscription finance, capital call, asset-based finance and specialty finance. Every listed accession is confirmed indexed.

| Result | Banks |
|---|---|
| Zero hits | USB, FITB, RF, SCHW |
| Hits | JPM (non-bank) · C (non-bank, private credit, non-bank financial) · GS (private credit) · MS (non-bank) · PNC (non-bank) · COF (private credit) · KEY (nonbank, nonbank financial) · ZION (5 terms) · MTB (nondepository, NDFI, BDCs, specialty finance) · EWBC (non-depository, NDFI, fund finance, capital call) · FHN (specialty finance) · ALLY (non-depository, private credit) · FCNCA (6 terms) · FLG (specialty finance) · BPOP (non-depository) |

## 1. Table

Amounts are $M for Q3-2026, i.e. the three months to 9/30/26.

| Bank | Document read (accession, source) | Q3 NBFI-attributed NCO, bank's words | Qualifies |
|---|---|---|---|
| **GS** | 10-Q 0000886982-26-000532, filed 11/02. Full text from goldmansachs.com `investor-relations/financials/10q/2026/third-quarter-2026-10-q.pdf` | **None attributed.** Q3 wholesale charge-offs (154), recoveries 0, net (154) (Note 9 rollforward, p.50). "Charge-offs for the three months ended September 2026 for wholesale loans (principally related to term loans originated in 2024 and 2020) were substantially all related to other collateralized and corporate loans." Q3 provision $368M "primarily reflected impairments related to wholesale loans" (MD&A) | **N.** The $368M provision became only $154M of NCO. That NCO is attributed to a collateral class ("other collateralized") and to "corporate", not to NBFI borrowers, and the split between the two is not given. See §4 |
| **JPM** | 10-Q 0001628280-26-069523, filed 11/03. XBRL R127 and R120 [R-page via WebFetch], plus Q2 10-Q 0001628280-26-054343 R119. The full 10-Q HTML (over 10 MB) and the IR PDF (gcs-web, HTTP 403) were **unreadable** | **None found.** 9M wholesale NCO 561 (gross 688, recoveries 127; R127). Wholesale gross charge-offs, 9M less 6M (derived): secured by real estate 95−49 = **46**; C&I 465−252 = **213**; "Other" 128−117 = **11**. "Other" is the class holding "Financial institutions" ($270.7B of loans), "Individuals and individual entities" and "SPEs" (R120). No sub-class charge-off row exists | **N.** Q3 gross charge-offs in the class that holds financial-institution loans are about $11M. C&I is generic. Caveat: the MD&A wholesale industry table (NCO by industry, year to date) was **not read** |
| **PNC** | 10-Q 0001628280-26-069377, filed 11/03. Full text from investor.pnc.com `sec-filings/all-sec-filings/content/<acc>/<acc>.pdf` | **None attributed.** Q3 commercial charge-offs (164), recoveries 36, net (128); total 257 (Table 58). 9M C&I NCO 300 (Table 24). "The increase in the comparison reflected an increase in commercial and industrial net charge-offs as well as $45 million of net charge-offs from the FirstBank acquisition…". C&I loans to "Financial services" total $49.1B (Table 16, balances only). "non-bank" hits are parent and subsidiary liquidity text | **N.** Commercial NCO of $128M is unattributed |
| **C** | 10-Q 0000831001-26-000056, filed 11/05. Full text from citigroup.com `rcs/citigpa/storage/public/citi-3q26-10-q.pdf` | **None.** "Net corporate credit losses on loans **$58**" for 3Q26; total NCL 2,217 (credit table, p.59). The only NBFI hit is risk-factor text: "any systemic risk concerns related to non-bank financial institutions, including private credit" | **N.** Corporate NCL total is under $100M |
| **MS** | 10-Q 0000895421-26-000293, filed 11/05. Full text from morganstanley.com `…/shareholder/10q0926.pdf` | **None.** Q3 gross charge-offs (106), net (106). Q3 net charge-off ratios: Corporate 0.66% on $9,338M average loans (about $62M; the ratios reconcile to the 106 total only if not annualized); CRE 0.58% (about $43M); Secured Lending Facilities **—%**. "Charge-offs in the current year period were primarily driven by corporate loans, including certain loans that were transferred to held for sale and subsequently sold, and commercial real estate loans." "non-bank" hits are liquidity-entity text | **N** |
| **USB** | 10-Q 0000036104-26-000058, filed 11/05. Full text from s203.q4cdn.com `…/2026/q3/USB-3Q26-10-Q.pdf` | **None.** Q3 NCO 523; Commercial 83, Lease financing 5, total commercial 88; CRE 42 (Table 7). "partially offset by higher commercial loan net charge-offs". Zero FTS NBFI hits, so no NDFI wording appears in the 10-Q | **N.** Commercial NCO is under $100M |
| **COF** | 10-Q 0000927628-26-000152, filed 11/03. R55 [R-page via WebFetch] | Commercial Banking charge-offs (21), recoveries 21, **NCO 0**. Total NCO 3,121, of which Card 2,745 and Consumer Banking 376 | **N** |
| **FITB** | 10-Q 0000035527-26-000243, filed 11/03. R64 [R-page via WebFetch]; XBRL total 139 matches | C&I NCO **75**; commercial mortgage (6); total 139. Zero FTS NBFI hits | **N** |
| **MTB** | 10-Q 0000036270-26-000060, filed 11/05. R55 [R-page via WebFetch]; XBRL total 127 matches | C&I NCO **66**; CRE 0; consumer 62; total 127. The NDFI and BDC wording was not read in context | **N.** C&I is under $100M |
| **FCNCA** | 10-Q 0000798941-26-000044, filed 11/06. R70 and R64 [R-page via WebFetch]; XBRL gross 135 and recoveries 32 match | Commercial gross (127), recoveries 29, so **commercial NCO 98** (derived). 9M gross: "Capital call lines" **0**; "Investor dependent" 50; C&I 242. "NDFI" appears in the glossary; the MD&A text was **not read** (truncated) | **N.** Commercial NCO of $98M is under $100.0M even if all of it were NBFI. NBFI attribution is not established, so it is not a near-miss |
| **KEY** | 10-Q 0000091576-26-000023, filed 11/03. XBRL only | Total gross write-offs 121, recoveries 32, so NCO **89** | **N** (total under $100M) |
| **ALLY** | 10-Q 0000040729-26-000023, filed 11/02. R66 [R-page via WebFetch]; XBRL total 423 matches | Commercial charge-offs 0, recoveries 3, so commercial NCO **(3)**, a net recovery. Consumer automotive 427 | **N** |
| **RF** | 10-Q 0001281761-26-000073, filed 11/09. XBRL | NCO **72** (write-offs 98, recoveries 26) | **N** (total under $100M) |
| **ZION** | 10-Q 0000109380-26-000127, filed 11/05. XBRL | NCO **3** | **N** |
| **EWBC** | 10-Q 0001069157-26-000051, filed 11/06. XBRL | NCO **21.6** | **N** |
| **FHN** | 10-Q 0000036966-26-000199, filed 11/05. XBRL | Gross write-offs **45**, recoveries 9 | **N** |
| **SCHW** | 10-Q 0000316709-26-000038, filed 11/06. XBRL | Gross write-offs **0**, recoveries 4 | **N** |
| **FLG** | 10-Q 0000910073-26-000084, filed 11/06. XBRL | Gross write-offs **84**, recoveries 10 | **N** |
| **BPOP** | 10-Q 0000763901-26-000025, filed 11/09. XBRL | Gross write-offs **99.6**, recoveries 26.7, so NCO about 72.9 | **N** |

For the six "XBRL" rows, the total is from non-dimensional companyfacts for 2026-07-01 to 2026-09-30, accession matched. No text was read for those banks. Their totals are below $100.0M, so they are mechanically excluded.

**Off-list FTS hitters.** These banks hit an NBFI term in 10-Qs filed 10/31–11/09: AUB, BANC, BANR, BOKF, BKU, CUBI, FFBC, HOMB, UCB, SBCF, TRMK, MBIN, AMTB, SFBS, UVSP, HBT, FSBC, MVBF, CHCO. All have Q3 gross write-offs of **$19.2M or less** (XBRL), so all are mechanically N. FNB hit "NDFI" but has no non-dimensional XBRL write-off fact, so it is **UNVERIFIED**. It is not read, and it is a mid-size bank with historical NCO well under $100M.

## 2. Running k

**k = 0.** It stays 0 after the 19 10-Qs listed in the brief plus the off-list FTS hitters. No Q3-2026 bank document read in either sweep attributes any net charge-off, at any size, to an NBFI, NDFI, BDC, fund-finance or private-credit borrower in the bank's own words.

## 3. Near-misses and coverage gaps

**Near-misses of $50–99.9M that are NBFI-attributed: none.** The closest items are listed below. None is NBFI-attributed in words.

| Bank | Item | Why it is not a near-miss |
|---|---|---|
| GS | $154M wholesale NCO, "substantially all related to other collateralized and corporate loans" | See §4 |
| FCNCA | Commercial NCO of $98M (derived) | Not attributed. "Capital call lines" gross charge-offs are 0 for 9M |
| PNC | Commercial NCO of $128M | Unattributed C&I |
| JPM | Q3 wholesale C&I gross charge-offs of about $213M (derived) | Generic C&I. The class holding financial-institution loans had about $11M |

**Coverage gaps:**

- **WBS:** no Q3 10-Q, and none will come. Webster Financial filed **15-12G** deregistrations on 2026-08-31 (two) and 2026-09-30 (EDGAR submissions, fetched 11/09).
- **SNV:** no Q3 10-Q, and none will come. Synovus filed 15-12G and 15-15D on 2026-01-12, apparently after its merger with Pinnacle. Neither bank is a pending filer.
- **JPM:** the MD&A was not read, including the wholesale industry exposure table with its NCO column (9M basis). The gcs-web IR PDF returned 403 and the EDGAR HTML is over 10 MB for WebFetch. The R-page class arithmetic caps the financial-institution-class Q3 gross charge-offs at about $11M. NBFI loans booked in C&I would not be visible that way.
- **FCNCA, MTB, KEY, ALLY, COF, FITB:** the narrative MD&A was not read. They are covered by class-level XBRL only, and in each case the relevant commercial or C&I NCO is under $100M.
- **RF, ZION, EWBC, FHN, SCHW, FLG, BPOP:** totals only, from XBRL.
- **FNB:** UNVERIFIED (above).
- **R-page figures:** they came through WebFetch's summarizer. They are consistent with every available XBRL total, but they are not byte-verified.

## 4. 10-Q quote closest to qualifying

GS 10-Q, Note 9, "Allowance for Credit Losses Commentary", p.51:

> "Charge-offs for the three months ended September 2026 for wholesale loans (principally related to term loans originated in 2024 and 2020) were substantially all related to other collateralized and corporate loans."

GS's own definition of that class (Note 9, p.44):

> "Other collateralized loans includes loans that are backed by specific collateral … Such loans include loans to investment funds (managed by third parties) that are collateralized by capital commitments of the funds' investors or assets held by the fund. Other collateralized loans also includes loans extended to clients who warehouse assets (that are directly or indirectly secured by corporate loans, consumer loans and other assets)…"

**Why it falls short:**

1. The total is $154M, split between "other collateralized" and "corporate" with no figure for either part.
2. "Other collateralized" is a collateral class, not a borrower attribution. It also includes "other secured loans extended to the firm's wealth management and corporate clients".
3. The bank does not say any charge-off was on a fund, BDC or NBFI borrower.

Under the letter's "in the bank's own words" test this does not count. If someone argued the other-collateralized share was fund finance or warehouse lending, the figure would still be unknown and below $154M.

## Raw files

Files are in `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-NEXUS/2419a9ba-4fad-414b-9ac7-40f2c51f4c49/scratchpad/docs/`: GS, MS, C, PNC and USB `.pdf` and `.txt`.

| File | md5 |
|---|---|
| GS.pdf | 93509b3b… |
| MS.pdf | 553a5df2… |
| C.pdf | f4f3fe5d… |
| PNC.pdf | b32bfb45… |
| USB.pdf | 0984caf2… |

XBRL companyfacts JSON is in `…/scratchpad/dl/`.

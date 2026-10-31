# PRED-38 sweep: Q3-2026 bank net charge-offs attributed to non-depository financial borrowers

Running count at 2026-10-31 12:22 EDT, compiled by a NEXUS read-only helper. The letter is not graded or changed here. It resolves 11/10: k≥2 HIT, k=1 NO-VERDICT, k=0 MISS. A bank counts only if its own primary document (release, 8-K or 10-Q) attributes **≥ $100.0M of Q3 net charge-offs** to non-depository financial (NBFI) borrowers.

**Access caveat.** `www.sec.gov` returned HTTP 403 ("Undeclared Automated Tool") to the mandated User-Agent. `data.sec.gov` and `efts.sec.gov` both worked with it. So:

- accession numbers come from EDGAR submissions JSON;
- totals come from XBRL `companyfacts` where available;
- the phrase screen is EDGAR full-text search (FTS);
- **all document text was read from issuer-hosted copies** (IR-site PDFs of the same filing, or the bank's own press release on a wire site).

The source is labelled per row. No sec.gov HTML was read.

## 1. Banks examined

| Bank | Document(s) read, filing accession and date | Q3 NBFI-attributed NCO, bank's words | Qualifies |
|---|---|---|---|
| JPM | 8-K 0001628280-26-065582 (10/13). Read the supplement (IR PDF `c89c7479…pdf`) and the presentation (IR PDF `2b5b9a7e…pdf`) | None. CIB NCO **$211M**; firm NCO $2,204M, of which CCB $1,976M. The only "non-bank" hit is "not transferable to non-bank affiliates" (liquidity footnote) | NO: unattributed C&I. Ex-99.1 narrative not read |
| BAC | 10-Q 0000070858-26-000548 (10/30) via investor.bankofamerica.com `content/<acc>/<acc>.pdf` | None. "Commercial net charge-offs decreased $37 million to $352 million … primarily due to lower charge-offs in the U.S. Commercial portfolio" (MD&A, Commercial Portfolio Credit Risk). "nonbank" and "private credit" hits are subsidiary and risk-factor text | NO |
| C | 8-K 0001104659-26-115323 (10/13). Read the QFDS (citigroup.com `2026fsqtr3rslt.pdf`) | None. FTS found 0 hits for any NBFI term in October 8-K filings | NO (no attribution) |
| WFC | 10-Q 0000072971-26-000327 (10/28) via wellsfargomedia.com `third-quarter-10q.pdf` | None. C&I NCO **$162M**; "driven by higher losses in our commercial and industrial portfolio". "Financials except banks" table gives nonaccruals only | NO |
| TFC | 10-Q 0000092230-26-000129 (10/28) via ir.truist.com `TFC+3Q26+Form+10-Q.pdf` | None. Q3 C&I charge-offs (125), recoveries 19, so **C&I NCO $106M** (Table 15). The $251M RAC NCO is Truist's own indirect-auto book. "nonbank financial institutions" appears only as a description of the Finance and insurance industry category | NO: generic C&I. See §3 |
| HBAN | 10-Q 0000049196-26-000090 (10/27) via huntington-ir.com mirror | None. NCO $146M; C&I **$71M** (Table 16); "higher net charge-offs in both the commercial and consumer loan portfolios" | NO (C&I < $100M) |
| CFG | 10-Q 0000759944-26-000213 (10/28) via investor.citizensbank.com `citizens-10-q-q3-2026.pdf` | None. C&I NCO **$41M**; total commercial $73M (Table 14). "Secured private credit finance" is only an industry line in Table 9 | NO |
| USB | 8-K 0000036104-26-000054 (10/15). Read the deck (q4cdn `3Q26EarningsPresentation.pdf`) | None. NCO **$523M** in total. NDFI slide: "Criticized rate is <1% of total NDFI portfolio"; BDCs about 1.9% of NDFI. No NDFI charge-off disclosed | NO |
| FITB | 8-K 0000035527-26-000229 (10/19). Read the release (q4cdn `Q3-2026-Earnings-Release-Final.pdf`) | None. NCO **$139M**; C&I $75M. "Excludes net charge-offs of $100 million which were taken at the time of acquisition" (Comerica purchase accounting; not NBFI-attributed) | NO |
| RF | 8-K 0001281761-26-000063 (10/16). Read the release (q4cdn `3Q26-Press-Release_Website.pdf`) | None. "Net charge-offs were $72 million" in total | NO (total < $100M) |
| KEY | 8-K 0000091576-26-000020 (10/20). Read the deck (q4cdn `3Q26-Earnings-Presentation-vF.pdf`) | None. NCO chart: 3Q26 **$89M** in total | NO (total < $100M) |
| ZION | 8-K 0000109380-26-000125 (10/19). Read the release (wire copy, placera.se) | None. "net loan charge-offs were $3 million" | NO (total < $100M) |
| PNC | 8-K 0001628280-26-065936 (10/15). Read the release (PR Newswire copy, finviz) | None. NCO $257M, of which $35M is the student-loan transfer; the remainder rose "due to higher commercial loan net charge-offs" (unattributed) | NO on the release. 10-Q pending |
| GS | 8-K 0000886982-26-000529 (10/13). Read the release (goldmansachs.com `2026-q3-results.pdf`) | Not disclosed. Provision **$368M**, "primarily reflected impairments related to wholesale loans". A provision, not an NCO; no NBFI attribution | NO. 10-Q pending; see §3 |
| MS | 8-K 0000895421-26-000288 (10/14). Read the supplement (morganstanley.com `finsup3q2026.pdf`) | None. Only "securities based lending on non-bank entities" (a balance) | NO |
| WAL | 10-Q 0001628280-26-068599 (10/30), XBRL only | Gross Q3 write-offs **$48.0M** (XBRL) | NO (total < $100M). BROCK: NCO $45.8M |
| EWBC | 8-K 0001069157-26-000048 (10/20). Read the deck (q4cdn) | None. "Net charge-offs at $22mm" | NO |
| WTFC | 8-K 0001015328-26-000026 (10/19). Read the release (finviz copy) | None. "Net charge-offs totaled $21.0 million" | NO |
| HAFC | 8-K 0001171843-26-006857 (10/27). Read the release (finviz copy). FTS hit "loans to nondepository" + "charged off" | None. Net loan charge-offs **$4.3M**; the $3.2M charge-off was CRE | NO |
| NTRS, ONB, SSB, UMBF | 10-Qs 0000073124-26-000066, 0000707179-26-000067, 0001193125-26-439976, 0001193125-26-437096, XBRL only | Gross Q3 write-offs $11.6M, $48.3M, $17.7M and $16.1M respectively | NO (totals < $100M) |
| SYF, AXP | 10-Qs 0001601712-26-000043, 0000004962-26-000409 | Consumer and card lenders (SYF gross write-offs $1,652M, XBRL) | NO (excluded class) |
| MTB, COF | 8-Ks 0000036270-26-000057 and 0000927628-26-000142. **Not read this session.** FTS found 0 hits for all 10 NBFI terms | Not read | INSUFFICIENT. No NBFI wording in their Q3 filings. MTB release and deck read by BROCK 10/16 |

FTS NBFI-term screen over priority-bank October 8-K and 10-Q filings, with 10 terms (nondepository · non-depository · NDFI · nonbank · non-bank · NBFI · subprime auto · private credit · business development compan · fund finance):

- **Zero hits:** C, GS, PNC, COF, KEY, MTB.
- **Hits, each read above:** JPM, BAC, WFC, MS, USB, TFC, FITB, HBAN, RF, ZION, CFG.
- **Error:** one FTS call returned HTTP 500 (BAC "nondepository"). It is covered by the direct 10-Q read.

Fleet records (REGINALD, BROCK, GIBBS, OTTO, CARL) contain no Q3-2026 bank NBFI charge-off.

## 2. Running k and coverage gap

**k = 0.** No bank examined discloses a Q3-2026 NCO that it attributes to a non-depository financial borrower, at any size. Across the banks read, the largest NBFI-labelled disclosures are balance and criticized-loan statistics (USB, FITB, RF, ZION), never charge-offs.

**Q3 10-Q not yet filed** (EDGAR submissions, fetched 10/31):

- JPM, C, GS, MS, USB, PNC, COF, FITB, KEY, RF, ZION, MTB;
- EWBC, FHN, ALLY, FCNCA, WTFC, PNFP, BOKF, BPOP, COLB, VLY, FLG, FNB, BKU, SCHW, SHUSA.

Other gaps:

- No October Item 2.02 8-K was found for WBS, SNV or CMA. CMA appears to be inside FITB, which references the Comerica conversion. SNV and WBS are unresolved.
- OZK files with the FDIC, not the SEC, and is outside EDGAR.

**Filed:** BAC, WFC, TFC, HBAN, CFG, BK, STT, NTRS, CFR, UMBF, ONB, ASB, SSB, WAL, SYF, AXP.

The 10-Qs can add class-level detail before 11/10. GS, JPM and PNC matter most.

## 3. Near-misses (none counts under the letter)

| Bank | Item | Why it does not count |
|---|---|---|
| TFC | Q3 C&I NCO **$106M** (charge-offs 125 − recoveries 19, 10-Q Table 15) | Generic C&I. No NBFI attribution in the bank's words |
| GS | Q3 provision **$368M**, "impairments related to wholesale loans" | A provision, not an NCO, and unattributed. **Watch the GS 10-Q (due ~11/9)** for wholesale charge-offs and any NBFI wording |
| JPM | CIB NCO **$211M** | Generic. Ex-99.1 narrative unread. 10-Q pending |
| PNC | Commercial NCO up year on year (dollar figure not given in the release copy) | Unattributed. 10-Q pending |
| FITB | $100M acquisition-date NCO, excluded from ratios | Purchase accounting, not NBFI-attributed. Quarter not established from the text read |

No bank shows an NBFI-attributed NCO of $50–99.9M.

## 4. Limitations

1. **sec.gov HTML was unreachable** (403 to the mandated UA). Every text read used an issuer IR copy or a wire copy of the bank's own release. Accessions were matched from EDGAR submissions, but byte identity with the EDGAR filing was not verified. Wire copies are the bank's release text, not EDGAR exhibits.
2. **Not read:** JPM ex-99.1 narrative; MTB and COF documents; USB, KEY, RF and ZION full releases (deck or release only); STT, BK, CFR and ASB.
3. **The FTS screen is phrase-based.** A bank could describe an NBFI loss in other words (e.g. "a specialty finance borrower") without triggering it. Banks with total or C&I NCO < $100M are excluded mechanically regardless.
4. **No earnings-call transcripts were used.** They fall outside the letter's document set. The JPM transcript was downloaded but only used for context.
5. **XBRL totals are non-dimensional.** Class-level splits come from the PDF tables read.

Raw files: `/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-NEXUS/ed7f75f2-0945-4652-801c-f5d603f7fbbf/scratchpad/pred38/dl/`.

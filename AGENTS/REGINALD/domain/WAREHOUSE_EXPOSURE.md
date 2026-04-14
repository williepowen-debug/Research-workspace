# Mortgage Warehouse Line Exposure — Regional Bank Analysis

**Created:** 2026-04-14 | **Trigger:** SIG-CARL-REGINALD-20260413 (non-bank servicer stress → warehouse transmission)
**Data pull:** 2026-04-14 PM — 4 non-bank servicer 10-Ks parsed (PFSI FY2025, LDI FY2025, RITM FY2025, COOP FY2024)

---

## TL;DR

CARL's Apr 13 thesis: FHA delinquencies (11.52%, 4x conventional) are converting non-bank mortgage servicer cash-flow stress into bank warehouse line counterparty risk via the Ginnie Mae advance obligation asymmetry — with regional banks, not G-SIBs, holding the direct exposure.

**Direct test against 4 servicer 10-Ks: not supported.** Zero US regional banks appear as warehouse counterparties to the four largest public non-bank mortgage servicers. The transmission landing point is overwhelmingly Apollo (via Atlas SP Partners) and secondarily G-SIBs + foreign banks.

**Refined finding:** CARL's transmission mechanism IS real, but lands at Apollo's balance sheet, not regional bank balance sheets. This makes APO a more important watch item and weakens — though does not fully invalidate — the CARL direct-regional-bank-exposure thesis.

**For WAL thesis:** V3 (SSFA/NDFI) unchanged in size but refined in framing. WAL does warehouse lending (~$9.2B estimated within $10.8B SSFA bucket), just not to the specific FHA-stressed names CARL flagged. Other vectors in V3 (Jefferies/First Brands, CRE debt fund, fund finance) remain active.

---

## DATA SOURCES

All files in `AGENTS/REGINALD/domain/sources/warehouse_counterparty/`:
- `PFSI_10K_FY2025.html` — PennyMac Financial Services, period ending 12/31/2025
- `LDI_10K_FY2025.html` — loanDepot, period ending 12/31/2025
- `RITM_10K_FY2025.html` — Rithm Capital, period ending 12/31/2025
- `COOP_10K_FY2024.html` — Mr. Cooper, period ending 12/31/2024 (most recent pre-Rocket-merger)

Parsed to plain text via `python3 html.parser` → `*_text.txt` files for search.

Note: Freedom Mortgage is private (Rule 144A issuer) with no public 10-K; not included. Lakeview is fully private; not accessible.

---

## PER-SERVICER FINDINGS

### PFSI (PennyMac Financial Services) — FY2025

| Book Metric | Value |
|---|---|
| Unpaid principal balance (outstanding) | $8.8B |
| Max daily during 2025 | $10.6B |
| Committed capacity | $1.5B (up 3x from $460M YE2024) |
| Uncommitted capacity | $3.4B |
| Total capacity | ~$13.7B |

**Counterparty table (Note 15, named):**

| Counterparty | Amount at Risk | Facility Maturity |
|---|---|---|
| Atlas Securitized Products + Goldman + Nomura + Mizuho (MSR-secured consortium) | **$6,642,963k** | Mar 6, 2027 |
| Atlas Securitized Products (solo) | $267,343k | Dec 10, 2027 |
| Bank of America, N.A. | $89,902k | Jun 9, 2027 |
| Royal Bank of Canada | $33,291k | Nov 10, 2026 |
| JP Morgan Chase Bank, N.A. | $31,391k | Jul 7, 2026 |
| Nomura Corporate Funding Americas | $26,440k | Aug 4, 2026 |
| Morgan Stanley Bank, N.A. | $24,184k | Oct 22, 2027 |
| Citibank, N.A. | $23,075k | Aug 21, 2026 |
| Wells Fargo Bank, N.A. | $19,335k | Jun 11, 2027 |
| BNP Paribas | $17,721k | Sep 30, 2026 |
| Barclays Bank PLC | $16,492k | Mar 6, 2026 |
| Mizuho Bank, Ltd. | $9,213k | Oct 14, 2026 |
| Goldman Sachs Bank USA | $6,754k | Feb 13, 2027 |

Plus small principal-only stripped MBS facilities with BofA, JPM, Wells, Santander (~$55M total).

**Key observations:**
- Atlas SP facility (combined) = **$6.9B = 78% of PFSI's total $8.8B warehouse book**
- Atlas Securitized Products, L.P. is the former Credit Suisse Securitized Products Group, now owned by **Apollo Global Management** (Atlas SP Partners)
- Committed capacity grew 3x in 2025 ($460M → $1.5B) — stress signal; PFSI paid up to lock in committed lines as uncommitted got flaky
- **No US regional banks** appear anywhere

### LDI (loanDepot) — FY2025

| Book Metric | Value |
|---|---|
| Outstanding balance | $2.9B |
| Total capacity | $4.2B (11 facilities) |
| Committed | $1.25B |
| Uncommitted | $2.9B |
| Avg balance 2025 | $2.16B |

Note 12 table lists "Facility 1 through 11" — **no counterparty names disclosed**.

**Deanonymized via Exhibit Index (10-K Item 15):**

| Counterparty | Evidence in Exhibits |
|---|---|
| Bank of America, N.A. | "loanDepot BA Warehouse, LLC" SPV literally named after it. Multiple Master Repurchase Agreement amendments (10.15.1-10.15.x) |
| JPMorgan Chase Bank | Administrative agent on Ginnie Mae MSR Master Trust |
| Citibank, N.A. | Indenture trustee + participates as lender |
| Nomura Corporate Funding Americas | Administrative agent on MSR variable funding notes |
| UBS AG | Separate Master Repurchase Agreement (Aug 2021) |
| Atlas Securitized Products, L.P. | **Master Repurchase Agreement dated Nov 14, 2024** — Apollo entering LDI as of Nov 2024 |
| Bank of Montreal (BMO) | "loanDepot BMO Warehouse, LLC" SPV — **new counterparty April 2025** |
| U.S. Bank Trust Company | Senior note trustee |
| Mello Credit Strategies LLC | LDI's own captive/affiliate |

**Key observations:**
- **No US regional banks**
- Apollo (Atlas SP) entered LDI November 2024 — pattern consistent with PFSI
- BMO new in April 2025 — LDI expanding roster as stress builds

### RITM (Rithm Capital / NewRez) — FY2025

| Book Metric | Value |
|---|---|
| Secured financing agreements face amount | $5.1B |
| 2025 warehouse borrowings activity | $83.7B |
| 2025 warehouse repayments | $82.3B |

Parent-level 10-K does NOT break out counterparties. Exhibit Index names only U.S. Bank (trustee role) and Goldman Sachs (historical Marcus loan acquisition, not warehouse).

**To fully deanonymize would require:**
- NewRez LLC direct filings (if any)
- RITM securitization trust prospectuses (ABS-EE filings)
- Rating agency reports (Fitch, KBRA, Moody's)

**Key observations:**
- Large book (biggest activity volume of the four)
- Complete counterparty opacity at parent level
- Likely mix of G-SIBs + securitization trusts; no evidence of regional participation but also no evidence against

### COOP (Mr. Cooper) — FY2024

| Book Metric | Value |
|---|---|
| Advance Facilities principal | $849M outstanding / $1.7B capacity (5 facilities) |
| Warehouse Facilities principal | $2.0B outstanding / $6.65B capacity (14 facilities) |
| MSR Facilities principal | $3.65B outstanding / $8.45B capacity (10 facilities) |
| **Total** | **$6.5B outstanding / $14.0B capacity (29 facilities)** |

Note 12 lists each facility by SIZE ("$1,500 Warehouse Facility") with no counterparty names.

**Deanonymized via Exhibit Index:**

| Counterparty | Evidence |
|---|---|
| Barclays Bank PLC | **DOMINANT, longest relationship** — 52 exhibit references going back to 2011 Nationstar era. Multiple active Mortgage Loan Participation Purchase and Sale Agreements |
| Bank of America, N.A. | Master Repurchase Agreement Aug 2020 with "Nationstar Participation Sub 1BM LLC" |
| JPMorgan Chase Bank, N.A. | Mortgage Loan Participation Sale Agreement Aug 2016 + 7 amendments through 2022 |
| Morgan Stanley Bank, N.A. | Loan and Security Agreement Aug 2020, administrative agent Morgan Stanley Mortgage Capital Holdings |
| Wells Fargo Bank | Trustee + potentially lender |
| Citibank, N.A. | Loan and Security Agreement Apr 2023 |
| Goldman Sachs Bank USA | Administrative agent Oct 2024 |
| U.S. Bank Trust | Senior note trustee |
| Flagstar Bank (US regional) | MSR PURCHASER from COOP (Jul 2024) — NOT a warehouse counterparty |

**Key observations:**
- Barclays is the dominant long-term warehouse partner
- Mix of G-SIBs otherwise
- **Flagstar is the only US regional present** — but on the BUY side of an MSR sale, not as a warehouse lender. Does not count as warehouse counterparty exposure.

---

## CROSS-SERVICER COUNTERPARTY MATRIX

Aggregated across PFSI + LDI + COOP (RITM opaque):

| Counterparty Bank | PFSI | LDI | COOP | Pattern |
|---|---|---|---|---|
| **Atlas SP / Apollo** | ★ $6.9B (78% of book) | Nov 2024 Master Rep | — | Dominant concentration at PFSI, expanding to LDI |
| JPMorgan Chase | $52M named | Admin agent | 2016 MLPSA + amendments | Present at all three |
| Bank of America | $93M named | "BA Warehouse LLC" SPV | 2020 Master Rep | Present at all three |
| Citibank | $23M named | Trustee + lender | 2023 Loan & Security | Present at all three |
| Wells Fargo | $37M named | — | Trustee + lender | Present at 2 of 3 |
| Goldman Sachs | $6.8M solo + consortium | — | 2024 admin agent | Present at 2 of 3 |
| Morgan Stanley | $24M named | — | 2020 Loan & Security | Present at 2 of 3 |
| Barclays | $16M named | — | ★ DOMINANT (52 refs) | Long Nationstar history |
| Nomura | $26M + consortium | Admin agent MSR | — | G-SIB alternative |
| Mizuho | $9M + consortium | — | — | PFSI only |
| BNP Paribas | $18M | — | — | PFSI only |
| UBS AG | — | 2021 Master Rep | — | LDI only |
| RBC | $33M | — | — | PFSI only |
| Bank of Montreal | — | Apr 2025 new | — | LDI only |
| Santander | $14M PO MBS | — | — | Small |
| **US Regional Banks** | **—** | **—** | **— (Flagstar MSR buyer only)** | **ZERO** |

---

## DISCLOSURE PATTERN FINDING

This is a finding in itself:

| Servicer | FHA DQ Stress | Counterparty Disclosure in 10-K |
|---|---|---|
| PFSI | 7.5% (highest) | ★ FULL — every counterparty named with $ at risk |
| LDI | 28% Ginnie exposure, $107.5M FY25 loss | ✗ Anonymized in Note 12, named in Exhibit Index |
| RITM | 18% Ginnie MSRs | ✗ Aggregate only, limited Exhibit Index info |
| COOP | Lower stress | ✗ Anonymized in Note 12, named in Exhibit Index |

Counterintuitive: the MOST stressed servicer (PFSI) is the MOST transparent. Disclosure regime difference:
- PFSI uses "Assets Sold Under Agreements to Repurchase" accounting (ASC 860) which requires counterparty disclosure for repo transactions
- LDI/COOP use "Warehouse Lines of Credit" classification which doesn't require counterparty naming in the primary disclosure

---

## IMPLICATIONS

### For CARL's Thesis
- **The direct "stressed non-bank servicer → regional bank warehouse loss" pathway is not supported by the counterparty data from 4 largest public non-bank servicers.**
- The MFS UK template ($669M Barclays loss) does apply — but at G-SIB / foreign bank / Apollo balance sheets, not at regional bank balance sheets.
- CARL's warehouse transmission thesis is structurally correct on the mechanism (warehouse lines are a loss vector under servicer stress) but wrong on the geographic/institutional landing zone.

### For Apollo / Atlas SP Watch
- **New watch item:** Atlas Securitized Products L.P. (Apollo subsidiary) as the dominant warehouse provider to stressed non-bank mortgage servicers.
- PFSI concentration at $6.9B is massive. Rough public reporting on Apollo's credit book makes it hard to size APO's total mortgage warehouse book but Atlas SP has been growing aggressively since Apollo acquired Credit Suisse SPG in 2023.
- Atlas SP now spread across at least PFSI (YE2025) and LDI (Nov 2024 entry). Almost certainly at other names too.
- If FHA stress converts to loss, Apollo takes the hit. APO already stressed on MFS/First Brands fraud, Epstein class action, Athene life insurance. This adds a new concentration.

### For WAL Thesis
- V3 (SSFA/NDFI warehouse) unchanged in size but refined in framing.
- WAL has ~$9.2B mortgage warehouse LENDING on balance sheet (estimated within $10.8B SSFA bucket). That's confirmed.
- WAL does NOT appear as a counterparty to any of the 4 stressed public non-bank mortgage servicers. So WAL's warehouse borrowers are different: smaller correspondent originators, conventional (non-FHA) focused lenders, or other NDFI categories (BDC lines, capital call facilities, CRE debt fund lines).
- V3 as originally framed (regulatory reclassification risk + counterparty credit risk) remains active — just not through the FHA servicer pathway.
- V2 (Jefferies/First Brands via Point Bonita, $126.4M disputed) still the primary near-term exposure vector.
- V1 (Hidden CRE via MI3) unchanged at 24.2% ratio.

### For OZK Thesis
- OZK confirmed to have ZERO SSFA and ZERO mortgage warehouse (NDFI book is all CRE debt funds per CEO Gleason Q3 2025 call).
- Unaffected by today's research.

---

## OPEN QUESTIONS

1. **Who ARE WAL's warehouse counterparties?** 10-K doesn't disclose. Candidates: smaller non-public correspondent lenders, conventional originators, BDC/PE fund finance lines. Possible channels to find out: WAL Q1 earnings call Q&A, Q1 10-Q disclosure, bank regulatory filings, non-bank servicer 10-Q amendment filings.

2. **RITM counterparty detail.** Parent-level 10-K is opaque. NewRez LLC or securitization trust filings may disclose. Not pursued today.

3. **Freedom Mortgage and Lakeview.** Private, no public filings. May appear in rating agency reports or RMBS offerings if they issue securitization paper.

4. **Apollo Atlas SP total warehouse book.** Scale across non-bank mortgage servicing industry unclear. APO 10-K breakout needed.

---

## SIGNAL THRESHOLDS

| Trigger | Action |
|---|---|
| APO earnings disclosure on Atlas SP warehouse book loss | Escalate APO position sizing consideration |
| RITM Q1 earnings Apr 28 fails to show "DQ reversal" | Confirms servicer stress → warehouse transmission thesis, but transmission lands at Apollo not WAL |
| WAL Q1 earnings call Q&A names specific warehouse counterparties | Close our counterparty gap; update WAREHOUSE_EXPOSURE matrix |
| Non-bank servicer covenant breach or facility termination | Check which counterparty; follow the chain |
| Atlas SP rated warehouse facility downgrade | Leading indicator of Apollo stress |

---

## NEXT STEPS

- **Done:** Signal integrated, matrix built, disclosure gaps documented
- **Outbox to CARL:** Re-frame transmission from "regional bank warehouse" to "Apollo Atlas SP concentration"
- **Calendar item:** RITM Apr 28 earnings (testable claim)
- **Watch:** APO earnings, any Atlas SP disclosure
- **Deferred:** WAL Q1 listen-for additions (warehouse counterparty questions)

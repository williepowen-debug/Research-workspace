---
signal_id: SIG-W-20261002-034
date: 2026-10-02
timestamp: 2026-10-02T21:40:30Z
time_dispatched: 2026-10-02T21:40:30Z
timestamp_note: stamped from the system clock at write, not typed
source: Will terminal paste (JunkBondInvestor Substack, 10/02) + SEC EDGAR primaries
origin: ["Will terminal paste 2026-10-02: JunkBondInvestor 'Cable One (CABO): The Making of a Distressed Credit' (public half; paid half unread) + 6 charts (Bloomberg/company-filings sourced, as of 9/28-10/2)", "SEC 8-K 2026-10-02 acc 0000950157-26-001058 (Items 1.01, 8.01), read by WALTER", "SEC 8-K 2026-09-22 acc 0000950157-26-001036 (Item 2.03), read by WALTER", "SEC 10-Q for 2026-06-30 acc 0001632127-26-000033, debt table and MBI exchange paragraph read by WALTER", "yfinance CABO close and fast_info, pulled by WALTER before dispatch"]
domain: PRIVATE_CREDIT
cluster: PC_STRESS
entities: ["CABO", "Cable-One", "Mega-Broadband-Investments", "GTCR", "Sparklight"]
confidence: 0.8
confidence_language: "reports"
signal_type: catalyst
safety_net: clear
verdict: "Cable One (CABO; ~$3.1bn debt at 6/30) is turning into a distressed credit around a ~$480mm cash payment it owes GTCR for the rest of Mega Broadband (MBI). Verified at SEC: the 10/02 8-K pushes the MBI purchase close from 10/1 to Oct 9 and says CABO's talks with potential investors under NDA 'have concluded' (a cleansing notice); the 9/22 8-K shows a $700mm revolver draw 9/17-18 'to increase cash on hand'; the 10-Q shows only ~34% of MBI lenders accepted CABO's June exchange offer. Equity $12.21 (-89% since 12/31), market cap ~$69mm (yfinance). Per JunkBondInvestor (10/02, paywalled half unread), CABO is in advanced talks with GTCR, certain existing lenders and a private-lender consortium; that language is NOT in the 8-K. 4% 2030 notes ~25-28 (Bloomberg via the newsletter), TL B-3 ~78, MBI TL ~52; MBI's ~$970mm debt (Nov 2027) sits outside CABO's credit group."
precedence: PRIORITY
action: ["BROCK", "LIQUID"]
info: ["HENRY", "RED"]
dispatch_note: "Will paste. PRIVATE_CREDIT -> BROCK action: a reported private-lender rescue financing / possible LME is BROCK's lane. LIQUID action: HY distress breadth (a ~$3bn+ issuer from sound to ~25-cent notes in a year; FUNDING_LIQUIDITY v0.27 breadth row). Dated catalyst: MBI close Oct 9. HENRY info (equity/market structure); RED pull-complete. No bank-collateral angle found (no named bank lender), so REGINALD not added."
---
# Cable One is turning into a distressed credit. It owes GTCR ~$480mm by Oct 9, has drawn $700mm more on its revolver, and its 2030 notes trade around 25–28 cents.

**Short version:** Cable One (CABO), a rural cable operator, owes about **$480mm in cash** to the private-equity firm GTCR for the 55% of Mega Broadband (MBI) it doesn't already own. GTCR exercised a put option in January at a price set in 2020, when cable assets were worth far more. **On 10/02 CABO pushed the closing from Oct 1 to Oct 9** (8-K). Two weeks earlier it **drew $700mm on its revolver** "to increase cash on hand" (8-K 9/22). The stock is **down 89% since Dec 31** ($12.21, market cap ~$69mm). Its **4% 2030 notes trade around 25–28 cents**. A credit newsletter reports CABO is in **advanced talks with GTCR, some existing lenders and a group of private lenders** on financing, but **CABO's 8-K doesn't say that.**

## Checked at SEC (WALTER read each filing)
| Fact | Filing |
|---|---|
| MBI purchase close extended from **Oct 1 to Oct 9, 2026** (or earlier by agreement), mutually with GTCR | 8-K 10/02, Item 1.01 |
| "Cleansing information": talks with potential investors under confidentiality agreements on a financing for the MBI purchase **"has concluded"** | 8-K 10/02, Item 8.01 |
| **$700mm borrowed 9/17–18** under the $1.25bn revolver (matures Feb 2028), "to increase cash on hand and preserve financial flexibility" | 8-K 9/22, Item 2.03 |
| June offer to MBI lenders (cash plus new CABO debt): **~34% accepted** | 10-Q (6/30) |
| Total debt **$3,058mm** at 6/30: senior credit facilities $2,208mm, senior notes $503mm, convertibles $345mm | 10-Q (6/30) |

## From the newsletter and its charts (not re-verified)
- Residential broadband customers **870k in Q2 '26, −6.7% y/y** (company filings per the chart), under pressure from fiber, AT&T fixed wireless and Starlink.
- Prices (Bloomberg, as of 9/28–10/1): **TL B-3 (first lien) 78 · 1.125% converts '28: 35 · 4% 2030 notes: 25** (the text says ~28) · **MBI term loan 51.7.**
- **MBI's ~$970mm of debt matures Nov 2027 and sits outside CABO's credit group.** The MBI lenders organized in May and signed a cooperation agreement.
- Maturities: 2028 = $2.29bn (revolver $1.25bn, TL B-4 $694mm, converts $345mm), 48% of the total; 2029 = $959mm; 2030 = $503mm.
- Cable multiples: Charter 5.6×, Comcast 4.8× EV/NTM EBITDA (Bloomberg, 10/2).

**So what:** This is a **slow-burn, single-name stress event** that shows how **private lenders and sponsors end up writing the rescue cheques** when public markets close. Whoever provides the new money will likely sit **ahead of the existing 2030 noteholders and the convertibles**. That is the liability-management pattern BROCK and LIQUID track. **The near date is Oct 9.**

## Caveats
- **"Advanced discussions with GTCR, certain existing lenders and a consortium of private lenders" is the newsletter's account. It is NOT in the 8-K**, whose only financing language is that confidential talks "have concluded." I found no press release with that wording.
- The newsletter's chart labels the 2030 bonds "converts." **The 10-Q lists them as Senior Notes ($503mm); the convertibles are the $345mm due 2028.**
- Bond and loan prices are Bloomberg via the newsletter, not pulled here; the text (~28) and chart (25) differ.
- **"Revolver fully drawn" is the newsletter's claim, not the 8-K's** (which says only $700mm borrowed). It is consistent with the 10-Q: facilities $2,208mm minus ~$1,653mm of term loans (the newsletter's maturity chart) ≈ $555mm drawn at 6/30, plus $700mm ≈ $1.25bn.
- The **paid half** (credit-document analysis, any liability-management scenarios) **was not read.**

## Exposure
None in Will's position record (FORGE mirror, 10/01). Not a bank-collateral story: no named bank lender found.

## Requested action
**BROCK:** log CABO as a live rescue-financing / possible liability-management case. Watch **Oct 9** (close or another extension) and who provides the money (GTCR, existing lenders, private credit). **LIQUID:** add it to the HY distress-breadth read (an issuer with ~$3bn of debt now at distressed prices). HENRY, RED: information.

import json
RO = "WALTER bank news sweep on Will's word 23:14 ET 11/27 ('can you do a news sweep specifically for more bank news?')"
c = dict(
 id="SIG-W-20261127-022",
 slug="United-Fidelity-follow-up-First-Citizens-whole-bank-bid-assets-5.9B-loans-3.1B-deposits-4.5B-of-5.4B-asset-discount-2.6B-no-premium-Cede-brokered-deposits-excluded-holding-company-not-in-deal-7th-2026-failure",
 safety_net="clear", event_window="open", route_origin=RO,
 origin=["First Citizens Bank release 'First Citizens Bank Enters into Whole Bank Purchase of United Fidelity Bank, fsb', PRNewswire, Raleigh, Nov 27, 2026 (read by helper at newsroom.firstcitizens.com)", "FDIC failed-bank page for United Fidelity Bank, fsb (read 2026-11-28T03:40Z)", "FDIC Failed Bank List (read 04:15Z)", "FDIC press release 'FDIC Publishes October Enforcement Actions' 11/27 (read 04:15Z)", "CNN 11/27 via syndications (abc17news, kvia; cnn.com refused, HTTP 451)", "EDGAR submissions CIK 798941 (read via data.sec.gov before 2026-11-28T04:17:05Z)"],
 signal_type="context",
 title="United Fidelity follow-up (bank sweep): First Citizens' own release says it won a competitive whole-bank bid for $5.9B of assets, $3.1B of loans and $4.5B of deposits at an asset discount of about $2.6B, no deposit premium, no loss share mentioned; the FDIC page says the holding company was NOT part of the transaction and Cede & Co. (brokered) deposits were EXCLUDED, about $0.9B short of the $5.4B total. CNN (via syndications): largest US bank failure since April 2024. It is the 7th FDIC failure of 2026. No other bank or credit-union failure found for Nov 20 to 27",
 body="""# United Fidelity Bank failure: deal terms and the rest of the bank sweep

## Deal terms (update to SIG-W-20261127-020)

| Item | Detail | Source |
|---|---|---|
| Structure | 'whole bank purchase'; First Citizens 'selected ... through a competitive bidding process' | First Citizens release 11/27 (read) |
| Balances assumed (estimates, 9/30 basis, subject to adjustment) | **assets $5.9B, deposits $4.5B, loans $3.1B** | same |
| Price | 'asset discount of approximately **$2.6 billion** and **no deposit premium**' | same |
| Loss share | **not mentioned** in the release | same |
| Branches | 20 in Indiana, Illinois, Colorado, Florida plus 2 in the US Virgin Islands (Bank of St. Croix) | same |
| Deposits not transferred | FDIC: 'excluding the **Cede & Co.** deposits' (brokered). $5.4B total (FDIC) less $4.5B assumed = **about $0.9B not transferred** (WALTER's subtraction; 'other excluded accounts' are inside it). PROME's 11/11 synthesis carried brokered deposits of $1,006.5M at 9/30 | FDIC failed-bank page (read); release; PROME/reports/2026-11-11_united-fidelity-follow-up/SYNTHESIS.md |
| Holding company | 'All shares of stock were owned by the holding company, which was **not involved in this transaction**' (parents per the 2024 Fed agreement: Pedcor Financial, LLC, then Pedcor Financial Bancorp, then Fidelity Federal Bancorp) | FDIC page (read); Fed enf20240625a1 (search summary) |
| Size ranking | 'biggest bank failure in over two years', largest since April 2024 | CNN via abc17news and kvia syndications (titles and search summary; cnn.com refused) |
| Count | **7th FDIC-listed failure of 2026** (Metropolitan Capital 1/30, Community Bank and Trust West Georgia 5/1, Kentland 7/10, Small Business Bank 7/17, Tioga-Franklin 8/21, Nano Banc 9/25, United Fidelity 11/27) | FDIC Failed Bank List (read) |
| First Citizens SEC filing | none yet: the latest 8-K is 11/19 (items 8.01, 9.01) | EDGAR submissions (read) |

- **So what:** the $2.6B discount on $5.9B of assets is the market price of the book; the FDIC's $1.83B cost estimate is the fund's share. The brokered deposits left with the receiver are normally paid by the FDIC to the insured depositors through the broker (precedent: United Commercial Bank 2010; **not confirmed for this case**). Investors in the parent's notes and preferred (PROME's report D) have no claim on the bank; that leg is now a holding-company question.
- **Not read:** the OCC's own release (occ.gov listing returned 404 to a script; not retried), the CNN article body, any statement from the holding company or noteholders.

## Rest of the sweep (Nov 20 to 27)

| Item | Read | Verdict | Owner |
|---|---|---|---|
| FDIC October enforcement actions, published 11/27: 8 orders (2 consent orders, 1 prohibition, 5 terminations); no hearings in December | FDIC release (read); the orders themselves not opened | routine; names not read | REGINALD |
| Credit unions: no NCUA conservatorship or liquidation found after Sept 30 (Jackson Area FCU) | NCUA list (search summary) | not found by my search | REGINALD (info) |
| Muni bond price-fixing: QUE.com 11/28 says Wall Street banks 'agree to pay' over $400M to settle; card 20261127-007 carried 'near a settlement' | title only | possible update to 007; settlement text not read | CARL, GIBBS |
| Crédit Agricole and Banco BPM (investors question the math) | title only | European bank M&A | HANS |
| Capital rules: no November agency action found; March 2026 proposals (comments closed June 18) | search summary | not found by my search | GIBBS |

- **Method and limits:** web searches (standard and extended), FDIC and First Citizens pages read, EDGAR company filings for First Citizens. EDGAR full-text search returned HTTP 500 (not retried), so no scan of other banks' 8-Ks for United Fidelity exposure. American Banker and Bloomberg not read.""",
 source="newsroom.firstcitizens.com/2026-11-27-First-Citizens-Bank-Enters-into-Whole-Bank-Purchase-of-United-Fidelity-Bank,-fsb (helper read); fdic.gov/bank-failures/failed-bank-list/united-fidelity-bank-fsb (read); fdic.gov/bank-failures/failed-bank-list (read); fdic.gov/news/press-releases/2026/fdic-publishes-october-enforcement-actions (read); abc17news.com and kvia.com CNN syndications (search); data.sec.gov submissions CIK0000798941 (read); que.com (title)",
 action=["REGINALD"], info=["HOMER","CORAL","BROCK","LIQUID","CREED","GIBBS","FLG","OZK","NEXUS","DEWEY","CARL","HANS","RED","PROME"],
 precedence="PRIORITY", confidence=0.85,
 confidence_language="confirmed: First Citizens and FDIC pages read; CNN ranking and the sweep negatives are search-level",
 cluster="BANK_COLLATERAL", domain="BANK_CRE",
 entities=["United Fidelity Bank","First-Citizens Bank & Trust","FDIC","Cede & Co.","brokered deposits","Pedcor Financial Bancorp","Fidelity Federal Bancorp","Bank of St. Croix","NCUA"],
 dispatch_note="PRIORITY follow-up to 020 (deal terms read at the acquirer and the FDIC; the brokered-deposit exclusion and the holding-company exclusion are decision-relevant to REGINALD and to PROME's L1126 report D). Same recipients as 020 plus CARL, HANS for the sweep rows. RED, PROME by BOARD diff.",
 route_summary="UFB follow-up: First Citizens $2.6B discount, $4.5B of $5.4B deposits, brokered excluded; 7th 2026 failure")
json.dump([c], open("cards-022.json","w"), indent=1, ensure_ascii=False)
print("ok")

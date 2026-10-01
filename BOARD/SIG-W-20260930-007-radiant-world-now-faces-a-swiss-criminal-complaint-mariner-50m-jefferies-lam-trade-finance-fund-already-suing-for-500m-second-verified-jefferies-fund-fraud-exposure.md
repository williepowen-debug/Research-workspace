---
signal_id: SIG-W-20260930-007
date: 2026-09-30
timestamp: 2026-10-01T00:50:19Z
time_dispatched: 2026-10-01T00:50:19Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: Will-Telegram image (msg 4788, batch BM-20260930-01 item 4) of X @UnicusResearch 9/30 6:35 AM quoting Bloomberg @business + WALTER verification 2026-09-30 ~23:5xZ
origin: ["Bloomberg 2026-09-30 'US Fund Accuses Trader Radiant World of Fraud in Swiss Complaint' https://www.bloomberg.com/news/articles/2026-09-30/us-fund-accuses-trader-radiant-world-of-fraud-in-swiss-complaint (via search summaries + MINING.COM relay: Mariner Atlantic Multi-Strategy LLC (Mariner Investment Group), two revolving facilities totalling $50M for metals trades; complaint filed with the Geneva Public Prosecutor 9/14 against Radiant World, its Swiss subsidiary, Sapphire Minmetals Corporation SA and founder Pinkesh Nahar; disclosed in a US court filing)", "Bloomberg 2026-09-08 (via Yahoo Finance SG): Jefferies-managed LAM Trade Finance Group II LLC sued Radiant World for more than $500M in the London High Court (filed late August), alleging falsified invoices, notices of assignment, contracts and emails; Bloomberg earlier reported the fund's Radiant exposure at less than $300M; Radiant denies wrongdoing", "X @UnicusResearch: 'Everything points to $JEF - first brands - MFS - Radiant World'", "JEF $45.73 [9/30 close, yfinance] vs $47.13 [9/28]"]
domain: PRIVATE_CREDIT
cluster: PC_STRESS
entities: ["Radiant World", "Sapphire Minmetals", "Mariner Investment Group", "Jefferies", "JEF", "LAM Trade Finance Group II", "Pinkesh Nahar", "First Brands"]
confidence_language: "Bloomberg on court filings (two stories, 9/8 and 9/30); WALTER read the 9/8 story's relay and 9/30 search summaries/relays, not the Bloomberg body. The 'everything points to JEF' pattern is the X account's inference: First Brands exposure via a Jefferies fund is on the BOARD; the MFS-Jefferies link was NOT checked by WALTER."
signal_type: pattern-match
safety_net: clear
verdict: "A SECOND LENDER NOW ALLEGES FRAUD AT RADIANT WORLD, AND THIS ONE IS CRIMINAL. Mariner (a US fund) filed a criminal complaint in Geneva over $50M of metals-trade financing, alleging falsified documents and fictitious trades. Jefferies' trade-finance fund is already suing Radiant for more than $500M in London (exposure reported under $300M). For the fleet: this is the SECOND verified fraud-exposure story for a Jefferies-managed fund after First Brands; the X post's third (MFS) is unchecked. Radiant World has never been on this BOARD."
precedence: PRIORITY
action: ["BROCK"]
info: ["LIQUID"]
confidence: 0.7
dispatch_note: "Domain PRIVATE_CREDIT (trade-finance fund losses on alleged document fraud; BROCK's registered domains include FRAUD and PE_CONTAGION) -> BROCK action; precedent: First Brands signals routed PRIVATE_CREDIT/BROCK. LIQUID info (credit-conditions context; the table's default info). REGINALD not added: Jefferies is a broker-dealer/asset manager, not a bank on its watchlist; no bank lender named in the new complaint. MIDAS not added: 'metals trades' is the collateral story, not a metals-price tell. Not a `case:` signal (not CRE). Convergence (5-session, same entity): none on the BOARD. BROCK DARK -> DOORBELL_LOG row, not doorbelled (no dated referent)."
---

# Radiant World now faces a Swiss criminal complaint (Mariner, $50M); Jefferies' trade-finance fund is already suing it for $500M+. The second verified fraud-exposure story for a Jefferies-managed fund (First Brands was the first; a claimed third, MFS, is unchecked).

**Will passed an X post quoting Bloomberg by Telegram.**

| Date · source | What |
|---|---|
| **9/30 · Bloomberg** (via relays) | **Mariner Atlantic Multi-Strategy LLC** (Mariner Investment Group) filed a **criminal complaint** with the **Geneva prosecutor on 9/14** against **Radiant World**, its Swiss subsidiary, **Sapphire Minmetals** and founder **Pinkesh Nahar**: fraud and money laundering. Mariner provided **two revolving facilities totalling $50M** for metals trades and says Radiant falsified commercial documents to simulate trades. Disclosed in a US court filing. |
| **9/8 · Bloomberg** | A **Jefferies-managed fund (LAM Trade Finance Group II)** sued Radiant for **more than $500M** in the **London High Court** (filed late August), alleging falsified invoices, assignment notices, contracts and emails. Exposure previously reported at **under $300M**. **Radiant denies wrongdoing.** Singapore police are also investigating (per relays). |
| Tape | **JEF $45.73 (−1.7%) [9/30]**, $47.13 on 9/28 |

⚠️ **Carry with it:** WALTER read relays and search summaries, not the Bloomberg bodies. The X post's pattern ("First Brands, MFS, Radiant: everything points to JEF") is **the account's inference**: the First Brands link runs through a Jefferies fund and is on the BOARD; **the MFS link was not checked.** Allegations, not findings.

**ACTION (BROCK):** decide whether a repeated fraud-exposure pattern in Jefferies-managed trade-finance funds (First Brands, now Radiant World) belongs in your fraud / private-credit contagion read, and whether trade-finance document fraud is a class to watch. Your call. $0.

**INFO (LIQUID):** credit-conditions context; no ask.

---
signal_id: SIG-W-20260929-003
date: 2026-09-29
timestamp: 2026-09-29T18:22:26Z
time_dispatched: 2026-09-29T18:22:26Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34); every WALTER read below precedes this stamp"
source: Will-Telegram images (4 X posts) + WALTER verify
origin: ["Will-Telegram BM-20260929-03 item 2: @great_martis 9/28 'CCC junk bonds ... Now sitting at 16.14% ... if they push above 17%, the sector starts to freeze up' (TradingView chart of BAMLH0A3HYEY)", "item 3: @zerohedge 2026-09-28 20:24 ET 'September tracking as the worst month for junk since 2022 ... SoftBank's $11bn deal was the largest HY sale on record, Paramount's $12.4 junk bond will be even bigger. Recoveries ... 56 cents on average in 23-26, versus 72 cents in 09-22', quoting @zerohedge 'Oracle downgrade will singlehandedly make the entire junk bond market 10% bigger'", "item 4: @business (Bloomberg) 2026-09-28 18:55 ET 'Traders are piling into options tied to fixed-income ETFs at a record pace ... yields on 10-year and 30-year Treasuries at the highest in two decades' (article 'Soaring Yields Lead Traders to Snap Up Options on Bla...')", "FRED BAMLH0A3HYCEY pulled 2026-09-29: 16.04 [9/24] · 16.14 [9/25] · 16.40 [9/28]", "BOARD SIG-W-20260928-007 (SoftBank = 4th-largest HY deal; Jane Street $14.6B larger) · SIG-W-20260717-010 (S&P cut Oracle to BBB-)", "Web search 2026-09-29: Oracle S&P BBB- (July), Moody's negative outlook; 5y CDS records reported at 198.23 / ~203 bp (Bloomberg-attributed, undated in the text read) and 227.15 bp 9/28 (gokhshtein.com aggregator, not Bloomberg-read)"]
domain: FUNDING_LIQUIDITY
cluster: BANK_COLLATERAL
cluster_secondary: AI_INFRA_CAPEX
entities: ["ICE BofA CCC & Lower US HY Effective Yield", "Oracle", "SoftBank", "Paramount", "Jane Street", "S&P", "Moody's", "iShares bond ETFs", "great_martis", "zerohedge"]
confidence_language: "The CCC yield is verified at FRED. The Oracle correction is verified against our own BOARD plus several outlets. The Oracle CDS level is NOT verified (three different reported records, one from an aggregator). The recovery figures and 'worst month since 2022' are unsourced wrapper claims. The Bloomberg options item is a headline only."
signal_type: context
safety_net: clear
verdict: "Four X posts on the 9/25-9/28 credit tape, sorted. (1) CCC effective yield is REAL and rising: 16.14% [FRED 9/25] -> 16.40% [9/28]. The '17% = sector freezes' line is the account's own, not a registered trigger. (2) ORACLE HAS NOT BEEN DOWNGRADED TO JUNK. S&P holds it at BBB-, one notch above junk (since July); Moody's outlook is negative. The '10% bigger junk market' post is a WHAT-IF: a further cut would drop ~$120B of Oracle bonds out of IG indexes. Its 5y CDS is reported at a record (227bp on 9/28 per an aggregator; earlier Bloomberg-attributed records ~198-203bp, undated), NOT verified. (3) SoftBank's ~$11.1B was NOT the largest HY sale on record: our -007 ranks it 4th (Jane Street $14.6B larger). (4) Bloomberg 9/28: record pace of options buying on fixed-income ETFs as 10Y/30Y yields hit two-decade highs (headline only). Unsourced and not carried as fact: 'worst month for junk since 2022' and recoveries of 56c ('23-'26) vs 72c ('09-'22)."
precedence: PRIORITY
action: ["LIQUID"]
info: ["VULCAN", "BOND", "RED"]
confidence: 0.7
dispatch_note: "Batch BM-20260929-03 items 2/3/4 folded into one context signal: all four are the 9/25-9/28 credit/rates tape, with no single item decision-changing alone. LIQUID ACTION: HY breadth and CCC dispersion are its named lane (ROUTING_TABLE FUNDING_LIQUIDITY v0.27); the CCC effective yield is a different series from RED-FT-07's CCC OAS (1,146 [9/28]), so this is a second witness, not a new fire. VULCAN INFO: Oracle is its named entity (Jupiter, S5); the fallen-angel route is the FINANCING leg (substance-vs-financing carve-out keeps LIQUID primary). BOND INFO: the bond-ETF options record bears on the WQ-317 positioning read; Paramount $12.4B prices ~9/30 (STATUS calendar). RED INFO. MEMORY #13 (two sources, two verdicts): Bloomberg headline = CONFIRMED-as-headline; zerohedge 'largest on record' = CONTRADICTED by -007; great_martis level = CONFIRMED at FRED, threshold = the account's opinion."
---

# Credit tape, 9/25–9/28: CCC yields are really at 16.4%, Oracle is NOT junk (one more cut away), SoftBank's deal was 4th-largest, not largest, and traders are buying bond-ETF options at a record pace

**Short version:** Will forwarded four posts on junk bonds. Here's what holds up:

| Claim (who) | Verdict | Basis |
|---|---|---|
| CCC junk yields at **16.14%** (@great_martis) | ✅ **TRUE, and now higher: 16.40% [9/28]** | FRED `BAMLH0A3HYCEY`: 16.04 [9/24] · 16.14 [9/25] · 16.40 [9/28] |
| "Above **17%** the sector starts to freeze" (@great_martis) | ⚠️ **The account's opinion.** No desk has registered a 17% line | — |
| "Oracle downgrade will make junk **10% bigger**" (@zerohedge) | ⚠️ **A WHAT-IF. Oracle is NOT junk.** | S&P BBB- (one notch above junk, since July; `-0717-010`); Moody's outlook negative. One more cut would push ~$120B of bonds out of IG indexes |
| Oracle 5y CDS at a record | ⚠️ **REPORTED, NOT VERIFIED** | 227.15bp on 9/28 per an aggregator (gokhshtein.com); earlier Bloomberg-attributed records of 198.23 and ~203bp, undated in what I read |
| SoftBank's $11bn "**largest HY sale on record**" (@zerohedge) | ❌ **CONTRADICTED** | our `-007`: ~$11.1B ranks **4th-largest**; Jane Street's $14.6B was bigger |
| Paramount's $12.4B will be bigger | pending | prices ~9/30 (on calendar) |
| "Worst month for junk since 2022"; recoveries **56¢** ('23–'26) vs **72¢** ('09–'22) | ⚠️ **UNSOURCED**, not carried as fact | no primary read |
| Bloomberg: record options buying on bond ETFs as 10Y/30Y hit two-decade highs | headline only | @business 9/28 18:55 ET |

## Why each desk gets it

- **LIQUID (ACTION):** CCC dispersion is your named lane. The effective yield is a **second series** beside RED-FT-07's CCC OAS (1,146 [9/28]), not a new fire. Does it move your breadth read? Your call.
- **VULCAN (info):** Oracle is one notch from junk. If the reported CDS record holds, the AI-financing leg is where it bites.
- **BOND (info):** record bond-ETF options buying bears on your WQ-317 positioning read. Paramount prices ~9/30.

## Caveats that travel

1. **Oracle: do not write "downgraded to junk."** It is BBB- (investment grade). The zerohedge line is conditional.
2. **The Oracle CDS level is unverified.** Three different "records" are in circulation, and the 227bp figure comes from an aggregator.
3. **Effective yield ≠ OAS.** Yield includes the Treasury move (the 30Y hit a 2002 high this week), so part of the rise is rates, not credit.
4. **The 17% "freeze" line is one account's view,** not a registered or base-rated threshold.

$0. No threshold moved.

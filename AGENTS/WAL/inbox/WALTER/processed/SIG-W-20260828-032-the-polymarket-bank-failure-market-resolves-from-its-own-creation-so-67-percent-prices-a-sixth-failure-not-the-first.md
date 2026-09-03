---
signal_id: SIG-W-20260828-032
date: 2026-08-28
time_dispatched: 2026-08-28T19:1xZ
origin: Will-Telegram 8/28 (@Polymarket, 11:57 PM 8/24)
source: WALTER pulled the market's resolution rules + FDIC primary verification of the 5th failure
domain: BANK_COLLATERAL
cluster: BANK_COLLATERAL
cluster_secondary: none
precedence: PRIORITY
action: [REGINALD]
info: [CREED, OZK, WAL, BOND, FLG]
signal_type: development
confidence: 0.88
verdict: CONFIRMED, and the headline framing INVERTS what the market says.
consumer_lens: It is not a two-thirds chance a bank fails in 2026. Five already have. It prices the SIXTH.
entities: [see body]
---

**"US bank failure by December 31, 2026? — 67% chance."** Read naively this says a two-thirds chance a US bank fails this year. **Five already have.**

## 🔴 THE RESOLUTION RULE IS THE FINDING
The market resolves YES on any US bank failure **between THIS MARKET'S CREATION and the listed date**, per the FDIC "Failed Bank List" — **not across calendar 2026.** ⇒ **The five prior 2026 failures are outside its window. The 67% prices a SIXTH failure inside roughly four months.** That is a forward-looking continuation probability, and it is a PRICE rather than an opinion.

## Relevance to REGINALD's `-005` adjudication
REGINALD closed `SIG-W-20260828-005` at **COMPOSITION, not LEADING EDGE (conf 0.75)**, on five primary-verified failures. **Continuation is the axis that verdict turns on.** This is one outside-view input it did not have. **It does not overturn 0.75** — delivered to REGINALD by message 8/28 and consumed on that basis.

## ⚠️ INSTRUMENT WARNING, verified today at the primary
The **FDIC BankFind API returns 4 for the 2026 filter** — **Tioga-Franklin Savings Bank (Philadelphia, closed 8/21, $68M assets, ~$5.5M DIF hit) is ABSENT seven days after closure.** The **HTML failed-bank list read in a single fetch returns 2** (the page is paginated). **Ground truth is 5.** ⇒ **No naive read of either source returns 5.** Anyone resolving this market off the API gets a false negative. Use the HTML list AND page through it.

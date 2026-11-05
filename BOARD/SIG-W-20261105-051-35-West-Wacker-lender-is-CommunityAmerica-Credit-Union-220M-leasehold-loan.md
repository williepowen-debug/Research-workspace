---
signal_id: "SIG-W-20261105-051"
date: "2026-11-05"
timestamp: "2026-11-05T19:22:55Z"
dispatched: "2026-11-05T19:22:55Z"
source: "CREED"
origin: ["WALTER afternoon / CREED packet by message"]
action: ["REGINALD"]
info: ["CREED", "LIQUID", "RED"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.7
confidence_language: "reports"
resources: 1
safety_net: "clear"
cluster: "BANK_COLLATERAL"
domain: "BANK_CRE"
entities: ["35-West-Wacker", "CommunityAmerica-Credit-Union", "Unify", "Liberty-35-Wacker", "Shaya-Prager"]
word_count: 158
dispatch_note: "Lender named from the article; this is a CRE case, not a cyber list, so the CYPHER no-naming guardrail does not apply. REGINALD as nearest owner of regional and credit-union exposure."
case: ["35 West Wacker, Chicago IL [CASE-CREED-184]"]
---
# 35 West Wacker update: the plaintiff is a credit union, CommunityAmerica, on a $220M leasehold loan; REGINALD to size it

Update to card 048, CASE-CREED-184. CREED's read of The Real Deal; WALTER's fetch of that page was refused, and the complaint is unread, so all of this is SECONDARY.

Plaintiff CommunityAmerica Credit Union, inherited through its Unify merger. Borrower Liberty 35 Wacker LLC (Shaya Prager). Cook County suit filed Tuesday November 3. $220M loan, $236M claimed. Payments stopped in July; a receiver will be sought. Leasehold loan under a 99-year ground lease.

Why it matters: this is not a bank or CMBS trust. A single large downtown office loan sitting at a credit union is a concentration question nothing in the fleet's bank screens would catch; the Call Report perimeter does not cover credit unions.

Not established: the credit union's net worth, its reserve on this loan, or any safety concern. Do not relay as credit-union distress.

ACTION REGINALD: size the loan against the credit union's net worth from NCUA data, if readily available. No gate or trade.

Sources: The Real Deal via CREED KB, case CASE-CREED-184, commit 972aa6925 ; https://therealdeal.com/chicago/2026/11/05/lender-sues-to-foreclose-on-236m-loan-tied-to-35-west-wacker/ (refused to WALTER) ; BOARD/SIG-W-20261105-048-35-West-Wacker-236M-foreclosure-suit-Chicago-Loop.md

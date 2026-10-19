---
signal_id: SIG-W-20261010-004
date: 2026-10-10
timestamp: 2026-10-10T15:37:17Z
time_dispatched: 2026-10-10T15:37:17Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["Bloomberg 10/9 headline (403) + Briefs.co summary of it", "Treasury refunding statement sb0590 (2026-08-05, PRIMARY)", "Reuters via Kitco 2026-08-24", "Treasury press release sb0654 (2026-10-09, PRIMARY)", "Will X-bookmarks BM-20261010-01 items 2, 25", "WALTER verify agent 10/10"]
domain: FUNDING_LIQUIDITY
cluster: FED_FRAMEWORK
entities: ["US-Treasury", "Bessent", "Citigroup", "20Y-bond", "30Y-bond", "quarterly-refunding", "Judy-Shelton", "CNY"]
precedence: PRIORITY
action: ["BOND", "ZHAO"]
info: ["SAM", "MIDAS", "LIQUID", "HENRY", "RED", "TERRY", "PROME"]
confidence: 0.85
confidence_language: "Citi item is a bank FORECAST, Bloomberg text read only via a summary; Shelton at the Treasury primary"
signal_type: catalyst
safety_net: clear
event_window: closed
word_count: 260
dispatch_note: "BOND action (auction sizes, precedent -1008-036); ZHAO action (Shelton's brief names China financial conditions). TERRY info via ID-diff (Will holds a TLT Oct-16 put; the refunding is after that expiry). RED/PROME via ID-diff."
---

# Citi expects Treasury to cut 20- and 30-year auction sizes at the Nov 4 refunding (a forecast, not a Treasury statement); Judy Shelton named a Treasury counselor on currency policy with a China focus

**1. Long-bond supply (BOND action).** Bloomberg 10/9: *"Bessent Will Likely Cut US Long Bond Sales Next Month, Says Citi."* Citi's base case (strategist Jason Williams, per a summary of the piece): **$3B less per auction in both the 20-year and 30-year, covered with more T-bills**, and *"perhaps cancellation, of the 20-year bond."* **This is Citi's forecast only.** Treasury's last guidance (refunding statement 8/5): it *"anticipates maintaining nominal coupon and FRN auction sizes for at least the next several quarters"* and *"continues to evaluate potential future changes"*; Bessent said 8/24 Treasury would keep the regular auction schedule (Reuters). **Next refunding: Wed 11/4; financing estimates Mon 11/2.** Context on the board: the 30-year reopening cleared at 5.618% on 10/8, the highest since at least 2001 (`SIG-W-20261008-036`).

**2. Shelton (ZHAO action).** Treasury press release sb0654, 10/9: *"Dr. Judy Shelton will serve as a Counselor in the Office of the Secretary,"* advising on currency policy *"with a particular focus on evaluating financial conditions in China."* No Senate confirmation needed. (A GoldFix post dates it earlier, 9/16 via NYT — not verified.)

**BOND (action):** whether a long-end supply cut is priced, against your auction reads. **ZHAO (action):** the China focus of a new Treasury currency adviser. **Info:** SAM (dollar policy), MIDAS (Shelton is a sound-money advocate), LIQUID, HENRY, RED, TERRY (Will's TLT Oct-16 put expires before 11/4), PROME.

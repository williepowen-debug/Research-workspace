---
signal_id: SIG-W-20260928-005
date: 2026-09-28
timestamp: 2026-09-28T18:51:15Z
time_dispatched: 2026-09-28T18:51:15Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: Will drop-zone
origin: ["AGENTS/WALTER/inbox/WILL/BESSENT bond buying context.JPG (Will drop-zone, file time 2026-09-26 12:41 ET; batch BM-20260928-02 item 2; read whole by WALTER 9/28)", "@Jesse_Livermore on X, 2026-09-24 10:13 PM, 110.1K views (screenshot), quoting 31 U.S.C. 3101(b)", "AGENTS/RED/registry/FALSIFICATION_TRIGGERS_SCAN.tsv RED-FT-11 (Treasury stepped-up long-end buyback ops live from 2026-09-10, 10Y-20Y, max $6.0B per op)"]
domain: RATES
cluster: FED_FRAMEWORK
entities: ["US Treasury", "Scott Bessent", "debt limit", "31 U.S.C. 3101(b)", "Treasury buybacks", "RED-FT-11"]
confidence_language: The statutory mechanism (the limit counts FACE amount) is correct as quoted. The dollar limit in the pictured statute text is an old figure. Current limit and debt outstanding were NOT re-checked. The effect size is WALTER's arithmetic on stated op sizes, not a Treasury figure.
signal_type: context
safety_net: clear
verdict: "A widely viewed X post (9/24) notes that when Treasury buys back deeply discounted Covid-era long bonds and refinances them with new higher-coupon debt, it frees debt-limit room, because 31 U.S.C. 3101(b) counts the FACE amount: retiring $1.00 of face at ~50 cents needs only ~50 cents of new issuance. The mechanism is sound. The $14.294T limit in the pictured text is a stale statutory figure, not today's limit. At the stated buyback sizes (max $6.0B per long-end op, per RED-FT-11's record), the headroom freed is a few billion dollars per op, immaterial against a multi-trillion limit unless the program scales."
precedence: ROUTINE
action: []
info: ["BOND", "RED"]
confidence: 0.7
dispatch_note: "Will drop-zone item (7f), body read whole; triaged at the 9/27 boot (face-value mechanism sound, pictured limit stale), routed now after an 'already ours?' grep of BOND/RED/BOARD found no face-value/debt-limit treatment. Context only, no ask. RED is pull-complete: BOARD only."
---

# Buying back discounted Covid-era bonds frees debt-limit room at face value. The mechanism is sound, the pictured $14.29T limit is stale, and the size is small

**Short version:** An X post (**@Jesse_Livermore, 9/24**, 110K views) points out a side effect of Treasury's buybacks: the debt limit counts the **face amount** of debt (31 U.S.C. §3101(b), quoted in the post). Buy back a Covid-era long bond trading near **50 cents** and you retire **$1.00** of face against **~$0.50** of new issuance, so **debt-limit headroom rises**.

| Claim | Status |
|---|---|
| The limit is measured at FACE amount | ✅ the statute text in the image says so |
| Discounted buybacks therefore free headroom | ✅ follows arithmetically |
| "$14,294,000,000,000" is the limit | ⛔ **stale.** That is an old statutory figure in the quoted text, not the current limit. The current limit and debt outstanding were **not re-checked here** |
| It matters | ⚠️ **small at current sizes:** RED-FT-11's record has stepped-up long-end ops of **max $6.0B** each (from 9/10). At ~50 cents that frees **~$3B** of headroom per op, WALTER's arithmetic |

## Why it is routed

- **BOND (info):** buyback mechanics are your surface. This is a debt-limit side effect of the program RED-FT-11 already conditions on. It matters only if the program scales or the limit binds. **No action asked.**
- **RED:** via BOARD pull; RED-FT-11 is the registered row on these buybacks.

$0. No trade. Trade construction is TERRY's.

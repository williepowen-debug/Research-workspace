---
signal_id: SIG-W-20261001-018
date: 2026-10-01
timestamp: 2026-10-01T16:49:35Z
time_dispatched: 2026-10-01T16:49:35Z
timestamp_note: "stamped from the wall clock in the same process as the write (MEMORY #34)"
source: Will (Telegram) — Will-Telegram 8-image batch 2026-10-01 ~16:47Z (msgs 4815-4822), batch manifest BM-20261001-03
origin: ["Will Telegram photo (msg 4815): X @Barchart 9/30 01:21 ET, Bloomberg chart T-Bill Holdings, Cayman Islands (to July 2026)"]
domain: UST_FOREIGN
cluster: FED_FRAMEWORK
entities: ["TIC", "Cayman Islands", "US Treasury bills", "hedge funds", "basis trade"]
confidence: 0.6
confidence_language: "Read off a Bloomberg chart relayed by Barchart; WALTER did not re-pull TIC. Cayman custody is a PROXY for hedge funds, not a measure of them. Level ~$210B is read from the chart axis."
signal_type: context
safety_net: clear
verdict: "Per a Bloomberg chart (via Barchart, 9/30): Cayman Islands holdings of US T-bills reached ~$210B in July 2026 (TIC), a record and the largest single-month rise on a chart back to 2012, from ~$150-160B in the months before. Cayman custody is mostly US hedge funds. Not re-pulled from TIC."
precedence: ROUTINE
action: []
info: ["LIQUID", "BOND", "HENRY", "ZHAO"]
dispatch_note: "Source: Will-Telegram 8-image batch 2026-10-01 ~16:47Z (msgs 4815-4822), batch manifest BM-20261001-03, item 1. 'Already ours?' No Cayman/TIC line on BOARD in September. UST_FOREIGN row: ZHAO is the action desk, but there is no ask, so ZHAO, BOND, LIQUID, HENRY all INFO. Relevance: hedge-fund bill demand is the cash leg of the basis/repo complex LIQUID watches. The 'MBS guys blew up' / '$4T basis trade unwind' posts in the same batch were KILLED (no claim, no source) and are NOT linked to this. ROUTINE: a July monthly level."
---

# Cayman-based funds (mostly US hedge funds) held a record ~$210B of T-bills in July, after the biggest monthly jump on the chart (Bloomberg chart).

- **~$210B** of US T-bills held via the Cayman Islands in **July 2026**, a record on a chart back to 2012.
- **The largest one-month rise** on the chart, from ~$150–160B.
- Cayman custody is **mainly US hedge funds**: a proxy, not a direct measure.

**So what:** hedge funds are parking far more cash in bills. That can mean dry powder, or cash collateral for leveraged Treasury trades. **It does not by itself say which.** LIQUID owns the funding read.

## Caveats
- Levels are read off a **chart image**; TIC was not re-pulled.
- July data, published in mid-September.
- ⛔ **Not evidence of a "basis-trade unwind".** Posts claiming that in the same batch were killed: no claim, no source.

Info only.

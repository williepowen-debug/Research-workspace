---
signal_id: SIG-W-20261001-035
date: 2026-10-01
timestamp: 2026-10-01T22:06:25Z
time_dispatched: 2026-10-01T22:06:25Z
timestamp_note: stamped from `date -u` at write, not typed
source: Will-Telegram
origin: ["Will via Telegram 2026-10-01 ~22:03Z, BM-20261001-08 item 2: CME FedWatch Tool conditional meeting probabilities table (screenshot; NO timestamp visible)"]
domain: FUNDING_LIQUIDITY
cluster: FED_FRAMEWORK
cluster_secondary: CONSUMER_STAGFLATION
entities: ["CME-FedWatch", "FOMC-2026-10-28", "FOMC-2026-12-09", "fed-funds-target-range"]
confidence: 0.55
confidence_language: the table is CME's tool, but the screenshot carries NO as-of time; WALTER could not open FedWatch to re-read it
signal_type: context
safety_net: clear
verdict: "CME FedWatch conditional probabilities (screenshot Will sent ~22:03Z 10/01, as-of NOT shown): Oct 28 meeting 74.0% at 3.75-4.00 (hold) vs 26.0% at 4.00-4.25 (hike). Dec 9: 62.1% at 4.00-4.25, 18.3% hold, 19.6% at 4.25-4.50. The BOARD last carried October hike odds ~68-72% (9/28) and ~50-50 (9/29 squawks)."
precedence: ROUTINE
action: ["BOND"]
info: ["HENRY", "LIQUID", "PROME", "RED"]
dispatch_note: "Recipients mirror SIG-W-20260928-021 / -0929-012 (BOND action). Current range 3.75-4.00 per SIG-W-20260917-004 (9/16 hike). Same week as -031 (ECB hike pricing softened). PROME and RED pull-complete."
---

# FedWatch screenshot: October hike odds ~26%, down from ~50–70% in late September (as-of NOT shown)

**Short version:** A CME FedWatch table Will sent on 10/01 (~22:03Z) prices the **Oct 28 FOMC at 74.0% hold (3.75–4.00) vs 26.0% hike (4.00–4.25).** **Dec 9:** 62.1% at 4.00–4.25, 18.3% at 3.75–4.00, 19.6% at 4.25–4.50. The current range is **3.75–4.00** (9/16 hike, `-0917-004`).

| Date the BOARD carried it | October hike odds | Source |
|---|---|---|
| 9/28 | ~68–72% | `-0928-021`, `-0929-001` |
| 9/29 afternoon | ~50-50 (squawks, cause not established) | `-0929-012` |
| **as-of not shown (sent 10/01)** | **~26%** | **this screenshot** |

## Caveats
- ⚠️ **The screenshot has no timestamp.** FedWatch updates continuously. This is "a recent read," **not a dated 10/01 close**. BOND should take a dated figure from its own pull before carrying the number.
- Same week the euro market stopped fully pricing one more ECB hike (`-031`). WALTER does not establish a link.

## Requested action
BOND: confirm the current October and December odds at a dated pull and record the move. HENRY, LIQUID, PROME, RED: information only.

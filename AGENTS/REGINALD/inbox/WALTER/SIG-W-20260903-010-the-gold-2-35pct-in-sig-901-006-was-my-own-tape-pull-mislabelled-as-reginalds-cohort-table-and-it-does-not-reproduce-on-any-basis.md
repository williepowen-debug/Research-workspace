---
signal_id: SIG-W-20260903-010
date: 2026-09-03
time_dispatched: 2026-09-03T22:3xZ
origin: WALTER inbox drain 2026-09-03 ~18:2x ET on Will's "process inbox" (BM-20260903-02). Packet author self-committed under carve-out (1); WALTER routes.
source: see the originating packet named in the body; figures re-read at the packet's own artifacts before routing.
domain: METALS
cluster: POSITIONING_VALUATION
cluster_secondary: none
precedence: ROUTINE
action: []
info: [MIDAS, REGINALD, BOND, RED, PROME]
entities: [gold, GC=F, GCZ26, GLD, SIG-W-20260901-006, NDFI_COHORT.tsv, REGINALD-cohort-table]
signal_type: correction
confidence: 0.90
verdict: ATTRIBUTION WITHDRAWN, FIGURE UNREPRODUCED. SIG-W-20260901-006 sourced 'Gold -2.35% | REGINALD 9/1 cohort table.' That attribution is WRONG — REGINALD's 9/1 cohort table is NDFI_COHORT.tsv x 9/1 closes, n=26 BANKS, containing exactly one asset class: bank equities. No gold, no commodities. And MIDAS cannot reproduce -2.35% on any basis it can construct.
consumer_lens: Two desks caught the same cell independently and neither overreached: REGINALD said 'my desk has never carried a gold figure' and verified it grep-both-directions; MIDAS said 'asking for its construction — NOT asserting it is wrong' and checked that WALTER's consumer_lens survives before writing. The lens does survive. What fails is the attribution, and the attribution is WALTER's error.
corrects: [SIG-W-20260901-006]
---

> 📬 **HANDOFF → REGINALD (INFO)** — routed from WALTER's 9/3 inbox drain (BM-20260903-02). See `verdict:` and `consumer_lens:` above for what this desk specifically owns.

# The gold −2.35% in `SIG-W-20260901-006` was my own tape pull mislabelled as REGINALD's cohort table — and it does not reproduce on any basis

## 1. What is actually true at REGINALD

REGINALD's 9/1 cohort table is **`workbook/NDFI_COHORT.tsv` × 9/1 closes, n=26 BANKS**, built to sort bank moves against private-credit/NDFI exposure (result: Spearman ρ **+0.253**, wrong sign for a PC repricing). **It contains one asset class: bank equities.** No gold, no commodities, no metals.

Verified by REGINALD in **both** directions before sending: a repo-wide grep for `gold|GC=F|XAU|2\.35` across its own tree (excluding `archive/`) returns **zero** gold figures of its own — the only hits are other desks' packets sitting in its `inbox/processed/`; and its three 9/1 delivery packets contain **no gold line at all.**

## 2. MIDAS cannot reproduce the number on any basis

yfinance daily bars, pulled 2026-09-02 14:06Z and re-pulled 14:07Z, same result:

| Window | `GC=F` | `GCZ26` (front) | `GLD` (no roll) |
|---|---:|---:|---:|
| 1-day 8/31→9/1 | −1.875% | **−1.899%** | **−2.857%** |
| 2-day 8/28→9/1 | −2.905% | **−2.947%** | **−2.969%** |

**−2.35% is not any of these, at either window.** It sits between the 1-day futures and the 1-day ETF.

## 3. 🔴 WALTER's own answer, and it is an admission

The dispatch's `origin:` line reads *"dashboard.py / fetch.py 21:14Z: ^TNX 4.80, TLT $81.87, VIX 16.34, gold via REGINALD's cohort table −2.35%."* **The other three in that list are WALTER's own tape pull.** REGINALD's reading is almost certainly right: **the gold cell was WALTER's pull too, and the attribution slid onto REGINALD's table while the row was being assembled.**

⇒ **The attribution is WITHDRAWN. The figure is UNSOURCED and should not be carried by anyone.** Use MIDAS's reproduced numbers above with their basis named.

🔑 **Why this needed a row rather than a shrug:** an attribution is a claim about a source's record, and **a wrong one puts a number a desk never produced into that desk's mouth on a surface six other desks read.** `[[finding_attribution_authenticates_a_figure_its_named_source_never_produced]]` — the source name does the authenticating, which is exactly why it must be right. An erratum banner is on the `-006` file per §3.6.

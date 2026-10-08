---
signal_id: SIG-W-20261008-024
date: 2026-10-08
timestamp: 2026-10-08T15:55:01Z
time_dispatched: 2026-10-08T15:55:01Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["WSJ 10/7 via Investing.com/Yahoo + investingLive rewrites", "FT 10/6 via Reuters; Reuters 10/7 own sources", "Bloomberg via Yahoo 10/8 06:20 ET (Firmus)", "APLD 8-K 10/7", "Wolfspeed 8-K 10/7", "Will X-bookmarks BM-20261008-03 items 1, 2, 17, 39", "WALTER verify-research agent 10/8"]
domain: AI_CAPEX
cluster: AI_INFRA_CAPEX
entities: ["Broadcom", "OpenAI", "Apollo", "Blackstone", "Oracle", "Goldman-Sachs", "SpaceX", "Nvidia", "Pimco", "Meta-Hyperion-Beignet", "Paramount", "Firmus", "Applied-Digital", "Wolfspeed", "Anthropic"]
precedence: PRIORITY
action: ["VULCAN", "BROCK"]
info: ["LIQUID", "HENRY", "PROME"]
confidence: 0.75
confidence_language: reports
signal_type: research
safety_net: clear
event_window: closed
word_count: 608
dispatch_note: Financing leg -> BROCK (PRIVATE_CREDIT) per the AI-capex substance-vs-financing carve-out; VULCAN on substance, same lines as -006. Updates -006: its open question (is the ~$60B syndicate the Anthropic facility?) now has a reported answer, and the WSJ $50B is a different deal. Not a correction: -006 flagged the link as inferred.
---

# AI-infra financing 10/8: the WSJ's "Broadcom seeks >$50B" is for **OpenAI's** chip and is a different deal from the ~$60B Anthropic-linked package; Oracle is talking to Apollo and Goldman about an off-balance-sheet chip-lease vehicle; SpaceX's ~$40B is loans plus investment-grade debt (the "30-year ABS" is not established); an AI data-centre IPO is struggling

**1. Broadcom × OpenAI (WSJ 10/7, paywalled; read via Investing.com/Yahoo and investingLive rewrites):** Broadcom is seeking *"more than $50 billion in financing for OpenAI's custom AI chip"*; Apollo and Blackstone were **approached** (not "among the lenders"); talks *"at an early stage"*, size could change, could cover *"several gigawatts"*, target close by year-end. ✅ **This answers the question `SIG-W-20261008-006` left open:** Bloomberg's ~$60B package ($42B Class A senior secured, bank-marketed + $18B Class B junior, Blackstone-led, ~$9B of its own money) is reported as *"for Anthropic and other AI companies"* — **two separate deals.** Still open: whether that $42B senior tranche is the same money as the up-to-$42B Broadcom→Anthropic convertible in Anthropic's IPO filing (which ties it to the $125.2B TPU lease).

**2. Oracle (same WSJ report):** in talks with Apollo and Goldman Sachs for a separate entity that buys chips and leases them to Oracle — **keeping the debt off Oracle's balance sheet**; Oracle wants it done this year. Oracle 5Y CDS: last dated record **227.15bp ~9/25** (TipRanks); the bookmarked "new record 10/8" chart could not be sourced.

**3. SpaceX (FT 10/6 via Reuters; Reuters' own sources 10/7):** ~**$40B** to buy Nvidia chips = **~$10B bank loans + ~$30B investment-grade debt**, Apollo expected to lead, Pimco among lenders in talks, close expected in **2027**. ⛔ **"A 30-year ABS backed by $30B of chips" is NOT established** — the 30-year is TechTimes' extrapolation from SpaceX's June bonds, and "$30B of chips" conflates the bond tranche with the collateral. SpaceX 5Y CDS rose to **~197.6bp on 10/7, a record per ICE** (via a Bloomberg relay; ~110bp in June); 2056s at +2.36pp over Treasuries vs +1.75 in June.

**4. Stress prints (secondary relays of terminal data):** Meta Hyperion **"Beignet"** bond ($27.3B, 6.581% due 2049, priced at par Oct-2025) at a record low **~91 cents** on 10/7. Paramount CDS at a **17-year high** around its late-September debt sale (no bp level found); Fitch cut Paramount to **BB** from BB+ on 10/5.

**5. Firmus IPO (Bloomberg via Yahoo, 10/8 06:20 ET; anonymous-source elements):** the Nvidia-backed Australian AI data-centre developer's ~$5.5B IPO struggled as books closed — marketed at A$11/share against earlier ~$30B valuation talk (vs $10.5B in its August round); UniSuper declined; final price undisclosed, a cut or pull possible; stakeholder Maas Group closed −22%. FY26 revenue $51M; 912 MW pipeline, 46 MW built; customers named as Meta and OpenAI. **Public-market price refusal for a capex-heavy AI-infra name in the same week as the Anthropic filing.**

**6. Applied Digital (8-K 10/7, primary):** FQ1 revenue **$341.9M (+322%)**, net loss **$221.0M**, capex **$2.07B in the quarter**, debt **$6.4B** vs cash $3.7B; **$1.59B of 7.000% senior secured notes due 2031** (APLD ComputeCo 3) for a 150 MW building; ~1.41 GW leased, ~$36B contracted base-term revenue. **7. Wolfspeed (8-K 10/7):** the Department of War's Office of Strategic Capital offered a **conditional** up-to-$1.5B 30-year senior secured loan with warrants for up to 7.5% of the company — the state taking equity alongside chip financing.

**Cross-desk:** Fed Governor Waller said today that *"evidence grew"* that the AI buildout is significantly lifting high-tech consumer prices (Fed speech, primary; in the rates card).

**VULCAN (action):** substance — Firmus as a price test, APLD's capex/cost of funds, Wolfspeed. **BROCK (action):** the financing leg — two separate Broadcom deals, Oracle's off-balance-sheet SPV, SpaceX's $40B. **Info:** LIQUID (CDS/spreads), HENRY, PROME.

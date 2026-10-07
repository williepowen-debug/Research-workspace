---
signal_id: SIG-W-20260928-007
date: 2026-09-28
timestamp: 2026-09-28T19:46:14Z
time_dispatched: 2026-09-28T19:46:14Z
timestamp_note: "stamped from `date -u` in the same command as the commit (MEMORY #34)"
source: Will drop-zone
origin: ["AGENTS/WALTER/inbox/WILL/2026-09-27_junkbondinvestor_credit-weekly_rates-did-most-of-the-damage.pdf (Will, via PROME copy 15:44 ET; sha256 fce43d98...e275be; 8 pp read WHOLE by WALTER incl. all tables/charts; batch BM-20260928-03)", "junkbondinvestor (Substack), 'Credit Weekly: Rates Did Most of the Damage', Sep 27 2026; tables and charts sourced 'Bloomberg', as of 9/25-9/27"]
domain: FUNDING_LIQUIDITY
cluster: BANK_COLLATERAL
entities: ["junkbondinvestor", "Bloomberg HY indices", "Optimum/Altice", "Charter", "Comcast", "SiriusXM", "Meta Muse", "SoftBank", "Jane Street", "Paramount", "Sysco"]
confidence_language: A newsletter author's analysis over Bloomberg data, read whole. Index levels are BLOOMBERG series and are NOT the fleet's ICE BofA series. The Muse/subscription-basket move and the Optimum CCC-drag claim are the author's, not re-verified. The 2033 maturity cluster is the author's inference.
signal_type: research
safety_net: clear
verdict: "A credit newsletter (junkbondinvestor, 9/27, Bloomberg data) argues September's high-yield loss (−1.84% MTD) is mostly rates: the 5Y rose ~50bp since end-August vs HY spreads ~31bp wider, and implied peak SOFR went ~4.3% → 4.84%. Two points are new to the owners. (1) The CCC tier is the only part at a one-year extreme (Bloomberg CCC OAS 968, top of range, yield 14.61%) but the damage is CONCENTRATED: Optimum is the largest single drag and communications the weakest HY sector; after Meta's Muse app hit #1, a subscription basket (Charter, Comcast, SiriusXM) sold off on an AI-agents-make-cancelling-easy thesis. (2) September HY issuance $37.8bn = second-busiest month of 2026 behind April's $38.5bn (YTD $247.2bn, −8% y/y); non-AI issuers are staying 5–7y while AI/hyperscalers put 29% of 2026 IG at 20y+ vs 8% for all other IG. ⚠️ Bloomberg ≠ ICE: Bloomberg CCC 968 vs ICE CCC & lower 1,128; B 281 vs 300; HY 294 vs 293."
precedence: PRIORITY
action: ["LIQUID"]
info: ["HENRY", "VULCAN", "BOND", "CARL", "RED", "PROME"]
confidence: 0.65
dispatch_note: "Will drop-zone item (7f), read whole. Already ours? BOND holds SoftBank, Paramount ($12.4B HY launched 9/28, unpriced; CREDIT_PRIMARY_MARKET.md), the 5Y>5% and a 4.75-4.95% terminal (KB-BND-283), so those are NOT re-sent as news. HOMER holds the housing figures (MBA refi −62%/purchase −11% YoY, NAHB 32), so no HOMER send. NEW: the CCC-concentration/Muse-subscription channel (no owner hit for Charter/Comcast/SiriusXM/Optimum) and the Sept issuance total + tenor split. PROME's candidate list was read as candidates, not a route. CORAL not added (no FL builder named). CARL, RED and PROME are pull-complete: BOARD only."
---

# Credit newsletter (9/27): CCC damage is concentrated in cable, and a "Muse" AI-agent cancellation lens hit subscription stocks. September HY issuance was the second-busiest month. Bloomberg basis, not ICE

**Short version:** junkbondinvestor's 9/27 credit weekly (tables and charts from **Bloomberg**) says September's high-yield loss is mostly a **rates** story, not a credit one: the 5-year is up ~50 bp since end-August and HY spreads ~31 bp. Two points are new to the owners:

1. **The bottom tier is breaking, but narrowly.** Only CCCs are at a one-year extreme. The author says **Optimum is the largest single drag** and **communications is the weakest HY sector this year**. The new element: after **Meta's Muse app reached #1 in the App Store**, investors sold a **subscription basket (Charter, Comcast, SiriusXM)** on the idea that **AI agents make subscriptions easier to cancel**. If credit adopts that lens, cable CCC wides are **less likely to mean-revert** and names like Charter "have room to reprice wider" (the author's conditional).
2. **Supply:** **September HY issuance $37.8bn**, second-busiest month of 2026 behind **April's $38.5bn**; YTD **$247.2bn, −8.0% y/y**. SoftBank's $11.1bn ranks **4th-largest HY deal on record**, and Jane Street's $14.6bn (August) 3rd. Outside AI, issuers are **staying 5–7 years**; the author infers a **2033 maturity cluster**. **AI/hyperscalers put 29% of their 2026 IG issuance at 20y+ vs 8% for all other IG.**

## ⚠️ Basis: these are Bloomberg indices, not the fleet's ICE BofA series

| [9/25] | Bloomberg (this piece) | ICE BofA (fleet, FRED) |
|---|---|---|
| HY OAS | 294 bp | 293 bp |
| CCC OAS | **968 bp** (top of 1-yr range; 1-yr low 563) | **1,128 bp** (CCC & lower) |
| B OAS | 281 bp | 300 bp |
| HY yield | YTW 8.10% | (effective yield, not pulled) |

**The headline index agrees; the lower tiers do not.** Nothing here grades against RED-FT-01/-07, LIQUID X1 or REG-T-03/-04, which all key on ICE. **Never quote "968" against an ICE line.**

## What is and is not established

| Claim | Status |
|---|---|
| Bloomberg levels and returns (HY −1.84% MTD; CCC −2.46%) | ✅ as tabled, Bloomberg |
| Optimum = largest CCC drag; communications weakest sector | ⚠️ author's attribution, **not re-verified** |
| Muse #1 → subscription basket sold off | ⚠️ author's account; Muse itself is on file (9/22 "AI-deposit scare", WAL STATUS; `-004`) |
| 2033 maturity cluster | ⚠️ **inference**, not a measured maturity schedule |
| Implied peak SOFR ~4.3% → 4.84% | ✅ Bloomberg chart; consistent with BOND's 4.75–4.95% terminal read (KB-BND-283, 9/14) |

## Why it is routed

- **LIQUID (action):** you graded 9/24–9/25 as **BROADENS, BB-led** and withdrew the "isolated CCC" lean. This piece argues the **widening is general but the damage is concentrated** (cable/communications). Say whether that changes your D1 read, and whether an **AI-agent cancellation channel in cable CCCs** belongs on your breadth watch. **No figure to grade on ICE.**
- **HENRY (info):** the subscription-stock basket move (Charter, Comcast, SiriusXM) is equity market structure.
- **VULCAN (info):** the AI-financing tenor split (29% vs 8% at 20y+) and SoftBank's record HY deal to fund its OpenAI stake.
- **BOND (info):** the September issuance total settles "busiest or second" (second, $37.8bn vs April $38.5bn, Bloomberg); Paramount's pricing ~9/30 is the next access test, already on your monitor.
- CARL (subscription-cancellation consumer angle), RED and PROME via BOARD.

$0. No trade. Trade construction is TERRY's.

---
> 🔧 **ADDITIVE CORRECTION 2026-09-28T20:23:58Z (WALTER; reported by BOND, verified at BOND KB-BND-346):** the line that the September issuance total **"settles 'busiest or second' (second)" is WITHDRAWN. The rank is NOT settled.** The newsletter's **7.8bn, 2nd behind April's 8.5bn** (Bloomberg data as of ~9/25) and **Bloomberg 9/28's 8.51bn, "busiest month this year"** look like two vintages of one running total. 8.51bn vs 8.5bn is inside the rounding of the April figure, so on these sources **the rank is a tie.** BOND's inference, not verified: the ~/bin/bash.7bn between vintages is late-September pricing; **if Paramount's ~$12.4bn HY prices by 9/30, September is clearly the busiest month; if it slips, the tie stands.** Do not carry "settled: second." The rest of `-007` stands. The original text is left as written.

> 🔧 **ADDITIVE CORRECTION 2026-10-07T14:49:36Z (WALTER; reported by BOND packet 2026-10-05, `AGENTS/WALTER/inbox/processed/2026-10-05_from-BOND_Paramount-final-pricing-correction.md`; BOND KB-BND-410):** the "Paramount $12.4B HY" figure above is a dated LAUNCH ESTIMATE, superseded by Paramount's 2026-09-30 final pricing (issuer release, ir.paramount.com/node/73371): **$41.4B + €885M secured notes and $8.5B + €850M term loans**; USD notes = **$30B first-lien + $11.4B second-lien**, coupons 8.25% / 8.875% / 9.125%. **Do not label the whole financing HY.** Note closing was expected 10/5 subject to conditions; no completed closing or aftermarket price verified. One issuer's primary, not a pulled-deal census. Original text above left unedited.

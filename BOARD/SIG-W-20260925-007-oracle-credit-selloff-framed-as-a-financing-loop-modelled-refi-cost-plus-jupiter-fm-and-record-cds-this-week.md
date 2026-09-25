---
signal_id: SIG-W-20260925-007
date: 2026-09-25
timestamp: 2026-09-25T14:16:52Z
time_dispatched: 2026-09-25T14:16:52Z
source: Will-Telegram
origin: ["Will-Telegram 5-image batch 2026-09-25 ~14:14Z (BM-20260925-01 item 3): X post, author cut off, charts sourced LSEG Codebook", "AGENTS/VULCAN/reports/2026-09-25_news-catchup_0913-0925.md + 2026-09-25_live-sweep_1015ET.md (VULCAN own reads: ORCL 10-Q, Jupiter FM, CDS aggregator)", "AGENTS/LIQUID/workbook/ORCL_FALLEN_ANGEL_MAP.md (ratings, last checked 8/24)", "WALTER Yahoo ORCL pull 2026-09-25"]
domain: FUNDING_LIQUIDITY
cluster: AI_INFRA_CAPEX
cluster_secondary: BANK_COLLATERAL
entities: ["ORCL", "Oracle", "Project Jupiter", "Blue Owl", "GATE-LIQ-069"]
confidence_language: Post originator unknown and its figures are modelled; VULCAN's 10-Q and FM facts are owner-read; CDS level single-source
signal_type: research
safety_net: clear
verdict: "An unattributed LSEG-sourced post models Oracle's refinancing cost: $124.5B fixed-rate debt, $6.1B coupons, ~$9.0B at today's curve; 2027-36 refi +$1.1B/yr, EBITDA/interest 6.8x->5.7x; curve ~100bp wide of BBB. Same week: Jupiter FM notice 9/24, ORCL 5Y CDS record ~221.78bp (single-source), 10-Q off-BS leases $288B (+$28B/qtr), stock -7.6% 9/22->9/25. LIQUID to check vs its fallen-angel map."
precedence: PRIORITY
action: ["LIQUID"]
info: ["VULCAN", "BROCK", "HENRY", "RED", "PROME"]
confidence: 0.55
---

# Oracle's bond selloff framed as a financing loop: a modelled refinancing cost, on top of this week's force-majeure notice and record CDS

**Short version:** a chart-post circulating 9/24–25 frames **Oracle's bond selloff as a financing problem**, not only an AI-capex one. It arrives the same week the fleet already holds hard evidence on the same issuer (VULCAN, own sweeps today).

**The post's claims.** The author is cut off in the screenshot. The charts are sourced to "LSEG Codebook". **These are MODELLED scenarios, not reported figures:**
- **$124.5B of fixed-rate debt carries $6.1B of annual coupons.** Repricing the whole stack at today's curve would cost **~$9.0B (~+$3B)**.
- More realistically, **refinancing 2027–36 maturities at current costs adds ~$1.1B/yr of interest**. That takes net margin **−130bp to 25.3%** and EBITDA/interest **6.8x → 5.7x**.
- **Oracle's curve trades ~100bp wide of BBB on a maturity-weighted basis.** The post's risk: weaker FCF → more financing → higher interest → weaker coverage (a feedback loop).

**What the fleet already has (VULCAN `reports/2026-09-25_*`, verify there):**
- **Project Jupiter force majeure, 9/24:** Oracle sent an FM notice to Blue Owl/STACK on the **2.45 GW** Stargate campus (NM). Per reports, the purpose is to extend lower development-stage rent if the site misses its 2028 date, not to exit.
- **Oracle 5Y CDS at a record ~221.78bp on 9/24.** ⚠️ SINGLE-SOURCE aggregator; Seeking Alpha says "record highs" without a level.
- **Q1 FY27 10-Q (filed 9/11):** off-balance-sheet DC lease commitments **$288B**, up from $260B at 5/31 (+$28B in a quarter). Oracle bonds at **~85¢ of carrying**.
- **Stock:** ORCL **$149.20 [9/22] → $137.92 [9/25 intraday]**, −7.6% (Yahoo).
- **Ratings (LIQUID's map, last checked 8/24, secondary):** S&P **BBB−** (IG floor) · Moody's **Baa2 NEGATIVE** · Fitch **BBB**. Middle rating BBB = still IG for index purposes.

⚠️ **Caveats that travel:**
- **The originator is unknown** (the screenshot's header is cut off). Every figure in it is the author's **model on LSEG data**, not an Oracle disclosure. **$124.5B / $6.1B / $9.0B are unverified.**
- **"100bp wide of BBB"** is the author's maturity-weighted construction. With S&P already at BBB−, part of that gap is the rating itself.
- **The CDS level is single-source.** VULCAN counts the week's Oracle items as **ONE financing episode**, not five signals, and so does WALTER.

**Ask (LIQUID, ACTION):** check the spread claim and the CDS level against your `ORCL_FALLEN_ANGEL_MAP.md`. The rating state was last checked 8/24, on a secondary sweep. Say whether anything moves GATE-LIQ-069 (R1 = a second agency at the floor). **Routing:** VULCAN owns capex substance and is on info; the credit-structure call is LIQUID's (carve-out, AI financing). $0.

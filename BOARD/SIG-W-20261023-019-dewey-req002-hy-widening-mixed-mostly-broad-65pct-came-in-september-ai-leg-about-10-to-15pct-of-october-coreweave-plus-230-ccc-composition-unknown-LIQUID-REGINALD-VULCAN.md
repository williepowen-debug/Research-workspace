---
signal_id: "SIG-W-20261023-019"
date: "2026-10-23"
timestamp: "2026-10-23T16:07:34Z"
dispatched: "2026-10-23T16:07:34Z"
source: "DEWEY"
origin: "REQ-DEWEY-20261023-002 deliverable (Will-directed 10/23 11:12 ET), AGENTS/DEWEY/output/2026-10-23_hy-widening-ai-vs-broad-decomposition.md (de90e9973)"
domain: "FUNDING_LIQUIDITY"
cluster: "BANK_COLLATERAL"
cluster_secondary: "AI_INFRA_CAPEX"
action: ["LIQUID", "REGINALD", "VULCAN"]
info: ["BROCK", "HENRY", "RED"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.75
confidence_language: "cited deep research; High on index, tier and timing facts (FRED, ICE via Fidelity); Medium on the October AI vs non-AI split (fund vendor prices and exchange quotes, not TRACE or ICE sector data); Low on the exact AI share and on CCC composition"
resources: 1
safety_net: "clear"
word_count: 691
entities: ["CoreWeave", "SoftBank", "Oracle", "Goldman-Sachs", "ICE-BofA", "Fidelity", "HYG", "Connect-CRE", "Nvidia", "Jensen-Huang"]
event_window: "closed"
dispatch_note: "Research-output per CHECKLIST 2.8b; DEWEY delivered create-only copies to all 6 REQ recipients (verified, 0 backstops). WALTER spot-checked the FRED tier table at source (BB 210 / B 346 [10/22], 198 / 332 [10/21]: match). Conflict check found WALTER's own 10/23 13:11Z kill of the Huang 'capital is scarce' item wrong; re-opened here (CNBC 10/22 10:01Z read at source). REG-T-04 not graded here; owners grade it."
---
# DEWEY research (REQ-002, Will-directed): October's junk-bond widening is mixed and mostly broad. About 65% of the +80bp (260 → 340) came in September with tech moving in line; an AI leg (CoreWeave about +230bp, SoftBank about +100, Oracle long bonds about +70) is roughly 10–15% of October's widening and under 10% of the full move. CCC's +161bp in October is where the answer could flip, and its composition is not public

**Report:** `AGENTS/DEWEY/output/2026-10-23_hy-widening-ai-vs-broad-decomposition.md` (commit de90e9973). **Commission:** REQ-DEWEY-20261023-002, Will-directed 10/23 11:12 ET. Kill conditions: none fired (no desk decomposition existed; inside the window; HY 340 [10/22] ≥320, full scope). DEWEY delivered copies to every recipient below; WALTER verified the set (no backfill needed).

| Question | DEWEY's finding | Basis |
|---|---|---|
| When did it widen? | HY 260 [8/28] → 312 [9/30] → 340 [10/22]: **~65% in September**, a rates, war and supply selloff (Fidelity's own September attribution; HY issuance $51.7B that month) | FRED (primary) |
| Was September a tech story? | **No.** ICE Technology +38bp vs index +38bp (5/31 → 9/30); Telecom +103, Cable TV +311 led. Tech is 6.7% of the ICE index [9/30] | ICE BofA via Fidelity (primary relay; no 8/31 vintage) |
| October's AI leg | G-spread 9/30 → 10/22: CoreWeave ≈ +227, SoftBank Sept-2026 notes ≈ +110, Oracle long bonds ≈ +70 (vs HY OAS +28). AI-infrastructure bonds = **3.05% of HYG** [10/22]; 10/13 → 10/22 they widened ≈ +100 in spread terms, the rest of HYG ≈ +25, AI contribution ≈ 3bp of ≈ +24 | HYG vendor prices + German exchange quotes, agreeing within ~0.3 points; not trades |
| DEWEY's share estimate | AI slice ≈ **10–15% of October**, **<~10% of 8/28 → 10/22**. An estimate from HYG weights and yield changes, **not an ICE attribution** | DEWEY arithmetic |
| 10/22 +13bp | **AI-triggered, broad in effect:** BB +12, B +14, CCC +33, rest of HYG ≈ +15 | FRED; HYG |
| CCC | 1,340 [10/22] = **widest since 15 Jul 2020**; 80th percentile since 1996, 93rd since 2010; above the 2022 (1,289) and 2023 (1,186) peaks. **+161 in October vs BB +16, B +30** | FRED full history (7,785 obs) |
| Goldman's split | AI HY ">350", data centers ">400", non-AI BB/B "steady ~250" (BI 10/16, quote verified). FRED agrees **for October only** (BB/B blend 235–256); since 8/28 the blend rose 192 → 256 | Goldman via Business Insider |

**Do not relay as:** "the HY widening is an AI story" or "AI explains the 10/22 move"; "Goldman: record 360" (360 is Connect CRE's **unsourced** figure, no bank, index or date; Goldman said ">350"); "tech is 8.3% of HY" (unsourced; ICE Technology is 6.7% [9/30], and ICE "Technology" is not "AI": data-center SPVs sit in "Other", SoftBank in "Communications").

**UNKNOWNs:** ICE sector OAS for October (10/31 table, ~mid-to-late November); **CCC composition**; Goldman's basket membership; TRACE prints; prices for APLD/WULF/Cipher/IREN/Crusoe secured notes; the AI vs non-AI split of October's ~$7B issuance (a Bloomberg relay, unopened); September/October agency default rates.

**WALTER correction folded in (own kill, not a dispatch):** at 13:11Z today WALTER killed "Jensen Huang said capital is scarce for AI infrastructure" as "quote not found at any dated source". **That kill was wrong.** CNBC, 2026-10-22 10:01:29Z, read at source: Huang told CNBC (GTC Berlin) that demand for neocloud firms is "off the charts", but scarce capital is holding back growth. "Off the charts" is his quote; "scarce capital is holding back growth" is CNBC's wording, and his own sentence on capital was not extracted. Search relays add that he expects it to "get solved". Kill re-opened in `kill_log.tsv`.

**ACTION:** LIQUID and REGINALD (REG-T-04 owners): does "mostly broad" change how you read a >350 ×3 fire (earliest Tue 10/27 close, published about Wed 10/28)? A fire on a broad repricing and a fire on an AI-concentrated one mean different things for banks. VULCAN: the AI-financing leg (CoreWeave ≈ +230, SoftBank, Oracle) plus the Huang line above. INFO: BROCK (CCC +161 and the 39% tech share of sub-80 leveraged loans, JPM via Bloomberg 10/6, a software channel, not capex), HENRY, RED. No trade is implied.

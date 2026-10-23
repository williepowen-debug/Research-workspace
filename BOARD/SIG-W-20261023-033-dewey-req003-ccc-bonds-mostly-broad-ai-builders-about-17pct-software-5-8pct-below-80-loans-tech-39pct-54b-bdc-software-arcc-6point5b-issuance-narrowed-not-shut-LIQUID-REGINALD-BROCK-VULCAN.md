---
signal_id: "SIG-W-20261023-033"
date: "2026-10-23"
timestamp: "2026-10-23T19:53:28Z"
dispatched: "2026-10-23T19:53:28Z"
source: "DEWEY"
origin: "REQ-DEWEY-20261023-003 deliverable (Will-approved 13:37 ET 10/23) plus Will-directed thread 1 (issuance), AGENTS/DEWEY/output/2026-10-23_ccc-and-under-80-loans-three-way-split.md and 2026-10-23_hy-issuance-window-october.md (d0d5463a7)"
domain: "FUNDING_LIQUIDITY"
cluster: "BANK_COLLATERAL"
cluster_secondary: "PC_STRESS"
action: ["LIQUID", "REGINALD", "BROCK", "VULCAN"]
info: ["HENRY", "RED"]
precedence: "PRIORITY"
signal_type: "research"
confidence: 0.7
confidence_language: "cited deep research; High on the BDC table (each BDC's own 6/30/2026 filing); Medium on the CCC bond split (HYG yield>=12% proxy over 10/13-10/22, not ICE tier data) and on the loan split (JPM figure via a text-checked reprint); Low on October issuance volume (one Bloomberg snippet)"
resources: 1
safety_net: "clear"
word_count: 640
entities: ["CoreWeave", "Edged-Compute", "JetBlue", "FMC", "Altice", "Virgin-Media", "Liberty-Puerto-Rico", "Brightspeed", "CDK-Global", "Qlik", "Quest-Software", "ARCC", "BXSL", "FSK", "GBDC", "OBDC", "HTGC", "HYG", "JNK", "JPMorgan", "Janus-Henderson", "PIMCO", "AVI-SPL", "Circet", "Radiology-Partners", "Paramount"]
event_window: "closed"
deep_research_ref: "REQ-DEWEY-20261023-003"
dispatch_note: "Research-output per CHECKLIST 2.8b. DEWEY delivered create-only copies to LIQUID, REGINALD, BROCK, VULCAN, TERRY, HENRY and RED (d0d5463a7); WALTER verified the set against the REQ list (0 backfills), so BOARD + route_log only. Quality gate: WALTER spot-checked ARCC 10-Q 6/30/2026 at EDGAR (accession 0001628280-26-050307): 'Software and Services 22.0%' (23.8% prior), total investments at fair value $29,349M: match. FRED first-published HY 340, CCC 1,340 [10/22] pulled by WALTER 19:48Z: match. Conflict check vs SIG-W-20261023-019 (REQ-002): no conflict; 019's AI slice (~10-15% of October HY) and this 17% are different bases (whole index vs a CCC-proxy sleeve's price loss). REG-T-04 not graded here; owners grade it. NCUA thread split to SIG-W-20261023-034 (S1: different owner)."
---
# DEWEY research (REQ-003, Will-approved): the two distressed pools hold different things. In CCC bonds about 78% of the 10/13–10/22 price loss is "everything else" (cable/telecom, JetBlue, FMC), AI builders about 17% (almost all CoreWeave), software about 5–8%. In loans priced below 80 cents, "technology" is 39% ($54.4B of $139.8B, JPM 10/6), led by PE-owned software. The issuance window is narrowed and expensive, not shown to be shut

**Reports:** `AGENTS/DEWEY/output/2026-10-23_ccc-and-under-80-loans-three-way-split.md` and `AGENTS/DEWEY/output/2026-10-23_hy-issuance-window-october.md` (commit d0d5463a7). **Commission:** REQ-DEWEY-20261023-003 (WALTER, Will-approved 13:37 ET 10/23; origin 015/016/019) and Will's thread 1. Kill conditions: none fired (no desk split published; delivered before the 10/26 deadline; HY 340 [10/22] at or above 320, full scope).

**Verdict:** REQ-002's "mostly broad" stands for high-yield bonds. "AI broadly defined" is a large share of distress only in leveraged loans and private credit, where the software bucket sits.

| Question | DEWEY's finding | Basis |
|---|---|---|
| CCC bonds, three-way split | HYG sleeve with yield-to-worst ≥12% (103 lines, 5.18% of the fund), 10/13 → 10/22: everything else **77.9%** of the price loss, AI builders (CoreWeave ×4, Edged) **16.6%**, software core list **5.5%** (broad list 8.0%). Largest single losses: JetBlue (−36.9%, 23% of the loss), FMC (−62.7%, 16%), Brightspeed (13%), CoreWeave (13%) | iShares holdings files, 1,328 of 1,332 bonds matched |
| CCC index composition | CCC = 8.58% of Bloomberg US HY; software 0.40 points = **about 4.7% of the tier**. Janus: cable/satellite and wirelines drive the CCC widening | Janus Henderson 10/15, Bloomberg index (not ICE) |
| Loans below 80 | **$139.8B** (+~90% y/y, $4B under the May 2020 high), 141 issuers; ≤60c $65B. "Technology" **39% = $54.4B** (CDK, Qlik, Quest), against software at about 10–13% of the index: **about 3× over-represented** | JPM 10/6 via The Edge reprint, text-checked; PIMCO 10/19 |
| Who holds the software loans (BDCs, 6/30/2026 filings) | ARCC 22.0% ≈ **$6.46B** (largest dollars); BXSL 18.9% ≈ $2.53B; GBDC 26.0% $2.14B; FSK 17.7% $2.02B; OBDC 11.6% ≈ $1.73B; **HTGC 32.8%** (highest share) $1.50B; PSEC 2.3% (lowest). Labels differ by BDC, so shares are not like-for-like | each BDC's own 10-Q / 10-K |
| HY ETFs | Software 4.1% of HYG, 3.6% of JNK; **0.6% of JNK's below-80 bucket**. The ETFs carry little of the distressed software bucket | iShares, SSGA daily files |
| Issuance | About **$7B October to date vs $51B September** (Bloomberg, snippet only); October 2025 also ran under half of September. **No named HY bond deal found pulled**; loans AVI-SPL $690M dropped, Circet €3B postponed, Radiology Partners loan pulled. CCC effective yield **17.99%** [10/22] (+127bp since 9/30) vs single-B **8.19%** (−2bp): the price lockout is at CCC only | Bloomberg via Advisor Perspectives (403, snippet); Octus 10/16; FRED |

**Per-recipient delta:**
- **LIQUID:** the CCC lockout is a CCC-only price story (single-B yield flat); "narrowed and expensive, not shut" is DEWEY's read, Low confidence on volume. Paramount's ~$11.4B month booking is UNKNOWN and can move the $7B.
- **REGINALD:** for the REG-T-04 lane, the bond widening is still broad, not an AI or software concentration; the loan-side software stress (39% of below-80) is where bank and NDFI exposure would sit.
- **BROCK:** the BDC software table is the new artifact. It goes stale when Q3 10-Qs land (late October to about 11/10); DEWEY suggests a re-run then. TSLX discloses no software line; BBDC UNKNOWN.
- **VULCAN:** AI builders are about 17% of the CCC-proxy price loss, almost all CoreWeave; **no AI builder appears in any distressed-loan list found** (absence of evidence only).

**Caveats (DEWEY's, kept in substance):** the bond window covers less than half of October (73bp of the 161bp CCC widening; 9/30 → 10/13 is decomposed only by Janus's sector read). Yield ≥12% is not a rating: CoreWeave's agency rating was not checked, and if it is above CCC the AI share of the true CCC tier is lower. The software list is DEWEY's own name classification. JPM's label is "technology", not software or AI; the Deep News reprint's "share of ≤60" reading is arithmetically impossible and treated as a translation error.

**Do not relay as:** "CCC widening is a software/AI story" (in bonds it is not); "JPM: software is 39% of distressed loans" (the label is technology, the denominator is loans ≤80c, not ≤60c); "AI builders are 17% of CCC" (it is a share of the price loss in a yield proxy over 10/13–10/22 only); "the HY market is frozen / issuance shut" (not shown on volume).

**UNKNOWNs:** ICE CCC tier sector composition; name-level drivers for 10/1 → 10/13 (+88bp); JPM's non-technology sector shares; CoreWeave's rating; Q3 BDC industry tables; BBDC software share; BIZD weights; normal October issuance baseline.

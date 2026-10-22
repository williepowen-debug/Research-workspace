# REGINALD — analysis of "Agentic AI at the Perimeter" (Will's docx, 2026-10-22)

**Input:** `AI Agent Banking Security Risks.docx` (Will's Downloads), read whole: 46,857 characters, 66 cited sources. It was copied to an isolated scratch folder and the text extracted with a stand-alone script; nothing in it was executed. **Verdict on the document:** an AI-generated synthesis. The structure and broad direction are sound, but it rests mostly on secondary and aggregator sources (financefeeds, Times of India, bankingnewsai, coinlaw, a Reddit thread, a YouTube video), and its in-text citation numbers do not map reliably to its source list. Read it as a well-organised hypothesis, not evidence.

## 1. Bottom line for us
1. **This is a funding-speed and margin story, not a credit story.** Nothing in it moves a loan-loss, CRE or NDFI channel. No matrix score, threshold, prediction or trade changes.
2. **The one mechanism that matters to this desk is deposit run speed.** If software agents move idle cash automatically, deposits at a bank under stress can leave faster than in 2023. Our funding observables (H.8, H.4.1 discount window, FHLB quarterly) are weekly or quarterly; they would record such a run after it happened, not before. This is a structural caveat on channel ③ (funding/confidence), which I used in this morning's HY answer. It is not a new instrument.
3. **The document's "winners vs losers" screen mislabels the regional it knows best.** It calls VLY "resilient". VLY's own Q3 release (8-K acc 0000714310-26-000045, 10/22) shows:
   - loan-to-deposit 96.3%
   - $5.3B of indirect/brokered deposits
   - time deposits +$482M, driven by indirect CDs and retail CD offers
   - Bluevine (a *pending* deal, close early 2027), bought for "low-cost, **digitally-sourced** deposit relationships" to "optimize our funding base".

   Digitally-sourced small-business deposits are the kind an agent can move most easily. On the document's own screen #1, VLY sits in both columns at once.
4. **Timescale is 12–24 months, and the size is unknown.** No bank has reported a loss (Morgan Stanley says it has not seen rogue agents; WALTER SIG-W-20261022-008). The FDIC Chair frames it as an open question ("how many and how big of an impact").

## 2. Load-bearing claims checked (11:1x ET, 10/22)
| Claim in the document | Check | Verdict |
|---|---|---|
| Big banks found agents "in multiple documented instances" acting without human instruction | WALTER -008: the Axios claim rests on **anonymous** executives, Morgan Stanley disputes it, no loss or regulator action | ⚠️ **Overstated.** "Documented" is the document's word, not the reporting's |
| Wells Fargo among the restricting banks | -008: only some secondary copies add WFC; one drops Citi | ⚠️ Unsettled |
| Dimon said at Q3 earnings that there is "a liability transfer" | -008 attributes the liability remark to the JPM **CFO**; the document cites Times of India | ⚠️ Attribution conflict; not checked at the transcript |
| Valley "acquired" Bluevine for $340M on 9/28 | VLY Q3 release: "**pending** acquisitions of Providence … and Bluevine"; close early 2027. Desk 8-K record: agreement 9/27, acc 0001193125-26-403391 | ❌ **Wrong tense.** Not closed. The 9/27 vs 9/28 date difference is press-release dating |
| VLY non-GAAP efficiency 52.1% | VLY Q3 release: **49.38% Q3**; 52.11% Q2 | ✅ for Q2, ⚠️ a quarter stale |
| VLY $15M AI run-rate savings; 80 of 3,600 staff with AI access | Source is bankingnewsai (aggregator); not in the Q3 release | UNVERIFIED |
| Huntington launched "The 1866 Studio" (AI agents, Google Cloud) on 10/19 | HBAN IR release, 10/19 08:25 ET: real; "built-in AI agents"; **early-access sign-up** | ✅ launch. ❌ the "saves pilot clients 4 hrs/week" figure **is not in the release** |
| FDIC Chair Hill: agent-driven deposit movement is a primary focus; ~50% of deposits are corporate | Banking Dive, remarks **10/20** (document says 10/21): "the big thing that we're thinking about"; "About half of deposits in the system are corporate" | ✅ substance. The article does **not** mention faster runs, the point the document attaches to it |
| CFPB 1033 rule: final 10/22/2024; same-day BPI/KBA/Forcht suit; tiers ≥$250B Apr-2026 · $10–250B Apr-2027 · $3–10B Apr-2028 · $1.5–3B Apr-2029 · $0.85–1.5B Apr-2030 · <$850M exempt; CFPB moved to set aside (2025); E.D. Ky. injunction | Consistent with my prior knowledge of the rule and suit; injunction timing not re-checked here | ✅ broadly; injunction date UNVERIFIED |
| Slok (Apollo): JPM+BAC+WFC hold ~$1.6T NIB deposits; full sweep = ~$47B/yr extra interest | Arithmetic implies a ~2.9% rate gap on the whole balance. That is a ceiling (100% swept), not an estimate | Secondary; treat as a **ceiling** |
| Regionals pay ~30bp more for deposits than Tier-1 (2.5% vs 2.2%) | GIBBS 10/21 same-line Q3 IB-deposit costs: large banks 1.98–2.94%, our cohort's changes inside that range ("overlapping ranges") | ⚠️ **Not supported** on GIBBS's same-line Q3 basis |
| Product names and adoption numbers (Meta "Muse" 6.6M downloads; OpenAI "Dots"; Anthropic "Claude Duet"; AISI 177,000-tool study) | Not checked; post-dates my reference knowledge | UNVERIFIED; do not cite |
| AI fraud-tool adoption 75–80% Tier-1 vs 30–40% regionals | Source coinlaw (aggregator) | UNVERIFIED |

## 3. Mechanisms, ranked by what they mean for the banks we track
| # | Mechanism | Who it hurts most | Size / evidence | Our read |
|---|---|---|---|---|
| ① | **Run speed:** agents move cash faster in stress | Banks with uninsured, digitally-reachable deposits and thin liquidity | No observation yet; 2023 runs were already phone/online-speed | **Most relevant to REGINALD.** Our weekly/quarterly funding gauges lag a faster run. Caveat only; no new monitor. |
| ② | **Deposit-cost drift:** agents end the "inertia" that keeps low-rate balances | Banks with large *cheap* retail balances. **In dollars that is the biggest banks** (Slok's $1.6T), not the regionals | Ceiling ~$47B/yr for three banks; a real share is unknown | Important nuance the document blurs: a bank already funded with brokered/CD money pays market rates and has **less** left to lose here. The exposed franchise is low-cost retail checking. |
| ③ | **Fraud / Reg E reimbursement** when an agent's payment is disputed | Retail-heavy banks with static call-centre checks | No losses reported | Operating cost, not credit. Small against current CRE recognition. |
| ④ | **1033 "trap":** regionals that paused API builds cannot block shared-credential bots without breaking customers' apps | Tier 2 ($10–250B), **the band most of our cohort sits in** (approximately WAL, OZK, VLY, SSB, BKU, FLG, ZION, CUBI, SBCF; CFG near the top; EGBN (~$9.5B) and AMTB near the $10B line; HBAN ($284B) is Tier 1. Asset bands are approximate and not re-checked per bank) | Real structural asymmetry; bank-by-bank readiness unknown | Plausible differentiator over 12–24 months; no bank-level data in hand |
| ⑤ | **Exam / vendor-risk pressure** (OCC non-core exams, model-risk rules, third-party guidance) | Smaller banks on Fiserv/FIS/Jack Henry cores | Document cites OCC bulletins; not re-checked | Compliance cost; not a stress channel |

## 4. Where it touches our existing work
- **BaaS / sponsor-bank perimeter (WQ-228):** Bluevine's deposits sit today with Coastal Community Bank (CCB) and migrate to VLY within ~180 days of close (~1H27; desk record). Digitally-sourced fintech deposits are the most agent-movable class. This adds a "how sticky are these deposits" question to the existing CCB/VLY watch. It is not a new thread.
- **VLY's early flag (Q3, this morning):** VLY released CRE reserves again while construction nonaccrual rose. Its funding is tight (96.3% loan-to-deposit, $5.3B indirect), and it is buying digital deposits. Credit and funding are separate legs; the document speaks only to the second.
- **Owners elsewhere:** GIBBS (large-bank operational risk; GIBBS is ACTION on -008) · VULCAN (agentic-AI adoption) · LIQUID (run speed and plumbing) · BROCK (none).

## 5. What would change this read
- A bank reports a **quantified loss** or a Reg E reserve tied to agent activity.
- A regulator issues agent-specific guidance or an enforcement action.
- A weekly H.8 or a bank 8-K shows deposit outflows **attributed** to automated sweeping.
- Bank-level disclosure of 1033/API readiness, which would let ④ rank names.

## 6. Improvement idea (for discussion; not approved; asked PROME to log it in `PROME/ideas/list.tsv`)
At the 11/07 matrix re-score, carry a **descriptive "run-speed exposure" column** beside each bank: share of uninsured deposits, share of brokered/indirect, share of non-interest-bearing retail (all Call Report). It would not be scored, and it would not be a threshold. **Benefit:** it names which cohort banks a faster deposit run would hit first, which our credit-only instruments cannot see. **Cost:** one more Call Report pull on the run that already happens.

---
## Addendum 2026-10-22 ~13:15 ET: DEWEY research consumed (two packets, Will-directed requests REQ-DEWEY-20261022-001/002). Prior text above unedited.

| Point in this analysis | DEWEY evidence | Effect |
|---|---|---|
| Run speed is the mechanism that matters (§1.2) | **No documented cyber/IT deposit run** (IMF 2024). Patelco's 17-day outage cost −2.7% of deposits for one quarter, recovered by Mar 2025. No AI-agent loss reported anywhere as of 10/22 (`../DEWEY/output/2026-10-22_bank-tech-vendor-concentration-ai-agent-risk.md`) | Caveat stands as a **structural possibility with no observed case**. Base rate = zero runs, so nothing here changes a score or a threshold |
| 1033 / core-vendor trap (§3 ④) | Core vendor named in 2024–26 primary documents for only **4 of 22** banks; WAL, OZK, SSB, EGBN, HBAN and VLY are UNKNOWN. Vendor breaches correlate across banks (MOVEit 2023: FLG via Fiserv, VLY, Cadence/HBAN) but none cut off customer access | Readiness still cannot be ranked bank by bank. Correlation is real at the data-breach level only |
| Deposit competition / stablecoins | Bank deposits **+$1,505.6B** vs stablecoin supply **+$46.1B** since GENIUS signing; supply −0.7% YoY. The OCC rule matches REGINALD's primary read (`../DEWEY/output/2026-10-22_genius-act-stablecoin-rewards-deposit-flight.md`) | No drain observed. "Stablecoins are draining regional deposits" stays a do-not-relay |
| §6 idea: run-speed exposure column at 11/07 | DEWEY Table 3 = NIB share, uninsured share (two bases, never ranked across), brokered and deposit cost for 22 banks, dated per row | **This is the input the idea needs.** Use it at 11/07 if Will approves the idea; it is an exposure INPUT, not a measure (no study links NIB share to outflows) |

DEWEY's "do-not-relay-as" lines are adopted: not "regional banks are the AI-agent target", and not "stablecoins are draining regional deposits".

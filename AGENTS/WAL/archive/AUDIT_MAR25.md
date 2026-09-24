> 🗄️ **ARCHIVED 2026-09-24** (WAL session #7, Will-directed housekeeping; PROME 8/23 item ②) under root `CLAUDE.md` § Data Hygiene retirement rule: >60 days old AND not boot-read AND not referenced by a live doc (index refs and dated records don't count), and not a pending-event artifact. **Content unchanged below this banner.** Record → `RETIREMENT_SWEEP_2026-09-24.md` (this folder). ⚠️ Bare file names inside (e.g. `THESIS.md`, `SCENARIOS.md`) now resolve one level up (`../`); `WAL/…`-prefixed paths are pre-promotion and resolve to `AGENTS/WAL/…`. **Historical record — cite with its own date, never as current.**

# WAL Domain Audit — March 25, 2026
**Auditor:** Reginald Subagent | **Commissioned by:** Prome (main agent)
**Scope:** Full domain review — architecture, KB quality, thesis coherence, staleness, research gaps, earnings readiness
**Coverage:** INDEX.md, STATUS.md, THESIS.md, SCENARIOS.md, WEAKNESSES.md, EARNINGS_PREP.md, EXTERNAL_PROMPTS.md, KB.tsv (59 rows), KB_INDEX.md

---

## 1. ARCHITECTURE ASSESSMENT

### What's There
The folder structure is coherent and has clearly been built with intent. The three-layer hierarchy (core docs → research/ subfolders → sources/) maps cleanly to the thesis vectors. INDEX.md functions well as a cold-boot navigator with read-order, data update rules, and a clear file map. KB_INDEX.md provides genuine navigational value.

### What's Missing or Incomplete

| Gap | Severity | Notes |
|-----|----------|-------|
| `TECHNICALS.md` — referenced in INDEX.md and STATUS.md but not read (flagged as "deep dive on-demand") | Medium | If it contains chart levels that inform put strike selection, it should be in boot sequence |
| `SCENARIOS.md` — explicitly marked **DRAFT** with "probabilities TBD" | High | For a ~27-day-to-earnings position, this is load-bearing and unfinished |
| `EARNINGS_PREP.md` — explicitly marked **DRAFT** with "populate after KB build" | High | KB is built now; this file was never updated post-KB |
| `WEAKNESSES.md` — marked **DRAFT** | Medium | Usable but thin — only 6 rows in the table |
| `research/HIDDEN_CRE/`, `research/JEFFERIES/`, `research/SSFA/` — referenced but not readable in this audit | Unknown | Cannot confirm whether these contain substantive research or just stubs |
| `sources/INSIDER_SCAN_WAL.md`, `sources/FDIC_QBP_...` — same | Unknown | KB cites them; cannot verify they exist |
| `PRIOR_RESEARCH_EXTRACTS.md`, `FORGE_STATUS.md`, `RQ-REG-A01_WAL_ZION_FRAUD_COMPARISON.md` — in file map but not read | Unknown | |

### Naming Consistency
Solid. File naming conventions are consistent. KB column headers are clear (ID, Date, Group, Entity, Fact, Source, Conf, Epistemic, Status, Stale_By, DerivedFrom, Vectors, Notes). One minor issue: STATUS.md says "59 rows" in footer, INDEX.md says "59 rows" in boot table, but KB.tsv actually has 60 rows (KB-WAL-001 through KB-WAL-060). The index seeding description ("59 rows across 10 groups") is one row short — KB-WAL-060 (SMFG full takeover) was added last and may not have been counted.

**⚠️ Concrete error:** Every reference to KB size says "59 rows" but there are 60 rows. Update INDEX.md, STATUS.md, and KB_INDEX.md.

---

## 2. KB QUALITY

### Overall Assessment: **B+ / Solid Foundation, Meaningful Gaps**

59 (actually 60) rows across 10 groups is a reasonable base for a $90B bank short thesis. The empirical rows are well-sourced — FFIEC call reports, 8-Ks, FDIC QBP, SEC Form 4s. But there are structural weaknesses in certain groups.

### Group-by-Group Critique

| Group | Rows | Grade | Issue |
|-------|------|-------|-------|
| HIDDEN_CRE | 7 | A | Strong. Empirical anchor (KB-001, 002, 003) + mgmt confirmation on tape (KB-004). H.8 context (KB-005) adds systemic framing. Equipment Finance as independent confirmation (KB-006) is clever. |
| SSFA | 6 | B | KB-009 conflates empirical amount with inferred composition (flagged "EMPIRICAL+INFERRED" — honest). KB-013 is regulatory forward-risk with no current regulatory action cited. The group lacks any external validation — no analyst, no regulatory precedent, no comparable bank that lost SSFA treatment. |
| CANTOR_FRAUD | 9 | A- | Best-evidenced group. ZION comparison (KB-015) is the standout — same ring, wildly different reserve rates. OREO trajectory (KB-019) is independently damning. Weakness: KB-021 (Portnoy/Rosen investigations) is A2-confidence but adds no quantitative teeth — class action = noise without underlying legal merit established. |
| INSIDER | 7 | B+ | CFO swap (KB-023) is the strongest individual KB row in the entire workbook. CEO medical leave timing (KB-024) is highly material. Zero buying (KB-027) is clean. KB-028 (cash-settled RSUs) is flagged ambiguous but not analyzed — what does cash settlement vs equity settlement signal about insider confidence? KB-029 (cross-bank comparison to OZK) is B1/ASSESSMENT and adds rhetorical rather than evidentiary value. |
| GEOGRAPHIC | 6 | A | Tightest group analytically. All four FDIC metrics hang together (NCO highest, pipeline lowest, PDNA/NCO gap tightest, CRE noncurrent below avg). The fast-transmission thesis is well-grounded here. KB-034 and KB-035 are B1/ASSESSMENT but clearly derived from A1 empiricals — appropriate. |
| JEFFERIES | 5 (+KB-060) | C+ | Weakest group. The intermediation chain (KB-036) is B1/ASSESSMENT with "needs Jefferies Q1 to confirm" — which happened today and hasn't been pulled. KB-037 is the SMFG 20% stake; KB-060 adds the full-acquisition FT story but notes it "cuts both ways." Convergence Day (KB-038) is solid but doesn't definitively prove WAL-Jefferies linkage — it proves WAL vulnerability. Madison fund letter (KB-039) is strong but the actual double-pledging mechanism is entirely unconfirmed. No SEC filing, no call report, no analyst report cited to establish that WAL actually lends to Jefferies. |
| NEVADA_GAMING | 5 | C | Worst-evidenced group. KB-041 (18-22% NV exposure) is B1/ESTIMATED — an analyst estimate with no primary source. Circa facility (KB-042) is solid but a single credit. KB-045 (consumer crossover from CARL) is B2/ASSESSMENT — two hops of inference. This group needs primary source work badly. |
| CAPITAL | 4 | B | CLN analysis (KB-047) correctly flags the limitation. Loans pledged (KB-048) is striking (74%) but needs sourcing detail — the "worst in SVB/FRC comparison set" claim has no citation. KB-049 (uninsured deposits vs unpledged assets) is flagged A2 but the $11.9B vs ~$10B numbers need Q1 refresh. |
| EARNINGS | 4 | B- | Only 4 rows for an entire earnings history is thin. No NIM trajectory, no deposit cost trend, no loan growth by segment. Q4 record earnings context (KB-050) is there, but this group should have 8-10 rows to anchor what "normal" looks like before the thesis fires. |
| MARKET_SIGNAL | 6 | B | Both -10%+ events are well-documented. May 2025 low (KB-058) is clean. Price trajectory (KB-059) is chart-based — appropriate to note the distribution pattern. Portnoy (KB-057) duplicates KB-021 (Cantor_Fraud) — these should be consolidated or cross-referenced. |

### Duplicate/Weak Entries
- **KB-056 (Madison_Sale) and KB-039 (Madison_Bankruptcy)** are the same fact in two groups (MARKET_SIGNAL and JEFFERIES). One should link to the other.
- **KB-057 (Portnoy) and KB-021 (Legal_Exposure)** overlap — KB-021 mentions Portnoy in CANTOR_FRAUD, KB-057 repeats in MARKET_SIGNAL. Should merge or cross-reference.
- **KB-029** (insider cross-bank comparison) is thin — this is editorial commentary, not evidence.

### Confidence Distribution
Of 60 rows:
- A1 (high confidence empirical): ~25 rows — good backbone
- A2 (solid empirical, some interpretation): ~18 rows
- B1 (assessment/analysis): ~14 rows
- B2 (speculative): ~3 rows

The B1/B2 concentration in JEFFERIES and NEVADA_GAMING is where thesis risk lives.

---

## 3. THESIS COHERENCE

### The Three Vectors: Do They Hold?

**Vector 1 (Hidden CRE) — HOLDS STRONGLY**
The logical chain is airtight: FFIEC call report → MI3 growing → management confirmed relabeling on tape → true CRE at 474% Tier 1. Equipment Finance decline as independent confirmation is clever and defensible. This is the strongest vector.

**Vector 2 (Jefferies Double-Pledging) — LOGICALLY COHERENT BUT EVIDENTIARY THIN**
The theory is plausible and the Convergence Day correlation is suggestive. But the actual intermediation chain (WAL → Jefferies → private credit fund → collateral) is not documented anywhere in the KB. There is no SEC filing, no call report disclosure, no analyst who has traced this chain. The vector rests on correlation (WAL dropped when credit market stress occurred) + inference (WAL lends to intermediaries). Convergence Day is consistent with V2 but also consistent with "WAL is a known CRE short and got caught in a sector rotation." The SMFG angle creates a genuine logical complication: if SMFG backstops Jefferies, V2 contagion risk is reduced. KB-060 acknowledges this but WEAKNESSES.md doesn't adequately model what a full Jefferies backstop does to the V2 probability.

**Vector 3 (SSFA Capital Arbitrage) — HOLDS AS STRUCTURAL RISK, NOT ACUTE CATALYST**
The math is sound: $17.2B at 20% RW vs 100% RW = $1.1B capital gap. But the KB correctly notes: "No current regulatory action — forward-looking risk." This vector requires a regulatory catalyst or a stress scenario that forces re-evaluation. As a standalone catalyst for Apr 21 earnings, V3 is unlikely to fire. It functions better as a multiplier: if V1 or V2 fires, V3 makes the hole deeper than consensus expects.

### Logical Gaps

1. **The "any one can fire" claim needs stress-testing against current price.** Stock at $68 with May 2025 low of $57 = 16% downside to prior cycle bottom. The thesis needs to answer: what actually moves the stock from $68 to $50-55 (the bear target)? SCENARIOS.md gives targets but not the specific transmission mechanism per vector.

2. **Fast-transmission differentiator is compelling but creates a monitoring problem.** If losses bypass the delinquency pipeline, the thesis is "we can't predict when it fires, only that it will." That's correct but makes position sizing and timing extremely difficult. The thesis would benefit from identifying what DOES provide advance warning if not delinquency data.

3. **War impact is mentioned in EARNINGS_PREP.md Q6** ("CRE borrower stress from oil/energy spike?") but is never developed. If the Middle East war is a genuine catalyst (Bloomberg framing), where does it transmit into WAL's book? Oil/energy spike → which WAL borrowers? Nevada gaming? Tech banking?

4. **The bull rebuttal section in THESIS.md doesn't address the strongest bull argument:** deposit growth. Deposits grew from $55B → $66B → $77B. A bank with deposit franchise stability and record earnings is harder to break quickly than a bank with funding stress. This isn't addressed in WEAKNESSES.md.

---

## 4. STALENESS

### Immediately Stale (Action Today)

| Row | Issue | Action |
|-----|-------|--------|
| KB-WAL-040 (Jefferies Q1 Signal) | Stale_By 2026-03-26 — Jefferies reported TODAY after close | Pull results NOW — provisions, credit commentary, Cantor/WAL mentions |
| STATUS.md Catalyst Calendar | "Mar 25: Jefferies Q1 after close" — this event has now occurred | Move to "What's Changed", log reaction |
| Research Agenda Item 1 | "Jefferies Q1 reaction" — pending and now actionable | Execute immediately |

### Stale at Apr 21 Earnings (Need Fresh Data)

20+ rows have Stale_By of 2026-04-30. These will all need Q1 2026 refresh:
- MI3 ratio (KB-001, 002, 003) — MOST CRITICAL: did hidden CRE continue growing?
- SSFA amounts (KB-008, 009, 010, 011, 012) — will Q1 call report shift these?
- Cantor reserve status (KB-014, 016, 018) — is $30M reserve still unchanged?
- OREO trajectory (KB-019) — did Q1 bring more charge-offs?
- Insider activity (KB-027) — any pre-earnings buying?
- Capital ratios (KB-046, 047, 048, 049) — NIM/funding cost movement
- Earnings context (KB-050, 051, 052, 053) — Q1 vs Q4

### Structurally Stale (Not Urgent but Notable)
- H.8 data (KB-005): June 2026 expiry — fine until Q2
- FDIC geographic data (KB-030, 031, 032, 033): June 2026 — fine for earnings
- SMFG acquisition (KB-037, 060): June 2026 — monitoring needed

---

## 5. RESEARCH GAPS

Things that should be in the KB but aren't:

### High Priority (Pre-Earnings)

1. **NIM and funding cost trajectory.** No KB row covering net interest margin trend, deposit repricing speed, or cost of funds. If NIM is compressing, it adds pressure. If stable, bulls use it as defense. This is the first question on any earnings call and the KB is silent.

2. **Loan growth by segment (Q4 2025 detail).** KB has growth_trajectory (KB-053) at asset level. But where is the new C&I growth coming from? Which segments grew? Without this, the MI3 relabeling story is harder to defend in real-time against management pushback.

3. **WAL Call Report RC-C state-level detail.** Listed in STATUS.md Research Agenda as pending. Arizona, California, Nevada noncurrent rates broken out. This would sharpen the geographic thesis beyond FDIC district aggregates.

4. **Jefferies Q1 actual results.** As of audit time, this has occurred and not been logged. Critical gap opening in real-time.

5. **War transmission mechanism.** Bloomberg framed Jefferies Q1 as "first look at credit markets + ME war impact." How does this hit WAL specifically? No KB row covers this.

### Medium Priority

6. **Deposit composition detail.** $77.2B in deposits — what's the brokered/wholesale percentage? WAL historically had a brokered deposit issue. Uninsured deposits $11.9B is in KB-049, but no breakdown of HOA deposits, tech banking deposits, or other segment-specific concentrations.

7. **Peer comparison on provision rates.** WAL's NCO of 0.24% is flagged as below peer avg of 0.32%, but there's no KB row mapping specific peer provisions (BANC, FHN, other regional CRE-heavy banks) as context for what "normal" looks like heading into a stress event.

8. **CARL/WAL quantified crossover.** KB-045 mentions consumer crossover as B2/ASSESSMENT. This should be a developed connection — Nevada gaming revenue data, consumer spending indexes, WAL gaming credit performance vs gaming revenue. Currently theoretical.

9. **Regulatory environment on SSFA.** KB-013 mentions Basel III Endgame risk but provides no specific regulatory citations. OCC, FDIC, Fed guidance on SSFA scrutiny should be sourced.

10. **Vecchione's return status.** CEO was on medical leave Dec 2024. Is he back? Leading Q1 earnings call? A CEO returning after absence could move the thesis either way — is this tracked anywhere?

### Low Priority

11. **Options market positioning.** The domain tracks put positions but no KB row covers WAL put/call skew, open interest, or options market pricing of tail risk. This would validate whether "vulnerability premium" is being priced.

12. **Short interest.** No KB row on WAL short interest levels or trend. If short interest is already elevated, squeeze risk increases.

---

## 6. EARNINGS READINESS

### EARNINGS_PREP.md Assessment: **Insufficient — Needs Immediate Work**

The file is marked DRAFT and was never populated with KB evidence anchors as promised. As of March 25, with 27 days to earnings, this is a problem.

**What's there:** 7 good questions, 5 thesis-confirm signals, 5 thesis-challenge signals. The questions are the right ones.

**What's missing:**

| Missing Element | Why It Matters |
|----------------|---------------|
| KB row anchors | Questions not tied to specific KB evidence. Can't do real-time call monitoring without pre-set benchmarks. |
| Baseline numbers | "Did MI3 ratio continue rising above 24.2%?" — needs Q0=24.2% explicitly, what level would be neutral, what level would be thesis-confirm or challenge |
| Quantitative tripwires | At what provision level does the thesis confirm? $50M+? $80M+? No thresholds set. |
| Call monitoring checklist | No real-time call format — what to listen for in the first 2 minutes, what to listen for in Q&A |
| Historical comparison | No Q4 2025 baseline transcript excerpts to compare against Q1 language changes |
| Segment-level expectations | What should C&I growth look like if relabeling continues? What CRE labeled decrease is suspicious? |
| War impact section | Not addressed at all |
| Options positions vs. scenarios | $65P Jun 18 is at -17% and expiring 8 weeks after earnings. Is there a plan if earnings are clean? |

**Critical gap:** There's no decision framework for the earnings call. "What would confirm thesis" and "what would challenge thesis" are listed, but there's no "if X then do Y" logic for position management. For a trade with four strikes across two expiries, this is load-bearing.

---

## 7. RECOMMENDATIONS — TOP 5 PRIORITIES BEFORE APR 21

### Priority 1: Pull Jefferies Q1 Results Tonight (Time-Sensitive)
KB-040 has Stale_By of March 26. Jefferies reported today. Pull the earnings release, transcript, and any credit provision commentary. Log as KB-WAL-061 with vector mapping. This is the only time-sensitive research item with a sub-24-hour window.

### Priority 2: Populate EARNINGS_PREP.md With KB Anchors and Tripwires
The file exists but is empty of substance. Before Apr 21, it needs:
- Specific numbers from KB as Q0 baselines (MI3=24.2%, provision=$30M, OREO=$137M, etc.)
- Quantitative tripwires (MI3 above 25% = thesis-confirm; below 22% + explanation = thesis-challenge)
- Real-time call monitoring format (what to listen for in opening remarks, what to listen for in Q&A)
- Position decision matrix: what happens to each put strike under each scenario

### Priority 3: Finalize SCENARIOS.md With Probability Weights
The file has been sitting as a draft since KB build. The KB now exists to anchor the probabilities. Run the SSFA regulatory analysis, the Jefferies chain logic, and the fast-transmission evidence to assign probabilities. Bear/Base/Bull targets are there — the timeline and probability weights are missing. Without this, position sizing lacks a framework.

### Priority 4: Address the Jefferies V2 Evidence Gap
The double-pledging chain is the weakest evidentiary group. Before earnings, either (a) pull the Jefferies Q1 call transcript and look for explicit mention of WAL or warehouse lending counterparties, or (b) acknowledge V2 is correlation-based and downgrade its probability weight accordingly. EXTERNAL_PROMPTS.md Prompt 3 on the Jefferies chain should be run immediately. Do not go into Apr 21 with V2 as a named primary vector if it has no primary source evidence of the actual WAL-Jefferies link.

### Priority 5: Build NIM/Deposit/Segment Baseline Into KB Before Earnings
The thesis correctly identifies hidden CRE via MI3 and SSFA as structural risks. But management will defend on NIM stability, deposit growth, and below-peer NCO rates. The KB currently has no ammunition to challenge these defenses. Before Apr 21, add 4-6 KB rows covering: NIM trend, deposit cost trend, brokered deposit %, and loan growth by segment. These are Q4 2025 data points that are already disclosed — they just aren't in the workbook.

---

## SUMMARY SCORECARD

| Dimension | Grade | Critical Issue |
|-----------|-------|---------------|
| Architecture | B+ | SCENARIOS.md, EARNINGS_PREP.md both marked DRAFT; row count is wrong (59 not 60) |
| KB Quality | B+ | Strong empirical core; JEFFERIES and NEVADA_GAMING groups evidentiary thin |
| Thesis Coherence | A- | V1 is rock-solid; V2 needs primary source; V3 is structural not acute |
| Staleness | ⚠️ | Jefferies Q1 data needed NOW; 20+ rows need Apr 21 refresh |
| Research Gaps | C+ | NIM, deposit composition, segment growth, regulatory SSFA citations all missing |
| Earnings Readiness | C | EARNINGS_PREP.md is framework-only; no anchors, no tripwires, no decision matrix |
| Overall | B- | Thesis is coherent and defensible. Operational readiness for Apr 21 is not there yet. |

---

*Audit completed 2026-03-25 | Next review: post-Jefferies Q1 reaction + Apr 21 earnings*

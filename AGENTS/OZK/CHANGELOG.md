# OZK THESIS — Changelog

Tracks changes to `OZK/THESIS.md` and structural shifts in the OZK bear case. Mirrors `AGENTS/REGINALD/thesis/CHANGELOG.md` format. Sub-docs (IQHQ_PLAYBOOK, SEVEN_CREDIT_DEEP_DIVE, RESG_MIX_DETERIORATION, IQHQ_SECONDARY_EXPOSURE, CIB_MARGIN_COMPRESSION) carry the deep math; this log tracks thesis-level deltas only.

## Version convention

- **Major (vX.0):** Structural change to the thesis — new channel, retired channel, conviction direction reversed, framework rewrite.
- **Minor (vX.Y):** Refinement — added leading indicator, recalibrated projection, integrated new evidence into existing structure, added/retracted sub-claim.

A new entry must describe:
1. **What changed** (one-line summary)
2. **Why it changed** (catalyst / source)
3. **Old view vs new view** (so the diff is auditable)
4. **Position implication** (one line, even if "unchanged")

---

## v1.4 — 2026-07-06 (staleness sweep: figures re-based to Call Report primary; prediction cross-refs re-wired)

### Summary
No thesis-direction change. Housekeeping refinement from the 7/6 staleness sweep: (a) all Q1'26 figures in THESIS re-based from the supplement basis ($465M/1.41% past-due, 0.57% NCO) to the **FDIC Call Report primary ($487.5M/1.48%, 0.56%)** adopted as canonical on 7/4 (definitional fork noted where relevant); (b) stale prediction cross-refs (REG-22/REG-23 — extracted to OZK-03/OZK-04 on 4/24) re-wired to the live OZK-xx rows, and the 7/4 pre-registered Jul-21 reads (OZK-05→09) linked from Migration Velocity + Invalidation sections.

### Changes

**1. Figure re-base** *(NO analytical change — same underlying quarter, standardized primary source)*
- Past-due Q1'26: $465M/1.41% → **$487.5M/1.48%** [Call Report REPDTE 20260331] in wave-1 summary, migration table, bull-rebuttal row, Invalidation §1. "10x in 6 months" → ">10x" (46→487.5 = 10.6x).
- NCO Q1'26: 0.57% → **0.56%** [Call Report] in wave-1 summary, ACL-thinning bull-pushback paragraph, Invalidation §2 — framing sharpened to "1bp above the ≤55bps kill line."
- **Invalidation §1 threshold (<$400M) deliberately kept unchanged** — set 4/23 on the supplement basis; re-basing the baseline doesn't move a pre-registered threshold.

**2. Cross-ref re-wire** *(navigation integrity)*
- REG-23 → **OZK-04** (re-scoped 7/4 to RESG-roster/commitments basis, 60%); REG-22 → **OZK-03** (+ **OZK-05** Q2 read); Invalidation §1 → **OZK-06**; Migration Velocity now points at the **OZK-05→09 Jul-21 pre-registration block** (conviction-governing: OZK-07).

- **Position implication:** Unchanged. Same data, standardized basis; all thresholds intact.

**Same-day addendum (7/6 PM — external-memo cross-check):** Will provided an external LLM memo (Atrium-2026-based; → `raw/llm_outputs/`). Cross-checking it against our primaries produced two THESIS-relevant changes: **(a) Pacific Center corrected** — Q4'25 Mgmt Comments disclose FULL principal repayment on $0.10B funded (par exit, NOT loss realization); WEAKNESSES C7 #5 adverse-selection transaction anecdote downgraded to one-of-two (Lincoln Yards remains the loss leg) [KB-199 corrected]. **(b) Extend-and-pretend counter updated 590 → 624 mods** (+34 in Q1'26; $904M reserves + $430M paydowns, per Q1'26 Mgmt Comments) [KB-202]. Neither changes thesis direction; (a) marginally strengthens the bull's funded-discipline point and is honestly logged as such. New unverified leads (Portal 405 / 777 Industrial / Southline, Peninsula) tracked at KB-201 pending the Atrium PDF.

---

## v1.3 — 2026-04-23 (audit-driven: Q1 NCO engaged, unverified claims removed, SCENARIOS reweighted)

### Summary
Completes self-audit punch list started in v1.2. (a) Engages Q1 26 NCO deceleration as a bull data point in THESIS.md ACL Thinning section, explicitly connecting it to "What Would Invalidate" §2. (b) Removes two unverified claims (KB-OZK-061 $13.8B quarterly origination breakdown, KB-OZK-062 DBRS 3.4-year time-to-default) from load-bearing prose. (c) Reweights SCENARIOS.md probabilities post-Q1 for the first time since Mar 23.

### Changes

**1. THESIS.md — Q1 26 NCO deceleration paragraph added** *(BULL-CASE ENGAGEMENT, no thesis direction change)*

- **What:** New paragraph inserted at end of ACL Thinning section. Acknowledges Q1 26 NCO annualized at 0.57% (in-line with ~50bps FY guide; below FY25's 1.18%) and explains why this doesn't break the thesis — recognition has been lumpy (quiet-quiet-quiet-pulse pattern Q1/Q2/Q3/Q4 25), and past-due metrics sit in the leading-indicator layer before charge-off conversion.
- **Why:** Self-audit (v1.2) flagged this as a soft spot — the thesis claimed Q4 25 was peak stress while Q1 26 actually came in materially lower. Bull-case pushback wasn't engaged.
- **Explicit kill criterion:** If FY 26 NCO tracks ≤55bps through Q3, reservoir framing is damaged — this is now a named invalidation trigger (see "What Would Invalidate" §2).
- **Position implication:** Unchanged. Past-due doubling is the leading indicator; NCO conversion by Q2-Q3 is the explicit test.

**2. THESIS.md — Two unverified claims removed from load-bearing prose** *(EVIDENCE DISCIPLINE)*

- **KB-OZK-061 removed** — Prior: "Original 2022 origination: Q1 $3.14B, Q2 $3.53B, Q3 $4.35B, Q4 $2.81B = ~$13.8B total [⚠️ UNVERIFIED]". Now: removed; replaced with parenthetical noting the removal. $3.7B 2026-maturing balance [KB-OZK-074, verified] and $1.5B life-sci concentration [KB-OZK-077, verified] retained — both independently primary-sourced.
- **KB-OZK-062 removed** — Prior: "DBRS: 2021-2022 vintages are 63% of CCC-C borrower pool; avg time to default 3.4 years [⚠️ UNSOURCED]". Now: replaced with arithmetic-only framing (3-year bridge + 2×1-year extension = default window 2025-2027 peaking 2026). No external citation needed; math is primary.
- **Why:** Self-audit flagged both as ⚠️ load-bearing but unsourced. Per LESSONS.md ("agent research is a starting point, not ground truth"), removing rather than preserving unverified claims in load-bearing language.
- **Position implication:** None — neither claim was decisive; thesis mechanics unchanged.

**3. SCENARIOS.md — Post-Q1 probability reweight** *(FIRST REWEIGHT SINCE MAR 23)*

- **Old weights (Mar 23-Apr 7):** Bear 50% / Base 30% / Bull 15% / Tail 5% → EV $37.45
- **New weights (Apr 23):** Bear 55% / Base 30% / Bull 12% / Tail 3% → EV $38.97
- **Bear +5pp:** Q1 past-due doubling ($207M → $465M) confirms migration-velocity thesis at leading-indicator layer. 3 new substandard + 2 new foreclosed direct data support.
- **Bull −3pp:** IQHQ Aug 2026 correction (from 2028) raises Wave 3 probability; Aimco fraud suit chills 4th rescue round; OZK pulling BACK from Fund Finance (Jake Munn Q1 call) removes a bull-path mechanism.
- **Tail −2pp:** CET1 11.64%, liquidity $16.9B, accretive buybacks, TBV +11% YoY — capital buffer demonstrated, rating/deposit-flight tail less likely.
- **Base unchanged:** slow-grind outcome remains single most plausible path.
- **Implied market overvaluation:** 24% → 22%. Thesis edge compressed modestly — accurate, not a problem.
- **April 16 Decision Framework:** RETRACTED (Q1 resolved Apr 21, framework obsolete). Replaced with "Post-Q1 Decision Gates" mapped to invalidation criteria from THESIS.md v1.2.
- **Put EV section:** Flagged as pre-Q1 premium basis; pointer added to THREAD3_ROLL_MATH.md for current roll economics.
- **Position implication:** Unchanged. EV framework still strongly favors the short at reweighted probabilities.

### What did NOT change
- Three-wave catalyst structure
- Migration velocity framework (KB-OZK-185)
- ACL thinning mechanics (1.26% ACL, 1.6× coverage, 8.86× → 1.39× collapse)
- Extend-and-pretend (590 mods / 98% gap / 59% re-default / 261bps rate cut)
- CRE concentration + Memo Item 3 (37.6%)
- IQHQ weighted EL ($140M = 22% of ACL)
- All 5 invalidation criteria (added v1.2)
- KB.tsv row count (185, no additions — one removal is in-prose only; KB rows stay in registry)

---

## v1.2 — 2026-04-23 (audit-driven: invalidation section + WEAKNESSES C5 correction)

### Summary
Self-audit identified two gaps: (a) PREDICTIONS.tsv had the falsifiability work but THESIS.md didn't carry concentrated kill criteria on its face; (b) WEAKNESSES.md C5 still claimed "IQHQ pushed to ~2028" which directly contradicted v1.1 THESIS.md framing of Aug 2026 as primary Wave 3 catalyst. Both fixed.

### Changes

**1. THESIS.md — New "What Would Invalidate" section added** *(STRUCTURE ADDITION, no thesis direction change)*

- **What:** 5 concentrated kill criteria with threshold levels inserted between "Bull Case Rebuttals" and "Short Interest Risk." Items 1 (past-due reversal), 2 (sustained sub-50bps NCO), 3 (IQHQ cure) are most load-bearing. Items 4 (sub-notes redemption) and 5 (office/life sci structural turn) are directional signals.
- **Why:** Self-audit 2026-04-23 found cold-boot agents needed invalidation criteria visible at thesis-level, not buried in PREDICTIONS.tsv.
- **Cross-refs:** Each criterion anchored to REG-22/23 in PREDICTIONS.tsv or IQHQ_PLAYBOOK.md scenarios.
- **Position implication:** Unchanged — no new catalysts, just explicit invalidation triggers for the existing thesis.

**2. WEAKNESSES.md C5 — Retracted "IQHQ pushed to 2028"** *(ERROR CORRECTION)*

- **Old view (retracted):** "IQHQ maturity pushed to ~2028. No longer a 2026 catalyst. The thesis should lean on Waves 1-2 without invoking IQHQ for near-term catalysis."
- **New view:** IQHQ RaDD maturity is August 2026 (correction Apr 22, integrated into THESIS v1.1). IQHQ is the primary Wave 3 catalyst with weighted EL $140M = 22% of OZK ACL.
- **Why error persisted:** WEAKNESSES.md wasn't updated when the Apr 22 maturity correction landed. Self-audit caught the inconsistency between THESIS (Aug 2026, primary catalyst) and WEAKNESSES (2028, deferred).
- **Position implication:** Unchanged — THESIS and positions have reflected Aug 2026 since Apr 22.

### What did NOT change
- Three-wave catalyst structure
- Migration velocity framework (KB-OZK-185)
- ACL thinning trajectory
- All other WEAKNESSES rebuttals (C1, C2, C3, C4, C6)
- KB.tsv rows (kill criteria cross-reference existing REG-21/22/23 + IQHQ scenarios without adding new rows)

---

## v1.1 — 2026-04-23 (Q1 26 print integration + 6Q historical refinement)

### Summary
Integrates the Q1 2026 earnings print (Apr 21) and the 6-quarter historical deep dive (Q4 24 → Q1 26 Mgmt Comments) completed Apr 22-23. Adds three sub-docs + one trajectory revision. Thesis direction is unchanged; mechanism is refined and one mid-flight projection is retracted.

### Changes (in order of impact)

**1. Leading indicator reframed: "mix shift" → "migration velocity" + "past-due regime change"** *(REFINEMENT, partially RETRACTED)*

- **Old view (Apr 22, Thread C):** Problem-category share (Office + Life Sciences + Land + Hotel) jumped 27.1% → 29.6% of RESG in one quarter (Q4 25 → Q1 26). Forward-projected to 36.4% in 8Q at observed pace ("biggest find" of Apr 22 work).
- **New view (Apr 23, after 6Q historical extract):** Share metric has been **stable in a 27-31% band for 6 consecutive quarters** (Q4 24 was actually the high at 30.9%). Q1 26's 29.6% is a partial retracement of a Q4 25 mechanical dip (San Diego Life Sci asset sale + $72M Boston Office charge-off lowered the denominator), NOT a new acceleration. Linear projection to 36.4% is **invalidated**.
- **What survived the retraction (the real story):** Underneath the stable share, three different leading indicators ARE accelerating:
  - **Substandard non-accrual mass migration** — $59M (Q2 25) → $150M (Q3 25) → $341M (Q4 25) → implied $400M+ (Q1 26). 154% then 127% QoQ. Migration started Q3 25, not Q1 26.
  - **Past-due 30+ DPD regime change** — flat at $45-50M / 0.14-0.17% for FOUR quarters Q4 24 through Q3 25, then stepped to $207M / 0.64% Q4 25, then $465M / 1.41% Q1 26. **10x in 6 months.** A regime change, not a gradual build.
  - **Recognition tempo (NCO) pulsed** — quiet quarters (Q1 25 25bp, Q2 25 10bp, Q3 25 41bp), then a Q4 25 pulse at 118bp ($72M Boston Office single charge-off), then back to 57bp Q1 26.
- **Source:** `historical/Q4_24_extract.md` through `historical/Q4_25_extract.md` (5 PDFs, 5 parallel sub-agents Apr 23). Combined with `research/threads/RESG_MIX_DETERIORATION.md` Q4 25 / Q1 26 baseline.
- **KB / PREDICTIONS impact:**
  - `KB-OZK-184` — share-projection claim (29.6% → 36.4% in 8Q) marked SUPERSEDED by `KB-OZK-185` (this version). Past-due / classified projection within KB-OZK-184 still holds.
  - `REG-21` (problem-category share ≥32% by Q4 26) — confidence revised DOWN from 60% → 25%.
  - `REG-22` (FY 26 NCO ≥60bps) — confidence unchanged at 55%.
  - `REG-23` (classified/RESG ≥3.8% by Q4 26) — confidence unchanged at 60%.
- **Position implication:** **Unchanged.** $42.5P Aug duration captures IQHQ + the migration-velocity recognition pipeline regardless of which leading indicator carries the bear case.

**2. IQHQ secondary-exposure question — DISPOSITIVELY closed** *(EVIDENCE INTEGRATION, no thesis change)*

- **Old view:** Gleason Q1 26 transcript ambiguity ("any other project with IQHQ") left a multi-credit IQHQ exposure scenario open at low probability.
- **New view:** OZK CCO Michelle Rossow on-record to Bisnow Mar 19 2026: *"We have one credit with IQHQ, which is the senior secured loan on their San Diego RaDD project."* Disconfirmation map for sister projects (Fenway → JPM, Arbor → KKR, Spur → Apollo, 155 N Beacon → Citizens, 109 Brookline → assumed from EQC, Boynton Yards → Leggat McCall). RaDD is OZK's SOLE IQHQ exposure.
- **Source:** `research/threads/IQHQ_SECONDARY_EXPOSURE.md` (Apr 22, Opus thread A). Updated `IQHQ_PLAYBOOK.md` with Apr 23 confirmation block. KB-OZK-178.
- **Position implication:** Weighted EL on RaDD ($140M on $555M funded) stands unchanged. No second IQHQ credit to model. Aug 21 put duration unchanged.

**3. Boynton Yards $246M sponsor identified — Leggat McCall, NOT IQHQ** *(EVIDENCE INTEGRATION)*

- **Old view:** SEVEN_CREDIT_DEEP_DIVE §2 #5 ($169M Boston Life Sci substandard) had two top candidates at 50/40 weight: Candidate A (10 Prospect / US2) vs Candidate B (808 Windsor / Boynton Yards). Boynton Yards was tentatively classified in some materials as an IQHQ project.
- **New view:** 808 Windsor / Boynton Yards Somerville sponsor confirmed as Leggat McCall + DLJ + Deutsche Finance America (Wolf Media Dec 2021 press release; Boston Globe Aug 2024). NOT IQHQ. Combined with the Apr 22 sole-exposure finding above, Candidate B promoted to HIGH confidence; Candidate A demoted to secondary.
- **Source:** `research/threads/IQHQ_SECONDARY_EXPOSURE.md`; SEVEN_CREDIT_DEEP_DIVE.md §2 #5 updated 2026-04-23. KB-OZK-179.
- **Position implication:** Unchanged. Sponsor identity refinement; loss severity work stays in SEVEN_CREDIT.

**4. CIB margin compression — vertical-specific, net-neutral** *(NEW EVIDENCE, calibrating-only)*

- **New finding:** 3 of 6 CIB verticals (ABLG, Fund Finance, LFG) compressing on spread/structure per Munn's Q1 26 commentary. Defense is rotation to CBSF/NRG/EFG plus Franchise Capital Solutions (new vertical Q1 26). "+12bp new-vs-legacy spread" is a mix-shift metric, not pricing power. NIM 4.20% Q1 26 likely drifts to 4.10-4.15% over 2026 absent rate-environment change.
- **Source:** `research/threads/CIB_MARGIN_COMPRESSION.md` (Apr 22, Opus thread B). KB-OZK-180, KB-OZK-181.
- **Position implication:** Confirmatory but not decisive — adds 0.5-1.0 vol to the NIM leg. IQHQ Aug + RESG migration remain higher-beta catalysts.

**5. Wave 1 of three-wave catalyst structure resolved** *(STATE UPDATE)*

- **Old view:** Wave 1 = "NOW → Apr 16 earnings" (later corrected to Apr 21 actual print date).
- **New view:** Wave 1 ✅ RESOLVED Apr 21. Print confirmed slow-grind thesis — past-due doubled QoQ, 3 new substandard credits identified, 2 new foreclosed (Chicago LS $50M / Santa Monica Office $45M at 15% leased), no fire. NCO 0.57% in-line with ~50bps FY guide.
- **Source:** `Q1_2026_ANALYSIS.md`, Q1 2026 Mgmt Comments PDF, earnings call transcript.
- **Position implication:** Wave 2 (NY pipeline conversion) and Wave 3 (IQHQ Aug 2026) are now the live legs. **IMPORTANT: STATUS previously labeled IQHQ as Aug 2028; corrected to Aug 2026 on Apr 22.**

### Sub-docs created/updated this version

| File | Status | Purpose |
|---|---|---|
| `research/threads/IQHQ_SECONDARY_EXPOSURE.md` | NEW (Apr 22) | Closes "any other IQHQ project" ambiguity. Verdict: NO EVIDENCE of second exposure. |
| `research/threads/CIB_MARGIN_COMPRESSION.md` | NEW (Apr 22) | 3 of 6 CIB verticals compressing; rotation defense exhaustible. |
| `research/threads/RESG_MIX_DETERIORATION.md` | NEW (Apr 22), REVISED (Apr 23) | Apr 22 version overstated linear projection. Apr 23 revision adds 6Q view + retraction. |
| `historical/Q4_24_extract.md` | NEW (Apr 23) | First in 5-quarter historical extract series. |
| `historical/Q1_25_extract.md` | NEW (Apr 23) | |
| `historical/Q2_25_extract.md` | NEW (Apr 23) | |
| `historical/Q3_25_extract.md` | NEW (Apr 23) | |
| `historical/Q4_25_extract.md` | NEW (Apr 23) | |
| `IQHQ_PLAYBOOK.md` | UPDATED (Apr 23) | Added Rossow sole-exposure confirmation block. |
| `SEVEN_CREDIT_DEEP_DIVE.md` | UPDATED (Apr 23) | §2 #5 Candidate B promoted to HIGH confidence. |

### KB / PREDICTIONS deltas

- **Added KB rows (Apr 22 work persisted Apr 23):** KB-OZK-178 through KB-OZK-184 (7 rows).
- **Added KB row (Apr 23 retraction):** KB-OZK-185 — corrected 6Q view; supersedes Claim A of KB-OZK-184.
- **Modified KB row:** KB-OZK-184 — Status ACTIVE → ACTIVE_PARTIAL; Conf B2 → C3; Notes flagged for partial supersession.
- **Added PREDICTIONS (Apr 23):** REG-21, REG-22, REG-23.
- **Modified PREDICTIONS (Apr 23):** REG-21 confidence 60% → 25% on retraction.

### What did NOT change

- Three-wave catalyst structure (Wave 1 RESOLVED, Wave 2 + Wave 3 unchanged)
- Reservoir thesis core
- Extend-and-pretend / classification gap analysis
- ACL thinning trajectory
- CRE concentration metrics
- Memo Item 3 / hidden CRE finding (37.6%)
- 2022 vintage maturity wall
- Life sciences collapse channel
- Bull case rebuttal structure (one rebuttal will be added in v1.2 covering share stability)

---

## v1.0 — Pre-2026-04-22 baseline (PINNED)

State of OZK/THESIS.md as it existed before the Q1 2026 earnings integration began. Document structure: Reservoir Thesis → Extend-and-Pretend Classification Gap → ACL Thinning → CRE Concentration → Memo Item 3 → 2022 Vintage Maturity Wall → Life Sciences Collapse → Bull Case Rebuttals → Short Interest Risk.

Three-wave catalyst structure as of v1.0: (1) NOW → Apr 16 earnings; (2) Q2 2026 NY pipeline; (3) Aug 2026 → likely Aug 2028 IQHQ RaDD.

Master KB ID range used through v1.0: KB-OZK-001 through KB-OZK-177.

---

*Future entries: append above v1.0, newest at top. Never delete; supersede instead.*

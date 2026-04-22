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
- **Source:** `historical/Q4_24_extract.md` through `historical/Q4_25_extract.md` (5 PDFs, 5 parallel sub-agents Apr 23). Combined with `RESG_MIX_DETERIORATION.md` Q4 25 / Q1 26 baseline.
- **KB / PREDICTIONS impact:**
  - `KB-OZK-184` — share-projection claim (29.6% → 36.4% in 8Q) marked SUPERSEDED by `KB-OZK-185` (this version). Past-due / classified projection within KB-OZK-184 still holds.
  - `REG-21` (problem-category share ≥32% by Q4 26) — confidence revised DOWN from 60% → 25%.
  - `REG-22` (FY 26 NCO ≥60bps) — confidence unchanged at 55%.
  - `REG-23` (classified/RESG ≥3.8% by Q4 26) — confidence unchanged at 60%.
- **Position implication:** **Unchanged.** $42.5P Aug duration captures IQHQ + the migration-velocity recognition pipeline regardless of which leading indicator carries the bear case.

**2. IQHQ secondary-exposure question — DISPOSITIVELY closed** *(EVIDENCE INTEGRATION, no thesis change)*

- **Old view:** Gleason Q1 26 transcript ambiguity ("any other project with IQHQ") left a multi-credit IQHQ exposure scenario open at low probability.
- **New view:** OZK CCO Michelle Rossow on-record to Bisnow Mar 19 2026: *"We have one credit with IQHQ, which is the senior secured loan on their San Diego RaDD project."* Disconfirmation map for sister projects (Fenway → JPM, Arbor → KKR, Spur → Apollo, 155 N Beacon → Citizens, 109 Brookline → assumed from EQC, Boynton Yards → Leggat McCall). RaDD is OZK's SOLE IQHQ exposure.
- **Source:** `IQHQ_SECONDARY_EXPOSURE.md` (Apr 22, Opus thread A). Updated `IQHQ_PLAYBOOK.md` with Apr 23 confirmation block. KB-OZK-178.
- **Position implication:** Weighted EL on RaDD ($140M on $555M funded) stands unchanged. No second IQHQ credit to model. Aug 21 put duration unchanged.

**3. Boynton Yards $246M sponsor identified — Leggat McCall, NOT IQHQ** *(EVIDENCE INTEGRATION)*

- **Old view:** SEVEN_CREDIT_DEEP_DIVE §2 #5 ($169M Boston Life Sci substandard) had two top candidates at 50/40 weight: Candidate A (10 Prospect / US2) vs Candidate B (808 Windsor / Boynton Yards). Boynton Yards was tentatively classified in some materials as an IQHQ project.
- **New view:** 808 Windsor / Boynton Yards Somerville sponsor confirmed as Leggat McCall + DLJ + Deutsche Finance America (Wolf Media Dec 2021 press release; Boston Globe Aug 2024). NOT IQHQ. Combined with the Apr 22 sole-exposure finding above, Candidate B promoted to HIGH confidence; Candidate A demoted to secondary.
- **Source:** `IQHQ_SECONDARY_EXPOSURE.md`; SEVEN_CREDIT_DEEP_DIVE.md §2 #5 updated 2026-04-23. KB-OZK-179.
- **Position implication:** Unchanged. Sponsor identity refinement; loss severity work stays in SEVEN_CREDIT.

**4. CIB margin compression — vertical-specific, net-neutral** *(NEW EVIDENCE, calibrating-only)*

- **New finding:** 3 of 6 CIB verticals (ABLG, Fund Finance, LFG) compressing on spread/structure per Munn's Q1 26 commentary. Defense is rotation to CBSF/NRG/EFG plus Franchise Capital Solutions (new vertical Q1 26). "+12bp new-vs-legacy spread" is a mix-shift metric, not pricing power. NIM 4.20% Q1 26 likely drifts to 4.10-4.15% over 2026 absent rate-environment change.
- **Source:** `CIB_MARGIN_COMPRESSION.md` (Apr 22, Opus thread B). KB-OZK-180, KB-OZK-181.
- **Position implication:** Confirmatory but not decisive — adds 0.5-1.0 vol to the NIM leg. IQHQ Aug + RESG migration remain higher-beta catalysts.

**5. Wave 1 of three-wave catalyst structure resolved** *(STATE UPDATE)*

- **Old view:** Wave 1 = "NOW → Apr 16 earnings" (later corrected to Apr 21 actual print date).
- **New view:** Wave 1 ✅ RESOLVED Apr 21. Print confirmed slow-grind thesis — past-due doubled QoQ, 3 new substandard credits identified, 2 new foreclosed (Chicago LS $50M / Santa Monica Office $45M at 15% leased), no fire. NCO 0.57% in-line with ~50bps FY guide.
- **Source:** `Q1_2026_ANALYSIS.md`, Q1 2026 Mgmt Comments PDF, earnings call transcript.
- **Position implication:** Wave 2 (NY pipeline conversion) and Wave 3 (IQHQ Aug 2026) are now the live legs. **IMPORTANT: STATUS previously labeled IQHQ as Aug 2028; corrected to Aug 2026 on Apr 22.**

### Sub-docs created/updated this version

| File | Status | Purpose |
|---|---|---|
| `IQHQ_SECONDARY_EXPOSURE.md` | NEW (Apr 22) | Closes "any other IQHQ project" ambiguity. Verdict: NO EVIDENCE of second exposure. |
| `CIB_MARGIN_COMPRESSION.md` | NEW (Apr 22) | 3 of 6 CIB verticals compressing; rotation defense exhaustible. |
| `RESG_MIX_DETERIORATION.md` | NEW (Apr 22), REVISED (Apr 23) | Apr 22 version overstated linear projection. Apr 23 revision adds 6Q view + retraction. |
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

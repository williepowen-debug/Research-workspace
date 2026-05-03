# Item #2.5 — KB→VX Reference Integrity DISPOSITIONS

**Created:** 2026-05-02 (Session 1 output — review-ready, ZERO TSV mutations applied)
**Source plan:** `workbook/ITEM_2.5_PLAN.md`
**Methodology rule:** codified to CARL CLAUDE.md as new "WORKBOOK DISCIPLINE" section (this session, S1.0)
**External feedback applied:** `User Input/Two views on the plan.md` Q1-Q8 + 1 missing-item check

> **Status:** Awaiting Will review. **Approval gate before Session 2 execution.**

---

## Verified count (S1.1)

Live re-run of enumeration script (verified vs `workbook/VX.tsv` IDs):

| Metric | Count |
|---|---|
| KB rows total | 260 |
| VX IDs in VX.tsv | 110 |
| **Distinct dangling VX IDs in KB.tsv** | **43** ✓ matches plan |
| **Total dangling KB→VX edges** | **59** ✓ matches plan |
| KB rows affected | 51 |

### Naming-generation breakdown (matches plan exactly)

| Generation | Count | IDs | Edges |
|---|---|---|---|
| DECIMAL | 1 | VX-CARL-1.10 | 2 |
| OTHER | 1 | VX-CARL-5 | 1 |
| STANDARD | 34 | (legacy + 7 CREATE candidates) | 47 |
| MULTITOKEN | 7 | ABS-AUTO-{ALLY,CACC,SPREAD}, AUTO-CVNA, CVNA-GT, LABOR-ICE-01, STATE-FL | 9 |
| **Total** | **43** | | **59** |

**Reviewer-flagged check (KB-105/106/153):** ✓ ALL THREE present in MULTITOKEN bucket. Script enumeration is complete; no upstream miss.

---

## Disposition summary

| Action | Count | Net effect |
|---|---|---|
| **CREATE** new VX rows | **9** | KB refs auto-resolve when targets exist |
| **REDIRECT** KB ref to existing VX | **5** | Refs swapped in-place |
| **REMOVE** dangling KB ref | **38 ref-blanks across ~33 KB rows** | Row Status preserved (conservative policy) |
| **VX_DEDUPE** | 1 (MACRO-05 NFP → MACRO-09) | NFP row renumbered; PPI row keeps MACRO-05 (KB-212 ref unaffected) |
| **SCHEMA edit** | 1 | Delegated_To description fix |

**Post-S2 expected state:** 0 dangling KB→VX refs. KB row count unchanged at 260. VX row count 110 + 9 CREATEs = 119.

---

## Per-VX-ID disposition table

Verified-by-reading column = read each KB row's Date/Status/Fact/Notes/Vectors before deciding.

### CREATEs (9)

| VX ID (new) | Anchor KB rows | Verified? | Rationale |
|---|---|---|---|
| VX-CARL-CC-01 | 096, 155, 243 | ✓ | All three measure CC 90+ DQ stress / SYF tier-spending; share NY Fed 12.7% anchor + GFC 13.74% threshold |
| VX-CARL-SAV-01 | 098 | ✓ | KB-098 is live STATUS metric (Savings rate 4.0% Feb), Stale_By 2026-06-30 |
| VX-CARL-AG-01 | 251 | ✓ | KB-251 already Delegated_To=POP; live thread per ROADMAP. Per #2d precedent: stays in CARL VX with `Delegated_To=POP` flag in Notes (POP/KB.tsv doesn't exist yet — conscious arch debt) |
| VX-CARL-DSL-01 | 253 | ✓ | KB-253 freight-demand-destruction signal; current open thread |
| VX-CARL-K-01 | 154, 155, 156 | ✓ | Anchor: BofA tier-spending-growth gap (Green/Yellow/Orange/Red bands measurable). KB-154 plasma is behavioral leading indicator (PARTIAL fit, noted in Notes). **KB-157 dropped per WORKBOOK DISCIPLINE** — Minneapolis Fed research is meta-acknowledgment with no measurable. **KB-091 dropped** — convergence-framework row, no shared threshold (REMOVE rather than force-fit) |
| VX-CARL-WEALTH-01 | (anchor pending) | ✓ | **[FLAG: uncertain — Will to review]** Per reviewer Q4 nuance: V14 = Upper-Decile Wealth Stress. Best measurable = Prime CC NCO (AXP/DFS proxy). Initial KB-237 (institutional positioning) and KB-111 (retail equity flows) **both REMOVE** — neither fits prime-NCO threshold. Vector created with TBD anchor pending Q1 AXP/DFS quarterly. *See "What V14 measures" section below.* |
| VX-CARL-FL-01 | 113, 249 | ✓ | KB-113 (FL UI Wave 1 fired) + KB-249 (FL labor weakness) share FL composite-stress measurement. KB-249 currently has dangling STATE-FL ref → REDIRECT to FL-01 |
| VX-CARL-ABS-AUTO-CACC | 106 | ✓ | Multitoken naming retained per Q6 (readability beats consistency). CACC FY2025 10-K data, distinct from existing ABS-08..11/15 (Santander/Exeter) |
| VX-CARL-ABS-AUTO-SPREAD | 153 | ✓ | Subprime auto ABS spreads (Wells Fargo Nov 2025 baseline). Distinct from existing ABS-17 (ABS vs HY divergence) |

### REDIRECTs (5)

| KB row | From (dangling) | To (existing or new) | Verified threshold fit? |
|---|---|---|---|
| KB-099 | VX-CARL-AUTO-01 | **VX-CARL-ABS-12** (Ally Retail Auto NCO) | ✓ Same metric (ALLY NCO 1.8-2.0% guide vs ABS-12 spot 1.97%) |
| KB-105 | VX-CARL-ABS-AUTO-ALLY | **VX-CARL-ABS-12** (Ally Retail Auto NCO) | ✓ Same metric (ALLY 2024 10-K NCO 2.2% data point) |
| KB-027 | VX-CARL-AUTO-CVNA | **VX-CARL-CVNA** (Carvana Stock canary) | ✓ Stock-canary threshold fits CVNA judge-order/16% drop event |
| KB-249 | VX-CARL-STATE-FL | **VX-CARL-FL-01** (new) | ✓ FL labor row consolidates with FL UI cascade (KB-113) |
| KB-162 | VX-CARL-1.10 | **VX-CARL-SAV-01** (new) | ✓ Savings rate Feb 4.0% feeds savings vector |

### REMOVEs — Conservative policy applied

**Per reviewer Q3 + WORKBOOK DISCIPLINE rule:** blank ref, preserve KB row Status. Do NOT silently downgrade. Where a row's continued ACTIVE status looks dependent on the dangling linkage (orphan-claim risk), surface as separate finding in **Section: Orphan-Claim Audit Byproduct** below.

**Legacy taxonomy refs (33 ref-blanks across 28 unique KB rows):**

| Group | KB rows | Removed VX ref | Notes |
|---|---|---|---|
| 401K | 009 | 401K-01 | Row CONFIRMED (>5.5% prediction settled); single legacy ref |
| Generic | 012, 021, 022 | STRESS-01, CREDIT-01, DEMO-01 | Generic single-row legacy |
| Fragment | 013, 014 | DQ-01, DQ-02 | Fragmentary DQ-* naming |
| HSG-* | 011, 015, 018, 019, 023, 053 + KB-052/054/062/066 (multi-ref) | HSG-06/07/08/09/10/11 | All HOMER-delegated; HOMER owns vectors. KB-052 also loses MTG-016. KB-062/066 preserve VX-CARL-MF-01 ref |
| MTG-* | 016, 017, 040, 046, 047, 048, 052, 097, 119 | MTG-01/016/020/021/022, FF-01, FHA-01/03 | HOMER-delegated; HOMER owns vectors |
| Decimal | 081 | VX-CARL-5 | Row already STALE; fragment ID |
| Retail/Macro | 094, 163 | RETAIL-01, VX-CARL-1.10 (KB-163 only) | KB-094 already STALE; KB-163 monthly Core PCE YoY has no matching vector (MACRO-07 measures Q-on-Q NIPA — different metric) |
| Cross-domain | 102, 103, 104 | LAB-01, LABOR-ICE-01 (×2) | LABOR/MARCO domain — not CARL VX scope |
| Supply event | 101 | FERT-01 | Russia AN suspension is supply event; FOOD-01 measures price downstream — strict-reading does not fit. Flag: consider supply-event sub-vector class later |
| Wealth/K-shape mismatches | 091, 111, 112, 157, 237 | KWLTH-01, KSHAPE-01, RV-01, K-01, WEALTH-01 | Per WORKBOOK DISCIPLINE: thresholds don't fit. KB-091 framework row; KB-111 retail flows ≠ prime NCO; KB-112 RV-canary ≠ tier-spending; KB-157 meta-research; KB-237 institutional flows ≠ prime NCO |
| CVNA fraud | 107, 152 | CVNA-GT, AUTO-CVNA | KB-107 binary trigger doesn't fit CVNA stock-canary threshold; KB-152 fraud architecture row, no shared metric |

---

## Architectural items

### 1. MACRO-05 dedupe (S2.1 mechanical)

Two rows in `workbook/VX.tsv` share ID `VX-CARL-MACRO-05`:
- Line 90: "3-Month NFP Average" (~68K/mo, RED, Apr 3 2026)
- Line 103: "PPI Final Demand YoY (Headline)" (+4.0%, RED, Apr 14 2026)

KB ref check: only **KB-CARL-212** references VX-CARL-MACRO-05, and from context (PPI March 2026) it unambiguously means the **PPI row**.

**Decision:** Renumber the **NFP row** (line 90) to **VX-CARL-MACRO-09** (next available — MACRO-08 is ISM Prices Paid). PPI row stays as MACRO-05. **Zero KB.tsv changes** required for this dedupe.

### 2. SCHEMA.tsv `Delegated_To` description fix (S2.4 mechanical)

Current description (per SCHEMA.tsv read at boot):
> "When set, Status should typically be SUPERSEDED (handed off) or CONFIRMED (still load-bearing but actively tracked downstream). Replaces the prior 'DELEGATED TO HOMER' Status overload."

This contradicts Item #2a's executed rule (Status preserved as ACTIVE for all 44 HOMER-delegated rows). Fix to:
> "When set, Status is preserved (ACTIVE/CONFIRMED/STALE/etc.) — Delegated_To is an orthogonal flag, not a Status override. Sub-agent ownership and lifecycle state are independent concerns. Filter `Status=ACTIVE AND Delegated_To IS NULL` for CARL-direct active claims."

### 3. AG-01 POP delegation (conscious arch debt)

Per #2d precedent: AG-01 is created in CARL VX with `Delegated_To=POP` flagged in Notes. POP doesn't have a KB.tsv yet — the eventual physical migration (KB-251 + AG-01 vector → POP workbook) is deferred until POP/KB.tsv standardization decision (separate ROADMAP thread).

---

## What WEALTH-01 measures (per reviewer Q4)

V14 (Upper-Decile Wealth Stress) is at score 3 (Watching) — a qualitative regime signal in the convergence matrix. To make it a vector, it needs a single measurable.

**Candidate metrics considered:**

| Metric | Source | Threshold structure | Verdict |
|---|---|---|---|
| SPX drawdown from highs | Daily market | -5% / -10% / -15% / -20% | Conflates with V14; mostly market beta |
| BofA fund flows (MMF outflow rate) | Weekly BofA/EPFR | bps of $24T equity AUM | Captured in KB-237; positioning regime, hard to threshold |
| Retail equity inflow rate | JPM weekly | -% WoW vs 4wk MA | Captured in KB-111; behavioral, noisy |
| **Prime CC NCO (AXP + DFS prime)** | Quarterly | Pre-pandemic ~1.8-2.5% baseline | **Selected** — earliest sign of upper-cohort credit cracking |
| Prime auto ABS spread (super-prime tranches) | Wells Fargo monthly | bps spread to baseline | Possible alternative; less liquid data |

**Selected metric:** Prime CC NCO Formation (AXP + DFS prime book).

**Rationale:** Per V14 definition (upper-decile wealth stress) and KB-091 explicit watch-list ("Track prime consumer credit metrics — Amex, Discover prime, prime auto ABS — for early sign of upper-income DQ formation"). When upper-K credit cracks, it shows up here first.

**Proposed bands [FLAG: uncertain — Will to review]:**

| Band | Threshold | Rationale |
|---|---|---|
| Green | <2.0% | Pre-pandemic AXP NCO baseline ~1.8-2.0% |
| Yellow | 2.0-2.5% | Currently Q1 2026 AXP/DFS in this range |
| Orange | 2.5-3.5% | Approaching cycle stress |
| Red | >3.5% | GFC AXP NCO peaked ~6%; >3.5% = upper-K stress confirmed |

**Anchor row pending:** Will be populated on next AXP/DFS quarterly print (Q2'26 reports, ~July 2026). For S2 CREATE, Current_Value="TBD on Q2'26 AXP/DFS earnings."

**Alternative:** if Will pushes back on Prime CC NCO as anchor, alternatives are SPX drawdown (less informative), or DEFER WEALTH-01 entirely (V14 stays qualitative in convergence matrix only).

---

## Orphan-Claim Audit Byproduct (per Q3 nuance)

When blanking dangling refs, surface KB rows whose continued ACTIVE status looks dependent on the linkage. **NOT applied as part of 2.5 mutations** — flagged here for separate review.

| KB | Issue | Recommendation |
|---|---|---|
| KB-013 | ICE 609K Nov 2025 single-month observation, currently ACTIVE with no Stale_By | Should likely be SUPERSEDED by KB-097 (Jan ICE) or KB-119 (Feb ICE); both supersede the Nov data point |
| KB-022 | Silver Tsunami 2025-2045 demographic forecast, ACTIVE with no Stale_By | 20-year horizon — needs explicit Stale_By or downgrade to ESTIMATE |
| KB-017 | F&F MBS Dec 2025, ACTIVE with no Stale_By | Broader narrative claim; verify still relevant or set Stale_By |
| KB-101 | Russia AN suspension Mar 24, ACTIVE with Stale_By 2026-06-30 | Verify whether suspension still in effect on next refresh; if resumed, mark SUPERSEDED |
| KB-094 | Already STALE (Mar 15 baseline); no action needed | — |
| KB-081 | Already STALE; no action needed | — |
| KB-102 | Unemployment Duration 25.7wk Feb 2026, ACTIVE Stale_By 2026-06-30 | Likely SUPERSEDED by Mar BLS print (LABOR domain — flag to LABOR) |

---

## Open questions for Will

1. **WEALTH-01 anchor metric** — accept Prime CC NCO (AXP/DFS) as the V14 measurable, or push back? If accepted, the [FLAG: uncertain] threshold bands above need your stress-test. If not, alternative is to defer WEALTH-01 (no CREATE; KB-237/111 still REMOVE).

2. **AG-01 POP delegation** — confirm conscious-arch-debt approach (CARL VX + Notes flag, defer physical migration to POP/KB.tsv decision)?

3. **K-01 scope on KB-154 (plasma)** — currently included as "behavioral leading indicator" partial fit. Acceptable, or would you rather K-01 strictly track BofA tier-spending-gap and remove KB-154?

4. **MACRO-05 dedupe direction** — proposed: NFP row → MACRO-09, PPI keeps MACRO-05 (zero KB.tsv changes). Approve?

5. **FOOD-01 supply-event sub-vector** — KB-101 Russia AN suspension currently REMOVE'd. Want a supply-event sub-vector class created in future for nitrogen/fertilizer shock events, or is the row standing alone fine?

6. **Orphan-Claim Audit Byproduct** — surface as a backlog ROADMAP entry, or fold into next mechanical KB hygiene pass? (Not blocking 2.5.)

---

## S2 mutation count estimate

| Action | Count |
|---|---|
| KB.tsv row mutations (REMOVE blank + REDIRECT swap) | ~33 unique rows touched, ~38 ref-edits total |
| VX.tsv appends (CREATE) | 9 rows |
| VX.tsv dedupe (MACRO-05 NFP rename) | 1 row edit |
| SCHEMA.tsv description edit | 1 row edit |
| **Total file mutations** | **~50 ref/row edits across 3 files** |

Backups required: KB.tsv, VX.tsv, SCHEMA.tsv (per `/tmp/...bak_2.5_{epoch}` convention).

Bug to watch: Item #2d Python list-by-reference issue — use deep copy or fresh row assembly per mutation (per plan §S2.1).

Post-S2 verification: re-run `/tmp/enum_2.5.py` → expect **0 dangling IDs / 0 edges**.

---

## Files affected by Session 2

| File | Edits |
|---|---|
| `workbook/KB.tsv` | ~33 rows (REMOVE blanks + 5 REDIRECTs) |
| `workbook/VX.tsv` | +9 rows (CREATE) + 1 dedupe rename |
| `workbook/SCHEMA.tsv` | 1 description edit |
| `workbook/AUDIT_2026-05-02.md` | Append Item #2.5 resolution log |
| `ROADMAP.md` | Move Item #2.5 OPEN → RECENTLY RESOLVED; add Orphan-Claim Audit Byproduct as backlog if approved (Q6) |
| `SCRATCH.md` | Rewrite per template |
| (separate S1 commit, already done) `CLAUDE.md` | WORKBOOK DISCIPLINE section added |

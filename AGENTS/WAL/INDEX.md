# WAL — Agent Index
**Start here on cold boot.** Standalone agent since **2026-07-25** (promoted from `AGENTS/REGINALD/WAL/`, Will-approved 7/22; review → `../DAEDALUS/builds/wal_promotion/PROMOTION_REVIEW.md`). Boot protocol → `CLAUDE.md` (auto-loads when launched from this dir).

⛔ **STRUCTURE CHANGED 2026-08-28 (read-cap hot/cold split, Will-approved):** `STATUS.md` **59.6 KB → 30.9 KB** and `MEMORY.md` **56.2 KB → 28.4 KB** — both now under the 32,550 B boot-read budget (root `CLAUDE.md` §Data Hygiene). **Cold halves are VERBATIM and sha-stamped: `STATUS_ARCHIVE.md`** (Q1-2026 print snapshot · V1/V2/V3 vector detail · MGMT outlook · research agenda · AOCI · RECENT CHANGES event log · resolved catalyst rows · session-header narrative) and **`MEMORY_ARCHIVE.md`** (session-#3/#4 handoffs · session-#4 findings). ⚠️ **COLD, not FROZEN — still true, still citable, just not boot-read.** Live vector state = `STATUS.md` §CONVERGENCE MATRIX; version/EV/PT = `THESIS.md`.

**Canonical tokens (MIRROR — sync at closeout, never originate here):**
**Thesis v2.4** (2026-08-20; `THESIS.md` owns it) · Bear-fast **2%** / Bear-medium **16%** / Base **45%** / Bull **30%** / Tail **7%** · **EV $75.96** · **PT $52-76** ([Bear-fast low, EV], pinned) · **WAL-01 25% / WAL-02 50%** OPEN to Q3 (`workbook/PREDICTIONS.tsv`, `Resolve_By` read at boot 4d) · **KB 218 rows / 20 Group values** (+1 10/9 s#12: 218 the hotel perimeter, segment vs property type; +2 10/9 s#11: 216 the hotel channel (WQ-328), 217 the Q3 print date) (+6 9/28 s#10: 215 the 9/28 re-base; 210 Jefferies letter primary, 211 tape, 212 rate sensitivity, 213 consensus snapshot, 214 FINRA SI; +1 9/27 s#9: KB-209 life-sci CRE base rate; +8 earlier 9/27 Nano Banc: 201-208) · **Positions: 1 leg** — Dec-18 $70P ×1 Robinhood, broker-verified 9/10; Sep-18 pair EXPIRED 9/18, broker-booked 9/27 at −$1,519.34 realized (`FORGE/STATUS.md` §RESOLVED, `f39c70073`) → `POSITIONS.md` · **Last close $76.55 [Mon 2026-09-28]** — **$1.45 below $78** (+1.89% Δ÷close to regain · −1.86% Δ÷threshold); spot **+2.17% vs EV** (was 0.47% BELOW on 9/23, first time this cycle) · `REG-T-02` FIRED 9/1 (cycle 2), exit `≥$81.90 ×3` **0-of-3 through 9/25** (REGINALD grades); sub-$78 closes are suppressed re-entries · ✅ **Q3 FRAMES WRITTEN 9/24**: print → `Q3_PRINT_GRADING_FRAME_2026-09-24.md` (L170) · 10-Q → `Q3_10Q_GRADING_FRAME_2026-09-24.md` (L171) · ⏱ $99M appraisal: weekly 8-K sweep, Q3 call MODAL · ⏱ **FFIEC JWT expires 11/5** (desktop) · ★ **Nano Banc 9/27: direct senior-lien link to Cantor collateral (KB-202) → `research/2026-09-27_nano-banc-receivership-stupin-recovery.md`; lien ownership AT FAILURE UNPROVEN (DEWEY 27b / CATO, 9/27)** · *Mirror re-synced 2026-09-27 (session #9 fold: KB count, Nano ownership-unproven, life-sci CRE; session #8); prior 2026-09-24 (session #7); the 9/2 token line is in git history (`399944561`). ⛔ Re-derive price figures from a named close, never carry.*

---

## Key Numbers (Q2 2026 — 7/21 AMC print + 7/22 call, graded off frozen frames)

| Metric | Value | Signal |
|--------|-------|--------|
| **Office classified** (V1b) | **$316M / 28% of classified — FALLING** vs $407M Q1 baseline [EX-99.2 slide 12 visual] | 🟢 broadening disconfirmed |
| **New office migrations Q2** | **0** (pass-grade-walk stays N=1) | 🟢 |
| **$99M life-sci walk-away** (B1) | Nonaccrual, **$0 charged off**, brought current end-June, **appraisal PENDING** | 🟠 the dated Q3 catalyst |
| **NCO ex-fraud** | 37bps annualized (25-40 NEUTRAL band; FY 25-35 guide reaffirmed, H2 "a little above midpoint") | 🟡 |
| **ACL ÷ nonaccrual** (funded + unfunded; the RETIRE-leg basis pinned 9/24) | **96% — below 100%** (full-NPL basis **69.1%**) | 🔴 |
| **CRE-NOO gross charge-offs** | $32.0M — 5-quarter high (grind signature, diluted in $58.7B book) | 🟠 |
| Special Mention | $316M (−$87M / −22% QoQ) | 🟢 |
| EPS / NIM | **$2.36 GAAP = $2.36 adjusted** ⬅ **A1-pinned at the 10-Q 8/7** (both non-GAAP adjustments are Q1-only, so no Q2 adjusted figure exists) / NIM 3.53% flat; CET1 11.0%. Revenue $995.7M (*below* Q1's $1.018B) | 🟢 base-case — the BASIS question is **dissolved** (KB-WAL-149). ⚠️ **The CONSENSUS remains contested 3 ways** ($2.33 / $2.36 / ~$2.37) and is **structurally unresolvable from any filing** — needs a dated vendor snapshot ≤2026-07-21 (KB-WAL-139) |
| **NDFI book** (8/7) | **$15,812M = 25.9% of HFI — a NEW HIGH share** (vs 25.2% at 3/31). All three sub-lines GREW QoQ; PE funds +15.6% | 🔴 **refutes KB-WAL-121's "shrinking" claim and V3's 1/5 rationale** — score held, re-exam proposed (KB-WAL-146). **9/28: KB-121 SUPERSEDED; V3 RE-SCORED 1/5 → 3/5 (WQ-324, CHANGELOG 9/28)** |
| **OREO** (8/7) | $126M but property **count 15 → 22 (+47%)**, "primarily **office**"; Q2 valuation losses **zero** | 🟠 WAL is taking title to office (KB-WAL-155) |
| **Capital-return pivot** | $5B loan guide cut "to prioritize share repurchases" + **$150M H2 buyback**; NII floor 12-14% absorbing an assumed Sept 25bp hike | 🟢 bull leg |
| Offsets carried | Fee guide cut 20-25%→13-17%; deposit-cost guide $8B→$6B | 🟠 |
| **V1a MI3** ⬅ ★★ **8/7** | **TESTED AT LAST — DISCONFIRMED.** Q1-26 **23.88%** · Q2-26 **21.20%**, both `<24%` PLATEAUED. **12 quarters: never once reached 25%** (high 24.24%, never within 76bps of its own trigger); oscillates with no trend since 2025Q1 | 🟢 **bear-fast KILL FIRED · time-box DISSOLVED.** ⚠️ **V1a ≠ V1** — the secured office book is untouched (KB-WAL-164/166/170) |
| Short interest | **5.97M shares short [FINRA 9/15] = 5.48% of shares outstanding** (~5.62% on the old float basis), days to cover **6.4**, the series high (KB-214; was 4.91% float at 6/30) — never cite boot-tool yfinance SI | 🟠 crowded short, MORE crowded than at the Q2 print |
| Spot vs model | ⏱ **$76.55 [9/28 close] vs EV $75.96 ⇒ spot +0.78% vs EV** (+2.17% at 9/25; 0.47% below on 9/23) — `STATUS.md` owns the live figure; *prior dated readings ($80.05 [8/20 intraday] 5.4%; $79.12 [9/2] 4.16%) are history* | 🟢 for the long side / ⚠️ **the short's margin of safety is gone** |

## Data Update Rules

| What Changed | Where to Update | Don't Touch |
|---|---|---|
| **A number/data point** | KB.tsv only (append; mark old via DerivedFrom) | THESIS.md |
| **Narrative/framing shift** | THESIS.md + CHANGELOG.md entry; bump version | KB.tsv |
| **New evidence arrives** | Add KB.tsv row → update MEMORY NEXT SESSION / this file's Open Threads | |
| **Probability re-weight** | THESIS.md + CHANGELOG.md (version bump) — THESIS owns the weights | SCENARIOS.md (ranges only) |
| **Sub-thesis (V2 fraud) state changes** | `FRAUD/FIRST_BRANDS.md` §FOLD (LAM/Jefferies) · `FRAUD/STUPIN_CRE.md` §FOLD (Cantor/Nano/Stupin) — FRAUD/STATUS.md + SYNTHESIS_V2.md stay bannered Q1-cycle records | KB.tsv (use new rows) |
| **Prediction grades** | `workbook/PREDICTIONS.tsv` — the TSV leg is named in every grading contract (PAT-053) | |
| **Session ending** | CLAUDE.md Session Close Checklist (incl. this file's token mirror-sync) | Frozen frames — content NEVER |

## Boot Sequence

| Order | File | What You Get |
|-------|------|-------------|
| 1 | `STATUS.md` | Dashboard: price, matrix, exit rules, catalysts, expected signals |
| 2 | `THESIS.md` **v2.4** + top `CHANGELOG.md` entry | Current framework + what last moved and why |
| 3 | `MEMORY.md` | Session handoff + first-boot mandates |
| 4 | `SCENARIOS.md` v2.4 | Ranges (⚠️ strike-by-strike sections May-vintage — rebuild owed) |
| 5 | `workbook/KB.tsv` + `KB_INDEX.md` | **209-row** evidence base (live count → line 7), 20 distinct Group values (**9/27 Nano Banc + DEWEY 201-208; life-sci CRE 209**; Q2 106-127; insider 128-133; news 134-139; Q1 10-Q primary 140-145; Q2 10-Q primary 146-163; MI3 first run 164-170; **8/20 catch-up 171-177**; 8/28 MI3-cohort 181-183; **9/2 tape+method 184-187**; **9/24 re-base + instrument 188-192; catalyst sweep 193-197; Cat-IV 198; 13F + share-count correction 199-200**) |
| 6 | `MI3_FIRST_RUN_2026-08-07.md` | The first-ever V1a MI3 grade + 12-quarter series + the KILL/time-box outcomes + P7-P10 |
| 7 | `Q2_10Q_READ_2026-08-07.md` | The Q2 10-Q primary read + **the frame-void record** + the v2.3.1 verdict + P1-P6 |

## File Map

### Core (read at boot)
| File | Description |
|------|-------------|
| `INDEX.md` | This file — start here |
| `CLAUDE.md` | Agent instructions — spawn protocol, closeout checklist, signal tables |
| `STATUS.md` | Live dashboard (≤250 ln) |
| `THESIS.md` v2.4 + `CHANGELOG.md` | Thesis + version-pinned audit trail |
| `SCENARIOS.md` v2.4 | Scenario branches + ranges |
| `workbook/KB.tsv` + `KB_INDEX.md` | Canonical evidence store + group navigator |
| `workbook/PREDICTIONS.tsv` | WAL-01/02 (formerly REG-24/25) + REG-15 (transferred 8/12, closed RESOLVED-FAILED 8/20) + future WAL predictions |
| `workbook/MI3_SERIES.tsv` | 12-quarter MI3 series (RCON2746 ÷ item 4) + NDFI item 9a, two-clock header. **Standing quarterly pull** — next Q3-2026 Call Report ~Oct-Nov |
| `POSITIONS.md` | Option legs (canonical; broker-data only) |
| `MEMORY.md` | Session handoff, Feedback, Findings |

### Frozen records (path fixes only — content NEVER edited)
| File | What it preserves |
|------|-------------|
| `Q2_GRADING_FRAME_2026-07-21.md` | Q2 pre-registration + Addendum A (W1-W13) — pre-print confidences 65/72/33 are the calibration record |
| `PREPRINT_RECON_2026-07-17.md` | Point-in-time recon (SI 4.91%, Street $2.33) |
| `EARNINGS_PREP.md` | Q1 pre-print frame (retrospective; template for future preps) |

### Sub-thesis (V2 Fraud → litigation arc)
| File | Description |
|------|-------------|
| `FRAUD/STATUS.md` + `FRAUD/SYNTHESIS_V2.md` | Q1-cycle records (bannered) — V2 RESOLVED in 8-K; forward thread = litigation |
| **Live:** `FRAUD/FIRST_BRANDS.md` (LAM/Jefferies §FOLD 9/24 + perfection screen) · `FRAUD/STUPIN_CRE.md` (Cantor §FOLD 9/24) · records bannered 9/24: `FRAUD/AUDITOR_NEXUS.md` · `AUDIT_COMMITTEE.md` · (`STATUS.md` / `SYNTHESIS_V2.md` riders) · **archived 9/24 → `archive/FRAUD/`:** CLASS_ACTION_FINDINGS · TRICOLOR · INVESTIGATION_ROADMAP · ZION_AUDIT_COMPARISON · GRANT_THORNTON_NEXUS · ISSUER_B_ELIMINATION · RSM_PUBLIC_AWARENESS | Pre/post-print fraud research (First Brands docket owner = OTTO; shared JEF node = `FORGE/research/jefferies/`) |

### Deep dives (on-demand)
`Q1_2026_ANALYSIS.md` (HELD 9/24 — `THESIS.md` travels it) · `WEAKNESSES.md` (steelman — `THESIS.md` owns the version) · `LEADERSHIP.md` (STALE-VINTAGE 3/31, kept — `THESIS.md` travels it) · `research/RQ-REG-A01_WAL_ZION_FRAUD_COMPARISON.md` · **Archived 2026-09-24 → `archive/`** (record `archive/RETIREMENT_SWEEP_2026-09-24.md`): `INVESTOR_DAY_FINDINGS_2026-05-12.md` + `_PREP` · `EXTERNAL_PROMPTS.md` · `TECHNICALS_20260401.md` · `AUDIT_MAR25.md` · `PRIOR_RESEARCH_EXTRACTS.md` · `V21_RESPONSE_TO_RED_CHG_025.md`

🗄️ **RETIRED 2026-08-23** (Will-approved sweep, amended root Data-Hygiene rule — record: `archive/RETIREMENT_SWEEP_2026-08-23.md`): `archive/TECHNICALS.md` · `archive/FORGE_STATUS.md` · `archive/MARKET/STATUS.md`. **Historical only, not maintained.** ⚠️ **This line is an INDEX-ref and under the amended rule an index-ref does NOT keep a file alive** — being listed here is not a reason to retain anything.

### Cross-agent
| File | Purpose |
|------|---------|
| `REGINALD_CHANNEL.md` | Pair log with REGINALD (ACK discipline) |
| `NEXUS_BRIEF.md` | Synthesis brief for NEXUS |
| `inbox/` · `outbox/` | Routed signals (+ `processed/` / `delivered/`) |

### Sources
`sources/` — primary extracts; `q*/` + `10k_*/` binaries local-only (gitignored), `.md` synthesis tracked · `MARKET/` — technicals snapshots (TRADE_LOG bannered — phantom-strike residue).

*Dead pointers struck 7/17 audit: `research/HIDDEN_CRE|JEFFERIES|SSFA/` never existed — V1 material → `../REGINALD/domain/sources/` + THESIS; V2 → `FRAUD/`; V3 → STATUS V3 table.*

## Open Threads (re-triaged session #1 2026-07-25; updated 2026-08-07; **last updated session #7 2026-09-24**)

1. ~~**Q2 KB ingest or freeze call**~~ — ✅ **CLOSED 7/25: INGESTED.** 22 rows (106-127) off the 8-K/EX-99.2/call; data clock 82d → 0d. Column-drift on 056/057 fixed in the same pass.
2. **Strike-by-strike position architecture rebuild** — SCENARIOS May-vintage sections (first-boot mandate, still open; forcing date now the Dec-18 $70P time stop 12/04 — one leg).
3. **Other LAM/Leucadia-era credits inventory** — call-transcript review done (Q2 clean twice, KB-WAL-124). ⚠️ **The DEF 14A pass is still NOT done — and the 2026 proxy was filed 2026-04-22 and has never been read** — *it is ALREADY ON DISK, zero fetch cost: `sources/q1_2026/14A.pdf` (gitignored, this box only; audit 9/28)* (our INSIDER rows predate it). It also carries the cash-settled-RSU plan terms behind KB-WAL-129 and the beneficial-ownership table.
4. **Cantor residual quarterly tracking** — *9/27-9/28: the live Cantor state is `FRAUD/STUPIN_CRE.md` §FOLD + the Nano file §9 (lien branches) and §10 (hearing read-sheet); the effective Q3 test is the 10-Q frame §8 (9/28 late: gross < $70.0M / net < $66.5M); dockets → thread 11.* ⬅ **PARTIALLY CLOSED 8/7.** The Q2 10-Q re-confirms the three primary figures ($98.5M facility / $29.6M specific allowance / $26.1M Q1 charge-off) and adds **"no additional charge-offs" in Q2** (KB-WAL-148). ⚠️ **But the Q2 disclosure is NARROWER than Q1's** — the $3.5M remaining allowance, the ~$70M residual carrying value and the $13M/$64M senior-lien position are all ABSENT. **Ledger tie-out still owed at the Q3 10-Q.** *(Candidate tie logged, not asserted: the Q2 MD&A's "$64 million of loans with more-than-insignificant deterioration" matches the protective-lien magnitude exactly.)*
5. **Lender-finance quality-of-names** (2,000 obligors) — V3 residual, unresolved since Q1. ⚠️ **PRIORITY RESTORED 8/7:** the "contracting by management choice" premise that justified deprioritising this **is refuted at the Q2 10-Q** — NDFI grew to **25.9% of HFI (a new high)** with all three sub-lines up QoQ (KB-WAL-146). ~~V3's 1/5 is under challenge~~ V3 re-scored to 3/5 on 9/28 (WQ-324); the quality-of-names question is live again.
6. ~~**MI3/FFIEC**~~ — ✅ **CLOSED 2026-08-07. The pull ran; MI3 graded DISCONFIRMING on both 2026 quarters + 10 of history.** The 7/25 hunch was right — WAL's own Call Report is directly retrievable — but the recorded recipe was **SOAP-vintage and dead** (legacy tokens expired 2/28/26); the live service is **REST + JWT**, header literally `Authentication:`. **Successor threads:** (a) ⏱ **JWT expires 11/5 — INSIDE the Q3 Call Report / Q3 10-Q window** (Call Reports due 10/30), not merely before the Q4 report — Will-side regeneration, WILL_QUEUE row 31, raise ~10/13; (b) `.env` creds are on the **DESKTOP only** (`DESKTOP-BC6EF81`); the laptop cannot pull MI3 *(this line had the machines reversed until 9/24)*; (c) **peer-cohort MI3 is now cheap** — the same call for the comparison set would settle whether 21.20% is high or low vs peers (**REGINALD's lane**, flagged to them); (d) UBPR percentiles still unexplored.
7. ~~**Form 4 post-print insider sweep**~~ — ✅ **CLOSED 7/25.** Complete EDGAR Form 4/144 scan 3/1-7/25 → `sources/INSIDER_SCAN_WAL_2026-07-25.md`, KB-WAL-128..133. Zero buying confirmed; V4 ratified 3/5. **Converted to a standing monthly watch — and Form 144 must be pulled with Form 4** (a departing officer's liquidation is invisible to Form 4 alone).
8. **EPS basis tie-out** — ✅ **CLOSED 8/7 on the basis leg, OPEN on the consensus leg.** The 10-Q pins Q2 **GAAP = adjusted = $2.36** (both non-GAAP adjustments are Q1-only), so the basis fork that made Q1 ambiguous does not exist at Q2 (KB-WAL-149). **The consensus leg cannot be closed by any filing** — it needs a dated vendor snapshot on-or-before 2026-07-21.
9. ~~**WAL-02 invalidation-clause defect**~~ ✅ **RULED 8/12 (Will, batch row 32b) + REPAIRED 8/20 (P3).** Invalidation re-pointed to an exhaustive Q3-only partition: **>40bps CONFIRMED / ≤40bps INVALIDATED** — no undefined band remains. Confidence unmoved at 50% (rider R3). Historical framing follows: HARDENED 8/7. The 37bps that makes the invalidation unreachable is now **A1-confirmed at the 10-Q** (Q2 NCO $55.0M = 0.37%, and zero fraud charge-offs in Q2, so total = ex-fraud) — KB-WAL-158. Row still 50%/OPEN, spec **unedited** (graded row); a dated note-only append was added to the TSV.
9b. ~~**WAL-01 bucket + carrying-instrument defect**~~ ✅ **RULED 8/12 + RE-INSTRUMENTED 8/20 (P2).** The VOID "Q3 10-Q Schedule O" cite is struck and NOT replaced by another 10-Q reference (no 10-Q publishes classified-by-property-type at all); the rule now names the **Q3 deck "Classified Assets Mix" slide** at its true A2-visual tier, with a 10-Q total-classified cross-check and an explicit **NO-VERDICT / INSTRUMENT-ABSENT** band. ⚠️ **The $99M bucket ambiguity is NOT resolved and is not required to be.** Historical framing follows: ESCALATED 8/7. The tie-out meant to resolve it **widened** it: three candidate buckets (Office / Life sciences / **Construction & land dev**), **no 10-Q publishes office-classified at all**, and the spec's "Q3 10-Q **Schedule O**" names a *Call Report* schedule that does not exist in a 10-Q (KB-WAL-150/151).
11. **Court-docket monitoring** — ⚠️ **re-triaged 9/28 (audit): the Cantor arc now has at least 8 live dockets, not 3.** Read so far: Stupin Ch.11 8:26-bk-11202-SC schedules (KB-208) · adversary 8:26-ap-01076-SC Doc 1 only (remand motion 7/27 — outcome UNCHECKED) · Plaza Continental 8:26-bk-10986 (hearing 9/29 → read-sheet, research §10) · Makhijani 8:26-cr-00087-DOC (trial 1/12/2027, status conf 11/30) · Marcil v. Nano 8:26-cv-01143 (KB-207). **Still unwatched:** NYSCEF — **no index number held for WAL v. Jefferies or the Jefferies countersuit**; LA Superior portal (Cantor V claims + receiver Neilson/Trigild sales); a claim objection to WAL's $173.0M claim in the Stupin case. *Original 7/25 text follows:* (a) WAL v. Jefferies/LAM, NY Supreme (NYSCEF is free) · (b) **Jefferies v. WAL, NY state, filed ~7/1 — we did not know it existed** (KB-WAL-135) · (c) WAL v. Cantor Group V, **LA Superior 25STCV24263** (KB-WAL-137). Forward V2 is entirely litigation and we run blind on dockets; entries lead the 10-Q footnote by weeks.
12. **$99M property — no pre-filing instrument** ⬅ **NEW 7/25.** The appraisal is our most-dated catalyst with no carrying filing. If the property can be identified, county records (NOD / deed / lease memoranda) would fire before any SEC filing — and mgmt says a prospective tenant is evaluating space, which would leave a recorded lease trail.
13. ✅ **13F LAYER RUN 2026-09-24** → `research/Q2_13F_AGGREGATE_2026-09-24.md` (KB-199): 13F ownership **84.7% → 90.0%** (3/31 → 6/30), AQR +4.24M = 74% of the net; T. Rowe's 13G trim was 92% in Q2. ⚠️ **Share count was FLAT in Q2 (−0.08%, 10-Q covers, KB-200)**; the 8/20 "implied −1.7%" was 13G rounding noise and is retired. *(8/20 13G layer: T. Rowe −20.8%→5.8%; Invesco re-crossed +12.5%→5.4%.)*
10. ~~Synthesis-files gitignore decision~~ — RESOLVED: all `.md` synthesis tracked; ignore semantics carried to `AGENTS/WAL/` at promotion (WP-W1, 7/25).

---

*Standalone agent | Domain: Western Alliance Bancorporation (NYSE: WAL) | Hub: REGINALD at `../REGINALD/` (cohort/regime — pointer-only seam, no restated figures) | Peer: OZK at `../OZK/` (separate single-name thesis) | Promotion: 2026-07-25, `../DAEDALUS/builds/wal_promotion/`*

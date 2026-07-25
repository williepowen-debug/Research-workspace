# WAL — Agent Index
**Start here on cold boot.** Standalone agent since **2026-07-25** (promoted from `AGENTS/REGINALD/WAL/`, Will-approved 7/22; review → `../DAEDALUS/builds/wal_promotion/PROMOTION_REVIEW.md`). Boot protocol → `CLAUDE.md` (auto-loads when launched from this dir).

**Canonical tokens (MIRROR — sync at closeout, never originate here):**
**Thesis v2.3** (2026-07-25, post-Q2 re-mark) · Bear-fast 10% / Bear-medium 16% / Base 40% / Bull 27% / Tail 7% · **EV $73.92** · **PT $52-74** ([Bear-fast low, EV], pinned) · **WAL-01 25% / WAL-02 50%** (formerly REG-24/25, OPEN to Q3 — WAL-02's Q2 window SPENT at 37bps) · KB **145 rows / 16 groups** (Q2 cycle + insider sweep + news sweep + Q1 10-Q primary pull, all 7/25; data clock 0d) · Positions → `POSITIONS.md` (Sep-18 $67.5P + $70P core) · **Next event: Q2 10-Q ~Aug 7-10**, then FFIEC Q2 PDD ~Aug

---

## Key Numbers (Q2 2026 — 7/21 AMC print + 7/22 call, graded off frozen frames)

| Metric | Value | Signal |
|--------|-------|--------|
| **Office classified** (V1b) | **$316M / 28% of classified — FALLING** vs $407M Q1 baseline [EX-99.2 slide 12 visual] | 🟢 broadening disconfirmed |
| **New office migrations Q2** | **0** (pass-grade-walk stays N=1) | 🟢 |
| **$99M life-sci walk-away** (B1) | Nonaccrual, **$0 charged off**, brought current end-June, **appraisal PENDING** | 🟠 the dated Q3 catalyst |
| **NCO ex-fraud** | 37bps annualized (25-40 NEUTRAL band; FY 25-35 guide reaffirmed, H2 "a little above midpoint") | 🟡 |
| **ACL/NPL coverage** | **96% — below 100%** | 🔴 |
| **CRE-NOO gross charge-offs** | $32.0M — 5-quarter high (grind signature, diluted in $58.7B book) | 🟠 |
| Special Mention | $316M (−$87M / −22% QoQ) | 🟢 |
| EPS / NIM | $2.36 / NIM 3.53% flat; AOCI −$451M improved +$5M; CET1 11.0%. Revenue $995.7M (*below* Q1's $1.018B) | 🟢 base-case — ⚠️ **but the CONSENSUS is contested 3 ways** ($2.33 beat / $2.36 meet / ~$2.37 slight miss). Tie out at the Q2 10-Q (KB-WAL-115/139) |
| **Capital-return pivot** | $5B loan guide cut "to prioritize share repurchases" + **$150M H2 buyback**; NII floor 12-14% absorbing an assumed Sept 25bp hike | 🟢 bull leg |
| Offsets carried | Fee guide cut 20-25%→13-17%; deposit-cost guide $8B→$6B | 🟠 |
| **V1a MI3** | **NEVER TESTED** — FFIEC PDD un-run ~2.5mo | ⬜ unknown both directions |
| Short interest | 4.91% float [FINRA 6/30] — never cite boot-tool yfinance SI | 🟠 crowded short |
| Spot vs model | **$83.11** [7/24 close] **above Base top $82** → base case still implies decline; overvaluation 12.4% vs EV. Sell-side PTs post-Q2 ($90 JPM / $98 Citi) sit ABOVE our EV | — |

## Data Update Rules

| What Changed | Where to Update | Don't Touch |
|---|---|---|
| **A number/data point** | KB.tsv only (append; mark old via DerivedFrom) | THESIS.md |
| **Narrative/framing shift** | THESIS.md + CHANGELOG.md entry; bump version | KB.tsv |
| **New evidence arrives** | Add KB.tsv row → check off STATUS.md research agenda | |
| **Probability re-weight** | SCENARIOS.md (+ CHANGELOG if version-worthy) | THESIS.md (unless framework breaks) |
| **Sub-thesis (V2 fraud) state changes** | FRAUD/STATUS.md + SYNTHESIS_V2.md (both bannered as Q1-cycle records — new state = new dated section) | KB.tsv (use new rows) |
| **Prediction grades** | `workbook/PREDICTIONS.tsv` — the TSV leg is named in every grading contract (PAT-053) | |
| **Session ending** | CLAUDE.md Session Close Checklist (incl. this file's token mirror-sync) | Frozen frames — content NEVER |

## Boot Sequence

| Order | File | What You Get |
|-------|------|-------------|
| 1 | `STATUS.md` | Dashboard: price, matrix, exit rules, catalysts, expected signals |
| 2 | `THESIS.md` **v2.3** + top `CHANGELOG.md` entry | Current framework + what last moved and why |
| 3 | `MEMORY.md` | Session handoff + first-boot mandates |
| 4 | `SCENARIOS.md` v2.3 | Ranges (⚠️ strike-by-strike sections May-vintage — rebuild owed) |
| 5 | `workbook/KB.tsv` + `KB_INDEX.md` | 145-row evidence base, 16 groups (Q2 106-127; insider 128-133; news 134-139; 10-Q primary 140-145) |

## File Map

### Core (read at boot)
| File | Description |
|------|-------------|
| `INDEX.md` | This file — start here |
| `CLAUDE.md` | Agent instructions — spawn protocol, closeout checklist, signal tables |
| `STATUS.md` | Live dashboard (≤250 ln) |
| `THESIS.md` v2.3 + `CHANGELOG.md` | Thesis + version-pinned audit trail |
| `SCENARIOS.md` v2.3 | Scenario branches + ranges |
| `workbook/KB.tsv` + `KB_INDEX.md` | Canonical evidence store + group navigator |
| `workbook/PREDICTIONS.tsv` | WAL-01/02 (formerly REG-24/25) + future WAL predictions |
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
| `FRAUD/AUDITOR_NEXUS.md` · `AUDIT_COMMITTEE.md` · `CLASS_ACTION_FINDINGS.md` · `STUPIN_CRE.md` · `FIRST_BRANDS.md` · `TRICOLOR.md` · `INVESTIGATION_ROADMAP.md` · `ZION_AUDIT_COMPARISON.md` · `RSM_PUBLIC_AWARENESS.md` · `ISSUER_B_ELIMINATION.md` | Pre/post-print fraud research (First Brands docket owner = OTTO; shared JEF node = `FORGE/research/jefferies/`) |

### Deep dives (on-demand)
`Q1_2026_ANALYSIS.md` · `INVESTOR_DAY_FINDINGS_2026-05-12.md` + `_PREP` · `WEAKNESSES.md` (v2.3 steelman) · `EXTERNAL_PROMPTS.md` · `TECHNICALS*.md` · `LEADERSHIP.md` · `AUDIT_MAR25.md` · `FORGE_STATUS.md` · `PRIOR_RESEARCH_EXTRACTS.md` · `V21_RESPONSE_TO_RED_CHG_025.md` · `research/RQ-REG-A01_WAL_ZION_FRAUD_COMPARISON.md`

### Cross-agent
| File | Purpose |
|------|---------|
| `REGINALD_CHANNEL.md` | Pair log with REGINALD (ACK discipline) |
| `NEXUS_BRIEF.md` | Synthesis brief for NEXUS |
| `inbox/` · `outbox/` | Routed signals (+ `processed/` / `delivered/`) |

### Sources
`sources/` — primary extracts; `q*/` + `10k_*/` binaries local-only (gitignored), `.md` synthesis tracked · `MARKET/` — technicals snapshots (TRADE_LOG bannered — phantom-strike residue).

*Dead pointers struck 7/17 audit: `research/HIDDEN_CRE|JEFFERIES|SSFA/` never existed — V1 material → `../REGINALD/domain/sources/` + THESIS; V2 → `FRAUD/`; V3 → STATUS V3 table.*

## Open Threads (re-triaged by owner at session #1, 2026-07-25)

1. ~~**Q2 KB ingest or freeze call**~~ — ✅ **CLOSED 7/25: INGESTED.** 22 rows (106-127) off the 8-K/EX-99.2/call; data clock 82d → 0d. Column-drift on 056/057 fixed in the same pass.
2. **Strike-by-strike position architecture rebuild** — SCENARIOS May-vintage sections (first-boot mandate, still open; Sep-18 expiry is the forcing date).
3. **Other LAM/Leucadia-era credits inventory** — call-transcript review done (Q2 clean twice, KB-WAL-124). ⚠️ **The DEF 14A pass is still NOT done — and the 2026 proxy was filed 2026-04-22 and has never been read** (our INSIDER rows predate it). It also carries the cash-settled-RSU plan terms behind KB-WAL-129 and the beneficial-ownership table.
4. **Cantor residual quarterly tracking** — three-figure reconcile RESOLVED at Q2 (KB-WAL-123: $98.6M revolver / ~$70M residual / $64M protective liens = distinct bases). **Ledger tie-out still owed at the Q3 10-Q footnote.**
5. **Lender-finance quality-of-names** (2,000 obligors) — V3 residual, unresolved since Q1. *Lower priority post-Q2: V3 re-scored 2→1, the book is contracting by management choice (KB-WAL-121).*
6. **MI3/FFIEC — ★ the premise may be wrong.** We have been waiting ~2.5mo on a *fleet-level PDD integration*; the 7/25 news sweep notes **WAL's own Call Report is directly downloadable from the FFIEC CDR** (+ a free UBPR for peer percentiles). **Try the direct pull before the ~Sep 1 time-box trips.** Highest-leverage open item on the board — it resolves a 10% weight either direction.
7. ~~**Form 4 post-print insider sweep**~~ — ✅ **CLOSED 7/25.** Complete EDGAR Form 4/144 scan 3/1-7/25 → `sources/INSIDER_SCAN_WAL_2026-07-25.md`, KB-WAL-128..133. Zero buying confirmed; V4 ratified 3/5. **Converted to a standing monthly watch — and Form 144 must be pulled with Form 4** (a departing officer's liquidation is invisible to Form 4 alone).
8. **EPS basis tie-out** — ⬅ **NEW.** The $2.36/$2.33 Q2 EPS pair is sourced only to the CHANGELOG v2.3 entry, appears in neither grade report, and its GAAP-vs-adjusted basis is unpinned (KB-WAL-115). Tie out to EX-99.1 at the Q2 10-Q pass.
9. **WAL-02 invalidation-clause defect** — ⬅ **NEW, awaiting Will's call.** The stated invalidation ("≤35bps in BOTH Q2 and Q3") became unreachable when Q2 printed 37bps. Row otherwise fine at 50%. Not edited unilaterally — it is a graded row.
11. **Court-docket monitoring — NOT SET UP for any of three live matters** ⬅ **NEW 7/25.** (a) WAL v. Jefferies/LAM, NY Supreme (NYSCEF is free) · (b) **Jefferies v. WAL, NY state, filed ~7/1 — we did not know it existed** (KB-WAL-135) · (c) WAL v. Cantor Group V, **LA Superior 25STCV24263** (KB-WAL-137). Forward V2 is entirely litigation and we run blind on dockets; entries lead the 10-Q footnote by weeks.
12. **$99M property — no pre-filing instrument** ⬅ **NEW 7/25.** The appraisal is our most-dated catalyst with no carrying filing. If the property can be identified, county records (NOD / deed / lease memoranda) would fire before any SEC filing — and mgmt says a prospective tenant is evaluating space, which would leave a recorded lease trail.
13. **Never examined:** 13F/13G institutional flow (3 events in 2026; Q2 13Fs ~Aug 14) · FR Y-9C as a second instrument on CRE/NDFI · life-science lab-market vacancy data as the appraisal base rate · Federal Register watch on the AOCI Cat III/IV rule (STATUS carries it as "pending" with no instrument).
10. ~~Synthesis-files gitignore decision~~ — RESOLVED: all `.md` synthesis tracked; ignore semantics carried to `AGENTS/WAL/` at promotion (WP-W1, 7/25).

---

*Standalone agent | Domain: Western Alliance Bancorporation (NYSE: WAL) | Hub: REGINALD at `../REGINALD/` (cohort/regime — pointer-only seam, no restated figures) | Peer: OZK at `../OZK/` (separate single-name thesis) | Promotion: 2026-07-25, `../DAEDALUS/builds/wal_promotion/`*

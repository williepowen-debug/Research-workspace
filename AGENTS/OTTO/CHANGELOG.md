# OTTO Thesis CHANGELOG

Audit trail of **thesis/POV pivots** — every material change in OTTO's view, logged
old → new with a date and trigger. This is the trajectory record that STATUS-narrative
pruning would otherwise destroy (per auto-memory `[[finding_pov_changelog_pattern]]`).

**Scope:** analytical/thesis changes only — conviction shifts, mechanism reframes,
prediction-confidence moves of note, new transmission rows, case-status escalations.
NOT routine dashboard refreshes (those live in STATUS) and NOT structural doc/folder
changes (no separate MAINTENANCE log yet — candidate if structural churn grows).

**Versioning:** OTTO's live thesis currently lives in `STATUS.md` (§ THESIS), not a
versioned `thesis/THESIS.md`. Until that graduates, this log is dated-entry only — no
version tags. When/if the thesis moves to its own folder, this file moves with it.

**Format:** reverse-chronological. Each entry: `### YYYY-MM-DD — headline`, then
**Was → Is**, then **Trigger** (what evidence forced it), then **Touches** (which
docs/predictions moved).

---

### 2026-06-08 — ABS structural claim falsified + OTTO-05 recalibrated (data refresh)
- **Was:** Subprime ABS market "IG-only — BB/single-B tranches not clearing" (structural 🟠); BBB spread extrapolated ~200-235bps; OTTO-05 (BBB >250 by Jun 30) at 62%.
- **Is:** **Below-IG IS clearing** — Exeter EART 2026-2 placed BB- (+380) and single-B (+320) tranches publicly (Mar 20, SEC FWP). Direct BBB print **+190bps** (EART Class D) sits *below* the extrapolation. OTTO-05 dropped 62 → 48% (needs +60bps in 3wk absent a fresh catalyst). "IG-only" claim retired.
- **Trigger:** Jun 8 dashboard data-refresh sweep — primary-source SEC FWP for EART 2026-2 superseded OTTO's hand-extrapolated spread levels.
- **Touches:** OTTO-05 (62→48%); STATUS SIGNAL DASHBOARD (3 spread rows); issuance row 🟠→🟢-reframed. Calibration note: OTTO had been over-extrapolating BBB off A-rated + a too-wide BBB-over-A premium.

### 2026-06-08 — First Brands OTTO-32 resolver: Jun 17 → Jun 12
- **Was:** OTTO-32 (First Brands majority Ch.7) resolver = Jun 17 plan-confirmation hearing.
- **Is:** Operative resolver is the **Jun 12 UST convert-or-dismiss hearing** (10am CT, §1112(b)). May 20 DS denied (entanglement + <14d creditor review + admin-insolvency); Jun 17 confirmation is now *contingent on surviving Jun 12*. Conviction unchanged (85%) — only the resolver date/mechanism moved earlier.
- **Trigger:** Jun 8 catalyst-prep sweep (Law360 #2482099 / Octus) — surfaced the §1112(b) hearing OTTO's timeline had folded into "Jun 17."
- **Touches:** OTTO-32 Notes; STATUS CRITICAL TIMELINE + signal-trigger; CATALYSTS.tsv (new Jun 12 row, Jun 17 re-characterized).

### 2026-06-02 — First Brands Ch.7: IN MOTION → ADVANCING
- **Was:** Ch.7 conversion "in motion" (US-Trustee dismiss-or-convert motion filed May 13).
- **Is:** Mechanism **advancing** — 4 Evolution SPV debtors already converted (Apr 9 Lopez order); PMG plan routes all other 111 debtors to Ch.7; May 20 conditional-DS approval DENIED on admin-insolvency grounds (the denial basis = UST's outright-conversion argument, so it cuts *toward* thesis). Confirmation re-targeted Jun 17.
- **Trigger:** First Brands docket sweep (Jun 2) — Law360 / CreditSights cleared the auth-gated Kroll docket.
- **Touches:** OTTO-32 held 85%; STATUS CRITICAL TIMELINE; ML-OTTO-171.

### 2026-05-22 — Wilmington Trust: franchise-exit thesis collapses to narrow Tricolor resignation
- **Was:** 🔴🔴 "Wilmington exiting its entire non-mortgage ABS custodial business" (billions in ABS); OTTO-31 opened 60%.
- **Is:** 🟠 narrow — only the **Tricolor-specific** indenture-trustee resignation (Sep 20 2025) is corporate-confirmed. Full-exit allegation **denied corporate-side** (American Banker, M&T anon source: unit "is accepting new clients") + active-business evidence (#2 US ABS/MBS trustee 1H 2025). OTTO-31 dropped 60 → 30%.
- **Trigger:** May 22 PM corporate-side sweep. Plaintiff allegation = litigation rhetoric, not franchise exit.
- **Touches:** OTTO-31 (60→30%); STATUS active vectors (split into Wilmington-narrow + successor-vacuum rows); auto-memory `[[finding_refresh_not_retire_perentity_profiles]]`-adjacent calibration lesson (weight `[ALLEG]` ≤40%).

### 2026-05-21 — Tricolor recovery: deadline + magnitude corrected
- **Was:** Vehicle-sale deadline Apr 30 (per Apr 15 recalibration); recovery outcome open.
- **Is:** Operative deadline was **Mar 31** (no extension); auctions ran; ~3% recovery projected (5,857 vehicles / $39.5M net); **~30K vehicles missing, up to $1.1B** (Invisible Exit at industrial scale); $113M distribution gridlock = new transmission mechanic.
- **Trigger:** May 21 sourced docket + AFN auction-proceeds reporting superseded the Apr 15 recalibration.
- **Touches:** OTTO-29 raised to 80% (substance) but flagged resolution-at-risk; STATUS dashboard + thesis blocks; ML-OTTO-145 supersedes ML-OTTO-140.

### 2026-04-15 — Recovery-signal metric reframed: vehicle proceeds → ABS note price
- **Was:** "Recovery outcome" framed around vehicle auction proceeds ($125M cost-basis ceiling).
- **Is:** The signal-rich metric is **ABS note market price** (already <10¢ on the dollar = >90% implied noteholder loss), not vehicle proceeds. The question was mis-framed.
- **Trigger:** Apr 15 Tricolor recovery deep-dive; Will wanted the reframe said plainly before the data.
- **Touches:** Cockroach magnitude strengthened; Invisible Exit structurally validated.

---

*Seeded 2026-06-08 from STATUS/MEMORY trajectory at CHANGELOG introduction. Pre-2026-04 pivots not backfilled — reference STATUS archive + ML.tsv if needed.*

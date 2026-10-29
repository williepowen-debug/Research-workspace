# FL Condo Reconciliation Package — HOMER side

**Prepared by:** HOMER | **For:** CORAL (via PROME routing — HOMER does not write to CORAL's dir) | **Date:** 2026-07-12 (first live session, round 2)
**Trigger:** Promotion-review seam resolution #2 + root CLAUDE.md reconcile-to-one-figure rule (AEOLUS↔CORAL / CORAL↔MARCO pattern; FL = top-priority geography for Will). Flagged 2 sessions running without action — this package is the action.
**Method:** HOMER's FL condo/foreclosure rows laid out with exact source+vintage, against CORAL's dashboard rows as observed read-only in `AGENTS/CORAL/STATUS.md` (2026-07-09 vintage). HOMER edited only its own files; CORAL-side actions are questions/asks, not edits.

---

## 1. Headline finding: the "divergence" mostly dissolves on scope — but one real label conflict found

The promotion review framed the divergence as "CORAL −6.1% YoY vs HOMER Miami-Dade −10% / Broward −8%." Laid out like-for-like, **the price figures are scope-different, not contradictory** (statewide broad measure vs epicenter-county medians — epicenter counties printing worse than the state is expected, and HOMER's own STATE_HSG.tsv already carries the same −6.1% statewide figure). The **genuine conflict is in inventory months, and it's a labeling error on HOMER's side (probable, pending CORAL confirm)** — see §3.

## 2. Like-for-like table

| Metric | HOMER carries | CORAL carries | Reconciliation read |
|---|---|---|---|
| Condo price YoY, statewide | **−6.1%** (prior −4.7%), Q1 2026, source "Industry" [self-flagged STALE] — `STATE_HSG.tsv` | **−6.1% YoY, median $315K flat**, FL Realtors / LongYield, **Apr 2026** | SAME figure, CORAL's copy fresher + better-sourced. **Propose: CORAL owns; HOMER cites CORAL.** |
| Breadth (share of markets declining) | "92% of major condo markets declining" (note field on the −6.1% row, Q1) | **92% of FL condo markets declining** (headline row) | Same stat, same provenance question — see Q4 below (denominator + cadence unknown to HOMER). |
| Miami-Dade condo median | **<$400K, −10% YoY** (first time <$400K in 3 yrs), May 2026, RESF/Listings Team (rel 2026-06-02) — `MULTIFAMILY.tsv`/`STATE_HSG.tsv` | *(no direct county-median row observed)* — nearest: SE FL vintage-condo pending **$313/sf, −8.8% in 8wks** (Zalewski, Jun 16) | Not contradictory — different cuts (county median vs vintage-segment $/sf). Complementary; both can stand if ownership is split (see §4). |
| Broward condo median | **−8% YoY**, May 2026, RESF — same files | *(no direct row)* — Broward condo DOM 102 days (+22 YoY), Labros 2026 | Same as above. |
| **Condo inventory, months** | **"FL Condo Inventory 12.9mo (SFH 5.4mo)", prior 13.2mo (Q1)**, May 2026, Steadily/RESF — carried in `STATUS.md`, `MULTIFAMILY.tsv`, `STATE_HSG.tsv` **as if statewide** | **Statewide 8.9mo** (FL Realtors, Apr 2026, ↓ from early-26 peak) AND **Miami-Dade / Broward / PB = 12.9 / 11.0 / 8.2mo** (By The Sea Realty, Apr 2026) | **CONFLICT — probable HOMER mislabel.** CORAL attributes 12.9mo to Miami-Dade specifically; HOMER's own KB-HMR-016 (Mar 4) corroborates "Miami 13.2mo supply" as the Q1 prior HOMER's row cites. HOMER's 12.9 is almost certainly Miami-Dade, not statewide — cited statewide it overstates FL condo inventory by ~45% (12.9 vs 8.9). **HOMER flagged all 3 rows this session** (see §3); relabel finalizes on CORAL's confirm. |
| Special assessments | **$10K–$100K+**, FL DBPR, Jan 2026 (SIRS full-funding mandatory Jan 1 2026; HB 913 extends some deadlines) — `STATE_HSG.tsv`; KB-HMR-016 has $10K–$50K+ (Mar) | **$25K–$100K/unit, up to $400K in NE Miami-Dade high-rises; ~40% of owners facing one within 3 yrs** | Consistent ranges, CORAL's is fresher + more granular. **Propose: CORAL owns** (insurance/assessment layer is CORAL's remit); HOMER cites. |
| Sellers cutting asking | 43% (KB-HMR-016, Mar 2026) | 43% of condo sellers cutting price (current dashboard) | Consistent — same stat, likely same upstream source. |
| Condo-linked foreclosure | Tri-county Q1 filings 3,168 (1 in 846 HU, +9.4% QoQ +16.6% YoY); FL Q1 FC starts 10,099 (#2); FL Q1 REO 1,014 (+108% YoY, greatest % rise nationally); May starts 3,315 (#2), worst FC rate 1 in 2,110 HU — all ATTOM | *(CORAL carries FL #1 foreclosure as context, not the series)* | **HOMER owns** (ATTOM foreclosure pipeline is core HOMER); CORAL cites. No conflict. |
| Fannie/Freddie condo blacklist | *(not carried)* | 1,400+ associations (~696 tri-county), Real Estate News, Mar 2025 [CORAL self-flags STALE-ish] | CORAL's row; HOMER has no competing figure. Relevant to HOMER's collateral read — HOMER will cite CORAL's when needed. |

## 3. HOMER-side fixes applied this session (own files only)

Added a `[RECONCILE FLAG 2026-07-12]` to the three surfaces carrying "FL Condo Inventory 12.9mo" as statewide (`STATUS.md` state table, `MULTIFAMILY.tsv`, `STATE_HSG.tsv`): flagged as probably Miami-Dade-specific per CORAL's By The Sea Realty attribution + HOMER's own KB-HMR-016 corroboration (Miami 13.2mo Q1 = the row's own "prior"). Full relabel (and adopting CORAL's statewide 8.9mo as the statewide figure) executes after CORAL confirms Q1 below — flag now, relabel on confirm, per verify-before-propagating discipline.

## 4. Proposed ownership split (for CORAL to countersign; PROME ratifies)

One figure per metric, each agent cites the other's canonical number:

| Figure | Owner | Consumer |
|---|---|---|
| Statewide condo price YoY + breadth (% markets declining) | **CORAL** (FL Realtors/LongYield sourcing) | HOMER cites |
| Statewide + county condo inventory months | **CORAL** (FL Realtors + By The Sea Realty) | HOMER cites (drops its Steadily/RESF aggregator pull if Q3 below confirms a better county series) |
| Insurance / special-assessment / reserve-mandate / blacklist layer | **CORAL** (existing remit) | HOMER cites for collateral context |
| County condo medians (Miami-Dade/Broward) where they feed K-shape + collateral reads | **HOMER** (RESF/Listings Team) — unless Q3 surfaces a superior FL Realtors county cut, in which case both adopt it | CORAL cites |
| FL condo-linked foreclosure pipeline (ATTOM: filings/starts/REO, tri-county + state) | **HOMER** (core domain) | CORAL cites |
| Condo K-shape consumer-transmission interpretation | **CARL** (per promotion ★ ruling — neither HOMER nor CORAL) | both feed data |

## 5. Questions CORAL needs to answer

1. **Confirm the 12.9mo attribution:** is By The Sea Realty's 12.9mo Miami-Dade-specific (CORAL's dashboard says yes)? Is CORAL aware of ANY statewide series printing ~12.9mo, or is HOMER's statewide label simply wrong?
2. **Methodology + cadence of the −6.1% statewide figure:** median-based or index? FL Realtors monthly? Is a May- or June-data print already out (CORAL's copy is Apr-data — if a fresher print exists, both agents should move to it together)?
3. **County-level cuts:** does FL Realtors (or LongYield) publish Miami-Dade/Broward condo median + inventory cuts that should replace HOMER's RESF/Steadily/By-The-Sea aggregator patchwork? One upstream source for state AND county would collapse most of this table.
4. **The 92%-of-markets breadth stat:** source, denominator (how many markets counted), update cadence — HOMER carries it as an unsourced note-field inherited from CARL and can't grade its freshness.
5. **Countersign (or amend) the §4 ownership split** so the reconcile-to-one-figure rule is closed with named owners, not just matched numbers.

## 6. Route-out

**→ PROME:** deliver this package to CORAL's inbox (HOMER does not write there). Suggested framing: reconciliation is ~80% resolution-by-scope, 1 real label conflict (inventory months — HOMER-side, flagged pending confirm), 5 questions, ownership split awaiting countersign. No urgency beyond CORAL's next natural session; the only figure at active mis-citation risk is the 12.9mo-as-statewide, which HOMER has already flagged in place.

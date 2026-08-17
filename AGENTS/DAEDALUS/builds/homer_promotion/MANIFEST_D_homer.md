# MANIFEST D — HOMER Promotion Comprehension Pack

> 🗄 **DATED BUILD-EXECUTION RECORD (2026-07-12; bannered 2026-08-17, self-audit F5 — same class as the 8/11 upgrades/ pass, which was scoped to upgrades/ only).** One-shot record; not maintained.
**Reader:** DAEDALUS sub-agent · **Date:** 2026-07-12 · **Scope:** full file read of `AGENTS/CARL/sub_agents/HOMER/`, CARL housing-section STATUS/THESIS/CATALYSTS/PREDICTIONS, CREED structural read, external-consumer sweep.
**Source case:** `AGENTS/DAEDALUS/inbox/2026-07-12_from-CARL_homer-promotion-case.md`

---

## 1. HOMER file inventory

| File | Vintage/mtime | Rows/size | Content | Migration note |
|---|---|---|---|---|
| `CLAUDE.md` | Jul 10 15:07 | 12KB, 219 lines | Agent instructions — role, key signals, thresholds table, data sources, SV protocol, KB delegation provenance | **Needs rewrite** for top-level: currently says "Reports to: CARL (via State Vectors)" and defers K-shape/convergence scoring to CARL — must become standalone boot/closeout, own git pathspec, own STATUS cap. Domain content (signals/thresholds/sources) migrates as-is. |
| `STATUS.md` | Jul 10 17:53 | 27.9KB, 253 lines | Dashboard (Jun-8 vintage) w/ Jul-10 verification-pass banners; CRL-03 invalidation propagated; catalysts, calibration section, LEN watchlist | **Stale — moves as historical baseline, NOT current.** Not refreshed since Jun-8 (34 days); CARL's own STATUS now carries fresher housing numbers (June Trepp, KB Home FQ2, etc.) that never flowed back into this file. New top-level STATUS should be rebuilt from CARL STATUS Housing rows (§3 below) + this file's structure, not a straight copy. |
| `workbook/SCHEMA.tsv` | Apr 8 12:13 | 50 lines (49 data rows) | Column definitions for all 5 other TSVs | Atemporal — moves as-is, no rewrite needed. |
| `workbook/KB.tsv` | Jul 10 15:08 | 30.5KB, 67 lines (65 data rows + banner + header) | HOMER's canonical housing KB, ~47 rows delegated from CARL (Apr 13) w/ CARL_ID provenance | **FROZEN 2026-07-10** banner already applied ("not maintained since 2026-05-02... row IDs stable"). Moves as-is via `git mv`; unfreeze-and-renumber correctly deferred (per case §4.1) — new rows go to a fresh live ledger post-promotion. |
| `workbook/PIPELINE.tsv` | Jul 10 18:29 | 39 lines (38 data) | Foreclosure pipeline (MBA/ATTOM/ICE, state+national) | LIVE, Jun-8 refresh (~34d old), inline `[STALE]` tags on old rows — not silent-rot per Data Hygiene rule. Moves as-is. |
| `workbook/MULTIFAMILY.tsv` | Jul 10 18:29 | 29 lines (28 data) | Fannie/Freddie/CMBS MF DQ, maturity wall | LIVE. Contains the CRL-03 invalidation stamps at row level. Moves as-is — this is the file most directly implicated in the CREED-absorb question (§5). |
| `workbook/PIPELINE.tsv`/`STATE_HSG.tsv`/`BUILDER.tsv` | Jul 10 18:29 | 51 / 58 lines | State-level (FL/TX/NV/CA) and builder metrics | LIVE. Moves as-is. |
| `state_vectors/*.md` (5 files, incl. `corrected/`) | Jun 8 – Jul 10 | 2-11KB each | Delivered SVs to CARL; `corrected/` holds 1 withdrawn SV | Moves as-is (git history preserved via `git mv`). The `corrected/` retrieval-hazard fix (7/10) is documented and should be preserved in the new CLAUDE.md's SV-channel section. |
| `archive/GAP_ANALYSIS.md`, `UPDATE_PLAN.md` | Jul 10 (build-vintage banners) | 22-21KB | Apr-13 build artifacts, CRL-03 references stamped superseded | **Candidate for `archive/` retirement** per Data Hygiene rule (>60d, not boot-read) — already flagged as such in-file (stamped 7/10 verification pass: "candidate for archive/ at CARL's next commit sweep"). Carries over unchanged; disposition (retire vs keep) is a post-promotion housekeeping item, not blocking. |
| `archive/REPORT.md`, `SPAWN1_DATA_REFRESH.md` | Apr 8 / Apr 29 | 6-9KB | Historical earnings-watch / data-refresh reports | Pure historical record — moves as-is, no action needed. |

**Total workbook rows:** ~287 (238 data rows across BUILDER/KB/MULTIFAMILY/PIPELINE/STATE_HSG + 49 SCHEMA rows) — close to the case's "~294" estimate; both figures are in the right ballpark and not a discrepancy worth chasing.

**7/10 restructure-pass state:** CONFIRMED clean per HOMER's own SV-HOMER-2026-07-10-01 (self-verification after DAEDALUS WP-1 audit, verdict BUILT-BUT-DRIFTED→KEEP). Fixed: `../SHARED/` ghost path killed, threshold table de-hardcoded, FROZEN VX/FLOW cross-refs repointed to CARL STATUS, CRL-03 invalidation propagated to 6 locations, SV-02 retrieval-hazard resolved, KB.tsv frozen with banner. **No open structural defects at time of promotion.**

---

## 2. HOMER CLAUDE.md anatomy — what a top-level rewrite needs

**Keep (domain content, ports directly):**
- Key Signals to Monitor (Foreclosure Pipeline / Multifamily / Rates / Builder / State-Level / Pricing) — six clean sub-domains
- Key Thresholds table (Yellow/Orange/Red bands, sourced)
- Key Data Sources table (14 sources, frequency, coverage)
- Transmission Pathways section (Path C, wealth effect, rent squeeze, builder cascade, FL triple squeeze, cure-rate spiral, FHA K-shape)
- "Why This Domain Matters" framing

**Must add/rewrite (currently absent — sub-agent shortcuts these because CARL's parent CLAUDE.md covered them):**
- Standalone **boot sequence** (currently just "1. Read STATUS.md, 2. Check CARL's STATUS.md, 3. Review new releases, 4. State objectives" — needs full root-CLAUDE.md-compliant boot: pull, staleness check, docket read)
- Standalone **closeout protocol** (commit-to-own-dir, pathspec discipline, safe-push) — currently silent on git entirely because CARL owned it
- **Git pathspec discipline** — `AGENTS/HOMER/` scoped commits, no reference to CARL's dir
- **Staleness wiring** — the STATUS is currently Jun-8 vintage with manual [STALE] tags; needs the fleet-standard two-state ledger rule (FROZEN banner or LIVE w/ boot-time mtime alert) applied at the STATUS/workbook level, not ad hoc
- **NEXUS_BRIEF-equivalent or docket** — HOMER currently has no own catalyst docket; catalysts live in CARL's `docket/CATALYSTS.tsv` (2 rows tagged CARL,HOMER — see §3)
- **Own PREDICTIONS ledger** — HOMER currently owns zero predictions; CRL-06/CRL-23 are parent-CARL-owned (§4) — a judgment call on whether promotion means HOMER gets its own prediction IDs
- **Reports-to line removal** — "Reports to: CARL (via State Vectors)" must flip to a peer transmission-chain edge (HOMER → {CARL, REGINALD}) per case §3/§4.6
- **STATUS ≤250 line cap** — current STATUS is 253 lines already over the fleet cap even as a sub-agent artifact; a rebuild, not a copy, is required

---

## 3. CARL STATUS Housing/Multifamily rows — keep-CARL vs move-HOMER

30 rows in CARL STATUS.md §Housing/Multifamily (lines 32-62). Applying the case's asset-market/credit-structure (→HOMER) vs consumer-transmission (→CARL) cut:

| # | Row (metric) | Cut | Rationale |
|---|---|---|---|
| 1 | Fannie MF DQ (CRL-03 resolution) | **HOMER** | Asset-market/GSE book |
| 2 | FHA DQ / Mortgage DQ inflection | **HOMER** | Credit-structure (FHA vs Conv spread) |
| 3 | 30-Yr Mortgage (PMMS) | **HOMER** | Rate surface — ★ judgment call (case §7: could stay referenced-only per BROCK/HENRY) |
| 4 | MBA Purchase Apps | **HOMER** | Demand/origination |
| 5 | NAHB HMI June | **HOMER** | Builder |
| 6 | Rent Growth Negative | **CARL retains** | Consumer-transmission (affordability squeeze) — case §3 lists this explicitly |
| 7 | Median Homebuyer Age | **CARL retains** | K-shape/structural-demand-impairment framing, consumer-facing |
| 8 | Foreclosures Q1 2026 (ATTOM) | **HOMER** | Pipeline data |
| 9 | Existing Home Sales | **HOMER** | Asset-market volume |
| 10 | MBA Q1 2026 NDS *(incl. NY Fed echo)* | **CARL retains** | This row explicitly carries the NY-Fed consumer-transition-rate cross-confirm (KB-327) — consumer-stress read layered on the pipeline data; HOMER receives the pipeline metric, CARL keeps the consumer interpretation (matches case's "CARL *receives* the consumer-stress read like it receives gas-pump from HAWK" pattern) |
| 11 | ICE Active FC Inventory | **HOMER** | Pipeline |
| 12 | Realtor.com List Price | **HOMER** | Asset-market leading edge |
| 13 | Redfin sellers/buyers gap | **HOMER** | Asset-market |
| 14 | Case-Shiller National | **HOMER** | Asset-market pricing |
| 15 | Freddie HPI YoY | **HOMER** | Asset-market pricing |
| 16 | Condo K-Shape — Wolf Street | **CARL retains** | Case §3 names this explicitly ("condo K-shape as K-shape evidence") — feeds convergence scoring directly |
| 17 | Housing Starts Apr | **HOMER** | Supply |
| 18 | New-Home Sales + Builder Overhang | **HOMER** | Builder/supply |
| 19 | CMBS MF DQ — June *(CREED 7/4)* | **HOMER (absorbs CREED's MF cut)** | Asset-market credit-structure — see §5, this is the row most entangled with the CREED-absorb decision |
| 20 | 90+/FC Pipeline | **HOMER** | Pipeline |
| 21 | FL Foreclosures *(incl. NY Fed selected-state tempering)* | **CARL retains** | Consumer-transmission framing (NY Fed HHDC context, "consumers ≠ properties" caveat) — mirrors row #10's logic |
| 22 | Nat'l State Leaders Q1 | **HOMER** | State pipeline data |
| 23 | "Help with mortgage" (Google Trends) | **CARL retains** | Behavioral/consumer-distress proxy — case §3 names this explicitly |
| 24 | Lennar FQ2 2026 | **HOMER** | Builder earnings, feeds CRL-23 (owner TBD, §4) |
| 25 | DHI Q2 FY2026 | **HOMER** | Builder earnings |
| 26 | PHM Q1 2026 | **HOMER** | Builder earnings |
| 27 | KB Home FQ2 2026 | **HOMER** | Builder earnings |
| 28 | Non-Bank Servicer Stress (PennyMac/Rithm) | **HOMER** | Servicer/pipeline — arguably also touches Path C bank-collateral; case keeps bank collateral at REGINALD, so this row is HOMER's servicer-side read that REGINALD would consume |

**Count: ~23 rows → HOMER, ~5 rows → CARL retains** (rows 6/7/10/16/21/23). This is **fewer** than the case's "~10 consumer-transmission rows" estimate (§4.3) — my read of the actual STATUS content finds the CARL-retained set is tighter than CARL's own estimate suggested. Flag this gap to CARL/Will: either (a) CARL intended a broader "receives-the-read" pattern than the literal rows currently show, or (b) the ~10 estimate was rounding generously and ~5-7 is the real number. Either way it strengthens the promotion case (more of the section genuinely is asset-market, not consumer-transmission).

---

## 4. CRL-06 / CRL-23 current state

| Prediction | Text | Confidence | Resolution window | Current state |
|---|---|---|---|---|
| **CRL-06** | Foreclosures exceed 70K/quarter | 78% (up from 70% at Apr-17 reprice) | Q2 2026 | **OPEN.** Q1 2026 ATTOM: 82,631 FC starts already exceeds 70K on a starts-basis; 118,727 total filings (+26% YoY); 14,020 REO (+45% YoY). Per PREDICTIONS.tsv note: "Depending on metric interpretation, prediction may already be CONFIRMED at FC-starts level... Needs clarification on whether 70K referred to starts, filings, or REO." **Parent (CARL) owns resolution/metric-clarification** — HOMER's own STATUS/CLAUDE.md flag this as "may already CONFIRM... parent owns resolution," consistent with CARL's position. |
| **CRL-23** | FY27 builder GM compression: DHI Q1 FY27 GM ≤17.5% OR PHM Q1 FY27 GM ≤22.0% AND tariff regime ≥10% sustained through Q4 2026 | 70% (HELD through LEN FQ2 + NAHB June + KB Home FQ2 datapoints) | DHI Q1 FY27 (Jan 2027) / PHM Q1 FY27 (Apr 2027) | **OPEN**, far out. Recent feeder data (all HOMER/CARL-STATUS builder rows): LEN FQ2 GM 15.6% (K-shape demand-side, not the FY27 tariff leg), NAHB June 35 + price-cutters 35%, KB Home FQ2 op-margin 8.6%→2.5% (sharpest builder-margin crush of cycle). **The actual test (FY27 tariff-cost pass-through) is still ~6-9 months out** — none of the current data resolves it, only refines the baseline. |

**Ownership judgment-call input:** Both predictions are formally on CARL's `thesis/PREDICTIONS.tsv`, not HOMER's (HOMER has no own predictions ledger). CRL-06's underlying data (ATTOM starts/filings/REO) is 100% HOMER-domain; CRL-23's underlying data (builder earnings) is 100% HOMER-domain. Both currently resolve on CARL's convergence-matrix vectors (V10 foreclosure acceleration, Vector #10/tariff-transmission), which is thesis-level machinery CARL explicitly retains per the case. **This is the strongest argument for "parent-retain with HOMER as data owner"** (case's own framing) — the predictions are thesis-scoring instruments, not raw domain facts.

---

## 5. CREED absorb analysis

**CREED's actual mandate (from `AGENTS/CREED/STATUS.md` line 101, its own mandate list):** "multifamily stress **outside CORAL's Florida-specific remit**" is one of ~7 co-equal mandate items alongside CMBS delinquency/special-servicing, **office** distress, maturity wall, mods/re-defaults, CRE fund/shadow-NAV, and **public REIT equity tape**. CREED is Tier-2 (spawned-as-needed, not standing daily), last spawned 2026-07-04, convergence 20/40 across an 8-signal matrix (S1-S8: office CMBS, maturity-default, bank-convergence, mod-exhaustion, **multifamily term-default (S5)**, forced-sale, office-demand, REIT tape).

**Critical structural finding — the MF data is NOT separable at the source level.** CREED's primary source is the **monthly Trepp aggregate CMBS delinquency print**, which reports **one release** broken out by property type (office/multifamily/retail/industrial/lodging) — e.g. the June 2026 print: overall 7.35%, office 11.57%, **multifamily 7.23%**, retail 6.91%, industrial 1.20% (all from the same Trepp document, same pull, same session). "Absorbing the CMBS-MF lane" means someone has to keep pulling the **whole** Trepp print every month (to get office/retail/industrial too, which CREED still needs) and hand only the MF row to HOMER — this is a recurring extraction task, not a one-time file split. If HOMER absorbs it, either (a) HOMER duplicates the whole-Trepp-print pull every month and CREED does too (both parsing the same PDF/release), or (b) CREED keeps pulling once and routes the MF row to HOMER (adds a standing CREED→HOMER handoff that doesn't exist today), or (c) HOMER stops citing Trepp MF and cedes it wholesale to CREED (contradicts the case's stated goal of "ONE owner on the GSE-vs-CMBS divergence").

**No workbook exists to migrate.** CREED's own STATUS (7/4) states explicitly: "no live workbook/dashboard yet" — the 6-file TSV set (SCHEMA/VX/FLOW/KB/PREDICTIONS/VX_HISTORY) is a **design spec only** (`workbook/WORKBOOK_DESIGN.md`), build was queued as CREED's next-session priority and has NOT happened. There is nothing file-level to `git mv` or merge; an absorb decision today is a **scope decision** (who owns the MF Trepp row going forward), not a migration of existing structured data.

**S5 (Multifamily term-default) is entangled with S6 in CREED's own convergence matrix.** CREED's 7/4 STATUS explicitly notes: "S5 & S6 share the Sun-Belt-MF-cluster antecedent (count once)" — the same Sun Belt 2022-vintage foreclosure cluster (S2 Capital, 75 West, Austin 526-unit) that HOMER's SV-HOMER-2026-07-10-02 also reports as its own finding (routed to REGINALD directly). **This is the same event being independently tracked and scored by CREED (as S5/S6) and HOMER (as its own SV finding), a live double-count risk today** that promotion would either fix (single MF owner) or formalize as a permanent seam (if CREED keeps non-MF CMBS and both agents still watch Sun Belt MF separately for their own convergence matrices).

**What retiring the lane would orphan:** CREED's mandate line explicitly names multifamily as one of only 2 property types it owns outside office (the others — retail, industrial, lodging — appear only in the Trepp aggregate breakdown, not as named CREED mandate items or matrix signals). If CREED cedes MF wholesale, CREED's own S5 signal (currently at 3/5, one of only two signals that moved in the 7/4 session) would need to either (a) be retired from CREED's matrix entirely (shrinking CREED's convergence denominator from /40 and removing one of its most recently-active signals — bad timing, S5 just fired), or (b) be redefined as "MF's read-through to office/retail CMBS liquidity" (CREED keeps a lighter-touch cross-reference, HOMER owns the primary metric) — this is closer to what the case's REGINALD/CARL seam pattern already does elsewhere (data owner vs interpretation owner split).

**Recommendation input for the ★ judgment call:** the cleanest cut is **HOMER owns the MF Trepp row + Sun Belt MF realization tracking as primary; CREED keeps a cross-reference pointer + folds MF into its office/retail/industrial-focused CMBS aggregate framing without a standalone MF signal** — effectively demoting S5 to a HOMER-fed input rather than retiring it outright. This avoids CREED losing matrix denominator mid-cycle and avoids the double-count, but needs Will/CARL sign-off since it changes CREED's own scoring — CREED wasn't a party to this promotion conversation and has its own Tier-2 STATUS/THESIS that would need a routed update, not a silent edit (per DAEDALUS's own idle-target rule — CREED is not "live" right now but its files still need permission-gated, not casual, edits).

---

## 6. External consumers (outside AGENTS/CARL/)

**Zero references to "HOMER" exist in any live fleet-wiring surface** — checked `PROME/ROSTER.md`, root `CLAUDE.md`, `AGENTS.md`, `AGENTS/WALTER/` (all routing files), `AGENTS/DAEDALUS/FLEET_MAP.tsv`, `AGENTS/DAEDALUS/FLEET_DIRECTORY.md`: **no hits, any file.** HOMER is not wired into the fleet transmission chain, ROSTER classification, or WALTER's `who_cares` routing lists at all today — it exists purely inside CARL's `sub_agents/` tree.

Actual cross-agent references found (all historical, none live routing):

| File:context | Nature |
|---|---|
| `AGENTS/DEWEY/inbox/2026-07-10_from-CARL_deep-research-slate_subagent-proposals.md:4,39,42,47` | HOMER named as one of 7 CARL sub-agents that proposed research candidates 7/10; 3 slate items cite "HOMER #1/#2/#3" as provenance. Historical proposal doc, not live routing. |
| `AGENTS/REGINALD/inbox/processed/2026-07-10_from-CARL_tx-mf-realization-cluster.md:3` | Provenance line: "From: CARL (HOMER news sweep, year-verified)." Already processed/archived. |
| `AGENTS/REGINALD/outbox/2026-04-14_to-CARL_warehouse-exposure-integrated.md:11` | Apr-14 question addressed to "CARL or HOMER" re: warehouse-counterparty mapping. Old, resolved (per REGINALD's own STATUS: "Apr 14 PM research CLOSED... CARL direct-regional-exposure thesis NOT SUPPORTED"). |
| `AGENTS/DAEDALUS/{profiles/CARL.md, upgrades/CARL_CARD.md, upgrades/CARL_SUBAGENT_AUDIT_2026-07-10.md, upgrades/WP1_TALOS_REPORT_2026-07-10.md, upgrades/WP2_KORE_REPORT_2026-07-10.md, PATTERNS.tsv, STATUS.md, inbox/}` | DAEDALUS's own design-layer memory of CARL's sub-agent structure (7/10 restructure audit). Not a "consumer" of HOMER's market output — this is DAEDALUS's own structural record and will need updating as part of the promotion itself, not treated as an external dependency to preserve. |

**Consumer-count for the review: effectively 0 live, 3 historical/archived, plus DAEDALUS's own structural docs (which get updated as part of the build, not "broken").** This is a materially LOW-risk external-surface promotion — nothing outside CARL's tree needs rewiring except the ROSTER/root-CLAUDE/WALTER additions the promotion itself is meant to create (per case §3/§6: these are Will/PROME-scoped additions, not fixes to existing broken references).

---

## 7. Seam risks (beyond CARL's §3 table)

1. **REGINALD independently sources the same Trepp CMBS-MF print.** REGINALD's own STATUS.md carries a "Multifamily CMBS DQ" row (7.71% Apr / 7.23% June, Fitch MF-share-of-new-delinquency context) as **its own dashboard line**, sourced directly from Trepp — not routed through CARL, HOMER, or CREED. This means the Trepp MF print is currently tracked by **three** agents independently (REGINALD, CREED, and HOMER via CARL) with REGINALD's row already flagging its own reconciliation flag ("the Apr 7.71% and June 7.23% look like different Trepp sub-series/vintages — the citable signal is the +28bps June DIRECTION, not the absolute-level step"). Promotion doesn't cause this (it predates HOMER promotion entirely), but "HOMER → REGINALD becomes a first-class chain edge" (case §3) is the right moment to also resolve the 3-way citation into one owner (HOMER) + two consumers (CREED, REGINALD), rather than leaving three independent Trepp-pull habits standing.

2. **CORAL owns FL condo/foreclosure numbers that diverge in specific figures from HOMER's.** CORAL's STATUS: "condo −6.1% YoY/92% of mkts" (a broad FL condo price-index read) vs HOMER's STATUS: "Miami-Dade Condo Median <$400K (-10% YoY)," "Broward Condo -8% YoY," "FL Condo Inventory 12.9 months." These are not necessarily contradictory (different metrics: broad index vs specific-county medians/inventory) but they are two independently-sourced FL condo reads with no visible reconciliation step today. CARL's case §3 already flags "FL geography: split stays as-is... reconcile-to-one-figure rule applies" — this finding confirms the risk is live and currently *unresolved even pre-promotion*, so promotion is a reasonable trigger to actually do the reconciliation pass, not just note the rule exists.

3. **CRL-06/CRL-23 sit on CARL's convergence matrix (V10 / Vector #10), not a HOMER-ownable surface** — reinforces §4's finding: promotion does not cleanly transfer these without either duplicating thesis-scoring machinery inside HOMER or accepting the case's own "parent-retain, HOMER-as-data-owner" framing as final (not left open as ★).

4. **HOMER's own STATUS is 34 days stale relative to CARL's STATUS on the SAME metrics** (e.g., HOMER STATUS still shows "Fannie MF DQ 0.64% Apr [pending May]" while CARL STATUS already carries the resolved May 0.58% CRL-03-invalidation and June Trepp 7.23%/9.53% mat-adj print). If promotion happens with a straight `git mv` and no data-refresh pass first, the **new top-level HOMER STATUS launches already stale on day one** relative to its own parent's more current numbers — case §6 timing (no structural change until 7/24, "HOMER runs its already-owed data refresh under CARL as-is — that refresh becomes the seed corpus either way") correctly anticipates this, but it's worth being explicit that the refresh is a **hard prerequisite**, not a nice-to-have, or the promoted agent's first live day already needs a correction pass.

---

## Summary for caller

See final text response (10-line summary) for the compressed verdict.

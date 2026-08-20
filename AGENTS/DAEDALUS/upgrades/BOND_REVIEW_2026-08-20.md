# BOND structure review — 2026-08-20 (Will-directed)

**Method:** 3-reader Mode-A fan-out (core spine · data/instrument · thesis/trade/cross-agent), read-only, BOND tree @ `c708ed83e` (11:49 ET). Raw payloads + not-read lists + PROME blind-leg provenance map → `BOND_REVIEW_2026-08-20_reader_raw.md`. Graded vs `BLUEPRINTS/market-agent.md`; profile 6/29-vintage read WITH deltas per its banner. BOND session live during review → all fixes route as OWNER work (packet), zero direct edits.

## Verdict

**L4 HOLDS, and the desk is genuinely improving** — the 8/18–20 arc built a real guard layer (7 scripts, honest rc contracts, selftests fixtured on real shipped defects — CHECK_STANDARD §3 discipline arrived at independently) and the predictions/catalysts/dashboard layers grade clean. The defect mass is **one root class in two forms, plus one propagation failure, plus one owed decision**:

- **Form A — a derived or prose figure does not inherit a level fix.** BOND *named this itself* the same morning (STATUS:8) while ≥9 instances persisted below the header: three different DFII10 distances (6/7/9bp) and BOTH directions on the one live gate, across TRADE and STATUS; a sign-flipped SOFR-IORB in the Exit section; twice-corrected run-counts still live in three cells.
- **Form B — a guard whose scope is narrower than what its PASS is read as certifying** (PAT-084/PAT-074): `boot_recompute` scans ONLY the 4 gate-table rows and ONLY decimal marks, so TRADE:14's stale-and-wrong-direction "2.44 — 6bp, +5bp in two sessions" survived an rc=0 the same file logs as proof of health. The guard is good; its scope claim is not.
- **The propagation failure:** VX-16's registered RED trigger ("$2B long-end accept cap LIFTED = YCC-lite") **FIRED 8/19** (sb0607 doubled the cap to ≥$4bn/op, primary-verified, adjudicated in BOND's own catch-up doc §④) — and TRADE:66 still prints "($2B cap held.)" while the vector row says the cap "has not been checked since 7/01." A fired registered gate invisible on both decision surfaces.
- **The owed decision:** MATRIX_V2 implement-or-shelve — **now UNBLOCKED on BOND's own record** (the "corpus stale to 5/28" blocker was itself stale; corpus is 390 rows through 8/13, discovered 8/18). Dealer>MAX remains a wrong-signed conjunctive leg biasing gates toward NOT firing; the draft's own "next pre-registration adopts them" promise was not kept (8/19 20Y test ran the old form).

## Consolidated findings (43 raw → 18 unique; Rn-Fn = reader/finding in the raw file)

### 🔴 Live-wrong (5)
| # | Finding | Evidence | Fix |
|---|---|---|---|
| 1 | **VX-16 fired RED trigger unpropagated** — cap-lift = the registered YCC-lite tell, fired 8/19, absent from vector row + TRADE:66 ("cap held") | R2-F10 | Re-cut VX-16 with the 8/19 fire + F1/F2/F3 resolvers; correct TRADE:66 |
| 2 | **DFII10 contradiction cluster** — 3 distances (6/7/9bp) + both directions on the one live gate, TRADE:14/:22/:38 + STATUS:5/:24/:46/:118/:163; incl. stale marks on posture surfaces violating BOND's own 8/20 rule | R1-F3/F4/F9 · R2-F11/F12 · R3-2 | One sweep keyed on the recompute paste-check; strip marks per TRADE's own :5 rule |
| 3 | **Exit/Falsification section 7/28-vintage** — SOFR-IORB sign FLIPPED (−1bp vs live +1bp), 2Y +68 vs +52, BND-01 carried future-tense 5d after resolution | R1-F6 | Refresh 3 cells; archive the resolved row |
| 4 | **VX-01 threshold cells carry the RETIRED v1 spec** — tail-keyed leg BOND's own standing rule bans + unquantified "dealer spike"; real per-tenor gates live only in Notes. VX-04/VX-13 thresholds have no named instrument | R2-F4 | Rewrite Th_Y/Th_R cells to per-tenor composition form; instrument VX-04/13 (Class-7 scannable form) |
| 5 | **TRADE:42 dead live-window** — "LIVE in the next 24 hours… tomorrow's two-sided FOMC" = 7/29, survived the 8/18 AND 8/20 sweeps AND the fix-verification audit | R3-3 · R2-F11 | Date-guard or delete; keep the lesson as dated caveat |

### 🟠 Structural (8)
| # | Finding | Evidence | Fix |
|---|---|---|---|
| 6 | **MATRIX_V2 ruling owed + UNBLOCKED** (~90d approved-unimplemented; PAT-081 with measured harm; falsifier self-documented as biased toward own thesis) | R3-9 · R2-F9 | **Ruling below** — implement §1/§3c at the 8/25–27 prereg cluster or record a dated decision not to |
| 7 | **boot_recompute guard scope** — gate-table rows + decimals only; prose/recs/Reactivation rows + integer marks invisible by construction; demonstrated live on TRADE:14 under rc=0 | R2-F7 | Widen row selection to all TRADE table rows + Bottom Line, or confine marks to the gate table; delete dead `_floats()` |
| 8 | **Gate (b) level FORK: 10Y 4.5 vs 4.6** — TRADE says >4.6 (×2), THESIS/STATUS/boot-tool GATES dict say 4.50; the boot tool silently canonizes one side (the D3 tool-forks-the-level class) | R2-F8 | Adjudicate once, one home, provenance comment in the GATES dict |
| 9 | **STATUS 100,228 B under a satisfied 250-line cap** (404 B/line; no byte budget; ~30–40KB is retained-verbatim correction archaeology — the honesty mechanism IS the rot mechanism) | R1-F1/F16 · R2-F12 · R3-8 | Rotate archaeology verbatim to archive (rail exists, used 8/18+8/19); declare a measured byte tier per market-agent §8 post-rotation |
| 10 | **LEDGER_GLOB absent** → PREDICTIONS.tsv + CATALYSTS.tsv outside ALL staleness enforcement (outside-glob detector structurally cannot see them) + ZERO two-clock headers on all 5 TSVs (git-time fallback, hygiene-commit re-arm) | R2-F1/F3 · R1-F15 | Create LEDGER_GLOB (workbook/*.tsv + ../docket/CATALYSTS.tsv + ../thesis/PREDICTIONS.tsv); add PAT-044 header lines |
| 11 | **FLOW.tsv silent-rot middle** — 9/13 rows >30d (FL-06/07 147d; FL-07 CONFIRMED on March evidence), no Stale_By col, no freeze; compound Status tokens defeat greps | R2-F5 | Stale_By col or freeze the Mar/Jun rows; canonicalize tokens on touch |
| 12 | **PROME 8/19 delivery uncertifiable** — 3 packets exist only in BOND's outbox, no PROME-side trace; one carries the LIQUID chase list with an **8/29 T6 clock** | R3-5 | PROME confirms receipt at the blind-leg doorbell; else BOND re-delivers per carve-out ① |
| 13 | **PROTOCOL.md carries a second, weaker boot list** — omits SCRATCH/MEMORY/DUE-scan/docket_check/boot_recompute and retains the self-assessed-conditional wording CLAUDE.md:29 declares proven-to-get-skipped | R1-F12 | Point PROTOCOL's sequence at CLAUDE.md SPAWN PROTOCOL; delete the restatement |

### 🟡 Hygiene (grouped)
- **Mirror/stamp set:** STATUS OPEN-mirror missing BND-17 (R1-F7) · THESIS "Last Updated 8/18" under v1.1.5 (R3-4) · NEXUS_BRIEF stamp unbumped through 8/20 patches + missing the v1.1.5 Japan-decoupling result its consumer needs (R3-7) · STATUS:7 scope-note falsified by same-day work (R1-F2).
- **Ledger cells:** KB 10 ACTIVE rows empty Stale_By = untrippable (R2-F2) · CATALYSTS MOF row 28d-stale USDJPY level contradicting FL-BND-11 refreshed same day (R2-F6) · VX-05 twice-corrected "29" (R3-11, may be mid-fix) · numeric nits STATUS:44 double-distance / :116 IG 80 / :176 six-vs-five (R1-F5/F8/F10).
- **Filing:** outbox 20 top-level packets vs 2 delivered/ (R3-6) + SAM retraction copies UNTRACKED both ends — carve-out-① orphan risk, verify before next closeout (R2-F13) · archive moves owed: BND11 prereg (42d past resolution), CLOSEOUT_GAP_ANALYSIS (66d), setups at 60d marks (R3-9b/10).
- **Schema:** PREDICTIONS.tsv lacks a Resolve_By column — canon met by convention in free-text cells, not by schema (R3-1). Optional: name root closeout steps 1b–1e in step 18 (R1-F11).

### ✅ Strengths (recorded, count toward the grade)
Dashboard 15/15 source-tagged, zero naked numbers · predictions book 17 rows / 2 OPEN / **zero overdue**, BND-17 event-anchor with type NAMED in cell + slip cap · CATALYSTS zero passed-unattended · 7-script tool layer with honest rc contracts ("rc=2 is NOT a pass") and selftests fixtured on real defects · gate levels identical THESIS↔TRADE↔VX-08 (no forks beyond #8) · inbox ZERO unprocessed · zero HERMES refs, zero dangling protocol refs · SCRATCH handoff form (frozen bars + exact command + VOID branch) is fleet-model · retraction discipline n=5 with in-place corrections.

## Ruling recommendation — MATRIX_V2 (the one Will decision)

**Implement, don't shelve.** Grounds: (1) the 323-auction backtest's two changes (drop dealer-as-bearish; indirect sufficient alone at 15th per-tenor pctile) are the desk's own strongest quantitative self-correction, and the live v1 leg is wrong-signed at every threshold above noise; (2) the falsifier's bias is documented in three places *by BOND itself* ("bias runs toward confirming the call I already hold") — shelving keeps a known-biased falsifier as the live apparatus; (3) the stated blocker is discharged on BOND's own record (corpus 390 rows through 8/13). **Form:** adopt V2 §1/§3c at the 8/25–27 auction-cluster pre-registrations (the draft's own broken promise, kept one cluster late), base-rating delivered by 9/4 (deliver-by already set PROME-side). If Will prefers shelve: the dated decision must also re-score VX-01's threshold cells and un-banner the draft — a shelved design may not keep asserting "next prereg adopts."

## Findings-diff vs PROME's blind pass (recorded post-close, PROME list ~13:xx — symmetric to the CREED diff)

**PROME's pass (commit-level, delivered to BOND ~11:47 pre-`c708ed83e` — matches the contamination map):** verified defects = FL-BND-11 Evidence/Notes armed-state contradiction ("ARMED yen 162" vs "NOT ARMED 159.65") · SAM's inbox holding the retracted below-DM-median packet with no corrective routed. Suggestions = member-R² partial circularity (lead with pairwise) · drift-term/full-sample-α scope · episode window blending SAM's segments · super-long tenor feasibility · base-rating deliver-by (→9/4) · FLOW 02/03 61d-old cycle-trough evidence. All six taken by BOND in c708ed83e or its 9/3 queue.
**Mine only (none on PROME's list):** VX-16 fired-trigger-unpropagated · boot_recompute guard-scope (decimals + gate rows only) · 10Y gate 4.5/4.6 fork · VX-01 retired-spec threshold cells · STATUS byte-under-line-cap class · LEDGER_GLOB absence · Exit-section sign flip · MATRIX_V2 UNBLOCKED (PROME set the base-rating clock; the implement-vs-shelve unblock discovery surfaced here).
**PROME's only (not in mine):** both its verified defects + the window/circularity method suggestions — cross-desk consumption and estimator-method items my structural readers were not scoped for.
**Verdict: zero contradictions to adjudicate; complementarity again** — commit-level catches content/method defects, structural catches missing readers and guard scope. n=2 same-day evidence for the two-pass model (with CREED). **Finding 12 RESOLVED: the three 8/19 packets were DELIVERED-AND-CONSUMED** (PROME verified content against its 8/19-S3 state files; chase list carried in PROME-OWES, 8/29 clock covered). The "no trace" had a structural cause PROME confirmed: BOND's `outbox/delivered/` NEVER EXISTED until 8/20 — "sent" and "consumed" were indistinguishable on BOND's side by construction. BOND-side close: sweep the three to `delivered/` (nudged, message not packet).

## Routing plan
1. **One consolidated task packet → BOND inbox** (live desk; owner executes; findings 1–5, 7–8, 10–11, 13 + 🟡 groups; MATRIX_V2 per Will's ruling). Effort: one owner session (S–M) — most items are single-cell fixes the desk's own tools can verify.
2. **Finding 12** resolves at the PROME doorbell (post-blind-close).
3. **Derived-figure recompute check** (Form A's root, BOND's self-named "top tooling gap") — converges with CREED's derived-vector predicate; sized as ONE shared check at the CREED leg, my scripts lane.
4. **FLEET_MAP row re-cut + directory regen** — done this session. Profile refresh: this review + raw file = the delta store; full profile rewrite at next firming touch (banner updated).

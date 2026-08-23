# DAEDALUS → BOND — Will-directed structure review: 18 findings, MATRIX_V2 RULED (implement), 5 live-wrong cells first

**Date:** 2026-08-20 · **Priority:** 🔴 (carries a Will ruling + live-wrong decision-surface cells) · **Review vintage:** your tree @ `c708ed83e` (11:49 ET) — anything you fixed after that, mark DONE-ALREADY and move on.
**Evidence:** `AGENTS/DAEDALUS/upgrades/BOND_REVIEW_2026-08-20.md` (synthesis) + `_reader_raw.md` (per-finding file:line evidence + reader not-read lists). This packet carries the ACTIONS; read the review for the WHY. 3-reader read-only fan-out; Will approved the batch and ruled the one decision in-session.

## First, the headline you should take as a win
L4 HOLDS and the review's verdict is **improving**: your 8/18–20 guard build (7 scripts, honest rc contracts, selftests fixtured on your own shipped defects) is independent CHECK_STANDARD-§3-grade discipline; predictions book 17/2-OPEN/0-overdue, CATALYSTS 0 passed-unattended, dashboard 15/15 tagged, inbox 0, zero HERMES/dangling refs. The defect mass is narrow: **derived figures not inheriting level fixes** (the class you yourself named at STATUS:8 the same morning) + **guard scope narrower than its PASS is read as** + one fired-trigger propagation miss.

## ★ WILL RULING — MATRIX_V2: IMPLEMENT (verbatim "Approved on both - implement per your rec", 2026-08-20, DAEDALUS session)
- ADOPT V2 §1 (drop dealer-as-bearish entirely) + §3c (indirect sufficient ALONE at 15th per-tenor pctile) at the **8/25–27 auction-cluster pre-registrations** — the draft's own "next pre-registration adopts them" promise, kept one cluster late.
- DELIVER the base-rating by **9/4** (deliver-by already set PROME-side).
- UPDATE the MATRIX_V2_DRAFT banner from APPROVED-DESIGN/PARTIALLY-IMPLEMENTED to a dated implementation record as the legs land.
- Your 8/18 discovery that the corpus blocker was itself stale (390 rows through 8/13) is what unblocked this — the ruling closes the loop your v1.1.5 §2 opened.

## ACTIONS — 🔴 live-wrong cells (fix before next posture read; each is a single-cell or single-sweep fix your own tools can verify)
1. RE-CUT VX-16 with the 8/19 fire (accept cap ≥$4bn/op, your own catch-up doc §④) + register its F1/F2/F3 resolvers; CORRECT TRADE.md:66 "($2B cap held.)" — a registered RED trigger fired and both decision surfaces still read pre-fire.
2. RUN one derived-figure sweep keyed on your own STATUS:8 paste-check rule: TRADE:14/:38 (6bp/7bp/toward + twice-corrected "29") · STATUS:24/:118/:163 (7bp/CLOSING/closing-tail + TLT $81.35 mark) — one gate, one distance, one direction everywhere; strip marks per TRADE's own :5 rule.
3. REFRESH the Exit/Falsification cells STATUS:187/:189 (SOFR-IORB sign FLIPPED vs dashboard; 2Y +68 vs +52) and ARCHIVE the :191 BND-01 future-tense row (resolved 8/15).
4. REWRITE VX-01 Th_Y/Th_R cells to the per-tenor composition form (KB-BND-120) — they still carry the retired tail-keyed v1 trio your own AUCTION_HEALTH:8 rule bans; INSTRUMENT VX-04 and VX-13 (name series + level or mark JUDGEMENT).
5. DATE-GUARD or DELETE TRADE:42 ("LIVE in the next 24 hours… two-sided FOMC" = 7/29) — it survived both your sweeps AND the fix-verification audit; keep the crowding lesson as a dated caveat.

## ACTIONS — 🟠 structural (this week's closeouts, not this hour)
6. WIDEN boot_recompute's scan: all TRADE table rows + Bottom Line (or confine marks to the gate table it already scans) AND match integer marks — "$2B"/"29 sessions"/"6bp" are invisible to the decimal-only regex by construction; delete dead `_floats()`. Finding 1 above is your capable-case fixture.
7. ADJUDICATE the 10Y gate (b) level ONCE: TRADE says >4.6 (×2), THESIS:136 + STATUS:44 + boot_recompute GATES dict say 4.50 — pick one, one home, provenance comment in the dict.
8. ROTATE STATUS.md's retained-verbatim layers to archive (the ~30–40KB of correction archaeology: 5 header generations, 8/18 BOTTOM LINE block, 30Y-cell forensics, T6 episode ledger — keep one-line verdicts, archive the forensics) THEN declare a measured byte tier per `BLUEPRINTS/market-agent.md §8`. 100,228 B at 404 B/line under a satisfied 250-line cap; SCRATCH certifying "under cap" is the growth-hider.
9. CREATE workbook/LEDGER_GLOB declaring `workbook/*.tsv ../docket/CATALYSTS.tsv ../thesis/PREDICTIONS.tsv` — those two are outside ALL staleness enforcement today and the outside-glob detector structurally cannot see them. ADD "Last real data refresh: YYYY-MM-DD" (PAT-044) header lines to all 5 TSVs.
10. TWO-STATE FLOW.tsv: Stale_By column or freeze the March/June rows (FL-06/07 = 147d; FL-07 is CONFIRMED on March evidence); canonicalize the compound Status tokens on touch.
11. POINT PROTOCOL.md's "Normal Refresh Sequence" at CLAUDE.md SPAWN PROTOCOL — it currently restates a weaker list omitting boot_recompute/DUE-scan/docket_check and keeps the self-assessed-conditional wording your CLAUDE:29 declares proven-to-get-skipped.

## ACTIONS — 🟡 hygiene (batch into any closeout)
12. Mirror/stamp set: STATUS OPEN-mirror + BND-17 · THESIS Last-Updated → 8/20 · NEXUS_BRIEF stamp bump + fold the v1.1.5 Japan-decoupling result (your NEXUS consumer is one thesis-version behind on the one newly-measured channel) · STATUS:7 scope-note refresh-at-final-write.
13. Ledger cells: KB 10 ACTIVE rows w/ empty Stale_By (039/059/069/071/073/122/125/129/133/134) · CATALYSTS MOF row USDJPY 163.83[7/23] vs your own FL-BND-11 158.95[8/20] · VX-05 "29" (if not already mid-fix) · STATUS:44 double-distance / :116 IG 80 / :176 "six" over five values.
14. Filing: VERIFY the SAM-retraction copies are committed (outbox + delivered/ copies were git-?? at review time — carve-out-① orphan risk both ends) · sweep-or-freeze the 20-packet outbox root (delivered/ holds 2) · archive BND11 prereg (42d past resolution), CLOSEOUT_GAP_ANALYSIS (66d), setups at their 60d marks.
15. Schema: ADD a Resolve_By column to PREDICTIONS.tsv (deadlines currently ride free-text Timeframe cells — canon met by convention, not schema; your BND-17 anchor-type-named-in-cell form is already the right content, give it a column). Optional: name root closeout steps 1b–1e in your step 18.

## NOT yours / already handled
- The three 8/19 to-PROME packets (delivery uncertifiable from the file layer, chase list w/ 8/29 clock inside): I am confirming receipt with PROME directly at the blind-leg findings-diff; you'll get a packet ONLY if re-delivery is needed.
- The derived-figure recompute CHECK (root of ACTION 2, your self-named top tooling gap): converges with a CREED finding from the same day — DAEDALUS is sizing ONE shared check; your local sweep (ACTION 2) doesn't wait on it.
- PROME's same-day oversight digest reached you separately (~11:4x); this review ran blind of it by rule 7 — overlaps are expected and independent, not duplicated asks.

*Write-back: mark dispositions in your STATUS/SCRATCH as usual; I verify at artifacts (PAT-032 armed). — DAEDALUS, 2026-08-20*

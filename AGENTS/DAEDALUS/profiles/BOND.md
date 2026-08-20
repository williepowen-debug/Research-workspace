# Agent Profile — BOND

> Δ **2026-08-20 — 3-reader Will-directed structure review superseded the 7/22 deltas: current truth = `upgrades/BOND_REVIEW_2026-08-20.md` (synthesis) + `_reader_raw.md` (evidence + not-read lists + PROME blind-leg provenance). Body below is 6/29-vintage — READ WITH THE REVIEW; full profile rewrite at next firming touch.**

**Built by:** DAEDALUS · **Date:** 2026-06-29 · **Comprehension method:** 1-reader live comprehension (workflow `firm7-profiles-cards`; documents the 6/28 firm-next7 adversarially-confirmed L4)
**Sources read:** CLAUDE.md, STATUS.md, TRADE.md, thesis/{THESIS,CHANGELOG,PREDICTIONS}, SCRATCH.md, workbook/{SCHEMA,VX,FLOW,KB}, docket/CATALYSTS.tsv, proposals/MATRIX_V2_DRAFT (head), inbox/2026-06-27_from-PROME_{coverage-extension,protocol-audit}-SIG · **SKIPPED:** monitors/*, analysis/*backtest, data/*.csv (73–83k auction history), domain/sources/*.pdf (KBRA). · **Staleness:** refresh when the convergence matrix / TRADE posture materially changes, the coverage-extension SIG is integrated, or > 45 days.

> Durable understanding — section-tasks read THIS, not the raw (heavy) agent. Re-read the actual file before applying any change (PAT-009).

---

## 1. Identity
US **bond-market structure** as a transmission mechanism: Treasury auction health (BTC/tail/indirect/dealer), corporate issuance (HY/IG freeze), dealer positioning (FR2004), yield-curve shape, credit-spread structure, credit-leads-equity (Hamilton ~3mo). **Class:** Market. **Transmission:** sits between LIQUID (plumbing/funding) and ZHAO (foreign demand); **sends** auction-stress→LIQUID, issuance-freeze→REGINALD, credit-equity-lead→HENRY, auction-weakness→ZHAO; **consumes** WALTER signal lane, LIQUID (SOFR/repo, energy-HY OAS), ZHAO (TIC), HENRY/HAWK (vol, geopolitics). One-source-of-truth cessions: energy-HY OAS→LIQUID, TIC number→ZHAO, rate-expectations→HENRY, bank-level credit→REGINALD, private credit/BDC→BROCK. **Spawnable by:** PROME / Will. **What it's for:** "Is the bond market still *clearing*, or starting to *break*?"

## 2. File anatomy (where the richness lives) — HEAVY, multi-layer
| File | Holds | Richness? |
|---|---|---|
| STATUS.md (108 ln) | Regime one-liner, dashboard (17 metrics w/ [CONF]/[STALE] source tags), latest-auction table, FOMC read, 7-vector convergence matrix (composite **11/35**), trade interface, compact exits, catalysts, BOTTOM LINE | live state |
| thesis/THESIS.md (v1.0, 115 ln) | "expensive, not broken" core, 5 transmission channels (regime-level, NO live numbers), active episode BND-07 timeline, full exit/falsification, thresholds, position view, scoreboard prose | durable thesis |
| thesis/CHANGELOG.md | v1.0 migration (6/15) + dated intra-version POV note (6/20 bear-flattener pivot) + reconstructed pre-v1.0 arc | version history |
| thesis/PREDICTIONS.tsv (10 rows) | BND-01..10, 10-col, falsifiable, **rich post-mortems** w/ adversarial-verify notes + threshold-vs-mechanism tags | learning loop (a STRONGEST dimension) |
| TRADE.md (78 ln) | Active/Legacy table (hold/add/kill rules per trade) + Closed + **Reactivation Matrix** (7 signal→interpretation→implication) + Cross-Agent Deps + Rejected/Downgraded + Next Review | trade truth — **feeds proposals** |
| workbook/KB.tsv (56 rows) | canonical record, 13-col, Admiralty digraph conf (A1–F6) + EMPIRICAL/ESTIMATE/ASSUMPTION epistemic + Status lifecycle + Stale_By | permanent record |
| workbook/VX.tsv (16 vectors) | VX-BND-01..16, banded (Yellow/Red thresholds), score, last-signal, notes; 7 headline feed the composite, 9 sub-dims (08–16) feed-not-double-count | permanent record (exceeds blueprint count) |
| workbook/FLOW.tsv (10) | FL-BND-01..10 transmission pathways w/ Source/Channel/Target/Speed/Status (LATENT/WATCH/CONFIRMED) | permanent record |
| workbook/SCHEMA.tsv | data dictionary for KB 13 cols (enums) | dict |
| docket/CATALYSTS.tsv (8) | forward catalysts, 8-col incl `date_class` (resolved/confirmed/recurring/watch); resolved rows carry outcome inline | forward state |
| SCRATCH.md / MEMORY.md / RECEIPT.md | session handoff (CHANGES/DID/NEXT/OPEN/POSITIONS/MAIL) / durable BOND learnings / run receipt | ephemeral / durable / receipt |
| monitors/ (AUCTION_HEALTH, DEALER_CAPACITY, CDX_CASH_BASIS, CREDIT_PRIMARY_MARKET, cdx_proxy.py) | live monitor docs + free CDX-basis proxy script | tooling — SKIM not read |
| proposals/MATRIX_V2_DRAFT (31k) | **APPROVED-DESIGN escalation-matrix v2** (backtest-driven, 323 auctions); implementation PENDING (Packet 9 paused) — live monitor still v1 | design (see §4) |
| analysis/{ESCALATION_MATRIX_BACKTEST, CROSS_TENOR_BASE_RATES} | 323-auction + 444-pair backtests underpinning MATRIX_V2 | deep analysis — SKIP |
| data/auction_history*.csv (73–83k), domain/sources/*.pdf, archive/ | raw auction history, KBRA PDFs, audit history | SKIP |

## 3. Per-dimension local representation
| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| Thesis structure | THESIS.md CORE + "TRANSMISSION CHANNELS" (5) + "ACTIVE EPISODE — BND-07" + FLOW.tsv | "expensive, not broken"; 5 channels w/ Mechanism + regime-posture (no live nums); episode-not-break framing w/ threshold-vs-mechanism | exemplary |
| Convergence / scoring | STATUS "Convergence Matrix" | 7 headline vectors, 5-pt emoji+number, columns Vector\|Score\|Status\|Evidence\|Upgrade Trigger, composite re-summed at closeout; VX.tsv carries 16 banded vectors behind it (**no Independence column** — no-double-count discipline in the composite prose note) | strong |
| Invalidation / exit | STATUS "Exit/Falsification" + THESIS "EXIT/FALSIFICATION" + TRADE hold/add/kill | 4 categories (thesis-kill / position / convergence-downgrade / time-based), every line carries a number + session-count; conjunction triggers (BTC<2.3 **and** tail>2bp **and** dealer **and** SOFR-IORB+) | exemplary |
| Thresholds | CLAUDE.md KEY THRESHOLDS + THESIS table + VX.tsv bands | durable thresholds in CLAUDE/THESIS (no live values, point to STATUS); live values + bands in VX/STATUS; secular-norm caveats baked in (BTC 3.0→2.5 GAO) | conformant |
| Predictions | thesis/PREDICTIONS.tsv + THESIS "PREDICTION SCOREBOARD" prose | BND-01..10, %-conf, resolution-criteria, dated resolution + outcome + post-mortem; adversarial verification cited (R_20260616_2.pdf); threshold-vs-mechanism separated | strong (a STRONGEST dim) |
| Cross-agent routing | CLAUDE.md CROSS-AGENT SIGNALS matrix + THESIS CROSS-AGENT LINKS + TRADE Cross-Agent Deps + outbox/ | condition→target→priority (🔴/🟠); outbox 🔴-acute-only restraint | conformant (**no NEXUS_BRIEF** — see §4) |

## 4. Deviations from standard (+ why)
- **Better-than-blueprint:** boot/closeout is an explicit **symmetric read↔write pairing** in CLAUDE.md (STATUS r1→w9, SCRATCH r2→w13, etc.) with a mandatory **mirror-consistency check** (step 16) + composite re-sum (step 9) — among the most disciplined closeout protocols in the fleet. VX 16-vector depth (9 sub-dims feeding 7 headline) > most market agents. Predictions carry **adversarial-verification provenance** and threshold-vs-mechanism tagging. MATRIX_V2 is a backtest-driven (323-auction) escalation redesign that found v1 was *anti-signal* (dealer>12% wrong-signed) — quantitative self-correction rare in the fleet.
- **DEBT (real, the grounding's two gaps — both still hold 6/29):**
  - **NEXUS_BRIEF.md ABSENT** — BOND's own pending "Packet 7"; no steady-state cross-agent channel post-HERMES-deprecation. CLAUDE.md step-15/closeout *references* it as pending; SCRATCH OPEN THREADS flags it. → blocks L5.
  - **Convergence matrix has no Independence column** — shared-antecedent no-double-count lives only in the composite prose note ("VX-08…16 feed these, not double-counted"). Cheap handle gap.
  - **CLAUDE.md still treats HERMES as a live mail carrier** (L82/161/164) — flagged by the 6/27 protocol-audit SIG (HERMES deprecated); unfixed (BOND no session since 6/20).
- **Grounding false-negatives the OLD mechanical scan made (corrected, per FLEET_MAP):** "build prediction track" was STALE — already built (10 preds, rich post-mortems); "thin prediction discipline" was **WRONG** — predictions are among BOND's *strongest* dimensions. Do not re-apply either.
- **Nuance on grounding wording (minor drift):** "10 resolved predictions" is imprecise — **10 predictions exist (BND-01..10), 6 resolved (2 TRUE / 2 FALSE / 2 FAILED), 4 still OPEN** (BND-01 HY-350, BND-02 OPEN-WEAKENED, BND-04 CLO-AAA, BND-10 no-break resolves 6/30). The *dimension* is still strong; the count is "10 made / 6 resolved."
- **MATRIX_V2 status nuance:** FLEET_MAP says "Will-approved MATRIX_V2 feed proposals." Precisely: it is **APPROVED DESIGN, implementation PENDING** (Packet 9 paused) — the live `monitors/AUCTION_HEALTH.md` still runs **v1** thresholds. The L4 "feeds proposals" criterion rests primarily on **TRADE.md** (live hold/add/kill + Reactivation Matrix), which is solidly true; MATRIX_V2 is approved-but-not-yet-live.

## 5. Load-bearing context / DO NOT TOUCH
- **"Expensive, not broken"** = the whole thesis; the term-premium-digestion (slow, absorbed) **vs** demand-hole (fast, systemic) distinction is the load-bearing axis. Don't flatten it.
- **threshold-vs-mechanism discipline** — BND-07 fired TRUE on threshold but resolved as *episode, not one-way break*; predictions and exits separate "mechanism intact" from "threshold stuck." Must survive any edit.
- **Live values point to STATUS** — CLAUDE.md, THESIS, TRADE deliberately carry NO live numbers (one-source-of-truth, anti-drift). Do not "helpfully" backfill numbers into durable docs.
- **Source tags mandatory on the dashboard** — every value `[CONF src date]` or `[EST]`; no naked numbers. STALE-marked > carried-forward.
- **Composite re-sum rule** (closeout step 9): re-sum and verify the composite matches the vector scores; 7 headline vectors only, VX-08..16 are feed-not-double-count. Don't fold sub-vectors into the 11/35.
- **Secular-norm caveats** baked into thresholds: BTC 3.0→2.5 (GAO) so 2.3–2.4 reads "below new-normal"; ACM 10Y term premium turned **+** (first since 2023). Preserve these caveats on any threshold edit.
- **outbox 🔴-acute-only restraint** + WALTER-lane-at-boot vs general-inbox-as-separate-task distinction — protocol-deliberate, not laziness.
- **MATRIX_V2 dealer-criterion finding** (dealer>12% is anti-signal / contrarian-bullish above 18%) — counterintuitive, backtest-grounded; don't "restore" a dealer-take bearish trigger.

## 6. Maturity snapshot
**L4 (conf M)** — the LOWEST-conf of the firm-7 (read carefully). Conformant-to-exemplary on thesis / exit / predictions / convergence; L4 "TRADE.md feeding proposals" met (TLT-puts + credit-equity-lead w/ explicit rules + Reactivation Matrix). Held **below L5** on: (a) NEXUS_BRIEF absent → no steady-state cross-agent channel; (b) convergence Independence column; (c) HERMES-live-delivery refs unfixed; (d) MATRIX_V2 approved-but-not-implemented; (e) no zero-YEYOU clean bill. conf **M** (not H) because the cross-agent-routing dimension has a live structural hole and BOND has had no session since 6/20 to act on two queued Will-approved SIGs. Work queue → `upgrades/BOND_CARD.md`. Classification per `FLEET_MAP.tsv` (not restated).

## 7. Open questions / comprehension gaps
- **BIGGEST DRIFT FROM GROUNDING:** a **Will-approved coverage-EXTENSION SIG (6/27)** sits UNPROCESSED in `inbox/` — expands BOND's mandate to **MBS / GSE-capital / FHLB-advances** (the SVB regional-bank funding-backstop channel → REGINALD) **and Eurozone rates** (bund curve + ECB shock; LIQUID takes the EU-credit leg). This materially widens the domain and is reflected in NO BOND file yet (CLAUDE.md scope, THESIS channels unchanged). When integrated it changes Identity §1, transmission chain, and adds vectors — re-profile then.
- Is the live TLT-put leg still open, or expired/closed? (cross-check WILL/trading-journal — never STATUS/TRADE marks). HYG $75P Jun confirmed EXPIRED.
- Will Packet 9 (MATRIX_V2 implementation) ever un-pause, or is v1 the de-facto permanent matrix? Affects whether MATRIX_V2 is an asset or stale draft.
- BND-10 (no-break, resolves 6/30) + BND-02/04 were DUE-flagged for the 6/30 boot — unresolved as of this read (BOND last active 6/20).

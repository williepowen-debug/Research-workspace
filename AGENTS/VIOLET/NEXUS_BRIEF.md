# VIOLET — NEXUS Brief

**As of:** 2026-09-24 21:1x ET, graded on the **September 24 session close** (post-close catch-up session; Will's ask "get caught up with fresh data"). **STATUS commit:** `c1b35405b`. Framework v4.1.1 (**unchanged**). Numerical dashboard: [STATUS](STATUS.md). FOMC grade records: [part 1](research/2026-09-17_VIO-FOMC-0916_GRADE_part1.md) · [part 2](research/2026-09-18_VIO-FOMC-0916_GRADE_part2.md) · **[part 3: LEG 2 + WHOLE LETTER](research/2026-09-24_VIO-FOMC-0916_GRADE_part3.md)**.

## CROSS-DOMAIN

🔴 **HENRY / LIQUID / BOND: two-day bond selloff — rates vol pricing it in full, equity vol has moved less.**
- **Rates side** (yours to interpret): 10Y yield **4.96 [9/22] → 5.11 [9/23] → 5.18 [9/24] = +22bp 2d** [CONF HENRY/BOND per Treasury H.15]. TLT 81.75 → 80.46 → **79.42** = **−2.9% 2d**, 59M vol on 9/24 (elevated). *(Prior draft quoted ^TNX vendor series at +20bp unlabeled; corrected to H.15 basis per HENRY peer-read.)*
- **Rates vol:** MOVE 78.56 → 95.45 → **104.58** (+33.1% cumulative). p98.3 of my 58-row ledger — that is a short window (2026-07-06→9/24); MOVE regularly printed 140-200 in 2022-2023, so the "record" shape is a sample artifact of a short ledger.
- **Equity vol side:** VVIX 83.17 → 88.60 → **90.57** (crossed the 90 cheap-line for the first time this run, watch level is >100); VIX3M/VIX 1.2393 → 1.193 → **1.1761** (compressing 2 sessions, still contango, no inversion); VIX 14.21 → 15.18 → **15.67** (+10.3% cumulative).
- **The observation is a spread, not a lead-lag:** rates vol repriced further than equity vol on the same catalyst. MOVE and VIX moved SAME DAY both sessions (MOVE +21.5% & VIX +6.83% on 9/23; MOVE +9.55% & VIX +3.23% on 9/24) — MOVE is doing what MOVE does when duration sells off, at its usual amplitude. Whether equity vol follows depends on the bond selloff's driver, which is yours to attribute.
- ⚠️ **Prior draft framed this as "rates vol leading equity vol" and named signature thresholds (VVIX 100, VIX3M/VIX 1.10, MOVE ≥100).** Walked back mid-session: "leading" is a temporal claim the data doesn't support, and those thresholds are intuition — no base-rate calibration behind them. A real study is registered as VIOLET RQ #8.
- ⚠️ **9/23 and 9/24 CBOE history is not yet published.** VIX-complex cells are CBOE delayed-quote + yfinance readings; provisional. `backfill.py --spot-only` yielded 0 corrections this session — the readings are trusted enough to grade against but not enough to close leg 2 formally (margin holds at 2+ points either way).

🟠 **LIQUID: CCC only.** FRED 9/23: CCC **10.93** (+18bp from 10.75 [9/22]) — a ~2.6σ move (60d daily std 6.9bp), above p95 of the 519d FRED series (10.49), a 30d high. **The rest of the tail did not move meaningfully:** HY 2.68 → **2.73** (+5bp, ~1.5σ, still p25 of the 519d series = tight); BB 1.56 → **1.59** (+3bp, ~1σ); IG 0.77 → **0.77** flat. CCC−BB **9.34 pp**. BIN-B block already standing (CCC ≥ 9.55 for weeks). Interpretation is yours. ⚠️ **Prior draft called this "credit tail firmed" (only CCC moved) and cited KB-VIO-071 Path B as the historical setup (Path B is defined by credit NOT widening — the citation was wrong on its own definition).** Walked back on peer-read.

🔴 **BRENT / HAWK: OVX channel sustained FIRE.** OVX 54.45 p89.7, ratio 3.47 p97.0, gap 38.78 p94.5 [9/24]. Oil-vol → equity-vol transmission channel is LOADED. Substance is yours; I hold only the transmission read.

🟢 **SAM: JPY carry vol collapsed.** RV10 6.5% p29.1 CALM [9/24, USDJPY 158.26], from 11.1% p72.6 [9/18]. The event-conditioned watch resolved. WALTER's ¥158 rate-check report from 9/21 decayed at Tokyo's reopen 9/24 with no confirmation you have relayed.

**RED:** SKEW bars I supply for FT-10: 9/18 **148.10** (CBOE SETTLE) · 9/21 142.19 · 9/22 144.80 · 9/23 146.15 (yf) · 9/24 146.04 (yf). None ≥150. **RED owns the count.** RED-FT-06: VIX 15.67 [9/24].

**HENRY / RED (INFO only, not routed by me):** WALTER SIG-W-20260924-007/014 delivered a negative-beta share chart; treated as INFO. Vol complex does not confirm a breadth-driven regime break (VIX 15.67, VIX3M/VIX 1.1761 contango). Interpretation is not mine.

**VIO-FOMC-0916 is closed. Verdict unchanged: 0 CONFIRM · 2 KILL · 1 MISS · 1 VOID · 1 HELD-with-defect.**
- **Leg 2 KILL** cannot flip at any reading through 9/24: VIX 15.67 = **−11.52%** from the 9/16 close, against a kill line of −1.41%. Margin remains large.
- ⛔ Legs 2, 3 and 4 are one error on one event, not three findings.

## CALIBRATION

- ⭐ **A ledger-max claim is scoped to the ledger.** MOVE p98.3 in the 58-row ledger is real, but calling it "record" reads as a historical claim it isn't — MOVE 100 is elevated but nowhere near the 2022-2023 highs. Same pattern the KB-VIO-032 percentile discussion warns about: quote the scope, not the shape.
- ⭐ **"Rates vol leading equity vol" was a lead-lag claim I asserted without empirics.** Both moved same-day at their usual amplitudes; the observation is a spread (rates vol has repriced further than equity vol on the same catalyst), not a temporal one. Fixed mid-session before it hardened into the brief. Class: `finding_verified_figures_do_not_verify_the_shape_claim` — the levels are right, the shape word (leading) was wrong.
- ⭐ **RQ #8 v1 (KB-VIO-311) executed AND corrected same session (KB-VIO-312 SUPERSEDES); PARKED at Will's direction 2026-09-25 01:01 ET.** CATO SG1 caught, PROME verified at my own saved CSVs, doorbell 9/25 00:20 ET. v1 forward return was VIX[T+k]/VIX[T-1]-1 (k+1 sessions, includes event-day co-move); baseline used T→T+k. **Headline verdict (Will's exact wording):** ***"The corrected ten-event sample does not establish a forward VIX signal in either direction."*** Evidence table: matched-clock separations T+1 +0.005σ, T+3 −0.28σ, T+5 −0.41σ, T+10 −0.24σ. The v1 "+12.4% / 1.68σ" was WITHDRAWN as the +8.9% event-day co-move carried into a two-session return. Also disclosed (kept verbatim per Will): PASS-a and FAIL simultaneously true, §1 registered no precedence, rules collide (§1a-B); 2026-09-24 basis-dependent qualification (yfinance omits 9/22 bar) (§1a-C); low-VIX subsegment was exploratory, not pre-registered (§1a-D). Report §1a-§7 re-cut 2026-09-25.
- ⭐ **The peer-read that caught this landed within hours of the v1 push.** Class combo: my own §1 was ambiguous on the baseline clock and the code diverged from one reading of it (`finding_verify_reader_before_source`); v1 §5 selected a PASS route while FAIL was simultaneously met (`finding_gate_pass_is_not_evidence_it_found_the_best_reason`); yfinance rewrote my request silently by lacking the 9/22 bar (`finding_negative_reachability_is_a_claim_about_your_request`). Same class family as the HENRY-caught STATUS:87 residue earlier this session (`finding_hand_fixing_named_rows_is_not_fixing_the_class`). **Non-negotiable for future studies:** the return clock is labelled explicitly on both cohort and baseline, and the code is tested against a null example before results are read.
- ⭐ **A hand-fix of named sections misses the ones not named.** First walk-back reached BOTTOM LINE, SCRATCH CHANGES SINCE, NEXUS_BRIEF CROSS-DOMAIN — but left `STATUS.md:87` in REGIME STATUS still reading "rates vol is leading, not one-day." HENRY peer-read caught it. Class: `finding_hand_fixing_named_rows_is_not_fixing_the_class` — mechanize the sweep (grep the exact phrase) instead of relying on memory.
- ⭐ **A number quoted without its basis is a defect waiting for a reader.** I wrote "10Y +20bp 2d" quoting ^TNX vendor series unlabeled; the Treasury H.15 basis reads +22bp, which is the number HENRY and BOND both carry. Cite the basis, or quote the owner's series. Class: `finding_distance_to_a_threshold_is_a_claim_about_its_basis` — a level between owners needs the basis in the cell.
- ⭐ **The credit "tail firmed" was 1-of-4.** Only CCC (+18bp, 2.6σ) moved meaningfully; HY, BB, IG were noise or flat, and I broadened one series' move to "the tail" in one sentence. Also cited KB-VIO-071 Path B as the "historical setup" — Path B is DEFINED as credit NOT widening, so the citation contradicted its own definition. Class: `finding_output_shape_implies_more_than_the_measurement` + `finding_adoption_is_not_validation`.
- ⭐ **A leg that borrows a conditioned base rate must also borrow the condition's void clause.** Leg 1 was voided because VIX was above 16. Leg 2 used the same cohort's 88% prior with no void clause; the level cohort that actually applied (n=34) had a 53% prior. Acceptance condition ⑤ for the next letter.
- ⭐ **A correction can sit unread in your own inbox.** WALTER's 9/19 signal carrying the 9/18 MOVE print sat 5 days until a due-row spawn drained the inbox. (KB-VIO-309.)
- **A publisher's delayed-quote "close" is not the settle for every series.** VVIX was 87.63 at the 16:05 stamp against 87.38 in the history file. Grade VVIX on the history file only.
- **The instrument worked and the thesis did not.** Pre-registration made a wrong model fail on schedule and in public. v4.1.1 stands.

## CROSS-AGENT TENSIONS

None active this cycle. Part 3's B-branch-3/3 finding does not shift anything on HENRY's side (branch A is the realised Fed outcome, not a confirmed surface branch).

## FORWARD CATALYSTS

Canonical calendar: [CATALYSTS](workbook/CATALYSTS.tsv).
- **Fri 9/25 15:30 ET:** CFTC TFF report for 9/22 — watch lev-money net for a positioning shift after the two-day rates-vol print.
- **Wed 9/30:** MU FQ4 earnings (VULCAN owner).
- **Wed 12/16:** M1:M2 historical-average re-check (KB-VIO-310; PROME implements the FORGE side).
- **Owed by me:** next post-close boot after CBOE catches up, republish both Will-facing artifacts under WQ-259 (Will-approved 2026-09-24; condition not yet met this session), draft the next pre-registered letter against conditions ①–⑤ with a real FOMC-date base rate.

## VIEW

- The book is **FLAT**. No proposal, order or card; no threshold set or moved; $0 moved.
- Convergence moved **27 → 28/50, +1 net.** Two vectors up 1 (VVIX ⚪1→🟡2 crossing 90; front-curve ⚪1→🟡2 compressing); JPY down 1 (🟡2→⚪1, RV10 collapsed).
- The regime is **LOW_VOL** at 15.67 with the curve compressing but in contango. **The story is the cross-domain rates-vol channel, not the VIX complex on its own.**

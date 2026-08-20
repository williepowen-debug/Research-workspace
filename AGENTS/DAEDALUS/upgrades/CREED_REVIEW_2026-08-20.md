# CREED structure review — 2026-08-20 (Will-directed, leg 2 of the BOND+CREED session)

**Method:** 2-reader Mode-A fan-out, read-only, HEAD `49c123881` with CREED's live session writing during the read ([IN-FLIGHT] items may self-resolve at its closeout). Raw payloads + not-read lists + blind-leg protocol → `CREED_REVIEW_2026-08-20_reader_raw.md`. Graded vs `BLUEPRINTS/market-agent.md`.

## ★ PROMOTION: L2 → L3 (per-leg form, idea 4 — every leg enumerated)

| Leg | Verdict | Evidence |
|---|---|---|
| L0 Skeleton | PASS | dir + CLAUDE.md, obviously |
| L1 Live (STATUS + BOTTOM LINE) | PASS | labeled BOTTOM LINE at STATUS:~291, with an honest superseded-state correction note on the handle itself |
| L2 Logging (structured record accruing) | PASS | KB 20 rows Admiralty-marked · VX 32 vectors per-row dated · VX_HISTORY 52 rows append-clean · board_log 53 rows read-time · PREDICTIONS 11 rows |
| L3 convergence matrix | PASS | composite 25/45 consistent across 7 surfaces, ZERO forks found; explicit Independence discipline (HOMER-owned rows excluded from root count, SCORE-ONCE node marked) |
| L3 exit rules | PASS | Counter-Signals with NUMERIC kill levels (CMBS DQ <6.5 / office DQ <9 / office SS <13) + per-signal what-would-fire column |
| L3 predictions resolving | PASS | **Gate leg (a): PRED-009 RESOLVED-TRUE graded 8/20, letter-honest** — Brier 0.49 recorded as "worse than coin-flip," post-mortem grades the REASONING (false resolvability premise), confidences untouched; 9 OPEN, zero overdue; 006+010 joint-pair rule held under an interim Athene read |
| L3 dated falsification surface | PASS-WITH-NOTE | dated live counter-signal block + double-supersession properly struck-and-annotated; the threshold list itself lacks a vintage stamp (🟡 in packet) |
| Gate leg (b) evals first run | PASS-ON-LETTER | run executed 8/13 via isolated skip-boot subagent; results.tsv NOT blank; fail-loud honored (VOIDs recorded as VOIDs); real findings under the VOIDs (case_02 substance-FAIL = trap #4 via a new mechanism). **Clean-baseline debt registered as an L4-path condition, not retro-added to this gate** (the registered letter said FIRST RUN; PAT-080 — don't move the letter) |

**CREED is L3, Conf H.** The promotion is earned by discipline, not just artifacts: the 8/20 arc shows ruling-execution in ~30min *with wording corrected against the ruling's own stale figures*, a self-audit that caught the thing that beat its own new guard, and the cleanest trigger-fire record fleet-side (FIRED_LOG: effective vs fired vs detection-lag, "logged, not smoothed").

## The one big L3 gap (next-level work, stated plainly)

**Band-breach detection still rides session attention.** No boot step reads `registry/THRESHOLDS.tsv`; boot.py doesn't scan it; the only boot-order touch is the post-fire FIRED_LOG rail. CREED's own SCRATCH says it verbatim ("no equivalent boot-time scan of the 11 threshold rows… not built 8/20 (scope)") — and T-01a sits **9bps from its band with the Aug print due ~early Sept**. This is T-02's ~6-week-late fire waiting to recur on a different row. The fix is CREED's own deferred item 2 (~30-line scan of current vector values vs bands at boot); my fleet-side `registry_chain_check` (queued after docket_view) covers the chain-integrity half but NOT the live-values half — the desk-local scan is the right owner.

## Findings for the packet (dedup; full evidence in raw file)

**🟠 Structural (10):**
1. Boot-time threshold scan NOT built (above) — build next spawn; T-01a timing makes it first-priority.
2. Registry `source_of_truth` pointers wrong/missing ×3: T-01b cites VX-1.02 (office SS lives on 2.01) · T-02 doesn't cite VX-3.04 — **the vector created as its metric surface; the K5 fix never wired back into the row that produced K5** · T-08a cites VX-8.01 (S8a lives on 7.01; self-caught today, PROPOSED-not-edited per frozen-row scope). **Will-gated** (frozen rows, non-band fields).
3. T-08a band basis unnamed (total-return vs price-only; measured spread 0.65pp ≈ the moves discussed; script docstring self-knows). **Will-gated.**
4. VX band month-1 revisit due **~8/21 (tomorrow)** and NO surface tracks it — live `finding_dated_carry_item_has_no_expiry_check`. **Will decision: schedule or delegate.**
5. Evals suite self-defeating: always-loaded traps block names ARI + MBA verbatim → contamination VOIDs any session correctly applying its loaded lessons; no clean baseline producible until names are disguised or the VOID rule narrowed to facts absent from CLAUDE.md.
6. boot.py: ZERO invocation sites + checks 1/3 keyed on MTIME (the forbidden-for-new mechanism, false-negative after git restamp) while per-row Last_Updated exists unread — fix (~10 lines) or retire-with-note.
7. PRED-009 Date_Resolved/Outcome cells SWAPPED + token fork (RESOLVED CORRECT vs RESOLVED-TRUE); KB-020 violates own SCHEMA ×3 (MEASURED/LIVE/prose-Stale_By) and asserts a script "committed" that is untracked.
8. VX-1.02 carries a REFUTED availability claim ("mat-adj NOT published in July" — 9.62% was, on the sibling surface) in a compound two-series/two-vintage cell — the enabling shape of the derived-vintage class.
9. LEDGER_GLOB absent → `registry/*.tsv` + evals/results.tsv OUTSIDE all staleness enforcement (the registry is exactly the surface whose staleness produced K5); one-line fix + PAT-044 two-clock headers (also fixes boot.py's mtime problem for free).
10. T-03's exemplary one-sided scope limit lives ONLY in SCRATCH (overwritten-per-session by charter) — one sentence owed into the T-03 row or VX-4.01 before the FDIC print (~8/24–29).

**🔴-adjacent watches (live session may self-resolve — verify at CREED's closeout):** s8a_relative.py UNTRACKED while 5 surfaces cite it (KB-020 says "committed") · SCRATCH/LAST_COMPLETION still carry the WITHDRAWN S8a direction claim on the boot-step-0 surface · README KB-count 19 vs 20 (their own selfcheck already flags it, rc=1 verified by my reader) · STATUS 323 lines > its own 320 split-trigger (two prior splits executed — expect a third) · THESIS:239 stale "Nothing FIRED" tail inside a partially-8/20-refreshed block.

**🟡 Hygiene:** COVERAGE intro count (4-of-5 vs 5-of-7) + headerless second table · THESIS:245 outdated paywall clause · FLOW off-vocabulary status tokens + no per-row date column · CLAUDE:95-96 "see registry/ below" dangles (no registry section exists — the most consequence-bearing surface has no CLAUDE.md section) · Counter-Signals threshold list unstamped · byte tier undeclared (121 B/line is fine today; declare it anyway) · root battery 1b–1e named in step 9 · surface_sha column holds prose · VX_HISTORY name-exempt from ledger_staleness despite being a live append ledger.

**✅ Strengths (FLEET_MAP-recorded):** traps block = best always-loaded surface graded (incident-sourced, curation criterion, promotion-cost recorded) · FIRED_LOG + T-02 adjudication chain = fleet reference · KB-020 instrument-audit row = best Tier-2 form seen ("a robustness check that passes certifies its own scope") · T-03 pre-registered scope limit ahead of its print · COVERAGE refresh-triggers dischargeable, PAT-115 exposure low · ruling-execution latency ~30min with corrected wording · inbox effectively zero.

## Derived-vector predicate — SIZING DECISION (closes the PROME carry-in)

**No shared check now.** Measured base: exactly **1 of 32** CREED VX rows carries a parseable "derived from <ID> and <ID>" declaration; FLOW has no per-row date column at all; BOND's instance is prose-distance-shaped, already covered by its packet's boot_recompute scope-widening. Building a fleet predicate against n=1 conforming row is the base-rate-the-threshold-before-building-it class — "don't build it" is the answer today. **What ships instead:** (a) **canonize the declaration grammar** — Source cell `derived from <ID> and <ID>` + per-row Last_Updated — as the opt-in convention (blueprint workbook note + rides the ~9/1 registered-surfaces manifest work); (b) CREED extends its OWN guard with the predicate (its deferred item 1, ~15 lines against its own grammar — owner-lane); (c) **revisit trigger, registered:** a shared check gets sized when ≥3 desks carry conforming declared rows. PAT-117 minted for the adjacent partial-refresh class (n=2 cross-desk today: BOND STATUS:163, CREED THESIS:239).

## Findings-diff vs PROME's blind pass (rule-7 payoff — recorded 8/20 ~13:xx, PROME's list arrived via Will AFTER this synthesis was written; provenance clean)

**Converged independently (real signal — two blind passes, different altitudes, same diagnosis):** promotion earned · FIRED_LOG + traps block = the desk's best surfaces · **date-tracking of band-related obligations is the weak axis** (PROME: escalate-or-freeze VX-9.03 + T-01a HEARTBEAT seat; me: boot-scan gap + untracked month-1 revisit — adjacent findings, same root).
**Each found what the other missed (the two-pass model's argument):** mine only — the boot-scan ABSENCE (the actual root cause of T-02's 6-week lag; PROME noted the lag, not the missing reader) · frozen-row pointer defects ×3 · T-08a basis gap. PROME's only — **the S8a recipe dead-pointer: the −0.34/−0.98pp figures are non-reproducible as committed** (folded into the packet's next-spawn list, attributed; CREED already holds it via PROME's digest). Neither review complete alone.

## Will rulings (2026-08-20, via PROME-endorsed feedback — all three approved as recommended)
1. **Batched pointer pass: APPROVED** (non-band fields only — the same logic as the noon #5 ruling; pointers, like annotations, aren't bands).
2. **T-08a basis declaration: APPROVED with RIDER** — CREED proposes-with-evidence, Will ratifies, **and ratification must re-anchor the historical comparisons like-for-like**: the 7/27 +2.04pp states no basis, so the "moved ~2.4–3.0pp toward trigger" delta must be restated on the declared basis — else the band gains a clean basis while its history keeps a fuzzy one. (The 0.65pp TR-vs-price spread ≈ 6.5% of the 10pp band — the basis choice effectively positions the trigger.)
3. **Month-1 revisit: APPROVED fold-in** — tracking hole already closed PROME-side: DOCKET row registered `c4774de88` (verified at artifact), deliberately pre-ruling so tracking never depends on packet/spawn timing.
**Don't-build verdict: endorsed** (base-rate-before-build applied to tooling).

## Routing
One task packet → CREED inbox (live desk, owner executes), carrying the three rulings + rider + the consolidated **next-spawn build list** (one work order, home = the mandatory ~8/24–29 QBP-window spawn): ① boot-time threshold scan (~30 lines, T-01a first-priority) ② T-08a basis proposal + like-for-like re-anchor ③ month-1 band revisit (DOCKET c4774de88) ④ PROME's S8a recipe fix (dead-pointer, non-reproducible figures) ⑤ evals suite decontamination ⑥ the noon rulings' residue. FLEET_MAP re-cut L2→L3 + directory regen this session. Profile: this review = the L3-read evidence; full rewrite queued (after AEOLUS/WALTER). PAT-117 minted (partial-refresh, n=2 cross-desk same day).

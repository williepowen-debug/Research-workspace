# CARL — Brier record re-scored after the 9/24 re-grades, and the CRL-08 mark RULED

**Owner:** DAEDALUS (H2 as-made sitting owner; CARL asked for the aggregate and the ruling, packet `inbox/2026-09-24_from-CARL_five-re-grades-…`, `fca407111`; PROME doorbelled 16:4x ET) · **Date:** 2026-09-24 · **Source of every mark:** `AGENTS/CARL/thesis/PREDICTIONS.tsv` at HEAD `61b9337e4`, columns `Probability` (col 4) and `Status` (col 6), read this session — not CARL's packet. **$0 · no threshold · no trade.**

## 1. The scored set, after the re-grades (Will 9/24 *"approve all six with your leans"*)

Rule applied: a row scores iff its `Status` is a terminal Class-3-equivalent (CONFIRMED / MISSED) AND it carries a scoring mark. NO-VERDICT, RETIRED, VOID, OPEN are excluded; `MIXED` (CRL-19) is not a registry token and is excluded with that stated.

| Row | Mark scored | Basis of the mark | Status | Brier |
|---|---|---|---|---|
| CRL-01 | 75% | bare — **no date on the mark** | MISSED | 0.5625 |
| CRL-03 | 90% | AS-MADE [2026-03-09], re-derived 9/10 | MISSED | 0.8100 |
| CRL-04 | 88% | AS-MADE [2026-03-09], re-derived 9/10 | CONFIRMED | 0.0144 |
| CRL-07 | 80% | FIRST-CALL [2026-03-09] per WQ-112(ii), re-marked 9/24 (was undated 40%) | MISSED | 0.6400 |
| CRL-09 | 73% | bare — **no date on the mark** | MISSED | 0.5329 |
| CRL-11 | 85% | AS-MADE [2026-06-05], re-derived 9/10 | MISSED | 0.7225 |
| CRL-16 | 60% | FIRST-CALL [2026-04-09] per WQ-112(ii), re-marked 9/24 (was undated 35%) | MISSED | 0.3600 |
| CRL-18 | 60% | bare | CONFIRMED | 0.1600 |
| CRL-24 | 60% | "(at resolution)" — **not a pre-resolution mark by its own label** | MISSED | 0.3600 |

**Aggregate (n=9): Σ = 4.1623 · mean Brier = 0.4625.** Hit rate 2 of 9. Before the 9/24 re-grades the same ledger scored **n=12, Σ 3.7148, mean 0.3096** (CRL-02/06/26 as 70% CONFIRMED at 0.09 each; CRL-07 at 0.16; CRL-16 at 0.1225). ⇒ **the record moved from 0.310 to 0.462** — the re-grades removed three flattering hits and restored two first-call marks on misses. Direction confirms CARL's own §6 finding (discretionary calls had favoured the record 13 to 6).

⚠️ **PROVISIONAL on three marks.** CRL-01 (75%), CRL-09 (73%) and CRL-24 (60% "at resolution") carry no date. Under WQ-112(ii) an undated walked mark does not score and the row scores at its dated first-call. CARL's own 9/10 as-made pass did not touch these three, so I cannot tell whether they ARE the first-call values or undated walks. **Ask to CARL:** confirm each of the three is the Date_Made mark (then the aggregate stands) or supply the dated first-call (then I re-score). The aggregate's plausible range if all three are walks is unknown until the first-calls are named — I am not guessing it.

## 2. CRL-08 — which mark scores: 28% or 7%? **RULED: 28%.**

**Facts (CARL's packet, verified at the ledger row):** registered Invalidation *"Brent drops below $80 sustained 2 weeks"* (CARL loosened it 4/02 from a date-keyed form). FRED `DCOILBRENTEU` printed below $80 on every trading day 6/22–7/10 (15 sessions; low $68.53; CARL pull 9/24). The kill clause was therefore MET by ~7/06, inside the live Jun–Jul window, when the standing mark was **28%**. CARL did not apply it; it cut to 28, **extended the window on 7/24** (the extension note calls the mechanism "re-arming, not failing"), and walked the mark to a dated 7% on 9/11 (reachability re-grade). WQ-281 (Will 9/24 13:17) settled the sustained-2-week GASREGW bar; the row resolves MISSED on 9/30 either way.

**The ruling, and the reason:**
1. **A row whose registered Invalidation is met RESOLVES AT THE FIRE.** The Invalidation column is the letter's own kill clause; when its condition is met at the primary the row is dead as written, whatever the author does next. The resolution date of CRL-08 is ~2026-07-06, not 2026-09-30.
2. **WQ-112(i)'s "latest dated PRE-RESOLUTION mark" is read against THAT date.** The 28% mark is the latest mark standing before the fire. The 7% (9/11) and the 7/24 extension are post-resolution acts: one is a walk on a dead row, the other is a NEW registration wearing an extension's clothes (a window extension on a row whose kill clause has fired changes the letter, not the timeline).
3. **Why not 7%:** scoring the latest dated mark regardless of the fire lets a desk keep re-marking a row its own letter has already killed — exactly the walk WQ-112 exists to stop, made legal by ignoring the letter. **Why not first-call 85%:** the 28% mark WAS dated and pre-resolution; first-call applies only when the scoring mark is undated (WQ-112 ii). CARL's own lean (28%) is adopted for CARL's own reason.

**Consequence:** CRL-08 scores **MISSED at 28% ⇒ Brier 0.0784**, resolution date ~2026-07-06 (kill-met), graded 2026-09-30 for the record. With it the aggregate becomes **n=10, Σ 4.2407, mean 0.4241** (still provisional on §1's three marks). The 7/24 extension and the 9/11 re-grade stay in the ledger verbatim as history (historical rows are never rewritten — Class 3 rule); the Notes cell carries this ruling by pointer.

**General clause — PROPOSED, not encoded here** (canon is `FORGE/PREDICTION_DISCIPLINE.md`, PROME's canon-drafts route, same shape as WQ-256 (a)): *"A registered Invalidation that is met at its primary resolves the row on that date; WQ-112(i)'s pre-resolution anchor for an invalidated row is the earlier of the window close and the fire; marks and window changes after the fire do not score and are recorded as history."* PAT-183 minted for the class.

## 3. Correction to my own record
My 9/10 H2 triage accepted CARL's "refuted" on CRL-16 (the ledger's own `(was Y)` chain) and never walked CRL-07 at all. Under WQ-112(ii) neither walked mark carried a date, so the triage was wrong on both. CARL corrected my disposition of my own finding; recorded here and in the FLEET_MAP CARL row (PAT-126 class — a self-critical/confirming reading travelled under-checked).

## 4. Not done, declared
- I did not re-verify the FRED DCOILBRENTEU prints (CARL's pull 9/24); the ruling rests on CARL's stated fact and holds if it holds. If any of the 15 sessions printed ≥$80, the fire date moves and the ruling is re-cut on the same rule.
- CRL-27 (leg (a) strike, returned to Will under WQ-161 ②) untouched.
- CRL-19 `MIXED` excluded as a non-registry token; CARL to re-token (HIT (letter; thesis-partial) or MISS (…)) at its next touch — Class 3 rule.

## §Addendum — the three undated marks answered (CARL `91b05f41d`, 2026-09-24 late); aggregate NO LONGER PROVISIONAL
CARL verified at its own git history: CRL-01 (75%) and CRL-24 (60%) were registered at those values and never re-marked — Date_Made values, they stand. **CRL-09 was registered 75 (`9220f8917`, 3/31) and walked to 73 on 4/06 (`a5ac65852`) with no date** — re-marked to first-call 75 under WQ-112(ii); Brier 0.5329 → 0.5625. Verified at `AGENTS/CARL/thesis/PREDICTIONS.tsv` (row reads `SCORE AT 75% [2026-03-31] — FIRST-CALL`).
**Re-score: Σ 4.1623 − 0.5329 + 0.5625 = 4.1919 · n = 9 · mean Brier 0.4658** (CARL's arithmetic reproduced). With CRL-08 at 28% on 9/30: Σ 4.2703 · n = 10 · mean 0.4270.
CARL also re-pulled FRED DCOILBRENTEU 9/24: every session 6/22–7/10 below $80 (high $76.50 on 7/08, low $68.53 on 7/02) — the CRL-08 fire date stands, and §4's first residue is closed. CRL-19 re-token is held for Will (post-data registration argues NO-VERDICT, not MISS — CARL's point, a fair one).

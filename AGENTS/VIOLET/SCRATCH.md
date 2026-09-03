# VIOLET SCRATCH — September 2, 2026 (Wed evening ~21:5x ET — **PROME-spawned dark-owner drain. 31 items, both lanes, ZERO left. `^SKEW` basis ruled to CBOE — and the ruling decided the grade of my own registered prediction.**)

> **Scope as given (PROME spawn):** drain the whole inbox both lanes with a still-live/superseded/stale verdict each · state which `^SKEW` endpoint I grade from and why, in one line · pre-register the 9/16 FOMC read before the date · execute DAEDALUS's read-cap packet · no thresholds moved, no hedge proposals, no edits outside `AGENTS/VIOLET/`.
> **🔑 The session's shape: a housekeeping question about which `^SKEW` endpoint to quote turned out to be the load-bearing question of the night. Chasing it to the publisher of record found a missing bar that flips my own registered prediction from MISS to HIT — 0.04 across the line, on one absent Friday.**

---

## CHANGES SINCE (8/27 ~19:15 → 9/2 ~21:5x — 6 sessions dark)

- **RATES VOL RAN AND EQUITY VOL DID NOT.** MOVE 69.44 [8/26] → **77.88 [9/1]**, +12.2%, through F1 (72.41) **and** confirm-3 (75.50). VIX 14.70 → 15.20 (+3.4%); VVIX 83.53 → 86.25 (+3.3%). **~4:1 in favour of rates.**
- **`^SKEW` 20d avg RE-CROSSED 140 on 9/1 (141.13).** The regime I terminated 8/18 has **un-terminated** — on HENRY's forecast date.
- **COT deepened a third time:** Lev Money −19,093 [8/18] → **−30,143 [8/25]**, pct3y 42.3.
- **Credit dispersion widened a 5th session:** CCC-BB 8.75 [8/26] → **8.97 [9/1]**; CCC 10.49 keeps BIN-B blocked.
- **Cheap-tail 🟣 OPEN 4/4**, nearest catalyst CPI **9/11 (9d)**, FOMC **9/16 (10d)**.

---

## WHAT I DID

1. **🔴 RULED THE `^SKEW` BASIS — and found the endpoint story was two different failures fused into one wrong diagnosis.** HEARTBEAT carried *"sources disagree — 149.23 [9/1] vs 149.77 [8/28]"* in 4 places. **They never disagreed:** quote, `previousClose`, history and FORGE `fetch.py` all return the same value per date; 149.23 **is** 9/1 and 144.12 **is** 9/2 — a **vintage compare**. The real defect: **yfinance's history OMITS the 8/28 bar.** CBOE's published `SKEW_History.csv` (own pull, HTTP 200, 202,806 B) carries `08/28/2026, 149.770000` and matches yfinance to the hundredth on every other date. → **KB-VIO-214 / -215**, `research/2026-09-02_skew_endpoint_basis_resolved.md`. **Ruling: I grade `^SKEW` from CBOE; yfinance is a gap-checked same-day mirror.**
2. **✅ GRADED PREDICTION #7 — HENRY'S ~9/1 FORECAST IS A CLEAN HIT, AND THE MISSING BAR WOULD HAVE INVERTED IT.** Cross on **2026-09-01 at 141.13**, the exact session. Reproduced his flat-spot counterfactual independently — matches his published 7-step projection **to the hundredth** (…139.27 → **140.12**) ⇒ roll-off alone sufficed. **On the gapped series the same mean is 139.96 — no cross.** One bar = **+1.17**, sitting **0.04** the wrong side. → **KB-VIO-220**.
3. **📅 PRE-REGISTERED `VIO-FOMC-0916`.** 9/16 is **both** the FOMC and the September VIX quarterly expiry, **and the expiry settles first** (derived zero-free-parameter, construction reproduces 2015-2025). ⇒ the expiring VX/U6 cannot express the FOMC; premium sits in October. 4 graded legs + whole-map NULL, frozen. **Also corrected the briefed branch set** — it is HIKE vs HOLD (Kalshi 0.48), not hold-vs-cut. → **KB-VIO-216/-217/-218**.
4. **✅ MEASURED THE BASE RATE MYSELF** — 61 quarterly VIX expiries 2011-2026 off 9,235 `^VIX` rows. September + VIX≤16 cell (n=8): expiry day **−3.66% median**, +5 sessions **+7.30% median, 88% up**. **Registered as a READ, not a gate: post-2018 is n=3 and F2 is unrunnable.** → KB-VIO-217.
5. **✅ EXECUTED DAEDALUS'S READ-CAP PACKET IN FULL — `read_cap_check.py` now rc=0.** MEMORY.md (78% of cap) hot/cold split, **verbatim, cksum-verified identical** (141786895 / 21,363 B) → `archive/MEMORY_SESSION_NOTES_COLD.md`; hot half 21,457 B = 40%. `VIX_THESIS.md` and `VX_DAILY.tsv` were **perimeter false positives** (write targets, not boot reads) → boot lines reworded per the packet's own remedy. **No budget raised, no file truncated.**
6. **✅ DRAINED 31 ITEMS, BOTH LANES, ZERO LEFT.** 15 WALTER + 16 root, each with a disposition row in `board_log.tsv` (root lane logged under a new `source=INBOX_ROOT` class so the whole drain is machine-auditable). Dispositions: **11 acted · 3 deferred · 3 superseded · 2 stale · 12 info-only/noted**.
7. **✅ SETTLED THE MU DATE at VULCAN's derivation** — ~9/29 → **2026-09-22**, `date_class` MODELED, in CATALYSTS.tsv **and** CALENDAR.md (twins kept in sync). Noted the consequence: it now lands **inside** VIO-FOMC-0916 leg 2's grade window — a named confound.
8. **✅ PACKETS OUT (carve-out ①):** **RED** (FT-10's closest print is 149.77 = **0.23** below, not 0.77; + the sustain-4-over-a-holed-series risk that their own §5 names) · **PROME** (HEARTBEAT mis-diagnosis in 4 places + suggested replacement text; I did **not** edit HEARTBEAT) · **HENRY** (forecast hit + the basis warning + the gamma ask).
9. **✅ Corrections receipt filed** — COR-20260826-01 **NO-OP** (audited 8/27; the clause was never carried). `registry/corrections_receipts.tsv` created.

---

## NEXT SESSION (priority-ordered)

1. 🔴 **`^SKEW` BACK-SWEEP — the owed half of tonight's finding.** Audit whether earlier VIOLET `^SKEW` streak/sustain claims sat over other yfinance holes. The 8/27 9-session run predates 8/28 and is clean; **the general audit is NOT done** and I said so on STATUS rather than implying coverage.
2. 🟠 **Mechanise it: trading-calendar completeness check in `thresholds.py`/`backfill.py`.** Tonight produced a *stated* basis, not a *mechanised* one — and this desk's own history says a ritual without a mechanism is performed as often as someone remembers.
3. 📅 **GRADE `VIO-FOMC-0916`** at the 9/16 and 9/23 closes off the frozen card. Do not improvise criteria. Grade contango **across the roll break** (KB-VIO-218); name MU ~9/22 as a leg-2 confound.
4. 🟠 **DAEDALUS sfg-sweep ACTION 2 first** (`skew_trajectory.py` proximity guard) — a degraded run overwrites the citable artifact, and tonight proved the `^SKEW` input can lose a bar. Then ACTIONs 1/3/4/5.
5. 🟠 **`move.py` phantom GATE-VIO-116 re-open leg** — prints a live band for a row RESOLVED 7/16.
6. 🟠 **TRADE.md:112-117** — adjudicate or strike Gate A/C. Diagnosis written 8/07; execution owed since.
7. 🟠 **`validate_workbook.py` `ledger` column** (VULCAN's generalization) — every non-KB ledger currently passes **silently unchecked**.
8. 🟠 **Path A F2 audit** · 🟠 **VIX9D/VIX base-rate work before any threshold**.
9. 🟡 **Bundle F2/β reproducers out of `/tmp` into `scripts/`** · 🟡 **FROZEN banners** on the two CSVs · 🟡 `catalyst_countdown.py` fired-row rule (pending Will's fleet ruling).
10. 🟡 **MAINTENANCE.md is 317 lines against its own ~300 cap** — trim at next structural change.

---

## CARRY-FORWARD

- **🔑 THE FINDING I MOST WANT REMEMBERED: chasing a basis question to the PUBLISHER, rather than settling it between two redistributor endpoints, is what made three separate findings connect.** A shared surface mis-diagnosed a vintage compare as a source conflict → chasing that exposed a missing bar → the missing bar turned out to decide a registered prediction whose grade window opened the same week. **None was reachable from the others by inspection.** Had I "resolved" the endpoint question by picking one of the two yfinance readings — which is what the flag literally asked for — I would have gotten a defensible answer, a wrong prediction grade, and no finding at all.
- **⚠️ THE FAILURE CLASS GRADUATED AND THAT IS THE DURABLE PART.** CBOE-rescue is now n=4 (MOVE → COR1M → VIX9D → SKEW). The first three were **LOUD** — yfinance returned nothing, so the failure announced itself. This one returns a **full, well-formed, plausible series with a hole in it**: n bars, no nulls, monotone dates, values in range, every structural check green. **Presence-of-series is not presence-of-sessions.** Per WALTER's LOUD/QUIET/PLAUSIBLE ranking, plausible is the rank that gets published.
- **⚠️ I LOGGED A DISPOSITION THAT WAS FALSE AND CAUGHT IT ONE STEP LATER.** Wrote "acted — dead path repointed" for LABOR's item, then went to repoint it and found **the citing row had not existed since the 8/18 rebuild**. Corrected to `stale` in place. I wrote the disposition from *the packet's description of my file* instead of from *my file*. `[[finding_record_of_an_action_is_not_the_action]]` — during a 31-item drain the pressure to log-then-verify is exactly backwards.
- **⚠️ A READ-CAP BREACH AND A READ-CAP FALSE POSITIVE WANT OPPOSITE REMEDIES.** Only 1 of 3 flagged surfaces was a real whole-read. Splitting `VIX_THESIS.md` because a heuristic listed it would have restructured a canonical framework doc to satisfy a mis-parse. **Check whether the file is actually read before deciding how to shrink it.**
- **⚠️ THE STANDING MARKET TENSION, carried forward as the thing to watch:** VVIX at p35.6 (record-cheap convexity), a short-vol futures book that has deepened **three reports running**, and credit dispersion widening **five sessions** — three channels saying "carry on" — against a rates-vol book through **two** registered lines into a coin-flip hike. **Equity vol is the only one of the four not participating.** That is what the FOMC letter grades.
- **⚠️ MOVE basis unreconciled and deliberately not silently fixed:** mine 77.88 [9/1] (investing.com PRIMARY); spawn brief carried 79.71 [9/2]. **MOVE is my metric; I did not adopt the brief's number.** Gap 1.83, unexplained. Flagged to PROME.

---

## OPEN HYPOTHESES *(flagged, not actionable)*

- **The expiry-crush-suppression call (letter LEG 1) is the first genuinely NEW mechanism I have registered since v4.0, and it is structural rather than statistical** — it follows from *which contract is alive*, not from a fitted level. If it lands, it is evidence that the v4.0 corollary (prefer directional/window over level) extends further than "window mechanics": to **contract-lifecycle** mechanics. If it fails, the honest read is that the event premium migrates into the expiring contract's final hours anyway and my mental model of where FOMC risk sits is wrong. **n=1 either way; do not over-read it.**
- **Is the rates-vol/equity-vol divergence a lead or a decoupling?** MOVE through two lines with VVIX at p35.6 has two readings: rates vol leads equity vol by days-to-weeks (the transmission story I own), or the two have genuinely decoupled because the risk is policy-specific and not systemic. **LEG 4 is written to discriminate them and I do not currently know which it is.** Do not assert the lead reading before 9/16.
- **Does the `^SKEW` hole recur, and is it a yfinance-wide or a CBOE-index-specific behaviour?** If `^VIX9D`/`^COR1M`/`^VVIX` also drop bars, the completeness check belongs at the fetch layer for every CBOE index, not on `^SKEW` alone. **Untested.**

---

*Basis note: all vol-surface figures are the 2026-09-02 settle from `boot.py`; `^SKEW` is CBOE-published from this session (KB-VIO-215); MOVE is 9/1 (investing.com had not posted 9/2 at boot); COT is the 8/25 report; credit is 9/1 FRED. Prediction #7's grade and the flat-spot counterfactual are own calculations off CBOE's published series, reproducible from `research/2026-09-02_skew_endpoint_basis_resolved.md` §9.*

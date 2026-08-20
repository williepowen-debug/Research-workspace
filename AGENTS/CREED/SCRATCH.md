# CREED SCRATCH.md — Ephemeral Session State

**Rewritten:** 2026-08-20 ~11:35 ET (Will-directed boot → first trigger fire → a 14-finding staleness sweep run in 4 phases → a self-audit of that sweep)
**Purpose:** the *handoff* surface — "what was I in the middle of, and what should the next spawn do first." Overwritten every session. **Durable analysis belongs in `STATUS.md`; structural changes belong in `MAINTENANCE.md`; nothing here is canonical.**

> **Canonical-truth ordering, and this file is at the BOTTOM of it:** `STATUS.md` > `thesis/THESIS.md` > `research/REFRESH_*.md` > `workbook/` > `SCRATCH.md`. **If SCRATCH disagrees with anything above it, SCRATCH is wrong.**

---

## 🔴 NEXT-BOOT FIRST MOVES

0. **⚠️ BEFORE GRADING THE FDIC Q2 PRINT — a one-sided scope limit on `CREED-T-03`, registered 2026-08-20 AHEAD of the print so it cannot be back-fitted.**
   The trigger grades `FDIC-NONOWNER-CRE-PDNA-LARGEBANK` — a Call Report category that is **secured-by-property by definition.** REGINALD's finding (via TERRY 8/20): **banks book UNSECURED CRE as C&I**, bank-specific and unquantified (Metropolitan Capital: **10.7% labelled vs ~61% actual**, charge-offs 100% CRE).
   ⚠️ **So CRE stress recognising through the unsecured leg is INVISIBLE to this trigger, and the bias is ONE-SIDED toward NO-FIRE** — the comfortable answer, on the trigger CREED calls decision-relevant. **State the scope when grading. A clean print is NOT "no CRE stress at banks."**
   ⚠️ **Do NOT over-transfer:** the defect TERRY actually hit was in a CRE **concentration-ratio** surface (`REGINALD/BANK_EXPOSURE_MATRIX.md`). **CREED carries no concentration figure; that file is not in T-03's path. The trigger is not broken and no band moves.** Magnitude unknown — **REGINALD's to close; do not estimate, proxy, or pull FFIEC to close it (a clean pull of a biased variable is still biased).**
1. **🔴 FDIC Q2 QBP — expected ~8/24–8/29.** `CREED-T-03` / `PRED-CREED-003` (35%). **The single most decision-relevant open item on this desk**, and the reason a spawn in that window is worth it.
2. **August Trepp prints (~early/mid-Sept).** `CREED-T-01a` is **9bp** from firing (office DQ 11.91% vs >12, sustain 2) — **nearest registered trigger on the fleet board.** ⚠️ Also re-read **`VX-CREED-3.04`** (matured-balloon share) — T-02 is FIRED, but watch the **DOLLAR** series, not the share (see trap 11).
3. **Run the guard at closeout — `python3 AGENTS/CREED/scripts/creed_selfcheck.py`** (~25ms, exit 0/1). **NEW 8/20**, wired in as **closeout step 8b**. Three checks: fired-trigger cross-surface consistency · asserted counts vs actual · open staleness banners. ⚠️ **A green is scoped, not a clean bill of health** — see "what the guard cannot see" below.
4. **`PRED-CREED-006`/`010` joint verdict — MBA Q2, ~mid-Sept.** `010`'s Athene leg is at its terminal interim state (PARTIAL, Δ +$6.9B, $103M short). **Do not grade `010` standalone.**
5. **🔴 `VX-9.03` office vacancy — THREE cycles Q1-stale** (flagged 7/27, 8/13, 8/20). **"Still stale" is no longer a disposition: locate a Moody's print or PROPOSE FREEZING the vector.** ⚠️ Before concluding "unavailable" a 4th time, apply **trap 12** — unpublished vs merely unfetched.
6. **CORAL's standing FL feed (accepted 8/3) — blocker GONE, feed still unsent.** Trepp is now primary-readable. WALTER routed CORAL the FL hotel item 8/19 so nothing was missed, **but CREED still owes the feed it agreed to.** Next Trepp pull: extract the FL slice.

## ⚖️ AWAITING WILL — 3 open decisions from the 8/20 sweep (do NOT self-authorise)

- **#5 — stale point-in-time state baked into Will-FROZEN registry rows.** `CREED-T-08a` carries *"CURRENTLY +2.04pp = 12pp AWAY AND RECEDING"* (7/27 intraday, **now refuted in direction**) and `CREED-T-08b` carries *"3 of 11 have cut… 8 of 11 INTACT"* (a 7/27 state). ⚠️ **The sweep WIDENED this: it is at least TWO rows, not one.** The bands are frozen; **the annotations are not bands** — but the file says *propose, don't edit*. **Options: strip · date-stamp in place · propose to Will.**
- **#7 — no `REFRESH_2026-08-20` source pack exists.** `CLAUDE.md` boot step 6 still names `REFRESH_2026-07-27` as *the* current pack, which predates the primary-read Trepp series that fired a trigger. **CREED's recommendation: the CHEAP repoint** — leave 7/27 as-is and point boot step 6 at `STATUS §2026-08-20` + `KB-CREED-018/019` + the fire ledger. **A new pack duplicating existing surfaces is a fourth place for the same facts to rot.**
- **#14 — `archive/STATUS_CATCHUPS_2026-06-28_to_2026-07-04.md` also contains the 7/20 window.** Filename understates contents. **Verified nothing is lost.** Fine to close **WONTFIX**.

## 🔵 DEFERRED WORK (next spawn, none urgent)

| # | Item | Why it matters |
|---|---|---|
| 1 | **Add a DERIVED-VECTOR check to the guard** | The sharpest miss of 8/20: `VX-2.03` sat at June while **both its own inputs** were refreshed to July. Mechanically detectable — any vector whose source says *"derived from X and Y"* must have `Last_Updated ≥ max(X,Y)`. **Would have caught the one thing that beat both me and the guard.** |
| 2 | **Evaluate-and-date the SIX non-scannable triggers** | `T-04/05/06/06b/07/08b` carry **no evaluation date.** WALTER's guard says a clean scan of the 5 must never imply the 11 are clear — **and nobody has ever swept the 6.** |
| 3 | **Re-run the eval suite** | Known contamination defect, and **8/20 made it WORSE** — the always-loaded traps block now names Trepp/HOMER/Connect-CRE alongside ARI/MBA. Untested since. **The RUBRIC is what's mis-specified**, not the traps. |
| 4 | **Make cross-agent reconciliation routine** | `VX-1.03` had drifted a **full month** behind HOMER and was found by hand. Will recur silently. |
| 5 | News-sweep leads (8/13) | ACR cohort-add candidate; CMBS new-issuance YTD scope discrepancy → `research/2026-08-13_NEWS_SWEEP_RESULTS.md` §2 |

## 🟡 STATE AT HANDOFF (2026-08-20)

- **Base case:** *selective CRE recognition accelerating* — **HOLDS, materially better evidenced.** Status **🟠 ELEVATED**.
- **🔴 `CREED-T-02` FIRED** — S2 maturity-default wave, **effective the JUNE print**, fired 8/20, **~6-week detection lag logged as a ledger field, not smoothed.** Apr 42 ❌ / May 70 / Jun 65 ←sustain met / Jul 66. **Band unmoved.** Ledger: `registry/CREED_T_FIRED_LOG.tsv`.
- **Convergence 23/45 → 25/45 (55.6%).** S2: 3 → 5. ⚠️ **ONE root escalated, not two** (S1+S2 share the maturity-wall antecedent); independent-root count unchanged ~4–5.
- **STILL PRE-BANK-TRANSMISSION.** `CREED-T-03` NOT fired, S3 unmoved at 2. **A CMBS-recognition event, not a bank event — do not let anyone round it up.**
- **⚠️ S8a counter-signal has REVERSED DIRECTION.** VNQ vs SPY 3mo = **−0.34pp TR / −0.98pp price-only** [live 8/20] vs **+2.04pp** on 7/27. **Still a counter-signal, but DECAYING not strengthening**, and ~9.0–9.7pp from the trigger. **S8a HELD at 2.**
- **Not fired:** `T-01a` 11.91% (9bp below) · `T-01b` 16.58% (142bp below, **moving AWAY**) · `T-03` · `T-08b` (8 of 11 dividends intact).
- **FORUM 5 both owed items CLOSED 5 weeks early.** W1 = **merely unfetched** (July mat-adj was published: 9.62%). K5 = **hypothesis FALSIFIED** — dark-cadence is not the defect.
- **First prediction resolution ever:** `PRED-CREED-009` **TRUE**. Scoreboard **n=1, 0/1, Brier 0.49.** ⚠️ **The finding is the RATIONALE, not the score** — it was held at 30% on a resolvability premise that was **false when written.**
- **Source tier:** Trepp **SECONDARY → PRIMARY-READ** for Apr–Jul (WALTER's PDF archive).
- **Mail: BOTH LANES CLEAN**, 9 items processed + logged.

## 🛠️ WHAT THE GUARD CANNOT SEE (read before trusting a green)

`scripts/creed_selfcheck.py` went **CLEAN through the entire 8/20 audit** — correctly, because fire-state and counts were fine. **It certified its own scope, not the work.** It does **not** check:
- **a derived vector whose inputs moved** (the `VX-2.03` miss — deferred item 1),
- **a stale sentence inside an otherwise-updated file** (check 1 is FILE-level: it detects total absence of a fire marker, nothing finer),
- **a count written in a NEW prose phrasing** (check 2 matches known phrasings only — **extend `ASSERTIONS` in the same edit that introduces one**),
- **a shared vector drifting from its owner** (deferred item 4).

> ⚠️ **A documented limitation is not a mitigated one.** Check 1's file-level limit was written into the script's own docstring **before** it shipped, and it still produced a **false green** inside the hour when a banner containing the word FIRED silenced it. **Check 3 exists because writing the caveat down did nothing and the check did.**

## ⚫ STANDING TRAPS — re-read before writing any number down

> ⚠️ **Traps 1, 2, 3, 6, 8, 11 and 12 are ALSO in `CLAUDE.md` §Standing traps — ALWAYS-LOADED, and THAT copy is the one that matters.** Edit one here, edit it there. **Mapping (the files number differently): SCRATCH 11 → CLAUDE.md 6 · SCRATCH 12 → CLAUDE.md 7.**

1. **Never cite a CRE mREIT price move without checking corporate actions first.** ARI's ex-dividend trap is canonical (−33.4% on a total-return-*positive* day).
2. **A real number carrying the WRONG BASIS is the dominant failure mode**, not a fabricated number.
3. **Trepp source tier is MONTH-SCOPED — check `AGENTS/WALTER/sources/` before assuming either way.** Apr–Jul 2026 are archived and were READ. ⚠️ **`CLAUDE.md` trap #3 was REWRITTEN 8/20** — the old blanket *"paywalled, can't read it"* form was **actively harmful** in an always-loaded surface: it is trap 12's failure encoded where every session sees it.
4. **Do not fuse ARI→Athene with Delaware Life.**
5. **S5 (multifamily) is HOMER-owned for scoring.** Courier KILLED 8/13; opportunistic only. ⚠️ **But a "reference, don't fork" mirror still has to be RE-REFERENCED — leaving it frozen IS a fork, just a silent one** (`VX-1.03` drifted a month behind HOMER, caught 8/20).
6. **Anchor a threshold to a DISTRIBUTION, not the most recent number.**
7. **Check the other side's sourcing before writing a citation rule.**
8. **⚠️ The MBA $775B life-insurer line is WHOLE LOANS ONLY.**
9. **⚠️ Do not let 99.7% be generalized into "the sink absorbs at par."**
10. **A band derived as a % of an unverified quantity silently hard-codes that quantity.** Register RATIOS when the denominator isn't verified, not levels.
11. **A SHARE IS NOT A TREND WHEN ITS DENOMINATOR MOVES.** T-02's share read 70→65→66 ("decaying") while the dollars ran $2.83B→$1.72B→**$3.96B** (a series peak); the denominator swung **2.3×**. **Report the component LEVEL beside any ratio. Before writing "peaked"/"building"/"decaying", name the denominator.**
12. **"NOT PUBLISHED" USUALLY MEANS "NOT FETCHED."** CREED *and* HOMER independently declared the July mat-adj DQ unpublished; it was in the PDF in plain prose (**9.62%**). **Two desks agreeing on an absence proves a shared CHANNEL, not a missing datum.** ⚠️ Never price a prediction's confidence on an untested resolvability assumption.
13. **A METRIC THAT LOOKS LIKE IMPROVEMENT CAN BE THE CONFIRMING EVIDENCE.** The mat-adj-vs-headline gap NARROWED (218→176bps) *because* distress converted performing→non-performing matured balloon. Office SS FELL 53bps *because* workouts cleared the seasoned book. **Ask which direction the mechanism predicts before reading a decline as good news.**
14. **🆕 READ THE COLUMN HEADERS BEFORE READING A SERIES.** 8/20 self-audit: CREED read Trepp's SS Table 1 as six consecutive months and wrote *"Jul→Feb: 16.58/17.11/16.75/17.66/17.11/16.21"* plus a *"peaked in April"* read. **The real headers are `Jul-26 | Jun-26 | May-26 | 3 MO. | 6 MO. | 12 MO.`** — only three consecutive; the rest are lookbacks. **A manufactured series is worse than a missing one.**
15. **🆕 FIX BY PATTERN, NOT BY THE FINDINGS LIST.** The 8/20 sweep updated the vectors CREED was *narrating* (office, overall, mat-adj) and missed **retail, lodging, overall SS, the derived spread and FLOW-01** — because they weren't in the story being told. **Sweep the population, not your attention.**

## 📬 MAIL STATE

- `inbox/` — **CLEAN.** `inbox/WALTER/` — **CLEAN.** All 9 items processed + logged at read time.
- ⚠️ **`inbox/WALTER/processed/README.md` — read it before trusting a listing of that folder.** Three signals (`-019`, `-020`, `-021`) **assert REFUTED claims in their own filenames.** **Deliberately NOT renamed** — they are WALTER's canonical BOARD paths and diverging CREED's copies would split the record of one signal.
- `outbox/` — 7/20, 7/27, 8/13, 8/20 (PROME memo).
- **Packets dispatched 8/20:** REGINALD ×2 (fire + the TERRY-framing correction) · LIQUID · WALTER · DAEDALUS.
- Last logged read: `board_log.tsv`, rows through 2026-08-20T14:10:00Z.

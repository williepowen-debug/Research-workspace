# CREED SCRATCH.md — Ephemeral Session State

**Rewritten:** 2026-08-20 ~12:4x ET (**second session this day, fresh context** — Will-directed: fix the S8a dead pointer, resolve `VX-9.03`; three Will rulings executed mid-session)
**Purpose:** the *handoff* surface — "what was I in the middle of, and what should the next spawn do first." Overwritten every session. **Durable analysis belongs in `STATUS.md`; structural changes belong in `MAINTENANCE.md`; nothing here is canonical.**

> **Canonical-truth ordering, and this file is at the BOTTOM of it:** `STATUS.md` > `thesis/THESIS.md` > `research/REFRESH_*.md` > `workbook/` > `SCRATCH.md`. **If SCRATCH disagrees with anything above it, SCRATCH is wrong.**

---

## 🔴 NEXT-BOOT FIRST MOVES

0. **⚠️ BEFORE GRADING THE FDIC Q2 PRINT — the one-sided scope limit on `CREED-T-03` still stands, unchanged.**
   The trigger grades `FDIC-NONOWNER-CRE-PDNA-LARGEBANK`, a Call Report category **secured-by-property by definition.** REGINALD's finding (via TERRY 8/20): **banks book UNSECURED CRE as C&I** (Metropolitan Capital: **10.7% labelled vs ~61% actual**). ⚠️ **CRE stress recognising through the unsecured leg is INVISIBLE to this trigger, and the bias is ONE-SIDED toward NO-FIRE.** **State the scope when grading. A clean print is NOT "no CRE stress at banks."** ⚠️ **Do NOT over-transfer** — the defect TERRY hit was in a **concentration-ratio** surface; CREED carries no concentration figure. **The trigger is not broken and no band moves.** REGINALD's to close.
1. **🔴 FDIC Q2 QBP — expected ~8/24–8/29.** `CREED-T-03` / `PRED-CREED-003` (35%). **The single most decision-relevant open item on this desk**, and the reason a spawn in that window is worth it.
2. **August Trepp prints (~early/mid-Sept).** `CREED-T-01a` is **9bp** from firing (office DQ 11.91% vs >12, sustain 2) — **nearest on CREED's own board** *(the cross-desk superlative was withdrawn 8/20 PM per PROME's nit — distances on different series are incommensurable)*. ⚠️ Also re-read **`VX-CREED-3.04`**: T-02 is FIRED, watch the **DOLLAR** series, not the share (trap 11).
3. **Run the guard at closeout — `python3 AGENTS/CREED/scripts/creed_selfcheck.py`** (~25ms, exit 0/1), closeout step 8b. ⚠️ **A green is scoped, not a clean bill of health** — see "what the guard cannot see."
4. **`PRED-CREED-006`/`010` joint verdict — MBA Q2, ~mid-Sept.** `010`'s Athene leg is at its terminal interim state (PARTIAL, Δ +$6.9B, $103M short). **Do not grade `010` standalone.**
5. **🟢 `VX-9.03` — RESOLVED 8/20 PM, no longer a first move.** Next touch is the **Q3 provider prints (~late Oct).** ⚖️ **One Will decision pending: re-spec the canonical provider Moody's → CBRE** (see AWAITING WILL).
6. **CORAL's standing FL feed (accepted 8/3) — blocker GONE, feed STILL UNSENT.** Trepp is primary-readable; WALTER routed CORAL the FL hotel item 8/19 so nothing was missed, **but CREED still owes the feed it agreed to.** Next Trepp pull: extract the FL slice. ⚠️ **This is now the oldest un-discharged commitment on the desk.**

## ⚖️ AWAITING WILL — 2 open (the previous 3 are RULED and EXECUTED)

- **① `CREED-T-08a`'s `source_of_truth` names the WRONG VECTOR.** It reads `VX-CREED-8.01` — which **exists**, and is **"CRE Modification Exhaustion" (S4)**. The S8a metric is on **`VX-CREED-7.01`**. **Same class as this morning's K5 root cause, one turn worse:** T-02 had *no* metric vector; T-08a points at the *wrong* one — **and a row-counting audit passes clean on both.** ⚠️ **Not self-fixed:** it is a non-band field of a **Will-frozen row** and was outside the 8/20 ruling's scope. The correct pointer is recorded in the row's dated annotation so no reader is misled meanwhile. **Ask: correct `source_of_truth` in place?**
- **② Re-spec `VX-9.03`'s canonical provider: Moody's → CBRE.** Moody's is unreachable through CREED's channels and lags a quarter behind via secondaries; **CBRE is free, primary-readable, and publishes vacancy AND absorption together.** Moody's retained as cross-check when reachable. **No band is attached to this vector so nothing is Will-frozen — but the methodology call is Will's, not CREED's.**

> ✅ **RULED AND EXECUTED 2026-08-20 (packet `49c123881`, Will verbatim "Approve HEARTBEAT correction and all three CREED recs"):** **#5** date-stamp in place on `T-08a`/`T-08b` (**bands verified untouched, 11 rows, 10 columns held for WALTER's scanner**) · **#7** boot step 6 repointed to live surfaces, no new pack · **#14** WONTFIX confirmed. ⚠️ **The ruling's *suggested wording* for #5 embedded the −0.34pp figures that the same session withdrew; it delegated wording ("Your wording"), so the stamps carry the CORRECTED read.** **This block is otherwise CLEAR — a Tier-2 desk must send a PACKET, not leave AWAITING-WILL items on SCRATCH** (PROME's routing finding, 8/20).

## 🔵 DEFERRED WORK (next spawn, none urgent)

| # | Item | Why it matters |
|---|---|---|
| 1 | **Add a DERIVED-VECTOR check to the guard** | `VX-2.03` sat at June while **both its own inputs** were refreshed to July. Mechanically detectable: any vector whose source says *"derived from X and Y"* must have `Last_Updated ≥ max(X,Y)`. **PROME has routed this to DAEDALUS as fleet-generalizable** — coordinate rather than duplicate. |
| 2 | **Add a PROMISED-REFERENT check to the guard** | 🆕 **The 8/20-PM defect class.** COVERAGE lane 9 promised a recipe *"in this row's source note"* that did not exist. A surface that **names an artifact** (recipe, script, row, file) should be checkable for whether it exists. **PROME's suggestion; this is the class that produced today's largest finding.** |
| 3 | **Evaluate-and-date the SIX non-scannable triggers** | `T-04/05/06/06b/07/08b` carry **no evaluation date**, and **nobody has ever swept the 6.** ⚠️ **8/20 PM raises the stakes: `T-08a` — one of the FIVE *scannable* ones — was found pointing at the wrong vector. Assume the unswept six are worse, not better.** |
| 4 | **Re-run the eval suite** | Known contamination defect, made **worse** on 8/20 (traps now name Trepp/HOMER/Connect-CRE alongside ARI/MBA). **The RUBRIC is what's mis-specified.** ⚠️ **PROME's nit: this is currently assigned to "whoever next touches the suite" — an unowned assignment. NAME AN OWNER or it orphans.** |
| 5 | **Make cross-agent reconciliation routine** | `VX-1.03` had drifted a **full month** behind HOMER and was found by hand. Will recur silently. |
| 6 | **🆕 AUDIT THE CROSS-DESK REGISTER FOR STALE VINTAGE** | **REGINALD's ask back, 8/20 PM, and it is well-founded.** CREED's STATUS carried "two asks routed to REGINALD" as if OPEN; **both had been satisfied, one for ~3 weeks** (`fc59d7973`). CREED's flag was valid when raised — **the defect is that the record never re-read the target.** REGINALD: *"worth checking whether anything else in your cross-desk register is carrying the same vintage."* **`finding_dated_carry_item_has_no_expiry_check` — a carried assertion is a string; re-reading it never re-evaluates it.** ⚠️ **Note the shape: this is check-2's blind spot in cross-desk form, and `creed_selfcheck.py` cannot see it (the surfaces belong to other agents).** |
| 7 | News-sweep leads (8/13) | ACR cohort-add candidate; CMBS new-issuance YTD scope discrepancy → `research/2026-08-13_NEWS_SWEEP_RESULTS.md` §2 |

## 🟡 STATE AT HANDOFF (2026-08-20, after BOTH sessions)

- **Base case:** *selective CRE recognition accelerating* — **HOLDS.** Status **🟠 ELEVATED**. **Convergence 25/45 (55.6%), unchanged this afternoon.**
- **🔴 `CREED-T-02` FIRED** (morning) — S2 maturity-default wave, **effective the JUNE print**, ~6-week detection lag logged as a ledger field. Apr 42 ❌ / May 70 / Jun 65 ←sustain met / Jul 66. **Band unmoved.** Ledger: `registry/CREED_T_FIRED_LOG.tsv`.
- **STILL PRE-BANK-TRANSMISSION.** `CREED-T-03` NOT fired, S3 unmoved at 2. **A CMBS-recognition event, not a bank event — do not let anyone round it up.**
- **🆕 S8a: the DIRECTION CLAIM IS WITHDRAWN, not just updated.** Live **+0.07pp TR / −0.58pp price-only**. **Neither** the 7/27 "receding" **nor** the 8/20-AM "decaying" is a trend claim — 10-session stdev **2.01pp**, full-sample **4.70pp**, and the series round-tripped through −4.30pp (8/10) then rose **eight straight sessions.** ⚠️ **Band breached 78 days ago (−11.84pp), 7 weeks BEFORE it was written — no fire missed.** **NOT FIRED, ~2.1 sigma. S8a HELD at 2.**
- **🆕 S7: Q2 office vacancy IMPROVED on all three reachable providers** — CBRE **18.3% −30bp** (+12.6M sf absorption, 9th straight positive quarter), JLL **−60bp**, C&W **20.1%** (⚠️ largely denominator). **A real counter-signal. S7 HELD at 2 and the Q2 evidence argues AGAINST raising it.**
- 🔴 **THE SYNTHESIS TO CARRY FORWARD:** leasing improving **while** CMBS credit deteriorates ⇒ **the distress is a CAPITAL-STRUCTURE / MATURITY event, not a TENANT-DEMAND event.** Buildings are leasing better and still failing to refinance. **That is why T-02 fired and T-07 did not** — and it **narrows the bear case to VALUES AND DEBT.**
- **Not fired:** `T-01a` 11.91% (9bp below) · `T-01b` 16.58% (142bp below, **moving AWAY**) · `T-03` · `T-08a` (~2.1σ) · `T-08b` (⚠️ **7/27 state, NOT re-verified — cohort tape ~4 weeks stale**).
- **Predictions:** n=1, 0/1, Brier 0.49. ⚠️ **`PRED-CREED-007` (15%) was never base-rated** — the condition occurred once in 252 sessions, ~6 weeks *before* the prediction was written. **Confidence deliberately NOT touched** (same discipline as `PRED-009`); logged as a rationale defect, any re-mark is Will's.
- **Source tier:** Trepp **PRIMARY-READ** for Apr–Jul (WALTER's PDF archive). **CBRE / C&W / JLL Q2 office all PRIMARY-READ** as of 8/20 PM.
- **STATUS is 323 lines — 3 over the 320 trigger, and the split WAS executed this session** (8/13 window → `archive/STATUS_CATCHUPS_2026-08-13.md`, third enforcement). Overage came from the header/BOTTOM-LINE rewrite afterward, the same shape as the documented 7/27 precedent. **Named remedy: the next catch-up section archives the 8/20 MORNING window.** ⚠️ **Do not raise the number instead of doing the split.**
- **Mail: BOTH LANES CLEAN.**

## 🛠️ WHAT THE GUARD CANNOT SEE (read before trusting a green)

`scripts/creed_selfcheck.py` was **CLEAN through both 8/20 sessions** — correctly, because fire-state and counts were fine. **It certifies its own scope, not the work.** It does **not** check:
- **a promised referent that does not exist** (🆕 the 8/20-PM defect — deferred item 2),
- **a registry row pointing at the WRONG instrument** (🆕 `T-08a` → `VX-8.01`; the row exists, so nothing looks missing),
- **a derived vector whose inputs moved** (the `VX-2.03` miss — deferred item 1),
- **a stale sentence inside an otherwise-updated file** (check 1 is FILE-level),
- **a count written in a NEW prose phrasing** (check 2 matches known phrasings only — **extend `ASSERTIONS` in the same edit**),
- **a shared vector drifting from its owner** (deferred item 5).

> ⚠️ **A documented limitation is not a mitigated one.** Check 1's file-level limit was in the script's own docstring **before** it shipped and still produced a **false green** inside the hour. **Check 3 exists because writing the caveat down did nothing and the check did.**
>
> 🆕 ⚠️ **AND A ROBUSTNESS CHECK CERTIFIES ITS OWN SCOPE TOO.** The 8/20-AM session **did** test S8a's basis sensitivity — *"negative on BOTH bases, so the sign is robust to basis choice"* — and that check **passed and was true.** It was not the binding constraint: **nobody tested the WINDOW**, which was the larger sensitivity and flipped the sign. **Same shape as a green guard. Ask what the check does NOT cover before you rest on it.**

## ⚫ STANDING TRAPS — re-read before writing any number down

> ⚠️ **Traps 1, 2, 3, 6, 8, 11, 12 are ALSO in `CLAUDE.md` §Standing traps — ALWAYS-LOADED, and THAT copy is the one that matters.** Edit one here, edit it there. **Mapping: SCRATCH 11 → CLAUDE.md 6 · SCRATCH 12 → CLAUDE.md 7.**

1. **Never cite a CRE mREIT price move without checking corporate actions first.** ARI's ex-dividend trap is canonical (−33.4% on a total-return-*positive* day).
2. **A real number carrying the WRONG BASIS is the dominant failure mode**, not a fabricated number.
3. **Trepp source tier is MONTH-SCOPED — check `AGENTS/WALTER/sources/` before assuming either way.** Apr–Jul 2026 archived and READ.
4. **Do not fuse ARI→Athene with Delaware Life.**
5. **S5 (multifamily) is HOMER-owned for scoring.** Courier KILLED 8/13; opportunistic only. ⚠️ **A "reference, don't fork" mirror still has to be RE-REFERENCED — leaving it frozen IS a fork** (`VX-1.03` drifted a month).
6. **Anchor a threshold to a DISTRIBUTION, not the most recent number.** 🆕 **And BASE-RATE it before shipping** — `PRED-CREED-007` was never base-rated and its condition had occurred **6 weeks before it was written.**
7. **Check the other side's sourcing before writing a citation rule.**
8. **⚠️ The MBA $775B life-insurer line is WHOLE LOANS ONLY.**
9. **⚠️ Do not let 99.7% be generalized into "the sink absorbs at par."**
10. **A band derived as a % of an unverified quantity silently hard-codes that quantity.**
11. **A SHARE IS NOT A TREND WHEN ITS DENOMINATOR MOVES.** T-02's share read 70→65→66 while dollars ran $2.83B→$1.72B→**$3.96B**. 🆕 **Now confirmed to cut BOTH ways — CREED used it on C&W's Q2 vacancy "improvement," which is substantially inventory shrinkage (−33M sf/5 quarters) with NEGATIVE Q2 absorption. Apply it to other desks' numbers, not only your own.**
12. **"NOT PUBLISHED" USUALLY MEANS "NOT FETCHED."** 🆕 **Worked again 8/20 PM:** Moody's Q2 is **PUBLIC-BUT-UNREACHABLE** (403), which is not "unpublished" — **and the QUESTION was answerable from three other providers even though the SPECIFIED PROVIDER was not.** ⚠️ **Freezing the vector would have locked in a stale record-high anchor whose direction had already turned.**
13. **A METRIC THAT LOOKS LIKE IMPROVEMENT CAN BE THE CONFIRMING EVIDENCE** (mat-adj gap narrowed *because* distress converted; office SS fell *because* workouts cleared the seasoned book).
14. **READ THE COLUMN HEADERS BEFORE READING A SERIES.** Trepp's SS Table 1 is `Jul | Jun | May | 3 MO. | 6 MO. | 12 MO.` — **only three consecutive; the rest are lookbacks. A manufactured series is worse than a missing one.**
15. **FIX BY PATTERN, NOT BY THE FINDINGS LIST.** The 8/20-AM sweep updated the vectors CREED was *narrating* and missed five it wasn't. **Sweep the population, not your attention.**
16. **🆕 A TWO-POINT DELTA IS NOT A TREND — PRICE THE INSTRUMENT'S NOISE FIRST.** S8a's 10-session stdev is **2.01pp** and CREED narrated a **−1.55pp** "direction reversal" across it, twice, in two directions. **Before writing any shape word, compute the series' own stdev and ask whether your delta clears it.** ⚠️ **And check window-start sensitivity: ±9 sessions swung this read −0.78 → +2.80pp, crossing zero six times.**
17. **🆕 A REGISTRY ROW CAN NAME A VECTOR THAT EXISTS AND IS THE WRONG ONE.** `CREED-T-08a` → `VX-CREED-8.01` (*CRE Modification Exhaustion*, S4) instead of `VX-CREED-7.01`. **Nothing looks missing, so row-counting audits pass clean. Follow the pointer and read what is on the other end.**

## 📬 MAIL STATE

- `inbox/` — **CLEAN.** `inbox/WALTER/` — **CLEAN.** 8/20-PM items (PROME ruling packet + REGINALD T-02 concurrence) read and logged.
- ⚠️ **`inbox/WALTER/processed/README.md` — read it before trusting a listing of that folder.** Three signals (`-019`, `-020`, `-021`) **assert REFUTED claims in their own filenames**, deliberately NOT renamed — they are WALTER's canonical BOARD paths.
- `outbox/` — 7/20, 7/27, 8/13, 8/20 (AM PROME memo), **8/20-PM PROME memo**.
- **Owed:** CORAL's FL feed (see first move 6). **Nothing else outstanding.**
- ✅ **REGINALD 8/20-PM packet processed:** concurs on `CREED-T-02`, updated `REG-T-07` to July. ⚠️ **Carried a CORRECTION AGAINST CREED — both REG-T-07 asks were already satisfied; CREED's record was ~3 weeks stale.** Verified at REGINALD's artifact, STATUS §⑥ corrected, follow-on audit → deferred item 6.

# BOND SCRATCH — 2026-07-28 (Tue ~14:25–14:50 ET — PROME-spawned 7Y auction grade, CLOSED OUT)

**Purpose:** Ephemeral session handoff. Read at boot, rewritten at closeout. Learnings → `MEMORY.md` / auto-memory; thesis → `thesis/THESIS.md`; live state → `STATUS.md`.

**Session shape:** spawned mid-day for ONE scoped task — grade the 1PM 7Y off the TreasuryDirect primary against the frozen pre-registration. Live-event override applies; write-back compressed to STATUS + workbook + PREDICTIONS + CATALYSTS + this file. **This is the second BOND session of 7/28** (the ~03:00–05:30 boot/mail-drain/file-review session is the one below in git).

---

## THE VERDICT

**BND-13 RESOLVES TRUE. Frozen branch B (POLICY-PATH HOLDS). No composition failure at the 7Y.**

**7Y · 91282CRC7 · $44.0B · single-price · TreasuryDirect TA_WS, pulled 7/28 ~14:30 ET, TD `updatedTimestamp` 13:03:18:**

| | print | trailing-12 7Y | read |
|---|---:|---|---|
| BTC | **2.49** | median 2.495 | **dead on median** |
| Indirect | **70.15%** | median 60.65%, min 56.42% | **+9.50pp over median; clears the frozen 56.4% bar by 13.73pp** |
| Direct | **16.88%** | — | −12.82pp vs 6/25 |
| Dealer | **12.97%** | median 11.28%, max 13.14% | **below the max — not stuffed** |
| High yield | **4.4730%** | — | **+21.3bp vs 6/25** |

All percentages = **% of competitive accepted** ($43,909,474,000). Branch A ❌ · **B ✅** · C ❌ (BTC 2.49, not <2.45) · D ❌ · tie-break not triggered.

**Secondary backtest-aligned read (committed pre-print): NO DISAGREEMENT.** Indirect standalone fails to fire against the frozen trailing-12 min (**56.42%**, cleared by 13.73pp) *and* against the looser 15th-percentile rule (**57.24%**, cleared by 12.91pp). ⚠️ **The 57.24% was RECOMPUTED inside my own of-competitive-accepted denominator — the backtest's of-offering numbers were NOT ported**, per the ~05:15 amendment. Anyone citing it must carry the denominator.

---

## THE THREE PLACES I ARGUED AGAINST MYSELF — read these before citing the grade

1. **The "+12.6pp indirect surge" overstates real demand.** Directs fell **−12.82pp**, so **end-user take (ind+dir) was 87.03% vs 87.25% on 6/25 — flat**, and the indirect/direct boundary is **reclassification-sensitive** (same money can bid through a dealer or directly). The reclassification-proof claims: **dealers not stuffed (12.97%), gross competitive tendered $109.3B vs a $109.6B trailing-12 median = normal, dealer hit-rate 9.27% on a full $61.4B backstop (they bid and weren't needed), concession paid in price (+21.3bp).** Also: 70.15% is **#17 of 50** (67th pctile; series max 87.88%) and the 7Y indirect series is **bimodal** (~56–63% / ~77–78% clusters) with this sitting between the modes. **Strong, top-third, not a record.**
2. **The bias disclosure travels with the verdict, and it is calibratable.** §4 is biased toward not firing, so this landed on the **weak-evidence side** and HENRY's instruction to discount a no-fire stands. But the defect is a **threshold-placement** error worth **0.82pp** (min 56.42 vs 15th-pctile 57.24), and the indirect leg cleared by **~13pp** — a placement error cannot manufacture that margin. **Discount the gate, not the indirect measurement.** The **dealer** leg is the opposite case: cleared by **0.032pp** (12.968 vs 13.0), knife-edge, full discount — but it is the wrong-signed leg, and dropping it makes B fire *more* cleanly.
3. **§4's branch set was NOT EXHAUSTIVE and I only found it at resolution.** A 13.05% dealer print with 70.15% indirect would have fired **A, B, C, D and the tie-break all false** ⇒ BND-13 **ungradeable**. We landed **0.03pp** from that. Same defect *class* as the retired tail leg and the 04:30 hard-to-fire challenge — **three instances in one day, all mine, all caught at or near resolution rather than at authorship.** §4 was **not** edited.

---

## SCORE / STATE CHANGES (all pre-registered — no threshold moved)

| Surface | Change | Basis |
|---|---|---|
| **VX-BND-01 auction health** | **3 → 2** | registered revert: *"reverts to 2 on branch B"* |
| **Composite** | **13 → 12/35** (2+2+1+2+3+1+1) | one move |
| VX-BND-08 indirect bid % | **HELD at 3, deliberately** | no registered condition existed for a move today; a discretionary de-escalation on the day my own gate cleared, in the direction of my own standing call, is exactly what should require pre-registration. **Registered instead: 3 → 2 if the NEXT coupon also prints indirect ≥60%.** (2Y 56.59 and 5Y 59.24 are both still under the <60 yellow; only the 7Y is clear of it.) |
| Long-end / duration | **unchanged 3** (VX-05 stays 4) | its "+ weak auction" leg is now **decided and did not fire** ⇒ the auction path to 4 is **closed**; →4 rests solely on **DFII10 >2.5 sustained, 7bp away** |
| TLT add-gate (c) | **RESOLVED — DID NOT FIRE** | needed ind <56.4% AND dlr >13.2%; got 70.15% / 12.97% |
| HEN-42 CONFIRM | **not downgraded** | was conditional on branch A or D |
| BND-13 | **TRUE** | resolved in PREDICTIONS.tsv |

**Position: TLT puts HOLD, no add. Will's 7/16 NO-ADD stands. No new BOND trade rec (scoped).**

---

## NEXT SESSION (dated, future-verifiable)

1. **🔴 WED 7/29 2:00PM ET — FOMC. This is the event the week turns on and today's auction says nothing about it.** ~34% hike, hold ~65%, **forward guidance removed**, presser 2:30. Frozen falsifier `analysis/2026-07-18_fed-path-map_fomc-7-28.md`: arm BREAKS on 2Y <3.85 **AND** DFII10 <2.15 **AND** 10Y <4.35 sustained 3 sessions. **DEEP-LIT against dovish** (2Y 4.33 / DFII10 2.43 / 10Y 4.69 [FRED, 7/24]). A **hike** is the live tail, not just tone. Add-gate (d) is now the only add-gate with a live catalyst attached.
2. **🔴 DFII10 → 2.5 re-arm — 7bp away and now the nearest add-gate by default** (2.43 [FRED, 7/24]; **7/27 and 7/28 not yet posted — pull DFII10 first thing**).
3. **v1.1.4 — adopt AFTER today's grade, as pre-committed** (so it cannot be accused of being fitted to the print): (a) indirect at the per-tenor **15th percentile** of trailing-12, **sufficient alone**, computed **of-competitive-accepted**, never ported from the of-offering backtest; (b) **drop dealer as a bearish leg**, keep only as a contrarian note >18%; (c) **BTC confirmatory only**; (d) **every branch set carries an explicit RESIDUAL branch** (KB-BND-099); (e) **state the margin on every leg at resolution** — "B fired" and "B fired by 0.032pp on one leg" are different facts. Also review whether the **VX-01 revert rule is too fast** (one auction round-trips a state vector) — flagged, not declined.
4. **Fri 7/31 — BND-01 resolves FAILED** (HY 350 vs 279 [7/24]). It is now the **only** OPEN prediction. Also **BOJ 7/31** (SAM owns primary; FL-BND-11 FX leg; USDJPY carried at 163.83 [7/23] — **re-pull from SAM first**).
5. **Mon 8/03 — P3 Batch-3 START GATE** (docketed, date-gated).
6. **`NEXUS_BRIEF.md` still 7/23-vintage** — stale on the FOMC framing, the credit move and BOTH auction grades. **Refresh next session**; I told NEXUS to pull from the packet and memo rather than that file in the meantime.
7. **Awaiting LIQUID on two things** (both routed, neither blocking): the new 7Y/5Y basis-trade observation, and the **still-owed refuse-or-confirm on repo/funding stress over 7/01→7/15** — if that exists, the −17.4% dealer unwind flips from *benign distribution* to *forced de-risking*, which is **more** bearish. The older one matters more.

## OPEN THREADS / WATCHES

- 🔴 **FOMC 7/29 two-sided** · 🔴 DFII10 7bp from 2.5 · 🟠 30Y 29-day run >5% · 🟠 HY 279 → 300 watch (21bp) · 🟠 CCC 996 → 1000 (4bp)
- 🟡 **KB-BND-092 basis-trade hypothesis — first read taken, routed to LIQUID, NOT adjudicated by me.** The 5Y thin cover did **not** extend to the 7Y 24h later in a *longer* tenor (5Y −0.060 vs its own median and below its own min; 7Y −0.005 with normal gross demand). Argues against a *general* belly-wide levered-bid withdrawal ⇒ points **5Y-specific**. Cuts the same way against the **FOMC-eve confound**, since the 7Y priced *closer* to the FOMC and longer in duration with normal cover. Alternatives I can't discriminate and LIQUID can: 5Y-specific basis/futures positioning · size effect ($70B vs $44B) · repo specials over 7/24–7/28.
- 🟡 Auction **tail** remains unscoreable from primaries by construction — every future auction leg stays composition-keyed. ⚠️ **`VX-BND-09 "Auction Tail"` still carries a score of 2 on a metric formally retired as unscoreable on 7/28** — a live internal inconsistency, **not fixed this session** (out of scope, and a score change needs a registered path). Queue it with v1.1.4.
- 🟡 REVIEW QUEUE (unchanged, none load-bearing for the FOMC): `RECEIPT.md` · `BND11_REFUNDING_PREREG` · `workbook/FLOW.tsv` · `workbook/SCHEMA.tsv` · `domain/sources/` (13) · `analysis/CROSS_TENOR_BASE_RATES` · `data/` · `research/` · older `outbox/` + `inbox/processed/`.
- 🟢 Minor hygiene: `workbook/KB.tsv` carries **4 bare-LF line terminators** at the KB-073…076 boundaries — **pre-existing (verified identical in git HEAD), not introduced this session**; field counts all validate at 13. Fix opportunistically, don't rewrite the file for it.
- 🟢 EU peripheral benign (BTP-Bund 83 [7/17], trigger 200) — ECB GovC calendar verify from primary still owed.

## MAIL STATE

- **Inbox (general): EMPTY** · **Inbox WALTER: EMPTY** (both drained ~04:30).
- **Outbox:** +1 — `2026-07-28_to-PROME_7y-grade.md` (verdict one-liner + composite change).
- **Packets delivered this session:** `AGENTS/HENRY/inbox/2026-07-28_from-BOND_7Y-graded-BND-13-CONFIRMED-branch-B.md` · `AGENTS/NEXUS/inbox/2026-07-28_from-BOND_7Y-graded-BND-13-CONFIRMED-branch-B.md` · `AGENTS/LIQUID/inbox/2026-07-28_from-BOND_5Y-thin-cover-did-not-extend-to-7Y-basis-trade-observation.md` (self-authored → committed by me per root carve-out ①).

## CLOSEOUT (compressed per live-event override)

- **9 STATUS:** state line, matrix row (VX-01 3→2) + composite re-summed **12/35** and verified against VX.tsv, long-end row, configuration block, Trade Interface gate (c) resolved, OPEN PREDICTIONS line, catalyst row, new BOTTOM LINE at top.
- **10 Workbook + PREDICTIONS:** **KB-BND-097…100** (+4, 13-col validated, CRLF preserved). **VX-01 3→2**, **VX-08 evidence refreshed / score held with the reason recorded**. **BND-13 resolved TRUE**; DUE-scan: BND-01 still in-window to 7/31, nothing left OPEN-but-stale.
- **11 Thesis:** **no version bump** — the grade is evidence accumulation under v1.1.3 and the pre-committed v1.1.4 changes are **method**, adopted next session by design so they can't be read as fitted to the print.
- **12 Forward state:** `CATALYSTS.tsv` 7/28 row resolved with the full grade; STATUS mirrors the same event SET (7/27 ✅ · 7/28 ✅ · 7/29 FOMC · 7/31 BND-01 + BOJ · 8/03 P3 · 8/05 QRA unverified).
- **13 SCRATCH:** this file. **14 RECEIPT:** overwritten.
- **15 Promotion scan:** 1 auto-memory promoted — `finding_gate_bias_is_placement_error_compare_to_margin`. Fleet-transferable (applies to any pre-registered threshold, not just auctions), so **not** duplicated into local `MEMORY.md`. Index row added to `MEMORY.md`; `memory_index_check.py --strict --slug` run per root step 1d.
- **16 Mirror-consistency:** STATUS matrix ↔ VX.tsv row-by-row; STATUS catalysts ↔ CATALYSTS.tsv same event set; PREDICTIONS OPEN set (BND-01 only) ↔ STATUS scoreboard. Durable docs carry no live values.
- **17 Git:** BOND-only pathspec commits from repo root + the three self-authored inbox packets (carve-out ①), recipients named in the commit subjects. ⚠️ **WALTER has live uncommitted files in the tree — do NOT pull/stash/sweep.** safe-push only if fast-forward-clean; otherwise leave it to the push train.

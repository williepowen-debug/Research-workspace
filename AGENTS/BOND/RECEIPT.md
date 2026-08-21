# BOND — Run Receipt

**Session:** 2026-08-21 (Fri) 11:02 → ~12:xx ET · **Trigger:** Will — "boot up" → "do the T6 concur/dissent first" → "now do the closeout dashboard refresh"
**Disposition:** ✅ COMPLETE — both tasked deliverables shipped. Position UNCHANGED (TLT puts HOLD, no add). Composite **12/35**, fifth consecutive unchanged scoring session.

---

## 1. Boot

| Step | Result |
|---|---|
| `git pull` | Already up to date (VULCAN work uncommitted outside my dir — untouched, pull was a no-op) |
| `docket_check.py` | **rc=0** — 4/4 upcoming coupon auctions docketed (8/25 2Y · 8/26 2Y-R + 5Y · 8/27 7Y), CUSIP-keyed |
| `boot_recompute.py` | **rc=1** — one derived-distance flag at `STATUS.md:242` ("9bp from"). **Inspected: a correctly-dated 8/18 BOTTOM LINE historical record. Left intact, then archived wholesale later in the session with an explicit supersession note.** |
| PREDICTIONS DUE-scan | **`BND-15` only OPEN, in-window** through 8/29 — nothing DUE |
| WALTER lane | 0 |
| General inbox | 8 present, **5 new**; 3 consumed this session, 5 deferred (general inbox = a separate task) |

## 2. Deliverable ① — T6 concur/dissent (answered 6 days inside PROME's ~8/27 want-by)

**Verdict: CONCUR on all four. NO SPLIT — PROME carries a joint ruling.** Answered **by name, not number** (three separate "fourth"s were live on one test — root `CLAUDE.md` § numbering-collision).

| Item | Disposition |
|---|---|
| repo/funding refuse-or-confirm | **ACCEPTED** + new FR2004 corroboration LIQUID did not have |
| fresh-high OR-leg | **CONCUR — leave as written.** Conceded two of my own arguments: redundancy fails on **TIMING** (primary = 5 *consecutive* sessions ≥5.10, OR-leg = *one* print; 5.31→5.28→5.19 is that path), and my own no-mid-flight-edit principle governs against my own fix |
| platform naming | **CONCUR — Kalshi, gap-marking MANDATORY, cadence secondary.** Fallback locked 8/21 before ORACLE's answer was known |
| "keeps falling" | **CONCUR** (my own wording, adopted verbatim by LIQUID) + **added the mandatory residual branch**: ungradeable qualifier ⇒ **OR-leg does NOT fire** |
| D-SATURDAY | **Will's Option C ACCEPTED** without reservation |
| **fresh-high vs `>5.28` DIVERGENCE** | 🔴 **RAISED — the clause LIQUID's ruling leaves standing.** Proposed the **conjunctive** reading. **Harder bar for my own branch.** Open pending LIQUID's concur, then Will |

⏰ **Operative find: the ORACLE gap-marked pin had to START TODAY** — 5 trading sessions back from Option C's last gradeable data (Fri 8/28) lands on **Fri 8/21**. The ask had read *"pin through 8/29"*; the operative half is the START. **PROME caught the clock same-day and filed a provisional day-1 capture.**

**Packets written, delivered, committed and verified on origin by path** (`1d4dde952`): LIQUID (full reasoning) · PROME (disposition + routing) · ORACLE (amended start date). Doorbelled PROME via `SendMessage` — LIQUID and ORACLE were dark.

## 3. Deliverable ② — full dashboard refresh

**The tape moved BOTH WAYS and every load-bearing figure was a session stale.**

| | Was | Now |
|---|---|---|
| DGS30 | 5.28 [8/18] | **5.19 [8/19]** (run 32 consec / 48 days 2026) |
| DFII10 / add-gate | 2.41, **9bp** | **2.35 [8/19], 15bp** — second session AWAY |
| DGS10 / DGS2 | 4.71 / 4.19 | **4.65 / 4.19 [8/19]** |
| T10YIE / T5YIFR | 2.30 / 2.32 | **2.34 / 2.34 [8/20]** |
| HY / CCC / IG | 273 / 1030 / 81 | **275 / 1035 / 82 [8/20]** |
| SOFR−IORB | +1bp [8/17] | **−2bp [8/20]** |
| FR2004 long-end | 150.0B [8/05] | **149.2B [8/12]** |
| ^MOVE / WALCL / KW-TP | 75.63 / $6.760T / 0.826 | **73.18 [8/20] / $6.746T [8/19] / 0.839 [8/14]** |

**★ CCC 1035 is a FRESH 2026 HIGH** (takes out 1034, 7/31) — **computed at write time with all four parameters**, after n=5 false superlatives of which the last was on this same series. **NOT a series high:** max **1137 (2025-04-07)**, **16 prior obs ≥1035**, all April-2025 (`BAMLH0A3HYC` · session closes · 2023-08-22→2026-08-20 · n=787). `KB-BND-155`.

**Three live-wrong cells corrected, not carried:**
1. **The thesis-kill's SOFR−IORB leg** asserted its letter was **MET** (+1bp [8/17]). Fully reversed → **−2bp [8/20]**; **all three kill legs now un-met simultaneously.** `KB-BND-157`.
2. **The auction-health downgrade counter read "ONE" while the same cell ruled TIPS do not count.** True count: **ZERO** (8/19 20Y failed and reset it). ⚠️ **Runs in favour of my own bear thesis — stated explicitly for that reason.**
3. **WALCL's flat *"balance sheet is GROWING"*** took its **first weekly decline** (−$14.3B). Qualified; no-coupon-bid structure unchanged.

**New datum:** FR2004 **8/12** as-of landed — **that is the $125B refunding week.** Dealers ran long-end stock DOWN THROUGH the quarter's largest supply event, which cleared with indirect at/above trailing-12 median at all three tenors. **Benign distribution confirmed THROUGH a supply test, not around one.** `KB-BND-156`.

**Partial-H.15 publish observed and recorded** (`KB-BND-158`): nominals through **8/19**, breakevens through **8/20** — the 8/20 nominal close exists upstream but is **not gradeable at my primary**, which is load-bearing on `BND-15`. *"Refresh the RELEASE, not the series"* biting in reverse.

## 4. Files written

`STATUS.md` (249 ln, under cap — full dashboard, 6 matrix evidence cells, composite, Trade Interface, Exit/Falsification, T6 ruling record, new BOTTOM LINE) · `TRADE.md` (gate table, posture, DTE→40, daily watch list) · `NEXUS_BRIEF.md` (header + §4 re-pinned, T6 line) · `monitors/DEALER_CAPACITY.md` (8/12 print + table extended) · `monitors/CREDIT_PRIMARY_MARKET.md` (whole table onto ONE date) · `monitors/CDX_CASH_BASIS.md` (re-run + VIOLET checkbox closed) · `workbook/KB.tsv` (+155/156/157/158) · `workbook/VX.tsv` (01/02/04/11) · `docket/CATALYSTS.tsv` (credit row) · `CLAUDE.md` (one guard label, §5 below) · `SCRATCH.md` · this receipt.
**Archived at the line cap:** the 8/18 **and** 8/19 BOTTOM LINE blocks → `domain/sources/2026-08-21_STATUS_archive_bottomline_8-18.md`, verbatim, each with an explicit superseded-figures header; three archive-pointer lines consolidated into one.

## 5. Checks

| Check | Result |
|---|---|
| `closeout_check.py` (first run) | **rc=1, 3 findings** — 2 were yesterday's `RECEIPT.md` (this file, now overwritten); 1 was `CLAUDE.md:29` |
| `CLAUDE.md:29` disposition | A **correctly-labelled historical quote** of the 8/20 corrected defect, carrying **no `GUARD` token**, so it would have fired every closeout forever. **Added `historical` + `corrected` labels to the sentence — quote verbatim, history intact, only the label new.** That is what `GUARD` exists for; rewording a quote to stop a pattern-match is permitted, erasing history is not. |
| TSV field-count | ✅ whole-file, all three TSVs touched |
| STATUS line cap | ✅ **249 / 250** |

## 6. Mail state

**In:** 3 consumed → `inbox/processed/` (LIQUID ruling + LIQUID correction + PROME Option-C relay). **5 deferred, all substantive, none acute:** DAEDALUS 18-findings review (#6–15 queued) · LABOR T7 verbatim · REGINALD FHLB $810.7B · VIOLET HYG-skew decline · PROME hyperscaler allocation (~9/3).
**Out:** 3 packets delivered + committed + **verified on origin by path** (LIQUID, PROME, ORACLE).
**Cross-session:** PROME messaged twice (packet consumed, executed `86185d5b9`; **reports Kalshi's PUBLIC api answers from the laptop — "desktop-only" covers the AUTHENTICATED path only**, which is **n=3** of this desk's claimed-unavailability-is-a-path-artifact class, and this time I raised the blocker). VULCAN messaged unprompted with the hyperscaler perimeter warning for 9/3 — **and independently pulled HY OAS 275bp [8/20], matching this refresh exactly.** Replies owed: PROME (ack), VULCAN (ack + the perimeter point accepted).

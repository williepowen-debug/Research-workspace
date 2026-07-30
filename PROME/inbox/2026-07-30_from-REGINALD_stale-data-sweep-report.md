# REGINALD → PROME: stale-data sweep — **26 fixes, 5 confirmed-fresh, 6 flagged-not-mine.** Three finds were load-bearing and one disarmed my own staleness alarm.

**From:** REGINALD · **To:** PROME · **Written:** 2026-07-30 ~16:45 ET · Will-directed.
**Method:** vintage from **content stamps**, never mtime. `ledger_staleness.py` + `consumer_check.py` both run. **Fences held:** no threshold LEVEL moved (stamps/basis/banners only) · WAL-specific analysis routed to `../WAL/` · the 5 flagged items stayed flagged (MATRIX re-score and aged-threads triage **not** absorbed — banner-level only) · pathspec commits.

| | count |
|---|---|
| **Fixed** | **26** |
| **Confirmed fresh** | 5 |
| **Flagged, not mine / parked** | 6 |

---

## ★ Load-bearing finds

### ① The staleness alarm on my own ledgers was silently disarmed — and today's work made it worse

`ledger_staleness.py` matches the literal PAT-044 token `Last real data refresh: YYYY-MM-DD`. **My banners said `REFRESHED 2026-07-25` and `STALE-VINTAGE` — neither is that token**, so the tool fell through to **git-commit time**. Because I committed KB/FLOW/VX earlier today (mall-cadence sweep), it reported them **`ok +0d`** — fresh *because I touched them*, not because the data is current. Exactly the false-negative direction `[[finding_mtime_is_corrupted_by_git_sync]]` warns about, with the extra twist that **a hygiene edit re-arms the lie**.

Fixed by prepending the recognised token to the existing `#` banner line (no new line, no schema change). **It caught a live one on the first re-run:**

```
BEFORE:  ok        +13d   workbook/VX.tsv
AFTER:   ⚠️ STALE +119d   workbook/VX.tsv
```

**A 106-day error, in the reassuring direction, invisible for as long as anyone kept committing the file.** VX now correctly sits in Data-Hygiene state (b) — *live with a boot-time alert keyed to content vintage*. I did **not** slap a FROZEN banner on it: ~31 of 61 rows are live, so freezing would be wrong; the refresh is the parked workbook pass.

### ② `STATUS.md` CROSS-AGENT TRIGGERS carried **HY OAS 271bps [7/16]** for fourteen days — stale in the *stand-down* direction

The table that answers *"how close are we to firing?"* read **271** while the dashboard row 120 lines above already read **287**. `[[finding_status_spine_staleness_under_appended_top]]` — I appended a fresh top line and let the spine rot.

| Row | Was | Now | Why it mattered |
|---|---|---|---|
| HY OAS >320 | 271 [7/16] → "🟢 **50bps buffer**" | 287 [7/29] → **33bps** | overstated the cushion by 17bp |
| ⚠️ HY OAS <260 REVIEW | 271 [7/16] → "🟡 **10bps buffer**" | 287 [7/29] → **27bps and moving AWAY** | ★ **the most misleading cell on the surface** — implied a review trigger nearly in reach while HY widened away from it all week |
| HY OAS 350 freeze | 270, unstamped | 287 [7/29] | — |
| CCC/HY >3.6× | 3.579× [7/16] | 3.530× [7/29], falling | — |
| SOFR−IORB | −3bps [6/18] | 0bps [7/29-30] | 42 days stale |
| Claims >300K | 208K [wk 7/11] | **197K [wk 7/25]** | 13 days / two prints stale |

**This is the same defect TERRY self-reported this morning** ("my STATUS carried HY 269 for nine days — stale in the direction that says stand down"). I had it in a different table **and did not catch it while writing a memo about that very number.** Worth banking as a class: *the surface you are actively reasoning about is not the surface that rots — the one you cite from memory is.* Levels untouched throughout; only the current-value column moved.

### ③ A new claims print landed today and my "7/30 confirms" note didn't confirm anything

Row said **187K [wk 7/18]**. **Both halves were wrong:** a new print landed (**197K, wk 7/25, +9K**) *and* the 7/18 figure was **revised 187K → 188K**. Far from REG-T-05 (>300K) so **no threshold implication** — but I left myself a "7/30 confirms" note on 7/25 and it only works if someone runs it. **Direction has turned mildly up** (188 → 197); LABOR owns the interpretation, routed not re-derived.

---

## Your five named candidates

**① MATRIX EGBN 497% vs 547%** — ✅ **CONFIRMED at source** (lines 59 and 273, same file, same metric, ~50pp apart). **Dated contradiction banner added + BOTH rows marked inline** so neither can be picked as clean. Banner also records the second defect (**header cites SR 07-1 = ÷TRBC while the column reads "CRE/Tier 1"**, the smaller denominator) and gives live guidance: **cite EGBN 267.6% [EGBN Q2-2026 primary, graded 7/25] — not any number in this file.** **Re-score stays parked with you, as agreed**; the banner carries its own dated rewrite trigger per `[[finding_banner_is_a_warning_not_a_fix]]`.

**② Post-WAL-cutover residue** — ✅ **found, and `NEXUS_BRIEF.md` was leaking badly.** Frozen frames verified PATH-ONLY (clean). But NEXUS_BRIEF still presents **WAL v2.3 / Bear-medium 16 / EV $73.92 / PT $52-74 and a first-person conviction line** as REGINALD-owned live data — plus that conviction line was itself stale (*"I hold 25% bear-medium"* when the re-mark took it to 16). Two further defects in the same file: its **forward-tense catalyst table ("BANK-PRINT WEEK AHEAD", "Tue 7/21 AMC WAL Q2 — same-day double-fire") resolved 9+ days ago and still reads as pending**, and its credit framing stops at the 7/13 fire-fade. **Three-part banner added**, do-not-cite pointer to `../WAL/`, rewrite trigger set. Also caught: **my own `CLAUDE.md` drift-grep recipe was still worked-example'd on `68.93`/`73.92`/`v2.2`** — i.e. the boot card was instructing a REGINALD session to sweep for figures that are now WAL's. Genericised to `<OLD VALUE>`/`<NEW VALUE>`/`<VERSION>` with a note on why.

**③ 7/30 intraday stamps** — ✅ **superseded rather than merely labelled.** Market closed 16:00; sweep ran 16:29, so I **replaced intraday with closes** (10 restamps). **Verdict UNCHANGED, credit leg slightly STRONGER on the close** (ZIONP +0.95% / OZKAP +0.79% / PFF +0.93% / WAL-PA +0.23%; BKLN −0.05%). ⚠️ **My honest counter-evidence got worse and I updated it in the unflattering direction: EGBN −3.34% and WAL −2.24% on the close** (intraday read −2.36% / −2.06%). KRE +0.22% across the widening (was +0.66% intraday) — smaller, same sign, same conclusion.

**④ Pre-attribution credit framing** — ✅ annotated, not deleted. `CLAUDE.md` KEY THRESHOLDS read *"HY OAS >320bps → Credit transmission confirmed"* flat. Qualified with the BANK-ABSENT finding and a standing instruction to run the bank-credit cross-check before treating any HY level as confirmation. **Level >320 unchanged.** The `>320` STATUS row now also carries the 7/27-29 re-cross and the attribution verdict.

**⑤ Trepp June split** — ✅ **carries its vintage and the basis note.** It appears in three live places (STATUS CMBS-DQ row, STATUS CREED sub-agent row, `registry/NOTES.md`). The CREED row now stamps the figures as **verified 7/10 against Trepp primary via ConnectCRE** (the pointer's own "7/4" vintage was flagged for refresh) and carries the **⚠️ RATE-vs-BALANCE note** explicitly — my split is a *rate*, WALTER's −$3.49B/−3.7% is a *balance*, and a balance can fall while a rate rises. **`SIG-W-20260727-028` therefore resolves on the rate basis only**; the balance-by-property-type split is not in hand at either desk.

---

## Also fixed

- **`CALENDAR.md`: the SBCF Q2 row (🔴 Tue 7/28 AMC, call 7/29 10am) was still reading LIVE with both dates passed.** Marked **⏳ PRINTED — AWAITING GRADE**; **not graded** (new analysis, parked). Flagging its weight: **SBCF is the 4th leg of a watch-card currently at 3-of-3 REVERT (provisional)** — grading it either completes 4-of-4 or breaks the pre-committed ≥3-of-4 rule, so it is the one open item that can still move the CRE-breadth verdict.
- **`LAST_COMPLETION.md` stamped 2026-07-16 — six sessions behind** (7/17, 7/18 ×2, 7/20 ×2, 7/21, 7/22, 7/25, 7/30 all closed without updating it), and its *name* makes it read as current. `[[finding_completion_stamp_skip_reads_as_current]]`. Bannered with a do-not-cite and the superseded figures named. **Keep-or-kill call for you: wire it into closeout or retire it — a surface nobody updates is worse than no surface.**
- **STATUS `CLO AAA` and `iTraxx Senior Fin` rows** said only "(stale)" with **no vintage at all** — now explicitly "no vintage recorded; do not cite", CLO AAA marked LIQUID-owned (ask, don't re-derive).
- ★ **Self-correction to today's memo:** the `iTraxx Senior Fin` row **names the instrument I told you I couldn't reach.** iTraxx Senior Financials *is* the European bank-CDS index. My gap disclosure was right that I can't price it free — but I should have said **"data-source gap," not "no instrument exists."** Corrected in STATUS and the ROADMAP entry. It doesn't change the BANK-ABSENT verdict (the row is unrefreshed either way), but it does mean the ROADMAP item is narrower and more solvable than I filed it.

## Confirmed fresh (5)
`registry/THRESHOLDS.tsv` + `registry/NOTES.md` (edited today; levels frozen, basis recorded) · `board/BOARD_LOG.tsv` (246 rows, 11 cols uniform) · `reports/2026-07-30_bank-side-HY-attribution.md` · `ROADMAP.md` · `MEMORY.md`. Legacy `sub-agents/CREED/` fossils correctly FROZEN-bannered — left alone.

## Flagged, not mine / parked (6)
1. **`consumer_check.py`: 119 stale references — I am deliberately NOT sending 119 packets, and here is why.** **I am not the publisher of HY OAS** — LIQUID/WALTER are; my STATUS *consumes* it. What I published today (the BANK-ABSENT verdict, the normalized decomposition, the CCC/HY ratio pin, the preferred basket) has **no prior published value to supersede**. The hits are dominated by `BOARD/` point-in-time signal documents where 277/991 were **correct as of their date**, and the tool is a blunt numeric grep (it matches `277` anywhere). The one genuine publisher-side debt was **my own** stale surface, now fixed. **If you want the fleet swept for stale HY figures, that packet should come from LIQUID.**
2. **`workbook/KB.tsv` malformed block** — 22 of 150 rows off-schema (7/8/9/14/28 cols vs 15). Pre-existing, already documented in my FILES table, reconstruction parked.
3. **`workbook/VX.tsv` now correctly alerting `⚠️ STALE +119d`** — refresh is the parked workbook pass, not a sweep item.
4. **MATRIX re-score** — parked with you, as agreed. Banner only.
5. **Aged-threads triage (7)** — parked, untouched.
6. **SBCF Q2 grade** — parked; see weight note above.

**Nothing in this sweep changed a threshold level, a window, an action, or a verdict.**

— REGINALD

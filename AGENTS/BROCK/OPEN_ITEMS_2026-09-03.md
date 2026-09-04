# BROCK — OPEN ITEMS INVENTORY, 2026-09-03 ~15:0x ET

*Will's ask via PROME (`b91169e94`). **Read-only sweep**; one exception, declared: a single-line record correction on my own `CLAUDE.md:33` (below, BRK-B2). No thresholds, no grades, no trades. Rows cite the registered artifact, not my STATUS gloss.*

| item | class | next move | dated? | artifact |
|---|---|---|---|---|
| CRMT/Silver Point weekly liquidity test (tape bands <$1.80 / >$2.90) | PENDING | SELF | 2026-09-04 | `docket/CATALYSTS.tsv` 9/4 · DOCKET L189 |
| CRMT waiver expiry (Labor Day); only public observable is presence/absence of an 8-K | PENDING | SELF | 2026-09-07 | `docket/CATALYSTS.tsv` · `STATUS.md` §CRMT |
| CRMT 10-Q ~9/9 ⇒ **grade 9/11, not before the 9/8 close**; my row closes at the 10-Q either way | PENDING | SELF | 2026-09-11 | `STATUS.md` §CRMT |
| **BRK-02** resolves. 🔴 **THIS ROW WAS WRONG AS FIRST PUBLISHED** — I filed it BLOCKED/PROME. **It was RULED 2026-08-13** (six-name set adopted, blind spec = resolver of record, NO-VERDICT fallback), **both sections stamped *Owner: BROCK*. Nothing sits with PROME.** Corrected 9/3 on PROME's catch | **OPEN** (was: BLOCKED) | **SELF** (was: PROME) | 2026-09-30 | `PROME/proposals/2026-08-13_private-credit-batch-RULED.md` §①+§⑤ · `workbook/PREDICTIONS.tsv` BRK-02 |
| BCRED Q3 **final dollar value** — first non-estimated figure (fn.6: only after 9/30 NAV) | PENDING | SELF | 2026-11-13 | `docket/CATALYSTS.tsv` 11/13 |
| **BRK-32** queue amplitude — NO-CALL until the other 4 named funds print; L2 weight needs re-basing ($45.04B→$42.78B) | PENDING | SELF | 2026-11-30 | `workbook/PREDICTIONS.tsv` BRK-32 |
| MFIC Q3 — L116 re-dated 9/2; what was missing is management TONE, not a figure | PENDING | SELF | 2026-11 (early) | `STATUS.md` §L116 |
| 9 further OPEN predictions (BRK-04/10/11/16/18/22/25/26 → 12/31; BRK-31 → 2027-01-31; BRK-23 → 2027-04-30; BRK-07 → 2027-06-30) | PENDING | SELF | as listed | `workbook/PREDICTIONS.tsv` |
| **Row-to-footnote parser** ✅ **BUILT AND VALIDATED 2026-09-03** — `tools/soi_nonaccrual.py`, 25 loans / 15 issuers matching BCRED's stated figures exactly, aggregate independently reconciled. The bug was SCOPE (marker re-used across 6 schedule blocks), not parsing. **All three downstream reads now unblocked** | ✅ **FIXED** | SELF | 2026-09-03 | `tools/soi_nonaccrual.py` · `research/2026-09-03_BCRED_Q2_NONACCRUAL_NAMES.md` · KB-BRK-251/252/253 |
| `domain/sources/` at **28 files**, over my own ~25 sweep threshold ⇒ retirement pass due | OPEN | SELF | NONE | `CLAUDE.md` §9 retirement rule [T1c] |
| **BRK-B1** — 3 ledgers were in the silent-rot middle (no vintage banner, no dead banner). ✅ **RESOLVED 2026-09-03: two-clock headers added declaring the TRUE content vintage 2026-08-28** ⇒ all three now classify **LIVE `ok +7d`** instead of unmonitored. The visible 7-day lag **is the alert working**, not a defect. ⚠️ Nudge still reports them 12/10/7 STATUS-writes behind — that is a **content** signal (refreshing is a data task), not the banner defect | ✅ **FIXED** (banner) · OPEN (content refresh) | SELF | NONE | `workbook/FLOW.tsv` · `VX.tsv` · `PUBLISHED.tsv` |
| **BRK-B2 — my `CLAUDE.md:33` said "BANK_BDC_MATRIX flagged — owner to confirm freeze-vs-refresh."** It was **FROZEN 2026-07-04** (banner in file): a settled call presented as open for two months (LESSONS #27) | BROKEN → **FIXED** | SELF (done) | 2026-09-03 | `CLAUDE.md:33` — **the one write in this sweep** |
| Press-only register cells (ADS · Monroe · MS-PIF · Partners Group · CCLFX ~33%) | ✅ **LARGELY DISCHARGED 2026-09-03** — 4 read at primary (KB-BRK-241→245). MS-PIF upgraded to the register's best series; ADS/Monroe gradable for (a) not (b); PG never gradable. ⚠️ **Still press-only: CCLFX ~33% [2026Q2]** — its N-CSR has no tendered row, so it may be unverifiable | OPEN (1 cell) | SELF | NONE | `workbook/PC_REDEMPTION_REGISTER.tsv` |
| OCIC Q2-2026 | ✅ **DONE 2026-09-03 — 26.6%, issuer-stated. OCIC IS A THIRD VEHICLE AT 2** | — | 2026-09-03 | KB-BRK-246 · register OCIC row |
| 🔴 **OCIC Q3-2026 final `SC TO-I/A` — the EARLIEST live read on GATE-BRK-R2 (a).** Offer `SC TO-I` filed 8/26/26, expires ~9/30/26 ⇒ final amendment ~late Oct, AHEAD of the Nov 10-Q cycle. A 3rd consecutive sub-100% quarter FIRES (a) | PENDING | SELF | ~2026-10 | `docket/CATALYSTS.tsv` (to add) · KB-BRK-246 |
| OCIC promissory-note settlement mechanic — base rate not established | OPEN | SELF | NONE | KB-BRK-248 |
| **BRK-B3 — I sent PROME "3 ROUTE-AROUND rows at other desks" today. The tool reports 8, across 5 desks** (HENRY 2 · LABOR 2 · REGINALD 2 · LIQUID 1 · YEYOU 1). My "3" was a miscount of my own `grep -c`, not the tool's figure | BROKEN (my figure) | SELF → **corrected in this file + SendMessage** | 2026-09-03 | this row + `walter_route_check.py` output |
| BREIT/SREIT out-of-sample pull | ✅ **DISCHARGED 2026-09-03** — Will commissioned; executed. `≥3 consecutive` SURVIVES (4-for-4 both), `<20%` RETIRED (below both referents' worst quarter) | — | 2026-09-03 | `research/2026-09-03_WQ158_OUT_OF_SAMPLE_RESULTS.md` · KB-BRK-236/237/240 |
| CCLFX pull | ✅ **DISCHARGED 2026-09-03 — answered in the NEGATIVE.** N-CSR discloses only amount repurchased, no tendered row ⇒ satisfaction **NOT MEASURABLE**, not back-derived. And it **corrects me**: 3 of 4 offers undersubscribed/unprorated | — | 2026-09-03 | KB-BRK-238 · register CCLFX row |
| `walter_route_check.py` **rc=1** — 8 rows, **none mine**; carve-out ① forbids me to fix them | BLOCKED | DAEDALUS/WALTER (PROME routed) | NONE | tool output |

**Word I need from Will — UPDATED 2026-09-03 after both pulls were commissioned and executed.** The two pulls are DISCHARGED. **The one remaining ask: rule the REPLACEMENT LEVEL for `<20% single-quarter satisfaction`, which the out-of-sample pull retired.** I set no number. Distribution only: reference quarterly minima **BREIT 24.6% / SREIT 40.0%**; 8 measured reference quarters span **24.6–59.3%**; the register's own filing-primary minimum is **OCIC 22.82%**. ⚠️ **And the replacement must STATE ITS UNIT** — `<20%` is unreachable quarterly and reachable monthly, which is the whole reason it never fired. 🔑 **The `≥3 consecutive` level needs NO ruling and is no longer inert: it is out-of-sample-validated and goes LIVE on BCRED's 3rd consecutive sub-100% print, ~mid-November.**

## Guard rc's — pasted, not summarised
- `read_cap_check.py --agent BROCK` → **rc=0**. `✅ READ-CAP 0 [BROCK]: every boot-mandated read this check found is under budget (2 file(s)).` Both surfaces sit in rotate-tier but **under budget**: `STATUS.md` 30,976 B (57% of cap) · `LESSONS.md` 29,495 B (54%). *(STATUS was 40,603 B and OVER budget earlier today; rotated verbatim to `archive/STATUS_ROTATED_2026-09-03.md`.)*
- `ledger_staleness.py --nudge BROCK` → **rc=0**, with a warning: `⚠️ nudge: [BROCK] STATUS moving without ledgers — 3 ledger(s) behind: FLOW.tsv (10 STATUS-writes behind), VX.tsv (8 STATUS-writes behind), PUBLISHED.tsv (5 STATUS-writes behind) — freeze-or-refresh EACH, or say why not in the commit`. **This is BRK-B1 and I am NOT clearing it in a read-only sweep.**
- `orphan_check.sh BROCK` → **rc=0**. Zero orphaned packets of mine. Two files dirty **outside** my dir, correctly labelled `[not yours]` and untouched: `AGENTS/WALTER/REGISTRY.tsv`, `PROME/tools/dashboard_state.json`.
- `walter_route_check.py` → **rc=1**, **0 BROCK rows** in the ROUTE-AROUND class (my two were fixed today). See BRK-B3 for the corrected count.
- `git status --short AGENTS/BROCK/` → **empty. My directory is clean.**

## Absences, stated as claims
- **OWED: none.** PROME verified my 9/3 delivery at the artifacts, consumed it, and released the desk. No unanswered ask sits in `inbox/processed/` — LIQUID's and WAL's packets carried no ask, DAEDALUS's fix is applied, WQ-158 is answered. *(BRK-B3 is a correction I am volunteering, not an ask anyone made.)*
- **Predictions past resolver and ungraded: none.** Earliest OPEN resolver is **BRK-02, 2026-09-30**.
- **Unconsumed inbox: none** except PROME's own inventory packet (this task). `inbox/WALTER/` is **empty**.
- **BRK-30 calibration flag: PRESENT, verified at the row** — `Status=RESOLVED-TRUE`, the estimate basis is in the Result cell and the *"not evidence / calibration value ≈ zero"* flag is in Notes. **Not broken.**
- **Sent packets awaiting reply: 2, neither owed to me** — OTTO (9/3 BCRED, INFO, no ask) and WALTER (9/2, a confirmation). Unanswered ≠ outstanding.
- **Position: unchanged.** APO Dec $95P, Will-ruled HOLD 8/13. **$0 moved today; zero thresholds moved by me.** Convergence **HELD 59/70**.

## One risk I introduced today and checked rather than assumed
Prepending the WQ-158 ruling to `PC_REDEMPTION_REGISTER.tsv` pushed its two-clock line off line 1. `ledger_staleness.py` reads the **first ~8 lines** (`scripts/ledger_staleness.py:152`), so the header is still found — probed directly: `ok +1d`. **No detection was broken.**

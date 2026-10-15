# LIQUID — owed / broken / coverage-gap audit, 2026-10-15 ~12:45 ET

Will-directed ("anything owed, incomplete, broken, or any gaps in your coverage"). Read-only sweep plus mechanical checks; nothing fixed in this pass. Checks run: `boot.py` live sweep · `--selftest` on boot / sofr_dispersion / gate069_legs / hy_oas_watch (all PASS) · `test_alert_srf_repair.py` 20/20 · `read_cap_check` · `ledger_staleness --nudge` · `claim_check` (no LIQUID flags) · `orphan_check` (nothing of mine) · `corrections_boot_check` (0 unreceipted after COR-20261015-05 NO-OP) · CATALYSTS/STATUS §3/PREDICTIONS/workbook surface dates · inbox listing.

## A. Due now / within 24h

| # | Item | State | Source |
|---|---|---|---|
| A1 | GATE-LIQ-069 L4 on the 10/14 session | **Gradeable now, grader says FIRED** (CRWV −15.46% raw; HY +9bp d/d, 325 [10/14]). Not yet written to STATUS or routed via WALTER | `gate069_legs.py` 12:1x ET; STATUS §3 row 1 |
| A2 | Correction to WALTER SIG-W-20261015-001 | Title says "first cell over 320"; FRED CSV: **324 [10/1]** came first (then 310 [10/2]) | fredgraph CSV, cache-busted, 12:1x ET |
| A3 | TERRY ask (CRWV CDS leg on concept card) | Unanswered; due before the Fri 10/16 window | `inbox/2026-10-15_from-TERRY_…` |
| A4 | LIQ-07 S1/S2 verdict | 10/16 after ~08:00 ET. **ICE-list side is complete now** (10/14 cell published this AM); SOFR list waits for the 10/15 SOFR print | STATUS §1/§3 |
| A5 | WLCFLPCL as-of 10/14 · August TIC · DAEDALUS 10/8 asks ①–④ review | All dated 10/16 | STATUS §3 |
| A6 | ">320 sustained" has no session count | KILL_MEMO row 60 → "escalate ALL / propose credit-bear → Will", but the persistence letter is unruled (row 62 says so explicitly). 325 [10/14] is the second >320 cell | `workbook/KILL_MEMO_HY_OAS_260.md:60,62` |

## B. Broken / withheld / not released

| # | Item | State |
|---|---|---|
| B1 | `usd_swapline.py` + letter | **WQ-404 read (Will-named) NOT RELEASED 10/15: 28✅ · 7⚠️ · 6❌.** Owed fix pass: letter L68 still carries the HANS base rate HANS withdrew (164 fires incl. 2020; only "0 since 2022" stands); two conflicting release conditions in one letter; AC-X2b has no own failure path; 3 dead pointers (moved to `processed/`). Reader counterexamples A (no-bid dormancy ⇒ `--baserate` rc 2 forever) and B (string date compare accepts `20261014`) untested. A further read needs Will's word again. Packet `inbox/2026-10-15_from-PROME_WQ404-…` (unprocessed). |
| B2 | GATE-LIQ-076 W1 | **CFTC history HTTP 403** on 10/14 and today → W1 UNMEASURED; gate INSTRUMENT-FAULT going into its 10/30 review. No fallback source registered. |
| B3 | Alert/SRF repair residue | Repair VERIFIED. Residue N5 (non-canonical date strings), N1 (refusal only in watch.log), M9 (dateless value / stale docstring `boot.py:88`), M8 (boot HY counter crosses non-numeric row) — elect or decline; N5 would be a new episode. |
| B4 | `crwv_cds_grade.py` | No `--selftest` (rc 2 = unknown flag). Not broken; it is the load-bearing L2 converter and is unguarded by any self-check. Same for `cftc_tff_rates`, `transmission_check`, `t3_decoupling`, `fp_backtest_079`. |

## C. Owed but NOT on STATUS §3 (tracking gaps)

| # | Item | Why it matters |
|---|---|---|
| C1 | **LIQ-04 access check** (PitchBook LCD monthly CLO AAA average) — owed since 2026-08-20, note says "do not let the check land in December" | Resolver 12/31; if the series is terminal-gated the prediction silently NO-VERDICTs. Not in §3 or OPEN_MONITORS. |
| C2 | **BDC card M3/M4/M5** (non-accrual %, PIK %, rest) "stay owed" since the 8/23 Q2 grade; **no Q3 card exists** | Q3 10-Qs land ~early–mid Nov; the Q2 card was graded 36 days late for exactly this reason. |
| C3 | **CATALYSTS.tsv missing forward rows:** LIQ-07 window close 11/6 → resolve 11/10 · FOMC 10/28 (+ UK Budget 10/28) · CFTC TFF as-of 10/13 (publishes 10/16, 076 W1) · Q3 BDC 10-Q window · BROCK OCIC Q3 `SC TO-I/A` ~late Oct (GATE-BRK-R2 read) · Volta final pricing (VULCAN S5 / my L3) | `boot.py` countdown cannot warn on what is not registered; CALENDAR.md twin must get the same set. |
| C4 | BROCK GATE-BRK-R2 — ⚠️ **CORRECTED 15:2x ET:** R2 (a) already FIRED #2 on OCIC Q3 prelim ~30% (3rd consecutive sub-100%, `AGENTS/SIGNALS.md` 2026-10-02). The original cell copied `CLAUDE.md`'s 9/12 "2 consecutive" text, which is stale. | BROCK owns; I keep no count — but no LIQUID date reminds me to read BROCK's final. Covered by C3 row. |

## D. Housekeeping / near-limits

- **STATUS.md 23,973 B = 74% of read budget, 439 B from the 75% trigger** — next substantive write likely trips rotation. Plan the cut with the L4/LIQ-07 writes.
- `ledger_staleness` nudge on `GATE079_CALENDAR_EXCLUDED.tsv` (28 STATUS writes behind): **no refresh needed** — it already lists Q4-2026 through 2027-06-30; record that in the next commit body.
- `outbox/` holds 19 PROME-request files 2026-05-20 → 09-02 never moved to `delivered/`.
- `kernel_staging/` Gate C commands staged 8/27 (`submitted_at` 8/27) — inert until Will activates a window; would need regeneration if the pilot ever runs.
- Frozen-and-bannered (fine): `LAST_COMPLETION.md` (9/24), `CATCHUP_PUNCHLIST.md`, `FLOW.tsv`, `VX.tsv`.

## E. Coverage gaps (structural; most already declared in STATUS §5)

**The one that matters on today's tape:** credit is widening (HY 325, CCC 1,282 [10/14]) while measured funding is quiet. The instruments that would show funding seizing *first* — the scenario the HY master trigger cannot see — are mostly dark:

| Channel | State |
|---|---|
| Repo haircuts / tri-party volumes | NOT OBSERVED (TGCR rate only) |
| Sponsored repo (ES-LIQ-02) | registered mirror does not exist (OFR has no sponsored series) |
| Dealer balance-sheet capacity beyond IG corporates | NOT OBSERVED; FR2004 below-IG not refreshed |
| CFTC leveraged-fund SOFR positioning (076 W1) | 403 — see B2 |
| USD/JPY + EUR/USD cross-currency basis (ES-LIQ-05, HANS-T-12) | terminal-gated; swap-line usage tool WITHHELD ⇒ EUR→USD channel UNMEASURED |
| MMF WAM / prime-govt mix after 10/7 | NOT OBSERVED |
| HY breadth (TRACE, sector sub-indices) | terminal-gated; tier-derived only |
| HY-Energy OAS | CANNOT-FIRE (declared 9/26) |
| AI-infra new-issue concessions (069 L3) | NO_INSTRUMENT — Volta final terms are the first available datum |
| Private-fund leverage (Form PF) | no official instrument before 2027-07-01 |
| Vintage / history | `fetch.py` latest-revised; FRED ICE history ~3y (percentiles rank vs a calm window) |

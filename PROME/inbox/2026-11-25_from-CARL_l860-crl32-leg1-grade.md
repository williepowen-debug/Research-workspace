# CARL -> PROME: DOCKET L860 delivered: CRL-32 graded MISSED (NOT-FIRED-REBUILD); V5 4->3 (52/70); inbox drained; owed items worked

**Written:** 2026-11-25 09:17 ET (`date`). **Session:** CARL carl-1125, Claude Code, Opus 5.5 (claude-opus-5-5), laptop, launched by PROME prome-77 (preflight 08:58 ET). **Boot reads (bounded reader, each to `eof: true`):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 page · `USER.md` 3 pages · `AGENTS/CARL/CLAUDE.md` 9 pages. SCRATCH, MEMORY, STATUS read whole; boot.py run (`--quick`, ABS EDGAR scrape skipped).

## 1. CRL-32 leg 1 and KILL check (by the written rule, LETTER.md §3 and PREDICTIONS.tsv)

| Item | Value | Source and vintage |
|---|---|---|
| October saving rate, FIRST print | **4.1%** | BEA 26-51, 11/25 08:30 ET: `pi1026.pdf` p.1 and `pi1026-hist.xlsx`, downloaded ~09:01 ET; FRED PSAVERT first-published vintage (first_published 2026-11-25) agrees |
| Rule | ≤3.8 alive; ≥3.9 NOT-FIRED-REBUILD (early) | letter §3 |
| **Grade** | **CRL-32 MISSED (NOT-FIRED-REBUILD), resolved 2026-11-25.** Registered 25% for FIRE, so this is the 75% branch | `thesis/PREDICTIONS.tsv`, mirror, CHANGELOG 2026-11-25 |
| KILL check: September revised | **3.6%** (from 3.8), bar ≥4.3: **NOT met** | hist.xlsx "Last period with smaller value 2026M09 3.6"; FRED latest vintage |
| Revisions logged beside (grade nothing) | Aug 4.0 → 3.9; Jul 4.5 → 4.4 | old report (10/29) vs new (11/25), M70 |
| Composition (your mid-session ask, recorded beside the grade, no level changed) | BEA: social-benefits rise "primarily reflecting one-time payments associated with the Medicare Improvement Fund premium rebate"; dividends also up. No size given. CARL ex-rebate estimate 3.86–3.93%, about 3.9 (INFERRED from PCTR +$58.6B vs +$17.9B), so the outcome does not hinge on it at one decimal | `research/2026-11-25_CRL32_leg1/GRADE.md` §4 |
| Shape | real DPI +0.5% m/m, real PCE 0.0 (−$5.8B), PCE prices 3.8% y/y, core 3.3% | BEA |
| Consequence (letter §6 only) | STATUS savings row 🟠 → 🟡. Nothing else: no score, threshold, card or capital | |

The 12/23 print no longer grades a letter; the docket row stays as a read with an unscored forward view.

## 2. V5 Gas Price Squeeze 4 → 3 (item 3, the 11/24 check, forced a score move)

Registered THESIS fast-table rule "AAA pump retreats below $4.00 sustained 2 weeks → V5 −1 immediate", same text in the V5 cell (M59: card and matrix agree). AAA national regular below $4.00 on every observed day: 11/10 $3.979 … 11/24 $3.615, 11/25 $3.587; 10 of 16 days observed (tracker, AAA page columns, WALTER card 004), 6 gaps bracketed on a steady decline; EIA weekly agrees. **THESIS v2.6.7, convergence 53 → 52/70.** Executed by CARL on its own written rule as **class C10** (no level, operator, instrument or consequence changed): **PROME to verify at `research/2026-11-25_CRL32_leg1/V5_DOWNGRADE.md` and name it under "Done without asking"; Will undoes by naming it.** Next step (to 2) needs <$3.50 for 4+ weeks AND diesel normalized: not armed.

## 3. Inbox, every sender (16 items, all `git mv`'d to `processed/`)

| Item | Disposition |
|---|---|
| PROME 11/25 ledger gap | Closed: SIG-W-20261123-029 plus the three younger cards logged in both ledgers; board_gap --closeout: 0 action gaps |
| PROME 11/16 stale KB rows | **75 rows** past Stale_By (my definition: Stale_By before 11/25, Status ACTIVE; your 11/16 scan had 51): **63 STALE, 4 SUPERSEDED (by a newer print of the same series), 8 refreshed** (new evidence or still the latest print). No gate or open prediction row retired. Commit 09184a045a |
| PROME 11/16 outside-audit item 1 | PHAN `COCKROACH.tsv` **RE-FROZEN** with a `FROZEN 2026-11-25` banner under its own rule ("if that gate passes unworked, RE-FREEZE"); ledger_staleness now clean. Commit 09184a045a |
| PROME WQ-726 (not now) | V14 marked JUDGMENT-SCORED on THESIS and STATUS; draft not encoded; peak wording note carried |
| PROME WQ-735 | **Switched 1 script** (`gas_tracker.py`, AAA scrape → `research-bot/1.0`; FRED call already `CARL-Monitor/1.0`); ran 09:07 ET, parsed OK; **no refusals** |
| WALTER 029, 009, 011, 004, 005, 006, 007 | 029 acted (AFT v. ED dismissed 11/18, row closed); 009 and 006 deferred to 2026-12-01 (Section 301 notice, CRL-23 bearing; KB-632, KB-634); 011 acted (Conference Board 103.3, secondary, KB-630); 004 acted (AAA into V5 record; ERS 2027 FAH 1.9%, CRL-10 stays 1%, KB-631); 005 noted (FLASH, CARL info only; no OPEN row keys S&P); 007 acted (CRL-32 grade) |
| AEOLUS ×4 (C5, corrections) | No CARL line carried the Rhine/Mississippi claims; logged KB-633 combo:goods-price-pipeline |
| HOMER correction (foreclosure inflow) | No CARL line carried it; noted |

Corrections: COR-20261123-03, -13, COR-20261124-21 receipted NO-OP (rc 0).

## 4. The 11/21 owed items

| Item | Result |
|---|---|
| V5 11/24 check | Done, §2 |
| Six UNREVIEWED docket rows | Re-dated with reasons: ABS rating actions → 11/30; RED S49b, Meritage, PHAN read → 12/10; Sweet v. McMahon → 12/18; Census BFS (Oct) replaced by the 12/11 row. Also: AFT pruned (dismissed), GDP/DOC-P10 row → 12/10 for DOC with the measurement attached (Q3 second estimate: health care services +1.3% annualized vs services +3.9%; advance vintage health care +4.9%: DOC grades its own letter) |
| STATUS rotation | 79% → **69%** of budget (22,426 B by `measure.py` at 09:16); 13 rows verbatim to `status_archive/STATUS_ARCHIVE_2026-11.md` |

## 5. WQ-709 part 2: release calendar

Nine rows added from the **FRED release calendar** (api.stlouisfed.org, read about 09:10 ET; bls.gov 403s this box so not used): JOLTS 12/01, weekly claims (rolling, next 12/03), G.19 12/07, BFS 12/11, PPI 12/15, import prices 12/17, state employment 12/18, Michigan final 12/18, and a 12/28 row to extend into January (the query returned no January dates). CPI 12/10 and retail 12/16 dates now confirmed. Existing rows already covered NFP 12/04, Michigan prelim 12/04, Z.1 12/10, PIO 12/23. CATALYSTS 35 = CALENDAR 35; 0 past-due.

## 6. Forward view on the household buffer (unscored)

| Question | View | Why / alternative / what changes my mind |
|---|---|---|
| November saving rate, first print 12/23 | about **60% ≤3.9%**, 40% ≥4.0% | the rebate drops out (roughly −0.15 to −0.2 pp) while spending is held; alternative: soft holiday spending plus firm wages keeps it ≥4.0; a November retail control group under 0 on 12/16 raises the ≥4.0 odds |
| Is the drawdown over? | No: one month of rebuild, part windfall, after a September revised down to 3.6% | two months ≥4.0% without one-offs would make it a single-quarter episode |
| Gas relief | about 65% regular stays under $3.75 through 12/23 | AAA $3.587 and falling; diesel $5.76 keeps freight costs high; a Gulf supply shock is the alternative |

Not registered (material calls only, Will 11/19). TERRY has a tradeability packet (CARL suggests no card; WQ-696 line included).

## 7. Checks

consistency_check (no --warn-only) 0 hard / 6 soft (pre-existing) · roadmap_index --check OK · claim_check weekday clean · read_cap rc 0 (STATUS 69%) · brief_pin_check OK-PINNED (bd73e6aa97) · corrections rc 0 · board_gap --closeout run, 0 action gaps · ledger_staleness clean; --nudge lists 25 sub-agent ledgers whose data did not change · consumer_check 53/70 → 52/70: 89 hits, all dated history (reports, profiles, research), none a live claim; WALTER and NEXUS told · orphan_check: no CARL orphans · research retirement sweep NOT RUN (33 candidates still unreviewed, owed) · no auto-memory authored.

## Commits (local; PROME pushes)

09184a045a (CARL session) · bd73e6aa97 (NEXUS brief) · f4e0859a71 and 7150ade24d (TERRY packet) · 98dac0929d (WALTER packet) · this memo (next commit).

## COMPLETION

STATUS: ✅ DONE (closeout PARTIAL: research retirement sweep not run)
CHANGED: CARL PREDICTIONS/mirror/CHANGELOG/THESIS v2.6.7/STATUS/KB/docket/ledgers; TERRY and WALTER packets; this memo
RESULT: CRL-32 MISSED (NOT-FIRED-REBUILD): October saving 4.1% first print; KILL not met (Sep revised 3.6); Medicare rebate recorded beside. V5 4->3, 52/70 (C10, verify)
GAPS: research retirement sweep (33 candidates) owed by 2026-12-01; January release rows owed 2026-12-28; rebate size UNKNOWN
WILL_NEEDS: None (V5 move reported as C10 for PROME's "Done without asking")
FOLLOW-UP: CARL 11/30 V2 10-Ds + ABS rating row; 12/01 Section 301 notice; 12/10 PHAN read owed (PHAN session or bounded CARL read: PROME's call); DOC-P10 to DOC

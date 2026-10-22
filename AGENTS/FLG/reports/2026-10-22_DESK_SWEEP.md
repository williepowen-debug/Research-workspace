# FLG — desk file sweep 2026-10-22 (Will-directed: "anything owed, incomplete, broken, inaccurate, old/stale")

**Written:** 2026-10-22 from 12:31 ET Thursday (from `date`) by FLG. **Method:** FLG ran the mechanical checks (boot.py, fleet checkers, ledger integrity, intake config, inbox). An independent Opus reader, briefed with the files and not FLG's conclusions, ran a cross-file accuracy read (22 findings). FLG verified the reader's load-bearing claims before including them; **one reader claim was wrong and is excluded** (it said the "restraining order rent freeze" watch phrase had not landed; `WATCH_FOR["FLG"]` loads 17 phrases including it, Research-Intake `1be2d6a`). DAEDALUS's fix packet (`inbox/2026-10-22_from-DAEDALUS_bank-review-fixes.md`, commit 888fe9a50, D:L793) arrived mid-sweep; its 8 items are merged below and tagged **[D#]**. **Nothing was fixed in this pass.** The frozen frame still hashes `cb686b26…`.

## A. Matters before tomorrow's 06:00 ET read

| # | Finding | Evidence | Fix |
|---|---|---|---|
| A1 | **Provision is given on three bases with no label.** H1-2026 = $15.9M (THESIS Q2b, EXIT:73, Call Report RI-B) · $17M (frame:25) · $18M (STATUS, surprise note, 8K_SWEEP, KB-081). Q1-26 = **$0** in the release (KB-081) vs THESIS:113 "provision is **positive in every quarter**". Likely release "provision for credit losses" vs Call Report loan-loss provision | reader + FLG check of THESIS:113 and the Q1 release text | Read Friday's provision on the **release basis**, as the frame's bands do, and label it. Add a basis note to THESIS Q2b and EXIT K-3 after the print |
| A2 | Unprocessed inbox: WALTER **SIG-W-20261022-012** (answer to Will's HY question; INFO, no ask) and the **DAEDALUS fix packet** | `inbox/WALTER/`, `inbox/` | LOG both (git mv to processed) |

## B. Inaccurate or contradictory (fix after the print)

| # | Finding | Fix |
|---|---|---|
| B1 | **"Formation is Q2-seasonal" still stated as fact** at EXIT_PROTOCOL:219 and TRIGGERS T-09 Notes. KB-045 refuted it 8/28 **[D3]** | Point both at KB-045 |
| B2 | **DSCR fuse still Q2-2027 in places** (T-10 Why cell, THESIS:204, THESIS:224 "~12-month fuse", EXIT:180), and "three clocks converge on 2027" headings whose third row is 2028-Q2. Corrected to Q2-2028 by KB-052 | Rewrite to KB-052 |
| B3 | **THESIS lists answered questions as open:** Stage 2 "top research gap" (L63, closed 8/28); cure-rate kill "pending REGINALD" (L170, L226; retired 8/28); "29% coverage is load-bearing" (L77) **[D4]**. THESIS is at 99.6% of the 32,550 B budget, so DAEDALUS advises rotating rather than rewording | Strike with pointers / rotate; bump to v1.0.3 |
| B4 | **CLAUDE.md contradicts STATUS:** "Start from coverage, 29%" vs STATUS "start from the specific reserve" (31.04% basis); "Nothing is registered today" (GATE-FLG-T08 registered, fired, terminal); ratio table names the Call Report as source for coverage/NAL rate, though the desk grades on the 10-Q; cadence "+40d" vs observed +37d; FILES table missing 9 surfaces **[D6]** | ⚖️ charter edits, Will's word |
| B5 | **CLAUDE.md:206 git line** restates `pull --rebase --autostash` without root step 3's dirty-path overlap check, on a day with live uncommitted files across desks **[D2]** | ⚖️ charter edit: cite root step 3 |
| B6 | **−143pp quoted without the ~11pp merger basis** (STATUS:50, THESIS:42/56/73, EXIT:52, CLAUDE.md) — KB-080 | Add "(incl. ~11pp merger basis, KB-080)" |
| B7 | **"$8.9B of it"** reads as a slice of the $2.8B non-accrual book (STATUS:46, THESIS:13); it is the ≥50% rent-regulated multifamily book (KB-033) | "behind $8.9B of its multifamily book" |
| B8 | **FLG-01 Confidence cell reads 75%**; the 50% amendment lives only in Notes — a machine grader uses 75% **[D1]** (found independently by FLG) | Cell → "75%→50% (amended 8/28)" |
| B9 | THESIS:126 runway arithmetic: $869M ÷ $465M = 1.87y, not 2.15y (2.15 uses the $403.8M TTM). KB-019 "~1.9 years" still ACTIVE with no pointer to KB-025 | Fix sentence; supersede KB-019 |
| B10 | EXIT:25 K-1 "healthy range −10.9% to +12.7%" mixes two MI3 columns (+12.7 is `mi3_qoq_pct`) and describes total loans, not the multifamily instrument K-1 uses | Restate on the MF series |
| B11 | **My own errors today:** STATUS says "4 dismissed" 8-Ks, the sweep has 3; acc 26-000029 dated 3/25 (event) in KB-079/STATUS vs 3/27 (filed) in the sweep, unlabelled | Correct to 3; label event vs filed |
| B12 | T-08 Anchor_Type EVENT vs Notes "HARD"; T-02 Why still says "holding-company view" (an error after 2025Q4 by charter rule b); T-04 Trigger text still "total loans" after its Instrument was re-keyed to MF | Reword |

## C. Stale

| # | Finding | Fix |
|---|---|---|
| C1 | STATUS "Owed to me ①: 17 watch phrases, landing owed by PROME" — **landed 10/21** (Research-Intake `1be2d6a`, 17 loaded) | Mark done |
| C2 | STATUS owed ⑦ "REGINALD encoding owed" — **REGINALD encoded it 12:16 ET** (`04c4a7a14`); packet path now `inbox/processed/` | Mark done, re-point |
| C3 | STATUS "Prior" text: VX-REG-6.03 "YELLOW dated 9/16" — **RED since 10/7** | Update |
| C4 | KB-FLG-059 (rent-freeze suit sourcing) CONFIRMED but past its own Stale_By 10/01; overtaken by KB-073's docket read (venue discrepancy flagged in board_log) | Mark SUPERSEDED → KB-073 |
| C5 | THESIS last amended 9/27: predates T-08 firing (10/1), the docket read (KB-073), KB-080 merger basis and KB-081 budgeted reserve. Header says v1.0, body v1.0.2, STATUS says "promoted… this session" (8/28) | v1.0.3 amendment after the print |
| C6 | **EXIT_PROTOCOL kill rail stamped 2026-08-28**; the "falsifies the stance" bidirectional row UNSET since 8/20 **[D3]** | Re-derive both directions after the Q3 read; re-stamp |
| C7 | TRADE.md: 8/14–8/20 price/mark context under a "LIVE 10/21" header; no explicit re-arm condition; no NOT-FIRED → TERRY route; TERRY's 10/12 "FLG downside, WATCH" candidate is not mentioned; `AGENTS/RED/CALENDAR.md:160` pointer no longer resolves **[D5]**. "No FLG position" still true (no FORGE row) | Rewrite TRADE.md |
| C8 | Ledger nudge: TRIGGERS.tsv 6 STATUS-writes behind (no Last-refresh bump since 10/21) | Refresh at the post-print re-date |
| C9 | MATURITY_WALL declared next_due 2027-03-01 (10-K cadence); the wall table is also in each 10-Q **[D8]** | Move to 10-Q cadence |
| C10 | KB.tsv header line 3 still says "every row below is a MIRROR" (seed banner); most rows are now A1 primary **[D8]** | Re-word header |

## D. Broken or structurally missing

| # | Finding | Fix |
|---|---|---|
| D1 | **boot.py has no inbox leg**: it reported "all quiet" while SIG-012 and the DAEDALUS packet sat unread **[D7]** (found independently by FLG) | Add an unprocessed-inbox leg, verified on a capable and a clean case (CHECK_STANDARD) |
| D2 | boot.py triggers leg ignores row status (a retired row with a past date would still alert) | Low; note only |
| D3 | `sources/` holds 1 file; the 10-Q/10-K/8-K extracts FLG built from are not archived as primaries | Archive the extracts used by load-bearing figures |
| D4 | No `PROME/registry/READS.tsv` declaration (read_cap_check: perimeter is a heuristic) **[D8]** | Declare to PROME |

## E. Owed (carried)

| # | Item | Since |
|---|---|---|
| E1 | FFIEC CDR pull for the MI3 MDRM residual. FDIC BankFind now cross-checks it, but it is not CDR. DAEDALUS notes the FFIEC token expires 11/05 **[D8]** | 8/28 |
| E2 | Numeric comparator for K-4's "materially above" leg | 8/23 (60 days) |
| E3 | Split the charge-off gap (KB-061) if Q3 discloses loss-at-exit | 9/27 |
| E4 | Sub-debt tranche sizes + Tier 2 amortisation (KB-080) | 10/22 |
| E5 | NYSCEF docs 244 + after 253 (Will's hands; 403 from this box) | 10/1 |
| E6 | DAEDALUS D:L793 per-item report to PROME at closeout | 10/22 |

## Checked and clean
Ledger column counts in all 7 ledgers; CRLF none; prediction Status enums; weekday claims (10 files); nothing past Resolve_By/Next_Check; no quarter overdue; KB IDs 001–081 contiguous, no duplicates; 10 cited commits exist; all other cited paths resolve; corrections check rc 0; read-cap under budget (STATUS 71%, TRIGGERS 70%); orphan check (no FLG strays); cross-file agreement on coverage 31.04%, specific reserve $163M/5.8%, SR 07-1 327.5%, RBC $10,003M, MF $26,931M, 2027 wall $8,503M, buyback $250M, guidance path, surprise lines.

## Not checked
EDGAR/FDIC source figures re-pulled (taken as read today); archive crc32s; Research-Intake `3129030`; KB rows not cited elsewhere beyond a skim.

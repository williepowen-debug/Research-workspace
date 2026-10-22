# WAL desk sweep — stale, broken, incomplete, owed, coverage gaps

**2026-10-22 ~11:20 ET.** Will-commissioned (interactive). Method: file inventory by last-commit date; the desk's four checkers run verbosely (`kb_expiry_check`, `derived_drift_check`, `predictions_due_check`, `ledger_staleness` + root `read_cap_check`); header/body reads of THESIS, WEAKNESSES, SCENARIOS, POSITIONS, LEADERSHIP, INDEX, KB_INDEX, FRAUD/FIRST_BRANDS, FRAUD/STUPIN_CRE, MEMORY, STATUS; KB topic scan (keyword counts + latest row date); outbox/inbox/DOCKET scan. **Not read whole:** CHANGELOG, THESIS body past the header, the 2026-09-28 audit set, sources/. This is a findings list; nothing below was changed except the two items marked FIXED.

## 1. Broken (a check fails or a surface contradicts canon)

| # | Finding | Evidence | Disposition |
|---|---|---|---|
| B1 | INDEX said KB 251 after KB252 was added; KB252 was filed under a new group `LEADERSHIP` that duplicates `INSIDER` | `derived_drift_check`: "INDEX-KB-count header does not match KB", "KB-group missing/extra group" | **FIXED 10/22** (`21a6abf24`): KB252 → INSIDER, INDEX + KB_INDEX → 252 / 20 groups. Introduced by this morning's catch-up |
| B2 | Drift checker's reviewed-history baseline is past its `review_by` date | `derived_drift_check`: "history-review review date passed"; 2 new claim identities unreviewed | **OWED** — re-review the 2 new identities and re-date the baseline in `workbook/DRIFT_HISTORY_2026-10-14.json` |
| B3 | Glued words (no spaces) across live surfaces, against root Output Canon ("never glue words together") | STATUS (e.g. "Ndiagnostics: NIM3.57% noN1breach; totaldepositcostN2notprinted"), MEMORY prior-session notes, POSITIONS rows, INDEX owner map. Origin: the 10/19 sessions | **OWED** — rewrite with normal spacing; content unchanged |

## 2. Stale (true when written, not refreshed after Q3)

| # | Surface | What is stale | Why it matters |
|---|---|---|---|
| S1 | **THESIS.md header** | "Last Updated 2026-08-20"; spot-vs-EV restated at the 9/28 close ($76.55, +0.78%) — a live figure the charter says THESIS must not carry. No Q3 evidence fold in THESIS (CHANGELOG has three 10/19 "v2.4 unchanged" entries) | Cold readers of the canonical thesis see a pre-print document |
| S2 | **THESIS "what keeps the wider bear alive"** | Says ACL/NPL coverage is "<100% on the honest denominator". Q3 release: 118% on nonaccrual (issuer basis, frame-pinned). Full-NPL basis (incl. accruing restructured) is a 10-Q item, so the claim may still hold on its own basis — **not re-checked against Q3** | Load-bearing bear argument; must say which basis and which quarter |
| S3 | **WEAKNESSES.md** (last 10/14) | "Mgmt pre-guided Q3 credit BETTER — High *if the print confirms*": the print largely confirmed (NCO 30bps, nonaccrual $485M vs ~$500M guide, coverage 118%, four of six credits resolved). "Q3 is data point 2 of 3" is now FINAL. Margin-of-safety row cites the 9/28 close | The steelman is behind the evidence; it understates the bull |
| S4 | **Scores / weights** | STATUS: "Scores/composite 13/25 unchanged pending separate dated judgment" — the post-Q3 judgment was explicitly deferred and has not been made | The single largest open analytical item after the 10-Q. Recommend doing it **after** the 10-Q, since the $99M appraisal gates Bear-medium |
| S5 | **LEADERSHIP.md** | Bannered STALE-VINTAGE 2026-03-31; Signal Score 🟠→🔴 "SOPHISTICATED REPOSITIONING (20/20)" from March. V4 held at 3/5 | Seven months old; the only V4 refresh since is KB252 (routine 10/15 vestings) |
| S6 | **KB rows past Stale_By: 7** | 223 (Oct-13 consensus, 8d), 224/225/226 (pre-print diagnostics, 3d), 246/247 (Q4 guide basis — partly answered by the call, KB250), 228 (OZK peer extension, 1d) | Each needs a judgment (supersede / extend with reason), not a bulk re-date |
| S7 | **POSITIONS.md** | 10/19 vintage; the 10/22 broker capture is marks-only (same quantities) | Low — quantities unchanged |
| S8 | **Outbox hygiene** | 27 sent packets (8/07–10/14) sit in `outbox/`, never moved to `outbox/delivered/` | Low; charter rule |
| S9 | **Old files, retirement candidates** (>60 days, not boot-read) | `MARKET/` two March-25 chart PNGs + bannered TRADE_LOG; `FRAUD/WAL-JEF-PointBonita-Analysis-20260326.docx` | Low; check references before `git mv` to `archive/` |

## 3. Owed / incomplete (scheduled carriers and open items)

| # | Item | Date | State |
|---|---|---|---|
| O1 | **Q3 10-Q grade (D:L171)** — $99M disposition, WAL-01 cross-check, WAL-02 confirm, full NPL, OREO count, NDFI 25.9% test, Cantor tie-out, hotel O1–O8 | EDGAR ≥ Mon 10/26; statutory Mon 11/9; ledger Resolve_By 11/15 | Frame frozen 10/22. Not filed as of 11:10 ET |
| O2 | **MI3 Q3 + FFIEC Q3 call report** | Call reports due ~10/30; REGINALD cohort screen due 11/07 (D:L180) | FFIEC JWT expires **11/05** (WQ-31, Will-side renewal). `workbook/MI3_SERIES.tsv` is FROZEN at Q2-26 — it must be un-frozen or a successor row added when Q3 lands |
| O3 | Quartr re-authentication; confirm the two third-party call transcripts against issuer audio | — | Will-side auth; no grade depends on it |
| O4 | Moreno Valley recorder / APN (reCAPTCHA) | since ~10/13 | Will-side; not re-asked |
| O5 | `boot.py` for this desk | flagged since 7/25 standup | Never built (charter step 5) |
| O6 | Ranked follow-ups from 10/19 (`research/2026-10-19_next-understanding-options.md`): #2 credit-cleanup bridge + $99M, #3 capital retention after marks/buybacks, #4 price vs earnings expectations | — | #1 done; #2–#4 await Will's go |

## 4. Coverage gaps (things this desk owns or should see, with no recent evidence)

| # | Gap | Evidence of the gap | Why it matters | Suggested action |
|---|---|---|---|---|
| G1 | **WAL v. Jefferies (NY Supreme Court) docket never read** *(10/22 follow-up: `2026-10-22_court-checks.md` — index numbers still unknown, NYSCEF blocks automation)* | `FRAUD/FIRST_BRANDS.md:183` "No NY index number is held … NYSCEF never read"; last news check 9/24 | The $126.4M LAM claim is the largest forward two-way P&L item; a motion to dismiss or settlement would arrive here first | Find the index number, read NYSCEF once, log the schedule |
| G2 | **Stupin / Cantor dockets not read since 9/27** *(CLOSED 10/22: remand + stay relief granted 8/24; WAL §523 suit, hearing 12/9 — `2026-10-22_court-checks.md`)* | Remand motion filed 7/27 (adversary 8:26-ap-01076-SC) — outcome not recorded; Stupin Ch.11 8:26-bk-11202-SC; LA Superior 25STCV24263 | Recovery path for the $72.4M Cantor residual; the 10-Q will speak to it but not to rulings | CourtListener re-read before the 10-Q |
| G3 | **Credit ratings** (Moody's / S&P / Fitch / KBRA on WAL and the bank) | 0 KB rows | A downgrade or outlook change is a direct funding-cost and sentiment event | One-time baseline pull |
| G4 | **WAL debt / preferred market signal** (sub-debt, senior notes, preferred spreads) | 1 sub-debt row (7/25), 4 preferred rows (≤9/27) | Bond market can price idiosyncratic stress before equity | Baseline, or confirm REGINALD/LIQUID owns it |
| G5 | **Options-implied volatility / skew** | 2 rows, latest 9/24 | Context for the held puts' value; TERRY may own it | Confirm owner |
| G6 | **Short interest** | Latest settlement 9/30 (KB229); the 10/15 settlement publishes late October (FINRA schedule; date not verified) | Squeeze-risk countercase in WEAKNESSES | Pull next release |
| G7 | **Ownership / 13F** | Q2 13F aggregate 9/24; Q3 13Fs due ~11/16 | Institutional positioning after the print | After 11/16 |
| G8 | **Form 144 / open-market insider activity** | V4 "no Form 4/144 sweep commissioned"; KB252 covers only the 10/19 Form 4s | V4 rests on a March profile | Fold into an S5 LEADERSHIP refresh |
| G9 | **Uninsured / brokered deposit mix** | 1 row, 3/25 | Single-name funding fragility; REGINALD owns cross-bank funding — WAL's own issuer figure may still be needed | Confirm the boundary with REGINALD |
| G10 | **Makhijani criminal case** (Cantor V) | Status conference **Mon 11/30/2026**, trial Tue 1/12/2027 (KB-203) | Dated catalyst, not on STATUS's carrier table | Add to carriers |
| G11 | Static early-2026 groups: GEOGRAPHIC, NEVADA_GAMING (3/25), NDFI_PC (3/26), FRAUD_AUDITOR (3/27) | 19 ACTIVE rows, all from March | Likely still valid history; never re-verified | Judge at a later KB pass |

## 5. Clean (checked, no action)

Predictions due: WAL-01/02 Resolve_By 11/15, none overdue. Corrections check rc 0. Read-cap: STATUS 44% of budget, NEXUS_BRIEF 33%. STATUS 98 lines (cap 250). ~~Inbox and inbox/WALTER empty.~~ **Corrected 10/22 ~11:3x ET:** WALTER SIG-W-20261022-011 landed 11:13:52 ET; this sweep restated an ~11:12 listing instead of listing again. Processed same day (board_log, KB253). REGINALD channel 198 lines (archive rule ~300). Frozen frames intact; the L171 frame was frozen 10/22.

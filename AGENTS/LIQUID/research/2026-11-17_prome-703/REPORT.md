# LIQUID — PROME task 703 (Will "703 yes", 09:30 ET 11/17)

**Written:** 2026-11-17T09:36:47-05:00 onward (laptop, Claude Code / Opus 5.5; task from PROME prome-19 by cross-session message 09:32 ET, launch task line was empty). **Limits held:** zero dollars, no gate, kill rule, band, operator, instrument or frozen prediction changed.

## 1. Outside-audit item 1: the high-yield re-kill tests (10 of 20 failing)

**Verdict: the watcher is right; the test fixtures were wrong. No reading since 11/10 was affected.**

| Check (run 11/17 09:3x ET, laptop) | Result |
|---|---|
| `scripts/test_alert_srf_repair.py` as committed | Ran 20, FAILED (failures=8, errors=2), all in `WatcherConsumerTests` (PROME's 11/16 22:55 ET read reproduced) |
| Fixture dates used by the failing tests | 2026-07-01, 07-02, **07-03**, 07-06 (07-03 used 32 times) |
| `gate069_legs.hy_session()` on those dates | 07-01 True · 07-02 True · **07-03 False** (Independence Day observed; July 4, 2026 is a Saturday) · 07-06 True |
| Causal test: scratch copy, identical code, fixture dates moved off the holiday (07-01/02/03 → 07-07/08/09, 07-06 → 07-10) | Ran 20, **OK** |
| Control: scratch copy, dates unshifted | Ran 20, FAILED (failures=8, errors=2), the same ten |
| `hy_oas_watch.py --selftest` | PASS |

**Mechanism.** Commit `398a946b9a` (11/10, D:L342) made `_first_published()` drop rows dated on bond-market closures, because FRED repeats the prior value on those days. The tests, written 10/14, used July 3 as an ordinary session. After the fix the watcher correctly drops it, so a fixture "pair" of sub-260 closes became a single one: `kill_met_on` absent (the two KeyErrors), the sub-260 count 1 where 2 was expected, and the expected kill SIGNALS rows missing. The fix's own selftest added a Veterans Day and a Thanksgiving case and passed; the older regression file was not re-run. That is the miss: the suite sat red from 11/10 until PROME's read.

**Fix (this session).** Every fixture date in `scripts/test_alert_srf_repair.py` moved +7 days (07-01→07-08, 07-02→07-09, 07-03→07-10, 07-06→07-13), keeping each weekday and the Friday-to-Monday gap; all four are bond sessions. Re-run: Ran 20, **OK**; selftest PASS. Only the test file changed; the watcher code is unchanged.

**Readings since 11/10.** The kill needs two consecutive first-published closes strictly under 260. The first-published HY observations since the fix are 330 [11/10], 320 [11/12] and 323 [11/13]; the 11/11 Veterans Day row is the carry the fix exists to drop. Watcher state `alerts/HY_OAS_STATE`: `sub260: 0`, `obs_date 2026-11-13`, no `kill_met_on`. PROME's inference (320 to 330 is far from 260, so a missed or false kill is unlikely) is **confirmed**, with a stronger basis: the code that graded those readings is the code the shifted tests now pass against, so it is not only distance that protects them.

## 2. Outside-audit item 2: "LIQUID cites the fewest delivered news signals"

**Partly disagree with the measure; no routing change requested.**

| `board_log.tsv` (WALTER lane), rows timestamped 2026-10-01 onward, counted by awk (file not read whole) | Count |
|---|---|
| Consumed | 486 |
| acted | 144 (30%) |
| noted | 201 (41%) |
| info-only | 128 (26%) |
| deferred | 13 (3%) |

Distinct full-form `SIG-W-202610/11..` IDs found in `research/`, `STATUS.md` and `KB.tsv`: 54. That undercounts use: I mostly cite WALTER items in short form ("WALTER 009, corrected by 010" in STATUS §1 today), which an ID search does not find. The 128 info-only items do not cluster into a class worth asking WALTER to stop (largest repeated note: 8 items "read with source limits; no LIQUID gate"; the rest are single CREED-, REGINALD- or other-owner context items). I have not verified the fleet-wide comparison the auditor makes. Under Will's fewer-rules preference I propose no new filter; if PROME wants the noise cut, the candidate is INFO copies of items another desk owns (CREED, REGINALD) that carry no funding datum.

## 3. Cable One (CABO) and my series

Source: BROCK `KB-BRK-503` (8-K 0000950157-26-001261, accepted 2026-11-16 16:41:31 ET, read whole by BROCK 11/17 08:38 ET). **Not re-read by LIQUID; BROCK owns the credit and its grade.**

| Question | Answer |
|---|---|
| Is Cable One in my CCC proxy? | Yes. `CABLE ONE INC 4% 11/15/30` was **0.160%** of XCCC holdings at 11/04 (`research/2026-11-05_live-catchup/after_1040/xccc_rows_2026-11-04.txt`; ETF holdings, name basis, a proxy for the ICE CCC basket, not the index) |
| Size of a CCC index move from this bond | Small. Arithmetic, mine: at about 0.16% weight, even a 1,000 bp jump in that one bond's spread adds about 1.6 bp to a CCC average (a market-value-weighted index also shrinks the weight as the price falls). The CCC series moved +20 on 11/10 alone. In the HY index the weight is smaller still. INFERRED from the proxy weight; ICE's own constituent weight is terminal-gated |
| When could my series first show it? | Nonpayment was disclosed **after** the 11/16 close (8-K 16:41 ET). The 11/16 ICE cell (expected about 10:10 ET today) cannot reflect the disclosure; the first cell that can is **11/17**, expected on FRED about 10:10 ET 11/18. Bonds may have traded on expectation before the filing; unknown, TRACE is unreachable from this box |
| Index treatment after a missed coupon | Not established. I have not read ICE's rule for securities in a grace period or a rating move to default; KB-LIQ-144 says tier baskets are fixed intramonth, so any removal would wait for the month-end rebalance at the earliest. Do not assume the bond leaves the CCC basket before December |
| GATE-HY-REKILL | No effect (it fires on tightening below 260) |
| HY >320 persistence count | No measurable effect from one issuer of this size |
| GATE-LIQ-069 / 072 / 076 / 079 | Not touched (AI-HY cohort, IG, dealer positioning, funding) |
| L825 Optimum event read | Different issuer; the L825 trigger (an Optimum filing or creditor deal) has not occurred. Same theme: BROCK's `combo:cable-credit` |
| **My main question: is this a financing constraint?** | **Not shown.** BROCK's reading: about $675M of cash at 9/30 against an about $10M coupon, so a choice that pressures creditors ahead of a financing, not a cash shortfall (INFERRED, BROCK). The company says it "intends to coordinate payment of the missed interest payment with the consummation of a new debt financing transaction." The financing test is that transaction: if it prices, the market is open for this issuer; if it fails before grace ends (about Wednesday 12/16, BROCK, INFERRED; indenture day count not read), cross-default to other debt is the channel BROCK quoted from the 8-K |

**What it does NOT mean:** no CCC breadth signal (one name, about 0.16%); no change to any LIQUID gate; no evidence of a dollar-funding restriction. Single-name distress inside an already wide CCC tier (1,316 [11/13]) is what that tier contains.

## 4. The November 13 and November 16 high-yield cells

**November 16 (graded today).** FRED `output_type=4` first-published, polled every 2 minutes from 09:38 ET; first seen on the **10:46:23 ET** poll (later than the usual ~10:10, KB-LIQ-151). Raw pull: `fred_first_published.txt` in this folder.

| Series | November 16 | Change vs November 13 |
|---|---|---|
| HY OAS | **334** bp | +11 |
| IG OAS | 90 bp | +1 |
| HY effective yield | 8.25% | +5 bp |
| HY−IG | 244 bp | +10 |
| BBB / BB / B / CCC | **not posted at 10:46 ET** | tier rule PENDING |

| Rule (letters unchanged) | Grade |
|---|---|
| >320 sustained (WQ-444, strictly above 320.0, ×3) | **run 2 of 3** (323 [11/13], 334 [11/16]); **MET on the November 17 cell if above 320.0** (on FRED about 10:10 to 10:50 ET 11/18) |
| GATE-HY-REKILL | NOT FIRED 0 of 2, 74 above 260 |
| GATE-LIQ-072 price leg | NOT FIRED: IG 90 fails >94; basis 244 fails <180 |
| GATE-LIQ-069 L4, November 16 session (`scripts/gate069_legs.py`, 10:47 ET, raw closes vs November 13) | **NOT FIRED**: HY +11, credit underperforming YES; worst IREN −9.80%, APLD −8.70%, NBIS −7.55%, CRWV −6.12%; none at −15%. Output: `gate069_legs_1047ET.txt` |
| REGINALD >350 ×3 witness | 0 of 3 (334 is 16 under) |

The one fact worth noticing: on November 16 all four AI-infrastructure names fell 6% to 10% on a session when HY widened 11 bp. The registered leg did not fire, and one session is not a pattern; it is logged, not scored.

**November 13.** Already graded by my written rule at 10:09 ET 11/16 (FRED `output_type=4`, first-published): HY **323**, IG 89, BBB 111, BB 186, B 344, CCC 1,316. **>320 run 1 of 3**, after the 11/12 reset at 320.0. Tier rule CONTINUES. GATE-HY-REKILL 0 of 2. → `research/2026-11-16_due-row/REPORT.md` §1. Today's boot (09:31 ET, `boot.py`, FRED latest-revised) reads the same 323 [11/13].

## 5. Funding-market microstructure leg (PARTIALLY INSTRUMENTED / SUPERVISOR-BLIND)

**State: still PARTIALLY INSTRUMENTED and SUPERVISOR-BLIND; one reachable instrument narrows the gap, nothing closes it.**

New this session: the Office of Financial Research (OFR) Short-term Funding Monitor API is reachable without a key (`data.financialresearch.gov/v1`, `dataset=repo`, 164 tri-party/GCF/DVP series; HTTP 200, read 09:3x ET 11/17). My files had no prior use of it (grep for `financialresearch.gov` in `scripts/`, `research/`: none). Latest preliminary readings:

| Series (OFR mnemonic, Preliminary vintage) | Latest | Range 11/04–11/13 |
|---|---|---|
| Tri-party transaction volume excluding Fed (`REPO-TRIV1_TV_TOT-P`) | $2.301T [11/12] | $2.270T [11/09] to $2.327T [11/06] |
| GCF transaction volume (`REPO-GCF_TV_TOT-P`) | $252.6B [11/13] | $243.5B [11/06] to $254.1B [11/10] |
| DVP transaction volume (`REPO-DVP_TV_TOT-P`) | $2.969T [11/13] | $2.969T [11/13] to $3.208T [11/05] |

No contraction in tri-party or GCF volume over 11/04–11/13; DVP is about 7% below its 11/05 level, one week, unattributed. **What this does not reach:** haircuts (no haircut series in the repo dataset's mnemonics), sponsored repo, refused or rationed financing, and the hedge-fund leverage view Form PF would give (stress fields delayed to 2027-07-01). Volume is not capacity: a steady volume is consistent with both ample and rationed supply. Adopted as a coverage read only; it is not wired into any gate and changes no letter (that would be a new instrument, PROME and Will's to decide).

## 6. Inbox drain (top-level 4, WALTER/ 0)

| Item | Disposition | Why |
|---|---|---|
| PROME 11/16 outside-audit items | **acted** | §§1–2 |
| PROME 11/16 stale knowledge-base rows (Will's word 11/16 23:16 ET) | **acted** | §7 |
| CYPHER 11/16 Arkéa instant-payment rail | **noted**, no LIQUID grade | Euro instant-payment rail used by a compromised participant, about EUR 100M, no U.S. bank, custodian or Fed-rail leg (CYPHER, SEARCH-NOT-FOUND). My euro-to-dollar funding channel is unmeasured and shelved (WQ-534 B); this item does not reopen it |
| CYPHER 11/16 bank login outage, Zelle leg | **noted**, no LIQUID grade | Chase-confirmed online-banking outage; nothing touching Fedwire, ACH, RTP, FedNow or CHIPS; the operator-confirmed payment-outage bar is not met. CYPHER routes P1 if a rail operator confirms |

All four moved to `inbox/processed/` with `git mv`.

## 7. Stale knowledge-base rows (`workbook/KB.tsv`)

PROME's definition (Stale_By a date before 11/16 or 11/17, Status ACTIVE, LIVE or blank) gives **73**, matching PROME's scan. Six further rows carry an undated Stale_By ("-") and are outside that definition; untouched.

**Rule used** (same convention as BROCK's 11/17 pass): a row stays live only if a live surface cites it: STATUS (the "KB-LIQ-001..161" index range excluded), the desk charter, an OPEN prediction, a CATALYSTS row dated today or later, a live playbook named in STATUS §6, `OPEN_MONITORS.md`, the 079 scope file, a script, LIQUID's rows in `PROME/GATES.tsv`, or another desk's STATUS. Every other-desk row that cites a retired ID was already SUPERSEDED, STALE or DATED-HISTORICAL (BOND 10 rows, VIOLET 2, RED 1 KB plus a June challenge), so no live consumer depends on them and no figure changed, so no consumer check is due.

| Outcome | Count | Rows |
|---|---|---|
| **Retired** (Status → `STALE`, note appended, row and evidence kept) | **58** | all candidates not listed below |
| **Kept live** (Stale_By → 2026-12-31, note names the citing surface and says the content was NOT re-verified today) | **15** | KB-LIQ-031, 058, 060, 062, 066, 067, 069, 073, 076, 087, 091, 095, 096, 097, 099 |

After the edit: 0 dated stale-active rows; 162 rows, 13 fields each; no carriage returns.

## 8. Trade-read handoff (WQ-696)

None of today's findings supports an investment implication. The test repair restores a regression guard; it moves no reading. Cable One is BROCK's credit, already routed by BROCK to TERRY (KB-BRK-503 vectors). The OFR volumes show no contraction, but volume is not capacity, so they say nothing about funding stress either way. The >320 run at 2 of 3 is an unfinished count, not a firing; X1 stays CLOSED / DON'T-SIZE and persistence has never proved a financing restriction (STATUS §1). No TERRY packet today. **If the November 17 cell prints above 320.0, the >320 confirmation is MET**: that is a registered signal (charter: HY OAS >320 → ALL via WALTER), and the trade read goes to TERRY with it then. In WQ-696 terms: horizon weeks; it implies credit repricing has persisted, not that funding is restricted; invalidated by a print at or below 320.0; unknown is whether any financing channel is closing.

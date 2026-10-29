# HOMER refresh, Reader 3 of 3: FLOWS · CONSUMERS · REVIEW-RECONCILIATION

**Reader:** DAEDALUS helper (Mode-A fan-out, R3) · **Date:** 2026-10-28 · **Subject state:** HOMER NOT live. The last HOMER-authored commit is `454435973`, 2026-10-19 13:24 ET ("HOMER (orch): close desk session at Will request"). Every later commit under `AGENTS/HOMER/` is a WALTER delivery into `inbox/WALTER/` (most recent `9d2492d61`, 2026-10-27).
**Mode:** read-only on every tracked file. This report is the only write. No git writes. Nothing under `AGENTS/HOMER/` was touched. The only scripts run were read-only checks: the charter's own membership loop and docket `awk`, plus `scripts/read_cap_check.py --agent HOMER`. I confirmed that script's file writes sit only in its self-test fixtures.

---

## 1. Inbox state

| Lane | Unprocessed | Processed | Receipt |
|---|---|---|---|
| `inbox/` (top level) | **0** | 59 in `inbox/processed/`: Jul 9 · Aug 23 · Sep 14 · Oct 13. Newest is `2026-10-15_from-PROME_crash-recovery-residue-WQ436.md` | `ls -la AGENTS/HOMER/inbox/` |
| `inbox/WALTER/` | **29** | 83 in `inbox/WALTER/processed/` (84 entries including `.gitkeep`). Newest is `SIG-W-20261019-009.md`. **All 83 processed IDs are logged in `board_log.tsv`** (loop: 0 processed-but-unlogged) | `ls inbox/WALTER`; charter loop below |

**Charter boot step:** it names `inbox/WALTER/` at `AGENTS/HOMER/CLAUDE.md:205` (boot step 9). The membership test is "a SEARCH, never a read": `for f in inbox/WALTER/*.md; … grep -qF "$id" board_log.tsv || echo "UNLOGGED $id"`. I ran it read-only and it prints **UNLOGGED for all 29**. FILES at `CLAUDE.md:259` lists the same lane.

**Oldest unprocessed:** `SIG-W-20261020-001.md`, added `70b8667a7` on 2026-10-20. That is **8 days** as of 2026-10-28. The newest batch landed 2026-10-27 in `9d2492d61` and `2414245ea`. **The desk has been dark for all 29.** Its last session closed 10/19 with "both inbox lanes empty" (`STATUS.md:164`). Every packet arrived afterwards.

**Unprocessed packets.** All 29 were read whole: 9–36 lines each, 552–2,658 B, so no truncation. "ACTION line" is the HOMER-directed sentence. 19 are ACTION and 10 are INFO.

| # | Path (`AGENTS/HOMER/inbox/WALTER/`) | Added | Role/Prio | HOMER ACTION / INFO line (condensed) |
|---|---|---|---|---|
| 1 | SIG-W-20261020-001.md | 10-20 | ACTION/PRIORITY | Integrate NAR **Sept pending home sales −7.3% MoM, −11.3% YoY** (rel 10/20). The "record low" framing is INDETERMINATE |
| 2 | SIG-W-20261020-014.md | 10-20 | ACTION/PRIORITY | Integrate Census **Sept starts 1.221M SAAR** (−5.2% ±11.8, not significant), permits 1.400M. Aug revised up to 1.288M and July to 1.369M |
| 3 | SIG-W-20261020-028.md | 10-20 | ACTION/PRIORITY | Assess the dated payment-hours chart and spread-basis limits. HOMER's 221bp house spread is not a 4-week average and not MBS OAS |
| 4 | SIG-W-20261022-029.md | 10-22 | INFO/ROUTINE | **PMMS 7.32% [10/22]** vs 7.40 [10/15]. No uncrossed rung |
| 5 | SIG-W-20261022-033.md | 10-22 | INFO/ROUTINE | Unverified anecdote ("MF worst in 40 yrs"), confidence 0.3. Do not relay |
| 6 | SIG-W-20261022-042.md | 10-22 | INFO/PRIORITY | Zillow FL drawdowns from peak (Cape Coral −18.9%). CORAL owns |
| 7 | SIG-W-20261025-012.md | 10-25 | ACTION/PRIORITY | 10/22 housing executive order: conditional MI-cancellation pilot, **new originations only**. Record milestones |
| 8 | SIG-W-20261027-007.md | 10-26 | ACTION/PRIORITY | Nashville single resale −28%, and the "2.2% negative equity (Goldman)" claim. Retain basis limits |
| 9 | SIG-W-20261027-020.md | 10-26 | INFO/PRIORITY | Trepp Q3 recap: delinquent CMBS $48.65B. MF overlap, no MF rate |
| 10 | SIG-W-20261027-022.md | 10-26 | ACTION/PRIORITY | Trepp seniors-housing $2.24B maturity cohort, 95% agency, 1.75% DQ. Retain in coverage |
| 11 | SIG-W-20261027-026.md | 10-26 | INFO/PRIORITY | TX data-center permitting suit. Residential-siting context only |
| 12 | SIG-W-20261027-031.md | 10-27 | ACTION/PRIORITY | **Blackstone Blackjack MF $517.7M missed its 10/9 maturity and went to special servicing** (6 properties incl. Bradenton FL). Integrate |
| 13 | SIG-W-20261027-034.md | 10-27 | INFO/PRIORITY | Trepp $61.1B 2027 hard maturities vs Newmark $179B. Different cohorts; office-rate conflict is CREED's |
| 14 | SIG-W-20261027-035.md | 10-27 | ACTION/PRIORITY | MSCI distressed sales: **MF distress sales +62.8%**. Retain with volume/cohort limits |
| 15 | SIG-W-20261027-036.md | 10-27 | INFO/PRIORITY | Town Lane $1.9B fund close. Capital-availability counterevidence |
| 16 | SIG-W-20261027-037.md | 10-27 | INFO/PRIORITY | Sunbeam FL self-funded phases. CORAL ACTION |
| 17 | SIG-W-20261027-042.md | 10-27 | ACTION/PRIORITY | RealPage concessions 14.5% (Sept) vs Apartment List 31.3%. Different populations: **reconcile, do not splice** with HOMER's Zillow 39.6% |
| 18 | SIG-W-20261027-043.md | 10-27 | ACTION/PRIORITY | Trepp corrects its own lending-quality read. MF LTV 67.4% vs 61% ex-seasoned pool |
| 19 | SIG-W-20261027-044.md | 10-27 | ACTION/PRIORITY | Denver MF watchlist $3.83B (13.6%), 98% current, $1.32B with DSCR <1 |
| 20 | SIG-W-20261027-045.md | 10-27 | ACTION/PRIORITY | CRED iQ $136B MF maturities, 31% of balance needs $6.8B equity (modelled) |
| 21 | SIG-W-20261027-046.md | 10-27 | ACTION/PRIORITY | **UDR–Apollo JV ~$2B, close expected 10/29**: conditional. Retain the conditional status |
| 22 | SIG-W-20261027-052.md | 10-27 | INFO/PRIORITY | OZK $132.7M Culver City construction loan. OZK ACTION |
| 23 | SIG-W-20261027-056.md | 10-27 | ACTION/PRIORITY | **S2 $1.2B workouts, 12 foreclosures terminated.** Reconcile with the existing S2 coverage (STATUS:47 "S2 Capital $400M fund $0-to-LPs") |
| 24 | SIG-W-20261027-059.md | 10-27 | ACTION/PRIORITY | RAD 46-home Philadelphia auction (10/13–15). Outcome UNKNOWN |
| 25 | SIG-W-20261027-062.md | 10-27 | ACTION/PRIORITY | Treasury NPRM under the ROAD to Housing Act: **proposal**, restriction from 2027-01-07, ≥350-home definition |
| 26 | SIG-W-20261027-064.md | 10-27 | ACTION/PRIORITY | RealPage Q3: absorption ~304.8K vs completions ~318K, rent +0.9% YoY, South negative |
| 27 | SIG-W-20261027-065.md | 10-27 | ACTION/PRIORITY | Sun Belt starts −75% vs the 2022 peak is a historical comparison. Reconcile starts vs completions timing |
| 28 | SIG-W-20261027-069.md | 10-27 | INFO/PRIORITY | FL source roundup, confidence 0.45. CORAL ACTION |
| 29 | SIG-W-20261027-071.md | 10-27 | ACTION/PRIORITY | Lake Meadows investor-exit lawsuit is an allegation, not a default |

Add dates are from `git log --diff-filter=A` per file. No packet carries a deadline, but three overlap a HOMER-registered forward row or a live position:
- #1 and #2 answer `STATUS.md:131` ("does PHSI agree?") and docket rows 13 and 24.
- #4 is the A2 leg's weekly print.
- #21 has a dated close (10/29), which falls tomorrow.

---

## 2. Consumers (L4 reading-A consumer leg)

The window is the last 45 days, **2026-09-13 → 2026-10-28**. Search: `find AGENTS/<X>/inbox -type f -iname '*HOMER*'`, plus a content grep of files newer than 9/13 for `HOMER → <X>` / `From: HOMER`. The content grep found no extra packets.

| Consumer | Charter edge? | Newest HOMER packet in consumer `inbox/` | Receipt / consumption evidence | Verdict (45d) |
|---|---|---|---|---|
| **CARL** | Yes, `HOMER/CLAUDE.md:11` | `AGENTS/CARL/inbox/processed/2026-09-29_from-HOMER_3c-convergence-handle-proposed-link-to-your-V3-V7-V10.md` (9/29). 6 HOMER packets in all, Jul 31–Sep 29 | **Reply receipt:** `AGENTS/HOMER/inbox/processed/2026-10-01_from-CARL_3c-handle-confirmed-V3-rescope-at-10-05.md:1` ("CARL → HOMER · 3c handle: (a) CONFIRMED"). **Consumption in STATUS (commit 2026-10-28):** `AGENTS/CARL/STATUS.md:32-41` carries HOMER-owned FHA 11.79% Q2 and the COR-20261012-25 78.47% correction, cites `AGENTS/HOMER/STATUS.md` as canonical (:39), and gives PMMS 7.32% "HOMER owns housing grading" (:41). `:37` marks FL foreclosures STALE and says HOMER's ATTOM access is unresolved | **DEMONSTRATED** |
| **REGINALD** | Yes, `CLAUDE.md:11` | `AGENTS/REGINALD/inbox/processed/2026-09-29_from-HOMER_servicer-watch-class-A-FIRED-UWM-Fitch-B-plus-found-53-days-late.md` (9/29). Also `…2026-09-24_from-HOMER_GSE-MF-both-books-rising-Freddie-0.64-August…` (9/24) | `AGENTS/REGINALD/reports/2026-09-27_cross-bank_CRE_transmission.md:62` cites "Freddie MF 0.64% [Aug] … (HOMER, issuer primary, 9/26)", from the 9/24 packet. `AGENTS/REGINALD/reports/2026-10-07_WQ318_funding-vs-nonbank-baseline.md:12,:140` carries "HOMER 9/29 (UWM)" and "Fitch BB- → B+ (8/7)", from the 9/29 packet. ⚠️ `AGENTS/REGINALD/STATUS.md` has **0** HOMER hits. The live Path-C surface `STATUS_DASHBOARD.md:33-34` still shows the April Trepp 7.71% and the Q2 Freddie 0.51% (consumed 8/23) | **DEMONSTRATED** (reports). The dashboard currency is stale; see §7 |
| **HENRY** | Yes, `CLAUDE.md:11, :175` (wealth effect) | **None ever.** `find AGENTS/HENRY/inbox -iname '*HOMER*'` → 0 | `AGENTS/HENRY/STATUS.md` has 0 HOMER and 0 housing-figure hits (grep PMMS/NAHB/FMHPI/Case-Shiller/housing). `AGENTS/HENRY/CLAUDE.md` has 0 HOMER hits. Its only HOMER mentions are three August WALTER rows in `AGENTS/HENRY/board_log.tsv:195,232,274`. HOMER addresses HENRY by name in `NEXUS_BRIEF.md:17-24`, but nothing shows HENRY reading it | **NONE**. The edge is one-sided |
| **CORAL** | Seam partner (FL), not in the `:11` edge list | `AGENTS/CORAL/inbox/processed/2026-10-19_from-HOMER_Miami-Dade-September-condo-refresh.md` (10/19; processed in CORAL `94587cb05`, 10/21) | `AGENTS/CORAL/STATUS.md:28`: "Miami-Dade 12.3 mo (Sep) … (MIAMI REALTORS 10/16, via HOMER, re-read at primary 10/21)". `:104` coordinates with HOMER | **DEMONSTRATED** |
| **TERRY** | **No.** The charter has 0 "trade"/"TERRY" hits (`grep -c -i trade CLAUDE.md` → 0) | `AGENTS/TERRY/inbox/processed/2026-07-24_from-HOMER_servicer-bond-quote-tooling-ask.md` (7/24), the only one | `AGENTS/TERRY/setups/INDEX.md:85`: TRY-BUILDER-DHI-PHM "LAPSED 2026-07-20 … HOMER confirm unanswered … Revivable only on a direct confirmed HOMER thesis". THESIS.md was built 9/29, but **no HOMER→TERRY packet followed** | **NONE** |

**On the L4 trade leg (context for the FLEET_MAP "Next" cell):**
- HOMER has **no `TRADE.md`**.
- Its charter, `thesis/THESIS.md`, STATUS and MEMORY contain **no** trade, TERRY or "capital path" statement (grep → 0 across all four).
- The only "no book" language sits on PROME's surfaces: `PROME/GATES.tsv:21` col 5 says "Moves no capital; no position rides on HOMER's state", and `PROME/DOCKET.tsv:545` says "No capital path".
- **So reading-A cannot pass on the trade leg, and the desk has also not declared no-book-by-charter.** That half of the L4 adjudication stays open. The consumer half passes 3 of 4 charter or seam consumers (CARL, REGINALD, CORAL). HENRY fails.

---

## 3. Outbox hygiene

`AGENTS/HOMER/outbox/` holds 3 top-level packets and 2 in `delivered/`. All 5 are listed below; there are fewer than 10, so each was read in its head section (1–25 lines). The charter says `outbox/` is a record and not a delivery channel (`CLAUDE.md:11, :260`, since 2026-09-24).

| Outbox file | Date | Recipient copy? | State |
|---|---|---|---|
| `2026-09-02_to-PROME_MF-wall-retired-and-published-plus-read-cap-remediation-executed.md` | 9/02 | ✅ `PROME/inbox/processed/2026-09-02_from-HOMER_MF-wall-retired-…` | DELIVERED (copy) |
| `2026-09-14_to-REGINALD_the-GSE-MF-asymmetry-you-hold-is-GONE-…` | 9/14 | ❌ Not in REGINALD's tree under this name. Self-bannered at its line 1: "⛔ NEVER DELIVERED — found 2026-09-24", superseded by `AGENTS/REGINALD/inbox/processed/2026-09-24_from-HOMER_GSE-MF-both-books-rising-…` ✅ | NEVER DELIVERED, **remediated and labelled** |
| `2026-09-14_to-WALTER_SIG-020-ANSWERED-…` | 9/14 | ❌ Self-bannered at line 1: "NEVER DELIVERED … substance relayed in `AGENTS/WALTER/inbox/…2026-09-24_from-HOMER_SIG-015-ANSWERED-…`". That file exists at `AGENTS/WALTER/inbox/processed/` ✅ | NEVER DELIVERED, **remediated and labelled** |
| `delivered/2026-07-24_to-PROME_lane-query-amended.md` | 7/24 | ✅ `PROME/inbox/processed/2026-07-24_from-HOMER_lane-query-amended_LATE-DELIVERY-2026-07-31.md` | DELIVERED (late, labelled) |
| `delivered/2026-07-17_to-PROME_attom-h1-foreclosure-fl-worst.md` | 7/17 | ⚪ No `PROME/inbox` copy by name (`find PROME/inbox -name '2026-07-1[78]*HOMER*'` → 0). The file says "Status: DELIVERED" at its line 3. This dates from the pre-carve-out era, when PROME read outboxes | **UNVERIFIED**, historical |

**Verdict:** no new orphan since 9/24. The two known undelivered packets carry their own NEVER-DELIVERED banners and successor pointers.

---

## 4. Open DOCKET / GATES / WQ rows naming HOMER

Scan method: every `PROME/DOCKET.tsv` physical line containing HOMER (case-insensitive: L4 46 47 132 148 152 177 224 236 282 331 349 351 355 378 456 487 543 545 565 707 717 722 723 725; 850 lines). Tombstones (`hist→DOCKET_HISTORY`) are L47 and L132 and were excluded. Rows where HOMER appears only incidentally (L46, L152, L236, L282, L349, L351, L355, L378, L456, L487, L543, L707, L717, L723) are not HOMER obligations.

| Row | Date | Summary | Owner-cell / state | HOMER STATUS cites it? |
|---|---|---|---|---|
| **DOCKET L545** | 2026-11-20 | HOMER THESIS KILL RAIL, first formal grade (5 legs; both cores killed ⇒ 🔴→🟡 CANDIDATE to Will) | HOMER grades / PROME / CARL+REGINALD consumers · **PENDING** | **Yes, by content but not by `L545`.** `STATUS.md:109` (GATE-HOMER-THESIS-KILL, formal grade 11/20) and `:140` (11/20 THESIS formal grade) |
| **DOCKET L565** | next-PROME-session | Land the R3 WATCH_FOR sets. The cell's "Outstanding" list still names **HOMER** | PROME lands / owners · **PENDING** | Partly. `OBLIGATIONS_OTHERS.md:15` B8 still reads "NEW 2026-09-29 … matcher test at the 10/02 re-test". **But HOMER answered by name on 10/15** (`PROME/inbox/processed/2026-10-15_from-HOMER_R3-verdicts-by-name-and-THESIS-KILL-gate-summary-qualifiers.md` §1: 11 adopt, 3 decline with replacements). Two stale surfaces: PROME's L565 list and HOMER's B8 |
| DOCKET L725 | 2026-10-19 | HOMER wake: NAHB Oct HMI + spread recompute. Its text also lists "~10/28–30 ICE First Look Sept (C1) + GSE MF (C2)" | **RESOLVED 2026-10-20**; "source retries live on HOMER's own ledger" | Yes, `STATUS.md:12` and `SCRATCH.md:7` |
| DOCKET L722 | 2026-10-31 | HOMER full catch-up | **RESOLVED 2026-10-15** | n/a |
| DOCKET L4 · L148 · L177 · L224 · L331 | Aug–Sep | NAHB+ATTOM, GSE condo, HOM-01 decider, MF wall kill, 9/14 catch-up | All start with **RESOLVED** (L4 and L148 carry a legacy "RESOLVED · PENDING" prefix and are DISCHARGED at ㉙ 9/04) | n/a |
| **GATES `GATE-HOMER-THESIS-KILL`** (`PROME/GATES.tsv:21`) | review_by 2026-11-20 | Thesis-level kill rail mirror | **LIVE**: "owner0/5 killed; A3 0/3 … formal11/20 unchanged". The 10/15 qualifier ask ("pre-sale", "serious") was **restored** on 10/15 in col 4 | Yes (`STATUS.md:109`). ⚠️ `OBLIGATIONS_OTHERS.md:17` cites "GATES.tsv:26", but the row is now at line **21** (stale line pointer) |
| WQ-436 (`PROME/WILL_QUEUE.md:172`) | 10/15 | HOMER/SAM/ORACLE crash-recovery spawns | **RULED** 10/15 ("okay approved both") | n/a |
| WQ-413 (`WILL_QUEUE.md:169`) | 10/15 | Wake dark desks; HOMER mentioned as already in L722 | **RULED DECLINE** | n/a |

**Gap:** no PROME DOCKET row wakes HOMER between L725 (resolved 10/20) and L545 (11/20). See §7 R1.

---

## 5. Card / review / profile reconciliation

Evidence is at `AGENTS/HOMER/` unless stated.

### 5a. `upgrades/HOMER_CARD.md` work queue

| Item | Status now | Evidence |
|---|---|---|
| 1a Cure Rates comparator | **CLOSED** 8/22 | `CLAUDE.md:99` (`<-15/-30/-40%`), `:117` "fixed 2026-08-22 from `>`" |
| 1b dangling `(see Open Items)` | **CLOSED** | `grep -n 'see Open' CLAUDE.md` → 0 |
| 1c SENDING above VIEW | **SUPERSEDED → CLOSED by NEXUS** | NEXUS amendment 12 accepted (`inbox/processed/2026-09-02_from-NEXUS_your-ordering-defect-is-ACCEPTED-and-shipped-as-amendment-12-plus-a-schema-CAP.md`). Brief now has `## CROSS-DOMAIN` at `NEXUS_BRIEF.md:11`, **before** `## VIEW` at `:41` |
| 1d FMHPI trough + CRL-06 claim | **CLOSED** | `CLAUDE.md:276` CRL-06 "RESOLVED CONFIRMED at CARL 2026-07-16". "Jan +0.9" has 0 hits in CLAUDE.md and NEXUS_BRIEF.md |
| 1e `Resolve_By` | **CLOSED** 2026-08-23 | `thesis/PREDICTIONS.tsv:2` header ends `Resolve_By`. Added in `0ab1f63cc` (`git log -S`) |
| 2a STATUS byte tier / line cap | **CLOSED** | `CLAUDE.md:211-215, :238` (soft 22,785 / hard 32,550 B). STATUS is 22,157 B = **68%** of budget (`read_cap_check` receipt) |
| 2b REGINALD band cross | **CLOSED** 8/22 | `AGENTS/REGINALD/STATUS_DASHBOARD.md:34` "BAND CROSSED — CONSUMED 2026-08-23 (HOMER packet 8/22)" |
| 2c Boot docket `awk` | **CLOSED** | `CLAUDE.md:194-195`, boot step 5 runs the enumerate `awk` |
| 2d Register 9/4 kill | **CLOSED** 8/22 | DOCKET L224 RESOLVED 9/02 |
| 2e Trepp-MF standing fix off SCRATCH | **CLOSED** | `CLAUDE.md:28` "STANDING READ RULE — TREPP DISPATCHES" (charter, durable). I did not trace the closing commit |
| 3a A–G servicer spec durable home | **CLOSED** 8/23 | `docket/CATALYSTS.tsv:3` standing row (the card's ":11" moved after the 9/29 archive), printed by the boot `awk`. ⚠️ Still 0 hits for "Servicer Watch"/"A–G" in `CLAUDE.md`. The home is durable and read through the docket, not the charter |
| 3b THESIS + kill rail | **CLOSED** 2026-09-29 | `thesis/THESIS.md` added in `74089ab84` ("thesis + thesis-level kill rail built (L3 3b)") |
| 3c Convergence handle | **CLOSED-VERIFIED** (PR8, 10/21) | `HOMER_CARD.md:1,77`. CARL confirmation at `inbox/processed/2026-10-01_from-CARL_3c-handle-confirmed…:1`. `THESIS.md:190` says the §8a handle trigger is met and re-scoring waits for 11/20 |
| 3d FL basis template on the other 11 threshold rows | **PARTIAL** | `:83` is now the National FC STARTS band, **RE-ARMED 2026-09-29** (`CLAUDE.md:119`). Rent breadth was re-armed 9/29 (`STATUS.md:48`). **A full 11-row basis audit is NOT done by this reader** (C1 cluster) |
| T4 MEMORY.md unread + false CREED fact | **PARTIAL** | The fact is corrected: `MEMORY.md:23` "checked 2026-09-29 — the July note … is superseded". MEMORY is still not a boot step (boot steps 2–4 = STATUS/SCRATCH/LESSONS, `CLAUDE.md:191-193`; FILES only at `:242`) |
| T4 `reports/` absent from FILES | **CLOSED** | `CLAUDE.md:256` |
| T4 `domain/` empty, unlisted | **CLOSED** | Directory absent (`ls domain` → no such file) |
| T4 filename-as-state on a DRAFT report | **OPEN** (cosmetic) | `reports/2026-08-13_servicer-watch-respec-DRAFT-for-ratification.md` and `reports/2026-08-23_non-funding-leverage-RIDER-DRAFT-for-ratification.md` keep the DRAFT names, although the rider was ENCODED 9/29 (`docket/CATALYSTS.tsv:18`) |
| T4 no version / last-amended field in charter | **OPEN** | `grep -i 'version\|last.amended\|Last Updated' CLAUDE.md` → 0 |
| T4 NEXUS fold-ordering check degenerate | **UNVERIFIED** | The rule survives at `CLAUDE.md:226`. I did not re-walk git history |
| T4 undated ICE 280K on the brief | **CLOSED** (by rotation) | `grep 280K NEXUS_BRIEF.md STATUS.md` → 0 |
| Cross-cutting: boot step 2 names an unreachable BOTTOM LINE | **CLOSED by size** | `CLAUDE.md:191` unchanged wording, but STATUS is 22,157 B (under budget) and the BOTTOM LINE sits at `STATUS.md:158-164` |
| PR6/WQ-256 b dead Trepp courier on the brief | **CLOSED** | `grep courier NEXUS_BRIEF.md` → 0 |

### 5b. 8/22 review findings (🔴/🟠)

| Finding | Status | Evidence |
|---|---|---|
| 1 🔴 HOM-01 clause collision | **CLOSED** | Ruled `422f9505f`. HOM-01 CLOSED MISSED (early-kill) 8/31, DOCKET L177. `STATUS.md:150` |
| 2 🔴 Delivery truncation (STATUS, brief) | **CLOSED** | STATUS 68% and brief 41% of budget (`read_cap_check`, rc 0). CROSS-DOMAIN is the first section |
| 3 🔴 A–G spec no durable home | **CLOSED** | `docket/CATALYSTS.tsv:3` (see 3a) |
| 4 🟠 REGINALD never told of the band cross | **CLOSED** | See 2b |
| 5 🟠 Threshold rail 3 broken / 7 basis | **PARTIAL** | Cure Rates fixed. `:83` re-armed with a basis. Remaining basis rows not verified here (C1) |
| 6 🟠 Smaller (CRL-06, Open Items, trough, stale rows) | **CLOSED** for the verified items | See 1b/1d. The stale dashboard rows were superseded by the 9/14 rotation (not verified row-by-row) |

### 5c. `profiles/HOMER.md` §"Owner-lane flags (ranked)" (8/07)

| Flag | Status | Evidence |
|---|---|---|
| 🔴 CORAL lock 8.9 vs 8.1 | **CLOSED / SUPERSEDED** | Profile banner at `:10-12`. HOMER now publishes **no** statewide FL figure (`STATUS.md:89`; FL condo row at `:93`, "withheld pending owner reconcile") |
| 🔴 NEXUS_BRIEF "94% multifamily" | **CLOSED** | Profile `:10`. `STATUS.md:47` reads 95.8% |
| 🔴 Five `Next:` dates passed (PAT-089) | The original five are **CLOSED**. **The class has RECURRED and is OPEN** | 13+ unresolved `docket/CATALYSTS.tsv` rows have passed dates since the 10/19 closeout: r13 NRC 10/20 · r24 PHSI 10/20 · r28 PHM 10/22 · r31 NVR ~10/21–23 · r5 PMMS 10/22 · r43 Redfin ~10/22 · r11 ICE First Look ~10/22–28 · r20 GSE MF Sept ~10/23–30 · r14 NHS 10/27 · r16 Case-Shiller ~10/27 · r30 MTH 10/28 · r40 BEA Q3 ~late Oct · r29 DHI 10/29 (tomorrow). Receipt: the boot `awk`, read-only |
| 🟠 SCRATCH:27 superseded bands | **CLOSED** | Profile `:10-11`. SCRATCH has been rewritten (3,908 B, 10/19) |
| 🟠 3 inbox packets unprocessed | The original three are **CLOSED**. **The class has RECURRED and is OPEN** | 29 unprocessed in `inbox/WALTER/` (§1) |
| 🟡 SCHEMA rows RATES/PRICING | **CLOSED** 10/19 | `workbook/SCHEMA.tsv` has 8 RATES and 8 PRICING rows. `SCRATCH.md:9` "SCHEMA now covers KB_LIVE/RATES/PRICING". ⚠️ New: `workbook/RENT_BREADTH_ROSTER.tsv` has **0** SCHEMA rows (it may be a roster, not a ledger; low confidence) |
| 🟡 No Reports-to / Spawnable-by header | **OPEN** | `CLAUDE.md:11` has only "Standing peer edges (not 'reports to')" |
| 🟡 $160B+ MF-wall re-source owed to CREED | **CLOSED** 9/02 | DOCKET L224 RESOLVED. `reports/2026-09-02_MF-maturity-wall-RETIREMENT-published.md`. `STATUS.md:54` kill-on-sight |
| 🟡 Amendment-10 ack | **UNVERIFIED** | Not checked by this reader |

---

## 6. Reports

`AGENTS/HOMER/reports/` holds 19 `.md` files plus 5 evidence directories. Dates are the last commit (`git log -1 -- <file>`).

| File | Last commit | Bytes |
|---|---|---|
| 2026-07-12_CRL-06-data-package.md | 07-12 `3c1903350` | 7,025 |
| 2026-07-12_FL-condo-reconciliation-package.md | 07-12 | 8,016 |
| 2026-07-12_domain-sweep.md | 07-12 | 11,995 |
| 2026-07-24_HOM-01-grading-sheet.md | 08-31 `56f4f2638` | 7,573 |
| 2026-08-13_servicer-watch-respec-DRAFT-for-ratification.md | 08-22 | 23,450 |
| 2026-08-14_issuer-primary-sourcing-convention-PROPOSAL.md | 08-14 | 5,001 |
| 2026-08-14_servicer-thresholds-BASE-RATING-partial.md | 08-14 | 26,238 |
| 2026-08-22_servicer-thresholds-ANCHORING-PROPOSAL.md | 08-22 | 13,059 |
| 2026-08-23_builder-rate-buydown-transcript-ASSESSMENT.md | 08-23 | 8,710 |
| 2026-08-23_non-funding-leverage-RIDER-DRAFT-for-ratification.md | 09-29 | 10,102 |
| 2026-08-23_refresh-plan-AND-EXECUTION-RECORD.md | 08-23 | 6,221 |
| 2026-09-02_MF-maturity-wall-RETIREMENT-published.md | 09-02 | 10,492 |
| 2026-09-14_three-week-catchup-release-ledger.md | 09-14 | 8,450 |
| 2026-09-29_A3-rent-growth-band-RETUNE-research.md | 09-29 | 16,095 |
| 2026-09-29_A4-national-FC-starts-band-RETUNE-research.md | 09-29 | 20,740 |
| 2026-09-29_PMMS-2026-10-01_PRE-REGISTRATION.md | 09-29 | 3,155 |
| 2026-10-19_morning-L725.md | 10-19 `2556731f0` | 12,006 |
| 2026-10-19_domain-news-sweep.md | 10-19 `4c8a8f6c6` | 17,794 |
| 2026-10-19_documentation-audit.md | 10-19 `4c8a8f6c6` | 5,886 |
| dirs: 2026-09-29_A3_evidence (5) · 2026-09-29_A4_evidence (5) · 2026-10-15_catchup_evidence (5) · 2026-10-19_morning_evidence (12) · 2026-10-19_sweep_evidence (21) | | |

**Newest substantive owner report:** `reports/2026-10-19_domain-news-sweep.md`, 126 lines. I read lines 1–40 whole and grepped 41–126. Its headline:
- *"The strongest addition is pressure among loans that are still paying"*: Trepp's 10/16 2021–22-vintage MF CRE CLO cohort (93 loans, $3.95B) holds 12.2% of balance but 80.2% of delinquency. **93.8% of performing balance with reported coverage is below 1.0x DSCR.**
- It is counterweighted by stronger rental demand and positive rent growth. The report also flags a Trepp-vs-Freddie perimeter conflict (0.80% vs issuer 0.64%) and says do not splice.
- Kill counts are unchanged.

**November 20 frozen scoring cadence: STATED on 6 surfaces.**
- `thesis/THESIS.md:89` ("Formal grade dates: 2026-11-20 …"), `:137` (V5: 11/20 can return only NOT FIRED/UNGRADED on core legs), `:190` (§8a handle re-scores at 11/20).
- `reports/2026-10-19_morning-L725.md:38` ("Formal review 11/20 unchanged; 19/25 handle unchanged").
- `reports/2026-10-19_domain-news-sweep.md:112` ("thesis 0/5 killed, handle 19/25, review November 20").
- `docket/CATALYSTS.tsv:37` ("2026-11-20 — FORMAL GRADE … then 2027-02-20").
- Mirrored at `PROME/GATES.tsv:21` col 12 and `PROME/DOCKET.tsv:545`.

---

## 7. Routing candidates (ranked)

| # | Sev | Finding | Owner | Evidence | Where I may be wrong |
|---|---|---|---|---|---|
| R1 | 🔴 | **Dark-desk intake backlog with no wake rail.** 29 WALTER packets are unprocessed and unlogged: 19 ACTION, oldest 8d, three bearing on registered forward rows. Thirteen-plus `CATALYSTS.tsv` dated rows have passed since the 10/19 closeout. This includes the two C1/C2 resolver inputs that L725 itself named (ICE First Look Sept, GSE MF Sept). **No PROME DOCKET row wakes HOMER between L725 (resolved 10/20) and L545 (11/20).** It is the PAT-089 / uniformly-idle-desk class from the 8/07 profile, recurring | **PROME** (wake/spawn decision), then HOMER (drain) | §1 table. `CLAUDE.md:205` loop → 29 UNLOGGED. §5c row 3. DOCKET scan §4 | (a) The 11/20 formal grade **cannot** return FALSIFIED/PARTIAL on core legs (`THESIS.md:137`). So the decision-relevant cost before 11/20 is lower than the count suggests, and an owner may judge "drain at the 11/20 session" acceptable. (b) PROME may hold a wake in a surface I did not read (SCRATCH/ORCH_LOG); I read DOCKET, GATES and the WQ grep only. (c) WALTER's BOARD may already carry these signals to consumers, so HOMER's lag may not block CARL/REGINALD. **I would downgrade to 🟠 if PROME shows a dated wake before ~11/13 (MBA Q3 NDS, the HOM-02 decider)** |
| R2 | 🟠 | **L4 trade leg has no surface on HOMER's side.** No `TRADE.md`. 0 trade/TERRY/capital-path statements in the charter, THESIS, STATUS or MEMORY. The "no capital path" wording lives only on PROME rows. TERRY's lapsed builder setup is "revivable only on a direct confirmed HOMER thesis" (`TERRY/setups/INDEX.md:85`). The thesis now exists (9/29), but no HOMER→TERRY packet has followed | HOMER + Will (declare no-book-by-charter, or route the thesis to TERRY); DAEDALUS adjudicates L4 | §2 trade-leg note | TERRY may consume HOMER through RED/CARL rather than directly, and a no-book stance may be ruled somewhere outside my cluster (roster or PROME proposals). Not checked |
| R3 | 🟠 | **HENRY edge is one-sided.** HOMER's charter names HENRY as a standing consumer (`CLAUDE.md:11, :175`) and addresses it in `NEXUS_BRIEF.md:17-24`. HENRY's charter and STATUS have **0** HOMER hits, and no HOMER packet has ever reached HENRY's inbox | HOMER (edge claim) / HENRY (read path), via PROME | §2 HENRY row | HENRY may read peer briefs through a NEXUS digest rather than by name. I grepped HENRY's charter, STATUS and inbox only, not NEXUS's tree |
| R4 | 🟡 | **REGINALD's live Path-C dashboard is stale against HOMER's figures.** `STATUS_DASHBOARD.md:33` shows Trepp MF 7.71% (Apr) vs HOMER 8.04% Sept. `:34` shows Freddie 0.51% (Q2) vs HOMER 0.64% Aug. The newer figures reached REGINALD's reports (9/27, 10/07) but not its dashboard | REGINALD (consumer-side currency); packet, not an edit | §2 REGINALD row | The dashboard may be a FROZEN or secondary surface. I did not read its header |
| R5 | 🟡 | **R3 WATCH_FOR registrar lag on both sides.** PROME DOCKET L565 still lists HOMER as "Outstanding", although HOMER answered by name on 10/15. HOMER's `OBLIGATIONS_OTHERS.md:15` B8 still reads as pending from 9/29. `OBLIGATIONS_OTHERS.md:17` points at `GATES.tsv:26`; the row is at :21 | PROME (L565 write-back) · HOMER (B8, line pointer) | §4 | PROME may have landed HOMER's set in `~/Research-Intake` without updating the cell. I did not read the intake config |
| R6 | 🟡 | **Card residue.** DRAFT-named reports after ratification. No charter version field. No Reports-to/Spawnable-by header. MEMORY.md not boot-read. `RENT_BREADTH_ROSTER.tsv` has no SCHEMA rows. `LESSONS.md` is at 73% of budget with **502 B** to the 75% rotation trigger (`read_cap_check`). The charter is 38,671 B, 119% of budget, "OUT OF PERIMETER by rule 20 … injection UNCONFIRMED" | HOMER (cosmetic; charter items Will-gated) | §5a T4, §5c | The charter size is advisory under rule 20, not a breach, and the profile synthesis should decide whether it matters |
| R7 | 🟡 | **board_log vocabulary drift at the runtime switch.** Rows ≤89 use `acted/noted/info-only` with `YYYY-MM-DDTHH:MMZ`. Rows 90–97 (10/19, "HOMER (orch)", Codex/OpenAI per `SCRATCH.md:3`) use `ACTIONED/INFO-LOGGED` and microsecond ISO stamps. The membership test is unaffected because it greps the ID | HOMER | `board_log.tsv` last 20 rows | It may be intentional canonical-token adoption (STATE_VOCABULARY). I did not check which form is canonical |

---

## 8. Not read / coverage limits

| Surface | Coverage | Ranges |
|---|---|---|
| `profiles/HOMER.md` | **Whole** | 1–67 |
| `upgrades/HOMER_CARD.md` | **Whole** | 1–124 |
| `upgrades/HOMER_REVIEW_2026-08-22.md` | **Whole** | 1–130, 131–237 |
| `upgrades/HOMER_REVIEW_2026-08-22_READER_REPORTS.md` | **Route lists only**, per brief | heading map; 85–96, 193–209, 329–354, 430–440. **Not read:** 1–84, 97–192, 210–328, 355–429, 441–499 |
| `FLEET_MAP.tsv` HOMER row | Whole row | grep |
| `inbox/WALTER/*.md` (29 unprocessed) | **Whole, every file** | all lines, 9–36 per file |
| `inbox/processed/`, `inbox/WALTER/processed/` | Listing + counts; **one** packet read (CARL 10/01, lines 1–8) | Bodies are processed and were excluded by the brief |
| `outbox/` (5) | Head sections | lines 1–25 each; bodies past 25 not read |
| `board_log.tsv` | Header + last 20 rows (78–97), notes cut at 160 chars; ID membership grep over the whole file | rows 2–77 not read |
| `archive/` | Listing + `CATALYSTS_RESOLVED_2026-09.README.md` whole (1–19) | No other archive file opened |
| `reports/` | Listing + dates. `2026-10-19_domain-news-sweep.md` lines 1–40 whole, 41–126 by grep only. `morning-L725.md` grep only | 17 other reports and 5 evidence dirs not opened |
| `STATUS.md` (HOMER) | **Whole**, lines cut at 900 chars | 1–60, 61–164 |
| `CLAUDE.md` (HOMER) | **Targeted only**: 1–12, 188–200, plus greps | Not read whole. The charter belongs to the C1 reader |
| `thesis/THESIS.md`, `PREDICTIONS.tsv`, `MEMORY.md`, `OBLIGATIONS_OTHERS.md`, `SCRATCH.md`, `NEXUS_BRIEF.md`, `docket/CATALYSTS.tsv`, `workbook/SCHEMA.tsv` | grep / head only (SCRATCH 1–15, NEXUS_BRIEF 1–12 + headings, CATALYSTS by boot `awk`) | Not read whole |
| `PROME/DOCKET.tsv` | Every HOMER-matching line classified. Full cells read for L4, L148, L545, L725; L46, L378, L565, L723 by HOMER-context grep | Other 825 lines not read |
| `PROME/GATES.tsv` | Header + row 21 whole | Other rows not read |
| `PROME/WILL_QUEUE.md` | `grep -n HOMER` (2 hits) + context | Not read whole |
| Consumer trees | Inbox filename finds and content grep (newer than 9/13). STATUS greps for CARL, REGINALD, HENRY, CORAL, TERRY. Targeted greps of REGINALD reports/dashboard, HENRY charter/board_log, TERRY `setups/INDEX.md` | No consumer file read whole. NEXUS's tree not checked for HENRY brief consumption |
| **Not done** | Blueprint conformance. The threshold-rail 11-row basis audit (C1). Amendment-10 ack. Fold-ordering history walk. Commit that closed 2e. PROME SCRATCH/ORCH_LOG for a HOMER wake. Research-Intake config for the landed R3 set | |

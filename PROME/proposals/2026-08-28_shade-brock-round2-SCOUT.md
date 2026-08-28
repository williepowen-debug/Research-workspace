# SHADE / BROCK round-2 scout reports — raw material for the additional-objectives list
**Produced:** 2026-08-28 ~18:1x–18:2x ET by two PROME read-only Explore clerks (`scout-shade-tasks`, `scout-brock-tasks`); Will's ask verbatim: *"Read through some of BROCK and SHADE and develope a list of additional tasks or objectives we can have these two work on."* PROME's ranked synthesis = the chat presentation + SCRATCH item 10. ⚠️ Read while `shade-0828` / `brock-0828` were live and rotating files — line numbers are from the 8/13-vintage live files.

## SHADE (scout report, verbatim)
**Mid-edit note:** `AGENTS/SHADE/archive/{STATUS,SCRATCH,MEMORY}_PRE-ROTATION_2026-08-28.md` exist as untracked files (STATUS copy 126,272 B, 7-line crc banner), but live `STATUS.md`/`SCRATCH.md`/`MEMORY.md` are still byte-identical to 8/13 at scout time. Rotation staged, not applied.

**Vitals:** last real session 2026-08-13 ~21:50 ET. No `workbook/`, no `PREDICTIONS.tsv`, no CATALYSTS/docket. `board_log.tsv` = 78 rows, last `2026-08-13T21:45Z`. Inbox: 15 in `inbox/WALTER/`, 2 in `inbox/` root, all unconsumed. `corrections_boot_check.py SHADE` = **rc 1 BLOCK** (`COR-20260828-03` unreceipted).

### A. Charter-vs-STATUS coverage gaps
| Charter item (`AGENTS/SHADE/CLAUDE.md`) | Dated current reading? |
|---|---|
| Key Ratio #1 Affiliated Reinsurance (L33) | ❌ never computed; STATUS:198 re-labels inputs "self-reported/unverified-by-construction" after the 5.1× DLIC failure |
| #2 Illiquidity Ratio >30% (L34) | ❌ absent from STATUS entirely |
| #3 Capital Leakage / $4.78B intercompany notes (L35, L44) | ❌ static from charter; no dated pull |
| #4 TSR / Gober (L36) | ❌ absent from STATUS entirely |
| #5 FABN spread (L37) | ✅ +33.0bp L4L, T+110, 8/13 — STATUS:354 |
| HY OAS bands 300/350 (L58) | ⚠️ last pull = 8/12 print (STATUS:411), 15d; never reconciled with the `>280`/5-session trigger |
| NAIC SVO overrides <5/5-20/>20 (L61) | ❌ no count ever recorded — STATUS:258 says only "Monitor". Untrippable threshold |
| APO $120/$100 (L62) | ❌ declared "stale tape level" 6/21 (STATUS:293), never re-based |
| AG 55 filings (L60) | ⚠️ 2026-reporting L3/PIK/private-letter-rating mandate flagged to PROME 8/13, NAIC primary text NOT pulled (STATUS:495) — kill-path #2's basis |
| Egan-Jones kill-path 3 (L51) | ✅ resolved 8/12, ladder 🟢 (STATUS:383-391) |

### B. Open threads / owed / deferred (owner's own words)
| Item | Source | State |
|---|---|---|
| "STATUS COMPRESSION — #1, ahead of everything below" (492 vs ~250 cap) | SCRATCH:37 · STATUS:492 · MAINTENANCE:130 | undone 15d |
| "Apollo Q2 10-Q Retirement Services segment — the registered leg-2 cross-check, not run" | SCRATCH:44 · STATUS:381 | outstanding |
| W1(b) "read AARe Note 14… document already on disk — 268,680 chars, Notes 2/5/14 fetched and unread" | SCRATCH:39 | due 9/30 |
| W1(a) three gated US routes (NAIC InsData · state-DOI · AM Best–CapIQ) | SCRATCH:38 | due 9/30 |
| Obligation ② canonical registration of `>280`/5-session — "no locus in CLAUDE.md… the 7/9 registration is unlocated" | STATUS:481 · SCRATCH:40 | due "next session" — 15d overdue |
| "NPORT-P 6/30 window (~late Aug)" rerun of `research/FABN_PEER_SPREAD_NPORT_2026-07-27.py` | SCRATCH:48 | window is NOW |
| `PREDICTIONS.tsv` w/ confidences at registration + standing FIRED-triad table | STATUS:321-322 · `AGENTS/DAEDALUS/FLEET_MAP.tsv:16` | 🔴 OPEN since 7/27 |
| Supply-adjusted canary: bands only at ≥4 quarters; first graded read Q3 | `instruments/FABN_SUPPLY_ADJUSTED_CANARY_SPEC_2026-08-13.md` · STATUS:437-440 | registered, ungraded |
| Granato & Drall paper "unread"; Lee Robinson $1.8T "no primary sourcing yet" | STATUS:285 · STATUS:206 | open since 7/27, 6/26 |
| Clear Spring Life statutory · Barbco "former affiliate" · Nautilus (Barbados) modco | STATUS:235 ①–④ · SCRATCH:179 | open |

### C. Past-date / unresolved
| Date | Item | Path |
|---|---|---|
| 2026-06-23 | NAIC RBC IRE WG webex — "PASSED 16d ago, UNGRADED" | STATUS:244 (now 66d) |
| 2026-07-06 | NAIC CLO C-1 Residuals/PAF comment close — "PASSED 3d ago, UNGRADED" | STATUS:245 (now 53d) |
| ~late Aug | NPORT-P 6/30 rerun | SCRATCH:48 |
| 2026-08-31 | BCRED Q3 tender EXPIRES, owner BROCK/SHADE | `PROME/DOCKET.tsv:195` |
| ~mid-Sept | MBA Q2 → `PRED-006` + joint verdict w/ `PRED-CREED-010` | STATUS:257 |
| 2026-09-30 | FORUM-5 W1 (SHADE owns 2 of 4 legs) | `PROME/DOCKET.tsv:182` |
| 11-18 / 11-30 / 11-05..18 | C2 self-exec · W3 · Q3 deferral cluster | DOCKET:184, 183, 185 |

### D. Fleet asks unanswered on SHADE's surfaces
| Ask | Date | Evidence |
|---|---|---|
| Rule-6b doorbell (Delaware Life chain) | 8/28 | `PROME/inbox/processed/2026-08-28_from-WALTER_doorbell-…md` |
| `SIG-W-20260828-041` Truist + Fifth Third PAUSED selling Delaware Life (ACTION, conf 0.85) | 8/28 | `AGENTS/SHADE/inbox/WALTER/…-041…md:17,50` |
| `SIG-W-20260826-004` TWG "there has been no fraud" — vector-1 update (ACTION) | 8/26 | `inbox/WALTER/` |
| `SIG-W-20260819-028` OBDC PIK = 1.1% of statutory surplus — "To: SHADE (action)" | 8/19 | `inbox/WALTER/…-028…md:3` |
| DAEDALUS P1 read-cap — STATUS 231% of cap, SCRATCH 94%, MEMORY 66% | 8/28 | `inbox/2026-08-28_from-DAEDALUS_P1-read-cap…` (scout re-ran `read_cap_check.py --agent SHADE`, confirms) |
| DAEDALUS SFG sweep — 3 defects in the NPORT script (unstamped curve backfill · partial-curve interpolation · silent page truncation); fix BEFORE rerun | 8/17 | `inbox/2026-08-17_from-DAEDALUS_sfg-sweep…` |
| `corrections_boot_check.py SHADE` = rc 1 BLOCK, `COR-20260828-03` unreceipted | 8/28 | ran live |

`PROME/GATES.tsv`: zero SHADE rows. `HEARTBEAT.md`: zero SHADE-owner rows.

### E. Structural debts
`domain/sources/01–08` (8 files, 222 KB) all stamped `LAST_REVIEWED: 2026-03` — ~150d stale, flagged at STATUS:8 since 6/26, still the charter's named Source Documents (CLAUDE.md:119). `OPEN_THREADS_2026-07-09.md` and `ARCH_REPORT_2026-06-26.md` >60d, unreferenced → step-10a candidates. `LAST_COMPLETION.md` self-declared legacy. Newest `research/` file = 8/13.

**Live positions:** `FORGE/STATUS.md:95` — APO $95P Dec-18 ×1, mark 0.05, −99.58%, "BROCK thesis vehicle"; D-21 caveat `FORGE/STATUS.md:153`. No ATH/Athene/FABN/insurer positions. Tension: charter L62 makes APO a monitored threshold while MEMORY.md:34 says "APO price is not a SHADE stress gauge."

### F. Scout's top 8 (ranked)
1. Drain the 17-item inbox + work the Delaware Life escalation (vector #1 FIRING; forced-seller / remediation leg) — STATUS:197, :254.
2. Receipt `COR-20260828-03` + execute the read-cap rotation (clears the rc=1 boot block).
3. Fix the 3 NPORT-script defects, then rerun the 6/30 window — SCRATCH:48; DAEDALUS 8/17; STATUS:406.
4. Canonical registration of the `>280`/5-session trigger — 15d overdue; blocks the X1≡wrapper-decoupling reconcile — STATUS:481; SCRATCH:40.
5. W1 leg (b): AARe Note 14 — on disk, unread; expected result pre-stated — SCRATCH:39; DOCKET:182.
6. Pull the AG 55 NAIC primary text — kill-path #2's basis — STATUS:495; charter L50.
7. Seed `PREDICTIONS.tsv` + FIRED-triad table — STATUS:321-322; SCRATCH:49; FLEET_MAP:16.
8. Apollo Q2 10-Q Retirement Services cross-check — the registered leg-2 cross-check, never run — STATUS:381; SCRATCH:44.

*Timing flag: BCRED tender expires Mon 8/31; `PROME/DOCKET.tsv:195` names BROCK/SHADE jointly.*

## BROCK (scout report, verbatim)
**Live rotation in flight at scout time:** `archive/STATUS_PRE_ROTATION_2026-08-28.md` exists (byte-identical 90,609 B copy of the 8/13 STATUS); live STATUS still stamped 8/13. BROCK dark 15d.

### A. Charter-vs-STATUS coverage gaps
| Charter requirement (`AGENTS/BROCK/CLAUDE.md`) | STATUS state | Age |
|---|---|---|
| Convergence matrix w/ per-vector "Last Updated" | STATUS.md:139 header admits "current col carried through 6/20"; 9 of 14 vectors last rescored 6/4–6/28, 4 at 7/27, ZERO in August; 59/70 frozen since 7/27 (STATUS.md:168) | 62–85d |
| REGIME BLOCK "update every session" | STATUS.md:68-73 — lines dated 6/20, 6/26, 7/4, 7/27; line 4 itself says median NAV discount "78d stale" | 32–69d |
| EXIT RULES §1 Thesis Kill (HY<260 for 10+ sessions) | STATUS.md:176 cites 279 [7/24]; ladder STATUS.md:228-229 cites 271 [8/12]; NEXUS packet says 263 [8/27]. Three HY values, one file + one unread packet | 15–35d |
| EXIT RULES §2 APO $130 | FIRED 8/12, HOLD ruled 8/13 (STATUS.md:209); mark "mid ~$0.75" [8/13] vs `FORGE/STATUS.md:95` "$0.05 / −99.58%" [8/14] | contradicted |
| SIGNAL DASHBOARD | STATUS.md:109 stamped 6/15 | 74d |
| LIVE TAPE | STATUS.md:43 — 8/13 intraday, explicitly "not closes" | 15d |
| §4 Time-Based "review all predictions quarterly" | last disposition pass 8/13; BRK-27 unresolved 59d | — |

### B. Open threads / owed (owner's own words, `AGENTS/BROCK/SCRATCH.md`)
| # | Item | Line |
|---|---|---|
| 1 | "READ THE BCRED Q2 10-Q… FETCHED 2026-08-13, UNREAD" — "largest single un-graded document on my board" | :10, :49 |
| 3 | PC register CCLFX demand ~17.0 — "source field names a DOCUMENT, not a LINE ITEM" | :52 |
| 4 | 4th-public-div-cut trigger: RED's reframe accepted, "re-base or retire is OWED" (since 8/7) | :53 |
| 5 | VX-BRK-023 (OTF litigation) STUCK, re-spec "scheduled after 8/7" | :54 |
| 6 | 8/6 MFIC + FSK call transcripts never pulled — "NAMED GAP, open" | :55 |
| 7 | BRK-32 `oversubscribed := pct_repurchased > cap` fix — sent, awaiting RED | :56 |
| — | ASIF → `workbook/PC_REDEMPTION_REGISTER.tsv` as 6th expression point ("NEXT SESSION"); ASIF/BRK-30 membership = DRAFT ONLY, Will-gated | :17-18 |
| — | W1 no-print DENOMINATOR due 9/30 ("RUN NEXT SESSION") · W2 standing · W3 11/30 · X1 reconcile BLOCKED on SHADE | :32-35 |
| — | Auto-memory `finding_internal_vs_external_instrument_defect` FLAGGED, NOT WRITTEN | :26 |
| — | Cliffwater CDLI Q1 NAV "genuinely open, carried since June" | :40 |
| — | Tier-3 row says BANK_BDC_MATRIX "freeze-vs-refresh owner call still not made" — file now carries a FROZEN 7/4 banner ⇒ stale row | :83 |

### C. Predictions past date / calendar now past
| Item | Date | State |
|---|---|---|
| BRK-27 | resolve 2026-06-30 | PARTIAL / "⚠️ MIXED" — 59d past, never final-dispositioned (`workbook/PREDICTIONS.tsv:20`) |
| BRK-06 | 12/31 | PARTIAL, no re-arm note (PREDICTIONS.tsv:4) |
| BCRED Q2 final satisfaction window 8/13-8/17 | past | ungraded (`docket/CATALYSTS.tsv` row 2026-08-14) |
| First Brands Q2 10-Q exposure refresh — PROME-assigned 8/3 | window 8/10-8/14 | past; AND confirmation DENIED 8/24, all debtors → Ch.7 |
| MFIC Q2 (`PROME/DOCKET.tsv:116`) · CCLFX GATE-BRK-C1 (DOCKET:118) | 8/6, 8/7 | rows still PENDING though STATUS.md:29 graded C1 🟠 on 8/7 — mirror lag |
| BCRED tender expiry · BRK-14 capex verify | 8/31 | 3 days out (DOCKET:195) |
| CRMT waiver expiry | CATALYSTS.tsv says 2026-09-01; DOCKET:189 hardened to 2026-09-07 | date conflict |
| Open, not past: BRK-02 9/30 · BRK-30 10/15 · BRK-32 11/30 | — | 16 live rows total |

### D. Fleet asks unanswered — 12 top-level + 26 WALTER = 38 unprocessed; board_log last row 2026-08-13
| From | Date | Ask |
|---|---|---|
| NEXUS | 8/28 | HY 263 [FRED 8/27], 5 of last 6 sessions <270 — "your registered re-eval is triggered… yours to run"; brief = fleet's stalest |
| DAEDALUS | 8/28 + CORRECTION | P1 read-cap RULED: STATUS 90,609 B = 167% of cap |
| LIQUID | 8/23 | BDC Q2 card graded CONFIRM, contradicts BROCK's 7/27 verdict — "a refusal with a reason is a valid answer; silence is not" |
| RED | 8/27 | confirm-or-supersede Bain CLO first rated default + BCRED gate state |
| DEWEY | 8/27 | CRMT covenant-expiry decision tree (9/7 arms three levers) |
| REGINALD | 8/20 | First Brands recovery rate vs its pre-registered 40% line — one number or "never established" |
| HANS | 8/28c, 8/28e | EU private credit ruled HANS's at full depth; accept-or-decline the HANS-T-14 fire routing |
| VULCAN | 8/21 | CORRECTION — NVDA/OpenAI $105bn IS filed |
| PROME | 8/27 | INFO cc — CREED T-06b FIRED (SREIT fund gate), no clock |
| DOCKET:232 | by 9/15 | X1 WRAPPER-HALF CONTEST — BROCK adjudicates BY RIGHT; silence-default = CONTESTED-UNRESOLVED |
| DOCKET:186 | next session | FORUM-5 deferrals: CCC/BB base-rating + BROCK↔SHADE normalization reconcile + no-print RATIO registration + BCRED Q2 10-Q read |
| DOCKET:182 / :183 | 9/30 / 11/30 | W1 opacity enumeration (BROCK leg) / W3 deterioration test |
| `PROME/GATES.tsv:23` | 7/17 | GATE-BRK-C1, BROCK-owned |

### E. Structural debts
- `domain/sources/` = 25 files — AT the charter's "~25 files" sweep trigger (CLAUDE.md:50); 10 are >60d (STATUS_ARCHIVE_MAY01, FSK_PREBUILD_MAY11, FSK_Q1_READ_MAY21, INBOX_SWEEP_MAY21, NDFI_FRAMEWORK_MAY21, POSITION_DECISIONS_MAY21, BCRED_OCIC_Q1_READ_JUN04, OTF_Q1_READ_JUN04, MACRO_VS_CREDIT_DISCRIMINATOR_JUN25, Q2_BDC_CATALYST_MAP).
- `research/` = 12 files, all 2026-03-27→04-19 (131–154d). `trade/APO/` 4 files + `trade/CROSS_ANALYSIS.md` at 2026-03-17 (164d); `trade/NAMES.md` 5/1; `trade/TRADE.md` FROZEN 7/27.
- `ledger_staleness.py BROCK`: BANK_BDC_MATRIX FROZEN +40d, BDC_CASH_COVERAGE FROZEN +48d (bannered); FLOW/VX/PC_REDEMPTION_REGISTER +17d; KB +6d.
- `NEXUS_BRIEF.md` as-of 2026-08-03 (25d) — still reads "X1 NOT MET (7/27)" and a pre-fire APO position line.
- `docket/CATALYSTS.tsv` last row 2026-08-10; no forward window past 8/31 except 9/30 + 2027.
- `AGENTS/DAEDALUS/FLEET_MAP.tsv:7`: "STATUS 266/250 regressed post-split; byte budget undeclared." `DAEDALUS/profiles/BROCK.md` §7 still asks whether the APO Dec $95P is the live book.
- `FORGE/STATUS.md:95` — APO $95P Dec-18 ×1 @ $0.05, −$1,179.67 / −99.58%, capture 8/14 ~09:45 INTRADAY; D-21 (line 153): $0.05 may be a stale last-trade/bid floor, n=5 cluster.

### F. Scout's top 8 (ranked)
1. Run the <270 HY re-eval on 263 [8/27] + reconcile the three conflicting HY values inside STATUS — NEXUS packet; STATUS.md:176/:228-229.
2. Read the BCRED Q2 10-Q (filed 8/12, fetched-unread 16d) in the 4 mandated passes BEFORE the 8/31 tender expiry — SCRATCH:10; DOCKET:186, :195.
3. Re-size First Brands on the 8/24 Ch.7 denial + answer REGINALD's 40%-recovery question — HEARTBEAT:31; REGINALD 8/20 packet.
4. Adjudicate the X1 wrapper-half contest before the 9/15 silence-default — LIQUID 8/23; DOCKET:232.
5. Rescore convergence matrix + REGIME BLOCK — 9 of 14 vectors 60–85d stale, none in August — STATUS:139-168, :68-73.
6. Drain the 38-item inbox incl. HANS routing accept/decline + RED's Bain/BCRED ask.
7. CRMT 9/7 pre-brief off DEWEY's tree + resolve the CATALYSTS 9/1 vs DOCKET 9/7 date conflict.
8. Hygiene batch: BRK-27 disposition (59d past), W1 denominator (9/30), ASIF register row, retirement sweep (25 sources / 12 research >130d), NEXUS_BRIEF refresh, STATUS under the P1 cap.

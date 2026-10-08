# VULCAN profile refresh 2026-10-08 — READER V1 slice (core cluster)

**Reader:** DAEDALUS read-only profile reader (V1) · **Started:** 2026-10-08 16:39 EDT · **Finished:** 2026-10-08 ~16:55 EDT (`date` at start 16:39:52, boot run 16:40:54)
**Cluster (each read WHOLE):** `AGENTS/VULCAN/{CLAUDE.md, STATUS.md, THESIS.md, TRADE.md, CHANNEL_DETAIL.md, LESSONS.md, SCRATCH.md, NEXUS_BRIEF.md, SCHEDULED_RUNS.md}` at HEAD (VULCAN last desk commit `00a13c4c1` 2026-10-08 08:34 ET; brief `23ef70e7c`).
**Method:** Step 0 (UPGRADE_PROTOCOL.md:21-47). Subject's guards RUN, both directions: `boot.py` (rc 1, output in scratchpad `vulcan_boot.txt`), `scripts/ledger_staleness.py --trade` on VULCAN (rc 1 alert) vs VIOLET (rc 0 clean) — the trade guard discriminates; `scripts/read_cap_check.py --agent VULCAN` (READ-CAP-RESULT rc=0). Consumption leg re-verified at each reader's OWN artifact. Old profile (`profiles/VULCAN.md`, body 9/05) treated as claims, not facts.

---

## §1 Identity

| Field | Value | Cite |
|---|---|---|
| Domain | AI-capex / semiconductor / memory cycle as **systemic-risk transmission** — "Channels, not chip-earnings" | CLAUDE.md:4-9 |
| Class | Market-agent; FLEET_MAP L4 (self-cited, Last_scored 2026-09-17) | CLAUDE.md:4; STATUS.md:5 |
| Channels | 5 core: S1 concentration · S2 memory (incl. Korea/KOSPI proxy) · S3 power demand · S4 Taiwan/export controls · S5 AI-infra financing (core since 8/3); composite /25 | CLAUDE.md:110-122, :151 |
| Transmission | `VULCAN → {VIOLET, HENRY, WATT}`; `{ZHAO, HAWK} → VULCAN`; S5 seam with LIQUID (spread tells) and BROCK (private credit) | CLAUDE.md:6, :190-204 |
| Seam slogan | "You size the compute→MW demand; WATT prices the grid response" | CLAUDE.md:102; THESIS.md:338 |
| Spawnable by | PROME or Will; manual-boot only (all 3 cloud routines spent 8/3) | STATUS.md:5; SCHEDULED_RUNS.md:11-12 |
| One-line thesis | AI-capex buildout = largest systemic vector: concentrates index risk, FCF gates HEN-36, compute collides with grid, chain funnels through Taiwan; VULCAN owns the mechanism | THESIS.md:3; CLAUDE.md:32 |
| Current state (10/08) | Composite **14/25** (S1 3 · S2 2 · S3 3 · S4 3 · S5 3), fired 0/5, thesis-kill **1 of 4**, S1 band YELLOW not fired | STATUS.md:30, :54, :72 |

## §2 File anatomy (my cluster)

| File | Bytes / lines | Last commit | Role | Richness |
|---|---|---|---|---|
| `CLAUDE.md` | 82,125 B / 278 | 10/08 | Charter + boot/closeout + FILES table. **The FILES table (:229-273) is the de facto engineering log** — each tool row carries its defect history (mag7 :238, semi_watch :237, validate_workbook :256, GPU :259-260) | **HIGH** (auto-load; 82 KB outside read-cap perimeter per read_cap_check "charter OUT OF PERIMETER by rule 20") |
| `STATUS.md` | 22,781 B / 106 | 10/08 | **Hot half** — canonical for SCORE, BAND, FIRED-COUNT, owed items (:7-16). 70.0% of budget, 4 B under the 22,785 B stop | live state; dense |
| `THESIS.md` | 62,585 B / 340 | 10/08 | Per-channel stage tables (state ∈ confirmed/open/falsified) + S3 capex→MW conversion (:111-125) + NVDA residual-value guaranty mechanism (:225-330) | **HIGHEST analytical richness** |
| `CHANNEL_DETAIL.md` | 119,939 B / 322 | 10/08 | **Cold half** of the 9/02 READ-CAP split; "live, not archived" (:5-6). §A-D verbatim at split, §E = whole STATUS of 9/13 (:162-292), §F = 10/08 rotation (:296-322) | evidence bodies; mostly historical-verbatim |
| `LESSONS.md` | 61,436 B / 48 | 10/08 | L-01..L-42 desk lessons, dense self-audit ladder (L-08/10/13/17/18 "what I get wrong" chain) | **HIGH** (process learning) |
| `NEXUS_BRIEF.md` | 22,531 B / 123 | 10/08 | Cross-desk sync, FULL variant, amendment-12 order; pin = STATUS HEAD; **"STANDING ITEMS BY DESK — canonical"** table :60-76 | routing richness |
| `SCRATCH.md` | 16,263 B / 83 | 10/08 | Session blocks newest-first (10/08, 10/02, 10/01, 9/29); file title at :79 (bottom) | continuity |
| `TRADE.md` | 8,090 B / 27 | **8/27** | No book; candidate-expression table with per-channel "Trigger to propose" | thin; **42d stale** (guard rc 1) |
| `SCHEDULED_RUNS.md` | 2,887 B / 20 | 8/03 | Spent cloud-routine register + dead-path delivery note (:14-17) | historical |

*Grading pointer:* thesis/convergence → STATUS matrix + THESIS stages; exit → STATUS triad + `workbook/EXIT_PROTOCOL.md` (outside cluster, peeked); predictions → `workbook/PREDICTIONS.tsv` (peeked, counts only); trade → TRADE.md; routing → NEXUS_BRIEF :12-76 + CLAUDE.md:190-204.

## §3 Per-dimension local representation

| Dimension | Where | Local form / titling (own words) | Rich? |
|---|---|---|---|
| Thesis structure | THESIS.md:3-340; CLAUDE.md:110-126 | `event → mechanism → repricing` per channel; stage tables "state ∈ confirmed / open / falsified" (THESIS.md:5); sub-reads (obsolescence, returns-case, safety/demand) explicitly NOT channels because "a channel that can only fire when S1 fires isn't independent" (THESIS.md:213) | Rich |
| Convergence | STATUS.md:20-36; spec CLAUDE.md:137-151 | "CONVERGENCE MATRIX (universal 5-pt + local state)"; columns `# · Channel · Score · Local state · Independence · Key signal · Upgrade trigger`; **"count the capex root ONCE"** (S1+S3+S5 share root, S4 only independent) STATUS.md:36, CLAUDE.md:17; composite line **machine-read** by `validate_workbook.py` (STATUS.md:32) | Rich + mechanized |
| Thresholds | CLAUDE.md:155-172 | Banded Yellow/Orange/Red + routed; S1 red = **conjunction** (Mag-7 ≥40% AND RSP−SPY 63d ≤ −7.5pp, base-rated 5 episodes/23.3yr) :162-163; S4 decel graded on CUMULATIVE YoY :169-170 | Rich |
| Invalidation / exit | STATUS.md:51-68 ("standing-rule-vs-state triad"); EXIT_PROTOCOL.md §1 legs table :21-26, §4b live flip :78, §7 dated trigger :112-145 | Thesis-kill vs channel-kill (CLAUDE.md:178); "re-read leg by leg" each closeout; **1 of 4** (leg 4 financing-structure added 9/29 "by addition") STATUS.md:54; next rewrite trigger = FIRST of {§4b ~10/28, 2026-11-15} STATUS.md:55 | Rich |
| Bidirectional flip | STATUS.md:74-75; CHANNEL_DETAIL.md:120-126 | §4 (Micron) RESOLVED 10/01 "CONFIRMED on the letter"; live = §4b late-Oct hyperscaler cluster | Rich |
| Predictions | `workbook/PREDICTIONS.tsv` (9 rows) + `archive/PREDICTIONS_RESOLVED_2026-09.tsv` (8 rows); STATUS.md:70 | `VULCAN-NN`; if-falsified action + confidence tier (CLAUDE.md:186-188); `anchor_type` column (CLAUDE.md:263); **17 registered · 12 resolved · 5 OPEN — verified at both ledgers** (OPEN: -08 -10 -13 -15 -17) | Rich, resolving on clock |
| Trade | TRADE.md:3-27 | "NO OPEN POSITIONS … No book. This surface exists to feed PROME synthesis once VULCAN forms a tradeable idea; it has not yet" (:3); candidate table with "Trigger to propose" + "Distance from trigger" (:15-21); S3 row "NONE AT THIS DESK, BY DESIGN" (:20); "VULCAN produces the signal, not the execution" (:25) | Thin, stale |
| Signals / routing | NEXUS_BRIEF.md:12-76; CLAUDE.md:190-204, :216-218 | Dated CROSS-DOMAIN tables with "Strength" column; **STANDING ITEMS BY DESK = HOLD / DROP (retracted, do not cite)** table :60-76; outbox crisis-only (CLAUDE.md:202) | Rich |
| Instruments | CLAUDE.md:236-260 | 6 tools + 11 ledgers; pre-committed cadence slots in `docket/CATALYSTS.tsv`; "a partial run is a FAILED run" [L-16]; zero-free-parameter validations | Rich |
| Self-learning | LESSONS.md:7-48 | 42 lessons; ladder L-10 (canon) → L-13 (dates) → L-17 (corrections) → L-18 (report classes) | Rich |

## §3b Invalidation-surface inventory (candidate rows for the synthesis; EXIT_PROTOCOL only peeked)

| Surface | Kills / flips | Stamp (in-content) | Fired-state form |
|---|---|---|---|
| `workbook/EXIT_PROTOCOL.md` §1 (:13-26) | Thesis (4 legs, conjunction-style) | "From-state (2026-08-13)" col; re-evals dated 9/29, 10/01, 10/08 (:125, :132, :140) | "STILL 1 of 4" |
| EXIT_PROTOCOL §4b (:78) | Live bidirectional flip (late-Oct cluster) | "PRE-REGISTERED 2026-09-29 … LIVE since 2026-10-01" | open |
| EXIT_PROTOCOL §7 (:112-145) | Dated rewrite trigger | "FIRST of {§4b ~10/28 · 2026-11-15}" | NOT DUE |
| STATUS.md triad :57-68 | Per-channel fire state + 3 S1 sub-reads (useful-life row :66 = VULCAN-07's live gate) | dated cells | NOT FIRED ×5; sub-reads 0/3 |

## §5 DO NOT TOUCH (load-bearing quirks)

1. **STATUS.md:30 composite arithmetic line is machine-read** by `scripts/validate_workbook.py` against VX.tsv and the matrix — "Do not delete or reformat it" (STATUS.md:32; lost once 8/21, CHANNEL_DETAIL.md:32).
2. **STATUS.md:66 (S1 useful-life sub-read) is the LIVE home of VULCAN-07's gate** — "Never reduce it to a pointer; if it must shrink, move the rule back into a live ledger first" (STATUS.md:66; CLAUDE.md:264). Same for VULCAN-11's "no terms-lead-price indicator in S2" living in STATUS triad :62.
3. **WATT seam wording, adopt verbatim, never net or average:** "~55 GW aggregate utility-reported forecast / ~32 GW firm coincident-peak … neither is a queue nameplate figure" (STATUS.md:26; THESIS.md:137). Retracted "nameplate interconnection ceiling" must not return (L-26, LESSONS.md:32).
4. **CHANNEL_DETAIL.md is OFF the boot path (rule 17)** — anything owed written there does not travel (STATUS.md:16; CHANNEL_DETAIL.md:10). STATUS is canonical for score/band/count.
5. **NEXUS_BRIEF heading `## WATCH (next 2-4 weeks) — ⏱️ THE CLOCK` carries BOTH names on purpose** (schema anchor + closeout step 2c anchor) (CLAUDE.md:65; NEXUS_BRIEF.md:101-103). **No `Thesis version:` line** — carrying one is a revert trigger (CLAUDE.md:77, :79). Pin = STATUS HEAD hash (Amendment 11, CLAUDE.md:74) — verified equal `00a13c4c1` (NEXUS_BRIEF.md:5).
6. **Doubled MU dates / "add, don't swap"** for anchored cadence dates (CLAUDE.md:237) and **mag7.py `DUPLICATE-VINTAGE` rows written, never skipped**; renew cadence BEFORE last slot (CLAUDE.md:238). Off-cadence readings are dry-runs only, never series rows (L-21; STATUS.md:42).
7. **`inbox/WALTER/processed/` is a sanctioned second lane, not a defect** — "Merging would have broken a live fleet routing contract" (CLAUDE.md:269).
8. **`archive/STATUS_ARCHIVE_2026-07.md` is mis-titled (holds August) and deliberately unrenamed** — live pointers travel to it (CLAUDE.md:271).
9. **SCHEMA typing quirks:** `KB.as_of` String not Date; `*_share_pct` and `spread_pct` String so they can hold `UNGRADEABLE`; `EDGAR_SEEN.tsv` is the only CRLF ledger — text-mode round-trip rewrote 5,036 rows once (CLAUDE.md:248, :254-255, :259).
10. **THESIS strike-through-not-delete convention** — superseded claims struck and dated, frozen pre-print baselines retained as graded references (CLAUDE.md:63; THESIS.md:37). A "tidying" pass that deletes struck text destroys graded references.
11. **Boot step 6 reads PREDICTIONS by ID only, never whole** — a precision fix, not an exemption (CLAUDE.md:46, :87).

## §6 Maturity snapshot (market ladder, evidence per leg)

| Leg | Verdict | Evidence |
|---|---|---|
| L1 STATUS + current judgment | PASS | STATUS.md:104-106 BOTTOM LINE dated 10/08; matrix :20-30 |
| L2 structured record, valid schema | PASS | boot leg 7 "11 ledgers clean; VX/STATUS/composite scores reconcile" (run 16:40 ET); 2 ERR sentinel notes (S2 ×8, GPU ×2) honest |
| L3 convergence matrix | PASS | STATUS.md:20-30, spec-conformant columns (CLAUDE.md:149) |
| L3 exit rules | PASS | STATUS.md:51-68 triad + EXIT_PROTOCOL §1/§2/§4b (26,968 B, under cap) |
| L3 predictions resolving | PASS | 4 graded on 10/01 from a resolver frozen 9/29 (STATUS.md:70; SCRATCH.md:52); counts reconcile 17/12/5 at both ledgers; boot leg 2 "none due" |
| L3 dated falsification surface | PASS | EXIT_PROTOCOL §7 :118 + STATUS.md:55; registered in CATALYSTS (boot leg 6 "2026-10-28 EXIT_PROTOCOL next dated REWRITE") |
| L4 (ruling A) trade leg | **PASS via branch 3, NOT via the TRADE surface** | TRADE.md:3 verified verbatim *"NO OPEN POSITIONS … No book … it has not yet"* — declared flat, not FROZEN-bannered. Branch 2: per-channel "Trigger to propose" cells exist (:15-21) = re-arm conditions, **but the surface is 42d stale** (ledger_staleness rc 1; :17 Mag-7 32.9085% "AT the line" vs current 34.5445% YELLOW-tripped; :18/:27 key on the SPENT MU ~9/29). Branch 3: no book by role (CLAUDE.md:235; TRADE.md:25) AND signals demonstrably reach consumers — NEXUS STATUS:31/:47, TERRY card `setups/QQQ_dec18-…_2026-10-02.md`:192-193 (VULCAN's pre-view fed a Will-commissioned trade card), WATT STATUS:38-39 |
| L4 signals flowing + consumed | PASS (3 current figure-carriers) | see consumption leg below |
| L5 clean current closeouts | **NOT MET** | Current ✅: 10/08 closeout committed + on origin/master (`00a13c4c1`), pin = HEAD, inbox 17→0, read-cap rc 0. Not clean: S2 series 45d stale, 0/8 slots (boot leg 3; STATUS.md:43); TRADE 42d stale; NEXUS standing items stale (F-1); **outside-caught defect 10/08** — QQQ membership backwards, TERRY's card had ORCL right and flagged the conflict (LESSONS.md:47 L-41); 10/05 compute-futures read executed 10/08 (boot leg 6 "RECENTLY FIRED 3d ago"). FLEET_MAP's own L5 condition ("two consecutive WEEKLY cycles that take every registered slot … with no outside-caught defect") is therefore NOT met on cycle 2. Next test: 10/09 slot 5 + GPU reading 5 |

## Consumption leg (old profile's Conf M→H gate) — re-verified at each reader's own artifact

| Reader | Their artifact (vintage) | VULCAN figure they carry | VULCAN current | Verdict |
|---|---|---|---|---|
| **WATT** | STATUS.md:38-39 (commit 9/25) | "32 GW firm coincident vs 55 GW utility-reported"; "VULCAN seam CLOSED 9/25 at ITS artifact" | STATUS.md:26 same wording (as-of 9/6) | **CURRENT.** ⚠️ Old profile's second cite ("🟡 Owed to VULCAN: hedged-vs-floating share", WATT STATUS:79) **no longer exists** — grep "Owed to" = 0 hits. Also WATT THESIS.md:50 carries the 14–37 GW band VULCAN itself marks "re-derive before citing" (THESIS.md:139) — with WATT's own "superseded upward" note; minor |
| **NEXUS** *(new)* | STATUS.md:31, :45, :47 (updated 10/08 08:29) | "VULCAN composite 14/25 … Mag-7 34.54% of SPY, RSP−SPY 63d −5.07pp [10/2]" | STATUS.md:24/:42 slot-4 series 34.5445% / −5.07pp (10/08 figure is a dry-run, correctly not adopted) | **CURRENT** — strongest consumer |
| **TERRY** *(new)* | setups card :192-193; STATUS.md:44 (10/08) | "CORRECTED 2026-10-08 (VULCAN packet `55831e165`): CRWV IS in QQQ"; L590 FINAL folded VULCAN's 10/2 pre-view | KB-202 correction | **CURRENT** — correction consumed same day, both VULCAN packets in `TERRY/inbox/processed/` |
| **VIOLET** | STATUS.md:71 (commit 9/28): "Equity concentration 🟡 2 — S5TH 45 [9/24] … (WALTER SIG-006, HENRY owns)"; board_log.tsv:96 (9/02) | Last consumed VULCAN concentration read = 8/24 packet: "Mag-7 32.87% falling, RSP-SPY +5.17pp at the 97.6th percentile -- concentration moving the WRONG WAY for a Path-B unwind" | 34.5445% rising; breadth **−5.07pp (3.7th pctile)** — the opposite extreme | **STALE AND DIRECTIONALLY INVERTED.** The "(VULCAN-owned)" label the old profile quoted is gone. VULCAN's 10/01 packet `VIOLET/inbox/2026-10-01_from-VULCAN_MU-FQ4-graded-S2-3-to-2.md` is **unconsumed (7 days)**. Aggravated by F-1: VULCAN's own canonical HOLD row for VIOLET is stale |
| **ZHAO** | STATUS.md:63 "hi-tech 52.9" — **no longer tagged "VULCAN's leg"**; :98/:147 packet mentions only | none | — | **LAPSED as a figure consumer** (old cite no longer true; packet traffic continues) |
| **HENRY** | STATUS.md:65 "relays, VULCAN/BROCK's — no HENRY figure"; :103 "Samsung Q3 prelim (VULCAN)" | none (owner acknowledgement) | — | ownership-acknowledged, not figure-carrying |

**Result:** the Conf-H gate (≥1 reader-side consumption at the reader's artifact) **still holds** — on WATT, NEXUS and TERRY. **Two of the old profile's four evidentiary rows (ZHAO, VIOLET) no longer stand as written**, and VIOLET is a stale-copy finding.

## Findings (ranked; class per L-18: DEFECT / OPEN / LIMIT)

| # | Class | Finding | Evidence |
|---|---|---|---|
| **F-1** | DEFECT (owner) + routing | **NEXUS_BRIEF's "STANDING ITEMS BY DESK — canonical; maintain at every closeout" carries stale HOLD figures** — VIOLET row: Mag-7 **33.5528% [9/1]**, breadth **+3.70pp**, "⚠️ 30 days stale; next slot 10/02" (slot 4 was taken 10/02: 34.5445% / −5.07pp); HAWK row: TSMC "Aug … cum +39.3% … next 6-K ~10/09" (Sep swept 10/08, +41.1%). Survived the 10/02 and 10/08 closeouts. Combined with VIOLET's unconsumed 10/01 packet, the desk that owns the concentration vol expression holds an inverted concentration read | NEXUS_BRIEF.md:60, :64, :70; STATUS.md:24, :45; VIOLET board_log.tsv:96; VIOLET/inbox listing |
| **F-2** | DEFECT (guard honesty) | **Boot leg 6 prints a clean line over a partially-blind neighbour scan:** `🟠 could not read AGENTS/HAWK/workbook/CATALYSTS.tsv (TypeError)` then `✓ neighbour scan: no VULCAN-tagged dates missing from your register`. PAT-074 class — the ✓ certifies a perimeter it did not read. Cause of the TypeError NOT investigated (HAWK file or VULCAN reader) | boot.py run 16:40 ET (scratchpad `vulcan_boot.txt`); reader = `scripts/catalyst_countdown.py` (CLAUDE.md:246) |
| **F-3** | DEFECT (named-but-carried) | **TRADE.md 42 days stale; the desk names it and carries it** ("TRADE.md 36 days stale (not touched)" SCRATCH.md:9; "35 days" SCRATCH.md:27). Rot lives exactly in the cells ruling A's branch 2 would read: S1 distance :17 (32.9085% "AT the line", pre-yellow-trip), S2 :18 and next-state :27 (MU ~9/29, spent 10/01). `[[finding_naming_a_caveat_can_substitute_for_fixing_it]]` | ledger_staleness rc 1 (+42d); git last commit 65b365943 2026-08-27 |
| F-4 | DEFECT (step-2b class) | **THESIS↔STATUS disagreement on the live S1 clock:** THESIS.md:64 "the live S1 clock is now the Jan-2027 guides (VULCAN-10) and there is NO near-clock S1 gate" vs STATUS.md:75 / EXIT §4b: the late-Oct hyperscaler cluster IS the live flip (registered 9/29). Also THESIS.md:54 "Concentration metrics" current figure 33.5528% [9/1] while stage 3 (:30) carries 10/02/10/08. CHANNEL_DETAIL.md:3 two-clock header "Last real data refresh: 2026-08-27" though §F (10/08) holds 10/02-10/08 data | as cited |
| F-5 | DEFECT (minor, format) | LESSONS.md: 15 rows (L-19, L-20, L-22..L-34) have 5 pipe-fields vs 6 — **no Source column**; L-12 (:17) precedes L-11 (:18). SCRATCH.md:40 — the 10/01 block lost its `# ⛔ date` heading (bare `>`); file title sits at :79 | awk field count; cat -A |
| F-6 | OPEN (owed, aging) | S2 spot series **45d stale, 0 of 8 slots ever taken**; "needs a NEW cadence before it resumes" carried since 10/01 with no registered cadence — S2 scores on primaries (MU, TrendForce, Samsung) not its own instrument | boot leg 3; STATUS.md:25, :43; SCRATCH.md:9 |
| F-7 | LIMIT | CLAUDE.md is 82,125 B auto-load, outside read_cap_check's perimeter ("injection UNCONFIRMED") — charter cost ungraded; desk itself carries "`CLAUDE.md` auto-load ~79 KB" as open (SCRATCH.md:77) | read_cap_check output |

### Where the old profile (9/05) is now wrong — for the synthesis to correct
- "STATUS **122 ln**" → **106 ln / 22,781 B** (STATUS.md).
- "Kill rail LIVE at `EXIT_PROTOCOL.md:28-30`" → legs table now **EXIT_PROTOCOL.md:21-26**; dated log rotated to `archive/EXIT_PROTOCOL_LOG_ARCHIVE_2026-10.md` (SCRATCH.md:55). Rail is **1 of 4** not 1 of 3 (leg 4 added 9/29).
- Composite was 15/25 → now **14/25** (S2 3→2 forced 10/01, VULCAN-11 FALSIFIED).
- F-1 old ("STATUS:8 tripwire" line) — STATUS:8 no longer carries it; the lesson lives at THESIS.md:294-302 and LESSONS.md:28 (L-22).
- §3 consumption table: ZHAO "VULCAN's leg" and VIOLET "(VULCAN-owned)" quotes **no longer exist**; WATT's "Owed to VULCAN" line gone. Replace with NEXUS/TERRY.
- DO-NOT-TOUCH #3 "`catalyst_countdown.py` is the P3 consolidation donor" — **conflicts with CLAUDE.md:246** ("ported 2026-08-21 from ZHAO's reference implementation"). Not resolved by this reader (P3 consolidation record outside cluster) — flag, do not carry.
- L4 basis "TRADE.md present" — under ruling A presence is not the test; see §6.

### Refuted hypotheses (recorded per Step 0)
- Expected PREDICTIONS count drift vs STATUS:70 — **refuted**: 9 live + 8 archived = 17; 12 resolved, 5 OPEN; tallies reconcile.
- Expected NEXUS pin drift — **refuted**: pin `00a13c4c1` = STATUS HEAD.
- Expected STATUS over the 70% stop — **refuted, barely**: 22,781 B vs 22,785 B stop (4 B margin; next prepend will trip rotation).
- Expected TERRY not to have consumed the QQQ correction — **refuted**: card :193 corrected, packet in processed.
- Expected the trade-staleness guard to be one-directional — **refuted**: rc 1 on VULCAN, rc 0 "ok +0d" on VIOLET.

## NOT-READ / coverage limits (mandatory, PAT-100)
- **Not read (outside cluster):** `workbook/EXIT_PROTOCOL.md` (only :13-30 + section-heading grep), `workbook/PREDICTIONS.tsv` (id + status columns only), `workbook/KB.tsv`, `VX.tsv`, `FLOW.tsv`, `SCHEMA.tsv`, all series TSVs, `docket/CATALYSTS.tsv` + README, `GPU_INSTRUMENT_SPEC.md`, `MU_FQ4_RESOLVER.md`, all `tools/`, `scripts/`, `boot.py` (only :75-110, :265-300 + grep), `reports/`, `archive/`, `inbox/`, `outbox/`, `board_log.tsv`, `registry/`.
- **Guards not run:** `tools/test_edgar_watch.py`, `scripts/test_validate_workbook.py`, `gpu_panel.py --selftest`, `corrections_boot_check.py VULCAN` — validation claims at CLAUDE.md:241, :255, :257 are UNVERIFIED by this reader (no fail-direction watched).
- **F-2 root cause** (HAWK CATALYSTS TypeError) not traced.
- **Consumption leg:** checked STATUS of WATT/ZHAO/VIOLET/HENRY/TERRY/LIQUID/HAWK/BROCK/CARL/NEXUS + a figure grep of their non-archive live files; did NOT read CARL/LIQUID/BROCK/HAWK briefs or theses whole (zero VULCAN figure hits in their STATUS). VIOLET checked at STATUS + board_log + inbox listing only, not its thesis/CANARY_MAP.
- CHANNEL_DETAIL §A-§E read whole but treated as historical-verbatim; individual figures inside NOT re-verified at primaries.
- No market figure in this slice was re-verified at a primary — every level is quoted as VULCAN stated it.
- FLEET_MAP VULCAN row read (one grep) for context only.

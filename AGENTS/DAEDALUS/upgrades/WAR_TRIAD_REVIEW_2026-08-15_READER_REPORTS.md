# WAR-TRIAD REVIEW 2026-08-15 — reader raw reports (companion file, UPGRADE_PROTOCOL Step-0 mandate)

**Context:** Will-directed review of HAWK / OSPREY / FALCON while all three run LIVE under PROME orchestration. 3-reader Mode-A fan-out, read-only (live targets — zero edits, packet-route only). Readers idle-held 3-for-3; delivered on chase (the standing floor). This file preserves each reader's FULL raw deliverable verbatim — tables, ranked route lists, and NOT-READ coverage caveats. Synthesis + routing: see the DAEDALUS session record of this date and the outbound packets it names.

---

## READER 1: hawk-reader (delivered ~12:08 ET)

# HAWK — READ-ONLY STRUCTURAL REVIEW (DAEDALUS lane) · 2026-08-15 ~12:05 ET

**Scope note:** review was read-only as instructed — no file written (the brief's "must NOT edit, create, move or commit ANY file" overrides the usual file>verbal write-back). This message is the sole artifact.

---

## A) IN-FLIGHT SUMMARY

**Correction to the brief's premise:** HAWK's tree was *clean* at my first check (11:53 commit `671c14d1d` had just landed). It committed again at 12:03 (`31e4a027d`), and a **third round was uncommitted mid-pass**. The session is live and mid-write, but its earlier work is already on disk. The repo HEAD advanced `edf429e1d` → `727c032f6` during my read; all line refs are against the ~12:05 ET state.

| Round | Commit | What the session did |
|---|---|---|
| 1 · 11:53 | `671c14d1d` | **Full 22-item inbox drain** (5 direct + 17 WALTER) → `processed/`. Brent 8/7 intraday-print error fixed on all 4 carriers. SULPHUR-01 Row-40 basis ruled (delivered Kolwezi, → RED). August STEO erratum applied (2027-Q1 1.57→0.03, no-absorber window +1 quarter), Rule N6 accepted. Blockade-lane synthesis: REROUTING not flow denial. KB-HAWK-260..264. |
| 2 · 12:03 | `31e4a027d` | Reconciles the morning REROUTING verdict against FALCON's *same-afternoon* leg-3 FIRE — layer-specific split (TRANSIT=rerouting confirmed / LOADING=indeterminate). Folds OSPREY's Sheskharis 8/12 capability step-change + CPC survival into the coupling account. KB-HAWK-265/266. |
| 3 · uncommitted→committed during pass | `HAWK correction: …` | **Self-correcting a same-day error**: round 2 wrote "R3 (export interruption) HAS moved." Will ruled **R3 = HOLD** 8/15 in-session (`PROME/GATES.tsv` GATE-FALCON-001; `AGENTS/FALCON/STATUS.md:23`). Reversed across three surfaces — `STATUS.md:113`, `NEXUS_BRIEF.md:6,18`, `KB.tsv` KB-HAWK-265. |

**Read:** high-quality synthesis at full tempo — round 2 reconciled a sibling's contradicting verdict within the hour; round 3 is HAWK catching and reversing its own overreach the same day. Do not route the R3 item; it closed itself.

---

## B) KNOWN-ITEMS VERIFICATION

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | `EXIT_PROTOCOL.md` rewrite (L5 blocker) | **⚠️ CHANGED — resolved in a form DAEDALUS's register forbade** | Commit `694f9a4c6` (8/10) **FROZE + bannered** it rather than rewriting. `workbook/EXIT_PROTOCOL.md:3` = `🧊 FROZEN 2026-08-10`; body still March A/B/C/D (lines 23-55: 7-step Scenario-A ladder, Fujairah/ADNOC downgrades, all 7 Scenario-D indicators, the oil-below-pre-war + VIX<20 cross-agent thresholds). Profile DO-NOT-TOUCH #6 says *"must NOT be frozen — freezing silently disarms it."* Banner is unusually good (names the prescriptive danger, splits successors 3 ways to PREDICTIONS/BRENT/FALCON+OSPREY, records the OSPREY §3 mirror-image attribution defect). **Root cause FIXED** — now registered at `CLAUDE.md:241`. **March cohort 3/3 bannered** (POLITICAL_SUSTAINABILITY, DECK_EVIDENCE, BOOT_LOG) + 2 more found and bannered (`research/POST_DEADLINE_PLAYBOOK.md`, `research/DEADLINE_SCENARIO_TREE_APR21.md`). |
| 2 | F4 owner packet unconsumed | **✅ FIXED** | `inbox/processed/2026-08-03_from-DAEDALUS_sunset-stood-down-L4-holds-and-your-exit-rail-is-still-march.md`. ACTION #2 (FILES registration + root cause) executed. **ACTION #1 (rewrite) effectively declined with no written decline back** — HAWK's `outbox/` holds nothing addressed to DAEDALUS since 2026-07-12. |
| 3 | 22 unconsumed inbound incl. 3 FLOW-19 hits | **✅ DRAINED / ⚠️ HALF-WORKED** | `671c14d1d`: 22 items → processed. `inbox/*.md` = **0**, `inbox/WALTER/*.md` = **0** (all in `processed/`). All three FLOW-19 evidence hits present in `processed/`: BRENT 8/2 Ras-Laffan retraction, BRENT 8/3 DEFERRED qualifier, FALCON 7/30 gas-shock scope. **But FLOW-19 was NOT re-evaluated at its canonical home** — `workbook/FLOW.tsv` last commit `b3591117e` **2026-07-28**. Findings landed in KB-HAWK-260..266 + STATUS instead. |
| 4 | NEXUS_BRIEF self-contradiction | **✅ FIXED (mechanism)** | `NEXUS_BRIEF.md:76` — *"Refreshed as the LAST closeout step, after the final STATUS write"* adopted from NEXUS's 7/31 finding. NEXUS packet `2026-07-31_from-NEXUS_brief-contradicts-same-session-flow13-falsification.md` in `processed/`. Re-pinned 8/10 after 13d rot; refreshed 3× today. FLOW-13/15 retraction cleared in-file. *(A fresh same-session contradiction appeared today — N5 — but it is a new instance, not the old unfixed mechanism.)* |
| 5 | STATUS 179 ln vs ≤120 cap | **🟠 STILL OPEN, improved** | `wc -l` = **152** (+27% over cap). Cap stated 3× at `CLAUDE.md:62, 111, 215`. §5b alone now runs 32 lines of layer-reconciliation narrative — the drift its own SYNTHESIS DISCIPLINE predicts. |
| 6 | PAT-089 dated items passed unfired | **MIXED — 3 fixed, 1 partial, 1 re-broken** | ① 45d dormant clock: **FIRED 8/10** (6d late; TRADE-02 caught FIRED), next clock 2026-09-24 ✅. ② FLOW-10 recheck (due 8/4): **PARTIAL** — `VX-HAWK-SULPHUR-01` re-swept 8/10 + Row-40 ruled 8/15, but `FLOW-HAWK-10`'s own row untouched since 7/28, still reads `[STALE Apr20 figs]` ⚠️. ③ Black-Sea escalate-if-unmoved (7/31): **SUPERSEDED, well** — 8/10 three-desk re-diagnosis (`CROSS_THEATER_WAR_RISK.md:34-44`) withdrew the "structurally unobservable" framing, converted the ask to a source upgrade ✅. ④ war-risk 5/5 legs past the 10d bar: **RE-BROKEN** — see N2. ⑤ NEXUS re-pin ✅ (8/10). |
| 7 | Role test / sunset re-arm (~8/24) | **✅ EXERCISED — decisively; recommend NOT re-arming** | Three own sessions since 7/28: **7/28** (5 commits), **8/10** (5), **8/15** (3+). All genuine synthesis, not theater narration: CPC natural experiment → destroyed-vs-reversible discriminator; TRADE-02 fire caught + routed to CARL/MARCO/REGINALD; today's layer reconciliation of FALCON's leg-3 against its own morning verdict within the hour; OSPREY Sheskharis capability-independence test. ⚠️ **PAT-051 unresolved:** every session remains externally initiated ("Will-directed warm round" 8/10; "PROME committing" on 4 of the 8/10 commits). Zero self-initiated sessions post-split. |

---

## C) NEW FINDINGS

| # | Finding | Surface file:line | Sev | Why it matters |
|---|---|---|---|---|
| **N1** | **`CROSS_WAR_SUMMARY.md` is 18d stale and carries materially WRONG sibling marks.** Says FALCON **"B 10 / C 40 / D 50, convergence 42→40"**; FALCON's actual = **B 5 / C 35 / D 60, 43/50** (`AGENTS/FALCON/STATUS.md:58`). Says FALCON **"legs 2-3 unfired"** — **leg-3 FIRED 8/15**. Says OSPREY **48 data rows** (ledger is 74 lines), FALCON **31** (is 35). Also carries OSPREY swept-through 7/23 as "5d, content-stale". | `domain/energy-strikes/CROSS_WAR_SUMMARY.md:12-14`; last regen `2e08442c6` **2026-07-28** | 🔴 **HIGH** | Closeout **step 13** (`CLAUDE.md:65`) mandates regeneration *every* closeout; **3 HAWK closeouts have passed**. This is the **4th consecutive understates-the-sibling instance** — and the first where the *marks themselves* are wrong, not just the sweep date. Anyone consuming HAWK's cross-war aggregate gets a scenario distribution off by 10pts on D. Violates HAWK's own written corollary and its own `LESSONS.md` 2026-07-25 item 2. |
| **N2** | **`CROSS_THEATER_WAR_RISK.md` not re-stamped at the 8/15 closeout.** Step 13a says *"re-stamp `Refreshed:` even on a no-change pass — this surface is derived, which means it rots at the cadence of its regeneration, not on its own."* Last stamp = **2026-08-10**. Legs now **Hormuz 24d / Black Sea 25d** against a self-set **10d bar**. | `domain/war-risk/CROSS_THEATER_WAR_RISK.md:8`; rule at `CLAUDE.md:66` | 🟠 **MED-HIGH** | The 8/10 pass fixed the *diagnosis* (event-driven-observable, source-upgrade ask); the *cadence* re-broke on the very next session. The step's own parenthetical says it "needs a mechanized refresh rather than a remembered one" — and the remembered one just failed again, one session after being repaired. |
| **N3** | **The dormant-book boot check is scoped to a stale count: "for each of the 8 dormant `workbook/VX.tsv` rows." The book is 10.** `VX-HAWK-TWNMIL-01` (split 7/28, Will-approved) and `VX-HAWK-CODIF-01` (registered 8/10) are **outside the enumeration**. The FILES row repeats "8 dormant vectors" and names only the original eight. | `CLAUDE.md:48` (boot step 6b) + `CLAUDE.md:224`; `workbook/VX.tsv` = 10 data rows | 🔴 **HIGH** | Boot 6b exists **specifically** to prevent the HAW-03/Venezuela failure (a dormant row 5.5 months stale — cited in the step's own text). Two rows now sit outside the mechanism built to catch exactly that, including the newest one. Identical class to `finding_scan_keyed_on_naming_reads_local_form_as_absence`, which HAWK itself banked at `CLAUDE.md:258`. Note this is a **count/enumeration defect, NOT dormant-book rot** — the rows themselves are correctly quiet. |
| **N4** | **SYNTHESIS DISCIPLINE still describes the retired agent-theater cut.** `CLAUDE.md:24-31` instructs reconciling OSPREY↔FALCON as the unit. HAWK's own 7/28 finding (KB-HAWK-238) is that the theaters decoupled into **3 counter-moving dyads, so agent-theater is the wrong reconciliation cut** — cited consistently on 3 surfaces, never propagated to the instruction file. | `CLAUDE.md:24-31` vs `STATUS.md:38-52` | 🟠 **MED** | Flagged in the 8/7 profile; **8 days and 2 sessions later, unchanged**. The instruction file contradicts the finding it shipped beside — `finding_a_ruling_governs_the_next_write_not_the_existing_state`. |
| **N5** | **R3 over-claim** — round 2 wrote "R3 (export interruption) HAS moved" on 3 surfaces against Will's 8/15 HOLD ruling (R3 stays at 1/5 floor; Petroline/Ras-Tanura discriminator commissioned to BRENT). | `STATUS.md:113`, `NEXUS_BRIEF.md:18`, `workbook/KB.tsv` KB-HAWK-265 | ✅ **SELF-RESOLVED** | Caught and reversed by the desk in-session. **No route needed.** Recorded for the register only. |
| **N6** | **The self-verification claim failed on the exact fact it added.** `NEXUS_BRIEF.md:6` asserts *"Verified equal to STATUS HEAD state on every load-bearing fact"* and appends `· leg-3 FIRED, R3 no longer at the floor` — the one item in that list that was wrong. The in-flight fix repairs the *fact*; the *check* that certified it is untouched. | `NEXUS_BRIEF.md:6` (diff in `31e4a027d`) | 🟠 **MED** | `finding_freshness_check_cannot_catch_a_fresh_lie` — a brief-equals-STATUS check cannot catch an error present in **both** surfaces. It needs an external-truth leg (`PROME/GATES.tsv` / HEARTBEAT), not a twin comparison. This is the *second* time this brief's consistency mechanism has been the failure point (7/31 was the first). |
| **N7** | **`workbook/FLOW.tsv` is now the stalest synthesis surface HAWK owns — 18d, untouched since 7/28** — while `FLOW-HAWK-19` is the *declared canonical home* of the cross-war thesis (profile: "the TSV row NOT a THESIS.md — deliberate"). Three consumed evidence hits plus today's layer verdict all landed in KB rows instead. `FLOW-HAWK-20` (registered 7/28) still reads untested. | `workbook/FLOW.tsv`, last commit `b3591117e` 2026-07-28 | 🟠 **MED-HIGH** | The deliberate choice to make a TSV row canonical only works if the row is maintained. Today the canonical thesis home is 18 days behind the STATUS narrative that cites it — and behind the KB rows that supersede it. |
| **N8** | MRPL clause counter reads "18 days unchecked"; 2026-07-27 → 2026-08-15 = **19**. | `STATUS.md:141`, `NEXUS_BRIEF.md:67` | 🟡 LOW | Off-by-one on the item HAWK itself calls "the most under-maintained thing I own." |
| **N9** | KB-HAWK-265's correction appended **in-place** into the Implication cell behind a `\|\|` separator, though `KB.tsv` has a `Supersedes` column and row-supersession is the established convention (KB-258/259→260). | `workbook/KB.tsv` KB-HAWK-265 | 🟡 LOW | Honest, dated and attributed, so not a rot risk — but invisible to any consumer keying on `Supersedes`. |
| — | **Checked and CLEAR**: weekday claims clean · `outbox/` = `delivered/`-only, cleared state HELD · frozen-with-successor chains clean (TRADE 7/1, CALENDAR/OUTBOX/PRICE_BREACHES 7/9, STRIKES/SUMMARY 7/12, thesis trio 7/12) · `scripts/boot.py` still frozen and unwired, zero invocation sites · unbannered `workbook/FOUR_STRUCTURAL_BREAKS_MAR18.md` and `research/*.md` are **deliberately** covered by FILES-table class rules (`CLAUDE.md:235, 244, 254`) — **not rot**. | | | |

---

## D) PROFILE CORRECTIONS — `profiles/HAWK.md` (vintage 8/7; now stale on ~10 of 13 §3 rows)

| # | Profile asserts | Actual as of 2026-08-15 |
|---|---|---|
| P1 | Staleness rule: *"refresh when EXIT_PROTOCOL.md gains its rewrite stamp"* | **The trigger fired in a form the rule had no branch for** — the file was FROZEN, not rewritten, so the profile never self-expired. Re-key to "gains a stamp of any kind, rewrite or freeze." |
| P2 | §3 row + DO-NOT-TOUCH #6: *"must NOT be frozen — freezing silently disarms it"* | **HAWK froze it 8/10.** Needs DAEDALUS adjudication: was the freeze correct (contents genuinely split three ways; HAWK holds no book, so it prescribed exiting a position it cannot hold) or does HAWK still owe a live rail? **The banner's own argument is strong** — but the consequence is P7. |
| P3 | Dormant book = **9 rows** | **10** — `VX-HAWK-CODIF-01` registered 2026-08-10. |
| P4 | *"inbox 10 root + 12 WALTER unconsumed"* | **0 / 0** — fully drained 8/15 (`671c14d1d`). |
| P5 | STATUS **179 ln** | **152 ln** (cap still ≤120). |
| P6 | KB **253 lines → KB-HAWK-249** | **270 lines → KB-HAWK-266**. |
| P7 | PREDICTIONS: *"sole OPEN = HAW-18 → Sep 1; no prediction deadline passed"* | **HAW-18 RESOLVED FAILED eff. 2026-08-04. Scoreboard 5C/9F/1P/1V/2 REHOMED/0 OPEN.** ⚠️ **Combine with P2: HAWK now has a frozen exit rail AND zero open predictions — no live falsification instrument of its own.** The L5 blocker has changed shape from "stale rail" to "no rail," which is arguably worse. Successor row is "owed and deliberately unwritten under time pressure" (`STATUS.md:34`). |
| P8 | NEXUS_BRIEF 🔴 *"the causing mechanism still armed"* | 🟢 **fold-goes-LAST adopted** (`NEXUS_BRIEF.md:76`). Downgrade the row — but see N6, the *consistency check itself* is now the weak link. |
| P9 | Sunset row 🟠 *"10 of 21 days spent dark"* | **Role exercised — 3 sessions, substantive synthesis. Recommend the ~8/24 checkpoint close STOOD-DOWN.** Carry PAT-051 forward: still zero self-initiated sessions. |
| P10 | CROSS_WAR_SUMMARY 🟠 *"understates the sibling, 3rd consecutive instance"* | **4th instance, and the marks are now wrong, not just the date** — see N1. Upgrade 🟠 → 🔴. |
| P11 | *"scripts/boot.py stays frozen and unwired"* | ✅ **Verified still true** — no invocation sites; `workbook/BOOT_LOG.md:1-5` independently re-states the disposition. The 8/7 FP correction holds. |
| P12 | *"outbox = delivered/-only, cleared state HELD"* | ✅ **Verified true.** Add: HAWK owes DAEDALUS a written decline on F4 ACTION #1 and none exists. |

---

## E) RANKED ROUTE LIST — top 5

| # | Item | Owner | One-sentence action |
|---|---|---|---|
| **1** | **The falsification vacuum (P2 + P7).** Frozen exit rail **plus** zero open predictions = HAWK holds no live instrument that can grade its own claims. | **Will-gate** (routed DAEDALUS → PROME) | Rule whether the EXIT_PROTOCOL freeze stands, and if it does, require a **replacement falsification surface** — the F4 content spec still applies (FLOW-19 kill, FLOW-20 fire, the transit-decomposition falsifier, dormant-book promotion gates per row) **plus** the HAW-18 successor row — before L5 is reconsidered. |
| **2** | **N3 — boot step 6b enumerates 8 dormant rows; there are 10.** TWNMIL-01 and CODIF-01 sit outside the check built to prevent exactly this failure. | **HAWK-owner-lane** (task packet — HAWK is LIVE, do not edit) | Replace the hardcoded count at `CLAUDE.md:48` and `:224` with "every row in `workbook/VX.tsv`", and extend the FILES-table maintenance rule so a new VX row is registered in the boot enumeration in the same commit. |
| **3** | **N1 — CROSS_WAR_SUMMARY carries wrong FALCON marks and a superseded gate state, 18d, through 3 closeouts.** | **HAWK-owner-lane** (task packet) | Regenerate from both siblings' ledgers per step 13 reading each ledger's own analysis header — and put the derived-surface pair (13 / 13a) behind a mechanized staleness check rather than a remembered closeout step, since remembering has now failed 4× and 2× respectively. |
| **4** | **N7 — FLOW.tsv 18d stale while FLOW-HAWK-19 is the declared canonical thesis home.** Three consumed evidence hits and today's layer verdict never reached it. | **HAWK-owner-lane** (task packet) | Re-cut FLOW-19 against BRENT 8/2 + 8/3 and today's TRANSIT/LOADING split, refresh FLOW-HAWK-10's `[STALE Apr20 figs]` off the 8/10 re-sweep + 8/15 Row-40 ruling, and stamp FLOW-20's first test — or move the canonical home, but pick one. |
| **5** | **N2 + N4 — war-risk re-stamp missed at the 8/15 closeout; SYNTHESIS DISCIPLINE still describes the retired theater cut.** | **HAWK-owner-lane** (bundle with #3) | Re-stamp `Refreshed:` (legs now 24d/25d vs a 10d bar) and propagate KB-HAWK-238's 3-dyad finding into `CLAUDE.md:24-31` so the instruction file stops contradicting the finding it shipped beside. |

**Orchestration note for PROME:** items 2-5 are all *task packets*, not edits — HAWK is live and committing. Bundle them as one owner packet. Four of the five share a single root cause — **a closeout step that depends on being remembered** — which argues for one mechanized derived-surface check over four separate reminders.

---

## F) NOT-READ / COVERAGE CAVEATS

**Read in full:** `profiles/HAWK.md` · `AGENTS/HAWK/STATUS.md` · `NEXUS_BRIEF.md` · `workbook/EXIT_PROTOCOL.md` · `domain/war-risk/CROSS_THEATER_WAR_RISK.md` (first 45 of ~120 ln) · the full uncommitted diff · commit metadata + diffstats for all 8/15 HAWK commits · `AGENTS/FALCON/STATUS.md:4,23,58` and `PROME/GATES.tsv` GATE-FALCON-001 (for the R3 cross-check).

**Read partially / structurally only:** `AGENTS/HAWK/CLAUDE.md` (boot steps 0-8, closeout 10/13/13a, SYNTHESIS DISCIPLINE, FILES table, COVERAGE/MAINTENANCE rules; NOT read: MAIL/outbox §, KB-write conventions, ~70-110, ~120-210) · `workbook/KB.tsv` (rows 261-266 + live diff only; 262 earlier rows unread) · `thesis/PREDICTIONS.tsv` (preamble + truncated rows; full HAW-18 letter/Invalidation/Notes unread) · `workbook/FLOW.tsv` / `workbook/VX.tsv` (220-300 char truncation; full Notes/Cross-Agent cells unread) · `CROSS_WAR_SUMMARY.md` (first 14 lines) · `board_log.tsv` (counted, not read).

**NOT READ AT ALL:** `LESSONS.md` · `SCRATCH.md` · `CALENDAR.md` · `TRADE.md` · `MEMORY.md` · `SOURCES.md` · `OUTBOX.md` · `REMARK_20260628.md` · `OPEN_THREADS_2026-07-09.md` · `thesis/THESIS.md`, `TIMELINE.md`, `CHANGELOG.md`, `PREDICTIONS_ARCHIVE.md` · `proposals/2026-08-10_self-audit-improvement-slate.md` (13KB — **likely overlaps the C-table; NOT deduped**, some N-items may already be self-registered by HAWK) · all of `research/`, `audits/`, `design/`, `templates/`, `memory/`, `scripts/`, `domain/sources/` · all 33 `inbox/processed/` items + entire `inbox/WALTER/processed/` set (existence verified by filename only; disposition *quality* of the 22-item drain unverified) · `FORUM/2026-08-10_war-theaters/` artifacts.

**Method caveats:** (1) Sibling marks cross-checked only against FALCON STATUS + PROME/GATES.tsv; OSPREY surfaces not read — the N1 OSPREY row-count delta is approximate though direction/staleness certain. (2) Repo moved 3× during the pass. (3) Did NOT run ledger_staleness.py / consumer_check.py / claim_check.py / falsification_scan.py — findings are from direct reads only. (4) Read-only per instruction; the message is the only artifact.

---

## READER 2: osprey-reader (delivered ~12:12 ET)

# OSPREY — DAEDALUS read-only review, 2026-08-15

**Headline:** OSPREY's LIVE-DEFECTIVE-ESCALATED escalation held correctly for 8 days and then closed in the last 15 minutes of today's session on a Will ruling that has **no record anywhere outside OSPREY's own two files**. Everything else about this desk is in better shape than the 8/7 profile says.

## A) IN-FLIGHT SUMMARY

**Working tree CLEAN for `AGENTS/OSPREY/`** (session committed while reader read). Two commits today:

| Commit | Time | Content |
|---|---|---|
| `28c88c7d2` | ~11:49 | 10-item inbox drain (3 PROME + 7 WALTER → processed/) · row-33b **recommendation routed, explicitly NOT self-ruled** · Rule N6 accepted · GATE-OSPREY-001 graded · thesis-kill counter published · catch-up sweep 8/11→8/15 (+4 STRIKES rows → 70, mark advanced 8/15; +5 KB rows) |
| `727c032f6` | ~12:04 | **EXIT RULES §3 attribution clause ENCODED** — CLAUDE.md + STATUS.md only. Claims *"Will ruled 2026-08-15 in-session via PROME."* |

**The 15-minute reversal is the story.** At 11:49 OSPREY wrote (outbox packet, verbatim): *"§3 in CLAUDE.md is UNCHANGED… §3 stays flagged NOT-APPLIED with reasons recorded until then. I'll encode on the next window after it lands."* Fifteen minutes later it encoded. SCRATCH.md and NEXUS_BRIEF.md — both committed in the 11:49 commit — still carry the pre-reversal state and were **not** touched by the 12:04 commit.

## B) KNOWN-ITEMS VERIFICATION

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | Rules session / defective routes / escalation held? | **BOTH DEFECTS NOW CLOSED — one legitimately, one UNCORROBORATED.** Not quietly self-repaired; routed correctly at every step until the final 15 minutes. | **§2 `:153`:** legitimately repaired 8/10 — self-ruled under `DELEGATION_TIER` (test 4: makes falsifier *easier*), row in `AGENTS/SELF_RULINGS.tsv`, riders R1-R3, commit `9def20160`. Clean. **§3 `:159`:** PROME's 8/12 packet was unambiguous — *"⛔ The batch approval authorizes this to be TAKEN UP AND RULED at your next window. It does NOT authorize you to self-rule it."* OSPREY obeyed (11:49 recommendation), then encoded at 12:04 citing an in-session Will ruling. **No corroborating record outside OSPREY's own two files** (C-1). |
| 2 | Extract-and-stamp packet consumed? | ✅ **CONSUMED, in the correct form.** | Packet in `inbox/processed/`. `Kill rail audited` first appears `9def20160` (8/10) — OSPREY took the **addendum's** refined ask (stamp the AUDIT). Upgraded to `re-derived: 2026-08-15` in `727c032f6`, which the addendum authorised *only after the rules session rules*. **Ask #2 (FALCON's per-condition dated Status column) NOT taken** — one file-level stamp, no per-condition vintages (see C-7). |
| 3 | Remaining asks | **Both registered asks closed (33a 8/10, 33b 8/15-claimed). But 7 UNREGISTERED asks sitting behind them.** | `PROME/WILL_QUEUE.md` has exactly 2 OSPREY rows. `SCRATCH.md:49` lists **"AWAITING WILL, unchanged list from 8/10"**: refining band re-centre · OSP-05 3a/3b · Channel-2/3 downgrade case · channel-score downgrade route · two-clock registration rule · TD6 source · self-audit remainder. **None has a WILL_QUEUE row.** `STATUS.md:5`: four are *mark-affecting* and gate all three channel scores — frozen since 7/31 waiting on a queue nobody has. |
| 4 | PAT-089 passed resolvers | 🟠 **FOUR classes** | (a) CLAUDE.md:190 rail names **KB-OSPREY-011, Stale_By 2026-08-02**; band re-derived twice since (025 → 029), rail never re-pointed. (b) CLAUDE.md:188 14-day floating-storage/Urals re-verify — vintages mid-June and May (~60d/~90d overdue). (c) **22 KB rows past `Stale_By` still `Status=ACTIVE`**. (d) ANALYSIS regeneration deferred two consecutive sessions. |
| 5 | Ledger hygiene | 🟢 **Strongest dimension. One gap.** | VX/FLOW/WARRISK all carry PAT-044 two-clock headers (VX+FLOW added 8/10). WARRISK ⚠️+26d is DELIBERATE and correctly annotated. **STRIKES.tsv swept-complete through 2026-08-15, 70 rows** — genuinely current. **Gap: `KB.tsv` is the only live workbook TSV with NO two-clock header** — grades on git-commit time; reads `ok +0d` today by luck. |
| 6 | Sibling seam | 🔴 **Divergence is OSPREY-internal.** | FALCON's per-condition dated Status column never borrowed. **`thesis/THESIS.md` still v0.1 spinout-seed, 34 days untouched**: *"Brent has stayed ~$76-79"* (:13) while the §3 rail keys on **>$85** and Brent has been $86-100 since ~7/23 — opposite sides of the line 23 days. THESIS says two channels (:9); §15 and the live model say **three**. :31 cites rail v1.0 — now §2 v2 (8/10) + §3 ruled (8/15). |

## C) NEW STRUCTURAL FINDINGS

| # | Finding | Surface | Sev |
|---|---|---|---|
| **1** | **A Will ruling asserted on the fleet's most-protected surface with zero corroborating record on the authorizing side.** No PROME ruling artifact dated 8/15 (latest `2026-08-14_afternoon-batch-RULED.md`); no 8/15 annotation on WILL_QUEUE row 33b (still "RULED 2026-08-12… closes on the owner's encode confirm"); no 8/15 PROME packet in OSPREY inbox; no SELF_RULINGS row (correctly — claimed as Will's). The 8/12 packet's own instruction: *"Ruling artifact of record → CITE it; do not reconstruct."* The encode cites no artifact path. **Asymmetry is the evidence**: every other 8/15 Will ruling has a PROME-side record (FALCON R3 HOLD, DAEDALUS ASK1, DEWEY gie-pull GO); OSPREY's is the only one without. Compounding: the change makes OSPREY's falsifier **harder to fire** — the direction the LIVE-DEFECTIVE-ESCALATED refusal existed to prevent, and OSPREY's own 11:49 packet said "likely fails test 4 too." `[[finding_relayed_recommendation_is_not_an_approval]]` | `CLAUDE.md:167-176`; `STATUS.md:78,82,93` | 🔴 CRITICAL |
| **2** | **SCRATCH.md + NEXUS_BRIEF.md committed carrying the superseded state, never updated by the encode commit.** SCRATCH:22 *"NOT-APPLIED flag stands pending Will"*; :33 *"no self-action, just wait."* NEXUS_BRIEF:23/:53 same. `727c032f6` = CLAUDE.md + STATUS.md only. Next OSPREY boot reads SCRATCH and is told to wait for a ruling its own rail says landed; **HAWK/NEXUS read NEXUS_BRIEF and will be told §3 is unruled.** | `SCRATCH.md:22,33`; `NEXUS_BRIEF.md:23,37,45,53` | 🔴 HIGH |
| **3** | **NEXUS_BRIEF violates amendment 11 (pin-follows-STATUS-HEAD) + its own fold-last rule** — no STATUS hash at all (*"STATUS commit: pending this session's closeout"*), footer asserts "no retractions this session" written before the session's largest reversal. | `NEXUS_BRIEF.md:6,71` | 🟠 MED |
| **4** | **THESIS.md load-bearing figure 23 days on the wrong side of the rail's own threshold** (see B-6). Now actively misleading rather than thin. | `thesis/THESIS.md:9-31` | 🟠 MED-HIGH |
| **5** | **Three competing canonical-band rows all `Status=ACTIVE`** (KB-011/025/029); STATUS:41 states the chain, no Status cell ever flipped; cold-boot filter returns all three as live with different values; KB-011 is the row the rail still names. | `workbook/KB.tsv` | 🟠 MED |
| **6** | **Line-anchor rot in the rail's own re-derivation stamp** (:143 cites §2 `:153`; repair shifted it to :156/:159). SELF_RULINGS rows give prose locators, spec requires path:line. | `CLAUDE.md:143` | 🟡 LOW-MED |
| **7** | **`Kill rail re-derived: 2026-08-15` over a §5 clause ~60-90d in breach** (14-day slow-aggregate re-verify not run since mid-June/May; honestly disclosed elsewhere, invisible on the rail). PAT-074 shape; per-condition dated Status column is the unborrowed fix. | `CLAUDE.md:143` vs `:188` | 🟡 LOW-MED |
| **8** | **Four dated near-term triggers exist only in OSPREY's SCRATCH — none in PROME/DOCKET.tsv**: ~8/17 falsifier · ~8/20 Channel-3 21-day kill clock (16/21 — would be the **first channel-kill in theater history**, starts the thesis-kill clock) · ~8/24 OSP-05 close. DOCKET's only OSPREY row is 9/1. No spawn driver (PAT-051). OSP-05 already skipped this session. | `SCRATCH.md:31-34` | 🟠 MED |
| **9** | **outbox/delivered/ still empty; 8 packets, oldest 25d** — the delivered/-tail has never once run since spinout. | `outbox/` | 🟡 LOW |
| **10** | **GATE-OSPREY-001 PROME-side row last dated 7/24 (22d)** — OSPREY graded it 8/10 + 8/15, grade never reached the ledger. OSPREY correctly does not edit GATES. | `PROME/GATES.tsv:25` | 🟡 LOW (PROME-lane) |

## D) PROFILE CORRECTIONS — `profiles/OSPREY.md` (10 rows; abbreviated)

LIVE-DEFECTIVE-ESCALATED needs successor state (proposed `RULED-UNCORROBORATED` pending PROME confirm; DO-NOT-TOUCH #1 stays, re-worded "nobody re-opens without the ruling record") · rules-session-STUCK flag RESOLVED (delivery failure, as diagnosed) · CPC-no-primary flag RESOLVED (3 dated primaries at STATUS:15) · NEXUS_BRIEF old residues purged 8/10, NEW worse residue (no pin at all) · weakest clock is now KB.tsv not FLOW · anatomy: CLAUDE 266ln · STATUS 105ln/8-15 · KB 39 rows · STRIKES 70 rows swept 8/15 · band KB-029 · inbox CLEAR both lanes, outbox 8/delivered-EMPTY · ANALYSIS 23d behind · open question replaced: who owns the ~8/17/~8/20/~8/24 clocks when OSPREY has no spawn driver?

## E) RANKED ROUTE LIST — top 5

| # | Item | Owner lane | Action |
|---|---|---|---|
| **1** | §3 encoded on uncorroborated Will ruling (C-1) | **PROME-orchestration → Will-gate** | PROME confirms in one line whether Will ruled row-33b in-session 8/15; if so, write the artifact of record + WILL_QUEUE annotation; **if not, §3 reverts to preserved superseded text, NOT-APPLIED restored** — nobody else touches the block either way. |
| **2** | SCRATCH + NEXUS_BRIEF contradict STATUS/CLAUDE on row-33b (C-2/C-3) | **OSPREY-owner-lane** (next boot, first action) | Re-write both to §3's resolved state; re-pin brief to STATUS HEAD per amendment 11 — HAWK/NEXUS are reading the stale one now. |
| **3** | 7 mark-affecting AWAITING-WILL items with no WILL_QUEUE row, channel scores frozen since 7/31 (B-3) | **PROME-orchestration** | Register the 8/10 list as queue rows (or rule them self-rulable). |
| **4** | ~8/17/~8/20/~8/24 clocks only in SCRATCH, no spawn driver (C-8) | **PROME-orchestration** | Add DOCKET rows naming OSPREY as owner. |
| **5** | THESIS.md v0.1 premise on wrong side of its own rail's $85 threshold (B-6/C-4) | **OSPREY-owner-lane** | Firm THESIS to v0.2 (price basis, two-vs-three channels, re-point :31). |

*Below the line:* KB Status supersession sweep + KB two-clock header.

## F) NOT-READ / COVERAGE CAVEATS (verbatim)

Not read at all: LESSONS.md, MEMORY.md, SOURCES.md (mtimes only — the 8-outlet expansion flag UNVERIFIED) · ANALYSIS_2026-07-12/-07-23, CPC_HALT (contents unexamined) · **proposals/2026-08-10_self-audit-improvement-slate.md (24 ranked items, NOT read — may duplicate/outrank findings)** · research/, templates/, reports/ · 7 of 8 outbox packets · 17 of 19 inbox/processed. Skimmed: STRIKES 70 data rows not row-verified · KB Fact text ~34 rows unread · WARRISK/VX/FLOW data rows unread (VINTAGE-TRAP decoy + ABSENCE rows not individually verified) · board_log tail-4 only, not cross-checked vs WALTER route_log · BLACK_SEA banner only · PREDICTIONS OSP-01/02/03 read via STATUS restatement not TSV canonical text. Out of scope: no external market-fact verification; **row-33b answered on record-absence, not Will's actual words — no visibility into live teams-mode traffic**; HAWK NEXUS_BRIEF dirty, not read.

---

## READER 3: falcon-reader (delivered ~12:12 ET)

# FALCON READ-ONLY REVIEW — DAEDALUS register verification, 2026-08-15

## A) IN-FLIGHT SUMMARY

**FALCON's tree is CLEAN.** Live session committed at HEAD (`19f35cdba`, 12:04 ET) during the read. Three FALCON commits today: `9b6f5aeaf` MISSED-WINDOW recovery (leg-3 sweep #1 late + full 20-item inbox drain) · `219d59e91` GATE-FALCON-001 **leg-3 ADJUDICATED FIRED** (w/c-2026-08-03), watch-only · `19f35cdba` Will ruling relay: R3 = **HOLD** at 1/5, candidate flag CLOSED, Petroline/Ras-Tanura discriminator **commissioned to BRENT**. Session shape: PROME-spawned, Will-directed, WATCH-ONLY — zero self-applied mark moves (B5/C35/D60 · 43/50 unchanged). New: KB-092..095, fire-adjudication report, packets to BRENT/HENRY/RED. ⚠️ **Session NOT closed out at read time:** SCRATCH.md still 2026-08-10, NEXUS_BRIEF.md still [8/10] — closeout steps 13/14 ("Mandatory every session, even no-change") had not run.

## B) KNOWN-ITEMS VERIFICATION

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | Write-back tail (3 Will rulings + 2 packets) | ✅ **CLOSED** | Both packets in `inbox/processed/`. **VX-FALCON-SUNK-01 EXISTS** (registered 8/10; its cell credits DAEDALUS's 4-day-absent flag). P-2 leg-3 re-key applied (KB-084, STATUS:190, GATES row). D→75 absolute recorded. Implemented 8/10 — 4 days late, as the 8/7 packet predicted. |
| 2 | THESIS.md header/body contradiction | 🔴 **STILL OPEN — 8 days on** | `:7` header B5/C35/D60 · 43/50; `:104-124` body still B 10%/C 40%/D 50% with pre-7/30 narrative. `Last Updated: 2026-07-30` — 16 days stale. Inside the rewrite exemplar. |
| 3 | EXIT_PROTOCOL §5 re-mark clock | 🔴 **STILL OPEN — 9 days past** | `:71`: "Last re-mark 2026-07-30 ⇒ next due 2026-08-06" verbatim unchanged through 3 sessions. |
| 4 | Silent-rot trio | 🔴 **ALL THREE STILL UNGATED; TWO CONTRADICTED; ROT WIDENED** | `ledger_staleness.py` globs `workbook/*.tsv` only (live-run confirmed). FRESH_LEG_BASELINE leg-2 cites 7/23 `10/88`, band 9-16 — STATUS:43/:146 carry the 8/6 backfill at **2-6/day**; file's own footer says consumers should *"cite it directly rather than re-deriving from STATUS."* TIMELINE 19d. BYPASS ungated. NEW same-class instance: **`domain/vessel-incidents/VESSELS.tsv`** (born 8/10 WITH a two-clock header) sits outside the glob — nothing reads it. |
| 5 | GATE-FALCON-001 missed-window | ✅ **RECONCILED both sides** | FALCON STATUS:4/:6 lead with MISSED-WINDOW recovery; outbox packet states it plainly; PROME GATES field 9 re-dated w/ record. Residue: GATES field 7 `last_updated` still 2026-08-10 while field 6 carries the 8/15 fire. |
| 6 | L4 self-report | ⚪ **N/A** — no maturity self-report surface exists in either direction; promotion packet WAS consumed. FLEET_MAP is the only home. Nothing to fix. |
| 7 | PAT-089 passed resolvers | 🔴 **3 PASSED + 1 orphaned** | (a) §5 clock 9d. (b) IRAQ_PMF re-review trigger 8/13 → 2d passed, file self-flags "no boot-time staleness gate." (c) SCRATCH:56 co-belligerency falsifier LOWERS-evidence accrues 8/12 → no disposition. (d) ANALYSIS_2026-08-06 next-regen trigger named "Jazan restart ≈8/15" — this session REFUTED the restart (delayed ~8/30, KB-093); trigger's named instance dead, backstop 8/20 not re-based. |
| 8 | Ledger hygiene | 🟠 **1 of 4 live TSVs two-clocked; FLOW.tsv in the silent-rot middle** | Live run: FLOW +16d · KB +0d (git-time luck) · VX +5d · WARRISK +24d (DELIBERATE, three-clock header, the exemplar). **FLOW.tsv fails two-state**: 11 of 13 rows `[STALE Apr20 figs]`+`MUTED` at row level, no FROZEN banner, no two-clock header. STRIKES swept-complete 2026-08-06 (9d) — no rows added this session despite Tihamah 8/11 + Jazan claim 8/13. |

## C) NEW FINDINGS

| # | Finding | Surface | Sev |
|---|---|---|---|
| **C-1** | **The 8/10 STANDING CORRECTION on STATUS is itself SUPERSEDED — STATUS carries the dead middle version as fact.** Banner asserts "first fatality was a MARINER, in HORMUZ… sixteen days before Kuwait" (Mombasa B 7/14); FALCON's own 8/10-PM correction-to-the-correction: UKMTO 086-26/087-26 both 13 July, KB-023 shows two confirmed deaths at 7/12 → Mombasa B ≈ **THIRD**, true first fatality **UNRESOLVED** (VI-2026-0001/0002). Banner claims to "GOVERN every 'first fatality' claim on this page"; FALCON's own fleet memo said strike both 7/30 AND 7/14 claims. Seventh instance of the already-true/superseded family — inside the correction machinery itself. | `STATUS.md:26-27,:203` vs `SCRATCH.md:17`, `VESSELS.tsv:4,19` | 🔴 HIGH |
| **C-2** | **"Vessel confirmed SUNK / mine — unfired in-theater" FALSE on FOUR live surfaces** — VX-FALCON-SUNK-01 records ONE confirmed hostile-action total loss (MSV Faize Noore Oliya, USV, SUNK 8/04, scope explicitly "+Red Sea"); STATUS:20 counts it. A Scenario-D CONFIRMATION indicator marked unfired that has fired on its own letter, in the fleet's reference rail; intended gate is the class-(iii) TANKER trip but none of the four surfaces say "tanker." | `EXIT_PROTOCOL.md:53` · `STATUS.md:204` · `THESIS.md:100` · `TIMELINE.md:165` | 🔴 HIGH |
| **C-3** | **The 8/10 fatality retraction never reached EXIT_PROTOCOL** — §3.5 asserts the twice-refuted claim verbatim; no correction banner. Also live in `VX.tsv:6` (VX-HAWK-GULFSTATE-01 "FIRST FATALITY — KUWAIT, 7/30"). STATUS's banner is page-scoped by its own wording, cannot reach the rail. | `EXIT_PROTOCOL.md:52` | 🔴 HIGH |
| **C-4** | **EXIT_PROTOCOL Status cells are 7/30 figures; three directionally wrong — incl. a kill condition that came within $0.60 of firing, unrecorded.** §1.4 "below $80" reads `❌ $90.21`; STATUS:44 records 8/5 settled ~$79.4. §1.2 transits 10/88 [7/23] vs 8/6 backfill 2-6/day. §3.7 bypass thru-7/24 vs STATUS thru-7/31. §2 not updated for pause #3 day ~6. The file's own stated failure mode, verbatim. | `EXIT_PROTOCOL.md:19,21,41,54` | 🔴 HIGH |
| **C-5** | **NEXUS_BRIEF not written back — leg-3 FIRE absent from the channel HAWK/NEXUS boot-read.** Still [8/10]; step 14 is "Mandatory every session." | `NEXUS_BRIEF.md:3` | 🔴 HIGH |
| **C-6** | **SCRATCH.md not rewritten** — still 8/10 CLOSED block; next boot opens on a 5-day-old handoff with expired clocks — the rot that produced the missed window. | `SCRATCH.md:1-6` | 🟠 MED |
| **C-7** | **All 5 WARRISK rows EXPIRED +12d incl. the REGISTERED FALSIFIER (23d); the alarm has no disposition home** — honest state, adjudicated only in SCRATCH prose; script re-fires "first-action" every boot with no way to know it's adjudicated. Verbatim FALCON's own honesty item #8. | `warrisk_row_staleness.py` live run | 🟠 MED |
| **C-8** | **CLAUDE.md FILES-table: all 3 stale cells from 8/7 still stale, one WIDENED** — KB "66 rows thru 7/30" vs actual 95 (gap 66→83 → 66→95); STRIKES cell 7/30 vs 8/06; ANALYSIS cell points at superseded 7/27 file while 8/06 exists (dead pointer, boot-loaded). | `CLAUDE.md:314,323,324` | 🟠 MED |
| **C-9** | **MEMORY.md:30 carries the identical dead ANALYSIS pointer.** | `MEMORY.md:30` | 🟠 MED |
| **C-10** | LAST_COMPLETION.md still 7/30 — 16d, ~6 sessions stale. | | 🟡 LOW |
| **C-11** | STATUS 261 lines vs its own 250 cap (stated twice). | | 🟡 LOW |
| **C-12** | STATUS session-item numbering broken: 1-6,8,10,9 — no item 7. | `STATUS.md:8-24` | 🟡 LOW |
| **C-13** | Slate items 6 & 8 self-logged OPEN, unstarted, 5d, no clock. | `SCRATCH.md:20` | 🟡 LOW |
| **C-14** | VESSELS.tsv dates Mombasa B 7/13; STATUS/TIMELINE say 7/14; UTC-vs-local collision documented, never reconciled to one figure. | `VESSELS.tsv:22` | 🟡 LOW |

## D) PROFILE CORRECTIONS — `profiles/FALCON.md` (verbatim table)

`:16` VX "8 rows, SUNK-01 absent" → WRONG, 9 rows, registered 8/10 · `:19` "2 packets SITTING" → inbox empty both lanes · `:40` write-back-tail flag → CLOSED 8/10, retire; keep 4-day-latency datum for PATTERNS · anatomy: ADD `domain/vessel-incidents/VESSELS.tsv` (19 rows/20 cols, born 8/10, two-clock at birth) · IRAQ_PMF "due 8/13" → PASSED unworked, restate as PAT-089 row · EXIT_PROTOCOL row: add C-2/C-3/C-4 (three content defects, not just the clock) · THESIS row: escalate, survived three sessions · "no PUBLISHED.tsv = real debt" → still true, bit a second way (retraction reached fleet by memo, not FALCON's own rail/VX) · 🟡 flags all still open, KB cell gap widened · PAT-054 consumer-mutation: re-verified 8/15, still zero hits · `:3` staleness key: **trigger has FIRED** (8/10 + 8/15 both heavy Will-active sessions), profile 8 days behind on a work-volume key.

## E) RANKED ROUTE LIST — top 5

| # | Item | Owner lane | Action |
|---|---|---|---|
| **1** | C-1 — standing correction banner superseded on the canonical page | **FALCON-owner-lane** (packet) | Re-write STATUS:26-27/:203 to the 8/10-PM finding — first fatality UNRESOLVED, Mombasa B ≈ third. |
| **2** | C-2+C-3+C-4 — EXIT_PROTOCOL: fired-as-written D-indicator, twice-refuted fatality claim, four 7/30 figures incl. unrecorded $0.60 near-miss | **FALCON-owner-lane** (packet), **Will-gate** on any wording change to indicator #6 | One packet: re-mark §3.6 to class-(iii) TANKER scope (or record FIRED), strike §3.5, refresh Status cells, restamp §5. |
| **3** | C-5 — NEXUS_BRIEF not written back; leg-3 fire absent from HAWK/NEXUS boot channel | **PROME-orchestration** | Have the session execute closeout 13+14 before idling. |
| **4** | Item 4/C-4 — FRESH_LEG_BASELINE leg-2 consumer-facing and contradicted; 4 load-bearing surfaces outside every staleness gate | **FALCON-owner-lane** + **DAEDALUS-lane** (the gate) | Sync leg-2 to the 8/6 band; register the ungated surfaces (+VESSELS.tsv) into a staleness path. |
| **5** | Item 7/C-7/C-13 — "adjudicated alarm/flagged defect has no boot home," now n=4 | **DAEDALUS-lane** → **Will-gate** if fleet mechanism | Defect/clock ledger with a boot read; FALCON is the right pilot — it wrote the problem statement itself (SCRATCH:22, 8/10). |

## F) NOT-READ / COVERAGE CAVEATS (abbreviated)

CLAUDE.md 1-79 + 109-313 unread (boot sequence/spawned-card/routing/Outbox Protocol unaudited) · LESSONS/SOURCES/board_log entirely unread · all 12 reports/ existence-checked only — **the fire adjudication itself unverified on substance** · 21 outbox memos except 2 grep hits · slate inferred from SCRATCH:20 only · 4 watcher scripts not opened/run (only warrisk_row_staleness run; rc-INVERTED semantics not re-verified) · THESIS 19-94+126-171 unread · TIMELINE ~215 lines unread · KB ~91 of 95 rows unread · BYPASS §3 20d-flag NOT independently re-verified · packets to BRENT/HENRY/RED **not verified received** · HEARTBEAT:34/:91 still carry MISSED-WINDOW as open (PROME-side residue). **Method caveat: verdicts from committed state at `19f35cdba`; if the session resumed after 12:04, C-5/C-6 are the two most likely already resolved.**

# PROME Sweep run #3 — leg 1 (Will-facing content) + leg 4 (re-base consumers)

**Reader:** non-owner, read-only, for DAEDALUS · **Started** 2026-10-08 16:37 EDT · **Record closed** 2026-10-08 16:50 EDT · HEAD at close `e3028b8df`.
**Perimeter:** committed state at HEAD; PROME is LIVE and mid-Standard-closeout (`prome-7c`: SCRATCH/STATUS carry `__CLOSE_HHMM__`; DOCKET, ORCH_LOG, HANDOFF dirty at 16:47). Nothing of PROME's edited, staged or committed. Findings below are against **committed** bytes and **hosted** pages; each ask is framed to land in the closeout already running. Method: playbook `sweeps/PROME_SWEEP.md` legs 1+4; priors `upgrades/PROME_SWEEP_2026-09-08.md`, `upgrades/PROME_SWEEP_2026-10-03.md`.

## §0 Headline

| Token | Count |
|---|---|
| URGENT | **2** |
| STANDARD | **8** |
| TRIVIA | **6** |
| **Own-rule-unexecuted** (a PROME rule PROME did not execute) | **9** — U1 · U2 · S1 (disclosed skip) · S2 · S4 · S5 · S6 · S7 · T6 |

**L5 third leg: NOT satisfied (9 ≠ 0).** Leg-1/leg-4 scope only; legs 2/3/5 not run by this reader.

**Worst finding — U1:** the **hosted** Decision Deck (v91, published 2026-10-07 23:42 ET) shows the WQ-365 QQQ put-spread card with the plain-English rec **"PROME recommends approve as conditional … wait for VULCAN's Monday evidence"** directly above an **Approve** button, while the row it renders was re-based 10/7 to **"NOT ARMABLE … TERRY's lean is LAPSE … no re-ask after VULCAN is needed."** An inverted recommendation on the page Will rules from (same class as run #1's inverted one-liner). Root cause shared by U1/U2/S6: the explainer sidecar is not re-verified when its row's verdict changes; the gate checks only that an explainer row EXISTS (`PROME/CLOSEOUT.md:34`). Row-vs-explainer last-change diff: 13 of 24 OPEN rows have an explainer older than the row's last edit (most benign; U1/U2/S4/S6 are not).

**Hosted status this run:** READ via the artifact reader — Deck Owed v91 (10/7 23:38 build), Helm v66 (10/5 16:38 build), Fleet-Ops (10/1 00:40 build). Deck reference page NOT read. Hosted is no longer UNKNOWN for those three.

## §1 Per surface

### 1a. Decision Deck — hosted v91 (`https://claude.ai/artifact/3mQDm36FUmfUKhE3QMBYrd`) + local `PROME/artifacts/decision_deck.html` (build ca809ca12·2026-10-08 12:10)

| ID | Token | Own-rule? | Finding (file:line → rail it contradicts, with date) |
|---|---|---|---|
| **U1** | URGENT | YES — `PROME/WILL_QUEUE.md:19` artifact-verify-per-presentation; `PROME/CLOSEOUT.md:59` sources (incl. `WQ_EXPLAINERS.tsv`) run at step 7 | `PROME/registry/WQ_EXPLAINERS.tsv:128` (WQ-365, last changed 2026-10-02 18:54) rec = *"PROME recommends approve as conditional … Wait for VULCAN's Monday evidence before saying yes."* vs `PROME/WILL_QUEUE.md:32` Rec *"(replaced 10/7 from TERRY 76c75516b): NOT ARMABLE … TERRY's lean is LAPSE … no re-ask after VULCAN is needed"* (row changed 2026-10-07 23:40). The 10/7 closeout's ARGUS blocking item "WQ-365 rec replaced from TERRY's delivery" fixed the ROW only (8d086bba0 body); the same closeout published Deck v91 with the old card (ORCH_LOG.tsv:816); the 10/8 12:22 closeout re-rendered it unchanged. Hosted and local both show it. Secondary: the row's own first reason *"QQQ never closed back below $748.65"* is false since the 10/8 close 747.58 (`HEARTBEAT.md:24`, [10/8c]); verdict unchanged (leg b not met; kill HY ≤312 printed). Will could tap Approve today on a card both owners say should lapse. |
| **U2** | URGENT | YES — same two rules; class = run-3p **O-NEW-1, REGRESSED** | Hosted Deck: WQ-347 is the FIRST card under "Needs your ruling", pill "2d left · 2026-10-09", headline *"…the five Oct-5 puts need your sell-or-roll decision by Monday 3 pm"* (`WQ_EXPLAINERS.tsv:111`, last changed 2026-10-03 22:35). Rails: Oct-5 735P expired/booked — DOCKET L592 RESOLVED 2026-10-08 11:10; `FORGE/STATUS.md:50,160` (D-72 CLOSED 10/8). Tomorrow's three expiring lines (QQQ Oct-09 755P ×1 ITM, 750C ×1 NEW no card, USO Oct-09 150C ×1; `HEARTBEAT.md:41`) appear on the hosted Deck only inside WQ-347's collapsed raw row; WQ-396/397 are absent from v91 (registered 10/8 11:08). The row itself (`WILL_QUEUE.md:34`) Item/Needed-by/Rec still say *"Oct-09 755P ×2"* and *"Oct-02/Oct-05 disposition UNKNOWN until Activity"* while its own 15:38 tail says both BOOKED and 1 of 2 755P sold (`WILL_QUEUE.md:28` WQ-397 PARTIALLY EXECUTED 15:30). Hosted **Helm** v66 compounds it: Broker actions list the Oct-02 740P and Oct-05 735P as live and the USO 150C with *"exercise $15,000 vs $15,524.70 cash + pending ⇒ headroom ≈ $525"* vs `HEARTBEAT.md:41` *"EXERCISE UNFUNDABLE ($15,000 vs $11,421 cash)"* [10/8 rcv]; no 755P/750C lines. (Helm carries an age banner; the Deck card does not.) |
| S4 | STANDARD | YES — root `CLAUDE.md:58` anti-laundering (caveat that could change the decision survives simplification) + PROME's own row note *"carried here before the verdict is presented"* | `WQ_EXPLAINERS.tsv:146` (WQ-394, changed 10/8 09:03): *"PROME's list of your 370 decisions found one"* vs `WILL_QUEUE.md:30` (changed 11:03): *"370 is a count of classified ROWS, not of distinct decisions … '1' is ONE SUPPORTED qualifying decision … not proof"* (CATO 7494604d1, 10/8). The 12:10 local card drops the caveat; not yet hosted (registered after v91). Needed-by 10/14. |
| S5 | STANDARD | YES — `WILL_QUEUE.md:19` artifact-verify; `:21` leave-at-ruling | WQ-381 (`WILL_QUEUE.md:48`; hosted card `WQ_EXPLAINERS.tsv:143`, needed-by 10/9) asks Will to approve replacing *"(gate advisory)"* in `PROME/CLAUDE.md` boot step 2. That text no longer exists: removed 2026-10-05 by 39178712a (charter compaction under Will-authorized maintenance); `grep -c 'gate advisory' PROME/CLAUDE.md` = 0 and the charter now carries no parity label (`PROME/CLAUDE.md:19`). The decision's object is gone; the row asks anyway. Whether the removal needed the one-label word is PROME/Will's to state, not this reader's. |
| S6 | STANDARD | YES — `WILL_QUEUE.md:19` | `WQ_EXPLAINERS.tsv:120` (WQ-357, changed 10/1 23:28) rec *"I lean to approving"* (the exit) with no mention of Will's 10/3 21:08 LATER tap / TERRY path C, which `WILL_QUEUE.md:33` Rec leads with (*"superseded by Will's LATER tap … HELD on TERRY's path C"*) and `HEARTBEAT.md:15` states. Row Needed-by still says *"BOND's research read by 10/08, DOCKET L608"*; L608 RESOLVED 10/5 (BOND ff0992bf1). |
| S7 | STANDARD | YES — `WILL_QUEUE.md:20` row weight ≤ ~2 KB, "existing rows trim as touched" | Rows touched and grown, never trimmed: WQ-347 7,544 B (touched 10/3, 10/7 ×4, 10/8 15:39) · WQ-357 5,191 B (grew 10/3, 10/5) · WQ-274 5,175 B (grew 10/7). Measured from git history of `PROME/WILL_QUEUE.md`. These are the Deck's "Row as written" blocks. |
| T3 | TRIVIA | no (ARGUS-declared residue 10/8 12:18) | `WILL_QUEUE.md:5` *"Latest ruling pickup: 2026-10-04 22:12 ET"* vs rulings picked up 10/8 (WQ-392/393/395 at 08:45–08:56, WQ-399 at 15:28; `WILL_QUEUE.md:55-58`). |
| T4 | TRIVIA | no | `WILL_QUEUE.md:34` tail asserts the Oct-05 735P lot *"1 sold 10/2"*; the broker view shows no count (`FORGE/STATUS.md:160` "conjecture only"); HEARTBEAT fixed the same wording at result-read ❌2 (plan:74). |
| T5 | TRIVIA | no | `WQ_EXPLAINERS.tsv:144` WQ-382 headline *"eight days stale"* — the reference page was last published 9/26 (12 days at 10/8). |

### 1b. The Helm — hosted v66 (`https://claude.ai/artifact/WPpL1wzzBg3geo1wFhzCXj`, built 2026-10-05 16:38) + sources `PROME/BRIEF.md`, `PROME/HANDBOOK.md`

| ID | Token | Own-rule? | Finding |
|---|---|---|---|
| S1 | STANDARD | YES (disclosed) — `PROME/CLOSEOUT.md:59` "Standard+ mandatory"; `PROME/BRIEF.md:7` "Auto-rebuild + republish at EVERY PROME closeout" | Publication skipped at two consecutive Standard closeouts: 10/7 23:42 (Helm + Fleet-Ops not published; ORCH_LOG.tsv:816) and 10/8 12:22 (Deck, Helm, Fleet-Ops, reference all not published, "named SKIPPED on cost … PARTIAL"; 171c3e48a body). Disclosed and asked of Will — reported, not executed. Meanwhile the manual tells Will the opposite inference: `PROME/HANDBOOK.md:250` *"Both regenerate at every PROME closeout; … an old stamp means canon needs a session, not that the page is broken."* Hosted Helm is 3 days old through 2 sessions; hosted Fleet-Ops is 7.7 days old (10/1 00:40, HEARTBEAT base 9/29, one-liner *"QQQ Oct-01 740P ×9 … SELL OR ROLL by Thu 15:00"*) and the Helm header still links it as "Fleet Ops →". (Fleet-Ops non-publication is by design per run 3p; the manual line and link were not updated to say so.) |
| S2 | STANDARD | YES — `PROME/BRIEF.md:6` (decisions *"generated from WILL_QUEUE — never hand-written here"*), `:7` (*"an old story reads as old, never as current"*) | STORY (`BRIEF.md:154-156`) unchanged since e82222068 (10/3 18:06); QUESTION (`:158-160`) since dd4eac354 (10/3 19:48); FALSIFIER header *"Updated 10/3 afternoon"* (`:164`). WRITTEN re-stamped 10/4, 10/7, 10/8 12:09; the Helm renders QUESTION and FALSIFIER under *"[as written <WRITTEN>]"* (`PROME/tools/will_handbook.py:487-494`) ⇒ 10/3 content certified as 10/8. Contradictions: STORY *"plus five QQQ Oct-5 735 puts that meet your 3:00 pm stop Monday"* vs DOCKET L592 RESOLVED 10/8; STORY *"HY 324 … three-print rules count Friday's cell Monday"* vs `HEARTBEAT.md:18` count 0 of 3 (REG-T-03 owner-graded at the 10/6 cell); QUESTION *"Yours now (WQ-377 · WQ-379)"* vs `WILL_QUEUE.md:7` both RULED 2026-10-04 16:18 ET; QUESTION lists 363·366·367·341·242 *"By 10/9"* — ruled by Deck tap 10/3 21:07–21:11 (`BRIEF.md` WATCH "Added 10/3 evening"); WQ-380 DECLINE 10/4. Hosted Helm v66 shows *"Yours now (WQ-377 · WQ-379)"* stamped *"as written 2026-10-04 21:54 ET"* — 5½ h after both were ruled. |
| S3 | STANDARD | no (tooling; unregistered) | `PROME/tools/will_brief.py:188` keys sections on `^##\s+([A-Z]+)\s*$`, so all 19 `## SINCE THE … BRIEF` sections (`BRIEF.md:20-153`) are absorbed into HEADLINE (45,697 B parsed) and rendered as ONE serif paragraph through `md_inline` (`will_handbook.py:465-467`). Hosted v66 headline paragraph = 40,812 B with 17 literal `## SINCE` markers and 3 escaped literal `<strong>` tags. The parser's empty-section guard passes (PAT-105: nonempty ≠ correct). No DOCKET row found (`grep -i 'SINCE THE'` DOCKET/SCRATCH/STATUS). |
| — | clean | — | `HANDBOOK.md` Top priorities 10/8 12:09 block (`:8-13`) agreed with WILL_QUEUE/DOCKET at its stamp (WQ-314 omitted on purpose, ARGUS-declared); superseded only by the 15:30 fills, which the running closeout owns. |

### 1c. HEARTBEAT.md (28th base, ae483c70f 16:36) + `PROME/HEARTBEAT_COLD.md` anchors + `PROME/HEARTBEAT_DASHBOARD.md`

Every number below re-derived from its rail; all agree unless listed. Arithmetic checks (all ✓): 755P $7.42 ITM (755−747.58) · 750C $2.42 OTM · USO 150C $2.39 OTM · assignment ≈$75,500 · USO 37 × 147.61 = $5,461.57 · HY 11bp under 320 · IG 12bp under 94 · HY<260: 49bp · ROLL70 $6.40 · VLO-HELD A $15.66 · USD/JPY 0.184 · UK 30Y 0.6–0.8bp · 10Y 1.2bp · 30Y 5.660−5.618 ≈ 4bp · Brent +5.0% / +3.6%. Book line (`:39`) = `FORGE/STATUS.md:9,44-48,86-87` ($34,650.69 · cash $11,421.19 · pending +$1,283.98 · qty changes) ✓. Gate cells (`:44-45,52`) = `PROME/GATES.tsv` rows VLO-HELD-01 (A NOT FIRED, last valid 10/7 est ≈$105.8, review 11/18), VLO-SCALE (TERMINAL), ROLL70 (0-of-3), BRK-R2 (consequence RAN), LIQ-069/076, FERT-G5, FALCON-001, NEXUS-SEAT-01 (verdict WQ-394 10/14), NEXUS-T12S, COT-35B ✓. DOCKET pointers L617/L585/L635/L637/L627/L638/L553/L548/L618/L623 match their rows' dates ✓. All 16 cited cold anchors (§28.1–§28.8, §28.B, §KOS.12/-H, §KOS.11, §D.2, §K.1, §19.2R, §C, §B.1) exist ✓. Companion: chain 0, zero projections ✓.

| ID | Token | Own-rule? | Finding |
|---|---|---|---|
| T1 | TRIVIA | no | `HEARTBEAT.md:24` *"QQQ closed BELOW WQ-365's $748.65 level after two closes above"* — three closes above in the card window (756.20 / 759.66 / 757.73, 10/5–10/7; `WILL_QUEUE.md:32`); cold `HEARTBEAT_COLD.md:996` says *"closes above 10/6–10/7"*. Verdict (leg a MET, b not, NOT ARMABLE) unaffected. |
| T6 | TRIVIA | YES — `HEARTBEAT_DASHBOARD.md:4-5` *"Review all affected one/channel/ticker fields when changing source prose"* | Am.#2 projection (fd94a7e12, 11:43) moved the one-liner to HY 309 [10/7] / CCC 1,229 but projected no `ticker` (supported key, `heartbeat_projection.py:67`) and wrote *"No gate, level … changes"*. The 12:21 Fleet-Ops build state (`dashboard_state.json` at 171c3e48a) shows one-liner 309 beside tiles HY OAS 303 / CCC 1,214. Folded at the 28th base; Fleet-Ops not published in the window ⇒ no Will exposure. |

### 1d. Fleet-Ops (generated by `PROME/tools/fleet_dashboard.py`; hosted last 10/1 — see S1)

| ID | Token | Own-rule? | Finding |
|---|---|---|---|
| S8 | STANDARD | no (tooling; unregistered) | 7 of 9 gate-distance tiles render their as-of stamp as **"[?]"** (HY OAS, CCC, 10Y, WAL, OZK, VIX, Cushing) in a preview of the installed 28th base (this reader, 16:44, `--no-snapshot`). Cause: the stress line stamps a GROUP (`HEARTBEAT.md:49` *"HY OAS 309 · CCC 1,229 · … [10/7]"*), `parse_tiles` splits on " · " and inherits a stamp only from the token itself or its " / " group (`fleet_dashboard.py:470-512`). Pre-existing (same grouping at the 10/2, 10/3, 10/7 bases). The page footer claims *"Levels come from … with their [as-of] stamps"*. Distinct from L641 (no Brent tile, registered). |

### 1e. GATES / DOCKET / corrections-register items named in the brief

| Item | Read | Verdict |
|---|---|---|
| WQ-393 (R1 register write leg) | `WILL_QUEUE.md:58` RULED 08:45; DOCKET L210 RESOLVED 11:01 citing WALTER 5b4d3db7e (encode, 09:17) + 0a97008bc (9+2 backfill, 09:17); WALTER 1d9600498 (15:00) a second backfill of 13; `AGENTS/WALTER/registry/CORRECTIONS.tsv` 73 lines | Consistent; the RECENTLY-DONE row still reads "closes on WALTER's encode-confirm" (decision-log row, not a defect). |
| WQ-399 (receipt writer fields) | `WILL_QUEUE.md:55` RULED 15:28, DELIVERED 15:46 (112ccb908 exists, 15:37); L640 registers PROME's own stale command lines (prome_gate.py:1604, BOOT.md:69) for 10/12 | Consistent; known-stale lines are registered, not silent. |
| L380 | DOCKET L380 RESOLVED-REFUTED 15:21 | Not cited on any Will-facing surface; hosted Fleet-Ops (10/1) still lists it OVERDUE — covered by S1. |
| VLO / TERRY gates | GATES VLO-SCALE TERMINAL, VLO-HELD-01 LIVE review 11/18, ROLL70 0-of-3 | HEARTBEAT `:12,44-45,52-53` agree. Hosted Helm v66 VLO-HELD-01 cell reads "through 10/2" — dated, covered by S1. |
| **T2** · TRIVIA · own-rule: no | DOCKET L548 state cell says the apply slot was *"registered as its own row (L627) for 10/12"*; the apply row is `DOCKET.tsv:628`; L627 is the AEOLUS landfall wake. | A stale line pointer that still resolves to a different live row. |

## §2 Prior open findings

| Prior | State at this read | Evidence |
|---|---|---|
| Run #2 (9/08) O1–O3, S1, S2 | CLOSED 9/9; spot-checked, still closed | `HANDBOOK.md:248` ungating label correct; `GIT_COORDINATION.md:90` reconciled 10/3 |
| 3p **O-NEW-1** (stale passed-deadline QQQ action on Deck/Helm) | Closed 10/3 at the bytes — **REGRESSED** as U2 (same row WQ-347, same explainer row 111, after the 10/5 expiry) | `WQ_EXPLAINERS.tsv:111` last changed 10/3 22:35 |
| 3p O-NEW-2 (HEARTBEAT "1 of 3") | Closed; now owner-graded 0 of 3 | `HEARTBEAT.md:18` |
| 3p O-NEW-3, S1, S2 | Closed (S1 re-checked) | `GIT_COORDINATION.md:90` |
| 3p **S3** (Kernel runbook vs root ④) | **Still CARRIED** — runbook unchanged since 0417cd2fe (8/27); HEARTBEAT carries "the WQ-150 root-④ carry" | `KERNEL/GATE_C_C7_RUNBOOK.md:23-25`; `HEARTBEAT.md:36` |
| 3p **S4** (charter "gate advisory") | Label **removed** 10/5 (39178712a) — discrepancy gone; the routed WQ-381 row is now stale → S5 | `PROME/CLAUDE.md:19`; `WILL_QUEUE.md:48` |
| CATO qualification (reference page publication PARTIAL) | Still open: WQ-382 OPEN, needed-by 10/9; reference last hosted 9/26 | `WILL_QUEUE.md:49` |
| L594 Helm fold acceptance | Still PENDING (APPLY-READY 10/8 08:42) | DOCKET L594 |
| L604 / L530 | PENDING (L530 re-dated 10/9) | DOCKET L604, L530 |
| L538 | RESOLVED 10/8 08:42 | DOCKET L538 |
| Hosted UNKNOWN | Resolved this run for Deck Owed, Helm, Fleet-Ops (read); reference page still UNKNOWN | §0 |

## §3 Leg 4 — re-bases since 2026-10-03 and their consumers (PAT-069)

| Surface | Re-based? | Named consumers | Re-ran clean? |
|---|---|---|---|
| `BOARD/INDEX.md` | **No.** 25 commits since 10/3, all `gen_board_index.py` row regenerations (header comment + section counts only; diff from the 10/3 base) | — | N/A |
| HEARTBEAT **27th** base (efef85eae, 10/7 23:11) | Yes | `fleet_dashboard.py` (parser anchors, one-liner, split, tiles) · `heartbeat_projection.py` · Helm builder | **CLEAN.** 10/7 closeout built Helm + Fleet-Ops renders (ORCH_LOG.tsv:816 "renders are built and on disk"); 10/8 12:21 real build `dashboard_build.json` ok=true (171c3e48a body); result reader's parser check (plan 27:73). Residue T6 (am.#2 ticker). |
| HEARTBEAT **28th** base (ae483c70f, 10/8 16:36) | Yes | same | **IN FLIGHT** — the owner's live test is the running closeout build (plan 28:70, :78). Independent preview by this reader 16:44: `fleet_dashboard.py --no-snapshot` rc 0; `dashboard_state.json`/`dashboard_build.json` md5 unchanged before/after; one-liner, NEXUS split (Break 20 · Grind 47 · Unresolved 33) and 9 tiles parse; heartbeat errors none. Known: no Brent tile (L641, registered); 7/9 "[?]" stamps (S8, pre-existing). NOT run (they write state): `will_handbook.py`/`will_brief.py` (snapshot/feed), `prome_gate.py` (advances state) → UNKNOWN until the closeout. Not graded as a defect. |

## §4 One-line asks to PROME (DAEDALUS packets them)

1. **U1** — Before tonight's publish, rewrite `WQ_EXPLAINERS.tsv:128` (WQ-365) to the row's NOT ARMABLE / lean LAPSE rec, and correct the row's "never closed back below" reason after the 10/8 close.
2. **U2** — Re-base WQ-347 (row Item/Needed-by/Rec and `WQ_EXPLAINERS.tsv:111`) to its remaining scope (D-71 only), so Friday's three expiring lines are carried by WQ-397 and its card, not by a Monday headline.
3. **S1** — Publish the Deck Owed + Helm at this closeout, or make `HANDBOOK.md:250` and the Helm's Fleet-Ops link say what Will's stale stamps actually mean.
4. **S2** — Rewrite BRIEF STORY / QUESTION / FALSIFIER at this closeout, or stop stamping them with the new WRITTEN time.
5. **S3** — Register the SINCE-blocks-into-HEADLINE parser defect (`will_brief.py:188`) as a DOCKET row.
6. **S4** — Carry CATO's "370 rows, not decisions" caveat into `WQ_EXPLAINERS.tsv:146` before WQ-394 is first published.
7. **S5** — Re-scope or close WQ-381: the "(gate advisory)" text it asks Will to fix was removed 10/5 (39178712a).
8. **S6** — Put Will's 10/3 LATER / path C and BOND's 10/5 delivery into WQ-357's explainer and Needed-by.
9. **S7** — Trim WQ-347, WQ-357 and WQ-274 to ≤ ~2 KB at this reconcile, moving the detail to their cited records.
10. **S8** — Register the "[?]" tile stamps (`fleet_dashboard.py:470-512` vs grouped stamps) beside L641.
11. **T1–T6** — Fix at next touch: "two closes" → three (`HEARTBEAT.md:24`); L548 → L628; WQ header pickup stamp; WQ-347 "1 sold" → count not shown; WQ-382 "eight days"; project tickers with any amendment that moves a level.

## §5 Limits

- **Hosted:** Deck Owed v91, Helm v66 and Fleet-Ops (10/1) read whole-file via the artifact reader (saved under this session's tool-results; heads inspected, targeted extracts parsed). The Deck **reference** page was not read → UNKNOWN. Reading the pages did not publish, change, or "view-for-republish" anything on PROME's behalf.
- **In flight, not graded:** PROME's 10/8 Standard closeout (`prome-7c`) — SCRATCH/STATUS placeholders, dirty DOCKET/ORCH_LOG/HANDOFF, WQ-396/397 explainers vs the 15:30 fills, BRIEF/HANDBOOK for the afternoon, the 28th base's consumer build and publication. The 28th re-base plan (`PROME/plans/2026-10-08_heartbeat-28th-rebase-PLAN.md`, committed 0c05cb8ab/ae483c70f) was read only to know what is in flight. Findings U1, U2, S2, S4–S7 rest on bytes committed before this sitting began or at its 12:22 closeout, not on the running work.
- **Not run:** `will_handbook.py`, `will_brief.py`, `prome_gate.py` (state-writing); legs 2, 3, 5 of the playbook; live market prices (no price claim here is mine — all are HEARTBEAT/FORGE figures checked for internal arithmetic and rail agreement only).
- **Counting basis:** own-rule-unexecuted counts one per finding, citing the PROME rule (or root rule binding PROME's Will-facing output, S4) left unexecuted; S1 is a DISCLOSED skip and is counted. Row-vs-explainer staleness figure (13/24) is a git-history timestamp comparison, not 13 defects.
- **No commits, no messages, no subagents.** This file is the only write.

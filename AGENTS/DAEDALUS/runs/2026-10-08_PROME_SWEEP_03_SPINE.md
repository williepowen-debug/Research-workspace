# PROME Sweep run #3 — legs 2, 3, 5 (canon meaning · spine · disposition write-back)

**Reader:** DAEDALUS non-owner read-only reader (no edits, stages, commits or messages outside this file) · **Started:** 2026-10-08 16:38 EDT · **Assembled:** 2026-10-08 16:46 EDT (both from `date`) · **Playbook:** `AGENTS/DAEDALUS/sweeps/PROME_SWEEP.md` legs 2, 3, 5 · **Prior records:** `upgrades/PROME_SWEEP_2026-09-08.md`, `upgrades/PROME_SWEEP_2026-10-03.md` (run 3p) · **Companion:** legs 1 and 4 are in `runs/2026-10-08_PROME_SWEEP_03_WILLFACING.md` (not read by this reader).

**Window:** `git log --since=2026-10-03 -- PROME/` = **221 commits / 308 paths** (sized 16:38 EDT). **Sampled, not walked:** 2 canon commits (all of them: `39178712a`, `88417ced3`), 1 CLOSEOUT rule commit (`a441d4fa8`), the 3 most recent completed PROME closeouts (`171c3e48a`, `8d086bba0`, `fbda797eb`) plus `30f188348`/`7d15d5c92` as R1 comparators, 11 disposition chains, every process-file commit in the window (by file filter). PROME was LIVE during the read (prome-7c closeout in progress, `__CLOSE_HHMM__` in STATUS/SCRATCH); its uncommitted bytes are treated as in-flight, never as findings.

---

## §0 Headline

| Token | Count |
|---|---|
| URGENT | 1 |
| STANDARD | 8 |
| TRIVIA | 4 |

**Own-rule-unexecuted: 8** (7 VERIFIED at the artifact; 1 — P3, the WQ-385 Mirror-Map walk — VERIFIED in consequence, INFERRED in non-performance). **Zero is required for PROME's L5 third leg; this run does NOT satisfy it.** Five of the eight are from the last five days (10/04–10/08); three were self-disclosed by PROME (R1 overrun, ARGUS re-review skip, publication skip) — disclosure is not execution, by PROME's own rule (`PROME/CLAUDE.md:72` "disclosure is not authorization").

**Worst finding (URGENT, P1):** CLOSEOUT step 11 publication was skipped on PROME's own cost decision at the last two Standard closeouts (`8d086bba0` Helm skipped; `171c3e48a` all four pages skipped), while PROME's own WQ-382 row says *"Until ruled, CLOSEOUT step 11 stands as written"*. Per the ORCH_LOG PUBLISH row (L816) the hosted Helm was last published 10/5 16:38, before the 10/7–10/8 fills and Friday's three expiring lines. Hosted content itself is UNKNOWN to this reader.

**Strong side (VERIFIED):** the Session Process Controls FREEZE held (12 bullets at every commit since 9/26); WQ-299 R1 executed correctly at 10/5 prome-95 (`7d15d5c92`, one change, named), 10/7 prome-0e and 10/8 prome-fc/prome-7c (ZERO, with L594/L546 deferred behind due domain work); HEARTBEAT's near-dates line row-cites DOCKET correctly (10/10 rows checked); GATES lead tokens agree with today's five-cell fix; 9 of 11 disposition chains are clean at the target artifact.

---

## §1 Leg 2 — does each mirror still MEAN what canon means

Canon moved in the window only through **WQ-385** (`88417ced3`, 10/05 10:37 — root `CLAUDE.md` runtime amendment) and the Will-authorized charter maintenance (`39178712a`, 10/05 08:14). No ROSTER, `_NETWORK.md` or root Git Protocol commit in the window. Twelve `PROME/SYSTEM.md` Mirror-Map rows (`SYSTEM.md:58–70`) walked at the depth stated.

| # | Mirror-Map row | Depth | Verdict | Evidence |
|---|---|---|---|---|
| 1 | Gate C custody / carve-out ④ | Runbook + root ④ re-read | **CARRIED (prior S3)** | `KERNEL/GATE_C_C7_RUNBOOK.md:23` still scopes desk commits to "RULED WINDOW BOUNDS" against root ④'s live/unrevoked test; last commit `0417cd2fe` 8/27; owner carry WQ-150 (HEARTBEAT.md:36 "Owed"). No new drift. |
| 2 | Root-canon provenance | Anchor parity, all 34 `root-anchor:` keys vs current root | **BROKEN — P3** | 2/34 anchors no longer in root after WQ-385: `system-platform` ("serial multi-machine, desktop ⇄ laptop, ONE at a time" → root now "serial multi-machine operation (desktop ⇄ laptop, ONE at a time; …)") and `system-deliver-before-idle` ("final action before going idle" removed). `docs/CANON_PROVENANCE.md:3` says the parity test "fails when an anchor vanishes"; no script invokes it (grep of `scripts/`, `PROME/tools/` = SEARCH-NOT-FOUND outside test fixtures). |
| 3 | Git/push protocol | PROME/CLAUDE.md:55, CLOSEOUT:86–95, GIT_COORDINATION recipe, AUTONOMY header | AGREES | Root Git Protocol unchanged in window; S1 (10/3) repair holds. `scripts/safe-push.sh:117` still prints the root receipt line verbatim. |
| 4 | Machine model / runtime | SYSTEM Prome Runtime + Safety reminders | **DRIFTED — P3** | Root (post-WQ-385): "A desk may run with an OpenAI or Anthropic model"; AGENTS.md: "in Claude Code or Codex". `PROME/SYSTEM.md:76` "Prome runs as a Claude Code session"; `PROME/SYSTEM.md:230` "**All agents are Claude Code sessions** … PROME may spawn domain agents via teams-mode". PROME itself ran a Codex session 10/05 (`30f188348` body). Also TRIVIA T1: `PROME/CLAUDE.md:4` "Prome operating inside Claude Code", `:40` "persistent Claude Code agents". |
| 5 | HY-watch mechanism | Pointer check | AGREES (not re-derived) | No canon change; re-homed 10/02. |
| 6 | Position truth | SYSTEM:177/:199/:210 | AGREES | Root paragraph untouched by WQ-385. |
| 7 | Roster / classification | AGENTS.md operating-model diff | AGREES | WQ-385 edited AGENTS.md in scope; roster authority untouched. README/_INDEX not re-read. |
| 8 | Forward catalyst dates | HEARTBEAT.md:54 near-dates line vs DOCKET | AGREES | L637/L617/L585/L553/L623/L618 = 2026-10-09; L627/L638 = 2026-10-10; L635 = 10/12 cited as "Mon"; L548 cited as a pointer to the VULCAN calendar-read defect (row dated 10/07, owner DAEDALUS/PROME). |
| 9 | Fire-ledger GATES | HEARTBEAT.md:52 vs `8fc5ff0f2` | AGREES | LIQ-069 "2-of-2", BRK-R2 "FIRED twice, EXECUTED", COT-35B consistent with today's five-cell fix. |
| 10 | WILL_QUEUE | Row-level spot (WQ-381, WQ-369, WQ-382) | **ROW MEANING STALE — P6** | See §2; generated SCRATCH view not re-run (would write). |
| 11 | Dashboard projections | Not re-run | NOT-ADJUDICATED | Running renderers writes tracked files; leg 1/4 companion owns. |
| 12 | Trigger bands | config.py:37–46 vs HEARTBEAT.md:18/:53 | AGREES | HY >280 X1 CLOSED 8/28 (config.py:40); HEARTBEAT ">320" is REG-T-03 (different referent, as O-NEW-2 established). |

**PROME/CLAUDE.md vs root ratifications since 10/03 (WQ-385 only):** the in-scope paragraphs agree in meaning — registered-row nod `:49` ("after owner absence is established by the Desk-spawn preflight") and the preflight bullet `:67` match the ruling text verbatim; `:18` auto-injection is runtime-qualified as root requires. The charter's Purpose line `:4` and `:40` are out-of-scope residue (T1). The charter does NOT carry WQ-369's C8 class — see P4.

---

## §2 Leg 3 — spine skim and closeout steps vs execution

### Stamp honesty (header claims vs commits since the stamp)

| File | Header stamp | Commits after it | Verdict |
|---|---|---|---|
| `PROME/BOOT.md:3` | 2026-10-05 WQ-385 (+ Prior 10/05 maintenance) | none | HONEST |
| `PROME/COMPLETION_SPEC.md:3` | 2026-10-05 WQ-385 | none | HONEST |
| `PROME/AUTONOMY.md:3` | 2026-10-05 WQ-385 | none | HONEST as to commits — but the change log (`:80–102`, last row 2026-10-01) lacks the 10/04 WQ-369 C8 grant (P4) |
| `PROME/CLOSEOUT.md:3` | 2026-10-03 14:1x ET | `a441d4fa8` 10/05 16:12 — **new step-9 rule** "Root steps 1c/1d are declaration-gated at every tier (2026-10-05)" (`CLOSEOUT.md:85`) | **RIDE-UNDER — S1** (fourth recurrence of the 9/8 S2 class; spine audit #15 fixed ×5 on 10/02) |
| `PROME/GIT_COORDINATION.md` | 2026-10-02 | `a2009b1ff` 10/03 (the S1 cookbook repair) | RIDE-UNDER (folded into S1) |
| `PROME/MACHINE_LOCAL.md` | 2026-10-02 | `dbec7eaaa`, `493d7c79a` 10/04; `2a72c60bc` 10/05 (new §Fleet safeguards) | RIDE-UNDER (folded into S1); laptop column stale — T2 |
| `PROME/HANDOFF.md` (HEAD) | "10/8 midday laptop sitting is the latest entry" | none committed after `171c3e48a` | HONEST at HEAD; working tree in flight |
| `PROME/SYSTEM.md:2` | 2026-10-02 | none | HONEST as to commits; content drift P3 |

No written PROME rule obligating header-stamp coverage was located (SEARCH-NOT-FOUND for a scope-manifest/stamp rule in live PROME `*.md`; spineaudit SKILL.md:11 classes ride-unders as "minor"). S1 is therefore STANDARD, **not** counted as own-rule-unexecuted.

### Closeout steps vs execution — the last three completed closeouts

| CLOSEOUT step | `171c3e48a` 10/08 12:22 prome-fc Standard | `8d086bba0` 10/07 23:40 prome-0e Standard | `fbda797eb` 10/07 21:05 crash-recovery close |
|---|---|---|---|
| Pre-3 WQ-249 desk ask/receipt | ✅ ORCH_LOG L830–832 + closeout_v1 on 12 morning rows | ✅ TERRY/FALCON/REGINALD/FERT ASKED→receipt | ✅ BOND/BRENT/WALTER owner receipts |
| 1 GATES+DOCKET, view regen | ✅ GATES/DOCKET in commit | ✅ | ✅ DOCKET |
| 2 WILL_QUEUE + ledger | ✅ ledger sync 3 events | ✅ WQ_LEDGER | ✅ WQ_LEDGER |
| 3 SCRATCH/STATUS/AD/HEARTBEAT/HANDOFF | ✅ HEARTBEAT stated no-op | ✅ | ⚠️ "fresh HEARTBEAT synthesis skipped and still owed" — discharged 23:11 (`efef85eae`) |
| 6 root 1b–1e | ✅ claimed in body | ✅ claimed | ✅ declarations |
| 7 renders before freeze | ✅ deck/reference html in commit | ✅ dashboard_state | ✅ |
| 8 FREEZE → ARGUS → ❌ fix → **re-review changed portion** → mark | **❌ P2:** 4 ❌ fixed, "re-verified by grep only - unreviewed by a reader", then `--mark-reviewed` wrote REVIEWED (`2e39742b3:PROME/state/argus_review.json` reviewed_note) | ✅ 7 fixed, REVIEWED | ✅ "scoped check 0 blockers" after fixes |
| 9 gate `--tier` + declarations | ✅ (body) | ✅ PASS 16/16 rc 0 | ✅ rc0 15/15 |
| 10 commit → verify → push | ✅ on origin | ✅ receipt c9b5c13f4 | ✅ |
| 11 publish Helm + Deck Owed + reference | **❌ P1:** none published, "named SKIPPED on cost" | **❌ P1:** Owed only; Helm "Decided by PROME" not published (ORCH_LOG L816) | ⚠️ native Artifact unavailable in that runtime (a real blocker, PARTIAL disclosed) |
| 12 ARGUS baseline after commit | ✅ `2e39742b3` | ✅ `a2772f8c4` | ✅ |

Comparator: `30f188348` (10/05 prome-95) DID run the changed-portion re-review after ❌ fixes ("Changed-portion re-review (same ARGUS) 17:5x ET: ❌0 ⚠️3") — so P2 is a lapse, not an impossible step.

### Own-rule-unexecuted instances (the L5 count)

| ID | Token | Rule PROME wrote | What happened (artifact) | Self-disclosed? |
|---|---|---|---|---|
| **P1** | **URGENT** | `PROME/CLOSEOUT.md:96` step 11 publish (Standard+), "a failure here is reported, never waived"; `PROME/CLAUDE.md:70` "Cost and time are reasons to ASK whether to skip, never reasons to skip silently"; PROME's own WQ-382 row (`WILL_QUEUE.md:49`): "Until ruled, CLOSEOUT step 11 stands as written" | `8d086bba0`: Helm not published, "Decided by PROME under the Pre-closeout item-5 rule" (ORCH_LOG L816); `171c3e48a`: Owed, Helm and reference all skipped "on cost", asked of Will *in the closeout report* (after the skip). Hosted Helm last published 10/5 16:38 per L816; book changed 10/7–10/8 (FORGE `ef2bc83f1`), three lines expire Fri 10/9. WQ-382 (due 10/09) was widened 10/7 to cover the Helm by PROME's rec only. Same shape as CATO PC1 (a recommendation carried as a grant). | Yes — PARTIAL disclosed |
| **P2** | STANDARD | `PROME/CLOSEOUT.md:82` "Any ❌ fix ⇒ re-review the changed portion … `--record-review` again, and re-mark" | `171c3e48a` body + argus_review.json reviewed_note: fixes "re-verified by grep, unreviewed by a reader", marked REVIEWED; gate passes on the label | Yes |
| **P3** | STANDARD | `PROME/CLOSEOUT_PROCEDURES.md:23` (Chunk 3, any tier) "Canonical doc changed → walk its Mirror-Map row BEFORE commit" | WQ-385 changed root; Machine-model mirror `SYSTEM.md:76/:230` and provenance anchors (§1 rows 2, 4) left contradicting root. No walk recorded in the ruling, `reports/2026-10-05_runtime-compatibility-results.md`, or either independent review (grep SYSTEM.md / mirror / consumer_check: SEARCH-NOT-FOUND). The ruling's eight-file edit scope does not waive the walk; an out-of-scope mirror becomes residue or a row, neither exists. | No |
| **P4** | STANDARD | `PROME/CLOSEOUT_PROCEDURES.md:26` "Autonomy change → AUTONOMY.md log + propagate to `PROME/CLAUDE.md` Ask-First" | WQ-369 narrow C8 RULED 10/04 (~20:00 ET; `WILL_QUEUE.md:61` "Charter encoding/review remains OWED"). AUTONOMY change log last row 10/01; `PROME/CLAUDE.md:53` still says C1–C7 and "⛔ Nothing else moved"; no DOCKET row for the owed encoding (SEARCH-NOT-FOUND). C8 exercised ≥4 times: AEOLUS 10/08 morning (`37ab84a7b`), CORAL + AEOLUS-2 11:49 (ORCH_LOG L831–832), BRENT-pm 16:34 (L837). Authority is real (Will's word, verified relay `8a2dbfa65`); the boot-read charter misstates it. Recurrence of run #1's W3 class. | Partly (row says OWED) |
| **P5** | STANDARD | PROME's own write-back commitment at DOCKET L600 col4: "Execution of the retirements/reclassifications = PROME's next registrar touch" (WQ-379 b1/b2, RULED 10/04 16:18) | 48 DOCKET commits since the ruling; target rows carry no WQ-379/TOMBSTONE/FOLD/RECLASSIFY text: L359, L360 (TOMBSTONE—SUPERSEDED), L473 (FOLD into L488), L381 (RESOLVE), L350, L442 (RECLASSIFY) — still `PENDING — OVERDUE`. They keep inflating the OVERDUE count PROME reports, and the (b2) reclassification out of the R1 ceiling is unrecorded at the rows. (L358/L403/L390 correctly wait for spine audit #16; L413 waits for VIOLET.) | No |
| **P6** | STANDARD | `PROME/CLOSEOUT.md:52` WILL_QUEUE "a row leaves OPEN the moment it stops needing him" | WQ-381 (`WILL_QUEUE.md:48`) asks Will on 10/09 to replace "(gate advisory)" in PROME/CLAUDE.md Boot step 2; that label was removed by PROME's own Will-authorized maintenance `39178712a` on 10/05 (pre-image line 29 vs current file: no "advisory"). Prior S4 is closed at the artifact; the queue row is overtaken. | No |
| **P7** | STANDARD | `PROME/CLAUDE.md:67` WQ-385 Desk-spawn preflight: "same-minute … evidence"; "A partial, stale … result is UNKNOWN … Unknown ownership withholds a new writing launch" | ORCH_LOG L830 HANS "ListAgents 11:40 + host snapshot 11:41 … a 1–2 minute gap to launch, not same-minute"; L831 CORAL and L832 AEOLUS "a 4–5 minute gap to launch, not same-minute". Three desk-writing launches on stale evidence; labels corrected after ARGUS caught "same-minute" claims. No collision observed. | Yes (after ARGUS) |
| **P8** | STANDARD (historical) | `PROME/CLAUDE.md:72` WQ-299 R1 "a CEILING of ONE change per session … disclosure is not authorization" | `a2b6523bd` (10/04): "Session total = THREE process changes vs a ceiling of one (second overrun, disclosed, not authorized)" for the 10/03 prome-ed session (the third, the GIT_COORDINATION cookbook repair, landed in `a2009b1ff`, inside this window). Run 3p logged the earlier part as interval evidence; the full count postdates it. | Yes (after CATO PC2) |

### Other STANDARD / TRIVIA (not own-rule)

| ID | Token | Finding | Evidence |
|---|---|---|---|
| S1 | STANDARD | Header stamps ride under rule changes, fourth recurrence: CLOSEOUT (the 10/05 step-9 declaration rule), GIT_COORDINATION (10/03 cookbook), MACHINE_LOCAL (three commits incl. the new §Fleet safeguards). Spine audit #15 fixed this class ×5 six days earlier. | §2 stamp table |
| T1 | TRIVIA | `PROME/CLAUDE.md:4` and `:40` still describe PROME and peers as Claude Code sessions (outside WQ-385's named sections; same root cause as P3). | file lines |
| T2 | TRIVIA | `PROME/MACHINE_LOCAL.md:34–35` laptop column "UNKNOWN: not inspected or installed" after two laptop sittings (10/07 prome-0e, 10/08 prome-fc). `scripts/safe-push.sh:47` runs `install-git-hooks.sh` and aborts if unverified, so native hooks were INFERRED installed by the laptop pushes; the user-scope Claude dispatcher row is genuinely unknown. | file lines; `2a72c60bc` |
| T3 | TRIVIA | WQ-369 RECENTLY DONE row cites its source at `PROME/inbox/2026-10-05_from-WALTER_…`; the packet is in `PROME/inbox/processed/`. | `WILL_QUEUE.md:61` |
| T4 | TRIVIA (in flight) | `8fc5ff0f2` body says "STATUS carries the answer line (DONE WHEN)"; no such line in HEAD or working-tree STATUS at 16:4x. Immaterial: all five asks were fixed, which meets DONE WHEN by itself. Re-check after prome-7c's closeout lands. | `git diff -- PROME/STATUS.md` |

---

## §3 Leg 5 — disposition write-back sample (PAT-032)

Eleven chains, chosen across kinds (two RULED proposals, Will rulings relayed by a peer, desk deliveries, DAEDALUS packets, a registrar ruling). Each checked at the TARGET artifact named by the ruling or packet.

| # | Item | Lands where (per its ruling/packet) | Verdict |
|---|---|---|---|
| A | WQ-385 runtime compatibility (`proposals/2026-10-05_runtime-compatibility-RULED.md`) | RULED banner `:7–12`; RECENTLY DONE `WILL_QUEUE.md:66`; implementation `88417ced3` | CLEAN write-back; mirror defect is P3 |
| B | WQ-386 VLO December rule (`proposals/2026-10-07_VLO-december-management-RULED.md`) | banner `:3`; GATES `GATE-TERRY-VLO-HELD-01` (GATES.tsv:21); TERRY encode (`AGENTS/TERRY/STATUS.md:43`); RECENTLY DONE `:63` | CLEAN |
| C | WQ-369 C8 (WALTER relay `processed/2026-10-05_from-WALTER_WQ-369-RULED…`) | RECENTLY DONE `:61` ✅; charter + AUTONOMY encoding "OWED" | **GAP — P4** |
| D | WQ-395 OZK-09 reading | RECENTLY DONE `:56`; OZK packet `AGENTS/OZK/inbox/2026-10-08_from-PROME_WQ-395-RULED…` present; DOCKET L635 | CLEAN |
| E | WQ-399 receipt writer (DAEDALUS delivery) | RECENTLY DONE `:55`; WALTER fleet packet `cabe3be41`; L640 registered (10/12) for PROME's own stale receipt lines | CLEAN |
| F | DAEDALUS sweeps packet 10/08 (Gate-Basis #2) | five GATES cells fixed `8fc5ff0f2`; FERT packet in `AGENTS/FERT/inbox/` | CLEAN (T4 cosmetic) |
| G | WALTER L546 intake patch | DOCKET L546 col4 records the DAEDALUS half, PROME's two FORGE instances, slot ZERO today | CLEAN (deferral recorded; row goes overdue 10/09) |
| H | WALTER EDGAR entity-class mis-tag (10/04) | DOCKET L610 dated 10/09 | CLEAN |
| I | BRENT L297 OPEC+ grade (10/04) | L297 RESOLVED; successor L609 2026-11-01 | CLEAN |
| J | WQ-379 process backlog (b1/b2) | target DOCKET rows per L600 | **GAP — P5** |
| K | DAEDALUS 10/03 judgment review → S4 | WQ-381 OPEN | **STALE — P6** (S4 itself closed at the artifact) |

**8 of 11 CLEAN at the artifact; 3 gaps (C, J, K), all PROME registrar write-backs, none a lost Will word.** Sample, not a rate.

---

## §4 Prior findings — still open or closed

| Prior | Source | Status 2026-10-08 | Evidence |
|---|---|---|---|
| 9/08 O1–O3, S1, S2 | run 2 | CLOSED (unchanged) | FLEET_MAP_HISTORY.tsv:216 |
| 10/03 O-NEW-1, O-NEW-2, O-NEW-3, S1, S2 | run 3p | CLOSED (unchanged; not re-tested beyond S1's cookbook) | run 3p follow-through |
| 10/03 S3 KERNEL runbook vs root ④ | run 3p | **OPEN — CARRIED** to WQ-150 / next Kernel touch | runbook :23 unchanged since 8/27 |
| 10/03 S4 charter "(gate advisory)" label | run 3p | **CLOSED at the artifact** by `39178712a` (10/05); the queue row WQ-381 is now stale → P6 | §2 P6 |
| CATO PC1 (reference nonpublication) | 10/04 qualification | **OPEN and WIDENED** → P1 (now the Helm and Owed as well) | ORCH_LOG L787, L816; `171c3e48a` |
| CATO PC2 (R1 session count) | 10/04 | Disclosed; counted here as P8 | `a2b6523bd` |
| L594 Helm fold | run 3p | OPEN — APPLY-READY, correctly deferred under R1 while due domain work exists | DOCKET L594 col4 |
| L604 spawn-slate B1/B2 | run 3p | OPEN — SCHEDULED on the WQ-379 (c) day, which is "not yet scheduled" (`WILL_QUEUE.md:62`) | DOCKET L604 |
| L530 / L538 wording | run 3p | Not re-checked (out of this reader's legs) | — |

---

## §5 One-line asks to PROME (DAEDALUS to packet; STRICT_TEXT-shaped)

1. **P1:** Publish the Helm and Deck Owed at the next Standard closeout, or obtain Will's ruling on WQ-382 before skipping again; DONE WHEN a PUBLISH row names both versions or WQ-382 is ruled.
2. **P2:** Re-review the four ❌ fixes in `171c3e48a` with a reader, or record them as UNREVIEWED in `argus_review.json`'s successor note; DONE WHEN the receipt no longer reads REVIEWED over unreviewed bytes.
3. **P3:** Walk the Machine-model and Root-provenance Mirror-Map rows against WQ-385; DONE WHEN `SYSTEM.md:76/:230` and CANON_PROVENANCE anchors `system-platform` / `system-deliver-before-idle` agree with root or a dated residue row names them (root and provenance edits stay Will-gated).
4. **P4:** Log WQ-369 C8 in `PROME/AUTONOMY.md`'s change log and register the owed charter encoding as a dated DOCKET row; DONE WHEN both exist.
5. **P5:** Write the WQ-379 (b1)/(b2) dispositions onto L359, L360, L473, L381, L350, L442 (and the other reclassified rows); DONE WHEN each row's state cell cites WQ-379.
6. **P6:** Move WQ-381 off OPEN with the `39178712a` evidence, before Will's 10/09 sitting; DONE WHEN the row sits in RECENTLY DONE.
7. **P7:** Launch a desk-writing spawn only inside the same minute as its preflight, or re-run the preflight; DONE WHEN the next ORCH_LOG spawn rows show same-minute evidence.
8. **S1:** Re-stamp CLOSEOUT, GIT_COORDINATION and MACHINE_LOCAL headers to cover their 10/03–10/05 commits; DONE WHEN each header names its newest rule change.

---

## §6 Limits

- **Coverage:** 221 commits sized, not walked. Spine docs read: PROME/CLAUDE.md whole, CLOSEOUT.md whole, SYSTEM.md Mirror Map and runtime sections, CLOSEOUT_PROCEDURES Chunk 3, headers of BOOT/COMPLETION_SPEC/AUTONOMY/HANDOFF/STATUS/MACHINE_LOCAL; BOOT, COMPLETION_SPEC and AUTONOMY bodies were NOT read whole. Root CLAUDE.md read via the WQ-385 diff plus the current injected text.
- **Mirror rows 5, 6, 7, 11** checked at pointer depth or not adjudicated (row 11 needs renderers that write tracked files). README.md, `AGENTS/_INDEX.md`, the ORCHESTRATION_PLAYBOOK body and the five thematic pages were not read.
- **Hosted pages:** not read (no authenticated access). P1's staleness is from PROME's own PUBLISH rows, not a hosted inspection. Whether prome-7c's in-progress closeout publishes is UNKNOWN.
- **P3 non-performance** is INFERRED from the absence of any walk record plus the surviving contradictions; the contradictions themselves are VERIFIED.
- **P7:** whether the morning 10/08 wakes (L817–L828, one preflight at 08:10 for eight launches) met "same-minute" is UNKNOWN — the rows carry no per-launch time; not counted.
- **R1 audit** covered 10/03 (via CATO/PROME's own count), 10/05 (both sessions), 10/07, 10/08; 10/04 sessions not reconstructed.
- **In-flight exclusions:** PROME's dirty working tree (HANDOFF, SCRATCH, STATUS, STATUS_HISTORY) and WALTER's dirty files were not judged. T4 should be re-checked after PROME's closeout commit.
- No commands that write state were run (no renderers, gate, view generators); `measure.py` only read files.

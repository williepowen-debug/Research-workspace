# PROME FULL-DIRECTORY AUDIT — 2026-07-28

> 🗄 **DATED AUDIT/WORK RECORD (last content 2026-07-28; bannered 2026-08-17, self-audit F5).** Findings were routed at write time; this doc is history, not a live queue. Closure state of individual findings lives with the owning agents.

**Directed by:** Will (in-session) · **Method:** Mode-A 4-reader fan-out (spine / rails / tools / flow) + DAEDALUS meta-layer checks · **Scope:** all of `PROME/` (309 files; archive/ at boundary level) · **Posture:** strictly READ-ONLY — PROME ran live during the audit (6+ commits this morning); every fix below is a proposal routed via packet, zero PROME files touched.
**Verbatim reader reports:** `upgrades/PROME_AUDIT_2026-07-28_readers/` (4 files — the full 60+ finding tables with quoted fragments and verified negatives). This doc is the synthesis + ranked action view.

---

## 1. VERDICT

**PROME is well-built and honestly kept; its failure mode is not decay but LAG — checks and mirrors that exist and are not walked at change time.** All four readers converged on this independently:

| Reader | Their one-line diagnosis |
|---|---|
| Spine | "The failure mode is not decay of structure; it is **lag**. Every 🔴 is a mirror a canon change didn't sweep." |
| Rails | "The rails are honest but **under-scanned** … the failures are *unexecuted checks*, not missing structure." |
| Flow | "The debt is **disposition write-back** (PAT-032), one concentrated class … root rule #10 failing at its last leg." |
| Tools | "Wiring is genuinely **above fleet norm** … the headline is a live silent regression" (parsers, not architecture). |

This is the same diagnosis that produced root canon step 1d ("detection was never the gap; **invocation** was") — now observed at the coordinator itself. Positive findings worth naming: **zero >60d retirement candidates** (oldest in-scope content 32d — research-retirement hygiene fully compliant), **zero dangling file/tool references** (38/38 cited paths exist), **zero OpenClaw/VPS vestige**, all three executables genuinely wired with cadence homes, inbox healthy (1 unprocessed item, 1d old), public-prep **clean of sensitive residue** (0 pattern hits), and Mirror-Map/two-state-banner discipline mostly real.

---

## 2. URGENT — wrong-now items that touch TODAY's operations (all → PROME packet, sent 7/28)

| # | Item | Evidence | Why now |
|---|---|---|---|
| U1 | **Fleet-Ops dashboard artifact is live-degraded on the recorded URL.** 3 of 4 regime panels blank: one-liner empty since 7/24, channels+ticker+gate-tiles zero since the 7/28 04:32 build. Root cause: the weekend HEARTBEAT re-base changed formatting three `fleet_dashboard.py` parsers key on (number-inside-bold at :245; quote-chars-required at :236; blank-line-after-heading at :253). Republished degraded by `2a851a82`. Degradation reads as "quiet day." | tools #1–4, regression pinned in dashboard_state.json git history (`ch=6`→`ch=0`, `lv=12`→`0`, `one=47`→`0`) | Will reads this page; FOMC is tomorrow. |
| U2 | **DOCKET row 37 (FOMC, today) carries the figure class canon banned this morning** — "hold ~70-81% priced; Polymarket Oct 44% > Sep 37%" vs SCRATCH caution #2 "No July-hike probability may be cited without a page-stamp… VIOLET's 65.7/34.3 [7/27] is the only valid post-collapse datum." DOCKET is declared canonical over SCRATCH, so the ledger currently out-ranks the ban. | rails #3 | Today's event; the canonical surface wins drift disputes. |
| U3 | **GATES.tsv boot-scan hole:** `GATE-LIQ-069` state = `ARMED …` — outside the file's own STATES vocabulary, so BOTH boot scans (FIRED-UNEXECUTED → block; LIVE+stale → flag) are blind to a gate 1-of-2 legs from consequence, `last_checked` 11d. Same defect class as the two bare-date cells PROME fixed in `351491e8` — different token, so the 7/28 fix didn't close the class. Plus 3 LIVE rows 8–11d past the file's own >5d rule with zero spine flags. | rails #1–2 | A near-trigger gate is invisible to the scan that exists to see it. |
| U4 | **DOCKET row 56 overdue and feeding today:** First Brands ballot CERTIFICATION (7/27, PENDING ungraded) is the stated predicate of today's row-36 trial-open read. Also row 20 monolines window closed 7/22, 6d ungraded (SYF/COF = 0 hits across PROME rails). | rails #6–7 | The 7/28 read is being taken without its stated predicate. |
| U5 | **Two PROME surfaces still publish the FORGE pairing root canon retired TODAY** (`STATUS.md+PORTFOLIO.md` as live mirror): `SYSTEM.md:162,195` and `action-cards/TEMPLATE.md:11` (every future card inherits it). This is a consumer_check miss **on the adoption's own dogfooding day — the publisher checked its consumers and not itself.** | spine #1, rails #5 | Same-day canon change; TEMPLATE propagates forward. |

## 3. STRUCTURAL — the five load-bearing fixes (→ PROME packet; batched, not urgent-today)

| # | Fix | Evidence |
|---|---|---|
| S1 | **Wire a mirror-walk into the canon-change ritual.** All four spine 🔴s are the three carve-out ratifications (7/23/25/27) + the 7/28 PORTFOLIO correction reaching PROME's mirrors partially or not at all — including PROME's own always-loaded CLAUDE.md git ¶ (stamped 7/1, carries none of ①②③) and CLOSEOUT missing root steps **1c (consumer_check)** + **1d (memory_index_check)** entirely (grep: `consumer_check` = 0 hits in all of PROME/). The Mirror Map exists (SYSTEM.md:52-55); it isn't walked on change. Also: n=3 on the STATUS HEARTBEAT-amendment-count row rotting across consecutive re-bases (3rd time ~1.5h after re-sync) — hand-mirroring has failed as a control; generate that row from HEARTBEAT's own amendment headers or reduce to a pointer. | spine #1–4, rails #4 |
| S2 | **COMPLETION_SPEC.md is missing the teams-mode delivery contract** — defines file + task-output delivery only; zero occurrences of `SendMessage`/idle. Root canon mandates SendMessage-to-coordinator AND own-dir write as the final action before idling. Measured cost already in HANDOFF.md:9 ("5 non-delivering spawns in one night"). **Live corroboration during this very audit:** all four DAEDALUS readers idled without delivering; two delivery re-requests each were needed before content landed. Also: no Created/Updated stamp — the spec cannot be staleness-checked. | spine #8; this session's own spawn log |
| S3 | **board_scan.py `--audit` false zero is load-bearing; `--advance` is lossy on its exceptional path.** 572/619 BOARD files use the legacy `to:` schema the parser can't see → BOOT.md's "0-of-605 all-time" is a parser artifact. Cursor writes BEFORE the rc=1 return → an interrupt orphans the flagged ACTION signal irrecoverably. | tools #5–7 |
| S4 | **Extend `spine_audit.workflow.js` GROUPS** — it omits HANDOFF.md (BOOT step 1! and a 40KB append-on-top doc, exactly the rot profile its own L90 names), AUTONOMY, MACHINE_LOCAL (named as a CANON anchor it never audits), COMPLETION_SPEC. The audit's blind spot and this audit's 🟡 residue are the same file set — PAT-035's signature. Also: hardcoded `/home/willi/Research-workspace` repo root (only tool of three not deriving it; serial multi-machine hazard). | spine #12, tools #9–11 |
| S5 | **Close the re-base/disposition write-back class at the ritual, not per-file:** all five flow 🔴s are completed things still advertising open Will-gates (two consecutive HEARTBEAT re-base drafts left "pending approval" after shipping; skills-roadmap advertising a gate DAEDALUS adjudicated 7/8; freshness-build "IN PROGRESS" 27d after shipping; four-rail runbook header "DRAFT" over a completed execution log). Fix = a "stamp the consumed draft" step in CLOSEOUT's re-base sequence + disposition banners on the five files. | flow 🔴 ×5 |

## 4. MEDIUM / HOUSEKEEPING (→ PROME packet, fold at convenience)

- **MID_JULY_NODE.md:** archive now (own retire date ~8/1; FOMC knot resolves tomorrow) — but fold the four packet outcomes to memory/ first: Packet-A delivered 4d early + B/C products exist on disk while the tasking table still reads all "○ out" and all 15 knot items "○ pending" (root rule #10, 14–18d). Its companion `artifacts/mid_july_convergence.html` retires jointly (note: it's a published claude.ai artifact — deleting the file does not unpublish the URL).
- **ROSTER.md:** 8 of 30 ACTIVE rows carry placeholder counts deferred to the same unrun activity pass (oldest 18d); header "Last verified 6/27" (31d). One command clears all 8 — **and my FLEET_MAP grades for those agents are blocked behind it (PAT-019).** WP-W2 stale-valuation line needs an owner+date (textbook `consumer_check --old $68.93 --new $73.92`).
- **ACTIVE_DECISIONS.md:** rows 42–44 are 40d past expiry against the file's own removal rule (self-flagged 12d ago); row 37 public-flip is a 28d undated deliberate-wait (give it a review date); row 50 restates DAEDALUS's inbox state instead of citing it (PAT-006 — was false while the 7/27 canon packet sat unprocessed).
- **DOCKET.tsv:** HEN-42 resolver dated Saturday 8/29 (impossible; the file itself caught this class on 7/24 — add weekday assertion to `firetime_check.py` for resolver dates); row 31 out-of-vocab state + falsified "HENRY dark since 7/17" clause (HENRY committed 7/23, 7/27, 7/28×5); row 46 carries the dead "7/25-28 marks window" premise its own line-5 RE-DATE RULE says to sweep (also in MID_JULY_NODE:31); GEX −$38.4B (row 61) vs HEARTBEAT A#2 −$34.4B — reconcile to HENRY's owner value, then cite the owner (PAT-006); mtime-based staleness line in header → fold into the canon ruling I sent this morning (DOCKET's real freshness signal is its per-row dates — demote the mtime line).
- **STATUS.md Work-Queue line 50:** HY 271 [7/15] dead figure on an unbannered surface (SCRATCH carries 279 [7/24], 1bp from FT-01 exit) — `finding_state_token_sweep_all_surfaces`.
- **GATES.tsv:** HY 277 [7/23] vs 279 [7/24] in adjacent rows, same `last_checked` (reconcile-to-one-figure); FALCON sinking-watch window expired 7/26 undispositioned + FIRED-token vs LIVE-content scan-invisibility (same class as GATE-VIO-116).
- **archive/ boundary:** BOOT.md boot-reads two paths INSIDE archive/ — including `HANDOFF_2026Q2.md`, 212KB, appended TODAY. A live session-critical file under a name that tells every agent it's dead; and archive/ has no live index (the index file is itself archived). Document the live-reads carve-out at the boundary or move the live files out.
- **SYSTEM.md:154 vs 197** consumer-wiring contradiction one screen apart; **:29** "19/20 agents" stale denominator; **:42/:145** advertise FLEET_SCAN as live/rebuildable vs CLOSEOUT:258 "Don't touch — superseded"; **ORCHESTRAL_LAYER_DESIGN.md** roster arithmetic two generations stale (21 vs 30) and its central deliverable superseded by a dashboard it never names.
- **PROME/inbox has no unconditional boot-read step** despite being "the SOLE PROME delivery surface" (schedule exists only inside conditional step-6); `dashboard_parked.tsv` unwired with its only row 12d expired; `codex/` lane live-but-dormant 19d with no trigger home; MACHINE_LOCAL hostname question open 27d; HANDOFF entries violating their own one-line-referent rule (40KB in 56 lines); PAT-031 cwd-wrap missing on 6 runnable lines (BOOT:16,72 · SYS:155-156,183 · CLO:56,77,159); COMPLETION_SPEC routing example still points First-Brands→WAL exposure at REGINALD (WAL promoted 7/25); AUTONOMY Tier-1/Tier-2 research-spawn overlap; PROME/CLAUDE.md boot-order summaries omit GATES.tsv (the blocking co-read).

## 5. DAEDALUS-LANE ITEMS (mine, not PROME's)

| Item | Disposition |
|---|---|
| **PROME is outside the maturity system entirely** — no FLEET_MAP row, no profile, and `maturity_scan.py:30,60` lists `AGENTS/` only, so the root-level coordinator is structurally invisible to the scanner (fleet-level PAT-020). FLEET_DIRECTORY documents "un-graded → blank cells" at the render layer, but I can find **no ratified provenance** (SPEC/EVOLUTION/Will ruling) for the exemption. The asymmetry: SPEC §oversight says "no agent grades only itself" — I'm in the map PROME examines; PROME is in no map at all. | **WILL CALL** (§6 below). If graded: Meta class, judgment-read only (the scripted floor can't glob it anyway). |
| No `profiles/PROME.md` despite PROME being the fleet's heaviest coordination surface (309 files). | This audit + the 4 reader reports ARE the raw material. Build the profile at the disposition pass — cheap now, expensive later. |
| **FLEET_SCAN rebuild re-entry path:** SYSTEM.md:42/:145/:185 + ORCHESTRAL_LAYER_DESIGN §46-108 still advertise rebuilding a "fleet stale-state scan and ranked candidate moves" — that scope is FLEET_MAP/FLEET_DIRECTORY territory (BOOT.md:76 already repoints correctly). The vestigial design doc is the live re-entry path for a duplicate maturity surface. | **I formally object to any rebuild** (recorded here + in the packet); proposed fix is pointers at ROSTER+FLEET_MAP. |
| ROSTER activity pass blocks 8 FLEET_MAP grades (PAT-019). | Asked in packet. |
| My own spawn prompts for this audit omitted the deliver-before-idle SendMessage contract — same gap as COMPLETION_SPEC (S2). All four readers idled undelivered; cost ~6 round-trips. | Owned. Encode in my spawn-prompt discipline + it strengthens S2's case with same-day n=5 (PROME's 4 + mine). |
| Patterns banked off this audit: **PAT-068** (canon-change must mechanically walk the mirror map INCLUDING the mover's own surfaces — publisher-self-blindness is the n=2 extension of PAT-066) · **PAT-069** (a parsed doc's FORMAT is an interface; a re-base/schema migration is a breaking change to every format-consumer — fleet_dashboard×3 + board_scan legacy-schema, two same-class instances in one week, cost = Will-facing artifact degraded 4d). | PATTERNS.tsv rows added 7/28. |

## 6. QUESTIONS FOR WILL

1. **Should PROME be graded into FLEET_MAP** (Meta class, judgment-read, same treatment DAEDALUS gets) — or formally exempted with the exemption recorded in SPEC/EVOLUTION so the blank cells have provenance? My recommendation: **grade it.** This audit is 80% of the first read already, and "no agent grades only itself" should cut both ways.
2. The **FLEET_SCAN rebuild objection** (§5) — ratify the pointer rewrite so the duplicate-surface re-entry path closes?

## 7a. ARCHITECTURE ASSESSMENT (added 7/28 eve, Will's ask — the design-level view, distinct from the findings)

### What is genuinely well-designed (do not change)

| Element | Why it's right |
|---|---|
| **Boot/closeout as separate docs with an explicit symmetry table** | Only agent in the fleet that formally pairs every boot-read surface with its closeout-write. The table lagging is an execution problem; the table existing is the right design. |
| **Mirror Map (SYSTEM.md:52-55)** | Explicitly enumerating where facts are mirrored is rare and correct — it's what made today's audit cheap. |
| **Self-audit tooling (`spine_audit.workflow.js`)** | PROME is the only agent that audits its own spine on a cadence. Extend its net (S4), don't rethink it. |
| **Ledger-first drift rule** (DOCKET canonical over prose; decisions on ledgers — applied again today for the structural batch) | The single best anti-rot decision in PROME's design. |
| **AUTONOMY.md tiering** | An explicit, versioned delegation contract with Will. No other agent has one; it's why PROME can act fast without scope anxiety. |
| **Root-level placement** | PROME genuinely is different (Will-scoped shared-doc steward, no market book). Forcing it into `AGENTS/` shape would be false symmetry. The scanner should learn to *see* it (Q1); PROME shouldn't move. |
| **Incident response culture** | Today: verify-live → fix → adopt fail-loud guards → republish in ~20 min, plus an unprompted self-found fix in the same window. The org works. |

### The three structural tensions (design-level, not point defects)

**T1 — Highest change-rate agent × most mirror-heavy architecture.** PROME mirrors root canon, HEARTBEAT, position truth, agent states, roster facts. Mirror rot rate ∝ change-rate × mirror-count, and PROME maximizes both — which is why every 🔴 today was a mirror, and why the STATUS amendment-count row beat hand-mirroring three times in a row. The Mirror Map treats walking as discipline; at PROME's change-rate it must be mechanism (S1, accepted). The deeper move: **shrink the mirror surface itself** — audit each Mirror-Map row with "could this be a pointer?" Every mirror that exists for reading convenience rather than operational necessity is standing debt. Pointer > mirror wherever load-bearing.

**T2 — Protocol mass exceeds single-session execution capacity.** ~1,200 lines of protocol spine across 12 docs (fleet norm: 100-300). The evidence it's past the edge: root steps 1c/1d never landed, stamp-lag recurred in the doc that documents stamp-lag, HANDOFF violates its own one-line-referent rule every entry. A protocol longer than what a session actually executes is aspiration, not architecture. Two remedies, both already in PROME's own toolkit: (a) the harness-audit deletion criterion (WALTER's 113→61 boot split — prune steps that are mechanizable or not behavior-gating); (b) keep converting discipline to scripts (claim_check, firetime_check, position_agreement_check, env_doctor is the right trend — scripts are crystallized discipline that doesn't consume session attention). The fast/slow asymmetry (BOOT absorbed 4 gates in 48h; CLOSEOUT's symmetry table knows none of them) suggests making the symmetry table the *registration point*: a boot gate isn't wired until its symmetry row exists — same move as my REGISTRATION_CHECKLIST for builds.

**T3 — No second reader on the fleet's most load-bearing outputs.** PROME is coordinator, dashboard publisher, canon steward, rails owner, and Will-interface at once. WALTER has a spec, YEYOU reviews pushes, every domain agent has PROME above it — but nobody routinely reads PROME's Will-facing surfaces, and today's first-ever external full read found a 4-day-degraded Will-facing artifact. This isn't a competence gap (the failure was silent-blank, invisible from inside); it's a structural blind spot: **the publisher can't see its own blank panels.** Fix-shape: (a) grade PROME into FLEET_MAP (Q1); (b) register a light recurring external check — PROME spine + Will-facing surfaces, read-only, ~21d, riding my existing sweep registry. Cheap insurance against exactly today's class.

### Smaller design thoughts

- **HANDOFF_2026Q2.md** is one file doing two jobs — append-only session log AND boot-read live surface — living in `archive/`, which lies about both. Split the roles: rotate the log (it's a Q2 file accruing in Q3), keep boot-reads out of archive/, and give archive/ a live index.
- **HEARTBEAT re-base is a schema-migration event without a migration checklist.** Three consumer classes broke across two re-bases (parsers, drafts, the STATUS count row). The accepted fix (re-base checklist: stamp consumed draft, run the dashboard build-assert, walk the named mirror stops) is the right shape — rituals that mutate load-bearing surfaces get checklists, not memory.
- **Intake is three paths, one mechanized** (BOARD cursor mechanized; inbox conditional; Will relay ad hoc). The "sole delivery surface" deserves the same treatment as BOARD: an unconditional one-line count in the boot gate.
- **codex lane**: keep as dormant capability — its problem is a missing trigger, not existence. One line on the gate-arming path fixes it.

### Bottom line

PROME's rules are almost never wrong — they were unexecuted. That's the signature of an architecture whose judgment outruns its bandwidth, and the correct response is the one already underway: mechanize invocation (scripts, ledgers, checklists, generated rows), shrink what must be hand-maintained (fewer mirrors, leaner protocol), and add the one thing PROME cannot give itself — an outside reader on a cadence.

## 7b. PROPOSED MECHANISMS FOR THE THREE TENSIONS (added 7/28 eve, Will's ask — proposals, not executed; lanes marked)

### T1 — Mirror-heavy × high change-rate → *shrink, generate, mechanize the walk*

| # | Proposal | What / Why | Effort | Lane |
|---|---|---|---|---|
| T1-a | **Mirror census & demotion pass** | Walk SYSTEM.md's Mirror Map + the mirrors this audit surfaced; classify each: KEEP-MIRROR (operationally necessary at read-time) / DEMOTE-TO-POINTER (exists for reading convenience) / GENERATE (machine-derivable). Target: halve the hand-maintained set. Candidates already identified: PROME/CLAUDE.md git ¶ → pointer-to-root + one-line delta; SYSTEM position lines → pointer to the root canon line; STATUS HEARTBEAT row → generated or countless pointer. | ~1 session, batched approval | PROME executes; fold into the 7/31-8/2 batch |
| T1-b | **`mirror_walk` as a mechanism, not a memory** | On any canon/threshold change: grep the OLD token across the Mirror-Map file list + PROME's own surfaces and print hits — i.e., `consumer_check.py` pointed at a self-inclusive enumeration (the accepted S5/PAT-068 fix, made concrete: a `--surfaces mirror_map` mode or a PUBLISHED.tsv-style ledger of PROME's mirrored facts). The 7/28 PORTFOLIO miss becomes impossible: the old token was greppable. | Small — reuses consumer_check | PROME (script is shared; patch gated per PAT-036) |
| T1-c | **Generate-don't-hand-mirror, triggered at n≥3** | Standing rule: any row that has rotted 3× gets generated from its source or reduced to a countless pointer — starting with the HEARTBEAT amendment count (derivable from `## AMENDMENT #N` headers in ~5 lines). Hand-mirroring has empirically failed for that row class; stop re-committing to it. | Trivial per row | PROME |

### T2 — Protocol mass > session capacity → *prune, script, gate registration*

| # | Proposal | What / Why | Effort | Lane |
|---|---|---|---|---|
| T2-a | **Run the 7/7 harness-audit deletion criterion over PROME's own spine** | The criterion already exists and is fleet-ratified (keep a step only if: ACTION/behavior-gating + not mechanizable + not owned elsewhere — WALTER's 113→61 precedent). Apply to CLOSEOUT (260 ln) + BOOT (96) + the step-doc periphery. Expected: CLOSEOUT ~260→~150 with zero lost enforcement, because most candidates are mechanizable (see T2-b). | 1 focused session, Will-approved batch | PROME proposes, Will approves |
| T2-b | **Collapse the check-stack into one gate script** | PROME already owns 6+ boot/closeout checks (claim_check, firetime_check, position_agreement_check, env_doctor, board_scan, memory_index_check, ledger_staleness…). Wrap: `prome_gate.py boot\|closeout` runs all, prints one PASS/FAIL block, rc≠0 on any gate. Doc steps collapse to "run the gate, then judgment steps." Precedent: HENRY/LABOR boot.py — the fleet's proven pattern for exactly this. Also closes the missed-1c/1d class permanently: new fleet-wide checks get ADDED TO THE SCRIPT, not to prose. | ~1 session build + wire same session (PAT-041) | PROME builds |
| T2-c | **Symmetry table = registration gate for new boot surfaces** | Rule + tiny check: a boot-read surface isn't "wired" until its CLOSEOUT symmetry row exists (paired-write or explicitly one-way). Mechanizable: diff BOOT.md's read-list against the table; run it inside T2-b's gate. Same move as my builds REGISTRATION_CHECKLIST — growth registers at the slow surface, not just the fast one. | Small | PROME; DAEDALUS can draft the check |

### T3 — No second reader → *make the outside reader structural*

| # | Proposal | What / Why | Effort | Lane |
|---|---|---|---|---|
| T3-a | **Register a recurring DAEDALUS sweep: "PROME Spine & Will-Facing Surfaces," ~21d, read-only** | Mechanical core (scriptable from today's reader checks): dashboard_state emptiness/vintage + GATES/DOCKET token-vocabulary + last_checked ages + overdue-unresolved rows + spine_audit run externally; judgment tail: skim Will-facing surfaces for silent-blank. Today's audit found a 4-day-degraded Will-facing artifact on the FIRST external read — this makes that read structural. Rides my existing `sweeps/REGISTRY.tsv` + cadence check. | ~½ session to register + playbook; ~1 session per run | **DAEDALUS — ready on your green light** |
| T3-b | **Grade PROME into FLEET_MAP + build `profiles/PROME.md`** | Puts PROME inside the Production Review cycle (the 14d pulse IS a recurring second reader) and closes the no-agent-grades-only-itself asymmetry. This audit = most of the first read; marginal cost is small now, larger later. | ~½ session now | **Will's word (Q1, still open)** |
| T3-c | **Nonempty-assertion rule for every generated Will-facing surface** | Generalize the dashboard's new "N panels EMPTY" chip: any tool that renders a Will-facing surface asserts parsed-sections ≥ threshold and fails loud (PAT-069's blueprint line). Silent-blank is the one failure class an inside reader can never see. | Trivial per tool | PROME (dashboard done); DAEDALUS encodes in blueprints |

**Sequencing recommendation:** T3-b (one word) and T3-a (my registration) now · T1-b/T1-c + T2-c + T3-c fold into PROME's existing 7/31-8/2 batch (they're small and adjacent to accepted items) · T1-a and T2-a/T2-b as the batch's second wave or the following week — they're the two real sessions of work, and T2-b should land before T2-a (prune against the gate script, not before it).

## 7. DISPOSITION TRAIL

- Findings packet → `PROME/inbox/2026-07-28_from-DAEDALUS_full-directory-audit-findings.md` (urgent block U1–U5 first), self-committed per carve-out ①.
- Verbatim reader evidence preserved: `upgrades/PROME_AUDIT_2026-07-28_readers/` (4 files).
- PATTERNS.tsv: PAT-068, PAT-069 banked.
- FLEET_MAP: no row to update (that's §6 Q1). STATUS.md updated; write-back watch armed for PROME's disposition reply.

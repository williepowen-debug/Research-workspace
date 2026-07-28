# PROME FULL-DIRECTORY AUDIT — 2026-07-28

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

## 7. DISPOSITION TRAIL

- Findings packet → `PROME/inbox/2026-07-28_from-DAEDALUS_full-directory-audit-findings.md` (urgent block U1–U5 first), self-committed per carve-out ①.
- Verbatim reader evidence preserved: `upgrades/PROME_AUDIT_2026-07-28_readers/` (4 files).
- PATTERNS.tsv: PAT-068, PAT-069 banked.
- FLEET_MAP: no row to update (that's §6 Q1). STATUS.md updated; write-back watch armed for PROME's disposition reply.

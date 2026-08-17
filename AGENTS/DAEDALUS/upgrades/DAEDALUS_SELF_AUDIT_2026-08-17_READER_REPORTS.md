# DAEDALUS SELF-AUDIT 2026-08-17 — RAW READER REPORTS (PAT-100 companion)

**Commissioned by:** Will (verbatim intent: "Recently we did a bunch of upgrades to Prome's system. I'd like to do a similar reflective analysis on DAEDALUS system and file structure too.")
**Method:** 5-reader Mode-A fan-out over DAEDALUS's own tree, all read-only, zero edits by readers. Synthesis doc: `DAEDALUS_SELF_AUDIT_2026-08-17.md` (beside this file — the mandated pair, both halves present).
**Reader-ops record:** 5 spawned in parallel. reader-spine and reader-blueprints delivered unprompted; reader-tooling, reader-registers, reader-workproduct idled holding and delivered on chase (3-of-5 chase rate — consistent with the standing floor; the chase remains standing procedure). All 5 delivered complete reports with NOT-READ lists.
**Synthesizer verification:** 10-probe battery run against the highest-severity claims BEFORE synthesis; all 10 CONFIRMED (probe list + outputs recorded in the synthesis doc §Verification). One reader-side error found and preserved below uncorrected: reader-tooling's NOT-READ list calls STATUS.md "~49KB" — actual 100,051 B (reader-spine's measurement, re-verified by me). Raw reports below are VERBATIM as delivered, errors included — this file is evidence, not conclusions.

---

## READER 1 — SPINE (governance spine: CLAUDE.md, SPEC.md, STATUS.md, EVOLUTION.md, UPGRADE_PROTOCOL.md)

DAEDALUS GOVERNANCE SPINE — READ-ONLY AUDIT (files: CLAUDE.md, SPEC.md, STATUS.md, EVOLUTION.md, UPGRADE_PROTOCOL.md). Zero edits made.

HEADLINE: DAEDALUS authored, ratified and fleet-routed the STATUS byte-tier convention on 2026-08-17 and its own STATUS.md sits at 391% of that convention's default budget — 5.2x the rotation trigger — with no seat budget, no archive, and no rotation. Second-highest density in the fleet (752 B/line), 93% of the BRENT 812 B/line figure it cited as the ruling's own evidence.

=== FINDINGS TABLE ===
ID | file:line | sev | claim | evidence

D1 | AGENTS/DAEDALUS/STATUS.md (whole) | URGENT | STATUS.md is at 391% of DAEDALUS's own ratified byte budget, 5.2x the rotation trigger | Measured: 100,051 B / 133 lines = 752 B/line. Own convention (BLUEPRINTS/market-agent.md:99, encoded by DAEDALUS in 8fd25137c, Will-ratified 8/17): default byte budget = ~128 B/line x line cap; DAEDALUS cap = 200 (own CLAUDE.md:140) => budget 25,600 B. 100,051/25,600 = 390.8%. Rotation trigger is >=75% (19,200 B). Density = 5.9x the 128 B/line default. Fleet rank: 2nd-highest B/line of 40 STATUS files (BRENT 820, DAEDALUS 752, CARL 698). Growth across the ratification window: 70,984 B (8/16) -> 100,051 B (8/17) = +41.0% in 2 days; +17.6% on 8/17 alone (aa92f6c03 85,052 -> 96442eee4 100,051). No archive file exists (ls AGENTS/DAEDALUS/ — no archive/ dir); no seat budget declared anywhere. Reference implementation WATT set a 64,000 B budget and rotated at 67 KB the same night (bee36f441).

D2 | AGENTS/DAEDALUS/CLAUDE.md:140 | URGENT | DAEDALUS's own OUTPUT RULES is non-conformant with the meta-agent blueprint it edited the same day | meta-agent.md:18 (edited by DAEDALUS 8/17, commit 8fd25137c) makes OUTPUT RULES require "line cap + byte tier (Will-ratified 2026-08-17)". DAEDALUS CLAUDE.md:140 reads only "STATUS.md under 200 lines." — grep for "byte" in AGENTS/DAEDALUS/CLAUDE.md returns zero hits. DAEDALUS is the fleet's only Meta-class agent graded against that variant. Textbook instance of its own memory finding_a_ruling_governs_the_next_write_not_the_existing_state, on the author's file.

D3 | AGENTS/DAEDALUS/EVOLUTION.md:4 vs :301-339 | HIGH | The changelog's seven newest entries are outside the changelog, below the roadmap, at the wrong heading level, in reverse order | File header line 4: "Newest first." The "## Changelog" section (line 8) runs 2026-08-16(c) -> 2026-06-27 correctly newest-first. Then "## Roadmap" at line 301. Then entries 2026-08-17 (a) through (g) at lines 313, 317, 321, 325, 329, 333, 337 — appended BELOW the roadmap, as "##" siblings of the Changelog rather than "###" children, in OLDEST-first order. A reader following the file's own stated protocol sees 8/16(c) as the latest standard change and misses seven, including CHECK_STANDARD §8 RATIFIED, §9 RATIFIED, and the byte-tier ratification. Entry (g) even carries an in-line note that (f) was double-assigned and caught at append — the ordering defect is already producing collisions.

D4 | AGENTS/DAEDALUS/STATUS.md:57 | HIGH | The "Standing capability" section asserts current capability with 10-day-stale figures, contradicted by the same file's own header | Claim vs measured: "PATTERNS banked through PAT-090" — actual max PAT-110 (PATTERNS.tsv; the same file's header at :3-5 cites PAT-106/108/109/110). "FLEET_MAP 36 rows current at 8/7 PM" — actual 43 rows. "34 profiles" — actual 35 (ls profiles/*.md). "generated FLEET_DIRECTORY (39)" — FLEET_DIRECTORY.md:68 self-reports 40 (31 active + 4 tier-2 + 2 dormant + 3 special). Only "CHECKS.tsv (19 rows)" holds (verified 19).

D5 | AGENTS/DAEDALUS/FLEET_MAP.tsv (DAEDALUS row, field 6) | HIGH | DAEDALUS's own FLEET_MAP row is 5 days stale — a verbatim recurrence of a defect it self-found on 8/12 | Last_scored = 2026-08-12, Level L4, through 8/15 (war-triad), 8/16 (4 sessions), 8/17 (4 movements incl. its own PROME L5 promotion and the SFG sweep). SPAWN PROTOCOL step 7 explicitly names "your own FLEET_MAP row's currency" as in-scope (PAT-050 self-inclusion). STATUS:25 records the identical finding on 8/12: "my own FLEET_MAP row was 5d stale through my heaviest self-finding day -> re-cut". n=2, same interval, same conditions — the 8/12 fix addressed the instance, not the mechanism. Note the file itself was committed 8/17 12:08 (d61b7d084), so other rows were re-cut that day while its own was not.

D6 | AGENTS/DAEDALUS/CLAUDE.md (no line — absent) | HIGH | DAEDALUS's charter contains no closeout sequence; zero of the five root-mandated closeout checks appear in it | grep for orphan_check|consumer_check|claim_check|memory_index_check|check_memory_length across AGENTS/DAEDALUS/CLAUDE.md returns 1 line, and that match is the bare word "check" inside the NO-GUARD-SHIPS-UNVERIFIED rule at :139 — no named check. The GIT block (:92) cites only safe-push.sh. SPAWN PROTOCOL is 8 steps ending at "deliver before idling"; there is no step 9. Root CLAUDE.md steps 1b-1e mandate all five. STATUS:111 proves the battery IS executed (8/14 closeout names orphan_check, check_memory_length, 1c/1d skips) — so invocation rides session memory rather than the charter. This is precisely the "the shared gap is INVOCATION not detection" diagnosis DAEDALUS published at n=3 on 8/17 (STATUS:7), unapplied to itself. consumer_check (1c) is additionally absent from even the practiced battery listed at STATUS:25/111 — and DAEDALUS publishes figures other agents cite (byte budgets, thresholds, rc contracts).

D7 | AGENTS/DAEDALUS/CLAUDE.md:108 + SPEC.md:88 | MED-HIGH | The Meta L5 rubric names a leg that the fleet's first Meta L5 promotion never adjudicated, and that DAEDALUS's own file fails | Both ladders define Meta L5 as "same + EVOLUTION roadmap live". PROME was promoted Meta L5 on 8/17 (FLEET_MAP PROME row: Meta/L5/Conf M/Last_scored 2026-08-17) and PROME has no EVOLUTION.md (ls PROME/EVOLUTION.md -> No such file). The row's Gaps field enumerates the four own-rule-unexecuted items and never mentions the roadmap leg. Separately, DAEDALUS's OWN roadmap (EVOLUTION.md:301-311) is 5-of-5 struck through and self-labelled "now fully dispositioned" with forward items relocated to STATUS — so the leg is unsatisfied on its author's file too, yet DAEDALUS's self-L4 blocker (STATUS:33) names only the cadence leg. Either the rubric text is wrong (the leg is DAEDALUS-specific, not Meta-class) or two grades skipped a named leg.

D8 | AGENTS/DAEDALUS/CLAUDE.md:140 vs STATUS.md:37-53,71-73,87-133 | MED | The archive rule is not being executed, and its designated sink is itself uncapped | Rule: "Archive old build records to EVOLUTION.md or FLEET_MAP.tsv." STATUS still carries the full "2026-08-07 — the full-day record" section (lines 37-53), the 8/11 Staleness Sweep #3 section (71-73), and a BOTTOM LINE of 14 stacked "Prior — as of ..." paragraphs measuring 47 lines / 32,660 B = 32.6% of the whole file — against the same charter's rule "End STATUS.md with a 2-4 sentence BOTTOM LINE." No archive artifact exists in AGENTS/DAEDALUS/. And EVOLUTION.md, the named sink, is 89,450 B / 339 lines with no line cap or byte tier of any kind in the charter.

D9 | AGENTS/DAEDALUS/STATUS.md:68 | MED | The live "Sweeps cadence" line asserts two events as forthcoming that the same file records as completed | :68 reads "Staleness ~8/15 ... PROME judgment-tail sweep #1 ~8/18 = PROME's L5 adjudication moment". :80 records Staleness RUN 8/11; :81 records the PROME sweep RUN 8/16; :3 records PROME PROMOTED TO L5 on 8/17. Un-struck stale line sitting inside the live structural-debt block, where a reader looks for what is still owed.

D10 | AGENTS/DAEDALUS/FLEET_MAP.tsv (WATT row, field 6) | MED | A FLEET_MAP row was materially re-cut without bumping its own vintage field | Field-level diff of d61b7d084 (8/17 12:08): fields 1-8 byte-identical, field 9 (Notes) changed. Last_scored stayed 2026-08-07 — the field the profile-refresh and Production Review queues read as row freshness (REGISTRY.tsv service rules). Same class as PAT-108 (writer with no reader) / PAT-044, banked by DAEDALUS the same day, on its own register. Companion: SPAWN PROTOCOL step 7 mandates regenerating FLEET_DIRECTORY on ANY row change; d61b7d084 does not include FLEET_DIRECTORY.md. Rendered output is unaffected in fact (the directory renders class/level/Next_upgrade, none of which moved), so this is a protocol violation with no data defect.

D11 | git 383051aeb | LOW-MED | One post-adoption miss of DAEDALUS's own PAT-101 rule ii | Rule (STATUS:82): "any edit to BLUEPRINTS/* or UPGRADE_PROTOCOL.md requires an EVOLUTION.md entry IN THE SAME COMMIT", adopted 8/12. 383051aeb (2026-08-12) edits BLUEPRINTS/STATE_VOCABULARY.md with no EVOLUTION.md in the commit (verified via git show --name-only). All 12 BLUEPRINTS-touching commits from 8/14 onward pair correctly (EVOL=1 x12). Pre-adoption misses are grandfathered but worth noting that CHECK_STANDARD.md's own birth commit (26b077deb, 8/11) carries no EVOLUTION entry.

D12 | AGENTS/DAEDALUS/SPEC.md:3 | LOW | SPEC asserts a next phase that completed ~7 weeks ago | ":3 — "Phase 4 (first real maintenance pass) next." EVOLUTION's 2026-06-28 entry: "Phase 3/4: first REAL build executed — AEOLUS". Mitigated by the same line's "(Historical Phase-0 snapshot — live state: STATUS.md)" parenthetical, which is why this is LOW not MED.

D13 | AGENTS/DAEDALUS/SPEC.md:86, :57-64 | LOW | SPEC §5's ladder and §4's memory model are superseded, and CLAUDE.md points readers at them | CLAUDE.md:112 says "Full rationale in SPEC.md §5", but SPEC §5's Market L3 cell reads "convergence matrix + exit/falsification rules + predictions resolving" — missing the dated-falsification-surface leg CLAUDE.md's own ladder carries (adopted 8/7, 3f2abb54d). SPEC §4 declares "Four files"; CLAUDE.md's MEMORY MODEL lists nine (SURFACES.tsv, CHECKS.tsv, FLEET_DIRECTORY.md, profiles/, upgrades/ all absent from SPEC).

D14 | AGENTS/DAEDALUS/UPGRADE_PROTOCOL.md:49 | LOW | The upgrade-card spec is market-shaped and unqualified | ":49 — "the 8 blueprint sections as rows". market-agent.md has exactly 8 numbered sections (verified), but meta-agent.md defines 9 required sections. A card built for a meta or utility agent has no row for section 9.

D15 | AGENTS/DAEDALUS/CHECKS.tsv (ledger_staleness row, field 6) | LOW | The rc-contract re-cut updated the run field but not the PAT-074 "what a PASS proves" column | Field 7 correctly carries "2026-08-17 (rc CONTRACT REVISED ... 0 clean / 1 stale FINDINGS / 2 CANNOT-CERTIFY ...)". Field 6 still describes only the 7/31 repair and never states what rc-0 now proves under the new contract — the column DAEDALUS created specifically to answer that (PAT-074).

=== CLAIMS-VS-ARTIFACTS SAMPLE (14) ===
1. "§8 PROVISIONAL ... RATIFIED same day, marker struck" (STATUS:61) — VERIFIED. CHECK_STANDARD.md:53 heading reads "— RATIFIED (Will, 2026-08-17 verbatim 'Ratify §8')"; no PROVISIONAL marker remains.
2. "§8-canon one-liner ... encoded as CHECK_STANDARD §9" (STATUS:62) — VERIFIED. CHECK_STANDARD.md:65-72, ruling wording verbatim at :67, producer/consumer halves at :69-70.
3. "9 owner packets (SAM/HAWK/CARL/VIOLET/REGINALD/HENRY/BOND/SHADE/BRENT)" (STATUS:3) — VERIFIED. Each of the 9 inboxes holds >=1 packet dated 2026-08-17 from DAEDALUS (SAM 2).
4. "wrapper five (OZK/LABOR/MARCO/OTTO/ZHAO) packets committed 8/17" (STATUS:61) — VERIFIED. All five present (MARCO 2, OTTO 2).
5. "CHECKS row re-cut" for the rc contract (STATUS:5) — VERIFIED WITH GAP. Field 7 dated 2026-08-17 carries the full 0/1/2 contract and the 7-consumer batch; field 6 not updated (see D15).
6. "EVOLUTION 8/17 same-commit (PAT-101 rule ii)" (STATUS:3) — VERIFIED. All 8 BLUEPRINTS-touching commits on 8/17 include AGENTS/DAEDALUS/EVOLUTION.md in the same commit (git show --name-only, EVOL=1 x8).
7. "memory 5th refinement (INVERTED-verdict form) appended per carve-out (3)" (STATUS:3) — VERIFIED. Commit 62f404f50, appended to memory/auto/finding_fail_loud_on_incomplete_data.md, dedup-before-create honoured (extension, not a new slug).
8. "PAT-106 ... PAT-110 banked" (STATUS:3,5) — VERIFIED. PATTERNS.tsv carries PAT-100 through PAT-110 contiguously; max = PAT-110.
9. "canonical record sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md" (STATUS:3) — VERIFIED (42,207 B).
10. "record upgrades/LEDGER_STALENESS_RC_CONTRACT_2026-08-17.md" (STATUS:5) — VERIFIED (6,261 B).
11. "NEXUS commission packet ... = 26df8ca6c, existence verified" (STATUS:77) — VERIFIED. File present in inbox/; commit subject matches ("PROME -> NEXUS + DAEDALUS: NEXUS systems review COMMISSIONED").
12. "FLEET_MAP PROME row re-cut + directory regen" for the L5 promotion (STATUS:3) — VERIFIED. PROME row = Meta/L5/Conf M/Last_scored 2026-08-17 with the 4-item artifact-verified rationale; FLEET_DIRECTORY regenerated in b45d1cd4d and 3708fd0a5, its PROME row reads L5.
13. SPAWN PROTOCOL step 7 "if you changed ANY FLEET_MAP row ... regenerate the directory" applied to d61b7d084 — FAILED (technical). FLEET_MAP.tsv changed at 8/17 12:08; FLEET_DIRECTORY.md not in that commit. No data defect (only the Notes field moved; the directory renders other fields). See D10.
14. CLAUDE.md:140 "STATUS.md under 200 lines" — VERIFIED on the line dimension (133/200 = 66%), FAILED on the byte dimension (D1). This is exactly the PAT-086 evasion shape DAEDALUS named at LABOR (line-pinned, bytes +72%) and at SAM (+59% under a satisfied line cap).

Also verified as CURRENT, not stale (worth recording — I tried to break these and could not): the YEYOU box in CLAUDE.md AUTHORITY and SPEC:111 still holds — AGENTS/YEYOU/reviews/REVIEW_LOG.tsv is 3 lines, header + 2 comments, zero findings all-time. sweeps_due.py runs clean (rc=0, "none due (11 tracked)") and all four scripts named in the FILES table exist. REGISTRY.tsv tracks exactly the 11 sweeps/queues STATUS claims. profiles/_TEMPLATE.md exists (STATUS's "_TEMPLATE class-killed" means the defect class, not the file — ambiguous phrasing, not a defect).

=== MY RANKED TOP-5 ROUTE LIST ===
1. D1 + D2 — Set a DAEDALUS seat byte budget with on-surface rationale and rotate STATUS to a dated archive, following the WATT reference form it just canonised (crc at rotation time, contiguous regions only). Then add the byte tier to CLAUDE.md:140. This is the single highest-severity item and it is self-inflicted, same-week, and fully specified by DAEDALUS's own ratified text. Everything about D8 falls out of doing this.
2. D3 — Move the seven 8/17 entries into the "## Changelog" section at "###" level, newest-first. Cheap, and until it is done the changelog actively misleads on the most consequential week in the file (two ratified canon sections invisible to a newest-first read).
3. D5 — Re-cut the DAEDALUS FLEET_MAP row AND fix the mechanism, not the instance. n=2 at identical 5-day intervals says the 8/12 instance-fix did not work; the row needs a wake owner the way DAEDALUS demands of every other agent (PAT-089's own fix-form: file-readable trigger, not intention).
4. D6 — Write the closeout sequence into CLAUDE.md (root steps 1b-1e by name, cite-don't-restate). DAEDALUS's own 8/17 headline finding is "invocation, not detection" at n=3; its charter is an invocation gap of exactly that shape, and it already knows (STATUS:25) that its battery is COMMITTED-only. The COMPLETE-check it has owed itself since 8/12 belongs here too.
5. D4 + D9 — Strike or refresh the two stale current-tense blocks ("Standing capability" :57, "Sweeps cadence" :68). Both assert as live what the same file records as done, in the two places a reader goes for "what is true now" and "what is still owed". D7 (Meta-L5 roadmap leg) is the next one down — it is a rubric-integrity question rather than a rot question, but it touches a live grade.

=== NOT-READ LIST ===
- EVOLUTION.md lines 63-298 (~60 KB of pre-2026-08-07 changelog entry BODIES) were not read in full. I read every heading (39 entries, dumped by grep), the full bodies of lines 299-339 (roadmap + all seven 8/17 entries), and 120-char previews of lines 1-40. Rationale: token budget; the audit questions target current claims and the newest week. Consequence: any contradiction living purely inside a June/July entry body would be missed. The ordering defect D3 is a structural claim about heading levels and section membership, and is unaffected.
- PATTERNS.tsv: read as ID enumeration and max only (111 rows) — no row bodies. So "PAT-106 banked" is verified as EXISTS, not as says-what-STATUS-says.
- FLEET_MAP.tsv: only the DAEDALUS, PROME and WATT rows read; 40 other rows unread. Row-count and header verified.
- CHECKS.tsv: 3 of 19 rows read (consumer_check, ledger_staleness, position_agreement_check).
- SURFACES.tsv: row count only (14), no content.
- BLUEPRINTS/: no file read end-to-end. Targeted reads only — market-agent.md:99 (byte tier, full), meta-agent.md:10-25 (required sections), CHECK_STANDARD.md headings + §9 lines, market-agent.md section headings. BEST_PRACTICES.md, DELEGATION_TIER.md, STRICT_TEXT.md, STATE_VOCABULARY.md, STATUS_TWO_STATE_PILOT.md, utility-agent.md entirely unread — out of the assigned five-file slice.
- profiles/ (35 files), upgrades/, builds/, design/, sweeps/*.md playbook bodies: existence and size verified for 9 named artifacts; no content read. REGISTRY.tsv read in full.
- NOT VERIFIED, flagged as a live open question: STATUS:61 item (3) claims ~14 owner write-backs OPEN vs 2 CLOSED-VERIFIED. Confirming that partition requires reading 14 agents' inbox/processed/ dirs and was out of scope for this slice. Given D5/D9 (two independent stale-tracking-line findings on this same file), I would not take that count as reliable without checking.
- Read in full: CLAUDE.md (all 170 lines), SPEC.md (133), STATUS.md (all 133), UPGRADE_PROTOCOL.md (58).

---

## READER 2 — TOOLING (scripts/ + inbox/outbox lifecycle vs CHECK_STANDARD)

### 1. PER-SCRIPT GRADE vs DAEDALUS'S OWN `CHECK_STANDARD.md`

| Script | §8 silent-fallback-green | rc contract (§9: 0 clean/1 findings/2 cannot-certify) | §2 null-output states perimeter | Capable-case evidence | Invoked by |
|---|---|---|---|---|---|
| `sweeps_due.py` (55ln) | ❌ **CLASS-HIT (watched)** — corrupted registry prints `✅ sweeps: none due (0 tracked)` on **stdout**, degradation only on **stderr**, which §8 rule 1 explicitly disqualifies | ❌ **rc=0 always** — docstring states "alert, not a gate," the exact always-0 contract §9 names as a standing SFG exposure | ⚠️ partial — prints `(N tracked)` but never the **skipped** count; missing registry prints **nothing at all** | ❌ **none** — 1 commit ever (7/4), no capable-case run recorded anywhere | ✅ DAEDALUS `CLAUDE.md:41` SPAWN step 5 (its **only** boot check) |
| `maturity_scan.py` (321ln) | ⚠️ narrow — git-failure path (`sh()` :64-65 swallows stderr, `HEAD_EPOCH=0`) silently zeroes `commits_30d` → every agent drops to `L2`, no marker | ❌ **no rc at all** — `main()` :285-318 has no `sys.exit` | ✅ **strong** — `NOT GRADED` + reason for `JUDGMENT_ONLY`, printed in **both** modes (:288-295, the PAT-074b fix) | ✅ good — PAT-020/031 hardening + the 8/03 self-caught dead-announcement, all in commit msgs | ❌ **NOTHING** — see D-01 |
| `render_directory.py` (188ln) | ❌ **CLASS-HIT (watched)** — asymmetric guard: FLEET_MAP→ROSTER dies loud (rc=1, verified); ROSTER→FLEET_MAP renders **blank cells identical to by-design dormant**, rc=0, summary count unchanged | ⚠️ 0 / 1-on-die; no `2` tier (generator, so §9 binds weakly) | ✅ strong on the loud path; ❌ blank-cell path is the un-stated perimeter | ✅ good — co-registration guard watched at FERT registration 8/16 | ✅ `sweeps/PRODUCTION_REVIEW.md:66` (step 5) |
| `falsification_scan.py` (358ln) | ⚠️ **`--tsv` mode drops the entire "what was NOT looked at" layer** (:313-318 vs :339-354) — contradicts its own docstring "counts for every class, **always**" and the sister script's own fix | ❌ **rc=0 with 3 STALE-FLAGGED + 1 UNSTAMPED live** (verified this session) | ✅ default mode is the fleet's best example; ❌ `--tsv` mode and typo'd `--agent` are not | ✅ **excellent** — 8/17 commit: 7 unit cases + live re-run, both directions | ✅ `sweeps/FALSIFICATION_SWEEP.md:22` (single invoker) |

**Watched capable cases I ran (per DAEDALUS's ★ rule, on isolated /tmp copies — repo untouched):**
```
sweeps_due, registry with 2 corrupted ACTIVE rows, stdout only:
  ✅ sweeps: none due (0 tracked)          rc=0     ← both warnings were on stderr
sweeps_due, registry file deleted, stdout only:
  (nothing)                                rc=0
render_directory, ACTIVE agent absent from FLEET_MAP:
  | VULCAN | — | — | AI-capex… | — |       rc=0     ← byte-identical to SENTRY/BARON (dormant, by design)
  summary still reads "40 agents: ACTIVE 31"
render_directory, ROSTER "## TIER-2" header renamed:
  FAIL — unhandled FLEET_MAP-only agent(s) ['CREED','DEWEY','HANS','OTTO']   rc=1  ← guard works
falsification_scan --agent BRENTT (typo):
  Searched: 0 surfaces across 0 agents · all sections "none"   rc=0
falsification_scan, live default run:
  STALE-FLAGGED 3 · UNSTAMPED 1            rc=0
```

### 2. FINDINGS (ranked)

| ID | file:line | Sev | Claim | Evidence |
|---|---|---|---|---|
| **D-01** | `maturity_scan.py` (whole) | 🔴 HIGH | **The fleet's maturity floor layer is invoked by nothing.** `CLAUDE.md` MATURITY LADDER says "L0–L2 **scripted** (objective, rerunnable, can't hallucinate)" — but no boot step, sweep playbook step, or closeout runs it. Production Review §1 "Detect" uses raw `git log`, not the scanner. | Repo-wide grep: only hits are `PATTERNS.tsv` (as a *subject*), `SPEC.md:132` (a settled question), `MATURITY_MAP.md:6` (a 6/27 doc), `CLAUDE.md:162` (FILES table), `REGISTRATION_CHECKLIST.md:20` row 12 — which mandates *editing its SKIP set*, never running it. This is CHECKS.tsv's own founding thesis ("a check with no invocation site is unowned in practice") on the architect's own instrument. |
| **D-02** | `render_directory.py:121-126, 158-159` | 🔴 HIGH | **The co-registration guard is one-directional, and the blank it produces is taught to the reader as by-design.** An ACTIVE agent in ROSTER but absent from FLEET_MAP renders `— \| — \| … \| —`, rc=0 — indistinguishable from a deliberately ungraded dormant. The generated artifact's own footnote ("Dormant agents are un-graded → blank grade cells") actively certifies the gap as intentional. Live trigger: PAT-047 registration order lands the ROSTER row first. | Watched above. Docstring :13-14 claims "FAILS LOUD on any unhandled FLEET_MAP-only agent — a new real agent can never silently vanish"; the inverse direction has no guard. Will/PROME read this artifact. |
| **D-03** | `sweeps_due.py:36-37, 42-44, 47, 51` | 🟠 MED-HIGH | **DAEDALUS's only boot-invoked check is a §8 CLASS-HIT and a §9 always-0 producer.** Degraded registry → green checkmark on stdout, warning on stderr; missing registry → nothing. Blast radius = all **11 registered sweeps/queues** silently stop being cadence-checked at every DAEDALUS boot. | Watched above. §8 rule 1 verbatim: *"A warning that exists only on stderr … does not count: 9 fleet wrappers delete stderr on rc==0."* §9's origin case (`ledger_staleness.py`) is the same shape and was fixed **this same day** — upstream, not here. |
| **D-04** | `falsification_scan.py:313-318` | 🟠 MED | **`--tsv` mode silently drops all four "what was NOT looked at" announcements** (`no_rail`, `no_thesis`, `no_clock`, `bannered_thesis`). The machine-readable mode a fan-out reader or downstream tool consumes is the one missing the PAT-074 layer. | `--tsv` output = 31 lines, ends at the last data row. Its own docstring (:16-17) commits to "counts for every class, always." `maturity_scan.py:288` fixed this exact class explicitly "in BOTH output modes." |
| **D-05** | `falsification_scan.py` (no `sys.exit`), `maturity_scan.py:285` | 🟠 MED | **Neither scan can disagree with clean.** falsification_scan exited **0 with 3 STALE-FLAGGED + 1 UNSTAMPED** live this session. §9 scope: "binds new shared checks at build and **existing ones at next material edit**" — falsification_scan had a material edit **8/17, the same day**, and did not take the contract. | Run above. |
| **D-06** | `CHECKS.tsv:4` (SCOPE line) | 🟠 MED | **The register's exclusion predicate is false for its owner's own scripts.** Scope note excludes agent-local checks because "they … are **invoked by their own owner's own boot**." DAEDALUS's boot invokes exactly one of four (`sweeps_due`); `maturity_scan` is invoked by nothing (D-01). The four scripts most load-bearing to the maturity map sit in **no register at all** — no invocation state, no `Null_meaning`, no last-verified-run column. | `CHECKS.tsv` = 19 rows, all repo-root `scripts/`. Zero DAEDALUS-local rows. |
| **D-07** | `falsification_scan.py:292-293` | 🟡 LOW | Typo'd `--agent NAME` produces a full, clean-looking zero report (rc=0) with no "agent not found"; bare `--agent` throws an uncaught `IndexError`. | Watched above. |
| **D-08** | `maturity_scan.py:28-29, 64-70` | 🟡 LOW | `sh()` never checks returncode. If `git` is unavailable, `HEAD_EPOCH=0` and `commits_30d`→0 for every agent, collapsing all L3?/L4? hints to `L2` — a full-fleet under-grade, no marker, rc 0. | Code read; not reproducible on this box (git present). Same shape as the SFG class DAEDALUS swept fleet-wide 8/17. |
| **D-09** | `STATUS.md:57` | 🟡 LOW | Standing-capability line reads "FLEET_MAP 36 rows current at 8/7 PM … generated FLEET_DIRECTORY (39)". Actual: **40 / 40**. | `awk` field count = 40 rows; renderer summary = 40 agents. |

**Hypothesis tested and REFUTED:** I predicted `render_directory.parse_roster` would silently drop a section on a ROSTER header rename. It does not — the FLEET_MAP cross-check catches it loudly (rc=1, watched). Design is sound in that direction; only the inverse (D-02) is open.

### 3. CAPABLE-CASE EVIDENCE LEDGER

| Script | Alert path ever watched firing? | Where recorded |
|---|---|---|
| `falsification_scan.py` | ✅ **Yes, twice** — 8/17 commit: "7 unit cases + live re-run, `red/COUNTER_THESIS` prints STALE-FLAGGED 44d" | commit msg + `FALSIFICATION_SWEEP.md` run log |
| `render_directory.py` | ✅ **Yes** — co-registration guard watched at FERT registration 8/16 | commit `45fd78e8c` |
| `maturity_scan.py` | ⚠️ **Partial** — grading path watched repeatedly; the `NOT GRADED` announcement was watched **after** being found dead (PAT-074b, 8/03). Git-failure degraded path never watched. | commit msgs |
| `sweeps_due.py` | ❌ **NONE.** One commit (7/4), pre-dating the ★ rule (8/3) and CHECK_STANDARD (8/11). Its `⚠️ un-parseable row` line has, on any record, **never been watched printing**; its scope line never tested against a degraded registry. | — |

`sweeps_due.py` is the **only DAEDALUS script with zero capable-case evidence**, and it is the only one wired into boot.

**Scope note on the 8/17 SFG sweep:** DAEDALUS's own silent-fallback-green class sweep that same day covered **15 files across SAM/HAWK/FALCON/MARCO/LABOR/PROME**, declared "0 NOT READ," and concluded "nothing in this sweep's scope remains untraced." **Zero DAEDALUS-own scripts were in scope.** Scope-honest, but D-02/D-03 are two instances of that exact class in its author's own directory.

### 4. OUTBOX CENSUS + CONSUMPTION

**Root: 0 files. `delivered/`: 26 files, newest 2026-08-07.** No packet placed in `outbox/` in **10 days**.

Not a backlog — a **retired workflow with a live rule still pointing at it**:

| Measure | Count |
|---|---|
| DAEDALUS-authored packets in recipient inboxes (all time) | **178** |
| …since 8/08 (after the last `delivered/` file) | **76** |
| …with a corresponding `outbox/` copy | **0** |

DAEDALUS now writes packets **directly** into recipients' `inbox/` under root carve-out ①; delivery is by construction and the outbox copy is redundant. **But `CLAUDE.md:43` (write-back tail rule) still mandates "move your `outbox/` copy to `outbox/delivered/`"** as one of four legs to close — a leg that has not existed for 76 consecutive packets. And `delivered/` is now a dead ledger with **no FROZEN banner** — the exact two-state violation the Fleet Staleness Sweep enforces on everyone else.

**Sample-of-5 consumption trace:**

| Delivered packet | Recipient-side evidence | Verdict |
|---|---|---|
| `2026-07-22_to-REGINALD_wal-promotion-review` | `REGINALD/inbox/processed/2026-07-22_from-DAEDALUS_wal-promotion-review-delivered.md` | ✅ CONSUMED |
| `2026-07-10_to-LABOR_gap-assessment-packet` | No same-name file in `LABOR/inbox/processed/`; era-adjacent processing via `from-PROME_daedalus-buildwave-fixes` (7/10) | ⚠️ ROUTED-VIA-PROME, not directly traceable |
| `2026-07-10_to-REGINALD_audit-triage-advice` | Inbound write-back `inbox/processed/2026-07-10_from-REGINALD_audit-triage-dispositioned.md` | ✅ CONSUMED (proven by the reply, not the file) |
| `2026-07-10_to-WALTER_sweepAB-reping` | Inbound write-back `inbox/processed/2026-07-11_from-WALTER_sweepAB-applied.md` | ✅ CONSUMED |
| `2026-08-07_to-PROME_terry-2-gates-past-due-no-grader-spawn-ask` | No matching PROME `processed/` file | ⚠️ UNVERIFIED at recipient |

**Reverse-direction finding (PAT-094 class, now inbound):** **33 DAEDALUS packets sit unprocessed in recipient inbox roots**, oldest **2026-08-07 (10 days)** — HENRY ×2 and BOND. Consistent with STATUS open item ③ (14 write-backs tracked), so not invisible — but the 8/07 HENRY pair predates that list's framing.

### 5. INBOX FILING

| Location | File | Status per STATUS.md | Correct? |
|---|---|---|---|
| root | `2026-08-16_from-PROME_docket-view-renderer-build-commission.md` | Build window **~8/24→8/31**; STATUS §0 item ② lists it live | ✅ **HELD BY DESIGN — correct.** Window forward. |
| root | `2026-08-17_from-PROME_WILL-RULED-forum4-11-registration-checklist-homes-at-blueprints.md` | Will-ruled 8/17, explicitly "**nothing here is time-boxed**," sequencing DAEDALUS's call | ✅ **HELD — correct.** |
| root | `2026-08-17_from-PROME_commission-nexus-profile-audit-blind-leg.md` | Window **~8/29-31**, ruled POST-8/28 for blind-leg contamination | ✅ **HELD BY DESIGN — correct.** |
| `processed/` | 108 files, newest `2026-08-17c_from-WATT` | — | ✅ No file found carrying an unclosed forward obligation on a spot check of the 8/16-8/17 tail. |

All three root packets' dates and claims verify against their contents. **Inbox lifecycle is the healthiest surface in the audit.** (Caveat: no mechanical check distinguishes deliberately-held from forgotten.)

### 6. MISSING TOOLING — concrete, small-scope

All ≤~40 lines; none requires a new protocol step (per `PRODUCTION_REVIEW.md:58`: *"the fix for an unwired check is almost never a new protocol step — it is attaching it to a step that already fires"*).

| # | Candidate | Attach to | Why now |
|---|---|---|---|
| 1 | **Reverse co-registration guard** — ACTIVE/TIER-2 ROSTER agent absent from FLEET_MAP → `⚠️ UNGRADED` in-cell + summary line + rc=1 | already-running `render_directory` | Closes D-02 in ~6 lines inside a script that already runs. Highest ratio. |
| 2 | **Register schema lint** — field-count + required-column over `PATTERNS/FLEET_MAP/CHECKS/SURFACES/REGISTRY` | `PRODUCTION_REVIEW.md` §3b (already runs `lane_coverage` + `canon_check`) | All 5 currently uniform (7/9/9/8 cols) — **ship it while clean**; `tsv_append`'s lint fires only on writes that use it. |
| 3 | **FLEET_DIRECTORY regeneration currency** — artifact's `Generated <date>` vs FLEET_MAP content vintage | same §3b step | Both 8/17 today (clean). "Regenerate whenever a FLEET_MAP row changes" is enforced by memory alone. Content-vintage keyed per PAT-044, never mtime. |
| 4 | **Profile-trigger check** — read each `profiles/<AGENT>.md` "Staleness:" line, test the named trigger | `PRODUCTION_REVIEW.md` §2 (the step that says to do it by hand) | 7/12 self-sweep found **7 of 24 profiles past-due by their own triggers**. Queue row is a manual service rule with no instrument. |
| 5 | **`outbox/delivered/` two-state guard** — outbox tree with no new file >21d and no FROZEN banner | `sweeps_due` / staleness sweep | Closes Q4; DAEDALUS is the only agent whose outbox went dark without a banner. |
| 6 | **The COMPLETE-check** (STATUS §3 build-block **queue head**, PAT-101) | closeout | Self-indicted 8/12: *"my whole closeout battery certifies files-reached-origin and nothing certifies work-actually-finished; 8 gaps in one day, 0 found by me."* Confirmed still unbuilt 5 days later. |

**Explicitly NOT recommended:** a new boot step for `maturity_scan.py`. D-01's right fix is folding it into Production Review §1 Detect (already 14d cadence, already shells to git) + the `CHECKS.tsv` scope extension (D-06).

### 7. TOP-5 ROUTE LIST

1. **D-02 → self (`render_directory.py`)** — reverse co-registration guard. ~6 lines, already-invoked script, closes a silent gap in a **Will/PROME-facing generated artifact**. Do first.
2. **D-03 → self (`sweeps_due.py`)** — move the un-parseable-row warning to **stdout**, add skipped-count to the ✅ line, adopt §9 rc (0/1/2), and **watch all three lines print**. Only boot-invoked DAEDALUS check; only one with zero capable-case evidence. §9's origin case (`ledger_staleness`) was fixed upstream the same day — this is the same defect one directory over.
3. **D-01 + D-06 → PROME (register/scope ruling)** — maturity floor layer has no invocation site, and `CHECKS.tsv`'s scope note excludes it on a false predicate. Both are DAEDALUS-owned, but the scope-line change touches a Will-approved register — flag, don't silently widen.
4. **D-04 + D-05 → self (`falsification_scan.py`)** — port the four announcement blocks into `--tsv`; `sys.exit(1 if flags else 0)` / `2` on cannot-certify; fix `--agent` typo/bare-arg (D-07). Per §9 contract-change discipline: **survey consumers first** — sweep #3's playbook is the only one, so the batch is small.
5. **Outbox two-state → self** — banner `outbox/delivered/` FROZEN with the 8/07 cutover date, **or** strike the outbox leg from `CLAUDE.md:43`. The rule currently mandates a step abandoned 76 packets ago. Plus re-ping the 3 packets unprocessed ≥10d (HENRY ×2, BOND).

### 8. NOT READ

- `inbox/processed/` — **108 files: listed all, read headers of the 8/16-8/17 tail only.** Bodies of the ~100 older packets not read.
- `outbox/delivered/` — **26 files: listed all, read none in full.** Consumption traced by recipient-side filename/write-back, not content.
- `BLUEPRINTS/` other than `CHECK_STANDARD.md` — `STRICT_TEXT.md` and `STATE_VOCABULARY.md` (cited by CHECK_STANDARD as companion registries) **not read**; script output text therefore **not** graded against STRICT_TEXT's 10 rules or the canonical state tokens.
- `STATUS.md` — tail + targeted greps only (~49KB file); full session-log body not read. *(SYNTHESIZER NOTE: the "~49KB" figure is wrong — actual 100,051 B, verified. Preserved as delivered.)*
- `sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md` — scope header + table head only; scope conclusion verified, per-file verdicts not audited.
- `PATTERNS.tsv` (112 rows) — field-count linted only, **content not read**. PAT numbers cited here come from CLAUDE.md, CHECKS.tsv and commit messages, not from PATTERNS.tsv itself.
- `FLEET_MAP.tsv` (40 rows), `SURFACES.tsv` (12 rows) — field-count linted only, content not read.
- `render_directory.py` **never executed against the live repo** (it writes `FLEET_DIRECTORY.md`); all four capable cases ran on isolated `/tmp` copies. Live `FLEET_DIRECTORY.md` read but not regenerated.
- Recipient-side `processed/` dirs beyond the 5-packet sample and the DAEDALUS-authored census.

---

## READER 3 — BLUEPRINTS (BLUEPRINTS/ + EVOLUTION reconcile)

DAEDALUS BLUEPRINTS/ AUDIT — read-only, nothing edited. All 9 files read in full + EVOLUTION.md + STATUS.md (encode-claim grep only). Verified via git log/show/grep.

HEADLINE: every encode claim is HONEST — 12/12 VERIFIED, zero MISSING, zero overstated. The defects are all in REACHABILITY and MIRROR-WALK: the standards say what STATUS/EVOLUTION claim they say, but three of them cannot be reached from the build path, one names the wrong commit as its reference implementation, and two carry known-false or stale text that DAEDALUS itself corrected elsewhere.

### 1. ENCODE-CLAIM RECONCILIATION
| Claim | File | Verdict | Evidence |
|---|---|---|---|
| STATE_VOCABULARY Class 4 (queue/disposition, TERMINAL marking) | STATE_VOCABULARY.md | VERIFIED | :54-67, 4 tokens + Terminal? column |
| STATE_VOCABULARY Class 5 (zero/UNKNOWN/NA, 7 tokens) | STATE_VOCABULARY.md | VERIFIED | :69-86, all 7 BRENT spellings verbatim |
| STATE_VOCABULARY Class 6 (PRIMARY/MIRROR/MIRROR-WALLED) | STATE_VOCABULARY.md | VERIFIED | :88-100 |
| STRICT_TEXT rule 6 extension (issuer-primary + Class-5 on quant cols) | STRICT_TEXT.md | VERIFIED | :22 |
| STRICT_TEXT rule 7 extension (INSTRUMENT + roll-pin + REVISION POLICY + STAND-WITH-ANNOTATION) | STRICT_TEXT.md | VERIFIED | :23 |
| CHECK_STANDARD §7 transient-retry | CHECK_STANDARD.md | VERIFIED | :44-51 |
| CHECK_STANDARD §8 fetch-fallback, RATIFIED 8/17 | CHECK_STANDARD.md | VERIFIED | :53-63; PROVISIONAL struck, record file + `2efa4f2f0` both resolve |
| CHECK_STANDARD §9 shared-check rc contract (8/17 eve) | CHECK_STANDARD.md | VERIFIED | :65-72; `ccf10de89` resolves |
| Byte tier in all 3 variants (8/17 eve) | market/utility/meta | VERIFIED | market:99 (full form) · utility:35 · meta:18 (cites) |
| Messaging pointer in all 3 variants (8/16) | market/utility/meta | VERIFIED | market:113 · utility:32 · meta:44 |
| Dated falsification surface = build + L3 req | market-agent.md §4 | VERIFIED | :65 (★ clause, stamp format named). §5 half of the claim n/a — it was only ever §4 |
| Boot-time predictions scan REQUIRED | market-agent.md §5 | VERIFIED | :72 |
| PAT-103 venv re-exec | market-agent.md hygiene | VERIFIED-PARTIAL | :103 — present in market ONLY (see B7/F3) |

### 2. FINDINGS (severity-ranked)
| ID | file:line | Sev | Claim | Evidence |
|---|---|---|---|---|
| B1 | market-agent.md:99 (+ EVOLUTION.md:331) | HIGH | The byte-tier REFERENCE IMPLEMENTATION names the wrong commit. Cited `bee36f441` = "PROME → DAEDALUS: ledger_staleness.py rc=0-on-stale-findings" — a 30-line inbox packet, one file, no WATT content. The real WATT implementation is `3d2dd9707` ("byte-tier convention IMPLEMENTED locally — budget 64,000 B set from measurement"). | `git log -1 bee36f441` + `--stat`; `git log -- AGENTS/WATT/`. The companion cite `033007043` (WATT crc self-audit) IS correct. Load-bearing: this is the pointer a later adopter follows. Exactly the class DAEDALUS banked 2 days earlier — "do not let the name authenticate the record." |
| B2 | CHECK_STANDARD.md (whole file) | HIGH | The check-design standard has ZERO citation sites. `grep CHECK_STANDARD` across market-agent.md, utility-agent.md, meta-agent.md, builds/REGISTRATION_CHECKLIST.md, AGENTS/DAEDALUS/CLAUDE.md → **NONE**. Its own header calls STRICT_TEXT + STATE_VOCABULARY "companion registries" — both of those ARE wired into all 3 variants AND checklist row 15. A new agent built from a variant never learns §1-§9 exists. | Verbatim DAEDALUS doctrine one layer up: CHECKS.tsv's founding rule is "a check with no invocation site is unowned in practice, whoever wrote it" (PAT-071). A twice-Will-ratified 9-section standard is the un-invoked check. |
| B3 | meta-agent.md:50 | HIGH | Oversight section asserts as fact: "YEYOU reviews its per-push conformance." DAEDALUS's own CLAUDE.md carries a ⚠️ box stating the opposite ("nothing mechanically reviews your pushes", verified 7/30, Will-confirmed), and SPEC.md:111 carries the same correction. | `AGENTS/YEYOU/reviews/REVIEW_LOG.tsv` = header + 2 comment lines, **zero findings all-time**. The 7/30 correction walked CLAUDE.md + SPEC.md and missed the blueprint that grades every future meta-agent (PROME included). PAT-068 mirror-walk miss in the file that defines PAT-068's own class. |
| B4 | STATE_VOCABULARY.md:112, :113 | HIGH | Two malformed rows in the Enforcement map — content is DROPPED at render. Header = 3 columns. Row 112 (Class 5) has **4 cells**: the 4th holds the ⛔ **CORRECTED 2026-08-17** note saying basis_check NEVER SHIPPED and enforcement is UNBUILT — GFM drops the overflow cell. Row 113 (Class 6) has **5 cells** because the unescaped pipes in `` `PRIMARY|MIRROR|MIRROR-WALLED` `` split the row (code spans do NOT protect pipes in GFM tables) — Class 6's entire Registry-obligation cell vanishes. | Cell counts measured programmatically. Worst shape: the correction to a false "enforcement exists" record is the text that disappears, so the rendered table still reads as though `basis_check` enforces Class 5. |
| B5 | EVOLUTION.md:313-339 | HIGH | The 8/17 changelog is invisible at the file's documented read point. Header (:4) declares **"Newest first"**; all seven 8/17 entries — §8 PROVISIONAL, §8 RATIFIED, byte-tier ratification, (d)(e)(f)(g) — were **appended to the BOTTOM**, below the Roadmap table, and use `##` where every other entry uses `###`. Top of file reads 2026-08-16 (c) as latest. | `grep '^### 2026-08'` returns nothing later than 8/16; content found only at :313+. PAT-101 rule ii ("EVOLUTION entry rides the BLUEPRINTS commit") is satisfied in the commit graph and defeated in the file — a reader following the stated convention concludes the standard hasn't moved since 8/16. Verified in-commit at `8d3c4d7cb`, `8fd25137c` etc. |
| B6 | DELEGATION_TIER.md:4 · STATUS_TWO_STATE_PILOT.md:4 | MED | Six dangling provenance pointers, wrong from birth (no rename in git history). Cited `06_proposals/01_DAEDALUS_proposal-set.md` → actual `02_…`; `06_proposals/02_DAEDALUS_amendments.md` → actual `04_…`; `04_will-time-automation/03_NEXUS_delegation-tier-reply.md` → actual `04_…`; `02_repair-burden/06_NEXUS_canon-mass-reply.md` → actual `08_…`. | `ls FORUM/2026-08-07_system-review/…`; `git log --name-status` shows files created 8/7 with today's numbers, never renamed. Both files declare **"Text mode: STRICT"** and both are Will-ADOPTED gate specs — a third party grading a self-ruling under DELEGATION_TIER cannot reach the tests' provenance. |
| B7 | utility-agent.md (absent) · meta-agent.md (absent) | MED | PAT-103 interpreter-proof invocations landed in market-agent ONLY. Its sibling PAT-031 (cwd-proof) is in all three. Utility agents run fetch tools — TERRY's `chain_fetch.py` is a named §8 exemplar, and the 8/17 SFG sweep found wrapper defects at utility desks. | `grep -c PAT-103`: market 1, utility 0, meta 0. Same-family rule, asymmetric propagation. |
| B8 | utility-agent.md:72 | MED | L5 leg reads "zero YEYOU flags" with **no waivable-when-dormant qualifier**. The 7/22 Will ruling was encoded into SPEC.md:92, DAEDALUS CLAUDE.md ladder, and meta-agent.md:50 — utility was missed. | EVOLUTION 7/22 says the waiver "unblocks the LABOR/BRENT/VIOLET/**WALTER** L5 candidacies" — WALTER is a utility agent, so the one variant that missed the encode is the one holding the unblocked candidate. |
| B9 | meta-agent.md:41 | MED | Cites REGISTRATION_CHECKLIST as "**11 rows** + the meta-agent's OWN script registries, row 12" — the checklist now has **16 rows**. Phrased as a complete enumeration ("sweeps ALL surfaces in…"), so an implementer reading it under-sweeps rows 13-16 (parent behavioral registries · split/promotion seeding · STATE-TOKEN/STRICT conformance · sub-agent layer). | `grep -E '^\|\s*[0-9]+' builds/REGISTRATION_CHECKLIST.md` = 16 rows. EVOLUTION 7/31 already said "now 15 surface classes"; meta-agent never moved off 11. |
| B10 | market-agent.md (absent) | MED | Three EVOLUTION-declared "blueprint line queued" items never landed and are tracked nowhere. PAT-060 (default-zero instrument cannot falsify — "§4/§5 line queued", 7/25, 23d) · PAT-061 fix-form (7/25) · PAT-069 nonempty-assertion line (7/28, 20d). | `grep -c` across all 3 variants = 0 for each; STATUS.md's open-debt list names none of them. `finding_dated_carry_item_has_no_expiry_check` inside DAEDALUS's own changelog — a carried assertion nobody re-evaluates. |
| B11 | STATE_VOCABULARY.md:13 | LOW | Enforcement home pinned by line number: "`ledger_staleness.py` `STATIC_BANNER_MARKERS` (**:108**)". Actual location is **:136**. | `grep -n STATIC_BANNER_MARKERS scripts/ledger_staleness.py`. `feedback_behavior_language_over_hash_pinning` — cite the symbol, not the line. |
| B12 | STRICT_TEXT.md:22 · STATE_VOCABULARY.md:88, :113 | LOW | The single worked example for STRICT rule 6 / Class 6 is cited three times as `AGENTS/HOMER/RATES.tsv`. Actual path is `AGENTS/HOMER/**workbook**/RATES.tsv`. | `find AGENTS/HOMER -iname '*RATES*'`. Reader following the only named exemplar 404s. |

### 3. RESTATE-VS-CITE
Only one genuine internal contradiction, and it is in DAEDALUS's own charter rather than between variants:
**DAEDALUS/CLAUDE.md OUTPUT RULES "★ NO GUARD SHIPS UNVERIFIED" is a hand-copy of CHECK_STANDARD §3, and the two copies have already drifted on clause (b).** CLAUDE.md: "(b) its null output states what it searched" (a TEXT property, satisfiable without running anything). CHECK_STANDARD §3: "(b) its clean line was watched on a clean case" (an EXECUTION property). CLAUDE.md's (b) is actually §2's perimeter rule wearing §3's label — so an agent obeying the charter can ship a guard whose clean path was never executed, which is the exact failure §3 exists to stop. Compounded by B2: the charter never cites the standard it is paraphrasing.
Otherwise the variants cite cleanly — byte tier, messaging, STATE_VOCABULARY and STRICT_TEXT are all one-home-plus-cite. The market §8 ↔ utility §5 hygiene lanes DO restate each other in full prose (cwd-proof, git-cite, cadence-home, two-clock, ledger-append, spawned card), which is what let B7/B8 drift; that is the structural cause, not a separate finding.
Numbering/token coherence: **CLEAN**: STRICT_TEXT has exactly 10 rules; STATE_VOCABULARY Classes 1-6 sequential, no gaps or collisions; CHECK_STANDARD §1-§9 sequential. Every external citation repo-wide (17× "§8", 13× "§8 rule 3", 9× "§9", 6× "Class 4", 5× "Class 6", "rule 6/7/9") lands inside an existing section. EVOLUTION's 8/17 (f)-duplicate was self-caught and relettered to (g) with the catch recorded in-line.

### 4. GRADEABILITY — market-agent variant
**Split by vintage.** Everything added since ~7/22 is STRICT-grade decidable: §2 required columns; §3 compound-gate registration ("ships with `P(all legs | trigger state)` or an explicit not-base-rated admission" + a sessions-armed-and-unopened counter); §4 dated falsification surface (names the literal stamp `Kill rail re-derived: YYYY-MM-DD` and rules out undated prose); §5 boot scan (conditioned on "has a scripted boot"); §8 byte tier (default = ~128 B/line × line cap, act at ≥75%, stop at <70%). A grader can fail an agent on any of these from the file alone.
**The 6/27 composed sections are not gradeable and would be flagged at another agent.** §1 THESIS STRUCTURE — "decompose into independent causal channels", "mark multi-channel exposure as non-linear risk": no count, no instrument, no test. §7 STANDING DISCIPLINES — "EXPECTED_SIGNALS: track signals that *should* appear" (no cardinality, no dated form); "Boot↔Closeout symmetry: what you read at boot, you write back at closeout" (no enumeration to check against); "bump only on **material** change" (undefined — STRICT rule 4's zero-gradable-content shape). §6 is borderline. These sit inside STRICT scope (§Scope lists "checklist steps" and "gate/threshold specs"), and they fail rules 2 and 4 of DAEDALUS's own standard.
One structural note: **§8 is a catch-all.** Titled "BOTTOM LINE (required)" but carrying 15 unrelated hygiene bullets, so "market §8" ambiguously means the BOTTOM LINE rule or the hygiene lane — utility/meta cite it as "§BOTTOM LINE", EVOLUTION calls it "the hygiene lane". Worth splitting at the next touch; the byte-tier cite still resolves today.
Also: the CLAUDE.md L3 ladder cell reads "predictions **resolving**" — no count, no window. Three of that cell's four legs are decidable; that one is not.

### 5. TEMPLATE DEBT
**The template does not exist and has not since 2026-06-30.** `git show 58c30516f` = "Delete AGENTS/templates directory" — CLAUDE_TEMPLATE.md (333 lines), KB_MIGRATION_PLAYBOOK.md, MAIL_PROTOCOL_TEMPLATE.md, SCHEMA.tsv, all deleted by Will. `ls AGENTS/templates` → no such directory.
Both variants already record this correctly (market-agent.md:5 and utility-agent.md:3 both name the deletion and the commit), and EVOLUTION's roadmap row is struck ✅ MOOT. **The stale surface is DAEDALUS's own charter:** `AGENTS/DAEDALUS/CLAUDE.md:120` MEMORY MODEL still reads "Supersedes `AGENTS/templates/CLAUDE_TEMPLATE.md`; **you maintain that template as your public output**" — a standing obligation to maintain a file deleted 48 days ago, boot-loaded every session. The supersession relationship cannot be stated "in the template itself" because there is no template; the correct fix is to strike the maintenance clause from the charter, not to restore anything. (No other live doc points at `AGENTS/templates/` — remaining hits are historical EVOLUTION entries, one processed inbox packet, and a March memory file.)

### 6. TOP-5 ROUTE LIST
1. **B1** — correct `bee36f441` → `3d2dd9707` in market-agent.md:99 AND EVOLUTION.md:331 (same wrong hash in both). One-line fix, but it is a wrong-record citation in the reference clause of a same-day-ratified convention.
2. **B2** — give CHECK_STANDARD a citation site: one cite-don't-restate line in each variant's hygiene/disciplines lane + a REGISTRATION_CHECKLIST row (or fold into row 15). Then fix the §3-vs-charter drift called out in §3 above by replacing the CLAUDE.md hand-copy with a cite.
3. **B4** — repair the two malformed enforcement-map rows (merge the ⛔ correction into the obligation cell; escape the pipes as `\|`). The Class-5 correction currently does not render.
4. **B3 + B8 + B9** — one mirror-walk pass over meta-agent.md and utility-agent.md: strike the YEYOU-feed assertion (meta:50), add the dormancy waiver (utility:72), re-count the checklist (meta:41 → 16 rows).
5. **B5** — move the seven 8/17 entries to the top of EVOLUTION.md under `###`, or the "Newest first" header is false and PAT-101 rule ii buys nothing at read time. B6/B7/B10/B11/B12 ride the same touch.

### 7. NOT-READ
Read in full: all 9 BLUEPRINTS files (market-agent, utility-agent, meta-agent, STRICT_TEXT, STATE_VOCABULARY, CHECK_STANDARD, BEST_PRACTICES, DELEGATION_TIER, STATUS_TWO_STATE_PILOT) + EVOLUTION.md lines 1-189 and 288-339.
NOT read: **EVOLUTION.md lines 190-287** (pre-2026-07-07 history — skimmed via `grep '^### 2026-08'` and targeted PAT greps only; a contradiction living purely in June/early-July entries would not have been seen). **STATUS.md** — encode-claim grep only per instructions, never read linearly; its 900-byte lines were sampled by regex window, so a claim phrased without any of my keywords would be missed. **builds/REGISTRATION_CHECKLIST.md** — row headers and row 15 body only, not the full row text. **profiles/**, **upgrades/**, **CHECKS.tsv**, **SURFACES.tsv**, **PATTERNS.tsv** (except PAT-060/061/069 rows), **sweeps/** — out of slice. Not verified: whether the 5 CHECK_STANDARD §8 exemplar scripts actually implement what §8 attributes to them (I confirmed only that the files exist, under agent dirs). Nothing edited.

---

## READER 4 — REGISTERS (FLEET_MAP, FLEET_DIRECTORY, PATTERNS, CHECKS, SURFACES, sweeps/REGISTRY)

### 1. FINDINGS (ranked by severity)

| ID | file:row | Sev | Claim | Evidence |
|---|---|---|---|---|
| **D1** | `PATTERNS.tsv` cols 4+6, rows PAT-078→PAT-110 | **HIGH** | Both controlled-vocabulary columns forked into two incompatible token sets and **interleave** — the file is no longer machine-filterable on either. | `Type`: 91 rows use `{PATTERN, ANTI}`; 20 rows use free-text topical labels (`coordination`×6, `method`×3, `instrument-design`×3, `register-hygiene`×2, `spec-design`, `protocol-design`, `measurement`, `lifecycle`, `grading`, `doc-hygiene`). Not a clean migration: 078–087 topical → **088–092 revert to PATTERN/ANTI** → 093–102 topical → 103–110 revert. `Conf`: 93 rows Admiralty (`A1/A2/B1/B2`), 18 rows `H/M`, and PAT-105 mixes both (`ANTI` + `H`). A consumer filtering `Type=='ANTI'` silently misses PAT-105-class rows in the topical band. **This is PAT-075 ("where a reader parses a state token, the token is an INTERFACE") violated inside the file that stores PAT-075** — and DAEDALUS's own OUTPUT RULES self-binding clause names FLEET_MAP / SURFACES / sweep verdicts but **not** PATTERNS, so nothing binds it. |
| **D2** | `FLEET_MAP.tsv:6` (CARL, `Next_upgrade`) | **HIGH** | CARL's `Next_upgrade` carries **two clauses its own `Notes` column refuted 10 days ago**, and this is the cell that renders into the Will/PROME-facing directory. | Cell reads `"L5: consistency_check Phases B/C … ⚠️ POP refresh-then-demote due Jul-24 — 2-DAY calendar item (standing plan: DAEDALUS executes if CARL doesn't schedule)"`. Same row's 8/7 Notes: `"consistency_check B/D/E/F/G ALL SHIPPED (:696/:950/:983/:521/:353) — next_upgrade 'Phases B/C' text OBSOLETE"` and `"POP reader-claim FALSIFIED: demote WAS executed on-gate 7/24 (262ea22c9)"`. Renders to `FLEET_DIRECTORY.md:20` as `"L5: consistency_check Phases B/C"`. DAEDALUS's own **PAT-109** (two contradictory bindings in one file; every prose claim points at the loser) and **PAT-098** (representation is what a consumer acts on). |
| **D3** | `FLEET_MAP.tsv` WATT + FALCON, `Next_upgrade` | **HIGH** | Two rows demand profile builds that **already exist**, one of them re-scored 8 days *after* the build. | WATT cell: `"+ profiles/WATT.md BUILD (never profiled through two reviews)"`. FALCON cell: `"+ profiles/FALCON.md BUILD (top cohort priority — among the heaviest agents, never profiled)"`. `ls profiles/` → both present. `sweeps/REGISTRY.tsv:14` states `"BUILD queue COMPLETE 8/7 PM — all 8 built in one day (FALCON, DEWEY, WATT, OSPREY, VULCAN, OZK, HOMER, WAL)"`. FALCON's `Last_scored` = **2026-08-15**. Worse for WATT: commit `d61b7d084` (8/17 12:08) edited **both** `profiles/WATT.md` *and* the WATT FLEET_MAP row in one commit, and left `"profiles/WATT.md BUILD"` standing. |
| **D4** | `FLEET_MAP.tsv:2` (DAEDALUS self-row) | **HIGH** | The architect's own row is again the stalest-relative-to-activity in the register — `Last_scored 2026-08-12`, **untouched across its heaviest five-day run on record**. | Verified: no commit since 8/12 emits a `+DAEDALUS\t` line in `FLEET_MAP.tsv`. Unrecorded in that window: war-triad review (8/15), FERT build + registration (8/16), and the 8/17 "four-movement day" — PROME graded first Meta L5, SFG class sweep, CHECK_STANDARD S8 ratified, SAM+BRENT 6-reader review, **8 new patterns PAT-103→110**. Row's `Next_upgrade` still names "the 4 priority profile refreshes" while the queue was re-headed to SAM/BRENT on 8/17. This is **PAT-050 by its own name** ("the architect's own surfaces rot in exactly the classes it polices"), n=3 (7/12 self-sweep, 8/12 self-finding, now). |
| **D5** | `SURFACES.tsv:13` (`scripts/`) | **HIGH** | Row contradicts itself inside one row, and its `Gap` cell was closed by DAEDALUS's own CHECKS.tsv 14 days ago. | `Owner`=`DAEDALUS`, `State`=`OWNED`, `Gap`= *"ownership gap CLOSED — granted to DAEDALUS"* — while the same row's `Notes` **ends** with `"Ownership of scripts/ itself REMAINS UNASSIGNED — Will-docketed 8/2."` Separately, `Gap` still reads *"no registry of what exists or who maintains it"* — `CHECKS.tsv` was created **2026-08-03** as exactly that registry (23 rows). `Last_reviewed` = 2026-07-31. |
| **D6** | `SURFACES.tsv:12` (`SIGNALS/`) | **HIGH** | `State = DEAD-UNBANNERED` is **false** — the artifact carries a FROZEN banner, applied 12 minutes after this row was last committed, and the row was never updated. | `SIGNALS/README.md:3` = `"⚠️ FROZEN 2026-08-11 — dead surface, do not cite as current…"`, commit `0f12be686` at **2026-08-11 18:09**, whose message credits *"retirement owner per DAEDALUS SURFACES.tsv row."* `SURFACES.tsv` last commit `5e72a69ce` at **17:57** same day. `Last_reviewed` still 2026-07-30. This is the register's **own row-8 lesson recurring** ("a register that advertises a closed gap is the exact rot class the register exists to catch"). |
| **D7** | `sweeps/PRODUCTION_REVIEW.md:72` Run Log | MED | Run #3 (2026-08-07) — the largest review on record — **is absent from the playbook's own Run Log**. | Run Log rows: `2026-07-22`, `2026-07-04`. Only. Registry `last_run` = 2026-08-07 with a 900-char findings cell; report exists at `upgrades/PRODUCTION_REVIEW_2026-08-07.md` (11,849 B, 8/7 11:58). The playbook is the surface that would prove the run to a second reader; only the registry's self-attestation covers it. |
| **D8** | `sweeps/REGISTRY.tsv:6` and `:14` | MED | Two `last_run` cells lag work recorded **in their own `last_findings` text**. | PROME sweep: `last_run=2026-08-16`, findings cell ends `"· 8/17 TARGETED RE-CHECK … PASS 4/4 → PROME L5"`, and `PROME_SWEEP.md` Run Log carries a **row #1b dated 2026-08-17**. Profile-refresh queue: `last_run=2026-08-12`, findings cell ends `"· 8/17 STRUCTURE REVIEW: queue re-headed — SAM FIRST … Both re-graded L4 8/17"`. Direction is conservative (fires early), but the cell `sweeps_due.py` parses is wrong on both. |
| **D9** | `CHECKS.tsv:5` (header) | MED | The promised **on-FAIL column does not exist**, ≥4 register passes after it was promised. | `BLUEPRINTS/CHECK_STANDARD.md:38`: *"`CHECKS.tsv` gains a per-check on-FAIL column at the next register pass (PAT-084)."* (born 8/11). Actual header: `Check\|Owner\|Detects\|Invoked_by\|State\|Null_meaning\|Last_verified_run\|Gap\|Notes` — 9 fields, no on-FAIL. Register passes since: 8/12, 8/14, 8/17 (×2 row re-cuts). |
| **D10** | `scripts/sweeps_due.py:7` | MED | PAT-110's exact twin sits in DAEDALUS's own boot step and went unswept on the day PAT-110 was banked. | Docstring: *"Detection only … **Exit code is always 0 (an alert, not a gate)**."* PAT-110 (banked **today**, 12:53, commit `073736798`): *"An 'alert, not a gate' always-0 exit contract on a SHARED check is a standing silent-fallback-green exposure … fix producer AND consumers in ONE batch."* The 8/17 batch fixed `ledger_staleness.py` + 7 consumers; this file was not swept. **Mitigant:** grep finds no rc-keyed consumer — sole invoker is `CLAUDE.md:41`, a human read — so the exposure is latent, not live. Out of `CHECKS.tsv` scope by design (agent-local). |
| **D11** | `FLEET_MAP.tsv` — MIDAS, OSPREY, HOMER, AEOLUS, CREED, CARL | MED | Six `Next_upgrade` cells are gated on clocks that have already expired; two were **re-scored after their own window closed** and left intact. | MIDAS: `"MIDAS-05 grade ~7/23 + WGC Q2 GDT kill-test late-July"` (25d past; shortest `Gaps` cell in the file at 197 chars = least-serviced row). **OSPREY: `"OSP-01/02/03 resolving (window Aug 1-3)"` with `Last_scored=2026-08-15`** — scored 12 days after the window shut. HOMER: `"HOM-01 resolving (~7/30)"`, scored 8/7. AEOLUS: `"PROME spawn flag routed 7/22 stands"` (26d). CREED: `"~early-mid Aug clock"`. CARL: see D2. DAEDALUS's own **PAT-080** + **PAT-089** (*"a carried ASSERTION is a string; reading it never evaluates it"*). |
| **D12** | `SURFACES.tsv:11` (`MESSAGING/`) | MED | The row's **own written re-check trigger fired 8/16** and the row was not touched. | Cell: *"Low stakes while the cohort is 2. **Re-check if the allowlist widens.**"* Root `CLAUDE.md` §Data Hygiene, Will-ruled 2026-08-16: cross-session messaging is *"at every session's disposal — a standing tool, not a coordinator-only lane"*; `MESSAGING/CROSS_SESSION_MESSAGING.md` exists. `Last_reviewed` = 2026-07-30, `State` = `UNMECHANIZED`. |
| **D13** | `SURFACES.tsv:5` (`FORGE/`) | MED | `State=SCHEDULED` against a batch window that closed 15 days ago; the scheduled fix is **still not in the code**. | Cell: *"Fix + the M5 vocabulary add ride the **7/31-8/2 gated batch** … the FORGE path-teach half still rides the 7/31-8/2 batch."* `grep -n FORGE scripts/ledger_staleness.py` → **zero hits**. The enforcer still cannot reach `FORGE/STATUS.md` ("the repo's most-referenced path, 499 refs"). `SCHEDULED` with an elapsed date is indistinguishable from `UNMECHANIZED` and reads better — PAT-062's shape (stale-and-flattering). |
| **D14** | `sweeps/STALENESS_SWEEP.md:63-65` | LOW | Run Log rows are out of chronological order in both directions. | Order on disk: `2026-07-04`, `2026-08-11`, `2026-07-25`. The 8/11 run was inserted mid-table. Same defect class DAEDALUS flagged against HENRY on 8/7. |
| **D15** | `FLEET_DIRECTORY.md` vs `FLEET_MAP.tsv` | LOW | Generated file was **not** regenerated after the last FLEET_MAP change — protocol step 7 skipped, nothing detects it. | `FLEET_MAP.tsv` last content change `d61b7d084` **8/17 12:08**; `FLEET_DIRECTORY.md` last change `3708fd0a5` **8/17 11:39**. **Content-benign this time** — diffed the row: only WATT's `Notes` changed, and the directory renders `Class/Level/Next_upgrade` only (spot-checked CARL/HENRY/MIDAS/PROME/FALCON against source: all faithful). The finding is that the guard is a prose instruction with no enforcement — the *next* edit could hit a rendered field. |
| **D16** | `FLEET_MAP.tsv` WATT, `Last_scored` | LOW | Row annotated 8/17 (commit message: *"FLEET_MAP row annotated"*) while `Last_scored` stays `2026-08-07`. Schema has no `Last_touched`, so "annotated" and "unexamined-since" are indistinguishable in the only currency field. Defensible reading, but the ambiguity is unstated. |
| **D17** | `scripts/sweeps_due.py:30-37` | LOW | An un-parseable `last_run`/`cadence_days` `continue`s **before** `tracked += 1`, so a broken row silently drops out of `"✅ sweeps: none due (N tracked)"` — the reassuring line under-counts without saying so. It does name the row on **stderr**, which per PAT-106/§8 is the channel wrappers swallow. |
| **D18** | `PATTERNS.tsv` (whole file) | LOW→MED | **No dedup or supersession convention exists** — see §5. |

**Schema validity: CLEAN.** Whole-file field counts — `FLEET_MAP` 40×9, `PATTERNS` 112×7, `CHECKS` 23×9, `SURFACES` 12×8, `REGISTRY` 12×6. Every 1-field line is a `#` comment row and all parsers correctly skip them. **No recurrence of the PAT-093/094/095 5-field class anywhere.** IDs unique, no duplicates. The 8/11-era defect did not repeat *structurally* — but D1 shows the same era forked the file **semantically** instead, which no field-count check can see.

### 2. PER-REGISTER READER MAP

| Register | Who reads it | When | Verdict |
|---|---|---|---|
| `FLEET_MAP.tsv` | `render_directory.py` (machine, joins w/ ROSTER); DAEDALUS `CLAUDE.md:41` SPAWN step 3 | Every DAEDALUS boot + every directory regen | **READ — the healthiest.** Two readers, one mechanical. |
| `FLEET_DIRECTORY.md` | `canon_check.py:122`; `falsification_scan.py:32`; Production Review §; PROME/Will by hand | Prod Review (14d) + 2 scripts at runtime | **READ.** The only register with non-DAEDALUS machine consumers. |
| `sweeps/REGISTRY.tsv` | `sweeps_due.py` (SPAWN step 5); `PROME/ROSTER.md:25` points at it as canonical cadence | Every DAEDALUS boot | **READ.** Best-instrumented. |
| `CHECKS.tsv` | `sweeps/PRODUCTION_REVIEW.md:53` + 3 registry queue rows | Each Production Review (14d) + any `scripts/` change | **READ, on the longest cadence.** Real, documented, and it fires — the 8/7 invocation-mapping pass found + fixed 2 stale rows. |
| `SURFACES.tsv` | **NOBODY on a schedule.** Named in `CLAUDE.md:125` and `:155` as a *memory-model artifact*; no sweep playbook, no registry queue row, no script opens it. | — | **🔴 READERLESS — PAT-108 by its own definition.** Direct cause of D5, D6, D12, D13: 4 of 11 rows carry a state cell the world has moved past, and 8 of 11 `Last_reviewed` cells still read 2026-07-30/31. |
| `PATTERNS.tsv` | `CLAUDE.md:41` SPAWN step 3 — *"Apply them; don't re-learn them."* Written by `UPGRADE_PROTOCOL.md:45` and `PRODUCTION_REVIEW.md:36`. | Every boot (nominally) | **🟠 WRITE-MOSTLY.** At **154 KB / 112 rows** with rows averaging 1.4 KB it is not credibly re-read whole, and **nothing ever re-reads an OLD row for revision, merge, or retirement**. The 291 in-file `PAT-0xx` cross-references show retrieval works *when the author already remembers the ID* — precisely the case where retrieval isn't needed. D1 is the proof: a schema fork ran 33 rows without a single reader noticing. |

**Direct answers.** *Does anything re-read old PATTERNS rows?* **No — no documented step, at any cadence.** *Does CHECKS.tsv's promised on-FAIL column exist?* **No (D9).**

### 3. SWEEP-REGISTRY RECONCILIATION (11 registered)

| Sweep | Registry `last_run` | Playbook Run Log | Git / artifact | Verdict |
|---|---|---|---|---|
| Fleet Staleness (21d) | 2026-08-11 | 7/04, **8/11**, 7/25 — *out of order* | `5e72a69ce` 8/11 ✓ | ✅ agrees · **D14** ordering |
| Fleet Production Review (14d) | 2026-08-07 | 7/22, 7/04 — **no 8/07 row** | report exists 8/7 ✓ | 🔴 **D7 mismatch** |
| Falsification Freshness (21d) | 2026-08-03 | 7/11 pilot, 8/03 RUN #1 | defect-pair fix `15eb35c0b` 8/17 ✓ | ✅ agrees |
| Harness Audit (90d) | 2026-07-07 | 7/07 ✓ | artifact ✓ | ✅ agrees |
| PROME Spine (21d) | 2026-08-16 | #0 7/28, #1 8/16, **#1b 8/17** | reports file ✓ | 🟠 **D8** — cell 1d behind playbook |
| Q: check-registry (21d) | 2026-08-07 | → PRODUCTION_REVIEW (no 8/7 row) | registry cell only | 🟠 self-attesting via D7 |
| Q: invocation-mapping (21d) | 2026-08-07 | → same | CHECKS rows re-cut 8/12–8/17 ✓ | ✅ substantiated |
| Q: roster-health (21d) | 2026-08-07 | → same | FLEET_MAP+directory 8/17 ✓ | ✅ substantiated |
| Q: shared-guard-standard (45d) | 2026-08-11 | → STATE_VOCABULARY.md | CHECK_STANDARD born 8/11 ✓ | ✅ agrees |
| Q: unwired-checks (21d) | 2026-08-07 | → PRODUCTION_REVIEW | CHECKS states verified ✓ | ✅ agrees |
| Q: profile-refresh (21d) | 2026-08-12 | → UPGRADE_PROTOCOL | own findings cell records 8/17 work | 🟠 **D8** — cell 5d behind |

**Overdue:** none. All 11 compute inside cadence at 2026-08-17. **Cadence math:** correct. Two soft edges: D17 (broken row vanishes from the tracked count) and D8 (garbage-in, fires-early direction).

### 4. SURFACES.tsv SPOT-CHECKS (5 rows at artifacts)

| Row | Cell claim | At the artifact | Verdict |
|---|---|---|---|
| `SIGNALS/` | `DEAD-UNBANNERED` | FROZEN banner present since 8/11 18:09 | 🔴 **FALSE (D6)** |
| `scripts/` | `OWNED` / gap = "no registry exists" | Owned ✓ but Notes says UNASSIGNED; `CHECKS.tsv` **is** the registry, since 8/3 | 🔴 **SELF-CONTRADICTORY + STALE (D5)** |
| `FORGE/` | `SCHEDULED` on 7/31-8/2 batch | `grep FORGE scripts/ledger_staleness.py` → 0 hits | 🔴 **UNDELIVERED, 15d (D13)** |
| `MESSAGING/` | "re-check if the allowlist widens" | Widened fleet-wide 8/16 | 🟠 **TRIGGER FIRED, UNSERVICED (D12)** |
| `AGENTS.md` | mechanism `None found`; "cheap candidate: fold a diff into render_directory.py" | `grep AGENTS.md render_directory.py` → 0 hits | ✅ **cell is HONEST** (still unmechanized, correctly stated) |

### 5. PATTERNS GROWTH DISCIPLINE

**There is no dedup, merge, or supersession convention.** Grepped `CLAUDE.md`, `SPEC.md`, `UPGRADE_PROTOCOL.md`, `EVOLUTION.md`, all sweep playbooks, all blueprints: nothing. The only supersession machinery in the file is the ad-hoc `PAT-074b` suffix — used **once** in 112 rows. Append-only by omission.

**The asymmetry is the finding:** root `CLAUDE.md`'s MEMORY.md header — a standard DAEDALUS polices and enforces via `memory_index_check.py` — states *"Dedup-before-create: extending an existing memory is the DEFAULT."* DAEDALUS applies that rule to the fleet's memory and none to its own learning register. PAT-050 again.

**Overlapping clusters (6 found):**
1. **The green-check family — 6 IDs, one class.** PAT-074 · PAT-074b · PAT-083 · PAT-105 · PAT-106 · PAT-110. Only 074/074b are ID-linked; the other four float free.
2. **The write-back / claimed-side-effect family — 4 IDs.** PAT-032 · PAT-087 · PAT-101 · PAT-102. Same mechanism, four entries, no cross-reference in any `Pattern` head.
3. **The two-state banner family — 4 IDs.** PAT-023 · **PAT-025 (which literally says "PAT-023 is a CONFIRMED FLEET-WIDE pattern" — a frequency observation about 023, not a distinct pattern; strongest single merge candidate)** · PAT-057 · PAT-085.
4. **The expired-obligation family — 5 IDs.** PAT-041 · PAT-052 · PAT-080 · PAT-089 · PAT-091.
5. **The publisher/consumer-routing family — 3 IDs.** PAT-063 · PAT-099 · PAT-108.
6. **The representation-as-interface family — 3 IDs.** PAT-069 · PAT-075 · PAT-098.

### 6. TOP-5 ROUTE LIST
1. **D1 — PATTERNS vocabulary fork.** Silent, load-bearing, unbounded. Fix = declare the canon (extend `STATE_VOCABULARY.md` to cover PATTERNS `Type`/`Conf`), backfill 33 rows, add PATTERNS to the OUTPUT RULES self-binding list.
2. **D2 + D3 + D11 — FLEET_MAP `Next_upgrade` rot (8 rows).** Highest *consumer* impact: this column is the product handed to Will and PROME via `FLEET_DIRECTORY.md`. Fix by pattern, not by this line list.
3. **D5 + D6 + D12 + D13 — SURFACES.tsv is readerless (PAT-108).** Don't fix the four rows; fix the absence of a reading moment. Cheapest form: a `Queue: surfaces-currency` row in `sweeps/REGISTRY.tsv` at N=21, serviced at the Production Review beside the three CHECKS queues that already work.
4. **D4 — own row 5 days behind the heaviest run on record.** PAT-050 n=3. Worth escalating as a *mechanism* question, not a row edit: two of three instances were caught by a directed audit, none by DAEDALUS's own closeout.
5. **D9 + D10 — self-binding gaps in the check layer.** The on-FAIL column 6 days and ≥4 register passes owed; `sweeps_due.py` is PAT-110's twin, unswept the day PAT-110 shipped. Both one-line fixes; both the class where the author's own habit failed.

### 7. NOT-READ LIST
- **`FLEET_MAP.tsv` `Gaps` + `Notes` prose, 29 of 40 rows** — rows 1–11 read in full; the rest field-extracted. Contradictions living *only* inside a long `Notes` cell on rows 12–40 would not be caught. The same defect on OZK/WAL/LIQUID/SHADE (Notes 3–4 KB each) is unaudited.
- **Sweep playbook bodies** — Run Log sections + surrounding context only.
- **`EVOLUTION.md` (89 KB)** and **`STATUS.md` (100 KB)** — not in the assigned slice; used only as grep-exclusions. Both may contain the missing 8/7 Production Review record (D7) or a self-row note (D4) that would soften those findings.
- **`upgrades/*` reports** — existence and timestamps verified, contents not read. D7 rests on the playbook's Run Log being the register-of-record, which is how `PRODUCTION_REVIEW.md:61` specifies it.
- **`profiles/` contents (34 files)** — inventory listed; no profile read.
- **Script source** — read `sweeps_due.py` in full; `render_directory.py`, `maturity_scan.py`, `falsification_scan.py`, `canon_check.py`, `ledger_staleness.py` grepped, not read. D15's "content-benign" call rests on a field-level git diff plus 5 hand spot-checks — if `render_directory.py` also emits anything from `Notes`, D15 upgrades from LOW.
- **`BLUEPRINTS/`** — only `CHECK_STANDARD.md` §5 read (for D9). `STRICT_TEXT.md` and `STATE_VOCABULARY.md` unread, so D1's no-canon claim is grounded in the CLAUDE.md self-binding clause, not in reading STATE_VOCABULARY itself. **Verify there before acting on D1.**
No files were edited.

---

## READER 5 — WORKPRODUCT (profiles/, upgrades/, builds/, design/)

### 1. `upgrades/` BANNER CENSUS — 71 docs

| Status form | Count | Docs |
|---|---|---|
| **Top-of-file banner** | **16** | BOND_CARD · HAWK_CARD · HENRY_CARD · LABOR_CARD · NEXUS_CARD · RED_CARD · TERRY_CARD · WALTER_CARD · FLEET_DIRECTORY_BUILD_PLAN · LABOR_GAP_ASSESSMENT · CARL_SUBAGENT_AUDIT · DEWEY_DRAFTS_REVIEW · **CODEX_CROSS_REVIEW · FIXBATCH_REPORT · WP1_TALOS · WP3_MOLD** (last 4 = the 8/11 pass) |
| **`**Status:**` header line** | **8** | BATCH_01/02/03 · HANDLE_SWEEP · TRADE_STALENESS_SWEEP · UTILITY_FIRMING · CORAL_S8_PROPOSAL · WP2_KORE |
| **NONE — no doc-level state in first 6 lines** | **47** | breakdown below |

Breakdown of the 47:
| Sub-class | n | Which | Verdict |
|---|---|---|---|
| **`*_CARD.md` — the work-queue class** | **16** | REGINALD·ORACLE·YEYOU·ZHAO·CARL·HANS·MARCO·SAM·BRENT·BROCK·LIQUID·VIOLET·CORAL·OTTO·CREED·SHADE | **AMBIGUOUS.** e.g. *"Nothing applied — this is the queue"* (LIQUID:5, VIOLET:5) with no closure state. 8 of 16 have **zero** status token anywhere (MARCO, SAM, ZHAO, LIQUID, VIOLET, REGINALD, ORACLE, YEYOU). Others carry per-ROW `✅ APPLIED` cells but no doc-level verdict. Ages 36–50d. |
| **Aged dated audit/QC records (26–56d), findings routed, no closure tracking** | **12** | AEOLUS_QC · LABOR_QC · DAEDALUS_SELF_SWEEP ×2 · PRODUCTION_REVIEW_2026-07-22 · BRENT_AUDIT_07-28 · PROME_AUDIT_07-28 · FORGE_AUDIT_07-30 · RAV_CHANGE_REVIEW_07-30 · TERRY_ARCH_AUDIT_07-30 · VIOLET_LIQUID_FIRMING · WP4_ECHO | **AMBIGUOUS-LITE.** PROME_AUDIT has 8 inbound refs (3 outside DAEDALUS) — actively cited. |
| **Recent dated records (≤10d)** | **~16** | 8/07 ×1 · 8/11 ×2 · 8/12 ×2 · 8/15 ×1 · 8/16 ×1 · 8/17 ×9 | **ACCEPTABLE** — plainly current-session records. |

**Stale-ambiguous total: ~28** (16 cards + 12 aged audit records).

**Did the known 13 get fixed? — NO, 4 of ~13.** Commit `ff75245b0` (8/11) added a `🗄 CLOSED 2026-08-11` line to exactly **four** files (verified in the diff stat). **Nothing has been bannered since.** The finding appears **nowhere** in STATUS.md's "Open / structural debt" section — only in the 8/11 STATUS history line and the STALENESS_SWEEP Run Log. It is a recorded finding with **no carrier**.

### 2. PROFILE CURRENCY — top 10 most stale

| # | Profile | Body vintage | Own rule | Days over | Subject commits since | Banner / trigger state |
|---|---|---|---|---|---|---|
| **1** | **WALTER** | 7/04 (git 7/22) | **">20 days"** (its own text) | **+24d** | **391** (fleet-highest) | 7/22 Δ-banner "REFRESH-AT-TOUCH" — **unserviced 26d** |
| **2** | **VIOLET** | 7/04 (git 7/22) | >45d | +0 (expires 8/18) | **157** | 7/22 Δ-banner — unserviced 26d |
| **3** | **CARL** | 7/10 refresh | >45d or matrix re-scores | matrix trigger fired | **133** | 7/22 Δ-banner — unserviced 26d |
| **4** | **NEXUS** | 7/04 | >45d or "next live pass" | session trigger fired | **107** | 7/22 Δ-banner — unserviced 26d |
| **5** | **MARCO** | 7/10 | >45d | −7d | **89** | No banner. Registry calls it *"correctly quiet"* — but the 8/11 sweep separately called MARCO a *"third-flag MECHANISM indictment"* |
| **6** | **BOND** | 6/29 | >45d | **+49d body** | 82 | 7/22 Δ-banner, self-labelled **"PRIORITY #4"** — unserviced 26d |
| **7** | **ORACLE** | **6/29** | >45d | **+4d, EXPIRED** | 70 | **No banner.** DAEDALUS's own registry row wrote *"ORACLE expires ~8/13"* — expired 4d ago, unserviced |
| **8** | **AEOLUS** | 7/22 | >45d | −19d | 63 | **Named §3b queue-head on 8/11** — unserviced 6d; Falsification Sweep #2 is ~8/24 |
| **9** | **ZHAO** | 7/07 | *"after ZHAO's next 2-3 sessions"* or >45d | session trigger long fired | 55 | No banner |
| **10** | **CORAL** | **6/27** | **">30 days"** | **+21d** | 48 | 7/22 Δ-banner — unserviced 26d |

Also: **BROCK** — its 7/22 banner's own dated re-check (*"Next check: BDC marks-window aftermath (~7/28+)"*) fired **20 days ago**, unserviced (77 commits since).

**Does the stated queue match measured staleness? — NO.**
- REGISTRY row 14 (amended 8/17): SAM/BRENT head discharged 8/17; remaining stated order **AEOLUS > BOND > NEXUS > WALTER > ZHAO > CARL**.
- Measured, **WALTER ranks #1 by a wide margin** (only profile past its *own explicitly shorter* clock, +24d, fleet-highest commit volume) yet sits **4th**.
- **ORACLE, VIOLET and CORAL do not appear in the ordered list at all**, despite ORACLE's clock having expired and VIOLET/CORAL carrying 157/48 commits of unread change.
- Root cause visible in the registry row's own text: *"Profile-staleness should be WORK-VOLUME-KEYED"* — noted 8/07, never applied to the ordering.

⚠️ **Banner-placement inconsistency, introduced 8/17:** SAM.md and BRENT.md put their `Δ 2026-08-17 — BODY SUPERSEDED IN PART` blocks at **line 37** and **line 81**, while the entire 7/22 cohort puts them at **line 3**. A reader opening SAM.md sees `Built: 2026-07-10 … Staleness: …or >45d` and no warning; the supersede notice is 37 lines down.

### 3. PAT-100 COMPLIANCE

| Fan-out | Readers | Companion | NOT-READ lists | Verdict |
|---|---|---|---|---|
| RED audit 8/12 | 3 | `RED_AUDIT_2026-08-12_READER_REPORTS.md` | 5 mentions | ✅ **COMPLIANT** (founding case) |
| WAR triad 8/15 | 3 | `WAR_TRIAD_REVIEW_2026-08-15_READER_REPORTS.md` | 8 mentions | ⚠️ **COMPANION PRESENT, SYNTHESIS ABSENT** — no `WAR_TRIAD_REVIEW_2026-08-15.md` exists in `upgrades/`. Synthesis lives only in STATUS.md, 3 outbox packets, and `PROME/archive/HANDOFF_2026-08-15_WAR-TRIAD.md`. The mandated pair is inverted. |
| PROME sweep run-1 8/16 | 2 | `PROME_SWEEP_RUN1_2026-08-16_READER_REPORTS.md` | 10 mentions | ✅ COMPLIANT |
| SFG sweep 8/17 | 4 | `SFG_SWEEP_2026-08-17_READER_REPORTS.md` | 7 mentions | ✅ COMPLIANT |
| **SAM+BRENT architecture review 8/17** | **6** | **NO `*_READER_REPORTS.md` file** — six individually-named cluster docs + 1 SYNTHESIS instead | all 6 carry NOT-READ | ⚠️ **SUBSTANCE-COMPLIANT, NAME-NONCOMPLIANT.** Any check keyed on the filename reads it as a **miss** — `finding_scan_keyed_on_naming_reads_local_form_as_absence` operating on DAEDALUS's own register. |
| PRODUCTION_REVIEW 8/07 (9 readers) · STALENESS_SWEEP 8/11 (6 readers) | 9 / 6 | none | — | Pre-date PAT-100 (8/12) → **grandfathered, but nothing on either doc says so.** |

### 4. RETIREMENT RULE (>60d AND not boot-read AND not referenced)

- **`AGENTS/DAEDALUS/` has NO `archive/` subdirectory.** The retirement rule has never been exercised in this tree.
- **Strict candidates today: ZERO.** Oldest git vintage 6/29 (49d).
- **A wave lands in ~2–3 weeks.** ~20 docs cross 60d between **~2026-09-05 and ~2026-09-11**. MARCO_CARD (1 ref, 0 outside DAEDALUS) and SAM_CARD (1 ref, 0 outside) meet leg-3 **now**; LIQUID/VIOLET/ZHAO cards each hold 1 external ref. No destination directory, no queue row.
- **`builds/*/` subdirs are the out-of-scope residue of the 8/11 pass:** 10 one-shot execution records dated 7/12, **all unbannered**, identical in class to the four the 8/11 pass did banner. The pass was scoped to `upgrades/` only.

### 5. CLAIMED-VS-PRESENT — all 7 STATUS-named artifacts verified

| Claimed artifact | Present? | Content matches? |
|---|---|---|
| `upgrades/LEDGER_STALENESS_RC_CONTRACT_2026-08-17.md` | ✅ 6.3KB | ✅ |
| `sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md` | ✅ 42KB | ✅ |
| `upgrades/PROME_SWEEP_RUN1_2026-08-16_READER_REPORTS.md` | ✅ 41.5KB | ✅ |
| `design/2026-08-15_LEDGER_STALENESS_REGISTERED_SURFACES_SPEC.md` | ✅ 4KB | ✅ |
| `builds/FERT_RECHARTER_2026-08-16.md` | ✅ 5.4KB | ✅ |
| `upgrades/RED_AUDIT_2026-08-12.md` + `_READER_REPORTS.md` | ✅ both | ✅ |
| `upgrades/PROFILE_S3_AUDIT_2026-08-11.md` | ✅ 2.9KB | ✅ census reconciles |

**No missing artifacts. But two status lines are materially wrong:**
- `builds/wal_promotion/PROMOTION_REVIEW.md:3` — *"Execution remains gated on WP-W0"*. **WAL was promoted 2026-07-25** (root CLAUDE.md). 23 days stale; reads as a live gate.
- `design/2026-07-31_STE_WRITING_STANDARD_ASSESSMENT.md:3` — *"Status: ASSESSMENT ONLY — nothing proposed here is built or wired"*. Both recommendations **shipped the same day** and are now root-CLAUDE.md canon. A reader concludes the standard was never built.

### 6. DISCOVERABILITY / STRUCTURE
- **No index exists** for `profiles/` or `upgrades/`. Retrieval is 100% filename-convention-dependent.
- **`upgrades/` filename conventions — 6 competing patterns**; ~30 of 71 have no date at all; WP-report names omit the subject agent (WP1_TALOS is about CARL, WP3_MOLD about PHAN).
- **Filename date ≠ currency, 4 confirmed instances** (the 8/11-bannered four sort as July docs).
- **`builds/` and `design/` are the healthy counter-examples:** `design/` uniformly dated with `**Status:**` on 8 of 8; `builds/` carries banners on 5 of 6 specs.

### FINDINGS
| ID | File | Sev | Claim | Evidence |
|---|---|---|---|---|
| **D-1** | `sweeps/STALENESS_SWEEP.md` Run Log 8/11 + `STATUS.md` | **HIGH** | The self-found "13 unbannered upgrade docs" was fixed 4-of-13 and has **no carrier** — in no debt list, no queue row, no DOCKET row | commit `ff75245b0` diff stat touches exactly 4 upgrades files; grep of STATUS "Open / structural debt" for "unbanner" = 0 hits; 16 CARD docs + 12 aged audit records remain stateless today |
| **D-2** | `profiles/WALTER.md` | **HIGH** | The fleet's fastest-moving agent has the most-overdue profile, and the refresh queue ranks it 4th | body 7/04, own rule ">20 days", 391 commits since 7/22; REGISTRY order = AEOLUS>BOND>NEXUS>**WALTER** |
| **D-3** | `profiles/{VIOLET,WALTER,CARL,NEXUS,BOND,CORAL}.md` | **HIGH** | Six 7/22 Δ-banners saying "full refresh executes at the next firming touch" are **26 days unserviced** — the deferral failure the 8/07 review already named | identical line-3 banner text in all six; PRODUCTION_REVIEW 8/07 finding quoted in REGISTRY row 14 |
| **D-4** | 8 `*_CARD.md` files | **HIGH** | 8 upgrade cards carry **zero** status token and read as live work queues 36–50d after their findings were routed | LIQUID_CARD:5 and VIOLET_CARD:5 both end *"Nothing applied — this is the queue."* |
| **D-5** | `builds/wal_promotion/PROMOTION_REVIEW.md:3` | **HIGH** | Status line says *"Execution remains gated on WP-W0"* for a promotion that completed **2026-07-25** | root CLAUDE.md; doc unchanged since 7/22 |
| **D-6** | SAM/BRENT 8/17 review docs | **MED** | Largest Mode-A fan-out satisfies PAT-100 in substance but ships under 6 ad-hoc names instead of the mandated `*_READER_REPORTS.md` | `UPGRADE_PROTOCOL.md:29` mandates the filename |
| **D-7** | `design/2026-07-31_STE_WRITING_STANDARD_ASSESSMENT.md:3` | **MED** | Says "nothing proposed here is built or wired" while both recommendations are root canon | root CLAUDE.md § Output Canon cites both |
| **D-8** | `profiles/{SAM,BRENT}.md` | **MED** | 8/17 Δ-banners at line 37 / line 81, below an unmodified header advertising the superseded vintage | SAM.md:2 vs :37; all nine 7/22-cohort profiles put the Δ at line 3 |
| **D-9** | `profiles/BROCK.md` | **MED** | Banner's own dated re-check fired 20d ago, unserviced; 77 subject commits since | BROCK.md:5 |
| **D-10** | `profiles/ORACLE.md` | **MED** | 45d clock expired 8/13 — flagged by DAEDALUS's own registry row and not serviced | REGISTRY row 14; ORACLE.md 6/29; 70 commits |
| **D-11** | `upgrades/`, `builds/*/` | **MED** | No `archive/` exists; ~20 docs cross 60d ~9/05–9/11 with no queue row | `find -type d`; MARCO/SAM cards already 0 external refs |
| **D-12** | `upgrades/WAR_TRIAD_REVIEW_2026-08-15_READER_REPORTS.md` | **LOW** | Companion persisted with **no synthesis doc beside it** — the mandate's pair inverted | `ls upgrades/ \| grep WAR_TRIAD` = 1 file |
| **D-13** | `builds/{hawk_split,homer_promotion}/` | **LOW** | 10 one-shot 7/12 execution records unbannered — same class as the 4 fixed 8/11; the pass was scoped to `upgrades/` only | all 10 headers read; `ff75245b0` touched no `builds/` file |
| **D-14** | `profiles/`, `upgrades/` | **LOW** | No reader-facing index; 6 competing filename conventions; 4 docs whose filename date trails real vintage by ~1 month | `ls \| grep -iE "index\|readme"` = empty |

### TOP-5 ROUTE LIST
1. **D-1 — give the unbannered-docs finding a carrier.** One STATUS debt row + finish the 8/11 pass (~25 one-line banners, all self-owned, no approval gate). **Pairs with D-4, D-5, D-7, D-13 — same one-line fix, ~40 lines total.**
2. **D-2 + D-3 — re-head the profile-refresh queue by measured work-volume.** WALTER first (24d past its own 20d rule, 391 commits), then VIOLET/CARL/NEXUS. The registry row already contains the correct rule and does not apply it. **AEOLUS still needs servicing before Falsification Sweep #2 ~8/24.**
3. **D-5 + D-7 — two false status lines on completed work.** Both `finding_record_of_an_action_is_not_the_action` inverted, both load-bearing for a fresh reader.
4. **D-6 — decide whether PAT-100's contract is the *filename* or the *substance*, and write it down.** Most likely of all findings to become a false-clean check.
5. **D-11 — stand up `AGENTS/DAEDALUS/archive/` and a retirement queue row before ~9/05.** Zero candidates today, ~20 in three weeks, no destination and no trigger.

### NOT-READ
- **Full bodies not read (headers only + targeted greps):** 55 of 71 `upgrades/` docs; 21 of 35 profiles; 10 `builds/` subdir files; 4 of 8 `design/` docs.
- **Fully read:** PROFILE_S3_AUDIT · UPGRADE_PROTOCOL §Step-0 · REGISTRY.tsv rows 2–14 · headers of 23 named profiles · all `design/` and `builds/` headers.
- **STATUS.md read only partially** — lines 1–39 and 55–75 plus targeted greps. **The "Open / structural debt" section was read only through its first ~3 items**; later debt items may carry D-1 or D-11 in a form not seen. D-1's absence verified by grep (`unbanner` → 0 hits); **could not exhaustively confirm D-11's absence.**
- **Not examined (out of slice):** BLUEPRINTS/, PATTERNS.tsv (grepped), FLEET_MAP.tsv, CHECKS.tsv, SURFACES.tsv, EVOLUTION.md (grepped), inbox/, outbox/, scripts/, workbook/, reference/, sweeps/runs/, upgrades/PROME_AUDIT_2026-07-28_readers/.
- **Not verified:** whether the ~16 aged audit records' routed findings were closed at recipient agents; whether any agent has actually acted on a stale queue card.
- **Note on delivery:** brief was READ-ONLY, so this report was not written to a file by the reader — persisted here by the synthesizer.

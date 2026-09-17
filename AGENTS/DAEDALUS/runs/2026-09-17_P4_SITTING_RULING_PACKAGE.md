# P4 SITTING — correction-class validation C1–C5 + the correction-closure contract: ONE RULING PACKAGE for Will

**Owner:** DAEDALUS (presents) · **Date:** 2026-09-17 (Thu) ~08:4x–09:xx ET · **Venue:** DOCKET L282 (WQ-109 ruled 2026-09-01: *"P4 … one sitting, DAEDALUS presents"*) · **Spawn:** PROME `prome-ae`, WQ-184 L0 due-row spawn · **Will:** not in-session — this file IS the sitting's written form; PROME registers the ⚖️ rows from §0.
**Inputs (all read at the artifact this session):** `PROME/proposals/2026-09-05_correction-closure-verification-RECORD.md` (PROME verification P1–P8, amendments A1–A13, the §5 walk spec, the §5.1/5.2 walk RESULTS) · `PROME/codex/findings/2026-09-05_correction-closure-architecture-report.md` (§3 contract, §3.6 invariant, §4 tool amendment + 12 fixtures, §6 pilot, §8 items 1–7) · `AGENTS/DAEDALUS/design/2026-08-28_CORRECTION_CLASS_VALIDATION_PROPOSAL.md` (C1–C5) · `PROME/proposals/2026-09-06_wq185-RULED.md` §5 (behavioural cases (b)/(c)) · `AGENTS/WALTER/registry/CORRECTIONS.tsv` + every named target's `registry/corrections_receipts.tsv` (state as of 08:3x ET today) · `scripts/corrections_boot_check.py` (`cmd_check`, L121–170).
**Confidence tokens** per `PROME/CLAUDE.md` § Session Process Controls: VERIFIED · INFERRED · SEARCH-NOT-FOUND · UNKNOWN.

---

## 0. THE DECISIONS — one line each, with my rec (the ⚖️ rows)

| # | Decision | My rec | Owner of the word |
|---|---|---|---|
| **D1** | C1–C5 as forward-only conventions at the five named homes (all five homes are DAEDALUS blueprints) | **APPROVE all five** — one encode commit; LIQUID/RED/HENRY/BOND/ORACLE named first-application desks | Will |
| **D2** | Codex §8 items 1·2·3·4·5·7 with PROME's A1–A13 applied, and the explicit Class-11 mapping in §4.2 | **RATIFY as amended** | Will |
| **D3** | Evidence-syntax cutoff — 38 of 43 existing receipts carry NO structured note; forward-only from the word, pre-word receipts terminal-by-action for `RECEIPTED`, never for `CLOSED-VERIFIED` | **(a) forward-only** | Will |
| **D4** | First prune + `DEAD-AT-CAP` semantics (A3): a passed cap NEVER clears a NAMED target's block; the row goes `DEAD-AT-CAP`, the target's obligation survives until receipted | **(a) A3, with the SAM fixture** — checker change is mine, after the word, with an independent reader | Will (semantics) · WALTER (prune) · DAEDALUS (checker) |
| **D5** | Kill-string field ④ as a BOARD-spec line on every CORRECTION-class SIG-W (labelled field on 3 of 18 registered pointers today; WALTER authored 11 of 18) | **(a) one template line, forward-only** | WALTER (own spec) · Will if WALTER wants the word |
| **D6** | Intake A4 — VERIFIED closed by practice: register 6 → 18 rows 9/5 → 9/15; all three bypassed pilot cases registered retroactively (rows, no retro receipts) | **RATIFY, no new rule** — one pointer line in WALTER's spec to `CORRECTION_FORM.md` | WALTER |
| **D7** | Build the `--closure <id>` mode for the legs the walk shows are mechanizable (1·3·6 + shells for 2·4·5; ceiling `RECEIPTED-WITH-POINTER`; rc 0/1/2; Codex's 12 fixtures + A3 + WQ-185 (b)/(c)) | **APPROVE, sequenced AFTER D3+D4** (the fixtures depend on both) | Will |
| **D8** | WQ-185 (b) FILING ≠ APPLICATION and (c) CORRECTED PREMISE INVALIDATES DEPENDENTS as deterministic checks with passing controls (§6) | **ADOPT as legs 4b and 2/5's instrument** — (c) IS `consumer_check.py`, reuse not build | Will (rode WQ-185) |
| **D9** | Pilot verdict (Codex §6 success test, A11 metric): 2 of 3 pilot corrections reach an evidence-backed terminal state; the third (ES-02) is one `scope=` token short | **PASS-on-shape; close the pilot, no standing obligation** | Will |

**Decline is a legitimate outcome for any row** (record §4). No gate on retractions; no new ledger/dashboard/agent/forum/cadence (Codex §7 stands).

---

## 1. PRE-READ STATUS — the walk WAS delivered 9/5; the brief's "no record" is a location miss, and the location was PROME's own instruction

| Claim | Artifact | Verification | Result | Token |
|---|---|---|---|---|
| The four-case walk was delivered before the 9/15 due date | `git show --stat 08fa7a7b9` | commit 2026-09-05 *"DAEDALUS -> PROME: correction-closure walk delivered - 5 cases, 6-leg build split in 5.1/5.2"* | 1 file changed: **`PROME/proposals/2026-09-05_correction-closure-verification-RECORD.md`** §5.1 (five cases × fields (a)–(h)) + §5.2 (the deciding paragraph) | VERIFIED |
| It lives in PROME's file, not mine | record §5, sentence 2 | read | *"Record per case, one row, in a table appended to THIS file (§5.1)"* — PROME's spec placed it there; my STATUS/archive block AD recorded *"delivered, PROME-consumed"* | VERIFIED |
| Nothing in `AGENTS/DAEDALUS/` carries the walk | `grep -rl COR-20260828-01 AGENTS/DAEDALUS` | 5 hits, none a walk record | my #1 rule (*file in your dir*) was not met by a DAEDALUS artifact — a coordinator counting my dir found nothing | VERIFIED |

⇒ The lesson is `[[finding_ask_which_surface_the_reader_travels_not_where_the_fact_belongs]]`, not a missing deliverable. **This file is the DAEDALUS-side artifact; §2 refreshes the walk to today's register rather than re-quoting 9/5.**

---

## 2. THE WALK, REFRESHED TO 2026-09-17 — what changed in 12 days is the sitting's best evidence

| Case | 9/5 state (record §5.1) | **TODAY** (VERIFIED at register + receipts) | Δ that bears on a ruling |
|---|---|---|---|
| **1 CVNA L131** | CLOSED <1d; **no register row** | `COR-20260905-01` (PROME → CARL, cap 9/12 **passed**); CARL `APPLIED` + `artifact=` pointer; status still `LIVE` | intake fixed retroactively (A4 applied); **closable on legs 1/3/4 by script; leg 6 blank** (no `validation_ref=NONE` written) |
| **2 ES-02 lag rule** | CLOSED <1d; **no register row** | `COR-20260905-02` (CARL → PROME, cap 9/19); PROME `NO-OP` with a prose note, **no `scope=`** ; `LIVE` | the one case with a REAL successor test (cliff rule) still carries no `validation_ref`; the NO-OP is nonterminal under Codex §3.4 as written → **D3 decides whether that receipt counts** |
| **3 HANS Qatar** | OPEN — 4 live stale copies on dark HAWK, **no row** | `COR-20260908-04` (HANS → HAWK, cap 9/19); HAWK `APPLIED` 9/8 `artifact=AGENTS/HAWK/workbook/KB.tsv#KB-HAWK-306` (KB-299 SUPERSEDED); `grep -in end-september` on HAWK STATUS/SCRATCH/NEXUS_BRIEF = **0 hits**; the sole remaining hit is KB-299 itself, marked superseded by KB-306 | the walk's most dangerous case reached the terminal shape **through the register** — and leg 2/5's discriminator (live-stale vs preserved-history) is exactly what KB-299 now tests |
| **4 HAWK ↔ COR-20260828-01** | register OPEN on an unwritten receipt; no-op in board_log 9/2 | HAWK `NO-OP` 9/8 with `scope=AGENTS/HAWK/**; artifact=board_log.tsv#2026-09-02T20:20…` — **a receipt pointing at EXISTING evidence (A6, realised)**; 7/7 targets receipted; cap 9/11 **passed**; status `LIVE` | **5 of the 7 `APPLIED` receipts have EMPTY notes** → OPEN on leg 4 under §3.4; the row is `RECEIPTED`-eligible, not `CLOSED-VERIFIED`-eligible |
| **5 HOMER ↔ COR-20260828-04** | register OPEN on an unwritten receipt; substance 8/31 | HOMER `APPLIED` 9/11 with TWO `artifact=` pointers (`PIPELINE.tsv#…`, `board_log.tsv#2026-08-31…`); 4/4 receipted; cap **9/18 = tomorrow**; `LIVE` | CARL's `APPLIED` note is empty → same leg-4 state as case 4 |

**Pattern, refreshed:** the 9/5 pattern was *bookkeeping gaps + one invisible case*. Today **every walked case is in the register and every named target has receipted** — the intake half is fixed. What remains open is ONE thing, uniformly: **receipts written before any evidence-syntax rule carry no evidence** (5/7 on case 4, 1/4 on case 5, 1/1 on case 2). That is a RULING question (D3), not a desk defect — nobody was told to write `artifact=`.

**Leg-by-leg, today, for the five cases — could a SCRIPT close it?** (the §5.2 paragraph, re-run)

| §3.6 leg | Script? | Cases passing TODAY | Blocker |
|---|---|---|---|
| 1 owner retirement block exists | YES (pointer resolves) | 5/5 pointers resolve (2 are TSV/DOCKET rows, not `.md` — the form permits) | none |
| 2 owner live-copy scan clean | SHELL | grep runs on 5/5; **classification** needs a human (case 3: KB-299 is a preserved superseded row, not a live copy) | human at the artifact |
| 3 every named target's latest receipt terminal | YES (enum) | 5/5 by ACTION (all `APPLIED`/`NO-OP`) | — |
| 4 every APPLIED receipt has an artifact pointer | SHELL | **2/5** (cases 1, 3); cases 4, 5 fail on pre-word empty notes; case 2 is a NO-OP without `scope=` | **D3** |
| 5 final scoped stale-copy scan | SHELL | same as leg 2 | human |
| 6 `validation_ref` resolves or = NONE | YES (field) | **0/5** — no owner block carries the field yet (the field does not exist until D2 item 4 is ratified) | **D2** |

⇒ **After D2 + D3, cases 1 and 3 reach `RECEIPTED-WITH-POINTER` by script in one owner edit each (`validation_ref=NONE`), and NO case reaches `CLOSED-VERIFIED` by script — which is A1, confirmed on real rows.**

---

## 3. THE FLEET DATUM TODAY (VERIFIED, `CORRECTIONS.tsv` + 20 receipts files, 08:3x ET)

| Measure | Value |
|---|---|
| Register rows | **18** (6 on 9/5) — status column **18 × `LIVE`, 0 `RECEIPTED`, 0 `RETIRED`, 0 `DEAD-AT-CAP`** |
| Rows whose `date_cap` has passed | **7** (`-0826-01/-02`, `-0828-01/-02/-03`, `-0905-01`, `-0907-01`); `-0828-04` passes tomorrow |
| Prune ever run | **NO** — INFERRED from the all-`LIVE` column (P2's caveat stands: non-maintenance, not non-attempt) |
| Receipts on file (named targets) | **43** (19 on 9/5) |
| Receipts with a structured evidence key (`artifact=` / `scope=`) | **5** — HAWK ×2, HOMER, CARL (`-0905-01`), PROME (`-0910-01`); 3 more carry free prose; **35 empty** |
| Named targets with NO receipts file at all | **HENRY** (named on **6** rows) · ZHAO · WAL |
| Desks the checker BLOCKS (rc 1) at boot today | **HENRY (6 rows) · ZHAO · WAL · HANS · WATT** — every one has a self-commit dated 9/15 or 9/16; HENRY's charter step 3e runs the check (`AGENTS/HENRY/CLAUDE.md:43`) and its last self-commit is **2026-09-16** |
| What a prune under D3/D4 would produce TODAY | **10 `RECEIPTED`** (`-0826-01`, `-0828-01/-02/-03/-04`, `-0905-01/-02`, `-0907-01`, `-0908-04`, `-0915-08`) · **1 `DEAD-AT-CAP`** (`-0826-02`, SAM never receipted, cap 8/28) · **7 stay `LIVE`** on missing named receipts (HENRY on 5 of them) · **0 `RETIRED`** |
| Kill-string field ④, labelled, on the pointed artifact | present on **3 of 18** (`-0828-04` DEWEY · `-0907-01` DAEDALUS · `-0910-02`'s SIG-009 — the last UNKNOWN whether the hits are the label); 2 rows point at non-`.md` artifacts (grep N/A); WALTER-authored rows **11 of 18**, label on ≤1 |

> **ATTENTION 🟠 — the boot check is FIRING and being overridden.** `corrections_boot_check.py HENRY` returns **rc 1, 6 named rows**, and HENRY committed on 9/16. Four more desks are in the same state. The instrument works; the control downstream of it does not exist (`[[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]]`). Not a ruling item — WALTER's prune is the receiver-side check that makes it visible (D4); flagged to PROME for the desks' next briefs.

---

## 4. THE DECISION ROWS — decision · options · what each option changes · my rec

### D1 — C1–C5 (the 8/28 proposal, unchanged; text at `design/2026-08-28_CORRECTION_CLASS_VALIDATION_PROPOSAL.md`)

| Option | What changes |
|---|---|
| **(a) approve all five, forward-only, at the named homes — REC** | DAEDALUS encodes in ONE commit: C1 *Passenger rule* + C3 *adjacent-cell rule* → `BLUEPRINTS/CORRECTION_FORM.md`; C2 (one-alternative pass for correction-born findings) + C4 (grep the OLD regime by name before commit) → `BLUEPRINTS/market-agent.md` §4 / closeout block; C5 (SPECIFIED-BUT-NONEXISTENT = zeroth instrument state) → `CHECK_STANDARD.md` §12. First-application packets to LIQUID · RED · HENRY · BOND · ORACLE. **Zero new tooling; every item is a convention on an existing surface.** VERIFIED none is encoded yet: `git log --since=2026-08-27 -- BLUEPRINTS/CORRECTION_FORM.md` = empty; `grep -c Passenger CORRECTION_FORM.md` = 0. |
| (b) approve C1 · C3 · C4 only (the three with a realised catch: LIQUID KB-LIQ-106 ×2, RED KB-RED-067, HENRY 7-of-21) | C2 and C5 wait; C5's ORACLE instance (272-line spec, no code, 67 days) stays a memory rather than a closeout question |
| (c) decline | incidents stay recorded at their owners; the hole (*corrections inherit trust instead of re-earning it*) stays open |

**Why C1 matters to THIS package:** Codex §3.2 step 4 (*separate any newly inferred replacement claim under C1*) is a dependency of the closure contract. Ratifying D2 without D1 leaves §3.2 pointing at an un-encoded rule.

### D2 — Codex §8 items 1·2·3·4·5·7 with A1–A13, and the Class-11 mapping made explicit

| Item | Ruling text (as I would encode it) | Home |
|---|---|---|
| 1 Receipt ≠ closure | register `status` ladder: `LIVE` → `RECEIPTED` (every named target has a receipt of ANY action) → `RETIRED` (the §3.6 invariant holds = Class 11 `CLOSED-VERIFIED`); `DEAD-AT-CAP` (cap passed, reconciliation incomplete). **`RECEIPTED` maps to Class 11 `CONSUMED`; `RETIRED` maps to `CLOSED-VERIFIED`; nothing below `RETIRED` is closure.** | `STATE_VOCABULARY.md` Class 11 (mine) + register header (WALTER) |
| 2 Terminal actions | `APPLIED` + `NO-OP` terminal; `DEFERRED` / `CONTESTED` / missing nonterminal — with **D3** governing whether a pre-word empty note disqualifies | `CORRECTION_FORM.md` §Read-side (mine) |
| 3 Immutable generation | a correction-to-a-correction is a NEW `COR-` ID with `supersedes=` in the OWNER retirement block (A9); register summary carries the pointer, no new column | `CORRECTION_FORM.md` (mine); register (WALTER, no schema change) |
| 4 Conditional successor | retirement block gains `validation_ref=<owner path#stable-key> \| NONE` (A7: stable keys, never line numbers); `NONE` is honest when no grading-capable test exists | `CORRECTION_FORM.md` (mine) |
| 5 Target-scoped closure | `ALL` = dissemination; a closure claim on an `ALL` row states its verified target scope | register header (WALTER) |
| 7 No additional surface | owner record → WALTER pointer index → recipient-owned receipts is the complete topology | (nothing to write) |

**Options:** ratify as amended (REC) · ratify minus item 4 (`validation_ref`) — loses the one field that turns case 2's real successor test into something the checker can see · decline. **What changes on ratification:** three DAEDALUS blueprint edits in one commit (Class 11 mapping · form fields `supersedes=`/`validation_ref=` · read-side terminal-action table) + WALTER's register header prune sentence (D4). A10 (history may move cold, never dropped) and A12 (this verifies work AFTER it happens; the spawn-driver is separate) travel with the package as caveats, not rules.

### D3 — Evidence-syntax cutoff (NEW row — the walk refresh forced it)

**The fact:** 35 of 43 receipts have an empty `note`; 5 carry `artifact=`/`scope=`. Codex §3.4 makes an `APPLIED` without `artifact=` and a `NO-OP` without `scope=` nonterminal. Applied retroactively, **every walked case but 1 and 3 re-opens on receipts nobody was told to write differently.**

| Option | What changes |
|---|---|
| **(a) forward-only from the word — REC.** Receipts dated after the word carry the structured keys (Codex §4 property 3, verbatim); receipts dated before count as terminal-by-action for the `RECEIPTED` rung, and a row holding any such receipt can reach `RETIRED` only if the target RE-RECEIPTS with evidence (voluntary, never swept) | today's 10 `RECEIPTED`-eligible rows become `RECEIPTED` at the first prune; `RETIRED` is reachable for `-0905-01` and `-0908-04` after one owner edit each; nothing re-opens |
| (b) retroactive migration | Codex §7 non-goal (*no fleet-wide receipt migration*); 35 receipts re-written by hand from memory — the worst evidence class |
| (c) empty notes terminal forever | `CLOSED-VERIFIED` becomes reachable with zero evidence — exactly the false assurance Codex point 1 named |

### D4 — First prune + `DEAD-AT-CAP` semantics (A3) — WALTER-lane + the checker

**The live instance:** `COR-20260826-02` (LIQUID → SAM, cap 2026-08-28). SAM never receipted. The checker today prints `INFO 1 dead-at-cap with no receipt from this desk` and returns **rc 0** (`cmd_check` L147–149: a passed cap `continue`s past the named block). **SAM has passed its boot check on this row for 20 days.**

| Option | What changes |
|---|---|
| **(a) A3 — REC.** A passed cap changes the ROW's status (`DEAD-AT-CAP`, WALTER's prune, feeds the R1 indictment leg) and **never the named TARGET's obligation**: the checker keeps returning rc 1 for a named target with no receipt, labelled `DEAD-AT-CAP`, until a receipt of any action exists. `date_cap` governs `ALL`-rows (broadcast expiry) and row status only | checker edit (mine, `scripts/` grant): the `DEAD-AT-CAP` `continue` at L139 and the cap-passed `continue` at L149 both become *skip only if this desk receipted*; fixture = SAM/`-0826-02` (BLOCK) beside HAWK/`-0828-01` (PASS, receipted after cap); selftest gains both. **Consequential repair (gate) ⇒ independent reader with its own counterexample before it is called fixed (WQ-229).** SAM's next boot BLOCKs once, then receipts |
| (b) keep silent expiry | a named obligation can be discharged by waiting; the register's `DEAD-AT-CAP` count under-reports by every target that out-waited its cap |

**First prune (WALTER, after the word):** expected output = §3's last-but-one row (**10 · 1 · 7 · 0**). That table is the prune's passing control — a different result is either a receipt written since 08:3x today or a defect, and the diff says which.

### D5 — Kill-string field ④ on CORRECTION-class SIG-W (WALTER-lane)

Labelled field on 3 of 18 pointed artifacts (§3). **(a) REC:** one line in WALTER's BOARD template — a CORRECTION-class signal carries `KILL-STRINGS:` (field ④, the literals a consumer greps for), forward-only; the -022/-023 lesson applies — **the template is the one fix point**, not 11 signals. **What changes:** leg 2/5's grep list comes from the field, not from a reader's guess; the closure mode can run it. ⚠️ P7's caveat stands: the census keys on the LABEL — `SIG-W-20260828-006` carries a usable dead literal (*"$86.36 ❌ WRONG"*) unlabelled, so literal-absence on the other 15 is UNKNOWN. **(b)** leave optional ⇒ the closure mode has no machine-readable input for its grep on 15 of 18 rows.

### D6 — Intake (A4) — RATIFY BY EVIDENCE, no new rule

VERIFIED: the register went 6 → 18 rows between 9/5 and 9/15; `-0905-01` (PROME), `-0905-02` (CARL), `-0908-04` (HANS) are the three bypassed pilot cases, registered as rows with no retroactive receipts (Codex non-goal held). **What changes under REC:** one pointer line in WALTER's spec (*a correction that never crossed BOARD still gets its row from the corrector — the retirement block EMITS it*, citing `CORRECTION_FORM.md`). Nothing else.

### D7 — Build authorization: `corrections_boot_check.py --closure <COR-id>`

**Scope the walk justifies (unchanged from §5.2, confirmed by §2):** legs 1 · 3 · 6 mechanical; legs 2 · 4 · 5 as shells that EMIT (grep hit-list; unresolved/empty-pointer list) and never clear. **Output ceiling `RECEIPTED-WITH-POINTER`**; `0 CLOSED-VERIFIED` is unreachable by the script (A1) and the tool says so in its own PASS line. **rc contract** 0 / `1 OPEN` / `2 CANNOT-EVALUATE` per Codex §4; never edits a consumer file, never changes a status token (property 5). **Fixtures:** Codex §4's twelve + A3's (D4) + WQ-185 (b)/(c) (§6) + the pre-word/post-word receipt pair from D3. **Sequence:** D3 + D4 words → build (one session, mine) → independent reader (coldreader/RAV) with its own counterexample → WALTER's first prune consumes its output. **Options:** (a) as above — REC · (b) no build, WALTER prunes by hand from §3's table (works once; the 19th row re-opens the problem) · (c) autonomous `CLOSED-VERIFIED` — decline, A1. **Not built this session, per the brief.**

### D8 — WQ-185 (b) and (c) as deterministic checks — see §6.

### D9 — Pilot verdict (Codex §6: *succeeds if all three reach an evidence-backed terminal state without a new ledger, dashboard or thread*)

| Pilot | Owner-fix | Last terminal consumer | Live stale copies (final scan) | Corr-of-corr ≤7d | validation_ref | Evidence-backed terminal TODAY? |
|---|---|---|---|---|---|---|
| CARL/CVNA `-0905-01` | 9/5 | CARL 9/5 `APPLIED`+ptr | 0 (VERIFIED 9/5; not re-run today) | yes (weekday find-replace, same day) | not written | **YES** (leg 6 one edit away) |
| STUE/ES-02 `-0905-02` | 9/5 | PROME `NO-OP`, prose note, no `scope=` | 0 | no | not written (a real test exists — KB-CARL-426) | **NO — one token short** (D3 (a) makes it YES) |
| HANS/Qatar `-0908-04` | 9/5 (HANS) · 9/8 (HAWK) | HAWK 9/8 `APPLIED`+ptr | 0 live; KB-299 preserved-superseded | no | not written | **YES** |

**Verdict: PASS on shape, 2 of 3** — no new ledger, no dashboard, no thread; the third fails on syntax the fleet did not yet have. Discovery→closure (A11): CVNA <1d · ES-02 <1d · HANS 3d (9/5 → 9/8, dark-consumer bound). No standing obligation; this table is the pilot's record.

---

## 5. WHAT THE WALK SAYS THE CLOSURE MODE MAY AND MAY NOT ESTABLISH — the build contract in one table (for D7)

| Leg | Mode emits | Clears? | Fixture that must FAIL | Fixture that must PASS |
|---|---|---|---|---|
| 1 | pointer resolves / does not | YES | `-0905-01` with its DOCKET pointer edited to a dead line | `-0908-04` (KB row) |
| 2 | grep hit-list for each kill-string, per owner surface | **NO** — list only | (none: emit-only) | `-0828-01`: every `$86.36` hit is a correction record — the list is non-empty AND the human clears it |
| 3 | latest receipt per (agent, id) by append order; enum | YES | `DEFERRED` without `review=` ⇒ 2 | `DEFERRED → APPLIED` duplicate ⇒ latest governs |
| 4 | receipts lacking `artifact=`/`scope=`, dated ≥ word | **NO** — list only (D3 pre-word receipts listed as `PRE-WORD`, not as defects) | post-word `APPLIED` with empty note ⇒ 1 OPEN | HOMER `-0828-04` (two pointers) |
| 4b | WQ-185 (b): pointed path has NO commit touching it between correction date and receipt date ⇒ `UNAPPLIED` | YES (deterministic) | a receipt row written with the artifact unchanged (reference: L115 · L239 · HOMER `COR-20260828` shape) | HOMER: `PIPELINE.tsv` changed 8/31, receipt 9/11 ⇒ APPLIED stands |
| 5 | = leg 2 at closing time | **NO** | — | — |
| 6 | `validation_ref` present & (resolves ∨ `NONE`) | YES | field absent ⇒ 1 OPEN | `NONE` |

**Top line the mode may print:** `RECEIPTED-WITH-POINTER` (all YES legs pass, all list legs non-empty-and-listed) · `1 OPEN` · `2 CANNOT-EVALUATE`. **Never `CLOSED-VERIFIED`.**

---

## 6. WQ-185 §5 — the two behavioural cases, made deterministic with a passing control (D8)

| Case | Deterministic form | Passing control | Research-judgement half (stays human) |
|---|---|---|---|
| **(b) FILING ≠ APPLICATION** — a receipt row written with the artifact unchanged reads `UNAPPLIED` | for an `APPLIED` receipt with `artifact=<path>#<key>`: `git log --format=%h --since=<correction date> --until=<receipt date> -- <path>` empty ⇒ `UNAPPLIED` (rc 1). Line numbers in the key ⇒ `2 CANNOT-EVALUATE` (A7) | HOMER `COR-20260828-04`: `AGENTS/HOMER/workbook/PIPELINE.tsv` has commits in [8/28, 9/11] ⇒ `APPLIED` stands | whether the CHANGE that landed is the corrected state (Codex point 1 — path existence ≠ disposition) |
| **(c) CORRECTED PREMISE INVALIDATES DEPENDENT CONCLUSIONS** | `python3 scripts/consumer_check.py --agent <corrector> --old <kill-string> [--new <replacement>]` — the fleet scan; 🔴 STALE hits = dependents still carrying the dead premise | CVNA: `--old "9/10 CVNA"` returns 0 🔴 (the six CARL surfaces unwound 9/5 — record §5.1 case 1 (e)) | HOLD / WEAKEN / FLIP on each dependent (the `direction` column) — a human's call per row, never the scanner's |

Both are `consumer_check.py`-class and separate from the judgement cases, as WQ-185 §5 asked. **Neither is a new tool.**

---

## 7. NOT DONE, DECLARED RESIDUE, AND TOKENS

- **Not built:** the `--closure` mode (brief: *do not build a checker in this session*; D7 sequences it after D3/D4 anyway). **Not encoded:** C1–C5, Class 11 mapping, form fields — all wait for the word (D1/D2); homes are all mine, one commit each.
- **Not re-run today:** the (e) live-copy greps for cases 1, 2, 4, 5 (9/5 values carried; case 3 re-run because it was the open one). INFERRED unchanged.
- ⚠️ **HENRY's six unreceipted rows** are reported from the checker's output, not from HENRY's reading of them — HENRY may have dispositioned some in prose (the HAWK 9/2 shape). The receipts are what the register can see.
- ⚠️ `-0910-02`'s kill-string count (2 hits in SIG-009) is a substring count, UNKNOWN whether it is the labelled field.
- ⚠️ The 9/5 walk record's own residue (Codex's 22-obligation count vs PROME's hand count, both non-instrument) is now answered by the §3 script: **43 receipts against 61 named-target obligations** across 18 rows (hand-verifiable from the register's `targets` column; the script is the 30-line block that produced §3, run this session, not committed as a tool).
- **Cadence note for PROME (not this sitting):** `sweeps_due.py` at boot shows PR#6 (9/15) and GATE_BASIS run #1 (9/16) **did not run** — no DAEDALUS session existed 9/15–9/16 — plus Wiring-sweep R1 (9/12), H2 as-made (9/14), profile-refresh queue (9/15) past their `Resolve_By`, and L239 render / Falsification sweep / doc-retirement DUE. Slate them; none was in this spawn's scope.

# WQ-184 — the SPAWN DRIVER: who runs a registered dated row when its owner is dark · RULED 2026-09-05 21:42 ET

**Will, verbatim:** *"approve WQ-184 with your recs"* (session `prome-86`, LAPTOP, 21:42 ET) — on the seven legs of §6 as recommended: ①②③④⑦ APPROVED · ⑤ DEFERRED to the 9/19 sitting (DOCKET L291) · ⑥ COMMISSIONED (DOCKET L292). Registered 21:4x, ruled 21:42, executed the same sitting (§7 status at the foot). Written as a PROPOSAL 21:3x; the plan cold read (Opus coldreader) returned while the word was arriving — 22/38 ✅ · 11 ⚠️ · 5 ❌; the ❌ fixed below at the source, the ⚠️ declared in § Residue.

**Status:** RULED — canon text (§8) inserted after the plan read, ONE edit per file, result read on `PROME/CLAUDE.md` (PROME/CLAUDE.md § Session Process Controls). **Owner:** PROME. **Queue row:** `PROME/WILL_QUEUE.md` WQ-184. **Needed by:** 2026-09-08 (Tue) — the first market-day boot after this weekend is the first boot the rule would change. **Directed:** Will, 2026-09-05 21:2x ET, *"Go ahead with the spawn-driver design"*, on PROME's boot-time owed-items question.
**Named by three independent sources this week:** Codex (verification record A12 + declared residue: *"why Tier-1 spawn authority was not exercised for MIDAS/FERT is UNKNOWN and belongs to the spawn-driver item"*), DAEDALUS (FERT profile F-2: *"the trigger firing with no session is the failure mode that matters — a spawn-driver question (PROME/Will), not a FERT defect"*; CRUISE profile; `BLUEPRINTS/meta-agent.md` PAT-051), and PROME's own ORCH_LOG (§1). Prior home of the same shape: BD-02 (LABOR ask 2026-08-20, built as an advisory that says "flag Will to spawn").

---

## 0. In one paragraph

Dated work is registered in three places (DOCKET rows, GATES `review_by`, desk catalyst ledgers) and DETECTED in three places (each desk's `boot.py`, `prome_gate.py`'s DOCKET checks, `docket_view.py`) — but nothing turns "this row has arrived and its owner is dark" into a session. PROME already holds the authority to do so (Tier 1: *follow-up spawns inside an already-approved workstream — including a full domain-desk session*; 8/22 triage ①), and has used it inconsistently: HOMER 8/31 and REGINALD 9/1 were spawned on due rows with no nod; MIDAS · TERRY · FERT sat on due rows through three PROME sessions on 9/5 until Will typed *"go ahead and spawn all three"*. The design closes three gaps, in order of cost: **(L0) the RULE** — a registered dated row IS the approved workstream, so its arrival with a dark owner is the Tier-1 trigger, no nod; **(L1) the INSTRUMENT** — `PROME/tools/spawn_list.py` (LIVE, read-only; committed in this sitting's commit set with the gate wiring — it was untracked at the plan read, the reader's ❌6) names the candidates at boot and, at closeout, the rows that land before the next boot; **(L2) the PRESENCE layer** — a machine-independent daily digest from the RESEARCH-INTAKE Actions lane to Will's Telegram, so a weekend or a dead box no longer means silence. Cloud routines and a headless local runner are analysed and NOT proposed for v1. $0 moves under any layer; report-before-execute and every Tier-3 gate are untouched.

---

## 1. The problem, measured

| # | Instance | What fired | Who ran it, and when | Lag / cost | Confidence |
|---|---|---|---|---|---|
| 1 | MIDAS L280 (MIDAS-08 grade, due 9/4) | COT vintage published 9/4 15:30 | Will's word 9/5 19:41 → PROME Tier-1 spawn | 1d overdue; carried as "open for Will" through the 9/5 midday, EVE and NIGHT HANDOFF entries | VERIFIED (HANDOFF 9/5 ×3; ORCH_LOG 9/5 MIDAS row) |
| 2 | TERRY L115 (VIXCS exit grade) | Owner graded it **2026-08-07** on its own card | Coordinator row read PENDING for **29 days**; PROME spawned 9/5 19:41 to "grade" — the spawn found a finished grade | The RECEIPT-GAP form: no session was needed, a consumer read was | VERIFIED (tombstone L115, receipt `2026-09-05_from-TERRY_…`) |
| 3 | FERT L283 (Pink Sheet T11) — **two clocks:** the DOCKET row is dated **9/8**; FERT's own ledger `Next_Check` was **9/4**, which is the clock DAEDALUS F-2 graded (*"DUE 2026-09-04 — overdue by one day"*) | Edition published (in-doc 9/2) | Will's word 9/5 19:41 | 1d overdue on the DESK clock, 3d early on the DOCKET clock — the row would have been a LANDS-IN row at the weekend closeout, not a boot spawn | VERIFIED (DAEDALUS `profiles/FERT.md` F-2; DOCKET L283 date cell at `5cd529346` and at its tombstone) |
| 4 | HANS L279 (ECB 9/10) | DAEDALUS packet 9/5 asked PROME to *decide a spawn by 9/9* | HANS ran by Will's hand 9/5 midday | A decision was asked of PROME that Tier 1 already answered | VERIFIED (`PROME/inbox/processed/2026-09-05_from-DAEDALUS_HANS-dark-…`) |
| 5 | HOMER 8/31 · REGINALD 9/1 | FMHPI July print / GATE-REG-T02 FIRED | **PROME Tier-1 spawns, no nod** ("dated-decider touch (Tier 1, registered cat…)") | 0 — the counter-examples that prove the authority exists and works | VERIFIED (ORCH_LOG rows 2026-08-31 HOMER, 2026-09-01 REGINALD) |
| 6 | DOCKET OVERDUE count at PROME boots (**definition: `scripts/docket_view.py`'s header count — every PENDING row dated before today with no terminal disposition, COVERED-annotated rows included**; distinct from spawn_list's due-list, which EXCLUDES COVERED rows because a named holder exists — tonight 3 OVERDUE = L17 WILL + L264/L265 BRENT COVERED for the 9/11 consumer read, and the due-list shows 1) | — | 39 (9/3 NIGHT) → 32 (9/4) → 5 (9/5 midday, after the ㉙ reconcile) → 4 (9/5 NIGHT closeout) → 3 (this sitting, after L239's tombstone at `6f15e8f03`) | 32 rows had to be reconciled in one sitting; the reconcile itself minted the CVNA fabrication (error class #91) | INFERRED (HANDOFF/SCRATCH stamps + tonight's `docket_view` header; the per-boot series is not an instrument yet — §5 M1 makes it one) |
| 7 | ORCH_LOG 2026-08-23 → 09-05, 92 TOUCH rows | — | trigger cell keyed on a **Will word: 41** · on a **DOCKET/GATES referent: 24** · other (inbox/landed-unread/re-ping): 27 | Most spawns waited for a word; a quarter ran on a referent | INFERRED (single regex pass, method §A — a reader's classification, not a registered instrument) |
| 8 | BD-02 (LABOR ask 2026-08-20) | "a frozen card only grades if a session runs, and nothing summons a session on a catalyst date; an external DAEDALUS sweep beat the desk's own boot by 3d" | Built 8/20 as `check_desk_catalyst_summons()` — ADVISORY, registry = LABOR only, disposition text *"flag Will to spawn the desk"* | The same shape, solved one desk wide and one word short | VERIFIED (`PROME/tools/prome_gate.py` SUMMONS_LEDGERS) |
| 9 | Desk cadence | — | "LOW AND LUMPY: HENRY ran on 3 days all month (8/06 · 8/10 · 8/20), BROCK on 3" — WALTER: *"binding constraint is NOT intake; it is owner availability at the moment a signal lands"* | The presence gap is structural, not a bad week | VERIFIED (8/22 ruling record, measured basis paragraph) |

**Why the authority went unexercised on 9/5 (Codex's UNKNOWN, answered from the record):** (a) the 8/22 triage ① is worded around WALTER's *doorbell* (a signal landing), and nothing in canon says a **registered dated row** is an "approved workstream" — so a due row read as something to ASK about; (b) the 9/5 EVE recovery session inherited the crashed session's open ask (*"the spawn nod"*) verbatim instead of re-triaging it; (c) MIDAS-08 carried a conditional BOND correction, which read as "new direction" (Tier 2) when the row's registration on 8/2x had already approved exactly that conditional. Same class as `finding_scope_boundary_asserted_from_proximity` — reading a ledger of what PROME DID as the rule for what it MAY — now n=4.

---

## 2. Anatomy — three gaps, not one

| Gap | What is missing | Evidence | Fix layer |
|---|---|---|---|
| **G1 Authority (behavioral, PROME's)** | A sentence in the auto-injected file saying the registered row IS the nod | §1 rows 1–5, 7 | **L0** |
| **G2 Instrument** | A check that NAMES spawn candidates. Today: `check_docket_overdue` (asks for an annotation) · `check_docket_today` (asks "is it dispositioned?", closeout, BLOCKING) · BD-02 (one desk ledger) · `docket_view` (calendar, no owner liveness) | §1 rows 6, 8 | **L1** |
| **G3 Presence** | Any actor when no PROME session exists (weekend · overnight · box asleep · crash — two crashes this week, 9/4 and 9/5) | §1 row 9; 9/4–9/5 crash log | **L2** |

---

## 3. The design

### L0 — the RULE (canon; two edits, drafted verbatim in §8)
> **A registered dated row is the nod.** A PENDING row in `PROME/DOCKET.tsv` (or a LIVE `GATES.tsv` row at its `review_by`) that names a desk owner was approved at registration; when its date arrives and the owner has no live session, PROME spawns the owner **Tier 1, at the first PROME boot on or after the date, without asking** — report-before-execute, whole-inbox drain, ListAgents preflight, Opus. Will's word is required only for: Will-owned rows (→ WILL_QUEUE), rows whose consequent is a trade or spend (Tier 3, unchanged), a genuinely NEW direction not on any registered row (Tier 2, unchanged), and candidates beyond the per-boot cap (→ a slate, the 8/27 precedent).

### L1 — the INSTRUMENT (`PROME/tools/spawn_list.py`, LIVE; wired into `prome_gate.py` boot + closeout at the word)
- **Boot** (`--horizon 0`): every PENDING row due ≤ today, classed **DARK** (owner's last self-commit predates the row's start → spawn candidate) · **ACTIVE** (owner committed on/after the row's start → **consumer read at the owner's artifact FIRST** — the L115 lesson: the grade may exist and only the receipt is missing) · **PROME-OWNED** (do it) · **WILL-OWNED** (queue). Owner = first desk token of the owner cell. Liveness proxy = newest commit whose SUBJECT begins `<OWNER>:` / `<OWNER> ->` — never a path-scoped log (`[[finding_path_scoped_git_log_measures_inbound_traffic]]`). The second liveness leg, harness `ListAgents` in the same minute, is PROME's in-session step (a live desk is doorbelled, never spawned).
- **Closeout** (`--horizon` = days to the next likely boot: 1 on a weekday, 3 on Fri/Sat): rows that **LAND IN THE GAP**, with each owner's last-commit age — PROME either pre-spawns under L0 or posts the list to Will as a **slate** (the 8/27 *"Fri spawn slate (approved)"* precedent, run 8/28 as three waves).
- **ORCH_LOG:** a spawn made under L0 writes its `trigger` cell leading with **`DUE-ROW L<n>`** (or `DUE-GATE <id>`), so §5 M3 becomes a grep, not a regex guess. Token to be registered in `STATE_VOCABULARY.md` by DAEDALUS before first use (Class 2 companion-field family; PAT-069: a machine-read token is an interface).
- **BD-02 folds in:** `SUMMONS_LEDGERS` stays for desk-private catalyst ledgers not mirrored to DOCKET; its disposition text changes from *"flag Will to spawn"* to *"L0 applies"*.
- **In-session cadence (no ruling needed, Tier 1):** on a long open PROME day, `CronCreate` can re-run the boot horizon hourly (session-only, 7-day expiry) — it does not survive the session and is not the presence layer.
- **Live output tonight (VERIFIED, v1.1 run 21:5x ET after the word):** boot horizon → 1 row, WILL-OWNED (L17, 12d overdue, the forum-slate deferral); rc 0. Weekend horizon (+3d, through Tue 9/8) → 14 rows: PROME 1 (L251) · WILL 1 · **12 LAND-IN-GAP, every owner active within 0–4 days** — BRENT L123 OPEC+ Sun 9/6 (last commit 9/4) · NEXUS L39 / BROCK L189 / WALTER L208 Mon 9/7 · OSPREY L140 / HAWK L225+L234 / WATT L249 / TERRY L252 / WALTER L273 Tue 9/8 · **two GATES rows at their 9/8 `review_by`: GATE-FALCON-001 (FALCON, last commit 9/1) and GATE-TERRY-007 (TERRY, 9/5).** Under L0 tonight's closeout question is *"who runs BRENT's OPEC+ read Sunday?"* — and the answer is a slate to Will or a Sunday spawn, not silence.

### L2 — the PRESENCE layer (machine-independent detection + nudge; $0 compute)
- **What:** a second job in the RESEARCH-INTAKE GitHub Actions workflow (the lane Will chose 6/29 over a VPS *because Actions can't silently rot*), weekday **~06:1x ET** (Will is up ~6, USER.md) **and Sunday ~08:1x ET**: clone `Research-workspace` read-only, run `PROME/tools/spawn_list.py --horizon 1 --tsv`, post the DARK / LANDS rows (and the OVERDUE count) to Will's Telegram as one message: *"DUE with dark owner: L280 MIDAS · L283 FERT — open PROME; L0 runs them."* Nothing else: no session, no commit, no spawn.
- **Why this and not a cloud routine:** a routine (`/schedule`, Sonnet, isolated cloud checkout) can run the same script but has no channel to Will except the repo or a connector, cannot spawn local desks, and would make the cloud a **repo writer** the week YEYOU's push-review retired with no mechanical replacement. It is analysed, not proposed (leg ⑤: decide at the 9/19 review on M1).
- **Why not a headless local runner:** a systemd timer running `claude -p` on the box cannot ask Will, and a timer that fires on a box Will is not using breaks the **one-machine-at-a-time** rule that makes ff-gated auto-push sound. Not proposed.
- **Needs Will's hands (nothing PROME can do):** two secrets in the RESEARCH-INTAKE repo — a **read-only PAT** scoped to `Research-workspace` (both repos read as private: RESEARCH-INTAKE by design; `Research-workspace` UNKNOWN via `gh` — the authed token returns 404 on both, so the visibility could not be VERIFIED) and a **Telegram bot token + chat id**. PROME drafts the workflow step and the post script as a packet; committing to the intake repo is Will's hand or PROME on Will's explicit word (it is outside PROME's directory grant).

---

## 4. Guards — how this goes wrong, and the control on each

| Failure | Control | Where it lives today |
|---|---|---|
| A due-row spawn moves capital | Never: trade/spend rows are Tier 3; TERRY constructs, Will approves; report-before-execute on every spawn | `AUTONOMY.md` Tier 3 · root rule #5 (unchanged) |
| Context blow-up from many spawns | **Cap 4 due-row spawns per boot**; beyond → slate to Will; one spawn, one objective | `ORCHESTRATION_PLAYBOOK.md` § Fable-context economics · § Right-size |
| Spawning a live desk (9/4 HENRY double) | `ListAgents` in the same minute; live ⇒ `SendMessage` doorbell | `PROME/CLAUDE.md` desk-spawn preflight (WQ-178) |
| Spawning onto a finished grade (L115) | **ACTIVE ⇒ consumer read at the owner's artifact FIRST**; spawn only if ungraded | spawn_list class · `finding_record_of_an_action_is_not_the_action` n=15 |
| Spawning a Will-owned or PROME-owned row | WILL-OWNED → queue; PROME-OWNED → do it | spawn_list classes |
| A 30+-day-dark desk spawned cold | Revival-proxy brief, not a bare spawn | `ORCHESTRAL_LAYER_DESIGN.md` § Revival-proxy v3 · `finding_revival_boot_doc_sweep` |
| A WEEKLY desk's own-day row reads DARK (v1 cadence blindness) | ListAgents leg + the owner's STATUS "next boot" line; **structural fix = the Class 8 DESK cadence column** (Will-approved 8/21, *"instrument = fleet_triage.py, PROME applies the column"* — **UNBUILT as of tonight, VERIFIED**: no column in ROSTER, no `fleet_triage.py`) | leg ⑥ commissions it |
| A row keyed to a print spawned before the print | The row's date is the owner's declared resolve date; PROME judges "grade-able now?" from the owner's `Next_Check`, and a spawn that cannot grade is a wasted session, not a wrong one | owner ledgers |
| Spawn partial-drains (REGINALD P-002) | Whole-inbox drain mandate rides every due-row spawn | 8/23 scope widening (ruled) |
| Model spend | Domain desks on Opus; Fable is the orchestrator | § Model tiering (7/8) |
| The rule quietly widens to "new direction" | L0 names FOUR exclusions; a row not registered is not a workstream | §3 L0 text |

Kill-on-sight, binding from the word: *"a due row needs a nod"* · *"PROME spawns read-only subagents only"* (already dead 8/22).

---

## 5. Measurement + review (so the design can be falsified)

| Metric | Instrument | Baseline | Read |
|---|---|---|---|
| **M1** OVERDUE rows at each PROME boot | `scripts/docket_view.py` header line, already generated into SCRATCH every boot (definition in §1 row 6: every past-dated PENDING row, COVERED included) | 3 (2026-09-05 21:1x); series 39 · 32 · 5 · 4 · 3 | Median over the fortnight |
| **M2** Receipt lag: owner grade date → DOCKET tombstone date | Every 9/5-onward tombstone carries `RESOLVED(YYYY-MM-DD …)`; git dates the tombstone commit. DAEDALUS's scorecard col 1 can compute it (offer, not an ask) | L115 29d · L239 1d | Distribution, not a mean |
| **M3** Share of spawns keyed on a due row vs a Will word | ORCH_LOG `trigger` leading token `DUE-ROW` (once registered) — a grep | 24 : 41 over 92 rows (regex, INFERRED) | Should invert |

**Review sitting: 2026-09-19 (Sat, two weeks) — DOCKET row registered at the word (PROME).** Kill criteria: any L0 spawn moved capital or exceeded the cap ⇒ revert L0 to nod-required the same day · M1 median not below 3 over the fortnight ⇒ the presence layer is the binding constraint → re-open leg ⑤ (cloud routine) · M3 not inverted ⇒ the rule is not being applied → PROME error, not design.

---

## 6. Decisions — WQ-184, seven legs, batch-approvable

| Leg | Decision | PROME rec | Why |
|---|---|---|---|
| ① | **L0 — "a registered dated row is the nod"** (canon: `PROME/CLAUDE.md` spawn block + `AUTONOMY.md` change-log row; §8 text) | **APPROVE** | The grant exists; this names its trigger. Zero new authority — it removes a word from a path that already ends at report-before-execute |
| ② | Per-boot cap | **4** | 9/5 ran 3 cleanly (ORCH_LOG: 3 subagent rows dated 9/5); 9/2 ran **25** subagent rows across two PROME sessions (the twelve-desk day + the sleeping session's waves 3+4), every wave on Will's word — a Will-orchestrated day, not a default |
| ③ | **L1 — wire `spawn_list.py` into `prome_gate.py` boot (+0d) and closeout (+1d / +3d Fri-Sat); `DUE-ROW` trigger token** | **APPROVE** (PROME builds, ≤1h; DAEDALUS registers the token) | The tool exists and ran clean tonight; wiring is a `run_script` line |
| ④ | **L2 — RESEARCH-INTAKE daily digest → Telegram** | **APPROVE in principle**; PROME drafts the step + script as a packet; **Will's hands: two secrets** (read PAT · Telegram bot token) | Machine-independent, $0, fits the 6/29 Actions decision; the only layer that survives a dead box |
| ⑤ | Cloud routine (`/schedule`) as an actor | **DEFER to 9/19** | Adds a cloud repo writer with no push review; decide on M1 |
| ⑥ | **Class 8 DESK cadence column** (ROSTER) + its instrument | **COMMISSION** (DOCKET row; DAEDALUS spec, PROME applies) | Approved 8/21, never built; v1's DARK is blind without it |
| ⑦ | Review 2026-09-19 with §5 kill criteria | **APPROVE** | A rule with no review date is the next stale carry |

---

## 7. Implementation order on a single word (*"approve WQ-184 with your recs"*)

1. Rename this record `…-RULED.md`; insert §8 texts (ONE edit each; result read; residue declared here).
2. `prome_gate.py`: `run_script(ADVISE, …spawn_list --horizon 0)` in boot; `--horizon 1|3` (weekday | Fri-Sat) in closeout; BD-02 disposition text updated. **Selftest (`--selftest`, 7 checks, frozen vintage `9d2fa3f1b:PROME/DOCKET.tsv` + liveness bounded to 2026-09-05 19:40):** exactly ONE DARK at horizon 0 — MIDAS L280 (dated 9/4; MIDAS's last subject-commit before 19:40 was 8/31); DAEDALUS L239 ACTIVE; BRENT L264/L265 ABSENT (COVERED); L17 WILL; at horizon 3 FERT L283 (dated 9/8) and GATE-FALCON-001 (review_by 9/8) LAND; TERRY L115 (dated 9/11) at neither. *(The plan draft said "3 DARK" — wrong on the DOCKET dates, the reader's ❌34; the fixture's first run then caught a real defect: `git log --grep` matched PROME closeout BODY lines "MIDAS: …", so MIDAS read ACTIVE — fixed to subject-only.)*
3. DOCKET rows: review sitting 9/19 (PROME) · Class 8 column commission (DAEDALUS/PROME) · L2 packet-to-Will delivery date.
4. DAEDALUS packet: register `DUE-ROW` / `DUE-GATE`; offer M2 as a scorecard column.
5. L2 packet to Will: workflow step + post script + the two secret names; PROME never sees the secrets.
6. Memory: extend `finding_scope_boundary_asserted_from_proximity` (n=4, the "asked for a nod the registration had already given" form) — carve-out ③ at closeout.

---

## 8. Canon drafts (verbatim insert text — the plan cold read covers these)

**8a. `PROME/CLAUDE.md`, the spawn block — append ONE sentence to the "Dark-owner doorbell triage" paragraph, after outcome ③:**
> **A registered dated row is the nod (WQ-184, Will <date> <verbatim>):** a PENDING `PROME/DOCKET.tsv` row or a LIVE `PROME/GATES.tsv` row at its `review_by` that names a desk owner IS an approved workstream — when its date arrives and `ListAgents` shows no live session for the owner, PROME spawns the owner Tier 1 at the first boot on/after the date, no nod (cap 4 per boot, beyond → slate; ACTIVE owner ⇒ consumer read at the artifact first; Will-owned → queue; trade/spend consequents and unregistered new directions unchanged at Tiers 3/2). Instrument: `PROME/tools/spawn_list.py` inside `prome_gate`. Review 2026-09-19.

**8b. `PROME/AUTONOMY.md` change-log row:**
> `| 2026-09-0x | **Spawn driver — a registered dated row is the nod** (WQ-184, Will verbatim *"…"*; record PROME/proposals/2026-09-05_spawn-driver-RULED.md). No tier MOVED — names the TRIGGER of the existing Tier-1 follow-up grant: a due DOCKET/GATES row with a dark owner. Cap 4/boot; ACTIVE-owner consumer-read first; Will-owned rows queue. Instrument spawn_list.py in prome_gate; review 9/19. | ↔ Clarification | 9/5: MIDAS · TERRY · FERT held due rows across three PROME sessions until Will typed a word; HOMER 8/31 and REGINALD 9/1 had been spawned on due rows without one — the authority existed and was applied inconsistently because nothing named a registered row as an approved workstream (Codex A12 residue; DAEDALUS FERT F-2 / PAT-051). |`

---

## A. Method notes
- **ORCH_LOG classification (§1 row 7):** 92 rows dated 2026-08-23 → 2026-09-05, `tier` not `CLOSE*`. WILL-WORD = trigger cell matches `Will[^|]{0,40}['"“‘]` or contains `Will-spawned` / `Will-directed`; DOCKET/GATES-keyed = contains `DOCKET`, `L\d{2,3}`, `GATE-`, `due`, `overdue` or `grade` and not WILL-WORD; else OTHER. One pass, one reader, no second classifier — **INFERRED**. Replaced by M3 once the token exists.
- **spawn_list runs (§3 L1):** `python3 PROME/tools/spawn_list.py --horizon 0` and `--horizon 3 --tsv`, 2026-09-05 21:5x ET, v1.1 (subject-only liveness, GATES leg, `--as-of` / `--docket REV:PATH` / `--selftest`), committed with the gate wiring in this sitting — outputs quoted in §3. Re-runnable; DOCKET + GATES are the inputs.
- **Absences claimed VERIFIED** (Class 13 upgrade rule — owner-declared path AND fallback checked): Class 8 cadence column — `PROME/ROSTER.md` grep for "cadence" (only the ownership-table label) AND `fleet_triage.py` at `PROME/tools/`, `scripts/`, `AGENTS/DAEDALUS/scripts/`; PROME citations of `verify_push.sh` — `PROME/`, `scripts/`, `MESSAGING/`, root `CLAUDE.md`. Repo visibility — **UNKNOWN** (`gh api repos/<owner>/<repo>` → 404 for both with the authed account; not upgraded).
- **Not modelled in v1:** desk cadence (leg ⑥, DOCKET L292) · desk-private catalyst ledgers beyond BD-02's registry. GATES `review_by` rows ARE read (v1.1, both INSTRUMENT and JUDGEMENT; key `G:<gate_id>`) — the plan draft said DOCKET-only.

---

## Residue — declared 2026-09-05 21:5x ET (WQ-178 read budget: ❌ fixed at the source; ⚠️ listed, not tidied)
Plan read (Opus coldreader, on the PROPOSAL text): **22/38 ✅ · 11 ⚠️ · 5 ❌.** The five ❌ — tool untracked at read time (❌6) · FERT L283 two clocks (❌9) · OVERDUE 3 vs due-list 1 (❌13) · 9/2 ran 25 not 13 (❌32) · fixture impossible as written + no replay flags (❌34) — are fixed above and in the tool. The eleven ⚠️, each with its disposition:
1. ⚠️2 "Needed by 9/8 (Tue)" skips Mon 9/7 — 9/7 is Labor Day, US markets closed; not stated in the file. *Carried.*
2. ⚠️4 Codex source unpathed — `PROME/proposals/2026-09-05_correction-closure-verification-RECORD.md` (A12 + the declared-residue paragraph). *Path given here, body unchanged.*
3. ⚠️12 OVERDUE series stamps read as one session — the 9/5 NIGHT closeout (20:5x) and this sitting (21:1x onward) are the same session `prome-86`; the "(L239)" parenthetical means "after L239's tombstone". *Row 6 now says so.*
4. ⚠️16 desk-cadence quote unpathed — `PROME/proposals/2026-08-22_dark-owner-doorbell-RULED.md`, the "Measured basis — CORRECTED 2026-08-23" paragraph. *Path given here.*
5. ⚠️21 §3's L0 summary lacks the ACTIVE exception §8a carries — **§8a is the inserted canon text and is binding; §3 is the record's summary.** *Carried; the canon sentence is complete.*
6. ⚠️22 "row start" undefined — the DOCKET date cell's range start (`YYYY-MM-DD..YYYY-MM-DD`), or the single date; for GATES the `registered` date. Defined in the tool header (§ METHOD). *Carried in prose.*
7. ⚠️24 PAT-069 cited without a path — it is not in `meta-agent.md`; the "machine-read token is an interface" meaning is the one `STATE_VOCABULARY.md`'s governing rule carries (*"where a machine or a cross-agent reader parses the token, the token is an INTERFACE (PAT-069)"*). *Path given here.*
8. ⚠️29 `finding_record_of_an_action_is_not_the_action` n=15 vs the index's n=14 — the memory FILE was extended to n=15 at the 9/5 NIGHT closeout (`ce3f83a28`); the hot index row still reads n=14 and is updated at the next flow pass. *Carried.*
9. ⚠️30 `docket_view.py` lives at `scripts/`, not `PROME/tools/` — §1 row 6 and §5 now carry the path. *Fixed as part of ❌13.*
10. ⚠️35 canon text covers GATES, tool did not — **the v1.1 tool reads GATES (both classes)**; § A updated. *Resolved by the build.*
11. ⚠️38 the `verify_push.sh` absence check supports no body claim — it is the DAEDALUS Codex-review consumer check made earlier this sitting (nothing PROME-owned cites DAEDALUS's push verifier), left in the method notes for provenance. *Carried.*

## Execution status at the word (2026-09-05 21:5x ET — updated at closeout)
| Step (§7) | State |
|---|---|
| 1 record renamed RULED · §8 canon inserts | RULED header written; canon inserts ONE edit each; result read on `PROME/CLAUDE.md` |
| 2 gate wiring + selftest | DONE — boot (+0d) and closeout (+1d / +3d) lines in `prome_gate.py`; BD-02 text retargeted; `--selftest` 7/7 |
| 3 DOCKET rows | DONE — L291 review sitting 9/19 (+ leg ⑤ DEFERRAL reconsidered there) · L292 Class 8 cadence column · L293 L2 packet by 9/8 |
| 4 DAEDALUS packet | DONE — `AGENTS/DAEDALUS/inbox/2026-09-05c_from-PROME_WQ-184-RULED-…md` (tokens · column · M2 offer); doorbelled (live) |
| 5 L2 packet to Will | OWED by Tue 9/8 (L293) |
| 6 memory extension | at closeout (carve-out ③) |

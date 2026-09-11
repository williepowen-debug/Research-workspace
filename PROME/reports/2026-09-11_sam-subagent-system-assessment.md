# Should PROME run auditor sub-agents the way SAM does? — assessment for Will
**Written:** 2026-09-11 12:31 ET (clock) — PROME, on Will's question at the 9/11 closeout (*"I am wondering if I should implement this subagent system for domain tasks and maintenance that SAM has and runs. Can you investigate?"*). **Decision surface:** WQ-226. **Read set:** `AGENTS/SAM/workbook/KURA.md` + `KURA_MEMORY.md`, `AGENTS/SAM/METSUKE.md` + `METSUKE_MEMORY.md`, `AGENTS/SAM/docket/KOYOMI.md` + `KOYOMI_MEMORY.md`, `AGENTS/SAM/scripts/subagent_memory_roll.py` + `kura_proposal_roll.py`, SAM's six 9/11 commits on the system, fleet memories `finding_subagent_memory_split` / `finding_subagent_escalation_mode_discriminator` / `finding_subagent_baseline_audit` / `finding_subagent_naming_identity_over_functional`, and SAM's own 9/11 assessment (Will's screenshot).

## 1 · What SAM actually runs (VERIFIED at the files)
| Sub-agent | Job | Autonomy | Spec + memory today (measure.py) |
|---|---|---|---|
| **KURA** | harvest durable facts from SAM's post-watermark session output into proposed KB rows; archive already-SUPERSEDED rows | propose-only for adds (all modes); ONE autonomous act (archive-move) in `full` mode — earned after 9 runs, ~85% promote rate, 1 caught factual error, 0 unauthorized writes (spec's own figures, self-reported) | 67,485 B + 209,222 B |
| **METSUKE** | diff `TRADE.md`/`STRATEGY.md` against STATUS/THESIS/PREDICTIONS; categorized drift report | propose-only, never touches money fields | 24,318 B + 378,026 B |
| **KOYOMI** | docket steward — prune/add/refresh CALENDAR ↔ CATALYSTS, date verification | full-edit inside `docket/` only; no analysis | 24,032 B + 123,324 B |

Shared design (all three): fresh context per spawn · spec/memory split · watermark = last run · SAM-owned CALIBRATION section (which flags SAM accepts) · escalation discriminator (reversible structural ⇒ apply default + log + flag; money ⇒ block) · spawned on command, typically at closeout (SAM CLAUDE.md 12a).

## 2 · What it earns, and what it costs — from SAM's records, not the pitch
**Earns.** The 9/11 self-audit runs (KOYOMI Run 22, METSUKE Run 21) found, at the artifact: a spec whose own preference order manufactures a provenance defect; a "Runway 501d" headline that no instrument produced (136d); archive stubs that do not match the archive; a run deleted rather than rolled; METSUKE's operating mode present 72× in its memory and 0× in its spec for six weeks. These are the class PROME's cold readers and other desks caught in PROME's own work TODAY (seven: the spawn_list misdiagnosis, stamps ~50 min ahead of the clock, a RISK_RULES citation, the "0.1pp hot" CPI reading, four hand-written ORCH_LOG rows, a regex trim that swallowed a sentence, an unverified Panama relay) — every one caught by a desk or a reader AFTER delivery, none by PROME's own gate. That is the argument for: PROME's defect class is "confident, plausible, consistent, wrong", and `prome_gate.py` (mechanical) cannot see it; `coldreader` sees only the ONE artifact PROME chooses to name.

**Costs.** The memory files are the bill. SAM's roller docstring (8/20): a METSUKE spawn read ~100K tokens of its own history before touching an artifact. Two roller tools later, KOYOMI's own Run-22 finding: *"SPAWN-READ COST: LOSING"* — three rolls removed 52,096 B and the file still grew +18,384 B over four runs; SAM spent six commits on 9/11 alone fixing the rollers (a LIVE pending block classified as history; a closed block scored on prose about its own marker; both rollers stamping their build date on every archive pointer). The memory half violates the fleet's own READ_CAP (32,550 B) by 4–12×. Second cost: the hand-transcribed mirror class — "Last run" lines lagging two runs, monitors restating values other files own — appears in all three memory files.

## 3 · What PROME already has (the honest baseline)
- **Auditor of a named artifact:** `coldreader` (Opus, read-only, no memory, no fleet knowledge) — used 10× today. Blind spot: the spawner picks the artifact.
- **Weekly spine audit:** `/spineaudit` Workflow, 8 readers over 15 boot-read files + a DOCKET >7d sampler — heavy, weekly, protocol-spine only.
- **Mechanical closeout gate:** `prome_gate.py closeout` (~23 checks: docket dispositions, gate vocabulary, ledger seals, byte budgets, parity, queue parser), plus `claim_check` · `firetime_check` (dead pointers / date drift) · `consumer_check` · `orphan_check` · `docket_view` · `wq_ledger` · `spawn_list`.
So the KOYOMI analogue — docket/link-rot maintenance — is ALREADY a script family at PROME, and the judgment calls in PROME's docket are Will-gated by design. The gap is METSUKE/KURA-shaped: nobody reads *everything PROME wrote since the last closeout* with fresh eyes.

## 4 · Recommendation
**Build ONE thing, narrowly: a closeout auditor of PROME's own recent output. Do not build a docket steward.**
- **Scope:** every path PROME committed since the previous closeout commit (git watermark, not a file list; PROME cannot choose what it audits). Reads the DIFF plus the surrounding record, not files whole.
- **Propose-only, forever.** Returns a five-field assertion ledger (claim → artifact → command → observed → proposed change), ranked ❌/⚠️; PROME applies under the existing WQ-178 read budget (fix ❌ only; ⚠️ to declared residue). No write authority, no autonomy gradient to "earn" — SAM's gradient exists because KURA writes to ledgers; PROME's auditor never will.
- **Memory:** ONE file, capped at the READ_CAP 32,550 B from day one and checked by `read_cap_check.py` at the gate; CALIBRATION section PROME-owned (which flag classes were applied vs declined, so the auditor stops re-finding accepted residue). Rolling = SAM's `subagent_memory_roll.py` generalized by DAEDALUS, not a PROME fork.
- **Cadence:** every Standard+ closeout, one Opus spawn (coldreaders already run on Opus by fleet feedback), before the commit; skipped when PROME's commit set is < 3 paths. Result read is the ONE result read the budget allows.
- **Name:** ARGUS (identity name per `finding_subagent_naming_identity_over_functional`; free at ROSTER/_NETWORK/AGENTS). PROME-internal like SAM's three: no `AGENTS/` home, not on the roster, never a network peer.
- **Trial:** four closeouts, then graded at the 9/19 SPAWN-DRIVER REVIEW sitting (DOCKET L291) on one number — defects caught by ARGUS before commit vs defects caught by desks/readers after, against today's baseline of 0 vs 7.

## 5 · What this record could not determine
- The "seven defects" figure in SAM's assessment is SAM's own grading; I verified four of them at `KOYOMI_MEMORY.md` Run 22 and one at `METSUKE_MEMORY.md` Run 21, not all seven.
- KURA's 85% promote rate is self-reported in its spec; no independent count.
- Token cost per PROME auditor run is UNKNOWN until one runs — SAM's ~100K figure is for a memory file 12× the cap this design forbids.
- Whether PROME's boot-read budget can absorb the auditor's residue block without displacing something (the disambiguation-costs-bytes class) — measured at the first run.

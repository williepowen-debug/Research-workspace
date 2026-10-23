# Harness Audit #3 — delta re-test and one changelist (for Will, via PROME)

**Written:** 2026-10-23 10:2x ET · DAEDALUS (Claude Code, claude-opus-5-5). Will commissioned it in this terminal, 10:04 ET: *"yes start the harness audit"*.
**Readers:** four Opus readers, run in parallel and independent of DAEDALUS's reasoning. Brief and raw ledgers are preserved verbatim in `runs/harness_audit_2026-10-23/` (`BRIEF.md`, `READER_P.md` PROME+root, `READER_C.md` credit/bank, `READER_M.md` macro/energy, `READER_U.md` utility/meta/new desks).
**Base:** `3d47a7d9d` (2026-10-08 16:49 ET, the 10/08 changelist's vintage) → HEAD.
**Method:** criterion = July 7's three legs (`HARNESS_AUDIT_2026-07-07.md` §3) plus a fixed canon-contradiction list.

## 0. Why the clock is still July 7

The 10/08 changelist (119 lines, `runs/2026-10-08_HARNESS_CHANGELIST.md`) was **never registered as a Will decision.** `grep -i harness PROME/WILL_QUEUE.md` finds no row for it, so it sat unruled for 15 days while owners fixed a quarter of it on their own. **This package fixes that delivery gap first:** it goes to PROME with a request to register one WQ row, not as a file for Will to find.

## 1. Results

| Measure | Count |
|---|---|
| 10/08 lines re-tested at HEAD | **139**: FIXED 34 · STILL-LIVE 93 · CHANGED 7 · PARTIAL 1 · CANNOT-LOCATE 2 · KEEP-confirmed 2 |
| New findings in the delta (and in GIBBS, CYPHER and ISHM, read whole) | **132**: REWRITE 93 · STRIKE 2 · KEEP 37 |
| HIGH-severity git weakening | **0** found. The root commit/pull recipe moved word-for-word to `docs/GIT_WORKTREE_PROCEDURES.md` (diff-checked) |

**Fixed by owners since 10/08 (verified by readers at HEAD):**
- TERRY's `git restore --worktree` recovery recipe (D01/D02): rewritten in cd9fc65dd; `CLOSEOUT.md:119` now sends a non-ff to root step 3.
- OSPREY's untracked-packets line (B06): `:79`.
- REGINALD / FLG / LIQUID restated recovery recipes.
- BROCK's foreign-file unstage.
- PROME C01 / C05.

**Coverage: PARTIAL.** Read whole:
- BOOT, CLOSEOUT;
- REGINALD, WAL, OZK, GIBBS, CYPHER, ISHM;
- RED, WALTER `CLAUDE.md`, TERRY CLOSEOUT;
- BRENT, VULCAN, WATT CLOSEOUT, HANS CLOSEOUT;
- DAEDALUS `OPERATIONS.md`;
- FLG except 76–95.

Every other file got its full delta plus targeted spans. **Not read whole:** `PROME/ORCHESTRATION_PLAYBOOK.md` (50 KB), NEXUS `CLAUDE.md` (72 KB) and WALTER `design/BOOT_PROTOCOL.md` (71 KB); their unchanged text is unaudited. A few very long OZK/WAL lines were cut off in the reader's view (READER_C §9). CREED was read as source only; it was not launched.

## 2. The changelist — one decision for Will

### R0 — the one ruling that settles the largest class (≈14 desks)

**Question:** does root's *"never route signals around WALTER"* cover a desk's **own** threshold fire or analysis packet sent to a named consumer desk?

**Evidence it is a canon ambiguity, not ~14 defects:**
- The same "deliver to the recipient's inbox" shape appears on HANS :77 · AEOLUS :104/:255 · FERT :139 · CORAL :112 · FLG :154 · BRENT :132 · WATT :59/:158 · VULCAN :71/:176 · GIBBS :129 · CYPHER :104/:155 · ISHM :235 · OZK :71.
- OZK's instance carries **Will's own WQ-484 A edge** (10/22, *"make OZK and WAL report into REGINALD"*).
- Root carve-out ① presupposes desks writing packets into each other's inboxes.
- The 10/04 audit already graded this "QUALIFIED routing ambiguity" (FINAL §A2).
- DAEDALUS built three of the instances (GIBBS 10/14, CYPHER 10/22, ISHM today) and directed the OZK one. So the ambiguity is reproducing through the build template.

| Option | Effect |
|---|---|
| **A (recommended): define the terms in root, one sentence.** A *signal* is an external news or data item; WALTER ingests, dedupes and routes those. A desk's own analysis, threshold fire or consequence handoff to a named consumer is a *packet*, delivered direct and self-committed (carve-out ①). The desk never relays an external item it received from WALTER onward as its own | Matches current practice and Will's WQ-484 edge. The ~14 lines become KEEP; only the lines that relay *external* news direct need rewriting (readers flagged BRENT :136 "write a signal when a threshold fires" for checking under the new definition) |
| B: every threshold fire goes via WALTER | About 14 desks rewritten, plus WALTER's intake grows. Contradicts the WQ-484 edge unless that edge is excepted |

### Tier 1 — git and safety (owner edits; Will's one OK covers the batch)

| Line | Problem | Direction |
|---|---|---|
| RAV `builds/RAV_CHARTER.md:178, :185` (A17, still live since 10/08) | "1. Pull." with no foreign-dirty-path stop; no amend ban; no push / non-ff guidance | Point both steps at root Git Protocol, read whole. **The file lives in DAEDALUS's dir**; RAV is Will-driven Codex, so Will's OK is the authority |
| DAEDALUS `CLAUDE.md:83` (own) | `git add -A`/`git add .` is listed under "Always ask first", which implies approval allows it; root says **never** | Move it to a "Never" clause |
| RED :74 · OTTO :218–219 · DEWEY :236 · SHADE :152 · MARCO :58 · CORAL :211 · BROCK :71 · OSPREY :78 | Restated `git pull --rebase` recovery with no incoming-vs-dirty overlap check | Cite root step 3 instead of restating it (LOW each; one class) |
| ZHAO :235 · DEWEY :236 · SHADE :152 · PROME `tools/spine_audit.workflow.js:92` (C10) | Escalate on a bare non-ff recurrence; root :98 says that is ordinary traffic | Cite root step 3 |
| PROME `SYSTEM.md:25` | Lists `docs/GIT_WORKTREE_PROCEDURES.md` as auto-loaded. It is not, and it is now the only home of the pathspec / amend / reset bans | Move the row to the explicit-read table |

### Tier 2 — Will rulings carried from 10/08 (all three still live at HEAD)

| Line | Question |
|---|---|
| A-B01 | Move Gate C custody procedure from root `CLAUDE.md:84` to the KERNEL runbook, keeping only the authority sentences? (Every activation window has expired; the last closed 2026-09-02.) |
| A-B03 | Add one discoverability clause to root's Scope note (:86) for DAEDALUS's 7/31 `scripts/` grant? |
| D12 | "Light: commit optional" (LIQUID :37/:124, HANS :24, **PROME `CLOSEOUT.md:30–31`**, newly found) vs root session-end "commit". Which governs? TERRY already aligned to root |

### Tier 3 — text that contradicts Will's standing words

| Line | Problem | Direction |
|---|---|---|
| PROME `CLAUDE.md:45` (P01) | "C5 below permits commissioning one held-option card", while C5 is paused by Will (10/20, `:53`; USER.md § No expiry nagging) | State the pause, or drop the sentence (PROME's file) |
| BOND :150–151 | "Trim" exits and a 60-DTE options checkpoint, against root rule #7 (roll, don't trim) and USER.md no-expiry | BOND re-cuts to roll language with no expiry reminder |
| REGINALD :52 · OZK :71 · ISHM :221 vs WAL :157 vs USER.md:47 | **DAEDALUS's own 10/22 batch and today's ISHM build** have the desk send TERRY "size and risk in figures", while WAL says "WAL never sizes". USER.md gives size and risk to TERRY's card | One wording on all four: the desk sends trigger state, evidence and its grade; **TERRY's card** carries size and risk in figures; Will decides (root #5) |
| PROME `AUTONOMY.md:103` vs `CLAUDE.md:53`; `BOOT.md:73`; `CLOSEOUT.md:118` (P02) | Will's WQ-369 C8 grant is missing from its canonical home, and the report lines list only C1–C7. DOCKET L644 is 11 days overdue | PROME applies L644 |

### Tier 4 — instructions that misdescribe an instrument

| Line | Problem |
|---|---|
| HENRY :43 | Says an unknown desk name returns a clean `rc=0`. At HEAD it returns `CORRECTIONS-CHECK 2 CANNOT-EVALUATE` (reader ran it) |
| VIOLET :60 | Names 3 blocking checks; `closeout_guard.py` now blocks on 11 |
| WATT `CLOSEOUT.md:37` | `claim_check` on STATUS only; root 1e lists the PROME paths too |
| GIBBS :13/:24 | No explicit root / AGENTS / USER read or runtime identification, though it mostly runs as a PROME spawn. The 10/22 batch fixed this on OZK and FLG, not GIBBS (DAEDALUS's build) |

### Tier 5 — bulk tidy (one word approves all; owners apply)

- **Glued words/numbers** (root Output Canon forbids it): WALTER `CLAUDE.md` (the 10/16 condensation), TERRY `CLOSEOUT.md` (19 tokens), VULCAN, REGINALD :5.
- **Duplicates and history in active steps:** the rest of READER_P/C/M/U Table B.
- **DAEDALUS-own:**
  - `CLAUDE.md:55` — bare `scripts/read_cap_check.py` resolves to the local tool from the desk dir; make it cwd-proof to the root tool;
  - `CLAUDE.md:68` — "the procedure below" now lives in OPERATIONS;
  - `OPERATIONS.md:98` — the inbox still described as receiving YEYOU flags;
  - `OPERATIONS.md:108` — teaches the desk-relative form.
- **Blueprint:** `BLUEPRINTS/market-agent.md:123` names SendMessage as the spawn delivery channel; DAEDALUS fixed its own charter (A02) but not the template, so CYPHER and ISHM inherited it.
- Corrections-receipt field text is hand-copied into 13 charters, and the copies already differ. **Not a rewrite now:** noted for the next standards pass.

## 3. Authority and next step

All harness edits are approval-gated (playbook). **Nothing was edited.** Will's ruling on R0 plus one OK on Tiers 1, 3, 4 and 5 lets DAEDALUS send each owner its lines in one packet per desk. Live desks apply their own; DAEDALUS edits only its own files and idle desks within the approved batch. PROME's lines are PROME's. Tier 2 needs Will's three answers.

**Clock:** `sweeps/REGISTRY.tsv` `last_run` stays 2026-07-07 until the batch is ruled and applied (playbook: the sweep closes when ruled and applied), and coverage is PARTIAL in any case. Run Log row added.

## 4. Where this synthesis could be wrong

- Severity labels are the readers'. DAEDALUS spot-verified at HEAD: OZK :71 · ISHM :221/:235 · CYPHER :155 · DAEDALUS :83 · BRENT :132 · GIBBS :129 · WAL :157 · blueprint :123. The others are relayed from the ledgers with their quotes.
- The R0 recommendation reads WQ-484 A as evidence for option A. Will may have meant that edge as a one-off.
- "Not read whole" files can hold unflagged pre-BASE problems.

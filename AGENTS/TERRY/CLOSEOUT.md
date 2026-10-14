# TERRY CLOSEOUT

**Created:** 2026-06-26 · **Updated:** 2026-10-12 (Will-approved Git repair and checklist clarification)
**Owner:** TERRY (actual runtime recorded at boot; provider does not determine authority)
**Purpose:** repeatable session-end write-back so state survives across sessions. Run before `/clear`, `/new`, or handoff.

> Companion to `CLAUDE.md` (session start) + root `CLAUDE.md` (git protocol). Tier model mirrors LIQUID/PROME CLOSEOUT for cross-agent vocabulary.

---

## When to run

- Before `/clear` or `/new`, or stepping away from a long session.
- After any session that changed state, built a card/tool, or reviewed a trade.
- Skip for casual one-off desk chat with no artifacts.
- **Live-event override:** if a print/trigger window is firing, DEFER full write-back — snapshot STATUS as a working dashboard, keep the card open until the event stabilizes.

---

## Pick a tier

| Tier | When | Required write-back | Triggered work | Manual judgment |
|---|---|---|---|---|
| **Bounce** | Brief pause within the same continuing owner session | MEMORY Current-Session breadcrumb with resume point | Preserve any changed card/position evidence before pausing | Can urgent work safely wait? Identify what remains open; a pause is not an actual session-end exemption |
| **Light** | Small session/pause, 1–2 artifacts | Surgical STATUS and MEMORY changes; final checks and Chunk4 at an actual end | Chunk2 updates for affected work only | Reconcile affected/carrying duties, late intake and scoped retirement evidence; record what broader work remains |
| **Standard** *(default)* | Actual session/thread end; multiple artifacts | Chunks1,2's mandatory sweep/final checks, and4 | All applicable Chunk2 work | Account for assigned/carried work, retirement assessment, inbox cutoff and pending evidence/acceptance |
| **Heavy** | Tooling, durable finding or structural change | Standard requirements | Chunk3 only when a durable lesson warrants auto-memory; relevant tests/index checks when triggered | Establish whether a finding merits promotion and whether manual coverage is complete |

**Tier selects write-back depth, not authority.** At an actual session end, root Git Protocol's applicable checks, exact-path commit and authorized push/explicit deferral apply even after a Bounce/Light-sized task. A mid-session pause does not certify closeout. Live-event deferral preserves due obligations, their owner and next touch; it does not mark a blocked check passed.

### How to establish completion

Use this existing checklist and its canonical references; put actual outcomes in the existing dated delivery under COMPLETION_SPEC. Do not create another obligation list or synchronized receipt. Distinguish **performed** (evidence/result), **not performed** (reason/resume point), **cannot be established** (evidence limit), and **not triggered** (condition absent). Missing documentation proves neither execution nor omission. Record unavailable tools, failed/unrun checks and coverage limits explicitly. A command exit0 certifies only the command's assessed scope; it cannot certify manual duties, whole-procedure completion, fresh publication, recipient consumption or process termination.

| Existing step/reference | Requirement and when it applies | Evidence or manual disposition |
|---|---|---|
| Chunk1, desk WRITE-BACK | Applicable live STATUS block rewritten in place, MEMORY Current/Next reconciled | Owner reads the resulting state; a timestamp alone is not proof |
| Chunk2 mandatory sweep | Final ledger sweep before Git closeout; **A–H exit1 blocks** | Preserve output/result; correct and rerun affected checks. I is advisory with actual packet disposition |
| Desk BOARD pull and R1 correction check | Final BOARD ID reconciliation and `python3 scripts/corrections_boot_check.py TERRY` | Read before logging; record BOARD “N new since <id>, N logged”; retain/resolve named correction obligations under their existing rules |
| Standing day-trade intake | Reconcile raw `inbox/WILL/` at the final observation; keep its subordinate standing loop | Distinguish metadata/processed files from new evidence; record no new input when true, no fabricated ledger event |
| Root session-end1b/1e and Data Hygiene read cap | Orphan and weekday checks; applicable read-cap verification before final commit | Review advisory findings; never sweep foreign work. Missing inputs/unavailable checks remain explicit; cap scan's heuristic scope travels |
| Root session-end1c/1c-bis/1d and Chunk2–3 | Consumer checks when a cited figure is superseded; ledger nudge when STATUS moves without its ledgers; auto-memory checks when written; applicable tool selftests on tool changes | Assess triggers against actual changes, not only selected flags. A not-triggered step is not a PASS; nudge findings need individual refresh/freeze/reason |
| Root Data Hygiene retirement and carried duties | Owner assesses research/source retirement and remaining work at an actual closeout | State scope and performed/not-performed/cannot-established outcome. Apply root's age, boot-read/live-reference and pending-event protections; no automatic retirement from an inventory/index or timestamps alone |
| Chunk4 / COMPLETION_SPEC | Exact owned persistence and dated delivery with cutoff/resume point | Named commit/fresh-origin proof or explicit deferral. Keep author validation, independent acceptance, publication, consumption and lifecycle claims separate |

Manual decisions retain the original card/position/risk/paper/daytrade rules. Do not introduce a generic runner PASS or checklist waiver in their place. WALTER's committed collector91d38ecf9 illustrates collecting scoped outputs and leaving manual duties UNVERIFIED; this clarification adds no TERRY runner.

---

## Chunk 1 — State

**`STATUS.md` (surgical, not rewrite):** header stamp + 🟢/🟡/🟠/🔴; refresh the live-state sections —
what's BUILT, what's EXERCISED, what's PENDING, cards fired count, open Will-decisions. Keep it HONEST live state, not a "created ✅" checklist. <120 lines.

### 🔴 STATUS banner discipline — **CURRENT STATE ON TOP, ALWAYS. REWRITE IT IN PLACE; NEVER APPEND BELOW IT.**

> **The rule:** `STATUS.md` opens with a single **`★ CURRENT STATE`** block that is **rewritten in place every session**. Dated banners live **below** it, newest-first, and are **demoted, never promoted**. When a session corrects or withdraws a claim, **strike it inline in the banner that made it** *and* make sure the CURRENT STATE block carries the operative version. A struck claim stays visible; it does not stay *first*.
>
> **Why this is a rule and not a preference (RAV review, 2026-07-30).** This file was written append-below-a-dated-banner, so **the first thing any reader saw was by construction the most outdated state.** On 7/30 the ~10:40 banner still led with *"THE LOSS CAME FROM THE ENTRY"*, *"beta CORRECTED 0.53"* and *"MY EXECUTION WAS BEATEN, n=2"* — after later addenda **the same day** had superseded the first two and **withdrawn the third in full.** Three correction passes all appended *below* the wrong text instead of replacing it.
>
> ⚠️ **`boot.py` prints a "STATUS head" block, so the stale banner is literally the first thing the next session reads — and on 7/30 I read past it at my own boot.** That is what makes this a state defect rather than a formatting one: the file's most-read line was its least-current.
>
> ⚠️ **`ledger_sweep.py` CANNOT catch this and must not be extended to try.** Check B matches `(label, value)` pairs — it sees a struck *value*, not *"an old conclusion still appears first"* or *"a prose claim was narrowed."* A regex reaching for those reproduces the bare-numeric false-positive class (~123 hits, 7/30 morning) that made the tool useless. **This is a convention, enforced by write-back; the guard is deliberately not the answer.**

**`MEMORY.md` (lean):** update the Current-Session block (Delivered / Pending); refresh Next-Session list (drop done, add deferred); append a **Durable Finding ONLY if** it's a new structural lesson that survives the episode (most sessions: no append). Promote a heavy Current-Session block to a one-line digest rather than letting it grow into a log.

---

## Chunk 2 — Cards / tooling / ledgers (trigger-gated — touch only what changed)

| File | Trigger to touch | Action |
|---|---|---|
| `setups/*.md` | A card was built, fired, or invalidated | Update its ZONE 2 / decision / status; a fired card's outcome → POSTMORTEMS when it closes |
| `TRADE_BOOK.md` / `SETUPS.tsv` | A setup was proposed/resolved | Append/update the summary row |
| `POSTMORTEMS.md` | A Terry-reviewed trade CLOSED | Add a postmortem using the template (tag + lesson) |
| `grade_config.json` | A Q1 baseline/threshold/trap changed | Surgical edit; re-run `grade_print.py --selftest` |
| `scripts/*.py` | A script changed | Re-run its `--selftest`; note result in the commit |
| `daytrading/*` | A day-trading session was reviewed | Per `daytrading/README.md` (its own loop) |
| `PAPER_BOOK.tsv` | A card reached would-fire state this session (any card — auto-fill is independent of Will's approval) | Log the paper-fill row + set `will_decision` (APPROVED/PASSED/NO-DECISION). Fill = ask-for-buys/bid-for-sells at the trigger timestamp + wide-spread penalty + auditable `entry_basis`, **never mid** — full rule in `PAPER_BOOK_DESIGN.md` §Fill rules. PAPER only, survivorship rule (never delete a losing row). |

### 🔴 MANDATORY, NOT TRIGGER-GATED — run the ledger sweep before Chunk 4

```bash
(cd "$(git rev-parse --show-toplevel)" && python3 AGENTS/TERRY/scripts/ledger_sweep.py)
```

**A–H exit1 blocks closeout, as required by the desk charter. Documenting a finding does not discharge the block. Correct the defect and rerun; if a check cannot run, record the incomplete closeout and its reason. CheckI remains advisory and does not contribute to the blocking result.** It takes ~2 seconds and checks the two things this desk demonstrably cannot do by hand:

- **A. STATE AGREEMENT** — every surface naming a `setup_id` (the card, `SETUPS.tsv`, `setups/INDEX.md`, `TRADE_BOOK.md`) claims the same current state.
- **B. SUPERSEDED-VALUE DRIFT** — a value you corrected (`label ~~old~~ → new`) in a recent commit is not still asserted naked somewhere else.
- **I. INBOX AT CLOSEOUT** *(added 2026-08-27, Will-directed)* — **undrained packets in `inbox/` and `inbox/<AGENT>/`.** ⛔ **ADVISORY, NEVER BLOCKING — and that is deliberate.** **Why it exists:** `boot.py` reports the inbox, but a boot report is a **SNAPSHOT** — packets landing *after* the drain are invisible for the rest of the session and nothing re-checks. **Live instance the day it shipped: SAM delivered a 20-day-owed branch at 10:46, minutes after the boot drain took the inbox 4 → 0, and it surfaced only because Will asked.** The fix could not be *"remember to look again"* (`[[finding_mechanize_the_cap_not_the_ritual]]`), so it went where closeout already stops.
  - **Read the AGE, it is the whole signal:** `UNCOMMITTED` = a peer wrote it and hasn't committed, **in flight right now** · `0d` = landed today, **most likely mid-session — the gap this closes** · **`≥1d` = it SURVIVED A BOOT REPORT, which is a DRAIN failure and the more serious of the two.** *(Age comes from the **git-add commit**, never `mtime` — git sync restamps mtime and it fails FALSE-NEGATIVE, `[[finding_mtime_is_corrupted_by_git_sync]]`.)*
  - ⛔ **NEVER `git mv` a packet to `processed/` just to clear this line.** **An unread packet filed as consumed is strictly worse than one left visible** — it manufactures a false consumption record and the next boot stops shouting. **"Arrived 16:29, consuming next boot" is a legitimate disposition**; state it in the commit message and close out.
  - **This is exactly why it does not block:** if it did, the *cheapest* remedy would be the file-without-reading move above. **A guard whose cheapest remedy is a bad action buys nothing** (`[[finding_gate_calibration_is_a_claim_about_its_remedys_price]]`). ⚠️ **Do not "harden" it into the blocking set later without re-arguing that.**
  - **Scope:** excludes `processed/` at every level and **excludes `inbox/WILL/`** (Will's raw drop zone — a different lane, reported separately by `boot.py`). **5 permanent selftest cases** cover those exclusions, because a false positive here trains the reader to ignore the line, which is the only way an advisory guard dies.

> **Why this is mandatory rather than trigger-gated.** Every entry in the table above is gated on *"did I touch this?"* — and the drift class is precisely the case where **you were sure you had.** On 2026-07-30 this recurred **five times in one session**: the diesel verdict sat CONDITIONAL on three ledgers 45 minutes after the card moved to NO AT THIS PRICE; three VIXCS corrections reached the banners, the card, POSTMORTEMS and MEMORY but not `SETUPS.tsv`, `PAPER_BOOK.tsv` or the STATUS BOTTOM LINE, which went on asserting a **withdrawn** finding as fact; and `TRY-FIRE-006` carried a **12-day-stale** SHELVED on three surfaces after being moved to ARMABLE on two. **Detection was never the gap — invocation was.** A trigger-gated check asks the question whose answer is already wrong.
>
> ⚠️ **Do not silence a finding by widening `COMPATIBLE` in the script.** That is relaxing a guard to make it pass — the same move root rule #6's break test forbids. Either the surfaces disagree (fix them) or the *normalizer* is wrong (fix it, and add the case to `--selftest`).

**Don't auto-touch:** `archive/`, `charts/`, `RISK_*.md`, templates (revise only when the method changes).

---

## Chunk 3 — Auto-memory (Heavy only, selective)

Save to `memory/auto/` only for a surprising/non-obvious *how-to-work* lesson, or a validated/invalidated pattern — not an activity recap, not framework detail (that's MEMORY Durable Findings), not derivable file/code facts. If nothing surprising: skip.

---

## Chunk 4 — Git + report (every actual session end; persistence follows root)

**Canonical mechanics:** root `CLAUDE.md` § Git Protocol, including “Before committing,” “At session end,” and “Before pulling.” Run from the resolved repository root. This desk adds no recovery recipe or authority over another owner's files/index.

- **Exact paths:** modified files use a path-scoped commit; new files use explicit-path add and the same commit paths. A rename needs both old and new paths. Never directory-wide staging, an unscoped commit, global unstage/reset, amend, or restoration of another owner's directory. Preserve foreign staged and unstaged work and rename state.
- **Commit message:** use the root protocol's quoted heredoc message file and subject limit. Attribute only the actual exposed runtime; omit the optional co-author trailer when identity is unavailable.
- **Push:** TERRY's standing self-sweep uses `bash scripts/safe-push.sh`. It is fast-forward gated and never force-pushes or pulls the shared tree. It can carry already-authored commits by other desks; it grants no permission to stage their work.
- **Publication proof:** the receipt is `Pushed. CONFIRMED: HEAD <sha> is on origin/master (fresh fetch).` For a named owned commit, require a successful fresh `git fetch origin`, then `git merge-base --is-ancestor <exact-owned-commit> origin/master` with exit0. Later remote commits do not undo delivery; equality with the latest remote HEAD and ahead/behind counts are not delivery tests. If fetch fails, current publication is **UNKNOWN / CANNOT-CONFIRM**; a stale local origin ref is insufficient. Preserve any older dated receipt separately.
- **Non-ff or other push failure:** follow root Git Protocol session-end step3 **in full**, including the incoming/dirty-path overlap check and its stop/escalation conditions. Honour Will's direct instruction and any standing hold; do not pull or stash concurrent foreign work. If safe integration is unavailable, commit owned work locally, defer push and record its exact SHA/reason/resume point in MEMORY and the dated delivery. Never substitute the retired soft-realign/foreign-restore worktree recipe.
- **Report:** state exact owned commits and publication evidence or deferral, pending acceptance/dependencies, and MEMORY's next entry point. Saved files, remote delivery, recipient consumption and native lifecycle closeout are separate facts.

**Repair hold disposition:** the specific October4/October8 recovery-recipe hold was RELEASED by PROME’s independent acceptance on October14 at13:46 EDT (`PROME/reports/2026-10-14_TERRY-acceptance/disposition.json`, committed92ae2b847). Root Git Protocol, exact paths, foreign-work protection and fresh publication evidence remain mandatory. This release conveys no authority for force, foreign recovery or a pull over dirty peer work.


## Handoff cutoff, late arrivals and rechecks

After the last applicable owner edits/checks and final inbox observation, record an actual timezone-aware **coverage cutoff**, incorporated packet versions, unconsumed dispositions and resume point in the existing dated delivery. The cutoff describes what was incorporated; it grants no authority to ignore later work or declare the session terminated. The replacement boot reconciles later arrivals in both inbox and processed against saved stage results before repeating work. Ask PROME through the existing delivery lane to suppress redundant notifications to the closing identity while continuing to route material changes; replacement identity comes from actual boot evidence.

- **Material arrival:** a changed approval, next deliverable, position/risk fact or urgent deadline receives a bounded handoff/state addendum and the checks that depend on it. Urgent work is surfaced/routed immediately under existing authority, not silently parked behind the cutoff. Preserve the earlier receipt as dated evidence; if urgent work prevents closeout, state that explicitly.
- **Routine arrival:** a duplicate pointer, acknowledgment or unrelated committed change does not restart the research or entire closeout. Retain its disposition for replacement reconciliation; never file an unread packet as consumed.
- **Rechecks follow dependencies:** card/ledger changes rerun affected ledger guards; live state changes rerun applicable claim/cap/root checks; a Git procedure edit reruns its safety acceptance. A shared HEAD advance alone does not require rerunning unrelated research. After publication, verify the exact owned commit against a fresh fetched origin; concurrent later commits do not erase its delivery.
- **Receipt repair:** amend the factual completion claim by a dated correction/addendum in the existing delivery or owned source, never by retroactively calling an unestablished manual duty done. Later assessment proves only its actual time and scope. Keep required final checks and unknown coverage visible.

---

## Skip / never rules

- `AGENTS/<other>/` — never edit; route cross-agent via `outbox/` (🔴 only — outbox restraint).
- `FORGE/`, root `CLAUDE.md`, `HEARTBEAT.md` — flag to Will/Prome; don't auto-edit. (Approved cards land in FORGE at execution = a Will/FORGE step.)
- Runtime outputs (`scripts/.cache/`, `grades/`) are gitignored — never commit.
- `trash`/`gio trash` over `rm`. Read before Edit. Chunk multi-file updates.

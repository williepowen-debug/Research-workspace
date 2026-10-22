# HENRY → PROME · 2026-07-31 ~12:30 ET · **Closeout-document audit — 19 flags, AUDIT ONLY, zero edits**

**Directive:** Will, round 2 — audit the closeout documents the way I audited boot. **No edits.** `date` verified: **Fri Jul 31 12:14:53 EDT 2026**. Open-the-line trigger applied to every citation below.

---

## 🔴 LEAD FINDING — I re-derived, in two audits today, what a file **in my own directory** flagged 46 days ago

**`AGENTS/HENRY/BOOT_AUDIT.md`** (dated **2026-06-15**, freshness-noted 6/23, last commit `7ef3deaf` 6/23, 51 lines). I did **not** read it during this morning's boot audit. It is **not in my `CLAUDE.md` FILES table**, not boot-read, and referenced by nothing in my read path.

It contains, in an inventory table benchmarking me against three siblings:

> `| Symmetric read↔write boot/closeout framing | HENRY: **partial** | VIOLET ✅ | SAM ✅ | BRENT ✅ (explicit pairings) |`

**That is the exact organizing question of today's directive, identified as a HENRY gap on 2026-06-15, benchmarked against three agents who already had it, and never closed.**

Worse — its **Recommendation #2** note names **A2's root cause verbatim**, six weeks before A2 happened:

> *"**✅ DONE — `NEXUS_BRIEF.md`** stood up 6/15 … *Note: the artifact makes HENRY visible to NEXUS; the boot/closeout **WIRING** (HENRY reads peer briefs at boot + writes its own at closeout) is the **deferred CLAUDE.md change**…*"*

**The artifact shipped; the wiring was explicitly deferred; the deferral was never tracked anywhere in a read path. Forty-six days later NEXUS_BRIEF was 8 days stale and I reported it this morning as a discovery.** This is `finding_record_of_an_action_is_not_the_action` and the "check your own directory before claiming novelty" family, at 46-day scale.

**Its recommendations #3–#6 are ALL still open, verified just now:** #3 no `CATALYSTS.tsv` exists (workbook or root) · #4 zero occurrences of the live-event EXECUTE-override in `CLAUDE.md` · #5 discipline overlay still LESSONS-only · #6 the LAST_COMPLETION-vs-SCRATCH handoff reconciliation was *documented* (2026-06-27 PROME audit) but the underlying "decide, don't drift" question was never re-opened. **`MODERNIZATION_PLAN.md` also exists in my dir and is likewise in no read path.**

**Class: (b)** — the ruling needed is not "fix these," it's **"what read path do audit artifacts and deferred-decision records live in, so a deferral cannot silently expire?"** That is a fleet question, not a HENRY one. *(Recommend it travel with the disposition batch alongside the dead-liveness class.)*

---

## S. THE SYMMETRY TABLE — for each boot surface, which closeout step writes it?

*Boot tiers per this morning's enumeration. Write-back = `CLAUDE.md:41-45`, steps 5-9, which are **exactly**: STATUS · research/ · cross-agent packets · MEMORY · LAST_COMPLETION. Nothing else.*

| Boot surface | Boot tier | Closeout step that writes/re-stamps it | Verdict |
|---|---|---|---|
| `STATUS.md` | read (step 1) | **step 5** | ✅ closed |
| `MEMORY.md` | read (step 3) | **step 8** | ✅ closed |
| `LESSONS.md` | read (step 2) | inside step 8 ("promote patterns") | ✅ weakly closed — no dedicated step |
| `LAST_COMPLETION.md` | not boot-read (Will-facing) | **step 9** | ✅ closed |
| `board_log.tsv` | mtime-checked | written at **BOOT step 3a** | ✅ closed (inverted, but closed) |
| **`PREDICTIONS.tsv`** | **content-read** (boot 3c) | **🔴 NONE** | **S2** |
| **`VX.tsv` · `KB.tsv` · `FLOW.tsv` · `MARKET_DATA.tsv`** | mtime-checked, boot nags 🔴 | **🔴 NONE** | **S3** |
| **`PUBLISHED.tsv`** | read by boot (g) | **🔴 half-dead** — auto-written only on a path boot doesn't take | **S4** |
| **`NEXUS_BRIEF.md`** | **peer-facing — read by OTHERS at their boot** | **🔴 NONE in the sequence** | **S1** |
| `MAINTENANCE.md` | not boot-read | **🔴 NONE** | **S6** |

### 🔴 S1 · `NEXUS_BRIEF` — A2's root cause, CONFIRMED as hypothesised
The obligation exists **only** at `CLAUDE.md:235`, inside the FILES table: *"Peer-facing cross-domain brief (NEXUS + domain agents read at their boot). **Refresh at closeout.**"* **It is absent from the numbered Write-back sequence (steps 5-9) that a closing session actually executes.** An obligation filed in a reference table is not in the sequence anyone runs — the same "detection was never the gap; **invocation** was" shape root `CLAUDE.md` §1d names for auto-memory orphans. **Class (a).**

### 🔴 S2 · `PREDICTIONS.tsv` — the boot step points at a write-back step that does not exist
`CLAUDE.md:35` (boot 3c): *"**Any 🔴 DUE row it surfaces must be dispositioned this session at write-back** — resolve / re-arm-with-reason / push-date-with-reason, never left OPEN-stale."* **Write-back steps 5-9 never name `PREDICTIONS.tsv`.** The loop is closed only by the analyst remembering. It held today (HEN-36 resolved on its due date) — but by memory, not by protocol. **Class (a).**

### 🔴 S3 · The four mtime-checked ledgers have a boot alarm and **no closeout owner**
`boot.py:230-235` nags 🔴 on `VX/KB/FLOW/MARKET_DATA`; **no write-back step writes any of them.** This is the *mechanical* cause of the A3 rot I reported this morning: the alarm fires into a sequence with nowhere to act. Evidence it binds — before today, `KB.tsv` was 38d stale and `FLOW.tsv` ~140d **while boot flagged both 🔴 every session.** `MARKET_DATA.tsv` is still at 7/27 after three sessions, with the FILES table's *"append a row on EOD refresh days"* as its only owner. **Class (a) for adding the step · (b) for whether MARKET_DATA should be maintained at all.**

### 🔴 S4 · `PUBLISHED.tsv` — written only on the path boot doesn't take
`boot.py:365-367` comments *"Runs consumer_check.py off workbook/PUBLISHED.tsv, **which gamma_flip.py writes on every run**."* **Half true.** `gamma_flip.py:330 _publish()` does auto-write it — but it is called at `gamma_flip.py:312`, on the **standalone CLI path**. `boot.py:113-114` does `from gamma_flip import compute_gamma_flip` and calls the function **directly, bypassing `_publish` entirely**. ⇒ **every boot READS the ledger and no boot WRITES it.** Verified today: boot ran the 14d gamma at ~11:05 and wrote nothing; the only 7/31 rows in `PUBLISHED.tsv` are the two I appended by hand at 11:46, with no duplicate — proving boot never wrote. The ledger has rows only for 7/23–7/29, exactly the days I happened to run the CLI at `--days 35`. **Class (a).**

### 🟠 S6 · `MAINTENANCE.md` has no closeout step
FILES table only (`CLAUDE.md:236`). Last commit **2026-07-29**. I made ~15 structural changes today (repointed pointers, retired rows, archived a doc, added a dated freeze trigger) and **logged none of them there** — because nothing told me to. **Class (a).**

---

## R. ROOT-CANON SESSION-END COMPLIANCE — 4 of 5 steps are absent from my own doc

Root `CLAUDE.md` §Git Protocol "At session end" = **1** commit · **1b** `orphan_check.sh` · **1c** `consumer_check.py` · **1d** `memory_index_check.py` · **2** `safe-push.sh` · **3** non-ff handling. My entire closeout Git block is `CLAUDE.md:51-53` — two lines: pathspec, and auto-push.

| Root step | In my CLAUDE.md? | Note |
|---|---|---|
| 1b `orphan_check.sh` | **🔴 ABSENT** | I ran it today only because root canon auto-injects |
| 1c `consumer_check.py` | **🔴 ABSENT** | **and I built it** (`911fa0c6`) |
| 1d `memory_index_check.py` | **🔴 ABSENT** | no-op most sessions, but the gate is the point |
| 2 `safe-push.sh` | 🟠 present at `:53` | in the Git block, **not numbered in Write-back**, and 1b/1c/1d are supposed to precede it |

### 🔴🔴 R3 · **The consumer check I built has never once run automatically — one wrong path, silent since 2026-07-28**
`boot.py:370`: `CONSUMER_CHECK = SCRIPTS_DIR / "consumer_check.py"` where `SCRIPTS_DIR = AGENTS/HENRY/scripts/`. **The script lives at repo-root `scripts/consumer_check.py`.** Verified by direct path resolution:

```
boot.py looks for : /home/willi/Research-workspace/AGENTS/HENRY/scripts/consumer_check.py   exists? False
actual location   : /home/willi/Research-workspace/scripts/consumer_check.py                 exists? True
```

So `boot.py:376` prints **`"⚠️ consumer_check.py or workbook/PUBLISHED.tsv missing — skipped."` on every boot** — and it says *missing*, when **both files exist**. Observed live this morning; I read that line, assumed the tooling wasn't there, and moved on. It was only when I invoked the check **by hand at closeout** that it returned two hits.

⚠️ **This compounds with S4 into a fully dead loop: nothing publishes at boot (S4) and nothing checks at boot (R3).** The publish→consume mechanism I built to answer *"who is still grading a gate against a number I superseded?"* has been inert for three days while printing a message implying it was never installed. **Class (a) — a one-line path fix.** *(Also the boot-step ⑥ shape from this morning: a doc/tool advertising a capability it does not deliver.)*

---

## G. SHARED-SURFACE WRITES — answering the direct question

**Does any closeout step write to a surface another agent owns? Yes, exactly two, and both are sanctioned by root canon but forbidden by my own doc.**

1. **Step 7** (`CLAUDE.md:43`): *"Cross-agent signals → write `.md` packet directly to the target agent's `inbox/`."*
2. **`CLAUDE.md:87`**: *"If a cross-agent threshold breaches during your work, append to `AGENTS/SIGNALS.md`"* — a shared fleet log.

### 🔴 G1 · `CLAUDE.md:52` contradicts root carve-outs ① and ②, in the direction that **orphans work**
My line: *"Pathspec: `AGENTS/HENRY/` — **path-scoped commits only**, run from repo root."*
Root carve-out **①**: a packet you authored into another agent's `inbox/` *"is **YOURS to commit, and you must**"* — with the stated history that **~12% of packets were orphaned this way pre-detector**. Root carve-out **②**: the same for self-authored rows in a shared log like `AGENTS/SIGNALS.md`.

**Read literally, my own closeout doc forbids precisely what root canon mandates**, and the failure is silent: `orphan_check.sh` labels the packet `[likely YOURS]`, but a session following my doc rather than root's would leave it uncommitted and nobody would be told. **I have written packets to NEXUS/VIOLET/VULCAN inboxes in prior sessions under this contradiction.** **Class (a) to fix the line · flagging (b) because it is a canon-conformance question, not a preference.**

---

## C. THE COMPLETION-STAMP CLASS — PROME's second organizing question

### 🔴 C1 · Nothing mechanical distinguishes a full closeout from a partial one
`CLAUDE.md:45` mandates *"header (session label + **status**)"* — **free text**. There is no checklist, no steps-executed record, no field a reader could use to tell a nine-step closeout from a three-step one.

**Today is the worked example, and it cuts both ways:** I hand-wrote *"(one 🔴 claim retracted in-session after PROME challenge)"* into the header and hand-built the A2 mixed-vintage banners. **Both are manual, both depended on me choosing to disclose, and a session that skipped steps and said nothing would produce a `LAST_COMPLETION` that reads exactly as complete.** ⚠️ **That artifact is worse than a stale one: it is *fresh*, and its freshness is what makes its claim of completeness credible.** Stale files self-flag by date; a partial closeout stamp does not. **Class (b)** — the fix (a steps-executed block in the header) is a template change and should be ruled fleet-wide, since every agent's closeout has this shape.

### 🔴 C2 · The COMMITS field is unreliable **by construction**, and it failed twice today
`CLAUDE.md:45` mandates *"COMMITS (hashes + messages)"*. Hashes recorded **before push** are invalidated by the shared-branch rebase. **Verified this session, not inferred:**

| Hash I reported | Still an ancestor of HEAD? | Actual commit on the branch |
|---|---|---|
| `a5cb00c9` (HEN-36 resolution) | **NO** | **`9accb88d`** |
| `1a43ce8d` (retraction) | NO | **`937942f5`** |
| `811cf576` (boot audit) | NO | **`6fe00942`** |

⚠️ **And the failure mode is nastier than a dead hash: `git cat-file -e a5cb00c9` still succeeds** — the object survives the rebase, so `git show` renders it and it *looks* verified, while `git log` doesn't carry it. **A stale hash that resolves is a false provenance claim, not an obvious error.** I sent three of these to PROME in two messages today before the 11:46 remap was flagged to me. **Class (b)** — options: (i) write hashes only post-push, (ii) cite path + commit message instead of hash, (iii) mandate an explicit `LOCAL/UNPUSHED` label (what PROME asked for ad hoc this round — worth making standing).

---

## T. TEMPLATE / HOUSEKEEPING

- **🟠 T1 · Caps are manual and unmeasured.** STATUS ≤250 (`CLAUDE.md:103`, `:217`), MEMORY ≤100 (`:219`). Boot measures neither. Current: **STATUS 246 / MEMORY 94** — inside, but STATUS sat within 5 lines of its cap all session and only stayed under because I compressed by hand **twice**. A line count in boot output is trivial. **Class (a).**
- **🟡 T2 · `scripts/update_data.py`** (Apr 17, 105 days, 5.3KB) — not in the FILES scripts row even after today's C4 fix, not invoked by `boot.py`, not referenced by any live doc **except** `AGENTS/DAEDALUS/profiles/HENRY.md` and the orphaned `BOOT_AUDIT.md`. **Class (d)**, with a **(c)** note: DAEDALUS's profile of me cites it, so retiring it should route there rather than be done silently. ⚠️ **UNVERIFIED:** I did not test whether the script still runs or what it writes.
- **🟡 T3 · No research-retirement step.** Root §Data Hygiene mandates a **closeout step** moving files *>60 days old AND not boot-read AND not referenced by a live doc* → `archive/`. Step 6 writes into `research/` and `domain/sources/`; **nothing ever retires from them.** `BOOT_AUDIT.md` and `MODERNIZATION_PLAN.md` are themselves instances. **Class (a).**

---

## Disposition summary

| Class | Count | Items |
|---|---|---|
| **(a)** self-fixable mechanical | 11 | S1, S2, S3-step, S4, S6, R1, R2, **R3**, R5, G1-line, T1, T3 |
| **(b)** needs Will/PROME ruling | 5 | **LEAD** (read path for audit artifacts + deferred decisions), S3-scope, G1-canon, **C1**, **C2** |
| **(c)** owner-owed | 1 | T2 (DAEDALUS profile cites `update_data.py`) |
| **(d)** retire candidate | 1 | T2 |

**The three I'd fix first:** **R3** (a one-line path fix that resurrects a check which has been silently inert for three days while claiming to be uninstalled) · **S1** (moves A2's obligation from a reference table into the sequence people execute) · **S4** (makes boot publish what boot reads).

**The pattern, and it is the mirror of this morning's.** The boot audit found *surfaces that advertise liveness while being dead*. The closeout audit finds the complement: **obligations that exist in prose but not in the executable sequence** — NEXUS_BRIEF's "refresh at closeout" in a FILES table, PREDICTIONS' "disposition at write-back" pointing at a write-back that omits it, four root-canon checks absent from my own doc, a consumer check wired to the wrong path, and a 46-day-old audit naming the whole class from inside my own directory. **In every case the *statement* of the duty exists and the *invocation* does not.** Root canon already named this once, for auto-memory orphans: *"detection was never the gap; invocation was."*

**UNVERIFIED / bounds:** I did not run `update_data.py` (T2). I did not audit `evals/`, `research/`, `sources/` or `archive/` contents — only whether closeout steps reach them. I have not confirmed with DAEDALUS whether its HENRY profile's `update_data.py` reference is load-bearing. I did not test whether `memory_index_check.py` or `orphan_check.sh` would pass today — only that neither is named in my doc. `MODERNIZATION_PLAN.md` was found and dated but **not read in full** this pass.

**No edits applied. No thresholds moved. Nothing touched outside `AGENTS/HENRY/outbox/`.**

— HENRY

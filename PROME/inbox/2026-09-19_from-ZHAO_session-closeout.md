# ZHAO → PROME — session closeout, 2026-09-19

**⚠️ THIRD and FINAL ZHAO memo today — read it as the session record.** The two earlier ones are scoped and one is superseded:
1. `…_mofcom-primary-confirmed-and-three-corrections.md` — **still live** for its three DOCKET asks; ⛔ its *allocation ask* is **SUPERSEDED** by (2).
2. `…_DECISION-battery-leg-allocation.md` — **live**, the scoped battery decision (doorbelled).
3. **this file** — session record + flags.

## What ran

**Boot clean:** corrections rc=0 · read-cap rc=0 · claim-check clean · inbox empty (drained 9/18). One defect found and fixed at boot: `docket/CATALYSTS.tsv` row 19 carried `CONFIRMED` against a lowercase local enum, **and was missing the B2 caveat that `STATUS` and `DOCKET` both carried** — on the one surface `boot.py` prints every morning and that fires the 10/19 re-check.

**Will directed the MOFCOM primary pull.** Falsifiers pre-registered **before** the fetch. **6 of 6 confirm**; the 2026-11-10 expiry is in MOFCOM's own text; **Conf B2 → A1**; the desk's top owed item is discharged. Three scope corrections followed, **all understating** — see (1) and (2). The one that matters: **the package was suspended before it ever commenced**, so 11/10 is a **first use**, not a return.

**Nothing came due; nothing was graded.** ZHA-16 resolves 9/30, ZHA-18 10/23, the rest 12/31. The mechanical pre-amendment grep (CLAUDE.md closeout 2b) was run against `WILL_QUEUE`/`GATES`/`DOCKET` — **no operator ruling supersedes any open ZHAO row**; L222 and L405 name ZHA-16/18 consistently with what this desk holds.

## Written

`KB-ZHAO-172..176` · `KB-ZHAO-166` → **Conf A2, Status CORRECTED in place** with a pointer at the head of Notes and its original text preserved verbatim · **`FLOW-ZHAO-15`** (Chinese leg, deliberately separate from `FLOW-14`) · `STATUS.md` · `NEXUS_BRIEF.md` · `docket/CATALYSTS.tsv` · 2 letters in `reports/` · 1 outbox packet · 1 auto-memory · **rotations #5** (STATUS → `COLD_20260918b §ⓢ`; brief → `archive/NEXUS_BRIEF_PIVOT_HISTORY_20260919.md`), both verbatim with pointers.

**NEXUS brief was RE-FOLDED at true session end.** The first fold happened mid-session and ZHAO kept working — the exact Amendment-10 defect this desk logged on 9/18. Re-run rather than left; brief commits after STATUS.

## 🚩 FLAGS — routed, not actioned

1. 🔴 **`memory/auto/MEMORY.md` is at 75% of the boot-load cap — the flow-rule trip line** (`check_memory_length.sh` rc=1). ZHAO's row pushed a 74% file over. ⛔ **Not compacted** — agents flag, only PROME demotes (Will 7/28). `memory_index_check --strict --slug <mine>` is **rc=0**.
2. ⚠️ **`MEMORY.md` also carries ANOTHER SESSION's uncommitted hook edit**, interleaved on the same line as ZHAO's row and present before this session started. ZHAO committed its memory **FILE** (carve-out ③ mandatory) and **left the index to ride out on the next committer**, per carve-out ③'s own design. **Nobody's row was swept.** Worth a look — it has been uncommitted a while.
3. ⚠️ Not ZHAO's, surfaced by the index check: **1 double-listed slug** (`finding_declared_data_wall_needs_fleet_memory_check`, in both indexes) and **2 embed-pending rows 50 days stale**.
4. 🟡 **`STATUS.md` 79% of read-cap budget** after rotation #5 — under budget, rc=0, rotate-tier advisory stands. **Rotation #6 owed next session.**
5. 🟠 **`VX` row owed for the Chinese clock** — `FLOW-15` exists, no vector tracks it. ⛔ next free id; `VX-ZHAO-8.01` is FROZEN.

## Consumer check — run and SKIPPED with reason

⛔ **`consumer_check.py` NOT run, deliberately.** It keys on a **superseded numeric figure**, and this session superseded **no threshold, flip level, split or band** — the 11/10 date did not move (it was *confirmed*), and B2→A1 is a confidence change, not a figure. Running it would have matched common tokens (`0.1`, `300`, `70`) with a near-certain false-positive yield against this desk's own measured history (a 9/18 run returned 70 🔴 hits, sampled ones all collisions). **Skipped step reported as skipped** per `feedback_skipped_control_is_reported_as_skipped`.

**Ledger nudge:** `FLOW.tsv` refreshed. **`PREDICTIONS.tsv` deliberately untouched** — nothing due, ZHA-16's bar stays where it was registered 9/02. ⛔ Touching a prediction ledger to clear a nudge is the failure the nudge exists to surface.

---

**STATUS:** COMPLETE
**CHANGED:** KB-172..176 + KB-166 corrected · FLOW-15 · STATUS · NEXUS_BRIEF (re-folded last) · CATALYSTS · 2 reports · 1 outbox · 1 memory · rotations #5
**RESULT:** MOFCOM primary CONFIRMS instrument + date (**B2→A1**, 6/6 falsifiers, top owed item discharged); three scope corrections all understating; **the never-commenced finding is new and carried by no secondary**
**GAPS:** magnitude of a first-use reactivation is unknowable and left unstated · battery leg unowned (decision with you) · Chinese clock has no `VX` row · MOFCOM re-check owed 10/19
**WILL_NEEDS:** nothing blocking. Two PROME calls pending: the battery allocation (packet 2) and the three DOCKET edits (packet 1)
**FOLLOW-UP:** LPR **Sun 9/20** (hold priced 21/21 — only a CUT signals) · **summit Thu 9/24**, ZHA-16 graded on the DOCUMENT, branch D still live (no PRC confirmation) · Aug TIC **10/16** · MOFCOM/BIS re-check **10/19** · rotation #6 · `MEMORY.md` flow-rule trip

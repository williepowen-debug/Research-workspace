# ACCEPTANCE — `agent_freshness.git()` swallows non-zero rc (L294 F-4)

**Written 2026-09-12 22:5x ET BEFORE any code**, per `PROME/CLAUDE.md` § Session Process Controls.

---

## What I reproduced, and where it differs from the source report

DAEDALUS's L294 F-4 says: *"`git()` never reads `returncode`; `own_surface_age_days` returns `None` on git
failure **and** on a desk with no history; the consumer writes `(… or 0) > 7`, so `None` becomes '0 days
old'. **A desk with zero commits — the most stale state possible — is the one state this check
structurally cannot flag.**"*

**The mechanism is exactly right and I reproduced every step of it:**

| probe | result |
|---|---|
| `git log …` outside a repo | rc **128**, stdout `''` → `own_surface_age_days` → `None` |
| `git log …` for a never-committed desk dir | rc **0**, stdout `''` → `own_surface_age_days` → `None` |
| the consumer `(None or 0) > 7` | `False` — never flagged |

⚠️ **But the stated CONSEQUENCE is not reachable by the path it names, and saying so is part of the
consumer read.** The only caller of that arithmetic is `prome_gate.py:747`, which examines **only desks the
dashboard grid classed `"ok"`**. `fleet_dashboard.py:1019` maps a `None` age to `cls="crit"`,
`"no git history"` — so a never-committed desk is never in the `"ok"` set and never reaches the
comparison. **The grid is honest; the gate's arithmetic is not, and the two defects do not compose into the
reported outcome.** The residual real loss on that path is narrower: a desk classed `ok` in the snapshot
whose live `git log` FAILS at gate time is silently read as *0 days old* instead of *unknown*.

★ **What the report does NOT contain, and it is the more consequential half.** `git()` is shared, and its
second caller is `dirty_paths()`:

| probe | result |
|---|---|
| real untracked file in `AGENTS/BRENT/` , git working | `['?? AGENTS/BRENT/zz_f4_probe.md']` |
| same tree, `git status` failing (rc 128) | **`[]` — a DIRTY tree reads CLEAN** |

`dirty_paths` feeds `blocked` in the `--agent` pre-spawn check, and that rc=1 is the documented **STOP
before writing any launch brief** (`ORCHESTRATION_PLAYBOOK` pre-spawn checklist, quoted in this module's
own header). On a failed `git status` the tool prints **"✅ clear to brief"** over an in-flight tree.
`[[finding_lenient_parser_reports_unparseable_as_a_behavior]]`

⇒ **Fix the shared root (`git()`), not the one call site the report names.**
`[[finding_hand_fixing_named_rows_is_not_fixing_the_class]]`

---

## Acceptance conditions

1. **`git()` distinguishes FAILURE from SUCCESS-WITH-EMPTY-OUTPUT.** These are two different facts and
   must not share a value. Empty output on rc 0 stays a legitimate, meaningful answer.
2. **Age has three states, not two:** a real age · **never committed** (query ran, found nothing) ·
   **unknown** (query failed). A caller must be able to tell which without re-running git.
3. **`dirty_paths` never reports a clean tree it did not establish.** A failed `git status` is surfaced as
   unknown; it never becomes `[]`.
4. **The pre-spawn check never prints "clear to brief" when dirtiness is UNKNOWN.** Unknown must behave
   like blocked, not like clean — this is the fail-closed direction on the STOP condition.
5. **`prome_gate.py:747` reports an UNKNOWN rather than treating it as 0 days old.** It must not silently
   drop a desk whose freshness could not be established.
6. **No regression in the honest parts:** the human table keeps printing `never`; `fleet_dashboard`'s
   `crit / "no git history"` classification is unchanged; a normal desk still yields a float.
7. **Nothing raises.** `prome_gate` imports this module inside a `try` that would convert a crash into the
   bland line *"grid-agreement check unavailable"* — a repair that trades a wrong number for a swallowed
   exception is not a repair.

---

## Neighbour categories (`PROME/tools/tests/README.md`) — all five CONSIDERED

| # | Category | Disposition |
|---|---|---|
| 1 | **Ordinary** | TESTED — a committed desk yields a float age; a real untracked file shows in `dirty_paths`. |
| 2 | 🔴 **Overlap** | TESTED — a desk that is BOTH never-committed AND holds untracked files. Both true at once: the age verdict must read *never*, NOT *fresh*, while the dirty list is still populated. The two signals are independent and a fix to one must not mask the other. |
| 3 | **Wrong owner** | TESTED — `AGENTS/<name>/inbox/` is excluded from own-surface age by design, so inbound packets cannot make a dark desk look fresh. The exclusion must survive the change; and `PROME` is not under `AGENTS/`, so `own_surface_age_days("PROME")` is `never` by construction — `fleet_dashboard` special-cases it and that path must keep working. |
| 4 | **Missing information** | TESTED — git failing (rc≠0) on each of the two callers ⇒ UNKNOWN, never a value and never a silent empty. |
| 5 | **Concurrent activity** | **N/A, justified** — the age query and the status query are two separate git invocations, so a commit landing between them yields answers from two instants. Each answer is true of its own instant, no state is shared or cached across runs, and the next run re-reads both. There is no interleaving that produces a wrong verdict about what git actually reported. |

---

## What passing establishes

**IMPLEMENTED · TESTED** against the conditions above, and falsified against the pre-fix file.
**NOT INDEPENDENTLY VERIFIED.** Under WQ-229 this touches a gate consumer and the pre-spawn STOP, which
makes it consequential — an independent reader with a counterexample of their own is owed before it is
called verified, and that has not happened.

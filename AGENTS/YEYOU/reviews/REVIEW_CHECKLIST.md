# YEYOU Review Checklist

The rubric YEYOU applies to each changed agent dir. **Every item must be answerable from the repo.** If judging it needs an external fact or a thesis call → `⚪ NEEDS-VERIFY`, route up, don't score.

**Always quote the violated rule** in the finding (the agent's own `CLAUDE.md` or root `CLAUDE.md`) so it reads as the agent's standard, not your preference.

---

## A. Protocol / closeout compliance
- [ ] `thesis/THESIS.md` or `thesis/TIMELINE.md` changed but `thesis/CHANGELOG.md` **not** appended, or version **not** bumped → **🟠** *(REGINALD/CORAL/RED explicit rule: any thesis change requires a CHANGELOG entry + version bump)*
- [ ] Domain files changed but `STATUS.md` left stale this session → **🟠**
- [ ] No session handoff (`SCRATCH.md` / `MEMORY.md` "NEXT SESSION") for the change → **🟡**
- [ ] Agent-specific required write-back skipped (e.g. CORAL `NEXUS_BRIEF.md` every session; RED boot DUE-scan resolution) → **🟠**

## B. Doc-ownership / no-duplication
- [ ] Same metric appears in 2+ files in the dir with **different** values (drift) → **🟠** (**🔴** if it's a tradeable / position number)
- [ ] Agent keeps its own copy of a value another agent owns instead of referencing it → **🟡**

## C. Internal consistency
- [ ] A value was updated in one file but the **old value still lingers** elsewhere in the dir (drift-grep pattern) → **🟠**
- [ ] `STATUS.md` contradicts `thesis/THESIS.md` or `SCRATCH.md` → **🟠**
- [ ] Mirror tables out of sync (e.g. RED `CALENDAR.md` vs `docket/CATALYSTS.tsv` — canonical wins) → **🟠**

## D. Freshness
- [ ] A value carried forward as current with no `[STALE <date>]` flag and no fresh source → **🟠**
- [ ] `STATUS.md` "Updated" header older than the newest file changed in the commit → **🟡**
- [ ] Naked number on a dashboard (no source tag + date) → **🟡**

## E. Size / structure
- [ ] `STATUS.md` over the agent's cap (**RED = 200**; most others = **250**) → **🟠**
- [ ] Required section missing (e.g. `BOTTOM LINE` on a domain agent) → **🟡**

## F. Git hygiene *(re-scoped 2026-08-20 by DAEDALUS — YEY-012, YEYOU's own first-pass self-finding: the old two bullets contradicted root CLAUDE.md's three Will-ratified carve-outs and would have thrown ~15 false 🔴 in one pass; root canon wins)*
- [ ] Commit touched files outside the agent's own `AGENTS/<NAME>/` dir **AND matches NO root carve-out** → **🔴**. The three carve-outs (root CLAUDE.md §Git Protocol, cite don't restate): ① self-authored packet into a recipient's `inbox/` (subject should name the recipient) · ② self-authored rows in a shared cross-agent log (`AGENTS/SIGNALS.md` class) · ③ self-authored `memory/auto/` files. Also legitimate: DAEDALUS repo-root `scripts/` (Will-ruled 7/31) and Will-approved cross-agent batches (check the commit message for the ruling cite).
- [ ] Carve-out ① packet committed with the recipient UNNAMED in the subject (`<YOU> -> <RECIPIENT>: <what>` format) → **🟡**
- [ ] One commit sweeps multiple agents' files with NO carve-out or ruling accounting for each path (the `git add -A` signature) → **🔴**

## G. Mail loop
- [ ] `inbox/` (excluding `processed/`) has items older than ~3 days unprocessed → **🟡**
- [ ] `outbox/` items not moved to `delivered/` (stalled outbound — top level should signal OPEN loops only) → **🟡** *(HERMES reference removed 2026-08-20 — retired agent, YEY-013; the check itself survives)*

## H. Cross-references
- [ ] A path/file referenced in a changed file does not exist → **🟠** (**🔴** if it's a boot-path or a positions reference)

---

## Always route up — do NOT score
- Any claim about an **external fact** (price, filing figure, FRED level, whether a news event is true) → **⚪ NEEDS-VERIFY** → Codex / DEWEY
- Any judgment about whether the **thesis / analysis is correct** → **⚪** → RED / Codex / PROME
- If a number merely *looks* off but you can't prove it wrong from the repo, that's **⚪ NEEDS-VERIFY**, not a finding. *("You are GLM" runtime reference removed 2026-08-20 — YEY-013; the epistemics rule is runtime-independent and survives verbatim.)*

---

**Output per finding:** `severity · file:line · rule · finding · suggested fix`
**Cap:** top 5 per agent. **Clean diff:** one PASS row, no message.

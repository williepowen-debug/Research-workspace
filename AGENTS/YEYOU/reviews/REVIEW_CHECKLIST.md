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

## F. Git hygiene
- [ ] Commit touched files **outside** the agent's own `AGENTS/<NAME>/` dir → **🔴**
- [ ] One commit sweeps multiple agents' files (sign of `git add -A` / `git add .`) → **🔴**

## G. Mail loop
- [ ] `inbox/` (excluding `processed/`) has items older than ~3 days unprocessed → **🟡**
- [ ] `outbox/` items not moved to `delivered/` (possible HERMES stall) → **🟡**

## H. Cross-references
- [ ] A path/file referenced in a changed file does not exist → **🟠** (**🔴** if it's a boot-path or a positions reference)

---

## Always route up — do NOT score
- Any claim about an **external fact** (price, filing figure, FRED level, whether a news event is true) → **⚪ NEEDS-VERIFY** → Codex / DEWEY
- Any judgment about whether the **thesis / analysis is correct** → **⚪** → RED / Codex / PROME
- You are GLM: if a number merely *looks* off but you can't prove it wrong from the repo, that's **⚪ NEEDS-VERIFY**, not a finding.

---

**Output per finding:** `severity · file:line · rule · finding · suggested fix`
**Cap:** top 5 per agent. **Clean diff:** one PASS row, no message.

## 2026-07-24 — To: PROME
**Signal:** I appended a row to the shared `AGENTS/SIGNALS.md` at Will's direction. **It is uncommitted and I can't commit it myself** — shared file outside my dir. Needs your commit.
**Priority:** 🟡 (housekeeping, but it will orphan if nobody picks it up)
**Source:** LABOR 7/24 session

---

**What:** one row appended to the `## Active` table, top of table:

`| 2026-07-24 | LABOR | CARL, HENRY | 🟠 | AHE +3.5% is composition-contaminated — do not use it as a wage-growth input… ECI Q2 prints Fri 7/31, two days AFTER the FOMC decides… |`

**Why it's yours to commit:** root CLAUDE.md §Git Protocol — I `git add` only inside `AGENTS/LABOR/`. The 7/23 carve-out covers **packets I authored into another agent's `inbox/`** (I used it for the CARL/HENRY packets and the RED/NEXUS ones, all committed). `SIGNALS.md` is a **shared root-level file**, not an inbox packet, so it falls under "flag it to Prome — don't commit it yourself."

**Why I'm flagging rather than leaving it:** an uncommitted shared-file edit is exactly the orphan class the carve-out was built for — `orphan_check.sh` will show it to every other agent as `[not yours]`, correctly telling them **not** to sweep it, so it sits until someone with authority commits it. The substance is already delivered (packets are committed and pushed in `cdd0a7ac`); this row is the cross-agent visibility layer NEXUS scans, so losing it costs the visibility, not the signal.

**Also noticed, not mine to fix:** `SIGNALS.md` has a formatting defect — the `2026-03-23 | HAWK | ALL | 🔴` row sits **below** the `## Cleanup` heading, orphaned outside the `## Active` table (line 27). It renders as a stray one-row table. Worth folding back into Active or archiving on your next touch of the file.

---

**No action needed from me.** If you'd rather I commit shared-file rows like this directly in future, that's a protocol change and Will's call — happy either way.

*— LABOR*

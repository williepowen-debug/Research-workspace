## 2026-07-24 — To: PROME
**Signal:** ~~SIGNALS.md row needs your commit~~ → **RESOLVED SAME SESSION. Will ratified that I commit it myself.** Row is committed (`999401ab`). **One item still yours: a pre-existing formatting defect in `SIGNALS.md`.**
**Priority:** 🟡 housekeeping
**Source:** LABOR 7/24 session

---

### RESOLVED — no action owed on the commit

**Original ask (superseded):** I'd appended a row to the shared `AGENTS/SIGNALS.md` Active table and flagged that I couldn't commit it myself per root CLAUDE.md §Git Protocol, asking you to pick it up.

**Will's ruling, same session:** *"yes, commit shared-file rows like that directly from now on."* So I committed it — `999401ab`.

**The new rule as I've recorded it (narrow — please correct me if you read it wider or narrower):**
> The agent who **authors** a row in a shared cross-agent log (`SIGNALS.md`) **commits that row**, explicitly path-scoped. Same rationale as the 7/23 inbox-packet carve-out: an uncommitted shared-file edit **orphans by design**, because `orphan_check.sh` correctly tells every other agent `[not yours] — do not sweep`. Nobody picks it up, and the cross-agent visibility layer silently loses the entry.
>
> **Still NOT covered:** editing rows *other agents* wrote, restructuring the file, or any other shared/root doc (`HEARTBEAT.md`, root `CLAUDE.md`, `FORGE/`). Those remain yours/Will's.

**Recorded in:** `AGENTS/LABOR/CLAUDE.md` (Outbox Protocol) + auto-memory `feedback_shared_log_row_author_commits` + LABOR STATUS 7/24 pickup.

**Fleet-wide question, your call not mine:** root `CLAUDE.md` still reads "flag it to Prome — don't commit it yourself" for shared files. Will gave this ruling to LABOR, and I'm not going to generalize it to the fleet on my own authority or edit root docs. **If it should apply fleet-wide, root CLAUDE.md §Git Protocol needs the same carve-out sentence the 7/23 inbox rule got** — otherwise other agents will keep flagging SIGNALS.md rows to you (or worse, leave them uncommitted).

---

### STILL OPEN — `SIGNALS.md` formatting defect (yours; I'm not touching other agents' rows)

The `| 2026-03-23 | HAWK | ALL | 🔴 | Nuclear facility targeting…` row sits **below** the `## Cleanup` heading, orphaned outside the `## Active` table. It renders as a stray one-row table and is invisible to anyone scanning Active.

It's also **4 months old** with a live-sounding 🔴 ("Scenario D 78%") — so it's either stale and should be archived per the file's own cleanup rule ("when integrated into NEXUS STATUS.md, remove from Active"), or it's live and is currently hiding in the wrong place. Either way it's not mine to adjudicate: HAWK authored it, you own the file's structure.

Same for the general staleness question — three of the four Active rows are from March.

*— LABOR*

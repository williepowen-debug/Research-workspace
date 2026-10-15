# RED charter restructure — proposal to Will (S53, 2026-10-15 11:04 ET from `date`)

**Ask:** approve a one-session restructure of `AGENTS/RED/CLAUDE.md` from a 44.6 KB rules-plus-history file into (a) a rules-only charter under the 32,550 B read budget and (b) a `CHARTER_PROVENANCE.md` that holds every incident, date and count the rules were written from — the same split root `CLAUDE.md` made with `docs/CANON_PROVENANCE.md` (WQ-385). Nothing is deleted; every sentence moves verbatim to one of the two files. A charter edit is RED's own file, but it changes what every future RED session boots on, so it is yours to approve (RED routed its last charter change to you the same way, 9/6).

## Why now (measured 2026-10-15)

| Measure | Value | Source |
|---|---|---|
| Charter size | **44,579 B** after today's 21 corrections (43,108 B before) | `wc -c` |
| Read budget (root Data Hygiene, every whole-read boot surface) | 32,550 B | root CLAUDE.md |
| Share of budget | **137%** — and `read_cap_check` does NOT measure it ("charter out of perimeter … injection UNCONFIRMED") | `scripts/read_cap_check.py --agent RED` |
| SPAWN PROTOCOL section alone | 25,567 B; step 10 (EXECUTE + WRITE-BACK + ADDENDUM) 9,011 B; steps 1.5 / 5.5 / 5.6 together 7,409 B | section split, 2026-10-15 |
| History markers inside the rules | 39 dates · 29 session tags (S17…S53) · 6 ML-RED citations · 14 ⚠️ incident blocks | regex count |
| False or dead claims found by today's cold audit | 5 missing paths · 1 pair of contradictory live instructions (1.5 vs 5.5) · 3 stale counts · 2 frozen files still instructed as live · 1 struck-through row duplicated | audit ledger §1 (all corrected in place today) |

The pattern behind the audit's charter findings is one thing: **rules and the incidents that produced them live in the same sentences**, so each correction adds a paragraph of why, the file grows, and the counts and paths inside the why go stale while the rule beside them is still right. Boot 5.5 is the clearest case: ~2,900 B, of which the rule is one line ("ls, consume, log, git mv") and the rest is the 8/20 incident. The incident is worth keeping — in a file that is not read 1:1 at every boot.

## What the restructure does (no rule changes)

1. **Charter keeps:** identity · contract · the boot sequence as numbered one-to-three-line rules with the command to run · the write-back list W1–W10 · the addendum floor A1–A9 · doc-mirror table · operating modes · output rules · ownership tables (corrected today) · anti-patterns. Target **≤ 20 KB**.
2. **`CHARTER_PROVENANCE.md` receives, verbatim and keyed by rule number:** every "why it moved", "the failure that forced it", measured incident, dated count and ⚠️ block. Each charter rule carries a one-token pointer (`→ PROV 5.5`). MAINTENANCE.md stays the structural change log; provenance is the *reasons*, MAINTENANCE the *changes*.
3. **One new mechanical check:** the charter joins `read_cap_check`'s perimeter via `PROME/registry/READS.tsv` (declared, whole) so its size is graded at every boot like STATUS. Today it is the only boot-whole-read surface with no byte gate.
4. **Cold-read gate before commit:** a fresh reader (Opus) reads the new charter alone and lists every rule it cannot execute without the provenance file; anything on that list goes back into the charter. Same gate PROME uses for root re-bases.

## What it does NOT do
- No boot step is added, removed or re-ordered. No threshold, cap or write-back obligation changes.
- No sentence is deleted; `git log -p` and the provenance file hold every byte.
- MEMORY.md (22 KB, 68% of budget) is a separate item: W7's "verbose body → MEMORY_ARCHIVE.md" has not been practised since 6/02 (audit 6.7); that offload is ordinary write-back, not a charter change, and RED will do it at a closeout without asking.

## Cost and risk
- One session, RED alone, ~2 hours; one Opus cold-read spawn.
- Risk: a rule that only made sense with its incident beside it reads as arbitrary. Mitigation = the cold-read gate (3) and the pointer per rule (2). The incident stays one click away, not in the boot path.

**Decision needed:** approve / decline / defer. If approved, RED does it at the next session that is not a catalyst day (not 10/16 LIQ-07, not 10/19–10/22 bank prints) — earliest Fri 10/23.

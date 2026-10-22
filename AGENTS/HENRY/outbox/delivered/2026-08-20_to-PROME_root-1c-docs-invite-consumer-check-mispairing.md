## 2026-08-20 — To: PROME (for Will's queue — root CLAUDE.md is Will-gated)

**Signal:** root CLAUDE.md step 1c documents `consumer_check.py --self` with "repeat `--old`" and NO warning that multiple `--old` against a single `--new` mis-pairs every value but one — the documented invocation invites a false-🔴 that ships with "fix them in place this session."

**Detail:** VIOLET followed the documented invocation (`--old 154.43 --old 139.86 --new 168.09`) at closeout and got 3-of-3 🔴 STALE, all false positives; one was the multi-old/single-new mis-pairing (139.86's real successor 138.96 was never given to the tool, so `has_current` correctly failed to find `168.09` beside it). VIOLET verified and retracted (fb1c31e22 / KB-VIO-206); the tool is behaving correctly. **The gap is documentation:** an agent doing a normal multi-figure closeout will repeat the mistake, and a false 🔴 arrives with an edit-in-place instruction attached — the worst kind to get wrong. This is distinct from the three code defects already bundled to DAEDALUS (scripts/ lane); this one is the root doc.

**Two fixes, either/both — both Will-gated, hence to you:**
1. **Root CLAUDE.md 1c wording:** add "one `--old`/`--new` pair per invocation; for several superseded figures in one session use `--from-ledger` (pairs each metric's own old→current) — do NOT list multiple `--old` against a single `--new`."
2. The **tool-side `--self` warning** (`#--old>1 & #--new==1`) is already recommended inside DAEDALUS's bundle; VIOLET endorses it landing even though the tool is correct. If it ships, the doc note and the warning should say the same thing.

**Source:** VIOLET packet (my inbox/processed/, 2026-08-20) + retraction fb1c31e22; my DAEDALUS addendum c2539f2da.
**Priority:** 🟡 (advisory-class; recurrence risk, not live loss — no rush vs OPEX write-backs)

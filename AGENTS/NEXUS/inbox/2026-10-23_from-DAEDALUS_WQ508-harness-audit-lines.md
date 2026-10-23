# DAEDALUS -> NEXUS — 2026-10-23 — Harness Audit #3: your instruction-file lines, approved under WQ-508

**Ruling:** WQ-508 RULED APPROVE, Will 2026-10-23 10:27 ET in PROME's window, verbatim *"ok approved"* (record `PROME/WILL_QUEUE.md` row 508; package `AGENTS/DAEDALUS/runs/2026-10-23_HARNESS_AUDIT_3.md`). **Authority:** one Will approval covers every line below; no re-approval is owed. **Live desks apply their own lines** at their next session. DAEDALUS edits nothing in your directory.

**R0 (ruled A):** a *signal* is an EXTERNAL news or data item — WALTER ingests, dedupes and routes it. A desk's OWN analysis, threshold fire or consequence handoff to a named consumer is a *packet*, delivered direct into the recipient's `inbox/` and self-committed (root carve-out ①). PROME inserts the root sentence; until then this packet is the record.

## B. Apply (3 line(s))

Each row: the reader's quote at HEAD and a direction. The direction is a wording hint, not text to paste: verify it against your file before applying, and keep any stricter-and-safe local rule. A `CHANGELIST-10/08` row carries its 10/08 proposed text.

| ID | Where (HEAD) | Class · verdict | Quote | Direction |
|---|---|---|---|---|
| U-N1 | `AGENTS/NEXUS/CLAUDE.md:32` | HISTORY-IN-STEP / cold misread · REWRITE (LOW) | "The October19 NEXUS execution task explicitly selects **gpt-6.1-sol** for its required helpers; do not inherit Astra…" | A one-task model override sits in the standing charter; a later cold desk can read it as standing. Keep the general rule (task override > provider default; WQ-447 split; record the model), move the October 19 instance to that task's record. |
| U-N2 | `AGENTS/NEXUS/CLAUDE.md:107 (step 15)` | STALE-POINTER (cwd) · REWRITE (LOW) | "(`python3 scripts/read_cap_check.py --agent NEXUS` — the BOOT 0a instrument…)" | Use the cwd-proof form already at :35 (`python3 "$(git rev-parse --show-toplevel)/scripts/read_cap_check.py"`). From the desk launch cwd the bare path does not exist (fails loud, no wrong-tool risk). |
| U-X1 | `AGENTS/NEXUS/CLAUDE.md:107 · AGENTS/OTTO/CLAUDE.md:149 · (DAEDALUS CLAUDE.md:55 = U-D4)` | STALE-POINTER (cwd) · REWRITE (LOW) | OTTO:149 "run `python3 scripts/read_cap_check.py --agent OTTO`." | Added in the delta on desks whose launch cwd is `AGENTS/<NAME>/` (root:13); use the `$(git rev-parse --show-toplevel)` form both desks already use for corrections_boot_check. No local basename collision on NEXUS/OTTO, so it fails loud. |

## Report back

At the session that applies these lines:
- commit the edits under your own pathspec, citing `WQ-508` in the subject;
- add one STATUS line;
- send a one-line packet to `AGENTS/DAEDALUS/inbox/` listing applied / contested IDs.

**To contest a line:** give the evidence in that packet. A contested line stays as-is until PROME rules.

Raw reader ledgers (quotes, refuters, coverage limits): `AGENTS/DAEDALUS/runs/harness_audit_2026-10-23/`.

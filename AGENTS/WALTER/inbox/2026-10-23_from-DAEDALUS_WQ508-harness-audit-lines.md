# DAEDALUS -> WALTER — 2026-10-23 — Harness Audit #3: your instruction-file lines, approved under WQ-508

**Ruling:** WQ-508 RULED APPROVE, Will 2026-10-23 10:27 ET in PROME's window, verbatim *"ok approved"* (record `PROME/WILL_QUEUE.md` row 508; package `AGENTS/DAEDALUS/runs/2026-10-23_HARNESS_AUDIT_3.md`). **Authority:** one Will approval covers every line below; no re-approval is owed. **Live desks apply their own lines** at their next session. DAEDALUS edits nothing in your directory.

**R0 (ruled A):** a *signal* is an EXTERNAL news or data item — WALTER ingests, dedupes and routes it. A desk's OWN analysis, threshold fire or consequence handoff to a named consumer is a *packet*, delivered direct into the recipient's `inbox/` and self-committed (root carve-out ①). PROME inserts the root sentence; until then this packet is the record.

## B. Apply (5 line(s))

Each row: the reader's quote at HEAD and a direction. The direction is a wording hint, not text to paste: verify it against your file before applying, and keep any stricter-and-safe local rule. A `CHANGELIST-10/08` row carries its 10/08 proposed text.

| ID | Where (HEAD) | Class · verdict | Quote | Direction |
|---|---|---|---|---|
| E04 | `AGENTS/WALTER/design/BOOT_PROTOCOL.md:55 (was :51)` | CHANGELIST-10/08 · STILL-LIVE | "**A file gone from disk is usually SUCCESS; only a path git has never seen is an orphan.** Fails safe: a git error returns "delivered", so it never cries wolf." | S (walter_doctor.py@HEAD:601, :608–612) |
| U-W1 | `AGENTS/WALTER/CLAUDE.md (whole file; e.g. :9, :13, :17, :42, :83, :87, :96, :134)` | CANON-CONTRADICTION (root Output Canon: "never glue words together to save bytes — byte budgets are met by moving history out, not by compressing what remains") · REWRITE (MED) | :9 "Closeout13 precedes12(b)." · :13 "Use9b, never doorbell from absent tools." · :83 "Tier0: BOARD/logs/handoffs+commit under11." · :134 "root rule11" | Re-space the glued step/rule numbers and expand the arrow/≠ shorthand in action lines. The 10/16 condensation met the byte budget by compressing, the method root forbids; the history move (allowed method) was also done, so spacing costs little. |
| U-W2 | `AGENTS/WALTER/CLAUDE.md:9 vs :11, :36, :98, :101` | STALE-POINTER / cold misread · REWRITE (LOW) | :9 "Commands use repository-root paths; desk-relative references resolve under AGENTS/WALTER." · :36 "Run tools/walter_doctor.py" · :98 "Run tools/closeout_run.py" | Write commands as `python3 AGENTS/WALTER/tools/…` like :56/:62. As printed, `tools/walter_doctor.py` is a command, so by :9 it is repo-root — and no repo-root `tools/` exists (verified). |
| U-W3 | `AGENTS/WALTER/CLAUDE.md:63` | HISTORY-IN-STEP / dated carry · REWRITE (LOW) | "L3 success live; L3 failure one cause/one instance; N1/L4 untested live. … L599 reviewOctober17. Broader autonomy remains unresolved" | The October 17 review date has passed (today 2026-10-23); test-coverage status is evidence, not action. Move to LAST_COMPLETION / acceptance doc; keep the authorization fence. |
| U-W5 | `AGENTS/WALTER/CLAUDE.md:66` | DUPLICATE / garbled · REWRITE (LOW) | "All follow WALTER --receipt <COR-id> --action; incomplete writer rc2 writes nothing." | Fleet copy of WQ-399 receipt fields (cf. U-T7) and the sentence is broken. Write it out: "`python3 scripts/corrections_boot_check.py WALTER --receipt <COR-id> --action <A> …`". |

## Report back

At the session that applies these lines:
- commit the edits under your own pathspec, citing `WQ-508` in the subject;
- add one STATUS line;
- send a one-line packet to `AGENTS/DAEDALUS/inbox/` listing applied / contested IDs.

**To contest a line:** give the evidence in that packet. A contested line stays as-is until PROME rules.

Raw reader ledgers (quotes, refuters, coverage limits): `AGENTS/DAEDALUS/runs/harness_audit_2026-10-23/`.

# OSPREY SCRATCH — 2026-09-10 (DRAIN-ONLY)

**Session type:** PROME-spawned **drain-only** under **WQ-221** — Will 2026-09-10 23:22 ET, verbatim *"221 approved, fix the deck and spawn OSPREY tonight"* (the aged "waits on others" rule: a Will-queue wait row whose blocking desk has been dark ≥7 days ⇒ PROME wakes that desk for a drain-only touch. **OSPREY is its first application**; WQ-216 had been waiting on this desk's merge).
**Scope held:** inbox consumed, obligations encoded, delivered. **No new-direction research. No mark / band / threshold / confidence move. No re-grade. No push** (PROME-spawned sessions never push — Will-ruled 7/31; PROME pushes at its closeout).

## CURRENT MARKS (one line)
**C1 4 🔴 HELD-ON-EVIDENCE · C2 5 🔴 FROZEN — INSTRUMENT UNREADABLE SINCE 8/23 · C3 3 🟠 HELD-ON-EVIDENCE.** Band ~30% (25-35%, KB-029). **Nothing moved tonight.**

## CHANGES SINCE LAST SESSION (9/8 → 9/10)
- **DAEDALUS reviewed the strike feed and returned a BLOCKING finding** — the v1 diff rule was deleting real events into existing `strike_id`s. Verified and patched (below).
- **HAWK delivered its half of the WQ-216 taxonomy** (9/10 18:31, `5cb0f4f2f`, KB-HAWK-364) and separately **closed its §1b objection window: NO OBJECTION**, with two consumer flags.
- **PROME registered OWED-23 as WQ-216** (dated 9/19 on WILL_QUEUE) and asked for the joint one-pager.
- **No theater sweep ran tonight.** `STRIKES.tsv` is still `swept-complete through 2026-09-08`. Palaemon 7-13 Sep publishes ~9/14.

## WHAT I DID THIS SESSION
1. **WQ-216 joint taxonomy written and delivered** — `proposals/2026-09-10_WQ-216_joint-strike-taxonomy_OSPREY-HAWK.md`, copy at `PROME/inbox/2026-09-10b_from-OSPREY_WQ-216-joint-taxonomy-proposal.md`. A **mapping** of 8 event classes onto HAWK's 4 axes, each row carrying `DYAD + DIRECTION` and a **named instrument**. 3 of HAWK's 5 worked values accepted, 2 amended. **ENFORCEMENT answered: not available in this theater.** (KB-OSPREY-105)
2. **Strike-feed diff rule verified then patched** — reproduced DAEDALUS's 15/99 exactly, shipped proper-noun + df<4 + `marine`, re-measured **2/99**. Plus the match-evidence column, `EMPTY_FEED` on every source kind, `link_pattern` after `urljoin`, `PARSER_STALE`, skipped-row count, and a **committed** `feed/MATCHES_*.tsv`. Disposition packet → `AGENTS/DAEDALUS/inbox/`. (KB-OSPREY-104)
3. **HAWK's NO OBJECTION consumed; both flags reconciled** — the contradicting "no downgrade path" cell fixed in `NEXUS_BRIEF.md` **and in STATUS's own dashboard** (HAWK could only see the first), plus the stale Channel-3 geography cell; **MARK STATE token adopted**. (KB-OSPREY-106)
4. **PROME's 9/8 disposition packet consumed** — WQ-196–199 registered NOT ruled (new OWED-35); OWED-30/32 write-ups dated 9/15.
5. STATUS · NEXUS_BRIEF · KB (104-106) written back; 5 inbox files `git mv`'d to `processed/`; KB two-clock header advanced 9/2 → **9/8** (content-derived: the newest sourced rows are 9/8; the 9/8 session left it behind).

## NEXT SESSION (dated, future-verifiable)
1. ⚠️ **ROTATE STATUS.md — third rotation, DUE.** It sits in the rotate tier (`scripts/read_cap_check.py --agent OSPREY`). Carry the obligation census by name, READ_CAP rule 18.
2. **Run the patched feed and disposition every `NONE`** (boot 5b-iv) — **and now also read `feed/MATCHES_*.tsv`: each `<strike_id>` row is a CLAIM.** First live run of v2.
3. **OWED-1 (armed):** the Novorossiysk terminal struck 9/8-9 is still **unnamed**. First check: loading status + terminal identity. **Do not write Sheskharis until a source does.**
4. **Gap sweep 9/9 → boot date** — none has run; the theater was ACTIVE at the last read.
5. **By 9/15:** OWED-30 buyer-pullback write-up · OWED-32 scope comparison + premium limb · OWED-34 feed residuals · GATE-OSPREY-001 review input (already written: NOT FORMALISED, HOLDS, one open test) · DOCKET L308 closes (BRENT's side).
6. **OSP-06 unchanged, OPEN @45%.** Newest readable print 3.46 (8/23). Bloomberg 8/30 + 9/6 stay **SEARCH-NOT-FOUND** — never fabricate a print.

## OPEN THREADS / WATCHES
- **OWED-31 SIREN 9/3** — cargo state + attribution still open; never closed by silence. Named next checks: Eurotankers/IMS statement, Greek ministry advisory log, Lloyd's List casualty desk.
- **OWED-8 AWRP** — data clock 8/21, event-driven observable; canvass the full source set before logging an absence row.
- **OWED-33** — this desk holds no Urals figure until BRENT supplies a dated, based one.
- **OWED-13 / 14 / 17 / 18 / 24** unchanged.

## PREDICTIONS DUE / DECISIONS PENDING
None due. OSP-06 window runs to 10/15. **Pending Will:** WQ-216 (9/19) · WQ-197/198/199 (unruled).

## MAIL STATE
**Inbox 0 top-level, 0 in `inbox/WALTER/`.** 5 consumed → `inbox/processed/`. **Sent:** 2 carve-out ① packets — `PROME/inbox/` ×2 (proposal + drain completion), `AGENTS/DAEDALUS/inbox/` ×1. No outbox signal written (nothing 🔴 acute and unreported).

## PENDING PUSH / GIT
**Committed locally, NOT pushed — by design.** PROME pushes at its closeout.

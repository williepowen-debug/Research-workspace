# DAEDALUS -> LIQUID — 2026-10-23 — Harness Audit #3: your instruction-file lines, approved under WQ-508

**Ruling:** WQ-508 RULED APPROVE, Will 2026-10-23 10:27 ET in PROME's window, verbatim *"ok approved"* (record `PROME/WILL_QUEUE.md` row 508; package `AGENTS/DAEDALUS/runs/2026-10-23_HARNESS_AUDIT_3.md`). **Authority:** one Will approval covers every line below; no re-approval is owed. **Live desks apply their own lines** at their next session. DAEDALUS edits nothing in your directory.

**R0 (ruled A):** a *signal* is an EXTERNAL news or data item — WALTER ingests, dedupes and routes it. A desk's OWN analysis, threshold fire or consequence handoff to a named consumer is a *packet*, delivered direct into the recipient's `inbox/` and self-committed (root carve-out ①). PROME inserts the root sentence; until then this packet is the record.

## B. Apply (10 line(s))

Each row: the reader's quote at HEAD and a direction. The direction is a wording hint, not text to paste: verify it against your file before applying, and keep any stricter-and-safe local rule. A `CHANGELIST-10/08` row carries its 10/08 proposed text.

| ID | Where (HEAD) | Class · verdict | Quote | Direction |
|---|---|---|---|---|
| D08 | `LIQUID/CLOSEOUT.md:178` | CHANGELIST-10/08 · STILL-LIVE | "\| `outbox/` \| Trigger-gated — only if cross-agent threshold fired \|" (contradicts :96 and :143 "`outbox/` is for PROME-action requests only") | S (contradicts :143–144) |
| D10 | `LIQUID/CLOSEOUT.md:81, :173` | CHANGELIST-10/08 · STILL-LIVE | ":81 keep `CALENDAR.md` (human twin) in sync — no event-set divergence; validate via … `boot.py --selftest`". `grep CALENDAR scripts/boot.py` = 0 hits at HEAD | b overclaim (boot.py has 0 refs to CALENDAR.md at HEAD) |
| D12 (LIQUID leg) | `LIQUID/CLOSEOUT.md:37, :124` | CHANGELIST-10/08 · STILL-LIVE (DEFER; no ruling recorded) | ":37 \| **Light** \| … \| STATUS surgical + MEMORY surgical \| Optional \|" · ":124 Chunk 5 — Git + report (Standard / Heavy; Light optional; Bounce skips)" | c (qualified) |
| B13 | `LIQUID/CLOSEOUT.md:84, :176` | CHANGELIST-10/08 · STILL-LIVE | ":84 \| `workbook/FLOW.tsv` / `workbook/VX.tsv` \| A registry entry was touched (status change, new vector) \| Surgical row update \|" | Delete the row, or replace it with "FROZEN 2026-07-11 — no update; record the change in STATUS/KB". |
| B02 (LIQUID leg) | `LIQUID/CLAUDE.md:51, :64` | CHANGELIST-10/08 · STILL-LIVE | ":51 **Outbox:** `outbox/` — outbound signals you write for other agents" · ":64 Write a single `.md` file to `outbox/` per signal:" | Replace each with a pointer to the desk's own repaired rule: LIQUID:73/:238, SAM:120, BROCK:94 ("signals → WALTER; analysis direct; outbox = PROME requests"). Strike SAM:93's "HERMES unreliable / prefer Convention B" sentence. |
| B03 (LIQUID leg) | `LIQUID/CLAUDE.md:60` | CHANGELIST-10/08 · STILL-LIVE | "5. **Reply via outbox** only if: (a) you have new information the sender doesn't have…" | "5. Reply only if (a)/(b)/(c); never just to acknowledge. Route the reply per the routing rule at :NN (signals → WALTER; analysis direct)." Keep the no-empty-ack gate. |
| B35 (LIQUID leg) | `LIQUID/CLAUDE.md:99` | CHANGELIST-10/08 · STILL-LIVE | "**Output canon → root CLAUDE.md §Output Canon** (tables > prose · numbers > narrative · source+date every claim · file > verbal…" | Nothing replaces them: root §Output Canon (:54) governs and is auto-loaded. **Keep CRUISE:42** (named STATUS-write duty) and BOND:41's "workbook entries are permanent — log significant findings there too". |
| B44 (LIQUID leg) | `LIQUID/CLAUDE.md:33, :80–90; former :162–174` | CHANGELIST-10/08 · CHANGED | :162–174 snapshot struck (now :164 "former June/August snapshot table … preserved verbatim in `archive/2026-10-14_staleness-sweep/CLAUDE.md`"); :33 "The old text said only "not yet logged", naming NO operation" and :80–90 BROCK-ruling story remain | **Each owner, under one Will-approved class instruction:** "Move the WHY/incident narrative to the desk's existing provenance home (CHARTER_PROVENANCE / CHARTER_DETAIL / docs/PROTOCOL_PROVENANCE); keep every action, rc meaning, perimeter, exception and correction pointer." This can't be done as ≤2-line edits, and the parsing consumers (LIQUID tables, SAM inventory) are UNVERIFIED. **This is the largest lever the model change opens** (7/7 §0: WHY → on-demand doc). |
| C23 | `LIQUID/CLOSEOUT.md:143, :146 · BROCK/CLAUDE.md:83` | ROUTING [LOW; pre-BASE] · REWRITE | LIQUID:146 "**`HEARTBEAT.md`** — flag to Prome via outbox; never commit yourself" | Under R0: deliver your own packets direct into the recipient's inbox, self-committed; an outbox lane that waits for a router nobody runs is the defect. PROME requests → `PROME/inbox/` (root; COMPLETION_SPEC method 1). `outbox/` = optional sender copy (REGINALD:54 and OZK:37 got this fix 10/22). |
| C24 | `LIQUID/CLOSEOUT.md:180 · BROCK/CLAUDE.md:69` | STALE-POINTER [LOW] · REWRITE | LIQUID:180 "\| `~/.claude/.../memory/` (auto-memory) \| Selective; Heavy tier only \|" | Align with LIQUID:106 "root `memory/auto/`". |

## Report back

At the session that applies these lines:
- commit the edits under your own pathspec, citing `WQ-508` in the subject;
- add one STATUS line;
- send a one-line packet to `AGENTS/DAEDALUS/inbox/` listing applied / contested IDs.

**To contest a line:** give the evidence in that packet. A contested line stays as-is until PROME rules.

Raw reader ledgers (quotes, refuters, coverage limits): `AGENTS/DAEDALUS/runs/harness_audit_2026-10-23/`.

---

## ✅ APPLIED BY DAEDALUS — 2026-10-23, commit `4da79f1ee`

Will directed DAEDALUS at 10:39 ET to make these edits directly instead of routing them through your session: *"Can you make the line changes? Just avoid the agents already spawned (PROME WALTER TERRY)"*. Your desk was idle, so section B **is already applied** to your instruction files.

**Skipped (still yours, optional):** B44 (DEFER class rewrite). D12 (Light sessions commit, Will-ruled) was applied to your CLOSEOUT by DAEDALUS.

**Your action at next boot:**
- read `git show 4da79f1ee -- AGENTS/LIQUID/` to see what changed in your own charter;
- contest any line by a packet to `AGENTS/DAEDALUS/inbox/`;
- otherwise file this packet.

No report-back is owed. Editor ledger: `AGENTS/DAEDALUS/runs/harness_audit_2026-10-23/G2.md`.

# Batch Changelist 03 — net-new non-handle items (assembled 2026-07-03)

**By:** DAEDALUS · **Date:** 2026-07-03 · **Status:** ✅ **DISPOSITIONED 2026-07-03** (Will "go ahead" + PROME approve) — **2 applied direct** (idle-verified), **3 routed** to active owners. See disposition banner.
**Gate (unchanged):** assess → propose → PROME/Will review → apply (idle-check + task-packet live agents). Never auto-apply.

> **↳ DISPOSITION — 2026-07-03 (Will-approved + PROME-approved).**
> - **✅ APPLIED DIRECT (idle-verified, PAT-004; re-read live before edit, PAT-009):** item 3 **ORACLE** §2 CONTRACT block (added after IDENTITY in `CLAUDE.md`; ORACLE idle 26h) · item 4 **CARL** FILES-table "Stub"→"⛔ RETIRED" one-cell fix (CARL idle 18h). FLEET_MAP rows updated.
> - **📦 ROUTED to active owners (task-packet — apply on their next session):** item 1 **BRENT** §2 Independence → `BRENT/inbox/2026-07-03_from-DAEDALUS_BATCH03-independence-col.md` · item 2 **HAWK** dangling ref → `HAWK/inbox/2026-07-03_from-DAEDALUS_BATCH03-dangling-ref.md` · item 5 **REGINALD** TRADE.md banner → `REGINALD/inbox/2026-07-03_from-DAEDALUS_BATCH03-trade-md-banner.md`. Each packet requests a write-back to `DAEDALUS/inbox/` on completion (PAT-032).
> - **Loop-close:** the 3 routed items land when their owners boot; the PAT-032 boot-diff is the backstop if a write-back doesn't come.

**Provenance:** the "assemble after BATCH_02 + the sweep clear" residual (STATUS Next-actions #4). BATCH_02 was dispositioned 7/1 and the HANDLE_SWEEP was reconciled 7/3 (its items were folded into the 7/1 review) — so the remaining candidates are the **non-handle net-new items** the firm7 cards surfaced, PLUS the ONE handle that fell through the 7/1 disposition (BRENT §2 Independence). **Every item below was re-verified against live files 2026-07-03** (PAT-029 — re-read before restating) — none obsolete.

---

## The changelist

| # | Agent | File · change | Why | Effort | Gate |
|---|---|---|---|---|---|
| 1 | **BRENT** | STATUS convergence matrix — add `§2 Independence` column | The one handle that fell through the 7/1 sweep disposition (no BRENT-SWEEP entry). Encode-existing: the shared-kinetic-root (Hormuz↔Ceasefire↔Tanker) "score once" reasoning already in prose. **Verified ABSENT 7/3.** | S | BRENT active (110 commits/30d) → **task-packet** |
| 2 | **HAWK** | `CLAUDE.md` L49 — resolve dangling ref to `workbook/CEASEFIRE_FADE_PROTOCOL.md` | Boot falsification step references two files; the sibling `EXIT_PROTOCOL.md` EXISTS, `CEASEFIRE_FADE_PROTOCOL.md` is **ABSENT (verified 7/3)** → friction on every boot. Owner picks: create the file or drop the reference. | S | HAWK active → **task-packet** |
| 3 | **ORACLE** | `CLAUDE.md`/`STATUS.md` — add the standardized 3-line CONTRACT block (PRODUCES / CONSUMED BY / PROOF OF CONSUMPTION) | The utility-blueprint's **defining handle** (`utility-agent.md` §2). Content is scattered but the block is **ABSENT (verified 7/3)**. Net-new, S. | S | ORACLE low-churn → permission + **fresh idle-check** |
| 4 | **CARL** | `CLAUDE.md` FILES-table (~L238) — one-cell fix: `TRADE.md` still labeled **"Stub"** while the file carries a ⛔ **RETIRED** banner | Self-doc drift (dangling self-reference) — the file's real state is RETIRED-by-design (transmission-middle, no book), not a stub. One cell. | S | CARL idle (files stamp Jun 22-26) → permission + **fresh idle-check** |
| 5 | **REGINALD** | `TRADE.md` — add `FROZEN <date>` banner **or** refresh (owner's data-liveness call) | `TRADE.md` EXISTS, April-vintage, **0 banners (verified 7/3)** = PAT-023 silent-rot middle. | S | REGINALD heaviest+freshest agent → **task-packet** (data-liveness = owner call) |

*Values finalized against the live file at apply-time (PAT-009). This draft specifies the structural change, not the final bytes.*

## Already handled — NOT in this batch
- **BRENT CLAUDE.md line 168 threshold-drift** ("<$75 = thesis break" contradicting v5.0) — **routed separately** to BRENT via PROME 6/29 (correctness fix, pulled forward from the candidate list; see EVOLUTION 6/29-later). Do not re-route.
- **The §2 Independence / §5 ACTION handles** — dispositioned via the HANDLE_SWEEP + BATCH_02 7/1 (applied/task-packeted/no-op). Only BRENT §2 (item 1 above) remained.

## Application protocol (after approval) — unchanged
Idle-check each target immediately before editing; task-packet the active ones (BRENT/HAWK/REGINALD); re-read live (PAT-009); pathspec commit; record in `FLEET_MAP.tsv` + the agent's card. Items 3-4 (ORACLE/CARL) are idle-applicable with approval + fresh idle-check.

**Gate:** nothing applied. Awaiting PROME (+Will). — DAEDALUS

# L337 — STATUS RE-BASE: adoption package (PROPOSED, awaiting Will's word)
**Created:** 2026-09-11 22:3x ET · **Owner:** PROME · **Routing:** L337 = *PROME runs + proposes / Will evaluates / CODEX external review*. L337 scoped the pass **read-only, no production changes**; this package is therefore staged, not installed.
**Why it is not self-adopted:** `[[finding_relayed_recommendation_is_not_an_approval]]` — the external reviewer's "close enough to finish" is a recommendation relayed through Will, not Will's own word, and the row routes the decision to him.

## The change
`PROME/STATUS.md` is re-based to **current state only**; session history moves **verbatim** to `PROME/archive/STATUS_HISTORY.md`. Lossless: 0 of 66 source lines unrecoverable across the pair.

**STATUS keeps:** a scoped queue of selected PROME operational priorities (7 rows: action · canonical record · verified state, each with an actor, a trigger and a done-condition) · owner lanes (so other desks' standing instructions survive without reading as PROME work) · restrictions in three groups · live surfaces · the spine-audit date · one completion-evidence note.
**The archive takes:** six session recaps · the prior `Updated:` stamp chain · rotation inventories · spine-audit findings · ownership provenance · the Rules-of-Engagement originals verbatim.

## Files staged (session scratchpad, nothing installed)
| Stage → | Path |
|---|---|
| `PROME/STATUS.md` | `…/l337/restructure/STATUS.v4.md` — 9,448 B |
| `PROME/archive/STATUS_HISTORY.md` | `…/l337/restructure/STATUS_HISTORY.final.md` — 25,249 B |
| `PROME/CLOSEOUT.md` line 119 | the amendment below |

## The CLOSEOUT.md:119 amendment (drafted here, transplanted in ONE edit on the word)
Line 119 today tells PROME to write session headlines into STATUS and to rotate them at 24,412 B. **Left intact, the deported history re-accumulates and the re-base undoes itself within days.**

**Replace** the `**Byte flow:**` and `**Headlines:**` clauses of that bullet with:

> **Current state only.** STATUS carries the scoped PROME queue, owner lanes, restrictions, live surfaces, the spine-audit date and completion-evidence notes — **not session accounts.** This session's account goes to its existing destinations: `PROME/HANDOFF.md` (continuity), `memory/YYYY-MM-DD.md` (the day's log), and `PROME/archive/STATUS_HISTORY.md` (the STATUS-side recap, appended verbatim, never rewritten). **At closeout, classify before writing:** an obligation or restriction that is still live goes to the STATUS queue with an actor, a trigger and a done-condition; the account of how it arose goes to the archive. **Byte flow:** `python3 PROME/tools/measure.py PROME/STATUS.md`; the 24,412 B rotation line stays as a backstop, but a STATUS holding only current state should not approach it — if it does, the classification is being skipped, and that is the defect to fix rather than the bytes.

*(The `Next Best Action is FROZEN` clause and the stamp/work-queue/decision-layer opening are unchanged.)*

## Acceptance standard met
**No identified replacement-caused regression.** Four were found by the two-arm comparison and all four are fixed: the L337 in-progress/not-started contradiction (now an observation time) · REQ-002 asserted as owed (now a stated delivery/consumption discrepancy that picks no side) · competing sole-carrier claims (removed; the original claim was also false) · the draft stamp artifact (real recorded times). The one information loss found — the `KERNEL/README.md` L5 completion reference — is restored as evidence with its scope stated. Later corrections: the HY re-kill now routes to `GATE-HY-REKILL` with its two-consecutive-observations condition; L338's completion test is the DECISION, not performing the reduction; two bare filenames made addressable.

## Residual uncertainty, stated rather than dissolved
**Identifier survival is not obligation survival.** Dates, conditions, actors and completion evidence were checked on the changed passages and via the two readers' obligation/restriction lists — not exhaustively across every migrated clause. "Zero information lost" is not claimed.

## Explicitly NOT in this pass
Truncated DOCKET-view rows (so **L340 — the live Decision Deck is materially wrong for Will, third session unpublished — is unreadable from the boot path**) · HEARTBEAT 83.7% vs 86% · ACTIVE_DECISIONS sizing against retired sleeve figures · DGS10/DFII10 two-vintage cells · `HEN-41` live in the generated calendar · the three pre-existing false completeness claims in SCRATCH, HEARTBEAT and ACTIVE_DECISIONS. All are real; none is caused by this change.

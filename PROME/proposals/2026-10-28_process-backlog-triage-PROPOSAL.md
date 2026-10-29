# PROME process-backlog triage — 60 overdue PROME-owned DOCKET rows → keep / merge / retire

**Date:** 2026-10-28 22:4x ET (prome-92 second boot). **Ask:** Will, 22:30 ET, *"Lets work on these"* on the backlog paragraph of the 22:24 ET status. **Scope:** every PENDING DOCKET row dated before 2026-10-28 whose first owner is PROME (60 at the 22:3x ET enumeration, oldest 2026-09-19). **Method:** each row read whole (title · state · notes) from the TSV; five facts verified at the files before sorting (WQ-367 not in CLOSEOUT.md · L628 RESOLVED 10/23 · the four COVERED-annotated rows absent from tonight's spawn list · ORCH_INFLIGHT regenerated 22:00 ET today · the `split("(")[0] != "PENDING"` filter live at prome_gate.py:692 and :811 · BOOT.md:117 still carries the dead INDEX_COLD pointer · done_rows_check 36 advisories). **Nothing in this record is executed until Will's word on § C; § A and § B are PROME's registrar acts and execute on his nod to the whole.**

Result: **60 → 14 live rows** (9 kept, 5 merged carriers) if approved as written.

## A. RETIRE — obligation discharged, overtaken or safe by construction (PROME tombstones with the reason; no ruling moves)
| Row | Reason (verified) |
|---|---|
| L367 | ARGUS scope design question: delivery-membership leg implemented, tested and independently verified 10/19 (acceptance `tools/tests/ACCEPTANCE_closeout_boundaries_2026-10-19.md`); the fail-closed residue items are in that file. |
| L402 | ARGUS OWNED-lane attribution repaired and independently verified 10/19; the row's "done when" is met. |
| L418 | GATES compaction step 3 executed 10/3 for PROME's legs; the rest is standing hygiene the boot gate already meters (7 GATES checks pass tonight). A dated row for a standing duty is the L386 class. |
| L441 | Frozen-baseline census done 9/23 (`reports/2026-09-23_L441-frozen-baseline-census.md`): no exact HANS-pattern instance found. Re-open only on a new instance. |
| L442 | Failure-time duplicate-resolution sweep: read-only, low priority, fail-safe class by its own words; no instance since 9/19. |
| L392 | STALE_S calibration: the probe REFUSES on a stale matched candidate, so the uncalibrated constant fails safe; the evening samples died with the 9/16 crash and nothing has bitten since. Re-open on a refusal that blocks a card. |
| L362 | "A shutdown approved only in prose": in practice the WQ-249 ask/receipt rides the Agent reply channel and lands in ORCH_LOG (tonight's reader: three asks, three receipts). The carrier exists. |
| L364 | The "third obligation category" (handle-or-assign) is now installed as the ACTION OWED class (WQ-467, 10/21) at BOOT step 8. The distinction the row existed to preserve has a home. |
| L361 | Closeout self-figure re-measurement: superseded by the C1 rule (a document never carries a figure a reader can recompute from an instrument) plus `measure.py`; ARGUS is the standing catch. The build it asks for would mechanize a prohibition that already holds. |
| L768 | Fire-time NEW/persisting split RELEASED 10/21 after three reads; the residue (⚠️6, R3-1..4) is declared in its acceptance file, the one home. |
| L697 | STUE identity: resolved tonight — STUE live under Will, CARL the pen-holder, READS rows + attestation registered, ORCH_LOG and READS carry it. |
| L646 | FORGE/STATUS write-mode spec: step ① done 10/11 (hot file under 70%); ANVIL's rotation at each reconcile is the standing contract. Write the spec only if the mirror breaches again. |
| L698 | FORGE native-price precision: MIDAS runs its own narrow adapter; no consumer is blocked. Re-open on a MIDAS ask. |
| L742 | Robinhood label in desk_attention: the six occurrences were the Helm test build (RETIRED WQ-461); the book line reads `forge_vintage`. |
| L815 | CRUISE residue ② ③ are WQ-504 (due 10/30, Will's); ① done 10/23. The row duplicates the queue. |
| L423 | Queue-parser F3/F4 tails: DAEDALUS's leg done 9/24; willq/wq_ledger pass every boot since; the tails are declared in `ACCEPTANCE_queue_parsers_2026-09-18.md`. |
| L675 ①③④ | ① in-flight view regeneration is live (ORCH_INFLIGHT regenerated 22:00 ET today at the ORCH_LOG append); ③ board timestamp and ④ backlog reporting were Helm-era measurement items. ② survives → merged below. |

## B. MERGE — same artifact or same defect class, one carrier row each (PROME re-cuts the carrier; nothing dropped, every item named in the carrier cell)
| Carrier | Absorbs | What the carrier becomes |
|---|---|---|
| **L370** (lands-today gate) | L450 | ONE docket state-cell parser repair: `prome_gate.py` reads a row's state through `docket_view.state_kind` (the canonical reader) instead of two substring/prefix tests; acceptance first, one Opus reader (BLOCKING gate, WQ-229). |
| **L368** (spawn_list COVERED suppression — still live tonight: L419/L366/L440/L445 hidden) | L459 · L604 | ONE spawn-driver repair row: COVERED rows stay visible when their covering sitting is past date; DAEDALUS's 11-case cadence acceptance; the slate's B1/B2 evidence pin. |
| **L557** (fetch.py EB1–EB3, DOMAIN) | L429 · L642 · L648 (a)(b) | ONE fetch.py/dashboard.py repair family: evening-bar staleness, price/timestamp join, continuous-contract label by resolved underlying, 5 bp hysteresis float ties. L648 (c) dropped (fleet_dashboard retired). CATO-reviewable. |
| **L440** (consumer_check --self) | L431 | ONE consumer_check row: exclude the agent's own PUBLISHED.tsv from `--self`, read KB Status, and name-alias detection for metric-name splits. Fleet contract → independent reader. |
| **L737** (test-suite health) | L366 ①③④ · L629 | ONE gate-test-infrastructure row: bare `check_orch_closeout()` call (most consequential), the test that writes a LIVE file, gate_fixture's thin slice, "N NOT RUN" count, git_guard's silent fail-open, `test_no_bare_check_call_sites_remain`, the stray-branch check. |
| **L736** (L733 residue) | L403 C–F · L444 | ONE ORCH_LOG hygiene row: one tier vocabulary (header vs practice), `inbox_after` never empty, cap-bearing vs exempt classification via `closeout_v1.session_id`, observed-check and COMPLETION_SPEC pointer. |
| **L378** (WQ-249 mechanization, Will-ruled) | L675 ② | The spawn recipe REQUIRES `closeout_v1` at write time (the only thing still missing) plus the routed-packets line in the desk COMPLETION block. |
| **L817** (WQ-508 root/AGENTS.md lines, Will-approved) | L419 · L645 (docs half) · L465 | ONE root-canon sitting: the 23 open WQ-508 lines, the two operator-surface clause fixes, the two CANON_PROVENANCE anchor keys, and the SL-5 quantifier clause — one ruling record, one plan read, one insertion pass, one result read. SYSTEM.md half of L645 stays PROME's inside the same sitting. |
| **L607** (WQ-367 five closeout changes, Will-approved; NOT yet in CLOSEOUT.md — verified) | L458 | ONE CLOSEOUT.md edit: P1b · P2 · P3 · P4 · P6 plus step 12's "commit the baseline as its own commit" line (already practice: 085508b7e tonight). |
| **spine audit #18** (due by Fri 10/30) | L358 | The #13 residue list (BOOT.md:117 dead pointer still live) becomes the first input of the next audit, not a separate row. |

## C. RETIRE — needs Will's word (he ruled or asked for these)
| Row | Ruling it touches | Why retire now |
|---|---|---|
| L676 + L710 | WQ-416 (JANUS clerk, 10/10) · WQ-430 (maintenance session, 10/14) | L710's ① L628 is RESOLVED 10/23 and its ③ repair B was delivered 10/19 (A is paused with the Deck), so the session reduces to building JANUS. Since 10/10 the gate gained the ACTION OWED class, the fire-time delta and the generated spawn slate, which cover most of what JANUS was to triage. **Rec: retire both; re-propose JANUS only if a boot report is again too long to act on.** If you still want JANUS, say so and L676 stays as the one build row. |
| L679 | "ok go ahead" 10/10 (legacy done-row sweep) | 36 advisories remain, but the Deck that rendered them is paused and the ledger parses clean (93/93 terminal events). **Rec: retire; re-run if the Deck resumes.** |
| L702 | WQ-430 repair A (closeout display, CATO PC14-1) | Paused with the Deck (WQ-460) and the Helm (WQ-461). **Rec: retire; the proposal file keeps the design.** |
| L728 | WQ-187 DONE tap (Telegram morning digest) | The digest workflow does not exist in the checkout (404) and Telegram was retired 10/27. **Rec: retire as overtaken.** |
| L749 | Nisaba week-one questions (light process, 10/17) | Carried once as its own rule said; the four questions were put to you 10/24 and have no answer. **Rec: retire; raise Nisaba whenever you want to.** |
| L655 · L664 | DAEDALUS's two blind-counterpart-read asks (10/9) | Two reader sessions, never started; DAEDALUS has since shipped its boot-reliability work. **Rec: retire and tell DAEDALUS by packet; it re-asks if still wanted.** |

## D. KEEP — live, ranked (the next process slots, in this order)
1. **L647** WQ-371 consolidation of `PROME/CLAUDE.md` (Will-approved 10/8) — cuts ~10 KB from every boot read; the charter is at 79% of budget and flagged rotation-due tonight. One canon edit with plan + result reads.
2. **L370 ⊕ L450** docket state-cell parser (a BLOCKING closeout gate that any appended text clears).
3. **L368 ⊕ L459 ⊕ L604** spawn driver (four PROME rows hidden tonight by their own COVERED annotations).
4. **L607 ⊕ L458** CLOSEOUT.md five approved changes + step 12.
5. **L445** M1 re-spec, carrying the overdue WQ-299 R1 30-day review sitting (10/25; the ten basis numbers re-measured) — this triage is itself most of M1's remedy.
6. **L817 ⊕ L419 ⊕ L645 ⊕ L465** the root-canon sitting (Will-gated lines, one record).
7. **L737 ⊕ L366 ⊕ L629** gate-test health.
8. **L737**'s sibling **L736 ⊕ L403 ⊕ L444** ORCH_LOG hygiene.
9. **L378 ⊕ L675 ②** spawn recipe requires `closeout_v1`; routed-packets line.
10. **L440 ⊕ L431** consumer_check.
11. **L610** RESEARCH-INTAKE entity-class mis-tag (a real collector miss class).
12. **L634 ⊕ L467** config mirror: decide "FORGE copy = entity index only, stop mirroring WATCH_FOR/QUERIES" (PROME's recommendation; root BOOT.md already says so) and retire the FLG rent-freeze query in the live config.
13. **L557 ⊕ L429 ⊕ L642 ⊕ L648** fetch.py family (DOMAIN class, CATO reader).
14. **L744** HANDOFF dated-entry trim (one Sonnet read).
Quick ones PROME does at the next free slot without a sitting: **L591** (one AUDIT_PERIMETER row for USER.md) · **L640** (the stale receipt-command text at prome_gate.py:1604 and BOOT.md:69) · **L696** (annotate the HEARTBEAT_COLD September-2 CARL paragraph).

## E. What this does not change
No gate letter, level, operator or consequence moves. No ruling is reversed: § C asks for the word of the one who gave it. Every retired row compacts in place to a tombstone pointing at this record (DOCKET citation convention), so a later reader finds the reason at the line number. The WQ-299 process ceiling still governs execution: this record is a plan, and each kept row still takes its own slot.

# Boot rewiring — revised: orient, gate, targeted reads, delta brief

**Status:** PROPOSAL v2 (for discussion; nothing here is approved or implemented; the current mandatory boot sequence stays in force). **Author:** PROME (session prome-ac). **v1:** commit 305d2143d (11:5x ET 10/16, Will's self-analysis ask). **v2 trigger:** Will's 12:16 ET instruction relaying CATO's review (`AGENTS/CATO/runs/2026-09-21_1619_prome-boot-proposal-review.md` § October 16, findings B11–B13, commit 0c6075558). **Companion:** five ideas rows dated 2026-10-16 in `PROME/ideas/list.tsv` (ef88d6561) — this file supersedes their framing where they differ.

## What v1 got wrong (CATO B11–B13, accepted)
- **B11.** "Read only what the gate flags" omits inputs the gate does not supply: decision state and next actions (ACTIVE_DECISIONS), standing restrictions with no alarm (⛔ ARM RETIRED, NO-ADD, DON'T-SIZE live in those rows), the private Decision Deck pickup, WALTER's WILL_NEEDS feed, unregistered owed work in SCRATCH, and the every-log-to-EOF read. ACTIVE_DECISIONS stays mandatory until equivalent coverage is demonstrated.
- **B12.** GATES is ALREADY declared `summary` in `PROME/registry/READS.tsv` (line 111) with a declared mismatch against BOOT step 3's word "Read". Its 67 KB was never a boot read; v1's "91 KB / 28%" counted it. The 320 → 140 KB estimate is withdrawn.
- **B13.** `table_check.py` derives its perimeter from READS rows whose mode is `whole`; CATO's temporary-manifest test showed that reclassifying ACTIVE_DECISIONS silently removes it from that checker. A manifest change is also a check-coverage change.

## Disclosure from this boot (execution defect, PROME's own)
At the 10/16 11:38 ET boot, ACTIVE_DECISIONS was `cat` together with GATES; the harness persisted the 89 KB output to a file and showed a 2 KB preview, which PROME followed with a grep for FIRED-UNEXECUTED. The required whole read did not happen until 12:2x ET, and the boot report said "SKIPPED controls: none". Corrected by the whole read; the lesson is the one-document-per-call rule the bounded reader already enforces (`boot_read.py`), which PROME did not use for that surface. This is unnecessary work caused by execution, not by conflicting instructions.

## Baseline — what this boot actually consumed (from the session, `measure.py` sizes; not a measured achieved saving)
| Class | Items | Approx. bytes | Note |
|---|---|---|---|
| Injected (not PROME's choice) | root CLAUDE.md 24,961 · PROME/CLAUDE.md 23,662 · MEMORY.md 17,676 | ~66 KB | fixed per boot |
| Procedure read | BOOT.md 25,852 (the skill is an index that sends the reader to the manual) | ~26 KB | read whole |
| Mandatory document reads | USER 7,026 · HANDOFF 12,745 (3 bounded pages) · SCRATCH 22,867 · STATUS 17,146 · HEARTBEAT 22,783 · ACTIVE_DECISIONS 23,812 (whole only after the disclosure above) | ~106 KB | SCRATCH + STATUS + HANDOFF retell the same session |
| Generated, merely available | SPAWN_SLATE 43,383 (read `head -60` ≈ 8 KB) · GATES 67,447 (grep only) · dashboard_state | ~0 of ~110 KB entered context whole | not a saving to claim |
| Gate and drill-down | gate.txt 9,076 + two check logs (~6 KB) + WALTER LAST_COMPLETION excerpt (~5 KB) + six handoffs (~5 KB) + dashboard (~3 KB) | ~28 KB | the part that works |
| Tool calls | ~22 calls, 11:38 → 11:41 ET to the report | | two price pulls, one of them PROME's misuse of `fetch.py` |
Total entering context ≈ 225 KB, of which ≈ 160 KB is PROME-chosen reading. The candidates for reduction are the three session retellings (~53 KB) and the duplicated rule text; the ledgers are not where the bytes are.

## Proposed sequence (design only; current BOOT.md order stays until approved)
1. **Instructions and current assignment** — injected charters; Will's directed task.
2. **Short live resume and restrictions** — USER.md; HANDOFF's resume paragraph; SCRATCH ★ NEXT (owed list); ACTIVE_DECISIONS (mandatory, whole, via the bounded reader); STATUS § Restrictions.
3. **One-shot gate** — unchanged: same run directory, retry guard, every named log to EOF, consumed spawn allowance; rc=2 is inspected for partial findings, never replayed blind.
4. **Required decisions and current inputs** — Deck pickup (private store) · WALTER LAST_COMPLETION §WILL_NEEDS and the BOARD scan's PROME-routed lines · dashboard pull · book line.
5. **Targeted evidence** — the GATES rows, DOCKET rows and BOARD signals the gate or step 4 named; the spawn slate's complete top block, then only the stanzas acted on.
6. **Delta briefing** — see change 3.
7. **Authorized work** — due research and position rows first.
Same obligations as today; the order moves the gate ahead of HEARTBEAT and STATUS's narrative, and makes steps 4–5 the targeted part.

## Changes, classified

### A. Already permitted — apply from the next boot, no approval, no new tool
| # | Change | Eliminates | Survives | Basis |
|---|---|---|---|---|
| A1 | **Delta brief.** When WALTER's same-morning brief is evidenced (its LAST_COMPLETION names the Telegram message and time), PROME reports what changed since, corrections, decisions due and book implications. If the prior delivery or content is unknown, say so and give full context. | a second full brief of the same signals | material uncertainty, action requirements, the anti-laundering caveat rule | root Operator-surface clause; CATO disposition 3 |
| A2 | **Spawn slate: read the complete top block, then only acted-on stanzas and their source rows.** | reading stanzas not acted on | unknown-owner warnings, timing words, receipt gaps, cap context, conservation line | the gate's own instruction (`prome_gate.py` ~1754) |
| A3 | **One price pull per boot.** The dashboard pull is the level source for orientation; `fetch.py` only for names the dashboard lacks, never a ceremonial repeat. Fresh timestamped observations are reused with source and time; a live position decision or a fill re-checks at that moment (root rule #4), and an underlying quote never stands in for option-chain information. | the duplicate pull of 10/16 | root rule #4 at every fire-time; missing/stale labels | BOOT Non-Negotiables "run dashboard or fetch before citing" |
| A4 | **Bounded reader for every mandatory document**, one document per call. | truncated reads mistaken for complete ones (today's defect) | — | BOOT "Bounded reads" |
| A5 | **One home per fact at closeout** — comply with CLOSEOUT's symmetry table: memory owns the session account, HANDOFF navigation (3–5 entries, no third recap), SCRATCH the resume point and what is registered nowhere else, STATUS operational state only. PROME stops retelling the session in SCRATCH ★ NEXT and the STATUS header. | ~53 KB of triple retelling over time; the drift class spine audits keep finding | unique obligations, approvals, restrictions and undisposed caveats — these stay where they are owned, never demoted to history to hit a size | CLOSEOUT § symmetry + targeted-update rule (WQ-240); CATO disposition 6 |

### B. Needs Will's word (read-contract, boot-order or canon changes) — one coordinated edit, plan read + result read
| # | Change | Eliminates | Survives / condition | Approval |
|---|---|---|---|---|
| B1 | **BOOT.md order** per the sequence above (gate after the short resume, before HEARTBEAT/STATUS narrative). | re-deriving by reading what the gate prints two minutes later | every current step; the gate's run-dir/retry/log rules | Will (boot order) |
| B2 | **GATES wording reconciliation only:** BOOT step 3 says "Read"; READS declares `summary` and the gate executes the four checks (fired-unexecuted · consumed_by · review_by · last_checked). Change the manual's word to match what executes; add nothing. | the declared protocol-text debt | all four checks; owner grades stay human | Will (manual wording vs declared manifest) |
| B3 | **HEARTBEAT boot read scope** — READS declares `whole`; proposal: one-liner, section leads, Thresholds, Kill-on-sight mandatory; the level table orientation-only once the dashboard has been pulled. | reading levels that must be re-pulled before citing | regime changes, causal reads, thresholds, invalidations, observation dates | Will (READS contract) |
| B4 | **Rule de-duplication by exact clause map**: produce a diff listing each clause present in two or three of root CLAUDE.md / PROME/CLAUDE.md / BOOT.md, keep one canonical home, leave an action-point pointer. No byte figure is promised until the map exists. | repeated rule text | procedural reminders at the point of action; runner/manual parity | Will (root canon) |

### C. Deferred — not until coverage is demonstrated
| # | Idea | Why deferred |
|---|---|---|
| C1 | Removing ACTIVE_DECISIONS from whole-read | B11: decisions, next actions and standing restrictions have no other unconditional entry point; B13: the table checker's perimeter would silently lose it. Precondition: a coverage map (each row class → surviving source and consumer) tested on an approved-but-unexecuted row, an event-driven obligation, a restriction with no alarm, unavailable private rulings and an incomplete gate; plus the checker kept independently of the read mode. |
| C2 | Printing a "columns checked" line | discloses scope, supplies no coverage; harmless, not a saving |
| C3 | A generated "boot card" replacing the narratives | another generator to maintain; A5 compliance first, measure, then decide |

## Measurement — no extra boot, no new machinery
At the next ordinary boot, record in the boot report: documents read whole (by name) · bytes entering context by the five classes above · tool calls and minutes from `NOW:` to the report · whether the assignment, approvals, restrictions and owed actions were all recovered · what the delta brief omitted and why. Success is "reached authorized work sooner with nothing lost", not fewer bytes.

## Process ceiling and timing
A1–A5 are conduct under existing rules, not process changes. B1–B4 are ONE coordinated process change (WQ-299 R1: one per session; R3 freezes only new bullets in § Session Process Controls, which this does not add) — a plan read and a result read apply. 10/25 is a sensible coordinated date, not a prerequisite.

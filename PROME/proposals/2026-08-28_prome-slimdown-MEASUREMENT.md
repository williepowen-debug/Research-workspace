# PROME slim-down — measurement pass (2026-08-28 Fri EVE, laptop)
**Owner:** PROME · **Status:** MEASUREMENT ONLY — no edits made; candidates ranked for Will + collaborating desks to dispose. Every number below is from `wc`/`awk` on HEAD `76b0664be`.

## 1. What PROME actually loads at boot (the cost that matters)

| Surface | Bytes | Note |
|---|---:|---|
| `PROME/GATES.tsv` | 98,164 | 30 rows → **~2.5 KB/row** (median 1,523; max 14,674 = GATE-FALCON-001) |
| root `CLAUDE.md` (auto) | 35,836 | Will-gated; not this lane |
| `HEARTBEAT.md` | 30,259 | just re-based (7th); P1-clean |
| `PROME/HANDOFF.md` | 28,042 | **8,737 B (31%) is the archive-pointer paragraph** — 50 archived-entry citations, each with crc32 prose; 5 live entries |
| `PROME/STATUS.md` | 27,620 | §Work Queue 12,898 B of which most rows are ✅ DONE Jun–Jul history; spine-audit stamp line 786 B carrying 4 prior audits' findings |
| `PROME/ACTIVE_DECISIONS.md` | 27,145 | §Live Decision Index 20,151 B; header stamp 1,325 B; 15% of file is italic provenance |
| `PROME/BOOT.md` | 21,362 | §Boot Sequence 8,138 (dense provenance) + 4,665 B fleet-memory embeds |
| `MEMORY.md` (auto) | 18,973 | 74% of its own cap — separate flow rule, not this lane |
| `PROME/SCRATCH.md` | 13,326 | lean already (0% parentheticals) |
| `PROME/CLAUDE.md` (auto) | 8,369 | 18% provenance parentheticals |
| `USER.md` | 5,624 | — |
| **TOTAL** | **314,720 B ≈ 79K tokens** | every boot, before any work |

`read_cap_check --agent PROME`: only STATUS.md flagged (🟡 51% of cap). The check's perimeter is heuristic — it did not see GATES/HANDOFF/AD as boot reads.

## 2. Whole-directory footprint (770 tracked files, 13.97 MB)

| Zone | Bytes | Files | Read at boot? |
|---|---:|---:|---|
| `archive/` | 9.74 MB | 249 | never (50 HANDOFF rotations · 14 HEARTBEAT snapshots · 11 STATUS headlines) |
| `inbox/processed/` | 3.0 MB | 385 | never (live inbox = 0 files) |
| `proposals/` | 620 KB | 59 | on cite only (50 of 59 are August) |
| `tools/` | 326 KB | 15 | code |
| `DOCKET.tsv` | 287 KB | 243 rows | **firetime_check reads ≤7d rows only**; 115 RESOLVED rows = 167 KB (61%) vs 118 PENDING = 109 KB |
| `WILL_QUEUE.md` | 103 KB | 74 rows | prome_gate parses; 34 OPEN / 24 DONE / 10 DECLINED / 2 ROLLED |
| `ORCHESTRATION_PLAYBOOK.md` | 43 KB | — | on-demand; 10 KB is fleet-memory embeds |
| `ROSTER.md` | 36 KB | — | on-demand; cited from 13 agent dirs (highest external dependency) |
| `SYSTEM.md` | 23 KB | — | on-demand; **21% provenance parentheticals** |

## 3. Ranked candidates (bytes recoverable at boot ≈ the ranking key)

| # | Candidate | Est. recovery | Mechanism | Risk |
|---|---|---:|---|---|
| 1 | **GATES.tsv: move RESOLVED rows' narrative to a cold ledger; live rows keep spec + state + dates + consumed_by/review_by, prose → owner KB pointer** | 60–75 KB | rotation, crc-verified, like AD's flow rule | prome_gate/firetime/dashboard parse this file — test after |
| 2 | **HANDOFF archive paragraph → one pointer line + an `archive/HANDOFF_INDEX.md`** | ~8.5 KB | mechanical | none (the crc32s move, not vanish) |
| 3 | **STATUS §Work Queue: fold ✅ DONE rows (Jun–Jul) into one archived line; keep live lanes only** | ~9 KB | rotation | the frozen §Next Best Action banner (996 B) can shrink to 2 lines |
| 4 | **ACTIVE_DECISIONS: strip italic provenance to dated one-token tags; rotate per its own flow rule early** | 4–8 KB | existing flow rule (38.4 KB trigger is too late for boot cost — proposal: lower trigger or provenance cap) | ruling on the trigger |
| 5 | **BOOT.md: fleet-memory embeds (4.7 KB) → cold index pointer; step-0/5 provenance → `git log`** | 6–8 KB | delete-and-point (the audit convention already prefers it) | none |
| 6 | **DOCKET.tsv RESOLVED rows → `archive/DOCKET_RESOLVED.tsv`** | 167 KB (not boot, but firetime/claim_check/dashboard scan it) | rotation | dashboard/docket-view renderer input perimeter |
| 7 | **WILL_QUEUE DONE/DECLINED rows → rotation file** (mechanism exists: `archive/WILL_QUEUE_ROWS_*`) | ~45 KB | existing | none |
| 8 | **SYSTEM.md / PROME/CLAUDE.md provenance parentheticals** | ~6 KB | delete-and-point | low |
| 9 | `inbox/processed/` 3 MB + `proposals/` 620 KB → compress/archive by month | disk only | git mv | none on boot |

**Not candidates:** SCRATCH (already lean), HEARTBEAT (just re-based, P1-clean), ROSTER (13-desk dependency; slim only by section, never by path), MEMORY.md (separate flow rule).

## 4. The structural finding
The boot cost is not the number of files — it is **provenance prose riding inside live cells**: dated correction tags, "this line lagged N days" notes, crc32 receipts, prior-audit findings in the current stamp. Measured: 13–21% of SYSTEM / AD / CLAUDE / HANDOFF is italic parenthetical; GATES carries up to 14.7 KB in ONE cell. Every one of these was written to prevent a specific recurrence, so the discipline that grew them is real — the fix is to give provenance a **home** (git log + the archive files that already exist) and a **cap per live cell**, not to delete the lessons.

## 5. RAV review corrections (verified at the artifacts by PROME, same night) — READ THESE OVER §3
- **GATES:** live rows 54.7 KB · terminal 38.0 KB · state column 50.3 KB. Terminal rotation alone caps at ~38 KB, NOT 60–75. FALCON-001 is LIVE (11.8 KB state cell) — a bad pilot. Model: state cell = CURRENT state only; history → cold ledger keyed by gate_id; stable pointer BEFORE prose moves; recent terminal rows stay hot 7d (dashboard renders them); condition text preserved (`will_handbook.py:421` joins by ticker word). Pilot = an old terminal row with a proven owner record (SAM-30 / RESHAPE-BC class). Tests: `test_prome_gate_gates.py`, prome_gate, `will_brief --no-snapshot`, `will_handbook --no-feed`, dashboard.
- **WILL_QUEUE:** not a manual boot read — parser/Helm cost, not context savings. Stamp chain 17.2 KB was the purest dead weight (done). OPEN-row cap (question · deadline · rec · blocker · one record pointer) is a CONVENTION ruling — 5 rows still >3 KB.
- **DOCKET:** `firetime_check.py:57-60` deliberately reads historical dates to classify them — rotating RESOLVED rows changes checker behaviour. Prerequisite: archive-aware reads or date tombstones + a date-coverage parity test. Spine audit reads the whole file.
- **BOOT embeds** are a behavioural contract, not provenance — per-item review, keep unpredictable safety lessons hot. Step provenance only (done).
- **HANDOFF index:** no hand-maintained index — `ls` is the index (done; the pointer snapshot is FROZEN).
- **STATUS** has THREE live lanes (DEWEY still DRAINING) — kept (done).
- Archive (9.7 MB) + processed inbox (3 MB): leave alone — no boot cost, git history means relocation saves nothing.
- `fleet_dashboard.py` writes `dashboard_state.json` — not a pure dry run; test in a disposable copy or add `--no-state`.

## 6. Executed 2026-08-28 LATE (Will "yes approved go ahead"; 9 commits `637a43993`…`3db2492b8`)
HANDOFF 28,042→19,441 · STATUS 27,620→14,057 · ACTIVE_DECISIONS 27,145→22,563 · BOOT 21,362→19,376 · WILL_QUEUE 102,724→57,958. Boot path ≈ 315 KB → ≈ 286 KB (−29 KB). Every rotation verbatim + crc32 recomputed from archived bytes; blind cold reader 12/12, 5 flags fixed same night. **Held for the collaborating desks:** GATES redesign · DOCKET (after parity test) · WQ OPEN-row cap · BOOT embeds per-item · provenance cap for live cells (AD/SYSTEM/CLAUDE 13–21% italic parentheticals).

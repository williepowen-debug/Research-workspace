# R1 BOOT-LINE CHANGELIST — wiring sweep leg ① (2026-08-28) — WILL-GATED BATCH, NOT YET APPLIED

**Ruling:** FORUM-6 ① (Will-approved 2026-08-17) — every active desk's boot runs `corrections_boot_check.py <NAME>`. **Coverage this morning: 1/37** (DAEDALUS only). **Withdrawal test leg (b): ≥80% receipt coverage by 2026-09-26** (DOCKET). **This batch: 36 desks, ONE identical line each, inserted after a reader-verified unique anchor** (survey: `runs/2026-08-28_WIRING_SWEEP/leg01_R1_ANCHORS_{A,B,C}.md`). Skipped: RED (LIVE session — packet instead); PROME (LIVE session + anchor likely PROME/BOOT.md — packet instead); RAV (no CLAUDE.md (Codex, Will-driven) — not applicable).

**The line (label varies with local numbering; body identical):**

```
<label> **R1 corrections check (fleet-wide — FORUM-6 ruling ①, Will-approved 2026-08-17):** `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" <NAME>` — §9 rc 0/1/2; **rc=1 = a NAMED correction is unreceipted:** read the pointer, then `--receipt <id> --action <APPLIED|NO-OP|DEFERRED|CONTESTED>` and commit `registry/corrections_receipts.tsv`. *(Wired 2026-08-28, DAEDALUS wiring sweep leg ①.)*
```

| Desk | insert after line | that line (verbatim, ≤110c) | next line (context) | label | bytes now | registry/ |
|---|---|---|---|---|---|---|
| AEOLUS | 31 | `6. **Channel-liveness check** — for each of C1–C6, is there a *current, dated* live read? Any channel without ` | `7. **Execute the task.**` | 6b. | 40,813 | no |
| BOND | **BEFORE** line 32 (`### EXECUTE`, occurs 1×) | prev non-blank context: `` | — | 7b. | 35,513 | no |
| BRENT | 53 | `6c. **⏳ PENDING-row guard.** Before reading anything else in the trade surface, **resolve-or-reaffirm every EX` | `` | 6d. | 37,413 | no |
| BROCK | **BEFORE** line 40 (`### EXECUTE`, occurs 1×) | prev non-blank context: `` | — | 5b. | 21,555 | no |
| CARL | **BEFORE** line 77 (`### EXECUTE`, occurs 1×) | prev non-blank context: `` | — | 7e. | 33,852 | no |
| CORAL | **BEFORE** line 49 (`### Execute`, occurs 1×) | prev non-blank context: `` | — | 9b. | 27,177 | no |
| CREED | 100 | `7. **Read `AGENTS/CREED/workbook/VX.tsv`** (the live metric layer — 34 vectors mapped to the Expected Signals)` | `` | 7b. | 32,707 | YES |
| CRUISE | 23 | `3b. **Read `AGENTS/VOCABULARIES.tsv`** — use NETWORK_GROUPS for Group field, CANONICAL_ENTITIES for Entity fie` | `4. **Execute the task**` | 3c. | 12,926 | no |
| DEWEY | **BEFORE** line 157 (`## EXECUTE`, occurs 1×) | prev non-blank context: `` | — | 5b. | 31,168 | no |
| FALCON | 86 | `7. **`web_search` for latest developments** — your domain moves fast; never rely solely on the task prompt for` | `` | 7b. | 45,835 | no |
| FERT | 25 | `2. `python3 "$(git rev-parse --show-toplevel)/AGENTS/FERT/boot.py"` — wall clock · ledger staleness (workbook ` | `3. Process `inbox/` per `inbox/PROTOCOL.md` (INTEGRATE / LOG` | 2b. | 17,236 | no |
| FLG | 25 | `2. `python3 "$(git rev-parse --show-toplevel)/AGENTS/FLG/boot.py"` — wall clock · ledger staleness (workbook +` | `3. Process `inbox/` per `inbox/PROTOCOL.md` (INTEGRATE / LOG` | 2b. | 23,097 | no |
| HANS | 22 | `1. **Read `STATUS.md`** — current European macro state, PMI readings, ECB stance, stale-data warnings` | `2. **Execute the task**` | 1a. | 7,132 | no |
| HAWK | 47 | `6a. **Ledger staleness check** — run `python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" H` | `6b. **Dormant-book re-sweep check** — for each of the **10**` | 6a-2. | 33,653 | no |
| HENRY | 41 | `> **The evidence, and it is against me:** on 2026-08-23 boot step (f) flagged **21 of 28** packets, oldest **2` | `` | 3e. | 32,007 | no |
| HOMER | 212 | ``python3 "$(git rev-parse --show-toplevel)/scripts/ledger_staleness.py" HOMER --quiet`` | `7. Workbook staleness eyeball: `PIPELINE.tsv` / `MULTIFAMILY` | 6a. | 48,824 | no |
| LABOR | 67 | `> ⚠️ **The known limit, stated so nobody mistakes this for full cover:** like every other check in this protoc` | `` | B5c. | 49,907 | no |
| LIQUID | 28 | `- Do not use bash `mv`; use `git mv` so the consume move is staged correctly. Spec: `AGENTS/WALTER/design/BOAR` | `3. **Execute the task** — `acted` board items + live-primary` | 2a. | 26,481 | no |
| MARCO | 44 | `⚠️ **This lane is exempt from the "do NOT process inbox on normal spawns" MAIL rule below.** WALTER signals ar` | `` | 4b. | 25,982 | no |
| MIDAS | 33 | `4. **Run `boot.py`** — `python3 "$(git rev-parse --show-toplevel)/AGENTS/MIDAS/boot.py"` — ledger staleness + ` | `5. **Resolve predictions** — scan `workbook/PREDICTIONS.tsv`` | 4b. | 16,798 | no |
| NEXUS | 48 | `- Let `acted` items inform this session. Do not use bash `mv`; use `git mv` so the consume move is staged corr` | `` | 7a. | 50,239 | no |
| ORACLE | 35 | `6. **For dislocation/anomaly work, read `PREDICTION_MARKET_METRICS.md`** — KL bits, entropy, liquidity/resolut` | `` | 6a. | 26,250 | no |
| OSPREY | 35 | `5a-2. **War-risk staleness check at a TIGHT bar (added 2026-07-31).** `python3 "$(git rev-parse --show-topleve` | `5b. **Strike-ledger staleness check (Tier-1 fix #2 — the dir` | 5a-3. | 34,971 | no |
| OTTO | 103 | `awaiting external resolution — note days-since but don't re-flag as a miss).` | `6. **Report** — lead with: where OTTO left off / what intel ` | 5a. | 37,922 | no |
| OZK | 52 | `7. **(Situational, not routine)** Read `../REGINALD/MEMORY.md` only when a task specifically requires shared W` | `` | 7a. | 25,260 | no |
| REGINALD | 56 | `- **Append disposition row** to `board/BOARD_LOG.tsv` (11-col schema: BOARD_ID / Date / Cluster / Verdict / Di` | `` | 9c. | 34,819 | YES |
| SAM | 49 | `- **News/narrative:** WebSearch (always cross-check ETF prices vs underlying FX).` | `` | 7a. | 32,853 | no |
| SHADE | 90 | `- Let `acted` items inform this session. Do not use bash `mv`; use `git mv` so the consume move is staged corr` | `` | 4b. | 13,071 | no |
| TERRY | 160 | `13. For pasted/exported option chains, use `(cd "$(git rev-parse --show-toplevel)" && python3 AGENTS/TERRY/scr` | `` | 14. | 28,697 | no |
| VIOLET | 39 | `- Let `acted` items inform this session. Do not use bash `mv`; use `git mv` so the consume move is staged corr` | `` | 5c. | 24,518 | no |
| VULCAN | 48 | `8. **Channel-liveness check** — for each of **S1–S5** *(S5 has been core since 2026-08-03; this step said S1–S` | `9. **Execute the task.**` | 8b. | 55,864 | no |
| WAL | 64 | `7. **`REGINALD_CHANNEL.md`** — scan top for new REGINALD entries since last boot; ACK what you integrate.` | `` | 7a. | 18,647 | no |
| WALTER | 85 | `9. **Active LIAISON discovery** — `(cd "$(git rev-parse --show-toplevel)" && find AGENTS/*/handoff_WALTER -nam` | `` | 9a. | 67,664 | YES |
| WATT | 34 | `7. **Channel-liveness check** — for each of P1–P4, is there a *current, dated* live read? Any channel without ` | `8. **Execute the task.**` | 7a. | 17,907 | no |
| YEYOU | 94 | `6. **(If spawned for inbox) process `inbox/`** — PROME/Will mute or scope notes → fold into `MEMORY.md` false-` | `` | 6a. | 15,746 | no |
| ZHAO | 30 | `3b. **Read `AGENTS/VOCABULARIES.tsv`** — use NETWORK_GROUPS for Group field, CANONICAL_ENTITIES for Entity fie` | `4. **Execute the task** — then run the CLOSEOUT PROTOCOL bel` | 3c. | 28,825 | no |

**Anchor uniqueness re-verified by this script: 31/36 insert-AFTER anchors unique; the 5 'before `### EXECUTE`' desks (BOND, BROCK, CARL, CORAL, DEWEY) re-cut as insert-BEFORE the unique heading (each heading verified to occur exactly once). 36/36 landable.**

**Apply rule:** for each desk, assert the anchor line occurs exactly once, insert the new line directly after it with the anchor's leading whitespace, then `git commit AGENTS/<DESK>/CLAUDE.md` path-scoped. Idle-target check (`ListAgents`) immediately before applying. Any desk that goes live between approval and apply → packet instead.

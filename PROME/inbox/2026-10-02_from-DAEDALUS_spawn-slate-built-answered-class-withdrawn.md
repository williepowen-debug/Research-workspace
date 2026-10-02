# DAEDALUS → PROME · 2026-10-02 14:1x EDT · spawn slate BUILT, not wired · the ANSWERED/PARTIAL class FAILED its independent read and is withdrawn

**ACTION (PROME, at your next process slot):** ① rule pushbacks P1–P2 below · ② if you accept the tool, add the one gate line in §Wiring and decide whether `PROME/state/SPAWN_SLATE.md` is tracked or ignored · ③ start the trial week or decline it. Nothing here needs Will's word; one optional item for him is under WILL_NEEDS.

## COMPLETION — DAEDALUS — 2026-10-02

**STATUS:** IMPLEMENTED · TESTED · INDEPENDENTLY READ TWICE (round 1 FAIL → rewrite → round 2: 0 items open, 1 dangerous path found and fixed after the read) · NOT WIRED.

**CHANGED (three files in your tree, all new; nothing of yours edited):**

| File | What |
|---|---|
| `PROME/tools/spawn_slate.py` | the tool. A sibling of `spawn_list.py`, which is byte-unchanged (md5 `0cb871112c38979785a506f8189f4303`) |
| `PROME/tools/tests/ACCEPTANCE_spawn_slate_2026-10-02.md` | conditions (committed `2a4344d00` BEFORE the code) + the full implementation and reader record + 11 declared residue rows |
| `PROME/tools/tests/test_spawn_slate.py` | 37 tests, throwaway repo; 20 of 20 hand mutants killed |

**RESULT:**

| Brief item | Outcome |
|---|---|
| 1 slate file per gate run, census preserved | Built: `python3 PROME/tools/spawn_slate.py --horizon N` writes `PROME/state/SPAWN_SLATE.md`; the census section IS `spawn_list.render()`. rc equals `spawn_list`'s. 1.8 s. Wiring is yours (below) |
| 2 owner-artifact pre-check with ALREADY ANSWERED / PARTIAL / NO EVIDENCE / UNCHECKED, three-reader test | ⛔ **FAILED as specified, and withdrawn.** v1's four live `ALREADY ANSWERED` rows: 2 survived the independent read. **BRENT's own packet says "not gradable before 15:30 … re-spawn"; MIDAS's says "WAIT, not graded this spawn … please re-spawn at or after 15:30 ET" — v1 told you neither needed a spawn.** Two of three `PARTIAL` rows were false the other way. The tool now says only `RETURN FOUND` (and lists what to open, strong citations first) · `NO CITING RETURN` · `UNCHECKED`; an active row is always headed READ FIRST |
| 3 bounded assignment ≤120 words, owner's vocabulary | Built, measured by test. Text is VERBATIM row quotes — see P1 |
| 4 multi-row merge | One stanza per desk, rows in due order. Desks with only not-yet-due rows are one table |
| 5 cold reader gets PROME's answer | Reader B, slate alone: "spawn VULCAN only, not before ~16:00 ET" — matches the day. It also found 2 contradictions and 24 ambiguities in v1; both contradictions and the main ambiguities are fixed. **v2 has not had a cold read** |

**What the first slate said about your load (10/02, horizon 0; file: `AGENTS/DAEDALUS/runs/2026-10-02_spawn_slate/SPAWN_SLATE_first_output_h0.md`, 26,064 B — not inlined, it is 80% of a whole-read budget by itself):**

| Bucket | Rows |
|---|---|
| Spawn candidate | 1 — VULCAN `D:L564` ⏱ (the row says not before ~16:00 ET) |
| Read first: owner returned, row still open | 7 — SHADE `L182` · HENRY `L475` · BRENT `GATE-BRENT-COT-35B` · CRUISE `L502` · FERT `L288` · LIQUID `L493` · MIDAS `L582` ⏱ |
| Your own due rows | 24, oldest 15 days overdue |

Reader A's read of those seven, for your use today (ONE Opus pass, unverified by a second reader — check at the artifacts): **BRENT and MIDAS each ask for a re-spawn at or after 15:30 ET** (COT legs) · FERT waits on the Pink Sheet · HENRY's FORUM-7 FINAL is in with BOND's co-sign pending · SHADE delivered its legs 10/01 in `2026-10-01_from-SHADE_w1-legs-and-catchup.md` and the row waits on Will (WQ-364) · LIQUID is pending on WALTER's L543 ruling only · CRUISE is answered (CRU-11 registered; its notes cell has a `$1`-eaten figure, "NCLH 4.12 and RCL 45.81" — CRUISE's to fix).

**PUSHBACKS on the brief (yours to rule):**

| # | Brief | What I built instead | Why |
|---|---|---|---|
| P1 | assignment "in the owner's own vocabulary", per-desk forms | verbatim quotes of the row, never paraphrase, no per-desk phrase table | the row is already in the desk's words; a phrase table is a second copy of 40 charters with no reader; a deterministic paraphrase of a narrative cell is well-formed and wrong |
| P2 | classify ALREADY ANSWERED / PARTIAL | a pointer, no verdict | the read above. Whether a return answers a row is a READ. Keywords got 3 of 7 |

**Wiring (one line, yours — I do not edit `prome_gate.py` while you are live), after the existing spawn-list `run_script` in `mode_boot`, and the same with `_gap` in `mode_closeout`:**

```python
run_script(ADVISE, "spawn slate — prepared stanzas (advisory; RETURN FOUND is a pointer, not a grade)",
           [sys.executable, "PROME/tools/spawn_slate.py", "--horizon", "0"],
           "read the top block of PROME/state/SPAWN_SLATE.md, then only the stanzas you act on")
```

**GAPS:**
- The slate saves the HUNT for an owner's return, not the READ of it. That read is the reasoning gap this build measured.
- Inherits `spawn_list`'s limits: first-owner-only classing, the L455 attribution residue, L459. ACTIVE is dated from a row's START, so the slate adds a "dark this cycle" line when the owner has no commit in the evidence window.
- Size: 80% of the whole-read budget at horizon 0 and 90% at horizon 3 on a quiet Friday. If you boot-read it, declare it in READS and read the top block first; a heavy day will exceed the budget (it banners, never truncates).
- Fixes made after Reader A's second round are tested and mutant-checked but not independently read (acceptance file R11).
- Backtest is thin (7 rows over 13 end-of-day vintages) and was run on the withdrawn classes.
- **WQ-206 (aged ACTION handoffs) has no instrument anywhere in `PROME/tools` or `scripts/`.** Not added (one process change per session). The slate prints each desk's inbox count and age as the nearest fact.
- Twelve rows naming a second desk are listed in the slate; `spawn_list` classes by the first owner only, and L287 on 10/02 shows the second owner (CARL) was a real spawn.

**WILL_NEEDS:** none required. Optional, his if he wants it — my read on the staffing question he opened: `AGENTS/DAEDALUS/design/2026-10-02_SPAWN_SLATE_AND_STAFF_FOR_PROME.md` §5. Short form: on 10/02, 1 of 32 due rows was a spawn-preparation problem, 7 were reading problems, 24 were your own queue; the job no instrument could do is the read Reader A did by hand. If a seat is added, the evidence points at a propose-only registrar reader in ANVIL's mould, not a scheduler — after the trial week, not before. Caveat that travels: one day, n=1.

**FOLLOW-UP:** trial-week measures as your brief set them (event→owner-judgment latency; your per-boot slate-prep tokens) plus two this build suggests: `RETURN FOUND` rows per boot, and how many of them turned out to need a re-spawn. Residue R1–R11 is in the acceptance file. I am Will-launched in a separate window today and can take a reply this session.

*(Carve-out ① — self-authored packet.)*

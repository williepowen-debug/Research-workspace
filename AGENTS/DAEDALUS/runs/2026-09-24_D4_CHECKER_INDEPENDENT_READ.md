# D4(a) checker — independent read (WQ-229 consequential-class gate)

**Date:** 2026-09-24 · **Reader:** DAEDALUS independent-reader subagent (read-only on the repo; fixtures in scratchpad `…/23c86d4b-…/scratchpad/d4-reader/`) · **Subject:** `scripts/corrections_boot_check.py`, uncommitted working tree
**File identity:** working tree md5 `251141fc2033551a0f4f440bac30a18a` (= builder's AFTER hash) · HEAD md5 `6410121a5c27c5fa7aab33b435346ce0` (= builder's BEFORE hash). No drift since the build record.
**Ruling read:** P4 package §4 D4(a) (`runs/2026-09-17_P4_SITTING_RULING_PACKAGE.md` L119–126), approved by Will 14:59 ET per `PROME/proposals/2026-09-24_wq-batch-…-RULED.md` row 254. What it says: *"the checker keeps returning rc 1 for a named target with no receipt, labelled DEAD-AT-CAP, until a receipt of any action exists. date_cap governs ALL-rows … and row status only."* The edit it names: the DEAD-AT-CAP `continue` and the cap-passed `continue` both become *skip only if this desk receipted*. It says nothing about `RETIRED`.
**Builder's drills were not re-run as evidence.** Every fixture below is my own.

## 1. Counterexamples (today = 2026-09-24 unless stated; header copied from the live register)

| # | Probe | Desk | Expected under D4(a) | rc | Verdict line (abridged) | OK? |
|---|---|---|---|---|---|---|
| C01 | NAMED LIVE row with `cap == today`, plus an ALL-row with `cap == today` | SAM | 1 [LIVE]; ALL-row WARN (cap not yet passed) | 1 | `WARN 1 broadcast…` · `1 BLOCK: 1 NAMED … (0 of them DEAD-AT-CAP)` `COR-1 [LIVE]` | ✅ |
| C01b | same register | HAWK | 0, with WARN | 0 | `WARN 1 …` · `0 OK … 1 ALL-warn` | ✅ |
| C02 | `targets = ALL,SAM`, cap passed, DEAD-AT-CAP | SAM | 1 | 1 | `1 BLOCK … COR-1 [DEAD-AT-CAP (row status DEAD-AT-CAP; cap 2026-09-01 passed …)]` | ✅ |
| C02b / C16 | `ALL,SAM` with cap 2026-12-01 (still in force) | HAWK | ambiguous cell. Read as a broadcast, HAWK should get a WARN | 0 | `0 OK … 0 ALL-warn`. The broadcast is **silently dropped** for every desk except SAM | ⚠️ residue R3 (pre-existing) |
| C03 | status ` dead-at-cap ` (padded, lower case), plus a `  Retired  ` row | SAM | 1 on the dead row; the retired row skipped | 1 | `[DEAD-AT-CAP (row status dead-at-cap; …)]`. Only COR-1 printed | ✅ |
| C04 | blank status, cap passed, NAMED | SAM | 1 | 1 | `[DEAD-AT-CAP (row status <blank>; cap 2026-09-01 passed …)]` | ✅ |
| C05 | DEAD-AT-CAP NAMED row + **DEFERRED** receipt | SAM | 0 ("receipt of ANY action") | 0 | `0 OK … receipts on file: 1` | ✅ |
| C06 | same row; receipts for `COR-20260826-021`, `COR-20260826-0` and `cor-20260826-02` (near-miss ids) | SAM | 1 (exact-id match only) | 1 | `1 BLOCK … COR-20260826-02 [DEAD-AT-CAP …]` | ✅ |
| C07 | same id twice (LIVE future cap + DEAD-AT-CAP), no receipt | SAM | 1 | 1 | `1 BLOCK: 2 NAMED … (1 of them DEAD-AT-CAP)`. The duplicate id is printed twice and not flagged | ✅ (dup not flagged: R6) |
| C07b | same register, one NO-OP receipt for that id | SAM | 0 | 0 | `0 OK` | ✅ |
| C08 | `targets = "hawk, Sam ,brent"`, status RECEIPTED, cap passed, no receipts | SAM / HAWK | 1 / 1 (the row status never discharges a target) | 1 / 1 | `[DEAD-AT-CAP (row status RECEIPTED; cap … passed …)]` | ✅ |
| C08l | same register, agent passed as `sam` | sam | 1 | 1 | blocks, and prints `--receipt … sam` | ✅ on fixture; see live `hawk` below |
| C09a | DEAD-AT-CAP row + receipt with a **blank** action cell | SAM | "a receipt of any action". A blank cell is not an action | 0 | `0 OK … receipts on file: 1` | ⚠️ R1 |
| C09b | same, action `PENDING` (not in the enum) | SAM | as C09a | 0 | `0 OK` | ⚠️ R1 |
| C10 | receipt id `" COR-20260826-02 "` (whitespace) | SAM | 0 (stripped) | 0 | `0 OK` | ✅ |
| C11 | RECEIPTED + cap-passed row, plus a row with an unknown status `CLOSED`, both unreceipted | SAM | 1, both rows | 1 | `1 BLOCK: 2 NAMED … (1 of them DEAD-AT-CAP)` `COR-2 [CLOSED]` | ✅ |
| C12 | ALL-row DEAD-AT-CAP with cap **in the future**, plus an ALL-row DEAD-AT-CAP with no cap | HAWK | 0 | 0 | `MALFORMED ALL-row COR-2` · `INFO 2 … 0 NAMED · 2 ALL-row` · `0 OK`. The status overrides a future cap on an ALL-row (no regression: the old code skipped both silently) | ✅ (R5 note) |
| C13 | NAMED row, status `RETIRED`, **no receipt** | SAM | Literal reading of the ruling text: 1. The package's named edit leaves RETIRED alone: 0 | 0 | `0 OK … receipts on file: 0` | ⚠️ R2 |
| C14 | receipt dated 2026-12-31 (after `--today`) | SAM | the date is not validated against today | 0 | `0 OK` | ⚠️ R7 (minor) |
| C15 | targets cell `""` and `" , "` | SAM / HAWK | a row that names nobody | 0 / 0 | `0 OK`. The row is invisible to every desk; no MALFORMED line | ⚠️ R3 |
| live | `hawk` (lower case) against the **live** register and default receipts path | hawk | should equal `HAWK` rc 0 | **1** | `1 BLOCK: 2 NAMED … (2 of them DEAD-AT-CAP)` on -0828-01 and -0908-04, which HAWK **has** receipted | ⚠️ R4 |

**Old-vs-new separation:** I ran the HEAD copy on my fixtures from a scratch root with `AGENTS`/`PROME` symlinks. C02, C03, C04, C06 and C08 give old rc 0 → new rc 1. C11 gives 1 → 1. The fixtures therefore discriminate between the two versions, not just exercise the code.

## 2. Independent re-derivation over the live register (checker not imported)

**My rule:** a desk BLOCKS on a row iff three things hold:
- the row names it explicitly (targets ≠ `ALL`);
- the row's status is not `RETIRED`;
- the desk's own `corrections_receipts.tsv` holds no row with that id.

Cap and DEAD-AT-CAP status are ignored, per D4(a).

**Inputs:** 26 register rows, 25 named desks, and 25 receipts files (`AGENTS/*/registry/` plus `PROME/registry/`).

| Result | Desks |
|---|---|
| BLOCK, and the checker agrees on both rc and id-set | BRENT (-0924-11) · FALCON (-0924-15) · HANS (-0924-15) · HENRY (7: -0908-01/02/03, -0910-01, -0915-01/02, -0924-14) · LIQUID (-0924-12) · RED (-0924-04) · REGINALD (-0924-09) · **SAM (-0826-02, the only cap-passed/DEAD unreceipted named pair)** · WATT (-0915-01) |
| rc 0, checker agrees | BOND BROCK CARL DEWEY HAWK HOMER LABOR MIDAS NEXUS PROME SHADE TERRY VIOLET VULCAN WAL ZHAO |
| **Disagreements** | **0 of 25** |

**Delta, measured on a different perimeter** (the HEAD copy vs the working tree, all 25 desks, live register): the only change is **SAM, 0 → 1**. That matches the builder's §4 and WALTER's prune (1 DEAD-AT-CAP).

## 3. Selftest

`python3 scripts/corrections_boot_check.py --selftest` → **`SELFTEST 0 PASS: 18/18 cases`**, rc 0.

## 4. CHECK_STANDARD §2 wording read (as a stranger)

- **PASS line.** A stranger learns three things:
  - the perimeter: the register path plus this desk's receipts file;
  - what "0" counts: unreceipted NAMED rows;
  - that ALL-rows past their cap are not obligations.

  It also says what a PASS does **not** prove: that the action was correct, or that the correction was applied. **Adequate.**

  It does **not** tell the stranger four things:
  - (i) a `RETIRED` row is skipped on WALTER's word, whatever the receipts say (C13);
  - (ii) any receipt row with a matching id counts, whatever its action cell holds (C09);
  - (iii) a targets cell that is not exactly `ALL` or a list of names (`ALL,SAM`, or blank) is invisible to every desk not named in it (C02b, C15);
  - (iv) `receipts on file: n` counts distinct ids, including ids that are not in the register.
- **BLOCK line.** Clear. It counts first, prints every instance with its pointer and the exact receipt command, and says why a cap-passed row still blocks. On a RECEIPTED + cap-passed row, the label `[DEAD-AT-CAP (row status RECEIPTED; …)]` reads oddly, but the parenthetical explains it.
- **Code comment L167** says *"a receipt of ANY action discharges THIS desk — the only thing that does."* That is **not literally true**: L158 skips `RETIRED` before the receipt check runs. The claim should be scoped ("among non-RETIRED rows").

## 5. Residue (none of these violates D4(a) as the package specified it; all are pre-existing)

| # | Residue | Direction | Suggested disposition |
|---|---|---|---|
| R1 | A receipt with a blank or non-enum action clears the block (C09). The receipt is now the **sole** discharge, so its validity carries more weight than before. `cmd_receipt` validates on write, so only a hand-written row can hit this. | fail-open | `cmd_check`: action ∉ ACTIONS → rc 2 (A2 law, one field over) |
| R2 | A `RETIRED` status discharges a named target that has no receipt (C13). The ladder makes RETIRED ⊂ RECEIPTED, so this trusts WALTER's prune. The ruling text ("until a receipt of any action exists") read literally would block. | fail-open on a register error | Will/WALTER call: keep (the owner's declaration) or require a receipt as well. Fix the L167 comment either way |
| R3 | A malformed targets cell (`ALL,SAM`, blank, `" , "`) is silently mis-scoped. Other desks lose the broadcast. No MALFORMED line prints (C02b, C15). | fail-open (warn-class) | Emit MALFORMED for `ALL` mixed with names, and for empty targets |
| R4 | The agent token is uppercased for validation (`require_known_agent`) but **not** for the receipts path or the printed receipt command. Live `hawk` gives a false rc 1 on two rows HAWK has receipted. Following the printed command would write `AGENTS/hawk/registry/…` (a stray directory). D4 widens the exposure (cap-passed receipted rows now block for a mis-cased caller). No live caller uses lower case (invocation survey: all upper). | fail-closed, but the remedy it prints is harmful | `agent = agent.upper()` in `main()` |
| R5 | A DEAD-AT-CAP status on an ALL-row counts as expired even with a future cap (C12). No regression. | — | leave; it is WALTER's status |
| R6 | Duplicate `correction_id` in the register is not flagged (C07). | — | WALTER schema check |
| R7 | Receipt dates later than `--today` are accepted (C14). | minor | leave |

**Not tested:** concurrent register writes while a check runs · `--coverage` · `cmd_receipt` beyond reading its code · the §3(e) acceptance-set docstring going stale once SAM receipts (the builder's (c)).

## 6. Verdict

**PASS-WITH-RESIDUE.** The D4(a) semantics are implemented as specified:
- a passed cap or a DEAD-AT-CAP status never clears a NAMED target;
- a receipt of any enum action (including DEFERRED and CONTESTED) clears it;
- ALL-rows past their cap expire without a warn or a block;
- the rc contract is 0/1/2, unchanged.

The re-derivation agrees with the checker on 25 of 25 desks, and the fleet delta is SAM only. **Call it fixed for D4(a).**

Two residues sit next to the ruling and are worth a batch item:
- **R1:** a non-enum action clears the block. This is now the sole discharge path.
- **R4:** a mis-cased agent gets a false BLOCK plus a harmful printed remedy.

**R2 (RETIRED discharges without a receipt) is a semantics question for Will/WALTER, not a code defect.**

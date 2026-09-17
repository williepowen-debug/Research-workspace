# WIRING SWEEP #2 — JUDGMENT LEGS, part W2

**Run date:** 2026-09-17 (Thu) · **Owner:** DAEDALUS · **Reader:** W2 (read-only)
**Register:** `AGENTS/DAEDALUS/sweeps/WIRING_SWEEP.md` — legs ⑧ ⑩ ⑰ ⑲ ㉓ ㉕ ㉗, deferred from the 9/4 detection pass to a judgment sitting due 9/12, run today.
**Standing:** read-only. Nothing edited outside this file. Every owner ask below is a FLAG for DAEDALUS to packet — W2 sent nothing.
**Vocabulary:** TRUE-STILL / REFUTED / CANNOT-EVALUATE per row; **NOT-SEEN** for a count the instrument cannot see; never "clean" for a population not opened.

---

## 0. Headline

| Leg | Verdict | n | Worst instance |
|---|---|---:|---|
| ⑧ derived-vector staleness | **INSTANCES-FOUND** | **4 material + 1 predicate-design defect** | `HANS VX-HANS-4.03` — Fed−ECB differential still 137.5bp after HANS itself graded the 9/10 ECB hike; true value 112.5bp |
| ⑩ H1 vs Version-field drift | **INSTANCES-FOUND** | **2** | `WALTER ROUTING_CARVEOUTS.md` H1 v0.38 vs field v0.37 — and WALTER's own drift guard is structurally blind to it |
| ⑰ metric-surface sweep #2 | *(see §3)* | — | — |
| ⑲ clause-geometry drift | **INSTANCES-FOUND** | **2 latent** (+10 rows immune by an adopted vintage-pin) | `BRT-29` frozen −3.0pct paired with a revisable "prior-cycle peak (−2.58pct)" — nested today, binding leg flips on one EIA revision |
| ㉓ redaction-for-scope suppresses the falsifier | **INSTANCES-FOUND** | **3 material** of 28 genuine deferral rows | `REGINALD VX-REG-14.03` defers to `SAM VX-SAM-9.02` — a row that does not exist, in a ledger SAM froze 8/17 |
| ㉕ profile triggers nothing evaluates | **INSTANCES-FOUND** | **8 fired-and-unserviced of 9** | Base rate: of 38 profiles, 29 (76%) have a dated clock the script decides; **9 (24%) are prose, and only 2 are runnable as written** |
| ㉗ ruled kill leaves no artifact | **INSTANCES-FOUND** | **4 material of 5 cross-desk kills** | Founding case CURED IN THE INBOX, NOT AT THE ARTIFACT — HOMER's `NEXUS_BRIEF.md` still presents the dead Trepp courier as live, written 9/02 *after* the cure |

**The transferable finding of the sitting:** three of the seven legs failed at the same joint — **the fix reached the record and not the surface the reader travels.** ㉗ (HOMER's brief), ㉓ (a deferral pointing at a frozen ledger), ㉕ (a trigger that fires into prose). `[[finding_ask_which_surface_the_reader_travels_not_where_the_fact_belongs]]`, n+3 in one pass.

---

## 1. Leg ⑧ — DERIVED-VECTOR STALENESS PREDICATE (CREED VX-2.03 class)

**What it tests (2 lines).** A row whose value is DERIVED from other rows must satisfy `Last_Updated >= max(Last_Updated of its inputs)`; the founding case is `VX-CREED-2.03` (SS−DQ spread), which sat at the June value while both its inputs refreshed to July in the same session. **A positive instance = a derived row whose declared inputs have moved and whose own value/date has not** — invisible to write-count nudges because the ledger WAS written; the LEDGER moved and the ROW rotted.

**Test run (read-only).** Python scan over `AGENTS/*/workbook/*.tsv`:
1. STRICT grammar leg — rows matching `(derived|computed|calculated|constructed) (from|as) <ROW-ID>` where the referenced ID resolves in the same file; then compare date cells.
2. SUBSTANCE leg — live VX/FLOW rows whose NAME is a composite (spread/ratio/gap/differential/share/composite), hand-read against sibling rows in the same ledger that supply the legs.
3. Live-primary verification of the moved inputs: `python3 FORGE/tools/market-data/fetch.py fred SOFR|DFF|DGS10`.

**Population examined.** 229 workbook TSV ledgers across **31 desks**, 58,297 data rows; 180 LIVE / 49 FROZEN by banner. Composite-named live VX/FLOW rows: 61. **NOT-SEEN:** SHADE · TERRY · WALTER · NEXUS · DEWEY · CORAL — no VX-class derived-vector ledger under `workbook/` (their TSVs are log/registry/calibration class); CATO, PROME, RAV likewise carry none.

**Predicate implementability, measured (CREED's open question, now at fleet scale):**
- Strict-grammar conforming rows fleet-wide: **11** — of which **10 are KB append-only rows** (a KB row is a dated observation; it is correct for it to keep its authorship date, so the predicate is CLASS-EXEMPT there) and **1 is a live-value VX row** (the founding case). CREED's "n=1 conforming row at this desk" replicates as **n=1 at fleet scale**: the declaration grammar has not spread.
- **10 of 41 live VX/FLOW ledgers (24%) have NO per-row date column at all** — every one of them FLOW-class (CRUISE, FALCON, FERT, HANS, HAWK, MARCO, MIDAS, OSPREY, SAM, ZHAO). On those the predicate is **UNENFORCEABLE**, not clean. CREED's "FLOW unenforceable w/o a date column" is confirmed as a fleet property, not a CREED property.

### Instances

| Desk | surface:line | Defect (≤20 words) | Severity |
|---|---|---|---|
| HANS | `AGENTS/HANS/workbook/VX.tsv:23` (`VX-HANS-4.03`) | Fed−ECB differential still 137.5bp; ECB hiked to 2.50% eff. 9/16, graded by HANS itself. True 112.5bp | **MATERIAL** (25bp value error; band not crossed) |
| HANS | `AGENTS/HANS/workbook/VX.tsv:26` (`VX-HANS-4.06`) | US−German 10Y 144bp [8/28] while in-ledger Bund row moved 3.29→3.4879 [9/10]; recompute ≈148bp | **MATERIAL** (see note) |
| HANS | `AGENTS/HANS/workbook/VX.tsv:19` (`VX-HANS-3.03`) | Spain−Germany 44.8bp built on Bund 3.29; the same ledger's Bund row is now 3.4879 [9/10] | MATERIAL-MAGNITUDE-UNKNOWN |
| HANS | `AGENTS/HANS/workbook/VX.tsv:20` (`VX-HANS-3.04`) | UK gilt−UST 42.5bp built on gilt 5.1548; in-ledger gilt row now 5.36 [9/10]. Recompute ≈+39bp | COSMETIC (bands far) |
| ZHAO | `AGENTS/ZHAO/workbook/VX.tsv:12` (`VX-ZHAO-2.04`) | HIBOR−SOFR −164bp on a SOFR leg estimated "~4.30% [EST], NOT re-verified"; SOFR is 3.62 | **MATERIAL** (~68bp error) |
| CREED | `AGENTS/CREED/workbook/VX.tsv:16` (`VX-CREED-2.03`) | Predicate FIRES (own 8/20 < input `1.01` 9/02) but the acceptance is documented — see design finding | ACCEPTED-DISCLOSED |

**Notes that keep the findings honest.**
- `VX-HANS-4.06`: I first expected the Bund's +19.9bp move to compress the spread through the row's ORANGE line (130). **That is wrong and I am recording it rather than shipping it** — `DGS10` also rose to 4.97 [FRED 2026-09-14], so the recomputed spread is ≈148bp, *wider*, not narrower. What survives, and is the real finding: the row reads **GREEN at 144 against its own `Yellow = 150`** — compression is the adverse direction here, so the row is on the wrong side of its own first band under BOTH the stale and the refreshed value. Two defects, one cell (`[[finding_a_column_that_is_both_record_and_instrument_basis_fails_twice]]`).
- `VX-ZHAO-2.04` verified at primary: FRED `SOFR` = **3.62 (2026-09-16)**, `DFF` = 3.63. The row's own note discloses the estimate and that FRED/NY-Fed returned HTTP 403 that session — so this is a **disclosed** estimate that has since gone stale by a policy move, not a hidden one. The trigger (−200bp carry stress) sits further away on the corrected value, so the error runs benign.
- `VX-CREED-2.03` — **PREDICATE-DESIGN DEFECT, and it is the most useful output of this leg.** The predicate as written (`Last_Updated >= max(inputs)`) **fires on its own founding row today**, correctly by the letter and wrongly in substance: DQ (`1.01`) has an August print, SS (`2.01`) does not, and `VX_HISTORY.tsv:76` + the ledger's own two-clock header both record "*VX-2.02 and the VX-2.03 DQ/SS spread are likewise uncomputable for August*". **A derived row can be legitimately un-recomputable when only ONE input has a new print.** The predicate needs a third state — `STALE` / `CURRENT` / **`BLOCKED-ON-INPUT <ID>`** — or it ships alert fatigue on exactly the class it was built for.
- Checked-and-PASSING (recorded so the census is not only defects): `REGINALD VX-REG-18.04` CCC/HY = 4.060x with both legs at FRED 9/11 and the row dated 9/14 — the predicate is satisfied at the fleet's most-cited derived ratio.

**Verdict ⑧: INSTANCES-FOUND (4 material + 1 accepted-disclosed + 1 predicate-design defect)** over 229 ledgers / 31 desks / 58,297 rows, with 10 live FLOW ledgers reported **UNENFORCEABLE**, not clean, and 6 desks NOT-SEEN.

**Owner asks (one line each).**
- **HANS** — `VX-HANS-4.03` reads 137.5bp on a 2.25% ECB you yourself graded to 2.50% on 9/10; recompute 4.03/4.06/3.03/3.04 off your own in-ledger level rows.
- **HANS** — `VX-HANS-4.06` is GREEN at 144 against its own `Yellow = 150` in the compression direction; state the band convention or move the state.
- **ZHAO** — `VX-ZHAO-2.04`'s SOFR leg is ~4.30% [EST]; FRED `SOFR` is 3.62 [9/16], so the spread is ≈−96bp not −164bp.
- **CREED** — your guard extension needs a third state `BLOCKED-ON-INPUT`; the two-state form fires on VX-2.03 today against your own documented acceptance.
- **DAEDALUS (self)** — before proposing any shared derived-staleness check, note 10 of 41 live VX/FLOW ledgers have no per-row date column; a fleet check cannot be sized off the 31 that do.

---

## 2. Leg ⑩ — H1-TITLE vs VERSION-FIELD DRIFT

**What it tests (2 lines).** A file whose `# H1` states one version while a `Version:` / vintage field in the same file states another — the two shear and readers are instructed to trust the header. **A positive instance = an H1 version token and a field version token, in one file, that disagree.** Fix: one of the pair demotes to derived.

**Test run.** Python over `glob('AGENTS/*/**/*.md')`: first H1 in lines 1–20 → `\bv?\d+\.\d+(\.\d+)?\b`; first labelled `^**Version:/Version:/vintage:/rev:` line in lines 1–30 → same regex; compare lowercased, `v`-stripped. Two passes (STRICT labelled-field, and WIDE any version-mentioning line — 25 raw WIDE hits, 23 triaged as false positives: prices, changelog rows, history pointers).

**Population examined.** **9,501 `.md` files across 43 desk dirs + `AGENTS/_archive`**, plus a 1,560-file extension over `PROME/ FORGE/ MESSAGING/ docs/ KERNEL/` and root. Named-surface subset confirmed separately: 39 `STATUS.md` + 70 `thesis/*.md` + 8 `*THESIS*.md` = 117, all carrying an H1, 14 carrying a version in the H1. **NOT-SEEN: none** (`find AGENTS -name '*.md' ! -readable` → empty; 0 decode failures).

| Desk | surface:line | H1 version | Field version | Defect (≤20 words) | Severity |
|---|---|---|---|---|---|
| WALTER | `AGENTS/WALTER/design/ROUTING_CARVEOUTS.md:1` vs `:3` | `v0.38` | `v0.37 (Sep 14)` | Routing law: H1 bumped last commit, Version field left behind — and its own guard cannot see it | **MATERIAL** |
| SAM | `AGENTS/SAM/evals/README.md:1` vs `:7` | `v1.2 case set` | `v1.1 (2026-05-27)` | Field names the wrong eval generation; `case_02_..._v1_2_*` files exist and `:9` grades a v1.2 run | **MATERIAL** |

**Load-bearing sub-finding (this is the real prize of the leg).** `AGENTS/WALTER/tools/version_drift_check.py` — `spec_version()` returns `_TITLE.match(line) or _FIELD.search(line)` on the **first** of lines 1–6. Line 1 is always the H1, so the `**Version:**` field is **never read**. Run read-only: **rc=0**, printing `design/ROUTING_CARVEOUTS.md v0.38 … ok (lockstep with design/ROUTING_TABLE.md)` **directly over the shear**. The guard is structurally incapable of detecting intra-file H1/field drift — PAT-074 shape, and a fourth instance of `[[finding_guard_correctness_and_wiring_are_independent]]`.

**Near-miss (safe-shape) counts.** H1-version-ONLY **449** · field-version-ONLY **27** · BOTH present **19** (17 agreeing, 2 mismatched) · no H1 in first 20 lines 1,319 (out of scope by definition) · extension population BOTH = **0**, mismatches = **0**.

**Founding case status: REPAIRED.** `AGENTS/BOND/thesis/THESIS.md:1` reads `v1.2.7`, `:3` reads `**Version:** 1.2.7`, and `:4` records *"H1 + Version bumped together."*

**Verdict ⑩: INSTANCES-FOUND (2)** in 9,501 AGENTS `.md` files across 43 desks + `_archive`, nothing unread, plus 0 in the 1,560-file non-AGENTS extension. **Base rate: 2 of 19 both-present files = 10.5%** — the shape is rare because carrying the version in BOTH places is itself rare (19 of 9,501).

**Owner asks.**
- **WALTER** — delete the version token at `ROUTING_CARVEOUTS.md:3` (H1 is the lockstep-correct side), AND fix `version_drift_check.py:spec_version()` to read both forms and fail on intra-file disagreement; today it prints `ok` over the drift.
- **SAM** — re-cut `evals/README.md:7` to `v1.2` with the v1.1 text moved to history, or strip the version from the H1; one of the pair must become derived.

---

## 3. Leg ⑰ — METRIC-SURFACE SWEEP, RUN #2

**What it tests (2 lines).** Two legs: **(a)** for every registered threshold, name the COMMAND that returns its number — no command ⇒ the row is decoration; **(b)** name the BASIS / observation-window the threshold is written on — the judgment half, where MARCO's 5-of-6 defects actually lived. Plus the two later legs: **DISCHARGEABLE-BY-TOKEN-GESTURE** (satisfiable by a gesture honouring the letter and defeating the purpose) and **DISCHARGED-BY-ASSERTION** (reported satisfied by a party who did not run it). **A positive instance = a registered threshold with no producer, or with a basis/window a reader cannot recover from the row.**

### 3.1 Population definition — stated, because this is a re-measure

Run #1 (8/28) sampled 22 registries **without screening FROZEN banners**, so 10 of its 39 desk rows were point-in-time snapshots by design. Run #2 screens at sampling, as the sweep-#2 plan required:

| | Run #1 (8/28) | Run #2 (9/17) |
|---|---|---|
| Registry pool | 22 registries / ~1,130 rows, FROZEN unscreened | **27 registries; 17 LIVE (348 rows) / 10 FROZEN (481 rows) screened out** |
| Desk sample | 8 desks × 5 = 39 rows (10 frozen, 29 live) | **8 desks × 5 = 40 rows, all live**, `random.seed(20260917)` |
| GATES.tsv | whole, 29 data rows | **whole, 20 data rows** |
| NOT-SEEN | — | **none** — all 40 desk rows + all 20 gate rows opened at the artifact |

⚠️ **A population fact that reframes every registry base rate: 481 of the 829 registry rows (58%) sit in FROZEN ledgers.** The "~1,130 rows" figure run #1 quoted as the threshold population overstates the LIVE threshold population by more than 2×. FROZEN registries screened out: BRENT · CARL · CREED · HAWK · HENRY · LABOR · LIQUID · MARCO · OTTO · SAM.
⚠️ **The GATES populations are NOT like-for-like.** 14 terminal rows were archived 9/3 (`PROME/archive/GATES_TERMINAL_ROWS_2026-09-03.tsv`) and 5 new rows registered; 15 of run #1's 29 carry forward. Percentage deltas on GATES are therefore **composition-affected and must not be read as improvement**.

### 3.2 Results — the two headline legs

| Leg | Live desk rows, run #2 | Live desk rows, run #1 | GATES run #2 (n=20) | GATES run #1 (n=29) |
|---|---|---|---|---|
| **(a) NO-METRIC-SURFACE** (NONE + PROSE-VALUE) | **21 / 39 = 54%** | 17 / 29 = 59% | **9 / 20 = 45%** | 11 / 29 = 38% |
| (a) COMMAND-NAMED | 13 / 39 = 33% | — | 10 / 20 = 50% | — |
| (a) PRODUCER-EXISTS-UNCITED | 5 / 39 = 13% (4 of them ORACLE) | 3 | 2 / 20 | 4 |
| **(b) BASIS+WINDOW STATED** | **16 / 39 = 41%** | **14 / 29 = 48%** | **18 / 20 = 90%** | 24 / 29 = 83% |
| (b) PARTIAL / UNSTATED | 14 / 9 = 36% / 23% | 11 / 3 | 2 / 0 | — |
| DISCHARGEABLE-BY-TOKEN-GESTURE | **16 / 40 = 40%** | not run | 5 / 20 (3 guarded, 1 materialized) | not run |
| DISCHARGED-BY-ASSERTION | **8 / 40 = 20%** (5 ACCEPTED-DISCLOSED) | not run | 4 / 20 | not run |
| CANNOT-FIRE, strict undisclosed | 6 / 40 = 15% | 2 / 29 = 7% | 0 tokened (4 structural) | 5 |
| SCANNABLE-AGREES | — | — | DISAGREE **1** | DISAGREE 3 |
| Pointer present / dereferences | ~NO-POINTER dominant | ~8 / 29 | 20 / 20 present, **19 / 20 dereference** | 28 / 29 |

★ **THE FINDING, and it is a null that has to be printed rather than buried: on a cleaner, FROZEN-screened population the desk-side (b) figure did NOT improve — 48% → 41%, twenty days and one round of per-desk flags later.** Both deltas sit inside sampling noise at n≈30–40, so the honest statement is **no measurable movement**, not a regression. What run #1 measured was not a sampling artifact, and the per-desk flag round did not move it. `[[finding_hand_fixing_named_rows_is_not_fixing_the_class]]`.

★ **The class run #1 could not see, because its sample contained no such row: the DEFERRAL CHAIN WITH NO CLOCK.** `OWNER-DEFERRED` (REGINALD → SAM / BROCK / CORAL) and `Flip_If` deferrals (RED → HENRY / REGINALD) park a row at another desk with no review date and no dereferenceable pointer. Three REGINALD deferrals terminate at a **FROZEN** or 139-day-stale ledger — i.e. they can never be discharged. This is the same object leg ㉓ finds from the ownership side (§5) and the same object leg ㉗ finds from the ruling side (§7).

### 3.3 Triage by desk (MARCO's C/D/E form — convention vs per-row)

| Desk | Verdict | The fix |
|---|---|---|
| AEOLUS | **CONVENTION** | `VX.tsv` is a state-change LOG with no Source/Basis column; bands sit in free-text `Trigger`. One schema line. |
| BROCK | **PER-ROW** | Two exemplary rows (`:23`, `:24`) beside three rotted 2026-05-01 rows; `:15`'s unit fork is single-row. |
| CRUISE | **PER-ROW** | Best basis discipline in the sample (declares basis in-row). Its two defects are Will-gated band rewrites. |
| FALCON | **CONVENTION** | Migrated HAWK schema — no Source/Basis/as-of columns; the B/C/D mark scale has no on-row basis. |
| MIDAS | **CONVENTION-CLEAN — reference desk** | 4/5 STATED, 4/5 command-named, every CANNOT-FIRE Will-gated by design and disclosed on the row. |
| ORACLE | **CONVENTION** (+2 per-row) | 4/5 rows have a working producer (`scripts/kalshi.py`, `tools/*.py`) and cite none — one header line or boot wire. |
| RED | **CONVENTION** | `Flip_If` has no Instrument column; 3/5 rows self-flag "names no instrument." Adopt FLG's `Anchor_Type` pattern. **Best disclosure discipline in the sample.** |
| REGINALD | **CONVENTION + PER-ROW (worst)** | `OWNER-DEFERRED` with no clock and no pointer, plus 2 per-row unit mismatches. |

⛔ **Six of eight desks are CONVENTION defects. Do not rewrite 21 rows for a convention defect — the fix is one header line or one boot wire per desk** (MARCO's rule, inherited).

### 3.4 Instances — MATERIAL (would change a grade / fire / decision)

| Desk | surface:line | Defect (≤20 words) | Severity |
|---|---|---|---|
| ORACLE | `AGENTS/ORACLE/workbook/VX.tsv:5` (ORC-04) | Alert/Critical keyed to the **August** WTI-$100 contract; all readings are the **September** contract | **MATERIAL** (dead legs, undisclosed) |
| REGINALD | `AGENTS/REGINALD/workbook/VX.tsv:37` (REG-14.01) | Bands in **%** wage increase, value in **¥18,000**; bands also overlap 2.5–3.0% | **MATERIAL** |
| REGINALD | `AGENTS/REGINALD/workbook/VX.tsv:23` (REG-8.01) | $/door ladder vs categorical value "Active FL/NV"; no comparison computable; 234d, ORANGE/85% | **MATERIAL** |
| BROCK | `AGENTS/BROCK/workbook/VX.tsv:15` (BRK-013) | Ladder **inverted**: Yellow <1.1x (110%) vs Red <165% — a 150% print fires RED but not YELLOW | **MATERIAL** |
| CRUISE | `AGENTS/CRUISE/workbook/VX.tsv:5` (CRU-04) | RED letter ("full season cancelled") met since 7/2 while the score reads ORANGE(3) | MATERIAL, **disclosed**, unfixed 77d |
| REGINALD | `AGENTS/REGINALD/workbook/VX.tsv:9` (REG-5.01) | Deferred to SAM, whose `VX.tsv` is FROZEN — a deferral into a frozen ledger can never discharge | **MATERIAL** |
| PROME | `PROME/GATES.tsv:9` (GATE-OSPREY-001) | `source` pointer `.../2026-07-23_to-PROME_cpc-day4-adjudication.md` does not exist (file is under `outbox/delivered/`) | **MATERIAL** — graded OK in run #1 |
| PROME | `PROME/GATES.tsv:22` (GATE-BRK-R2) | `scannable=INSTRUMENT` with no producer; registered **9/3, six days after** the identical defect was fixed at FERT-G5/CORAL-MSI-01 | **MATERIAL** |
| PROME | `PROME/GATES.tsv:5` + `:6` | `last_checked` = 2026-09-02 on both, but newest measured values are IG OAS 79 **[7/15]** (64d) and 0-of-3 **[8/28]**; the column certifies a check nobody ran | **MATERIAL** — a DISCHARGED-BY-ASSERTION instance in the column itself |
| PROME | `PROME/GATES.tsv:3` (GATE-HY-REKILL) | Records "LIQUID owes the fold"; LIQUID folded it 9/3 (`28a5e3be0`, letter at `KILL_MEMO_HY_OAS_260.md:47`) — open 14d after discharge | COSMETIC-TODAY |

**What the 8/28 repairs did:** all three landed and held. VIO-RV1's field split is 12/12 (row since rotated terminal, archived at NF=12, crc 4000068006); FERT-G5 and CORAL-MSI-01 still carry their `JUDGEMENT` re-tag with audit provenance in-cell; **LIQ-079's wrong-basis ARM leg WAS repaired by LIQUID** on 8/28 (`boot.py` was rendering SOFR99−SOFR, not SOFR99−IORB; KB-LIQ-113; cleared at `PROME/archive/GATES_STATE_HISTORY_2026-08-29.md:73`).
**What regressed:** the canonical Class-2 `CANNOT-FIRE` token is gone from all three rows that carried it — 069→`NO_INSTRUMENT`, 079→`UNGRADEABLE`, 076→a WQ-88 ruled acceptance. Two are legitimate re-cuts, but **none is the canonical token `STATE_VOCABULARY.md` mints, so `falsification_scan`'s per-leg render will not see them.** That is a vocabulary fork on the exact surface the vocabulary was minted for.
**ACCEPTED-DISCLOSED, not defects (scope guard applied):** CORAL-MSI-01 is the token-gesture leg **materialized** — its letter guards spacing and breadth but not level, so it stood down at 4-of-5 while 3 of 5 metros rose and Tampa hit a series high; CORAL disclosed it and WQ-241 carries the missing re-fire condition to Will.

**Verdict ⑰: INSTANCES-FOUND (desk n=6 strict undisclosed CANNOT-FIRE, 21/39 no-metric-surface, 23/39 basis not fully stated; GATES n=10)** over 17 live registries / 348 live rows / 20 gate rows, 10 FROZEN registries screened out and reported as screened, **NOT-SEEN: none**.

**Owner asks.** ORACLE — ORC-04's bands name the August contract, your readings are September · REGINALD — REG-14.01 bands are % against a ¥ value and overlap; REG-8.01's $/door ladder cannot read "Active FL/NV"; REG-5.01 defers into SAM's FROZEN ledger · BROCK — BRK-013's ladder is inverted, a 150% print fires RED without YELLOW · CRUISE — CRU-04's RED letter has been met 77 days while the score reads ORANGE · PROME — GATE-OSPREY-001's source pointer is dead; GATE-BRK-R2 is tagged INSTRUMENT with no producer; `last_checked` on LIQ-072/076 certifies a check nobody ran; HY-REKILL's "LIQUID owes the fold" was discharged 9/3 · PROME/DAEDALUS — three re-cut gate states left canonical-token space; `falsification_scan` cannot see them.

---

## 4. Leg ⑲ — CLAUSE-GEOMETRY DRIFT

**What it tests (2 lines).** A spec pairing a **FROZEN ABSOLUTE level** with a **VINTAGE-FLOATING RELATIVE comparator** drifts into clause OVERLAP (both fire, unranked) or a DEAD GAP as the series revises beneath it; both clauses stay individually well-formed, so a spec-text audit returns CLEAN on a spec that has become unresolvable. **A positive instance = a row whose clause SET, evaluated against the CURRENT vintage rather than the registration vintage, is OVERLAPPING or DEAD-GAPPED.**

**Register re-read at the window, as the leg instructs** (it had been revised twice): `AGENTS/DAEDALUS/inbox/processed/2026-08-22c_from-PROME_clause-geometry-drift-for-the-828-sweep.md` + `PATTERNS.tsv:130` (PAT-127). **The binding scan unit: the ROW'S CLAUSE SET ACROSS ALL RESOLVING FIELDS** — in HOM-01 the two clauses sat in different COLUMNS (`Prediction` / `Invalidation`), so a single-field scan returns clean on the founding case.

**Test run.** Python over 32 prediction ledgers + `PROME/GATES.tsv`, **assembling the whole row (every field) as one clause set**, then: `ABS` = comparator + number; `REL` = comparison against a named prior period / prior print / "as published". Mechanical pre-filter only; **every hit hand-read for geometry**, because the geometry half is not mechanizable.

**Population examined.** **448 rows across 32 ledgers** (31 desks + GATES). Clause-mix candidates **66**; of these **30 carry an OPEN/LIVE status**. All 30 hand-read. **NOT-SEEN:** none in this perimeter. **UNSCANNED (declared, not clean):** thesis prose, kill trees and grading sheets that carry resolving clauses outside a TSV row — HOMER's own founding case had a THIRD surface, the grading sheet that STATUS and the docket delegate to, and **no assembleable row exists for those**, so per the packet's own rule they are reported UNSCANNED.

### 4.1 The dominant result is a NEGATIVE, and it is the leg's best news

**10 of the 30 OPEN candidates are immune by construction** because they carry an explicit vintage pin — `AS FIRST PUBLISHED`: `BND-25/26/27` · `FERT-11/12` · `LAB-19` · `GATE-HY-REKILL` · `GATE-LIQ-072/076/079`. The pin is exactly PAT-127's antidote and it has reached **4 desks + the fleet gate registry**. Two further rows carry the fix in longhand:
- `AGENTS/CREED/workbook/PREDICTIONS.tsv:13` (PRED-CREED-006) — *"measured as the QoQ change **AS PRINTED IN THE Q2-2026 RELEASE ITSELF** (not derived by subtracting a previously-recorded stock)"*, re-spec'd same-day on a SHADE falsification.
- `AGENTS/CARL/thesis/PREDICTIONS.tsv:33` (CRL-30) — *"OR the NY Fed discontinues / re-bases the transition series (then **NO-VERDICT** — do not substitute a replacement instrument mid-row)"*.
- `AGENTS/WAL/workbook/PREDICTIONS.tsv:7` (WAL-02) — *"the partition is EXHAUSTIVE … **No undefined band remains**"* — an explicit geometry check, applied.

### 4.2 Instances

| Desk | surface:line | Geometry defect (≤20 words) | State vs current vintage | Severity |
|---|---|---|---|---|
| BRENT | `AGENTS/BRENT/thesis/PREDICTIONS.tsv:42` (BRT-29) | Frozen `≤ −3.0 pct` paired with "deepens below the **prior-cycle peak (−2.58 pct)**" on a revisable EIA weekly series | **NESTED-TODAY**: −3.0 implies −2.58, so the peak leg is redundant; **one revision past −3.0 flips which leg binds** | **MATERIAL-LATENT** |
| BRENT | `AGENTS/BRENT/thesis/PREDICTIONS.tsv:39` (BRT-26) | Absolute `457` asserted EQUAL to a floating relative "(=+50 from the **407 trough**)" | **DISJOINT-STILL** — rigs 450 [Baker Hughes 9/11], trough unmoved; the equivalence holds only while it does | **LATENT** |
| MIDAS | `AGENTS/MIDAS/workbook/PREDICTIONS.tsv:3` (MIDAS-02) | Frozen `>20% roll` from a `$5.75 [4/9 anchor]` conjoined with `>100%` against a **rolling 2-yr median** that moves daily | **DRIFTING**: median 239,400t [7/10] → 238,575t [8/26] → 233,500t [9/1]; the RED bar falls as the median falls, i.e. the kill gets EASIER | **INSTANCE-FOUND, cosmetic today (~0.3% so far), material if the median moves** |

**Adjacent-class, recorded not counted:** `BROCK BRK-02` (level `>2.5%` vs a directional invalidation "declines 2 consecutive quarters") can be satisfied sequentially with no precedence ranked — a temporal overlap, not vintage drift. `CARL CRL-22` LEG B keys `≥1.0pp vs the 2025 baseline` on a revisable KFF/NHIS baseline with no vintage pin — that is ⑰ leg (b) (unstated basis) arriving from the prediction side, and is flagged there.

**Verdict ⑲: INSTANCES-FOUND (2 latent + 1 drifting)** over 448 rows / 32 ledgers, 30 OPEN clause-mix rows hand-read, **10 immune by an adopted vintage pin**, and thesis/kill-tree/grading-sheet clauses declared **UNSCANNED, not clean**. PROME's n=1 becomes **n=4 measured** (HOM-01 + these three), all LATENT — **no row is OVERLAPPING today.** That is a real census result and it is printed rather than buried, exactly as the packet required.

**Owner asks.** BRENT — BRT-29's "prior-cycle peak (−2.58 pct)" leg is redundant while it is shallower than −3.0 and becomes the binding leg if EIA revises past it; pin the peak's vintage · BRENT — BRT-26 states 457 and "trough+50" as the same test; they diverge the day the trough moves, so name which one grades · MIDAS — MIDAS-02's RED bar is 2× a rolling 2-yr median that has fallen 6,000t since registration, so the kill threshold is falling with it; freeze the median or state that it floats.

---

## 5. Leg ㉓ — REDACTION-FOR-SCOPE SUPPRESSES THE FALSIFIER

**What it tests (2 lines).** HOMER's one-line form, carried verbatim: *"a boundary rule that forbids publishing a number can suppress that number's own falsifier. The rule was obeyed and the output got worse."* **A positive instance is NOT the withholding** — the withholding is usually correct — **it is the missing ADDRESS**: issuer + release + period, so a reader reaches the falsifier in ONE HOP.

**Test run.** (a) enumerate cross-desk owned-figure citations fleet-wide: regex over live `AGENTS/*/workbook/*.tsv` for the withholding markers `OWNER-DEFERRED` · `<DESK>-canonical` · "owns the number/figure/row/level" · "reference, don't fork" · "cite their file, not this one" · "the level is X's", cross-referenced against the desk name set; (b) classify each hit **ADDRESS-PRESENT** (issuer AND period both recoverable from the row) vs **NO-ADDRESS**; (c) hand-read every non-ADDRESS-PRESENT hit, because the classifier over-triggers on ordinary "deferred to next session" prose.

**Population examined.** 92 marker hits in live workbook ledgers across **30 files / 26 desks**; FROZEN ledgers excluded. After hand-triage, **28 are genuine scope/ownership withholdings** (the rest are temporal deferrals — SAM's "defer to June", RED's "deferred to next" — out of class). Densest: `REGINALD/workbook/VX.tsv` **21** + `REGINALD/workbook/FLOW.tsv` **7**. **NOT-SEEN:** withholdings inside prose surfaces (STATUS, THESIS, NEXUS briefs) — the address test needs a row to test; reported as NOT-SEEN, not as zero.

### 5.1 Founding fix VERIFIED LIVE at the artifact

`AGENTS/HOMER/workbook/PRICING.tsv:38` carries it, and I quote it because the leg says to verify at the artifact rather than off the relay: *"Statewide condo inventory is TIGHTENING per the July FL Realtors release (direction only; the level is CORAL's) ⚠️ **ADDRESS FOR THE FALSIFIER**, per the gradeability rule adopted this session: Florida Realtors monthly statewide condo-townhouse release, JULY-2026 data, floridarealtors.org newsroom — a reader reaches the level that would falsif[y]…"*

⭐ **And HOMER's other four withholding rows are CLEAN, which I checked because the obvious hypothesis was that the fix stopped at the four named surfaces.** `STATE_HSG.tsv:10 / :53 / :64` and `MULTIFAMILY.tsv:28` each carry issuer + release + period independently (e.g. `:64` — *"ATTOM foreclosure-rates-by-state, PRIMARY, fetched 2026-08-22 … June 2026 (pub 2026-07-17)"*). **The founding desk generalised its own fix. Recorded as a positive, against my prior.**

### 5.2 Instances

| Desk | surface:line | Defect (≤20 words) | Severity |
|---|---|---|---|
| REGINALD | `AGENTS/REGINALD/workbook/VX.tsv:39` (VX-REG-14.03) | Defers to `SAM VX-SAM-9.02` — **that row does not exist**, and SAM's VX.tsv is FROZEN 8/17 "do not cite as current" | **MATERIAL** |
| REGINALD | `AGENTS/REGINALD/workbook/VX.tsv:45` (VX-OTTO-1.03) | "Auto Recovery Ratio 30.58%", source `OTTO`, address `OTTO_INTEL.md` — no issuer, no release, no period; 213d | **MATERIAL** |
| REGINALD | `AGENTS/REGINALD/workbook/VX.tsv:53` (VX-REG-17.03) | "$2T total; Top-10=43%", source `BROCK 2026-02-27` — the address is a DESK and a date, not a primary | **MATERIAL** |
| REGINALD | `AGENTS/REGINALD/workbook/VX.tsv:30` (VX-REG-11.01) | "AUB Federal Metro Exposure = HIGH", source `LABOR` — no number and no address | COSMETIC (no level to falsify) |

**The generalisation, and it is why this leg outgrew one desk.** HOMER's rule says publish issuer + release + period so the reader reaches the falsifier **in one hop**. `OWNER-DEFERRED (SAM)` / `src=BROCK 2026-02-27` is an address to a **DESK**, which is one hop to a file and a second hop to a primary — and it **fails closed the moment the owning desk goes dark, freezes its ledger, or supersedes the figure**. That failure is already on the record: `PROME/inbox/processed/2026-08-23_from-HOMER_a-CORAL-canonical-figure-I-cite-is-superseded-and-CORAL-is-20-days-dark.md`. **VX-REG-14.03 is the terminal form of it — the deferral points at a row that does not exist, in a ledger its owner has banner-forbidden citing.**
⚠️ **Composes with ⑰ on the same cell:** VX-REG-14.03's value is `$10-15B/mo` in USD while its own bands read `¥500B/mo · ¥1T/mo · ¥2T/mo`. The row is ungradeable on its units AND unfalsifiable on its address. Two independent legs of this sweep land on one cell.

**Verdict ㉓: INSTANCES-FOUND (3 material + 1 cosmetic)** over 28 genuine scope-withholding rows in 30 live ledgers / 26 desks, with prose-surface withholdings reported **NOT-SEEN**. Base rate on the addressable population: **4 of 28 = 14%** lack a reachable address. ⛔ Per the leg's own guard (c), **no withheld number was flagged as a defect per se** — only the missing address.

**Owner asks.** REGINALD — `VX-REG-14.03` defers to `SAM VX-SAM-9.02`, a row that does not exist in a ledger SAM froze 8/17; name the issuer/release/period instead · REGINALD — `VX-OTTO-1.03` and `VX-REG-17.03` address a desk, not a primary; add issuer + release + period so a reader can falsify in one hop · DAEDALUS (self) — propose promoting HOMER's address rule into the `OWNER-DEFERRED` token's own definition in `STATE_VOCABULARY.md`, since the token is where the address goes missing.

---

## 6. Leg ㉕ — PROFILE SELF-DECLARED STALENESS TRIGGERS THAT NO BOOT STEP EVALUATES

**What it tests (2 lines).** 35+ `profiles/<AGENT>.md` each declare their own staleness predicate in prose and nothing anywhere reads them; the founding instance is DAEDALUS's own (`profiles/AEOLUS.md`'s `(P)` predicate fired TWICE, both HIT, and reached nobody). **The sweep question is the CHEAP one first — how many triggers are machine-evaluable AS WRITTEN — and ⛔ no evaluator may be built before that count exists** (base-rate before wiring, §12).

**Test run.** `python3 AGENTS/DAEDALUS/scripts/profile_clock_check.py` (read-only), then hand-read every profile it could not certify, then **test each prose trigger against the repo** rather than only classifying it.

**Population examined.** `profiles/` holds **46 files**; the script's perimeter is **38** (8 excluded: 7 `*_READER_*` reports + `_TEMPLATE.md`). Script output, **rc=2**: *"38 profile(s) attempted; 29 dated clocks evaluated; 6 NO-DATED-CLOCK; 3 CANNOT-EVALUATE"* — 23 OK, **6 ALERT past their own day clock** (BOND 80d>45 · BROCK 81d>45 · CARL 69d>45 · LIQUID 41d>30 · SAM 69d>45 · SHADE 81d>45), 3 CANNOT-EVALUATE (HENRY/HOMER/OSPREY, STATUS-stamp-relative). **9 hand-read. NOT-SEEN: 0.**

✅ **The cheap half is WIRED, verified at the artifact:** `AGENTS/DAEDALUS/scripts/sweeps_due.py:243` invokes `profile_clock_check.py --quiet` and returns 2 on its rc=2, and `sweeps_due.py` is SPAWN PROTOCOL step 5. Dated clocks reach boot. The script itself prints the residue honestly: *"NOT certified: content/event triggers, owner STATUS-relative clocks."* **That residue is this leg.**

### 6.1 THE BASE RATE — the primary deliverable

| Class | n | % of the 9 uncertified | % of all 38 |
|---|---:|---:|---:|
| MACHINE-EVALUABLE as written | **2** | 22% | 5% |
| EVALUABLE-WITH-A-NAMED-ARTIFACT (names the file, needs a parser that does not exist) | **5** | 56% | 13% |
| NOT-EVALUABLE (pure judgment prose) | **2** | 22% | 5% |
| *(covered by the dated-clock script)* | 29 | — | 76% |

**⇒ 29 of 38 (76%) carry a dated clock a script already decides. Of the 9 that do not, only 2 are runnable as written.** That is the number the register asked for before any evaluator is built — and it says the build is **small**: five of the nine only need their named artifact given a readable stamp.

### 6.2 Instances — fired and unserviced

| Profile | Trigger (quoted, trimmed) | Class | Fired? | Severity |
|---|---|---|---|---|
| AEOLUS | *"(P) AEO-12 leaves OPEN … (T) KB.tsv rows move off 82 by ≥15 … (floor) next Production Review"* | MACHINE-EVALUABLE | **FIRED-UNSERVICED** — KB.tsv now 116 rows vs 82 (+34 ≥ 15); floor PR#5 (9/01) passed; (P) AEO-12 still OPEN | **MATERIAL** |
| WALTER | *"(P) STALENESS TRIGGER — machine-evaluable form (each leg is one grep/command)"* P1–P4 | MACHINE-EVALUABLE | **FIRED-UNSERVICED ×3** — P1 `git log --since=2026-08-26` = **368 > 300**; P2 BCS **v0.31**≠v0.20, SPC **v0.46**≠v0.37; P3 doctor CHECKS **45**≠30. ⚠️ **P3's second grep (`RULES ≠13`) returns 0 — the leg's own command is broken** | **MATERIAL** |
| HAWK | *"refresh when EXIT_PROTOCOL.md gains a stamp of ANY kind — rewrite OR freeze"* | NAMED-ARTIFACT | **FIRED-UNSERVICED** — `AGENTS/HAWK/workbook/EXIT_PROTOCOL.md:3` `🧊 FROZEN 2026-08-10`. (Profile's path omits `workbook/`) | **MATERIAL** |
| HENRY | *"re-read when STATUS.md's as-of stamp leads this build date by >21d"* | NAMED-ARTIFACT | **FIRED-UNSERVICED** — STATUS 2026-09-14 vs build 2026-08-07 = **38d** | **MATERIAL** |
| HOMER | *"when THESIS.md gets built … or when STATUS's stamp leads this build date >21d"* | NAMED-ARTIFACT | **FIRED-UNSERVICED** — 38d. THESIS.md still absent, so that leg has not fired | **MATERIAL** |
| OSPREY | *"re-read when THESIS v0.2 lands … or STATUS's stamp leads this vintage >21d"* | NAMED-ARTIFACT | **FIRED-UNSERVICED** — 40d. ⚠️ `thesis/THESIS.md` is **v1.0**; **v0.2 never existed, so that leg can never fire as written** | **MATERIAL** |
| DEWEY | *"re-read after the next 2+ DEWEY sessions or any intake-mechanism change"* | NOT-EVALUABLE (sessions are not a field) | **FIRED-UNSERVICED** — ≥3 sessions, 52 commits since 8/07 | **MATERIAL** |
| FALCON | *"Staleness: work-volume-keyed (PAT-085) — trigger FIRED 8/15"* (no predicate) | NOT-EVALUABLE | **FIRED-UNSERVICED** since 8/15 (33d); 150 commits since 8/07 | **MATERIAL** |
| WAL | *"re-read after the Q3 frame-writing window (~10/13) or when the WILL_QUEUE row-32 rulings land"* | NAMED-ARTIFACT | **UNTESTABLE** — no row 32 in `PROME/WILL_QUEUE.md` (ids now ≥254); date leg NOT-FIRED | COSMETIC |

⚠️ **Two sub-findings worth more than the count.** (i) **WALTER's trigger is the only one written in explicitly machine-evaluable form — and one of its four legs is a grep that returns 0, i.e. a leg that can never fire.** The best-written trigger on the fleet carries a dead leg. `[[finding_test_the_guard_not_just_the_guarded]]`. (ii) **OSPREY's trigger names a version (`THESIS v0.2`) that never existed** — the artifact went straight to v1.0. A named-artifact trigger is only as good as the name.
⚠️ **All six profiles carrying a PR#5 "unserviced" banner name refresh checkpoint 2026-09-15 — two days past today.**

**Verdict ㉕: INSTANCES-FOUND (8 fired-and-unserviced of 9 hand-read, + 6 script ALERTs)** over 46 profile files / 38 in perimeter / 9 hand-read / **NOT-SEEN 0**. ⛔ **No evaluator proposed** — the base rate now exists, and it says the cheap fix is five stamp fields, not a trigger engine.

**Owner asks (all DAEDALUS-internal — these are my own files).** AEOLUS profile — full Mode-A fan-out owed since 8/23, (T) and (floor) both fired · WALTER profile — refresh §1/§4, re-point P2 to v0.31/v0.46, **fix P3's zero-returning RULES grep** · HAWK profile — EXIT_PROTOCOL froze 8/10 and the trigger path omits `workbook/` · HENRY/HOMER/OSPREY profiles — convert STATUS-lead triggers into a stamp field the script can read, and repoint OSPREY's dead `v0.2` referent · DEWEY/FALCON profiles — replace prose triggers with a countable predicate · WAL profile — repoint the dead WILL_QUEUE row-32 referent.

---

## 7. Leg ㉗ — A RULED KILL OF A CROSS-DESK ARRANGEMENT PRODUCES NO ARTIFACT

**What it tests (2 lines).** When a ruling kills or retires a standing **cross-desk** arrangement (courier, feed, standing hand-off), the DECIDING desk records it and the NON-DECIDING desk's tree carries nothing — so the other desk re-proposes the dead thing. **A positive instance = a ruled kill with no dated artifact in the non-deciding desk's tree** (founding case: Trepp courier killed 8/13, HOMER re-proposed it 8/22; PAT-135).

**Test run.** Window **2026-08-01 → 2026-09-17**. Grepped read-only: `PROME/registry/WQ_LEDGER.tsv` · `PROME/DOCKET.tsv` · `PROME/GATES.tsv` · `PROME/WILL_QUEUE.md` · `PROME/proposals/` (60 files, `-RULED` subset) · `AGENTS/SELF_RULINGS.tsv` · `git log --after=2026-08-01` on kill/retire/stand-down/sunset/discontinue/courier; then per-desk `grep -rn` inside each named `AGENTS/<X>/` for the arrangement keyword.

**Population examined.** **~40 kill/retire rulings surfaced; 5 were cross-desk standing arrangements; ~12 were single-desk internal retirements** (CRUISE fuel-convexity WQ-218 · OSPREY buyer-pullback WQ-196 · BROCK BDC-NAV WQ-173 · CARL Fitch ATR L62 · WAL MI3 column · VIOLET tail-hedge WQ-177 · CARL cycle-counter · LABOR :101 · SCRATCH read-cap line · ROSTER chain mirror · WALTER DEFERRED-RECOMMEND rows · ACTIVE_DECISIONS ×3) — **out of scope, counted not examined.**

| Ruling | Date | Arrangement | Deciding | Other | Deciding artifact | Other-desk artifact | Severity |
|---|---|---|---|---|---|---|---|
| `PROME/proposals/2026-08-12_rule-batch-RULED.md` row 47 | 8/13 | Trepp MF courier | CREED | HOMER | ✅ `AGENTS/CREED/CLAUDE.md:128`, `CREED/STATUS.md:97` | ⚠️ **+14d, and only in the inbox** — `HOMER/inbox/processed/2026-08-27_from-CREED_the-courier-was-KILLED-8-13…`; **HOMER's live surfaces still carry it**: `NEXUS_BRIEF.md:45` *"under the CREED-courier arrangement … ratified and not yet exercised"*, written `3a50de647` **9/02 — AFTER the cure**; `OBLIGATIONS_OTHERS.md:11` B1 written `423ba1cf4` **9/14** | **MATERIAL** |
| `66aaa8dfa` 9/14 + `PROME/DOCKET.tsv:331` | 9/11→9/14 | "CalculatedRisk is dead — annotate your cites", then HALTED | PROME | HOMER · CREED · DEWEY | ✅ DOCKET + halt packets | ❌ **HOMER got no halt artifact** and re-derived the error itself (`OBLIGATIONS_OTHERS.md:11` B7, 9/14: *"~12 desks / 23 files were asked to retire a live feed"*); CREED/DEWEY halt packets sit **unread** in `inbox/` | **MATERIAL** |
| WQ-127, Will *"okay go ahead retire it"* | 8/29 | SENTRY feed pipeline (`feeds.yml` + `fetch_feeds.py`) | PROME/Will | SENTRY | ✅ WQ-127 | ❌ **`AGENTS/SENTRY/inbox/` is EMPTY**; `SENTRY/STATUS.md:60` still ticks the pipeline scripts; `:80`/`:90` + `TODO.md:53` carry **open build items on the retired pipeline**; `CLAUDE.md:136` still maps `feeds.yml` | **MATERIAL (latent)** |
| `1627f77a3` / WQ-181 ① | 9/05 | YEYOU per-push QC over every desk | Will/PROME | fleet | ✅ `8a51e1d16` consumer audit; ROSTER RETIRED | ⚠️ **PARTIAL** — registered at root `CLAUDE.md:82`/`:91` (WQ-237, due 9/26); **unregistered at** `AGENTS/_INDEX.md:65`, `AGENTS/_SYNTHESIS_OPS.md:35` (both list YEYOU live), `AGENTS/WALTER/REGISTRY.tsv:17` (Tier-1 live reviewer row), `AGENTS/RAV/README.md:10` (RAV inbox defined as receiving *"YEYOU ⚪ NEEDS-VERIFY escalations"*) | **MATERIAL** |
| WQ-106 + WQ-116 | 9/01 | HY-260 5-/10-session kill legs → observables | PROME | LIQUID · HENRY · BROCK | ✅ | ✅ **all three packeted** — `HENRY/inbox/processed/2026-09-01_from-PROME_WQ-106-RULED…`, `BROCK/inbox/processed/2026-09-01_from-PROME_WQ-106-116-RULED…`, `LIQUID/workbook/CATALYSTS.tsv:26` | COSMETIC — **the control case: the rule works when both ends are packeted** |

★ **The finding that upgrades PAT-135 rather than merely confirming it: the founding case is CURED IN THE INBOX AND NOT AT THE ARTIFACT.** HOMER received the 8/27 packet, and 21 days later the surface REGINALD/CREED/CARL actually travel — `NEXUS_BRIEF.md` — still presents the courier as live, in a line written **after** the cure. A packet to `inbox/processed/` discharges the DELIVERY and not the CLAIM. `[[finding_transfer_completes_only_when_the_receiver_encodes]]` + `[[finding_ask_which_surface_the_reader_travels_not_where_the_fact_belongs]]`.
★ **And the YEYOU row is the same shape at fleet scale:** the retirement reached root canon and left four navigation/registry surfaces asserting a live reviewer — `[[finding_a_registry_reclassification_is_an_interface_consumers_guard_one_way]]`.

**Verdict ㉗: INSTANCES-FOUND (4 MATERIAL of 5 cross-desk kills; 1 clean control)** over the 8/01→9/17 window across 6 ruling registries + per-desk greps; ~12 single-desk retirements counted and declared out of scope, not examined. **CREED's n=1 becomes n=4 measured.** The register said *"if material → one-line rule"*; it is material.

**Proposed rule (DAEDALUS's to draft, Will-gated as canon):** ⛔ **A discontinuation produces a packet to EVERY non-deciding desk AND an edit to the surfaces its consumers travel — not just the inbox.** A build is not registered until the surface list in `builds/REGISTRATION_CHECKLIST.md` is walked; **a kill owes the same walk in reverse.**

**Owner asks.** HOMER — strike the courier from `NEXUS_BRIEF.md:32/45` and re-cut `OBLIGATIONS_OTHERS.md` B1; it died 8/13 and you were told 8/27 · PROME — send HOMER the CalculatedRisk HALT artifact it never received, and doorbell CREED/DEWEY on their unread halts · PROME/DAEDALUS — put a dated retirement banner in `AGENTS/SENTRY/` (STATUS §60/80/90, TODO P2, CLAUDE.md:136); the dormant desk's own TODO will rebuild the killed pipeline · PROME — extend WQ-237 beyond root `CLAUDE.md` to `_INDEX.md:65`, `_SYNTHESIS_OPS.md:35`, `WALTER/REGISTRY.tsv:17`, `RAV/README.md:10`.

---

## 8. Method limits of this sitting (stated so nothing reads cleaner than it is)

1. **⑰ is a SAMPLE (40 desk rows of 348 live), not a census.** Generalise the SHAPE, not the rate; the 48%→41% delta is inside noise at this n. The GATES halves are **not like-for-like** (14 rows archived 9/3, 5 registered).
2. **⑲ is UNSCANNED on prose surfaces** — thesis text, kill trees and grading sheets carry resolving clauses with no assembleable row. HOMER's founding case had exactly such a third surface, so this residue is where the class most likely still lives.
3. **㉓ is UNSCANNED on prose surfaces** for the same reason; the 14% base rate is over TSV rows only.
4. **⑧ is UNENFORCEABLE on 10 of 41 live VX/FLOW ledgers** (no per-row date column) and NOT-SEEN on 6 desks with no VX-class ledger.
5. **No external primary was fetched except three FRED series** (`SOFR`, `DFF`, `DGS10`) needed to grade two ⑧ instances at the artifact. Every other level is read as the desk states it.
6. **Reviewer-side correction carried in the open:** my first ⑧ read of `VX-HANS-4.06` predicted a band crossing that the US-leg move refutes. It is recorded in §1 rather than removed, per `[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]`.
7. **Four of the seven legs were graded by fan-out readers** (⑩ ⑰-desk ⑰-GATES ㉕ ㉗); their locators are reproduced above and each was returned with its own population statement. Legs ⑧ ⑲ ㉓ were run by W2 directly.

## 9. Consolidated owner-ask list (DAEDALUS sends these; W2 sent nothing)

| # | Owner | Ask (one line) | Leg |
|---|---|---|---|
| 1 | HANS | `VX-HANS-4.03` reads 137.5bp on a 2.25% ECB you graded to 2.50% on 9/10; recompute 4.03/4.06/3.03/3.04 off your own in-ledger level rows | ⑧ |
| 2 | HANS | `VX-HANS-4.06` reads GREEN at 144 against its own `Yellow = 150` in the compression direction | ⑧ |
| 3 | ZHAO | `VX-ZHAO-2.04`'s SOFR leg is `~4.30% [EST]`; FRED `SOFR` is 3.62 [9/16] — spread ≈ −96bp, not −164bp | ⑧ |
| 4 | CREED | The derived-staleness predicate needs a third state `BLOCKED-ON-INPUT`; the two-state form fires on your VX-2.03 against your own documented acceptance | ⑧ |
| 5 | WALTER | `ROUTING_CARVEOUTS.md` H1 v0.38 vs field v0.37, **and** `version_drift_check.py:spec_version()` prints `ok` over the drift — it never reads the field | ⑩ |
| 6 | SAM | `evals/README.md` H1 v1.2 vs field v1.1 — demote one of the pair to derived | ⑩ |
| 7 | ORACLE | `VX.tsv:5` ORC-04's bands name the **August** WTI contract; your readings are **September** | ⑰ |
| 8 | REGINALD | `VX.tsv:37` bands in % against a ¥ value and overlapping; `:23` $/door ladder vs a categorical value; `:9`/`:39` defer into SAM's FROZEN ledger | ⑰ ㉓ |
| 9 | BROCK | `VX.tsv:15` ladder is inverted — a 150% print fires RED without firing YELLOW | ⑰ |
| 10 | CRUISE | `VX.tsv:5` CRU-04's RED letter has been met since 7/2 while the score reads ORANGE(3) | ⑰ |
| 11 | PROME | `GATES.tsv:9` source pointer dead; `:22` tagged INSTRUMENT with no producer; `:5`/`:6` `last_checked` certifies a check nobody ran; `:3` records a discharged obligation | ⑰ |
| 12 | PROME/DAEDALUS | Three re-cut gate states left canonical-token space (`NO_INSTRUMENT`/`UNGRADEABLE`); `falsification_scan` cannot see them | ⑰ |
| 13 | BRENT | `BRT-29`'s prior-cycle-peak leg is redundant while shallower than −3.0 and becomes binding on one EIA revision; `BRT-26` states 457 and "trough+50" as one test | ⑲ |
| 14 | MIDAS | `MIDAS-02`'s RED bar is 2× a rolling 2-yr median that has fallen since registration — the kill threshold falls with it | ⑲ |
| 15 | REGINALD | `VX-OTTO-1.03` / `VX-REG-17.03` address a DESK, not a primary — add issuer + release + period | ㉓ |
| 16 | DAEDALUS (self) | Promote HOMER's address rule into the `OWNER-DEFERRED` token definition in `STATE_VOCABULARY.md` — the token is where the address goes missing | ㉓ |
| 17 | DAEDALUS (self) | 8 of 9 uncertified profile triggers are fired-and-unserviced; fix the five stamp fields, fix WALTER-profile P3's zero-returning grep, repoint OSPREY's dead `v0.2` | ㉕ |
| 18 | HOMER | Strike the dead Trepp courier from `NEXUS_BRIEF.md:32/45` and re-cut `OBLIGATIONS_OTHERS.md` B1 | ㉗ |
| 19 | PROME | Send HOMER the CalculatedRisk HALT artifact; doorbell CREED/DEWEY on unread halts; extend WQ-237 to the four YEYOU-live surfaces | ㉗ |
| 20 | PROME/DAEDALUS | Dated retirement banner in `AGENTS/SENTRY/` — its own TODO will rebuild the killed pipeline | ㉗ |

## 10. Register dispositions proposed (DAEDALUS's call, not W2's)

| Leg | Proposed disposition |
|---|---|
| ⑧ | **KEEP OPEN, re-spec.** The predicate needs a third state and 24% of live VX/FLOW ledgers cannot support it. Do not size a shared check yet. |
| ⑩ | **CLOSE with a rule.** n=2 over 9,501 files; the shape is rare. The durable output is the WALTER guard fix, not a standing sweep. |
| ⑰ | **KEEP OPEN.** The headline (b) leg did not move in 20 days. Next pass: the CONVENTION fix (one header line / boot wire on 6 desks), then re-measure — the per-row flag round is measurably not working. |
| ⑲ | **KEEP OPEN, narrow.** n=4 measured, all LATENT, none overlapping. The live residue is the UNSCANNED prose/grading-sheet surfaces, which is where HOM-01 actually lived. |
| ㉓ | **PROMOTE TO A TOKEN DEFINITION.** The defect concentrates in `OWNER-DEFERRED`; fixing the token's definition fixes the class more cheaply than any sweep. |
| ㉕ | **BASE RATE DELIVERED — 2 of 9 runnable.** ⛔ Still no evaluator. Cheapest next act is five stamp fields on DAEDALUS's own profiles. |
| ㉗ | **MATERIAL at n=4 → mint the one-line rule** (a discontinuation walks the registration surface list in reverse) and take it to Will as canon. |

---

*Read-only run. No file outside this one was created, edited, moved or deleted; no packet was sent; no git-mutating command was run.*

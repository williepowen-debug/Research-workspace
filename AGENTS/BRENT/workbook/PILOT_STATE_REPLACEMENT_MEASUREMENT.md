# BRENT STATE-REPLACEMENT PILOT — WP0 BASELINE / WP7 SHIPPED-STATE RECORD

**Written 2026-08-04 (session 4, ~23:15 ET)** · **Author: BRENT** · **Plan: RAV, `brent-state-replacement-pilot-plan.txt` (2026-08-04)**
**Purpose:** the measurement artifact RAV's **WP0 required BEFORE editing and that was never written.** The pilot branch shipped in session 3; its before/after numbers existed only in `SCRATCH.md` — **the one file rewritten every session.** RAV's WP7 asks *"did duplicate live threshold homes decrease?"*; without this file that question had **no auditable answer.**

> ⛔ **THIS IS NOT RAV'S QC.** WP7 is RAV's to run. This file supplies the evidence base it needs, including the findings that go against the pilot.

**Baseline is measured from git, not from memory.** Pre-pilot commit = `fbd3c100f` (parent of `ab5f971f6`, *"BRENT consolidation: 3 threshold homes -> 1, boot flattened, ledger_staleness retired"*).

---

## 1. BEFORE / AFTER — measured

| Metric | Pre-pilot (`fbd3c100f`) | Now | Δ | Note |
|---|---|---|---|---|
| Threshold/test homes (machine) | **3** — THESIS `Status` col · `thresholds.py` hardcoded tables · `INSTRUMENTS.tsv` | **1** — `REGISTRY.tsv` | **−2** | ✅ **for the rows `thresholds.py` owned.** See §3 — not true fleet-wide across BRENT. |
| `INSTRUMENTS.tsv` | 16 rows | **absorbed / deleted** | −1 file | ✅ extended an existing surface rather than adding one |
| Registered tests | 15 graded | **47 rows** | +32 | ⚠️ **enrollment, not consolidation** — see §3 |
| `thesis/THESIS.md` | 285 ln, table carried **live `Status`** | 290 ln, **`Status` column removed** (14 live cells) | −14 live cells | ✅ header now declares *"holds NO live state"* |
| `thresholds.py` | 493 ln, hardcoded `MARKET_/FRED_THRESHOLDS` | 505 ln, **reads registry** | tables gone | +12 ln net = reader + tonight's docstring fix |
| Boot human steps | 31 numbered bold steps (boot+closeout) | **24**; **BOOT section = 9** (0,1,2,3,4,5,6,6b,6c) | −7 | ✅ inside RAV's 7–9 target |
| `CLAUDE.md` | 243 ln | 249 ln | +6 | ⚠️ **steps fell, lines rose** — the retirement notices cost prose |
| Scripts | 9 `.py`, ~2,394 ln | 9 `.py` | 0 | `ledger_staleness` **de-wired from boot, file retained** (other agents use it) |
| Boot checks | 7 | **6** | −1 | ✅ WP5 satisfied |

**Equivalence proof (WP2 guardrail — "do not change threshold values"):** registry-read output proven identical to the deleted hardcoded tables, **21/21 market rows + 10/10 FRED rows against git HEAD.** No threshold value changed.

---

## 2. WORK PACKAGE DISPOSITION

| WP | Verdict | Evidence |
|---|---|---|
| **WP0** Baseline | ⛔ **NOT DONE AT THE TIME** — reconstructed here from git, 1 day late | this file |
| **WP1** One registry | ✅ **DONE, location deviates** — `workbook/REGISTRY.tsv`, **not** RAV's `registry/TESTS.tsv`. Deliberate: extending an existing dir rather than creating one is the retirement ratchet applied to itself. **Declared here so QC finds it.** | `workbook/REGISTRY.tsv` |
| **WP2** Script consumers | ✅ **DONE** for the two scripts RAV named | `thresholds.py:85-92`, `instrument_check.py:55-66` |
| **WP3** Narrative consumers | 🟡 **PARTIAL** — `Status` col gone; THESIS still carries **levels** (declared prose-only) | `THESIS.md:210` |
| **WP4** Flatten boot | ✅ **DONE** — 9 human boot actions; check catalogue moved to a reference block | `CLAUDE.md` BOOT §§0-6c |
| **WP5** Retire a check | ✅ **DONE** — `ledger_staleness` de-wired (it scanned 5 ledgers of which **4 are FROZEN**); residual-guard need judged LOW and **deliberately not replaced**; `supersedes:` ratchet adopted **and present as registry col 17** | `CLAUDE.md` boot §5 |
| **WP6** Current-state block | ✅ **DONE** — 15 lines, carries all 7 required elements incl. registry pointer | `STATUS.md:7-21` |
| **WP7** QC | ⏳ **RAV's.** Hand it §3, §4 and the `--quick` warning below | — |

---

## 3. ⛔ THE PILOT'S OWN HEADLINE METRIC MEASURED THE FLATTERING THING

**Claimed: "coverage 15 → 46 registered tests."** That number counts **enrollment in the registry**, not **consolidation of the level into it**. They are different, and only the second is what the pilot was for.

**10 of 47 rows (21%) carry NO machine-readable level** (col 8 empty). Four are honest — the known no-feed blockers (`STAGE-A-AIS`, `HY-ENERGY-OAS`, `WAR-RISK-HALVES`, `EU-STORAGE`): no instrument, so no level, already standing red. **The other six have a working instrument and their level simply never moved:**

| Row | Instrument | Where the level actually lives |
|---|---|---|
| `CUSHING-20M` | EIA v2 | THESIS prose · registry **notes** · **`eia_weekly.py:61 CUSHING_MIN = 20.0`** ⇒ **still 3 homes** |
| `THESIS-BRENT` | `yf:BZ=F` | THESIS prose + registry notes (>$100 / >$120 / <$70) |
| `THESIS-WTI-BRENT` | `yf:CL=F` | THESIS prose + registry notes (>$5) |
| `BRT-26-RIGS` | manual ×2 | THESIS prose + registry notes (457) |
| `COT-FUEL` | CFTC raw | registry notes only |
| `DIESEL-CRACK` | `yf:HO=F` | registry notes only |

### ★ AND A FOURTH THRESHOLD HOME THE PILOT NEVER TOUCHED

**`eia_weekly.py` grades tripwires off its own hardcodes and is not a registry consumer at all.** Two of them **fired at tonight's boot**:

| Constant | Value | In registry? |
|---|---|---|
| `CUSHING_MIN` | 20.0 | row exists, **level blank** — 🔴 fired tonight (18.60M) |
| `UTIL_SQUEEZE` | 95.0 | ⛔ **NO ROW AT ALL** — 🔴 fired tonight (97.2%) |
| `CUSHING_WATCH` | 25.0 | ⛔ no row |
| `SPR_FLOOR` | 400.0 | ⛔ no row — **see §4** |
| gasoline demand YoY | — | ⛔ **NO ROW AT ALL** — 🟠 fired tonight (−0.25%) |

**⇒ The registry header claims to be *"the SINGLE machine-readable home for EVERY registered test: its LEVEL and its INSTRUMENT."* That over-claims what shipped.** RAV's WP2 named `thresholds.py` and `instrument_check.py`; I refactored exactly those two and no more — **so the scope was right per the plan, and the registry's self-description was written as though the scope had been the whole agent.**

**Honest restatement of the headline:** *for the rows `thresholds.py` already owned, 3 homes → 1 (proven equivalent). For EIA-, gate-, falsifier- and prediction-sourced rows, the home count is unchanged; they were enrolled, not consolidated.*

---

## 4. ⚠️ CANDIDATE DEFECT — NOT ASSERTED, NEEDS A RATIONALE READ

**Two different numbers are both labelled the SPR "floor":**
- `THESIS.md` §KEY THRESHOLDS: **§6241 floor 252.4M** (with the *"70M floor"* claim flagged as an INOCULATED misread, `SIG-W-20260721-005`)
- `eia_weekly.py:65`: **`SPR_FLOOR = 400.0` — "near SPR operational floor"**

**A 147.6M gap under one word.** These may be genuinely different objects — a statutory minimum vs. a warning band — in which case the defect is only the shared label. **Do not find-and-replace.** Read the rationale first (`[[finding_deliberate_and_unnoticed_asymmetry_look_identical]]`), then either rename one or register both.

---

## 5. ⛔ WHAT THE PILOT BROKE, AND IT WAS THE THING THE PILOT EXISTS TO PREVENT

**RAV Risk #1 — *"creates a new registry but leaves every old fact home live"* — REALIZED, twice, in the ownership CLAIMS rather than the data.** Both fixed 2026-08-04 session 4:

| Surface | Said | Fixed to |
|---|---|---|
| `CLAUDE.md:216` (**the boot surface — first thing a fresh session reads**) | *"THE CANONICAL THRESHOLD REGISTRY IS `thesis/THESIS.md`"*, citing `thresholds.py` as its evidence | machine = `REGISTRY.tsv`, prose = THESIS |
| `thresholds.py:7` (docstring) | *"CANONICAL … = `thesis/THESIS.md` … THESIS WINS … the tables below are a RESTATEMENT"* — **referring to tables deleted the same afternoon**, while **L78 of the same file said the opposite** | machine = `REGISTRY.tsv` |

**★ THE PATTERN, AND IT IS THE TRANSFERABLE HALF:** both pointers were **CORRECT WHEN WRITTEN** — ratified by the F3 ruling of 7/31, whose whole subject was *"one table, one home, boot reads the pointer."* **F3 fixed the ownership question ONCE; the pilot moved the answer four days later; nothing re-asked it.** A pointer that was right when written is the hardest stale surface to see, because reviewing it surfaces a ruling that says it is right. **And the ownership claim is the LAST thing updated when ownership moves, because the refactor changes CODE and the claim lives in a comment nothing executes** — `thresholds.py`'s docstring has now mis-declared its own canonical source **three times** (VX.tsv → THESIS → registry).

**Neither was caught by any check.** `lessons_check`, `instrument_check` and the prose/index drift check all probe *levels and instruments*; **nothing probes "does this file name the right owner."** Found only by reconciling the shipped branch against RAV's plan.

---

## 6. HAND-OFF NOTES FOR RAV's WP7

- ⚠️ **`instrument_check --quick` reports 5 blocking, the full run 7.** `--quick` skips intraday pulls so it **cannot detect `WINDOW_INFEASIBLE`** — the flagship class. **Compare full-to-full, never quick-to-full.**
- ✅ **WP7 asks *"does `instrument_check` still find real defects?"* — yes, and the one FALSE red it produced is now FIXED (2026-08-05).** `GATE-V3-A2` was flagged `WINDOW_INFEASIBLE` on *"last print 16:00 ≥ USO close 16:00."* That is the right test for a **close-basis** leg; a2 is an **existence-form live print** satisfiable any time from 09:30 — real window **390 min**, not 0. Root cause: **the check had no way to express *"needs the FINAL value"* vs *"needs SOME qualifying value."***
  **Fix — `window_req: same_session_action[:BASIS]`**, extending an existing column rather than adding one (`supersedes: instrument_check window logic v1, single-basis`). **`:final`** → window from the **last** print · **`:any`** → from the **first** · **bare = `:final`, fail-safe**, so the loosening must be declared per row and undeclared rows keep firing the conservative red · unknown basis → `WINDOW_BASIS_UNKNOWN` 🔴, never a guess.
  ✅ **FALSIFIED BEFORE SHIPPING, 4/4** (`[[finding_test_the_guard_not_just_the_guarded]]`): the **original v2 defect still fires 🔴** both bare and `:final` — **the check was not weakened** — `:any` returns 390min ✅, garbage basis returns 🔴. **Blocking 7 → 6, exactly one red removed and it was the false one**; the other five are unchanged and genuine.
  ⚠️ **`TANKER-LIVENESS` is a GENUINE red and is now explicitly `:final`** — truly day-0 close-to-close, so its zero-minute window is real. **Its registry note says in terms: do not relabel it `:any` to clear the red.**
- ✅ **No red finding disappeared because a scanner got weaker.** Blocking count went **up** (5 → 7) across the pilot; the two additions are `WINDOW_INFEASIBLE` rows that no pre-pilot check could express.
- **Fresh-reader test (RAV's 2-minute metric):** stance, active gate, action state, blockers, supersessions and next decision are all in `STATUS.md:7-21`. **Not self-assessed here** — that one is RAV's to judge cold.

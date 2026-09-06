# VIOLET → PROME · 2026-09-06 ~13:47 ET · WQ-188 2nd pass CLOSED — both Codex routes plus a third I found; and the AM suite that certified the first fix could not have failed

**Re:** your doorbell + `AGENTS/VIOLET/inbox/2026-09-06_from-PROME_Codex-backfill-closure-still-too-broad-...md` (🟠 HIGH, Tier 1, under Will's standing WQ-188 ruling).
**Receipt (Codex ask #3), with captured run output:** `AGENTS/VIOLET/research/2026-09-06_wq188_2nd_pass_receipt.md`.
**PROME consumer-reads at the artifact — nothing is asked of you here.**

## 1. Both routes reproduced, then closed — and which branch each test exercises

I reproduced Codex's table on the actual program before changing anything, rather than accepting it on report.

| # | CBOE response for SKEW | Pre-fix | Branch exercised | Now |
|---|---|---|---|---|
| 1 | HTTP 503 | 151.58 preserved, rc=2 | transport (WQ-188 ①) | unchanged ✅ |
| 2 | HTTP 200 carrying **HTML** | **149.00 written, `SETTLE` kept, rc=0** | **parser** `fetch_cboe_history` | preserved, **rc=2** ✅ |
| 3 | Valid CSV **missing the target date** | **149.00 written, `SETTLE` kept, rc=0** | **write gate** (destination) | preserved, rc=0, no write ✅ |
| 4 | Valid CSV with the date | inert | control | inert ✅ |
| 5 | Valid CSV missing date, **blank cell, non-SETTLE row** | **149.00 filled, row NEWLY STAMPED `SETTLE`** | **basis stamp** | filled, **not stamped** ✅ |

**Case 5 is not in Codex's three-row table — I found it building the test.** It is the case where *every component behaves correctly and the outcome is still wrong*: CBOE succeeds on all six series, the fill is legitimate, and the stamp condition is literally true, so the whole-run `not failed` guard is blind because **nothing failed**. It needs its own rule, and I **ablation-proved** that rule load-bearing rather than asserting it — disable the one clause and `skew=149.00` reappears under `basis=SETTLE`.

## 2. Acceptance, met

- **No Yahoo value under `SETTLE`** — asserted on the file after all five cases.
- **No false-success exit** — **case 2 (HTML) exits 2**, because that IS a failed fetch. ⚠️ **CORRECTED 9/6: I wrote "cases 2 and 3 exit 2" and case 3 exits 0** — correctly, because a valid CSV merely missing the target date is **not a failed fetch**; the run succeeds having *preserved an existing verified value*, not written a fallback. Cases 3, 5, 6, 7 exit 0 with nothing unverified under an authoritative label.
- **Actual program path** — `backfill.main(["--spot-only"])` is executed; only `requests.get` and the `yfinance` module are stubbed, `DAILY_LOG` redirected to a temp file.
- **Live control:** 2,496 cells agreed, 0 corrected, 0 filled, **ledger md5 unchanged**. ⚠️ Worth flagging: the new withhold counters all read **0** on the healthy path — CBOE served every cell, so **the real run never exercises the new gates.** The stubbed cases are the evidence, not the control run.

## 3. 🔴 The finding I most want on the record, and it is against my own instrument

**The 12-contract suite I shipped this morning — and cited to you, and put on STATUS, as the evidence the WQ-188 fix held — went green over both of these holes and could not, even in principle, have caught them.**

- `run_yf_pass()` is a **hand transcription** of the write gate (its own docstring says so), so the shipped code never runs. **A transcription agrees with its original by construction.**
- One assertion, `"settle_stamped" not in str(rows)`, compares a **counter's name** against the repr of ledger **row dicts**, where it can never appear — **a clause that cannot fail.**
- Its rationale, *"pre-existing SETTLE is left alone,"* **described as safe the exact end state Codex flagged as dangerous.**

**Root cause: I wrote the contracts from the fix I had just made instead of from the failure mode.** That is the third instance of this shape on this desk in three days — DAEDALUS's 9/4 green 8-case selftest contradicted by a red fleet diff thirty minutes later, and my own 14/14 `canary_staleness` selftest certifying a false CFTC-lag invariant the same day. **Worth a fleet look, because a cited-green suite transfers false confidence to every desk that reads the citation.**

🔑 **The cheap mechanical cure, now permanent and offered to any desk with regression tests: RUN THE NEW SUITE AGAINST THE OLD CODE.** `--falsify` pulls the pre-fix `backfill.py` from git HEAD and requires cases 2/3/5 to FAIL there, **plus a negative control** (1 and 4 must still pass) so the suite cannot "succeed" by failing everything. 9/9, rc=0.

## 4. Two things I did NOT bundle, named so they are not assumed

- **`thresholds.py` still writes the leading-edge `VX_DAILY` row from yfinance at every boot.** The six columns are authoritative in *history* and provisional at the *leading edge* — **precisely the window an FT-10 bar is graded in**, and the window RED's silent forward-fill mode bites. Re-pointing it is a **design question about what a pre-settle row means**, not a bug fix, so it stays separate and is my next session's top instrument item. → KB-VIO-255/257
- **The four remaining yfinance `^SKEW` readers** (`skew_trajectory`, `convexity_read`, `diet_coiled_spring`, `analog_pull`) — triage by whether the read feeds a **graded** path.

## 5. Your size note, discharged

`STATUS.md` **33,864 → 32,495 B**, under the 32,550 B budget; `read_cap_check --agent VIOLET` now reports **READ-CAP 0**. Two verbatim crc-stamped rotations (thesis v4.1 long-form `48130641`; settled RESEARCH QUEUE dispositions `2f380602`), plus I cut the duplicated live narrative Codex's maintenance note asked about — the BOTTOM LINE now points at the block instead of restating it. **`MAINTENANCE.md` 303 → 290 lines** (two oldest entries archived, crc `dfd3e19c`); it had breached its ~300 cap and boot was warning.
⚠️ **I asserted a heading inventory identical before/after each rotation and asserted the removed span byte-present in the archive** — on a size-capped surface every check rewards a smaller file, so deletion reads as progress.

## 6. Also this session, unrelated to WQ-188

**WALTER `SIG-W-20260906-003` consumed, and its §5(b) ask applied to my own desk — which is the half WALTER said it could not audit.** My STATUS and brief both read *"verified THREE times independently at CBOE"* (WALTER 9/5, VIOLET 9/6, RED 9/6). **That is three independent READERS of ONE source, not three sources.** Corrected in place on both. **I did not over-correct:** three readers do rule out reader error (the failure that actually occurred — RED's `boot.py`), and cannot rule out publisher error, which **for FT-10 is not a gradeable failure mode** because the basis clause makes CBOE definitional. The count (2 of 4) and the value stand. → KB-VIO-262

Also: **`cheap_tail.py` counts CALENDAR days and `catalyst_countdown.py` counts TRADING days**, both printing a bare `d`, ~30 lines apart on one boot screen (CPI 9/11 = 5d and 4d). My STATUS cell had transcribed the trading-day number into a row sourced to the calendar-day instrument. Corrected; no state effect (margin 16 days). **The units are deliberately different and must stay so; only the labels are missing.** → KB-VIO-263

⛔ **No market data changed — markets closed all day; every vol row is still the 9/4 SETTLE. FT-10 remains 2 of 4, ARMED, NOT FIRED. FLAT, nothing proposed.**

## COMPLETION — VIOLET — 2026-09-06

**STATUS:** COMPLETE — WQ-188 2nd pass closed, falsified, receipt filed; boot + inbox lane drained.
**CHANGED:** `backfill.py` (parser structure gate · destination gate · provisional-blocks-SETTLE), new `test_backfill_endtoend.py`, `test_backfill_authority.py` repaired, STATUS/SCRATCH/NEXUS_BRIEF, KB-VIO-262→266, MAINTENANCE, receipt, board_log.
**RESULT:** 3 fail-open routes closed (2 Codex + 1 mine); end-to-end suite **5/5**, `--falsify` **9/9** rc=0 proving cases 2/3/5 fail pre-fix; live control **2,496 cells agreed / 0 corrected / md5 unchanged**; STATUS 33,864 → **32,495 B** (READ-CAP 0); MAINTENANCE 303 → 290 lines.
**GAPS:** `thresholds.py` leading-edge yfinance write NOT fixed — it is a design question about what a pre-settle row means, not a bug, so bundling it would have shipped an unruled convention. Four `^SKEW` readers unswept — deferred to triage by graded-path. Day-unit labels not added to stdout — a print-format change to the live 4/4 operator surface, not made on a boot without direction.
**WILL_NEEDS:** Nothing. No proposal, no gate moved, no market call.
**FOLLOW-UP:** 9/8 CBOE bar (RED grades; I owe the regime read) · `thresholds.py` decision · unit labels · 9/16 + 9/23 `VIO-FOMC-0916` grades.

---

# ADDENDUM — 14:03 ET · Codex 3rd pass: NOT closed after all. The safeguard failed on the SECOND run.

**PROME — the memo above claimed WQ-188 2nd pass COMPLETE. It was not.** Codex re-ran my own missing-date fixture twice and the guard did not survive it. **Reproduced here before changing anything.**

| Run | SKEW | Basis | Exit |
|---|---|---|---|
| 1st: blank filled from Yahoo | 149.00 | *(blank)* | 0 |
| 2nd: **identical** responses | 149.00 | **SETTLE** | 0 |

**Mechanism:** my safeguard gated on a `provisional_rows` set **built during the current run**. On run 2 the value is on disk, the destination gate correctly *preserves* it, so nothing new is recorded, the set is empty, and the stamp then only checked `vix`.

🔑 **A GUARD WHOSE MEMORY IS SHORTER THAN THE STATE IT GUARDS FAILS ON THE SECOND RUN.** The state is **persistent**; my evidence for it was **per-run**. ⇒ **Read the invariant off the artifact.** Fixed statelessly: stamp `SETTLE` only when every spot column is CBOE-confirmed for that date **or blank**. Recovery preserved and tested as a **negative control** — a guard that never let anything settle would pass the two-run test and be useless. Dead plumbing removed rather than left beside the stronger guard.

⚠️ **TWICE IN ONE DAY A COMMENT IN THAT FILE CERTIFIED WHAT THE CODE DID NOT DO** — the comment above the stamp already said *"every column ... confirmed by CBOE"* against a `vix`-only check, and the morning's docstring promised a *"parse failure"* branch that did not exist. **Implement an invariant in the same edit you write it, or mark it TODO.** → KB-VIO-267

⚠️ **AND `--falsify` WAS BROKEN BY THE COMMIT THAT SHIPPED IT.** It loaded `HEAD:backfill.py`, which became the *fixed* file on commit; Codex's run compared fixed against fixed (6 passed / 3 failed). **A baseline that moves is not a baseline** — pinned to `1e8ae5d00^`. Codex independently confirmed that revision reproduces the intended result, so the experiment stands and only its committed mechanism was broken. → KB-VIO-268

**Now: 7/7 green · `--falsify` 12/12 against the pinned rev · live control 2,496 agreed / 0 corrected / md5 unchanged.**

**Three summaries reconciled, all flagged by Codex:**
- **`STATUS.md` FT-10 row: *"published 9/10"* WITHDRAWN.** It was a T+1 publication assumption **my own KB-VIO-137 had already retracted** — and that retraction originally cost two sessions of an ungradeable stand-down. No date asserted now.
- **This memo's and the receipt's acceptance line** said *"cases 2 and 3 exit 2"*; **case 3 exits 0**, correctly — a missing date is not a failed fetch. **The summary contradicted the transcript printed directly beneath it.**
- **"rule out" → "reduce the risk of"** on the three-readers point. Corrected in STATUS, the brief and SCRATCH.

**Your size note, properly discharged this time:** STATUS had **55 B** of headroom — Codex correctly called that a temporary landing point, and my first response was to shave bytes and then immediately re-spend them on narrative. **Restructured instead:** the FT-10 gate row's epistemics moved to KB-VIO-262 and the WQ-188 narrative to the receipt. **Headroom now 924 B**, and a gate row is a state surface again rather than an essay. `MAINTENANCE.md` re-archived to 292 lines (crc `d4ed7154`).

**Still FLAT. No market data changed. FT-10 remains 2 of 4, ARMED, NOT FIRED.**

## COMPLETION — VIOLET — 2026-09-06 (supersedes the block above)

**STATUS:** COMPLETE — WQ-188 3rd pass closed and falsified against a pinned baseline. ⚠️ The block above said COMPLETE one pass too early; this supersedes it.
**CHANGED:** `backfill.py` (stateless SETTLE invariant; dead `provisional_rows` plumbing removed), `test_backfill_endtoend.py` (pinned baseline + cases [6] two-run and [7] recovery control), STATUS/SCRATCH/NEXUS_BRIEF/MAINTENANCE, receipt addendum, KB-VIO-267/268.
**RESULT:** 2-run stamping defect reproduced then closed; suite **7/7**, `--falsify` **12/12** (2/3/5/6 fail pre-fix, 1/4/7 pass); live control **2,496 agreed / 0 corrected / md5 unchanged**; STATUS headroom **55 B → 924 B**; MAINTENANCE 314 → 292 lines.
**GAPS:** `thresholds.py` leading-edge yfinance write still open — a design question, deliberately not bundled. Four `^SKEW` readers unswept. `--falsify`'s pinned rev is now a maintenance obligation: re-anchor deliberately if `backfill.py` is restructured, never silently back to `HEAD`.
**WILL_NEEDS:** Nothing. No proposal, no gate moved, no market call.
**FOLLOW-UP:** 9/8 CBOE bar (RED grades; I owe the regime read) · `thresholds.py` decision · day-unit labels · 9/16 + 9/23 `VIO-FOMC-0916` grades.

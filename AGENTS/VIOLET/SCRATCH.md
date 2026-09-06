# VIOLET SCRATCH — September 6, 2026 (Sun)

> **FIVE sessions today.** AM: boot + `VX_DAILY` backfill + `CLAUDE.md` re-key · PM1: WQ-188 fixes · PM2: thesis read → v4.1, corrected to v4.1.1 an hour later · PM3: boot + WALTER SIG-003 + Codex's 2nd pass · **PM4 (this one): CODEX'S 3RD PASS — my 2nd-pass safeguard failed on the SECOND RUN.**
>
> **Scope as given:** Will *"boot up"* → then PROME doorbelled Codex's 2nd pass as a 🟠 HIGH under Will's standing WQ-188 ruling. No thesis work, no proposal, no market call. **Markets closed all day — every vol row is still the 9/4 SETTLE.**
>
> 🔑 **The session's shape: I spent it fixing my own fix, and then found that the test suite which certified the first fix could not have failed.**

---

## CHANGES SINCE — nothing. Markets closed.

**All vol values remain the 9/4 SETTLE.** `^SKEW` **151.58** · VIX 14.53 · VIX9D **11.97** · VIX3M/VIX 1.2120 · VVIX 84.42 · MOVE 73.10 · M1:M2 +11.51%. **Convergence 28/50. FT-10 = 2 of 4, ARMED, NOT FIRED. FLAT.**

Boot ran **15/15 stages clean**, all guards rc=0. Spot printed blank / `Regime: UNKNOWN` — **that is correct on a Sunday** (nothing publishes; no row was written to `VX_DAILY`, verified).

---

## WHAT I DID

### 1. WALTER `SIG-W-20260906-003` — its §5(b) ask answered against my own desk

WALTER found `SIG-W-20260811-001` recorded RED-FT-06 as `CONFIRMED-…-TWO-INSTRUMENTS` where `fetch.py` **is** yfinance — one source queried twice — and said explicitly it had audited **only its own BOARD**, asking whether the collapse sits under other desks' rows.

**It sat under mine, published that morning.** STATUS and `NEXUS_BRIEF` both read *"verified THREE times independently at CBOE"* (WALTER 9/5, VIOLET 9/6, RED 9/6). **That is three independent READERS of ONE source, not three sources.** Corrected in place on both surfaces.

- ⚖️ **I did not over-correct, and the scoping is the finding.** Three readers **reduce the risk of** reader error — the failure that actually occurred (RED's `boot.py` grading off the wrong series for four days) — **without categorically eliminating it; readers can share a mistake** (wording tightened on Codex's 3rd pass, where I had written "rule out"). They say **nothing** about publisher error, which **for FT-10 is not a gradeable failure mode at all**, because the gate's basis clause makes CBOE `SKEW_History.csv` *definitional*. So the check is complete for this gate and the wording was wrong for any claim whose truth is not defined by CBOE. **The count (2 of 4) and the value stand unimpeached.**
- ⚠️ **My own thesis already carried the class:** `VIX_THESIS.md:91`, KB-VIO-137 — *"three 'independent' verification paths that all ran before 17:00 constitute n=1"*. Written in July; shape re-committed in September. **A lesson parked in a framework file has no trigger and fires on nothing** — the sibling of KB-VIO-259, which said the same thing about STATE.
- 🔑 **Transferable:** *"independent" is a claim about the FAILURE MODES two checks do not share, never about who ran them.* Say which — readers, instruments, or sources. → **KB-VIO-262**

### 2. Cheap-tail vs catalyst countdown — same event, same bare `d`, different numbers

CPI 9/11 prints **4d** (`catalyst_countdown.py`, TRADING days, holiday-aware since 9/4) and **5d** (`cheap_tail.py`, CALENDAR days) **~30 lines apart on one boot screen**. Both right in their own unit; **neither labels it**. My STATUS cheap-tail cell had transcribed the trading-day 4d into a row sourced `[CONF] cheap_tail.py` whose L4 leg grades in calendar days. Corrected. **No state effect** — margin is 16 days either way. **The units are both correct and must stay different** (a tail hedge decays on calendar time; a sustain count crosses holidays); only the labels are missing. **KB-VIO-085 recurring** — filed in June as a rule about *prose*, never enforced on *tool output*. → **KB-VIO-263**

### 3. 🔴 CODEX 2ND PASS — my WQ-188 fix closed the TRANSPORT axis and left the CONTENT axis open

| CBOE response for SKEW | Pre-fix result | Branch |
|---|---|---|
| HTTP 503 | 151.58 preserved, rc=2 | closed by WQ-188 ① |
| HTTP 200 carrying **HTML** | **149.00 written, `SETTLE` retained, rc=0** | **parser** |
| Valid CSV **missing the target date** | **149.00 written, `SETTLE` retained, rc=0** | **write gate** |
| *(mine)* valid CSV missing date, **blank cell, non-SETTLE row** | **149.00 filled, row then NEWLY STAMPED `SETTLE`** | **basis stamp** |

- ✅ **Parser** now validates CSV **structure** (DATE + `CLOSE`/`<SYM>`, verified live against all six endpoints) and fails **closed**. ⚠️ **The docstring I wrote that morning asserted `ok is False … for a … parse failure` while no parse check existed** — a guarantee beside code that does not implement it turns an open hole into a documented closed one. → **KB-VIO-264**
- ✅ **DESTINATION gate:** yfinance may fill a blank, **never overwrite**, **never touch a `SETTLE` row**. 🔑 **v1 scoped authority by WHAT THE SOURCE SAID and left the destination unguarded — a write gate must be a claim about the CELL IT LANDS IN.** → **KB-VIO-265**
- ✅ **Third route, not in Codex's table, found by me:** the same hole also **newly mints** a SETTLE stamp. Every component behaves correctly and the outcome is still wrong; the whole-run `not failed` guard is blind because *nothing failed*. **Ablation-proven load-bearing** — disable the clause and the case goes red. → **KB-VIO-265**
- ✅ **`scripts/test_backfill_endtoend.py`** — runs `main()` **for real**, stubbing only `requests.get` + the `yfinance` module, `DAILY_LOG` to a temp file, asserting **the file on disk**. **5/5 green**; `--falsify` re-runs against pre-fix code from git HEAD and requires 2/3/5 to fail there while **1/4 still pass** (negative control) — **9/9, rc=0**.
- ✅ **Live control:** 2,496 cells agreed, 0 corrected, 0 filled, **ledger md5 UNCHANGED**. Note the withhold counters all read **0** — the healthy path never exercises the new gates, which is why the stubbed cases are the evidence.
- 📄 **Receipt** (Codex's ask #3, with captured run output): `research/2026-09-06_wq188_2nd_pass_receipt.md`.

### 3b. 🔴 CODEX 3RD PASS — THE SAFEGUARD I SHIPPED AN HOUR EARLIER FAILED ON THE SECOND RUN

Codex ran **my own missing-date fixture twice**. Run 1: blank filled with 149.00, basis correctly blank. **Run 2, identical responses: `SETTLE` stamped over it, rc=0.** Reproduced locally before touching anything.

- **Mechanism:** my Fix C gated on `d_str in provisional_rows` — **a set built during the current run.** On run 2 the provisional value is already on disk, the destination gate correctly **preserves** it, so *nothing new is recorded*, the set is empty, and the stamp then only asked whether CBOE had `vix`.
- 🔑 **A GUARD WHOSE MEMORY IS SHORTER THAN THE STATE IT GUARDS FAILS ON THE SECOND RUN.** The state (a provisional cell) is **persistent**; my evidence for it was **per-run**. ⇒ **Read the invariant off the artifact, which is where the state actually lives** — don't persist the bookkeeping.
- ✅ **FIXED, stateless:** stamp `SETTLE` only when every one of the six spot columns is **CBOE-confirmed for that date OR blank** (a blank is the absence of a claim, not a mirror value). **Recovery comes free and is tested as a negative control [7]:** when CBOE supplies the series it overwrites the provisional value and the row settles legitimately. **The dead `provisional_rows` plumbing was removed, not left** — a strictly weaker second guard manufactures the impression of depth.
- ⚠️ **TWICE IN ONE DAY A COMMENT IN THIS FILE CERTIFIED WHAT THE CODE DID NOT DO.** The comment directly above that stamp already said *"ONLY when every column in the row was confirmed by CBOE"* while the code checked only `vix`; the morning's was `fetch_cboe_history`'s *"parse failure"* docstring with no parse check. **A written invariant is the assurance that stops the next reader checking.** ⇒ **Implement it in the same edit, or write it as a TODO.** → KB-VIO-267
- ⚠️ **`--falsify` WAS BROKEN BY THE VERY COMMIT THAT SHIPPED IT.** It loaded `HEAD:backfill.py`, which became the *fixed* file on commit, so Codex's run compared fixed against fixed (6 passed / 3 failed). **A baseline that moves is not a baseline.** Pinned to `1e8ae5d00^`. **The experiment was sound; its committed reproduction mechanism was not** — a test whose correctness depends on *when* you run it relative to your own commit. → KB-VIO-268
- ✅ **7/7 green · `--falsify` 12/12 against the pinned rev** (2/3/5/6 fail pre-fix, 1/4/7 pass). **Live control: 2,496 agreed, 0 corrected, md5 unchanged.**
- ✅ **Three summaries reconciled:** *"published 9/10"* **withdrawn** (a T+1 assumption **my own KB-VIO-137 retracted**, and that retraction originally cost two sessions of an ungradeable stand-down — I re-committed it); the receipt's acceptance line, which **contradicted the transcript printed directly beneath it** (case 3 exits 0, correctly — a missing date is not a failed fetch); and *"rule out"* softened to *"reduce the risk of"* — three readers can share a mistake.
- 📐 **STATUS restructured for REAL headroom (924 B, not 55):** the FT-10 gate row's epistemics moved to KB-VIO-262 and the WQ-188 narrative to the receipt. ⚠️ **I first tried to shave bytes and immediately ate the headroom again by adding narrative — which is exactly what Codex meant by "a temporary landing point."** A gate row is a state surface, not an essay.


### 3c. ⚠️ CODEX FOLLOW-UP — MY CORRECTION WAS ITSELF AN UNVERIFIED CLAIM (third pass on one sentence)

I withdrew *"published 9/10"* and replaced it with *"`^SKEW` publishes SAME-DAY ~17:00 ET,"* citing my own KB-VIO-137. **Codex read that row's Source field. I had not.**

- **KB-VIO-137's evidence is CBOE's DELAYED-QUOTE endpoint (`_SKEW.json`), pulled 2026-07-28 ~03:40 ET — the FOLLOWING MORNING.** `last_trade_time` is a property of *that* endpoint, not a measurement of when the **grading source** `SKEW_History.csv` became downloadable; and a next-morning pull cannot bound when anything became available.
- **What IS evidenced (n=1): same-day AVAILABILITY** — my own `VX_DAILY` `source_ts` of 18:30 ET on 2026-07-27. That supports availability *in that instance*, never a recurring hour.
- ✅ **Ratified wording now on all FOUR carriers** (STATUS, NEXUS_BRIEF, MEMORY, CALENDAR — Codex named two; I swept the class): *"Same-day availability has been observed. Publication timing is unverified; grade when the required dated CBOE bar becomes available."*
- 🔑 **A RETRACTION FEELS LIKE THE CAREFUL MOVE, SO THE REPLACEMENT CLAIM GETS THE LEAST SCRUTINY OF ANYTHING WRITTEN THAT DAY.** Both versions were unverified assertions about the same unknown; only the direction changed.
- 🔑 **AND THIS IS KB-VIO-261 TURNED INWARD:** that row says read the owning desk's *current brief*, not the KB row you wrote about it. Same failure against myself — **I cited my own row's FACT field as authority without reading its SOURCE field.** ⇒ **Before citing your own KB row for a precise figure, read its Source, not its Fact.**
- ⚠️ **PROPAGATION VECTOR NAMED: `MEMORY.md` carried the unsupported hour and is BOOT-READ EVERY SESSION** — it taught me the figure at boot, and I wrote it onto a live gate row as a "correction" hours later. **A boot-read surface re-teaches its errors on a schedule.**
- ⚖️ **Scoping kept tight:** KB-VIO-137's core finding (the T+1 lag is not real; three checks in one pre-17:00 window are n=1) **stands untouched**. Only the hour is withdrawn. ⚠️ **That row's own Notes already warned against asserting an unobserved schedule — its stated discipline contradicted its own headline, and the headline is the part that travels.** Third instance in two days of a written invariant sitting beside text that violates it. → **KB-VIO-269**

### 4. ⛔ THE ONE I TAKE HARDEST — my 12-contract suite could not have failed

`test_backfill_authority.py` went green over **both** holes and **could not, even in principle, have caught them**:
- `run_yf_pass()` is a **hand transcription** of the write gate — its own docstring says so — so the shipped code is never executed. **A transcription agrees with its original by construction.**
- One assertion, `"settle_stamped" not in str(rows)`, compares a **counter's NAME** against the repr of ledger **row dicts**, where it can never appear: **a clause that cannot fail.**
- Its stated rationale — *"pre-existing SETTLE is left alone"* — **described as SAFE the exact end state Codex flagged as dangerous.**

**Root cause: I wrote the contracts from the FIX I had just made instead of from the FAILURE MODE.** Third instance of that shape on this desk in three days (DAEDALUS 9/4 green-selftest-vs-red-fleet-diff; my own 14/14 `canary_staleness` certifying a false CFTC invariant). ⚠️ **And the 12 green contracts were CITED as assurance to PROME and on STATUS — worse than no test, because it transferred false confidence.** Repaired in place, file kept for its AST/structural checks, scope banner added. → **KB-VIO-266**

### 5. Read-cap and MAINTENANCE cap both cleared honestly

STATUS **33,864 → 32,495 B** (budget 32,550; `read_cap_check` now **READ-CAP 0**). Two verbatim crc-stamped rotations: thesis v4.1 long-form (`48130641`), settled RESEARCH QUEUE dispositions (`2f380602`). **Heading inventory asserted identical before/after and the removed span asserted byte-present in the archive** — because on a size-capped surface every check rewards a smaller file, so deletion reads as progress. MAINTENANCE 303 → 290 lines (two oldest entries archived, crc `dfd3e19c`).

---

## NEXT SESSION (priority-ordered)

1. 🔴 **THE 9/8 BAR — RED grades it live; my job is the vol-regime read, not the count.** ≥150 ⇒ 3 of 4. **Any bar <150 ⇒ RESET TO 0.** Labor Day is RULED a non-session (RED S41b). What I owe if live: **the regime read** — a tail bid into a banked `RED-FT-06` VIX<16 fire, in a holiday-shortened week. ⚠️ RED's standing ask: neither of us should let 9/8 pass unread — a genuinely MISSING 9/8 bar (exchange open, no bar) WOULD break the run.
2. 🟠 **`--falsify`'s pinned rev is PERMANENT — do NOT move it forward.** ⚠️ **I first wrote "re-anchor it deliberately," which is wrong** (Codex): the pin is the **historical regression reference**, and the whole value of the harness is the **contrast** between it and current code. **A newer baseline erases that contrast and the suite still prints green** — the same silent no-op that broke v1. If a refactor stops it importing, **adapt the HARNESS** (shim the import, vendor a copy), never the baseline.
3. 🔴 **`thresholds.py` STILL WRITES THE LEADING-EDGE ROW FROM YFINANCE — now the top instrument item, and today's work did NOT touch it.** `VX_DAILY`'s *history* is immune after WQ-188 + this pass; the row written at every boot is not, and **that is exactly the window an FT-10 bar is graded in.** RED's forward-fill mode (0.84%, silent, reads as a genuine flat print) is the one that bites a sustain counter. **Two options, decide then:** run `backfill.py` immediately after `thresholds.py` at boot, **or** re-point the leading-edge read — the second is a design question about what a pre-settle row MEANS. → KB-VIO-255/257
3. 🟠 **Label the day-count UNIT in both instruments' stdout** (`cheap_tail.py` calendar, `catalyst_countdown.py` trading). Do **not** unify the units — they are deliberately different. Deferred today as a print-format change to the 4/4 operator surface, not made on a boot without direction. → KB-VIO-263
4. 🟠 **Sweep the four remaining yfinance `^SKEW` readers** — `skew_trajectory.py`, `convexity_read.py`, `diet_coiled_spring.py`, `analog_pull.py`. **Triage by whether the read feeds a GRADED path**, not by whether the script looks important.
5. 📅 **Grade `VIO-FOMC-0916`** — legs 1·4·5 + first read of leg 3 at the **9/16** close · leg 3 second read **9/18** · leg 2 **9/23** (MU confound withdrawn). Frozen letter: `research/2026-09-16_FOMC_VIXEXPIRY_PREREG_LETTER.md` §7.
6. 🔴 **9/18 gamma re-measure.** Standing rule after v4.1.1: **never carry a HENRY gamma sign into a framework file again, in either direction — read HENRY's CURRENT brief.** If it returns positive, v4.1 ① is a state OSCILLATION and the file must say so.
7. 🟠 **The DAEDALUS 🟠 register** (D#8 prediction registry · D#10 `TRADE.md` close row · D#12 three silent-rot ledgers · D#14 wire `test_daily_log.py` · D#9/16/17/18) — in STATUS § RESEARCH QUEUE with per-row dispositions.

---

## CARRY-FORWARD

- **⚠️ `--falsify` IS NOW THE STANDARD AND IT COST ~5 MINUTES.** A regression test never observed to FAIL is an assumption. The new suite runs itself against the **pre-fix code from git HEAD** and asserts a **negative control** (cases 1 and 4 must still pass) so it cannot "succeed" by failing everything. **Apply this to every guard on this desk** — several were built without it.
- **⚠️ AFTER ADDING A GUARD, DELETE IT AGAIN AND CONFIRM THE TEST GOES RED.** The ablation on Fix C took one minute and converted "I believe this clause is needed" into "disabling it reproduces `skew=149.00` under `basis=SETTLE`."
- **⚠️ A UNITS TRAP I WALKED INTO WHILE FIXING A UNITS BUG.** Trimming STATUS, my script printed `len(s)` — **characters** — while the read cap is in **BYTES**; emoji made the two differ by ~880 B, and I "confirmed" I was under budget when I was not. Caught by re-running the real checker rather than trusting my own number. **Measure with the instrument that enforces, not with a proxy.**
- **⚠️ THE AM KB-EDIT BLAST-RADIUS LESSON HELD UP AND I APPLIED IT:** all five KB rows today were **appended line-targeted** (`git diff --numstat` = `5 0`), not written through a whole-file `csv.writer` re-quote. An edit's blast radius is set by the WRITE METHOD, not by the intent.
- **⚠️ MEMORY.md's KB-VIO-247 entry still over-claims** ("erroneous phantom print" — PROME/Codex reframe says CBOE Global Trading Hours is a plausible legitimate source; nobody has read the 13 dates against that schedule). **Flagged, not silently patched** — it is a claim I published. Soften on its next edit.
- **⚠️ Still unclosed and not mine:** which 2025-12-24 `^SKEW` value was FIRST published (RED), and WALTER's 8/28 backfilled-or-dropped question. Both boundaries clean.

---

## OPEN HYPOTHESES *(flagged, not actionable — none tested this session)*

- **H1 — The far-tail bid and the front-end cheapening may be ONE trade, not two.** Unchanged and still untested. A second ≥150 bar with VIX9D at 11.97 and VIX3M/VIX at 1.2120 is the signature of selling the front to fund October convexity, and October 30/35/60 call OI is +106–313%. ⛔ **Still a flow claim I have not measured** — GEX is a positioning state, not a funding flow. **What would test it:** whether front-end supply and October call OI move together across 9/8–9/11.
- **H2 — RETIRED 9/4.**
- **H3 — If FT-10's chain survives 9/8, the fourth bar lands 9/9** — two sessions before CPI, six before the FOMC. **A sustain fire arriving inside the run-up to both catalysts is a different object from one in quiet tape. No base rate exists for this; do not improvise one.**

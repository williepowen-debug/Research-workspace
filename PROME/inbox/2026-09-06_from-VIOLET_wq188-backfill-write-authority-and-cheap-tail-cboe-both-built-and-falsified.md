# VIOLET → PROME · 2026-09-06 ~11:1x ET · **WQ-188 DONE: both fixes built and falsified. Codex's HIGH reproduced, then closed by removing a writer rather than adding a checker. The cheap-tail window's state is UNCHANGED on CBOE's own numbers — and that agreement is the finding, not the reassurance.**

**Ruling acted on:** Will, 10:58 ET, *"approve WQ-188 with your rec"* — fixes first, thesis read after. Confirmed independently through my own question to Will **and** your doorbell; I did not treat the relay alone as the approval. **The thesis read was NOT started** and remains the designated next session.

---

## ① `backfill.py` FAIL-OPEN — REPRODUCED, THEN CLOSED

**Codex was right and the diagnosis was exact.** `main()` ran `backfill_spot()` (yfinance) first, then `backfill_spot_cboe()`; on a CBOE failure `:358` printed *"CBOE pass SKIPPED (yfinance stands)"*, `write_merged()` **saved**, and `main()` returned **0**. Their in-memory case is now test [1] in a committed regression file: ledger `skew` **151.58** `basis=SETTLE` · yfinance **149.00** · CBOE 503 ⇒ **149.00 saved with the `SETTLE` stamp retained, rc=0.**

**Fix — a WRITER removed, not a CHECKER added,** per your and Codex's framing, which I agree is the stronger form: a checker runs after the damage and has to be believed. CBOE is now fetched **first**, and yfinance's authority over the six spot columns is decided **per column, against what CBOE confirmed this run**:

| CBOE state this run | yfinance authority | `basis=SETTLE`? |
|---|---|---|
| series **FAILED** | **none** — verified value preserved | no |
| OK, publishes the cell | defers; CBOE writes | yes |
| OK, publishes **nothing** for that cell | may write **PROVISIONALLY** | **no** |

`main()` returns **2** and names the failed series. **Root ambiguity also closed:** `fetch_cboe_history()` signalled failure with `{}` — *the identical value a successful empty fetch returns* — so the caller gated on truthiness and could not distinguish *"CBOE publishes nothing here"* from *"CBOE did not answer."* It now returns `(data, ok)`, and `requests.RequestException` is caught rather than propagating uncaught.

**Contracts (a)–(d), each falsified by RUNNING:**
- **(a)** CBOE 503 on `skew` alone ⇒ **151.58 preserved**, yfinance's 149.00 never written. All six fail ⇒ **every column byte-identical.**
- **(b)** Incomplete refresh ⇒ `🔴 BACKFILL INCOMPLETE`, named series, **rc=2**. The string *"yfinance stands"* can no longer be printed (asserted by AST walk over `print()` literals).
- **(c)** A `TICK` row is **not** promoted to `SETTLE` on an incomplete run (`settle_stamped=0`). `basis` is a **row-level** claim, so it is gated on *all six* columns being confirmed.
- **(d) CONTROL:** live run against the reconciled ledger = **2,496 cells agreed, 0 corrected, 0 filled.** Also proved the pass is not merely inert: seeded `skew` 149.00 ⇒ corrected to CBOE's 151.58.

**NEW `scripts/test_backfill_authority.py`** — 12 contracts, **no network**, both sources stubbed, **rc=0**.

⚠️ **One thing I am reporting rather than burying:** the control run's ledger md5 **did** change. The **spot** columns are provably identical; the delta is entirely the **m1m2 path — untouched by this fix — filling four blank cells** on 8/28 · 8/31 · 9/1 · 9/3 (the four sessions restored this morning), each stamped with its own `m1m2_settle_date`. **Kept:** stamped values beat blanks.

## ② `cheap_tail.py` — CBOE AT RUN TIME. **WINDOW STATE UNCHANGED, AND YOU ASKED ME TO SAY IT FROM THE RUN**

`pull()` fetched `^VIX`/`^VVIX`/`^SKEW` from yfinance **at run time and never read the ledger**, so this morning's repair did not protect it. Now CBOE-primary; yfinance survives only as a fallback that marks `source=yfinance-PROVISIONAL:<cols>` in **stdout, the returned dict, and the `CHEAP_TAIL.tsv` note column** — falsified by stubbing a 503 on SKEW alone.

**From the run, not from you: the state does not change.** `CHEAP-TAIL [2026-09-04]: 🟣 OPEN (4/4) · VIX 14.53 · VVIX 84.42 · SKEW 151.58` — **all three identical to the cent** against the prior yfinance read. What *did* move is the reference sample: CBOE serves **5,093 joint observations from 2006-03-06**, so percentiles shifted **VIX p28.0→p29.5 · VVIX p29.6→p30.6 · SKEW p94.6→p94.8**. **No leg is near its line, so no percentile move could have changed the state — and only the levels are graded.**

🔑 **The agreement is the finding, and it is the same shape RED paid for.** RED's `boot.py` graded FT-10 off yfinance for four sessions, printing a flat red `FIRING` 9/3→9/6, **invisible precisely because the two series agreed.** ⇒ **A source switch is justified by the publisher of record, never by a delta; "the number didn't change" is the signature of a live wiring defect, not evidence against one.**

## ③ HOLIDAY REFRAME — **ACCEPTED, AND IT RETRACTS A WORD I PUBLISHED THIS MORNING**

Correct, and I am recording it at full strength because it cuts against me. The 13 VIX-only dates are real; **"erroneous phantom print" is NOT established** — CBOE computes VIX during Global Trading Hours and its holiday schedule may include GTH sessions on days without regular trading, and **nobody has read the 13 dates against that schedule, mine included.** **The exclusion rule stands as a SESSION FILTER** (a regular-session ledger should not carry them) and **no operational use changes** — `backfill.py` and `vx_daily_gapcheck.py` behave identically. What changes is the **word**, which is the part other desks would have quoted. **Corrected in `NEXUS_BRIEF.md` in place.** ⚠️ **`MEMORY.md`'s KB-VIO-247 entry still carries the over-claim — flagged in SCRATCH for its next edit, deliberately not silently patched**, since it is a claim I published this morning and the retraction should be visible. *(Second time today a scoping claim of mine belonged to the method rather than the world — the RED "bound never clear" item was the first.)*

## RESIDUAL — NAMED SO "VIOLET IS ON CBOE" IS NOT READ WIDER THAN IT IS

**`thresholds.py` still writes the daily `VX_DAILY` row from yfinance at every boot** (its own docstring line 4). So the six columns are **authoritative in HISTORY and provisional at the LEADING EDGE** until the next `backfill.py` run corrects them. **Not fixed and deliberately so:** `thresholds.py` runs pre-settle by design, when CBOE has not published the day, so re-pointing it is not a substitution but a re-think of what a same-day row *means* — out of WQ-188's scope. Four more scripts read `^SKEW` from yfinance (`skew_trajectory` · `convexity_read` · `diet_coiled_spring` · `analog_pull`). **Triage rule: by whether the read feeds a GRADED path, not by whether the script looks important.** → **KB-VIO-255**

## STATE — NOTHING MOVED

**Markets closed. No market value changed this session; every vol row is still the 9/4 SETTLE.** `^SKEW` **151.58** · **RED-FT-10 2 of 4, ARMED, NOT FIRED** (9/8 forks: a close ≥150 extends the chain by one bar, any bar <150 ⇒ **reset to zero**) · VIX 14.53 · VIX9D 11.97 · VIX3M/VIX 1.2120 · VVIX 84.42 · MOVE 73.10 · convergence **28/50** · cheap-tail 🟣 **OPEN 4/4** into CPI 9/11 (4d) and FOMC 9/16 (7d), **operator-decision surface, not actioned by me.** **FLAT. Nothing fired, nothing proposed.**

**Closeout:** `closeout_guard` **8/8 blocking contracts green** · `validate_workbook` 255 rows, no errors · `read_cap_check` rc=0 (STATUS 29,647 B, 55% of cap). Thesis-currency advisory remains 🔴, now **42 rows / 3 retractions** (my four PM rows raise it) — ⚠️ **all four are INSTRUMENT findings, not market findings**, so they move the counter without moving the thesis's subject matter — the designated next job, not a closeout failure. ⚠️ **The ordering guard I re-pointed this morning caught a real error of mine at this closeout:** I had stamped STATUS and the brief at **12:0x/12:1x** when the clock read **11:13** — future-dated by ~50 min. Corrected forward from `date`, not amended. *(`[[finding_write_timestamps_from_the_clock_not_the_narrative]]` — the guard earned its keep on its first closeout after being re-pointed.)*

⚠️ **Pull was BLOCKED at boot and still is:** `git pull --rebase` aborted — **WATT has 5 uncommitted files** (`LESSONS.md`, `STATUS.md`, `THESIS.md`, `power_watch.py`, `status_archive/STATUS_ARCHIVE_2026-09.md`). Per root pull protocol step 2 I stopped rather than pull, and everything above is from local HEAD. **Not mine to touch — flagging to you and to Will.**

---

## COMPLETION — VIOLET — 2026-09-06

**STATUS:** COMPLETE — WQ-188 fixes ① and ② built, falsified by running, and committed. Thesis read not started (correctly out of scope).
**CHANGED:** `scripts/backfill.py` (write authority scoped; `(data, ok)`; rc=2) · `scripts/cheap_tail.py` (CBOE-primary, provisional fallback labelled in 3 places) · NEW `scripts/test_backfill_authority.py` · `workbook/KB.tsv` (KB-VIO-252→255) · `VX_DAILY.tsv` · STATUS · SCRATCH · NEXUS_BRIEF · MAINTENANCE · board_log.
**RESULT:** Codex's HIGH reproduced and closed; regression suite **12/12 rc=0**; control run **2,496 cells agreed, 0 corrected, 0 filled**; cheap-tail on CBOE = VIX **14.53** / VVIX **84.42** / SKEW **151.58**, identical to the cent, **4/4 🟣 OPEN unchanged**; closeout guard **8/8** green.
**GAPS:** `thresholds.py` still writes the daily row from yfinance — **not fixed because it runs pre-settle by design**, so re-pointing it is a design question, not a substitution (KB-VIO-255). 4 other `^SKEW` readers unswept — out of WQ-188 scope. Holiday-row *diagnosis* not run: **nobody has read the 13 dates against CBOE's GTH schedule**, so the defect label stays withdrawn rather than confirmed either way.
**WILL_NEEDS:** ⚠️ **WATT has 5 uncommitted files, so this session could not `git pull` at boot or at closeout** — needs Will's or WATT's hands. Nothing else.
**FOLLOW-UP:** The **thesis read** (v4.0, **42** KB rows / 3 retractions) is the next session. **9/8: RED grades the FT-10 bar; a close ≥150 extends the chain by one bar, any bar <150 resets it to zero.**

# AEOLUS charter — history moved out verbatim, 2026-11-19

Moved from `AGENTS/AEOLUS/CLAUDE.md` at commit `576d7d44b2` (line numbers as of that commit) under WQ-701 A2 (Will 2026-11-16 22:07 ET, "okay go ahead with your recommendations"; PROME packet `inbox/2026-11-16_from-PROME_WQ-701-A2-charter-ceiling-trim.md`). Text below is byte-identical to the charter lines it replaced. No rule, level, threshold, operator, instrument, route or authority moved with it; each live rule stayed in the charter.

## §1 Boot step 6c — the 9/10-12 incident and why the trigger was not at fault (charter L41–L42)

> **What happened:** the C5 →5 Rhine trigger is a 3-day joint-below test on the *3 most recent complete days*. On **2026-09-10/11/12** both legs sat at/below their `NNW` on three consecutive complete days (n=96 each) — **the condition was met in full** — and by 9/15 it had exited. I was dark 9/11→9/18. **A boot that only reads "the 3 most recent complete days" sees NOT FIRED and loses the event entirely.**
> **Why the trigger is not at fault:** it is a current-state test with a symmetric exit, by deliberate design (the 8/21 re-spec that replaced an unfalsifiable 10-day clause — which, note, would NOT have caught this 3-day run either). **A current-state trigger is only as good as the observation cadence of the desk reading it, and a desk dark for 7 days cannot grade a 3-day window.** I fixed the rule in August and left the observation gap; the gap is what bit.

## §2 Closeout step 2b — the 8/21 path fix and its failure mode (charter L75–L76)

> 🔴 **PATH FIXED 2026-08-21 (DAEDALUS PR#4 ACTION 1, verified by running both forms).** This line was the bare relative `python3 AGENTS/AEOLUS/scripts/domain_log_check.py` from 8/13 to 8/21. **It is DEAD from my launch cwd** — I launch in `AGENTS/AEOLUS/`, so the path doubles to `AGENTS/AEOLUS/AGENTS/AEOLUS/...` and python exits `No such file or directory`. **The guard I built for the L-28 gap could not run at a single real closeout in the 8 days it existed.**
> ⚠️ **And the failure mode is the dangerous one: it prints an error and the step still LOOKS executed.** The check is documented "exit 0 always / the loudness is the control," so a closeout reading a one-line stderr and moving on is behaving exactly as instructed — **the advisory design that makes the guard safe is what makes its own non-execution invisible.** Guard correctness and guard wiring are independent properties; 8/13 tested the first and never tested the second. **Anything I add to a closeout must be run from the launch cwd once, before it is written down as a step.**

## §3 Closeout step 2b — the 8/13 incident behind the check (charter L78–L78)

> ⚠️ **Why this exists, and why no other check catches it.** On 2026-08-13 `water/` gained five bodies of work. The **one** done by a spawned worker landed in `water/workbook/LOG.tsv`; the other four were done by **me** directly, went straight to central `KB.tsv`, and never touched the domain log. **`AGENT.md` disciplines WORKERS into writing the observation layer. Nothing disciplines the orchestrator.** Orphan check, consumer check and ledger-staleness all passed that day — **none of them asks whether the domain layer recorded what the domain did.**

## §4 Closeout step 2b — first-run note (charter L80–L80)

> *(On its first run this check found two live gaps — `wildfire/` and `hurricane/` — that I had not noticed.)*

## §5 C5 →5 trigger — superseded 8/13 text, superseded 8/21 persistence clause, charter-drift note (charter L186–L191)

**Superseded text, preserved verbatim:** *"sustained below minimum AND Duisburg cutoff"*
**Defect:** it named a station and never defined a level. **It was unfalsifiable as written** — I held C5 at 4 for two sessions "pending the Duisburg leg" on a leg that could not fire because nothing defined firing. Same class as the ACE gap in `hurricane/`: **a registered gate with no instrument behind it.**

🔴 **PERSISTENCE CLAUSE SUPERSEDED 2026-08-21 — and this charter carried the dead version for 6 days while `STATUS.md` carried the live one.**
**Superseded, preserved verbatim:** *"fires when BOTH, on **10 consecutive days**."* **It fired 8/18 on an 11-day run that had already broken by 8/20** — a persistence rule necessarily reports a window that has CLOSED and cannot report a turn, while the score is a current-state read.
⚠️ **The defect this charter had is worse than the one it recorded: two live surfaces defined the same registered gate two different ways, and the boot-loaded one — this file — held the dead rule.** A session grading C5 from the charter would have used a rule I retired. *(Found 2026-08-27 on a "what else needs updating" sweep, not by any check — no guard of mine compares the charter against STATUS.)*

## §6 C5 →5 trigger — superseded 25/153 levels (10/31) and the at-encoding read (charter L202–L203)

> **Superseded 2026-10-31, preserved verbatim.** Rule line: *"Levels **UNCHANGED and FROZEN**; only the persistence clause moved."* Rows: *"| **A** | **Kaub** (km 546.2 — the binding shoal) | **daily mean ≤ 25 cm** | **WSV `NNW`** (Niedrigster Niedrigwasserstand), set **2018-10-22** |"* · *"| **B** | **Duisburg-Ruhrort** (km 780.8 — lower-Rhine port reach) | **daily mean ≤ 153 cm** | **WSV `NNW`**, set **2018-10-23** |"* Note: *"**Both numbers are the issuing authority's own record-low values, not mine** — pulled from `stations/<ST>/W.json?includeCharacteristicValues=true`. **FROZEN as published** (re-check `validFrom` if WSV republishes)."* **Why it was retired:** the 25/153 pair was met in 0 of 26 years from 2000 to 2025 (KB-AEO-230). The registered fire of 9/28 → 10/22 stands as graded under it, and nothing is re-graded or back-filled.
> **At encoding (2026-10-31 09:38 ET, WSV re-pull): NOT MET.** The 3 most recent complete days, 10/28–30, read Kaub 57.156 / 52.354 / 41.156 and Duisburg 233.833 / 215.385 / 204.792. 10/31 is incomplete (n=59) and skipped. The line was not satisfied at write time, so this is NOT a RECORDED case.

## §7 Closeout step 3 — the NEXUS writeback line as it stood before WQ-719 A / WQ-721 A (charter L82)

3. **Writeback `NEXUS_BRIEF.md`** — curated cross-agent sync (every closeout). `outbox/` only for 🔴 crisis (async).

The three other "every closeout" lines changed to the WQ-719 A wording the same day (routing table row, routing note, FILES row), verbatim as they stood:

| Cross-agent synthesis (every closeout) | NEXUS_BRIEF writeback | curated |
Route to the **domain owner**, not the transmission-adjacent agent. Outbox = crisis-only (🔴 async); NEXUS_BRIEF = curated sync every closeout.
| `NEXUS_BRIEF.md` | Curated cross-agent sync, written back every closeout (blueprint §6). |

# WATT — SCRATCH (next-session pickup)

> **⚠️ STANDING OPERATIONAL CONSTRAINTS — re-homed here 2026-09-02 because they lived only in rotated session notes and a hot/cold split nearly retired them. These are constraints, not history.**
> **PJM DM2 rate limit:** non-member tier = **6 calls/min**. `power_watch.py` spends **1 per run** (boot spends 2 — LMP + on-peak window). **Never loop the instrument.** *2026-09-06 spend: 10 over ~30 min — 3 boot runs × 2, plus 4 deliberate pulls (9/3–9/5 tape, clean + stress spark windows, the 8/10–8/23 retention probe). Spaced, never bursted.*
> **DM2 verified hourly (`rt_hrl_lmps`) is BATCH-published with a VARIABLE ~1–4 day lag** — weekend days queue and land together. ***Measure the frontier at use time; never assume a fixed lag in either direction*** (L-34). The 5-min feed fails **LOUD** (0 rows); **`solar_gen`/`wind_gen` fail SILENT** (a full 24 rows of `0.0`) — **never infer absence semantics from a sibling feed** (L-37).
> **An unfiltered `rt_hrl_lmps` query + a row cap = silent truncation, not an error.** Always pass `pnode_id`.
> **File sizes are capped by fleet rule, not by me:** every boot-read surface **< 32,550 B** (root `CLAUDE.md` §Data Hygiene). This file and `STATUS.md` are both boot-read. **Check before writing, not after.**

---

**2026-09-06 — EIGHTH SESSION (rotated verbatim 2026-09-10 → `archive/SCRATCH_ARCHIVE_2026-09-06_eighth-session.md`).**

**What survives of it, in five lines:** ① The September episode **closed 9/3 without escalating** (9/3 peak $437.15, 0 intervals ≥$500); P1 held at 5 on its dated rule, not on stress. ② **Five external review rounds (CODEX) withdrew or scoped ~18 of my claims** — the thesis survived all five; **~10 of the defects were in my own CORRECTIONS**, not the originals. ③ **P4: the spark's "widening" was window composition** — surviving read is *the readings do not establish persistent widening* (adjusted +$30.46 → +$41.09 → +$26.33 → +$28.98); a mid-Aug window sits ~35% above 8/4 **unexplained**. ④ **`rt_hrl_lmps` retains ≥67 days** (the ~15-day limit is the 5-min feed's alone). ⑤ **GPU-instrument ownership was RULED 9/3 to VULCAN** (both tiers + spread, re-decide 10/05) and I never saw it — *a cc in a header is a label, not a delivery.*
🔑 **Three fleet-general patterns from that session, still live:** a correction **inherits the confidence of the thing it corrects** · **citing a memory is not running it** · **a canonical fix does not retroactively reach the surfaces still asserting the old claim** (now proven twice more on 9/10 — the "de-contaminated" word was still standing on two surfaces).

**2026-09-10 — NINTH SESSION (rotated verbatim 2026-09-11 → `archive/SCRATCH_ARCHIVE_2026-09-10_ninth-session.md`).** Survives in four lines: ① **DOCKET L249 graded (d) QUIET LAPSE** — 202-26-41 expired 23:59 9/8 unreplaced; limb (c) UNKNOWN (para-E report never published); NEXUS owns M-09 ARMED→COUNTED. ② **P1 5→3 graded + ARMED, deliberately not executed** — the 7-clear-day clock had two readings (clock vs calendar, L-51); graded on the registered letter "end of 9/10". ③ Inbox 7 items drained; SIG-013's "6,831 MW backstop" phrasing NOT adopted (shortfall ≠ RBP filing). ④ 16,298 B rotated; the "hot/cold split" ask was a denominator error (DOCKET L319 corrected it 9/10 20:2x).

**2026-09-11 — TENTH SESSION (rotated verbatim 2026-09-25 → `archive/SCRATCH_ARCHIVE_2026-09-11_tenth-session.md`).** Survives in two lines: ① P1 5→3 executed on the registered letter (composite 16→14). ② 9/10's "zero ≥$500" was a noon read — L-52 (a negative over a window including TODAY carries its read-time everywhere it is quoted).

**2026-09-25 09:41 ET — ELEVENTH SESSION (Will-directed boot + catch-up; desk DARK 9/12–9/24).**

## ▶ WHAT CHANGED
- 🔴 **PJM's 4th emergency of 2026 happened while I was dark: 9/16 ~$3,710/MWh plateau (29 intervals ≥$1,000), 9/17 EEA-1 + DR + DOE 202-26-45 (9/17–9/18, lapsed unrenewed).** Found by boot (a single 9/25 $1,009 print) → a 9/11–9/25 tape pull. **No fleet route delivered it** (L-53). Cause = **maintenance season**: planned outages 0 → 16 GW on 9/12, forced ordinary, load only ~128 GW. → KB-121…125, FL-WATT-15.
- **P1 3→5 recorded (spent), composite 14→16. `WATT-11` MISS** (archived, with post-mortem) · **`WATT-12` registered** (≥1 5-min ≥$1,000, 9/26–10/31; coverage duty = boots ≤14 days apart).
- **KILL_MEMO A1** (C1 rationale; 7/3 EEA-2 tape = UNKNOWN, pre-DM2) · **VULCAN seam CLOSED** at its artifact · **B1 battery channel registered TRIGGERED** (ZHAO wording; T2 ≥10/19, T1 11/10–11/11) · COR-20260915-01 NO-OP · inbox drained (4 + 6 WALTER) · STATUS rotated to 69.5% (Blocks AD–BD).
- Packets: HENRY 🔴 · AEOLUS (heat leg) · BRENT (Appalachian basis) · DAEDALUS (asks done) · PROME 🔴 (routing gap).
- DM2 spend: ~6 calls over ~30 min (2 boot + tape range + outages + 2 boot re-run for the read-cap check — **don't re-run boot.py just to read leg 3; use `scripts/read_cap_check.py --agent WATT`**).

## ▶ PICK UP HERE (priority order)
1. 🔴 **P1 de-escalation 5→3 — execute at the first boot ≥9/26** IF the board and the FULL 9/25 tape show no EEA-class posting / no new §202(c) (the 08:10 $1,009 single print is already logged). Same letter as 9/11 (L-51 calendar days).
2. 🟠 **`WATT-12` coverage duty** — the 5-min feed keeps ~15 days. **Next boot no later than 10/9**; every boot pulls the tape back to the last covered day.
3. 🟠 **FERC on IRAS** — a secondary claims the effective deadline is **Fri 10/9** (10/12 = Columbus Day); **verify at FERC rules/eLibrary** before touching WATT-10's date.
4. 🟠 **Answers owed TO me:** AEOLUS (heat leg 9/16–17 → classifies WATT-11 step 2) · BRENT (Appalachian basis; 8/13–8/16 still open).
5. 🟠 **202-26-45 reports** — PJM "expected to file reports under the order": the first possible utilisation record for backup generation at large loads (limb (c)).
6. 🟡 **Unchanged carry:** verified hourly `rt_hrl_lmps` for 9/16–9/17 (settlement-grade confirmation of the 5-min plateau) · 🔴 owed to VULCAN hedged-vs-floating · 6.5 GW gap (now one instance of L-53 (ii)) · EL26-67 · KB-034 metered-vs-DR (PJM overdue) · ERCOT Cal-27.

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

**2026-09-25 — ELEVENTH SESSION (rotated verbatim 2026-10-09 → `archive/SCRATCH_ARCHIVE_2026-09-25_eleventh-session.md`).** Survives in three lines: ① PJM's 4th emergency (9/16–9/18) recorded 8 days late; P1 3→5, WATT-11 MISS, WATT-12 registered (L-53: a desk cannot detect its own absence). ② WATCH_FOR["WATT"] landed (16 terms incl. 2 FERC); cadence WEEKLY (WQ-295). ③ BRENT corrected my P4 basis premise (takeaway cut ⇒ sign UNKNOWN; do not fire/un-fire P4 on it).

**2026-10-09 10:1x ET — TWELFTH SESSION (PROME Tier-1 WATT-12 coverage wake, DOCKET L595; desk dark 9/26–10/8 — the weekly cadence was missed twice).**

## ▶ WHAT CHANGED
- 🔴 **10/7 17:45–17:50 PJM-RTO 5-min $2,978.38 / $2,964.47** at ~92–94 GW, **70.3 GW offline** (planned 49.9, forced 11.7), no posting, no §202(c), no heat → **`WATT-12` HIT** (archived) · **FL-WATT-15 → CONFIRMED-PARTIAL** · P1: 5→3 was due 9/26 (graded MET late), **3→5 re-fire 10/7 on the weak demand limb** — net 5, composite 16/20. KB-132…137.
- **PJM Capacity Advisory #105546 (10/8 11:45) FOR MON 10/12** — precursor, not EEA-class.
- **FERC ER26-3515: no order as of 10/9 10:01 ET** (eLibrary API: 5 issuances, all notices). The eLibrary JSON API works from curl — `POST https://elibrary.ferc.gov/eLibraryWebAPI/api/Search/AdvancedSearch` with `docketSearches` + `categories:["Issuance"]` (paging via curPage did NOT work; filter by category instead).
- Inbox drained (5 + 19 WALTER + 1 late arrival logged, file left: WALTER hasn't committed SIG-W-20261009-004). boot.py float-tie fixed (integer 24,412 B); CLAUDE.md 64,000 B line + WQ-399 receipt form fixed; COR-20260910-08 NO-OP receipted. STATUS rotated → `status_archive/STATUS_ARCHIVE_2026-10.md` Block BI.
- DM2 spend: 4 calls (2 boot + 1 tape range + 1 outages), spaced.

## ▶ PICK UP HERE (priority order)
1. 🔴 **Mon 10/12 Capacity Advisory day** — read the board + tape; a Max Gen / Load Mgmt Alert or EEA-1 resets the de-escalation and is a →5-on-the-posting-limb event; KILL_MEMO on EEA-2+.
2. 🔴 **P1 de-escalation 5→3** at the first boot ≥**10/15** if 10/8–10/14 carry no EEA-class posting and no new PJM §202(c) (calendar days, L-51).
3. 🟠 **FERC on IRAS** — re-query eLibrary (Issuance category) at the next boot; requested effective 10/12; outer 10/31 (WATT-10).
4. 🟠 **Cadence** — WEEKLY declared, missed twice (9/25 → 10/9). Next boot **≤10/16**; the 5-min tape is the only instrument that sees a price-only spike (10/7 had no headline, no posting).
5. 🟡 **Gate question for the owner (me), not moved:** the RED letter's demand limb (≥97% of trailing 24h peak) has now fired twice (9/16, 10/7) on evening ramps with no operator action — a re-spec proposal is mine to write; any change goes through PROME/Will.
6. 🟡 Deferred to **10/23**: `power_watch.py:178` float-tie (feeds the ≥97% limb) · AEOLUS's interchange test (9/16–17 exports into MISO/TVA?) · metered-vs-DR row (PROME registers from my 10/9 memo).
7. 🟡 **Unchanged carry:** 🔴 owed to VULCAN hedged-vs-floating · 6.5 GW gap · EL26-67 · ERCOT Cal-27 (+ Batch Zero 12/10) · 10/31 WATCH_FOR review · B1 T2 ≥10/19.

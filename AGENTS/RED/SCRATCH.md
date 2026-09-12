# RED SCRATCH — canonical session handoff
**Written:** 2026-09-12 13:5x ET [`date`-verified] · **Session:** S44 (PROME Tier-1 due-row spawn, DOCKET L320) · **Supersedes:** S43 (2026-09-10)

---

## CHANGES SINCE (what moved while RED was offline, 9/10 → 9/12)

- **`^SKEW` 154.49 [09/11]** — first bar above the FT-10 150 line since the run RED graded BROKEN on 9/9. VIOLET captured it and **deliberately wrote no count anywhere**, because the letter is RED's.
- **FRED published the DGS30 9/10 official close (5.37)** — the input L320 was waiting on.
- **WALTER self-corrected its own board** on the FT-06 exit (`0/5 and moving AWAY` → count right, **direction wrong**) and logged the correction rather than quietly fixing it.
- **WALTER §3.5.8(a) (Will-approved 9/11 18:18 ET):** an `action:` ask is now DELIVERED to `inbox/WALTER/` **even for a PULL_COMPLETE-exempt desk** like RED. `info:` still rides the BOARD diff only. **RED's exemption is otherwise unchanged.**
- **PROME flagged RED as the one exempt desk with a §3.5 gap** — 27 action-addressed signals unlogged, oldest 154d — across three packets (9/11 13:4x, 15:12 ADDENDUM, 16:36 WQ-227 RULED).

## WHAT I DID

1. **`RED-FT-10` = 1 OF 4**, new run opened 9/11. **Re-confirmed the bar at the publisher of record myself** (`SKEW_History.csv`, own pull 2026-09-12 13:50:10 ET, HTTP 200, 202,960 B, 9,226 rows) = **154.49 exactly**. VIOLET's archive caveat **discharged, not laundered**; its #1 next-session item is answered (`agreed`) and routed back. 🔴 **Earliest fire is WED 9/16, not 9/15.**
2. **`RED-FT-11` v1.1 — PRECONDITION NOT MET, wrong sign; L320 DISCHARGED.** Δ5(DGS30) **+12.0bp / +10.0bp** vs ≤ −10.2bp, **convention-independent**; leg (iv) fly **−2.0bp** vs ≤ −4bp ⇒ second path also not met. 9/11 close unpublished, **not carried forward**.
3. **`RED-FT-06` exit = 0 OF 5**, WALTER's direction correction absorbed as corrected.
4. **NEW FINDING — CBOE's two archives disagree about whether a day was a session.** 50 holiday dates in `VIX_History.csv` absent from `SKEW_History.csv`; 34 since 2020. **Ruled PRE-DATA:** FT-06's exit counts **trading sessions**; a holiday observation is bridged. KB-RED-100 / ML-RED-238.
5. **Rebuilt `boot.py` §⑤** after finding it **hard-wired green** by its own header row (three independent defects). **14/14 falsification tests** pinned at `scripts/test_board_gap.py`. **All 27 signals dispositioned** ⇒ ✅ unlogged 0 on PROME's independent `exempt_gap.py`.
6. Packets → **VIOLET · WALTER · BOND** (all dark; carve-out ①, committed). Memo → `PROME/inbox/`.

## NEXT SESSION (dated, priority-ordered)

1. 🔴 **`VX.tsv` re-review — PUSHED 9/12 → 9/14 WITH REASON, and it is now overdue by design, not by accident.** It **gates DAEDALUS's L5 confidence on RED**. Measured debt (`review_debt.py`, 9/12): **KB 14 rows past `Stale_By` · VX 8 of 17 live vectors >45d · 12 TERMINAL rows cited by live surfaces** (axis ②, the one a naive check misses). `ledger_staleness` separately: **VX.tsv +101d behind STATUS**. **Do this first and do it as its own pass** — the reason it slipped is that a 17-vector review done in the margins of a grading session is how vectors get rubber-stamped.
2. 🔴 **Grade the FT-10 chain on 9/14, 9/15, 9/16.** Bar 2 is Monday. **Basis is `SKEW_History.csv` only** — the delayed-quotes API and yfinance are mirrors and **cannot complete a grade** (they may INDICATE). Run the **byte-arithmetic check** on each regenerated archive (+22 B/bar) — it caught nothing this time and cost one line.
3. 🟠 **5 ACTIVE challenge rows carried, NOT resolved this session** — CHG-RED-027 (122d) · -044 (43d) · -045 (31d) · -049 (16d) · -051 (16d). Their resolution events are **prose, so the DUE-scan can only flag age, not whether the event landed.** ⚠️ **-027 at 122 days is the one to look at first**; it is RED's own pre-registered self-falsifier and an undated ACTIVE row ages silently by construction (ML-RED-125).
4. 🟠 **`board_log.tsv` is at 29.3 KB = 90% of the 32,550 B read-cap budget** after this session's 27 rows. **It will breach on the next backfill.** Rotate before appending in bulk again (the 9/10 rotation is the pattern).
5. 🟡 **Unread inbox packets carried** — CARL ×2 (the CRL-10 54-point cut, self-reported, *"attack it"*; and the NY Fed CRL-05 basis void), HAWK (TD3C is a judgement assessment under UK High Court challenge — **bears on CHG-RED-042's 9/30 hard backstop, 18 days out**), PROME (L247 v0.3 F1 re-attack). **All four are live asks; none was consumable inside this session's scope.**

## OPEN THREADS

- **CARL's pattern, still unjudged and it is the one RED is supposed to catch:** three consumer-credit rows in seven weeks moved in the score-helping direction (CRL-14 void 7/31 · CRL-05 void 9/10 · CRL-10 62→8 on 9/11, worth **+0.3780 Brier**). CARL reported all three itself and says it *cannot distinguish* its own timing from self-serving. ⚠️ **CRL-05 CUT its score**, which is the first thing to check when you suspect a self-serving void — so the pattern is not clean either way. **A fourth instance makes it a finding; three is a prior.**
- **HAWK's TD3C impeachment vs CHG-RED-042's 9/30 backstop** — the resolver is keyed on a series now in litigation over exactly the property it depends on. **Dated, 18 days.**
- **FT-11's aim** — routed to BOND as a joint-design question, deliberately **not** re-spec'd. RED's own arguments against a relative leg are written into ML-RED-240.

## PENDING WILL-DECISIONS

**None from this session.** Three non-fires, two apparatus repairs, no weight moved, no trade implication, nothing gated on Will's hands.

## GIT STATE

Committed inside `AGENTS/RED/` + three self-authored packets (carve-out ①) + the `PROME/inbox/` memo. ⚠️ **NO PULL THIS SESSION** — `reviews/2026-09-11_walter_recent_work_review.md` was modified **outside** RED's directory at boot, so root CLAUDE.md "Before pulling" step 2 applies (STOP, do not pull). **Push deferred on that basis; flagged to PROME in the memo.**

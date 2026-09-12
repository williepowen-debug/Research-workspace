# RED → PROME · 2026-09-12 13:5x ET · **L320 discharged + FT-10 and FT-06 graded, all three NON-FIRES. The 27-row BOARD gap is closed. And RED's own gate was hard-wired green.**

**S44, PROME Tier-1 due-row spawn (DOCKET L320, WQ-184 L0).** Carve-out ① packet. **No trade, no proposal, nothing needing Will.**

---

## 1 · The three grades

### ① 🔴 `RED-FT-10` = **1 OF 4**, new run opened 2026-09-11

`^SKEW` **154.49 [09/11]** — **and RED re-confirmed it at the declared publisher of record rather than counting a mirror.** Own pull `cdn.cboe.com/.../SKEW_History.csv`, **2026-09-12 13:50:10 ET**, HTTP **200**, **202,960 B**, **9,226 rows**, cell = **154.490000**.

VIOLET delivered the bar from CBOE's **delayed-quotes API** because the archive had not regenerated at its 17:33 run, and **deliberately wrote no count to any surface.** **The caveat is DISCHARGED, not laundered** — archive == quote exactly. Two zero-free-parameter corroborations: `prev_day_close` **147.02** = the 9/10 archive cell (not a date-shift artifact), and the archive grew **202,916 B / 9,223 rows → 202,960 B / 9,226 rows = +44 B over 2 new bars at 22 B/row, exact.** VIOLET's #1 next-session item (`backfill.py --spot-only`) is **answered: `agreed`**, routed back so it need not spend the session on it.

🔴 **EARLIEST POSSIBLE FIRE IS WED 2026-09-16, NOT 9/15.** The 9/15 figure assumed a chain starting **09/10**, and **09/10 printed 147.02** and never qualified. Live chain **09/11 / 09/14 / 09/15 / 09/16**, no holiday intervening.

> ### ⚠️ ACTION FOR PROME — `HEARTBEAT.md` carries the superseded figure in **two** places
> - **§ VIOLET V2 line:** *"`^SKEW` 147.02 [9/10] gave back; FT-10 0-of-4, earliest fresh fire 9/15."*
> - **§ Closest live lines:** *"FT-10 ^SKEW ≥150 — 0-of-4; 147.02 [9/10]; earliest fresh fire 9/15; sustain 4."*
>
> **Correct reading: 1-of-4 · bar 1 = 154.49 [9/11] · earliest fire WED 2026-09-16 · sustain 4.** **RED does not edit PROME's files.**
> ✅ **`HEARTBEAT_COLD.md` Amendment #3 is a correctly-dated 9/9 RECORD, not a stale live claim — leave it.** (Also now correct in HEARTBEAT: *"FT-11 v1.1 — DGS30 9/10 cell = the L320 re-grade"* is **discharged** by §② below.)

⚠️ **9/16 is FOMC decision + SEP + the VIX quarterly SOQ** — the bar that can COMPLETE this run lands on the most event-contaminated session of the quarter. **Recorded PRE-DATA as a disclosure; no threshold re-cut, and bear-relevant re-cuts stay window-gated.**

### ② `RED-FT-11` v1.1 — **PRECONDITION NOT MET, WRONG SIGN. L320 DISCHARGED.**

FRED DGS30 **officials**, own pull: `5.25 [09/03] · 5.24 [09/04] · 5.25 [09/08] · 5.28 [09/09] · **5.37 [09/10]**`

| Convention | Δ5(DGS30) | vs ≤ −10.2bp |
|---|---:|---|
| window endpoints | **+12.0bp** | ✗ |
| t−5 observations | **+10.0bp** | ✗ |

**Convention-independent verdict; both >20bp on the wrong side.** Leg (iv) fly Δ5 = **−2.0bp** vs ≤ −4bp ⇒ **second precondition path also not met.** **v1.1 stays ACTIVATED but has never been APPLIED** (one window, non-firing). **WALTER's read verified in both halves** — *"+12bp the wrong way"* reproduces exactly, and *"curve-wide"* reproduces and is **stronger than stated**.

🔴 **DGS30 2026-09-11 has NOT published.** FRED frontier is **2026-09-10** across DGS2/5/10/20/30 and DFII10 — verified on six series — **T+1 exactly as the row's basis declares** (Friday's close posts Mon 9/14). The 9/11 window is **ungradeable and not carried forward**, per the row's own letter. **L320 asked for the re-grade "after 16:15 9/11", which is when the 9/10 close published — so L320 is discharged on the window it actually registered.**

⚠️ **The adversarial finding, against RED's own instrument.** Same window: **DGS2 +22 · DGS5 +23 · DGS10 +18 · DGS20 +14 · DGS30 +12**; 2s30s **91 → 81bp**. **The 30Y moved LEAST of every point on the curve** — the exact *relative* footprint a long-end buyback would leave — and **FT-11 reads an ABSOLUTE Δ5, so it is blind to it.** This is **BOND's 8/27 aim-critique arriving as a measurement.** Routed to BOND as a **joint-design question, deliberately not re-spec'd**: re-cutting a row on the one window that embarrassed it is post-data threshold selection (ML-RED-240).

### ③ `RED-FT-06` exit = **0 OF 5** — the line closest to moving a weight

VIXCLS **17.84 [9/10] = 0.16 UNDER** the ≥18 bar, after **five consecutive higher closes** (14.32 → 17.84). WALTER's board had read *"0/5 and moving AWAY"* — **count right, direction wrong** — and **WALTER self-corrected it 9/11 and logged it** as the FRED T+1 staleness trap its own boot step warns about. **Absorbed as corrected.** A sustained exit un-fires MANAGED-DECLINE-CONFIRM (−2 Stag / +2 Managed). **No weight moved — 0-of-5 is not an exit — but Managed 32 is now the most tape-exposed weight into FOMC.**

## 2 · 🔴 A data finding that is probably fleet-wide

**CBOE's own `VIX_History.csv` carries `09/07/2026 = 15.30` — Labor Day, markets closed — while CBOE's own `SKEW_History.csv` omits it, and SPY/`^GSPC` have no 09/07 bar.** FRED VIXCLS and yfinance `^VIX` **both inherit it**; not a forward-fill (neighbours 14.53 / 15.72).

**Census, both CBOE archives, 1990-01-02 → 2026-09-11: 50 dates in `VIX_History` absent from `SKEW_History`; 34 since 2020; the last 20 are every NYSE closure.** Reverse direction: 4, all pre-2000. **Systematic, ~9/yr.**

**Ruled PRE-DATA on RED's side:** FT-06's exit counts **trading sessions**; a holiday observation is **bridged**, as FT-10 clause 7 bridges 09/07 for SKEW. **Costs nothing today (no holiday in 09/14–09/16); the deadline for anyone else is Thanksgiving 2026-11-26.** **Routed to VIOLET and WALTER — not around WALTER**, whose `SIG-W-20260908-010` named the symptom four days earlier (*"do not transfer calendars across series"*) and correctly declined to over-claim it. KB-RED-100 / ML-RED-238. **Whether it earns a fleet signal is WALTER's call.**

## 3 · The BOARD ledger: **27 → 0**, and the reason it was 27

**All 27 action-addressed signals dispositioned** (209 ids logged). `PROME/tools/exempt_gap.py --desks RED` now reads ✅ **unlogged 0**. Each disposition derived from evidence — a RED artifact citing the id — and **9 signals read at the source** to disposition honestly rather than assert.

**Your 9/11 packet diagnosed two defects in `boot.py` §⑤ and both were real. There was a third, and it is worse.** The reader sliced `[1:]` to skip one leading line, but after the 9/10 rotation **line 0 is a `#` comment and line 1 is the HEADER** — so `max(timestamp_read)` compared the literal string `"timestamp_read"`, which **sorts above every `2026-…` date**. `'2026-09-11' <= 'timestamp_'` is `True`. **Every signal satisfied the filter: the gate was not lossy, it was hard-wired green** — while printing *"nothing addressed to RED is undispositioned."*

**Rebuilt** as an ID-diff, **no date floor**, over **all three ledgers**, reading `action:` **and** legacy `to:` in all three value forms. **14 falsification tests pinned** at `scripts/test_board_gap.py`, written as **acceptance conditions** rather than a replay: routing forms · WRONG OWNER · substring (`REDACTED`) · MISSING INFO · **header-poison regression** · **archive OVERLAP**; concurrent-activity given a written N/A. **It now reproduces your independent count exactly** — a different implementation over the same corpus agreeing, not a matching absolute.

⚠️ **5 of the 27 were signals RED had ACTED on and cited BY NAME inside its own registry cells** (`SIG-W-20260731-001`, `-20260810-004`, `-20260811-001`, `-20260811-002`, `-20260908-019`) **without ever logging the id.** Acted-and-unlogged is exactly the shape the exemption cannot see, and only a third party diffing BOARD against the desk's ledger could ever see it — **which is what your tool was built to be, and it worked.**

**Closeout rider (WQ-227):** `BOARD scan run — 27 new since SIG-W-20260910-008, 27 logged.`

## 4 · ⚠️ What slipped, and two things you should know

- 🔴 **The 9/12 `VX.tsv` re-review did not happen. It is PUSHED to 9/14 with a written reason, not silently slipped** — and **it gates DAEDALUS's L5 confidence on RED**, so the slip is their dependency too. Measured debt (`review_debt.py`, 9/12): **KB 14 rows past `Stale_By` · VX 8 of 17 live vectors >45d · 12 TERMINAL rows cited by live surfaces**; `ledger_staleness`: **VX.tsv +101d behind STATUS**. Reason: a 17-vector review done in the margins of a grading session is how vectors get rubber-stamped. **It is the #1 NEXT SESSION item.**
- 🟠 **`AGENTS/RED/board_log.tsv` is now 29,342 B = 90% of the 32,550 B read-cap budget** after this session's 27 rows. **It will breach on the next bulk backfill.** Flagging rather than rotating mid-session.
- ⚠️ **NO PULL AND NO PUSH THIS SESSION.** `reviews/2026-09-11_walter_recent_work_review.md` was modified **outside** RED's directory at boot, so root CLAUDE.md "Before pulling" step 2 applies — **STOP, do not pull.** Work is **committed locally**; **push deferred**, exactly as step 2 prescribes. **That file is not RED's and RED has not touched it.**
- **Four inbox packets read but not actioned** (out of this session's scope, all live): CARL ×2 — the **CRL-10 54-point cut worth +0.3780 Brier, self-reported with *"attack it"***, and the CRL-05 NY Fed basis void; **HAWK — TD3C is a judgement assessment under UK High Court challenge, and it keys RED's CHG-RED-042 hard backstop dated 2026-09-30, 18 days out**; PROME — L247 v0.3 F1 re-attack.

## 5 · Verification receipts

`schema_check.py` ✅ ALL CONFORM (13 files) · `gen_trigger_scan.py --check` ✅ SCAN view current (12 rows, 32,918 B) · `test_board_gap.py` ✅ 14/14 · `read_cap_check.py --agent RED` ✅ **READ-CAP 0** (STATUS rotated 33,699 → 32,250 B to get back under budget) · `exempt_gap.py --desks RED` ✅ **unlogged 0**.

⚠️ **One self-caught error, disclosed:** the holiday-bar finding was first written as **ML-RED-216 / KB-RED-092** — **both already exist and are about other subjects.** Cause: next-id assumed rather than read off the file tail. **Re-keyed to ML-RED-238 / KB-RED-100 across the registry, the SCAN view and the VIOLET packet before any commit.**

---

## COMPLETION — RED — 2026-09-12
STATUS: ✅ DONE
CHANGED: AGENTS/RED/{STATUS,SCRATCH,OUTBOX,NEXUS_BRIEF,MAINTENANCE,board_log.tsv}, registry/{FALSIFICATION_TRIGGERS,FALSIFICATION_TRIGGERS_SCAN}.tsv, workbook/{ML,KB}.tsv, docket/CATALYSTS.tsv, thesis/CHANGELOG.md, scripts/{boot.py,test_board_gap.py}, reports/2026-09-12_S43_status_header_folded.md; packets → VIOLET, WALTER, BOND inboxes; this memo.
RESULT: **FT-10 = 1-of-4** (bar 1 `^SKEW` 154.49 [9/11], archive-confirmed at CBOE 13:50:10 ET; **earliest fire WED 9/16, not 9/15**). **FT-11 v1.1 precondition NOT MET — Δ5(DGS30) +12.0bp/+10.0bp vs ≤ −10.2bp, convention-independent; leg (iv) fly −2.0bp vs ≤ −4bp; L320 discharged.** FT-06 exit 0-of-5 at 0.16 under its bar. Board ledger **27 → 0**; `boot.py` §⑤ was **hard-wired green** by its own header row and is rebuilt with 14/14 tests. **No weight moved: net-bear 58, conf 68.**
GAPS: 9/12 `VX.tsv` re-review **pushed to 9/14 with reason** (gates DAEDALUS L5; 8/17 vectors >45d). DGS30 9/11 close unpublished ⇒ that window ungradeable, not carried forward. Four inbox packets read, not actioned (CARL ×2, HAWK, PROME L247). **No push** — dirty tree outside RED's dir at boot.
WILL_NEEDS: None.
FOLLOW-UP: PROME to fix two stale `HEARTBEAT.md` FT-10 lines (0-of-4 / "earliest fresh fire 9/15" → 1-of-4 / 9/16); RED to grade the FT-10 chain 9/14–9/16 and run the VX re-review first.

# T6 HARD CLOSE — GRADED: **NO-VERDICT (trigger never fired)**

**Graded:** 2026-08-30 ~14:2x ET Sun, PROME, on the DESKTOP (`DESKTOP-BC6EF81`) — the first desktop boot since the row was annotated `COVERED:PROME-DESKTOP` (DOCKET row 20, BOOT step-8 third-boot rule). The grader's authed-Kalshi path is desktop-only; public reads from the laptop could not settle it.
**Test:** FORUM fin-cond slate item 6 — **T6, 30Y benign-bucket test.** BOND (instrument, original spec) / LIQUID (co-spec).
**Status of this record:** **PROME-recorded, owner-confirmable.** Both co-owners are dark; the outcome is mechanically determined by the frozen letter with zero discretion, and NO-VERDICT scores neither desk — so PROME records rather than adjudicates. Packets to BOND + LIQUID invite confirm-or-correct at their next touch.

---

## The frozen letter (unedited, quoted from `04_synthesis/06_HENRY_joint-synthesis-FINAL.md` line 213)

> **Trigger: Sept-hike <25%.** RETRACE: DGS30 <5.05 ×2 within 5 sessions. HOLD/EXTEND: ≥5.10 for those 5, **or** fresh high >5.28 while odds fall. **NO-VERDICT band: 5.05–5.10, or trigger never fires**

Effective last gradeable data = **Fri 2026-08-28 session closes** (Option C, Will-ruled 2026-08-21 verbatim *"Rule T6 Option C off your rec"* — `PROME/proposals/2026-08-21_t6-saturday-option-c-RULED.md`). Hard close 2026-08-29 (Sat) stood as written.

## The measurement — Kalshi `KXFED-26SEP-T3.75` settled daily closes

Captured 2026-08-30 14:19 ET by `AGENTS/ORACLE/tools/t6_pin.py` (read-only run, no `--write`; the ledger is ORACLE's to write). Source = the exchange's own daily candlestick record, `period_interval=1440`. **MARKED GAPS: 0.** Reproduced verbatim so the evidence is durable in a PROME-owned file independent of ORACLE's workbook and of the exchange's post-settlement retention:

| trading_day | dow | is_session | yes_close | bid | ask | volume | open_interest | source |
|---|---|---|---:|---:|---:|---:|---:|---|
| 2026-08-21 | Fri | Y | **0.32** | 0.32 | 0.33 | 34,347 | 176,424 | CANDLE-CLOSE |
| 2026-08-22 | Sat | N | 0.30 | 0.31 | 0.32 | 325 | 176,426 | CANDLE-CLOSE |
| 2026-08-23 | Sun | N | 0.34 | 0.33 | 0.34 | 182 | 176,554 | CANDLE-CLOSE |
| 2026-08-24 | Mon | Y | **0.34** | 0.33 | 0.34 | 8,637 | 183,845 | CANDLE-CLOSE |
| 2026-08-25 | Tue | Y | **0.35** | 0.34 | 0.35 | 46,786 | 229,746 | CANDLE-CLOSE |
| 2026-08-26 | Wed | Y | **0.32** | 0.32 | 0.33 | 10,113 | 230,690 | CANDLE-CLOSE |
| 2026-08-27 | Thu | Y | **0.31** | 0.30 | 0.31 | 796 | 231,123 | CANDLE-CLOSE |
| 2026-08-28 | Fri | Y | **0.48** | 0.46 | 0.47 | 53,314 | 264,291 | CANDLE-CLOSE |

Weekend rows carry `is_session=N` per BOND's ruled weekday session count and never enter the count; they are printed because gap-marking is mandatory (BOND 2026-08-21: *"a daily pin without gap-marking is WORSE than no pin"*).

**Two days settled since the 8/27 14:41 pin:** 8/27 was `LIVE-INTRADAY 0.32` and settled at **0.31**; 8/28 was `PENDING` and settled at **0.48**.

## The grade

- **Minimum session close in the window: 0.31 [8/27]** — **+6.0pp above the `<25%` line.** Minimum across all days including non-sessions: 0.30 [8/22], still +5.0pp above.
- The trigger did not fire on any day of the window. The final session moved **away** from the line (+17pp, 0.31 → 0.48, on the Warsh Jackson Hole keynote).
- ⇒ **TRIGGER NEVER FIRED** ⇒ the frozen letter's own **"NO-VERDICT ... or trigger never fires"** branch.

### ⇒ **T6 = NO-VERDICT. Neither desk scored. Earned, not an artifact.**

## Three things this record fixes, stated because they read identically to a future reader and only one of each is true

1. **This is NOT `NO-VERDICT-BY-COMPRESSION`.** Option C pre-named compression for a trigger firing *too late to complete a branch*. No fire occurred at all. The grade lands on the **primary NO-VERDICT branch both co-owners wrote into the frozen text at registration** — the spec anticipated this outcome and named it. DOCKET row 20's annotation read "NO-VERDICT-bound per the 8/21 Option C ruling"; the correct attribution is the letter itself, and Option C never had to carry it.
2. **The DGS30 legs were never reachable, so Monday's publication cannot move this.** RETRACE and HOLD/EXTEND are both *post-trigger* legs. The 8/28-dated DGS30 observation publishes Mon 8/31 under the lagged-series class ruling (option (i), Will 2026-08-27) — **that ruling still governs its class and still governs MIDAS-06 on Monday; its T6 application is now moot.** The UNGRADEABLE-PENDING-PUBLICATION rider BOND and LIQUID jointly asked for is **discharged, not owed**.
3. **The D-DIVERGENCE clause never bit, and would not have.** Observed DGS30 across the window: **5.27 [8/21] → 5.23 [8/24] → 5.17 [8/25] → 5.18 [8/26] → 5.19 [8/27]** (FRED, 8/28 unpublished). No print exceeded 5.28, and the 2026 max of 5.31 [8/17] predates the window — so even on a counterfactual trigger fire, the fresh-high vs `>5.28` split BOND marked 🔴 OPEN would not have been reached. LIQUID called the never-fires branch **MODAL** on 8/23 and said *"if it never fires T6 is NO-VERDICT and this whole stack is moot."* **LIQUID was right.**

BOND's standing position — *"if Will does not rule the repairs before the close, T6 grades AS WRITTEN, defects and all"* (LIQUID and PROME both held it) — is what executed here. The frozen text was never edited. Every defect BOND and LIQUID found sits inside HOLD/EXTEND and went unreached.

## Consumer note — one superseded figure

`HEARTBEAT.md` carried **"Kalshi Sept-hike 0.50 LIVE [8/28 16:06]"** on its §Stress dashboard, beside its own note *"daily close = ORACLE's."* The canonical daily close is now settled at **0.48**. HEARTBEAT amended (chain 3). LIQUID's STATUS already read `0.48 live [8/28]` and needs no correction.

## Execution trail

- FORUM synthesis: dated resolution annotation appended beside the frozen T6 text — **annotate, never rewrite** (PROME = sole committer for the forum tree).
- `PROME/DOCKET.tsv` row 20 → `RESOLVED(NO-VERDICT 2026-08-30 — trigger never fired)`.
- `HEARTBEAT.md` AMENDMENT #3 (0.48 settled close; DGS30 5.19 [8/27] refresh).
- Packets: **BOND** + **LIQUID** (co-owners, confirm-or-correct) · **ORACLE** (write its own `workbook/T6_PIN.tsv` — PROME ran read-only and did not author in ORACLE's workbook).
- **WQ-136** registered: rows 72/73 re-scope, Will's call.

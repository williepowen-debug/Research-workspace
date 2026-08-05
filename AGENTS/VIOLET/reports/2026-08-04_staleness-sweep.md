# VIOLET — staleness / open-items sweep · 2026-08-04 ~21:00 ET

**Scope as given (Will):** *"a sweep for any stale/old data in VIOLET. Anything open/incomplete?"* Mechanical, not from memory: file inventory by git vintage, ledger last-rows, date-stamp scan across every live surface, KB lifecycle audit, reference-count scan on `research/`, and the boot staleness contracts.

> ## 🔴 THE HEADLINE: the sweep found a live market event, not just doc rot.
> **SKEW collapsed to 126.41 on the 8/4 settle — −13.55 pts / −9.68%, the 6th-largest one-day drop in three years and effectively the 3-year low** (0.3rd pct of n=734; 3y min 125.77). My dashboard carried **139.96 [8/3]**. The print had been public since **17:00 ET**. → **KB-VIO-186**, and the dashboard is now on a full 8/4 SETTLE basis.
> 🔑 **How it was missed is the transferable part.** I closed out at ~15:00 on a TICK basis having *correctly labelled* "SKEW — 8/4 print publishes 17:00." **A labelled gap is not a filled gap.** That is the third instance today of writing down that I could not see something and treating the label as the remedy (MOVE: five sessions; FRED: retracted within the hour; SKEW: this).

---

## 1. FIXED THIS SWEEP

| # | What was stale | State found | Action |
|---|---|---|---|
| 1 | **SKEW 8/4 settle** | dashboard on 139.96 [8/3]; 126.41 published at 17:00 | ✅ Verified at 2 sources (CBOE `last_trade_time` 2026-08-04T17:00:18 + yfinance), filed **KB-VIO-186** |
| 2 | **All `^`-index rows on a 15:00 TICK basis** | market closed 16:00, 4h earlier | ✅ `thresholds.py --supersede` → VX_DAILY 8/4 **SETTLE**; dashboard rebuilt on settle |
| 3 | **Canary ledgers not on the settle** | CHEAP_TAIL/JPY_VOL/OVX/IMPLIED_CORR last = 8/3 or TICK | ✅ All four re-run; **cheap-tail 2/4 → 1/4**, implied-corr TICK→SETTLE (COR1M 7.19) |
| 4 | **`CANARY_MAP.md` — 5 `CURRENT` cells 5–11 days stale** | **MOVE carried no current value at all** while the instrument made an episode high (83.02); COT carried +3,098/p92.9 after the sign flipped to −12,289/p76.9; JPY carried a CALM 7/30 read across a first-ever FIRE *and* its stand-down; OVX carried 7/27 levels through a −21% collapse; cheap-tail carried 7/29 across the episode's only ARMING 3/4 | ✅ All five refreshed + the diagnosis stamped on the file |
| 5 | **Convergence matrix** | Skew vector scored 2 on "chopping around 140" | ✅ Cut **2 → 1** (3y low); score **21 → 20/55**, verified mechanically |
| 6 | **`FLOW.tsv` missing today's formal send** | BIN-A proposal to PROME unlogged | ✅ Row added (`FLOW.tsv` = formal sends only) |
| 7 | **KB lifecycle** | 5 April *value-snapshot* rows still ACTIVE | ✅ `KB-VIO-001..005` → **STALE** with closing dispositions. ⚠️ Scoped deliberately — structural rows of the same vintage (`-006`, `-010`, `-011`) **left ACTIVE**; their age is not staleness |
| 8 | **Analog-table sources invisible** | all 7 crisis-analog corpora at **zero inbound references** → retirement candidates under the >60d rule | ✅ **Did NOT archive.** Cited them from the MEMORY analog table instead — see §3 |

## 2. STILL OPEN / INCOMPLETE

**Owed deliverables**

| Priority | Item | State |
|---|---|---|
| 🔴 | **BIN-A re-base ruling** | Delivered 8/4 to `outbox/` + `PROME/inbox/`. **Awaiting Will.** `KB-VIO-090` untouched. If ratified I owe: implementation in `fred_fetch.py`, `PROME/GATES.tsv` registration, and repointing ~8 surfaces citing the old lines |
| 🔴 | **8/5 SOQ grade** — tomorrow | Official CBOE SOQ, line >20.45. From 16.50 needs **+24.0%**. Score all four items; **two repaired premises under it**, not one |
| 🔴 | **8/7 triple header** | NFP 8:30 · COT report-date 8/4 15:30 (first that post-dates the yen move) · **KB-VIO-174 credit bands resolve on the 8/7 data print** — grade mechanically, do not re-derive |
| 🟠 | **DAEDALUS ratchet packet — UNANSWERED** | 5 days old. `TRADE.md:112–117` arms 1-of-3, stands down 3-of-3. Owe either the rationale-on-the-line or `P(all three benign \| escalated)`. **Pairs with the re-base and the rising-vol gate — one connective-counting discipline, do them together** |
| 🟠 | **Rising-vol design (Option 1)** | Sequenced 3rd. ⚠️ **The re-base changed its premise: no credit-keyed trigger has a measured edge at VIX 16.5**, so its trigger must come from another channel |
| 🟠 | **Re-run the re-base on pre-2023 history if it can be found** | Rests on **~7 episodes, no credit crisis in sample**. FRED truncation survives an authenticated API call (KB-VIO-185). DEWEY/LIQUID may hold older pulls |
| 🟠 | **Will-facing Artifacts — 5 days stale** | Both last refreshed **7/30**. Their own trigger is *material vol shift · post-FOMC · material agent-state change*, and today cleared it several times over (SKEW 3y low, MOVE re-banked, canary stand-down, credit retrace, re-base). **Not refreshed — flagging rather than republishing unasked** |
| 🟡 | **MOVE feed source order** | Registered defect: yfinance is primary and unreliable; invert to investing.com primary / yfinance cross-check. **Not built** |
| 🟡 | **Grading-note sweep** | n=4 instances. No mechanism asserting `CATALYSTS.tsv` note figures still match their KB source. **Not built** |
| 🟡 | **Issue-level HY breadth** | **6th ask** to LIQUID. The discriminator between broad widening and a CCC-cohort artifact |
| ⚪ | **`H4` implied-corr lead test** | Time-gated. `IMPLIED_CORR.tsv` has **4 rows**, cannot be backfilled, needs ~40+. Not before ~September |
| ⚪ | **NAAIM + ICI equity positioning** | `equity_positioning.py` **not built / not wired**. Standing gap, carried deliberately |

**Known data gaps (labelled, not defects)**

- `IMPLIED_CORR.tsv` is **missing 8/3** — no boot ran that day and `^COR*` has no daily history, so it is **permanently unrecoverable**. The 8/4 `+27.5% d/d` reads against an 8/3 close of 5.64 recovered only from CBOE's `prev_day_close`.
- **EuroHY / EM_HY** still 7/31 — not re-pulled since.
- `VX_M1_HISTORY.tsv` / `VX_TERM_HISTORY.tsv` last **7/29** — 4 sessions stale. Not load-bearing today (the 0.591 forward beta is derived and registered), but the 8/5 SOQ grade cites that beta, so **refresh before grading**.
- **FRED credit history is capped at ~3 years** (2023-08-07) across 4 access paths incl. an authenticated API call → KB-VIO-185.

## 3. THE JUDGMENT CALL I MADE — and why I overrode the retirement rule

The closeout rule says: *a file >60 days old AND not boot-read AND not referenced by a live doc → `git mv` to `archive/`.* **Seven crisis-analog source files matched all three conditions** (Feb-2018 Volmageddon, Mar-2020 COVID, Feb-2021 meme; `refs=0` verified twice).

**I did not archive them.** They are the evidence base under the **live** CRISIS ANALOGS framework in `MEMORY.md` and `thesis/VIX_THESIS.md` — and I had, hours earlier, written *"this configuration is not in my analog table"* as a load-bearing statement about the SKEW collapse. **Retiring the corpus under a framework I was actively reasoning from would have been the rule defeating its own purpose.**

🔑 **The zero-ref count was the actual finding: the analog table used its sources without ever citing them.** That is what made a live evidence base look retirable. **Fixed by adding source citations to each analog row**, so the next sweep sees them as referenced — and the general form is now recorded in `MEMORY.md`: **a live doc that cites nothing makes its own sources look retirable.**

## 4. THE PATTERN WORTH ACTING ON

**`boot.py` printed `🔴 CANARY_MAP STALE 'CURRENT' CELLS — 2` on the morning of 8/4. I read it and did not act.** Every one of those five cells *already* carried a parenthetical confessing a prior staleness incident (*"this cell read X until 7/28 — 11 days stale"*). So this is **n=4 on the same file**, and the diagnosis has to change:

> **Detection was never the gap. Acting on detection is.** The >4d contract works and fires on time. **A boot warning that is read and not actioned is indistinguishable, at the file, from no warning at all.**

The honest fix is **a closeout step that refuses to complete while a staleness contract is red** — not a better alert. Same shape as the three "labelled gap ≠ filled gap" instances today. **Not built; recorded here and in `CANARY_MAP.md` so it is not re-discovered.**

# BRENT SCRATCH — Wed Sep 2, 2026 ~18:0x ET

**Purpose:** Ephemeral session handoff — canonical "where are we / what next". Read at boot (step 2), rewritten at closeout (step 11).

> # ⛔ READ FIRST — THE THREE THINGS THAT CHANGE HOW YOU WORK TOMORROW
>
> **① BASIS DISCIPLINE IS NOT A SOLVED PROBLEM ON THIS DESK — IT FAILED TWICE IN ONE DAY.** Every Brent figure NAMES **(a) the CONTRACT** and **(b) the BASIS (settled close vs live intraday bar)**. On 9/1 I wrote a 17:5x live bar (`$95.22`) into STATUS as a *close*; the settled close was **`$94.65`**. I corrected that this morning — **and then reproduced the identical defect four hours later**, putting a 15:05 bar (`M1−M3 +$6.72`) into a ladder whose other rungs were all closes (true close figure **`+$6.43`**). ★ **Writing the guard is not obeying it. Only re-pulling on ONE declared basis caught the second one.** Canonical `BZX26` closes: **8/26 `86.94` · 8/28 `88.10` · 8/31 `90.49` · 9/1 `94.65` · 9/2 `95.23`.** ⛔ `BZ=F` still banned for deltas.
> **② THE BAKER HUGHES URL ROTATES *AND* THE PRIMARY IS NOW 403-ING.** Picker first at every rig grade: HEAD every uuid on `na-rig-count`, **pick by the DATE in `content-disposition`, NEVER by link text** (the index also lists a year-stale archive whose link also says "New Report"). ⚠️ **NEW: `instrument_check` has probed `BRT-26-RIGS` DEAD (HTTP 403) on BOTH 9/1 and 9/2.** `curl` cannot reach the BH primary from this box; **`urllib` can.** Budget time for that before Friday's print.
> **③ THE REGIME VERDICT IS A PROMPT SQUEEZE, NOT A BULL MARKET.** Throughput impairment is **DEAD** as a claim I may carry (Goldman `~2/3` of pre-war ≈ `59/day` vs the retired `>35/day` bar). What survives: **"the barrels move, and the risk of moving them has not re-rated"** — insurance + delivered-cost legs only. **`$100` is NOT a live threshold — it fired 7/23. The next registered rung is `$120` and it needs a NEW event class.**

---

## ✅ WHAT THIS SESSION DID

**Boot → Will POV → STATUS/TRADE write → full closeout. `$0` moved, no `BRT-xx` graded, no threshold or gate touched.**

- **Inbox 3 → 0.** All three WALTER signals logged + archived. **`SIG-W-20260901-011` (Edouard) ACTED — I closed the question WALTER deliberately left open:** Valero Port Arthur (385 kb/d) partial blackout Tue night, smaller **AVU-147 CDUs SHUT**, larger **AVU-146 at minimum runs**; **Motiva (656.4 kb/d), Exxon Beaumont, TotalEnergies (238 kb/d) ALL NORMAL** [Reuters via TradingView/oedigital + qcintel 9/2]. **Run-cut CONFIRMED but NARROW.** `-010` Ust-Luga and `-014` Iran declaration noted (other desks' action).
- **WPSR wk-8/28 pulled twice, independently, agreeing to the decimal** (my 15:19 pull + the 11:3x autonomous routine): commercial **424.5M (−4.45M)** · SPR **286.604M (−3.12M)** · Cushing **22.51M (+0.08M)** · **refinery util 98.0% 🔴 leg high** · gasoline demand YoY **−1.61%** (deepening).
- **THESIS v5.7 → v5.8 (minor): THE TIMED RACE RE-CLOCKED AND ONE OF ITS TWO CLOCKS REVERSED.** vs the June wk-6/12 calibration: combined draw **−17.2M/wk → −7.57M/wk (44% of pace)**; **Cushing 20.03M AT the floor → 22.51M, REBUILT +2.5M, moving AWAY.** ⇒ the up-whipsaw branch is **DE-CLOCKED, not refuted.** **The SPR is the only buffer still counting: `34.2M` over the `252.4M` statutory floor at −3.12M/wk ≈ `11 weeks` ⇒ ~mid-November 2026.** CHANGELOG entry written.
- **TRADE.md first mark refresh in 6 days** (Will-asked). Four legs **$6,442.48 → $7,829.95 (+21.5%)**, driven almost entirely by the Oct-16 135C (+68.9%). **`N_eff = 1` unchanged — the gain is ONE factor working, not four.**
- **`consumer_check` on the 9/1 correction ⇒ 9 🔴 on live surfaces.** Packets sent to **WALTER** (4 hits) and **PROME** (2 hits, one written TODAY at 13:4x = live propagation). Dated TSV history rows deliberately EXCLUDED.
- **TRACKER registered-alert-lines block: lines 7–11 refreshed, 1–6 verified current.**

## 🔴 THE FINDING THAT IS BIGGER THAN THIS SESSION

**`demand_destruction/TRACKER.md` lines 7 (rigs) and 8 (COT) sat a FULL PRINT STALE FOR FIVE DAYS.** Both were graded on 8/28 with zero latency and written to STATUS — **and neither was written back to the block THREE CLOUD ROUTINES READ AT RUN TIME.** ★ **Both autonomous routines (8/26, 9/2) re-stamped SCOPED-PARTIAL correctly and correctly scoped themselves to lines 1–6. The routines did their job. NOTHING OWNED THE HOP from "grade taken" to "machine-read block updated."** `[[finding_transfer_completes_only_when_the_receiver_encodes]]` — flagged to PROME as **plausibly fleet-wide**: any desk whose grades feed a machine-read surface has the same unowned hop.

## ⏳ NEXT SESSION (dated, future-verifiable)

| when | what |
|---|---|
| **Fri 9/4** | 🔴 **THE FRIDAY PAIR — both now have a CATALYSTS row (they had none).** Baker Hughes ~13:00 (**picker FIRST; primary 403 on 9/1 AND 9/2 — use `urllib`**); ladder 447, needs **+2.5/wk** over 4 prints vs a negative pace. COT as-of **Tue 9/1** ~15:30 (`f_disagg.txt` primary, not Socrata). ⛔ **DO NOT LET THEM STACK.** |
| **Sun 9/6** | 🔴 **OPEC+ Q4 — FROZEN LETTER pre-registered.** Graded on the STATEMENT, never a relay (the 8/2 error). ⚠️ At ~**0.02 mb/d** effective spare a quota INCREASE is close to a paper event. |
| **~Tue 9/8** | DOCKET L198 ①② re-dated reads · Russia diesel Q1 decree text · matched Dated-Brent physical-vs-paper. |
| **Wed 9/9** | 🔴 **SPR exchange-window test** — AND the **row is now EXTENDED**: the same wk-9/4 WPSR is the **first instrumented read of Edouard**. **Pre-registered so it cannot be fitted after the fact:** >~1pp utilization fall ⇒ the outage was **under-disclosed**; flat-to-−1pp ⇒ the narrow read was right. |
| **Fri 9/18** | 🔴 **USO 150/165 spread EXPIRY — now has a CATALYSTS row (it had none, despite being the earlier of the two expiries and the one under active question).** |
| **Wed 9/30** | XLE 65C expiry · `BRT-12` and `BRT-29` both resolve. |

## 🔓 OPEN THREADS / DEBT

- 🔴 **READ-CAP — NOW THREE SURFACES OVER, WAS TWO.** `board_log.tsv` **536%** · `TRADE.md` **320%** · **`STATUS.md` 101% (crossed during the 9/1 session; today's writes added to it).** ⛔ **Remedy is a Will-approved rotation, not a closeout trim. Re-flagged to PROME today.**
- 🟠 **`XLE Sep-30 65C ×2` CHANGED CHARACTER AND NOBODY RE-ASKED.** Its **LAPSE** disposition was set when it was dying at 4.1% OTM / −59%. It is now **0.1% ITM at XLE $65.10, delta 0.539, P(ITM) 51.1%, mark −25.8%.** **A LAPSE call on a coin-flip is a different decision from a LAPSE call on a corpse.** Flagged to Will/TERRY; **not re-dispositioned by me.** `[[finding_dated_carry_item_has_no_expiry_check]]`
- 🟠 **Root `CLAUDE.md` § DOMAIN SCOPE carries `~$5,131 at market` [8/4 broker vintage] — now ~$2,700 light** vs my $7,829.95 pull. **Will-gated file, outside my commit boundary — routed to PROME, not edited.**
- ⚠️ **`INCIDENTS.tsv` — 12 ACTIVE rows past the 60d re-verify budget** (oldest RF-004 at 167d) + 6 present-tense rows the budget doesn't cover. **The one real ledger debt; a research job, not a sweep.** ⛔ **Ust-Luga 9/1 NOT logged: no facility damage, no throughput loss and no operator/tank specifics were established — a fire in a port area is not facility damage evidence** (LESSONS #1). HAWK owns the cross-theater ledger; check `AGENTS/HAWK/` before ever logging it.
- ⚠️ **`catalyst_countdown.py` fork still lacks OTTO's fired-row rule** (0 `fired` refs).
- ⚠️ **`NEXUS_BRIEF.md` is `234` lines against its provisional `100`-line cap — it was ALREADY `215` before this session and I added `19`.** Per its own rule the compression comes **upward from FORWARD CATALYSTS/VIEW**, protecting CROSS-DOMAIN + CALIBRATION-divergence. **Not done today — flagged rather than hidden;** the overflow is dated 8/28–8/31 retained history, so the cut is a rotation decision, not a trim.
- **TERRY:** decoupling-vs-XLE falsifier slot NAMED BUT EMPTY on a filled position. Top open item, unchanged.
- **Energy HY OAS: PERMANENTLY UNMEASURED here;** LIQUID owns the systemic leg.

## 💼 POSITIONS

**NONE PROPOSED. `$0` moved.** **USO 35 sh · USO Oct-16 135C ×2 · USO Sep-18 150/165 ×1 · XLE Sep-30 65C ×2.** `TRADE.md` canonical, **marks refreshed 9/2 post-close (first in 6 days)**. **The Sep-18 spread is the one leg my own thesis argues against** — ~19% to break even, $125 of $300 recoverable now, needs a spike that HOLDS while my read is spike-and-fade. **Disposition Will's, construction TERRY's.**

## 📬 MAIL

**Inbox 0** (3 consumed, logged, archived). **Outbox clear.** **Packets sent this session: WALTER ×1, PROME ×1** (both the 9/1 close correction; PROME's also carries the root-`CLAUDE.md` stale-book-value flag, the read-cap re-flag and the TRACKER unowned-hop finding). The autonomous routine independently filed its own SPR packet to PROME at 11:3x — **checked for conflict, none; it agrees with my pull on every figure.**

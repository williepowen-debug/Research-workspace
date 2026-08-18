# VIOLET SCRATCH — August 18, 2026 (Tuesday, boot session ~09:20–10:15 ET — **market PRE-OPEN, basis TICK. FLAT.**)

> **Scope as given: "boot up."** First VIOLET-authored session since **8/10** — eight days dark, and the gap is where most of this session's findings came from.
> **🔑 The session's shape: the boot was clean and the boot was wrong.** All 14 stages passed, and **the single most important session on the tape (8/17) was missing from four of my instruments** because yfinance silently dropped it. The N5 capture-time rule — adopted while I was dark — is the only reason I found it: it forced me to establish the provenance of a pre-open print instead of writing it down.

---

## CHANGES SINCE (8/10 → 8/18) — *eight days dark*

| | 8/10 | 8/14 | **8/17 SETTLE** | 8/18 tick |
|---|---|---|---|---|
| VIX | 15.46 | 14.25 *(episode low area)* | **15.19** (+6.6%) | **15.78** [PROVISIONAL] |
| VVIX | 92.51 | 87.48 | **93.92** (+7.4%) | — |
| SKEW (daily) | 137.13 | 138.36 | **142.91** (+4.55) ← **back >140** | — |
| **SKEW 20d avg** | 142.11 | 140.02 | 🔴 **139.86 — REGIME TERMINATED** | — |
| VIX9D | — | 10.61 | **12.39 (+16.8%)** ← biggest mover | — |
| VIX3M/VIX | 1.2206 | 1.2954 | **1.2535** (flattening) | — |
| MOVE | 75.46 | 69.58 *(below F1)* | **75.63** (+6.05) ← re-armed leg 1/2 | — |
| COR1M | 7.82 | — | — | **8.47** (+25% off the 7/31 low) |
| COT lev money net | — | — | **−12,127** [8/11 report] | — |

**Also while dark:** RED-FT-06 **FIRED** 8/11 (VIX 15.28 = 5 of 5). VIX printed its episode low **14.25 [8/14]**. N5 fleet canon ratified 8/11 and **amended 8/13 (capture-time clause i-b)**.

---

## WHAT I DID

1. **Processed the entire WALTER lane — 8 signals, backlogged 11 days** (8/07 → 8/13), all disposed with reasoned notes and `git mv`'d to `processed/`. Board log 48 → 56 rows. **Two carried direct asks to me and both are answered below.**
2. **🔴 FOUND THE REGIME TERMINATION.** Recomputed the SKEW 20d-avg (stale since 7/30): **139.86 on 8/17 — first sub-140 since 2026-06-04.** The regime that re-established 6/5 ran **49 td**. Verified it is **mechanically robust**, not a one-day wobble: window roll-off keeps it sub-140 for ≥10 sessions even if daily SKEW holds; reversing it next session needs **≥154.43**. → **KB-VIO-192**
3. **🔴 FOUND THE 8/17 BROAD VOL BID** — every gauge up together, **front-led** (VIX9D +16.8%). Explicitly graded it **NOT the coiled spring** (that needs VIX+VVIX *falling*). → **KB-VIO-193**
4. **✅ ANSWERED WALTER'S UNRESOLVABLE ASK.** WALTER wrote *"I cannot see the gross legs — a net is two numbers pretending to be one."* My `COT_VIX.tsv` was **missing the 8/04 report entirely**; `--backfill` recovered 189 rows. **93% of the +16,062 flip was NEW LONGS (+14,961), 7% covering (−1,101) — then it round-tripped at a loss by 8/11.** → **KB-VIO-194**
5. **✅ GRADED THE 8/5 SOQ — 13 DAYS LATE.** It was SCRATCH's #1 🔴 priority on 8/4, pre-registered, and **nobody came back for it.** Line >20.45 **NOT MET**: 8/5 opened 16.15, high **18.43**. Fade verdict ✅ · no-re-entry ✅ · TERRY beta **not graded** (honestly recorded, not scored by assertion) · HENRY steelman ⚠️ partial. → **KB-VIO-196**
6. **✅ REPAIRED THE DATA LAYER.** Backfilled VX_DAILY (8 missing sessions), recovered **8/17 from the CBOE primary** after yfinance returned a partial date, filled 47 blank cells, corrected a **wrong 7/31 VIX (16.57 → 15.99)** that had my ledger disagreeing with the fleet on a session load-bearing for a fired trigger. → **KB-VIO-195**
7. **✅ RECONCILED CATALYSTS.tsv ↔ CALENDAR.md**, which had genuinely diverged (CALENDAR still said *"Aug 5 (tomorrow)"* on 8/18). Pruned 4 fired rows, **added a RESOLVED section** so a grading obligation no longer dies with the row that carries it. Added COT 8/21, Aug CPI 9/11, MU ~9/29 (flagged DATE-ESTIMATED).
8. **✅ ANSWERED PROME'S DOORBELL** on cheap-tail: count is **2/4, not 3/4 — the spawn-sooner clause does NOT fire** — but the composition **rotated** (8/14 L1+L2 → 8/17 L2+L3). PROME was right that 1/4 was stale and right to claim exactly one leg.
9. **✅ DISCHARGED THE VIX 14.55 CONFIRM** owed to PROME — independently verified at the CBOE primary (8/12 close 14.55).

---

## NEXT SESSION (priority-ordered)

1. 🔴 **GRADE TWO REGISTERED LINES ON TODAY'S SETTLE — both resolve today and both are at session 1 of 2.** **MOVE re-arm** (≥72.41 ×2; 75.63 [8/17] = session 1) and **COR1M first-tell** (≥8.43 on 2 consecutive **SETTLE** closes; 8.47 [8/18] is a **TICK** and does not count). **Grade the letter, not the summary** — the tick/settle distinction is the whole test.
2. 🔴 **MAKE CBOE `*_History.csv` PRIMARY for the VX_DAILY spot series; demote yfinance to cross-check.** This is the **second** feed needing this exact inversion (MOVE was the first, KB-VIO-177) — and the first one had to be learned twice. **Mechanism, not content.** ⚠️ **`cheap_tail.py` is downstream of the same hole and currently prints a 4-day-old state as current — fix it in the same pass.**
3. 🔴 **Backfill `IMPLIED_CORR.tsv` 8/11–8/17.** ⚠️ **CALENDAR says this series "cannot be backfilled"** (no `^COR*` daily history on yfinance) — **if that is still true, then the COR1M first-tell can never be graded on a session I did not boot, and that is a defect in the REGISTRATION, not the data.** Either find a source or re-spec the trigger.
4. 🟠 **RISING-VOL DESIGN (Option 1) — docketed at `next-VIOLET-session`, i.e. it is owed NOW.** PROME's 8/18 packet: the row has **no market clock**, which is why it has waited 18 days. **New input this session is exactly what it needs:** a live front-led bid, a terminated SKEW regime, and two registered lines at 1-of-2. **Do not design it against legs I cannot reliably measure** (see #3).
5. 🟠 **Send NEXUS the fresher SKEW.** It is carrying **135.59 [8/11]** and explicitly asked for a newer print; I have **142.91 [8/17]**, which is **through the 140 line RED owns.**
6. 🟠 **DAEDALUS ratchet packet** (`TRADE.md:112–117`) — still unanswered since 8/4.
7. 🟠 **BIN-A re-base** — delivered 8/4, awaiting Will. Unchanged.
8. 🟡 **Process the remaining top-level inbox** (8 files, incl. 3 DAEDALUS packets from 8/17). **Not done this session — MAIL rule says inbox is a separate spawn**, and I am flagging rather than silently skipping.

---

## CARRY-FORWARD

- **🔑 A CLEAN BOOT IS NOT A COMPLETE BOOT.** 14/14 stages green, and the tape's most important session was absent from four instruments. **The failure was a PARTIAL date — yfinance returned `^VIX3M` for 8/17 and nothing else** — which is invisible to every check I own, because they all test "did the stage run," not "does the stage's own source have holes." `backfill.py` literally printed *"touched 36 rows"* while leaving the hole it exists to fill.
- **🔑 THE RULE I ADOPTED WHILE DARK IS WHAT CAUGHT IT.** N5 (i-b) says *establish the instrument's own clock before quoting a reading.* Applying it to a routine pre-open print (15.78) is what sent me to the CBOE primary, which is where 8/17 was. **A discipline adopted for one purpose paid out on a different one — and it paid because I ran it on a number I had no suspicion about.**
- **⚠️ A GRADING OBLIGATION DIES WITH THE ROW THAT CARRIES IT.** The 8/5 SOQ was pre-registered, cheap to grade, marked 🔴 as the #1 next-session item — and went 13 days unexecuted, on track to be deleted when its CATALYSTS row was pruned. **Pruning has a trigger (the event fires); grading has none.** That is the *same structural gap* this file's own 8/4 notes had already documented for macro-row replenishment. **Found twice, fixed neither time — fixed now, with a RESOLVED section.**
- **⚠️ THE COUNT WAS RIGHT AND THE INSTRUMENT WAS DIFFERENT.** Cheap-tail read 2/4 on 8/14 and 2/4 on 8/17 with **not one leg in common with what it was measuring** (L1+L2 → L2+L3). Second instance of KB-VIO-178's rotation class in two weeks. **A scalar that repeats is not a state that persisted.**
- **⚠️ I ALMOST SHIPPED A WRONG PREDICTION INSIDE A CORRECT FINDING.** I wrote in STATUS that a live cheap-tail re-run "would print 0/4" — reasoning from the two legs I had just watched fail, without computing the two I hadn't. It prints **2/4**. **The finding was right, the extrapolation off it was wrong, and the extrapolation is what a reader would have acted on.** Caught only because PROME's doorbell made me compute it.
- **⚠️ FOUR OF MY LEDGERS HAD HOLES FROM IRREGULAR BOOTS** (VX_DAILY 8 sessions · COT 1 report · IMPLIED_CORR 5 sessions · CHEAP_TAIL). **A weekly/daily feed on an agent that boots irregularly loses data silently** — the boot fetch pulls the LATEST, never the SKIPPED. Two were backfillable, one may not be.

---

## OPEN HYPOTHESES *(flagged, not actionable)*

- **The dispersion regime is unwinding, and that alone lifts VIX without any new fear.** COR1M +25% off its low while constituent-vol EST fell 63.2 → 54.2. Through 8/4 I argued a sub-16 VIX was *partly arithmetic*; **the same arithmetic now runs the other way, and I have not tested how much of the 8/17 move it explains.** Needs a decomposition, not an assertion.
- **The 8/17 front-end bid may be expiry mechanics, not fear.** VIX9D +16.8% two sessions before the **8/19 monthly expiry**, with 8/19 carrying 3.63M call OI. **Pin/roll is an untested alternative and I did not discriminate it.** Do not read the front-end move as signal until this is ruled out.
- **Positioning is offside and 5 sessions blind.** Leveraged money is net short vol after a failed long, and the 8/18 COT (publishes **Fri 8/21**) is the first read that sees the 8/17 bid. **If they are still short into a rising surface, that is a squeeze setup — but it is a hypothesis about data I do not have yet.**

---

*Basis note: every `^`-index figure above is the **8/17 SETTLE** unless marked TICK/PROVISIONAL. VIX 15.78 is a pre-RTH 8/18 live bar (verified against CBOE `prev_day_close` 15.19 / `last_trade_time` 2026-08-17T16:15:01) and **is not a close**.*

# RED STATUS — folded blocks, S44 header + three resolved TOP-PRIORITIES rows

**Folded:** 2026-09-14 (S45, PROME WQ-184 Tier-1 spawn on DOCKET L341/L344) · **Reason:** READ_CAP budget rotation — `STATUS.md` stood at **32,297 B = 99.2% of the 32,550 B cap** with 253 B of headroom, and S45 had to write the FT-10/FT-11 grades dated today. **Nothing here is edited, resolved, or retracted — every block is verbatim.**

⚠️ **Rotation is not resolution.** The S44 header's live state is carried forward into the S45 header in compressed form; the three priority rows below were folded because their dates (**8/31 · 9/3 · 9/4**) have all PASSED and their items are resolved or superseded — they were sitting under a header that says *live*. `[[finding_live_claim_in_a_closed_container_is_invisible]]`, inverted: a CLOSED row under a LIVE header manufactures work.

---

## 1 · S44 `Last Updated` header (verbatim) — 3343 B, crc32 `1911721231`

**Last Updated:** 2026-09-12 13:5x ET [`date`-verified] — **S44 (PROME Tier-1 due-row spawn, DOCKET L320): three owed grades written; the gate that should have caught a fourth problem was hard-wired green.** **(1) 🔴 `RED-FT-10` = 1 OF 4, new run opened 9/11.** `^SKEW` **154.49 [09/11]**, **re-confirmed by RED at the publisher of record** (`SKEW_History.csv`, own pull 2026-09-12 13:50:10 ET, HTTP 200, 202,960 B, 9,226 rows). VIOLET delivered it from CBOE's **delayed-quotes API** and wrote no count; **caveat DISCHARGED, not laundered** — archive == quote exactly, `prev_day_close` 147.02 matches the 9/10 cell, +44 B / 2 bars at 22 B/row. 🔴 **EARLIEST FIRE IS WED 9/16, NOT 9/15** (the 9/15 chain assumed 09/10, which printed 147.02). **9/16 = FOMC + SEP + VIX SOQ**, disclosed pre-data. ⛔ `HEARTBEAT.md` carries *"earliest fresh fire 9/15"* ×2 — **PROME owns it, packeted.** **(2) `RED-FT-11` v1.1 NOT MET, WRONG SIGN; L320 DISCHARGED.** FRED DGS30: Δ5 **+12.0bp** (endpoint) / **+10.0bp** (t−5) vs **≤ −10.2bp** — **convention-independent, both >20bp the wrong way**; leg (iv) fly Δ5 **−2.0bp** vs ≤ −4bp ⇒ second path also not met. v1.1 ACTIVATED but **never APPLIED** (one window, non-firing). DGS30 **9/11 unpublished** (FRED frontier 9/10 on six series, T+1) — **not carried forward.** ⚠️ **Against RED's own instrument:** same window, **the 30Y moved LEAST on the curve** (DGS2 +22 · DGS5 +23 · DGS10 +18 · DGS20 +14 · **DGS30 +12**; 2s30s 91→81) — the *relative* footprint a buyback leaves, invisible to an **absolute** Δ5. **BOND's 8/27 aim-critique as a measurement**; routed to BOND as a joint-design question, **not re-spec'd** (ML-RED-240). **(3) `RED-FT-06` exit = 0 OF 5; WALTER's direction correction ABSORBED.** VIXCLS **17.84 [9/10]** = **0.16 under** the ≥18 bar after **five consecutive higher closes**; WALTER's *"moving AWAY"* self-corrected 9/11 (FRED T+1 trap). **The count was never the issue; the trajectory was.** **(4) 🔴 ONE PUBLISHER, TWO ARCHIVES, OPPOSITE ANSWERS ON WHETHER A DAY WAS A SESSION.** CBOE's `VIX_History.csv` carries **09/07/2026 = 15.30** (Labor Day, closed); its own `SKEW_History.csv` omits it, SPY/`^GSPC` have no bar, FRED + yfinance inherit it. **Census: 50 such dates, 34 since 2020, last 20 = every NYSE closure.** **Ruled PRE-DATA:** FT-06's exit counts **trading sessions**; a holiday observation is **bridged**. Free today (no holiday in 09/14–09/16); **bites Thanksgiving 11/26.** KB-RED-100 / ML-RED-238. **(5) 🔴 THE APPARATUS FAILURE, THE WORST ITEM HERE.** `boot.py` §⑤ — whose docstring promised it would be *"loud in exactly the failure mode"* — **read its own HEADER ROW as data**, so `max(timestamp_read)` compared the literal `"timestamp_read"`, which sorts above every date. **Not lossy — hard-wired green**, while **27 action-addressed signals sat unlogged, oldest 154d.** Rebuilt as an **ID-diff, no date floor, 3 ledgers, `action:` + legacy `to:`**; **14/14 falsification tests** at `scripts/test_board_gap.py`; **all 27 dispositioned** ⇒ ✅ **unlogged 0** on PROME's independent `exempt_gap.py`. ML-RED-239. **NO WEIGHT MOVED: net-bear 58, conf 68 [9/6] stand** — three non-fires and two repairs move nothing; **5 of the 27 were signals RED had acted on and cited by name without logging the id.**

---

## 2 · TOP ADVERSARIAL PRIORITIES rows 2–4 (verbatim)

**row 2** — 189 B, crc32 `1506371510`

2. **🔴 Mon 8/31 post-16:15 ET — MIDAS-06 verifier duty** (RED holds `resolution.verify` on Q-…006a; four-branch letter in a binary ledger; ⛔ do NOT verify (d) INDETERMINATE as NO).

**row 3** — 247 B, crc32 `1123184154`

3. **🟠 Thu 9/3 — 30Y JGB (CHG-047 / CH-009 / CH-012).** SAM rail perimeters STATED. **VX-RED-004 CLOSED S38e as FLIPPED-BEAR-TERMINAL** (rather than fake-re-specced with a level RED could not base-rate without SAM's series; ML-203 practiced).

**row 4** — 1409 B, crc32 `2102435685`

4. **✅ RESOLVED 9/4 (graded 9/6) — August NFP.** **−23K did NOT survive revision (→ +21K); the labour force did NOT stop shrinking — it GREW +683K.** Both legs of the re-test resolved against the bear. → weights moved S41; `RED-23` registered as the revision watch. **🆕 S42 9/9 — `RED-23` AMENDED PRE-DATA on LABOR's CORRECTED cut (their 9/7 retraction), both vintages left readable: the "July ranks 44/44 most-upward-revised" finding is WITHDRAWN at source — on first→third, RED's resolving cut, **July 2026 has no value at all** (only 2 vintages exist). The registered base rate is now **n=39 stage-OK, mean −33.5K, median −39K, SE 8.8K, t=−3.8, 71.8% revised DOWN.** **Confidence HELD at 60% — the NUMBER did not move, the BASIS did:** it no longer rests on an off-horizon n=1, and the arithmetic is now shown — the threshold needs the Jun+Jul+Aug sum ≥ **150K** against **214K** today, i.e. a **−64K** total buffer, while only **August's** leg carries a full first→third cut (Jun is already at its third print, Jul at its second). P(Aug leg alone > −64K) ≈ **71%** on N(−33.5, 55); with an unmeasured −20K from the Jul/Jun legs it is ≈ **58%**. **60 sits inside 58–71 — and the Jul(2→3) and Jun(3→n) distributions are UNKNOWN, declared, not invented.** The uncalibrated flag is **partially lifted**: August's leg is calibrated, the other two are not.

---

**Disposition of each folded priority row, stated so the fold is auditable:**

| row | dated | why folded |
|---|---|---|
| 2 · MIDAS-06 verifier duty | Mon **8/31** | Date passed 14 days ago. The `resolution.verify` duty and the ⛔ do-not-verify-(d)-as-NO caution are preserved verbatim above; if the duty is still open it is an ACTIVE-row question for `CHALLENGES.tsv`, not a STATUS priority line. |
| 3 · 30Y JGB CHG-047/CH-009/CH-012 | Thu **9/3** | Date passed 11 days ago; VX-RED-004 is recorded CLOSED as FLIPPED-BEAR-TERMINAL in the row itself. |
| 4 · August NFP | **✅ RESOLVED 9/4, graded 9/6** | Self-labelled RESOLVED. Weights already moved at S41; `RED-23` carries the revision watch. A resolved item is history, and history belongs in `reports/`. |

*Folded by RED, session S45, 2026-09-14. Byte counts and crc32 values produced by `PROME/tools/measure.py` / `zlib.crc32` at fold time.*

# HANS — SESSION LOG

**Created 2026-09-19 as owed #20, the hot/cold split PROME ruled should be its own task.**
This is the twin of the 2026-09-05 `DISPATCH_LOG.md` split: **a whole CATEGORY moved out, not old rows rotated.** Three rotation passes on 2026-09-19 took `STATUS.md` 91% → 75% of the read-cap budget and it was back to 85% within the hour, because the thing that regrows is **session narrative**, and rotating it only delays the next breach.

---

## 🔒 THE CONTRACT — what lives here, and why STATUS stays small

| Goes HERE (`SESSION_LOG.md`) | Stays in `STATUS.md` |
|---|---|
| **How** a finding was reached; what I got wrong and how it was caught | **What is true now** — levels, fires, states |
| Session-by-session narrative | The prediction book, the catalyst docket, the owed board |
| Defect write-ups and their reasoning | Any caveat that **changes what the next session does** |
| Superseded reasoning kept for provenance | The two-sentence summary |

🔴 **THE TEST, applied per item:** *would a booting session act differently if it never read this?* If no, it belongs here. **If yes it stays in STATUS, however long the file gets** — the byte budget is never a reason to drop a decision-relevant caveat, only a reason to move narrative.
⛔ **This file is LIVE and maintained, not an archive.** It is NOT boot-read; a session reads it when it needs the *why* behind a STATUS line. Rotation of genuinely dead material still goes to `workbook/`.
⚠️ **Newest session at the top.** Each block keeps its pointers to the `workbook/` verbatim files and the `ML-`/`KB-` rows, which remain the canonical records — this is connective tissue, never the primary record.

---

## 🆕 SESSION 5 (2026-09-25) — PROME Tier-1 spawn (WQ-294): `T-10` fire graded, whole inbox drained, `T-07` pinned to a named contract. Records → `registry/HANS_T_FIRED_LOG.tsv` `HANS-F-006` · `workbook/2026-09-25_INBOX_DISPOSITIONS.md` · `KB-HANS-097`–`099`

**How the `T-10` basis was settled:** pulled ideal-investisseur (both legs one screen), TradingEconomics (both legs), the ECB AAA 10Y primary via `fetch_eu`, and the Bundesbank BBSIS Svensson 10Y (keyless, a zero-coupon basis — direction only). The i-i Bund leg matched the ECB primary within 0.4bp; TE ran ~5bp (Bund) / ~8bp (OAT) higher. Tried to reach a Banque de France daily OAT primary: Webstat's Opendatasoft TEC10 dataset exists but returns 0 records keyless, and ECB FM has no FR benchmark — **recorded as a gap, not a verdict** (third time a 'manual' row may merely be unfetched).

**How `T-07`'s fix was tested:** acceptance conditions written first — graded on a NAMED contract on every covered date; the expiry day itself still grades the expiring contract; an exhausted calendar fails LOUD with no `TTF=F` fallback; the continuation stays visible as context. Neighbours: ordinary (mid-month) · overlap (expiry day) · missing information (calendar exhausted) tested; wrong-owner and concurrency N/A (single-owner script, no shared state). The 'never a continuation' test was falsified by injecting the 9/23 defect — it fails. **IMPLEMENTED + TESTED by the author; NOT independently verified.** ⚠️ **The fire broke two old C9 tests**: their fixtures borrowed the then-live OAT 4.47 as a 'current' level, and publishing 4.67 retired it — a test coupled to live ledger data fails when the world moves. Fixtures now isolate the band with a non-numeric level.

---

## 📦 STATUS ROTATION 2026-10-01 — VERBATIM from STATUS (§CARRY FORWARD lines 14–15, §ENERGY line 39 as of 10/01 pre-rotation), rotated for the read cap (75% → under 70%)

- 🔴 **9/25 — `HANS-T-10` FIRED 2026-09-24 (`HANS-F-006`, OPEN): OAT–Bund 109.9bp AND OAT 4.67%, both legs the same day for the first time** (ideal-investisseur; 9/25 intraday 105.4 / 4.63). **Basis settled: i-i GOVERNS** (one screen; its Bund = ECB AAA primary within 0.4bp; the conservative basis). **Fires on TE too** (108.3bp / 4.711, 9/25 intraday) and the margins (+9.9bp / +17bp) exceed the largest logged basis gap — **unlike 9/18, not decided inside the gap.** ⚠️ **~11bp of the OAT's +19bp was common-mode Bund**; ex-common the level leg clears by ~6bp. ⛔ **Cause (budget / government-fall risk) is HEADLINE-ONLY — not established here.** No BdF daily primary reachable. *(Exit registered 10/01, see above.)* → `KB-HANS-097`, `099` (superseded 10/01 by `100`/`102`)
- ✅ **`HNS-06` HIT** — German Mfg flash **53.8** [9/23] ≥50.0 (at secondaries; S&P primary unreadable). Another momentum-continuation HIT. **The FINAL (~10/1) is what `VX-HANS-8.06`/`T-02` take — not the flash.** → `KB-HANS-098`
**9/19 boot pull:** TTF **€79.52** (L2 ORANGE still OPEN, no rung crossed) · EUR/USD **1.15** · DXY **100.22** · euro-area AAA 10Y **3.488% [9/17]**. Market closed Sat — these are Friday closes, no new fire.

*§TWO-SENTENCE SUMMARY, verbatim as of 10/01 pre-rotation:*

🆕 **Session 4's sharper one:** the ECB and ESRB jointly say supervisors **cannot quantify** euro-area bank exposure to private credit — they found €4bn, called it far below what supervisory intelligence implies, and dropped the category — so my `T-14` row, which waits for a regulator to *name* institutions, has been reading clean over a perimeter its own author calls blind; **the offset is that euro-area banks are net borrowers from the non-bank sector, not net lenders to it, so Europe's exposure is to losing that funding in a stress rather than to credit losses on private credit.**

**The Bank of England stopped selling long gilts** — auctions paused, £222bn pre-2035 and £120bn of the longest-dated held to maturity out of £488.2bn — which moved both my UK thresholds *away* from their bands, **but it is a supply withdrawal and not a demand recovery**, and the 11/26 Budget now arrives with the long end's biggest seller stood down. **Session 2 says why it could, and it cuts against my own ECB call:** UK CPI accelerated to 3.1% the day before the hold and euro-area HICP finalised at 3.2%, **yet on both sides of the Channel the entire overshoot is energy and core did not move** — so `T-04` is no longer a hawkish lean into 10/29, and **the one new number to carry forward is German debt service: €41.8bn in 2027 against €30.3bn in 2026, +38% in a year, the Bund at a 15-year high arriving inside the budget.**

*§CARRY FORWARD, two 9/19 bullets, verbatim, rotated 10/01 13:0x (superseded by the 10/01 HNS-07 checkpoint and the current doc_audit count):*

- ⚠️ **`HNS-07` anchor corrected 9/19:** 45d from **gas day 9/17**, required **0.2431 pp/d** vs **0.22 observed** (was 9/18/44d/0.249). **Verdict unchanged, MISS-side.** → `ML-HANS-471`
- 🆕 **Instruments:** `doc_audit` **13 checks** (C9 prose-superseded · C12 key-uniqueness · C13 value/band scale), **86 tests**. **`8.05` German IP −1.6% YoY GREEN→YELLOW** — hard data contracting while surveys drove five refutations of the growth leg; **do not let the PMI read silence it.** **`4.09` UK food: AHDB partly REFUTES the claim that created the row** (wheat −12%, spring barley −19%, but winter barley in line, OSR **+19%**) — alarm marked down.

## 📦 STATUS ROTATION 2026-09-25 — VERBATIM from STATUS §ENERGY (9/19 text), rotated for the read cap (77.5% → under 70%)

✅ **THE 9/10 RULING IS VINDICATED.** WALTER asked whether −14.7pp exited the fire; I ruled **NOT AN EXIT** — 0.3pp was inside the cross-source error. **Ten days later it had widened further** — to −19.7pp on the then-current GEF-norm basis, since re-based to **−15.99pp** single-source `[[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]`.
✅ **9/19 LATE — WILL PROVISIONED THE AGSI KEY AND THE PICTURE CHANGED TWICE.** The exit condition (owed #9) is registered AND its single-source precondition is now satisfied. 🔴 **But the first single-source pull found the instrument had been wrong in BOTH directions:** my carried **−19.7** used a GEF **88.0** norm; `fetch_eu.py` carried a **hardcoded 82.0 frozen on 2026-08-28** and printed **−12.9**. The AGSI-native truth is **−15.99** (fill 69.06% [gas day 09-17] vs an AGSI norm of **85.05%** = mean of 09-17 across 2021–25; median basis −16.61). 🔴 **The frozen constant was the dangerous one: the true norm RISES through the injection season, so a frozen denominator makes the gap read BETTER as time passes — fail-OPEN drift, and it had the fire on the wrong side of its own −15 band.** Fixed: `agsi_norm()` computes the norm from AGSI history and **fails closed — no norm ⇒ NO GAP PRINTED**, never a constant fallback. → `ML-HANS-467`, `KB-HANS-094`
⛔ **DO NOT READ −19.7 → −15.99 AS IMPROVEMENT.** ~80% of it is the denominator. **The fire stays OPEN** by 1.0pp (mean) / 1.6pp (median). 🔑 **AND A SECOND FAILURE MODE, from PROME's negative control, verified by reproducing it:** **a REJECTED AGSI key returns HTTP 200 with an EMPTY array — shape-identical to an unpublished gas day**, so silent expiry prints exactly the message that means *come back tomorrow*, and a desk defers its checkpoint forever. **Now that the norm is AGSI-native a dead key blinds BOTH legs.** Discriminator wired (empty-`x-key` probe ⇒ REJECTED / no-data / BLIND), quirk-dependent, **re-check 2026-12-19** → `KB-HANS-095`.
⚠️ **I nearly refuted that control with a probe that never left my machine** — `curl -H "x-key: "` DROPS the header, so I silently re-tested the ABSENT case and got a reproducible wrong answer twice. **Reproducibility did not rescue it; varying the client did** → `ML-HANS-468`. An injection test then found **two key-resolution paths** I had created an hour earlier → `ML-HANS-469`.
✅ **This morning's fail-closed exit clause earned itself on its first live pull** — had I taken the cross-source −12.9, the row would have looked 2.1pp from an exit on a norm AGSI's own history contradicts.

---

## 🆕 SESSION 4 (2026-09-19) — OWED-BOARD CATCH-UP. **Full read → `workbook/2026-09-19_ESRB_REPORT202602_PRIMARY_READ.md`** · `KB-HANS-090`–`093`

**🔴 ESRB `esrb.report202602` READ AT PRIMARY (owed #4) — EMBARGO DISCHARGED, AND IT WAS RIGHT TO HAVE HELD.** ECB/ESRB joint workstream, Feb-2026, 82pp full-text PDF — not the press release.
**Identified bank credit exposure to private equity / private credit is €4bn** (AIFs €4.5bn) — the report calls it **"far below the figures implied by supervisory intelligence"** and **excluded the class from the analysis** rather than publish it. Fn.4: *"not possible to identify or quantify these exposures accurately."* Ch.5: leverage for PE/PC, hedge funds and most non-EU entities *"cannot be computed from existing data"*, and the non-EU gap is *"likely to remain even if the proposals from the HLTF are fully implemented."*
🔴 **WHAT IT DOES TO MY BOARD: `T-14` is NOT fired — no institution named, no losses tied — but leg (b) waits for a supervisor to NAME institutions, which is downstream of that supervisor being able to SEE the exposure. The sweep has been reading clean over a perimeter its own author calls blind** `[[finding_instrument_reports_clean_against_the_wrong_reference]]`. ⛔ **Band UNCHANGED, deliberately NOT re-tuned** — the tell that I am about to re-tune a leg is that the change would help me.
🔑 **AND IT CUTS AGAINST MY OWN ALARM:** euro-area banks are aggregate **NET DEBTORS** to NBFI (NBFI funds **~15%** of their balance sheets; asset-side linkage **~10%** of SI assets); **US banks are net LENDERS.** ⇒ **the euro-area channel's DOMINANT route is FUNDING, not credit.** ⛔ **This does NOT bound the credit channel** — a net position says nothing about GROSS exposure, and the same report documents asset-side NBFI exposure at **~10% of SI assets with ~a quarter to potentially leveraged entities**. *(Corrected 2026-09-19 on CATO's review: I had written "small **by construction**", which reads net borrowing as protection against gross credit losses. It is not.)* **`HNS-09` keeps 70% and SWAPS ITS BASIS** to this (the HNS-05 lesson — outcome HIT, rationale FAIL — applied *before* resolution).
⚠️ **TWO PERIMETERS, NEVER MERGED:** FSR **€62.5bn drawn / 12 banks / 0.2% of assets** ≠ ESRB **€4bn** identified. ⛔ **NOT claiming it is LARGER** — it is *unquantifiable*. **Routed → LIQUID, REGINALD, PROME.**

**🔴 TWO FAIL-CLOSED RULES REGISTERED, both written BEFORE they bind.**
- **`T-08` EXIT (owed #9)** — it had **none**, so an open fire had no way to close. Now **inside −12pp for 5 consecutive gas days**; hysteresis −15/−12. ⛔ **A blind gas day never counts toward an exit**; ⛔ **no exit on a cross-source basis.** **→ §ENERGY for what that clause caught hours later.**
- **`HNS-07` PRE-COMMITTED RE-MARK RULE (owed #12)** — registered **43 days before the resolver**, which is the point. Checkpoints **10/01 · 10/15 · 10/25**; triggers: required pace > season's best trailing-14d pace (→≤35%), instruments converging off the straddle (→80%/30%), 5+ days net withdrawal pre-10/25 (→≤20%), arithmetic kill (resolve MISS early). ⛔ **AS FIRST WRITTEN — SUPERSEDED THE SAME DAY.** The CATO correction pass below **WITHDREW the arithmetic kill** and **demoted the pace rule to confidence evidence**. Do not apply this list as written. ⛔ **ANTI-CHASE: drift *inside* the range my two instruments already straddled is NOT a trigger — that is what 65% priced.** Anchor (**corrected 9/19 late**): **0.2431 pp/d required** over **45d from gas day 9/17** vs **0.22 observed** — I first keyed it to 9/18 / 44d / 0.249. Verdict unchanged; **a rule nobody re-derives must be right when written.**21 observed**.

**🔴 A BANKING VECTOR HAD BEEN MEASURING A BROAD INDEX FOR THREE WEEKS.** `VX-HANS-5.01` carried **Euro Stoxx 50** (~6,486) against bands **240/210/180** built for **SX7E** (~268) — it could not fire under any outcome, and **C10 and C11 both passed, correctly**: the arithmetic was consistent, the two halves named different objects → `ML-HANS-465`. Restored to **SX7E 313.44 [9/18]**, cross-checked (313.96; deltas agree — **the LEVEL is two-source; the 52-wk range/YTD are single SECONDARY**, `KB-HANS-093`). ⚠️ **GREEN here is a weak negative, not corroboration.**

**STALE ROWS CLEARED — boot §[6] had 5 over 21d, now 0:** **`8.05`** 89d → **−1.6% YoY** (Destatis `PE26_316_421`, rel. 9/7), the basis the row wants; **GREEN→YELLOW**, 0.4pp off Orange — ⚠️ **the hard data is contracting YoY while the surveys drive the fifth-refutation growth picture; do not let the PMI read silence it.** · **`4.09`** the named artifact was found and **PARTLY REFUTES the claim that created the row** — AHDB 8/28: wheat **−12%** and spring barley **−19%** vs 5-yr, but winter barley **in line** and OSR **+19%**; **not a uniform failure**, "food shortages within months" unsupported; alarm **DOWN**, confidence LOW→MEDIUM; the falsifier is **`T-17`**. · **`11.04`** **FROZEN OUT-OF-SCOPE** → HAWK/BRENT (65d stale at RED — a stale RED implies someone is watching when nobody is; ⚠️ do not cite 42.7% as current). · **`4.07`** reviewed, unchanged at 503 — an **annual-programme construct**, so a 22d flag is a **cadence mismatch, not rot**; next real move **12/17**.

✅ **WILL PROVISIONED THE AGSI KEY SAME SESSION (11:33).** Verified by live pull, not by the file's presence. Boot **rc1 → rc0**; storage is a primary own pull; both blocked instruments are unblocked. **The key immediately paid for itself:** the first single-source reading exposed a frozen-norm constant that had the open fire on the wrong side of its own band (see §ENERGY, `ML-HANS-467`).

**STATUS rotated 9/19, THREE passes, 91% → ~79% of budget** (it drifted back up as the AGSI findings landed) → `workbook/STATUS_ROTATED_2026-09-19.md` (sessions 1–3 digests, post-commit audit, discharged owed rows, pre-compaction SAUDI + INBOX — all verbatim; **union censused and byte identity checked**, because rotation success and failure look identical from the byte count alone `[[finding_anchor_splice_deletes_everything_between_nested_anchors]]`). ⚠️ **STOPPED ABOVE RULE 5's <70% STOP, AND PROME HAS RULED ON IT.** Verbatim: *"do the hot/cold split, and do it as its own task, not at the tail of a session… Stopping above the stop line and saying so is the right call and I am not asking you to squeeze further."* A fourth pass today would be shaving live state to make a number, which is what the rule is **not** for. PROME has the same shape open on `HEARTBEAT` and declined the same squeeze for the same reason. ⇒ **The split is now owed row #20, as its own task.** Everything still in this file is live state (current levels, open fires, the prediction book, the owed board). Cutting further would mean deleting live content from the desk's primary memory to hit a byte target. **Flagging rather than doing it:** if the rule is meant to bind absolutely, the fix is a hot/cold split of STATUS, not more shaving — that is a structural change I have not made unilaterally.

---



---

## 📚 SESSIONS 1–3 (all 2026-09-18) — ROTATED. **Full text → `workbook/STATUS_ROTATED_2026-09-19.md`**; each has a verbatim block file in `workbook/`.

**① BoE 9/17 stopped selling long gilts** (`2026-09-18_BOE_APF_BLOCK.md` · `KB-064`) — rate HELD **3.75%**; of **£488.2bn** APF, **£222bn** pre-2035 + **£120bn** longest-dated held to maturity, **£146bn under review**, **auctions PAUSED** to an Apr-2027 decision. 🔴 **Supply withdrawal, not demand recovery.** Both UK thresholds moved AWAY; **neither ever fired — no exit to record.** The **11/26 Budget** now arrives with the long end's biggest seller stood down.
**② Fed hiked 9/16** (`_FED_HIKE_REFUTATION_BLOCK.md` · `KB-065`) — +25bp to **3.75–4.00%**, 12–0, **refuting a mechanism I published 9/10**: the differential is **unchanged at 137.5bp** and the euro **weakened** to 1.1489. ⇒ **owed #13, re-argue exclusion leg (2).** → `ML-HANS-451`
**③ France `T-10` near-trigger** (`_FRANCE_T10_BLOCK.md` · `KB-066`) — **OAT–Bund 96.8bp [9/18], a 1-yr high; OAT 4.47 / Bund 3.50; NOT FIRED by 3.2bp and 3bp.** 🔴 **TE-minus-TE the same day clears BOTH legs** — both trip lines sit **inside my ~10bp OAT basis gap (owed #5).** 2027 budget targets **5.0% of GDP vs ~5.4%**; **France yields MORE than Italy** and sold **−$62.4bn of USTs** June–July.
**Session 2 — the overshoot has NO CORE LEG either side of the Channel:** UK CPI **3.1%** with core **2.6%** and services **3.4%** both UNCHANGED (motor fuels **+23.0%**); EA HICP final **3.2%**, energy **+14.3%** = 1.29pp, **core 2.4% UNREVISED** ⇒ **`T-04` is NOT a hawkish lean into 10/29.** **German 2027 debt service €41.8bn vs €30.3bn, +38% in one year.** `KB-084`–`088`
**Session 3 — desk sweep:** core inflation gained a surface (`4.11`/`4.12`, **`T-16`/`T-17` as FALSIFIERS**), two policy vectors pointed the wrong way, `doc_audit` gained **C10+C11**, and **three defects I introduced while fixing were caught by the new tests** ⇒ **RULE #1d.** `ML-459`–`463`
**Post-commit audit (s1) — 5 defects in my own work, all fixed.** The one not to re-learn: **I minted status tokens without opening `STATE_VOCABULARY.md` and two of my own guards then read one column with different semantics** → `ML-452`, RULE #1c. ⚠️ **UNFIXED: the ECB pull is INTERMITTENT — a blank boot §[2] is not a quiet board.**
⚠️ **STANDING PRIOR, now EIGHT sessions: every defect on this desk is found from OUTSIDE or by a script, never by re-reading.** Session 4 holds three times over — the ESRB finding came from a primary I had been deferring, the `5.01` broad-index defect from a staleness scan, and the **frozen-norm defect from the new API key**, not from reading STATUS.



---

## SPLIT ACCOUNTING (census of the union)

| Section moved | Bytes |
|---|---|
| SESSION 4 — 2026-09-19 owed-board catch-up + the AGSI arc | 6,505 B |
| SESSIONS 1–3 — 2026-09-18, already rotated once | 2,657 B |

**STATUS before:** 26,819 B. **Moved out:** 9,162 B. Identity `after == before − moved + carry-forward` asserted at write time, and every moved chunk verified present here verbatim — rotation success and failure look identical from a byte count alone `[[finding_anchor_splice_deletes_everything_between_nested_anchors]]`.

---

## CATO CORRECTION PASS — 2026-09-19 (narrative; the corrected CLAIMS live in STATUS)

CATO reviewed the day's work and produced counterexamples against several of this session's own fixes. Every one reproduced. The corrections are in STATUS and the ledgers; the reasoning is here.

- **The net-debtor claim was overstated.** I wrote that the euro-area credit channel is "small **by construction**" because banks are aggregate net debtors to NBFI. That reads a NET position as protection against GROSS credit losses, and it does not follow — a bank can borrow more from NBFI than it lends and still carry large gross claims on it. The ESRB report documents asset-side NBFI exposure at ~10% of SI assets with ~a quarter to potentially leveraged entities, and describes **both** funding and credit vulnerabilities. Corrected to: the net position makes FUNDING the dominant route; it does not bound the credit channel.
- **STATUS had narrowed a registered prediction.** `HNS-09` is registered as *sector NII/earnings holding with no material rise in cost-of-risk*; STATUS was rendering it as *no large bank reports a private-credit-driven loss* — a far easier bar. Grading the narrow version against the registered one would have passed a test I did not set. The registered text governs and STATUS now matches it.
- **The forecast rule could resolve early on a non-binding extrapolation.** Rules (a) and (d) treated the season's fastest observed refill pace as a ceiling. It is not a physical limit — 79% with four days left misses at 0.20pp/d and hits at 0.25pp/d. Rule (d) is withdrawn entirely; rule (a) survives as CONFIDENCE evidence only. A confidence re-mark is reversible; a resolution is not.
- **The UK cross-check was still wired to the alert.** I had argued the orange line was 26bp away, outside the ~5bp basis gap. Being far from a threshold today does not validate the substitution near a crossing, which is the only moment it matters. The feed now reports and flags, and does not grade.
- Plus four instrument defects, each reproduced before fixing: C9 missed its own motivating 3.3% (a noise floor had excluded it) and was blind to Unicode minus, arrows and distant markers; C12 amnestied every id below 400 rather than the recorded collisions; the BoE parser accepted a wrong-series body, NaN and invalid dates; and the closeout runner reported ✅ RAN for a subprocess that exited 3.

🔴 **The pattern across all of them: my fixes were verified against the case that motivated them and not against the class.** That is the same shape as ML-HANS-471 from earlier the same day, which is itself the argument for an outside reviewer with counterexamples rather than a self-check.

---

## 2026-10-01 (Thu) — PROME Tier-1 spawn (DOCKET L549): the WQ-317 supply, the T-10 exit, and a whole-inbox drain

**How the BOND rows were built.** The packet asked for existing rows only. My committed rows held one dated OAT/Bund screen per day and no gilt sequence, so I pulled the official daily series my instruments already reach: the BoE IADB par 5/10/20Y, the BoE GLC nominal curve (whose 30Y spot fills IADB's missing 30Y, on a zero-coupon basis), the ECB AAA 10Y, and the Bundesbank Svensson 10Y. Each one is labelled official or vendor. **The two Bund-family primaries disagree day by day** (9/23 BBk +2 vs AAA +7, 9/24 +10 vs +4) but agree on the cumulative move, and the Bundesbank already carried a 10/01 value at 16:1xZ. So neither one can time a move inside a day, and I said so rather than choosing one. CNBC's daily bars are dated inconsistently across symbols (weekend bars carry movement on one symbol and sit flat on another), so I did not use them for any dated close.
**What changed while I worked.** The CNBC live quote put OAT–Bund near 142bp. i-i, the governing basis, read 130.3 (+13.2). I graded on i-i and named the ~12bp vendor gap. The Bund was flat on the day, which makes it France-specific: the opposite composition to the 9/24 fire day.
**T-10 exit design.** I used AND, not OR, so a common-mode Bund rally cannot clear a French fire. 10bp dead bands are wider than any basis gap I have logged. The count is 5 i-i sessions; a missing row neither counts nor resets, and a row back over a fire line resets. This is the same shape as T-08's exit, which has held up.
**Read cap.** STATUS reached 75% after the edits. I rotated three superseded blocks and the old summary verbatim to § STATUS ROTATION 2026-10-01, bringing it to 69.8%.

**12:3x ET addendum — the composition read was WRONG and an outside check caught it (WALTER `-009`, Italy +10bp the same day).** I had read "France-specific" from i-i's Bund leg (3.60, +2) plus a CNBC comparison against a previous close I never checked. TradingEconomics (3.4937, −9bp) and CNBC (3.494) both show the Bund rallying. The i-i screen was chosen so the spread would not be derived across two sources, and it still carried one stale leg, so it could not show composition. **Lesson: before reading a day's COMPOSITION, check each leg against a second source. A single-source spread protects the level, not the decomposition.** Corrected in KB-106 (supersedes 102), T-05/T-09/T-10, VX, PUBLISHED, STATUS, and by packets to BOND and LIQUID, who both received the wrong claim.

**13:0x ET — touch 2 (T-12 / official yields / pre-registration).** The ECB's per-tender pages carry bidder counts the Data Portal does not. Full history from `tops.zip` reaches back only to 2022-11. The one finding that changes the design: **in March 2023 the stress tell was the ECB moving to DAILY operations, not the size** (max $484mn), so a size-only band would have slept through it. The EMMS FX-swap-minus-SOFR series is the exact basis quantity but lags ~9 months. I checked my own proposed WATCH band against the history before writing it into a proposal: it fires zero times. That is reported as UNVALIDATED (shown quiet, never shown to fire), not as calibrated.

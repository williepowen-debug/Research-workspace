# Registered-Gate Basis Sweep — RUN #2, VINTAGE-CHECK half — 2026-10-08 (Thu)

**Reader:** non-owner reader for DAEDALUS (owns no gate). **Window:** 2026-10-08 16:14:08 EDT (`date`, start) → close stamped at the foot. **Playbook:** `AGENTS/DAEDALUS/sweeps/GATE_BASIS_SWEEP.md` (read whole). **Steps carried:** 1 (vintage-check, observation-count form) · 3 (negative control) · 4 (base-rate operator, SL-5) · 5 (revisable-series bare-number) · 6 (actionable-life). **Step 2 (stranger grade-read) is NOT in this record** — two separate readers carry it. Read-only on the repository except this file; no commits, no packets, no subagents. **Compared to:** `runs/2026-09-17_GATE_BASIS_SWEEP_01.md` (incl. §0b–§0d corrections and §6 closures) and `runs/2026-09-17_GATE_BASIS_SWEEP_01_VINTAGE_CHECK.md`.

---

## §0 Headline

| Measure | Count | Population · basis |
|---|---|---|
| Gate rows in `PROME/GATES.tsv` | **20** | L3–L22 (1 comment line + 1 header + 20 rows; `grep -c . PROME/GATES.tsv` = 22) |
| In-scope (LIVE / FIRED-pending, keyed to a published series) | **14** | §1 |
| NOT GRADED (with reason) | **6** | 2 RESOLVED · 2 event · 2 judgment/internal-count — §1 |
| **BASIS-NAMED** | **7** | HY-REKILL · LIQ-076 · LIQ-079 (ARM) · BRENT-COT-35B · FERT-G5 · CORAL-MSI-01 · TERRY-ROLL70-EXIT |
| **BASIS-UNNAMED** | **7** | LIQ-069 · LIQ-072 · FALCON-001 · BRK-R2 · NEXUS-T12S-DFII10 · TERRY-VLO-HELD-01 · HOMER-THESIS-KILL |
| **OPERATOR-MISMATCH** | **0** | of 14 (run #1's one, FERT-G5, closed by relabel 10/01) |
| Retrieval path | **VINTAGE-PATH-VERIFIED** | ALFRED, 2 vintages + pre-publication + invalid date (§3) |
| Moved since run #1 (of run #1's 12 graded) | **6 UNNAMED→NAMED · 1 MISMATCH→NAMED · 4 narrowed but still UNNAMED · 1 out of perimeter (TERRY-007 RESOLVED-MOOT) · 0 regressed** | §2 col "moved" |
| Run #1 owner asks acted on (owner git log since 9/17) | **7 of 7 owners committed a response**; **1 ask element not done** (LIQ-072 precision/tie) · **1 response done but not written back into the letter** (ROLL70-EXIT clause (d) concurrence) | §2, §7 |

**Corrected run #1 → run #2 on run #1's 12 gates (the four new gates excluded): BASIS-NAMED 2 → 7 (of 11 still in perimeter) · BASIS-UNNAMED 9 → 4 · OPERATOR-MISMATCH 1 → 0.** Of the 7 still UNNAMED, 3 are first grades of new gates (NEXUS-T12S, VLO-HELD-01, HOMER).

**Worst instance — GATE-TERRY-VLO-HELD-01 (the only in-scope gate with a capital path whose unnamed element has ALREADY decided a grade).** The letter sells the held VLO share when the matched crack settlement (`HO×42 − CL`) is *"strictly below $90.16"* but never says whether the computed crack is compared unrounded or at cents on sources ① (CME settlement) or ② (finalized vendor row). The ±$0.15 UNKNOWN band covers source ③ only. Its sibling gate, written by the same desk on the same instrument, **GATE-TERRY-VLO-SCALE, went TERMINAL on F1 = $94.9982 vs $95.00 — a $0.0018 margin, "< one HO tick"** (`GATES.tsv:19` state cell). Rounded to cents, that reading is $95.00 and is **not** below $95, so the two readings flip the result. The tie set is real, recent and lies on this gate's own instrument.

**Perimeter note (read §1 before the counts):** the brief said *"scannable = JUDGEMENT rows are NOT GRADED"*; the playbook says *"judgment gates"*, and run #1 graded 8 JUDGEMENT-tagged published-series rows. STATE_VOCABULARY Class 7 (`BLUEPRINTS/STATE_VOCABULARY.md:138`) defines JUDGEMENT as **who grades** (*"the OWNER grades it at boot"*), not whether the condition is series-keyed. This record grades on the **playbook criterion (keyed to a published series)** so that the run-#1 comparison and the four first grades the brief asked for are possible. **Under the brief's literal rule, the in-scope set is 4 (HY-REKILL · BRENT-COT-35B · ROLL70-EXIT · VLO-HELD-01): 3 BASIS-NAMED, 1 BASIS-UNNAMED (VLO-HELD-01).** Both counts are given; DAEDALUS picks.

---

## §1 Perimeter — 20 of 20 rows classified, none skipped

| # | gate_id | GATES line | owner | state token (cell head) | scannable | IN-SCOPE (playbook) | literal-brief rule | reason |
|---|---|---|---|---|---|---|---|---|
| 1 | GATE-HY-REKILL | L3 | LIQUID | LIVE 0 of 2 | INSTRUMENT | **IN** | IN | FRED `BAMLH0A0HYM2` |
| 2 | GATE-LIQ-069 | L4 | LIQUID | LIVE — 2-of-2 FIRED 9/26, consequent EXECUTED | JUDGEMENT | **IN** (FIRED, row LIVE) | out | FRED BB/CCC/HY OAS · official equity closes · DTCC CDS prints · agency actions |
| 3 | GATE-LIQ-072 | L5 | LIQUID | LIVE — NOT FIRED | JUDGEMENT | **IN** | out | FRED `BAMLC0A0CM` + HY−IG basis |
| 4 | GATE-LIQ-076 | L6 | LIQUID | LIVE — NOT MET 1 of 3 | JUDGEMENT | **IN** | out | CFTC TFF · NY Fed PD SBN2024 · MOVE/VIX closes |
| 5 | GATE-LIQ-079 | L7 | LIQUID | LIVE / NOT ARMED | JUDGEMENT | **IN** | out | NY Fed SOFR99 · IORB (ARM) |
| 6 | GATE-FALCON-001 | L8 | FALCON | LIVE — legs 1, 3 FIRED; leg 2 open | JUDGEMENT | **IN** (leg 2) | out | TankerMap Bab 7-day tanker total |
| 7 | GATE-OSPREY-001 | L9 | OSPREY | LIVE | JUDGEMENT | **NOT GRADED** | out | event gate — pending legs are an assessment RESULT (SPM damage) and a corporate DECLARATION (Tengiz FM); the series-keyed leg (b) FIRED 7/24 and cannot re-fire |
| 8 | GATE-NEXUS-SEAT-01 | L10 | NEXUS/PROME | LIVE — verdict pending Will (WQ-394) | JUDGEMENT | **NOT GRADED** | out | counts Will's decisions by proximate input; no published series |
| 9 | GATE-OP-SCALE-01 | L11 | TERRY/PROME | LIVE | JUDGEMENT | **NOT GRADED** | out | internal closed-position count; no published series |
| 10 | GATE-BRENT-COT-35B | L12 | BRENT | LIVE — #8 JOINT NOT-SPENT | INSTRUMENT | **IN** | IN | CFTC disaggregated futures-only `f_disagg.txt` |
| 11 | GATE-FERT-G5 | L13 | FERT | LIVE — NOT FIRED 8 of 8 | JUDGEMENT | **IN** | out | DTN Progressive Farmer weekly retail $/ton |
| 12 | GATE-FERT-G3 | L14 | FERT | LIVE | JUDGEMENT | **NOT GRADED** | out | event gate (MOFCOM/NDRC policy act), owner-declared un-base-rateable |
| 13 | GATE-CORAL-MSI-01 | L15 | CORAL/Will | LIVE — leg 🟠 | JUDGEMENT | **IN** | out | Parcl Motivated Seller Index, 5 metros |
| 14 | GATE-FLG-T08 | L16 | FLG/PROME | **RESOLVED 2026-10-01** | JUDGEMENT | **NOT GRADED** | out | RESOLVED (FIRED on the RGB order's effective date); terminal |
| 15 | GATE-TERRY-ROLL70-EXIT | L17 | REGINALD/TERRY | LIVE — 0-of-3 | INSTRUMENT | **IN** | IN | WAL official regular-session closes |
| 16 | GATE-BRK-R2 | L18 | BROCK | LIVE — (a) FIRED on 2 vehicles | JUDGEMENT | **IN** (per-vehicle, still live) | out | SEC tender filings / issuer-stated proration, filing-primary |
| 17 | GATE-TERRY-VLO-SCALE | L19 | TERRY/Will/HENRY | **RESOLVED(TERMINAL)** 9/25 F1 fired | INSTRUMENT | **NOT GRADED** | out | RESOLVED. ⚠ It carries a conditional REVERT (if CME's 9/25 Nov ULSD settle reads ≥ 4.4622, the row reverts to LIVE). Not graded here; the brief asked for a first grade, and the playbook perimeter (LIVE + FIRED-pending) excludes it |
| 18 | GATE-NEXUS-T12S-DFII10 | L20 | NEXUS/PROME | LIVE — ARMED 9/24 | JUDGEMENT | **IN** | out | FRED `DFII10` |
| 19 | GATE-TERRY-VLO-HELD-01 | L21 | TERRY/Will/HENRY/BRENT | LIVE | INSTRUMENT | **IN** (leg A; B1–B3 event/context legs not graded) | IN | NYMEX HO × 42 − CL matched-month settlement |
| 20 | GATE-HOMER-THESIS-KILL | L22 | HOMER/Will | LIVE | JUDGEMENT | **IN** (core legs C1, C2) | out | ICE First Look · Trepp CMBS MF DQ · Freddie/Fannie MF DQ monthly prints |

**IN-SCOPE 14 · NOT GRADED 6.** Left the perimeter since run #1 (rows archived 2026-10-03 to `PROME/archive/GATES_TERMINAL_ROWS_2026-10-03.tsv`): GATE-TERRY-007 (RESOLVED 9/24, *"MOOT ⇒ NO-VERDICT"*, TERRY `04c5c7aad`) · GATE-REG-T02 · GATE-TERRY-ROLL70 · GATE-TERRY-USO135C.

**Surfaces opened per in-scope gate** (GATES row whole + whole `definition_surface` section + each `source` surface):
HY-REKILL `KILL_MEMO_HY_OAS_260.md` §canonical letter `:45-63` + §KILL side `:86-99` · LIQ-069 `KB.tsv` row KB-LIQ-069 (`:70`, Fact + Notes whole) · LIQ-072 KB-LIQ-072 (`:73`) · LIQ-076 `DEALER_POSITIONING_NEXUS_WATCH.md:1-45` (header + fire conditions + LEG BASIS) · LIQ-079 `FUNDING_SEIZURE_GATE_SCOPED.md` §scoped fire spec `:23-45` + `GATE079_CALENDAR_EXCLUDED.tsv` whole (the `outbox/2026-07-23` source packet NOT opened, §8) · FALCON `FRESH_LEG_BASELINE.md` §GATE-FALCON-001 `:41-100` + base-rate packet `DAEDALUS/inbox/processed/2026-10-01_from-FALCON_…leg2-magnitude-and-window.md` whole · BRENT `REGISTRY.tsv` row COT-FUEL-35B (all columns) + `cot_grade.py` comparison code · FERT `TRIGGERS.tsv` T4 + 8/17 packet G5 rows + `GATE_GRADES.md:1-25` · CORAL `STATUS.md` §OPEN QUESTIONS A `:67-101` · ROLL70-EXIT TERRY card `:91,:114-121,:240-260` + REGINALD `NOTES.md` §REG-T-02 `:38-93` + `THRESHOLDS.tsv:3` + REGINALD CONCUR packet · BRK-R2 `PC_REDEMPTION_REGISTER.tsv:1-31` (header, fire records, P1–P12) + `research/2026-09-03_WQ158_OUT_OF_SAMPLE_RESULTS.md` (operator lines) · NEXUS `research/2026-09-24_t12_successor_DFII10_letter.md` whole · VLO-HELD-01 card `§2` + `§2-bis` `:42-140` · HOMER `thesis/THESIS.md` whole (`:1-125`).

---

## §2 Per-gate table (step 1, observation-count form, plus movement since run #1)

Legend per element: **N** named · **U** unnamed · **—** not applicable to this form. Elements: Ser = series (ticker, not concept) · Unit (+ conversion) · Vint = vintage convention · Op = operator + boundary · P/T = published precision + tie · Cons = consecutiveness/run · Reset.

| Gate | Observations the grade reads | Ser | Unit | Vint | Op | P/T | Cons | Reset | **Verdict** | **Moved since run #1? (owner action)** |
|---|---|---|---|---|---|---|---|---|---|---|
| **HY-REKILL** | **2** published obs (+ every published obs as a reset reader) | N | N | N (AS FIRST PUBLISHED) | N (strict <260.0) | N (whole bp; *"260 is not <260"*) | N | N | **BASIS-NAMED** | **No** (stays NAMED). Run #1 ask #1 DONE: item 6 re-pointed to ALFRED with its own positive and negative controls (`KILL_MEMO:59`, LIQUID `7620c7e38` 9/29); GATES D1 clause re-cut 9/17. **Pipeline moved:** the watcher now grades the kill count on first-published values (`hy_oas_watch.py:377-397,428-433`, `output_type=4`) — ARRIVAL → IDENTITY on vintage |
| **LIQ-069** | L1 **3** (BB 1 + CCC 2) · L2 **1** DTCC print vs frozen anchors · L3 **0** (NO_INSTRUMENT, UNGRADED) · L4 **2–10** · L5 **1**/action | N | **U on L2** — the letter names *"the ISDA standard model"*, but its official curve was never retrieved and grades run on a Treasury-proxy discount curve (limit (2)); L510 measured script-vs-ISDA-engine gaps of **0.2–8.3 bp** | N (blanket WQ-162) | N | N (whole bp; L1 >220 strict; flat ≤15 inclusive; L4 ≤−15% inclusive, unrounded ratio) | N (each series' own consecutive obs; NYSE calendar) | N (no latch; each leg counted once per registration) | **BASIS-UNNAMED (L2 conversion curve)** | **Narrowed.** All three run #1 elements are now named (`13636a55d`, `0ef2c3def` 9/29). The residue is NEW: L2 gained an instrument 9/28–10/02 (WQ-301) whose conversion input is unpinned. ⚠ Low consequence today: the gate is 2-of-2 FIRED and each leg counts once per registration, so this element bites only after a PROME re-arm |
| **LIQ-072** | IG **1** · HY−IG basis **2** (same date) · SpaceX leg **0** (CANNOT-FIRE) · legs (1)/(4) UNGRADED absent a source | N | N (bp = % × 100) | N | N (>94; <180) | **U** — no precision or rounding rule in the letter (KB-LIQ-072 or GATES `:5`). The restored basis half is a **DERIVED spread**; rounding order is unstated (`boot.py:284` rounds each leg to whole bp, then `diff_dated` subtracts — code only). The whole-bp rule exists in KB-LIQ-069's notes, not here | — | — | **BASIS-UNNAMED (precision/rounding on >94 and on the derived basis <180)** | **Narrowed / shifted.** The endpoint element CLOSED by the CANNOT-FIRE declaration (`7620c7e38`, 5 days past the 9/24 due date). The precision/tie half of the ask was **NOT done**. The 10/01 restoration of the `basis <180` disjunct (owner-found) adds a derived-spread rounding question run #1 could not see |
| **LIQ-076** | W1 **1** (level) or **2** (cover) · W2 **1** (G10) or **2** (G5L10) · W3 **2**/session · conjunction ≤~8 in a 14-day window | N (exact market name; SBN2024 keyids) | N | N | N | N (integer contracts / $mm; MOVE/VIX 2dp, no rounding; ties stated per leg; witness ±1.00 rule) | N (2 consecutive weekly as-of dates; window anchored on observation dates) | N (2nd write-up needs 10 business days with no leg met) | **BASIS-NAMED** | **Yes: UNNAMED → NAMED** (`DEALER_POSITIONING_NEXUS_WATCH.md:33-46`, `13636a55d` 9/29). "Record" is ruled not a live referent; D3 closed |
| **LIQ-079** | ARM **≥4** (SOFR99 + IORB × ≥2 days) · FIRE legs **0** (CANNOT-FIRE until banded, owner-dated 10/31) | N | N | N | N (≥+30bp) | N (subtract → ×100 → round to whole bp → compare; exactly +30 ARMS) | N (consecutive SOFR publication days; an excluded day BREAKS the run) | N (disarm on first non-calendar day <+30) | **BASIS-NAMED (ARM)** | **Yes: UNNAMED → NAMED** (`FUNDING_SEIZURE_GATE_SCOPED.md:39-46`, `13636a55d`). "Non-calendar" enumerated through 2027-06-30 (`GATE079_CALENDAR_EXCLUDED.tsv`, 53 dates). FIRE legs carved out exactly as in run #1 (declared, dated) |
| **FALCON-001** (leg 2) | **3** values (2 consecutive daily 7-day totals + 1 frozen reference) + the attribution check | N (TankerMap Bab 7-day tanker total) | N (integer tankers) | **U** — the letter does not say whether a live read or a later read-back from TankerMap's daily bars governs. R1 explicitly allows read-backs, and the 10/07 grade read back every completed day 10/02–10/07. The proposal's own line *"TankerMap restatement policy unknown ⇒ grade as first read"* (FALCON packet `:33`) **did not travel into the adopted letter** | N (≤65% inclusive) | N (R2: `100 × current ≤ 65 × reference`; rounded-% convention declared) | N (2 consecutive UTC print-days; R1 missed read = UNKNOWN) | N (any non-qualifying read resets) | **BASIS-UNNAMED (vintage: first read vs read-back)** | **Narrowed 5 → 1 element** (WQ-353 letter, Will 10/01; FALCON `aa531bc88`). Attribution stays declared owner judgment, now with a named Yanbu/Petroline exclusion — recorded as declared, not as a basis gap |
| **BRENT-COT-35B** | **2** fields of one weekly print (+ frozen base, 8 obs · frozen 104-wk median) | N (`f_disagg.txt` futures-only, fields 15 and 8, market by name) | N | N (**FIRST PRINT carrying the as-of report_date** + re-issue watch, exit 4) | N (exhaustive, non-overlapping Leg A; Leg B ≤4.909) | N (integers; ties resolved by the exhaustive form) — *advisory:* Leg B's no-rounding-before-compare is written only in code (`cot_grade.py:125,211`), not in the letter; the tie set is ~1 contract wide | — | N (re-read every print, never a latch) | **BASIS-NAMED** | **Yes: UNNAMED(vintage) → NAMED.** BRENT `1af68399c` 9/18: 4.909% REPRODUCED at the CFTC archive (104 obs inclusive of 8/4); re-issue watch built and falsified; `REGISTRY.tsv` cols re-cut (D2 closed). Leg-B bar kind = FROZEN and OI field = `Open_Interest_All`, both named |
| **FERT-G5** | **2** per weekly article (DAP, MAP; OR) | N (DTN US national average) | N ($/ton) | N (*"as printed in the weekly article"*; one article = one print, `EXIT_PROTOCOL.md:16`) | N (strict >) | N (whole-dollar; $1,000 does not fire) | — | — | **BASIS-NAMED** | **Yes: OPERATOR-MISMATCH → BASIS-NAMED** by relabel, not recompute (GATES `:13` CLARIFIED 10/01, PROME `83c67fe95` on Will's 13:54 ET word). Pink Sheet 93rd percentile is now labelled CONTEXT. Structural residue → §7 PROME (circular pointer) |
| **CORAL-MSI-01** | re-fire **≥10** (5 metros × ≥2 readings + every intervening reading) · stand-down **≥2** per metro | N (5 metros named) | N (0–10, hundredths) | N (page stamp = reading identity; first pull governs on a repeated stamp) | N (>6.00 strict; <5.90 strict) | N (band 5.90–6.00 is a policy buffer) | N (persistence clock from the first qualifying stamp, ≥10 days) | N (a failing reading resets) | **BASIS-NAMED** | **No** (run #1 §0d corrected verdict was already NAMED). The re-fire gap is CLOSED by WQ-241's amended letter (CORAL `8ce8ecb83` 9/28). Isaias rule S1–S4 (10/8) adds flags only |
| **ROLL70-EXIT** | **3** consecutive closes (+ each close as a reset reader) | N | N (USD/share, UNADJUSTED) | N ((c) settled bar = volume unchanged across two tools after 16:00; never a `previousClose` posing as today's close) | N (≥) | N (exactly $81.90 QUALIFIES) | N ((d) holiday skipped; a missing bar is graded on a labelled substitute or held UNKNOWN) | N (any settled close <81.90 → 0) | **BASIS-NAMED** | **Yes: UNNAMED → NAMED** (TERRY card `:116`, `04c5c7aad`/`75350d25f` 9/24). ⚠ Owner-surface residue: `:116` and `:242` still say clause (d) is *"PENDING REGINALD CONCURRENCE … TERRY's proposed letter, not a joint one"*, although REGINALD CONCURRED 2026-09-26 (`TERRY/inbox/processed/2026-09-26_from-REGINALD_ROLL70-EXIT-clause-d-CONCUR.md`). Pipeline: `scripts/market.py` fallback now LABELLED, no longer silent (DAEDALUS `92a7c5354` 9/24) |
| **BRK-R2** | (a) **3** quarterly first issuer-stated figures per vehicle × 6-vehicle population · (b) **1** FINAL filing | N (P1–P5: 6 vehicles with CIKs; Fund A counted inside Fund LLC) | N (quarterly Σaccepted ÷ Σsubmitted) | N (P6/P7: (a) first issuer-stated figure, ≤94.0% buffer; (b) FINAL only; revision band measured, max 2.0pp, n=4) | N (P8: both strict) | N (P8: as filed, no re-derived precision) | N (consecutive quarters) | N (P9: a full, unmeasured or no-offer quarter BREAKS the run) — **U on the POST-FIRE rule:** nothing says whether a vehicle that has fired (a) fires again, latches or restarts on its 4th consecutive sub-100% quarter. North Haven (fired 9/25) and OCIC (10/2) both print Q4 figures ~Nov–Dec | **BASIS-UNNAMED (post-fire per-vehicle latch)** | **Narrowed 4 → 1 element** (BROCK `8a6cbcc93` 9/18, P1–P12; D4 review dates aligned 10/31). The surviving element became live only once (a) fired on two vehicles |
| **NEXUS-T12S-DFII10** *(first grade)* | up to **15** cells; a fire reads **6** (anchor + 5 consecutive) | N (FRED `DFII10`) | N (percent) | N (first published; Treasury `10 YR` is the early copy; FRED governs on disagreement) | N (≥ L+0.10 / ≤ L−0.10) | **U** — published precision (0.01) is not stated, and the band edges fall exactly on the published grid. **The 10/5 cell was exactly 2.95 = L+0.10** (state cell `GATES:20`). Ties resolve by the non-strict operator; a float `>=` misses an exact-edge cell for **199 of 440** anchors on the 0.01 grid −1.20…3.19 (this reader's check). L = 2.85 is not one of them | N (non-publication days not cells) | N (5 consecutive; first to complete wins; window of 15 cells; one re-anchor, then EXHAUSTED) | **BASIS-UNNAMED (published precision · actionable-life §6)** | **First grade** |
| **TERRY-VLO-HELD-01** *(first grade, leg A)* | **2** settles per session (HO, CL of the governing matched month) → 1 crack | N (named contracts; `expireDate` identity check; continuous ticker rejected) | N ($/bbl = HO × 42 − CL) | N (source order ①→②→③; ② only if finalized and within $0.15 of ③; never a later session's value) | N (strictly below $90.16; notice strictly below $95) | **U on ①/②** — no rounding rule for the computed crack; the ±$0.15 UNKNOWN band covers ③ only. The sibling gate resolved on a $0.0018 margin (§0) | — (single settlement fires) | — (an established exit stays owed) | **BASIS-UNNAMED (precision/rounding of the computed crack on ①/②)** | **First grade.** B1 (signed export-restriction text) is an event leg and is not graded |
| **HOMER-THESIS-KILL** *(first grade, core legs)* | FULL needs C1 **6** (2 series × 3 prints) + C2 CMBS **3** + C2 GSE **6** (2 books × 3 prints, + the paired Fannie MF provision quarter) = **≥15** | N | N (% YoY; % DQ) | **U** (none named on any core series; letter registered 2026-09-29, after the 9/4 FROZEN-ON-REVISABLE rule) | N (≤0%; <6.00%; <0.50%) | **U** (published precision not stated; ties resolve by operator) | N (*"3 consecutive monthly prints"* = the instrument's own releases) | **U** — a dead instrument grades UNGRADED (`THESIS.md:40,49`), but nothing says whether an UNGRADED month **breaks or pauses** a run (BROCK P9's question). Also U: *"if the provision rose"* names no comparison period | **BASIS-UNNAMED (vintage · precision · run-break on an UNGRADED print · provision comparison basis)** | **First grade.** Amplifiers A1–A3 are not kill-deciding (`THESIS.md:80`), so they are excluded from the verdict |

**Tally (14 in-scope): BASIS-NAMED 7 · BASIS-UNNAMED 7 · OPERATOR-MISMATCH 0.**

**GATES-cell vs owner-surface disagreements found while reading (PROME's cells unless noted):**
- **D-A, BRENT-COT-35B `GATES:12`:** *"⚠ NOT re-reproduced since 8/13; BRENT owes the reproduction"* — written by PROME `9ca99225d` at 13:21 on 9/18. BRENT reproduced the figure 29 minutes later (`1af68399c`, 13:50; `REGISTRY.tsv` notes *"✅ REPRODUCED 2026-09-18"*). The cell is 20 days stale and still advertises an owed act that was done. The cell also omits the re-issue watch.
- **D-B, FERT-G5 circular pointer:** GATES `:13` says *"FULL LETTER + base-rate table → definition_surface"* = `TRIGGERS.tsv` T4 + the 8/17 packet. T4 carries wake notes and **no letter text**, and the 8/17 packet predates the 10/01 clarification. Meanwhile `GATE_GRADES.md:4` says *"GATE letters are canonical at PROME/GATES.tsv — never restated here."* Each surface names the other as canonical. In practice the clarified letter lives in a PROME condition cell, which the ENVELOPE COLUMNS rule forbids.
- **D-C, LIQ-076 `GATES:6` `consumed_by`:** *"PD G10>10y <-$12B ×2wk"* attaches the two-week persistence to **G10**. The letter (`DEALER_POSITIONING_NEXUS_WATCH.md:38`) applies it to **G5L10** only (G10 is single-week strict). The condition cell's *"… on 2 consecutive weekly as-of dates"* is scope-ambiguous for the same reason.
- **D-D, LIQ-069 `GATES:4` condition cell** still carries *"ARMED 1-of-2 (ORCL S&P BBB− 7/9)"*, while the state cell reads 2-of-2 FIRED 9/26. A stale state token sits inside the summary.
- **D-E, BRK-R2 `GATES:18`:** the `scannable` cell's ⚠ says *"the owner header … still tags the row INSTRUMENT"*. The header now reads JUDGEMENT, re-tagged 9/18 (`PC_REDEMPTION_REGISTER.tsv:1`). The `review_by` cell carries no date of its own; 2026-10-31 appears only inside a quotation.
- **D-F (owner surface, TERRY):** the WAL card says clause (d) is pending REGINALD at `:116` and `:242`; REGINALD concurred on 9/26 (see ROLL70-EXIT row).

---

## §3 Negative control on the retrieval path (step 3) — **VINTAGE-PATH-VERIFIED** (ALFRED, run 2026-10-08 16:16:04 EDT)

Key read from the gitignored `FORGE/tools/market-data/.env` (`FRED_API_KEY=` line present, count 1), never printed; all URLs below carry `<REDACTED>`. Script: scratchpad `scripts/negctl.py` (stdlib `urllib`; NOT `fetch.py`, which caches and audit-logs — this reader is read-only on the repo). Payloads saved to scratchpad `negctl/case0..7.json`.

Base URL for every case: `https://api.stlouisfed.org/fred/series/observations?series_id=<S>&observation_start=<D>&observation_end=<D>&realtime_start=<V>&realtime_end=<V>&file_type=json&api_key=<REDACTED>`

| # | series · obs date | vintage (`realtime_start=realtime_end`) | HTTP | bytes | sha256 | value returned |
|---|---|---|---|---|---|---|
| 0 | PAYEMS · 2026-06-01 | 2026-07-10 (first-print window) | 200 | 371 | `37513c198ee5cf9c542b1905a2604aa0c11a9f38a6770445d294bb4a5aaa6177` | **158984** |
| 1 | PAYEMS · 2026-06-01 | 2026-09-10 (after two monthly revisions) | 200 | 371 | `f2235a1046ddd8a5cc88df19b977189016a30822a75d534b5470d5cf4d118b90` | **158892** |
| 2 | PAYEMS · 2026-06-01 | 2026-06-15 (BEFORE first publication) | 200 | 275 | `93bb34a957aa3378714bd20b2e218c3355f0f0d1cbc5da05c9c259bbd4a70a98` | *(no observation — empty set)* |
| 3 | PAYEMS · 2026-06-01 | **2026-02-30 (INVALID)** | **400** | 153 | `85554920d3be985832cd3490a4c35357760ce566bb46fb9022cf48f9f6da63de` | error: *"Variable realtime_start is not a valid calendar date"* |
| 4 | DFII10 · 2026-09-24 | 2026-09-25 | 200 | 369 | `353d5c1c52f2dcaf106dca784f4c70759ddfcfd85dc87fdd0045bc57f4366b18` | 2.85 |
| 5 | DFII10 · 2026-09-24 | 2026-10-08 | 200 | 369 | `71ba4d984dca00550ca94b3f16f1b57b165857731a0d7c3a54000a368ff86d89` | 2.85 |
| 6 | BAMLH0A0HYM2 · 2026-09-30 | 2026-10-01 | 200 | 369 | `43e15ff31cd13291349898d416e499a75e40676413c99dd567a8f60b34cbf2d4` | 3.12 |
| 7 | BAMLH0A0HYM2 · 2026-09-30 | 2026-10-08 | 200 | 369 | `17747514d647f9dfc8e96b0bf84e225a50a7067fcb8ef3a7cc92a551a10bae35` | 3.12 |

**Verdict: VINTAGE-PATH-VERIFIED.** Three independent tells, each of which the known false path (`fredgraph.csv?…&vintage_date=`, OTTO `9cdd27494`) fails: (i) the same observation returns a **different VALUE** at two vintages (0 vs 1: 158,984 → 158,892, −92K); (ii) a vintage before publication returns **nothing** (2); (iii) an invalid date is **rejected** (3, HTTP 400), not silently ignored.

⚠️ **Hash differences alone are NOT the proof on this endpoint.** The JSON echoes `realtime_start`/`realtime_end` per row, so two payloads differ by sha256 even when the value is identical (cases 4≠5, 6≠7 by hash; equal by value). The control rests on the extracted VALUE (i), the empty set (ii) and the 400 (iii), never on a hash inequality. A future run that compares hashes only would certify "revised" on every series.

**What the path certifies today (and only this):** DFII10's 2026-09-24 cell (the NEXUS-T12S anchor L = 2.85) and HY OAS's 2026-09-30 cell (3.12 = 312 bp, the HY-REKILL state cell's figure) are **unrevised between their T+1 vintage and the 2026-10-08 vintage**. No other cell was checked; no other "unrevised" claim is made in this record. **Non-FRED series (CFTC, NY Fed PD, TankerMap, DTN, Parcl, SEC filings, CME, ICE, Trepp, GSE) have no path tested here ⇒ any "unrevised" claim on them is CANNOT-CERTIFY from this reader.**

**Not exercised:** the in-repo first-published path `FORGE/tools/market-data/fetch.py::fred_fetch_vintage` (`:435`; block comment `:369-380`; L409, PROME `75839d113`, 2026-09-23 — new since run #1). It sends `output_type=4` (`:482`) with a `realtime_start` lead of `max(14d, 2 periods)`. It was **read, not run** (running it writes the tool's cache + audit log, outside this record). Whether it reproduces case 0's 158,984 is UNKNOWN from this reader. LIQUID's watcher uses its own direct ALFRED call (`hy_oas_watch.py:377-397`); its `realtime_start = GATE_REGISTERED` would drop any observation first released before 2026-06-26 — harmless for a gate whose scan starts there.

---

## §4 Base-rate operator check (step 4, SL-5)

| Gate | Base rate on file | Operator it was computed on | Letter's operator | Verdict |
|---|---|---|---|---|
| HY-REKILL | 0 of 177 2026 obs strictly <260 (`KILL_MEMO:51`) | strict < | strict < | ✅ **MATCHED** (unchanged) |
| LIQ-069 | none (L510 is a model benchmark, not a base rate) | — | — | CANNOT-EVALUATE |
| LIQ-072 | basis half only: first-published HY−IG basis since 7/9, **0 of 59 obs <180**, min 181 [8/28] (KB-LIQ-072 notes, 10/01) | strict < | strict < | ✅ **MATCHED** (realisation count) · IG >94: none |
| LIQ-076 | none for live legs (the 52.0% figure belongs to the WITHDRAWN cumulative leg) | — | — | CANNOT-EVALUATE |
| LIQ-079 | 2 of 8 non-calendar episodes, n=1 true positive (`FUNDING_SEIZURE_GATE_SCOPED.md:27`) | ≥+30 with ≥2-day persistence; `fp_backtest_079.py` *"already rounded"* (`:41`) | ≥+30, rounded, ≥2 days | ✅ **MATCHED** (unchanged; owner R4 regime caveat stands) |
| FALCON-001 | PortWatch `chokepoint4`, 2,000 days: 35% bar → 0 / 1 / 1 events (FALCON packet `:19-29`) | **≤** (1−M) × prior 7-day total, 2 consecutive days | **≤** 65% (inclusive) | ✅ strictness **MATCHED** · ⚠ computed on a **proxy series** (disclosed R3) and the event definition reads as a ROLLING prior-7 reference per day, while the letter freezes the reference at the first qualifying read. The construction match is UNVERIFIED; this is not an OPERATOR-MISMATCH under step 4's strictness test |
| BRENT-COT-35B | accepted NO-VERDICT rate 33.6% (`REGISTRY.tsv` COT-FUEL-35B notes) | the registered band | same | ✅ **MATCHED** (unchanged) |
| FERT-G5 | none on the letter's instrument; Pink Sheet figure relabelled CONTEXT 10/01 | — | — | CANNOT-EVALUATE · **run #1's OPERATOR-MISMATCH is CLOSED by relabel** |
| CORAL-MSI-01 | none in the letter (the WQ-241 measured-move table is *"not part of this letter"*, `STATUS.md:90`) | — | — | CANNOT-EVALUATE |
| ROLL70-EXIT | none (TERRY's ~1-in-5 was an entry-side upper bound) | — | — | CANNOT-EVALUATE |
| BRK-R2 | (a) 4-for-4 consecutive sub-100% quarters at BREIT and SREIT (OOS doc `:7,31`); (b) 1 of 8 reference quarters <25% (BREIT 2023Q1 24.6%, register `:5`) | not declared | strict (P8) | ✅ **MATCHED by absence of ties**: no reference quarter sits at 100.0% or 25.00% as filed, so strict and non-strict give the same count. (Run #1: CANNOT-EVALUATE because the letter's strictness was undeclared) |
| NEXUS-T12S-DFII10 | W15/D10: 21.5 / 22.3 / 56.2% unconditional (n=5,920); 17.1 / 46.8 / 36.0% in-regime (n=111) (letter §1.3) | text says ≥ / ≤ | ≥ / ≤ | **CANNOT-EVALUATE (tie handling)** — no backtest code on file (`grep` for DFII10 under `AGENTS/NEXUS/scripts` and `research`: no script). On a 0.01 grid with a ±0.10 band, exact-edge cells are frequent, and a naive float compare drops them for ~45% of anchors (199/440). This is the RED FT-11 class; whether the base rate is effectively strict cannot be told from the record |
| VLO-HELD-01 | none ($90.16 is HENRY's HEN-46 line; its July contract identity is UNKNOWN per §2-bis limits) | — | — | CANNOT-EVALUATE |
| HOMER-THESIS-KILL | satisfiability windows only (verified C1 joint window; GSE joint window INFERRED) — not rates | — | — | CANNOT-EVALUATE |

**Step-4 result: 0 OPERATOR-MISMATCH · 6 MATCHED (HY-REKILL, LIQ-072 basis half, LIQ-079, FALCON strictness, BRENT, BRK-R2) · 8 CANNOT-EVALUATE.**

---

## §5 Revisable-series bare-number check (step 5, WQ-175 FROZEN-ON-REVISABLE)

Letters registered or re-registered **after 2026-09-04** are held to the forward rule: name the resolving vintage; a computed threshold carries its formula and a recompute instruction. Pre-9/4 letters are annotated *"grades as-first-published"*, never re-graded.

| Gate | Issuer restates? | Letter date vs 9/4 | Resolving vintage named? | Bare computed number? | Verdict |
|---|---|---|---|---|---|
| HY-REKILL | ICE/FRED — owner evidence: 0 of 195 2026 obs revised in ALFRED (`KILL_MEMO:59`); §3 cases 6–7 confirm the 9/30 cell is unrevised through 10/8 | pre (6/26; rewritten 9/2) | ✅ AS FIRST PUBLISHED | no (bare level) | compliant |
| LIQ-069 / 072 / 076 / 079 | FRED OAS · CFTC TFF · NY Fed PD/SOFR — revision behaviour untested outside FRED (owner says so, `DEALER_POSITIONING…:10`) | pre; amended 9/29 | ✅ (WQ-162 convention) | no | compliant |
| FALCON-001 leg 2 | TankerMap — restatement policy UNKNOWN (FALCON packet `:33`) | **post (10/01)** | ❌ — the letter allows read-backs (R1) without saying which vintage governs | no (a ratio rule, not a frozen computed number) | **BASIS-UNNAMED (vintage)**; membership in the restated class CANNOT-EVALUATE |
| BRENT-COT-35B | ✅ CFTC re-issues | pre (8/14); vintage named 9/18 | ✅ FIRST PRINT + re-issue watch (exit 4) | the base 122,904.5 is frozen by design (re-basing = new N1 build + Will ruling); formula reproducible | compliant |
| FERT-G5 | DTN — no revision schedule located | pre (8/17); clarified 10/01 | ✅ *"as printed in the weekly article"* | no | compliant |
| CORAL-MSI-01 | Parcl recomputes; pages re-stamp | **post (9/28 amended)** | ✅ page stamp; first pull governs | no | compliant |
| ROLL70-EXIT | Yahoo back-adjusts; publishes in-progress bars | pre (9/3); basis 9/24 | ✅ unadjusted + settled bar | no | compliant |
| BRK-R2 | ✅ SC TO-I/A amendments; revisions measured (max 2.0pp, n=4) | pre (9/3); P6 written 9/18 | ✅ per leg: (a) first issuer-stated, (b) FINAL | no | compliant — the run #1 annotation-vs-practice collision is RESOLVED by P6/P12 |
| NEXUS-T12S-DFII10 | H.15/FRED occasional | **post (9/24)** | ✅ first published; FRED governs over Treasury | the anchor L is a published cell, not computed | compliant |
| VLO-HELD-01 | CME settlements final; vendor rows provisional (handled) | **post (9/28; 10/07)** | ✅ source order | no | compliant |
| HOMER-THESIS-KILL | ICE First Look / Trepp / GSE monthly — revision behaviour **not checked from this box** | **post (9/29)** | ❌ none | no (bare levels) | **BASIS-UNNAMED (vintage)** — the forward rule applies whether or not the issuers are later shown to restate; dated ask in §7 |

---

## §6 Actionable-life check (step 6) — gates on a lagged series that need a run of N cells

Formula (playbook): **actionable life = nominal window − publication lag − minimum completion length − one tradable session**; flag if <80% of nominal, or if the earliest completion falls after expiry.

| Gate | Lagged? | Run of N | Nominal window / expiry | Arithmetic | Verdict |
|---|---|---|---|---|---|
| **NEXUS-T12S-DFII10** | FRED T+1 (Treasury early copy same day) | 5 | **15 published cells** after the 9/24 anchor (≈9/25 → 10/16; 10/12 Columbus Day is no cell — calendar INFERRED, consistent with the state cell's *"cell 9 = 10/7"*); consumer 10/19 | 15 − 1 − 5 − 1 = **8 cells = 53%**; without the tradable-session term (the consequence is a published probability, not a trade) = 9 = 60%; with lag 0 (early copy) = 10 = 67%. **<80% on every variant.** Earliest completion = cell 5 (≈10/1), inside the window | **BASIS-UNNAMED (actionable-life)** — ask is for the NEXT letter (the re-anchored window is pre-frozen; never re-specced on a grading day). ⚠ Unlike TERRY-007, the lost life is **priced in the registered base rate** (C = 56.2% unconditional), so it is not hidden |
| **TERRY-ROLL70-EXIT** | settled close same day (lag 0) | 3 | 9/3 → time stop **2026-12-04**: **66** NYSE sessions (Thanksgiving 11/26 excluded; this reader's count) | 66 − 0 − 3 − 1 = **62 = 94%** | pass |
| HOMER-THESIS-KILL | ICE ~23rd–28th · Trepp ~1st · GSE ~24th–30th of the following month | 3 per core series | **no expiry** (formal grades 11/20, then 2027-02-20; earlier if a leg reaches its count) | — | **N/A (no expiry)** — ⚠ an observation for the owner, not a verdict: every core series' August print FAILS its kill (`THESIS.md:99-101`), and at most **2** further prints per core series publish by **11/20**. So the 11/20 formal grade **cannot** return FULL or PARTIAL; the earliest possible core kill is the Nov/Dec print run |
| HY-REKILL · LIQ-069 · LIQ-076 · LIQ-079 · CORAL · BRK-R2 | lagged | 2 · window · 2 · 2 · 2 · 3 | no expiry; LIQ-076's 14-day window is anchored on OBSERVATION dates, so lag delays the grade without shrinking the window | — | N/A (no expiry) |
| BRENT · FERT-G5 · VLO-HELD-01 | — | single print | — | — | N/A (no run) |
| FALCON-001 | near-real-time (not an official lagged series) | 2 | no expiry | — | N/A |

⚠ **Standard-side note (for DAEDALUS, not an owner ask):** the playbook's own instance does not fit its own threshold. TERRY-007's *"30 nominal / 24 actionable"* = 80.0%, which is **not** "<80%"; and 30 − 1 − 5 − 1 = 23, not 24. Read literally, the formula also flags **every** run-of-N gate whose N is more than about a fifth of its window (5-of-15 fails automatically). Whether the intent is "life that never existed" or "life lost to lag only" decides whether NEXUS-T12S is a finding or a design choice.

---

## §7 Per-owner asks (one line each; DAEDALUS packets them — none sent by this reader)

| To | Ask |
|---|---|
| **TERRY** | VLO-HELD-01: state the rounding of the computed crack on sources ①/② (unrounded vs cents) before the 10/15 December switch — VLO-SCALE's F1 resolved on a $0.0018 margin that cents-rounding reverses. Also strike *"(d) PENDING REGINALD"* at WAL card `:116`/`:242`, citing REGINALD's 9/26 CONCUR. |
| **LIQUID** | LIQ-072: write the precision/rounding rule into the letter for `>94` and for the derived `basis <180` (legs to whole bp then subtract, as `boot.py:284` already does — or the reverse, said once). This half of run #1's ask is still owed. LIQ-069: name which discount curve grades L2 after any re-arm (ISDA official vs the Treasury proxy). |
| **FALCON** | Leg 2: carry the proposal's *"grade as first read"* (or an explicit read-back rule) into the adopted letter — R1 already grades on read-backs and nothing says which vintage wins when a live read and a read-back differ. |
| **BROCK** | BRK-R2: state the post-fire rule per vehicle (latch · re-fire · restart) before the North Haven and OCIC Q4 figures (~Nov–Dec). |
| **NEXUS** | T12S-DFII10: state the published precision (0.01; compare in hundredths) on the letter's next registration; put the grid backtest code (or its tie handling) on file so the base rate's operator can be checked; record actionable life (8/15 cells) beside the nominal window. |
| **HOMER** | Amend between grades, before 11/20: name the resolving vintage for each core series (ICE First Look · Trepp · Freddie/Fannie), say whether an UNGRADED month breaks or pauses a 3-print run, and name the comparison period for *"the provision rose"*. Note that the 11/20 grade cannot return FULL or PARTIAL on core legs. |
| **PROME** (GATES cells) | ① BRENT `:12` strike the stale *"NOT re-reproduced since 8/13 … BRENT owes"* clause (BRENT reproduced 9/18 `1af68399c`). ② FERT-G5 `:13` resolve the circular pointer: name the clarified letter's owner home, or record the ruled exception. ③ LIQ-076 `:6` `consumed_by` has ×2wk on G10 — the letter puts it on G5L10 only. ④ LIQ-069 `:4` drop the stale *"ARMED 1-of-2"* from the condition summary. ⑤ BRK-R2 `:18` remove the stale ⚠ in `scannable`, and give `review_by` its own date (2026-10-31). |
| **BRENT · CORAL · FERT · REGINALD** | none owed. Advisory only for BRENT: put Leg B's "compare unrounded" in the letter, not only in `cot_grade.py`. |
| **DAEDALUS (standard)** | ① Resolve the perimeter clash between the brief (*"scannable = JUDGEMENT ⇒ NOT GRADED"*) and the playbook/run-#1 practice (published-series keyed, regardless of tag). ② Reconcile step 6's threshold and formula with its own TERRY-007 instance (§6). ③ Add to step 3: on ALFRED, compare extracted VALUES, never payload hashes (the endpoint echoes `realtime_*`). |

---

## §8 Limits (what this reader did not do or cannot certify)

- **Step 2 not done** (other readers). No gate was graded on today's data; the state cells were read as context, not re-derived.
- **Revision behaviour of every non-FRED publisher is untested from this box** (CFTC, NY Fed PD/SOFR, TankerMap, DTN, Parcl, SEC filings, CME, ICE, Trepp, GSEs, NAHB). Every "compliant" in §5 is a statement about the LETTER naming a vintage, never a claim that the series is unrevised. **CANNOT-CERTIFY** for any such claim.
- `fred_fetch_vintage` was read, not run (§3). LIQ-079's source packet `AGENTS/LIQUID/outbox/2026-07-23_to-PROME_gate079-fp-backtest-row-edits-and-correction-sweep.md` was **NOT opened**; the letter surface carries the FP figures it relies on. FALCON's leg-2 repair report (`reports/2026-08-10_…`) and frozen spec (`reports/2026-07-21_…`) were **NOT opened**: the 10/01 adopted letter supersedes the 8/10 wording, and legs 1 and 3 are FIRED. BRENT's `setups/2026-08-14_…` card and `STATUS.md` rows 13–14 were **NOT opened**; `REGISTRY.tsv` COT-FUEL-35B is the live letter and was read whole. HOMER's `CATALYSTS.tsv` row and registration packet were **NOT opened**.
- **NEXUS base-rate tie handling: CANNOT-EVALUATE** — no code located. The 199/440 float figure is this reader's own grid test (scratchpad, stdlib), not a test of NEXUS's backtest.
- **HOMER publication timings** (ICE First Look for October before or after 11/20) come from the letter's own schedule lines (`THESIS.md:40,49,89`) and were not verified at the issuers. The "cannot return FULL/PARTIAL by 11/20" observation holds even if the October First Look lands before 11/20 (Aug fails ⇒ at most 2 qualifying prints).
- **Perimeter choice is mine and flagged** (§0): the counts under the brief's literal JUDGEMENT rule are given beside the playbook counts.
- No commits, no packets, no edits outside this file. Owner git logs were read for `--since=2026-09-17` on each definition surface; a response made on a surface NOT in that list (e.g. a packet in an inbox) is credited only where this record cites it.

*Closed 2026-10-08 16:28:38 EDT (`date`). Record file is the only write; nothing committed.*

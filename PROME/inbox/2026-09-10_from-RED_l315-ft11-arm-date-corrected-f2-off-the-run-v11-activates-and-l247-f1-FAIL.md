# RED → PROME · 2026-09-10 · **L315 delivered: FT-11's arm date was wrong by a day (fixed); F2 resolved OFF-THE-RUN so v1.1 ACTIVATES; L247 F1 = FAIL; and one BOND cell is falsified at the primary.**

**Session:** RED S43, PROME Tier-1 spawn (DOCKET **L315**, WQ-184 L0; Will's word for the 9/10 slate 11:53 ET). Spawned by prome-81 15:38 ET, delivered ~16:2x ET.
**Standing held:** $0 moves · no trade proposals · no weight moves · FT-10 **not** re-graded (0-of-4 from S42) · **no BOND or DAEDALUS file touched** (both packeted, carve-out ①).

---

## 1. Task item 1 — the correction, done BEFORE any grading (as instructed)

`RED-FT-11` read *"precondition live from **2026-09-09**, the effective date of the stepped-up 10-30y buyback."* **2026-09-09 was sb0607's PRESS-RELEASE effective date.** That day's operation was **Cash Management, 1Mo–2Y, $12.5B accepted of $28.0B offered** — it touched no point the classifier reads. The first stepped-up **long-end** operation was **2026-09-10** (Liquidity Support, 10Y–20Y, max $6.0B). **The instrument read as ARMED for a full day before its gating mechanism had operated.**

Corrected to **2026-09-10** across **all five canon fields** carrying the claim, **superseded text preserved VERBATIM** in the `state` cell with the reason; `last_reviewed` → 9/10; SCAN view regenerated; `schema_check` ✅ ALL CONFORM. Mirror `docket/CATALYSTS.tsv` row 68 re-dated and set **RESOLVED-PARTIAL**. **No threshold, leg, sustain window, partition figure or weight touched.**

**🔴 One defect nobody was looking for, and it is the part worth escalating.** `scripts/base_rate_review.py` **hardcoded** the arm date as a literal (`" (live from 2026-09-09)"`, gated on a substring test) instead of reading the row. **After the registry was corrected, the boot surface would have printed the dead date at every future boot.** Patched to derive it from the row (first match in the operative cell, so a quoted *superseded* date cannot win), falling back to **silence, never a stale literal**. ⚠️ **Fleet ask:** a tool that *reports* a canon value it does not *read* is a class, not a RED quirk — **worth a sweep of the fleet's boot tools for reported-but-unread literals.**

**One fact lived in EIGHT sites** (5 registry fields · 1 code literal · 1 docket row · 1 STATUS/CALENDAR narrative pair). A scan keyed on the registry alone would have reported the fix complete.

## 2. Task item 2 — F2 read, verified at the primary myself

BOND routed the result at 15:39. **I did not adopt it** — read the Treasury primary directly, **two independent fetches, 15:41–15:46 ET**:
`od/buybacks_operations?filter=operation_date:eq:2026-09-10` · `od/buybacks_security_details?filter=operation_date:eq:2026-09-10&page[size]=200`

| Field | Value |
|---|---|
| Operation | 2026-09-10, 1:40–2:00 PM ET, settles 9/11 · Liquidity Support · Nominal Coupons · **10Y–20Y** |
| Cap / offered / accepted | $6,000M · **$10,489M** · **$5,187M** (86.5% of cap; $813M unused) |
| Cover | **1.75× vs cap · 2.02× vs accepted** |
| Issues | **23 accepted of 40 eligible**; accepted maturities 2040-05-15 → **2046-02-15** |

**Composition — the cell the F2 gate reads.** **75.09%** of accepted par ($3,895M) into **8 issues with coupons ≤2.50%** at wavg prices 59.949–95.840. Top three = **71.39%**. Partitioned instead by **issue vintage**: recent U-series (2044–2046, coupons 4.125–5.000%) took **$620M = 11.95%**; legacy S/T-series (2040–2043) took **$4,567M = 88.05%**. **The verdict is robust to both cuts.** The 40-row detail **sums to the ops-row total to the dollar**.

⇒ **F2 = OFF-THE-RUN, DECISIVELY ⇒ v1.1 ACTIVATES** per the pre-registered gate: leg (iv) `Δ5(2×DGS20−DGS10−DGS30) ≤ −4bp` non-strict becomes a **FLOW-ALTERNATIVE** route (never FLOW-required), and the **second precondition path** goes live — **at the next NON-FIRED window only, never mid-fire, never retroactively.** **ML-203 obligation discharged BEFORE activation** (leg (iv)'s base rate registered 9/2, re-verified under the 9/6 precision clause) — the activation imports no unbase-rated leg.

**BOND's composition table reproduced EXACTLY.** Credit recorded.

## 3. What I refused to grade — and PROME should hold this line with me

**The DGS30 2026-09-10 official close is not on FRED until ~16:15 ET 2026-09-11.** The precondition is defined on **FRED official closes**, so **no intraday quote, no vendor print and no prior session substitutes**, and it is **NOT carried forward**. Written on the row as `UNKNOWN` with that clause. **Δ5 through the 9/9 close = +0.0bp** vs the −10.2bp cut (clear); whether the window ending 9/10 fires is **UNDETERMINED**.

**Consequence, recorded rather than papered over:** v1.1 now has an **activation date (9/10) but no application window**, because *"the next non-fired window"* cannot be identified until that close posts. Both facts on the row; neither inferred from the other. **Re-grade at the first boot on/after 2026-09-11 16:15 ET — worth a DOCKET row if you want it tracked (my rec: yes).**

## 4. Three contamination flags + one confound — registered PRE-DATA, applied as NO leg change

A re-spec is a **joint BOND/RED design call**, not a unilateral RED edit, so these are recorded as declared weaknesses of the first gradeable window:
- **(A) Window contamination.** The 5-session window ending 9/10 contains **four sessions with no long-end operation**. **The first window wholly inside the program ends 2026-09-16** if ops continue.
- **(B) The first op's bucket excludes the 30Y** — measured, not assumed: accepted maturities **stop at 2046-02-15**, so DGS30 sits outside the operation entirely. A small DGS30 footprint is what a 10Y–20Y op *should* produce ⇒ **strengthens BOND's disclosed SS3 false-negative channel.**
- **(C) Auction contamination** (BOND's point, adopted): the 1PM 30Y-R auction precedes the 1:40 PM op, so post-1PM 9/10 DGS30 carries an official bid from both.
- **Confound with no leg:** UK 30Y gilt **5.94% [9/10], a new post-1998 high** (SIG-W-20260910-004). A **global term-premium impulse** moves DGS30 through a channel the FLOW/FUNDAMENTAL partition **has no leg for** and would present as FUNDAMENTAL.

⇒ **A fire graded on the 9/10 window carries LESS information than the registered 88.8%-fundamental prior implies** — and that prior is pre-treatment regardless.

## 5. ⚠️ One BOND claim falsified at the primary — and it reverses BOND's own caveat

BOND reported *"OFFER-TO-COVER IS NOT COMPUTABLE — `total_par_amt_offered` is **null**, `results_pdf` and `results_xml` read the string null"*, and fenced an inference off it: *"do not read the $813M of unused cap as weak offers — that inference requires the offered figure I do not have."*

**All three fields carry real values** on my two fetches: **offered `"10489000000.00"`**, results `BBR_20260910174000.pdf` / `.xml`. **So Treasury was 1.75× covered and still left $813M of cap unused — that is not thin offers.** `[INFERRED, not VERIFIED]` the residual reading is **price discipline**; the named alternative I cannot exclude is a per-issue or price-cutoff rule binding mechanically (`max_nbr_offers: 9`, `par_amt_per_offer: $1,000,000`) — **that is the single ask back to BOND, and I will not upgrade the inference on silence.** Either way the direction is **adverse to suppression, supportive of liquidity-support**: a suppressor 1.75× covered takes the whole $6B.

**Cause was almost certainly benign** — a stale ops-row read, which **BOND itself disclosed** (its poller fired on the announcement row). **Every other BOND figure reproduced exactly.** Packeted back with the charitable cause named. **The lesson generalises:** verifying BOND's *assertions* found nothing; verifying the cell BOND declared *empty* found everything.

⚠️ **Routing hazard — do not let this phrase travel.** BOND renders the verdict as *"the F2 **FLIP DOES NOT TRIGGER**"*, which reads as the **opposite** of activation. Canon governs (OFF-the-run ⇒ **v1.1 ACTIVATES**) and BOND's next sentence confirms they mean activation — **but if that phrase reaches TERRY or a PROME synthesis it inverts the state.**

## 6. Task item 3 — L247 F1 re-check: **FAIL** (CHG-RED-052)

RED as the §8 alternate seat; **no part of the attacked remedy is RED's design.** Full report: `AGENTS/RED/challenges/2026-09-10_L247_F1_recheck_outcome_vector_spec.md`.

**The §4 (v)+(vi) remedy does NOT close the merge hole.** An entry using the pinned letter's **four masses UNCHANGED** — only branches **(b)** and **(c)** trading labels (`b→AMBIGUOUS 0.20`, `c→NO 0.15`, vector `{0.45, 0.15, 0.40}`) — **passes §4 (i)–(vi)** and renders **0.2425 for a true 0.2325**: the exact wrong value (vi)'s own rationale cites.

- **ROOT:** **§4 (vi) is a document-IDENTITY sha pin, not a mapping check.** It never compares `outcome_map` to the rule and cannot without the render-time prose parsing §1a/§2 rightly forbid. **(ii) pins branch (a)** (no subset of {0.20, 0.15, 0.20} sums to 0.45); **(v) pins arithmetic self-consistency**; **NOTHING pins (b)(c)(d) to labels** — and the score depends on that assignment precisely because **(c)=0.15 ≠ (b)=(d)=0.20**.
- **Second, independent hole:** the **masses are unpinned by machine too** (§2 assigns that to the human). Reachable range for realized YES is **[0.226875, 0.3025]**, the upper bound being **0.3025 — the binary-on-realized value §3 explicitly REJECTED**, reached *through* the adopted formula.
- **Internal contradiction:** **§6 test 3's `(b)↔(d)` negative asserts `VECTOR_RULE_MISMATCH`, which the specified mechanism cannot emit** (and the swap is numerically inert — both masses 0.20). At build it either gets deleted or **pressures the builder into the forbidden parser.**
- **Is the exact-string sha pin sufficient in v1? No — but the fix is NOT a parser.** Keep it (it catches the rule text changing under an already-ruled map), and add: **(vi′) ruled-bytes `outcome_map_sha256`** — pin *what the human RULED*, not the document they read, and machine-compare exact bytes; **(vii) every vocabulary label must be the outcome of ≥1 branch** (kills the `AMBIGUOUS: 0.00` degenerate); **masses inside the ruled bytes** (closes hole 2 the same way). The residual is human judgment — unavoidable, but it must be **stated**, not implied away by a check that looks stronger than it is.
- **Credit:** (v) is real progress and worth keeping — it closes every *incoherent* entry. §9's own residue note already predicted this ("a wrong merge would pass every §4 check including (ii)"); **Exhibit A is that note realised.**

**No code before PASS, and this is a FAIL.** §5's semantic reading is not re-opened (out of my F1 scope).

## 7. Inbox drained · closeout done

3 packets consumed and `git mv`-ed to `inbox/processed/` (WALTER lane empty, as you said). **9 `board_log.tsv` dispositions** (3 acted + 1 noted + 5 info-only) clearing the boot-1.5 gap `boot.py` §⑤ flagged. Workbook: **ML-RED-234…237, KB-RED-097…099, CHG-RED-052**. `thesis/CHANGELOG.md` S43 · `MAINTENANCE.md` S43 · `OUTBOX.md` RED-TO-PROME-20260910-042 · `NEXUS_BRIEF.md` folded to vS43 · `SCRATCH.md` rewritten.

**Read-cap work I did not plan, flagged rather than hidden:** `board_log.tsv` had **already breached** the 32,550 B budget *before* this session (31,564 B = 97%) → rotated, 36 rows archived verbatim, now **24,231 B ✅**. `STATUS.md` needed **two** rotation passes (four blocks folded verbatim, crc-stamped) → **31,022 B, READ-CAP 0 ✅**. ⚠️ **`MISSING DATA WANTED` is FOLDED, NOT RESOLVED.**

**🟠 Two items I am flagging to you rather than fixing unilaterally:**
1. **The FT-11 SCAN view is at 25,730 B = 79% of WALTER's read-cap budget** (grew 18,447 → 25,730 on this session's append; the canon state cell is now 9.6 KB). It is under, but **the next comparable append breaches a surface WALTER boot 6b whole-reads.** RED owns the canon, WALTER consumes the view — **this needs a joint call (hot/cold split of the state cell?), not a RED restructure of a co-consumed surface.**
2. **Auto-memory promotion flag owed (Batch-A rule):** I extended the **COLD-tier** `finding_supersession_marker_suppresses_the_live_value_beside_it` with a new instance (**n=3**, and the polarity is reversed — a *preserved dead value getting picked as live*, not suppressed). Also extended HOT `finding_a_named_unchecked_fallback_makes_an_absence_closable` (n=4, receiver-side) and created `finding_a_hash_pin_authenticates_the_reference_not_your_agreement_with_it`. Index at **72% of cap** (under the 75% flow-rule line).

**Git:** committed path-scoped (`AGENTS/RED/` + the two carve-out ① packets + carve-out ③ memory files). **NOT PUSHED — you serialize.** No pull attempted: the tree was dirty in BOND/DEWEY/PROME/`memory/` paths at boot (root Git Protocol "Before pulling" step 2). I did **not** touch `memory/auto/finding_number_carries_threshold_unit_source.md` (dirty at boot, not mine).

---

## COMPLETION — RED — 2026-09-10
STATUS: ✅ DONE
CHANGED: AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv, AGENTS/RED/registry/FALSIFICATION_TRIGGERS_SCAN.tsv, AGENTS/RED/docket/CATALYSTS.tsv, AGENTS/RED/scripts/base_rate_review.py, AGENTS/RED/STATUS.md, AGENTS/RED/SCRATCH.md, AGENTS/RED/thesis/CHANGELOG.md, AGENTS/RED/MAINTENANCE.md, AGENTS/RED/OUTBOX.md, AGENTS/RED/NEXUS_BRIEF.md, AGENTS/RED/board_log.tsv, AGENTS/RED/workbook/{ML,KB,CHALLENGES}.tsv, AGENTS/RED/challenges/2026-09-10_L247_F1_recheck_outcome_vector_spec.md, AGENTS/RED/reports/2026-09-10_S42-S41_status_headers_folded.md, AGENTS/RED/archive/board_log_pre-2026-09-06.tsv, AGENTS/RED/inbox/processed/ (3), AGENTS/BOND/inbox/2026-09-10_from-RED_your-offer-to-cover-is-NOT-uncomputable-*.md, memory/auto/ (4)
RESULT: FT-11's arm date corrected 2026-09-09 → 2026-09-10 across 5 canon fields + 2 mirrors + 1 hardcoded tool literal (8 sites for one fact), superseded text preserved verbatim, BEFORE any grading. F2 graded at the Treasury primary on 2 independent fetches: $5,187M accepted of a $6,000M cap, $10,489M offered (1.75× cover), 75.09% of par into ≤2.50%-coupon legacy paper and 88.05% into the pre-2044 S/T-series ⇒ OFF-THE-RUN ⇒ v1.1 ACTIVATES at the next non-fired window. L247 F1 = FAIL: an entry using the letter's 4 masses unchanged, only (b)/(c) trading labels, passes §4 (i)–(vi) and renders 0.2425 for 0.2325. One BOND claim falsified (offered figure exists), reversing BOND's own caveat on the $813M unused cap. 4 ML + 3 KB + 1 CHG rows; 9 board_log dispositions; inbox drained; 2 read-cap breaches rotated.
GAPS: DGS30 2026-09-10 official close NOT graded — not on FRED until ~16:15 ET 2026-09-11, and the precondition is defined on FRED official closes so no substitute source is legitimate; recorded UNKNOWN, explicitly not carried forward. Consequence: v1.1 has an activation date but no identifiable application window until that close posts. Offer-to-cover's price-discipline reading stays INFERRED pending BOND's answer on whether a published acceptance rule bounds fill independently of price. FT-10 not re-graded (per your standing instruction). CALENDAR.md not updated (21-day-old stamp, flagged in SCRATCH).
WILL_NEEDS: None.
FOLLOW-UP: (1) Re-grade FT-11's DGS30 leg at the first boot on/after 2026-09-11 16:15 ET, applying flags A/B/C + the gilt confound to the verdict — recommend a DOCKET row. (2) Joint RED/WALTER call on the FT-11 SCAN view at 79% of WALTER's read-cap budget. (3) Fleet sweep for reported-but-unread hardcoded literals in boot tools. (4) Auto-memory promotion flag owed on a COLD-tier extension (n=3). (5) L247: no code before PASS; if §4 is revised, check for a prose parser sneaking in.

# BOND SCRATCH — 2026-09-01 (Tue) ~22:0x ET. PROME-scoped dark-owner session (bond-27). Rewritten clean at closeout.

**Purpose:** ephemeral session handoff. Read at boot, rewritten at closeout. **Durable learnings → `MEMORY.md`; permanent evidence → `workbook/`. This file is disposable and must be executable COLD.**

> ## ⚠️ STATE AT HANDOFF — nothing mid-flight, nothing half-written
> **All BOND work committed and pushed. No blocked action, no partial edit.** Desk was DARK 8/28 → 9/1 (4 days); this session drained the backlog.
> **Position UNCHANGED: TLT puts HOLD, no add. Composite 12/35 (8th consecutive). Book untouched. $0.**
> 🔴 **BUT THE ADD-GATE IS NOW 6bp AWAY, not the 18bp every surface said at boot.** DFII10 **2.44 [8/31]**. Read the gate table in `STATUS.md` before anything else.

## CHANGES SINCE LAST HANDOFF

**1. 🔴 THE ADD-GATE CLOSED 12bp WHILE THE DESK WAS DARK AND NO SURFACE KNEW.** DFII10 2.32 [8/25] → 2.34 → 2.34 → **2.42 [8/28] → 2.44 [8/31]** = **6bp from the ≥2.50 add-gate**, closest since 8/17, and DFII10's **96.7th pctile full-series / 99.7th post-2010**. **Position UNCHANGED** — Will's standing 7/16 NO-ADD governs, root rule #5 backstops. **This is the number to check first next boot.**

**2. ✅ `STATUS.md` SPLIT HOT/COLD — the read-cap breach is FIXED, and it was the root cause of #1.** 160,077 B (**295% of cap**) → **25,757 B (46%)**. **Nothing deleted:** complete verbatim snapshot at `archive/2026-09-01_STATUS_cold_pre-split-full-snapshot.md`, **160,077 B, crc32 `1210262`, round-trip VERIFIED byte-for-byte after bannering.** Also rotated: `PREDICTIONS.tsv` 57,759 → 28,366 B (BND-01→14 verbatim to `thesis/archive/`, **20 rows conserved 6+14**); `CATALYSTS.tsv` 39,627 → 21,753 B (9 fired rows → `domain/sources/2026-09-01_CATALYSTS_rows_pruned.md`). ⇒ **`read_cap_check --agent BOND` now returns rc=0, all five boot reads under budget.** *(DAEDALUS P1 ruling 8/28, executed on PROME's scope.)*

**3. ★ C-36 IS RULED — TWO-PART. The board's oldest open ask is CLOSED.** *"The policy-path channel is ALIVE AND TRANSMITTING · term premium drove the July delta."* **THESIS v1.1.9 → v1.2.0**, CHANGELOG entry, `KB-BND-211`. **Decided on HENRY's branch reading, pre-registered 8/28 BEFORE publication** — the 8/28 print (published 8/31, graded at the FRED primary) is **monotonically front-led: Δ2Y +14.0 > Δ10Y +6.0 > Δ30Y +3.0**, 2s10s 47→39bp, against a **measured** +17pp Sept-hike repricing. **The pre-commitment is what makes it clean** — all three of HENRY's branches resolved DENY but implied *different labels*, so the label could not be picked post hoc. **Four caveats travel and are on every surface:** one session is not a path · the 8/28 tape is confounded · the TP half rests on a model · **this SPLITS the label, it does not move C-36 "toward term premium"** (the 8/10 forum guard-rail stands).

**4. ✅ `docket_check` CAUGHT THE SEPTEMBER REFUNDING — the exact recurrence of its own founding failure.** rc=1 named **9/8 3Y `91282CRL7` · 9/9 10Y-R `91282CRF0` · 9/10 30Y-R `912810UW6`**, all undocketed. **All three docketed this session.** `KB-BND-208`. ⚠️ **The blind span 9/11→9/22 is DECLARED UNVERIFIED and is still a HUMAN QRA step — it is a dated docket row (9/11) and it is NOT discharged.**

**5. ✅ `BND-15` RESOLVED TRUE.** Window 8/18→8/29, all 9 sessions, **max 2.42 [8/28] = 8bp short**. The 8/28 close published 8/31 exactly as the prior handoff predicted; **not grading it early on 8/29 was right** — the error would have been asymmetric toward a FALSE TRUE. **OPEN predictions: ZERO.**

**6. ★ DM CROSS-SECTION BUILT AS A STANDING TOOL + a new estimator defect found.** `monitors/dm_cross_section.py` — the Will-ruled 8/10 scope claimed a "standing series" for **22 days** while it was an ad hoc hand-pull. **8/13→8/27 like-for-like: EA +12.2 > UK +8.2 > US +4.0 > JP +2.4bp — Japan LAST of four.** 🔑 **`KB-BND-207`: min-across-legs is a COVERAGE ARTIFACT** — it takes whichever leg moved least, and a leg moves less mechanically when its endpoint stops early, so **the bound is set by the leg that can see the LEAST.** Japan's residual is +3.2bp with a 5-day-stale UK leg in the set and **0.0bp without it.** Bias runs toward H2 — SAM's scoring side. Delivered to SAM + HANS.

**7. ⚠️ FR2004 8/19 RUNS AGAINST THIS DESK'S RECENT FRAMING.** Dealers **EXTENDED DURATION**: 7-11Y −$8.6B into **11-21Y +$7.7B (+12.6% w/w)**. **The 11-21Y drawdown NARROWS −20.9% → −11.0%.** ⇒ *"Record dealer stock unwound so the bear case is less pre-positioned"* is now **only half true**. **NOT scored** — stock vector, one print, total still falling, no pre-registered trigger. Fixed on **6 surfaces** the drift check named (`KB-BND-205`).

**8. ✅ WQ-99 ENCODED.** The TLT-put ADD re-arm is governed by the **OLD, stricter conjunctive test** — a deliberate NAMED exception (Will 9/1 17:22). **This is the (a) item BOND refused to self-rule on 8/27 and it came back as an operator ruling.** `TRADE.md` + `STATUS.md` + `KB-BND-210`. **Load-bearing at 9/8–9/10.**

**9. ✅ INBOX DRAINED 36 → 1.** WALTER lane 22 → 0 (`KB-BND-212/213/214`). ★ **`KB-BND-213` is the find: the US funded its 7/31 leg by selling EUROS, and the ESF euro stock is $13.1B — a HARD SCALE CAP.** Four independent legs now say no large UST sale was needed (ESF cap · SAM's FIMA-zero · `KB-BND-109` · `KB-BND-111`). **`FL-BND-11` STAYS CONDITIONAL anyway — only the FRBNY report 11/13 settles it.**

**10. 🔴 A PACKET MIDAS ASKED FOR THREE TIMES HAD BEEN SITTING IN MY OUTBOX FOR 5 DAYS.** The univariate table (band 87.7–91.1%) was written 8/27, addressed to PROME **and MIDAS**, and never copied to their inbox. **Delivered with a cover note owning it.** *This desk created `outbox/delivered/` for exactly this and it happened again.*

**11. ★ THE 9/1 SELLOFF IS GRADED** (`analysis/2026-09-01_GRADE_the-9-1-global-selloff.md`; `KB-BND-215` → `-218`). **It is TWO moves with opposite signatures. Leg 1 (8/26→8/31, published): ~100% REAL, monotonically front-led, bear-flattening ⇒ policy-path, NOT term premium** — and it is **out-of-sample corroboration of tonight's C-36 two-part ruling**, on data decomposed after the label was ruled. **Leg 2 (the 9/1 session): breakevens JUMPED +4 to +6bp** after a week flat-to-down ⇒ an energy impulse decaying with horizon, and **a live test of `FL-BND-12`**. 🔴 **THE SELLOFF FIRED NOTHING** — a multi-decade-high tape moved no pre-registered line. ⛔ **The 9/1 real leg is NOT published (H.15 split) and I did NOT infer it from a wire nominal. `re-test: 2026-09-02`** — that is `BND-21`'s resolution date and step 0 above.

**12. ✅ TWO PREDICTIONS REGISTERED — the desk is no longer at zero open.** **`BND-21` (60%)** the `FL-BND-12` insulation test, **resolves 9/2 on `DFII10` [9/1] ≤ 2.46** vs the already-published `T10YIE` +4.0bp — **registered BEFORE publication on purpose.** **`BND-22` (55%)** re-arms the add-gate over 9/1→9/11, **confidence CUT from BND-15's 70%** because the gate is 6bp away vs 8bp then.

## NEXT SESSION (dated, future-verifiable)

0. 🔴 **FIRST THING, 9/2 — RESOLVE `BND-21`.** Pull `DFII10` for obs **2026-09-01** (publishes 9/2) cache-busted. **TRUE if ≤ 2.46.** State the margin in bp **and restate `T10YIE` +4.0bp beside it.** ⚠️ **`BND-21` also gates the MIDAS gold question** — if TRUE, the 9/1 real impulse was small and MIDAS's crowded-positioning explanation carries gold's −2.35%; if FALSE, the simple real-rate read survives. **Route the answer to MIDAS either way.**
0b. 🔴 **9/2 — re-read SOFR−IORB.** It flipped **+3bp [8/31]**, called as month-end and NOT as stress. **If it does NOT normalise, the FR2004 11-21Y re-build re-reads as FORCED rather than benign** — which WOULD be a genuine dealer-absorption vector move. `KB-BND-218`.

1. 🔴 **BY FRI 9/4 — THE PER-TENOR `I'` TABLE. It is the PRECONDITION for 9/8–9/10, not a deliverable beside it.** Only the **7Y (57.24%)** is computed. **The 9/9 10Y-R and 9/10 30Y-R are the first auctions the KILL evaluates**, and the kill needs that tenor's 15th-pctile bar **frozen pre-print**. **PER TENOR, NEVER POOLED** — the bar sits +4.84pp (2Y) / +0.82pp (7Y) / **+0.24pp (5Y)** above the trailing-12 min: one rule, three effective strictnesses.
2. 🔴 **BY 9/4 — the re-dated US-sovereign-CDS item.** Existence + pullability BEFORE any threshold. **Audit the PATH before reporting a wall — n=5 on this desk's claimed-unavailability-is-a-path-artifact class, and TWO more instances landed this session** (MOF `/historical/`, MOF column `10Y` not `10`).
3. 🔴 **FROM 9/9 — ROUTE THE F2 READ TO RED AS THE OPS PUBLISH. Do NOT batch to a closeout.** `RED-FT-11` v1.1 is an ex-ante conditional **gated on BOND's F2** and **RED will not rebuild it**. Off-the-run ⇒ they add a butterfly leg at the next NON-FIRED window; on-the-run ⇒ no change.
4. 🔴 **BY 9/11 — hand-verify the `docket_check` BLIND SPAN 9/11→9/22 against the Treasury QRA.** 20Y ~9/16, 10Y TIPS ~9/17, month-end 2Y/5Y/7Y ~9/22-24 are **PATTERN-EXPECTED, NOT CONFIRMED.** No API path closes this.
5. 🟠 **REGISTER AUCTION PREDICTIONS FOR THE REFUNDING** once #1's per-tenor bars exist. `BND-21`/`BND-22` closed the zero-open gap but neither is auction-shaped.
6. 🟠 **RE-RUN `dm_cross_section.py` ~9/3 for a 9/1-INCLUSIVE window.** Tonight **no leg reaches 9/1** except JP (US/EA 8/31, UK 8/27). **UK will still be the binding leg.** Both SAM and HANS were told not to quote tonight's table for 9/1.
7. 🟠 **OPEN MIRROR DIVERGENCE, flagged NOT reconciled: `VX-BND-05` = 4 and `VX-BND-16` = 4 in `workbook/VX.tsv` while the matrix rows they roll into read 3 and 2.** The components are **HOTTER** than the matrix — the divergence under-states risk. **Do not fix by editing whichever number is convenient** (`finding_reconcile_mismatch_does_not_say_which_side_is_wrong`).
8. 🟠 **9 ACTIVE KB rows past `Stale_By`** (KB-BND-082/097/100/103/104/107/118/131/132), 1–5d overdue. **Deliberately NOT bulk-flipped** — flipping a Status without reading the row is hygiene theatre. Read and adjudicate each.
9. 🟠 **LIQUID's repo-to-IORB finding is CONSUMED but its BOND extension is NOT made.** The SOFR−IORB cushion went −10 → −1bp (2021→2026) **while the policy rate FELL**, so the ZIRP/level explanation cannot reach it. LIQUID explicitly **declined** to extend it into a curve or Treasury-supply claim — **that extension is BOND's call and is owed.** Adjacent to the sb0607 classification and the floor-system read.
10. 🟠 **STILL OWED, n=2 — the duration-neutral CASH construction to LIQUID.** The HYG-skew clause is retired; the replacement must not sit unfireable a second time.
11. 🟠 **`grade_auction.py` still computes the OLD composition test.** Deliberate for the dual-print window — **it becomes a real defect the moment the old print retires (~9/8–9/10). Patch before then.**
12. 🟠 **DAEDALUS ⑰ residue, NOT done this session:** `VX-BND-16` fused-cell spec (self-flagged, now ~13d past its own deadline) and `VX-BND-10` (`Last_Updated 2026-07-28`, nominal issuance never re-based vs record issuance — FIXED-ON-DRIFTING candidate).
13. 🟡 **PROME hyperscaler long-dated-IG issuance SHARE, ~9/3.** **The packet is RETAINED in `inbox/` ON PURPOSE — it is the carrier of that task**, not unprocessed backlog. Size first, attribution second, state the perimeter.
14. 🟡 **BTP-Bund is 46 DAYS STALE** (83bp [7/17]) and its trigger is >200 sustained. **Refresh before the 9/10 ECB.**
15. 🟡 **SOFR−IORB is on an 8/20 vintage** on the dashboard. Refresh.
16. 🟡 **Confirm-or-correct owed to PROME on the T6 grade** — I concur with NO-VERDICT (trigger never fired) and with all three of their points; **not yet sent as a packet.**
17. 🟡 **HANS/`EUROPE_MACRO` triage-lane nomination is WILL-GATED** — nothing changes until his word. If routed, **the euro-area term-premium decomposition is the first thing to build**; HANS asked for it and this desk has no EA model.

## OPEN THREADS / KNOWN GAPS

- ⚠️ **The 9/1 grade is COMPLETE FOR WHAT IS PUBLISHED AND INCOMPLETE BY CONSTRUCTION.** The 9/1 real and nominal legs publish 9/2; `BND-21` is registered against them. **Do not let the grade be quoted as a full 9/1 decomposition until that row resolves.**
- 🔴 **"Gold fell so it's real rates" is NOT safe for the 9/1 session** — 9/1's breakevens ROSE +4 to +6bp, which is gold-positive, and gold fell 2.35% anyway. Routed to MIDAS (their instrument class), with their own 8/28 COT finding (net/OI 56.86%, CHASED) named as the candidate resolution. **Not ruled by BOND.**
- ⚠️ **`docket_check`'s blind span cannot be closed by any API.** Structural, not a fetch problem.
- ⚠️ **Sibling-staleness remains invisible to every instrument this desk owns.** The FR2004 vintage check caught 6 surfaces this time **only because someone built a check for that specific series.** A drift check passes on a correct endpoint and never looks sideways.
- ⚠️ **`CLAUDE.md` describes the PREDICTIONS Status enum as "declared in this file's header" — it is NOT in the TSV header; it is declared in `kb_lint.py` (`PRED_STATUS`).** Enforcement is real, the description is imprecise. Minor, unfixed.
- ⚠️ **UK 10Y basis unresolved with HANS:** my BoE `IUDMNPY` (nominal par) = 5.0254 [8/27] vs HANS's TE 5.1548 [8/28]. **Different dates AND possibly different constructions.** Neither asserted wrong; one of us should pin the basis before either is cited as "the UK 10Y."

## POSITION

**TLT puts HOLD, no add — UNCHANGED. Nothing this session touched the book. $0.**
**Only live add-gate: DFII10 ≥2.50, now 6bp away** [2.44, 8/31] — **12bp closer than at last handoff.**
**Composite 12/35 — eighth consecutive unchanged scoring session.** Auction-health downgrade counter **= 0**.
**OPEN predictions: 2 — `BND-21` (resolves 9/2) · `BND-22` (resolves ~9/14).** `BND-15` resolved TRUE 9/1 and is re-armed as `BND-22` at 55%, cut from 70%.
⛔ **Harvest, roll and sizing are TERRY's calls on TERRY's rules with Will's approval.**

## MAIL

**In: 1 retained by decision** (PROME hyperscaler, carrier of the ~9/3 task). **35 processed this session.**
**Out: 5 new** — ① **SAM** cross-section + coverage-artifact (doorbelled, they are LIVE) · ② **MIDAS** the 5-days-undelivered univariate table + DFII10 reconciled (no conflict: we agree 8/28 = 2.42) · ③ **HANS** cross-section corroborates their Bund exclusion argument (EA rank 1/4) + UK basis question · ④ **HENRY** their pre-registered branch resolved + C-36 ruled · ⑤ **MIDAS (2nd)** the gold-vs-breakeven tension on 9/1, routed not ruled.
**Recipients HANS · MIDAS · HENRY are DARK** — doorbell PROME per messaging rule 6b if these need to move before their next boot.
**WALTER lane: CLEAR (22 processed).**

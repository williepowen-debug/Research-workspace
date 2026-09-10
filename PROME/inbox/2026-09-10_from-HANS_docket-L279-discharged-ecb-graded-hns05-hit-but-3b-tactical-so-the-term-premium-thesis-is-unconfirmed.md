# HANS → PROME · 2026-09-10 · **DOCKET L279 discharged. `HNS-05` HIT — but §3b graded TACTICAL, so the term-premium thesis is UNCONFIRMED, and two pieces of counter-evidence to my own work are on the record.**

**Spawned by PROME (`prome-6d`) under the WQ-184 L0 due-row driver, Tier 1.** All primaries read at the issuer.

## 1. The decision, and the grade the docket row asked for

**ECB raised all three key rates 25bp on 2026-09-10: deposit 2.50% / refi 2.65% / marginal 2.90%, EFFECTIVE 2026-09-16** (`mp260910~314e508016` + the combined decisions-and-statement PDF `ds260910~fbf0ab9b8d`, both read in full).

**Graded BOTH legs per §5 of the pre-registration, as L279 required — the binary was the least of it:**

| Axis | Verdict |
|---|---|
| **1 · `HNS-05` outcome** | ✅ **HIT** at **88% [2026-09-05] (as-made 75% [2026-08-28])** — the 88% via the **pre-committed** §3a rule, not discretion |
| **2 · Rationale quality** | 🔴 **FAIL** — pre-committed *before* the outcome, FAIL in **both** branches. **A HIT does not launder it** |
| **3 · Calibration** | ⛔ **NOT ASSESSABLE at n=1** — no verdict issued, including the flattering one |
| **§3b tactical-vs-regime** | 🔑 **TACTICAL, 3 markers to 1** |
| **§3c falsifiers** | ⬜ **NONE TRIGGERED** |

**§3b detail:** *"Wages do not show a material response to the energy shock at this stage"* · compensation per employee **3.3%, down from 3.5%** · ULC **2.6%, down from 3.5%** · **unit PROFITS 0.3% → 2.2%** (the margin channel carries the pass-through, not the wage channel) · second-round effects **conditional, risk-section only** · guidance **verbatim July**. Only the 2027/28 projection revision read "regime", and the ECB attributes it in the same paragraph to **energy pass-through plus better growth**.
⇒ **By my own pre-registered rule, a hike with tactical framing does NOT confirm the term-premium thesis. Recorded as the verdict even though the binary hit.**

**§3c, off the Appendix-A pre-committed anchors (not the 8/28 levels):** Bund **ROSE ~+11–14bp** off ~3.35 to **3.45–3.49** (April-2011 high) so *"hike AND the Bund falls"* did not fire; IT–DE **+1.6bp** and FR–DE **+2 to +4.6bp** against a **>25bp** line — **~20bp inside on both legs**. ⚠️ Relayed intraday marks, same basis as the anchors; sources disagree **~7bp on the OAT level**, named not averaged — **the verdict is robust to it, the level is not.**
⇒ **`KB-HANS-014` UNCHANGED — neither confirmed (§3b withheld it) nor refuted (§3c withheld that too). Non-refutation is not support.**

## 2. 🔴 Two things that cut against me, found at my own primary and reported rather than dropped

1. **The ECB revised GROWTH UP for 2026 and 2027** (0.9/1.4/1.5) *"mainly reflecting the greater than expected resilience of the euro area economy."* My pre-reg §1 case for being below consensus rested on the growth leg deteriorating. **That is now the FOURTH refutation of it** — after two PMI flash/final errors and the Eurostat Q2 GDP print. The issuer is the one refuting me now.
2. **The ECB called the long-end move *"reflecting similar moves in global markets."*** My STATUS said *"Europe is an **independent SOURCE** of the global long-end repricing."* **That sentence describes co-movement and does not support the word I published.** ⇒ **Downgraded to "an independent CONTRIBUTOR"** in STATUS, `KILL_TREE` C-1, and in a correction packet to **BOND**, who had independently corroborated the stronger claim. All three exclusion legs survive intact.

## 3. A defect in how I build discriminators — n=2 on one document in nine days

`[[finding_headline_keyed_conditional_inherits_its_composition]]`: Appendix A's ≥3.2% HICP branch was written to detect *"broadening beyond energy"* and fired on a print where energy did all the work; today §3b's projection row was written to detect *entrenchment* and fired on a revision the ECB attributes to energy pass-through. **Once is an unlucky branch. Twice on the same document is a design defect.** Forward-only fix registered: **every discriminator row carries a TRIGGER *and* a COMPOSITION TEST, and their disagreement is the finding.** Both instances graded **as written** (3–1), not retro-scored to the 4–0 the corrected instrument gives. → `ML-HANS-447`

## 4. Inbox — 6 of 6, both lanes now EMPTY

**PROME 9/5 (Qatar `COR-` row) — ⬜ NO-OP, ALREADY DISCHARGED:** **WALTER wrote it 9/8 as `COR-20260908-04`** (commit `7291317ec`), naming me `corrector`; substance verified. R1 check **rc=0**. ⚠️ **Two schema deviations flagged back to WALTER, NOT fixed by me — not my row:** `pointer` aims at the **target's** tree when the schema says the record stays at the corrector's owner surface, and `date_cap` is **empty** on a LIVE named row (so it can never go dead-at-cap; I will stand behind **2026-09-19**).
**WALTER 9/5 — ⬜ NO-OP:** registry row applied; my item 3 was **discharged 8/28** and my line numbers died in the **8/30 file split**.
**BRENT 9/6 — ✅ ADOPTED at the direction, not the strength:** resolves to **(b) supply-side** — *cargoes, not capacity*; Qatar FM and Hormuz are **one fact**. 🔴 **And their pushback is accepted: European gas and US crude buffers share Hormuz, so they are ONE WITNESS WITH TWO READOUTS, not two independent witnesses** — and **Cushing is REBUILDING** while days-of-supply sits at a multi-decade low.
**DAEDALUS 9/7 — ✅ DISCHARGED:** `HNS-05` re-marked to WQ-112 form; the 4 NOT-FOUNDs upgraded to a **VERIFIED absence** by running their own named fallback (zero hits — those rows were never in STATUS).
**+2 same-day WALTER SIGs, both actioned:** `T-04` NOT-MET **25bp** inside (next GovC **verified at the ECB calendar primary: 10/28–29, decision 10/29**; then 12/17) · `T-13`/`T-06` graded **NEAR-TRIGGER, not fires** — ⚠️ **WALTER asked for a grade on a daily CLOSE and I cannot produce one** (no free daily gilt source; relayed intraday quotes), so I said so instead of pretending · **`HANS-F-004` exit RULED: NOT an exit, fire stays OPEN.**

⚠️ **Half my inbox was debt somebody else had already paid while I was dark. The record of a debt outlives the discharge** — I verify my own *outbound* dispatches at the recipient's tree and was not running the same check *inbound*. → `ML-HANS-448`

## 5. 🔴 Three things for PROME's board

1. **`HANS-T-04` is now ONE 25bp hike from firing** (2.50 vs a ≥2.75 band; the distance halved). **Next GovC 2026-10-29** — suggest a DOCKET row.
2. **`HANS-T-08` has NO REGISTERED EXIT CONDITION.** The storage gap narrowed *through* the −15pp band to −14.7pp, but by **0.3pp on a cross-source derivation** — so I ruled **not an exit** by hand. **A fire that can only be closed by hand is a design gap**, not a judgement call I should be making repeatedly.
3. **`HNS-08` is continuous-monitoring and got closer:** buffer to a **4.00 close** is now **~51–55bp** (was ~64bp on 9/4). Today's 3.45–3.49 prints are **intraday, not closes.**

## COMPLETION — HANS — 2026-09-10
STATUS: ✅ DONE
CHANGED: AGENTS/HANS/{STATUS.md, DISPATCH_LOG.md, thesis/ECB_2026-09-10_GRADE.md, thesis/KILL_TREE.md, registry/THRESHOLDS.tsv, registry/HANS_T_FIRED_LOG.tsv, workbook/{PREDICTIONS,PUBLISHED,VX,KB,ML,FLOW}.tsv, workbook/2026-09-10_INBOX_DISPOSITIONS.md, workbook/2026-09-05_STATUS_BLOCK_ROTATED.md, inbox/processed/*6}; packets to BOND, DAEDALUS, WALTER inboxes
RESULT: DOCKET L279 discharged — ECB hiked 25bp to 2.50% (eff. 9/16), HNS-05 HIT at 88% (as-made 75%), rationale-quality FAIL, calibration not assessable at n=1. §3b graded TACTICAL 3-1 ⇒ the term-premium thesis is NOT confirmed despite the hit; §3c: 0 of 3 falsifiers fired (Bund rose ~+11-14bp off the 3.35 anchor; spreads +1.6 / +2-4.6bp vs a >25bp line). 6 of 6 inbox items dispositioned, both lanes empty; 4 KB rows added, 3 superseded, 2 ML findings, 7 doc_audit defects found and fixed, 4 commits.
GAPS: Cannot grade UK T-13/T-06 on a daily close as WALTER asked — this desk has no free daily gilt source, so 5.94%/5.36% are relayed intraday quotes and are logged as NEAR-TRIGGERS, not fires. OAT level carries an unresolved ~7bp source basis gap (verdict robust, level is not). ESRB esrb.report202602 still unread at primary, so the no-onward-routing constraint on ESRB findings still binds.
WILL_NEEDS: None.
FOLLOW-UP: (1) Register a DOCKET row for the 2026-10-29 GovC — HANS-T-04 is one 25bp hike from firing. (2) HANS-T-08 needs a REGISTERED EXIT CONDITION and an AGSI-derived norm; I ruled the -14.7pp crossing not-an-exit by hand and that should not be a recurring hand ruling. (3) WALTER owes two fixes on COR-20260908-04 (pointer, date_cap). (4) NOT PUSHED — PROME serializes pushes this session; 4 HANS commits sit local.

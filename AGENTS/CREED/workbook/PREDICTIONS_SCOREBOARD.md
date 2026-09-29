# CREED Predictions Scoreboard

**Created:** 2026-07-27 · **Updated:** 2026-09-29 *(**FIFTH RESOLUTION — `PRED-CREED-005` HIT (70%, Brier 0.09)**: ARI stockholders approved the Plan of Complete Liquidation and Dissolution on 9/29, 8-K Item 5.07 filed the same day, PRIMARY-READ. n=4 → n=5; mean Brier 0.37375 → 0.317. Not Kernel-pinned, so no ledger divergence on this row.)* · Prior 2026-09-28 *(**THIRD + FOURTH RESOLUTIONS — `PRED-CREED-004` HIT (60%, Brier 0.16) and `PRED-CREED-007` MISS (15%, Brier 0.7225)**, graded on CREED's own ledger under **WQ-304 option B** (Will verbatim *"Approve WQ-303 at 4 and WQ-304 option B"*, 2026-09-28, `PROME/WILL_QUEUE.md` @`47623f8b1`). n=2 → n=4. ⚠️ **The Kernel ledger disagrees until a Gate C sitting settles it** — see §SCORE.)* · Prior 2026-08-27 *(**SECOND RESOLUTION — `PRED-CREED-003` RESOLVED-FALSE** on the FDIC Q2 QBP, correct side, Brier 0.1225. n=1 → n=2.)* · Prior 2026-08-20 *(row `002` refreshed to the July SS print in a self-audit — it had carried a June distance AND a since-reversed direction)* · (**FIRST RESOLUTION — `PRED-CREED-009` RESOLVED-TRUE**, and it is a calibration MISS: called at 30%, resolved TRUE, Brier 0.49, worse than a coin flip. n=0 → n=1.)
Tracks resolution outcomes and calibration for CREED's pre-registered predictions. Open rows live in `PREDICTIONS.tsv`; this is the **summary + calibration read**.

> **Created at n=0 on purpose.** CREED registered **10 predictions with self-set confidences** on 2026-07-27 (Will's §10 decision 2, 7/21: *"YES, you set them — your conviction, your numbers"*) and had **no calibration surface at all**. The discipline has to exist **before** the first resolution — otherwise the first resolution sets the precedent for skipping it. *(Adopted from BROCK's scoreboard, which at n=10 produced a read that changed its behaviour.)*

---

## SCORE (fully-resolved, gradeable)

| Hit rate (correct side) | Brier (mean) | Baseline |
|---|---|---|
| **n = 5 — 3/5 (60%)** | **0.317** *(1.585 / 5; was 0.37375 at n=4, 0.30625 at n=2)* | 0.25 (coin-flip) |

| ID | Call | Conf | Outcome | Side | Brier |
|---|---|:--:|---|---|---:|
| `PRED-CREED-009` | matured-balloon share sustains >50% | 30% | **TRUE** | ✗ wrong | 0.49 |
| `PRED-CREED-003` | large-bank CRE PDNA RISES on Q2 QBP, ending the streak | 35% | **FALSE** | ✓ right | **0.1225** |
| `PRED-CREED-007` | VNQ trails SPY ≥10pp over a trailing 3-mo window (the S8a trigger) | 15% | **TRUE** (−10.12 TR 9/24 · −13.06 9/25) | ✗ wrong | **0.7225** |
| `PRED-CREED-004` | a further CRE mREIT cuts / reviews / winds down | 60% | **TRUE** (GPMT review 9/23 + cut $0.05→$0.01) | ✓ right | **0.16** |
| `PRED-CREED-005` | ARI liquidation plan receives stockholder approval (not amended / terminated / merged) | 70% | **TRUE** (9/29: For 72,217,727 · Against 799,088 · Abstain 439,400; 8-K Item 5.07) | ✓ right | **0.09** |

> 🔴 **2026-09-28 — the mean Brier WORSENS 0.30625 → 0.37375, and that is the honest consequence of grading, not a defect.** Leaving 004/007 open would have FLATTERED the record (CATO WR30/WR31; PROME recomputed the figures from this ledger). **`007` is the book's worst score:** the 15% "honesty anchor" priced the office-demand counter-signal and did not price a rate shock — the fire was rate-led (10y 4.38 → 5.18% on the window, FOMC +25bp 9/16) while tenant demand was still improving. ⚠️ **n=4 is still not a calibration read.**
>
> ⚠️ **TWO LEDGERS DISAGREE, DELIBERATELY (dated 2026-09-28).** Both rows are Kernel-pinned (Sitting 2). Under option B this ledger grades them now; **the Kernel records stay OPEN** until a Gate C sitting resolves them retroactively. **No Gate C window is live; carve-out ④ is inactive.** Reconciling the two is option B's deferred cost. Cite THIS ledger for CREED's score, and name the divergence when you do.

**`PRED-CREED-003` resolved FALSE and CREED was on the correct side of it.** Called at **35%** — *probably not* — and the FDIC Q2 QBP showed large-bank CRE PDNA **falling** (>$250B nonfarm-nonresidential **2.73% → 2.48%, −25bp**; all-institutions **1.66 → 1.52**, which the QBP itself names the largest quarterly PDNA decline of any portfolio). Brier = (0.35 − 0)² = **0.1225**. Mean Brier improves **0.49 → 0.306**.

> ⚠️ **Do not read that improvement as calibration improving.** It is two observations, and §the finding below is that *neither* of them scored for the reason its rationale gave.

> ⚠️ **n=1 is not a calibration read.** One resolution cannot distinguish a bad process from an unlucky draw, and the Brier number above must not be quoted as CREED's calibration. **What IS readable at n=1 is the RATIONALE**, and that is where the finding is.

### 🔴 The finding at n=1: the confidence was low for a reason that was FALSE WHEN WRITTEN

`009`'s registered rationale held it at 30% **explicitly** on data-availability grounds:

> *"Held at 30% because CREED does not currently receive the new-delinquency COMPOSITION split monthly… **RESOLVABILITY RISK IS REAL: if the composition data stays unavailable this becomes STUCK, not wrong.**"*

**Trepp publishes that split, in prose, in every monthly report — and published it in all four of April, May, June and July.** The confidence was suppressed by an assumption about CREED's own *reach*, not by a judgement about the *world*.

**This matters more than the score.** A prediction priced low on a false unavailability premise:
- **scores as well-calibrated whenever it resolves FALSE**, for reasons unrelated to the analyst's model of the world, and
- **teaches nothing when it resolves TRUE**, because the miss reads as ordinary bear-skew rather than a broken input.

**Rule adopted 2026-08-20:** *before pricing a prediction low on resolvability, establish that the datum is genuinely unpublished rather than merely unfetched.* Same root cause, same channel, same session as FORUM 5 item **W1** (`VX-CREED-3.01`, where CREED and HOMER both declared a published figure "not published" after reaching only the Connect-CRE secondary). **Two independent instances of one defect, found the same day — a process finding, not two coincidences.**

### 🔴🔴 The finding at n=2 — **THE SAME DEFECT, ON THE OTHER SIDE OF THE SCORE**

`003`'s registered rationale priced it below 50% on an explicit factual premise:

> *"Below 50% deliberately: **the series has improved for SIX straight quarters**, the Q1 print was still improving…"*

**That premise is not verifiable on any source CREED can currently reach, and it is FALSE on the nearest available one.** Grading this prediction forced the first like-for-like pull of the cited cell across four QBP editions, and the >$250B nonfarm-nonresidential PDNA series reads **Q3-25 3.20 → Q4-25 3.23 → Q1-26 2.73 → Q2-26 2.48**. **Q4-2025 is a RISE.** There is no six-quarter streak on that basis, and the same pull showed the row's **3.40% baseline cannot be reproduced from the FDIC Q1 2026 QBP it cites at all** (`KB-CREED-024`).

**So both of CREED's two graded predictions were priced on premises that did not hold — and the scoring is uninformative about the model in both cases:**

| | `009` | `003` |
|---|---|---|
| Premise in the rationale | "CREED does not receive the composition split" | "the series has improved for six straight quarters" |
| Was it true when written? | **No** — Trepp published it monthly | **Not verifiable; false on the only basis reachable** |
| Resolved | TRUE | FALSE |
| Scored | **badly** (0.49) | **well** (0.1225) |
| What the score tells us about CREED's model | **nothing** | **nothing** |

> 🔴 **This is the sharper version of the 8/20 rule, and it now has two instances pointing opposite ways.** A prediction priced on a false premise is not a forecast — it is a coin weighted by an error, and **the Brier score cannot tell you which.** `009` looked like bear-skew and was a broken input; `003` looks like well-judged restraint and rests on a streak that is not in the data. **A good score from a bad premise is the more dangerous of the two, because nothing prompts anyone to look.**
>
> **Rule extended 2026-08-27:** *before pricing a prediction on a stated fact about a series' own history — its streak, its trend, its level — pull that history.* The 8/20 rule covered **resolvability** premises; this one covers **baseline** premises. **Both defects were invisible until a resolution forced a primary pull**, which is the argument for pulling at WRITE time.

**Next resolutions due (as of 2026-09-29):** `006`+`010` joint (MBA Q2, ~wk of 9/28) · `001`/`002` (Trepp monthly, by 12/31; Sept DQ ~10/01) · `008` (KREF Q4, ~Feb 2027).

### Excluded from calibration (recorded for provenance only)

| ID | Call | Conf | Outcome | Why excluded |
|---|---|---|---|---|
| `PRED-CREED-002a` | June office SS prints above 17.00%, up from May's 16.75% | **none recorded** | ✅ correct — June office SS = **17.11%** | Written into `WORKBOOK_DESIGN` §7 on 7/4 as a build candidate and **resolved 7/15, before the workbook existed**. **No confidence was recorded at the time, so it is not gradeable.** Counting it would inflate the hit rate with a call that carried no risk. |

---

## OPEN BOOK (5 open, 5 graded + 1 excluded) — what each one actually tests

| ID | Conf | Resolves | Tests |
|---|:--:|---|---|
| `001` | 40% | Trepp monthly DQ, by 12/31 | office DQ >12% **and holds 2 consecutive** — the "holds" clause is doing the work. **Jul print in: 11.91% (+34bps), still 9bps below trigger — NOT resolved, largest MoM move since Jan** |
| `002` | 45% | Trepp monthly SS, by 12/31 | office SS crosses **18%** (the S1 trigger). ⚠️ **UPDATED 8/20 — the trajectory REVERSED and this row had missed it.** July SS **16.58% (−53bps)**: now **142bps away and MOVING AWAY**, not "89bps away at +36bps/mo". **The direction, not just the distance, was stale.** Trepp attributes the fall to workout/resolution activity on the seasoned book — **not** to absent distress, which is entering via the DQ door instead. **Confidence UNCHANGED at 45%** — the resolution window runs to 12/31 and one month against does not re-price a 4-month call. |
| ~~`003`~~ | ~~35%~~ | **RESOLVED-FALSE 2026-08-27** | S3's trigger — **did NOT rise.** >$250B CRE PDNA 2.73 → **2.48** (−25bp), 2nd straight decline; reserve coverage 166.8 → **172.7**. `CREED-T-03` **NOT FIRED**. **Moved to SCORE above.** ⚠️ Its "six straight quarters" premise does not survive the primary pull — see the n=2 finding |
| ~~`004`~~ | ~~60%~~ | **RESOLVED-TRUE 2026-09-28 (event 9/23)** | **HIT** — GPMT formal Board review (sale / combination / capital raise) + dividend cut. ARI's template propagated to one more name. **Moved to SCORE above.** Kernel record still OPEN (option B) |
| ~~`005`~~ | ~~70%~~ | **RESOLVED-TRUE 2026-09-29** | **HIT** — dissolution **approved** at the 9/29 Special Meeting (98.9% of votes cast For; ~57.1% of outstanding represented). No amendment, termination or merger. **Moved to SCORE above.** ⚠️ First-distribution amount/dates NOT yet declared |
| `006` | **30%** ⚠️ | MBA Q2, ~mid-Sept | the **aggregate** life-insurer line rises **≥ +$10.0B** *(re-spec'd 7/27 — see below)* |
| ~~`007`~~ | ~~15%~~ | **RESOLVED-TRUE 2026-09-28 (condition met 9/24)** | **MISS** — the S8a trigger fired (`CREED-T-08a`). The counter-signal it anchored is gone, taken by rates rather than tenants. **Moved to SCORE above.** Kernel record still OPEN (option B) |
| `008` | 45% | KREF Q4, ~Feb 2027 | management's own <10% legacy-office target |
| ~~`009`~~ | ~~30%~~ | **RESOLVED-TRUE 2026-08-20** | the S2 trigger — **FIRED.** May 70 / Jun 65 / Jul 66; sustain met at the **June** print. **Moved to SCORE above.** The "resolvability risk" clause was the defect, not the safeguard |
| `010` | 70% | **Athene Q2 10-Q, ~Aug** | the **acquirer's own balance sheet** — second independent surface for the ARI $9B. **Athene leg read 8/13, off the primary 10-Q (filed 8/10): Δ +$6.9B — PARTIAL band, $103M short of the $7.0B LANDED bar. Primary now confirms final purchase price $8.7B (not ~$9B). NOT a full resolution — waits on `006` for the joint verdict per this pair's grading rule** |

---

## CALIBRATION READ

**🆕 n=4 (2026-09-28) — still NOT a calibration read, but the n=0 baseline's `007` bullet has now been tested and FAILED.** The "honesty anchor" at 15% resolved TRUE (Brier 0.7225) — **its rationale priced the tape as a proxy for office demand, and the tape moved on RATES instead.** Unlike `009`/`003`, the premise was not factually false when written (REITs *were* outperforming, +2.04pp 7/27); what it omitted was a channel. **Read: a low confidence on a trigger must name which drivers it is betting against, not only which it is honouring.** `004` resolved on the correct side at 60% on its stated template-propagation mechanism (GPMT). Confidences on open rows **unchanged** — no post-hoc adjustment at n=4. *The n=1 text below is preserved as written.*

**n=1 — still nothing gradeable, but one structural read is now available and it runs AGAINST the pre-registered expectation below.**

🔴 **The bear-skew hypothesis just took its first hit, from a direction it did not anticipate.** The note below pre-registered that if the low-confidence structural calls resolved correct, the read would be *"structural calls under-priced."* `009` — one of the two lowest in the book at 30% — **did** resolve in CREED's thesis direction. But it was under-priced **not** out of analytical conservatism about a structural call; it was under-priced on a **false belief about data access**. **So the first datum does not support "raise the structural confidences." It supports "audit every rationale for availability assumptions before touching any number."** Confidences unchanged this session — moving them on n=1, off a rationale defect, is exactly the post-hoc adjustment this book was built to prevent.

*Original n=0 baseline, preserved unchanged:*

- **The book is deliberately bear-skewed-LOW.** Seven of ten sit at or below 45%, and the two trigger-crossing predictions most aligned with CREED's own thesis (`003` FDIC at 35%, `009` S2 composition at 30%) carry the **lowest** confidences in the book. That is intentional — betting against a **six-quarter improvement streak** (`003`) needs more than a thesis. **If these resolve correct at high rates, the read is "structural calls under-priced" and confidences should rise. If they resolve wrong, the thesis is over-weighted, not the confidences.**
- **`007` at 15% is the honesty anchor.** It is the trigger for the signal that most contradicts CREED's bear read, and writing a low number on it holds the thesis accountable to a tape that has moved *against* CREED for three consecutive sessions (−2.9pp → −1.6pp → **+2.04pp**).
- **`006` + `010` are a matched pair and must be graded together, not separately.** Both test the same event (the ARI→Athene $9B) on different surfaces. **Grading them independently would double-count one transaction.** The joint read: both move = confirmed; only Athene moves = `006` is a **bad instrument, not a bad thesis**; **neither moves = the migration read needs re-derivation.**

---

## ⚠️ RE-SPEC LOG — `PRED-CREED-006`, 2026-07-27 (same day it was written)

**The original spec was defective and would have resolved TRUE on an information-free print.** Caught by SHADE within hours, **independently verified by CREED against MBA primary releases**, re-spec'd the same session.

**The defect:** the spec read *"rising by MORE than the Q1 pace of +$3.3B."* **+$3.3B is a seasonal trough, not a run-rate.**

| Quarter | Life-insurer CM/MF change | Verified |
|---|---:|---|
| H1-2025 (Q1+Q2 **combined**) | **+$4.4B** | SHADE, MBA Q4-25 PDF |
| Q3-2025 | +$12.1B | SHADE, MBA Q4-25 PDF |
| Q4-2025 | **+$11.5B (+1.5%)**, stock $774B | ✅ CREED, MBA release |
| Q1-2026 | **+$3.3B (+0.4%)**, stock $775B | ✅ CREED, MBA release |

**H2-2025 ran ~5× H1-2025.** A **+$11B** Q2 print would have satisfied the old spec while being an entirely normal H2-magnitude quarter carrying **zero information about ARI**.

**What CREED did NOT adopt — SHADE proposed a ~+$20B bar, and that over-corrects by the same error class in the opposite direction.** The $20B anchors to the **H2** norm (+$11–12B), but **Q2 is a seasonally weak H1 quarter**: H1-2025 averaged ~+$2.2B/qtr and Q1-2026 printed +$3.3B. The no-ARI counterfactual for Q2-2026 is **~+$2–4B**, so ARI's ~$9B landing visibly produces **~+$11–13B** — which **fails a $20B bar.** *A $20B bar can resolve FALSE even if the entire $9B lands in the line.*

**The bar set: ≥ +$10.0B** — ~3× the highest observed H1 quarterly change, ~4.5× the H1-2025 per-quarter average. Reachable essentially only if a large **discrete block** lands.

**Measurement basis also fixed:** MBA rounds to the nearest $B **and revises prior quarters** — as published, $774B (Q4) + $3.3B ≠ $775B (Q1). **A threshold that subtracts a remembered prior stock is fragile.** The re-spec reads the change **off the carrying release itself.**

**Confidence 65% → 30%, and this is a genuine probability update, not a resolvability trim.** SHADE read **Annex A §2.8** of the DEFM14A (`0001193125-26-119995`) directly: Athene may, **by private written notice 10 business days before closing**, designate *Affiliates, Managed Accounts or Portfolio Companies* — including the **ACRA co-invest vehicles** — to acquire **"all or any portion of the Assets."** The split was never disclosed. The MBA line derives from the **Fed's US life-insurance-company sector**, which does not contain those vehicles. **That is an explicit contractual right to route the assets outside the instrument — information CREED did not have at Made_Date.**

**Legitimacy check (`finding_rebased_metric_check_made_date`):** was the NEW metric already true at Made_Date? **No** — Q1-2026's +$3.3B does not clear +$10B. So this is a **re-spec, not a retire-and-replace.**

**Branch 2 now names the §2.8 case explicitly:** `010` moves but `006` doesn't ⇒ the assets landed **wholly or largely** outside the Fed US life sector (ACRA / managed-account / portfolio-company vehicles) ⇒ **the MBA line is a bad instrument for this channel — a finding, not a miss.**

> **⚠️ Branch-2 wording amended 2026-07-27 — SHADE ask, ACCEPTED.** It must read ***"wholly or largely outside,"*** never a bare *"outside."*
>
> **Why:** §2.8 permits designation of *"all or any **portion**"* of the Assets. **A partial landing is the modal outcome of a clause written that way, not an edge case.**
>
> | Landing in the Fed US life sector | Q2 print (approx) | `006` at ≥ +$10B |
> |---|---:|---|
> | Full ~$9B | +$11–13B | ✅ TRUE |
> | **~$4–5B (partial)** | **+$7–9B** | ❌ **FALSE** |
> | ~None | +$2–4B | ❌ FALSE |
>
> **A partial landing and a full exclusion produce the same verdict.** The bar is binary; the underlying quantity is continuous and **partitionable by private notice**.
>
> **The level was deliberately NOT moved.** +$10.0B is well-chosen for the full-landing case, and **CREED will not tune a bar to an unobservable split** — that fits the test to a quantity nobody can see. **The cost is recorded rather than engineered away: a half-landing must not be written up as a clean instrument failure.**

> **The lesson worth keeping:** the original bar failed on its **baseline**, not its threshold. *"Materially above the last print"* is only a test if the last print is representative — and a single prior observation cannot tell you that. **Anchor a threshold to a distribution, not to the most recent number.** *(See also `finding_single_month_subcomponent_skepticism`, `finding_delta_vs_own_prior_local_extreme`.)*

---

## RESOLUTION PROTOCOL — both writes, or neither counts

1. **Update the `PREDICTIONS.tsv` row AND this file in the same session.** *(BROCK's `BRK-29` was substantively graded in STATUS prose on 7/4 but its ledger row sat `Status=OPEN` for **5 days** past its own resolve date — a "said it but didn't file it" gap caught only by an explicit resolve-date scan.)* **A narrative grade in STATUS is not a substitute for the ledger row.**
2. **Scan resolve dates at boot**, not at closeout — an overdue row is information the session should have *before* it does its work.
3. **A prediction that cannot resolve is `STUCK` — a Status change, never a confidence cut.** Ask *"what number goes from X% to Y%?"*; if there isn't one, it's a resolvability defect. `PRED-CREED-009` is the live candidate.
4. **Grade the premise, not just the outcome.** BROCK's `BRK-09` missed at 60% because the underlying framing was **factually inverted** — the fix was verifying the premise at *creation*, not lowering confidence. **A wrong-premise miss and a well-calibrated low-confidence miss are different species and must be labelled differently here.**
5. **Never retro-fit a confidence.** See `PRED-CREED-002a` above.

# CARL CONSUMER BOOK — DESIGN v0.1

**Status:** ✅ **PHASE 1 (paper sleeve) APPROVED by Will 2026-07-24 and LIVE — NO CAPITAL.** Ledger `book/PAPER_SLEEVE.tsv`, conventions `book/README.md`. Phases beyond 1 remain proposal-only.

> ⚠️ **Architecture change on build:** §6 proposed a sleeve *inside* TERRY's `PAPER_BOOK.tsv`. Reading TERRY's spec showed that's the wrong shape — that book measures **card quality** (options fire-cards, defined-risk premium, refusal calibration); this measures **thesis-expression quality** (unlevered equity relative-value). Blending corrupts both, and TERRY's own spec splits lanes to prevent exactly that. **Built adjacent, on TERRY's rules, with TERRY as rules authority and a merge path preserved at scoring time.** TERRY notified and asked to object if the split is wrong.

**Original proposal status line:** PROPOSAL. Nothing here is live. Written 2026-07-24 at Will's direction after he proposed a CARL book scoped to **consumer-focused equities, explicitly NOT regional banks**.
**Decision owner:** Will. **Construction owner if approved:** TERRY. **Position surface:** FORGE.

> **I argued against a CARL book earlier the same day and then changed my mind on evidence.** That reversal is recorded in §2 rather than buried, because the evidence that changed it is also the evidence this design rests on — and if the evidence is wrong, so is the design.

---

## 1. The problem this solves

**CARL generates consumer-specific evidence that has no expression path.** Today alone: gas crossing $4.00 with a first-ever two-surge base-rate break · Edmunds negative-equity payment records ($944, $6,884) · CRMT's rescue financing defaulting with 40% of stores closed · FHA total DQ 11.88% · FL cost-stack bifurcation. None of it is expressible through REGINALD's book (banks), HENRY's (macro/vol), or BRENT's (energy).

**And the one position commitment CARL did write was unexecutable.** CRL-21's clause — *"trim short positions 25% + extend duration to Q2 2027+"* — named no surface and no legs. When it came time to surface it, the positions it was written against had already expired (WAL/ZION/OZK, Jul-17); the sole survivor is one KRE $25P Jan-2027 that FORGE labels a "deep-OTM lottery." **A research agent wrote a trading commitment it could neither see nor execute.**

---

## 2. The evidence — including the part that cuts against the design

### 2a. What changed my mind

One-year total return to 2026-07-24, vs S&P **+14.7%**:

| | 1y | vs SPX | |
|---|---|---|---|
| XLY | −5.6% | **−20.3pp** | broad discretionary |
| COF | −10.7% | **−25.5pp** | *released $662M of reserves, NCO −39bps* |
| SYF | −4.5% | **−19.2pp** | *NCO 5.43%, under its guide ceiling* |
| AXP | −1.5% | **−16.3pp** | *billings +9%, write-offs flat, guide raised* |
| CRMT | −93.2% | **−107.9pp** | CARL-flagged on going-concern |
| DLTR / WMT / DG | +10.3 / +12.9 / +7.8% | −4.4 / −1.9 / −6.9pp | trade-down cohort |

**The equity expression worked in exactly the places the credit expression failed — and that is the masking framework's own logic.** If issuer credit metrics are survivor-biased and lag, then equity (forward-discounting on the same cohort) should lead credit *by approximately the masking lag*. **CARL had never drawn that inference from its own thesis.**

### 2b. The complication that survives, and it is serious

A 21-name breadth test on mega-cap-uncontaminated consumer names confirms the weakness is **real and mostly absolute** (~12 names down 19–47pp relative; BBWI −31.9%, AZO −29.6%, CMG −24.6%, RH −22.7% *in absolute terms*) — so it is not merely an artifact of an AI-led index melt-up.

**But the cross-section does not sort on the K-shape axis:**

- **Auto aftermarket — the classic defensive trade-down winner — is down hardest:** AZO **−44pp**, ORLY **−30pp**, AAP **−23pp**. CARL's own STATUS carries AZO domestic SSS +4.1% as a *defensive counter-channel*. The tape says the opposite, hard.
- **Premium/aspirational is UP:** YETI **+28.6pp**, WSM **+5.8pp**.

**So the honest reading is: consumer equities are genuinely weak, and CARL cannot yet explain the *cross-section* with its own framework.** A book opened today would be trading a signal CARL has not fully characterized. **That is the single strongest argument for Phase 1 being paper.**

> **Partial correction to my own claim, found on build.** I initially wrote that CARL "cannot explain the dispersion." **That overstates it — CARL has a logged, testable explanation for the biggest anomaly.** STATUS L74 and the May-26 CHANGELOG entry characterize AZO's decline as **margin/LIFO-driven, NOT US-demand**, with domestic SSS **+4.1%** as a defensive counter-channel ("CORRECTED-FRAMING"). So the framework *does* make a falsifiable claim about AZO — it just never got connected to the tape. **That claim is now the sleeve's diagnostic position (PS-0005, long AZO against the tape), with invalidation written against the characterization (domestic SSS <+1.0% ⇒ demand not margin ⇒ CARL wrong), not the price.** What remains genuinely unexplained is ORLY/AAP and the premium-up leg (YETI/WSM).

### 2c. Caveats on the evidence itself
One window · one benchmark · back-of-envelope look-back, **not a backtest** · tickers chosen by me (though the set is not obviously cherry-picked — XRT +3.3% and WMT +12.9% cut against the bear case) · no entry/exit timing modelled, which is precisely the untested variable.

---

## 3. Scope

### IN — consumer names where CARL owns the evidence and no other agent does
| Sleeve | Names | CARL evidence base |
|---|---|---|
| Broad discretionary | XLY, XRT | K-shape aggregate, retail control, Beige Book bifurcation |
| Trade-down | DG, DLTR, WMT, TGT | survival-spending / downtrade reads (KB-280s) |
| Deep-subprime retail | CRMT-class | going-concern + survivor-pool mechanism (KB-355) |
| Restaurants / discretionary services | Black Box names, CMG/DRI-class | traffic −3.5%, discretionary capitulation |
| Gig platforms | UBER, LYFT, DASH | GIG sub-agent: oversupply, per-trip compression |
| BNPL / phantom debt | AFRM | PHAN dossier |
| Top-cohort barometer | AXP | the K-shape *top* leg (V8/V14) |
| Builders | DHI, PHM, LEN, KBH | CRL-23 (CARL-owned prediction; HOMER = data owner) |

### OUT — other agents' domains, non-negotiable
**KRE / WAL / OZK / ZION / regional banks → REGINALD** · **rates / vol / TLT / SPX → HENRY, BOND, VIOLET** · **USO / energy → BRENT** · **metals → MIDAS** · **Japan/FX → SAM**

### CONTESTED — routed to REGINALD 2026-07-24; **the conflict appears to be one-sided and in CARL's own file**
**SYF, COF, ALLY.** ⚠️ **Corrected on routing:** I labelled these "contested" on the strength of my own doc without reading REGINALD's. **REGINALD's `CLAUDE.md` DOMAIN SCOPE says verbatim: *"You do NOT own: … Consumer credit → CARL (but delinquencies flow to your NCO estimates)"* — and SYF/COF/ALLY appear ZERO times in it** (their named universe is OZK ×17, WAL ×11, KRE ×5, ZION, EGBN, HBAN, CFG). **The only text assigning these to REGINALD is a parenthetical in CARL's own `CLAUDE.md`** (*"ALLY/COF underwriting standards"*). I asserted a boundary dispute against a file I hadn't checked.

**Also corrected: a ticker split was the wrong frame.** All three are *both* bank holding companies *and* consumer lenders, so ticker-level ownership forces a false choice. REGINALD's own wording implies the right cut — "delinquencies flow to your NCO estimates" means REGINALD **consumes** CARL's consumer read as an input to a bank-level output. **The split is by SURFACE:**

- **CARL takes the consumer-cohort EQUITY read** — multiple, cohort composition, spend/burden.
- **REGINALD keeps bank-credit and underwriting** — provisions, ACL, capital, and any credit-instrument expression.
- **Equity expression on these three → CARL**, on the consumer-cohort thesis. **Credit-instrument expression → REGINALD.**
- **Neither opens a position in these three without notifying the other in-session.** If REGINALD objects, the name is OUT until Will adjudicates.
- ⚠️ **ALLY is the genuinely dual-surface name and CARL defers hardest there** — REGINALD's STATUS tracks it inside the bank-print week (7/21 WAL+OZK+ALLY), so they have live coverage regardless of the CLAUDE.md text. **If REGINALD wants ALLY out, it's out.**
- **Routed 2026-07-24** → `AGENTS/REGINALD/inbox/2026-07-24_from-CARL_syf-cof-ally-boundary-i-may-have-invented-this-conflict.md`. Three-way ruling requested (agree / agree-except-ALLY / disagree); silence past REGINALD's next session reads as agree, per the reply-only-if convention. **Until ruled, the names stay BLOCKED in the sleeve.**

---

## 4. Entry gate

> ⚠️ **Corrected 2026-07-24 on build.** As originally written, all four gates applied to *any* expression — which would have prohibited the paper sleeve Will had just approved, since paper legs are opened by CARL without per-trade TERRY construction or per-trade Will approval. **The gates split by lane:**

**PAPER lane (`lane=paper`) — gates 1 and 2 only:**
1. It ties to a **registered, dated prediction** in `thesis/PREDICTIONS.tsv` with a **declared `Instrument`** — `consistency_check.py` Check D already enforces the declaration half mechanically.
2. The prediction is **OPEN and reachable** — a leg that has become arithmetically unreachable (the CRL-21 failure) disqualifies it.

*Rationale for the lighter gate: paper risks no capital, and per-trade approval would reproduce exactly the near-zero-volume problem TERRY's `PAPER_BOOK_DESIGN.md` identifies as PAT-028. Sizing is fixed by convention ($3,000/position) so CARL is not exercising sizing judgement either way.*

**REAL lane (`lane=real`) — all four, non-negotiable:**
3. **TERRY constructs it.** CARL never sizes, never picks strikes, never sets stops. Rules #6/#7 are TERRY's.
4. **Will approves.** Unchanged by anything in this document.

**Thesis-vibes trades are prohibited in BOTH lanes by construction:** if CARL cannot point at the prediction ID and its instrument, there is no position — paper or real.

---

## 5. Controls — the bias problem, addressed directly

The strongest objection to a CARL book is **not** instrument overlap. It is that **CARL's job is to say "my thesis just took damage," and a book makes that harder.** On 2026-07-24 CARL graded CRL-24 a clean MISS and cut six confidences on a 0-of-4 adverse cycle. That behaviour is the asset; a book puts it at risk.

| Control | Mechanism |
|---|---|
| **Bias tripwire** | ✅ **MECHANISED 2026-07-24 — `consistency_check.py` Check F.** ⚠️ **Not as originally written:** *"adverse data lands"* is not mechanically detectable, so F substitutes what is — **F1** position against a no-longer-OPEN prediction (dead-thesis, the CRL-21 class) · **F2** entry-gate breach · **F3** the **asymmetry signature** (a positioned prediction RAISED in the same change-set where an unpositioned one was CUT — motivated reasoning visible in the deltas, needing no view on whether data was adverse) · **F4** the bias statistic · **F5** marking discipline. 3 acceptance tests passed. **Currently DEGENERATE and says so** — all 5 legs sit on CRL-27, so there is no unpositioned contrast group yet. |
| **RED standing challenge** | RED may challenge any CARL position as thesis-motivated at any time, and CARL must answer in writing. |
| **Pre-registration is the gate** | §4.1 — the prediction must exist *before* the position, so the position cannot retro-justify the view. |
| **Separation of powers** | TERRY constructs, Will approves, FORGE marks, CARL only proposes. CARL gains **no decision rights**. |
| **Public scoreboard** | Every sleeve position carries its prediction ID; the Brier audit (§7) scores prediction and expression together. |

---

## 6. Phase 1 — paper sleeve in TERRY's existing book

**Do not open with capital.** `AGENTS/TERRY/PAPER_BOOK_DESIGN.md` already exists and was built for the analogous problem (*"0 cards fired live → 0 track record → the card product is un-instrumentable"*). CARL needs **a sleeve, not a new book.**

**What Phase 1 tests — and note it is NOT direction:** §2a already suggests the direction has been right. The untested variables are **entry timing, exit discipline, and whether CARL can characterise the dispersion** (§2b) well enough to pick the right names rather than the right theme.

**Graduation criteria to capital — proposed, all four required over ≥2 quarters:**
1. Paper sleeve beats a naive short-XLY benchmark on a risk-adjusted basis (the theme is free; the selection has to add something).
2. **CARL correctly called ≥1 name against its own prior** — e.g. explained or predicted the AZO/ORLY anomaly. Without this, CARL is trading a theme it cannot explain.
3. **Zero bias-tripwire events.**
4. Brier score on the governing predictions has improved or held.

**Kill criteria:** any bias-tripwire event that survives RED challenge, or a REGINALD boundary dispute Will has to adjudicate twice.

---

## 7. Related open work
- **CRL-27 registered 2026-07-24** — the equity-leads-credit prediction. **This design's central premise is CRL-27's subject.** If CRL-27 fails (credit stays clean through Q1-2027 while equity weakness persists), §2a's reading was wrong and this document should be revisited, not defended.
- **Brier audit deferred since v2.5.1 (May 1)** — 26 predictions, 12 resolved, never scored. Should run *before* capital, not after.
- **CARL is tape-blind.** Twice today the tape corrected a read formed from fundamentals (AXP; the whole trade-down leg). That gap is real whether or not this book is approved, and arguably a price/market-data cadence is the cheaper fix.

---

## 8. Open questions for Will
1. ~~**Approve the paper sleeve?**~~ ✅ **APPROVED 2026-07-24, LIVE.** 5 legs open, all `pred_id=CRL-27`.
2. ~~**The SYF/COF/ALLY split with REGINALD**~~ — **ROUTED to REGINALD 2026-07-24.** Only escalates to Will if CARL and REGINALD can't land it between them. Note the finding: the conflict was one-sided and in CARL's file; REGINALD's own scope already routes consumer credit to CARL.
3. **Should the Brier audit be a prerequisite** to Phase 1, or run in parallel?
4. ~~**Does the bias tripwire go in `consistency_check.py`?**~~ ✅ **MECHANISED 2026-07-24 as Check F** — see §5. **All four §8 questions are now closed.**

*Nothing in this document is live. No position exists. Approval gates every element.*

# CREED Predictions Scoreboard

**Created:** 2026-07-27 · **Updated:** 2026-07-27
Tracks resolution outcomes and calibration for CREED's pre-registered predictions. Open rows live in `PREDICTIONS.tsv`; this is the **summary + calibration read**.

> **Created at n=0 on purpose.** CREED registered **10 predictions with self-set confidences** on 2026-07-27 (Will's §10 decision 2, 7/21: *"YES, you set them — your conviction, your numbers"*) and had **no calibration surface at all**. The discipline has to exist **before** the first resolution — otherwise the first resolution sets the precedent for skipping it. *(Adopted from BROCK's scoreboard, which at n=10 produced a read that changed its behaviour.)*

---

## SCORE (fully-resolved, gradeable)

| Hit rate | Brier (mean) | Baseline |
|---|---|---|
| **n = 0** | — | 0.25 (coin-flip) |

**No CREED prediction has resolved yet.** First resolutions due: `PRED-CREED-002` (July SS, ~mid-Aug) and `PRED-CREED-001` (July DQ, ~early Aug).

### Excluded from calibration (recorded for provenance only)

| ID | Call | Conf | Outcome | Why excluded |
|---|---|---|---|---|
| `PRED-CREED-002a` | June office SS prints above 17.00%, up from May's 16.75% | **none recorded** | ✅ correct — June office SS = **17.11%** | Written into `WORKBOOK_DESIGN` §7 on 7/4 as a build candidate and **resolved 7/15, before the workbook existed**. **No confidence was recorded at the time, so it is not gradeable.** Counting it would inflate the hit rate with a call that carried no risk. |

---

## OPEN BOOK (10) — what each one actually tests

| ID | Conf | Resolves | Tests |
|---|:--:|---|---|
| `001` | 40% | Trepp monthly DQ, by 12/31 | office DQ >12% **and holds 2 consecutive** — the "holds" clause is doing the work |
| `002` | 45% | Trepp monthly SS, by 12/31 | office SS crosses **18%** (the S1 trigger). 89bps away at +36bps/mo |
| `003` | **35%** | **FDIC Q2 QBP, ~late Aug** | **S3's actual trigger** — large-bank non-owner CRE PDNA rising vs Q1's 3.40%. *The single most decision-relevant open item* |
| `004` | 60% | 8-K / earnings, by 12/31 | a **4th** CRE mREIT cuts / reviews / winds down — does ARI's template propagate? |
| `005` | 70% | ARI proxy + vote | dissolution actually **approved** (board-resolved ≠ approved) |
| `006` | 65% | MBA Q2, ~mid-Sept | the **aggregate** life-insurer line moves more than +$3.3B |
| `007` | **15%** | market data, by 12/31 | the S8a trigger (VNQ −10pp/3mo). **Deliberately low — this is the counter-signal CREED is committed to honoring** |
| `008` | 45% | KREF Q4, ~Feb 2027 | management's own <10% legacy-office target |
| `009` | 30% | Trepp composition, by 12/31 | the S2 trigger. **Resolvability risk is real** — if composition data stays unavailable this is `STUCK`, not wrong |
| `010` | 70% | **Athene Q2 10-Q, ~Aug** | the **acquirer's own balance sheet** — second independent surface for the ARI $9B |

---

## CALIBRATION READ

**Nothing to read yet — n=0.** Recorded now so the first read has a baseline to be measured against:

- **The book is deliberately bear-skewed-LOW.** Seven of ten sit at or below 45%, and the two trigger-crossing predictions most aligned with CREED's own thesis (`003` FDIC at 35%, `009` S2 composition at 30%) carry the **lowest** confidences in the book. That is intentional — betting against a **six-quarter improvement streak** (`003`) needs more than a thesis. **If these resolve correct at high rates, the read is "structural calls under-priced" and confidences should rise. If they resolve wrong, the thesis is over-weighted, not the confidences.**
- **`007` at 15% is the honesty anchor.** It is the trigger for the signal that most contradicts CREED's bear read, and writing a low number on it holds the thesis accountable to a tape that has moved *against* CREED for three consecutive sessions (−2.9pp → −1.6pp → **+2.04pp**).
- **`006` + `010` are a matched pair and must be graded together, not separately.** Both test the same event (the ARI→Athene $9B) on different surfaces. **Grading them independently would double-count one transaction.** The joint read: both move = confirmed; only Athene moves = `006` is a **bad instrument, not a bad thesis**; **neither moves = the migration read needs re-derivation.**

---

## RESOLUTION PROTOCOL — both writes, or neither counts

1. **Update the `PREDICTIONS.tsv` row AND this file in the same session.** *(BROCK's `BRK-29` was substantively graded in STATUS prose on 7/4 but its ledger row sat `Status=OPEN` for **5 days** past its own resolve date — a "said it but didn't file it" gap caught only by an explicit resolve-date scan.)* **A narrative grade in STATUS is not a substitute for the ledger row.**
2. **Scan resolve dates at boot**, not at closeout — an overdue row is information the session should have *before* it does its work.
3. **A prediction that cannot resolve is `STUCK` — a Status change, never a confidence cut.** Ask *"what number goes from X% to Y%?"*; if there isn't one, it's a resolvability defect. `PRED-CREED-009` is the live candidate.
4. **Grade the premise, not just the outcome.** BROCK's `BRK-09` missed at 60% because the underlying framing was **factually inverted** — the fix was verifying the premise at *creation*, not lowering confidence. **A wrong-premise miss and a well-calibrated low-confidence miss are different species and must be labelled differently here.**
5. **Never retro-fit a confidence.** See `PRED-CREED-002a` above.

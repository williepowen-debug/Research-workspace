# UST behaviour around the five 2026 MOF yen-buying operations — and three errors it was used to support

**Written 2026-09-20 by SAM, after a CATO review (`4ab2133c3`) found three consequential errors in how this study was reported to Will. All three are upheld. This file is the corrected record; the study itself stands, with its limits stated.**

Reproduce: `.venv/bin/python3 AGENTS/SAM/research/outputs/2026-09-20_intervention-ust-study/study.py` → `output.json`.
⚠️ **The original table was run inline in a shell heredoc and saved nowhere.** CATO could not reproduce it, and was right to say so: a load-bearing number with no artifact is not a finding. Fixed here.

## The measurement

Operation days — MOF per-operation disclosure (`feio/quarter/2026_2Qe.html`) for April/May; July 30 and 31 are the two operation days inside the Jul-30→Aug-26 reporting window, whose per-op split is not published until ~Nov-9.

| From each op day | +1d | +2d | +3d | +5d |
|---|---|---|---|---|
| TLT, % | +0.02 | +0.34 | **+0.42** | +0.14 |
| US 30Y, bp | −0.3 | −2.0 | **−2.7** | −0.2 |

Baseline, 176 sessions Jan–Sep 2026: TLT 3-day **−0.06%** (sd 0.94), 30Y 3-day **+0.79bp** (sd 5.84).

**Direction: Treasuries rallied and long yields fell around the operations.** That is the opposite of a "MOF sells USTs to fund the intervention, so yields rise" story.

## ⛔ What this study CANNOT support — three corrections

**① "Cannot detect an effect" is not "the channel is too small." (CATO, upheld.)** The study finds no distinguishable effect. That is a statement about the study's power, not about the world. I reported it as if absence of evidence established a mechanism; it does not.

**② The independence assumption is false, so even the nominal error bar is too small. (CATO, upheld.)** Apr-30, May-4 and May-6 sit within five business days, so their +3d and +5d windows **overlap**. There are five dates but roughly **two independent campaigns**. The nominal standard error (2.61bp) assumes five independent draws and therefore **overstates precision**. ⇒ **This study cannot support a significance claim in either direction.**

**③ The "$98B spread over four weeks" framing was wrong, and my own file says so. (CATO, upheld.)** ¥15,399.3B is the **MOF reporting window** Jul-30→Aug-26 — a reporting interval, not a spending schedule. This desk's own record decomposes it as **7/30 ~¥8.45T (Bloomberg estimate) + 7/31 ~¥6.95T (derived residual)** ⇒ essentially the whole amount on **two days**. Corrected scale: ~**$49B/day for two days**, against US Treasury cash volume on the order of $900B/day ≈ **5% of a session**, not the ~1%-spread-over-a-month I implied. **That is an order of magnitude more concentrated and materially weakens the size argument I built on it.**

## What survives

The **direction** of the observed moves, as a descriptive fact with its window and baseline stated. Nothing about mechanism, and no claim that intervention does or does not move Treasuries. **The honest status is UNRESOLVED, and the November primaries (MOF quarterly ~Nov-9, FRBNY ~Nov-13) remain the instruments that settle the funding question.** What changed is that I no longer assert a directional prior while waiting for them.

## A fourth error, not in this study but reported alongside it

**Instrument direction on Will's own book.** I described KRE / HBAN / WAL as an equity cluster exposed to a risk-off. **They are PUTS** — KRE $60P and $25P, HBAN $16P, WAL $70P / $67.5P / $77.5P — i.e. short regional-bank exposure. A bank selloff **helps** them. I read a ticker list out of table rows and never read the instrument column. ⇒ My conclusion that the bank leg and the duration-short leg "lose together in a Japan shock" is **backwards**: in a flight-to-quality the duration-short legs lose and the bank puts gain, which **partially offsets**. ⚠️ Size is a separate question and is NOT established here — most of those puts were marked at pennies (−74% to −99%) on a **9/10-vintage mirror that its own banner calls contradicted on six Fidelity cells and the Robinhood account**. Direction is structural; size needs a reconcile.

📌 **Class:** `[[finding_unqualified_identifier_is_a_defect_waiting_for_a_reader]]` — a ticker without its instrument is not a position. And the tell I missed: I was answering a question about *his book* from a surface I had just finished describing as stale and contradicted.

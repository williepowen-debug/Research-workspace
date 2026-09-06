# `^SKEW` mirror vs publisher — **full-history census. Three defect modes, 4.31% of sessions, and the dominant one is structured against sustain counting.**

**Date:** 2026-09-06 ~11:5x ET · **Owner:** RED · **Closes:** WALTER's 8/28 question (`SIG-W-20260903-001` §3) · **Supersedes:** RED's published `0.79%/session` figure · **Bears on:** VIOLET's open 2025-12-24 item, and `RED-FT-10`'s basis declaration

---

## 0. BOTTOM LINE

**I went looking for one bar and found that my own published defect rate was wrong in both directions.**

| measurement | RED published (9/2) | measured today |
|---|:--:|:--:|
| 253-session window | **0.79%/session** | **0.40%/session** |
| **full history (9,221 sessions)** | *never measured* | **4.31%/session** |

**The 253-session sample was unrepresentatively CLEAN and I generalised from it.** Full history: **62 omissions (0.67%) + 335 value disagreements (3.66%) = 397 defective sessions of 9,221.**

**And the defect is not noise — it is STRUCTURED, in the one shape that is adversarial to a sustain counter.** That is a materially stronger justification for the CBOE basis than the one I gave.

---

## 1. WALTER's question, answered as far as the evidence permits — and no further

**Asked:** RED's 9/2 claim that yfinance OMITS the 2026-08-28 bar did not reproduce on WALTER's 9/3 pull. *Backfilled between pulls, or did RED's original window drop it?*

**Measured today, across window specs:**

| `period=` | 5d | 15d | 1mo | 3mo | 6mo | 1y | 2y | max |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 8/28 bar | **ABSENT** | 149.77 | 149.77 | 149.77 | 149.77 | 149.77 | 149.77 | 149.77 |

⇒ **The short-window mechanism is REAL — `period=5d` drops it** — and the bar is present in every window ≥15d.

**⛔ I cannot distinguish the two hypotheses and I am not going to pretend otherwise.** `fetch.py`'s audit log records ticker counts and latency, **not the returned frame**, so the 9/2 pull is unrecoverable. **The evidence that would settle it does not exist.**

**What I can do is correct the consequence, which is the part that travelled:** **the published `0.79%/session` is WITHDRAWN and replaced by `0.40%/session` on that window** — the reproducible figure. Either the bar was backfilled (0.79% was right when measured, and the defect is *transient*, which is worse for a grader, not better) or my window dropped it (0.79% was wrong when published). **Both readings require the correction; only the blame differs, and the blame is the least interesting part.**

## 2. The census (full history, 1990-01-02 → 2026-09-04)

| | CBOE (publisher of record) | yfinance `^SKEW` |
|---|:--:|:--:|
| bars | **9,221** | 9,163 |

| defect mode | sessions | rate |
|---|:--:|:--:|
| **① OMISSION** — CBOE bar absent from mirror | **62** | 0.67% |
| **② FORWARD-FILL** — mirror repeats its own prior value while CBOE moved | **77** | 0.84% |
| **③ DATE-SHIFT** — mirror value equals CBOE's *previous* session | **316** | 3.43% |
| *(② and ③ overlap; total distinct disagreements)* | **335** | 3.66% |
| **TOTAL DEFECTIVE** | **397** | **4.31%** |
| extra bars in mirror (not at CBOE) | 4 | — |

**I previously reported TWO defect modes. There are at least THREE, and the two I had were the two smallest.**

## 3. 🔴 Why mode ② is the one that matters — a worked example

| session | CBOE | mirror |
|---|:--:|:--:|
| 2023-11-29 | 139.82 | 139.82 ✅ |
| 2023-11-30 | 140.91 | **144.54** |
| 2023-12-01 | 138.04 | **144.54** |
| 2023-12-04 | 136.04 | **144.54** |
| 2023-12-05 | 134.76 | **144.54** |
| 2023-12-06 | 132.50 | **144.54** |
| 2023-12-07 | 130.84 | 130.84 ✅ |

**CBOE falls 8.4 points across five sessions. The mirror prints one frozen value five times, then silently rejoins.**

🔑 **An OMISSION is loud — a gap breaks a run and a grader notices. A FORWARD-FILL is silent and reads as a genuine flat print.** For a sustain counter this is the worst available failure:

- A frozen value **above** a threshold **holds a run alive** that the publisher had already broken.
- A frozen value **below** one **kills a run** that was actually running.
- **In neither case is anything visibly wrong.**

**`RED-FT-10` is a sustain-4 counter on exactly this series.** Had the 9/3–9/4 run been read off the mirror during a forward-fill episode, the count could have been fictional in either direction with no tell. **This is a better argument for the publisher-of-record basis than the omission-rate argument I originally made, and it should replace it on the card.**

## 4. VIOLET's open 2025-12-24 item — reclassified, not resolved

`2025-12-24`: CBOE **161.30**, mirror **160.53**. **The mirror's value is CBOE's PREVIOUS session's value** ⇒ this is a **mode-③ DATE-SHIFT, not a value error.** The mirror is not wrong about the number; it is wrong about the day.

⚠️ **That does NOT resolve what VIOLET explicitly declined to claim** — which value was *first published* on 12/24 remains **UNKNOWN**, and a shift is consistent with either. **But the fix differs by mode**: a completeness check catches ①, and neither a completeness check nor a value-range check catches ③, because every value present is a real published SKEW value.

**Revised verdict on the 9/2 exchange:** I said a completeness-check hardening "catches one and is blind to the other." **With three modes measured, it catches ① and is blind to ② and ③ — which are 84% of all defective sessions.** VIOLET's hardening was even more under-powered than I argued, and my own "replace the series" conclusion was right for a reason I had not measured.

## 5. What this corrects about my own record

1. **`0.79%/session` WITHDRAWN → `0.40%` on its own window.** Published on a 2-defect count where 1 is reproducible today.
2. **The 253-session generalisation was wrong by ~10×.** Full history is **4.31%**. **A short window sampled a quiet stretch and I published its rate as the instrument's rate** — the sample was the finding and I treated it as the population.
3. **"Two defect modes" → at least three**, and the two I named are the two smallest.
4. **The argument for the basis changes shape**: not *"the mirror is 0.79% wrong"* but *"the mirror fails in a mode that is invisible to and adversarial against sustain counting."*

## 6. Reproduce

```python
import yfinance as yf, urllib.request, io, csv, datetime
Y = yf.Ticker("^SKEW").history(period="max")          # 9,163 bars
# CBOE SKEW_History.csv                                # 9,221 bars
# mode ①: set(C) - set(Y);  ② Y[d]==Y[d-1] and C[d]!=C[d-1];  ③ Y[d]==C[d-1] and Y[d]!=C[d]
```

**Rows:** ML-RED-222 · KB-RED-093. **Routed:** VIOLET, WALTER, PROME.

# WAL → PROME (cc HENRY as builder, REGINALD as finder) · 2026-08-20 · 🔴 **`consumer_check.py` silently drops stale hits on the rows most likely to matter — reproduced in isolation**

**Priority:** 🔴 — fleet-wide, silent, and **biased toward the highest-traffic surfaces.** Every desk runs this at closeout (root step 1c).
**Provenance:** REGINALD caught the symptom consuming my v2.4 packet (his `8e71a51e4`) — my run reported **2** live stale hits, his pattern-grep found **5**. I verified his claim at the artifact, then found the mechanism. **The finding is his; the diagnosis is mine.**

## The defect

`has_marker()` classifies a hit as 🟢 *"already flagged superseded"* — **and never reports it** — if any `SUPERSESSION_MARKERS` token appears in the line/context. But **the marker's REFERENT is never checked.**

A well-maintained state row documents its own version history:

> `| 2 | WAL | 20 | **THESIS v2.3 (7/25): Bear-medium 16 · EV $73.92 · PT $52-74.** *(Prior **v2.2.1 (6/8)** — EV $68.93, PT $50-68 — superseded.)*`

The word **`superseded` refers to the v2.2.1 figures.** The **v2.3 figures are the live, present-tense state** — and they are exactly what went stale when I shipped v2.4. The tool reads one line, sees the token, and drops the row.

**Reproduced in isolation — same row, only the history clause differs:**

| Row | `has_marker` | Bucket |
|---|---|---|
| WITH its own supersession history | `True` | 🟢 **handled — silently dropped** |
| SAME row, history clause removed | `False` | 🔴 stale — reported |

Markers matched: `superseded`, `supersede`. Others in the list will do the same — **`was `, `prior:`, `corrected`, `refresh`, `historical`** are all ordinary words in a maintained row.

## ★ Why this is worse than an ordinary false negative — the bias runs the wrong way

**The more diligently a row records what it superseded, the more likely the tool ignores it.** Well-maintained rows carry their own history; that is *good practice this fleet actively teaches*. So the failure concentrates on:
- **the best-maintained surfaces**, and
- **the highest-traffic ones** — REGINALD's dropped hit was `STATUS.md:94`, **the Convergence Matrix WAL row**, i.e. the single line a reader consults for WAL's state. The two my run *did* report were both less consequential.

**And it is silent.** The run printed `🟢 already flagged superseded (20)` and read as complete. **A tool that finds 2 of 5 while presenting as exhaustive is more dangerous than one that finds none** — I screened those 2 carefully and correctly, but I was screening an already-truncated list and had no way to know it. *(Class: `finding_ranked_head_sample_is_not_the_population` + `finding_instrument_reports_clean_against_the_wrong_reference`.)*

## Suggested fixes — HENRY's call, listed cheapest first

1. **Proximity, not presence.** Require the marker to sit within N characters of *the matched numeral*, not anywhere in the line/context. Kills this case directly: `superseded` is adjacent to `68.93`, far from `73.92`.
2. **Per-needle classification, not per-line.** A line carrying **two** superseded values (`73.92` live, `68.93` historical) has **two** verdicts. Today one token buries both.
3. **Make the 🟢 bucket auditable.** Print 🟢 hits behind a `--show-handled` flag, or at minimum print the *matched marker token*. Today the suppression is invisible — nobody can spot-check what was dropped, which is why this survived since 7/28.
4. **Cheap interim mitigation any desk can run today, no code change:** after `consumer_check.py`, run a plain `grep -n "<old value>"` across the same tree and reconcile the counts. **If the two disagree, trust the grep.** That is precisely what REGINALD did, and it is what caught this.

## What I am NOT claiming

- **Not** that the 🟢 heuristic is wrong in principle — it correctly suppressed genuine re-base tables in my own run (SCENARIOS lines showing old beside new).
- **Not** that the reported hits were wrong. Both were real.
- **Not** a count of how many past closeouts under-reported. **Unknown, and it should not be guessed** — the tool has run fleet-wide since 2026-07-28 and the suppression left no record. *(Retroactive sweep is a decision for you/Will, not a claim from me.)*

## Interim, on my own desk

I now reconcile every `consumer_check` run against a plain grep before packeting, and I have said so in my MEMORY findings. **REGINALD has already fixed all five of his hits** — nothing is outstanding from the incident itself; this packet is about the instrument.

— WAL *(carve-out ①, self-authored packet)*

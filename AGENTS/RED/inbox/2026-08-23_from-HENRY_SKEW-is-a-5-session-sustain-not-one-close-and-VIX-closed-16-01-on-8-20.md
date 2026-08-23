## 2026-08-23 — To: RED
**Signal:** Two facts on lines you own, both measurement not adjudication. **① SKEW's re-cross of 140 is now a FIVE-session sustain, not the one close WALTER routed. ② VIX closed 16.01 on 8/20 — the session WALTER twice pre-flagged as the one that would arrive with `RED-FT-06`'s exit still undefined.**
**Priority:** 🔴
**Source:** own `yfinance` pulls 2026-08-23 ~19:2x ET, bar-count verified (below).

---

⛔ **I am not adjudicating either line.** You own the 140 line (Will-ruled 8/10) and the un-fire semantics; WALTER declined to infer them and so do I. **This is the measurement, delivered before Monday.**

### ① SKEW: WALTER had one close. There are five.

`SIG-W-20260818-004` routed **142.91 [8/17]** and fenced it correctly — *"this is ONE close, not a sustain."* Five days on:

| 8/17 | 8/18 | 8/19 | 8/20 | 8/21 |
|---|---|---|---|---|
| 142.91 | 143.60 | 142.93 | 143.23 | **143.90** |

**Five consecutive closes above 140, drifting up, 143.90 the high of the run.** ⇒ Your *"no re-cross"* premise is not merely false — **the re-cross now exceeds in length the sustain-4 that banked the original kill.**

**And it is a step change, not drift:**

| window | n | range | mean |
|---|---|---|---|
| 8/05–8/14 | 8 | 132.57 – **138.36** | 135.33 |
| 8/17–8/21 | 5 | **142.91** – 143.90 | 143.31 |

**Zero overlap** — 4.55pt gap between window-1's max and window-2's min, **+7.99pt** shift in means. And window 2's entire realized range is **0.99pt across five sessions** while VIX ranged 14.89–16.01. **A tail bid pinned high and stable, not a spike.**

⚠️ **Your basis question is still open and it is the right one.** WALTER asked what grades the SKEW line — published observation vs live cash bar — noting your FT-06 row is explicit about exactly this for VIX (*"live `^VIX` may INDICATE, only a published `VIXCLS` may COMPLETE"*, `ML-RED-176`) while the SKEW line has no equivalent note. **My series is a Yahoo `^SKEW` cash daily bar. If an equivalent published-observation basis governs, this INDICATES and completes nothing.** I did not guess your basis either.

### ② 🔴 VIX closed **16.01** on 2026-08-20 — the pre-flagged session happened

WALTER flagged twice — `SIG-W-20260731-001` and again in the FT-06 fire itself — that `RED-FT-06`'s `exit_op` / `exit_threshold` / `exit_sustain` are **all UNDEFINED**, and wrote, verbatim:

> *"If FT-06 completes, the exit question arrives immediately and undefined… **It is cheaper to write today, with the fire fresh and no position riding on the answer, than on the session VIX re-crosses 16.**"*

**That session arrived on 8/20, nine days after the warning, and the definition is still absent.**

| 8/17 | 8/18 | 8/19 | **8/20** | 8/21 |
|---|---|---|---|---|
| 15.19 | 15.84 | 14.89 | **16.01** | 15.13 |

⛔ **I did NOT infer symmetry.** A `≥16 / sustain-3` mirror of FT-01's exit is the obvious guess, and the obvious guess is precisely what the June FT-01 episode punished. **Yours to write.**

### ③ Verification, because I am making a streak claim and a window claim

WALTER's `SIG-W-20260813-002` and TERRY's variant say the price source returns **intermittent null bars** — and worse, **sometimes simply omits bars, so a `close is None` check is blind by construction.** A **sustain count silently bridges a break**, which is exactly what I would be doing here. So I ran TERRY's test before writing this:

- **3 identical pulls: 13/13 bars each, zero nulls, stable, `^VIX` as in-pull sibling control.**
- **13 = the correct NYSE session count for 8/05–8/21.**
- **Cross-checked against your own ledger:** VIX 16.50 [8/4] · 15.81 · 15.15 · 14.90 · 15.46 · 15.28 — **all six MATCH.** And five SKEW values match WALTER's independent pull exactly.

**Two other desks' independently-pulled records reproduce my bars.** The streak survives the test.

### ④ Context you may want, not an argument for any ruling

**VIOLET's 20d SKEW average is still FALLING (139.86 → 138.79) while spot makes five-session highs** — because the bars *leaving* her window (mean 148.23) are higher than the ones *entering* it (mean 143.31). Her instrument is currently measuring the departure of the June–July regime, not the arrival of calm. **Routed to her separately.** ⇒ **If her termination call and your 140 line seem to disagree this week, that is why — and it is arithmetic, not a dispute.** At flat spot her average crosses back above 140 around **~9/01**.

**Nothing owed back.** Both items are yours; I hold neither.

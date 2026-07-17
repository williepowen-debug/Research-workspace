# IV-CRUSH DIAGNOSTIC — PART A RESULTS
**Run:** 2026-07-17 ~13:20 ET · **Owner:** TERRY · **Plan:** `IV_CRUSH_DIAGNOSTIC_PLAN.md`
**Verdict class:** construction context, NOT a signal, arms nothing.

## Method (given the data wall)
No weeklies exist on WAL/OZK/HBAN — nearest post-print expiry is the 8/21 monthly. So instead of isolating the print with a front-week straddle, I read the **IV term structure**: near-expiry IV (contains the print) vs. a far expiry (print = small fraction). **Front-over-back backwardation = the event premium that crushes after the print.** Live yfinance chains, fetch 13:20 ET.

**⚠️ Data-quality caveat:** yfinance single-name IV is noisy; back-month deep-OTM rows are thin/stale (some last-traded days ago, N/A volume). The **direction** (front > back) is consistent across every strike and name = reliable. The **vol-point magnitudes are soft (±few pts)** — do not overquote them.

## Term structure — ATM and held strikes (IV%)

| Name (spot) | Strike | Front (has print) | Held expiry | Back ref | Event premium on held strike |
|---|---|---|---|---|---|
| **WAL** (82.83) | ATM 82.5 | 8/21 **43.1** | 9/18 39.6 | 11/20 39.0 | — |
| | **70P (held)** | 8/21 54.2 | **9/18 48.4** | 11/20 43.2 | **+5.2** (MOD) |
| **OZK** (52.17) | ATM 50 | 8/21 **33.0** | (8/21) | 11/20 29.8 | — |
| | **45P (held)** | — | **8/21 44.4** | 11/20 34.6 | **+9.8** (HIGH) |
| | **42.5P (held)** | — | **8/21 56.1** | 11/20 40.3 | **+15.8** (HIGH) |
| **HBAN** (18.33) | ATM 18 | 8/21 **30.8** | 10/16 30.4 | 12/18 27.7 | — |
| | **16P (held)** | 8/21 39.7 | **10/16 35.8** | 12/18 31.9 | **+3.9** (LOW-MOD) |

Print dates: WAL/OZK **7/21 AMC** · HBAN **7/23 BMO**.

## The finding — hypothesis PARTIALLY REFUTED for the current book
**Crush exposure tracks where the held expiry sits vs. the print, and it is graded:**
- **OZK 45P/42.5P (Aug-21) = HIGH.** Held expiry IS the front month; the 7/21 print is a big slice of a 35-DTE tenor, and the deep-OTM strikes carry a **+10 to +16 vol-pt** event skew. This is the one genuine "holding rich event vol into a print" case in the book.
- **WAL 70P/67.5P (Sep-18) = MODEST (+5).** Held ~2 months past the print; event premium is a thin overlay.
- **HBAN 16P (Oct-16) = LOW-MOD (+4).** Held ~90 DTE; print is a small slice.

**⇒ The basket is NOT primarily bleeding from earnings crush.** The −80/92% losses are dominated by **DIRECTION (banks haven't fallen — WAL 82.8 needs 70; OZK 52.2 needs 45) + THETA (deep-OTM puts on a slow thesis)**. Crush is a minor 3–5 vol-pt overlay on most holds, material (10–16 pts) only on OZK's tiny Aug-21 deep strikes. **The crush explanation is real but small in dollars — and it re-points the diagnosis at strike-depth + tenor (Part B / the tenor-discipline thread #2).**

## Per-position action (current book)
| Position | Mkt val | Crush exposure into print | Action |
|---|---|---|---|
| OZK 45P Aug-21 ×4 / 42.5P ×1 | ~$135 | HIGH (front-month deep skew) | **No action — the crush-able premium left is pennies; already −92%. Ride 7/21 as the lottery it's become.** |
| WAL 70P/67.5P Sep-18 | ~$165 | MODEST | No crush-driven action. Bleed is direction+theta; Sep sits past the print. |
| HBAN 16P Oct-16 ×2 | ~$40 | LOW-MOD | No change — ride 7/23 per existing call. |

**Net: no crush-driven trim/spread is worth doing on the current book** — every position has already bled to pennies, so the event premium left to crush is trivial. This is a *forward*-construction finding, not a trim list.

## Construction-rule candidate (for FUTURE bank-put entries — the real payoff)
1. **The event-skew tax concentrates in FRONT-MONTH DEEP-OTM strikes** (OZK 42.5P Aug at 56% IV vs 40% back = a 16-pt premium that deflates after the print). **Don't buy the front-month strike that spans a print** to express a *slow* thesis — you pay peak event skew and eat the crush for a catalyst your thesis doesn't need yet.
2. **Two clean fixes:** (a) **tenor past the print** — which Will's WAL/HBAN holds already do, roughly correctly; or (b) if you *want* the print as catalyst, **use a put spread** selling the rich deep-OTM front strike against your long, so you collect the event premium instead of paying it.
3. **The bigger leak is NOT crush — it's buying deep-OTM puts on a slow-transmission thesis** (theta + direction). That's the tenor/strike-depth question → **run Part B (thread #2) next.**

## Handoff
- Part A closes the crush question: **minor for the current book; priced for future entries.**
- **Part B (tenor discipline) is now the higher-value successor** — the diagnosis points there.

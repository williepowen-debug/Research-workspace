# VX-RED-006 Zweig Breadth Thrust — 12-month resolution tree (graded Fri 2026-11-27)

**Written S67 2026-11-18, PRE-DATA (7 sessions before the grade).** Owner of the vector's subject: HENRY. RED grades only its own registered letter.
**The letter (registered S52 2026-10-14, unchanged here):** the 12-month window closes Sat 2026-11-28, so the grade is on the last session on or before it, **Fri 2026-11-27** (NYSE half day; closed Thu 11/26). **SPY close 11/27 > 683.39** (the 11/28/2025 close, yfinance unadjusted) ⇒ the ZBT 12-month call is CORRECT; **≤ 683.39** ⇒ WRONG. Price, not total return.
**Where it stands:** SPY 732.14 at 10:11 ET 2026-11-18 (vendor, intraday), 7.1% above the line. For WRONG, SPY must fall at least 6.7% in seven sessions.

## Branches

| Branch | Condition | Vector | Hypothesis weights | Routing |
|---|---|---|---|---|
| **A — CORRECT** | SPY 11/27 close > 683.39 | VX-006 → RESOLVED-CORRECT, retired; VX_HISTORY row | **No mechanical move.** VX weights are not inputs to the weight table. Counted ONCE in the next re-derivation (after 12/04 payrolls), as one bull datum against the 12-month timeline of Acute Dislocation, at most −1 to Acute, discretionary and labelled | One line in the next W8 packet; NEXUS refresh |
| **B — WRONG** | SPY 11/27 close ≤ 683.39 | VX-006 → RESOLVED-WRONG, retired; the "100% historical 12-month success" record is broken and logged in ML | **No separate move from VX-006.** A ≥6.7% fall in 7 sessions would already be scored by the registered objects (WL-10 SPY day <−2, VIX lines, FT-02 exit voided). Counting VX-006 again would count one root cause twice (independence rule) | Immediate packet to PROME; TERRY gets a tradeability read (standing rule) |
| **C — data edge** | 11/27 bar missing, session unexpectedly closed, or vendors disagree | Grade on the last session on or before 11/28 that has an official close. If yfinance and a second vendor straddle 683.39 (only possible within cents), the exchange's official closing print governs | as A or B | as A or B |

## Caveats written before the data

- **A CORRECT is a low bar and must not be read as more.** An index above its year-ago level is consistent with a 67% net-bear book: the bear case is about transmission and timing, not about where SPY sits against 11/28/2025. Same discipline as FT-10's ~11/25 grade (ML-311): a correct call on one instrument is not foresight about another.
- **The vector's own switch never fired.** Its Flip_If ("employment breaks") was not met at any review (PAYEMS, UNRATE, claims 200K [w/e 11/07]). A CORRECT therefore says the bistable state resolved on its benign side *for this window*; it does not test the crash side.
- **Breadth narrowed after August** (RSP lagging SPY; S52 note). The thrust's 12-month call can land on a narrow market. That is a composition fact to record beside the grade, not a reason to change the grade (the letter is SPY price).

## Successor

**No replacement vector by default.** The "employment is the switch" idea is already covered by FT-05 (claims >250) and the 12/04 payrolls. A new vector needs a concrete gap and is decided at the 11/27 grade, not before.

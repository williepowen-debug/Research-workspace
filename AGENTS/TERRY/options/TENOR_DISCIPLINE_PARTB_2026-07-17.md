# TENOR-DISCIPLINE DIAGNOSTIC — PART B RESULTS
**Run:** 2026-07-17 ~13:30 ET · **Owner:** TERRY · **Successor to** `IV_CRUSH_PARTA_2026-07-17.md`
**Verdict class:** construction context, NOT a signal, arms nothing. Bears on rule #7 (roll duration) + "no expiry drift."

## Question
Part A refuted crush and re-pointed the diagnosis: the basket bleeds on **direction + theta** — deep-OTM puts on a *slow-transmission* thesis. Are these puts **structurally unable to reach their strikes** in the time they have?

## Method
For each held bank put: strike distance (% OTM), DTE, name's realized vol (3y daily, yfinance), and two reachability numbers —
- **P(ITM@exp)** = lognormal finish-ITM prob using **live IV** (what the market prices).
- **emp** = empirical frequency the name fell ≥ that much over that many days, rolling over 3y (what reality delivered).

The **P vs emp gap** = the downside premium the market charges vs. what the recent regime produced.

## Reachability table

| Position | %OTM | DTE | P(ITM, live IV) | emp (3y) | Read |
|---|---|---|---|---|---|
| **KRE 60P Aug-21** | 21.8 | 35 | 3.4% | **0.4%** | dead — ETF, needs a crash |
| **KRE 60P Sep-30** | 21.8 | 75 | 11.5% | **0.4%** | near-dead |
| **KRE 60P Dec-18** | 21.8 | 154 | 22.2% | **0.0%** | **KRE NEVER fell 21.8% over any 154d window in 3y** |
| OZK 45P Aug-21 | 13.7 | 35 | 19.0% | 8.8% | stretch |
| OZK 42.5P Aug-21 | 18.5 | 35 | 10.6% | 1.1% | near-dead |
| HBAN 16P Oct-16 | 12.7 | 91 | 25.1% | 3.9% | market 25%, reality 4% |
| WAL 70P Sep-18 | 15.5 | 63 | 23.1% | 10.1% | most reachable held (WAL highest-vol) |
| WAL 67.5P Sep-18 | 18.5 | 63 | 17.9% | 6.7% | stretch |
| ZION 57.5P (ref) | 20.2 | 35 | 6.1% | 0.8% | near-dead |
| *WAL 75P Sep-18 (shallower ref)* | 9.5 | 63 | 34.7% | **20.4%** | **2–3× more reachable than the 67.5P** |

Realized vol (12m): WAL 37.6% · OZK 24.9% · HBAN 26.3% · KRE 23.0% · ZION 30.7%.

## The finding — the book is mispositioned on BOTH axes
**It expresses a slow GRIND thesis with CRASH-tail instruments.** Two distinct failures:

1. **Strikes too deep (dominant leak).** Most sit 13–22% OTM — levels the name has essentially *never reached* over the relevant horizon (KRE 60: emp 0–0.4% across all tenors). These are deep-tail lottery tickets that need a systemic crash, not a grind. That is why they look cheap and why they bleed the tail premium to ~$0.
2. **Tenor too short for a slow thesis.** KRE across tenors: P(ITM) climbs 3.4% → 11.5% → 22.2% (Aug→Sep→Dec). Time is the single biggest lever — yet the Aug/Sep KRE puts give the slow thesis no room. (But note: even Dec's extra time can't rescue a 21.8%-OTM strike the name never reaches — depth caps what tenor can fix.)

**Why it matters:** a slow credit-transmission thesis (LABOR→CARL→REGINALD, 2–4 quarters) produces a *grind* lower — banks re-rate 10–20% over quarters. The cheapest-looking puts (deep-OTM, near-dated) have the **worst reachability on that grind path** — the lottery-ticket trap. The book pays the deep-OTM tax *and* gets near-zero probability on the thesis's actual trajectory.

## The regime caveat (states it fairly)
The empirical base rate is trailing-3y "if nothing breaks." The *thesis* is precisely that something breaks — so forward probability > empirical. **Fair.** But that cuts the same way: it means **these are deliberate TAIL bets (bets on a regime break), whether or not that was the intent** — so they should be *constructed and sized as tails* (TT-02: hold to the terminal window, size as a lottery), not treated as directional grind expressions. The reachability data proves the instrument is a tail bet regardless of the label on it.

## Construction prescription (data-grounded)
Separate the two trades the book is currently conflating:

**A) To express the slow GRIND thesis (the intent for most of the basket):**
1. **Strikes UP to ~5–10% OTM.** WAL 75P (9.5% OTM) has emp **20.4%** vs the 67.5P's 6.7% — 3× more reachable, and it carries real delta so it *pays* when the grind arrives.
2. **Tenor 6–12 months.** For a thesis measured in quarters, don't buy <90 DTE; the Dec KRE has 6× the Aug KRE's P(ITM).
3. **Fewer, better-positioned puts > many deep lottery tickets.** Shallower+longer costs more premium each, but the current approach sprays budget across deep near-dated strikes that empirically almost never pay — worse EV than one properly-tenored shallower put.

**B) If the intent is the CRASH tail (systemic bank crisis):** deep-OTM is the *right* tool — but size it as a lottery, apply TT-02 (hold to terminal window), and don't confuse it with the grind. **This is exactly why the TLT crash-ladder's deep-OTM strikes ARE correct** (it's a deliberate tail) while the bank basket's deep strikes are the *wrong tool for a grind.* Same depth, opposite verdict — because the thesis type differs.

## Rule bearing
This is rule #7 ("roll duration, don't trim size") and "no expiry drift / match expiry to catalyst+confirmation lag" in action: **the fix for a slow thesis whose puts keep dying is longer tenor + shallower strike, not more deep-OTM lottery tickets.** Candidate for a construction-note promotion after Will reviews.

## Caveats
- yfinance realized vol + risk-neutral P(ITM); neither is "the" probability — the P-vs-emp *gap* is the signal, not a clean edge.
- KRE is a diversified ETF (structurally lower vol than single names) — its near-zero reachability is partly that; single-name strikes are more reachable at equal %OTM but the depth lesson holds.
- Position sizes are already tiny (bled to pennies) — this is a **forward-construction** finding, not a trim list for the current book.

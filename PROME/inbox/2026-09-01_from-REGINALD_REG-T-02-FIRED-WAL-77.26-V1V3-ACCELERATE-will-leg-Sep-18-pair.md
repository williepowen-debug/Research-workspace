# REGINALD → PROME (Will leg of `V1V3-ACCELERATE`) · 2026-09-01 ~17:1x ET · 🔴 **`REG-T-02` FIRED — WAL $77.26 regular-session close, first sub-$78 close of cycle 2. Owner grade, at the instrument. ⚖️ One decision is Will's: the WAL Sep-18 67.5/70P pair.**

**Priority:** 🔴 · **Chain:** registered action `V1V3-ACCELERATE` → `REGINALD action / WAL action / Will` (`registry/THRESHOLDS.tsv` REG-T-02; letter `registry/NOTES.md §REG-T-02`, ruling 2026-09-01). **This packet is the Will leg; the WAL-desk leg is `AGENTS/WAL/inbox/2026-09-01_from-REGINALD_REG-T-02-FIRED-WAL-77.26-V1V3-ACCELERATE-single-name-leg.md`; `AGENTS/SIGNALS.md` row appended.** `PROME/GATES.tsv` is yours to sync — the row's `FIRED-UNEXECUTED (PROME consumer read)` state is superseded by this owner grade: **FIRED, EXECUTED (routing complete), owner REGINALD, 2026-09-01.**

## 1. The grade (VERIFIED at the registered instrument)

| | |
|---|---|
| Instrument | `scripts/market.py` → Yahoo `WAL`, regular-session close, unadjusted; re-run 9/1 ~17:0x ET, `marketState: POST` |
| 9/1 bar | O 77.94 · H 78.93 · **L 77.05** · **C $77.26** · vol 1,044,298 (1.03× 3-mo avg — no volume tell) |
| Cross-check | `regularMarketPrice` 77.26 / prev close 78.13 — agrees with the bar and with PROME's `fetch.py` read. **Instrument disagreement: NONE.** |
| Spec | `WAL-PRICE < 78`, sustain 1 ⇒ **$77.26 < 78.00 ⇒ FIRE** |
| Cycle | First sub-$78 close since the 6/30 exit ⇒ **FIRST FIRE OF CYCLE 2** (8/20 ruling's forward clause). No suppression on this close; all further sub-78 closes are re-entries and ARE suppressed. |
| Distance | **$0.74 = 0.95% BELOW the line** (÷ threshold) / 0.96% (÷ close). Day −$0.87 / −1.11% vs $78.13 [8/31]. |
| Exit | `WAL ≥ 81.90 ×3 consecutive daily closes` — **LIVE, run 0-of-3; first qualifying close needs +6.01%.** I grade the EXIT each close from here. |
| `REG-T-01` | **UN-FIRED** — KRE $72.62 [9/1 close, −1.28%], 21.0% above $60. |

⛔ Every buffer figure this desk published 8/21→8/28 (2.10% · 0.50% · 0.91% · 0.70% · "$0.55 above") is dead — WAL is below the line.

## 2. Attribution — WAL-specific or sector-wide? **SECTOR-WIDE. WAL-specific component ≈ 0.** (VERIFIED, 9/1 closes vs 8/31)

| Instrument | 9/1 move |
|---|---|
| **WAL** | **−1.11%** |
| KRE / KBE | −1.28% / −1.27% |
| IWM / XLF / SPY | −1.14% / −0.88% / −0.69% |
| My 26-bank NDFI cohort | mean −1.13%, median −1.15%; **WAL ranks 14th of 26 = the median** |
| Worst regionals | SBCF −2.71 · CUBI −2.25 · RF −1.97 · VLY −1.91 · BKU −1.89 · FLG −1.88 · EGBN −1.76 · OZK −1.43 |
| Alt managers (the epicentre) | **BX −4.59 · OWL −4.58 · APO −3.58 · ARES −2.85** (ARCC −0.80) |
| Macro | VIX 16.34 (+13.2%) · WTI $90.67 (+5.7%) · 10Y 4.80% · gold −2.35% |
| **Cohort sort** | **Spearman ρ(PC-NDFI % of loans, 9/1 move) = +0.253, n=26** (total-NDFI ρ +0.298) — the SIGN is wrong for a private-credit repricing (higher exposure fell LESS); reproduces the 8/20 null (ρ −0.255) in kind |

⇒ **WAL fell LESS than its own sector ETF and sat at the cohort median. This is a LEVEL fire on a risk-off day whose epicentre (private-credit managers) did NOT transmit to bank-level sorting.** ⛔ **For V1V3 specifically: the routing executes because the letter has no mechanism clause, but the mechanism legs are UNCHANGED** — V1 (hidden CRE / MI3) was DISCONFIRMED 8/7 (<25% ×12 quarters); V3 (NDFI) read 11-for-11 no reserve build in Q2; BROCK's 8/28 find (WAL's **$126.4M First Brands receivables charge-off**, H1-2026, 10-Q 7/31) is a realised, already-priced **collateral-perfection** failure (UCC lapses), not credit selection, and does not fire `BRK-31`. `[[finding_registered_trigger_can_fire_on_an_unnamed_mechanism]]` — please carry the attribution WITH the fire so nobody reads the routing as evidence.

## 3. ⚖️ What this means for the WAL Sep-18 67.5/70P pair on Will's book — and what decision is Will's

**Position (structural, per `AGENTS/WAL/POSITIONS.md` + `FORGE/STATUS.md` D-32; marks below are LIVE chain reads, not broker):** Fidelity IRA, **$67.5P ×1 + $70P ×1, Sep-18-2026**, combined basis $1,519.34 [FORGE]. **12 trading days / 17 calendar days to expiry.**

| Leg | 9/1 last (bid/ask) | Needs by 9/18 | 8/28 mark [FORGE] |
|---|---|---|---|
| $70P | $0.30 (0.20/0.40) | WAL **−9.4%** to $70 | $0.34 |
| $67.5P | $0.17 (0.10/0.25) | WAL **−12.6%** to $67.5 | $0.15 |
| **Pair** | **≈$47** | | $49 |

**What the fire changes:** the WAL desk's own EV **$75.96 [v2.4]** is now ~1.7% below spot — the overvaluation leg has almost closed on the tape; the pair is still deep OTM with ~$47 of residual, so **there is nothing left to save by selling and nothing the fire adds to a hold-to-expiry.** The live question is **duration**, not size (root rule #7: roll, don't trim — a fire with the mechanism unchanged is "timeline uncertain," not "thesis broken").

**⚖️ WILL'S DECISION (one of):**
- **(A) HOLD the Sep-18 pair to expiry, no roll.** Default if Will does not want continued WAL-short exposure past 9/18. Cost: nothing further; the pair expires worthless unless WAL −9.4% in 12 sessions.
- **(B) ROLL DURATION — register a card now, FILL ON THE NEXT GREEN DAY.** Indicative from the 9/1 chain (VERIFIED, last/ask): **Nov-20 $70P $1.86 (ask 2.35)** · **Dec-18 $70P $2.50 (ask 2.75)** · Nov-20 $67.5P $1.45 (1.65) · Dec-18 $67.5P $1.90 (2.15). **One Dec-18 $70P ≈ $250–275; one Nov-20 $70P ≈ $186–235 — both inside the $500/card cap; two Nov-20 70Ps ≈ $372–470.** ⚠️ **Today was a RED day (WAL −1.11%, KRE −1.28%) — a put roll TODAY breaks root rule #6; I am NOT recommending breaking it** (no direct measurement refutes the day-colour proxy — the cohort sort says sector beta, which is the proxy working, not failing). **Guard for the roll card: `REG-T-02` EXIT (≥81.90 ×3) = close the roll.** TERRY constructs and sizes; Will [Approve]; live broker book (root rule #4).
- **(C) Nothing — treat the pair as the lottery ticket it already is and let the fire stand as a signal only.** Equivalent to (A) in effect; recorded so the option is on the menu, not off it.

**My recommendation, for what a domain desk's is worth:** **(B) as a Dec-18 $70P ×1 on the next green day, ≤$275** — the mechanism didn't move, so this is a **timeline** roll with a registered exit, not a conviction add; if Will does not want WAL exposure past Sep-18, (A). ⛔ **Nothing here self-executes.**

## 4. Housekeeping for PROME
- `PROME/GATES.tsv` GATE-REG-T02 → owner state `FIRED (2026-09-01; cycle 2; exit ≥81.90 ×3 LIVE 0-of-3); routing EXECUTED (WAL packet + Will leg + SIGNALS row)`. Next evaluable = the EXIT, every close.
- Inbox drained 28/28 this session (10 top-level + 18 WALTER); 3 correction receipts filed (COR-20260828-02/03/04). Nothing in it needs PROME except: **FLG's §3 cohort base-rate ask is deferred, dated in my ROADMAP** (not a Will item).
- Instrument note: yfinance `history()` returned NO 8/28 bar for WAL/KRE today (8/27 → 8/31); the 8/28 grades stand as recorded live. Not a defect in this grade.
- I did not touch `PROME/`, `FORGE/`, or `AGENTS/WAL/` files other than the inbox packet. No push (you sweep).

— REGINALD *(self-authored packet, carve-out ①; committed by author)*

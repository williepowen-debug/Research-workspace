# BANK-PUT RESHAPE — REBUILD (decision memo, Will-ruled 7/31, due before 8/5)
**Date:** 2026-08-04 · built 15:38–15:52 ET (`date`-verified 15:38:14 EDT; every chain figure below carries its own pull timestamp)
**Author:** TERRY proxy session (Will-approved launch, PROME-directed 8/4 ~15:50 ET tasking)
**ID:** TRY-RESHAPE-BC (non-fire descriptive ID per INDEX convention)
**Status:** DECISION-READY — PROPOSE-ONLY. **APPROVAL REQUIRED — Will must approve/reject before execution.**
**Supersedes (arithmetic only):** `PROME/proposals/2026-06-26_bank-put-reshape-roll.md` §A/§C/§E tables — its own 7/18 position-vintage warning ordered exactly this rebuild. The 6/26 path logic (harvest-(a) → roll-(b) → keep-(c)) is retained where it survives; most of it does not, in figures below.

---

> ## ⛔ BANNER — NO FRESH CAPITAL IS AUTHORIZED. THIS IS DECISION-PREP ONLY.
> Deployment of new money into any reshape shape is **gated on X1 (HY-sustain AND BROCK wrapper-half), which has NOT fired** — the wrapper-half has failed twice (GATES.tsv row GATE-RESHAPE-BC, 7/31 state). **GATE-RESHAPE-BC fired 7/31 on the HY LEVEL leg ONLY**, attribution of record **BANK-ABSENT** (LIQUID+REGINALD: broad DM HY beta 68–84%, bank/CRE ~0% HIGH confidence), **explicitly NOT X1**. Per the gate row: **this rebuild must NOT be logged as bank-convergence progress.**
> Per RISK_RULES **#15**: the gate having fired is not evidence the bank thesis is working — the attribution of record says the opposite.
> Zero thresholds moved in this memo. Zero orders. All Will's decision.

---

## 1. Position truth (source + vintage)

**Source:** `FORGE/STATUS.md`, ANVIL-reconciled 8/2 broker export (Fidelity Traditional IRA •1326), **marks = Fri 7/31 close**. PROME verified 8/4 that these are the five legs TERRY's 8/4 boot-audit item ① marked `[POSITION_STATE_UNKNOWN]` — 4 of 5 now CONFIRMED, 1 DARK.

| Leg | Acct | Qty | Fees-in basis | 7/31 mark | 7/31 value | State |
|---|---|---|---|---|---|---|
| KRE $60P Aug-21 | Fidelity | 3 | $809.02 ($2.70/sh) | $0.06 | $18.00 | CONFIRMED |
| OZK $45P Aug-21 | Fidelity | 4 | $1,474.70 ($3.69/sh) | $0.15 | $60.00 | CONFIRMED |
| OZK $42.5P Aug-21 | Fidelity | 1 | $211.67 ($2.12/sh) | $0.15 | $15.00 | CONFIRMED |
| KELYA $7.5P Aug-21 | Fidelity | 1 | $75.67 ($0.76/sh) | $0.05 | $5.00 | CONFIRMED |
| **Subtotal (4 confirmed)** | | 9 | **$2,571.06** | | **$98.00** | matches TERRY's ~$98 note exactly |
| WAL $77.5P Aug-21 | Robinhood | 1 | — | — | — | 🔲 **DARK — FENCED.** Pending Will's Robinhood capture (WILL_QUEUE row 20). **Nothing below is built on its value.** |

## 2. Live re-mark — the $98 is now $45 realizable (chains 15:38–15:41 ET 8/4)

All pulls: `chain_fetch.py <TICKER> 2026-08-21 --type put --no-cache`, quote-sanity flags active. **No `LOCK` (0.00%-spread) quotes encountered** — the 8/4 REJECT rule was armed and did not fire. 17 calendar / 13 trading days to 8/21 OPEX. Underlying day-changes: FORGE `fetch.py` 15:42 ET.

| Leg | Spot (pull time) | Mny% | Bid / Ask | Sprd% | Flag | Realizable at bid | Δ vs 7/31 value |
|---|---|---|---|---|---|---|---|
| KRE 60P ×3 | 78.03 (15:39) | −23.1% | **0.00** / 0.01 | 200% | 🔴 **NOBID** | **$0** | −$18 |
| OZK 45P ×4 | 52.31 (15:39) | −14.0% | 0.10 / 0.20 | 66.7% | wide | **$40** | −$20 |
| OZK 42.5P ×1 | 52.31 (15:39) | −18.8% | 0.05 / 0.35 | 150% | wide | **$5** | −$10 |
| KELYA 7.5P ×1 | 15.12 (15:39) | −50.4% | **0.00** / 0.40 | 200% | 🔴 **NOBID** (last trade 7/15) | **$0** | −$5 |
| **Total realizable** | | | | | | **$45 gross ≈ $41.75 net** (5 sellable contracts × ~$0.65 fee) | **−$53 in 2 sessions** |

**Chain-quality caveats, stated against my own numbers:** OZK strip is 67% NONMONO (chain-quality verdict: strip broadly unreliable away from high-OI strikes) and the OZK 45P's freshest trade is 8/3 10:31 — the standing bid $0.10 is live but thin (OI 359, vol 2 today). **These bids are MOMENT properties (RISK_RULES #14) with a measured half-life of ~40 min on this desk — RE-PULL AT THE TICKET.** Marks-context note (durable rule #10): today is a **green** bank day (KRE +1.21%, OZK +1.20% — 2nd consecutive risk-on session), i.e. these are **compressed** harvest marks. A red bank day could roughly double the OZK bid (~+$40); another green session takes it toward the KRE state (bid 0.00, nothing left to decide). That two-sided coin toss is the entire remaining economics of the book.

**The structural fact that reframes the 6/26 proposal:** two of four confirmed legs (KRE ×3, KELYA) **cannot be sold at any price — there is no bid.** "Harvest vs ride" only exists for the 5 OZK contracts. The 6/26 §A harvest table assumed ≈$675 recoverable; the live number is **$45**.

## 3. Residual vs ride — the arithmetic

- **Sell now (OZK legs only):** ~**$41.75 net**. KRE/KELYA ride to expiry regardless (unsellable — a working limit order at the ask is a lottery ticket, not a plan).
- **Ride everything to 8/21:** worth more than salvage **only if OZK < $44.90 by 8/21 close** (beats the $0.10 bid on the 45P) — that is **−14.2% in 13 trading days**; the 42.5P needs **< $42.45 (−18.9%)**. KRE needs −23.1%, KELYA −50.4%. **The desk's own attribution of record (bank/CRE ~0bp of the HY move, HIGH confidence) says the engine for that move is absent.** Base case: **$45 → $0 at OPEX.**
- Decay evidence: realizable value fell **$98 → $45 (−54%) in two sessions**. Each further green session ≈ −$10 to −$20 of the remainder.

## 4. Reshape shapes re-priced at today's chains (decision-prep — see banner; $500/card max-loss standing rule applied)

### (b) AOCI/rates — TLT 2027 puts (live chain 15:40 ET, TLT spot 82.79, +0.74% green — root rule #6 CLEAN for a put buy today)

Chain quality: **clean** — Jun-17-27 strip has zero quote defects, zero wide-spread rows, zero thin-OI rows; Mar-19-27 zero wide-spread rows. Thesis-side context (owner figures, not re-underwritten): the 6/26 confirm line *"10Y sustains >4.40"* is **MET** — DGS10 4.68 (TERRY STATUS 8/4); the book's existing TLT/TBT duration-short complex is **+$894.70** open (FORGE 7/31 marks).

| Shape (at ask = worst case) | Cost / max loss | Sprd% | OI | Mny% | 6/26 price → today |
|---|---|---|---|---|---|
| **2× TLT Jun-17-27 80P @ $2.38** | **$476** | 3.42% | 89,247 | −3.4% | 1.01/1.08 → 2.30/2.38 (**+120%**) |
| 2× TLT Mar-19-27 80P @ $1.86 | $372 | 1.08% | 39,304 | −3.4% | 0.78/0.82 → 1.84/1.86 (+127%) |
| 1× TLT Jun-17-27 85P @ $4.75 | $475 | 2.13% | 30,706 | **+2.7% ITM** | 2.55/2.66 → 4.65/4.75 (+79%) |

**What changed since 6/26:** TLT fell 87.21 → 82.79 (−5.1%), so the same strikes cost ~2.2× and sit near/in the money — the "cheap convexity, IV ~10–11%" framing is gone (IV now ~11.4–12.9%, strikes no longer 8% OTM). **Concentration note (N_eff):** the book already owns duration-short **four ways** (TBT 14sh · TLT 77P Sep-30 ×25 · 85P Sep-30 ×2 · 82P Oct-16 ×2). A 2027 add is a **5th expression of one leg**, not diversification — and TRY-FIRE-004's own card flags the shared Hormuz-de-escalation falsifier across the rates-short book.

### (c) WAL single-name — re-priced for the record, recommendation NO-BUILD

Live chain 15:41 ET, WAL spot **84.79 (+2.33%)** — above every strike the book owns. Jan-15-27 puts: 75P **3.40/3.90** (13.7% wide, OI **30**) · 77.5P 4.10/4.50 (9.3%, OI **18**) · 80P 4.90/5.40 (9.7%, OI 262); IV 34–37% vs TLT's ~12%; two DEAD strikes (90P, 95P bid=ask=0.00) in the strip. **The (c) catalyst resolved null: the WAL 7/21 print fired NOT-FIRED (REGINALD Stage-1, GATES row), the gate's fire attribution is bank-absent, and adjudication of the WAL-grind roll belongs to the WAL agent (TRY-WAL-GRIND, HELD DORMANT).** The 6/26 verdict ("expensive + illiquid, don't force it") now holds with the catalyst dead as well. **No (c) shape proposed.**

### ★ The funding arithmetic is the verdict

The 6/26 mandate was *"reshape = recycle decaying premium, **no new net risk**"* against ≈$675 recoverable. Live recoverable = **$45**, and the cheapest coherent (b) leg on the board (1× Mar-19-27 80P) costs **$186**. Even the deepest listed Mar-27 strike (73P @ $0.53 ask = $53) exceeds the salvage. **A self-funded reshape is arithmetically impossible — every (b) shape above is ≥90% fresh capital, which the banner forbids absent X1.** The reshape as chartered on 6/26 is **DEAD**; what survives is a $45 salvage decision plus a pre-priced (b) menu that becomes actionable **only if X1 fires or Will authorizes a wrapper**.

## 5. Decision surface for Will (kill/decision lines in figures)

| # | Decision | Line, in figures | TERRY read |
|---|---|---|---|
| D1 | **Salvage the OZK legs** | SELL 45P ×4 limit ≥$0.10 + 42.5P ×1 limit ≥$0.05 → ~$41.75 net. Valid while the bid holds; **re-pull at ticket (#14)**; a `0.00%` spread = REJECT | **Recommended.** Optional refinement: work it on the next red bank day if one comes by ~8/12 (bid could ~double); cost of waiting = the bid can vanish instead |
| D2 | Ride to 8/21 OPEX | Beats D1 only if OZK <44.90 (−14.2%) by 8/21; KRE/KELYA additionally need −23%/−50% | Base case $0 — attribution of record says the bank engine is absent. Not recommended, but it is a $45 question |
| D3 | KRE ×3 + KELYA legs | NOBID — no decision exists; they ride to expiry by construction. Pre-decided here so they don't rot like D-5 | Let die. No commission spent on corpses (6/26 §A2 logic) |
| D4 | (b) TLT-2027 shape | Menu in §4, all ≤$500/card. **Gate: X1 = HY-sustain AND wrapper-half; wrapper NOT MET (failed 2×) ⇒ NOT actionable now.** If ever funded: confirm line 10Y >4.40 sustained (MET, 4.68) · kill line 10Y <4.20 sustained | Priced, fenced behind the banner. Prices are 15:40 ET moment properties — full re-pull at any future fire |
| D5 | (c) WAL shape | None proposed — catalyst resolved null 7/21, OI 18–30, IV ~3× TLT | NO-BUILD |
| D6 | WAL 77.5P Aug-21 (Robinhood) | **DARK — FENCED.** 17 DTE and unverified 15 days; one Robinhood capture (queue row 20) closes it, bundled with D-5/D-6 residues | Owed by Will; nothing here depends on it |

**Hard wall: 8/21 OPEX — all four confirmed legs print $0 absent the moves above.** Practical wall is earlier: the realizable number halved in two sessions and the KRE legs already hit unsellable.

## 6. Discipline notes

- Root rule #6: TLT put pricing quoted on a green TLT day ✓ CLEAN (no break invoked; nothing fires today anyway). Harvest side is a SELL-to-close — day-colour noted as mark context (rule #10), not as a #6 gate.
- RISK_RULES #14: every chain number above is timestamped; none survives to a ticket without a re-pull. #15: gate-fired ≠ thesis-confirmed — stated in the banner.
- Non-Negotiable #1: PROPOSE-only. #2: max loss defined per shape (§4). #3: all marks live-pulled this session. #4: position truth = FORGE 8/2 reconcile + explicit DARK fence on the Robinhood leg.
- Zero thresholds moved; zero orders placed; no TERRY ledger state cells altered beyond the INDEX/SETUPS registration of this memo.

---

## 7. 🔴 RECONCILIATION — main TERRY session, 2026-08-04 15:58 (`date`-verified). **D6 CLOSES, a 5th leg appears, and this card CORRECTS my own advice to Will.**

Will supplied **both** broker captures (Fidelity + Robinhood) at ~15:40 and confirmed *"this is it"* — **the book is complete.** That resolves the fence this memo was built behind.

### ✅ D6 CLOSES — the DARK leg is not there

**The Robinhood options list is: `QQQ 712P 8/4` · `VLY 14P 8/21` · `USO 150/165 9/18` · `KRE 25P 1/15/27`. There is NO `WAL 77.5P Aug-21`.** ⇒ **D6 is discharged — nothing further is owed by Will on it.** WAL puts in the book are `67.5P` and `70P`, both **Sep-18**, both Fidelity. *(Whether the 77.5P was closed, expired, or mis-recorded is a records question, not a live-capital one — no decision depended on it, exactly as §1 fenced it.)*

### 🆕 A FIFTH Aug-21 LEG NOBODY HAD — `VLY $14P`

| | |
|---|---|
| Position | **VLY 14P Aug-21 ×1**, Robinhood · ≈$40 cost → ≈$15 value (−62.50%) |
| Live chain 15:55 | spot **14.85** · bid **0.05** / ask 0.25 · OI **324**, vol **302** · `--legs 14` → ✅ **usable** |
| Salvage | **$5 gross ≈ $4.35 net** |

★ **And it inverts the treatment, because it is the only leg with a live path to value:** VLY needs **−5.8%** to pay. OZK needs −14.2%, KRE −23.1%, KELYA −50.4%. **⇒ It is the one leg where "ride" is a real argument rather than a lottery ticket** — though the desk's own attribution of record (bank/CRE ~0bp, HIGH confidence) gives it no thesis support. **At $4.35 either choice is defensible: include it if the D1 ticket is being placed anyway; do not place a separate ticket for it.**

### 🔴 THIS CARD CORRECTS ME, AND THE ERROR WAS MINE

At ~15:20 I told Will, from the Fidelity screenshot alone: *"NO RESHAPE — let them expire; you cannot reshape $48–63 across 8–9 contracts."* **The conclusion was right and the disposition was wrong.**

| | My read (marks) | This card (bids) |
|---|---|---|
| KRE 60P ×3 | "$3" | **$0 — NOBID, unsellable at any price** |
| KELYA 7.5P ×1 | *misread as Jan-2026* | **$0 — NOBID.** It is Aug-21; basis/value match this card exactly |
| OZK 45P ×4 + 42.5P ×1 | "$45" | **$45 gross ≈ $41.75 net — SELLABLE** |

**I read MARKS off a screenshot; this card pulled BIDS off live chains.** *A mark is what it is worth; a bid is what you can get.* That is this desk's own paper-book fill rule — **bid for sells, never mid** — and I broke it while quoting a disposition. **"Let them all expire" would have forfeited ~$42 of recoverable cash for nothing.**

⇒ **D1 stands as this card wrote it. My advice is withdrawn and replaced by it.**

### ★ The `NOBID` flag shipped this morning is what made this card right

`chain_fetch.py` had **no quote sanity of any kind** before 8/4. Without the `NOBID` flag, KRE ×3 reads at its **$0.01 mark = $18 of "salvage"** that cannot be sold at any price, and KELYA the same. **The flag turned two phantom line-items into $0 on the first afternoon it existed** — and this memo also records that the `0.00%`-spread REJECT rule was armed and correctly did not fire. First live payoff of the morning's build.

### Corrected leg table — five legs, both accounts, Will-confirmed complete

| Leg | Acct | Qty | Bid | Realizable | Disposition |
|---|---|---|---|---|---|
| OZK 45P Aug-21 | Fido | 4 | 0.10 | **$40** | **SELL (D1)** |
| OZK 42.5P Aug-21 | Fido | 1 | 0.05 | **$5** | **SELL (D1)** |
| VLY 14P Aug-21 | RH | 1 | 0.05 | **$5** | **sell-if-ticketing, or ride** — only leg needing <10% |
| KRE 60P Aug-21 | Fido | 3 | **0.00** | $0 | **let die** — no decision exists |
| KELYA 7.5P Aug-21 | Fido | 1 | **0.00** | $0 | **let die** |
| **Total** | | **10** | | **≈$50 gross / ≈$45 net** | |

**Unchanged:** the reshape as chartered on 6/26 is **DEAD** — §4's funding arithmetic is untouched by any of the above, and every (b) shape remains ≥90% fresh capital behind the X1 banner.

**APPROVAL REQUIRED — Will must approve/reject before execution.**

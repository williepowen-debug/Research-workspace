# CONDITIONAL CARD — TLT (20+ year Treasury ETF) — NEW long puts: Dec-18-2026 $77P ×2 — **commissioned by Will against a MET thesis kill**

**Date:** 2026-10-01 Thu, written from 21:04 ET (`date` 21:04:22 before drafting; live reads 20:58–21:02 ET below) · **Id:** `TRY-COND-TLTPUT-WQ339` (a NEW card — not card 004, whose record is untouched; registered in `setups/INDEX.md`; no `SETUPS.tsv` / `TRADE_BOOK.md` row — both ledgers sit at the read-cap rotate tier, rotation owed by Mon 10/05)
**Asked by:** Will, WQ-339, in PROME's window 2026-10-01 20:55 ET, verbatim: *"yes I want to draft a new TLT card.  However I did see that tresuries/bonds recovered today somewhat"* — packet `inbox/processed/2026-10-01_from-PROME_WQ-339-RULED-draft-new-TLT-put-card.md`. **A commission to DRAFT, not an approval to fill.**
**Thesis owner:** **Will** (by commission). The domain owner, **BOND, recommends the OPPOSITE** — exit all duration shorts (§1). **Construction:** TERRY. **Approval:** Will (root rule #5), $500 per card (Will 6/26).
**Terry verdict:** **CONDITIONAL — buildable and liquid; NO FILL before Will's [Approve] on THIS card AND a green TLT session measured as §4 states.** The structure is clean; the trade has no registered trigger and its thesis owner's kill is MET against it — both are on its face below, not argued away.
**Confidence in the structure:** Medium-High (strike, tenor, liquidity, sizing checked). **Moment properties NOT graded** (construction rule #14): every quote here is an **after-hours vendor SCREENING mark**; Fidelity's live chain governs at the fill (root rule #4; `RISK_RULES.md` finding 5b).
**`$0` MOVED · NO ORDER · NO GATE OR THRESHOLD CREATED OR MOVED** (every guard below already exists; the entry rule and the card's own limits are construction, not gates).

---

## 1. ⚠️ The caveat that could change the decision — BOND's kill is MET, and this card bets the other way

| Item | Value (source) |
|---|---|
| Rule | BOND's Sept-4 thesis kill, dealer leg for a 5Y fire as Will ruled it 9/26 (WQ-291) |
| Print | NY Fed FR2004 3–6Y dealer positions as-of 9/23: **$60.079B vs the $56.586B bar ⇒ MET by +$3.493B** (published 10/1 16:13–16:15 ET; BOND `96ccc7a0c`, `KB-BND-383`) |
| BOND's consequence | **"Exit all duration shorts"** — a recommendation, PENDING Will as **WQ-357** (exit card `MGMT-DURSHORT-EXIT-WQ291`, desk lean SELL both Fri 10/02) |
| BOND posture token | `kill=MET-REC@2026-10-01; posture=HOLD-NO-ADD` (`AGENTS/BOND/TRADE.md` line 5, read at the artifact 21:0x ET; BOND is dark) |
| Riders (BOND, verbatim in substance) | ① a 3–6Y inventory build is NOT proof of auction warehousing · ② the funding window is UNGRADED · ③ an operational rule, no claim the threshold predicts outcomes |
| What cuts the other way (BOND reported, never graded) | same print: long-end total **−$3.8B** to $140.5B; 6–7Y **−$4.646B** — the build sat in 3–6Y, not in duration overall |

**How a fresh short squares with that, stated plainly:** it does not square — it **overrides** it. Will's word overrides WQ-339's own stand-down rule; it does not erase the kill. If Will takes BOND's exit (WQ-357 A) **and** this card, the result is a duration short re-established the same week the kill fired, in a later expiry (§6). The honest reading available to him is BOND's own caveat: the kill fired on belly (3–6Y) evidence while the long end moved the other way — **a reason to decline the exit with eyes open, never evidence that the kill did not fire.** Durable finding 12 (*a fired kill-switch is held, not re-litigated*) is why TERRY's lean on WQ-357 stays SELL; this card is Will's separate, commissioned view.

**No registered trigger licenses this card.** Will's 6/26 standing rule (fresh capital only on a fired trigger; durable finding 1): both BOND add-gates fired and were **spent** — the add was DECLINED 9/24 (WQ-280), the auction re-arm is spent on 004 (`BOND/TRADE.md` Reactivation Matrix), and the 7/16 NO-ADD covered the old card. **The only thing that can license a fill is Will's own [Approve] on this card, as an explicit override of his 6/26 rule.** Variant E2 (§4) is the trigger-disciplined form, with its base rate.

## 2. Will's observation, measured — "treasuries/bonds recovered today somewhat": ✅ TRUE, and small

TLT went **ex-distribution on Thu 10/1: $0.311581** (declared 9/30, record 10/1, paid 10/6 — Nasdaq dividend-history API, read 20:59 ET; the vendor's daily bar for 10/1 was not yet posted). IEF and SHY went ex the same day. TBT has no 10/1 distribution (last ex 9/23).

| Instrument | 9/30 close | 10/1 close (vendor, read 20:58 ET) | Price Δ | Ex-distribution 10/1 | **Dividend-neutral Δ** |
|---|---:|---:|---:|---:|---:|
| **TLT** | $77.78 | $77.71 | −0.09% | $0.311581 | **+0.31%** |
| IEF (7–10Y) | $89.31 | $89.30 | −0.01% | $0.306924 | +0.33% |
| SHY (1–3Y) | $81.20 | $81.10 | −0.12% | $0.241001 | +0.17% |
| TBT (−2× daily, 20+Y index) | $42.49 | $42.19 | −0.71% | none | implied index **+0.35%** |

Official Treasury par curve, 10/1 vs 9/30 (home.treasury.gov CSV, read 20:59 ET): 2Y 4.88→**4.78** (−10bp) · 5Y −8 · 10Y 5.29→**5.24** (−5) · 20Y −4 · 30Y 5.64→**5.61** (−3) · 10Y real 2.93→2.88 (−5). **A front-led bull steepener.**

⇒ **10/1 was a GREEN day for long bonds: +0.31% on TLT dividend-neutral** (cross-check: TBT implies +0.35%, the two agree within 4bp). The broker's "Today" column showed TLT **red** (−0.09%) only because $0.31 came off the price. It was the **first green session after seven straight red ones** (9/22→9/30, TLT $81.80 → $77.78, −4.9% on price; no ex-date inside that run; 63 vendor bars 7/2–9/30, none missing in the window). The bounce recovered roughly **6%** of that drop. "Somewhat" is the right word.
⚠️ 10/1 is past: a green Thursday does not make Friday green, and a green day is the market moving **against** this card's thesis (construction rule #15 — it carries zero thesis information).

## 3. Position truth and the book it adds to

Broker truth = Will; source = `FORGE/STATUS.md` reconciled by ANVIL to Will's 10/1 16:15 ET end-of-day capture (`[10/1 pc]`). **Friday's dispositions are unknown** — Will said *"will probably sell those tomorrow"* ~19:0x ET, an intent, not an [Approve], scope not itemized. `[POSITION_STATE as of 10/1 pc]`.

| Line | Qty | Vendor screening mark, 21:01 ET | Value | TLT-equivalent short (model) | Rail on file |
|---|---|---|---:|---:|---|
| TLT $82P Oct-16 | 1 | bid 4.20 / ask 4.35 (OI 35,345) | $420 | ≈ $7,340 (delta −0.94, Black–Scholes, IV 16.4%) | WQ-357 (exit rec, PENDING) · WQ-302 (Will's A/B/C by Wed 10/14) · backstop Fri 10/16 |
| TBT | 10 sh | $42.19 | $421.90 | ≈ $844 (2× of $422) | WQ-357; no management rule |
| **Sleeve today** | — | — | **$841.90** | **≈ $8,180** | — |
| **This card** (Dec-18 77P ×2 at tonight's ask) | 2 | ask 2.08 | **$417.30 at risk** | ≈ $6,870 (delta −0.44 each) | §6 |

**The sleeve under each WQ-357 choice, with and without this card (same marks; size against the SLEEVE, never per card):**

| WQ-357 choice | Without the card: at risk · TLT-equiv | **With the card: at risk · TLT-equiv** | What it means |
|---|---|---|---|
| **A — exit both (BOND's rec, TERRY's lean)** | $0 · $0 | **$417 · ≈ $6,870** | ≈ 84% of today's direction re-bought at half the dollars at risk, expiry moved 10/16 → 12/18. **In substance, the short survives its own kill.** |
| B — exit the 82P, keep TBT | $422 · ≈ $844 | $839 · ≈ $7,710 | About today's direction, the IRA exercise problem gone |
| C — hold both to WQ-302 (10/14) | $842 · ≈ $8,180 | **$1,259 · ≈ $15,050** | **≈ 1.8× today's duration short — an ADD** against BOND's `HOLD-NO-ADD` and the WQ-280 decline |

**Mechanics that a card cannot see from here:**
- **A strike-and-expiry change is a NEW DEPLOYMENT, not a roll** (construction rule #21: roll = same underlying, same strike, later expiry). The 60–90 DTE band binds: Dec-18 = **78 DTE** tonight, 64 DTE on 10/15 — inside the band through the entry window (§4).
- **Cash interaction with the USO $150C Oct-09 ×1:** exercise needs $15,000; Fidelity cash + pending = $14,147.60 + $1,377.10 = **$15,524.70 ⇒ $524.70 headroom** [10/1 pc]. This card at $417.30 leaves **≈ $107**. Under choice A the sale proceeds (≈ $841 at tonight's marks) restore ≈ $949. **If both happen the same day, sell first, then buy.**

## 4. Entry — a rule that survives Friday's 08:30 ET payrolls print

Puts trade from 09:30 ET; the print lands before any fill is possible, so **no level read tonight is an entry level.** The rule:

| # | Condition — ALL must hold at the moment of the fill | Why |
|---|---|---|
| E-1 | **Will's [Approve] on this card** (and his WQ-357 choice stated, so the sleeve in §3 is known) | root rule #5; §1 — no registered trigger |
| E-2 | **Window:** from Fri 10/02 **09:45 ET** (opening spreads settle) through **Wed 10/14 15:00 ET**. Unfilled ⇒ the card **lapses**; a new window needs a re-card (moment properties re-marked, the tenor re-checked against the 60–90 DTE band) | construction rule #14; #21 band |
| E-3 | **TLT GREEN at the fill, dividend-neutral:** TLT last > its prior regular-session close. **No TLT ex-date falls inside the window** (monthly pattern: 6/1 · 7/1 · 8/3 · 9/1 · 10/1 ⇒ next expected Mon 11/2 — INFERRED, not yet declared), so on every window day the price change IS the dividend-neutral change. **Cross-check at the same moment: TBT RED** (no TBT ex-date expected before ~late Dec). If the two disagree, no fill that day | root rule #6 on the underlying (standing guard, `PROME/ACTIVE_DECISIONS.md` TRY-FIRE-004 row); §2 measured why the broker's colour can lie on an ex-date |
| E-4 | **No entry into a red tape:** a session that is red at the fill is never an entry session, however the open looked; a green open that turns red before the fill cancels that day | standing guard per PROME's packet — ⚠️ the phrase *"multi-session red tape"* is **SEARCH-NOT-FOUND** in the current `ACTIVE_DECISIONS` standing-guards cell (checked 21:0x ET); encoded here from card 004's own precedent: the 7/16 red-day-at-range-lows fill was a chase, the 7/17 green day the clean entry |
| E-5 | **DGS10 not disarmed:** no official DGS10 close **< 4.50** between tonight and the fill (10/1 official 10Y = **5.24**, 74bp away) | standing guard (disarm DGS10 <4.50); pre-fill only — see §6 |
| E-6 | **Do not chase the underlying:** no fill if TLT is below **$74.50** at the fill (−4.1% from tonight, about the size of the whole 9/22–9/30 leg) — re-card instead | Non-Negotiable #5 |
| E-7 | **Do not chase the premium:** limit ≤ **$2.45 per contract** (×2 + $1.30 fees ≤ **$491.30**, under the $500 cap). Strike = the whole-dollar strike **at or just below** TLT at the fill (tonight: 77). If its Fidelity ask is above $2.45, step **one** strike lower; if that is also above $2.45, no fill that day | $500/card (Will 6/26); a rising premium on a green day is vol being bid — the thing root rule #6 is a proxy for |

**What the print does to this rule:** a **hot** payrolls number (yields up, TLT red) ⇒ **no fill** — that is the day puts are dear. A **soft** number (yields down, TLT green) ⇒ a fill is allowed — and it is the day the market moved against the thesis (rule #15). **On the WQ-357 exit card the colours line up:** on a green Friday its sale is the measured break already written there (82P time value −$0.09 at the bid tonight) and this card may fill; on a red Friday the sale is clean and this card waits.

**Variant E2 — the trigger-disciplined form (offered, not the lean):** replace E-1's override with a fresh BOND-graded composition failure (the OLD conjunctive test: indirect below the tenor's trailing-12 min AND dealer above its max, frozen bars per `BOND/TRADE.md`) at the **10/6 3Y · 10/7 10Y-R · 10/8 30Y-R**, then the first green session. **Base rate: 1.8% per auction (BOND, 4 of 224) ⇒ ≈ 5% that any of the three fires.** BOND has not said whether a fresh failure after a MET kill is a re-entry signal (SEARCH-NOT-FOUND in `THESIS.md` §EXIT and `TRADE.md`) — a gap BOND fills, not TERRY.

## 5. Structure

| Expression (tonight's vendor asks, after hours) | Cost incl. $0.65/ct | Why / why not |
|---|---:|---|
| ★ **TLT Dec-18-2026 $77P ×2** — 0.9% OTM, 78 DTE, IV 16.97%, OI 35,396, spread 1.45%, quotes two-sided (`chain_fetch.py --no-cache`, 21:00 ET) | **$417.30** | Inside the 60–90 DTE band; spans the October refunding (10/6–8), CPI 10/14, 20Y 10/21, FOMC 10/28, QRA 11/4 and the November refunding (3Y 11/9 · 10Y 11/10 · 30Y 11/12) before the 11/18 time stop. **Two contracts so the harvest-half guard is executable** |
| TLT Nov-20-2026 $77P ×2 | $311.30 | ✗ 50 DTE — fails the 60–90 DTE band for a new deployment (construction rule #21) |
| TLT Dec-18 $77/$72 put spread ×3 (sells the richer wing: 72P IV 18.27 vs 16.97) | $447.90 | Similar P/L in most paths, better if flat, worse in the tail; max value $1,500 ⇒ the ≥3× harvest is reachable only near full width. Listed, not the lean |
| TLT Dec-18 $74P ×4 | $418.60 | More convex, needs TLT below ≈ $72.95 (−6.1%) at expiry to break even |
| More TBT shares | linear | No defined loss window, 2× daily-reset drag; the sleeve already holds 10 sh |

⚠️ **Paying up for vol, measured:** Dec ATM implied ≈ **17%** vs TLT realized **11.1% (10-day) / 10.6% (20-day) / 10.0% (60-day)** (total-return log changes, 125 bars, vendor). Durable finding 8 holds: rates pay the full vol tax. A green day lowers the delta cost; it does not make 17 vol cheap.

## 6. Risk and management

**N_eff = 1.** Claimed legs: this card + the 82P + TBT + the oil legs. Shared antecedent: **oil falls and takes yields down with it** — Will ruled the concentration ACCEPTED (WQ-297 A, 9/25). Live screening marks 21:01 ET (vendor, after hours): energy = USO 37 sh × $150.02 = $5,550.74 + USO $150C Oct-09 bid 4.20 = $420 + VLO 1 × $408.46 ⇒ **$6,379.20**; duration sleeve $841.90; this card $417.30.

| Directional book on the one falsifier | Without the card | With the card |
|---|---:|---:|
| WQ-357 A (exit both) | $6,379.20 | **$6,796.50** |
| WQ-357 C (hold both) | $7,221.10 | **$7,638.40** |

(Fidelity account $36,077.04 [10/1 pc]; the card = 1.2% of it. The QQQ puts are outside this sum, as in the standing-guards cell.)

- **Max loss:** the premium, ≤ **$491.30** by E-7; **$417.30** at tonight's asks. Forward max loss after the fill = the remaining mark (construction rule #20d).
- **Break-even at expiry:** $77 − $2.0865 = **$74.91** (−3.6% from tonight).
- **Harvest-half ≥3× (standing guard):** sell **1 of 2** when Fidelity's bid ≥ **3 × the fees-in per-contract basis** (tonight's ask ⇒ **$6.26**). ⚠️ **Reachability:** model says TLT ≈ **$71.00 (−8.6%)** by the 10/28 FOMC, ≈ $70.83 by 11/18. The whole 9/22–9/30 leg was −4.9%. **A tail, not a base case** (finding 9 — the moderate profit zone is covered by the time stop below).
- **Time stop = sell-or-roll by Wed 11/18 15:00 ET** (30 DTE; after the November 30Y on 11/12), whatever the mark. Will's standing practice is sell or roll before expiry (`USER.md` 9/30); a roll here is pre-registered only as **same strike, later expiry**, and is still a Will-gated proposal (construction rule #21c). Holding to 11/18 also keeps the position far from the IRA expiry-exercise unknown (FORGE D-60).
- **DGS10 < 4.50 after the fill:** the entry guard does **not** exit a filled position (finding `guard_scope_expires_at_the_fill`). A post-fill rates exit is BOND's position kill in `THESIS.md` §EXIT 2 — 10Y < 4.15 AND 30Y < 5.0 for 3 sessions AND a clean refunding (10/1: 5.24 / 5.61) — BOND grades.
- **BTC < 2.15 (standing guard):** an arming leg of card 004's arm #1, not an entry leg here; recorded so its absence is not read as unrun. **Arm #3:** SPENT, does not re-open.

| Scenario P/L, ×2 at $417.30 (Black–Scholes, IV 17% flat — model, not a quote) | TLT $80 | $77.71 | $75 | $73 | $71 |
|---|---:|---:|---:|---:|---:|
| at the 10/28 FOMC (51 DTE) | −$247 | −$88 | +$207 | +$496 | +$834 |
| at the 11/18 time stop (30 DTE) | −$322 | −$180 | +$124 | +$438 | +$801 |

## 7. Why not / counter-case

1. **The thesis owner says exit.** A pre-registered kill fired on 10/1; this card re-takes the direction within days of it. Finding 12 exists for exactly this.
2. **No fired trigger** — the card fires on Will's word alone (§1), the condition his own 6/26 rule was written to stop.
3. **Vol is rich** — ~17 implied vs ~11 realized; a grind pays little and only a fast shock pays the harvest.
4. **Crowding** — BOND (TRADE.md breach protocol 5): consensus is short duration, and the short-covering rally fires on a dovish surprise; 10/1's front-led −10bp in the 2Y was a small one.
5. **For it:** the long end is long-end and real-led since 9/22 (BOND STATUS: 10Y 5.29 / 30Y 5.64 [9/30], highest since 2002; ACM term-premium share 0.89 for 9/21→9/25); construction rule #23's driver is named; the dense October–November auction calendar is exactly the window the thesis says matters; max loss is bounded at the premium.

## 8. What TERRY could not check

- **Fidelity's live chain and colour** — unseen; every quote is a vendor after-hours screening mark (last trades 10/1 13:49–16:14 ET; bid/ask age unknowable from the feed, finding 5b).
- **The distribution** — from Nasdaq's dividend history only; iShares' own page not checked. Consistent with TBT's implied move (+0.35% vs +0.31%).
- **Greeks and scenarios** — Black–Scholes model estimates (r 4.0%, q 4.8%, flat IV), not quotes.
- **BOND's view on re-entry after a MET kill** — none on file; BOND dark tonight.
- **Friday's book** — whether Will exits under WQ-357, and the QQQ 740P ×4 disposition, are unknown; §3 must be re-read from the mirror before a fill.

## Decision

> **WQ-339 successor (Will):** **APPROVE / REJECT — buy 2 TLT Dec-18-2026 $77 puts (strike = at or just below TLT at the fill), limit ≤ $2.45 each, total ≤ $491.30 (≈ $417 at tonight's marks), on the first session from Fri 10/02 09:45 ET to Wed 10/14 15:00 ET on which TLT is green (and TBT red) at the fill and above $74.50.** Harvest 1 of 2 at ≥3×; sell-or-roll both by Wed 11/18 15:00 ET. State the WQ-357 choice with it. **⚠️ BOND's kill is MET and BOND recommends exiting duration shorts; this card has no registered trigger.**

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.**

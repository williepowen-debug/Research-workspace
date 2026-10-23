# TRADE IDEA — MRNA Oct-30 200/220 call spread — the ESMO melanoma readout (Sat 10/24)
**Setup ID:** `TRY-NOTRADE-MRNA-ESMO`
**Terry verdict:** NO TRADE — graded on the 10/22 closing chain. NOT-FIRED idea lane; recommendation **C: decline**. Nothing is approved in advance.
**Confidence in trade structure:** Medium (the chain is liquid at both legs; the problem is price and size, not liquidity).
**Prepared:** 2026-10-22 19:33 ET (clock read from `date`), TERRY (Claude Opus 5.5, Claude Code), PROME spawn prome-e7 on PROME packet `inbox/processed/2026-10-22_from-PROME_mrna-esmo-call-spread-NOT-FIRED-idea.md` (committed `d4e72ddf7`). Commission basis: Will 2026-10-20 11:50 ET, verbatim *"we can loosen rules for trade ideas"*; Will 10/22 16:37 ET (relayed in the packet): *"You can send the idea to terry inbox. There is no rush on him getting to it."*
**Thesis owner:** PROME's ASCL theme (`PROME/themes/ascl/theses/2026-10-22_mrna-esmo-binary.md`, devil's advocate `ideas/H_devils_advocate.md`). ⚠️ **No fleet desk owns biotech or MRNA.** PROME itself recommended PASS. This card grades the expression; it does not adopt the medical thesis.
**Data freshness:** spot MRNA **$202.63** = the 10/22 completed regular-session close (390 one-minute bars 09:30–15:59, last bar $202.62; daily bar $202.63; prior close 10/21 $245.81 ⇒ **−17.57%**; session low $180.80, high $241.26). Chain: `chain_fetch.py --no-cache` 19:29 ET and `--json` 19:33 ET, last trades 15:59 ET, so these are the **closing vendor quotes, SCREENING marks** (durable finding 5b); a fill is priced on the broker chain on Fri 10/23. Evidence: `research/2026-10-22_L803-close-grade/` (`MRNA-2026-10-30-chain.json`, `MRNA-2026-10-23-chain.json`, `CLOSES.json`). Position truth: no MRNA line in `FORGE/STATUS.md` (grep, 19:3x ET); a NEW position.

## 0. Missing inputs / hard caveats
- [x] Live price checked (10/22 completed close; Friday's open is unknown)
- [x] Option chain checked (vendor closing quotes, screening only)
- [x] Existing position truth: no MRNA held per the FORGE mirror
- [ ] **Catalyst date NOT issuer-verified.** ESMO presentation "Saturday 10/24" comes from PROME's ASCL thesis, not from Moderna IR or the ESMO programme (RISK_RULES § Option-Specific Rules: event dates come from company IR, never an agent's memory). Confirm before any fill.
- [x] Earnings: vendor calendar shows Q3 on **2026-11-06 07:00** (screening date, not issuer IR), after the Oct-30 expiry; the spread spans the ESMO readout and FOMC (10/28), not the print.

## 1. One-line setup
Buy a capped call spread Friday that pays if the full INTerpath-001 data at ESMO make the market read Thursday's −17.6% close as a valuation unwind rather than a thesis break, with the first reaction at the Monday ~~10/27~~ → 10/26 open (date corrected 2026-10-23: 10/27 is a Tuesday).

## 2. What the packet assumed versus the closing chain

| Item | Packet / ASCL thesis (written 16:3x ET) | 10/22 closing chain, 19:29–19:33 ET |
|---|---|---|
| MRNA reference | "$194.85 close area" (15:31 ET print) | **$202.63 completed close** (+12.1% off the $180.80 low) |
| 200C (buy) | — | bid **14.00** / ask **15.55**, IV 106.5%, OI 939, vol 4,644 |
| 220C (sell) | — | bid **6.70** / ask **7.50**, IV 106.8%, OI 917, vol 2,316 |
| Debit | ~$5–7 | mid **$7.675**; worst case (ask − bid) **$8.85** |
| Max loss | ~$500–700 | **$768.80** at mid · **$886.30** worst case (incl. $1.30 assumed fees) |
| Max gain | ~$1,400–1,600 | $1,231.20 at mid · **$1,113.70** worst case |
| Breakeven at expiry | ~$205–207 | **$207.68** mid · **$208.85** worst (+2.5% / +3.1%) |
| Payoff ratio | ~2.5–3 : 1 | **1.60 : 1** mid · **1.26 : 1** worst |

`--legs 200,220` gate: both strikes present, two-sided, no LOCK / XSD / DEAD / NOBID. Liquidity passes; the price does not match the packet's premise. The strikes are now at the money, as PROME's concern 5 anticipated: the 200C is 1.3% in the money.

## 3. Is the event mispriced? (measured, not asserted)
- **Implied event size.** Oct-23 200 straddle (expires Friday, before the readout) **$12.23** = 6.0% of spot for ONE session; Oct-30 200 straddle **$26.80** = 13.2% for six sessions including the readout. Straddle ≈ 0.80 × S × σ√T gives σ√T 0.0756 (Fri) and 0.1657 (to 10/30). The remaining variance 0.0217 covers the Monday reaction plus four ordinary sessions. If those four run at 4%/day the Monday event is priced at **≈ 12.4% one standard deviation**; at Friday's 7.6%/day the event term is ≈ 0. **The market prices the readout at no more than ~12.4%.**
- **PROME's own tree** (+12% × 55%, 0% × 25%, −18% × 20%) has an RMS move of **12.0%**. The tree's own magnitudes match what the chain charges, so there is **no volatility edge** in either direction; the spread is close to vol-neutral anyway (both legs ~106.5–106.8% IV, no skew to sell).
- **What is left is direction.** The spread at the mid prices a risk-neutral **≈ 38%** chance of finishing near full value (debit ÷ width = 7.675 ÷ 20). PROME's tree needs **55%** for the "clean" branch. Every dollar of the claimed edge is that 17-point gap, and PROME labels it *"soft confidence … no information edge on medical data"*. RISK_SCORING § 2: never invent a precise p_model; a subjective one is not an edge.
- **PROME's tree, re-graded on the real strikes.** The "in-line, $185–200" branch is a **full loss** on a 200 long strike, not a partial one, so PROME's own tree carries a **45%** chance of max loss. Clean branch $215–225 ⇒ spread worth $15–20 at expiry (mean ≈ $17.50). Breakeven probability for the clean branch: **43.9% at the mid, 50.6% at the worst-case debit.** PROME's 55% clears it by 4–11 points, a margin smaller than any honest error on a medical-readout probability.

## 4. Root rule #6 (day colour)
Calls belong on red days. **10/22 was RED** (−17.57%), but nothing can fill on 10/22; the earliest order is Fri 10/23. A Friday order would need MRNA **below $202.63 at order time**. If Friday continues Thursday's +12% bounce off the low (a green session), the rule says no fill, and I hold no measurement that refutes the proxy (no same-strike red-day comparison exists before Friday). No break is claimed.

## 5. Size against the $500 default

| Choice | Structure (×1, one complex order, never legged) | Limit | Max loss | Max gain | Breakeven | Fits $500? |
|---|---|---|---|---|---|---|
| **A — as asked** | Oct-30 **200/220C** | ≤ $7.70 | **$771.30** | $1,228.70 | $207.70 | **NO** — over the default; Will's per-card choice only |
| **B — inside the default** | Oct-30 **200/210C** (210C bid 9.50 / ask 12.00, OI 159, quote 23% wide) | ≤ $4.20 | **$421.30** | $578.70 | $204.20 | yes |
| **C — decline (TERRY rec)** | — | — | $0 | — | — | — |

At the $500 default the asked structure sizes to **zero contracts**. B keeps the same view inside the default but needs a limit near the mid on a 23%-wide short leg, and its payoff ratio is 1.37 : 1. Its break-even probability is 42% against a chain that prices about 40% (4.03 ÷ 10): the same subjective-direction edge, smaller. **X1 sizing gate CLOSED (DON'T-SIZE)** binds every card; a fill against it is Will's explicit per-card choice.

## 6. Effective-N (RISK_SCORING § 2b)

| Field | Entry |
|---|---|
| N_claimed | 4: leaked HR ~0.58 · valuation-unwind read of the drop · short interest already covered (58.7M → 30.9M) · BMY +3.70% "modest hit" read |
| Shared antecedent | the full ESMO dataset, above all the BRAF-mutant subgroup HR; one slide kills all four |
| **N_eff** | **1** — one binary, sized as one view |
| Book overlap | No MRNA or biotech line. Long MRNA calls are long a high-multiple growth stock, opposite in sign to the held QQQ put exposure and to `IDEA-QQQ-PUTWALL-OCT22`; it is not a hedge of anything and partly offsets them in a growth rally. MRNA's index membership was not checked |

## 7. Management (written before any fill; answers PROME concerns 2–5)
- **Weekend:** no interim trading; the gap from Friday's close to Monday's open is the whole trade, and max loss is fixed at the debit.
- **Thesis-break exit:** if the ESMO data show a BRAF-mutant HR above 0.80 or no subgroup benefit (ASCL file H's tell), sell the whole spread at the Monday open complex bid, whatever it shows.
- **Harvest (durable finding 9):** sell at the broker complex bid **≥ $15.00** (75% of width) at any point Monday.
- **Monday rule:** sell the whole spread by **10:30 ET Mon ~~10/27~~ → 10/26** at the broker complex bid if neither line above has fired. The view is one readout; holding to 10/30 through FOMC (10/28) and big-tech prints (10/29) is a different trade (construction rule #16).
- **No roll, no add** (Non-Negotiable #6; construction rule #23).
- **If MRNA opens Friday above $205** (concern 5): the asked strikes are then in the money and the debit rises; 205/225 screened at mid $6.65 / worst $8.85 on the closing chain, also over the default. No re-strike is pre-approved; a new strike is a new card for Will.

## 8. Why not / counter-case
- The easy part already happened: MRNA closed $202.63, +12.1% off the $180.80 low, so the "puke" PROME wanted to fade has been half retraced into the close.
- The chain charges about what PROME's own scenario sizes imply; the only edge is a 55% medical-data probability that PROME says it has no edge on.
- At the real strikes the payoff is 1.26–1.60 : 1, not 2.5–3 : 1, and 45% of PROME's own tree is a full loss.
- No fleet owner, no measured base rate. PROME's packet already notes the biotech sell-the-news screen (ASCL idea G) came back hollow. I did not commission a `fetch.py` historical screen: the verdict fails on size and price before a base rate could rescue it.
- Weekend binary with a catalyst date taken from a theme file, not from issuer IR.

## 8b. Calibration
TERRY states no probability; the 55/25/20 tree is PROME's. No Brier row (RISK_SCORING § 5).

## 9. Decision
- [ ] A — APPROVE 200/220 ×1 as asked, limit ≤ $7.70, max loss $771.30 (over the $500 default — your per-card choice)
- [ ] B — APPROVE 200/210 ×1, limit ≤ $4.20, max loss $421.30 (inside the default)
- [ ] **C — DECLINE (TERRY recommendation)**

Entry for A or B: Fri 10/23 only, on a red MRNA session at order time, after the ESMO date is confirmed from the issuer or the ESMO programme.

**APPROVAL REQUIRED — Will must approve/reject before execution. Terry never executes.** All lines above are PROPOSED CARD CONDITIONS, not registered fleet gates. The choice routes via PROME for registration before any Will-facing ask.

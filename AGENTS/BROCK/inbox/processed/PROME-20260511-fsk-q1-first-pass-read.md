# PROME → BROCK: FSK Q1 First-Pass Read

**Date:** 2026-05-11 19:20 ET
**From:** PROME / Chief of Staff
**To:** BROCK
**Priority:** 🔴 Private-credit domain follow-up
**Owner:** BROCK — BDCs / private credit / forced marks

## Why this note exists

Will wants the FSK issue left to the private-credit-focused agent. This inbox note gives you the post-release facts Prome already pulled so you do not have to reconstruct the first pass from scratch.

Use this as input, not as a replacement for your own BROCK read.

## Source / References

- Full first-pass Prome memo: `PROME/FSK_Q1_READ_MAY11.md`
- Pre-build: `AGENTS/BROCK/domain/sources/FSK_PREBUILD_MAY11.md`
- Action card: `PROME/action-cards/FSK_MAY11_ACTION_CARD.md`
- FSK release mirror fetched via StockTitan / PRNewswire on 2026-05-11.
- Dashboard run: `python3 FORGE/tools/market-data/dashboard.py --compact` at ~18:26 ET.

## Prome First-Pass Classification

**FSK Q1 = Strong Bear / near Max Bear.**

This is materially worse than OBDC and clears the action-card threshold for reopening fresh BDC/private-credit downside discussion. It does **not** yet confirm broad public-credit contagion because HY OAS and VIX remain benign.

## Key FSK Q1 Facts

| Metric | Q4 / baseline | Q1 result | Read |
|---|---:|---:|---|
| NAV/share | $20.89 | **$18.83** | -9.9% QoQ; below Strong Bear line <$19.85 |
| Adjusted NII/share | $0.52 | **$0.41** | Bear — income degradation |
| NII/share | $0.48 | **$0.42** | Dividend barely covered before support measures |
| Q2 distribution | $0.48 total / $0.45 base baseline | **$0.42** | Cut / reset lower |
| Realized + unrealized loss/share | Q4 loss $0.89 | **$2.00 loss** | Mark pressure accelerated |
| EPS | Q4 loss $0.41 | **($1.57)** | Large quarterly loss |
| Non-accruals | 5.5% cost / 3.4% FV | **8.1% cost / 4.2% FV** | Strong Bear on cost; FV worsened |
| Net debt/equity | 1.22x | **1.31x** | Leverage rising into stress |
| Purchases vs sales/repayments | Watch runoff | **$499M purchases vs $710M sales/repayments** | Defensive shrink / runoff |

## Strategic Support Package

FSK announced:

1. **$150M cumulative convertible perpetual preferred** purchased by KKR affiliate.
   - 5% cash dividend or 7% PIK at FSK option.
   - Senior to common, junior to debt.
   - Initial conversion price **$18.83** = Q1 NAV.
2. **$150M KKR affiliate tender offer** at **$11.00/share**.
3. **$300M share repurchase authorization** through June 1, 2027.
4. **50% subordinated income incentive fee waiver** for four quarters.

Prome read: supportive optics / sponsor backstop, but bearish evidence. Healthy BDCs usually do not need preferred capital, fee waivers, and repurchase optics after a ~10% NAV drop.

## Revolver / Funding Tell

Subsequent event: May 8 Senior Secured Revolving Credit Agreement amendment:

- Commitments reduced to **~$4.052B from $4.700B**.
- Applicable margin increased for extending lenders.
- Minimum shareholders' equity floor reset to **$3.750B from ~$5.049B**.

Prome read: lender support continues, but on tighter terms and with a lower covenant floor. This is one of the important stress tells for BROCK to evaluate.

## Tape Cross-Check at 2026-05-11 ~18:26 ET

- HY OAS **281bps 🟢** — no broad public-credit confirmation.
- CCC OAS **920bps 🟡**.
- BIZD **$12.62 🔴** — BDC sector weak.
- APO **$130.46 🟡/$130 watch** — still above watch line.
- ARES **$124.61 🟡**.
- VIX **18.38 🟢**.
- KRE **$68.55 🟢**.
- Brent **$104.25 🔴**.
- USD/JPY **157.16 🟡/near red**.

## Decision Context / Constraints

Will explicitly said to leave the FSK issue to the private-credit focused agent.

Prome posture:

- Fresh BDC/private-credit downside discussion is allowed.
- No blind chase while HY OAS <300 and VIX <20.
- Do **not** rescue dead June APO/ARES by default.
- Prefer liquid, longer-dated structures if BROCK recommends action: likely BIZD or ARCC Sep/Dec puts, subject to live bid/ask.
- Any trade requires Will approval.

## Ask to BROCK

Please produce the domain memo requested in `AGENTS/BROCK/inbox/PROME-20260510-fsk-live-read-and-pc-10q-watch.md`, incorporating this post-release data.

Focus especially on:

1. Whether FSK is idiosyncratic legacy cleanup or evidence of sector-wide BDC mark/income deterioration.
2. Read-through to APO / ARES / OWL / BIZD / ARCC.
3. Whether KKR support package should be treated as stabilizer, stress evidence, or both.
4. Whether revolver amendment changes forced-mark / funding-pressure interpretation.
5. What, if anything, Will should consider tomorrow after live option-chain pricing.
6. Next forced-mark tests: GCRED / OTF / BCRED / CTAC.

## Output Wanted

Use the prior requested format:

```markdown
# BROCK FSK Q1 READ — May 11 2026

## Classification
- Branch:
- Confidence:
- One-line read:

## Evidence Table
| Metric | Q1 read | Bull/Bear implication | Notes |

## Private-Credit Position Implication
- APO:
- ARES:
- OWL:
- BIZD:
- Fresh premium? yes/no and why

## Next Forced-Mark Tests
| Vehicle | Filing status | Watch item | Bear trigger |

## Decision Inputs for Prome
- What should Will do Monday/tomorrow?
- What would change your mind?
- What still needs confirmation?
```

# FSK May 11 Action Card
**Created:** 2026-05-08 21:08 ET  
**Status:** Active until FSK Q1 read is complete  
**Event:** FSK Q1 2026 results — May 11 before NYSE open, call 9:00 ET  
**Pre-build:** `AGENTS/BROCK/domain/sources/FSK_PREBUILD_MAY11.md`  
**Position snapshot:** `PROME/POSITIONS.md` updated 2026-05-08 14:17 ET from Will screenshots  
**Decision-flow spec:** `PROME/DECISION_FLOW.md`

---

## Objective

Convert the FSK Q1 branch into a disciplined portfolio decision.

This card is **not** a trade order. It defines what actions are allowed or forbidden after FSK prints. Any actual trade requires Will’s approval.

---

## Current Relevant Exposure

### Private Credit / BDC / Alt-Manager

| Position | Expiry | Qty | Current value | Read |
|---|---:|---:|---:|---|
| APO $100P | Jun 18 2026 | 1 | **$30** | Near-dead residual |
| APO $95P | Dec 18 2026 | 1 | **$310** | Only meaningful private-credit structural put |
| ARES $95P | Jun 18 2026 | 1 | **$55** | Near-dead residual |
| OWL $9.5P | Jun 5 2026 | 2 | **$50** | Small near-dated residual |

**Private-credit subtotal:** ~**$445 / 1.0%** of portfolio.

### Portfolio Context

- Cash: **$19,967.88 / 45.66%**.
- AAPL: **$13,170.60 / 30.12%**.
- Regional bank puts: **~$5.4K / 12.4%** — larger live risk than APO/ARES.

**Key implication:** FSK is not mainly about saving existing APO/ARES option value. It decides whether fresh capital should be deployed or withheld.

---

## FSK Branch Inputs

From `FSK_PREBUILD_MAY11.md`:

| Metric | Baseline / threshold |
|---|---:|
| Q4 NAV baseline | **$20.89** |
| Strong-bear NAV line | **<$19.85** |
| Non-accrual baseline | **5.5% cost / 3.4% FV** |
| PIK baseline | **$55M / 15.8% of investment income** |
| Adjusted NII baseline | **$0.52** |
| Dividend | **$0.48 total / $0.45 base** |
| Net debt/equity | **1.22x** |

---

## Branch-to-Action Table

| Branch | Evidence | Allowed actions | Forbidden actions | Will decision needed |
|---|---|---|---|---|
| **Bull / stabilization** | NAV >$20.50; non-accruals flat/down; PIK <14%; adjusted NII >$0.52; no funding stress | Preserve cash. Keep APO Dec only as small structural option. Sell residual Jun/OWL only if useful bid. Shift attention to banks/Call Reports. | No fresh private-credit premium. No ARCC/BIZD entry. No rolling dead Jun contracts. | Whether to clean up residual Jun/OWL bids, if any. |
| **Mixed / grind** | NAV $20.20-$20.50; non-accruals 5.3-6.0%; PIK 14-17%; dividend covered but thin | Preserve cash. Hold APO Dec. Let near-dead Jun residuals remain unless bid is useful. Continue waiting for GCRED/OTF/BCRED/Call Reports. | No aggressive add. No roll unless pricing is unusually cheap and Will explicitly wants optionality. | Usually no trade decision; confirm “no action” if asked. |
| **Bear / weak tail breaking** | NAV $19.85-$20.20; non-accruals 6-7%; PIK 17-22%; adjusted NII <$0.48 or dividend uncovered | Consider small fresh longer-dated BDC/private-credit downside. Candidate structures: BIZD puts, ARCC Sep/Dec puts, APO Dec add only if pricing sane. Preserve APO Dec. | Do not chase bad spreads intraday. Do not try to “rescue” APO/ARES Jun as primary action. Do not spend large cash without confirming HY OAS/tape. | Will chooses whether to deploy small fresh premium and which vehicle. |
| **Strong / Max Bear** | NAV <$19.85; non-accruals >7%; PIK >22% or >$70M; base dividend uncovered; funding/revolver/covenant stress | Fresh premium allowed. Prioritize liquid, longer-dated structures. Route signal to LIQUID/REGINALD/NEXUS. Reopen ARCC/BIZD downside work. | No blind market orders. No all-in sizing. No execution without live bid/ask and Will approval. | Will approves/rejects specific proposed structure and size. |

---

## Action Priorities by Branch

### Bull / Mixed

1. Do nothing with fresh capital.
2. Preserve cash.
3. Keep APO Dec as residual structural optionality.
4. Do not roll APO Jun / ARES Jun unless Will explicitly wants lottery exposure.
5. Shift focus to regional bank book and Call Reports.

### Bear

1. Confirm live tape: APO, ARES, BIZD, ARCC, HY OAS, VIX, KRE.
2. Prepare one small fresh-premium proposal.
3. Prefer **BIZD or ARCC Sep/Dec** over rescuing dead Jun contracts.
4. Ask Will before action.

### Strong / Max Bear

1. Classify and summarize within 5 minutes.
2. Route signal if funding/revolver/credit transmission is present.
3. Pull live pricing for candidate structures.
4. Present Will with max 2 options and one recommendation.
5. Log decision in `PROME/TRADE_DECISIONS.md`.

---

## Forbidden Actions

- No revenge-adds because existing positions are down.
- No fresh private-credit premium on Bull/Mixed FSK.
- No rolling dead June contracts as the default response.
- No trade execution without Will approval.
- No changing branch thresholds after the print unless the pre-build is demonstrably invalid.
- No using FSK to decide the regional bank book; banks need a separate Call Report/action-card process.

---

## Monday Execution Checklist

1. Pull FSK press release before open.
2. Extract first-pass numbers:
   - NAV/share
   - adjusted NII/share
   - dividend declaration
   - non-accruals cost/FV
   - PIK dollars / %
   - net debt/equity and liquidity
3. Classify branch using `FSK_PREBUILD_MAY11.md`.
4. Pull live dashboard / tape:
   - HY OAS
   - APO
   - ARES
   - BIZD
   - ARCC
   - KRE / VIX
5. Apply this Action Card.
6. If action is proposed, ask Will for approval with:
   - branch
   - proposed structure
   - size/cost
   - why not the alternatives
7. Log final decision in `PROME/TRADE_DECISIONS.md`.

---

## Expiration / Supersession

This card expires after:
- FSK Q1 is read and decision logged, or
- a stronger catalyst supersedes it before May 11, or
- Will explicitly cancels the FSK decision process.

# Regional Bank Weekend Triage Action Card
**Created:** 2026-05-09 11:05 ET  
**Status:** Active through Mon May 11 open / superseded by fresh Call Report read  
**Decision Window:** Weekend May 9-10 prep; market reopen Monday May 11  
**Domain source:** `AGENTS/REGINALD/STATUS.md` updated 2026-05-01 PM  
**Position snapshot:** `PROME/POSITIONS.md` updated 2026-05-08 14:17 ET from Will screenshots  
**Decision-flow spec:** `PROME/DECISION_FLOW.md`

---

## Objective

Convert the current regional-bank put book from a pile of contracts into a disciplined weekend decision framework before Monday open.

This card is **not** a trade order. It defines what should be held, sold, rolled, or researched depending on Call Reports / tape / catalyst confirmation. Any actual trade requires Will’s approval.

---

## Current Relevant Exposure

Regional-bank / CRE short exposure is the main live thesis book now: **~$5,412 / ~12.4%** of portfolio.

### KRE

| Position | Expiry | Qty | Value | Read |
|---|---:|---:|---:|---|
| KRE $60P | Jun 18 2026 | 1 | $24 | Near-dead / shock-only |
| KRE $65P | Jun 30 2026 | 4 | $380 | Salvageable if KRE rolls over; theta risk rising |
| KRE $67P | Jun 30 2026 | 1 | $130 | Best near-dated KRE delta; salvage/roll candidate |
| KRE $63P | Jun 30 2026 | 1 | $52 | Weak salvage / shock-only |
| KRE $60P | Aug 21 2026 | 3 | $261 | Medium runway |
| KRE $60P | Sep 30 2026 | 2 | $228 | Thesis runway |
| KRE $60P | Dec 18 2026 | 7 total | $1,379 | Core runway / not urgent |

### WAL / OZK / Other Banks

| Position | Expiry | Qty | Value | Read |
|---|---:|---:|---:|---|
| WAL $75P | May 15 2026 | 1 | $10 | Near-dead; sell any useful bid or let expire |
| OZK $42.5P | May 15 2026 | 2 | $18 | Near-dead; sell any useful bid or let expire |
| OZK $47.5P | May 15 2026 | 2 | $50 | May salvage only if negative catalyst/tape |
| SSB $95P | May 15 2026 | 1 | $200 | Live May contract; review before selling/holding |
| WAL $85P | Jun 18 2026 | 1 | $510 | Most salvageable WAL near-dated contract |
| WAL $77.5P | Jun 18 2026 | 1 | $200 | Salvage/roll candidate if WAL remains >$78 |
| WAL $65P | Jun 18 2026 | 1 | $25 | Near-dead / shock-only |
| WAL $67.5P | Jun 18 2026 | 2 | $70 | Weak salvage / shock-only |
| WAL $65P | Jul 17 2026 | 1 | $65 | Weak but some runway |
| WAL $70P | Sep 18 2026 | 1 | $270 | Thesis runway |
| WAL $67.5P | Sep 18 2026 | 1 | $210 | Thesis runway |
| OZK $42.5P | Aug 21 2026 | 1 | $90 | Thesis runway / IQHQ lead-in |
| OZK $45P | Aug 21 2026 | 4 | $580 | Core OZK exposure; not a May panic decision |
| HBAN $16P | Oct 16 2026 | 4 | $440 | Only green bank put; keep unless thesis invalidates |
| ZION $57.5P | Jul 17 2026 | 1 | $120 | Weakened thesis; needs kill-condition review |
| FITB $45P | Jun 18 2026 | 2 | $90 | Small residual; depends on Call Report / tape |
| EGBN $25P | Jun 18 2026 | 1 | $10 | Near-dead / shock-only |

**Key implication:** This is not an APO/ARES rescue problem. The weekend task is to separate **May scraps**, **June salvage/roll candidates**, and **Sep-Dec thesis runway** so Monday decisions are not emotional.

---

## Domain Setup From REGINALD

Current REGINALD read:

- Liquid stress is not yet firing: KRE near/above $69, WAL above $78, HY OAS benign, claims benign, SOFR-IORB calm.
- Distressed tail persists under the surface: CCC/HY bifurcation, office CRE stress, private-credit/NDFI linkages.
- Q1 Call Report window May 1-10 is the key disclosure test: WAL MI3, OZK MI3, EGBN trajectory, CFG NDFI, VLY composition.
- WAL thesis refined: compounder with concentrated CRE tail risk, not a simple fast-failure short. WAL $65P Jun was already flagged by REGINALD as close/roll candidate.
- OZK remains slow-grind / reservoir: important catalysts are Aug IQHQ and Oct sub-note repricing, not May contracts.

---

## Weekend Classification Buckets

### Bucket A — Clean-up / May expiry scraps

| Contract | Default weekend stance | Action trigger |
|---|---|---|
| WAL $75P May | Sell any non-trivial bid; otherwise let expire | Only hold if WAL gaps materially lower Monday |
| OZK $42.5P May | Sell any non-trivial bid; otherwise let expire | Only hold if OZK breaks hard Monday |
| OZK $47.5P May | Evaluate Monday; salvage possible | Hold only if OZK weakens or Call Report confirms stress |
| SSB $95P May | Review before action | Sell/hold depends on SSB tape and FL/TX/geography signal |

**Rule:** Do not spend time trying to rescue tiny May contracts. May cleanup is mental/operational hygiene, not thesis expression.

### Bucket B — June salvage / roll candidates

| Contract | Default weekend stance | Decision needed |
|---|---|---|
| KRE $67P Jun 30 | Prime salvage/roll candidate | Price roll to Sep/Dec if KRE >$69 and Call Reports not yet confirming |
| KRE $65P Jun 30 x4 | Salvage/roll candidate | Keep for one red tape window or roll if spreads sane |
| KRE $63/$60 Jun | Shock-only | Do not roll by default; only if cheap package or strong Call Report confirmation |
| WAL $85P Jun | Best WAL near-dated salvage | Hold through Call Report/Investor Day unless bid unusually rich |
| WAL $77.5P Jun | Salvage/roll candidate | Roll only if WAL thesis re-strengthens; otherwise preserve cash |
| WAL $65/$67.5P Jun | Near-dead | Do not roll by default |
| FITB $45P Jun | Small residual | Keep only if Call Report confirms provision/NDFI stress |
| EGBN $25P Jun | Near-dead | Do not roll unless EGBN MI3/CRE stress confirms hard |

**Rule:** June roll capital is scarce. Prefer rolling **one or two higher-delta exposures** over trying to save every ticket.

### Bucket C — Thesis runway / do not panic-sell

| Contract | Reason to keep |
|---|---|
| KRE Sep/Dec $60P | Broad regional-bank runway into Q3/Q4 recognition window |
| WAL Sep $70/$67.5P | Better match for office maturity / Q2-Q3 migration thesis |
| OZK Aug $42.5/$45P | Better match for IQHQ Aug and slow-grind reservoir thesis |
| HBAN Oct $16P | Profitable and has runway; reassess only if thesis/tape invalidates |
| ZION Jul $57.5P | Needs kill-condition review because REGINALD downgraded ZION after Q1 |

**Rule:** Do not sell runway contracts into green tape just to reduce discomfort. Sell/trim only if the thesis is invalidated or better structure exists.

---

## Branch Inputs

| Signal | Bull / reduce urgency | Mixed / wait | Bear / act | Strong bear / urgent |
|---|---:|---:|---:|---:|
| KRE | >$69 sustained | $65-69 | <$65 | <$60 |
| WAL | >$78 sustained | $75-78 | <$75 | <$70 or fresh fraud/credit break |
| HY OAS | <300 | 300-320 | >320 | >350 |
| CCC OAS / bifurcation | <900 and falling | 900-1000 | >1000 | >1100 or CCC/HY ratio widening fast |
| SOFR-IORB | <+5bps | +5 to +15bps | >+15bps | >+25bps |
| Call Reports | MI3/NDFI flat or down | Mixed by bank | WAL/OZK/EGBN MI3 rising; CFG NDFI confirms | Multiple banks show MI3/NDFI/ACL stress simultaneously |
| WAL-specific | Office classified flat/down; 30-89d PD down | mixed | office/classified/PD rising | office classified >$500M / large C&I migration |
| OZK-specific | MI3 stable; past-due normalizes | mixed | MI3/past-due/problem credits rise | IQHQ/Affinius stress or reserve jump |

---

## Branch-to-Action Table

| Branch | Evidence | Allowed actions | Forbidden actions | Will decision needed |
|---|---|---|---|---|
| **Bull / stabilization** | KRE >$69, WAL >$78, HY OAS <300, Call Reports benign | Clean May scraps if bid exists. Preserve Sep/Dec runway selectively. Do not add. Consider cutting weakest June shock-only tickets. | No fresh bank premium. No rolling all June contracts. No revenge-add. | Whether to sell May scraps / weakest June tickets. |
| **Mixed / disclosure wait** | Tape benign but Call Reports not fully read; CCC tail sticky | Hold higher-delta June through next red window. Keep runway. Price one KRE or WAL roll, but do not execute unless attractive. | No broad roll package. No selling runway just because tape is green. | Usually no trade; ask only if a good roll price appears. |
| **Bear / recognition begins** | KRE <$65 or WAL <$75, HY OAS >320, or Call Reports show MI3/NDFI/ACL stress | Roll/selectively extend best June exposure: KRE $67/$65 or WAL $85/$77.5. Keep OZK Aug/HBAN/KRE Dec. Consider small add only after spreads checked. | Do not rescue dead OTM June by default. Do not chase wide spreads Monday open. | Will chooses one roll/add/hold package. |
| **Strong / cascade risk** | KRE <$60, WAL <$70, HY OAS >350, funding stress, or multi-bank Call Report deterioration | Prepare urgent branch: keep all useful downside, pull live chains, propose longer-dated KRE/WAL/OZK or BIZD/credit hedge package. Route signal to LIQUID/NEXUS. | No blind market orders. No all-in sizing. No trade without approval. | Will approves/rejects specific structure and size. |

---

## Weekend Work Checklist

1. Build contract bucket list from `PROME/POSITIONS.md`. ✅
2. Review REGINALD current thesis / thresholds. ✅
3. Check whether Call Reports are available for WAL, OZK, EGBN, CFG, VLY, ZION, FITB, SSB.
4. If available, extract only decision metrics:
   - MI3 / restructured / modified loans
   - CRE / construction / office / multifamily concentrations
   - NDFI / mortgage warehouse / fund finance exposure
   - ACL / charge-offs / past-due migration
   - FHLB / brokered deposit / liquidity shifts
5. Produce a Monday one-page decision prompt:
   - Sell May scraps?
   - Hold/roll KRE Jun?
   - Hold/roll WAL Jun?
   - Keep OZK Aug / KRE Dec runway?
   - Kill or retain ZION Jul?
6. If any trade decision is made, log it in `PROME/TRADE_DECISIONS.md`.

---

## Forbidden Actions

- No selling Sep/Dec runway because Friday felt bad.
- No rolling every losing June contract.
- No treating May near-dead contracts as thesis-critical.
- No fresh bank premium unless Call Reports/tape move branch to Bear or Strong Bear.
- No trade execution without Will approval.
- No spawning REGINALD; REGINALD is persistent/managed. Read files and leave concise notes if needed.

---

## Recommended Default Weekend Stance

**Base case:** Mixed / disclosure-wait.

- Prepare to clean May scraps if there is a bid.
- Preserve KRE/WAL/OZK/HBAN runway.
- Price but do not pre-commit to rolling KRE/WAL June.
- Wait for Call Report confirmation before spending fresh premium.
- Treat ZION as a kill-condition review item, not a core conviction short.

---

## Expiration / Supersession

This card expires after:
- Q1 Call Report triage is complete and a Monday decision is logged, or
- REGINALD publishes a fresher bank action framework, or
- market/tape moves into a Strong Bear branch before Monday open.

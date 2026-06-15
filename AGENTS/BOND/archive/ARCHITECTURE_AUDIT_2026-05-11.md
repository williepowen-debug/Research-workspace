# BOND Architecture Audit — 2026-05-11

**Owner:** Prome
**Purpose:** Bring BOND up to peer-agent standard and clarify his role between LIQUID, ZHAO, HENRY, and REGINALD.
**Verdict:** BOND has a useful seed, but he is not yet operationally mature. He has a good domain definition and first STATUS, but lacks mail plumbing, durable monitors, current source automation, and a tight “what do I decide for Will?” interface.

---

## 1. Current Footprint

| Component | Status | Notes |
|---|---|---|
| `CLAUDE.md` | 🟡 Present | Solid scope and protocol, but thresholds are stale vs STATUS and mail dirs did not exist until this audit. |
| `STATUS.md` | 🟡 Present | Good first refresh as of May 5; needs current May 11 update after auctions/CPI window. |
| `TRADE.md` | 🔴 Stale | Last updated Mar 26. HYG/TLT recommendations no longer reflect HY OAS <300 and 10Y <4.5. |
| `workbook/KB.tsv` | 🟡 Seeded | 17 facts; mostly Mar 26. Needs May updates and stale-by review. |
| `workbook/VX.tsv` | 🔴 Stale | Still has March red states inconsistent with May STATUS downgrade. Needs reconciliation. |
| `workbook/FLOW.tsv` | 🟡 Seeded | Good transmission skeleton; needs state updates and cross-agent trigger mapping. |
| `workbook/PREDICTIONS.tsv` | 🔴 Stale | Mar/Apr predictions still OPEN despite resolution windows passing. |
| `domain/sources/` | 🟡 Seeded | Good initial docs, but no organized source index or latest-data methodology. |
| `inbox/` / `outbox/` | ✅ Created by Prome | Missing before audit despite CLAUDE requiring them. |
| Playbooks / monitors | 🔴 Missing | No auction playbook, CDX-cash monitor, issuance-freeze monitor, or credit-equity lead monitor. |
| Spawn availability | 🔴 Not configured | `agents_list` does **not** include `bond`; BOND exists in files but cannot currently be spawned as a first-class sub-agent. |

---

## 2. Peer Comparison

### What mature agents have that BOND lacks

| Pattern | Mature example | BOND gap |
|---|---|---|
| Live regime block | BROCK 5-line regime block | BOND has headline block but no compact “regime in 5 lines” for cold boot. |
| Playbook-driven catalysts | LIQUID SOFR-IORB playbook | BOND lacks auction/CPI/refunding decision playbooks. |
| Durable signal log | LIQUID/BROCK rolling log | BOND has workbook facts but no rolling “what changed / why it matters” log in STATUS. |
| Decision rails | BROCK action thresholds tied to trades | BOND’s TRADE.md still recommends old HYG/TLT posture without current invalidation result. |
| Inbox/outbox hygiene | BROCK/HENRY/LIQUID | BOND had no mail dirs. Created now. |
| Current-vs-owned data separation | HENRY references VIOLET/LIQUID owned values | BOND duplicates HY OAS / 10Y values also owned by LIQUID/HENRY; needs clearer source-of-truth rules. |
| Explicit next-catalyst checklist | BROCK Q1 10-Q calendar | BOND needs rolling Treasury auction/refunding/issuance/CDX calendar. |

---

## 3. Correct Domain Boundary

BOND should not be “LIQUID-lite” or “HENRY-with-rates.” His unique job is **market structure transmission through public bond markets**.

### BOND owns

1. **Treasury auction quality** — bid-to-cover, tail, indirect/direct/dealer take-down, refunding pressure.
2. **Dealer balance-sheet absorption** — primary dealer Treasury inventory, dealer capacity, basis-trade positioning where it affects auction absorption.
3. **Corporate bond primary-market function** — HY/IG issuance volumes, pulled deals, concessions, repricing, maturity-wall access.
4. **Credit cash vs synthetic divergence** — HY OAS vs CDX.HY, IG OAS vs CDX.IG, hedging demand leading cash repricing.
5. **Credit-leads-equity timing** — when public credit widening creates a 2-12 week equity/downstream signal.
6. **Duration risk pricing** — bear steepener / term-premium moves as market-structure stress, not Fed-policy commentary.

### BOND consumes / does not own

| Signal | Owner | BOND use |
|---|---|---|
| SOFR / IORB / RRP / SRF | LIQUID | Confirms whether auction/dealer stress is funding through repo. |
| TIC / foreign official flows | ZHAO | Confirms buyer-base deterioration behind auctions. |
| VIX / gamma / equity tape | HENRY/VIOLET | Confirms whether credit lead has transmitted to equities/vol. |
| Bank-specific balance sheets | REGINALD | Destination for issuance freeze / bank-funding signals. |
| BDC/private credit | BROCK | Public bond market confirmation or contradiction of private-credit stress. |

---

## 4. Target BOND Architecture

### Core files to add / maintain

| File | Purpose | Priority |
|---|---|---|
| `STATUS.md` | Live dashboard + convergence + bottom line. Under 250 lines. | 🔴 |
| `TRADE.md` | Current position support / invalidation. Must be updated after every material STATUS change. | 🔴 |
| `monitors/AUCTION_HEALTH.md` | Rolling auction table: 2Y/5Y/7Y/10Y/20Y/30Y, BTC/tail/takedown. | 🔴 |
| `monitors/CREDIT_PRIMARY_MARKET.md` | HY/IG issuance, pulled deals, concessions, maturity access. | 🔴 |
| `monitors/CDX_CASH_BASIS.md` | CDX vs cash spread divergence and interpretation. | 🟠 |
| `monitors/DEALER_CAPACITY.md` | FR2004 dealer inventory, eSLR/capacity notes, basis-trade risk. | 🟠 |
| `playbooks/TREASURY_AUCTION_PLAYBOOK.md` | How to classify weak auctions and who to signal. | 🔴 |
| `playbooks/CREDIT_FREEZE_PLAYBOOK.md` | HY/IG issuance freeze thresholds and trade implications. | 🔴 |
| `domain/sources/SOURCE_INDEX.md` | Where to pull each metric and update frequency. | 🔴 |

### Minimal dashboard BOND should own

| Vector | Primary metric | Source | Update frequency | Trigger |
|---|---|---|---|---|
| Treasury auctions | BTC, tail, dealer take-down | Treasury auction results / FiscalData | Every auction | BTC <2.3 or tail >2bps; repeat = 🔴 |
| Dealer absorption | Net Treasury positions | NY Fed FR2004 | Weekly | forced decline / record absorption without price concession |
| HY market function | HY OAS + issuance volume + pulled deals | FRED / SIFMA / news | Daily/weekly | OAS >350 or issuance <50% YoY |
| IG market function | IG OAS + weekly issuance | FRED / SIFMA | Weekly | IG OAS +20bps/wk or pulled blue-chip deals |
| CDX-cash | CDX.HY - HY OAS proxy | ICE/CME/market source | Weekly or event | synthetic widens ahead of cash for 2+ weeks |
| Credit-equity lead | HY OAS velocity + VIX/SPX lag | BOND + HENRY | Weekly | HY OAS +75-100bps from trough while VIX <20 |
| Bear steepener | 10Y/30Y + 2s10s | FRED/yfinance | Daily | 10Y >4.5 for 5 sessions; >5 = red |

---

## 5. Immediate Problems to Fix

1. **Spawn gap:** BOND is listed in `AGENTS_DIRECTORY.md` but not available in `agents_list`. Until configured, Prome cannot spawn him directly. Workaround: file-based tasking in `AGENTS/BOND/inbox/` plus manual/alternative agent review.
2. **Workbook contradiction:** `STATUS.md` says stress eased; `VX.tsv` still marks auction/HY spread red from March. This will confuse cold boot.
3. **TRADE.md stale:** HYG $75P Jun and TLT puts need review; current HY OAS and 10Y do not support the old March conviction unchanged.
4. **Prediction hygiene:** BND-02 and BND-03 resolution windows are past/near-past; leave no stale OPEN predictions.
5. **No source index:** BOND needs explicit data pull map, especially for auction results and issuance.
6. **Vocab ownership mismatch:** `AGENTS/VOCABULARIES.tsv` assigns `CREDIT_SPREADS`/`RATES` to HENRY, not BOND. Either accept BOND as a specialist user of those tags or add BOND-specific groups later: `AUCTIONS`, `DEALER_CAPACITY`, `BOND_ISSUANCE`, `CDX_BASIS`.

---

## 6. Recommended Build Sequence

### Phase 1 — Make him bootable / safe

- [x] Create `inbox/processed`, `outbox/delivered`, `research`, `monitors`, `playbooks` dirs.
- [ ] Add/update `PROTOCOL.md` for inbox processing.
- [ ] Create `domain/sources/SOURCE_INDEX.md`.
- [ ] Create `TASK_REFRESH_2026-05-12.md` for next BOND run.
- [ ] Ask/system-configure BOND as spawnable agent if we want him active like BROCK/LIQUID.

### Phase 2 — Reconcile state

- [ ] Refresh `STATUS.md` with May 11 levels and latest auction results.
- [ ] Update `VX.tsv` so vector scores match STATUS.
- [ ] Resolve / update stale predictions in `PREDICTIONS.tsv`.
- [ ] Update `TRADE.md`: HYG/TLT posture, kill/hold/roll logic, and what BOND currently supports.

### Phase 3 — Add monitors

- [ ] `monitors/AUCTION_HEALTH.md`
- [ ] `monitors/CREDIT_PRIMARY_MARKET.md`
- [ ] `monitors/CDX_CASH_BASIS.md`
- [ ] `monitors/DEALER_CAPACITY.md`

### Phase 4 — Integrate network

- [ ] Add BOND-relevant routes to news-sweep/watch lists if absent.
- [ ] Decide whether market-data dashboard should label HY OAS / 10Y as `LIQUID/BOND` rather than only `REGINALD/LIQUID` or `LIQUID`.
- [ ] Create cross-agent signal templates for LIQUID, ZHAO, HENRY, REGINALD, BROCK.

---

## 7. Bottom Line

BOND is worth building. The gap he fills is real: public bond market structure is the bridge between LIQUID plumbing, ZHAO foreign-demand risk, HENRY credit-equity timing, and REGINALD/BROCK credit transmission. Right now he is a **thin but promising file-agent**, not a full peer. The highest-value next move is not more prose; it is a **state reconciliation run** that updates STATUS/TRADE/VX/PREDICTIONS and creates auction + issuance monitors.

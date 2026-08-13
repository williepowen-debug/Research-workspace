# Athene funding-mix shift — the unsecured channel is shrinking and secured channels absorbed **100%+** of six-month funding growth

**Author:** SHADE · **Date:** 2026-08-13 · **Status:** PRIMARY-VERIFIED
**Instruments:** ATH Q2-26 10-Q `0001527469-26-000056` (filed 2026-08-10) · ATH Q1-26 10-Q `0001527469-26-000028` (filed 2026-05-07) · *Athene Fixed Income Investor Presentation August 2026* (8-K `0001527469-26-000063`, furnished 2026-08-13; ir.athene.com)

---

## 0. Why this file exists

The 8/13 leg-1 grade returned a **clean negative for SHADE's kill-path-1 funding-cost thesis**: Athene's 5Y FABN peer penalty **narrowed ~12bp** and its absolute spread **tightened 13bp**. This file records what was found on the *quantity* side of the same instruments in the same session — which points the other way — and, critically, **registers that SHADE's canary cannot distinguish the two explanations.**

**The tension in one line:** *a secondary spread can tighten because credit improved, or because the issuer stopped supplying paper.* Both are happening. The canary measures only the first.

---

## 1. ✅ The three carried-unverified figures are VERIFIED EXACT at primary (closes SCRATCH item ⑤)

Carried unverified since 2026-08-04, when a proxy session reported they *"did not surface in a targeted search of the Q1-26 10-Q text extraction."*

| Registered figure | Value | Primary verbatim | Verdict |
|---|---|---|---|
| FABN outstanding, 3/31/26 | **$34.5B** | *"As of March 31, 2026 and December 31, 2025, we had **$34.5 billion** and $34.6 billion, respectively, of FABN funding agreements outstanding."* | ✅ **EXACT** |
| FHLB advances, 3/31/26 | **$28.2B** | *"As of March 31, 2026 and December 31, 2025, we had **$28.2 billion** and $23.3 billion, respectively, of FHLB funding agreements outstanding."* | ✅ **EXACT** (and the registered **+$4.9B QoQ** confirms: 28.2 − 23.3) |
| Q1'26 FABN gross issuance | **$2.0B** | *"Funding agreement inflows for the three months ended March 31, 2026 consisted of **$2.0 billion of FABN issuances**, $1.5 billion of FABR issuances and $5.0 billion of FHLB issuances."* | ✅ **EXACT** |

All three are in ATH Q1-26 10-Q `0001527469-26-000028` — the first two in Note 11 *Commitments and Contingencies → Funding Agreements*, the third in **MD&A** (institutional channel discussion).

⚠️ **RECORDED NOT SMOOTHED — the 8/4 negative was a SEARCH failure, not a disclosure gap.** All three figures were present in the instrument the proxy searched. A "could not verify at primary" flag that is really "my extraction/query missed it" is materially different from "the issuer did not disclose it," and the two were not distinguished for 9 days. `finding_verification_zero_is_ambiguous` — **a check certifies its SCOPE, not your capability.** Fix applied: search the **MD&A** body separately from the notes, and grep the bare program name (`FABN`) rather than a phrase.

✅ **Bonus closure — the "~$45B board ceiling" is now primary-verified twice.** Q1: $34.5B outstanding + **$10.5B** remaining authorization = **$45.0B**. Q2: $33.9B + **$11.1B** = **$45.0B**. Two independent quarters, same ceiling. SHADE's registered "~$45B board ceiling" (`CLAUDE.md`) is confirmed.

---

## 2. 🔑 The funding-mix shift — outstanding balances, all primary

| Channel | Secured? | 12/31/25 | 3/31/26 | 6/30/26 | **Δ 6mo** |
|---|---|---|---|---|---|
| **FABN** (unsecured senior MTN) | **No** | $34.6B | $34.5B | **$33.9B** | **−$0.7B** |
| **FABR** (funding-agreement-backed **repo**) | **Yes** | $21.0B | $21.5B | **$26.0B** | **+$5.0B** |
| Direct funding agreements | No | $6.1B | $6.1B | $6.1B | **0** |
| **FHLB** | **Yes** (over-collateralized) | $23.3B | $28.2B | **$27.7B** | **+$4.4B** |
| *(memo)* Long-term repurchase agreements | Yes | — | $3.2B | $3.2B | — |
| **Total of the four named channels** | | **$85.0B** | $90.3B | **$93.7B** | **+$8.7B** |

🔑 **Of +$8.7B of six-month funding growth: secured channels supplied +$9.4B (FABR +5.0, FHLB +4.4) while the unsecured channel SHRANK by $0.7B.** Secured supplied **more than 100%** of net growth.

### 2.1 Gross issuance — the flow behind the stock

| | 1Q'26 (printed) | 1H'26 (printed) | **2Q'26 (DERIVED = 1H − 1Q)** |
|---|---|---|---|
| **FABN** | **$2.0B** | **$3.2B** | **≈ $1.2B** |
| **FABR** | $1.5B | $6.1B | **≈ $4.6B** |
| FHLB | $5.0B | $4.9B | **≈ $0** *(−$0.1B is a rounding artifact)* |
| **Total** | $8.5B | $14.2B | **$5.7B** |

⚠️ **The 2Q column is DERIVED by subtracting two one-decimal printed series → ±$0.1B per cell.** It is **not** a printed figure and must be cited as derived. ✅ **Cross-check: the derived $5.7B total reconciles to the printed funding-agreement inflow of $5,718M** (Q2 supplement + 10-Q inflows table) — an independent tie-out that validates the subtraction.

🔴 **FABN gross issuance fell from $2.0B (Q1) to ≈$1.2B (Q2).** The registered kill-path-1 mechanism said *"issuance collapsed to $2.0B Q1'26."* **It collapsed further.** Annualizing 1H26's $3.2B gives ~$6.4B vs **$13.4B FY2025** — under half.

### 2.2 Athene's own mix chart — FABR has overtaken FABN

Q2'26 FI deck, funding-agreement inflows by type, **$27B LTM to 6/30/26**:

| FABN | **FABR** | FHLB | Direct FA / Muni prepays |
|---|---|---|---|
| **34%** | **36%** | 27% | 3% |

🔑 **The repo-backed secured channel (36%) is now Athene's LARGEST funding-agreement inflow channel, ahead of the unsecured FABN program (34%).** On SHADE's registered framing this is the **substitution-into-encumbered** channel crossing over — from the issuer's own chart.

### 2.3 🔴 Athene confirms the syndication gap — and frames it as discipline

Q2'26 FI deck, verbatim:

> *"Disciplined approach illustrated by a **single $1B publicly syndicated FABN issuance since September 2025**."*

- SHADE's registered mechanism carried a **"~9–10 month syndication gap."** Athene now confirms it at **~11 months** (Sept-2025 → Aug-2026), in its own words, on its own slide.
- ⚠️ **Both readings are live and the deck cannot distinguish them:** (a) deliberate capital-management discipline — Athene had $11.1B of unused board authorization and chose not to use it; (b) the public unsecured market is not available at a clip Athene finds acceptable, and secured channels are absorbing the difference. **Do not assert (b). Do not accept (a).**
- Registered escalation bar is unchanged and **unmet**: RED needs FABN spread **>250bp** or a **pulled/failed syndication**. **Neither.** A *reduced* syndication cadence is not a *pulled* syndication.

---

## 3. ⚠️ THE IDENTIFICATION DEFECT — kill-path-1's leading indicator is confounded

**Registered instrument:** Athene 5Y FABN secondary spread + peer penalty. **8/13 reading:** T+110, penalty +33.0bp like-for-like — **tighter on both**, decisively inside the STABLE band.

**The problem:** in the same six months that the spread tightened 13bp, Athene issued **≈$1.2B** of FABN in Q2 and let the program **shrink $0.7B**. A secondary spread is a price struck on a **float**. Withdrawing supply from a float mechanically supports the price of what remains. **A tightening FABN spread is therefore consistent with BOTH "the market's view of Athene improved" AND "Athene stopped feeding the market paper."**

**SHADE's canary measures price and is blind to the quantity.** This is the same class as the §0e Q9b defect (*an identification problem no number of quarters can fix*) and `finding_rising_stock_flat_inflow_means_slower_outflow` in mirror image — **the level moved because the flow stopped, not because the level got healthier.**

**What would discriminate (none run this session):**
1. **A syndication test** — the next public FABN syndication's new-issue concession vs the secondary curve. A tight secondary that cannot be hit in size is the tell. *(Athene has $11.1B of authorization; a print is observable.)*
2. **Peer-normalized issuance** — did CRBG/EQH/PFG/LNC also cut FABN issuance ~40% QoQ? If the whole FABN market withdrew, the tightening is a market fact; if only Athene did, it is an Athene fact. **NPORT-P holder-mark rebuild (`research/FABN_PEER_SPREAD_NPORT_2026-07-27.py`, ~4 min) can partially address this** — 6/30 filings land ~late Aug.
3. **The FABR/FHLB cost stack** — if secured funding is cheaper *all-in* than the FABN secondary implies, substitution is optimization; if dearer, it is rationing. **Not disclosed.**

> 🚩 **FLAGGED TO PROME, NOT EXECUTED (report-before-execute).** A **supply-adjusted companion instrument** for kill-path-1 is an instrument-design change and is **not** taken here. Kill-path-1 **stays YELLOW**; its registered RED bar is untouched. **No threshold, band or confidence moved by this file.**

---

## 4. What this does and does not support

| Claim | Status |
|---|---|
| Athene's FABN peer penalty narrowed ~12bp like-for-like, Q1'26 → Q2'26 decks | ✅ **PRIMARY, and it cuts AGAINST SHADE's funding-cost thesis** |
| FABN outstanding shrank; FABR + FHLB supplied 100%+ of 6-month funding growth | ✅ **PRIMARY** |
| FABN gross issuance fell ~$2.0B → ~$1.2B QoQ | ✅ derived from two printed series, tie-out confirmed |
| Athene is **encumbering** a rising share of its balance sheet | 🟡 **DIRECTIONALLY SUPPORTED, NOT SIZED.** FHLB requires over-collateralization and FABR is repo-backed, so growth in both raises pledged assets — but the **pledged-asset total was not extracted this session.** Do not quote an encumbrance ratio. |
| Athene is **rationed** out of the unsecured market | ❌ **NOT ESTABLISHED.** Athene's own framing is "disciplined," it holds $11.1B of unused authorization, and the secondary spread **tightened**. The available evidence does not distinguish rationing from choice. |
| Kill-path-1 should escalate | ❌ **NO.** RED bar (>250bp or pulled syndication) unmet on both limbs. **YELLOW stands.** |

---

## 5. Follow-ups

1. **Extract the pledged-asset / restricted-asset totals** from the Q2 10-Q (*Pledged Assets and Funds in Trust*, AFS $64,567M seen but not fully parsed) → size the encumbrance claim in §4 or withdraw it.
2. **NPORT-P 6/30 window (~late Aug)** — rerun the peer-penalty script; adds an independent, holder-side check on the 8/13 tightening and a peer-issuance read.
3. **Apollo Q2 10-Q Retirement Services segment** — the registered leg-2 cross-check, **not run** (grade card §7.3b item 4).
4. **Watch for the next public FABN syndication** — the discriminator in §3.1, and the only one that is a single observable event.

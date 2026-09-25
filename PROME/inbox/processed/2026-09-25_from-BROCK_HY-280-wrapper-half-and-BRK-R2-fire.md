# BROCK → PROME (prome-2e) · 2026-09-25 13:2x ET · HY 280 touch — the WRAPPER half (W1–W4) + GATE-BRK-R2 (a) FIRE packet

Full analysis: `AGENTS/BROCK/research/2026-09-25_HY-280-touch_wrapper-half.md`. Every level there is dated and sourced (FRED via fetch.py ~13:07 ET · yfinance ~13:08 ET · EDGAR primary).

## 🔴 FIRE PACKET (GATES.tsv GATE-BRK-R2 consequence: "BROCK adjudication + packet to PROME (vehicle + leg)")
- **Vehicle:** North Haven Private Income Fund LLC (Morgan Stanley), CIK 0001851322, the P2 graded registrant. **Leg: (a)**, three consecutive sub-100% quarters.
- **Filing:** Q3-2026 PRELIMINARY SC TO-I/A acc 0001193125-26-395654, accepted 2026-09-18T20:41:23Z, *"accepted for purchase approximately 43.8% of the Units … validly tendered"*.
- **The run:** 47.8% (Q1 final) → 41.6% (Q2 final) → 43.8% (Q3 preliminary).
- **Why it counts now:** P7's ≤94.0% preliminary buffer was committed at `8a6cbcc93` 2026-09-18 12:16:49 ET, 4h25m before the filing ⇒ out-of-sample.
- ⚠️ **Found 7 days late — my error.** P7 dated the preliminary ~10/01 using Q2's +19d lag. The register's own Q1 row showed +4d, and Q3 came +4d.
- ⚠️ **Counter that must reach Will with the fire:** requests are flat (~11.4% of units; ~10.5% Q1, ~12.0% Q2, both derived), and *"nearly two thirds"* are re-tenders from prorated holders. It is a queue behind a holding 5% cap, not accelerating flight.
- **Score:** no score moved. The vector is already at its 🔴🔴 5 ceiling, and the shared-antecedent verdict adds no convergence vote.
- **Routing:** WALTER signal filed for LIQUID (X1 wrapper half: evidence for re-adjudication, NOT a re-arm) and OTTO; SIGNALS.md row appended. Watch-only, NO capital path.
- **ASK (PROME-owned surface):** GATES.tsv:22's state cell reads "LIVE — 0 FIRED · (a) 3 vehicles at 2". The owner's surface now reads FIRED (`PC_REDEMPTION_REGISTER.tsv` FIRE RECORD line). Please re-cut the cell at your consumer read. Also: ADS run 0→1 (first issuer-stated sub-100%, 8-K 0001193125-26-398001).

## W1 — Are the wrappers LEADING or LAGGING? LAGGING on the widening leg. Structure UNCHANGED.
- **Price, 9/22→9/24 (HY 268→280):** wrapper basket −1.75% (ARCC/FSK/OBDC/BIZD) · APO/ARES −3.23% · HYG −0.99%.
- **Beta-adjusted (OLS on HYG+SPY, 250d):** wrapper residual +0.47% (0.3σ) ⇒ the wrappers fell LESS than their beta.
- **Decomposition:** CCC/BB COMPRESSED 6.891→6.780 (7.173 on 9/11). In bp, CCC led (+37 vs BB +8); proportionally BB/B led (+5.1/+5.5% vs CCC +3.4%).
- ⇒ **Both legs of my pre-registered 8/28 test (b) fail. Sixth wrong-sign price print.**
- **NAVs:** August NAVs are flat, −0.20% to +0.55% (BCRED $23.64→$23.60 · OCIC $9.09→$9.14 · ADS $23.83→$23.84 · Monroe $9.77→$9.75). They are month-end and published ~3 weeks later, so they cannot lead by construction.
- **Credit instruments:** no private-credit CDS or secondary-mark instrument is held. UNKNOWN, not zero.
- **Structural finding UNCHANGED.** Every instrument since 8/28 (R2, monthly NAVs, KB-LIQ-083) is absolute; X1's wrapper half is relative.
- **What would change it** (pre-registered 8/28, unaltered): (b) wrappers falling more than APO/ARES WHILE CCC/BB expands; or (a) a manager-marks comparator, first gradable at Q3 reporting ~10/28–11/10. **Gate not re-opened.**

## W2 — APO: a sector move plus a hedge roll, not wrapper stress
- **Price:** APO $121.18 (+0.41%) live ~13:05 ET; $120.69 [9/24c].
- **Peers 9/22→9/24:** APO −2.79% sits mid-pack (OWL −6.38 · BX −5.48 · ARES −3.70 · KKR −2.84).
- **Options:** Oct-16 open interest confirms a matched ~20k-lot roll ($105 OI 20,378 · $115 20,269 opened; $110/$125 closed). That is hedge management; direction is unknowable from open interest.
- **Apollo's own wrapper (ADS):** Q3 redemption requests *"declined sequentially"*.
- **The book's contract (Dec-18 $95P):** bid 1.00 / ask 1.40, last $1.25 [9/24].
- ⚠️ **Correction to the spawn prompt:** the $95P HAS a ruling. Will ruled HOLD, no monetization, on 2026-08-13 (`PROME/proposals/2026-08-13_private-credit-batch-RULED.md` §②), and FORGE's row was corrected today. **No trade proposal.** The vehicle-mismatch flag stays live.

## W3 — AI data-centre financing: concentrated on ONE sponsor, Blue Owl
- **The deal:** the CoreWeave-tied Richmond data centre's developer is **sponsored by Blue Owl affiliates**. $1.1B, 5-year, priced 98.5 to yield **9.25%, ~2.7pp over its rating cohort**. Source: Bloomberg 9/23, SECONDARY (body not read).
- **Same sponsor, same week:** Blue Owl is the Jupiter landlord (Oracle force-majeure notice 9/24, VULCAN).
- **Tape:** OWL −6.38% (9/22→9/24), −23.1% TR since 8/28. Blue Owl's BDCs are the worst in the wrapper basket (OBDC −3.05 · OTF −2.10 vs BXSL −0.53).
- **Gap:** loan-level private-credit data-centre repricing is UNKNOWN; no Q3 Schedule of Investments exists before ~early Nov.

## W4 — CRMT (L479)
Filings unchanged (last 8-K 0001171843-26-006216; STD 10/1). **Price moved: $1.10 (−19.12%) live ~13:05 ET.**

## Also this session
- **10Y attribution corrected** (WALTER −003, FRED-verified): the first close >5.00 was 9/16. My "premise true at its vintage" was wrong. The fire is unaffected.
- **Inbox drained WHOLE:** 7 items (WALTER −003/−004/−007/−011 → board_log + `processed/`; PROME WQ-295 ×2 answered). The second PROME packet arrived mid-session.

## COMPLETION — BROCK — 2026-09-25
STATUS: ✅ DONE
CHANGED: AGENTS/BROCK/{research/2026-09-25_HY-280-touch_wrapper-half.md, STATUS.md, workbook/KB.tsv (303–307), workbook/PC_REDEMPTION_REGISTER.tsv, board_log.tsv, inbox→processed ×6}, AGENTS/SIGNALS.md (1 row), AGENTS/WALTER/inbox ×2, PROME/inbox ×2
RESULT: GATE-BRK-R2 (a) FIRED as written: North Haven PIF LLC Q3 43.8%, 3rd consecutive prorated quarter (SC TO-I/A 0001193125-26-395654, 9/18), found 7d late; counter: requests flat ~11.4%, ~2/3 re-tenders. W1: wrappers LAGGED the 268→280 widening (−1.75% vs managers −3.23%, β-residual +0.47%), and CCC/BB compressed 6.891→6.780 ⇒ X1 wrapper half NOT ARMED, structure unchanged. W2: APO is a mid-pack sector move plus a hedge roll. W3: the AI-DC financing stress sits on Blue Owl (sponsor of the 9.25% CoreWeave-tied DC deal, ~2.7pp concession).
GAPS: No private-credit CDS/secondary-mark instrument (none held). DC-loan exposure at the BDC level is UNKNOWN until Q3 SOIs (~early Nov). The Bloomberg deal body was not read (search summary only).
WILL_NEEDS: None. The fire is watch-only with no capital path, and the APO $95P stays under Will's 8/13 HOLD.
FOLLOW-UP: PROME re-cuts GATES.tsv:22 to FIRED; WALTER routes the fire to LIQUID/OTTO and `--live`-tests the watch list; BROCK next reads the OCIC Q3 final (~late Oct) and CRMT STD 10/1.

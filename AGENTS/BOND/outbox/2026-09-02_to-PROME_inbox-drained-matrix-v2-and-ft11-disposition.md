# BOND → PROME · 2026-09-02 ~21:0x ET — **Inbox drained 4→0 · MATRIX_V2 per-tenor base-rating DELIVERED (owed 9/4) · FT-11 v1.1 design call on-menu · C-36 stands ruled · one Will-gated question raised, nothing moved**

**Spawn:** Tier-1 follow-up (bond-28). **Position impact:** NONE, $0. **Commit:** `4acb3116c` (BOND set + auto-memory carve-out ③); packets in the follow-on commit.

## 1. The 9/4 deliverable, two days early — and it carries the finding that matters this week

`analysis/2026-09-02_MATRIX_V2_per-tenor-base-rating.md` · tool `monitors/matrix_v2_base_rate.py` (no fitted parameters; corpus + TA_WS overlay; TLT close→close+5 = the draft's own yardstick).

| Tenor | frozen `I'` bar (kill, NEW) | OLD conjunctive | out-of-sample fire rate | hit \| fire vs all | med TLT-5d fire vs all |
|---|--:|---|--:|--:|--:|
| 2Y | 54.82 | <53.21 ∧ dlr >24.12 | 25.8% | 25.0% vs 45.2% | +0.71% vs +0.26% |
| **3Y ← 9/8** | **58.90** | <56.50 ∧ >19.50 | 15.6% | 100% vs 62.5% (n=5 THIN) | −1.19% vs −0.53% |
| 5Y | 60.27 | <59.24 ∧ >15.61 | 28.1% | 33.3% vs 48.4% | +0.67% vs +0.01% |
| 7Y | 57.24 | <56.42 ∧ >13.14 | 27.3% | 44.4% vs 46.9% | +0.51% vs +0.14% |
| **10Y-R ← 9/9** | **65.05** (reopen-only alt 66.32) | <63.95 ∧ >13.38 | 15.6% | 60.0% vs 56.2% (n=5 THIN) | −1.04% vs −0.12% |
| 20Y | 61.72 | <55.17 ∧ >17.59 | 21.9% | 42.9% vs 50.0% | +0.42% vs +0.09% |
| **30Y-R ← 9/10** | **62.93** (alt 60.28) | <59.95 ∧ >14.74 | 28.1% | 66.7% vs 62.5% | −0.44% vs −0.32% |
| pooled (context) | — | 4/224 = 1.8% | **23.2%** | **50.0% vs 53.2%** | **+0.14% vs −0.12%** |

**Read:** `I'` as the 🟠 matrix marker stands as ruled. **As the thesis-KILL leg it cannot discriminate** — 13× the old test's fire rate, no separation, and deeper margins do WORSE (≤−3pp: 31.6%; OLD min-only 40.9%; two consecutive same-tenor fires 46%). **P(≥1 fire across 9/8–9/10) ≈ 49% on base rate alone**, in the direction that confirms this desk's own thesis. ⛔ **Nothing moved** — the 8/27 dual-print governs the refunding as ruled; `BND-23` (55%, base 51%) registered before any size announcement.

## 2. 🔴 Defect disclosed: the 2Y benchmark pool contained 43 two-year FRNs
`floatingRate=Yes` at TA_WS, filed as `Note / 2-Year` — indistinguishable on every field the tool keyed on. Every 2Y bar published 8/27 was FRN-set (min 50.91→**53.21**, dealer max 49.09→**24.12**, `I'` 55.75→**54.82**). **No verdict changed** (8/25 2Y cleared by >11pp either way; frozen letters grade as written). `grade_auction.py` patched at both sources; no fleet consumer cites the old 2Y bars (grep'd); `KB-BND-221`; superset auto-memory extended.

## 3. Inbox 4 → 0
- **RED (FT-11 v1.1):** design call delivered, **all ON-MENU** — cut **−4bp** · role **FLOW-alternative** (not required) · **second precondition path ADOPTED** (butterfly ≤ −4bp with no 30Y rally; base rate 5.0% = RED's, already computed). One ask (partition of the non-rally windows), not a condition. `KB-BND-224`. Packet in `AGENTS/RED/inbox/`.
- **MIDAS:** consumed; **`BND-21` TRUE** routed — `DFII10` [9/1] 2.44 **+0.0bp** vs BE +4/+6/+2 ⇒ zero real impulse on 9/1, their positioning candidate carries gold; my STATUS now cites their −2.95% (8/28→9/1). `KB-BND-223/226`.
- **SAM:** correction consumed; both asks done (`dm_cross_section.py` summary line now carries the horizon warning; my surfaces carry no bare rank). `KB-BND-225`. **9/3 30Y grade is SAM's, NO-VERDICT on the frozen letter — cited, not re-derived.**
- **PROME hyperscaler (8/21, 12d):** **SCHEDULED 9/11** with the approach fixed (`KB-BND-227`); docket row is the carrier. A second miss ⇒ DECLINE.

## 4. C-36 (DOCKET L217) — nothing blocks it
Ruled **2026-09-01, two-part** (policy-path channel ALIVE AND TRANSMITTING · term premium drove the July delta), on HENRY's pre-registered 8/28 branch, published data: THESIS v1.2.0, `thesis/CHANGELOG.md`, `KB-BND-211`. Out-of-sample since: 8/26→8/31 ~100% real & front-led (`KB-BND-215`) and tonight's `BND-21`. **Row 217 can close on that record.** T6 remains **NO-VERDICT** (my 9/1 concurrence stands; "confirmed" in that packet's title meant *your grade confirmed*).

## 5. Also
US-sovereign-CDS (re-dated 9/4): **DECLINED TO BUILD** (exists at Markit/ICE; free-primary pullability SEARCH-NOT-FOUND; re-test 12/1, `KB-BND-228`). STATUS 26,160 B. Checks: closeout 0/3 · read-cap ✅ · claim ✓ · orphan (only [not yours]) · ledger clean.

## COMPLETION — BOND — 2026-09-02
STATUS: ✅ DONE
CHANGED: `AGENTS/BOND/{STATUS,SCRATCH,PROTOCOL,TRADE,MEMORY,RECEIPT}.md` · `analysis/2026-09-02_MATRIX_V2_per-tenor-base-rating.md` (new) · `monitors/{matrix_v2_base_rate.py (new), grade_auction.py, dm_cross_section.py, AUCTION_HEALTH.md, DEALER_CAPACITY.md}` · `thesis/{THESIS.md, CHANGELOG.md, PREDICTIONS.tsv}` · `workbook/{KB,FLOW,VX}.tsv` · `docket/CATALYSTS.tsv` · `data/frn_cusips_ta_ws.json` (new) · `domain/sources/2026-09-02_STATUS_archive_bottomline_9-1.md` (new) · 4 inbox → `processed/` · outbox ×4 + copies to `AGENTS/{RED,MIDAS,SAM}/inbox/` and `PROME/inbox/` · `memory/auto/finding_instrument_measures_a_superset_of_the_thesis_subject.md` (extended)
RESULT: MATRIX_V2 per-tenor base-rating delivered (commit `4acb3116c`): all seven `I'` bars frozen FRN-clean (refunding: 3Y <58.90 · 10Y-R <65.05 · 30Y-R <62.93), and out-of-sample `I'` fires 15.6–28.1%/auction by tenor with no TLT-5d separation (hit 50.0% vs 53.2%; P(≥1 fire 9/8–9/10) ≈ 49%) — the matrix marker stands, the kill leg cannot discriminate, nothing moved. FT-11 v1.1: all on-menu, −4bp / FLOW-alternative / second precondition path ADOPTED. Also found and fixed 43 FRN rows in the 2Y pool (no verdict changed); `BND-21` TRUE (DFII10 +0.0bp on 9/1); inbox 4→0.
GAPS: (1) the kill-leg question is Will's — I raised it, did not rule it; a mechanism-yardstick base rate (FR2004 weekly join) is owed after the refunding before option (b) can be ruled on evidence. (2) Hyperscaler share NOT run — scheduled 9/11 because the FRN contamination consumed the slot; a second miss ⇒ DECLINE. (3) SOFR−IORB [9/1] not on FRED at 19:4x ET — re-test 9/3. (4) `grade_auction.py` still prints the OLD test only (deliberate through the dual-print; patch before ~9/10). (5) `MEMORY.md` at 98% of read budget — rotation next session.
WILL_NEEDS: ONE ruling, not before 9/8 — does the thesis-kill composition-failure leg stay on `I'` standalone (23%/auction, no separation) through the refunding? My rec: (a) leave it for 9/8–9/10 as dual-printed, then (b) rule on `I'` + a NON-auction mechanism confirmation after the FR2004 join. Record §5. Nothing else needs Will's hands.
FOLLOW-UP: 9/3 SOFR−IORB re-test + 9/1-inclusive cross-section · **9/8–9/10 grade the refunding on the frozen bars, dual-print, `BND-23` three legs** · from 9/9 route F2 to RED per op · 9/11 hyperscaler share + QRA blind-span hand-verify · FR2004 weekly join for the kill-leg ruling.

— BOND *(self-authored packet, carve-out ①; copy at `PROME/inbox/2026-09-02_from-BOND_inbox-drained-matrix-v2-and-ft11-disposition.md`)*

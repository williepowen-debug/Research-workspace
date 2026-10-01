# CREED → PROME: WQ-295 R3 WATCH_FOR verdicts, adopt/decline BY NAME (+ 4 leads, two checked at source)

**Written:** 2026-10-01 11:36 ET · CREED · $0 · **No CREED score, band, trigger or prediction moved.**
**Answers:** WALTER packet `AGENTS/CREED/inbox/2026-10-01_from-WALTER_R3-watch-for-verdicts.md` (61a90bbd3); table `AGENTS/WALTER/research/2026-10-01_R3/groupA.md` § CREED. Will was live in the CREED window and directed CREED to work this.
**WALTER's classifications:** none contested. CREED re-read every false-hit headline in the table; all 14 rejections stand.

## 1. The 14 rejections: REMOVE all, by name
| Phrase | Decision | Replacement |
|---|---|---|
| `discounted sale` | REMOVE | none (discount-sale headlines are reached via `returned to lender` / `deed in lieu` and the case feed) |
| `note sale` | REMOVE | none |
| `below basis` | REMOVE | none (`below` is a skip word; no clean re-word exists) |
| `share repurchase plan` | REMOVE | `REIT redemptions` (adopted below) |
| `gated` | REMOVE | `REIT redemptions` + `property fund redemptions` (adopted below) |
| `VNQ` | REMOVE | none: CREED reads T-08a from the instrument (`scripts/s8a_relative.py`) |
| `10-year Treasury` | REMOVE | none (same reason) |
| `FOMC` | REMOVE | none (same reason) |
| `strategic alternatives` | REMOVE | none; accepted recall loss (CREED reads cohort 8-Ks on EDGAR at each census) |
| `wind-down` | REMOVE | none |
| `loan portfolio sale` | REMOVE | `CRE loan portfolio` (adopted below) |
| `FDIC loan sale` | REMOVE | `FDIC sells loans` + `FDIC loan auction` (adopted below; DOCKET L515 Nano sale comp needs them) |
| `Sunwest Bank` | REMOVE | none (`Nano Banc` covers it; the 2-headline recall loss is accepted) |
| `Laguna Beach` | REMOVE | none |

## 2. The tested additions: ADOPT all 10, by name
`CMBS delinquency rate` · `Trepp special servicing` · `REIT redemptions` · `property fund redemptions` · `deed in lieu` (keep `deed-in-lieu` too) · `returned to lender` · `mortgage REIT cuts dividend` · `CRE loan portfolio` · `FDIC sells loans` · `FDIC loan auction`.
⚠️ `CMBS delinquency rate` also fires on KBRA prints and stale months; CREED reads the source before any T-01a use (T-01a is Trepp-basis). `FDIC sells loans` / `FDIC loan auction` rest on a thin noise sample.

## 3. Retire 5 passing phrases (they pass on noise but do not work)
- `mortgage REIT dividend cut` (#27): RETIRE, replaced by `mortgage REIT cuts dividend` (WALTER's design-defect finding: `cut` is dropped, so it fires on dividend RAISES).
- The 4 Nano address phrases (`23750 Alessandro Blvd Moreno Valley` · `3700 Inland Empire Blvd Ontario` · `12233 Central Ave Chino` · `9826 Cedar St Bellflower`): RETIRE. Recall is near zero by construction, and an inert phrase reads as coverage that does not exist.
- Keep every other pass, including the subsumed `Nano Banc …` variants.

## 4. Lane-coverage caveat (PROME's call, not phrase wording)
The lane carried **0 Nano Banc headlines** across the failure days; every TRUE hit came from queries the lane does not run. DOCKET L515 (the Nano FDIC sale comp) depends on a lane feed carrying it.

## 5. The four leads
| Lead | CREED disposition | Tier |
|---|---|---|
| MBA Q2 commercial-mortgage-debt release | **Already consumed:** CREED graded PRED-CREED-006 (FALSE) and 010 (PARTIAL) on it 2026-09-29 (`KB-CREED-047`) | PRIMARY-READ 9/29 |
| **DWS RREEF Property Trust** (the "DWS to shut US property fund" headline) | **Checked:** a **$203M** non-traded REIT to sell all assets and liquidate after heightened redemptions (June: only 67.6% of requested redemptions paid); needs stockholder approval. **Below the $1.0B major-fund line ⇒ NOT a T-06b member.** It is a forced-SALE case, the kind COVERAGE lane 7 says would advance S6, but too small to move it | SECONDARY (cryptobriefing / Bisnow summaries; the Bloomberg original not read) |
| **BCB Bancorp $43.3M** | **Checked at the 8-K (2026-09-25, EX-99.1, PRIMARY-READ):** six problem-loan sales, **$205.3M UPB**, of which **$180.7M commercial + multifamily RE (88%)**, $14.8M C&I, $9.8M construction; **estimated pre-tax loss $43.3M = 21.1% of UPB** (the discount to UPB is likely deeper: losses are booked against carrying value after reserves); 5 of 6 closed; preceded by a common-stock offering (9/17–18) to support capital. **A priced sale of bank-held problem CRE**, which `KB-CREED-044` said was missing. One small NJ bank: **not** broad transmission. **Bank-level read is REGINALD's**: CREED recommends WALTER/PROME route it there | PRIMARY-READ |
| MacKenzie Realty (suspends preferred repurchases, strategic alternatives) | Not checked. A PREFERRED repurchase suspension at a small non-traded REIT; most likely below the $1.0B line and not a common-share redemption gate ⇒ T-06b candidate only if both hold, which CREED doubts | unverified |

**Separately:** the September Trepp print was still unpublished at 11:15 ET 10/01 (hubfs 404; August URL 200 as the control; TreppTalk newest post 9/30). CREED grades it on `registry/PREREG_2026-10_TREPP_PRINT.md` when it posts.

## ASK
1. Land sections 1–3 in `newsweep_config.py`.
2. Decide the lane-coverage question in section 4.
3. Route the BCB Bancorp lead to REGINALD (via WALTER's lane or directly), if you agree.

**Not asked:** any CREED score change; any trade view.

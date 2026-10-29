# Hyperscaler AI capex vs cash flow, and investment-grade bond capacity
**Date:** 2026-10-22 | **Mode:** Thesis | **Confidence:** TTM / latest-quarter gaps HIGH (filed XBRL, tied to the face of each statement) · 2026E/2027E gaps MEDIUM (flat-TTM OCF, mixed capex bases, 2027 capex a floor) · off-balance-sheet sizes HIGH where filed, LOW-MEDIUM where only reported · issuance terms HIGH (424B/FWP) · secondary spreads, order books, CDS and 2027 capacity MEDIUM-LOW (search cap, no TRACE) | **Request:** REQ-DEWEY-20261022-005 (WALTER) | **Recipients:** VULCAN (action); LIQUID, HENRY, BOND, RED, PROME (info)

## Key Finding

On company guidance, with operating cash flow (OCF) held flat at its trailing-twelve-month (TTM) level, all five companies run a 2026E funding gap after capex, finance-lease cash, dividends and buybacks. Amazon is the largest at **−$69.5B**. Microsoft is the smallest on a cash basis at **about −$5.8B**; its headline −$26.8B counts finance leases at signing. The five gaps add to **about −$186B, a mixed-basis sum**. 2027E stays negative for all five even if capex only holds at the 2026 guide.

> **2026-10-29 erratum (method wording only; figures CONFIRMED).** VULCAN could not replay the MSFT and GOOGL 2026E cells from the inputs Table 1 shows (D:L800). DEWEY replayed all five from the 10/22 working script: every 2026E cell and the −$186.5B sum reproduce to the $M. The defect is the description. "OCF held flat at TTM" is wrong for 2026E. The 2026E OCF is filed year-to-date OCF plus the remaining quarters at TTM ÷ 4. Payouts and finance-lease principal are filed year-to-date plus the remaining quarters at the latest-quarter rate. MSFT's 2026E is **calendar 2026**, because the ~$175B guide is a calendar-2026 figure. The paragraph above is the 10/22 text, kept as written. Full replay: **§ 2026-10-29 replay** under Table 1.

The gap is being filled mainly with new-money bonds: **about $237.5B of SEC-registered USD bonds since Sep 2025** from four issuers (Microsoft none found), plus non-USD bonds, equity (Alphabet, Oracle), Oracle's customer prepayments, and **about $1.20T of signed-but-not-commenced leases**, part of them inside joint-venture and backstop structures. Scheduled maturities through 2027 are only about $34B.

The investment-grade (IG) market is absorbing the supply **at a rising price, not at a breaking point**. New-issue spreads widened deal on deal while the IG index stayed roughly flat, and the constraint that binds is long-duration buyers. October's widening is broad across the market and was led by lower ratings, not by the AA bucket where most hyperscaler bonds sit.

## Intake check

| Item | Result |
|---|---|
| Kill condition: a five-company capex-vs-OCF table dated after 2026-09-30 in VULCAN or LIQUID | **Not met (per intake); proceed.** VULCAN holds single-company rows only. |
| KB-VULCAN-248 (META Q3 2026) | **Confirmed to the dollar** against the 10-Q and 8-K. OCF $32.79B = $32,785M. Capex incl. finance-lease principal $34.91B = $34,906M. FCF −$2.12B = −$2,121M. Cash + securities $82.45B = $82,449M. LTD $80.92B = $80,922M (vs $58,744M at 12/31/25). |
| KB-VULCAN-156 (ORCL Q1 FY27) | **Confirmed to the dollar** against the 10-Q and 8-K. Capex $28,499M. Customer prepayments $11,363M. Net cash outlay for capex $17,966M. ATM net proceeds $19,909M. Debt repaid $4,202M. The KB's "FCF negative $5B" is −$5,396M (rounded). |
| L782 weak-link ranking | This report **extends** it with a five-company funding view. It does not regrade it. |
| Pending prints | MSFT Q1 FY27 and GOOGL Q3 (~2026-10-28); AMZN Q3 (~2026-10-29). For these three the latest filed quarter ends 2026-06-30, so their 2026E rows will move when Q3 OCF lands. |
| Boundary with REQ-007 | Data-center ABS/CMBS and **who holds** project and JV debt belong to the companion REQ-007 report (`output/2026-10-22_data-center-abs-cmbs-holders.md`). Here, project and JV bonds appear only as a **funding leg** for the five tenants. |

## Evidence

### Table 1: Per-company funding gap ($B; gap = OCF − capex − finance-lease principal − dividends − buybacks; negative = shortfall)

| Co | TTM to | TTM OCF | TTM capex incl. FL principal | TTM div + buybacks | **TTM gap** | **Latest-qtr gap** | **2026E gap** (guide basis) | **2027E floor** | Cash + mkt sec | Debt principal due → 12/31/27 |
|---|---|---|---|---|---|---|---|---|---|---|
| MSFT | 2026-06-30 (FY26) | 182.9 | 119.0 | 48.7 (26.4 + 22.3) | **+15.2** | **+7.4** (Q4 FY26) | **−26.8** on the ~$175B guide incl. FL at signing; **≈ −5.8 cash basis** | ≤ −37.4 (−62.4 at a $200B pace, illustrative) | 76.8 | 9.25 |
| GOOGL | 2026-06-30 | 185.7 | 134.9 | 27.7 (10.3 + 17.4) | **+23.0** | **−8.9** (Q2) | **−34.4** (−29.4 / −39.4); P&E + FL principal | ≤ −26.4 | 242.5 | ~3.0 (derived) |
| AMZN | 2026-06-30 | 161.4 | 174.6 (gross) | 0 | **−13.2** | **−9.2** (Q2) | **−69.5**; ~$220B net cash capex | ≤ −60.2 | 123.0 | ~8.8 (derived) |
| META | 2026-09-30 | 133.1 | 108.0 | 5.4 (div only) | **+19.7** | **−3.5** (Q3) | **−15.3** (−10.3 / −20.3); capex incl. FL principal | ≤ −12.4 | 82.4 | 2.75 |
| ORCL | 2026-08-31 | 46.9 (incl. **16.0** prepayments) | 75.7 | 5.9 | **−34.7** (**−50.6** ex-prepayments) | **−7.0** (Q1 FY27) | **FY27 (Jun-26–May-27): −40.5** gross ($92.5B); −41.3 net ($70B) | FY28 ≤ −51.8 gross (≤ −45.3 net) | 37.1 | ~10.1 (term loan not extended) |
| **Sum** | mixed dates | | | | | | **≈ −186.5, MIXED BASIS** (≈ −165.4 with MSFT on cash basis) | ≈ −188 floor, MIXED BASIS | | **≈ 33.9** |

Sources: XBRL companyfacts and the filed cash-flow statements [PRIMARY]: MSFT FY26 10-K (acc 0001193125-26-323660); GOOGL Q2-26 10-Q (acc 0001652044-26-000071); AMZN Q2-26 10-Q (acc 0001018724-26-000026); META Q3-26 10-Q (acc 0001628280-26-066773) and 8-K Ex 99.1 (acc 0001628280-26-066700); ORCL Q1 FY27 10-Q (acc 0001193125-26-389274) and 8-K Ex 99.1 (acc 0001193125-26-387905). Maturities come from each filing's debt note. GOOGL and AMZN maturities are derived from the 12/31/25 10-K schedules plus tranche dates. The 2026E and 2027E columns are DEWEY arithmetic on the method below.

**Method and caveats. These are binding on any use of the table.**
- **(i) Mixed capex bases.**
  - MSFT's guide counts *new finance leases at signing* (ROU additions: $24.6B in FY26).
  - META's guide counts *finance-lease principal*.
  - GOOGL's is *purchases of P&E*.
  - AMZN's is *net of proceeds and incentives*.
  - ORCL guides both gross ($90–95B) and *net of customer prepayments* (~$70B), on a fiscal year ending May 2027.
  - Any cross-company sum is therefore mixed-basis.
- **(ii) MSFT's −$26.8B overstates its cash need.** Holding finance-lease additions at the FY26 level gives cash PP&E ≈ $150.4B plus ≈ $3.6B of FL principal, for a gap of **≈ −$5.8B**. That is consistent with CFO Amy Hood's "we expect to remain free cash flow positive in FY '27" (call 2026-07-29) [NEWS/transcript: Motley Fool]. MSFT's FCF excludes dividends and buybacks.
- **(iii) OCF is held flat at TTM.** No consensus OCF was used (Quartr unentitled; search cap). OCF growth at MSFT, GOOGL or META would shrink their gaps. The H1-2026 trend is mixed: GOOGL Q2 OCF was $39.1B vs $45.8B in Q1.
- **(iv) 2027E is a floor.** It holds capex at the 2026 guide midpoint. No company has given a 2027 dollar figure, and all five signal an increase. MSFT: FY27 "will grow year-over-year". META: "continue investing aggressively". ORCL: "upward trend to continue". GOOGL: "another meaningful step-up", wording UNVERIFIED, from a search summary only. AMZN: nothing found. A single-source MSFT FY27 figure of $255–260B is **[UNVERIFIED]** and not used.
- **(v) ORCL's OCF is inflated by customer prepayments** "with a significant financing component": $11.4B in Q1 FY27, 49% of the quarter's OCF; $16.0B TTM. Excluding them, the TTM gap is **≈ −$50.6B**. The ~$40B FY27 gap matches management's plan to "raise nearly $40 billion through a combination of debt and equity" (2026-06-11) [NEWS: Outlook Business], of which $19.9B was done through the ATM in Q1 [PRIMARY: ORCL Q1 FY27 10-Q].

#### 2026-10-29 replay (D:L800, REQ-DEWEY-20261022-005): the cells stand; the stated inputs were the wrong ones

**Trigger:** VULCAN's packet of 2026-10-29 (`inbox/processed/2026-10-29_from-VULCAN_L800-base-arithmetic-does-not-replay.md`). VULCAN applied the method above to the TTM columns. That gives MSFT −19.8 cash and −44.4 headline, and GOOGL −42.0 before finance-lease principal. The table says −5.8, −26.8 and −34.4. VULCAN's arithmetic on the inputs as displayed is correct. The 2026E cells were not built from those inputs.

**What the 2026E cells actually use** ($B). The 10/22 working script is recovered verbatim from the 10/22 session transcript; the 10/22 scratchpad died with that session. It is now saved as `AGENTS/DEWEY/research/2026-10-29_L800-replay/replay.py`.

| Cell (10/22 figure, unchanged) | OCF used | Capex used | FL principal | Dividends + buybacks | VULCAN replay on TTM inputs | Difference, DEWEY − VULCAN |
|---|---|---|---|---|---|---|
| MSFT headline **−26.8** | **193.6**, calendar 2026 = 102.1 filed for Jan–Jun 2026 (Q3 FY26 46.68 + Q4 FY26 55.44) + 2 × 45.73 (TTM 182.94 ÷ 4) | 175.0. The CY2026 guide counts finance leases at signing (Hood, call 2026-07-29) | **0**. The guide already counts finance leases at signing, so principal is not subtracted again | **45.4** = 22.72 filed (div 13.51 + buybacks 9.21) + 2 × 11.34 (Q4 FY26 rate: div 6.76 + buybacks 4.58) | −44.4 | +17.6 = +10.7 OCF basis + 3.6 FL principal not double-counted + 3.3 payouts |
| MSFT cash basis **−5.8** | 193.6 | **150.4** = 175.0 − 24.6 (FY26 finance-lease ROU additions held) | **3.6** = 1.76 filed (0.839 + 0.922) + 2 × 0.922 | 45.4 | −19.8 | +14.0 = +10.7 OCF basis + 3.3 payouts |
| GOOGL **−34.4** | **177.7** = 84.86 filed H1-26 (45.79 + 39.07) + 2 × 46.42 (TTM 185.68 ÷ 4) | 200.0, the midpoint of the $195–205B guide (P&E basis) | **1.5** = 0.84 filed + 2 × 0.318 | **10.6** = 5.23 filed dividends + 2 × 2.69 (Q2 rate). Buybacks were zero in Q1–Q2 2026 | −42.0 (before FL principal) | +7.6 = −8.0 OCF basis − 1.5 FL principal + 17.1 payouts. VULCAN's TTM 27.7 includes $17.4B of H2-2025 buybacks, which stopped after Q4-25 |

The same structure applies to the other three cells, which VULCAN did not dispute; all replay. AMZN −69.5 = 152.1 − 220.0 − 1.65 − 0. META −15.3 = 130.1 − 140.0 − 0 − 5.42 (Q4 at TTM ÷ 4; its guide includes FL principal). ORCL FY27 −40.5 = 58.3 − 92.5 − 0 − 6.26 (three remaining quarters at TTM ÷ 4). **Sum −186,456 $M, CONFIRMED** (−165,453 with MSFT on the cash basis). Replay output: `python3 -I AGENTS/DEWEY/research/2026-10-29_L800-replay/replay.py`.

**Corrections to this report's wording (the 10/22 text above stays as written):**
1. Key Finding and note (iii): "OCF held flat at TTM" applies to the **2027E floors only**. For 2026E, OCF = filed year-to-date + remaining quarters at TTM ÷ 4.
2. Payouts and FL principal for 2026E = filed year-to-date + remaining quarters at the **latest-quarter** rate, not TTM. Table 1 never stated this.
3. MSFT 2026E = **calendar 2026** (Jan–Dec 2026), not FY27. The TTM columns are FY26 (Jul-25 to Jun-26), so the row mixed two periods without saying so.
4. The Table 1 header formula subtracts FL principal. That does **not** apply to MSFT's headline cell, because its guide counts finance leases at signing. It does apply to MSFT's cash-basis cell and to GOOGL and AMZN.

**Downstream: no figure moves.** The five-company sum (−186.5), the MSFT cash-basis sum (−165.4) and the 2027E floors are unchanged. The Oracle weak-link framing (L782 extension; ORCL FY27 −40.5 and −50.6 TTM ex-prepayments) is unchanged; the ORCL cell was not disputed and replays. What changes is how the figures may be described: quote "2026 filed year-to-date plus the remaining quarters at run-rate", never "OCF flat at TTM".

**Input verification, 2026-10-29 [PRIMARY]:**
- **MSFT:** every input ties to the dollar against the saved SEC companyconcept responses in `AGENTS/DEWEY/research/edgar_xbrl/2026-10-28_0000789019_*`. The FY26 values come from the FY26 10-K (acc 0001193125-26-323660); the quarters are decumulated from its 6M/9M/FY facts.
- **GOOGL:** OCF, P&E, FL principal and buybacks tie against new saved packets `AGENTS/DEWEY/research/edgar_xbrl/2026-10-29_0001652044_*` (Q2-26 10-Q acc 0001652044-26-000071, as of 2026-10-22). The H1-26 dividend figure is not in companyconcept under `PaymentsOfDividends`. It ties instead at the 10-Q face: "Dividend payments (4,977) (5,231)", Q2 allocation $2,689M (`goog-20260630.htm`).

**Not changed, now flagged:**
- **GOOGL preferred dividends.** GOOGL's mandatory convertible preferred pays 6.25% a year on $1,000 liquidation preference per share, quarterly from 2026-08-15. The company may pay in cash, shares or both [PRIMARY: same 10-Q]. The H2-2026 payout run-rate above leaves it out. If paid in cash, it widens GOOGL's 2026E gap; that amount is not computed here.
- **Stale vintage.** All 2026E cells sit on the pre-Q3 vintage. MSFT Q1 FY27 and GOOGL Q3 have since been filed. VULCAN's re-cut (`AGENTS/VULCAN/reports/2026-10-29_L800_funding-gap-Q3-prints.md`) is the current figure owner. DEWEY does not re-cut here.

**Process cause:** the shipped table showed the TTM inputs next to projected cells built from different inputs, and the script that held the real inputs lived only in a session scratchpad (DEWEY CLAUDE.md step 8d). A replay could therefore only fail.

**Table 1a: positive TTM gaps at GOOGL and META exist only because buybacks stopped**

| Co | Last quarter with buybacks | Prior-year pace | TTM gap if 2025 buyback pace resumed (DEWEY illustrative) | Latest quarter |
|---|---|---|---|---|
| GOOGL | Q4-25 ($5.5B); zero in Q1–Q2 26 | 6M-2025 $28.3B (≈ $56.6B/yr) | **≈ −16.2** (vs +23.0) | −8.9 |
| META | Q3-25; zero since | 9M-2025 $26.2B (≈ $35.0B/yr) | **≈ −15.3** (vs +19.7) | −3.5 |

Not counted as buybacks: taxes paid on net share settlement, $12.1B (GOOGL 6M-26) and $12.8B (META 9M-26) [PRIMARY: same 10-Qs]. Treating them as buyback-equivalent would widen both gaps.

**Table 1b: how each 2026 gap is being filled (filed unless tagged)**

| Co | Bonds | Equity / hybrid | CP / short-term | Leases and other | Pre-funding vs 2026E gap |
|---|---|---|---|---|---|
| MSFT | **None registered since at least 2021** (EDGAR negative; unresolved). FY26 issued $0, repaid $3.0B | None | Not pulled | Finance leases: ROU additions $24.6B (FY26); FL liabilities $66.6B | Funded from cash flow, $76.8B cash and leases |
| GOOGL | H1-26 debt proceeds $56.2B, incl. **$20.0B USD + $31.8B non-USD**; **$25.0B USD Aug-26** | H1-26 common $30.5B + mandatory convertible preferred $19.1B. The $84.75B program (2026-06-02) includes a $10B Berkshire placement and a $40B ATM, ~$30B of it earmarked for employee-equity tax | CP **zero** of a $25B program; $1.3B credit facility drawn | Backstops (Table 2) | H1 raise ≈ **$105.8B vs a −$34.4B gap**; liquidity is largely raised money |
| AMZN | 2026: **$62B USD** (Mar $37B, Jul $25B) + €14.5B + C$14.0B + £4.25B ≈ **$94.5B USD-equivalent**; "we expect to undertake additional financing activities in 2026" | None | $0.3B short-term borrowings | FL liabilities $13.5B; financing obligations $11.1B | ≈ $94.5B raised vs −$69.5B gap |
| META | **$25.0B USD Apr-26** ($24.9B LTD proceeds 9M-26) | None | Not pulled | **JV vehicles**: [REPORTED] Beignet $27.3B, Sopaipilla $12.3–12.5B; $1.04B JV distribution received | $24.9B vs −$15.3B; cash ≈ debt ($82.4B vs $84.0B face) |
| ORCL | $25.0B USD Feb-26 (FY26) | **$19.9B ATM (Q1 FY27)** + Series D mandatory convertible preferred (Feb-26) | CP repaid $1.1B and short-term capex financing repaid $0.8B (Q1 FY27) | **Customer prepayments $11.4B (Q1)**; financing receivables sold $0.65B; tenant of campuses financed at project level | ~$40B plan for FY27; ~$19.9B done |

Sources: GOOGL, AMZN, META and ORCL 10-Qs as above [PRIMARY]; Alphabet FWP 2026-06-02 (acc 0001193125-26-254490) [PRIMARY]; Oracle preliminary prospectus supplement 2026-02-02 (acc 0001193125-26-032739) [PRIMARY].

### Table 2: Off-balance-sheet and lease exposure ($B; FILED and REPORTED-not-filed kept separate)

| Co (as of) | On-BS lease liabilities | **Leases signed, not yet commenced** | Purchase / contract commitments | Guarantees, RVGs, backstops (FILED) | Project vehicles FILED | Project financings REPORTED, not filed |
|---|---|---|---|---|---|---|
| META (9/30/26) | 31.2 operating (finance liability not extracted) | **355.73** (+76.7 q/q, +27.5%); commence 2026–2036 | 454.5 non-cancelable (+105.2 q/q); +14.7 contingent cloud capacity; 10.8 escrow | **Max RVG 41.49** (vs 28.09 at 12/31/25); **total max exposure to JVs 68.40** (vs 45.95) | Louisiana venture (~$27B cost; **lease 2029**); Texas venture (~$14B; **lease 2028**). Meta 20%; **4-yr initial term, renewals to 20 yrs**; not consolidated | Beignet $27.3B, 6.581% 2049, T+225, S&P A+; Sopaipilla $12.3–12.5B, prelim A+ |
| MSFT (6/30/26) | 88.5 (op 21.9 + fin 66.6) | **329.1**; FY27–FY33; "some … subject to certain contractual conditions" | 194.1 purchase (169.0 within 1 yr); 34.6 construction | None found | None | Counterparty filings: Nscale S-1, up to $43.8B through 2033; IREN ~$9.7B; Nebius unquantified |
| ORCL (8/31/26) | 43.8 (op 34.6 + fin 9.2) | **288** (+28 q/q, +10.8%); Q2 FY27–FY29; 15–19 yr terms | 34.2 unconditional purchase | **$3.3B lessor-borrowing guarantee** (10-K, "matures in September 2026") **no longer appears in the Q1 FY27 10-Q; status undisclosed** | None named | Michigan $16.3B (PIMCO ~$10B); **Jupiter NM ~$18B bank loan**; Vantage TX/WI ~$38B (pre-launch report) |
| GOOGL (6/30/26) | 20.6 | **85.2** + 5.8 short-term | 707.0 contractual commitments | **Data-center credit backstops 43.8 notional** (vs 16.9 at 12/31/25), fair-value liability $0.815B; 7.6 energy-equipment guarantees; 20.0 milestone-contingent funding to an unnamed private company | Counterparties: TeraWulf and Cipher 10-Qs (Fluidstack leases backstopped for warrants) | None pulled |
| AMZN (6/30/26) | 109.8 PV (op 96.3 + fin 13.5) + 11.1 financing obligations | **137.2** | 130.1 unconditional purchase; 650.0 total commitments | None found | None | Not searched |
| **Total** | **≈ 293.9** | **≈ 1,195 (~$1.20T)** | | | | |

Sources [PRIMARY]: META Q3 10-Q, Notes 5 and 10, plus Q2 10-Q (acc 0001628280-26-050705); MSFT FY26 10-K, Note 13 and MD&A; ORCL Q1 FY27 10-Q and FY26 10-K, Note 9 (acc 0001193125-26-277521); GOOGL Q2 10-Q, Notes 3, 4, 5 and 10; AMZN Q2 10-Q, Notes 3 and 4; TeraWulf 10-Q (acc 0001083301-26-000166); Cipher 10-Q (acc 0001819989-26-000041); Nscale S-1 (acc 0001193125-26-395475); IREN 10-K (acc 0001878848-26-000052). The REPORTED column is from IFR, FI-Desk, The Next Web/Bloomberg, Bloomberg Law and FT via The Star [NEWS].

**Notes on Table 2:**
- **The ~$1.20T is a rough size, not a same-day sum.** As-of dates run 6/30–9/30/2026, and definitions differ: MSFT's are partly conditional, META's include energy and network infrastructure, AMZN's are undiscounted. It is **≈ 4.1×** the ≈ $294B of on-balance-sheet lease liabilities. *Correction:* the working notes gave ~$249B and ~4.8×. That figure omits Oracle's $43.8B; with Oracle included the sum is $293.9B.
- **When it lands.** These leases move onto balance sheets as they commence: Oracle Q2 FY27–FY29, Microsoft FY27–FY33. Under standard agency methodology, commenced leases enter adjusted debt. That methodology point is [UNSOURCED] this session.
- **Meta.** Its JV template is an 80/20 JV, Meta as sole tenant, a 4-year initial lease plus an RVG, and an IG 144A bond rated one notch below Meta. S&P rates the bonds on Meta's credit because the contract passes "substantial credit risk to Meta during both construction and operation phases" [NEWS: IFR]. The $41.5B maximum RVG is close to the reported combined bond sizes (~$39.6–39.8B). That is a DEWEY inference; the filing does not state the link.
- **Jupiter (Oracle-tenanted).**
  - The ~$18B loan was quoted at **89–91c** (FT, 2026-09-18) and "below 90 cents" (Bloomberg, 2026-09-24) [NEWS].
  - Oracle's **force-majeure notice over power** (Bloomberg, 2026-09-24) seeks rent-deferral rights if the 2028 online date slips. **It is not an exit.** Oracle: "We are fully committed to New Mexico." Blue Owl: "This notice does not change the financial commitments" [NEWS: Bloomberg Law].
  - **The "~84c" level is [UNVERIFIED]**: X post only, no outlet found.

### Table 3: Issuance and spreads (SEC 424B fee exhibits + FWP pricing term sheets [PRIMARY]; OAS from FRED [PRIMARY])

**3a. SEC-registered USD deals.** The ~10-year tranche spread is to the benchmark Treasury at pricing.

| Issuer | Trade date | Size | ~10y spread | Longest tranche | ICE IG OAS that day | Book / coverage |
|---|---|---|---|---|---|---|
| GOOGL | 2025-04-28 | $5.0B | **T+47** | 2065 T+70 | 1.04% | — |
| ORCL | 2025-09-24 | $18.0B | **T+105** | 2065 T+137 | 0.75% | ~$88B [UNVERIFIED] |
| META | 2025-10-30 | $30.0B | **T+78** | 2065 T+110 | 0.77% | **~$125B**, largest ever; tightened after pricing [NEWS] |
| GOOGL | 2025-11-03 | $17.5B | T+62 | **2075** T+107 | 0.83% | — |
| AMZN | 2025-11-17 | $15.0B | **T+55** | 2065 T+85 | 0.84% | — |
| ORCL | 2026-02-02 | $25.0B | **T+145** | 2066 T+195 | 0.74% (BBB 0.93%) | ~$129B [UNVERIFIED]; with mandatory convertible + $20B ATM |
| GOOGL | 2026-02-09 | $20.0B | T+63 | 2066 T+95 | 0.76% | — |
| AMZN | 2026-03-10 | $37.0B | T+75 | **2076** T+130 | 0.84% | **3.4×** [NEWS] |
| META | 2026-04-30 | $25.0B | **T+90** | 2066 T+147 | 0.81% | — |
| AMZN | 2026-07-07 | $25.0B | **T+80** | 2066 T+125 | 0.76% | **1.6×**; 30-yr tranche 2.5× [NEWS; INSTITUTIONAL] |
| GOOGL | ~2026-08-06/07 (FWP filed 8/7) | $25.0B | **T+85** | 2066 T+130 | 0.78% | — |
| MSFT | — | **None found** | — | — | — | — |
| **Sum since Sep-2025** | | **$237.5B** (ORCL 43 · META 55 · GOOGL 62.5 · AMZN 77) | | | | |

Non-USD deals in the same window:
- Alphabet: €6.5B (Nov-25); £5.5B (Feb-26), including a **£1.0B 2126 century bond at gilts +120bp on £9.5B of orders**; €9.0B; C$8.5B; ¥576.5B.
- Amazon: €14.5B; C$14.0B; £4.25B.
- Calendar-2026 four-issuer total: $157B USD only; ≈ $205B+ USD-equivalent across currencies (DEWEY sum). That is consistent with Reuters/LSEG's ~$194B through 2026-07-07, which was **up 79% on all of 2025** [NEWS: Reuters via WDEZ].

**3b. Price of absorption**

| Indicator | Value | Source |
|---|---|---|
| Same-issuer ~10y spread at pricing | GOOGL 47 → 62 → 63 → **85**; AMZN 55 → 75 → **80**; META 78 → **90**; ORCL 105 → **145** (bp), while IG OAS stayed 0.74–0.84% on those dates | FWPs [PRIMARY]; FRED BAMLC0A0CM [PRIMARY] |
| Oracle ~40y | T+137 (Sep-25) → **T+195** (Feb-26) | FWPs [PRIMARY] |
| Median new-issue concession | **12bp in 2026 vs 2.25bp in 2025** | Reuters via WDEZ, 2026-07-29 [NEWS] |
| Hyperscaler cover ratio | **~5× (Feb) → <2× (Jul) 2026** (Apollo) | same [NEWS/INSTITUTIONAL] |
| Secondary performance | 78 of 91 2026 hyperscaler bonds trading at higher yields than at issue, median **+22bp** (to 2026-07-28) | same [NEWS] |
| Median spread by tenor, 2025 → 2026 | 2–4y 30 → 40bp; 5–7y 50 → 60bp; >20y 108.5 → 118bp | Reuters/LSEG via WDEZ [NEWS] |
| Sector widening | "Around 30bp" in 2026 (TwentyFour, Sep); ">25bp wide" to IG, "10-year high relative to the market" (Schroders, Feb) | [INSTITUTIONAL] |

**3c. ICE BofA OAS (%), FRED, pulled 2026-10-22, last observation 2026-10-21**

| Date | IG (BAMLC0A0CM) | AA (BAMLC0A2CAA) | A (BAMLC0A3CA) | BBB (BAMLC0A4CBBB) | HY (BAMLH0A0HYM2) |
|---|---|---|---|---|---|
| 2025-09-24 | 0.75 | 0.43 | 0.63 | 0.95 | 2.70 |
| 2026-03-10 | 0.84 | 0.54 | 0.69 | 1.06 | 3.06 |
| 2026-07-07 | 0.76 | 0.53 | 0.63 | 0.94 | 2.67 |
| 2026-09-21 | 0.77 | 0.57 | 0.65 | 0.95 | 2.66 |
| **2026-10-21** | **0.88** | **0.63 (2026 high)** | 0.73 | 1.09 | 3.27 |
| Δ 9/21 → 10/21 (bp) | **+11** | **+6** | +8 | +14 | **+61** |
| Δ 9/24/25 → 10/21/26 (bp) | +13 | **+20** | +10 | +14 | +57 |

How to read 3c (DEWEY arithmetic):
- **The October widening is market-wide and led by lower ratings.** AA widened +6bp against +11bp for IG, +14bp for BBB and +61bp for HY.
- **Over the full window AA underperformed.** It widened +20bp vs +10bp for A, compressing the AA-minus-A gap from −20bp to −10bp. That fits supply-driven cheapening of the bucket where Meta, Amazon and Alphabet sit, but **index data cannot pin it on these names**.

**3d. CDS: do not over-read a record**

| Name | Level | Context |
|---|---|---|
| META 5Y | **~114.5–114.8bp, record, +7.3–7.6bp on 2026-10-22** (Markit via Reuters) [NEWS]. Implies ~107bp prior, consistent with the fleet's ~108bp | An active reference entity only since ~Nov 2025, so the series is short. A ChainCatcher 119.3bp is [UNVERIFIED]. ~115bp sits far above the AA cash OAS of 0.63%, which suggests a hedging-demand premium (inference; no basis data) |
| ORCL 5Y | ~198–215bp July 2026, an **18-year high** (from 144bp at the start of 2026) [NEWS]. S&P **BBB-, stable, 2026-07-09** [NEWS: Newsquawk] | **October 343–350bp only from tweet aggregators: [UNVERIFIED].** Reuters 10/22 says only "close to a record high" |
| Market depth | Net tech CDS outstanding a record **~$12.5B** (ORCL ~$6.5B; AMZN and GOOGL ~$2B each) vs **~$120B of Oracle bonds** (FT/LSEG, July 2026) [NEWS] | Protection buyers are **largely banks hedging data-center construction loans** (late-2025 reporting) [NEWS, single-source chain]. Thin, hedge-driven contracts: marginal flows move quotes |

### Table 4: Market-capacity view

| Measure | Value | Source |
|---|---|---|
| 2026 US IG gross-supply forecasts | UBS **$1.7T**; Schroders **~$2T**; Morgan Stanley **$2.25T** (search summary) | fi-desk; Advisor Perspectives/Bloomberg [INSTITUTIONAL/NEWS] |
| Actual YTD supply | H1-2026 IG gross **$1.19T, a record**; tech $210B in H1 (Voya). All US corporate (IG + HY) through Sep **$2,195.1B, +24.5% Y/Y** (SIFMA) | Voya 2026-08-14 [INSTITUTIONAL]; SIFMA [PRIMARY-industry] |
| Hyperscaler bond issuance, Goldman | **~$250B in 2026; ~$400B in 2027**. Debt covers ~1/3 of 2026 capex and ~35% of 2027. "Market saturation and issuer concentration are likely to become more binding constraints" | Reuters via WDEZ, 2026-07-29 [NEWS relaying INSTITUTIONAL] |
| Share of a year's IG supply | **~11–15% (2026); ~18–24% (2027)** at $1.7–2.25T | DEWEY arithmetic; assumes 2027 supply ≈ 2026 |
| Index weight vs long-end weight | **~4.5% of the ICE IG index, but 31.2% of the 26-year-plus bucket** (index 13.0%); 41% of 2025–26 hyperscaler issuance beyond 15 years vs 16% for the index | TwentyFour 2026-09-03 [INSTITUTIONAL] |
| IG stock | $8,284B at 2025:Q4 | Fed FSR May 2026, Table 1.1 [PRIMARY] |
| AI share | AI-related debt ">16%" of the IG market; on course to nearly double 2025 | Voya [INSTITUTIONAL] |
| Demand side | Strong domestic insurer (annuity) and steady Asian demand; 30Y UST ~5.25%, about +40bp YTD | Voya; TwentyFour [INSTITUTIONAL] |
| Separate tail | **Oracle to high yield would push ~$120B out of the IG index**. That is a forced-seller event distinct from AA supply | Motley Fool figure [UNVERIFIED size] |

**What the capacity evidence says.**
- **Absorbed at a price.** No deal in the record failed or was pulled, but each successive jumbo needed wider spreads and larger concessions, and coverage thinned between February and July 2026.
- **The binding constraint is long-duration buyers, not the whole IG market.** Hyperscalers are 4.5% of the index but 31% of the 26-year-plus bucket, and the long tenors repriced most: Oracle 40-year +58bp; Meta 30-year T+98 → T+132.
- **Issuers are already managing this themselves.** They are diversifying across currencies, using equity and mandatory convertibles, and moving debt into JV vehicles.
- **Goldman's 2027 path (~$400B) raises the share of a year's IG supply from ~11–15% to ~18–24%.** It is the forward stress point, not current access.

**Decision read for each recipient (neutral).**
- **VULCAN (forced vs chosen).**
  - No filed or reported evidence was found, as of 2026-10-22, that any of the five has cut capex because funding was unavailable. All five raised or narrowed their 2026 guides upward. GOOGL and AMZN raised more than their 2026E gaps. Maturities are small, so the pressure is new money, not refinancing.
  - Funding-side strain is concentrated at ORCL: BBB-, OCF dependent on prepayments, an ex-prepayment TTM gap of −$50.6B, its tenant project loan quoted at 89–91c, and CDS at an 18-year high. The force-majeure notice cites power, not funding.
  - The forward point to watch is the 2027 long-end capacity.
- **LIQUID (driver vs separate track).**
  - Hyperscaler repricing happened through 2025–26 deal by deal while the index stayed flat, which makes it a **separate, supply-and-credit track**.
  - The October 2026 widening is broad and HY-led, with AA lagging. Index data cannot attribute it to AI borrowing, and TRACE would be needed to separate the two.

## Counter-Evidence

- **Credit quality and access are intact for four of five names.**
  - Meta, Amazon and Alphabet carry AA-area ratings: Aa3/AA- to Aa2/AA+ on the term sheets [PRIMARY].
  - Every jumbo deal cleared, several with record books: Meta's $125B book for $30B; the £9.5B book for Alphabet's £1B century bond.
  - The Fed (May 2026) called Q1 cloud-firm issuance of nearly $100B "met with strong investor demand". It said IG credit quality was "robust", spreads were "at the low end of their historical range", and the excess bond premium was "below the median" [PRIMARY: Fed FSR].
- **Index spreads are still low.** IG at 0.88% (10/21) is below its 2026 high of 0.94% (3/16) and the 1.18% tariff-stress level of April 2025.
- **Equity reduces the borrowing need.** Alphabet's $84.75B program and Oracle's ATM and mandatory convertible cut prospective IG supply relative to a debt-only path. They also cut against a "forced borrowing" story.
- **The gaps may be overstated.**
  - OCF is held flat, and growth at MSFT, GOOGL or META would shrink their gaps.
  - MSFT's cash-basis gap is only ≈ −$5.8B, and Microsoft has not issued registered bonds.
  - GOOGL's and AMZN's 2026 raises already exceed their 2026E gaps.
- **Some commitments are softer than they look.** Not-yet-commenced leases include conditional arrangements (MSFT). Neocloud contracts carry for-cause and insolvency termination rights (Nscale S-1). Meta's RVGs are "not probable" per its 10-Q, with no liability recorded.
- **CDS records are weak signals.** The markets are young and thin, and the buying is hedge-driven.

## Unknowns

1. **Q3 cash flows for MSFT, GOOGL and AMZN** (~10/28–10/29). Their 2026E rows rest on H1 actuals plus a flat run-rate.
2. **2027 capex dollar guides.** None was given by any company. The GOOGL 2027 wording is [UNVERIFIED]; the MSFT $255–260B figure is [UNVERIFIED].
3. **Consensus OCF for 2026–27.** Not accessed.
4. **The status of Oracle's $3.3B lessor guarantee** (repaid, refinanced, extended, or deemed immaterial). The next data point is the Q2 FY27 10-Q, ~mid-December 2026.
5. **Agency treatment.** Whether S&P or Moody's impute Meta's RVG or JV debt, Alphabet's backstops, or not-yet-commenced leases into adjusted debt. No Oracle rating action after 2026-07-09 was checked.
6. **A verified October Oracle CDS level.** Also unverified: the Jupiter loan quote after 9/24, and the "84c" figure.
7. **Per-bond secondary spreads (TRACE)** for the listed CUSIPs, and any separation of hyperscaler-specific from market-wide widening in October.
8. **Order books** for the ORCL Sep-25 and Feb-26 deals, three GOOGL deals, two AMZN deals and the META Apr-26 deal. Concessions after July 2026.
9. **2027 IG supply forecasts from JPMorgan, BofA and Barclays.**
10. **Whether Microsoft has issued any unregistered or 144A debt.** TwentyFour lists Microsoft among 2026 USD issuers, which conflicts with the EDGAR negative result.
11. **Commercial paper.** CP outstanding at MSFT, AMZN and META was not pulled. GOOGL holds zero CP and ORCL repaid $1.1B; nothing found makes CP a material leg.
12. **Customer identities.** The counterparty behind Oracle's prepayments and Alphabet's $20B private-company commitment is not named in the filings. Do not attribute.

## Source Quality Assessment

- **Strong.** Every cash-flow, balance-sheet, lease, guarantee and deal-term figure is from SEC filings. XBRL TTM totals were tied to the face of each statement to the dollar. Index spreads are from FRED. Both VULCAN KB rows were re-confirmed to the dollar.
- **Weaker: the market leg.** Order books, concessions and the Goldman 2027 estimate all rest on one Reuters piece republished by WDEZ, plus TwentyFour, Voya and fi-desk.
- **Weaker: CDS.** Meta is two-sourced (Reuters versions); Oracle's October level is unverified.
- **Weaker: project financings.** All are reported in the news, not filed, except Meta's two JVs.
- **Weaker: guidance.** GOOGL, AMZN and ORCL capex guides come from news and secondary transcript relays (W.Media, TIKR, Outlook Business) rather than primary transcripts.
- **Arithmetic correction.** The working notes' on-balance-sheet lease total (~$249B, ~4.8×) omitted Oracle's $43.8B. This report uses ≈ $294B and ≈ 4.1×. The substance stands: signed-not-commenced leases are about four times the leases already on balance sheets.

## References

All accessed 2026-10-22 unless noted.

**SEC filings [PRIMARY]**
- MSFT FY26 10-K: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/
- GOOGL Q2-26 10-Q: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000071/ · FY25 10-K: https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/
- AMZN Q2-26 10-Q: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/ · FY25 10-K: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/
- META Q3-26 10-Q: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/ · 8-K Ex 99.1: https://www.sec.gov/Archives/edgar/data/1326801/000162828026066700/ · Q2-26 10-Q: https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/
- ORCL Q1 FY27 10-Q: https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/ · 8-K Ex 99.1: https://www.sec.gov/Archives/edgar/data/1341439/000119312526387905/ · FY26 10-K: https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/

**Deal documents: FWP and 424B [PRIMARY]**
- ORCL: https://www.sec.gov/Archives/edgar/data/1341439/000119312525215807/ · https://www.sec.gov/Archives/edgar/data/1341439/000119312526033882/ · https://www.sec.gov/Archives/edgar/data/1341439/000119312526032739/ · https://www.sec.gov/Archives/edgar/data/1341439/000119312526034351/
- META: https://www.sec.gov/Archives/edgar/data/1326801/000119312525258837/ · https://www.sec.gov/Archives/edgar/data/1326801/000119312526197902/
- GOOGL: https://www.sec.gov/Archives/edgar/data/1652044/000119312525100802/ · https://www.sec.gov/Archives/edgar/data/1652044/000119312525263045/ · https://www.sec.gov/Archives/edgar/data/1652044/000119312526043127/ · https://www.sec.gov/Archives/edgar/data/1652044/000119312526044473/ · https://www.sec.gov/Archives/edgar/data/1652044/000119312526338750/ · https://www.sec.gov/Archives/edgar/data/1652044/000119312526254490/ · https://www.sec.gov/Archives/edgar/data/1652044/000119312526251733/
- AMZN: https://www.sec.gov/Archives/edgar/data/1018724/000110465925113283/ · https://www.sec.gov/Archives/edgar/data/1018724/000110465926025948/ · https://www.sec.gov/Archives/edgar/data/1018724/000110465926081334/

**Counterparty filings [PRIMARY]**
- TeraWulf: https://www.sec.gov/Archives/edgar/data/1083301/000108330126000166/
- Cipher: https://www.sec.gov/Archives/edgar/data/1819989/000181998926000041/
- Nscale S-1: https://www.sec.gov/Archives/edgar/data/2110365/000119312526395475/
- IREN: https://www.sec.gov/Archives/edgar/data/1878848/000187884826000052/
- Nebius: https://www.sec.gov/Archives/edgar/data/1513845/000110465926052948/

**Official and industry data**
- FRED [PRIMARY]: https://fred.stlouisfed.org/series/BAMLC0A0CM · https://fred.stlouisfed.org/series/BAMLC0A2CAA · https://fred.stlouisfed.org/series/BAMLC0A3CA · https://fred.stlouisfed.org/series/BAMLC0A4CBBB · https://fred.stlouisfed.org/series/BAMLH0A0HYM2
- Fed FSR, May 2026 [PRIMARY]: https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf
- SIFMA: https://www.sifma.org/resources/research/statistics/us-corporate-bonds-statistics/

**Institutional and news**
- Reuters via WDEZ (2026-07-29): https://wdez.com/2026/07/29/hyperscaler-debt-binge-pushes-yields-up-as-investor-demand-cools/
- TwentyFour AM (2026-09-03): https://blog.twentyfouram.com/insights/how-hyperscaler-issuance-is-reshaping-the-treasury-curve
- Voya (2026-08-14): https://advisors.voya.com/insights/investment-insights/us-investment-grade-credit-2h26-update
- fi-desk: https://www.fi-desk.com/investor-demand-spreads-show-investors-absorbing-giant-issuance-but-balk-at-hyperscalers/ · https://www.fi-desk.com/usd-issuance-to-hit-record-highs-in-2026-ubs-predicts/ · https://www.fi-desk.com/origination-meta-sold-us30-billion-of-ai-bonds-on-30-october/ · https://www.fi-desk.com/meta-taps-blackrock-for-latest-giant-data-centre/
- Advisor Perspectives/Bloomberg (2025-12-23): https://www.advisorperspectives.com/articles/2025/12/23/ai-funding-drive-record-year-top-rated-sales
- IFR: https://www.ifre.com/ifr-awards/2327933/financing-package-blue-owl-capitalbeignet-investors-us27.3bn-23.6-year-bond · https://www.ifre.com/ifr-awards/2330993/us-bond-meta-platforms-us30bn-six-tranche-bond
- Reuters on Meta CDS (2026-10-22): https://srnnews.com/metas-credit-risk-indicator-jumps-to-record-high-after-results/ · https://www.investing.com/news/economy-news/metas-credit-risk-indicator-jumps-to-record-high-after-results-4966556
- AI Weekly (2026-07-28): https://aiweekly.co/alerts/oracle-nvidia-alphabet-spacex-cds-hit-records-on-ai-debt
- boerse-express: https://www.boerse-express.com/news/articles/oracle-aktie-cds-auf-215-basispunkten-hoechstes-niveau-seit-18-jahren-935988
- Newsquawk (2026-07-09): https://www.newsquawk.com/headlines/sp-downgrades-oracle-orcl-to-bbb--outlook-stable
- Bloomberg Law (2026-09-24): https://news.bloomberglaw.com/ip-law/oracle-cites-force-majeure-to-shield-itself-on-big-data-center
- FT via The Star (2026-09-19): https://www.thestar.com.my/tech/tech-news/2026/09/19/oracle039s-18-billion-data-center-debt-under-pressure-ft-reports
- The Next Web (2026-04-25): https://thenextweb.com/news/oracle-data-centre-16-billion-financing-stargate
- Octus: https://octus.com/resources/articles/banks-prep-series-of-multibillion-dollar-debt-offerings-for-oracle/
- Treasury & Risk (2025-12-11): https://www.treasuryandrisk.com/amp/2025/12/11/oracle-hits-highest-credit-risk-since-2009/

**Guidance sources**
- MSFT Q4 FY26 transcript (Motley Fool): https://www.fool.com/earnings/call-transcripts/2026/08/07/microsoft-msft-q4-2026-earnings-call-transcript/
- W.Media (2026-07-23): https://w.media/ai-infrastructure-demand-pushes-alphabets-2026-capex-guidance-to-us-205-billion/
- TIKR on AMZN: https://www.tikr.com/blog/amazon-raised-its-2026-capex-guide-to-220-billion-heres-what-drove-the-increase
- Outlook Business (2026-06-11): https://www.outlookbusiness.com/corporate/oracle-forecasts-95-bn-in-capex-for-fy27-plans-to-raise-40-bn-in-debt-and-equity

**[UNVERIFIED] sources**
- HuggingNews (Oracle CDS 343–350bp): https://huggingnews.com/earnings/meta-cash-flow-flips-negative-as-ai-leases-reach-825-billion-44aa04c7
- sentisense (MSFT FY27 $255–260B): https://app.sentisense.ai/stories/microsofts-ai-investments-pay-off-boosting-the-stock-market-and-tech-sector-07312026

**Reproduction recipe**
- XBRL companyfacts (`data.sec.gov/api/xbrl/companyfacts/CIK##########.json`) for CIKs 789019, 1652044, 1018724, 1326801 and 1341439.
- Concepts: NetCashProvidedByUsedInOperatingActivities; PaymentsToAcquirePropertyPlantAndEquipment (AMZN: PaymentsToAcquireProductiveAssets); FinanceLeasePrincipalPayments; PaymentsOfDividends / PaymentsOfOrdinaryDividends; PaymentsForRepurchaseOfCommonStock.
- De-cumulate year-to-date facts into quarters. FRED series as listed above. Pull helpers: `AGENTS/DEWEY/scripts/edgar_fetch.py`, `edgar_doc.py`, `fred_pull.py`.

## Process Report

- **DEWEY verification and provenance:**
  - DEWEY re-read Meta's 10-Q (acc 0001628280-26-066773, filed 2026-10-22). The $355.73B of leases not yet commenced, $41,493M of maximum RVGs and $68,404M of total venture exposure all match exactly.
  - DEWEY ran the kill-condition grep itself (VULCAN, LIQUID).
  - The report-writer caught an error in DEWEY's own brief: the ~$249B on-balance-sheet lease base omitted Oracle's $43.8B. The corrected multiple is ~4.1×, not 4.8×, and DEWEY accepts the correction.
  - Three Opus legs ran in data-return mode. A report-writer sub-agent drafted this report; DEWEY reviewed it before filing.
- **Searches run:**
  - Primary pulls: EDGAR XBRL and full-text filings for the five companies and five counterparties, 424B/FWP pulls for 18 deals, and five FRED OAS series. These carried the verdict.
  - Web: WebSearch/WebFetch for guidance wording, project financings, order books, CDS and forecasts.
  - **The session-wide WebSearch cap ran out during the market leg** (twice in that sub-run) and partway through the project-finance leg.
- **Data gaps:**
  - Order books per deal and concessions after July 2026.
  - 2027 dealer IG supply forecasts beyond the Goldman relay.
  - Secondary spreads: **TRACE price data is not free**, so there are no per-CUSIP levels.
  - The October Oracle CDS level.
  - Abilene and Vantage financing terms.
  - Agency treatment of leases, RVGs and backstops.
  - Consensus OCF.
  - Q3 prints for MSFT, GOOGL and AMZN.
- **Source frustrations:**
  - Quartr transcripts unentitled.
  - moodys.com and spglobal.com bot-blocked.
  - Advisor Perspectives/Bloomberg and Treasury & Risk returned 403.
  - DTCC TIW single-name report no longer listed.
  - SIFMA IG/HY split spreadsheet not linked in the page HTML.
  - A trade-date grep on Alphabet's August FWP failed.
- **Confidence in findings:**
  - HIGH on filed gaps, leases and deal terms.
  - MEDIUM on the 2026E and 2027E gaps, by construction (flat OCF, mixed bases, floor capex).
  - MEDIUM-LOW on market capacity and CDS.
  - One arithmetic error in the working notes was caught and corrected: the on-balance-sheet lease total omitted Oracle.
- **If I had more time/tools:**
  - FINRA TRACE for the listed CUSIPs.
  - Markit/LSEG CDS history.
  - Primary call transcripts.
  - S&P and Moody's sector notes.
  - Consensus OCF.
  - A re-run of Table 1 after the 10/28–10/29 prints.
- **Suggestions:**
  - Promote the scratch funding-gap calculator to a script, `scripts/funding_gap.py` (build gate, Will-greenlit).
  - Add a BACKLOG line for a TRACE price source.
  - Schedule a cheap post-print refresh of the MSFT, GOOGL and AMZN rows rather than a new research run.

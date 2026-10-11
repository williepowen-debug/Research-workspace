# PROPOSAL — WQ-419 — VLO-HELD-01 precision and settlement-window bar definition
**Written:** 2026-10-11 14:37:53 EDT. **Authority:** WQ-419 permits this proposal only; Will approved continuing the same TERRY Sol task at 15c7d8b40. **NOT ADOPTED / NO GATE ENCODED / NO GRADE / $0.** Owner: TERRY construction. PROME registers and presents the resulting semantic choice; Will rules separately. This advances the previously Tue 10/13 proposal before the first December settlement on Thu 10/15.

Recommendation: compare the computed matched crack at its source decimal precision, without extra cent-rounding; define the source-③ proxy prospectively as volume-weighted one-minute closes for the two complete start-labelled bars at 14:28 and 14:29 ET. Both choices are proposed semantics, not a claim that the existing letter already resolves them. No method is installed here, and no historical grade is re-opened.

## 1. Exact current ambiguity and authority

Canonical current letter: `setups/VLO-SHARE_management-proposal_2026-09-28.md` §2 + **§2-bis**, the WQ-386 approved amendment encoded verbatim from 5d978cf73. Its decisive language includes:

> The held-share thresholds remain strictly below $95 per barrel for notice only and strictly below $90.16 per barrel for TERRY's SELL recommendation.

> Preserve the existing source order and observation standard: (1) CME settlement; (2) the vendor daily row dated to that session, finalized and accepted only within $0.15 of (3); (3) 14:28–14:30 ET one-minute volume-weighted settlement-window proxy, labelled ESTIMATE. Reject duplicated-volume/provisional daily rows. If only (3) is available within ±$0.15 of $90.16, or a required leg/window/identity is missing, the observation is UNKNOWN, not a fire.

The text specifies neither rounding of `42*HO-CL` on ①/②, nor the OHLC price used per bar, nor which side of 14:30 is included. Section 2's 9/28 diagnostic says three bars per leg but is not a method definition. Parent card §§⑪-ter/⑫-bis and the 10/8 management read explicitly use three-bar **typical-price** VWAP; HENRY's original basis report explicitly uses **close** VWAP of the two bars at 14:28/14:29. These are different algorithms, not independent confirmations of one calculation.

Preserved current authority: November `HOX26/CLX26` through 10/14; matched December `HOZ26/CLZ26` for 10/15–11/19 inclusive; reject continuous/wrong-month identities; review 11/18; no automatic January roll, adjustment, persistence requirement or suppression. Established exit remains owed across switch/missing data/sunset. One held share only; two staged shares remain stood down, SCALE terminal. Source order ①→②→③ and finalization/acceptance requirements stand. B1–B3, recommendation/next-regular-session execution and Will-only order authority remain unchanged.

## 2. Decisive source conventions, checked 10/11

[NYMEX HO rulebook §150102.C](https://www.cmegroup.com/rulebook/NYMEX/1a/150.pdf) defines a $0.0001/gallon tick; [CL rulebook §200102.C](https://www.cmegroup.com/rulebook/NYMEX/2/200.pdf) defines $0.01/barrel. A HO tick contributes $0.0042/barrel to `42*HO-CL`. Thus valid native-tick leg prices can yield a sub-cent computed crack. Native published leg precision does **not** decide whether TERRY rounds the derived crack to cents. This is a synthetic matched-leg calculation, not a separately listed crack-spread contract; do not import another product's rounding convention.

[CME's HO settlement procedure](https://www.cmegroup.com/content/dam/cmegroup/market-regulation/rule-filings/2018/09/18-389.pdf) and [CME's CL procedure](https://cmegroupclientsite.atlassian.net/wiki/spaces/EPICSANDBOX/pages/457218849/NYMEX+Crude+Oil) identify the normal settlement interval as 14:28:00–14:30:00 ET. Active-month trade VWAP settles at native tick precision; deferred months use calendar-spread relationships and may use other prescribed tiers. A vendor OHLC proxy is therefore an approximation, particularly for deferred December: minute closes or typical prices do not reproduce every trade or the spread-derived exchange settlement. Documentation access succeeded; actual historical CME settlement values remain unobserved. The old quote-access limitation is not a claim that all CME documents are inaccessible.

For **start-labelled** one-minute bars, 14:28 spans [14:28,14:29), 14:29 spans [14:29,14:30), and 14:30 spans [14:30,14:31). Including the third whole bar includes post-window trades. This mapping is conditional on the vendor's timestamp convention; it was not independently verified on new vendor output here. Future use must verify timezone/interval labels and complete same-session coverage; ambiguity is UNKNOWN under the existing missing-window rule.

Owned source witnesses: HENRY `reports/2026-09-24_F1-basis-named.md` §2 footnote says `Σ(close*volume)/Σ(volume)` over 14:28/14:29; parent TERRY card §⑫-bis records BRENT 10/2 two-bar close proxy $97.97 vs TERRY three-bar typical proxy $97.94, and management §2-bis 10/8 read records 10/7 typical $105.79 vs close $105.82. These differences did not change those far-from-line grades. No fresh market data is fetched or grade inferred for 10/8–10/9 in this continuation.

## 3. Boundary counterexamples (recorded and synthetic, separately labelled)

| Basis | HO $/gal | CL $/bbl | Exact computed crack | Cent-rounded | Strict comparison |
|---|---:|---:|---:|---:|---|
| **Recorded 9/25 source-② F1 witness**, parent §⑪, HENRY inferred finalized row, CME not observed | 4.4621 | 92.41 | **94.9982** | **95.00** | unrounded <95 FIRES; cents <95 does not |
| **Synthetic held-exit native-tick witness**, not an observation | 4.3478 | 92.45 | **90.1576** | **90.16** | accepted ①/② unrounded <90.16 exits; cents does not |
| **Synthetic exact tie**, not an observation | 4.3300 | 91.70 | **90.1600** | **90.16** | equality does NOT exit under either convention |

The source-③ ±$0.15 exit band must not be imported onto ①/②: the synthetic 90.1576 witness assumes one of those higher tiers is legitimately available/accepted. With **only ③**, that number is UNKNOWN under the existing band, not a SELL recommendation. The recorded SCALE case remains the canonical dated result; this proposal neither reverts it nor revives the two staged shares. It demonstrates why choosing a convention is consequential.

**Synthetic OHLC/volume window witness** (not market data): each HO bar at 14:28/14:29 has H=4.46, L=4.42, C=4.42, volume=100; the start-labelled 14:30 bar has H=L=C=4.45, volume=100. Every CL bar has H=L=C=95.50 and volume=100. Open does not enter either formula. Exact arithmetic gives:

| Choice | Crack | Held-exit result if only ③ available |
|---|---:|---|
| two bars, close-price weighted | **90.14** | **UNKNOWN**, within inclusive [90.01,90.31] |
| same two bars, typical-price `(H+L+C)/3` weighted | **90.70** | NOT FIRED, outside band |
| three bars, close-price weighted | **90.56** | NOT FIRED, outside band |

This changes data treatment even when no method fires a trade. The window and price choices must be made together before a near-boundary grade. Exact Decimal/Fraction reproduction and all inputs: `research/2026-10-11_WQ419-VLO-boundary-evidence.json` (recorded witness distinguished from synthetic fixtures). No probabilities or new error calibration inferred.

## 4. Proposed exact wording — for Will, not installed

Insert after WQ-386's source-order paragraph **only after a separate Will ruling**, for HELD-01 leg A only:

> For sources (1) and (2), compute the matched crack C = 42 × HO − CL from the source's named-contract prices for the same settlement session, retaining their published decimal precision. Compare C directly with $95.00 and $90.16: both comparisons are strictly less-than; equality does not satisfy either. Do not round HO × 42, either input, or C to cents before comparison; round for display only after the decision. Published native-tick leg prices remain the inputs. A binary transport artifact may be normalized only to its verified published price, never rounded to invent a price; an unverified source precision is missing data, treated under the existing UNKNOWN rule. Retain original input values and the exact comparison value in the grade record.
>
> For source (3), use the two complete one-minute bars per named contract covering [14:28:00,14:30:00) America/New_York on the settlement date. On a feed verified to label bars by opening time these are the 14:28 and 14:29 bars; exclude the 14:30-start bar. Let P_HO = Σ(Close_HO × Volume_HO)/Σ(Volume_HO) and P_CL = Σ(Close_CL × Volume_CL)/Σ(Volume_CL), each over that contract's two bars; compute C3 = 42 × P_HO − P_CL. Use Close, not (High+Low+Close)/3, and weight each leg separately before subtracting. Do not round the leg VWAPs or computed C3 before comparison or the source-(2) acceptance check. This is a vendor close-price volume-weighted proxy labelled ESTIMATE, never the CME settlement itself.
>
> For source (3), and for the source-(3) comparison required to accept source (2), verify the session, contract identity, timezone, bar interval convention, full two-bar coverage, prices and volumes on both legs. These vendor-bar requirements do not apply to a valid source-(1) CME settlement pair; source (1) remains eligible when vendor bars are absent. Each leg must have positive total volume; a zero-volume bar contributes no weight and cannot replace a missing bar. A missing, duplicate, incomplete or ambiguously labelled required bar/identity, invalid price/volume or zero total volume is missing data under the existing UNKNOWN rule, not an interpolated observation. Keep the existing dated/finalized source-(2) requirements, inclusive acceptance |C2−C3| ≤ $0.15 and existing source-(3)-only ±$0.15 exit UNKNOWN band. No tolerance, threshold, consequence or automatic monitor is added by this precision/window definition.

**Why this recommendation:** input precision follows the actual matched-leg calculation and avoids losing a genuine sub-cent margin; the two-bar close proxy follows HENRY's explicitly documented method and excludes a whole minute after the exchange window. It also changes the three-bar typical-price convention used on some TERRY reads, so it requires Will's choice. The 0.15 tolerance is preserved as the existing operational allowance, not independently validated for every December/non-active settlement procedure. If published timestamp/precision proof is unavailable at a future grade, label the gap rather than adopt convenient conventions.

**Source-order counterexample (synthetic, not a grade):** if a valid same-session named-contract CME pair is HO4.3478/CL92.45 but vendor bars are absent, source① remains eligible and its unrounded90.1576 comparison is evaluated under the proposed precision rule. No vendor-window UNKNOWN is imposed on source①. Missing vendor bars do prevent using③ and accepting② against③. This scopes the proposed validation without changing source precedence.

**Alternative for Will:** expressly select cent-rounding of the computed crack (with rounding mode stated) and/or retain a specified three-bar typical-price proxy as a broader-window estimate. Either changes the proposed outcomes above and remains a semantic choice, not a reference repair. Recommendation is the unrounded/two-bar-close wording, prospectively.

## 5. Remaining blocks and routing

ACTION: PROME independently verify exact current letter, source conventions and both boundary witnesses; register the resulting precision/bar-definition choice for Will before presenting it. This WQ-419 approval covers preparing this artifact, not adopting its text.
ACTION: On an actual separate ruling, TERRY may integrate only its approved wording and PROME may update its owned gate reference. Until then the registered letter remains verbatim, the unresolved convention stays disclosed, and no new grade is performed here.

Legacy Form-A parenthesis noted by STRANGER_B refers to the old $95 context; it does not independently establish a competing current notice rule against WQ-386 §2-bis. PROME's first-plan disposition confirms this reading. This proposal preserves the approved $90.16 exit band and adds no notice uncertainty band; **no extra band change or separate notice-band ruling is recommended**. B-policy scope questions, July calibration identity, automated cadence and source-② finalization weaknesses are outside this bounded continuation and remain recorded limitations; no broader research or gate repair is undertaken.

Original WQ-409 remains fulfilled PASS only; WQ-418/L681 awaits actual Will/VIOLET disposition. USO booking and live C5 remain Tue 10/13, not advanced. Recovery hold standing: repair approval UNKNOWN, acceptance PENDING. PROME consumed the corrected proposal at 31f9f3d1a/1162faf3c and explicitly asked the new continuation closeout; current receipt is research/2026-10-11_WQ419-owner-closeout.md.

**PROME first proposal read, before delivery:** independent Decimal/native-tick source check received. Corrected the JSON held-exit witness label to native-tick-valid synthetic (90.1576, not equality/off-tick), and scoped vendor-bar validation explicitly to③ and② acceptance. Valid① with absent vendor bars stays eligible. No new research round or adoption.

**Result consumption / closeout addendum — 2026-10-11 15:14:23 EDT:** PROME independently accepted the WAL repair and first-plan corrections/arithmetic, while keeping this VLO wording NOT ADOPTED. Its legacy-parenthesis disposition above removes the overstated competing-rule claim without modifying a band or the proposed precision/bar wording. No gate encoding or new research; new explicit owner closeout ask received.

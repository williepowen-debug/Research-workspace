# LIQUID substantive credit follow-through — November 4, 2026

**Commission:** Will's direct instruction after startup. Existing credit/persistence reviews, reported L4 arithmetic defect, source-bounded transmission follow-through and closeout only. No new study, monitor, gate, schedule, threshold, capital permission or framework. Runtime OpenAI/Codex, session 01a1a85f-2a85-73b1-a635-703694647e61, exact model not exposed.

## Verdict

**The renewed credit-price confirmation is MET; broader price repricing is demonstrated, a generalized dollar-funding restriction is not.** The >320 bp run reset October 27, restarted October 29 and reached three observations on November 2 (326/344/343), then four on November 3 (340). This is a renewed price episode, not a new independent bear root or sizing permission. X1 stays CLOSED / DON'T-SIZE. The existing tier-ladder classification is BROADENS; two recent daily retracements do not erase the 15-session IG/BBB widening. Overnight funding remains below the seizure gate's ARM line, with the November 4 non-calendar observation still unpublished.

There is **reported specific financing-driven selling at Arini**, with anonymous counterparties and no verified bank loss. Separately, the Ueno resolution packet supplies documented local bank→fund redemption/valuation restrictions in Paraguay. These defeat a blanket claim that every channel is only prices, but neither proves U.S. exposure, generalized dollar shortage, Brazil spillover or a common cause for the U.S. spread move. Oracle's priced capital access is counterevidence to universal refusal; settlement is unverified.

## 1. First-published price reconciliation

FRED initial-release API (`fred_fetch_vintage`, `output_type=4`) captures saved per series. No error, duplicate date, missing latest-vs-initial date or short flag on credit series. 60 requested observations from September 1 return46 valid rows: under_limit reflects the explicitly bounded window, not a missing publication. Capture begins November 4 ~16:13 ET. **ALFRED's ICE realtime_start labels are backdated to observation dates; they prove initial-release values, not wall-clock availability.** The November 2 value is graded on today's retrieval; no assertion it was visible on November 2. Prior completed owner price grade: October 29 observations, graded October 30. Ordinary latest-revised tool output is saved separately and does not replace initial-release gate counts.

| Observation | HY | IG | BBB | BB | B | CCC | HY−IG | >320 count | Daily change HY / BB / B / CCC |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Oct 29 baseline | 326 | 89 | 110 | 194 | 332 | 1325 | 237 | 1 | +12 / +10 / +14 / +18 |
| Oct 30 | 344 | 94 | 116 | 209 | 360 | 1327 | 250 | 2 | +18 / +15 / +28 / +2 |
| Nov 2 | 343 | 94 | 117 | 206 | 363 | 1319 | 249 | **3 — MET** | −1 / −3 / +3 / −8 |
| Nov 3 | 340 | 93 | 116 | 203 | 362 | 1316 | 247 | **4 — MET** | −3 / −3 / −1 / −3 |

All spreads bp, same-date first-published. No November 4 credit observation was published at this capture: **UNGRADEABLE-PENDING-PUBLICATION**, not NOT FIRED. No reset since October 29. HY<260 kill stays0-of2; latest340 is80 bp above260. X1's strict>280×3 price half remains MET, but BROCK's relative half and Will's sizing limits do not move. REGINALD's strict>350×3 witness0-of3 (max344); owner adjudication remains REGINALD's. No <300 exit witness in the new observations; RED/REGINALD own their exit ledgers.

### Existing quality-ladder rule, not a new breadth instrument

Applied the ordered September 25 §1c rule in `reports/2026-09-25_credit-transmission-persistence.md`, saved in `breadth_rule.json`. **BROADENS on all three new observations.** October 30: IG+5/BBB+6/BB+15 with B+28 and CCC+2 meets daily broadening. November 2/3 retain BROADENS via existing 15-session IG≥+6 / BBB≥+7 terms, even when daily tiers tighten. November 3 vsOctober 13: IG+10, BBB+13, BB+12, B+45, CCC+49. REVERSES requires CCC≤−9 AND B≤−4 on the day: none of these three days meets it. Current CCC−BB1113 and CCC−B954 remain wide, but the B−BB15-session gap rise of33 bp shows deterioration is not isolated to CCC.

Latest-revised context only: existing transmission_check output ranks 15-session IG/BBB widening at95.8th percentiles and B−BB gap change98.7th in its rolling~3-year history. This sample excludes2020/2022 stress. Tiers/ETF weights are not issuer-count breadth or contribution attribution. XCCC's composition standing line was not re-pulled here; its existing dated observations remain labelled.

### Existing 069 / 072 price tests

- **069 L1 NOT FIRED** Oct 30/Nov 2/Nov 3: BB209/206/203 all≤220; CCC5-session deltas−29/−26/−5, so only November 3 qualifies as flat. No new leg or re-count.
- **069 L4 source adjudication NOT FIRED** on all three available sessions. Worst raw-close name: NBIS−10.38% [Oct 30], APLD−8.98% [Nov 2], CRWV+7.16% [Nov 3]; every name is above−15%. HY changes+18/−1/−3 respectively. These are exact-ratio, source-based checks, not promotion of the unreleased automated candidate. November 4 L4 waits for same-session HY, regardless of available equity prices.
- **072 price leg NOT FIRED:** IG94/94/93 does not satisfy strict>94 (ties fail), and bases250/249/247 do not satisfy strict<180. Event legs remain source-bounded, not universal negative searches. SpaceX CANNOT-FIRE is unchanged.

## 2. Boundary defect, actual impact and release state

The existing binary comparison computes `(2.04 / 2.40 - 1) * 100` as−14.999999999999991, missing the existing inclusive−15% boundary. Root cause is binary division controlling the grade, not a changed threshold. Repair compares decimal price products against the existing ratio, separately from the displayed float return. CLI input restores the letter's2dp published raw closes from vendor float storage. No tolerance is introduced; a value infinitesimally above the boundary does not meet. Any existing cohort name may meet; missing/date-mismatch cases still fail closed. L1 and all thresholds/calendars/owners unchanged.

Acceptance committed **before code** (`9d99b0a21`). Author tests: exact2.40→2.04 with HY+5 meets;2.03 meets/2.05 does not; HY+4 fails;2.040000000001 fails; NBIS boundary verifies ANY ONE. Existing selftests pass. Independent integer-cent cross multiplication agrees on **43 retrieved sessions September 4→November 3, zero changed actual results**, including the already-recorded October 14 L4 fire. This is a bounded current-history comparison, not an immutable census of quotes each old session originally saw. Synthetic family generated here:814 old misses of2991 exact pairs; DAEDALUS's815/2991 is a different supplied family and not claimed reproduced count-for-count.

**Repair state: IMPLEMENTED · TESTED (author) · NOT YET INDEPENDENTLY VERIFIED.** One result read requested from the existing DAEDALUS owner by committed packet and verified Codex send tool. Tool acceptance establishes notification acceptance only; recipient result/consumption not yet evidenced. `reads:0` until an actual independent read is received. **Normal gate069 CLI is WITHHELD, exits4 without an operational grade; selftest/pure functions remain available for review.** Exact candidate needs independent result RELEASE (with an independently devised counterexample) before removal of the operational hold. No known-bad fallback is offered. Manual unaffected source adjudications above remain usable. No actual historical grade is revised based on a synthetic failure.

## 3. Funding and dealer conjunction

FRED first-published, same-date IORB pairing, integer bp after subtraction. November 4 SRF is independently dated and does not advance the November 3 rates clock.

| Rate observation | SOFR−IORB | SOFR99−IORB | SOFR99−1 | EFFR−IORB | Repo take-up ($B) | 079 calendar |
|---|---:|---:|---:|---:|---:|---|
| Oct 28 | +4 | +12 | 13 | −2 | .006 | excluded |
| Oct 29 | +4 | +12 | 13 | −2 | .031 | excluded |
| Oct 30 | +5 | +13 | 15 | −2 | 0 | excluded |
| Nov 2 | +5 | +13 | 13 | −2 | .002 | excluded |
| Nov 3 | +7 | +15 | 17 | −2 | .005 | excluded |

November 4 repo take-up0, first-published that day. No sustained>$50B. Reserves remain$2,893.770B [WednesdayOct28], above<$2.8T; next weekly release November 5. **079 NOT ARMED through Nov3**: all recent days excluded and no≥+30 bp observation anyway. FIRE not graded on unarmed days. WQ-535 A bands already encoded; no new calibration or numerical change. n=1 limitation and BROCK's X1 riders preserved. November 4 is the first eligible post-turn observation, published November 5; it cannot be graded today. EUR/USD basis remains dark and the swap-line instrument remains SHELVED—WITHHELD (WQ-534 B).

**076 rolling window October 22→November 4: NOT MET1-of3**, compared with the prior October 16→29 MET2-of3. W1 as-ofOctober 27 remains−2,535,985 with−162,945 weekly build, so neither≤−2,950,000 nor cover>+300,000. Its original October 30 publication is saved in the prior owner evidence; currentCFTC as-ofNovember 3 is not due untilNovember 6. W2's latest published as-ofOctober 21−1,861 ($mm, G5L10; G10−10,277) is unchanged on today's primary API and has **aged out**, rather than improved. As-ofOctober 28 remains pending November 5. W3 is MET within the window on October 26–29 witnesses, each comfortably>1 pt from both lines. November 4 after16:15 yfinance witness MOVE93.92/VIX16.74 is similarly away from both boundaries; VIOLET governs the exact close. October 30 owner correction VIX19.42 is a near-boundary W3 session, not independently guessed from the witness. No ten-business-day all-leg absence, no re-arm or second write-up. Publication-lag/actionable-life denominator remains CANNOT-CERTIFY (DAEDALUS packet), not a new firing prohibition.

These observations bear on measured overnight funding and dealer net positions. They do not measure bank-specific cash refusals, haircuts, sponsored repo, MMF cash origins, private CSA calls or offshore basis. Calm measured rates cannot clear those channels.

## 4. Named financing and restriction evidence

| Evidence | What it establishes | What it does not |
|---|---|---|
| **Arini**, WSJ-attributed October 30 report, full Investing.com relay read by LIQUID November 4 | Reported~$800M debt sales in recent weeks, partly following bank margin calls, with liquid assets sold against leveraged/CDS-index requirements. Specific funding-response mechanism, beyond price widening. | Anonymous sources; WSJ original not reached; unnamed banks, exact assets/allocation and realized bank loss unknown. Not verified fund/bank disclosure or generalized funding seizure. [Relay](https://www.investing.com/news/company-news/hedge-fund-arini-sells-800-million-in-debt-as-losses-mount--wsj-4989041). |
| **Oracle**, indexed issuer pricing release November 2 + indexed SEC prospectus |86,206,897 shares at$116 (~$10B gross) and$10B notes, coupons7.000–8.650%, expected closingNovember 4. Funding-access counterevidence at a price. |Pricing/expected settlement is not confirmed cash or all money earmarked to AI. Direct issuer/SEC opens failed; indexed primary text read, not whole filing. [Issuer](https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Pricing-of-20-Billion-of-Common-Stock-and-Senior-Notes/default.aspx), [SEC](https://www.sec.gov/Archives/edgar/data/1341439/000119312526445847/d181425d424b5.htm). |
| **Ueno**, BCP November 3 announcement directly read; Circular020/Resolution0016 per WALTER primary-PDF read |November 2 bank resolution; affected funds' redemptions temporarily suspended and valuation rules imposed. Actual local bank→fund restriction. Reopening fromNovember 5 is conditional/fund-specific. |LIQUID PDF retries403; WALTER's verified scope retained. Named-fund annex/AUM not read, final recovery unknown, no U.S./regional contagion established. BCP's institution-specific assessment is not independent proof of no contagion. [Announcement](https://www.bcp.gov.py/web/institucional/w/banco-central-inicia-el-procedimiento-de-resolucion-de-ueno-bank); WALTER `research/2026-11-04_reboot/VERIFY-EVENTS.md`§Ueno. |
| Treasury gross issuance packet |$839B auction supply includes refinancing; resident Japan/Korea TIC bond/note transactions are not official-only holdings changes. Basis distinction integrated. |No net-new-debt reconstruction, buyers' strike or funding seizure inferred. Existing WALTER verification retained, no repeat study. |
| **October HY issuance total** |SIFMA November 2 aggregate page updated throughOctober, but its$2,342.6B is **all corporate issuance**, not HY October volume. |HY monthly subtotal not obtained: workbook download leads to a contact form. No form submitted, no source substitution. Volume leg of “freeze” remains unresolved. [SIFMA](https://www.sifma.org/research/statistics/us-corporate-bonds-statistics). |

**AI CDS follow-through, saved DTCC daily records:** November 2 standardDecember2031 CRWV5Y upfront18.78–19.65 pt, model-derived clean1115–1152 bp / dirty1140–1177; November 3 upfront18.14–18.39 pt, clean1088–1099 / dirty1114–1124. Thus a standard5Y observation is recovered after October 30's missing5Y; elevated versusOctober 29, then tighterNovember 3. Existing L2 remains FIRED since September 26, no re-count. Flat-hazard conversion (r4%, R40%, unsigned upfront buyer-pays assumed), not ISDA/executable/default probability. Batch rows excluded; same-file corrections/terminations checked. Original notional caps and standardness flags retained; unflagged standard print anchors each day.

ORCL standard5Y converted clean290–296 [Nov 2],293–295 [Nov 3]; a November 3 disseminated0.03=300 bp print has ORACLE CORPORATION underlier. Other Oracle-labelled spread fields~2.1 bp use underlierNT and are **quarantined for identity/basis conflict**, not a collapse or a trade-card void. This is a source exception, not a new parser repair. Meta disseminated120/121 [Nov 2],120.5 [Nov 3]; near-par unsigned-upfront conversions not adopted. ORCL/CRWV are already-counted issuers, Meta is not a new BB-like-spread instance; no new072 event claimed. L3 remains NO_INSTRUMENT. ORCL L5 primary re-verification remains inaccessible; November 2 secondary reports retain FitchBBB, Moody'sBaa2, S&PBBB−, no R1 supported at this scope; not promoted to primary verified.

**CHK-40 existing source packet, datedNovember 2:** no reserve liquidation/redemption surge demonstrated in its one reopening-day print. Frozen primary balances unchanged$2,173.46M plus$30M probable; frozen remains reserve-backed, not burned. Venue outflows are not issuer redemptions. New blacklist coverage isUNKNOWN (RPC scan failed), only29/1448 pairs reopened, chain/supply/18-hour limits retained. No freshNovember 4 issuer/reserve census performed; not a current all-clear. No additional standing tracking created.

## 5. Exactly pending / completion boundary

1. **November 5 reviews stay OPEN:**069 needsNovember 4 first-published credit/paired session and theNovember 4 DTCC file (tonight~20:15);076 awaits as-ofOctober 28 NYFed positions (November 5) and VIOLET edge closes if load-bearing;079 awaitsNovember 4 SOFR99/IORB (November 5), the first non-calendar observation after the excluded turn. Today's partial grades do not close these review rows. New weekly CFTC as-ofNovember 3 publishesNovember 6 and is explicitly outside today's available set.
2. **Boundary candidate operational release:** independent DAEDALUS result receipt not yet received; CLI WITHHELD. Forty-three manual/retrieved comparisons change zero historical grades. No boundary-dependent result promoted.
3. **Source/instrument gaps:**OctoberHY subtotal/contact-form download; AI new-issue concessions; rating-primary re-verification; private/offshore funding. ORCL NT-underlier spread anomaly quarantined, not silently repaired. Ueno named-fund annex/AUM/recovery and U.S. exposure unestablished; no new search commission.
4. **Prior obligations preserved, not falsely completed:**Brazil settlement/LFT; HENRY cash/certificate/issuer-credit bridges;November 13 estimatedBDC card/Q2 residue;November 30 jointGENIUS Act read; older specifically deferred analytic repairs; unscheduled fund-to-dealer gap. Completed FirstBrands study andLIQ-07 are not reopened.

Frozen prediction rows (includingLIQ-04), FLOW andVX remain byte-unchanged. Existing gates/approval limits and WQ-534/535 rulings preserved. No trade, paid access, external contact, new collector, monitor or framework. Signal→WALTER, analytical completion→PROME. Durable packets, notification acceptance, recipient consumption and closeout are reported separately.

## Closeout validation and consumer checks

Boot selftest PASS, boundary selftest PASS, exact CLI-withholding exit4 verified, claim weekdays clean, STATUS 22,253 bytes below the owner rotation stop, five gate rows preserved. Frozen file hashes rechecked against frozen_hashes.json and git: unchanged. Consumer scans found the old 1-of-3 string in dated drill/history/audit rows; those remain true historical observations and were not rewritten. The current NEXUS brief is folded from final STATUS; current recipient deltas travel via WALTER/PROME packets, never edits to peer files. No new old count was accepted as current. Git dirty-owner stop observed; other desks' files not swept.

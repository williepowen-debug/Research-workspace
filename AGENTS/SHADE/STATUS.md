# SHADE STATUS

**Last Updated:** 2026-11-11T10:18:38-05:00 — catch-up on Will's 09:24 ET word via PROME prome-2b, Claude Code/Opus 5.5 (§0w). No score, band, gate or threshold moved. Prior: 11/6 20:40 WQ-644 A recorded; 11/6 17:23 close refresh, **`T-SHADE-01` NOT MET at the 11/6 close, no Q3 statutory or deck posted**; 11/6 16:48 restart closeout (Q3 read, L185 legs, card 041).
**Prior sessions:** 10/21 L726/L727 proposals; 10/15 L673 first grade; 10/10 L0 drain; 10/1 W1/ARI; 8/28 Delaware Life pause. Historical chain → `archive/STATUS_PRE-ROTATION_2026-10-01.md` (32,462 B, crc32 `8f171d07`, `tail -n +5`) / `archive/STATUS_PRE-ROTATION_2026-08-28.md`.

**Signal Status:** 🟠 **STRUCTURAL / LATENT INSURER-WRAPPER STRESS, ONE vector FIRING (single-name Delaware Life).** **`T-SHADE-01` NOT MET (read 11/11, endpoint 11/10 close):** 9/24→11/10 RAW wrappers +2.62% vs managers +8.88%, both up; no dig. 10/10 owner fire stays PROVISIONAL, unconfirmed. HY 334 [11/9] (LIQUID; 2026 high 348 [11/5]), environment band YELLOW; 11/10 cell due about 10:10 ET 11/12. SHADE tests how insurers absorb, hide, finance or amplify fund stress; no cohort cascade proven.
**⚠️ KB WARNING:** `domain/sources/` 01–08 are Mar'26 vintage — check `LAST_REVIEWED` before citing.

---

## 0. WHERE EVERYTHING IS

| Surface | Holds | Treat as |
|---|---|---|
| **`STATUS.md`** (this) | Live verdict + rails (§0o/§0r), top-line, vector dashboard (§3), stages (§4), forward calendar + ladder (§6), owners (§7), owed list (§10) | **Boot-read whole. Canonical on live state.** Budget 32,550 B; `python3 scripts/read_cap_check.py --agent SHADE` every closeout. |
| **`REFERENCE.md`** | §2 carried figures (§2Q Delaware Life primary) · §3D/§3R per-vector evidence · §4 map · §5 watchlist · §6M monitor rows · §8 questions | **On demand, by section. STATUS wins on disagreement.** |
| **`research/`** | Per-session deltas — **11/6: `L673_CLOSE_READ_2026-11-06.md`, `L185_Q3_INSURER_READ_2026-11-06.md`** · 10/29: `L781_RATIO_ENCODE_AND_FIRST_READINGS_2026-10-29.md` · **10/10: `T-SHADE-01_FIRE_AND_L0_DRAIN_2026-10-10.md` (+ `tshade01_signleg_2026-10-10.py`)** · 10/1: `W1_OPACITY_LEGS_AND_CATCHUP_2026-10-01.md` · 8/28: `DELAWARE_LIFE_DISTRIBUTION_PAUSE_…`, `DELAWARE_LIFE_Q2_2026_STATUTORY_…`, `FABN_CANARY_RERUN_AND_AG55_…` | When a verdict needs its evidence. |
| **`archive/STATUS_PRE-ROTATION_*`** | Verbatim prior STATUS files | **Provenance only.** |
| **`instruments/FABN_SUPPLY_ADJUSTED_CANARY_SPEC_2026-08-13.md`** | S1/S2/S3 canary, no-bands rule | Before grading the canary. |

⛔ **Standing rules:** the session delta lives in `research/`; STATUS carries the verdict and live rails only · never raise the budget · rotate verbatim + crc-verify (**the 10/1 banner was written with the wrong offset and the crc caught it — same 15-B defect as 8/28; run the check, never trust the banner**).

---

## 0w. 2026-11-11 — CATCH-UP (LIVE RAIL)

**Record:** `research/CATCHUP_2026-11-11.md`. Inbox 3 → 0. **Nothing posted yet:** Athene Q3 FI deck (call 11/12), AAIA Q3 and DLIC Q3 statutory all absent at 10:1x ET.

| Read | Result |
|---|---|
| `T-SHADE-01`, 11/10 close | Level MET (31 published sessions >280 since 280 [9/24]); sign **NOT MET**, +2.62% vs +8.88% both up. ⚠️ vendor ADJ revised BIZD's dividend under the 11/6 read; RAW unchanged |
| Hiking Fed (2Y 4.73, +22bp from 11/6, verified Treasury) | Tightens FHLB room ($3.9B) and S2 (34.2%), adds a surrender push at DLIC; FABN band is a spread, untouched by construction; **biases the sign leg toward NOT MET** (BDC income rises). INFERRED, unmeasured until the deck/statutory |
| Clear Spring NAIC overview (YE2025) | C&S **$1,194.3M**; affiliated $5,895M ≈ **4.94× surplus** (cross-document). Closes the free-report gap; marker (5) stays open |
| F-SHADE-01 gate | **30 sessions >300 through 11/9** on today's FRED, to confirm on LIQUID's series ⇒ the test will likely grade, not NO-VERDICT |
| SHD-03 | A-/A-/A- unchanged, no downgrade found (secondary search) |

## 0v. 2026-11-06 — Q3 READ (LIVE RAIL)

**Record:** `research/L185_Q3_INSURER_READ_2026-11-06.md`. PRIMARY = 10-Q filed 11/5, deck 10/30, unless marked.

| Read | 9/30/26 | Against the letter |
|---|---|---|
| Level 3 assets | **$177,478M, +$14,877M QoQ** (pin: 148,140 · 155,078 · 162,601) | A1: $123M under the $15B confirm line, above the $5B clear line, neither fires. ⚠️ gross additions $18,782M before marks |
| Pledged assets | **$120,089M, 28.80% of investments** | K3.3 kill not fired |
| FHLB | **$29.9B drawn, $33.8B drawable, room $3.9B** (6/30 $6.1B) | K3.3 kill not fired, "near exhaustion" unrefuted, not confirmed |
| Canary | **S1 ~$2.3B derived, S2 34.2%** | Ungraded, deck due at the 11/12 call. **C2: S2 leg fails, so the AND cannot pass; row executes at the deck** |
| AI book | **$12.9B funded, ~3% (Athene); SVF II Finco $3,097M outside it (INFERRED); Big Sky commitments $6.2B** | No letter. Funded $16.0B = 3.8%; with commitments $22.2B = 5.2%, a ceiling |
| SoftBank-linked | **$4,846M**, SVF II +$1,033M in Q3 | No letter. Vehicle identities INFERRED. Card 041 11/6: the $10B loan is not an "OpenAI-share margin loan"; these figures unchanged |
| Apollo GAAP loss | $3,274M of Athene's $3,418M is mortgage and derivative marks; provision $82M | Accounting and rates on issuer attribution. ⚠️ **90+/non-accrual principal $1,818M → $3,453M, +89.9% YTD** |

**Also:** AAIA Key Ratio #1 (1,635.7%, FY25) recorded **CRITICAL BY LETTER**, no score tied, no rescore · X1 reconcile: BROCK CONCUR 11/6, RULED two named tests (WQ-644 A, §7) · BMA holds FY2025 statements for ALRe, AARe, ALReI and each ACRA vehicle, unread · Delaware Life ladder unchanged, sale exploration attributed only, Q3 not posted · cyber: no change.

## 0u / 0m ②②b③⑥ — ROTATED 2026-11-11

Verbatim → `archive/STATUS_ROTATED_SECTIONS_2026-11-11.md` (crc32 `5fcf94c5`, `tail -n +5`). L781 10/29 ratio readings (DLIC Key Ratio #2 NOT RED on L1; SHADE-R/T v1 first readings) and the 10/1 ARI/DLIC/coordination rails.

## 0t / 0s / 0m ① — ROTATED 2026-11-06

Verbatim → `archive/STATUS_ROTATED_SECTIONS_2026-11-06.md` (crc32 `0fe75ab2`, `tail -n +4`). W1 RULED 10/15 (WQ-364): bloc claim WITHDRAWN, AARe Note 14 gap survives.

## 0r / 0o / 0n — ROTATED 2026-10-21

10/12 gap-pass verdict (evidence PARTIAL; no 30% breach; composite 20/30), 10/12 L673 rails (superseded by the 10/15 grade) and 10/10 history → verbatim at `archive/STATUS_ROTATED_SECTIONS_2026-10-21.md` (crc32 `11d53b30`, `tail -n +4`). Evidence → `research/GAP_INVESTIGATION_2026-10-12.md`.

## 0m. 2026-10-01 — LIVE RAILS

**④ Delaware Life remediation — PRIMARY plan (issuer 9/11, read 10/12):** Aug17 agreement exchanges **up to $6.5B** for equivalent unaffiliated assets from TWG; approval required, target before Q3 filing. **Plan ≠ completed exchange or forced market sale**; issuer disclaims external reduction mandate. Marker(4) remains PARTIAL: amount/target sourced, execution unverified. Bases and pro forma interpretation → targeted freshness research.

**⑤ Carried primary figures (8/28, DLIC Q2 statutory — basis → `REFERENCE.md` §2Q):** 1H-26 direct premiums + deposit-type **$6,726M (+13.9%)** · surrenders **$2,061M (+44.6%)** · ratio **24.1% → 30.6%** · affiliate-contingent **$16,822M = 32.82% of $51,249M GA** (12/31/25 **$16,372M = 35.67%** — quote the PAIR) · C&S **$4,028M** · Illiquidity **10.05% GA FLOOR; charter denominator unresolved** · going concern NEGATIVE · no permitted practices · FHLBI **#2 borrower $4,963M, flat two quarters** `[CONF BROCK 8/28]`.

**⛔ GUARDS.** (1) **No POST-PAUSE flow figure recovered; Q3 publication still expected ~11/15.** (2) **12× leverage RETRACTED — filing says 5.1×.** (3) **n=2 distributors of an unknown denominator; "paused" ≠ terminated; no current enforcement disposition recovered in the bounded10/12 pass, absence not proved.** Refutation pre-registered: probes close with no charges AND a distributor resumes ⇒ marker (0) reverts, recorded FALSE POSITIVE. (4) **Never quote S2 without S1; never difference NPORT +37.8bp (pooled) against 7/27 +40.2bp (paired).**

---

## 1. Top-line read

**Fund-level stress is BROCK's confirmed domain; a live insurer-wrapper systemic cascade remains unproven.** The fixed-window `T-SHADE-01` grade was NOT MET at the 11/6 close (read 11/6, dated reading); the 10/10 owner fire remains provisional. The conditional statutory dig tests collateral re-marking and overlapping insurer equity/lending exposure. A basket reading supplies no insurer loss by itself.

---

## 3. Signal dashboard

**Convergence index:** 5 🔴🔴 firing → 4 🔴 → 3 🟠 → 2 🟡 → 1 ⚪/🟢. Independence = shared-antecedent flag.

| # | Vector | Score | Independence |
|---|---|---:|---|
| 1 | Insurer asset-transfer / affiliated exposure | **5 🔴🔴 FIRING** *(since 7/27; 8/28 + 10/1 = BASIS changes, scale max)* | Independent |
| 2 | AMAPS / rated structured wrappers | 4 | Independent |
| 3 | Funding fragility: FABN/FHLB | 3 | Independent |
| 4 | Regulatory capital: NAIC/AG55/SVO | 2 | Independent |
| 5 | Ratings / valuation machinery | 3 | Independent |
| 6 | BROCK stress translation | 4 | ⟂ BROCK-owned; shares Q2 wave w/ #7,#8 |
| 7 | Insurer-lender double-jeopardy | 3 | ⟂ count the wave ONCE |
| 8 | Lee Robinson $1.8T insurer-short | 3 | ⟂ corroborates #7 |
| 9 | System transmission | 2 | ⟂ LIQUID/REGINALD/NEXUS-owned |

**Composite (#1–5,7): 20/30, unchanged.** ⚠️ **The firing vector is SINGLE-NAME and moved on mechanism, not realized loss — guard against reading it as cohort credit stress.** Per-vector evidence → `REFERENCE.md` §3D/§3R.

| Vector | Live read |
|---|---|
| **#1 Asset-transfer** | 🔴🔴 Delaware Life: affiliate-contingent **$16,822M = 32.82% GA** (pair: +2.75% $ / −2.85pp share). SSAP-25 filer-self-defined test. S&P **A- NEGATIVE**. Marker (0) MET 8/28. 🆕 **Up to $6.5B parent exchange (issuer9/11), target before Q3 filing/approval required; execution unverified.** ⚠️ No realized loss established; no newer enforcement disposition recovered, absence not proved. |
| **#2/#5 Ratings, AMAPS, Athene perimeter** | FiveQ2AMAPS positions$13.515B namedfloor; AHL/WHCOguarantee primary15%O, Ounknown. **Athene's US insurer detail PUBLIC quarterly**; economicallocation remainsmissing. ~$7.4B ≈ 85% of the ARI price landed at AAIA BY DATE — ⚠️ ARI identity UNDETERMINED by the 10/1 rule-based match (31.4% matched; `research/ARI_ATTRIBUTION_MATCH_2026-10-01.md`). Egan-Jones: 8/12 denial ≠ revocation, ladder 🟢 not advanced. |
| **#3 FABN/FHLB** | 🟠 kill-path-1 **YELLOW**; NPORT +37.8bp (6/30), Athene T+112 vs deck T+110; RED bar >250bp far. 🆕 9/30: S2 34.2%, FHLB room $3.9B (§0v). |
| **#4 NAIC/AG55/SVO** | 🟠→🟡 Adopted AG55 + final2025YE template read: scoped/confidential analysis; dedicated L3/PIK/PLR fields absent there, blanket public mandate unsupported. Final2026 template unresolved; no frozen-spec change. |
| **#7–9** | Double-jeopardy lender leg refuted at named-entity level · Robinson allegation-grade · system 🟡/🟠: **HY 348 [11/5], LIQUID's series.** **`T-SHADE-01`: NOT MET at the 11/6 close (read 11/6, dated reading); 10/10 fire PROVISIONAL. Dig conditional on MET (§10 #8); score unchanged.** |

---

## 4. Insurer-wrapper transmission map

**Full map → `REFERENCE.md` §4.** Stages: **1** BROCK fund stress → **2** assets move into insurer/captive/rated structure → **3** capital/rating treatment masks risk → **4** funding channel accelerates → **4b** distribution channel closes (liability-side inflow; added 8/28) → **5** system bridge. 🆕 **10/1: stage 2 is now OBSERVABLE at the US insurer entity quarterly (AAIA Schedule B/D/BA Pt 2-4) — the gap was mine, not the issuer's.**

---

## 6. Regulatory / funding calendar — FORWARD rows only

| Date / Window | Item | SHADE read | Status |
|---|---|---|---|
| **Ongoing — SHADE-OWNED** | 🔴 **Delaware Life / Clear Spring — SDNY + SEC probes: ESCALATION LADDER** | **(0) COUNTERPARTY/DISTRIBUTION — ✅ MET 8/28** (Truist + Fifth Third paused; n=2, share unsized) · **(1)** charges/Wells · **(2)** further rating action (S&P A- NEG) · **(3)** Delaware DOI action · **(4)** remediation forced-sale size/timetable — 🆕 **PARTIAL: up to $6.5B/target before Q3 filing (issuer9/11); approval/closing unverified** · **(5)** Clear Spring own restatement — issuer table read,83607 verified; full statutory capital/funding bridge owed · **(6)** probe widens to Guggenheim AM. Rungs are INDEPENDENT unless ordering is sourced. | **Live — (0) MET, (4) PARTIAL** |
| ✅ **GRADED 11/11** | **`T-SHADE-01`, endpoint 11/10 close** | Level MET through 334 [11/9], sign NOT MET (+2.62% vs +8.88%, both up) ⇒ **NOT MET, no dig**. Next eligible endpoint 11/11 close. | Done |
| **2026-11-15** | **NAIC Fall National Meeting, Dallas** (Life RBC WG 11/15, GOES governance; offshore-reinsurance and private-credit agenda) | SECONDARY (previews; NAIC PDF 403s this box). Vector #4 watch, no letter. | Forward |
| **~2026-11-15** | **Delaware Life Q3-2026 statutory** (issuer page, free) | Exhibit 1 + SoO L15 vs the 1H-26 baseline. **Not posted 11/11** (index shows Q1/Q2 2026). 🆕 **Also: gross completed TWG transfers/assets/marks in Note10/subsequent events, then reconcile affiliate dollars vs$16,822M; net decline alone cannot prove execution.** ⚠️ ≤1 of 3 months post-pause; first clean read FY2026 annual ~2027-03-01. | Forward — dated |
| **11/12 → 11/18** | **Athene FI call 11/12 and Q3 deck** + **AAIA Q3 statutory (same IR page, not posted 11/11 10:1x ET; newest deck is Q2)** | 10-Q read 11/6 (§0v). First GRADED canary needs the deck for S3 and the penalty. **AAIA Sch B/D Pt 2-4 cross-checks landing claims and AI names.** | Forward |
| **Standing / source gap** | **AG55 final2026 template / VAWG findings** | Adopted text + final2025YE template recovered10/12. Blanket public L3/PIK/PLR mandate unsupported. Final2026 revision and completed submissions unverified. | Final2026/submissions not obtained |
| **2026-11-18** | **C2 withdrawal test — SELF-EXECUTING** | penalty ≤+48bp AND S1 ≥$2.0B AND S2 ≥36.2% ⇒ withdraw C2. 🆕 S2 34.2% fails, so no withdrawal absent a restatement. | DOCKET row live |
| **2026-11-30** | **W3 deterioration test** (BROCK grades) | ≥3 of 4 channels reversing ⇒ deterioration read withdrawn. | Forward |
| **Standing** | **W2 ordering test** (shared with BROCK) | Gated instrument firing before/with the non-gated channel ⇒ RETRACTION owed. | Live |
| ✅ **CLOSED 9/29** | **MBA Q2 / `PRED-CREED-006`** | **FALSE: +$7.83B < +$10.0B** (CREED graded). `PRED-CREED-010` **PARTIAL, NOT SCORED (Will).** | Closed |
| ✅ **DELIVERED 10/1** | **W1 legs (a)+(b)** | §0m ①. All four legs in 10/2. | Done — **WQ-364 RULED 10/15: bloc claim WITHDRAWN, Note 14 gap survives** |

*(Five MONITOR-class rows → `REFERENCE.md` §6M; no date, nothing comes due.)*

---

## 7. Cross-agent dependencies — read the OWNER, never re-derive

- **Fund gates / BDC stress / BCRED / First Brands** → BROCK. SHADE translates the insurer implication only.
- **HY OAS series + its readings** → LIQUID. SHADE owns only whether `T-SHADE-01` fires. ⛔ **Not X1, not L494's 3-obs proposal** — X1 and `T-SHADE-01` stay two named tests with shared inputs (WQ-644 A, Will 11/6 20:31 ET, `PROME/proposals/2026-11-06_wq642-644-RULED.md`); the FORUM-5 'one instrument' ruling closes, no gate or letter moves.
- **CCC channel** → **`CCC/HY` = REGINALD `VX-REG-18.04`; `CCC/BB` + gap = BROCK `KB-BRK-221`.** SHADE registers neither. 🔴 **Same 787-obs series ⇒ agreement is ARITHMETIC, never corroboration.**
- **Bank/NDFI/FHLB, Truist and Fifth Third as banks** → REGINALD. ⛔ An FHLB is a cooperative, not a bank credit story.
- **CRE/CMBS series + triggers, MBA/Z.1 sector reads** → CREED. 🆕 **Packet 10/1: AAIA (a US life insurer) took ~$7.4B on 4/24 — the sector's +$3.6B commercial print is not evidence of diversion outside the US life sector.**
- **Synthesis** → `NEXUS_BRIEF.md`.

---

## 10. Next actions — OWED, in order

🆕 **IREN Mackenzie (BROCK 11/6):** no insurer established as a holder; PIMCO ABL 10-Q ~11/16 and N-PORTs ~11/29 are the next look, BROCK's search stops at EDGAR full text.

**Items carrying a lapsed 10/8 or 10/23 date below are re-dated 2026-11-20 unless marked; the conditional `T-SHADE-01` dig (#8) stays ahead of them.**

0. ✅ **DLIC FY2025 annual pulled (L241), 10/1 touch 2** — ratio #1 **1.62%**; ratio #2 **GA-only9.75% floor / ≈37.2% conditional**. 🔴 **Owed: REGISTERED ABS-leg/GA denominator/perimeter definition.** Same-audit analysis completed; evidencedABS proposal delivered for PROME/Will ruling; no grade. Affiliate-contingent bonds are not the formalABS category. **NAIC SVO override COUNT still owed** (never record zero).
1. 🔴 **ARI match = UNDETERMINED (31.4% strict).** Next: ① find the **~20% holder** on the ~0.8 cluster (ACRA? managed accounts? — §2.8's designees) · ② ARI DEFM14A (acc 0001193125-26-119995) for a loan-level annex · ③ AAIA FY2026 annual Schedule B for carrying value vs cost on the $265.6M non-accruing rows.
2. ✅ **11/6:** `thesis/PREDICTIONS.tsv` created, SHD-01 to 03 registered. **F-SHADE-01 thesis falsifier written** (research record §11): test 2027-03-31 on FY2026 filings, gated on HY >300 for 30 sessions. 🔴 **Declared-flat TRADE surface still owed, re-dated 2026-11-20.**
3. ✅ **MEMORY.md rotated 11/6.** Carry the promotion candidate: *"the opacity claim was falsified by documents in my own directory."*
3b. **ARI DEFM14A read** (acc 0001193125-26-119995, 2026-03-23) for a loan-level annex — **re-dated 2026-11-20.**
3c. **Illiquidity ABS leg + denominator/perimeter/vintage** for charter ratio #2 — **proposal to PROME; LAPSED 10/8; by 2026-10-23.** Same-audit GA9.75/37.24% vs total6.92/26.42%; formalABS/liquidity distinct. Proposal delivered, approval and30% grade still withheld. 🆕 **10/21: exact criterion + unknown rule DELIVERED (L726 → `research/L726_ILLIQUIDITY_BASIS_2026-10-21.md`); TSR method (L727 → `research/L727_TSR_METHOD_2026-10-21.md`): TSR UNAVAILABLE, SHADE-R/T v1 proposed. Both await Will's word via PROME WQ rows. WQ-422 Clear Spring documents are Will's hands; not chased.** ✅ **10/29: RULED A/A, ENCODED + first readings done (§0u, L781).**
3d. **NAIC SVO override count** — **re-dated 2026-11-20** (never record zero). 🆕 **PROME re-keys D:L241 to a dated 11/20 row for this count alone (prome-2b 11/11).**
3f. 🆕 **BMA entity reads:** ACRA 1A/2A FY2025 Level 3 and related-party notes; Catalina FY2025 (posted 11/4). **Deck read at 11/12:** S3, penalty, C2 execution. **AAIA Q3:** name-level AI and SoftBank lines.
3e. 🆕 **Guggenheim Universe lead — primary verification** once WALTER pulls the 23-page doc: DLIC Q2 Sch D (in hand) for the "Chicago-street" LLC family, then EquiTrust / Security Benefit statutory (issuer routes first). Assessment 10/10 = ADDS (§0n ③).
4. **Delaware Life TWG implementation evidence** — issuer9/11 primary PLAN now read; approval/closing still missing. DLIC Q3 Note10/subsequent events before~11/15.
5. **AG55 residual:** adopted text/final2025YE template recovered10/12; final2026 revision/completed filings unverified. Blanket public L3/PIK/PLR premise unsupported; re-spec belongs to PROME/Will.
6. **Clear Spring fullstatutory** (marker5);83607 verified, freefinancialsummary notobtained; own correctedFY25/Q1/Q2 needed.
7. **Apollo Q2 Retirement Services cross-check COMPLETE10/12** (Notes4/16/17); AMAPSfloor/ACRA/guarantees/collateral reconciled. Loan/tranche allocation and netloss remainmissing; no historicalgrade changed.
8. **L673 — GRADED 11/11, endpoint 11/10 close: NOT MET, no dig** (10/15, 11/5, 11/6 same result). Next assessment re-reads both legs fresh on the latest completed close; 🆕 design question (10/23 slot): an eligible endpoint that passes unassessed — prospective only. Historical 10/10 owner fire PROVISIONAL, unconfirmed. **If a later eligible assessment is MET:** (a) AAIA FY2025 Schedule BA → ADS equity holding · (b) ADS facility counterparties · (c) F&G > Brighthouse > Corebridge Schedule BA · (d) BROCK cross-check. Other standing dig triggers retain their existing letter (FABN >250bp, RBC breach, enforcement escalation). **No dig absent a qualifying trigger.**
9. **Watch:** a THIRD named distributor pausing · the next public FABN syndication · 🆕 **Blue Owl's insurance mandate push** (FT 10/7 relay; no insurer purchase).

---

## BOTTOM LINE

**[2026-11-11] Nothing new has posted for the insurers I follow, and my trigger still reads not met.** Athene's Q3 investor deck (call 11/12) and the Q3 statutory statements for Athene's US insurer and Delaware Life were not up this morning. Through the 11/10 close, private-credit funds rose 2.62% and their managers 8.88% since 9/24, so no dig. A hiking Fed (2-year Treasury 4.73%, up 0.22 points since 11/6) squeezes the two links I already called thinnest, Athene's remaining Federal Home Loan Bank room ($3.9B) and its shift to secured funding, and adds surrender pressure at Delaware Life; my funding-spread band does not see a base-rate move, and my trigger gets harder to fire because private-credit funds earn more at higher rates. Clear Spring's affiliated book was about five times its surplus at year-end 2025.

**[2026-11-06] Athene's Q3 filing shows more secured funding, more hard-to-value assets and more AI credit, but no recognized credit loss of size yet.** Unsecured funding fell to 34.2% of the funding-agreement stack, and room at the Federal Home Loan Bank fell to $3.9B. Level 3 assets rose $14.9B, just under my line. The GAAP loss is mostly rate marks, though seriously delinquent mortgage principal nearly doubled this year. The AI cards reach Athene through SoftBank ($4.8B) and Oracle ($2.4B), plus $6.2B of unfunded Anthropic-chip commitments. Nothing moved a score. Who holds the SoftBank paper's risk after ACRA, and what the 11/12 deck says about public issuance, are the next two reads. At the 11/6 close my trigger for the statutory dig still reads not met: private-credit funds rose 0.79% and their managers 4.14% since 9/24, and no Q3 statutory filing or deck had posted.

Prior bottom line (10/29) → `git show cf97c133c:AGENTS/SHADE/STATUS.md`.

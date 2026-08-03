# OTTO STATUS archive — 2026-08-03 (session 017 line-cap pass)

*Archived: the session-016 (Jul 25) boot-pointer block, moved out of `STATUS.md` when the
s017 pointer was written. Historical only — do not cite rows as current state. Canonical
live state → `STATUS.md`; thesis pivots → `thesis/CHANGELOG.md`; dated events →
`docket/CATALYSTS.tsv`.*

---

## Session 016 boot-pointer (Jul 25 2026) — as written, superseded 2026-08-03

> **📌 Session 016 (Jul 25 — 21-day-dark catch-up + T-3 pre-7/28 sweep):**
> - **🔴🔴 HEADLINE — DOJ HAS CRIMINALLY CHARGED BOTH OF OTTO'S THESIS MECHANISMS.** A **superseding 8-count indictment** (unsealed **Jun 24**) vs founder Daniel Chu alleges Tricolor executives *"manipulated delinquent loan data to make non-performing loans appear current"* **and** *"pledged the same collateral to multiple lenders simultaneously"* + fictitious payment records + falsified borrowing-base reports. **The Invisible Exit (DQ-chain bypass) was OTTO's own inference from data; it is now a federal criminal allegation.** DOJ invoked **18 U.S.C. §225 — the "financial kingpin" statute, 10-years-to-life mandatory minimum**, used a handful of times since the S&L crisis and not in over a decade. Alleges a **continuing enterprise from at least 2018** → *originations* tainted from 2018. **⚠ CORRECTED Jul 25 (RP-OTT-1.6): the '2018-2021 vintages' framing was overstated by me — Tricolor securitized only TWO deals in that window (TAST 2018-2, 2021-1) with a 32-month gap; 9 of 11 deals are 2022-2025.** Securitized impairment concentrates where OTTO already looks. Lead retired. Chu pleaded not guilty Jun 30. **Ex-COO David Goodgame pleaded GUILTY Jun 24 (6 counts) and is COOPERATING** — flipping from his Jan-2026 not-guilty plea; **fires OTTO's standing 🟠 cooperating-witness trigger → CARL/REGINALD.** ⚠️ **All four events landed BEFORE OTTO's Jul 4 session and were missed then too** — the criminal track was never being swept (see CHANGELOG calibration note).
> - **Tricolor trial RE-DATED Oct 19 2026 → Jan 25 2027** (Castel; Feb 1 2027 reserved as alternative) `[Inner City Press Jul 7]`. **The Oct-19 fraud-surface catalyst leaves 2026 entirely.** Jul 29 survives as the date-*confirmation* node, not the decision node OTTO had docketed.
> - **🔴 NEW COCKROACH-ADJACENT EXPOSURE — Triumph Financial (TFIN/TBK Bank) `[CONF SEC 10-Q, filed 2026-07-21]`.** TBK is **agent bank on a $60.5M Tricolor floorplan facility, holding ~$22.5M**, secured by a claimed **first-priority interest in Tricolor vehicle inventory**. As of Jun 30 2026 TBK says collateral "adequately secures" the balance — **no charge-off, no reserve disclosed, 9.5 months after the Ch.7 filing** — while conceding *"other creditors have asserted that they have interests in some of the collateral."* Two firsts for OTTO: (a) **the double-pledge mechanic now appears in a THIRD collateral class** (floorplan/inventory, alongside ABS warehouse + the $113M receivables escrow); (b) TBK's "adequately secured" claim rests on the very inventory OTTO's own data says is **~30,000 vehicles missing / ~3% realized recovery**. **A $60.5M syndicate means ~$38M sits with unnamed participants — a live, unexhausted bank-discovery channel.**
> - **OTTO-30 near-falsified 45→12%** — a **complete** EDGAR full-text scan (not a press sample) of every operating-company filing mentioning "Tricolor" for the whole window (2026-04-15 → 07-25) returns **zero NEW US bank names**. Every bank in-window (MTB, TFIN, OBK) disclosed *before* the window opened. **TFIN is a 7th known-unknown predating the window — the OBK trap, second occurrence.**
> - **OTTO-31 collapses 30→12%** — MTB Q2 (Jul 15) posted **record EPS $5.32 vs $4.66 est**, no custodial wind-down language, and affirmatively promotes Wilmington Trust's custody franchise (CEO named *CEO of the Year for Clearing & Custodial Firms*). Second corporate-side disconfirmation; the plaintiff allegation is not surviving contact.
> - **⚠️ OTTO-32 REFRAMED (85% held, resolution mechanics changed):** Jul 28 is **not** a same-day resolver — press describes a **multiday, contested confirmation trial** with privilege disputes and "a wall of objections" incl. the UST. Expect a *process* outcome on 7/28, not a verdict. Still comfortably inside Sep 30.
> - **CVNA Q2 earnings = Wed Jul 29 after close** `[CONF Businesswire/IR]` — **was entirely absent from the docket.** Stock $70.66 (Jul 16) → **$60.46** (Jul 24, −14.4%); no company-specific catalyst found — PT trims (Jefferies $95→$90, RBC $92→$85) + rate-sensitivity/risk-off. Gotham precedent = report dropped **on earnings day** (Jan 28). Short-seller T-7 protocol is now T-4 and was unrun.
> - **New bank loss — Western Alliance (WAL) $126.4M** vs Jefferies/Point Bonita, First Brands receivables "largely fraudulent or non-existent." ⚠️ **Filed 2026-03-06, not 7/21** — PROME's packet dated it to a 7/21 re-coverage item; corrected back to PROME.
> - **🔴 SUMMER RE-DETERIORATION CONFIRMED — the watch is resolved.** Built a **10-D performance panel** (`scripts/panel_10d.py`) after S&P/KBRA were tested and found closed. **7 of 7 deals, both tiers, four vintages: 60+ DQ troughed in the spring tax-refund window and has risen every month since — every deal is now ABOVE its first-observation level** (+0.89 to +1.57pp off trough). This is the deterioration OTTO could not observe all session because Fitch's obtainable data stopped at March; the panel answered it within hours. **⚠ BROAD subprime is NOT insulated** — off-trough it has risen *slightly faster* than deep (+1.44 vs +1.26pp mean); in the latest month deep is marginally faster (+0.61 vs +0.46pp). The honest read is **comparable, not contained** — which still cuts against the "deep bleeds, broad is fine" framing.
> - **Boot-kit: 2 defects found + fixed** (fired-catalyst rows were being priority-filtered out of the boot; look-back window now auto-sizes to time-since-closeout). — *Jul 4 pointer below.*
>
> **📌 Prior sessions:** boot-pointer blocks for **session 015 (Jul 4 — 2022-vintage 10-D bifurcation, OTTO-04 68→62%, Fitch-lag finding, ML.tsv repair)**, the **Jul 4 catch-up sweep (OTTO-05 + OTTO-28 falsified, OTTO-32 → Jul 28)**, and **Jun 9 / Jun 8 / Jun 2 infra passes** archived to [`workbook/STATUS_archive_20260725.md`](workbook/STATUS_archive_20260725.md). Thesis pivots → [`thesis/CHANGELOG.md`](thesis/CHANGELOG.md); structural history → [`MAINTENANCE.md`](MAINTENANCE.md).


---

## Sections retired from STATUS.md at the s017 line-cap pass (2026-08-03)

### MFS duplicate standalone section (lines 120-122) — content preserved in the Tricolor-gridlock+MFS vector

### MFS (Cockroach #4) — CONFIRMED Feb 26
UK mortgage-finance. Barclays + Atlas SP (Apollo) = £2B+. Shortfall £1.3B ($1.7-1.8B). Same double-pledging mechanism as Tricolor. Bloomberg: "regulatory black hole."


### Carvana pre-earnings T-4 watch block (lines 160-166) — event fired 7/29, superseded by the POST-PRINT vector

### Carvana — 🟠 T-4 to earnings, short-seller window OPEN (Jul 25) [SUPERSEDED — event has passed]
**Q2 earnings Wed Jul 29, after close, call 5:30pm ET** `[CONF Businesswire/investors.carvana.com]` — consensus ~$0.42 EPS / ~$6.88-6.97B revenue. **This date was missing from OTTO's docket entirely** (now added). Price **$60.46** (Jul 24) after a 6-session slide from **$70.66** (Jul 16) = **−14.4%**; no company-specific catalyst identified — sell-side PT trims (Jefferies $95→$90 Jul 14; RBC $92→$85) plus rate-sensitivity/risk-off. YTD ≈ −24%.
**The live risk is timing, not direction.** OTTO's own CLAUDE.md short-seller protocol calls for a T-7 sweep; T-7 was Jul 22 and it was not run (OTTO was dark). Gotham's Jan 28 report — the related-party/DriveTime thesis that *is* OTTO's Carvana sub-thesis — landed **on earnings day**, and the Feb 18 CVNA lesson is explicitly that short-report timing was not factored into an exit. A weak tape into a binary event with an active, previously-published short thesis is the exact setup that rule exists for. **No position (TRADE.md FROZEN), so this is a watch, not an exposure** — but if a re-entry is ever contemplated, it does not happen in the 48h before Jul 29.
*(Prior Jul 4 read below — superseded on price/positioning, intact on substance.)*

*Jul 4 "thesis patience" Carvana block (pre-collateral-read, pre-slide) archived to [`workbook/STATUS_archive_20260725.md`](workbook/STATUS_archive_20260725.md).*


### Private Credit systemic block (lines 123-125) — BROCK's domain, Feb-Apr stale, retained in dashboard row

### Private Credit — 🔴🔴 SYSTEMIC
9+ funds gating/restricting. BCRED, MS North Haven, BlackRock HPS, Cliffwater, Blue Owl. Fortune: "$265B meltdown." El-Erian: "2007-like." Economist: Dimon "cockroach" metaphor. Alt managers ~40% AUM from retail — retail wants out, can't get it.


### Resolved CRITICAL TIMELINE rows Apr 27 – Jul 21 2026 (archived at s017)

| Date | Event | Status |
|---|---|---|
| **Apr 27** | **First Brands: examiner (De Luca) files INTERIM report — then PAUSES, $7M budget exhausted** | 🔴 **NEWLY DISCOVERED (swept Jul 25)** — unintegrated primary. Finds James ran a web of entities "not as a for-profit business, but as **a liquidity generating and value extracting enterprise**"; ~90 days' further work offered *if* funded. **No docketed report deadline exists** `[PRESS Bloomberg Law/TT/TPS]` |
| **Jun 24** | **Tricolor: superseding 8-count indictment vs Chu unsealed (§225 "financial kingpin", 10yr-life min) + COO Goodgame pleads GUILTY & cooperates** | 🔴🔴 **NEWLY DISCOVERED (swept Jul 25)** — happened 10 days before the Jul 4 session and was missed then; criminal track was unswept `[CONF DOJ via Reuters/Bloomberg/NatLawReview]` |
| **Jun 30** | Tricolor: Chu arraigned on superseding indictment — pleads NOT GUILTY | ✅ **NEWLY DISCOVERED (swept Jul 25)** |
| **Jul 7** | Tricolor: Castel re-dates executive trial **Oct 19 2026 → Jan 25 2027** (Feb 1 2027 reserved as alternative) | ✅ **NEWLY DISCOVERED (swept Jul 25)** `[Inner City Press Jul 7]` — Oct-19 catalyst exits 2026 |
| **Jul 13** | First Brands: parties ordered to update Lopez on the James criminal proceedings (stay-modification consideration; debtor suits vs James + Onset seek **>$2.7B**, currently stayed) | 🟠 **NEWLY DISCOVERED (swept Jul 25)** — was never on OTTO's docket; outcome not yet public `[PRESS Law360/Octus]` |
| **Jul 14** | Q2 bank earnings open (JPM/WFC/C) — OTTO-30 forward-discovery | ✅ **SWEPT Jul 25 — NO new Tricolor-exposed US bank.** Complete EDGAR FTS scan of window returns zero new names → OTTO-30 45→12% |
| **Jul 15** | Fitch Auto ABS Index ("Jun print") | ✅ **SWEPT — NO NEW DATA.** Latest available remains **March** data (DQ 6.11% / ANL 8.80% / recovery 37.48%). Summer re-deterioration still unobserved; OTTO-04 input 4 months stale by data-month |
| **Jul 15** | M&T Bank (MTB) Q2 2026 | ✅ **SWEPT — cuts AGAINST OTTO-31.** Record EPS **$5.32** vs $4.66 est; rev $2.53B; no custodial wind-down language; Wilmington custody franchise actively promoted → OTTO-31 30→12% |
| **Jul 20** | First Brands creditor-vote deadline (6pm ET) | ✅ **RESOLVED Aug 3 at the docket.** Secured Classes 3/4/5/6 accepted **100% by number AND amount at every debtor**; **Class 7 GUC REJECTED at 83 of 92 subclasses** → §1129(b) cramdown required `[CONF Dkt 3351]` |
| **Jul 21** | Ally (ALLY) Q2 2026 earnings, 7:30am ET | ✅ **SWEPT** — retail NCO **1.57% (−18bps)**, 30+ DQ **4.80% (−8bps)**, 5th straight YoY improvement. Bifurcation widening; no Carvana-specific break-out (OTTO-28 postscript closed) |
| **Jul 21** | Triumph Financial (TFIN) Q2 10-Q — **$60.5M Tricolor floorplan / $22.5M TBK-held, unreserved** | 🔴 **NEWLY DISCOVERED (swept Jul 25)** `[CONF SEC 10-Q]` — see ACTIVE VECTORS |

### Outbound Signals table (archived at s017 — statuses were stale to Feb/Mar 2026)

## Outbound Signals

| To | Priority | Signal | Status |
|----|----------|--------|--------|
| REGINALD | 🔴 | Bank losses ~$1.8B+; MFS UK Barclays/Atlas SP £2B+ | ✅ DELIVERED |
| BROCK | 🔴 | BCRED $3.7B redemptions; TCPC class action | ✅ DELIVERED |
| CARL | 🔴 | DQ 7.1% RED; SoFi CNL triggered | 📤 QUEUED |
| NEXUS | 🔴🔴 | Consumer durables demand destruction confirmed | 📤 QUEUED |
| LIQUID | 🟠 | BCRED gate breach | ✅ DELIVERED |

---



### Wilmington Trust vector, full text (archived at s017 — compressed in STATUS, OTTO-31 at 12%)

### Wilmington Trust + successor-trustee vacuum — 🟠 low-activity, OTTO-31 at 12%
Sep 20 2025 30-day notice to resign as Tricolor ABS indenture trustee/custodian (7 trusts 2018-2025 / $1.8B+) — **narrow, Tricolor-only and corporate-confirmed**. The broader "exiting all non-mortgage ABS custody" framing came from the Jan 14 plaintiff complaint and is **denied corporate-side** (American Banker Feb 19-20); MTB's Q2 (Jul 15) record results with the custody franchise actively promoted is the second disconfirmation → **OTTO-31 30→12%**. Structural residue worth keeping: **major trustees are reportedly shunning the Tricolor successor role** (Auto Finance News) — the indenture-trustee market can't clear on fraud-tainted post-default ABS. Watch for trustee-substitution filings on the 7 trusts.



### BOTTOM LINE as of s016 (archived at s017)

## BOTTOM LINE

**Fraud-leg 🔴🔴 — DOJ has criminally charged both of OTTO's thesis mechanisms. Systemic-funding-leg 🟠 DISCONFIRMED. The gap between the two legs widened again.**

**The Invisible Exit stopped being OTTO's inference.** The Jun-24 superseding indictment charges Tricolor executives with *"manipulat[ing] delinquent loan data to make non-performing loans appear current"* — that is the DQ-chain bypass, as a federal criminal allegation — alongside simultaneous multi-lender collateral pledging. DOJ backed it with the **§225 "financial kingpin" statute (10-years-to-life minimum, dormant for a decade)** and secured a **cooperating COO**. A prosecutor's charging decision is not proof, but reviving a dormant mandatory-minimum statute is a strong revealed signal about evidence quality. **Both OTTO theses are now externally corroborated by the party with subpoena power.**

Meanwhile the systemic leg kept disconfirming: Ally posted a 5th straight quarter of improving prime/near-prime credit (NCO 1.57%, −18bps), and a *complete* EDGAR sweep found **zero** new Tricolor-exposed bank names. And the fraud leg keeps producing new surface independently — the double-pledge mechanic now appears in a **third collateral class** (TBK Bank's $22.5M floorplan claim on vehicle inventory, carried **unreserved** while other creditors contest the same collateral). **Do not position for a broad subprime-ABS repricing; do keep pulling the idiosyncratic thread.**

**The summer re-deterioration is no longer a watch — it is observed.** OTTO spent this session unable to test it because Fitch's obtainable data stopped in March. After S&P and KBRA were tested and found closed, OTTO built its own 10-D panel — and **7 of 7 deals across both tiers troughed in the spring refund window and have risen every month since**, all now above their first-observation level. The instrument that was missing turned out to be one parser away, in documents OTTO was already reading. **Note the wrinkle: broad subprime is not insulated.** Off-trough it has risen slightly faster than deep (+1.44 vs +1.26pp); month-over-month deep is marginally faster (+0.61 vs +0.46pp). Comparable, not contained — which still cuts against the clean "deep bleeds, broad is fine" framing OTTO has carried since s015.

**One thing got worse, and one thing I claimed got worse turned out not to.** Worse: the fraud-surface catalyst **left 2026** — the Tricolor trial moved Oct 19 → **Jan 25 2027**. Not worse: I said the "at least 2018" allegation made OTTO's 2022-vintage focus too narrow. **RP-OTT-1.6 tested that and it's wrong** — only two Tricolor deals exist in 2018-2021 vs nine in 2022-2025. The focus was right. **What RP-OTT-1.6 found instead is better:** eleven deals cleared third-party diligence over seven years because the procedure reconciles the data tape to *Tricolor's own servicing system* — the system the indictment says was falsified. "The books looked clean" is now documented, with a mechanism.

**The honest scoreboard this session is two prediction downgrades, not an escalation.** OTTO-30 (45→12%) and OTTO-31 (30→12%) both moved hard against OTTO on primary-source evidence. Three of the last five resolved/downgraded predictions failed on *measure* rather than substance — the pattern is real and is now the thing to fix in how claims get written, not a run of bad luck.

**Nearest resolvers:** **Jul 28 First Brands** — now understood as the *opening* of a multiday contested trial, so expect process not verdict (OTTO-32 85% held). **Jul 29** is a double: Castel rules on the Tricolor trial date **and** CVNA reports after close with an open short-seller window and a −14% run-up of weakness into it. **Best remaining discovery lead:** the ~$38M of unnamed participants in TBK's Tricolor floorplan syndicate.


### Tricolor Floorplan Layer (TFIN/TBK) — full text, archived at s017; compressed in STATUS

### Tricolor Floorplan Layer — 🔴 NEW Jul 25 (TFIN/TBK Bank)
`[CONF SEC 10-Q, filed 2026-07-21]` TBK Bank (Triumph Financial) is **agent bank on a $60.5M floorplan facility to Tricolor Holdings, holding ~$22.5M**, secured by a claimed **first-priority security interest in vehicle inventory**. Three things make this a distinct vector, not a footnote:
1. **Third collateral class touched by the same double-pledge mechanic.** OTTO already tracks the ABS-warehouse layer (29,000 double-pledged loans) and the receivables layer ($113M escrow gridlock). Floorplan/**inventory** is a third, and TBK's own filing concedes *"other creditors have asserted that they have interests in some of the collateral in which the Bank asserts a first-priority security interest."* Same pattern, new layer.
2. **The "adequately secured" claim is in direct tension with OTTO's own data.** TBK asserts collateral adequacy as of Jun 30 2026 — against inventory where **~30,000 vehicles are missing (up to $1.1B)** and the auction realized **~3% of debt**. Either TBK's specific collateral is genuinely ring-fenced, or the reserve is coming. **No charge-off and no disclosed reserve 9.5 months post-Ch.7.**
3. **~$38M of the syndicate sits with unnamed participants** — an open, unexhausted bank-discovery channel. This is the most promising remaining lead for a genuinely new Tricolor-exposed name.
**⚠ DIRECT ACCOUNTING CONTRAST (Jul 25) `[CONF SEC 10-Q]`:** **ACV Auctions held its own Tricolor floorplan receivables and provisioned them IN FULL in Q3 2025** — immediately on the Ch.7 filing — writing off **$7.6M** attributable to Tricolor in Q1-2026 alone. **Same borrower, same collateral class, same bankruptcy; opposite accounting.** A non-bank marketplace wrote it to zero on day one while a regulated bank still carries $22.5M at par 9.5 months later. Not proof TBK is wrong — it may hold genuinely ring-fenced units — but it is a comparable counterparty taking the opposite view.
**Syndicate roster: NOT obtainable from EDGAR** (only 10 `"TBK Bank" "Tricolor"` hits, all Triumph's own). The ~$38M sits with non-filers; roster needs the Verita docket (cert-blocked) or UCC-1 searches → **REGINALD's channel**.
→ Routed to REGINALD (sizing) via WALTER. OTTO stops at "the bank is exposed."



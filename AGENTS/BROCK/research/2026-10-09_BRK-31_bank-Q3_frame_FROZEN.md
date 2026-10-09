# BRK-31 — bank Q3 pre-registration FRAME (🧊 FROZEN at commit)

**Written:** 2026-10-09 Fri 10:59 ET (`date`), BROCK, Tier-1 spawn from PROME prome-75. **Frozen at the git commit that adds this file, which is before the first cohort release (JPM ~07:00 ET Tue 10/13).** The commit time is the freeze proof. After that commit, this file is not edited before the Q4 cohort prints. Grades go to `catchups/` and `workbook/KB.tsv`, never into this file.

**What this file is:** it states how each print will be READ against the letter of BRK-31. It is not a new prediction. **It changes no threshold, no population, no confidence and no consequence.** BRK-31's letter (`workbook/PREDICTIONS.tsv`, registered 2026-07-27, 45%, resolves 2027-01-31) governs. Where this frame and the letter disagree, the letter wins. GATE-BRK-R2 is untouched. The OTIC letter stays frozen pending WQ-403.

---

## 1. The letter (verbatim substance)

**Fires (resolves TRUE)** if at least 1 of the 11 mapped banks — **JPM · WFC · C · MTB · CFG · WAL · OZK · EGBN · BKU · AMTB · SSB** — in its Q3 or Q4 2026 print:
- **Leg F1:** discloses a **PC/NDFI-ATTRIBUTABLE reserve BUILD**, OR
- **Leg F2:** **names a private-credit counterparty** in a criticized/classified migration.

**Resolves FALSE** only if Q3 AND Q4 both come back release-or-flat across the cohort with no PC/NDFI attribution, AND CFG's combined capital-call + secured private-credit finance book is still GROWING at Q4. **⇒ Q3 alone cannot resolve BRK-31 FALSE.** A clean Q3 is recorded as "Q3 leg: no fire" and nothing else.

## 2. Reading rules (fixed before the first release)

| # | Rule | Operator |
|---|---|---|
| R1 | **"Q3 print"** = every issuer document for the period ended 2026-09-30: earnings release (8-K EX-99), financial supplement, presentation, earnings-call prepared remarks and Q&A, and the Q3 10-Q (OZK: release + management comments + FFIEC Call Report; it files no 10-Q). Release-day documents give a **provisional** read; the 10-Q/Call Report **confirms or adds**. | — |
| R2 | **BUILD** = the allowance (ACL) on the attributed category at 9/30 **>** the same category at 6/30, OR provision **>** net charge-offs with the excess **attributed by the bank** to that category. A charge-off by itself is **not** a build (WAL's $126.4M First Brands charge-off, H1-26, stays not-a-build — KB-BRK-225). | `>` strictly; no magnitude floor (the letter sets none) |
| R3 | **ATTRIBUTABLE** = the **bank's own words** tie the build or migration to one of: loans to nondepository financial institutions / NDFI / "financials except banks" / nonbank financials; a named BDC, private-credit fund, direct lender or credit manager; capital-call / subscription / fund-finance / back-leverage / asset-based lending to credit funds; a named PC-originated credit where the bank's exposure is to the PC vehicle. **My inference from category totals does not count.** | bank's text, not mine |
| R4 | **COMPOSITION EXCLUSIONS** (each would have inverted a Q2 read): **mortgage warehouse** (WAL ~69% of its NDFI headline; BKU's warehouse book) · **card / consumer seasonal builds** (JPM's Q2 $149M) · **CRE office** · generic **C&I** (BKU's Q2 +$86.6M) · **macro-scenario / weighting** builds with no category named · **AMTB SFR growth artifacts**. A build under any of these labels is NOT F1, whatever its size. | decompose before grading |
| R5 | **F2 "private-credit counterparty"** = the bank's **obligor or counterparty is the PC vehicle or manager itself** (BDC, fund, direct lender, real-estate credit manager), named by the bank. A PC **portfolio company** named as a troubled borrower is NOT F2 (it is a borrower, not the counterparty). Migration = moved INTO special mention / substandard / doubtful / nonaccrual during the quarter. | named + migrated in-quarter |
| R6 | **Third-party reports** (press, analyst notes, Semafor) of a bank's PC reserve **do not grade.** They trigger a read of the issuer document. | primary only |
| R7 | **GS, BAC, MS and any other bank are NOT in the 11.** Their disclosures are recorded as context and never fire BRK-31. Population unchanged. | — |
| R8 | **Supervision is not a print.** The NY Fed visits to JPM/WFC (KB-BRK-319) and any supervisory commentary grade nothing unless a cohort bank's own document shows F1 or F2. | — |

## 3. Per-bank frame (dates verified at the issuer unless marked)

| Bank · date (ET) | Q2-26 baseline (KB-BRK-195; REGINALD 7/25, primary) | What fires F1 | What fires F2 | Not a fire (named traps) |
|---|---|---|---|---|
| **JPM · Tue 10/13 ~07:00** (call 08:30; JPM IR 9/17) | Token build **$149M, card-seasonal**; no criticized build. JPM is admin agent on FSK's revolver, which it TIGHTENED 5/8 (KB-BRK-314) | Wholesale ACL build that JPM attributes, in whole or a named part, to **nonbank financials / NBFI / fund finance / private credit** | A named BDC/PC fund/direct lender in criticized or nonaccrual migration | Card or consumer build; macro-weighting build; trading-led results; FSK facility terms (a tightening is not a reserve build) |
| **C · Tue 10/13 ~08:00** (call 11:00; Citi PR 10/2) | Token **$118M** build; ACL ↓ YoY; criticized neutral | ACL build Citi attributes to **financial institutions / NBFI / private-credit or fund-finance** lending | Same as JPM | Card (Branded Cards / Retail Services) build; macro-scenario build |
| **WFC · Tue 10/13 ~07:00** (call 10:00; **WFC newsroom update 2/20/26 moved Q3 from 10/14 to 10/13**) | **RELEASING office CRE** reserves; NPA **−$824M** QoQ | ACL build WFC attributes to **"financials except banks"** (its C&I NDFI line) or to private-credit / fund-finance lending | Same as JPM | Office CRE moves in either direction; consumer; a growing "financials except banks" BALANCE without a reserve build |
| **MTB · Fri 10/16 pre-open** (call 08:00; M&T PR 9/18, read via syndication) | Criticized **−$700M** QoQ, **9th** straight decline; release-lean | ACL build attributed to NDFI / fund finance / PC | Same | Office CRE criticized (~24%) moving either way |
| **CFG · Fri 10/16** (call 09:00; release pre-open INFERRED; CFG IR 9/10 per REGINALD) | Provision **$134M ↓**; ACL 1.48%; coverage **152% ↑**; capital-call **$8,756M** + secured PC finance **$4,096M** = **$12.85B, GROWING** | ACL build attributed to capital-call or secured private-credit finance | Same | Book growth alone (it is the INVALIDATION leg at Q4 — record the combined figure, operator `>` $12,852M = still growing) |
| **WAL · Mon 10/19 after close** (call Tue 10/20 12:00; WAL Business Wire 10/6 per REGINALD) | **BUILD ~$25M**, one named CRE credit; classified $1,128M; business-credit intermediaries **$3,415M** | ACL build attributed to **business-credit intermediaries** or another PC-lender book | A named PC lender/credit manager in classified migration | **Mortgage warehouse** (~69% of NDFI headline); life-science CRE; Cantor liens; First Brands H1 charge-off |
| **OZK · Tue 10/20 after close** (call Wed 10/21 08:30; OZK release 9/30 per REGINALD) | Classified **$1,215M → $1,282M ↑** while RESG $27.8B → $25.7B ↓; ~**$490M debt-on-debt / note-assignment** book (KB-BRK-185); The Jack $27.7M CO Q1 + San Carlos $14.8M Q2 (KB-BRK-300) | A reserve build OZK attributes to the **note-assignment (debt-on-debt) book** — those loans are to other lenders (Claros, Affinius / Square Mile) | **Claros, Affinius or Square Mile** (or another named credit originator) as the counterparty on a classified / nonaccrual migration | A charge-off on a named property with $0 reserve and no new build (the Q1/Q2 pattern); RESG classified rises on property names |
| **EGBN · Wed 10/21 after close** (call Thu 10/22 10:00; EagleBank IR 10/7 per REGINALD) | ACL **drawn down $26.0M**; NCO **2.78%** ann.; coverage 109.01% | NDFI/PC-attributed build | Same | ACL consumed by realized CRE loss (REGINALD's discriminator) |
| **BKU · Wed 10/21 pre-open** (call 09:00; BKU Business Wire 9/22 per REGINALD) | **BUILD +$8.7M** (C&I-led); warehouse **$877M**, counterparties unnamed | NDFI/PC-attributed build | Same | **Mortgage warehouse** (excluded by R4); C&I build without NDFI label |
| **SSB · Wed 10/21 after close** (call Thu 10/22 09:00; 8-K 7.01 acc 0001193125-26-411326 per REGINALD) | NCO 6bps; classified **$2,227.1M** | NDFI/PC-attributed build | Same | Rate-shock reclassification of CRE |
| **AMTB · Thu 10/22 after close** (call Fri 10/23 09:00; AMTB IR 9/30 per REGINALD) | Classified **−14.7%** via loan SALES | NDFI/PC-attributed build | Same | SFR book-growth artifacts; sale-driven declines |

*Dates for CFG, WAL, OZK, EGBN, BKU, SSB, AMTB are REGINALD's issuer-verified dates (REGINALD `CALENDAR.md`, 10/7) — cited to the owner, not re-read by me 10/9. JPM, C, WFC verified by me at the issuer 10/9; MTB at syndicated issuer text 10/9. GS (Tue 10/13 ~07:30, call 09:30; Goldman PR) is context only (R7).*

## 4. What a result does

| Outcome | Grade | Consequence |
|---|---|---|
| F1 or F2 at any of the 11, surviving R3 + R4 | **BRK-31 RESOLVED-TRUE** at that print (provisional on release text; the 10-Q/Call Report confirms) | 🔴 signal → WALTER (REGINALD, LIQUID); Bank warehouse/NDFI vector 🟠3 re-read at the next convergence rescore (STATUS: "moves only on a BUILD"). **No score is moved by this frame.** |
| Build or migration present but fails R3 (attribution) or R4 (composition) | **NO FIRE**, recorded with the decomposition | Disagreement recorded if I think the excluded build is economically PC — the letter governs |
| Release-or-flat across all 11, no attribution | **Q3 leg: no fire.** BRK-31 stays OPEN | Q4 prints + CFG Q4 book decide FALSE |
| A cohort bank does not disclose the attributed category at all | **INSUFFICIENT for that bank** — named, never read as "flat" | — |

## 5. Weaknesses declared before the data (trap 7)

- **Inversion test:** a token NDFI-labelled build of a few million dollars at a GSIB would fire F1 in a world where private credit is fine (NDFI balances are growing fast, and growth alone draws a CECL build). The letter has no magnitude floor; I do not add one here. **If F1 fires on a build that is small relative to the bank's NDFI book, I will record that alongside the grade** — the grade stands.
- **Panel depth:** GSIB releases often report reserves by segment (consumer / wholesale) and do not split wholesale by NDFI. F1 at JPM/C/WFC may only be visible on the call or in the 10-Q (~early Nov). An empty release is INSUFFICIENT, not flat.
- Regional names (OZK, BKU, WAL) carry the only Q2 reservoir signatures, and all three have composition traps.
</content>
</invoke>

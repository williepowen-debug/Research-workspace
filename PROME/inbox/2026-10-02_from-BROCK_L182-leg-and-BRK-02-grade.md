# BROCK → PROME · 2026-10-02 Fri 09:4x ET · BRK-02 graded FALSE · L182 W1 BROCK leg NOT FOUND · WQ-318 upgraded to FOUND (FSK)

Follow-up task on Will's 09:23 ET "go for all four". Full evidence: `AGENTS/BROCK/research/2026-10-02_BRK-02-grade_W1-leg_WQ-318-facility-notes.md`. $0. No score or threshold moved.

## 1. BRK-02 — "Industry non-accruals rise to >2.5%" (75%, due 9/30): ❌ RESOLVED-FALSE
Graded on the resolver of record (8/13 blind spec, Will-ratified). Every candidate was read at the publisher's own page, in raw text:

| Instrument | Population · statistic · basis | Q2-26 | Prior | Published |
|---|---|---:|---:|---|
| **Octus** (spec §6(a), industry aggregate) | over 170 BDCs · aggregate · cost | **1.90%** | 2.02% Q1 | 2026-09-18 |
| KBRA (§6(b)) | 35 rated; non-perpetual-life **median** · cost | 2.75% | 1.81% Q1 | 2026-09-07 (secondary) |
| Morningstar DBRS (§6(b)) | ~60 BDCs **average** · cost | 3.4% | 3.1% Q4-25 | 2026-08-25 |
| Fitch (the spec's named survivor) | 32 rated | no rate readable by 9/30; 9/16 monitor: "broadly stable" | — | — |

- **Why Octus:** the spec's own 8/13 text sets population = INDUSTRY and ranks the SEC-derived aggregate "best definition-match in principle". The choice comes from that text, not from the values.
- ⚠️ **The instruments disagree, and no tie-break was pre-registered.** The rated-universe medians and averages fire. The gap is the statistic: a dollar-weighted aggregate is held down by the big non-traded funds, while a median weighs each small BDC equally. A "typical BDC" reading of the letter would flip the grade to TRUE on KBRA. That is not the reading the spec registered. DBRS was already above 2.5% before the letter was written, so it cannot show a "rise".
- **Conflict:** the thesis is mine, and the grade goes against it.
- **Contamination:** search summaries showed me values before I qualified any instrument (disclosed).
- **Attribution error caught:** a search summary credited KBRA's 2.75% to Fitch.
- **Invalidation (2 consecutive declines → trim/close APO put) is NOT met** — Octus fell once. No position consequence; the put is Will's in any case.

## 2. L182 W1 — BROCK leg (price-producing-exit denominator): NOT FOUND · bounds only
- **Pre-stated 08:3x:** "FOUND functionally — 10-Qs name exited positions with proceeds vs cost; BDCs only."
- **Actual,** from the Q2-26 10-Qs of ARCC · FSK · OBDC · OCSL · MFIC: exits are disclosed in aggregate, with sales and repayments merged (e.g., ARCC $3,026M in Q2). Named realized items appear only for "significant" gains and losses, which are mostly restructurings. Block sales carry a block price (OBDC, Feb-2026: $357.6M at 99.8% of par, purchasers unnamed). **No filing gives the route and price of each exit.**
- **Where they differ:** my pre-statement over-claimed the surface — the "proceeds vs cost per exited position" I expected is not there.
- **Self-check:** NOT FOUND supports the bloc's opacity claim, which is partly mine. It rests on the five-filing table, not on a failed search.
- **Found instead, cutting against the counter as built:** ARCC sold **$1,087M (Q2) / $2,128M (H1)** of loans to its own affiliate IHAM. That is no-print volume under definition (iii), so the 8/13 "count = 2" is a large undercount if affiliate sales qualify.
- **Not run:** OTF (its CIK lookup failed).
- **Tally:** strict 1 of 4 (CREED) ⇒ not withdrawn; functional 2 of 4 (CREED + SHADE (a)) ⇒ withdrawn. My leg changes neither count. **Per L182 this sends strict-vs-functional to Will** (the test was Will-approved 8/13).

## 3. WQ-318 (optional, done): UPGRADED from NONE FOUND to **FOUND, n=1**
- **FS KKR Capital Corp ← JPMorgan Chase Bank (administrative agent) / ING Capital (collateral agent) syndicate.** Amendment No. 1 dated **2026-05-08** to the 7/16/2025 revolver:
  - commitments **$4,700.0M → ~$4,051.7M (−13.8%)**;
  - margin **+12.5bp** (term SOFR 1.65% → 1.775%; 1.775% → 1.90%);
  - minimum equity covenant floor **$5,048.6M → $3,750.0M**;
  - "non-extending lender" language.
  - Drawn $733M at 6/30. Source: FSK 10-Q Q2-26 (0001628280-26-053783) Note 9.
- **Counter-evidence at the same depth:** ARCC's SMBC line grew $1,100M → $1,600M and its BNP line $1,265M → $1,465M; ARCC's main revolver draw fell $2,028M → $1,566M. OBDC's Truist revolver was extended to 2031 and trimmed −0.5%.
- **Read:** banks are tightening on the weakest large BDC (FSK, 7.1% non-accrual at cost) and expanding to the strongest. **No attributable bank loss was found.**
- **Not read:** OCSL, MFIC, OTF and the non-traded funds' facility notes.
- **No signal row fires:** draws fell. Bank warehouse/NDFI stays 🟠(3) — this is not a reserve build.
- **For REGINALD (L527):** this supersedes the NONE FOUND in my 08:4x pointer packet. Please route, or I will if you prefer.

## Record
KB-BRK-312 (BRK-02 instruments) · 313 (W1) · 314 (FSK facility). PREDICTIONS BRK-02 → RESOLVED-FALSE. STATUS stamp, calendar, REGIME line 1, EXIT §4 and BOTTOM LINE updated. SCRATCH W1 row closed. ⚠️ STATUS is now ~94% of the read-cap budget (`read_cap_check` rc=0); a rotation is due next session.

## COMPLETION — BROCK — 2026-10-02 (follow-up)
STATUS: ✅ DONE
CHANGED: AGENTS/BROCK/{workbook/PREDICTIONS.tsv (BRK-02), workbook/KB.tsv (KB-BRK-312..314), STATUS.md, SCRATCH.md (W1 row), research/2026-10-02_BRK-02-grade_W1-leg_WQ-318-facility-notes.md}; this memo
RESULT: BRK-02 RESOLVED-FALSE on the spec's industry instrument: Octus, 170+ BDCs, 1.90% at cost Q2-26, down from 2.02%. KBRA's median (2.75%) and DBRS's average (3.4%) fire; the disagreement is recorded and there was no tie-break. The W1 BROCK leg is NOT FOUND (bounds only) and differs from my pre-statement, which over-claimed the 10-Q surface. WQ-318 is upgraded to FOUND n=1: FSK's JPMorgan-agented revolver was cut 13.8%, repriced +12.5bp and had its equity floor reset (5/8/26), while ARCC's lenders expanded.
GAPS: OTF not read (CIK lookup failed). Facility notes not read for OCSL, MFIC, OTF or the non-traded funds. Fitch's 2Q26 BDC rate not found.
WILL_NEEDS: W1 strict-vs-functional ruling (L182: BROCK NOT-FOUND ⇒ WQ row; strict 1/4 not withdrawn vs functional 2/4 withdrawn).
FOLLOW-UP: PROME — register the W1 WQ row; route KB-BRK-314 (FSK) to REGINALD for L527 or tell me to; close the BRK-02 docket obligation; optional: whether affiliate sales (ARCC→IHAM) count toward the no-print counter (FORUM ruling 4).

# WAL leg — CRE → regional-bank loss transmission (2026-09-27, Sun)

**Task:** PROME packet `17:24 ET` under Will's objective — *"how CRE distress is reaching regional-bank losses, isolated vs broader, and what would change that."* Plan: `PROME/plans/2026-09-27_cre-to-bank-loss-transmission-PLAN.md` (`e614dee5e`).
**My leg (in order):** (1) reconcile the received Nano corrections + list the remaining lien ownership/priority-at-failure unknowns per property, net exposure with branches OPEN; (2) separate Nano-linked exposure from WAL's broader CRE risk, and say how much of the thesis each carries.
**Reuse:** `research/2026-09-27_nano-banc-receivership-stupin-recovery.md` · `STATUS.md` · `THESIS.md` v2.4 · `SCENARIOS.md` · `workbook/KB.tsv` (KB-WAL-143/148/202/205/206/207/208/209) · fold commit `577ae167e`.
**Contract:** no score / threshold / gate / tool / trade change here — proposals return separately.

---

## PART 1 SUMMARY — corrections status + the one-line net

- **All four received corrections are RECONCILED and folded** (`577ae167e`, s#9). See OBSERVED §A.
- **Net exposure, branches open:** the Nano Banc failure creates **NO new WAL exposure.** WAL's Cantor-fraud exposure is bounded by two *already-booked, dated* components — the **$72.4M gross Cantor residual** ($3.5M specific allowance left, Q1 10-Q, KB-143) and the **$64M purchased protective senior liens** (Q2 deck, KB-123). The failure changes **recovery dynamics** (mixed/worse) ⤵ *(9/28: OPEN on the senior-lien leg across branches A/B1/B2/U; WORSE on the guaranty leg — Nano file §9c)*, not exposure. The **$173.0M Stupin bankruptcy claim (Claim No. 5)** is a *filed claim amount*, unreconciled against the **$98.6M** facility balance — **not booked exposure** (KB-208; CATO NB3).

## PART 2 SUMMARY — how much of the thesis each risk carries

| Risk | Thesis vector | Weight it carries | Live? |
|---|---|---|---|
| **Nano-/Cantor-fraud-linked** | **V2 (fraud/Jefferies)** | **~0% of forward EV** — P&L arc CLOSED at the Q1 $152.5M charge-off; **V2 is EXCLUDED from the live composite.** Forward is a two-way *recovery/litigation* tail on already-charged amounts | Recovery-only |
| **Broader CRE — office / life-science** | **V1b-magnitude (4/5 ACTIVE)** + V1b-broadening (2/5) | **Essentially the ENTIRE live idiosyncratic bear.** Bear-medium **16%** keys on it; resolved by the Q3 print + the **$99M** appraisal | ★ LIVE |
| **Macro / rates CRE** (10Y 5.11%, AOCI Cat III/IV) | valuation / capital-drain leg, mostly sector-wide | Small, tail-adjacent; not the core credit bear | Sector |

**One-liner for PROME:** *For WAL the fraud channel (which the Nano failure sits inside) is a closed-P&L recovery tail carrying ~none of the forward thesis; the live bear is entirely the office/life-science CRE magnitude leg (~16% bear-medium), and that is where CRE distress actually transmits to WAL — through the $99M life-science appraisal and Q3 credit, not through Nano.*

---

## OBSERVED (filing / primary, dated, cited)

### §A — corrections reconciled (settled by `577ae167e`)

| Correction | Source | What it changed | Disposition |
|---|---|---|---|
| **COR-20260927-05** | WALTER, from WAL's own verified complaint | The WAL↔Nano link is a **direct senior-lien link**, not only via the fraud; "participant not victim" too strong | **APPLIED / receipted.** WAL authored the underlying finding; reflected in research §2 + STATUS §NANO BANC |
| **COR-20260927-06** | REGINALD (owner) `d8010b97f` | "$108M BANC+EFSC" = **3 lenders** (BANC+EFSC+Nano, Reuters secondary, no primary split); FDIC retained **~$215M not $260M** (9/22 books); cite REGINALD's **~$120M ≈ 17%** loss (range $110–120M); FDIC's ~$114M=15.5% correct on its own 6/30 basis | **APPLIED / receipted.** Recovery file L57 already carried $215M; loss figure is **pointer-only** to REGINALD §3 per the seam rule (no restated figure on any WAL surface) |
| **DEWEY 2026-09-27b** | DEWEY `b9887abd2` (supersedes its own O1–O3) | Lien status is a **dated observation, not ownership at failure**; "passes to receiver" is the conditional default, **not a finding** | **APPLIED.** Softened STATUS §NANO BANC row + WAL-net + BOTTOM LINE, MEMORY #1b, KB-205 Notes to conditional |
| **CATO NB6 / NB3** | CATO `runs/2026-09-27_1300...` | Keep ownership as conditional branches; **preserve BOTH** dated components ($72.4M gross + $64M liens); don't equate the $173M claim with booked exposure | **APPLIED.** Same edits; dual perimeter now explicit on STATUS + MEMORY |

### §B — the direct lien link (WAL's verified complaint, LA Superior 25STCV24263, 8/18/2025, tier A2)

Nano Banc holds **4 deeds of trust, $28.04M ORIGINAL face**, senior to / alongside WAL on **5 of the 10** pleaded collateral loans (KB-202):

| Loan | Property | Nano DOT (orig. face) | Stated rank | Other senior |
|---|---|---|---|---|
| 32/33 | 23750 Alessandro Blvd, **Moreno Valley** | $9.72M (rec. 9/9/2019); NOD 5/20/2025 | 1st | — |
| 43 | 3700 Inland Empire Blvd, **Ontario** | $4.33M (11/10/2022); NOD 5/20/2025 | 2nd | Preferred $25.9M 1st |
| 44 | 12233 Central Ave, **Chino** | $5.99M (1/26/2023) | 2nd | Preferred $22.4M 1st |
| 45 | 9826 Cedar St, **Bellflower** | $8.00M (9/16/2024) | 2nd | Umpqua $6.47M 1st |

⚠️ Face at origination, **not** current balance; the pleaded list is the complaint's examples, not necessarily WAL's whole collateral pool.

### §C — the recovery-side facts the failure DID move (KB-206/207)

- WAL's **GUARANTY** claims vs Stupin + Marcil were removed to bankruptcy court (adversary 8:26-ap-01076-SC, 6/25/2026); WAL moved to remand 7/27. Guarantor **Andrew Stupin in Ch.11 since 4/17/2026** (8:26-bk-11202-SC); WAL filed **Claim No. 5 ≈ $173.0M** (KB-206/208). Collection **stayed**.
- ⤵ *(9/28: holder after 9/25 unproven — FDIC-R or Sunwest; KB-207)* The **FDIC-R now holds ~$27.7M** (face) of accelerated **Marcil** loans → a well-funded **competing creditor** against the same guarantors (KB-207). **Guaranty leg WORSE.**
- Two debtors (Ontario, Chino) are **investigating avoidance** of the Cantor V liens WAL holds as pledgee → a **NEW two-way collateral risk** (KB-206).
- **Makhijani** (ran Cantor V) arrested ~June 2026, ~$100M bank fraud, "Bank #1" = WAL; trial continued to **1/12/2027** (KB-203). Detained.

### §D — the live CRE / thesis facts (Q2 10-Q, 8-K, filings)

- **v2.4:** EV **$75.96**, PT **$52–76**; weights Bear-fast 2 / Bear-medium 16 / Base 45 / Bull 30 / Tail 7; live-bear composite **11/25** (V2 excluded). Spot **$77.61** [Fri 9/25 close] = **+2.17% ABOVE EV** — margin of safety gone, on **price not evidence** (EV unmoved since 8/20; no vector moved).
- **V1b-magnitude ACTIVE (4/5):** NPL +15% QoQ to **$781M**; OREO count 15→22 "primarily office"; **$99M** life-science office credit on nonaccrual, $0 charged off, borrower brought current end-June, **appraisal pending** (Q2 call, KB-109/112/155-157). Coverage **96% on nonaccrual / 69.1% on full NPL** (state the denominator).
- **V1b-broadening DISCONFIRMED at Q2 (2/5):** 0 new office migrations (N stays 1).
- **CEO Q3 pre-guide (Barclays 9/16, B2, model-extracted, unverified at primary, KB-194):** NPLs $567M→~$500M (−10%), NCO rate + $ below Q2, ACL "well over 100%" of Q3 NPLs (on the *nonaccrual* basis) vs 95%, "six credits… four down, two to go." **Silent on the $99M.** Guidance, not data — the Q3-frame benchmark, no weight moved.
- **KB-209 (this session, web, B2):** life-science / lab CRE — once resilient — now **rising vacancies / biotech capital drying up** (CRE Daily · S&P · Wharton WIFPR). Sector: ~$1T CRE maturing 2026 (~1/5 office); S&P sees bank provisions → 24% of revenue vs 20.8%. **Directional downside pressure on the $99M appraisal base rate.** Secondary, industry-level, **no score moved.**

---

## SCENARIO ASSUMPTIONS (named as such, with basis)

1. **Three lien-ownership states, ALL still open** (research §2; none established for any of the 4 DOTs):
   - **(a)** WAL already bought Nano's liens (would fit inside the $64M; $28.04M face < $64M). *Basis: magnitudes allow it; INFERENCE only, never promoted.*
   - **(b)** Nano still held at failure → liens pass to **FDIC-R or Sunwest** → forced disposition typically **3–9 months** ⤵ *(B1 only — FDIC-retained; under B2 Sunwest is not a forced seller)*. *Basis: NODs on Nano DOTs 5/20/2025 = Nano was enforcing, not selling, mid-2025.*
   - **(c)** Nano foreclosed **pre-failure** → a senior trustee's sale extinguishes WAL's junior interest unless WAL bid; loss would **already be inside** the Q1 $26.1M Cantor charge-off ⤵ *(inference — no filing states it)*. *Basis: NODs recorded 5/20/2025 made a trustee's sale legally possible from ~late 2025.*
2. **"WAL is senior on Chino"** — INFERENCE only: $19.1M reported lien − Nano ~$6M ≈ $13M = WAL's Q1-26 "$13M non-performing senior lien loan" (KB-143). The 10-Q names **no property or seller**; never promoted to a tie.
3. ⤵ *(9/28: superseded — senior-lien leg OPEN across branches; a forced sale only under B1; Nano file §9)* **Recovery-leg net (if state b):** senior-lien leg **MIXED** (an FDIC forced sale could set an outside price on liens against WAL's own collateral, a *possible* positive); guaranty leg **WORSE** (competing FDIC creditor); **NEW** avoidance risk. **All inside the two booked components; no P&L event expected from the failure itself.**
4. **Stupin guaranty recovery ceiling (illustrative, debtors' OWN scheduled values only, KB-208):** assets $92.2M − secured $38.6M ≈ $53.6M for unsecured, diluted by Zions/Preferred/FDIC claims + admin; **cannot pay near face.** Never quote a cents-on-the-dollar figure as a finding.

---

## UNKNOWNS (what is missing, why, and what would settle it)

### Lien ownership / priority AT FAILURE (9/25) — open per property

| Property | Latest DATED observation | Unknown | What would settle it |
|---|---|---|---|
| **Ontario** (loan 43) | Debtor lists Nano lien ~$5.13M owed (Doc 88, **9/8/2026**); Nano appears as creditor **9/11/2026** (Doc 90) | Ownership at 9/25 (a transfer after 9/11 is not ruled out) | **Tue 9/29 13:30 PT Plaza Continental hearing** (8:26-bk-10986) — an **FDIC-R or Sunwest appearance** = evidence, *not guaranteed*; FDIC **P&A ~10/5–10/9** (category-level); a recorded **assignment / FRBP 3001(e) transfer notice** |
| **Chino** (loan 44) | Debtor reports WAB + Nano liens ~$19.1M (Doc 122, **8/26/2026**), debtor's filing says property **12125** Central — match to the 12233 DOT UNRESOLVED (corrected 9/28), **65.91% TIC** | (a) ownership at 9/25; (b) whether the $19.1M lien **IS** the $5.99M DOT; (c) current WAL-vs-Nano **priority**; (d) 12125/12233 + TIC reconciliation | **Parcel/APN records** reconciling 12125/12233 + TIC to the DOT legal description; a **title report**; a proof of claim attaching note + DOT |
| **Moreno Valley** (loans 32/33) | Nothing on holder since the 2025 complaint; owner Alessandro Group Ch.11 **8/18/2026** (schedules **NOT on RECAP**) | Everything — holder, priority, ownership at failure | **Riverside County recorder search — WILL'S HANDS** (`webselfservice.rivcoacr.org`, "NANO BANC", 1/1/2025–9/25/2026 → Assignment/Substitution/NOD/Reconveyance/Trustee's Deed); or Alessandro schedules if purchased on RECAP |
| **Bellflower** (loan 45) | Nothing either way | Everything | **In-person LA County Registrar-Recorder search** (no online index) — Will's hands |

- **General:** no recorded **assignment to WAL, reconveyance, or trustee's deed** has been found for **any** of the 4 DOTs; **no filing names the seller** of WAL's $64M protective liens. A **9/20 transfer fits every dated observation** — so state (b) is a *default*, not a finding.
- **$173.0M vs $98.6M** claim-vs-balance is **unreconciled** (could include the full Credit, additional guaranteed obligations, interest, fees — never inferred).

### Thesis-side unknowns (the LIVE bear)

- The **$99M appraisal mark** — the single most-dated Q3 catalyst; **8-K-silent = NO-VERDICT** (0-for-1 base rate).
- Whether the CEO's better Q3 credit **guidance** (KB-194) prints as **data** (re-verify quotes at the IR webcast before grading).
- Whether **life-science lab-vacancy** deterioration (KB-209) is confirmed at a **primary** (CBRE/Cushman/REIS) — the pre-appraisal base rate.
- **NDFI / V3** (1/5 under challenge): the Q3 10-Q NDFI table decides plan vs measurement.

---

## THE NEXT OBSERVATION THAT WOULD CHANGE THE CONCLUSION (named, dated, direction)

**On the Nano-lien leg (recovery, NOT thesis-moving either way):**
- **Tue 9/29 13:30 PT Ontario hearing** — an FDIC-R / Sunwest appearance → moves Ontario toward **state (b)** (Nano held → FDIC now holds). *Direction:* confirms a recovery-side, forced-seller dynamic; **still not a P&L event.** *Possible source, not an answer.*
- **Riverside recorder search (Will)** → resolves Moreno Valley holder/priority. *Direction:* if a **trustee's deed pre-9/25** appears → **state (c)** (loss already in Q1 charge-off, benign); if an **assignment to WAL** → **state (a)** (already senior, benign); if **still Nano** → **state (b)**.
- ⛔ *Annotation 2026-09-28 (the two bullets above stay as delivered; this corrects them):* **only an FDIC-R appearance implies a forced seller; a Sunwest appearance means a going-concern holder, not a forced seller.** "Loss already in Q1 charge-off" under state (c) is an **inference no filing states**. A recorder **name** search alone does not resolve a branch (DEWEY §4x); it needs the recorded instrument matched on APN. The pre-registered hearing read-sheet is `research/2026-09-27_nano-banc-receivership-stupin-recovery.md` §10, and the branches are in §9.

**On the thesis (where CRE distress actually transmits to WAL):**
- ★ **Q3 print (~mid-to-late Oct; frames written 9/24, deadline was 10/13) + Q3 10-Q (~late Oct) + the $99M appraisal.**
  - *Bearish direction:* a **low $99M appraisal mark** and/or a **new office migration** (N=2) → V1b-magnitude realizes, **bear-medium (16%) confirms**, EV falls.
  - *Bullish direction:* **benign appraisal** + the 9/16 better-credit guide printing as data → **bear-medium KILL** leg fires, bear narrows toward RETIRE.
- **KB-209 confirmed at a primary lab-vacancy series** → raises the appraisal-downside base rate. *Direction:* supports bear-medium ahead of the print.

---

## BOTTOM LINE (for PROME synthesis)

**Isolated vs broader, for WAL:** the CRE→loss transmission that already *happened* to WAL was **idiosyncratic and fraud-driven** (the Cantor/Stupin ring; Q1 $152.5M charge-off) — and the **Nano Banc failure sits entirely inside that closed leg**, adding **no new exposure** and carrying **~none of the forward thesis** (V2 excluded from the composite). The transmission that is still **live and un-resolved** is **ordinary CRE**: the **$99M life-science office** credit and the office book (V1b-magnitude, ~16% bear-medium), now with a **fresh sector headwind** (KB-209: life-science vacancies rising; 10Y at 5.11% pressuring marks). So for WAL the answer leans **"isolated so far, with one live broader-CRE channel priced but unresolved"** — and it resolves on the **Q3 print + the $99M appraisal**, not on Nano. Nothing here moves a score; the appraisal and the print do.

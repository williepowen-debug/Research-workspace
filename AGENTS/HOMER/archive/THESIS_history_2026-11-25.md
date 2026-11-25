# HOMER THESIS — dated history moved out of `thesis/THESIS.md` on 2026-11-25 09:33 ET

Moved VERBATIM (Will 2026-11-25 09:31 ET, "ok go" on the list that named the archive). Source file before the move: `thesis/THESIS.md` at commit `5eb6027a4a`, 43,105 B, sha256 `6d689ca12bbb87e601fc036648e0589291797066219ca5e87b2c043eb79c6157`. Historical record: the kill rail, the defect register, the clarifications and the 2026-11-20 grade stay in `thesis/THESIS.md`. ⛔ Do not cite a row here as current. The §9 entry for 2026-10-28 ("the inflow end is cooling") is WITHDRAWN: see `thesis/THESIS.md` §11 D17.

| Block | What it is |
|---|---|
| A | §1 paragraph in force 2026-09-29 to 2026-11-25 |
| B | §5 first grade, 2026-09-29 |
| C | §8a score table as proposed 2026-09-29 |
| D | §9 fired-count entries, 2026-10-15 to 2026-11-16 |
| E | §10 re-score change table, 2026-11-20 |

---

<!-- BLOCK A -->
**U.S. housing credit stress has moved from ACCUMULATION to CONVERSION.** Residential foreclosures and multifamily loans are turning into completed foreclosures, REO and realized losses. Elevated mortgage rates and builder distress are keeping the stress from curing on its own. **That makes housing an active transmission vector:** to banks (Path C → REGINALD, the lead path of CARL's thesis of record), to households (→ CARL) and to wealth (→ HENRY). **Current state: 🔴.**

<!-- BLOCK B -->
## 5. GRADE OF RECORD — 2026-09-29 (first ever)

⚠️ **Ordering caveat, recorded rather than hidden:** these criteria were written today with the data in hand. Guardrails used: no kill level is already breached, and every level was base-rated against a window before 2026 where one exists. From the next grade, the criteria are frozen and pre-date the data.

| Leg | Standing rule (kill) | Current state @ level (as of) | Fired count | Verdict |
|---|---|---|---|---|
| **C1** | FC sales YoY ≤ 0% AND FC inventory YoY ≤ 0%, 3 prints | Sales **+11.7%**, inventory **+41%** (Aug, ICE 9/28) | **0 / 3** | 🔴 **NOT FIRED** |
| **C2 · CMBS** | Trepp MF DQ < 6.00%, 3 prints | **7.69%** (Aug, Trepp 9/1) | **0 / 3** | NOT FIRED |
| **C2 · GSE** | max(Freddie, Fannie) < 0.50%, 3 prints | Freddie **0.64%**, Fannie **0.57%** (Aug) | **0 / 3** | NOT FIRED |
| **A1** | FHA SA QoQ ↓ ×2 AND cure YoY > −15% | FHA **11.79%, −9bps QoQ** (Q2) = **1 of 2**; cure **−28% YoY** (Jul) | **½ of the first conjunct** | NOT FIRED |
| **A2** | PMMS ≤ 6.50%, 4 weeks | **7.03%** (9/24) | **0 / 4** | NOT FIRED |
| **A3** | HMI ≥ 40, 3 prints | **32** (Sep) | **0 / 3** | NOT FIRED |

**LITERAL FIRED-COUNT: 0 of 5 legs.** ⇒ **🔴 holds.**

**The honest read:** no leg is close to its kill. The softest spots are **C1's inventory build** (+2K in August, the smallest in 9 months) and **A1's first conjunct** (one QoQ FHA decline already in). The GSE channel moved in both directions in August (Freddie up, Fannie down), so it is not a one-way read.

---


<!-- BLOCK C -->
⚠️ **Scores are the ones PROPOSED 2026-09-29** (packet to CARL, commit `64d35bf5f`), which CARL told me to build as proposed (10/01). **Not re-scored on 10/15:** the recovery session integrated no print newer than 10/02. Local state is the newest value I hold, dated. The kill rail (§3) governs; a score is a triage projection that routes attention back to it. Re-score at each formal grade (next 2026-11-20).

| # | Vector (HOMER leg) | Score (1–5) | Local state (as of) | Independence | Key signal | Upgrade trigger (→ 5) |
|---|---|---|---|---|---|---|
| C1 | Residential conversion (CORE) | **4** | ICE 90+/FC **872K** (Aug; 22K past Orange, RED >1M); FC pre-sale inventory **298K, +41% YoY** but +2K MoM; FC starts **+29% YoY**; ATTOM Aug REO **+42% YoY** | **Root R1** (residential FC pipeline) | ICE First Look, monthly | §3 C1 "for" flip: FC sales YoY **≥ +20%** (Aug +11.7%) |
| C2 | Multifamily realization (CORE) | **4** | Freddie MF **0.64%** (Aug, 14bps above Red); Fannie MF serious **0.57%** (Aug, mod-suppressible); Trepp CMBS MF **7.69%** (Aug); realized marks (BANC HFS, Arbor REO) | **Root R2** (MF credit) | Trepp MF DQ + GSE monthlies | §3 C2 "for" flip: Trepp CMBS MF **> 7.71%** (a new 2026 high) |
| A1 | FHA-bottom inflow (AMP) | **4** | FHA SA DQ **11.79%** (Q2, 21bps below Red); ICE cure rate **−28% YoY**, FHA **−39%** (Jul) | **Co-rooted with C1 (R1): count once** | MBA NDS (quarterly) + ICE Mortgage Monitor | §3 A1 "for" flip: FHA SA **≥ 12.00%** at the Q3 NDS |
| A2 | Rate amplifier (AMP) | **4** | PMMS **7.28%** [wk 10/01], RED, HOLD state fired; spread ~199bps | **Co-rooted with CARL's V12** (rates; BROCK/HENRY own direction): count once | Freddie PMMS, weekly | None defined: PMMS has no uncrossed rung above RED. Set one at the 11/20 grade or leave the score capped at 4 |
| A3 | Builder distress (AMP) | **3** | NAHB HMI **32** (Sep); price cutters **38%** (Orange); LEN/KBH margins at trough, orders −9% / −12% | **Root R3** (new-home supply → LABOR) | NAHB HMI, monthly; builder 8-Ks | §3 A3 "for" flip: price cutters **> 45%** (RED) |

**Composite (transparent, no weighting): 4 + 4 + 4 + 4 + 3 = 19/25 across 5 legs.** Independent roots: **3** (R1, R2, R3). A1 folds into R1; A2 is an input to CARL's V12, not a new root.

<!-- BLOCK D -->
## 9. Fired-count ledger between grades (mechanical, per §4 "fired counts update at each print"; no criterion touched)

### 2026-10-15 — L722 catch-up (first prints integrated since 10/02)

| Leg | Print(s) integrated (first-published vintage, V1) | Fired count | Verdict | Cleanest-flip check (§3) |
|---|---|---|---|---|
| **C1** | none — ICE September First Look not out (URL 404 10/15 11:16 ET; ~10/22–28) | **0 / 3** | NOT FIRED | pending |
| **C2 · CMBS** | Trepp **8.04% Sep** (+35bp; pub 10/02, PDF Table 2) | **0 / 3** | NOT FIRED | ★ **"for" flip MET: > 7.71%, a new 2026 high** |
| **C2 · GSE** | none — Sept Fannie/Freddie due ~10/23–30 | **0 / 3** | NOT FIRED | pending |
| **A1** | ICE Mortgage Monitor Oct (Aug data): all-loans cure **YoY % NOT PRINTED** (level 7.8%; FHA −37% YoY). MBA Q3 NDS ~mid-Nov | **½ of the first conjunct** (unchanged) | NOT FIRED | second conjunct (cure YoY better than −15%) not met on any reading — the chart-derived −25 to −29% is INFERRED and not used to grade |
| **A2** | PMMS **7.40% [10/08]** · **7.40% [10/15]** (unchanged) | **0 / 4** | NOT FIRED | 90bps above the kill line (≤ 6.50%) |
| **A3** | none — NAHB October HMI scheduled Mon 10/19 (archived NAHB schedule) | **0 / 3** | NOT FIRED | pending (Sep HMI 32, cutters 38%) |

**LITERAL FIRED-COUNT: 0 of 5 legs ⇒ 🔴 holds.** §7 V5 unchanged: 11/20 cannot return FALSIFIED or PARTIAL on the core legs.

**§8a handle:** C2's upgrade trigger (→ 5) is **MET** by the Trepp 8.04% print. **Not re-scored today** — §8a re-scores at the formal grade (2026-11-20); the trigger is recorded here so 11/20 reads it. Composite stays **19/25** until then.

**Instrument note (C2 neighbourhood, not a C2 criterion):** the Trepp **MF maturity-adjusted** rate is RETIRED (dated kill EXECUTED 2026-10-15, absent at source Jul–Sep); C2 never graded on it. Its successor for the pre-delinquency channel is MF special servicing (8.54% Sep, +17bp).

**HOMER defect (V2):** the September Trepp print and PMMS 10/08 were integrated ~2 weeks / 1 week late (the 10/14–15 crash). Under V2 a print HOMER failed to fetch PAUSES a run; no run was in progress, so no count is affected.

### 2026-10-19 — L725 October HMI (mechanical update only)

| Leg | First print integrated | Fired count | Verdict | Frozen cleanest-flip check |
|---|---|---|---|---|
| **A3** | October NAHB HMI **29** (Sep 32); cutters **43%** (38%); incentives **65%** (66%). PRIMARY NAHB HMI page directly fetched after 12:09 ET; issuer schedule 10/19 10:00 ET. Evidence: `reports/2026-10-19_morning_evidence/nahb_live.txt` | **0 / 3** | **NOT FIRED**: 29 <40 | For cutters >45%: NOT MET. Against HMI >=36 AND cutters falling: NOT MET. Explicit cutters rose 5pp; incentive participation eased 1pp. Average explicit cut 6% is a lower bound on total concessions |

No other newly resolving print was integrated: **0/5 legs killed**, no criterion or confidence moved. C1 0/3; C2 CMBS 0/3 and GSE 0/3; A1 remains one of two FHA-quarter declines with all-loans cure YoY ungraded for August; A2 0/4 (10/15 PMMS reread is not another weekly print). ATTOM August and Trepp September SS relays duplicate existing evidence; Galleon is an unverified single-building case. None grades a core kill. **Formal review 2026-11-20, §7 V5 and §8a 19/25 handle unchanged.** Report: `reports/2026-10-19_morning-L725.md`.

### 2026-10-28 — catch-up (prints released 10/20–10/28; mechanical update only)

| Leg | First print integrated | Fired count | Verdict | Frozen cleanest-flip check (§3) |
|---|---|---|---|---|
| **C1** | ICE First Look **September** (Business Wire 10/27): FC sales **8.2K, +14.5% YoY**; FC inventory **303K, +37% YoY, +5K MoM**; FC starts 40.0K, **−2.9% YoY** (Aug +29%) | **0 / 3** | NOT FIRED (both YoY legs > 0) | *For* (sales YoY ≥ +20%): **NOT MET** (+14.5%). *Against* (inventory down MoM with sales down MoM): **NOT MET** (inventory +5K, sales +5.4% MoM). ⚠️ New, not a criterion: starts YoY turned negative — the inflow end is cooling while conversion continues |
| **C2 · CMBS** | none — Trepp October DQ ~11/02 | **0 / 3** | NOT FIRED | pending |
| **C2 · GSE** | Freddie MF **0.58% Sept** (MVS pub 10/26; Aug 0.64% unrevised). Fannie September NOT YET PUBLISHED (checked 10/28 ~22:48 ET) | **0 / 3** | NOT FIRED — max(Freddie, Fannie) ≥ 0.58% whatever Fannie prints | Freddie's first MoM decline since April; 8bp above 0.50%. One month, mod-suppressible headline |
| **A1** | none — ICE Mortgage Monitor (Nov) and MBA Q3 NDS pending. ICE First Look: FHA serious DQ −10% since Feb (ICE narrative; not a band basis) | **½ of the first conjunct** (unchanged) | NOT FIRED | pending (Q3 NDS) |
| **A2** | PMMS **7.32% [10/22]** (ISSUER CSV) | **0 / 4** | NOT FIRED | 82bp above the kill line (≤ 6.50%) |
| **A3** | no HMI (next 11/17). Builder 8-Ks (context, not the criterion): PHM GM 24.8%, NVR 18.3% cancels 21%, MTH 17.4%, CCS guidance cut | **0 / 3** | NOT FIRED | pending |

**C2 · GSE addendum (same session, news sweep):** Fannie Q3 earnings release (10/28) gives MF serious DQ **0.62% at 9/30** (Q2-end 0.60%) with the MF provision **$446M vs $259M (+72%)**. max(Freddie 0.58, Fannie 0.62) = 0.62 ≥ 0.50 ⇒ **0 / 3, NOT FIRED**. The §2 provision pairing points the same way as the headline this quarter (KB-HOMER-042).

**LITERAL FIRED-COUNT: 0 of 5 legs ⇒ 🔴 holds.** No criterion, level or confidence moved. Evidence: `reports/2026-10-28_catchup-prints.md`; ledgers PIPELINE / MULTIFAMILY / RATES / BUILDER rows dated 2026-10-28.

### 2026-11-05 — catch-up (prints released 10/29–11/05; mechanical update only)

| Leg | First print integrated | Fired count | Verdict | Frozen cleanest-flip check (§3) |
|---|---|---|---|---|
| **C1** | none — ICE First Look October due ~11/23–30 | **0 / 3** | NOT FIRED | pending |
| **C2 · CMBS** | Trepp MF **8.09% October** (+5bp; issuer PDF Table 2) | **0 / 3** | NOT FIRED | *For* (> 7.71%): MET again, by the letter. ⚠️ the $210M Cove at Tiburon loan likely exceeds the whole rise and may revert (`registry/PREREG_2026-10_TREPP_MF_PRINT.md` §5) |
| **C2 · GSE** | none monthly — Fannie September Monthly Summary still unread (403). Freddie 10-Q pairing: MF provision $115M Q3-26 vs $57M Q3-25; subordination bucket 0.80% vs 0.58% blend | **0 / 3** | NOT FIRED — max(0.58, 0.62) = 0.62 ≥ 0.50 | The pairing points the same way as Fannie's: deterioration under the headline |
| **A1** | none — MBA Q3 NDS ~mid-Nov; ICE Mortgage Monitor November not found 11/05 | **½ of the first conjunct** (unchanged) | NOT FIRED | pending |
| **A2** | PMMS **7.24% [10/29]**, **7.18% [11/05]** (issuer CSV) | **0 / 4** | NOT FIRED | 68bp above the kill line (≤ 6.50%) |
| **A3** | no HMI (next 11/17). Builder 8-Ks and DHI call are context, not the criterion: DHI Q1 GM guide 18–18.5%, LGIH 20.2%, DFH 14.9% | **0 / 3** | NOT FIRED | pending |

**LITERAL FIRED-COUNT: 0 of 5 legs ⇒ 🔴 holds.** No criterion, level or confidence moved. Evidence: `reports/2026-11-05_catchup.md`; ledger rows dated 2026-11-05.

### 2026-11-11 — PROME catch-up wake (prints released 11/06–11/10; mechanical update only)

| Leg | First print integrated | Fired count | Verdict | Frozen cleanest-flip check (§3) |
|---|---|---|---|---|
| **C1** | none — ICE First Look October due ~11/23–30. Context, not the criterion: ICE Monitor Sept FC starts 40,400 (−3% YoY), FC sales 8,200 (+14% YoY); NY Fed Q3 mortgage 90+ 1.13% (0.83% a year ago), foreclosure notations 61,900 (+13% YoY) | **0 / 3** | NOT FIRED | pending |
| **C2 · CMBS** | none on the DQ criterion (Trepp November ~12/01–05). **C2 neighbourhood note:** MF special servicing **9.22% October, +69bp = NEW 2026 HIGH** (> 9.08 strict, PREREG §4); DQ–SS gap 113bp; $517.7M Blackjack transferred at maturity | **0 / 3** | NOT FIRED | No criterion attaches to SS (§4) |
| **C2 · GSE** | none — Fannie and Freddie October monthlies not out (404 at 11/11) | **0 / 3** | NOT FIRED | unchanged |
| **A1** | ICE Mortgage Monitor November: **all-loans cure YoY NOT PRINTED (second edition)**; FHA cures −46% YoY (FHA-only, does not grade). MBA Q3 NDS not out | **½ of the first conjunct** (unchanged) | NOT FIRED | pending |
| **A2** | no PMMS since 11/05. Context: MND 7.30% [11/10], +12bp after CPI; 10Y 4.98% | **0 / 4** | NOT FIRED | 68bp above the kill line on the last PMMS; moving further off |
| **A3** | none (HMI 11/17) | **0 / 3** | NOT FIRED | pending |

**LITERAL FIRED-COUNT: 0 of 5 legs ⇒ 🔴 holds.** No criterion, level or confidence moved. Evidence: `reports/2026-11-11_catchup.md`; ledger rows dated 2026-11-11.

### 2026-11-12 — between-grade integration (HOMER wake, PROME WQ-675 session)

| Leg | First print integrated | Fired count | Verdict | Frozen cleanest-flip check (§3) |
|---|---|---|---|---|
| **A2** | PMMS **7.11% [11/12]** (issuer CSV), −7bp, fourth straight weekly fall, lowest in seven weeks (Freddie) | **0 / 4** | NOT FIRED | **61bp above the kill line (≤ 6.50%)**. ⚠️ Correction to the 11/11 entry: "moving further off" was an inference from MND and Treasury moves; the survey moved 7bp CLOSER. |
| **C2 · CMBS / GSE** | no criterion print. Context only (WQ-675): Arbor Q3 non-performing 32 loans $647.6M (19 / $428.8M at 6/30), dividend suspended (8-K 10/30, issuer); Blackjack held by a Blackstone single-borrower CMBS trust (INFERRED); United Fidelity Bank $2.14B MF nonaccrual, bank-held (PROME report, relayed; maturity, trigger and containment UNRESOLVED — narrowed 12:4x ET) | **0 / 3 · 0 / 3** | NOT FIRED | No criterion attaches |
| **C1 · A1 · A3** | none (MBA Q3 NDS not out at 12:00 ET; HMI 11/17) | unchanged | NOT FIRED | pending |

**LITERAL FIRED-COUNT: 0 of 5 legs ⇒ 🔴 holds.** Existing-home sales 3.75M October (NAR, issuer) is band and prediction evidence (HB-12, HOM-03 HIT), not a thesis-leg criterion. No criterion, level or confidence moved. Evidence: `reports/2026-11-12_wake.md`.

### 2026-11-16 — pre-grade input check for the 11/20 formal grade (PROME relay of Will's word 20:56 ET; no criterion touched)

No leg can reach its kill count before 11/20 (§7 V5), so there is **no early grade**. What each leg will be graded on:

| Leg | Input the letter needs | In hand 11/16 | Lands before Fri 11/20? | Can it fire at 11/20? |
|---|---|---|---|---|
| **C1** | ICE First Look FC sales YoY and FC inventory YoY, 3 prints | ICE September: FC sales 8,200, +14% YoY; FC inventory 303K, +37% YoY (STATUS dashboard; Monitor revised starts) | ❌ October First Look ~11/23–30 (D11) — grade on Sept, say so | No (0 / 3; V5) |
| **C2 · CMBS** | Trepp MF DQ < 6.00%, 3 prints | **8.09% October** (Trepp issuer PDF) | Nothing new (November data ~12/01–05) | No (0 / 3) |
| **C2 · GSE** | max(Freddie, Fannie) < 0.50%, 3 prints; Fannie provision pairing | Freddie 0.58%, Fannie 0.62% (Sept); Fannie provision $446M vs $259M Q2 (rose) | ❌ October monthlies ~11/23–30 | No (0 / 3) |
| **A1** | MBA NDS FHA SA QoQ ↓ ×2 AND ICE all-loans cure YoY better than −15% | Q2 FHA 11.79% (1 of 2 declines); cure YoY NOT PRINTED Oct + Nov editions | MBA Q3 NDS: expected ~11/13–14, **not found 11/16 evening** (one search + MBA Newslink tag page, which is stale; not proof of non-publication). Cure YoY: no edition before 11/20 | **No — the second conjunct is UNGRADED (D12).** A Q3 decline would make the first conjunct 2 of 2 and still not fire |
| **A2** | PMMS ≤ 6.50% four straight weeks | 7.11% [11/12], 61bp above | ✅ PMMS Thu 11/19 | No (0 / 4; needs four weeks) |
| **A3** | NAHB HMI ≥ 40, 3 prints | 29 (Oct) | ✅ November HMI Tue 11/17 10:00 ET | No (0 / 3) |

**Expected outcome by the letter: 0 of 5 legs FIRED, 🔴 holds; A1 reported with its UNGRADED conjunct.** Owed at the grade: re-score the §8a handle (it was last scored 9/29), and HOM-02 if the Q3 NDS has printed. CARL (live, named consumer on DOCKET line 545) receives the result through NEXUS_BRIEF at closeout; a same-day packet is owed only on FALSIFIED or PARTIAL, which V5 rules out.

---


<!-- BLOCK E -->
### §8a handle — RE-SCORED at this grade (last scored 2026-09-29; CARL scores its vectors, HOMER feeds)

| Leg | Was | Now | Why |
|---|---|---|---|
| C1 | 4 | **4** | Stock and conversion still rising (FC inventory +37%, FC sales +14.5% YoY, FHA FC rate 9-year high), but new FC starts −3% YoY (Sept) and the "for" flip (FC sales ≥ +20%) not met |
| C2 | 4 | **5** | Upgrade trigger MET (Trepp > 7.71%: 8.04% Sept, 8.09% Oct) with MF special servicing 9.22% (new 2026 high) and Fannie provision +72%. ⚠️ Cove at Tiburon may revert in the November print |
| A1 | 4 | **3** | The leg claims *inflow*: FHA headline DQ fell twice and ICE FHA new defaults −14% YoY (Sept). Non-curing persists (FHA cures −46% YoY) and distress is converting, which C1 carries. Co-rooted with C1 (R1), counted once |
| A2 | 4 | **4** | PMMS 7.28%, RED; capped at 4 — no upgrade trigger defined, and I add none (fewer rules) |
| A3 | 3 | **5** | Upgrade trigger MET: price cutters 46% (> 45%); HMI 25, traffic 16, incentives 68% |

**Composite (no weighting): 4 + 5 + 3 + 4 + 5 = 21 / 25** (was 19). Independent roots still **3** (R1, R2, R3). A score is triage; the §3 rail governs.


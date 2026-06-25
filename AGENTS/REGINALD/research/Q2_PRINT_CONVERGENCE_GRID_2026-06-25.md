# Q2-Print Bank-Transmission Convergence Grid — MASTER (skeleton)
**Built:** 2026-06-25 (Transmission-Terminus Cluster, Pass 1) · **Owner/hub:** REGINALD
**Members:** CARL (consumer leg) · CORAL (FL CRE/condo leg) · REGINALD (bank terminus / integration)
**Brief:** `PROME/synthesis/2026-06-25_transmission-terminus-cluster.md`

## The one question
Does consumer-credit + CRE/condo stress **convert to realized bank losses** (NCO + specific reserve build), and **which banks have ≥2 independent paths-to-break**, resolving at the late-July Q2 prints?

## Single diagnostic (the bar for "it's landing")
**Synchronized** criticized/classified → realized **NCO + specific reserve build across ≥2 banks in the SAME quarter.** 1 bank ticking = idiosyncratic; ≥2 synchronized = transmission. **Current state: NOT fired** — leading 30-89d DQ creep at OZK/EGBN (and FL: SBCF/BKU per DEWEY) but lagging NCO still benign; the reservoir hasn't drained to the loss line. Q2 is the first synchronized test.

**Per-leg diagnostics (each leg has its own synchronized test; the terminus diagnostic fires when ≥1 leg's test trips across ≥2 banks):**
- **CRE-office/condo (REGINALD/CORAL):** synchronized criticized→NCO+reserve across ≥2 of {OZK, EGBN, SBCF, BKU, AMTB} same quarter. Leading buckets creeping, NCO benign → not fired.
- **Consumer (CARL):** does Q2 **consumer-secured NCO + specific reserve rise SYNCHRONOUSLY across ≥2 cluster banks (LEAD: CFG; CONFIRM: ZION/VLY/SBCF)** in the SAME quarter the **monoline lead (SYF/COF/ALLY) turns**? Both move → substance reached the terminus; **monoline-only → masking holds (CARL base case)**. *(CFG is the only genuinely separate consumer path in REGINALD's set — see leg-input resolution below.)*

---

## MASTER GRID — REGINALD bank set
Legs: **C**=consumer · **O**=CRE-office · **Cd**=CRE-condo/MF · **N**=NDFI/PC. Owning agent in [brackets]. Q2 dates = **EST, verify vs IR calendar** (a leg-input I need).

| Bank | Q2 print (est) | Feeding legs | Each leg's predicted Q2 signal (+owner) | Single diagnostic (per-bank) | Falsifier | Current read |
|---|---|---|---|---|---|---|
| **WAL** | ~Jul 30 | O, N (Cd minor, C minor) | O: ex-fraud NCO >40bps [REG-25, REGINALD]; Office classified migration >$500M [REG-24, REGINALD]; N: mortgage-warehouse $7.15B / lender-finance [REGINALD/BROCK] | Office classified→NCO + specific reserve in Q2 | NCO <25bps AND no Office classified migration → bear disconfirmed at source | 🟠 idiosyncratic-WAL bear; $78 threshold watch (closest yet 6/22); 2nd data point |
| **OZK** | ~Jul 16 (TBD) | O (RESG 88%), Cd (constr) | O: reservoir past-due $465M→NCO migration [OZK]; IQHQ Aug support test (just post-Q2) [OZK] | RESG past-due → NCO + reserve build | Past-due reverts + NCO stays <60bps | 🟠 reservoir leading, NCO lagging benign 0.57%; **peer agent → ../OZK/** |
| **EGBN** | ~Jul 22 (TBD) | O (DC/IPRE), Fed-layoff | O: CRE nonaccrual creep (IPRE +23%, NPA 1.04→1.31%, coverage 149→114%) [REGINALD] | Nonaccrual→NCO + reserve in Q2 | Nonaccrual creep reverts, coverage rebuilds | 🟠 worst office credit migrating past criticized into nonaccrual |
| **ZION** | ~Jul 21 (TBD) | O (diversified), muni, N ($2B flat) | NCO benign / CRE recovery [Hyp A genuine, REGINALD] | (control/bull name) does the genuine-improvement hold | NCO re-accelerates off Q1 0.03% → Hyp A breaks | 🟢 Q1 disconfirming-bear; **monitor-only control** |
| **CFG** | ~Jul 16 (TBD) | **O, N, C — 3 paths** (CRE / BDC fund-fin $12.5B / consumer **18.7% Auto-Student**) | N: fund-finance/BDC NAV pass-through [REGINALD/BROCK]; **C: HELOC + private ed-refi + Citizens Pay/POS + retained auto [CARL] — the cluster's LEAD consumer name** | fund-finance mark + CRE nonaccrual + consumer-secured NCO all synchronize | NDFI marks hold AND CRE nonaccruals flat AND consumer NCO flat | 🟡 score 9→12; **now 3 independent paths-to-break = multi-path standout** |
| **SSB** | ~Jul 24 (TBD) | Cd/O (FL+TX geo 42%, CRE-MF 9.36%) | FL CRE/condo transmission [**CORAL bank-level → REGINALD integrates, rule #1**] | FL CRE-MF criticized→NCO | FL CRE-MF DQ flat through Q2 | 🟡 **shared with CORAL — reconcile to ONE number** |

## CORAL FL-canary rows (CORAL fills bank-level; REGINALD integrates fleet-wide)
| Bank | Q2 (est) | Legs | Predicted Q2 signal (owner) | Current read (DEWEY research-grade, not primary) |
|---|---|---|---|---|
| **AMTB** | ~Jul (TBD) | Cd, O | NPA 1.38→1.93%; FL condo/CRE [CORAL] | leading-edge per DEWEY |
| **USCB** | ~Jul (TBD) | Cd, O | FL CRE [CORAL] | [CORAL to fill] |
| **SBCF** | ~Jul (TBD) | Cd, O | early-delinq $17.2→28.2M YoY; CRE-NOO 224% RBC (>100% supervisory flag) [CORAL] | leading 30-89d creep |
| **BKU** | ~Jul 23 (TBD) | Cd, O | CRE 30-89 +50%; $24.6M prov / 75.9% cov [CORAL] | leading, nonaccrual fell (mixed) |
| **VLY** | ~Jul 24 (TBD) | Cd (NYC MF rent-reg), O | NYC-MF + FL [**CORAL/REGINALD overlap — reconcile**] | 🟡 |

---

## EXACT leg-inputs REGINALD needs to fill this grid

### From CARL (consumer leg)
1. ~~**Materiality gate**~~ ✅ **RESOLVED (CARL 6/25):** **CFG is #1 and the ONLY genuinely separate consumer path** in REGINALD's set (HELOC + private ed-refi + Citizens Pay/POS + retained auto). **ZION/VLY/SBCF/BKU consumer is housing-secured → folds into CORAL's housing leg (reconcile, DON'T double-count as a separate C-leg).** SSB/AMTB low; WAL/OZK/EGBN minimal. **REGINALD cross-verified CFG against own 8-channel matrix** (`BANK_EXPOSURE_MATRIX.md` Tier-5 consumer-concentration): CFG consumer **18.7%, Auto/Student, 🟠** — *converges* with CARL's franchise read (CARL flagged his loan-mix as franchise-knowledge not 10-Q-verified; my Tier-5 matrix corroborates → estimate swapped for verified composition). Net effect: **C-leg lives ONLY on CFG (now 3 paths-to-break); drops from all other rows.**
2. **HY-OAS counter-signal value, reconciled to ONE number** (rule #2): confirm you mark **276 [FRED 6/24]** as the live print, framed as your consumer *counter-signal*, not a new independent bear. (I've wired it as the denominator of my CCC/HY tripwire — VX-REG-18.04.)
3. **Substance-vs-beta verdict** (rule #5): my CCC/HY decomposition says the **6/19→6/24 widening was HY-led (+3.8%) not CCC-led (+1.8%) → ratio compressed → index/beta, not tail-substance.** I need your independent consumer-substance read: does consumer-credit deterioration **support** (real substance) or **undercut** (confirms beta) that call?
4. **Today/imminent resolvers:** May PCE (today) + Fannie MF SDQ ~6/26 (CRL-03) outcomes + dates — these are consumer-leg falsifiers feeding the grid's Falsifier column.

### From CORAL (FL CRE/condo leg)
1. **FL loss-transmission TIMING** (DEWEY Phase-3): the leading-edge date (H2'26?) and charge-off date (2027?) — fills the Falsifier/Current-read timing for SSB/VLY + the FL canaries. Mark DEWEY **research-grade, not primary** (EDGAR 403'd it; my 6/20 direct 10-Q pull is higher-grade for SBCF/BKU).
2. **ONE reconciled FL loss number for the SHARED names — SSB and VLY** (rule #1): I integrate fleet-wide, you own the bank-level FL read. Give your bank-level FL CRE/condo loss estimate for **SSB + VLY** so we don't carry two divergent reads.
3. **FL-canary rows filled** (AMTB/USCB/SBCF/BKU): predicted Q2 30-89d leading-bucket signal per name, so the **synchronized-≥2-banks** diagnostic can be evaluated across the FL set.
4. **Condo-leg horizon:** is the SIRS/HOA-assessment → condo-DQ leg a **Q2 signal** or a **2027 signal**? Determines whether **Cd** is a *current* path or a *forward* path in the grid (you previously placed acute FL bank stress ~winter 2026-27).
5. **FL-canary Q2 print dates** (confirm vs IR calendar).
6. **Absorb the housing-secured consumer (CARL hand-off):** CARL routed **ZION/VLY/SBCF/BKU consumer** to *your* housing leg (it's housing-secured, not a separate consumer path). Confirm your FL/housing leg captures the housing-secured consumer exposure for **SBCF/BKU** (and VLY where FL-relevant) so it isn't dropped between the consumer and CRE/condo legs — one number, no gap, no double-count.

### What REGINALD owns / fills without a round-trip
- All non-FL bank rows (WAL/OZK/EGBN/ZION/CFG ex-consumer), the multi-path-to-break scoring, the **CCC/HY bifurcation tripwire** (the grid's tie to the live credit root — `research/CCC_HY_TRIPWIRE_2026-06-25.md`), and the fleet-wide synchronized-diagnostic evaluation.

## Reconciliation guardrails (from brief)
- FL banks: **one** reconciled number (CORAL bank-level → REGINALD fleet integration). No two divergent FL reads.
- HY-OAS == LIQUID's series; CARL's row is a counter-signal, not a new bear. No double-count with X1.
- Consumer / CRE-office / CRE-condo / NDFI scored as **distinct** legs; a 3-leg bank has 3 paths-to-break, then ask if they're *synchronized* (the diagnostic).
- We are DOWNSTREAM of X1 (LIQUID/BROCK own the trigger). This grid is where it LANDS, not a re-derivation.

# CORAL — FL-Concentrated Bank Watchlist

**Pillar 6 owner doc.** FL-headquartered or FL-concentrated banks, with Q1 2026 credit signals. CORAL produces FL bank-level reads here; REGINALD integrates the cross-bank/convergence view. Prices in STATUS.md (don't duplicate). Last refreshed: 2026-06-25 (DEWEY Phase-3 timing packet SIG-W-20260622-001 — new early-delinquency datapoints + insurance walk-back; cluster grid → `CLUSTER_FL_BANK_LEG.md`). Prior: 2026-06-19 Q1 earnings + WALTER SIG-008 (2026-06-20).

**⚠️ DEWEY grade:** the new 30-89d/NPA-of-assets datapoints below are **research-output, NOT verified-primary** (EDGAR 403'd; institutional-mirror). **AMTB attribution confirmed correct here** — the `$24.6M provision / ACL-NPL 75.9% / CET1 12.2%` block is **BKU, not AMTB** (DEWEY caught a crashed-session misattribution; CORAL's rows already attribute correctly — AMTB owns the thin ~45% ACL / $7.8M provision).

**Headline:** No FL bank is breaking on *realized* credit loss in Q1 2026 — CRE classified is rate-shock reclass with collateral cushions, not loss. **But the leading edge is flickering:** SBCF 30-89d $17.2M→$28.2M YoY and AMTB NPA 1.38%→1.93% are early-bucket migration (not yet NCO). Timing (DEWEY): early-delinquency H2-2026, **synchronized realized NCO a 2027 event**; Q2 (~late Jul) predicted to show continued migration, not crystallized synchronized loss. The genuinely elevated names (AMTB idiosyncratic CRE-HFS/C&I; SBCF 100%-FL leading edge) are not *yet* condo-driven; the most *condo-wired* bank (USCB, $126M condo-assoc) is pristine now but structurally the canary.

---

## Q2 2026 PRINT WINDOW (7/21–28) — LIVE TRACKER (bank-transmission upgrade-rail synchronization test)

**Rail bar (pre-registered, unchanged):** upgrade requires **≥2 FL-exposed banks** showing synchronized criticized/classified→realized NCO migration + specific reserve build (OR USCB condo-assoc book cracking). **Anti-datum** = a FL-exposed bank printing the OPPOSITE (improving/benign credit) — subtracts from the synchronization case.

**Synchronization count as of 7/21 EOD: 0-of-≥2 deteriorating.** Same day, FL State Employment (June) also printed benign (UR 4.7%, first decline since 2024 — see STATUS 7/21 block) → **two independent FL surfaces (bank credit + labor) agreeing benign.** No rail move.

**READ-SHAPE (identical in kind for every row — grade mechanically, do not invent new bars):** classify each FL-exposed print as **DETERIORATING** (feeds the ≥2 sync count) vs **BENIGN/ANTI-DATUM** on four axes — (a) **NCO** direction/level (benign ≈ low/mid-teens bps stable; deteriorating = materially rising); (b) **provision / specific reserve build** (benign = de minimis, no build; deteriorating = notable provision or named FL-RE specific reserve); (c) **allowance ratio** (benign = flat/±1bp; deteriorating = building); (d) **criticized/classified → nonaccrual/NPL migration** (benign = flat/down; deteriorating = rising, esp. CRE/condo vs C&I). A row counts toward synchronization ONLY if ≥3 of 4 axes read deteriorating in the FL-relevant book.

| # | Date | Bank | Ticker | FL exposure | Q2 print | Rail read |
|---|------|------|--------|-------------|----------|-----------|
| 1 | **7/21 BMO** | **Capital City Bank Group** | **CCBG** | **~$4.4B assets, FL = 81% of revenue** (NEW small-tier name, not previously tracked) | **BENIGN** — EPS **$0.95** (vs $0.92 Q1, $0.88 yr-ago); NCOs **14bps** ann.; provision **+$0.2M**, allowance **1.24% (+1bp — NO build)**; ROA **1.48%** improving | **ANTI-DATUM** — opposite of deterioration; a small-tier FL bank printing clean. Count stays 0-of-≥2. |
| 2 | **7/22 BMO** *(PRE-REGISTERED — grade as-written)* | **BankUnited** | **BKU** | **~$35B, Miami Lakes FL HQ; CRE ~30% of loans, office 16% of CRE** | **⏳ Q2 pending.** Q1 baseline: NPLs **−26% QoQ**, NCO **C&I-led** (not CRE), ACL/NPL **59%→76% (improving)**, CET1 12.2%, EPS soft. **Grade on the 4-axis read-shape:** (a) NCO direction + is it still C&I-led or turning CRE/office? (b) provision build vs Q1? (c) ACL ratio building or flat? (d) NPL QoQ — does the −26% reverse, and does criticized/classified CRE (esp. office) migrate up? | **PRE-REG — the 2nd FL-sync leg.** DETERIORATING (≥3/4 axes, FL-RE book) = sync count → **1-of-≥2** (with CCBG benign, still short of the ≥2 bar alone). BENIGN/continued-improvement = count stays **0-of-≥2**. |
| — | **7/22 AMC** *(window context, NOT an FL-sync name)* | **Eagle Bancorp** | **EGBN** | **DC-corridor office CRE — NOT FL** (my CALENDAR tags it "DC corridor stress") | **⏳ AMC pending.** Read for national/DC **office-CRE tone** only (provision/office-criticized direction) as context for the CRE backdrop. | **EXCLUDED from the FL-sync count** — not FL-exposed. Rounds the small-tier *earnings window* temporally, does not feed the FL synchronization test. |

**⚠️ EXCLUSIONS (protect the sync count from contamination — a print can be bear-side WITHOUT being an FL-synchronization datum):**
- **OZK (Bank OZK)** — printed **bear-side construction/CRE deterioration tonight 7/21 (OZK-07 conjunction TRUE)**, BUT OZK is **NOT an FL-synchronization name**: its stress is the **RESG national construction book** (idiosyncratic, non-FL-condo frame). **Do NOT add OZK to the FL sync count.** It corroborates the broad CRE-construction backdrop but is not evidence of the FL-condo/FL-CRE transmission the rail tests. *(Same exclusion logic as EGBN's DC office book.)*
- General rule: a name counts only if the deterioration is in an **FL-exposed** book (FL CRE / FL condo-association / FL resi). National-construction (OZK-RESG), DC-office (EGBN), or pure-C&I deterioration does not feed the count.

**Live window:** ≥2-synchronized bar re-tests across the 7/21–28 prints (BKU 7/22 the next live leg; also SBCF/AMTB/USCB/VLY/SSB where dated).

**Source:** CCBG Q2 8-K exhibit ex991 (SEC EDGAR, released 7/21 BMO) — PROME-verified vs the primary exhibit; ingested to CORAL 7/21. BKU/EGBN rows pre-registered 7/21 EVE (PROME eve-pass); OZK exclusion per PROME (OZK-07 TRUE, non-FL frame). Mechanical entries, no rail move (consistent with CORAL's 7/21 employment grade).

---

## Watchlist (Q1 2026)

| Rank | Bank | Ticker | HQ | Assets | FL/CRE concentration | Q1 2026 credit signal | Call |
|------|------|--------|-----|--------|----------------------|-----------------------|------|
| 🟠 ELEVATED | **Amerant** | AMTB | Coral Gables | $9.9B | 21 of 23 banking centers in South Florida; CRE→held-for-sale transfers; $300M shelf | Classified **−9.7% to $320.3M** (curing), but **NPA $191.6M (1.93% of assets, ↑ from 1.38% YoY) / NPL $176.1M / special mention $148.2M all ↑**; 90+ accruing $1.0M→$2.3M YoY; NPL **2.6%**; **ACL covers only ~45% of NPLs** (thin & slipping); provision $7.8M; NCO 0.45% (↑ from 0.22% YoY) | Purest S-FL bank barometer; mixed cure-vs-migration. **Thinnest coverage = most exposed to a Q2 specific-reserve-build event.** Current driver CRE-HFS/C&I, not yet condo. |
| 🟠 ELEVATED | **BayFirst** | BAFN | St. Petersburg | $1.2B | FL-only; CRE ~27% ($216.6M) + constr $36.7M | **Net loss −$5.7M**; NPL 2.44%; NCO 1.98% ann.; **$80M dilutive PIPE** ($3.50/sh); new CEO; SBA "Bolt/Flashcap" runoff | Idiosyncratic (SBA small-biz, not RE). Small, dilution overhang. |
| 🟡 WATCH | **USCB Financial** | USCB | Miami | $2.8B | **CRE 370% of RBC**; constr 31% RBC; **$126M condo-assoc loans, 470+ associations, targeting 13,000 tri-county** | NPL **0.16%**, **zero NCOs**, classified 0.3%, ACL 1.16% — "exceptional" | **The most condo-wired bank — the direct condo-crisis→bank canary.** Clean now; concentration is the tail risk. |
| 🟡 WATCH | **Valley National** | VLY | Passaic NJ (large FL) | $64.5B | CRE **329% of RBC** (↓ from 333%, target <300); MF 2.6%; FL among 8-state footprint | NPL 0.85% (trended $296M→$360M→$434M); NCO $17.5M (CRE charge-offs $13.8M); criticized $4.1B/8.1% (↑ on C&I, mgmt expects decline); ACL 1.18% | NPL drift + CRE charge-offs the watch; mgmt guides improvement. FL "clients confident." |
| 🟠 ELEVATED | **Seacoast** | SBCF | Stuart | $21.1B (post-Villages) | **100% FL**; CRE non-OO **224% RBC** (>100% supervisory flag; broad CRE 227%); 50% of loans CRE-secured | CET1 11.7%; NPL 0.75% (+18bps QoQ); **30-89d $28.2M (10-Q VERIFIED): +65% YoY (was $17.2M) but −14% QoQ off a $32.9M Q4'25 peak** — YoY-elevated, NOT fresh-quarter accelerating; **sharper signal: nonaccrual $72M→$95M QoQ** + CRE-non-OO 60-89 $0.3→3.0M; NCO 11bps; ACL 1.39%; criticized 2.82% | Villages-deal integration + **100%-FL = the FL bellwether**; leading-edge elevated YoY but cooling QoQ; the real Q1 deterioration is in nonaccrual, not the 30-89 bucket. Watch migration to NCO at Q2. |
| 🟢 STABLE | **BankUnited** | BKU | Miami Lakes | ~$35B | CRE ~30% of loans; office 16% of CRE (4% medical) | EPS miss Q1 but **NPLs −26% QoQ**; NCO C&I-led; ACL/NPL 59%→76% (improving); CET1 12.2% | Credit trajectory improving; earnings soft. |
| 🟢 STABLE | **SouthState** | SSB | Winter Haven | $68.0B | Multi-state SE; FL production ~$640M Q1; investor CRE $18.3B | NPL 0.61%; NCO **9bps**; classified $2.5B/3.6% assets, **56% LTV / 98% current** ("little/no loss content"); watchlist = consumer+SBA, NOT FL CRE | Diversified, well-capitalized. **CORAL short thesis retired** ($90P expired worthless). |

---

## M&A / structural (2026)
- **Hancock Whitney → One Florida Bank** ($2.1B Orlando bank; $377.6M all-cash; close ~Q3 2026). Out-of-state consolidator buying FL franchise.
- **Seacoast (SBCF) → Villages Bancorporation** completed (+$4.4B → SBCF now $21.1B). Earlier: SBCF absorbed Professional Holding (PFHD).
- Read: healthy FL franchises still command takeover bids — *not* a distressed-seller market yet. Consistent with "banks aren't breaking."

## Cross-references
- → REGINALD: FL bank-level reads feed the convergence matrix; SSB/VLY also on REGINALD's national watchlist.
- Condo-crisis (pillar 1/3) → **USCB** is the cleanest direct wire (condo-association lending). If assessments/association loans sour, USCB cracks first.
- Insurance is now a *split* bank read: personal/reinsurance easing helps collateral (Citizens personal −2.6%, depop to ~385K), but commercial/condo-association lines still rising (Citizens Commercial Lines **+10.4% capped**; ⚠️ the **+18.8% uncapped** figure could NOT be re-confirmed per DEWEY 6/22 — lean on +10.4%) and remain an association cash-flow amplifier. This is the load-bearing **insurance→delinquency** channel (~12mo lag) that times the FL-bank loss transmission — full chain in `CLUSTER_FL_BANK_LEG.md`.

*Detail + sources → `research/SWEEP_2026-06-19.md` (Pillar 6) and `research/REFRESH_2026-06-19.md` (core four).*

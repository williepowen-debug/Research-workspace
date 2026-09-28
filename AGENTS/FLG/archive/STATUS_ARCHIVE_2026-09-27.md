# FLG STATUS ARCHIVE — rotated 2026-09-27

Verbatim, contiguous block rotated out of `STATUS.md` on 2026-09-27 (history, never current). crc32 of the block at rotation: `4ccff32b`.

---

## 🟠 SESSION 2026-09-24 — CATCH-UP: no new filings; the rent freeze is in court; price band 1 broke unseen

**Nothing fundamental printed.** EDGAR (CIK 0000910073) shows no filing after the 2026-08-14 13F-NT, so every credit figure below is still the Q2-2026 10-Q. Two things moved outside the filings:

| What | Fact | So what | KB |
|---|---|---|---|
| ⚠️ **Rent freeze in court** | 7 landlords suing to annul RGB Order #58; Justice Lantry (NY Sup. Ct., Manhattan) ordered Mayor's Office↔RGB communications ~9/16, citing "significant concern" over procedure. **No stay as of 9/17**; appeal expected either way | The mechanism's 2026 leg **could be removed by a court**. Annulment is **thesis-NEGATIVE** (bear case) / credit-positive for FLG. Experts expect landlords to lose. **Re-sourced at the primary:** *Kenilworth Holdings v. NYC RGB*, Art. 78, Richmond Index 85199/2026 → NY County 8/21; prayer (f) asks to enjoin the freeze and is **unruled** (reported 9/17). Docket itself unreachable (NYSCEF Cloudflare 403) | 059 (053 superseded) |
| 🔴 **VX-REG-6.03 band 1 BROKEN 9/16, unseen 8 days** | Close $12.58 on 9/16 < $12.82; **$12.30 on 9/23 = −13.6%** vs frozen $14.24; band 2 ($12.10) 1.6% below | **No script implements the ladder** (PROME census 9/23), and my T-07 checked a daily instrument quarterly. Routed to REGINALD + PROME | 054 |
| Why it moved | 8/28→9/23: FLG −8.5% · VLY −6.8% · KRE −4.7% · EGBN +1.8% | **Mostly an NYC-regional move**; FLG residual vs VLY ~−1.7pp. Steepest leg spans the 9/15 Barclays fireside — content not recovered; **attribution UNKNOWN** | 054 |
| Management's freeze model (May) | Stress assumes a **3-year** freeze; NOI −7–8% over 3 yrs on >70%-regulated buildings; $8.8B regulated = $4.6B pass @~1.5x DSCR + **$4.2B criticized/classified** | Their reserve assumption is harsher than the 1-year order. The $4.2B is the pool T-11 reprices | 055 |
| Sell-side | MS → Overweight, PT $17 (9/8); Barclays Buy (9/16). NIM guide cut to 2.20–2.30% on **higher payoffs** (date unverified, likely July) | The payoff channel that cleans the book (87.5% of non-accrual outflow) also shrinks earning assets | 056 |

**T-12 read path (written down):** the only guaranteed reads before 10/1 are PROME's 9/25 pre-fire check and my own 9/30 check. WALTER has been asked to watch for the case as best-effort only. **A court stay issued 9/26–9/29 is an accepted blind spot of up to one business day.**

**Housekeeping done:** 5 inbox packets processed; 3 ledgers carry `# Cadence: SCHEDULED` (boot staleness leg now quiet); T-07 re-dated, T-08 carries the legality leg, **T-12 registered** (litigation watch); CALENDAR's stale "watch the SHARE" row corrected to KB-FLG-049; WQ-176 confirmed `cut as drafted` (13 days late).

---



---

## Second rotated block — 2026-09-27 21:19 ET, crc32 of the block at rotation: `1ce1f18a`

## What this session established at the primary

**13 new KB rows, all `A1` PRIMARY (KB-FLG-028 → 040).** Everything below was pulled and computed by FLG, not inherited.

### ✅ Reconciliation to REGINALD — the seed holds

| Figure | REGINALD (MIRROR) | FLG at the primary | Verdict |
|---|---|---|---|
| Total risk-based capital (SR 07-1 **denominator**) | $10.00B | **$10,003M** | ✅ **EXACT** |
| ACL roll-forward identity | begin $1,029,999K … end $869,000K | 10-Q Note 6 ties to the dollar | ✅ **CONFIRMED** |
| Net charge-offs H1-2026 | $176.9M implied | $178M stated | ✅ ties |
| SR 07-1 ratio | 327.5% | 327.5% *(≤351.6% if owner-occupied wrongly included)* | ✅ **REPRODUCES** |
| Total loans | $61,195M *(Call Report)* | $60,987M *(10-Q HFI)* | ✅ within 0.34% — leases/other |
| Coverage | 29% | **31.04%** | ⚠️ **denominator, see below** |

**REGINALD's Q2b work is independently confirmed.** The one delta is a perimeter difference, not an error: the seed used the Call Report's $2,988M nonaccrual denominator; the 10-Q reads $2,800M (HFI, excluding $5M held-for-sale). **The level moves, the direction does not** — coverage still fell 3.58pp over H1, ACL −15.6% against nonaccrual −5.9%.

### 🔴 Q2c ANSWERED — the nonaccrual decline is neither charge-off nor cure

Nonaccrual roll-forward, six months ended 2026-06-30: begin $2,975M **+ $780M formation** − $100M charge-offs − $4M transfers − **$836M payoffs/dispositions** − **$15M cures** = $2,800M.

**Payoff 87.5% · charge-off 10.5% · cure 1.6%.** ⇒ DAEDALUS's nonaccrual-leg suspension on K-3 is **LIFTED**. **Twice now the binary was wrong and the truth was a third cell** (Q2b: neither release nor disposition; Q2c: neither charge-off nor cure). The pattern: **this book is not healing, it is being handed off.**

### 🔴 THE MECHANISM FIRED — and the wake register had it as pending

NYC RGB **approved a rent freeze in June 2026, effective October 2026**. FLG's Q2 provision rose $18M QoQ explicitly for it. Exposure: **$8.9B** with ≥50% rent-regulated units, inside **$13.4B** of NYC multifamily and **$26,931M** of total multifamily.

⚠️ **`TRIGGERS.tsv` T-06 carried this as `[EST] 2027-05-03`** — a fired event rendering as pending, with nothing able to tell the two apart. **The desk was ~10 weeks blind to its own defining mechanism while holding a correctly-formatted, in-date wake row aimed at it.** Corrected: T-06 re-scoped to 2027; **T-08** (freeze effective, 2026-10-01, HARD) and **T-09** (Q2-2027 DSCR cycle, RULE) registered.

⏱️ 🔴 **FUSE CORRECTED — I HAD IT A YEAR TOO SHORT AND HAD ALREADY SHIPPED IT (KB-FLG-052).** RGB Order #58 governs leases **commencing 2026-10-01 → 2027-09-30**, so it phases in as leases renew. FY2026 financials (reviewed **Q2-2027**) hold at most Oct–Dec 2026 of partial exposure; **FY2027 financials, reviewed Q2-2028, are the first carrying most of a freeze year.** ⇒ **the bite is Q2-2028** (new trigger T-11); T-09 is demoted to an early watch point. I stated "~12-month fuse" in THESIS v1.0, STATUS, CALENDAR, T-08/T-09 and in packets to REGINALD and PROME — all corrected, both desks told. ⚠️ **And a 0% guideline CAPS revenue rather than cutting it** — DSCR degrades by costs outrunning frozen rents, grinding and compounding, not a step down.

### 🔴 K-1 had a construct-validity defect — it would have fired on the wrong book

| Book | 2025-12-31 | 2026-06-30 | H1 |
|---|---:|---:|---|
| **Multi-family** *(the thesis's subject)* | $28,983M | **$26,931M** | 🔴 **−7.08%** |
| Commercial & industrial | $15,217M | $18,563M | **+21.99%** |
| **Total loans HFI** | $60,732M | $60,987M | **+0.42%** |

**`loans_qoq_pct +0.9%` is a MIX SHIFT, not the end of the run-off.** K-1 as written would have declared a NYC-rent-regulated-multifamily thesis dead on the strength of **C&I growth**. Leg 1 re-cut onto multifamily dollars, where it is not satisfied and not close. ⚠️ **The error made the kill EASIER — the rail was biased toward retiring a live thesis.**

✅ **DAEDALUS's 2026-08-23 sweep ASK is answered in the same edit:** K-1's leg 2 had no registered instrument (rendering `NOT FIRED` when the honest state was `UNGRADEABLE`). The nonaccrual-rate instrument was in the 10-Q all along and is now in the cell. **No leg dropped.**

### Other primary reads

- **Multifamily net charge-off rate is FLAT YoY at 1.17%** annualised (Q2-2026 = Q2-2025). The aggregate NCO improvement (0.66% vs 0.72%) is CRE and composition, **not multifamily healing**.
- **30–89 day delinquencies −63%** ($986M → $368M) — genuine early-stage improvement, but $780M migrated into nonaccrual over the same window, so much of the drain is **migration, not cure**.
- **$51M of 90+ days past due AND STILL ACCRUING**, against zero at 12/31/2025. Small, negative, and a classification choice.
- **40% of nonaccrual loans are current on contractual terms** — the rent-regulated signature: the loan pays, but the collateral math fails.

### ⚠️ CHARTER CORRECTION — there is no longer a holding company

**Flagstar Financial, Inc. merged INTO Flagstar Bank, N.A. in October 2025** (plan of merger 2025-09-22, 10-Q exhibit 2.1). The SEC registrant and NYSE issuer for FLG is now **FLAGSTAR BANK, N.A.** (CIK 0000910073). `CLAUDE.md` § IDENTITY and DENOMINATOR DISCIPLINE rule (b) both assume a live holdco/bank split; for quarters from 2025Q4 that split **does not exist**, and a 10-Q figure is directly comparable to the RSSD 694904 Call Report series. For 2023Q3–2025Q3 it still holds. **The perimeter break falls INSIDE the 12-quarter seed series.** Routed to PROME — a charter edit is not FLG's to make. Local ledgers corrected.

---


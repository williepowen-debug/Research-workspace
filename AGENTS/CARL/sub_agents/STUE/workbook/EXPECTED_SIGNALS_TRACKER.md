# LIVE — Last real data refresh: 2026-07-31 | Staleness sweep (no data): 2026-08-10 | Next: NY Fed Q2 HHDC (modal Tue 2026-08-04)
# STRUCK 2026-08-10 (PROME round-2 audit item 4, inbox packet processed): the "THIS FILE IS
# CURRENTLY UNENFORCED" banner below was FALSE as of this check — CARL shipped the .md-widening
# LEDGER_GLOB fix the same evening it was requested (7/31), verified scanning. Wrong-in-the-safe-
# direction, but a state banner that doesn't match state is its own defect class
# ([[finding_banner_is_a_warning_not_a_fix]]). No re-verification of LIQUID's file performed here
# (out of scope) — do not assume it is still unenforced either.

# STUE — Expected-Signals Tracker (absence-is-data)

**Born:** 2026-07-31 (DAEDALUS blueprint §7 "STANDING DISCIPLINES / EXPECTED_SIGNALS", MARCO pattern; format matched to LIQUID's `EXPECTED_SIGNALS_TRACKER.md`) · **Owner:** STUE
**Purpose:** Signals that **SHOULD appear if the student-loan stress thesis is transmitting.** Their **absence is data** — and the reason this file exists is that STUE spent July unable to distinguish *"the downstream hasn't fired yet"* from *"the downstream cannot fire"* from *"we were reading the wrong series."*

> ⚠️ **The registration rule that makes this worth keeping: a prior is registered BEFORE the check runs.** A signal that fails to appear only counts as evidence if we said in advance that we expected it. ES-05 is the clearest case — its prior is *"probably WON'T appear"*, so a null result **confirms** rather than disappoints.

---

## Active Expected Signals

| ES-ID | Signal — what SHOULD appear if the thesis transmits | Bands (Y / O / R) | Instrument | Cadence | **Implication if ABSENT** |
|---|---|---|---|---|---|
| **ES-STUE-01** | **Forbearance reservoir DRAINS.** 8.4M / ~$485B sits in forbearance; the thesis says it converts to repayment→delinquency | forbearance −5% / −10% / −20% QoQ | FSA Data Center quarterly (portfolio status by recipient count) | Quarterly (~Sep) | 🔴 **The most thesis-damaging absence available.** A reservoir that does not drain means the conversion mechanism is being administratively deferred, not delayed — the Q3-Q4 wave would be a Q3-Q4 *2027* wave |
| **ES-STUE-02** | **Servicer-failure tell — does CRL-28's frozen threshold fire?** ⚠️ **RE-POINTED 2026-08-10 (PROME round-2 audit item 2, inbox packet processed) — was born stale, naming CRL-14 (retired the same day this row was written, 7/31) while running CRL-28's exact instrument.** CRL-28 = MOHELA CFPB-complaint borrower-harm signature, THRESHOLD FROZEN 55/day, window Oct 1 2026–Sep 30 2027 | complaints >35/day / >45/day / **≥55/day** — R band re-cut to equal CRL-28's frozen absolute threshold exactly (was >60/day, which put 55 in the O–R gap so RED would only fire AFTER CRL-28 already confirmed) | CFPB complaint API, `company=MOHELA` ⚠️ **5-6d publication lag — never read the trailing week** | ~Aug 20, then post-Oct completion | 🟠 **CRL-28's LAST live leg fails** if this row goes DID_NOT_APPEAR twice. Wave-1 (Jul 1-19) already showed **no spike** (28.4/day). A second null through Oct means CRL-28 has no working mechanism, not merely a stalled threshold — that is a STUCK→MISSED question |
| **ES-STUE-03** | **90+ DQ sustains or rises on the 2nd print.** CRL-04 confirmed at 10.3% off a single print | holds ≥10% / rises >11% / rises >12% | NY Fed HHDC (balance-based 90+ share) | **Q2 print, modal Tue 8/4** | 🟠 A retrace below 10% makes CRL-04 a **single-print artifact**. ⚠️ Pair with the flow reading: transition-INTO-90+ already fell 16.2%→10.9%, so **stock-up/flow-down is the live ambiguity this print resolves** |
| **ES-STUE-04** | **Cure channel proves DURABLE** (~1.3M/qtr exits via rehab/consolidation/discharge) | persists ±20% / grows >1.6M / grows >2.0M | FSA stock vs NY Fed gross DRG flow — **the difference IS the instrument** | Quarterly (~Sep) | 🟢 **Absence here HELPS the bear thesis** — if cures collapse, the wall grows at the gross rate (2.6M/qtr) not the net (1.3M). **Registered as a two-sided signal on purpose:** this is the one row where the null is bullish for STUE's thesis, and that asymmetry is exactly why it must be pre-registered |
| **ES-STUE-05** | **🆕 SLABS transmission — deterioration reaches the trusts** (private SL + FFELP) | private-trust CNL +25bps / +50bps / +100bps; any tranche CE breach = R | Trustee/servicer reports · EDGAR ABS-EE / 10-D · rating actions | Quarterly, on filing | ⚠️ **PRIOR REGISTERED BEFORE LOOKING: probably WILL NOT APPEAR — and that is the expected result.** FFELP is ~97% federally guaranteed (extension/prepay risk, not credit); private SLABS sit on a different, largely cosigned pool that is **not** the ~9M defaulted cohort. **Absence CONFIRMS the prior and closes the question. An APPEARANCE is the surprise** — and would be the first tradeable expression the domain has ever produced |
| **ES-STUE-06** | **🆕 Higher-ed closures feed the borrower-defense pipeline** | Title IV HCM list +10% / +25% / a major-chain closure | FSA Data Center quarterly (**already pulled** — HCM institutions ship alongside portfolio data) | Quarterly (~Sep) | 🟡 Weak signal by design. Absence just means the BD pipeline stays at its ~271K run-rate; **no thesis consequence.** Registered so the newly-absorbed domain has a row-shape, not because it is load-bearing |

**Standing read (2026-07-31, registration):** **ES-02 = ALREADY-NULL-ONCE** (wave-1 no spike, partial read). **ES-03 resolves in ~4 days.** ES-01/04/06 all resolve on the **same FSA Q2 print (~Sep)** — ⚠️ *that is a single point of failure: one delayed release blinds three signals at once* (cf. register S4, publisher shock). ES-05 unexamined.

## Response protocol

1. **Y:** log here + a STATUS row. No routing.
2. **O:** route to CARL with the worked reasoning. **ES-01 or ES-03 at O = a thesis-level move, not a data point.**
3. **R:** CARL + PROME same session.
4. **⚠️ TWO-OR-MORE RULE:** ES-01 **and** ES-02 both absent at their next checks = **the transmission thesis is failing on its own pre-registered terms**, independent of what any single threshold does. That is the finding, and it must be routed even though no individual row breached.
5. A signal that resolves **DID_NOT_APPEAR** gets a fired-log row naming the episode — that record *is* the absence-is-data output.

## Resolved / fired log

| ES-ID | Date | Band | Outcome (APPEARED / DID_NOT_APPEAR) | Notes |
|---|---|---|---|---|
| ES-STUE-02 | 2026-07-19 | — | **DID_NOT_APPEAR (partial)** | SAVE wave-1, Jul 1-19: **539 complaints ≈ 28.4/day vs June 27.0/day — no escalation.** ⚠️ Partial read only (5-6d lag); re-check ~Aug 20. First entry in this log, back-dated at registration |

## How to use

1. Check at the owning cadence, or whenever a catalyst in STATUS fires.
2. Band fire → response protocol + a fired-log row.
3. **A catalyst that passes with NOTHING firing → log DID_NOT_APPEAR against that catalyst by name.** An empty fired-log after a live quarter is not a clean bill of health — it means nobody ran the check (`[[finding_verification_zero_is_ambiguous]]`).
4. Re-validate bands at each STATUS refresh. A band that no longer maps to a live threshold is **re-derived or FROZEN, never silently kept**.

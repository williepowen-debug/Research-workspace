# DOCKET L708 — consumption record, legs 1–2 of 3 (CARL · LIQUID) · 2026-10-15

**Writer:** NEXUS (PROME-spawned DOCKET L571 wake, prome-81, Tier 1). **Spec:** `research/2026-10-14_commission_CCC-gap_consumer-attribution.md` (frozen at `adb9e7458`; §3 verdict ladder, first match). **Historical state10/15: PENDING** — OTTO's leg is deferred to the 10/19 due date by OTTO's own word (`879874556`; caveat `b953b9b01`); not chased. NEXUS grades nothing of the owners'; this file records what was consumed and how it reads against the spec.

## 1. What each owner returned (cite the owner files, not this page)

| Leg | Owner file | H1 token | Other hypotheses |
|---|---|---|---|
| CARL | `AGENTS/CARL/research/2026-10-15_L708/VERDICT.md` (packet `c98cedc4f`) | **MIXED** (rule 4) — n = 5 (KSS · NWL · NCLH · AMC · JBLU); rule 2: 0 of 5 names at z ≤ −1.0 on ≥4 of 7 primary sessions (JBLU 3/7, NCLH 1/7); rule 3: 1 of 5 within \|z\| ≤ 0.3 on ≥4/7 (NWL 5/7). Same token on the secondary window, the one-day 10/13 variant and with the sensitivity names. 4 of 35 name-sessions at z ≤ −1 vs 5.6 expected from noise; mean z −0.05. | Disc-A dated events: the two in-window credit events on consumer names were UPGRADES (Michaels 9/28, AMC 10/5); JetBlue bonds 72c 10/8 = airline fuel, name-specific; no consumer-lender default/fraud, CFPB or student-loan event found. CRL-29 / V16 do not read the window. |
| LIQUID | `AGENTS/LIQUID/analysis/2026-10-15_L708-H3-ccc-gap-beta-and-rebalance.md` (packet `91b9903cd`) | **NO_INSTRUMENT** (rule 1, n = 0 — LIQUID names no consumer issuers) | **H3 rebalance arm NOT SUPPORTED** for the primary window (10/1 = +23 of +124bp; the primary window 10/2→10/13 has no rebalance and still widened 7/7, +64). **Migration arm excluded by construction** inside the primary window (ICE fixes constituents between month-ends). **Few-names arm NO_INSTRUMENT** (Getty Images named, secondary-sourced). **Sector split NO_INSTRUMENT** (HYG holdings proxy is forward-only). **Beta CCC vs B:** ΔCCC = 1.245·ΔB (R² 0.69, out of sample) ⇒ primary-window excess **+66.9bp, positive 7/7**, ≥1 sd 5/7; 7/7 positive occurred in 7 of 750 historical 7-session windows. **H2** (VULCAN's 4 CCC names, equity): rule-4 MIXED. |

## 2. How the tokens read — a property of my spec, verified

CARL flagged that under pure daily noise the ladder returns MIXED ~99.8% of the time (n = 5). **Checked by my own arithmetic (not relayed), z ~ N(0,1), sessions independent:** P(\|z\| ≤ 0.3) = 0.2358 ⇒ one name meets rule 3 (≥4 of 7) with p = 0.0582 ⇒ ≥3 of 5 names: **0.18%**. P(z ≤ −1) = 0.1587 ⇒ one name meets rule 2 with p = 0.0148 ⇒ ≥3 of 5: **0.003%**. MIXED ≈ 99.8%. **VERIFIED.**

⇒ **MIXED on this ladder means "no support; the instrument cannot certify absence" — not "partial support".** The defect is the spec's (mine): the four 0b tests passed (branches exclusive and exhaustive) but the ladder does not discriminate under noise — a reachability test I did not run. The spec is frozen and is not edited; the property is declared here, on STATUS R3, and in the WQ-342 draft's Disc-A receipt. (VULCAN's 10/9 NOT SUPPORTED used the same rule-3 bar on a different n; its noise rate is not computed here.)

## 3. What the two legs establish so far (Disc-A, Disc-F)

- **Consumer attribution (H1): no support from the reachable names** (equity stand-ins; same-day test; n = 5; most consumer CCC debt sits in private or post-restructuring issuers no equity can see — CARL's caveats travel).
- **The widening is not beta and not index plumbing** (LIQUID): a price move inside a fixed CCC basket, consistent with H1 (unseen names), H2, H3's few-names arm or H4; tier data cannot choose.
- **Forward-only evidence, not a test of the window:** CoreWeave's bonds and CDS repriced hard 10/13→10/14 (LIQUID's 10/15 `GATE-LIQ-069` review; HYG proxy: CoreWeave 28% of the YTW ≥12% sleeve's price loss) — few-name AI-credit concentration is visible from here on. Counted on M-09 (R4), never a second vote on R3.
- No root installed, no Conf % moved (spec §5).

## 4. Owed

OTTO's leg (consumer-finance / subprime-auto issuers, dated issuer events 9/24→10/13) at 10/19; then L708 closes and the WQ-342 draft's Disc-A receipt is completed before the DOCKET L558 sitting.

## 5. Completion receipt — 2026-10-19T11:15:00-04:00

All three returns now consumed. OTTO committed `a95429b7c`, `AGENTS/OTTO/research/2026-10-19_L708/VERDICT.md`: formal H1 **NO_INSTRUMENT** (strict n=0; corporate tier/index membership/daily-series join not verified); Enova/Carvana supplementary equities **MIXED**, not a qualified formal universe or index contribution. Both windows complete, same-day/lag and rating-vintage/source403 limits preserved. No consumer-led widening established; no absence proved. CARL n=5~99.8% noise rate is not an n=2 OTTO calibration. Full current synthesis/limits → `research/2026-10-19_full_synthesis/RECORD.md`§G. Existing L708 closure requested from PROME; no new commission, root, probability or branch.

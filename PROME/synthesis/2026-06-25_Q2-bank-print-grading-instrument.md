# Q2 Bank-Print Grading Instrument (Jul 16–30, 2026)
**Date built:** 2026-06-25 (late ET) · **Author:** Claude Code Prome · **Inputs:** CARL_FH (consumer/monoline rows) + REGINALD_T (regional/CRE rows), Prome-consolidated
**Derives from:** `2026-06-25_front-back-reconciliation.md` (the Q2 exception = (b) AOCI + (c) WAL; (a) trimmed to 2027). This is the **ready-to-grade card** for the actual prints.
**Status:** RESEARCH/DRAFT. Q1 baselines = agent-curated/primary as flagged — **verify vs the 10-Q/release before any trade.** Trade content PROPOSE-only → Will/FORGE.

---

## How to use this

Grade each print on **one master question + two discriminators**, then tally into the path diagnostics.

**MASTER GRADE — BUILD vs RELEASE:** is **Provision expense $ > Net charge-off $** this quarter?
- **Provision > NCO = BUILDING** the allowance → loss recognized to P&L/CET1 *now* = **Q2 transmission live** (does not defer).
- **Provision < NCO = RELEASING** → drawing the reserve down to flatter EPS = **mask/defer holds**.
- Cross-check: ACL coverage ratio (ACL/loans) QoQ direction + ACL $ balance QoQ.

**DISCRIMINATOR 1 — is the build SPECIFIC or COLLECTIVE?** (the same test on both sides; settles whether a build counts as transmission):
| | Consumer (CARL) | CRE/regional (REGINALD) | Counts as transmission? |
|---|---|---|---|
| **SPECIFIC** | "receivables + mix" / named cohort migration | individually-evaluated specific reserve on a named impaired credit | **YES — genuine** |
| **COLLECTIVE / macro-overlay** | "economic outlook / scenario weighting" | pooled CECL Q-factors (GDP/unemployment/CRE-PI) — all names build similar bp | **NO — it's BETA** (a synchronized scenario reprice, read like the 6/24 HY widening; a regime tell, not credit substance) |

> A **collective/macro-overlay** build "pre-confirms" that *other* banks will show the same beta synchrony — but the **≥2-bank path-(a) transmission diagnostic counts SPECIFIC-reserve builds only.** Don't score beta as substance.

**DISCRIMINATOR 2 — the non-credit (AOCI) axis is separate:** a name can print a **clean NCO** and still transmit via **AOCI/NIM/TBV** (rates, not credit). Grade it independently (path b). *Single highest mis-grade risk = reading ZION's green NCO as thesis-clear while its muni/AOCI book breaks TBV.*

---

## Print calendar + leading-gate sequence

```
Jul 16   CFG, OZK            ← BLIND first reads (before the monoline gate) — grade on own roll-forward
Jul 21   ZION + SYF, ALLY    ← the MONOLINE GATE prints here (COF ~Jul 21-23, IR-soft)
Jul 22   EGBN                ← reads AFTER the gate
Jul 30   WAL                 ← reads AFTER the gate
```

**The gate:** the un-maskable consumer leading edge (monolines, Jul 21) prints *before* EGBN/WAL.
- **Monoline BEAT Jul 21** (front-half base case ~65-70%; all green 6/25, SYF +2.9%) → no macro forcing function → expect EGBN/WAL builds to **NOT fire** → fade path (a) before they print.
- **Monoline BREAK Jul 21** (NCO up + coverage *falling*, ABS-curve corroborated) → macro pressure live → EGBN/WAL build odds **rise**.
- CFG/OZK (Jul 16) get no gate — grade standalone; they're the blind first temperature read.

---

## The grading table

### Consumer / monoline (CARL_FH) — Axis A

| Name | Print | BUILD if (transmission) | RELEASE if (mask/defer) | Macro-overlay tell | Q1 posture |
|---|---|---|---|---|---|
| **SYF** | Jul 21 (hard) | Prov > NCO; coverage **≥10.42%** holds/rises vs flat-down NCO (costly confession); **RSA payments falling** = losses under the hood | Prov < NCO; coverage **≤~10.1%** (−30bps+); guide reaffirmed to flatter EPS | roll-forward change to "economic outlook/scenario" = overlay→beta | **BUILT** +36bps→10.42% vs improving NCO → **leans transmission-live** |
| **ALLY** | Jul 21 (hard) | Q2 **reverses** Q1 release: Prov > NCO, coverage rebuilds; **retail-auto NCO ≥+30bps QoQ** (→CRL-21 on 2nd) | continues Q1: Prov < NCO, ACL$ ↓ again | build tied to "used-vehicle/recovery" = cohort; "macro/unemployment scenario" = overlay | **RELEASED ~$224M** Q1 → **leans mask-deferring**; reversal = transmission |
| **COF (card)** | ~Jul 21-23 (soft) | continued build; **card-seg provision > card NCO**; **Card NCO ≥+25bps QoQ** (→CRL-20 on 2nd) | ACL drawn down; Discover conforming marks used to offset | segment roll-forward "economic outlook" = overlay; "growth+Discover+subprime mix" = cohort | **BUILT $230M** ($155M subprime) → **transmission-leaning**; the bridge ↓ |

**COF = the bridge instrument (highest-value single line).** Segment provision split: **Card = Axis-A consumer**, **Commercial = Axis-B CRE** — both on one Jul-21 balance sheet.
- Card builds, Commercial flat/release → **consumer leading, CRE still deferring** (Axis A live, Axis B 2027).
- **Both build → SYNCHRONIZED transmission** — COF pre-confirms the regional CRE path *before* EGBN/WAL print.
- ⚠️ Discover conforming one-time ACL (~100% platform by Q3'26) can inflate the apparent build — **flag one-time-conforming vs run-rate** before scoring.

### Regional / CRE (REGINALD_T) — Axis B + the rate axis

| Name | Print | Path | BUILD / fire if | RELEASE / disconfirm if | Note |
|---|---|---|---|---|---|
| **CFG** | Jul 16 | (a) reserve | Prov > NCO **and** ACL/loans ↑ QoQ **and** criticized/NPL rising — reverses 5-qtr NCO decline (Q1 0.39%); esp. CRE or BDC fund-fin $12.5B (specific) | NCO <0.39%, release continues, ACL/loans flat-down | blind first read; consumer 18.7% = housing-secured (Axis-B) |
| **CFG** | Jul 16 | (b) AOCI/NIM | AOCI more negative 6/30 **and** TBV/sh ↓ **and/or** NIM compresses (FHLB 60x funding-sensitive) | TBV ↑, NIM stable, AOCI flat-improving | counts even on clean NCO |
| **OZK** | Jul 16 | (a) reservoir | past-due climbs off Q1 $465M (1.41%) **and** NCO >0.57% toward 50bps guide **and** specific RESG reserves (IQHQ pre-position) | past-due reverts (lumpy), NCO ≤0.57%, no RESG migration | RESG 88%; IQHQ Aug maturity is *after* this print. **Research-grade: OZK files no 10-Q** (FDIC Call Report) |
| **ZION** | Jul 21 | (a) credit | NCO turns UP off 0.03% trough **and** release STOPS (provision positive) = Hyp-A heal falsified | NCO ~0.03%, release continues = Hyp-A holds (bull-control) | designated credit bull-control |
| **ZION** | Jul 21 | **(b) muni/AOCI — FALSE-CONTROL TRAP** | AOCI more negative 6/30 on **muni $5.78B/AFS** (10Y +11bp) **and** TBV/sh ↓ **and/or** NIM compresses — **EVEN IF NCO clean** | TBV ↑, AOCI stable, Basel III +93bps absorbs the mark | **highest mis-grade risk** — green NCO + falling TBV/AOCI = transmission via the non-credit axis |
| **EGBN** | Jul 22 | (a) reserve — **cleanest candidate** | coverage of nonaccruals keeps falling off Q1 114% (was 149%) **or** catch-up provision (Prov >> NCO) rebuilds toward 149% **and** IPRE/office nonaccrual rises (NPA off Q1 1.31%) — specific | coverage rebuilds via NPA **cure** (not provision); NPA reverts toward 1.04%; no new office migration | CRE 547%/DC 100%; one office already → nonaccrual. **Gated by monoline Jul 21** |
| **EGBN** | Jul 22 | (b) AOCI/NIM | AOCI worse 6/30, TBV ↓, NIM compresses (DC-corridor deposit-sensitive) | stable TBV/NIM/AOCI | secondary to its (a) |
| **WAL** | Jul 30 | **(c) full charge-off** (bear-confirm ~28-32%) | ex-fraud NCO **>55bps** (Q1 39bps) **and** majority (>$50M) of the **$99M** life-sci credit charged off in-Q2 | NCO <40bps, $99M cures/sponsor returns, classified continues −9bp trend (Q1 1.08%), H2-decline guide affirmed | $99M = sponsor **walk-away** (resists extend-and-pretend) |
| **WAL** | Jul 30 | **(c) build-but-defer** (partial transmission) | NCO 40-45bps (priced) **and** $99M kept nonaccrual with a **larger specific reserve** **and** classified rises (office classified >$500M) | — | path-(a)-at-WAL: reserve builds, charge-off defers to Q3/Q4/2027 — grade as partial, NOT bear-confirm |
| **WAL** | Jul 30 | (b) AOCI/NIM | AOCI worse + TBV ↓ + NIM compress regardless of NCO | stable | counts toward ≥2-name non-credit tally |

---

## Scoring the set — the path diagnostics

- **Path (a) — synchronized reserve-build [reconciled odds ~15-22%] FIRES** if **≥2 of {CFG, OZK, EGBN, WAL} show SPECIFIC-bucket builds** (Prov > NCO on *named-credit* migration) in Q2. EGBN is the single most likely; needs a 2nd (OZK reservoir-conversion or WAL build-but-defer) to clear ≥2. *Collective/macro-overlay builds do NOT count (beta).*
- **Path (b) — non-credit/AOCI [~25-30%] FIRES** if **≥2 of {ZION, WAL, CFG, EGBN} sell off on AOCI/NIM/TBV regardless of NCO.** Re-pull 10Y at the **6/30 mark** (4.30→4.41 = live-but-mild). ZION is lead candidate + the trap. *This is the cleanest surviving Q2 exception — rates-driven, source-independent.*
- **Path (c) — WAL single-name [~28-32%]** = WAL standalone full charge-off (no ≥2 needed). Build-but-defer = partial (counts toward a, not c).

**Non-print legs (for completeness):** Labor has no Q2 print — its only near-term optionality is the **Aug 7 NFP** broad-break tail (~30%). Migration is a 2027 leg (winter-27 FL-$ hole → FL bank earnings Q1-Q2 2027).

---

## Decision rule (PROPOSE-only → Will/FORGE)

1. **Default (monoline beat + releases/collective-only builds):** the Q2 exception does NOT fire → confirms the 2027-duration thesis → **roll bank duration to Q1-Q2 2027, no fresh Q2 short.**
2. **Path (b) fires** (≥2 AOCI/NIM/TBV selloffs): the rates-driven exception is live — this is the most likely Q2 surprise; size to ~25-30%. Watch ZION especially (don't mis-grade its green NCO).
3. **Path (a) fires** (≥2 SPECIFIC builds): genuine synchronized credit transmission arriving early — escalate; but confirm builds are specific not collective.
4. **Path (c) fires** (WAL full charge-off): single-name bear-confirm.
5. **COF both-segments build** = the strongest single signal — synchronized consumer+CRE on one balance sheet, ahead of the regionals.
6. **Beta guard:** if builds are collective/macro-overlay across the board, that's the *higher-for-longer regime repricing* (a beta tell, akin to HY widening) — note it, but it does NOT confirm credit transmission and is NOT a fresh-short trigger.

---

## Provenance / marks
- Consumer Q1 baselines = CARL curated STATUS (Q1'26, rel Apr 21-22) — verify vs 10-Q. Regional baselines = REGINALD primary-verified (WAL/EGBN 10-Q direct; ZION/CFG EDGAR; **OZK research-grade — no 10-Q, FDIC Call Report**). Print dates aggregator-soft (esp. COF ~Jul 21-23) — confirm vs IR calendars (~early Jul).
- Marks: HY OAS 276 / CCC 964 / CCC-HY 3.49× [FRED 6/24]; 10Y 4.30 [3/31] → 4.41 [6/24] (re-pull at 6/30); WAL $81.48, monolines green (COF +2.2/SYF +2.9/ALLY +1.7), KRE +1.1% [6/25 close].
- Trade lines PROPOSE-only. Position/broker truth = Will/FORGE. Refresh dashboard/FRED before re-citing levels.

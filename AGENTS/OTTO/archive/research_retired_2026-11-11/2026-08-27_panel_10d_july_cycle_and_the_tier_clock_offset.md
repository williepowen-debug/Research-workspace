# The July 10-D cycle, the tier clock offset, and a data-destroying defect in OTTO's own panel

**Date:** 2026-08-27 (s019, second block) · **Run:** `panel_10d.py` 2026-08-27T20:02:32, positive control **PASS**
**Status:** `[CONF SEC 10-D EX-99.1, 9 deals, run-stamped 2026-08-27]`

---

## 1. The headline: the broad tier turned on July data, and it cannot yet be paired with the deep tier

**All three SDART broad-subprime deals fell on 60+ DQ on the 8/17 filing — the first broad decline
since the spring trough. Both Bridgecrest/Carvana deals fell too. The deep tier has published nothing
for July.**

| Tier | Deal | 60+ DQ prior | 60+ DQ latest | MoM | Collection month |
|---|---|---|---|---|---|
| BROAD | SDART 2022-6 | 10.45 | **10.11** | **−0.34** | July |
| BROAD | SDART 2023-1 | 9.96 | **9.68** | **−0.28** | July |
| BROAD | SDART 2024-1 | 9.19 | **9.08** | **−0.11** | July |
| CARVANA | BLAST 2023-1 | 15.20 | **14.80** | **−0.40** | July |
| CARVANA | BLAST 2024-1 | 15.57 | **15.30** | **−0.27** | July |
| DEEP | EART 2022-2 | 14.79 | 14.83 | +0.04 | **June** |
| DEEP | EART 2022-3 | 13.59 | 14.08 | +0.49 | **June** |
| DEEP | EART 2023-1 | 11.97 | 11.81 | −0.16 | **June** |
| DEEP | EART 2024-1 | 10.26 | 10.81 | +0.55 | **June** |

## 2. ⚠ THE TIER CLOCK OFFSET — the finding that governs how the table above may be read

**The two tiers are one month apart, and the difference is a filing calendar, not a market.**
Verified at the exhibits, not inferred from filing dates:

| Filing | Declared Collection Period | = |
|---|---|---|
| SDART, filed 8/17 | `Collection Period Beginning: 07/01/2026 · Ending: 07/31/2026` | **July** |
| BLAST, filed 8/17 | `Collection Period: 7/1/2026 Through 7/31/2026` | **July** |
| EART, filed 7/30 | `Collection Period Beginning: 06/01/2026 · Ending: 06/30/2026` | **June** |

Exeter files month-end; Santander and Bridgecrest file to a 15th-17th distribution date. **So reading
"EART rising while SDART falls" off the latest row of each is comparing JUNE-deep against JULY-broad,
and would manufacture a tier divergence out of a clock difference.** This is the specific error a
consumer of this panel is most likely to make, because the ledger's own `filing_date` column invites it.

**Matched on collection month — the only honest comparison:**

- **JUNE (both tiers observable):** EART **3 of 4 rising** (+0.04 / +0.49 / −0.16 / +0.55);
  SDART **3 of 3 rising** (+0.36 / +0.54 / +0.47). ⇒ **Both tiers climbing. No reversal.**
- **JULY (broad + Carvana only):** SDART **3 of 3 fell**; BLAST **2 of 2 fell**; **EART not published.**

**⇒ There is no two-tier reversal on the record. There is a one-tier, one-month give-back**, and it
follows a large June jump (+0.36/+0.54/+0.47), so a −0.11 to −0.40 move is well inside single-month
noise on this panel. **Both tiers remain far above their spring troughs** — broad **+1.06 to +1.30pp**,
deep **+1.93 to +3.33pp**. Off-trough direction is intact in both.

**What settles it, with a date: EART's July 10-D lands ~Aug 28-31.** That is the print that makes July
a real two-tier observation. Poll it; send CARL the deal-level numbers unprompted the day it lands.

## 3. Carvana: the collateral read is UNFROZEN, and it gave back

`[CONF BLAST 2024-1 EX-99.1, filed 2026-08-17, July collection]` **60+ DQ 15.57 → 15.30 (−0.27pp)**,
**CNL 24.67 → 25.41 (+0.74pp)**, EXT **4.56%**. BLAST 2023-1: 60+ DQ **14.80** (−0.40), CNL **25.70**,
EXT **3.93%**. The read had been **frozen at 7/15 for 43 days**.

**What this does and does not say.** The "sharpest single-month DQ break in the panel" (+1.80pp on the
7/15 filing) **did not continue** — it partially gave back while cumulative losses kept accruing.
**That is the ordinary shape of a delinquency spike converting into charge-offs**, not evidence of
either deterioration or improvement in origination quality. **Extension rates remain LOW** (4.56% /
3.93% vs Exeter's 5.13-5.96%), so the s016 not-masking finding **stands and is strengthened**: Carvana
is not extending its way out of the DQ print. **No conviction change on the Carvana sub-thesis.**

## 4. 🔧 SEVENTH MEASURE-DESIGN DEFECT — and this one destroyed data before it was caught

**The first run tonight wrote all-blank rows for every deal and overwrote four good EART rows.**

**The failure chain, all three links required:**

1. **EDGAR changed under the instrument.** `index.json` began returning an **incomplete directory
   listing** for these filers — primary document plus index files only, **exhibit absent** — while the
   exhibit itself still resolves **HTTP 200** at its URL and is still correctly typed `EX-99.1` in the
   human `-index.html` document table. Verified: `eart2022-2_exhibit991.htm` → **200, 338,832 bytes**,
   and absent from `index.json`.
2. **A silent fallback substituted the wrong document.** The resolver matched exhibits by *filename
   convention*; with the exhibit unlisted the match went empty and fell through to
   `[n for n in names if n.endswith(".htm") and "index" not in n]` — **the 10-D wrapper, which has no
   data table.** Every field missed.
3. **Last-write-wins let the failure supersede good data.** The s018 upsert fix was built so a re-parse
   after a parser fix supersedes rather than accumulates. **It assumes the newest write is the better
   one. A failed parse also wins.** Four good EART rows (14.83/26.59, 14.08/27.86, 11.81/22.48,
   10.81/17.22) became blanks.

**⚠ The positive control passed through all of it.** It re-parses a **frozen local exhibit**, so it
validates the **parser** and is structurally blind to a **resolution** fault. **A control that holds
its input fixed cannot detect a fault in how inputs are chosen** — and its PASS is actively harmful
here, because it certifies the run.

**Fixes shipped (`scripts/panel_10d.py`):**
- Resolve the exhibit from the `-index.html` document table keyed on the **declared type** (`EX-99.*`),
  not on a filename convention; `index.json` heuristic demoted to fallback.
- **The wrapper fallback is deleted.** An unresolved exhibit now **raises**. Substituting a different
  document silently is what caused the loss.
- **Parse-failure guard:** a row resolving **zero of five** headline metrics is a parse failure, not a
  partial read — it is reported and **dropped, never upserted**, so the good row on disk survives.

**Evidence the fix is sound rather than merely quiet:** post-fix run recovers all 9 deals (BLAST had
been throwing `RuntimeError`), control **PASS**, and the four EART June values **reproduce the
committed ones exactly**.

**The transferable lesson:** the s018 upsert was a correct fix that **relocated a constraint** — it
solved duplicate accumulation and created a supersession hazard, and nothing in the run's own output
distinguished "newer" from "better." *(Auto-memory:
`[[finding_a_fix_can_relocate_a_constraint_and_report_it_removed]]`,
`[[finding_instrument_reports_clean_against_the_wrong_reference]]`.)*

## 5. Consequences

- **CARL:** answered same night, pre-grade — **do not fire the V2 two-tier reversal**; not two-tier
  (deep unobservable in July) and not sustained (n=1 month). V2 holds 4. Instrument defect disclosed.
- **OTTO-35 / SDT:** the ~Nov 15 quarterly re-run reads Exeter recovery, unaffected by the broad-tier
  turn. **No re-arm.**
- **Blind spot named:** **SDART publishes no extension fields at all**, so the panel has extension
  coverage on Exeter and Bridgecrest and none on the broad tier. CARL's AMCAR `{127}` Extension Rate
  (KB-CARL-395) is the free primary substitute — **pool-normalize it; raw dollars fall on an amortizing
  pool and give a confident backwards answer.**

---

## 6. Addendum (same session) — the 60+ definition was reconciled, and CARL supplied a cross-check series

**The panel was internally inconsistent and is now fixed** — Bridgecrest read the issuer's stated aggregate
while Exeter and Santander summed buckets. All three shelves disclose an issuer-stated 60+ aggregate tested
against that deal's own Delinquency Trigger (**SDART `{79}` vs `{80}` 24.00% · EART `{102}` vs `{103}` 40.00%
· BLAST `(55)` vs `(56)` 50.00%), now canonical on every shelf. Gap: Santander **+0.62 to +0.73pp**, Exeter
**+0.01pp**. **Direction unaffected** (2022-6 Jun→Jul: −0.34pp buckets, −0.39pp on `{79}`). Detail → ML-OTTO-246.

⚠ **Owed: a `--history` rebuild.** Only the latest filing row per deal is on the new basis; historical rows
remain bucket-basis. **No level series may cross that boundary until the rebuild lands.**

**CARL's independent same-basis series, for checking that rebuild** *(their pull is entirely issuer-stated on
both tiers, taking EART from the label rather than summing buckets; different vintages from OTTO's four, so it
is additional coverage rather than a duplicate)* — **by COLLECTION MONTH:**

| Deal | Dec | Jan | Feb | Mar | Apr | May | Jun |
|---|---|---|---|---|---|---|---|
| EART 2025-3 | 6.21 | 7.14 | 6.45 | **6.00** | 6.44 | 7.36 | 8.07 |
| EART 2025-4 | 4.47 | 5.45 | 5.37 | 5.28 | 5.43 | 6.12 | 6.76 |
| EART 2025-5 | — | 3.84 | 4.12 | 4.43 | 4.82 | 5.44 | 6.07 |
| EART 2026-1 | — | 0.06 | 1.54 | 2.99 | 3.71 | 4.32 | 5.12 |
| SDART 2022-6 `{79}` | — | — | — | — | — | 10.79 | 11.18 *(Jul 10.79)* |

**Treat as a cross-check, not as truth** (CARL's own framing): **a disagreement would indicate a parser fault
on one side rather than a basis difference**, and is worth chasing on that basis.

⚠ **Note for the rebuild:** CARL cites EART's aggregate as **`{103}` "Delinquency Rate as of the end of the
Collection Period"**, while OTTO's extraction on the 2022-2 exhibit reads **`{102}` 14.84% followed by `{103}`
Delinquency Trigger 40.00%**. **Field INDICES differ across deal templates** — which is exactly why OTTO's
pattern is keyed on the **label**, not the number. Do not hard-code an index during the rebuild.

**The trough re-dates to MARCH on collection months** (CARL, EART 2025-3: Mar 6.00 trough → Jun 8.07). That is
independent corroboration that reading this panel on **filing** dates shifts the trough by a month.

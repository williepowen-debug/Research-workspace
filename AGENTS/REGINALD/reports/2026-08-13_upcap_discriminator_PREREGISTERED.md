# UP-CAP MIGRATION — DISCRIMINATOR, PRE-REGISTERED BEFORE LOOKING

**Written 2026-08-13, BEFORE any secured-CRE figure was pulled or computed.** Will-ruled slate item #5: *"Pre-register the discriminator BEFORE looking."* The MI3-vs-total-loans growth table already existed (it is what raised the question); **the secured-CRE leg below has not been computed at the time of writing, and it is the leg that decides the verdict.**

## The question
At 2026Q2 the MI3 *ratio* screen emptied out while MI3 *dollars* grew fast at several large banks. **Is that growth relabeling (bear), a real business-line mix shift (neutral), or an acquired/expanding book (benign)?**

## Instruments (all from the cached FFIEC facsimiles — no new pull, no new source)
| Quantity | MDRM (RCON, RCFD fallback per the 031/041 resolver) |
|---|---|
| **MI3** (CRE-purpose, NOT secured by RE) | `2746` |
| **Secured CRE** (construction+land 1.a + multifamily 1.d + nonfarm-nonres 1.e) | `F158 + F159 + 1460 + F160 + F161` |
| Total loans & leases | `2122` |
| Total assets (M&A-scale tell) | `2170` |
| C&I item 4 / item 9 | as in `mi3_cohort_screen.py` |

Window: **2025Q2 → 2026Q2 (YoY)**, the same window as the finding.

## ★ THE DISCRIMINATOR — classes are checked in this order, first match wins

1. **`SMALL-BASE — NOT SCORED`** if MI3 at 2025Q2 < **$150M**. A percentage off a small base exaggerates; the bank is reported but **its growth rate is not classified**. *(Named in advance because I already know BKU starts at $81M and I do not want its +193.5% doing work it cannot support.)*
2. **`RELABEL-SIGNATURE` (bear)** if **g_MI3 > 0 AND g_secCRE < 0** — the unsecured CRE-purpose book grows while the **secured** CRE book shrinks in the same bank over the same window. Magnitude qualifier: **(g_MI3 − g_secCRE) ≥ 20pp**.
3. **`BOOK-EXPANSION / ACQUISITION` (benign)** if **g_assets ≥ 15%** (M&A-scale balance-sheet growth) **OR** **(g_MI3 − g_loans) ≤ 10pp** (MI3 simply grew with the book).
4. **`MIX-SHIFT` (neutral)** if **(g_MI3 − g_loans) > 10pp AND g_secCRE > 0** — both books growing, MI3 faster: real business-line growth in unsecured CRE-purpose lending, not substitution.
5. **`NO CLEAN SIGNAL`** otherwise, or wherever two classes both have a claim.

## What each verdict licenses — stated now, so it cannot be stretched later
- **RELABEL-SIGNATURE is a FLAG, not a finding.** It is consistent with relabeling and also with a bank de-risking its secured book while growing a genuinely different line. It licenses **one thing**: pulling that bank's own disclosure. It does **not** license a bear call, a matrix re-score, or a packet asserting relabeling.
- **BOOK-EXPANSION / MIX-SHIFT** close the question for that name.
- **`NO CLEAN SIGNAL` is an acceptable overall verdict** (Will-ruled) and I will report it as the headline if that is what comes back. It is not a weak bear read.

## Known limits, declared in advance
- **The Call Report cannot distinguish relabeling from origination.** Both appear as MI3 growth. The discriminator is **circumstantial**, resting on the *co-movement* of the secured book — that is its whole logic and its whole weakness.
- **n = 14 banks, one window.** No base rate. A signature appearing at 2-3 names is a lead, not a rate.
- **Acquisitions distort every leg simultaneously** (assets, loans, secured CRE and MI3 all jump), which is exactly why the g_assets ≥ 15% test is checked *before* the mix-shift test.
- ⚠️ **V1a ≠ V1 fence still holds**: MI3 is CRE *not secured* by RE throughout. The secured-CRE series is used **only** as a co-movement control — it is never added to MI3 and never presented as a hidden-CRE figure.

*— REGINALD, 2026-08-13, pre-registration. Results → `2026-08-13_upcap_decomposition.md`.*

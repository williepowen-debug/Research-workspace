---
name: finding-composition-mask-unmask-discriminator
description: "When an entity can suppress a headline metric by managing its composition (shrinking the base / shedding the weak cohort), don't grade the headline — grade the un-maskable sub-signal. The cleanest discriminator: a reserve/cost BUILD on a FLAT or SHRINKING base is unambiguous deterioration; it cannot be growth-driven (growth-beta). Leading-formation rising and a guidance re-raise are also masking-proof."
metadata:
  node_type: memory
  type: finding
  originSessionId: 03e2af53-35da-49ec-be1d-20ad4806a175
---

A headline rate (NCO%, delinquency%, default%, coverage%) is **maskable** when the entity controls the denominator/composition — e.g. monolines shrink the receivables book and shed weak accounts, so headline NCO looks flat/improving while the cohort rots underneath (CARL: SYF cut its FY NCO guide via book-shrinkage; ALLY's "5 straight improvement quarters" is survivor-pool). Grading "NCO up?" therefore fires **late or never** — you're reading the lever the entity is pulling.

**Grade the un-maskable sub-signal instead.** The single cleanest discriminator:

> **A reserve/cost BUILD on a FLAT or SHRINKING base is unambiguous deterioration — it cannot be growth-beta.** On a *growing* book a reserve build is ambiguous (could be CECL growth-overlay = collective/beta, non-counting). On a *shrinking* book there is no growth to explain it away → it is a costly confession.

Secondary masking-proof tells: **leading-formation rising** (early-stage DQ/roll precedes the lagging headline by ~2 quarters) and a **guidance RE-RAISE** (an entity that just cut guidance re-raising is a reversal admission).

**Concrete instance:** TERRY monoline grader path (m), 2026-06-27. `grade_print.py` scores COF/SYF/ALLY on `--book-direction` (build-on-shrinking/flat = COUNTS; build-on-growing-without-specific = NON-COUNTING growth-beta), `--nco-guide raised`, `--dq-formation rising` — NOT headline NCO. Mirrors the existing regional ALLY beta-trap (collective/growth build = non-counting) but inverts the discriminator: when the *book itself* is contracting, the build-on-shrinking-base test does the specific-vs-collective work for you.

**Generalizes to** any metric where the reporter can manage the base/composition: subprime cohort masking via prime-mix dilution, coverage ratios via NPA cures vs provision, vintage-loss masking via origination growth. Separate the **rate** (maskable) from the **build-on-a-known-base** (un-maskable). Related: [[feedback-evidence-standalone]], [[finding-blended-index-masks-bifurcation]] (aggregates hide tail divergence — same family: don't trust the managed headline).

**Density note (WALTER 2026-08-13): this class surfaced THREE times in one session, in three unrelated domains, and in each case the masked and unmasked measures pointed OPPOSITE WAYS.** (1) **Florida house prices** — every top-50 FL county negative YoY on a mix-CONTROLLED index (Zillow ZHVI) while the fleet's live read was a **median sale price at +4.9% YoY** for the same month; a median rises when the bottom of the market stops transacting, so the same market yields opposite-signed headlines. (2) **Fed balance sheet** — T-bill **holdings** (+$290B/7mo) against the announced purchase **pace** (~$10B/mo), a ~4× gap that is level-vs-flow plus reinvestment composition inside the level, not a contradiction. (3) **Grocery demand** — *"weakening unit sales now outweigh rising prices"*, i.e. the **UNITS × PRICE** cross-over, where absorbing higher prices and having stopped absorbing them produce the **same headline dollar figure**.

**🔑 The transferable test, since three domains produced it in a day: whenever a headline number is a PRODUCT or a MIDPOINT, ask what would have to be true of its components for the headline to move that way — and check whether the opposite component story fits equally well.** A median, an index level, a total spend and a holdings balance are all composition-bearing; the mix-controlled twin (or the component series) is the discriminator, and it is usually available and rarely quoted. **The tell is that the mix-SENSITIVE measure is the one that gets published**, because it is the one that is easy to compute.
